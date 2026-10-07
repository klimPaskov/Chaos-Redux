// Actual family-resolver replay under conservative scripted-helper frames.
// No payment, state operation or native delayed callback is mocked as success.
const fs = require('fs'), assert = require('assert/strict');
const { parse, namedBlock, assignment, hash } = require('../../docs/plans/033_acid_rain_plans/validation/caller_repairs_source_tests_2026_10_03.js');
const path = 'common/scripted_effects/033_acid_rain_preparedness_effects.txt', bytes = fs.readFileSync(path);
const constants = new Map();
for (const category of parse(fs.readFileSync('common/script_constants/033_acid_rain_constants.txt', 'utf8')))
	for (const entry of Array.isArray(category.value) ? category.value : [])
		if (!Array.isArray(entry.value) && Number.isFinite(Number(entry.value))) constants.set('constant:' + category.key + '.' + entry.key, Number(entry.value));
const body = parse(namedBlock(bytes.toString('utf8'), 'acid_rain_resolve_operation_family'))[0].value;
const opening = parse(namedBlock(bytes.toString('utf8'), 'acid_rain_open_operation'))[0].value;
function resolve(action, initialized) {
	const parent = new Map([['caller_sentinel', 37]]), saved = new Map([['acid_rain_selected_action', constants.get('constant:acid_rain_action.' + action)]]);
	assert.ok(saved.get('acid_rain_selected_action') !== undefined);
	if (initialized) parent.set('acid_rain_op_family', 0);
	const child = new Map(parent);
	const value = token => constants.has(token) ? constants.get(token) : child.get(token) ?? saved.get(token) ?? 0;
	function run(nodes) {
		let previousMatched = false;
		for (const node of nodes) {
			if (node.key === 'set_temp_variable') { const [key, token] = assignment(node); child.set(key, value(token)); continue; }
			assert.ok(['if', 'else_if'].includes(node.key), 'unknown effect ' + node.key);
			if (node.key === 'if') previousMatched = false;
			const limit = node.value.find(n => n.key === 'limit');
			const matched = limit.value.every(n => {
				assert.equal(n.key, 'check_variable');
				assert.equal(n.value.find(x => x.key === 'compare').value, 'equals');
				const [key, token] = assignment(n); return value(key) === value(token);
			});
			if (!previousMatched && matched) { run(node.value.filter(n => n.key !== 'limit')); previousMatched = true; }
		}
	}
	run(body);
	for (const key of parent.keys()) parent.set(key, child.get(key));
	assert.equal(parent.get('caller_sentinel'), 37);
	assert.equal(saved.get('acid_rain_selected_action'), constants.get('constant:acid_rain_action.' + action));
	return parent.get('acid_rain_op_family');
}
const cases = [['urgent_shelter', 1], ['urgent_water_land', 2], ['urgent_water_island', 2], ['urgent_medical', 3], ['urgent_transport', 4], ['recovery_demobilize', 5],
	['urgent_evacuate_land', 0], ['urgent_evacuate_island', 0], ['recovery_transport', 0], ['recovery_decontaminate_land', 0], ['recovery_decontaminate_island', 0], ['recovery_industry', 0]];
for (const [action, expected] of cases) {
	assert.equal(resolve(action, true), expected, action);
	assert.equal(resolve(action, false), undefined, 'negative control retained child-only family');
}
assert.equal(opening[0].key, 'set_temp_variable', 'operation opening lacks caller-owned family storage');
assert.deepEqual(assignment(opening[0]), ['acid_rain_op_family', 'constant:acid_rain_runtime.zero']);
assert.equal(opening[1].key, 'acid_rain_resolve_operation_family');
console.log(JSON.stringify({ status: 'pass', source_sha256: hash(bytes), resolver_cases: cases.length,
	negative_controls: cases.length, limits: ['No full quote/debit/open-operation execution', 'No native scope, payment, scheduling or save/reload proof'] }, null, 2));
