// Read-only source/API regression for private conventional incident transactions.
// Execute from mod root. This interprets only the explicit tested Clausewitz subset.
// Provider validity, native timer ordering and factory release are model contracts,
// never engine evidence. Unsupported commands fail instead of silently passing.
import {readFileSync} from "node:fs";
import {createHash} from "node:crypto";
import assert from "node:assert/strict";
const root="common/";
const paths=[
 root+"scripted_effects/016_mengele_conventional_incident_effects.txt",
 root+"scripted_triggers/016_mengele_conventional_incident_triggers.txt",
 root+"decisions/016_mengele_conventional_incident_decisions.txt",
 root+"dynamic_modifiers/016_mengele_conventional_incident_modifiers.txt",
 root+"scripted_localisation/016_mengele_conventional_incident_localisation.txt",
 "localisation/english/016_mengele_conventional_incident_l_english.yml"
];
const read=p=>readFileSync(p,"utf8");
function parse(s){
 const t=s.replace(/#[^\r\n]*/g,"").match(/"(?:\\.|[^"])*"|[{}=<>]|[^\s{}=<>]+/g)||[];
 let i=0;
 function body(nested=false){const a=[];while(i<t.length){
  if(t[i]==="}"){i++;return a;}
  const k=t[i++],op=t[i++];assert(["=","<",">"].includes(op),"parse "+k);
  let v=t[i++];v=v==="{"?body(true):v?.startsWith('"')?v.slice(1,-1):v;
  a.push({k,op,v});
 }assert(!nested,"unclosed");return a;}return body();
}
const defs=s=>Object.fromEntries(parse(s).map(n=>[n.k,n.v]));
const e=defs(read(paths[0])),tr=defs(read(paths[1])),d=defs(read(paths[2]));
const computationPaths=[
 root+"scripted_effects/016_mengele_computation_incident_effects.txt",
 root+"scripted_triggers/016_mengele_computation_incident_triggers.txt",
 root+"decisions/016_mengele_computation_incident_decisions.txt"
];
Object.assign(e,defs(read(computationPaths[0])));
Object.assign(tr,defs(read(computationPaths[1])));
const computationDecisions=defs(read(computationPaths[2]));
d.mengele_clone_army_category.push(...computationDecisions.mengele_clone_army_category);
for(const[k,v]of Object.entries(computationDecisions))if(k.startsWith("@"))d[k]=v;
// Execute the actual unchanged shared debit helpers as parsed source.
const shared=defs(read(root+"scripted_effects/chaosx_dynamic_effects.txt"));
for(const k of ["remove_support_equipment_from_stockpile","remove_fuel_from_stockpile"])e[k]=shared[k];
tr.brilliant_scientist_mengele_computation_incident_stage_is_valid=
 defs(read(root+"scripted_triggers/016_mengele_computation_incident_triggers.txt")).brilliant_scientist_mengele_computation_incident_stage_is_valid;
const c={};for(const path of [
 root+"script_constants/016_brilliant_scientist_constants.txt",
 root+"script_constants/016_brilliant_scientist_project_constants.txt",
 root+"script_constants/016_brilliant_scientist_directorate_constants.txt"
]){
 for(const [cat,rows]of Object.entries(defs(read(path))))if(Array.isArray(rows))
 for(const n of rows)if(!Array.isArray(n.v)&&Number.isFinite(Number(n.v)))c["constant:"+cat+"."+n.k]=Number(n.v);
}
const get=(ns,k)=>ns.find(n=>n.k===k)?.v;
const H="brilliant_scientist_mengele_";
function num(t,s){
 if(t.startsWith("var:"))return num(t.slice(4),s);
 if(t in c)return c[t];if(t in s.t)return s.t[t];if(t==="political_power")return s.pp;
 if(t in s.v)return s.v[t];if(Number.isFinite(Number(t)))return Number(t);
 if(t.startsWith("constant:"))throw Error("missing constant "+t);return 0;
}
const cmp=(a,op,b)=>op==="equals"||op==="="?a===b:op==="greater_than_or_equals"?a>=b:op==="less_than_or_equals"?a<=b:op==="greater_than"||op===">"?a>b:op==="less_than"||op==="<"?a<b:(()=>{throw Error(op)})();
function pred(n,s){
 const{k,op,v}=n;
 if(k===H+"project_stage_provider_is_valid")return s.provider;
 if(k==="OR")return v.some(x=>pred(x,s));
 if(k==="NOT")return !v.every(x=>pred(x,s));
 if(["AND","hidden_trigger","custom_trigger_tooltip"].includes(k))return v.filter(x=>x.k!=="tooltip").every(x=>pred(x,s));
 if(k==="has_country_flag")return s.f.has(v);
 if(k==="has_variable")return v in s.v;
 if(k==="has_dynamic_modifier")return s.mods.has(get(v,"modifier"));
 if(k==="check_variable")return cmp(num(get(v,"var"),s),get(v,"compare"),num(get(v,"value"),s));
 if(k==="has_equipment")return v.every(x=>cmp(s.support,x.op,num(x.v,s)));
 if(k==="has_fuel")return cmp(s.fuel,op,num(v,s));
 if(k==="num_of_civilian_factories_available_for_projects")return cmp(s.civ,op,num(v,s));
 if(tr[k])return tr[k].every(x=>pred(x,s));
 throw Error("unknown predicate "+k);
}
function run(nodes,s){
 let previous=false;
 for(const n of nodes){const{k,v}=n;
  if(k==="if"){previous=get(v,"limit").every(x=>pred(x,s));if(previous)run(v.filter(x=>x.k!=="limit"),s);continue;}
  if(k==="else"){if(!previous)run(v,s);continue;}
  if(k==="hidden_effect"){run(v,s);continue;}
  if(k==="custom_effect_tooltip"){s.tooltips.push(v);continue;}
  if(k==="random_list"){
   assert([0,1].includes(s.forcedBranch),"random_list requires an explicit forced branch, never samples");
   assert.equal(v.length,2,"approved incident pool has exactly two outcomes");
   const weights=v.map(n=>num(n.k,s));
   assert(weights.every(x=>Number.isFinite(x)&&x>=0),"invalid forced-pool weights");
   s.rolls.push({weights,forcedBranch:s.forcedBranch});
   run(v[s.forcedBranch].v,s);continue;
  }
  if(["set_variable","set_temp_variable","add_to_variable","multiply_temp_variable","subtract_from_temp_variable"].includes(k)){
   const a=v[0],dest=k.includes("temp")?s.t:s.v;
   dest[a.k]=k==="add_to_variable"?(dest[a.k]||0)+num(a.v,s):k==="multiply_temp_variable"?(dest[a.k]||0)*num(a.v,s):k==="subtract_from_temp_variable"?(dest[a.k]||0)-num(a.v,s):num(a.v,s);continue;
  }
  if(k==="clear_variable"){delete s.v[v];continue;}
  if(k==="set_country_flag"){s.f.add(v);continue;}
  if(k==="clr_country_flag"){s.f.delete(v);continue;}
  if(k==="add_dynamic_modifier"){s.mods.add(get(v,"modifier"));continue;}
  if(k==="remove_dynamic_modifier"){s.mods.delete(get(v,"modifier"));continue;}
  if(k==="remove_decision"){s.civ+=s.reserved[v]||0;delete s.reserved[v];continue;}
  if(k==="add_political_power"){s.pp+=num(v,s);continue;}
  if(k==="add_fuel"){s.fuel+=num(v,s);continue;}
  if(k==="add_equipment_to_stockpile"){assert.equal(get(v,"type"),"support_equipment");s.support+=num(get(v,"amount"),s);continue;}
  if(e[k]){run(e[k],s);continue;}throw Error("unknown effect "+k);
 }
}
const call=(k,s)=>run(e[k],s);
const families=[["electronics","technical"],["materials","industrial"],["rocketry","industrial"],["high_energy","exotic"],["biomedical","biological"]];
const fresh=()=>({pp:1000,support:10000,fuel:20000,civ:30,provider:true,t:{mengele_event016_requested_stage:1},v:{learned_knowledge:77,provider_stage_receipt:88},f:new Set,mods:new Set,reserved:{},tooltips:[],rolls:[]});
const money=s=>[s.pp,s.support,s.fuel,s.civ];
const cost=p=>["political_power","support_equipment","fuel","civilian_factories"].map(k=>c["constant:brilliant_scientist_project_board.response_"+p+"_"+k]);
const dec=f=>d.mengele_clone_army_category.find(n=>n.k==="mengele_event016_"+f+"_incident_recovery").v;
function start(f,s,reserveFirst=false,afterAdmission=()=>{}){const n=dec(f);assert(get(n,"available").every(x=>pred(x,s)));assert(get(n,"custom_cost_trigger").every(x=>pred(x,s)));
 afterAdmission();
 // Model both native orderings. The decision admitted CIC before either.
 const v=Number(d[get(get(n,"modifier"),"civilian_factory_use")]);
 const reserve=()=>{s.civ-=v;s.reserved["mengele_event016_"+f+"_incident_recovery"]=v;};
 if(reserveFirst)reserve();
 run(get(n,"complete_effect"),s);
 if(!reserveFirst)reserve();
}
function end(f,s,kind){const id="mengele_event016_"+f+"_incident_recovery";s.civ+=s.reserved[id]||0;delete s.reserved[id];run(get(dec(f),kind),s);}
let scenarios=0;
for(const [f,p]of families){
 const prefix="mengele_event016_"+f+"_",price=cost(p);
 const s=fresh();call(H+"record_"+f+"_incident",s);call(H+"record_"+f+"_incident",s);assert.equal(s.v[prefix+"incident_history_count"],1);
 const old=money(s);start(f,s);assert.deepEqual(money(s),old.map((v,i)=>v-price[i]));
 assert(s.tooltips.includes(prefix+"incident_recovery_started_tt"));
 call(H+"begin_"+f+"_incident_recovery",s);assert.deepEqual(money(s),old.map((v,i)=>v-price[i]));
 end(f,s,"cancel_effect");call(H+"cancel_"+f+"_incident_recovery",s);assert.deepEqual(money(s),old);
 start(f,s);end(f,s,"remove_effect");call(H+"finish_"+f+"_incident_recovery",s);
 assert.equal(s.v[prefix+"recovery_history_count"],1);assert(!s.f.has(prefix+"incident_active"));
 call(H+"record_"+f+"_incident",s);assert.equal(s.v[prefix+"incident_history_count"],2);
 start(f,s);s.provider=false;call(H+"cleanup_"+f+"_incident",s);const settled=money(s);
 call(H+"cleanup_"+f+"_incident",s);assert.deepEqual(money(s),settled);assert(!s.mods.size);assert(!Object.keys(s.reserved).length);
 assert.equal(s.v.learned_knowledge,77);assert.equal(s.v.provider_stage_receipt,88);assert.equal(s.v[prefix+"recovery_history_count"],1);
 scenarios+=5;
 for(let axis=0;axis<4;axis++){
  const q=fresh();[q.pp,q.support,q.fuel,q.civ]=price;call(H+"record_"+f+"_incident",q);
  assert(pred({k:H+"incident_"+p+"_can_pay",v:"yes"},q)); // Exact equality.
  const key=["pp","support","fuel","civ"][axis];q[key]-=1;
  assert(!pred({k:H+"incident_"+p+"_can_pay",v:"yes"},q));
  assert(!get(dec(f),"available").every(x=>pred(x,q)));
  const before=money(q);
  // Native admission owns CIC, so direct begin calls are invalid for that axis.
  if(axis<3)call(H+"begin_"+f+"_incident_recovery",q);
  assert.deepEqual(money(q),before);scenarios++;
 }
 for(const stage of [0,5,99]){const q=fresh();q.t.mengele_event016_requested_stage=stage;call(H+"record_"+f+"_incident",q);assert(!q.mods.size);scenarios++;}
 const q=fresh();q.provider=false;call(H+"record_"+f+"_incident",q);assert(!q.mods.size);scenarios++;
 // Refund the original receipt after tuning changes, not the current profile.
 const snapshot=fresh();call(H+"record_"+f+"_incident",snapshot);const original=money(snapshot);start(f,snapshot);
 const keys=["political_power","support_equipment","fuel"].map(k=>"constant:brilliant_scientist_project_board.response_"+p+"_"+k);
 const saved=keys.map(k=>c[k]);keys.forEach(k=>c[k]*=2);
 end(f,snapshot,"cancel_effect");assert.deepEqual(money(snapshot),original);
 keys.forEach((k,i)=>c[k]=saved[i]);scenarios++;
 // Invalid ownership at natural expiry refunds instead of recording success.
 const invalid=fresh();call(H+"record_"+f+"_incident",invalid);const baseline=money(invalid);start(f,invalid);
 invalid.provider=false;end(f,invalid,"remove_effect");assert.deepEqual(money(invalid),baseline);
 assert.equal(invalid.v[prefix+"recovery_history_count"],undefined);scenarios++;
 for(const reserveFirst of [false,true]){
  const edge=fresh();[edge.pp,edge.support,edge.fuel,edge.civ]=price;
  call(H+"record_"+f+"_incident",edge);start(f,edge,reserveFirst);
  assert.deepEqual(money(edge),[0,0,0,0]);assert(edge.f.has(prefix+"incident_recovery_active"));
  end(f,edge,"cancel_effect");assert.deepEqual(money(edge),price);scenarios++;
 }
 for(const component of ["political_power","support_equipment","fuel"]){
  const malformed=fresh();call(H+"record_"+f+"_incident",malformed);start(f,malformed);
  delete malformed.v[prefix+"incident_recovery_cost_"+component];
  const paid=money(malformed);malformed.tooltips=[];
  end(f,malformed,"remove_effect");
  assert.deepEqual(money(malformed),[...paid.slice(0,3),paid[3]+price[3]]);
  assert(!malformed.f.has(prefix+"incident_recovery_active"));
  assert(!Object.keys(malformed.v).some(k=>k.startsWith(prefix+"incident_recovery_cost_")));
  assert(malformed.f.has(prefix+"incident_active"));assert.equal(malformed.v[prefix+"recovery_history_count"],undefined);
  assert(!malformed.tooltips.includes(prefix+"incident_recovery_effect_tt"));
  call(H+"cancel_"+f+"_incident_recovery",malformed);assert.deepEqual(money(malformed),[...paid.slice(0,3),paid[3]+price[3]]);scenarios++;
 }
 for(const reserveFirst of [false,true])for(const axis of ["pp","support","fuel"]){
  const race=fresh();[race.pp,race.support,race.fuel,race.civ]=price;
  call(H+"record_"+f+"_incident",race);
  start(f,race,reserveFirst,()=>{race[axis]-=1;});
  const expected=price.slice(0,3);expected[["pp","support","fuel"].indexOf(axis)]-=1;
  assert.deepEqual(money(race).slice(0,3),expected);
  assert(!race.f.has(prefix+"incident_recovery_active"));
  assert(!race.tooltips.includes(prefix+"incident_recovery_started_tt"));
  assert(get(dec(f),"cancel_trigger").every(n=>pred(n,race)));
  const unpaid=money(race);end(f,race,"cancel_effect");
  assert.deepEqual(money(race),[...unpaid.slice(0,3),price[3]]);scenarios++;
 }
}
// Every family can coexist. Resolving one never changes another receipt.
const simultaneous=fresh();for(const[f]of families){call(H+"record_"+f+"_incident",simultaneous);start(f,simultaneous);}
for(const[f]of families){end(f,simultaneous,"remove_effect");assert.equal(simultaneous.v["mengele_event016_"+f+"_recovery_history_count"],1);}
assert.equal(simultaneous.civ,30);assert.equal(simultaneous.mods.size,0);scenarios++;
for(const[f]of families){const s=fresh();s.t.mengele_event016_project_family=c["constant:brilliant_scientist_project_family."+f];const selector=s.t.mengele_event016_project_family;call(H+"record_requested_conventional_incident",s);assert.equal(s.v["mengele_event016_"+f+"_incident_history_count"],1);assert.equal(s.t.mengele_event016_project_family,selector);scenarios++;}
for(const family of [0,1,7,99]){const s=fresh();s.t.mengele_event016_project_family=family;call(H+"record_requested_conventional_incident",s);assert.equal(s.mods.size,0);scenarios++;}
// Parent-requested sixth-family coverage for the same native admission boundary.
for(const reserveFirst of [false,true]){
 const s=fresh(),price=cost("technical");[s.pp,s.support,s.fuel,s.civ]=price;
 call(H+"record_computation_incident",s);start("computation",s,reserveFirst);
 assert.deepEqual(money(s),[0,0,0,0]);assert(s.f.has("mengele_event016_computation_incident_recovery_active"));
 end("computation",s,"cancel_effect");assert.deepEqual(money(s),price);scenarios++;
}
// Separate parent-owned Computation malformed-expiry regression.
for(const component of ["political_power","support_equipment","fuel"]){
 const s=fresh(),prefix="mengele_event016_computation_",price=cost("technical");
 call(H+"record_computation_incident",s);start("computation",s);
 delete s.v[prefix+"incident_recovery_cost_"+component];const paid=money(s);
 end("computation",s,"remove_effect");
 assert(!s.f.has(prefix+"incident_recovery_active"),"Computation malformed expiry must clear active receipt");
 assert(!Object.keys(s.v).some(k=>k.startsWith(prefix+"incident_recovery_cost_")));
 assert.deepEqual(money(s),[...paid.slice(0,3),paid[3]+price[3]]);
 assert.equal(s.v[prefix+"recovery_history_count"],undefined);scenarios++;
}
// Forced outcomes exercise actual dispatcher AST and actual pressure-loader AST.
// There is no PRNG, sampling, normalized probability estimate, or timing model.
let forcedDispatcherScenarios=0;
const stagePressure=[["theory",5],["prototype",10],["deployment",18.75],["weaponization",24]];
const dispatchState=(f,stage,branch=0)=>{
 const s=fresh();s.t.mengele_event016_project_family=c["constant:brilliant_scientist_project_family."+f];
 s.t.mengele_event016_requested_stage=c["constant:brilliant_scientist_project_stage."+stage];s.forcedBranch=branch;
 s.v.mengele_event016_computation_incident_history_count=13;
 s.v.mengele_event016_computation_recovery_history_count=11;
 s.v.mengele_event016_computation_incident_recovery_cost_fuel=123;
 s.v.brilliant_scientist_exposure=57;
 return s;
};
const persistent=s=>({vars:{...s.v},flags:[...s.f].sort(),mods:[...s.mods].sort(),money:money(s)});
const dispatch=H+"dispatch_conventional_incident";
for(const[f]of families)for(const[stage,pressure]of stagePressure)for(const branch of [0,1]){
 const s=dispatchState(f,stage,branch),before=persistent(s),selectors=[s.t.mengele_event016_project_family,s.t.mengele_event016_requested_stage];
 call(dispatch,s);assert.deepEqual(s.rolls,[{weights:[pressure,100-pressure],forcedBranch:branch}]);
 assert.deepEqual([s.t.mengele_event016_project_family,s.t.mengele_event016_requested_stage],selectors);
 if(branch===0){
  const key="mengele_event016_"+f+"_incident_history_count";
  assert.equal(s.v[key],1);delete s.v[key];
  s.f.delete("mengele_event016_"+f+"_incident_active");s.f.delete("mengele_event016_"+f+"_incident_history");
  s.mods.delete(H+f+"_incident");assert.deepEqual(persistent(s),before);
  assert.equal(s.t.mengele_event016_conventional_incident_recorded,1);
 }else{assert.deepEqual(persistent(s),before);assert.equal(s.t.mengele_event016_conventional_incident_recorded,0);}
 forcedDispatcherScenarios++;
}
function blockedDispatch(s){
 const before=persistent(s),selectors=[s.t.mengele_event016_project_family,s.t.mengele_event016_requested_stage];
 call(dispatch,s);assert.equal(s.rolls.length,0);assert.deepEqual(persistent(s),before);
 assert.deepEqual([s.t.mengele_event016_project_family,s.t.mengele_event016_requested_stage],selectors);
 assert.equal(s.t.mengele_event016_conventional_incident_recorded,0);forcedDispatcherScenarios++;
}
for(const[f]of families){
 for(const[stage]of stagePressure){
  const invalid=dispatchState(f,stage);invalid.provider=false;blockedDispatch(invalid);
  for(const suffix of ["incident_active","incident_recovery_active"]){
   const active=dispatchState(f,stage);active.f.add("mengele_event016_"+f+"_"+suffix);blockedDispatch(active);
  }
 }
 for(const invalidStage of [undefined,-1,0,5,99]){
  const s=dispatchState(f,"theory");if(invalidStage===undefined)delete s.t.mengele_event016_requested_stage;
  else s.t.mengele_event016_requested_stage=invalidStage;blockedDispatch(s);
 }
 for(const[other]of families.filter(([other])=>other!==f))for(const branch of [0,1]){
  const s=dispatchState(f,"prototype",branch),prefix="mengele_event016_"+other+"_";
  s.f.add(prefix+"incident_active");s.f.add(prefix+"incident_recovery_active");
  s.v[prefix+"incident_history_count"]=4;s.v[prefix+"incident_recovery_cost_fuel"]=7;
  call(dispatch,s);assert.equal(s.rolls.length,1);assert.equal(s.v[prefix+"incident_history_count"],4);
  assert.equal(s.v[prefix+"incident_recovery_cost_fuel"],7);assert(s.f.has(prefix+"incident_active"));assert(s.f.has(prefix+"incident_recovery_active"));
  assert.equal(s.v["mengele_event016_"+f+"_incident_history_count"],branch===0?1:undefined);
  forcedDispatcherScenarios++;
 }
 // A second immediate call is suppressed by the real first incident's active state.
 const once=dispatchState(f,"deployment");call(dispatch,once);const after=persistent(once);
 call(dispatch,once);assert.equal(once.rolls.length,1);assert.deepEqual(persistent(once),after);forcedDispatcherScenarios++;
}
for(const[stage]of stagePressure)for(const invalidFamily of [undefined,0,1,7,15,99]){
 const s=dispatchState("electronics",stage);if(invalidFamily===undefined)delete s.t.mengele_event016_project_family;
 else s.t.mengele_event016_project_family=invalidFamily;blockedDispatch(s);
}
scenarios+=forcedDispatcherScenarios;
// Structural causal-hook proof only. The actual array-backed paid-stage receipt
// interpreter is not part of this bounded harness, so post-recovery stage replay
// is not represented as an executed receipt regression.
const stagePath=root+"scripted_effects/016_mengele_project_stage_effects.txt";
const stageDefs=defs(read(stagePath)),finish=stageDefs[H+"finish_project_stage"];
const receiptBranch=finish.find(n=>n.k==="if"&&get(n.v,"limit").some(t=>t.k===H+"project_stage_receipt_matches")).v;
const clearIndex=receiptBranch.findIndex(n=>n.k===H+"clear_project_stage_active_receipt");
const dispatchIndex=receiptBranch.findIndex(n=>n.k==="if"&&n.v.some(x=>x.k===dispatch));
assert(clearIndex>=0&&dispatchIndex>clearIndex,"paid receipt must clear before incident dispatch");
assert.deepEqual(get(receiptBranch[dispatchIndex].v,"limit"),[
 {k:"check_variable",op:"=",v:[
  {k:"var",op:"=",v:"mengele_event016_project_output_applied"},
  {k:"value",op:"=",v:"constant:brilliant_scientist_value.one"},
  {k:"compare",op:"=",v:"equals"}
 ]}
]);
assert(dispatchIndex<receiptBranch.findIndex(n=>n.k===H+"adopt_completed_native_after_theory"));
// Native risky-option ownership/selector checks, without simulating engine reward selection.
const nativePath=root+"special_projects/projects/016_brilliant_scientist_projects.txt";
const nativeSource=read(nativePath);
function namedBlock(source,name){
 // Isolate the named reward before parsing. Unrelated native bare-token lists
 // are outside this strict transaction parser's supported assignment subset.
 const tokens=source.replace(/#[^\r\n]*/g,"").match(/"(?:\\.|[^"])*"|[{}=<>]|[^\s{}=<>]+/g)||[];
 const start=tokens.findIndex((t,i)=>t===name&&tokens[i+1]==="="&&tokens[i+2]==="{");assert(start>=0,name);
 let depth=1,end=start+3;for(;depth&&end<tokens.length;end++){if(tokens[end]==="{")depth++;if(tokens[end]==="}")depth--;}
 assert.equal(depth,0,name+" balanced extraction");return defs(tokens.slice(start,end).join(" "))[name];
}
let nativePrivateHookScenarios=0;
for(const[f,project,reward]of [
 ["materials","sp_brilliant_scientist_advanced_materials","self_propagating_batch"],
 ["biomedical","sp_brilliant_scientist_biomedical_acceleration","unlicensed_trial"]
]){
 const rewardId=project+"_reward_"+reward,rows=namedBlock(nativeSource,rewardId);
 assert.equal(get(rows,"fire_only_once"),"yes",rewardId+" must retain native once-only selection");
 const option=rows.find(n=>n.k==="option"&&get(n.v,"token")===rewardId+"_risky").v;
 const country=get(get(option,"iteration_output"),"country_effects");
 const privateBranch=country.find(n=>n.k==="if"),publicBranch=country.find(n=>n.k==="else_if");
 assert.deepEqual(get(privateBranch.v,"limit"),[{k:H+"project_stage_provider_is_valid",op:"=",v:"yes"}]);
 assert.deepEqual(get(publicBranch.v,"limit"),[{k:"brilliant_scientist_is_current_host",op:"=",v:"yes"}]);
 assert.deepEqual(publicBranch.v.filter(n=>n.k!=="limit").map(n=>n.k),[
  "set_temp_variable","set_temp_variable","brilliant_scientist_refresh_project_accident_pressure","brilliant_scientist_dispatch_project_accident"
 ]);
 assert.deepEqual(publicBranch.v.filter(n=>n.k==="set_temp_variable").map(n=>n.v[0]),[
  {k:"brilliant_scientist_project_family",op:"=",v:"constant:brilliant_scientist_project_family."+f},
  {k:"brilliant_scientist_requested_project_stage",op:"=",v:"constant:brilliant_scientist_project_stage.prototype"}
 ]);
 assert(country.indexOf(privateBranch)<country.indexOf(publicBranch));
 for(const branch of [0,1]){
  const s=dispatchState(f,"weaponization",branch);s.t.mengele_event016_project_family=99;
  run([privateBranch],s);assert.deepEqual(s.rolls,[{weights:[10,90],forcedBranch:branch}]);
  assert.equal(s.t.mengele_event016_project_family,c["constant:brilliant_scientist_project_family.none"]);
  assert.equal(s.t.mengele_event016_requested_stage,c["constant:brilliant_scientist_project_stage.none"]);
  assert.equal(s.v["mengele_event016_"+f+"_incident_history_count"],branch===0?1:undefined);
  assert.equal(s.t.brilliant_scientist_project_family,undefined);nativePrivateHookScenarios++;
 }
}
scenarios+=nativePrivateHookScenarios;
const loc=read(paths[5]);assert.equal(loc.charCodeAt(0),0xfeff);
const locKeys=new Set([...loc.matchAll(/^(\w+):/gm)].map(m=>m[1]));
const selectors=parse(read(paths[4])).filter(n=>n.k==="defined_text");
for(const p of ["technical","industrial","exotic","biological"]){
 const profileSelectors=selectors.filter(n=>get(n.v,"name").startsWith("GetMengeleIncident"+p[0].toUpperCase()+p.slice(1)));
 assert.equal(profileSelectors.length,4);
 for(let axis=-1;axis<4;axis++){
  const s=fresh();[s.pp,s.support,s.fuel,s.civ]=cost(p);
  if(axis>=0)s[["pp","support","fuel","civ"][axis]]-=1;
  const selected=profileSelectors.map(n=>n.v.filter(x=>x.k==="text").find(x=>!get(x.v,"trigger")||get(x.v,"trigger").every(z=>pred(z,s))));
  const keys=selected.map(x=>get(x.v,"localisation_key"));keys.forEach(k=>assert(locKeys.has(k),k));
  assert.equal(keys.filter(k=>k.endsWith("_blocked")).length,axis<0?0:1);scenarios++;
 }
}
const privateMods=defs(read(paths[3])),publicMods=defs(read(root+"dynamic_modifiers/016_brilliant_scientist_project_modifiers.txt"));
// Parent-approved urgent recovery profile after the frozen probability baseline.
// Exact AST equality rejects extra modifiers, alternate weights, or missing AI.
for(const f of [...families.map(([family])=>family),"computation"]){
 assert.deepEqual(get(dec(f),"ai_will_do"),[
  {k:"base",op:"=",v:"constant:brilliant_scientist_project_board.ai_urgent"}
 ],f+" recovery AI must use only the approved urgent base");
}
for(const[f,p]of families){
 const n=dec(f);
 assert.equal(get(n,"days_remove"),"constant:brilliant_scientist_project_board.response_"+p+"_days");
 const civ=get(get(n,"modifier"),"civilian_factory_use");assert.equal(Number(d[civ]),cost(p)[3]);
 const icon=get(n,"icon"),gfx=read("interface/016_brilliant_scientist_project_icons.gfx");
 const match=gfx.match(new RegExp('name = "'+icon+'" texturefile = "([^"]+)"'));assert(match,icon);
 const bytes=readFileSync(match[1]);assert.equal(bytes.subarray(0,4).toString(),"DDS ");
 const penalty=rows=>rows.filter(x=>!["icon","enable","remove_trigger"].includes(x.k));
 assert.deepEqual(penalty(privateMods[H+f+"_incident"]),penalty(publicMods["brilliant_scientist_"+f+"_incident"]));
 // Clear receipt authority and all values before the first refund effect.
 const cancel=get(e[H+"cancel_"+f+"_incident_recovery"],"if");
 const firstRefund=cancel.findIndex(x=>x.k==="add_political_power");
 assert(cancel.slice(0,firstRefund).some(x=>x.k==="clr_country_flag"));
 assert.equal(cancel.slice(0,firstRefund).filter(x=>x.k==="clear_variable").length,3);
}
console.log(JSON.stringify({status:"source_api_pass",scenarios,forcedDispatcherScenarios,nativePrivateHookScenarios,engineValidation:false,probabilityValidation:false,limitations:["provider validity stub","native timer/factory order modeled, not executed","engine resource caps not modeled","forced branches are not probability evidence","paid-stage receipt hook structural only, no executed post-recovery receipt replay","native reward once-only selection and public branch structurally checked, not engine-executed"],sources:[...paths,...computationPaths,stagePath,nativePath].map(path=>({path,sha256:createHash("sha256").update(readFileSync(path)).digest("hex")}))},null,2));
