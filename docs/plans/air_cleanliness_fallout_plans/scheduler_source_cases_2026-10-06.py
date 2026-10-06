"""Production selector-condition regression cases, not probability evidence.

The score calculator and broad eligibility predicate are declared external
inputs; these tests execute the actual first-found and tie conditions.
Native queue delivery and complete receipt validation require MCP/live checks.
"""
import importlib.util
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('fallout_memory_cases', here / 'winter_recovery_source_cases_2026-10-06.py')
model = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = model
spec.loader.exec_module(model)
root = here.parents[2]
source = (root / 'common/scripted_effects/fallout_consolidated_effects.txt').read_text(encoding='utf-8-sig')
node = model.definition(source, 'fallout_event_select_reviewed_candidate')
loop = node.children('if')[0].children('for_each_loop')[0]
eligible = loop.children('if')[0]
gate = eligible.children('if')[0].children('limit')[0]
assert eligible.children('limit')[0].scalar('fallout_event_candidate_row_is_eligible') == 'yes'

defaults = {
    'fallout_event_selected_candidate_found': 1,
    'fallout_event_candidate_score': -5,
    'fallout_event_selected_candidate_score': -5,
    'fallout_event_candidate_tie_priority': 2,
    'fallout_event_selected_candidate_priority': 2,
    'fallout_event_candidate_loop_id': 20,
    'fallout_event_selected_candidate_id': 20,
    'fallout_event_candidate_target_entries^fallout_event_candidate_loop_index': 4,
    'fallout_event_selected_candidate_target': 4,
    'fallout_event_candidate_partner_registry_index_entries^fallout_event_candidate_loop_index': 2,
    'fallout_event_selected_candidate_partner': 2,
}
cases = [
    ('first_negative', {'fallout_event_selected_candidate_found': 0, 'fallout_event_selected_candidate_score': 0}, True),
    ('first_zero', {'fallout_event_selected_candidate_found': 0, 'fallout_event_candidate_score': 0}, True),
    ('negative_ranking', {'fallout_event_candidate_score': -2}, True),
    ('lower_negative', {'fallout_event_candidate_score': -8}, False),
    ('priority_tie', {'fallout_event_candidate_tie_priority': 1}, True),
    ('id_tie', {'fallout_event_candidate_loop_id': 19}, True),
    ('target_tie', {'fallout_event_candidate_target_entries^fallout_event_candidate_loop_index': 3}, True),
    ('partner_tie', {'fallout_event_candidate_partner_registry_index_entries^fallout_event_candidate_loop_index': 1}, True),
    ('unchanged_exact_tie', {}, False),
]
for name, changes, expected in cases:
    world = model.World()
    world.country['vars'].update(defaults)
    world.country['vars'].update(changes)
    assert world.conditions(gate.children(), world.country) == expected, name

# Check the actual saved numerical-row score contract independently of the
# unrelated registry/header predicates in the larger trigger.
triggers = (root / 'common/scripted_triggers/fallout_consolidated_triggers.txt').read_text(encoding='utf-8-sig')
row = model.definition(triggers, 'fallout_event_country_runtime_row_is_current')
score_gate = next(n for n in row.children('OR') if any(
    c.scalar('fallout_event_last_selected_score') == 'constant:fallout_event_runtime.zero'
    for a in n.children('AND') for c in a.children('check_variable')))
for candidate, score, expected in ((0, 0, True), (0, -1, False), (20, -5, True), (20, 0, True)):
    world = model.World()
    world.country['vars'].update(fallout_event_last_selected_candidate_id=candidate, fallout_event_last_selected_score=score)
    assert world.conditions([score_gate], world.country) == expected
print(f'{len(cases) + 4} production selector/score cases passed; no probability or queue-delivery claim.')

# Execute the real saved-quote refund, including its consume-before-credit
# order, with only native currency/variable primitives modelled.
refund = model.definition(source, 'air_cleanliness_treaty_refund_relief_vote_quote')
for paid, expected in ((25, 100), (27, 102), (0, 75), (None, 75)):
    world = model.World()
    world.country['vars']['political_power'] = 75
    if paid is not None:
        world.country['vars']['air_cleanliness_treaty_relief_vote_paid_quote'] = paid
    world.execute(refund.children())
    assert world.country['vars']['political_power'] == expected
    assert 'air_cleanliness_treaty_relief_vote_paid_quote' not in world.country['vars']
    world.execute(refund.children())
    assert world.country['vars']['political_power'] == expected
print('4 saved-quote/refund cases passed; repeated cancellation cannot credit twice.')
