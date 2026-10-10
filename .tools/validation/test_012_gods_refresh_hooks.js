/* Bounded actual-source Event 012 transaction refresh regression.
 * Run from mod root: node .tools/validation/test_012_gods_refresh_hooks.js
 * Optional argv[2]: directory containing the five raw before-source basenames.
 * Imports are silent and write-free. CLI receipts use .tmp/012_gods_refresh_hooks.
 * SourceNoNativeProof: typed country/state/getter fixtures, conservative helper
 * frame cleanup and five-decimal arithmetic, without native callback execution.
 * No Strength helper, authorization helper, measurement or publisher is mocked.
 * Exact relationship authorization and selected success nodes execute. Unrelated
 * transaction consumers are an explicit boundary, never synthesized outputs.
 */
'use strict';
const fs = require('node:fs'), path = require('node:path'), crypto = require('node:crypto');
const assert = require('node:assert/strict');
const {spawnSync} = require('node:child_process');
const {parse, effects, triggers, constants, namedBlock, C, addCountry, P, F} = require('./test_012_gods_strength_inputs.js');
const {IntegrationVM, runSuite: integrationSuite, decorate, invoke, sample, executeRetained,
	assertPublished, snapshotPublic, callCount} = require('./test_012_gods_strength_integration.js');
const root = path.resolve(__dirname, '../..'), scratch = path.join(root, '.tmp/012_gods_refresh_hooks');
const main = 'common/scripted_effects/012_africa_gods_effects.txt';
const inputs = 'common/scripted_effects/012_africa_gods_strength_inputs_effects.txt';
const evolution = 'common/scripted_effects/012_africa_evolution_effects.txt';
const relations = 'common/scripted_effects/012_africa_effects.txt';
const callbacks = 'common/on_actions/012_africa_gods_on_actions.txt';
const active = P + 'refresh_active_strength';
const doctrines = ['reciprocal_covenant', 'sovereign_exaction', 'strategic_ambiguity'];
const evolutions = ['i', 'ii', 'iii'];
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const walk = ns => ns.flatMap(n => [n, ...(Array.isArray(n.value) ? walk(n.value) : [])]);
const field = (ns, key) => { const n = ns.find(x => x.key === key); assert(n, 'Missing source field ' + key); return n.value; };
// Whole-file comparison preserves bare resource/equipment atoms as well as
// assignment nodes. The execution VM still uses its original strict parser.
function auditParse(source) {
	const ts = (source.match(/"(?:\\.|[^"\\])*"|#[^\r\n]*|[{}=<>]|[^\s{}=<>#]+/g) || []).filter(t => !t.startsWith('#'));
	let at = 0;
	function block(nested) {
		const out = [];
		while (at < ts.length && ts[at] !== '}') {
			const key = ts[at++];
			if (!['=', '<', '>'].includes(ts[at])) { out.push({atom: key}); continue; }
			const op = ts[at++]; let value = ts[at++];
			if (value === '{') value = block(true);
			out.push({key, op, value});
		}
		if (nested) assert.equal(ts[at++], '}');
		return out;
	}
	const result = block(false); assert.equal(at, ts.length); return result;
}
function runSuite(baselineDir = scratch) {
	const results = [], evidence = {units: {deployed_army_manpower_k: 'thousands of men', strength: '0..100', day: 'native days'},
		actualBindingReader: 'namedBlock/parse from the existing inputs suite, full source bodies installed by exact identifier'};
	const hashes = new Map(), bodies = new Map(), localVariables = new Set(), localArrays = new Set(), instances = [];
	const saved = {effects: {...effects}, triggers: {...triggers}, constants: {...constants}};
	const read = p => { const absolute = path.isAbsolute(p) ? p : path.join(root, p), bytes = fs.readFileSync(absolute); hashes.set(absolute, sha(bytes)); return bytes.toString('utf8'); };
	const test = (name, fn) => { try { fn(); results.push({name, passed: true}); } catch (e) { results.push({name, passed: false, error: e.message.slice(0, 1600), stack: e.stack.split('\n').slice(0, 5)}); } };
	function install(p, names, store = effects) {
		const source = read(p);
		for (const name of names) { const body = namedBlock(source, name); store[name] = body; bodies.set(name, {path: p, body}); }
	}
	const namedBoundaries = new Set(['record_events_log_evolution_entry', 'africa_refresh_continental_focus_tree_layout', 'africa_achievement_refresh_survival_windows']);
	class HooksVM extends IntegrationVM {
		constructor() { super(); this.hookCalls = []; this.nativeEvents = []; this.nativeBoundaries = []; instances.push(this); }
		value(token, c) {
			if (typeof token === 'string' && token.includes('^') && !token.includes('.')) {
				const [key, index] = token.split('^');
				if (localArrays.has(key)) { const a = c.scope.arrays[key] || []; return index === 'num' ? a.length : a[this.value(index, c)]; }
			}
			if (localArrays.has(token)) return c.scope.arrays[token] || [];
			if (localVariables.has(token) && !Object.hasOwn(this.temp, token)) return c.scope.vars[token] ?? 0;
			return super.value(token, c);
		}
		call(name, c, trigger = false) { this.hookCalls.push({name, trigger, scope: c.scope.id, root: c.root?.id, from: c.from?.id}); return super.call(name, c, trigger); }
		test(ns, c, mode = 'AND') {
			return super.test(ns.map(n => {
				let answer;
				if (['any_core_state', 'any_controlled_state'].includes(n.key)) {
					assert.equal(c.scope.type, 'country');
					answer = this.worldStates.filter(s => n.key === 'any_core_state' ? s.core === c.scope : s.controller === c.scope).some(s => this.test(n.value, this.ctx(s, c, c.root)));
				}
				return answer === undefined ? n : {key: answer ? 'AND' : 'NOT', value: []};
			}), c, mode);
		}
		exec(ns, c) {
			for (let i = 0; i < ns.length; i++) {
				const n = ns[i];
				if (namedBoundaries.has(n.key)) { this.nativeBoundaries.push({name: n.key, scope: c.scope.id, root: c.root?.id}); continue; }
				if (n.key === 'country_event') { this.nativeEvents.push({id: field(n.value, 'id'), scope: c.scope.id, days: n.value.some(x => x.key === 'days') ? this.value(field(n.value, 'days'), c) : 0}); continue; }
				if (n.key === 'remove_from_array') {
					const key = field(n.value, 'array'), value = this.value(field(n.value, 'value'), c);
					assert(localArrays.has(key), 'Unknown removal array ' + key);
					c.scope.arrays[key] = (c.scope.arrays[key] || []).filter(o => o !== value); continue;
				}
				let end = i + 1;
				if (n.key === 'if') while (end < ns.length && ['else_if', 'else'].includes(ns[end].key)) end++;
				super.exec(ns.slice(i, end), c); i = end - 1;
			}
		}
	}
	const counts = v => ({refresh: callCount(v, 'refresh_strength'), publish: callCount(v, 'observe_public_strength'),
		globalCommits: v.writes.filter(w => w.scope === 'global' && w.key === 'global.' + P + 'strength' && w.operation === 'set_variable').length,
		samples: callCount(v, 'measure_strength_armies'), discovery: callCount(v, 'remember_strength_country'),
		foreignReads: v.armyReads.filter(r => r.id !== v.host.id).length});
	function assertDelta(v, before, amount, label) {
		const after = counts(v);
		for (const key of ['refresh', 'publish', 'globalCommits']) assert.equal(after[key] - before[key], amount, label + ': ' + key);
		for (const key of ['samples', 'discovery', 'foreignReads']) assert.equal(after[key], before[key], label + ': no ' + key);
		return after;
	}
	function prepared(extraCountries = []) {
		const v = new HooksVM(); for (const c of extraCountries) addCountry(v, c);
		sample(v); invoke(v, 'activate_system'); assertPublished(v, 58.5);
		// A foreign ROOT is an existing typed object in the sampled census.
		v.actor.vars.foreign_root_marker = 41;
		return v;
	}
	function snapshot(c) { return JSON.stringify({vars: c.vars, flags: [...c.flags].sort(), arrays: Object.fromEntries(Object.entries(c.arrays).map(([k, a]) => [k, a.map(o => o.id ?? o)])), pp: c.pp}, (k, v) => v && ['country', 'state'].includes(v.type) ? {type: v.type, id: v.id} : v); }
	function call(v, name, scope = v.host, rootScope = scope) { v.call(name, v.ctx(scope, null, rootScope)); }
	function callback(v, name, scope, rootScope, from = null) { const c = v.ctx(scope, null, rootScope); c.from = from; executeRetained(v, field(field(field(parse(read(callbacks)), 'on_actions'), name), 'effect'), c); }
	function coherent(v) { call(v, 'africa_reconcile_relationship_counts_and_caps'); call(v, active); assertPublished(v, 55.5); return v; }
	try {
		for (const p of ['.tools/validation/test_012_gods_refresh_hooks.js', '.tools/validation/test_012_gods_strength_integration.js', '.tools/validation/test_012_gods_strength_inputs.js', '.tools/validation/test_012_gods_industry_helpers.js', inputs, main, evolution, relations, callbacks,
			'common/scripted_effects/012_africa_gods_public_values_effects.txt', 'common/scripted_triggers/012_africa_gods_strength_inputs_triggers.txt', 'common/scripted_triggers/012_africa_gods_recovery_triggers.txt']) read(p);
		install(inputs, [active]);
		install(main, doctrines.map(n => P + 'choose_' + n).concat('africa_gods_of_africa_begin_consolidation'));
		install(evolution, evolutions.map(n => 'africa_activate_evolution_' + n));
		install(relations, ['africa_clamp_host_values', 'africa_reconcile_relationship_counts_and_caps', 'africa_unregister_current_relationship_state', 'africa_register_current_relationship_state']);
		install('common/scripted_effects/012_africa_gods_recovery_effects.txt', [P + 'authorize_initial_epoch']);
		install('common/scripted_effects/012_africa_gods_contribution_effects.txt', [P + 'bind_contribution_campaign']);
		install('common/scripted_triggers/012_africa_triggers.txt', ['africa_is_valid_relationship_target', 'africa_member_can_begin_integration', 'africa_member_can_enter_autonomous_federal'].concat(
			parse(read('common/scripted_triggers/012_africa_triggers.txt')).filter(n => n.key.startsWith('africa_relationship_is_')).map(n => n.key)), triggers);
		for (const p of ['common/script_constants/012_africa_evolution_constants.txt', 'common/script_constants/012_africa_action_constants.txt', 'common/script_constants/012_africa_constants.txt', 'common/script_constants/012_africa_gods_constants.txt', 'common/script_constants/012_africa_gods_strength_inputs_constants.txt', 'common/script_constants/chaos_meter_constants.txt']) {
			// The shared Chaos constants have native bare lists. Already loaded by
			// IntegrationVM's leaf reader, so hash rather than broad-parse them.
			if (p.includes('chaos_meter')) { read(p); continue; }
			for (const cat of parse(read(p))) for (const n of cat.value) if (typeof n.value === 'string' && Number.isFinite(Number(n.value))) constants[cat.key + '.' + n.key] = Number(n.value);
		}
		const fullTransition = namedBlock(read(relations), 'africa_apply_relationship_transition');
		const success = fullTransition.find(n => n.key === 'if' && walk(n.value).some(x => x.key === active)); assert(success);
		const selected = new Set(['limit', 'africa_unregister_current_relationship_state', 'set_variable', 'africa_register_current_relationship_state', 'set_country_flag', 'set_temp_variable', 'event_target:africa_host']);
		const successNodes = success.value.filter(n => selected.has(n.key));
		// Keep only the direct host recount and exact new refresh scope node.
		const retainedSuccess = successNodes.filter(n => n.key !== 'event_target:africa_host' || n.value.some(x => x.key === 'africa_reconcile_relationship_counts_and_caps' || x.key === active));
		assert.equal(retainedSuccess.filter(n => n.key === 'set_variable').length, 2, 'actual state and generation mutations');
		assert.deepEqual(retainedSuccess.at(-2), parse('set_temp_variable = { africa_relationship_transition_result = constant:africa_value.one }')[0]);
		assert.deepEqual(retainedSuccess.at(-1), parse('event_target:africa_host = { ' + active + ' = yes }')[0]);
		const transitionBody = fullTransition.map(n => n === success ? {...n, value: retainedSuccess} : n);
		effects.africa_apply_relationship_transition = transitionBody;
		bodies.set('africa_apply_relationship_transition', {path: relations, body: transitionBody});
		evidence.relationshipBoundary = {fullBodyHash: sha(JSON.stringify(fullTransition)), selectedBodyHash: sha(JSON.stringify(transitionBody)),
			retainedSuccessKeys: retainedSuccess.map(n => n.key), omittedSuccessNodes: success.value.filter(n => !retainedSuccess.includes(n)).map(n => ({key: n.key, hash: sha(JSON.stringify(n))})),
			meaning: 'Actual leading authorization and exact selected successful subtree. No consequence, autonomy, patronage or achievement result is invented. Actual registry/count helpers supply the measured political/physical values.'};
		for (const {body} of bodies.values()) for (const n of walk(body)) {
			if (n.key === 'has_variable' || /^(clear|round)_variable$/.test(n.key)) localVariables.add(n.value.replace(/^global\./, ''));
			if (/_variable$/.test(n.key) && Array.isArray(n.value)) localVariables.add((n.value.find(x => x.key === 'var')?.value || n.value[0].key).replace(/^global\./, ''));
			if (n.key === 'array' || n.key === 'clear_array') localArrays.add(n.value.replace(/^global\./, ''));
		}
		test('exact_active_wrapper_executes_actual_ROOT_independent_guards_and_callee', () => {
			assert.deepEqual(effects[active], parse('if = { limit = { gods_of_africa_strength_host_is_current = yes gods_of_africa_epoch_permission_is_current = yes has_country_flag = gods_of_africa_active NOT = { has_country_flag = gods_of_africa_final_settlement_committed } } gods_of_africa_refresh_strength = yes }'));
			const v = prepared(), before = counts(v), foreign = snapshot(v.actor); call(v, active, v.host, v.actor);
			assertDelta(v, before, 1, 'authorized foreign ROOT'); assertPublished(v, 58.5); assert.equal(snapshot(v.actor), foreign);
			for (const n of ['strength_host_is_current', 'epoch_permission_is_current', 'authority_owner_object_is_current', 'authority_owner_has_physical_return', 'refresh_strength', 'measure_territorial_control', 'apply_strength_input_factors', 'observe_public_strength']) assert(v.hookCalls.some(c => c.name === P + n && c.root === v.actor.id), 'actual body ' + n);
		});
		const denied = [
			['no_active_Gods', v => v.host.flags.delete(P + 'active')],
			['unauthorized_epoch', v => v.host.flags.delete(P + 'epoch_authorized')],
			['zero_epoch', v => v.host.vars[P + 'authority_epoch'] = 0],
			['stale_epoch_generation', v => v.host.vars[P + 'authority_host_generation']++],
			['stale_epoch_origin', v => v.host.vars[P + 'authority_origin_host_id']++],
			['stale_epoch_host', v => v.host.vars[P + 'authority_host_id']++],
			['final_settlement', v => v.host.flags.add(P + 'final_settlement_committed')],
			['missing_target', v => delete v.targets.africa_host],
			['former_host', v => v.targets.africa_host = v.actor],
			['no_commit', v => v.host.flags.delete('africa_host_commit_completed')],
			['no_first_proof', v => v.host.firstProof = false],
			['capital_lost', v => v.host.capital.controller = v.actor],
			['host_capitulated', v => v.host.capitulated = true],
			['world_terminal', v => v.globalFlags.add('world_end')]
		];
		for (const [name, mutate] of denied) test('active_permission_denied_' + name, () => {
			const v = prepared(); mutate(v); const before = counts(v), publicBefore = snapshotPublic(v), foreign = snapshot(v.actor);
			call(v, active, v.host, v.actor); assertDelta(v, before, 0, name); assert.equal(snapshotPublic(v), publicBefore); assert.equal(snapshot(v.actor), foreign);
		});
		test('direct_foreign_country_cannot_enter_host_refresh', () => {
			const v = prepared(), before = counts(v), foreign = snapshot(v.actor), publicBefore = snapshotPublic(v);
			call(v, active, v.actor, v.host); assertDelta(v, before, 0, 'foreign THIS'); assert.equal(snapshot(v.actor), foreign); assert.equal(snapshotPublic(v), publicBefore);
		});
		test('active_hook_corrects_current_host_army_row_without_reading_changed_foreign_army', () => {
			const v = prepared(), before = counts(v); v.host.armyK = 1000; v.actor.armyK = 99999;
			call(v, active, v.host, v.actor); assertDelta(v, before, 1, 'cached correction'); assertPublished(v, 57.3157);
			assert.equal(v.componentFrames.at(-1).military, 35.2628); assert.equal(v.host.vars[F + 'world_army_k'], 20000); assert.equal(v.host.vars[F + 'host_army_k_sample'], 2000);
			evidence.currentArmyRowCorrection = {cachedWorldK: 20000, sampledHostK: 2000, currentHostK: 1000, correctedWorldK: 19000, unobservedForeignK: 99999, military: 35.2628, published: 57.3157, before, after: counts(v)};
		});
		test('authorized_active_hook_with_stale_sample_executes_real_refresh_without_publication', () => {
			const v = prepared(), before = counts(v), publicBefore = snapshotPublic(v); v.day += 31;
			call(v, active, v.host, v.actor); const after = counts(v);
			assert.equal(after.refresh, before.refresh + 1); assert.equal(after.publish, before.publish); assert.equal(after.globalCommits, before.globalCommits);
			for (const key of ['samples', 'discovery', 'foreignReads']) assert.equal(after[key], before[key]);
			assert.equal(snapshotPublic(v), publicBefore); assert(v.host.flags.has(F + 'input_publication_blocked'));
		});
		for (const doctrine of doctrines) {
			test('actual_doctrine_' + doctrine + '_refreshes_once_preserves_prices_and_guards', () => {
				const v = prepared(), before = counts(v), foreign = snapshot(v.actor);
				const prices = {gods_of_africa_demand_amount: 37.5, gods_of_africa_demand_remaining: 17.25, gods_of_africa_payment_amount: 9.25, gods_of_africa_demand_due_day: 233, gods_of_africa_partial_payment_amount: 7.125};
				Object.assign(v.host.vars, prices); const moneyWrites = v.moneyWrites.length, pp = v.host.pp;
				call(v, P + 'choose_' + doctrine); assert.equal(v.host.vars[P + 'doctrine'], constants['gods_of_africa_doctrine.' + doctrine]);
				assertDelta(v, before, 1, doctrine); assertPublished(v, 58.5);
				for (const [key, value] of Object.entries(prices)) assert.equal(v.host.vars[key], value, key);
				assert.equal(v.host.pp, pp); assert.equal(v.moneyWrites.length, moneyWrites); assert.equal(snapshot(v.actor), foreign);
			});
			for (const [label, mutate, foreignRoot] of [['foreign_ROOT_old_action_gate', () => {}, true], ['no_activation_commit', v => v.host.flags.delete(P + 'activation_committed'), false], ...denied.filter(([n]) => ['no_active_Gods', 'unauthorized_epoch', 'stale_epoch_generation', 'final_settlement'].includes(n)).map(([n, f]) => [n, f, false])]) test('actual_doctrine_' + doctrine + '_denies_' + label, () => {
				const v = prepared(); v.host.vars[P + 'doctrine'] = 91; mutate(v); const before = counts(v), publicBefore = snapshotPublic(v);
				call(v, P + 'choose_' + doctrine, v.host, foreignRoot ? v.actor : v.host);
				assert.equal(v.host.vars[P + 'doctrine'], 91); assertDelta(v, before, 0, doctrine + '/' + label); assert.equal(snapshotPublic(v), publicBefore);
			});
		}
		for (const stage of ['ii', 'iii']) for (const [sustain, equip, fuel, factor] of [['full', 100, 100, 1], ['equipment_only', 100, 0, 0.76], ['fuel_only', 0, 100, 0.64]]) test('actual_evolution_' + stage + '_' + sustain + '_components_amplifier_smoothing', () => {
			const v = coherent(prepared()); v.host.getters['num_equipment_in_armies_k@infantry_equipment'] = equip; v.host.getters.fuel_k = fuel;
			call(v, active); const before = counts(v), old = v.host.vars[P + 'strength'], foreign = snapshot(v.actor);
			call(v, 'africa_activate_evolution_' + stage, v.host, v.actor); assertDelta(v, before, 1, 'evolution ' + stage); assert.equal(snapshot(v.actor), foreign);
			const expectedComponents = {military: (stage === 'iii' ? 45 : 40) * factor, industry: stage === 'ii' ? 72.5 : 70,
				continent: stage === 'iii' ? 56.25 : 55, reach: stage === 'ii' ? 52.5 : 50, internal: 80, chaos: stage === 'ii' ? 65 : 75};
			assert.deepEqual(v.componentFrames.at(-1), expectedComponents);
			const expected = stage === 'ii' ? {full: 57.875, equipment_only: 55.475, fuel_only: 54.275}[sustain] : {full: 59.5, equipment_only: 56.8, fuel_only: 55.45}[sustain];
			assertPublished(v, expected); assert.equal(v.host.vars[F + 'sustain_factor'], factor); assert(v.globalFlags.has('africa_evolution_' + stage + '_logged'));
			if (stage === 'ii') { assert.equal(v.host.vars.africa_central_capacity, 85); assert.equal(v.host.vars.africa_continental_reach, 45); }
			else { assert.equal(v.host.vars.africa_continental_war_readiness, 70); assert.equal(v.host.vars.africa_charter_authority, 65); assert(v.host.flags.has(P + 'contribution_campaign_active')); }
			assert.equal(v.nativeEvents.at(-1).id, stage === 'ii' ? 'chaosx.nr12.402' : 'chaosx.nr12.403');
			const row = {stage, sustain, factor, old, components: expectedComponents, published: expected, before, after: counts(v)};
			(evidence.evolutionArithmetic ||= []).push(row);
		});
		test('evolution_II_then_III_adds_both_real_Chaos_amplifiers', () => {
			const v = coherent(prepared()); call(v, 'africa_activate_evolution_ii'); const before = counts(v); call(v, 'africa_activate_evolution_iii');
			assertDelta(v, before, 1, 'II then III'); assertPublished(v, 61.875); assert.equal(v.componentFrames.at(-1).chaos, 90);
		});
		for (const stage of ['ii', 'iii']) test('evolution_' + stage + '_ordinary_refresh_keeps_eight_point_smoothing', () => {
			const v = coherent(prepared()); v.host.vars[P + 'strength'] = 20; const before = counts(v); call(v, 'africa_activate_evolution_' + stage);
			assertDelta(v, before, 1, 'ordinary evolution'); assertPublished(v, 28); assert(!v.host.flags.has(F + 'immediate'));
		});
		test('evolution_I_starts_real_consolidation_and_new_refresh_does_not_publish_or_activate', () => {
			const v = sample(new HooksVM()); v.globalFlags.delete('africa_evolution_i_logged'); v.host.flags.delete(P + 'consolidation_pending');
			v.host.vars[P + 'strength'] = 18; v.global.vars[P + 'strength'] = 18;
			const before = counts(v); call(v, 'africa_activate_evolution_i');
			assertDelta(v, before, 0, 'Evolution I consolidation'); assert.equal(v.host.vars[P + 'strength'], 18); assert.equal(v.global.vars[P + 'strength'], 18);
			assert(v.host.flags.has(P + 'consolidation_pending')); assert(!v.host.flags.has(P + 'active')); assert(!v.host.flags.has(P + 'activation_committed'));
			assert.equal(v.host.vars[P + 'consolidation_due_day'], v.day + constants['gods_of_africa_timing.consolidation_days']);
			assert.deepEqual(v.nativeEvents.map(e => e.id), ['chaosx.nr12.401', 'chaosx.nr12.600']);
			assert(v.hookCalls.some(c => c.name === active)); assert.equal(v.host.vars.africa_charter_authority, 63); assert.equal(v.host.vars.africa_continental_reach, 45);
		});
		function transitionFixture() {
			const v = coherent(prepared()); v.worldStates[9].core = v.host;
			v.actor.vars.africa_relationship_state = constants['africa_relationship.outside']; v.actor.vars.africa_member_host_generation = 1;
			v.temp.africa_requested_relationship_state = constants['africa_relationship.associate']; v.temp.africa_relationship_transition_result = 77;
			return v;
		}
		test('actual_successful_relationship_subtree_mutates_member_recounts_and_refreshes_host', () => {
			const v = transitionFixture(), before = counts(v); call(v, 'africa_apply_relationship_transition', v.actor, v.actor);
			assertDelta(v, before, 1, 'member transition'); assert.equal(v.temp.africa_relationship_transition_result, 1);
			assert.equal(v.actor.vars.africa_relationship_state, constants['africa_relationship.associate']); assert.equal(v.actor.vars.africa_member_host_generation, 1);
			assert.deepEqual(v.host.arrays.africa_associate_countries, [v.actor]); assert.deepEqual(v.host.arrays.africa_relationship_countries, [v.actor]);
			assert.equal(v.host.vars.africa_cooperative_relationship_count, 1); assert.equal(v.host.vars[F + 'member_states'], 2); assert.equal(v.host.vars[F + 'member_core_states'], 1);
			assert.equal(v.host.vars[F + 'physical_control'], 90); assert.equal(v.componentFrames.at(-1).continent, 60.25);
			assert.equal(v.global.vars[P + 'strength'], 56.55); assert.equal(v.global.vars[P + 'strength_display'], 56);
			assert(v.hookCalls.some(c => c.name === active && c.scope === v.host.id && c.root === v.actor.id));
			evidence.memberTransition = {before, after: counts(v), cooperative: 1, memberStates: 2, memberCoreStates: 1, physical: 90, continent: 60.25, published: 56.55};
		});
		test('actual_relationship_exit_unregisters_member_before_hook_recomputes_both_components', () => {
			const v = transitionFixture(); call(v, 'africa_apply_relationship_transition', v.actor);
			v.temp.africa_requested_relationship_state = constants['africa_relationship.outside']; const before = counts(v);
			call(v, 'africa_apply_relationship_transition', v.actor); assertDelta(v, before, 1, 'member exit');
			assert.equal(v.temp.africa_relationship_transition_result, 1); assert.equal(v.host.vars.africa_cooperative_relationship_count, 0);
			assert.deepEqual(v.host.arrays.africa_associate_countries, []); assert.equal(v.host.vars[F + 'member_core_states'], 0);
			assert.equal(v.host.vars[F + 'physical_control'], 80); assert.equal(v.componentFrames.at(-1).continent, 55); assert.equal(v.global.vars[P + 'strength'], 55.5);
		});
		for (const [label, mutate] of [['stale_generation', v => v.actor.vars.africa_member_host_generation = 2], ['illegal_outside_to_chartered', v => v.temp.africa_requested_relationship_state = constants['africa_relationship.chartered']], ['capitulated_member', v => v.actor.capitulated = true], ['uncommitted_host', v => v.host.flags.delete('africa_host_commit_completed')]]) test('failed_relationship_' + label + '_no_new_hook_or_publication', () => {
			const v = transitionFixture(); mutate(v); const before = counts(v), publicBefore = snapshotPublic(v), actor = snapshot(v.actor);
			call(v, 'africa_apply_relationship_transition', v.actor); assertDelta(v, before, 0, label); assert.equal(v.temp.africa_relationship_transition_result, 0);
			assert.equal(snapshotPublic(v), publicBefore); assert.equal(snapshot(v.actor), actor); assert(!v.hookCalls.some(c => c.name === active && c.root === v.actor.id));
		});
		for (const direction of ['host_attacker_ROOT', 'host_defender_FROM', 'foreign_war']) test('native_war_relation_' + direction + '_actual_callback_body', () => {
			const v = prepared(direction === 'foreign_war' ? [decorate(C(3))] : []), before = counts(v), foreign = snapshot(v.actor); v.host.armyK = 1000; v.actor.armyK = 99999;
			const attacker = direction === 'host_attacker_ROOT' ? v.host : v.actor, defender = direction === 'host_defender_FROM' ? v.host : direction === 'foreign_war' ? v.worldCountries[2] : v.actor;
			assert.notEqual(attacker, defender, 'Two distinct native war countries'); const defenderBefore = snapshot(defender);
			callback(v, 'on_war_relation_added', attacker, attacker, defender);
			const amount = direction === 'foreign_war' ? 0 : 1; assertDelta(v, before, amount, direction); assertPublished(v, amount ? 57.3157 : 58.5); assert.equal(snapshot(v.actor), foreign);
			if (direction === 'foreign_war') assert.equal(snapshot(defender), defenderBefore);
			if (amount) assert(v.hookCalls.some(c => c.name === active && c.scope === v.host.id && c.root === attacker.id));
		});
		for (const label of ['host_THIS_foreign_ROOT', 'foreign_THIS_host_ROOT']) test('native_peace_' + label + '_safe_actual_callback_body', () => {
			const v = prepared(), before = counts(v), foreign = snapshot(v.actor); v.host.armyK = 1000; v.actor.armyK = 99999;
			const host = label.startsWith('host_THIS'); callback(v, 'on_peace', host ? v.host : v.actor, host ? v.actor : v.host);
			assertDelta(v, before, host ? 1 : 0, label); assertPublished(v, host ? 57.3157 : 58.5); assert.equal(snapshot(v.actor), foreign);
		});
		for (const [name, mutate] of denied.filter(([n]) => ['no_active_Gods', 'unauthorized_epoch', 'final_settlement'].includes(n))) for (const native of ['on_war_relation_added', 'on_peace']) test(native + '_permission_denied_' + name, () => {
			const v = prepared(); mutate(v); const before = counts(v), publicBefore = snapshotPublic(v);
			callback(v, native, v.host, native === 'on_peace' ? v.actor : v.host, v.actor); assertDelta(v, before, 0, name); assert.equal(snapshotPublic(v), publicBefore);
		});
		test('strict_unknown_effect_trigger_getter_and_missing_native_input_throw', () => {
			const v = prepared(); assert.throws(() => v.exec(parse('unknown_refresh_effect = yes'), v.ctx(v.host)), /Unsupported source effect/);
			assert.throws(() => v.test(parse('unknown_refresh_trigger = yes'), v.ctx(v.host)), /Unsupported source trigger/);
			assert.throws(() => v.value('unknown_refresh_getter', v.ctx(v.host)), /Unknown getter/);
			delete v.host.getters.fuel_k; assert.throws(() => call(v, active), /Missing native getter/);
		});
		test('whole_before_after_AST_projects_only_exact_new_hook_nodes', () => {
			const projection = [], hookNode = {key: active, op: '=', value: 'yes'};
			for (const p of [inputs, main, evolution, relations, callbacks]) {
				const baseline = path.join(baselineDir, path.basename(p)); assert(fs.existsSync(baseline), 'Raw before snapshot required: ' + baseline);
				const before = auditParse(read(baseline)), current = auditParse(read(p)); let removed = 0, projected = current;
				if (p === inputs) {
					assert.equal(current.filter(n => n.key === active).length, 1); assert(!before.some(n => n.key === active));
					projected = current.filter(n => n.key !== active); removed = 1;
				} else if (p === callbacks) {
					const oa = field(current, 'on_actions');
					for (const name of ['on_war_relation_added', 'on_peace']) { assert.equal(oa.filter(n => n.key === name).length, 1); assert(!field(before, 'on_actions').some(n => n.key === name)); }
					assert.deepEqual(field(field(oa, 'on_peace'), 'effect'), [hookNode]);
					assert.deepEqual(field(field(oa, 'on_war_relation_added'), 'effect'), parse('if = { limit = { has_event_target = africa_host OR = { ROOT = { tag = event_target:africa_host } FROM = { tag = event_target:africa_host } } } event_target:africa_host = { ' + active + ' = yes } }'));
					projected = current.map(n => n.key === 'on_actions' ? {...n, value: n.value.filter(x => !['on_war_relation_added', 'on_peace'].includes(x.key))} : n); removed = 2;
				} else {
					const owners = p === main ? doctrines.map(n => P + 'choose_' + n) : p === evolution ? evolutions.map(n => 'africa_activate_evolution_' + n) : ['africa_apply_relationship_transition'];
					projected = current.map(n => {
						if (!owners.includes(n.key)) return n;
						assert.equal(walk(n.value).filter(x => x.key === active).length, 1, n.key + ': exactly one hook');
						if (p === evolution) { assert.deepEqual(n.value.at(-1), hookNode); removed++; return {...n, value: n.value.slice(0, -1)}; }
						const branch = p === main ? field(n.value, 'if') : n.value.find(x => x.key === 'if' && walk(x.value).some(y => y.key === active)).value;
						const expected = p === main ? hookNode : parse('event_target:africa_host = { ' + active + ' = yes }')[0];
						assert.deepEqual(branch.at(-1), expected); removed++;
						return {...n, value: n.value.map(x => x.value === branch ? {...x, value: branch.slice(0, -1)} : x)};
					});
					assert.equal(removed, owners.length);
				}
				assert.deepEqual(projected, before, p + ': all non-hook AST, guards, prices and weights unchanged');
				projection.push({path: p, beforePath: baseline, removedExactNodes: removed, projectedHash: sha(JSON.stringify(projected)), beforeHash: sha(JSON.stringify(before))});
			}
			evidence.structuralProjection = projection;
		});
		test('original_integration_57_groups_remain_unchanged', () => {
			const r = integrationSuite(); assert.equal(r.cases, 57); assert.equal(r.passed, 57, JSON.stringify(r.failures));
			evidence.integrationPreserved = {cases: r.cases, passed: r.passed, evidenceKind: r.evidenceKind};
			// Retain all original dependency identities, including the real native
			// Africa collection, world census, observer, and complete guard files.
			for (const s of r.sourceHashes) read(s.path);
			const collection = 'C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/collections/collections.txt'; read(collection);
		});
		test('original_inputs_26_CLI_groups_remain_unchanged_and_integration_import_is_silent', () => {
			const run = spawnSync(process.execPath, ['.tools/validation/test_012_gods_strength_inputs.js'], {cwd: root, encoding: 'utf8'});
			assert.equal(run.status, 0, run.stderr); const r = JSON.parse(run.stdout); assert.equal(r.cases, 26);
			const imported = spawnSync(process.execPath, ['-e', "require('./.tools/validation/test_012_gods_strength_integration.js'); require('./.tools/validation/test_012_gods_refresh_hooks.js');"], {cwd: root, encoding: 'utf8'});
			assert.equal(imported.status, 0, imported.stderr); assert.equal(imported.stdout, ''); assert.equal(imported.stderr, '');
			evidence.inputsPreserved = {cases: r.cases, evidenceKind: r.evidenceKind};
		});
		test('all_bound_source_bytes_stay_stable_during_run', () => {
			for (const [p, hash] of hashes) assert.equal(sha(fs.readFileSync(p)), hash, 'Source changed during test: ' + p);
		});
	} finally {
		for (const [name, store] of Object.entries({effects, triggers, constants})) { for (const key of Object.keys(store)) delete store[key]; Object.assign(store, saved[name]); }
	}
	return {evidenceKind: 'SourceNoNativeProof', cases: results.length, passed: results.filter(r => r.passed).length,
		failures: results.filter(r => !r.passed), results, ...evidence,
		sourceHashes: [...hashes].map(([p, hash]) => ({path: path.relative(root, p).replace(/\\/g, '/'), sha256: hash})),
		actualBindings: [...bodies].map(([name, {path: p, body}]) => ({name, path: p, bodyHash: sha(JSON.stringify(body))})),
		executedProductionBodies: [...new Set(instances.flatMap(v => v.hookCalls.map(c => c.name)))].sort(),
		actualROOTBindings: ['ROOT attacker/FROM defender', 'peace country THIS with preserved foreign ROOT', 'member THIS with unchanged member ROOT and event_target host refresh'],
		nativeBoundaries: [...namedBoundaries],
		limits: ['Source replay only, no native HOI4 callback/getter/timing or numeric-range proof', 'Conservative caller-owned temporary lifetime and five-decimal truncation from existing VM', 'First-proof, classification, secured-continent and unrelated integration consumer predicates retain the existing declared fixtures', 'Relationship processor executes exact leading authorization and selected success subtree, with unrelated consumers omitted and hash-listed', 'No probability analysis, AI review, GUI rendering, production, Git, workbook or game edit', 'Historical structural comparison needs the raw before basenames supplied by the owner']};
}
module.exports = {runSuite};
if (require.main === module) {
	const report = runSuite(process.argv[2] ? path.resolve(process.argv[2]) : scratch);
	fs.mkdirSync(scratch, {recursive: true}); fs.writeFileSync(path.join(scratch, 'refresh_hooks_results.json'), JSON.stringify(report, null, 2) + '\n');
	console.log(JSON.stringify({evidenceKind: report.evidenceKind, cases: report.cases, passed: report.passed, failures: report.failures, evidence: '.tmp/012_gods_refresh_hooks/refresh_hooks_results.json'}, null, 2));
	process.exitCode = report.failures.length ? 1 : 0;
}
