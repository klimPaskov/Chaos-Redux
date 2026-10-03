// Real receipt/debit/credit APIs under the exact VM's conservative helper frames.
// Only native resource reads/writes are modeled; shared receipt APIs are NEVER mocked.
// Run from the mod root with node; --details emits the complete evidence object.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const core = require('./exact_quote_source_tests.js');
const { VM, S, ticks, parse, root, definitions, callerOutputs, helperOutputs } = core;
const triggerPath = 'common/scripted_triggers/chaosx_universal_cost_triggers.txt';
const triggerSource = fs.readFileSync(path.join(root, triggerPath), 'utf8');
for (const node of parse(triggerSource)) definitions.set(node.key, node.value);
// Read-only bounded Event 026 integration: execute these TWO scanner bodies,
// never replace them with mocks or edit the parent's owning source file.
const bfSourcePath = 'common/scripted_effects/026_black_friday_effects.txt';
const bfConstantsPath = 'common/script_constants/026_black_friday_constants.txt';
const bfSource = fs.readFileSync(path.join(root, bfSourcePath), 'utf8');
const bfConstantsSource = fs.readFileSync(path.join(root, bfConstantsPath), 'utf8');
const bfScannerNames = ['black_friday_scan_receipt_non_political_payment', 'black_friday_scan_receipt_political_power_only'];
const bfScannerNodes = parse(bfSource).filter(n => bfScannerNames.includes(n.key));
assert.equal(bfScannerNodes.length, 2);
for (const node of bfScannerNodes) definitions.set(node.key, node.value);
const ordinaryProof = parse(bfSource).find(n => n.key === 'black_friday_validate_ordinary_receipt_proof');
assert(ordinaryProof); definitions.set(ordinaryProof.key, ordinaryProof.value);
for (const category of parse(bfConstantsSource)) if (Array.isArray(category.value)) for (const item of category.value)
  if (!Array.isArray(item.value) && /^-?\d+(\.\d+)?$/.test(item.value)) core.constants.set(`constant:${category.key}.${item.key}`, ticks(item.value));
const outputs = {
  universal_cost_pay_component: ['universal_cost_payment_result'],
  universal_cost_credit_component: ['universal_cost_credit_result'],
  universal_cost_find_transaction_row: ['universal_cost_transaction_found_index', 'universal_cost_transaction_is_indexed',
    'universal_cost_transaction_lookup_result', 'universal_cost_transaction_pointer'],
  universal_cost_find_component_row: ['universal_cost_component_found_index', 'universal_cost_component_lookup_result'],
  universal_cost_record_transaction: ['universal_cost_record_transaction_result', 'universal_cost_recorded_component_index'],
  universal_cost_settle_transaction: ['universal_cost_settle_transaction_result'],
  universal_cost_decrement_non_political_paid_count: [],
  universal_cost_mark_component_refunded: ['universal_cost_mark_component_refunded_result'],
  universal_cost_validate_component_chain: ['universal_cost_chain_valid'],
  universal_cost_refund_component_at_cursor: ['universal_cost_refund_total', 'universal_cost_refund_unhandled_total', 'universal_cost_refund_all_complete'],
  universal_cost_refund_transaction: ['universal_cost_refund_transaction_result', 'universal_cost_refund_total', 'universal_cost_refund_unhandled_total'],
  universal_cost_component_is_affordable: [],
  universal_cost_resource_kind_is_native: [],
  black_friday_scan_receipt_non_political_payment: ['black_friday_purchase_receipt_proof_valid', 'black_friday_purchase_has_non_political_paid_component'],
  black_friday_scan_receipt_political_power_only: ['black_friday_purchase_receipt_proof_valid', 'black_friday_purchase_has_non_political_paid_component'],
};
for (const [name, vars] of Object.entries(outputs)) {
  helperOutputs[name] = { vars, arrays: [] }; callerOutputs[name] = { vars, arrays: [] };
}
const instances = [];
const effectResources = { add_political_power: 'pp', add_command_power: 'cp', army_experience: 'army_xp',
  navy_experience: 'navy_xp', air_experience: 'air_xp', add_manpower: 'manpower', add_fuel: 'fuel',
  add_stability: 'stability', add_war_support: 'war_support' };
const triggerResources = { has_political_power: 'pp', political_power: 'pp', command_power: 'cp',
  has_army_experience: 'army_xp', has_navy_experience: 'navy_xp', has_air_experience: 'air_xp',
  has_manpower: 'manpower', has_fuel: 'fuel', has_stability: 'stability', has_war_support: 'war_support' };
class ReceiptVM extends VM {
  constructor() { super(); this.resources = new Map(); this.nativeWrites = []; instances.push(this); }
  balance(key, amount) { this.resources.set(key, ticks(amount)); return this; }
  eval(nodes) {
    // Keep if/else groups intact when delegating all non-native statements.
    for (let i = 0; i < nodes.length; i++) {
      const node = nodes[i], { key: k, value: v, op } = node;
      if (effectResources[k]) {
        const key = effectResources[k], delta = this.value(v);
        this.resources.set(key, (this.resources.get(key) || 0n) + delta);
        this.nativeWrites.push({ effect: k, key, delta: String(delta) });
      } else if (k === 'add_equipment_to_stockpile') {
        const key = `eq:${this.field(v, 'type')}`, delta = this.value(this.field(v, 'amount'));
        this.resources.set(key, (this.resources.get(key) || 0n) + delta);
        this.nativeWrites.push({ effect: k, key, delta: String(delta) });
      } else if (triggerResources[k] || k === 'has_equipment') {
        const comparison = k === 'has_equipment' ? v[0] : node;
        const key = k === 'has_equipment' ? `eq:${comparison.key}` : triggerResources[k];
        const left = this.resources.get(key) || 0n, right = this.value(comparison.value);
        const yes = comparison.op === '<' ? left < right : comparison.op === '>' ? left > right : left === right;
        if (!yes) return false;
      } else {
        const group = [node];
        if (k === 'if') while (nodes[i + 1] && ['else_if', 'else'].includes(nodes[i + 1].key)) group.push(nodes[++i]);
        if (!super.eval(group)) return false;
      }
    }
    return true;
  }
}
const keyPrefix = 'constant:universal_cost_resource_kind.';
const kind = name => core.constants.get(keyPrefix + name) / S;
const results = { sourceHashes: { ...Object.fromEntries([...core.sources].map(([f, s]) => [f, crypto.createHash('sha256').update(s).digest('hex')])),
    [triggerPath]: crypto.createHash('sha256').update(triggerSource).digest('hex') },
  lifetimeModel: 'ALL real shared APIs get conservative lexical cleanup; native resource effects/queries alone are modeled',
  helperContracts: outputs, scenarios: [], helperOutputChecks: {}, nativeResourceBranches: 0 };
results.sourceHashes[bfSourcePath] = crypto.createHash('sha256').update(bfSource).digest('hex');
results.sourceHashes[bfConstantsPath] = crypto.createHash('sha256').update(bfConstantsSource).digest('hex');
results.bfScannerSnapshots = bfScannerNodes.map(node => ({ name: node.key, body: node.value,
  astSha256: crypto.createHash('sha256').update(JSON.stringify(node.value)).digest('hex') }));
results.bfScannerCases = [];
function setupComponent(vm, tx, component, resource, paid, ordinary = paid) {
  return vm.set('universal_cost_transaction_id', tx).set('universal_cost_transaction_component_id', component)
    .set('universal_cost_transaction_resource_kind', resource).set('universal_cost_transaction_resource_id', 0)
    .set('universal_cost_transaction_ordinary_cost', ordinary).set('universal_cost_transaction_quoted_cost', paid)
    .set('universal_cost_transaction_actual_paid_cost', paid).set('universal_cost_transaction_source_id', 26)
    .set('universal_cost_transaction_primary_component', component === 1 ? 1 : 0);
}
function allocation(vm, tx) {
  vm.set('universal_cost_transaction_id', tx);
  // Persisted allocator PROOF is a fixture input. The record API must validate
  // and consume it; no allocator or receipt API is mocked in the test.
  vm.write('universal_cost_allocated_transaction_id_@var:universal_cost_transaction_id', ticks(tx), false);
  return vm;
}
function record(vm, tx, component, resource, paid, ordinary = paid, metadata = null) {
  setupComponent(vm, tx, component, resource, paid, ordinary);
  if (metadata) vm.set('universal_cost_transaction_achievement_family_id', metadata.family)
    .set('universal_cost_transaction_achievement_primary_component_id', metadata.primary)
    .set('universal_cost_transaction_achievement_cost_basis', metadata.basis)
    .set('universal_cost_transaction_achievement_primary_member', metadata.member);
  assert(vm.call('universal_cost_record_transaction'));
  assert.equal(vm.value('universal_cost_record_transaction_result'), S, 'real record API must succeed');
}
function lookup(vm, tx) {
  vm.set('universal_cost_transaction_lookup_id', tx); assert(vm.call('universal_cost_find_transaction_row'));
  return Number(vm.value('universal_cost_transaction_found_index') / S);
}
function row(vm, suffix, tx) { const index = lookup(vm, tx); assert(index >= 0); return vm.arrays.get(`universal_cost_transaction_${suffix}`)[index]; }
function componentLookup(vm, tx, component) {
  vm.set('universal_cost_component_lookup_transaction_id', tx).set('universal_cost_component_lookup_id', component);
  assert(vm.call('universal_cost_find_component_row')); return Number(vm.value('universal_cost_component_found_index') / S);
}
function expectRefund(vm, tx, result, total, unhandled = 0) {
  vm.set('universal_cost_transaction_id', tx); assert(vm.call('universal_cost_refund_transaction'));
  assert.equal(vm.value('universal_cost_refund_transaction_result'), ticks(result));
  assert.equal(vm.value('universal_cost_refund_total'), ticks(total));
  assert.equal(vm.value('universal_cost_refund_unhandled_total'), ticks(unhandled));
}
function scenario(id, fn) { fn(); results.scenarios.push(id); }

scenario('cold-record-append-lookup-chain-refund-repeat', () => {
  const vm = allocation(new ReceiptVM().balance('pp', 100).balance('cp', 100), 1001);
  record(vm, 1001, 1, kind('political_power'), 7, 14);
  record(vm, 1001, 2, kind('command_power'), 3, 6);
  assert.equal(lookup(vm, 1001), 0); assert.equal(vm.value('universal_cost_transaction_is_indexed'), S);
  assert.equal(componentLookup(vm, 1001, 2), 1);
  assert.equal(row(vm, 'total_paid_costs', 1001), ticks(10));
  assert.equal(row(vm, 'non_political_paid_component_count', 1001), S);
  vm.set('universal_cost_transaction_id', 1001);
  assert(vm.call('universal_cost_validate_component_chain')); assert.equal(vm.value('universal_cost_chain_valid'), S);
  expectRefund(vm, 1001, 1, 10);
  assert.equal(vm.resources.get('pp'), ticks(107)); assert.equal(vm.resources.get('cp'), ticks(103));
  assert.equal(row(vm, 'states', 1001), ticks(2)); assert.equal(row(vm, 'total_refunded_costs', 1001), ticks(10));
  assert.equal(row(vm, 'non_political_paid_component_count', 1001), 0n);
  const writes = vm.nativeWrites.length; expectRefund(vm, 1001, 0, 0); assert.equal(vm.nativeWrites.length, writes);
});
scenario('settlement-is-idempotent-and-blocks-refund-or-extension', () => {
  const vm = allocation(new ReceiptVM(), 1002); record(vm, 1002, 1, kind('political_power'), 5);
  vm.set('universal_cost_transaction_id', 1002); assert(vm.call('universal_cost_settle_transaction'));
  assert.equal(vm.value('universal_cost_settle_transaction_result'), S); assert.equal(row(vm, 'states', 1002), ticks(4));
  assert(vm.call('universal_cost_settle_transaction')); assert.equal(vm.value('universal_cost_settle_transaction_result'), 0n);
  expectRefund(vm, 1002, 0, 0); assert.equal(vm.nativeWrites.length, 0);
  setupComponent(vm, 1002, 2, kind('command_power'), 4); assert(vm.call('universal_cost_record_transaction'));
  assert.equal(vm.value('universal_cost_record_transaction_result'), 0n); assert.equal(row(vm, 'component_counts', 1002), S);
});
scenario('duplicate-proof-consumption-invalid-paid-and-missing-proof', () => {
  const vm = allocation(new ReceiptVM(), 1003); record(vm, 1003, 1, kind('political_power'), 5);
  assert.equal(vm.regularVars.has('universal_cost_allocated_transaction_id_@1003'), false);
  setupComponent(vm, 1003, 1, kind('political_power'), 5); assert(vm.call('universal_cost_record_transaction'));
  assert.equal(vm.value('universal_cost_record_transaction_result'), 0n); assert.equal(row(vm, 'component_counts', 1003), S);
  setupComponent(vm, 1003, 2, kind('command_power'), 4).set('universal_cost_transaction_actual_paid_cost', 3);
  assert(vm.call('universal_cost_record_transaction')); assert.equal(vm.value('universal_cost_record_transaction_result'), 0n);
  setupComponent(vm, 9999, 1, kind('political_power'), 1); assert(vm.call('universal_cost_record_transaction'));
  assert.equal(vm.value('universal_cost_record_transaction_result'), 0n); assert.equal(vm.arrays.get('universal_cost_transaction_ids').length, 1);
});
scenario('partial-owner-credit-acknowledgement-and-retry', () => {
  const vm = allocation(new ReceiptVM(), 1004);
  record(vm, 1004, 1, kind('political_power'), 7);
  record(vm, 1004, 2, kind('custom_adapter'), 11);
  expectRefund(vm, 1004, 2, 7, 11);
  assert.equal(row(vm, 'states', 1004), ticks(3)); assert.equal(row(vm, 'non_political_paid_component_count', 1004), S);
  const nativeWrites = vm.nativeWrites.length; expectRefund(vm, 1004, 2, 0, 11); assert.equal(vm.nativeWrites.length, nativeWrites);
  vm.set('universal_cost_transaction_component_id', 2); assert(vm.call('universal_cost_mark_component_refunded'));
  assert.equal(vm.value('universal_cost_mark_component_refunded_result'), S);
  assert.equal(row(vm, 'total_refunded_costs', 1004), ticks(18)); assert.equal(row(vm, 'non_political_paid_component_count', 1004), 0n);
  assert(vm.call('universal_cost_mark_component_refunded')); assert.equal(vm.value('universal_cost_mark_component_refunded_result'), 0n);
  expectRefund(vm, 1004, 1, 0); assert.equal(vm.nativeWrites.length, nativeWrites);
});
scenario('zero-paid-component-and-warm-outer-refund-cursors', () => {
  const vm = allocation(new ReceiptVM(), 1005);
  record(vm, 1005, 1, kind('political_power'), 1);
  record(vm, 1005, 2, kind('command_power'), 2);
  record(vm, 1005, 3, kind('support_equipment_1'), 3);
  record(vm, 1005, 4, kind('custom_adapter'), 0, 7);
  vm.set('universal_cost_refund_cursor', 999).set('universal_cost_refund_pointer', 999)
    .set('universal_cost_transaction_found_index', 999).set('universal_cost_component_found_index', 999);
  expectRefund(vm, 1005, 1, 6);
  assert.equal(vm.nativeWrites.length, 3); assert.equal(row(vm, 'total_refunded_costs', 1005), ticks(6));
  assert(vm.arrays.get('universal_cost_component_refunded_states').every(v => v === S));
});
for (const defect of ['wrong-row-pointer', 'wrong-next-target', 'cycle', 'wrong-tail', 'wrong-count']) scenario(`reject-corrupt-${defect}`, () => {
  const vm = allocation(new ReceiptVM(), 2001); record(vm, 2001, 1, kind('political_power'), 5);
  record(vm, 2001, 2, kind('command_power'), 4);
  if (defect === 'wrong-row-pointer') vm.regularVars.set('universal_cost_transaction_row_plus_one_@2001', ticks(9));
  if (defect === 'wrong-next-target') vm.arrays.get('universal_cost_component_next_plus_one')[0] = ticks(999);
  if (defect === 'cycle') vm.arrays.get('universal_cost_component_next_plus_one')[1] = S;
  if (defect === 'wrong-tail') vm.arrays.get('universal_cost_transaction_component_tail_plus_one')[0] = S;
  if (defect === 'wrong-count') vm.arrays.get('universal_cost_transaction_component_counts')[0] = ticks(3);
  expectRefund(vm, 2001, 3, 0); assert.equal(vm.nativeWrites.length, 0);
  if (defect !== 'wrong-row-pointer') {
    assert.equal(componentLookup(vm, 2001, 2), -1); assert.equal(vm.value('universal_cost_component_lookup_result'), ticks(3));
  }
});
scenario('payer-isolation-and-interleaved-links', () => {
  const a = allocation(new ReceiptVM(), 3001), b = allocation(new ReceiptVM(), 3001);
  record(a, 3001, 1, kind('political_power'), 5); record(b, 3001, 1, kind('command_power'), 8);
  allocation(a, 3002); record(a, 3002, 1, kind('political_power'), 9);
  record(a, 3001, 2, kind('command_power'), 4); expectRefund(a, 3001, 1, 9);
  assert.equal(row(a, 'states', 3002), S); assert.equal(row(b, 'states', 3001), S);
  assert.equal(b.nativeWrites.length, 0); assert.equal(a.nativeWrites.length, 2);
});
scenario('legacy-mapless-lookup-refund-and-extension-rejection', () => {
  const vm = allocation(new ReceiptVM(), 4001); record(vm, 4001, 1, kind('political_power'), 6);
  vm.regularVars.delete('universal_cost_transaction_row_plus_one_@4001');
  assert.equal(lookup(vm, 4001), 0); assert.equal(vm.value('universal_cost_transaction_is_indexed'), 0n);
  assert.equal(componentLookup(vm, 4001, 1), 0);
  setupComponent(vm, 4001, 2, kind('command_power'), 4); assert(vm.call('universal_cost_record_transaction'));
  assert.equal(vm.value('universal_cost_record_transaction_result'), 0n);
  expectRefund(vm, 4001, 1, 6); assert.equal(vm.nativeWrites.length, 1);
});
scenario('indexed-receipt-beyond-legacy-1000-row-bound', () => {
  const vm = new ReceiptVM();
  for (let i = 0; i < 1003; i++) { allocation(vm, 5000 + i); record(vm, 5000 + i, 1, kind('political_power'), 1); }
  assert.equal(lookup(vm, 6002), 1002); assert.equal(componentLookup(vm, 6002, 1), 1002);
  expectRefund(vm, 6002, 1, 1); assert.equal(vm.nativeWrites.length, 1);
  vm.regularVars.delete('universal_cost_transaction_row_plus_one_@6002');
  lookup(vm, 6002); assert.equal(vm.value('universal_cost_transaction_lookup_result'), ticks(3));
});
scenario('native-noops-unsupported-and-inclusive-affordability', () => {
  const vm = new ReceiptVM().balance('pp', 5);
  vm.set('universal_cost_payment_resource_kind', kind('political_power')).set('universal_cost_payment_amount', 5);
  assert(vm.call('universal_cost_pay_component')); assert.equal(vm.value('universal_cost_payment_result'), S);
  assert.equal(vm.resources.get('pp'), 0n);
  assert(vm.call('universal_cost_pay_component')); assert.equal(vm.value('universal_cost_payment_result'), 0n);
  assert.equal(vm.nativeWrites.length, 1);
  for (const amount of [0, -5]) {
    vm.set('universal_cost_payment_amount', amount); assert(vm.call('universal_cost_pay_component'));
    assert(vm.call('universal_cost_credit_component')); assert.equal(vm.value('universal_cost_credit_result'), S);
  }
  vm.set('universal_cost_payment_resource_kind', kind('custom_adapter')).set('universal_cost_payment_amount', 2);
  assert(vm.call('universal_cost_pay_component')); assert.equal(vm.value('universal_cost_payment_result'), 0n);
  assert(vm.call('universal_cost_credit_component')); assert.equal(vm.value('universal_cost_credit_result'), 0n);
  vm.set('universal_cost_affordability_resource_kind', kind('custom_adapter'));
  assert.equal(vm.call('universal_cost_resource_kind_is_native'), false);
  assert.equal(vm.nativeWrites.length, 1);
});
scenario('real-quote-payment-record-expiry-refund', () => {
  const vm = allocation(new ReceiptVM().balance('pp', 100), 8001);
  vm.set('universal_cost_source_ratio', 5000).set('universal_cost_source_eligibility_mask', 0);
  assert(vm.call('universal_cost_source_register_black_friday'));
  vm.set('universal_cost_quote_ordinary_cost', 125).set('universal_cost_quote_family_mask', 1).set('universal_cost_quote_rounding_quantum', 1);
  assert(vm.call('universal_cost_quote_integer')); assert.equal(vm.value('universal_cost_quote_final_cost'), ticks(63));
  vm.set('universal_cost_payment_resource_kind', kind('political_power')).set('universal_cost_payment_amount', 63);
  assert(vm.call('universal_cost_pay_component')); assert.equal(vm.resources.get('pp'), ticks(37));
  record(vm, 8001, 1, kind('political_power'), 63, 125);
  assert(vm.call('universal_cost_source_clear_black_friday'));
  assert(vm.call('universal_cost_quote_integer')); assert.equal(vm.value('universal_cost_quote_final_cost'), ticks(125));
  expectRefund(vm, 8001, 1, 63); assert.equal(vm.resources.get('pp'), ticks(100));
  assert.equal(row(vm, 'total_paid_costs', 8001), ticks(63)); assert.equal(row(vm, 'total_refunded_costs', 8001), ticks(63));
});
const ppComponentId = core.constants.get('constant:black_friday_event.owner_component_political_power') / S;
function scan(vm, label, tx, actualPaid, nonPoliticalExpected, ppOnlyExpected) {
  vm.set('black_friday_purchase_transaction_id', tx).set('black_friday_purchase_family_id', 1)
    .set('black_friday_purchase_actual_paid_cost', actualPaid).set('black_friday_purchase_ordinary_cost', 5)
    .set('black_friday_purchase_is_refundable', 0);
  for (const [api, expected] of [[bfScannerNames[0], nonPoliticalExpected], [bfScannerNames[1], ppOnlyExpected]]) {
    // EXPLICIT source-like caller declarations, not blanket VM scratch seeds.
    vm.set('black_friday_purchase_receipt_proof_valid', 0).set('black_friday_purchase_has_non_political_paid_component', 0);
    assert(vm.call(api));
    const proof = vm.value('black_friday_purchase_receipt_proof_valid') / S;
    const nonPolitical = vm.value('black_friday_purchase_has_non_political_paid_component') / S;
    assert.deepEqual([proof, nonPolitical], expected.map(BigInt), `${label} ${api}`);
    results.bfScannerCases.push({ label, api, transaction: String(tx), actualPaid: String(actualPaid),
      proofValid: String(proof), hasNonPoliticalPaid: String(nonPolitical) });
  }
}
scenario('actual-BF-scans-recorded-settled-refunded-absent-and-mixed', () => {
  const typed = (vm,tx,id,resource,paid) => record(vm,tx,id,resource,paid,paid,{family:1,primary:ppComponentId,basis:1,member:BigInt(id)===ppComponentId?1:0});
  const pp = allocation(new ReceiptVM(), 8801); typed(pp, 8801, ppComponentId, kind('political_power'), 5);
  scan(pp, 'recorded-pp-immediate-rejected', 8801, 5, [0, 0], [0, 0]);
  pp.set('universal_cost_transaction_id', 8801); assert(pp.call('universal_cost_settle_transaction'));
  scan(pp, 'settled-pp', 8801, 5, [1, 0], [1, 0]);
  const mixed = allocation(new ReceiptVM(), 8802);
  typed(mixed, 8802, ppComponentId, kind('political_power'), 5); typed(mixed, 8802, 99, kind('command_power'), 3);
  scan(mixed, 'recorded-mixed-aggregate', 8802, 8, [0, 0], [0, 0]);
  mixed.set('universal_cost_transaction_id', 8802); assert(mixed.call('universal_cost_settle_transaction'));
  scan(mixed, 'settled-mixed-wrong-basis-aggregate', 8802, 8, [0, 0], [0, 0]);
  scan(mixed, 'settled-mixed-matching-primary-component', 8802, 5, [1, 1], [0, 1]);
  const refunded = allocation(new ReceiptVM(), 8803);
  typed(refunded, 8803, ppComponentId, kind('political_power'), 5); typed(refunded, 8803, 99, kind('command_power'), 3);
  expectRefund(refunded, 8803, 1, 8);
  scan(refunded, 'fully-refunded-mixed', 8803, 8, [0, 0], [0, 0]);
  scan(refunded, 'absent-receipt-warm-caller', 9999, 5, [0, 0], [0, 0]);
  const wrong = allocation(new ReceiptVM(), 8804); typed(wrong, 8804, ppComponentId, kind('political_power'), 5);
  wrong.set('universal_cost_transaction_id', 8804); assert(wrong.call('universal_cost_settle_transaction'));
  wrong.arrays.get('universal_cost_component_source_ids')[0] = ticks(77);
  scan(wrong, 'settled-wrong-component-source', 8804, 5, [0, 0], [0, 0]);
  pp.set('black_friday_purchase_transaction_id', 8801).set('black_friday_purchase_actual_paid_cost', 5).set('black_friday_purchase_family_id', 2);
  pp.set('black_friday_purchase_receipt_proof_valid', 0).set('black_friday_purchase_has_non_political_paid_component', 0);
  assert(pp.call(bfScannerNames[1])); assert.equal(pp.value('black_friday_purchase_receipt_proof_valid'), 0n);
  results.bfScannerCases.push({ label: 'settled-wrong-family', api: bfScannerNames[1], transaction: '8801',
    actualPaid: '5', family: '2', proofValid: '0', hasNonPoliticalPaid: '0' });
});
// Enumerate the actual credit body to exercise every native dispatch pair.
const dispatches = [];
function walk(nodes) { for (const n of nodes) { if (effectResources[n.key]) dispatches.push(effectResources[n.key]);
  if (n.key === 'add_equipment_to_stockpile') dispatches.push(`eq:${n.value.find(x => x.key === 'type').value}`);
  if (Array.isArray(n.value)) walk(n.value); } }
walk(definitions.get('universal_cost_credit_component'));
for (let resource = 1; resource <= 29; resource++) scenario(`native-dispatch-${resource}`, () => {
  const fractional = resource === Number(kind('stability')) || resource === Number(kind('war_support'));
  const baseline = fractional ? '0.5' : '50', amount = fractional ? '0.07' : '7', after = fractional ? '0.43' : '43';
  const vm = new ReceiptVM(); for (const key of dispatches) vm.balance(key, baseline);
  vm.set('universal_cost_affordability_resource_kind', resource); assert(vm.call('universal_cost_resource_kind_is_native'));
  vm.set('universal_cost_payment_resource_kind', resource).set('universal_cost_payment_amount', amount);
  assert(vm.call('universal_cost_pay_component')); assert.equal(vm.value('universal_cost_payment_result'), S);
  assert.equal(vm.nativeWrites.length, 1); const { key } = vm.nativeWrites[0]; assert.equal(vm.resources.get(key), ticks(after));
  assert(vm.call('universal_cost_credit_component')); assert.equal(vm.value('universal_cost_credit_result'), S);
  assert.equal(vm.nativeWrites.length, 2); assert.equal(vm.resources.get(key), ticks(baseline)); results.nativeResourceBranches++;
});
for (const vm of instances) for (const [name, n] of vm.helperOutputChecks) results.helperOutputChecks[name] = (results.helperOutputChecks[name] || 0) + n;
for (const name of Object.keys(outputs)) assert(results.helperOutputChecks[name] > 0, `unexercised real receipt API ${name}`);
results.scenarioCount = results.scenarios.length;
results.helperReturns = instances.reduce((n, vm) => n + vm.helperReturns, 0);
results.droppedTemps = instances.reduce((n, vm) => n + vm.droppedTemps, 0);
// Freeze the exact parsed bodies above. If an outer-caller worker changes the
// file concurrently, report both revisions and selected-body equality explicitly.
const finalBfSource = fs.readFileSync(path.join(root, bfSourcePath), 'utf8');
const finalBfAst = parse(finalBfSource).filter(n => bfScannerNames.includes(n.key));
results.concurrentBfSource = { capturedSha256: results.sourceHashes[bfSourcePath],
  finalSha256: crypto.createHash('sha256').update(finalBfSource).digest('hex'),
  selectedScannerBodiesUnchanged: JSON.stringify(bfScannerNodes) === JSON.stringify(finalBfAst) };
assert(results.concurrentBfSource.selectedScannerBodiesUnchanged, 'BF scanner body changed during evidence run; retry on one source snapshot');
results.concurrentBfSource.wholeFileChanged = results.concurrentBfSource.capturedSha256 !== results.concurrentBfSource.finalSha256;
console.log(JSON.stringify(results, null, process.argv.includes('--details') ? 0 : 2));
