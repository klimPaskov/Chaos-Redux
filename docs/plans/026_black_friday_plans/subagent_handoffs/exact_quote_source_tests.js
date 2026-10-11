// Execute the checked-in Clausewitz helpers under a bounded fixed-point model.
// This is source-semantic evidence, not an HOI4 or MCP engine emulator claim.
// Run: node docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const root = path.resolve(__dirname, '../../../..');
const S = 100000n, MAX = 214748364799999n;
const files = [
  'common/script_constants/chaosx_universal_cost_constants.txt',
  'common/scripted_effects/chaosx_universal_cost_effects.txt',
  'common/scripted_triggers/chaosx_universal_cost_exact_triggers.txt',
  'common/scripted_triggers/026_black_friday_triggers.txt',
];
function ticks(x) {
  const text = String(x), sign = text.startsWith('-') ? -1n : 1n;
  const [whole, fraction = ''] = text.replace(/^-/, '').split('.');
  assert(fraction.length <= 5, 'fixture must be a represented input');
  return sign * (BigInt(whole) * S + BigInt(fraction.padEnd(5, '0')));
}
function parse(source) {
  const tokens = source.replace(/#[^\r\n]*/g, '').match(/"[^"\r\n]*"|[{}=<>]|[^\s{}=<>]+/g) || [];
  let i = 0;
  function body(nested = false) {
    const nodes = [];
    while (i < tokens.length && tokens[i] !== '}') {
      const key = tokens[i++];
      // Native slots and other token lists contain bare atoms, not assignments.
      // Retain them structurally without teaching the arithmetic VM to execute them.
      if (!['=', '<', '>'].includes(tokens[i])) { nodes.push({ key, op: null, value: key, atom: true }); continue; }
      const op = tokens[i++];
      assert(['=', '<', '>'].includes(op), `parse ${key} ${op}`);
      let value = tokens[i++];
      if (value === '{') value = body(true);
      assert(value !== undefined, `missing ${key}`);
      nodes.push({ key, op, value });
    }
    if (nested) assert.equal(tokens[i++], '}');
    return nodes;
  }
  const result = body(); assert.equal(i, tokens.length); return result;
}
const sources = new Map(files.map(f => [f, fs.readFileSync(path.join(root, f), 'utf8')]));
const parsed = new Map([...sources].map(([f, source]) => [f, parse(source)]));
const constants = new Map();
for (const category of parsed.get(files[0])) {
  if (Array.isArray(category.value)) for (const item of category.value) {
    if (!Array.isArray(item.value)) constants.set(`constant:${category.key}.${item.key}`, ticks(item.value));
  }
}
const definitions = new Map();
for (const f of files.slice(1)) for (const node of parsed.get(f)) definitions.set(node.key, node.value);
const executedVMs = [];
class VM {
  constructor() {
    this.vars = new Map(); this.regularVars = new Map(); this.arrays = new Map(); this.tempArrays = new Map();
    this.flags = new Set(); this.ops = 0; this.maxAccumulator = 0n; this.helperReturns = 0; this.droppedTemps = 0;
    this.helperOutputChecks = new Map();
    executedVMs.push(this);
  }
  array(name) { return this.tempArrays.get(name) ?? this.arrays.get(name) ?? []; }
  key(name) {
    return name.replace(/@var:([a-zA-Z0-9_]+)/g, (_, selector) => {
      const value = this.value(selector); assert.equal(value % S, 0n, `noninteger targeted key ${name}`);
      return `@${value / S}`;
    });
  }
  value(token) {
    if (/^-?\d+(\.\d+)?$/.test(token)) return ticks(token);
    if (token === 'THIS') return 7n * S; // one existing selected payer scope
    if (constants.has(token)) return constants.get(token);
    assert(!token.startsWith('constant:'), `unknown script constant ${token}`);
    token = this.key(token);
    if (token.includes('^')) {
      const [name, index] = token.split('^'); const a = this.array(name);
      if (index === 'num') return BigInt(a.length) * S;
      const j = this.value(index); assert.equal(j % S, 0n, `fractional index ${token}`);
      const n = Number(j / S);
      assert(n >= 0 && n < a.length, `absent array element ${token} at ${n}/${a.length}`);
      return a[n];
    }
    return this.vars.get(token) ?? this.regularVars.get(token) ?? 0n;
  }
  write(name, value, temporary = true) {
    name = this.key(name);
    assert(value <= MAX && value >= -MAX, `overflow ${name}=${value}`);
    if (name === 'uc_exact_accumulator' || name === 'uc_exact_trial_accumulator') {
      if (value > this.maxAccumulator) this.maxAccumulator = value;
    }
    if (name.includes('^')) {
      const [array, index] = name.split('^'), a = (temporary ? this.tempArrays : this.arrays).get(array);
      const j = this.value(index); assert.equal(j % S, 0n);
      const n = Number(j / S); assert(a && n >= 0 && n < a.length, `write ${name}`); a[n] = value;
    } else (temporary ? this.vars : this.regularVars).set(name, value);
  }
  set(name, value) { this.write(name, ticks(value), !name.startsWith('global.')); return this; }
  tempArray(name, values = [0n]) { this.tempArrays.set(name, values); return this; }
  field(nodes, key, fallback) { const n = nodes.find(n => n.key === key); return n ? n.value : fallback; }
  run(name, allowUninitializedCaller = false) {
    assert(definitions.has(name), `missing helper ${name}`);
    const contract = helperOutputs[name];
    if (contract && !allowUninitializedCaller) {
      for (const key of contract.vars) assert(this.vars.has(key), `caller lacks temporary output ${key} before ${name}`);
      for (const key of contract.arrays) assert(this.tempArrays.has(key), `caller lacks temporary array output ${key} before ${name}`);
      this.helperOutputChecks.set(name, (this.helperOutputChecks.get(name) || 0) + 1);
    }
    // ALL scripted calls, including public APIs, get conservative lexical frames.
    // Existing temporary names retain modifications. Newly created names die.
    // Regular writes remain persistent and are never included in this cleanup.
    const inheritedVars = new Set(this.vars.keys()), inheritedArrays = new Set(this.tempArrays.keys());
    try { return this.eval(definitions.get(name)); }
    finally {
      for (const key of this.vars.keys()) if (!inheritedVars.has(key)) { this.vars.delete(key); this.droppedTemps++; }
      for (const key of this.tempArrays.keys()) if (!inheritedArrays.has(key)) {
        this.tempArrays.delete(key); this.droppedTemps++;
      }
      this.helperReturns++;
    }
  }
  call(name) {
    // Explicit OUTER caller storage only: no internal scratch is preseeded.
    // This models the documented API contract; it does not repair owner source.
    const contract = callerOutputs[name] || { vars: [], arrays: [] };
    const declarations = [
      ...contract.vars.filter(key => !this.vars.has(key)).map(key => `set_temp_variable = { ${key} = 0 }`),
      ...contract.arrays.filter(key => !this.tempArrays.has(key)).map(key => `resize_temp_array = { array = ${key} size = 1 }`),
    ].join('\n');
    assert(this.eval(parse(declarations)));
    return this.run(name);
  }
  eval(nodes) {
    for (let i = 0; i < nodes.length; i++) {
      const { key: k, value: v, op } = nodes[i]; this.ops++;
      if (k === 'if') {
        let accepted = this.eval(this.field(v, 'limit', []));
        if (accepted && !this.eval(v.filter(n => n.key !== 'limit'))) return false;
        while (nodes[i + 1] && ['else_if', 'else'].includes(nodes[i + 1].key)) {
          const next = nodes[++i];
          if (!accepted) {
            const yes = next.key === 'else' || this.eval(this.field(next.value, 'limit', []));
            if (yes) { accepted = true; if (!this.eval(next.value.filter(n => n.key !== 'limit'))) return false; }
          }
        }
      } else if (k === 'always') { if (v !== 'yes') return false; }
      else if (k === 'NOT') { if (v.some(n => this.eval([n]))) return false; }
      else if (k === 'OR') { if (!v.some(n => this.eval([n]))) return false; }
      else if (k === 'AND' || k === 'hidden_trigger') { if (!this.eval(v)) return false; }
      else if (k === 'has_global_flag') { if (!this.flags.has(v)) return false; }
      else if (k === 'has_variable') { if (!this.vars.has(this.key(v)) && !this.regularVars.has(this.key(v))) return false; }
      else if (k === 'check_variable') {
        const long = this.field(v, 'var');
        const left = this.value(long || v[0].key);
        const right = this.value(long ? this.field(v, 'value') : v[0].value);
        const compare = this.field(v, 'compare', (long ? '=' : v[0].op));
        const yes = ({ '=': left === right, equals: left === right,
          not_equals: left !== right, '<': left < right, less_than: left < right, '>': left > right, greater_than: left > right,
          less_than_or_equals: left <= right, greater_than_or_equals: left >= right })[compare];
        assert(yes !== undefined, `compare ${compare}`); if (!yes) return false;
      } else if (k === 'while_loop_effect') {
        const limit = this.field(v, 'limit', []), body = v.filter(n => n.key !== 'limit');
        let iterations = 0;
        while (iterations < 1000 && this.eval(limit)) { if (!this.eval(body)) return false; iterations++; }
      } else if (k === 'all_of') {
        // Numeric iteration retains THIS and allows replacing existing slots.
        // Array length stays fixed throughout the token-fill pass.
        const name = this.field(v, 'array'), a = this.array(name), length = a.length;
        const valueName = this.field(v, 'value', 'v'), indexName = this.field(v, 'index', 'i');
        const body = v.filter(n => !['array', 'value', 'index'].includes(n.key));
        for (let index = 0; index < length; index++) {
          this.write(valueName, a[index]); this.write(indexName, BigInt(index) * S);
          if (!this.eval(body)) return false;
          assert.equal(a.length, length, 'fill must preserve array length');
        }
      } else if (k === 'all_of_scopes') {
        const name = this.field(v, 'array'), a = this.array(name);
        const snapshot = [...a]; // arrays are ordered and preserve repeated scope values
        const body = v.filter(n => n.key !== 'array' && n.key !== 'tooltip');
        for (const scope of snapshot) {
          assert.equal(scope, 7n * S, `iteration token must be THIS, ${name}`);
          if (!this.eval(body)) return false;
        }
        assert.deepEqual(a, snapshot, `mutated traversed iteration tokens ${name}`);
      } else if (k === 'clear_temp_array' || k === 'clear_array') {
        (k === 'clear_temp_array' ? this.tempArrays : this.arrays).set(v, []);
      }
      else if (k === 'resize_temp_array' || k === 'resize_array') {
		const arrayStore = k === 'resize_temp_array' ? this.tempArrays : this.arrays;
        const name = this.field(v, 'array', v[0].key), size = this.value(this.field(v, 'size', v[0].value));
        assert.equal(size % S, 0n); const n = Number(size / S); assert(n >= 0);
        const a = arrayStore.get(name) || [], value = this.value(this.field(v, 'value', '0'));
        while (a.length < n) a.push(value); a.length = n; arrayStore.set(name, a);
      } else if (k === 'add_to_temp_array' || k === 'add_to_array') {
        const map = k === 'add_to_temp_array' ? this.tempArrays : this.arrays;
        const name = this.field(v, 'array'), a = map.get(name) || [];
        a.push(this.value(this.field(v, 'value'))); map.set(name, a);
      } else if (k === 'remove_from_temp_array' || k === 'remove_from_array') {
        const name = this.field(v, 'array'), a = (k === 'remove_from_temp_array' ? this.tempArrays : this.arrays).get(name) || [];
        const index = this.field(v, 'index'); const n = index === undefined ? a.length - 1 : Number(this.value(index) / S);
        assert(n >= 0 && n < a.length); a.splice(n, 1);
      } else if (k === 'clear_variable') this.regularVars.delete(this.key(v));
      else if (k === 'is_in_array') {
        const a = this.array(this.field(v, 'array'));
        if (!a.includes(this.value(this.field(v, 'value')))) return false;
      } else if (['set_temp_variable', 'set_variable', 'add_to_temp_variable', 'subtract_from_temp_variable',
        'multiply_temp_variable', 'divide_temp_variable', 'modulo_temp_variable'].includes(k)) {
        const long = this.field(v, 'var'), name = long || v[0].key;
        const b = this.value(long ? this.field(v, 'value') : v[0].value);
        const a = k.startsWith('set_') ? 0n : this.value(name);
        let result;
        if (k.startsWith('set_')) result = b;
        else if (k.startsWith('add_')) result = a + b;
        else if (k.startsWith('subtract_')) result = a - b;
        else if (k.startsWith('multiply_')) {
          assert.equal(a * b % S, 0n, `multiplication lost fractional precision ${name}`); result = a * b / S;
        } else if (k.startsWith('divide_')) {
          assert(b !== 0n, `zero divisor ${name}`);
          assert.equal(a * S % b, 0n, `division lost fractional precision ${name}`); result = a * S / b;
        } else { assert(b > 0n); result = ((a % b) + b) % b; }
        this.write(name, result, k !== 'set_variable');
      } else if (definitions.has(k)) {
        const yes = this.run(k); if ((v === 'no' && yes) || (v !== 'no' && !yes)) return false;
      } else throw Error(`unsupported tested command ${k} ${op}`);
    }
    return true;
  }
}
const quoteOutputs = ['universal_cost_quote_final_cost', 'universal_cost_quote_displayed_cost', 'universal_cost_quote_saved_cost',
  'universal_cost_quote_valid', 'universal_cost_quote_source_count', 'universal_cost_quote_primary_source_id',
  'universal_cost_quote_composed_ratio', 'universal_cost_quote_rounding_quantum'];
const callerOutputs = {
  universal_cost_quote_exact: { vars: quoteOutputs, arrays: [] },
  universal_cost_quote_integer: { vars: quoteOutputs, arrays: [] },
  black_friday_quote_custom_cost: { vars: [...quoteOutputs, 'black_friday_quote_final_cost', 'black_friday_quote_valid',
    'black_friday_quote_composed_ratio', 'black_friday_quote_rounding_quantum', 'black_friday_quote_requested_quantum'], arrays: [] },
  universal_cost_round_up_to_quantum: { vars: ['universal_cost_quantize_result', 'universal_cost_quantize_valid',
    'universal_cost_quantize_units', 'universal_cost_quantize_units_valid', 'universal_cost_quantize_quantum'], arrays: ['uc_exact_units'] },
  universal_cost_source_register: { vars: ['universal_cost_source_register_result'], arrays: [] },
  universal_cost_source_clear: { vars: ['universal_cost_source_clear_result'], arrays: [] },
  universal_cost_source_register_black_friday: { vars: ['universal_cost_source_register_result'], arrays: [] },
  universal_cost_source_clear_black_friday: { vars: ['universal_cost_source_clear_result'], arrays: [] },
  universal_cost_check_quote_affordable: { vars: ['universal_cost_quote_affordable'], arrays: [] },
  universal_cost_source_matches_quote_family: { vars: ['universal_cost_source_matches_quote'], arrays: [] },
};
// Every temporary export/in-out array in the exact helper call graph is checked
// at helper ENTRY. This audit never creates storage or seeds internal scratch.
const helperOutputs = {
  ...callerOutputs,
  black_friday_quote_custom_cost: { vars: ['black_friday_quote_final_cost', 'black_friday_quote_valid',
    'black_friday_quote_composed_ratio', 'black_friday_quote_rounding_quantum'], arrays: [] },
  universal_cost_exact_scalar_to_ticks: { vars: [], arrays: ['uc_exact_factor'] },
  universal_cost_exact_multiply: { vars: [], arrays: ['uc_exact_product'] },
  universal_cost_exact_trim_product: { vars: [], arrays: ['uc_exact_product'] },
  universal_cost_exact_match_family: { vars: ['universal_cost_source_matches_quote'], arrays: [] },
  universal_cost_exact_find_source: { vars: ['universal_cost_source_found_index'], arrays: [] },
  universal_cost_exact_division_trial: { vars: ['uc_exact_comparison'], arrays: ['uc_exact_trial_product'] },
  universal_cost_exact_quantize_product: { vars: ['uc_exact_scalar_result', 'uc_exact_scalar_valid'],
    arrays: ['uc_exact_product', 'uc_exact_units', 'uc_exact_units_tokens'] },
  universal_cost_exact_ticks_to_scalar: { vars: ['uc_exact_scalar_result', 'uc_exact_scalar_valid'], arrays: ['uc_exact_product'] },
  universal_cost_exact_quantize_scalar: callerOutputs.universal_cost_round_up_to_quantum,
};
const rows = (...ratios) => ratios.map((ratio, i) => ({ id: 26 + i, ratio: String(ratio), priority: 500 - i, mask: 0 }));
function fixture(cost, quantum, family, sourceRows) {
  const vm = new VM().set('universal_cost_quote_ordinary_cost', cost).set('universal_cost_quote_rounding_quantum', quantum)
    .set('universal_cost_quote_family_mask', family).set('global.universal_cost_custom_quote_cache_valid', 1);
  for (const [suffix, key] of [['ids', 'id'], ['ratios', 'ratio'], ['priorities', 'priority'], ['eligibility_masks', 'mask']])
    vm.arrays.set(`global.universal_cost_source_${suffix}`, sourceRows.map(r => ticks(r[key])));
  vm.flags.add('black_friday_active'); return vm;
}
// Independent direct BigInt rational oracle: no limbs, schedules or VM helpers.
function oracle(cost, quantum, family, sourceRows) {
  const c = ticks(cost), q = ticks(quantum) > 0n ? ticks(quantum) : S;
  const eligible = sourceRows.filter(r => r.id > 0 && ticks(r.ratio) > 0n && ticks(r.ratio) <= 10000n * S &&
    family > 0 && (r.mask === 0 || (BigInt(r.mask) & BigInt(family)) !== 0n));
  if (c <= 0n || eligible.length === 0) return { price: c, valid: true, count: 0, primary: 0 };
  let numerator = c, denominator = q;
  for (const r of eligible) { numerator *= ticks(r.ratio); denominator *= 1000000000n; }
  const price = ((numerator + denominator - 1n) / denominator) * q;
  const primary = eligible.reduce((a, b) => b.priority < a.priority ? b : a).id;
  return { price, valid: price <= MAX, count: eligible.length, primary };
}
// Receipt tests reuse this SAME interpreter and real shared API definitions.
// Importing the module does not run or mock the quotation test suite.
module.exports = { VM, S, MAX, ticks, parse, root, files, sources, definitions, constants, callerOutputs, helperOutputs, fixture, oracle };
if (require.main === module) {
const summary = { sourceHashes: Object.fromEntries([...sources].map(([f, s]) => [f, crypto.createHash('sha256').update(s).digest('hex')])),
  quoteScenarios: 0, quantizerScenarios: 0, mutations: 0, maxBoundedAccumulator: '0', operations: 0,
  lifetimeModel: 'ALL scripted calls drop newly created temporary variables/arrays and retain caller temporaries plus regular storage',
  helperOutputContracts: helperOutputs, callerOutputDeclarations: callerOutputs, helperOutputChecks: {}, helperReturns: 0, droppedTemps: 0, results: [] };
function recordLifetime(vm) {
  summary.helperReturns += vm.helperReturns; summary.droppedTemps += vm.droppedTemps;
  for (const [key, n] of vm.helperOutputChecks) summary.helperOutputChecks[key] = (summary.helperOutputChecks[key] || 0) + n;
}
function check(id, cost, quantum, family, sourceRows, bridge = true) {
  const expected = oracle(cost, quantum, family, sourceRows);
  const frontends = ['universal_cost_quote_exact', 'universal_cost_quote_integer'];
  if (bridge) frontends.push('black_friday_quote_custom_cost');
  for (const entry of frontends) {
    const vm = fixture(cost, quantum, family, sourceRows);
    vm.set('black_friday_quote_ordinary_cost', cost).set('black_friday_quote_family_mask', family).set('black_friday_quote_requested_quantum', quantum);
    const success = vm.call(entry), bf = entry.startsWith('black_friday');
    assert.equal(success, bf ? expected.valid : true, `${id} ${entry} result`);
    assert.equal(vm.value(bf ? 'black_friday_quote_valid' : 'universal_cost_quote_valid'), expected.valid ? S : 0n, `${id} validity`);
    if (expected.valid) {
      assert.equal(vm.value(bf ? 'black_friday_quote_final_cost' : 'universal_cost_quote_final_cost'), expected.price, `${id} ${entry} price`);
      assert.equal(vm.value('universal_cost_quote_displayed_cost'), expected.price, `${id} displayed`);
      assert.equal(vm.value('universal_cost_quote_source_count'), BigInt(expected.count) * S, `${id} count`);
      assert.equal(vm.value('universal_cost_quote_primary_source_id'), BigInt(expected.primary) * S, `${id} source`);
      const saved = ticks(cost) > expected.price ? ticks(cost) - expected.price : 0n;
      assert.equal(vm.value('universal_cost_quote_saved_cost'), saved, `${id} savings`);
    }
    if (vm.maxAccumulator > BigInt(summary.maxBoundedAccumulator)) summary.maxBoundedAccumulator = String(vm.maxAccumulator);
    summary.operations += vm.ops;
  }
  summary.quoteScenarios++;
  summary.results.push({ id, cost: String(cost), quantum: String(quantum), family, sourceCount: sourceRows.length,
    expectedTicks: String(expected.price), valid: expected.valid });
}
for (const cost of ['0', '0.00001', '0.04001', '1', '2', '2.00001', '3', '5', '101', '125', '1000000', '2147483647.99999'])
  for (const ratio of ['5000', '2500']) for (const quantum of ['1', '0.01', '0.00001', '0.00003', '0.12345', '1000000.00001'])
    check(`single-${cost}-${ratio}-${quantum}`, cost, quantum, 1, rows(ratio));
for (const cost of ['0.00001', '2', '6', '1000000']) for (const quantum of ['1', '0.01', '0.00003', '3.14159']) {
  for (const ratios of [['9999.99999', '5000.00001'], ['5000', '3333.33335'], ['5000', '0.001', '0.001'],
    ['0.00001', '9999.99999', '2500', '8000.00001']]) {
    const r = rows(...ratios); check(`compose-${cost}-${quantum}-${ratios}`, cost, quantum, 1, r);
    check(`reverse-${cost}-${quantum}-${ratios}`, cost, quantum, 1, [...r].reverse());
  }
}
for (const family of [1, 2, 3, 4, 16, 32, 64, 112, 512, 1024, 4096, 134217728, 536870912, 1073741823]) {
  const r = [{ id: 26, ratio: '5000', priority: 500, mask: 1 }, { id: 41, ratio: '3333.33335', priority: 200, mask: 536870912 },
    { id: 52, ratio: '9999.99999', priority: 200, mask: 16 + 32 }, { id: 53, ratio: '5000.00001', priority: 200, mask: 0 }];
  check(`mask-${family}`, '101.00001', '0.00007', family, r);
}
for (const cost of ['0', '-0.00001', '-5', '0.00001', '0.5', '125', '1000000']) {
  check(`no-source-${cost}`, cost, '0.12345', 1, []);
  check(`excluded-${cost}`, cost, '0.12345', 2, [{ id: 26, ratio: '5000', priority: 500, mask: 1 }]);
  check(`zero-family-${cost}`, cost, '0.12345', 0, rows('5000'), false);
}
check('many-identities', '2.00001', '1', 1, Array.from({ length: 1105 }, (_, i) => ({ id: 26 + i, ratio: '10000', priority: 500, mask: 0 })));
check('long-product', '1000000', '0.00003', 1, rows(...Array(120).fill('9999.99999')));
check('tiny-product', '1000000', '0.00001', 1, rows(...Array(80).fill('0.00001')));
check('unrepresentable-output', '2147483647.99999', '2000000000', 1, rows('10000'));
check('exact-max-envelope', '2147483647.99999', '0.00001', 1, rows('10000'));
check('priority-tie', '2', '1', 1, [{ id: 90, ratio: '5000', priority: 1, mask: 0 }, { id: 26, ratio: '5000', priority: 1, mask: 0 }]);
check('many-nonidentities', '1000000', '0.00003', 1, rows(...Array(1105).fill('0.00001')));
// Exercise multiplication iteration arrays with more than 1,000 actual limbs.
const wide = new VM();
wide.tempArray('uc_exact_product', Array(1005).fill(999n * S));
wide.tempArray('uc_exact_factor', [999n * S]);
assert(wide.call('universal_cost_exact_multiply'));
const wideValue = wide.tempArrays.get('uc_exact_product').reduceRight((a, digit) => a * 1000n + digit / S, 0n);
assert.equal(wideValue, (1000n ** 1005n - 1n) * 999n);
summary.wideMultiplyLimbs = 1005;
// A deterministic sweep uses direct rational expectations, never a limb oracle.
let seed = 261003;
const next = () => (seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0);
const decimal = n => `${n / S}.${String(n % S).padStart(5, '0')}`;
for (let i = 0; i < 120; i++) {
  const cost = decimal(BigInt(next()) * 49999n + BigInt(next() % 100000));
  const quantum = decimal(BigInt(next()) * 4321n + 1n);
  const r = Array.from({ length: 1 + next() % 5 }, (_, j) => ({ id: 26 + j,
    ratio: decimal(1n + BigInt(next() % 1000000000)), priority: next() % 900000, mask: next() % 16 }));
  check(`sweep-${i}`, cost, quantum, 1 + next() % 15, r);
}
// Existing family defaults and consumed generic override cannot leak across calls.
const defaults = fixture('0.04001', '1', 67108864, rows('2500'));
defaults.set('black_friday_quote_ordinary_cost', '0.04001').set('black_friday_quote_family_mask', 67108864);
assert(defaults.call('black_friday_quote_custom_cost'));
assert.equal(defaults.value('black_friday_quote_final_cost'), ticks('0.02'));
defaults.set('black_friday_quote_family_mask', 134217728);
assert(defaults.call('black_friday_quote_custom_cost'));
assert.equal(defaults.value('black_friday_quote_final_cost'), ticks('0.02'));
defaults.set('black_friday_quote_requested_quantum', '0.00003');
assert(defaults.call('black_friday_quote_custom_cost'));
assert.equal(defaults.value('black_friday_quote_final_cost'), ticks('0.01002'));
assert(defaults.call('black_friday_quote_custom_cost'));
assert.equal(defaults.value('black_friday_quote_final_cost'), ticks('0.02'));
defaults.set('black_friday_quote_family_mask', 512);
assert(defaults.call('black_friday_quote_custom_cost'));
assert.equal(defaults.value('black_friday_quote_final_cost'), ticks('1'));
summary.crossCallChecks = 5;
for (const frontend of ['universal_cost_quote_exact', 'universal_cost_quote_integer']) {
  const optional = fixture('2.00001', '1', 1, rows('5000'));
  optional.vars.delete('universal_cost_quote_rounding_quantum');
  assert(optional.call(frontend)); assert.equal(optional.value('universal_cost_quote_final_cost'), ticks('2'));
}
const optionalQuantum = new VM().set('universal_cost_quantize_amount', '2.00001');
optionalQuantum.set('universal_cost_quote_rounding_quantum', '0.12345');
assert(optionalQuantum.call('universal_cost_round_up_to_quantum'));
assert.equal(optionalQuantum.value('universal_cost_quantize_result'), ticks('3'));
assert.equal(optionalQuantum.value('universal_cost_quote_rounding_quantum'), ticks('0.12345'));
summary.optionalQuantumChecks = 3;
// HOI4 NOT is NOR over sibling triggers. An explicit AND is required to
// negate a conjunction, and this distinction is independent of price math.
for (const a of [false, true]) for (const b of [false, true]) {
  const vm = new VM();
  definitions.set('vm_boolean_nor', parse(`NOT = { always = ${a ? 'yes' : 'no'} always = ${b ? 'yes' : 'no'} }`));
  definitions.set('vm_boolean_nand', parse(`NOT = { AND = { always = ${a ? 'yes' : 'no'} always = ${b ? 'yes' : 'no'} } }`));
  assert.equal(vm.run('vm_boolean_nor'), !(a || b));
  assert.equal(vm.run('vm_boolean_nand'), !(a && b));
}
summary.booleanTruthTableChecks = 8;
const alignedData = ['ratios', 'priorities', 'eligibility_masks'];
let malformedChecks = 0;
function rejectMisalignment(changes) {
  for (const frontend of ['universal_cost_quote_exact', 'universal_cost_quote_integer', 'black_friday_quote_custom_cost']) {
    const vm = fixture('3', '1', 1, rows('5000'));
    for (const [suffix, length] of changes) {
      const array = vm.arrays.get(`global.universal_cost_source_${suffix}`);
      if (length === 0) array.pop(); else array.push(0n);
    }
    vm.set('black_friday_quote_ordinary_cost', '3').set('black_friday_quote_family_mask', 1).set('black_friday_quote_requested_quantum', 1);
    assert.equal(vm.call(frontend), frontend === 'black_friday_quote_custom_cost' ? false : true);
    assert.equal(vm.value(frontend === 'black_friday_quote_custom_cost' ? 'black_friday_quote_valid' : 'universal_cost_quote_valid'), 0n);
    assert(vm.call('universal_cost_check_quote_affordable'));
    assert.equal(vm.value('universal_cost_quote_affordable'), 0n);
    recordLifetime(vm); malformedChecks++;
  }
}
for (let pattern = 0; pattern < 27; pattern++) {
  let encoded = pattern;
  const changes = [];
  for (const suffix of alignedData) {
    const length = encoded % 3; encoded = Math.floor(encoded / 3);
    if (length !== 1) changes.push([suffix, length]);
  }
  if (changes.length) rejectMisalignment(changes);
}
rejectMisalignment([['ids', 0]]);
rejectMisalignment([['ids', 2]]);
assert.equal(malformedChecks, 84);
summary.malformedRegistryGateChecks = malformedChecks;
// Malformed aligned storage and nonrepresentable price fail the quoted gate.
const malformed = fixture('3', '1', 1, rows('5000'));
malformed.arrays.set('global.universal_cost_source_ratios', []);
assert(malformed.call('universal_cost_quote_integer'));
assert.equal(malformed.value('universal_cost_quote_valid'), 0n);
assert(malformed.call('universal_cost_check_quote_affordable'));
assert.equal(malformed.value('universal_cost_quote_affordable'), 0n);
const impossible = fixture('2147483647.99999', '2000000000', 1, rows('10000'));
assert(impossible.call('universal_cost_quote_integer'));
assert(impossible.call('universal_cost_check_quote_affordable'));
assert.equal(impossible.value('universal_cost_quote_affordable'), 0n);
summary.invalidQuoteGateChecks = 2;
for (const cost of ['0', '-5', '0.00001', '0.04001', '2.00001', '125', '1000000', '2147483647.99999'])
  for (const quantum of ['1', '0.01', '0.00001', '0.00003', '0.12345', '0', '-1']) {
    const vm = new VM().set('universal_cost_quantize_amount', cost).set('universal_cost_quantize_quantum', quantum);
    assert(vm.call('universal_cost_round_up_to_quantum'));
    const c = ticks(cost), q = ticks(quantum) > 0n ? ticks(quantum) : S;
    const expected = c <= 0n ? c : ((c + q - 1n) / q) * q;
    assert.equal(vm.value('universal_cost_quantize_valid'), expected <= MAX ? S : 0n);
    if (expected <= MAX) assert.equal(vm.value('universal_cost_quantize_result'), expected);
    const units = c <= 0n ? 0n : (c + q - 1n) / q;
    assert.equal(vm.value('universal_cost_quantize_units_valid'), units * S <= MAX ? S : 0n);
    if (units * S <= MAX) assert.equal(vm.value('universal_cost_quantize_units'), units * S);
    const exactUnits = vm.tempArrays.get('uc_exact_units').reduceRight((a, digit) => a * 1000n + digit / S, 0n);
    assert.equal(exactUnits, units, 'temporary unit limbs survive the public API return');
    summary.quantizerScenarios++;
  }
// Actual register/upsert/clear and cache lifecycle, with payer receipts untouched.
const vm = fixture('2', '1', 1, []);
vm.set('global.universal_cost_custom_quote_ratio_political_power', '5000');
vm.arrays.set('universal_cost_component_actual_paid_costs', [ticks('1')]);
vm.arrays.set('universal_cost_transaction_ids', [ticks('12')]);
for (const r of [{ id: 26, ratio: '9999.99999', priority: 500, mask: 0 }, { id: 45, ratio: '5000.00001', priority: 200, mask: 0 }]) {
  vm.set('universal_cost_source_id', r.id).set('universal_cost_source_ratio', r.ratio).set('universal_cost_source_priority', r.priority)
    .set('universal_cost_source_eligibility_mask', r.mask);
  assert(vm.call('universal_cost_source_register')); summary.mutations++;
}
assert(vm.call('universal_cost_quote_integer')); assert.equal(vm.value('universal_cost_quote_final_cost'), ticks('2'));
vm.set('universal_cost_source_id', 26); assert(vm.call('universal_cost_source_clear')); summary.mutations++;
assert.equal(vm.value('global.universal_cost_custom_quote_cache_valid'), 0n);
assert.equal(vm.regularVars.has('global.universal_cost_custom_quote_ratio_political_power'), false);
assert.deepEqual(vm.arrays.get('global.universal_cost_source_ids'), [ticks('45')]);
assert(vm.call('universal_cost_quote_integer')); assert.equal(vm.value('universal_cost_quote_final_cost'), ticks('2'));
vm.set('black_friday_quote_ordinary_cost', '2').set('black_friday_quote_family_mask', 1);
assert.equal(vm.call('black_friday_quote_custom_cost'), false);
vm.set('universal_cost_source_ratio', '5000').set('universal_cost_source_priority', 500).set('universal_cost_source_eligibility_mask', 0);
assert(vm.call('universal_cost_source_register')); summary.mutations++;
assert(vm.call('universal_cost_quote_integer')); assert.equal(vm.value('universal_cost_quote_final_cost'), ticks('1'));
vm.set('universal_cost_source_id', 45); assert(vm.call('universal_cost_source_clear')); summary.mutations++;
assert.deepEqual(vm.arrays.get('global.universal_cost_source_ids'), [ticks('26')]);
assert.equal(vm.value('global.universal_cost_custom_quote_cache_valid'), S);
assert.deepEqual(vm.arrays.get('universal_cost_component_actual_paid_costs'), [ticks('1')]);
assert.deepEqual(vm.arrays.get('universal_cost_transaction_ids'), [ticks('12')]);
const large = fixture('1', '1', 1, Array.from({ length: 1105 }, (_, i) => ({ id: 26 + i, ratio: '10000', priority: 500, mask: 0 })));
large.set('universal_cost_source_id', 1130).set('universal_cost_source_ratio', '2500').set('universal_cost_source_priority', 0)
  .set('universal_cost_source_eligibility_mask', 536870912);
assert(large.call('universal_cost_source_register')); summary.mutations++;
assert.equal(large.arrays.get('global.universal_cost_source_ratios')[1104], ticks('2500'));
assert(large.call('universal_cost_source_clear')); summary.mutations++;
assert.equal(large.arrays.get('global.universal_cost_source_ids').length, 1104);
const expiry = fixture('125', '1', 1, rows('5000', '5000'));
expiry.arrays.set('universal_cost_component_actual_paid_costs', [ticks('32')]);
assert(expiry.call('universal_cost_quote_integer'));
assert.equal(expiry.value('universal_cost_quote_final_cost'), oracle('125', '1', 1, rows('5000', '5000')).price);
expiry.set('universal_cost_source_id', 26); assert(expiry.call('universal_cost_source_clear')); summary.mutations++;
assert(expiry.call('universal_cost_quote_integer'));
assert.equal(expiry.value('universal_cost_quote_final_cost'), oracle('125', '1', 1, rows('5000')).price);
assert.deepEqual(expiry.arrays.get('universal_cost_component_actual_paid_costs'), [ticks('32')]);
expiry.set('universal_cost_source_id', 27); assert(expiry.call('universal_cost_source_clear')); summary.mutations++;
assert(expiry.call('universal_cost_quote_integer')); assert.equal(expiry.value('universal_cost_quote_final_cost'), ticks('125'));
assert.deepEqual(expiry.arrays.get('universal_cost_component_actual_paid_costs'), [ticks('32')]);
summary.expiryPrices = ['32', '63', '125'];
const noOpArrays = JSON.stringify([...expiry.arrays].filter(([name]) => name.startsWith('global.')), (_, v) => typeof v === 'bigint' ? String(v) : v);
expiry.set('universal_cost_source_id', 888); assert(expiry.call('universal_cost_source_clear'));
assert.equal(expiry.value('universal_cost_source_clear_result'), 0n);
expiry.set('universal_cost_source_ratio', 0).set('universal_cost_source_priority', 0).set('universal_cost_source_eligibility_mask', 0);
assert(expiry.call('universal_cost_source_register')); assert.equal(expiry.value('universal_cost_source_register_result'), 0n);
assert.equal(JSON.stringify([...expiry.arrays].filter(([name]) => name.startsWith('global.')), (_, v) => typeof v === 'bigint' ? String(v) : v), noOpArrays);
summary.noOpMutationChecks = 2;
// Public wrappers must preserve nested registration-result outputs as well.
const wrappers = fixture('3', '1', 1, []);
wrappers.set('universal_cost_source_ratio', 5000).set('universal_cost_source_eligibility_mask', 0);
assert(wrappers.call('universal_cost_source_register_black_friday'));
assert.equal(wrappers.value('universal_cost_source_register_result'), S);
assert.deepEqual(wrappers.arrays.get('global.universal_cost_source_ids'), [ticks('26')]);
assert(wrappers.call('universal_cost_source_clear_black_friday'));
assert.equal(wrappers.value('universal_cost_source_clear_result'), S);
assert.deepEqual(wrappers.arrays.get('global.universal_cost_source_ids'), []);
summary.sourceWrapperLifetimeChecks = 2;
for (const [source, family, expected] of [[1, 2, 0], [0, 536870912, 1], [536870912, 536870912, 1], [112, 32, 1]]) {
  const matcher = new VM().set('universal_cost_source_mask', source).set('universal_cost_quote_family_mask', family);
  assert(matcher.call('universal_cost_source_matches_quote_family'));
  assert.equal(matcher.value('universal_cost_source_matches_quote'), ticks(expected));
}
summary.familyMatcherLifetimeChecks = 4;
const warmUnits = new VM().set('universal_cost_quantize_amount', '2.00001').set('universal_cost_quantize_quantum', 1);
assert(warmUnits.call('universal_cost_round_up_to_quantum'));
assert.equal(warmUnits.tempArrays.get('uc_exact_units')[0], ticks('3'));
for (const amount of ['0', '-5']) {
  warmUnits.set('universal_cost_quantize_amount', amount);
  assert(warmUnits.call('universal_cost_round_up_to_quantum'));
  assert.deepEqual(warmUnits.tempArrays.get('uc_exact_units'), [0n]);
}
summary.warmUnitArrayChecks = 2;
// Verify the model itself: regular storage survives, inherited temps keep
// changes, helper-local temps die, and temporary shadowing leaves regular data.
definitions.set('vm_lifetime_probe', parse(`
  set_temp_variable = { inherited = 9 }
  set_temp_variable = { helper_local = 8 }
  set_temp_variable = { shadow = 7 }
  set_temp_variable = { inherited_array^0 = 6 }
  resize_temp_array = { array = helper_local_array size = 1 value = 5 }
  resize_temp_array = { array = shadow_array size = 1 value = 4 }
  set_variable = { regular_created = 3 }
  add_to_array = { array = regular_created_array value = 2 }
`));
const model = new VM().set('inherited', 1).tempArray('inherited_array', [ticks(1)]);
model.regularVars.set('shadow', ticks(11)); model.arrays.set('shadow_array', [ticks(12)]);
assert(model.run('vm_lifetime_probe'));
assert.equal(model.value('inherited'), ticks(9)); assert.deepEqual(model.tempArrays.get('inherited_array'), [ticks(6)]);
assert.equal(model.vars.has('helper_local'), false); assert.equal(model.tempArrays.has('helper_local_array'), false);
assert.equal(model.value('shadow'), ticks(11)); assert.deepEqual(model.array('shadow_array'), [ticks(12)]);
assert.equal(model.value('regular_created'), ticks(3)); assert.deepEqual(model.array('regular_created_array'), [ticks(2)]);
summary.lexicalModelAssertions = 8;
// A bare API invocation returns its predicate result but does not export newly
// created temporaries. This deliberately bypasses only the outer contract audit,
// never lexical cleanup or nested helper audits, and exposes caller obligations.
for (const api of ['universal_cost_quote_exact', 'universal_cost_quote_integer', 'black_friday_quote_custom_cost']) {
  const bare = fixture('2.00001', '1', 1, rows('5000'));
  bare.set('black_friday_quote_ordinary_cost', '2.00001').set('black_friday_quote_family_mask', 1);
  assert(bare.run(api, true));
  const key = api.startsWith('black_friday') ? 'black_friday_quote_final_cost' : 'universal_cost_quote_final_cost';
  assert.equal(bare.vars.has(key), false, `new public output ${key} must die without an outer declaration`);
  assert.deepEqual(bare.arrays.get('global.universal_cost_source_ids'), [ticks(26)]);
}
summary.bareApiOutputLossControls = 3;
for (const testedVM of executedVMs) recordLifetime(testedVM);
for (const name of Object.keys(helperOutputs)) assert(summary.helperOutputChecks[name] > 0, `unexercised lifetime contract ${name}`);
summary.maxBoundedAccumulator = String(BigInt(summary.maxBoundedAccumulator) / S);
if (process.argv.includes('--details')) console.log(JSON.stringify(summary));
else {
  const { results, helperOutputContracts, callerOutputDeclarations, ...counts } = summary;
  console.log(JSON.stringify({ ...counts, criticalResults: results.filter(r =>
    ['single-2.00001-5000-1', 'single-0.04001-2500-0.01', 'single-1000000-5000-1',
      'compose-2-1-9999.99999,5000.00001', 'many-nonidentities', 'unrepresentable-output'].includes(r.id)) }, null, 2));
}
}
