// Actual bounded consumer fragments with the architect-owned source VM.
// Captured source hashes, not moving Git HEAD, govern preservation checks.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),Module=require('node:module');
const audit=require('./existing_owner_caller_contract_audit.js');
const core=require('./exact_quote_source_tests.js');
const {root,files,sources,defs,parsed,field,sha,canonical,stripAdded}=audit;
const {S,ticks,definitions,constants}=core;
// Reuse the existing native-balance adapter class verbatim. Its scenarios and
// reporting tail are not executed, and its source file is never modified.
const receiptPath=path.join(__dirname,'universal_cost_receipt_lifetime_source_tests.js');
const receiptSource=fs.readFileSync(receiptPath,'utf8');
const cut=receiptSource.indexOf('const keyPrefix =');assert(cut>0);
const loaded=new Module(receiptPath,module);loaded.filename=receiptPath;loaded.paths=module.paths;
loaded._compile(receiptSource.slice(0,cut)+'\nmodule.exports={ReceiptVM};',receiptPath);
const {ReceiptVM}=loaded.exports;
for(const [name,{node}]of defs)definitions.set(name,node.value);
const constFiles=['026_black_friday_constants','007_fury_constants','chaosx_random_faction_constants',
  'cbrn_system_constants','cbrn_occupation_constants','cbrn_doctrine_constants',
  'germany_mengele_constants','condemnation_sanctions_constants'];
for(const name of constFiles){
  const file=path.join(root,`common/script_constants/${name}.txt`);assert(fs.existsSync(file),`missing real tuning source ${file}`);
  const source=fs.readFileSync(file,'utf8');
  for(const category of source.matchAll(/^([a-z_0-9]+) = \{([\s\S]*?)^\}/gm))
    for(const item of category[2].matchAll(/^\s*([a-z_0-9]+) = (-?\d+(?:\.\d{1,5})?)\s*(?:#[^\r\n]*)?$/gm))
      constants.set(`constant:${category[1]}.${item[1]}`,ticks(item[2]));
}
const callContracts=new WeakMap();
for(const r of audit.roots) {
  function walk(nodes){for(const n of nodes){
    const row=audit.inventory.find(x=>x.file===r.file&&x.owner===r.owner&&x.start===n.start);
    if(row)callContracts.set(n,row.required);
    if(Array.isArray(n.value))walk(n.value);
  }}walk(r.nodes);
}
class ConsumerVM extends ReceiptVM {
  eval(nodes){
    for(let i=0;i<nodes.length;i++){
      const n=nodes[i];
      if(definitions.has(n.key)&&!Array.isArray(n.value)){
        const required=callContracts.get(n);
        if(required)for(const name of required)assert(audit.tempArrays.has(name)?this.tempArrays.has(name):this.vars.has(name),`missing consumed caller storage ${name} before ${n.key}`);
        // Public calls require exactly their consumed caller exports. All
        // internal exact/receipt frames keep the core VM's strict contracts.
        const yes=this.run(n.key,Boolean(required));
        if((n.value==='no'&&yes)||(n.value!=='no'&&!yes))return false;
      }else if(n.key==='has_country_flag'){if(!this.flags.has(n.value))return false;}
      else if(n.key==='add_to_variable'){
        const name=field(n.value,'var')||n.value[0].key,value=field(n.value,'value')||n.value[0].value;
        this.write(name,this.value(name)+this.value(value),false);
      }
      else if(n.key==='resize_array'){
        const name=field(n.value,'array')||n.value[0].key,size=this.value(field(n.value,'size')||n.value[0].value);
        assert.equal(size%S,0n);const count=Number(size/S);assert(count>=0);
        const a=this.arrays.get(name)||[],fill=this.value(field(n.value,'value')||'0');
        while(a.length<count)a.push(fill);a.length=count;this.arrays.set(name,a);
      }
      else if(n.key==='round_temp_variable'){
        const name=Array.isArray(n.value)?field(n.value,'var'):n.value,value=this.value(name);
        assert(value>=0n,'bounded cost fixture requires nonnegative rounding input');
        this.write(name,((value+S/2n)/S)*S,true);
      }
      else if(n.key==='clamp_temp_variable'){
        const name=field(n.value,'var'),min=field(n.value,'min'),max=field(n.value,'max');let value=this.value(name);
        if(min!==undefined&&value<this.value(min))value=this.value(min);
        if(max!==undefined&&value>this.value(max))value=this.value(max);
        this.write(name,value,true);
      }else{
        const group=[n];if(n.key==='if')while(nodes[i+1]&&['else','else_if'].includes(nodes[i+1].key))group.push(nodes[++i]);
        if(!super.eval(group))return false;
      }
    }return true;
  }
  run(name,bypass=false){
    try {
      if(name==='black_friday_quote_custom_cost'){
        assert(this.vars.has('black_friday_quote_final_cost'),'central quote caller lacks consumed final');
        return super.run(name,true);
      }
      return super.run(name,bypass);
    } catch(error) { error.message=`${name}: ${error.message}`;throw error; }
  }
}
const scenarios=[],unresolved=[],concurrentSourceChanges=[];
function scenario(id,fn){fn();scenarios.push(id);}
function fixture(active=true,ratio=5000){
  const vm=new ConsumerVM();
  for(const [suffix,v]of [['ids',26],['ratios',ratio],['priorities',500],['eligibility_masks',0]])
    vm.arrays.set(`global.universal_cost_source_${suffix}`,active?[ticks(v)]:[]);
  vm.set('global.universal_cost_custom_quote_cache_valid',1);
  if(active)vm.flags.add('black_friday_active');
  for(const resource of ['pp','cp','fuel','eq:support_equipment_1'])vm.balance(resource,100000);
  for(const model of ['decontamination_equipment_1','decontamination_equipment_2','decontamination_equipment_3'])
    vm.write(`num_equipment@${model}`,ticks(100000),false);
  return vm;
}
const baseline=JSON.parse(fs.readFileSync(path.join(__dirname,'existing_owner_caller_baseline.json'),'utf8'));
scenario('captured-before-preservation-with-explicit-concurrent-source-boundary',()=>{
  for(const file of files){
    const observed=sha(canonical(stripAdded(sources.get(file))));
    if(observed===baseline[file].canonicalSha256)continue;
    assert.equal(file,'common/scripted_effects/germany_mengele_effects.txt',`unexpected non-declaration change ${file}`);
    const commit='e64e95aa3bcb9fcab5a38a248cad28aa78bd2294';
    const before=require('node:child_process').execFileSync('git',['show',commit+':'+file],{cwd:root,encoding:'utf8'});
    const expectedNodes=audit.parse(before),actualNodes=audit.parse(stripAdded(sources.get(file)));
    const owned=audit.changes().filter(x=>x.file===file).map(x=>x.owner);
    const normalized=node=>JSON.stringify(node,(k,v)=>['start','end'].includes(k)?undefined:v);
    for(const name of owned)assert.equal(normalized(actualNodes.find(n=>n.key===name)),normalized(expectedNodes.find(n=>n.key===name)),`owned caller changed beyond declarations ${name}`);
    concurrentSourceChanges.push({file,capturedBeforeSha256:baseline[file].sha256,capturedCanonicalSha256:baseline[file].canonicalSha256,
      observedSourceSha256:sha(sources.get(file)),observedCanonicalSha256:observed,ownedFunctions:owned,
      pinnedCostFunctionBeforeCommit:commit,pinnedSourceSha256:sha(before),
      status:'owned cost function preservation passed, whole-file concurrent changes remain for parent review'});
  }
  assert.equal(audit.gaps.length,0);
});
scenario('regular-ordinary-cost-providers-are-never-shadowed',()=>{
  const forbidden=/communism_counter_agitation_(?:command_power|political_power)_cost|communism_emergency_(?:command_power|manpower|equipment|political_power)_cost|communist_intervention_(?:command_power|manpower|equipment)_cost|cbrn_response_(?:shelter_support|shelter_train)_cost/;
  for(const file of files)for(const group of sources.get(file).matchAll(/# Existing-owner caller output storage\.\r?\n((?:\s*(?:set_temp_variable|resize_temp_array) = \{[^\r\n]*\}\r?\n)+)/g))
    assert(!forbidden.test(group[1]),`normal scoped input shadowed ${file}`);
});
const getterNames=['GetCbrnReconditionPoliticalCost','GetCbrnReconditionSupportCost','GetCbrnConvertPoliticalCost',
  'GetCbrnConvertSupportCost','GetCbrnSimplifyPoliticalCost','GetCbrnSimplifySupportCost',
  'GetCbrnCleanupCommandCost','GetCbrnCleanupEquipmentCost','GetCbrnCleanupFuelCost'];
for(const name of getterNames)scenario(`actual-getter-${name}-cold-warm-normal-sale-evolution-shortage`,()=>{
  const texts=[...parsed].filter(([f])=>f.includes('scripted_localisation')).flatMap(([,nodes])=>nodes)
    .find(n=>n.key==='defined_text'&&field(n.value,'name')===name).value.filter(n=>n.key==='text');
  const ownerRoots=audit.roots.filter(r=>r.owner===name);
  const price=[...ownerRoots[0].out][0];assert(price,`real localisation value lacks observed cost ${name}`);
  const component=name.includes('Support')?'eq:support_equipment_1':name.includes('Command')?'cp':name.includes('Fuel')?'fuel':name.includes('Equipment')?'decon':'pp';
  for(const active of [true,false])for(const ratio of [5000,2500]){
    const vm=fixture(active,ratio);
    for(let repeat=0;repeat<2;repeat++){
      assert.equal(vm.eval(field(texts[0].value,'trigger')),false,'sufficient exact component must use ready row');
      assert(vm.eval(field(texts[1].value,'trigger')));assert(vm.vars.has(price),`price vanished after getter quote ${name}`);
      assert(vm.value(price)>0n,'live positive ordinary cost must remain positive');
    }
    if(component==='decon')for(const model of ['decontamination_equipment_1','decontamination_equipment_2','decontamination_equipment_3'])vm.write(`num_equipment@${model}`,0n,false);
    else vm.balance(component,0);
    assert(vm.eval(field(texts[0].value,'trigger')),'selected component shortage must choose short row');
  }
});
scenario('new-owner-component-array-placeholder-clear-and-append-cold-warm',()=>{
  const owner=defs.get('random_faction_black_friday_pay_stabilize_alignment').node.value;
  let chosen;
  function locate(nodes){for(const n of nodes){if(n.key==='random_faction_black_friday_begin_component_list')chosen=nodes;if(Array.isArray(n.value))locate(n.value);}}locate(owner);assert(chosen);
  const lo=chosen.findIndex(n=>n.key==='resize_temp_array'),hi=chosen.findIndex(n=>n.key==='if');
  assert(lo>=0&&hi>lo);const prepare=chosen.slice(lo,hi),vm=fixture();
  vm.write('random_faction_stabilize_pp_cost',ticks(20),false);vm.write('random_faction_stabilize_support_cost',ticks(10),false);
  for(let repeat=0;repeat<2;repeat++){
    assert(vm.eval(prepare));for(const suffix of ['ids','resource_kinds','family_masks','ordinary_costs'])
      assert.equal(vm.tempArrays.get(`random_faction_black_friday_component_${suffix}`).length,2,'placeholder or stale component survived');
  }
  const bare=fixture();assert(bare.run('random_faction_black_friday_begin_component_list',true));
  assert(!bare.tempArrays.has('random_faction_black_friday_component_ids'));
});
scenario('actual-fury-decision-prefix-retains-single-payment-result-on-ordinary-path',()=>{
  const r=audit.roots.find(r=>r.owner==='fury_select_new_target.complete_effect');assert(r);
  const hidden=r.nodes.find(n=>n.key==='hidden_effect').value;
  const stop=hidden.findIndex(n=>n.key==='if'),prefix=hidden.slice(0,stop);assert(stop>0);
  const vm=fixture(false);vm.balance('cp',100);
  const fee=constants.get('constant:fury_decision_cost.target_cp');assert(fee>0n);
  for(let repeat=0;repeat<2;repeat++){
    assert(vm.eval(prefix));assert.equal(vm.value('black_friday_fury_payment_success'),S);
    assert.equal(vm.resources.get('cp'),ticks(100)-BigInt(repeat+1)*fee);
  }
  assert.equal(vm.nativeWrites.filter(w=>w.key==='cp').length,2,'one debit per unchanged ordinary callback');
});
scenario('missing-display-caller-declaration-negative-control',()=>{
  const r=audit.roots.find(r=>r.owner==='GetCbrnReconditionPoliticalCost');assert(r);
  const vm=fixture();
  assert.throws(()=>vm.eval(r.nodes.filter(n=>n.key!=='set_temp_variable')),/missing consumed caller storage/);
});
scenario('real-liaison-component-quote-pay-record-and-refund-with-caller-storage',()=>{
  const vm=fixture();vm.balance('cp',30);
  for(const [key,value]of Object.entries({ordinary_cost:20,family_mask:2,resource_kind:2,component_id:4,is_primary:1}))
    vm.write(`random_faction_request_liaison_black_friday_${key}`,ticks(value),false);
  assert(vm.run('random_faction_black_friday_quote_request_liaison_component',true));
  assert.equal(vm.value('random_faction_request_liaison_black_friday_quoted_cost'),ticks(10));
  assert.equal(vm.value('random_faction_request_liaison_black_friday_affordable'),S);
  assert(vm.run('random_faction_black_friday_pay_request_liaison_component',true));
  assert.equal(vm.value('random_faction_request_liaison_black_friday_payment_succeeded'),S);
  assert.equal(vm.value('random_faction_request_liaison_black_friday_receipt_succeeded'),S);
  assert.equal(vm.resources.get('cp'),ticks(20));
  assert.deepEqual(vm.arrays.get('universal_cost_component_actual_paid_costs'),[ticks(10)]);
  vm.set('universal_cost_transaction_id',String(vm.value('random_faction_request_liaison_black_friday_transaction_id')/S));
  assert(vm.call('universal_cost_refund_transaction'));assert.equal(vm.resources.get('cp'),ticks(30));
  vm.balance('cp',5);assert(vm.run('random_faction_black_friday_quote_request_liaison_component',true));
  assert.equal(vm.value('random_faction_request_liaison_black_friday_affordable'),0n,'warm shortage quote must clear earlier affordability');
  const writes=vm.nativeWrites.length;assert(vm.run('random_faction_black_friday_pay_request_liaison_component',true));
  assert.equal(vm.value('random_faction_request_liaison_black_friday_payment_succeeded'),0n);
  assert.equal(vm.value('random_faction_request_liaison_black_friday_receipt_succeeded'),0n);
  assert.equal(vm.nativeWrites.length,writes,'unaffordable component must not debit or append a receipt');
});
scenario('dynamic-clone-cost-output-retains-current-route-input',()=>{
  const nodes=defs.get('mengele_clone_army_black_friday_pay_clone_deployment_command_power').node.value;
  const prefix=nodes.slice(0,nodes.findIndex(n=>n.key==='mengele_clone_army_black_friday_pay_command_power'));
  assert(prefix.length>1);
  for(const flag of [null,'mengele_clone_decision_discounted_deployment_unlocked','mengele_clone_decision_streamlined_deployment_unlocked']){
    const vm=fixture();if(flag)vm.flags.add(flag);assert(vm.eval(prefix));
    const key=flag?.includes('streamlined')?'raise_clone_wave_streamlined_command_power':flag?'raise_clone_wave_discount_command_power':'raise_clone_wave_command_power';
    assert.equal(vm.value('mengele_clone_black_friday_ordinary_cost'),constants.get(`constant:mengele_clone_decision.${key}`));
  }
});
scenario('parent-repaired-condemnation-multiplier-survives-nested-provider',()=>{
  for(const score of [-50,0,500,1000,1500]) for(const [action,base] of [['seal_state',40],['destroy_records',60]]) {
    const vm=fixture(false);vm.write('condemnation_total',ticks(score),false);
    vm.set('cbrn_occupation_coverup_pp_quote',0);
    assert(vm.run(`cbrn_occupation_prepare_${action}_pp_quote`,true));
    assert.equal(vm.value('cbrn_occupation_coverup_pp_quote'),ticks(base*(1+Math.max(0,Math.min(1000,score))/500)));
  }
  for(const score of [-50,0,1,500,1000,1500]) {
    const vm=fixture(false);vm.write('condemnation_total',ticks(score),false);
    vm.set('condemnation_unscaled_cost',3).set('condemnation_scaled_cost',0);
    assert(vm.run('condemnation_prepare_scaled_integer_cost',true));
    const clamped=Math.max(0,Math.min(1000,score));
    assert.equal(vm.value('condemnation_scaled_cost'),ticks(Math.ceil(3*(1+clamped/500))));
    vm.set('condemnation_inspection_consumer_goods_increment_temp',0).set('condemnation_inspection_consumer_goods_total',0);
    assert(vm.run('condemnation_prepare_inspection_consumer_goods',true));
    assert.equal(vm.value('condemnation_inspection_consumer_goods_total'),ticks((0.05+clamped*0.0001).toFixed(5)));
  }
});
const protectedSourceChanges=audit.readOnlyFiles.filter(f=>baseline[f]&&sha(sources.get(f))!==baseline[f].sha256);
console.log(JSON.stringify({scenarioCount:scenarios.length,scenarios,knownCostCalls:audit.inventory.length,
  unresolved,concurrentSourceChanges,protectedSourceChanges,sourceHashes:Object.fromEntries([...sources].map(([f,s])=>[f,sha(s)])),
  sourceVMHashes:{exact:sha(fs.readFileSync(path.join(__dirname,'exact_quote_source_tests.js'),'utf8')),receipt:sha(receiptSource)},
  limits:'Only selected actual consumer fragments executed, native balances, clamp, regular increments and regular array resize modeled. Full owner scopes, callbacks, native engine, display renders and achievement acceptance remain unproven.'},null,2));
