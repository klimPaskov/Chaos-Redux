"""Exercise the production Soviet national release gate and effect with mocked engine primitives."""
from pathlib import Path
import json

from foundation_source_tests import parse, get, prime_existing_custody
from major_countries_source_tests import CountryRuntime
import black_friday_sale_prices as sale


ROOT = Path(__file__).resolve().parents[4]
SALE_RATIO = sale.RATIO_BASIS


def scenario(second_k=5, invalid_second=False, population_k=100):
    runtime = CountryRuntime()
    sale.install(runtime, SALE_RATIO)
    country = runtime.country('SOV')
    country.update(government='communism', war=True, forced_labor_quota=30,
                   famine_pressure=20, old_movement_grievance=15, camp_policy_reform=0,
                   political_power=100)
    runtime.root = 'SOV'
    old_target = runtime.target
    runtime.target = lambda value, scope, prev: runtime.root if value == 'ROOT' else old_target(value, scope, prev)
    for name in ('A', 'B'):
        site = runtime.state(name, 'SOV', population=population_k, buildings=2)
        site['gulag_labor_camp_network'] = 2
        site['camp_admin_responsible_country'] = 'SOV'
        prime_existing_custody(runtime, name, 10 if name == 'A' else second_k)
    if invalid_second:
        runtime.scopes['B']['arrays']['camp_admin_row_amounts_k'][0] -= 1
    runtime.triggers.update({name: body for name, _, body in parse(
        (ROOT / 'common/scripted_triggers/camp_repression_rework_triggers.txt').read_text(encoding='utf-8-sig'))})
    source = parse((ROOT / 'common/scripted_effects/camp_repression_major_country_effects.txt').read_text(encoding='utf-8-sig'))
    runtime.effects['camp_rework_soviet_release_prisoners_for_military_service'] = get(
        source, 'camp_rework_soviet_release_prisoners_for_military_service')
    for file, names in [
        ('camp_repression_action_dispatcher_effects.txt', ('camp_rework_dispatch_soviet_action',)),
        ('camp_repression_rework_effects.txt', ('camp_rework_route_country_specific_action',
                                               'camp_rework_record_country_gui_action_cooldown',
                                               'camp_rework_apply_country_gui_slot_cooldown')),
    ]:
        entries = parse((ROOT / 'common/scripted_effects' / file).read_text(encoding='utf-8-sig'))
        for name in names:
            runtime.effects[name] = get(entries, name)
    for category, _, body in parse((ROOT / 'common/script_constants/camp_repression_rework_constants.txt').read_text(encoding='utf-8-sig')):
        if isinstance(body, list):
            for name, _, value in body:
                if name != 'schema' and not isinstance(value, list):
                    try:
                        runtime.constants[f'{category}.{name}'] = float(value)
                    except (TypeError, ValueError):
                        pass
    for name in ('camp_rework_soviet_initialize_country_values',
                 'camp_rework_soviet_refresh_famine_states', 'camp_rework_recalculate_country_values'):
        runtime.effects[name] = []
    decision = parse((ROOT / 'common/decisions/camp_repression_major_country_decisions.txt').read_text(encoding='utf-8-sig'))
    block = next(body for _, _, category in decision if isinstance(category, list)
                 for name, _, body in category if name == 'sov_release_prisoners_for_military_service')
    availability = get(block, 'available')
    tooltip = get(availability, 'custom_trigger_tooltip')
    assert get(tooltip, 'tooltip') == 'sov_release_prisoners_for_military_service_rows_tt'
    assert get(tooltip, 'camp_rework_soviet_service_release_ready') == 'yes'
    assert get(block, 'cost') == 'global.black_friday_price_camp_rework_cost_review_pp'
    runtime.release_decision = block
    return runtime, country, availability


def execute_paid(runtime, country):
    quote = runtime.val(get(runtime.release_decision, 'cost'), 'SOV')
    country['political_power'] -= quote  # Native decision debit before complete_effect.
    runtime.execute(get(runtime.release_decision, 'complete_effect'), 'SOV')
    assert runtime.temp['camp_rework_native_pp_paid'] == 0  # The charged amount is consumed by refund or credit.


def decision_available(runtime, block):
    # The source interpreter omits the UI-only tooltip wrapper, not its trigger.
    def unwrap(entries):
        result = []
        for name, operator, value in entries:
            if name == 'custom_trigger_tooltip':
                result.extend(unwrap([entry for entry in value if entry[0] != 'tooltip']))
            else:
                result.append((name, operator, unwrap(value) if isinstance(value, list) else value))
        return result

    return runtime.cond(unwrap(block), 'SOV')


def policy_description_key(runtime):
    source = parse((ROOT / 'common/scripted_localisation/camp_administration_country_localisation.txt').read_text(encoding='utf-8-sig'))
    block = next(body for name, _, body in source if name == 'defined_text'
                 and get(body, 'name') == 'GetSovServiceReleaseConsequence')
    return next(get(text, 'localization_key') for name, _, text in block if name == 'text'
                and (get(text, 'trigger') is None or runtime.cond(get(text, 'trigger'), 'SOV')))


def PRICE():
    return sale.sale_prices(SALE_RATIO)['global.black_friday_price_camp_rework_cost_review_pp']


def run_cases():
    results = []
    runtime, country, available = scenario(second_k=10, invalid_second=True)
    assert policy_description_key(runtime) == 'sov_release_prisoners_first_consequence'
    assert not decision_available(runtime, available)
    before = [(runtime.scopes[site]['camp_admin_detainees_k'], runtime.scopes[site]['state_population_k']) for site in ('A', 'B')]
    execute_paid(runtime, country)
    assert country['political_power'] == 100 and country['forced_labor_quota'] == 30 and sale.credits(runtime) == 0
    assert country['famine_pressure'] == 20 and country['old_movement_grievance'] == 15
    assert country['camp_policy_reform'] == 0 and country['camp_admin_country_last_released_k'] == 0
    assert country['camp_admin_total_released_k'] == 0
    assert before == [(runtime.scopes[site]['camp_admin_detainees_k'], runtime.scopes[site]['state_population_k']) for site in ('A', 'B')]
    assert all('camp_admin_census_intake_closed' not in runtime.scopes[site]['flags'] for site in ('A', 'B'))
    assert 'camp_gui_country_action_3_cooldown' not in country['flags']
    assert 'camp_rework_soviet_service_release_policy_enacted' not in country['flags']
    results.append({'case': 'mixed_valid_invalid_rows', 'refund_pp': PRICE(), 'actual_release_people': 0})

    runtime, country, available = scenario(second_k=5)
    assert decision_available(runtime, available)
    before = [runtime.scopes[site]['state_population_k'] for site in ('A', 'B')]
    execute_paid(runtime, country)
    assert country['political_power'] == 100 - PRICE() and country['camp_admin_country_last_released_k'] == 15
    assert sale.credits(runtime) == 1
    assert country['camp_admin_total_released_k'] == 15
    assert runtime.scopes['A']['camp_admin_total_released_k'] == 10
    assert runtime.scopes['B']['camp_admin_total_released_k'] == 5
    assert all(runtime.scopes[site]['camp_admin_detainees_k'] == 0 for site in ('A', 'B'))
    assert all('camp_admin_census_intake_closed' in runtime.scopes[site]['flags'] for site in ('A', 'B'))
    assert 'camp_gui_country_action_3_cooldown' in country['flags']
    assert 'camp_rework_soviet_service_release_policy_enacted' in country['flags']
    assert policy_description_key(runtime) == 'sov_release_prisoners_repeat_consequence'
    assert before == [runtime.scopes[site]['state_population_k'] for site in ('A', 'B')]
    assert country['camp_policy_reform'] == runtime.constants['camp_rework_country_value.reform_major']
    assert country['forced_labor_quota'] < 30 and country['famine_pressure'] < 20 and country['old_movement_grievance'] < 15
    results.append({'case': 'two_valid_sites', 'paid_pp': PRICE(), 'actual_release_people': 15000,
                    'population_unchanged': True})

    runtime, country, available = scenario(second_k=0)
    runtime.scopes['A']['state_population_k'] = runtime.constants['camp_admin_value.minimum_population_k']
    runtime.scopes['B']['state_population_k'] = runtime.constants['camp_admin_value.minimum_population_k']
    assert not decision_available(runtime, available)  # Fresh provenance also rejects the unobserved physical decline.
    execute_paid(runtime, country)
    assert country['political_power'] == 100 and country['camp_admin_country_last_released_k'] == 0 and sale.credits(runtime) == 0
    assert country['camp_admin_total_released_k'] == 0
    assert country['forced_labor_quota'] == 30 and country['camp_policy_reform'] == 0
    assert all('camp_admin_census_intake_closed' not in runtime.scopes[site]['flags'] for site in ('A', 'B'))
    assert 'camp_gui_country_action_3_cooldown' not in country['flags']
    assert 'camp_rework_soviet_service_release_policy_enacted' not in country['flags']
    results.append({'case': 'headroom_exhausted_at_execution', 'refund_pp': PRICE(),
                    'actual_release_people': 0, 'policy_relief': 0})

    runtime, country, available = scenario(second_k=0)
    runtime.scopes['A']['camp_admin_detainees_k'] = .001
    runtime.scopes['A']['arrays']['camp_admin_row_amounts_k'][0] = .001
    assert decision_available(runtime, available)
    before = runtime.scopes['A']['state_population_k']
    execute_paid(runtime, country)
    assert country['political_power'] == 100 - PRICE() and country['camp_admin_country_last_released_k'] == .001
    assert country['forced_labor_quota'] == 23 and country['famine_pressure'] == 8
    assert country['old_movement_grievance'] == 8 and country['camp_policy_reform'] == 6
    assert runtime.scopes['A']['state_population_k'] == before
    assert 'camp_admin_census_intake_closed' in runtime.scopes['A']['flags']
    assert 'camp_gui_country_action_3_cooldown' in country['flags']
    assert 'camp_rework_soviet_service_release_policy_enacted' in country['flags']
    results.append({'case': 'one_survivor_fixed_policy_sensitivity', 'paid_pp': PRICE(),
                    'actual_release_people': 1, 'quota_delta': -7, 'famine_delta': -12,
                    'grievance_delta': -7, 'reform_delta': 6,
                    'interpretation': 'Fixed national policy effect; no accepted minimum cohort.'})

    runtime, country, available = scenario(second_k=0)
    execute_paid(runtime, country)
    assert country['camp_admin_country_last_released_k'] == 10
    country['flags'].discard('camp_gui_country_action_3_cooldown')  # A later native re-enable is assumed.
    new_site = runtime.state('C', 'SOV', population=100, buildings=2)
    new_site['gulag_labor_camp_network'] = 2
    new_site['camp_admin_responsible_country'] = 'SOV'
    prime_existing_custody(runtime, 'C', .001)
    assert decision_available(runtime, available)
    execute_paid(runtime, country)
    assert country['political_power'] == 100 - 2 * PRICE() and country['camp_admin_country_last_released_k'] == .001
    assert sale.credits(runtime) == 2
    assert country['camp_policy_reform'] == 6 and country['forced_labor_quota'] == 23
    assert country['camp_admin_total_released_k'] == 10.001
    assert policy_description_key(runtime) == 'sov_release_prisoners_repeat_consequence'
    results.append({'case': 'later_new_site_repeat_sensitivity', 'orders': 2, 'paid_pp': 2 * PRICE(),
                    'second_release_people': 1, 'total_reform_delta': 6,
                    'second_policy_delta': 0,
                    'premise': 'A new eligible Gulag site and a later native decision re-enable are declared.'})
    return results


if __name__ == '__main__':
    cases = {}
    for ratio in sale.SALE_RATIOS:
        SALE_RATIO = ratio
        cases[f'payment_ratio_{ratio}'] = run_cases()
    result = {'status': 'passed', 'source_scenarios': cases, 'sale_ratios': list(sale.SALE_RATIOS),
              'limit': 'Parsed production effects and triggers with mocked native PP debit; no live decision click or physical engine receipt.'}
    Path(__file__).with_name('soviet_release_integrity_source_results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'scenarios': sum(len(group) for group in cases.values())}, indent=2))
