/* Bounded actual-source Event 012 Strength caller replay. No native proof.
 * Reuses the owner VM's conservative helper-frame lifetime and 5dp arithmetic.
 * Import is silent and writes nothing. CLI evidence stays in its owned folder.
 * Run from the repository root: node .tools/validation/test_012_gods_strength_integration.js
 */
'use strict';
const fs = require('node:fs'), path = require('node:path'), crypto = require('node:crypto');
const assert = require('node:assert/strict');
const { InputsVM, parse, effects, triggers, constants, fixed, state, namedBlock, C, addCountry, P, F } = require('./test_012_gods_strength_inputs.js');
const root = path.resolve(__dirname, '../..');
const handoffs = 'docs/plans/012_africa_plans/subagent_handoffs/';
const evidenceDir = path.join(root, handoffs, 'own_strength_integration_evidence');
const manifestPath = handoffs + '012_gods_strength_inputs_2026-10-09_evidence/before/manifest.json';
const hashes = new Map(), sources = new Map(), executed = new Set(), subtrees = [];
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
function read(p) {
	if (!sources.has(p)) { const bytes = fs.readFileSync(path.join(root, p)); hashes.set(p, sha(bytes)); sources.set(p, bytes.toString('utf8')); }
	return sources.get(p);
}
const main = 'common/scripted_effects/012_africa_gods_effects.txt';
const world = 'common/scripted_effects/012_africa_world_order_effects.txt';
const transfer = 'common/scripted_effects/012_africa_host_transfer_effects.txt';
const recovery = 'common/scripted_effects/012_africa_gods_recovery_effects.txt';
for (const p of ['.tools/validation/test_012_gods_strength_integration.js', '.tools/validation/test_012_gods_strength_inputs.js', '.tools/validation/test_012_gods_industry_helpers.js']) read(p);
function install(p, names, store = effects) { for (const n of names) store[n] = namedBlock(read(p), n); }
install(main, ['refresh_strength', 'activate_system', 'run_owner_tick', 'initialize_registry', 'remember_candidate', 'try_register_participant', 'clean_system', 'initialize_system', 'start_consolidation', 'cancel_on_unifier_loss', 'emit_global_credibility_super_event'].map(n => P + n));
install(recovery, ['revoke_current_epoch', 'close_recovery_requests', 'clear_recovery_member_request'].map(n => P + n));
install('common/scripted_effects/012_africa_gods_public_values_effects.txt', ['observe_public_strength', 'clear_public_strength_observation', 'reset_public_strength_values'].map(n => P + n));
install(transfer, ['africa_host_transfer_restore_world_order_state', 'africa_host_transfer_stage_scalar_ledger', 'africa_host_transfer_stage_arrays']);
install('common/scripted_triggers/012_africa_gods_triggers.txt', ['has_current_host', 'active_host_is_valid', 'system_can_activate', 'consolidation_ready', 'owner_tick_due', 'candidate_is_valid', 'candidate_can_be_remembered', 'participant_is_valid', 'participant_can_register'].map(n => P + n), triggers);
install('common/scripted_triggers/012_africa_gods_recovery_triggers.txt', ['authority_owner_object_is_current', 'authority_owner_has_physical_return', 'epoch_permission_is_current'].map(n => P + n), triggers);
install('common/scripted_triggers/012_africa_triggers.txt', ['africa_is_current_host'], triggers);
for (const p of ['common/script_constants/012_africa_action_constants.txt', 'common/script_constants/012_africa_event_log_constants.txt'])
	for (const cat of parse(read(p))) for (const n of cat.value)
		if (typeof n.value === 'string' && Number.isFinite(Number(n.value))) constants[cat.key + '.' + n.key] = Number(n.value);
for (const n of namedBlock(read('common/script_constants/012_africa_world_order_constants.txt'), 'africa_world_super_event'))
	if (typeof n.value === 'string' && Number.isFinite(Number(n.value))) constants['africa_world_super_event.' + n.key] = Number(n.value);
for (const p of ['common/scripted_effects/012_africa_gods_strength_inputs_effects.txt', 'common/scripted_triggers/012_africa_gods_strength_inputs_triggers.txt', 'common/script_constants/012_africa_gods_strength_inputs_constants.txt', 'common/script_constants/012_africa_constants.txt', 'common/script_constants/012_africa_gods_constants.txt']) {
	// Already parsed by the owner VM. These required inputs must also be hashed.
	read(p);
}
// Read the real shared Chaos endpoint from its schema-independent leaf.
{
	const p = 'common/script_constants/chaos_meter_constants.txt';
	const finalTier = read(p).match(/^\s*tier_final\s*=\s*\{[^{}]*\}/m);
	assert(finalTier, 'real final-tier leaf declaration');
	constants['chaos_meter_tier_range.tier_final.min'] = Number(parse(finalTier[0])[0].value.find(n => n.key === 'min').value);
}
const walk = ns => ns.flatMap(n => [n, ...(Array.isArray(n.value) ? walk(n.value) : [])]);
const field = (ns, key) => { const n = ns.find(x => x.key === key); assert(n, key); return n.value; };
function retained(p, name, select, description) {
	const full = namedBlock(read(p), name), selected = select(full);
	assert(selected.length, description);
	subtrees.push({ path: p, caller: name, description, fullBodyHash: sha(JSON.stringify(full)), selectedBodyHash: sha(JSON.stringify(selected)) });
	return selected;
}
// Exact caller subtrees, preserving order, limits and source node identities.
const worldCensus = retained(world, 'africa_initialize_scramble_and_world_packages', full => {
	const body = field(full, 'if');
	const initialize = body.find(n => n.key === P + 'initialize_strength_census');
	const loop = body.find(n => n.key === 'for_each_scope_loop' && field(n.value, 'array') === 'global.countries');
	const finish = body.find(n => n.key === P + 'finish_strength_census');
	assert(body.indexOf(initialize) < body.indexOf(loop) && body.indexOf(loop) < body.indexOf(finish));
	const reset = body[body.indexOf(loop) - 1];
	assertPrivateReset(reset, loop, 'africa_initialize_scramble_and_world_packages');
	return [initialize, reset, loop, finish];
}, 'one-time census initialize, complete global.countries loop before candidate filter, finish');
const stageScalars = retained(transfer, 'africa_host_transfer_stage_scalar_ledger', full => full.filter(n => /strength_census/.test(JSON.stringify(n))), 'Strength flags and cardinality staging');
const stageArrays = retained(transfer, 'africa_host_transfer_stage_arrays', full => full.filter((n, i) => /strength_countries/.test(JSON.stringify(n)) || (full[i + 1]?.key === 'for_each_scope_loop' && /strength_countries/.test(JSON.stringify(full[i + 1])) && assertPrivateReset(n, full[i + 1], 'africa_host_transfer_stage_arrays'))), 'complete measurement-country object array staging with adjacent reset');
const control = field(field(field(parse(read('common/on_actions/012_africa_gods_on_actions.txt')), 'on_actions'), 'on_state_control_changed'), 'effect');
const manifest = JSON.parse(read(manifestPath));
const beforeSources = manifest.sources.map(s => ({...s, verified: sha(fs.readFileSync(path.join(root, s.snapshot))) === s.sha256}));
for (const s of manifest.sources) read(s.path);
const baseline = namedBlock(read(manifest.sources.find(s => s.path === main).snapshot), P + 'refresh_strength');

function assertPrivateReset(reset, loop, owner) {
	const binding = loop.value.find(n => n.key === 'break');
	assert(binding && /_break_[1-9][0-9]*$/.test(binding.value), 'private foreach binding');
	assert.equal(loop.value.filter(n => n.key === 'break').length, 1, 'one break binding per foreach');
	assert.equal(binding.op, '=');
	if (owner) assert.match(binding.value, new RegExp('^' + owner + '_break_[1-9][0-9]*$'), 'private break belongs to the caller');
	assert.deepEqual(reset, {key: 'set_temp_variable', op: '=', value: [{key: binding.value, op: '=', value: 'constant:gods_of_africa_value.zero'}]}, 'exact adjacent private reset');
	return true;
}
// Project only reviewed iterator descriptors from the older Strength baseline.
// Every other producer, scope, price, weight and arithmetic node stays intact.
function withoutPrivateForeachState(ns, owner = P + 'refresh_strength') {
	const out = [];
	for (let i = 0; i < ns.length; i++) {
		const n = ns[i], next = ns[i + 1];
		if (n.key === 'set_temp_variable' && next?.key === 'for_each_scope_loop' && next.value.some(x => x.key === 'break' && /_break_[1-9][0-9]*$/.test(x.value))) {
			assertPrivateReset(n, next, owner);
			out.push({...next, value: withoutPrivateForeachState(next.value.filter(x => x.key !== 'break'), owner)}); i++;
		} else out.push(Array.isArray(n.value) ? {...n, value: withoutPrivateForeachState(n.value, owner)} : n);
	}
	return out;
}

// Named, deliberately untested unrelated routes. No Strength producer, guard,
// cache observer or output can be replaced through this boundary registry.
const effectBoundaries = new Set([
	P + 'register_participant', P + 'review_industry_program', P + 'capture_industry_retirement',
	P + 'build_need_profile', P + 'dispatch_next_demand', P + 'clear_response_view',
	P + 'retire_owned_industry_program', P + 'record_milestone', 'africa_refresh_continental_focus_tree_layout',
	'africa_world_emit_super_event'
]);
const triggerBoundaries = {
	is_actual_nonhuman_country: (v, c) => c.scope.nonhuman,
	is_special_chaos_country: (v, c) => c.scope.special,
	africa_focus_first_proof_satisfied: (v, c) => c.scope.firstProof,
	[P + 'continent_is_secured']: v => v.secured,
	[P + 'recovery_mandate_is_current']: v => v.recoveryMandate,
	[P + 'participant_has_active_demand']: () => false,
	[P + 'instalment_is_due']: () => false,
	[P + 'participant_needs_reconciliation']: () => false
};
const nativeGetters = new Set(['deployed_army_manpower_k', 'num_divisions', 'num_target_equipment_in_armies_k@infantry_equipment', 'num_equipment_in_armies_k@infantry_equipment', 'max_fuel_k', 'fuel_k', 'num_of_civilian_factories', 'num_of_military_factories', 'stability', 'surrender_progress']);
const declaredVariables = new Set(), declaredArrays = new Set();
for (const body of [...Object.values(effects), ...Object.values(triggers), worldCensus, stageScalars, stageArrays, control]) for (const n of walk(body)) {
	if (n.key === 'has_variable') declaredVariables.add(n.value.replace(/^global\./, ''));
	if (/_variable$/.test(n.key) && Array.isArray(n.value)) {
		const b = Object.fromEntries(n.value.map(x => [x.key, x.value]));
		declaredVariables.add((b.var || n.value[0].key).replace(/^global\./, ''));
	}
	if (/^(clear|round)_variable$/.test(n.key)) declaredVariables.add(n.value.replace(/^global\./, ''));
	if (n.key === 'array' && typeof n.value === 'string') declaredArrays.add(n.value.replace(/^global\./, ''));
	if (n.key === 'clear_array') declaredArrays.add(n.value.replace(/^global\./, ''));
}
// Input fields of preserved component producers and the native identity tuple.
for (const n of ['africa_origin_host_id', 'africa_host_generation', 'chaos_meter_value']) declaredVariables.add(n);
function decorate(c) {
	Object.assign(c, { arrays: c.arrays || {}, getters: {
		'num_target_equipment_in_armies_k@infantry_equipment': 100,
		'num_equipment_in_armies_k@infantry_equipment': 100, max_fuel_k: 100, fuel_k: 100,
		num_of_civilian_factories: 20, num_of_military_factories: 10, stability: 0.8, surrender_progress: 0
	}, techs: new Set(['radio', 'radio_detection', 'construction5', 'advanced_machine_tools', 'fighter3', 'synth_oil_experiments']),
		ai: true, nonhuman: false, special: false, firstProof: true, major: false });
	return c;
}
class IntegrationVM extends InputsVM {
	constructor() {
		super(); this.global = {type: 'global', vars: {chaos_meter_value: 500}, arrays: {countries: this.worldCountries}};
		this.calls = []; this.boundaryCalls = []; this.armyReads = []; this.writes = []; this.nativeClockCalls = []; this.componentFrames = [];
		this.secured = false; this.recoveryMandate = false;
		for (const c of this.worldCountries) decorate(c);
		this.worldStates = Array.from({length: 10}, (_, i) => state(100 + i, i < 8 ? this.host : this.actor, 0));
		for (const c of this.worldCountries) { c.states = this.worldStates.filter(s => s.owner === c); c.capital = c.states[0]; }
		this.objects.push(...this.worldStates);
		Object.assign(this.host.vars, {africa_continental_war_readiness: 60, africa_central_capacity: 80,
			africa_cooperative_relationship_count: 60, africa_charter_authority: 60, africa_continental_reach: 40,
			gods_of_africa_restoration_generation: 1, gods_of_africa_authority_host_id: 1,
			gods_of_africa_authority_host_generation: 1, gods_of_africa_authority_origin_host_id: 1,
			gods_of_africa_candidate_count: 0, gods_of_africa_active_demand_count: 0,
			gods_of_africa_consolidation_due_day: this.day});
		this.host.flags.add(P + 'epoch_authorized'); this.host.flags.add(P + 'consolidation_pending');
		this.host.arrays[P + 'candidate_registry'] = [];
		this.host.armyK = 2000; this.host.divisions = 400; this.actor.armyK = 18000;
		for (const f of ['africa_is_one', 'africa_evolution_i_logged']) this.globalFlags.add(f);
	}
	ctx(scope, prev = null, root = scope) { const c = super.ctx(scope, prev, root); c.from = prev?.from || null; return c; }
	scope(token, c) {
		if (token === 'global') return this.global;
		if (token === 'FROM') return c.from;
		if (token === 'FROM.FROM') return c.from?.from;
		if (token === 'capital_scope') { assert.equal(c.scope.type, 'country'); assert(c.scope.capital, 'explicit capital fixture required'); return c.scope.capital; }
		return super.scope(token, c);
	}
	value(token, c) {
		if (typeof token === 'number') return token;
		assert.equal(typeof token, 'string', 'value token must be explicit');
		if (Number.isFinite(Number(token)) || token.startsWith('constant:') || token === 'global.num_days') return super.value(token, c);
		if (token.startsWith('var:')) return this.value(token.slice(4), c);
		if (token === 'global.countries') return this.worldCountries;
		if (token === 'global.countries^num') return this.worldCountries.length;
		if (token.includes('.')) { const at = token.indexOf('.'), s = this.scope(token.slice(0, at), c); assert(s, 'Unknown value scope ' + token); return this.value(token.slice(at + 1), this.ctx(s, c, c.root)); }
		if (nativeGetters.has(token)) {
			assert.equal(c.scope.type, 'country', token + ' requires country');
			if (token === 'deployed_army_manpower_k') { this.armyReads.push({id: c.scope.id, day: this.day}); assert(Number.isFinite(c.scope.armyK)); return c.scope.armyK; }
			if (token === 'num_divisions') { assert(Number.isFinite(c.scope.divisions)); return c.scope.divisions; }
			assert(Object.hasOwn(c.scope.getters, token), 'Missing native getter ' + token); return c.scope.getters[token];
		}
		if (['THIS', 'PREV', 'ROOT', 'FROM', 'FROM.FROM', 'OWNER', 'CONTROLLER'].includes(token) || token.startsWith('event_target:')) { const s = this.scope(token, c); assert(s, 'Missing scope ' + token); return s; }
		if (token === 'id') return c.scope.id;
		if (declaredArrays.has(token)) return c.scope.arrays[token] || [];
		if (token.includes('^')) { assert(declaredArrays.has(token.split('^')[0]), 'Unknown array ' + token); return super.value(token, c); }
		if (Object.hasOwn(c.scope.arrays || {}, token)) return super.value(token, c);
		assert(Object.hasOwn(this.temp, token) || declaredVariables.has(token), 'Unknown getter/variable ' + token);
		return super.value(token, c);
	}
	variable(n, c) {
		let node = n, context = c;
		if (!n.key.includes('temp_variable')) {
			const b = Object.fromEntries(n.value.map(x => [x.key, x.value]));
			const key = b.var || n.value[0].key;
			if (key.startsWith('global.')) {
				node = {...n, value: n.value.map(x => x.key === 'var' ? {...x, value: key.slice(7)} : x.key === key ? {...x, key: key.slice(7), value: this.value(x.value, c)} : ['value', 'min', 'max'].includes(x.key) ? {...x, value: this.value(x.value, c)} : x)};
				context = {...c, scope: this.global};
			}
			this.writes.push({scope: context.scope.type === 'global' ? 'global' : context.scope.id, key, operation: n.key});
		}
		return super.variable(node, context);
	}
	call(name, c, trigger = false) {
		assert(Object.hasOwn(trigger ? triggers : effects, name), 'Unknown helper ' + name);
		executed.add(name); this.calls.push({name, id: c.scope.id, root: c.root?.id, day: this.day});
		const result = super.call(name, c, trigger);
		if (name === P + 'apply_strength_input_factors') this.componentFrames.push(Object.fromEntries(['military', 'industry', 'continent', 'reach', 'internal', 'chaos'].map(k => [k, this.temp[F + k]])));
		return result;
	}
	test(ns, c, mode = 'AND') {
		const mapped = ns.map(n => {
			let answer;
			if (Object.hasOwn(triggerBoundaries, n.key)) { answer = triggerBoundaries[n.key](this, c); assert.equal(typeof answer, 'boolean', n.key); this.boundaryCalls.push(n.key); }
			if (n.key === 'has_tech') { assert(c.scope.techs instanceof Set, 'explicit tech set'); answer = c.scope.techs.has(n.value); }
			if (n.key === 'is_ai') answer = c.scope.ai === (n.value === 'yes');
			if (n.key === 'has_variable' && n.value.startsWith('global.')) answer = Object.hasOwn(this.global.vars, n.value.slice(7));
			if (answer !== undefined && n.value === 'no' && Object.hasOwn(triggerBoundaries, n.key)) answer = !answer;
			return answer === undefined ? n : {key: answer ? 'AND' : 'NOT', value: []};
		});
		return super.test(mapped, c, mode);
	}
	exec(ns, c) {
		for (let i = 0; i < ns.length; i++) {
			const n = ns[i];
			if (effectBoundaries.has(n.key)) { this.boundaryCalls.push(n.key); continue; }
			if (n.key === 'country_event') { this.nativeClockCalls.push({id: field(n.value, 'id'), days: this.value(field(n.value, 'days'), c)}); continue; }
			if (['set_global_flag', 'clr_global_flag'].includes(n.key)) { assert.equal(typeof n.value, 'string', 'timed flags require explicit boundary'); this.globalFlags[n.key === 'set_global_flag' ? 'add' : 'delete'](n.value); continue; }
			if (['clear_variable', 'round_variable'].includes(n.key) && typeof n.value === 'string') {
				const global = n.value.startsWith('global.'), store = global ? this.global.vars : c.scope.vars, key = global ? n.value.slice(7) : n.value;
				if (n.key === 'clear_variable') delete store[key]; else store[key] = Math.sign(store[key]) * Math.floor(Math.abs(store[key]) + 0.5);
				continue;
			}
			if (n.key === 'clear_array' && n.value.startsWith('global.')) { this.global.arrays[n.value.slice(7)] = []; continue; }
			if (n.key === 'add_to_array' && field(n.value, 'array').startsWith('global.')) {
				(this.global.arrays[field(n.value, 'array').slice(7)] ||= []).push(this.value(field(n.value, 'value'), c)); continue;
			}
			let end = i + 1;
			if (n.key === 'if') while (end < ns.length && ['else', 'else_if'].includes(ns[end].key)) end++;
			super.exec(ns.slice(i, end), c); i = end - 1;
		}
	}
}
function invoke(v, n, scope = v.host, rootScope = scope) { v.call(n.startsWith('africa_') ? n : P + n, v.ctx(scope, null, rootScope)); }
function executeRetained(v, body, context) {
	const before = new Set(Object.keys(v.temp));
	try { v.exec(body, context); }
	finally { for (const key of Object.keys(v.temp)) if (!before.has(key)) delete v.temp[key]; }
}
function sample(v) { executeRetained(v, worldCensus, v.ctx(v.host)); invoke(v, 'measure_strength_armies'); return v; }
function fixture() { return sample(new IntegrationVM()); }
function activate(v) { invoke(v, 'activate_system'); return v; }
function refresh(v, foreign = v.host) { invoke(v, 'refresh_strength', v.host, foreign); }
function strength(v) { return v.global.vars[P + 'strength']; }
function assertPublished(v, expected) {
	assert.equal(strength(v), expected); assert.equal(v.host.vars[P + 'strength'], expected);
	assert.equal(v.host.vars[P + 'strength_previous_observed'], expected);
	assert.equal(v.global.vars[P + 'strength_display'], Math.floor(expected));
	assert.equal(v.global.vars[P + 'strength_frame'], Math.floor(expected) + 1);
	assert.equal(v.global.vars[P + 'strength_fill'], fixed(expected / 100));
	assert(!v.host.flags.has(F + 'input_publication_blocked')); assert.deepEqual(v.temp, {});
}
function snapshotPublic(v) { return JSON.stringify({global: v.global.vars, local: Object.fromEntries(Object.entries(v.host.vars).filter(([k]) => [P + 'strength', P + 'strength_band', P + 'strength_previous_observed'].includes(k))), flags: [...v.host.flags].filter(k => /strength_(trend|sample_known)/.test(k)).sort()}); }
function callCount(v, name) { return v.calls.filter(c => c.name === P + name).length; }
function callback(v, site, old, next) {
	const c = v.ctx(next, null, next); c.from = old; old.from = site;
	try { v.exec(control, c); } finally { delete old.from; }
}
const cases = [], arithmetic = [];
function test(name, fn) { try { fn(); cases.push({name, passed: true}); } catch (e) { cases.push({name, passed: false, error: e.message, stack: e.stack.split('\n').slice(0, 5)}); } }
function runSuite() {
	cases.length = 0; arithmetic.length = 0; executed.clear();
	test('pinned_eight_source_hashes_and_preserved_weighted_penalty_smoothing_tail', () => {
		assert.equal(beforeSources.length, 8); assert(beforeSources.every(s => s.verified));
		const oldBody = field(baseline, 'if').filter(n => n.key !== 'limit');
		const current = withoutPrivateForeachState(field(effects[P + 'refresh_strength'], 'if').filter(n => n.key !== 'limit'));
		assert.deepEqual(field(field(effects[P + 'refresh_strength'], 'if'), 'limit'), parse(P + 'strength_host_is_current = yes'));
		const index = oldBody.findIndex(n => n.key === 'set_temp_variable' && n.value[0].key === F + 'target'); assert(index > 0);
		const gate = current.find(n => n.key === 'if' && walk(n.value).some(x => x.key === P + 'strength_input_factors_applied'));
		assert(gate); assert.deepEqual(gate.value.filter(n => n.key !== 'limit' && !(n.key === 'clr_country_flag' && n.value === F + 'input_publication_blocked')), oldBody.slice(index));
		assert.deepEqual(current.filter(n => ![P + 'measure_territorial_control', P + 'apply_strength_input_factors'].includes(n.key)).slice(0, index), oldBody.slice(0, index));
		assert(!walk(effects[P + 'refresh_strength']).some(n => n.key === P + 'measure_strength_armies' || n.key === 'every_country'));
		assert.deepEqual(['military', 'industry', 'continent', 'reach', 'internal', 'chaos'].map(k => constants['gods_of_africa_value.strength_' + k + '_weight']), [25, 20, 20, 15, 10, 10]);
		for (const [k, value] of Object.entries({divisions_divisor: 20, evolution_ii_amplifier: 15, evolution_iii_amplifier: 25})) assert.equal(constants['gods_of_africa_strength.' + k], value);
		for (const [k, value] of Object.entries({equipment_share: 0.6, fuel_share: 0.4, floor: 0.4, span: 0.6})) assert.equal(constants['gods_of_africa_strength_sustain.' + k], value);
		assert.equal(constants['chaos_meter_tier_range.tier_final.min'], 1000);
	});
	test('real_census_before_candidate_filter_retains_host_dormant_nonhuman_special', () => {
		const v = new IntegrationVM(), dormant = decorate(addCountry(v, C(3, 900, false))), nonhuman = decorate(addCountry(v, C(4, 100))), special = decorate(addCountry(v, C(5, 300)));
		nonhuman.nonhuman = true; special.special = true; sample(v);
		assert.deepEqual(v.host.arrays[F + 'countries'], v.worldCountries);
		assert(!v.host.arrays[P + 'candidate_registry'].includes(v.host)); assert(!v.host.arrays[P + 'candidate_registry'].includes(nonhuman)); assert(!v.host.arrays[P + 'candidate_registry'].includes(special));
		assert(v.host.arrays[P + 'candidate_registry'].includes(dormant)); assert.equal(v.host.vars[F + 'world_army_k'], 20400);
		assert.equal(v.host.vars[F + 'army_processed_count'], 5);
		dormant.exists = true; invoke(v, 'measure_strength_armies'); assert.equal(v.host.vars[F + 'world_army_k'], 21300);
	});
	test('actual_full_refresh_foreign_ROOT_commits_causal_weighted_result_and_cache', () => {
		const v = new IntegrationVM(), foreign = decorate(addCountry(v, C(90))); sample(v); refresh(v, foreign); assertPublished(v, 58.5); assert.deepEqual(foreign.vars, {});
		assert.deepEqual(v.componentFrames.at(-1), {military: 40, industry: 70, continent: 70, reach: 50, internal: 80, chaos: 50});
		// (40*25 + 70*20 + 70*20 + 50*15 + 80*10 + 50*10) / 100 = 58.5.
		arithmetic.push({scenario: 'full foreign ROOT', military: 40, industry: 70, continent: 70, reach: 50, internal: 80, chaos: 50, published: 58.5});
	});
	for (const [name, change] of [
		['missing_world_sample', v => { delete v.host.vars[F + 'world_army_k']; }],
		['stale_age', v => { v.day += 31; }],
		['future_sample', v => { v.host.vars[F + 'army_sample_day']++; }],
		['wrong_sample_host', v => { v.host.vars[F + 'army_sample_host_id']++; }],
		['wrong_sample_generation', v => { v.host.vars[F + 'army_sample_generation']++; }],
		['wrong_sample_origin', v => { v.host.vars[F + 'army_sample_origin_host_id']++; }],
		['partial_processed_rows', v => { v.host.vars[F + 'army_processed_count']--; }],
		['unwitnessed_new_object', v => { decorate(addCountry(v, C(9, 300))); }],
		['negative_army_observation', v => { v.actor.armyK = -1; invoke(v, 'measure_strength_armies'); }],
		['negative_current_host_army', v => { v.host.armyK = -1; }],
		['missing_Africa_geography', v => { v.worldStates = []; }]
	]) test('publication_gate_' + name, () => {
		const v = activate(fixture()); v.host.vars[P + 'strength_band'] = constants['gods_of_africa_band.extreme'];
		const before = snapshotPublic(v), emitCalls = callCount(v, 'emit_global_credibility_super_event'); change(v); refresh(v);
		assert.equal(snapshotPublic(v), before); assert.equal(callCount(v, 'emit_global_credibility_super_event'), emitCalls);
		assert(v.host.flags.has(F + 'input_publication_blocked')); assert(!v.globalFlags.has(P + 'global_credibility_super_event_emitted'));
	});
	test('successful_refresh_clears_block_and_host_row_corrects_without_foreign_resample', () => {
		const v = fixture(); refresh(v); v.host.flags.add(F + 'input_publication_blocked');
		v.host.armyK = 1000; v.actor.armyK = 99999; const reads = v.armyReads.length, samples = callCount(v, 'measure_strength_armies');
		v.host.flags.add(F + 'immediate'); refresh(v, decorate(C(90))); assertPublished(v, 57.3157);
		assert.equal(callCount(v, 'measure_strength_armies'), samples); assert(v.armyReads.slice(reads).every(r => r.id === v.host.id));
		assert.equal(v.host.vars[F + 'world_army_k'], 20000); assert.equal(v.host.vars[F + 'host_army_k_sample'], 2000);
		// Corrected denominator 19000, not 21000 or the unobserved foreign 99999.
		arithmetic.push({scenario: 'host row correction', correctedWorldK: 19000, military: 35.2628, published: 57.3157});
		assert.equal(v.componentFrames.at(-1).military, 35.2628);
	});
	for (const [name, mutate, expected, component, value] of [
		['readiness_absent', v => { delete v.host.vars.africa_continental_war_readiness; }, 53.5, 'military', 20],
		['industry_capacity', v => { v.host.getters.num_of_civilian_factories = 0; v.host.getters.num_of_military_factories = 0; }, 52.5, 'industry', 40],
		['technology_absent', v => { v.host.techs.clear(); }, 54, 'reach', 20],
		['political_authority', v => { v.host.vars.africa_cooperative_relationship_count = 0; v.host.vars.africa_charter_authority = 0; }, 52.5, 'continent', 40],
		['Chaos_zero', v => { v.global.vars.chaos_meter_value = 0; }, 53.5, 'chaos', 0],
		['Chaos_endpoint', v => { v.global.vars.chaos_meter_value = 1000; }, 63.5, 'chaos', 100],
		['zero_divisions', v => { v.host.divisions = 0; }, 48.5, 'military', 0],
		['zero_deployed_host', v => { v.host.armyK = 0; }, 48.5, 'military', 0]
	]) test('preserved_component_causal_' + name, () => {
		const v = fixture(); mutate(v); refresh(v); assertPublished(v, expected); assert.equal(v.componentFrames.at(-1)[component], value);
	});
	test('actual_recognition_major_loop_changes_political_component_only', () => {
		const v = fixture(); v.actor.major = true; v.actor.flags.add(P + 'recognition_granted'); v.host.arrays[P + 'participants'] = [v.actor];
		refresh(v); assertPublished(v, 59); assert.equal(v.host.vars[P + 'recognising_major_count'], 1); assert.equal(v.componentFrames.at(-1).continent, 72.5);
	});
	test('valid_high_inputs_publish_then_actual_super_event_guard_dispatches_once', () => {
		const v = new IntegrationVM(); v.host.armyK = 5000; v.actor.armyK = 15000; v.host.divisions = 2000;
		Object.assign(v.host.vars, {africa_continental_war_readiness: 100, africa_central_capacity: 100, africa_charter_authority: 100, africa_cooperative_relationship_count: 100, africa_continental_reach: 140});
		Object.assign(v.host.getters, {num_of_civilian_factories: 50, num_of_military_factories: 0, stability: 1}); v.global.vars.chaos_meter_value = 1000;
		for (const s of v.worldStates) { s.owner = v.host; s.controller = v.host; s.core = v.host; }
		sample(v); activate(v); assertPublished(v, 100); assert(v.globalFlags.has(P + 'global_credibility_super_event_emitted'));
		assert.deepEqual(v.componentFrames.at(-1), {military: 100, industry: 100, continent: 100, reach: 100, internal: 100, chaos: 100});
		assert.equal(v.boundaryCalls.filter(n => n === 'africa_world_emit_super_event').length, 1); refresh(v);
		assert.equal(v.boundaryCalls.filter(n => n === 'africa_world_emit_super_event').length, 1);
	});
	for (const [name, equip, fuel, expected, factor] of [['floor', 0, 0, 52.5, 0.4], ['equipment_only', 100, 0, 56.1, 0.76], ['fuel_only', 0, 100, 54.9, 0.64]]) test('sustainment_' + name + '_causal_weighted_result', () => {
		const v = fixture(); v.host.getters['num_equipment_in_armies_k@infantry_equipment'] = equip; v.host.getters.fuel_k = fuel;
		refresh(v); assertPublished(v, expected); assert.equal(v.host.vars[F + 'sustain_factor'], factor);
	});
	test('ordinary_movement_smooths_then_observes_committed_value', () => {
		const v = fixture(); v.host.vars[P + 'strength'] = 20; refresh(v); assertPublished(v, 28);
		refresh(v); assertPublished(v, 36); assert(v.host.flags.has(F + 'trend_rising'));
		v.host.vars[P + 'strength'] = 90; refresh(v); assertPublished(v, 82); assert(v.host.flags.has(F + 'trend_rising'));
		refresh(v); assertPublished(v, 74); assert(v.host.flags.has(F + 'trend_falling'));
	});
	test('real_capital_capture_is_immediate_then_ordinary_and_recapture_rearms_loss', () => {
		const v = fixture(); refresh(v); v.host.capital.controller = v.actor; refresh(v, decorate(C(90)));
		assertPublished(v, 42.5); assert(v.host.flags.has(F + 'capital_lost'));
		v.host.getters.stability = 1; refresh(v); assertPublished(v, 44.5);
		v.host.capital.controller = v.host; refresh(v); assertPublished(v, 52.5); assert(!v.host.flags.has(F + 'capital_loss_recorded'));
		v.host.capital.controller = v.actor; refresh(v); assertPublished(v, 44.5);
	});
	for (const [surrender, expected] of [[0.1, 58.5], [0.10001, 53.5], [0.25, 53.5], [0.25001, 46.5], [0.35, 46.5], [0.35001, 41.5], [0.4, 41.5], [0.40001, 33.5]]) test('surrender_penalty_boundary_' + surrender, () => {
		const v = fixture(); v.host.getters.surrender_progress = surrender; refresh(v); assertPublished(v, expected);
	});
	test('heavy_surrender_bypasses_smoothing_but_light_surrender_obeys_it', () => {
		const v = fixture(); v.host.vars[P + 'strength'] = 90; v.host.getters.surrender_progress = 0.2; refresh(v); assertPublished(v, 82);
		v.host.getters.surrender_progress = 0.3; refresh(v); assertPublished(v, 46.5);
	});
	for (const [label, flags, expected] of [['none', [], 58.5], ['II', ['africa_evolution_ii_logged'], 60], ['II_III', ['africa_evolution_ii_logged', 'africa_evolution_iii_logged'], 62.5]]) test('Chaos_1000_endpoint_and_evolution_' + label, () => {
		const v = fixture(); flags.forEach(f => v.globalFlags.add(f)); refresh(v); assertPublished(v, expected);
	});
	test('host_member_owned_control_core_and_capture_statistics_drive_full_refresh', () => {
		const v = fixture(); Object.assign(v.actor.vars, {africa_member_host_generation: 1, africa_relationship_state: constants['africa_relationship.chartered']});
		v.host.arrays.africa_relationship_countries = [v.actor]; v.worldStates[8].core = v.host;
		refresh(v); assertPublished(v, 59.5); assert.equal(v.host.vars[F + 'member_states'], 2); assert.equal(v.host.vars[F + 'member_core_states'], 1);
		const invader = decorate(C(90)); v.worldStates[8].controller = invader; v.host.flags.add(F + 'immediate'); refresh(v, invader);
		assertPublished(v, 58.5); assert.equal(v.host.vars[F + 'member_states'], 1); assert.equal(v.host.vars[F + 'member_core_states'], 0);
		assert.equal(v.host.vars[F + 'african_core_total'], 9); assert.equal(v.host.vars[F + 'african_secured_cores'], 8);
	});
	test('actual_activation_and_due_owner_only_sample_on_existing_clock', () => {
		const v = new IntegrationVM(); executeRetained(v, worldCensus, v.ctx(v.host)); activate(v); assertPublished(v, 58.5);
		assert.equal(callCount(v, 'measure_strength_armies'), 1); assert.equal(v.host.vars[F + 'army_sample_day'], 100);
		// Existing activation makes the first owner tick due immediately.
		invoke(v, 'run_owner_tick'); assert.equal(callCount(v, 'measure_strength_armies'), 2); assert.equal(v.host.vars[P + 'next_owner_tick_day'], 130);
		v.actor.armyK = 48000; v.day = 129; invoke(v, 'run_owner_tick'); assert.equal(callCount(v, 'measure_strength_armies'), 2); assertPublished(v, 58.5);
		v.day = 130; invoke(v, 'run_owner_tick'); assert.equal(callCount(v, 'measure_strength_armies'), 3); assert.equal(v.host.vars[F + 'world_army_k'], 50000); assertPublished(v, 57);
		invoke(v, 'run_owner_tick'); assert.equal(callCount(v, 'measure_strength_armies'), 3); assert.equal(v.host.vars[P + 'next_owner_tick_day'], 160);
	});
	test('named_registration_after_cardinality_change_repairs_census_at_owner_boundary', () => {
		const v = activate(fixture()), c = decorate(addCountry(v, C(9, 300))), d = decorate(addCountry(v, C(10, 200, false))); c.special = true;
		v.host.flags.add(P + 'final_settlement_committed'); invoke(v, 'try_register_participant', c, decorate(C(90)));
		assert(v.host.arrays[F + 'countries'].includes(c)); assert(!v.host.arrays[P + 'candidate_registry'].includes(c));
		assert(!v.host.flags.has(F + 'census_complete')); invoke(v, 'try_register_participant', d);
		assert.equal(v.host.arrays[F + 'countries'].length, 4); assert(!v.host.flags.has(F + 'census_complete'));
		invoke(v, 'try_register_participant', c); assert.equal(v.host.arrays[F + 'countries'].filter(x => x === c).length, 1);
		v.host.flags.delete(P + 'final_settlement_committed'); invoke(v, 'run_owner_tick');
		assert.equal(v.host.vars[F + 'world_army_k'], 20300); assert.equal(v.host.vars[F + 'census_size'], 4);
		assert(v.host.flags.has(F + 'census_complete')); assert(!v.host.flags.has(F + 'input_publication_blocked'));
	});
	test('real_transfer_staging_restore_new_owner_tuple_invalidates_cache_without_mandate', () => {
		const v = fixture(), old = v.host, next = v.actor; refresh(v);
		old.flags.add('africa_scramble_state_machine_initialised');
		executeRetained(v, stageScalars, v.ctx(old)); executeRetained(v, stageArrays, v.ctx(old));
		assert.deepEqual(v.global.arrays.africa_host_transfer_strength_countries, v.worldCountries); assert.equal(v.global.vars.africa_host_transfer_strength_census_size, 2);
		v.globalFlags.add('africa_host_transfer_scramble_state_machine_initialised');
		// Trusted surrounding transfer transaction owns target and generation changes.
		v.targets.africa_host = next; v.targets.africa_host_transfer_new_host = next;
		Object.assign(next.vars, {africa_host_generation: 2, africa_origin_host_id: 1}); next.flags.add('africa_unifier_host'); next.flags.add('africa_host_commit_completed');
		Object.assign(next.vars, {[F + 'world_army_k']: 999, [F + 'army_sample_generation']: 1}); next.flags.add(F + 'army_sample_valid'); next.flags.add(F + 'input_publication_blocked');
		invoke(v, 'africa_host_transfer_restore_world_order_state', next, old);
		assert.deepEqual(next.arrays[F + 'countries'], v.worldCountries); assert.equal(next.arrays[F + 'countries'].filter(x => x === next).length, 1);
		assert.deepEqual(['host_id', 'generation', 'origin_host_id'].map(k => next.vars[F + 'census_' + k]), [2, 2, 1]);
		assert.equal(next.vars[F + 'world_army_k'], undefined); assert(!next.flags.has(F + 'army_sample_valid'));
		// Restore discards measurement evidence. Its block receipt lasts until a
		// successful publication or the cleanup/revoke owner, as specified.
		assert(next.flags.has(F + 'input_publication_blocked'));
		assert(!next.flags.has(P + 'epoch_authorized')); assert.equal(next.vars[P + 'authority_epoch'], undefined);
		invoke(v, 'finish_strength_census', next); invoke(v, 'remember_strength_country', next); invoke(v, 'measure_strength_armies', next);
		assert.equal(next.vars[F + 'world_army_k'], 20000); assert.equal(next.vars[F + 'host_army_k_sample'], 18000); assert.equal(next.vars[F + 'army_sample_generation'], 2);
		assert.equal(next.arrays[F + 'countries'].length, 2); assert(!v.call(P + 'strength_host_is_current', v.ctx(old), true));
	});
	test('actual_loss_revoke_and_reentry_clear_samples_retain_census_and_observe_neutral', () => {
		const v = activate(fixture()), roster = [...v.host.arrays[F + 'countries']]; v.host.flags.add(F + 'input_publication_blocked'); v.host.capitulated = true;
		invoke(v, 'cancel_on_unifier_loss', v.host, decorate(C(90)));
		assert.deepEqual(v.host.arrays[F + 'countries'], roster); assert.equal(v.host.vars[F + 'world_army_k'], undefined); assert(!v.host.flags.has(F + 'input_publication_blocked'));
		assert.equal(strength(v), 0); assert(!v.host.flags.has(P + 'epoch_authorized')); assert.equal(v.host.vars[P + 'loss_sequence'], 1);
		invoke(v, 'cancel_on_unifier_loss'); assert.equal(v.host.vars[P + 'loss_sequence'], 1);
		// Authorized original-owner recovery is an external transaction, not a new grant here.
		v.host.capitulated = false; v.host.flags.delete(P + 'cancelled_on_unifier_loss'); v.host.flags.add(P + 'epoch_authorized'); v.host.vars[P + 'authority_epoch']++;
		delete v.host.vars[P + 'restoration_generation']; invoke(v, 'initialize_system');
		assert.equal(strength(v), 18); assert(!v.host.flags.has(F + 'trend_rising')); assert(!v.host.flags.has(F + 'trend_falling'));
		v.day = v.host.vars[P + 'consolidation_due_day']; activate(v); assertPublished(v, 58.5); assert.deepEqual(v.host.arrays[F + 'countries'], roster);
	});
	test('actual_clean_system_clears_samples_block_flag_and_public_values_retains_roster', () => {
		const v = activate(fixture()), roster = [...v.host.arrays[F + 'countries']]; v.host.flags.add(F + 'input_publication_blocked');
		invoke(v, 'clean_system', v.host, decorate(C(90)));
		assert.equal(v.host.vars[F + 'world_army_k'], undefined); assert(!v.host.flags.has(F + 'input_publication_blocked')); assert.deepEqual(v.host.arrays[F + 'countries'], roster);
		assert.equal(strength(v), 0); assert.equal(v.global.vars[P + 'strength_frame'], 1); assert(!v.host.flags.has(F + 'sample_known'));
	});
	for (const [name, mutate, expectedCalls, expected] of [
		['relevant_capture_foreign_ROOT', () => {}, 1, 57.5],
		['irrelevant_Europe', (v, site) => { site.continent = 'europe'; }, 0, 58.5],
		['no_active_Gods', v => { v.host.flags.delete(P + 'active'); }, 0, 58.5],
		['no_authorized_epoch', v => { v.host.flags.delete(P + 'epoch_authorized'); }, 0, 58.5],
		['irrelevant_foreign_noncore_Africa', (v, site) => { site.owner = v.actor; site.core = v.actor; }, 0, 58.5]
	]) test('actual_control_callback_' + name, () => {
		const v = new IntegrationVM(), next = decorate(addCountry(v, C(90))); sample(v); activate(v); const site = v.worldStates[1];
		let old = v.host; mutate(v, site); if (name === 'irrelevant_foreign_noncore_Africa') old = v.actor;
		site.controller = next; const calls = callCount(v, 'refresh_strength'), samples = callCount(v, 'measure_strength_armies'), reads = v.armyReads.length;
		callback(v, site, old, next); assert.equal(callCount(v, 'refresh_strength') - calls, expectedCalls); assertPublished(v, expected);
		assert.equal(callCount(v, 'measure_strength_armies'), samples); assert(v.armyReads.slice(reads).every(r => r.id === v.host.id)); assert.deepEqual(next.vars, {});
	});
	test('actual_control_callback_old_and_new_member_keep_core_capture_causal_without_resample', () => {
		const v = new IntegrationVM(), invader = decorate(addCountry(v, C(90))); sample(v); activate(v);
		Object.assign(v.actor.vars, {africa_member_host_generation: 1, africa_relationship_state: constants['africa_relationship.chartered']});
		v.host.arrays.africa_relationship_countries = [v.actor]; const site = v.worldStates[8]; site.core = v.host;
		v.host.flags.add(F + 'immediate'); refresh(v); assertPublished(v, 59.5);
		const samples = callCount(v, 'measure_strength_armies'), reads = v.armyReads.length;
		site.controller = invader; callback(v, site, v.actor, invader); assertPublished(v, 58.5); assert.equal(v.host.vars[F + 'member_core_states'], 0);
		site.controller = v.actor; callback(v, site, invader, v.actor); assertPublished(v, 59.5); assert.equal(v.host.vars[F + 'member_core_states'], 1);
		assert.equal(callCount(v, 'measure_strength_armies'), samples); assert(v.armyReads.slice(reads).every(r => r.id === v.host.id));
	});
	test('actual_control_callback_host_core_between_foreign_controllers_is_relevant', () => {
		const v = new IntegrationVM(), invader = decorate(addCountry(v, C(90))); sample(v); activate(v); const site = v.worldStates[1];
		site.controller = invader; refresh(v); assertPublished(v, 57.5);
		const calls = callCount(v, 'refresh_strength'); site.controller = v.actor; callback(v, site, invader, v.actor);
		assert.equal(callCount(v, 'refresh_strength'), calls + 1); assertPublished(v, 57.5); assert.equal(v.host.vars[F + 'african_core_total'], 8);
	});
	test('strict_unknown_native_getter_trigger_effect_and_typed_context_rejected', () => {
		const v = fixture(); assert.throws(() => v.value('undeclared_getter', v.ctx(v.host)), /Unknown getter/);
		assert.throws(() => v.exec(parse('undeclared_effect = yes'), v.ctx(v.host)), /Unsupported source effect/);
		assert.throws(() => v.test(parse('undeclared_trigger = yes'), v.ctx(v.host)), /Unsupported source trigger/);
		assert.throws(() => v.value('stability', v.ctx(v.worldStates[0])), /requires country/);
		delete v.host.getters.fuel_k; assert.throws(() => refresh(v), /Missing native getter/);
	});
	test('source_bytes_stable_during_bounded_run', () => { for (const [p, hash] of hashes) assert.equal(sha(fs.readFileSync(path.join(root, p))), hash, 'Source changed during replay: ' + p); });
	return {evidenceKind: 'SourceNoNativeProof', cases: cases.length, passed: cases.filter(c => c.passed).length, failures: cases.filter(c => !c.passed), results: cases, arithmetic,
		beforeSources, sourceHashes: [...hashes].map(([p, hash]) => ({path: p, sha256: hash})),
		executedProductionHelpers: [...executed].sort(), actualCallerSubtrees: subtrees,
		effectBoundaries: [...effectBoundaries], triggerBoundaries: Object.keys(triggerBoundaries),
		limits: ['5 decimal truncation, no native range or rounding proof', 'typed allocated-country/state/getter/technology/global-flag/ROOT/FROM.FROM fixtures are external inputs', 'only named census and scalar/array transfer subtrees execute, surrounding World routes and transfer commit are outside scope', 'no probability MCP or AI audit', 'native clocks and super-event audiovisual dispatch are boundaries', 'New Strength remains incomplete: capital anchors, port, rail, resource and base families queued']};
}
module.exports = { IntegrationVM, runSuite, worldCensus, stageScalars, stageArrays, decorate, invoke, sample, executeRetained, assertPrivateReset, withoutPrivateForeachState, fixture, activate, assertPublished, snapshotPublic, callCount };
if (require.main === module) {
	const report = runSuite(); fs.mkdirSync(evidenceDir, {recursive: true});
	fs.writeFileSync(path.join(evidenceDir, 'integration_results.json'), JSON.stringify(report, null, 2) + '\n');
	console.log(JSON.stringify({cases: report.cases, passed: report.passed, failures: report.failures, sourceHashes: report.sourceHashes, evidence: path.relative(root, path.join(evidenceDir, 'integration_results.json'))}, null, 2));
	process.exitCode = report.failures.length ? 1 : 0;
}
