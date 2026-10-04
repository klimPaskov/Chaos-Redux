"""Execute the captured-UWR decision helper with only the camp result stubbed."""
from pathlib import Path
import re
from foundation_source_tests import ROOT, Runtime, get, parse, prime_existing_custody

source = (ROOT / 'common/scripted_effects/005_soviet_collapse_effects.txt').read_text(encoding='utf-8-sig')
start = source.index('soviet_collapse_dismantle_uwr_aftermath_site = {')
end = source.index('soviet_collapse_secure_uwr_aftermath_site = {', start)
helper = get(parse(source[start:end]), 'soviet_collapse_dismantle_uwr_aftermath_site')
review_start = source.index('soviet_collapse_uwr_aftermath_validate_target = {', start)
review_end = source.index('soviet_collapse_kmb_apply_basin_resource_surge = {', review_start)
review_helpers = parse(source[review_start:review_end])
decision_source = (ROOT / 'common/decisions/005_soviet_collapse_decisions.txt').read_text(encoding='utf-8-sig')
decision_start = decision_source.index('uwr_dismantle_captured_blacksite = {')
decision_end = decision_source.index('uwr_secure_captured_blacksite = {', decision_start)
decision = get(parse(decision_source[decision_start:decision_end]), 'uwr_dismantle_captured_blacksite')
availability = get(get(get(get(decision, 'available'), 'FROM'), 'custom_trigger_tooltip'), 'hidden_trigger')
def decision_body(name):
    start = decision_source.index(name + ' = {')
    opening = decision_source.index('{', start)
    depth = 1
    index = opening + 1
    while depth:
        depth += (decision_source[index] == '{') - (decision_source[index] == '}')
        index += 1
    return get(parse(decision_source[start:index]), name)

other_availability = {
    name: get(get(get(get(decision_body(name), 'available'), 'FROM'), 'custom_trigger_tooltip'), 'hidden_trigger')
    for name in ('uwr_secure_captured_blacksite', 'uwr_exploit_captured_blacksite')
}
trigger_source = (ROOT / 'common/scripted_triggers/005_soviet_collapse_triggers.txt').read_text(encoding='utf-8-sig')
trigger_start = trigger_source.index('soviet_collapse_uwr_aftermath_requires_camp_receipt = {')
trigger_end = trigger_source.index('has_soviet_collapse_uwr_aftermath_site = {', trigger_start)
camp_obligation = get(parse(trigger_source[trigger_start:trigger_end]), 'soviet_collapse_uwr_aftermath_requires_camp_receipt')
balance = (ROOT / 'common/script_constants/005_soviet_collapse_constants.txt').read_text(encoding='utf-8-sig')
balance = balance.split('soviet_collapse_uwr_aftermath = {', 1)[1].split('\n}', 1)[0]
keys = ('dismantlement_cost', 'dismantlement_stability', 'remove_facility_levels',
        'containment_cost', 'containment_breakthrough_gain', 'containment_stability',
        'exploitation_cost', 'exploitation_breakthrough_gain', 'exploitation_army_experience', 'exploitation_stability')
values = {key: float(re.search(r'(?m)^\s*' + key + r'\s*=\s*(-?[0-9.]+)', balance)[1]) for key in keys}

completion_stub = get(parse('''
camp_rework_complete_dismantlement = {
	add_to_temp_variable = { mock_camp_complete_calls = 1 }
	if = {
		limit = {
			has_state_flag = mock_camp_accept
			check_variable = { camp_rework_enemy_liberation = constant:camp_admin_value.one }
			camp_admin_site_rows_reconciled = yes
			NOT = { has_state_flag = camp_admin_closed }
		}
		set_temp_variable = { camp_rework_dismantlement_completion_accepted = constant:camp_admin_value.one }
	}
	else = { set_temp_variable = { camp_rework_dismantlement_completion_accepted = constant:camp_admin_value.zero } }
}
'''), 'camp_rework_complete_dismantlement')
target_stub = get(parse('''
is_soviet_collapse_uwr_aftermath_target_state = {
	has_state_flag = soviet_collapse_uwr_blacksite_aftermath_site
}
'''), 'is_soviet_collapse_uwr_aftermath_target_state')


def fixture(camp=True, ordinary=False, gulag=False, accepted=True, target=True, execute=True):
    runtime = Runtime()
    country = runtime.country('ENG')
    site = runtime.state('U1', 'ENG')
    runtime.effects['soviet_collapse_dismantle_uwr_aftermath_site'] = helper
    for name in ('soviet_collapse_uwr_aftermath_validate_target', 'soviet_collapse_secure_uwr_aftermath_site', 'soviet_collapse_exploit_uwr_aftermath_site'):
        runtime.effects[name] = get(review_helpers, name)
    runtime.effects['camp_rework_complete_dismantlement'] = completion_stub
    runtime.triggers['is_soviet_collapse_uwr_aftermath_target_state'] = target_stub
    runtime.triggers['soviet_collapse_uwr_aftermath_requires_camp_receipt'] = camp_obligation
    for key, value in values.items():
        runtime.constants['soviet_collapse_uwr_aftermath.' + key] = value
    site['flags'].add('soviet_collapse_uwr_blacksite_aftermath_site')
    site['biowarfare_facility'] = 1
    site['cw_facility'] = 1
    if camp:
        site['flags'].add('camp_rework_experiment_site')
    elif ordinary:
        prime_existing_custody(runtime, 'U1', 10)
        if gulag:
            site['concentration_camp'] = 0
            site['gulag_labor_camp_network'] = 1
    elif not ordinary:
        site['concentration_camp'] = 0
        site['flags'].discard('camp_admin_initialized')
        site['flags'].discard('camp_rework_site_active')
    if accepted:
        site['flags'].add('mock_camp_accept')
    if not target:
        site['flags'].discard('soviet_collapse_uwr_blacksite_aftermath_site')
    runtime.targets['soviet_collapse_uwr_aftermath_state'] = 'U1'
    if execute:
        country['political_power'] -= values['dismantlement_cost']  # native decision charge
        runtime.run('soviet_collapse_dismantle_uwr_aftermath_site', 'ENG')
    return runtime, country, site


def test_receipt_guard():
    before, _, _ = fixture(execute=False)
    assert before.cond(availability, 'U1')
    success, country, site = fixture()
    assert success.temp['mock_camp_complete_calls'] == 1
    assert success.temp['camp_rework_enemy_liberation'] == 0
    assert 'soviet_collapse_uwr_aftermath_dismantled' in site['flags']
    assert site['biowarfare_facility'] == 0
    assert country['political_power'] == 100 - values['dismantlement_cost']
    assert abs(country['stability'] - values['dismantlement_stability']) < 1e-8

    rejected, country, site = fixture(accepted=False)
    assert rejected.temp['mock_camp_complete_calls'] == 1
    assert rejected.temp['soviet_collapse_uwr_aftermath_dismantle_accepted'] == 0
    assert country['political_power'] == 100
    assert country.get('stability', 0) == 0
    assert site['biowarfare_facility'] == 1
    assert 'soviet_collapse_uwr_blacksite_aftermath_site' in site['flags']

    invalid, _, site = fixture(execute=False)
    site['arrays']['camp_admin_row_origins'].append('unmatched')
    assert not invalid.cond(availability, 'U1')
    site['arrays']['camp_admin_row_origins'].pop()
    site['flags'].add('camp_admin_closed')
    assert not invalid.cond(availability, 'U1')

    ordinary_before, _, _ = fixture(camp=False, ordinary=True, execute=False)
    assert ordinary_before.cond(availability, 'U1')
    ordinary, country, site = fixture(camp=False, ordinary=True)
    assert ordinary.temp['mock_camp_complete_calls'] == 1
    assert country['political_power'] == 100 - values['dismantlement_cost']
    assert 'soviet_collapse_uwr_aftermath_dismantled' in site['flags']
    inherited_gulag, _, _ = fixture(camp=False, ordinary=True, gulag=True)
    assert inherited_gulag.temp['mock_camp_complete_calls'] == 1
    co_located, country, site = fixture(camp=False, ordinary=True, execute=False)
    site['arrays']['camp_admin_row_origins'].append('unmatched')
    assert not co_located.cond(availability, 'U1')
    country['political_power'] -= values['dismantlement_cost']
    co_located.run('soviet_collapse_dismantle_uwr_aftermath_site', 'ENG')
    assert co_located.temp['mock_camp_complete_calls'] == 1
    assert co_located.temp['soviet_collapse_uwr_aftermath_dismantle_accepted'] == 0
    assert country['political_power'] == 100 and country.get('stability', 0) == 0
    assert site['biowarfare_facility'] == 1 and 'soviet_collapse_uwr_blacksite_aftermath_site' in site['flags']
    closed_live, _, site = fixture(camp=False, ordinary=True, execute=False)
    site['flags'].add('camp_admin_closed')
    assert not closed_live.cond(availability, 'U1')
    closed_empty, country, site = fixture(camp=False, ordinary=True, execute=False)
    site['flags'].add('camp_admin_closed')
    site['camp_admin_detainees_k'] = 0
    site['arrays']['camp_admin_row_amounts_k'][0] = 0
    assert closed_empty.cond(availability, 'U1')
    country['political_power'] -= values['dismantlement_cost']
    closed_empty.run('soviet_collapse_dismantle_uwr_aftermath_site', 'ENG')
    assert closed_empty.temp.get('mock_camp_complete_calls', 0) == 0
    assert site['concentration_camp'] > 0 and site['biowarfare_facility'] == 0

    facility_before, _, _ = fixture(camp=False, execute=False)
    assert facility_before.cond(availability, 'U1')
    facility, country, site = fixture(camp=False)
    assert facility.temp.get('mock_camp_complete_calls', 0) == 0
    assert 'soviet_collapse_uwr_aftermath_dismantled' in site['flags']
    assert country['political_power'] == 100 - values['dismantlement_cost']
    assert site['cw_facility'] == 0

    stale, country, site = fixture(target=False)
    assert country['political_power'] == 100
    assert country.get('stability', 0) == 0
    assert 'soviet_collapse_uwr_aftermath_dismantled' not in site['flags']


def test_other_aftermath_outcomes():
    for action, decision_id, cost_key, gain_key, flag in (
        ('soviet_collapse_secure_uwr_aftermath_site', 'uwr_secure_captured_blacksite', 'containment_cost', 'containment_breakthrough_gain', 'soviet_collapse_uwr_aftermath_contained'),
        ('soviet_collapse_exploit_uwr_aftermath_site', 'uwr_exploit_captured_blacksite', 'exploitation_cost', 'exploitation_breakthrough_gain', 'soviet_collapse_uwr_aftermath_exploited'),
    ):
        accepted, country, site = fixture(camp=False, execute=False)
        assert accepted.cond(other_availability[decision_id], 'U1')
        country['political_power'] -= values[cost_key]
        accepted.run(action, 'ENG')
        assert flag in site['flags'] and 'soviet_collapse_uwr_blacksite_aftermath_site' not in site['flags']
        assert country['political_power'] == 100 - values[cost_key]
        assert country['breakthrough']['specialization_biowarfare'] == values[gain_key]
        assert country['breakthrough']['specialization_cw'] == values[gain_key]
        if action == 'soviet_collapse_secure_uwr_aftermath_site':
            assert country['stability'] == values['containment_stability'] and country.get('army_experience', 0) == 0
        else:
            assert country['stability'] == values['exploitation_stability']
            assert country['army_experience'] == values['exploitation_army_experience']
        first_stability = country['stability']
        country['political_power'] -= values[cost_key]
        accepted.run(action, 'ENG')
        assert country['political_power'] == 100 - values[cost_key]
        assert country['stability'] == first_stability
        assert country['breakthrough']['specialization_biowarfare'] == values[gain_key]

        stale, country, site = fixture(camp=False, target=False, execute=False)
        assert not stale.cond(other_availability[decision_id], 'U1')
        country['political_power'] -= values[cost_key]
        stale.run(action, 'ENG')
        assert country['political_power'] == 100 and country.get('stability', 0) == 0
        assert country.get('breakthrough', {}) == {} and country.get('army_experience', 0) == 0
        assert flag not in site['flags'] and site['biowarfare_facility'] == 1


if __name__ == '__main__':
    test_receipt_guard()
    test_other_aftermath_outcomes()
    print('Captured-UWR camp receipt and three aftermath outcome scenarios passed; engine execution remains unproved.')
