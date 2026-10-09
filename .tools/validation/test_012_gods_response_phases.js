// Bounded Event 012 response-phase source model. Run with Node from the mod root.
// Evaluates production view/context helpers and decision blocks, never HOI4.
// Legacy gameplay predicates/effects and native mission dispatch are explicit
// boundaries. Unknown tokens fail closed by throwing, not by returning true.
// No files are written. AST comparison preserves prices, AI scores and clocks.
const fs = require('fs');
const assert = require('assert/strict');
const { parse, assignment, hash } = require('../../docs/plans/033_acid_rain_plans/validation/caller_repairs_source_tests_2026_10_03.js');
const P = 'gods_of_africa_';
const evidenceDir = 'docs/plans/012_africa_plans/subagent_handoffs/012_gods_decision_phases_2026-10-07_evidence/before/';
const manifest = JSON.parse(fs.readFileSync(evidenceDir + 'manifest.json', 'utf8'));
const sources = new Map(), ast = new Map(), constants = new Map(), triggers = new Map(), effects = new Map();
function load(path) {
	if (!sources.has(path)) { sources.set(path, fs.readFileSync(path)); ast.set(path, parse(sources.get(path).toString('utf8'))); }
	return ast.get(path);
}
const decisionPath = 'common/decisions/012_africa_gods_decisions.txt';
const triggerPath = 'common/scripted_triggers/012_africa_gods_triggers.txt';
const effectPath = 'common/scripted_effects/012_africa_gods_effects.txt';
const recoveryPath = 'common/scripted_effects/012_africa_gods_recovery_effects.txt';
const punishmentPath = 'common/scripted_effects/012_africa_gods_punishment_effects.txt';
const viewTriggerPath = 'common/scripted_triggers/012_africa_gods_response_view_triggers.txt';
const contextPath = 'common/scripted_triggers/012_africa_gods_response_context_triggers.txt';
const viewEffectPath = 'common/scripted_effects/012_africa_gods_response_view_effects.txt';
const statusPath = 'common/scripted_localisation/012_africa_gods_response_scripted_localisation.txt';
for (const file of ['012_africa_gods_constants.txt', '012_africa_gods_response_constants.txt', '012_africa_action_constants.txt', '012_africa_event_log_constants.txt']) {
	for (const category of load('common/script_constants/' + file))
		for (const entry of Array.isArray(category.value) ? category.value : [])
			if (!Array.isArray(entry.value) && Number.isFinite(Number(entry.value)))
				constants.set('constant:' + category.key + '.' + entry.key, Number(entry.value));
}
const block = (nodes, key) => { const matches = nodes.filter(n => n.key === key); assert.equal(matches.length, 1, 'unique block ' + key); return matches[0].value; };
const field = (nodes, key) => nodes.find(n => n.key === key)?.value;
const allNodes = nodes => nodes.flatMap(n => [n, ...(Array.isArray(n.value) ? allNodes(n.value) : [])]);
const chaosRanges = block(load('common/script_constants/chaos_meter_constants.txt'), 'chaos_meter_tier_range');
const chaosEndpoint = Number(field(block(chaosRanges, 'tier_final'), 'min'));
assert.ok(chaosEndpoint > 0);
constants.set('constant:chaos_meter_tier_range.tier_final.min', chaosEndpoint);
const suffixes = ['can_prepare_defensive_defiance', 'can_harden_stockpiles', 'can_secure_transport', 'can_prepare_countermeasures', 'participant_can_defy'];
for (const path of [viewTriggerPath, contextPath]) for (const n of load(path)) triggers.set(n.key, n.value);
for (const name of [...suffixes, 'participant_can_reconcile', 'substitute_offer_is_pending', 'reconciliation_can_be_paid', 'participant_can_offer_aid', 'participant_generation_is_current']) triggers.set(P + name, block(load(triggerPath), P + name));
triggers.set(P + 'council_response_phase_is_open', block(load('common/scripted_triggers/012_africa_gods_council_triggers.txt'), P + 'council_response_phase_is_open'));
triggers.set(P + 'final_ultimatum_is_open', block(load('common/scripted_triggers/012_africa_gods_punishment_triggers.txt'), P + 'final_ultimatum_is_open'));
triggers.set(P + 'victor_renewal_is_current', block(load('common/scripted_triggers/012_africa_gods_victor_triggers.txt'), P + 'victor_renewal_is_current'));
for (const n of load(viewEffectPath)) effects.set(n.key, n.value);
const preparations = ['prepare_defensive_defiance', 'harden_stockpiles', 'secure_transport', 'prepare_countermeasures'];
for (const name of preparations) effects.set(P + name, block(load(effectPath), P + name));
// Manually invoked handlers expose native dispatch as a recorded boundary.
// No scheduler, world simulation, punishment reconstruction or timer engine.
for (const name of ['start_reconciliation', 'seek_reconciliation', 'complete_reconciliation', 'fail_reconciliation']) effects.set(P + name, block(load(effectPath), P + name));
for (const name of ['issue_final_ultimatum', 'resolve_final_ultimatum', 'expire_final_ultimatum']) effects.set(P + name, block(load(punishmentPath), P + name));
effects.set(P + 'clear_reconciliation_epoch', block(load('common/scripted_effects/012_africa_gods_lifecycle_effects.txt'), P + 'clear_reconciliation_epoch'));
const decisions = new Map();
for (const category of load(decisionPath).filter(n => Array.isArray(n.value)))
	for (const row of category.value) decisions.set(row.key, row.value);
const beforeDecisions = new Map();
const historical = new Map();
for (const item of manifest) {
	const bytes = fs.readFileSync(item.before);
	assert.equal(hash(bytes), item.sha256, 'immutable baseline ' + item.before);
	historical.set(item.source, parse(bytes.toString('utf8'))); load(item.source);
}
for (const category of historical.get(decisionPath).filter(n => Array.isArray(n.value)))
	for (const row of category.value) beforeDecisions.set(row.key, row.value);
const results = [], failures = [], executed = new Set(), boundaryCalls = new Set();
function test(name, fn) {
	try { const details = fn(); results.push({ name, status: 'passed', ...(details ?? {}) }); }
	catch (error) { failures.push({ name, message: error.message }); }
}

// Explicitly supported legacy boundaries only. Values are fixture inputs, not
// recreated game logic. ROOT/THIS/FROM are real distinct fixture objects.
const legacyPredicates = new Set(`active_host_is_valid can_change_priority can_escalate_offense can_public_pardon coalition_target_is_valid continent_is_secured contribution_sender_is_current council_is_open council_material_is_accounted council_pledge_can_be_paid council_pledge_is_affordable council_pledge_retry_is_ready council_speech_can_replace_pledge council_speech_is_affordable current_demand_can_be_paid defiance_action_is_valid demand_contract_is_current demand_is_diplomatic demand_payment_is_open expedition_target_is_valid final_ultimatum_is_open frozen_territory_payment_is_possible host_can_arm_coalition host_can_coerce_occupier host_can_receive_demand_payment host_can_send_expedition instalments_can_be_signed occupier_coercion_target_is_valid partial_payment_is_affordable participant_aid_can_be_sent participant_can_offer_aid participant_can_offer_substitute participant_can_receive_protection participant_can_request_extension participant_generation_is_current participant_host_is_active participant_needs_reconciliation participant_holds_host_core_state participant_owns_host_core_state payment_retry_is_open priority_offender_capacity_available protection_package_is_affordable proven_offender reconciliation_can_be_paid reconciliation_epoch_is_current settlement_source_has_pending_delivery settlement_source_has_spare_stock substitute_offer_is_affordable substitute_transfer_is_clear ultimatum_has_land_or_war ultimatum_settlement_is_affordable victor_can_request_relegitimation victor_renewal_can_withdraw victor_renewal_is_current substitute_slot_1_is_valid substitute_slot_2_is_valid substitute_slot_3_is_valid substitute_slot_1_transfer_is_clear substitute_slot_2_transfer_is_clear substitute_slot_3_transfer_is_clear`.split(/\s+/).map(x => P + x));
const legacyEffects = new Set(['choose_reciprocal_covenant', 'choose_sovereign_exaction', 'choose_strategic_ambiguity', 'set_priority', 'grant_leniency', 'public_pardon', 'protect_partner', 'mark_offender', 'escalate_offense', 'arm_offender_enemies', 'send_expedition', 'coerce_occupier', 'commit_final_settlement'].map(x => P + x));
for (const name of ['bind_reconciliation_epoch', 'record_history', 'record_milestone', 'apply_wrath', 'record_accepted_reconciliation', 'resolve_accepted_grading_conduct', 'evaluate_punishment', 'request_victor_relegitimation']) legacyEffects.add(P + name);
legacyPredicates.add(P + 'contract_history_identity_is_current');
for (const name of ['participant_is_live', 'has_current_host', 'participant_epoch_is_current']) legacyPredicates.add(P + name);
for (const name of ['victor_relationship_is_available', 'victor_request_epoch_is_current']) legacyPredicates.add(P + name);
function fixture() {
	const country = label => ({ identity: Object.freeze({ opaqueCountryIdentity: label }), exists: true, ai: false, pp: 1000, equipment: 100000, fuel: 100000, vars: new Map(), flags: new Set(), arrays: new Map(), predicates: new Map(), wars: new Set() });
	const host = country('host'), participant = country('participant'), victor = country('non-member-victor'), other = country('unrelated-host');
	host.predicates.set(P + 'active_host_is_valid', true);
	for (const c of [participant, victor]) for (const key of ['participant_host_is_active', 'participant_generation_is_current', 'reconciliation_epoch_is_current', 'demand_contract_is_current']) c.predicates.set(P + key, true);
	for (const key of ['participant_is_live', 'has_current_host', 'participant_epoch_is_current']) participant.predicates.set(P + key, true);
	host.vars.set('africa_host_generation', 4); participant.vars.set(P + 'participant_generation', 4);
	host.vars.set('africa_origin_host_id', host.identity);
	participant.flags.add(P + 'participant');
	host.arrays.set(P + 'participants', [participant]); host.arrays.set(P + 'candidate_registry', [participant, victor]);
	host.vars.set(P + 'doctrine', constants.get('constant:' + P + 'doctrine.reciprocal_covenant'));
	const state = { day: 130, writes: [], targets: new Map([['africa_host', host]]), globals: new Map(), globalFlags: new Set() };
	function context(root = host, from = participant) { return { root, from, current: root, previous: null, temps: new Map() }; }
	function scoped(token, ctx) {
		if (token === 'ROOT') return ctx.root;
		if (token === 'FROM') { assert.ok(ctx.from, 'FROM outside decision context'); return ctx.from; }
		if (token === 'THIS') return ctx.current;
		if (token === 'PREV') { assert.ok(ctx.previous); return ctx.previous; }
		if (token.startsWith('event_target:')) { assert.ok(state.targets.has(token.slice(13))); return state.targets.get(token.slice(13)); }
		throw Error('unsupported scope ' + token);
	}
	function value(token, ctx) {
		if (constants.has(token)) return constants.get(token);
		assert.ok(!token.startsWith('constant:'), 'unresolved constant ' + token);
		if (Number.isFinite(Number(token))) return Number(token);
		if (token === 'global.num_days') return state.day;
		if (token === 'global.chaos_meter_value') return state.globals.get('chaos_meter_value') ?? 0;
		if (['ROOT', 'FROM', 'THIS', 'PREV'].includes(token)) return scoped(token, ctx);
		if (token.endsWith('.id')) return scoped(token.slice(0, -3), ctx).identity;
		if (token.startsWith('event_target:') && token.includes('.')) { const dot = token.indexOf('.'); return scoped(token.slice(0, dot), ctx).vars.get(token.slice(dot + 1)) ?? 0; }
		if (/^(ROOT|FROM|PREV|THIS)\./.test(token)) { const dot = token.indexOf('.'); return scoped(token.slice(0, dot), ctx).vars.get(token.slice(dot + 1)) ?? 0; }
		if (token.startsWith('var:')) token = token.slice(4);
		return ctx.temps.get(token) ?? ctx.current.vars.get(token) ?? 0;
	}
	function compare(a, b, op) {
		if (op === '=' || op === 'equals') return a === b;
		assert.equal(typeof a, 'number', 'opaque identity in arithmetic'); assert.equal(typeof b, 'number');
		if (op === '>' || op === 'greater_than') return a > b;
		if (op === '<' || op === 'less_than') return a < b;
		if (op === 'greater_than_or_equals') return a >= b;
		if (op === 'less_than_or_equals') return a <= b;
		throw Error('unsupported compare ' + op);
	}
	function trigger(n, ctx) {
		if (['AND', 'hidden_trigger', 'custom_trigger_tooltip'].includes(n.key)) return every(n.value.filter(x => x.key !== 'tooltip'), ctx);
		if (n.key === 'OR') return n.value.some(x => trigger(x, ctx));
		if (n.key === 'NOT') return !every(n.value, ctx);
		if (n.key === 'NOR') return !n.value.some(x => trigger(x, ctx));
		if (n.key === 'always') return n.value === 'yes';
		if (n.key === 'exists') return ctx.current.exists === (n.value === 'yes');
		if (n.key === 'is_ai') return ctx.current.ai === (n.value === 'yes');
		if (n.key === 'has_country_flag') return ctx.current.flags.has(n.value);
		if (n.key === 'has_global_flag') return state.globalFlags.has(n.value);
		if (n.key === 'has_variable') return ctx.current.vars.has(n.value);
		if (n.key === 'is_in_array') return (ctx.current.arrays.get(field(n.value, 'array')) ?? []).includes(value(field(n.value, 'value'), ctx));
		if (n.key === 'has_event_target') return state.targets.has(n.value);
		if (n.key === 'has_war_with') return ctx.current.wars.has(scoped(n.value, ctx).identity);
		if (n.key === 'tag') return ctx.current.identity === scoped(n.value, ctx).identity;
		if (n.key === 'has_political_power') return compare(ctx.current.pp, value(n.value, ctx), n.op);
		if (n.key === 'has_equipment') { assert.equal(n.value[0].key, 'infantry_equipment'); return compare(ctx.current.equipment, value(n.value[0].value, ctx), n.value[0].op); }
		if (n.key === 'has_fuel') return compare(ctx.current.fuel, value(n.value, ctx), n.op);
		if (n.key === 'check_variable') { const [left, right] = assignment(n); return compare(value(left, ctx), value(right, ctx), field(n.value, 'compare') ?? n.value[0].op); }
		if (['ROOT', 'FROM', 'THIS', 'PREV'].includes(n.key) || n.key.startsWith('event_target:')) return every(n.value, { ...ctx, previous: ctx.current, current: scoped(n.key, ctx) });
		if (n.key === 'any_of_scopes') {
			const array = ctx.current.arrays.get(field(n.value, 'array')) ?? [];
			return array.some(current => every(n.value.filter(x => x.key !== 'array'), { ...ctx, previous: ctx.current, current }));
		}
		if (triggers.has(n.key)) { executed.add(n.key); return every(triggers.get(n.key), ctx) === (n.value === 'yes'); }
		assert.ok(legacyPredicates.has(n.key), 'unmodeled trigger ' + n.key);
		boundaryCalls.add(n.key);
		return (ctx.current.predicates.get(n.key) ?? false) === (n.value === 'yes');
	}
	function every(nodes, ctx) { return nodes.every(n => trigger(n, ctx)); }
	function run(nodes, ctx) {
		for (let i = 0; i < nodes.length; i++) {
			const n = nodes[i];
			if (n.key === 'if') {
				let hit = every(field(n.value, 'limit'), ctx);
				if (hit) run(n.value.filter(x => x.key !== 'limit'), ctx);
				while (['else_if', 'else'].includes(nodes[i + 1]?.key)) {
					const branch = nodes[++i];
					if (!hit && (branch.key === 'else' || every(field(branch.value, 'limit'), ctx))) { run(branch.value.filter(x => x.key !== 'limit'), ctx); hit = true; }
				}
				continue;
			}
			if (n.key === 'hidden_effect') { run(n.value, ctx); continue; }
			if (n.key === 'custom_effect_tooltip') continue;
			if (['ROOT', 'FROM'].includes(n.key) || n.key.startsWith('event_target:')) { run(n.value, { ...ctx, previous: ctx.current, current: scoped(n.key, ctx) }); continue; }
			if (n.key === 'save_event_target_as') { state.targets.set(n.value, ctx.current); continue; }
			if (n.key === 'clear_variable') { ctx.current.vars.delete(n.value); continue; }
			if (['set_variable', 'set_temp_variable', 'multiply_temp_variable', 'divide_temp_variable', 'add_to_temp_variable', 'add_to_variable'].includes(n.key)) {
				const [key, token] = assignment(n), store = n.key.endsWith('_temp_variable') ? ctx.temps : ctx.current.vars, right = value(token, ctx);
				if (['multiply_temp_variable', 'divide_temp_variable'].includes(n.key)) { assert.equal(typeof right, 'number'); assert.equal(typeof store.get(key), 'number'); if (n.key === 'divide_temp_variable') assert.notEqual(right, 0); store.set(key, n.key === 'multiply_temp_variable' ? store.get(key) * right : store.get(key) / right); }
				else if (['add_to_variable', 'add_to_temp_variable'].includes(n.key)) { assert.equal(typeof right, 'number'); assert.equal(typeof (store.get(key) ?? 0), 'number'); store.set(key, (store.get(key) ?? 0) + right); }
				else store.set(key, right);
				continue;
			}
			if (n.key === 'clamp_temp_variable') { const key = field(n.value, 'var'), lo = value(field(n.value, 'min'), ctx), hi = value(field(n.value, 'max'), ctx); assert.ok(hi >= lo); ctx.temps.set(key, Math.max(Math.min(ctx.temps.get(key), hi), lo)); continue; }
			if (n.key === 'set_country_flag') { ctx.current.flags.add(n.value); continue; }
			if (n.key === 'clr_country_flag') { ctx.current.flags.delete(n.value); continue; }
			if (['activate_mission', 'remove_mission', 'country_event', 'add_opinion_modifier'].includes(n.key)) { state.writes.push({ nativeBoundary: n.key, payload: n.value, scope: ctx.current.identity }); continue; }
			if (n.key === 'add_political_power') { ctx.current.pp += value(n.value, ctx); state.writes.push({ effect: n.key, scope: ctx.current.identity }); continue; }
			if (['add_stability', 'add_war_support'].includes(n.key)) { state.writes.push({ effect: n.key, scope: ctx.current.identity }); continue; }
			if (effects.has(n.key)) { executed.add(n.key); run(effects.get(n.key), ctx); continue; }
			assert.ok(legacyEffects.has(n.key), 'unmodeled effect ' + n.key);
			state.writes.push({ effect: n.key, scope: ctx.current.identity });
		}
	}
	function testTrigger(name, root = host, from = participant) { return every([{ key: P + name, op: '=', value: 'yes' }], context(root, from)); }
	function visible(name, root = host, from = participant) {
		const row = decisions.get(P + name); assert.ok(row, name);
		const ctx = context(root, from);
		return every(field(row, 'visible') ?? [], ctx) && (!field(row, 'target_trigger') || every(field(row, 'target_trigger'), ctx));
	}
	function available(name, root = host, from = participant) { return every(field(decisions.get(P + name), 'available') ?? [], context(root, from)); }
	function click(name, root = host, from = participant) { run(field(decisions.get(P + name), 'complete_effect'), context(root, from)); }
	function helper(name, root = host) { run([{ key: P + name, op: '=', value: 'yes' }], context(root, null)); }
	return { host, participant, victor, other, state, context, every, run, testTrigger, visible, available, click, helper };
}
const doctrine = ['choose_reciprocal_covenant', 'choose_sovereign_exaction', 'choose_strategic_ambiguity'];
const priority = ['prioritize_land', 'prioritize_support', 'prioritize_fuel', 'prioritize_manpower', 'prioritize_industry', 'prioritize_transport', 'prioritize_air_defense', 'prioritize_emergency'];
const partners = ['grant_leniency', 'public_pardon', 'protect_partner', 'send_expedition'];
const judgment = ['mark_offender', 'escalate_offense', 'arm_offender_enemies', 'coerce_occupier'];
const navigation = ['open_priorities', 'open_partner_relations', 'open_judgments', 'return_to_overview'];
const answers = ['accept_substitute', 'reject_substitute', 'accept_reconciliation'];
const viewKey = P + 'response_view';
const view = name => constants.get('constant:' + P + 'response_view.' + name);
function allNeeds(f, lane = 'emergency') {
	for (const name of ['land_equipment', 'fuel', 'manpower', 'industry', 'transport', 'emergency', 'support_equipment', 'aircraft']) f.host.vars.set(P + 'need_' + name, 1);
	if (lane === 'support') f.host.flags.add(P + 'focus_arsenal_support_unlocked');
	if (lane === 'air_defense') f.host.flags.add(P + 'focus_logistics_support_unlocked');
	f.host.predicates.set(P + 'can_change_priority', true);
}
function targetContext(f) {
	for (const key of ['office_voices_complete', 'shelter_unlocked', 'expedition_unlocked', 'offense_memory_unlocked', 'sanctions_unlocked', 'occupier_coercion_unlocked']) f.host.flags.add(P + 'focus_' + key);
	for (const key of ['demand_active', 'offender']) f.participant.flags.add(P + key);
	for (const key of ['can_public_pardon', 'participant_can_receive_protection', 'expedition_target_is_valid', 'proven_offender', 'can_escalate_offense', 'coalition_target_is_valid', 'occupier_coercion_target_is_valid']) f.participant.predicates.set(P + key, true);
	f.host.predicates.set(P + 'priority_offender_capacity_available', true);
}
function offer(f, kind) {
	const p = kind === 'victor' ? f.victor : f.participant;
	if (kind === 'substitute') {
		for (const key of ['negotiation_open', 'substitute_offered']) p.flags.add(P + key);
		p.vars.set(P + 'substitute_family', 1); p.vars.set(P + 'substitute_amount', 20);
	} else if (kind === 'paid') {
		for (const key of ['reconciliation_pending', 'reparations_paid', 'reconciliation_offer_pending']) p.flags.add(P + key);
		p.vars.set(P + 'reconciliation_due_day', 160); p.predicates.set(P + 'participant_needs_reconciliation', true);
	} else {
		p.flags.add(P + 'victor_renewal_requested'); p.predicates.set(P + 'victor_renewal_is_current', true);
		p.predicates.set(P + 'victor_relationship_is_available', true); p.predicates.set(P + 'victor_request_epoch_is_current', true);
		p.vars.set(P + 'victor_request_host_id', f.host.identity); p.vars.set(P + 'victor_request_origin_host_id', f.host.identity);
		p.vars.set(P + 'victor_request_generation', 4); p.vars.set(P + 'victor_request_sequence', 3); p.vars.set(P + 'victory_count', 3);
	}
	return p;
}
function gateFor(name) {
	if (doctrine.includes(name)) return P + 'host_doctrine_view_is_open';
	if (priority.includes(name)) return P + 'host_priorities_view_is_open';
	if (partners.includes(name)) return P + 'host_partners_view_is_open';
	if (judgment.includes(name)) return P + 'host_judgment_view_is_open';
	return P + 'host_settlement_view_is_open';
}
const gated = [...doctrine, ...priority, ...partners, ...judgment, 'commit_settlement'];
// The later fixed-cost AI budgeting pass adds metadata without changing payment.
// File-local literals are required here, so reject drift from shared charge tuning.
const fixedPpHints = new Map([
	['ultimatum_pay_settlement', ['ULTIMATUM', 'ultimatum.settlement_pp']],
	['council_speech', ['COUNCIL_SPEECH', 'council.speech_pp']],
	['prepare_defensive_defiance', ['DEFENSIVE_PREPARATION', 'transaction.defensive_preparation_pp_cost']],
	['harden_stockpiles', ['DEFENSIVE_STOCKPILE', 'transaction.defensive_stockpile_pp_cost']],
	['secure_transport', ['DEFENSIVE_TRANSPORT', 'transaction.defensive_transport_pp_cost']],
	['prepare_countermeasures', ['DEFENSIVE_COUNTERMEASURE', 'transaction.defensive_countermeasure_pp_cost']],
	['protect_partner', ['PROTECTION', 'transaction.protection_pp_cost']],
	['arm_offender_enemies', ['COALITION', 'coalition.pp_cost']],
	['send_expedition', ['EXPEDITION', 'expedition.pp_cost']],
	['coerce_occupier', ['OCCUPIER_COERCION', 'occupier_coercion.pp_cost']],
]);
test('AST_preservation_all_existing_decisions_prices_weights_and_gameplay', () => {
	assert.equal(gated.length, 20);
	for (const [id, old] of beforeDecisions) {
		const current = decisions.get(id); assert.ok(current, 'deleted row ' + id);
		for (const key of ['cost', 'custom_cost_trigger', 'custom_cost_text', 'ai_will_do', 'days_remove', 'days_re_enable', 'days_mission_timeout', 'cancel_trigger', 'timeout_effect', 'cancel_effect', 'activation', 'target_array', 'target_root_trigger'])
			assert.deepEqual(field(current, key), field(old, key), id + '.' + key);
		const short = id.slice(P.length);
		if (fixedPpHints.has(short)) {
			const [literal, charge] = fixedPpHints.get(short), token = '@GODS_OF_AFRICA_' + literal + '_PP_COST';
			assert.equal(field(current, 'ai_hint_pp_cost'), token, id + ' fixed AI hint');
			assert.equal(Number(field(load(decisionPath), token)), constants.get('constant:' + P + charge), id + ' shared PP charge');
		} else assert.deepEqual(field(current, 'ai_hint_pp_cost'), field(old, 'ai_hint_pp_cost'), id + ' unchanged AI hint');
		if (gated.includes(short)) {
			const gate = gateFor(short);
			assert.deepEqual(field(current, 'visible'), [{ key: gate, op: '=', value: 'yes' }, ...field(old, 'visible')], id + ' live visibility');
			assert.deepEqual(field(current, 'available'), [{ key: 'hidden_trigger', op: '=', value: [{ key: gate, op: '=', value: 'yes' }] }, ...field(old, 'available')], id + ' availability');
			const hidden = field(field(current, 'complete_effect'), 'hidden_effect');
			assert.equal(hidden.length, 1); assert.equal(hidden[0].key, 'if');
			assert.equal(field(hidden[0].value, 'limit')[0].key, gate);
			const body = hidden[0].value.filter(n => n.key !== 'limit' && n.key !== P + 'clear_response_view');
			assert.deepEqual(body, field(field(old, 'complete_effect'), 'hidden_effect'), id + ' wrapped gameplay');
			assert.deepEqual(field(current, 'complete_effect').filter(n => n.key !== 'hidden_effect'), field(old, 'complete_effect').filter(n => n.key !== 'hidden_effect'));
		} else {
			assert.deepEqual(field(current, 'complete_effect'), field(old, 'complete_effect'), id + ' gameplay');
			assert.deepEqual(field(current, 'available'), field(old, 'available'), id + ' availability');
		}
	}
	assert.equal(field(decisions.get(P + 'seek_reconciliation'), 'ai_hint_pp_cost'), undefined, 'mixed free/paid reconciliation must not reserve a fixed fee');
	return { existingRows: beforeDecisions.size, guardedHostRows: gated.length, navigationRows: navigation.length, fixedPpHintsMatchingCharges: fixedPpHints.size };
});
test('AST_owner_trigger_effect_and_tuning_preservation', () => {
	// Only accepted presentation calls in their named owner bodies may be
	// omitted from this legacy gameplay comparison. No wildcard helper strip.
	const presentationHooks = new Map([
		['initialize_system', ['clear_public_strength_observation', 'observe_public_strength']],
		['register_participant', ['clear_public_wrath_values']],
		['archive_invalid_participant', ['clear_public_wrath_values']],
		['refresh_strength', ['observe_public_strength']],
		['enforce_wrath_floor', ['observe_public_wrath_commit']],
		['clean_participant', ['clear_public_wrath_values']],
		['finalize_participant', ['clear_public_wrath_values']],
		['cancel_on_unifier_loss', ['clear_public_strength_observation', 'reset_public_strength_values']],
		['cancel_participant', ['clear_public_wrath_values']],
		['clean_system', ['clear_public_strength_observation', 'reset_public_strength_values']],
	].map(([owner, hooks]) => [P + owner, hooks.map(x => P + x)]));
	const presentationNames = new Set([...presentationHooks.values()].flat());
	// These accepted industrial owners are replayed by the dedicated actual-
	// source integration suite. Preserve every other legacy owner here.
	const industrialOwners = new Set(['initialize_system', 'run_owner_tick',
		'register_participant', 'archive_invalid_participant', 'build_need_profile',
		'select_demand_family', 'create_demand_contract', 'compute_partial_payment_amount',
		'transfer_payment', 'resolve_full_compliance', 'apply_partial_delivery',
		'clear_demand', 'fail_demand', 'clean_participant', 'finalize_participant',
		'cancel_on_unifier_loss', 'cancel_participant', 'commit_final_settlement'].map(x => P + x));
	const strengthChangedOwners = new Map([
		[effectPath, new Set(['try_register_participant', 'activate_system', 'refresh_strength', 'clean_system'].map(x => P + x))],
		[recoveryPath, new Set([P + 'revoke_current_epoch'])],
	]);
	for (const path of [effectPath, recoveryPath]) {
		const observed = new Map();
		function strip(nodes, owner) { return nodes.flatMap(n => {
			if (n.key === P + 'clear_response_view') return [];
			if (presentationNames.has(n.key) && !Array.isArray(n.value)) {
				assert.equal(path, effectPath, 'presentation hook file');
				assert.ok(presentationHooks.get(owner)?.includes(n.key), owner + ' hook ' + n.key);
				assert.equal(n.op, '='); assert.equal(n.value, 'yes');
				const key = owner + '/' + n.key;
				observed.set(key, (observed.get(key) ?? 0) + 1);
				return [];
			}
			return [{ ...n, value: Array.isArray(n.value) ? strip(n.value, owner ?? n.key) : n.value }];
		}); }
		let expected = historical.get(path);
		if (path === effectPath) {
			let replacements = 0;
			function normalize(nodes) { return nodes.flatMap(n => {
				if (n.key === 'divide_temp_variable' && assignment(n)[0] === P + 'strength_chaos' && assignment(n)[1] === 'constant:' + P + 'strength.chaos_divisor') {
					replacements++;
					const divide = structuredClone(n), multiply = structuredClone(n);
					divide.value[0].value = 'constant:chaos_meter_tier_range.tier_final.min';
					multiply.key = 'multiply_temp_variable'; multiply.value[0].value = 'constant:' + P + 'strength.component_max';
					return [divide, multiply];
				}
				return [{ ...n, value: Array.isArray(n.value) ? normalize(n.value) : n.value }];
			}); }
			expected = normalize(expected); assert.equal(replacements, 1);
		}
		const unchanged = ns => ns.filter(n => !(path === effectPath && industrialOwners.has(n.key)) && !strengthChangedOwners.get(path).has(n.key));
		assert.deepEqual(unchanged(strip(load(path))), unchanged(expected), path + ' unchanged owners');
		if (path === effectPath) for (const [owner, hooks] of presentationHooks)
			for (const hook of hooks) assert.equal(observed.get(owner + '/' + hook), 1, owner + ' exactly one ' + hook);
	}
	for (const old of historical.get(triggerPath)) {
		const actual = block(load(triggerPath), old.key);
		if (suffixes.includes(old.key.slice(P.length))) assert.deepEqual(actual, [{ key: 'NOT', op: '=', value: [{ key: 'has_country_flag', op: '=', value: P + 'final_ultimatum_pending' }] }, ...old.value]);
		else if (old.key === P + 'participant_can_receive_protection' && actual.length === 1 && actual[0].key === 'custom_trigger_tooltip') {
			// Parent-owned F2: this exact wrapper and one private policy gate.
			assert.equal(actual[0].op, '=');
			const wrapped = actual[0].value;
			assert.deepEqual(wrapped.filter(n => n.key === 'tooltip'), [{ key: 'tooltip', op: '=', value: P + 'protection_target_requirements_tt' }]);
			assert.deepEqual(wrapped.filter(n => n.key === P + 'protection_relationship_is_eligible'), [{ key: P + 'protection_relationship_is_eligible', op: '=', value: 'yes' }]);
			assert.deepEqual(wrapped.filter(n => !['tooltip', P + 'protection_relationship_is_eligible'].includes(n.key)), old.value.filter(n => !(n.key === 'has_country_flag' && n.value === P + 'reliable_memory_applied')), old.key + ' retained original requirements');
		}
		else if ([P + 'current_demand_can_be_paid', P + 'partial_payment_is_affordable'].includes(old.key)) {
			// Physical industrial payment gates are executed in the integration suite.
			assert.ok(allNodes(actual).some(n => n.key === P + (old.key.endsWith('can_be_paid') ? 'industry_full_payment_can_execute' : 'industry_partial_payment_can_execute')));
		}
		else assert.deepEqual(actual, old.value, old.key);
	}
	const constantPath = 'common/script_constants/012_africa_gods_constants.txt';
	const expectedTuning = historical.get(constantPath).map(n => n.key === P + 'strength' ? { ...n, value: n.value.filter(x => x.key !== 'chaos_divisor') } : n);
	const currentTuning = load(constantPath).map(n => {
		if (n.key === P + 'history_kind') {
			assert.deepEqual(n.value.filter(x => x.key === 'industry_service_ended'), [{ key: 'industry_service_ended', op: '=', value: '23' }]);
			return { ...n, value: n.value.filter(x => x.key !== 'industry_service_ended') };
		}
		if (n.key !== P + 'protection') return n;
		const gate = n.value.filter(x => x.key === 'minimum_completed_demands');
		if (!gate.length) return n;
		assert.deepEqual(gate, [{ key: 'minimum_completed_demands', op: '=', value: '3' }], 'parent-owned F2 minimum');
		assert.equal(field(block(historical.get(constantPath), n.key), 'minimum_completed_demands'), undefined);
		return { ...n, value: n.value.filter(x => x.key !== 'minimum_completed_demands') };
	});
	assert.deepEqual(currentTuning, expectedTuning);
	const enumAst = block(load('common/script_constants/012_africa_gods_response_constants.txt'), P + 'response_view');
	assert.equal(enumAst[0].key, 'schema'); assert.equal(field(enumAst[0].value, 'data'), 'int');
	assert.deepEqual(enumAst.slice(1).map(n => [n.key, Number(n.value)]), [['overview', 0], ['priorities', 1], ['partners', 2], ['judgment', 3]]);
	return { unchangedOwnerBodiesPreserved: true, industrialOwnerCoverage: 'dedicated production integration suite', acceptedStrengthNormalization: 'shared final-tier endpoint', otherTuningPreserved: true };
});
test('012_GODS_STRENGTH_CHAOS_component_curve', () => {
	const body = field(block(load(effectPath), P + 'refresh_strength'), 'if');
	const oldBody = field(block(historical.get(effectPath), P + 'refresh_strength'), 'if');
	const key = P + 'strength_chaos';
	function component(nodes) {
		const start = nodes.findIndex(n => n.key === 'set_temp_variable' && assignment(n)[0] === key && assignment(n)[1] === 'global.chaos_meter_value');
		const end = nodes.findIndex((n, i) => i >= start && n.key === 'clamp_temp_variable' && field(n.value, 'var') === key);
		assert.ok(start >= 0 && end > start); return nodes.slice(start, end + 1);
	}
	const publication = body.find(n => n.key === 'if' && field(n.value, 'limit')?.some(x => x.key === P + 'strength_input_factors_applied'));
	assert.ok(publication);
	const weightedBody = publication.value;
	const weightAt = weightedBody.findIndex(n => n.key === 'set_temp_variable' && assignment(n)[0] === P + 'strength_component' && assignment(n)[1] === key);
	const divisor = weightedBody.find(n => n.key === 'divide_temp_variable' && assignment(n)[0] === P + 'strength_target');
	assert.ok(weightAt > 0 && divisor);
	const weighting = [...weightedBody.slice(weightAt, weightAt + 3), divisor];
	const obsolete = 'constant:' + P + 'strength.chaos_divisor';
	constants.set(obsolete, Number(field(block(historical.get('common/script_constants/012_africa_gods_constants.txt'), P + 'strength'), 'chaos_divisor')));
	const maximum = constants.get('constant:' + P + 'strength.component_max');
	const budget = maximum * constants.get('constant:' + P + 'value.strength_chaos_weight') / constants.get('constant:' + P + 'strength.weighted_divisor');
	const points = [...new Set([maximum, chaosEndpoint * 1.2, ...chaosRanges.filter(n => n.key !== 'schema').flatMap(n => n.value.filter(x => ['min', 'max', 'plus'].includes(x.key)).map(x => Number(x.value)))])].sort((a, b) => a - b);
	const rows = [];
	try {
		for (const flags of [[], ['africa_evolution_ii_logged'], ['africa_evolution_iii_logged'], ['africa_evolution_ii_logged', 'africa_evolution_iii_logged']]) {
			let previous = -1;
			for (const meter of points) {
				function run(nodes) { const f = fixture(), ctx = f.context(); f.state.globals.set('chaos_meter_value', meter); flags.forEach(x => f.state.globalFlags.add(x)); ctx.temps.set(P + 'strength_target', 0); f.run(component(nodes), ctx); f.run(weighting, ctx); return { component: ctx.temps.get(key), contribution: ctx.temps.get(P + 'strength_target') }; }
				const before = run(oldBody), after = run(body);
				const bonus = (flags.includes('africa_evolution_ii_logged') ? constants.get('constant:' + P + 'strength.evolution_ii_amplifier') : 0) + (flags.includes('africa_evolution_iii_logged') ? constants.get('constant:' + P + 'strength.evolution_iii_amplifier') : 0);
				assert.ok(Math.abs(after.component - Math.min(maximum, meter / chaosEndpoint * maximum + bonus)) < 1e-8);
				assert.ok(after.component >= previous && after.contribution >= 0 && after.contribution <= budget + 1e-8); previous = after.component;
				if (meter >= chaosEndpoint) assert.equal(after.component, maximum);
				if (meter === maximum && flags.length === 0) { assert.equal(before.component, maximum); assert.ok(after.component < maximum); }
				rows.push({ meter, evolutionFlags: flags, before, after });
			}
		}
	} finally { constants.delete(obsolete); }
	return { sourceArithmeticOnly: true, cases: rows.length, maximumContribution: budget, sharedEndpoint: chaosEndpoint, rows };
});

test('012_GODS_HOST_DOCTRINE_ALL_NEEDS', () => {
	for (const lane of ['emergency', 'support', 'air_defense']) for (const saved of [undefined, 0, 1, 2, 3, 999]) {
		const f = fixture(); allNeeds(f, lane); targetContext(f); f.host.vars.delete(P + 'doctrine');
		if (saved !== undefined) f.host.vars.set(viewKey, saved);
		assert.equal(doctrine.filter(x => f.visible(x)).length, 3);
		assert.equal([...priority, ...partners, ...judgment, ...navigation.filter(x => x !== 'return_to_overview')].some(x => f.visible(x)), false);
	}
	return { laneAndSavedViewCases: 18 };
});
test('012_GODS_HOST_PRIORITY_AND_OFFENDER', () => {
	for (const lane of ['emergency', 'support', 'air_defense']) {
		const f = fixture(); allNeeds(f, lane); targetContext(f);
		assert.deepEqual(navigation.filter(x => f.visible(x)), navigation.slice(0, 3));
		f.click('open_priorities'); assert.equal(f.host.vars.get(viewKey), view('priorities'));
		assert.equal(priority.filter(x => f.visible(x)).length, 6);
		assert.equal(f.visible('prioritize_' + lane), true);
		assert.equal(f.visible('commit_settlement'), false);
		assert.equal(f.visible('return_to_overview'), true);
		f.click('prioritize_land'); assert.equal(f.host.vars.has(viewKey), false);
		assert.equal(f.state.writes.at(-1).effect, P + 'set_priority');
		f.click('open_partner_relations'); assert.equal(partners.filter(x => f.visible(x)).length, 4);
		f.click('return_to_overview'); f.click('open_judgments'); assert.equal(judgment.filter(x => f.visible(x)).length, 4);
		// Capacity must be evaluated on ROOT, never the participant inside the array.
		f.host.predicates.set(P + 'priority_offender_capacity_available', false);
		f.participant.predicates.set(P + 'priority_offender_capacity_available', true);
		for (const key of ['can_escalate_offense', 'coalition_target_is_valid', 'occupier_coercion_target_is_valid']) f.participant.predicates.set(P + key, false);
		assert.equal(f.testTrigger('host_has_judgment_context'), false);
	}
	return { advancedVariants: 3, priorityPrimaryCount: 6, partnersPrimaryCount: 4, judgmentPrimaryCount: 4, backIsNavigation: true };
});
test('empty_contexts_invalid_view_fallback_and_recovery_back', () => {
	for (const saved of [undefined, 0, -1, 999]) {
		const f = fixture(); if (saved !== undefined) f.host.vars.set(viewKey, saved);
		assert.equal(f.testTrigger('response_view_is_overview'), true);
		assert.equal(navigation.some(x => f.visible(x)), false);
		for (const effect of navigation.slice(0, 3)) f.helper(effect);
		assert.equal(f.host.vars.get(viewKey), saved);
	}
	for (const saved of [1, 2, 3]) {
		const f = fixture(); f.host.arrays.clear(); f.host.vars.set(viewKey, saved);
		assert.equal(f.visible('return_to_overview'), true); f.click('return_to_overview'); assert.equal(f.host.vars.has(viewKey), false);
	}
	return { absentAndInvalidCases: 4, validEmptyFamilyBackCases: 3 };
});
test('012_GODS_HOST_REPLIES_PREEMPT_and_daily_prewarm', () => {
	for (const kind of ['substitute', 'paid', 'victor']) for (const saved of [0, 1, 2, 3]) for (const chosen of [false, true]) {
		const f = fixture(); allNeeds(f); targetContext(f); const target = offer(f, kind);
		f.host.vars.set(viewKey, saved); if (!chosen) f.host.vars.delete(P + 'doctrine');
		assert.equal(f.testTrigger('host_has_pending_answers'), true);
		assert.equal([...doctrine, ...priority, ...partners, ...judgment, ...navigation].some(x => f.visible(x)), false);
		const visible = answers.filter(x => f.visible(x, f.host, target));
		assert.deepEqual(visible, kind === 'substitute' ? answers.slice(0, 2) : kind === 'paid' ? [answers[2]] : answers.slice(1));
		assert.equal(f.host.vars.get(viewKey), saved);
		if (kind === 'substitute') { assert.equal(f.available('accept_substitute'), false); assert.equal(f.available('reject_substitute'), true); }
		if (kind === 'victor') assert.equal(target.flags.has(P + 'participant'), false);
		for (const nav of navigation) f.helper(nav);
		assert.equal(f.host.vars.get(viewKey), saved);
	}
	for (const id of answers) {
		const row = decisions.get(P + id), old = beforeDecisions.get(P + id);
		assert.deepEqual(field(row, 'target_trigger'), [{ key: 'FROM', op: '=', value: [{ key: 'exists', op: '=', value: 'yes' }] }]);
		assert.deepEqual(field(row, 'available'), field(old, 'available'));
		const f = fixture(); assert.equal(f.visible(id), false);
		const ctx = f.context(); assert.equal(f.every(field(row, 'target_trigger'), ctx), true);
		offer(f, id === 'accept_reconciliation' ? 'paid' : 'substitute');
		assert.equal(f.visible(id), true, 'offer appears from live visible without daily refresh');
	}
	return { pendingKindViewDoctrineCases: 24, answerRowsPrewarmed: 3, affordabilityExcludedFromUrgency: true };
});
test('AI_ignore_view_existing_eligibility_and_zero_navigation', () => {
	for (const saved of [undefined, -4, 0, 1, 2, 3, 999]) {
		const f = fixture(); allNeeds(f); targetContext(f); offer(f, 'substitute'); f.host.ai = true;
		if (saved !== undefined) f.host.vars.set(viewKey, saved);
		for (const id of gated) {
			const old = beforeDecisions.get(P + id), row = decisions.get(P + id), ctx = f.context();
			assert.equal(f.every(field(row, 'visible'), ctx), f.every(field(old, 'visible'), ctx), id);
			assert.equal(f.available(id), f.every(field(old, 'available'), ctx), id + ' available');
		}
		assert.equal(navigation.some(x => f.visible(x)), false);
	}
	for (const name of navigation) {
		const row = decisions.get(P + name); assert.equal(field(row, 'cost'), '0');
		assert.equal(constants.get(field(field(row, 'ai_will_do'), 'base')), 0);
	}
	return { AIViewCases: 7, existingHostRowsCompared: 20, scores: 'AST unchanged, no probability claim' };
});
test('reply_helpers_match_exact_legacy_target_predicates', () => {
	let comparisons = 0;
	for (const id of answers) for (let mask = 0; mask < 256; mask++) {
		const f = fixture(), p = f.participant;
		const flags = ['participant', 'negotiation_open', 'substitute_offered', 'victor_renewal_requested', 'reparations_paid', 'reconciliation_offer_pending', 'reconciliation_pending'];
		p.flags.clear(); flags.forEach((key, i) => { if (mask & (1 << i)) p.flags.add(P + key); });
		p.exists = Boolean(mask & 128);
		p.vars.set(P + 'substitute_family', 1); p.vars.set(P + 'substitute_amount', 20); p.vars.set(P + 'reconciliation_due_day', 160);
		p.predicates.set(P + 'participant_needs_reconciliation', true);
		p.predicates.set(P + 'victor_renewal_is_current', p.flags.has(P + 'victor_renewal_requested'));
		p.predicates.set(P + 'victor_relationship_is_available', true); p.predicates.set(P + 'victor_request_epoch_is_current', true);
		p.vars.set(P + 'victor_request_host_id', f.host.identity); p.vars.set(P + 'victor_request_origin_host_id', f.host.identity);
		p.vars.set(P + 'victor_request_generation', 4); p.vars.set(P + 'victor_request_sequence', 3); p.vars.set(P + 'victory_count', 3);
		const ctx = f.context(), row = decisions.get(P + id), old = beforeDecisions.get(P + id);
		assert.equal(f.every(field(row, 'visible'), ctx), f.every(field(old, 'target_trigger'), ctx) && f.every(field(old, 'visible'), ctx), id + ' flags ' + mask);
		comparisons++;
	}
	for (const kind of ['substitute', 'paid', 'victor']) {
		const f = fixture(); const p = offer(f, kind);
		p.predicates.set(P + (kind === 'substitute' ? 'demand_contract_is_current' : kind === 'paid' ? 'reconciliation_epoch_is_current' : 'victor_request_epoch_is_current'), false);
		assert.equal(f.testTrigger('host_has_pending_answers'), false);
		assert.equal(answers.some(id => f.visible(id, f.host, p)), false);
	}
	return { targetTruthComparisons: comparisons, staleAuthorityBoundaries: 3, canonicalLegacyPredicateInternals: 'explicit fixtures, not simulated contracts' };
});
test('settlement_budget_scope_isolation_and_stale_view_click', () => {
	const f = fixture(); allNeeds(f); targetContext(f); f.host.predicates.set(P + 'continent_is_secured', true); f.host.flags.add(P + 'focus_final_council_unlocked');
	assert.equal(f.visible('commit_settlement'), true);
	f.host.vars.set(viewKey, view('priorities')); assert.equal(f.visible('commit_settlement'), false); assert.equal(f.available('commit_settlement'), false); f.click('commit_settlement'); assert.equal(f.state.writes.length, 0);
	assert.equal(priority.filter(x => f.visible(x)).length, 6);
	// Poisoned participant scalar cannot select the host's family.
	f.participant.vars.set(viewKey, view('judgment')); assert.equal(f.visible('mark_offender'), false);
	f.host.vars.set(viewKey, view('partners')); assert.equal(f.available('prioritize_land'), false); f.click('prioritize_land'); assert.equal(f.state.writes.length, 0);
	f.host.vars.delete(P + 'doctrine'); assert.equal(f.visible('commit_settlement'), true);
	offer(f, 'substitute'); assert.equal(f.visible('commit_settlement'), true);
	assert.equal(answers.filter(x => f.visible(x)).length + Number(f.visible('commit_settlement')), 3);
	f.host.predicates.set(P + 'active_host_is_valid', false); f.participant.predicates.set(P + 'active_host_is_valid', true);
	assert.equal(f.testTrigger('host_has_pending_answers'), false);
	const renewal = fixture(), victor = offer(renewal, 'victor'); assert.equal(renewal.visible('accept_reconciliation', renewal.host, victor), true);
	victor.vars.set(P + 'victor_request_host_id', renewal.other.identity); assert.equal(renewal.testTrigger('host_has_pending_answers'), false); assert.equal(renewal.visible('reject_substitute', renewal.host, victor), false);
	return { settlementAllowed: ['overview', 'doctrine', 'pending', 'AI'], prioritySeventhPrimaryPrevented: true, hostAndTargetScalarsIsolated: true };
});
test('all_priority_shortages_and_individual_target_contexts', () => {
	for (const name of ['land_equipment', 'fuel', 'manpower', 'industry', 'transport', 'emergency', 'support_equipment', 'aircraft']) {
		const f = fixture(); f.host.vars.set(P + 'need_' + name, 1);
		if (name === 'support_equipment') f.host.flags.add(P + 'focus_arsenal_support_unlocked');
		if (name === 'aircraft') f.host.flags.add(P + 'focus_logistics_support_unlocked');
		assert.equal(f.visible('open_priorities'), true, name);
		f.click('open_priorities'); assert.equal(priority.filter(x => f.visible(x)).length, 1, name);
	}
	for (const id of [...partners, ...judgment]) {
		const f = fixture(); targetContext(f);
		for (const name of ['can_public_pardon', 'participant_can_receive_protection', 'expedition_target_is_valid', 'proven_offender', 'can_escalate_offense', 'coalition_target_is_valid', 'occupier_coercion_target_is_valid']) f.participant.predicates.set(P + name, false);
		f.participant.flags.delete(P + 'offender');
		const predicate = { public_pardon: 'can_public_pardon', protect_partner: 'participant_can_receive_protection', send_expedition: 'expedition_target_is_valid', mark_offender: 'proven_offender', escalate_offense: 'can_escalate_offense', arm_offender_enemies: 'coalition_target_is_valid', coerce_occupier: 'occupier_coercion_target_is_valid' }[id];
		if (predicate) f.participant.predicates.set(P + predicate, true); else f.participant.flags.add(P + 'offender');
		const nav = partners.includes(id) ? 'open_partner_relations' : 'open_judgments';
		assert.equal(f.visible(nav), true, 'context from ' + id); f.click(nav); assert.equal(f.visible(id), true, id);
	}
	return { independentShortages: 8, isolatedTargetOutcomes: 8, targetAffordabilityDoesNotCloseMenus: true };
});
test('stale_clicks_phase_preflight_and_original_target_scopes', () => {
	for (const id of gated) {
		const f = fixture(); allNeeds(f); targetContext(f);
		f.host.vars.set(viewKey, view(priority.includes(id) ? 'priorities' : partners.includes(id) ? 'partners' : judgment.includes(id) ? 'judgment' : 'overview'));
		// Every guarded action must refuse once the host validity changes.
		f.host.predicates.set(P + 'active_host_is_valid', false); f.click(id);
		assert.equal(f.state.writes.length, 0, id + ' stale invalid-host click');
	}
	for (const id of [...priority, ...partners, ...judgment]) {
		const f = fixture(); allNeeds(f); targetContext(f); f.host.vars.set(viewKey, view(priority.includes(id) ? 'priorities' : partners.includes(id) ? 'partners' : 'judgment'));
		offer(f, 'substitute'); f.click(id); assert.equal(f.state.writes.length, 0, id + ' urgent reply stale click');
	}
	for (const id of [...partners, ...judgment]) {
		const f = fixture(); targetContext(f); f.host.vars.set(viewKey, view(partners.includes(id) ? 'partners' : 'judgment')); f.click(id);
		const write = f.state.writes.at(-1); assert.ok(write, id);
		const hostOwned = ['arm_offender_enemies', 'send_expedition', 'coerce_occupier'].includes(id);
		assert.equal(write.scope, hostOwned ? f.host.identity : f.participant.identity);
	}
	return { staleHostChecks: 20, pendingPreflights: 16, targetedCallerScopeChecks: 8, IDs: 'opaque objects, no numeric conversion' };
});
test('optional_preparation_and_untimed_defiance_preflight_before_payment', () => {
	for (const [i, id] of preparations.entries()) {
		const f = fixture(); f.participant.flags.add(P + 'defiant');
		assert.equal(f.visible(id, f.participant), true); assert.equal(f.available(id, f.participant), true);
		f.participant.flags.add(P + 'final_ultimatum_pending');
		assert.equal(f.visible(id, f.participant), false); assert.equal(f.available(id, f.participant), false);
		const pp = f.participant.pp; f.click(id, f.participant); assert.equal(f.participant.pp, pp); assert.equal(f.state.writes.length, 0);
		f.state.day = 999; assert.equal(f.testTrigger(suffixes[i], f.participant), false, 'expired but unresolved ultimatum');
		f.participant.flags.delete(P + 'final_ultimatum_pending'); f.click(id, f.participant); assert.ok(f.participant.pp < pp);
		const boughtFlags = [...f.participant.flags]; f.participant.flags.add(P + 'final_ultimatum_pending');
		assert.ok(boughtFlags.every(flag => f.participant.flags.has(flag))); const paid = f.participant.pp; f.click(id, f.participant); assert.equal(f.participant.pp, paid);
	}
	const f = fixture(); assert.equal(f.visible('permanent_defiance', f.participant), true);
	f.participant.flags.add(P + 'final_ultimatum_pending'); assert.equal(f.visible('permanent_defiance', f.participant), false); assert.equal(f.testTrigger('participant_can_defy', f.participant), false);
	return { preparationPaymentPreflights: 4, expiredPendingSuppression: true, boughtFlagsPreserved: true, permanentDefianceDeferred: true };
});
test('012_GODS_NEGOTIATION_AND_COUNCIL_and_obligation_deferral', () => {
	const f = fixture(); f.participant.predicates.set(P + 'council_is_open', true);
	for (const flag of ['demand_active', 'negotiation_open', 'reconciliation_pending', 'final_ultimatum_pending']) {
		f.participant.flags.add(P + flag); assert.equal(f.testTrigger('council_response_phase_is_open', f.participant), false);
		assert.equal(f.visible('council_pledge', f.participant), false); assert.equal(f.visible('council_speech', f.participant), false); f.participant.flags.delete(P + flag);
	}
	assert.equal(f.visible('council_pledge', f.participant), true); assert.equal(f.visible('council_speech', f.participant), true);
	f.participant.flags.add(P + 'demand_active'); f.participant.flags.add(P + 'negotiation_open');
	for (const count of [3, 2, 1, 0]) {
		for (const i of [1, 2, 3]) f.participant.predicates.set(P + 'substitute_slot_' + i + '_is_valid', i <= count);
		const slots = [1, 2, 3].filter(i => f.visible('substitute_demand_slot_' + i, f.participant));
		assert.equal(slots.length, count); assert.equal(f.visible('return_to_demand', f.participant), true); assert.equal(f.visible('substitute_demand', f.participant), false);
	}
	return { obligationFlags: 4, namedSlotCounts: [3, 2, 1, 0], duplicateGenericHidden: true, councilReceiptExecution: 'outside model, Council test owns it' };
});
test('012_GODS_OPEN_DEMAND_NARROW_and_SUPPORT_AND_COUNCIL', () => {
	const participantRows = block(load(decisionPath), P + 'participant_category').filter(n => !n.key.endsWith('_mission')).map(n => n.key.slice(P.length));
	const f = fixture(); f.participant.flags.add(P + 'demand_active'); f.participant.predicates.set(P + 'council_is_open', true);
	f.participant.vars.set(P + 'demand_family', constants.get('constant:' + P + 'demand_family.land_equipment'));
	assert.deepEqual(participantRows.filter(x => f.visible(x, f.participant)), ['comply_demand', 'partial_compliance', 'negotiate_demand', 'refuse_demand', 'permanent_defiance']);
	f.participant.vars.set(P + 'demand_family', constants.get('constant:' + P + 'demand_family.continuing_support'));
	assert.equal(participantRows.filter(x => f.visible(x, f.participant)).length, 5); assert.equal(f.visible('sign_support_agreement', f.participant), true);
	f.participant.flags.add(P + 'instalments_signed');
	assert.equal(participantRows.filter(x => f.visible(x, f.participant)).length, 4); assert.equal(f.visible('sign_support_agreement', f.participant), false);
	for (const paid of [0, 17, 101]) {
		f.participant.vars.set(P + 'paid_infantry_k', paid); assert.equal(f.visible('council_pledge', f.participant), false);
		assert.equal(f.visible('comply_demand', f.participant), true);
	}
	return { ordinaryPrimaryCount: 5, continuingSupportBeforeSign: 5, continuingSupportAfterSign: 4, measuredDeliveryExecution: 'unchanged source boundary, not modeled' };
});
test('012_GODS_DEFIANCE_TWO_CLOCKS_and_paid_offer_boundaries', () => {
	const f = fixture(); offer(f, 'paid'); f.participant.flags.add(P + 'defiant'); f.participant.flags.add(P + 'final_ultimatum_pending');
	f.participant.vars.set(P + 'reconciliation_start_day', 100); f.participant.vars.set(P + 'final_ultimatum_due_day', 180);
	f.participant.predicates.set(P + 'final_ultimatum_is_open', true); f.participant.predicates.set(P + 'ultimatum_has_land_or_war', true);
	const rows = ['seek_reconciliation', 'ultimatum_return_land', 'ultimatum_pay_settlement', 'ultimatum_refuse'];
	assert.equal(rows.filter(x => f.visible(x, f.participant)).length, 4);
	assert.equal(preparations.some(x => f.visible(x, f.participant)), false); assert.equal(f.visible('council_pledge', f.participant), false);
	assert.equal(f.visible('accept_reconciliation'), true);
	for (const nav of navigation) f.helper(nav);
	assert.equal(f.participant.vars.get(P + 'reconciliation_due_day'), 160); assert.equal(f.participant.vars.get(P + 'final_ultimatum_due_day'), 180);
	assert.equal(f.participant.flags.has(P + 'reparations_paid'), true);
	f.state.day = 160; assert.equal(f.visible('accept_reconciliation'), false); assert.equal(f.visible('ultimatum_refuse', f.participant), true);
	// The legacy final-ultimatum predicate remains an explicit boundary here.
	// Native dispatch/order is established only as unchanged source, below.
	return { declaredDay130Remaining: [30, 50], paidOfferAcceptanceThroughOriginalDeadline: true, nativeClockDispatch: 'not evaluated' };
});
test('012_GODS_NONDEFIANT_ULTIMATUM_and_pending_exit_saved_view', () => {
	const f = fixture(), p = f.participant; allNeeds(f); p.flags.add(P + 'final_ultimatum_pending'); p.vars.set(P + 'final_ultimatum_due_day', 180);
	p.predicates.set(P + 'ultimatum_has_land_or_war', true); p.predicates.set(P + 'council_is_open', true);
	const rows = ['ultimatum_return_land', 'ultimatum_pay_settlement', 'ultimatum_refuse', 'offer_voluntary_aid', 'seek_reconciliation', 'permanent_defiance', 'council_pledge', 'council_speech', ...preparations];
	assert.deepEqual(rows.filter(x => f.visible(x, p)), rows.slice(0, 4));
	offer(f, 'paid'); assert.deepEqual(rows.filter(x => f.visible(x, p)), [...rows.slice(0, 3), 'seek_reconciliation']);
	assert.equal(f.available('seek_reconciliation', p), false, 'paid offer cannot pay twice');
	f.host.vars.set(viewKey, view('priorities')); assert.equal(f.visible('prioritize_land'), false);
	f.state.day = 160; assert.equal(f.testTrigger('host_has_pending_answers'), false); assert.equal(f.visible('prioritize_land'), true); assert.equal(f.host.vars.get(viewKey), view('priorities'));
	assert.equal(p.vars.get(P + 'final_ultimatum_due_day'), 180); assert.equal(p.flags.has(P + 'reparations_paid'), true);
	return { primaryActionsWithAid: 4, primaryActionsWithPaidReview: 4, storedViewRestoredAfterContextDeadline: true, expiryHandlerNotAutomaticallyInvoked: true };
});
test('native_clock_definitions_and_reconciliation_handlers_unchanged', () => {
	for (const id of ['demand_mission', 'reconciliation_mission', 'final_ultimatum_mission']) assert.deepEqual(decisions.get(P + id), beforeDecisions.get(P + id));
	for (const name of ['start_reconciliation', 'complete_reconciliation', 'fail_reconciliation', 'seek_reconciliation'])
		assert.deepEqual(block(load(effectPath), P + name), block(historical.get(effectPath), P + name), name);
	assert.equal(constants.get('constant:' + P + 'timing.defiance_review_days'), 60); assert.equal(constants.get('constant:' + P + 'ultimatum.deadline_days'), 60);
	const complete = allNodes(block(load(effectPath), P + 'complete_reconciliation'));
	assert.equal(complete.some(n => String(n.key).includes('ultimatum') || String(n.value).includes(P + 'final_ultimatum')), false);
	for (const name of ['resolve_final_ultimatum', 'expire_final_ultimatum']) {
		const nodes = allNodes(block(load(punishmentPath), P + name));
		assert.equal(nodes.some(n => /reconciliation|reparations_paid/.test(n.key) || (typeof n.value === 'string' && /reconciliation|reparations_paid/.test(n.value))), false, name);
	}
	return { missionDefinitionsComparedToBaseline: 3, reconciliationHandlersComparedToBaseline: 4, crossClockWritesAbsent: true, punishmentBaseline: 'not in supplied six-file snapshot, current source inspection only', expiryOrders: 'native reconciliation-first, ultimatum-first and same-day dispatch untested' };
});
test('012_GODS_PAID_OFFER_AND_ULTIMATUM_manual_source_handler_orders', () => {
	for (const order of ['ultimatum_first', 'reconciliation_first']) {
		const f = fixture(), p = f.participant;
		p.flags.add(P + 'defiant'); p.predicates.set(P + 'participant_needs_reconciliation', true); p.predicates.set(P + 'contract_history_identity_is_current', true);
		f.state.day = 100; f.helper('start_reconciliation', p); assert.equal(p.vars.get(P + 'reconciliation_due_day'), 160);
		f.state.day = 120; f.helper('issue_final_ultimatum', p); assert.equal(p.vars.get(P + 'final_ultimatum_due_day'), 180);
		f.state.day = 125; const beforePp = p.pp; f.helper('seek_reconciliation', p);
		assert.equal(p.pp, beforePp - constants.get('constant:' + P + 'transaction.reconciliation_pp_amount'));
		const paidPp = p.pp; f.helper('seek_reconciliation', p); assert.equal(p.pp, paidPp); assert.equal(p.vars.get(P + 'reconciliation_offer_sequence'), 1);
		assert.equal(f.visible('accept_reconciliation'), true);
		f.state.day = 140;
		const reconcile = () => f.run([{ key: P + 'complete_reconciliation', op: '=', value: 'yes' }], { ...f.context(), current: p });
		if (order === 'ultimatum_first') {
			f.helper('resolve_final_ultimatum', p);
			for (const flag of ['reparations_paid', 'reconciliation_offer_pending', 'reconciliation_pending']) assert.equal(p.flags.has(P + flag), true);
			assert.equal(p.vars.get(P + 'reconciliation_due_day'), 160); assert.equal(f.visible('accept_reconciliation'), true); reconcile();
		} else {
			reconcile(); assert.equal(p.vars.get(P + 'final_ultimatum_due_day'), 180); assert.equal(p.flags.has(P + 'final_ultimatum_pending'), true);
			assert.equal(f.visible('ultimatum_refuse', p), true); f.helper('resolve_final_ultimatum', p);
		}
		assert.equal(p.vars.get(P + 'reconciliation_offer_sequence'), 1); assert.equal(p.pp, paidPp);
		assert.equal(p.flags.has(P + 'reconciliation_pending'), false); assert.equal(p.flags.has(P + 'final_ultimatum_pending'), false);
		assert.equal(f.state.writes.filter(x => x.effect === P + 'record_accepted_reconciliation').length, 1); reconcile(); assert.equal(f.state.writes.filter(x => x.effect === P + 'record_accepted_reconciliation').length, 1);
	}
	return { manuallyInvokedOrders: 2, ppDebitCount: 1, paidSequencePreserved: true, nativeDispatchAndHistoryConsumers: 'explicit boundaries, not engine execution' };
});
test('012_GODS_TWO_CLOCK_EXPIRY_manual_source_handler_orders', () => {
	let cases = 0;
	for (const [recDue, ultDue] of [[160, 180], [180, 160], [160, 160]]) for (const first of ['reconciliation', 'ultimatum']) {
		const f = fixture(), p = offer(f, 'paid'); p.vars.set(P + 'reconciliation_due_day', recDue); p.vars.set(P + 'final_ultimatum_due_day', ultDue); p.flags.add(P + 'final_ultimatum_pending'); p.vars.set(P + 'reconciliation_offer_sequence', 7);
		const rec = () => f.helper('fail_reconciliation', p), ult = () => f.helper('expire_final_ultimatum', p);
		f.state.day = Math.min(recDue, ultDue) - 1; rec(); assert.equal(p.flags.has(P + 'reconciliation_pending'), true);
		// Ultimatum expiry also serves explicit refusal and has no due-day guard.
		// Invoke it only at the fixture's declared callback date.
		f.state.day = Math.max(recDue, ultDue);
		if (first === 'reconciliation') { rec(); assert.equal(p.flags.has(P + 'final_ultimatum_pending'), true); ult(); }
		else { ult(); assert.equal(p.flags.has(P + 'reparations_paid'), true); assert.equal(p.vars.get(P + 'reconciliation_due_day'), recDue); rec(); }
		rec(); ult();
		assert.equal(f.state.writes.filter(x => x.nativeBoundary === 'country_event' && field(x.payload, 'id') === 'chaosx.nr12.611').length, 1);
		assert.equal(f.state.writes.filter(x => x.effect === P + 'evaluate_punishment').length, 1);
		assert.equal(p.vars.get(P + 'reconciliation_offer_sequence'), 7); assert.equal(p.flags.has(P + 'reparations_paid'), false); cases++;
	}
	return { dueDateAndManualInvocationOrders: cases, failureDispatchesOnceEach: true, nativeSchedule: 'not simulated', punishmentAndDurableHistory: 'explicit unchanged consumer boundaries' };
});
test('view_cleanup_fresh_generation_and_presentation_only_effects', () => {
	const init = block(load(effectPath), P + 'initialize_system');
	const branch = allNodes(init).find(n => n.key === 'if' && Array.isArray(n.value) && n.value.some(x => x.key === P + 'clear_response_view'));
	assert.ok(branch); assert.ok(JSON.stringify(field(branch.value, 'limit')).includes(P + 'restoration_generation'));
	const clears = allNodes(load(effectPath)).filter(n => n.key === P + 'clear_response_view'); assert.equal(clears.length, 3);
	for (const name of ['cancel_on_unifier_loss', 'clean_system']) assert.equal(allNodes(block(load(effectPath), P + name)).filter(n => n.key === P + 'clear_response_view').length, 1);
	assert.equal(allNodes(load(recoveryPath)).filter(n => n.key === P + 'clear_response_view').length, 1);
	assert.equal(block(load(recoveryPath), P + 'clear_residual_recovery_roster')[0].key, P + 'clear_response_view');
	for (const n of allNodes(load(viewEffectPath))) {
		if (n.key === 'set_variable') assert.equal(assignment(n)[0], viewKey);
		if (n.key === 'clear_variable') assert.equal(n.value, viewKey);
		assert.equal(/mission|political_power|country_flag|reconciliation|reparations|history|deadline/.test(n.key), false, n.key);
	}
	for (const saved of [1, 2, 3]) {
		const f = fixture(); f.host.vars.set(viewKey, saved); f.helper('clear_response_view'); assert.equal(f.host.vars.has(viewKey), false);
	}
	return { lifecycleClearCalls: 4, navigationChangesOnlyPrivateView: true, prioritySelectionsAlsoReturn: 8 };
});
test('qualitative_status_uses_actual_order_and_no_numeric_meter', () => {
	const texts = load(statusPath).filter(n => n.key === 'defined_text');
	const phase = texts.find(n => field(n.value, 'name') === 'GetGodsOfAfricaHostResponsePhase');
	function select(f, root = f.host) {
		const match = phase.value.filter(n => n.key === 'text').find(n => !field(n.value, 'trigger') || f.every(field(n.value, 'trigger'), f.context(root, null)));
		return field(match.value, 'localization_key');
	}
	const f = fixture(); assert.equal(select(f), P + 'response_overview'); f.host.vars.set(viewKey, 999); assert.equal(select(f), P + 'response_overview');
	f.host.vars.set(viewKey, view('priorities')); assert.equal(select(f), P + 'response_priorities'); f.host.vars.delete(P + 'doctrine'); assert.equal(select(f), P + 'response_doctrine');
	offer(f, 'paid'); assert.equal(select(f), P + 'response_pending'); f.host.predicates.set(P + 'active_host_is_valid', false); assert.equal(select(f), P + 'response_no_status');
	assert.equal(/\[\?/.test(sources.get(statusPath).toString()), false);
	const parallel = texts.find(n => field(n.value, 'name') === 'GetGodsOfAfricaParallelReviewText');
	for (const [rec, ult] of [[false, false], [true, false], [false, true], [true, true]]) {
		const fixture = f.participant; fixture.flags[rec ? 'add' : 'delete'](P + 'reconciliation_pending'); fixture.flags[ult ? 'add' : 'delete'](P + 'final_ultimatum_pending');
		const match = parallel.value.filter(n => n.key === 'text').find(n => !field(n.value, 'trigger') || f.every(field(n.value, 'trigger'), f.context(fixture, null)));
		assert.equal(field(match.value, 'localization_key'), P + (rec && ult ? 'parallel_reviews_status' : 'response_no_status'));
	}
	return { statusPrecedence: 'pending, doctrine, view, overview, inactive', parallelStatusFlagCases: 4, extraNumericValues: 0 };
});

// Stable run identities and drift detection let the parent rerun after changes.
const sourceHashes = [...sources].map(([path, bytes]) => ({ path, sha256: hash(bytes) }));
for (const item of sourceHashes) assert.equal(hash(fs.readFileSync(item.path)), item.sha256, 'source changed during run: rerun ' + item.path);
process.stdout.write(JSON.stringify({ evidenceKind: 'bounded_source_model', engineEvaluation: false, sourceHashes, results, failures, executedProductionHelpers: [...executed].sort(), explicitLegacyPredicatesUsed: [...boundaryCalls].sort() }, null, 2) + '\n');
if (failures.length) process.exitCode = 1;
