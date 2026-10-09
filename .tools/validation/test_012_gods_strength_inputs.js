// Execute actual Strength helper bodies and pure guards under typed source fixtures.
// Native allocation coverage, engine rounding and callback scheduling remain unobserved.
'use strict';
const fs = require('fs'), assert = require('assert/strict');
const { parse, VM, effects, triggers, constants, fixed, country, state } = require('./test_012_gods_industry_helpers.js');
const P = 'gods_of_africa_', F = P + 'strength_', rows = [], arithmetic = [];
const readSource = p => fs.readFileSync(p, 'utf8');
const effectFile = 'common/scripted_effects/012_africa_gods_strength_inputs_effects.txt';
for (const n of parse(readSource(effectFile))) effects[n.key] = n.value;
for (const n of parse(readSource('common/scripted_triggers/012_africa_gods_strength_inputs_triggers.txt'))) triggers[n.key] = n.value;
const existingTriggers = parse(readSource('common/scripted_triggers/012_africa_triggers.txt'));
const nativeDependencies = ['africa_has_current_host', 'africa_member_host_generation_is_current', 'africa_relationship_is_cooperative',
	'africa_relationship_is_protected', 'africa_relationship_is_associate', 'africa_relationship_is_chartered',
	'africa_relationship_is_autonomous_federal', 'africa_relationship_is_integrated_region'];
for (const name of nativeDependencies) {
	const n = existingTriggers.find(x => x.key === name);
	assert.ok(n, name); triggers[name] = n.value;
}
for (const p of ['common/script_constants/012_africa_constants.txt', 'common/script_constants/012_africa_gods_strength_inputs_constants.txt']) {
	for (const cat of parse(readSource(p))) for (const n of cat.value)
		if (typeof n.value === 'string' && Number.isFinite(Number(n.value))) constants[cat.key + '.' + n.key] = Number(n.value);
}
const collectionFile = 'C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/collections/collections.txt';
function namedBlock(source, name) {
	const start = source.search(new RegExp('^' + name + '\\s*=\\s*\\{', 'm'));
	assert.ok(start >= 0, name);
	let end = source.indexOf('{', start), depth = 0;
	do { if (source[end] === '{') depth++; else if (source[end] === '}') depth--; end++; } while (depth > 0);
	return parse(source.slice(start, end))[0].value;
}
// Only this native block is parsed. Other blocks contain bare operators.
const collection = namedBlock(readSource(collectionFile), 'states_in_africa');
assert.equal(collection.find(n => n.key === 'input').value, 'game:all_states');
const geography = collection.find(n => n.key === 'operators').value.find(n => n.key === 'limit').value;
const baselineFile = 'docs/plans/012_africa_plans/subagent_handoffs/012_gods_strength_inputs_2026-10-09_evidence/before/common__scripted_effects__012_africa_gods_effects.txt';
const legacy = namedBlock(readSource(baselineFile), 'gods_of_africa_refresh_strength').find(n => n.key === 'if').value.filter(n => n.key !== 'limit');
const setsTemp = (n, field) => n.key === 'set_temp_variable' && n.value[0].key === F + field;
const milStart = legacy.findIndex(n => setsTemp(n, 'military'));
const indStart = legacy.findIndex(n => setsTemp(n, 'industry'));
const continentStart = legacy.findIndex(n => setsTemp(n, 'continent'));
const reachStart = legacy.findIndex(n => setsTemp(n, 'reach'));
assert.ok(milStart >= 0 && indStart > milStart && continentStart > indStart && reachStart > continentStart);
class InputsVM extends VM {
	constructor() {
		super(); this.worldStates = []; this.worldCountries = [this.host, this.actor];
		this.globalFlags = new Set(['africa_event_active']); this.maxArrayBodyRows = Infinity; this.foreachRuns = [];
		for (const o of [this.host, this.actor]) { o.arrays = {}; o.armyK = 0; o.divisions = 0; o.exile = false; o.getters = {}; }
		this.host.flags.add('africa_unifier_host'); this.host.flags.add('africa_host_commit_completed');
		this.host.arrays.africa_relationship_countries = []; this.host.arrays.gods_of_africa_participants = [];
	}
	scope(token, c) {
		if (token === 'OWNER') return c.scope.owner;
		if (token === 'CONTROLLER') return c.scope.controller;
		return super.scope(token, c);
	}
	value(token, c) {
		if (token === 'global.countries^num') return this.worldCountries.length;
		if (token === 'deployed_army_manpower_k') return c.scope.armyK;
		if (token === 'num_divisions') return c.scope.divisions;
		if (Object.hasOwn(c.scope.getters || {}, token)) return c.scope.getters[token];
		if (token.includes('^') && !token.includes('.')) {
			const [key, i] = token.split('^'), a = c.scope.arrays?.[key] || [];
			return i === 'num' ? a.length : a[Number(i)];
		}
		if (Object.hasOwn(c.scope.arrays || {}, token)) return c.scope.arrays[token];
		return super.value(token, c);
	}
	test(ns, c, mode = 'AND') {
		const mapped = ns.map(n => {
			let answer;
			if (n.key === 'has_global_flag') answer = this.globalFlags.has(n.value);
			else if (n.key === 'is_government_in_exile') answer = c.scope.exile === (n.value === 'yes');
			else if (n.key === 'is_major') answer = !!c.scope.major === (n.value === 'yes');
			else if (n.key === 'is_in_array') {
				const b = Object.fromEntries(n.value.map(x => [x.key, x.value]));
				answer = (this.value(b.array, c) || []).includes(this.value(b.value, c));
			} else if (n.key === 'is_owned_and_controlled_by') {
				const target = this.scope(n.value, c); answer = c.scope.owner === target && c.scope.controller === target;
			}
			return answer === undefined ? n : { key: answer ? 'AND' : 'NOT', value: [] };
		});
		return super.test(mapped, c, mode);
	}
	exec(ns, c) {
		for (let i = 0; i < ns.length; i++) {
			const n = ns[i];
			if (n.key === 'every_collection_element') {
				assert.equal(n.value.find(x => x.key === 'input').value, 'collection:states_in_africa');
				const body = n.value.filter(x => x.key !== 'input');
				for (const s of this.worldStates) {
					const child = this.ctx(s, c, c.root);
					if (this.test(geography, child)) this.exec(body, child);
				}
			} else if (['for_each_scope_loop', 'for_each_loop'].includes(n.key)) {
				const metadata = Object.fromEntries(n.value.filter(x => ['array', 'break', 'value', 'index'].includes(x.key)).map(x => [x.key, x.value]));
				const body = n.value.filter(x => !['array', 'break', 'value', 'index'].includes(x.key));
				const breakVariable = metadata.break || 'break';
				assert(!breakVariable.includes('.'), 'foreach break is an unscoped temporary');
				const a = this.value(metadata.array, c) || [];
				assert(Array.isArray(a), 'foreach requires an array');
				const run = { kind: n.key, array: metadata.array, breakVariable, scope: c.scope.id, root: c.root?.id, rows: [] };
				this.foreachRuns.push(run);
				// No foreach ceiling is inferred. maxArrayBodyRows is an explicit
				// incomplete-observation fixture used by the existing coverage test.
				for (let row = 0; row < Math.min(a.length, this.maxArrayBodyRows); row++) {
					if ((this.temp[breakVariable] ?? 0) !== 0) break;
					const o = a[row];
					if (metadata.index) this.temp[metadata.index] = row;
					if (n.key === 'for_each_loop') this.temp[metadata.value || 'v'] = o;
					else assert(o && ['country', 'state'].includes(o.type), 'foreach scope requires a typed object');
					run.rows.push(n.key === 'for_each_scope_loop' ? o.id : o);
					this.exec(body, n.key === 'for_each_scope_loop' ? this.ctx(o, c, c.root) : c);
				}
			} else if (n.key === 'clear_array') {
				c.scope.arrays[n.value] = [];
			} else if (n.key === 'add_to_array') {
				const b = Object.fromEntries(n.value.map(x => [x.key, x.value]));
				(c.scope.arrays[b.array] ||= []).push(this.value(b.value, c));
			} else {
				let end = i + 1;
				if (n.key === 'if') while (end < ns.length && ['else_if', 'else'].includes(ns[end].key)) end++;
				super.exec(ns.slice(i, end), c); i = end - 1;
			}
		}
	}
}
function test(name, fn) { fn(); rows.push(name); }
function read(v, field) { return v.host.vars[F + field]; }
function run(v, name, scope = v.host, root = scope) { v.call(P + name, v.ctx(scope, null, root)); }
function gate(v, name, scope = v.host, root = scope) { return v.call(P + name, v.ctx(scope, null, root), true); }
function measure(v, root = v.host) { run(v, 'measure_territorial_control', v.host, root); }
function C(id, armyK = 0, exists = true) { return Object.assign(country(id), { arrays: {}, armyK, divisions: armyK > 0 ? 20 : 0, exists, exile: false, getters: {} }); }
function addCountry(v, c) { v.worldCountries.push(c); v.objects.push(c); return c; }
function census(v) {
	run(v, 'initialize_strength_census');
	for (const c of v.worldCountries) run(v, 'remember_strength_country', c);
	run(v, 'finish_strength_census');
}
function prepared() {
	const v = new InputsVM(); v.host.armyK = 200; v.host.divisions = 20; v.actor.armyK = 19800;
	v.worldStates = [state(1, v.host, 0), state(2, v.actor, 0)];
	census(v); run(v, 'measure_strength_armies'); measure(v); return v;
}
function apply(v, military = 10, continent = 60) {
	v.temp[F + 'military'] = military; v.temp[F + 'continent'] = continent;
	run(v, 'apply_strength_input_factors');
	return [v.temp[F + 'military'], v.temp[F + 'continent']];
}
function legacyArithmetic(v) {
	v.temp[F + 'military'] = 0; v.temp[F + 'continent'] = 0;
	v.exec(legacy.slice(milStart, indStart), v.ctx(v.host));
	v.exec(legacy.slice(continentStart, reachStart), v.ctx(v.host));
	return [v.temp[F + 'military'], v.temp[F + 'continent']];
}
module.exports = { InputsVM, parse, effects, triggers, constants, fixed, state, namedBlock, C, addCountry, P, F };
if (require.main === module) {
test('home cores are distinct from continental extent', () => {
	const v = new InputsVM();
	v.worldStates = Array.from({ length: 10 }, (_, i) => state(i + 1, i < 2 ? v.host : v.actor, 0));
	measure(v);
	assert.equal(read(v, 'african_state_total'), 10); assert.equal(read(v, 'african_secured_cores'), 2);
	assert.equal(read(v, 'territorial_control'), 20);
});
test('ownership control cores and Africa geography remain independent', () => {
	const v = new InputsVM(), third = country(3);
	const owned = state(1, v.host, 0); owned.controller = v.actor;
	const occupied = state(2, v.actor, 0); occupied.controller = v.host; occupied.core = v.host;
	const noncore = state(3, v.host, 0); noncore.core = v.actor;
	const secured = state(4, v.host, 0);
	const foreign = state(5, third, 0);
	const europe = state(6, v.host, 0); europe.continent = 'europe';
	v.worldStates = [owned, occupied, noncore, secured, foreign, europe]; measure(v);
	assert.equal(read(v, 'african_state_total'), 5); assert.equal(read(v, 'african_owned_states'), 3);
	assert.equal(read(v, 'african_controlled_states'), 3); assert.equal(read(v, 'african_secured_states'), 2);
	assert.equal(read(v, 'african_core_total'), 3); assert.equal(read(v, 'african_secured_cores'), 1);
	assert.equal(read(v, 'territorial_control'), 20);
});
test('capture reduces physical strength input without changing core claims', () => {
	const v = new InputsVM(); v.worldStates = [state(1, v.host, 0), state(2, v.host, 0)]; measure(v);
	assert.equal(read(v, 'territorial_control'), 100);
	v.worldStates[0].controller = v.actor; v.day++; measure(v);
	assert.equal(read(v, 'african_core_total'), 2); assert.equal(read(v, 'territorial_control'), 50);
	assert.equal(read(v, 'territory_observation_day'), v.day);
});
test('foreign native ROOT cannot receive the host measurement', () => {
	const v = new InputsVM(); v.worldStates = [state(1, v.host, 0)]; const root = country(8); measure(v, root);
	assert.equal(read(v, 'territorial_control'), 100); assert.deepEqual(root.vars, {});
});
test('empty geographic input fails to zero without division by zero', () => {
	const v = new InputsVM(); measure(v); assert.equal(read(v, 'african_state_total'), 0);
	assert.equal(read(v, 'territorial_control'), 0);
});
test('unauthorized former host cannot mutate existing measurements', () => {
	const v = new InputsVM(); v.host.vars[F + 'territorial_control'] = 17;
	v.targets.africa_host = v.actor; measure(v); assert.equal(read(v, 'territorial_control'), 17);
	assert.equal(read(v, 'african_state_total'), undefined);
});

test('real host guards reject each missing identity witness and honor foreign ROOT', () => {
	for (const corrupt of [
		v => { v.targets.africa_host = v.actor; },
		v => { v.host.flags.delete('africa_unifier_host'); },
		v => { v.host.flags.delete('africa_host_commit_completed'); },
		v => { delete v.host.vars.africa_host_generation; },
		v => { delete v.host.vars.africa_origin_host_id; },
		v => { v.globalFlags.delete('africa_event_active'); },
		v => { v.host.exists = false; },
	]) {
		const v = new InputsVM(); corrupt(v); assert.equal(gate(v, 'strength_host_is_current'), false);
		measure(v, C(80)); assert.equal(read(v, 'african_state_total'), undefined);
	}
	const v = prepared(); assert(gate(v, 'strength_host_is_current', v.host, C(80)));
	assert.deepEqual(apply(v), [7.75, 55]); assert(gate(v, 'strength_input_factors_applied', v.host, C(80)));
});
test('remember before initialization is denied; census includes dormant nonhuman special and host objects', () => {
	const v = new InputsVM(); run(v, 'remember_strength_country', v.actor);
	assert.equal(v.host.arrays[F + 'countries'], undefined);
	const dormant = addCountry(v, C(3, 999, false)), nonhuman = addCountry(v, C(4, 20)), special = addCountry(v, C(5, 30));
	nonhuman.nonhuman = true; special.special = true; v.host.armyK = 10; v.actor.armyK = 40;
	census(v); assert.equal(v.host.arrays[F + 'countries'].length, 5);
	run(v, 'remember_strength_country', v.host); run(v, 'remember_strength_country', dormant);
	assert.equal(v.host.arrays[F + 'countries'].length, 5);
	run(v, 'measure_strength_armies'); assert.equal(read(v, 'world_army_k'), 100);
	assert.equal(read(v, 'host_army_k_sample'), 10); assert.equal(read(v, 'army_processed_count'), 5);
	dormant.exists = true; run(v, 'measure_strength_armies'); assert.equal(read(v, 'world_army_k'), 1099);
});
test('government in exile is explicitly measured even if existence fixture is false', () => {
	const v = new InputsVM(), exile = addCountry(v, C(3, 70, false));
	exile.exile = true; v.host.armyK = 10; census(v); run(v, 'measure_strength_armies');
	assert.equal(read(v, 'world_army_k'), 80);
});
test('partial census cannot finish or publish factors', () => {
	const v = new InputsVM(); run(v, 'initialize_strength_census'); run(v, 'remember_strength_country', v.host);
	run(v, 'finish_strength_census'); assert(!gate(v, 'strength_census_is_complete'));
	run(v, 'measure_strength_armies'); measure(v); assert.deepEqual(apply(v, 12, 34), [12, 34]);
	assert(!gate(v, 'strength_input_factors_applied')); assert(v.host.flags.has(F + 'world_coverage_incomplete'));
});
test('unwitnessed allocated object invalidates known coverage until named insertion', () => {
	const v = prepared(), released = addCountry(v, C(9, 300));
	assert(!gate(v, 'strength_census_is_complete')); assert.deepEqual(apply(v), [10, 60]);
	run(v, 'remember_strength_country', released); assert(gate(v, 'strength_census_is_complete'));
	assert(!gate(v, 'strength_army_sample_is_current'));
	run(v, 'measure_strength_armies'); assert.equal(read(v, 'world_army_k'), 20300);
	assert(gate(v, 'strength_army_sample_is_current'));
});
test('host row correction removes old row instead of adding host twice', () => {
	const v = prepared(); v.host.armyK = 100;
	assert.deepEqual(apply(v), [7.6255, 55]);
	assert.equal(read(v, 'world_army_k'), 20000); assert.equal(read(v, 'host_army_k_sample'), 200);
});
test('zero host divisions and zero host manpower independently suppress readiness component', () => {
	for (const which of ['divisions', 'armyK']) { const v = prepared(); v.host[which] = 0; assert.equal(apply(v, 30)[0], 0); assert(gate(v, 'strength_input_factors_applied')); }
});
test('zero world is a valid zero army observation without division by zero', () => {
	const v = prepared(); v.host.armyK = 0; v.host.divisions = 0; v.actor.armyK = 0;
	run(v, 'measure_strength_armies'); assert.equal(read(v, 'world_army_k'), 0);
	assert.equal(apply(v, 30)[0], 0); assert(gate(v, 'strength_input_factors_applied'));
});
test('manpower_k boundaries remain thousand-unit values and never use deprecated raw manpower', () => {
	for (const amount of [0.00001, 2147.48364, 2147.48365, 2147.48366, 2147483]) {
		const v = prepared(); v.host.armyK = amount; v.actor.armyK = amount * 9;
		run(v, 'measure_strength_armies'); assert.equal(read(v, 'world_army_k'), fixed(amount * 10));
		assert.equal(apply(v, 10)[0], 10);
	}
});
test('sample host generation origin and age proofs reject stale cache without mutating caller components', () => {
	for (const field of ['army_sample_host_id', 'army_sample_generation', 'army_sample_origin_host_id']) {
		const v = prepared(); v.host.vars[F + field]++; assert.deepEqual(apply(v, 12, 34), [12, 34]);
		assert(!gate(v, 'strength_input_factors_applied'));
	}
	const v = prepared(); v.day += constants['gods_of_africa_timing.owner_tick_days']; measure(v);
	assert(gate(v, 'strength_input_sample_is_current')); v.day++; measure(v);
	assert.deepEqual(apply(v, 12, 34), [12, 34]); assert(!gate(v, 'strength_input_factors_applied'));
	const future = prepared(); future.host.vars[F + 'army_sample_day']++; assert(!gate(future, 'strength_input_sample_is_current'));
});
test('territory tuple and stale observation reject factors even with current army sample', () => {
	for (const field of ['territory_host_id', 'territory_generation', 'territory_origin_host_id', 'territory_observation_day']) {
		const v = prepared(); v.host.vars[F + field]++; assert.deepEqual(apply(v, 12, 34), [12, 34]);
		assert(!gate(v, 'strength_input_factors_applied'));
	}
	const empty = prepared(); empty.worldStates = []; measure(empty); assert.deepEqual(apply(empty, 12, 34), [12, 34]);
});
test('missing sample and negative army read fail explicitly rather than producing fake world power', () => {
	const v = prepared(); delete v.host.vars[F + 'world_army_k']; assert.deepEqual(apply(v, 12, 34), [12, 34]);
	const bad = prepared(); bad.actor.armyK = -1; run(bad, 'measure_strength_armies');
	assert(!gate(bad, 'strength_army_sample_is_current')); assert(bad.host.flags.has(F + 'army_read_invalid'));
	assert.deepEqual(apply(bad, 12, 34), [12, 34]);
});
test('partial body processing is rejected; retained scope iterator can process a roster over 1000 in this model', () => {
	const v = new InputsVM();
	for (let i = 3; i <= 1003; i++) addCountry(v, C(i, 1));
	census(v); v.maxArrayBodyRows = 1000; run(v, 'measure_strength_armies');
	assert.equal(read(v, 'army_processed_count'), 1000); assert(!gate(v, 'strength_army_sample_is_current'));
	v.maxArrayBodyRows = Infinity; run(v, 'finish_strength_census'); run(v, 'measure_strength_armies');
	assert.equal(read(v, 'army_processed_count'), 1003); assert(gate(v, 'strength_army_sample_is_current'));
	// This verifies the processed-row guard, not native iterator-cap semantics.
});
test('successor row remains single and cache cannot survive an owner identity change', () => {
	const v = prepared(), old = v.host, next = v.actor, saved = old.arrays[F + 'countries'];
	next.armyK = 200; old.armyK = 100; Object.assign(next.vars, { africa_host_generation: 2, africa_origin_host_id: 1 });
	next.flags.add('africa_unifier_host'); next.flags.add('africa_host_commit_completed'); v.targets.africa_host = next;
	Object.assign(next.vars, Object.fromEntries(Object.entries(old.vars).filter(([k]) => k.startsWith(F))));
	for (const flag of old.flags) if (flag.startsWith(F)) next.flags.add(flag);
	next.arrays[F + 'countries'] = [...saved]; next.arrays.africa_relationship_countries = [];
	assert(!gate(v, 'strength_army_sample_is_current', next));
	run(v, 'clear_strength_input_sample', next); assert.deepEqual(next.arrays[F + 'countries'], saved);
	Object.assign(next.vars, { [F + 'census_host_id']: next.id, [F + 'census_generation']: 2, [F + 'census_origin_host_id']: 1 });
	run(v, 'finish_strength_census', next); run(v, 'remember_strength_country', next); run(v, 'measure_strength_armies', next);
	assert.equal(next.vars[F + 'world_army_k'], 300); assert.equal(next.vars[F + 'host_army_k_sample'], 200);
	assert.equal(next.arrays[F + 'countries'].length, 2); assert.equal(next.vars[F + 'army_sample_generation'], 2);
	assert(!gate(v, 'strength_host_is_current', old)); assert.deepEqual(old.arrays[F + 'countries'], saved);
});
test('all five cooperative relationships can supply sovereign member host cores without direct ownership', () => {
	for (const rel of ['protected', 'associate', 'chartered', 'autonomous_federal', 'integrated_region']) {
		const v = prepared(); Object.assign(v.actor.vars, { africa_member_host_generation: 1, africa_relationship_state: constants['africa_relationship.' + rel] });
		v.host.arrays.africa_relationship_countries.push(v.actor); v.worldStates[1].core = v.host;
		measure(v, C(90)); assert.equal(read(v, 'member_states'), 1); assert.equal(read(v, 'member_core_states'), 1);
		assert.equal(read(v, 'territorial_control'), 50); assert.equal(read(v, 'physical_control'), 100);
		assert.equal(apply(v)[1], 80);
	}
});
test('unregistered stale departed capitulated and hostile members cannot supply member land', () => {
	for (const variant of ['unregistered', 'stale', 'capitulated', 'outside', 'resistant', 'leaving', 'rival_bloc', 'occupied_settlement']) {
		const v = prepared(); Object.assign(v.actor.vars, { africa_member_host_generation: 1, africa_relationship_state: constants['africa_relationship.chartered'] });
		v.host.arrays.africa_relationship_countries.push(v.actor); v.worldStates[1].core = v.host;
		if (variant === 'unregistered') v.host.arrays.africa_relationship_countries = [];
		else if (variant === 'stale') v.actor.vars.africa_member_host_generation = 2;
		else if (variant === 'capitulated') v.actor.capitulated = true;
		else v.actor.vars.africa_relationship_state = constants['africa_relationship.' + variant];
		measure(v); assert.equal(read(v, 'member_core_states'), 0); assert.equal(read(v, 'physical_control'), 50);
	}
});
test('member noncores occupation and allied cross control remain separate from secured cores', () => {
	const v = prepared(), invader = addCountry(v, C(3));
	Object.assign(v.actor.vars, { africa_member_host_generation: 1, africa_relationship_state: constants['africa_relationship.chartered'] });
	v.host.arrays.africa_relationship_countries = [v.actor];
	const secured = state(10, v.actor, 0); secured.core = v.host;
	const noncore = state(11, v.actor, 0);
	const captured = state(12, v.actor, 0); captured.core = v.host; captured.controller = invader;
	const cross = state(13, v.actor, 0); cross.core = v.host; cross.controller = v.host;
	v.worldStates = [state(9, v.host, 0), secured, noncore, captured, cross];
	measure(v, C(80)); assert.equal(read(v, 'member_states'), 2); assert.equal(read(v, 'member_core_states'), 1);
	assert.equal(read(v, 'occupied_states'), 1); assert.equal(read(v, 'territorial_control'), 20);
	assert.equal(read(v, 'physical_control'), 40); assert.equal(read(v, 'african_controlled_states'), 2);
});
test('cleanup clears private measurements while retaining census roster receipts and unrelated state', () => {
	const v = prepared(), roster = [...v.host.arrays[F + 'countries']]; v.host.vars.unrelated = 55;
	run(v, 'clear_strength_input_sample'); assert.deepEqual(v.host.arrays[F + 'countries'], roster);
	assert(v.host.flags.has(F + 'census_initialized')); assert(v.host.flags.has(F + 'census_complete'));
	assert.equal(read(v, 'world_army_k'), undefined); assert.equal(read(v, 'african_secured_cores'), undefined);
	assert.equal(v.host.vars.unrelated, 55); assert(!gate(v, 'strength_input_factors_applied'));
});
test('caller temp ownership and unknown helper rejection remain real VM contracts', () => {
	const v = prepared(); v.temp[F + 'military'] = 10;
	run(v, 'apply_strength_input_factors'); assert.equal(v.temp[F + 'military'], 10);
	assert(!gate(v, 'strength_input_factors_applied'));
	assert.throws(() => v.exec(parse('made_up_strength_helper = yes'), v.ctx(v.host)), /Unsupported source effect/);
	assert.throws(() => v.test(parse('made_up_strength_trigger = yes'), v.ctx(v.host)), /Unsupported source trigger/);
	apply(v); assert.deepEqual(Object.keys(v.temp).sort(), [F + 'continent', F + 'military'].sort());
});
test('weak strong competition occupation and zero cases compare actual legacy arithmetic with source helpers', () => {
	for (const fixture of [
		{ name: 'weak', divisions: 20, readiness: 20, army: 200, foreign: 19800, held: 5, expectedM: 8.1375, expectedC: 32.5 },
		{ name: 'strong', divisions: 800, readiness: 80, army: 4000, foreign: 16000, held: 80, political: 80, expectedM: 60, expectedC: 80 },
		{ name: 'world anchor', divisions: 400, readiness: 60, army: 2000, foreign: 18000, held: 80, expectedM: 40, expectedC: 70 },
		{ name: 'world competition', divisions: 400, readiness: 60, army: 2000, foreign: 48000, held: 80, expectedM: 34, expectedC: 70 },
		{ name: 'occupation', divisions: 400, readiness: 60, army: 2000, foreign: 18000, held: 30, expectedM: 40, expectedC: 45 },
		{ name: 'zero despite readiness', divisions: 0, readiness: 60, army: 0, foreign: 18000, held: 80, expectedM: 0, expectedC: 70 },
		{ name: 'sustainment floor', divisions: 400, readiness: 60, army: 2000, foreign: 18000, held: 80, equip: 0, fuel: 0, expectedM: 16, expectedC: 70 },
	]) {
		const v = new InputsVM(); v.host.divisions = fixture.divisions; v.host.armyK = fixture.army; v.actor.armyK = fixture.foreign;
		const political = fixture.political || 60;
		Object.assign(v.host.vars, { africa_continental_war_readiness: fixture.readiness, africa_cooperative_relationship_count: political, africa_charter_authority: political });
		Object.assign(v.host.getters, { 'num_target_equipment_in_armies_k@infantry_equipment': 100,
			'num_equipment_in_armies_k@infantry_equipment': 100 * (fixture.equip ?? 1), max_fuel_k: 100, fuel_k: 100 * (fixture.fuel ?? 1) });
		v.worldStates = Array.from({ length: 100 }, (_, i) => state(i + 1, i < fixture.held ? v.host : v.actor, 0));
		census(v); run(v, 'measure_strength_armies'); measure(v);
		const old = legacyArithmetic(v), after = apply(v, ...old);
		assert.equal(after[0], fixture.expectedM, fixture.name); assert.equal(after[1], fixture.expectedC, fixture.name);
		assert(after[0] <= old[0]); assert(gate(v, 'strength_input_factors_applied'));
		arithmetic.push({ case: fixture.name, oldMilitary: old[0], military: after[0], oldContinent: old[1], continent: after[1],
			rawWeightedDelta: fixed((after[0] - old[0]) * constants['gods_of_africa_value.strength_military_weight'] / 100 + (after[1] - old[1]) * constants['gods_of_africa_value.strength_continent_weight'] / 100) });
	}
});
console.log(JSON.stringify({ evidenceKind: 'SourceNoNativeProof', cases: rows.length, rows, arithmetic,
	fixedPointModel: '5 decimal truncation, no native range claim', productionBodiesExecuted: true,
	externalNativeFixtures: 'state/country getters, flags, scope iterators and arrays',
	pureDependencyBodies: nativeDependencies, integration: 'owner helpers delivered, parent wiring and weighted-consumer audit pending' }));
}
