// Bounded actual-source transaction tests. Reuses the conservative source VM.
// Native stock/PP/scopes and named context fixtures are explicit model inputs.
const fs = require('node:fs'), path = require('node:path'), assert = require('node:assert/strict'), crypto = require('node:crypto');
const core = require('../plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
const { VM, root, S, ticks, parse, definitions, constants, helperOutputs } = core;
const sha = value => crypto.createHash('sha256').update(value).digest('hex');
const sources = new Map(core.sources), selected = new Set(), inspected = new Set(), instances = [], localisations = new Map();
const vmFile = 'docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js', vmHash = sha(fs.readFileSync(path.join(root, vmFile)));
const load = file => { const source = fs.readFileSync(path.join(root, file), 'utf8'); sources.set(file, source); return source; };
for (const file of ['common/script_constants/026_black_friday_constants.txt', 'common/script_constants/cbrn_occupied_transaction_constants.txt'])
  for (const cat of parse(load(file))) for (const n of cat.value) if (typeof n.value === 'string' && /^-?\d+(\.\d+)?$/.test(n.value))
    constants.set(`constant:${cat.key}.${n.key}`, ticks(n.value));
const cbrnConstantsPath = 'common/script_constants/cbrn_system_constants.txt', cbrnConstants = load(cbrnConstantsPath);
const constantCategories = ['cbrn_math', 'cbrn_protection_decision_cost', 'cbrn_protection_ai'];
for (const name of constantCategories) {
  const text = cbrnConstants.match(new RegExp(`^${name}\\s*=\\s*\\{[\\s\\S]*?^\\}`, 'm'));
  assert(text, name);
  for (const cat of parse(text[0])) for (const n of cat.value) if (typeof n.value === 'string' && /^-?\d+(\.\d+)?$/.test(n.value))
    constants.set(`constant:${cat.key}.${n.key}`, ticks(n.value));
}
for (const file of ['common/scripted_effects/026_black_friday_effects.txt',
  'common/scripted_triggers/chaosx_universal_cost_triggers.txt',
  'common/scripted_effects/cbrn_immediate_response_cost_effects.txt', 'common/scripted_triggers/cbrn_immediate_response_cost_triggers.txt',
  'common/scripted_effects/cbrn_export_transaction_effects.txt', 'common/scripted_triggers/cbrn_export_transaction_triggers.txt',
  'common/scripted_effects/cbrn_occupied_transaction_effects.txt', 'common/scripted_triggers/cbrn_occupied_transaction_triggers.txt',
  'common/scripted_effects/cbrn_protection_effects.txt', 'common/scripted_effects/cbrn_protection_decision_effects.txt',
  'common/scripted_triggers/cbrn_protection_triggers.txt'])
  for (const n of parse(load(file))) definitions.set(n.key, n.value);
const nativeEscrowPath = 'common/scripted_effects/cbrn_state_escrow_native_effects.txt';
if (fs.existsSync(path.join(root, nativeEscrowPath))) for (const n of parse(load(nativeEscrowPath))) definitions.set(n.key, n.value);
for (const file of ['common/scripted_localisation/cbrn_export_transaction_localisation.txt', 'common/scripted_localisation/cbrn_occupied_transaction_localisation.txt'])
  for (const n of parse(load(file))) localisations.set(n.value.find(x => x.key === 'name').value, n.value.filter(x => x.key === 'text').map(x => x.value));
const controlChangePath = 'common/on_actions/chaosx_on_actions.txt';
const controlCleanupSource = source => { const match = source.match(/FROM\.FROM\s*=\s*\{[\s\S]*?\n\t\t\t\}/); assert(match, 'bounded control-change receipt block'); return match[0]; };
const controlCleanup = parse(controlCleanupSource(load(controlChangePath)));
const outputs = {
  black_friday_quote_custom_cost: ['black_friday_quote_final_cost', 'black_friday_quote_valid'],
  black_friday_allocate_owner_transaction: ['black_friday_owner_transaction_id'],
  cbrn_quote_immediate_response_component: ['cbrn_response_component_quoted', 'cbrn_response_component_valid', 'cbrn_response_component_source', 'cbrn_response_component_affordable'],
  cbrn_export_transaction_quote_fee: ['cbrn_export_fee', 'cbrn_export_fee_valid', 'cbrn_export_fee_source', 'cbrn_export_fee_affordable'],
  cbrn_occupied_quote_transaction_costs: ['cbrn_occupied_fee', 'cbrn_occupied_fee_valid', 'cbrn_occupied_fee_source', 'cbrn_occupied_fee_affordable', 'cbrn_occupied_factory_quote', 'cbrn_occupied_factory_quote_valid'],
  cbrn_occupied_pay_and_record_fee: ['cbrn_occupied_payment_success', 'cbrn_occupied_transaction'],
  cbrn_pay_and_record_response_component: ['cbrn_response_all_paid'],
  universal_cost_pay_component: ['universal_cost_payment_result'], universal_cost_credit_component: ['universal_cost_credit_result'],
  universal_cost_record_transaction: ['universal_cost_record_transaction_result', 'universal_cost_recorded_component_index'],
  universal_cost_find_transaction_row: ['universal_cost_transaction_found_index', 'universal_cost_transaction_lookup_result', 'universal_cost_transaction_is_indexed', 'universal_cost_transaction_pointer'],
  universal_cost_settle_transaction: ['universal_cost_settle_transaction_result'],
  universal_cost_validate_component_chain: ['universal_cost_chain_valid'],
  universal_cost_refund_component_at_cursor: ['universal_cost_refund_total', 'universal_cost_refund_unhandled_total', 'universal_cost_refund_all_complete'],
  universal_cost_refund_transaction: ['universal_cost_refund_total', 'universal_cost_refund_unhandled_total', 'universal_cost_refund_transaction_result'],
  cbrn_reserve_requested_masks_to_state: ['cbrn_mask_escrow_completed'],
  cbrn_refund_occupied_state_mask_reservation: ['cbrn_mask_escrow_refunded', 'cbrn_mask_escrow_refund_blocked'],
  cbrn_refund_external_state_mask_reservation: ['cbrn_mask_escrow_refunded', 'cbrn_mask_escrow_refund_blocked'],
  cbrn_state_escrow_measure_model_debit: ['cbrn_mask_native_before', 'cbrn_mask_native_after', 'cbrn_mask_native_requested', 'cbrn_mask_native_observed', 'cbrn_mask_native_valid'],
  cbrn_state_escrow_measure_model_credit: ['cbrn_mask_native_before', 'cbrn_mask_native_after', 'cbrn_mask_native_requested', 'cbrn_mask_native_observed', 'cbrn_mask_native_valid'],
  cbrn_state_escrow_record_native_mismatch: ['cbrn_mask_escrow_quarantined'],
  cbrn_state_escrow_refund_models: ['cbrn_mask_escrow_refunded', 'cbrn_mask_escrow_refund_blocked'],
};
for (const [name, vars] of Object.entries(outputs)) helperOutputs[name] = { vars, arrays: [] };
const models = ['gas_mask_equipment_reconditioned', 'gas_mask_equipment_1', 'gas_mask_equipment_2', 'gas_mask_equipment_3', 'gas_mask_equipment_4'];
const tokenIDs = new Map(models.map((name, i) => [name, ticks(200 + i)]));
const contextFixtures = ['cbrn_protection_program_category_visible', 'cbrn_target_can_receive_exported_masks', 'cbrn_refresh_country_mask_snapshot', 'cbrn_occupation_close_external_aid_reservation'];
class NativeVM extends VM {
  constructor() {
    super(); this.current = 7; this.recipient = 8; this.scopes = new Map([[7, { vars: this.regularVars, arrays: this.arrays, flags: new Set(), stock: new Map(), exists: true }]]);
    this.writes = []; this.mutationCaps = []; this.sendPairs = []; this.fixtureCalls = new Map(); instances.push(this);
  }
  scope(id) { if (!this.scopes.has(id)) this.scopes.set(id, { vars: new Map(), arrays: new Map(), flags: new Set(), stock: new Map(), exists: true }); return this.scopes.get(id); }
  withScope(id, fn) { const saved = this.current; this.current = id; this.regularVars = this.scope(id).vars; this.arrays = this.scope(id).arrays;
    try { return fn(); } finally { this.current = saved; this.regularVars = this.scope(saved).vars; this.arrays = this.scope(saved).arrays; } }
  key(name) { return super.key(name.replace(/@FROM/g, `@${this.recipient}`).replace(/@ROOT/g, '@7')); }
  value(token) {
    if (token === 'ROOT') return ticks(7); if (token === 'FROM') return ticks(this.recipient); if (token === 'THIS') return ticks(this.current);
    if (token.startsWith('token:')) { assert(tokenIDs.has(token.slice(6)), token); return tokenIDs.get(token.slice(6)); }
    if (token.startsWith('FROM.num_equipment@')) return this.scope(this.recipient).stock.get(token.slice(19)) || 0n;
    if (token.startsWith('num_equipment@')) return this.scope(this.current).stock.get(token.slice(14)) || 0n;
    if (token.startsWith('global.')) return this.vars.get(token) ?? this.scope(7).vars.get(token) ?? super.value(token);
    return super.value(token);
  }
  balance(key, amount, id = 7) { this.scope(id).stock.set(key, ticks(amount)); return this; }
  regular(name, amount, id = this.current) { this.withScope(id, () => this.write(name, ticks(amount), false)); return this; }
  flag(name, id = this.current) { this.scope(id).flags.add(this.key(name)); return this; }
  run(name, uninitialized = false) { selected.add(name); return super.run(name, uninitialized); }
  eval(nodes) {
    for (let i = 0; i < nodes.length; i++) {
      const node = nodes[i], { key: k, value: v } = node;
      if (contextFixtures.includes(k)) this.fixtureCalls.set(k, (this.fixtureCalls.get(k) || 0) + 1);
      else if (k === 'cbrn_quote_occupied_state_mask_reservation' && this.contextNeedFixture !== undefined) {
        this.fixtureCalls.set(k, (this.fixtureCalls.get(k) || 0) + 1); this.set('cbrn_reservation_quote_state_need', this.contextNeedFixture);
      } else if (k === 'cbrn_state_has_emergency_context' && this.contextNeedFixture !== undefined) {
        this.fixtureCalls.set(k, (this.fixtureCalls.get(k) || 0) + 1); if (!this.scope(this.current).emergency) return false;
      } else if (k === 'is_controlled_by') { if (ticks(this.scope(this.current).controller || 0) !== this.value(v)) return false;
      } else if (k === 'is_core_of') { if (ticks(this.scope(this.current).core || 0) !== this.value(v)) return false;
      } else if (k === 'state_population_k') { const left = ticks(this.scope(this.current).population || 0), right = this.value(v);
        if (!(node.op === '>' ? left > right : node.op === '<' ? left < right : left === right)) return false;
      }
      else if (k === 'ROOT' || k === 'FROM' || k === 'FROM.FROM' || k.startsWith('var:')) {
        const id = k === 'ROOT' ? 7 : k === 'FROM' ? this.recipient : k === 'FROM.FROM' ? 100 : Number(this.value(k.slice(4)) / S);
        if (!this.withScope(id, () => this.eval(v))) return false;
      } else if (k === 'every_controlled_state' || k === 'any_controlled_state') {
        const states = [...this.scopes.keys()].filter(id => id >= 100 && this.scope(id).controller === 7);
        const test = id => this.withScope(id, () => { const valid = this.eval(this.field(v, 'limit', []));
          return valid && this.eval(v.filter(n => n.key !== 'limit')); });
        if (k === 'any_controlled_state') { if (!states.some(test)) return false; }
        else for (const id of states) test(id);
      } else if (k === 'set_country_flag' || k === 'set_state_flag') this.flag(Array.isArray(v) ? this.field(v, 'flag') : v);
      else if (k === 'clr_country_flag' || k === 'clr_state_flag') this.scope(this.current).flags.delete(this.key(v));
      else if (k === 'has_country_flag' || k === 'has_state_flag') { if (!this.scope(this.current).flags.has(this.key(v))) return false; }
      else if (k === 'exists') { if (this.scope(this.current).exists !== (v === 'yes')) return false; }
      else if (k === 'tag') { if (ticks(this.current) !== this.value(v)) return false; }
      else if (k === 'has_capitulated') { if ((this.scope(this.current).capitulated || false) !== (v === 'yes')) return false; }
      else if (k === 'add_to_variable' || k === 'subtract_from_variable') {
        const name = this.field(v, 'var', v[0].key), amount = this.value(this.field(v, 'value', v[0].value));
        this.write(name, this.value(name) + (k === 'add_to_variable' ? amount : -amount), false);
      } else if (k === 'clamp_variable' || k === 'clamp_temp_variable') {
        const name = this.field(v, 'var'), min = this.value(this.field(v, 'min', '-2147483647')), max = this.value(this.field(v, 'max', '2147483647'));
        this.write(name, this.value(name) < min ? min : this.value(name) > max ? max : this.value(name), k === 'clamp_temp_variable');
      } else if (k === 'meta_effect') {
        const substitutions = new Map(v.filter(n => n.key !== 'text').map(n => {
          const match = String(n.value).match(/^"\[\?(\w+)\.GetTokenKey\]"$/); assert(match, `unsupported meta substitution ${n.value}`);
          const token = [...tokenIDs].find(([, id]) => id === this.value(match[1])); assert(token); return [n.key, token[0]];
        }));
        const replace = value => typeof value === 'string' ? value.replace(/\[(\w+)\]/g, (_, key) => { assert(substitutions.has(key)); return substitutions.get(key); }) :
          value.map(n => ({ key: replace(n.key), op: n.op, value: replace(n.value) }));
        if (!this.eval(replace(this.field(v, 'text')))) return false;
      } else if (k === 'add_political_power' || k === 'add_equipment_to_stockpile') {
        const name = k === 'add_political_power' ? 'pp' : this.field(v, 'type'), requested = this.value(k === 'add_political_power' ? v : this.field(v, 'amount'));
        const cap = k === 'add_equipment_to_stockpile' && this.mutationCaps.length ? this.mutationCaps.shift() : null;
        const observed = cap === null ? requested : ticks(cap);
        const stock = this.scope(this.current).stock; stock.set(name, (stock.get(name) || 0n) + observed);
        this.writes.push({ effect: k, scope: this.current, model: name, requested: String(requested / S), observed: String(observed / S) });
      } else if (k === 'send_equipment') {
        const name = this.field(v, 'type'), requested = this.value(this.field(v, 'amount'));
        const [debit, gain] = this.sendPairs.length ? this.sendPairs.shift().map(ticks) : [requested, requested];
        this.scope(7).stock.set(name, (this.scope(7).stock.get(name) || 0n) - debit);
        this.scope(this.recipient).stock.set(name, (this.scope(this.recipient).stock.get(name) || 0n) + gain);
        this.writes.push({ effect: k, model: name, requested: String(requested / S), debit: String(debit / S), gain: String(gain / S) });
      } else if (k === 'has_political_power' || k === 'political_power' || k === 'has_equipment') {
        const cmp = k === 'has_equipment' ? v[0] : node;
        const left = k !== 'has_equipment' ? this.scope(this.current).stock.get('pp') || 0n : cmp.key === 'gas_mask_equipment' ?
          models.reduce((sum, name) => sum + (this.scope(this.current).stock.get(name) || 0n), 0n) : this.scope(this.current).stock.get(cmp.key) || 0n;
        const right = this.value(cmp.value); if (!(cmp.op === '<' ? left < right : cmp.op === '>' ? left > right : left === right)) return false;
      } else {
        const group = [node]; if (k === 'if') while (nodes[i + 1] && ['else', 'else_if'].includes(nodes[i + 1].key)) group.push(nodes[++i]);
        if (!super.eval(group)) return false;
      }
    }
    return true;
  }
}
const resultFile = path.join(root, 'docs/testing/2026-10-03_cbrn_occupied_export_source_results.json');
const previous = fs.existsSync(resultFile) ? JSON.parse(fs.readFileSync(resultFile, 'utf8')) : {};
const results = { status: 'running', baselineDefectEvidence: previous.baselineDefectEvidence || null, sourceHashes: Object.fromEntries([...sources].map(([f, s]) => [f, sha(s)])),
  reusedVM: { file: vmFile, sha256: vmHash }, scenarios: [], selectedBodies: {}, inspectedBodyHashes: {}, concurrentSources: {}, fixtureHelpers: contextFixtures, fixtureHelperCalls: {}, helperOutputChecks: {},
  adapterBoundary: 'Explicit donor7, FROM8/9, controlled STATE100/101. Conservative temp cleanup retained. Literal MODEL meta substitution only. PP/concrete native stock deltas are model inputs.',
  limitations: ['Full recipient/category eligibility and snapshot refresh are excluded named fixtures.', 'No producer/variant provenance, timer, save, native dispatch, AI, renderer or engine proof.',
    'Occupied acceptance publication is a persisted program fixture after actual fee payment. Occupied state need/outcome paths are not simulated unless explicitly listed.',
    'Partial native adapters test source conservation guards, without establishing actual native engine occurrence.'] };
const num = (vm, token) => Number(vm.value(token) / S), stock = (vm, name, id = 7) => Number((vm.scope(id).stock.get(name) || 0n) / S);
function declares(vm, name) { for (const v of outputs[name] || []) if (!vm.vars.has(v)) vm.set(v, 0); }
function exec(vm, name) { declares(vm, name); assert(vm.run(name)); }
function scenario(id, fn) { try { results.scenarios.push({ id, status: 'passed', evidence: fn() }); } catch (e) { results.scenarios.push({ id, status: 'failed', error: e.stack }); } }
function sale(vm, ratio) {
  vm.set('global.universal_cost_custom_quote_cache_valid', 1).regular('global.black_friday_sale_sequence', 1);
  if (ratio !== null) {
    vm.flags.add('black_friday_active');
    for (const [suffix, value] of [['ids', 26], ['ratios', ratio], ['priorities', 500], ['eligibility_masks', 0]]) vm.arrays.set(`global.universal_cost_source_${suffix}`, [ticks(value)]);
  }
  return vm;
}
function expiry(vm) { vm.flags.delete('black_friday_active'); vm.set('universal_cost_source_clear_result', 0); assert(vm.run('universal_cost_source_clear_black_friday')); }
function masks(vm, amounts) { models.forEach((name, i) => vm.balance(name, amounts[i])); return vm; }
function receipt(vm, id, suffix) { const i = vm.scope(7).arrays.get('universal_cost_transaction_ids').indexOf(ticks(id)); assert(i >= 0); return Number(vm.scope(7).arrays.get(`universal_cost_transaction_${suffix}`)[i] / S); }
function getter(vm, name) { for (const branch of localisations.get(name)) if (vm.eval(vm.field(branch, 'trigger', []))) return vm.field(branch, 'localization_key'); throw Error(`no branch ${name}`); }

for (const [ratio, exportFee, occupiedFee] of [[null, 15, 25], [5000, 8, 13], [2500, 4, 7]]) for (const delta of [-1, 0, 1]) {
  scenario(`export-fee-${exportFee}-balance-${exportFee + delta}`, () => {
    const vm = sale(masks(new NativeVM().balance('pp', exportFee + delta), [100, 150, 250, 400, 600]), ratio);
    exec(vm, 'cbrn_export_transaction_quote_fee'); assert.equal(num(vm, 'cbrn_export_fee'), exportFee); assert.equal(num(vm, 'cbrn_export_fee_valid'), 1);
    assert.equal(num(vm, 'cbrn_export_fee_affordable'), delta < 0 ? 0 : 1);
    vm.set('cbrn_export_started', 0); exec(vm, 'cbrn_export_transaction_start');
    assert.equal(num(vm, 'cbrn_export_started'), delta < 0 ? 0 : 1);
    if (delta < 0) { assert.equal(vm.writes.length, 0); return { affordable: false, nativeWrites: 0 }; }
    assert.equal(stock(vm, 'pp'), delta); const id = num(vm, 'cbrn_export_receipt_@FROM');
    assert.equal(receipt(vm, id, 'total_paid_costs'), exportFee); assert.equal(receipt(vm, id, 'component_counts'), 1);
    assert.equal(receipt(vm, id, 'source_ids'), ratio === null ? 0 : 26);
    assert.equal(receipt(vm, id, 'achievement_family_ids'), Number(constants.get('constant:universal_cost_family.political_power') / S));
    assert.equal(receipt(vm, id, 'achievement_primary_component_ids'), 1); assert.equal(receipt(vm, id, 'achievement_cost_bases'), 1);
    assert.deepEqual(vm.scope(7).arrays.get('universal_cost_component_achievement_primary_members'), [S]);
    assert.equal(models.reduce((sum, name) => sum + num(vm, `cbrn_export_held_${name}_@FROM`), 0), 500);
    const writes = vm.writes.length; exec(vm, 'cbrn_export_transaction_start'); assert.equal(vm.writes.length, writes);
    expiry(vm); assert.equal(getter(vm, 'GetCbrnExportPoliticalCost'), 'cbrn_export_fee_cost_frozen'); assert.equal(num(vm, 'cbrn_export_fee'), exportFee);
    assert(vm.run('cbrn_export_transaction_can_continue'));
    vm.set('cbrn_export_cancelled', 0); exec(vm, 'cbrn_export_transaction_cancel'); assert.equal(num(vm, 'cbrn_export_cancelled'), 1);
    assert.equal(stock(vm, 'pp'), delta); assert.equal(receipt(vm, id, 'states'), 4);
    assert.deepEqual(models.map(name => stock(vm, name)), [100, 150, 250, 400, 600]);
    const closed = vm.writes.length; exec(vm, 'cbrn_export_transaction_cancel'); assert.equal(vm.writes.length, closed);
    return { paid: exportFee, receipt: id, cancellationFeeRemainsSpent: true, exactModelsRestored: true, writes: vm.writes };
  });
  scenario(`occupied-fee-${occupiedFee}-balance-${occupiedFee + delta}`, () => {
    const vm = sale(new NativeVM().balance('pp', occupiedFee + delta), ratio);
    exec(vm, 'cbrn_occupied_quote_transaction_costs'); assert.equal(num(vm, 'cbrn_occupied_fee'), occupiedFee);
    assert.equal(num(vm, 'cbrn_occupied_factory_quote'), ratio === null ? 2 : 1); assert.equal(num(vm, 'cbrn_occupied_fee_affordable'), delta < 0 ? 0 : 1);
    exec(vm, 'cbrn_occupied_pay_and_record_fee'); assert.equal(num(vm, 'cbrn_occupied_payment_success'), delta < 0 ? 0 : 1);
    if (delta < 0) { assert.equal(vm.writes.length, 0); assert.equal(vm.scope(7).vars.has('universal_cost_allocated_transaction_id_@1'), false); return { affordable: false, writes: 0 }; }
    const id = num(vm, 'cbrn_occupied_transaction'); assert.equal(receipt(vm, id, 'total_paid_costs'), occupiedFee);
    assert.equal(receipt(vm, id, 'source_ids'), ratio === null ? 0 : 26);
    assert.equal(receipt(vm, id, 'achievement_family_ids'), Number(constants.get('constant:universal_cost_family.political_power') / S));
    assert.equal(receipt(vm, id, 'achievement_primary_component_ids'), 1); assert.equal(receipt(vm, id, 'achievement_cost_bases'), 1);
    assert.deepEqual(vm.scope(7).arrays.get('universal_cost_component_achievement_primary_members'), [S]);
    vm.regular('cbrn_occupied_committed_fee', occupiedFee).regular('cbrn_occupied_committed_source', ratio === null ? 0 : 26)
      .regular('cbrn_occupied_committed_transaction', id).regular('cbrn_occupied_committed_variant', ratio === null ? 1 : 2)
      .regular('cbrn_occupied_committed_reserved', 100).flag('cbrn_occupied_transaction_active').flag('cbrn_civilian_distribution_program_active');
    expiry(vm); assert.equal(getter(vm, 'GetCbrnOccupiedDistributionPoliticalCost'), 'cbrn_occupied_fee_cost_ready'); assert.equal(num(vm, 'cbrn_occupied_fee'), occupiedFee);
    exec(vm, 'cbrn_occupied_cancel_selected_program'); assert.equal(stock(vm, 'pp'), delta); assert.equal(receipt(vm, id, 'states'), 4);
    const writes = vm.writes.length; exec(vm, 'cbrn_occupied_cancel_selected_program'); exec(vm, 'cbrn_occupied_finish_selected_program'); assert.equal(vm.writes.length, writes);
    return { paid: occupiedFee, receipt: id, cancellationFeeRemainsSpent: true, acceptanceFields: 'explicit fixture', writes: vm.writes };
  });
}

scenario('active-sale-missing-source-rejects-both-quotes-without-debit', () => {
  const vm = sale(new NativeVM().balance('pp', 100), null); vm.flags.add('black_friday_active');
  exec(vm, 'cbrn_export_transaction_quote_fee'); assert.equal(num(vm, 'cbrn_export_fee_valid'), 0);
  exec(vm, 'cbrn_occupied_quote_transaction_costs'); assert.equal(num(vm, 'cbrn_occupied_fee_valid'), 0); assert.equal(vm.writes.length, 0);
  return { bothInvalid: true };
});
scenario('occupied-conflicting-record-credits-only-new-debit', () => {
  const vm = sale(new NativeVM().balance('pp', 100), 2500); exec(vm, 'cbrn_occupied_quote_transaction_costs'); exec(vm, 'cbrn_occupied_pay_and_record_fee');
  vm.regular('black_friday_transaction_sequence', 0).set('cbrn_occupied_fee', 13); exec(vm, 'cbrn_occupied_pay_and_record_fee');
  assert.equal(num(vm, 'cbrn_occupied_payment_success'), 0); assert.equal(stock(vm, 'pp'), 93); assert.equal(receipt(vm, 1, 'total_paid_costs'), 7);
  return { nativeWrites: vm.writes, existingReceiptPaid: 7 };
});
scenario('export-two-recipient-ownership-isolation-and-repeated-release', () => {
  const vm = sale(masks(new NativeVM().balance('pp', 100), [1000, 1000, 0, 0, 0]), null);
  vm.set('cbrn_export_started', 0); exec(vm, 'cbrn_export_transaction_start'); vm.recipient = 9; exec(vm, 'cbrn_export_transaction_start');
  assert.equal(num(vm, 'cbrn_export_owned_receipts_count'), 2); assert.equal(num(vm, 'cbrn_export_held_gas_mask_equipment_reconditioned_@FROM'), 500);
  vm.recipient = 8; vm.set('cbrn_export_cancelled', 0); exec(vm, 'cbrn_export_transaction_cancel'); assert.equal(num(vm, 'cbrn_export_owned_receipts_count'), 1);
  vm.recipient = 9; assert(vm.run('cbrn_export_transaction_has_owned_receipt')); assert.equal(num(vm, 'cbrn_export_held_gas_mask_equipment_reconditioned_@FROM'), 500);
  exec(vm, 'cbrn_export_transaction_cancel'); assert.equal(num(vm, 'cbrn_export_owned_receipts_count'), 0); exec(vm, 'cbrn_export_transaction_cancel');
  assert.equal(stock(vm, 'pp'), 70); assert.equal(stock(vm, models[0]), 1000); return { twoReceipts: true, isolatedCancellation: true, writes: vm.writes };
});
for (const mode of ['partial-reserve', 'partial-refund', 'partial-release', 'partial-send', 'mismatch']) scenario(`export-${mode}-concrete-native-observation`, () => {
  const vm = new NativeVM().balance(models[0], 500); vm.set('cbrn_export_remaining', 500).set('cbrn_export_model', 200).regular('cbrn_export_delivered_total_@FROM', 0);
  if (mode === 'partial-reserve') vm.mutationCaps = [-200]; exec(vm, 'cbrn_export_transaction_reserve_model');
  assert.equal(num(vm, `cbrn_export_held_${models[0]}_@FROM`), mode === 'partial-reserve' ? 200 : 500);
  if (mode === 'partial-reserve') { assert.equal(num(vm, 'cbrn_export_remaining'), 300); assert.equal(stock(vm, models[0]), 300); }
  else if (mode === 'partial-refund') {
    vm.mutationCaps = [200]; exec(vm, 'cbrn_export_transaction_refund_model'); assert.equal(num(vm, `cbrn_export_held_${models[0]}_@FROM`), 300);
    exec(vm, 'cbrn_export_transaction_refund_model'); assert.equal(stock(vm, models[0]), 500);
  } else {
    if (mode === 'partial-release') vm.mutationCaps = [250];
    if (mode === 'partial-send') vm.sendPairs = [[100, 100]];
    if (mode === 'mismatch') vm.sendPairs = [[500, 250]];
    exec(vm, 'cbrn_export_transaction_send_model');
    if (mode === 'partial-release') { assert.equal(stock(vm, models[0]), 250); assert.equal(num(vm, `cbrn_export_held_${models[0]}_@FROM`), 250); assert.equal(stock(vm, models[0], 8), 0); }
    if (mode === 'partial-send') { assert.equal(stock(vm, models[0]), 400); assert.equal(stock(vm, models[0], 8), 100); assert.equal(num(vm, 'cbrn_export_delivered_total_@FROM'), 100); }
    if (mode === 'mismatch') { assert(vm.scope(7).flags.has('cbrn_export_native_mismatch_@8')); assert.equal(num(vm, 'cbrn_export_delivered_total_@FROM'), 0); }
    const writes = vm.writes.length; exec(vm, 'cbrn_export_transaction_send_model'); assert.equal(vm.writes.length, writes);
  }
  if (mode !== 'mismatch') { exec(vm, 'cbrn_export_transaction_refund_model'); assert.equal(stock(vm, models[0]) + stock(vm, models[0], 8), 500); }
  else { const writes = vm.writes.length; exec(vm, 'cbrn_export_transaction_refund_model'); assert.equal(vm.writes.length, writes); }
  return { mode, writes: vm.writes, held: num(vm, `cbrn_export_held_${models[0]}_@FROM`), donor: stock(vm, models[0]), recipient: stock(vm, models[0], 8) };
});

function stateReserve(vm, amount, external = 0) { vm.scope(100).controller = 7; vm.withScope(100, () => { vm.set('cbrn_mask_escrow_requested', amount).set('cbrn_mask_escrow_external', external).set('cbrn_mask_escrow_completed', 0); exec(vm, 'cbrn_reserve_requested_masks_to_state'); }); }
function stateRefund(vm, external = 0) { vm.withScope(100, () => exec(vm, external ? 'cbrn_refund_external_state_mask_reservation' : 'cbrn_refund_occupied_state_mask_reservation')); }
for (const mode of ['exact', 'partial-debit', 'partial-credit']) scenario(`occupied-state-escrow-${mode}-actual-source`, () => {
  const initial = mode === 'partial-debit' ? [100, 0, 0, 0, 0] : [100, 150, 250, 0, 0];
  const vm = masks(new NativeVM(), initial); if (mode === 'partial-debit') vm.mutationCaps = [-40];
  stateReserve(vm, mode === 'exact' ? 500 : 100);
  const completed = num(vm, 'cbrn_mask_escrow_completed'); assert.equal(completed, mode === 'exact' ? 500 : mode === 'partial-debit' ? 40 : 100);
  if (mode === 'partial-credit') vm.mutationCaps = [40]; stateRefund(vm);
  const returned = num(vm, 'cbrn_mask_escrow_refunded'); assert.equal(returned, mode === 'partial-credit' ? 40 : completed);
  if (mode === 'partial-credit') {
    assert.equal(Number(vm.scope(100).vars.get('cbrn_occupied_mask_escrow_reconditioned') / S), 60);
    assert(vm.scope(100).flags.has('cbrn_occupied_mask_escrow_active')); assert.equal(num(vm, 'cbrn_mask_escrow_refund_blocked'), 1); stateRefund(vm);
  }
  assert.deepEqual(models.map(name => stock(vm, name)), initial); const writes = vm.writes.length; stateRefund(vm); assert.equal(vm.writes.length, writes);
  return { completed, firstReturned: returned, writes: vm.writes };
});
for (const external of [0, 1]) scenario(`${external ? 'external' : 'occupied'}-state-mixed-five-model-reserve-return-and-repeat`, () => {
  const initial = [20, 30, 40, 50, 60], vm = masks(new NativeVM(), initial), family = external ? 'external' : 'occupied';
  stateReserve(vm, 200, external); assert.equal(num(vm, 'cbrn_mask_escrow_completed'), 200);
  assert.deepEqual(['reconditioned', 'basic', 'improved', 'advanced', 'sealed'].map(suffix => Number(vm.scope(100).vars.get(`cbrn_${family}_mask_escrow_${suffix}`) / S)), initial);
  assert.deepEqual(models.map(name => stock(vm, name)), [0, 0, 0, 0, 0]);
  stateRefund(vm, external); assert.equal(num(vm, 'cbrn_mask_escrow_refunded'), 200); assert.deepEqual(models.map(name => stock(vm, name)), initial);
  assert.equal(vm.scope(100).flags.has(`cbrn_${family}_mask_escrow_active`), false);
  const writes = vm.writes.length; stateRefund(vm, external); assert.equal(vm.writes.length, writes);
  return { family, modelRows: initial, exactRestoration: true, writes: vm.writes };
});
scenario('external-state-valid-partial-debit-records-only-real-model-units', () => {
  const vm = masks(new NativeVM(), [100, 0, 0, 0, 0]); vm.mutationCaps = [-40]; stateReserve(vm, 100, 1);
  assert.equal(num(vm, 'cbrn_mask_escrow_completed'), 40); assert.equal(vm.scope(100).vars.get('cbrn_external_mask_escrow_reconditioned'), ticks(40));
  assert.equal(stock(vm, models[0]), 60); stateRefund(vm, 1); assert.equal(num(vm, 'cbrn_mask_escrow_refunded'), 40); assert.equal(stock(vm, models[0]), 100);
  const writes = vm.writes.length; stateRefund(vm, 1); assert.equal(vm.writes.length, writes);
  return { completed: 40, held: 40, exactRestoration: 100, writes: vm.writes };
});

scenario('occupied-cancel-refunds-five-models-only-owned-state-and-preserves-busy-flag', () => {
  const vm = sale(masks(new NativeVM().balance('pp', 100), [100, 100, 100, 100, 100]), 5000);
  exec(vm, 'cbrn_occupied_quote_transaction_costs'); exec(vm, 'cbrn_occupied_pay_and_record_fee'); const id = num(vm, 'cbrn_occupied_transaction');
  stateReserve(vm, 500); vm.flag('cbrn_occupied_distribution_program_target', 100).flag('cbrn_protection_project_active', 100);
  vm.scope(101).controller = 7; vm.flag('cbrn_occupied_distribution_program_target', 101).flag('cbrn_occupied_mask_escrow_active', 101);
  vm.regular('cbrn_occupied_mask_escrow_donor', 9, 101).regular('cbrn_occupied_mask_escrow_basic', 50, 101);
  vm.regular('cbrn_occupied_committed_transaction', id).regular('cbrn_occupied_committed_fee', 13).regular('cbrn_occupied_committed_source', 26)
    .flag('cbrn_occupied_transaction_active').flag('cbrn_civilian_distribution_program_active');
  expiry(vm); exec(vm, 'cbrn_occupied_cancel_selected_program');
  assert.deepEqual(models.map(name => stock(vm, name)), [100, 100, 100, 100, 100]); assert.equal(stock(vm, 'pp'), 87);
  assert.equal(receipt(vm, id, 'states'), 4); assert(vm.scope(100).flags.has('cbrn_protection_project_active'));
  assert.equal(vm.scope(101).vars.get('cbrn_occupied_mask_escrow_basic'), ticks(50)); assert(vm.scope(101).flags.has('cbrn_occupied_distribution_program_target'));
  const writes = vm.writes.length; exec(vm, 'cbrn_occupied_cancel_selected_program'); assert.equal(vm.writes.length, writes);
  return { feeSpent: 13, exactModelsRestored: 5, foreignDonorStateUntouched: true, busyFlagRetained: true, acceptanceFields: 'explicit fixture', writes: vm.writes };
});
scenario('export-five-model-exact-send-and-repeat-refusal', () => {
  const vm = masks(new NativeVM(), [100, 100, 100, 100, 100]); vm.set('cbrn_export_remaining', 500).regular('cbrn_export_delivered_total_@FROM', 0);
  for (const name of models) { vm.set('cbrn_export_model', tokenIDs.get(name) / S); exec(vm, 'cbrn_export_transaction_reserve_model'); }
  assert.equal(num(vm, 'cbrn_export_remaining'), 0);
  for (const name of models) { vm.set('cbrn_export_model', tokenIDs.get(name) / S); exec(vm, 'cbrn_export_transaction_send_model'); }
  assert.equal(num(vm, 'cbrn_export_delivered_total_@FROM'), 500); assert.deepEqual(models.map(name => stock(vm, name, 8)), [100, 100, 100, 100, 100]);
  const writes = vm.writes.length; for (const name of models) { vm.set('cbrn_export_model', tokenIDs.get(name) / S); exec(vm, 'cbrn_export_transaction_send_model'); }
  assert.equal(vm.writes.length, writes); return { measuredDelivered: 500, fiveModels: true, writes: vm.writes };
});
for (const external of [0, 1]) for (const phase of ['debit', 'credit']) for (const anomaly of ['negative-observation', 'oversized-observation'])
scenario(`${external ? 'external' : 'occupied'}-${phase}-${anomaly}-quarantine-refuses-retry`, () => {
  const vm = masks(new NativeVM(), [500, 0, 0, 0, 0]), family = external ? 'external' : 'occupied';
  if (phase === 'debit') vm.mutationCaps = [anomaly === 'negative-observation' ? 40 : -140];
  stateReserve(vm, 100, external);
  if (phase === 'credit') { vm.mutationCaps = [anomaly === 'negative-observation' ? -40 : 140]; stateRefund(vm, external); }
  assert(vm.scope(100).flags.has(`cbrn_${family}_mask_escrow_native_mismatch`)); assert(vm.scope(100).flags.has(`cbrn_${family}_mask_escrow_active`));
  assert.equal(vm.scope(100).vars.get(`cbrn_${family}_mask_escrow_native_observed`), ticks(anomaly === 'negative-observation' ? -40 : 140));
  const writes = vm.writes.length; stateRefund(vm, external); stateReserve(vm, 100, external); assert.equal(vm.writes.length, writes);
  assert.equal(num(vm, 'cbrn_mask_escrow_completed'), 0); assert.equal(num(vm, 'cbrn_mask_escrow_refund_blocked'), 1);
  return { phase, anomaly, family, nativeWrites: vm.writes, quarantineRetained: true };
});
scenario('occupied-continuation-uses-owned-need-with-unrelated-busy-state', () => {
  const vm = new NativeVM(); vm.contextNeedFixture = 100; vm.scope(100).controller = 7; vm.scope(100).population = 1000; vm.scope(100).emergency = true;
  vm.regular('cbrn_occupied_committed_transaction', 1).flag('cbrn_occupied_transaction_active').flag('cbrn_civilian_distribution_program_active').flag('cbrn_national_respirator_reserve');
  vm.flag('cbrn_occupied_distribution_program_target', 100).flag('cbrn_occupied_mask_escrow_active', 100).flag('cbrn_protection_project_active', 100);
  vm.regular('cbrn_occupied_mask_escrow_donor', 7, 100);
  assert(vm.run('cbrn_occupied_country_can_continue')); assert.equal(stock(vm, 'pp'), 0);
  vm.contextNeedFixture = 0; assert.equal(vm.run('cbrn_occupied_country_can_continue'), false);
  vm.contextNeedFixture = 100; vm.regular('cbrn_occupied_mask_escrow_donor', 9, 100); assert.equal(vm.run('cbrn_occupied_country_can_continue'), false);
  const keys = body => body.flatMap(n => [n.key, ...(Array.isArray(n.value) ? keys(n.value) : [])]);
  assert(!keys(definitions.get('cbrn_occupied_country_can_continue')).includes('cbrn_state_can_reserve_occupied_masks'));
  assert(keys(definitions.get('cbrn_occupied_finish_selected_program')).includes('cbrn_occupied_state_can_complete_reserved_distribution'));
  assert(!keys(definitions.get('cbrn_complete_occupied_state_distribution')).includes('cbrn_end_state_protection_project'));
  inspected.add('cbrn_complete_occupied_state_distribution');
  return { parsedContinuation: true, busyFlag: true, emptyPPAndUnreservedStock: true, zeroNeedRefused: true, otherDonorRefused: true,
    fixtureBoundary: 'Native control/core/population and emergency/need query result are explicit fixtures. Exact physical state need/outcome are not executed.' };
});
scenario('occupied-quarantine-retains-target-and-blocks-positive-aggregate-fee', () => {
  inspected.add('cbrn_occupied_begin_selected_program');
  const body = definitions.get('cbrn_occupied_begin_selected_program');
  const descendants = nodes => nodes.flatMap(n => [n, ...(Array.isArray(n.value) ? descendants(n.value) : [])]);
  const paymentBlock = descendants(body).find(n => n.key === 'if' && n.value.some(x => x.key === 'cbrn_occupied_pay_and_record_fee'));
  assert(paymentBlock, 'actual aggregate payment guard');
  const vm = new NativeVM().set('cbrn_occupied_program_reserved', 100).flag('cbrn_occupied_transaction_recovery_pending');
  assert.equal(vm.eval(vm.field(paymentBlock.value, 'limit')), false);
  vm.scope(7).flags.delete('cbrn_occupied_transaction_recovery_pending'); assert(vm.eval(vm.field(paymentBlock.value, 'limit')));
  const states = descendants(body).find(n => n.key === 'every_controlled_state').value;
  const quarantineMarker = states.find(n => n.key === 'if' && JSON.stringify(n).includes('cbrn_occupied_mask_escrow_native_mismatch'));
  assert(quarantineMarker);
  vm.flag('cbrn_occupied_mask_escrow_active', 100).flag('cbrn_occupied_mask_escrow_native_mismatch', 100).regular('cbrn_occupied_mask_escrow_donor', 7, 100);
  vm.withScope(100, () => assert(vm.eval([quarantineMarker]))); assert(vm.scope(100).flags.has('cbrn_occupied_distribution_program_target'));
  return { actualParsedPaymentLimit: true, positiveEarlierAggregate: 100, quarantinePreventsFee: true, quarantineTargetPreserved: true,
    sourceBoundary: 'Executes the actual parsed country payment limit and STATE quarantine marker block, without full national selection orchestration.' };
});
for (const external of [0, 1]) scenario(`control-change-${external ? 'external' : 'occupied'}-partial-refund-retains-target-until-exact-retry`, () => {
  const vm = masks(new NativeVM(), [100, 0, 0, 0, 0]); stateReserve(vm, 100, external);
  const target = external ? 'cbrn_occupation_external_aid_project_active' : 'cbrn_occupied_distribution_program_target'; vm.flag(target, 100);
  vm.mutationCaps = [40]; assert(vm.withScope(8, () => vm.eval(controlCleanup))); assert(vm.scope(100).flags.has(target));
  assert.equal(stock(vm, models[0]), 40); assert.equal(num(vm, 'cbrn_mask_escrow_refund_blocked'), 1);
  assert(vm.withScope(8, () => vm.eval(controlCleanup))); assert.equal(vm.scope(100).flags.has(target), false); assert.equal(stock(vm, models[0]), 100);
  const writes = vm.writes.length; assert(vm.withScope(8, () => vm.eval(controlCleanup))); assert.equal(vm.writes.length, writes);
  return { modelRefunded: 100, partialTargetRetained: true, exactTargetCleared: true, writes: vm.writes,
    scopeBoundary: 'Actual first FROM.FROM receipt-cleanup block only. FROM.FROM is modeled STATE100 and var:stored_donor resolves7. Later on-action callbacks and external aid counter closure are excluded.' };
});

// Capture executed definitions and require stable selected bodies through run.
for (const [file, source] of sources) {
  const final = fs.readFileSync(path.join(root, file), 'utf8'); let nodes, finalNodes;
  if (file === controlChangePath) { nodes = parse(controlCleanupSource(source)); finalNodes = parse(controlCleanupSource(final));
    results.controlChangeFragment = { file, astSha256: sha(JSON.stringify(nodes)) };
  } else if (file === cbrnConstantsPath) { nodes = constantCategories.map(name => source.match(new RegExp(`^${name}\\s*=\\s*\\{[\\s\\S]*?^\\}`, 'm'))[0]);
    finalNodes = constantCategories.map(name => final.match(new RegExp(`^${name}\\s*=\\s*\\{[\\s\\S]*?^\\}`, 'm'))[0]); }
  else { nodes = parse(source).filter(n => selected.has(n.key) || inspected.has(n.key) || file.includes('script_constants/') || file.includes('scripted_localisation/'));
    finalNodes = parse(final).filter(n => selected.has(n.key) || inspected.has(n.key) || file.includes('script_constants/') || file.includes('scripted_localisation/')); }
  const stable = JSON.stringify(nodes) === JSON.stringify(finalNodes); results.concurrentSources[file] = { before: sha(source), after: sha(final), selectedStable: stable, wholeFileChanged: source !== final };
  if (file !== cbrnConstantsPath) for (const n of nodes) if (selected.has(n.key)) results.selectedBodies[n.key] = { file, astSha256: sha(JSON.stringify(n.value)) };
  if (file !== cbrnConstantsPath) for (const n of nodes) if (inspected.has(n.key)) results.inspectedBodyHashes[n.key] = { file, astSha256: sha(JSON.stringify(n.value)) };
  if (!stable) results.scenarios.push({ id: `source-stability:${file}`, status: 'failed', error: 'Executed body/selected constants/localisation changed during run. Rerun stable snapshot.' });
}
for (const vm of instances) for (const [name, count] of vm.helperOutputChecks) results.helperOutputChecks[name] = (results.helperOutputChecks[name] || 0) + count;
for (const vm of instances) for (const [name, count] of vm.fixtureCalls) results.fixtureHelperCalls[name] = (results.fixtureHelperCalls[name] || 0) + count;
results.reusedVM.unchanged = sha(fs.readFileSync(path.join(root, vmFile))) === vmHash;
if (!results.reusedVM.unchanged) results.scenarios.push({ id: 'source-stability:reusedVM', status: 'failed', error: 'Reused VM changed during run.' });
results.scenarioCount = results.scenarios.length; results.failedCount = results.scenarios.filter(n => n.status === 'failed').length;
results.helperReturns = instances.reduce((sum, vm) => sum + vm.helperReturns, 0); results.droppedTemps = instances.reduce((sum, vm) => sum + vm.droppedTemps, 0);
results.status = results.failedCount ? 'failed' : 'passed'; fs.writeFileSync(resultFile, JSON.stringify(results, null, 2) + '\n');
console.log(JSON.stringify({ status: results.status, cases: results.scenarioCount, failures: results.scenarios.filter(n => n.status === 'failed') }, null, 2));
if (results.failedCount) process.exitCode = 1;
