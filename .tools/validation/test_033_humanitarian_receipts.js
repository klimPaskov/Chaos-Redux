// Executes the two actual Event 033 registration helpers with explicit native
// primitives and an out-of-scope famine-owner acceptance mock. No file writes.
const fs = require('fs');
const assert = require('assert/strict');
const { parse, namedBlock, assignment, constants, hash } = require('../../docs/plans/033_acid_rain_plans/validation/caller_repairs_source_tests_2026_10_03.js');
const path = 'common/scripted_effects/033_acid_rain_aftermath_effects.txt';
const bytes = fs.readFileSync(path);
for (const category of parse(fs.readFileSync('common/script_constants/033_acid_rain_constants.txt', 'utf8')))
	for (const entry of Array.isArray(category.value) ? category.value : [])
		if (!Array.isArray(entry.value) && Number.isFinite(Number(entry.value)))
			constants.set('constant:' + category.key + '.' + entry.key, Number(entry.value));
const names = ['acid_rain_register_humanitarian_pressure', 'acid_rain_register_aftermath_humanitarian_pressure'];
const bodies = Object.fromEntries(names.map(name => [name, parse(namedBlock(bytes.toString('utf8'), name))[0].value]));

function fixture({ population = 100000, frozen = true } = {}) {
	const state = { id: 64, saved: new Map([['acid_rain_state_aftermath_tier', 2]]), population };
	const owner = { id: 1, saved: new Map() }, controller = { id: 2, saved: new Map() };
	const targets = new Map(), frames = [new Map()], requests = [];
	let accepts = false;
	const temps = () => frames.at(-1);
	function value(token, scope) {
		if (token.startsWith('constant:')) { assert.ok(constants.has(token), 'unresolved constant ' + token); return constants.get(token); }
		if (Number.isFinite(Number(token))) return Number(token);
		if (token === 'THIS.id') return scope.id;
		if (token === 'global.acid_rain_generation_id') return 1;
		if (token === 'global.date') return 1936.0101;
		if (token === 'state_population_k') return scope.population / 1000;
		if (token === 'event_target:famine_adapter_actor.id') return targets.get('famine_adapter_actor').id;
		return temps().get(token) ?? scope.saved.get(token) ?? 0;
	}
	function compare(left, right, kind) {
		if (['=', 'equals'].includes(kind)) return left === right;
		if (['>', 'greater_than'].includes(kind)) return left > right;
		if (kind === 'less_than') return left < right;
		if (kind === 'greater_than_or_equals') return left >= right;
		throw Error('unknown comparison ' + kind);
	}
	function trigger(node, scope) {
		if (node.key === 'NOT') return !node.value.every(n => trigger(n, scope));
		if (node.key === 'OR') return node.value.some(n => trigger(n, scope));
		if (node.key === 'has_variable') return temps().has(node.value) || scope.saved.has(node.value);
		if (node.key === 'acid_rain_state_is_frozen_valid') return frozen;
		if (node.key === 'check_variable') {
			const [key, token] = assignment(node);
			const kind = node.value.find(n => n.key === 'compare')?.value ?? node.value[0].op;
			return compare(value(key, scope), value(token, scope), kind);
		}
		throw Error('unknown trigger ' + node.key);
	}
	function helper(name, scope) {
		const parent = temps(), inherited = new Set(parent.keys());
		frames.push(new Map(parent));
		run(bodies[name], scope);
		const child = frames.pop();
		for (const key of inherited) parent.set(key, child.get(key));
	}
	function run(nodes, scope) {
		for (let i = 0; i < nodes.length; i++) {
			const node = nodes[i];
			if (node.key === 'if') {
				const limit = node.value.find(n => n.key === 'limit');
				const hit = limit.value.every(n => trigger(n, scope));
				if (hit) run(node.value.filter(n => n.key !== 'limit'), scope);
				if (nodes[i + 1]?.key === 'else') { if (!hit) run(nodes[i + 1].value, scope); i++; }
				continue;
			}
			if (node.key === 'OWNER' || node.key === 'CONTROLLER') { run(node.value, node.key === 'OWNER' ? owner : controller); continue; }
			if (names.includes(node.key)) { helper(node.key, scope); continue; }
			if (node.key === 'save_event_target_as') { targets.set(node.value, scope); continue; }
			if (node.key === 'famine_adapt_acid_rain_state') {
				requests.push({ amount: value('acid_rain_humanitarian_amount', scope), generation: value('famine_adapter_generation', scope),
					revision: value('famine_adapter_revision', scope), result: Number(accepts) });
				temps().set('famine_adapter_result', Number(accepts));
				continue;
			}
			if (node.key === 'round_temp_variable') { temps().set(node.value, Math.round(value(node.value, scope))); continue; }
			assert.ok(['set_temp_variable', 'set_variable', 'multiply_temp_variable', 'add_to_temp_variable'].includes(node.key), 'unknown effect ' + node.key);
			const [key, token] = assignment(node), right = value(token, scope);
			if (node.key === 'set_variable') scope.saved.set(key, right);
			else if (node.key === 'set_temp_variable') temps().set(key, right);
			else temps().set(key, node.key === 'multiply_temp_variable' ? value(key, scope) * right : value(key, scope) + right);
		}
	}
	return { state, requests, attempt(accepted, tier = 2) {
		accepts = accepted;
		state.saved.set('acid_rain_state_aftermath_tier', tier);
		helper(names[1], state);
	} };
}

const retry = fixture();
retry.attempt(false);
assert.equal(retry.state.saved.has('acid_rain_humanitarian_tier_registered'), false, 'rejected tier request committed its registration watermark');
retry.attempt(true);
assert.equal(retry.requests.length, 2, 'valid retry suppressed after owner rejection');
assert.equal(retry.state.saved.get('acid_rain_humanitarian_tier_registered'), 2);
retry.attempt(true);
assert.equal(retry.requests.length, 2, 'accepted tier registered twice');
retry.attempt(false, 3);
assert.equal(retry.state.saved.get('acid_rain_humanitarian_tier_registered'), 2, 'rejected higher tier advanced watermark');
retry.attempt(true, 3);
assert.equal(retry.state.saved.get('acid_rain_humanitarian_tier_registered'), 3);
retry.attempt(true, 2);
assert.equal(retry.requests.length, 4, 'older lower tier registered again');
assert.deepEqual(retry.requests.map(r => r.amount), [500, 500, 1000, 1000]);
const tiny = fixture({ population: 10 });
tiny.attempt(true);
assert.equal(tiny.requests.length, 0, 'rounded-zero amount reached owner');
assert.equal(tiny.state.saved.has('acid_rain_humanitarian_tier_registered'), false, 'zero amount committed watermark');
const stale = fixture({ frozen: false });
stale.attempt(true);
assert.equal(stale.requests.length, 0);
assert.equal(stale.state.saved.has('acid_rain_humanitarian_tier_registered'), false, 'stale state committed watermark');
// A nested helper's newly created temporary cannot replace caller storage.
const originalTierBody = bodies[names[1]];
function removeOutputDeclaration(nodes) {
	return nodes.filter(n => !(n.key === 'set_temp_variable' && assignment(n)[0] === 'acid_rain_humanitarian_result'))
		.map(n => ({ ...n, value: Array.isArray(n.value) ? removeOutputDeclaration(n.value) : n.value }));
}
bodies[names[1]] = removeOutputDeclaration(originalTierBody);
const missingOutput = fixture();
missingOutput.attempt(true);
assert.equal(missingOutput.state.saved.has('acid_rain_humanitarian_tier_registered'), false, 'negative control did not lose undeclared receipt');
bodies[names[1]] = originalTierBody;
console.log(JSON.stringify({ status: 'pass', source_sha256: hash(bytes), helpers: names, cases: 8,
	negative_controls: ['removed caller output declaration loses nested receipt'],
	limits: ['Famine owner acceptance and native arithmetic/scopes are explicit mocks', 'No native pressure, retirement, migration or save/reload proof'] }, null, 2));
