"""Exercise the production Italy local-modifier helpers with engine primitives mocked."""
from pathlib import Path
from foundation_source_tests import ROOT, Runtime, get, parse

colonial = parse((ROOT / 'common/scripted_effects/camp_repression_colonial_country_effects.txt').read_text(encoding='utf-8-sig'))
triggers = parse((ROOT / 'common/scripted_triggers/camp_repression_rework_triggers.txt').read_text(encoding='utf-8-sig'))
constants = parse((ROOT / 'common/script_constants/camp_repression_rework_constants.txt').read_text(encoding='utf-8-sig'))
modifier = get(parse((ROOT / 'common/dynamic_modifiers/camp_repression_italy_security_dynamic_modifiers.txt').read_text(encoding='utf-8-sig')), 'ita_colonial_security_sweep_state')


def fixture():
    runtime = Runtime()
    runtime.country('ITA')
    runtime.country('GER')
    site = runtime.state('LIB', 'ITA')
    site['cores'] = {'LBA'}
    for name in ('camp_rework_italy_begin_security_sweep_state', 'camp_rework_italy_end_security_sweep_state', 'camp_rework_italy_clear_security_sweep_state'):
        runtime.effects[name] = get(colonial, name)
    runtime.triggers['camp_rework_italy_security_battalions_site_ready'] = []  # Selected paid site already validated.
    runtime.triggers['camp_rework_italy_security_sweep_state_active'] = get(triggers, 'camp_rework_italy_security_sweep_state_active')
    for category in ('camp_rework_timing', 'camp_rework_italy_security_modifier'):
        for key, _, value in get(constants, category):
            if key != 'schema': runtime.constants[category + '.' + key] = float(value)
    return runtime, site


def run_scenarios():
    site_ready = get(triggers, 'camp_rework_italy_security_battalions_site_ready')
    assert ('is_italy_libya_repression_pool_state', '=', 'yes') in site_ready
    success_site = get(get(triggers, 'camp_rework_italy_security_sweep_requirements_met'), 'var:ita_security_sweep_state_id')
    assert ('camp_rework_italy_security_sweep_state_active', '=', 'yes') in success_site
    assert get(success_site, 'has_dynamic_modifier') == [
        ('modifier', '=', 'ita_colonial_security_sweep_state'),
        ('scope', '=', 'var:genocide_responsible_country')]
    assert get(modifier, 'icon') == 'GFX_modifiers_generic_defense'
    assert get(modifier, 'enable') == [('camp_rework_italy_security_sweep_state_active', '=', 'yes')]
    assert get(modifier, 'remove_trigger') == [('NOT', '=', [('camp_rework_italy_security_sweep_state_active', '=', 'yes')])]
    assert all(get(modifier, key) == 'constant:camp_rework_italy_security_modifier.' + key for key in
               ('required_garrison_factor', 'resistance_damage_to_garrison', 'resistance_target'))
    italian = get(constants, 'camp_rework_italy_security_modifier')
    cbrn = get(parse((ROOT / 'common/script_constants/cbrn_occupation_constants.txt').read_text(encoding='utf-8-sig')),
               'cbrn_occupation_state_modifier')
    for italy_key, cbrn_key in (('required_garrison_factor', 'active_required_garrison'),
                                ('resistance_damage_to_garrison', 'active_garrison_damage'),
                                ('resistance_target', 'active_resistance_target')):
        assert 0 < abs(float(get(italian, italy_key))) < abs(float(get(cbrn, cbrn_key)))

    runtime, site = fixture()
    runtime.run('camp_rework_italy_begin_security_sweep_state', 'LIB')
    assert runtime.temp['camp_rework_italy_security_state_applied'] == 1
    assert runtime.temp['camp_rework_italy_security_duration_days'] == (
        runtime.constants['camp_rework_timing.ita_colonial_security_sweep_days'] +
        runtime.constants['camp_rework_timing.ita_security_sweep_flag_grace_days'])
    assert 'ita_security_sweep_active' in site['flags']
    assert site['mods'] == {'ita_colonial_security_sweep_state'}
    assert runtime.cond(runtime.triggers['camp_rework_italy_security_sweep_state_active'], 'LIB')
    site['cores'].clear()
    assert not runtime.cond(runtime.triggers['camp_rework_italy_security_sweep_state_active'], 'LIB')
    site['cores'].add('LBA')
    site['cores'].add('ITA')
    assert not runtime.cond(runtime.triggers['camp_rework_italy_security_sweep_state_active'], 'LIB')
    site['cores'].remove('ITA')
    runtime.run('camp_rework_italy_begin_security_sweep_state', 'LIB')
    assert site['mods'] == {'ita_colonial_security_sweep_state'}  # Repeat refresh, never stack.

    runtime.scopes['ITA']['ita_security_sweep_state_id'] = 'LIB'
    runtime.run('camp_rework_italy_clear_security_sweep_state', 'ITA')
    assert 'ita_security_sweep_active' not in site['flags'] and not site['mods']
    runtime.run('camp_rework_italy_clear_security_sweep_state', 'ITA')
    assert not site['mods']  # Cleanup is idempotent.

    runtime.run('camp_rework_italy_begin_security_sweep_state', 'LIB')
    site['controller'] = 'GER'
    assert not runtime.cond(runtime.triggers['camp_rework_italy_security_sweep_state_active'], 'LIB')
    runtime.run('camp_rework_italy_end_security_sweep_state', 'LIB')
    assert not site['mods'] and 'ita_security_sweep_active' not in site['flags']
    site['controller'] = 'ITA'
    assert not runtime.cond(runtime.triggers['camp_rework_italy_security_sweep_state_active'], 'LIB')
    assert 'ita_colonial_security_sweep_state' not in site['mods']

    for modifier_accepts in (True, False):
        paid, paid_site = fixture()
        country = paid.scopes['ITA']
        guard_cost = float(get(get(constants, 'camp_rework_cost'), 'guard_pp'))
        country['flags'].discard('camp_admin_initialized')  # Legacy Italy decision before administration cutover.
        country['camp_selected_state_id'] = 'LIB'
        country['political_power'] = 100 - guard_cost  # Native decision or Ledger charge.
        paid.temp['camp_rework_italy_security_pp_paid'] = guard_cost
        paid.effects['camp_rework_italy_raise_security_battalions'] = get(colonial, 'camp_rework_italy_raise_security_battalions')
        paid.effects['camp_rework_consume_colonial_security_battalion_resources'] = get(
            parse('camp_rework_consume_colonial_security_battalion_resources = { set_temp_variable = { mock_non_pp_debits = 1 } }'),
            'camp_rework_consume_colonial_security_battalion_resources')
        paid.effects['camp_rework_update_colonial_country_monthly_bridge'] = []
        paid.triggers['camp_rework_italy_security_battalions_resources_ready'] = []  # Exact stock tested in civil scenarios.
        for key, _, value in get(constants, 'camp_rework_country_value'):
            if key != 'schema': paid.constants['camp_rework_country_value.' + key] = float(value)
        paid.constants['camp_rework_cost.guard_pp'] = guard_cost
        if not modifier_accepts:
            paid.effects['camp_rework_italy_begin_security_sweep_state'] = get(
                parse('camp_rework_italy_begin_security_sweep_state = { set_temp_variable = { camp_rework_italy_security_state_applied = 0 } }'),
                'camp_rework_italy_begin_security_sweep_state')
        paid.run('camp_rework_italy_raise_security_battalions', 'ITA')
        assert paid.temp['camp_rework_italy_security_action_accepted'] == int(modifier_accepts)
        assert paid.temp.get('mock_non_pp_debits', 0) == int(modifier_accepts)
        assert country['political_power'] == (100 - guard_cost if modifier_accepts else 100)
        assert ('ita_colonial_security_sweep' in country.get('missions', set())) == modifier_accepts
        assert ('ita_colonial_security_sweep_state' in paid_site['mods']) == modifier_accepts

    for cutover_flag in ('camp_admin_initialized', 'camp_admin_civil_initialized'):
        blocked, blocked_site = fixture()
        country = blocked.scopes['ITA']
        cost = float(get(get(constants, 'camp_rework_cost'), 'guard_pp'))
        country['flags'].add(cutover_flag)
        country['camp_selected_state_id'] = 'LIB'
        country['political_power'] = 100 - cost
        blocked.temp['camp_rework_italy_security_pp_paid'] = cost
        blocked.constants['camp_rework_cost.guard_pp'] = cost
        blocked.effects['camp_rework_italy_raise_security_battalions'] = get(colonial, 'camp_rework_italy_raise_security_battalions')
        blocked.triggers['camp_rework_italy_security_battalions_resources_ready'] = []
        blocked.run('camp_rework_italy_raise_security_battalions', 'ITA')
        assert blocked.temp['camp_rework_italy_security_action_accepted'] == 0
        assert country['political_power'] == 100
        assert not blocked_site['mods'] and 'ita_colonial_security_sweep' not in country.get('missions', set())

    print('Italy modifier lifecycle and paid success/refund source scenarios passed; native modifier execution remains unproved.')


if __name__ == '__main__':
    run_scenarios()
