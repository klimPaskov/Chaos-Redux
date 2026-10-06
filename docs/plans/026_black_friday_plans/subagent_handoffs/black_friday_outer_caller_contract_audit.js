// Read-only caller storage audit. No arithmetic or receipt VM is duplicated.
// Run from the mod root with node. --inventory reports every inspected boundary.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const root = path.resolve(__dirname, '../../../..');
const files = ['common/scripted_effects/026_black_friday_effects.txt',
  'common/scripted_triggers/026_black_friday_triggers.txt',
  'common/scripted_localisation/026_black_friday_scripted_localisation.txt'];
const sourceFiles = [...files, 'common/scripted_effects/chaosx_universal_cost_effects.txt',
  'common/scripted_triggers/chaosx_universal_cost_triggers.txt'];
function parse(source) {
  const tokens = [...source.matchAll(/#[^\r\n]*|"[^"\r\n]*"|[{}=<>]|[^\s{}=<>]+/g)]
    .filter(t => !t[0].startsWith('#'));
  let i = 0;
  function body(nested = false) {
    const nodes = [];
    while (i < tokens.length && tokens[i][0] !== '}') {
      const token = tokens[i++], key = token[0];
      if (!['=', '<', '>'].includes(tokens[i]?.[0])) {
        nodes.push({ key, op: null, value: key, atom: true, start: token.index, end: token.index + key.length }); continue;
      }
      const op = tokens[i++][0];
      assert(['=', '<', '>'].includes(op), `parse ${key} ${op}`);
      let value = tokens[i++][0];
      if (value === '{') value = body(true);
      nodes.push({ key, op, value, start: token.index, end: tokens[i - 1].index + tokens[i - 1][0].length });
    }
    if (nested) assert.equal(tokens[i++][0], '}');
    return nodes;
  }
  return body();
}
const sources = new Map(sourceFiles.map(f => [f, fs.readFileSync(path.join(root, f), 'utf8')]));
const parsed = new Map([...sources].map(([f, s]) => [f, parse(s)]));
const defs = new Map();
for (const [file, nodes] of parsed) if (!file.includes('scripted_localisation'))
  for (const node of nodes) defs.set(node.key, { file, node });
const field = (nodes, key) => nodes.find(n => n.key === key)?.value;
const union = (...sets) => new Set(sets.flatMap(s => [...s]));
const tempName = token => typeof token === 'string' && /^(black_friday_|universal_cost_)/.test(token)
  ? token.split('^')[0].split('@')[0] : null;
function direct(nodes) {
  const writes = new Set(), reads = new Set(), calls = [];
  function read(token) {
    if (typeof token !== 'string') return;
    for (const part of token.split(/[\^:]/)) { const name = tempName(part); if (name) reads.add(name); }
  }
  function walk(nodes) {
    for (const n of nodes) {
      if (defs.has(n.key) && !Array.isArray(n.value)) calls.push(n.key);
      if (n.key === 'set_temp_variable') {
        writes.add(field(n.value, 'var') || n.value[0].key); read(field(n.value, 'value') || n.value[0].value);
      } else if (n.key === 'clear_temp_array') writes.add(n.value);
      else if (n.key === 'resize_temp_array') { writes.add(field(n.value, 'array')); read(field(n.value, 'size')); }
      else if (Array.isArray(n.value)) { read(n.key); walk(n.value); }
      else { read(n.key); read(n.value); }
    }
  }
  walk(nodes); return { writes, reads, calls };
}
const meta = new Map([...defs].map(([name, { node }]) => [name, direct(node.value)]));
const inputs = new Map(), outputs = new Map();
for (const [name, m] of meta) { inputs.set(name, new Set([...m.reads].filter(x => !m.writes.has(x)))); outputs.set(name, m.writes); }
for (let pass = 0; pass < 30; pass++) {
  for (const [name, m] of meta) {
    outputs.set(name, union(m.writes, ...m.calls.map(c => outputs.get(c))));
    inputs.set(name, new Set([...union(m.reads, ...m.calls.map(c => inputs.get(c)))].filter(x => !outputs.get(name).has(x))));
  }
}
const arrays = ['black_friday_fury_component_ids', 'black_friday_fury_component_resource_kinds',
  'black_friday_fury_component_family_masks', 'black_friday_fury_component_ordinary_costs'];
const publicOutputs = {
  universal_cost_quote_integer: ['universal_cost_quote_final_cost', 'universal_cost_quote_valid'],
  black_friday_quote_custom_cost: ['black_friday_quote_final_cost'],
  black_friday_fury_begin_component_list: arrays,
  black_friday_fury_append_component: arrays,
  black_friday_fury_append_spend_component: arrays,
  black_friday_pay_fury_bundle: ['black_friday_fury_payment_success'],
  black_friday_fury_pay_single_active: ['black_friday_fury_payment_success'],
  black_friday_fury_pay_prepared_bundle_active: ['black_friday_fury_payment_success'],
};
// Restrict shared candidates to their documented public return fields.
// Receipt scratch (including current cursors and payment inputs) is private.
const sharedOutputs = {
  universal_cost_quote_integer: ['universal_cost_quote_final_cost', 'universal_cost_quote_displayed_cost',
    'universal_cost_quote_saved_cost', 'universal_cost_quote_valid', 'universal_cost_quote_source_count',
    'universal_cost_quote_primary_source_id', 'universal_cost_quote_composed_ratio', 'universal_cost_quote_rounding_quantum'],
  universal_cost_check_quote_affordable: ['universal_cost_quote_affordable'],
  universal_cost_pay_component: ['universal_cost_payment_result'],
  universal_cost_credit_component: ['universal_cost_credit_result'],
  universal_cost_record_transaction: ['universal_cost_record_transaction_result', 'universal_cost_recorded_component_index'],
  universal_cost_settle_transaction: ['universal_cost_settle_transaction_result'],
  universal_cost_mark_component_refunded: ['universal_cost_mark_component_refunded_result'],
  universal_cost_refund_transaction: ['universal_cost_refund_transaction_result', 'universal_cost_refund_total', 'universal_cost_refund_unhandled_total'],
  universal_cost_find_transaction_row: ['universal_cost_transaction_found_index', 'universal_cost_transaction_is_indexed',
    'universal_cost_transaction_lookup_result', 'universal_cost_transaction_pointer'],
  universal_cost_find_component_row: ['universal_cost_component_found_index', 'universal_cost_component_lookup_result'],
  universal_cost_source_register_black_friday: ['universal_cost_source_register_result'],
  universal_cost_source_clear_black_friday: ['universal_cost_source_clear_result'],
  universal_cost_source_is_active: [], universal_cost_component_is_affordable: [],
};
const inheritedInputs = {
  black_friday_fury_append_component: arrays,
  black_friday_fury_append_spend_component: arrays,
  black_friday_pay_fury_bundle: arrays,
  black_friday_fury_pay_prepared_bundle_active: arrays,
  black_friday_cbrn_theater_pay_decon_model: ['black_friday_cbrn_theater_all_paid', 'black_friday_cbrn_theater_primary_model_assigned'],
};
const arraySet = new Set(arrays);
function defaultValue(name) {
  if (name.endsWith('found_index') || name === 'black_friday_achievement_transaction_index' || name === 'universal_cost_recorded_component_index')
    return 'constant:universal_cost_framework.invalid_index';
  if (name.endsWith('result')) return 'constant:universal_cost_framework.result_no_op';
  if (name === 'black_friday_quote_final_cost') return 'black_friday_quote_ordinary_cost';
  if (name === 'universal_cost_quote_final_cost') return 'universal_cost_quote_ordinary_cost';
  return 'constant:universal_cost_framework.zero';
}
const inventory = [], gaps = [];
const demand = new Map([...defs.keys()].map(k => [k, new Set()]));
const liveAt = new Map();
function candidatesFor(name) {
  return new Set(sharedOutputs[name] || [...outputs.get(name)].filter(x => x.startsWith('black_friday_')));
}
function liveness(nodes, outgoing) {
  let live = new Set(outgoing);
  for (const n of [...nodes].reverse()) {
    liveAt.set(n, new Set(live));
    if (n.key === 'set_temp_variable') {
      const name = field(n.value, 'var') || n.value[0].key;
      live.delete(name);
      const value = field(n.value, 'value') || n.value[0].value;
      if (tempName(value)) live.add(tempName(value));
      if (typeof value === 'string' && value.includes('^') && tempName(value.split('^')[1])) live.add(tempName(value.split('^')[1]));
    } else if (defs.has(n.key) && !Array.isArray(n.value)) {
      const candidates = candidatesFor(n.key);
      const required = union((publicOutputs[n.key] || []).filter(x => !arrays.includes(x) || n.key === 'black_friday_fury_begin_component_list'),
        [...candidates].filter(x => live.has(x)));
      for (const name of required) demand.get(n.key).add(name);
      live = union(live, inputs.get(n.key));
    } else if (Array.isArray(n.value)) live = union(live, liveness(n.value, live));
    else live = union(live, direct([n]).reads);
  }
  return live;
}
// Forwarded caller outputs must also survive each nested wrapper return.
for (let pass = 0; pass < 20; pass++) for (const file of files) for (const node of parsed.get(file)) {
  if (node.key === 'black_friday_quote_custom_cost') continue;
  if (node.key === 'defined_text') for (const text of node.value.filter(n => n.key === 'text'))
    liveness(field(text.value, 'trigger') || [], new Set());
  else liveness(node.value, demand.get(node.key));
}
function inspect(file, owner, nodes, inherited = new Set()) {
  const frame = union(inherited, inheritedInputs[owner] || []), own = direct(nodes);
  function walk(nodes, storage) {
    for (const n of nodes) {
      if (n.key === 'set_temp_variable') storage.add(field(n.value, 'var') || n.value[0].key);
      else if (n.key === 'resize_temp_array') storage.add(field(n.value, 'array'));
      // Clearing contents alone is not proof of a cold caller-owned array.
      else if (defs.has(n.key) && !Array.isArray(n.value)) {
        const candidates = candidatesFor(n.key);
        const used = liveAt.get(n) || new Set();
        const required = union((publicOutputs[n.key] || []).filter(x => !arrays.includes(x) || n.key === 'black_friday_fury_begin_component_list'),
          [...candidates].filter(x => used.has(x)));
        const missing = [...required].filter(x => !storage.has(x));
        const row = { file, owner, helper: n.key, line: sources.get(file).slice(0, n.start).split('\n').length,
          required: [...required], missing, start: n.start };
        inventory.push(row);
        if (missing.length) gaps.push(row);
        if (process.argv.includes('--patch')) for (const name of missing) storage.add(name);
      } else if (Array.isArray(n.value)) {
        const child = new Set(storage);
        walk(n.value, child);
        if (!['if', 'else_if', 'else', 'NOT', 'OR', 'while_loop_effect', 'for_each_loop', 'every_country'].includes(n.key))
          for (const name of child) storage.add(name);
      }
    }
  }
  walk(nodes, frame);
}
for (const file of files) for (const node of parsed.get(file)) {
  if (node.key === 'black_friday_quote_custom_cost') continue; // architect01a10115 owns this block
  if (node.key === 'defined_text') {
    const owner = field(node.value, 'name');
    for (const text of node.value.filter(n => n.key === 'text')) inspect(file, owner, field(text.value, 'trigger') || []);
  } else inspect(file, node.key, node.value);
}
module.exports = { files, sources, parsed, defs, inventory, gaps, field, parse, root };
if (require.main !== module) {
  // Import for the bounded source caller scenarios, without executing a CLI.
} else if (process.argv.includes('--inventory')) console.log(JSON.stringify({ inventory, gaps }, null, 2));
else if (process.argv.includes('--changes')) {
  const changes = [];
  for (const file of files) for (const node of parsed.get(file)) {
    const text = sources.get(file).slice(node.start, node.end), declarations = [];
    for (const group of text.matchAll(/# Caller-owned cost API outputs\.\r?\n((?:[\t ]*(?:set_temp_variable|resize_temp_array) = \{[^\r\n]*\}\r?\n)+)/g))
      for (const line of group[1].trim().split(/\r?\n/)) declarations.push(line.trim());
    if (declarations.length) changes.push({ file, owner: node.key,
      callBoundaries: (text.match(/# Caller-owned cost API outputs\./g) || []).length,
      declarations: [...new Set(declarations)], declarationCount: declarations.length });
  }
  console.log(JSON.stringify(changes));
}
else if (process.argv.includes('--patch')) {
  const patch = ['*** Begin Patch'];
  for (const file of files) {
    const rows = gaps.filter(g => g.file === file); if (!rows.length) continue;
    patch.push(`*** Update File: ${path.join(root, file).replaceAll('\\', '/')}`);
    const source = sources.get(file), lines = source.split(/\r?\n/);
    const edits = new Map();
    for (const row of rows) {
      // Native containers have the same frame. For inline limit calls, create
      // storage immediately inside the container before its helper predicate.
      const i = row.line - 1, line = lines[i], indent = line.match(/^\s*/)[0];
      const declarations = row.missing.map(name => arraySet.has(name)
        ? `resize_temp_array = { array = ${name} size = constant:universal_cost_framework.one }`
        : `set_temp_variable = { ${name} = ${defaultValue(name)} }`);
      const pos = row.start - (source.lastIndexOf('\n', row.start - 1) + 1);
      if (line.slice(0, pos).trim()) {
        const tail = line.slice(pos);
        edits.set(i, [line.slice(0, pos).trimEnd(), `${indent}\t# Caller-owned cost API outputs.`,
          ...declarations.map(d => `${indent}\t${d}`),
          `${indent}\t${tail.replace(/\s+\}$/, '')}`, `${indent}}`]);
      } else edits.set(i, [`${indent}# Caller-owned cost API outputs.`, ...declarations.map(d => `${indent}${d}`), line]);
    }
    const ranges = [];
    for (const i of [...edits.keys()].sort((a,b) => a-b)) {
      const begin = Math.max(0, i - 2), end = Math.min(lines.length - 1, i + 1);
      if (ranges.length && begin <= ranges.at(-1)[1] + 1) ranges.at(-1)[1] = end;
      else ranges.push([begin, end]);
    }
    for (const [begin, end] of ranges) {
      patch.push('@@');
      for (let i = begin; i <= end; i++) {
        if (edits.has(i)) patch.push(`-${lines[i]}`, ...edits.get(i).map(line => `+${line}`));
        else patch.push(` ${lines[i]}`);
      }
    }
  }
  patch.push('*** End Patch'); console.log(patch.join('\n'));
} else {
  const summary = { evidence: 'static source declaration checks, no engine or math execution',
    sourceHashes: Object.fromEntries([...sources].filter(([f]) => files.includes(f))
      .map(([f,s]) => [f, crypto.createHash('sha256').update(s).digest('hex')])),
    inspectedBoundaries: inventory.length, missingBoundaries: gaps.length,
    byFile: Object.fromEntries(files.map(f => [f, { calls: inventory.filter(x => x.file === f).length,
      gaps: gaps.filter(x => x.file === f).length }])), gaps };
  console.log(JSON.stringify(summary, null, 2));
  if (gaps.length) process.exitCode = 1;
}
