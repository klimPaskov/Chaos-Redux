// Source-only caller-boundary replay. Native population execution is not tested.
// Run from the repository root with Node.js. This test writes no files.
const fs = require('fs');
const crypto = require('crypto');
const assert = require('assert/strict');
const dir = 'docs/plans/033_acid_rain_plans/validation/';
const evidence = JSON.parse(fs.readFileSync(dir + 'caller_repairs_2026_10_03_evidence.json', 'utf8'));
const before = JSON.parse(fs.readFileSync(dir + 'caller_repairs_2026_10_03_before_blocks.json', 'utf8'));
const hash = value => crypto.createHash('sha256').update(value).digest('hex');
const gateway = 'apply_exact_state_civilian_population_loss';
const prefix = 'state_civilian_population_loss_';
const outputNames = [prefix + 'applied', prefix + 'result'];
const results = [];
const record = (name, details) => results.push({ name, status: 'passed', ...details });

function parse(text) {
	const tokens = text.replace(/#[^\r\n]*/g, '').match(/"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>]+/g) || [];
	let i = 0;
	function body(nested = false) {
		const nodes = [];
		while (i < tokens.length && tokens[i] !== '}') {
			const key = tokens[i++];
			if (key === '{') {
				nodes.push({ key: '__anonymous', op: '=', value: body(true) });
				continue;
			}
			if (!['=', '<', '>'].includes(tokens[i])) {
				nodes.push({ key: '__atom', op: '=', value: key });
				continue;
			}
			const op = tokens[i++];
			let value = tokens[i++];
			if (value === '{') value = body(true);
			nodes.push({ key, op, value });
		}
		if (nested) assert.equal(tokens[i++], '}');
		return nodes;
	}
	return body();
}

function namedBlock(text, name) {
	const found = new RegExp('^' + name + '\\s*=\\s*\\{', 'm').exec(text);
	assert.ok(found, 'missing named block ' + name);
	let depth = 0, quoted = false, comment = false;
	for (let i = found.index + found[0].indexOf('{'); i < text.length; i++) {
		const c = text[i];
		if (c === '\n') comment = false;
		if (comment) continue;
		if (!quoted && c === '#') { comment = true; continue; }
		if (c === '"' && text[i - 1] !== '\\') { quoted = !quoted; continue; }
		if (quoted) continue;
		if (c === '{') depth++;
		if (c === '}' && --depth === 0) return text.slice(found.index, i + 1);
	}
	throw Error('unclosed block ' + name);
}

function findCall(nodes) {
	for (let i = 0; i < nodes.length; i++) {
		if (nodes[i].key === gateway) return { nodes, index: i };
		if (Array.isArray(nodes[i].value)) {
			const found = findCall(nodes[i].value);
			if (found) return found;
		}
	}
}

const constants = new Map();
for (const filename of ['chaos_meter_constants.txt', 'humanitarian_runtime_constants.txt']) {
	for (const category of parse(fs.readFileSync('common/script_constants/' + filename, 'utf8'))) {
		if (!Array.isArray(category.value)) continue;
		for (const entry of category.value) {
			if (!Array.isArray(entry.value) && Number.isFinite(Number(entry.value)))
				constants.set('constant:' + category.key + '.' + entry.key, Number(entry.value));
		}
	}
}

// Temporaries and saved variables intentionally use different storage.
function read(token, temps, saved = new Map()) {
	if (token.startsWith('var:')) token = token.slice(4);
	if (token.startsWith('constant:')) {
		assert.ok(constants.has(token), 'unresolved test constant ' + token);
		return constants.get(token);
	}
	if (Number.isFinite(Number(token))) return Number(token);
	if (token.includes('.')) return saved.get(token) ?? 0;
	return temps.get(token) ?? saved.get(token) ?? 0;
}

function assignment(node) {
	assert.ok(Array.isArray(node.value));
	const explicit = node.value.find(n => n.key === 'var');
	return explicit ? [explicit.value, node.value.find(n => n.key === 'value').value]
		: [node.value[0].key, node.value[0].value];
}

function declarations(call, temps) {
	for (const n of call.nodes.slice(0, call.index)) {
		if (n.key !== 'set_temp_variable') continue;
		const [key, value] = assignment(n);
		if (outputNames.includes(key)) temps.set(key, read(value, temps));
	}
}

// The native transaction is stubbed with an explicit observed receipt.
// Frame cleanup drops helper-created temporaries and retains caller-owned keys.
function returnObserved(temps, observed) {
	const callerKeys = new Set(temps.keys());
	const frame = new Map(temps);
	frame.set(outputNames[0], observed);
	frame.set(outputNames[1], observed > 0 ? 1 : 0);
	frame.set('helper_private_scratch', 12345);
	frame.set(prefix + 'reason', constants.get('constant:chaos_meter_deaths_reason.unknown'));
	for (const key of callerKeys) if (frame.has(key)) temps.set(key, frame.get(key));
	assert.equal(temps.has('helper_private_scratch'), false);
}

function receiptReads(nodes) {
	const reads = [];
	for (const n of nodes) {
		if (/^(set|add_to|subtract_from)_(temp_)?variable$/.test(n.key)) {
			const pair = assignment(n);
			if (pair[1] === outputNames[0]) reads.push(pair);
		}
		if (Array.isArray(n.value)) reads.push(...receiptReads(n.value));
	}
	return reads;
}

function runCallerChecks(refreshPath) {
results.length = 0;
const refresh = refreshPath ? JSON.parse(fs.readFileSync(refreshPath, 'utf8')) : null;
if (refresh) {
	assert.equal(refresh.schema, 1);
	for (const immutable of refresh.immutableEvidence)
		assert.equal(hash(fs.readFileSync(immutable.path)), immutable.sha256, 'immutable evidence changed');
}
const currentBlocks = new Map();
for (const file of before.files) {
	const current = fs.readFileSync(file.path, 'utf8');
	const freshFile = refresh?.files.find(f => f.path === file.path);
	if (refresh) {
		assert.ok(freshFile, 'missing refreshed file identity');
		assert.equal(hash(fs.readFileSync(file.path)), freshFile.sha256, 'unreviewed file drift: ' + file.path);
	}
	let reversed = current;
	for (const oldBlock of file.blocks) {
		assert.equal(hash(oldBlock.text), oldBlock.sha256, 'before block evidence hash');
		let expected = oldBlock.text;
		for (const change of evidence.changes.filter(c => c.path === file.path && c.block === oldBlock.name)) {
			assert.ok(expected.includes(change.before), 'owned before hunk missing');
			expected = expected.split(change.before).join(change.after);
		}
		let reviewedBase = oldBlock.text;
		for (const change of refresh?.reviewedNamedBlockChanges.filter(c => c.path === file.path && c.block === oldBlock.name) ?? []) {
			assert.equal(expected.split(change.before).length - 1, 1, 'reviewed drift anchor must be unique');
			expected = expected.replace(change.before, change.after);
			reviewedBase = reviewedBase.replace(change.before, change.after);
		}
		const actual = namedBlock(current, oldBlock.name);
		assert.equal(actual, expected, 'unexpected edit in ' + oldBlock.name);
		if (refresh) assert.equal(hash(actual), freshFile.blocks.find(b => b.name === oldBlock.name).sha256);
		currentBlocks.set(oldBlock.name, actual);
		reversed = reversed.replace(actual, reviewedBase);
	}
	assert.equal(hash(reversed), refresh ? freshFile.withoutOwnedHunksSha256 : file.sha256,
		'byte identity outside owned hunks changed: ' + file.path);
}
record(refresh ? 'refreshed_owned_hunk_identity' : 'owned_hunk_byte_reversal', {
	files: before.files.length, namedBlocks: currentBlocks.size,
	historicalWholeFileIdentityClaim: !refresh,
	reviewedCurrentCallerTextUsed: true
});
const currentParentHash = hash(fs.readFileSync('common/scripted_effects/chaosx_dynamic_effects.txt'));
assert.equal(currentParentHash, refresh ? refresh.helperSourceSha256 : evidence.parentGatewaySha256);
record(refresh ? 'parent_gateway_refresh_identity' : 'parent_gateway_unchanged', { sha256: currentParentHash });

const storage = evidence.changes.filter(c => c.kind === 'caller_output_storage');
assert.equal(storage.length, 12);
for (const change of storage) {
	const call = findCall(parse(currentBlocks.get(change.block)));
	const old = before.files.find(f => f.path === change.path).blocks.find(b => b.name === change.block);
	const oldCall = findCall(parse(old.text));
	assert.ok(call && oldCall);
	const reads = receiptReads(call.nodes.slice(call.index + 1));
	assert.ok(reads.length, change.block + ' must have an actual-source receipt consumer');
	const cold = new Map([['cursor', 29], [prefix + 'requested', 501]]);
	declarations(call, cold);
	assert.equal(cold.get('cursor'), 29);
	assert.equal(cold.get(prefix + 'requested'), 501);
	assert.deepEqual(outputNames.map(k => cold.get(k)), [0, 0]);
	for (const observed of [0, 17, 101, 0]) {
		declarations(call, cold);
		returnObserved(cold, observed);
		assert.deepEqual(outputNames.map(k => cold.get(k)), [observed, observed > 0 ? 1 : 0]);
		for (const [, token] of reads) assert.equal(read(token, cold), observed);
	}
	const stale = new Map([[outputNames[0], 888], [outputNames[1], 1]]);
	declarations(call, stale);
	returnObserved(stale, 0);
	assert.deepEqual(outputNames.map(k => stale.get(k)), [0, 0]);
	const negative = new Map();
	declarations(oldCall, negative);
	returnObserved(negative, 17);
	assert.equal(negative.has(outputNames[0]), false, 'before source must expose storage regression');
	assert.equal(read(reads[0][1], negative), 0);
}
record('caller_storage_replay', { callers: 12, observedSequence: [0, 17, 101, 0], beforeNegativeControls: 12 });

const floorCall = findCall(parse(currentBlocks.get('famine_apply_related_state_deaths_exact')));
const floorKey = prefix + 'minimum_remaining';
const directFloor = floorCall.nodes.slice(0, floorCall.index).filter(n => n.key === 'set_temp_variable' && assignment(n)[0] === floorKey);
assert.equal(directFloor.length, 1);
assert.equal(assignment(directFloor[0])[1], 'humanitarian_related_deaths_minimum_remaining');
const floorCases = [];
for (const supplied of [0, 300, 1000, 1500, -10]) {
	for (const ambient of [undefined, 0, 777]) {
		const temps = new Map([['humanitarian_related_deaths_minimum_remaining', supplied]]);
		if (ambient !== undefined) temps.set(floorKey, ambient);
		const [key, value] = assignment(directFloor[0]);
		temps.set(key, read(value, temps));
		assert.equal(temps.get(floorKey), supplied);
		// Mathematical contract boundary only, not an executed native debit.
		const modeled = Math.min(900, Math.max(0, Math.floor(1000 - Math.max(0, Math.round(temps.get(floorKey))))));
		assert.ok(1000 - modeled >= Math.min(1000, Math.max(0, Math.round(supplied))));
		floorCases.push({ supplied, ambient: ambient ?? 'missing', modeledApplied: modeled });
	}
}
record('famine_floor_boundary', { cases: floorCases.length, details: floorCases });

const migration = findCall(parse(currentBlocks.get('migration_apply_related_state_deaths_exact')));
assert.equal(migration.nodes.slice(0, migration.index).some(n => n.key === 'set_temp_variable' && assignment(n)[0] === floorKey), false);
const gatewayAst = parse(fs.readFileSync('common/scripted_effects/chaosx_dynamic_effects.txt', 'utf8')).find(n => n.key === gateway).value;
const contractGuard = gatewayAst.find(n => n.key === 'if').value.find(n => n.key === 'limit').value;
function requiredVariables(nodes) {
	return nodes.flatMap(n => n.key === 'has_variable' ? [n.value] : Array.isArray(n.value) ? requiredVariables(n.value) : []);
}
const required = [...new Set(requiredVariables(contractGuard))];
assert.equal(required.length, 7);
assert.ok(required.includes(floorKey));
const inputCoverage = storage.map(change => {
	const call = findCall(parse(currentBlocks.get(change.block)));
	const fields = new Map(call.nodes.slice(0, call.index)
		.filter(n => n.key === 'set_temp_variable')
		.map(assignment).filter(([key]) => required.includes(key)));
	const missingFields = required.filter(key => !fields.has(key));
	assert.deepEqual(missingFields, change.block === 'migration_apply_related_state_deaths_exact' ? [floorKey] : []);
	return { caller: change.block, freshlyAssignedInputCount: fields.size, missingFields };
});
record('seven_field_caller_input_coverage', { completeCallers: 11, queuedFloorCaller: 1, details: inputCoverage });
const missing = new Map(required.filter(k => k !== floorKey).map(k => [k, 1]));
assert.equal(required.every(k => missing.has(k)), false);
const ambientZero = new Map(missing);
ambientZero.set(floorKey, 0);
assert.equal(required.every(k => ambientZero.has(k)), true);
record('migration_floor_policy_gap', {
	requiredInputs: required.length,
	coldMissingFloorFailsExistenceGuard: true,
	ambientZeroPassesExistenceGuard: true,
	policyResolved: false,
	status: 'queued_owner_policy'
});

let unscopedSites = 0;
for (const change of evidence.changes.filter(c => c.kind.startsWith('unscoped_temporary'))) {
	const block = currentBlocks.get(change.block);
	assert.equal(block.includes(change.before), false);
	const old = before.files.find(f => f.path === change.path).blocks.find(b => b.name === change.block).text;
	const oldLines = old.split(/\r?\n/).filter(l => l.includes(change.before));
	for (const oldLine of oldLines) {
		const afterLine = oldLine.split(change.before).join(change.after);
		assert.ok(block.includes(afterLine));
		const oldNode = parse(oldLine)[0];
		const newNode = parse(afterLine)[0];
		function valueToken(n) {
			if (n.key === 'add_manpower') return n.value;
			if (['set_variable', 'set_temp_variable'].includes(n.key)) return assignment(n)[1];
			if (Array.isArray(n.value)) {
				for (const child of n.value) { const value = valueToken(child); if (value) return value; }
			}
		}
		const token = valueToken(newNode).replace(/^var:/, '');
		const temps = new Map([[token, 80]]);
		const saved = new Map([['ROOT.' + token, 999]]);
		assert.equal(read(valueToken(newNode), temps, saved), 80);
		assert.equal(read(valueToken(oldNode), temps, saved), 999);
		unscopedSites++;
	}
}
assert.equal(unscopedSites, 5);
record('unscoped_temporary_reads_and_credits', { sites: unscopedSites, savedRootSentinel: 999, actualTemporary: 80 });

for (const change of evidence.changes.filter(c => c.kind === 'caller_known_cause')) {
	const nodes = parse(currentBlocks.get(change.block));
	function findCause(ns) {
		for (const n of ns) {
			if (n.key === 'set_temp_variable' && assignment(n)[0] === 'famine_adapter_cause_proven') return assignment(n)[1];
			if (Array.isArray(n.value)) { const v = findCause(n.value); if (v) return v; }
		}
	}
	const cause = findCause(nodes);
	const temps = new Map([[prefix + 'reason', constants.get('constant:chaos_meter_deaths_reason.unknown')]]);
	assert.notEqual(read(cause, temps), read(prefix + 'reason', temps));
	assert.equal(cause, change.after.split(' = ')[1]);
}
record('cause_proof_after_input_cleanup', { callers: 2 });

let census = 0;
for (const filename of fs.readdirSync('common/scripted_effects')) {
	if (!filename.endsWith('.txt')) continue;
	census += (fs.readFileSync('common/scripted_effects/' + filename, 'utf8').match(/^\s*apply_exact_state_civilian_population_loss\s*=\s*yes\s*$/gm) || []).length;
}
assert.equal(census, 213);
record('exact_caller_census', { calls: census });
process.stdout.write(JSON.stringify({ evidenceKind: 'source_only', nativeTransaction: 'stubbed', results }, null, 2) + '\n');
return results;
}

module.exports = { parse, namedBlock, assignment, constants, hash, runCallerChecks };
if (require.main === module) {
	const index = process.argv.indexOf('--refresh');
	if (index !== -1) assert.ok(process.argv[index + 1], '--refresh needs a reviewed journal path');
	runCallerChecks(index === -1 ? null : process.argv[index + 1]);
}
