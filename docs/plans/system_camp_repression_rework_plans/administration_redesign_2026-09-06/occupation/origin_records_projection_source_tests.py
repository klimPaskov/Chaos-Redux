"""Production display projection, with declared record states and mocked primitives."""
import copy
import json
from pathlib import Path
from origin_parent_lifecycle_source_tests import make_mixed, LifecycleRuntime
from origin_observer_owner_integration_source_tests import ROOT, foundation

HERE = Path(__file__).resolve().parent


def load_ui(r):
    r.triggers.update({k: v for k, _, v in foundation.parse((ROOT / 'common/scripted_triggers/camp_administration_ui_triggers.txt').read_text())})


def run_cases():
    out = []
    r, c, a, b = make_mixed()
    load_ui(r)
    c['arrays']['camp_occ_states'] = [88]
    state_before = copy.deepcopy((a, b))
    r.run('camp_admin_project_origin_uncertainty', 'GER')
    assert c['camp_admin_gui_uncertain_locations'] == 2
    assert (a, b) == state_before and r.logged == 0 and r.debits == 0
    # This scratch target is assigned before every loop read; its absence
    # after return is not part of the projection's observable contract.
    out.append('Two uncertain custody hosts with one co-located occupation reference count twice, not three times, without state/death mutation')

    r = LifecycleRuntime()
    c = r.country('GER')
    a = r.state(88, 'GER')
    a['flags'].add('camp_origin_ambiguous')
    c['arrays']['camp_active_site_states'] = []
    c['arrays']['camp_occ_states'] = [88]
    load_ui(r)
    before = copy.deepcopy(a)
    r.run('camp_admin_project_origin_uncertainty', 'GER')
    assert c['camp_admin_gui_uncertain_locations'] == 1 and a == before
    out.append('Occupation-only uncertain host remains in Records projection')

    r = LifecycleRuntime()
    c = r.country('GER')
    r.state(88, 'GER')
    load_ui(r)
    r.run('camp_admin_project_origin_uncertainty', 'GER')
    assert c['camp_admin_gui_uncertain_locations'] == 0
    out.append('Healthy empty initialized host shows no uncertain-origin warning')
    return out


if __name__ == '__main__':
    cases = run_cases()
    result = {'scope': 'Parsed source projection only; no GUI pixel or engine proof', 'count': len(cases), 'cases': cases}
    (HERE / 'origin_records_projection_source_results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
