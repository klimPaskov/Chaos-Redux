// Executes the actual RSA adapter blocks against mocked native/shared API
// contracts. This is source-model evidence, not an engine or live UI test.
import fs from 'node:fs';
import assert from 'node:assert/strict';

function parse(path) {
	const text = fs.readFileSync(path, 'utf8').replace(/^\uFEFF/, '');
	const tokens = text.replace(/#[^\r\n]*/g, '').match(/"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>]+/g) || [];
	let at = 0;
	function block(close = false) {
		const entries = [];
		while (at < tokens.length && tokens[at] !== '}') {
			const key = tokens[at++], op = tokens[at++];
			assert.ok(['=', '<', '>'].includes(op), `${path}: ${key} ${op}`);
			let value = tokens[at++];
			if (value === '{') value = block(true);
			entries.push({key, op, value});
		}
		if (close) assert.equal(tokens[at++], '}');
		return entries;
	}
	return block();
}
const get = (b, k) => b.find(e => e.key === k)?.value;
const constants = new Map();
for (const path of ['common/script_constants/chaosx_universal_cost_constants.txt', 'common/script_constants/026_black_friday_constants.txt', 'common/script_constants/012_africa_rsa_constants.txt', 'common/script_constants/012_africa_rsa_purchase_constants.txt']) {
	for (const group of parse(path)) if (Array.isArray(group.value)) for (const e of group.value) if (!Array.isArray(e.value) && Number.isFinite(Number(e.value))) constants.set(`constant:${group.key}.${e.key}`, Number(e.value));
}
const functions = new Map();
for (const path of ['common/scripted_triggers/012_africa_rsa_purchase_triggers.txt', 'common/scripted_effects/012_africa_rsa_purchase_effects.txt', 'common/scripted_effects/012_africa_rsa_effects.txt']) for (const e of parse(path)) if (Array.isArray(e.value)) functions.set(e.key, e.value);

const resource = new Map([[1, 'pp'], [2, 'cp'], [11, 'support'], [12, 'trains'], [15, 'stability']]);
const familyResource = new Map([[1, 'pp'], [2, 'cp'], [112, 'support'], [128, 'trains'], [67108864, 'stability']]);
const zero = 'constant:universal_cost_framework.zero';
function oracle(c, ratio, quantum = 1) {
	const ticks = BigInt(Math.round(c * 100000)), q = BigInt(Math.round(quantum * 100000));
	if (!ticks) return 0;
	const numerator = ticks * BigInt(ratio), denominator = 10000n * q;
	return Number((numerator + denominator - 1n) / denominator * q) / 100000;
}
class Model {
	constructor(ratio) {
		this.ratio = ratio; this.vars = new Map(); this.arrays = new Map();
		this.tempVars = new Set(); this.tempArrays = new Set();
		this.stock = {pp: 1000, cp: 1000, support: 1000, trains: 1000, stability: 1};
		this.flags = new Set(['africa_rsa_continental_victory']); this.stateFlags = [];
		this.receipts = new Map(); this.nextId = 0; this.payStep = 0; this.recordStep = 0;
		this.credits = []; this.queued = []; this.nativeGuarantee = true; this.guaranteed = false;
		this.vars.set('africa_rsa_external_support_count', 0);
	}
	value(token) {
		if (constants.has(token)) return constants.get(token);
		if (Number.isFinite(Number(token))) return Number(token);
		if (token.includes('^')) { const [name, i] = token.split('^'); return i === 'num' ? (this.arrays.get(name) || []).length : (this.arrays.get(name) || [])[this.value(i)] ?? 0; }
		return this.vars.get(token) ?? 0;
	}
	assign(key, value) { this.vars.set(key, this.value(value)); }
	tempOutput(key, value) { this.vars.set(key, value); this.tempVars.add(key); }
	check(b) {
		const explicit = get(b, 'var');
		const key = explicit || b[0].key;
		const target = explicit ? get(b, 'value') : b[0].value;
		const cmp = get(b, 'compare') || (b[0].op === '>' ? 'greater_than' : b[0].op === '<' ? 'less_than' : 'equals');
		const a = this.value(key), v = this.value(target);
		return ({equals: a === v, not_equals: a !== v, greater_than: a > v, less_than: a < v, greater_than_or_equals: a >= v, less_than_or_equals: a <= v})[cmp];
	}
	api(name) {
		const kind = resource.get(this.value('universal_cost_affordability_resource_kind'));
		if (name === 'universal_cost_component_is_affordable') return this.stock[kind] >= this.value('universal_cost_affordability_amount');
		if (name === 'universal_cost_source_is_active') return this.ratio !== 10000;
		if (name === 'black_friday_is_active') return this.ratio !== 10000;
		if (name === 'black_friday_quote_custom_cost') {
			if (this.invalidQuote) return false;
			const f = this.value('black_friday_quote_family_mask');
			this.tempOutput('black_friday_quote_final_cost', oracle(this.value('black_friday_quote_ordinary_cost'), this.ratio, familyResource.get(f) === 'stability' ? constants.get('constant:universal_cost_fixed_point_quantum.stability') : 1)); return true;
		}
		if (name === 'universal_cost_quote_integer') {
			this.tempOutput('universal_cost_quote_final_cost', oracle(this.value('universal_cost_quote_ordinary_cost'), this.ratio, this.value('universal_cost_quote_rounding_quantum')) + (this.quoteMismatch || 0));
			this.tempOutput('universal_cost_quote_valid', 1); return true;
		}
		if (name === 'universal_cost_check_quote_affordable') {
			const r = resource.get(this.value('universal_cost_quote_resource_kind'));
			this.tempOutput('universal_cost_quote_affordable', this.stock[r] >= this.value('universal_cost_quote_final_cost') ? 1 : 3); return true;
		}
		if (name === 'black_friday_allocate_owner_transaction') { this.tempOutput('black_friday_owner_transaction_id', ++this.nextId); return true; }
		if (name === 'universal_cost_pay_component') {
			const r = resource.get(this.value('universal_cost_payment_resource_kind')), amount = this.value('universal_cost_payment_amount');
			const ok = ++this.payStep !== this.failPay && this.stock[r] >= amount;
			if (ok) this.stock[r] -= amount;
			this.tempOutput('universal_cost_payment_result', ok ? 1 : 3); return true;
		}
		if (name === 'universal_cost_credit_component') { this.stock[resource.get(this.value('universal_cost_payment_resource_kind'))] += this.value('universal_cost_payment_amount'); this.tempOutput('universal_cost_credit_result', 1); return true; }
		if (name === 'universal_cost_record_transaction') {
			if (++this.recordStep === this.failRecord) { this.tempOutput('universal_cost_record_transaction_result', 3); return true; }
			const id = this.value('universal_cost_transaction_id');
			const receipt = this.receipts.get(id) || {state: 1, rows: []};
			receipt.rows.push({kind: this.value('universal_cost_transaction_resource_kind'), paid: this.value('universal_cost_transaction_actual_paid_cost'), ordinary: this.value('universal_cost_transaction_ordinary_cost'), source: this.value('universal_cost_transaction_source_id'), component: this.value('universal_cost_transaction_component_id')});
			this.receipts.set(id, receipt); this.tempOutput('universal_cost_record_transaction_result', 1); return true;
		}
		if (name === 'universal_cost_refund_transaction') {
			const id = this.value('universal_cost_transaction_id'), receipt = this.receipts.get(id);
			this.tempOutput('universal_cost_transaction_found_index', receipt ? id : -1); this.tempOutput('universal_cost_transaction_lookup_result', receipt ? 1 : 0);
			if (this.refundRejected) { this.tempOutput('universal_cost_refund_transaction_result', 3); return true; }
			this.tempOutput('universal_cost_refund_transaction_result', receipt && receipt.state === 1 ? 1 : 0);
			if (receipt && receipt.state === 1) { for (const row of receipt.rows) this.stock[resource.get(row.kind)] += row.paid; receipt.state = 2; }
			if (receipt) { const states = this.arrays.get('universal_cost_transaction_states') || []; states[id] = receipt.state; this.arrays.set('universal_cost_transaction_states', states); }
			return true;
		}
		if (name === 'universal_cost_settle_transaction') { const receipt = this.receipts.get(this.value('universal_cost_transaction_id')); const ok = receipt?.state === 1 && !this.failSettle; if (ok) receipt.state = 4; this.tempOutput('universal_cost_settle_transaction_result', ok ? 1 : 0); return true; }
		if (name === 'africa_rsa_queue_paid_regional_support_request') { assert.ok(!this.targetPending); this.targetPending = true; this.queued.push('chaosx.nr12.1202'); return true; }
		if (name === 'black_friday_record_achievement_transaction') { if (this.natural !== false && this.ratio !== 10000) { const id = this.value('black_friday_purchase_transaction_id'); assert.equal(this.receipts.get(id)?.state, 4); this.credits.push({id, family: this.value('black_friday_purchase_family_id')}); } return true; }
		if (name === 'africa_rsa_is_valid_regional_support_target') return this.routeValid !== false && !this.targetPending;
		if (['africa_is_current_host', 'africa_rsa_is_continental_coalition', 'africa_rsa_exile_recovery_can_be_completed'].includes(name)) return this.routeValid !== false;
		if (['africa_rsa_check_postwar_first_proof', 'africa_consume_first_proof_recovery_ready'].includes(name)) return true;
		return undefined;
	}
	invoke(name) {
		// Conservative documented helper lifetime: caller-created temporary
		// storage survives; storage created only inside this helper does not.
		const varsBefore = new Set(this.tempVars), arraysBefore = new Set(this.tempArrays);
		try {
			const api = this.api(name); if (api !== undefined) return api;
			assert.ok(functions.has(name), `unknown helper ${name}`);
			return this.run(functions.get(name));
		}
		finally {
			for (const k of this.tempVars) if (!varsBefore.has(k)) { this.vars.delete(k); this.tempVars.delete(k); }
			for (const k of this.tempArrays) if (!arraysBefore.has(k)) { this.arrays.delete(k); this.tempArrays.delete(k); }
		}
	}
	run(b) {
		let result = true, branch = null;
		for (const e of b) {
			const a = e.value;
			if (e.key === 'if' || e.key === 'else_if') {
				if (e.key === 'if') branch = false;
				if (!branch && this.run(get(a, 'limit') || [])) { branch = true; result = this.run(a.filter(x => x.key !== 'limit')) && result; }
				continue;
			}
			if (e.key === 'else') { if (!branch) { result = this.run(a) && result; branch = true; } continue; }
			if (e.key === 'set_temp_variable' || e.key === 'set_variable') { for (const x of a) { this.assign(x.key, x.value); if (e.key === 'set_temp_variable') this.tempVars.add(x.key); else this.tempVars.delete(x.key); } }
			else if (e.key === 'clear_variable') this.vars.delete(a);
			else if (e.key === 'check_variable') result = this.check(a) && result;
			else if (e.key === 'always') result = (a === 'yes') && result;
			else if (e.key === 'NOT') result = !a.some(x => this.run([x])) && result;
			else if (e.key === 'AND') result = this.run(a) && result;
			else if (e.key === 'OR') result = a.some(x => this.run([x])) && result;
			else if (e.key === 'has_variable') result = this.vars.has(a) && result;
			else if (e.key === 'has_country_flag') result = this.flags.has(a) && result;
			else if (e.key === 'has_global_flag') result = (a === 'africa_rsa_civil_war_active') && result;
			else if (e.key === 'set_country_flag') this.flags.add(a);
			else if (e.key === 'clr_country_flag') this.flags.delete(a);
			else if (e.key === 'set_state_flag') this.stateFlags.push(a);
			else if (e.key === 'clear_temp_array') { this.arrays.set(a, []); this.tempArrays.add(a); }
			else if (e.key === 'resize_temp_array') { const name = get(a, 'array'), size = this.value(get(a, 'size')), arr = this.arrays.get(name) || []; arr.length = size; for (let i = 0; i < size; i++) arr[i] ??= 0; this.arrays.set(name, arr); this.tempArrays.add(name); }
			else if (e.key === 'add_to_temp_array') { const name = get(a, 'array'), arr = this.arrays.get(name) || []; arr.push(this.value(get(a, 'value'))); this.arrays.set(name, arr); this.tempArrays.add(name); }
			else if (e.key === 'for_each_loop') { const arr = [...(this.arrays.get(get(a, 'array')) || [])]; arr.forEach((v, i) => { this.vars.set(get(a, 'value'), v); this.vars.set(get(a, 'index'), i); this.run(a.filter(x => !['array', 'value', 'index'].includes(x.key))); }); }
			else if (e.key === 'give_guarantee') { this.guaranteed = this.nativeGuarantee; if (!this.nativeGuarantee && this.expireOnFailure) this.ratio = 10000; }
			else if (e.key === 'is_guaranteed_by') result = this.guaranteed && result;
			else if (e.key === 'country_event') this.queued.push(get(a, 'id'));
			else if (['FROM', 'ROOT', 'capital_scope', 'any_core_state', '275', '681', '719'].includes(e.key)) result = this.run(a) && result;
			else if (['exists', 'is_subject', 'has_capitulated', 'is_on_continent', 'is_neighbor_of', 'has_war_with', 'is_controlled_by', 'original_tag'].includes(e.key)) { const actual = !['original_tag', 'is_subject', 'has_capitulated', 'has_war_with'].includes(e.key); result = (a === 'yes' || a === 'no' ? actual === (a === 'yes') : actual) && result; }
			else if (a === 'yes') result = this.invoke(e.key) && result;
			else throw new Error(`unsupported modeled command ${e.key}`);
		}
		return result;
	}
}

const actions = [
	['relief', {pp: 35, cp: 20, trains: 5, support: 150}, 'africa_rsa_civilians_protected'],
	['regional_request', {pp: 15}, null],
	['citizenship', {pp: 75, stability: 0.05}, 'africa_rsa_citizenship_land_milestone'],
	['sovereignty', {pp: 40, cp: 10}, 'africa_rsa_neighbor_sovereignty_guaranteed'],
	['exile_recovery', {pp: 60, cp: 25}, 'africa_rsa_exile_recovery_completed']
];
let checks = 0;
for (const ratio of [10000, 5000, 2500]) for (const [name, costs, flag] of actions) {
	const expected = Object.fromEntries(Object.entries(costs).map(([r, c]) => [r, ratio === 10000 ? c : oracle(c, ratio, r === 'stability' ? 0.01 : 1)]));
	const m = new Model(ratio); Object.assign(m.stock, expected); const before = {...m.stock};
	m.invoke(`africa_rsa_purchase_${name}`);
	for (const [r, paid] of Object.entries(expected)) assert.ok(Math.abs(m.stock[r] - (before[r] - paid)) < 1e-9, `${name}/${ratio}/${r}`);
	assert.ok(!m.vars.has('africa_rsa_purchase_pending_receipt'));
	assert.equal([...m.receipts.values()][0]?.rows.length, Object.keys(costs).length);
	assert.equal([...m.receipts.values()][0]?.state, 4);
	assert.equal(m.credits.length, ratio === 10000 ? 0 : 1);
	if (flag) assert.ok(m.flags.has(flag)); else assert.deepEqual(m.queued, ['chaosx.nr12.1202']);
	for (const row of [...m.receipts.values()][0].rows) assert.equal(row.source, ratio === 10000 ? 0 : 26);
	checks++;
	for (const [r, paid] of Object.entries(expected)) { const n = new Model(ratio); Object.assign(n.stock, expected); n.stock[r] = paid - (r === 'stability' ? 0.00001 : 0.01); const start = {...n.stock}; n.invoke(`africa_rsa_purchase_${name}`); assert.deepEqual(n.stock, start); assert.equal(n.receipts.size, 0); checks++; }
	for (const failure of ['failPay', 'failRecord']) for (let step = 1; step <= Object.keys(costs).length; step++) { const n = new Model(ratio); n[failure] = step; const start = {...n.stock}; n.invoke(`africa_rsa_purchase_${name}`); for (const r of Object.keys(start)) assert.ok(Math.abs(n.stock[r] - start[r]) < 1e-9, `${failure}/${name}/${step}`); assert.equal(n.credits.length, 0); if (flag) assert.ok(!n.flags.has(flag)); n.invoke('africa_rsa_refund_pending_purchase'); for (const r of Object.keys(start)) assert.ok(Math.abs(n.stock[r] - start[r]) < 1e-9); checks++; }
}
for (const ratio of [5000, 2500]) {
	const g = new Model(ratio); g.nativeGuarantee = false; g.expireOnFailure = true; const initial = {...g.stock}; g.invoke('africa_rsa_purchase_sovereignty'); assert.deepEqual(g.stock, initial); assert.equal(g.credits.length, 0); assert.ok(!g.flags.has('africa_rsa_neighbor_sovereignty_guaranteed')); checks++;
	const m = new Model(ratio); m.quoteMismatch = 1; const initialM = {...m.stock}; m.invoke('africa_rsa_purchase_relief'); assert.deepEqual(m.stock, initialM); assert.equal(m.receipts.size, 0); checks++;
	const d = new Model(ratio); d.natural = false; d.invoke('africa_rsa_purchase_relief'); assert.equal(d.credits.length, 0); checks++;
}
const prior = parse('docs/testing/2026-10-03_event26_rsa_before/012_africa_rsa_decisions.txt')[0].value;
const current = parse('common/decisions/012_africa_rsa_decisions.txt').find(e => e.key === 'africa_rsa_crisis_category').value;
for (const action of prior) {
	const now = current.find(e => e.key === action.key); assert.ok(now);
	for (const key of ['visible', 'activation', 'target_array', 'target_root_trigger', 'target_trigger', 'fire_only_once', 'days_re_enable', 'days_mission_timeout', 'ai_will_do']) assert.deepEqual(get(now.value, key), get(action.value, key), `${action.key}: ${key}`);
	checks++;
}
for (const ratio of [10000, 5000, 2500]) for (const [name] of actions) {
	for (const blocked of ['routeValid', 'pending', 'invalidQuote']) {
		if (blocked === 'invalidQuote' && ratio === 10000) continue;
		const m = new Model(ratio), before = {...m.stock};
		if (blocked === 'routeValid') m.routeValid = false;
		else if (blocked === 'pending') m.vars.set('africa_rsa_purchase_pending_receipt', 99);
		else m.invalidQuote = true;
		m.invoke(`africa_rsa_purchase_${name}`);
		assert.deepEqual(m.stock, before, `${name}/${ratio}/${blocked}`);
		assert.equal(m.receipts.size, 0); assert.equal(m.credits.length, 0); checks++;
	}
}
for (const ratio of [5000, 2500]) {
	const m = new Model(ratio), before = {...m.stock};
	m.nativeGuarantee = false; m.refundRejected = true;
	m.invoke('africa_rsa_purchase_sovereignty');
	assert.ok(m.vars.has('africa_rsa_purchase_pending_receipt'));
	assert.ok(!m.flags.has('africa_rsa_neighbor_sovereignty_guaranteed'));
	const debited = {...m.stock}; m.invoke('africa_rsa_purchase_relief'); assert.deepEqual(m.stock, debited);
	m.ratio = 10000; m.refundRejected = false; m.invoke('africa_rsa_refund_pending_purchase');
	assert.deepEqual(m.stock, before); assert.ok(!m.vars.has('africa_rsa_purchase_pending_receipt')); checks++;
}
// Each actual normal/blocked/detail text trigger starts a fresh enclosing
// render context. It must publish its quote after nested helper cleanup.
let displayContexts = 0;
for (const d of parse('common/scripted_localisation/012_africa_rsa_purchase_localisation.txt')) {
	if (!Array.isArray(d.value)) continue;
	const trigger = get(get(d.value, 'text') || [], 'trigger');
	if (!trigger?.some(e => e.key.startsWith('africa_rsa_quote_'))) continue;
	for (const ratio of [10000, 5000, 2500]) {
		const m = new Model(ratio); m.run(trigger);
		const quoteCall = trigger.find(e => e.key.startsWith('africa_rsa_quote_')).key;
		const costs = actions.find(([name]) => quoteCall === `africa_rsa_quote_${name}_purchase`)[1];
		for (const r of ['pp', 'cp', 'trains', 'support', 'stability']) {
			const cost = costs[r] || 0;
			assert.equal(m.value(`africa_rsa_purchase_${r}_cost`), ratio === 10000 ? cost : oracle(cost, ratio, r === 'stability' ? 0.01 : 1));
		}
		assert.equal(m.value('africa_rsa_purchase_quote_valid'), 1); displayContexts++; checks++;
	}
}
assert.equal(displayContexts, 45);
let fallbackContexts = 0;
for (const d of parse('common/scripted_localisation/012_africa_rsa_purchase_localisation.txt')) {
	if (!Array.isArray(d.value)) continue;
	const texts = d.value.filter(e => e.key === 'text').map(e => e.value);
	if (!get(texts[0] || [], 'trigger')?.some(e => e.key.startsWith('africa_rsa_quote_'))) continue;
	for (const ratio of [10000, 5000, 2500]) for (const invalid of [false, true]) {
		if (invalid && ratio === 10000) continue;
		const m = new Model(ratio);
		if (invalid) m.invalidQuote = true; else m.vars.set('africa_rsa_purchase_pending_receipt', 99);
		const selected = texts.find(t => !get(t, 'trigger') || m.run(get(t, 'trigger')));
		const details = get(d.value, 'name').endsWith('Details') ? '_details' : '';
		assert.equal(get(selected, 'localization_key'), `africa_rsa_purchase_${invalid ? 'quote_unavailable' : 'order_pending'}${details}`);
		fallbackContexts++; checks++;
	}
}
assert.equal(fallbackContexts, 75);
for (const ratio of [10000, 5000, 2500]) {
	const failed = new Model(ratio), stock = {...failed.stock}; failed.failSettle = true;
	failed.invoke('africa_rsa_purchase_regional_request');
	assert.deepEqual(failed.stock, stock); assert.equal(failed.queued.length, 0); assert.equal(failed.credits.length, 0);
	assert.ok(!failed.vars.has('africa_rsa_purchase_pending_receipt')); checks++;
	const duplicate = new Model(ratio), initial = {...duplicate.stock}; duplicate.targetPending = true;
	duplicate.invoke('africa_rsa_purchase_regional_request'); assert.deepEqual(duplicate.stock, initial); assert.equal(duplicate.receipts.size, 0); checks++;
}
console.log(JSON.stringify({status: 'pass', sourceModelChecks: checks, actions: actions.length, components: 11, ratios: [10000, 5000, 2500], helperTemporaryLifetime: 'caller-preinitialized storage only', nativeAndSharedApis: 'mocked contracts, no live evidence'}, null, 2));

export {parse, get, constants};
