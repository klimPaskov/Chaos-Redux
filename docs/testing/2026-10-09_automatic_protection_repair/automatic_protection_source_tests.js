// Bounded execution of production ASTs. Native stock/scope inputs are modeled.
// The reused VM.run retains conservative helper temporary cleanup unchanged.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const base = require('../../plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
const { VM, S, ticks, parse, definitions, constants, root } = base;
const sourcePaths = ['common/scripted_effects/cbrn_protection_effects.txt', 'common/scripted_effects/cbrn_protection_decision_effects.txt'];
const models = ['reconditioned', 'basic', 'improved', 'advanced', 'sealed'];
const equipment = ['gas_mask_equipment_reconditioned', 'gas_mask_equipment_1', 'gas_mask_equipment_2', 'gas_mask_equipment_3', 'gas_mask_equipment_4'];
const before = sourcePaths.map(f => fs.readFileSync(path.join(__dirname, path.basename(f) + '.before')));
const after = sourcePaths.map(f => fs.readFileSync(path.join(root, f)));
const hash = b => crypto.createHash('sha256').update(b).digest('hex');
const report = { model: 'Production ASTs and unchanged VM.run cleanup, five decimal fixed point, modeled native stock/scope inputs', cases: [], sourceHashes: sourcePaths.map((p, i) => ({ path: p, before: hash(before[i]), after: hash(after[i]) })) };
const originalDefinitions = new Map(before.flatMap(b => parse(b.toString('utf8')).map(n => [n.key, n.value])));
const currentDefinitions = new Map(after.flatMap(b => parse(b.toString('utf8')).map(n => [n.key, n.value])));
for (const id of ['cbrn_debit_mask_stockpile_oldest_first', 'cbrn_issue_masks_to_field_army', 'cbrn_issue_requested_masks_to_military', 'cbrn_refresh_country_mask_snapshot', 'cbrn_refresh_state_civilian_mask_snapshot', 'cbrn_refresh_country_readiness_status', 'cbrn_start_protection_maintenance_job', 'cbrn_apply_annual_mask_storage_loss', 'cbrn_recondition_damaged_masks', 'cbrn_distribute_requested_masks_to_state_internal']) assert.deepEqual(currentDefinitions.get(id), originalDefinitions.get(id), `preserved production helper ${id}`);
report.preservedHelperASTs = 10;
assert.deepEqual(currentDefinitions.get('cbrn_complete_mask_reconditioning').find(n => n.key === 'if'), originalDefinitions.get('cbrn_complete_mask_reconditioning').find(n => n.key === 'if'), 'quality roll, weights and event branch unchanged');
report.dependencies = [];
for (const f of fs.readdirSync(path.join(root, 'common/script_constants')).filter(f => f.startsWith('cbrn_') && f.endsWith('.txt'))) {
  const walk = (nodes, prefix = []) => {
    for (const n of nodes) {
      if (Array.isArray(n.value)) walk(n.value, [...prefix, n.key]);
      else if (/^-?\d+(\.\d+)?$/.test(n.value)) constants.set('constant:' + [...prefix, n.key].join('.'), ticks(n.value));
    }
  };
  report.dependencies.push({ path: 'common/script_constants/' + f, sha256: hash(fs.readFileSync(path.join(root, 'common/script_constants', f))) });
  // Schema metadata contains anonymous braces outside the harness grammar.
  // Remove only balanced schema blocks, retaining every authored tuning value.
  let text = fs.readFileSync(path.join(root, 'common/script_constants', f), 'utf8');
  for (let m; (m = /\bschema\s*=\s*\{/.exec(text));) {
    let end = m.index + m[0].length, depth = 1;
    while (depth && end < text.length) { const c = text[end++]; if (c === '{') depth++; if (c === '}') depth--; }
    assert.equal(depth, 0); text = text.slice(0, m.index) + text.slice(end);
  }
  walk(parse(text));
}
for (const f of ['common/scripted_triggers/cbrn_protection_triggers.txt', 'common/scripted_triggers/cbrn_triggers.txt', 'docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js']) report.dependencies.push({ path: f, sha256: hash(fs.readFileSync(path.join(root, f))) });
const noops = new Set([
  // Fixtures are already initialized. Ancillary achievements and cleanup pools
  // do not determine mask issue/service or derived mask readiness in these cases.
  'cbrn_initialize_country_data', 'cbrn_initialize_state_protection',
  'cbrn_refresh_state_civilian_decontamination_snapshot', 'cbrn_refresh_country_civilian_decontamination_pool',
  'cbrn_achievement_record_country_protection_snapshot', 'cbrn_achievement_record_state_protection_snapshot',
  // Reserved-wrapper cases stop at refund entry. Full native refunds are a
  // separate owner suite, not coverage claimed by this source model.
  'cbrn_refund_occupied_state_mask_reservation', 'cbrn_refund_external_state_mask_reservation',
]);
class ProtectionVM extends VM {
  constructor() {
    super();
    this.scopes = new Map([['country', { vars: new Map(), flags: new Set(), tech: new Set(), stock: new Map(), native: new Map([['deployed_army_manpower_k', ticks(100)]]) }], ['state', { vars: new Map(), flags: new Set(), tech: new Set(), stock: new Map(), native: new Map([['state_population_k', ticks(1000)]]) }]]);
    this.scope = 'country'; this.previous = 'country'; this.trace = []; this.debits = []; this.rolls = []; this.events = []; this.branch = 0; this.publicThreat = false;
    this.select('country');
  }
  select(name) { this.scope = name; this.regularVars = this.scopes.get(name).vars; }
  scoped(name, fn) {
    const old = this.scope, previous = this.previous; this.previous = old; this.select(name);
    try { return fn(); } finally { this.previous = previous; this.select(old); }
  }
  normal(scope, key, value) { this.scopes.get(scope).vars.set(key, ticks(value)); return this; }
  get(scope, key) { return this.scopes.get(scope).vars.get(key) || 0n; }
  stock(values) { equipment.forEach((e, i) => this.scopes.get('country').stock.set(e, ticks(values[i] || 0))); return this; }
  totalStock() { return equipment.reduce((a, e) => a + (this.scopes.get('country').stock.get(e) || 0n), 0n); }
  value(token) {
    if (token === 'ROOT' || token === 'THIS' || token === 'PREV') return (token === 'THIS' && this.scope === 'state' ? 8n : 7n) * S;
    if (token.startsWith('PREV.')) return this.scopes.get(this.previous).vars.get(token.slice(5)) || 0n;
    if (token.startsWith('ROOT.')) return this.scopes.get('country').vars.get(token.slice(5)) || 0n;
    if (token.startsWith('num_equipment@')) return this.scopes.get(this.scope).stock.get(token.split('@')[1]) || 0n;
    if (token.startsWith('num_equipment_in_armies@')) return 0n;
    if (this.scopes.get(this.scope).native.has(token)) return this.scopes.get(this.scope).native.get(token);
    return super.value(token);
  }
  run(name, allow = false) {
    this.trace.push({ name, scope: this.scope });
    if (noops.has(name)) return true;
    if (name === 'cbrn_achievement_record_external_mask_aid') { this.aidCredits = (this.aidCredits || 0) + 1; return true; }
    if (name.startsWith('cbrn_profile_is_') || name.startsWith('cbrn_designer_has_') || name === 'cbrn_project_has_renewing_filters') return false;
    if (['cbrn_country_has_public_chemical_emergency', 'cbrn_country_faces_enemy_chemical_capability'].includes(name)) return this.publicThreat;
    if (name === 'cbrn_country_needs_civilian_mask_issue') return false; // fixture has service need only
    return super.run(name, allow);
  }
  eval(nodes) {
    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i], k = n.key, v = n.value, f = (key, fallback) => this.field(v, key, fallback);
      if (k === 'if') {
        const chain = [n]; while (nodes[i + 1] && ['else', 'else_if'].includes(nodes[i + 1].key)) chain.push(nodes[++i]);
        if (!super.eval(chain)) return false;
      } else if (['ROOT', 'controller', 'var:cbrn_occupied_mask_escrow_donor', 'var:cbrn_external_mask_escrow_donor', 'event_target:cbrn_distribution_external_supplier'].includes(k)) {
        if (!this.scoped('country', () => this.eval(v))) return false;
      } else if (k === 'PREV') { if (!this.scoped(this.previous, () => this.eval(v))) return false; }
      else if (k === 'capital_scope') { if (!this.scoped('state', () => this.eval(v))) return false; }
      else if (k === 'every_controlled_state' || k === 'any_controlled_state') {
        const yes = this.scoped('state', () => this.eval(f('limit', [])) && this.eval(v.filter(n => n.key !== 'limit')));
        if (k === 'any_controlled_state' && !yes) return false;
      } else if (k === 'is_capital') { if (v !== 'yes') return false; }
      else if (k === 'is_controlled_by' || k === 'is_core_of' || k === 'exists' || k === 'tag') { /* one valid controlled core state */ }
      else if (k === 'has_state_category') return false; // rural fixture
      else if (k === 'infrastructure') { if (!(5 < Number(v))) return false; }
      else if (this.scopes.get(this.scope).native.has(k)) {
        const a = this.value(k), b = this.value(v); if (!(n.op === '>' ? a > b : n.op === '<' ? a < b : a === b)) return false;
      }
      else if (k === 'has_tech' || k === 'has_doctrine') { if (!this.scopes.get(this.scope).tech.has(v)) return false; }
      else if (k === 'has_idea') return false;
      else if (k === 'has_equipment') {
        const e = v[0]; const a = e.key === 'gas_mask_equipment' ? this.totalStock() : this.scopes.get(this.scope).stock.get(e.key) || 0n;
        if (e.op === '>' ? a <= this.value(e.value) : a !== this.value(e.value)) return false;
      } else if (k === 'has_country_flag' || k === 'has_state_flag') { if (!this.scopes.get(this.scope).flags.has(v)) return false; }
      else if (k === 'set_country_flag' || k === 'set_state_flag') this.scopes.get(this.scope).flags.add(Array.isArray(v) ? f('flag') : v);
      else if (k === 'clr_country_flag' || k === 'clr_state_flag') this.scopes.get(this.scope).flags.delete(v);
      else if (k === 'has_event_target') { if (!this.hasSupplier) return false; }
      else if (k === 'save_event_target_as') this.hasSupplier = true;
      else if (k === 'add_equipment_to_stockpile') {
        const e = f('type'), amount = this.value(f('amount')), store = this.scopes.get(this.scope).stock;
        const old = store.get(e) || 0n; assert(old + amount >= 0n, `modeled debit cannot exceed stock ${e}`); store.set(e, old + amount);
        this.debits.push({ scope: this.scope, model: e, amount: String(amount / S) });
      } else if (k === 'country_event') this.events.push({ id: f('id'), days: f('days') === undefined ? null : String(this.value(f('days')) / S) });
      else if (k === 'random_list') {
        const weights = v.map(n => this.value(n.key)); this.rolls.push(weights.map(x => String(x / S)));
        assert(this.branch >= 0 && this.branch < v.length); if (!this.eval(v[this.branch].value)) return false;
      } else if (k === 'clamp_variable' || k === 'clamp_temp_variable') {
        const key = f('var'), a = this.value(key), min = f('min'), max = f('max');
        this.write(key, min !== undefined && a < this.value(min) ? this.value(min) : max !== undefined && a > this.value(max) ? this.value(max) : a, k === 'clamp_temp_variable');
      } else if (k === 'round_variable' || k === 'round_temp_variable') {
        const a = this.value(v); this.write(v, ((a + S / 2n) / S) * S, k === 'round_temp_variable');
      } else if (['add_to_variable', 'subtract_from_variable', 'multiply_variable', 'divide_variable'].includes(k)) {
        const key = f('var', v[0].key), operand = this.value(f('value', v[0].value)), a = this.value(key);
        assert(k !== 'divide_variable' || operand !== 0n);
        const result = k === 'add_to_variable' ? a + operand : k === 'subtract_from_variable' ? a - operand : k === 'multiply_variable' ? a * operand / S : a * S / operand;
        this.write(key, result, false);
      } else if (k === 'divide_temp_variable' || k === 'multiply_temp_variable') {
        // Ordinary protection arithmetic truncates to the modeled five decimals.
        // Exact-cost API arithmetic is unchanged in the reused VM.
        const key = f('var', v[0].key), operand = this.value(f('value', v[0].value)); assert(k !== 'divide_temp_variable' || operand !== 0n);
        this.write(key, k === 'divide_temp_variable' ? this.value(key) * S / operand : this.value(key) * operand / S);
      } else if (noops.has(k) || k.startsWith('cbrn_profile_is_') || k.startsWith('cbrn_designer_has_') || ['cbrn_project_has_renewing_filters', 'cbrn_country_has_public_chemical_emergency', 'cbrn_country_faces_enemy_chemical_capability', 'cbrn_country_needs_civilian_mask_issue', 'cbrn_achievement_record_external_mask_aid'].includes(k)) {
        const yes = this.run(k); if ((v === 'no' && yes) || (v !== 'no' && !yes)) return false;
      } else if (!super.eval([n])) return false;
    }
    return true;
  }
}
function load(buffers) {
  buffers.forEach(b => parse(b.toString('utf8')).forEach(n => { if (Array.isArray(n.value)) definitions.set(n.key, n.value); }));
  for (const p of ['common/scripted_triggers/cbrn_triggers.txt','common/scripted_triggers/cbrn_protection_triggers.txt']) parse(fs.readFileSync(path.join(root,p),'utf8')).forEach(n => definitions.set(n.key,n.value));
}
function fixture(values = [0, 0, 0, 0, 0]) {
  return new ProtectionVM().stock(values)
    .normal('country', 'cbrn_military_issued_mask_basic', 1000).normal('country', 'cbrn_military_mask_filter_condition', 50)
    .normal('country', 'cbrn_mask_replacement_demand', 180)
    .normal('state', 'cbrn_civilian_mask_crates', 1000).normal('state', 'cbrn_civilian_mask_basic_crates', 1000).normal('state', 'cbrn_civilian_mask_fit_points', 1000)
    .normal('state', 'cbrn_civilian_mask_filter_condition', 50).normal('state', 'cbrn_civilian_mask_replacement_demand', 180);
}
function scenario(id, fn) { fn(); report.cases.push({ id, passed: true }); }
const num = x => Number(x) / Number(S);
for (const side of ['before', 'after']) {
  load(side === 'before' ? before : after);
  for (const target of ['military', 'state']) for (const stock of [0, 45, 90]) scenario(`${side}-${target}-service-stock-${stock}`, () => {
    const vm = fixture([0, stock]); const scope = target === 'state' ? 'state' : 'country'; vm.select(scope);
    assert(vm.run(target === 'state' ? 'cbrn_replace_state_civilian_mask_filters' : 'cbrn_replace_military_mask_filters'));
    assert.equal(vm.totalStock(), 0n); // request 90, modeled stock is fully used
    const condition = target === 'state' ? 'cbrn_civilian_mask_filter_condition' : 'cbrn_military_mask_filter_condition';
    assert.equal(vm.get(scope, condition), ticks(side === 'after' ? 50 + stock / 90 * 50 : 50));
    const demand = target === 'state' ? 'cbrn_civilian_mask_replacement_demand' : 'cbrn_mask_replacement_demand';
    assert.equal(vm.get(scope, demand), ticks(side === 'after' ? 180 - stock : 180));
    assert.equal(vm.get('country', 'cbrn_mask_replacement_demand'), ticks(side === 'after' ? 180 - stock : 180));
    if (target === 'military') assert.equal(vm.get('country', 'chemical_readiness'), side === 'after' ? ticks(50 + stock / 90 * 50) * 55n / 100n : ticks('27.5'));
    if (side === 'after' && stock === 90) {
      vm.scoped('country', () => vm.stock([0, 90])); const debits = vm.debits.length;
      assert(vm.run(target === 'state' ? 'cbrn_replace_state_civilian_mask_filters' : 'cbrn_replace_military_mask_filters'));
      assert.equal(vm.totalStock(), ticks(90)); assert.equal(vm.debits.length, debits);
    }
    report.cases.push({ id: `${side}-${target}-observed-${stock}`, filterCondition: num(vm.get(scope, condition)), readiness: num(vm.get('country', 'chemical_readiness')) });
  });
  for (const target of ['military', 'state']) scenario(`${side}-${target}-five-model-oldest-first`, () => {
    const vm = fixture([18, 18, 18, 18, 18]); vm.select(target === 'state' ? 'state' : 'country');
    vm.run(target === 'state' ? 'cbrn_replace_state_civilian_mask_filters' : 'cbrn_replace_military_mask_filters');
    assert.deepEqual(vm.debits.map(d => d.model), equipment); assert.equal(vm.totalStock(), 0n);
    assert.equal(vm.debits.reduce((a, d) => a - Number(d.amount), 0), 90);
  });
  scenario(`${side}-oldest-first-stops-mid-model`, () => {
    const vm = fixture([10, 20, 30, 40, 50]).set('cbrn_mask_stock_debit_requested', 90).set('cbrn_mask_stock_debit_completed', 0);
    vm.run('cbrn_debit_mask_stockpile_oldest_first');
    assert.equal(vm.value('cbrn_mask_stock_debit_completed'), ticks(90)); assert.equal(vm.totalStock(), ticks(60));
    assert.deepEqual(equipment.map(e => num(vm.scopes.get('country').stock.get(e))), [0, 0, 0, 10, 50]);
    assert.deepEqual(vm.debits.map(d => Number(d.amount)), [-10, -20, -30, -30]);
  });
  for (const target of ['military', 'state']) scenario(`${side}-${target}-rapid-filter-service-cost`, () => {
    const vm = fixture([0, 63]); vm.scopes.get('country').tech.add('rapid_filter_replacement'); vm.select(target === 'state' ? 'state' : 'country');
    vm.run(target === 'state' ? 'cbrn_replace_state_civilian_mask_filters' : 'cbrn_replace_military_mask_filters');
    assert.equal(vm.totalStock(), 0n); assert.equal(vm.get(target === 'state' ? 'state' : 'country', target === 'state' ? 'cbrn_civilian_mask_filter_condition' : 'cbrn_military_mask_filter_condition'), ticks(side === 'after' ? 100 : 50));
  });
  scenario(`${side}-civilian-contamination-cost-preserved`, () => {
    const vm = fixture([0, 180]).normal('state', 'cbrn_chemical_contamination', 100); vm.select('state');
    vm.run('cbrn_replace_state_civilian_mask_filters'); assert.equal(vm.totalStock(), 0n);
    assert.equal(vm.get('state', 'cbrn_civilian_mask_filter_condition'), ticks(side === 'after' ? 100 : 50));
  });
  scenario(`${side}-registration-debit-to-damaged-cache`, () => {
    const vm = fixture([20, 480]).normal('country', 'cbrn_reconditionable_mask_cache', 0);
    vm.run('cbrn_complete_population_registration');
    assert.equal(vm.totalStock(), ticks(490)); assert.equal(vm.get('country', 'cbrn_reconditionable_mask_cache'), ticks(side === 'after' ? 10 : 0));
    assert.equal(vm.scopes.get('country').flags.has('cbrn_protection_maintenance_active'), side === 'after');
  });
  for (const material of [0, 200]) for (const branch of [0, 1]) scenario(`${side}-reconditioning-material-${material}-quality-branch-${branch}`, () => {
    const vm = fixture().normal('country', 'cbrn_mask_replacement_demand', 0).normal('country', 'cbrn_reconditionable_mask_cache', material); vm.branch = branch;
    vm.run('cbrn_complete_mask_reconditioning');
    assert.equal(vm.totalStock(), ticks(material ? 90 : 0)); assert.equal(vm.get('country', 'cbrn_reconditionable_mask_cache'), 0n);
    assert.equal(vm.rolls.length, side === 'after' && material > 0 ? 1 : 0);
    if (vm.rolls.length) assert.deepEqual(vm.rolls[0], ['20', '80']);
    assert.equal(vm.events.filter(e => e.id === 'cbrn_protection.2').length, side === 'after' && material > 0 && branch === 0 ? 1 : 0);
    assert.equal(vm.get('country', 'cbrn_reconditioned_batch_size'), ticks(side === 'after' && material > 0 && branch === 0 ? 90 : 0));
    vm.run('cbrn_complete_mask_reconditioning');
    assert.equal(vm.rolls.length, side === 'after' && material > 0 ? 1 : 0); assert.equal(vm.totalStock(), ticks(material ? 90 : 0));
    assert(!vm.vars.has('cbrn_recondition_recovered'), 'outer output still requires its own caller declaration');
  });
  scenario(`${side}-military-issue-competes-with-civilian-service`, () => {
    const vm = fixture([0, 90]).normal('country', 'cbrn_military_issued_mask_basic', 750).normal('country', 'cbrn_military_mask_filter_condition', 100);
    vm.run('cbrn_run_protection_maintenance_cycle');
    assert.equal(vm.get('country', 'cbrn_military_issued_mask_basic'), ticks(side === 'after' ? 840 : 750));
    assert.equal(vm.totalStock(), 0n); assert.equal(vm.get('state', 'cbrn_civilian_mask_filter_condition'), ticks(50));
    const order = vm.trace.map(t => t.name);
    assert.equal(order.indexOf('cbrn_issue_masks_to_field_army') < order.indexOf('cbrn_complete_civilian_filter_replacement_program'), side === 'after');
  });
  for (const threat of [false, true]) scenario(`${side}-historical-reserve-threat-${threat}`, () => {
    const vm = fixture([0, 250]).normal('country', 'cbrn_military_issued_mask_basic', 750).normal('country', 'cbrn_military_mask_filter_condition', 100).normal('country', 'cbrn_historical_1936_replacement_reserve_ratio', '.25');
    vm.scopes.get('country').flags.add('cbrn_historical_1936_force_scaled_protection'); vm.publicThreat = threat;
    vm.run('cbrn_issue_masks_to_field_army');
    assert.equal(vm.get('country', 'cbrn_military_issued_mask_basic'), ticks(threat ? 1000 : 750)); assert.equal(vm.totalStock(), ticks(threat ? 0 : 250));
  });
  scenario(`${side}-issue-increment-not-full-shortage`, () => {
    const vm = fixture([0, 1000]).normal('country', 'cbrn_military_issued_mask_basic', 0).normal('country', 'cbrn_military_mask_filter_condition', 100);
    vm.run('cbrn_issue_masks_to_field_army'); assert.equal(vm.get('country', 'cbrn_military_issued_mask_basic'), ticks(250)); assert.equal(vm.totalStock(), ticks(750));
  });
  scenario(`${side}-annual-twelfth-cycle-and-maintenance-delay`, () => {
    const vm = fixture().normal('country', 'cbrn_protection_maintenance_cycle', 10);
    vm.run('cbrn_run_protection_maintenance_cycle'); assert.equal(vm.get('country', 'cbrn_protection_maintenance_cycle'), ticks(11));
    assert.equal(vm.trace.filter(t => t.name === 'cbrn_apply_annual_mask_storage_loss').length, 0);
    vm.run('cbrn_run_protection_maintenance_cycle'); assert.equal(vm.get('country', 'cbrn_protection_maintenance_cycle'), 0n);
    assert.equal(vm.trace.filter(t => t.name === 'cbrn_apply_annual_mask_storage_loss').length, 1);
    vm.run('cbrn_start_protection_maintenance_job'); vm.run('cbrn_start_protection_maintenance_job');
    assert.deepEqual(vm.events, [{ id: 'cbrn_protection.1', days: '30' }]);
  });
  // No usable-output preseed: wrapper must own storage for its nested read.
  for (const wrapper of ['cbrn_distribute_requested_external_masks_to_state', 'cbrn_distribute_reserved_occupied_masks_to_state', 'cbrn_distribute_reserved_external_masks_to_state']) for (const amount of [0, 60]) scenario(`${side}-${wrapper}-useful-${amount}`, () => {
    const vm = fixture([0, amount]).normal('state', 'cbrn_civilian_mask_crates', 0).normal('state', 'cbrn_civilian_mask_basic_crates', 0).normal('state', 'cbrn_civilian_mask_fit_points', 0).normal('state', 'cbrn_civilian_mask_filter_condition', 100);
    vm.select('state'); vm.hasSupplier = true;
    const occupied = wrapper.includes('occupied'), reserved = wrapper.includes('reserved');
    const prefix = occupied ? 'cbrn_occupied_mask_escrow_' : 'cbrn_external_mask_escrow_';
    if (reserved) { vm.scopes.get('state').flags.add(prefix + 'active'); vm.normal('state', prefix + 'donor', 7).normal('state', prefix + 'basic', amount); vm.stock([]); }
    vm.set('cbrn_distribution_target_fraction', '.5').set('cbrn_distribution_base_cost_mult', 1).set('cbrn_distribution_effectiveness_mult', 1).set('cbrn_distribution_new_filter_condition', 100);
    const proof = occupied ? 'cbrn_reserved_distribution_proof' : 'cbrn_external_distribution_proof'; vm.set(proof, 0);
    vm.run(wrapper);
    assert.equal(vm.value(proof), ticks(side === 'after' && amount > 0 ? 1 : 0));
    assert.equal(vm.get('state', 'cbrn_civilian_mask_crates'), ticks(amount) * S / constants.get('constant:cbrn_mask_distribution.urban_or_capital_cost_mult'));
    assert.equal(vm.aidCredits || 0, !occupied && side === 'after' && amount > 0 ? 1 : 0);
    assert.equal(vm.totalStock(), 0n);
    if (reserved) { assert.equal(vm.get('state', prefix + 'basic'), 0n); assert(vm.trace.some(t => t.name === (occupied ? 'cbrn_refund_occupied_state_mask_reservation' : 'cbrn_refund_external_state_mask_reservation'))); }
    // Newly created public output dies after wrapper return, so outer callers
    // that read it must still declare storage independently.
    assert(!vm.vars.has('cbrn_distribution_usable_crates'));
  });
}
// Unchanged helper lifetime remains pessimistic even in the subclass.
scenario('bare-debit-output-dies-without-outer-declaration', () => {
  const vm = fixture([0, 9]).set('cbrn_mask_stock_debit_requested', 9);
  vm.run('cbrn_debit_mask_stockpile_oldest_first'); assert(!vm.vars.has('cbrn_mask_stock_debit_completed')); assert.equal(vm.totalStock(), 0n);
});
scenario('caller-declared-debit-output-survives', () => {
  const vm = fixture([0, 9]).set('cbrn_mask_stock_debit_requested', 9).set('cbrn_mask_stock_debit_completed', 999);
  vm.run('cbrn_debit_mask_stockpile_oldest_first'); assert.equal(vm.value('cbrn_mask_stock_debit_completed'), ticks(9));
});
report.passedCases = report.cases.filter(c => c.passed).length;
fs.writeFileSync(path.join(__dirname, 'source_test_results.json'), JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({ passedCases: report.passedCases, failed: 0, sourceHashes: report.sourceHashes }, null, 2));
