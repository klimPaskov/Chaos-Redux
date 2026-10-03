// Bounded actual caller scenarios. Reuses architect01a10115's source VM.
// No quote math, receipt algorithm, payment adapter, or engine proof is duplicated.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const cp = require('node:child_process');
const core = require('./exact_quote_source_tests.js');
const audit = require('./black_friday_outer_caller_contract_audit.js');
const { VM, S, ticks, definitions, constants, helperOutputs } = core;
const { root, sources, parsed, defs, field, files } = audit;
for (const [name, { node }] of defs) definitions.set(name, node.value);
for (const file of ['common/script_constants/026_black_friday_constants.txt',
  'common/script_constants/cbrn_system_constants.txt', 'common/script_constants/007_fury_constants.txt']) {
  // Only numeric tuning entries used by these callers. Broader schema list
  // grammar is outside the quotation VM's deliberately bounded parser.
  const text = fs.readFileSync(path.join(root, file), 'utf8');
  for (const category of text.matchAll(/^([a-z_0-9]+) = \{([\s\S]*?)^\}/gm)) {
    if (!['black_friday_event', 'fury_decision_cost', 'cbrn_protection_decision_cost'].includes(category[1])) continue;
    for (const item of category[2].matchAll(/^\s*([a-z_0-9]+) = (-?\d+(?:\.\d+)?)\s*(?:#[^\r\n]*)?$/gm))
      constants.set(`constant:${category[1]}.${item[1]}`, ticks(item[2]));
  }
}
// Only consumed public returns are required at an OUTER owner call. Internal
// exact producer boundaries keep the original VM's complete assertions.
class CallerVM extends VM {
  constructor() { super(); this.balances = new Map(); }
  run(name, bypass = false) {
    if (name === 'black_friday_quote_custom_cost') {
      assert(this.vars.has('black_friday_quote_final_cost'), 'caller lacks quote final output');
      return super.run(name, true);
    }
    return super.run(name, bypass);
  }
  eval(nodes) {
    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i];
      if (n.key === 'has_political_power' || n.key === 'command_power' || n.key === 'has_fuel' || n.key === 'has_equipment') {
        const check = n.key === 'has_equipment' ? n.value[0] : n;
        const resource = n.key === 'has_equipment' ? check.key : n.key;
        const balance = this.balances.get(resource) || 0n, amount = this.value(check.value);
        const accepted = check.op === '<' ? balance < amount : check.op === '>' ? balance > amount : balance === amount;
        if (!accepted) return false;
      } else {
        const group = [n];
        if (n.key === 'if') while (nodes[i+1] && ['else', 'else_if'].includes(nodes[i+1].key)) group.push(nodes[++i]);
        if (!super.eval(group)) return false;
      }
    }
    return true;
  }
}
const scenarios = [];
function scenario(id, f) { f(); scenarios.push(id); }
function quoteFixture(active = true, ratio = 5000) {
  const vm = new CallerVM();
  for (const [key, value] of [['ids', 26], ['ratios', ratio], ['priorities', 500], ['eligibility_masks', 0]])
    vm.arrays.set(`global.universal_cost_source_${key}`, active ? [ticks(value)] : []);
  vm.set('global.universal_cost_custom_quote_cache_valid', 1);
  if (active) vm.flags.add('black_friday_active');
  for (const name of ['has_political_power', 'command_power', 'has_fuel', 'support_equipment_1']) vm.balances.set(name, ticks(100000));
  return vm;
}
function frame(name) { return definitions.get(name); }
function prefixBeforeCall(name, call) {
  const body = frame(name), i = body.findIndex(n => n.key === call);
  assert(i >= 0, `${name} -> ${call}`); return body.slice(0, i + 1);
}
scenario('all-scoped-caller-declarations-and-no-localisation-quote-calls', () => {
  assert.equal(audit.gaps.length, 0);
  assert.equal(audit.inventory.filter(x => x.file === files[2] && /quote|can_pay/.test(x.helper)).length, 0);
});
scenario('cold-and-warm-fury-arrays-before-clear-append-and-spend-wrapper', () => {
  const vm = new VM(), body = frame('black_friday_fury_pay_reinforcement_cost');
  const active = field(body.find(n => n.key === 'if').value, 'limit');
  assert(active);
  const branch = body.find(n => n.key === 'if').value.filter(n => n.key !== 'limit');
  const i = branch.findIndex(n => n.key === 'black_friday_fury_pay_prepared_bundle_active');
  const prepare = branch.slice(0, i);
  for (let repeat = 0; repeat < 2; repeat++) {
    assert(vm.eval(prepare));
    for (const name of ['black_friday_fury_component_ids', 'black_friday_fury_component_resource_kinds',
      'black_friday_fury_component_family_masks', 'black_friday_fury_component_ordinary_costs']) {
      assert.equal(vm.tempArrays.get(name).length, 2, `${name}: placeholder or stale row survived`);
    }
    assert(vm.tempArrays.get('black_friday_fury_component_ordinary_costs').every(x => x > 0n));
  }
  const bare = new VM(); assert(bare.run('black_friday_fury_begin_component_list'));
  assert(!bare.tempArrays.has('black_friday_fury_component_ids'), 'cold undeclared array must die on helper return');
});
scenario('actual-protection-wrapper-chain-cold-warm-and-sale-expiry', () => {
  // Execute the actual owner limit prefix, including its four caller declarations.
  const owner = frame('black_friday_pay_cbrn_recondition_masks');
  const limit = field(owner.find(n => n.key === 'if').value, 'limit');
  for (const active of [true, false]) {
    const vm = quoteFixture(active);
    for (let repeat = 0; repeat < 2; repeat++) {
      assert(vm.eval(limit));
      for (const suffix of ['ordinary_pp', 'ordinary_support', 'pp_cost', 'support_cost'])
        assert(vm.vars.has(`black_friday_cbrn_protection_pair_${suffix}`), `${suffix} lost across can_pay/quote/pair returns`);
      const ordinaryPP = vm.value('black_friday_cbrn_protection_pair_ordinary_pp');
      const ordinarySupport = vm.value('black_friday_cbrn_protection_pair_ordinary_support');
      assert(ordinaryPP > 0n && ordinarySupport > 0n, 'original owner inputs must be positive, not initializer zeros');
      const expected = amount => active ? ((amount + 2n*S-1n)/(2n*S))*S : amount;
      assert.equal(vm.value('black_friday_cbrn_protection_pair_pp_cost'), expected(ordinaryPP));
      assert.equal(vm.value('black_friday_cbrn_protection_pair_support_cost'), expected(ordinarySupport));
    }
  }
});
scenario('protection-required-component-shortage-and-missing-live-source-fail-closed', () => {
  const limit = field(frame('black_friday_pay_cbrn_recondition_masks').find(n => n.key === 'if').value, 'limit');
  const short = quoteFixture(); short.balances.set('support_equipment_1', 0n); assert.equal(short.eval(limit), false);
  const missing = quoteFixture(); missing.arrays.set('global.universal_cost_source_ids', []); assert.equal(missing.eval(limit), false);
});
scenario('negative-control-undeclared-protection-forwarded-prices-do-not-export', () => {
  const limit = field(frame('black_friday_pay_cbrn_recondition_masks').find(n => n.key === 'if').value, 'limit');
  const bare = quoteFixture();
  assert(bare.eval(limit.filter(n => n.key !== 'set_temp_variable')));
  assert.equal(bare.vars.has('black_friday_cbrn_protection_pair_pp_cost'), false);
  assert.equal(bare.vars.has('black_friday_cbrn_protection_pair_ordinary_pp'), false);
});
scenario('preserved-parent-lookup-and-proof-output-storage', () => {
  for (const row of audit.inventory.filter(x => x.file === files[0] && ['universal_cost_find_transaction_row', 'universal_cost_find_component_row'].includes(x.helper)))
    assert.equal(row.missing.length, 0);
  const body = frame('black_friday_record_achievement_transaction');
  const encoded = JSON.stringify(body);
  assert(encoded.includes('black_friday_purchase_receipt_proof_valid'));
  assert(encoded.includes('black_friday_purchase_has_non_political_paid_component'));
});
// Recover pre-patch tokens by removing only our marked declaration groups.
function originalTokens(source) {
  const stripped = source.replace(/^[\t ]*# Caller-owned cost API outputs\.\r?\n(?:[\t ]*(?:set_temp_variable|resize_temp_array) = \{[^\r\n]*\}\r?\n)+/gm, '');
  return stripped.replace(/#[^\r\n]*/g, '').match(/"[^"\r\n]*"|[{}=<>]|[^\s{}=<>]+/g) || [];
}
scenario('effects-preservation-beyond-the-parents-existing-20-declarations', () => {
  const before = core.parse(cp.execFileSync('git', ['show', `HEAD:${files[0]}`], { cwd: root, encoding: 'utf8' }));
  const current = core.parse(originalTokens(sources.get(files[0])).join(' '));
  let removed = 0;
  function clean(nodes) {
    const out = [];
    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i];
      // Existing parent patch: four lookup outputs at each transaction finder,
      // two at each component finder, and two achievement-proof exports.
      if (n.key === 'set_temp_variable') {
        const name = n.value[0].key;
        const look = nodes.slice(i+1, i+6).find(x => !['set_temp_variable'].includes(x.key));
        const lookup = look && ['universal_cost_find_transaction_row', 'universal_cost_find_component_row'].includes(look.key);
        const lookupOutput = ['universal_cost_transaction_found_index', 'universal_cost_transaction_lookup_result',
          'universal_cost_transaction_is_indexed', 'universal_cost_transaction_pointer',
          'universal_cost_component_found_index', 'universal_cost_component_lookup_result'].includes(name);
        if (lookup && lookupOutput) { removed++; continue; }
      }
      out.push({ ...n, value: Array.isArray(n.value) ? clean(n.value) : n.value });
    }
    return out;
  }
  // Compare lookup-cleaned structures with the matching baseline structures.
  // The two proof declarations are preserved explicitly and accounted below.
  const actual = clean(current), currentLookupCount = removed;
  const expected = clean(before), baselineLookupCount = removed - currentLookupCount;
  assert.equal(currentLookupCount - baselineLookupCount, 18, 'parent lookup storage declarations changed');
  function removeProofPair(nodes) {
    return nodes.map(n => n.key === 'black_friday_record_achievement_transaction' ? { ...n,
      value: n.value.map(child => child.key === 'if' ? { ...child, value: child.value.filter(x =>
        !(x.key === 'set_temp_variable' && ['black_friday_purchase_receipt_proof_valid',
          'black_friday_purchase_has_non_political_paid_component'].includes(x.value[0].key))) } : child) } : n);
  }
  assert.deepEqual(removeProofPair(actual), removeProofPair(expected), 'noninitialization effect logic changed');
  function proofCount(nodes) {
    const target = nodes.find(n => n.key === 'black_friday_record_achievement_transaction');
    return target.value.find(n => n.key === 'if').value.filter(n => n.key === 'set_temp_variable' &&
      ['black_friday_purchase_receipt_proof_valid', 'black_friday_purchase_has_non_political_paid_component'].includes(n.value[0].key)).length;
  }
  assert.equal(proofCount(actual) - proofCount(expected), 2, 'parent receipt-proof declarations changed');
});
scenario('trigger-preservation-outside-the-architect-owned-central-block', () => {
  const before = core.parse(cp.execFileSync('git', ['show', `HEAD:${files[1]}`], { cwd: root, encoding: 'utf8' }));
  const current = core.parse(originalTokens(sources.get(files[1])).join(' '));
  const outside = nodes => nodes.filter(n => n.key !== 'black_friday_quote_custom_cost');
  assert.deepEqual(outside(current), outside(before), 'noninitialization trigger logic changed');
  const central = defs.get('black_friday_quote_custom_cost').node;
  assert(!sources.get(files[1]).slice(central.start, central.end).includes('# Caller-owned cost API outputs.'), 'protected central block was patched');
});
scenario('scoped-localisation-is-byte-identical-to-the-captured-baseline', () => {
  const crypto = require('node:crypto');
  assert.equal(crypto.createHash('sha256').update(sources.get(files[2])).digest('hex'),
    '665dd28b4cb12380ace61fcbbab36a11e035da885ac5fa38b590a4fc2f17098e');
});
console.log(JSON.stringify({ scenarios, scenarioCount: scenarios.length, inspectedBoundaries: audit.inventory.length,
  evidence: 'actual caller fragments with architect-owned conservative VM, native affordability queries modeled only',
  limitations: 'No engine, full owner payment, save/reload, GUI render, or repository-wide caller acceptance proof' }, null, 2));
