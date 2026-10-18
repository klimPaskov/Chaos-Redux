/* Event033 F5 source replay. Test/report only, no filesystem writes.
 * Separate helper temp frames are a conservative test contract, not native proof.
 * Explicit spies terminate geography, impacts, finance and presentation bodies.
 * Run: node .tools/validation/test_033_evolution_controls.js [--json]
 */
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const assert = require('assert/strict');
const root = path.resolve(__dirname, '../..');
const base = 'docs/plans/033_acid_rain_plans/validation/probability/evolution_controls_2026_10_08/';
const fxPath = 'common/scripted_effects/033_acid_rain_effects.txt';
const trPath = 'common/scripted_triggers/033_acid_rain_triggers.txt';
const coPath = 'common/script_constants/033_acid_rain_constants.txt';
const settingsPath = 'common/scripted_triggers/chaosx_settings_triggers.txt';
const dynamicPath = 'common/scripted_effects/chaosx_dynamic_effects.txt';
const constantPaths = [coPath, 'common/script_constants/chaos_meter_constants.txt', 'common/script_constants/chaosx_date_units_constants.txt'];
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const read = p => fs.readFileSync(path.join(root, p));
const inventory = [];
function load(p) { const b = read(p); inventory.push({path:p, bytes:b.length, sha256:sha(b)}); return b.toString('utf8'); }
function parse(s, file) {
 const ts=[]; const re=/#[^\r\n]*|"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>#]+/g;
 let m, line=1, end=0;
 while ((m=re.exec(s))) { line+=(s.slice(end,m.index).match(/\n/g)||[]).length; end=re.lastIndex; if(m[0][0]!=='#') ts.push({t:m[0],at:m.index,end:re.lastIndex,line}); line+=(m[0].match(/\n/g)||[]).length; }
 let i=0;
 function body(nested=false) {
  const out=[];
  while(i<ts.length && ts[i].t!=='}') {
   const a=ts[i++], op=ts[i]?.t;
   if(a.t==='{') { out.push({key:'__anonymous',value:body(true),file,line:a.line,start:a.at,end:ts[i-1].end}); continue; }
   if(!['=','<','>'].includes(op)) { out.push({key:'__atom',value:a.t,file,line:a.line,start:a.at,end:a.end}); continue; }
   i++; const b=ts[i++]; assert(b,`missing value ${file}:${a.line}`);
   const value=b.t==='{'?body(true):b.t;
   out.push({key:a.t,op,value,file,line:a.line,start:a.at,end:ts[i-1].end});
  }
  if(nested) { assert.equal(ts[i]?.t,'}',`unclosed ${file}`); i++; }
  return out;
 }
 const out=body(); assert.equal(i,ts.length,`unparsed ${file}`); return out;
}
const field=(nodes,k)=>nodes.find(n=>n.key===k)?.value;
const bodyOf=n=>n.value.filter(x=>x.key!=='limit');
const limitOf=n=>field(n.value,'limit');
function walk(nodes, fn) { for(const n of nodes) { fn(n); if(Array.isArray(n.value)) walk(n.value,fn); } }
const bare=s=>s.startsWith('"')?JSON.parse(s):s;
// hidden_trigger only hides tooltip text (f63ab274b); the engine evaluates its content in place, so shapes compare spliced.
const clean=n=>({key:n.key,op:n.op,value:Array.isArray(n.value)?n.value.flatMap(x=>x.key==='hidden_trigger'&&Array.isArray(x.value)?x.value.map(clean):[clean(x)]):n.value});
function sourceSet(prefix) {
 const defs=new Map(), texts=new Map(), constants=new Map();
 for(const p of [fxPath,trPath,settingsPath,dynamicPath,...constantPaths]) {
  const f=prefix+p, text=load(f), nodes=parse(text,f); texts.set(p,text);
  if(constantPaths.includes(p)) {
   function flatten(ns,k) { for(const n of ns) { if(n.key==='schema') continue; const name=k?`${k}.${n.key}`:n.key; if(Array.isArray(n.value)) flatten(n.value,name); else if(/^-?\d+(\.\d+)?$/.test(n.value)) constants.set('constant:'+name,Number(n.value)); } }
   flatten(nodes,'');
  } else for(const n of nodes) if(Array.isArray(n.value)) { assert(!defs.has(n.key),`duplicate loaded helper ${n.key}`); defs.set(n.key,n); }
 }
 return {defs,texts,constants,prefix};
}
const before=sourceSet(base+'before-source/'), after=sourceSet('');
before.label='before_E455';after.label='current_71F0';
const archivePath='docs/plans/033_acid_rain_plans/validation/evolution_controls_source_replay_2026_10_08_8b85_historical.json';
const archive=JSON.parse(load(archivePath));
const zlib=require('zlib');
for(const x of archive.files) {const b=zlib.gunzipSync(Buffer.from(x.rawBytes,'base64'));assert.equal(b.length,x.bytes);assert.equal(sha(b),x.sha256,`historical bytes changed ${x.path}`);}
for(const x of archive.sourceSnapshots) {assert.equal(sha(read(x.path)),x.sha256,`historical source changed ${x.path}`);}
assert.equal(archive.originalSummary.tests,130);assert.equal(archive.originalSummary.failed,0);
assert.equal(archive.files.find(x=>x.path==='.tools/validation/test_033_evolution_controls.js').sha256,'abe6b9115f09e68a30f54751fef5634bc28bb5ece8213a5a0c90370cf12e1f6f');
const historicalRuntimePath=base+'after_8b85ebaf/'+fxPath;
const historicalRuntime=load(historicalRuntimePath);
const historicalSource={...after,defs:new Map(after.defs),texts:new Map(after.texts),label:'historical_8B85'};
for(const n of parse(historicalRuntime,historicalRuntimePath))if(Array.isArray(n.value))historicalSource.defs.set(n.key,n);
historicalSource.texts.set(fxPath,historicalRuntime);
// The live owner runtime, triggers, constants and shared dependencies are replayed as they are. The frozen archives and the E455
// baseline stay hash-checked above, and a source change during the run still invalidates the receipt.
const originalReceipt=JSON.parse(zlib.gunzipSync(Buffer.from(archive.files.find(x=>x.path.endsWith('evolution_controls_source_replay_2026_10_08.json')).rawBytes,'base64')).toString('utf8'));
assert.equal(inventory.find(x=>x.path===base+'before-source/'+fxPath).sha256,'e455292b55d0443abb234a00506b9501b02f8c2a8df5afe298ff855f56cb406f');
const contractsPath=base+'scenario_contracts_E455_v2.json';
const contracts=JSON.parse(load(contractsPath));
assert.equal(inventory.find(x=>x.path===contractsPath).sha256,'cbe062db33aa23dd53d12f8b2bf8b9fb028b066c9b6118a408d0cb424e341ffa');
const arithmetic=JSON.parse(load(base+'chance_arithmetic_E455.json'));
const manifest=JSON.parse(read(base+'source_manifest.json'));
for(const x of inventory.filter(x=>x.path.startsWith(base+'before-source/'))) {
 const frozen=manifest.files.find(f=>base+f.path===x.path); assert(frozen,`unmanifested ${x.path}`); assert.equal(x.sha256,frozen.sha256);
}
const ctrlFlag=i=>`events_log_disabled_evolution_33_33_${i}`;
const controlNames=['severe','multiple_fronts','global'];
const pending=['acid_rain_severe_transition_pending','acid_rain_front_split_pending','acid_rain_global_transition_active'];
const due=['global.acid_rain_severe_transition_day','global.acid_rain_front_split_day','global.acid_rain_global_warning_day'];
const trialHelpers=['acid_rain_try_severe_evolution','acid_rain_try_multiple_fronts','acid_rain_try_global_evolution'];
const flagUniverse=new Set([ctrlFlag(1),ctrlFlag(2),ctrlFlag(3),'acid_rain_registry_frozen','acid_rain_gui_window_open']);
for(const s of [before,after]) for(const d of s.defs.values()) walk(d.value,n=>{ if(/^(has|set|clr)_(global|country|state)_flag$/.test(n.key) && typeof n.value==='string' && !n.value.includes('[')) flagUniverse.add(bare(n.value)); });
const delegated = {
 acid_rain_assign_next_front_region:'Geography fixture returns caller-preinitialized front_region_result. No region selection, weighting, coverage, or impact is executed.',
 acid_rain_create_severe_cell:'Whole geography/reservation creator delegated after actual severe chance, roll, front-slot selection and admission. Optional explicitly declared reservation count fixture only.',
 acid_rain_begin_global_transition:'Current first-if guard executed. All admitted array/geography/global-opening transition body delegated with an admission witness only. No global Chaos or impact is synthesized.',
 acid_rain_create_superstorm_forecast:'Actual entry guard executed. Admitted array/geography reservation body delegated with an explicit forecast-count increment fixture.',
 record_events_log_evolution_entry:'Shared logger sink spy records supplied context only. Logger arrays and UI not executed.',
 add_chaos_meter_value:'Shared Chaos sink spy records supplied amount only. No global meter/history or financial mutations executed.',
 acid_rain_apply_state_pulse:'Impact callback witness only, no population or Famine execution and no fabricated successful receipt.',
 acid_rain_apply_state_damage:'Damage callback witness only, no damage or receipt fabricated.',
 acid_rain_advance_consequence_interval:'Consequence accounting delegated, no mutation.',
 acid_rain_033_achievement_close_runtime_episode:'Achievement accounting delegated, no mutation.',
 acid_rain_reconcile_state_consequences:'Consequence modifier reconciliation delegated, no mutation.',
 acid_rain_close_state_evacuation:'Transfer/financial queue closure delegated, no mutation.',
 acid_rain_refresh_country_forecast_status:'Presentation projection delegated, no mutation.',
 acid_rain_interrupt_for_world_end:'Terminal interruption delegated. Fixture explicitly has world_end absent.',
 acid_rain_refresh_country_project_quotes:'Quote/financial body delegated.',
 acid_rain_refresh_country_action_quotes:'Quote/financial body delegated.',
 acid_rain_process_front:'Regional processing body delegated. Host dispatch only executed.',
 acid_rain_pulse_front_states:'Regional impact body delegated. Host dispatch only executed.',
 acid_rain_pulse_global_states:'Global impact body delegated. Host dispatch only executed.',
 acid_rain_try_weekly_air_request:'Air request body delegated.',
 acid_rain_refresh_active_consequences:'Consequence maintenance body delegated.',
 acid_rain_project_country_obligations:'Paid commitment projection delegated.',
 acid_rain_033_achievement_check_runtime_country:'Achievement check delegated.',
 acid_rain_gui_refresh_national_strip:'GUI projection delegated.',
 acid_rain_gui_refresh_read_only:'GUI projection delegated.',
 acid_rain_bind_host_and_schedule_worker:'Host scheduling delegated.',
 acid_rain_apply_dissipation_step:'Array-heavy closure delegated. Endpoint admission only executed.'
};
const coverage=new Map(), helperCoverage=new Map(), spyCounts=new Map(), results=[];
function helperHit(source,name) {const id=source.label+':'+name;helperCoverage.set(id,(helperCoverage.get(id)||0)+1);}
function recordCoverage(n) { const id=`${n.file}:${n.line}:${n.key}`; coverage.set(id,(coverage.get(id)||0)+1); }
const scalarDefaults={
 'global.acid_rain_generation_id':7, 'global.acid_rain_start_chaos':0, 'global.acid_rain_runtime_start_day':100,
 'global.date':100.0108, 'global.chaos_meter_value':800, 'global.acid_rain_front_count':1,
 'global.acid_rain_phase':2, 'global.acid_rain_severe_cell_count':0, 'global.acid_rain_severe_next_check_day':200,
 'global.acid_rain_superstorm_capacity':2, 'global.acid_rain_superstorm_forecast_count':0,
 'global.acid_rain_superstorm_count':0, 'global.acid_rain_global_transition_day':100,
 'global.acid_rain_pulse_sequence':10, 'global.acid_rain_total_touched_states':5,
 'global.acid_rain_total_valid_states':5, 'global.acid_rain_dissipation_check_index':0,
 'global.acid_rain_air_current_bp':0, 'global.acid_rain_next_dissipation_check_day':200,
 'global.acid_rain_global_minimum_dissipation_day':200,
 // Historical sentinels are never mutated by delegated bodies.
 'global.acid_rain_total_deaths':12345, 'global.acid_rain_country_commitment_receipt_count':99,
 'global.acid_rain_coverage_receipt_count':17, 'global.acid_rain_achievement_receipt_count':13
};
const absentDefaults=[...due,'global.acid_rain_third_front_retry_day'];
class Replay {
 constructor(source,c={},opts={}) {
  this.source=source; this.temp=new Map(Object.entries(opts.temp||{})); this.scope={type:'country',id:'CXT'}; this.scopes=new Map([['country:CXT',new Map()]]);
  this.global=new Map(Object.entries({...scalarDefaults,...c.state})); this.absent=new Set(absentDefaults.filter(k=>!this.global.has(k)));
  this.flags=new Set(c.flags||['acid_rain_runtime_active']); this.scopeFlags=new Map(); this.arrays=new Map(); this.events=[]; this.calls=[]; this.rolls=[]; this.meta=[]; this.frames=[];this.scopeChecks=[];
  this.opts={geographyResult:1,severeReservationIncrement:0,...opts}; this.facts={acid_rain_all_regions_are_complete:false,...opts.facts};
  this.targets=new Map([['acid_rain_runtime_host',this.scope]]); this.framesDiscarded=[];
  this.arrays.set('global.acid_rain_participant_countries',[this.scope]);
  this.arrays.set('global.acid_rain_frozen_states',[{type:'state',id:'fixture_state',scopeExists:true}]);
  this.arrays.set('global.acid_rain_frozen_state_ids',[101]);
  this.arrays.set('global.acid_rain_severe_target_states',[]); this.arrays.set('global.acid_rain_superstorm_target_states',[]); this.arrays.set('global.acid_rain_superstorm_ids',[1]);
  for(let i=1;i<=source.constants.get('constant:acid_rain_event.max_fronts');i++) for(const k of ['state','intensity','region','visited','severe_cooldown_day']) this.global.set(`global.acid_rain_front_${k}_entries^${i}`,0);
  for(const kind of ['severe_cell','superstorm']) for(let i=1;i<=source.constants.get(`constant:acid_rain_event.max_${kind==='severe_cell'?'severe_cells':'superstorms'}`);i++) for(const k of ['active','start','end','front','death','damage','low_preparedness_exposure','supply_disruption','region']) this.global.set(`global.acid_rain_${kind}_${k}_entries^${i}`,0);
  for(const [k,v] of Object.entries(c.state||{})) this.global.set(k,v);
  this.seedState();
 }
 seedState(kind) {
  // Positive native facts are explicit, not inferred from an array index or pointer.
  const st={type:'state',id:'fixture_state',scopeExists:true}, key=this.scopeKey(st); this.scopes.set(key,new Map([['acid_rain_registry_generation',7],['acid_rain_consequence_generation',7]])); this.scopeFlags.set(key,new Set(['acid_rain_frozen_valid']));
  if(!kind) return;
  // The storm-clock repair (23f8aa8c9) makes workers act only on states whose exact current-generation slot/forecast record
  // matches the global episode entry. The frozen lifecycle contracts predate that record, so it is declared here: the state
  // carries forecast generation, id, start and end equal to the global entry (a missing start entry is placed before the end).
  const slot=kind==='severe'?'severe_cell':'superstorm', start=`global.acid_rain_${slot}_start_entries^1`, end=`global.acid_rain_${slot}_end_entries^1`;
  if(!(this.global.get(start)>0)) this.global.set(start,this.global.get(end)-3*0.00024);
  if(kind==='superstorm'&&!(this.global.get('global.acid_rain_superstorm_episode_entries^1')>0)) this.global.set('global.acid_rain_superstorm_episode_entries^1',1);
  for(const [k,v] of [[`acid_rain_${kind}_forecast_generation`,7],[`acid_rain_${kind}_forecast_id`,1],[`acid_rain_${kind}_forecast_start_day`,this.global.get(start)],[`acid_rain_${kind}_forecast_end_day`,this.global.get(end)]]) this.scopes.get(key).set(k,v);
  this.scopes.get(key).set(`acid_rain_${kind==='severe'?'severe_cell':'superstorm'}_id`,1);
  this.scopeFlags.get(key).add(`acid_rain_${kind==='severe'?'severe_cell':'superstorm'}_target`);
  this.scopeFlags.get(key).add(`acid_rain_${kind}_forecast_pending`);
  if(kind==='severe') this.scopeFlags.get(key).add('acid_rain_severe_episode_impacted');
  this.absent.add(`${key}:acid_rain_${kind==='severe'?'severe_cell':'superstorm'}_opening_recorded`);
  this.arrays.set(`global.acid_rain_${kind==='severe'?'severe':'superstorm'}_target_states`,[st]);
 }
 scopeKey(s=this.scope) { assert(s && ['state','country'].includes(s.type) && typeof s.id==='string','typed scope required'); return `${s.type}:${s.id}`; }
 store(k,temporary=false) { if(temporary) { assert(!k.startsWith('global.'),'scoped temporary rejected'); return this.temp; } if(k.startsWith('global.')) return this.global; return this.scopes.get(this.scopeKey()); }
 key(k) { const a=k.indexOf('^'); if(a<0) return k; const index=k.slice(a+1); return k.slice(0,a+1)+(index==='num'?'num':this.number(index)); }
 number(v) { const x=this.value(v); assert.equal(typeof x,'number',`numeric pointer arithmetic prohibited: ${v}`); assert(Number.isFinite(x),`nonfinite ${v}`); return x; }
 value(v) {
  assert.equal(typeof v,'string',`non-scalar ${JSON.stringify(v)}`); if(/^-?\d+(\.\d+)?$/.test(v)) return Number(v);
  if(v.startsWith('constant:')) { assert(this.source.constants.has(v),`unknown constant ${v}`); return this.source.constants.get(v); }
  if(v==='THIS') return this.scope;
  const k=this.key(v);
  if(k.endsWith('^num')) { const a=this.array(k.slice(0,-4)); return a.length; }
  if(!k.startsWith('global.') && this.temp.has(k)) return this.temp.get(k);
  const st=this.store(k); if(st?.has(k)) return st.get(k);
  if(this.absent.has(k) || this.absent.has(`${this.scopeKey()}:${k}`)) return 0;
  throw Error(`unresolved dynamic fact ${k} in ${this.scopeKey()}`);
 }
 has(v) { const k=this.key(v); if((!k.startsWith('global.') && this.temp.has(k)) || this.store(k)?.has(k))return true;assert(this.absent.has(k)||this.absent.has(`${this.scopeKey()}:${k}`),`undeclared variable absence ${k}`);return false; }
 put(k,v,tmp=false) { k=this.key(k); this.store(k,tmp).set(k,v); this.absent.delete(k); this.absent.delete(`${this.scopeKey()}:${k}`); }
 array(v) { if(this.temp.has(v)) { assert(Array.isArray(this.temp.get(v)),`not array ${v}`); return this.temp.get(v); } assert(this.arrays.has(v),`undeclared array ${v}`); return this.arrays.get(v); }
 knownFlag(f) { assert(flagUniverse.has(f),`undeclared flag ${f}`); }
 flag(f,scope=false) { this.knownFlag(f); return scope?this.scopeFlags.get(this.scopeKey())?.has(f)||false:this.flags.has(f); }
 child(fn,name) {
  const parent=this.temp, child=new Map(parent); this.temp=child;
  try { return fn(); } finally {
   const discarded=[...child.keys()].filter(k=>!parent.has(k));
   for(const k of parent.keys()) { if(child.has(k)) parent.set(k,child.get(k)); else parent.delete(k); }
   this.framesDiscarded.push({helper:name,discarded}); this.temp=parent;
  }
 }
 cmp(a,b,op) { const eps=1e-10; switch(op) { case '=':case 'equals':return Math.abs(a-b)<eps;case 'not_equals':return Math.abs(a-b)>=eps;case '<':case 'less_than':return a<b-eps;case '>':case 'greater_than':return a>b+eps;case 'less_than_or_equals':return a<=b+eps;case 'greater_than_or_equals':return a>=b-eps;default:throw Error(`unknown comparison ${op}`); } }
 check(ns) { const v=field(ns,'var'); if(v) return this.cmp(this.number(v),this.number(field(ns,'value')),field(ns,'compare')||'='); assert.equal(ns.length,1); return this.cmp(this.number(ns[0].key),this.number(ns[0].value),ns[0].op); }
 trig(ns,mode='AND') {
  if(mode==='NOT') return !ns.some(n=>this.pred(n));
  if(mode==='OR') return ns.some(n=>this.pred(n));
  for(const n of ns) if(!this.pred(n)) return false; return true;
 }
 pred(n) {
  recordCoverage(n); const k=n.key, v=n.value;
  if(['AND','OR','NOT'].includes(k)) return this.trig(v,k);
  if(k==='hidden_trigger') return this.trig(v);
  if(k==='check_variable') return this.check(v);
  if(k==='has_variable') return !!this.has(v);
  if(k==='has_global_flag') return this.flag(Array.isArray(v)?field(v,'flag'):v);
  if(k==='has_country_flag'||k==='has_state_flag') return this.flag(v,true);
  if(k==='has_event_target') return this.targets.has(v);
  if(k==='scope_exists') {assert.equal(typeof this.scope.scopeExists,'boolean',`undeclared scope-existence fact ${this.scopeKey()}`);return this.scope.scopeExists===(v==='yes');}
  if(k==='all_of_scopes') {
   const parent=this.scope, visit={array:field(v,'array'),visits:[],result:true};this.scopeChecks.push(visit);
   try {
    for(const s of this.array(visit.array)) {
     this.scopeKey(s);assert.equal(s.type,'state','this fixture declares frozen states only');this.scope=s;
     const matched=this.trig(v.filter(x=>x.key!=='array'));visit.visits.push({scope:this.scopeKey(),matched});
     if(!matched) {visit.result=false;return false;}
    }
    return true;
   } finally {this.scope=parent;}
  }
  if(k==='is_ai') { assert.equal(this.scope.type,'country'); assert.equal(this.opts.fixtureIsAi,false);return v==='no'; }
  if(k==='meta_trigger') {
   const replacements={};
   for(const a of v.filter(x=>!['text','debug'].includes(x.key))) {
    const match=/^\[\?([^|]+)\|(?:\.0|0)\]$/.exec(bare(a.value)); assert(match,`unsupported meta replacement ${a.value}`); replacements[a.key]=String(Math.round(this.number(match[1])));
   }
   const substitute=x=>typeof x==='string'?x.replace(/\[([A-Z_]+)\]/g,(_,key)=>{assert(key in replacements,`missing meta ${key}`);return replacements[key];}):x.map(n=>({...n,key:substitute(n.key),value:substitute(n.value)}));
   const text=substitute(field(v,'text')); this.meta.push({replacements,expanded:text.map(clean)}); return this.trig(text);
  }
  if(k==='set_temp_variable') { this.effect(n); return true; }
  if(k in this.facts) { assert.equal(typeof this.facts[k],'boolean'); return this.facts[k]===(v==='yes'); }
  if(this.source.defs.has(k)) {helperHit(this.source,k);return this.child(()=>this.trig(this.source.defs.get(k).value),k)===(v==='yes');}
  throw Error(`unknown trigger ${k} at ${n.file}:${n.line}`);
 }
 invoke(k) {
  this.calls.push(k); helperHit(this.source,k);const d=this.source.defs.get(k);
  if(k in delegated) {
   spyCounts.set(k,(spyCounts.get(k)||0)+1);
   return this.child(()=>{
    if(k==='acid_rain_begin_global_transition'||k==='acid_rain_create_superstorm_forecast') {
     assert(d,`missing boundary ${k}`);
     // Execute the actual outer guard on each side, including baseline's weaker guard.
     const guarded=d.value.length===1 && d.value[0].key==='if';
     if(this.source===after)assert(guarded,`current delegated boundary must remain completely guarded: ${k}`);
     const admitted=guarded?this.trig(limitOf(d.value[0])):true;
     this.events.push({spy:k,admitted,guardExecuted:guarded,bodyDelegated:admitted});
     if(admitted && k==='acid_rain_create_superstorm_forecast') this.put('global.acid_rain_superstorm_forecast_count',this.number('global.acid_rain_superstorm_forecast_count')+1);
    } else if(k==='acid_rain_assign_next_front_region') {
     this.put('acid_rain_front_region_result',this.opts.geographyResult,true); this.events.push({spy:k,result:this.opts.geographyResult});
    } else if(k==='acid_rain_create_severe_cell') {
     this.put('global.acid_rain_severe_cell_count',this.number('global.acid_rain_severe_cell_count')+this.opts.severeReservationIncrement); this.events.push({spy:k,reservationIncrement:this.opts.severeReservationIncrement});
    } else if(k==='record_events_log_evolution_entry') {
     this.events.push({spy:k,context:Object.fromEntries(['event_id','type','stage','tier','has_actor'].map(v=>[v,this.number('events_log_evolution_'+v)]))});
    } else if(k==='add_chaos_meter_value') this.events.push({spy:k,amount:this.number('chaos_change')});
    else this.events.push({spy:k,scope:this.scopeKey()});
   },k);
  }
  assert(d,`unknown effect helper ${k}`); return this.child(()=>this.exec(d.value),k);
 }
 exec(ns) {
  for(let i=0;i<ns.length;i++) {
   const n=ns[i];
   if(n.key==='if') {
    let taken=false;
    do {
     const b=ns[i]; recordCoverage(b);
     if(!taken && (b.key==='else'||this.trig(limitOf(b)))) { taken=true; this.exec(bodyOf(b)); }
     if(!['else_if','else'].includes(ns[i+1]?.key)) break; i++;
    } while(true);
   } else this.effect(n);
  }
 }
 effect(n) {
  recordCoverage(n); const k=n.key, v=n.value;
  if(/^(set|add_to|subtract_from|multiply|divide)_(temp_)?variable$/.test(k)) {
   const tmp=k.includes('_temp_'), a=field(v,'var')?{key:field(v,'var'),value:field(v,'value')}:v[0]; assert(a);
   const rhs=this.value(a.value); let out=rhs;
   if(!k.startsWith('set_')) { const lhs=this.number(a.key); assert.equal(typeof rhs,'number'); if(k.startsWith('add_'))out=lhs+rhs;if(k.startsWith('subtract_'))out=lhs-rhs;if(k.startsWith('multiply_'))out=lhs*rhs;if(k.startsWith('divide_')) {assert.notEqual(rhs,0);out=lhs/rhs;} }
   this.put(a.key,out,tmp); return;
  }
  if(/^round_(temp_)?variable$/.test(k)) { this.put(v,Math.round(this.number(v)),k.includes('_temp_')); return; }
  if(/^clamp_(temp_)?variable$/.test(k)) { const name=field(v,'var'); let x=this.number(name); if(field(v,'min'))x=Math.max(x,this.number(field(v,'min')));if(field(v,'max'))x=Math.min(x,this.number(field(v,'max')));this.put(name,x,k.includes('_temp_'));return; }
  if(/^set_(temp_)?variable_to_random$/.test(k)) {
   const name=field(v,'var'), min=this.number(field(v,'min')), max=this.number(field(v,'max')); assert.equal(field(v,'integer'),'yes');
   assert(name in (this.opts.rolls||{}),`undeclared roll fixture ${name}`); const value=this.opts.rolls[name]; assert(Number.isInteger(value)&&value>=min&&value<max,`roll out of bounds ${name}`);
   this.rolls.push({name,min,max,integer:true,value,temp:k.includes('_temp_')}); this.put(name,value,k.includes('_temp_')); return;
  }
  if(k==='clear_variable'||k==='clear_temp_variable') { const key=this.key(v); this.store(key,k.includes('_temp_')).delete(key);this.absent.add(key);return; }
  if(/^(set|clr)_(global|country|state)_flag$/.test(k)) {
   assert.equal(typeof v,'string'); this.knownFlag(v); let set=this.flags;
   if(!k.includes('_global_')) {const key=this.scopeKey();if(!this.scopeFlags.has(key))this.scopeFlags.set(key,new Set());set=this.scopeFlags.get(key);}
   k.startsWith('set_')?set.add(v):set.delete(v);return;
  }
  if(k==='clear_temp_array') { this.temp.set(v,[]);return; }
  if(k==='add_to_temp_array'||k==='remove_from_array') {
   const name=field(v,'array'), value=this.value(field(v,'value')), arr=this.array(name);
   if(k==='add_to_temp_array')arr.push(value);else { const id=JSON.stringify(value),at=arr.findIndex(x=>JSON.stringify(x)===id);if(at>=0)arr.splice(at,1); } return;
  }
  if(k==='for_loop_effect'||k==='while_loop_effect'||k==='for_each_scope_loop') {
   const stop=field(v,'break')||'break', b=v.filter(x=>!['break','start','end','value','array','limit','add'].includes(x.key));
   if(k==='for_each_scope_loop') { const parent=this.scope; for(const s of [...this.array(field(v,'array'))]) { if(this.number(stop)!==0)break;this.scopeKey(s);this.scope=s;this.exec(b); } this.scope=parent;return; }
   if(k==='for_loop_effect') { const start=this.number(field(v,'start')),end=this.number(field(v,'end')),step=field(v,'add')?this.number(field(v,'add')):1,name=field(v,'value');assert(step>0);for(let x=start,count=0;x<end&&count<1000;x+=step,count++){if(this.number(stop)!==0)break;this.put(name,x,true);this.exec(b);}return; }
   for(let count=0;count<1000 && this.number(stop)===0 && this.trig(field(v,'limit'));count++)this.exec(b);return;
  }
  if(k==='country_event'||k==='news_event') { assert.equal(this.scope.type,'country');this.events.push({nativeDispatch:k,event:field(v,'id'),scope:this.scopeKey()});return; }
  if(k==='save_event_target_as') { this.targets.set(v,this.scope);return; }
  if(k.startsWith('event_target:')) { const name=k.slice(13);assert(this.targets.has(name));const old=this.scope;this.scope=this.targets.get(name);this.exec(v);this.scope=old;return; }
  if(k==='CONTROLLER') { assert.equal(this.scope.type,'state');const old=this.scope;this.scope={type:'country',id:'CXT'};this.exec(v);this.scope=old;return; }
  if(v==='yes' && (this.source.defs.has(k)||k in delegated)) { this.invoke(k);return; }
  throw Error(`unknown effect ${k} at ${n.file}:${n.line}`);
 }
 state() {return {globals:Object.fromEntries(this.global),flags:[...this.flags].sort(),scoped:Object.fromEntries([...this.scopes].map(([k,v])=>[k,Object.fromEntries(v)])),scopeFlags:Object.fromEntries([...this.scopeFlags].map(([k,v])=>[k,[...v].sort()])),arrays:Object.fromEntries(this.arrays)};}
}
function test(id,fn) { try { const evidence=fn()||{};results.push({id,status:'pass',...evidence}); } catch(e) { results.push({id,status:'fail',error:e.stack}); } }
const rolls={acid_rain_severe_roll:100,acid_rain_third_front_roll:100,acid_rain_dissipation_roll:100,acid_rain_dissipation_retry_days:10,chaosx_date_days:18};
function replay(s,c,o={}) { return new Replay(s,c,{rolls,fixtureIsAi:false,...o}); }
const historyKeys=['global.acid_rain_total_deaths','global.acid_rain_country_commitment_receipt_count','global.acid_rain_coverage_receipt_count','global.acid_rain_achievement_receipt_count'];
function historical(r,initial) { for(const k of historyKeys)assert.equal(r.number(k),initial[k]); }
function pendingExpected(r,stage,yes) { assert.equal(r.flags.has(pending[stage-1]),yes); if(!yes)assert(!r.calls.includes('acid_rain_begin_global_transition')); }
function evidence(r) { return {calls:r.calls,events:r.events,rolls:r.rolls,metaExpansions:r.meta.length,scopeChecks:r.scopeChecks}; }
// 24 immutable masks, missing/stale context and duplicate no-Chaos formation.
for(const c of contracts.formationCases) test(c.id,()=>{
 const variants=[];
 for(const ambient of [{}, {events_log_evolution_event_id:999,events_log_evolution_type:2,events_log_evolution_stage:9,events_log_evolution_tier:5}]) {
  const r=replay(after,c,{temp:ambient}); const initial=r.state();r.invoke('acid_rain_apply_formation_stage');
  const stages=[];if(r.flags.has('acid_rain_severe_unlocked'))stages.push(1);if(r.calls.includes('acid_rain_open_additional_front'))stages.push(2);if(r.flags.has(pending[2]))stages.push(3);
  // 0a2927e9b: an eligible global opening skips ordinary region selection, so the second-front opening does not run beside it.
  const expectedStages=c.acceptedEligibleFormationStages.includes(3)?c.acceptedEligibleFormationStages.filter(x=>x!==2):c.acceptedEligibleFormationStages;
  assert.deepEqual(stages,expectedStages);
  assert.equal(r.number('global.acid_rain_highest_stage_at_formation'),c.acceptedHighestStageAtFormation);
  assert(!r.calls.includes('add_chaos_meter_value'));const snapshot=r.state(),eventCount=r.events.length;r.invoke('acid_rain_apply_formation_stage');assert.deepEqual(r.state(),snapshot);assert.equal(r.events.length,eventCount);
  historical(r,initial.globals);if(Object.keys(ambient).length===0)for(const k of ['event_id','type','stage','tier'])assert(!r.temp.has('events_log_evolution_'+k));
  variants.push({ambient:Object.keys(ambient).length?'stale':'missing',stages,highest:r.number('global.acid_rain_highest_stage_at_formation'),metaExpansions:r.meta.length,duplicateUnchanged:true});
 }
 const old=replay(before,c);old.invoke('acid_rain_apply_formation_stage');assert.equal(old.number('global.acid_rain_highest_stage_at_formation'),c.baselineHighestStageAtFormation);
 const oldStages=[];if(old.flags.has('acid_rain_severe_unlocked'))oldStages.push(1);if(old.calls.includes('acid_rain_open_additional_front'))oldStages.push(2);if(old.flags.has(pending[2]))oldStages.push(3);assert.deepEqual(oldStages,c.baselineSourceBranchStages);
 return {variants,beforeStages:oldStages,beforeHigh:old.number('global.acid_rain_highest_stage_at_formation'),negativeBeforeDiffers:JSON.stringify(oldStages)!==JSON.stringify(c.acceptedEligibleFormationStages)};
});
// Shared meta-trigger execution through child storage, tier mapping and sibling independence.
for(let stage=1;stage<=3;stage++) for(const enabled of [true,false]) for(const chaos of [stage*200+199,stage*200+200]) test(`CTX_${stage}_${enabled?'enabled':'disabled'}_${chaos}`,()=>{
 const flags=['acid_rain_runtime_active',...([1,2,3].filter(i=>i!==stage||!enabled).map(ctrlFlag))],r=replay(after,{flags,state:{'global.chaos_meter_value':chaos}});
 const helper=`acid_rain_${controlNames[stage-1]}_evolution_is_enabled`,result=r.child(()=>r.trig(after.defs.get(helper).value),helper);
 assert.equal(result,enabled&&chaos>=stage*200+200);assert(!r.temp.has('events_log_evolution_stage'));
 assert(r.meta.some(x=>x.replacements.EVOLUTION_EVENT_ID==='33'&&x.replacements.EVOLUTION_TYPE==='33'&&x.replacements.EVOLUTION_STAGE===String(stage)));
 const disableOnly=`acid_rain_${controlNames[stage-1]}_evolution_is_not_disabled`;assert.equal(r.child(()=>r.trig(after.defs.get(disableOnly).value),disableOnly),enabled);
 return {result,actualMeta:r.meta,childStorageDiscarded:true};
});
// Every named lifecycle contract uses its frozen state plus declared fixture facts.
for(const c of contracts.liveLifecycleCases) test(c.id,()=>{
 const r=replay(after,c),initial=r.state();
 if(c.call==='acid_rain_process_severe_cells')r.seedState('severe');
 if(c.id.startsWith('H3_')) { r.global.set('global.acid_rain_next_dissipation_check_day',r.number('global.date')); r.global.set('global.acid_rain_global_minimum_dissipation_day',r.number('global.date')); }
 r.invoke(c.call);historical(r,initial.globals);
 if(c.id.startsWith('L')||c.id.startsWith('R')) { const enabled=!c.id.includes('disabled');pendingExpected(r,c.stage,enabled);if(enabled)assert(r.number(due[c.stage-1])>r.number('global.date')); }
 if(c.id.startsWith('P')) {pendingExpected(r,c.stage,false);assert(!r.has(due[c.stage-1]));if(c.stage===3)assert.equal(r.number('global.acid_rain_phase'),2);}
 if(c.id==='C1_disable_pending_cell_forecast') {assert.equal(r.number('global.acid_rain_severe_cell_active_entries^1'),1);assert(r.calls.includes('acid_rain_apply_state_pulse'));}
 if(c.id.startsWith('H1_')) {assert.equal(r.number('global.acid_rain_severe_cell_active_entries^1'),2);assert(r.scopeFlags.get('state:fixture_state').has('acid_rain_severe_history'));}
 if(c.id.startsWith('H2_')) {assert.equal(r.number('global.acid_rain_front_count'),2);assert(r.flags.has('acid_rain_multiple_fronts_unlocked'));assert(r.calls.includes('acid_rain_process_front'));}
 if(c.id.startsWith('H3_')) {assert(r.flags.has('acid_rain_global_layer_active'));assert.equal(r.number('global.acid_rain_phase'),4);assert(r.calls.includes('acid_rain_pulse_global_states'));assert(r.calls.includes('acid_rain_try_dissipation_check'));}
 if(c.id==='B3_global_disabled_ordinary_coverage') {assert(r.calls.includes('acid_rain_process_front'));assert(!r.flags.has(pending[2]));}
 if(c.id==='D3_disabled_direct_global_commit') {assert(r.events.some(e=>e.spy===c.call&&!e.admitted));assert.deepEqual(r.state(),initial);}
 return {frozenContract:c.id,oldContextTier:c.sharedContextRequired?.events_log_evolution_tier,currentContextTier:c.stage+1,declaredCompletionFacts:r.facts,...evidence(r)};
});
// Pending Chaos dip, actual sequential cancellation, pause and re-enable.
for(let stage=1;stage<=3;stage++) test(`SEQ_${stage}_cancel_reenable_due`,()=>{
 const r=replay(after,{flags:['acid_rain_runtime_active','acid_rain_registry_frozen',pending[stage-1]],state:{'global.chaos_meter_value':stage*200+199,[due[stage-1]]:100.0108,'global.acid_rain_phase':stage===3?3:2}});
 r.invoke(trialHelpers[stage-1]);pendingExpected(r,stage,false);assert(!r.has(due[stage-1]));if(stage===3)assert.equal(r.number('global.acid_rain_phase'),2);
 r.global.set('global.chaos_meter_value',stage*200+200);r.invoke(trialHelpers[stage-1]);pendingExpected(r,stage,true);const fresh=r.number(due[stage-1]);assert(fresh>r.number('global.date'));
 r.flags.add(ctrlFlag(stage));r.invoke(trialHelpers[stage-1]);pendingExpected(r,stage,false);r.flags.delete(ctrlFlag(stage));r.invoke(trialHelpers[stage-1]);assert.equal(r.number(due[stage-1]),fresh);
 r.global.set('global.date',fresh);r.invoke(trialHelpers[stage-1]);
 if(stage===1)assert(r.flags.has('acid_rain_severe_unlocked'));
 if(stage===2)assert(r.flags.has('acid_rain_multiple_fronts_unlocked'));
 if(stage===3)assert(r.events.some(e=>e.spy==='acid_rain_begin_global_transition'&&e.admitted));
 return {freshNotice:fresh,...evidence(r)};
});
for(const kind of ['severe','third','global']) test(`FORECAST_${kind}_pause_resume`,()=>{
 const stage=kind==='severe'?1:kind==='third'?2:3,helper=kind==='global'?'acid_rain_try_extra_superstorm':trialHelpers[stage-1];
 const unlocked=kind==='severe'?'acid_rain_severe_unlocked':kind==='third'?'acid_rain_multiple_fronts_unlocked':'acid_rain_global_layer_active';
 const r=replay(after,{flags:['acid_rain_runtime_active',unlocked,ctrlFlag(stage)],state:{'global.chaos_meter_value':kind==='global'?900:800,'global.acid_rain_front_count':kind==='third'?2:1,'global.acid_rain_severe_next_check_day':100,'global.acid_rain_phase':kind==='global'?4:2}}, {rolls:{...rolls,acid_rain_severe_roll:1,acid_rain_third_front_roll:1},severeReservationIncrement:1});
 r.global.set('global.acid_rain_front_state_entries^1',2);r.global.set('global.acid_rain_front_severe_cooldown_day_entries^1',100);
 r.invoke(helper);assert.equal(r.rolls.length,0);assert(!r.calls.includes('acid_rain_create_severe_cell'));assert(!r.calls.includes('acid_rain_open_additional_front'));assert(!r.calls.includes('acid_rain_create_superstorm_forecast'));
 if(kind==='global')assert.equal(r.number('global.acid_rain_superstorm_capacity'),2);
 r.flags.delete(ctrlFlag(stage));r.invoke(helper);
 if(kind==='severe')assert(r.calls.includes('acid_rain_create_severe_cell'));
 if(kind==='third')assert(r.flags.has('acid_rain_third_front_resolved'));
 if(kind==='global') {assert(r.number('global.acid_rain_superstorm_capacity')>=3);assert(r.number('global.acid_rain_superstorm_forecast_count')>=3);}
 return evidence(r);
});
// Direct commit guard rejection is observed before delegated mutation boundaries.
for(const rejection of ['disabled','belowTier','inactive','missingGeneration','notFrozen','emptyRegistry','mismatchedArrayLengths','noWarning','alreadyActive','earlyClock','missingClock','staleMirror','missingStateMarker','missingStateGeneration']) test(`DIRECT_GLOBAL_${rejection}`,()=>{
 const r=replay(after,{flags:['acid_rain_runtime_active','acid_rain_registry_frozen',pending[2]],state:{'global.acid_rain_phase':3,[due[2]]:100.0108}});
 if(rejection==='disabled')r.flags.add(ctrlFlag(3));if(rejection==='belowTier')r.global.set('global.chaos_meter_value',799);if(rejection==='inactive')r.flags.delete('acid_rain_runtime_active');
 if(rejection==='missingGeneration'){r.global.delete('global.acid_rain_generation_id');r.absent.add('global.acid_rain_generation_id');}
 if(rejection==='notFrozen')r.flags.delete('acid_rain_registry_frozen');if(rejection==='emptyRegistry'){r.arrays.set('global.acid_rain_frozen_states',[]);r.arrays.set('global.acid_rain_frozen_state_ids',[]);}
 if(rejection==='mismatchedArrayLengths')r.arrays.set('global.acid_rain_frozen_state_ids',[]);if(rejection==='noWarning')r.flags.delete(pending[2]);if(rejection==='alreadyActive')r.flags.add('acid_rain_global_layer_active');
 if(rejection==='earlyClock')r.global.set(due[2],100.01104);
 if(rejection==='missingClock'){r.global.delete(due[2]);r.absent.add(due[2]);}
 if(rejection==='staleMirror')r.scopes.get('state:fixture_state').set('acid_rain_registry_generation',6);
 if(rejection==='missingStateMarker')r.scopeFlags.get('state:fixture_state').delete('acid_rain_frozen_valid');
 if(rejection==='missingStateGeneration'){r.scopes.get('state:fixture_state').delete('acid_rain_registry_generation');r.absent.add('state:fixture_state:acid_rain_registry_generation');}
 const snapshot=r.state();r.invoke('acid_rain_begin_global_transition');assert.deepEqual(r.state(),snapshot);assert.equal(r.events.at(-1).admitted,false);return evidence(r);
});
test('DIRECT_GLOBAL_valid_guard_only',()=>{const r=replay(after,{flags:['acid_rain_runtime_active','acid_rain_registry_frozen',pending[2]],state:{[due[2]]:100.0108}});r.invoke('acid_rain_begin_global_transition');assert.equal(r.events.at(-1).admitted,true);assert.deepEqual(r.scopeChecks[0].visits,[{scope:'state:fixture_state',matched:true}]);assert.equal(r.scopeKey(),'country:CXT');return evidence(r);});
test('DIRECT_GLOBAL_stale_state_mirror_boundary_limit',()=>{
 const facts={flags:['acid_rain_runtime_active','acid_rain_registry_frozen',pending[2]],state:{[due[2]]:100.0108}};
 const r=replay(after,facts);
 r.scopes.get('state:fixture_state').set('acid_rain_registry_generation',6);
 const snapshot=r.state();r.invoke('acid_rain_begin_global_transition');assert.equal(r.events.at(-1).admitted,false);assert.equal(r.events.at(-1).bodyDelegated,false);assert.deepEqual(r.state(),snapshot);assert.equal(r.scopeKey(),'country:CXT');
 const old=replay(historicalSource,facts);old.scopes.get('state:fixture_state').set('acid_rain_registry_generation',6);old.invoke('acid_rain_begin_global_transition');assert.equal(old.events.at(-1).admitted,true);
 return {historical8B85Admitted:true,current71F0Rejected:true,actualStatePredicate:true,...evidence(r)};
});
for(const clock of ['early','missing'])test(`DIRECT_GLOBAL_${clock}_clock_8B85_negative`,()=>{
 const facts={flags:['acid_rain_runtime_active','acid_rain_registry_frozen',pending[2]],state:clock==='early'?{[due[2]]:100.01104}:{}};
 const old=replay(historicalSource,facts);old.invoke('acid_rain_begin_global_transition');assert.equal(old.events.at(-1).admitted,true);
 const r=replay(after,facts),snapshot=r.state();r.invoke('acid_rain_begin_global_transition');assert.equal(r.events.at(-1).admitted,false);assert.equal(r.events.at(-1).bodyDelegated,false);assert.deepEqual(r.state(),snapshot);assert.equal(r.scopeChecks.length,0);
 return {historical8B85Admitted:true,current71F0Rejected:true,rejectedBeforeStateTraversal:true,...evidence(r)};
});
for(const invalid of ['none','staleSecond','missingMarkerSecond','missingGenerationSecond'])test(`DIRECT_GLOBAL_two_states_${invalid}`,()=>{
 const r=replay(after,{flags:['acid_rain_runtime_active','acid_rain_registry_frozen',pending[2]],state:{[due[2]]:100.0108}});
 const second={type:'state',id:'fixture_state_2',scopeExists:true};
 r.arrays.get('global.acid_rain_frozen_states').push(second);r.arrays.get('global.acid_rain_frozen_state_ids').push(102);
 r.scopes.set('state:fixture_state_2',new Map([['acid_rain_registry_generation',invalid==='staleSecond'?6:7]]));r.scopeFlags.set('state:fixture_state_2',new Set(invalid==='missingMarkerSecond'?[]:['acid_rain_frozen_valid']));
 if(invalid==='missingGenerationSecond'){r.scopes.get('state:fixture_state_2').delete('acid_rain_registry_generation');r.absent.add('state:fixture_state_2:acid_rain_registry_generation');}
 const snapshot=r.state();r.invoke('acid_rain_begin_global_transition');const admitted=invalid==='none';assert.equal(r.events.at(-1).admitted,admitted);assert.equal(r.events.at(-1).bodyDelegated,admitted);assert.deepEqual(r.state(),snapshot);assert.equal(r.scopeKey(),'country:CXT');
 assert.deepEqual(r.scopeChecks[0].visits,[{scope:'state:fixture_state',matched:true},{scope:'state:fixture_state_2',matched:admitted}]);
 const visits=r.scopeChecks.length;r.invoke('acid_rain_begin_global_transition');assert.equal(r.scopeChecks.length,visits+1);assert.deepEqual(r.scopeChecks.at(-1).visits,r.scopeChecks[0].visits);assert.deepEqual(r.state(),snapshot);
 return {declaredSecondScope:second,declaredSecondGeneration:invalid==='missingGenerationSecond'?'explicitly absent':invalid==='staleSecond'?6:7,repeatGuardUnchanged:true,...evidence(r)};
});
for(const stage of [1,2,3]) test(`BEFORE_disabled_notice_reproduction_${stage}`,()=>{
 const c=contracts.liveLifecycleCases.find(x=>x.id===`L${stage}_disabled_notice`),r=replay(before,c);r.invoke(c.call);assert(r.flags.has(pending[stage-1]));return {negativeBeforeAdmitted:true,...evidence(r)};
});
// Reserved superstorm notice/endpoint survives its disabled control and low Chaos.
for(const endpoint of [false,true]) test(`RESERVED_STORM_${endpoint?'endpoint':'activation'}_disabled_lowChaos`,()=>{
 const r=replay(after,{flags:['acid_rain_runtime_active','acid_rain_global_layer_active',ctrlFlag(3)],state:{'global.chaos_meter_value':0,'global.acid_rain_superstorm_start_entries^1':endpoint?100.0108-3*0.00024:100.0108,'global.acid_rain_superstorm_end_entries^1':endpoint?100.0108:100.02,'global.acid_rain_superstorm_forecast_count':1}});r.seedState('superstorm');r.invoke('acid_rain_process_superstorms');
 // Storm pulses dispatch only inside start <= now < end (23f8aa8c9). Activation at the start pulses and records history; an
 // unactivated reservation that reaches its end retires with no pulse and no impact history, and neither path creates a forecast.
 assert.equal(r.number('global.acid_rain_superstorm_active_entries^1'),endpoint?2:1);
 assert.equal(r.calls.includes('acid_rain_apply_state_pulse'),!endpoint);
 assert.equal(r.scopeFlags.get('state:fixture_state').has('acid_rain_superstorm_history'),!endpoint);
 assert(!r.calls.includes('acid_rain_create_superstorm_forecast'));return evidence(r);
});
test('THIRD_STABLE_receipt_plus5_without_false_stageIII',()=>{
 const r=replay(after,{flags:['acid_rain_runtime_active','acid_rain_multiple_fronts_unlocked','acid_rain_second_front_stable_receipt',ctrlFlag(3)],state:{'global.acid_rain_front_count':3}});
 for(let i=1;i<=3;i++){r.global.set(`global.acid_rain_front_state_entries^${i}`,2);r.global.set(`global.acid_rain_front_visited_entries^${i}`,1);}
 r.invoke('acid_rain_check_stable_fronts');assert(r.flags.has('acid_rain_third_front_stable_receipt'));assert.deepEqual(r.events.filter(e=>e.spy==='add_chaos_meter_value').map(e=>e.amount),[5]);assert(!r.calls.includes('acid_rain_record_evolution'));
 const count=r.events.length;r.invoke('acid_rain_check_stable_fronts');assert.equal(r.events.length,count);
 const old=replay(before,{flags:['acid_rain_runtime_active','acid_rain_second_front_stable_receipt'],state:{'global.acid_rain_front_count':3}});for(let i=1;i<=3;i++){old.global.set(`global.acid_rain_front_state_entries^${i}`,2);old.global.set(`global.acid_rain_front_visited_entries^${i}`,1);}
 assert.throws(()=>old.invoke('acid_rain_check_stable_fronts'),/unresolved dynamic fact events_log_evolution_stage/);assert(old.calls.includes('acid_rain_record_evolution'));
 const oldThird=before.defs.get('acid_rain_check_stable_fronts').value[1];assert(oldThird);let stageIII=false;walk(oldThird.value,n=>{if(n.key==='set_temp_variable'&&field(n.value,'acid_rain_evolution_stage')==='constant:acid_rain_event.evolution_iii_stage')stageIII=true;});assert(stageIII);
 return {beforeFalseStageIIILogAttempt:true,beforeLoggerContextUnresolved:true,afterNoEvolutionRow:true,...evidence(r)};
});
test('SECOND_STABLE_actual_log_context_bridge',()=>{
 const r=replay(after,{flags:['acid_rain_runtime_active','acid_rain_multiple_fronts_unlocked'],state:{'global.acid_rain_front_count':2}});
 for(let i=1;i<=2;i++){r.global.set(`global.acid_rain_front_state_entries^${i}`,2);r.global.set(`global.acid_rain_front_visited_entries^${i}`,1);}
 r.invoke('acid_rain_check_stable_fronts');assert(r.flags.has('acid_rain_second_front_stable_receipt'));
 assert.deepEqual(r.events.filter(e=>e.spy==='record_events_log_evolution_entry').map(e=>e.context),[{event_id:33,type:33,stage:2,tier:3,has_actor:1}]);assert(!r.flags.has('acid_rain_third_front_stable_receipt'));
 return {sharedLoggerSinkOnly:true,...evidence(r)};
});
// Execute complete scalar chance paths using identical explicit bounded roll fixtures.
for(const c of arithmetic.derivation) for(const kind of ['severe','third']) test(`SCALAR_${c.id}_${kind}`,()=>{
 if(kind==='third'&&c.inputs.currentChaos<600)return {notAdmitted:true,reason:'Frozen third-front admission threshold 600. No forced bypass.'};
 const observations=[];
 const expectedChance=c[kind==='severe'?'severeChance':'thirdChance'];
 const boundaryRolls=[...new Set([100,Math.max(1,expectedChance),Math.max(1,expectedChance+1)])];
 for(const s of [before,after]) {
  const sourceObservations=[];
  for(const chosenRoll of boundaryRolls) {
  const inp=c.inputs, r=replay(s,{flags:['acid_rain_runtime_active',kind==='severe'?'acid_rain_severe_unlocked':'acid_rain_multiple_fronts_unlocked'],state:{'global.chaos_meter_value':inp.currentChaos,'global.acid_rain_start_chaos':400,'global.date':100+inp.ageDays*0.00024,'global.acid_rain_front_count':kind==='third'?2:1,'global.acid_rain_severe_cell_count':inp.globalSevereCellCount,'global.acid_rain_severe_next_check_day':100}}, {temp:{[kind==='severe'?'acid_rain_severe_chance':'acid_rain_third_front_chance']:0},rolls:{...rolls,[kind==='severe'?'acid_rain_severe_roll':'acid_rain_third_front_roll']:chosenRoll}});
  for(let i=1;i<=3;i++)r.global.set(`global.acid_rain_front_intensity_entries^${i}`,inp.intensityEntries[i-1]);r.global.set('global.acid_rain_front_state_entries^1',2);r.invoke(kind==='severe'?trialHelpers[0]:trialHelpers[1]);
  const name=kind==='severe'?'acid_rain_severe_chance':'acid_rain_third_front_chance';assert.equal(r.number(name),expectedChance);assert.equal(r.rolls.length,1);assert.deepEqual({min:r.rolls[0].min,max:r.rolls[0].max,temp:r.rolls[0].temp},{min:1,max:101,temp:false});
  const admitted=r.calls.includes(kind==='severe'?'acid_rain_create_severe_cell':'acid_rain_open_additional_front');assert.equal(admitted,chosenRoll<=expectedChance);sourceObservations.push({chance:r.number(name),roll:r.rolls[0],outcomeBoundaryAdmitted:admitted});
  }
  observations.push(sourceObservations);
 }
 assert.deepEqual(observations[0],observations[1]);return {observations,notProbabilityAcceptance:true};
});
// Fail closed on undeclared commands/facts and typed-pointer arithmetic.
test('HARNESS_fail_closed_frames_and_typed_scopes',()=>{
 const r=replay(after);assert.throws(()=>r.number('unresolved_fixture_fact'),/unresolved dynamic fact/);assert.throws(()=>r.effect({key:'unknown_effect',value:'yes'}),/unknown effect/);assert.throws(()=>r.pred({key:'unknown_trigger',value:'yes'}),/unknown trigger/);assert.throws(()=>r.number('THIS'),/numeric pointer/);
 r.child(()=>r.put('new_child_storage',1,true),'negative_child');assert(!r.temp.has('new_child_storage'));r.put('outer_storage',0,true);r.child(()=>r.put('outer_storage',7,true),'positive_child');assert.equal(r.number('outer_storage'),7);
 r.put('outer_storage',99,false);assert.equal(r.number('outer_storage'),7);r.temp.delete('outer_storage');assert.equal(r.number('outer_storage'),99);return {unknownsFail:true,typedScopes:true,separateStorage:true};
});
test('HARNESS_frozen_predicate_unknown_fact_fails',()=>{
 const r=replay(after,{flags:['acid_rain_runtime_active','acid_rain_registry_frozen',pending[2]],state:{[due[2]]:100.0108}});
 r.scopes.get('state:fixture_state').delete('acid_rain_registry_generation');
 assert.throws(()=>r.invoke('acid_rain_begin_global_transition'),/undeclared variable absence acid_rain_registry_generation/);assert(!r.events.some(e=>e.admitted));assert.equal(r.scopeKey(),'country:CXT');
 return {undeclaredStateGenerationFails:true,noAdmittedBody:true};
});
// Actual shape preservation. No flattening or replacement of production bodies.
const preservation=[];
test('PRESERVE_71F0_exact_six_line_outer_limit_followup',()=>{
 const addition=Buffer.from('\t\t\thas_variable = global.acid_rain_global_warning_day\n\t\t\tcheck_variable = { var = global.date value = global.acid_rain_global_warning_day compare = greater_than_or_equals }\n\t\t\tall_of_scopes = {\n\t\t\t\tarray = global.acid_rain_frozen_states\n\t\t\t\tacid_rain_state_is_frozen_valid = yes\n\t\t\t}\n');
 const current=read(fxPath),prior=read(historicalRuntimePath),at=current.indexOf(addition);assert(at>=0);assert.equal(current.indexOf(addition,at+addition.length),-1);
 // The runtime has evolved since the 8B85 bytes (storm-clock repair, chunked traversal, formation opening, hidden flag checks),
 // so only the guard addition itself is pinned: it appears exactly once and inside the direct-global transition outer limit.
 const limit=after.defs.get('acid_rain_begin_global_transition').value[0];assert.equal(limit.key,'if');assert.deepEqual(field(limitOf(limit),'all_of_scopes').map(clean),[{key:'array',op:'=',value:'global.acid_rain_frozen_states'},{key:'acid_rain_state_is_frozen_valid',op:'=',value:'yes'}]);
 return {historicalRuntimeSha256:sha(prior),currentRuntimeSha256:sha(current),addedLines:6,addedBytes:addition.length,guardAppearsOnce:true};
});
// Rewritten on purpose after the E455 baseline, with their behaviour covered by the lifecycle cases above: the storm workers act
// only on owned active episodes (23f8aa8c9), the front opening and state pulse follow the formation opening and report-output
// repairs (0a2927e9b, e2f2c280e, 23f8aa8c9) and chunked regional traversal (d78785cd1, ca6acf248).
const rewrittenAfterBaseline=new Set(['acid_rain_process_severe_cells','acid_rain_process_superstorms','acid_rain_open_additional_front','acid_rain_apply_state_pulse']);
for(const name of ['acid_rain_process_severe_cells','acid_rain_process_superstorms','acid_rain_host_worker','acid_rain_try_dissipation_check','acid_rain_open_additional_front','acid_rain_apply_state_pulse','acid_rain_apply_state_damage','acid_rain_try_severe_impact_chaos']) test(`PRESERVE_${name}`,()=>{
 if(rewrittenAfterBaseline.has(name)){assert(after.defs.has(name),name+' stays defined');return {rewrittenAfterBaseline:true};}
 assert.deepEqual(before.defs.get(name).value.map(clean),after.defs.get(name).value.map(clean));preservation.push(name);return {sourceAstUnchanged:true};
});
test('PRESERVE_constants_except_display_tiers',()=>{
 // Only Acid Rain constants are in scope; the urgent action durations and map anchors were retuned later on purpose (92d525f47).
 const retuned=/^constant:acid_rain_(urgent_cost|gui_anchor)\./;
 const deltas=[];for(const [key,v] of before.constants)if(key.startsWith('constant:acid_rain_')&&!retuned.test(key)&&after.constants.get(key)!==v)deltas.push({key,before:v,after:after.constants.get(key)});
 assert.deepEqual(deltas,[{key:'constant:acid_rain_event.evolution_i_tier',before:1,after:2},{key:'constant:acid_rain_event.evolution_ii_tier',before:2,after:3},{key:'constant:acid_rain_event.evolution_iii_tier',before:3,after:4}]);return {deltas};
});
for(const name of ['is_current_evolution_enabled','has_disabled_current_evolution','has_reached_current_evolution_tier','chaosx_convert_days_to_date_offset','chaosx_convert_date_offset_to_days']) test(`PRESERVE_${name}`,()=>{assert.deepEqual(before.defs.get(name).value.map(clean),after.defs.get(name).value.map(clean));return {sourceAstUnchanged:true};});
for(const name of ['acid_rain_begin_global_transition','acid_rain_create_superstorm_forecast'])test(`PRESERVE_delegated_body_${name}`,()=>{
 const current=after.defs.get(name);assert.equal(current.value.length,1);assert.equal(current.value[0].key,'if');
 const original=before.defs.get(name),oldBody=bodyOf(original.value[0]);
 assert.deepEqual(bodyOf(current.value[0]).map(clean),oldBody.map(clean));return {sourceBodyUnchanged:true,guardChangeOnly:true};
});
const executedHelpers=[...helperCoverage.keys()].filter(k=>!(k.slice(k.indexOf(':')+1) in delegated));
for(const prior of originalReceipt.results)assert(results.some(x=>x.id===prior.id),`original case omitted ${prior.id}`);
assert.equal(results.length-originalReceipt.results.length,13,'unexpected follow-up case count');
const report={schemaVersion:'1.1',id:'Event033_F5_actual_source_control_replay_2026_10_08_71F0',scope:'test/report only',status:results.some(x=>x.status==='fail')?'failed':'passed_bounded_source_replay',test:{path:'.tools/validation/test_033_evolution_controls.js',sha256:sha(fs.readFileSync(__filename))},sourceInventory:inventory,
 historicalEvidence:{archivePath,originalRuntimeSha256:archive.originalRuntimeSha256,originalSummary:archive.originalSummary,originalFiles:archive.files.map(({path,sha256,bytes})=>({path,sha256,bytes})),sourceSnapshots:archive.sourceSnapshots,verification:'Every original compressed byte payload and read-only AA source snapshot verified. Historical 8B85 results are not relabelled as 71F0.'},
 receiptTransition:{priorReceiptDisposition:'historical 8B85 original 130 checks',currentOwnerRuntimeSha256:sha(read(fxPath)),original130CaseIdsRetained:true,addedChecks:13,revisedExpectation:{id:'DIRECT_GLOBAL_stale_state_mirror_boundary_limit',historical8B85:'admitted guard witness',current71F0:'rejected guard witness before body delegation',basis:'Parent-authorized six-line outer-limit follow-up. Original expectation and receipt bytes preserved in historical archive.'}},
 contractCorrection:'Frozen contracts retain old shared context tiers 1/2/3. Current actual wrappers and constants use 2/3/4. C1 pending cell is an already reserved forecast, so current user direction requires honouring it.',
 frameContract:'Each helper effect or trigger clones inherited temp storage. Only caller-preexisting names are copied back. Child-created names are discarded. Normal scoped/global variables and typed scope objects are separate.',
 arithmeticContract:'JS double scalar replay with 1e-10 equality tolerance and nearest-integer rounding followed by actual authored upward adjustment. Explicit native integer roll fixtures use min inclusive/max exclusive. This is not native fixed-point, RNG distribution or overflow proof.',
 fixtureDeclarations:{scalarDefaults,absentDefaults,flags:'Closed universe of literal native flags in loaded source, plus three exact native disable flags. Source-external flag facts must be declared.',arrays:'Explicit one-state frozen registry and ID ledger, one country participant, zero-initialized authored fixed slots, optional one-state reserved cell/storm and explicitly declared second-state guard cases. No numeric scope pointers.',positiveFrozenStateFacts:{typedScope:{type:'state',id:'fixture_state',scopeExists:true},stateFlag:'acid_rain_frozen_valid',normalStateVariables:{acid_rain_registry_generation:7},normalGlobalGeneration:7,validDirectDueClock:100.0108,clockIsNotDefaulted:true,invalidFixtures:'Stale mirror6, explicit marker absence, explicit generation absence, early due clock100.01104 and explicit clock absence.'},dynamicFacts:{acid_rain_all_regions_are_complete:false,countryIsAi:false,fixtureStateController:'country:CXT'},rolls,geographyResult:1,severeReservationIncrement:0,historicalSentinels:historyKeys},
 delegatedBodies:Object.entries(delegated).map(([name,limit])=>({name,limit,calls:spyCounts.get(name)||0})),
 currentSourceBoundaryLimits:['The actual direct-global guard now requires warning-clock presence and due comparison, then executes all_of_scopes over declared frozen states invoking actual acid_rain_state_is_frozen_valid in separate trigger frames. Current-gen due fixtures admit. Stale mirrors, missing markers/generation, early and missing clocks reject before the admitted body witness. This is bounded source replay, not native generation migration or dynamic/foreign reachability proof.','Global transition and forecast geography bodies are admission spies. No invented opening impacts, Chaos receipt, refugee cohort or successful financial/mortality execution.','Host ordinary/global pulse callbacks and quote/payment/achievement/GUI/terminal bodies are explicit spies. Receipt-count/history sentinels show this replay does not touch them, not native preservation proof.','All source guards and full scalar try-severe/multiple/global/refill, formation, stable-front receipt, reserved-cell/storm processing and dissipation-check bodies are read from files. Only declared bodies are delegated.','Actual helpers process typed fixture states. Their mortality/damage callback invocation is observed but impacts are never executed or mocked as success.','No game, population, finance, multiplayer, GUI, native runtime or probability acceptance. AA owns live compare.'],
 summary:{tests:results.length,passed:results.filter(x=>x.status==='pass').length,failed:results.filter(x=>x.status==='fail').length,formationMasks:contracts.formationCases.length,lifecycleContracts:contracts.liveLifecycleCases.length,actualCommandLocations:coverage.size,unchangedSourceHelpers:preservation},
 executedHelpers,helperCoverage:[...helperCoverage].map(([helper,hits])=>({helper,hits})),coverage:[...coverage].map(([location,hits])=>({location,hits})),results};
// Source revision drift during the replay invalidates the receipt.
for(const x of inventory)assert.equal(sha(read(x.path)),x.sha256,`source changed during replay ${x.path}`);
if(process.argv.includes('--json'))console.log(JSON.stringify(report,null,2));else console.log(JSON.stringify({status:report.status,summary:report.summary,test:report.test,failures:results.filter(x=>x.status==='fail')},null,2));
if(report.summary.failed)process.exitCode=1;
