// Audits actual loop envelopes, then exercises their native traversal contract
// with explicit two-object bodies. Numeric loops model the documented 1000
// limit; foreach fixtures do not invent that limit or prove engine behavior.
const fs = require('fs'), assert = require('assert/strict');
const { parse, assignment, hash } = require('../../docs/plans/033_acid_rain_plans/validation/caller_repairs_source_tests_2026_10_03.js');
const path = 'common/scripted_effects/033_acid_rain_effects.txt', bytes = fs.readFileSync(path);
const kinds = new Set(['for_each_loop', 'for_each_scope_loop', 'for_loop_effect', 'while_loop_effect']), loops = [];
function walk(nodes, helper) {
	for (let i = 0; i < nodes.length; i++) {
		const n = nodes[i];
		if (kinds.has(n.key)) {
			const binding = n.value.find(x => x.key === 'break')?.value;
			assert.ok(binding && binding !== 'break', helper + ' lacks private break');
			assert.equal(nodes[i - 1]?.key, 'set_temp_variable', helper + ' lacks immediate reset');
			assert.deepEqual(assignment(nodes[i - 1]), [binding, 'constant:acid_rain_runtime.zero']);
			loops.push({ helper, kind: n.key, binding });
		}
		if (Array.isArray(n.value)) walk(n.value, helper);
	}
}
for (const n of parse(bytes.toString('utf8'))) if (Array.isArray(n.value)) walk(n.value, n.key);
// The original 77 envelopes remain, with one bounded connected-growth loop.
assert.equal(loops.length, 78);
assert.equal(new Set(loops.map(x => x.binding)).size, loops.length, 'break names collide across helper boundaries');
function traverse(kind, count, temps, binding, reset, body, earlyAt) {
	if (reset) temps.set(binding, 0);
	let visited = 0;
	const cap = kind.startsWith('for_each') ? count : Math.min(count, 1000);
	for (let i = 0; i < cap && !temps.get(binding); i++) {
		body(i); visited++;
		if (earlyAt !== undefined && visited === earlyAt) temps.set(binding, 1);
	}
	return visited;
}
for (const loop of loops) {
	const temps = new Map([['break', 1], [loop.binding, 1]]);
	for (let repeat = 0; repeat < 2; repeat++) {
		assert.equal(traverse(loop.kind, 2, temps, loop.binding, true, () => temps.set('break', 1)), 2);
		temps.set(loop.binding, 1);
	}
	assert.equal(traverse(loop.kind, 2, temps, loop.binding, false, () => {}), 0, 'negative control ignored inherited private stop');
	assert.equal(traverse(loop.kind, 2, temps, loop.binding, true, () => {}, 1), 1, 'intentional stop lost');
}
const foreach = loops.filter(x => x.kind.startsWith('for_each'));
for (const loop of foreach) {
	const pending = Array.from({ length: 1301 }, (_, i) => i), acknowledged = new Set(), temps = new Map([['break', 1]]);
	const visited = traverse(loop.kind, pending.length, temps, loop.binding, true, i => { if (i % 2 === 0) acknowledged.add(pending[i]); temps.set('break', 1); });
	assert.equal(visited, 1301);
	const unresolved = pending.filter(id => !acknowledged.has(id));
	assert.equal(unresolved.length, 650, 'unacknowledged receipts disappeared');
}
const nested = new Map([['break', 1], ['outer', 1], ['inner', 1]]), visits = [];
traverse('for_each_scope_loop', 2, nested, 'outer', true, p => traverse('for_each_loop', 2, nested, 'inner', true, r => { visits.push([p, r]); nested.set('break', 1); }));
assert.deepEqual(visits, [[0, 0], [0, 1], [1, 0], [1, 1]]);
console.log(JSON.stringify({ status: 'pass', runtime_sha256: hash(bytes), loops: loops.length, foreach_loops: foreach.length,
	boundaries: loops, limits: ['Traversal bodies and input arrays are fixtures, not full gameplay', 'No native foreach limit, scheduling, save/reload or engine proof'] }, null, 2));
