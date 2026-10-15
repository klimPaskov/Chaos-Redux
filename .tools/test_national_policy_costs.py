"""Run ``python .tools/test_national_policy_costs.py`` from the repository root.

Reads current national-policy and Black Friday helpers, modifiers and constants.
Writes source hashes and scenario results to .tmp/national_policy_panels/.
Needs only Python's standard library and current repo source, with no snapshots.
This bounded interpreter checks source behavior, not native rounding, tooltips,
affordability quantization, observed PP debit, or HOI4 execution.
"""
from pathlib import Path
from decimal import Decimal
import re
import json
import hashlib

ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r'#[^\n]*|"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>]+')

def parse(text):
    tokens = [t for t in TOKEN.findall(text) if not t.startswith('#')]
    def block(i):
        out = []
        while i < len(tokens) and tokens[i] != '}':
            key = tokens[i]
            if i + 1 == len(tokens) or tokens[i + 1] not in ('=', '<', '>'):
                out.append((key, '=', key)); i += 1; continue
            op, value = tokens[i + 1:i + 3]; i += 3
            if value == '{': value, i = block(i)
            out.append((key, op, value))
        return out, i + (i < len(tokens))
    return block(0)[0]

def load(rel): return parse((ROOT / rel).read_text(encoding='utf-8-sig'))
def find(nodes, key): return next(v for k, _, v in nodes if k == key)

FILES = ['common/scripted_effects/national_policy_cost_effects.txt',
         'common/scripted_effects/026_black_friday_native_sale_effects.txt',
         'common/scripted_effects/026_black_friday_effects.txt',
         'common/dynamic_modifiers/national_policy_cost_modifiers.txt',
         'common/dynamic_modifiers/026_black_friday_dynamic_modifiers.txt']
EFFECTS = {k: v for rel in FILES[:3] for k, _, v in load(rel)}
MODS = {k: v for rel in FILES[3:] for k, _, v in load(rel)}
CONSTANTS = {}
for path in (ROOT / 'common/script_constants').glob('*.txt'):
    for category, _, body in parse(path.read_text(encoding='utf-8-sig')):
        if not isinstance(body, list): continue
        for key, _, val in body:
            if isinstance(val, str):
                try: CONSTANTS[f'constant:{category}.{key}'] = Decimal(val)
                except Exception: pass

WAR = ['chemical_use_policy', 'biological_use_policy', 'nuclear_use_policy']
CIV = ['refugee_reception', 'civilian_departure']
SLOTS = CIV + WAR

class World:
    def __init__(self, doctrine=False, sale=False, ratio=5000, external=0):
        self.vars = {'global.black_friday_discount_ratio': Decimal(ratio), 'political_power': Decimal(500)}
        self.frames = [{}]
        self.flags = {'black_friday_active'} if sale else set()
        self.bindings = set()
        self.doctrine = doctrine
        self.external = {f'{s}_cost_factor': Decimal(str(external)) for s in SLOTS}
        self.modifiers = dict(self.external)
        self.ideas = set()
        self.credits = []

    def value(self, token):
        try: return Decimal(token)
        except Exception: pass
        if token.startswith('constant:'): return CONSTANTS[token]
        if token.startswith('modifier@'): return self.modifiers.get(token[9:], Decimal(0))
        for frame in reversed(self.frames):
            if token in frame: return frame[token]
        return self.vars.get(token, Decimal(0))

    def write(self, key, value, temporary=False):
        if temporary:
            for frame in reversed(self.frames):
                if key in frame: frame[key] = value; return
            self.frames[-1][key] = value
        else: self.vars[key] = value

    def condition(self, nodes):
        answers = []
        for key, op, val in nodes:
            if key in ('AND', 'hidden_trigger'): answer = self.condition(val)
            elif key == 'NOT': answer = not self.condition(val)
            elif key == 'OR': answer = any(self.condition([n]) for n in val)
            elif key == 'has_doctrine': answer = self.doctrine and val == 'chaos_warfare'
            elif key in ('has_global_flag', 'has_country_flag'): answer = val in self.flags
            elif key == 'has_dynamic_modifier': answer = val in self.bindings
            elif key == 'has_idea': answer = val in self.ideas
            elif key in ('black_friday_achievement_is_valid_sale', 'black_friday_engine_purchase_can_credit'): answer = True
            elif key == 'always': answer = val == 'yes'
            elif key == 'check_variable':
                pairs = {k:v for k, _, v in val}
                if 'var' in pairs: lhs, rhs = pairs['var'], pairs['value']; cmp = pairs.get('compare', 'equals')
                else: lhs, cmp, rhs = val[0]
                a,b = self.value(lhs),self.value(rhs)
                answer = {'=': a == b,'equals': a == b,'<': a < b,'less_than': a < b,'>': a > b,'greater_than': a > b}.get(cmp)
                if answer is None: raise AssertionError(cmp)
            else: raise AssertionError(('condition', key))
            answers.append(answer)
        return all(answers)

    def refresh(self):
        self.modifiers = dict(self.external)
        for binding in self.bindings:
            body = MODS[binding]
            enable = next((v for k, _, v in body if k == 'enable'), [])
            if self.condition(enable):
                for key, _, val in body:
                    if key.endswith('_cost_factor'):
                        self.modifiers[key] = self.modifiers.get(key, Decimal(0)) + self.value(val)

    def call(self, name):
        if name == 'black_friday_engine_purchase_count_slots':
            for key in ('black_friday_engine_advisor_count','black_friday_engine_staff_count'):
                self.write(key, Decimal(0), True)
            return
        if name == 'black_friday_add_committed_achievement_family':
            self.credits.append(self.value('black_friday_purchase_family_id')); return
        nodes = EFFECTS[name]
        self.frames.append({})
        self.run(nodes)
        self.frames.pop()

    def run(self, nodes):
        branch = None
        for key, op, val in nodes:
            if key in ('if','else_if','else'):
                take = (key == 'if' or not branch) and (key == 'else' or self.condition(find(val,'limit')))
                if key == 'if': branch = False
                if take:
                    branch = True
                    self.run([n for n in val if n[0] != 'limit'])
                continue
            branch = None
            if key in ('set_country_flag','set_global_flag'): self.flags.add(val)
            elif key in ('clr_country_flag','clr_global_flag'): self.flags.discard(val)
            elif key == 'add_dynamic_modifier': self.bindings.add(find(val,'modifier'))
            elif key == 'remove_dynamic_modifier': self.bindings.discard(find(val,'modifier'))
            elif key == 'force_update_dynamic_modifier': self.refresh()
            elif key in EFFECTS or key in ('black_friday_add_committed_achievement_family',):
                assert val == 'yes', ('unsupported scripted helper argument block',key,val)
                self.call(key)
            elif key == 'clear_variable': self.vars.pop(val,None)
            elif key == 'clamp_temp_variable':
                args = {k:v for k,_,v in val}; name = args['var']; number = self.value(name)
                if 'min' in args: number = max(number,self.value(args['min']))
                if 'max' in args: number = min(number,self.value(args['max']))
                self.write(name,number,True)
            elif key.endswith('_variable'):
                name,_,rhs = val[0]
                number = self.value(rhs)
                if key.startswith('add_to'): number = self.value(name) + number
                elif key.startswith('subtract_from'): number = self.value(name) - number
                elif key.startswith('multiply'): number = self.value(name) * number
                elif key.startswith('divide'): number = self.value(name) / number
                elif not key.startswith('set_'): raise AssertionError(key)
                self.write(name,number,'temp_' in key)
            else: raise AssertionError(('effect',key))

    def prices(self):
        return {s: max(Decimal(0),1+self.modifiers.get(s+'_cost_factor',0))*(100 if s in CIV else 150) for s in SLOTS}

results = []
def check(name, world, sale, doctrine, external=0, ratio=5000):
    expected = {}
    for slot in SLOTS:
        ordinary = max(Decimal(0),1+Decimal(str(external))+(Decimal('-0.25') if doctrine and slot in WAR else 0))
        expected[slot] = ordinary*(100 if slot in CIV else 150)*(Decimal(ratio)/10000 if sale else 1)
    assert world.prices() == expected, (name, world.prices(),expected)
    active = [binding for binding in world.bindings if binding.startswith('national_policy_') and world.condition(next((v for k,_,v in MODS[binding] if k=='enable'),[]))]
    assert len(active) == int(sale or doctrine), (name,active)
    results.append({'name':name,'prices':{k:str(v) for k,v in expected.items()},'enabled_policy_variants':active})

for external in (0,-0.1,0.2,-0.9,-1.2):
    for doctrine in (False,True):
        w = World(doctrine=doctrine,external=external)
        w.call('national_policy_initialize_cost_modifiers'); check('normal',w,False,doctrine,external)
        w.doctrine = not doctrine; w.refresh(); check('doctrine_toggle_outside_sale',w,False,not doctrine,external)
        for ratio in (5000,2500):
            w = World(doctrine=doctrine,external=external,sale=True,ratio=ratio)
            w.call('national_policy_initialize_cost_modifiers'); check('policy_init_inside_sale',w,True,doctrine,external,ratio)
            w.call('national_policy_initialize_cost_modifiers'); check('policy_init_repeat_inside_sale',w,True,doctrine,external,ratio)
            w.call('black_friday_native_sale_apply'); check('sale_new_country',w,True,doctrine,external,ratio)
            w.call('black_friday_native_sale_apply'); check('sale_repeat_refresh',w,True,doctrine,external,ratio)
            w.doctrine = not doctrine; w.refresh(); check('doctrine_toggle_inside_sale',w,True,not doctrine,external,ratio)
            w.call('black_friday_native_sale_apply'); check('sale_refresh_after_toggle',w,True,not doctrine,external,ratio)
            w.flags.discard('black_friday_active'); w.call('black_friday_native_sale_remove'); check('sale_expiry',w,False,not doctrine,external)
            assert not any(k.startswith('national_policy_sale_') or k.startswith('black_friday_sale_') for k in w.vars)

assert all(not any(k == s+'_cost_factor' for k,_,v in MODS['black_friday_native_sale']) for s in WAR)
assert all(sum(k == s+'_cost_factor' for k,_,v in MODS['black_friday_native_sale']) == 1 for s in CIV)
assert len([n for n in MODS['black_friday_native_sale'] if n[0].endswith('_cost_factor')]) == 582
assert '$' not in (ROOT/FILES[0]).read_text(encoding='utf-8-sig')

options = {
    'refugee_reception':['humanitarian','controlled','transit','quarantine','closed','violent','forced_return'],
    'civilian_departure':['free','permit','prohibited'],
    'chemical_use_policy':['retaliation','battlefield','unrestricted'],
    'biological_use_policy':['retaliation','battlefield','unrestricted'],
    'nuclear_use_policy':['none','retaliation','unrestricted'],
}
prefix = dict(zip(SLOTS,['reception','departure','chemical','biological','nuclear']))
for slot, names in options.items():
    for option in names:
        w = World(sale=True)
        w.ideas.add(f'national_policy_{prefix[slot]}_{option}')
        w.call('black_friday_engine_purchase_snapshot')
        saved = w.vars[f'black_friday_engine_snapshot_{slot}_law']
        w.ideas.clear()
        replacement = names[(names.index(option)+1)%len(names)]
        w.ideas.add(f'national_policy_{prefix[slot]}_{replacement}')
        w.vars['political_power'] -= 1
        w.call('black_friday_engine_purchase_credit')
        assert CONSTANTS['constant:universal_cost_family.laws'] in w.credits, (slot,option,saved)
        assert not any(k.startswith('black_friday_engine_snapshot_') for k in w.vars)
    w = World(sale=True)
    w.ideas.add(f'national_policy_{prefix[slot]}_{names[0]}'); w.call('black_friday_engine_purchase_snapshot')
    w.ideas.clear(); w.ideas.add(f'national_policy_{prefix[slot]}_{names[1]}'); w.call('black_friday_engine_purchase_credit')
    assert not w.credits, (slot,'free change credited')

payload = {'source_semantics_only':True,'native_consumer_unverified':['rounding','tooltip','affordability','debit'],
           'cost_scenarios':results,'law_options_with_paid_change_credit':sum(map(len,options.values())),
           'free_policy_changes_rejected':len(SLOTS),
           'source_sha256':{rel:hashlib.sha256((ROOT/rel).read_bytes()).hexdigest() for rel in FILES}}
output_path = ROOT/'.tmp/national_policy_panels/cost_test_results.json'
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
print(f'{len(results)} cost lifecycle cases, {sum(map(len,options.values()))} paid law-option changes and {len(SLOTS)} free-change rejections passed.')
