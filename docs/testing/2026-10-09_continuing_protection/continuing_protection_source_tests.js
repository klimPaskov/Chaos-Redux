// Actual production ASTs under explicitly modeled native scope/stock/time/RNG.
// Reuse the existing parser and unchanged conservative VM.run cleanup.
const fs = require('node:fs'), path = require('node:path'), assert = require('node:assert/strict'), sandbox = require('node:vm'), crypto = require('node:crypto');
const base = require('../../plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
const { VM, S, ticks, parse, definitions, constants, root } = base;
// Reuse the previous bounded native scope/stock adapter without running its
// scenarios, changing its source or weakening its helper lexical cleanup.
const previousDir = path.join(root, 'docs/testing/2026-10-09_automatic_protection_repair');
const previous = fs.readFileSync(path.join(previousDir, 'automatic_protection_source_tests.js'), 'utf8').split("for (const side of ['before', 'after'])")[0];
const moduleBox = { exports: {} };
sandbox.runInNewContext(previous + '\nmodule.exports = { ProtectionVM, fixture };', { require, module: moduleBox, __dirname: previousDir });
const { ProtectionVM } = moduleBox.exports;
const paths = ['common/scripted_effects/cbrn_chemical_state_effects.txt', 'events/cbrn_chemical_delivery_events.txt', 'common/scripted_effects/cbrn_immediate_response_cost_effects.txt', 'common/on_actions/chaosx_on_actions.txt', 'common/scripted_effects/cbrn_protection_effects.txt', 'common/decisions/cbrn_protection_decisions.txt', 'common/scripted_triggers/cbrn_protection_triggers.txt', 'common/scripted_triggers/cbrn_immediate_response_cost_triggers.txt'];
const frozen = paths.map(p => fs.readFileSync(path.join(__dirname, path.basename(p) + '.before')));
const current = paths.map(p => fs.readFileSync(path.join(root, p)));
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const report = { cases: [], assumptions: ['Native scope, stock, timing, fixed-point rounding and random inputs are modeled, not engine execution.', 'Hospital order tests execute production order/gate/payment AST with an explicitly modeled ordinary quote and native receipt settlement boundary.', 'Generic deaths execute the actual percentage/RNG/cap AST and observe its register_deaths boundary without executing unrelated global history/UI.', 'Current stock, fitting, filter and controller inputs are sampled discretely at each due tick for both medical passes.'], sourceHashes: paths.map((p, i) => ({ path: p, before: sha(frozen[i]), after: sha(current[i]) })) };
report.rootBindings = { stateEvents: 0, stateHelpers: 0, paidOutcomes: 0, paidOrders: 0, controlCallbacks: 0, rootValues: 0, rootVariableReads: 0, rootScopeEntries: 0 };
report.assumptions.push('State-event ROOT is STATE throughout nested controller scopes. Paid-decision ROOT is payer COUNTRY. Control callback ROOT is new-controller COUNTRY. Temporary variables stay unscoped.');
report.sourceHashes.push({ path: 'common/scripted_effects/cbrn_continuing_protection_effects.txt', before: null, after: sha(fs.readFileSync(path.join(root, 'common/scripted_effects/cbrn_continuing_protection_effects.txt'))) });
report.dependencies = ['docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js', 'docs/testing/2026-10-09_automatic_protection_repair/automatic_protection_source_tests.js', 'common/scripted_effects/cbrn_protection_effects.txt', 'common/scripted_effects/cbrn_protection_decision_effects.txt', 'common/scripted_effects/cbrn_designer_effects.txt', 'common/scripted_effects/chaos_meter_effects.txt', 'common/scripted_triggers/cbrn_triggers.txt', 'common/scripted_triggers/cbrn_protection_triggers.txt', 'common/scripted_triggers/cbrn_immediate_response_cost_triggers.txt', ...fs.readdirSync(path.join(root, 'common/script_constants')).filter(p => p.startsWith('cbrn_') || p.startsWith('chaos_meter') || p.startsWith('chaosx_universal_cost')).map(p => 'common/script_constants/' + p)].map(p => ({path:p,sha256:sha(fs.readFileSync(path.join(root,p)))}));
const beforeOrder = parse(frozen[2].toString()).find(n => n.key === 'cbrn_execute_hospital_response_order');
const afterOrder = parse(current[2].toString()).find(n => n.key === 'cbrn_execute_hospital_response_order');
const rewriteOrdinaryInputs = nodes => nodes.map(n => ({ ...n, value: Array.isArray(n.value) ? rewriteOrdinaryInputs(n.value) : n.value === 'FROM.cbrn_response_hospital_mask_cost' ? 'cbrn_hospital_ordinary_masks' : n.value === 'FROM.cbrn_response_hospital_support_cost' ? 'cbrn_hospital_ordinary_support' : n.value }));
const expectedOrder = { ...beforeOrder, value: rewriteOrdinaryInputs(beforeOrder.value) };
expectedOrder.value.splice(1,0,...parse('set_temp_variable = { cbrn_hospital_ordinary_masks = constant:cbrn_math.zero } set_temp_variable = { cbrn_hospital_ordinary_support = constant:cbrn_math.zero }'));
assert.deepEqual(afterOrder, expectedOrder, 'only two caller declarations and authorized ordinary receipt/achievement inputs change the existing order');
const removeControlHook = nodes => nodes.filter(n => n.key !== 'cbrn_end_active_hospital_protection').map(n => ({...n, value: Array.isArray(n.value) ? removeControlHook(n.value) : n.value}));
assert.deepEqual(removeControlHook(parse(current[3].toString())), parse(frozen[3].toString()), 'all other shared callbacks, refunds and guards preserved');
report.preservedASTs = ['hospital order except two ordinary declarations and exact ordinary receipt/achievement inputs', 'shared on_actions except exact authorized transfer hook'];
for (const f of ['common/script_constants/chaos_meter_constants.txt', 'common/script_constants/chaos_meter_state_death_constants.txt']) {
  if (!fs.existsSync(path.join(root, f))) continue;
  let text = fs.readFileSync(path.join(root, f), 'utf8');
  for (let m; (m = /\bschema\s*=\s*\{/.exec(text));) { let i = m.index + m[0].length, depth = 1; while (depth) { const c = text[i++]; depth += (c === '{') - (c === '}'); } text = text.slice(0, m.index) + text.slice(i); }
  const walk = (nodes, prefix = []) => nodes.forEach(n => {
    if (!prefix.length && !['chaos_meter_state_death_dynamic', 'chaos_meter_deaths', 'chaos_meter_deaths_reason'].includes(n.key)) return;
    if (Array.isArray(n.value)) walk(n.value, [...prefix, n.key]);
    else if (/^-?\d+(\.\d+)?$/.test(n.value)) {
      // Some unused legacy fractional-rate constants have six decimals.
      // Mark them unavailable rather than silently rounding authored tuning.
      if (n.value.includes('.') && n.value.split('.')[1].length > 5) return;
      constants.set('constant:' + [...prefix, n.key].join('.'), ticks(n.value));
    }
  });
  walk(parse(text));
}
function load(side) {
  for (const p of ['common/scripted_effects/cbrn_protection_effects.txt', 'common/scripted_effects/cbrn_protection_decision_effects.txt', 'common/scripted_effects/cbrn_designer_effects.txt', 'common/scripted_effects/chaos_meter_effects.txt', 'common/scripted_triggers/cbrn_triggers.txt', 'common/scripted_triggers/cbrn_protection_triggers.txt', 'common/scripted_triggers/cbrn_immediate_response_cost_triggers.txt']) {
    for (const n of parse(fs.readFileSync(path.join(root, p), 'utf8'))) if (Array.isArray(n.value)) definitions.set(n.key, n.value);
  }
  for (const n of parse(fs.readFileSync(path.join(root, 'common/scripted_effects/cbrn_continuing_protection_effects.txt'), 'utf8'))) { if (side === 'after') definitions.set(n.key, n.value); else definitions.delete(n.key); }
  const buffers = side === 'before' ? frozen : current;
  buffers.forEach((b, i) => {
    const nodes = parse(b.toString());
    if (i === 1) {
      for (const n of nodes.filter(n => n.key === 'state_event')) { const id = n.value.find(n => n.key === 'id').value; definitions.set(id, n.value.find(n => n.key === 'immediate').value); }
    } else if (i === 3) definitions.set('control_callback', nodes[0].value.find(n => n.key === 'on_state_control_changed').value.find(n => n.key === 'effect').value);
    else if (i === 5) { /* public decision blocks are loaded explicitly below */ }
    else for (const n of nodes) if (Array.isArray(n.value)) definitions.set(n.key, n.value);
  });
}
class ContinuingVM extends ProtectionVM {
  constructor() { super(); this.day = 1000; this.draws = 0; this.losses = []; this.dynamic = new Map(); this.flagExpiry = new Map(); this.worldAllowed = true; this.burn = false; this.terminal = false; this.quotes = 0; this.receiptSuccess = true; this.pp = ticks(100); this.inControl = false; this.rootScope = 'state'; }
  scopeId(scope) { assert(['state','country','old_country'].includes(scope)); return ticks(scope === 'state' ? 8 : scope === 'country' ? 7 : 9); }
  rooted(scope, kind, fn) {
    const previousRoot = this.rootScope; this.rootScope = scope; report.rootBindings[kind]++;
    assert.equal(this.value('ROOT'), this.scopeId(scope));
    try { return fn(); } finally { assert.equal(this.rootScope, scope, 'nested scopes must not rebind ROOT'); this.rootScope = previousRoot; }
  }
  value(token) {
    if (token === 'ROOT') { report.rootBindings.rootValues++; return this.scopeId(this.rootScope); }
    if (token === 'THIS') return this.scopeId(this.scope);
    if (token === 'PREV') return this.scopeId(this.previous);
    if (token.startsWith('ROOT.')) {
      report.rootBindings.rootVariableReads++; const name = token.slice(5), target = this.scopes.get(this.rootScope);
      // Scoped reads resolve normal variables/native inputs, never unscoped
      // temporary storage merely because its name matches a scoped token.
      return target.native.get(name) ?? target.vars.get(name) ?? 0n;
    }
    if (token === 'global.num_days') return ticks(this.day);
    if (token.startsWith('FROM.')) { const target=this.scopes.get(this.inControl ? 'old_country' : 'state'), name=token.slice(5); return target.native.get(name) ?? target.vars.get(name) ?? 0n; }
    if (token.startsWith('var:') && !token.startsWith('var:cbrn_occupied') && !token.startsWith('var:cbrn_external')) return super.value(token.slice(4));
    return super.value(token);
  }
  run(name, allow = false) {
    if (['cbrn_refresh_country_civilian_decontamination_pool', 'cbrn_refresh_state_civilian_decontamination_snapshot'].includes(name)) return VM.prototype.run.call(this, name, allow);
    if (name === 'cbrn_calculate_action_protection') { (this.protectionInputs ||= []).push(this.value('cbrn_protection_medical')); }
    if (name === 'cbrn_designer_has_burn_treatment') return this.burn;
    if (name === 'fallout_world_rewrite_callbacks_are_allowed') return this.worldAllowed;
    if (['cbrn_achievement_record_state_medical_response', 'cbrn_achievement_record_nerve_episode_deaths', 'black_friday_record_achievement_transaction'].includes(name)) return true;
    if (name === 'black_friday_allocate_owner_transaction') { this.write('black_friday_owner_transaction_id', ticks(1)); return true; }
    if (name === 'universal_cost_settle_transaction') { this.write('universal_cost_settle_transaction_result', constants.get('constant:universal_cost_framework.' + (this.receiptSuccess ? 'result_success' : 'result_rejected'))); return true; }
    if (name === 'universal_cost_pay_component') {
      const kind = this.value('universal_cost_payment_resource_kind'), amount = this.value('universal_cost_payment_amount');
      const entry = [...constants].find(([key, value]) => key.startsWith('constant:universal_cost_resource_kind.') && value === kind); assert(entry);
      const resource = entry[0].split('.').pop();
      if (resource === 'political_power') { assert(this.pp >= amount); this.pp -= amount; }
      else { const stock = this.scopes.get('country').stock; assert((stock.get(resource) || 0n) >= amount); stock.set(resource, stock.get(resource) - amount); }
      this.write('universal_cost_payment_result', constants.get('constant:universal_cost_framework.result_success')); return true;
    }
    if (name === 'universal_cost_record_transaction') { this.write('universal_cost_record_transaction_result', constants.get('constant:universal_cost_framework.result_success')); return true; }
    if (name === 'cbrn_quote_immediate_response_component') {
      this.quotes++; const amount = this.value('cbrn_response_component_ordinary'), kind = this.value('cbrn_response_component_kind');
      let reserve = ticks(1000000);
      if (kind === constants.get('constant:universal_cost_resource_kind.political_power')) reserve = this.pp;
      if (kind === constants.get('constant:universal_cost_resource_kind.support_equipment_1')) reserve = this.scopes.get('country').stock.get('support_equipment_1') || 0n;
      this.write('cbrn_response_component_quoted', amount); this.write('cbrn_response_component_valid', ticks(1)); this.write('cbrn_response_component_source', ticks(0)); this.write('cbrn_response_component_affordable', reserve >= amount ? ticks(1) : 0n); return true;
    }
    if (name === 'chaos_meter_register_deaths') { this.losses.push(this.value('chaos_deaths_change')); return true; }
    return super.run(name, allow);
  }
  eval(nodes) {
    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i], k = n.key, v = n.value, f = (key, fallback) => this.field(v, key, fallback);
      if (['has_country_flag','set_country_flag','has_tech','has_doctrine','has_equipment','add_equipment_to_stockpile','has_idea'].includes(k)) assert(['country','old_country'].includes(this.scope), `${k} needs a country scope, found ${this.scope} with ROOT=${this.rootScope}`);
      if (['has_state_flag','set_state_flag','clr_state_flag'].includes(k)) assert.equal(this.scope,'state', `${k} needs STATE`);
      if (k === 'if') { const chain = [n]; while (nodes[i + 1] && ['else', 'else_if'].includes(nodes[i + 1].key)) chain.push(nodes[++i]); if (!super.eval(chain)) return false; }
      else if (k === 'ROOT') { report.rootBindings.rootScopeEntries++; const bound = this.rootScope; if (!this.scoped(bound, () => { assert.equal(this.scope, bound); assert.equal(this.value('THIS'), this.value('ROOT')); return this.eval(v); })) return false; }
      else if (k === 'FROM' || k === 'FROM.FROM') { if (!this.scoped(k === 'FROM' && this.inControl ? 'old_country' : 'state', () => this.eval(v))) return false; }
      else if (k === 'CONTROLLER') { if (!this.scoped('country', () => this.eval(v))) return false; }
      else if (k === 'event_target:cbrn_old_state_controller' || k === 'event_target:cbrn_new_state_controller') { if (!this.scoped(k.includes('old') ? 'old_country' : 'country', () => this.eval(v))) return false; }
      else if ((k === 'every_controlled_state' || k === 'any_controlled_state') && this.scope === 'old_country') { if (k.startsWith('any')) return false; }
      else if (k === 'for_each_loop') {
        const name = f('array'), values = [...this.array(name)], key = f('value'), index = f('index'), stop = f('break', 'break');
        for (let j = 0; j < values.length && this.value(stop) === 0n; j++) { if (key) this.write(key, values[j]); if (index) this.write(index, ticks(j)); if (!this.eval(v.filter(n => !['array', 'value', 'index', 'break', 'tooltip'].includes(n.key)))) return false; }
        assert.deepEqual(this.array(name), values, 'traversed array must not mutate');
      } else if (k === 'infrastructure') { if (!(n.op === '>' ? 5 > Number(v) : 5 < Number(v))) return false; }
      else if (k === 'has_state_category') { if (v !== 'rural') return false; }
      else if (k === 'has_state_flag') { if (!this.scopes.get('state').flags.has(v) || (this.flagExpiry.has(v) && this.flagExpiry.get(v) <= this.day)) return false; }
      else if (k === 'set_state_flag') { const name = Array.isArray(v) ? f('flag') : v; this.scopes.get('state').flags.add(name); if (Array.isArray(v) && f('days')) this.flagExpiry.set(name, this.day + Number(this.value(f('days')) / S)); }
      else if (k === 'clr_state_flag') { this.scopes.get('state').flags.delete(v); this.flagExpiry.delete(v); }
      else if (k === 'has_dynamic_modifier') { const id = Array.isArray(v) ? f('modifier') : v; if (!this.dynamic.has(id) || this.dynamic.get(id) <= this.day) return false; }
      else if (k === 'add_dynamic_modifier') this.dynamic.set(f('modifier'), this.day + Number(this.value(f('days', '1000000')) / S));
      else if (k === 'remove_dynamic_modifier') this.dynamic.delete(f('modifier'));
      else if (k === 'has_idea') { if (!(v === 'cbrn_terminal_hazard_doctrine_spirit' && this.terminal)) return false; }
      else if (k === 'set_temp_variable_to_random') { this.draws++; this.write(f('var'), ticks('.5')); }
      else if (k === 'state_event') this.events.push({ id: f('id'), days: String(this.value(f('days')) / S) });
      else if (['cbrn_designer_has_burn_treatment', 'fallout_world_rewrite_callbacks_are_allowed', 'cbrn_achievement_record_state_medical_response', 'cbrn_achievement_record_nerve_episode_deaths', 'black_friday_record_achievement_transaction', 'black_friday_allocate_owner_transaction', 'universal_cost_settle_transaction', 'universal_cost_pay_component', 'universal_cost_record_transaction', 'cbrn_quote_immediate_response_component', 'chaos_meter_register_deaths'].includes(k)) { const yes = this.run(k); if ((v === 'no' && yes) || (v !== 'no' && !yes)) return false; }
      else if (!super.eval([n])) return false;
    }
    return true;
  }
  paid(day) { this.day = day; return this.rooted('country','paidOutcomes',() => this.scoped('state', () => this.run('cbrn_complete_paid_hospital_response'))); }
  interval(side, day) { return this.paid(day); }
  order() { return this.rooted('country','paidOrders',() => { this.select('country'); return this.run('cbrn_execute_hospital_response_order'); }); }
  tick(day) { this.day = day; return this.rooted('state','stateEvents',() => { this.select('state'); this.run('cbrn_delivery.4'); }); }
  scalar(day) { this.day = day; return this.rooted('state','stateHelpers',() => { this.select('state'); this.set('chaos_state_deaths_mult', 1); this.write('chaos_state_deaths_percent', this.get('state','cbrn_chemical_continuing_death_rate')); this.run('cbrn_apply_continuing_civilian_protection'); return this.value('chaos_state_deaths_mult'); }); }
  control(day) { this.day = day; const c = this.scopes.get('country'); this.scopes.set('old_country', { vars: new Map(c.vars), flags: new Set(c.flags), tech: new Set(c.tech), stock: new Map(c.stock), native: new Map(c.native) }); return this.rooted('country','controlCallbacks',() => { this.select('country'); this.inControl = true; try { this.run('control_callback'); } finally { this.inControl = false; } }); }
}
function fixture(cls = 1, fraction = '1', model = 'sealed', med = 50, kitStock = 10000) {
  const vm = new ContinuingVM(); vm.scopes.get('state').native.set('state_population_k', ticks(10000));
  vm.scopes.get('country').stock.set('decontamination_equipment', ticks(kitStock)); vm.scopes.get('country').tech.add('field_decontamination_kits');
  vm.normal('country', 'cbrn_medical_capacity', med).normal('country', 'cbrn_decontamination_capacity', 100).normal('country', 'cbrn_military_mask_filter_condition', 100).normal('country', 'cbrn_military_issued_mask_basic', 1000);
  const crates = ticks(10000) * ticks(fraction) / S; vm.scopes.get('state').vars.set('cbrn_civilian_mask_' + model + '_crates', crates); vm.scopes.get('state').vars.set('cbrn_civilian_mask_fit_points', crates); vm.scopes.get('state').vars.set('cbrn_civilian_mask_crates', crates);
  vm.normal('state', 'cbrn_civilian_mask_filter_condition', 100).normal('state', 'cbrn_chemical_contamination', 100).normal('state', 'cbrn_chemical_contamination_class', 5).normal('state', 'cbrn_last_chemical_agent_class', cls).normal('state', 'cbrn_chemical_contamination_expiry_day', 2000).normal('state', 'cbrn_chemical_continuing_death_due_day', 1030);
  vm.dynamic.set('chem_state_contamination', 2000);
  vm.scoped('state', () => vm.run('cbrn_chemical_refresh_continuing_death_profile'));
  return vm;
}
function test(id, fn) { fn(); report.cases.push({ id, passed: true }); }
const arr = (vm, name) => vm.array('cbrn_hospital_protection_' + name + '_days').map(x => Number(x / S));
// Independent binding probes prevent the reused adapter from passing cases by
// silently treating a state ROOT as the country used by payment/control paths.
report.rootBindingProbes = [];
for (const binding of ['state_event', 'paid_decision', 'control_callback']) {
  const vm = new ContinuingVM(), bound = binding === 'state_event' ? 'state' : 'country';
  vm.scopes.set('old_country', { vars: new Map([['root_probe',ticks(33)]]), flags: new Set(), tech: new Set(), stock: new Map(), native: new Map() });
  vm.normal('state','root_probe',22).normal('country','root_probe',11).set('root_probe_temp',37); vm.select('state');
  vm.rooted(bound,binding === 'state_event' ? 'stateHelpers' : binding === 'paid_decision' ? 'paidOrders' : 'controlCallbacks',() => {
    assert.equal(vm.value('ROOT'),ticks(bound === 'state' ? 8 : 7));
    assert.equal(vm.value('ROOT.root_probe'),ticks(bound === 'state' ? 22 : 11));
    assert.equal(vm.value('ROOT.root_probe_temp'),0n,'ROOT prefix must not resolve an unscoped temporary');
    vm.scoped(binding === 'control_callback' ? 'old_country' : 'country',() => {
      assert.equal(vm.value('ROOT.root_probe'),ticks(bound === 'state' ? 22 : 11),'nested country scope retains event ROOT');
      assert(vm.eval(parse('ROOT = { set_variable = { root_probe_written = 44 } }')));
    });
    assert.equal(vm.get(bound,'root_probe_written'),ticks(44));
    assert.equal(vm.get(bound === 'state' ? 'country' : 'state','root_probe_written'),0n);
    assert.equal(vm.get('old_country','root_probe_written'),0n);
  });
  report.rootBindingProbes.push({binding,root:bound,passed:true});
}
{
  const vm = new ContinuingVM(); vm.select('state');
  assert.throws(() => vm.rooted('state','stateHelpers',() => vm.eval(parse('ROOT = { has_country_flag = root_country_probe }'))), /needs a country scope/);
  report.rootBindingProbes.push({binding:'state_ROOT_rejects_country_only_flag',root:'state',passed:true});
}
for (const side of ['before', 'after']) {
  load(side);
  for (const cls of [1, 2, 3, 4]) for (const [id, fraction, model] of [['zero', '0', 'basic'], ['partial', '.25', 'basic'], ['full_basic', '1', 'basic'], ['full_sealed', '1', 'sealed']]) test(`${side}-${cls}-${id}-standard-first-hospital-expired-before-tick`, () => {
    const vm = fixture(cls, fraction, model); vm.paid(1000); assert.equal(vm.flagExpiry.get('cbrn_hospitals_utilities_secured'), 1014); const stocks = [...vm.scopes.get('country').stock]; const pp = vm.pp;
    vm.tick(1030); assert.equal(vm.draws, 2); assert.equal(vm.get('state', 'cbrn_chemical_continuing_death_due_day'), ticks(1060)); assert.deepEqual([...vm.scopes.get('country').stock], stocks); assert.equal(vm.pp, pp);
    if (side === 'after') assert.deepEqual(arr(vm, 'start'), []);
    report.cases.push({ id: `${side}-${cls}-${id}-loss`, deaths: Number(vm.losses[0] / S) });
  });
}
load('after');
for (const side of ['before', 'after']) for (const fraction of ['0', '1']) for (const allowed of [true, false]) test(`${side}-control-mask-${fraction}-world-callbacks-${allowed}`, () => {
  load(side); const vm = fixture(1, fraction); vm.worldAllowed = allowed; vm.paid(1000); vm.control(1007);
  if (side === 'after') { assert.deepEqual(arr(vm, 'end'), [1007]); assert(!vm.scopes.get('state').flags.has('cbrn_hospitals_utilities_secured')); if (!allowed) assert(!vm.trace.some(t => t.name === 'cbrn_transfer_state_civilian_mask_ledger')); }
  else if (allowed && fraction === '0') assert(vm.scopes.get('state').flags.has('cbrn_hospitals_utilities_secured'), 'original zero-mask branch lacked hospital cleanup');
  const stock = [...vm.scopes.get('country').stock]; vm.control(1007); assert.deepEqual([...vm.scopes.get('country').stock], stock);
});
load('after');
for (const side of ['before','after']) for (const masks of [29, 30, 31]) test(`${side}-actual-order-mask-stock-${masks}`, () => {
  load(side);
  const vm = fixture(); vm.normal('state', 'cbrn_response_hospital_mask_cost', 30).normal('state', 'cbrn_response_hospital_support_cost', 20);
  vm.scopes.get('state').native.set('state_population_k',ticks(1000));
  vm.scopes.get('state').flags.add('cbrn_chemical_raid_alert_active'); vm.scopes.get('country').stock.set('gas_mask_equipment_1', ticks(masks)); vm.scopes.get('country').stock.set('support_equipment_1', ticks(20));
  vm.order();
  assert.deepEqual(arr(vm, 'start'), side==='before'||masks < 30 ? [] : [1000]); assert.equal(vm.scopes.get('country').stock.get('gas_mask_equipment_1'), ticks(masks < 30 ? masks : masks - 30)); assert.equal(vm.pp, ticks(masks < 30 ? 100 : 90));
});
load('after');
for (const cls of [1, 2, 3, 4]) test(`hospital-authored-full-sealed-threshold-${cls}`, () => {
  const vm = fixture(cls); vm.select('state'); for (const name of ['cbrn_continuing_mask_only_mult', 'cbrn_continuing_without_hospital_mult', 'cbrn_continuing_with_hospital_mult']) vm.set(name, 0);
  vm.run('cbrn_calculate_continuing_civilian_protection'); const M = vm.value('cbrn_continuing_mask_only_mult');
  assert.equal(M, ticks(['.12', '.42', '.32', '.20'][cls - 1])); assert.equal(vm.value('cbrn_continuing_without_hospital_mult'), M); assert.equal(vm.value('cbrn_continuing_with_hospital_mult'), M / 2n);
});
test('registration-merges-union-and-retains-cross-period-service', () => {
  const vm = fixture(); vm.paid(1000); vm.paid(1005); vm.paid(1019); assert.deepEqual(arr(vm, 'start'), [1000]); assert.deepEqual(arr(vm, 'end'), [1033]);
  vm.tick(1030); assert.deepEqual(arr(vm, 'start'), [1030]); assert.deepEqual(arr(vm, 'end'), [1033]); vm.tick(1060); assert.deepEqual(arr(vm, 'start'), []);
});
for (const [id, days, expected] of [['preexposure', [993], '7'], ['multiple', [1000, 1020], '24'], ['duplicate', [1000, 1000], '14'], ['cross_period', [1025], '5']]) test(`overlap-${id}`, () => {
  const vm = fixture(); days.forEach(d => vm.paid(d)); vm.select('state'); vm.set('cbrn_continuing_window_start', 1000).set('cbrn_continuing_window_end', 1030).set('cbrn_continuing_hospital_fraction', 0); vm.run('cbrn_measure_hospital_protection_overlap');
  assert.equal(vm.value('cbrn_continuing_hospital_fraction'), ticks(expected) * S / ticks(30));
});
test('old-idle-history-prunes-at-registration', () => {
  const vm = fixture(); vm.paid(1000); vm.normal('state', 'cbrn_chemical_continuing_death_due_day', 1100); vm.paid(1090); assert.deepEqual(arr(vm, 'start'), [1090]); assert.deepEqual(arr(vm, 'end'), [1104]);
});
test('late-pending-window-not-discarded-by-a-later-registration', () => {
  const vm = fixture(); vm.paid(1000); vm.paid(1032); assert.equal(arr(vm, 'start')[0], 1000); vm.tick(1032); assert.deepEqual(arr(vm, 'start'), [1032]); assert.deepEqual(arr(vm, 'end'), [1046]);
});
test('combined-burn-and-current-terminal-share-one-budget', () => {
  const vm = fixture(2); vm.burn = true; vm.terminal = true; vm.paid(1000); vm.paid(1014); vm.paid(1028); const actual = vm.scalar(1030);
  assert.equal(actual, ticks('.21')); assert.equal(vm.value('chaos_state_deaths_percent'), ticks('.0165')); assert.equal(vm.get('state', 'cbrn_chemical_continuing_death_rate'), ticks('.015'));
  vm.terminal = false; assert.equal(vm.scalar(1030), ticks('.21')); vm.burn = false; assert.equal(vm.scalar(1030), ticks('.21'));
});
test('calculator-preserves-inherited-enum-inputs-and-results', () => {
  const vm = fixture(); vm.select('state'); const keys = ['cbrn_action_agent_class', 'cbrn_protection_medical', 'cbrn_protection_respiratory', 'cbrn_action_casualty_mult', 'cbrn_action_mask_only_casualty_mult', 'cbrn_action_disruption_mult']; keys.forEach((k, i) => vm.set(k, i + 1));
  vm.scalar(1030); keys.forEach((k, i) => assert.equal(vm.value(k), ticks(i + 1)));
});
test('bare-timed-flag-never-invents-paid-time', () => {
  const vm = fixture(); vm.scopes.get('state').flags.add('cbrn_hospitals_utilities_secured'); vm.flagExpiry.set('cbrn_hospitals_utilities_secured', 1040); assert.equal(vm.scalar(1030), ticks('.12'));
});
test('duplicate-callback-has-no-extra-loss-or-draw-or-receiver', () => {
  const vm = fixture(); vm.paid(1000); vm.tick(1030); const losses = [...vm.losses], draws = vm.draws, events = [...vm.events]; vm.tick(1030); assert.deepEqual(vm.losses, losses); assert.equal(vm.draws, draws); assert.deepEqual([...vm.events], events);
});
test('early-callback-preserves-future-due-and-pending-receiver', () => { const vm = fixture(); vm.tick(1029); assert.equal(vm.losses.length, 0); assert.equal(vm.draws, 0); assert.equal(vm.get('state', 'cbrn_chemical_continuing_death_due_day'), ticks(1030)); assert.equal(vm.events.length, 0); });
test('expired-contamination-registers-no-loss-and-cleans-idle-time', () => { const vm = fixture(); vm.paid(900); vm.normal('state', 'cbrn_chemical_contamination_expiry_day', 1000); vm.tick(1030); assert.equal(vm.losses.length, 0); assert.equal(vm.draws, 0); assert.deepEqual(arr(vm, 'start'), []); });
test('disabled-deaths-consume-completed-care-without-loss-or-later-credit', () => { const vm = fixture(); vm.paid(1000); vm.flags.add('settings_chaos_deaths_disabled'); vm.tick(1030); assert.equal(vm.losses.length, 0); assert.equal(vm.draws, 0); assert.deepEqual(arr(vm, 'start'), []); vm.flags.delete('settings_chaos_deaths_disabled'); assert.equal(vm.scalar(1060), ticks('.12')); });
test('private-break-inputs-reset-and-unrelated-cursor-survives', () => { const vm = fixture(); vm.set('break', 1).set('cbrn_hospital_history_break', 1).set('cbrn_hospital_overlap_break', 1).set('outer_cursor', 19); vm.paid(1000); assert.equal(vm.scalar(1030) > 0n, true); assert.equal(vm.value('break'), ticks(1)); assert.equal(vm.value('outer_cursor'), ticks(19)); });
test('zero-kit-stock-does-not-create-advanced-hospital-protection', () => { const vm = fixture(1, '1', 'sealed', 50, 0); vm.paid(1000); vm.paid(1014); vm.paid(1028); assert.equal(vm.scalar(1030), ticks('.12')); assert.equal(vm.get('state', 'cbrn_civilian_decontamination_allocated_kits'), 0n); });
test('shortage-masks-and-filters-remain-real-snapshot-inputs', () => { const vm = fixture(1, '.25', 'basic'); vm.normal('state', 'cbrn_civilian_mask_filter_condition', 0); assert.equal(vm.scalar(1030), ticks(1)); assert.equal(vm.get('state', 'cbrn_civilian_mask_coverage'), 0n); });
test('mismatched-paired-history-never-grants-or-destroys-time', () => { const vm = fixture(); vm.arrays.set('cbrn_hospital_protection_start_days', [ticks(1000)]); vm.arrays.set('cbrn_hospital_protection_end_days', []); const starts = [...vm.array('cbrn_hospital_protection_start_days')]; assert.equal(vm.scalar(1030), ticks('.12')); vm.select('state'); vm.run('cbrn_prune_idle_hospital_protection_history'); assert.deepEqual(vm.array('cbrn_hospital_protection_start_days'), starts); });
test('sorted-overlapping-receipts-count-union-once', () => { const vm = fixture(); vm.arrays.set('cbrn_hospital_protection_start_days', [ticks(1000), ticks(1005), ticks(1020)]); vm.arrays.set('cbrn_hospital_protection_end_days', [ticks(1014), ticks(1019), ticks(1034)]); vm.select('state'); vm.set('cbrn_continuing_window_start', 1000).set('cbrn_continuing_window_end', 1030).set('cbrn_continuing_hospital_fraction', 0); vm.run('cbrn_measure_hospital_protection_overlap'); assert.equal(vm.value('cbrn_continuing_hospital_fraction'), ticks(29) * S / ticks(30)); });
test('idle-cleanup-preserves-paid-time-for-a-later-overlapping-episode', () => { const vm = fixture(); vm.paid(1011); vm.day = 1020; vm.select('state'); vm.regularVars.delete('cbrn_chemical_continuing_death_due_day'); vm.run('cbrn_prune_idle_hospital_protection_history'); assert.deepEqual(arr(vm, 'start'), [1011]); assert.deepEqual(arr(vm, 'end'), [1025]); vm.normal('state', 'cbrn_chemical_continuing_death_due_day', 1052); assert(vm.scalar(1052) < ticks('.12')); });
test('old-episode-callback-does-not-move-new-episode-date', () => { const vm = fixture(); vm.normal('state', 'cbrn_chemical_continuing_death_due_day', 1070); vm.paid(1040); vm.tick(1050); assert.equal(vm.get('state', 'cbrn_chemical_continuing_death_due_day'), ticks(1070)); assert.equal(vm.events.length, 0); assert.deepEqual(arr(vm, 'end'), [1054]); });
for (const med of [0, 50, 90, 100]) for (const active of [false, true]) test(`pre-hospital-base-${med}-flag-${active}-partial-period`, () => { const vm = fixture(1, '1', 'sealed', med); vm.paid(1000); if (active) { vm.scopes.get('state').flags.add('cbrn_hospitals_utilities_secured'); vm.flagExpiry.set('cbrn_hospitals_utilities_secured', 1040); } else vm.flagExpiry.set('cbrn_hospitals_utilities_secured', 1014); vm.scalar(1030); assert.deepEqual(vm.protectionInputs, [ticks(med), ticks(Math.min(med + 25, 100))]); });
test('partial-real-kit-coverage-does-not-become-full-support', () => { const vm = fixture(1, '1', 'sealed', 50, 75); vm.paid(1000); vm.paid(1014); vm.paid(1028); assert.equal(vm.scalar(1030), ticks('.12')); assert.equal(vm.get('state', 'cbrn_civilian_decontamination_protection'), ticks(50)); });
test('insufficient-real-fitting-reduces-mask-foundation', () => { const vm = fixture(); vm.normal('state', 'cbrn_civilian_mask_fit_points', 5000); vm.scalar(1030); assert.equal(vm.get('state', 'cbrn_civilian_mask_coverage'), ticks(50)); assert.equal(vm.get('state', 'cbrn_civilian_respiratory_protection'), ticks(50)); });
test('zero-rate-due-pass-consumes-care-and-keeps-period-without-rng', () => { const vm = fixture(); vm.normal('state', 'cbrn_chemical_continuing_death_rate', 0); vm.paid(1000); vm.tick(1030); assert.equal(vm.losses.length, 0); assert.equal(vm.draws, 0); assert.deepEqual(arr(vm, 'start'), []); assert.equal(vm.get('state', 'cbrn_chemical_continuing_death_due_day'), ticks(1060)); assert.equal(vm.events.length, 1); });
test('zero-population-never-produces-phantom-loss-or-rng', () => { const vm = fixture(); vm.scopes.get('state').native.set('state_population_k', 0n); vm.paid(1000); vm.tick(1030); assert.equal(vm.losses.length, 0); assert.equal(vm.draws, 0); });
for (const verified of [0, 1]) test(`second-raid-alert-verified-${verified}-future-care-matches-reset`, () => { const vm = fixture(); vm.paid(1000); vm.day = 1007; vm.select('state'); vm.set('cbrn_exact_state_alert_verified', verified); vm.run('cbrn_register_exact_state_chemical_raid_alert'); assert.deepEqual(arr(vm,'end'), [verified ? 1007 : 1014]); if (verified) assert(!vm.scopes.get('state').flags.has('cbrn_hospitals_utilities_secured')); else assert(vm.scopes.get('state').flags.has('cbrn_hospitals_utilities_secured')); });
test('central-hospital-clear-without-modifier-still-closes-receipt-once', () => { const vm = fixture(); vm.paid(1000); vm.dynamic.delete('cbrn_hospitals_utilities_protected'); vm.day = 1007; vm.select('state'); vm.run('cbrn_clear_state_raid_dynamic_modifiers'); vm.run('cbrn_clear_state_raid_dynamic_modifiers'); assert.deepEqual(arr(vm,'end'), [1007]); assert(!vm.scopes.get('state').flags.has('cbrn_hospitals_utilities_secured')); });
for (const fromTerminal of [false, true]) test(`terminal-transfer-current-source-${fromTerminal}`, () => {
  const vm = fixture(1, '0', 'basic', 0, 0); vm.terminal = fromTerminal; vm.scoped('state', () => vm.run('cbrn_chemical_refresh_continuing_death_profile')); vm.control(1007); vm.terminal = !fromTerminal;
  assert.equal(vm.get('state', 'cbrn_chemical_continuing_death_rate'), ticks('.009')); assert.equal(vm.scalar(1030), ticks(1)); assert.equal(vm.value('chaos_state_deaths_percent'), ticks(!fromTerminal ? '.0099' : '.009'));
});
for (const cls of [1,2,3,4]) for (const stage of [2,3,4,5]) for (const terminal of [false,true]) test(`matched-unprotected-loss-and-rng-${cls}-${stage}-${terminal}`, () => {
  const outcomes=[];
  for (const side of ['before','after']) { load(side); const vm=fixture(cls,'0','basic',0,0); vm.terminal=terminal; vm.normal('state','cbrn_chemical_contamination_class',stage); vm.scoped('state',()=>vm.run('cbrn_chemical_refresh_continuing_death_profile')); vm.tick(1030); outcomes.push({losses:vm.losses.map(String),draws:vm.draws,due:String(vm.get('state','cbrn_chemical_continuing_death_due_day'))}); }
  assert.deepEqual(outcomes[1],outcomes[0]);
});
load('after');
test('history-pruning-traverses-more-than1000-rows-without-index-shift', () => {
  const vm = fixture(); vm.arrays.set('cbrn_hospital_protection_start_days', Array.from({length:1205},(_,i)=>ticks(i))); vm.arrays.set('cbrn_hospital_protection_end_days', Array.from({length:1205},(_,i)=>ticks(i+1)));
  vm.select('state'); vm.set('cbrn_hospital_history_cutoff',1000).set('cbrn_hospital_history_truncate',1).set('cbrn_hospital_history_end_limit',1010).set('cbrn_hospital_history_break',1).set('cbrn_hospital_history_copy_break',1); vm.run('cbrn_prune_hospital_protection_history'); assert.deepEqual(arr(vm,'start'),Array.from({length:10},(_,i)=>1000+i)); assert.deepEqual(arr(vm,'end'),Array.from({length:10},(_,i)=>1001+i));
});
for (const cls of [1, 2, 3, 4]) test(`matched-first-window-loss-improves-with-real-full-sealed-${cls}`, () => {
  const find = side => report.cases.find(c => c.id === `${side}-${cls}-full_sealed-loss`).deaths;
  assert(find('after') < find('before'));
});
// Public entry and live quote use production ASTs. Only native stock, price
// service and receipt APIs are modeled; the population calculation is real.
class PublicHospitalVM extends ContinuingVM {
  run(name, allow = false) {
    if (name === 'universal_cost_refund_transaction') { this.refundAttempted=true; this.write('universal_cost_refund_transaction_result',constants.get('constant:universal_cost_framework.result_rejected')); this.write('universal_cost_refund_unhandled_total',ticks(60)); return true; }
    if (name === 'cbrn_quote_immediate_response_component') {
      const ordinary = this.value('cbrn_response_component_ordinary');
      const amount = (ordinary + S * BigInt(this.saleDivisor) - 1n) / (S * BigInt(this.saleDivisor)) * S;
      const kind = this.value('cbrn_response_component_kind');
      let reserve = ticks(1000000);
      if (kind === constants.get('constant:universal_cost_resource_kind.political_power')) reserve = this.pp;
      if (kind === constants.get('constant:universal_cost_resource_kind.support_equipment_1')) reserve = this.scopes.get('country').stock.get('support_equipment_1') || 0n;
      this.write('cbrn_response_component_quoted', amount); this.write('cbrn_response_component_valid', ticks(1));
      this.write('cbrn_response_component_source', ticks(this.saleDivisor === 1 ? 0 : 1));
      this.write('cbrn_response_component_affordable', reserve >= amount ? ticks(1) : 0n); return true;
    }
    if (name === 'universal_cost_record_transaction') this.receipts.push({ ordinary: this.value('universal_cost_transaction_ordinary_cost'), paid: this.value('universal_cost_transaction_actual_paid_cost'), member: this.value('universal_cost_transaction_achievement_primary_member') });
    if (name === 'black_friday_record_achievement_transaction') this.purchase = { ordinary: this.value('black_friday_purchase_ordinary_cost'), paid: this.value('black_friday_purchase_actual_paid_cost') };
    return super.run(name, allow);
  }
  eval(nodes) {
    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i];
      if (n.key === 'if') { const chain = [n]; while (nodes[i + 1] && ['else','else_if'].includes(nodes[i + 1].key)) chain.push(nodes[++i]); if (!super.eval(chain)) return false; }
      else if (n.key === 'is_controlled_by') { assert.equal(this.scope, 'state'); assert.equal(n.value, 'ROOT'); if (!this.controlled) return false; }
      else if (['hidden_trigger','hidden_effect'].includes(n.key)) { if (!this.eval(n.value)) return false; }
      else if (n.key === 'custom_effect_tooltip') { /* presentation-only */ }
      else if (!super.eval([n])) return false;
    }
    return true;
  }
  gate(decision, field) { return this.rooted('country','paidOrders',() => this.scoped('country',() => this.eval(decision.value.find(n => n.key === field).value))); }
  displayed(getter) {
    return this.rooted('country','paidOrders',() => this.scoped('country',() => {
      for (const row of getter.value.filter(n => n.key === 'text')) if (this.eval(row.value.find(n => n.key === 'trigger').value)) return row.value.find(n => n.key === 'localization_key').value;
      throw Error('No matching cost text');
    }));
  }
}
const hospitalDecision = side => parse((side === 'before' ? frozen : current)[5].toString()).find(n => n.key === 'cbrn_civil_defence_category').value.find(n => n.key === 'cbrn_protect_hospitals_and_utilities');
const locPath = 'common/scripted_localisation/cbrn_immediate_response_cost_localisation.txt';
const locDefs = parse(fs.readFileSync(path.join(root,locPath),'utf8'));
report.dependencies.push({path:locPath,sha256:sha(fs.readFileSync(path.join(root,locPath)))});
function publicFixture() {
  const vm = fixture(); Object.setPrototypeOf(vm,PublicHospitalVM.prototype);
  vm.controlled = true; vm.saleDivisor = 1; vm.receipts = [];
  vm.scopes.get('state').native.set('state_population_k',ticks(1000));
  vm.scopes.get('country').stock.set('gas_mask_equipment_1',ticks(30));
  vm.scopes.get('country').stock.set('support_equipment_1',ticks(20)); vm.pp = ticks(10);
  assert(!vm.scopes.get('state').vars.has('cbrn_response_hospital_mask_cost'));
  return vm;
}
report.publicEntryCases = [];
for (const side of ['before','after']) for (const scenario of ['contamination','alert','clean','secured','wrong-controller']) test(`public-${side}-${scenario}`,() => {
  load(side); const vm=publicFixture(), decision=hospitalDecision(side);
  if (scenario === 'alert') { vm.scopes.get('state').vars.delete('cbrn_chemical_contamination'); vm.scopes.get('state').flags.add('cbrn_chemical_raid_alert_active'); }
  if (scenario === 'clean') vm.scopes.get('state').vars.delete('cbrn_chemical_contamination');
  if (scenario === 'secured') vm.scopes.get('state').flags.add('cbrn_hospitals_utilities_secured');
  if (scenario === 'wrong-controller') vm.controlled=false;
  const gates=Object.fromEntries(['visible','target_root_trigger','target_trigger','available','custom_cost_trigger'].map(k=>[k,vm.gate(decision,k)]));
  const canPay=side==='after' && ['contamination','alert'].includes(scenario);
  assert.equal(gates.available,canPay); assert.equal(gates.custom_cost_trigger,canPay);
  if (canPay) assert(Object.values(gates).every(Boolean));
  if (scenario==='clean') assert.equal(gates.visible,false);
  if (side==='before' && scenario==='contamination') assert.equal(gates.visible,false);
  vm.order(); assert.equal(vm.pp,ticks(canPay?0:10)); assert.equal(vm.receipts.length,canPay?7:0);
  assert.deepEqual(arr(vm,'start'),canPay?[1000]:[]);
  report.publicEntryCases.push({side,scenario,gates,paid:canPay});
});
load('after');
for (const resource of ['pp','masks','support']) for (const delta of [-1,0,1]) test(`public-live-quote-${resource}-${delta}`,()=>{
  const vm=publicFixture(), decision=hospitalDecision('after');
  if(resource==='pp') vm.pp=ticks(10+delta);
  if(resource==='masks') vm.scopes.get('country').stock.set('gas_mask_equipment_1',ticks(30+delta));
  if(resource==='support') vm.scopes.get('country').stock.set('support_equipment_1',ticks(20+delta));
  const getterName={pp:'GetCbrnHospitalPoliticalCost',masks:'GetCbrnHospitalMaskCost',support:'GetCbrnHospitalSupportCost'}[resource];
  const key=vm.displayed(locDefs.find(n=>n.value.find(x=>x.key==='name')?.value===getterName));
  assert(key.endsWith(delta<0?'_short':'_ready')); assert.equal(vm.gate(decision,'available'),delta>=0); assert.equal(vm.gate(decision,'custom_cost_trigger'),delta>=0);
  const before={pp:vm.pp,masks:vm.scopes.get('country').stock.get('gas_mask_equipment_1'),support:vm.scopes.get('country').stock.get('support_equipment_1')}; vm.order();
  assert.equal(vm.pp,before.pp-(delta>=0?ticks(10):0n)); assert.equal(vm.scopes.get('country').stock.get('gas_mask_equipment_1'),before.masks-(delta>=0?ticks(30):0n)); assert.equal(vm.scopes.get('country').stock.get('support_equipment_1'),before.support-(delta>=0?ticks(20):0n));
  assert.deepEqual(arr(vm,'start'),delta>=0?[1000]:[]);
});
for(const [population,masks,support] of [[0,10,20],[1000,30,20],[1017,31,20],[2051,62,21],[20000,400,200],[50000,400,300]]) test(`public-population-price-${population}`,()=>{
  const vm=publicFixture(); vm.scopes.get('state').native.set('state_population_k',ticks(population));
  vm.normal('state','cbrn_response_hospital_mask_cost',999).normal('state','cbrn_response_hospital_support_cost',999);
  vm.rooted('country','paidOrders',()=>vm.scoped('country',()=>{
    vm.set('cbrn_hospital_ordinary_masks',0).set('cbrn_hospital_ordinary_support',0);
    vm.run('cbrn_quote_hospital_response_bundle'); assert.equal(vm.value('cbrn_hospital_ordinary_masks'),ticks(masks)); assert.equal(vm.value('cbrn_hospital_ordinary_support'),ticks(support));
  }));
});
for(const divisor of [1,2,4]) test(`public-receipts-and-duplicate-${divisor}`,()=>{
  const vm=publicFixture(); vm.saleDivisor=divisor; vm.normal('state','cbrn_response_hospital_mask_cost',999).normal('state','cbrn_response_hospital_support_cost',999);
  vm.order(); assert.deepEqual(vm.purchase,{ordinary:ticks(50),paid:ticks(Math.ceil(30/divisor)+Math.ceil(20/divisor))});
  assert.equal(vm.receipts.filter(r=>r.member===ticks(1)).reduce((a,r)=>a+r.ordinary,0n),ticks(50));
  const paid=vm.pp, count=vm.receipts.length; vm.order(); assert.equal(vm.pp,paid); assert.equal(vm.receipts.length,count); assert.deepEqual(arr(vm,'start'),[1000]);
});
test('public-controller-lost-after-display-refuses-order',()=>{ const vm=publicFixture(); assert(vm.gate(hospitalDecision('after'),'available')); vm.controlled=false; vm.order(); assert.equal(vm.receipts.length,0); assert.equal(vm.pp,ticks(10)); assert.deepEqual(arr(vm,'start'),[]); });
test('public-five-model-payment',()=>{ const vm=publicFixture(),models=['gas_mask_equipment_reconditioned','gas_mask_equipment_1','gas_mask_equipment_2','gas_mask_equipment_3','gas_mask_equipment_4']; [1,2,3,4,20].forEach((n,i)=>vm.scopes.get('country').stock.set(models[i],ticks(n))); vm.order(); models.forEach(k=>assert.equal(vm.scopes.get('country').stock.get(k),0n)); assert.deepEqual(vm.purchase,{ordinary:ticks(50),paid:ticks(50)}); assert.deepEqual(arr(vm,'start'),[1000]); });
test('public-rejected-settlement-and-refund-retain-recovery-without-care',()=>{ const vm=publicFixture(); vm.receiptSuccess=false; vm.order(); assert(vm.refundAttempted); assert.equal(vm.get('country','cbrn_response_refund_status_@1'),constants.get('constant:universal_cost_framework.result_rejected')); assert.equal(vm.purchase,undefined); assert(!vm.scopes.get('state').flags.has('cbrn_hospitals_utilities_secured')); assert.deepEqual(arr(vm,'start'),[]); });
test('public-payment-then-expired-care-reaches-loss-tick',()=>{ const vm=publicFixture(); vm.order(); vm.tick(1030); assert.equal(vm.losses.length,1); assert.deepEqual(arr(vm,'start'),[]); assert.equal(vm.receipts.length,7); });
report.assumptions[1]='Public decisions/getter triggers, population quote, five-model allocation, preflight and order/receipt inputs execute actual AST. Native stock, component price service (ordinary/half/quarter fixtures), receipt APIs and final purchase observer are modeled boundaries; no full Black Friday or native UI proof.';
report.passed = report.cases.filter(c => c.passed).length; report.failed = 0;
report.harnessSha256 = sha(fs.readFileSync(__filename));
fs.writeFileSync(path.join(__dirname, 'source_test_results.json'), JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({ passed: report.passed, failed: report.failed, sourceHashes: report.sourceHashes }, null, 2));
