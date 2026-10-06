"""Dated start of the German campaign for Western, Greek and Italian origins.

Evaluates the production camp_occ_origin_campaign_deferred trigger at each
documented start date, runs the production monthly occupation pass and the
manual-transfer source check with the joined harness of the Danish rescue
suite, and reruns the 13-state dated sensitivity with each origin's first
deportation month. Engine primitives are harness mocks and controllers are
declared; the monthly pass is modeled on the first of each month.
Not HOI4 execution. Run: python <this file>.
"""
from decimal import Decimal as D
from pathlib import Path
import datetime
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from danish_rescue_source_tests import RescueRuntime, months
from partner_deportation_source_tests import PartnerRuntime, transform as partner_transform
from test_historical_envelopes import vanilla_european_origin_inventory, staged_direct_control_rows, NINE_STAGED_CONTROL_WINDOWS
from test_occupation_accounting import constant

# First day on which the deferral no longer holds (USHMM chronology, agent decision 16).
START = {
    'DEN': datetime.date(1943, 10, 1),   # unchanged rule (agent decision 6)
    'FRA': datetime.date(1942, 3, 27),   # first train from Drancy/Compiegne to Auschwitz
    'HOL': datetime.date(1942, 7, 15),   # first train from Westerbork
    'BEL': datetime.date(1942, 8, 4),    # first train from Mechelen
    'NOR': datetime.date(1942, 10, 26),  # arrest of Jewish men by Norwegian police
    'GRE': datetime.date(1943, 3, 15),   # first train from Salonika, state 731
}
GREEK_OTHER_START = datetime.date(1944, 3, 24)
ITALIAN_START = datetime.date(1943, 10, 16)
UNDEFERRED = ('POL', 'SOV', 'LIT', 'LAT', 'CZE', 'YUG', 'HUN')
# The trigger before this change: only Denmark was deferred.
PRIOR_RULE = [('is_core_of', '=', 'DEN'), ('date', '<', '1943.10.1')]
# Baseline for incremental Greece and Italy sensitivity, including the prior
# single date applied to every Greek state.
PRE_GREECE_ITALY_RULE = [('OR', '=', [
    ('AND', '=', [('is_core_of', '=', 'DEN'), ('date', '<', '1943.10.1')]),
    ('AND', '=', [('is_core_of', '=', 'FRA'), ('date', '<', '1942.3.27')]),
    ('AND', '=', [('is_core_of', '=', 'HOL'), ('date', '<', '1942.7.15')]),
    ('AND', '=', [('is_core_of', '=', 'BEL'), ('date', '<', '1942.8.4')]),
    ('AND', '=', [('is_core_of', '=', 'NOR'), ('date', '<', '1942.10.26')]),
    ('AND', '=', [('is_core_of', '=', 'GRE'), ('date', '<', '1943.3.15')]),
])]

RESULTS = json.loads((HERE / 'historical_envelope_results.json').read_text(encoding='utf-8'))


class DatedRuntime(PartnerRuntime):
    """Bind the engine's current-state `state = ID` test to a harness flag."""
    def __init__(self):
        super().__init__()
        # This suite isolates origin-date behavior; extended partner responses
        # are exercised by their own source suite and are not loaded here.
        self.effects['camp_occ_try_extended_partner_orders'] = []
        # Provenance readiness is supplied as a fixture below; the boundary
        # being tested is campaign timing after a valid row exists.
        self.triggers['camp_origin_host_provenance_ready'] = []

    def run(self, name, scope, params=None, prev=None):
        if name == 'camp_occ_prove_active_row':
            owner = self.scopes[scope].get('camp_occ_responsible_country')
            arrays = self.scopes[owner]['arrays']
            index = int(self.temp.get('camp_occ_active_row_index', -1))
            row_id = self.temp.get('camp_occ_active_row_id', 0)
            aligned = (0 <= index < len(arrays.get('camp_occ_row_ids', []))
                       and arrays['camp_occ_row_ids'][index] == row_id
                       and arrays['camp_occ_row_statuses'][index] == self.constants['camp_occ_row_status.active']
                       and str(arrays['camp_occ_row_hosts'][index]) == str(scope))
            self.temp['camp_occ_active_row_valid'] = self.constants['camp_occ_value.transfer_valid'] if aligned else self.constants['camp_occ_value.transfer_invalid']
            self.temp['camp_occ_active_row_remaining_k'] = arrays['camp_occ_row_amounts_k'][index] if aligned else 0
            return
        return super().run(name, scope, params, prev)

    def cond(self, block, scope, previous=None):
        self.triggers.setdefault('always', [])
        def bind(items):
            bound = []
            for key, operator, value in items:
                if key == 'state':
                    marker = 'test_origin_state_' + str(value)
                    current = self.scopes.get(scope)
                    if current is None:
                        bound.append(('always', '=', 'no'))
                    else:
                        flags = current.setdefault('flags', set())
                        if str(current.get('state', scope)) == str(value):
                            flags.add(marker)
                        else:
                            flags.discard(marker)
                        bound.append(('has_state_flag', '=', marker))
                elif isinstance(value, list):
                    bound.append((key, operator, bind(value)))
                else:
                    bound.append((key, operator, value))
            return bound

        return super().cond(bind(partner_transform(block)), scope, previous)


def stored_windows(key):
    rows = RESULTS[key]['rows']
    windows = []
    for row in rows:
        first = tuple(int(x) for x in row['assumed_direct_control_first_month'].split('-'))
        last = tuple(int(x) for x in row['assumed_direct_control_last_month'].split('-'))
        windows.append((row['origin'].lower(), row['state_id'], first, last))
    return windows, rows


def origin_start(tag, state_id):
    if tag == 'GRE' and int(state_id) != 731:
        return GREEK_OTHER_START
    if tag == 'ITA':
        return ITALIAN_START
    return START[tag]


def first_pass_month(tag, state_id=None):
    start = START[tag] if state_id is None else origin_start(tag, state_id)
    return (start.year, start.month) if start.day == 1 else ((start.year + 1, 1) if start.month == 12 else (start.year, start.month + 1))


def adjusted(windows):
    out = []
    for origin, state_id, first, last in windows:
        tag = origin.upper()
        if tag in START and tag != 'DEN':
            first = max(first, first_pass_month(tag, state_id))
        elif tag in ('GRE', 'ITA'):
            first = max(first, first_pass_month(tag, state_id))
        out.append((origin, state_id, first, last))
    return out


def allocation(origin, state_id):
    inventory, _ = vanilla_european_origin_inventory()
    states = dict(inventory[origin])
    return states[state_id], int(D(states[state_id]) * constant(origin) * 1000 / D(sum(states.values())))


def world(tag, state_id, prior=False, deferred_rule=None):
    r = DatedRuntime()
    if prior:
        r.triggers['camp_occ_origin_campaign_deferred'] = list(PRIOR_RULE)
    if deferred_rule is not None:
        r.triggers['camp_occ_origin_campaign_deferred'] = deferred_rule
    r.date = datetime.date(1941, 7, 1)
    ger = r.country('GER')
    ger['flags'].add('origin_test_campaign_eligible')
    r.run('camp_occ_initialize_country', 'GER')
    r.scopes[tag] = {'id': tag, 'exists': True, 'flags': set(), 'arrays': {}, 'mods': set()}
    r.global_flags.add('test_exists_' + tag)
    population, allocated = allocation(tag.lower(), state_id)
    r.scopes[state_id] = {
        'id': state_id, 'state': state_id, 'flags': {'camp_occ_origin_assigned', 'test_continent_europe'},
        'arrays': {}, 'mods': set(), 'owner': tag, 'controller': 'GER', 'cores': {tag},
        'state_population_k': population / 1000, 'chaos_state_civilian_deaths_total': 0,
        'camp_occ_origin_country': tag, 'camp_occ_origin_ceiling_k': allocated / 1000,
        'camp_occ_origin_observed_population_k': population / 1000, 'camp_occ_origin_observed_state_deaths': 0,
    }
    ger['arrays'].setdefault('camp_occ_eligible_states', []).append(state_id)
    # Seed the production row once, independently of the monthly country
    # registration scan, so this suite isolates only campaign-date eligibility.
    r.temp.update(camp_occ_source_proven=1, camp_occ_source_requested_k=allocated / 1000,
                  camp_occ_source_membership_k=allocated / 1000, camp_occ_source_authority='GER',
                  camp_occ_source_profile=r.constants['camp_occ_profile.germany'])
    r.run('camp_occ_register_cohort', state_id)
    return r, allocated


def run_months(r, start, end):
    for year, month in months(start, end):
        r.date = datetime.date(year, month, 1)
        r.run('camp_occ_monthly_country', 'GER')


def deaths(r):
    rows = r.scopes['GER']['arrays']
    return round(sum(rows.get('camp_occ_row_deaths_k', [])) * 1000)


def origin_scope(r, tag, state_id=None):
    key = state_id if state_id is not None else 'origin_' + tag
    r.scopes[key] = {'id': key, 'state': key, 'flags': set(), 'arrays': {}, 'mods': set(), 'cores': {tag}}
    return key


def by_origin(rows):
    totals = {}
    for row in rows:
        entry = totals.setdefault(row['origin'], {'states': [], 'apportioned_source_people': 0, 'campaign_violence_people': 0, 'survivors_people': 0, 'campaign_months': 0})
        entry['states'].append(row['state_id'])
        entry['apportioned_source_people'] += row['apportioned_source_people']
        entry['campaign_violence_people'] += row['campaign_violence_people']
        entry['survivors_people'] += row['survivors_at_control_end_people']
        entry['campaign_months'] += row['accepted_campaign_receipts']
    return totals


def tests():
    cases = []
    results = {}

    # 1. The production trigger at each documented boundary, including both
    #    Greek regions and an Italian core state.
    r = DatedRuntime()
    boundaries = {}
    boundary_cases = {
        'DEN': ('DEN', 37, START['DEN']),
        'FRA': ('FRA', 16, START['FRA']),
        'HOL': ('HOL', 7, START['HOL']),
        'BEL': ('BEL', 6, START['BEL']),
        'NOR': ('NOR', 110, START['NOR']),
        'GRE_SALONIKA': ('GRE', 731, START['GRE']),
        'GRE_OTHER': ('GRE', 47, GREEK_OTHER_START),
        'ITA': ('ITA', 114, ITALIAN_START),
    }
    for label, (tag, state_id, start) in boundary_cases.items():
        scope = origin_scope(r, tag, state_id)
        r.date = start - datetime.timedelta(days=1)
        before = r.cond([('camp_occ_origin_campaign_deferred', '=', 'yes')], scope)
        r.date = start
        after = r.cond([('camp_occ_origin_campaign_deferred', '=', 'yes')], scope)
        r.date = datetime.date(1941, 7, 1)
        early = r.cond([('camp_occ_origin_campaign_deferred', '=', 'yes')], scope)
        assert before and early and not after, (tag, before, after, early)
        boundaries[label] = {'origin': tag, 'state_id': state_id, 'deferred_until': start.isoformat(),
                             'first_campaign_pass': '%d-%02d' % first_pass_month(tag, state_id)}
    for tag in UNDEFERRED:
        scope = origin_scope(r, tag)
        r.date = datetime.date(1941, 7, 1)
        assert not r.cond([('camp_occ_origin_campaign_deferred', '=', 'yes')], scope), tag
    results['deferral_boundaries'] = boundaries
    cases.append('the production deferral holds the day before and not on the documented start for Denmark, the Western origins, Salonika state 731, other Greek cores, and Italian cores; the non-dated Poland, Soviet, Baltic, Czech, Yugoslav and Hungarian origins remain unchanged')

    # 2. The 13-state dated sensitivity before and after the change.
    nine, nine_rows = stored_windows('staged_nine_state_direct_control_sensitivity')
    four, four_rows = stored_windows('staged_four_additional_state_direct_control_sensitivity')
    assert [w for w in nine] == [(o, s, f, l) for o, s, f, l in NINE_STAGED_CONTROL_WINDOWS]
    before_rows = staged_direct_control_rows(nine + four)
    stored = nine_rows + four_rows
    for row, old in zip(before_rows, stored):
        assert row['campaign_violence_people'] == old['campaign_violence_people'], (row['state_id'], row['campaign_violence_people'], old['campaign_violence_people'])
    after_rows = staged_direct_control_rows(adjusted(nine + four))
    before_origin = by_origin(before_rows)
    after_origin = by_origin(after_rows)
    comparison = {}
    for origin in before_origin:
        comparison[origin] = {
            'states': before_origin[origin]['states'],
            'apportioned_source_people': before_origin[origin]['apportioned_source_people'],
            'campaign_months_before': before_origin[origin]['campaign_months'],
            'campaign_months_after': after_origin[origin]['campaign_months'],
            'deaths_before': before_origin[origin]['campaign_violence_people'],
            'deaths_after': after_origin[origin]['campaign_violence_people'],
            'survivors_after': after_origin[origin]['survivors_people'],
        }
        changed = origin in ('FRA', 'HOL', 'BEL', 'NOR', 'GRE')
        assert (comparison[origin]['deaths_after'] < comparison[origin]['deaths_before']) == changed, origin
        assert after_origin[origin]['apportioned_source_people'] == after_origin[origin]['campaign_violence_people'] + after_origin[origin]['survivors_people']
    total_before = sum(row['campaign_violence_people'] for row in before_rows)
    total_after = sum(row['campaign_violence_people'] for row in after_rows)
    assert total_before == RESULTS['staged_thirteen_state_disjoint_source_subtotal']['total_campaign_violence_people']
    results['thirteen_state_sensitivity_by_origin'] = comparison
    results['thirteen_state_totals'] = {
        'deaths_before': total_before, 'deaths_after': total_after,
        'campaign_months_before': sum(row['accepted_campaign_receipts'] for row in before_rows),
        'campaign_months_after': sum(row['accepted_campaign_receipts'] for row in after_rows),
        'apportioned_source_people': sum(row['apportioned_source_people'] for row in after_rows),
    }
    cases.append('13-state dated sensitivity: modeled campaign deaths fall from %d to %d; only the FRA, HOL, BEL, NOR and GRE rows change, and every row still conserves its people' % (total_before, total_after))

    # The existing 13-state set has only Salonika state 731. Add one other
    # Greek core and one Italian core for the newly dated zones, comparing the
    # previous policy with the current dates over the same declared window.
    representative_windows = [
        ('gre', 47, (first_pass_month('GRE', 731)[0], first_pass_month('GRE', 731)[1]), (1945, 4)),
        ('ita', 114, (1941, 7), (1945, 4)),
    ]
    representative_before = staged_direct_control_rows(representative_windows)
    representative_after = staged_direct_control_rows(adjusted(representative_windows))
    representative_sensitivity = {}
    for old, new in zip(representative_before, representative_after):
        assert old['state_id'] == new['state_id']
        assert new['campaign_violence_people'] < old['campaign_violence_people']
        assert new['apportioned_source_people'] == new['campaign_violence_people'] + new['survivors_at_control_end_people']
        representative_sensitivity[new['origin']] = {
            'state_id': new['state_id'],
            'campaign_months_before': old['accepted_campaign_receipts'],
            'campaign_months_after': new['accepted_campaign_receipts'],
            'deaths_before': old['campaign_violence_people'],
            'deaths_after': new['campaign_violence_people'],
            'source_people': new['apportioned_source_people'],
        }
    results['incremental_greek_other_and_italian_sensitivity'] = representative_sensitivity
    cases.append('representative Thessaly state 47 and Italian Sardinia state 114 sensitivity reruns the prior and new dated windows with conserved source people')

    # 3. The production monthly pass matches the rerun for each changed origin, before and after.
    production = {}
    for origin, state_id, first, last in nine + four:
        tag = origin.upper()
        if tag not in ('FRA', 'HOL', 'BEL', 'NOR', 'GRE'):
            continue
        old_world, allocated = world(tag, state_id, prior=True)
        run_months(old_world, (1941, 7), last)
        new_world, _ = world(tag, state_id)
        start = first_pass_month(tag, state_id)
        previous = (start[0], start[1] - 1) if start[1] > 1 else (start[0] - 1, 12)
        run_months(new_world, (1941, 7), previous)
        assert deaths(new_world) == 0, (tag, deaths(new_world))
        run_months(new_world, start, last)
        old_model = next(row for row in before_rows if row['state_id'] == state_id)['campaign_violence_people']
        new_model = next(row for row in after_rows if row['state_id'] == state_id)['campaign_violence_people']
        receipts_old = next(row for row in before_rows if row['state_id'] == state_id)['accepted_campaign_receipts']
        receipts_new = next(row for row in after_rows if row['state_id'] == state_id)['accepted_campaign_receipts']
        assert abs(deaths(old_world) - old_model) <= receipts_old, (tag, deaths(old_world), old_model)
        assert abs(deaths(new_world) - new_model) <= receipts_new, (tag, deaths(new_world), new_model)
        production[tag] = {'state_id': state_id, 'allocated_people': allocated,
                           'production_deaths_before': deaths(old_world), 'production_deaths_after': deaths(new_world),
                           'model_deaths_before': old_model, 'model_deaths_after': new_model}
    results['production_monthly_pass'] = production
    cases.append('the production monthly pass records no campaign death for a FRA, HOL, BEL, NOR or GRE origin row before its first deportation month and then matches the rerun sensitivity within one person per campaign month, before and after the change')

    # Run the production monthly pass for an additional Greek zone and Italy.
    # The baseline preserves the old shared Greek date and has no Italian date.
    incremental_production = {}
    for tag, state_id, last in (('GRE', 47, (1945, 4)), ('ITA', 114, (1945, 4))):
        old_world, allocated = world(tag, state_id, deferred_rule=PRE_GREECE_ITALY_RULE)
        run_months(old_world, (1941, 7), last)
        new_world, _ = world(tag, state_id)
        start = first_pass_month(tag, state_id)
        previous = (start[0], start[1] - 1) if start[1] > 1 else (start[0] - 1, 12)
        run_months(new_world, (1941, 7), previous)
        assert deaths(new_world) == 0, (tag, state_id, deaths(new_world))
        run_months(new_world, start, last)
        old_model = next(row for row in representative_before if row['state_id'] == state_id)['campaign_violence_people']
        new_model = next(row for row in representative_after if row['state_id'] == state_id)['campaign_violence_people']
        receipts_old = next(row for row in representative_before if row['state_id'] == state_id)['accepted_campaign_receipts']
        receipts_new = next(row for row in representative_after if row['state_id'] == state_id)['accepted_campaign_receipts']
        assert abs(deaths(old_world) - old_model) <= receipts_old, (tag, state_id, deaths(old_world), old_model)
        assert abs(deaths(new_world) - new_model) <= receipts_new, (tag, state_id, deaths(new_world), new_model)
        incremental_production[tag + '_' + str(state_id)] = {
            'allocated_people': allocated,
            'production_deaths_before': deaths(old_world), 'production_deaths_after': deaths(new_world),
            'model_deaths_before': old_model, 'model_deaths_after': new_model,
        }
    results['incremental_production_monthly_pass'] = incremental_production
    cases.append('the production monthly pass records no Greek-other or Italian campaign death before its new first month, then matches each representative sensitivity within one person per campaign month')

    # 4. The manual Auschwitz order reads the same dates.
    manual = {}
    for tag, state_id in (('FRA', 16), ('HOL', 7), ('BEL', 6), ('NOR', 110), ('GRE', 731), ('GRE', 47), ('ITA', 114)):
        m, _ = world(tag, state_id)
        start = first_pass_month(tag, state_id)
        previous = (start[0], start[1] - 1) if start[1] > 1 else (start[0] - 1, 12)
        run_months(m, (1941, 7), previous)
        m.scopes[state_id]['camp_occ_cohort_origin_state'] = state_id
        origin_date = origin_start(tag, state_id)
        m.date = origin_date - datetime.timedelta(days=1)
        early = m.cond([('camp_occ_manual_transfer_source_ready', '=', 'yes')], state_id)
        deferral = m.triggers['camp_occ_origin_campaign_deferred']
        m.triggers['camp_occ_origin_campaign_deferred'] = list(PRIOR_RULE)
        early_prior = m.cond([('camp_occ_manual_transfer_source_ready', '=', 'yes')], state_id)
        m.triggers['camp_occ_origin_campaign_deferred'] = deferral
        m.date = origin_date
        late = m.cond([('camp_occ_manual_transfer_source_ready', '=', 'yes')], state_id)
        assert not early and late and early_prior, (tag, early, late, early_prior)
        manual[tag + '_' + str(state_id)] = {'source_ready_day_before': early, 'source_ready_day_before_under_prior_rule': early_prior, 'source_ready_on_start': late}
    results['manual_transfer_source'] = manual
    cases.append('the manual Auschwitz order skips French, Dutch, Belgian, Norwegian, Salonika, other Greek, and Italian source cohorts before their own start dates and permits them on those dates')

    # 5. The generic campaign rate is unchanged.
    assert constant('german_campaign_monthly_fraction') == D('0.025')
    cases.append('the generic German campaign fraction stays 0.025 per month')
    return cases, results


if __name__ == '__main__':
    cases, results = tests()
    payload = {'status': 'passed', 'count': len(cases), 'cases': cases, 'scenarios': results,
               'limits': 'Parsed production triggers/effects with harness primitives, declared GER controllers over staged windows, and monthly passes on the first of each month. The harness seeds an aligned cohort row and mocks its provenance/row proof to isolate date eligibility; extended partner orders use their separate suite. Modeled campaign cause only; no deportation, arrival, custody or outside losses; no HOI4 execution.'}
    (HERE / 'deportation_start_dates_source_results.json').write_text(json.dumps(payload, indent=2) + '\n')
    print(json.dumps(payload, indent=2))
