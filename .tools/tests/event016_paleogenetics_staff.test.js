// CommonJS actual-source staff fixture; run with node from repo root.
// Reuses the shared fixed-point/lifetime interpreter; financial APIs are never stubbed.
const fs=require('node:fs'), path=require('node:path'), assert=require('node:assert/strict'), crypto=require('node:crypto');
const root=path.resolve(__dirname,'../..');
const core=require(path.join(__dirname,'lib','universal_cost_source_model.js'));
const {VM,S,ticks,parse,definitions,constants,helperOutputs,callerOutputs}=core;
const P='mengele_event016_paleogenetics_staff_', H='brilliant_scientist_mengele_paleogenetics_staff_';
const paired='brilliant_scientist_mengele_paleogenetics_';
const sources=new Map(core.sources), kinds=new Map();
const files=[
'common/script_constants/016_mengele_paleogenetics_staff_constants.txt',
'common/script_constants/016_brilliant_scientist_constants.txt',
'common/script_constants/026_black_friday_constants.txt',
'common/scripted_effects/016_mengele_paleogenetics_staff_effects.txt',
'common/scripted_triggers/016_mengele_paleogenetics_staff_triggers.txt',
'common/scripted_triggers/chaosx_universal_cost_triggers.txt',
'common/scripted_effects/026_black_friday_effects.txt'];
for(const f of files){
 const raw=fs.readFileSync(path.join(root,f),'utf8');sources.set(f,raw);
 if(f.includes('/script_constants/'))for(const cat of parse(raw))if(Array.isArray(cat.value))for(const n of cat.value)
  if(!Array.isArray(n.value)&&/^-?\d/.test(n.value))constants.set('constant:'+cat.key+'.'+n.key,ticks(n.value));
 else {}
 if(!f.includes('/script_constants/'))for(const n of parse(raw)){
  if(f.endsWith('026_black_friday_effects.txt')&&n.key!=='black_friday_allocate_owner_transaction')continue;
  definitions.set(n.key,n.value);kinds.set(n.key,f.includes('/scripted_triggers/')?'trigger':'effect');
 }
}
const outputs={
 universal_cost_pay_component:['universal_cost_payment_result'],
 universal_cost_credit_component:['universal_cost_credit_result'],
 universal_cost_find_transaction_row:['universal_cost_transaction_found_index','universal_cost_transaction_is_indexed','universal_cost_transaction_lookup_result','universal_cost_transaction_pointer'],
 universal_cost_find_component_row:['universal_cost_component_found_index','universal_cost_component_lookup_result'],
 universal_cost_record_transaction:['universal_cost_record_transaction_result','universal_cost_recorded_component_index'],
 universal_cost_settle_transaction:['universal_cost_settle_transaction_result'],
 universal_cost_mark_component_refunded:['universal_cost_mark_component_refunded_result'],
 universal_cost_validate_component_chain:['universal_cost_chain_valid'],
 universal_cost_refund_component_at_cursor:['universal_cost_refund_total','universal_cost_refund_unhandled_total','universal_cost_refund_all_complete'],
 universal_cost_refund_transaction:['universal_cost_refund_transaction_result','universal_cost_refund_total','universal_cost_refund_unhandled_total']};
for(const [name,vars]of Object.entries(outputs))helperOutputs[name]={vars,arrays:[]};
const stubNames=['brilliant_scientist_mengele_project_stage_provider_is_valid',paired+'deployment_outputs_are_complete',paired+'current_pair_is_valid'];
for(const n of stubNames)definitions.set(n,[]);
class StaffVM extends VM{
 constructor(){
  super();this.actor=7n*S;this.outerRoot=this.actor;this.scope=this.actor;this.prev=this.actor;
  this.provider=true;this.exists=true;this.tech=true;this.pairComplete=true;this.cic=2n*S;
  this.balance=new Map([['crew',1000n*S],['support',1000n*S]]);
  this.states=new Map([[701n*S,{owner:this.actor,control:this.actor,infra:3n*S,civ:0n}],
                      [702n*S,{owner:this.actor,control:this.actor,infra:2n*S,civ:3n*S}]]);
  this.writes=[];this.calls=[];this.factor=new Map();this.onNative=null;this.rejectRecord=false;this.rejectSettle=false;
  this.flags.add('mengele_event016_paleogenetics_deployment_completed');
  this.regularVars.set('mengele_event016_paleogenetics_paid_reserve',701n*S);
  this.regularVars.set('mengele_event016_paleogenetics_paid_hatchery',702n*S);
  this.regularVars.set('mengele_event016_paleogenetics_deployment_serial',S);
  this.regularVars.set('mengele_event016_paleogenetics_reserve_post',3n*S);
  this.regularVars.set('mengele_event016_paleogenetics_hatchery_post',3n*S);
  this.arrays.set('global.universal_cost_source_ids',[]);
  this.arrays.set('global.universal_cost_source_ratios',[]);
  this.arrays.set('global.universal_cost_source_priorities',[]);
  this.arrays.set('global.universal_cost_source_eligibility_masks',[]);
  this.regularVars.set('global.universal_cost_custom_quote_cache_valid',S);
  this.seed();
 }
 seed(marker=1){
  this.vars.set('paleo_staff_native_entry',ticks(marker));
  for(const n of ['begin','finish','cancel','demobilize','cleanup','recovery','ack'])this.vars.set('paleo_staff_'+n+'_result',0n);
  for(const n of ['support','source','source_count','valid'])this.vars.set('paleo_staff_quote_'+n,0n);
  this.vars.set('paleo_staff_owner_family',constants.get('constant:universal_cost_family.personnel'));
  this.vars.set('paleo_staff_owner_primary_component',constants.get('constant:black_friday_event.owner_component_support_equipment'));
  this.vars.set('paleo_staff_owner_cost_basis',constants.get('constant:universal_cost_achievement_basis.primary_component'));
  this.vars.set('paleo_staff_owner_primary_member',S);
  return this;
 }
 source(ratio='5000',mask=32,id=26){
  this.arrays.set('global.universal_cost_source_ids',[ticks(id)]);
  this.arrays.set('global.universal_cost_source_ratios',[ticks(ratio)]);
  this.arrays.set('global.universal_cost_source_priorities',[ticks(500)]);
  this.arrays.set('global.universal_cost_source_eligibility_masks',[ticks(mask)]);
  this.flags.add('black_friday_active');return this;
 }
 regular(n){return this.regularVars.get(P+n)||0n}
 flag(n){return this.flags.has(P+n)}
 value(token){
  if(token==='THIS')return this.scope;if(token==='ROOT')return this.outerRoot;if(token==='PREV')return this.prev;
  if(token.startsWith('PREV.')){assert.equal(this.prev,this.actor);return super.value(token.slice(5))}
  if(token.startsWith('ROOT.')){assert.equal(this.outerRoot,this.actor);return super.value(token.slice(5))}
  if(token==='manpower_k')return this.balance.get('crew')/1000n;
  if(token==='num_equipment@support_equipment_1')return this.balance.get('support');
  if(token==='num_of_civilian_factories_available_for_projects')return this.cic;
  if(token.startsWith('non_damaged_building_level@')){
   const state=this.states.get(this.scope);assert(state,'state reader requires STATE');
   return token.endsWith('@infrastructure')?state.infra:state.civ;
  }
  return super.value(token);
 }
 run(name,bare=false){
  this.calls.push(name);
  if(name===stubNames[0])return this.exists&&this.provider;
  if(name===stubNames[1])return this.pairComplete;
  if(name===stubNames[2])return [...this.states.values()].every(s=>s.owner===this.actor&&s.control===this.actor);
  if(name==='universal_cost_record_transaction'&&this.rejectRecord){
   this.regularVars.set(this.key('universal_cost_allocated_transaction_id_@var:universal_cost_transaction_id'),0n);
  }
  if(name==='universal_cost_settle_transaction'&&this.rejectSettle){
   const row=Number(this.value('universal_cost_transaction_row_plus_one_@var:universal_cost_transaction_id')/S)-1;
   if(row>=0)this.arrays.get('universal_cost_transaction_states')[row]=0n;
  }
  return super.run(name,bare);
 }
 eval(nodes){
  for(let i=0;i<nodes.length;i++){
   const node=nodes[i],{key:k,value:v,op}=node;
   if(k==='has_country_flag'){if(!this.flags.has(v))return false}
   else if(k==='set_country_flag'){assert.equal(typeof v,'string');this.flags.add(v)}
   else if(k==='clr_country_flag'){this.flags.delete(v)}
   else if(k==='has_variable'){if(!this.vars.has(v)&&!this.regularVars.has(this.key(v)))return false}
   else if(['add_to_variable','subtract_from_variable','multiply_variable','divide_variable','modulo_variable'].includes(k)){
    const long=this.field(v,'var'),name=long||v[0].key,b=this.value(long?this.field(v,'value'):v[0].value),a=this.value(name);
    let n=k==='add_to_variable'?a+b:k==='subtract_from_variable'?a-b:k==='multiply_variable'?a*b/S:k==='divide_variable'?a*S/b:a%b;
    this.write(name,n,false);
   }
   else if(k.startsWith('var:')){
    const target=this.value(k.slice(4)),old=this.scope,prev=this.prev;
    if(!this.states.has(target))return false;
    this.scope=target;this.prev=old;
    try{if(!this.eval(v))return false}finally{this.scope=old;this.prev=prev}
   }else if(k==='is_owned_by'||k==='is_controlled_by'){
    const state=this.states.get(this.scope);if(!state||state[k==='is_owned_by'?'owner':'control']!==this.value(v))return false;
   }else if(k==='exists'){if(this.exists!==(v==='yes'))return false}
   else if(k==='has_tech'){if(!this.tech)return false}
   else if(k==='has_manpower'||k==='has_equipment'||k==='num_of_civilian_factories_available_for_projects'){
    const cmp=k==='has_equipment'?v[0]:node;
    if(k==='has_equipment')assert.equal(cmp.key,'support_equipment_1');
    const a=k==='has_manpower'?this.balance.get('crew'):k==='has_equipment'?this.balance.get('support'):this.cic,b=this.value(cmp.value);
    if(!(cmp.op==='<'?a<b:cmp.op==='>'?a>b:a===b))return false;
   }else if(k==='add_manpower'||k==='add_equipment_to_stockpile'){
    const role=k==='add_manpower'?'crew':'support';if(k!=='add_manpower')assert.equal(this.field(v,'type'),'support_equipment_1');
    const requested=this.value(k==='add_manpower'?v:this.field(v,'amount'));
    const direction=requested<0n?'debit':'credit',f=this.factor.get(role+'_'+direction)??S;
    const actual=requested*f/S;this.balance.set(role,this.balance.get(role)+actual);
    this.writes.push({role,direction,requested:String(requested),actual:String(actual)});
    if(this.onNative)this.onNative(this,{role,direction,requested,actual});
   }else{
    const group=[node];if(k==='if')while(nodes[i+1]&&['else_if','else'].includes(nodes[i+1].key))group.push(nodes[++i]);
    if(!super.eval(group))return false;
   }
  }
  return true;
 }
 quote(){this.run(H+'quote');return this.value('paleo_staff_quote_support')}
 begin(){this.seed();this.run(H+'begin_training');return this.value('paleo_staff_begin_result')}
 finish(){this.run(H+'finish_training');return this.value('paleo_staff_finish_result')}
 release(){this.run(H+'demobilize');return this.value('paleo_staff_demobilize_result')}
 recover(){this.run(H+'recover_release');return this.value('paleo_staff_recovery_result')}
 qualified(){return this.run(H+'is_qualified')}
 ack(role,amount,options={}){
  this.vars.set('paleo_staff_ack_verified',options.verified??S);
  this.vars.set('paleo_staff_ack_actor',options.actor??this.actor);
  this.vars.set('paleo_staff_ack_serial',options.serial??this.regular('receipt_serial'));
  this.vars.set('paleo_staff_ack_nonce',options.nonce??(role==='debit'?this.regular('receipt_serial'):this.regular(role+'_credit_nonce')));
  this.vars.set('paleo_staff_ack_amount',ticks(amount));
  if(role==='debit')this.vars.set('paleo_staff_ack_resource_kind',options.kind??this.regular('unverified_debit_kind'));
  this.run(H+'acknowledge_'+(role==='debit'?'debit':role+'_credit'));
  return this.value('paleo_staff_ack_result');
 }
}
const results={cases:[],sourceHashes:{},stubs:stubNames,limits:[
 'native personnel and stockpile effects/reads are narrow synchronous primitive fixtures',
 'fixed-point helper lifetimes modeled conservatively; no engine callback/reservation/save proof',
 'zero/negative/oversized credit requires externally verified positive matching acknowledgment',
 'no model/design/producer restoration claim; no AI/GUI or full Event016 acceptance']};
function test(n,f){if(require.main!==module)return;f();results.cases.push(n);console.log('PASS '+n)}
function started(v=new StaffVM()){assert.equal(v.begin(),S);assert(v.flag('funded'));assert.equal(v.regular('crew_held'),250n*S);return v}
function trained(v=started()){assert.equal(v.finish(),S);assert(v.qualified());return v}
function count(v,role,direction){return v.writes.filter(w=>w.role===role&&w.direction===direction).length}
test('nominal shared fee and actual 250 staff then demobilization once',()=>{
 const v=trained();assert.equal(v.balance.get('support'),900n*S);assert.equal(v.balance.get('crew'),750n*S);
 assert.equal(v.regular('handlers'),100n*S);assert.equal(v.regular('veterinary_staff'),150n*S);
 assert.equal(v.release(),S);assert.equal(v.balance.get('crew'),1000n*S);assert.equal(v.balance.get('support'),900n*S);assert(!v.qualified());
 v.release();v.recover();v.run(H+'cleanup');assert.equal(count(v,'crew','credit'),1);
 assert(v.flag('training_completed'));assert(v.flag('closed'));assert.equal(v.regular('crew_held'),0n);
});
test('retraining after acknowledged demobilization uses new owner transaction',()=>{
 const v=trained(),tx=v.regular('transaction');v.release();v.begin();assert(v.regular('transaction')>tx);assert.equal(v.balance.get('support'),800n*S);assert.equal(v.balance.get('crew'),750n*S)
});
test('source50/25 quote changes support only; workforce/CIC stay250/2',()=>{
 for(const ratio of ['5000','2500']){const v=new StaffVM().source(ratio),price=ratio==='5000'?50n*S:25n*S;assert.equal(v.quote(),price);started(v);assert.equal(v.balance.get('support'),1000n*S-price);assert.equal(v.balance.get('crew'),750n*S);assert.equal(v.cic,2n*S)}
});
test('wrong resource mask does not discount support',()=>{const v=new StaffVM().source('2500',64);assert.equal(v.quote(),100n*S)});
test('fresh pure quote and paid expiry use different live prices safely',()=>{
 const v=started(new StaffVM().source('5000'));v.call('universal_cost_source_clear_black_friday');assert.equal(v.quote(),100n*S);assert.equal(v.finish(),S);assert.equal(v.regular('support_actual'),50n*S)
});
for(const sale of [false,true])for(const d of [-1,0,1])test('support exact inclusive '+sale+'/'+d,()=>{
 const v=new StaffVM();if(sale)v.source('5000');const p=sale?50:100;v.balance.set('support',ticks(p+d));
 const r=v.begin();assert.equal(r,d<0?0n:S);if(d<0)assert.equal(v.writes.length,0);
});
for(const d of [-1,0,1])test('reserve people units below/exact/above '+d,()=>{
 const v=new StaffVM();v.balance.set('crew',ticks(250+d));assert.equal(v.begin(),d<0?0n:S);if(d<0)assert.equal(v.writes.length,0)
});
test('full2CIC selection vs admitted0CIC entry',()=>{
 const v=new StaffVM();v.cic=S;assert(!v.run(H+'can_start'));v.cic=2n*S;assert(v.run(H+'can_start'));v.cic=0n;assert.equal(v.begin(),S);
});
test('bare/missing owner descriptor refusal consumes admission marker',()=>{
 const v=new StaffVM();v.vars.set('paleo_staff_native_entry',0n);v.run(H+'begin_training');assert.equal(v.writes.length,0);
 v.seed();v.vars.set('paleo_staff_owner_primary_member',0n);v.run(H+'begin_training');assert.equal(v.writes.length,0);assert.equal(v.value('paleo_staff_native_entry'),0n);
});
test('wrong logical role refuses without borrowing fee/resource family',()=>{
 const v=new StaffVM();v.vars.set('paleo_staff_owner_family',constants.get('constant:universal_cost_family.equipment'));v.run(H+'begin_training');assert.equal(v.writes.length,0);
});
test('duplicate entry freezes actor/sites/prices and consumes stale marker',()=>{
 const v=started(),before=new Map(v.regularVars),writes=v.writes.length;v.begin();assert.deepEqual(v.regularVars,before);assert.equal(v.writes.length,writes);assert.equal(v.value('paleo_staff_native_entry'),0n);
});
test('authority published before native writes and nested cancel cannot reenter',()=>{
 const v=new StaffVM();v.onNative=(x,n)=>{if(n.direction==='debit'){assert(x.flag('receipt_open')&&x.flag('busy'));assert.equal(x.regular('actor'),x.actor);assert.equal(x.regular('receipt_serial'),S);const t=new Map(x.vars);x.run(H+'cancel_training');x.run(H+'finish_training');x.vars=t;}};
 started(v);assert.equal(v.writes.length,2);
});
for(const kind of ['provider','tech','pair','reserve_damage','hatchery_damage','control','missing_scope'])test('qualification suspends '+kind,()=>{
 const v=trained();if(kind==='provider')v.provider=false;if(kind==='tech')v.tech=false;if(kind==='pair')v.pairComplete=false;
 if(kind==='reserve_damage')v.states.get(701n*S).infra=2n*S;if(kind==='hatchery_damage')v.states.get(702n*S).civ=2n*S;
 if(kind==='control')v.states.get(702n*S).control=8n*S;if(kind==='missing_scope')v.states.delete(702n*S);
 assert(!v.qualified());assert.equal(v.balance.get('crew'),750n*S);assert.equal(v.regular('crew_held'),250n*S)
});
test('unchanged neutral tech under cleanup; trained fee remains consumed',()=>{
 const v=trained();v.provider=false;v.run(H+'cleanup');assert.equal(v.balance.get('crew'),1000n*S);assert.equal(v.balance.get('support'),900n*S);assert(v.tech);assert(!v.qualified())
});
test('zero-output training cancel releases fee/personnel once under provider loss',()=>{
 const v=started();v.provider=false;v.run(H+'cancel_training');assert.equal(v.balance.get('crew'),1000n*S);assert.equal(v.balance.get('support'),1000n*S);assert(v.flag('closed'));v.run(H+'cleanup');assert.equal(count(v,'support','credit'),1)
});
test('partial native workforce debit is refundable measured125 not250',()=>{
 const v=new StaffVM();v.factor.set('crew_debit',S/2n);assert.equal(v.begin(),2n*S);assert.equal(v.regular('crew_held'),125n*S);assert.equal(count(v,'support','debit'),0);v.recover();assert.equal(v.balance.get('crew'),1000n*S)
});
test('partial fee debit uses actual measured50 and no invented shared full row',()=>{
 const v=new StaffVM();v.factor.set('support_debit',S/2n);assert.equal(v.begin(),2n*S);assert.equal(v.regular('support_actual'),50n*S);assert(!v.flag('support_recorded'));assert.equal(v.recover(),S);assert.equal(v.balance.get('support'),1000n*S)
});
test('actual shared record rejection preserves debit and compensates exactly',()=>{
 const v=new StaffVM();v.rejectRecord=true;assert.equal(v.begin(),2n*S);assert(v.flag('release_pending'));assert.equal(v.recover(),S);assert.equal(v.balance.get('support'),1000n*S)
});
test('partial crew release retains125 debt then credits only remaining125',()=>{
 const v=trained();v.factor.set('crew_credit',S/2n);assert.equal(v.release(),2n*S);assert.equal(v.regular('crew_held'),125n*S);assert(!v.qualified());v.factor.set('crew_credit',S);assert.equal(v.recover(),S);assert.equal(v.balance.get('crew'),1000n*S);assert.equal(count(v,'crew','credit'),2)
});
test('partial support refund acknowledgment never blindly invokes full shared refund',()=>{
 const v=started();v.factor.set('support_credit',S/2n);v.run(H+'cancel_training');assert.equal(v.regular('support_due'),50n*S);assert.equal(v.balance.get('support'),950n*S);
 v.factor.set('support_credit',S);v.recover();assert.equal(v.balance.get('support'),1000n*S);assert.equal(count(v,'support','credit'),2);assert(v.flag('closed'));
});
test('zero credit quarantines and matching positive delayed acknowledgment permits only remainder',()=>{
 const v=trained();v.factor.set('crew_credit',0n);v.release();assert(v.flag('crew_credit_inflight'));const writes=v.writes.length;v.recover();assert.equal(v.writes.length,writes);
 v.balance.set('crew',v.balance.get('crew')+125n*S);assert.equal(v.ack('crew',125),S);assert.equal(v.regular('crew_held'),125n*S);
 v.factor.set('crew_credit',S);v.recover();assert.equal(v.balance.get('crew'),1000n*S);
});
for(const defect of ['actor','serial','nonce','zero','over','unverified'])test('delayed credit acknowledgment rejects '+defect,()=>{
 const v=trained();v.factor.set('crew_credit',0n);v.release();const opts={};let amt=250;
 if(defect==='actor')opts.actor=8n*S;if(defect==='serial')opts.serial=2n*S;if(defect==='nonce')opts.nonce=2n*S;
 if(defect==='zero')amt=0;if(defect==='over')amt=251;if(defect==='unverified')opts.verified=0n;
 assert.equal(v.ack('crew',amt,opts),3n*S);assert.equal(v.regular('crew_held'),250n*S);assert.equal(v.value('paleo_staff_ack_verified'),0n)
});
test('zero debit is retained until matching positive original-debit acknowledgment',()=>{
 const v=new StaffVM();v.factor.set('crew_debit',0n);v.begin();assert(v.flag('debit_unverified'));assert(!v.run(H+'can_recover_release'));const writes=v.writes.length;v.recover();assert.equal(v.writes.length,writes);
 v.balance.set('crew',v.balance.get('crew')-250n*S);assert.equal(v.ack('debit',250),S);v.factor.set('crew_credit',S);v.recover();assert.equal(v.balance.get('crew'),1000n*S)
});
test('country destruction/foreign actor cannot redirect held workforce',()=>{
 const v=trained();v.exists=false;const writes=v.writes.length;v.run(H+'cleanup');assert.equal(v.writes.length,writes);assert(v.flag('receipt_open'));
 v.exists=true;v.actor=8n*S;v.scope=v.actor;v.run(H+'cleanup');assert.equal(v.writes.length,writes)
});
test('unrelated outer ROOT never pays or receives the team',()=>{
 const v=new StaffVM();v.outerRoot=8n*S;trained(started(v));v.release();assert.equal(v.balance.get('crew'),1000n*S)
});
test('expiry never repurchases manpower/support or factories',()=>{
 const v=started();v.balance.set('crew',0n);v.balance.set('support',0n);v.cic=0n;assert.equal(v.finish(),S);assert(v.qualified())
});
test('warm/cold return ownership and internal real shared output contracts',()=>{
 const warm=started();assert.equal(warm.value('paleo_staff_begin_result'),S);assert(warm.helperOutputChecks.get('universal_cost_record_transaction')>0);
 const cold=new StaffVM();cold.vars.delete('paleo_staff_begin_result');cold.run(H+'begin_training',true);assert(!cold.vars.has('paleo_staff_begin_result'));assert(cold.flag('funded'));
});
test('recorded support role tuple matches registered owner descriptor',()=>{
 const v=started(),i=Number(v.regular('record_index')/S),tx=Number(v.value('universal_cost_transaction_row_plus_one_@var:'+P+'transaction')/S)-1;
 assert.equal(v.arrays.get('universal_cost_component_achievement_family_ids')[i],2097152n*S);
 assert.equal(v.arrays.get('universal_cost_component_achievement_primary_members')[i],S);
 assert.equal(v.arrays.get('universal_cost_transaction_achievement_primary_component_ids')[tx],6n*S);
 assert.equal(v.arrays.get('universal_cost_transaction_achievement_cost_bases')[tx],S);
 assert.equal(v.arrays.get('universal_cost_transaction_component_counts')[tx],S);
});
test('corrupted held/owed conservation fails closed without currency writes',()=>{
 for(const field of ['crew_held','support_due','support_actual','crew_allocated']){
  const v=started(),writes=v.writes.length;v.regularVars.set(P+field,v.regular(field)+S);v.run(H+'cleanup');assert.equal(v.writes.length,writes);assert(v.flag('receipt_open'));
 }
});
test('missing/corrupt shared fee row cannot duplicate support credits',()=>{
 const v=started(),i=Number(v.regular('record_index')/S);v.arrays.get('universal_cost_component_transaction_ids')[i]=99n*S;
 v.run(H+'cancel_training');assert.equal(v.balance.get('crew'),1000n*S);assert.equal(count(v,'support','credit'),0);assert(v.flag('receipt_open'));
});
test('shared settle failure retains committed training and permits settlement-only recovery',()=>{
 const v=started();v.rejectSettle=true;assert.equal(v.finish(),2n*S);assert(!v.qualified());assert(v.flag('fee_consumed'));
 const i=Number(v.value('universal_cost_transaction_row_plus_one_@var:'+P+'transaction')/S)-1;
 v.arrays.get('universal_cost_transaction_states')[i]=S;v.rejectSettle=false;const writes=v.writes.length;
 v.run(H+'recover_training');assert(v.qualified());assert.equal(v.writes.length,writes);
});
test('nested cleanup during positive release cannot reopen or credit twice',()=>{
 const v=trained();v.onNative=(x,n)=>{if(n.direction==='credit'){const t=new Map(x.vars);x.run(H+'cleanup');x.run(H+'demobilize');x.run(H+'recover_release');x.vars=t;}};
 assert.equal(v.release(),S);assert.equal(v.balance.get('crew'),1000n*S);assert.equal(count(v,'crew','credit'),1);
});
test('duplicate delayed acknowledgment is consumed and cannot replay currency',()=>{
 const v=trained();v.factor.set('crew_credit',0n);v.release();v.balance.set('crew',1000n*S);assert.equal(v.ack('crew',250),S);
 const writes=v.writes.length;assert.equal(v.ack('crew',250),3n*S);v.recover();assert(v.flag('closed'));assert.equal(v.writes.length,writes);
});
test('support zero credit has independent positive acknowledgment debt',()=>{
 const v=started();v.factor.set('support_credit',0n);v.run(H+'cancel_training');assert(v.flag('support_credit_inflight'));assert.equal(v.regular('support_due'),100n*S);
 v.balance.set('support',1000n*S);assert.equal(v.ack('support',100),S);v.recover();assert(v.flag('closed'));assert.equal(count(v,'support','credit'),1);
});
test('late support-debit acknowledgment refunds actual quantity without new payment',()=>{
 const v=new StaffVM();v.factor.set('support_debit',0n);v.begin();assert(v.flag('debit_unverified'));
 v.balance.set('support',950n*S);assert.equal(v.ack('debit',50),S);const writes=v.writes.length;v.recover();assert(v.flag('closed'));assert.equal(v.balance.get('support'),1000n*S);assert.equal(count(v,'support','debit'),1);
});
test('unregistered/depleted inputs and malformed generation are refusals not paid receipts',()=>{
 for(const serial of [-1,'0.5']){const v=new StaffVM();v.regularVars.set(P+'serial',ticks(serial));v.begin();assert.equal(v.writes.length,0);assert(!v.flag('receipt_open'));}
 const v=new StaffVM();v.arrays.set('global.universal_cost_source_ids',[26n*S]);assert.equal(v.begin(),0n);assert.equal(v.writes.length,0);
});
test('invalid allocator output cannot debit or publish a paid staffing receipt',()=>{
 const v=new StaffVM();v.regularVars.set('black_friday_transaction_sequence',-S);assert.equal(v.begin(),0n);assert.equal(v.writes.length,0);assert(!v.flag('receipt_open'));
});
test('large reserve reads thousands and scales only the bounded personnel delta',()=>{
 const v=new StaffVM();v.balance.set('crew',2500000000n*S);started(v);assert.equal(v.regular('crew_held'),250n*S);v.run(H+'cancel_training');assert.equal(v.balance.get('crew'),2500000000n*S);
});
test('owner helpers have valid effect/trigger call positions',()=>{
 function walk(nodes,kind){for(const n of nodes){if(n.key.startsWith(H)&&kinds.has(n.key))assert.equal(kinds.get(n.key),kind,n.key);
  if(Array.isArray(n.value)){if(n.key==='if'||n.key==='else_if'){for(const c of n.value)walk(c.key==='limit'?c.value:[c],c.key==='limit'?'trigger':kind)}
   else walk(n.value,kind)}}}
 for(const f of files.filter(f=>f.includes('paleogenetics_staff_')&&!f.includes('/script_constants/')))for(const n of parse(sources.get(f)))walk(n.value,f.includes('/scripted_triggers/')?'trigger':'effect')
});
for(const [f,src]of sources)results.sourceHashes[f]=crypto.createHash('sha256').update(src).digest('hex');
results.sourceHashes[path.relative(root,__filename).replaceAll('\\','/')]=crypto.createHash('sha256').update(fs.readFileSync(__filename)).digest('hex');
results.casesPassed=results.cases.length;
if(process.argv.includes('--results')){const out=path.join(root,'.tmp/event016_paleogenetics_staff');fs.mkdirSync(out,{recursive:true});fs.writeFileSync(path.join(out,'core_results.json'),JSON.stringify(results,null,2)+'\n');}
module.exports={StaffVM,definitions,constants,parse,ticks,S,root,P,H,paired,results};
if(require.main===module)console.log(JSON.stringify({casesPassed:results.casesPassed,sourceHashes:results.sourceHashes,stubs:results.stubs,limits:results.limits},null,2));
