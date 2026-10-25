// Actual-source regression for generation-owned regional cursor batches.
// Original state-body entry is witnessed; physics, RNG, costs and native gameplay are not executed.
const fs = require('fs'), assert = require('assert/strict'), { execFileSync } = require('child_process');
const { parse, assignment, hash } = require('./lib/clausewitz_source_model.js');
const runtimePath = 'common/scripted_effects/033_acid_rain_effects.txt';
const beforeBytes = execFileSync('git', ['show', '23f8aa8c9de178decd5bf7f267ae23a596521df3:' + runtimePath]);
assert.equal(hash(beforeBytes), '48b6c9b8ddcbacc8fafc002551735b7ade269929ecb36fa7beb5e6cc0a2ecabe');
const afterBytes = fs.readFileSync(runtimePath);
const before = parse(beforeBytes.toString('utf8')), after = parse(afterBytes.toString('utf8'));
const categories = parse(fs.readFileSync('common/script_constants/033_acid_rain_constants.txt', 'utf8'));
const changes = [];
function originalCursors(nodes) {
	for (const node of nodes) {
		if (node.key === 'for_loop_effect' && node.value.find(x => x.key === 'start')?.value === 'acid_rain_cursor_start') {
			const stop = node.value.find(x => x.key === 'break').value, prefix = stop.replace(/_break$/, '_chunk');
			changes.push({ stop, fullEnd: node.value.find(x => x.key === 'end').value, chunkStop: prefix + '_break' });
		}
		if (Array.isArray(node.value)) originalCursors(node.value);
	}
}
originalCursors(before);
const manifest = { changes, runtimeCandidate: hash(afterBytes) };
const constants = new Map();
for (const category of categories) for (const row of Array.isArray(category.value) ? category.value : [])
	if (!Array.isArray(row.value) && Number.isFinite(Number(row.value))) constants.set('constant:' + category.key + '.' + row.key, Number(row.value));
const batch = constants.get('constant:acid_rain_runtime.region_cursor_batch_size');
assert.ok(batch > 0 && batch <= 1000 && Number.isInteger(batch));
const byBreak = new Map(manifest.changes.map(row => [row.stop, row]));
const rawLoops = [], wrappedLoops = [];
const setting = (nodes, key) => nodes.find(x => x.key === key)?.value;
function collect(nodes, wrapped) {
	for (const node of nodes) {
		if (node.key === 'for_loop_effect' && byBreak.has(setting(node.value, 'break'))) rawLoops.push(node);
		if (node.key === 'for_each_loop' && setting(node.value, 'array') === 'global.acid_rain_region_iteration_chunks') wrappedLoops.push(node);
		if (Array.isArray(node.value)) collect(node.value, wrapped);
	}
}
collect(before); const oldLoops = rawLoops.splice(0); collect(after);
assert.equal(oldLoops.length, 16); assert.equal(rawLoops.length, 16); assert.equal(wrappedLoops.length, 16);
for (let i = 0; i < oldLoops.length; i++) {
	const modified = structuredClone(rawLoops[i]), row = manifest.changes[i];
	modified.value.find(x => x.key === 'start').value = 'acid_rain_cursor_start';
	modified.value.find(x => x.key === 'end').value = row.fullEnd;
	assert.deepEqual(modified, oldLoops[i], 'original loop payload/order changed');
}
const allowed = new Set(['acid_rain_build_region_index', 'acid_rain_prepare_region_cursor']);
function containsReset(node) {
	if (node.key === 'clear_variable' && node.value === 'global.acid_rain_region_index_generation') return true;
	return Array.isArray(node.value) && node.value.some(containsReset);
}
for (const node of before) if (containsReset(node)) allowed.add(node.key);
function unwrap(nodes) {
	const out = [];
	for (const node of nodes) {
		if (node.key === 'set_temp_variable' && manifest.changes.some(r => assignment(node)[0] === r.chunkStop)) continue;
		if (node.key === 'for_each_loop' && setting(node.value, 'array') === 'global.acid_rain_region_iteration_chunks') {
			const body = node.value.find(x => x.key === 'if').value;
			const inner = structuredClone(body.find(x => x.key === 'for_loop_effect'));
			const row = byBreak.get(setting(inner.value, 'break'));
			inner.value.find(x => x.key === 'start').value = 'acid_rain_cursor_start';
			inner.value.find(x => x.key === 'end').value = row.fullEnd;
			out.push({ key: 'set_temp_variable', op: '=', value: [{ key: row.stop, op: '=', value: 'constant:acid_rain_runtime.zero' }] }, inner);
		} else out.push({ ...node, value: Array.isArray(node.value) ? unwrap(node.value) : node.value });
	}
	return out;
}
const reversed = unwrap(after);
assert.equal(reversed.length, before.length);
// hidden_trigger only hides tooltip text (f63ab274b) and the engine evaluates it like its content.
const unhide = ns => Array.isArray(ns) ? ns.flatMap(n => n.key === 'hidden_trigger' && Array.isArray(n.value) ? unhide(n.value) : [Array.isArray(n.value) ? { ...n, value: unhide(n.value) } : n]) : ns;
for (let i = 0; i < before.length; i++) if (!allowed.has(before[i].key)) assert.deepEqual(unhide([reversed[i]]), unhide([before[i]]));
function env(states) { return { temps: new Map(), vars: new Map([['global.acid_rain_generation_id', 2]]),
	arrays: new Map([['global.acid_rain_frozen_states', states]]), flags: new Set(), state: null, trace: [], stop: null }; }
function value(token, e) {
	if (typeof token === 'number') return token;
	if (token === 'THIS') return e.state;
	if (constants.has(token)) return constants.get(token);
	if (Number.isFinite(Number(token))) return Number(token);
	const split = token.indexOf('^');
	if (split >= 0) {
		const name = token.slice(0, split), index = token.slice(split + 1), array = e.arrays.get(name) ?? [];
		return index === 'num' ? array.length : array[value(index, e)] ?? 0;
	}
	return e.temps.get(token) ?? e.vars.get(token) ?? e.state?.[token] ?? 0;
}
function set(name, v, e, temporary) {
	const split = name.indexOf('^');
	if (split >= 0) { const base = name.slice(0, split), array = e.arrays.get(base) ?? []; array[value(name.slice(split + 1), e)] = v; e.arrays.set(base, array); }
	else (temporary ? e.temps : e.vars).set(name, v);
}
function cmp(a, b, op) {
	return ({ equals: () => a === b, not_equals: () => a !== b, less_than: () => a < b,
		greater_than: () => a > b, greater_than_or_equals: () => a >= b, less_than_or_equals: () => a <= b })[op]();
}
function condition(nodes, e) {
	return nodes.every(n => {
		if (n.key === 'check_variable') {
			if (n.value.some(x => x.key === 'var')) return cmp(value(setting(n.value, 'var'), e), value(setting(n.value, 'value'), e), setting(n.value, 'compare') ?? 'equals');
			const a = n.value[0]; return cmp(value(a.key, e), value(a.value, e), a.op === '>' ? 'greater_than' : a.op === '<' ? 'less_than' : 'equals');
		}
		if (n.key === 'OR') return n.value.some(x => condition([x], e));
		if (n.key === 'NOT') return !condition(n.value, e);
		if (n.key === 'has_global_flag') return e.flags.has(n.value);
		if (n.key === 'has_variable') return e.vars.has(n.value) || e.temps.has(n.value);
		throw Error('unsupported condition: ' + n.key);
	});
}
function execute(nodes, e) {
	for (const n of nodes) {
		const b = n.value;
		if (n.key === 'if') { if (condition(b.find(x => x.key === 'limit').value, e)) execute(b.filter(x => x.key !== 'limit'), e); }
		else if (n.key === 'set_temp_variable' || n.key === 'set_variable') { const [k, v] = assignment(n); set(k, value(v, e), e, n.key === 'set_temp_variable'); }
		else if (n.key === 'add_to_temp_variable') { const [k, v] = assignment(n); set(k, value(k, e) + value(v, e), e, true); }
		else if (n.key === 'clamp_temp_variable') { const k = setting(b, 'var'); set(k, Math.min(value(k, e), value(setting(b, 'max'), e)), e, true); }
		else if (n.key === 'clear_array') e.arrays.set(b, []);
		else if (n.key === 'resize_array') e.arrays.set(setting(b, 'array'), Array(value(setting(b, 'size'), e)).fill(value(setting(b, 'value') ?? '0', e)));
		else if (n.key === 'add_to_array') e.arrays.get(setting(b, 'array')).push(value(setting(b, 'value'), e));
		else if (n.key === 'set_global_flag') e.flags.add(b);
		else if (n.key === 'clr_global_flag') e.flags.delete(b);
		else if (n.key.startsWith('var:global.acid_rain_region_ordered_states^')) {
			const state = value(n.key.slice(4), e); assert.ok(state && typeof state === 'object');
			e.trace.push(state.id);
			if (e.stop && e.trace.length === e.stop.at) e.temps.set(e.stop.binding, 1);
		} else if (n.key === 'acid_rain_build_region_index') execute(builder, e);
		else if (['for_loop_effect', 'for_each_loop', 'for_each_scope_loop'].includes(n.key)) {
			const stop = setting(b, 'break'), name = setting(b, 'value') ?? 'v';
			const control = new Set(['break', 'array', 'value', 'start', 'end', 'compare', 'add', 'index']);
			const body = b.filter(x => !control.has(x.key));
			if (n.key === 'for_loop_effect') {
				let v = value(setting(b, 'start'), e), count = 0;
				while (cmp(v, value(setting(b, 'end'), e), setting(b, 'compare') ?? 'less_than') && count++ < 1000 && !value(stop, e)) {
					e.temps.set(name, v); execute(body, e); v += value(setting(b, 'add') ?? '1', e);
				}
			} else {
				let ordinal = 0;
				for (const item of [...e.arrays.get(setting(b, 'array'))]) {
					if (value(stop, e)) break;
					e.temps.set(setting(b, 'index') ?? 'i', ordinal++);
					e.temps.set(name, item);
					const parent = e.state;
					if (n.key === 'for_each_scope_loop') e.state = item;
					execute(body, e); e.state = parent;
				}
			}
		} else throw Error('unsupported effect: ' + n.key);
	}
}
const builder = after.find(x => x.key === 'acid_rain_build_region_index').value;
const prepare = after.find(x => x.key === 'acid_rain_prepare_region_cursor').value;
const legacy = env([{ id: 1, acid_rain_region_id: 1 }, { id: 2, acid_rain_region_id: 7 }]);
legacy.vars.set('global.acid_rain_region_index_generation', 2);
legacy.temps.set('acid_rain_cursor_region', 7);
legacy.temps.set('acid_rain_cursor_start', 0); legacy.temps.set('acid_rain_cursor_end', 0);
execute(prepare, legacy);
assert.deepEqual([legacy.temps.get('acid_rain_cursor_start'), legacy.temps.get('acid_rain_cursor_end')], [1, 2]);
assert.deepEqual(legacy.arrays.get('global.acid_rain_region_iteration_chunks'), [0, 1]);
const storedChunks = legacy.arrays.get('global.acid_rain_region_iteration_chunks');
execute(prepare, legacy); assert.equal(legacy.arrays.get('global.acid_rain_region_iteration_chunks'), storedChunks, 'same generation rebuilt unnecessarily');
legacy.vars.set('global.acid_rain_generation_id', 3); execute(prepare, legacy);
assert.notEqual(legacy.arrays.get('global.acid_rain_region_iteration_chunks'), storedChunks);
assert.equal(legacy.vars.get('global.acid_rain_region_index_generation'), 3);
const fixtures = [[0, 1, 23, 999, 1000, 1001, 2001], [1001, 0, 23, 2101, 2, 1001, 0]];
const checks = [];
for (const sizes of fixtures) {
	const states = [];
	for (let r = 0; r < 7; r++) for (let i = 0; i < sizes[r]; i++) states.push({ id: states.length + 1, acid_rain_region_id: r + 1 });
	// Deliberately interleave regions to prove original per-region stable ordering.
	states.sort((a, b) => (a.id % 17) - (b.id % 17) || a.id - b.id);
	const e = env(states); execute(builder, e);
	assert.equal(e.arrays.get('global.acid_rain_region_ordered_states').length, states.length);
	assert.equal(e.arrays.get('global.acid_rain_region_iteration_chunks').length, sizes.reduce((n, size) => n + Math.ceil(size / batch), 0));
	for (let r = 1; r <= 7; r++) for (let i = 0; i < wrappedLoops.length; i++) {
		const row = manifest.changes[i], start = e.arrays.get('global.acid_rain_region_index_start_entries')[r], end = e.arrays.get('global.acid_rain_region_index_end_entries')[r];
		e.temps.set('acid_rain_cursor_start', start); e.temps.set(row.fullEnd, end);
		e.temps.set(row.chunkStop, 0); e.temps.set(row.stop, 1); e.trace = []; e.stop = null;
		e.temps.set('i', 7845);
		execute([wrappedLoops[i]], e);
		assert.equal(e.temps.get('i'), 7845, 'chunk iterator clobbered caller index');
		const wanted = states.filter(x => x.acid_rain_region_id === r).map(x => x.id);
		assert.deepEqual(e.trace, wanted);
		const fresh = [...e.trace]; e.trace = []; e.temps.set(row.stop, 0); execute([oldLoops[i]], e);
		assert.deepEqual(e.trace, wanted.slice(0, 1000));
		if (wanted.length > 1000) assert.ok(fresh.includes(wanted[1000]) && !e.trace.includes(wanted[1000]));
		if (wanted.length > 1001) {
			e.trace = []; e.temps.set(row.chunkStop, 0); e.stop = { at: 1001, binding: row.stop };
			execute([wrappedLoops[i]], e); assert.deepEqual(e.trace, wanted.slice(0, 1001));
		}
		checks.push({ loop: row.stop, region: r, size: wanted.length });
	}
}
console.log(JSON.stringify({ status: 'pass', runtime_sha256: manifest.runtimeCandidate,
	traversalCases: checks.length, migrationIndexCases: 3, protectedPayloads: oldLoops.length, allowedNonEnvelopeRoots: [...allowed],
	limits: ['Documented 1000 numeric limit is modeled; no cap invented for foreach', 'Actual original state-body entry is witnessed, not physics, RNG, payment or native execution', 'Before source is immutable commit 23f8aa8c; current engine-facing source is replayed'] }, null, 2));
