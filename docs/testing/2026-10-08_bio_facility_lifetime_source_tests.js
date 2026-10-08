// Bounded facility caller lifetime evidence. Reuses unchanged BaseVM call-frame cleanup.
// Run: node docs/testing/2026-10-08_bio_facility_lifetime_source_tests.js
const fs = require('node:fs'), path = require('node:path'), assert = require('node:assert/strict'), crypto = require('node:crypto');
const { VM: BaseVM, S, ticks, parse, root, definitions, constants } = require('../plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
const evidence = 'docs/testing/2026-10-08_bio_facility_lifetime/';
const read = f => fs.readFileSync(path.join(root, f));
const hash = b => crypto.createHash('sha256').update(b).digest('hex');
const manifest = JSON.parse(read(evidence + 'insertion_manifest.json'));
const supporting = ['common/scripted_effects/biological_lifecycle_effects.txt'];
const captured = new Map([...manifest.files.map(f => f.path), ...supporting].map(f => [f, read(f)]));
const basePath = 'docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js', baseHash = hash(read(basePath));
const walk = ns => ns.flatMap(n => [n, ...(Array.isArray(n.value) ? walk(n.value) : [])]);
const def = (ns, key) => { const n = ns.find(n => n.key === key); assert(n, key); return n.value; };
const normal = s => s.replace(/\r\n/g, '\n');
const out = x => Number(x) / Number(S), cases = [], executedHelpers = new Set(), observedCommands = new Set(), constantHashes = {};
const constantFiles = ['biological_lifecycle_constants', 'biological_facility_capture_constants', 'biological_field_test_constants', 'biological_stockpile_safety_constants', 'cbrn_diplomacy_constants', 'special_project_constants'];
function withoutSchemas(text) { let match; while ((match = /\bschema\s*=\s*\{/.exec(text))) { let pos = match.index + match[0].length, depth = 1; while (depth && pos < text.length) { if (text[pos] === '{') depth++; else if (text[pos] === '}') depth--; pos++; } assert.equal(depth, 0); text = text.slice(0, match.index) + text.slice(pos); } return text; }
for (const file of constantFiles) {
 const source = 'common/script_constants/' + file + '.txt', bytes = read(source); constantHashes[source] = hash(bytes);
 const ns = parse(withoutSchemas(bytes.toString('utf8')));
 function loadNumeric(ns, prefix = '') { for (const n of ns) { if (n.key === 'schema') continue; const name = prefix ? prefix + '.' + n.key : n.key; if (Array.isArray(n.value)) loadNumeric(n.value, name); else if (/^-?\d+(\.\d+)?$/.test(n.value)) constants.set('constant:' + name, ticks(n.value)); } }
 loadNumeric(ns);
}
const fixtures = {
 bio_lifecycle_prepare_route_profile: 'set_temp_variable = { bio_seed_intensity = 10 } set_temp_variable = { bio_seed_exposed_share = 20 } set_temp_variable = { bio_seed_evidence = 30 }',
 bio_lifecycle_prepare_agent_profile: '',
 bio_lifecycle_finalize_seed_values: 'set_temp_variable = { bio_seed_intensity_final = 10 } set_temp_variable = { bio_seed_exposed_share_final = 20 } set_temp_variable = { bio_seed_evidence_final = 30 }',
 cbrn_diplomacy_classify_biological_seed_retaliation: '',
 bio_lifecycle_store_seed_in_current_agent_record: 'test_seed_store = yes',
 bio_lifecycle_grant_integrated_operations_release_command_recovery: '',
 bio_lifecycle_schedule_incubation_for_current_agent: '',
 bio_lifecycle_mark_current_agent_detected: '',
 bio_lifecycle_record_internal_deliberate_use: 'test_deliberate_use = yes',
};
function load(stage) {
 for (const f of captured.keys()) {
  const text = stage === 'before' && manifest.files.some(x => x.path === f) ? read(evidence + 'before/' + f) : captured.get(f);
  for (const n of parse(text.toString('utf8'))) definitions.set(n.key, n.value);
 }
 for (const [name, source] of Object.entries(fixtures)) definitions.set(name, parse(source));
}
class VM extends BaseVM {
 constructor(options = {}) {
  super(); this.options = { context: true, seedValid: true, draw: 0, accident: true, actorExists: true, controller: 9, root: 7, ...options };
  this.scope = 100; this.stores = new Map([[100, this.regularVars], [7, new Map()], [9, new Map()], [200, new Map()]]);
  this.scopeFlags = new Map([...this.stores.keys()].map(k => [k, new Set()])); this.targets = new Map(); this.trace = []; this.seedStores = [];
 }
 enter(id, body) { assert(this.stores.has(id), 'unknown scope ' + id); const old = this.scope, map = this.regularVars; this.scope = id; this.regularVars = this.stores.get(id); try { return body(); } finally { this.scope = old; this.regularVars = map; } }
 value(t) {
  if (t === 'THIS') return ticks(this.scope);
  if (t === 'ROOT') return ticks(this.options.root);
  if (t === 'global.num_days') return ticks(40);
  if (t.startsWith('ROOT.')) return this.stores.get(this.options.root).get(t.slice(5)) ?? 0n;
  if (t.startsWith('event_target:')) { const [name, field] = t.slice(13).split('.'); const id = this.targets.get(name); return field ? this.stores.get(id)?.get(field) ?? 0n : ticks(id ?? 0); }
  return super.value(t);
 }
 run(name, ...args) {
  executedHelpers.add(name);
  if (name === 'bio_lifecycle_dispatch_seed') this.trace.push({ kind: 'dispatch_entry', scope: this.scope, targets: Object.fromEntries(this.targets), inputs: Object.fromEntries([...this.vars].filter(([k]) => k.startsWith('bio_seed_')).map(([k, v]) => [k, out(v)])) });
  const yes = super.run(name, ...args);
  if (['bio_facility_capture_select_release_agent', 'bio_facility_capture_prepare_fraction_amount', 'bio_facility_capture_enforce_release_minimum', 'bio_facility_capture_debit_selected_release', 'bio_lifecycle_dispatch_seed'].includes(name)) this.trace.push({ kind: 'return', helper: name, scope: this.scope, outputs: Object.fromEntries([...this.vars].filter(([k]) => k.startsWith('bio_facility_capture_') || k === 'bio_seed_dispatch_status').map(([k, v]) => [k, out(v)])) });
  return yes;
 }
 eval(nodes) {
  let chunk = [];
  const flush = () => { const ns = chunk; chunk = []; return !ns.length || super.eval(ns); };
  for (const n of nodes) {
   const k = n.key, v = n.value;
   observedCommands.add(k);
   const scope = k.startsWith('event_target:') || k.startsWith('var:') || ['ROOT', 'FROM', 'FROM.owner', 'CONTROLLER'].includes(k);
   const local = ['has_event_target', 'save_event_target_as', 'exists', 'tag', 'has_state_flag', 'set_state_flag', 'clr_state_flag', 'has_country_flag', 'set_country_flag', 'clr_country_flag', 'add_to_variable', 'multiply_variable', 'round_temp_variable', 'random', 'random_list', 'meta_effect', 'country_event', 'state_event', 'add_project_progress_ratio', 'test_seed_store', 'test_deliberate_use'];
   const fixture = ['bio_facility_capture_release_context_is_valid', 'bio_facility_capture_state_has_payload', 'bio_lifecycle_seed_record_is_valid', 'cbrn_designer_has_sealed_sample_chain'].includes(k);
   if (!scope && !local.includes(k) && !fixture) { assert(!['add_equipment_to_stockpile', 'add_command_power', 'add_fuel'].includes(k), 'native command outside modeled boundary ' + k); chunk.push(n); continue; }
   if (!flush()) return false;
   if (scope) {
    const id = k.startsWith('event_target:') ? this.targets.get(k.slice(13)) : k.startsWith('var:') ? Number(this.value(k.slice(4)) / S) : k === 'ROOT' ? this.options.root : k === 'FROM' ? 200 : k === 'FROM.owner' ? 7 : this.options.controller;
    if (!id) return false; if (!this.enter(id, () => this.eval(v))) return false;
   } else if (k === 'save_event_target_as') this.targets.set(v, this.scope);
   else if (k === 'has_event_target') { if (!this.targets.has(v)) return false; }
   else if (k === 'exists') { if (!(this.scope !== 7 || this.options.actorExists)) return false; }
   else if (k === 'tag') { if (this.scope !== Number(this.value(v) / S)) return false; }
   else if (k.startsWith('has_') && k.endsWith('_flag')) { if (!this.scopeFlags.get(this.scope).has(v)) return false; }
   else if (k.startsWith('set_') && k.endsWith('_flag')) this.scopeFlags.get(this.scope).add(v);
   else if (k.startsWith('clr_') && k.endsWith('_flag')) this.scopeFlags.get(this.scope).delete(v);
   else if (k === 'add_to_variable' || k === 'multiply_variable') { const name = this.field(v, 'var') || v[0].key, a = this.value(name), b = this.value(this.field(v, 'value') || v[0].value); this.write(name, k === 'add_to_variable' ? a + b : a * b / S, false); }
   else if (k === 'round_temp_variable') { const a = this.value(v); assert(a >= 0n); this.write(v, (a + S / 2n) / S * S); }
   else if (k === 'random_list') { const chosen = this.options.draw; assert(chosen < v.length); this.trace.push({ kind: 'fixed_draw', scope: this.scope, branch: v[chosen].key }); if (!this.eval(v[chosen].value)) return false; }
   else if (k === 'random') { this.trace.push({ kind: 'fixed_random', accident: this.options.accident }); if (this.options.accident && !this.eval(v.filter(n => n.key !== 'chance'))) return false; }
   else if (k === 'meta_effect') {
    const args = {}; for (const arg of v.filter(n => n.key !== 'text')) { const match = arg.value.match(/^"\[\?([^|\]]+)\|\.0\]"$/); assert(match, arg.value); args[arg.key] = String(this.value(match[1]) / S); }
    const replace = x => x.replace(/\[([^\]]+)\]/g, (_, key) => { assert(Object.hasOwn(args, key)); return args[key]; });
    const expand = ns => ns.map(n => ({ ...n, key: replace(n.key), value: Array.isArray(n.value) ? expand(n.value) : replace(n.value) }));
    if (!this.eval(expand(this.field(v, 'text')))) return false;
   } else if (k === 'country_event' || k === 'state_event') this.trace.push({ kind: k, id: this.field(v, 'id'), scope: this.scope });
   else if (k === 'add_project_progress_ratio') { assert.equal(this.scope, 200); this.trace.push({ kind: 'project_progress', gain: out(this.value(v)), scope: this.scope }); }
   else if (k === 'test_seed_store') {
    const fields = ['bio_seed_agent', 'bio_seed_route', 'bio_seed_source', 'bio_seed_result', 'bio_seed_payload_required', 'bio_seed_payload_consumed', 'bio_seed_intensity_override', 'bio_seed_exposed_share_override', 'bio_seed_evidence_override', 'bio_seed_condemnation_override', 'bio_seed_weaponization_mult', 'bio_seed_actor_proof', 'bio_seed_victim_proof', 'bio_seed_force_detection_on_activation'];
    this.seedStores.push({ scope: this.scope, actor: this.targets.get('bio_seed_actor') ?? null, victim: this.targets.get('bio_seed_victim') ?? null, fields: Object.fromEntries(fields.map(k => [k, out(this.value(k))])) });
   } else if (k === 'test_deliberate_use') throw Error('accident reached deliberate-use sink');
   else if (fixture) {
    const yes = k === 'bio_facility_capture_state_has_payload' ? ['anthrax', 'plague', 'tularemia', 'smallpox'].some(a => this.regularVars.get('bio_captured_facility_' + a) > 0n) : k === 'bio_lifecycle_seed_record_is_valid' ? this.options.seedValid : k === 'cbrn_designer_has_sealed_sample_chain' ? false : this.options.context;
    if (yes !== (v === 'yes')) return false;
   }
  }
  return flush();
 }
}
function test(id, fn) { try { cases.push({ id, status: 'passed', ...fn() }); } catch (e) { cases.push({ id, status: 'failed', error: e.stack }); } }
test('exact-insertions-preserve-all-original-statements-and-weighted-asts', () => {
 let declarations = 0, sites = 0, weightedBlocks = 0;
 for (const f of manifest.files) {
  const old = read(evidence + 'before/' + f.path), after = read(evidence + 'after/' + f.path); assert.equal(hash(old), f.beforeSha256); assert.equal(hash(after), f.afterSha256); assert.equal(normal(captured.get(f.path).toString('utf8')), normal(after.toString('utf8')));
  let text = after.toString('utf8'); for (const i of f.insertions.slice().reverse()) { const at = i.beforeOffset + f.insertions.filter(j => j.beforeOffset < i.beforeOffset).reduce((a, j) => a + j.text.length, 0); assert.equal(text.slice(at, at + i.text.length), i.text); text = text.slice(0, at) + text.slice(at + i.text.length); declarations += Object.keys(i.fields).length; sites++; }
  assert.equal(text, old.toString('utf8')); assert.deepEqual(parse(text), parse(old.toString('utf8')));
  const weighted = ns => walk(ns).filter(n => ['random', 'random_list', 'ai_chance', 'ai_will_do'].includes(n.key)); const a = weighted(parse(after.toString('utf8'))), b = weighted(parse(old.toString('utf8')));
  assert.deepEqual(a, b); weightedBlocks += a.length;
 }
 assert.equal(declarations, 29); assert.equal(sites, 7); return { declarations, sites, weightedBlocks, byteReconstruction: true };
});
const agents = ['anthrax', 'plague', 'tularemia', 'smallpox'];
function captureVM(draw, stock, options = {}) { const vm = new VM({ draw, ...options }); for (const [i, a] of agents.entries()) vm.stores.get(100).set('bio_captured_facility_' + a, ticks(i === draw ? stock : 0)); vm.stores.get(100).set('bio_stockpile_safety_arsenal_actor', ticks(7)); vm.write('bio_facility_capture_release_fraction', ticks(0.1)); return vm; }
for (const [draw, agent] of agents.entries()) for (const stock of [1, 10, 100]) test('capture-' + agent + '-stock-' + stock, () => {
 load('after'); const vm = captureVM(draw, stock); assert(vm.run('bio_facility_capture_dispatch_accidental_release')); const key = 'bio_captured_facility_' + agent, amount = Math.max(1, Math.round(stock * 0.1));
 assert.equal(vm.stores.get(100).get(key), ticks(stock - amount)); assert.equal(vm.stores.get(100).get('bio_captured_facility_last_release_agent'), ticks(draw + 1)); assert.equal(vm.stores.get(100).get('bio_captured_facility_last_release_amount'), ticks(amount)); assert.equal(vm.seedStores.length, 1); assert.equal(vm.seedStores[0].scope, 100); assert.equal(vm.seedStores[0].actor, 7); assert.equal(vm.seedStores[0].victim, 9); assert.equal(vm.seedStores[0].fields.bio_seed_payload_consumed, amount);
 load('before'); const old = captureVM(draw, stock); assert(old.run('bio_facility_capture_dispatch_accidental_release')); assert.equal(old.stores.get(100).get(key), ticks(stock)); assert.equal(old.seedStores.length, 0);
 return { agent, stockBefore: stock, stockAfter: stock - amount, amount, baselineFailureReproduced: true, trace: vm.trace, seed: vm.seedStores[0] };
});
for (const [draw, agent] of agents.entries()) test('direct-debit-nested-storage-' + agent, () => {
 load('after'); const vm = captureVM(draw, 100); assert(vm.run('bio_facility_capture_debit_selected_release')); assert.equal(vm.stores.get(100).get('bio_captured_facility_' + agent), ticks(90));
 const fraction = vm.trace.find(t => t.kind === 'return' && t.helper === 'bio_facility_capture_prepare_fraction_amount').outputs; assert.equal(fraction.bio_facility_capture_fraction_amount, 10); assert.equal(fraction.bio_facility_capture_fraction_amount_negative, -10);
 load('before'); const old = captureVM(draw, 100); assert(old.run('bio_facility_capture_debit_selected_release')); assert.equal(old.stores.get(100).get('bio_captured_facility_' + agent), ticks(100)); return { agent, nestedPositive: 10, nestedNegative: -10, baselineFailureReproduced: true, trace: vm.trace };
});
for (const scenario of ['invalid_context', 'zero_stock', 'missing_actor', 'seed_rejected']) test('capture-' + scenario, () => {
 load('after'); const vm = captureVM(0, scenario === 'zero_stock' ? 0 : 100, { context: scenario !== 'invalid_context', actorExists: scenario !== 'missing_actor', seedValid: scenario !== 'seed_rejected' }); assert(vm.run('bio_facility_capture_dispatch_accidental_release'));
 if (['invalid_context', 'zero_stock'].includes(scenario)) { assert.equal(vm.stores.get(100).get('bio_captured_facility_anthrax'), ticks(scenario === 'zero_stock' ? 0 : 100)); assert.equal(vm.seedStores.length, 0); }
 else if (scenario === 'missing_actor') { assert.equal(vm.seedStores.length, 1); assert.equal(vm.seedStores[0].fields.bio_seed_actor_proof, 0); assert(!vm.targets.has('bio_seed_actor')); }
 else { assert.equal(vm.seedStores.length, 0); assert.equal(vm.stores.get(100).get('bio_captured_facility_anthrax'), ticks(90)); assert(vm.scopeFlags.get(100).has('bio_captured_facility_release_history')); }
 return { scenario, seed: vm.seedStores, trace: vm.trace, semantics: scenario === 'seed_rejected' ? 'existing debit/history precede dispatch acceptance' : 'unchanged selected path' };
});
for (const [draw, agent] of agents.entries()) for (const accept of [false, true]) test('field-' + agent + '-' + accept, () => {
 const setup = () => { const vm = new VM({ controller: 7, seedValid: accept }); vm.write('bio_active_agent', ticks(99)); return vm; };
 load('after'); const vm = setup(); assert(vm.run('conduct_' + agent + '_field_test')); assert.equal(vm.value('bio_active_agent'), ticks(accept ? draw + 1 : 99)); assert.equal(vm.seedStores.length, accept ? 1 : 0); assert.equal(vm.trace.filter(t => t.kind === 'country_event').length, accept ? 1 : 0); assert.equal(vm.trace.find(t => t.kind === 'return' && t.helper === 'bio_lifecycle_dispatch_seed').outputs.bio_seed_dispatch_status, accept ? 1 : 0);
 if (accept) { assert.equal(vm.seedStores[0].actor, 7); assert.equal(vm.seedStores[0].victim, 7); assert.equal(vm.seedStores[0].scope, 100); assert.equal(vm.seedStores[0].fields.bio_seed_payload_required, 0); }
 load('before'); const old = setup(); assert(old.run('conduct_' + agent + '_field_test')); assert.equal(old.trace.filter(t => t.kind === 'country_event').length, 0);
 return { agent, accepted: accept, baselineReceiptLossReproduced: accept, trace: vm.trace, seeds: vm.seedStores };
});
for (const scenario of ['contained', 'wrong_controller', 'missing_actor']) test('field-' + scenario, () => {
 load('after'); const vm = new VM({ accident: scenario !== 'contained', controller: scenario === 'wrong_controller' ? 9 : 7, actorExists: scenario !== 'missing_actor' }); assert(vm.run('conduct_anthrax_field_test')); assert.equal(vm.seedStores.length, 0); assert.equal(vm.trace.filter(t => t.kind === 'country_event').length, scenario === 'contained' ? 1 : 0); return { scenario, trace: vm.trace };
});
for (const [index, agent] of agents.entries()) for (const severity of ['contained', 'lab_contamination', 'local_outbreak', 'major_domestic_outbreak', 'international_exposure']) test('stockpile-' + agent + '-' + severity, () => {
 load('after'); const vm = new VM({ controller: 7 }); const actor = vm.stores.get(7); const fields = { bio_stockpile_safety_arsenal_state: 100, bio_stockpile_safety_selected_agent: index + 1, bio_stockpile_safety_selected_intensity: 11, bio_stockpile_safety_selected_exposed_share: 22, bio_stockpile_safety_selected_evidence: 33, bio_stockpile_safety_selected_condemnation: 44, bio_stockpile_safety_stock_loss_amount: 5 };
 for (const [k, v] of Object.entries(fields)) actor.set(k, ticks(v)); actor.set('bio_stockpile_safety_selected_incident_severity', constants.get('constant:bio_stockpile_safety_incident_severity.' + severity)); actor.set('fixture_national_stock', ticks(95));
 assert(vm.enter(7, () => vm.run('bio_stockpile_safety_dispatch_selected_accident'))); assert.equal(actor.get('fixture_national_stock'), ticks(95)); assert.equal(vm.stores.get(100).get('bio_stockpile_safety_last_accident_agent'), ticks(index + 1)); assert.equal(vm.stores.get(100).get('bio_stockpile_safety_last_accident_stock_loss'), ticks(5)); assert.equal(vm.seedStores.length, severity === 'contained' ? 0 : 1);
 if (severity !== 'contained') { const seed = vm.seedStores[0]; assert.equal(seed.scope, 100); assert.equal(seed.actor, 7); assert.equal(seed.victim, 7); assert.equal(seed.fields.bio_seed_intensity_override, 11); assert.equal(seed.fields.bio_seed_exposed_share_override, 22); assert.equal(seed.fields.bio_seed_evidence_override, 33); assert.equal(seed.fields.bio_seed_condemnation_override, 44); assert.equal(seed.fields.bio_seed_payload_consumed, 5); assert.equal(seed.fields.bio_seed_weaponization_mult, 1); }
 return { agent, severity, countryStockAtSeedEntry: 95, countryStockAfterSeed: 95, stateReceipt: 5, trace: vm.trace, seeds: vm.seedStores, scopeCaveat: 'ROOT and dispatching actor are the same country, as in current owner callback' };
});
for (const owner of ['bio_facility_capture_dispatch_accidental_release', 'bio_field_test_resolve_exact_facility_test', 'bio_stockpile_safety_dispatch_selected_accident']) test('reset-only-storage-' + owner, () => {
 const file = manifest.files.find(f => f.insertions.some(i => i.owner === owner && i.call === 'bio_lifecycle_reset_seed_record = yes'));
 const insertion = file.insertions.find(i => i.owner === owner && i.call === 'bio_lifecycle_reset_seed_record = yes');
 function sequence(ns) { if (ns.some(n => n.key === 'bio_lifecycle_reset_seed_record')) return ns; for (const n of ns) if (Array.isArray(n.value)) { const found = sequence(n.value); if (found) return found; } return null; }
 function check(stage, stale) { load(stage); const text = stage === 'before' ? read(evidence + 'before/' + file.path) : captured.get(file.path); const seq = sequence(def(parse(text.toString('utf8')), owner)); const at = seq.findIndex(n => n.key === 'bio_lifecycle_reset_seed_record'); const vm = new VM(); if (stale) for (const key of Object.keys(insertion.fields)) vm.write(key, ticks(77)); assert(vm.eval(seq.slice(0, at + 1).filter(n => n.key !== 'limit'))); return vm; }
 const fresh = check('after', false), old = check('before', false), stale = check('after', true);
 for (const [key, value] of Object.entries(insertion.fields)) { assert(fresh.vars.has(key), key); assert.equal(fresh.value(key), constants.get(value)); assert(!old.vars.has(key), key); assert.equal(stale.value(key), constants.get(value)); }
 return { fields: insertion.fields, baselineAbsentStorageReproduced: true, staleDefaultsCleared: true };
});
test('base-vm-remains-unchanged', () => { assert.equal(hash(read(basePath)), baseHash); return { baseHash }; });
const result = { status: cases.some(c => c.status === 'failed') ? 'failed' : 'passed', cases: cases.length, failures: cases.filter(c => c.status === 'failed').length, evidenceKind: 'actual owner, debit/fraction/select/reset/dispatcher source under conservative BaseVM helper lifetime', sourceHashes: Object.fromEntries([...captured].map(([f, b]) => [f, hash(b)])), constantHashes, executedHelpers: [...executedHelpers].sort(), observedCommands: [...observedCommands].sort(), baseVM: { path: basePath, sha256: baseHash, unchanged: true }, fixtures, fixtureSemantics: ['fixed random-list branch and direct-random boolean, no RNG distribution', 'explicit source-context and canonical seed-validity booleans', 'route/profile/final-value and later storage/scheduler sinks are declared fixtures, no shared-lifecycle acceptance claim', 'separate country/state/project maps', 'ordinary arithmetic/rounding modeled, no native equipment payment or callback simulation'], results: cases };
fs.writeFileSync(path.join(root, 'docs/testing/2026-10-08_bio_facility_lifetime_source_results.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify({ status: result.status, cases: result.cases, failures: result.failures, failed: cases.filter(c => c.status === 'failed').map(c => ({ id: c.id, error: c.error.split('\n')[0] })) }, null, 2));
process.exitCode = result.failures ? 1 : 0;
