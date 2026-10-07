"""Execute parent candidate initialization/dispatch prefixes.

Fresh collection executes real candidate helpers. Frozen replay is a declared
durable-receipt callback fixture, not validation of native receipt admission.
These prefixes do not execute whole opening or scenario transactions.
"""
from decimal import Decimal
import unittest

from test_event021_candidate_output_lifetime import ALIGNED, PARENT, CandidateRuntime


COLLECT = 'event021_parent_collect_dynamic_optional_front_candidates'
REPLAY = 'event021_parent_load_scenario_optional_front_rows'
FROZEN = 'random_civil_war_scenario_optional_front_plan_frozen'


def bodies(nodes):
    yield nodes
    for _, data in nodes:
        if isinstance(data, list):
            yield from bodies(data)


def dispatch_prefix(name, helper):
    """Select the actual ownership/dispatch prefix, not a reconstructed one."""
    for body in bodies(PARENT[name]):
        for index, node in enumerate(body):
            direct = node == (helper, 'yes')
            conditional = node[0] == 'if' and (helper, 'yes') in node[1]
            if not (direct or conditional):
                continue
            starts = [i for i, (key, data) in enumerate(body[:index])
                      if key == 'clear_temp_array' and data == ALIGNED[0]]
            if not starts:
                continue
            end = index + 1
            if conditional and end < len(body) and body[end][0] == 'else':
                end += 1
            return body[starts[-1]:end]
    raise AssertionError(f'No caller-owned dispatch prefix for {name}/{helper}')


class ParentRuntime(CandidateRuntime):
    def __init__(self):
        super().__init__()
        self.replays = 0
        # A declared immutable normal-country receipt, separate from scratch.
        self.durable = {name: [Decimal(55)] for name in ALIGNED}

    def call(self, name, actor):
        if name != REPLAY:
            return super().call(name, actor)
        scalars, arrays = set(self.temporary), set(self.temp_arrays)
        self.replays += 1
        self.temp_arrays.update({key: list(value) for key, value in self.durable.items()})
        self.temporary.update(event021_parent_dynamic_optional_front_valid=Decimal(1),
                              event021_parent_dynamic_optional_front_count=Decimal(1))
        self.temporary = {k: v for k, v in self.temporary.items() if k in scalars}
        self.temp_arrays = {k: v for k, v in self.temp_arrays.items() if k in arrays}


class ParentCandidateLifetimeTests(unittest.TestCase):
    def test_opening_builder_owns_actual_fresh_collector_results(self):
        rt = ParentRuntime()
        rt.run(dispatch_prefix('event021_parent_build_front_plan', COLLECT), rt.host)
        self.assertEqual(rt.temporary['event021_parent_dynamic_optional_front_count'], 2)
        self.assertEqual(rt.temporary['event021_parent_dynamic_optional_front_valid'], 1)
        self.assertEqual(rt.temp_arrays[ALIGNED[-1]], rt.states)
        self.assertTrue(set(ALIGNED) <= set(rt.temp_arrays))

    def test_scenario_freezer_owns_actual_fresh_collector_results(self):
        rt = ParentRuntime()
        rt.run(dispatch_prefix('event021_parent_freeze_scenario_plan', COLLECT), rt.host)
        self.assertEqual(rt.temporary['event021_parent_dynamic_optional_front_count'], 2)
        self.assertEqual(rt.temporary['event021_parent_dynamic_optional_front_valid'], 1)
        self.assertEqual(rt.temp_arrays[ALIGNED[-1]], rt.states)

    def test_frozen_builder_replays_durable_rows_at_consumption(self):
        rt = ParentRuntime()
        rt.host.flags.add(FROZEN)
        rt.temp_arrays.update({name: [Decimal(999)] for name in ALIGNED})
        rt.run(dispatch_prefix('event021_parent_build_front_plan', COLLECT), rt.host)
        self.assertEqual(rt.replays, 1)
        self.assertEqual(rt.temp_arrays, rt.durable)
        self.assertEqual(rt.temporary['event021_parent_dynamic_optional_front_count'], 1)
        self.assertFalse(any(name == COLLECT for name, _, _ in rt.calls))

    def test_frozen_apply_owns_replay_results_without_reroll(self):
        rt = ParentRuntime()
        rt.run(dispatch_prefix('event021_parent_apply_frozen_scenario_plan', REPLAY), rt.host)
        self.assertEqual(rt.replays, 1)
        self.assertEqual(rt.temp_arrays, rt.durable)
        self.assertEqual(rt.temporary['event021_parent_dynamic_optional_front_valid'], 1)


if __name__ == '__main__':
    unittest.main()
