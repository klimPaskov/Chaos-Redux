"""Execute production institutional-loss helpers with mocked engine primitives."""
from pathlib import Path
from datetime import date
import json

from foundation_source_tests import ROOT, parse, prime_existing_custody
from major_countries_source_tests import CountryRuntime


def experiment_site(tag='GER', permission=3, support=1, budget=2, mandate=2):
    runtime = CountryRuntime()
    runtime.date = date(1943, 6, 1) if tag == 'GER' else date(1942, 1, 1)
    country = runtime.country(tag)
    state_id = '88' if tag == 'GER' else '328'
    if tag == 'JAP':
        subject = runtime.country('MAN')
        subject['overlord'] = 'JAP'
    site = runtime.state(state_id, tag, population=100, buildings=2)
    prime_existing_custody(runtime, state_id, 10)
    site.update(camp_admin_support_ratio=support, camp_admin_role=runtime.constants['camp_admin_role.custody'])
    country.update(camp_admin_budget=budget, camp_admin_mandate=mandate)
    if tag == 'GER':
        site['flags'].add('genocide_auschwitz_experiment_site')
        country['mengele_permission_level'] = permission
        country['flags'].add('test_mengele_active')
        runtime.triggers['germany_mengele_program_active'] = [('has_country_flag', '=', 'test_mengele_active')]
        runtime.triggers['germany_mengele_restricted_program_active'] = [('has_country_flag', '=', 'test_mengele_restricted')]
        for category, _, body in parse((ROOT / 'common/script_constants/germany_mengele_constants.txt').read_text(encoding='utf-8-sig')):
            if category == 'germany_mengele_permission':
                for key, _, value in body:
                    if key != 'schema':
                        try:
                            runtime.constants[f'{category}.{key}'] = float(value)
                        except (TypeError, ValueError):
                            pass
    else:
        site.update(owner='MAN', controller='MAN')
        site['flags'].update({'camp_admin_subject_authority', 'camp_rework_pingfang_anchor',
                              'camp_rework_pingfang_bureau_completed', 'camp_rework_experiment_site'})
        country['flags'].add('japan_ishii_program_active')
    return runtime, country, site, state_id


def close(actual, expected):
    assert abs(actual - expected) < 1e-7, (actual, expected)


def legacy_mengele_occupied_owner_case():
    """Run the production exact-loss adapter with GER root and POL ownership."""
    runtime = CountryRuntime()
    runtime.country('GER')
    runtime.country('POL')
    site = runtime.state('88', 'GER', population=100)
    site['owner'] = 'POL'
    site['controller'] = 'GER'
    source = parse((ROOT / 'common/scripted_effects/camp_repression_rework_effects.txt').read_text(encoding='utf-8-sig'))
    effect = next(body for name, _, body in source if name == 'camp_rework_register_exact_state_deaths')
    def mock_death_primitive(block):
        return [('test_capture_exact_death_receipt' if name == 'chaos_meter_register_deaths' else name,
                 op, mock_death_primitive(value) if isinstance(value, list) else value)
                for name, op, value in block]

    runtime.effects['camp_rework_register_exact_state_deaths'] = mock_death_primitive(effect)
    runtime.effects['test_capture_exact_death_receipt'] = []
    original_val, original_run = runtime.val, runtime.run
    runtime.val = lambda value, scope, prev=None: 'GER' if value == 'ROOT' else original_val(value, scope, prev)
    receipt = {}

    def run_with_receipt(name, scope, params=None, prev=None):
        if name == 'test_capture_exact_death_receipt':
            receipt['target'] = runtime.temp['chaos_deaths_target_country']
            receipt['people'] = runtime.temp['chaos_deaths_change']
            assert runtime.temp['chaos_deaths_apply_state_pop'] == 1
            runtime.scopes[scope]['state_population_k'] -= receipt['people'] / 1000
            runtime.debits += 1
            return
        return original_run(name, scope, params, prev)

    runtime.run = run_with_receipt
    runtime.temp['camp_exact_deaths'] = 100
    runtime.temp['camp_exact_deaths_reason'] = runtime.constants['chaos_meter_deaths_reason.camp_atrocity']
    runtime.run('camp_rework_register_exact_state_deaths', '88')
    assert receipt == {'target': 'GER', 'people': 100}
    assert runtime.debits == 1 and site['owner'] == 'POL' and site['controller'] == 'GER'
    close(site['state_population_k'], 99.9)
    return {'case': 'legacy_mengele_occupied_polish_owner', 'responsible_country': receipt['target'],
            'territorial_owner': site['owner'], 'measured_people': receipt['people'], 'physical_debits': runtime.debits}


def run_cases():
    results = []
    for permission, expected_people in [(1, 10), (2, 15), (3, 20), (4, 30)]:
        runtime, country, site, state_id = experiment_site(permission=permission)
        before = site['state_population_k']
        runtime.run('camp_admin_country_apply_institutional_site_mortality', state_id)
        actual = runtime.temp['camp_admin_death_actual_k']
        close(actual, expected_people / 1000)
        close(before - site['state_population_k'], actual)
        close(10 - site['camp_admin_detainees_k'], actual)
        close(10 - site['arrays']['camp_admin_row_amounts_k'][0], actual)
        close(site['camp_admin_total_institutional_deaths_k'], actual)
        close(country['camp_admin_total_institutional_deaths_k'], actual)
        close(runtime.logged, actual)
        assert runtime.debits == 1 and country.get('camp_admin_institution_progress', 0) == 0 and not runtime.awards
        results.append({'case': f'ger_permission_{permission}', 'measured_people': expected_people,
                        'physical_debits': runtime.debits, 'institutional_records_people': round(actual * 1000)})

    runtime, country, site, state_id = experiment_site(tag='JAP')
    runtime.run('camp_admin_country_apply_institutional_site_mortality', state_id)
    close(runtime.temp['camp_admin_death_actual_k'], .025)
    assert runtime.debits == 1 and country.get('camp_admin_institution_progress', 0) == 0 and not runtime.awards
    results.append({'case': 'jap_pingfang_subject_control', 'measured_people': 25,
                    'physical_debits': 1, 'institutional_records_people': 25})
    country['flags'].add('japan_prisoner_experiments_shutdown')
    runtime.run('camp_admin_country_apply_institutional_site_mortality', state_id)
    assert runtime.debits == 1
    results.append({'case': 'jap_shutdown_stops_institutional_loss', 'additional_people': 0})

    runtime, country, site, state_id = experiment_site(tag='JAP')
    runtime.scopes['MAN']['overlord'] = None
    runtime.run('camp_admin_country_apply_institutional_site_mortality', state_id)
    assert runtime.debits == 0 and runtime.logged == 0
    results.append({'case': 'jap_subject_authority_lost', 'additional_people': 0})

    runtime, country, site, state_id = experiment_site(tag='JAP')
    runtime.date = date(1938, 12, 31)
    runtime.run('camp_admin_country_apply_institutional_site_mortality', state_id)
    assert runtime.debits == 0 and runtime.logged == 0
    results.append({'case': 'jap_before_1939', 'additional_people': 0})

    for label, change in [
        ('support_below_minimum', lambda r, c, s: s.update(camp_admin_support_ratio=.74)),
        ('maintenance_only', lambda r, c, s: c.update(camp_admin_budget=1)),
        ('custody_mandate', lambda r, c, s: c.update(camp_admin_mandate=1)),
        ('capture', lambda r, c, s: (r.country('USA'), s.update(controller='USA'))),
        ('reform', lambda r, c, s: c['flags'].add('camp_admin_reforming')),
        ('bad_living_rows', lambda r, c, s: s['arrays']['camp_admin_row_amounts_k'].__setitem__(0, 9)),
        ('closed_site', lambda r, c, s: s['flags'].add('camp_admin_closed')),
    ]:
        runtime, country, site, state_id = experiment_site()
        change(runtime, country, site)
        before = site['state_population_k']
        runtime.run('camp_admin_country_apply_institutional_site_mortality', state_id)
        assert runtime.debits == 0 and runtime.logged == 0
        close(site['state_population_k'], before)
        close(site['camp_admin_total_institutional_deaths_k'], 0)
        results.append({'case': label, 'additional_people': 0})

    runtime, country, site, state_id = experiment_site(permission=3, support=.75)
    runtime.run('camp_admin_country_apply_institutional_site_mortality', state_id)
    close(runtime.temp['camp_admin_death_actual_k'], .015)
    results.append({'case': 'minimum_funded_support_scales_request', 'measured_people': 15})

    runtime, country, site, state_id = experiment_site(permission=3)
    country['flags'].add('camp_admin_done_ger_auschwitz')
    runtime.run('camp_admin_monthly_state', state_id)
    first = site['camp_admin_total_institutional_deaths_k']
    assert first > 0 and runtime.debits == 2
    runtime.run('camp_admin_monthly_state', state_id)
    close(site['camp_admin_total_institutional_deaths_k'], first)
    assert runtime.debits == 2
    runtime.date = date(1943, 7, 1)
    runtime.run('camp_admin_monthly_state', state_id)
    assert site['camp_admin_total_institutional_deaths_k'] > first and runtime.debits == 4
    assert country.get('camp_admin_institution_progress', 0) == 0
    results.append({'case': 'post_award_monthly_continuation_and_duplicate_guard',
                    'first_month_institutional_people': round(first * 1000),
                    'two_month_physical_debits': runtime.debits})

    runtime, country, site, state_id = experiment_site()
    runtime.global_flags.add('settings_chaos_deaths_disabled')
    runtime.run('camp_admin_country_apply_institutional_site_mortality', state_id)
    assert runtime.debits == 0 and runtime.logged == 0
    results.append({'case': 'deaths_disabled', 'additional_people': 0})

    runtime, country, site, state_id = experiment_site()
    site['state_population_k'] = runtime.constants['camp_admin_value.minimum_population_k']
    runtime.run('camp_admin_country_apply_institutional_site_mortality', state_id)
    assert runtime.debits == 0 and runtime.logged == 0
    close(site['state_population_k'], runtime.constants['camp_admin_value.minimum_population_k'])
    close(site['camp_admin_total_institutional_deaths_k'], 0)
    results.append({'case': 'population_floor', 'additional_people': 0})

    runtime, country, site, state_id = experiment_site()
    runtime.date = date(1943, 5, 29)
    runtime.run('camp_admin_country_apply_institutional_site_mortality', state_id)
    assert runtime.debits == 0
    results.append({'case': 'ger_before_1943_05_30', 'additional_people': 0})

    for tag, year in [('GER', 1944), ('JAP', 1942)]:
        runtime, country, site, state_id = experiment_site(tag=tag)
        if tag == 'GER':
            country['flags'].add('camp_admin_done_ger_auschwitz')
        for month in range(1, 13):
            runtime.date = date(year, month, 1)
            runtime.run('camp_admin_monthly_state', state_id)
        institutional = site['camp_admin_total_institutional_deaths_k']
        custody = site['camp_admin_total_custody_deaths_k']
        close(100 - site['state_population_k'], institutional + custody)
        close(10 - site['camp_admin_detainees_k'], institutional + custody)
        close(10 - site['arrays']['camp_admin_row_amounts_k'][0], institutional + custody)
        close(country['camp_admin_total_institutional_deaths_k'], institutional)
        assert runtime.debits == 24 and country.get('camp_admin_institution_progress', 0) == 0 and not runtime.awards
        results.append({'case': f'{tag.lower()}_twelve_month_supported_site',
                        'institutional_people': round(institutional * 1000),
                        'custody_people': round(custody * 1000),
                        'physical_debits': runtime.debits,
                        'surviving_custody_people': round(site['camp_admin_detainees_k'] * 1000)})
    results.append(legacy_mengele_occupied_owner_case())
    return results


if __name__ == '__main__':
    cases = run_cases()
    result = {'status': 'passed', 'source_scenarios': cases,
              'limit': 'Parsed production effects with mocked engine primitives; historical rate calibration, explicit legacy burst cohort binding, and native execution remain unresolved'}
    Path(__file__).with_name('institutional_mortality_source_results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'scenarios': len(cases)}, indent=2))
