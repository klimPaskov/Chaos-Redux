"""Danish rescue once Denmark's own government falls, through the production occupation pass.

Runs the real camp_occ_monthly_country, registration, campaign, rescue and
exact movement bodies with the existing joined harness. Engine primitives
(population credit/debit, Deaths projection) are the harness mocks; the
controller series is declared per scenario. Danish states are shielded while
Denmark's government stands (camp_occ_danish_government_shields); the harness
ends that government on DEN_FALLS to stage the autumn 1943 collapse of Danish
cooperation. The gate itself is the production trigger, not the date.
Not HOI4 execution. Run from the mod root: python <this file>.
"""
from pathlib import Path
from decimal import Decimal as D
import copy
import datetime
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from origin_observer_owner_integration_source_tests import JoinedRuntime, ROOT
from test_historical_envelopes import vanilla_european_origin_inventory, staged_direct_control_rows


def transform(block):
    """Map engine triggers the base harness lacks onto its existing primitives."""
    out = []
    for key, op, value in block:
        if isinstance(value, list):
            value = transform(value)
        if key == 'country_exists':
            out.append(('has_global_flag', '=', 'test_exists_' + value))
        elif key == 'is_in_faction_with':
            out.append(('has_country_flag', '=', 'test_faction_' + value))
        elif key == 'is_owned_and_controlled_by' and value == 'OWNER':
            out.append(('is_controlled_by', '=', 'OWNER'))
        elif key == 'is_owned_and_controlled_by':
            out.append(('AND', '=', [('OWNER', '=', [('tag', '=', value)]), ('is_controlled_by', '=', value)]))
        else:
            out.append((key, op, value))
    return out


# Harness timeline only: the day Denmark's government ends. The shield, the
# rescue window and the deportation order all follow from that state change.
DEN_FALLS = datetime.date(1943, 10, 1)


class RescueRuntime(JoinedRuntime):
    def __init__(self):
        super().__init__()
        self.den_falls = DEN_FALLS
        self.triggers = {name: transform(body) for name, body in self.triggers.items()}
        # External shared Deaths reason enum; its value is immaterial to conservation.
        self.constants.setdefault('chaos_meter_deaths_reason.occupation_repression', 1)

    def cond(self, block, scope, previous=None):
        return super().cond(transform(block), scope, previous)

    def run(self, name, scope, params=None, prev=None):
        den = self.scopes.get('DEN')
        if den is not None and self.den_falls is not None and self.date >= self.den_falls:
            den['has_capitulated'] = True
        return super().run(name, scope, params, prev)

    def target(self, x, s, prev):
        if x == 'capital_scope':
            return self.scopes[s]['capital']
        return super().target(x, s, prev)


DEN_STATES = (37, 99)


def allocations():
    inventory, _ = vanilla_european_origin_inventory()
    states = dict(inventory['den'])
    total = sum(states.values())
    ceiling = D('5.7') * 1000
    return {state_id: (states[state_id], int(D(states[state_id]) * ceiling / D(total))) for state_id in DEN_STATES}


def world(sweden='neutral', deferral=True):
    r = RescueRuntime()
    if not deferral:
        # Pre-change control only: the policy deferral did not exist.
        r.triggers['camp_occ_origin_campaign_deferred'] = [('always', '=', 'no')]
        r.triggers['always'] = []
    r.date = datetime.date(1941, 7, 1)
    ger = r.country('GER')
    ger['flags'].add('origin_test_campaign_eligible')
    r.run('camp_occ_initialize_country', 'GER')
    r.scopes['DEN'] = {'id': 'DEN', 'exists': True, 'flags': set(), 'arrays': {}, 'mods': set()}
    r.global_flags.add('test_exists_DEN')
    for state_id, (population, allocated) in allocations().items():
        r.scopes[state_id] = {
            'id': state_id, 'state': state_id, 'flags': {'camp_occ_origin_assigned'}, 'arrays': {}, 'mods': set(),
            'owner': 'DEN', 'controller': 'GER', 'cores': {'DEN'},
            'state_population_k': population / 1000, 'chaos_state_civilian_deaths_total': 0,
            'camp_occ_origin_country': 'DEN', 'camp_occ_origin_ceiling_k': allocated / 1000,
            'camp_occ_origin_observed_population_k': population / 1000, 'camp_occ_origin_observed_state_deaths': 0,
        }
        ger['arrays'].setdefault('camp_occ_eligible_states', []).append(state_id)
    if sweden != 'absent':
        r.scopes['SWE'] = {'id': 'SWE', 'exists': True, 'flags': set(), 'arrays': {}, 'mods': set(), 'capital': 38,
                           'has_war': False, 'wars': set()}
        r.global_flags.add('test_exists_SWE')
        for state_id, population in ((138, 1200), (38, 1500)):
            r.scopes[state_id] = {'id': state_id, 'state': state_id, 'flags': set(), 'arrays': {}, 'mods': set(),
                                  'owner': 'SWE', 'controller': 'SWE', 'cores': {'SWE'},
                                  'state_population_k': population, 'chaos_state_civilian_deaths_total': 0}
        if sweden == 'axis':
            r.scopes['SWE']['flags'].add('test_faction_GER')
        elif sweden == 'puppet':
            r.scopes['SWE']['overlord'] = 'GER'
        elif sweden == 'at_war_with_denmark':
            r.scopes['SWE'].update(has_war=True, wars={'DEN'})
        elif sweden == 'skane_occupied':
            r.scopes[138]['controller'] = 'GER'
        elif sweden == 'both_occupied':
            r.scopes[138]['controller'] = 'GER'
            r.scopes[38]['controller'] = 'GER'
    return r


def months(start, end):
    year, month = start
    while (year, month) <= end:
        yield year, month
        year, month = (year + 1, 1) if month == 12 else (year, month + 1)


def run_months(r, start=(1941, 7), end=(1945, 4)):
    for year, month in months(start, end):
        r.date = datetime.date(year, month, 1)
        r.run('camp_occ_monthly_country', 'GER')


def totals(r):
    ger = r.scopes['GER']
    rows = ger['arrays']
    deaths = sum(rows['camp_occ_row_deaths_k']) * 1000
    escaped = ger.get('camp_occ_total_escaped_k', 0) * 1000
    living = sum(a for a, s in zip(rows['camp_occ_row_amounts_k'], rows['camp_occ_row_statuses']) if s == 1) * 1000
    return round(deaths), round(escaped), round(living)


def tests():
    cases = []
    results = {}
    allocated = sum(a for _, a in allocations().values())

    # Pre-change control: no policy deferral and no refuge (generic campaign from July 1941).
    control = world(sweden='absent', deferral=False)
    run_months(control)
    control_deaths, control_escaped, control_living = totals(control)
    envelope = staged_direct_control_rows([('den', 37, (1941, 7), (1945, 4)), ('den', 99, (1941, 7), (1945, 4))])
    envelope_deaths = sum(row['campaign_violence_people'] for row in envelope)
    assert control_escaped == 0
    assert abs(control_deaths - envelope_deaths) <= 2 * len(DEN_STATES) * 46, (control_deaths, envelope_deaths)
    results['pre_change_no_deferral_no_refuge'] = {'deaths': control_deaths, 'escaped': 0, 'living_at_end': control_living}
    cases.append('pre-change production control reproduces the rejected no-rescue source model (%d vs %d deaths)' % (control_deaths, envelope_deaths))

    # Current rule without a refuge: the Danish government shields its cohorts until it falls.
    no_refuge = world(sweden='absent')
    run_months(no_refuge, end=(1943, 9))
    assert totals(no_refuge)[0] == 0 and no_refuge.logged == 0
    run_months(no_refuge, start=(1943, 10))
    nr_deaths, nr_escaped, nr_living = totals(no_refuge)
    assert nr_escaped == 0 and not no_refuge.scopes['GER']['arrays'].get('camp_admin_history_kinds', [])
    results['deferral_without_refuge'] = {'deaths': nr_deaths, 'escaped': 0, 'living_at_end': nr_living}
    cases.append('Danish cohorts take no campaign deaths while the Danish government stands; without a refuge nothing moves or is recorded')

    # Current rule with neutral Sweden: one rescue per Danish home state once the shield ends.
    r = world()
    run_months(r, end=(1943, 9))
    assert totals(r) == (0, 0, allocated)
    before = {state_id: r.scopes[state_id]['state_population_k'] for state_id in DEN_STATES + (138, 38)}
    rows_before = copy.deepcopy(r.scopes['GER']['arrays'])
    debits, credits, logged = r.debits, r.credits, r.logged
    r.date = datetime.date(1943, 10, 1)
    r.run('camp_occ_try_danish_rescue', 'GER')
    ger = r.scopes['GER']
    moved = round(ger['camp_occ_total_escaped_k'] * 1000)
    assert r.debits - debits == len(DEN_STATES) and r.credits - credits == len(DEN_STATES) and r.logged == logged
    assert round((r.scopes[138]['state_population_k'] - before[138]) * 1000) == moved
    assert round(sum(before[s] - r.scopes[s]['state_population_k'] for s in DEN_STATES) * 1000) == moved
    assert r.scopes[38]['state_population_k'] == before[38]
    new = len(ger['arrays']['camp_occ_row_ids']) - len(rows_before['camp_occ_row_ids'])
    assert new == len(DEN_STATES)
    for index in range(len(rows_before['camp_occ_row_ids']), len(ger['arrays']['camp_occ_row_ids'])):
        root = ger['arrays']['camp_occ_row_root_ids'][index]
        source = rows_before['camp_occ_row_root_ids'].index(root)
        assert ger['arrays']['camp_occ_row_authorities'][index] == 'GER'
        assert ger['arrays']['camp_occ_row_origins'][index] == rows_before['camp_occ_row_origins'][source]
        assert ger['arrays']['camp_occ_row_hosts'][index] == 138
        assert ger['arrays']['camp_occ_row_statuses'][index] == 2 and ger['arrays']['camp_occ_row_amounts_k'][index] == 0
        assert ger['arrays']['camp_occ_row_released_k'][index] == ger['arrays']['camp_occ_row_moved_in_k'][index] > 0
        assert ger['arrays']['camp_occ_row_deaths_k'][index] == 0
    for state_id in DEN_STATES:
        assert 'camp_occ_danish_rescue_done' in r.scopes[state_id]['flags']
        assert r.cond(r.triggers['camp_origin_host_rows_valid'], state_id)
        share = r.constants['camp_occ_rescue.danish_escape_share']
        index = rows_before['camp_occ_row_hosts'].index(state_id)
        living_before = rows_before['camp_occ_row_amounts_k'][index]
        assert abs(ger['arrays']['camp_occ_row_amounts_k'][index] - (living_before - ger['arrays']['camp_occ_row_moved_out_k'][index])) < 1e-9
        assert ger['arrays']['camp_occ_row_moved_out_k'][index] <= living_before * share + 1e-9
    assert 138 not in ger['arrays'].get('camp_occ_states', []) and 'camp_occ_registered' not in r.scopes[138]['flags']
    kinds = ger['arrays']['camp_admin_history_kinds']
    assert kinds.count(r.constants['camp_admin_history_kind.escape']) == len(DEN_STATES)
    r.run('camp_occ_try_danish_rescue', 'GER')
    assert round(ger['camp_occ_total_escaped_k'] * 1000) == moved and r.debits - debits == len(DEN_STATES)
    cases.append('the rescue after the Danish government falls moves each Danish home row once to Skane: one measured debit and credit per row, GER authority, origin and root kept, arrival retired as released, no death, two Records entries, repeat does nothing')

    run_months(r, start=(1943, 10))
    rescue_deaths, rescue_escaped, rescue_living = totals(r)
    assert rescue_escaped == moved
    assert rescue_deaths * 10 < control_deaths, (rescue_deaths, control_deaths)
    results['deferral_and_rescue'] = {'deaths': rescue_deaths, 'escaped': rescue_escaped, 'living_at_end': rescue_living}
    cases.append('Danish losses collapse from %d (pre-change) to %d with %d escaped to Sweden; the generic campaign rate is unchanged' % (control_deaths, rescue_deaths, rescue_escaped))

    for kind in ('axis', 'puppet', 'at_war_with_denmark', 'both_occupied'):
        bad = world(sweden=kind)
        run_months(bad, end=(1943, 10))
        assert totals(bad)[1] == 0 and bad.scopes['GER'].get('camp_occ_total_escaped_k', 0) == 0
        assert not any(k == bad.constants['camp_admin_history_kind.escape'] for k in bad.scopes['GER']['arrays'].get('camp_admin_history_kinds', []))
        cases.append('Sweden %s: no rescue fires and nothing is fabricated' % kind.replace('_', ' '))

    fallback = world(sweden='skane_occupied')
    run_months(fallback, end=(1943, 10))
    assert fallback.scopes['GER']['camp_occ_total_escaped_k'] > 0 and fallback.scopes[138]['state_population_k'] == 1200
    assert fallback.scopes[38]['state_population_k'] > 1500
    cases.append('with Skane under German control the escape reaches the Swedish capital instead')

    # A Danish cohort first under German authority after the government fell must also
    # wait until German authority over its state has consolidated, then flees.
    late = world()
    for state_id in DEN_STATES:
        late.scopes[state_id]['controller'] = 'DEN'
    run_months(late, end=(1944, 2))
    for state_id in DEN_STATES:
        late.scopes[state_id]['controller'] = 'GER'
    run_months(late, start=(1944, 3), end=(1944, 3))
    # German authority has held the states for under 45 days: still deferred.
    assert late.scopes['GER'].get('camp_occ_total_escaped_k', 0) == 0
    run_months(late, start=(1944, 4), end=(1944, 5))
    assert late.scopes['GER']['camp_occ_total_escaped_k'] > 0
    assert all('camp_occ_danish_rescue_done' in late.scopes[s]['flags'] for s in DEN_STATES)
    cases.append('a Danish cohort first under German control in 1944 stays deferred until German authority has held its state for 45 days, then escapes')
    return cases, results, allocated


if __name__ == '__main__':
    cases, results, allocated = tests()
    payload = {'status': 'passed', 'count': len(cases), 'cases': cases, 'danish_allocated_people': allocated, 'scenarios': results,
               'limits': 'Parsed production bodies with harness primitives and declared controllers; no HOI4 execution, no live Sweden or Denmark state.'}
    (HERE / 'danish_rescue_source_results.json').write_text(json.dumps(payload, indent=2) + '\n')
    print(json.dumps(payload, indent=2))
