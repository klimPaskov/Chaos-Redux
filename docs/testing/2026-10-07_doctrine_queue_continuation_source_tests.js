// Actual-source continuation regression. This does not execute HOI4.
// The native doctrine transaction, country initialization, and achievement
// checks are explicit stubs. Queue activation, compaction, closure, wake
// scheduling, and annex cleanup execute their parsed production bodies.
// Run: node docs/testing/2026-10-07_doctrine_queue_continuation_source_tests.js
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const root = path.resolve(__dirname, '../..');
const effectPath = 'common/scripted_effects/027_doctrine_research_effects.txt';
const constantsPath = 'common/script_constants/027_doctrine_research_constants.txt';
const beforePath = 'docs/plans/027_doctrine_research_plans/queue_continuation_before_20261007/027_doctrine_research_effects.txt';
const read = name => fs.readFileSync(path.join(root, name), 'utf8');
const sha = name => crypto.createHash('sha256').update(fs.readFileSync(path.join(root, name))).digest('hex');
function parse(source) {
	const tokens = (source.match(/#[^\r\n]*|"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>#]+/g) || []).filter(t => !t.startsWith('#'));
	let cursor = 0;
	function block(nested = false) {
		const rows = [];
		while (cursor < tokens.length && tokens[cursor] !== '}') {
			const key = tokens[cursor++], op = tokens[cursor++];
			assert(['=', '<', '>'].includes(op), 'Unsupported source token ' + key + ' ' + op);
			let value = tokens[cursor++];
			if (value === '{') value = block(true);
			rows.push({key, op, value});
		}
		if (nested) assert.equal(tokens[cursor++], '}');
		return rows;
	}
	const rows = block();
	assert.equal(cursor, tokens.length);
	return rows;
}
const constants = new Map();
for (const group of parse(read(constantsPath))) {
	for (const row of group.value) if (row.key !== 'schema') constants.set('constant:' + group.key + '.' + row.key, Number(row.value));
}
const first = (rows, key) => rows.find(row => row.key === key)?.value;
const tests = [];
function test(name, action) { action(); tests.push(name); }
function fixture(sourcePath, count = 1, ai = true) {
	const definitions = new Map(parse(read(sourcePath)).map(row => [row.key, row.value]));
	const locals = new Map([...definitions].filter(([key]) => key.startsWith('@')).map(([key, value]) => [key, Number(value)]));
	const saved = new Map(), temporary = new Map(), flags = new Set(), arrays = new Map();
	const events = [], prompts = [], resolved = [], transitions = [];
	const f = {ai, live: true, saved, temporary, flags, arrays, events, prompts, resolved, transitions, depth: 0, maxDepth: 0, resolverDepth: 0, maxResolverDepth: 0};
	const prefix = 'doctrine_research_';
	const batchColumns = ['ids', 'firing_ids', 'stages', 'sizes', 'remaining_choices', 'statuses', 'created_dates', 'human_started', 'start_empty_army', 'start_empty_navy', 'start_empty_air', 'start_empty_special_forces', 'start_empty_chaos_warfare'];
	const receiptColumns = ['ids', 'batch_ids', 'choice_numbers', 'states', 'actions', 'domains', 'grands', 'tracks', 'track_indices', 'subdoctrines', 'pre_levels', 'post_levels'];
	for (const column of batchColumns) arrays.set(prefix + 'batch_' + column, Array.from({length: count}, (_, index) => column === 'ids' || column === 'firing_ids' ? index + 1 : column === 'sizes' || column === 'remaining_choices' ? 5 : column === 'statuses' ? constants.get('constant:doctrine_research_batch_status.queued') : 0));
	for (const column of receiptColumns) arrays.set(prefix + 'receipt_' + column, []);
	saved.set(prefix + 'queued_batches', count);
	saved.set(prefix + 'active_batch_index', -1);
	function value(token) {
		if (typeof token === 'number') return token;
		if (constants.has(token)) return constants.get(token);
		if (locals.has(token)) return locals.get(token);
		if (/^-?\d+(\.\d+)?$/.test(token)) return Number(token);
		if (token.includes('^')) {
			const [name, index] = token.split('^'), a = arrays.get(name) || [];
			return index === 'num' ? a.length : a[value(index)] ?? 0;
		}
		return temporary.has(token) ? temporary.get(token) : saved.get(token) ?? 0;
	}
	function write(name, amount, temp = false) {
		if (name.includes('^')) { const [column, index] = name.split('^'); arrays.get(column)[value(index)] = amount; }
		else (temp ? temporary : saved).set(name, amount);
	}
	function compare(a, b, kind) {
		return kind === 'equals' ? a === b : kind === 'greater_than' || kind === '>' ? a > b : kind === 'less_than' || kind === '<' ? a < b : kind === 'greater_than_or_equals' ? a >= b : kind === 'less_than_or_equals' ? a <= b : (() => { throw Error('Unknown comparison ' + kind); })();
	}
	function predicate(row) {
		if (row.key === 'AND') return row.value.every(predicate);
		if (row.key === 'OR') return row.value.some(predicate);
		if (row.key === 'NOT') return !row.value.some(predicate);
		if (row.key === 'check_variable') {
			if (first(row.value, 'var') !== undefined) return compare(value(first(row.value, 'var')), value(first(row.value, 'value')), first(row.value, 'compare') || 'equals');
			const entry = row.value[0]; return compare(value(entry.key), value(entry.value), entry.op === '=' ? 'equals' : entry.op);
		}
		if (row.key === 'has_country_flag') return flags.has(row.value);
		if (row.key === 'has_variable') return saved.has(row.value);
		if (row.key === 'is_ai') return f.ai === (row.value === 'yes');
		if (row.key === prefix + 'country_is_live') return f.live;
		if (row.key === prefix + 'country_has_valid_action') return true;
		throw Error('Unmodelled predicate ' + row.key);
	}
	function execute(rows) {
		let chain = null;
		for (const row of rows) {
			if (row.key === 'if' || row.key === 'else_if' || row.key === 'else') {
				if (row.key === 'if') chain = false;
				if (!chain && (row.key === 'else' || first(row.value, 'limit').every(predicate))) {
					chain = true; execute(row.value.filter(entry => entry.key !== 'limit'));
				}
				continue;
			}
			chain = null;
			if (['set_variable', 'set_temp_variable', 'add_to_variable', 'add_to_temp_variable', 'subtract_from_temp_variable', 'subtract_from_variable'].includes(row.key)) {
				const entry = row.value[0], temp = row.key.includes('temp'), operand = value(entry.value);
				write(entry.key, row.key.startsWith('set_') ? operand : value(entry.key) + (row.key.startsWith('subtract_') ? -operand : operand), temp);
			} else if (row.key === 'set_country_flag') flags.add(row.value);
			else if (row.key === 'clr_country_flag') flags.delete(row.value);
			else if (row.key === 'clear_variable') saved.delete(row.value);
			else if (row.key === 'clear_array') arrays.set(row.value, []);
			else if (row.key === 'remove_from_array') arrays.get(first(row.value, 'array')).splice(value(first(row.value, 'index')), 1);
			else if (row.key === 'country_event') {
				const id = first(row.value, 'id');
				if (id === 'chaosx.nr27.14') events.push({id, hours: value(first(row.value, 'hours') || '0')});
				else prompts.push({id, batch: saved.get(prefix + 'active_batch_id')});
			} else if (row.key === 'for_loop_effect') {
				const start = value(first(row.value, 'start') || '0'), end = value(first(row.value, 'end') || '0'), name = first(row.value, 'value') || 'v', increment = value(first(row.value, 'add') || '1'), type = first(row.value, 'compare') || 'less_than', stop = first(row.value, 'break');
				const body = row.value.filter(entry => !['start', 'end', 'value', 'add', 'compare', 'break'].includes(entry.key));
				for (let index = start, runs = 0; compare(index, end, type) && runs < 1000; index += increment, runs++) {
					temporary.set(name, index); execute(body); if (stop && value(stop)) break;
				}
			} else if (row.key === prefix + 'initialize_country_state' || row.key === prefix + 'update_achievements') {
				// Explicit boundary: initialized aligned ledger and no award side effects.
			} else if (row.key === prefix + 'ai_resolve_active_batch') {
				f.maxResolverDepth = Math.max(f.maxResolverDepth, ++f.resolverDepth);
				const batch = saved.get(prefix + 'active_batch_id'), index = saved.get(prefix + 'active_batch_index');
				resolved.push(batch);
				for (let choice = 1; choice <= arrays.get(prefix + 'batch_sizes')[index]; choice++) {
					for (const column of receiptColumns) arrays.get(prefix + 'receipt_' + column).push(column === 'batch_ids' ? batch : column === 'choice_numbers' ? choice : 0);
				}
				arrays.get(prefix + 'batch_remaining_choices')[index] = 0;
				call(prefix + 'complete_active_batch'); --f.resolverDepth;
			} else if (definitions.has(row.key)) call(row.key);
			else throw Error('Unmodelled effect ' + row.key);
		}
	}
	function call(name) {
		if (++f.depth > 100) throw Error('Recursive continuation exceeded 100 helper frames');
		f.maxDepth = Math.max(f.maxDepth, f.depth);
		const callerOwned = new Set(temporary.keys());
		execute(definitions.get(name));
		for (const key of temporary.keys()) if (!callerOwned.has(key)) temporary.delete(key);
		--f.depth;
	}
	f.call = suffix => call(prefix + suffix);
	f.deliver = () => { assert(events.length); events.shift(); call(prefix + 'wake_country_batches'); };
	return f;
}
test('literal delayed-event tuning agrees with the shared constant', () => {
	const macro = parse(read(effectPath)).find(row => row.key === '@DOCTRINE_RESEARCH_AI_QUEUE_WAKE_HOURS');
	assert.equal(Number(macro.value), constants.get('constant:doctrine_research_event.ai_queue_wake_hours'));
});
test('frozen source reproduces recursive AI continuation', () => {
	const f = fixture(beforePath, 1201);
	assert.throws(() => f.call('wake_country_batches'), /Recursive continuation exceeded/);
	assert(f.maxResolverDepth > 1);
});
test('1201 queued five-choice batches retain FIFO identities across bounded deliveries', () => {
	const f = fixture(effectPath, 1201);
	f.call('wake_country_batches');
	assert.equal(f.resolved.length, 1);
	assert.equal(f.events.length, 1);
	assert.equal(f.events[0].hours, 1);
	assert.equal(f.saved.get('doctrine_research_queued_batches'), 1200);
	for (let request = 0; request < 10; request++) f.call('resume_queued_batches');
	assert.equal(f.events.length, 1);
	while (f.events.length) f.deliver();
	assert.deepEqual(f.resolved, Array.from({length: 1201}, (_, index) => index + 1));
	assert.equal(f.saved.get('doctrine_research_queued_batches'), 0);
	assert.equal(f.maxResolverDepth, 1);
	assert(!f.flags.has('doctrine_research_active_batch'));
	assert(!f.flags.has('doctrine_research_batch_wake_scheduled'));
});
test('AI-to-human switch uses the controller at delivery and duplicate wake opens no second page', () => {
	const f = fixture(effectPath, 3); f.call('wake_country_batches'); f.ai = false;
	f.deliver(); assert.equal(f.prompts.length, 1); assert.equal(f.prompts[0].batch, 2);
	f.call('wake_country_batches'); assert.equal(f.prompts.length, 1);
	f.call('close_active_batch_and_start_next'); assert.equal(f.prompts.length, 2); assert.equal(f.prompts[1].batch, 3);
});
test('a closed prefix longer than the loop ceiling preserves every queued suffix row', () => {
	const closed = 2501, queued = 1201, f = fixture(effectPath, closed + queued);
	const statuses = f.arrays.get('doctrine_research_batch_statuses');
	for (let index = 0; index < closed; index++) statuses[index] = constants.get('constant:doctrine_research_batch_status.completed');
	f.saved.set('doctrine_research_queued_batches', queued);
	f.call('wake_country_batches');
	assert.equal(f.resolved.length, 0);
	assert.equal(f.saved.get('doctrine_research_queued_batches'), queued);
	assert.equal(f.events.length, 1);
	while (f.events.length) f.deliver();
	assert.deepEqual(f.resolved, Array.from({length: queued}, (_, index) => closed + index + 1));
	assert.equal(f.maxResolverDepth, 1);
});
test('quarantine schedules only the remaining country-owned queue', () => {
	const f = fixture(effectPath, 2, false); f.call('wake_country_batches'); f.ai = true;
	f.call('quarantine_active_batch_and_start_next');
	assert.equal(f.events.length, 1); assert.equal(f.resolved.length, 0);
	f.deliver(); assert.deepEqual(f.resolved, [2]);
});
test('annexation removes queued work and stale delivery grants nothing', () => {
	const f = fixture(effectPath, 3); f.call('wake_country_batches');
	f.call('discard_annexed_country_state'); f.live = false; f.deliver();
	assert.deepEqual(f.resolved, [1]); assert.equal(f.arrays.get('doctrine_research_batch_ids').length, 0);
	assert(!f.flags.has('doctrine_research_batch_wake_scheduled'));
});
console.log(JSON.stringify({model: 'actual-source country continuation with explicit native/initialization/achievement stubs', loopCeiling: 1000, callerTemporaryCleanup: true, tests, inputs: [effectPath, constantsPath, beforePath].map(file => ({file, sha256: sha(file)}))}, null, 2));
