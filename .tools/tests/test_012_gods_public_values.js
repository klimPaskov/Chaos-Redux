// Event 012 committed public-value source model. Run from the mod root.
// Executes production observer/visibility bodies, apply_wrath/floor bodies and
// the actual Strength smoothing/commit tail. SourceNoNativeProof: no engine,
// census, scheduler, scoring, native inventory or GUI rendering is simulated.
const fs = require('fs');
const assert = require('assert/strict');
const { parse, assignment, hash } = require('./lib/clausewitz_source_model.js');
const P = 'gods_of_africa_';
const mainPath = 'common/scripted_effects/012_africa_gods_effects.txt';
const publicPath = 'common/scripted_effects/012_africa_gods_public_values_effects.txt';
const triggerPath = 'common/scripted_triggers/012_africa_gods_public_values_triggers.txt';
const sources = new Map();
const load = path => { const bytes = fs.readFileSync(path); sources.set(path, bytes); return parse(bytes.toString('utf8')); };
const field = (nodes, key) => nodes.find(n => n.key === key)?.value;
const block = (nodes, key) => { const matches = nodes.filter(n => n.key === key); assert.equal(matches.length, 1, key); return matches[0].value; };
const walk = nodes => nodes.flatMap(n => [n, ...(Array.isArray(n.value) ? walk(n.value) : [])]);
const main = load(mainPath), pub = load(publicPath), predicates = load(triggerPath);
const constants = new Map();
for (const category of load('common/script_constants/012_africa_gods_constants.txt'))
	for (const entry of category.value) if (!Array.isArray(entry.value) && Number.isFinite(Number(entry.value)))
		constants.set('constant:' + category.key + '.' + entry.key, Number(entry.value));
const effects = new Map(pub.map(n => [n.key, n.value]));
for (const name of ['apply_wrath', 'enforce_wrath_floor']) effects.set(P + name, block(main, P + name));
const visibility = block(predicates, P + 'public_wrath_is_visible');
const results = [], failures = [], executed = new Set();
function test(name, fn) { try { results.push({ name, status: 'passed', ...fn() }); } catch (e) { failures.push({ name, error: e.message }); } }
function fixture() {
	const country = name => ({ name, vars: new Map(), flags: new Set(), generationIsCurrent: true });
	const host = country('host'), actor = country('actor'), other = country('other'), globals = new Map();
	const f = { host, actor, other, globals, currentHost: host, writes: [], calls: [], temps: new Map(), root: other };
	function ref(token, actor) {
		if (token.startsWith('global.')) return [globals, token.slice(7)];
		assert.ok(!/^(ROOT|PREV|FROM|THIS)\./.test(token), 'unexpected scoped arithmetic ' + token);
		return [actor.vars, token];
	}
	function value(token, actor) {
		if (Number.isFinite(Number(token))) return Number(token);
		if (constants.has(token)) return constants.get(token);
		if (token.startsWith('constant:')) throw Error('unknown constant ' + token);
		if (f.temps.has(token)) return f.temps.get(token);
		const [vars, key] = ref(token, actor); return vars.get(key) ?? 0;
	}
	function condition(nodes, actor) { return nodes.every(n => {
		if (n.key === 'NOT') return !condition(n.value, actor);
		if (n.key === 'AND' || n.key === 'hidden_trigger') return condition(n.value, actor); // hidden_trigger hides the tooltip only; the engine evaluates it like AND
		if (n.key === 'OR') return n.value.some(x => condition([x], actor));
		if (n.key === 'has_variable') { const [vars, key] = ref(n.value, actor); return vars.has(key); }
		if (n.key === 'has_country_flag') return actor.flags.has(n.value);
		if (n.key === 'has_event_target') { assert.equal(n.value, 'africa_host'); return f.currentHost !== null; }
		if (n.key === 'tag') { assert.equal(n.value, 'event_target:africa_host'); return actor === f.currentHost; }
		if (n.key === P + 'participant_generation_is_current') return actor.generationIsCurrent;
		if (n.key === 'check_variable') {
			let left, right, op;
			if (field(n.value, 'var') !== undefined) { left = field(n.value, 'var'); right = field(n.value, 'value'); op = field(n.value, 'compare') ?? 'greater_than_or_equals'; }
			else { [left, right] = assignment(n); op = n.value[0].op; }
			const a = value(left, actor), b = value(right, actor);
			if (['>', 'greater_than'].includes(op)) return a > b;
			if (['<', 'less_than'].includes(op)) return a < b;
			if (['=', 'equals'].includes(op)) return a === b;
			if (op === 'greater_than_or_equals') return a >= b;
			throw Error('unknown comparison ' + op);
		}
		throw Error('unknown predicate ' + n.key);
	}); }
	function run(nodes, actor) {
		let branch = null;
		for (const n of nodes) {
			if (n.key === 'if') { branch = condition(field(n.value, 'limit'), actor); if (branch) run(n.value.filter(x => x.key !== 'limit'), actor); continue; }
			if (n.key === 'else_if') { assert.notEqual(branch, null); if (!branch && condition(field(n.value, 'limit'), actor)) { branch = true; run(n.value.filter(x => x.key !== 'limit'), actor); } continue; }
			if (n.key === 'else') { assert.notEqual(branch, null); if (!branch) run(n.value, actor); branch = null; continue; }
			branch = null;
			if (effects.has(n.key)) { f.calls.push(n.key); executed.add(n.key); run(effects.get(n.key), actor); continue; }
			if (['set_country_flag', 'clr_country_flag'].includes(n.key)) {
				f.writes.push({ actor: actor.name, kind: n.key, key: n.value });
				if (n.key === 'set_country_flag') actor.flags.add(n.value); else actor.flags.delete(n.value);
				continue;
			}
			if (n.key === 'clear_variable') { const [vars, key] = ref(n.value, actor); vars.delete(key); f.writes.push({ actor: vars === globals ? 'global' : actor.name, kind: n.key, key }); continue; }
			if (n.key === 'round_variable') {
				const [vars, key] = ref(n.value, actor), raw = vars.get(key) ?? 0;
				vars.set(key, Math.sign(raw) * Math.floor(Math.abs(raw) + 0.5));
				f.writes.push({ actor: vars === globals ? 'global' : actor.name, kind: n.key, key }); continue;
			}
			if (/^(set|add_to|subtract_from|multiply|divide|clamp)_(temp_)?variable$/.test(n.key)) {
				const temporary = n.key.includes('_temp_');
				const pair = n.key.startsWith('clamp_') ? [field(n.value, 'var'), null] : assignment(n);
				const [vars, key] = temporary ? [f.temps, pair[0]] : ref(pair[0], actor);
				const current = vars.get(key) ?? 0, rhs = pair[1] === null ? null : value(pair[1], actor);
				let result;
				if (n.key.startsWith('set_')) result = rhs;
				else if (n.key.startsWith('add_to_')) result = current + rhs;
				else if (n.key.startsWith('subtract_from_')) result = current - rhs;
				else if (n.key.startsWith('multiply_')) result = current * rhs;
				else if (n.key.startsWith('divide_')) { assert.notEqual(rhs, 0); result = current / rhs; }
				else { const min = field(n.value, 'min'), max = field(n.value, 'max'); result = Math.max(min === undefined ? -Infinity : value(min, actor), Math.min(max === undefined ? Infinity : value(max, actor), current)); }
				vars.set(key, result); f.writes.push({ actor: vars === globals ? 'global' : temporary ? 'temp' : actor.name, kind: n.key, key }); continue;
			}
			throw Error('unknown effect ' + n.key);
		}
	}
	f.run = (name, actor = f.actor) => { executed.add(P + name); f.calls.push(P + name); run(effects.get(P + name), actor); };
	f.runNodes = run; f.visible = actor => condition(visibility, actor); return f;
}
function checkCache(vars, metric, raw) {
	assert.equal(vars.get(P + metric + '_display'), Math.floor(raw));
	assert.ok(Math.abs(vars.get(P + metric + '_fill') - Math.max(0, Math.min(1, raw / constants.get('constant:' + P + 'value.maximum_' + metric)))) < 1e-10);
	assert.equal(vars.get(P + metric + '_frame'), Math.floor(raw) + 1);
}
function trend(actor, metric, direction) {
	assert.equal(actor.flags.has(P + metric + '_trend_rising'), direction === 'rising');
	assert.equal(actor.flags.has(P + metric + '_trend_falling'), direction === 'falling');
}
test('initial_missing_and_incomplete_sample_neutrality', () => {
	const f = fixture(); f.run('observe_public_strength', f.host); f.run('observe_public_wrath'); assert.equal(f.writes.length, 0);
	for (const metric of ['strength', 'wrath']) {
		const actor = metric === 'strength' ? f.host : f.actor, vars = metric === 'strength' ? f.globals : actor.vars;
		for (const incomplete of ['none', 'flag_only', 'previous_only']) {
			actor.flags.delete(P + metric + '_sample_known'); actor.vars.delete(P + metric + '_previous_observed');
			if (incomplete === 'flag_only') actor.flags.add(P + metric + '_sample_known');
			if (incomplete === 'previous_only') actor.vars.set(P + metric + '_previous_observed', 100);
			vars.set(P + metric, 18.75); f.run('observe_public_' + metric, actor);
			checkCache(vars, metric, 18.75); trend(actor, metric, 'neutral'); assert.equal(actor.vars.get(P + metric + '_previous_observed'), 18.75);
		}
	}
	return { firstObservation: 'accurate cache, neutral trend', incompleteSampleCases: 6 };
});
test('rise_fall_steady_and_subpoint_movement', () => {
	for (const metric of ['strength', 'wrath']) {
		const f = fixture(), actor = metric === 'strength' ? f.host : f.actor, vars = metric === 'strength' ? f.globals : actor.vars;
		for (const [raw, direction] of [[19.1, 'neutral'], [19.2, 'rising'], [19.15, 'falling'], [19.15, 'neutral'], [20.1, 'rising'], [19.99, 'falling']]) {
			vars.set(P + metric, raw); f.run('observe_public_' + metric, actor); checkCache(vars, metric, raw); trend(actor, metric, direction);
		}
	}
	return { committedObservationCases: 12 };
});
test('fractional_band_boundaries_and_endpoints', () => {
	let cases = 0;
	for (const [metric, bands] of [['strength', [20, 40, 60, 80]], ['wrath', [15, 30, 50, 70, 85]]]) {
		const f = fixture(), actor = metric === 'strength' ? f.host : f.actor, vars = metric === 'strength' ? f.globals : actor.vars;
		for (const raw of [0, 100, ...bands.flatMap(b => [b - 0.999, b - 0.5, b - 0.001, b, b + 0.001])]) {
			vars.set(P + metric, raw); f.run('observe_public_' + metric, actor); checkCache(vars, metric, raw); assert.equal(vars.get(P + metric), raw); cases++;
		}
	}
	return { cases, exactBoundaryRule: 'floor display never advances raw band' };
});
function strengthPublicationBody() {
	const producer = field(block(main, P + 'refresh_strength'), 'if');
	const gate = producer.find(n => n.key === 'if' && field(n.value, 'limit')?.some(x => x.key === P + 'strength_input_factors_applied'));
	assert.ok(gate, 'actual validated-input publication gate');
	return gate.value;
}
test('actual_strength_smoothing_commit_tail', () => {
	const owner = strengthPublicationBody();
	const start = owner.findIndex(n => n.key === 'if' && walk(n.value).some(x => x.key === 'has_country_flag' && x.value === P + 'strength_immediate'));
	// Earlier capital branches also read strength_immediate only by writing it.
	assert.ok(start >= 0);
	const end = owner.findIndex(n => n.key === P + 'observe_public_strength'); assert.ok(end > start);
	const tail = owner.slice(start, end + 1), f = fixture();
	f.host.vars.set(P + 'strength', 19.9); f.globals.set(P + 'strength', 19.9); f.run('observe_public_strength', f.host);
	const step = constants.get('constant:' + P + 'value.strength_smoothing_step');
	for (const [target, immediate, expectedDirection] of [[90, false, 'rising'], [0, false, 'falling'], [7.75, true, 'falling']]) {
		const before = f.host.vars.get(P + 'strength'); f.temps.set(P + 'strength_target', target);
		if (immediate) f.host.flags.add(P + 'strength_immediate'); else f.host.flags.delete(P + 'strength_immediate');
		f.runNodes(tail, f.host);
		const expected = immediate ? target : before + Math.max(-step, Math.min(step, target - before));
		assert.equal(f.globals.get(P + 'strength'), expected); assert.equal(f.host.vars.get(P + 'strength_previous_observed'), expected);
		checkCache(f.globals, 'strength', expected); trend(f.host, 'strength', expectedDirection);
	}
	return { productionTail: true, projectedTargetExcluded: true, cases: 3 };
});
test('wrath_floor_committed_delta_and_single_observation', () => {
	const f = fixture(), floor = constants.get('constant:' + P + 'wrath.floor_war');
	f.actor.flags.add(P + 'war_floor'); f.actor.vars.set(P + 'wrath', floor); f.run('observe_public_wrath');
	for (const [before, amount, direction, expected, expectedTrend] of [[floor, 20, 'direction_decrease', floor, 'neutral'], [floor + 9, 20, 'direction_decrease', floor, 'falling'], [floor, 2.75, 'direction_increase', floor + 2.75, 'rising']]) {
		f.actor.vars.set(P + 'wrath', before); f.run('observe_public_wrath');
		f.actor.vars.set(P + 'wrath_request', amount); f.actor.vars.set(P + 'wrath_direction', constants.get('constant:' + P + 'wrath.' + direction));
		const calls = f.calls.length; f.run('apply_wrath');
		assert.equal(f.calls.slice(calls).filter(x => x === P + 'observe_public_wrath').length, 1);
		assert.equal(f.actor.vars.get(P + 'wrath'), expected); checkCache(f.actor.vars, 'wrath', expected); trend(f.actor, 'wrath', expectedTrend);
		assert.equal(f.actor.vars.has(P + 'wrath_request'), false); assert.equal(f.actor.vars.has(P + 'wrath_direction'), false);
	}
	f.actor.vars.set(P + 'wrath', 5.25); f.run('observe_public_wrath'); f.run('enforce_wrath_floor');
	assert.equal(f.actor.vars.get(P + 'wrath'), floor); trend(f.actor, 'wrath', 'rising');
	const directCalls = f.calls.length; f.run('enforce_wrath_floor'); trend(f.actor, 'wrath', 'rising');
	assert.equal(f.calls.slice(directCalls).filter(x => x === P + 'observe_public_wrath').length, 0, 'unchanged direct floor never re-observes a movement');
	f.actor.generationIsCurrent = false; const writes = f.writes.length; f.run('enforce_wrath_floor'); assert.equal(f.writes.length, writes);
	return { floorClampedDecrease: 'neutral', partiallyAppliedDecrease: 'falling', directFloorIncrease: 'rising', duplicateDirectFloor: 'preserves recorded movement', invalidGeneration: 'no writes' };
});
test('enrollment_initialization_and_durable_reentry', () => {
	const lifecycle = load('common/scripted_effects/012_africa_gods_lifecycle_effects.txt');
	const initializers = block(lifecycle, P + 'initialize_participant_history').slice(-2);
	assert.ok(walk(initializers).some(n => n.key === 'set_variable' && assignment(n)[0] === P + 'wrath'));
	const enrollment = field(block(main, P + 'register_participant'), 'if');
	const clear = enrollment.find(n => n.key === P + 'clear_public_wrath_values'); assert.ok(clear);
	for (const restored of [false, true]) {
		const f = fixture(); f.actor.flags.add(P + 'war_floor'); f.actor.vars.set(P + 'history_count', 12);
		if (restored) {
			f.actor.vars.set(P + 'wrath', 81.75); f.run('observe_public_wrath');
			f.actor.vars.set(P + 'wrath', 82.75); f.run('observe_public_wrath'); trend(f.actor, 'wrath', 'rising');
		}
		f.runNodes([clear, ...initializers], f.actor); f.run('enforce_wrath_floor');
		const expected = restored ? 82.75 : Math.max(constants.get('constant:' + P + 'value.starting_wrath'), constants.get('constant:' + P + 'wrath.floor_war'));
		assert.equal(f.actor.vars.get(P + 'wrath'), expected); checkCache(f.actor.vars, 'wrath', expected); trend(f.actor, 'wrath', 'neutral');
		assert.equal(f.actor.vars.get(P + 'history_count'), 12);
	}
	return { productionRawInitializerTail: true, firstEnrollmentFloorIncluded: true, reentryHistoryPreserved: true, wholeRegistryLifecycle: 'outside model' };
});
test('cleanup_restoration_actor_isolation_and_visibility', () => {
	const f = fixture(); f.actor.vars.set(P + 'wrath', 73.75); f.actor.vars.set(P + 'history_count', 4); f.actor.flags.add(P + 'permanent_opt_out');
	f.other.vars.set(P + 'wrath', 14.75); f.run('observe_public_wrath', f.other); const isolated = [...f.other.vars];
	f.run('observe_public_wrath'); f.actor.vars.set(P + 'wrath', 74.5); f.run('observe_public_wrath');
	f.run('clear_public_wrath_values'); assert.equal(f.actor.vars.get(P + 'wrath'), 74.5); assert.equal(f.actor.vars.get(P + 'history_count'), 4); assert.ok(f.actor.flags.has(P + 'permanent_opt_out'));
	for (const suffix of ['display', 'fill', 'frame', 'previous_observed']) assert.equal(f.actor.vars.has(P + 'wrath_' + suffix), false);
	f.run('enforce_wrath_floor'); checkCache(f.actor.vars, 'wrath', 74.5); trend(f.actor, 'wrath', 'neutral'); assert.deepEqual([...f.other.vars], isolated);
	f.globals.set(P + 'strength', 60.5); f.run('observe_public_strength', f.host); const globalBefore = [...f.globals];
	f.run('observe_public_strength', f.other); assert.deepEqual([...f.globals], globalBefore);
	f.run('clear_public_strength_observation', f.host); f.run('reset_public_strength_values', f.host); checkCache(f.globals, 'strength', 0); assert.equal(f.globals.get(P + 'strength'), 60.5, 'reset never writes raw Strength');
	f.globals.set(P + 'strength', 18); f.run('observe_public_strength', f.host); trend(f.host, 'strength', 'neutral');
	assert.equal(f.visible(f.actor), true); assert.equal(f.visible(f.host), false);
	f.host.vars.set(P + 'wrath', 74.5); assert.equal(f.visible(f.host), false);
	f.currentHost = null; assert.equal(f.visible(f.actor), true); assert.equal(f.visible(f.host), true);
	const keys = [...f.actor.vars]; const flags = [...f.actor.flags]; f.visible(f.actor); assert.deepEqual([...f.actor.vars], keys); assert.deepEqual([...f.actor.flags], flags);
	return { durableWrathAndHistoryRetained: true, isolatedActors: 3, root: 'unrelated country', absentHost: 'has-variable actor visible' };
});
test('hook_locations_and_presentation_write_inventory', () => {
	const call = (nodes, name) => nodes.findIndex(n => n.key === P + name);
	const init = field(block(main, P + 'initialize_system'), 'if');
	const generation = init.find(n => n.key === 'if').value;
	const globalStart = generation.findIndex(n => n.key === 'set_variable' && assignment(n)[0] === 'global.' + P + 'strength');
	assert.equal(call(generation, 'observe_public_strength'), globalStart + 1);
	const strength = strengthPublicationBody();
	const commit = strength.findIndex(n => n.key === 'set_variable' && assignment(n)[0] === 'global.' + P + 'strength');
	assert.equal(call(strength, 'observe_public_strength'), commit + 1);
	const floor = field(block(main, P + 'enforce_wrath_floor'), 'if'); assert.equal(floor.at(-1).key, P + 'observe_public_wrath_commit');
	assert.equal(walk(block(main, P + 'apply_wrath')).filter(n => n.key === P + 'observe_public_wrath').length, 0, 'no outer duplicate');
	const enrollment = field(block(main, P + 'register_participant'), 'if'); assert.equal(enrollment[1].key, P + 'clear_public_wrath_values');
	assert.ok(call(enrollment, 'refresh_participant_floors') > call(enrollment, 'initialize_participant_history'));
	for (const owner of ['archive_invalid_participant', 'clean_participant', 'cancel_participant', 'finalize_participant'])
		assert.equal(walk(block(main, P + owner)).filter(n => n.key === P + 'clear_public_wrath_values').length, 1, owner);
	const loss = walk(block(main, P + 'cancel_on_unifier_loss')).find(n => n.key === 'if' && Array.isArray(n.value) && n.value.some(x => x.key === P + 'reset_public_strength_values'));
	assert.ok(loss); assert.equal(field(loss.value, 'limit').find(n => n.key === 'tag')?.value, 'event_target:africa_host');
	const allowedVars = new Set(['global.' + P + 'strength_display', 'global.' + P + 'strength_fill', 'global.' + P + 'strength_frame', P + 'strength_previous_observed', P + 'wrath_display', P + 'wrath_fill', P + 'wrath_frame', P + 'wrath_previous_observed']);
	const allowedFlags = new Set(['strength', 'wrath'].flatMap(x => ['trend_rising', 'trend_falling', 'sample_known'].map(y => P + x + '_' + y)));
	for (const n of walk(pub)) {
		if (/^(set|add_to|subtract_from|divide)_variable$/.test(n.key)) assert.ok(allowedVars.has(assignment(n)[0]), n.key);
		if (n.key === 'clamp_variable') assert.ok(allowedVars.has(field(n.value, 'var')));
		if (['round_variable', 'clear_variable'].includes(n.key)) assert.ok(allowedVars.has(n.value));
		if (['set_country_flag', 'clr_country_flag'].includes(n.key)) assert.ok(allowedFlags.has(n.value));
		assert.ok(!n.key.includes('temp_variable'), 'observer never borrows transaction temps');
	}
	return { observerCallsPerCommittedProducer: 1, rawMetricWritesInNewHelpers: 0, temporaryWritesInNewHelpers: 0 };
});
const report = { evidenceKind: 'SourceNoNativeProof', engineEvaluation: false, modelArithmetic: 'JavaScript numbers and documented nearest-integer ties away from zero, not native fixed-point execution', explicitBoundaries: ['participant_generation_is_current is a declared fixture gate', 'only Strength smoothing/commit tail executes, component producers are inputs', 'enrollment/archive/recovery hooks are structurally checked, native lifecycle is unobserved'], sourceHashes: [...sources].map(([path, bytes]) => ({ path, sha256: hash(bytes) })), results, failures, executedProductionHelpers: [...executed].sort() };
console.log(JSON.stringify(report, null, 2));
if (failures.length) process.exitCode = 1;
