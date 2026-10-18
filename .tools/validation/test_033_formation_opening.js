/* Event033 F6 TEST/REPORT ONLY. No filesystem writes.
 * Default: replay of the current owner source (live bytes). --runtime=SHA --triggers=SHA --constants=SHA --root=SHA
 * optionally bind each file to a reviewed pin.
 * --frozen: hermetic frozen 71F0 research replay, NOT F6 acceptance; it reproduces the historical connected-first violation by design.
 * Source bodies execute with typed scopes, separate temp frames and saved maps.
 */
'use strict';
const fs=require('fs'),path=require('path'),crypto=require('crypto'),zlib=require('zlib'),assert=require('assert/strict');
const root=path.resolve(__dirname,'../..'),dir='docs/plans/033_acid_rain_plans/validation/formation_opening_2026_10_08/';
const baseline=JSON.parse(fs.readFileSync(path.join(root,dir+'baseline_71f0.json'),'utf8'));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const sealedRunnerStartHash=sha(fs.readFileSync(__filename));
const args=Object.fromEntries(process.argv.slice(2).filter(x=>x.includes('=')).map(x=>x.replace(/^--/,'').split('=')));
const current=!process.argv.includes('--frozen'),inventory=[];
const pins={runtime:'common/scripted_effects/033_acid_rain_effects.txt',triggers:'common/scripted_triggers/033_acid_rain_triggers.txt',constants:'common/script_constants/033_acid_rain_constants.txt',root:'events/033_acid_rain.txt'};
for(const k of Object.keys(pins))if(args[k])assert(/^[a-f0-9]{64}$/.test(args[k]),`--${k} must be a SHA-256`);
function parse(text,file){
 const tokens=[];const re=/#[^\r\n]*|"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>#]+/g;let m,line=1,end=0;
 while((m=re.exec(text))){line+=(text.slice(end,m.index).match(/\n/g)||[]).length;end=re.lastIndex;if(m[0][0]!=='#')tokens.push({t:m[0],line,at:m.index,end:re.lastIndex});line+=(m[0].match(/\n/g)||[]).length;}
 let i=0;function body(nested=false){const out=[];while(i<tokens.length&&tokens[i].t!=='}'){const a=tokens[i++];if(a.t==='{'){out.push({key:'__anonymous',value:body(true),line:a.line,file});continue;}if(!['=','<','>'].includes(tokens[i]?.t)){out.push({key:'__atom',value:a.t,line:a.line,file});continue;}const op=tokens[i++].t,b=tokens[i++];assert(b);out.push({key:a.t,op,value:b.t==='{'?body(true):b.t,line:a.line,file,start:a.at,end:tokens[i-1].end});}if(nested){assert.equal(tokens[i]?.t,'}');i++;}return out;}const out=body();assert.equal(i,tokens.length);return out;
}
const field=(ns,k)=>ns.find(n=>n.key===k)?.value;
function walk(ns,fn){for(const n of ns){fn(n);if(Array.isArray(n.value))walk(n.value,fn);}}
const defs=new Map(),constants=new Map(),texts=new Map();let eventRoot;
for(const f of baseline.files){
 const archived=zlib.gunzipSync(Buffer.from(f.rawBytes,'base64'));assert.equal(sha(archived),f.sha256);assert.equal(archived.length,f.bytes);
 const b=current?fs.readFileSync(path.join(root,f.path)):archived;
 for(const [k,p]of Object.entries(pins))if(current&&args[k]&&p===f.path)assert.equal(sha(b),args[k],`parent source drift ${p}`);
 inventory.push({path:f.path,sha256:sha(b),bytes:b.length,mode:current?'current':'frozen_71F0'});const text=b.toString('utf8'),nodes=parse(text,f.path);texts.set(f.path,text);
 if(f.path.includes('/script_constants/')){function flatten(ns,p=''){for(const n of ns){if(n.key==='schema')continue;const k=p?`${p}.${n.key}`:n.key;if(Array.isArray(n.value))flatten(n.value,k);else if(/^-?\d+(\.\d+)?$/.test(n.value))constants.set('constant:'+k,Number(n.value));}}flatten(nodes);}
 else if(f.path.startsWith('events/'))eventRoot=nodes.find(n=>n.key==='country_event'&&field(n.value,'id')==='chaosx.nr33.1');
 else for(const n of nodes)if(Array.isArray(n.value)){assert(!defs.has(n.key),`duplicate helper ${n.key}`);defs.set(n.key,n);}
}
assert(eventRoot);
// The sibling F5 runner is a maintained test under version control, so it is not hash-sealed here.
const knownFlags=new Set(['acid_rain_launch_authorized','acid_rain_launch_forced','acid_rain_country_warning_active','acid_rain_country_project_arrival_risk','super_event_visible']);
for(const n of [...defs.values(),eventRoot])walk(n.value,x=>{if(/^(has|set|clr)_(global|state|country)_flag$/.test(x.key)){const v=Array.isArray(x.value)?field(x.value,'flag'):x.value;if(v&&!v.includes('['))knownFlags.add(v);}});
for(let s=1;s<=3;s++)knownFlags.add(`events_log_disabled_evolution_33_33_${s}`);
const boundaryNames={
 acid_rain_migrate_legacy_runtime:'No-legacy fixture. Migration/cleanup body delegated, no migration acceptance.',
 acid_rain_adopt_legacy_coverage:'No prior coverage fixture. Legacy adoption delegated.',
 acid_rain_form_country_registry:'National bootstrap boundary supplies explicit prepared country maps and participant scopes. State registry/footprint not delegated.',
 acid_rain_register_country_on_control_transfer:'National-provider accounting boundary, not transfer/payment proof.',
 air_contamination_prepare_source_ledger_arrays:'Explicit zero-pressure native source-ledger fixture, no Air mutation proof.',
 acid_rain_apply_air_request:'Air owner mutation boundary, no assumed applied amount.',
 acid_rain_bind_host_and_schedule_worker:'Scheduling boundary only.',
 acid_rain_gui_refresh_read_only:'Presentation only.',acid_rain_gui_open_at_formation:'Presentation only.',play_current_super_event_audio:'Presentation only.',
 acid_rain_033_achievement_register_runtime_state:'Achievement tracking boundary only.',
 acid_rain_033_achievement_record_runtime_warning:'Achievement warning/visit accounting boundary only. Source state visit bindings still execute.',
 acid_rain_033_achievement_record_runtime_arrival:'Achievement arrival accounting boundary only. Source membership/episode/coverage writes still execute.',
 acid_rain_prepare_warning_report:'Report output ABI is outside footprint proof. No invented returned output.',
 acid_rain_send_front_warning_report:'Warning publication invocation observer only.',
 acid_rain_store_arrival_report_facts:'Arrival report projection boundary.',
 acid_rain_reconcile_state_consequences:'Modifier/country accounting boundary, no fabricated physical impact.',
 acid_rain_publish_state_country_counts:'National projection/accounting boundary. Exact state target and coverage ledgers execute separately.',
 acid_rain_assess_window_aftermath:'Prior-impact assessment boundary. Fresh states explicitly have no prior impact.',
 record_events_log_evolution_entry:'Logger sink only, no history-array or GUI acceptance.',
 add_chaos_meter_value:'Observe authored input only. Do not mutate shared meter/history.',
 acid_rain_apply_state_pulse:'Mortality boundary is forbidden at birth. Later cadence test records dispatch only, no successful loss/receipt.',
 acid_rain_apply_state_damage:'Damage boundary is forbidden at birth. Later cadence test records dispatch only.',
 acid_rain_033_achievement_close_runtime_episode:'Achievement settlement boundary only.',
 acid_rain_refresh_country_forecast_status:'Presentation/accounting projection boundary.',
 acid_rain_store_departure_report_facts:'Departure report projection boundary.',
 acid_rain_advance_consequence_interval:'Time integration outside footprint proof. No mutation fabricated.',
 acid_rain_close_state_evacuation:'No evacuation fixture. Closure/financial helper delegated.'
};
const coverage=new Map(),helperHits=new Map();
class World{
 constructor({chaos=200,mask='111',sizes=[20,20],topology='chain',percent=12,seedBreak=true,invalid=false}={}){
  this.global=new Map([['global.date',100],['global.chaos_meter_value',chaos],['global.air_contamination_bp',0]]);this.globalArrays=new Map();this.temp=new Map(seedBreak?[['break',1]]:[]);this.scope={type:'country',key:'CXT'};this.rootScope=this.scope;this.previous=[];this.saved=new Map();this.arrays=new Map();this.flags=new Set();this.scopeFlags=new Map();this.absent=new Map();this.native=new Map();this.states=[];this.countries=[this.scope,{type:'country',key:'OTHER'}];this.targets=new Map([['acid_rain_runtime_host',this.scope]]);this.calls=[];this.events=[];this.random=[];this.neighbors=[];this.selectionTrace=[];this.mode='birth';this.opts={chaos,mask,sizes,topology,percent,invalid};
  this.globalAbsent=new Set(['global.acid_rain_generation_id','global.acid_rain_region_index_generation']);
  this.globalArrays.set('global.acid_rain_participant_countries',[]);this.globalArrays.set('global.acid_rain_frozen_states',[]);
  for(let i=0;i<3;i++)if(mask[i]==='0')this.flags.add(`events_log_disabled_evolution_33_33_${i+1}`);
  for(const c of this.countries){this.saved.set(c.key,new Map([['acid_rain_water_tier',0],['acid_rain_preparedness',0],['acid_rain_active_exposed_states',0],['acid_rain_current_warning_state_count',0],['acid_rain_touched_states',0],['acid_rain_active_projects',0]]));this.arrays.set(c.key,new Map());this.scopeFlags.set(c.key,new Set(['acid_rain_launch_authorized']));this.absent.set(c.key,new Set(['acid_rain_last_arrival_report_day','acid_rain_last_departure_report_day','event_cluster_member_event_system_only','event_cluster_id','event_cluster_member_event_id','event_id']));this.native.set(c.key,{exists:true,is_ai:false,tag:c.key,is_actual_nonhuman_country:false,has_capitulated:false});}
  const continents=['europe','middle_east','asia','africa','australia','north_america','south_america'];
  for(let region=1;region<=sizes.length;region++)for(let i=0;i<sizes[region-1];i++){
   const s={type:'state',key:`S${region}_${i}`,region};this.states.push(s);this.saved.set(s.key,new Map());this.arrays.set(s.key,new Map());this.scopeFlags.set(s.key,new Set());
   this.absent.set(s.key,new Set(['acid_rain_touch_responsible_country_id','acid_rain_touch_responsibility_generation','acid_rain_target_generation','acid_rain_target_front_id','acid_rain_ordinary_cap_population_people','acid_rain_ordinary_inactive_day','acid_rain_region_id','acid_rain_last_pulse_day','acid_rain_warning_visit_id']));
   this.native.set(s.key,{scope_exists:true,impassable:invalid,state_population_k:1000+i,continent:continents[region-1],category:'rural',owner:this.countries[0],controller:this.countries[0],neighbors:[]});
  }
  for(const s of this.states){const peers=this.states.filter(t=>t.region===s.region),i=peers.indexOf(s);this.native.get(s.key).neighbors=topology==='islands'?[]:topology==='disconnected'?peers.filter((t,j)=>Math.floor(j/2)===Math.floor(i/2)&&j!==i):peers.filter((t,j)=>Math.abs(j-i)===1);}
  if(['non_topological_chain','interleaved_islands','stalled_then_island'].includes(topology)){
   assert.deepEqual(sizes,[20],'declared graph fixture uses 20 states');for(const s of this.states)this.native.get(s.key).neighbors=[];
   const chains=topology==='non_topological_chain'?[[0,19,...Array.from({length:17},(_,i)=>i+2)],[1]]:topology==='stalled_then_island'?[[0,19],[1,18,17],[2,16,15],...[3,4,5,6,7,8,9,10,11,12,13,14].map(x=>[x])]:[[0,19,18,17],[1,16,15,14],[2,13,12,11],[3,10,9,8],[4,5,6,7]];
   for(const chain of chains)for(let i=1;i<chain.length;i++){const a=this.states[chain[i-1]],b=this.states[chain[i]];this.native.get(a.key).neighbors.push(b);this.native.get(b.key).neighbors.push(a);}
  }
  if(seedBreak)for(const n of defs.values())walk(n.value,x=>{if(x.key==='break'&&typeof x.value==='string')this.temp.set(x.value,1);});
 }
 typed(s){assert(s&&['state','country'].includes(s.type)&&this.saved.has(s.key),`undeclared typed scope ${JSON.stringify(s)}`);return s;}
 enter(s,fn){this.typed(s);const prior=this.scope;this.previous.push(prior);this.scope=s;try{return fn();}finally{this.scope=prior;this.previous.pop();}}
 scoped(prefix){if(prefix==='THIS')return this.scope;if(prefix==='ROOT')return this.rootScope;if(prefix==='PREV'){assert(this.previous.length);return this.previous.at(-1);}if(['CONTROLLER','OWNER'].includes(prefix)){assert.equal(this.scope.type,'state');return this.typed(this.native.get(this.scope.key)[prefix.toLowerCase()]);}throw Error(`unknown scope ${prefix}`);}
 child(fn){const parent=this.temp;this.temp=new Map(parent);try{return fn();}finally{for(const k of parent.keys()){if(this.temp.has(k))parent.set(k,this.temp.get(k));else parent.delete(k);}this.temp=parent;}}
 location(k){if(k.startsWith('global.'))return{map:this.global,absent:this.globalAbsent,arrays:this.globalArrays,key:k};const dot=k.indexOf('.');if(dot>=0){const scope=this.scoped(k.slice(0,dot));return{map:this.saved.get(scope.key),absent:this.absent.get(scope.key),arrays:this.arrays.get(scope.key),key:k.slice(dot+1)};}return{map:this.saved.get(this.scope.key),absent:this.absent.get(this.scope.key),arrays:this.arrays.get(this.scope.key),key:k};}
 array(k,create=false){if(this.temp.has(k)&&Array.isArray(this.temp.get(k)))return this.temp.get(k);const x=this.location(k);if(create&&!x.arrays.has(x.key))x.arrays.set(x.key,[]);assert(x.arrays.has(x.key),`undeclared array ${k}`);return x.arrays.get(x.key);}
 indexed(k){const a=k.indexOf('^');if(a<0)return null;const index=k.slice(a+1);return{array:this.array(k.slice(0,a)),index:index==='num'?'num':this.num(index)};}
 val(k){assert.equal(typeof k,'string');if(/^-?\d+(\.\d+)?$/.test(k))return Number(k);if(k.startsWith('constant:')){assert(constants.has(k),`unknown constant ${k}`);return constants.get(k);}if(['THIS','ROOT','PREV','CONTROLLER','OWNER'].includes(k))return this.scoped(k);if(k.endsWith('.id'))return{opaqueNativeIdentity:this.scoped(k.slice(0,-3)).key};const a=this.indexed(k);if(a){if(a.index==='num')return a.array.length;assert(Number.isInteger(a.index)&&a.index>=0&&a.index<a.array.length,`unallocated indexed fact ${k}`);return a.array[a.index];}if(!k.startsWith('global.')&&this.temp.has(k))return this.temp.get(k);const l=this.location(k);if(l.map.has(l.key))return l.map.get(l.key);if(l.absent.has(l.key))return 0;const native=this.native.get(this.scope.key);if(k in native)return native[k];throw Error(`unknown fact ${k} in ${this.scope.key}`);}
 num(k){const v=this.val(k);assert.equal(typeof v,'number',`pointer arithmetic forbidden ${k}`);assert(Number.isFinite(v));return v;}
 has(k){if(!k.startsWith('global.')&&this.temp.has(k))return true;const l=this.location(k);if(l.map.has(l.key))return true;assert(l.absent.has(l.key),`unknown variable absence ${k} in ${this.scope.key}`);return false;}
 put(k,v,temp=false){const a=this.indexed(k);if(a){assert(!temp&&a.index!=='num');assert(a.index<a.array.length);a.array[a.index]=v;return;}if(temp){assert(!k.startsWith('global.'));this.temp.set(k,v);return;}const l=this.location(k);l.map.set(l.key,v);l.absent.delete(l.key);}
 flag(k,local=false){assert(knownFlags.has(k),`unknown flag ${k}`);return(local?this.scopeFlags.get(this.scope.key):this.flags).has(k);}
 compare(a,b,op){if(typeof a!=='number'||typeof b!=='number'){assert(['=','equals','not_equals'].includes(op),'typed identity ordering/arithmetic forbidden');const same=JSON.stringify(a)===JSON.stringify(b);return op==='not_equals'?!same:same;}const e=1e-9;switch(op){case '=':case'equals':return Math.abs(a-b)<e;case'<':case'less_than':return a<b-e;case'>':case'greater_than':return a>b+e;case'not_equals':return Math.abs(a-b)>=e;case'greater_than_or_equals':return a>=b-e;case'less_than_or_equals':return a<=b+e;default:throw Error(`unknown compare ${op}`);}}
 check(ns){const name=field(ns,'var');if(name)return this.compare(this.val(name),this.val(field(ns,'value')),field(ns,'compare')||'=');assert.equal(ns.length,1);return this.compare(this.val(ns[0].key),this.val(ns[0].value),ns[0].op);}
 hit(n){const k=`${n.file}:${n.line}:${n.key}`;coverage.set(k,(coverage.get(k)||0)+1);}
 trig(ns,mode='AND'){if(mode==='NOT')return!ns.some(n=>this.pred(n));if(mode==='OR')return ns.some(n=>this.pred(n));return ns.every(n=>this.pred(n));}
 pred(n){this.hit(n);const k=n.key,v=n.value;if(['AND','OR','NOT'].includes(k))return this.trig(v,k);if(k==='hidden_trigger')return this.trig(v);if(k==='check_variable')return this.check(v);if(k==='has_variable')return this.has(v);if(k==='has_event_target')return this.targets.has(v);if(k==='has_global_flag')return this.flag(Array.isArray(v)?field(v,'flag'):v);if(k==='has_state_flag'||k==='has_country_flag')return this.flag(v,true);if(k==='set_temp_variable'){this.effect(n);return true;}
  if(k==='is_in_array'){const value=this.val(field(v,'value'));return this.array(field(v,'array')).some(x=>JSON.stringify(x)===JSON.stringify(value));}
  if(k==='is_on_continent')return this.native.get(this.scope.key).continent===v;if(k==='has_state_category')return this.native.get(this.scope.key).category===v;
  if(['scope_exists','exists','impassable','is_ai','is_actual_nonhuman_country','has_capitulated'].includes(k)){assert(k in this.native.get(this.scope.key),`unknown native fact ${k}`);return this.native.get(this.scope.key)[k]===(v==='yes');}
  if(k==='tag')return this.native.get(this.scope.key).tag===v;
  if(k==='any_state')return this.states.some(s=>this.enter(s,()=>this.trig(v)));
  if(k==='any_owned_state')return this.states.filter(s=>this.native.get(s.key).owner.key===this.scope.key).some(s=>this.enter(s,()=>this.trig(v)));
  if(k==='any_neighbor_state'){const s=this.scope,neighbors=this.native.get(s.key).neighbors;assert(Array.isArray(neighbors),'unknown geography');const answer=neighbors.some(t=>this.enter(t,()=>this.trig(v)));this.neighbors.push({scope:s.key,neighbors:neighbors.map(x=>x.key),answer});return answer;}
  if(k==='all_of_scopes')return this.array(field(v,'array')).every(s=>this.enter(s,()=>this.trig(v.filter(x=>x.key!=='array'))));
  if(['ROOT','PREV','CONTROLLER','OWNER'].includes(k))return this.enter(this.scoped(k),()=>this.trig(v));
  if(k==='meta_trigger'){const replacements={};for(const x of v.filter(x=>x.key!=='text')){const m=/^"\[\?([^|]+)\|(?:0|\.0)\]"$/.exec(x.value);assert(m,`unsupported meta replacement ${x.value}`);replacements[x.key]=String(Math.round(this.num(m[1])));}const sub=x=>typeof x==='string'?x.replace(/\[([A-Z_]+)\]/g,(_,key)=>{assert(key in replacements);return replacements[key];}):x.map(n=>({...n,key:sub(n.key),value:sub(n.value)}));return this.trig(sub(field(v,'text')));}
  if(defs.has(k))return this.child(()=>this.trig(defs.get(k).value))===(v==='yes');throw Error(`unknown trigger ${k}`);
 }
 invoke(k){this.calls.push(k);helperHits.set(k,(helperHits.get(k)||0)+1);if(k==='acid_rain_process_front')assert(this.trig(defs.get('acid_rain_runtime_is_active').value),'process_front creation requires actual active-runtime predicate');
  if(k in boundaryNames){if(['acid_rain_apply_state_pulse','acid_rain_apply_state_damage'].includes(k))assert.notEqual(this.mode,'birth',`forbidden formation impact ${k}`);
   if(k==='acid_rain_form_country_registry'){this.globalArrays.set('global.acid_rain_participant_countries',[...this.countries]);this.global.set('global.acid_rain_country_record_count',this.countries.length);}
   if(k==='air_contamination_prepare_source_ledger_arrays'){const size=constants.get('constant:acid_rain_air.source_id')+1;this.globalArrays.set('global.air_contamination_source_lifetime_added_bp_entries',Array(size).fill(0));this.globalArrays.set('global.air_contamination_source_current_bp_entries',Array(size).fill(0));}
   this.events.push({boundary:k,scope:this.scope.key,mode:this.mode,...(k==='add_chaos_meter_value'?{amount:this.num('chaos_change')}:{} )});return;
  }
  assert(defs.has(k),`unknown effect helper ${k}`);return this.child(()=>{this.exec(defs.get(k).value);if(k==='acid_rain_start_runtime')this.events.push({privateHelperObservation:k,frontRegionResult:this.temp.has('acid_rain_front_region_result')?this.temp.get('acid_rain_front_region_result'):'not-created',publicReturnClaim:false});});
 }
 exec(ns){for(let i=0;i<ns.length;i++){const n=ns[i];if(n.key==='if'){let taken=false;do{const b=ns[i];this.hit(b);if(!taken&&(b.key==='else'||this.trig(field(b.value,'limit')))){taken=true;this.exec(b.value.filter(x=>x.key!=='limit'));}if(!['else_if','else'].includes(ns[i+1]?.key))break;i++;}while(true);}else this.effect(n);}}
 effect(n){this.hit(n);const k=n.key,v=n.value;
  if(/^(set|add_to|subtract_from|multiply|divide)_(temp_)?variable$/.test(k)){const a=field(v,'var')?{key:field(v,'var'),value:field(v,'value')}:v[0];let x=this.val(a.value);if(!k.startsWith('set_')){const old=this.num(a.key);assert.equal(typeof x,'number');if(k.startsWith('add_'))x=old+x;if(k.startsWith('subtract_'))x=old-x;if(k.startsWith('multiply_'))x=old*x;if(k.startsWith('divide_')){assert.notEqual(x,0);x=old/x;}}this.put(a.key,x,k.includes('_temp_'));return;}
  if(/^clamp_(temp_)?variable$/.test(k)){const name=field(v,'var');let x=this.num(name);if(field(v,'min'))x=Math.max(x,this.num(field(v,'min')));if(field(v,'max'))x=Math.min(x,this.num(field(v,'max')));this.put(name,x,k.includes('_temp_'));return;}
  if(/^round_(temp_)?variable$/.test(k)){this.put(v,Math.round(this.num(v)),k.includes('_temp_'));return;}
  if(k==='clear_variable'){const l=this.location(v);l.map.delete(l.key);l.absent.add(l.key);return;}
  if(k==='clear_array'||k==='clear_temp_array'){if(k==='clear_temp_array')this.temp.set(v,[]);else{const l=this.location(v);l.arrays.set(l.key,[]);}return;}
  if(k==='resize_array'){const a=this.array(field(v,'array'),true),size=this.num(field(v,'size'));assert(Number.isInteger(size)&&size>=0);const value=field(v,'value')?this.val(field(v,'value')):0;while(a.length<size)a.push(value);a.length=size;return;}
  if(k==='add_to_array'||k==='add_to_temp_array'||k==='remove_from_array'){const name=field(v,'array'),value=this.val(field(v,'value'));if(k==='add_to_temp_array'&&!this.temp.has(name))this.temp.set(name,[]);const a=this.array(name,k==='add_to_array');if(k==='remove_from_array'){const at=a.findIndex(x=>JSON.stringify(x)===JSON.stringify(value));if(at>=0)a.splice(at,1);}else a.push(value);return;}
  if(/^(set|clr)_(global|country|state)_flag$/.test(k)){const flag=Array.isArray(v)?field(v,'flag'):v;assert(knownFlags.has(flag),`unknown flag ${flag}`);const s=k.includes('_global_')?this.flags:this.scopeFlags.get(this.scope.key);k.startsWith('set_')?s.add(flag):s.delete(flag);if(Array.isArray(v)&&field(v,'days'))this.events.push({timedFlag:flag,days:this.num(field(v,'days')),scope:this.scope.key});return;}
  if(k==='save_event_target_as'){this.targets.set(v,this.scope);return;}
  if(k==='meta_effect'){const replacements={};for(const x of v.filter(x=>x.key!=='text')){const m=/^"\[\?([^|]+)\|(?:0|\.0)\]"$/.exec(x.value);assert(m,`unsupported meta-effect replacement ${x.value}`);replacements[x.key]=String(Math.round(this.num(m[1])));}const sub=x=>typeof x==='string'?x.replace(/\[([A-Z_]+)\]/g,(_,key)=>{assert(key in replacements);return replacements[key];}):x.map(n=>({...n,key:sub(n.key),value:sub(n.value)}));this.exec(sub(field(v,'text')));return;}
  if(k==='for_loop_effect'||k==='while_loop_effect'||k==='for_each_scope_loop'||k==='for_each_loop'){const b=v.filter(x=>!['start','end','add','value','index','array','break','limit'].includes(x.key)),stop=field(v,'break')||'break';let observation;
   if(k==='for_loop_effect'&&['acid_rain_touch_cursor','acid_rain_touch_island_cursor'].includes(field(v,'value'))){
    const front=this.num('acid_rain_front_id'),region=this.num('acid_rain_selected_region_id'),selected=this.array('global.acid_rain_ordinary_target_states').filter(s=>this.saved.get(s.key).get('acid_rain_target_front_id')===front);
    const reachable=this.states.filter(s=>s.region===region&&!this.scopeFlags.get(s.key).has('acid_rain_touched')&&this.native.get(s.key).neighbors.some(t=>selected.some(x=>x.key===t.key)));
    const fallback=field(v,'value')==='acid_rain_touch_island_cursor';observation={source:`${n.file}:${n.line}`,phase:fallback?'island_fallback':'neighbor_pass',front,region,selectedBefore:selected.map(s=>s.key),visitedBefore:this.num(`global.acid_rain_front_visited_entries^${front}`),connectedUntouchedBefore:reachable.map(s=>s.key),targetLimit:this.num('acid_rain_front_touch_limit'),...(fallback?{beforeFallback:selected.map(s=>s.key),connectedUntouchedBeforeFallback:reachable.map(s=>s.key)}:{})};this.selectionTrace.push(observation);
   }
   if(k==='for_loop_effect'){const start=this.num(field(v,'start')),end=this.num(field(v,'end')),add=field(v,'add')?this.num(field(v,'add')):1;assert(add>0);for(let x=start,count=0;x<end&&count<1000;x+=add,count++){if(this.num(stop)!==0)break;this.put(field(v,'value'),x,true);this.exec(b);}if(observation){observation.visitedAfter=this.num(`global.acid_rain_front_visited_entries^${observation.front}`);observation.selectedAfter=this.array('global.acid_rain_ordinary_target_states').filter(s=>this.saved.get(s.key).get('acid_rain_target_front_id')===observation.front).map(s=>s.key);observation.progress=observation.visitedAfter-observation.visitedBefore;}return;}
   if(k==='while_loop_effect'){let count=0;for(;count<1000&&this.num(stop)===0&&this.trig(field(v,'limit'));count++)this.exec(b);if(stop==='acid_rain_process_front_connected_break')this.events.push({numericLoop:stop,iterations:count,sourceLimit:40,nativeModeledLimit:1000,source:`${n.file}:${n.line}`});return;}
   const a=[...this.array(field(v,'array'))];for(let i=0;i<a.length;i++){if(this.num(stop)!==0)break;if(k==='for_each_scope_loop')this.enter(a[i],()=>this.exec(b));else{if(field(v,'value'))this.put(field(v,'value'),a[i],true);if(field(v,'index'))this.put(field(v,'index'),i,true);this.exec(b);}}return;
  }
  if(k==='every_state'||k==='every_country'){for(const s of k==='every_state'?this.states:this.countries)this.enter(s,()=>{const limit=field(v,'limit');if(!limit||this.trig(limit))this.exec(v.filter(x=>x.key!=='limit'));});return;}
  if(k.startsWith('var:')){this.enter(this.val(k.slice(4)),()=>this.exec(v));return;}
  if(k.startsWith('event_target:')){assert(this.targets.has(k.slice(13)));this.enter(this.targets.get(k.slice(13)),()=>this.exec(v));return;}
  if(['ROOT','PREV','CONTROLLER','OWNER'].includes(k)){this.enter(this.scoped(k),()=>this.exec(v));return;}
  if(k==='random_list'){const options=v.filter(x=>this.num(x.key)>0);assert(options.length,'empty random list');const chosen=this.opts.regionChoice?options.find(x=>x.key===`acid_rain_region_weight_${this.opts.regionChoice}`):options[0];assert(chosen,'explicit region choice is ineligible');this.random.push({native:'random_list',choice:chosen.key,policy:'explicit eligible-weight choice fixture, no probability inference'});this.exec(chosen.value);return;}
  if(/^set_(temp_)?variable_to_random$/.test(k)){const name=field(v,'var'),min=this.num(field(v,'min')),max=this.num(field(v,'max'));assert.equal(field(v,'integer'),'yes');const chosen={acid_rain_footprint_percent:this.opts.percent,acid_rain_first_visit_percent:60,acid_rain_front_minimum_dwell_days:18,acid_rain_front_maximum_dwell_days:36,acid_rain_front_retire_percent:20,acid_rain_third_front_roll:this.opts.thirdRoll||100}[name];assert(chosen!==undefined,`undeclared random fixture ${name}`);assert(chosen>=min&&chosen<max);this.random.push({native:k,name,min,max,chosen});this.put(name,chosen,k.includes('_temp_'));return;}
  if(k==='country_event'||k==='news_event'){assert.equal(this.scope.type,'country');this.events.push({dispatch:k,id:field(v,'id'),scope:this.scope.key});return;}
  if(v==='yes'&&(defs.has(k)||k in boundaryNames)){this.invoke(k);return;}throw Error(`unknown effect ${k} at ${n.file}:${n.line}`);
 }
 launch(){this.child(()=>this.exec(field(eventRoot.value,'immediate')));}
 snapshot(){return JSON.stringify({global:[...this.global],globalArrays:[...this.globalArrays],saved:[...this.saved].map(([k,v])=>[k,[...v]]),flags:[...this.flags].sort(),scopeFlags:[...this.scopeFlags].map(([k,v])=>[k,[...v].sort()]),targets:[...this.targets]});}
 summary(){return{runtimeActive:this.flags.has('acid_rain_runtime_active'),phase:this.global.get('global.acid_rain_phase'),frontCount:this.global.get('global.acid_rain_front_count'),activeFronts:this.global.get('global.acid_rain_active_front_count'),targets:(this.globalArrays.get('global.acid_rain_ordinary_target_states')||[]).map(x=>x.key),touchCount:this.global.get('global.acid_rain_total_touched_states'),loss:this.global.get('global.acid_rain_total_deaths'),population:this.states.map(s=>({state:s.key,populationK:this.native.get(s.key).state_population_k,episodeCapPeople:this.saved.get(s.key).get('acid_rain_ordinary_cap_population_people'),arrivalVisit:this.saved.get(s.key).get('acid_rain_state_arrival_visit_id')})),calls:this.calls,events:this.events,random:this.random,neighborFacts:this.neighbors};}
}
const results=[];
function scenario(id,fixture,fn){let w;try{w=new World(fixture);const evidence=fn(w);results.push({id,status:'executed',fixture,evidence});}catch(e){results.push({id,status:e.message.includes('SOURCE_CONNECTED_FIRST_VIOLATION')?'source_contract_failure':'fixture_or_source_failure',fixture,error:e.stack,...(w?{failureEvidence:{selectionTrace:w.selectionTrace,selected:w.summary().targets,neighborGraph:w.states.map(s=>({state:s.key,neighbors:w.native.get(s.key).neighbors.map(t=>t.key)}))}}:{})});}}
function opening(w){w.launch();const summary=w.summary();assert(!w.calls.includes('acid_rain_apply_state_pulse'));assert(!w.calls.includes('acid_rain_apply_state_damage'));assert.equal(summary.loss,0);for(const name of ['pulse_receipt_count','pulse_positive_receipt_count','positive_receipt_registry_count','damage_receipt_count'])assert.equal(w.num('global.acid_rain_'+name),0);
 const globalOpening=w.opts.chaos>=800&&w.opts.mask[2]==='1',second=w.opts.chaos>=600&&w.opts.mask[1]==='1'&&!globalOpening;
 const expectedFronts=globalOpening?0:second?2:1;
 const observedContract={globalOpening,expectedFronts,ordinaryRegionDraws:w.random.filter(x=>x.native==='random_list').length,immediateFootprint:summary.targets.length>0,activeFronts:summary.activeFronts};
 if(current){assert(summary.runtimeActive);assert.equal(summary.activeFronts,expectedFronts);assert.equal(summary.frontCount,expectedFronts);
  if(globalOpening){assert.equal(summary.targets.length,0);assert.equal(observedContract.ordinaryRegionDraws,0);assert(!w.calls.includes('acid_rain_assign_next_front_region'));assert(!w.calls.includes('acid_rain_open_additional_front'));assert.equal(summary.phase,3);assert(Math.abs(w.num('global.acid_rain_global_warning_day')-100-3*0.00024)<1e-9);}
  else {assert(summary.targets.length>0);assert(!w.events.some(x=>x.timedFlag==='acid_rain_country_warning_active'||x.timedFlag==='acid_rain_country_project_arrival_risk'));assert(!w.calls.includes('acid_rain_send_front_warning_report'));for(const key of summary.targets){const fields=w.saved.get(key);assert(fields.get('acid_rain_state_arrival_visit_id')>0);assert(!w.scopeFlags.get(key).has('acid_rain_warning_pending'));}}
  if(second)assert.notEqual(w.num('global.acid_rain_front_region_entries^1'),w.num('global.acid_rain_front_region_entries^2'));
 }
 const snapshot=w.snapshot(),events=w.events.length;w.launch();assert.equal(w.snapshot(),snapshot);assert.equal(w.events.length,events+1,'duplicate may only invoke read-only GUI refresh');return {...summary,desiredF6Contract:observedContract,contractChecked:current};}
scenario('BASE200',{chaos:200},opening);
for(const chaos of [400,600,800])for(let mask=0;mask<8;mask++){const bits=mask.toString(2).padStart(3,'0');scenario(`F${chaos}_M${bits}`,{chaos,mask:bits},opening);}
for(const n of [1,2,20,100,500])for(const percent of [12,20])for(const topology of ['chain','islands','disconnected'])scenario(`FOOTPRINT_n${n}_p${percent}_${topology}`,{sizes:[n],percent,topology},w=>{
 w.launch();const birth=w.summary();const entry=w.num('global.acid_rain_front_next_warning_day_entries^1');
 // Research can reach the baseline's delayed entry without rewriting its guard.
 w.global.set('global.date',entry);w.temp.set('acid_rain_front_id',1);w.temp.set('acid_rain_selected_region_id',w.num('global.acid_rain_front_region_entries^1'));w.invoke('acid_rain_process_front');const built=w.summary();
 const expected=Math.min(n,40,Math.max(2,Math.ceil(n*percent/100)));assert.equal(built.targets.length,expected);assert.equal(built.touchCount,expected);assert.equal(built.loss,0);
 for(const key of built.targets){const state=w.states.find(s=>s.key===key),saved=w.saved.get(key);assert.equal(saved.get('acid_rain_ordinary_cap_population_people'),w.native.get(key).state_population_k*1000);assert(saved.get('acid_rain_state_arrival_visit_id')>0);assert.equal(saved.get('acid_rain_ordinary_episode_loss'),0);}
 w.mode='scheduled_callback_witness';w.global.set('global.date',entry+2*0.00024);w.invoke('acid_rain_pulse_front_states');assert(!w.calls.includes('acid_rain_apply_state_pulse'));w.global.set('global.date',entry+3*0.00024);w.invoke('acid_rain_pulse_front_states');assert.equal(w.calls.filter(x=>x==='acid_rain_apply_state_pulse').length,expected);
 return{birth,built,expected,entryClock:entry,actualActivationAndMembership:true,cadenceBoundaryOnly:true};
});
scenario('ROOT_REJECT_empty_states',{sizes:[]},w=>{w.launch();assert(!w.calls.includes('acid_rain_start_runtime'));return w.summary();});
scenario('ROOT_REJECT_invalid_states',{invalid:true},w=>{w.launch();assert(!w.calls.includes('acid_rain_start_runtime'));return w.summary();});
scenario('ROOT_REJECT_terminal',{sizes:[2]},w=>{w.flags.add('world_end');w.launch();assert(!w.calls.includes('acid_rain_start_runtime'));return w.summary();});
scenario('REGION_POOL_empty',{sizes:[]},w=>{
 for(const k of ['acid_rain_initialize_runtime_scalars','acid_rain_initialize_front_arrays','acid_rain_form_frozen_registry'])w.invoke(k);
 w.temp.set('acid_rain_front_id',1);w.temp.set('acid_rain_front_region_result',0);w.invoke('acid_rain_assign_next_front_region');assert.equal(w.num('acid_rain_front_region_result'),0);assert(!w.calls.includes('acid_rain_commit_front_region'));return w.summary();
});
scenario('REGION_POOL_reserved',{sizes:[4]},w=>{
 w.launch();w.temp.set('acid_rain_front_id',3);w.temp.set('acid_rain_front_region_result',0);w.put('global.acid_rain_front_region_entries^1',1);w.put('global.acid_rain_front_next_region_entries^2',1);
 const prior=w.calls.filter(x=>x==='acid_rain_commit_front_region').length;w.invoke('acid_rain_assign_next_front_region');assert.equal(w.num('acid_rain_front_region_result'),0);assert.equal(w.calls.filter(x=>x==='acid_rain_commit_front_region').length,prior);return w.summary();
});
scenario('WARNING_existing_cross_region_7days',{sizes:[4,4]},w=>{
 w.launch();w.temp.set('acid_rain_front_id',1);w.opts.regionChoice=2;w.temp.set('acid_rain_front_region_result',0);w.invoke('acid_rain_assign_next_front_region');assert.equal(w.num('global.acid_rain_front_region_entries^1'),2);assert(Math.abs(w.num('global.acid_rain_front_next_warning_day_entries^1')-w.num('global.date')-7*0.00024)<1e-9);assert(w.events.some(x=>x.timedFlag==='acid_rain_country_warning_active'&&x.days===7));return w.summary();
});
scenario('TWO_VISIT_remaining_quota',{sizes:[20]},w=>{
 w.launch();w.temp.set('acid_rain_front_id',1);w.temp.set('acid_rain_selected_region_id',1);w.put('global.acid_rain_front_visit_entries^1',2);w.put('global.acid_rain_region_touched_entries^1',12);
 const draws=w.random.length;w.invoke('acid_rain_calculate_front_goal');assert.equal(w.num('global.acid_rain_front_target_goal_entries^1'),8);assert.equal(w.random.length,draws);return {remaining:8,actualQuotaBody:true,syntheticPriorTouchedCount:12,fullTraversalCase:'TWO_VISIT_full_exact_membership'};
});
scenario('TWO_VISIT_full_exact_membership',{sizes:[20],topology:'islands'},w=>{
 w.launch();w.temp.set('acid_rain_front_id',1);w.temp.set('acid_rain_selected_region_id',1);w.global.set('global.date',w.num('global.acid_rain_front_next_warning_day_entries^1'));const visits=[];
 for(let step=0;step<40;step++){
  w.invoke('acid_rain_process_front');visits.push({day:w.num('global.date'),visit:w.num('global.acid_rain_front_visit_entries^1'),touched:w.num('global.acid_rain_total_touched_states'),frontState:w.num('global.acid_rain_front_state_entries^1')});
  if(w.num('global.acid_rain_completed_region_count')===7)break;
  w.global.set('global.date',w.num('global.date')+6*0.00024);
 }
 assert.equal(w.num('global.acid_rain_total_touched_states'),20);assert.equal(w.num('global.acid_rain_region_first_visit_observed_entries^1'),12);assert.equal(w.num('global.acid_rain_region_second_visit_observed_entries^1'),8);
 assert.equal(w.num('global.acid_rain_coverage_receipt_count'),20);assert.equal(new Set(w.array('global.acid_rain_coverage_receipt_states').map(x=>x.key)).size,20);assert.equal(w.num('global.acid_rain_front_movement_count_entries^1'),1);assert(!w.calls.includes('acid_rain_apply_state_pulse'));return {visits,firstVisit:12,secondVisit:8,exactUniqueCoverage:20,actualGeometryAndMembership:true};
});
for(const topology of ['non_topological_chain','interleaved_islands'])scenario(`CONNECTED_FIRST_${topology}`,{sizes:[20],topology,percent:20},w=>{
 assert.equal(w.scopeFlags.get('S1_0').has('acid_rain_front_target'),false,'no fixture-provided active anchor');w.launch();
 if(!current){w.temp.set('acid_rain_front_id',1);w.temp.set('acid_rain_selected_region_id',1);w.global.set('global.date',w.num('global.acid_rain_front_next_warning_day_entries^1'));w.invoke('acid_rain_process_front');}
 const fallback=w.selectionTrace.filter(x=>x.phase==='island_fallback');assert(w.selectionTrace.some(x=>x.phase==='neighbor_pass'),'actual neighbor phase must execute');assert.equal(w.summary().targets.length,4);
 for(const trace of fallback)assert(!(trace.beforeFallback.length<trace.targetLimit&&trace.connectedUntouchedBeforeFallback.length>0),`SOURCE_CONNECTED_FIRST_VIOLATION: ${JSON.stringify(trace)}; final=${JSON.stringify(w.summary().targets)}`);
 assert.deepEqual(w.summary().targets,topology==='non_topological_chain'?['S1_0','S1_19','S1_2','S1_3']:['S1_0','S1_19','S1_18','S1_17']);
 return {selectionTrace:w.selectionTrace,membership:w.summary().targets,noAssumedAnchor:true,sourceRule:'Only use island fallback after connected growth actually stalls.'};
});
if(current)scenario('CONNECTED_FIRST_stall_one_island_then_neighbor_resume',{sizes:[20],topology:'stalled_then_island',percent:20},w=>{
 w.launch();assert.deepEqual(w.summary().targets,['S1_0','S1_19','S1_1','S1_18']);const traces=w.selectionTrace;const at=traces.findIndex(x=>x.phase==='island_fallback');assert(at>0);assert.equal(traces[at-1].phase,'neighbor_pass');assert.equal(traces[at-1].progress,0);assert.deepEqual(traces[at].connectedUntouchedBefore,[]);assert.equal(traces[at].progress,1);assert.equal(traces[at+1].phase,'neighbor_pass');assert(traces[at+1].progress>0);assert.equal(w.events.find(x=>x.numericLoop==='acid_rain_process_front_connected_break').iterations,3);
 return {selectionTrace:traces,membership:w.summary().targets,actualStall:true,oneSeedThenNeighborResume:true};
});
for(const id of [2,3])scenario(`CREATION_front${id}_immediate_and_duplicate_work`,{sizes:[20,20,20]},w=>{
 w.launch();if(id===3)w.invoke('acid_rain_open_additional_front');w.invoke('acid_rain_open_additional_front');
 const region=w.num(`global.acid_rain_front_region_entries^${id}`),count=w.num(`global.acid_rain_front_active_state_count_entries^${id}`);
 if(current){assert.equal(count,3);assert.equal(w.num(`global.acid_rain_front_state_entries^${id}`),2);assert.equal(w.num(`global.acid_rain_front_next_warning_day_entries^${id}`),w.num('global.date'));
  w.temp.set('acid_rain_front_id',id);w.temp.set('acid_rain_selected_region_id',region);const before=w.snapshot(),credits=w.events.filter(x=>x.boundary==='add_chaos_meter_value').length;w.invoke('acid_rain_process_front');assert.equal(w.snapshot(),before);assert.equal(w.events.filter(x=>x.boundary==='add_chaos_meter_value').length,credits);assert.equal(w.num(`global.acid_rain_front_movement_count_entries^${id}`),0);
 }
 return {...w.summary(),directCreationFixture:'Already-authorized helper body only, not evolution eligibility acceptance.',immediacyChecked:current};
});
scenario('LIVE_SPLIT_prior7day_notice_then_immediate_front',{chaos:200,sizes:[20,20,20]},w=>{
 w.launch();w.global.set('global.chaos_meter_value',600);w.invoke('acid_rain_try_multiple_fronts');assert(w.flags.has('acid_rain_front_split_pending'));const due=w.num('global.acid_rain_front_split_day');assert(Math.abs(due-100-7*0.00024)<1e-9);assert.equal(w.num('global.acid_rain_front_count'),1);
 w.global.set('global.date',due);w.invoke('acid_rain_try_multiple_fronts');assert.equal(w.num('global.acid_rain_front_count'),2);if(current){assert.equal(w.num('global.acid_rain_front_active_state_count_entries^2'),3);assert.equal(w.num('global.acid_rain_front_next_warning_day_entries^2'),due);assert(w.flags.has('acid_rain_multiple_fronts_unlocked'));}
 return {...w.summary(),priorNoticeDays:7,noAdditionalEntryDelayChecked:current};
});
if(current)for(const start of [799,800])for(const enabled of [false,true])scenario(`PURE_GLOBAL_start${start}_${enabled}`,{chaos:800,mask:enabled?'001':'000'},w=>{
 w.global.set('global.acid_rain_start_chaos',start);const before=w.snapshot();const result=w.child(()=>w.trig(defs.get('acid_rain_formation_has_global_opening').value));assert.equal(result,start===800&&enabled);assert.equal(w.snapshot(),before);assert(!w.temp.has('events_log_evolution_event_id'));return {result,persistedStateUnchanged:true,actualControlFrames:true};
});
if(current)scenario('GLOBAL_no_ordinary_before3days_actual_control',{chaos:800,mask:'011',sizes:[2]},w=>{
 w.launch();assert(w.flags.has('acid_rain_runtime_active'));assert(w.flags.has('acid_rain_global_transition_active'));assert(!w.calls.includes('acid_rain_assign_next_front_region'));assert(!w.calls.includes('acid_rain_open_additional_front'));
 assert.equal(w.num('global.acid_rain_front_count'),0);assert.equal(w.num('global.acid_rain_front_region_entries^1'),0);assert.equal(w.num('global.acid_rain_total_touched_states'),0);assert.equal(w.events.find(x=>x.privateHelperObservation==='acid_rain_start_runtime').frontRegionResult,0);
 for(const elapsed of [0,1,2]){w.global.set('global.date',100+elapsed*0.00024);const before=w.snapshot();w.invoke('acid_rain_try_global_evolution');assert.equal(w.snapshot(),before);assert(!w.calls.includes('acid_rain_begin_global_transition'));assert(!w.calls.includes('acid_rain_apply_state_pulse'));assert(!w.calls.includes('acid_rain_apply_state_damage'));}
 return {...w.summary(),genuineRegionSlotZero:true,independentGlobalAdmission:true,pre3dayControlExecuted:true,globalTransitionBodyNotExecuted:true};
});
scenario('HARNESS_no_unknown_defaults_or_numeric_pointers',{},w=>{
 assert.throws(()=>w.num('unknown_fact'),/unknown fact/);assert.throws(()=>w.has('unknown_absence'),/unknown variable absence/);assert.throws(()=>w.num('THIS.id'),/pointer arithmetic/);assert.throws(()=>w.effect({key:'unknown_native_effect',value:'yes'}),/unknown effect/);
 w.child(()=>w.put('created_in_child',9,true));assert(!w.temp.has('created_in_child'));w.temp.set('predeclared_output',0);w.child(()=>w.put('predeclared_output',9,true));assert.equal(w.num('predeclared_output'),9);return {strictUnknowns:true,typedIds:true,separateTempFrames:true};
});
if(current)scenario('PRESERVE_weights_quota_size_drift_pulse_physics',{},w=>{
 const file='common/scripted_effects/033_acid_rain_effects.txt',old=zlib.gunzipSync(Buffer.from(baseline.files.find(x=>x.path===file).rawBytes,'base64')).toString('utf8'),oldDefs=new Map(parse(old,file).filter(x=>Array.isArray(x.value)).map(x=>[x.key,x]));
 // hidden_trigger only hides tooltip text (f63ab274b), so its content is compared in place.
 const shape=n=>({key:n.key,op:n.op,value:Array.isArray(n.value)?n.value.flatMap(x=>x.key==='hidden_trigger'&&Array.isArray(x.value)?x.value.map(shape):[shape(x)]):n.value});
 const names=['acid_rain_compute_region_candidate_weight','acid_rain_select_weighted_region','acid_rain_calculate_front_goal','acid_rain_initialize_front_visit_timing','acid_rain_activate_front','acid_rain_touch_state_for_front','acid_rain_pulse_front_states','acid_rain_calculate_mortality_profile','acid_rain_apply_state_damage','acid_rain_begin_global_transition'];
 // Rewritten on purpose after the 71F0 baseline: d78785cd1 and ca6acf248 moved regional traversal into private chunked loops
 // (retire, warning, move) and e2f2c280e kept impact report outputs across the pulse helper return. Their behaviour is
 // exercised by the replay scenarios above rather than by body equality.
 const rewrittenAfterBaseline=['acid_rain_retire_front_footprint_states','acid_rain_prepare_front_warning','acid_rain_execute_front_move','acid_rain_apply_state_pulse'];
 for(const name of rewrittenAfterBaseline)assert(defs.has(name),`${name} stays defined`);
 for(const name of names)assert.deepEqual(defs.get(name).value.map(shape),oldDefs.get(name).value.map(shape),`source body changed ${name}`);
 const c=baseline.files.find(x=>x.path===pins.constants),e=baseline.files.find(x=>x.path===pins.root);{
  // Every pre-existing constant keeps its value except the two tuning categories that 92d525f47 retuned on purpose
  // (urgent action durations and the trimmed map anchors); new constants may be added.
  const flat=(ns,p,m)=>{for(const n of ns){if(n.key==='schema')continue;const k=p?`${p}.${n.key}`:n.key;if(Array.isArray(n.value))flat(n.value,k,m);else m.set(k,n.value);}};
  const oldConstants=new Map(),nowConstants=new Map();flat(parse(zlib.gunzipSync(Buffer.from(c.rawBytes,'base64')).toString('utf8'),c.path),'',oldConstants);flat(parse(texts.get(c.path),c.path),'',nowConstants);
  const retuned=/^(acid_rain_urgent_cost|acid_rain_gui_anchor)\./;
  for(const [k,v] of oldConstants)if(!retuned.test(k))assert.equal(nowConstants.get(k),v,`constant changed ${k}`);
 }
 assert.equal(inventory.find(x=>x.path===e.path).sha256,e.sha256);
 return {unchangedAstBodies:names,constantsUnchangedExceptRetuned:true,rootRawUnchanged:true};
});
if(current)scenario('PRESERVE_E5_growth_only_change_and_78loops',{},w=>{
 const archive=JSON.parse(fs.readFileSync(path.join(root,dir+'failing_checkpoint_inputs.json'),'utf8')),oldFile=archive.d717Files.find(x=>x.path===pins.runtime),bytes=zlib.gunzipSync(Buffer.from(oldFile.rawBytes,'base64'));assert.equal(sha(bytes),oldFile.sha256);
 const oldNodes=parse(bytes.toString('utf8'),pins.runtime),old=oldNodes.find(x=>x.key==='acid_rain_process_front').value,now=defs.get('acid_rain_process_front').value,shape=n=>({key:n.key,op:n.op,value:Array.isArray(n.value)?n.value.flatMap(x=>x.key==='hidden_trigger'&&Array.isArray(x.value)?x.value.map(shape):[shape(x)]):n.value});
 assert.deepEqual(old[0].value.map(shape),now[0].value.map(shape));assert.deepEqual(old[2].value.map(shape),now[2].value.map(shape));
 // d78785cd1 wrapped each regional traversal in a private chunk loop. Reverse that wrapper (same projection as the region batch
 // test) so the unchanged parts of the process body are compared against the pre-chunk baseline.
 const unchunk=ns=>ns.flatMap(n=>{
  if(n.key==='set_temp_variable'&&/_chunk_break$/.test(n.value[0]?.key))return [];
  if(n.key==='for_each_loop'&&field(n.value,'array')==='global.acid_rain_region_iteration_chunks'){
   const body=field(n.value,'if'),limit=field(body,'limit'),endVar=field(limit.find(x=>x.key==='check_variable'&&field(x.value,'compare')==='less_than').value,'value');
   const inner=structuredClone(body.find(x=>x.key==='for_loop_effect'));inner.value.find(x=>x.key==='start').value='acid_rain_cursor_start';inner.value.find(x=>x.key==='end').value=endVar;
   return [{key:'set_temp_variable',op:'=',value:[{key:field(inner.value,'break'),op:'=',value:'constant:acid_rain_runtime.zero'}]},{...inner,value:unchunk(inner.value)}];
  }
  return [Array.isArray(n.value)?{...n,value:unchunk(n.value)}:n];
 });
 const a=old[1].value,b=unchunk(now[1].value),oldStart=a.findIndex(n=>n.key==='set_temp_variable'&&field(n.value,'acid_rain_cursor_region')==='acid_rain_selected_region_id'),oldEnd=a.findIndex(n=>n.key==='for_loop_effect'&&field(n.value,'value')==='acid_rain_touch_island_cursor'),newStart=b.findIndex(n=>n.key==='set_temp_variable'&&field(n.value,'acid_rain_connected_passes')==='constant:acid_rain_runtime.zero'),newEnd=b.findIndex(n=>n.key==='while_loop_effect'&&field(n.value,'break')==='acid_rain_process_front_connected_break');
 assert(oldStart>=0&&oldEnd>=oldStart&&newStart>=0&&newEnd>=newStart);assert.deepEqual(a.slice(0,oldStart).map(shape),b.slice(0,newStart).map(shape));assert.deepEqual(a.slice(oldEnd+1).map(shape),b.slice(newEnd+1).map(shape));
 assert.equal(b[newEnd-1].key,'set_temp_variable');assert.equal(field(b[newEnd-1].value,'acid_rain_process_front_connected_break'),'constant:acid_rain_runtime.zero');
 const limit=field(b[newEnd].value,'limit');assert(limit.some(n=>n.key==='check_variable'&&field(n.value,'var')==='acid_rain_connected_passes'&&field(n.value,'value')==='constant:acid_rain_coverage.first_footprint_max_states'&&field(n.value,'compare')==='less_than'));
 let oldLoops=0,newLoops=0;walk(oldNodes,n=>{if(['for_loop_effect','while_loop_effect','for_each_loop','for_each_scope_loop'].includes(n.key))oldLoops++;});walk(parse(texts.get(pins.runtime),pins.runtime),n=>{if(['for_loop_effect','while_loop_effect','for_each_loop','for_each_scope_loop'].includes(n.key))newLoops++;});let chunkWrappers=0;walk(parse(texts.get(pins.runtime),pins.runtime),n=>{if(n.key==='for_each_loop'&&field(n.value,'array')==='global.acid_rain_region_iteration_chunks')chunkWrappers++;});
 // One new bounded while loop for connected growth, plus the chunk wrapper that d78785cd1 put around every regional traversal.
 assert.equal(oldLoops,77);assert.equal(chunkWrappers,16);assert.equal(newLoops,oldLoops+1+chunkWrappers);
 return {priorRuntimeSha256:oldFile.sha256,newRuntimeSha256:inventory.find(x=>x.path===pins.runtime).sha256,oldLoops,newLoops,nonGrowthProcessBodyUnchanged:true,privateResetImmediatelyBeforeWhile:true,chunkWrappers,actualSourceGrowthPassBound:40};
});
const failed=results.some(x=>x.status!=='executed');
const report={id:current?'Event033_F6_formation_opening_actual_source_replay':'Event033_F6_formation_opening_71F0_historical_replay',status:current?(failed?'source_replay_failed':'hash_bound_source_replay_passed'):'historical_frozen_71F0_research_only',sourceInventory:inventory,sealedF5Test:baseline.sealedF5Test,test:{path:'.tools/validation/test_033_formation_opening.js',sha256:sealedRunnerStartHash,startHashSealed:true,endHashChecked:true,selfFileWrites:false},summary:{cases:results.length,executed:results.filter(x=>x.status==='executed').length,sourceContractFailures:results.filter(x=>x.status==='source_contract_failure').length,fixtureFailures:results.filter(x=>x.status==='fixture_or_source_failure').length,unresolved:results.filter(x=>x.status!=='executed').length,sourceLocations:coverage.size},boundaryDeclarations:boundaryNames,fixtureContract:'Typed state/country scopes, explicit neighbors/continents/population, scoped saved maps, strict arrays, documented resize zero-fill only, separate temporary helper frames. Host is explicit country:CXT regular target. Fresh country projection fields are explicit zero-valued fixture inputs, arrival/departure clocks explicitly absent. No arbitrary unknown facts default to zero. Scope identity getters return opaque identity tokens, never numeric pointers.',limits:['Actual scalar initializers, state registry/index, region selector arithmetic, activation, process_front footprint loops, touch membership and episode population baseline execute. Unrelated native/bootstrap/accounting/impact callbacks are named boundaries.','Random list uses explicitly declared eligible-weight choices, not probability acceptance. AA independently owns baseline/compare.','Birth mortality/damage calls fail. Three-day cadence records callback dispatch without successful population loss or loss receipts.','Global transition impact body is not executed. Current global control is tested only before the actual three-day due date. No native gameplay, population loss, finance, migration, multiplayer or GUI acceptance claim.','Arithmetic uses JS doubles with 1e-9 equality tolerance and nearest-integer rounding followed by actual upward/downward source adjustments, not native fixed-point/overflow acceptance.'],helperCoverage:[...helperHits].map(([helper,hits])=>({helper,hits})),results};
if(current)for(const x of inventory)assert.equal(sha(fs.readFileSync(path.join(root,x.path))),x.sha256,'source changed during current replay');
assert.equal(sha(fs.readFileSync(__filename)),sealedRunnerStartHash,'runner changed during replay');
console.log(JSON.stringify(process.argv.includes('--json')?report:{status:report.status,summary:report.summary,test:report.test,failures:results.filter(x=>x.status!=='executed').map(x=>({id:x.id,error:x.error.split('\n').slice(0,2).join(' ')}))},null,2));
if(report.summary.unresolved)process.exitCode=1;
