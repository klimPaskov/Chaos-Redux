"""Actual Clausewitz source fixture. Run: python docs/testing/event016_private_paleogenetics_20261008/core_source_tests.py
Narrow primitive model, NOT engine proof. Unknown executed commands fail closed.
Only provider validity is an external helper stub; generic quote/debit/receipt bodies execute from current source.
"""
from pathlib import Path
from decimal import Decimal as D
import re, hashlib, json, sys

ROOT = Path(__file__).resolve().parents[3]
P = 'mengele_event016_paleogenetics_'
H = 'brilliant_scientist_mengele_paleogenetics_'
G = 'brilliant_scientist_mengele_'
OWNED = [
'common/script_constants/016_mengele_paleogenetics_deployment_constants.txt',
'common/scripted_triggers/016_mengele_paleogenetics_deployment_triggers.txt',
'common/scripted_effects/016_mengele_paleogenetics_deployment_effects.txt']
SHARED = [
'common/scripted_triggers/016_mengele_computation_incident_triggers.txt',
'common/script_constants/016_brilliant_scientist_directorate_constants.txt',
'common/scripted_effects/016_mengele_conventional_incident_effects.txt',
'common/scripted_triggers/016_mengele_conventional_incident_triggers.txt',
'common/script_constants/016_mengele_project_stage_constants.txt',
'common/script_constants/016_brilliant_scientist_constants.txt',
'common/script_constants/016_brilliant_scientist_project_constants.txt',
'common/scripted_effects/016_mengele_project_stage_effects.txt',
'common/scripted_triggers/016_mengele_project_stage_triggers.txt',
'common/scripted_triggers/016_mengele_paleogenetics_stage_decision_triggers.txt']
def parse(text):
    text = re.sub(r'#[^\n]*', '', text)
    tok = re.findall(r'"[^"]*"|[{}=<>]|[^\s{}=<>]+', text)
    pos = 0
    def block():
        nonlocal pos
        rows = []
        while pos < len(tok) and tok[pos] != '}':
            k = tok[pos]; pos += 1
            if pos == len(tok) or tok[pos] not in ('=', '<', '>'):
                rows.append((k, '=', 'yes')); continue
            op = tok[pos]; pos += 1
            v = tok[pos]; pos += 1
            if v == '{':
                v = block()
                assert tok[pos] == '}'; pos += 1
            rows.append((k, op, v))
        return rows
    result = block()
    assert pos == len(tok), (pos, len(tok))
    return result

defs = {}; constants = {}; snapshots = {}
for rel in OWNED + SHARED:
    raw = (ROOT / rel).read_bytes()
    snapshots[rel] = hashlib.sha256(raw).hexdigest()
    rows = parse(raw.decode('utf-8-sig'))
    if '/script_constants/' in rel:
        for cat, _, entries in rows:
            if isinstance(entries, list):
                for key, _, value in entries:
                    if not isinstance(value, list):
                        try: constants['constant:'+cat+'.'+key] = D(value)
                        except Exception: pass
    else:
        for name, _, entries in rows:
            if isinstance(entries, list): defs[name] = entries

def fields(b): return {k: v for k, _, v in b}
class VM:
    def __init__(self):
        self.scopes = {
            10001: dict(kind='country', flags=set(), v={}, a={}, mods=set(), pp=D(1000), support=D(4000), fuel=D(9000), provider=True, tech=True, cic=D(4)),
            10002: dict(kind='country', flags=set(), v={}, a={}, pp=D(999), support=D(999), fuel=D(999), provider=True, tech=True, cic=D(4)),
            20001: dict(kind='state', flags=set(), v={}, a={}, owner=10001, control=10001, infrastructure=D(2), industrial_complex=D(0), slots=D(3), locked=D(0)),
            20002: dict(kind='state', flags=set(), v={}, a={}, owner=10001, control=10001, infrastructure=D(2), industrial_complex=D(2), slots=D(3), locked=D(0))}
        self.this = 10001; self.prev = 10001; self.root = 10001; self.frm = 20001
        self.t = {}; self.builds = []; self.calls = []; self.build_factor = D(1)
        self.debit_factor = D(1); self.credit_factor = D(1); self.on_build = None; self.on_debit = None
        self.s['flags'].add('mengele_event016_paleogenetics_prototype_completed')
        self.seed()
    @property
    def s(self): return self.scopes[self.this]
    @property
    def owner(self): return self.scopes[10001]
    def seed(self, marker=1):
        self.t.update(mengele_event016_project_family=D(10), mengele_event016_requested_stage=D(3),
                      mengele_event016_stage_started=D(0), mengele_event016_stage_finished=D(0),
                      mengele_event016_stage_cancelled=D(0), mengele_event016_project_output_applied=D(0))
        self.t[P+'native_entry'] = D(marker)
    def scopeval(self, s):
        return {'THIS': self.this, 'PREV': self.prev, 'ROOT': self.root, 'FROM': self.frm}.get(s)
    def split(self, token):
        for prefix, ident in [('ROOT.',self.root), ('PREV.',self.prev), ('THIS.',self.this), ('FROM.',self.frm)]:
            if token.startswith(prefix): return ident, token[len(prefix):]
        return self.this, token
    def val(self, x):
        if x in constants: return constants[x]
        if x.startswith('constant:'): raise AssertionError('missing constant '+x)
        scope = self.scopeval(x)
        if scope is not None: return D(scope)
        try: return D(x)
        except Exception: pass
        if x in self.t: return self.t[x]
        sid, name = self.split(x); s = self.scopes[sid]
        if name == 'political_power': return s.get('pp', D(0))
        if name == 'fuel_k': return s.get('fuel', D(0)) / 1000
        if name == 'num_equipment@support_equipment': return s.get('support', D(0))
        if name == 'num_of_civilian_factories_available_for_projects': return s.get('cic', D(0))
        if name.startswith('building_level@'): return s.get(name.split('@')[1], D(0))
        if name in ('infrastructure','industrial_complex'): return s.get(name, D(0))
        if '^' in name:
            key, ix = name.split('^',1); arr = s['a'].get(key,[])
            if ix == 'num': return D(len(arr))
            idx = int(self.val(ix)); return arr[idx] if 0 <= idx < len(arr) else D(0)
        return s['v'].get(name, D(0))
    def write(self, name, value, temp=False):
        if temp: self.t[name] = value; return
        sid, key = self.split(name); s = self.scopes[sid]
        if '^' in key:
            key, ix = key.split('^',1); idx = int(self.val(ix)); a = s['a'].setdefault(key,[])
            while len(a) <= idx: a.append(D(0))
            a[idx] = value
        else: s['v'][key] = value
    def compare(self, a, b, op):
        return {'equals':a==b,'not_equals':a!=b,'greater_than':a>b,'less_than':a<b,
                'greater_than_or_equals':a>=b,'less_than_or_equals':a<=b, '=':a==b,'>':a>b,'<':a<b}[op]
    def scoped(self, target, b, trigger):
        old, prev = self.this, self.prev
        sid = self.scopeval(target)
        if target.startswith('var:'): sid = int(self.val(target[4:]))
        if sid not in self.scopes: return False
        self.this, self.prev = sid, old
        try: return self.test(b) if trigger else self.run(b)
        finally: self.this, self.prev = old, prev
    def call(self, name, trigger=False):
        self.calls.append(name)
        if name == G+'project_stage_provider_is_valid':
            return self.s.get('provider',False) # Explicit only external helper stub.
        if name == G+'conventional_incident_provider_is_valid':
            return self.s.get('provider',False) # Explicit incident-provider identity stub; dispatcher executes actual source.
        if name not in defs: raise AssertionError('unsupported helper '+name)
        keys = set(self.t)
        try: return self.test(defs[name]) if trigger else self.run(defs[name])
        finally:
            for key in set(self.t)-keys: del self.t[key] # conservative helper-frame cleanup
    def test(self, b): return all(self.testrow(k,op,v) for k,op,v in b)
    def testrow(self, k, op, v):
        if k == 'AND': return self.test(v)
        if k == 'OR': return any(self.testrow(*row) for row in v)
        if k == 'NOT': return not self.test(v)
        if k in ('THIS','ROOT','FROM','PREV') or k.startswith('var:'): return self.scoped(k,v,True)
        if k in defs or k == G+'project_stage_provider_is_valid': return self.call(k,True)
        if k.startswith('set_temp_') or k.startswith('modulo_temp_'):
            self.effect(k,op,v); return True
        if k == 'check_variable':
            f=fields(v)
            if 'var' in f: return self.compare(self.val(f['var']),self.val(f['value']),f.get('compare','equals'))
            a, relation, rhs = v[0]; return self.compare(self.val(a),self.val(rhs),relation)
        if k == 'has_country_flag' or k == 'has_state_flag': return v in self.s['flags']
        if k == 'has_variable': return v in self.s['v']
        if k == 'exists': return (self.this in self.scopes) == (v=='yes')
        if k == 'is_owned_by': return self.s.get('owner') == int(self.val(v))
        if k == 'is_controlled_by': return self.s.get('control') == int(self.val(v))
        if k == 'has_tech': return self.s.get('tech',False)
        if k == 'has_dynamic_modifier': return v in self.s.get('mods',set())
        if k in ('is_special_project_completed','has_dlc'): return False
        if k == 'has_equipment':
            name, relation, amount = v[0]
            if name != 'support_equipment': raise AssertionError('unsupported equipment check '+name)
            return self.compare(self.s['support'],self.val(amount),relation)
        if k == 'has_fuel': return self.compare(self.s['fuel'],self.val(v),op)
        if k == 'free_building_slots':
            f=fields(v); building=f['building']
            n=D(5)-self.s['infrastructure'] if building=='infrastructure' else self.s['slots']
            # slots contains current unlocked unused slots. Locked slots do not count unless requested.
            if f.get('include_locked')=='yes': n += self.s['locked']
            _, relation, amount = next(row for row in v if row[0]=='size')
            return self.compare(n,self.val(amount),relation)
        if k in ('infrastructure','industrial_complex','num_of_civilian_factories_available_for_projects'):
            return self.compare(self.val(k),self.val(v),op)
        raise AssertionError('unsupported tested command '+k+' '+op)
    def run(self, b):
        last=None
        for k,op,v in b:
            if k == 'if':
                last=self.test(fields(v).get('limit',[]))
                if last: self.run([row for row in v if row[0]!='limit'])
            elif k == 'else_if':
                if not last:
                    last=self.test(fields(v).get('limit',[]))
                    if last: self.run([row for row in v if row[0]!='limit'])
            elif k == 'else':
                if last is False: self.run(v)
                last=None
            elif k == 'while_loop_effect':
                limit=fields(v)['limit']; count=0
                while self.test(limit):
                    self.run([r for r in v if r[0]!='limit']);count+=1
                    assert count<=1000
            elif k in ('THIS','ROOT','PREV','FROM') or k.startswith('var:'): self.scoped(k,v,False)
            elif k in defs: self.call(k)
            else: self.effect(k,op,v)
        return True
    def effect(self,k,op,v):
        if k == 'force_update_dynamic_modifier': return
        if k == 'add_dynamic_modifier': self.s.setdefault('mods',set()).add(fields(v)['modifier']);return
        if k in ('set_country_flag','set_state_flag'): self.s['flags'].add(v); return
        if k in ('clr_country_flag','clr_state_flag'): self.s['flags'].discard(v); return
        if k == 'clear_variable': self.s['v'].pop(v,None); return
        if k == 'clear_array': self.s['a'].pop(v,None); return
        if k == 'add_to_array':
            f=fields(v);self.s['a'].setdefault(f['array'],[]).append(self.val(f['value']));return
        if k in ('set_variable','add_to_variable','subtract_from_variable','multiply_variable',
                 'set_temp_variable','add_to_temp_variable','subtract_from_temp_variable','multiply_temp_variable','modulo_temp_variable'):
            f=fields(v);name=f.get('var',v[0][0]);rhs=f.get('value',v[0][2]);amount=self.val(rhs)
            current=self.val(name)
            if k.startswith('add_'): amount=current+amount
            elif k.startswith('subtract_'): amount=current-amount
            elif k.startswith('multiply_'): amount=current*amount
            elif k.startswith('modulo_'): amount=current%amount
            self.write(name,amount,'temp' in k);return
        if k in ('add_political_power','add_fuel','add_equipment_to_stockpile'):
            amount=self.val(fields(v)['amount']) if isinstance(v,list) else self.val(v)
            resource={'add_political_power':'pp','add_fuel':'fuel','add_equipment_to_stockpile':'support'}[k]
            if isinstance(v,list): assert fields(v)['type']=='support_equipment'
            self.s[resource] += amount*(self.debit_factor if amount<0 else self.credit_factor)
            if amount<0 and self.on_debit: self.on_debit(self,k)
            return
        if k == 'add_building_construction':
            f=fields(v);building=f['type'];amount=self.val(f['level'])
            self.builds.append((self.this,building,amount))
            self.s[building]+=amount*self.build_factor
            if building=='industrial_complex': self.s['slots']-=amount*self.build_factor
            if self.on_build: self.on_build(self,k)
            return
        raise AssertionError('unsupported effect '+k)

def choose(v):
    v.frm=20001;v.call(H+'select_reserve')
    v.frm=20002;v.call(H+'select_hatchery')
def begun():
    v=VM();choose(v);v.seed();v.call(G+'begin_project_stage')
    assert v.t['mengele_event016_stage_started']==1
    assert v.owner['pp']==870 and v.owner['support']==3025 and v.owner['fuel']==7500
    return v
def finish(v):
    v.seed(marker=0);v.call(G+'finish_project_stage')
def cancel(v):
    v.seed(marker=0);v.call(G+'cancel_project_stage')
def flag(v,n): return P+n in v.owner['flags']
def row(v): return v.owner['a'].get('mengele_event016_active_project_stage_entries',[0]*10)[9]
def completed(v): return 'mengele_event016_paleogenetics_deployment_completed' in v.owner['flags']
cases=0
def case(name,fn):
    global cases
    fn(); cases+=1; print('PASS '+name)

def assert_full(v):
    assert completed(v) and row(v)==0 and not flag(v,'deployment_pending')
    assert len(v.builds)==2 and v.call(H+'deployment_outputs_are_complete',True)
    assert v.owner['v'][P+'reserve_post']==3 and v.owner['v'][P+'hatchery_post']==3
def full():
    v=begun();finish(v);assert_full(v)
    assert 'brilliant_scientist_paleogenetics_deployment' in v.owner['mods']
    assert v.calls.count(G+'reconcile_project_availability')==1
    assert v.calls.count(G+'dispatch_conventional_incident')==1
    before=(list(v.builds),v.owner['pp'],v.owner['support'],v.owner['fuel'])
    finish(v);cancel(v);v.call(H+'recover_deployment')
    assert before==(v.builds,v.owner['pp'],v.owner['support'],v.owner['fuel'])
case('full success/durable close/repeated finish cancel recovery',full)
def no_marker():
    v=VM();choose(v);v.seed(0);before=dict(v.owner['v']);v.call(H+'begin_deployment')
    assert v.t['mengele_event016_stage_started']==0 and v.owner['pp']==1000 and v.owner['v']==before
case('bare begin no marker preserves records',no_marker)
for resource,threshold in [('pp',130),('support',975),('fuel',1500)]:
    for delta in [-1,0,1]:
        def boundary(resource=resource,threshold=threshold,delta=delta):
            v=VM();choose(v);v.owner[resource]=D(threshold+delta);v.seed();v.call(H+'begin_deployment')
            assert bool(v.t['mengele_event016_stage_started'])==(delta>=0)
            assert v.t[P+'native_entry']==0
            if delta<0: assert not flag(v,'deployment_pending') and P+'deployment_actor' not in v.owner['v']
        case(resource+' below/exact/above '+str(delta),boundary)
def reserved():
    v=VM();choose(v);v.owner['cic']=D(0);v.seed();v.call(H+'begin_deployment')
    assert v.t['mengele_event016_stage_started']==1
case('native reserved CIC zero after source admission',reserved)
def duplicate():
    v=begun();before=dict(v.owner['v']);v.seed();v.call(H+'begin_deployment')
    assert v.owner['v']==before and v.owner['pp']==870 and v.t[P+'native_entry']==0
case('duplicate entry consumes marker without overwriting paid proof',duplicate)
for defect in ['same','reservefull','hatcheryfull','futurepenfull','locked','control','owner','infra']:
    def invalid(defect=defect):
        v=VM();choose(v)
        if defect=='same':v.owner['v'][P+'selected_hatchery']=D(20001)
        elif defect=='reservefull':v.scopes[20001]['infrastructure']=D(5)
        elif defect=='hatcheryfull':v.scopes[20002]['slots']=D(0)
        elif defect=='futurepenfull':v.scopes[20002]['infrastructure']=D(5)
        elif defect=='locked':v.scopes[20002]['slots']=D(0);v.scopes[20002]['locked']=D(5)
        elif defect=='control':v.scopes[20002]['control']=10002
        elif defect=='owner':v.scopes[20001]['owner']=10002
        elif defect=='infra':v.scopes[20001]['infrastructure']=D(0)
        v.seed();v.call(H+'begin_deployment')
        assert v.t['mengele_event016_stage_started']==0 and not flag(v,'deployment_pending')
    case('invalid selection '+defect,invalid)
def free():
    v=VM();choose(v);assert len(v.builds)==0 and v.owner['pp']==1000
    v.call(H+'clear_selection');assert P+'selected_reserve' not in v.owner['v']
    choose(v);v.seed();v.call(H+'begin_deployment');paid=dict(v.owner['v'])
    v.call(H+'clear_selection');v.frm=20001;v.call(H+'select_hatchery');assert v.owner['v']==paid
case('free selection reset then frozen selection guard',free)
def foreign():
    v=VM();v.root=10002;choose(v);v.seed();v.call(H+'begin_deployment');finish(v)
    assert_full(v);assert v.scopes[10002]['pp']==999
case('foreign outer ROOT uses THIS payer and PREV state owner',foreign)
def external():
    v=begun();v.scopes[20001]['infrastructure']=D(4);v.scopes[20002]['industrial_complex']=D(7)
    finish(v);assert completed(v) and v.owner['v'][P+'reserve_pre']==4 and v.owner['v'][P+'hatchery_pre']==7
    assert v.owner['v'][P+'reserve_post']==5 and v.owner['v'][P+'hatchery_post']==8
case('rival construction changes attempt baseline not paid quantity',external)
def partial():
    v=begun();v.scopes[20002]['slots']=D(0);finish(v)
    assert len(v.builds)==1 and row(v)==3 and flag(v,'deployment_pending') and not completed(v)
    assert not v.call(H+'recovery_is_ready',True)
    cancel(v);assert row(v)==3 and v.owner['pp']==870
    v.scopes[20002]['slots']=D(1);assert v.call(H+'recovery_is_ready',True)
    v.call(H+'recover_deployment');assert_full(v)
case('partial capacity blocked cancel retains payment then one-component recovery',partial)
def bothfull():
    v=begun();v.scopes[20001]['infrastructure']=D(5);v.scopes[20002]['slots']=D(0);finish(v)
    assert not v.builds and not completed(v) and not v.call(H+'recovery_is_ready',True)
    cancel(v);assert row(v)==0 and v.owner['pp']==1000 and not flag(v,'deployment_pending')
case('external completion/full capacity never satisfies output; zero attempt refund',bothfull)
for kind in ['provider','tech','control','pointer','actor','cost','row','serial','prototype']:
    def defect(kind=kind):
        v=begun()
        if kind=='provider':v.owner['provider']=False
        elif kind=='tech':v.owner['tech']=False
        elif kind=='control':v.scopes[20002]['control']=10002
        elif kind=='pointer':v.owner['v'][P+'paid_hatchery']=D(99999)
        elif kind=='actor':v.owner['v'][P+'deployment_actor']=D(10002)
        elif kind=='cost':v.owner['a']['mengele_event016_active_cost_fuel_entries'][9]=D(1)
        elif kind=='row':v.owner['a']['mengele_event016_active_project_stage_entries'][9]=D(0)
        elif kind=='serial':v.owner['v'][P+'deployment_serial']=D(0)
        elif kind=='prototype':v.owner['flags'].discard('mengele_event016_paleogenetics_prototype_completed')
        finish(v);assert not v.builds and not completed(v) and flag(v,'deployment_pending')
    case('finish rejects missing/corrupt '+kind,defect)
def no_output_cancel():
    v=begun();v.owner['provider']=False;cancel(v)
    assert row(v)==0 and v.owner['pp']==1000 and v.owner['support']==4000 and v.owner['fuel']==9000
    cancel(v);assert v.owner['pp']==1000
case('provider loss no-output matching refund once',no_output_cancel)
def depleted():
    v=begun();v.owner.update(pp=D(0),support=D(0),fuel=D(0),cic=D(0));finish(v);assert_full(v)
case('expiry does not repurchase depleted resources or factories',depleted)
def debit_bad():
    v=VM();choose(v);v.debit_factor=D('.5');v.seed();v.call(H+'begin_deployment')
    assert flag(v,'payment_unverified') and flag(v,'deployment_pending') and row(v)==3
    finish(v);cancel(v);assert not v.builds and v.owner['pp']==935
case('partial native debit retains measured payment fault without refund/grant',debit_bad)
for factor in [D(0),D('.5'),D(2)]:
    def output_bad(factor=factor):
        v=begun();v.build_factor=factor;finish(v)
        assert flag(v,'construction_unverified') and row(v)==3 and not completed(v)
        before=(v.owner['pp'],len(v.builds));cancel(v);v.call(H+'recover_deployment')
        assert before==(v.owner['pp'],len(v.builds))
    case('unverified construction delta '+str(factor)+' no blind refund or retry',output_bad)
def refund_bad():
    v=begun();v.credit_factor=D('.5');cancel(v)
    assert flag(v,'refund_unverified') and flag(v,'deployment_pending') and row(v)==0
    before=v.owner['pp'];cancel(v);v.call(H+'recover_deployment');assert v.owner['pp']==before
case('unverified default refund retained fault no duplicate credit',refund_bad)
def nested():
    v=begun()
    def reenter(v,k):
        original=dict(v.t);v.seed(0);v.call(H+'cancel_deployment');v.seed(0);v.call(H+'finish_deployment');v.t=original
    v.on_build=reenter;finish(v);assert_full(v);assert v.owner['pp']==870
case('synchronous construction callback reentry cannot refund or replay output',nested)
def bare_component():
    v=VM();choose(v);v.call(H+'attempt_reserve_construction');assert not v.builds
case('bare internal construction helper cannot grant buildings',bare_component)
def neutral():
    v=VM();v.owner['flags'].add('mengele_event016_paleogenetics_deployment_completed')
    v.owner['v'][P+'selected_reserve']=D(20001);v.owner['v'][P+'selected_hatchery']=D(20002)
    v.seed();v.call(H+'begin_deployment')
    assert v.owner['tech'] and not flag(v,'deployment_pending') and not v.builds
    assert not any('krg_' in x or 'grant_custom' in x for x in v.calls)
case('neutral Prototype entitlement unchanged and no KRG or grant helper',neutral)
def before_debit():
    v=VM();choose(v)
    def observe(v,k):
        assert flag(v,'deployment_pending') and flag(v,'deployment_busy')
        assert v.owner['v'][P+'deployment_actor']==10001
        assert v.owner['v'][P+'paid_reserve']==20001 and v.owner['v'][P+'paid_hatchery']==20002
        assert v.owner['v'][P+'deployment_family']==10 and v.owner['v'][P+'deployment_stage']==3
        assert v.t[P+'native_entry']==0
    v.on_debit=observe;v.seed();v.call(H+'begin_deployment')
    assert v.t['mengele_event016_stage_started']==1
case('immutable pending authority and consumed marker precede every debit',before_debit)
def reverse_partial():
    v=begun();v.scopes[20001]['infrastructure']=D(5);finish(v)
    assert len(v.builds)==1 and flag(v,'hatchery_delivered') and not flag(v,'reserve_delivered')
    v.scopes[20001]['infrastructure']=D(4);v.scopes[20002]['slots']=D(0)
    v.call(H+'recover_deployment');assert completed(v) and len(v.builds)==2
case('hatchery-first partial recovers reserve without rechecking full hatchery slots',reverse_partial)
def non_paleo():
    v=VM();v.t['mengele_event016_project_family']=D(13);v.t['mengele_event016_requested_stage']=D(1)
    v.call(G+'begin_project_stage');assert v.t['mengele_event016_stage_started']==1
    assert G+'begin_project_stage_default' in v.calls and H+'begin_deployment' not in v.calls
    v.t['mengele_event016_project_family']=D(13);v.t['mengele_event016_requested_stage']=D(1)
    v.call(G+'finish_project_stage')
    assert 'mengele_event016_alien_arms_theory_completed' in v.owner['flags']
    assert G+'finish_project_stage_default' in v.calls and not v.builds and not flag(v,'deployment_pending')
case('non-Paleo native public/default quote debit finish actual source',non_paleo)
def cold_frame():
    v=VM();choose(v);v.seed()
    v.t.pop('mengele_event016_stage_started')
    v.call(G+'begin_project_stage')
    assert 'mengele_event016_stage_started' not in v.t
    assert row(v)==3 and flag(v,'deployment_pending')
    v.seed(0);v.t.pop('mengele_event016_stage_finished');v.t.pop('mengele_event016_project_output_applied')
    v.call(G+'finish_project_stage')
    assert completed(v) and 'mengele_event016_stage_finished' not in v.t and 'mengele_event016_project_output_applied' not in v.t
    warm=begun();finish(warm)
    assert warm.t['mengele_event016_stage_finished']==1 and warm.t['mengele_event016_project_output_applied']==1
case('cold helper-created outputs discarded; caller-owned warm results retained',cold_frame)
for serial in [D(-1),D('.5')]:
    def bad_serial(serial=serial):
        v=VM();choose(v);v.owner['v'][P+'deployment_serial']=serial;v.seed();v.call(H+'begin_deployment')
        assert v.owner['pp']==1000 and not flag(v,'deployment_pending') and v.owner['v'][P+'deployment_serial']==serial
    case('malformed prepayment generation '+str(serial),bad_serial)
snapshots[str(Path(__file__).resolve().relative_to(ROOT)).replace('\\','/')] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
result = {'cases_passed':cases,'source_sha256':snapshots,
 'external_helper_stubs':['brilliant_scientist_mengele_project_stage_provider_is_valid','brilliant_scientist_mengele_conventional_incident_provider_is_valid'],
 'native_limits':['opaque mock pointers','aggregate support/fuel/PP primitive model',
 'slots and building delta not engine proof','no native timer/reservation ordering',
 'no delayed recount/provenance or unique building identity']}
if '--results' in sys.argv:
    target=Path(__file__).with_name('core_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

