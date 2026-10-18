// Executes actual interruption/finalizer control flow. Native scopes/arrays,
// arithmetic and delegated consequence/finance/achievement helpers are explicit
// fixtures or call-envelope spies, not native gameplay evidence.
const fs = require('fs'), assert = require('assert/strict');
const { parse, namedBlock, assignment, hash } = require('../../docs/plans/033_acid_rain_plans/validation/caller_repairs_source_tests_2026_10_03.js');
const path = 'common/scripted_effects/033_acid_rain_effects.txt', bytes = fs.readFileSync(path), source = bytes.toString('utf8');
const names = ['acid_rain_interrupt_for_world_end', 'acid_rain_finish_runtime'];
const bodies = Object.fromEntries(names.map(n => [n, parse(namedBlock(source, n))[0].value]));
const constants = new Map();
for (const cat of parse(fs.readFileSync('common/script_constants/033_acid_rain_constants.txt', 'utf8')))
	for (const n of Array.isArray(cat.value) ? cat.value : [])
		if (!Array.isArray(n.value) && Number.isFinite(Number(n.value))) constants.set('constant:' + cat.key + '.' + n.key, Number(n.value));
const delegated = new Set(['acid_rain_advance_consequence_interval', 'acid_rain_assess_window_aftermath', 'acid_rain_033_achievement_close_runtime_episode',
	'acid_rain_reconcile_state_consequences', 'acid_rain_033_achievement_record_dissipation_state_snapshot', 'acid_rain_close_state_evacuation',
	'acid_rain_project_country_obligations', 'acid_rain_store_dissipation_report_facts', 'acid_rain_033_achievement_record_acute_closure',
	'acid_rain_033_achievement_mark_admin_disqualified', 'acid_rain_enter_country_recovery_tail']);
function test(f) {
	const flags = new Set(['acid_rain_runtime_active', 'acid_rain_global_layer_active', 'acid_rain_host_bound', 'acid_rain_host_worker_scheduled']);
	if (f.terminal) flags.add('world_end');
	if (f.natural) flags.add('acid_rain_dissipation_pending');
	if (f.global) flags.add('acid_rain_global_layer_receipt');
	if (f.inactive) flags.delete('acid_rain_runtime_active');
	const states = Array.from({ length: f.count ?? 2 }, (_, id) => ({ id, type: 'state', population: 100000, debt: 2, vars: new Map(),
		flags: new Set(['acid_rain_front_target', 'acid_rain_warning_pending', 'acid_rain_global_pulse_receipt', 'acid_rain_aftercare_unresolved']) }));
	const countries = Array.from({ length: 2 }, (_, id) => ({ id, type: 'country', commitment: 10, flags: new Set(['acid_rain_runtime_host']), vars: new Map() }));
	const globals = new Map([['global.acid_rain_world_coverage', 0.43], ['global.air_contamination_bp', 4999], ['global.acid_rain_total_deaths', 123]]);
	const arrays = new Map([['global.acid_rain_frozen_states', states], ['global.acid_rain_participant_countries', countries],
		...['ordinary', 'severe', 'superstorm'].map(n => ['global.acid_rain_' + n + '_target_states', [...states]]),
		['global.acid_rain_active_consequence_states', [...states]], ['global.acid_rain_pulse_receipt_states', [17, 19]]]);
	const targets = new Map([['acid_rain_runtime_host', countries[0]]]), frames = [new Map([['break', 1]])], calls = [];
	const temps = () => frames.at(-1);
	function value(t, scope) { if (constants.has(t)) return constants.get(t); if (Number.isFinite(Number(t))) return Number(t); return temps().get(t) ?? globals.get(t) ?? scope.vars.get(t) ?? 0; }
	function trigger(n, scope) {
		if (n.key === 'NOT') return !n.value.every(x => trigger(x, scope));
		// hidden_trigger only hides tooltip text; the engine evaluates it like AND.
		if (n.key === 'hidden_trigger') return n.value.every(x => trigger(x, scope));
		if (n.key === 'OR') return n.value.some(x => trigger(x, scope));
		if (n.key === 'has_global_flag') return flags.has(n.value);
		if (n.key === 'has_state_flag') return scope.flags.has(n.value);
		if (n.key === 'has_event_target') return targets.has(n.value);
		if (n.key === 'is_core_of') return false;
		assert.equal(n.key, 'check_variable', 'unknown trigger ' + n.key);
		const [key, token] = assignment(n), kind = n.value.find(x => x.key === 'compare').value;
		if (kind === 'equals') return value(key, scope) === value(token, scope);
		if (kind === 'greater_than') return value(key, scope) > value(token, scope);
		throw Error('unknown comparison ' + kind);
	}
	function helper(name, scope) {
		const parent = temps(), inherited = new Set(parent.keys()); frames.push(new Map(parent)); run(bodies[name], scope);
		const child = frames.pop(); for (const key of inherited) parent.set(key, child.get(key));
	}
	function run(nodes, scope) {
		for (let i = 0; i < nodes.length; i++) {
			const n = nodes[i];
			if (n.key === 'if') {
				const hit = n.value.find(x => x.key === 'limit').value.every(x => trigger(x, scope));
				if (hit) run(n.value.filter(x => x.key !== 'limit'), scope);
				if (nodes[i + 1]?.key === 'else') { if (!hit) run(nodes[i + 1].value, scope); i++; }
			} else if (names.includes(n.key)) helper(n.key, scope);
			else if (n.key === 'for_each_scope_loop') {
				const binding = n.value.find(x => x.key === 'break')?.value ?? 'break';
				for (const s of arrays.get(n.value.find(x => x.key === 'array').value)) {
					if (value(binding, scope) !== 0) break;
					run(n.value.filter(x => !['array', 'break'].includes(x.key)), s);
				}
			} else if (n.key.startsWith('event_target:')) run(n.value, targets.get(n.key.slice(13)));
			else if (n.key === 'set_global_flag') flags.add(n.value);
			else if (n.key === 'clr_global_flag') flags.delete(n.value);
			else if (n.key === 'clr_state_flag' || n.key === 'clr_country_flag') scope.flags.delete(n.value);
			else if (n.key === 'clear_global_event_target') targets.delete(n.value);
			else if (n.key === 'clear_array') arrays.set(n.value, []);
			else if (['set_temp_variable', 'add_to_temp_variable', 'set_variable'].includes(n.key)) {
				const [key, token] = assignment(n), right = value(token, scope);
				if (n.key === 'set_variable') globals.set(key, right);
				else temps().set(key, n.key === 'set_temp_variable' ? right : value(key, scope) + right);
			} else if (delegated.has(n.key)) {
				calls.push({ helper: n.key, scope: scope.type, id: scope.id, keep: temps().get('acid_rain_keep_recovery_operations') });
				// Stress that a called owner can set its default break without
				// truncating either Event 33 cleanup iterator.
				temps().set('break', 1);
			} else if (['country_event', 'news_event', 'add_chaos_meter_value'].includes(n.key)) calls.push({ helper: n.key });
			else throw Error('unknown effect ' + n.key);
		}
	}
	const entry = f.natural ? names[1] : names[0];
	helper(entry, countries[0]); const afterFirst = calls.length; helper(entry, countries[0]); assert.equal(calls.length, afterFirst, 'duplicate cleanup effect');
	assert.equal(globals.get('global.air_contamination_bp'), 4999); assert.equal(globals.get('global.acid_rain_total_deaths'), 123);
	assert.deepEqual(arrays.get('global.acid_rain_pulse_receipt_states'), [17, 19]);
	for (const state of states) { assert.equal(state.population, 100000); assert.equal(state.debt, 2); }
	const shouldClose = f.natural || (f.terminal && !f.inactive);
	if (shouldClose) {
		assert.equal(flags.has('acid_rain_runtime_active'), false); assert.equal(flags.has('acid_rain_runtime_resolved'), true);
		assert.equal(targets.has('acid_rain_runtime_host'), false); assert.equal(flags.has('acid_rain_host_worker_scheduled'), false);
		assert.equal(calls.filter(x => x.helper === 'acid_rain_advance_consequence_interval').length, states.length);
		assert.equal(calls.filter(x => x.helper === 'acid_rain_enter_country_recovery_tail').length, countries.length);
		assert.ok(states.every(s => !s.flags.has('acid_rain_front_target') && s.flags.has('acid_rain_aftercare_unresolved')));
		assert.equal(calls.filter(x => x.helper === 'add_chaos_meter_value').length, f.natural ? 1 : 0);
		assert.equal(calls.filter(x => x.helper === 'news_event').length, f.natural ? 1 : 0);
		assert.equal(globals.get('global.acid_rain_world_coverage'), f.natural ? 1 : 0.43);
		assert.ok(calls.filter(x => x.helper === 'acid_rain_enter_country_recovery_tail').every(x => x.keep === (f.natural ? 1 : 0)));
	} else assert.equal(calls.length, 0);
	return { ...f, closed: shouldClose, delegated_calls: calls.length };
}
const cases = [{ terminal: true }, { terminal: true, global: true }, { terminal: true, count: 1301 }, { terminal: false }, { terminal: true, inactive: true }, { natural: true }, { natural: true, global: true }];
console.log(JSON.stringify({ status: 'pass', runtime_sha256: hash(bytes), cases: cases.map(test),
	limits: ['Delegated aftermath, financial returns and achievements are call spies', 'No native state, finance, pressure-retirement, reload or multiplayer proof'] }, null, 2));
