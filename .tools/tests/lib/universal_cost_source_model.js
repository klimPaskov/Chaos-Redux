// Universal cost source model shared by the maintained Event 016 paleogenetics staff tests.
// Lines 4-284 are copied unchanged from the Event 026 handoff test of the same model
// (docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js), which stays in
// its plan folder as a historical record together with its own scenario runner. Only the mod-root
// path changes, because this file sits three levels below the root.
// This is source-semantic evidence, not an HOI4 or MCP engine emulator claim.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const root = path.resolve(__dirname, '../../..');
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
