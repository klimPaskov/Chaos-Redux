// Read-only source-contract checks for the shared Mengele / Event 016 adapters.
// Run from the repository root: node .tools/audit_mengele_project_adapter_contract.mjs
// Node built-ins only. No generated output or source writes. Provider validity
// and neutral grant success are explicit stubs, not engine execution.
// Contract and limitations: common/scripted_effects/016_mengele_project_bridge_effects.md
import { readFileSync } from "node:fs";
import { createHash } from "node:crypto";
import assert from "node:assert/strict";

const read = path => readFileSync(path, "utf8");
const inputPaths = {
  gates: "common/scripted_triggers/016_mengele_conventional_stage_decision_triggers.txt",
  stages: "common/scripted_effects/016_mengele_project_stage_effects.txt",
  bridge: "common/scripted_effects/016_mengele_project_bridge_effects.txt",
  hostGates: "common/scripted_triggers/016_brilliant_scientist_project_triggers.txt",
  stageTriggers: "common/scripted_triggers/016_mengele_project_stage_triggers.txt",
  incidents: "common/scripted_effects/016_mengele_conventional_incident_effects.txt",
  incidentTriggers: "common/scripted_triggers/016_mengele_conventional_incident_triggers.txt",
  cloneEffects: "common/scripted_effects/016_clone_maturation_effects.txt",
  cloneGates: "common/scripted_triggers/016_clone_maturation_triggers.txt",
  cloneDecision: "common/decisions/016_brilliant_scientist_kruger_state_clone_machine_decisions.txt",
  cloneCompatibility: "common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt",
  terminalEffects: "common/scripted_effects/016_brilliant_scientist_effects.txt",
};
const source = Object.fromEntries(Object.entries(inputPaths).map(([k,p]) => [k, read(p)]));
function parse(s) {
  const t = s.replace(/#[^\r\n]*/g, "").match(/"(?:\\.|[^"])*"|[{}=<>]|[^\s{}=<>]+/g) || [];
  let i = 0;
  function body(nested = false) {
    const a = [];
    while (i < t.length) {
      if (t[i] === "}") { i++; return a; }
      const k=t[i++], op=t[i++]; assert(["=","<",">"].includes(op), "Unsupported parse: "+k);
      let v=t[i++]; v=v==="{" ? body(true) : v?.startsWith('"') ? v.slice(1,-1) : v;
      a.push({k,op,v});
    }
    assert(!nested, "Unclosed block"); return a;
  }
  return body();
}
function block(s,name) {
  const start=s.indexOf(name+" = {"); assert(start>=0, name+" absent");
  let p=s.indexOf("{",start), depth=1, end=p+1;
  for (;depth&&end<s.length;end++) { if(s[end]==="{")depth++; if(s[end]==="}")depth--; }
  assert.equal(depth,0); return parse(s.slice(start,end))[0].v;
}
const constants={};
for(const p of [
  "common/script_constants/016_brilliant_scientist_project_constants.txt",
  "common/script_constants/016_brilliant_scientist_constants.txt",
  "common/script_constants/016_brilliant_scientist_custom_technology_constants.txt",
  "common/script_constants/016_mengele_project_stage_constants.txt",
  "common/script_constants/016_clone_maturation_constants.txt",
  "common/script_constants/016_brilliant_scientist_kruger_state_decision_constants.txt",
]) {
  const s=read(p);
  for(const m of s.matchAll(/^(\w+) = \{/gm)) {
    for(const n of block(s,m[1])) if(!Array.isArray(n.v)&&Number.isFinite(Number(n.v)))
      constants["constant:"+m[1]+"."+n.k]=Number(n.v);
  }
}
const ast=parse(source.gates), definitions=Object.fromEntries(ast.map(x=>[x.k,x.v]));
const literals=Object.fromEntries(ast.filter(x=>x.k.startsWith("@")).map(x=>[x.k,Number(x.v)]));
const cloneDecisionLiterals=Object.fromEntries(parse(source.cloneDecision).filter(x=>x.k.startsWith("@")).map(x=>[x.k,Number(x.v)]));
function number(token,state,localLiterals=literals) {
  if(token in constants) return constants[token];
  if(token in localLiterals) return localLiterals[token];
  if(token==="political_power")return state.pp;
  if(token.endsWith("^num"))return (state.arrays?.[token.slice(0,-4)]||[]).length;
  if(token.includes("^")&&state.arrays?.[token.split("^")[0]]){
    const [array,index]=token.split("^");return state.arrays[array][number(index,state,localLiterals)]||0;
  }
  if(token.startsWith("mengele_event016_active_project_stage_entries^"))
    return state.active[Number(token.split("^")[1])]||0;
  if(token in (state.temp||{}))return state.temp[token];
  if(token in (state.vars||{}))return state.vars[token];
  if(Number.isFinite(Number(token)))return Number(token);
  throw Error("Unresolved numeric token "+token);
}
function test(n,s) {
  const {k,op,v}=n;
  if(Object.hasOwn(s.triggerStubs||{},k))return s.triggerStubs[k];
  if(k==="has_capitulated")return s.capitulated===(v==="yes");
  if(k==="any_owned_state")return s.states.filter(x=>x.owner===s.country).some(x=>v.every(y=>test(y,{...s,currentState:x,previousCountry:s.country})));
  if(k==="is_controlled_by")return s.currentState.controller===(v==="PREV"?s.previousCountry:v==="ROOT"?s.rootCountry:v);
  if(k==="has_state_flag")return s.currentState.flags.has(v);
  if(k==="OR")return v.some(x=>test(x,s));
  if(k==="NOT")return !v.some(x=>test(x,s));
  if(k==="AND"||k==="hidden_trigger")return v.every(x=>test(x,s));
  if(k==="brilliant_scientist_mengele_project_stage_provider_is_valid")return s.valid;
  if(definitions[k])return definitions[k].every(x=>test(x,s));
  if(k==="has_country_flag")return s.flags.has(v);
  if(k==="has_variable")return Object.hasOwn(s.vars||{},v);
  if(k==="has_dynamic_modifier")return s.modifiers.includes(Array.isArray(v)?v.find(x=>x.k==="modifier").v:v);
  if(k==="has_tech")return s.techs.has(v);
  if(k==="is_special_project_completed")return s.projects.has(v);
  if(k==="has_dlc")return s.dlc;
  if(k==="check_variable") {
    if(v.length===1){const x=v[0],a=number(x.k,s),b=number(x.v,s);return x.op==="<"?a<b:x.op===">"?a>b:a===b;}
    const d=Object.fromEntries(v.map(x=>[x.k,x.v])), a=number(d.var,s),b=number(d.value,s);
    if(d.compare==="equals")return a===b;
    if(d.compare==="less_than")return a<b;
    if(d.compare==="greater_than")return a>b;
    if(d.compare==="greater_than_or_equals")return a>=b;
    throw Error("Unsupported compare "+d.compare);
  }
  if(k==="has_resources_in_country"){
    const d=Object.fromEntries(v.map(x=>[x.k,x.v]));return (s.res[d.resource]||0)<number(d.amount,s);
  }
  if(k==="has_equipment")return s.support<number(v[0].v,s);
  const val={num_of_civilian_factories_available_for_projects:s.cic,
    num_of_available_military_factories:s.mil,has_fuel:s.fuel}[k];
  if(val!==undefined)return op==="<"?val<number(v,s):val>number(v,s);
  throw Error("Unsupported trigger "+k);
}
const gate=(name,s)=>definitions[name].every(x=>test(x,s));
let counts={adapter:0,initialization:0,publication:0,grant:0,adoption:0,singularity:0,weaponization:0,finish:0,maturation:0,maturationWrapper:0};
function check(group,label,actual){counts[group]++;assert(actual,label);}
const families=[
  ["electronics",1,["sp_air_radar"]],
  ["materials",2,["sp_brilliant_scientist_advanced_materials"]],
  ["rocketry",3,["sp_rockets_flying_bomb","sp_air_jet_engine"]],
  ["high_energy",4,["sp_nuclear_reactor"]],
  ["biomedical",5,["sp_brilliant_scientist_biomedical_acceleration"]],
];
for(const [f,index]of families)for(const stage of ["theory","deployment","weaponization"]){
  const id=f+"_"+stage,h="brilliant_scientist_mengele_"+id+"_decision";
  const c=k=>constants["constant:brilliant_scientist_project_stage_cost."+id+"_"+k];
  const stageId=constants["constant:brilliant_scientist_project_stage."+stage];
  const flags=new Set(["mengele_event016_provider_receipts_initialized"]);
  const previous={deployment:"prototype",weaponization:"deployment"}[stage];
  if(previous)flags.add("mengele_event016_"+f+"_"+previous+"_completed");
  const req=JSON.stringify(definitions[h+"_requirements"]), res={};
  for(const r of req.matchAll(/MENGELE_\w+_(STEEL|CHROMIUM|RUBBER|TUNGSTEN)/g))
    res[r[1].toLowerCase()]=c("resource_units");
  const allTokens=(key)=>[...req.matchAll(new RegExp('"k":"'+key+'","op":"=","v":"([^"]+)"',"g"))].map(m=>m[1]);
  const s={valid:true,flags,active:{},techs:new Set(allTokens("has_tech")),
    projects:new Set(allTokens("is_special_project_completed")),dlc:true,
    pp:c("political_power"),support:c("support_equipment"),fuel:c("fuel"),
    cic:c("civilian_factories"),mil:c("military_factories"),res};
  const a=(label,result)=>check("adapter",id+" "+label,result);
  a("exact",gate(h+"_requirements",s)&&gate(h+"_can_pay",s));
  for(const k of ["cic","pp","support",...(s.fuel?["fuel"]:[])])
    a("short "+k,!gate(h+"_can_pay",{...s,[k]:s[k]-1}));
  a("poor remains visible",gate(h+"_visible",{...s,cic:0,pp:0,support:0,fuel:0}));
  a("own visible",gate(h+"_visible",{...s,active:{[index]:stageId}}));
  a("own blocks start",!gate(h+"_requirements",{...s,active:{[index]:stageId}}));
  a("other family independent",gate(h+"_requirements",{...s,active:{[index===1?2:1]:4}}));
  a("invalid cancels",gate(h+"_cancel_trigger",{...s,valid:false,active:{[index]:stageId}}));
  a("exact stays",!gate(h+"_cancel_trigger",{...s,active:{[index]:stageId}}));
  a("stale cancels",gate(h+"_cancel_trigger",{...s,active:{[index]:stage==="theory"?3:1}}));
  for(const r of Object.keys(res))a("reserve "+r,!gate(h+"_requirements",{...s,res:{...res,[r]:res[r]-1}}));
  if(s.mil)a("military reserve",!gate(h+"_requirements",{...s,mil:s.mil-1}));
  if(["rocketry","high_energy"].includes(f)&&stage==="weaponization"){
    a("DLC native needed",!gate(h+"_requirements",{...s,projects:new Set()}));
    a("noDLC predecessor",gate(h+"_requirements",{...s,dlc:false,projects:new Set()}));
  }
  if(["electronics","rocketry","high_energy"].includes(f)&&stage==="deployment")
    a("native needed without DLC",!gate(h+"_requirements",{...s,dlc:false,projects:new Set()}));
}
for(const[f]of families)check("initialization",f+" empty uninitialized",
  gate("brilliant_scientist_mengele_"+f+"_decision_receipt_is_empty",{flags:new Set(),active:{}}));
const effectDefinitions={};
function effects(seq,s) {
  let last=false;
  for(const n of seq){
    if(s.effectStubs?.[n.k]){s.effectStubs[n.k](s);continue;}
    if(n.k==="if"){last=n.v.find(x=>x.k==="limit").v.every(x=>test(x,s));if(last)effects(n.v.filter(x=>x.k!=="limit"),s);}
    else if(n.k==="else"){if(!last)effects(n.v,s);}
    else if(n.k==="hidden_effect")effects(n.v,s);
    else if(n.k==="custom_effect_tooltip")s.tooltips.push(n.v);
    else if(n.k==="set_country_flag")s.flags.add(n.v);
    else if(n.k==="clr_country_flag")s.flags.delete(n.v);
    else if(n.k==="set_temp_variable"){const x=n.v[0];s.temp[x.k]=number(x.v,s);}
    else if(n.k==="multiply_temp_variable"){const x=n.v[0];s.temp[x.k]*=number(x.v,s);}
    else if(n.k==="add_to_temp_variable"){const x=n.v[0];s.temp[x.k]=(s.temp[x.k]||0)+number(x.v,s);}
    else if(n.k==="subtract_from_temp_variable"){const x=n.v[0];s.temp[x.k]-=number(x.v,s);}
    else if(n.k==="set_variable"||n.k==="add_to_variable"){
      const x=n.v[0],parts=x.k.split("^"),target=parts.length===2?s.arrays[parts[0]]:s.vars,key=parts.length===2?number(parts[1],s):x.k;
      target[key]=(n.k==="set_variable"?0:(target[key]||0))+number(x.v,s);
    }
    else if(n.k==="clear_variable")delete s.vars[n.v];
    else if(n.k==="add_political_power")s.pp+=number(n.v,s);
    else if(n.k==="add_fuel")s.fuel+=number(n.v,s);
    else if(n.k==="add_equipment_to_stockpile"){
      const d=Object.fromEntries(n.v.map(x=>[x.k,x.v]));
      if(d.type==="support_equipment")s.support+=number(d.amount,s);
      else if(d.type==="clone_equipment_1"){
        assert(!s.flags.has("brilliant_scientist_krg_clone_maturation_paid"),"Clone output precedes receipt consumption");
        s.clones+=number(d.amount,s);
      }else throw Error("Unmodeled equipment transaction "+d.type);
    }
    else if(n.k==="activate_mission")s.missions.push(n.v);
    else if(n.k==="remove_decision"){
      s.removals.push(n.v);
      if(s.nativeRemovalCallback)effects(s.nativeRemovalCallback,s);
    }
    else if(n.k==="add_to_array"){const d=Object.fromEntries(n.v.map(x=>[x.k,x.v]));(s.arrays[d.array]??=[]).push(number(d.value,s));}
    else if(n.k==="while_loop_effect"){
      let iterations=0;const limit=n.v.find(x=>x.k==="limit").v;
      while(limit.every(x=>test(x,s))){assert(++iterations<100,"Unbounded source loop");effects(n.v.filter(x=>x.k!=="limit"),s);}
    }
    else if(n.k==="add_dynamic_modifier")s.modifiers.push(n.v.find(x=>x.k==="modifier").v);
    else if(n.k==="remove_dynamic_modifier")s.modifiers=s.modifiers.filter(x=>x!==n.v.find(x=>x.k==="modifier").v);
    else if(n.k==="force_update_dynamic_modifier")s.refreshes++;
    // Availability has separate publisher scenarios above; the adoption harness
    // records this boundary call without evaluating unrelated publishers.
    else if(n.k==="brilliant_scientist_mengele_reconcile_project_availability")s.availabilityCalls++;
    else if(effectDefinitions[n.k])effects(effectDefinitions[n.k],s);
    else if(n.k==="chaosx_grant_custom_operational_technology"){
      s.calls.push([s.temp.chaosx_custom_technology_family,s.temp.chaosx_custom_technology_source]);
      s.temp.chaosx_custom_technology_grant_applied=s.grantResult;
    }else throw Error("Unsupported effect "+n.k);
  }
}
const reconcile=block(source.stages,"brilliant_scientist_mengele_reconcile_project_availability");
const publisher=reconcile.find(n=>n.k==="if"&&JSON.stringify(n).includes("directorate_special_project_electronics_available"));
assert(publisher,"Five-family publisher absent");
for(const[f,,native]of families){
  const available="directorate_special_project_"+f+"_available",theory="mengele_event016_"+f+"_theory_completed";
  const run=(name,flags,projects,valid,expected)=>{
    const s={flags:new Set(flags),projects:new Set(projects),valid,temp:{}};
    effects([publisher],s);check("publication",f+" "+name,s.flags.has(available)===expected);
  };
  run("Theory publishes",[theory],[],true,true);
  run("no Theory clears",[available],[],true,false);
  run("private Prototype clears",[theory,available,"mengele_event016_"+f+"_prototype_completed"],[],true,false);
  run("completed receipt clears",[theory,available,"directorate_special_project_"+f+"_completed"],[],true,false);
  for(const n of native)run(n+" clears",[theory,available],["sp:"+n],true,false);
  run("nonprivate present untouched",[theory,available],[],false,true);
  run("nonprivate absent untouched",[theory],[],false,false);
}
const mapping=[
 ["teleportation","portal","quantum_transit"],["cloning","clone","cloning"],
 ["robotics","robot","autonomous_cognition"],["paleogenetics","paleogenetic","paleogenetics"],
 ["xenobiological_synthesis","xenobiological","xenobiological_synthesis"],
 ["alien_arms","alien_infantry","alien_arms"],["temporal","temporal","temporal_mechanics"],
];
const grant=block(source.bridge,"brilliant_scientist_mengele_grant_native_custom_operational_package");
for(const[f,custom,native]of mapping){
 const theory="mengele_event016_"+f+"_theory_completed",proto="mengele_event016_"+f+"_prototype_completed";
 const id=constants["constant:brilliant_scientist_project_family."+f];
 const make=()=>({valid:true,flags:new Set([theory,proto]),projects:new Set(["sp:sp_brilliant_scientist_"+native]),
   temp:{mengele_event016_native_grant_family:id,brilliant_scientist_project_family:901,
     mengele_event016_project_family:902,mengele_event016_requested_stage:903},calls:[],grantResult:1});
 for(const mode of ["valid","invalid_owner","no_theory","no_prototype","no_native","neutral_failure","noncustom"]){
   const s=make();if(mode==="invalid_owner")s.valid=false;if(mode==="no_theory")s.flags.delete(theory);
   if(mode==="no_prototype")s.flags.delete(proto);if(mode==="no_native")s.projects.clear();
   if(mode==="neutral_failure")s.grantResult=0;if(mode==="noncustom")s.temp.mengele_event016_native_grant_family=1;
   const oldFlags=[...s.flags],expected=["valid","neutral_failure"].includes(mode);
   effects(grant,s);
   check("grant",f+" "+mode+" call count",s.calls.length===(expected?1:0));
   check("grant",f+" "+mode+" result",s.temp.mengele_event016_native_operational_grant_applied===(mode==="valid"?1:0));
   check("grant",f+" "+mode+" cleanup",["mengele_event016_native_grant_family","chaosx_custom_technology_family","chaosx_custom_technology_source"].every(k=>s.temp[k]===0));
   check("grant",f+" "+mode+" selector preservation",s.temp.brilliant_scientist_project_family===901&&s.temp.mengele_event016_project_family===902&&s.temp.mengele_event016_requested_stage===903);
   check("grant",f+" "+mode+" history preservation",JSON.stringify([...s.flags])===JSON.stringify(oldFlags));
   if(expected)check("grant",f+" "+mode+" mapped provenance",s.calls[0][0]===constants["constant:chaosx_custom_technology_family."+custom]&&s.calls[0][1]===constants["constant:mengele_event016_project_stage.provenance_mengele"]);
 }
}
// Evaluate current adoption, authentication, initialization, component recording,
// selector cleanup and Prototype output source. Native completion/provider/neutral
// API responses are injected state, not an emulation of HOI4's project engine.
for(const m of source.stageTriggers.matchAll(/^(brilliant_scientist_mengele_\w+) = \{/gm))
  definitions[m[1]]=block(source.stageTriggers,m[1]);
for(const name of ["adopt_completed_native_after_theory","record_singularity_component",
  "initialize_project_stage_receipts","clear_project_stage_selectors",
  "sync_native_project_prototypes","apply_family_stage_output"])
  effectDefinitions["brilliant_scientist_mengele_"+name]=block(source.stages,"brilliant_scientist_mengele_"+name);
effectDefinitions.brilliant_scientist_mengele_grant_native_custom_operational_package=grant;
const adopt=effectDefinitions.brilliant_scientist_mengele_adopt_completed_native_after_theory;
const components=["command_core","power_link","containment_lattice","temporal_authenticator","delivery_architecture","fail_deadly_governor"];
const outerKeys=["mengele_event016_project_family","mengele_event016_requested_stage","mengele_event016_project_index",
 "mengele_event016_project_output_applied","mengele_event016_computation_output_applied","mengele_event016_stage_output_gap",
 "mengele_event016_project_output_authorized","mengele_event016_project_availability_reconciled","brilliant_scientist_singularity_component"];
const makeAdoption=f=>({valid:true,flags:new Set([`mengele_event016_${f}_theory_completed`]),projects:new Set(),
 temp:Object.fromEntries(outerKeys.map((k,i)=>[k,i===0?constants["constant:brilliant_scientist_project_family."+f]:i===1?1:i===3?1:910+i])),
 vars:{mengele_event016_singularity_component_count:0},arrays:{},calls:[],grantResult:1,modifiers:[],refreshes:0,availabilityCalls:0});
const saved=s=>outerKeys.map(k=>s.temp[k]);
const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
for(let mask=0;mask<64;mask++)for(const mode of ["valid","invalid_owner","no_theory"]){
 const s=makeAdoption("singularity"),selected=components.filter((_,i)=>mask&(1<<i));
 s.projects=new Set(selected.map(c=>"sp:sp_brilliant_scientist_singularity_"+c));
 if(mode==="invalid_owner")s.valid=false;
 if(mode==="no_theory")s.flags.clear();
 const before=saved(s),nativeBefore=[...s.projects],expected=mode==="valid"?selected:[];
 for(let repeat=0;repeat<2;repeat++){
  effects(adopt,s);const label=`mask ${mask} ${mode} repeat ${repeat}`;
  check("singularity",label+" exact private components",components.every(c=>s.flags.has("mengele_event016_singularity_"+c+"_completed")===expected.includes(c)));
  check("singularity",label+" unique count",s.vars.mengele_event016_singularity_component_count===expected.length);
  check("singularity",label+" Prototype iff six",s.flags.has("mengele_event016_singularity_prototype_completed")===(expected.length===6));
  check("singularity",label+" Prototype modifier once",s.modifiers.filter(x=>x==="brilliant_scientist_singularity_prototype").length===(expected.length===6?1:0));
  check("singularity",label+" nine outer values restored",equal(saved(s),before));
  check("singularity",label+" native read only and no custom grant",equal([...s.projects],nativeBefore)&&s.calls.length===0);
  check("singularity",label+" no payment mutation",Object.keys(s.vars).every(k=>k==="mengele_event016_singularity_component_count")&&Object.values(s.arrays).every(a=>a.every(x=>x===0)));
  check("singularity",label+" no terminal or foreign history",[...s.flags].every(x=>x.startsWith("mengele_event016_singularity_")||x==="mengele_event016_provider_receipts_initialized"));
 }
}
// Ordinary fourteen-family native adoption remains routed through the actual
// source sync/output helper; this includes either authentic Rocketry project.
const ordinary=["computation",...families.map(x=>x[0]),...mapping.map(x=>x[0]),"biological_weapons"];
for(const f of ordinary){
 const auth=definitions["brilliant_scientist_mengele_"+f+"_native_output_is_authentic"];
 const native=[...JSON.stringify(auth).matchAll(/"k":"is_special_project_completed","op":"=","v":"([^"]+)"/g)].map(x=>x[1]);
 assert(native.length,"Missing native mapping "+f);
 for(const project of native){
  const s=makeAdoption(f);s.projects.add(project);const before=saved(s);
  effects(adopt,s);effects(adopt,s);
  check("adoption",f+" "+project+" private Prototype",s.flags.has("mengele_event016_"+f+"_prototype_completed"));
  check("adoption",f+" "+project+" nine outer values",equal(saved(s),before));
  check("adoption",f+" "+project+" native remains evidence",equal([...s.projects],[project]));
 }
}
// Evaluate the two exact host entry gates. Board readiness and the nested
// affordability helper are declared inputs, not inferred from score ranking.
for (const [family,index,projects] of [
  ["rocketry",3,["sp:sp_rockets_long_range_ballistic_missile","sp:sp_air_supersonic_jet"]],
  ["high_energy",4,["sp:sp_thermo_nuclear_bomb","sp:sp_nuclear_warheads"]],
]) {
  const entry=block(source.hostGates,"brilliant_scientist_can_begin_"+family+"_weaponization");
  for(let stage=0;stage<5;stage++) for(let mask=0;mask<32;mask++) {
    const s={dlc:!!(mask&1),board:!!(mask&2),pay:!!(mask&4),projects:new Set(projects.filter((_,i)=>mask&(8<<i)))};
    function evaluate(n) {
      if(n.k==="OR")return n.v.some(evaluate);
      if(n.k==="NOT")return !n.v.some(evaluate);
      if(n.k==="has_dlc"){assert.equal(n.v,"Gotterdammerung");return s.dlc;}
      if(n.k==="is_special_project_completed")return s.projects.has(n.v);
      if(n.k==="brilliant_scientist_project_board_is_ready")return s.board;
      if(n.k==="brilliant_scientist_can_pay_"+family+"_weaponization")return s.pay;
      if(n.k==="check_variable"){
        const d=Object.fromEntries(n.v.map(x=>[x.k,x.v]));
        assert.equal(d.var,"brilliant_scientist_project_stage_entries^"+index);
        assert.equal(d.compare,"equals");
        return stage===constants[d.value];
      }
      throw Error("Unexpected weaponization gate "+n.k);
    }
    const expected=s.board&&s.pay&&stage===constants["constant:brilliant_scientist_project_stage.deployment"]&&(!s.dlc||s.projects.size>0);
    check("weaponization",family+" stage "+stage+" mask "+mask,entry.every(evaluate)===expected);
  }
}
// Finish integration: the starting five aligned arrays are a paid-receipt fixture,
// not a mocked receipt predicate. Execute actual match, index, clear and refund
// source. Only family output and weighted incident dispatch are boundary stubs.
for(const name of ["finish_project_stage","prepare_project_index","clear_project_stage_active_receipt","refund_snapshot_direct_costs"])
 effectDefinitions["brilliant_scientist_mengele_"+name]=block(source.stages,"brilliant_scientist_mengele_"+name);
for(const m of source.incidentTriggers.matchAll(/^(brilliant_scientist_mengele_\w+) = \{/gm))
 definitions[m[1]]=block(source.incidentTriggers,m[1]);
for(const[f]of families)for(const name of [`finish_${f}_incident_recovery`,`clear_${f}_incident`])
 effectDefinitions["brilliant_scientist_mengele_"+name]=block(source.incidents,"brilliant_scientist_mengele_"+name);
const receiptArrays=["mengele_event016_active_project_stage_entries","mengele_event016_active_cost_political_power_entries",
 "mengele_event016_active_cost_support_equipment_entries","mengele_event016_active_cost_fuel_entries","mengele_event016_active_cost_civilian_factory_commitment_entries"];
for(const[f,index]of families)for(const stage of ["theory","deployment","weaponization"])
for(const mode of ["success","invalid_provider","failed_output","mismatched_stage"]){
 const s=makeAdoption(f),familyId=constants["constant:brilliant_scientist_project_family."+f],stageId=constants["constant:brilliant_scientist_project_stage."+stage];
 const quote=k=>constants[`constant:brilliant_scientist_project_stage_cost.${f}_${stage}_${k}`];
 const paid=[stageId,quote("political_power"),quote("support_equipment"),quote("fuel"),quote("civilian_factories")];
 const other=index===1?2:1;s.arrays=Object.fromEntries(receiptArrays.map((key,i)=>{
  const values=Array(15).fill(0);values[index]=paid[i];values[other]=i===0?4:700+i;return[key,values];
 }));
 s.flags=new Set(["mengele_event016_provider_receipts_initialized"]);
 if(stage!=="theory")s.flags.add(`mengele_event016_${f}_${stage==="deployment"?"prototype":"deployment"}_completed`);
 s.pp=0;s.support=0;s.fuel=0;s.valid=mode!=="invalid_provider";s.outputCalls=0;s.dispatchCalls=0;
 const select=()=>{s.temp.mengele_event016_project_family=familyId;s.temp.mengele_event016_requested_stage=mode==="mismatched_stage"?(stageId===1?3:1):stageId;};
 s.effectStubs={
  brilliant_scientist_mengele_apply_family_stage_output:q=>{
   q.outputCalls++;assert.equal(q.temp.mengele_event016_project_output_authorized,1);
   assert(receiptArrays.every(key=>q.arrays[key][index]===0),"Receipt must clear before output");
   if(mode!=="failed_output"){
    q.flags.add(`mengele_event016_${f}_${stage}_completed`);q.temp.mengele_event016_project_output_applied=1;
   }
  },
  brilliant_scientist_mengele_dispatch_conventional_incident:q=>{q.dispatchCalls++;assert.equal(q.temp.mengele_event016_project_output_applied,1);},
 };
 const finish=()=>{select();effects(effectDefinitions.brilliant_scientist_mengele_finish_project_stage,s);};
 finish();const label=f+" "+stage+" "+mode,matching=mode!=="mismatched_stage";
 check("finish",label+" matching receipt cleared",receiptArrays.every((key,i)=>s.arrays[key][index]===(matching?0:paid[i])));
 check("finish",label+" concurrent family untouched",receiptArrays.every((key,i)=>s.arrays[key][other]===(i===0?4:700+i)));
 check("finish",label+" output call",s.outputCalls===(["success","failed_output"].includes(mode)?1:0));
 check("finish",label+" dispatch only success",s.dispatchCalls===(mode==="success"?1:0));
 const refund=mode==="invalid_provider"||mode==="failed_output";
 check("finish",label+" exact snapshot refund",equal([s.pp,s.support,s.fuel],refund?paid.slice(1,4):[0,0,0]));
 check("finish",label+" first finish result",s.temp.mengele_event016_stage_finished===(matching?1:0));
 if(mode==="success"){
  // Explicit post-dispatch, paid recovery fixture. Execute the real recovery
  // receipt predicate and completion/clear helpers; no weighted roll is modeled.
  s.flags.add(`mengele_event016_${f}_incident_active`);s.flags.add(`mengele_event016_${f}_incident_recovery_active`);
  s.modifiers.push(`brilliant_scientist_mengele_${f}_incident`);
  for(const cost of ["political_power","support_equipment","fuel"])s.vars[`mengele_event016_${f}_incident_recovery_cost_${cost}`]=27;
  effects(effectDefinitions[`brilliant_scientist_mengele_finish_${f}_incident_recovery`],s);
  check("finish",label+" actual recovery completed",s.temp.mengele_event016_conventional_recovery_finished===1&&s.flags.has(`mengele_event016_${f}_recovery_history`));
  check("finish",label+" transient recovery cleared",!s.flags.has(`mengele_event016_${f}_incident_active`)&&!s.flags.has(`mengele_event016_${f}_incident_recovery_active`)&&!s.modifiers.includes(`brilliant_scientist_mengele_${f}_incident`));
 }
 const before={output:s.outputCalls,dispatch:s.dispatchCalls,wallet:[s.pp,s.support,s.fuel],arrays:JSON.stringify(s.arrays),flags:[...s.flags],vars:{...s.vars}};
 // Even provider recovery cannot resurrect a consumed stage receipt.
 s.valid=true;
 finish();
 check("finish",label+" duplicate no output or dispatch",s.outputCalls===before.output&&s.dispatchCalls===before.dispatch);
 check("finish",label+" duplicate no refund",equal([s.pp,s.support,s.fuel],before.wallet));
 check("finish",label+" duplicate receipt/history unchanged",JSON.stringify(s.arrays)===before.arrays&&equal([...s.flags],before.flags)&&equal(s.vars,before.vars));
 check("finish",label+" duplicate not finished and selectors clear",s.temp.mengele_event016_stage_finished===0&&s.temp.mengele_event016_project_family===0&&s.temp.mengele_event016_requested_stage===0&&s.temp.mengele_event016_project_output_authorized===0);
}
// Durable KRG maturation suite: invoke the actual live wrapper callbacks and
// core. Provider identity/project health and reserve-refresh engine behavior are
// explicit stubs; owned-state traversal and PREV/ROOT relationships are modeled.
for(const n of parse(source.cloneGates))definitions[n.k]=n.v;
for(const n of parse(source.cloneEffects))effectDefinitions[n.k]=n.v;
const clonePrefix="brilliant_scientist_krg_",cloneDecisionId=clonePrefix+"run_bounded_clone_growth_cycle";
const cloneWrapper=block(source.cloneDecision,cloneDecisionId),field=k=>cloneWrapper.find(n=>n.k===k)?.v;
effectDefinitions[clonePrefix+"complete_clone_growth_cycle"]=block(source.cloneCompatibility,clonePrefix+"complete_clone_growth_cycle");
const debitSource=read("common/scripted_effects/chaosx_dynamic_effects.txt");
for(const k of ["remove_support_equipment_from_stockpile","remove_fuel_from_stockpile"])effectDefinitions[k]=block(debitSource,k);
const terminal=block(source.terminalEffects,"brilliant_scientist_cleanup_transient_targets_after_world_end");
const terminalCloneHook=terminal.filter(n=>n.k===clonePrefix+"cleanup_clone_maturation");
const walk=seq=>seq.flatMap(n=>[n,...(Array.isArray(n.v)?walk(n.v):[])]);
const wrapperCheck=(label,condition)=>check("maturationWrapper",label,condition),mentions=(seq,k)=>walk(seq).some(n=>n.k===k);
wrapperCheck("native PP zero, custom row and PP planning65",field("cost")==="0"&&field("custom_cost_text")==="clone_maturation_custom_cost"&&number(field("ai_hint_pp_cost"),{},cloneDecisionLiterals)===65);
wrapperCheck("same inclusive affordability in admission and custom cost",mentions(field("available"),clonePrefix+"clone_maturation_can_pay")&&mentions(field("custom_cost_trigger"),clonePrefix+"clone_maturation_can_pay"));
const cicToken=field("modifier").find(n=>n.k==="civilian_factory_use").v;
const cicMirror=source.cloneDecision.match(new RegExp("^"+cicToken+"\\s*=\\s*(\\d+)","m"));
wrapperCheck("dedicated CIC mirror equals4/profile",cicToken==="@CLONE_MATURATION_CIC"&&Number(cicMirror?.[1])===4&&constants["constant:clone_maturation.civilian_factories"]===4);
wrapperCheck("90day timer30day cooldown",number(field("days_remove"),{})===90&&number(field("days_re_enable"),{})===30);
wrapperCheck("actual begin/cancel/compatibility finish calls",mentions(field("complete_effect"),clonePrefix+"begin_clone_maturation")&&mentions(field("cancel_effect"),clonePrefix+"cancel_clone_maturation")&&mentions(field("remove_effect"),clonePrefix+"complete_clone_growth_cycle"));
wrapperCheck("compatibility helper only delegates finish",equal(effectDefinitions[clonePrefix+"complete_clone_growth_cycle"],[{k:clonePrefix+"finish_clone_maturation",op:"=",v:"yes"}]));
wrapperCheck("pending wrapper stays despite visibility changes",field("cancel_if_not_visible")==="no");
wrapperCheck("timer cancels on missing receipt or live invalidity",mentions(field("cancel_trigger"),clonePrefix+"clone_maturation_receipt_is_current")&&mentions(field("cancel_trigger"),clonePrefix+"clone_maturation_is_operational"));
wrapperCheck("worldend cleanup has one direct maturation hook",terminalCloneHook.length===1);
wrapperCheck("cleanup refunds before native removal",equal(effectDefinitions[clonePrefix+"cleanup_clone_maturation"].map(n=>n.k),[clonePrefix+"cancel_clone_maturation","remove_decision"]));
wrapperCheck("no obsolete batch/cap/rifle output in live wrapper/core",!/(pay_project_batch_cost|clone_growth_cycle_maximum|infantry_equipment_0|clone_infantry_batch|clone_support_batch)/.test(JSON.stringify(cloneWrapper)+source.cloneEffects+source.cloneGates));
const cloneOp=clonePrefix+"clone_maturation_is_operational",cloneStart=clonePrefix+"clone_maturation_can_start";
const makeClone=()=>({country:"KRG",rootCountry:"GER",krg:true,capitulated:false,
 triggerStubs:{brilliant_scientist_krg_decisions_are_active:true,brilliant_scientist_kruger_focus_cloning_is_operational:true,brilliant_scientist_krg_clone_identity_revolt_is_prevented:false},
 techs:new Set(["clone_infantry_access_tech"]),states:[{owner:"KRG",controller:"KRG",flags:new Set(["brilliant_scientist_krg_clone_growth_site"])}],
 flags:new Set(),vars:{brilliant_scientist_krg_clone_growth_cycles:0},temp:{},pp:65,support:150,fuel:1000,cic:4,
 clones:0,refreshCount:0,missions:[],removals:[],tooltips:[],
 effectStubs:{clone_refresh_reserve_manpower:s=>{s.refreshCount++;s.refreshedStock=s.clones;assert(!s.flags.has(clonePrefix+"clone_maturation_paid"));}}});
const cloneWallet=s=>[s.pp,s.support,s.fuel],cloneCheck=(label,v)=>check("maturation",label,v);
const cloneRun=(callback,s)=>effects(field(callback),s),cloneCleanup=s=>effects(terminalCloneHook,s);
for(const cic of [0,4])for(const marker of ["brilliant_scientist_krg_clone_growth_site","brilliant_scientist_cloning_growth_site"]){
 const s=makeClone();s.states[0].flags=new Set([marker]);cloneCheck("exact admission "+marker,gate(cloneStart,s));s.cic=cic;
 cloneRun("complete_effect",s);cloneCheck("both CIC ordering models pay once",equal(cloneWallet(s),[0,0,0]));
 cloneCheck("pending receipt exists",gate(clonePrefix+"clone_maturation_receipt_is_current",s));
 cloneCheck("pending blocks another start",!gate(cloneStart,s));
 const tips=s.tooltips.length;cloneRun("complete_effect",s);cloneCheck("duplicate begin no charge or misleading started tooltip",equal(cloneWallet(s),[0,0,0])&&s.tooltips.length===tips);
 cloneRun("remove_effect",s);cloneCheck("100 real clone equipment",s.clones===100);cloneCheck("refresh after output once",s.refreshCount===1&&s.refreshedStock===100);cloneCheck("history once",s.vars.brilliant_scientist_krg_clone_growth_cycles===1);
 cloneRun("remove_effect",s);cloneRun("cancel_effect",s);cloneCleanup(s);cloneCheck("duplicate finish cancel cleanup inert",s.clones===100&&s.refreshCount===1&&s.vars.brilliant_scientist_krg_clone_growth_cycles===1&&equal(cloneWallet(s),[0,0,0]));
}
for(const key of ["pp","support","fuel","cic"]){const s=makeClone();s[key]--;cloneCheck("one short "+key,!gate(cloneStart,s));}
for(const reason of ["foreign_owner","lost_control","country_flag_only","no_technology","closed","suspended","capitulated"]){
 const s=makeClone();cloneRun("complete_effect",s);
 if(reason==="foreign_owner")s.states[0].owner="GER";
 if(reason==="lost_control")s.states[0].controller="GER";
 if(reason==="country_flag_only"){s.states=[];s.flags.add("brilliant_scientist_krg_clone_growth_site_operational");}
 if(reason==="no_technology")s.techs.clear();
 if(reason==="closed")s.triggerStubs.brilliant_scientist_krg_decisions_are_active=false;
 if(reason==="suspended")s.triggerStubs.brilliant_scientist_kruger_focus_cloning_is_operational=false;
 if(reason==="capitulated")s.capitulated=true;
 cloneCheck(reason+" live gate invalid",!gate(cloneOp,s));cloneRun("remove_effect",s);
 cloneCheck(reason+" exact refund without output",equal(cloneWallet(s),[65,150,1000])&&s.clones===0);
 cloneRun("cancel_effect",s);cloneRun("remove_effect",s);cloneCleanup(s);
 cloneCheck(reason+" repeated refund blocked",equal(cloneWallet(s),[65,150,1000])&&s.vars.brilliant_scientist_krg_clone_growth_cycles===0);
}
for(const cycles of [7,8,9]){const s=makeClone();s.vars.brilliant_scientist_krg_clone_growth_cycles=cycles;cloneCheck("cycle "+cycles+" no lifetime cap",gate(cloneStart,s));cloneRun("complete_effect",s);cloneRun("remove_effect",s);cloneCheck("cycle "+cycles+" advances real history",s.clones===100&&s.vars.brilliant_scientist_krg_clone_growth_cycles===cycles+1);}
{const s=makeClone();cloneRun("complete_effect",s);s.vars.brilliant_scientist_krg_clone_maturation_paid_pp=61;s.vars.brilliant_scientist_krg_clone_maturation_paid_support=141;s.vars.brilliant_scientist_krg_clone_maturation_paid_fuel=901;cloneRun("cancel_effect",s);cloneCheck("refund stored amounts not profile",equal(cloneWallet(s),[61,141,901]));}
{const s=makeClone();cloneRun("complete_effect",s);s.vars.brilliant_scientist_krg_clone_maturation_paid_output=103;cloneRun("remove_effect",s);cloneCheck("output stored quantity not profile",s.clones===103);}
for(const missing of ["pp","support","fuel","output"]){const s=makeClone();cloneRun("complete_effect",s);delete s.vars[clonePrefix+"clone_maturation_paid_"+missing];cloneRun("remove_effect",s);cloneCheck("malformed "+missing+" fails closed",s.clones===0&&equal(cloneWallet(s),[0,0,0])&&!s.flags.has(clonePrefix+"clone_maturation_paid"));}
{const s=makeClone();s.vars.brilliant_scientist_krg_clone_growth_cycles=3;s.flags.add("brilliant_scientist_focus_unlock_clone_identity_pressure_crises");cloneRun("complete_effect",s);cloneRun("remove_effect",s);cloneRun("remove_effect",s);cloneCheck("identity threshold4 mission once",s.missions.length===1&&s.vars.brilliant_scientist_krg_clone_growth_cycles===4);}
{const s=makeClone();cloneCheck("foreign outer ROOT does not reject invoking owner",gate(cloneOp,s));s.states[0].controller="GER";cloneCheck("outer ROOT control cannot substitute invoking control",!gate(cloneOp,s));}
for(const removalCallback of [false,true]){
 const s=makeClone();cloneRun("complete_effect",s);s.triggerStubs.brilliant_scientist_krg_decisions_are_active=false;
 if(removalCallback)s.nativeRemovalCallback=field("remove_effect");
 cloneCleanup(s);cloneCleanup(s);cloneRun("remove_effect",s);
 cloneCheck("terminal cleanup refund once, removal callback="+removalCallback,equal(cloneWallet(s),[65,150,1000])&&s.clones===0&&s.vars.brilliant_scientist_krg_clone_growth_cycles===0);
 cloneCheck("terminal removal targets exact native decision",s.removals.length===2&&s.removals.every(x=>x===cloneDecisionId));
}
console.log(JSON.stringify({classification:"source-only; provider validity, native completion, board readiness, affordability and neutral API results stubbed; availability callback counted in adoption; finish scenarios stub authorized family output/weighted dispatch and seed paid stage/recovery receipts, but execute actual matching/clearing/refund/recovery; maturation executes actual wrapper/core/site scopes with provider/project-health and reserve-refresh stubs; native CIC order/removal callbacks modeled, not engine evidence; old history AST equality is historical in-memory evidence, not compared to the live thin wrapper",assertions:counts,
  hashes:Object.fromEntries(Object.entries(inputPaths).map(([k,p])=>[p,createHash("sha256").update(source[k]).digest("hex")]))},null,2));
