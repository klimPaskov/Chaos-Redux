// Real cursor-body replay and exact caller-storage audit. Native indexed reads
// and index rebuilding are explicit fixtures, not HOI4 execution or map proof.
const fs = require('fs');
const assert = require('assert/strict');
const { parse, namedBlock, assignment, hash } = require('./lib/clausewitz_source_model.js');
const path = 'common/scripted_effects/033_acid_rain_effects.txt';
const bytes = fs.readFileSync(path), text = bytes.toString('utf8');
const outputs = {
	acid_rain_prepare_region_cursor: ['acid_rain_cursor_start', 'acid_rain_cursor_end'],
	acid_rain_assign_next_front_region: ['acid_rain_front_region_result'],
	acid_rain_select_weighted_region: ['acid_rain_region_candidate', 'acid_rain_region_weight_total'],
	acid_rain_compute_region_candidate_weight: ['acid_rain_region_candidate_weight'],
};
const expectedCounts = [16, 2, 3, 7], sites = Object.fromEntries(Object.keys(outputs).map(name => [name, []]));
function collect(nodes, caller) {
	for (let i = 0; i < nodes.length; i++) {
		const node = nodes[i];
		if (outputs[node.key] && node.value === 'yes') sites[node.key].push({ caller, before: nodes.slice(0, i), after: nodes[i + 1] });
		if (Array.isArray(node.value)) collect(node.value, caller);
	}
}
for (const effect of parse(text)) if (Array.isArray(effect.value)) collect(effect.value, effect.key);
const cursorBody = parse(namedBlock(text, 'acid_rain_prepare_region_cursor'))[0].value;
const constants = new Map();
for (const category of parse(fs.readFileSync('common/script_constants/033_acid_rain_constants.txt', 'utf8')))
	for (const row of Array.isArray(category.value) ? category.value : [])
		if (!Array.isArray(row.value) && Number.isFinite(Number(row.value))) constants.set('constant:' + category.key + '.' + row.key, Number(row.value));

function replay(prefix, region, stale = false, indexed = true) {
	const globals = new Map([['global.acid_rain_generation_id', 2], ['global.acid_rain_region_index_generation', stale ? 1 : 2],
		['global.acid_rain_region_index_start_entries', [0, 0, 4, 8, 12, 16, 20, 24]],
		['global.acid_rain_region_index_end_entries', [0, 4, 8, 12, 16, 20, 24, 28]]]);
	const parent = new Map([['acid_rain_cursor_region', region], ['caller_sentinel', 37]]);
	let temps = parent, rebuilds = 0;
	const flags = new Set(indexed ? ['acid_rain_region_chunks_indexed'] : []);
	function value(token) {
		if (token.startsWith('constant:')) { assert.ok(constants.has(token)); return constants.get(token); }
		if (Number.isFinite(Number(token))) return Number(token);
		if (token.includes('^')) { const [key, index] = token.split('^'); return globals.get(key)[value(index)]; }
		return temps.get(token) ?? globals.get(token) ?? 0;
	}
	function trigger(node) {
		if (node.key === 'NOT') return !node.value.every(trigger);
		if (node.key === 'OR') return node.value.some(trigger);
		if (node.key === 'has_variable') return temps.has(node.value) || globals.has(node.value);
		if (node.key === 'has_global_flag') return flags.has(node.value);
		assert.equal(node.key, 'check_variable', 'unknown trigger');
		const [key, token] = assignment(node), a = value(key), b = value(token);
		const kind = node.value.find(n => n.key === 'compare').value;
		if (kind === 'not_equals') return a !== b;
		if (kind === 'greater_than_or_equals') return a >= b;
		if (kind === 'less_than_or_equals') return a <= b;
		throw Error('unknown comparison ' + kind);
	}
	function run(nodes) {
		for (const node of nodes) {
			if (node.key === 'if') {
				if (node.value.find(n => n.key === 'limit').value.every(trigger)) run(node.value.filter(n => n.key !== 'limit'));
			} else if (node.key === 'set_temp_variable') {
				const [key, token] = assignment(node); temps.set(key, value(token));
			} else if (node.key === 'acid_rain_build_region_index') {
				// Out-of-scope rebuild mock, with unchanged fixture array contents.
				rebuilds++; globals.set('global.acid_rain_region_index_generation', 2);
				flags.add('acid_rain_region_chunks_indexed');
			} else throw Error('unknown effect ' + node.key);
		}
	}
	run(prefix);
	const inherited = new Set(parent.keys());
	temps = new Map(parent);
	run(cursorBody);
	for (const key of inherited) parent.set(key, temps.get(key));
	assert.equal(parent.get('acid_rain_cursor_region'), region, 'input region changed');
	assert.equal(parent.get('caller_sentinel'), 37);
	return { start: parent.get('acid_rain_cursor_start'), end: parent.get('acid_rain_cursor_end'), rebuilds };
}

const checked = [];
for (const [index, name] of Object.keys(outputs).entries()) {
	assert.equal(sites[name].length, expectedCounts[index], 'call-site inventory changed: ' + name);
	for (const site of sites[name]) {
		const prefix = site.before.slice(-outputs[name].length);
		assert.equal(prefix.length, outputs[name].length);
		assert.deepEqual(prefix.map(n => { assert.equal(n.key, 'set_temp_variable'); return assignment(n); }),
			outputs[name].map(output => [output, 'constant:acid_rain_runtime.zero']), 'missing caller storage: ' + site.caller + ' -> ' + name);
		if (name === 'acid_rain_prepare_region_cursor') {
			for (let region = 1; region <= 7; region++) {
				assert.deepEqual(replay(prefix, region), { start: (region - 1) * 4, end: region * 4, rebuilds: 0 });
			}
			assert.deepEqual(replay(prefix, 0), { start: 0, end: 0, rebuilds: 0 });
			assert.deepEqual(replay(prefix, 8), { start: 0, end: 0, rebuilds: 0 });
			assert.deepEqual(replay(prefix, 4, true), { start: 12, end: 16, rebuilds: 1 });
			assert.deepEqual(replay(prefix, 4, false, false), { start: 12, end: 16, rebuilds: 1 }, 'same-generation legacy index needs chunks');
		}
		checked.push({ caller: site.caller, helper: name, outputs: outputs[name] });
	}
}
assert.deepEqual(replay([], 4), { start: undefined, end: undefined, rebuilds: 0 }, 'negative control must lose newly created outputs');
assert.equal(/set_variable_to_random\s*=\s*\{\s*var\s*=\s*acid_rain_region_candidate/.test(text), false, 'retry candidate escaped into saved scope');
assert.equal(parse(namedBlock(text, 'acid_rain_select_weighted_region'))[0].value[0].key, 'clear_variable');
assert.equal(parse(namedBlock(text, 'acid_rain_select_weighted_region'))[0].value[0].value, 'acid_rain_region_candidate', 'legacy saved scratch not retired');
console.log(JSON.stringify({ status: 'pass', source_sha256: hash(bytes), call_sites: checked, cursor_cases: 176,
	negative_control: 'undeclared cursor outputs disappear on helper return',
	limits: ['Native array reads/rebuilding/predicates are fixtures', 'Weighted selector caller storage is audited, not numerical probability or full formation execution'] }, null, 2));
