// Executes the real root immediate/launch predicates with explicit native
// state-existence/iterator fixtures and a runtime-initializer call spy.
const fs = require('fs'), assert = require('assert/strict');
const { parse, namedBlock, assignment, hash } = require('./lib/clausewitz_source_model.js');
const baseline = 'docs/plans/033_acid_rain_plans/validation/probability/current_2026_10_07/sources/';
const before = process.argv.includes('--before');
const eventPath = 'events/033_acid_rain.txt', runtimePath = 'common/scripted_effects/033_acid_rain_effects.txt';
const eventBytes = fs.readFileSync((before ? baseline : '') + eventPath), runtimeBytes = fs.readFileSync((before ? baseline : '') + runtimePath);
const root = parse(eventBytes.toString('utf8')).find(n => n.key === 'country_event' && n.value.some(x => x.key === 'id' && x.value === 'chaosx.nr33.1'));
const immediate = root.value.find(n => n.key === 'immediate').value;
const entryLimit = parse(namedBlock(runtimeBytes.toString('utf8'), 'acid_rain_start_runtime'))[0].value[0].value.find(n => n.key === 'limit').value;
const triggerSource = fs.readFileSync('common/scripted_triggers/033_acid_rain_triggers.txt', 'utf8');
const names = ['acid_rain_launch_preflight_is_valid', 'acid_rain_previous_generation_is_settled', 'acid_rain_cluster_reservation_allows_current_context'];
const predicates = Object.fromEntries(names.map(name => [name, parse(namedBlock(triggerSource, name))[0].value]));
const constants = new Map();
for (const file of ['033_acid_rain_constants.txt', 'event_cluster_constants.txt'])
	for (const category of parse(fs.readFileSync('common/script_constants/' + file, 'utf8')))
		for (const x of Array.isArray(category.value) ? category.value : [])
			if (!Array.isArray(x.value) && Number.isFinite(Number(x.value))) constants.set('constant:' + category.key + '.' + x.key, Number(x.value));
function runCase(f) {
	const flags = new Set(f.globalFlags ?? []), country = { tag: f.tag ?? 'AST', flags: new Set(f.countryFlags ?? []), vars: new Map(Object.entries(f.vars ?? {})) };
	const priorCountry = { flags: new Set(f.paidWork ? ['acid_rain_national_action_active'] : []), vars: new Map([['acid_rain_active_projects', f.project ? 1 : 0]]) };
	const state = { flags: new Set(f.debt ? ['acid_rain_aftercare_unresolved'] : f.lock ? ['acid_rain_action_lock'] : []), vars: new Map() };
	const arrays = new Map([['global.acid_rain_participant_countries', [priorCountry]], ['global.acid_rain_frozen_states', [state]]]);
	const counters = { starts: 0, stages: 0, refreshes: 0, maps: 0, news: 0 };
	let generation = 1;
	const initialOrigin = flags.has('acid_rain_forced_generation');
	const value = (token, scope) => constants.has(token) ? constants.get(token) : Number.isFinite(Number(token)) ? Number(token) : scope.vars.get(token) ?? 0;
	function trigger(n, scope) {
		if (predicates[n.key]) return predicates[n.key].every(x => trigger(x, scope));
		if (n.key === 'NOT') return !n.value.every(x => trigger(x, scope));
		if (n.key === 'AND') return n.value.every(x => trigger(x, scope));
		if (n.key === 'OR') return n.value.some(x => trigger(x, scope));
		if (n.key === 'has_global_flag') return flags.has(n.value);
		if (n.key === 'has_country_flag' || n.key === 'has_state_flag') return scope.flags.has(n.value);
		if (n.key === 'has_variable') return scope.vars.has(n.value);
		if (n.key === 'tag') return scope.tag === n.value;
		if (n.key === 'any_state') return f.validTarget !== false;
		if (n.key === 'all_of_scopes') return arrays.get(n.value.find(x => x.key === 'array').value).every(s => n.value.filter(x => x.key !== 'array').every(x => trigger(x, s)));
		if (n.key === 'check_variable') {
			const [key, token] = assignment(n), a = value(key, scope), b = value(token, scope);
			const kind = n.value.find(x => x.key === 'compare')?.value ?? n.value[0].op;
			if (kind === '>' || kind === 'greater_than') return a > b;
			if (kind === '=' || kind === 'equals') return a === b;
			throw Error('unknown comparison ' + kind);
		}
		throw Error('unknown trigger ' + n.key);
	}
	function execute(nodes) {
		for (let i = 0; i < nodes.length; i++) {
			const n = nodes[i];
			if (n.key === 'if') {
				const hit = n.value.find(x => x.key === 'limit').value.every(x => trigger(x, country));
				if (hit) execute(n.value.filter(x => x.key !== 'limit'));
				if (nodes[i + 1]?.key === 'else') { if (!hit) execute(nodes[i + 1].value); i++; }
			} else if (n.key === 'set_global_flag') flags.add(Array.isArray(n.value) ? n.value.find(x => x.key === 'flag').value : n.value);
			else if (n.key === 'clr_global_flag') flags.delete(n.value);
			else if (n.key === 'clr_country_flag') country.flags.delete(n.value);
			else if (n.key === 'acid_rain_start_runtime') {
				if (entryLimit.every(x => trigger(x, country))) { counters.starts++; generation++; flags.add('acid_rain_runtime_active'); }
			} else if (n.key === 'acid_rain_apply_formation_stage') counters.stages++;
			else if (n.key === 'acid_rain_gui_refresh_read_only') counters.refreshes++;
			else if (n.key === 'acid_rain_gui_open_at_formation') counters.maps++;
			else if (n.key === 'news_event') counters.news++;
			else assert.ok(['set_temp_variable', 'set_variable', 'every_country'].includes(n.key), 'unknown effect ' + n.key);
		}
	}
	execute(immediate);
	assert.equal(country.flags.has('acid_rain_launch_authorized'), false);
	assert.equal(country.flags.has('acid_rain_launch_forced'), false);
	assert.equal(counters.starts, f.expectedStart, f.id + ' initializer');
	assert.equal(counters.stages, f.expectedStart, f.id + ' formation stage replay');
	assert.equal(generation, 1 + f.expectedStart);
	if (!f.expectedStart) { assert.equal(flags.has('acid_rain_forced_generation'), initialOrigin, f.id + ' changed rejected origin'); assert.equal(counters.news, 0); assert.equal(counters.maps, 0); }
	else assert.equal(flags.has('acid_rain_forced_generation'), f.forced);
	assert.deepEqual([...priorCountry.vars], [['acid_rain_active_projects', f.project ? 1 : 0]]);
	assert.equal(state.flags.has('acid_rain_aftercare_unresolved'), !!f.debt);
	return { id: f.id, ...counters };
}
const cases = [
	{ id: 'direct_world_end', globalFlags: ['world_end'], expectedStart: 0 },
	{ id: 'direct_paid_work', globalFlags: ['acid_rain_runtime_resolved'], paidWork: true, expectedStart: 0 },
	{ id: 'direct_paid_project', globalFlags: ['acid_rain_runtime_resolved'], project: true, expectedStart: 0 },
	{ id: 'direct_aftermath', globalFlags: ['acid_rain_runtime_resolved'], debt: true, expectedStart: 0 },
	{ id: 'direct_target_lock', globalFlags: ['acid_rain_runtime_resolved'], lock: true, expectedStart: 0 },
	{ id: 'migration_failed', globalFlags: ['acid_rain_migration_failed_closed'], expectedStart: 0 },
	{ id: 'foreign_reservation', globalFlags: ['acid_rain_cluster_reserved'], expectedStart: 0 },
	{ id: 'duplicate_active', globalFlags: ['acid_rain_runtime_active'], countryFlags: ['acid_rain_launch_authorized', 'acid_rain_launch_forced'], expectedStart: 0 },
	{ id: 'authorized_independent', countryFlags: ['acid_rain_launch_authorized'], expectedStart: 1, forced: false },
	{ id: 'authorized_cluster_after_dispatch', countryFlags: ['acid_rain_launch_authorized', 'event_cluster_member_fire_context'], expectedStart: 1, forced: false },
	{ id: 'settled_second_generation', globalFlags: ['acid_rain_runtime_resolved'], expectedStart: 1, forced: true },
	{ id: 'forced_wins', countryFlags: ['acid_rain_launch_authorized', 'acid_rain_launch_forced'], expectedStart: 1, forced: true },
	{ id: 'cxt_forced', tag: 'CXT', countryFlags: ['acid_rain_launch_authorized'], expectedStart: 1, forced: true },
	{ id: 'no_valid_target', validTarget: false, expectedStart: 0 },
];
console.log(JSON.stringify({ status: 'pass', event_sha256: hash(eventBytes), runtime_sha256: hash(runtimeBytes), cases: cases.map(runCase),
	limits: ['Native state/iterator facts and initializer/presentation effects are fixtures/spies', 'No full formation, resource debit, migration or native multiplayer execution'] }, null, 2));
