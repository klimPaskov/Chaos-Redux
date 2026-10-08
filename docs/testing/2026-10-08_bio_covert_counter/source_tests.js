// Bounded source evidence. Reuses the unchanged existing parser and fixed-point VM.
// Run from mod root: node docs/testing/2026-10-08_bio_covert_counter/source_tests.js --capture
// Subsequent archived replay: node docs/testing/2026-10-08_bio_covert_counter/source_tests.js
// The dispatch projection executes actual source predicates and actual recorder call placement.
// It omits unrelated seed/profile/storage effects and cannot prove native callback cardinality.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const shared = require('../../plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
const { VM: BaseVM, parse, ticks, S, root, definitions, constants } = shared;
const owned = 'common/scripted_effects/cbrn_achievement_effects.txt';
const dependencyPaths = [
  'common/scripted_effects/biological_lifecycle_effects.txt',
  'common/scripted_triggers/biological_lifecycle_triggers.txt',
  'common/scripted_triggers/cbrn_achievement_triggers.txt',
  'common/script_constants/biological_lifecycle_constants.txt',
  'common/script_constants/cbrn_achievement_constants.txt',
  'common/script_constants/cbrn_system_constants.txt',
  'common/script_constants/cbrn_chemical_delivery_constants.txt',
];
const digest = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
if (process.argv.includes('--capture')) {
  for (const rel of [owned, ...dependencyPaths]) {
    const dest = path.join(__dirname, 'after', rel);
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.copyFileSync(path.join(root, rel), dest);
  }
}
const receipts = {};
function read(rel, side = 'after') {
  const bytes = fs.readFileSync(path.join(__dirname, side, rel));
  receipts[`${side}/${rel}`] = digest(bytes);
  const source = bytes.toString('utf8');
  if (rel.includes('/script_constants/')) {
    // Complex anonymous schema declarations elsewhere are outside the existing parser.
    // Extract only exact, column-zero named categories required by this test.
    const categories = ['bio_lifecycle_math', 'bio_lifecycle_agent', 'bio_lifecycle_route',
      'bio_lifecycle_source', 'bio_lifecycle_result', 'bio_lifecycle_proof',
      'cbrn_achievement_value', 'cbrn_achievement_threshold', 'cbrn_delivery_route', 'cbrn_chemical_raid_result'];
    const selected = [...source.matchAll(/^(\w+) = \{\r?\n[\s\S]*?^\}/gm)].filter(m => categories.includes(m[1]));
    assert(selected.length > 0, rel);
    return selected.flatMap(m => parse(m[0]));
  }
  return parse(source);
}
for (const rel of dependencyPaths.filter(p => p.includes('/script_constants/'))) {
  for (const category of read(rel)) if (Array.isArray(category.value)) {
    for (const item of category.value) if (!Array.isArray(item.value) && /^-?\d+(\.\d+)?$/.test(item.value)) {
      constants.set(`constant:${category.key}.${item.key}`, ticks(item.value));
    }
  }
}
for (const rel of dependencyPaths.filter(p => p.includes('/scripted_triggers/'))) {
  for (const node of read(rel)) definitions.set(node.key, node.value);
}
const beforeNodes = read(owned, 'before');
const afterNodes = read(owned);
const lifecycle = read(dependencyPaths[0]);
const field = (nodes, key) => nodes.find(n => n.key === key)?.value;
const body = (nodes, key) => { const value = field(nodes, key); assert(Array.isArray(value), key); return value; };
const walk = (nodes, key) => nodes.flatMap(n => [ ...(n.key === key ? [n] : []), ...(Array.isArray(n.value) ? walk(n.value, key) : []) ]);
const bioName = 'cbrn_achievement_record_biological_operation';
const strategic = 'cbrn_achievement_covert_strategic_result_history';
// Check only executed definitions, so the parent's unrelated capture-helper removal is tolerated.
const dispatch = body(lifecycle, 'bio_lifecycle_dispatch_seed');
const accepted = dispatch.filter(n => n.key === 'if' && JSON.stringify(field(n.value, 'limit')).includes('bio_lifecycle_seed_record_is_valid'));
assert.equal(accepted.length, 1);
const history = accepted[0].value.filter(n => n.key === 'if' && walk(n.value, 'bio_lifecycle_record_internal_deliberate_use').length);
assert.equal(history.length, 1);
assert.equal(walk(dispatch, 'bio_lifecycle_record_internal_deliberate_use').length, 1);
const deliberate = body(lifecycle, 'bio_lifecycle_record_internal_deliberate_use');
const actorBlocks = deliberate.filter(n => n.key === 'event_target:bio_seed_actor' && walk(n.value, bioName).length);
assert.equal(actorBlocks.length, 1);
assert.equal(walk(deliberate, bioName).length, 1);
const realRecorderCall = actorBlocks[0].value.find(n => n.key === bioName);
assert.equal(realRecorderCall.value, 'yes');
// Source-preserving projection: full actual limits, only the relevant body call.
const gateProjection = [{ key: 'if', op: '=', value: [
  accepted[0].value.find(n => n.key === 'limit'),
  { key: 'if', op: '=', value: [history[0].value.find(n => n.key === 'limit'),
    { key: 'event_target:bio_seed_actor', op: '=', value: [realRecorderCall] }] },
] }];
definitions.set('fixture_source_gate_projection', gateProjection);

// Local adapters add only the missing receipt commands and declared typed context.
// Boolean/control flow and variable comparisons remain the existing BaseVM implementation.
const extended = new Set(['has_country_flag', 'set_country_flag', 'add_to_variable', 'has_event_target',
  'CONTROLLER', 'tag', 'exists', 'is_ai', 'has_capitulated', 'is_zombie_controlled_state',
  'has_state_category', 'state_population_k', 'event_target:bio_seed_actor']);
class ReceiptContext extends BaseVM {
  constructor() {
    super(); this.identity = 'state:fixture'; this.controller = 'country:victim';
    this.targets = new Map([['bio_seed_actor', 'country:actor'], ['bio_seed_victim', 'country:victim']]);
    this.actorFlags = new Set(); this.ai = false; this.capitulated = false;
    this.zombie = false; this.wasteland = false; this.populationK = ticks(100);
  }
  countryIdentity() { assert(this.identity.startsWith('country:'), `country command in ${this.identity}`); }
  eval(nodes) {
    for (let i = 0; i < nodes.length;) {
      const n = nodes[i];
      if (!extended.has(n.key)) {
        let end = i + 1;
        while (end < nodes.length && !extended.has(nodes[end].key)) end++;
        if (!super.eval(nodes.slice(i, end))) return false;
        i = end; continue;
      }
      this.ops++; i++;
      const { key: k, value: v, op } = n;
      if (k === 'has_country_flag') { this.countryIdentity(); if (!this.actorFlags.has(v)) return false; }
      else if (k === 'set_country_flag') { this.countryIdentity(); this.actorFlags.add(v); }
      else if (k === 'add_to_variable') {
        const name = field(v, 'var') || v[0].key;
        this.write(name, this.value(name) + this.value(field(v, 'value') || v[0].value), false);
      } else if (k === 'has_event_target') { if (!this.targets.has(v)) return false; }
      else if (k === 'CONTROLLER' || k === 'event_target:bio_seed_actor') {
        const previous = this.identity;
        this.identity = k === 'CONTROLLER' ? this.controller : this.targets.get('bio_seed_actor');
        try { if (!this.identity || !this.eval(v)) return false; } finally { this.identity = previous; }
      } else if (k === 'tag') { if (this.identity !== this.targets.get(v.replace('event_target:', ''))) return false; }
      else if (k === 'exists') { if ((v === 'yes') !== Boolean(this.identity)) return false; }
      else if (k === 'is_ai') { if ((v === 'yes') !== this.ai) return false; }
      else if (k === 'has_capitulated') { if ((v === 'yes') !== this.capitulated) return false; }
      else if (k === 'is_zombie_controlled_state') { if ((v === 'yes') !== this.zombie) return false; }
      else if (k === 'has_state_category') { assert.equal(v, 'wasteland'); if (!this.wasteland) return false; }
      else if (k === 'state_population_k') { assert.equal(op, '>'); if (!(this.populationK > this.value(v))) return false; }
    }
    return true;
  }
}
const token = (category, key) => constants.get(`constant:${category}.${key}`);
function seedFixture(route = 'food_water_medical_sabotage', result = 'partial') {
  const vm = new ReceiptContext();
  for (const [name, value] of Object.entries({
    bio_seed_route: token('bio_lifecycle_route', route), bio_seed_result: token('bio_lifecycle_result', result),
    bio_seed_agent: token('bio_lifecycle_agent', 'anthrax'), bio_seed_source: token('bio_lifecycle_source', 'deliberate'),
    bio_seed_actor_proof: token('bio_lifecycle_proof', 'supplied'), bio_seed_victim_proof: token('bio_lifecycle_proof', 'supplied'),
    bio_seed_use_history_proof: token('bio_lifecycle_proof', 'supplied'), bio_seed_payload_debit_proof: token('bio_lifecycle_proof', 'supplied'),
    bio_seed_payload_required: ticks(10), bio_seed_payload_consumed: ticks(10),
    bio_seed_intensity: ticks(1), bio_seed_exposed_share: ticks(1), bio_seed_evidence: ticks(0),
    'global.num_days': ticks(100),
  })) { assert(value !== undefined, name); vm.vars.set(name, value); }
  return vm;
}
function actorRun(vm, name) { const old = vm.identity; vm.identity = 'country:actor'; try { return vm.run(name); } finally { vm.identity = old; } }
function facts(vm) {
  return { count: Number(vm.value('cbrn_achievement_covert_operation_count') / S),
    types: Number(vm.value('cbrn_achievement_operation_type_count') / S),
    firstDay: Number(vm.value('cbrn_achievement_first_covert_operation_day') / S), success: vm.actorFlags.has(strategic) };
}
function install(nodes) { definitions.set(bioName, body(nodes, bioName)); }
function threeReceipts(nodes, route) {
  install(nodes); const vm = seedFixture(route); const steps = [];
  for (const [day, result] of [[100, 'partial'], [130, 'partial'], [170, 'success']]) {
    vm.vars.set('global.num_days', ticks(day)); vm.vars.set('bio_seed_result', token('bio_lifecycle_result', result));
    assert(vm.run('fixture_source_gate_projection')); steps.push(facts(vm));
  }
  return { vm, steps };
}
const summary = { evidenceKind: 'source-predicate projection plus recorder semantics, not native execution',
  sourceHashes: receipts, positive: [], rejectedAtSourceGate: [], acceptedWithoutHistory: [], directBypassControl: [],
  cleanHands: [], chemicalResultProjection: [], baselineRegressionControls: [], cardinalityProved: false };
for (const route of ['food_water_medical_sabotage', 'operative_release']) {
  const before = threeReceipts(beforeNodes, route);
  assert.equal(before.steps[2].count, 1); assert.equal(before.steps[2].success, false);
  summary.baselineRegressionControls.push({ route, steps: before.steps, expectedAssertionsFailed: ['count equals three', 'success flag on third full receipt'] });
  const after = threeReceipts(afterNodes, route);
  assert.deepEqual(after.steps, [
    { count: 1, types: 1, firstDay: 100, success: false },
    { count: 2, types: 1, firstDay: 100, success: false },
    { count: 3, types: 1, firstDay: 100, success: true },
  ]);
  summary.positive.push({ route, steps: after.steps });
  after.vm.actorFlags.add('cbrn_achievement_start_country_eligible');
  after.vm.vars.set('global.num_days', ticks(100) + token('cbrn_achievement_threshold', 'covert_duration_days'));
  assert(actorRun(after.vm, 'cbrn_achievement_clean_hands_dirty_work_is_complete'));
  for (const exclusion of ['cbrn_achievement_covert_discovered_history', 'cbrn_achievement_covert_coverup_history',
    'cbrn_achievement_strategic_civilian_attack_history', 'cbrn_achievement_doomsday_use_history']) {
    after.vm.actorFlags.add(exclusion);
    assert.equal(actorRun(after.vm, 'cbrn_achievement_clean_hands_dirty_work_is_complete'), false);
    after.vm.actorFlags.delete(exclusion); summary.cleanHands.push({ route, exclusion, completed: false });
  }
}
install(afterNodes);
for (const [id, change] of [
  ['failed', vm => vm.vars.set('bio_seed_result', token('bio_lifecycle_result', 'failed'))],
  ['rejected', vm => vm.vars.set('bio_seed_result', token('bio_lifecycle_result', 'rejected'))],
  ['missing_actor', vm => vm.targets.delete('bio_seed_actor')],
  ['wrong_controller', vm => vm.controller = 'country:other'],
  ['missing_debit_proof', vm => vm.vars.delete('bio_seed_payload_debit_proof')],
  ['zero_payload', vm => vm.vars.set('bio_seed_payload_consumed', ticks(0))],
  ['invalid_agent', vm => vm.vars.set('bio_seed_agent', ticks(99))],
  ['zero_intensity', vm => vm.vars.set('bio_seed_intensity', ticks(0))],
  ['ineligible_target', vm => vm.zombie = true],
]) {
  const vm = seedFixture(); change(vm);
  assert.equal(vm.run('bio_lifecycle_seed_record_is_valid'), false, id);
  assert(vm.run('fixture_source_gate_projection'));
  assert.equal(vm.actorFlags.size, 0, id); assert.equal(facts(vm).count, 0, id);
  summary.rejectedAtSourceGate.push(id);
}
for (const [id, change] of [
  ['missing_history_proof', vm => vm.vars.delete('bio_seed_use_history_proof')],
  ['accident', vm => { vm.vars.set('bio_seed_source', token('bio_lifecycle_source', 'accident')); vm.vars.set('bio_seed_route', token('bio_lifecycle_route', 'laboratory_accident')); vm.vars.set('bio_seed_result', token('bio_lifecycle_result', 'accident')); }],
  ['spread', vm => { vm.vars.set('bio_seed_source', token('bio_lifecycle_source', 'spread')); vm.vars.set('bio_seed_route', token('bio_lifecycle_route', 'connected_spread')); vm.vars.set('bio_seed_result', token('bio_lifecycle_result', 'spread')); }],
]) {
  const vm = seedFixture(); change(vm);
  assert(vm.run('bio_lifecycle_seed_record_is_valid'), id);
  assert(vm.run('fixture_source_gate_projection'));
  assert.equal(vm.actorFlags.size, 0, id); assert.equal(facts(vm).count, 0, id);
  summary.acceptedWithoutHistory.push(id);
}
for (const route of ['operative_release', 'food_water_medical_sabotage']) {
  const catastrophic = seedFixture(route, 'catastrophic'); assert(catastrophic.run('fixture_source_gate_projection'));
  assert.deepEqual(facts(catastrophic), { count: 1, types: 1, firstDay: 100, success: false });
  summary.positive.push({ route, result: 'catastrophic', facts: facts(catastrophic) });
}
const noncovert = seedFixture('strategic_raid', 'success'); assert(noncovert.run('fixture_source_gate_projection'));
assert.equal(facts(noncovert).count, 0); assert.equal(facts(noncovert).success, false);
summary.positive.push({ route: 'strategic_raid', facts: facts(noncovert) });
// Deliberately calling the recorder directly bypasses its caller contract.
// These controls must never be reported as dispatch rejection or accepted native receipts.
for (const result of ['failed', 'rejected']) {
  const vm = seedFixture('food_water_medical_sabotage', result); assert(actorRun(vm, bioName));
  assert.equal(facts(vm).count, 1); summary.directBypassControl.push({ result, facts: facts(vm) });
}
function chemicalFlagBlocks(nodes) {
  return body(nodes, 'cbrn_achievement_record_chemical_action').filter(n => n.key === 'if' && n.value.some(x => x.key === 'set_country_flag' && x.value === strategic));
}
const beforeChemical = chemicalFlagBlocks(beforeNodes), afterChemical = chemicalFlagBlocks(afterNodes);
assert.equal(beforeChemical.length, 2); assert.equal(afterChemical.length, 1);
assert.deepEqual(afterChemical[0], beforeChemical[0], 'chemical own result condition preserved exactly');
assert.deepEqual(body(afterNodes, 'cbrn_achievement_record_chemical_action'),
  body(beforeNodes, 'cbrn_achievement_record_chemical_action').filter(n => n !== beforeChemical[1]),
  'the chemical recorder changes only by removing the misplaced biological condition');
for (const [side, blocks] of [['before', beforeChemical], ['after', afterChemical]]) {
  definitions.set('fixture_chemical_strategic_flag_projection', blocks);
  for (const [route, result, expected] of [['cylinder_release', 'failed', side === 'before'],
    ['covert_operation', 'failed', side === 'before'], ['covert_operation', 'success', true],
    ['covert_operation', 'catastrophic', true]]) {
    const vm = seedFixture('food_water_medical_sabotage', 'success');
    vm.vars.set('cbrn_action_delivery_route', token('cbrn_delivery_route', route));
    vm.vars.set('cbrn_action_raid_result', token('cbrn_chemical_raid_result', result));
    assert(actorRun(vm, 'fixture_chemical_strategic_flag_projection'));
    assert.equal(vm.actorFlags.has(strategic), expected, `${side}/${route}/${result}`);
    summary.chemicalResultProjection.push({ side, route, result, strategicFlag: expected, staleBioResult: 'success' });
  }
}
// Verify scope of change semantically: only the two assigned recorder definitions differ.
const beforeMap = new Map(beforeNodes.map(n => [n.key, n]));
for (const n of afterNodes) if (![bioName, 'cbrn_achievement_record_chemical_action'].includes(n.key)) assert.deepEqual(n, beforeMap.get(n.key), n.key);
assert.equal(afterNodes.length, beforeNodes.length);
summary.sharedParserVMHash = digest(fs.readFileSync(path.join(root, 'docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js')));
summary.executedDependencyDefinitions = ['bio_lifecycle_seed_record_is_valid', 'bio_lifecycle_deliberate_seed_record_is_valid',
  'bio_lifecycle_accident_seed_record_is_valid', 'bio_lifecycle_spread_seed_record_is_valid', 'bio_lifecycle_doomsday_seed_record_is_valid',
  'bio_lifecycle_state_is_eligible_ordinary_pathogen_target', 'cbrn_achievement_clean_hands_dirty_work_is_complete',
  'cbrn_achievement_human_campaign_is_eligible'];
summary.projectionContracts = { dispatch: gateProjection, actorRecorderCall: realRecorderCall,
  omitted: ['profile calculations', 'native delivery and callback scheduling', 'policy at native preflight',
    'resource transactions', 'state episode storage', 'unified record and other internal histories'] };
fs.writeFileSync(path.join(__dirname, 'source_results.json'), JSON.stringify(summary, null, 2) + '\n');
console.log(JSON.stringify({ passed: true, acceptedReceiptSequences: 2, sourceGateRejections: summary.rejectedAtSourceGate.length,
  acceptedWithoutHistory: summary.acceptedWithoutHistory.length, exclusionChecks: summary.cleanHands.length,
  chemicalFlagChecks: summary.chemicalResultProjection.length, directBypassControls: summary.directBypassControl.length,
  baselineRegressionControls: summary.baselineRegressionControls.length, cardinalityProved: false }, null, 2));
