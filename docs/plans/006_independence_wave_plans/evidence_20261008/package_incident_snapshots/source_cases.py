from pathlib import Path
import sys,json,math,operator,re
sys.path.insert(0,str(Path(__file__).resolve().parent))
from clausewitz_subset_parser import parse
constants={}
for p in Path('common/script_constants').glob('*.txt'):
 for group,items,_,_ in parse(p.read_text(encoding='utf-8-sig')):
  if isinstance(items,list):
   for k,v,_,_ in items:
    try:constants[group+'.'+k]=float(v)
    except (ValueError,TypeError):pass
effect_path=Path('common/scripted_effects/006_independence_wave_package_incident_effects.txt')
trigger_path=Path('common/scripted_triggers/006_independence_wave_package_incident_triggers.txt')
effects={k:v for k,v,_,_ in parse(effect_path.read_text(encoding='utf-8-sig'))}
triggers={k:v for k,v,_,_ in parse(trigger_path.read_text(encoding='utf-8-sig'))}
old_path=Path('docs/plans/006_independence_wave_plans/evidence_20261008/package_incident_snapshots/frozen_before')
before_triggers={k:v for k,v,_,_ in parse((old_path/trigger_path.name).read_text(encoding='utf-8-sig'))}
maps=json.loads((Path(__file__).resolve().parent/'original_event_maps.json').read_text())

class Model:
 # Game-active origin is an external fixture. Actual snapshot, dispatch,
 # cleanup and reply predicates run; native popup timing is not simulated.
 def __init__(self,pkg=1,gen=1):
  self.normal={'independence_wave_package_id':pkg,'independence_wave_generation_id':gen};self.flags=set();self.frames=[{}];self.date=0.02;self.active=True;self.queued=[]
 def value(self,x):
  if x.startswith('constant:'):return constants[x[9:]]
  if x=='global.date':return self.date
  try:return float(x)
  except ValueError:pass
  for f in reversed(self.frames):
   if x in f:return f[x]
  return self.normal.get(x,0)
 def put(self,k,v):
  for f in reversed(self.frames):
   if k in f:f[k]=v;return
  self.frames[-1][k]=v
 def trigger(self,nodes,defs=None):
  defs=triggers if defs is None else defs;ans=[]
  for k,v,_,_ in nodes:
   if k=='NOT':r=not any(self.trigger([n],defs) for n in v)
   elif k=='OR':r=any(self.trigger([n],defs) for n in v)
   elif k=='AND':r=self.trigger(v,defs)
   elif k=='is_independence_wave_active_country':r=self.active
   elif k=='has_country_flag':r=v in self.flags
   elif k=='has_variable':r=v in self.normal or any(v in f for f in self.frames)
   elif k=='check_variable':
    f={a:b for a,b,_,_ in v};var=f.get('var')
    if var is None:var=next(a for a in f if a not in ('value','compare'))
    r={'equals':operator.eq,'greater_than':operator.gt,'less_than':operator.lt,'greater_than_or_equals':operator.ge}[f.get('compare','equals')](self.value(var),self.value(f.get('value',f.get(var))))
   elif k in defs:r=self.trigger(defs[k],defs)
   else:raise AssertionError(('undeclared trigger',k))
   ans.append(r)
  return all(ans)
 def call(self,k):
  self.frames.append({})
  try:self.run(effects[k])
  finally:self.frames.pop()
 def run(self,nodes):
  matched=False
  for k,v,_,_ in nodes:
   if k in ('if','else_if','else'):
    f={a:b for a,b,_,_ in v};take=(k=='if' or not matched) and (k=='else' or self.trigger(f.get('limit',[])))
    if k=='if':matched=take
    elif take:matched=True
    if take:self.run([n for n in v if n[0]!='limit'])
   elif k=='set_country_flag':self.flags.add(v)
   elif k=='clr_country_flag':self.flags.discard(v)
   elif k=='clear_variable':self.normal.pop(v,None)
   elif k in ('set_variable','add_to_variable'):
    for a,b,_,_ in v:self.normal[a]=self.value(b) if k=='set_variable' else self.normal.get(a,0)+self.value(b)
   elif k in ('set_temp_variable','subtract_from_temp_variable','multiply_temp_variable'):
    for a,b,_,_ in v:
     val=self.value(b)
     self.put(a,val if k=='set_temp_variable' else self.value(a)-val if k=='subtract_from_temp_variable' else self.value(a)*val)
   elif k=='clamp_temp_variable':
    f={a:b for a,b,_,_ in v};self.put(f['var'],max(self.value(f['var']),self.value(f['min'])))
   elif k=='chaosx_convert_days_to_date_offset':
    # Shared documented converter: ceil whole hours, five-decimal date units.
    self.put('chaosx_date_offset',math.ceil(self.value('chaosx_date_days')*constants['chaosx_date_units.hours_per_day'])/constants['chaosx_date_units.hours_per_date_unit'])
   elif k=='meta_effect':
    f={a:b for a,b,_,_ in v}
    def param(name):return self.value(re.fullmatch(r'"\[\?([^|]+)\|\.0\]"',f[name]).group(1))
    self.queued.append(('chaosx.nr6.'+str(round(param('INCIDENT'))),round(param('HOURS'))))
   elif k in effects:self.call(k)
   else:raise AssertionError(('undeclared effect',k))

mapping_count=0
for slot,entries in maps['maps'].items():
 for pkg,eid in entries:
  m=Model(constants[pkg[9:]])
  if slot=='b':m.flags.add('independence_wave_package_incident_a_resolved')
  m.call('independence_wave_schedule_package_incident_'+slot)
  hours=constants['independence_wave_package_incident.'+('first_delay_days' if slot=='a' else 'second_delay_days')]*constants['chaosx_date_units.hours_per_day']
  assert m.queued==[(eid,hours)],(slot,pkg,m.queued)
  due=m.normal['independence_wave_package_incident_'+slot+'_due_date']
  m.call('independence_wave_schedule_package_incident_'+slot)
  assert len(m.queued)==1 and m.normal['independence_wave_package_incident_'+slot+'_due_date']==due
  mapping_count+=1

results=[]
for slot in ['a','b']:
 m=Model();m.normal['independence_wave_package_incident_generation']=1;m.normal['independence_wave_package_incident_'+slot+'_due_date']=m.date
 m.flags.add('independence_wave_package_incident_'+slot+'_scheduled');m.call('independence_wave_package_incident_capture_'+slot+'_shown')
 assert m.trigger(triggers['can_resolve_independence_wave_package_incident_'+slot])
 m.call('independence_wave_clear_package_incident_runtime');assert 'independence_wave_package_incident_'+slot+'_shown' in m.flags
 m.normal['independence_wave_generation_id']=2
 if slot=='b':m.flags.add('independence_wave_package_incident_a_resolved')
 m.call('independence_wave_schedule_package_incident_'+slot);due=m.normal['independence_wave_package_incident_'+slot+'_due_date'];assert not m.queued
 m.date=due
 assert not m.trigger(triggers['can_deliver_independence_wave_package_incident_'+slot])
 assert not m.trigger(triggers['can_resolve_independence_wave_package_incident_'+slot])
 # Reproduces the old authority gap when replacement delivery is allowed.
 m.flags.add('independence_wave_package_incident_'+slot+'_delivered')
 assert m.trigger(before_triggers['can_resolve_independence_wave_package_incident_'+slot],before_triggers)
 assert not m.trigger(triggers['can_resolve_independence_wave_package_incident_'+slot])
 m.flags.discard('independence_wave_package_incident_'+slot+'_delivered')
 m.call('independence_wave_package_incident_close_'+slot+'_shown');assert len(m.queued)==1 and m.queued[0][1]==0 and m.normal['independence_wave_package_incident_'+slot+'_due_date']==due
 m.call('independence_wave_package_incident_close_'+slot+'_shown');assert len(m.queued)==1
 m.call('independence_wave_package_incident_capture_'+slot+'_shown');assert m.trigger(triggers['can_resolve_independence_wave_package_incident_'+slot])
 m.flags.add('independence_wave_package_incident_'+slot+'_resolved');assert not m.trigger(triggers['can_resolve_independence_wave_package_incident_'+slot])
 m.call('independence_wave_package_incident_close_'+slot+'_shown');assert len(m.queued)==1
 results.append({'slot':slot,'baseline_gap_reproduced':True,'new_snapshot_rejects_stale':True,'due_date_preserved':True,'duplicate_delivery_and_close_before_reuse_blocked':True})

m=Model();m.normal['independence_wave_package_incident_generation']=1;m.normal['independence_wave_package_incident_a_due_date']=m.date;m.flags.add('independence_wave_package_incident_a_scheduled');m.call('independence_wave_package_incident_capture_a_shown');m.call('independence_wave_clear_package_incident_runtime');m.normal['independence_wave_generation_id']=2;m.call('independence_wave_schedule_package_incident_a');due=m.normal['independence_wave_package_incident_a_due_date'];m.date+=13*24/100000;m.call('independence_wave_package_incident_close_a_shown');assert m.queued==[('chaosx.nr6.101',32*24)] and m.normal['independence_wave_package_incident_a_due_date']==due
unknown=Model(999);unknown.call('independence_wave_schedule_package_incident_a');assert not unknown.queued and not unknown.flags

def event_bodies(t):return {next(v for k,v,_,_ in b if k=='id'):b for k,b,_,_ in parse(t) if k=='country_event'}
before=(old_path/'006_independence_wave_package_incident_events.txt').read_text(encoding='utf-8-sig');after=Path('events/006_independence_wave_package_incident_events.txt').read_text(encoding='utf-8-sig');b=event_bodies(before);a=event_bodies(after)
def shape(n):return [(k,shape(v) if isinstance(v,list) else v) for k,v,_,_ in n]
assert set(a)==set(b)==set(maps['slots'])
for eid,body in b.items():
 original=[(k,v,0,0) for k,v,_,_ in body if k not in ('immediate','after')]
 current=[(k,v,0,0) for k,v,_,_ in a[eid] if k not in ('immediate','after')]
 assert shape(original)==shape(current),eid
 old_options=[before[s:e] for k,v,s,e in body if k=='option']
 new_options=[after[s:e] for k,v,s,e in a[eid] if k=='option']
 assert old_options==new_options,eid

# Old B and current A may coexist, but each AFTER releases only its own slot.
mixed=Model();mixed.normal.update(independence_wave_package_incident_generation=1,independence_wave_package_incident_b_due_date=mixed.date);mixed.flags.add('independence_wave_package_incident_b_scheduled');mixed.call('independence_wave_package_incident_capture_b_shown');mixed.call('independence_wave_clear_package_incident_runtime');mixed.normal['independence_wave_generation_id']=2;mixed.call('independence_wave_schedule_package_incident_a');mixed.date=mixed.normal['independence_wave_package_incident_a_due_date'];mixed.call('independence_wave_package_incident_capture_a_shown');assert mixed.trigger(triggers['can_resolve_independence_wave_package_incident_a']);assert not mixed.trigger(triggers['can_resolve_independence_wave_package_incident_b']);mixed.call('independence_wave_package_incident_close_b_shown');assert 'independence_wave_package_incident_a_shown' in mixed.flags and mixed.trigger(triggers['can_resolve_independence_wave_package_incident_a']);mixed.flags.add('independence_wave_package_incident_a_resolved');mixed.call('independence_wave_schedule_package_incident_b');assert mixed.queued[-1]==('chaosx.nr6.102',150*24)
out={'coverage':'Source interpreter with declared active-origin oracle, documented date converter, and queued meta-event records; no native popup/timing/economy simulation.','preserved_mappings':mapping_count,'preserved_events':len(a),'preserved_options_and_ai':len(a)*2,'slot_cases':results,'early_closure_remaining_hours':32*24,'unknown_package_no_appointment':True,'arbitrary_closed_handler_replay_after_slot_reuse_not_proven':True}
out['all_260_option_bodies_byte_identical']=True
out['old_b_closure_preserves_current_a']=True
out['valid_current_a_schedules_b_at_original_150_day_delay']=True
(Path(__file__).resolve().parent/'source_case_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
