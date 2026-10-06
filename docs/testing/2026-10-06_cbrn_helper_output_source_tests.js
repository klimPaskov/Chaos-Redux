// Actual-source caller-storage regression. Conservative helper-frame cleanup,
// not native execution. Reuses the existing fixed-point VM without editing it.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const {VM:BaseVM,S,parse,root,definitions,constants,ticks}=require('../plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
// Two regular-variable primitives needed by these fragments, absent from the shared VM.
class VM extends BaseVM {
 eval(nodes){let chunk=[];
  for(const n of nodes){
   if(n.key==='clamp_variable'||n.key==='add_to_variable'){
    if(chunk.length&&!super.eval(chunk))return false;chunk=[];
    if(n.key==='add_to_variable'){
     const key=this.field(n.value,'var')||n.value[0].key,delta=this.value(this.field(n.value,'value')||n.value[0].value);
     this.write(key,this.value(key)+delta,false);continue;
    }
    const key=this.field(n.value,'var'),value=this.value(key),lo=this.value(this.field(n.value,'min')),hi=this.value(this.field(n.value,'max'));
    this.write(key,value<lo?lo:value>hi?hi:value,false);
   }else chunk.push(n);
  }
  return chunk.length?super.eval(chunk):true;
 }
}
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const paths=['common/scripted_effects/cbrn_exposure_effects.txt','common/scripted_effects/cbrn_chemical_state_effects.txt','common/scripted_effects/cbrn_doctrine_effects.txt','common/scripted_effects/cbrn_diplomacy_effects.txt','common/scripted_effects/cbrn_consequence_effects.txt','common/scripted_effects/chaos_meter_effects.txt'];
const bytes=new Map(paths.map(f=>[f,fs.readFileSync(path.join(root,f))]));
const trees=new Map([...bytes].map(([f,b])=>[f,parse(b.toString('utf8'))]));
for(const [file,names] of [['common/script_constants/cbrn_system_constants.txt',['cbrn_math','cbrn_meter','cbrn_contamination_class','cbrn_contamination_threshold','cbrn_attribution_state','cbrn_evidence_threshold']],['common/script_constants/cbrn_chemical_delivery_constants.txt',['cbrn_chemical_air_cleanliness']],['common/script_constants/chaos_meter_constants.txt',['chaos_meter_deaths']]]){
 const text=fs.readFileSync(path.join(root,file),'utf8');
 for(const name of names){const block=text.match(new RegExp('^'+name+' = \\{[\\s\\S]*?^\\}','m'));assert(block,name);
  const cat=parse(block[0])[0];for(const item of cat.value)if(typeof item.value==='string'&&/^-?\d+(\.\d+)?$/.test(item.value))constants.set('constant:'+cat.key+'.'+item.key,ticks(item.value));}
}
const def=(tree,name)=>{const d=tree.find(n=>n.key===name);assert(d,name);return d.value;};
const current=def(trees.get(paths[0]),'cbrn_apply_state_contamination_delta_internal');
const beforeBytes=fs.readFileSync(path.join(__dirname,'2026-10-06_cbrn_helper_outputs_before/cbrn_state_delta_internal.txt'));
const before=def(parse(beforeBytes.toString('utf8')),'cbrn_apply_state_contamination_delta_internal');
definitions.set('cbrn_refresh_state_contamination_class',def(trees.get(paths[0]),'cbrn_refresh_state_contamination_class'));
definitions.set('cbrn_chemical_set_air_contribution_from_class',def(trees.get(paths[1]),'cbrn_chemical_set_air_contribution_from_class'));
const assignment=(n,key)=>n.key==='set_temp_variable'&&n.value[0]?.key===key;
const intro=body=>body.slice(0,body.findIndex(n=>assignment(n,'cbrn_state_previous_contamination_class'))+1);
const airFragment=body=>{const end=body.findIndex(n=>n.key==='cbrn_chemical_set_air_contribution_from_class');assert(end>=0);
 const start=end>0&&assignment(body[end-1],'cbrn_air_contribution_value')?end-1:end;return body.slice(start,end+1);};
const cases=[];
for(const [intensity,expected] of [[0,0],[0.99999,0],[1,1],[9.99999,1],[10,2],[24.99999,2],[25,3],[49.99999,3],[50,4],[74.99999,4],[75,5],[100,5]]){
 const newVM=new VM();newVM.write('cbrn_chemical_contamination',ticks(intensity),false);assert(newVM.eval(intro(current)));
 assert.equal(newVM.value('cbrn_state_previous_contamination_class'),ticks(expected));
 const oldVM=new VM();oldVM.write('cbrn_chemical_contamination',ticks(intensity),false);assert(oldVM.eval(intro(before)));
 assert.equal(oldVM.value('cbrn_state_previous_contamination_class'),0n);
 cases.push({id:'class-'+intensity,expected,after:Number(newVM.value('cbrn_state_previous_contamination_class')/S),before:0,oldDefectReproduced:expected>0});
}
for(const [clazz,expected] of [[0,0],[1,0],[2,1],[3,3],[4,5],[5,10]]){
 const newVM=new VM().set('cbrn_air_contribution_class',clazz);assert(newVM.eval(airFragment(current)));assert.equal(newVM.value('cbrn_air_contribution_value'),ticks(expected));
 const oldVM=new VM().set('cbrn_air_contribution_class',clazz);assert(oldVM.eval(airFragment(before)));assert.equal(oldVM.value('cbrn_air_contribution_value'),0n);
 cases.push({id:'air-class-'+clazz,expected,after:expected,before:0,oldDefectReproduced:expected>0});
}
for(const [file,fn] of [[paths[2],'cbrn_apply_theater_decontamination_assignment_paid'],[paths[3],'cbrn_diplomacy_complete_international_decon_mission']]){
 const walk=nodes=>nodes.flatMap(n=>[n,...(Array.isArray(n.value)?walk(n.value):[])]),nodes=walk(def(trees.get(file),fn));
 const at=nodes.findIndex(n=>n.key==='cbrn_apply_state_contamination_delta_internal');assert(at>=0);
 for(const key of ['cbrn_state_previous_contamination_value','cbrn_state_new_contamination_value'])assert(nodes.slice(0,at).some(n=>assignment(n,key)),file+' missing '+key);
 cases.push({id:'cleanup-storage-'+fn,after:'old/new outputs allocated before returning helper',before:'no caller allocation',nativeCleanupAmounts:'not simulated'});
}
// Narrow immediate-loss arithmetic: actual first three native-helper statements,
// excluding native population caps/random multipliers and death-ledger effects.
const sequenceContaining=(nodes,pred)=>{
 if(nodes.some(pred))return nodes;
 for(const n of nodes)if(Array.isArray(n.value)){const found=sequenceContaining(n.value,pred);if(found)return found;}
 return null;
};
const dispatch=def(trees.get(paths[4]),'cbrn_dispatch_apply_state_consequences');
const callerFragment=(callKey,output)=>{
 const sequence=sequenceContaining(dispatch,n=>n.key===callKey);assert(sequence,callKey);
 const at=sequence.findIndex(n=>n.key===callKey);assert(at>0);
 assert(assignment(sequence[at-1],output),callKey+' missing ancestor storage');
 assert.equal(sequence[at+1].key,'set_temp_variable');
 return sequence.slice(at-1,at+2);
};
const deathNodes=sequenceContaining(def(trees.get(paths[5]),'chaos_meter_register_state_civilian_deaths_percent'),n=>assignment(n,'chaos_deaths_change'));assert(deathNodes);
const deathStart=deathNodes.findIndex(n=>assignment(n,'chaos_deaths_change'));assert(deathStart>=0);
definitions.set('chaos_meter_register_state_civilian_deaths_percent',deathNodes.slice(deathStart,deathStart+3));
const deathCaller=callerFragment('chaos_meter_register_state_civilian_deaths_percent','chaos_deaths_change');
for(const [populationK,fraction,expected] of [[100,0.00999,999],[100,0.01,1000],[100,0.02,2000]]){
 const make=()=>{const v=new VM().set('chaos_state_deaths_percent',fraction);v.write('state_population_k',ticks(populationK),false);return v;};
 const newer=make();assert(newer.eval(deathCaller));assert.equal(newer.value('cbrn_action_civilian_deaths'),ticks(expected));
 const older=make();assert(older.eval(deathCaller.slice(1)));assert.equal(older.value('cbrn_action_civilian_deaths'),0n);
 cases.push({id:'immediate-loss-output-'+expected,expected,after:expected,before:0,oldDefectReproduced:true,nativeLossCalculation:'only first three arithmetic statements modeled'});
}
definitions.set('cbrn_apply_state_evidence_delta_internal',def(trees.get(paths[0]),'cbrn_apply_state_evidence_delta_internal'));
definitions.set('cbrn_refresh_state_attribution',def(trees.get(paths[0]),'cbrn_refresh_state_attribution'));
const evidenceCaller=callerFragment('cbrn_apply_state_evidence_delta_internal','cbrn_state_attribution_output');
for(const [quality,expected] of [[19,0],[20,1],[45,2],[75,3],[100,3]]){
 const make=()=>{const v=new VM().set('cbrn_state_evidence_delta',0);v.write('cbrn_evidence_quality',ticks(quality),false);return v;};
 const newer=make();assert(newer.eval(evidenceCaller));assert.equal(newer.value('cbrn_action_attribution_state'),ticks(expected));
 const older=make();assert(older.eval(evidenceCaller.slice(1)));assert.equal(older.value('cbrn_action_attribution_state'),0n);
 cases.push({id:'nested-attribution-output-'+quality,expected,after:expected,before:0,oldDefectReproduced:expected>0});
}
for(const [f,b] of bytes)assert.equal(hash(fs.readFileSync(path.join(root,f))),hash(b),'source changed during test');
const out={status:'passed',cases:cases.length,sourceHashes:Object.fromEntries([...bytes].map(([f,b])=>[f,hash(b)])),baselineSourceHash:hash(beforeBytes),results:cases,
 limitations:['STATE variables are modeled, not native scope execution.','Strict helper frames discard only newly created temporary storage; caller-owned modifications survive.','Tests exercise actual class/air/nested-attribution fragments and inspect actual cleanup caller allocations; full state delta, global air change and real cleanup totals remain outside the model.','Immediate-loss cases narrow the native death helper to its first three actual arithmetic statements; population caps, random multipliers, native death totals and achievement unlock are not simulated.']};
fs.writeFileSync(path.join(__dirname,'2026-10-06_cbrn_helper_output_source_results.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({status:out.status,cases:out.cases,reproducedBaselineFailures:cases.filter(x=>x.oldDefectReproduced).length},null,2));
