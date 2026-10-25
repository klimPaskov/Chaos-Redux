// Actual report-preparer body and caller-storage replay, not native mortality.
// The physical positive-loss guard and report ledger remain separate gates.
'use strict';
const fs = require('fs'), cp = require('child_process'), assert = require('assert/strict');
const { parse, namedBlock, assignment, hash } = require('./lib/clausewitz_source_model.js');
const path = 'common/scripted_effects/033_acid_rain_effects.txt';
const beforeCommit = '0a2927e9b34d94f81758dba7070376bcac8cd0e2';
const oldBytes = cp.execFileSync('git', ['show', beforeCommit + ':' + path]);
assert.equal(hash(oldBytes), 'e5c34d8bd73971609e26b7aef2d4a01cdd4f3f795c2856d83189dfcd546f5def');
const bytes = fs.readFileSync(path), text = bytes.toString('utf8'), oldText = oldBytes.toString('utf8');
const outputs = ['acid_rain_impact_episode_key', 'acid_rain_impact_evacuation_status', 'acid_rain_impact_end_day'];
const oldAnchor = '\t\t\tsave_event_target_as = acid_rain_report_state\n\t\t\tacid_rain_prepare_severe_impact_report = yes';
const newAnchor = '\t\t\tsave_event_target_as = acid_rain_report_state\n' +
	'\t\t\tset_temp_variable = { acid_rain_impact_episode_key = constant:acid_rain_runtime.zero }\n' +
	'\t\t\tset_temp_variable = { acid_rain_impact_evacuation_status = constant:acid_rain_reporting.evacuation_none }\n' +
	'\t\t\tset_temp_variable = { acid_rain_impact_end_day = global.date }\n' +
	'\t\t\tacid_rain_prepare_severe_impact_report = yes';
assert.equal(oldText.split(oldAnchor).length, 2, 'before anchor must be unique');
// The file has evolved since the pinned parent, so the owned surface is the call-site anchor: the three
// output declarations sit directly before the single preparer call, and the pinned parent had none.
assert.equal(text.split(newAnchor).length, 2, 'the three owned declarations precede the single preparer call');
assert.equal(text.split('acid_rain_prepare_severe_impact_report = yes').length, 2, 'one preparer call site');
const constants = new Map();
for (const category of parse(fs.readFileSync('common/script_constants/033_acid_rain_constants.txt', 'utf8')))
	for (const row of Array.isArray(category.value) ? category.value : [])
		if (!Array.isArray(row.value) && Number.isFinite(Number(row.value))) constants.set('constant:' + category.key + '.' + row.key, Number(row.value));
const body = parse(namedBlock(text, 'acid_rain_prepare_severe_impact_report'))[0].value;
assert.equal(namedBlock(text, 'acid_rain_prepare_severe_impact_report'), namedBlock(oldText, 'acid_rain_prepare_severe_impact_report'));
function callSite(ns) {
	for (let i = 0; i < ns.length; i++) {
		if (ns[i].key === 'acid_rain_prepare_severe_impact_report') return { prefix: ns.slice(0, i), next: ns[i + 1] };
		if (Array.isArray(ns[i].value)) { const found = callSite(ns[i].value); if (found) return found; }
	}
}
const nowCall = callSite(parse(namedBlock(text, 'acid_rain_apply_state_pulse'))), oldCall = callSite(parse(namedBlock(oldText, 'acid_rain_apply_state_pulse')));
assert.equal(nowCall.next.key, 'CONTROLLER');
assert(nowCall.next.value.some(x => x.key === 'acid_rain_send_severe_impact_report' && x.value === 'yes'));
const initializers = call => call.prefix.filter(n => n.key === 'set_temp_variable' && outputs.includes(assignment(n)[0]));
assert.equal(initializers(nowCall).length, 3);
assert.equal(initializers(oldCall).length, 0);
const cases = [];
function replay({ kind, evacuated, partial, hasEnd, stale, before }) {
	const saved = new Map([['global.date', 100]]), absent = new Set();
	if (kind === 'superstorm') { saved.set('acid_rain_superstorm_forecast_id', 11); absent.add('acid_rain_severe_cell_id'); }
	else { saved.set('acid_rain_severe_cell_id', 2); absent.add('acid_rain_superstorm_forecast_id'); }
	for (const key of ['acid_rain_superstorm_forecast_end_day', 'acid_rain_severe_forecast_end_day']) {
		if (hasEnd && key.includes(kind === 'superstorm' ? 'superstorm' : 'severe')) saved.set(key, 101);
		else absent.add(key);
	}
	const parent = new Map([['acid_rain_pulse_class', constants.get('constant:acid_rain_mortality_class.' + kind)], ['caller_sentinel', 37]]);
	if (stale) for (const key of outputs) parent.set(key, 999);
	let temps = parent;
	function read(token) {
		if (constants.has(token)) return constants.get(token);
		if (Number.isFinite(Number(token))) return Number(token);
		if (temps.has(token)) return temps.get(token);
		if (saved.has(token)) return saved.get(token);
		throw Error('unknown fact: ' + token);
	}
	function pred(n) {
		if (n.key === 'has_variable') { assert(saved.has(n.value) || absent.has(n.value), 'undeclared absence'); return saved.has(n.value); }
		if (n.key === 'has_state_flag') { assert.equal(n.value, 'acid_rain_evacuated'); return evacuated; }
		if (n.key === 'acid_rain_state_has_partial_evacuation') return partial;
		assert.equal(n.key, 'check_variable');
		assert.equal(n.value.find(x => x.key === 'compare').value, 'equals');
		const [key, value] = assignment(n); return read(key) === read(value);
	}
	function run(ns) {
		for (let i = 0; i < ns.length; i++) {
			const n = ns[i];
			if (n.key === 'if') {
				let taken = false;
				do {
					const b = ns[i], limit = b.value.find(x => x.key === 'limit');
					if (!taken && (!limit || limit.value.every(pred))) { taken = true; run(b.value.filter(x => x.key !== 'limit')); }
					if (!['else_if', 'else'].includes(ns[i + 1]?.key)) break;
					i++;
				} while (true);
			} else { assert.equal(n.key, 'set_temp_variable'); const [key, value] = assignment(n); temps.set(key, read(value)); }
		}
	}
	run(initializers(before ? oldCall : nowCall));
	const inherited = [...parent.keys()]; temps = new Map(parent); run(body);
	for (const key of inherited) if (temps.has(key)) parent.set(key, temps.get(key));
	assert.equal(parent.get('caller_sentinel'), 37);
	const expected = [kind === 'superstorm' ? 11 : 2, evacuated ? 2 : partial ? 1 : 0, hasEnd ? 101 : 100];
	if (before) for (const key of outputs) assert.equal(parent.has(key), false, 'before cold call must expose lost output');
	else assert.deepEqual(outputs.map(key => parent.get(key)), expected);
	cases.push({ kind, evacuated, partial, hasEnd, stale, before, returned: outputs.map(key => parent.get(key) ?? 'absent') });
}
for (const kind of ['severe', 'superstorm']) for (const protection of ['none', 'partial', 'finished']) for (const hasEnd of [false, true]) for (const stale of [false, true])
	replay({ kind, evacuated: protection === 'finished', partial: protection === 'partial', hasEnd, stale, before: false });
for (const kind of ['severe', 'superstorm']) replay({ kind, evacuated: false, partial: false, hasEnd: true, stale: false, before: true });
assert.equal(hash(fs.readFileSync(path)), hash(bytes), 'source changed during replay');
console.log(JSON.stringify({ status: 'pass', runtimeSha256: hash(bytes), beforeCommit, beforeRuntimeSha256: hash(oldBytes), cases: cases.length,
	actualPreparerBodyExecuted: true, onlyThreeCallerDeclarationsChanged: true, coldBeforeNegativeControls: 2,
	limits: ['State scalar facts, evacuation readiness and helper call frames are declared fixtures; no native STATE/CONTROLLER scope execution is claimed.', 'Positive native loss, report delivery/deduplication, damage, prevention, migration and UI evaluation are not executed.'] }, null, 2));
