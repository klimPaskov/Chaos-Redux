"""Terminal caller integration, using production closure with native primitives mocked."""
from pathlib import Path
import copy
import json
from origin_observer_owner_integration_source_tests import JoinedRuntime, ROOT, foundation, custody

HERE = Path(__file__).resolve().parent


class LifecycleRuntime(JoinedRuntime):
    def __init__(self):
        super().__init__()
        self.effects.update({k: v for k, _, v in foundation.parse((ROOT / 'common/scripted_effects/camp_administration_integration_effects.txt').read_text(encoding='utf-8-sig')) if not k.startswith('@')})
        self.effects.update({k: v for k, _, v in foundation.parse((ROOT / 'common/scripted_effects/camp_administration_country_effects.txt').read_text(encoding='utf-8-sig')) if k == 'camp_admin_country_clear_engineer_pending_receipt'})
        # These country policy/mission adapters have separate owner suites.
        for name in ('camp_rework_usa_cancel_security_sunset', 'camp_admin_country_halt', 'camp_administration_civil_cleanup', 'camp_admin_integration_cancel_routine_projects'):
            self.effects[name] = []
    def cond(self, block, scope, previous=None):
        for key, op, value in block:
            if key in ('AND', 'OR', 'NOT'):
                vals = [self.cond([item], scope, previous) for item in value]
                okay = all(vals) if key == 'AND' else any(vals) if key == 'OR' else not any(vals)
                if not okay:
                    return False
            elif key == 'has_active_mission':
                if value not in self.scopes[scope].get('missions', set()):
                    return False
            elif not super().cond([(key, op, value)], scope, previous):
                return False
        return True


def make_mixed():
    r = LifecycleRuntime()
    c = r.country('GER')
    r.country('POL')
    a = r.state(88, 'GER', population=100, buildings=2)
    b = r.state(87, 'GER', population=100, buildings=2)
    custody(r, [10, 10], origins=[87, 88])
    b['arrays'] = copy.deepcopy(a['arrays'])
    b.update(camp_admin_detainees_k=20, camp_admin_row_count=2, camp_admin_next_row_id=3)
    r.run('camp_origin_observe_host', 88)
    r.run('camp_origin_observe_host', 87)
    for host in (88, 87):
        r.scopes[host]['state_population_k'] = 90
        r.scopes[host]['chaos_state_civilian_deaths_total'] = 10000
        r.run('camp_origin_observe_host', host)
    return r, c, a, b


def run_cases():
    results = []
    r, c, a, _ = make_mixed()
    rows = copy.deepcopy(a['arrays'])
    r.run('camp_admin_integration_close_site', 88, prev='GER')
    assert 'camp_admin_closed' not in a['flags'] and a['arrays'] == rows
    assert not c['arrays'].get('camp_admin_history_ids') and r.logged == 0
    results.append('Ordinary controlled uncertain closure rejects without history or release')

    r, c, a, b = make_mixed()
    before_rows = copy.deepcopy(a['arrays'])
    before_population = (a['state_population_k'], b['state_population_k'])
    c['flags'].add('camp_admin_country_engineer_release_pending')
    c.update(camp_admin_country_engineer_receipt_k=10, camp_admin_country_engineer_receipt_state_id=88, camp_admin_country_engineer_receipt_authority='GER', camp_admin_country_engineer_receipt_program=9, camp_admin_country_engineer_receipt_progress=6, camp_admin_country_engineer_receipt_target=6)
    r.run('camp_admin_integration_close_country', 'GER')
    assert 'camp_admin_closed' in a['flags'] and 'camp_admin_closed' in b['flags']
    assert a['arrays'] == before_rows and a['camp_admin_detainees_k'] == 20
    assert (a['state_population_k'], b['state_population_k']) == before_population
    assert r.logged == 0 and r.debits == 0
    assert r.temp['camp_origin_terminal_close_contract'] == 0
    assert 'camp_admin_country_engineer_release_pending' not in c['flags']
    assert not any(key.startswith('camp_admin_country_engineer_receipt_') for key in c)
    history = list(c['arrays'].get('camp_admin_history_ids', []))
    assert len(history) == 2
    r.run('camp_admin_integration_close_country', 'GER')
    assert c['arrays']['camp_admin_history_ids'] == history and a['arrays'] == before_rows
    results.append('Terminal country stages every site, preserves uncertain rows, records closure once and makes no population/death transaction')
    return results


if __name__ == '__main__':
    cases = run_cases()
    data = {'scope': 'Parsed production caller/closure, mocked engine primitives and unrelated country policy adapters', 'cases': cases, 'count': len(cases)}
    (HERE / 'origin_parent_lifecycle_source_results.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(data, indent=2))
