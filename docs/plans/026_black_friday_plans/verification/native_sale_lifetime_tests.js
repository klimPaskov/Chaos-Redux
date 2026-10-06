// Runs the production helpers with the existing conservative temporary-frame VM.
// Native modifier aggregation, law possession, and slot counts are fixture inputs.
// This checks helper storage and arithmetic, not native HOI4 pricing or rounding.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const { VM, S, ticks, parse, root, definitions, constants } = require('../subagent_handoffs/exact_quote_source_tests.js');
const nativePath = 'common/scripted_effects/026_black_friday_native_sale_effects.txt';
const effectsPath = 'common/scripted_effects/026_black_friday_effects.txt';
const nativeSource = fs.readFileSync(path.join(root, nativePath), 'utf8');
const effectsSource = fs.readFileSync(path.join(root, effectsPath), 'utf8');
const dynamic = parse(fs.readFileSync(path.join(root, 'common/dynamic_modifiers/026_black_friday_dynamic_modifiers.txt'), 'utf8'))[0].value;
for (const category of parse(fs.readFileSync(path.join(root, 'common/script_constants/026_black_friday_constants.txt'), 'utf8'))) {
  for (const entry of category.value) if (!Array.isArray(entry.value)) constants.set(`constant:${category.key}.${entry.key}`, ticks(entry.value));
}
for (const node of parse(nativeSource)) definitions.set(node.key, node.value);
for (const node of parse(fs.readFileSync(path.join(root, 'common/scripted_triggers/chaosx_universal_cost_triggers.txt'), 'utf8'))) definitions.set(node.key, node.value);
function block(source, name) {
  const start = source.indexOf(`${name} = {`);
  assert(start >= 0, name);
  let depth = 0, end = source.indexOf('{', start);
  do { if (source[end] === '{') depth++; if (source[end] === '}') depth--; end++; } while (depth);
  return parse(source.slice(start, end))[0].value;
}
for (const name of ['black_friday_engine_purchase_read_laws', 'black_friday_engine_purchase_snapshot', 'black_friday_engine_purchase_credit', 'black_friday_entry_event', 'black_friday_simple_cost_pay']) {
  definitions.set(name, block(effectsSource, name));
}
class NativeVM extends VM {
  constructor() {
    super(); this.ordinary = new Map(); this.applied = new Map(); this.nativeCalls = new Map();
    this.ideas = new Set(); this.credit = []; this.events = []; this.ai = false;
  }
  value(token) {
    if (token.startsWith('modifier@')) {
      const key = token.slice('modifier@'.length);
      return (this.ordinary.get(key) || 0n) + (this.applied.get(key) || 0n);
    }
    return super.value(token);
  }
  run(name, uninitialized = false) {
    if (this.nativeCalls.has(name)) return this.nativeCalls.get(name)();
    // The simple quote consumes only final_cost, which production preinitializes.
    // Other public quote outputs are not read after return by this caller.
    if (name === 'black_friday_quote_custom_cost') return super.run(name, true);
    return super.run(name, uninitialized);
  }
  eval(nodes) {
    const primitives = new Set(['has_country_flag', 'set_country_flag', 'clr_country_flag', 'has_dynamic_modifier',
      'add_dynamic_modifier', 'remove_dynamic_modifier', 'force_update_dynamic_modifier', 'clear_variable',
      'clamp_temp_variable', 'has_idea', 'is_ai', 'country_event', 'has_political_power', 'add_political_power']);
    const translated = nodes.map(node => {
      if (!primitives.has(node.key)) return node;
      const name = `native_test_primitive_${this.nativeCalls.size}`;
      this.nativeCalls.set(name, () => {
        const { key, value } = node;
        if (key === 'has_country_flag') return this.flags.has(value);
        if (key === 'set_country_flag') { this.flags.add(value); return true; }
        if (key === 'clr_country_flag') { this.flags.delete(value); return true; }
        if (key === 'has_dynamic_modifier') return this.flags.has('native_modifier_applied');
        if (key === 'add_dynamic_modifier') { this.flags.add('native_modifier_applied'); return true; }
        if (key === 'remove_dynamic_modifier') { this.flags.delete('native_modifier_applied'); this.applied.clear(); return true; }
        if (key === 'force_update_dynamic_modifier') {
          this.applied = new Map(dynamic.map(entry => [entry.key, this.value(entry.value)])); return true;
        }
        if (key === 'clear_variable') { this.regularVars.delete(value); return true; }
        if (key === 'has_idea') return this.ideas.has(value);
        if (key === 'is_ai') return this.ai === (value === 'yes');
        if (key === 'country_event') { this.events.push(this.field(value, 'id')); return true; }
        if (key === 'has_political_power') {
          const a = this.value('political_power'), b = this.value(value);
          return node.op === '<' ? a < b : node.op === '>' ? a > b : a === b;
        }
        if (key === 'add_political_power') { this.write('political_power', this.value('political_power') + this.value(value), false); return true; }
        const variable = this.field(value, 'var'), min = this.field(value, 'min'), max = this.field(value, 'max');
        let amount = this.value(variable);
        if (max !== undefined && amount > this.value(max)) amount = this.value(max);
        if (min !== undefined && amount < this.value(min)) amount = this.value(min);
        this.write(variable, amount); return true;
      });
      // The base VM dispatches only known helpers. Primitive shims are explicit
      // fixtures and do not preinitialize any production helper output storage.
      definitions.set(name, []);
      return { key: name, op: '=', value: 'yes' };
    });
    return super.eval(translated);
  }
}
const failures = [], scenarios = [];
function check(name, body) {
  try { body(); scenarios.push(name); }
  catch (error) { failures.push({ name, error: error.message }); }
}
for (const ratio of [5000, 2500]) {
  for (const ordinary of ['-0.25', '0', '0.25', '-1']) check(`all_native_keys_${ratio}_${ordinary}`, () => {
    const vm = new NativeVM(); vm.regularVars.set('global.black_friday_discount_ratio', ticks(ratio));
    for (const entry of dynamic) vm.ordinary.set(entry.key, ticks(ordinary));
    vm.run('black_friday_native_sale_apply');
    const base = ticks(ordinary) + S;
    const expected = base > 0n ? base * (ticks(ratio) / 10000n - S) / S : 0n;
    for (const entry of dynamic) assert.equal(vm.applied.get(entry.key), expected, entry.key);
    vm.run('black_friday_native_sale_apply');
    for (const entry of dynamic) assert.equal(vm.applied.get(entry.key), expected, `refresh ${entry.key}`);
    vm.ordinary.set('economy_cost_factor', ticks('0.5'));
    vm.run('black_friday_native_sale_apply');
    assert.equal(vm.applied.get('economy_cost_factor'), ticks('1.5') * (ticks(ratio) / 10000n - S) / S);
    vm.run('black_friday_native_sale_remove');
    assert.equal(vm.applied.size, 0);
    for (const entry of dynamic) assert(!vm.regularVars.has(entry.value), `expiry ${entry.value}`);
  });
  check(`linked_advisor_discount_${ratio}`, () => {
    const vm = new NativeVM(); vm.regularVars.set('global.black_friday_discount_ratio', ticks(ratio));
    vm.ordinary.set('army_advisor_cost_factor', ticks('-0.5'));
    vm.run('black_friday_native_sale_apply');
    assert.equal(vm.applied.get('army_chief_cost_factor'), ticks('0.5') * (ticks(ratio) / 10000n - S) / S);
    vm.run('black_friday_native_sale_apply');
    assert.equal(vm.applied.get('army_chief_cost_factor'), ticks('0.5') * (ticks(ratio) / 10000n - S) / S);
  });
}
function achievementFixture() {
  const vm = new NativeVM();
  definitions.set('black_friday_achievement_is_valid_sale', []);
  definitions.set('black_friday_engine_purchase_can_credit', []);
  definitions.set('black_friday_add_committed_achievement_family', []);
  vm.nativeCalls.set('black_friday_add_committed_achievement_family', () => { vm.credit.push(vm.value('black_friday_purchase_family_id')); return true; });
  // Native slot trigger/meta text evaluation is outside this model. This fixture
  // intentionally creates its outputs inside a helper frame, as production does.
  definitions.set('black_friday_engine_purchase_count_slots', parse('set_temp_variable = { black_friday_engine_advisor_count = fixture_advisors } set_temp_variable = { black_friday_engine_staff_count = fixture_staff }'));
  vm.regularVars.set('fixture_advisors', ticks(1)); vm.regularVars.set('fixture_staff', ticks(2));
  vm.regularVars.set('global.black_friday_sale_sequence', ticks(1));
  vm.regularVars.set('political_power', ticks(100)); vm.regularVars.set('command_power', ticks(20));
  vm.ideas = new Set(['civilian_economy', 'export_focus', 'volunteer_only']);
  return vm;
}
check('native_law_and_slot_snapshot_survives_helper_return', () => {
  const vm = achievementFixture(); vm.run('black_friday_engine_purchase_snapshot');
  assert.equal(vm.value('black_friday_engine_snapshot_economy_law'), constants.get('constant:black_friday_engine_law.civilian_economy'));
  assert.equal(vm.value('black_friday_engine_snapshot_trade_law'), constants.get('constant:black_friday_engine_law.export_focus'));
  assert.equal(vm.value('black_friday_engine_snapshot_mobilization_law'), constants.get('constant:black_friday_engine_law.volunteer_only'));
  assert.equal(vm.value('black_friday_engine_snapshot_advisor_count'), ticks(1));
  assert.equal(vm.value('black_friday_engine_snapshot_staff_count'), ticks(2));
});
check('native_credit_detects_law_and_new_slots', () => {
  const vm = achievementFixture(); vm.run('black_friday_engine_purchase_snapshot');
  vm.ideas.delete('civilian_economy'); vm.ideas.add('war_economy');
  vm.regularVars.set('fixture_advisors', ticks(2)); vm.regularVars.set('fixture_staff', ticks(3));
  vm.regularVars.set('political_power', ticks(75));
  vm.run('black_friday_engine_purchase_credit');
  assert.deepEqual(vm.credit, ['laws', 'personnel', 'officer_corps'].map(key => constants.get(`constant:universal_cost_family.${key}`)));
  assert(!vm.regularVars.has('black_friday_engine_snapshot_sale_sequence'));
});
check('unchanged_native_state_does_not_credit', () => {
  const vm = achievementFixture(); vm.run('black_friday_engine_purchase_snapshot'); vm.run('black_friday_engine_purchase_credit');
  assert.deepEqual(vm.credit, []);
});
check('free_law_and_slot_changes_do_not_credit', () => {
  const vm = achievementFixture(); vm.run('black_friday_engine_purchase_snapshot');
  vm.ideas.delete('civilian_economy'); vm.ideas.add('war_economy');
  vm.regularVars.set('fixture_advisors', ticks(2)); vm.regularVars.set('fixture_staff', ticks(3));
  vm.run('black_friday_engine_purchase_credit'); assert.deepEqual(vm.credit, []);
});
check('staff_appointment_with_command_payment_credits', () => {
  const vm = achievementFixture(); vm.run('black_friday_engine_purchase_snapshot');
  vm.regularVars.set('fixture_staff', ticks(3)); vm.regularVars.set('command_power', ticks(10));
  vm.run('black_friday_engine_purchase_credit');
  assert.deepEqual(vm.credit, ['officer_corps', 'command_power'].map(key => constants.get(`constant:universal_cost_family.${key}`)));
});
for (const [ratio, payable] of [[10000, 50], [5000, 25], [2500, 13]]) {
  check(`simple_cost_affordability_and_payment_${ratio}`, () => {
    const vm = new NativeVM();
    for (const [key, value] of [['ids', 26], ['ratios', ratio], ['priorities', 500], ['eligibility_masks', 0]])
      vm.arrays.set(`global.universal_cost_source_${key}`, ratio === 10000 ? [] : [ticks(value)]);
    if (ratio !== 10000) vm.flags.add('black_friday_active');
    vm.regularVars.set('global.universal_cost_custom_quote_cache_valid', S);
    vm.regularVars.set('political_power', ticks(payable));
    vm.set('black_friday_simple_cost_ordinary', 50).set('black_friday_simple_cost_kind', 1);
    assert(vm.run('black_friday_simple_cost_is_affordable'));
    // Achievement proof is separately covered by the public receipt suite.
    definitions.set('black_friday_credit_sale_purchase', []);
    vm.set('black_friday_simple_cost_paid', 0); vm.run('black_friday_simple_cost_pay');
    assert.equal(vm.value('political_power'), 0n); assert.equal(vm.value('black_friday_simple_cost_paid'), S);
    vm.run('black_friday_simple_cost_pay'); assert.equal(vm.value('political_power'), 0n);
    assert.equal(vm.value('black_friday_simple_cost_paid'), 0n);
    assert.equal(vm.run('black_friday_simple_cost_is_affordable'), false);
  });
}
for (const reason of ['active', 'fired', 'disabled', 'paused', 'world_end', 'reserved', 'below_chaos']) {
  check(`manual_failure_${reason}_once`, () => {
    const vm = new NativeVM();
    for (const [trigger, result] of Object.entries({
      black_friday_is_active: reason === 'active', black_friday_is_fired: reason === 'fired',
      black_friday_is_disabled: reason === 'disabled', black_friday_event_system_is_running: reason !== 'paused',
      black_friday_is_reserved: reason === 'reserved',
    })) {
      definitions.set(trigger, []); vm.nativeCalls.set(trigger, () => result);
    }
    if (reason === 'world_end') vm.flags.add('world_end');
    definitions.set('black_friday_initialize_runtime', []);
    definitions.set('black_friday_select_or_activate', []);
    vm.nativeCalls.set('black_friday_select_or_activate', () => {
      vm.regularVars.set('global.black_friday_launch_result', ticks(0)); return true;
    });
    vm.regularVars.set('global.black_friday_dispatch_mode', ticks(0));
    vm.run('black_friday_entry_event');
    assert.equal(vm.value('black_friday_entry_failure_reason'), constants.get(`constant:black_friday_entry_failure.${reason}`));
    assert.deepEqual(vm.events, ['chaosx.nr26.3']);
    vm.run('black_friday_entry_event');
    assert.deepEqual(vm.events, ['chaosx.nr26.3']);
    vm.flags.delete('black_friday_entry_notice_shown');
    vm.events = []; vm.regularVars.set('global.black_friday_dispatch_mode', constants.get('constant:black_friday_event.dispatch_natural'));
    vm.run('black_friday_entry_event'); assert.deepEqual(vm.events, []);
    vm.ai = true; vm.regularVars.set('global.black_friday_dispatch_mode', constants.get('constant:black_friday_event.dispatch_force'));
    vm.run('black_friday_entry_event'); assert.deepEqual(vm.events, []);
  });
}
const stale = new NativeVM(); stale.regularVars.set('global.black_friday_discount_ratio', ticks(2500));
stale.run('black_friday_native_sale_apply');
stale.ordinary.set('political_advisor_cost_factor', ticks('-0.25'));
const staleFactor = S + stale.value('modifier@political_advisor_cost_factor');
// This is a documented completion blocker, not a passing safety assertion.
const limitations = [{ name: 'ordinary_factor_changed_after_last_refresh', ordinary: '-0.25', ratio: 2500,
  storedContribution: String(stale.applied.get('political_advisor_cost_factor')),
  totalFactorBeforeRefresh: String(staleFactor), expectedFactor: String(ticks('0.1875')) }];
console.log(JSON.stringify({ nativeKeys: dynamic.length, passed: scenarios, failures, limitations }, null, 2));
if (failures.length && !process.argv.includes('--baseline')) process.exitCode = 1;
