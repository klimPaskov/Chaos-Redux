"""Campaign-age start of the German campaign for Western, Greek and Italian origins.

Evaluates the production camp_occ_origin_campaign_deferred trigger at the
boundaries of the campaign age and the German-authority age, runs the production monthly occupation pass and the
manual-transfer source check with the joined harness of the Danish rescue
suite, and reruns the 13-state sensitivity with each origin's first
deportation month under the campaign-age rule. Engine primitives are harness mocks and controllers are
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

# Harness staging, not gates: the day Germany's campaign opens and the day German
# authority over each origin state begins. The production trigger decides deferral
# from the two ages (camp_occ_timing.foreign_origin_campaign_days and
# foreign_origin_held_days) and, for Denmark, from the standing Danish government.
CAMPAIGN_OPENED = datetime.date(1941, 6, 22)
FOREIGN_ORIGIN_CAMPAIGN_DAYS = int(constant('foreign_origin_campaign_days'))
FOREIGN_ORIGIN_HELD_DAYS = int(constant('foreign_origin_held_days'))
HELD = {
    'DEN': datetime.date(1940, 4, 9),
    'FRA': datetime.date(1940, 6, 25),
    'HOL': datetime.date(1940, 5, 15),
    'BEL': datetime.date(1940, 5, 28),
    'NOR': datetime.date(1940, 6, 10),
    'GRE_SALONIKA': datetime.date(1941, 4, 9),
    'GRE_OTHER': datetime.date(1941, 4, 30),
    'ITA': datetime.date(1943, 9, 9),
}
HELD_TAGS = ('DEN', 'FRA', 'HOL', 'BEL', 'NOR', 'GRE', 'ITA')
UNDEFERRED = ('POL', 'SOV', 'LIT', 'LAT', 'CZE', 'YUG', 'HUN')
# Baseline for the sensitivities: the campaign without any pacing.
UNPACED_RULE = [('always', '=', 'no')]

RESULTS = json.loads((HERE / 'historical_envelope_results.json').read_text(encoding='utf-8'))


class DatedRuntime(PartnerRuntime):
    """Bind the engine's current-state `state = ID` test to a harness flag."""
    def __init__(self):
        super().__init__()
        # This suite isolates origin-date behavior; extended partner responses
        # are exercised by their own source suite and are not loaded here.
        self.effects['camp_occ_try_extended_partner_orders'] = []
        # Denmark's government is staged explicitly below, not by the rescue suite's timeline.
        self.den_falls = None
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


def held_since(tag, state_id):
    """Harness staging: the day German authority over the origin state began."""
    if tag == 'GRE':
        return HELD['GRE_SALONIKA'] if int(state_id) == 731 else HELD['GRE_OTHER']
    return HELD[tag]


def deferral_end(held):
    """First day a paced origin is no longer deferred: both ages strictly exceed their thresholds."""
    return max(CAMPAIGN_OPENED + datetime.timedelta(days=FOREIGN_ORIGIN_CAMPAIGN_DAYS + 1),
               held + datetime.timedelta(days=FOREIGN_ORIGIN_HELD_DAYS + 1))


def first_pass_of(day):
    """The monthly pass (first of the month) on or after a day."""
    if day.day == 1:
        return (day.year, day.month)
    return (day.year + 1, 1) if day.month == 12 else (day.year, day.month + 1)


def first_pass_month(tag, state_id):
    return first_pass_of(deferral_end(held_since(tag, state_id)))


def adjusted(windows):
    """Shift each paced origin's stored first month to its first pass under the campaign-age rule."""
    out = []
    for origin, state_id, first, last in windows:
        tag = origin.upper()
        if tag in HELD_TAGS and tag != 'DEN':
            began = datetime.date(first[0], first[1], 1)
            first = max(first, first_pass_of(deferral_end(began)))
        out.append((origin, state_id, first, last))
    return out


def allocation(origin, state_id):
    inventory, _ = vanilla_european_origin_inventory()
    states = dict(inventory[origin])
    return states[state_id], int(D(states[state_id]) * constant(origin) * 1000 / D(sum(states.values())))


def world(tag, state_id, unpaced=False, held=None):
    r = DatedRuntime()
    if unpaced:
        r.triggers['camp_occ_origin_campaign_deferred'] = list(UNPACED_RULE)
    r.date = datetime.date(1941, 7, 1)
    ger = r.country('GER')
    ger['flags'].add('origin_test_campaign_eligible')
    # Germany's campaign opened on CAMPAIGN_OPENED; German authority over the origin
    # state began on `held`. Both flags carry the staged day, as the production pass
    # would record them.
    ger['flags'].add('camp_occ_campaign_opened')
    ger.setdefault('flag_dates', {})['camp_occ_campaign_opened'] = CAMPAIGN_OPENED
    r.run('camp_occ_initialize_country', 'GER')
    r.scopes[tag] = {'id': tag, 'exists': True, 'flags': set(), 'arrays': {}, 'mods': set()}
    r.global_flags.add('test_exists_' + tag)
    population, allocated = allocation(tag.lower(), state_id)
    r.scopes[state_id] = {
        'id': state_id, 'state': state_id, 'flags': {'camp_occ_origin_assigned', 'test_continent_europe', 'camp_occ_german_authority_held'},
        'flag_dates': {'camp_occ_german_authority_held': held or held_since(tag, state_id)},
        'arrays': {}, 'mods': set(), 'owner': tag, 'controller': 'GER', 'cores': {tag},
        'state_population_k': population / 1000, 'chaos_state_civilian_deaths_total': 0,
        'camp_occ_origin_country': tag, 'camp_occ_origin_ceiling_k': allocated / 1000,
        'camp_occ_origin_observed_population_k': population / 1000, 'camp_occ_origin_observed_state_deaths': 0,
    }
    ger['arrays'].setdefault('camp_occ_eligible_states', []).append(state_id)
    # Seed the production row once, independently of the monthly country
    # registration scan, so this suite isolates only campaign-age eligibility.
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


def origin_scope(r, tag, state_id=None, held=None):
    key = state_id if state_id is not None else 'origin_' + tag
    r.scopes[key] = {'id': key, 'state': key, 'flags': set(), 'arrays': {}, 'mods': set(), 'cores': {tag}}
    if held is not None:
        r.scopes[key]['flags'].add('camp_occ_german_authority_held')
        r.scopes[key]['flag_dates'] = {'camp_occ_german_authority_held': held}
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


def deferred(r, scope):
    return r.cond([('camp_occ_origin_campaign_deferred', '=', 'yes')], scope)


def tests():
    cases = []
    results = {}
    assert FOREIGN_ORIGIN_CAMPAIGN_DAYS == 240 and FOREIGN_ORIGIN_HELD_DAYS == 45, 'camp_occ_timing constants changed'

    # 1. The production trigger at each boundary of the two ages, including both Greek
    #    regions and an Italian core state. Denmark is covered by its own shield below.
    r = DatedRuntime()
    r.global_flags.add('test_exists_DEN')
    r.scopes['DEN'] = {'id': 'DEN', 'exists': True, 'flags': set(), 'arrays': {}, 'mods': set(), 'has_war': False, 'wars': set()}
    ger = r.country('GER')
    boundaries = {}
    boundary_cases = {
        'FRA': ('FRA', 16, HELD['FRA']),
        'HOL': ('HOL', 7, HELD['HOL']),
        'BEL': ('BEL', 6, HELD['BEL']),
        'NOR': ('NOR', 110, HELD['NOR']),
        'GRE_SALONIKA': ('GRE', 731, HELD['GRE_SALONIKA']),
        'GRE_OTHER': ('GRE', 47, HELD['GRE_OTHER']),
        'ITA': ('ITA', 114, HELD['ITA']),
    }
    for label, (tag, state_id, held) in boundary_cases.items():
        scope = origin_scope(r, tag, state_id, held=held)
        end = deferral_end(held)
        ger['flags'].add('camp_occ_campaign_opened')
        ger.setdefault('flag_dates', {})['camp_occ_campaign_opened'] = CAMPAIGN_OPENED
        r.date = end - datetime.timedelta(days=1)
        before = deferred(r, scope)
        r.date = end
        after = deferred(r, scope)
        r.date = CAMPAIGN_OPENED + datetime.timedelta(days=10)
        early = deferred(r, scope)
        assert before and early and not after, (label, before, after, early)
        # Each age alone is not enough: a fresh campaign or a fresh conquest keeps the origin deferred.
        young = origin_scope(r, tag, 'young_' + str(state_id), held=end)
        r.date = end
        assert deferred(r, young), (label, 'authority held only a day')
        boundaries[label] = {'origin': tag, 'state_id': state_id, 'authority_since': held.isoformat(),
                             'deferred_until': end.isoformat(), 'first_campaign_pass': '%d-%02d' % first_pass_month(tag, state_id)}
    # A campaign younger than its threshold defers even a long-held state.
    fresh = origin_scope(r, 'FRA', 'fresh_fra', held=HELD['FRA'])
    r.date = CAMPAIGN_OPENED + datetime.timedelta(days=FOREIGN_ORIGIN_CAMPAIGN_DAYS)
    assert deferred(r, fresh)
    r.date = CAMPAIGN_OPENED + datetime.timedelta(days=FOREIGN_ORIGIN_CAMPAIGN_DAYS + 1)
    assert not deferred(r, fresh)
    # No campaign yet: every paced origin is deferred.
    ger['flags'].discard('camp_occ_campaign_opened')
    r.date = datetime.date(1945, 1, 1)
    assert deferred(r, fresh)
    ger['flags'].add('camp_occ_campaign_opened')
    for tag in UNDEFERRED:
        scope = origin_scope(r, tag, held=HELD['FRA'])
        r.date = CAMPAIGN_OPENED + datetime.timedelta(days=10)
        assert not deferred(r, scope), tag
    results['deferral_boundaries'] = boundaries
    cases.append('the production deferral holds until both the campaign is older than %d days and German authority has held the state more than %d days, for France, the Low Countries, Norway, Salonika state 731, other Greek cores and Italian cores; a young campaign, a fresh conquest and a missing campaign each keep the origin deferred, and the unpaced Poland, Soviet, Baltic, Czech, Yugoslav and Hungarian origins are never deferred' % (FOREIGN_ORIGIN_CAMPAIGN_DAYS, FOREIGN_ORIGIN_HELD_DAYS))

    # Denmark: the cooperating government shields its Jews while it stands unbeaten and at peace.
    den = origin_scope(r, 'DEN', 37, held=HELD['DEN'])
    r.date = deferral_end(HELD['DEN']) + datetime.timedelta(days=400)
    assert deferred(r, den), 'both ages long passed, government standing'
    r.scopes['DEN']['wars'] = {'GER'}
    r.scopes['DEN']['has_war'] = True
    assert not deferred(r, den), 'at war with Germany ends the shield'
    r.scopes['DEN']['wars'] = set()
    r.scopes['DEN']['has_war'] = False
    r.scopes['DEN']['has_capitulated'] = True
    assert not deferred(r, den), 'a fallen government ends the shield'
    r.scopes['DEN']['has_capitulated'] = False
    r.date = CAMPAIGN_OPENED + datetime.timedelta(days=10)
    r.scopes['DEN']['has_capitulated'] = True
    assert deferred(r, den), 'a fallen government alone does not skip the campaign ages'
    results['denmark_shield'] = {'standing': 'deferred', 'at_war_with_germany': 'released', 'capitulated': 'released', 'campaign_young': 'deferred'}
    cases.append('Denmark stays deferred while its government stands unbeaten and at peace with Germany, is released when it goes to war with Germany or falls, and still waits for the campaign and authority ages')

    # 2. The 13-state sensitivity before and after the campaign-age rule.
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
    cases.append('13-state sensitivity: modeled campaign deaths fall from %d (unpaced) to %d once paced origins wait for the campaign age; only the FRA, HOL, BEL, NOR and GRE rows change, and every row still conserves its people' % (total_before, total_after))

    # The 13-state set has only Salonika state 731. Add one other Greek core and one
    # Italian core, comparing the unpaced campaign with the paced one over the same window.
    gre_first = (HELD['GRE_OTHER'].year, HELD['GRE_OTHER'].month)
    ita_first = (HELD['ITA'].year, HELD['ITA'].month)
    representative_windows = [
        ('gre', 47, gre_first, (1945, 4)),
        ('ita', 114, ita_first, (1945, 4)),
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
    cases.append('representative Thessaly state 47 and Italian Sardinia state 114 sensitivity reruns the unpaced and paced windows with conserved source people')

    # 3. The production monthly pass matches the rerun for each changed origin, unpaced and paced.
    production = {}
    for origin, state_id, first, last in nine + four:
        tag = origin.upper()
        if tag not in ('FRA', 'HOL', 'BEL', 'NOR', 'GRE'):
            continue
        began = datetime.date(first[0], first[1], 1)
        old_world, allocated = world(tag, state_id, unpaced=True, held=began)
        run_months(old_world, (1941, 7), last)
        new_world, _ = world(tag, state_id, held=began)
        start = first_pass_of(deferral_end(began))
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
    cases.append('the production monthly pass records no campaign death for a FRA, HOL, BEL, NOR or GRE origin row before the campaign and authority ages pass, then matches the rerun sensitivity within one person per campaign month, unpaced and paced')

    # Run the production monthly pass for an additional Greek zone and Italy.
    incremental_production = {}
    for tag, state_id, first, last in (('GRE', 47, gre_first, (1945, 4)), ('ITA', 114, ita_first, (1945, 4))):
        began = datetime.date(first[0], first[1], 1)
        old_world, allocated = world(tag, state_id, unpaced=True, held=began)
        run_months(old_world, first, last)
        new_world, _ = world(tag, state_id, held=began)
        start = first_pass_of(deferral_end(began))
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
    cases.append('the production monthly pass records no Greek-other or Italian campaign death before the ages pass, then matches each representative sensitivity within one person per campaign month')

    # 4. The manual Auschwitz order reads the same gate.
    manual = {}
    for tag, state_id in (('FRA', 16), ('HOL', 7), ('BEL', 6), ('NOR', 110), ('GRE', 731), ('GRE', 47), ('ITA', 114)):
        m, _ = world(tag, state_id)
        start = first_pass_month(tag, state_id)
        previous = (start[0], start[1] - 1) if start[1] > 1 else (start[0] - 1, 12)
        run_months(m, (1941, 7), previous)
        m.scopes[state_id]['camp_occ_cohort_origin_state'] = state_id
        end = deferral_end(held_since(tag, state_id))
        m.date = end - datetime.timedelta(days=1)
        early = m.cond([('camp_occ_manual_transfer_source_ready', '=', 'yes')], state_id)
        deferral = m.triggers['camp_occ_origin_campaign_deferred']
        m.triggers['camp_occ_origin_campaign_deferred'] = list(UNPACED_RULE)
        early_unpaced = m.cond([('camp_occ_manual_transfer_source_ready', '=', 'yes')], state_id)
        m.triggers['camp_occ_origin_campaign_deferred'] = deferral
        m.date = end
        late = m.cond([('camp_occ_manual_transfer_source_ready', '=', 'yes')], state_id)
        assert not early and late and early_unpaced, (tag, early, late, early_unpaced)
        manual[tag + '_' + str(state_id)] = {'source_ready_day_before': early, 'source_ready_day_before_unpaced': early_unpaced, 'source_ready_on_first_open_day': late}
    results['manual_transfer_source'] = manual
    cases.append('the manual Auschwitz order skips French, Dutch, Belgian, Norwegian, Salonika, other Greek and Italian source cohorts until the campaign and authority ages pass, and permits them from the first open day')

    # 5. The generic campaign rate is unchanged.
    assert constant('german_campaign_monthly_fraction') == D('0.025')
    cases.append('the generic German campaign fraction stays 0.025 per month')
    return cases, results


if __name__ == '__main__':
    cases, results = tests()
    payload = {'status': 'passed', 'count': len(cases), 'cases': cases, 'scenarios': results,
               'limits': 'Parsed production triggers/effects with harness primitives, declared GER controllers over staged windows, and monthly passes on the first of each month. The harness stages the campaign opening and each state\'s German authority day, seeds an aligned cohort row and mocks the population and Deaths primitives; it is not HOI4 execution.'}
    (HERE / 'deportation_start_dates_source_results.json').write_text(json.dumps(payload, indent=2) + '\n')
    print(json.dumps(payload, indent=2))
