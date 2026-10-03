// EC-A02: real public achievement record -> scanner/receipt lookup -> family credit.
// No receipt, scanner, public record, confirmation, or credit helper is mocked.
// Native country eligibility/classification, resource queries/writes and final
// engine award delivery are modeled; flag/progress effects execute real source.
const fs = require('node:fs'), path = require('node:path'), assert = require('node:assert/strict'), crypto = require('node:crypto');
const core = require('./exact_quote_source_tests.js');
const {VM, S, ticks, parse, root, definitions, constants, callerOutputs, helperOutputs} = core;
const read = p => fs.readFileSync(path.join(root,p),'utf8');
const paths = ['common/scripted_effects/026_black_friday_effects.txt','common/scripted_triggers/026_black_friday_triggers.txt',
  'common/scripted_triggers/chaosx_universal_cost_triggers.txt','common/script_constants/026_black_friday_constants.txt'];
const sources = Object.fromEntries(paths.map(p=>[p,read(p)]));
// Read-only owner coverage. Extract only named definitions so unrelated Germany
// unit-string syntax is neither rewritten nor interpreted by this bounded VM.
const externalPaths=['common/scripted_effects/017_random_faction_effects.txt','common/scripted_effects/germany_mengele_effects.txt'];
for(const p of [...externalPaths,'common/script_constants/chaosx_random_faction_constants.txt'])sources[p]=read(p);
const externalBodies=new Map();
function ownerBody(p,name){const match=sources[p].match(new RegExp(`^${name} = \\{[\\s\\S]*?^\\}`,'m'));assert(match,`missing owner ${name}`);const body=parse(match[0])[0].value;externalBodies.set(name,body);return body;}
function boundaryFragment(body,call){const hits=[];function walk(nodes,scope=[]){for(let i=0;i<nodes.length;i++){const n=nodes[i];if(n.key===call){let start=i-1;while(start>=0&&!(nodes[start].key==='set_temp_variable'&&nodes[start].value[0].key===(call==='universal_cost_record_transaction'?'universal_cost_transaction_id':'black_friday_purchase_transaction_id')))start--;assert(start>=0);let end=i+1;if(call==='universal_cost_record_transaction'&&nodes[end]?.key==='if'){end++;while(['else','else_if'].includes(nodes[end]?.key))end++;}hits.push({nodes:nodes.slice(start,end),scope});}if(Array.isArray(n.value))walk(n.value,[...scope,n.key]);}}walk(body);assert.equal(hits.length,1,`unique ${call} boundary`);return hits[0];}
const externalFragments=new Map();
for(const [p,name] of [[externalPaths[0],'random_faction_black_friday_pay_component_list'],[externalPaths[0],'random_faction_black_friday_pay_request_liaison_component'],[externalPaths[1],'mengele_clone_army_black_friday_pay_command_power']]){
  const body=ownerBody(p,name),record=boundaryFragment(body,'universal_cost_record_transaction');
  definitions.set(`ec02_test_${name}_record`,record.nodes);externalFragments.set(name,{path:p,record});
  if(name!=='random_faction_black_friday_pay_request_liaison_component'){const claim=boundaryFragment(body,'black_friday_record_achievement_transaction');definitions.set(`ec02_test_${name}_claim`,claim.nodes);externalFragments.get(name).claim=claim;}
}
const liaisonClaim=boundaryFragment(ownerBody(externalPaths[0],'random_faction_black_friday_pay_request_liaison'),'black_friday_record_achievement_transaction');
assert(!liaisonClaim.scope.includes('FROM'),'liaison public credit must remain requester-only');
definitions.set('ec02_test_liaison_root_claim',liaisonClaim.nodes);
for(const match of sources[externalPaths[0]].matchAll(/^(@[a-z0-9_]+) = (\d+)$/gm))constants.set(match[1],ticks(match[2]));
for(const cat of parse(sources['common/script_constants/chaosx_random_faction_constants.txt']))if(Array.isArray(cat.value))for(const n of cat.value)if(!Array.isArray(n.value)&&/^-?\d+(\.\d+)?$/.test(n.value))constants.set(`constant:${cat.key}.${n.key}`,ticks(n.value));
for(const p of paths.filter(p=>!p.includes('script_constants'))) for(const n of parse(sources[p])) definitions.set(n.key,n.value);
for(const cat of parse(sources[paths[3]])) if(Array.isArray(cat.value)) for(const n of cat.value)
  if(!Array.isArray(n.value)&&/^-?\d+(\.\d+)?$/.test(n.value)) constants.set(`constant:${cat.key}.${n.key}`,ticks(n.value));
const out = {
  // These owner fragments consume only record_result. The unused exported index
  // is allowed to die at helper return, never injected into owner source.
  universal_cost_record_transaction:['universal_cost_record_transaction_result'],
  universal_cost_find_transaction_row:['universal_cost_transaction_found_index','universal_cost_transaction_lookup_result','universal_cost_transaction_is_indexed','universal_cost_transaction_pointer'],
  universal_cost_find_component_row:['universal_cost_component_found_index','universal_cost_component_lookup_result'],
  universal_cost_settle_transaction:['universal_cost_settle_transaction_result'],
  universal_cost_refund_transaction:['universal_cost_refund_transaction_result','universal_cost_refund_total','universal_cost_refund_unhandled_total'],
  universal_cost_refund_component_at_cursor:['universal_cost_refund_total','universal_cost_refund_unhandled_total','universal_cost_refund_all_complete'],
  universal_cost_credit_component:['universal_cost_credit_result'],
  universal_cost_validate_component_chain:['universal_cost_chain_valid'],
  black_friday_scan_receipt_non_political_payment:['black_friday_purchase_receipt_proof_valid','black_friday_purchase_has_non_political_paid_component'],
  black_friday_scan_receipt_political_power_only:['black_friday_purchase_receipt_proof_valid','black_friday_purchase_has_non_political_paid_component'],
  black_friday_validate_ordinary_receipt_proof:['black_friday_purchase_receipt_proof_valid','black_friday_purchase_has_non_political_paid_component'],
  black_friday_find_achievement_transaction:['black_friday_achievement_transaction_index','black_friday_achievement_lookup_result','black_friday_achievement_row_pointer'],
};
for(const [n,vars] of Object.entries(out)){callerOutputs[n]={vars,arrays:[]};helperOutputs[n]={vars,arrays:[]};}
const nativeEffects={add_political_power:'pp',add_command_power:'cp',add_manpower:'mp',add_fuel:'fuel',army_experience:'army_xp',navy_experience:'navy_xp',air_experience:'air_xp',add_stability:'stability',add_war_support:'war_support'};
const all=[];
class ProofVM extends VM {
  constructor(){super();this.countryFlags=new Set();this.targets=new Set();this.tag='GER';this.ai=false;this.debug=false;this.special=false;this.credits=[];this.wallet=new Map();all.push(this);}
  run(n,...args){if(n==='is_special_chaos_country')return this.special;
    if(n==='black_friday_credit_achievement_family')this.credits.push({family:String(this.value('black_friday_purchase_family_id')/S),ordinary:String(this.value('black_friday_purchase_ordinary_cost')),paid:String(this.value('black_friday_purchase_actual_paid_cost')),nonPP:String(this.value('black_friday_purchase_has_non_political_paid_component')/S)});
    return super.run(n,...args);}
  eval(nodes){for(let i=0;i<nodes.length;i++){const n=nodes[i],k=n.key,v=n.value;
    if(k==='exists'){if(v!=='yes')return false;}
    else if(k==='is_ai'){if(this.ai!==(v==='yes'))return false;}
    else if(k==='is_debug'){if(this.debug!==(v==='yes'))return false;}
    else if(k==='is_special_chaos_country'){if(this.special!==(v==='yes'))return false;}
    else if(k==='original_tag'){if(this.tag!==v)return false;}
    else if(k==='has_country_flag'){if(!this.countryFlags.has(v))return false;}
    else if(k==='set_country_flag')this.countryFlags.add(v);
    else if(k==='clr_country_flag')this.countryFlags.delete(v);
    else if(k==='has_event_target'){if(!this.targets.has(v))return false;}
    else if(k==='is_in_array'&&this.field(v,'array')===undefined){if(!this.array(v[0].key).includes(this.value(v[0].value)))return false;}
    else if(k==='add_to_variable'||k==='subtract_from_variable'){
      const key=this.key(this.field(v,'var',v[0].key)),delta=this.value(this.field(v,'value',v[0].value));
      this.write(key,(this.regularVars.get(key)||0n)+(k==='add_to_variable'?delta:-delta),false);
    } else if(nativeEffects[k])this.wallet.set(nativeEffects[k],(this.wallet.get(nativeEffects[k])||0n)+this.value(v));
    else if(k==='add_equipment_to_stockpile'){const key=this.field(v,'type');this.wallet.set(key,(this.wallet.get(key)||0n)+this.value(this.field(v,'amount')));}
    else {const group=[n];if(k==='if')while(nodes[i+1]&&['else_if','else'].includes(nodes[i+1].key))group.push(nodes[++i]);if(!super.eval(group))return false;}
  }return true;}
}
function fresh(){const v=new ProofVM();v.flags.add('black_friday_active');v.flags.add('black_friday_natural_activation');v.arrays.set('global.fired_events',[ticks(26)]);
  v.set('global.black_friday_sale_sequence',1);v.write('black_friday_achievement_active_sale_sequence',S,false);v.write('black_friday_achievement_indexed_sale_sequence',S,false);return v;}
function component(v,tx,id,{family=1,primary=1,basis=1,member=id===primary?1:0,ordinary=10,paid=5,kind=1,source=26}={}){
  v.set('universal_cost_transaction_id',tx);if(!v.arrays.get('universal_cost_transaction_ids')?.includes(ticks(tx)))v.write('universal_cost_allocated_transaction_id_@var:universal_cost_transaction_id',ticks(tx),false);
  v.set('universal_cost_transaction_component_id',id).set('universal_cost_transaction_resource_kind',kind).set('universal_cost_transaction_resource_id',0)
   .set('universal_cost_transaction_ordinary_cost',ordinary).set('universal_cost_transaction_quoted_cost',paid).set('universal_cost_transaction_actual_paid_cost',paid)
   .set('universal_cost_transaction_source_id',source).set('universal_cost_transaction_primary_component',0)
   .set('universal_cost_transaction_achievement_family_id',family).set('universal_cost_transaction_achievement_primary_component_id',primary)
   .set('universal_cost_transaction_achievement_cost_basis',basis).set('universal_cost_transaction_achievement_primary_member',member);
  assert(v.call('universal_cost_record_transaction'));assert.equal(v.value('universal_cost_record_transaction_result'),S);return v;}
function settle(v,tx){v.set('universal_cost_transaction_id',tx);assert(v.call('universal_cost_settle_transaction'));assert.equal(v.value('universal_cost_settle_transaction_result'),S);}
function claim(v,tx,{family=1,ordinary=10,paid=5,pending=0,ppOnly=0,postExpiry=0}={}){
  v.set('black_friday_purchase_transaction_id',tx).set('black_friday_purchase_family_id',family).set('black_friday_purchase_ordinary_cost',ordinary)
   .set('black_friday_purchase_actual_paid_cost',paid).set('black_friday_purchase_is_refundable',pending).set('black_friday_purchase_allow_political_power_only',ppOnly)
   .set('black_friday_purchase_allow_post_expiry_confirmation',postExpiry).set('black_friday_purchase_sale_sequence',1);
  assert(v.run('black_friday_record_achievement_transaction'));return v;}
const results={sourceHashes:Object.fromEntries([...Object.entries(sources),...core.sources].map(([p,s])=>[p,crypto.createHash('sha256').update(s).digest('hex')])),scenarios:[],limitations:['native country eligibility/classification modeled','native resource credit effects modeled','native achievement delivery/serialization/performance not observed']};
function test(name,fn){fn();results.scenarios.push(name);}
test('valid-settled-primary-public-record-credit-and-repeat',()=>{const v=component(fresh(),1001,1);settle(v,1001);claim(v,1001);assert.equal(v.credits.length,1);assert.deepEqual(v.arrays.get('black_friday_achievement_transaction_family_ids'),[S]);claim(v,1001);assert.equal(v.credits.length,1);});
test('declared-consumer-goods-family-admits-explicit-typed-owner-payment',()=>{
  for(const kind of [1,100]){
    const v=component(fresh(),1110+kind,1,{family:65536,primary:1,member:1,kind});
    settle(v,1110+kind);claim(v,1110+kind,{family:65536});
    assert.equal(v.credits.length,1);assert.equal(v.credits[0].family,'65536');
    assert.equal(v.credits[0].ordinary,String(ticks(10)));assert.equal(v.credits[0].paid,String(ticks(5)));
  }
});
test('undeclared-logical-family-remains-ineligible-despite-positive-receipt',()=>{
  const v=component(fresh(),1111,1,{family:4097,primary:1,member:1});
  settle(v,1111);claim(v,1111,{family:4097});assert.equal(v.credits.length,0);
});
for(const defect of ['fully-refunded','partially-refunded','different-source','mismatched-paid','mismatched-ordinary','zero-paid','zero-ordinary','unsettled-immediate','wrong-family','missing-metadata','wrong-primary','refunded-component','wrong-component-source','tampered-total','conflicting-family'])test(`reject-${defect}`,()=>{
  const v=component(fresh(),1002,1,{source:defect==='different-source'?99:26,paid:defect==='zero-paid'?0:defect==='mismatched-paid'?1:5,ordinary:defect==='zero-ordinary'?0:defect==='mismatched-ordinary'?2:10,family:defect==='missing-metadata'?0:1,primary:defect==='wrong-primary'?9:1,member:defect==='wrong-primary'?0:1});
  if(defect!=='unsettled-immediate')settle(v,1002);
  if(defect==='fully-refunded')v.arrays.get('universal_cost_transaction_states')[0]=ticks(2);
  if(defect==='partially-refunded')v.arrays.get('universal_cost_transaction_states')[0]=ticks(3);
  if(defect==='refunded-component')v.arrays.get('universal_cost_component_refunded_states')[0]=S;
  if(defect==='wrong-component-source')v.arrays.get('universal_cost_component_source_ids')[0]=ticks(99);
  if(defect==='tampered-total')v.arrays.get('universal_cost_transaction_total_paid_costs')[0]=ticks(9);
  if(defect==='conflicting-family'){v.arrays.get('universal_cost_transaction_states')[0]=S;component(v,1002,2,{family:112,primary:1,member:0});settle(v,1002);}
  claim(v,1002,{paid:5,family:defect==='wrong-family'?112:1});assert.equal(v.credits.length,0);assert.equal((v.arrays.get('black_friday_achievement_transaction_ids')||[]).length,0);
});
test('primary-logical-family-not-resource-kind-and-secondary-nonPP-evidence',()=>{const v=component(fresh(),1003,1,{family:131072});component(v,1003,2,{family:131072,member:0,kind:2,ordinary:6,paid:3});settle(v,1003);claim(v,1003,{family:131072});assert.equal(v.credits[0].family,'131072');assert.equal(v.credits[0].nonPP,'1');});
test('primary-group-exact-claimed-subtotal-excludes-secondary-resource',()=>{const v=component(fresh(),1004,17,{family:131072,primary:0,basis:2,member:1,kind:17,ordinary:4,paid:2});component(v,1004,18,{family:131072,primary:0,basis:2,member:1,kind:18,ordinary:6,paid:3});component(v,1004,6,{family:131072,primary:0,basis:2,member:0,kind:11,ordinary:20,paid:10});settle(v,1004);claim(v,1004,{family:131072});assert.equal(v.credits.length,1);assert.equal(v.credits[0].paid,String(ticks(5)));});
test('group-rejects-whole-bundle-claim-instead-of-owner-subtotal',()=>{const v=component(fresh(),1005,17,{family:131072,primary:0,basis:2,member:1});component(v,1005,6,{family:131072,primary:0,basis:2,member:0,kind:11,ordinary:20,paid:10});settle(v,1005);claim(v,1005,{family:131072,ordinary:30,paid:15});assert.equal(v.credits.length,0);});
test('pending-refundables-no-early-credit-confirm-after-settle-only',()=>{const v=component(fresh(),1006,11,{family:112,primary:11,member:1,kind:100});claim(v,1006,{family:112,pending:1});assert.equal(v.credits.length,0);assert.equal(v.arrays.get('black_friday_achievement_transaction_states')[0],0n);v.run('black_friday_confirm_achievement_transaction');assert.equal(v.credits.length,0);settle(v,1006);v.run('black_friday_confirm_achievement_transaction');assert.equal(v.credits.length,1);v.run('black_friday_confirm_achievement_transaction');assert.equal(v.credits.length,1);});
test('pending-refund-before-confirm-rejects-credit',()=>{const v=component(fresh(),1007,1);claim(v,1007,{pending:1});v.set('universal_cost_transaction_id',1007);v.call('universal_cost_refund_transaction');v.run('black_friday_confirm_achievement_transaction');assert.equal(v.credits.length,0);assert.equal(v.arrays.get('black_friday_achievement_transaction_states')[0],0n);});
test('ordinary-expiry-blocks-new-credit-and-pending-confirm',()=>{const v=component(fresh(),1008,1);claim(v,1008,{pending:1});settle(v,1008);v.flags.delete('black_friday_active');v.run('black_friday_confirm_achievement_transaction');assert.equal(v.credits.length,0);});
test('accepted-delayed-PP-completion-after-expiry',()=>{const v=component(fresh(),1009,1);settle(v,1009);v.flags.delete('black_friday_active');claim(v,1009,{ppOnly:1,postExpiry:1});assert.equal(v.credits.length,1);claim(v,1009,{ppOnly:1,postExpiry:1});assert.equal(v.credits.length,1);});
test('PP-only-rejects-mixed-positive-secondary-payment',()=>{const v=component(fresh(),1010,1);component(v,1010,2,{member:0,kind:2,ordinary:6,paid:3});settle(v,1010);claim(v,1010,{ppOnly:1});assert.equal(v.credits.length,0);});
test('legacy-metadata-migration-preserves-earned-progress-and-pending-state',()=>{const v=component(fresh(),1011,1);claim(v,1011,{pending:1});v.arrays.delete('universal_cost_transaction_achievement_family_ids');v.arrays.delete('universal_cost_component_achievement_family_ids');v.arrays.delete('black_friday_achievement_transaction_ordinary_costs');v.write('black_friday_achievement_family_count',ticks(3),false);v.arrays.set('black_friday_achievement_family_ids',[S,ticks(112),ticks(131072)]);v.run('universal_cost_prepare_achievement_receipt_metadata');v.run('black_friday_prepare_achievement_claim_metadata');assert.equal(v.value('black_friday_achievement_family_count'),ticks(3));assert.equal(v.arrays.get('black_friday_achievement_transaction_states')[0],0n);settle(v,1011);v.run('black_friday_confirm_achievement_transaction');assert.equal(v.credits.length,0);});
test('modeled-reload-preserves-typed-pending-and-earned-regular-progress',()=>{const v=component(fresh(),1015,11,{family:112,primary:11,kind:100,member:1});claim(v,1015,{family:112,pending:1});v.write('black_friday_achievement_family_count',ticks(2),false);v.arrays.set('black_friday_achievement_family_ids',[S,ticks(131072)]);
  const encoded=JSON.stringify({vars:[...v.regularVars],arrays:[...v.arrays],flags:[...v.flags],country:[...v.countryFlags]},(_,x)=>typeof x==='bigint'?{ticks:String(x)}:x);
  const restored=JSON.parse(encoded,(_,x)=>x&&typeof x==='object'&&'ticks' in x?BigInt(x.ticks):x);const w=new ProofVM();w.regularVars=new Map(restored.vars);w.arrays=new Map(restored.arrays);w.flags=new Set(restored.flags);w.countryFlags=new Set(restored.country);
  w.run('universal_cost_prepare_achievement_receipt_metadata');w.run('black_friday_prepare_achievement_claim_metadata');assert.equal(w.value('black_friday_achievement_family_count'),ticks(2));assert.equal(w.arrays.get('black_friday_achievement_transaction_states')[0],0n);
  settle(w,1015);w.set('black_friday_purchase_transaction_id',1015);w.run('black_friday_confirm_achievement_transaction');assert.equal(w.credits.length,1);assert.equal(w.value('black_friday_achievement_family_count'),ticks(3));});
test('generic-source-zero-record-settle-refund-stays-usable-not-achievement',()=>{const v=component(fresh(),1012,1,{source:0,family:0});settle(v,1012);claim(v,1012);assert.equal(v.credits.length,0);const w=component(fresh(),1013,1,{source:0,family:0});w.set('universal_cost_transaction_id',1013);w.call('universal_cost_refund_transaction');assert.equal(w.value('universal_cost_refund_transaction_result'),S);assert.equal(w.wallet.get('pp'),ticks(5));});
test('accepted-native-Japan-raid-after-expiry-remains-separate',()=>{const v=fresh();v.tag='JAP';v.flags.delete('black_friday_active');v.targets.add('japan_cbrn_raid_price_sale');v.targets.add('japan_cbrn_raid_outcome_success');v.run('black_friday_credit_native_japan_cbrn_raid_family');assert.equal(v.credits.length,1);assert(v.countryFlags.has('black_friday_achievement_native_non_political_payment'));});
for(const invalid of ['manual','force','AI'])test(`eligibility-reject-${invalid}`,()=>{const v=component(fresh(),1014,1);settle(v,1014);if(invalid==='AI')v.ai=true;else v.flags.add(invalid==='manual'?'black_friday_manual_disqualified':'black_friday_force_disqualified');claim(v,1014);assert.equal(v.credits.length,0);});
function allocated(v,tx){v.set('black_friday_owner_transaction_id',tx);v.write('universal_cost_allocated_transaction_id_@var:black_friday_owner_transaction_id',ticks(tx),false);}
test('actual-RF-component-list-record-and-public-credit-fragments',()=>{
  const name='random_faction_black_friday_pay_component_list',v=fresh();allocated(v,1101);
  v.set('random_faction_black_friday_primary_family_id',2).set('random_faction_black_friday_primary_component_id',4)
    .set('random_faction_black_friday_primary_ordinary',10).set('random_faction_black_friday_primary_paid',5);
  for(const [name,values] of Object.entries({component_ids:[4,6],component_resource_kinds:[2,11],component_ordinary_costs:[10,6],component_final_costs:[5,3]}))v.tempArray(`random_faction_black_friday_${name}`,values.map(ticks));
  for(const cursor of [0,1]){v.set('random_faction_black_friday_payment_cursor',cursor);assert(v.run(`ec02_test_${name}_record`));}
  settle(v,1101);assert(v.run(`ec02_test_${name}_claim`));assert.equal(v.credits.length,1);assert.equal(v.credits[0].family,'2');assert.equal(v.credits[0].paid,String(ticks(5)));assert.deepEqual(v.arrays.get('universal_cost_component_achievement_primary_members'),[S,0n]);
});
test('actual-RF-liaison-1701-root-primary-1702-separate-leader-no-family-credit',()=>{
  assert.equal(constants.get('@random_faction_request_liaison_root_component_id'),ticks(1701));assert.equal(constants.get('@random_faction_request_liaison_leader_component_id'),ticks(1702));
  const requester=fresh(),leader=fresh(),ordinary=constants.get('constant:random_faction_decision_cost.command_power_low')/S;
  for(const [v,tx,id,kind,cost,paid,primary] of [[requester,1102,1701,2,ordinary,5,1],[leader,1103,1702,11,20,10,0]]){
    allocated(v,tx);v.write('random_faction_request_liaison_black_friday_transaction_id',ticks(tx),false);
    v.set('random_faction_request_liaison_black_friday_component_id',id).set('random_faction_request_liaison_black_friday_resource_kind',kind)
      .set('random_faction_request_liaison_black_friday_ordinary_cost',String(cost)).set('random_faction_request_liaison_black_friday_quoted_cost',paid).set('random_faction_request_liaison_black_friday_is_primary',primary);
    assert(v.run('ec02_test_random_faction_black_friday_pay_request_liaison_component_record'));settle(v,tx);
    assert.equal(v.arrays.get('universal_cost_transaction_achievement_primary_component_ids')[0],ticks(1701));
  }
  assert(requester.run('ec02_test_liaison_root_claim'));assert.equal(requester.credits.length,1);assert.equal(requester.credits[0].family,'2');assert.equal(requester.credits[0].nonPP,'1');
  // CP is non-PP payment, but the leader's equipment is not in ROOT's receipt.
  assert.equal(requester.arrays.get('universal_cost_component_ids').length,1);assert.equal(leader.arrays.get('universal_cost_component_achievement_primary_members')[0],0n);
  claim(leader,1103,{family:112,ordinary:20,paid:10});claim(leader,1103,{family:2,ordinary:20,paid:10});assert.equal(leader.credits.length,0);
});
test('actual-Mengele-CP-record-settle-public-credit-success-continuation',()=>{const name='mengele_clone_army_black_friday_pay_command_power',v=fresh();allocated(v,1104);v.set('mengele_clone_black_friday_ordinary_cost',10).set('mengele_clone_black_friday_paid_cost',5);assert(v.run(`ec02_test_${name}_record`));assert.equal(v.arrays.get('universal_cost_transaction_states')[0],ticks(4));assert.equal(v.credits.length,1);assert(v.run(`ec02_test_${name}_claim`));assert.equal(v.credits.length,1);assert.equal(v.credits[0].family,'2');assert.equal(v.arrays.get('universal_cost_transaction_achievement_primary_component_ids')[0],constants.get('constant:black_friday_event.owner_component_command_power'));});
results.externalBoundaryEvidence=[...externalFragments].map(([helper,x])=>({helper,path:x.path,recordStatements:x.record.nodes,claimScope:x.claim?.scope}));
results.externalBoundaryEvidence.push({helper:'random_faction_black_friday_pay_request_liaison',claimScope:liaisonClaim.scope,claimStatements:liaisonClaim.nodes});
results.externalSourceFinalHashes=Object.fromEntries(externalPaths.map(p=>[p,crypto.createHash('sha256').update(read(p)).digest('hex')]));
for(const p of externalPaths)assert.equal(results.externalSourceFinalHashes[p],results.sourceHashes[p],`concurrent owner source change: ${p}`);
results.limitations.push('Outside owner record/public-claim fragments execute actual receipt APIs. Allocation, quote, debit and cross-country outcome/eligibility gates are outside these bounded fragment fixtures. Separate requester/leader payer VMs model scope isolation.');
results.ownerForwarding=[];
for(const p of ['common/scripted_effects/026_black_friday_effects.txt','common/scripted_effects/012_africa_rsa_purchase_effects.txt']){
  const source=read(p);results.sourceHashes[p]=crypto.createHash('sha256').update(source).digest('hex');
  function audit(nodes,owner){for(let i=0;i<nodes.length;i++){const n=nodes[i];if(n.key==='universal_cost_record_transaction'){
    const recent=nodes.slice(Math.max(0,i-9),i);for(const field of ['family_id','primary_component_id','cost_basis','primary_member'])assert(recent.some(x=>x.key==='set_temp_variable'&&x.value[0].key===`universal_cost_transaction_achievement_${field}`),`${owner} lacks explicit ${field}`);
    results.ownerForwarding.push({path:p,owner,roleSource:recent.filter(x=>x.key==='set_temp_variable'&&x.value[0].key.startsWith('universal_cost_transaction_achievement_')).map(x=>x.value[0])});
  }if(Array.isArray(n.value))audit(n.value,owner);}}
  for(const n of parse(source))if(Array.isArray(n.value))audit(n.value,n.key);
}
results.scenarioCount=results.scenarios.length;results.familyPaymentEvidence=all.flatMap(v=>v.credits);results.helperReturns=all.reduce((n,v)=>n+v.helperReturns,0);results.droppedTemps=all.reduce((n,v)=>n+v.droppedTemps,0);
console.log(JSON.stringify(results,null,process.argv.includes('--details')?0:2));
