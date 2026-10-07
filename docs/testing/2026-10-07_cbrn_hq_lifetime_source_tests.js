// Actual HQ source under the existing conservative scripted-helper frames.
// No engine execution. Run: node docs/testing/2026-10-07_cbrn_hq_lifetime_source_tests.js
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const {VM:BaseVM,S,parse,root,definitions,constants,ticks}=require('../plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
const file='common/scripted_effects/cbrn_hq_effects.txt',beforeFile='docs/testing/2026-10-07_cbrn_hq_lifetime/before/'+file;
const bytes=new Map(),hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=f=>{if(!bytes.has(f))bytes.set(f,fs.readFileSync(path.join(root,f)));return bytes.get(f).toString('utf8');};
const trees=new Map(),tree=f=>{if(!trees.has(f))trees.set(f,parse(read(f)));return trees.get(f);};
read('docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
const def=(t,k)=>{const d=t.find(n=>n.key===k);assert(d,k);return d.value;};
const walk=ns=>ns.flatMap(n=>[n,...(Array.isArray(n.value)?walk(n.value):[])]);
for(const f of ['common/script_constants/cbrn_hq_constants.txt','common/script_constants/cbrn_system_constants.txt','common/script_constants/cbrn_doctrine_constants.txt','common/script_constants/cbrn_designer_constants.txt','common/script_constants/cbrn_commander_progression_constants.txt']) {
 // Bounded numeric constant categories. Nested schema metadata is not executed.
 const text=read(f),blocks=text.match(/^[a-z0-9_]+ = \{[\s\S]*?^\}/gm)||[];
 for(const block of blocks){const name=block.slice(0,block.indexOf(' ='));if(!name.startsWith('cbrn_hq_')&&!['cbrn_math','cbrn_meter','cbrn_hazard_budget','cbrn_doctrine_leader','cbrn_decontamination_designer_effect','cbrn_commander_progression'].includes(name))continue;const cat=parse(block)[0];for(const n of cat.value)if(typeof n.value==='string'&&/^-?\d+(\.\d+)?$/.test(n.value))constants.set('constant:'+cat.key+'.'+n.key,ticks(n.value));}
}
const packageKeys=['mask','filter_condition','decon','instrument','support','motorized','fuel','medical','manpower'].map(k=>'cbrn_hq_'+k+'_debit');
const starterKeys=[...packageKeys,...['preparation_base','preparation_min','preparation_max','active_duration','command_power_native','command_power_total','preparation_days'].map(k=>'cbrn_hq_'+k)];
const nestedOutputs=['cbrn_mask_stock_debit_completed','cbrn_hq_family_debit_completed','cbrn_motorized_stock_debit_completed'];
const operations=[
 ['protective','theater_protective_posture','cbrn_hq_active_protective_posture'],['decon','decontamination_corridor','cbrn_hq_active_decontamination_corridor'],['seal_area','seal_operational_area','cbrn_hq_active_sealed_operational_area'],['antidote','mass_antidote_response','cbrn_hq_active_antidote_response'],['infection','seal_infection_corridor','cbrn_hq_active_infection_corridor']
].map(([kind,name,trait])=>({kind,name,trait,start:'cbrn_hq_start_'+name,upkeep:'cbrn_hq_debit_'+kind+'_upkeep',activation:'cbrn_hq_set_'+kind+'_activation_package',weekly:'cbrn_hq_set_'+kind+'_upkeep_package'}));
const sourceBefore=tree(beforeFile),sourceAfter=tree(file),results=[];
const triggerFile='common/scripted_triggers/cbrn_hq_triggers.txt',progressionFile='common/scripted_effects/cbrn_commander_progression_effects.txt',progressionTriggerFile='common/scripted_triggers/cbrn_commander_progression_triggers.txt';
const protectionFile='common/scripted_effects/cbrn_protection_effects.txt',dynamicFile='common/scripted_effects/chaosx_dynamic_effects.txt',eventFile='events/cbrn_hq_events.txt',abilityFile='common/abilities/cbrn_hq_abilities.txt';
const baseDefinitions=[
 ...tree(triggerFile).filter(n=>/^cbrn_hq_(force_is_|committed_force_is_|has_no_preparation)/.test(n.key)),
 ...tree(progressionTriggerFile).filter(n=>n.key==='cbrn_commander_hq_completion_is_eligible'),
 ...tree(progressionFile).filter(n=>n.key==='cbrn_commander_record_completed_hq_operation'),
 ...tree(protectionFile).filter(n=>n.key==='cbrn_debit_mask_stockpile_oldest_first'),
 ...tree(dynamicFile).filter(n=>n.key==='cbrn_debit_motorized_stockpile_oldest_first'),
];
function load(stage){for(const n of [...(stage==='before'?sourceBefore:sourceAfter),...baseDefinitions]) definitions.set(n.key,n.value);}
const decode=x=>Number(x)/Number(S),snapshot=(vm,keys)=>Object.fromEntries(keys.map(k=>[k,decode(vm.value(k))]));
// Temporary storage and BaseVM.run cleanup are unchanged. Only regular storage
// switches between this one character and its OWNER country. Native effects
// below are narrow captured arguments or explicit fixture stock changes.
class VM extends BaseVM {
 constructor({band=1,readiness=60,commander=false,designer=false,pay=true}={}){
  super();this.scope='character';this.character=this.regularVars;this.country=new Map();this.traits=new Set(commander?['chemical_operations_commander']:[]);this.characterFlags=new Set();this.countryFlags=new Set();this.designer=designer;this.pay=pay;this.stock=new Map();this.trace=[];this.packageReceipts=[];this.predicateCaptures=[];
  this.character.set('num_battalions',ticks([99,100,200][band-1]));this.character.set('cbrn_hq_committed_force_band',ticks(band));this.character.set('chemical_readiness',ticks(999));
  this.country.set('chemical_readiness',ticks(readiness));this.country.set('cbrn_medical_capacity',ticks(100));this.country.set('cbrn_military_mask_filter_condition',ticks(100));
  for(const k of ['gas_mask_equipment_reconditioned','gas_mask_equipment_1','gas_mask_equipment_2','gas_mask_equipment_3','gas_mask_equipment_4','decontamination_equipment_1','decontamination_equipment_2','decontamination_equipment_3','cbrn_instrument_equipment_1','cbrn_instrument_equipment_2','cbrn_instrument_equipment_3','motorized_equipment_0','motorized_equipment_1','support_equipment_1'])this.stock.set(k,ticks(100000));
 }
 inScope(scope,action){const prior=this.scope,store=this.regularVars;this.scope=scope;this.regularVars=scope==='country'?this.country:this.character;try{return action();}finally{this.scope=prior;this.regularVars=store;}}
 value(token){if(token.startsWith('num_equipment@')){assert.equal(this.scope,'country');return this.stock.get(token.slice(14))??0n;}return super.value(token);}
 run(name,...args){if(name==='cbrn_hq_debit_operating_package')this.packageReceipts.push(snapshot(this,packageKeys));return super.run(name,...args);}
 eval(nodes){let chunk=[];const flush=()=>{if(!chunk.length)return true;const c=chunk;chunk=[];return super.eval(c);};
  for(const n of nodes){const k=n.key,v=n.value;
   const local=['OWNER','event_target:cbrn_hq_commander','save_event_target_as','clamp_temp_variable','clamp_variable','round_temp_variable','add_to_variable','subtract_from_variable','add_equipment_to_stockpile','add_command_power','add_fuel','add_manpower','country_event','meta_effect','has_trait','remove_unit_leader_trait','has_character_flag','set_character_flag','clr_character_flag','set_country_flag','is_army_leader','is_field_marshal','is_assigned','num_units','cbrn_designer_has_truck_mounted_wash_systems','cbrn_refresh_country_mask_snapshot','cbrn_apply_military_mask_loss','cbrn_achievement_record_hq_commitment','cbrn_commander_refresh_earned_traits'];
   const predicate=/^cbrn_hq_(can_pay_.*_upkeep|.*_command_is_valid)$/.test(k);
   if(!local.includes(k)&&!predicate){chunk.push(n);continue;}
   if(!flush())return false;
   if(k==='OWNER'||k==='event_target:cbrn_hq_commander'){if(!this.inScope(k==='OWNER'?'country':'character',()=>this.eval(v)))return false;}
   else if(k==='clamp_temp_variable'||k==='clamp_variable'){
    const key=this.field(v,'var'),a=this.value(key),lo=this.field(v,'min'),hi=this.field(v,'max');let b=a;
    if(lo!==undefined&&b<this.value(lo))b=this.value(lo);if(hi!==undefined&&b>this.value(hi))b=this.value(hi);this.write(key,b,k==='clamp_temp_variable');
   }else if(k==='round_temp_variable'){const a=this.value(v);assert(a>=0n);this.write(v,((a+S/2n)/S)*S);}
   else if(k==='add_to_variable'||k==='subtract_from_variable'){const key=this.field(v,'var')||v[0].key,delta=this.value(this.field(v,'value')||v[0].value);this.write(key,this.value(key)+(k==='add_to_variable'?delta:-delta),false);}
   else if(k==='add_equipment_to_stockpile'){assert.equal(this.scope,'country');const type=this.field(v,'type'),amount=this.value(this.field(v,'amount'));this.trace.push({kind:k,scope:this.scope,type,amount:decode(amount)});const next=(this.stock.get(type)||0n)+amount;assert(next>=0n,'stock overdraw '+type);this.stock.set(type,next);}
   else if(['add_command_power','add_fuel','add_manpower'].includes(k)){assert.equal(this.scope,'country');this.trace.push({kind:k,scope:this.scope,amount:decode(this.value(v))});}
   else if(k==='country_event'){this.trace.push({kind:k,scope:this.scope,id:this.field(v,'id'),days:decode(this.value(this.field(v,'days')))});}
   else if(k==='save_event_target_as'){assert.equal(this.scope,'character');assert.equal(v,'cbrn_hq_commander');}
   else if(k==='meta_effect'){
    const text=this.field(v,'text'),first=text[0];
    if(first.key==='add_timed_unit_leader_trait')this.trace.push({kind:'preparing_trait',scope:this.scope,days:decode(this.value('cbrn_hq_preparation_days'))});
    else {assert.equal(first.key,'unit_leader_event');this.trace.push({kind:'scheduled_leader_event',scope:this.scope,id:decode(this.value('cbrn_hq_scheduled_event_id')),days:decode(this.value('cbrn_hq_scheduled_event_days'))});}
   }else if(k==='has_trait'){if(!this.traits.has(v))return false;}
   else if(k==='remove_unit_leader_trait')this.traits.delete(v);
   else if(k==='has_character_flag'){assert.equal(this.scope,'character');if(!this.characterFlags.has(v))return false;}
   else if(k==='set_character_flag'||k==='clr_character_flag'){assert.equal(this.scope,'character');if(k==='set_character_flag')this.characterFlags.add(v);else this.characterFlags.delete(v);}
   else if(k==='set_country_flag'){assert.equal(this.scope,'country');this.countryFlags.add(v);}
   else if(['is_army_leader','is_field_marshal','is_assigned'].includes(k)){const yes=k!=='is_field_marshal';if(yes!==(v==='yes'))return false;}
   else if(k==='num_units'){assert.equal(n.op,'>');if(!(ticks(1)>this.value(v)))return false;}
   else if(k==='cbrn_designer_has_truck_mounted_wash_systems'){if(this.designer!==(v==='yes'))return false;}
   else if(predicate){this.predicateCaptures.push(k);const yes=k.includes('can_pay')?this.pay:true;if(yes!==(v==='yes'))return false;}
   else if(k==='cbrn_apply_military_mask_loss'){assert.equal(this.scope,'country');const now=this.value('cbrn_military_mask_filter_condition')-this.value('cbrn_mask_condition_loss');this.write('cbrn_military_mask_filter_condition',now>0n?now:0n,false);}
   // Snapshot/achievement/earned-trait dispatch are explicit no-op boundaries.
  }
  return flush();
 }
}
function test(id,action){try{const detail=action();results.push({id,status:'passed',...detail});}catch(e){results.push({id,status:'failed',error:e.message});}}
// Prove that the only engine-source differences are newly literal owned slots.
const added=[];
function compareBlocks(old,current,owner,p=''){
 let i=0;for(const n of current){const prior=old[i];if(prior&&n.key===prior.key&&n.op===prior.op&&Array.isArray(n.value)&&Array.isArray(prior.value)){compareBlocks(prior.value,n.value,owner,p+'/'+n.key);i++;}
  else if(prior&&JSON.stringify(n)===JSON.stringify(prior)){i++;}
  else{assert.equal(n.key,'set_temp_variable',owner+p);assert.equal(n.value.length,1);assert.equal(n.value[0].value,'constant:cbrn_math.zero');const key=n.value[0].key;
   const allowed=operations.some(o=>o.start===owner)?starterKeys:operations.some(o=>o.upkeep===owner)?packageKeys:owner==='cbrn_hq_debit_operating_package'?nestedOutputs:[];
   assert(allowed.includes(key),'unauthorized initializer '+owner+' '+key);added.push({helper:owner,path:p,key});}
 }assert.equal(i,old.length,'source statement removed '+owner+p);
}
test('AST preserves all source statements except the promised literal caller declarations',()=>{assert.deepEqual(sourceAfter.map(n=>n.key),sourceBefore.map(n=>n.key));for(const n of sourceAfter)compareBlocks(def(sourceBefore,n.key),n.value,n.key);assert.equal(added.length,129);return{newDeclarations:added};});
const manifestPath='docs/testing/2026-10-07_cbrn_hq_lifetime/baseline_manifest.json',manifest=JSON.parse(read(manifestPath));
test('all8 baseline hashes match and7 untouched dependency files remain byte-identical',()=>{assert.equal(manifest.files.length,8);for(const f of manifest.files){assert.equal(hash(Buffer.from(read(f.beforePath),'utf8')),f.sha256,f.beforePath);if(f.path!==file)assert.equal(hash(Buffer.from(read(f.path),'utf8')),f.sha256,f.path);}return{baselineCommit:manifest.baselineCommit};});
test('owned slots occur at exact entries and immediately before four nested debit returns',()=>{
 for(const op of operations)for(const [helper,keys]of [[op.start,starterKeys],[op.upkeep,packageKeys]]){const entry=def(sourceAfter,helper).slice(0,keys.length);assert.deepEqual(entry.map(n=>n.value[0].key),keys);for(const n of entry){assert.equal(n.key,'set_temp_variable');assert.equal(n.value[0].value,'constant:cbrn_math.zero');}}
 const owner=def(sourceAfter,'cbrn_hq_debit_operating_package').find(n=>n.key==='OWNER').value;
 for(const [call,key]of [['cbrn_debit_mask_stockpile_oldest_first','cbrn_mask_stock_debit_completed'],['cbrn_hq_debit_decontamination_stock_oldest_first','cbrn_hq_family_debit_completed'],['cbrn_hq_debit_instrument_stock_oldest_first','cbrn_hq_family_debit_completed'],['cbrn_debit_motorized_stockpile_oldest_first','cbrn_motorized_stock_debit_completed']]){const branch=owner.find(n=>Array.isArray(n.value)&&n.value.some(v=>v.key===call)).value,index=branch.findIndex(n=>n.key===call);assert.equal(branch[index-1].key,'set_temp_variable');assert.deepEqual(branch[index-1].value,[{key,op:'=',value:'constant:cbrn_math.zero'}]);}
});
function producerControl(op,kind,options){const vm=new VM(options);for(const key of kind==='activation'?starterKeys:packageKeys)vm.write(key,0n);assert(vm.run(op[kind==='activation'?'activation':'weekly']));
 const expected=snapshot(vm,kind==='activation'?starterKeys:packageKeys);
 if(kind==='activation'){assert(vm.run('cbrn_hq_calculate_preparation_days'));assert(vm.run('cbrn_hq_apply_operations_commander_preparation_discount'));assert(vm.run('cbrn_hq_enforce_preparation_efficiency_budget'));expected.cbrn_hq_preparation_days=decode(vm.value('cbrn_hq_preparation_days'));}
 return expected;
}
const readinessCases=[0,39.99999,40,59.99999,60,79.99999,80];
for(const op of operations)for(const band of [1,2,3])for(const readiness of readinessCases)for(const commander of [false,true])for(const designer of op.kind==='decon'?[false,true]:[false])test(`activation-${op.kind}-${band}-${readiness}-${commander}-${designer}`,()=>{
 load('after');const options={band,readiness,commander,designer},expected=producerControl(op,'activation',options),newer=new VM(options);assert(newer.run(op.start));
 assert.deepEqual(newer.packageReceipts[0],Object.fromEntries(packageKeys.map(k=>[k,expected[k]])));
 const prep=expected.cbrn_hq_preparation_days,active=expected.cbrn_hq_active_duration;
 assert.deepEqual(newer.trace.filter(t=>t.kind==='scheduled_leader_event').map(t=>[t.id,t.days]),[[3,prep+active],[1,prep]]);
 assert.equal(newer.trace.find(t=>t.kind==='preparing_trait').days,prep);
 const recoveries=newer.trace.filter(t=>t.kind==='country_event'),expectedRecoveries=[];
 if(expected.cbrn_hq_medical_debit>0)expectedRecoveries.push('cbrn_hq.'+(19+band));if(expected.cbrn_hq_manpower_debit>0)expectedRecoveries.push('cbrn_hq.'+(22+band));
 assert.deepEqual(recoveries.map(t=>t.id),expectedRecoveries);for(const t of recoveries){assert.equal(t.scope,'country');assert.equal(t.days,prep+active);}
 assert(!newer.characterFlags.has('cbrn_hq_command_completion_recorded'),'preparation creates no completed receipt');
 assert.equal(newer.trace.find(t=>t.kind==='add_command_power').amount,-Math.max(0,expected.cbrn_hq_command_power_total-expected.cbrn_hq_command_power_native)||0);
 assert.equal(newer.character.get('cbrn_hq_operation_code'),constants.get('constant:cbrn_hq_operation.'+op.name));assert(!newer.country.has('cbrn_hq_operation_code'));assert(!newer.character.has('cbrn_hq_mask_consumption_total'));assert.equal(newer.vars.size,0);
 load('before');const older=new VM(options);assert(older.run(op.start));assert(Object.values(older.packageReceipts[0]).every(x=>x===0));assert.equal(older.trace.filter(t=>t.kind==='scheduled_leader_event').at(-1).days,0);
 return{band,readiness,commander,designer,expected,after: newer.trace,beforePackage:older.packageReceipts[0],baselineFailureReproduced:true};
});
for(const op of operations)for(const band of [1,2,3])for(const designer of op.kind==='decon'?[false,true]:[false])test(`upkeep-${op.kind}-${band}-${designer}`,()=>{
 load('after');const options={band,designer},expected=producerControl(op,'upkeep',options),newer=new VM(options);assert(newer.run(op.upkeep));assert.deepEqual(newer.packageReceipts[0],expected);assert.equal(newer.vars.size,0);
 load('before');const older=new VM(options);assert(older.run(op.upkeep));assert(Object.values(older.packageReceipts[0]).every(x=>x===0));return{expected,after:newer.trace,baselineFailureReproduced:true};
});
// Independently isolate nested completion ownership. Package inputs intentionally
// belong to the test's outer caller for both versions, so only nested return
// completion loss is under test here, not the outer starter defect.
for(const requested of [0,1,6,15,30])test('mixed-model-completed-ledgers-'+requested,()=>{
 const setup=()=>{const vm=new VM();for(const k of packageKeys)vm.write(k,0n);for(const k of ['mask','decon','instrument','motorized'])vm.write('cbrn_hq_'+k+'_debit',ticks(requested));
  for(const key of vm.stock.keys())vm.stock.set(key,0n);for(const [type,count]of [['gas_mask_equipment_reconditioned',2],['gas_mask_equipment_1',3],['gas_mask_equipment_2',7],['decontamination_equipment_1',2],['decontamination_equipment_2',3],['decontamination_equipment_3',7],['cbrn_instrument_equipment_1',2],['cbrn_instrument_equipment_2',3],['cbrn_instrument_equipment_3',7],['motorized_equipment_0',5],['motorized_equipment_1',7]])vm.stock.set(type,ticks(count));return vm;};
 load('after');const newer=setup();assert(newer.run('cbrn_hq_debit_operating_package'));load('before');const older=setup();assert(older.run('cbrn_hq_debit_operating_package'));
 for(const key of ['cbrn_hq_mask_consumption_total','cbrn_mask_replacement_demand','cbrn_hq_decontamination_consumption_total','cbrn_hq_instrument_consumption_total','cbrn_hq_motorized_losses_total']){assert.equal(decode(newer.country.get(key)||0n),Math.min(requested,12));assert.equal(older.country.get(key)||0n,0n);assert(!newer.character.has(key));}
 assert.deepEqual(newer.stock,older.stock);assert.deepEqual([...newer.vars.keys()].sort(),packageKeys.slice().sort());
 return{requested,completed:Math.min(requested,12),afterDebits:newer.trace,beforePhysicalDebitsSame:true,baselineFailureReproduced:requested>0};
});
test('distinct mixed stock families credit separate actual completed amounts',()=>{
 const setup=()=>{const vm=new VM();for(const k of packageKeys)vm.write(k,0n);for(const [kind,amount]of [['mask',6],['decon',7],['instrument',9],['motorized',4]])vm.write('cbrn_hq_'+kind+'_debit',ticks(amount));for(const k of vm.stock.keys())vm.stock.set(k,0n);
  for(const [model,count]of [['gas_mask_equipment_reconditioned',1],['gas_mask_equipment_1',2],['decontamination_equipment_1',2],['decontamination_equipment_2',3],['cbrn_instrument_equipment_1',1],['cbrn_instrument_equipment_2',2],['cbrn_instrument_equipment_3',7],['motorized_equipment_0',1],['motorized_equipment_1',7]])vm.stock.set(model,ticks(count));return vm;};
 load('after');const newer=setup();assert(newer.run('cbrn_hq_debit_operating_package'));load('before');const older=setup();assert(older.run('cbrn_hq_debit_operating_package'));
 const totals={cbrn_hq_mask_consumption_total:3,cbrn_mask_replacement_demand:3,cbrn_hq_decontamination_consumption_total:5,cbrn_hq_instrument_consumption_total:9,cbrn_hq_motorized_losses_total:4};
 for(const [k,n]of Object.entries(totals)){assert.equal(newer.country.get(k),ticks(n));assert.equal(older.country.get(k)||0n,0n);}assert.deepEqual(newer.stock,older.stock);
 return{totals,orderedActualDebits:newer.trace,baselineFailureReproduced:true};
});
const events=tree(eventFile),eventBody=id=>def(events.find(n=>n.key==='unit_leader_event'&&n.value.some(v=>v.key==='id'&&v.value===id)).value,'immediate');
for(const op of operations)for(const pay of [false,true])test(`final-paid-upkeep-receipt-${op.kind}-${pay}`,()=>{
 load('after');const vm=new VM({pay,band:2});vm.character.set('cbrn_hq_operation_code',constants.get('constant:cbrn_hq_operation.'+op.name));vm.character.set('cbrn_hq_upkeep_ticks_remaining',ticks(1));vm.traits.add(op.trait);assert(vm.eval(eventBody('cbrn_hq.2')));
 const eligible=pay&&op.kind!=='protective';assert.equal(vm.characterFlags.has('cbrn_hq_command_completion_recorded'),eligible);
 if(!pay){assert.equal(vm.packageReceipts.length,0);assert(!vm.character.has('cbrn_hq_upkeep_ticks_remaining'));assert(!vm.traits.has(op.trait));}
 else{assert.equal(vm.packageReceipts.length,1);assert.equal(vm.character.get('cbrn_hq_upkeep_ticks_remaining'),0n);}
 // The real no-posture trigger still refuses reuse while persistent code exists.
 assert.equal(vm.run('cbrn_hq_has_no_preparation_or_active_posture'),false);assert(vm.eval(eventBody('cbrn_hq.3')));assert.equal(vm.run('cbrn_hq_has_no_preparation_or_active_posture'),true);
 assert.equal(vm.vars.size,0);return{pay,receipt:eligible,characterCounters:Object.fromEntries([...vm.character].filter(([k])=>k.includes('completed')).map(([k,v])=>[k,decode(v)])),scopeIsolation:!vm.country.has('cbrn_hq_command_completion_recorded'),plannedEndCodeGuard:true,predicates:vm.predicateCaptures};
});
test('consecutive operations and final paid ticks preserve no temporary storage or duplicate receipt',()=>{
 load('after');const vm=new VM({band:3});for(const op of [operations[4],operations[0],operations[1]]){assert(vm.run(op.start));assert.equal(vm.vars.size,0);assert(vm.eval(eventBody('cbrn_hq.3')));}
 const receiptVm=new VM();const op=operations[1];receiptVm.character.set('cbrn_hq_operation_code',constants.get('constant:cbrn_hq_operation.'+op.name));receiptVm.character.set('cbrn_hq_upkeep_ticks_remaining',ticks(2));receiptVm.traits.add(op.trait);
 assert(receiptVm.eval(eventBody('cbrn_hq.2')));assert(!receiptVm.characterFlags.has('cbrn_hq_command_completion_recorded'));assert(receiptVm.eval(eventBody('cbrn_hq.2')));assert(receiptVm.characterFlags.has('cbrn_hq_command_completion_recorded'));assert.equal(receiptVm.character.get('cbrn_chemical_operations_completed'),ticks(1));assert(receiptVm.eval(eventBody('cbrn_hq.2')));assert.equal(receiptVm.character.get('cbrn_chemical_operations_completed'),ticks(1));
 return{scheduledArguments:vm.trace.filter(t=>t.kind==='scheduled_leader_event'),duplicateReceiptBlocked:true};
});
read(abilityFile);
test('native one-time effect consumers retain exact five starter calls',()=>{const found=walk(tree(abilityFile)).filter(n=>operations.some(o=>o.start===n.key));assert.deepEqual(found.map(n=>n.key).sort(),operations.map(o=>o.start).sort());});
const architect='docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-07_hq_helper_lifetime_audit.md';
const architectPresent=fs.existsSync(path.join(root,architect));if(architectPresent)read(architect);
const referenceSections=[
 ['wiki',path.join(root,'paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md'),435,443,'62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4'],
 ['installed', 'C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md',7820,7827,'2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af']
].map(([kind,p,startLine,endLine,requestedRevision])=>({kind,path:p,startLine,endLine,requestedRevision,sha256:hash(fs.readFileSync(p))}));
test('audited input bytes stable through final run',()=>{for(const [f,b]of bytes)assert.equal(hash(fs.readFileSync(path.join(root,f))),hash(b),f);});
const output={status:results.some(r=>r.status==='failed')?'failed':'passed_conservative_helper_frame_model',command:'node docs/testing/2026-10-07_cbrn_hq_lifetime_source_tests.js',timestamp:new Date().toISOString(),architectHandoff:{path:architect,read:architectPresent},baselineManifest:manifest, cases:results.length,results,sourceHashes:Object.fromEntries([...bytes].map(([f,b])=>[f,hash(b)])),referenceSections,limitations:[
 'BaseVM.run lexical frames are retained without modification. Caller-owned temporary writes survive a helper return, newly created helper slots do not. This conservative documented failure mode is not observed HOI4 execution.',
 'Regular maps distinguish one saved character and OWNER country. Temporary storage is unscoped as documented, but retains the existing per-helper cleanup lifetime.',
 'Actual package setters, preparation arithmetic, force-band triggers, nested stock depletion, CP remainder, country ledgers, upkeep completion, receipt effect and eligibility, and planned-end no-posture guard are evaluated from parsed source.',
 'Affordability and command validity are explicit true/false fixture predicates, not full native country/HQ/policy/equipment checks. Army-assigned leader properties and stock counts are fixture inputs.',
 'Equipment native effects update only fixture stocks. Mask snapshot is a no-op, and military filter-condition loss is a narrow requested-loss stub. That mask-loss system is not fully evaluated.',
 'Native command power/fuel/manpower effects and event/meta schedule calls are captured arguments, not native resource, event, or timed-trait execution. Positive half-up integer rounding is the local arithmetic convention.',
 'Achievement commitment and earned-trait refresh are no-op boundaries. Commander receipt flags/counters and the real eligibility body are exercised, but actual trait awards are outside scope.',
 'Actual upkeep event .2 and planned-end event .3 immediate blocks are explicitly invoked under fixed fixture states. Real event timing, cancellation, target identity persistence across saves, or later restoration callbacks are not simulated.',
 'No gameplay, shared VM, index, commit, MCP probability, game launch, or log search was performed by this worker.'
]};
fs.writeFileSync(path.join(__dirname,'2026-10-07_cbrn_hq_lifetime_source_results.json'),JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify({status:output.status,cases:output.cases,failed:results.filter(r=>r.status==='failed'),reproducedBeforeFailures:results.filter(r=>r.baselineFailureReproduced).length},null,2));
if(results.some(r=>r.status==='failed'))process.exitCode=1;
