"""Production cleanup contracts; native engine primitives are explicit mocks."""
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PLAN = ROOT / 'docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06'
sys.path.insert(0, str(PLAN / 'occupation'))
sys.path.insert(0, str(PLAN))
import foundation_source_tests as foundation
from origin_observer_helper_source_tests import fixture, occupation, observe, known
from origin_parent_lifecycle_source_tests import make_mixed
from origin_records_projection_source_tests import load_ui


class ModifierRuntime(foundation.Runtime):
    def __init__(self):
        super().__init__()
        self.removals = 0

    def execute(self, block, scope, prev=None):
        for key, _, value in block:
            if key == 'remove_dynamic_modifier':
                modifier = foundation.get(value, 'modifier')
                assert modifier in self.scopes[scope]['mods'], 'Native missing-modifier removal'
                self.removals += 1
        return super().execute(block, scope, prev)


def tests():
    cases = []
    r = ModifierRuntime()
    c = r.country('GER', factories=0)
    c['mods'].add('unrelated_modifier')
    for _ in range(64):
        r.run('camp_admin_refresh_country_economy', 'GER')
    assert r.removals == 0 and c['mods'] == {'unrelated_modifier'}
    c['mods'].add('camp_admin_country_economy')
    r.run('camp_admin_refresh_country_economy', 'GER')
    r.run('camp_admin_refresh_country_economy', 'GER')
    assert r.removals == 1 and c['mods'] == {'unrelated_modifier'}
    cases.append('64 absent-modifier refreshes make no removal; a present modifier removes once and repeat is inert')

    r = fixture()
    occupation(r, [10])
    host = observe(r)
    host['state_population_k'] = 95
    assert known(r, 100, 95) == 1
    before = copy.deepcopy(host)
    r.run('camp_origin_adjust_known_receipt', 88)
    assert r.temp['camp_origin_known_contract'] == 0
    assert r.temp['camp_origin_known_adjustment_accepted'] == 0 and host == before
    r.temp['camp_origin_known_contract'] = 1
    r.run('camp_origin_adjust_known_receipt', 88)
    assert r.temp['camp_origin_known_adjustment_accepted'] == 0 and host == before
    host['state_population_k'] = 90
    assert known(r, 95, 90) == 1
    cases.append('Known receipt consumes its value-one token, rejects unarmed/stale replay and permits a fresh complete envelope')

    r, c, a, b = make_mixed()
    r.temp['camp_origin_terminal_close_contract'] = 1
    r.run('camp_admin_integration_close_site', 88, prev='GER')
    assert 'camp_admin_closed' in a['flags'] and r.temp['camp_origin_terminal_close_contract'] == 0
    r.run('camp_admin_integration_close_site', 87, prev='GER')
    assert 'camp_admin_closed' not in b['flags']
    assert r.debits == 0 and r.logged == 0
    cases.append('Terminal close token cannot authorize a following ordinary uncertain-site close')

    r, c, a, b = make_mixed()
    load_ui(r)
    c['arrays']['camp_occ_states'] = [88]
    r.temp['camp_admin_origin_projection_host'] = 999999
    before = copy.deepcopy((a, b))
    for _ in range(2):
        r.run('camp_admin_project_origin_uncertainty', 'GER')
        assert c['camp_admin_gui_uncertain_locations'] == 2
    assert (a, b) == before and r.debits == 0 and r.logged == 0
    cases.append('Projection overwrites poisoned/retained scratch targets before reads and remains duplicate-safe')
    return cases


if __name__ == '__main__':
    cases = tests()
    result = {'evidence': 'Parsed production helpers; mocked native primitives, not live retest', 'count': len(cases), 'cases': cases}
    Path(__file__).with_name('source_results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
