"""Check warfare law and receipt helpers against declared source fixtures.

Inputs: current repository scripts, located relative to this file, with no
baseline or scratch dependency. Run with Python and no arguments.
Output: unittest results on stderr and a nonzero exit status on failure.
Limits: native primitives and Event 023 receipt acceptance are fixture models,
not HOI4 execution or operational weapon simulation.
"""
import re
import operator
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
TOKEN = re.compile(r'#[^\n]*|"[^"\n]*"|[{}=]|[^\s{}=]+')


def parse(text):
    """Read only the Clausewitz key/value blocks used by these fixtures."""
    tokens = [m.group() for m in TOKEN.finditer(text) if not m.group().startswith('#')]
    cursor = 0

    def body():
        nonlocal cursor
        result = []
        while cursor < len(tokens) and tokens[cursor] != '}':
            if tokens[cursor] == '{':
                cursor += 1
                nested = body()
                if cursor >= len(tokens) or tokens[cursor] != '}':
                    raise AssertionError('Unclosed anonymous schema block')
                cursor += 1
                result.append(('_anonymous', nested))
                continue
            key = tokens[cursor]
            cursor += 1
            if cursor >= len(tokens) or tokens[cursor] != '=':
                result.append((key, None))
                continue
            cursor += 1
            value = tokens[cursor]
            cursor += 1
            if value == '{':
                value = body()
                if cursor >= len(tokens) or tokens[cursor] != '}':
                    raise AssertionError('Unclosed source block')
                cursor += 1
            result.append((key, value))
        return result

    return body()

def load(p):
 text=(ROOT/p).read_text(encoding='utf-8-sig')
 def short(m):
  compare={'=':'equals','>':'greater_than','<':'less_than'}[m[2]]
  return 'check_variable = { var = '+m[1]+' value = '+m[3]+' compare = '+compare+' }'
 return parse(re.sub(r'check_variable\s*=\s*\{\s*([^\s{}=<>]+)\s*([=<>])\s*([^\s{}=<>]+)\s*\}',short,text))
TRIG={}
for p in ['cbrn_triggers','cbrn_diplomacy_triggers','national_policy_warfare_triggers']:
 TRIG.update(load('common/scripted_triggers/'+p+'.txt'))
EFF={}
for p in ['cbrn_diplomacy_effects','national_policy_warfare_effects']:
 EFF.update(load('common/scripted_effects/'+p+'.txt'))
CONST={}
for p in ['cbrn_diplomacy_constants','cbrn_system_constants','023_sov_nuclear_bombs_constants']:
 for key,val in load('common/script_constants/'+p+'.txt'):
  if isinstance(val,list): CONST[key]=dict(val)

class Country:
 def __init__(self,id): self.id=id; self.v={}; self.ideas=set(); self.flags=set(); self.enemies=[]; self.exists=True
class RT:
 def __init__(self):
  self.a=Country(1);self.b=Country(2);self.c=Country(3)
  self.a.enemies=[self.b,self.c];self.b.enemies=[self.a];self.c.enemies=[self.a]
  self.root=self.a;self.frm=self.b;self.prev=None;self.temp={};self.targets={};self.day=100;self.calls=[];self.global_flags=set();self.native_receipt_valid=True
 def val(self,t,a):
  t=t.strip('"')
  if t=='THIS':return a
  if t=='ROOT':return self.root
  if t=='PREV':return self.prev
  if t=='FROM':return self.frm
  if t=='id' or t=='THIS.id':return a.id
  if t=='global.num_days':return self.day
  if t.startswith('event_target:'):return self.targets.get(t[13:])
  if t.startswith('var:'):return self.val(t[4:],a)
  if t.startswith('ROOT.'):return self.root.v.get(t[5:],0)
  if t.startswith('constant:'):
   group,name=t[9:].split('.',1);return float(CONST[group][name])
  if t in self.temp:return self.temp[t]
  try:return float(t)
  except ValueError:return a.v.get(t,0)
 def scope(self,k,a):
  if k=='CONTROLLER':return getattr(a,'controller',None)
  if k in ('ROOT','FROM','PREV','THIS') or k.startswith(('event_target:','var:')):return self.val(k,a)
  return None
 def nested(self,body,a,target,effect=False):
  if not isinstance(target,Country):return False
  prev=self.prev;self.prev=a
  try:return self.run(body,target) if effect else self.test(body,target)
  finally:self.prev=prev
 def meta(self,d,a):
  args={}
  for k,v in d:
   if k=='text':continue
   m=re.search(r'\[\?([^|]+)\|',v)
   args[k]=str(int(self.val(m[1],a))) if m else v.strip('"')
  def sub(v):
   if isinstance(v,list):return [(sub(k),sub(d)) for k,d in v]
   for k,d in args.items():v=v.replace('['+k+']',d)
   return v
  return sub(dict(d)['text'])
 def test(self,n,a):
  prior_if=False
  for k,d in n:
   target=self.scope(k,a)
   if k in ('OR','NOT'):r=any(self.test([x],a) for x in d);r=(not r) if k=='NOT' else r
   elif k in ('AND','hidden_trigger'):r=self.test(d,a)
   elif k=='custom_trigger_tooltip':r=self.test([(k,v) for k,v in d if k!='tooltip'],a)
   elif k=='if':
    prior_if=self.test(dict(d)['limit'],a);r=(not prior_if) or self.test([(k,v)for k,v in d if k!='limit'],a)
   elif k=='else':r=prior_if or self.test(d,a)
   elif k=='always':r=d=='yes'
   elif k=='exists':r=a.exists==(d=='yes')
   elif k=='has_idea':r=d in a.ideas
   elif k=='has_variable':r=d in a.v or d in self.temp
   elif k=='has_event_target':r=d in self.targets
   elif k in ('has_country_flag','has_state_flag'):r=d in a.flags
   elif k=='has_global_flag':r=d in self.global_flags
   elif k=='sov_nuclear_bombs_native_delivery_country_is_valid':r=self.native_receipt_valid
   elif k=='tag':r=a is self.val(d,a)
   elif k=='has_war_with':r=self.val(d,a) in a.enemies
   elif k=='any_enemy_country':r=any(self.nested(d,a,e) for e in a.enemies)
   elif k=='meta_trigger':r=self.test(self.meta(d,a),a)
   elif k=='set_temp_variable':self.temp[d[0][0]]=self.val(d[0][1],a);r=True
   elif k=='check_variable':
    b=dict(d); op={'equals':operator.eq,'greater_than':operator.gt,'less_than':operator.lt,'less_than_or_equals':operator.le,'greater_than_or_equals':operator.ge}[b['compare']]
    r=op(self.val(b['var'],a),self.val(b['value'],a))
   elif k in TRIG:r=self.test(TRIG[k],a)
   elif target is not None:r=self.nested(d,a,target)
   else:raise AssertionError(('unsupported trigger',k,d))
   if not r:return False
  return True
 def run(self,n,a):
  prior_if=False
  for k,d in n:
   target=self.scope(k,a)
   if k in ('if','else_if'):
    if k=='else_if' and prior_if:continue
    hit=self.test(dict(d)['limit'],a)
    if hit:self.run([(k,v)for k,v in d if k!='limit'],a)
    prior_if=hit
   elif k=='else':
    if not prior_if:self.run(d,a)
   elif k=='meta_effect':self.run(self.meta(d,a),a)
   elif k in ('set_variable','set_temp_variable','add_to_temp_variable'):
    name,token=d[0];store=self.temp if k!='set_variable' else a.v
    store[name]=self.val(token,a)+store.get(name,0) if k=='add_to_temp_variable' else self.val(token,a)
   elif k=='clear_variable':a.v.pop(d,None)
   elif k=='set_country_flag':a.flags.add(dict(d)['flag'] if isinstance(d,list) else d)
   elif k=='save_event_target_as':self.targets[d]=a
   elif k in ('cbrn_convention_on_member_attacked','sov_nuclear_bombs_clear_action_context'):self.calls.append(k)
   elif k in EFF:self.run(EFF[k],a)
   elif target is not None:self.nested(d,a,target,True)
   else:raise AssertionError(('unsupported effect',k,d))
 def confirmed(self,actor,victim,date,source=1):
  self.root=actor;self.targets['cbrn_retaliation_target_country']=victim
  self.temp.update(cbrn_confirmed_use_action_date=date,cbrn_retaliation_source_type=source)
  self.run(EFF['cbrn_diplomacy_record_confirmed_cbrn_use'],actor)
 def allowed(self,actor,target,family,tier='strategic'):
  self.root=actor;self.frm=target;self.temp['cbrn_retaliation_target_id']=target.id
  key='cbrn_policy_allows_'+tier+'_use_against_from' if family=='chemical' else 'national_policy_'+family+'_allows_'+('use_against_from' if family=='nuclear' else tier+'_use_against_from')
  return self.test(TRIG[key],actor)

class WarfareContract(unittest.TestCase):
 def test_family_isolation_and_exact_enemy(self):
  r=RT();r.confirmed(r.b,r.a,99,3)
  r.a.ideas={'national_policy_chemical_unrestricted','national_policy_biological_retaliation','national_policy_nuclear_none'}
  self.assertTrue(r.allowed(r.a,r.c,'chemical'))
  self.assertTrue(r.allowed(r.a,r.b,'biological'))
  self.assertFalse(r.allowed(r.a,r.c,'biological'))
  self.assertFalse(r.allowed(r.a,r.b,'nuclear'))
  r.a.ideas.remove('national_policy_nuclear_none');r.a.ideas.add('national_policy_nuclear_retaliation')
  self.assertTrue(r.allowed(r.a,r.b,'nuclear'));self.assertFalse(r.allowed(r.a,r.c,'nuclear'))
 def test_receipt_expiry_and_duplicate_no_refresh(self):
  r=RT();r.confirmed(r.b,r.a,99)
  key='cbrn_retaliation_2_expiry_day';self.assertEqual(r.a.v[key],465)
  r.day=120;r.confirmed(r.b,r.a,99);self.assertEqual(r.a.v[key],465)
  r.a.ideas={'national_policy_nuclear_retaliation'}
  r.day=465;self.assertTrue(r.allowed(r.a,r.b,'nuclear'))
  r.day=466;self.assertFalse(r.allowed(r.a,r.b,'nuclear'))
 def test_same_day_tie_revokes_both_and_keeps_history(self):
  r=RT();r.confirmed(r.a,r.b,100);r.confirmed(r.b,r.a,100,3)
  self.assertNotIn('cbrn_retaliation_2_expiry_day',r.a.v)
  self.assertNotIn('cbrn_retaliation_1_expiry_day',r.b.v)
  self.assertEqual(r.a.v['cbrn_confirmed_use_against_2_first_action_date'],100)
  self.assertEqual(r.b.v['cbrn_confirmed_use_against_1_first_action_date'],100)
 def test_civil_war_copy_cannot_authorize_or_be_adopted_by_new_receipt(self):
  r=RT();r.confirmed(r.b,r.a,99)
  r.c.v=r.a.v.copy();r.c.ideas={'national_policy_nuclear_retaliation'};r.c.enemies=[r.b];r.b.enemies.append(r.c)
  self.assertFalse(r.allowed(r.c,r.b,'nuclear'))
  r.confirmed(r.b,r.c,101,3)
  self.assertTrue(r.allowed(r.c,r.b,'nuclear'))
  # Original victim's receipt still names its original holder.
  self.assertIs(r.a.v['cbrn_retaliation_2_owner'],r.a)
 def test_battlefield_taxonomy_does_not_expand_strategic_retaliation(self):
  r=RT();r.confirmed(r.b,r.a,99)
  r.a.ideas={'national_policy_biological_battlefield'}
  self.assertTrue(r.allowed(r.a,r.b,'biological','battlefield'))
  self.assertFalse(r.allowed(r.a,r.b,'biological','strategic'))
 def test_all_six_native_launches_have_production_gate(self):
  types=dict(load('common/raids/nuclear_raids.txt'))['types']
  self.assertEqual(len(types),6)
  for name,body in types:
   self.assertIn(('national_policy_nuclear_allows_use_against_from','yes'),dict(body)['launchable'],name)
 def test_nuclear_combat_preflight_denies_without_own_family_law(self):
  r=RT();r.a.v.update(sov_nuclear_bombs_action_target=r.b,sov_nuclear_bombs_action_type=float(CONST['sov_nuclear_bombs_action']['combat_strike']))
  r.a.ideas={'national_policy_chemical_unrestricted','national_policy_nuclear_none'}
  self.assertFalse(r.test(TRIG['national_policy_nuclear_event_action_policy_is_valid'],r.a))
  r.a.ideas.add('national_policy_nuclear_unrestricted')
  self.assertTrue(r.test(TRIG['national_policy_nuclear_event_action_policy_is_valid'],r.a))
 def test_normalized_nuclear_callback_uses_hostile_controller_only(self):
  r=RT();state=Country(50);state.controller=r.c;state.owner=r.b;r.frm=state
  r.run(EFF['national_policy_record_confirmed_nuclear_use'],r.a)
  self.assertIn('cbrn_retaliation_1_expiry_day',r.c.v)
  self.assertNotIn('cbrn_retaliation_1_expiry_day',r.b.v)
  self.assertEqual(r.c.v['cbrn_retaliation_1_source'],3)
  self.assertEqual(r.calls,[]) # no duplicate treaty/physical consequence owner
 def test_nuclear_callback_excludes_visual_test_and_nonce_mismatch(self):
  for case in ('visual','test','demonstration','accident','wrong_nonce','missing_state_id','own_controller'):
   with self.subTest(case=case):
    r=RT();state=Country(50);state.controller=r.b;r.frm=state
    if case=='visual':r.global_flags.add('asteroid_incoming_visual_strike_active')
    elif case=='own_controller':state.controller=r.a
    else:
     r.a.flags.add('sov_nuclear_bombs_native_delivery_pending')
     r.a.v.update(sov_nuclear_bombs_action_state_id=50,sov_nuclear_bombs_action_nonce=7)
     state.flags.add('sov_nuclear_bombs_native_delivery_state_pending')
     state.v['sov_nuclear_bombs_native_delivery_nonce']=8 if case=='wrong_nonce' else 7
     kind='combat_strike' if case in ('wrong_nonce','missing_state_id') else case
     r.a.v['sov_nuclear_bombs_action_type']=float(CONST['sov_nuclear_bombs_action'][kind])
     if case=='missing_state_id':r.a.v.pop('sov_nuclear_bombs_action_state_id')
    r.run(EFF['national_policy_record_confirmed_nuclear_use'],r.a)
    self.assertNotIn('cbrn_retaliation_1_expiry_day',r.b.v)
 def test_tightening_cancels_uncommitted_even_during_native_idea_overlap(self):
  r=RT();r.a.ideas={'national_policy_nuclear_unrestricted','national_policy_nuclear_none'}
  r.a.flags.add('sov_nuclear_bombs_action_reservation_active')
  r.a.v.update(sov_nuclear_bombs_action_target=r.b,sov_nuclear_bombs_action_type=float(CONST['sov_nuclear_bombs_action']['combat_strike']))
  r.temp.update(national_policy_changed_family=3,national_policy_new_value=0,national_policy_previous_value=5)
  r.run(EFF['national_policy_on_warfare_law_changed'],r.a)
  self.assertEqual(r.calls,['sov_nuclear_bombs_clear_action_context'])
  r.calls=[];r.a.flags.add('sov_nuclear_bombs_native_delivery_pending')
  r.run(EFF['national_policy_on_warfare_law_changed'],r.a)
  self.assertEqual(r.calls,[]) # committed native delivery cannot receive a refund

if __name__=='__main__':unittest.main(verbosity=2)
