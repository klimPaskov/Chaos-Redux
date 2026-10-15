"""Execute production camp mutation and immediate-panel publication contracts.

Usage: python .tools/test_camp_panel_publishers.py

Uses the existing national-policy panel runtime and conservative helper frames.
Admission/release rows, reform/closure, paid institution progress, occupation
transfer metadata, exact recipients and real cache projections execute source.
Read-only eligibility/provenance predicates and origin row inspection are declared
fixtures. Shared population-loss and equipment-removal APIs are modelled external
dependencies. All existing camp temporary scratch is caller-preinitialized in the
fixture, so this does not certify unprepared external callers or native receipts.
No game date advances, native engine execution, game launch or render is involved.
"""
from pathlib import Path
import sys, unittest, re, json
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.tools'))
import test_national_policy_panel_updates as N
H=N.H;P=N.P;D=H.Decimal
class Runtime(N.Runtime):
 EXTERNAL_FIXTURES=N.Runtime.EXTERNAL_FIXTURES | {'remove_support_equipment_from_stockpile','apply_state_population_loss_without_recruitable_manpower_gain'}
 def __init__(self,states=()):
  super().__init__(states)
  for path in (ROOT/'common/scripted_effects').glob('camp*.txt'):
   self.effect_defs.update(P.read_definitions(str(path.relative_to(ROOT))))
  for path in (ROOT/'common/scripted_effects').glob('camp*.txt'):
   raw=path.read_text(encoding='utf-8-sig')
   for name,num in re.findall(r'(?m)^(@\w+) = (-?[\d.]+)',raw):self.file_constants[name[1:]]=D(num)
   for name in re.findall(r'(?:set_temp_variable|add_to_temp_variable)\s*=\s*\{\s*(\w+)\s*=',raw):self.temp_frames[0].setdefault(name,D(0))
  # Keep price consumers as externally declared fixtures exactly as core tests.
  for n in ('camp_admin_refresh_command_quotes','camp_admin_generic_reform_refresh_quote'):
   self.effect_defs.pop(n,None)
  self.effect_defs['camp_admin_record_history']=H.read_named('common/scripted_effects/camp_administration_ui_effects.txt','camp_admin_record_history')
  self.fixture_predicates={
   'camp_admin_site_is_operational':True,'camp_origin_host_provenance_ready':True,
   'camp_admin_has_supported_workforce':False,'camp_admin_site_authority_is_valid':True,
   'camp_admin_site_rows_reconciled':True,'camp_origin_host_records_incomplete':False,
   'camp_admin_country_program_completion_ready':False,'camp_admin_country_institution_supported':True,
   'camp_admin_country_sites_ready_for_reform':True,'camp_administration_civil_country_supported':False,
   'camp_admin_can_use_radical_mandate':False,
  }
 def _call_effect(self,name,scope):
  if name=='remove_support_equipment_from_stockpile':
   scope.resources['support_equipment']-=self._variable('equipment_stockpile_removal_amount');return
  if name=='apply_state_population_loss_without_recruitable_manpower_gain':
   scope.population_k-=self._variable('state_population_transaction_loss')/1000;return
  return super()._call_effect(name,scope)
 def _native_effect(self,key,value,scope,line):
  if key=='add_manpower' and scope.kind=='state':scope.population_k+=self._value(value)/1000;return
  return super()._native_effect(key,value,scope,line)
 def _write_path(self,path,value,clear=False): P.Event35Runtime._write_path(self,path,value,clear)
 def _value(self,t):
  if t=='num_of_military_factories':return D(10)
  if t=='num_equipment@support_equipment':return D(self.current.resources.get('support_equipment',0))
  if t=='political_power':return D(self.current.resources.get('political_power',0))
  if t=='manpower_k':return D(self.current.resources.get('manpower',0))/1000
  if t in ('state_population_k','chaos_state_civilian_deaths_total'):return D(str(self.current.population_k if t=='state_population_k' else self.current.values.get(t,0)))
  if isinstance(t,str) and t.startswith('building_level@'):return D(str(self.current.buildings.get(t.split('@')[1],0)))
  if t in ('global.year','global.month'):return D(1936 if t.endswith('year') else 1)
  return super()._value(t)
 def _condition(self,n,s):
  if n.key=='has_variable' and any(n.value in f for f in self.temp_frames):return True
  if n.key=='is_owned_and_controlled_by':return s.owner is s.controller
  if n.key in self.fixture_predicates:return self.fixture_predicates[n.key]
  if n.key in ('owner','controller','OWNER','CONTROLLER'):
   target=getattr(s,n.key.lower());self.scope_stack.append(target)
   try:return self._conditions(n.value,target)
   finally:self.scope_stack.pop()
  if n.key=='camp_origin_host_rows_valid':
   # Declared row-inspector fixture. Actual custody row append/check/count/consume execute.
   vals={'camp_origin_rows_valid':1,'camp_origin_inspect_custody_k':s.values.get('camp_admin_detainees_k',0),'camp_origin_inspect_occupation_k':s.values.get('camp_occ_remaining_k',0),'camp_origin_inspect_shortfall_k':0,'camp_origin_live_row_count':0,'camp_origin_mixed_lineages':0}
   for k,v in vals.items():self._set_temp(k,D(v))
   return True
  try:return super()._condition(n,s)
  except TypeError as e:raise AssertionError((n,s.id,self.call_stack)) from e
 def _effects(self,nodes,s):
  # Production while loops over sparse custody rows, enforcing native 1000 ceiling.
  chunk=[]
  for n in nodes:
   if n.key in ('OWNER','CONTROLLER'):
    if chunk:super()._effects(chunk,s);chunk=[]
    target=getattr(s,n.key.lower());self.scope_stack.append(target)
    try:self._effects(n.value,target)
    finally:self.scope_stack.pop()
   elif n.key=='while_loop_effect':
    if chunk:super()._effects(chunk,s);chunk=[]
    limit=P.first(n.value,'limit');body=[x for x in n.value if x.key!='limit']
    for _ in range(1000):
     if not self._conditions(limit,s):break
     self._effects(body,s)
    else:raise AssertionError('Unexpected row-loop cap')
   else:chunk.append(n)
  if chunk:super()._effects(chunk,s)

def case(captured=False):
 owner=H.country('ENG');authority=H.country('GER') if captured else owner
 authority.values['fixture_camp_eligible']=True;authority.flags.add('camp_repression_ledger_open')
 site=H.state(7,owner,flags=['camp_admin_initialized','camp_admin_rows_initialized','camp_origin_observation_initialized'],camp_admin_responsible_country=authority,genocide_responsible_country=authority,camp_admin_detainees_k=0,camp_admin_next_row_id=1,camp_admin_row_count=0,camp_origin_observed_population_k=100)
 site.buildings['concentration_camp']=1
 for key in ('ids','origins','authorities','occupation_roots','amounts_k','deaths_k','arrival_deaths_k','released_k','removed_k','statuses'):site.arrays['camp_admin_row_'+key]=[]
 authority.arrays['camp_active_site_states']=[site];authority.arrays['camp_admin_known_site_states']=[site]
 r=Runtime([site]);r.run_effect('national_policy_panel_refresh_open',authority);r.refreshes.clear()
 return r,owner,authority,site
class Tests(unittest.TestCase):
 def test_admit_release_source_updates_paused_cache_and_preserves_receipts(self):
  r,o,a,s=case();t=r.temp_frames[0];t.update(camp_admin_admission_accepted_k=0,camp_admin_admission_requested_k=2,camp_admin_admission_source_k=2,camp_admin_admission_proven=1)
  r.run_effect('camp_admin_admit_detainees',s)
  self.assertEqual(s.values['camp_admin_detainees_k'],2);self.assertEqual(a.values['camp_admin_gui_site_detainees_k'],2)
  self.assertEqual(t['camp_admin_admission_accepted_k'],2);self.assertEqual(len(r.refreshes),1)
  t.update(camp_admin_release_requested_k=1,camp_admin_release_actual_k=0)
  r.run_effect('camp_admin_release_detainees',s)
  self.assertEqual(s.values['camp_admin_detainees_k'],1);self.assertEqual(a.values['camp_admin_gui_site_detainees_k'],1);self.assertEqual(t['camp_admin_release_actual_k'],1)
  self.assertEqual(s.population_k,100);self.assertEqual(r.globals['date'],0)
 def test_reform_nested_closure_publication_contains_final_flags(self):
  r,o,a,s=case();r.temp_frames[0].update(camp_admin_admission_accepted_k=0,camp_admin_admission_requested_k=2,camp_admin_admission_source_k=2,camp_admin_admission_proven=1)
  r.run_effect('camp_admin_admit_detainees',s);r.refreshes.clear()
  r.temp_frames[0]['camp_admin_release_actual_k']=0
  r.run_effect('camp_admin_reform_site',s)
  self.assertIn('camp_admin_closed',s.flags);self.assertIn('camp_admin_civilian_conversion_pending',s.flags)
  self.assertEqual(a.values['camp_admin_gui_site_detainees_k'],0);self.assertEqual(len(r.refreshes),1)
  self.assertEqual(r.globals['date'],0)
 def test_distinct_record_authority_and_owner_no_disclosure(self):
  r,o,a,s=case(True);o.flags.add('camp_repression_ledger_open');o.values['fixture_camp_eligible']=True
  # Original authority may see its retained closed record, current owner cannot inherit it.
  s.flags.add('camp_admin_closed');o.arrays['camp_admin_known_site_states']=[s]
  r.run_effect('camp_origin_mark_ambiguous',s)
  self.assertIn(('camp_admin_refresh_interface',a.id),r.refreshes);self.assertIn(('camp_admin_refresh_interface',o.id),r.refreshes)
  self.assertEqual(o.arrays['camp_admin_gui_states'],[]);self.assertEqual(a.arrays['camp_admin_gui_states'],[s]);self.assertEqual(r.globals['date'],0)
 def test_country_program_cancel_and_progress_publication(self):
  r,o,a,s=case();a.values.update(camp_admin_economy_progress=4,camp_admin_economy_target=8)
  r.run_effect('camp_admin_cancel_economy_project',a);self.assertEqual(a.values['camp_admin_gui_economy_progress'],0)
  a.flags.update(['camp_admin_institution_slot_active']);a.values.update(camp_admin_country_program=1,camp_admin_institution_state_id=s,camp_admin_institution_progress=1,camp_admin_institution_target=6,camp_admin_research_year=1936,camp_admin_research_awards_this_year=0)
  # Execute the actual paid institution tick and payment helper.
  a.values.update(camp_admin_budget_support_remaining=1000,camp_admin_budget_pp_remaining=1000)
  a.resources['support_equipment']=10000
  r.fixture_predicates['camp_admin_country_is_major_kit']=True
  r.run_effect('camp_admin_country_tick_institution',a)
  self.assertEqual(a.values['camp_admin_institution_progress'],2)
  self.assertEqual(a.values['camp_admin_gui_institution_progress'],D(2)/6)
  self.assertNotIn('camp_admin_country_institution_paused',a.flags)
  self.assertEqual(r.globals['date'],0)
 def test_actual_occupation_transfer_publishes_both_endpoints_and_original_authority(self):
  r,o,a,s=case(True)
  receiver=H.country('FRA');receiver.flags.add('camp_repression_ledger_open');receiver.values['fixture_camp_eligible']=True
  o.flags.add('camp_repression_ledger_open');o.values['fixture_camp_eligible']=True
  dest=H.state(8,receiver,flags=['camp_origin_observation_initialized','camp_occ_registered'],camp_origin_observed_population_k=100,camp_occ_responsible_country=a,camp_occ_remaining_k=0)
  r.states.append(dest)
  s.flags.add('camp_occ_registered');s.values.update(camp_occ_remaining_k=5,camp_occ_responsible_country=a,camp_occ_native_row_id=1)
  a.arrays['camp_occ_states']=[s];a.flags.add('camp_occ_rows_initialized')
  row={'ids':[1],'root_ids':[1],'origins':[s],'hosts':[s],'authorities':[a],'profiles':[1],'amounts_k':[5],'deaths_k':[0],'removed_k':[0],'released_k':[0],'moved_out_k':[0],'moved_in_k':[0],'statuses':[1]}
  for k,v in row.items():a.arrays['camp_occ_row_'+k]=v
  a.values.update(camp_occ_row_count=1,camp_occ_next_row_id=2)
  r.fixture_predicates.update(camp_occ_state_has_route_authority=True,camp_occ_state_accepts_transfer_authority=True,camp_occ_state_has_current_authority=True)
  r.targets['camp_occ_transfer_destination']=dest
  r.temp_frames[0].update(camp_occ_transfer_row_id=1,camp_occ_transfer_requested_people=1000,camp_occ_transfer_route_proven=1,camp_occ_transfer_escape=0,camp_occ_transfer_committed_people=0,camp_occ_transfer_result=0)
  r.run_effect('camp_occ_transfer_survivors_exact',s)
  self.assertEqual(r.temp_frames[0]['camp_occ_transfer_result'],1,{k:str(v) for k,v in r.temp_frames[0].items() if k.startswith(('camp_occ_transfer_','camp_occ_active_')) and not isinstance(v,N.Scope)})
  self.assertEqual(s.values['camp_occ_remaining_k'],4);self.assertEqual(dest.values['camp_occ_remaining_k'],1)
  self.assertEqual(a.arrays['camp_occ_row_authorities'],[a,a])
  self.assertEqual(s.population_k,99);self.assertEqual(dest.population_k,101)
  for c in (o,a,receiver):self.assertIn(('camp_admin_refresh_interface',c.id),r.refreshes)
  self.assertEqual(r.globals['date'],0)
  for c in (o,a,receiver):self.assertNotIn('national_policy_panel_update_depth',c.values)
 def test_closed_panels_publisher_bookkeeping_is_idle(self):
  r,o,a,s=case();a.flags.remove('camp_repression_ledger_open');r.refreshes.clear()
  before=(dict(s.values),{k:list(v) for k,v in s.arrays.items()},dict(a.values),set(a.flags))
  r.run_effect('camp_admin_panel_begin_state_update',s);r.run_effect('camp_admin_panel_end_state_update',s)
  self.assertEqual(before,(s.values,s.arrays,a.values,a.flags));self.assertEqual(r.refreshes,[])
if __name__=='__main__':unittest.main(verbosity=2)
