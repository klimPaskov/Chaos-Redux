// Actual-source caller-storage regression. Conservative helper-frame cleanup,
// not native execution. Reuses the existing fixed-point VM without editing it.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const {VM:BaseVM,S,parse,root,definitions,constants,ticks}=require('../plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
// One primitive needed by the actual classifier, absent from the shared VM.
class VM extends BaseVM {
 eval(nodes){let chunk=[];
  for(const n of nodes){
   if(n.key==='clamp_variable'){
    if(chunk.length&&!super.eval(chunk))return false;chunk=[];
    const key=this.field(n.value,'var'),value=this.value(key),lo=this.value(this.field(n.value,'min')),hi=this.value(this.field(n.value,'max'));
    this.write(key,value<lo?lo:value>hi?hi:value,false);
   }else chunk.push(n);
  }
  return chunk.length?super.eval(chunk):true;
 }
}
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const paths=['common/scripted_effects/cbrn_exposure_effects.txt','common/scripted_effects/cbrn_chemical_state_effects.txt','common/scripted_effects/cbrn_doctrine_effects.txt','common/scripted_effects/cbrn_diplomacy_effects.txt'];
const bytes=new Map(paths.map(f=>[f,fs.readFileSync(path.join(root,f))]));
const trees=new Map([...bytes].map(([f,b])=>[f,parse(b.toString('utf8'))]));
for(const [file,names] of [['common/script_constants/cbrn_system_constants.txt',['cbrn_math','cbrn_meter','cbrn_contamination_class','cbrn_contamination_threshold']],['common/script_constants/cbrn_chemical_delivery_constants.txt',['cbrn_chemical_air_cleanliness']]]){
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
for(const [f,b] of bytes)assert.equal(hash(fs.readFileSync(path.join(root,f))),hash(b),'source changed during test');
const out={status:'passed',cases:cases.length,sourceHashes:Object.fromEntries([...bytes].map(([f,b])=>[f,hash(b)])),baselineSourceHash:hash(beforeBytes),results:cases,
 limitations:['STATE variables are modeled, not native scope execution.','Strict helper frames discard only newly created temporary storage; caller-owned modifications survive.','Tests exercise actual class/air source fragments and inspect actual cleanup caller allocations; full state delta, global air change and real cleanup totals remain outside the model.']};
fs.writeFileSync(path.join(__dirname,'2026-10-06_cbrn_helper_output_source_results.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({status:out.status,cases:out.cases,reproducedBaselineFailures:cases.filter(x=>x.oldDefectReproduced).length},null,2));
