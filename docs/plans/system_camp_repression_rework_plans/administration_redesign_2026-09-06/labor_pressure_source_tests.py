"""Forced-labor trade-off through the production foundation helpers.

Executes camp_admin_refresh_state_economy and camp_admin_monthly_state with harness
primitives: the radical mandate raises output and labor deaths, hunger in the host state
lowers the assigned workforce, and a suspended or custody-only site adds no labor burden.
Not HOI4 execution. Run from the mod root: python <this file>.
"""
from pathlib import Path
import json
import re

from foundation_source_tests import ROOT, Runtime, parse, prime_existing_custody


def runtime(mandate, famine_stage=None, priority=1):
    r = Runtime()
    # The famine stage constants belong to the Famine package; the harness reads them from its file.
    for category, _, body in parse((ROOT / 'common/script_constants/famine_core_constants.txt').read_text(encoding='utf-8-sig')):
        if category == 'famine_food_stage':
            for key, _, value in body:
                if key != 'schema':
                    r.constants['famine_food_stage.' + key] = float(value)
    for category, _, body in parse((ROOT / 'common/script_constants/camp_administration_constants.txt').read_text(encoding='utf-8-sig')):
        if category == 'camp_admin_labor':
            for key, _, value in body:
                if key != 'schema':
                    r.constants['camp_admin_labor.' + key] = float(value)
    country = r.country()
    country.update(camp_admin_mandate=mandate, camp_admin_priority=priority)
    site = r.state()
    site['flags'].discard('camp_admin_site_suspended')
    prime_existing_custody(r, 'S1', 100)
    site.update(camp_admin_support_ratio=1, camp_admin_role=r.constants['camp_admin_role.labor'])
    if famine_stage is not None:
        site['famine_food_stage'] = famine_stage
    return r, country, site


def refresh(r):
    r.run('camp_admin_refresh_state_economy', 'S1')


def tests():
    cases = []
    results = {}

    base_r, _, base = runtime(mandate=2)
    refresh(base_r)
    workforce = base['camp_admin_workforce_k']
    industry = base['camp_admin_industry_k']
    equivalent = base['camp_admin_industrial_equivalent']
    assert workforce > 0 and equivalent > 0
    results['coercive'] = {'workforce_k': workforce, 'industry_k': industry, 'equivalent': equivalent}

    radical_r, _, radical = runtime(mandate=3)
    refresh(radical_r)
    output_factor = radical_r.constants['camp_admin_labor.radical_output']
    assert radical['camp_admin_workforce_k'] == workforce
    assert abs(radical['camp_admin_industrial_equivalent'] - equivalent * output_factor) < 1e-9, (radical['camp_admin_industrial_equivalent'], equivalent)
    results['radical'] = {'equivalent': radical['camp_admin_industrial_equivalent'], 'output_factor': output_factor}
    cases.append('a radical mandate multiplies a labor site\'s industrial output by camp_admin_labor.radical_output without changing who is assigned')

    # Monthly labor deaths scale with the mandate's mortality factor; custody deaths are unchanged.
    def monthly_labor_deaths(mandate):
        r, c, s = runtime(mandate=mandate)
        r.date = r.date.replace(year=1941, month=3, day=1)
        r.run('camp_admin_monthly_state', 'S1')
        return s['camp_admin_total_labor_deaths_k'], s['camp_admin_total_custody_deaths_k']
    coercive_labor, coercive_custody = monthly_labor_deaths(2)
    radical_labor, radical_custody = monthly_labor_deaths(3)
    factor = base_r.constants['camp_admin_labor.radical_mortality']
    assert coercive_labor > 0
    assert abs(radical_labor - coercive_labor * factor) < 0.002, (radical_labor, coercive_labor, factor)
    assert abs(radical_custody - coercive_custody) < 1e-9
    results['monthly_deaths'] = {'coercive_labor_k': coercive_labor, 'radical_labor_k': radical_labor, 'custody_k': coercive_custody}
    cases.append('radical labor deaths equal the coercive deaths times camp_admin_labor.radical_mortality (within whole-person rounding); custody deaths are the same under both mandates')

    # Hunger lowers the workforce stage by stage and never raises deaths through this path.
    stages = base_r.constants
    expected = {}
    for stage, key in ((2, 'acute_shortage_workforce'), (3, 'famine_workforce'), (4, 'catastrophic_famine_workforce')):
        r, _, s = runtime(mandate=2, famine_stage=stage)
        refresh(r)
        factor = r.constants['camp_admin_labor.' + key]
        assert abs(s['camp_admin_workforce_k'] - workforce * factor) < 1e-9, (stage, s['camp_admin_workforce_k'], workforce * factor)
        expected[stage] = s['camp_admin_workforce_k']
    r, _, s = runtime(mandate=2, famine_stage=1)
    refresh(r)
    assert s['camp_admin_workforce_k'] == workforce
    assert expected[2] > expected[3] > expected[4] > 0
    results['famine_workforce_k'] = expected
    cases.append('supply strain leaves the workforce intact; acute shortage, famine and catastrophic famine scale it by their constants')

    # Suspended and custody-only sites add no labor burden to the legacy profile index.
    r, _, s = runtime(mandate=2)
    refresh(r)
    s['camp_state_labor_output'] = 5
    r.run('camp_admin_scale_profile_labor_output', 'S1')
    assert s['camp_state_labor_output'] == 5
    s['flags'].add('camp_admin_site_suspended')
    refresh(r)
    s['camp_state_labor_output'] = 5
    r.run('camp_admin_scale_profile_labor_output', 'S1')
    assert s['camp_state_labor_output'] == 0
    r, _, s = runtime(mandate=1)
    refresh(r)
    s['camp_state_labor_output'] = 5
    r.run('camp_admin_scale_profile_labor_output', 'S1')
    assert s['camp_state_labor_output'] == 0
    cases.append('the legacy labor burden index follows assigned labor: unchanged for a working site, zero when suspended or under a custody mandate')
    return cases, results


if __name__ == '__main__':
    cases, results = tests()
    payload = {'status': 'passed', 'count': len(cases), 'cases': cases, 'scenarios': results,
               'limits': 'Parsed production helpers with harness primitives; no HOI4 execution and no live Famine registry.'}
    (Path(__file__).resolve().parent / 'labor_pressure_source_results.json').write_text(json.dumps(payload, indent=2) + '\n')
    print(json.dumps(payload, indent=2))
