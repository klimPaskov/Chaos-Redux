// New cold-source projection cases, not retries of lost GUI requests. Writes nothing.
const m=require('./source_frame_tests.js'),assert=require('assert/strict');
const base=JSON.parse(require('fs').readFileSync('docs/plans/033_acid_rain_plans/validation/gui_current_2026_10_07/abi_repair/final_source_replay.json','utf8')).projectionFixtures;
const out={};
for(const phase of ['regional_one','regional_two','regional_three','global','aftercare_static','regional_two_static','global_static']){
 const s=structuredClone(base[phase]),saved={...s.variables,'global.date':100,'global.acid_rain_phase':s.variables['global.acid_rain_phase']};
 for(let r=1;r<=7;r++){saved['global.acid_rain_region_valid_entries^'+r]=s.variables['global.acid_rain_gui_region_'+r+'_eligible'];saved['global.acid_rain_region_touched_entries^'+r]=s.variables['global.acid_rain_gui_region_'+r+'_touched'];}
 const visible=phase.startsWith('regional')?phase.startsWith('regional_one')?1:phase.startsWith('regional_two')?2:3:0;
 for(let i=1;i<=3;i++){
  const p='global.acid_rain_gui_front_'+i+'_';
  saved['global.acid_rain_front_state_entries^'+i]=i<=visible?s.variables[p+'warning']?1:2:0;
  saved['global.acid_rain_front_region_entries^'+i]=i<=visible?s.variables[p+'region']:0;
  saved['global.acid_rain_front_intensity_entries^'+i]=s.variables[p+'intensity'];
  saved['global.acid_rain_front_active_state_count_entries^'+i]=s.variables[p+'active_states'];
  saved['global.acid_rain_front_next_work_day_entries^'+i]=100+s.variables[p+'movement_days'];
  saved['global.acid_rain_front_next_warning_day_entries^'+i]=100+s.variables[p+'movement_days'];
  saved['global.acid_rain_front_visited_entries^'+i]=30;
  saved['global.acid_rain_front_target_goal_entries^'+i]=40;
 }
 if(visible>1){const severeFront=phase.startsWith('regional_two')?1:2;saved['global.acid_rain_severe_cell_front_entries^1']=severeFront;saved['global.acid_rain_severe_cell_end_entries^1']=120;saved['global.acid_rain_severe_cell_target_count_entries^1']=s.variables['global.acid_rain_gui_front_'+severeFront+'_severe_state_count'];}
 // The real refresh reset/phase-admission tranche and complete nested bodies.
 const c=m.ctx(saved);for(const[k,v]of Object.entries(s.flags))if(v)c.flags.add(k);
 if(visible)c.flags.add('acid_rain_runtime_active');c.t.set('break',1);
 for(const name of ['acid_rain_gui_region_facts_regions_break','acid_rain_gui_region_facts_fronts_break','acid_rain_gui_region_facts_severe_break','acid_rain_gui_front_1_severe_break','acid_rain_gui_front_2_severe_break','acid_rain_gui_front_3_severe_break'])c.t.set(name,1);
 const refresh=m.current.defs.get('acid_rain_gui_refresh_read_only');
 const start=refresh.findIndex(n=>n.key==='set_variable'&&Array.isArray(n.value)&&n.value[0].key==='global.acid_rain_gui_front_1_visible');
 const end=refresh.findIndex(n=>n.key==='acid_rain_gui_project_region_facts');
 assert.ok(start>=0&&end>start);m.run(refresh.slice(start,end+1),c,m.current);
 if(phase.startsWith('global')||phase==='aftercare_static'){
  c.g.set('global.acid_rain_gui_superstorm_list_count',3);
  for(let i=0;i<3;i++){c.g.set('global.acid_rain_superstorm_ids^'+i,21+i);c.g.set('global.acid_rain_superstorm_region_entries^'+(21+i),1);c.g.set('global.acid_rain_superstorm_active_entries^'+(21+i),i===0?0:1);c.g.set('global.acid_rain_superstorm_target_count_entries^'+(21+i),6-i);}
  const at=refresh.findIndex(n=>n.key==='set_variable'&&Array.isArray(n.value)&&n.value[0].key==='global.acid_rain_gui_superstorm_1_visible');
  m.run(refresh.slice(at),c,m.current);
 }
 for(const[k,v]of c.g)if(k.startsWith('global.acid_rain_gui_')){s.variables[k]=v;s.values[k]=v;}
 for(const[k,v]of c.c)if(k.startsWith('acid_rain_gui_')){s.variables[k]=v;s.values[k]=v;}
 // Native display strings are resolved from the actual unchanged selectors and YML.
 for(const key of Object.keys(s.values).filter(k=>k.startsWith('This.Get'))){const name=key.slice(5);if(m.current.texts.has(name))s.values[key]=m.getter(name,c,m.current);}
 for(let r=1;r<=7;r++)s.values['This.GetAcidRainRegion'+r+'Tooltip']=m.getter('GetAcidRainRegion'+r+'Tooltip',c,m.current);
 s.values['This.GetAcidRainPreparednessTooltip']=m.getter('GetAcidRainPreparednessTooltip',c,m.current);
 assert.equal(m.num('break',c),1);
 out[phase]={scenario:s,trace:c.trace.map(t=>({helper:t.helper,inheritedCount:t.inherited.length,discardedNames:t.discarded})),loopVisits:c.visits.length,declaredRuntimeInputs:Object.fromEntries(Object.entries(saved).filter(([k])=>!k.includes('acid_rain_gui_'))),declaredBaseFixture:phase,declaredCallerTemps:{break:1,privateBreaks:1},executedSource:'Actual refresh front-reset/admission/region-publication tranche, complete projectors and region/getter helpers, actual three-call superstorm tail. Remaining GUI ledger/country facts are declared inputs. Date converter remains fixture-relative stub, not native time.'};
}
const chosen=process.argv[2];
console.log(JSON.stringify({hashes:{effects:m.sha(m.current.guiPath),scriptedLoc:m.sha(m.current.slPath)},fixtures:chosen?{[chosen]:out[chosen]}:out,limits:'Conservative source frames with shared scoped saved maps, not gameplay/native execution or full refresh prefix.'}));

