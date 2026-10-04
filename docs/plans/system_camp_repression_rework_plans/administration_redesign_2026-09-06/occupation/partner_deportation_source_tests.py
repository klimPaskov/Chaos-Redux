"""Hungary 1944 partner deportation through the production occupation pass.

Runs the real camp_occ_monthly_country, partner registration, exact custody
transfer, arrival-phase loss and closure bodies with the existing joined
harness. Engine primitives (population credit/debit, Deaths projection) are
harness mocks; controllers, governments and factions are declared per scenario.
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
from danish_rescue_source_tests import RescueRuntime, transform as rescue_transform, months
from test_historical_envelopes import vanilla_european_origin_inventory


def transform(block):
    out = []
    for key, op, value in rescue_transform(block):
        if isinstance(value, list):
            value = transform(value)
        if key == 'is_on_continent':
            out.append(('has_state_flag', '=', 'test_continent_' + value))
        else:
            out.append((key, op, value))
    return out


class PartnerRuntime(RescueRuntime):
    root = 'GER'

    def __init__(self):
        super().__init__()
        self.triggers = {name: transform(body) for name, body in self.triggers.items()}

    def cond(self, block, scope, previous=None):
        return super().cond(transform(block), scope, previous)

    def target(self, x, s, prev):
        if x == 'ROOT':
            return self.root
        if isinstance(x, str) and x.isdigit():
            return int(x)
        return super().target(x, s, prev)

    def execute(self, block, scope, prev=None):
        pending = []
        for key, op, value in block:
            if key == 'every_controlled_state':
                if pending:
                    super().execute(pending, scope, prev)
                    pending = []
                limit = next((v for k, _, v in value if k == 'limit'), [])
                body = [entry for entry in value if entry[0] != 'limit']
                for state_id, state in list(self.scopes.items()):
                    if 'state_population_k' in state and state.get('controller') == scope and self.cond(limit, state_id, scope):
                        self.execute(body, state_id, scope)
            else:
                pending.append((key, op, value))
        if pending:
            super().execute(pending, scope, prev)


def allocations():
    inventory, _ = vanilla_european_origin_inventory()
    states = dict(inventory['hun'])
    total = sum(states.values())
    ceiling = D('445') * 1000
    return {state_id: (population, int(D(population) * ceiling / D(total))) for state_id, population in states.items()}


HUN_STATES = tuple(sorted(allocations()))


def world(government='fascism', faction=True, puppet=False, at_war=False, destination='killing'):
    r = PartnerRuntime()
    r.date = datetime.date(1944, 5, 1)
    ger = r.country('GER')
    ger['flags'].add('origin_test_campaign_eligible')
    r.run('camp_occ_initialize_country', 'GER')
    r.scopes['HUN'] = {'id': 'HUN', 'exists': True, 'flags': set(), 'arrays': {}, 'mods': set(),
                       'government': government, 'wars': set(), 'has_war': False}
    r.global_flags.add('test_exists_HUN')
    if faction:
        r.scopes['HUN']['flags'].add('test_faction_GER')
    if puppet:
        r.scopes['HUN']['overlord'] = 'GER'
    if at_war:
        r.scopes['HUN'].update(has_war=True, wars={'GER'})
    for state_id, (population, allocated) in allocations().items():
        r.scopes[state_id] = {
            'id': state_id, 'state': state_id, 'flags': {'camp_occ_origin_assigned', 'test_continent_europe'},
            'arrays': {}, 'mods': set(), 'owner': 'HUN', 'controller': 'HUN', 'cores': {'HUN'},
            'state_population_k': population / 1000, 'chaos_state_civilian_deaths_total': 0,
            'camp_occ_origin_country': 'HUN', 'camp_occ_origin_ceiling_k': allocated / 1000,
            'camp_occ_origin_observed_population_k': population / 1000, 'camp_occ_origin_observed_state_deaths': 0,
        }
    site = r.state(88, 'GER', population=2000, buildings=2)
    site.update(extermination_camp=2, camp_admin_support_ratio=1)
    if destination == 'killing':
        site['camp_admin_role'] = r.constants['camp_admin_role.killing']
    elif destination == 'detention':
        site['camp_admin_role'] = r.constants['camp_admin_role.custody']
    elif destination == 'lost':
        site['controller'] = 'SOV'
        site['camp_admin_role'] = r.constants['camp_admin_role.killing']
    return r


def run_months(r, start, end):
    for year, month in months(start, end):
        r.date = datetime.date(year, month, 1)
        r.run('camp_occ_monthly_country', 'GER')


def hungarian_rows(r):
    rows = r.scopes['GER']['arrays']
    return [i for i, host in enumerate(rows.get('camp_occ_row_hosts', [])) if host in HUN_STATES]


def snapshot(r):
    site = r.scopes[88]['arrays']
    imported = [i for i, origin in enumerate(site.get('camp_admin_row_origins', [])) if origin in HUN_STATES]
    return {
        'registered_people': round(sum(r.scopes['GER']['arrays']['camp_occ_row_amounts_k'][i] + r.scopes['GER']['arrays']['camp_occ_row_moved_out_k'][i] + r.scopes['GER']['arrays']['camp_occ_row_released_k'][i] for i in hungarian_rows(r)) * 1000),
        'deported_people': round(sum(r.scopes['GER']['arrays']['camp_occ_row_moved_out_k'][i] for i in hungarian_rows(r)) * 1000),
        'released_at_home_people': round(sum(r.scopes['GER']['arrays']['camp_occ_row_released_k'][i] for i in hungarian_rows(r)) * 1000),
        'occupation_deaths_people': round(sum(r.scopes['GER']['arrays']['camp_occ_row_deaths_k'][i] for i in hungarian_rows(r)) * 1000),
        'arrival_deaths_people': round(sum(site['camp_admin_row_deaths_k'][i] for i in imported) * 1000) if imported else 0,
        'living_at_site_people': round(sum(site['camp_admin_row_amounts_k'][i] for i in imported) * 1000) if imported else 0,
    }


def tests():
    cases = []
    results = {}
    allocated = sum(a for _, a in allocations().values())
    share = None

    # A fascist Hungary inside Germany's faction, German killing center operating.
    r = world()
    share = r.constants['camp_occ_partner.hungary_deportation_share']
    run_months(r, (1944, 5), (1944, 5))
    assert not hungarian_rows(r), 'no registration before 15 May 1944'
    population_before = {s: r.scopes[s]['state_population_k'] for s in HUN_STATES + (88,)}
    debits, credits, logged = r.debits, r.credits, r.logged
    r.date = datetime.date(1944, 6, 1)
    r.run('camp_occ_monthly_country', 'GER')
    ger = r.scopes['GER']
    rows = ger['arrays']
    indexes = hungarian_rows(r)
    assert len(indexes) == len(HUN_STATES)
    for i in indexes:
        host = rows['camp_occ_row_hosts'][i]
        assert rows['camp_occ_row_authorities'][i] == 'GER'
        assert rows['camp_occ_row_origins'][i] == host
        assert {'camp_occ_registered', 'camp_occ_partner_host'} <= r.scopes[host]['flags']
        assert r.scopes[host]['controller'] == 'HUN'
        ceiling = allocations()[host][1] / 1000
        registered = rows['camp_occ_row_amounts_k'][i] + rows['camp_occ_row_moved_out_k'][i]
        assert registered <= ceiling * share + 1e-9, (registered, ceiling * share)
        assert rows['camp_occ_row_deaths_k'][i] == 0
    first = snapshot(r)
    assert first['deported_people'] > 0
    moved = first['deported_people']
    assert round(sum(population_before[s] - r.scopes[s]['state_population_k'] for s in HUN_STATES) * 1000) == moved
    arrival = first['arrival_deaths_people']
    assert round((r.scopes[88]['state_population_k'] - population_before[88]) * 1000) == moved - arrival
    assert arrival > 0 and abs(arrival - moved * r.constants['camp_occ_arrival.violence_request_fraction']) <= r.debits
    waves = r.credits - credits
    assert r.debits - debits == 2 * waves and r.logged > logged
    site = r.scopes[88]['arrays']
    for i, origin in enumerate(site['camp_admin_row_origins']):
        if origin in HUN_STATES:
            assert site['camp_admin_row_authorities'][i] == 'GER' and site['camp_admin_row_occupation_roots'][i] > 0
    kinds = rows['camp_admin_history_kinds']
    history_states = [state for kind, state in zip(kinds, rows['camp_admin_history_states'])
                      if kind == r.constants['camp_admin_history_kind.killing_center_transfer']]
    assert history_states and set(history_states) <= set(HUN_STATES)
    assert r.scopes[88]['camp_admin_detainees_k'] <= r.scopes[88]['camp_admin_capacity_k'] + 1e-9
    cases.append('June 1944: every Hungarian-held cohort is registered once under German responsibility at its home state (no more than %.2f of its origin ceiling), %d people move to the state-88 killing center through %d exact waves, each with one debit and one credit, and %d arrival-phase deaths are recorded on their bound rows only' % (share, moved, waves, arrival))

    run_months(r, (1944, 7), (1944, 7))
    second = snapshot(r)
    assert second['deported_people'] >= first['deported_people']
    run_months(r, (1944, 8), (1944, 9))
    final = snapshot(r)
    assert final['deported_people'] == second['deported_people'], 'no movement after 9 July 1944'
    for i in hungarian_rows(r):
        host = rows['camp_occ_row_hosts'][i]
        assert 'camp_occ_closed' in r.scopes[host]['flags']
        assert rows['camp_occ_row_amounts_k'][i] == 0 and rows['camp_occ_row_statuses'][i] == r.constants['camp_occ_row_status.released']
    assert final['occupation_deaths_people'] == 0
    assert final['registered_people'] == final['deported_people'] + final['released_at_home_people']
    assert final['registered_people'] <= round(allocated * share) + len(HUN_STATES)
    results['fascist_axis_hungary'] = dict(final, origin_ceiling_people=allocated, order_share=share)
    cases.append('after the 9 July 1944 halt nothing more moves; every Hungarian host closes and its remaining order cohort (%d people) is released at home; no campaign death is recorded inside Hungary; registered = deported + released' % final['released_at_home_people'])

    # Repeat month does nothing twice.
    again = copy.deepcopy(r.scopes)
    r.run('camp_occ_monthly_country', 'GER')
    assert r.scopes == again
    cases.append('a repeated monthly pass in the same month changes nothing')

    puppet = world(government='neutrality', faction=False, puppet=True)
    run_months(puppet, (1944, 6), (1944, 6))
    assert snapshot(puppet)['deported_people'] > 0
    cases.append('a Hungary that is a German subject is deported from under any government')

    for label, kwargs in (('Horthy-government Axis member', dict(government='neutrality')),
                          ('Hungary outside the faction', dict(faction=False)),
                          ('Hungary at war with Germany', dict(at_war=True)),
                          ('no killing role at state 88', dict(destination='detention')),
                          ('state 88 lost to the Soviet Union', dict(destination='lost'))):
        bad = world(**kwargs)
        before = copy.deepcopy({s: bad.scopes[s] for s in HUN_STATES})
        run_months(bad, (1944, 6), (1944, 7))
        assert not hungarian_rows(bad), label
        assert {s: bad.scopes[s] for s in HUN_STATES} == before, label
        assert bad.debits == 0 and bad.credits == 0 and bad.logged == 0, label
        cases.append('%s: nothing is registered, moved or recorded' % label)

    for year in (1942, 1943):
        r2 = world()
        r2.date = datetime.date(year, 6, 1)
        r2.run('camp_occ_monthly_country', 'GER')
        assert not hungarian_rows(r2)
    cases.append('outside 15 May - 9 July 1944 (June 1942, June 1943) nothing is registered or moved')

    # Hungary leaves the faction after the first pass: the order lapses, hosts close.
    lapse = world()
    run_months(lapse, (1944, 6), (1944, 6))
    moved_first = snapshot(lapse)['deported_people']
    lapse.scopes['HUN']['flags'].discard('test_faction_GER')
    run_months(lapse, (1944, 7), (1944, 7))
    lapsed = snapshot(lapse)
    assert lapsed['deported_people'] == moved_first
    assert all('camp_occ_closed' in lapse.scopes[s]['flags'] for s in HUN_STATES)
    cases.append('when Hungary leaves the German faction mid-window the order lapses: no further movement, hosts close, the remainder is released at home')

    # A German-occupied Hungarian state follows the ordinary occupation path, never the partner path.
    occupied = world()
    occupied.scopes[HUN_STATES[0]]['controller'] = 'GER'
    occupied.scopes['GER']['arrays'].setdefault('camp_occ_eligible_states', []).append(HUN_STATES[0])
    run_months(occupied, (1944, 6), (1944, 6))
    assert 'camp_occ_partner_host' not in occupied.scopes[HUN_STATES[0]]['flags']
    assert 'camp_occ_registered' in occupied.scopes[HUN_STATES[0]]['flags']
    assert len(hungarian_rows(occupied)) == len(HUN_STATES)
    cases.append('a Hungarian state under direct German control registers once through the ordinary occupation path and is not re-registered as a partner cohort')
    return cases, results, allocated


if __name__ == '__main__':
    cases, results, allocated = tests()
    payload = {'status': 'passed', 'count': len(cases), 'cases': cases, 'hungarian_origin_ceiling_people': allocated,
               'scenarios': results,
               'limits': 'Parsed production bodies with harness primitives; declared controllers, governments and factions; one state-88 fixture with two extermination and two concentration levels at full support. No HOI4 execution.'}
    (HERE / 'partner_deportation_source_results.json').write_text(json.dumps(payload, indent=2) + '\n')
    print(json.dumps(payload, indent=2))
