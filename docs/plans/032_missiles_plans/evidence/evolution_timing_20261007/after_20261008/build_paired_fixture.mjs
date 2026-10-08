import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const base=path.resolve('docs/plans/032_missiles_plans/evidence/evolution_timing_20261007');
const out=path.join(base,'after_20261008');
const originalPath=path.join(base,'scenarioSet.json');
const originalBytes=fs.readFileSync(originalPath);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
if(sha(originalBytes)!=='2f5136de919f4e1b1a3b9459e061a9ce3d80c69e16e6aff401eb6cc49ac89608') throw Error('Original fixture changed');
const original=JSON.parse(originalBytes);
const source=p=>fs.readFileSync(path.join(out,'source',p),'utf8');
const constants=source('common/script_constants/032_missiles_constants.txt');
function constant(token){
  const [category,key]=token.replace(/^constant:/,'').split('.');
  const start=constants.indexOf('\n'+category+' = {');
  if(start<0) throw Error('Unknown constant group '+category);
  const tail=constants.slice(start+1);
  const next=tail.slice(category.length+4).search(/\n\w+ = \{/);
  const block=next<0?tail:tail.slice(0,category.length+4+next);
  const m=new RegExp('^\\s*'+key+' = (-?\\d+(?:\\.\\d+)?)\\s*$','m').exec(block);
  if(!m) throw Error('Unknown numeric constant '+token);
  return Number(m[1]);
}
const mtth=source('common/mtth/032_missiles_evolution_mtth.txt');
const tracks=[
 {key:'rogue_launch_commands',short:'rogue',id:201,base:'rogue_days',entry:'missiles_rogue_evolution_mtth',few:'vulnerable',fewLimit:'constant:missiles_evolution_pacing.widespread_vulnerable_programs'},
 {key:'unreliable_guidance',short:'guidance',id:202,base:'guidance_days',entry:'missiles_guidance_evolution_mtth',few:'operational',fewLimit:'constant:missiles_evolution_pressure.minimum_operational_programs'},
 {key:'saturation',short:'saturation',id:203,base:'saturation_days',entry:'missiles_saturation_evolution_mtth',few:'operational',fewLimit:'constant:missiles_evolution_pressure.minimum_operational_programs'},
 {key:'special_warheads',short:'special',id:204,base:'special_days',entry:'missiles_special_evolution_mtth',few:'payload_owners',fewLimit:'constant:missiles_evolution_pacing.special_pressure_payload_owners'},
 {key:'automatic_retaliation',short:'retaliation',id:205,base:'retaliation_days',entry:'missiles_retaliation_evolution_mtth',few:'responders',fewLimit:'constant:missiles_evolution_pressure.minimum_retaliation_programs'}
];
const trace=[];
const scenarios=original.scenarios.map(old=>{
 const s=structuredClone(old), v=s.state;
 for(const [k,x] of Object.entries(v)) if(k.startsWith('missiles_pressure_'))v['global.'+k]=x;
 const countries=s.scopePools[0].candidates;
 const op=countries.filter(c=>c.state.missiles_program_stage>=2);
 let pairs=0;
 for(let i=0;i<op.length;i++)for(let j=i+1;j<op.length;j++)
  if((op[i].state.has_war_with??[]).includes(op[j].id)||(op[j].state.has_war_with??[]).includes(op[i].id))pairs++;
 // All listed sites are stipulated controlled, launchable, hardened and secure.
 // This is a cache-input contract. It is not execution of the source recount.
 const responders=op.filter(c=>c.state.missiles_program_stage>=4&&c.state.missiles_command_control>=75&&c.state.missiles_operational_reserve>=4).length;
 v['global.missiles_pressure_hostile_pairs']=pairs;
 v['global.missiles_pressure_responders']=responders;
 v['global.missiles_pressure_mature']=countries.filter(c=>c.state.missiles_program_stage>=6).length;
 v['global.missiles_pressure_reserve']=countries.reduce((n,c)=>n+c.state.missiles_operational_reserve,0);
 v['global.missiles_pressure_observation_generation']=1;
 v['global.missiles_evolution_host_id']=1; v.id=1; v.exists=true;
 v['flag.missiles_program_initialized']=true;
 v['flag.missiles_program_cleanup_complete']=false;
 v['flag.missiles_pressure_observation_ready']=true;
 v['flag.missiles_evolution_observing']=false;
 const chaos=v['global.chaos_meter_value'];
 const tier=chaos>=1000?5:Math.floor(chaos/200);
 v['flag.chaos_tier']=true; v['flag.chaos_tier.value']=tier;
 const high={
  rogue:v['global.missiles_pressure_vulnerable']>=constant('constant:missiles_evolution_pacing.widespread_vulnerable_programs'),
  guidance:v['global.missiles_pressure_war']>=constant('constant:missiles_evolution_pressure.minimum_war_programs')||(v['global.missiles_pressure_launches']>=constant('constant:missiles_evolution_pacing.launch_strain_threshold')&&v['global.missiles_pressure_low_readiness']>=constant('constant:missiles_evolution_pacing.minimum_strained_programs')),
  saturation:v['global.missiles_pressure_war']>=constant('constant:missiles_evolution_pacing.saturation_pressure_war_programs'),
  special:v['global.missiles_pressure_payload_owners']>=constant('constant:missiles_evolution_pacing.special_pressure_payload_owners'),
  retaliation:pairs>=constant('constant:missiles_evolution_pacing.retaliation_pressure_pairs')
 };
 for(const t of tracks){
  const pos=mtth.indexOf(t.entry+' = {'); if(pos<0)throw Error('Missing actual MTTH entry');
  const block=mtth.slice(pos).split(/\n\}/)[0];
  const baseToken=/base = (constant:[\w.]+)/.exec(block)?.[1];
  const factors=[...block.matchAll(/factor = (constant:[\w.]+)/g)].map(x=>x[1]);
  if(baseToken!=='constant:missiles_evolution_timing.'+t.base||factors.length!==3||!block.includes('var = global.missiles_pressure_'+t.few)||!block.includes(t.fewLimit))throw Error('MTTH entry differs from reviewed shape '+t.entry);
  const baseDays=constant(baseToken), applies=[v['global.missiles_pressure_'+t.few]<constant(t.fewLimit),high[t.short],tier===5];
  let days=baseDays;
  const modifiers=factors.map((factor,i)=>{const n=constant(factor); if(applies[i])days*=n;return {sourceConstant:factor,value:n,applied:applies[i],valueAfter:days};});
  v['global.missiles_evolution_'+t.short+'_mtth_days']=days;
  const prefix='flag.missiles_evolution_'+t.key;
  // Stale armed clocks deliberately exercise the native eligibility/disable/recorded gates.
  v[prefix+'_pending']=true;
  v[prefix+'_native_pending']=s.id!=='EVO-PACE';
  v[prefix+'_short_pending']=s.id==='EVO-PACE';
  delete v['global.missiles_evolution_'+t.key+'_due_date'];
  if(s.id==='EVO-PACE')v['global.missiles_evolution_'+t.key+'_due_date']=1;
  trace.push({scenarioId:s.id,eventId:'chaosx.nr32.'+t.id,entry:t.entry,baseToken,baseDays,fewUsableCount:v['global.missiles_pressure_'+t.few],fewThreshold:constant(t.fewLimit),highPressure:high[t.short],chaosTier:tier,modifiers,declaredCacheDays:days,classification:'source-derived conditional input, not an MCP output or publication test'});
 }
 const hostState={id:1,exists:true,'flag.missiles_program_initialized':true,'flag.missiles_program_cleanup_complete':false};
 const host={id:'GER',type:'country',actor:'GER',state:hostState,flags:['missiles_program_initialized']};
 s.scopes={ROOT:structuredClone(host),THIS:structuredClone(host),'var:global.missiles_evolution_host':structuredClone(host)};
 delete s.scopePools; // No country iteration occurs inside these native gates.
 s.flags=Object.entries(v).filter(([k,x])=>k.startsWith('flag.')&&!k.endsWith('.value')&&x===true).map(([k])=>k.slice(5));
 s.uncertainInputs=[]; s.schedule=[];
 return s;
});
const paired={schemaVersion:'1.0',id:'E32_EVOLUTION_NATIVE_PAIRED_V2_20261008',workspaceId:original.workspaceId,surfaceHint:'event_mean_time_to_happen',description:'Explicit v2 binding of the preserved thirteen EVO intents to cached native clocks. Conditional on complete publication, one host and static state. Source-derived cache-day inputs are recorded separately. Old delay has no recognized adapter. EVO-PACE uses finite short mode and cannot prove short-clock cadence.',scenarios};
const notes={
 original:{path:originalPath,sha256:sha(originalBytes)},pairedId:paired.id,
 boundary:'Conditional clock entry after publication and arming. This is an explicit phase change from the original before-arming fixture.',
 mappings:['Original pressure temporaries remain and gain actual global aliases.','Unordered operational hostile pairs are recalculated from declared wars, with no other wars, war goals or justifications stipulated. Old responding-endpoint scalar is retained under its original temporary key.','Responders are separate from pairs. All declared program sites are stipulated controlled, active, hardened and secure. Their actual publication is unproved.','Mature count uses stage >= 6. Reserve sums declared country reserves.','GER is the only host. Numeric engine id=1 and cached host_id=1 are synthetic equality facts, not a claim about GER actual native ID. Typed country binding id remains GER.','All ordinary cases have pending/native flags true, including stale clocks in negative cases so exclusion must follow their native gates.','EVO-PACE is in short mode, pending=true, native=false, short=true, due-date present. Due value 1 tests presence only, not native date encoding or a deadline.','EVO-11 disable and EVO-12 unlocked/legacy flags are preserved.','Date remains 1939.1.1. global.date is intentionally absent and unused by ordinary native gates. No simulated external uncertainty or state schedule.','No candidateOverrides, helper truth overrides, inline probability proxy, or invented future source field is supplied.'],
 candidatePool:{ids:tracks.map(t=>'chaosx.nr32.'+t.id),complete:true,normalization:'not applicable, independent clocks'},
 externalCompleteness:'Complete declared primitives for the native gate/day factor are intended. Actual pressure publication, site/scoped-world reconstruction, global native-id getter, trigger polling phase, rejection after refresh, finite short pacing and lifecycle hooks are outside this conditional model.',
 cacheInputAuthority:'Actual frozen common/mtth/032_missiles_evolution_mtth.txt and numeric constants. High-pressure trigger predicates were directly reviewed from frozen operations triggers. Cache traces are calculation/review evidence only.',
 artifacts:{mtthSourceSha256:sha(fs.readFileSync(path.join(out,'source/common/mtth/032_missiles_evolution_mtth.txt')))},
 simulationSeed:null,horizonDays:365,
 originalUniformDeltaGap:'The old helper is unsupported by direct_random and event MTTH. No exact numeric before/after delta can be claimed from an empty before adapter.',
 schemaStatus:'Validate the saved paired object before any MCP evaluation.'
};
function write(name,obj){const p=path.join(out,name);fs.writeFileSync(p,typeof obj==='string'?obj:JSON.stringify(obj,null,2)+'\n',{flag:'wx'});return {path:p,sha256:sha(fs.readFileSync(p)),bytes:fs.statSync(p).size};}
const saved=[write('scenarioSet.paired.v2.json',paired),write('paired_mapping.v2.json',notes),write('cache_input_traces.v2.json',trace)];
const threshold=structuredClone(paired);threshold.id='E32_EVOLUTION_AUTO_THRESHOLD_V1_20261008';threshold.description='Two-point diagnostic of native automatic-retaliation chaos gate. Cache M fixed at reviewed EVO-10 value. Not a pressure-publication sweep.';threshold.scenarios=threshold.scenarios.filter(s=>s.id==='EVO-10');threshold.scenarios[0].uncertainInputs=[{path:'global.chaos_meter_value',range:{min:899,max:900}}];
saved.push(write('scenarioSet.threshold.v1.json',threshold));
console.log(JSON.stringify({saved,cacheDays:trace.filter(t=>['EVO-01','EVO-03','EVO-04','EVO-05','EVO-08','EVO-10','EVO-PACE'].includes(t.scenarioId)).map(t=>({scenario:t.scenarioId,event:t.eventId,M:t.declaredCacheDays}))}));
