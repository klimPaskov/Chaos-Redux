// Country-contract CBRN component tests using the existing actual-source VM.
// Native PP/equipment reads and writes alone are modeled. Receipt APIs are real.
// Inputs are component fixtures, not proof of the full state order or quotation.
// Run from the mod root: node docs/testing/2026-10-03_cbrn_immediate_protection_source_tests.js
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const core = require('../plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
const { VM, S, ticks, parse, root, definitions, constants, helperOutputs } = core;
const sha = value => crypto.createHash('sha256').update(value).digest('hex');
const sources = new Map(core.sources);
for (const file of ['common/scripted_triggers/chaosx_universal_cost_triggers.txt',
  'common/scripted_effects/cbrn_immediate_response_cost_effects.txt']) {
  const source = fs.readFileSync(path.join(root, file), 'utf8'); sources.set(file, source);
  for (const node of parse(source)) definitions.set(node.key, node.value);
}
// Entry audits require storage declared by the actual caller. These maps do not
// initialize nested API scratch or replace any parsed effect/trigger body.
const outputs = {
  cbrn_pay_and_record_response_component: ['cbrn_response_all_paid'],
  cbrn_refund_unfinished_response_transaction: [],
  universal_cost_pay_component: ['universal_cost_payment_result'],
  universal_cost_credit_component: ['universal_cost_credit_result'],
  universal_cost_find_transaction_row: ['universal_cost_transaction_found_index', 'universal_cost_transaction_is_indexed',
    'universal_cost_transaction_lookup_result', 'universal_cost_transaction_pointer'],
  universal_cost_record_transaction: ['universal_cost_record_transaction_result', 'universal_cost_recorded_component_index'],
  universal_cost_validate_component_chain: ['universal_cost_chain_valid'],
  universal_cost_refund_component_at_cursor: ['universal_cost_refund_total', 'universal_cost_refund_unhandled_total', 'universal_cost_refund_all_complete'],
  universal_cost_refund_transaction: ['universal_cost_refund_transaction_result', 'universal_cost_refund_total', 'universal_cost_refund_unhandled_total'],
};
for (const [name, vars] of Object.entries(outputs)) helperOutputs[name] = { vars, arrays: [] };
const selected = new Set(), instances = [];
class ResponseVM extends VM {
  constructor() { super(); this.resources = new Map(); this.nativeWrites = []; instances.push(this); }
  balance(key, amount) { this.resources.set(key, ticks(amount)); return this; }
  run(name, uninitialized = false) { selected.add(name); return super.run(name, uninitialized); }
  eval(nodes) {
    for (let i = 0; i < nodes.length; i++) {
      const node = nodes[i], { key: k, value: v } = node;
      if (k === 'add_political_power' || k === 'add_equipment_to_stockpile') {
        const key = k === 'add_political_power' ? 'pp' : `eq:${this.field(v, 'type')}`;
        const delta = this.value(k === 'add_political_power' ? v : this.field(v, 'amount'));
        this.resources.set(key, (this.resources.get(key) || 0n) + delta);
        this.nativeWrites.push({ effect: k, key, delta: String(delta / S) });
      } else if (k === 'has_political_power' || k === 'political_power' || k === 'has_equipment') {
        const comparison = k === 'has_equipment' ? v[0] : node;
        const key = k === 'has_equipment' ? `eq:${comparison.key}` : 'pp';
        const left = this.resources.get(key) || 0n, right = this.value(comparison.value);
        const yes = comparison.op === '<' ? left < right : comparison.op === '>' ? left > right : left === right;
        if (!yes) return false;
      } else {
        // Preserve native if/else grouping before handing execution to the VM.
        const group = [node];
        if (k === 'if') while (nodes[i + 1] && ['else_if', 'else'].includes(nodes[i + 1].key)) group.push(nodes[++i]);
        if (!super.eval(group)) return false;
      }
    }
    return true;
  }
}
const constant = name => constants.get(`constant:${name}`) / S;
const kind = name => constant(`universal_cost_resource_kind.${name}`);
const maskNames = ['gas_mask_equipment_reconditioned', 'gas_mask_equipment_1', 'gas_mask_equipment_2',
  'gas_mask_equipment_3', 'gas_mask_equipment_4'];
const resultPath = path.join(root, 'docs/testing/2026-10-03_cbrn_immediate_protection_source_results.json');
const vmPath = 'docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js';
const capturedVMHash = sha(fs.readFileSync(path.join(root, vmPath)));
const results = {
  status: 'running', sourceHashes: Object.fromEntries([...sources].map(([f, source]) => [f, sha(source)])),
  reusedVM: 'docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js',
  reusedVMSha256: capturedVMHash,
  nativeAdapterPrecedent: 'docs/plans/026_black_friday_plans/subagent_handoffs/universal_cost_receipt_lifetime_source_tests.js',
  lifetimeModel: 'Conservative lexical helper cleanup. Outer component inputs/all_paid alone are initialized in cold cases.',
  inputContract: 'Explicit component fixtures, including persisted allocator proofs. No quote, allocator, ROOT/FROM order, issue, outcome, AI, renderer, engine, or performance claim.',
  scenarios: [], helperOutputChecks: {}, concurrentSources: {}, selectedBodyHashes: {},
  limitations: [
    'Native PP and concrete equipment stock are modeled without producer provenance or engine caps.',
    'Hospital oldest-first model amounts are fixtures. The quote helper and allocation algorithm are not executed.',
    'Positive-issued emergency commitment is a persisted marker fixture. Physical issue and marker creation are outside this helper test.',
    'No engine-facing source was edited. MCP reference routes are not exposed to this subagent, and source tests do not replace parent MCP evidence.',
  ],
};
function tx(vm, id, emergency = false) {
  vm.set('cbrn_response_transaction', id).set('cbrn_response_source', 26)
    .set('cbrn_response_family', constant(`universal_cost_family.${emergency ? 'political_power' : 'state_project'}`))
    .set('cbrn_response_basis', constant(`universal_cost_achievement_basis.${emergency ? 'primary_component' : 'primary_group'}`))
    .set('cbrn_response_primary', emergency ? kind('political_power') : 0).set('cbrn_response_all_paid', 1);
  // Persisted proof is an allocator-contract fixture, consumed by real record.
  vm.write('universal_cost_allocated_transaction_id_@var:cbrn_response_transaction', ticks(id), false);
  return vm;
}
function pay(vm, name, ordinary, quoted, member = 1) {
  vm.set('cbrn_response_component_kind', kind(name)).set('cbrn_response_component_ordinary', ordinary)
    .set('cbrn_response_component_quoted', quoted).set('cbrn_response_component_primary_member', member);
  assert(vm.run('cbrn_pay_and_record_response_component'));
}
function refund(vm) { assert(vm.run('cbrn_refund_unfinished_response_transaction')); }
function receipt(vm, suffix, id) {
  const index = vm.array('universal_cost_transaction_ids').indexOf(ticks(id)); assert(index >= 0);
  return vm.array(`universal_cost_transaction_${suffix}`)[index];
}
function expectBalance(vm, key, amount) { assert.equal(vm.resources.get(key) || 0n, ticks(amount), key); }
function expectNoProof(vm, id) { assert.equal(vm.regularVars.has(`universal_cost_allocated_transaction_id_@${id}`), false); }
function snapshot(vm) { return Object.fromEntries([...vm.resources].map(([key, n]) => [key, String(n / S)])); }
function warm(vm) {
  for (const vars of Object.values(outputs)) for (const name of vars) if (!vm.vars.has(name)) vm.set(name, 999);
  for (const name of ['universal_cost_refund_cursor', 'universal_cost_refund_pointer', 'universal_cost_component_found_index']) vm.set(name, 999);
  return vm;
}
function scenario(id, fn) {
  try { results.scenarios.push({ id, status: 'passed', evidence: fn() }); }
  catch (error) { results.scenarios.push({ id, status: 'failed', error: error.stack }); }
}

for (const mode of ['cold', 'warm']) for (const fixture of [
  { label: 'normal', pp: 10, support: 20, masks: [3, 4, 5, 6, 12] },
  { label: 'half', pp: 5, support: 10, masks: [3, 4, 5, 3, 0] },
  { label: 'quarter', pp: 3, support: 5, masks: [3, 4, 1, 0, 0] },
]) scenario(`hospital-${fixture.label}-${mode}-exact-model-payment-refund-repeat`, () => {
  const id = 100 + results.scenarios.length;
  const vm = tx(new ResponseVM().balance('pp', 100).balance('eq:support_equipment_1', 100), id);
  const initialMasks = [3, 4, 5, 6, 12];
  maskNames.forEach((name, i) => vm.balance(`eq:${name}`, initialMasks[i]));
  if (mode === 'warm') warm(vm);
  const before = snapshot(vm), count = fixture.masks.reduce((a, b) => a + b, 0);
  pay(vm, 'political_power', 10, fixture.pp, 0);
  pay(vm, 'support_equipment_1', 20, fixture.support);
  maskNames.forEach((name, i) => pay(vm, name, fixture.masks[i] + (i === 0 ? 30 - count : 0), fixture.masks[i]));
  assert.equal(vm.value('cbrn_response_all_paid'), S);
  expectBalance(vm, 'pp', 100 - fixture.pp); expectBalance(vm, 'eq:support_equipment_1', 100 - fixture.support);
  maskNames.forEach((name, i) => expectBalance(vm, `eq:${name}`, initialMasks[i] - fixture.masks[i]));
  assert.equal(receipt(vm, 'component_counts', id), ticks(7));
  assert.equal(receipt(vm, 'total_ordinary_costs', id), ticks(60));
  assert.equal(receipt(vm, 'total_paid_costs', id), ticks(fixture.pp + fixture.support + count));
  assert.equal(receipt(vm, 'achievement_family_ids', id), ticks(constant('universal_cost_family.state_project')));
  assert.equal(receipt(vm, 'achievement_cost_bases', id), ticks(constant('universal_cost_achievement_basis.primary_group')));
  assert.deepEqual(vm.array('universal_cost_component_achievement_primary_members'), [0n, S, S, S, S, S, S]);
  expectNoProof(vm, id);
  const afterPayment = snapshot(vm), debitWrites = vm.nativeWrites.length;
  refund(vm); assert.deepEqual(snapshot(vm), before); assert.equal(receipt(vm, 'states', id), ticks(2));
  assert(vm.array('universal_cost_component_refunded_states').every(n => n === S));
  const afterRefundWrites = vm.nativeWrites.length;
  assert.equal(afterRefundWrites, debitWrites * 2, 'zero-paid rows do not create resource credits');
  refund(vm); assert.equal(vm.nativeWrites.length, afterRefundWrites); assert.deepEqual(snapshot(vm), before);
  if (mode === 'cold') for (const name of ['universal_cost_payment_result', 'universal_cost_record_transaction_result', 'universal_cost_refund_total'])
    assert.equal(vm.vars.has(name), false, `helper-local output ${name} must die on return`);
  else { assert.equal(vm.value('universal_cost_refund_total'), 0n); assert.equal(vm.value('universal_cost_refund_transaction_result'), 0n); }
  return { components: 7, masks: fixture.masks, quotedInputs: { pp: fixture.pp, support: fixture.support, masks: count }, before, afterPayment,
    nativeWrites: vm.nativeWrites, lexicalTempsDropped: vm.droppedTemps };
});

scenario('zero-paid-counterfactual-model-does-not-invent-stock', () => {
  const vm = tx(new ResponseVM().balance('pp', 20).balance('eq:support_equipment_1', 20)
    .balance('eq:gas_mask_equipment_1', 8), 201);
  pay(vm, 'political_power', 10, 3, 0); pay(vm, 'support_equipment_1', 20, 5);
  // Ordinary30/quoted8: the unused22 counterfactual belongs to an empty oldest model.
  pay(vm, maskNames[0], 22, 0); pay(vm, maskNames[1], 8, 8);
  for (const name of maskNames.slice(2)) pay(vm, name, 0, 0);
  assert.equal(vm.value('cbrn_response_all_paid'), S);
  assert.equal(vm.array('universal_cost_component_ordinary_costs')[2], ticks(22));
  assert.equal(vm.array('universal_cost_component_actual_paid_costs')[2], 0n);
  assert.equal(vm.nativeWrites.length, 3);
  refund(vm); expectBalance(vm, `eq:${maskNames[0]}`, 0); expectBalance(vm, `eq:${maskNames[1]}`, 8);
  assert.equal(vm.nativeWrites.length, 6); refund(vm); assert.equal(vm.nativeWrites.length, 6);
  return { counterfactualOrdinary: 22, actualPaid: 0, nativeWrites: vm.nativeWrites };
});

for (const mode of ['cold', 'warm']) for (const failure of ['first-payment', 'first-record', 'missing-proof', 'later-payment', 'later-record'])
scenario(`${failure}-${mode}-rollback-and-proof-cleanup`, () => {
  const id = 300 + results.scenarios.length;
  const vm = tx(new ResponseVM().balance('pp', failure === 'first-payment' ? 2 : 100)
    .balance('eq:support_equipment_1', failure === 'later-payment' ? 2 : 100), id);
  if (mode === 'warm') warm(vm);
  const before = snapshot(vm);
  if (failure === 'missing-proof') vm.regularVars.delete(`universal_cost_allocated_transaction_id_@${id}`);
  pay(vm, 'political_power', failure === 'first-record' ? -1 : 10, 5, 0);
  if (failure.startsWith('later-')) pay(vm, 'support_equipment_1', failure === 'later-record' ? -1 : 20, 10);
  assert.equal(vm.value('cbrn_response_all_paid'), 0n);
  const writes = vm.nativeWrites.length;
  pay(vm, 'gas_mask_equipment_4', 1, 1); assert.equal(vm.nativeWrites.length, writes, 'failed order must skip later components');
  refund(vm); assert.deepEqual(snapshot(vm), before); expectNoProof(vm, id);
  const refundedWrites = vm.nativeWrites.length; refund(vm); assert.equal(vm.nativeWrites.length, refundedWrites);
  if (!failure.startsWith('later-')) assert.equal(vm.array('universal_cost_transaction_ids').length, 0);
  else assert.equal(receipt(vm, 'states', id), ticks(2));
  return { failureFixture: failure, restored: snapshot(vm), allocatorProofCleared: true, nativeWrites: vm.nativeWrites };
});

for (const committed of [false, true]) scenario(`emergency-pp-only-${committed ? 'positive-issued-commit-refuses-refund' : 'unissued-refund'}`, () => {
  const id = committed ? 502 : 501, vm = tx(new ResponseVM().balance('pp', 50), id, true);
  pay(vm, 'political_power', 10, 5);
  assert.equal(vm.value('cbrn_response_all_paid'), S); assert.equal(receipt(vm, 'component_counts', id), S);
  assert.equal(receipt(vm, 'achievement_family_ids', id), ticks(constant('universal_cost_family.political_power')));
  assert.equal(receipt(vm, 'achievement_primary_component_ids', id), ticks(kind('political_power')));
  assert.equal(receipt(vm, 'achievement_cost_bases', id), ticks(constant('universal_cost_achievement_basis.primary_component')));
  assert.deepEqual(vm.array('universal_cost_component_achievement_primary_members'), [S]);
  // A different transaction's positive-issue marker must not block this receipt.
  vm.write('cbrn_emergency_committed_receipt_@999', ticks(999), false);
  if (committed) vm.write('cbrn_emergency_committed_receipt_@var:cbrn_response_transaction', ticks(id), false);
  const refundCallsBefore = vm.helperOutputChecks.get('universal_cost_refund_transaction') || 0;
  refund(vm); refund(vm);
  expectBalance(vm, 'pp', committed ? 45 : 50);
  assert.equal(vm.nativeWrites.length, committed ? 1 : 2);
  assert.equal(receipt(vm, 'states', id), ticks(committed ? 1 : 2));
  if (committed) assert.equal(vm.helperOutputChecks.get('universal_cost_refund_transaction') || 0, refundCallsBefore,
    'committed marker refuses refund even before settlement, without calling refund API');
  return { metadata: 'political_power / primary_component / PPmember1', markerFixture: committed, nativeWrites: vm.nativeWrites };
});

scenario('corrupt-recorded-chain-retains-status-without-credit-and-clears-after-repair', () => {
  const cases = [];
  for (const mode of ['cold', 'warm']) {
    const id = mode === 'cold' ? 601 : 602;
    const vm = tx(new ResponseVM().balance('pp', 20).balance('eq:support_equipment_1', 20), id);
    if (mode === 'warm') warm(vm);
    const initial = snapshot(vm);
    pay(vm, 'political_power', 10, 5, 0); pay(vm, 'support_equipment_1', 20, 10);
    const paid = snapshot(vm), writes = vm.nativeWrites.length;
    const savedNext = vm.array('universal_cost_component_next_plus_one')[0];
    // Explicit persisted-ledger corruption fixture. No API body is changed.
    vm.array('universal_cost_component_next_plus_one')[0] = ticks(999);
    for (let attempt = 0; attempt < 2; attempt++) {
      refund(vm); assert.deepEqual(snapshot(vm), paid); assert.equal(vm.nativeWrites.length, writes);
      assert.equal(vm.regularVars.get(`cbrn_response_refund_status_@${id}`), ticks(constant('universal_cost_framework.result_rejected')));
      assert.equal(receipt(vm, 'total_refunded_costs', id), 0n);
      assert.equal(receipt(vm, 'states', id), ticks(1));
      assert(vm.array('universal_cost_component_refunded_states').every(n => n === 0n));
    }
    // Fixture repair allows the same real refund path to clear its diagnostic.
    vm.array('universal_cost_component_next_plus_one')[0] = savedNext;
    refund(vm); assert.deepEqual(snapshot(vm), initial);
    assert.equal(vm.regularVars.has(`cbrn_response_refund_status_@${id}`), false);
    assert.equal(receipt(vm, 'total_refunded_costs', id), ticks(15));
    const recoveredWrites = vm.nativeWrites.length; refund(vm); assert.equal(vm.nativeWrites.length, recoveredWrites);
    cases.push({ mode, corruption: 'first next pointer = 999', rejectedAttempts: 2, retainedStatus: 'result_rejected',
      afterRepair: snapshot(vm), nativeWrites: vm.nativeWrites });
  }
  return { cases };
});

scenario('stored-unrecorded-native-credit-retry-clears-exact-fields-and-refuses-repeat', () => {
  const cases = [];
  for (const mode of ['cold', 'warm']) for (const name of ['political_power', 'support_equipment_1', ...maskNames]) {
    const id = 700 + cases.length, key = name === 'political_power' ? 'pp' : `eq:${name}`;
    const vm = tx(new ResponseVM().balance(key, 20), id);
    if (mode === 'warm') warm(vm);
    // Execute the real debit API, then provide pending-credit storage as an
    // explicit recovery fixture. Native credit failure is not manufactured.
    vm.set('universal_cost_payment_resource_kind', kind(name)).set('universal_cost_payment_amount', 7)
      .set('universal_cost_payment_result', 0);
    assert(vm.run('universal_cost_pay_component')); assert.equal(vm.value('universal_cost_payment_result'), S);
    expectBalance(vm, key, 13);
    vm.write('cbrn_response_unrecorded_credit_amount_@var:cbrn_response_transaction', ticks(7), false);
    vm.write('cbrn_response_unrecorded_credit_kind_@var:cbrn_response_transaction', ticks(kind(name)), false);
    vm.write('cbrn_response_unrecorded_credit_amount_@9999', ticks(9), false);
    vm.write('cbrn_response_unrecorded_credit_kind_@9999', ticks(kind(name)), false);
    refund(vm); expectBalance(vm, key, 20); assert.equal(vm.nativeWrites.length, 2);
    assert.equal(vm.regularVars.has(`cbrn_response_unrecorded_credit_amount_@${id}`), false);
    assert.equal(vm.regularVars.has(`cbrn_response_unrecorded_credit_kind_@${id}`), false);
    expectNoProof(vm, id);
    assert.equal(vm.array('universal_cost_transaction_ids').length, 0, 'unrecorded recovery must not invent a receipt');
    assert.equal(vm.regularVars.get('cbrn_response_unrecorded_credit_amount_@9999'), ticks(9));
    assert.equal(vm.regularVars.get('cbrn_response_unrecorded_credit_kind_@9999'), ticks(kind(name)));
    refund(vm); refund(vm); expectBalance(vm, key, 20); assert.equal(vm.nativeWrites.length, 2);
    cases.push({ mode, resource: name, kind: String(kind(name)), pendingAmountFixture: 7,
      retryRestoredBalance: 20, repeatAttempts: 2, nativeWrites: vm.nativeWrites });
  }
  return { cases, boundary: 'The pending amount/kind creation branch after native credit failure is not exercised. Native kind credits succeed in the parsed API.' };
});

// Re-read every loaded file and require equality for executed bodies. Whole-file
// edits elsewhere are reported separately, never silently treated as one revision.
for (const [file, source] of sources) {
  const final = fs.readFileSync(path.join(root, file), 'utf8');
  const bodies = parse(source).filter(n => selected.has(n.key));
  const currentBodies = parse(final).filter(n => selected.has(n.key));
  const unchanged = JSON.stringify(bodies) === JSON.stringify(currentBodies);
  results.concurrentSources[file] = { capturedSha256: sha(source), finalSha256: sha(final), wholeFileChanged: source !== final,
    selectedBodiesUnchanged: unchanged };
  for (const node of bodies) results.selectedBodyHashes[node.key] = { file, astSha256: sha(JSON.stringify(node.value)) };
  if (!unchanged || (file === core.files[0] && source !== final)) results.scenarios.push({ id: `source-stability:${file}`, status: 'failed',
    error: 'Executed body or constant source changed during run. Retry on a stable snapshot.' });
}
results.reusedVMUnchanged = sha(fs.readFileSync(path.join(root, vmPath))) === capturedVMHash;
if (!results.reusedVMUnchanged) results.scenarios.push({ id: 'source-stability:reused-VM', status: 'failed', error: 'VM source changed during run.' });
for (const vm of instances) for (const [name, n] of vm.helperOutputChecks)
  results.helperOutputChecks[name] = (results.helperOutputChecks[name] || 0) + n;
results.scenarioCount = results.scenarios.length;
results.failedCount = results.scenarios.filter(s => s.status === 'failed').length;
results.helperReturns = instances.reduce((n, vm) => n + vm.helperReturns, 0);
results.droppedTemps = instances.reduce((n, vm) => n + vm.droppedTemps, 0);
results.status = results.failedCount ? 'failed' : 'passed';
fs.writeFileSync(resultPath, JSON.stringify(results, null, 2) + '\n');
console.log(JSON.stringify({ status: results.status, scenarioCount: results.scenarioCount, failedCount: results.failedCount,
  resultPath, failures: results.scenarios.filter(s => s.status === 'failed') }, null, 2));
if (results.failedCount) process.exitCode = 1;
