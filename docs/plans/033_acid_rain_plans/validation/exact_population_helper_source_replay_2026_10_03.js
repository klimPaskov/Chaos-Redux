// Bounded source replay of two locked helpers, not an HOI4 execution test.
// Arithmetic primitives model exact finite-decimal fixture values/Math.round.
// This avoids a JS 1.001 * 1000 artifact and does not claim engine precision.
// Population application and
// recruitable credits are explicit fixtures, not assertions about engine behavior.
// No source file is written. Unknown effects/triggers fail instead of being mocked.
const fs = require('fs');
const assert = require('assert/strict');
const { parse, namedBlock, assignment, constants, hash } = require('./caller_repairs_source_tests_2026_10_03.js');
const path = 'common/scripted_effects/chaosx_dynamic_effects.txt';
const bytes = fs.readFileSync(path);
const sourceHash = hash(bytes);
// Record the actual current parent-owned bytes. The original 8b4db4 checkpoint
// remains immutable evidence and is not the identity of the ceil-floor repair.
const outerName = 'apply_exact_state_civilian_population_loss';
const physicalName = 'apply_state_population_loss_without_recruitable_manpower_gain';
const helperNames = [outerName, physicalName];
const sourceBodies = Object.fromEntries(helperNames.map(name => [name, namedBlock(bytes.toString('utf8'), name)]));
const actualBodies = Object.fromEntries(helperNames.map(name => [name, parse(sourceBodies[name])[0].value]));
const prefix = 'state_civilian_population_loss_';
const zero = constants.get('constant:chaos_meter_deaths.zero');
const one = constants.get('constant:chaos_meter_deaths.one');
const reason = constants.get('constant:chaos_meter_deaths_reason.acid_rain');
const unknown = constants.get('constant:chaos_meter_deaths_reason.unknown');
const outputKeys = [prefix + 'applied', prefix + 'result'];
const required = ['requested', 'minimum_remaining', 'reason', 'log_deaths', 'target_country', 'has_target_country', 'contract_supplied'].map(k => prefix + k);
const approx = (a, b, message) => assert.ok(Math.abs(a - b) < 1e-7, message + ': ' + a + ' versus ' + b);
function arithmetic(left, right, operation) {
	function decimal(x) {
		const text = String(x);
		assert.ok(!/[eE]/.test(text), 'fixture arithmetic requires finite decimal notation');
		const [whole, fraction = ''] = text.split('.');
		return { numerator: BigInt(whole + fraction), denominator: 10n ** BigInt(fraction.length) };
	}
	const a = decimal(left), b = decimal(right), denominator = a.denominator * b.denominator;
	const numerator = operation === 'multiply_temp_variable' ? a.numerator * b.numerator :
		operation === 'add_to_temp_variable' ? a.numerator * b.denominator + b.numerator * a.denominator :
		a.numerator * b.denominator - b.numerator * a.denominator;
	return Number(numerator) / Number(denominator);
}

function replay(fixture, bodies = actualBodies) {
	const owner = { type: 'COUNTRY', id: 'OWNER_A', manpower: 10000, saved: new Map([['saved_sentinel', 29]]) };
	const controller = fixture.occupied ? { type: 'COUNTRY', id: 'CONTROLLER_B', manpower: 7000, saved: new Map([['saved_sentinel', 31]]) } : owner;
	const state = { type: 'STATE', id: 'STATE_1', population: fixture.population ?? 1000, owner, controller,
		saved: new Map([[prefix + 'applied', 999], ['saved_sentinel', 33]]) };
	const flags = new Set(fixture.flags ?? []);
	const frames = [new Map()];
	const events = [], returns = [], calls = Object.fromEntries(helperNames.map(n => [n, 0]));
	const temps = () => frames.at(-1);
	const numeric = value => { assert.equal(typeof value, 'number', 'numeric primitive input'); return value; };
	function value(token, scope) {
		if (token.startsWith('var:')) token = token.slice(4);
		if (token.startsWith('constant:')) { assert.ok(constants.has(token), 'unresolved constant ' + token); return constants.get(token); }
		if (Number.isFinite(Number(token))) return Number(token);
		if (token === 'OWNER' || token === 'CONTROLLER') {
			assert.equal(scope.type, 'STATE');
			return token === 'OWNER' ? scope.owner : scope.controller;
		}
		if (token === 'state_population_k') { assert.equal(scope.type, 'STATE'); return scope.population / 1000; }
		if (token === 'manpower_k') { assert.equal(scope.type, 'COUNTRY'); return scope.manpower / 1000; }
		if (token.includes('.')) throw Error('unsupported scoped variable token: ' + token);
		return temps().has(token) ? temps().get(token) : scope.saved.get(token) ?? 0;
	}
	function compare(left, right, op) {
		switch (op) {
			case '=': case 'equals': return left === right;
			case 'not_equals': return left !== right;
			case '>': case 'greater_than': return numeric(left) > numeric(right);
			case '<': case 'less_than': return numeric(left) < numeric(right);
			case 'greater_than_or_equals': return numeric(left) >= numeric(right);
			case 'less_than_or_equals': return numeric(left) <= numeric(right);
			default: throw Error('unsupported comparison ' + op);
		}
	}
	function trigger(node, scope) {
		switch (node.key) {
			case 'OR': return node.value.some(n => trigger(n, scope));
			case 'NOT': return !node.value.some(n => trigger(n, scope));
			case 'AND': return node.value.every(n => trigger(n, scope));
			case 'has_variable': return temps().has(node.value) || scope.saved.has(node.value);
			case 'has_global_flag': return flags.has(node.value);
			case 'is_owned_and_controlled_by': {
				assert.equal(scope.type, 'STATE');
				const target = value(node.value, scope);
				return scope.owner === target && scope.controller === target;
			}
			case 'check_variable': {
				const explicit = node.value.find(n => n.key === 'var');
				if (explicit) return compare(value(explicit.value, scope), value(node.value.find(n => n.key === 'value').value, scope),
					node.value.find(n => n.key === 'compare')?.value ?? 'equals');
				const entry = node.value[0];
				return compare(value(entry.key, scope), value(entry.value, scope), entry.op);
			}
			default: throw Error('unsupported trigger ' + node.key);
		}
	}
	function helper(name, scope) {
		assert.ok(helperNames.includes(name), 'out-of-scope scripted helper ' + name);
		calls[name]++;
		const parent = temps(), inherited = new Set(parent.keys());
		frames.push(new Map(parent));
		run(bodies[name], scope);
		const child = frames.pop();
		for (const key of inherited) if (child.has(key)) parent.set(key, child.get(key));
		returns.push({ helper: name, scope: scope.type, droppedKeys: [...child.keys()].filter(k => !inherited.has(k)),
			reconciledGain: child.get('state_population_transaction_reconciled_gain') ?? 0,
			clearedTransactionLoss: child.get('state_population_transaction_loss') });
	}
	function nativeManpower(node, scope) {
		const amount = numeric(value(node.value, scope));
		if (scope.type === 'STATE') {
			assert.ok(amount < 0, 'gateway must request a negative state debit');
			const applied = fixture.nativeApplied ?? -amount;
			assert.ok(applied >= 0 && applied <= -amount && applied <= scope.population, 'invalid native fixture');
			events.push({ kind: 'native_state_debit', requested: -amount, applied, before: scope.population });
			scope.population -= applied;
			owner.manpower += fixture.ownerCredit ?? 0;
			if (controller !== owner) controller.manpower += fixture.controllerCredit ?? 0;
		} else {
			assert.equal(scope.type, 'COUNTRY');
			events.push({ kind: 'native_country_correction', country: scope.id, amount });
			scope.manpower += amount;
		}
	}
	function deathsConsumer(scope) {
		// Explicit out-of-scope consumer mock. It records the call envelope only.
		assert.equal(scope.type, 'STATE');
		assert.equal(temps().get('chaos_deaths_apply_state_pop'), 0, 'record-only apply_state_pop');
		assert.equal(temps().get('chaos_deaths_record_state_ledger'), 1, 'record-only state ledger');
		assert.equal(temps().get('chaos_deaths_is_civilian'), 1);
		events.push({ kind: 'deaths_consumer', amount: temps().get('chaos_deaths_change'), reason: temps().get('chaos_deaths_reason'),
			target: temps().get('chaos_deaths_target_country').id, hasTarget: temps().get('chaos_deaths_has_target_country'),
			populationAtCall: scope.population, applyStatePop: temps().get('chaos_deaths_apply_state_pop'),
			recordStateLedger: temps().get('chaos_deaths_record_state_ledger') });
	}
	function run(nodes, scope) {
		for (let i = 0; i < nodes.length; i++) {
			const node = nodes[i];
			if (node.key === 'if') {
				let matched = false, j = i;
				do {
					const branch = nodes[j], limit = branch.value.find(n => n.key === 'limit');
					if (!matched && (branch.key === 'else' || limit.value.every(n => trigger(n, scope)))) {
						run(branch.value.filter(n => n.key !== 'limit'), scope);
						matched = true;
					}
					j++;
				} while (j < nodes.length && ['else_if', 'else'].includes(nodes[j].key));
				i = j - 1;
				continue;
			}
			if (node.key === 'OWNER' || node.key === 'CONTROLLER') { run(node.value, value(node.key, scope)); continue; }
			if (helperNames.includes(node.key)) { assert.equal(node.value, 'yes'); helper(node.key, scope); continue; }
			if (node.key === 'chaos_meter_register_deaths') { assert.equal(node.value, 'yes'); deathsConsumer(scope); continue; }
			if (node.key === 'add_manpower') { nativeManpower(node, scope); continue; }
			if (node.key === 'round_temp_variable') { temps().set(node.value, Math.round(numeric(value(node.value, scope)))); continue; }
			if (node.key === 'clamp_temp_variable') {
				const key = node.value.find(n => n.key === 'var').value;
				let amount = numeric(value(key, scope));
				for (const entry of node.value.filter(n => n.key !== 'var')) {
					assert.ok(['min', 'max'].includes(entry.key));
					amount = entry.key === 'min' ? Math.max(amount, numeric(value(entry.value, scope))) : Math.min(amount, numeric(value(entry.value, scope)));
				}
				temps().set(key, amount);
				continue;
			}
			assert.ok(['set_temp_variable', 'multiply_temp_variable', 'add_to_temp_variable', 'subtract_from_temp_variable'].includes(node.key),
				'unsupported effect ' + node.key);
			const [key, token] = assignment(node), right = value(token, scope);
			if (node.key === 'set_temp_variable') temps().set(key, right);
			else {
				const left = numeric(value(key, scope));
				temps().set(key, arithmetic(left, numeric(right), node.key));
			}
		}
	}
	const initialPopulation = state.population;
	const initialSaved = [state, owner, controller].map(s => [...s.saved]);
	const input = { requested: fixture.requested ?? 100, minimum_remaining: fixture.floor ?? 100, reason,
		log_deaths: fixture.log ?? one, target_country: fixture.targetController ? controller : owner,
		has_target_country: one, contract_supplied: fixture.proof ?? one };
	for (const [key, v] of Object.entries(input)) temps().set(prefix + key, v);
	if (fixture.missing) temps().delete(prefix + fixture.missing);
	if (fixture.ambientFloor) temps().set(prefix + 'minimum_remaining', zero);
	if (fixture.predeclare !== false) { temps().set(outputKeys[0], 888); temps().set(outputKeys[1], one); }
	temps().set('caller_cursor', 37);
	const callerKeys = [...temps().keys()];
	helper(outerName, state);
	assert.deepEqual([...temps().keys()], callerKeys, 'private helper temporaries leaked');
	assert.equal(temps().get('caller_cursor'), 37);
	assert.deepEqual([state, owner, controller].map(s => [...s.saved]), initialSaved, 'saved scopes were conflated with temporary storage');
	return { state, owner, controller, temps: temps(), events, returns, calls, initialPopulation };
}

function validate(fixture, model) {
	const observed = model.initialPopulation - model.state.population;
	if (fixture.strictFloor !== undefined)
		assert.ok(model.state.population >= Math.min(model.initialPopulation, fixture.strictFloor), 'crossed supplied fractional minimum');
	approx(observed, fixture.expectedApplied, 'native fixture observed delta');
	if (fixture.predeclare !== false) {
		approx(model.temps.get(outputKeys[0]), observed, 'observed output');
		assert.equal(model.temps.get(outputKeys[1]), observed > 0 ? 1 : 0, 'result follows observed loss');
	} else assert.equal(model.temps.has(outputKeys[0]), false, 'cold caller output must expire at return');
	const physical = model.events.filter(e => e.kind === 'native_state_debit');
	assert.equal(physical.length, fixture.expectedPhysical ?? 1, 'one physical loss primitive');
	assert.equal(model.calls[physicalName], fixture.expectedPhysical ?? 1, 'physical helper source invocation count');
	if (physical.length) approx(physical[0].requested, fixture.expectedRequest ?? fixture.requested ?? 100, 'clamped native request');
	const records = model.events.filter(e => e.kind === 'deaths_consumer');
	assert.equal(records.length, fixture.expectedRecords ?? (observed > 0 ? 1 : 0));
	if (records.length) {
		approx(records[0].amount, observed, 'Deaths payload is observed loss');
		assert.equal(records[0].reason, reason);
		assert.equal(records[0].target, fixture.targetController ? model.controller.id : model.owner.id);
		approx(records[0].populationAtCall, model.state.population, 'record cannot apply another population debit');
		assert.ok(model.events.findIndex(e => e.kind === 'deaths_consumer') > model.events.findIndex(e => e.kind === 'native_state_debit'));
	}
	approx(model.owner.manpower, 10000, 'owner manpower reconciliation');
	if (model.controller !== model.owner) approx(model.controller.manpower, 7000, 'controller manpower reconciliation');
	for (const key of required.filter(k => model.temps.has(k))) {
		if (key === prefix + 'reason') assert.equal(model.temps.get(key), unknown);
		else if (key === prefix + 'target_country') assert.equal(model.temps.get(key), model.owner);
		else assert.equal(model.temps.get(key), zero, 'one-shot input cleanup ' + key);
	}
	if (physical.length) {
		const returned = model.returns.find(r => r.helper === physicalName);
		approx(returned.reconciledGain, (fixture.ownerCredit ?? 0) + (fixture.occupied ? fixture.controllerCredit ?? 0 : 0), 'nested physical output storage');
		assert.equal(returned.clearedTransactionLoss, 0);
	}
}

const fixtures = [
	{ id: 'positive_owner', expectedApplied: 100, ownerCredit: 20 },
	{ id: 'native_zero_application', expectedApplied: 0, nativeApplied: 0 },
	{ id: 'partial_owner_controller', expectedApplied: 41, nativeApplied: 41, occupied: true, ownerCredit: 10, controllerCredit: 7, targetController: true },
	{ id: 'positive_owner_controller', expectedApplied: 100, occupied: true, ownerCredit: 20, controllerCredit: 11, targetController: true },
	{ id: 'zero_application_owner_controller', expectedApplied: 0, nativeApplied: 0, occupied: true },
	{ id: 'floor_limited', population: 1000, requested: 500, floor: 900, expectedRequest: 100, expectedApplied: 100 },
	{ id: 'at_floor', population: 300, floor: 300, expectedApplied: 0, expectedPhysical: 0 },
	{ id: 'floor_above_population', floor: 1500, expectedApplied: 0, expectedPhysical: 0 },
	{ id: 'availability_250_5', population: 1250.5, floor: 1000, requested: 251, expectedRequest: 250, expectedApplied: 250, strictFloor: 1000 },
	{ id: 'large_regular_people_variable', population: 4000000, floor: 1000, expectedApplied: 100 },
	{ id: 'fractional_availability_floor', population: 1000.75, floor: 1000, requested: 1, expectedApplied: 0, expectedPhysical: 0 },
	{ id: 'fractional_availability_whole_debit', population: 1000.75, floor: 0, requested: 1001, expectedRequest: 1000, expectedApplied: 1000 },
	{ id: 'rounded_request', requested: 10.6, expectedRequest: 11, expectedApplied: 11 },
	{ id: 'negative_request', requested: -10, expectedApplied: 0, expectedPhysical: 0 },
	{ id: 'zero_request', requested: 0, expectedApplied: 0, expectedPhysical: 0 },
	{ id: 'zero_proof', proof: 0, expectedApplied: 0, expectedPhysical: 0 },
	{ id: 'log_zero', log: 0, expectedApplied: 100, expectedRecords: 0 },
	{ id: 'logging_disabled', flags: ['settings_chaos_deaths_disabled'], expectedApplied: 100, expectedRecords: 0 },
	{ id: 'cold_output_negative_control', predeclare: false, expectedApplied: 100 },
	{ id: 'cold_missing_floor', missing: 'minimum_remaining', expectedApplied: 0, expectedPhysical: 0 },
	{ id: 'ambient_zero_floor_gap', missing: 'minimum_remaining', ambientFloor: true, expectedApplied: 100, policyResolved: false }
];
for (const floor of [1000.1, 1000.5, 1000.9]) {
	for (const occupied of [false, true]) {
		fixtures.push({ id: 'strict_fractional_floor_' + floor + (occupied ? '_occupied' : '_owner'),
			population: 1001, requested: 1, floor, strictFloor: floor, occupied,
			expectedApplied: 0, expectedPhysical: 0 });
	}
}
for (const name of ['fallout_air_cleanliness_disabled', 'fallout_transition_active', 'fallout_active',
	'fallout_manual_scenario_active', 'fallout_manual_sweep_active', 'fallout_manual_countdown_active']) {
	fixtures.push({ id: 'disabled_logging_override_' + name, flags: ['settings_chaos_deaths_disabled', name], expectedApplied: 100 });
}
fixtures.push({ id: 'override_retains_caller_log_zero', log: 0, flags: ['settings_chaos_deaths_disabled', 'fallout_active'], expectedApplied: 100, expectedRecords: 0 });
for (const key of ['requested', 'reason', 'log_deaths', 'target_country', 'has_target_country', 'contract_supplied'])
	fixtures.push({ id: 'missing_' + key, missing: key, expectedApplied: 0, expectedPhysical: 0 });
const results = fixtures.map(f => {
	const m = replay(f); validate(f, m);
	return { id: f.id, status: 'passed', policyResolved: f.policyResolved, applied: m.initialPopulation - m.state.population,
		physicalCalls: m.calls[physicalName], events: m.events, perHelperCleanup: m.returns.map(r => ({
			helper: r.helper, scope: r.scope, droppedKeyCount: r.droppedKeys.length,
			droppedPublicOutputs: r.droppedKeys.filter(k => outputKeys.includes(k)),
			reconciledGain: r.reconciledGain, clearedTransactionLoss: r.clearedTransactionLoss
		})) };
});

// Mutated ASTs exist only in memory and must be rejected by the substantive checks.
function walk(nodes, fn) { for (const n of nodes) { fn(n); if (Array.isArray(n.value)) walk(n.value, fn); } }
const badRecord = structuredClone(actualBodies);
walk(badRecord[outerName], n => {
	if (n.key === 'set_temp_variable' && assignment(n)[0] === 'chaos_deaths_apply_state_pop') n.value[0].value = 'constant:chaos_meter_deaths.one';
});
assert.throws(() => replay(fixtures[0], badRecord), /record-only/);
const badReadback = structuredClone(actualBodies);
function removeObservedSubtraction(nodes) {
	return nodes.filter(n => !(n.key === 'subtract_from_temp_variable' && assignment(n)[0] === outputKeys[0]))
		.map(n => ({ ...n, value: Array.isArray(n.value) ? removeObservedSubtraction(n.value) : n.value }));
}
badReadback[outerName] = removeObservedSubtraction(badReadback[outerName]);
assert.throws(() => validate(fixtures[2], replay(fixtures[2], badReadback)), /observed output/);
const badController = structuredClone(actualBodies);
walk(badController[physicalName], n => { if (n.key === 'CONTROLLER') n.key = 'OWNER'; });
assert.throws(() => validate(fixtures[2], replay(fixtures[2], badController)), /controller manpower reconciliation/);
const badCeil = structuredClone(actualBodies);
badCeil[outerName] = badCeil[outerName].filter(n => !(n.key === 'if' && JSON.stringify(n.value)
	.includes('state_civilian_population_loss_minimum_unrounded')));
const fractionalCase = fixtures.find(f => f.id === 'strict_fractional_floor_1000.1_owner');
assert.throws(() => validate(fractionalCase, replay(fractionalCase, badCeil)), /crossed supplied fractional minimum/);

process.stdout.write(JSON.stringify({ evidenceKind: 'actual_source_replay_with_native_mocks', sourceHash,
	helperBodies: helperNames.map(name => ({ name, sha256: hash(sourceBodies[name]) })),
	mockedBoundary: ['native arithmetic and variable/flag predicates', 'native state/country add_manpower',
		'native state_population_k/manpower_k getters', 'out-of-scope chaos_meter_register_deaths call-envelope recorder'],
	scriptedHelperBodiesMocked: [], unknownCommands: 'fail_closed',
	limits: ['finite-decimal arithmetic/JS rounding model is not native fixed-point proof', 'population applied and recruitable credit are declared native fixtures',
		'Deaths consumer body, ledgers, history, and Chaos progression are not executed', 'no HOI4 execution or save persistence evidence'],
	negativeControls: ['missing caller output storage', 'record-only flag mutation', 'observed readback subtraction removed',
		'controller scope replaced with owner', 'minimum ceil correction removed'],
	results }, null, 2) + '\n');
