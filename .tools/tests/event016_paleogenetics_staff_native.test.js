// Native decision/claim/navigation integration against actual parsed source.
// Native primitives and campaign eligibility remain explicit fixtures.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const base=require('./event016_paleogenetics_staff.test.js');
const {StaffVM,definitions,constants,parse,ticks,S,root,P,H}=base;
const load=f=>fs.readFileSync(path.join(root,f),'utf8');
for(const f of ['common/scripted_effects/026_black_friday_effects.txt','common/scripted_triggers/026_black_friday_triggers.txt'])
 for(const n of parse(load(f)))definitions.set(n.key,n.value);
const actions=new Map();
for(const cat of parse(load('common/decisions/016_mengele_paleogenetics_staff_decisions.txt')))
 if(Array.isArray(cat.value))for(const n of cat.value)actions.set(n.key,n.value);
class NativeVM extends StaffVM{
 constructor(){super();this.ai=false;this.sale=true;this.tag='MCL';this.removals=[];
  for(const k of ['global.black_friday_sale_sequence','black_friday_achievement_active_sale_sequence','black_friday_achievement_indexed_sale_sequence'])this.regularVars.set(k,S);
 }
 run(name,bare=false){
  if(['black_friday_achievement_is_valid_sale','black_friday_achievement_possible_campaign_is_valid','black_friday_is_active'].includes(name))return this.sale;
  return super.run(name,bare);
 }
 eval(nodes){
  for(let i=0;i<nodes.length;i++){
   const n=nodes[i];
   if(n.key==='is_ai'){if(this.ai!==(n.value==='yes'))return false;continue}
   if(n.key==='has_war'){if((this.war||false)!==(n.value==='yes'))return false;continue}
   if(n.key==='tag'){if(this.tag!==n.value)return false;continue}
   if(n.key==='remove_decision'){this.removals.push(n.value);continue}
   if(n.key==='hidden_trigger'||n.key==='hidden_effect'){if(!this.eval(n.value))return false;continue}
   if(n.key==='custom_trigger_tooltip'){if(!this.eval(n.value.filter(x=>x.key!=='tooltip')))return false;continue}
   if(n.key==='custom_effect_tooltip')continue;
   const group=[n];if(n.key==='if')while(nodes[i+1]&&['else_if','else'].includes(nodes[i+1].key))group.push(nodes[++i]);
   if(!super.eval(group))return false;
  }
  return true;
 }
 block(id,key){const n=actions.get(id).find(n=>n.key===key);assert(n,key);return n.value}
 native(id,key){return this.eval(this.block(id,key))}
 train(){this.cic=0n;this.native('mengele_event016_paleogenetics_train_staff','complete_effect');return this.value('paleo_staff_begin_result')}
 finishNative(){this.native('mengele_event016_paleogenetics_train_staff','remove_effect')}
}
const cases=[];function test(name,fn){fn();cases.push(name)}
test('native full quote and already-reserved callback agree',()=>{
 const v=new NativeVM();assert(v.run(H+'native_start_is_available'));assert.equal(v.train(),S);
 assert.equal(v.regular('crew_held'),ticks(250));v.finishNative();assert(v.qualified());
 assert(!v.run(H+'can_recover_training'));
});
test('real Personnel claim records, confirms and remains after consumed-fee release',()=>{
 const v=new NativeVM().source();v.train();const tx=v.regular('transaction');
 assert.deepEqual(v.arrays.get('black_friday_achievement_transaction_ids'),[tx]);
 assert.deepEqual(v.arrays.get('black_friday_achievement_transaction_family_ids'),[constants.get('constant:universal_cost_family.personnel')]);
 v.finishNative();assert(v.qualified());
 assert.equal(v.arrays.get('black_friday_achievement_transaction_states')[0],constants.get('constant:black_friday_event.achievement_transaction_committed'));
 v.run(H+'demobilize_native');assert.equal(v.balance.get('crew'),ticks(1000));assert.equal(v.balance.get('support'),ticks(950));
 assert.equal(v.arrays.get('black_friday_achievement_transaction_states')[0],constants.get('constant:black_friday_event.achievement_transaction_committed'));
 assert(v.removals.includes('mengele_event016_paleogenetics_train_staff'));
});
test('cancellation withdraws pending claim and restores actual fee and workforce once',()=>{
 const v=new NativeVM().source();v.train();v.run(H+'cancel_native');
 assert.equal(v.balance.get('crew'),ticks(1000));assert.equal(v.balance.get('support'),ticks(1000));
 assert.equal(v.arrays.get('black_friday_achievement_transaction_states')[0],constants.get('constant:black_friday_event.achievement_transaction_refunded'));
 const writes=v.writes.length;v.run(H+'cancel_native');assert.equal(v.writes.length,writes);
});
test('programme-loss cleanup retires native timer and preserves owed release',()=>{
 const v=new NativeVM();v.train();v.provider=false;v.factor.set('crew_credit',S/2n);v.run(H+'cleanup_native');
 assert(v.flag('release_pending'));assert.equal(v.regular('crew_held'),ticks(125));
 assert(v.run(H+'identity_is_visible'));assert(v.run('brilliant_scientist_mengele_paleogenetics_operations_can_open'));
 assert(v.removals.includes('mengele_event016_paleogenetics_train_staff'));
 v.factor.set('crew_credit',S);v.run(H+'recover_release');assert(v.flag('closed'));assert.equal(v.balance.get('crew'),ticks(1000));
});
test('human navigation is presentation-only and AI keeps both row contexts',()=>{
 const v=new NativeVM();const before=v.balance.get('crew');
 v.native('mengele_event016_paleogenetics_open_operations','complete_effect');
 assert(!v.run('brilliant_scientist_mengele_biological_program_rows_are_visible'));
 assert(v.run('brilliant_scientist_mengele_paleogenetics_operations_rows_are_visible'));
 v.ai=true;assert(v.run('brilliant_scientist_mengele_biological_program_rows_are_visible'));assert(v.run('brilliant_scientist_mengele_paleogenetics_operations_rows_are_visible'));
 v.ai=false;v.native('mengele_event016_paleogenetics_close_operations','complete_effect');
 assert(v.run('brilliant_scientist_mengele_biological_program_rows_are_visible'));assert.equal(v.balance.get('crew'),before);
});
test('completed training exposes no settlement recovery row',()=>{
 const v=new NativeVM();v.train();v.finishNative();v.flags.add('mengele_event016_paleogenetics_operations_view');
 assert(!v.native('mengele_event016_paleogenetics_complete_staff_training','visible'));
 const writes=v.writes.length;v.run(H+'recover_training');assert.equal(v.writes.length,writes);
});
test('ordinary non-sale training does not create an achievement claim',()=>{
 const v=new NativeVM();v.sale=false;v.train();v.finishNative();assert(v.qualified());
 assert.equal((v.arrays.get('black_friday_achievement_transaction_ids')||[]).length,0);
});
test('sale expiry keeps the paid fee and obeys ordinary delayed-credit policy',()=>{
 const v=new NativeVM().source();v.train();v.sale=false;v.finishNative();assert(v.qualified());
 assert.equal(v.arrays.get('black_friday_achievement_transaction_states')[0],constants.get('constant:black_friday_event.achievement_transaction_pending'));
 assert.equal(v.balance.get('support'),ticks(950));
});
for(const rate of ['5000','2500'])for(const delta of [-1,0,1])test('native fee boundary '+rate+'/'+delta,()=>{
 const v=new NativeVM().source(rate);const fee=rate==='5000'?50:25;v.balance.set('support',ticks(fee+delta));v.balance.set('crew',ticks(250));
 assert.equal(v.run(H+'native_start_is_available'),delta>=0);
});
test('actual source observer leaves production allocations and currency untouched',()=>{
 const v=new NativeVM();v.train();v.finishNative();v.tag='CXT';v.flags.add('chaosx_test_country_initialized');
 const held=v.regular('crew_held'),fee=v.regular('support_actual'),writes=v.writes.length;
 v.run('chaosx_cxt_event016_probe_paleogenetics_staff');
 assert(v.flags.has('chaosx_cxt_event016_staff_qualified'));assert.equal(v.regular('crew_held'),held);assert.equal(v.regular('support_actual'),fee);assert.equal(v.writes.length,writes);
});
test('CXT carrier application is inert and idempotent',()=>{
 const v=new NativeVM();v.tag='CXT';v.flags.add('chaosx_test_country_initialized');const writes=v.writes.length;
 v.run('chaosx_cxt_extension_event016_paleogenetics_staff_apply');v.run('chaosx_cxt_extension_event016_paleogenetics_staff_apply');
 assert(v.flags.has('paleo_staff_cxt_fixture_ready'));assert.equal(v.writes.length,writes);assert(!v.flag('receipt_open'));
});
test('zero-debt completion cannot bypass an unresolved credit attempt',()=>{
 const v=new NativeVM();v.train();v.finishNative();v.run(H+'demobilize_native');
 v.flags.add(P+'receipt_open');v.flags.add(P+'release_pending');v.flags.add(P+'crew_credit_inflight');
 assert(v.run(H+'receipt_is_current'));assert(!v.run(H+'can_recover_release'));
 const writes=v.writes.length;v.run(H+'recover_release');assert.equal(v.writes.length,writes);
});
const result={casesPassed:cases.length,cases,limits:['Native reserve/stockpile/callback primitives modeled','Campaign/sale eligibility predicates modeled; actual achievement proof/record/confirm/retract execute','No native UI or engine observations']};
if(require.main===module){const out=path.join(root,'.tmp/event016_paleogenetics_staff');fs.mkdirSync(out,{recursive:true});fs.writeFileSync(path.join(out,'native_results.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result,null,2));}
module.exports={NativeVM,actions,result};
