// Bounded source model for Event 012 Council receipts. Run from the mod root.
// Executes production Council preflight/finalizer and shared begin/measure/record.
// Native stock/send and external authority/history/world boundaries are explicit.
// This writes no files and does not prove HOI4 engine execution or timed expiry.
const fs = require('fs');
const assert = require('assert/strict');
const { parse, namedBlock, assignment, constants, hash } = require('../../docs/plans/033_acid_rain_plans/validation/caller_repairs_source_tests_2026_10_03.js');
const prefix = 'gods_of_africa_';
const effectPaths = ['common/scripted_effects/012_africa_gods_council_effects.txt',
	'common/scripted_effects/012_africa_gods_contribution_effects.txt',
	'common/scripted_effects/012_africa_gods_focus_payoff_effects.txt'];
const triggerPaths = ['common/scripted_triggers/012_africa_gods_council_triggers.txt',
	'common/scripted_triggers/012_africa_gods_contribution_triggers.txt',
	'common/scripted_triggers/012_africa_gods_focus_payoff_triggers.txt'];
const constantPaths = ['common/script_constants/012_africa_gods_constants.txt',
	'common/script_constants/012_africa_gods_contribution_constants.txt'];
const sources = Object.fromEntries([...effectPaths, ...triggerPaths, ...constantPaths].map(p => [p, fs.readFileSync(p)]));
for (const p of constantPaths) for (const category of parse(sources[p].toString('utf8')))
	for (const entry of Array.isArray(category.value) ? category.value : [])
		if (!Array.isArray(entry.value) && Number.isFinite(Number(entry.value)))
			constants.set('constant:' + category.key + '.' + entry.key, Number(entry.value));
const effects = new Map(), triggers = new Map();
const executed = new Set();
for (const [paths, table] of [[effectPaths, effects], [triggerPaths, triggers]])
	for (const p of paths) for (const n of parse(sources[p].toString('utf8')))
		if (Array.isArray(n.value)) table.set(n.key, n.value);
const boundaryPredicates = new Set(['participant_epoch_is_current', 'participant_generation_is_current',
	'participant_host_is_active', 'contribution_history_is_proven', 'contribution_contract_is_current']);
const results = [], failures = [];
// Fixtures use three decimal source-accounting precision. IDs/pointers are opaque.
const fixed = n => { assert.ok(Number.isFinite(n), 'opaque reference or nonfinite number used in arithmetic'); return Math.round(n * 1000) / 1000; };
function fixture({ stock = 1500, gainStock = 0, campaign = false } = {}) {
	const country = label => ({ identity: Object.freeze({ opaqueCountryIdentity: label }), vars: new Map(), flags: new Set(), stock: 0, pp: 100 });
	const actor = country('participant'), host = country('host'), other = country('other-host');
	actor.stock = stock; host.stock = gainStock;
	host.vars.set('africa_origin_host_id', host.identity);
	host.vars.set('africa_host_generation', 4);
	host.vars.set(prefix + 'authority_epoch', 9);
	host.vars.set(prefix + 'restoration_generation', 4);
	host.vars.set('africa_common_defence_stockpile', 0);
	host.flags.add(prefix + 'focus_final_council_unlocked');
	actor.vars.set(prefix + 'participant_authority_epoch', 9);
	actor.vars.set(prefix + 'material_transfer_sequence', 0);
	actor.vars.set(prefix + 'last_consumed_material_transfer_id', 0);
	for (const name of ['paid_infantry_k', 'voluntary_paid_infantry_k', 'campaign_paid_infantry_k', 'emergency_paid_infantry_k']) actor.vars.set(prefix + name, 0);
	const targets = new Map([['africa_host', host]]), frames = [new Map()];
	const state = { day: 100, authority: true, history: true, campaign, sends: [], historyWrites: [], worldWrites: 0, flagWrites: [], nextSend: null };
	const temps = () => frames.at(-1);
	function scopeOf(token, current) {
		if (token === 'THIS') return current;
		if (token.startsWith('event_target:')) { const found = targets.get(token.slice(13)); assert.ok(found, 'missing target ' + token); return found; }
		if (token.startsWith('var:')) { const found = current.vars.get(token.slice(4)); assert.ok(found?.vars instanceof Map, 'invalid country pointer ' + token); return found; }
		throw Error('unsupported scope ' + token);
	}
	function value(token, current) {
		assert.equal(typeof token, 'string');
		if (token.startsWith('constant:')) { assert.ok(constants.has(token), 'unknown constant ' + token); return constants.get(token); }
		if (Number.isFinite(Number(token))) return Number(token);
		if (token === 'THIS') return current;
		if (token === 'THIS.id') return current.identity;
		if (token === 'global.num_days') return state.day;
		if (token === 'num_equipment@infantry_equipment') return current.stock;
		if (token === 'max_fuel_k' || token === 'fuel_k') return 0;
		if (token.startsWith('event_target:') && token.includes('.')) {
			const dot = token.indexOf('.'), owner = scopeOf(token.slice(0, dot), current), key = token.slice(dot + 1);
			return key === 'id' ? owner.identity : owner.vars.get(key) ?? 0;
		}
		if (token.startsWith('event_target:')) return scopeOf(token, current);
		if (token.startsWith('var:')) token = token.slice(4);
		assert.ok(!token.includes('.'), 'unhandled scoped token ' + token);
		return temps().get(token) ?? current.vars.get(token) ?? 0;
	}
	function compare(a, b, op) {
		if (op === '=' || op === 'equals') return a === b;
		assert.equal(typeof a, 'number'); assert.equal(typeof b, 'number');
		if (op === '>' || op === 'greater_than') return a > b;
		if (op === '<' || op === 'less_than') return a < b;
		if (op === 'greater_than_or_equals') return a >= b;
		if (op === 'less_than_or_equals') return a <= b;
		throw Error('unsupported comparison ' + op);
	}
	function invoke(name, current, isTrigger = false) {
		const table = isTrigger ? triggers : effects;
		assert.ok(table.has(name), 'missing production helper ' + name);
		executed.add(name);
		const parent = temps(), inherited = new Set(parent.keys());
		frames.push(new Map(parent));
		const result = isTrigger ? table.get(name).every(n => trigger(n, current)) : run(table.get(name), current);
		const child = frames.pop();
		for (const key of inherited) parent.set(key, child.get(key));
		return result;
	}
	function trigger(n, current) {
		if (['AND', 'hidden_trigger'].includes(n.key)) return n.value.every(x => trigger(x, current));
		if (n.key === 'OR') return n.value.some(x => trigger(x, current));
		if (n.key === 'NOT' || n.key === 'NOR') return n.key === 'NOT' ? !n.value.every(x => trigger(x, current)) : !n.value.some(x => trigger(x, current));
		if (n.key === 'has_variable') return current.vars.has(n.value);
		if (n.key === 'has_country_flag') return current.flags.has(n.value);
		if (n.key === 'has_global_flag') return false;
		if (n.key === 'exists') return true;
		if (n.key === 'has_war') return current === host && state.campaign;
		if (n.key === 'has_war_with') return false;
		if (n.key === 'has_equipment') { assert.equal(n.value[0].key, 'infantry_equipment'); return compare(current.stock, value(n.value[0].value, current), n.value[0].op); }
		if (n.key === 'has_political_power') return compare(current.pp, value(n.value, current), n.op);
		if (n.key === 'check_variable') { const [key, token] = assignment(n); return compare(value(key, current), value(token, current), n.value.find(x => x.key === 'compare')?.value ?? n.value[0].op); }
		if (n.key.startsWith('set_temp_variable') || n.key === 'add_to_temp_variable' || n.key === 'modulo_temp_variable') { mutate(n, current); return true; }
		if (n.key.startsWith('event_target:') || n.key.startsWith('var:')) return n.value.every(x => trigger(x, scopeOf(n.key, current)));
		const short = n.key.slice(prefix.length);
		if (boundaryPredicates.has(short)) {
			if (short === 'contribution_contract_is_current') return false; // No ordinary contract in Council fixtures.
			return short === 'contribution_history_is_proven' ? state.history : state.authority;
		}
		if (triggers.has(n.key)) return invoke(n.key, current, true);
		throw Error('unsupported trigger ' + n.key);
	}
	function mutate(n, current) {
		const [key, token] = assignment(n), right = value(token, current);
		const store = n.key.includes('_temp_variable') ? temps() : current.vars;
		const left = store.get(key) ?? 0;
		if (n.key.startsWith('set_')) store.set(key, right);
		else {
			assert.ok(Number.isFinite(left) && Number.isFinite(right), 'arithmetic on opaque country identity');
			if (n.key.startsWith('add_to_')) store.set(key, fixed(left + right));
			else if (n.key.startsWith('subtract_from_')) store.set(key, fixed(left - right));
			else if (n.key.startsWith('multiply_')) store.set(key, fixed(left * right));
			else if (n.key.startsWith('modulo_')) store.set(key, (Math.round(left * 1000) % Math.round(right * 1000)) / 1000);
			else throw Error('unsupported mutation ' + n.key);
		}
	}
	function run(nodes, current) {
		for (let i = 0; i < nodes.length; i++) {
			const n = nodes[i];
			if (n.key === 'if') {
				let hit = n.value.find(x => x.key === 'limit').value.every(x => trigger(x, current));
				if (hit) run(n.value.filter(x => x.key !== 'limit'), current);
				while (['else_if', 'else'].includes(nodes[i + 1]?.key)) {
					const branch = nodes[++i];
					if (!hit && (branch.key === 'else' || branch.value.find(x => x.key === 'limit').value.every(x => trigger(x, current)))) {
						run(branch.value.filter(x => x.key !== 'limit'), current); hit = true;
					}
				}
				continue;
			}
			if (n.key === 'set_country_flag' || n.key === 'clr_country_flag') { state.flagWrites.push([n.key, n.value]); current.flags[n.key === 'set_country_flag' ? 'add' : 'delete'](n.value); continue; }
			if (n.key === 'clear_variable') { current.vars.delete(n.value); continue; }
			if (n.key === 'save_event_target_as') { targets.set(n.value, current); continue; }
			if (n.key.startsWith('event_target:') || n.key.startsWith('var:')) { run(n.value, scopeOf(n.key, current)); continue; }
			if (n.key === prefix + 'record_history') { state.historyWrites.push(current.vars.get(prefix + 'history_kind_request')); current.vars.delete(prefix + 'history_kind_request'); continue; }
			if (n.key === prefix + 'sync_world_history') { state.worldWrites++; continue; }
			if (n.key === 'add_opinion_modifier') continue; // World diplomacy consumer is outside this receipt test.
			if (n.key === 'add_political_power') { current.pp = fixed(current.pp + value(n.value, current)); continue; }
			if (n.key === 'send_equipment') {
				const fields = Object.fromEntries(n.value.map(x => [x.key, x.value]));
				assert.equal(fields.equipment, 'infantry_equipment');
				const receiver = scopeOf(fields.target, current), requested = value(fields.amount, current);
				const injected = state.nextSend ?? { debit: requested, gain: requested };
				assert.ok(injected.debit >= 0 && injected.debit <= current.stock);
				current.stock -= injected.debit; receiver.stock += injected.gain;
				state.sends.push({ receiver, requested, ...injected }); state.nextSend = null; continue;
			}
			if (n.key === 'clamp_variable' || n.key === 'clamp_temp_variable') {
				const fields = Object.fromEntries(n.value.map(x => [x.key, x.value])), store = n.key.includes('temp') ? temps() : current.vars;
				let number = value(fields.var, current);
				if (fields.min !== undefined) number = Math.max(number, value(fields.min, current));
				if (fields.max !== undefined) number = Math.min(number, value(fields.max, current));
				store.set(fields.var, fixed(number)); continue;
			}
			if (/^(set|add_to|subtract_from|multiply|modulo)_(temp_)?variable$/.test(n.key)) { mutate(n, current); continue; }
			if (effects.has(n.key)) { invoke(n.key, current); continue; }
			throw Error('unsupported effect ' + n.key);
		}
	}
	return { actor, host, other, state, targets, temps: temps(), get: name => actor.vars.get(prefix + name) ?? 0,
		flag: name => actor.flags.has(prefix + name), gate: name => invoke(prefix + name, actor, true),
		call: name => invoke(prefix + name, actor), attempt(debit, gain = debit) { state.nextSend = { debit, gain }; invoke(prefix + 'council_pledge', actor); } };
}
function check(name, body) {
	try { body(); results.push(name); }
	catch (error) { failures.push({ name, error: error.message }); }
}
check('full_1000_from_1500_and_duplicate_finalization', () => {
	const f = fixture({ campaign: true }); f.attempt(1000);
	assert.equal(f.actor.stock, 500); assert.equal(f.host.stock, 1000);
	assert.equal(f.get('paid_infantry_k'), 1); assert.equal(f.get('voluntary_paid_infantry_k'), 1); assert.equal(f.get('campaign_paid_infantry_k'), 1);
	assert.equal(f.host.vars.get('africa_common_defence_stockpile'), 1000); assert.ok(f.flag('council_voice_pledge'));
	assert.equal(f.state.sends[0].receiver, f.host, 'native send used the wrong recipient');
	assert.equal(f.flag('council_pledge_pending'), false); assert.equal(f.state.historyWrites.length, 1);
	f.call('complete_council_pledge'); f.call('complete_material_transfer'); f.call('record_paid_contribution'); f.attempt(1000);
	assert.equal(f.state.historyWrites.length, 1); assert.equal(f.state.sends.length, 1); assert.equal(f.get('paid_infantry_k'), 1);
	assert.equal(f.state.flagWrites.filter(([op, name]) => op === 'set_country_flag' && name === prefix + 'council_voice').length, 1);
});
check('partial_700_then_300_requires_800', () => {
	const f = fixture(); f.attempt(700); assert.equal(f.actor.stock, 800); assert.equal(f.get('council_pledge_remaining'), 300);
	assert.equal(f.get('paid_infantry_k'), 0.7); assert.equal(f.flag('council_voice'), false); assert.equal(f.get('council_pledge_retry_day'), 0);
	f.actor.stock = 799; assert.equal(f.gate('council_pledge_is_affordable'), false); f.attempt(300); assert.equal(f.state.sends.length, 1);
	f.actor.stock = 800; assert.equal(f.gate('council_pledge_is_affordable'), true); f.attempt(300);
	assert.equal(f.actor.stock, 500); assert.equal(f.get('paid_infantry_k'), 1); assert.equal(f.state.sends[1].requested, 300); assert.ok(f.flag('council_voice_pledge'));
});
check('zero_delivery_retry_and_speech_switch', () => {
	const f = fixture(); f.attempt(0); assert.equal(f.get('paid_infantry_k'), 0); assert.equal(f.get('council_pledge_remaining'), 1000);
	assert.equal(f.get('council_pledge_retry_day'), 107); assert.equal(f.flag('council_voice'), false); assert.equal(f.host.vars.get('africa_common_defence_stockpile'), 0);
	f.attempt(1000); assert.equal(f.state.sends.length, 1); assert.equal(f.gate('council_speech_can_be_made'), true);
	f.call('council_speech'); assert.equal(f.actor.pp, 75); assert.ok(f.flag('council_voice_speech')); f.call('council_speech'); assert.equal(f.actor.pp, 75);
});
check('zero_retry_boundary_runs_actual_preflight', () => {
	const f = fixture(); f.attempt(0); f.state.day = 106; assert.equal(f.gate('council_pledge_can_be_paid'), false);
	f.state.day = 107; assert.equal(f.gate('council_pledge_can_be_paid'), true); f.attempt(1000); assert.equal(f.get('paid_infantry_k'), 1);
});
check('speech_blocked_after_partial', () => {
	const f = fixture(); f.attempt(700); assert.equal(f.gate('council_speech_can_be_made'), false); f.call('council_speech');
	assert.equal(f.actor.pp, 100); assert.equal(f.get('council_pledge_remaining'), 300); assert.equal(f.flag('council_voice'), false);
});
check('receiver_gain_bounded_by_consumed_donor_loss', () => {
	const f = fixture(); f.attempt(700, 900); assert.equal(f.get('paid_infantry_k'), 0.7); assert.equal(f.get('council_pledge_remaining'), 300);
	assert.equal(f.host.vars.get('africa_common_defence_stockpile'), 700); assert.ok(f.flag('material_transfer_mismatch'));
	const g = fixture(); g.attempt(700, 400); assert.equal(g.host.vars.get('africa_common_defence_stockpile'), 400);
});
check('opaque_stale_tuple_and_wrong_purpose_rejected', () => {
	const f = fixture(); f.call('initialize_council_pledge'); assert.equal(f.gate('council_pledge_context_is_current'), true);
	const key = prefix + 'council_pledge_host_id'; f.actor.vars.set(key, f.other.identity); assert.equal(f.gate('council_pledge_context_is_current'), false);
	f.actor.vars.set(key, f.host.identity);
	for (const [field, stale] of [['participant_id', f.other.identity], ['host', f.other], ['origin_id', f.other.identity], ['generation', 3], ['epoch', 8]]) {
		const name = prefix + 'council_pledge_' + field, original = f.actor.vars.get(name);
		f.actor.vars.set(name, stale); assert.equal(f.gate('council_pledge_context_is_current'), false, field + ' drift accepted'); f.actor.vars.set(name, original);
	}
	f.temps.set(prefix + 'contribution_kind', 1); f.temps.set(prefix + 'contribution_requested', 1000); f.temps.set(prefix + 'contribution_voluntary', 1); f.temps.set(prefix + 'contribution_native_emit_kind', 1);
	assert.equal(f.gate('contribution_council_context_is_current'), false); f.actor.flags.add(prefix + 'council_pledge_transfer');
	assert.equal(f.gate('contribution_council_context_is_current'), true); f.temps.set(prefix + 'contribution_requested', 999); assert.equal(f.gate('contribution_inputs_are_owned'), false);
});
check('false_begin_preserves_uncharged_frozen_terms', () => {
	const f = fixture(); f.actor.vars.delete(prefix + 'material_transfer_sequence'); f.attempt(1000);
	assert.equal(f.state.sends.length, 0); assert.equal(f.get('paid_infantry_k'), 0); assert.equal(f.get('council_pledge_remaining'), 1000);
	assert.equal(f.get('council_pledge_retry_day'), 0); assert.equal(f.flag('council_pledge_transfer'), false); assert.equal(f.flag('council_voice'), false);
});
check('unknown_native_quantity_retains_receipt_without_voice', () => {
	const f = fixture({ gainStock: 2147483.647 }); f.attempt(1000);
	assert.equal(f.get('paid_infantry_k'), 0); assert.equal(f.get('council_pledge_remaining'), 1000); assert.equal(f.flag('council_voice'), false);
	assert.ok(f.flag('material_transfer_receipt_pending')); assert.ok(f.flag('material_transaction_unresolved')); assert.equal(f.gate('council_speech_can_be_made'), false);
	f.call('clear_council_pledge'); assert.ok(f.flag('material_transfer_receipt_pending')); assert.ok(f.flag('material_transaction_unresolved'));
});
check('cleanup_retains_measured_contribution', () => {
	const f = fixture(); f.attempt(700); f.call('clear_council_pledge'); assert.equal(f.get('paid_infantry_k'), 0.7);
	assert.equal(f.get('voluntary_paid_infantry_k'), 0.7); assert.equal(f.flag('council_pledge_pending'), false); assert.equal(f.get('last_consumed_material_transfer_id'), 1);
});
check('subset_accumulation_failure_retains_pending_receipt', () => {
	const f = fixture(); f.actor.vars.set(prefix + 'voluntary_paid_infantry_k', 2147483.647); f.attempt(1000);
	assert.equal(f.get('paid_infantry_k'), 0); assert.equal(f.get('last_consumed_material_transfer_id'), 0);
	assert.ok(f.flag('material_transfer_receipt_pending')); assert.ok(f.flag('material_transaction_unresolved'));
	assert.equal(f.get('council_pledge_remaining'), 1000); assert.equal(f.flag('council_voice'), false); assert.equal(f.host.vars.get('africa_common_defence_stockpile'), 0);
});
check('unresolved_native_work_blocks_speech_without_current_terms', () => {
	const f = fixture(); f.actor.flags.add(prefix + 'material_transaction_unresolved'); assert.equal(f.gate('council_speech_can_be_made'), false);
	f.call('council_speech'); assert.equal(f.actor.pp, 100); assert.equal(f.flag('council_voice'), false);
});
check('normal_settlement_source_calls_live_council_cleanup', () => {
	// Call-chain source check only. Do not mock the ordinary settlement finalizer.
	const p = 'common/scripted_effects/012_africa_gods_effects.txt';
	const bytes = fs.readFileSync(p); sources[p] = bytes;
	const finalizer = parse(namedBlock(bytes.toString('utf8'), prefix + 'finalize_participant'))[0].value;
	const outer = finalizer.find(n => n.key === 'if').value;
	assert.ok(outer.some(n => n.key === prefix + 'clear_council_pledge' && n.value === 'yes'), 'normal participant finalizer lacks live Council cleanup');
});
console.log(JSON.stringify({ evidenceKind: 'source_model_not_engine_proof', status: failures.length ? 'fail' : 'pass',
	sources: Object.fromEntries(Object.entries(sources).map(([p, bytes]) => [p, hash(bytes)])), passed: results, failures,
	executedProductionHelpers: [...executed].sort(), boundaries: [...boundaryPredicates].map(n => prefix + n),
	limits: ['Native send/stock observations injected explicitly', 'Authority and historical ledger eligibility external to Council',
		'History/world/opinion consumers external to receipt accounting', 'Three-decimal source arithmetic, no native type or expiry proof',
		'Only infantry Council lane executed, no ordinary tribute/armor/fuel gameplay claim'] }, null, 2));
if (failures.length) process.exitCode = 1;
