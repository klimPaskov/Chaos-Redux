"""Task-specific source interpreter and exact migration preservation checks.

This models intended pre-migration macro substitution and migrated boolean calls.
It does not execute the HOI4 parser or prove runtime temporary-variable lifetime.
"""
import copy
import hashlib
import json
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
BACKUP = HERE.parent / 'pre_patch_repression_parameters'
DEST = HERE / 'candidates'
if '--live' in sys.argv:
    DEST = ROOT
TOKEN = re.compile(r'"(?:\\.|[^"\\])*"|[^\s={}<>]+|[={}<>]')

def parse(text):
    ts = TOKEN.findall(re.sub(r'#[^\r\n]*', '', text.lstrip('\ufeff')))
    pos = 0
    def block(close=False):
        nonlocal pos
        out = []
        while pos < len(ts) and ts[pos] != '}':
            key, op = ts[pos:pos+2]
            pos += 2
            assert op in ['=', '<', '>'], (key, op)
            value = ts[pos]
            pos += 1
            if value == '{':
                value = block(True)
            out.append((key, op, value))
        if close:
            assert ts[pos] == '}'
            pos += 1
        return out
    result = block()
    assert pos == len(ts)
    return result

def definitions(folder, rel):
    return {k:v for k,op,v in parse((folder / rel).read_text(encoding='utf-8-sig'))}

CONSTANTS = definitions(ROOT, 'common/script_constants/camp_repression_site_cost_constants.txt')['camp_site_cost']
CONSTANTS = {k:Decimal(v) for k,op,v in CONSTANTS if k != 'schema'}
TRIG = 'common/scripted_triggers/camp_repression_site_cost_triggers.txt'
EFF = 'common/scripted_effects/camp_repression_site_cost_effects.txt'

class Model:
    def __init__(self, folder, states, country, selected):
        self.defs = definitions(folder, TRIG) | definitions(folder, EFF)
        self.states = states
        self.country = copy.deepcopy(country)
        self.temp = {'camp_site_cost_state_id': Decimal(selected)}
        self.native_effects = []
        self.state = None
        self.argument = selected
    def value(self, token):
        try:
            return Decimal(token)
        except Exception:
            pass
        if token.startswith('constant:camp_site_cost.'):
            return CONSTANTS[token.split('.')[-1]]
        if token.startswith('building_level@'):
            assert self.state is not None
            return Decimal(self.states[self.state][token.split('@')[1]])
        if token in self.temp:
            return self.temp[token]
        if token == 'manpower_k':
            return self.country.get('manpower', Decimal(0)) / 1000
        return self.country.get(token, Decimal(0))
    def run(self, body):
        for key,op,data in body:
            if key in self.defs:
                if not self.run(self.defs[key]):
                    return False
            elif key in ['$STATE$', 'var:camp_site_cost_state_id']:
                sid = self.argument if key == '$STATE$' else int(self.temp['camp_site_cost_state_id'])
                if sid not in self.states:
                    raise ValueError('Runtime behavior for absent state pointers is unresolved')
                old = self.state
                self.state = sid
                assert self.run(data)
                self.state = old
            elif key in ['set_temp_variable', 'add_to_temp_variable', 'multiply_temp_variable', 'set_variable']:
                var,_,token = data[0]
                assert len(data) == 1
                value = self.value(token)
                if key == 'set_variable':
                    self.country[var] = value
                elif key == 'set_temp_variable':
                    self.temp[var] = value
                elif key == 'add_to_temp_variable':
                    self.temp[var] += value
                else:
                    self.temp[var] *= value
            elif key == 'round_temp_variable':
                self.temp[data] = self.temp[data].quantize(Decimal(1), rounding=ROUND_HALF_UP)
            elif key == 'clamp_temp_variable':
                fields = {k:v for k,op,v in data}
                assert set(fields) == {'var', 'min'}
                self.temp[fields['var']] = max(self.temp[fields['var']], self.value(fields['min']))
            elif key == 'check_variable':
                if len(data) == 1:
                    var,cmp,val = data[0]
                    left,right = self.value(var),self.value(val)
                    result = {'=':left == right, '<':left < right, '>':left > right}[cmp]
                else:
                    fields = {k:v for k,op,v in data}
                    assert fields['compare'] == 'greater_than_or_equals'
                    result = self.value(fields['var']) >= self.value(fields['value'])
                if not result:
                    return False
            elif key == 'if':
                assert data[0][0] == 'limit'
                if self.run(data[0][2]):
                    assert self.run(data[1:])
            elif key == 'always':
                assert data == 'yes'
            elif key in ['add_political_power', 'add_manpower', 'add_command_power']:
                resource = {'add_political_power':'political_power', 'add_manpower':'manpower', 'add_command_power':'command_power'}[key]
                amount = self.value(data)
                self.country[resource] = self.country.get(resource, Decimal(0)) + amount
                self.native_effects.append((resource, amount))
            elif key == 'add_equipment_to_stockpile':
                fields = {k:v for k,op,v in data}
                resource = 'num_equipment@' + fields['type']
                amount = self.value(fields['amount'])
                self.country[resource] = self.country.get(resource, Decimal(0)) + amount
                self.native_effects.append((resource, amount))
            elif key == 'clear_variable':
                self.country.pop(data, None)
            else:
                raise AssertionError(('Unsupported source operation', key, op, data))
        return True
    def call(self, name):
        return self.run(self.defs[name])

def migrate_checks():
    manifest = json.loads((HERE / 'migration_manifest.json').read_text())
    for item in manifest['protected']:
        assert hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest() == item['sha256'], 'Protected file changed: ' + item['path']
    details = []
    for item in manifest['files']:
        rel = item['path']
        before = (BACKUP / rel).read_bytes()
        after = (DEST / rel).read_bytes()
        assert hashlib.sha256(before).hexdigest() == item['before_sha256']
        assert hashlib.sha256(after).hexdigest() == item['candidate_sha256']
        if rel.endswith('.md'):
            continue
        original = before.decode('utf-8')
        edited = after.decode('utf-8')
        reverse = edited.replace('var:camp_site_cost_state_id = {', '$STATE$ = {')
        rows = manifest['calls'][rel]
        for row in rows:
            assert row['after_line'] in reverse
            reverse = reverse.replace(row['after_line'], row['before_line'], 1)
        assert parse(reverse) == parse(original), rel
        after_tree = parse(edited)
        calls = []
        def walk(block):
            for i,(k,op,v) in enumerate(block):
                if re.fullmatch(r'camp_rework_(?:prepare_site_cost_quote|(?:can_pay|pay)_site_\w+)', k) and v == 'yes':
                    calls.append(k)
                    if not rel.endswith(('camp_repression_site_cost_effects.txt','camp_repression_site_cost_triggers.txt')):
                        if i and block[i-1][0] == 'set_temp_variable':
                            assert block[i-1][2][0][0] == 'camp_site_cost_state_id'
                        else:
                            assert rel.endswith('camp_repression_ledger_scripted_localisation.txt')
                if isinstance(v,list):
                    if k == 'NOT' and any(a.startswith('camp_rework_can_pay_site_') for a,_,_ in v):
                        assert i and block[i-1][0] == 'set_temp_variable'
                        assert len(v) == 1
                    if k == 'OR':
                        assert not any(a == 'set_temp_variable' and b[0][0] == 'camp_site_cost_state_id' for a,_,b in v)
                    walk(v)
        walk(after_tree)
        assert len(calls) == len(rows)
        details.append({'file':rel,'calls':len(calls),'unrelated_AST_unchanged':True})
    return details

def scenarios():
    cases = []
    levels = [(0,0,0),(1,0,0),(5,0,0),(0,0,3),(2,1,2),(0,1,0)]
    buildings = ['concentration_camp','extermination_camp','gulag_labor_camp_network']
    for index, values in enumerate(levels):
        sid = index + 1
        state = {sid:dict(zip(buildings,values))}
        for action in ['labor','inspect','dismantle','evidence','restricted']:
            quote_name = 'camp_rework_prepare_site_cost_quote'
            gate_name = 'camp_rework_can_pay_site_' + action
            pay_name = 'camp_rework_pay_site_' + action
            rich = {key:Decimal(1000000) for key in ['political_power','manpower','command_power','num_equipment@motorized_equipment_1','num_equipment@train_equipment_1','num_equipment@support_equipment_1']}
            models = [Model(p,state,rich,sid) for p in [BACKUP,DEST]]
            for model in models:
                assert model.call(quote_name)
                assert model.call(gate_name)
                assert model.call(pay_name)
            assert models[0].temp == models[1].temp
            assert models[0].country == models[1].country
            assert models[0].native_effects == models[1].native_effects
            debits = models[1].native_effects
            assert len(debits) == len(set(key for key,value in debits)), 'Duplicate debit'
            threshold = {key:-amount for key,amount in debits}
            if action == 'labor':
                for equipment, label in [('motorized_equipment_1','motorized'),('train_equipment_1','trains'),('support_equipment_1','support')]:
                    threshold['num_equipment@'+equipment] += models[1].temp['camp_site_quote_labor_'+label+'_reserve']
            for folder in [BACKUP,DEST]:
                exact = Model(folder,state,threshold,sid)
                assert exact.call(gate_name)
                for resource in threshold:
                    short = threshold.copy()
                    short[resource] -= Decimal(1)
                    assert not Model(folder,state,short,sid).call(gate_name), (values,action,resource)
                exact.call(pay_name)
                if action == 'labor':
                    for resource in ['motorized','trains','support']:
                        name = 'generic_labor_project_'+resource+'_reserve'
                        assert exact.country[name] == exact.temp['camp_site_quote_labor_'+resource+'_reserve']
                    exact.call('camp_rework_clear_site_labor_reserve')
                    assert not any(k.startswith('generic_labor_project_') for k in exact.country)
            cases.append({'levels':values,'action':action,'payments':debits,'exact_gate':True,'single_resource_shortages_rejected':list(threshold),'single_debit_each':True,'before_after_equal':True})
    states = {1:dict(zip(buildings,(1,0,0))),2:dict(zip(buildings,(0,0,5)))}
    model = Model(DEST,states,{},1)
    outputs = []
    for sid in [1,2,1,2]:
        model.temp['camp_site_cost_state_id'] = Decimal(sid)
        assert model.call('camp_rework_prepare_site_cost_quote')
        outputs.append(model.temp['camp_site_quote_inspect_pp'])
    assert outputs == [Decimal(13),Decimal(25),Decimal(13),Decimal(25)]
    return cases, outputs

if __name__ == '__main__':
    details = migrate_checks()
    cases, outputs = scenarios()
    result = {'method':'Strict interpreter of the actual before and candidate quote/gate/payment ASTs, modeling intended pre-migration substitution, Decimal nearest rounding, and shared unscoped temporaries. Not a HOI4 engine run.', 'source_preservation':details,'scenarios':cases,'repeated_state_ids':[1,2,1,2],'repeated_inspection_pp':outputs,'runtime_limits':['Engine parsing and temporary lifetime across helper/limit/localisation contexts remain parent-owned.','Missing or invalid dynamic state pointers have no invented model behavior or fallback.','MCP fixtures supply presentation values and do not execute quote or payment logic.']}
    result['source'] = 'live' if DEST == ROOT else 'candidate'
    (HERE / ('source_validation_live.json' if DEST == ROOT else 'source_validation.json')).write_text(json.dumps(result,indent=2,default=str)+'\n',encoding='utf-8')
    print('Verified 114 call mappings, eight preserved ASTs, 30 quote/gate/payment boundary cases, reserve save/clear, and repeated state inputs.')
