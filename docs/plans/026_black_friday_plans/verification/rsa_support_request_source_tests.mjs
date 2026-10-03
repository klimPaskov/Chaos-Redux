// Actual owner helpers with explicit country-scope fixtures. Native dispatch,
// equipment transfer, and unchanged polity eligibility are mocked, not live.
import assert from 'node:assert/strict';
import {parse, get, constants} from './rsa_purchase_source_tests.mjs';
const definitions = new Map();
for (const p of ['common/scripted_effects/012_africa_rsa_support_request_effects.txt', 'common/scripted_effects/012_africa_rsa_effects.txt', 'common/scripted_triggers/012_africa_rsa_triggers.txt']) {
	for (const e of parse(p)) if (Array.isArray(e.value)) definitions.set(e.key, e.value);
}
class Requests {
	constructor() {
		this.host = this.country('host'); this.current = this.root = this.host;
		this.from = null; this.prev = null; this.active = true; this.queued = []; this.shipments = [];
		this.targets = new Map([['africa_rsa_continental_coalition', this.host]]);
		this.host.vars.set('africa_rsa_external_support_count', 0);
	}
	country(id) { return {id, exists: true, eligible: true, flags: new Set(), arrays: new Map(), vars: new Map()}; }
	value(t) {
		if (constants.has(t)) return constants.get(t);
		if (Number.isFinite(Number(t))) return Number(t);
		if (t === 'FROM') return this.from;
		if (t === 'ROOT') return this.root;
		if (t === 'PREV') return this.prev;
		if (t === 'THIS') return this.current;
		if (t.startsWith('event_target:')) return this.targets.get(t.slice(13));
		if (t.endsWith('^num')) return (this.current.arrays.get(t.slice(0, -4)) || []).length;
		return this.current.vars.get(t) || 0;
	}
	invoke(name) {
		if (name === 'africa_rsa_is_eligible_regional_support_target') return this.current.exists && this.current.eligible && !this.current.flags.has('africa_rsa_regional_supporter') && !this.current.flags.has('africa_rsa_regional_support_refused');
		assert.ok(definitions.has(name), name); return this.run(definitions.get(name));
	}
	scope(c, body) {
		assert.ok(c, 'scope fixture missing'); const saved = this.current, prev = this.prev;
		this.current = c; this.prev = saved;
		try { return this.run(body); } finally { this.current = saved; this.prev = prev; }
	}
	run(body) {
		let result = true;
		for (const e of body) {
			const a = e.value;
			if (e.key === 'if') { if (this.run(get(a, 'limit') || [])) this.run(a.filter(x => x.key !== 'limit')); }
			else if (e.key === 'NOT') result = !this.run(a) && result;
			else if (e.key === 'hidden_trigger') result = this.run(a) && result;
			else if (e.key === 'has_country_flag') result = this.current.flags.has(a) && result;
			else if (e.key === 'has_global_flag') { assert.equal(a, 'africa_rsa_civil_war_active'); result = this.active && result; }
			else if (e.key === 'has_event_target') result = this.targets.has(a) && result;
			else if (e.key === 'exists') result = this.current.exists === (a === 'yes') && result;
			else if (e.key === 'set_country_flag') this.current.flags.add(a);
			else if (e.key === 'clr_country_flag') this.current.flags.delete(a);
			else if (e.key === 'save_event_target_as') this.targets.set(a, this.current);
			else if (e.key === 'set_variable') for (const x of a) this.current.vars.set(x.key, this.value(x.value));
			else if (e.key === 'check_variable') {
				const left = this.value(get(a, 'var')), right = this.value(get(a, 'value'));
				assert.equal(get(a, 'compare'), 'less_than'); result = left < right && result;
			}
			else if (e.key === 'is_in_array') result = (this.current.arrays.get(get(a, 'array')) || []).includes(this.value(get(a, 'value'))) && result;
			else if (e.key === 'add_to_array') {
				const n = get(a, 'array'), arr = this.current.arrays.get(n) || [];
				arr.push(this.value(get(a, 'value'))); this.current.arrays.set(n, arr);
			}
			else if (e.key === 'remove_from_array') {
				const n = get(a, 'array'), value = this.value(get(a, 'value'));
				this.current.arrays.set(n, (this.current.arrays.get(n) || []).filter(x => x !== value));
			}
			else if (e.key === 'clear_array') this.current.arrays.set(a, []);
			else if (e.key === 'for_each_scope_loop') {
				for (const c of [...(this.current.arrays.get(get(a, 'array')) || [])]) this.scope(c, a.filter(x => x.key !== 'array'));
			}
			else if (e.key === 'country_event') this.queued.push({recipient: this.current, id: get(a, 'id')});
			else if (e.key === 'send_equipment_fraction') this.shipments.push({donor: this.current, recipient: this.value(get(a, 'target')), fraction: this.value(get(a, 'value'))});
			else if (e.key === 'FROM') result = this.scope(this.from, a) && result;
			else if (e.key.startsWith('event_target:')) result = this.scope(this.value(e.key), a) && result;
			else if (a === 'yes') result = this.invoke(e.key) && result;
			else throw new Error(`unmodeled request command ${e.key}`);
		}
		return result;
	}
	queue(donor) { this.current = this.root = this.host; this.from = donor; this.invoke('africa_rsa_queue_paid_regional_support_request'); }
	reply(donor, accept = true) { this.current = this.root = donor; this.from = this.host; this.invoke(`africa_rsa_${accept ? 'accept' : 'refuse'}_pending_support_request`); }
}
let checks = 0;
for (const ratio of [10000, 5000, 2500]) {
	const m = new Requests(), a = m.country('A'), b = m.country('B'), c = m.country('C');
	m.queue(a); m.queue(a); assert.equal(m.queued.length, 1); checks++;
	m.queue(b); m.queue(c); m.reply(a); m.reply(a);
	assert.equal(m.shipments.length, 1); assert.equal(m.host.vars.get('africa_rsa_external_support_count'), 1); checks++;
	m.queue(a); assert.equal(m.queued.length, 3); checks++;
	m.reply(b); m.reply(c); assert.equal(m.shipments.length, 2); assert.equal(m.host.vars.get('africa_rsa_external_support_count'), 2); checks++;
	assert.equal(m.host.arrays.get('africa_rsa_pending_support_requests').length, 0); assert.ok(!c.flags.has('africa_rsa_regional_support_request_pending')); checks++;
	for (const s of m.shipments) assert.equal(s.fraction, constants.get('constant:africa_rsa_ratio.regional_support_transfer'), `reward not discounted at ${ratio}`);
	const refused = m.country('D'); m.queue(refused); m.reply(refused, false); m.reply(refused, false);
	assert.ok(refused.flags.has('africa_rsa_regional_support_refused')); assert.equal(m.host.arrays.get('africa_rsa_regional_responses').length, 3); checks++;
	const expired = new Requests(), e = expired.country('E'); expired.queue(e); expired.active = false; expired.reply(e);
	assert.equal(expired.shipments.length, 0); assert.ok(!e.flags.has('africa_rsa_regional_support_request_pending')); checks++;
	const changed = new Requests(), f = changed.country('F'); changed.queue(f); f.eligible = false; changed.reply(f);
	assert.equal(changed.shipments.length, 0); assert.ok(!f.flags.has('africa_rsa_regional_support_request_pending')); checks++;
	const cleanup = new Requests(), g = cleanup.country('G'), h = cleanup.country('H'); cleanup.queue(g); cleanup.queue(h);
	cleanup.current = cleanup.root = cleanup.host; cleanup.invoke('africa_rsa_clear_pending_support_requests');
	assert.equal(cleanup.host.arrays.get('africa_rsa_pending_support_requests').length, 0);
	assert.ok(!g.flags.has('africa_rsa_regional_support_request_pending') && !h.flags.has('africa_rsa_regional_support_request_pending')); checks++;
}
const originalTargets = parse('docs/testing/2026-10-03_event26_rsa_before/common/scripted_triggers/012_africa_rsa_triggers.txt');
assert.deepEqual(definitions.get('africa_rsa_is_eligible_regional_support_target'), get(originalTargets, 'africa_rsa_is_valid_regional_support_target')); checks++;
const findReply = p => parse(p).find(e => e.key === 'country_event' && get(e.value, 'id') === 'chaosx.nr12.1202').value;
const before = findReply('docs/testing/2026-10-03_event26_rsa_before/events/012_africa_rsa.txt'), after = findReply('events/012_africa_rsa.txt');
for (const opt of before.filter(e => e.key === 'option')) {
	const now = after.find(e => e.key === 'option' && get(e.value, 'name') === get(opt.value, 'name'));
	assert.deepEqual(get(now.value, 'ai_chance'), get(opt.value, 'ai_chance')); checks++;
}
console.log(JSON.stringify({status: 'pass', requestSourceChecks: checks, duplicateShipments: 0, supporterCap: 2, rewardRatioUnchanged: true, nativeDispatchTransferAndPolityEligibility: 'mocked, no live evidence'}, null, 2));
