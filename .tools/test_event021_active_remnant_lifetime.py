"""Actual-source remnant measurement and state-retention regressions.

Only the builder's state-retention phase and complete measurement helper run.
Adjacency and ownership are declared fixtures, not engine observations.
Force allocation, country creation and commit are not modeled.
"""
from decimal import Decimal
import unittest

from test_event021_active_front_receipt import ACTIVE, ReceiptRuntime, State


class MapRuntime(ReceiptRuntime):
    def __init__(self):
        super().__init__()
        self.states = [State(i, self.source, self.source) for i in (1, 2, 3, 4)]
        for index, state in enumerate(self.states):
            state.flags = set()
            state.neighbors = self.states[max(0, index - 1):index] + self.states[index + 1:index + 2]
        self.source.values['capital'] = self.states[0]
        self.source.values['owned_states'] = self.states

    def value(self, token, actor):
        if token == 'event021_active_remnant_reach' and token not in self.temp_arrays:
            return []  # Declared missing-output fixture, not engine evidence.
        return super().value(token, actor)

    def condition(self, nodes, actor):
        for key, data in nodes:
            if key == 'has_state_flag':
                result = data in actor.flags
            elif key == 'any_neighbor_state':
                result = any(self.condition(data, neighbor) for neighbor in actor.neighbors)
            else:
                result = super().condition([(key, data)], actor)
            if not result:
                return False
        return True

    def run(self, nodes, actor):
        previous_if = None
        for key, data in nodes:
            if key.startswith('event_target:'):
                self.run(data, self.targets[key[13:]])
            elif key == 'capital_scope':
                self.run(data, actor.values['capital'])
            elif key == 'every_owned_state':
                fields = dict(data)
                for state in actor.values['owned_states']:
                    if state.owner is actor and self.condition(fields.get('limit', []), state):
                        self.run([(k, v) for k, v in data if k != 'limit'], state)
            elif key == 'while_loop_effect':
                fields = dict(data)
                iterations = 0
                while self.condition(fields['limit'], actor):
                    iterations += 1
                    if iterations > 1000:
                        raise AssertionError('Fixture exceeded native effect-loop limit')
                    self.run([(k, v) for k, v in data if k != 'limit'], actor)
            elif key in ('set_state_flag', 'clr_state_flag'):
                (actor.flags.add if key == 'set_state_flag' else actor.flags.discard)(data)
            elif key == 'remove_from_temp_array':
                fields = dict(data)
                self.temp_arrays[fields['array']].remove(self.value(fields['value'], actor))
            elif key == 'if':
                previous_if = self.condition(dict(data)['limit'], actor)
                if previous_if:
                    self.run([(k, v) for k, v in data if k != 'limit'], actor)
            elif key == 'else':
                if previous_if is None:
                    raise AssertionError('else without a paired condition')
                if not previous_if:
                    self.run(data, actor)
            else:
                super().run([(key, data)], actor)

    def retention_phase(self, candidate):
        self.temp_arrays.update(event021_parent_dynamic_optional_front_archetypes=[Decimal(1)],
                                event021_parent_dynamic_optional_front_state_offsets=[Decimal(0)],
                                event021_parent_dynamic_optional_front_state_counts=[Decimal(2)],
                                event021_parent_dynamic_optional_front_selected_states=candidate)
        body = next(data for key, data in ACTIVE['event021_parent_build_active_front_rows'] if key == 'if')
        phase = []
        for node in body:
            if node[0] == 'limit':
                continue
            if node == ('set_temp_variable', [('event021_active_weight_remaining', 'constant:random_civil_war_value.zero')]):
                break
            phase.append(node)
        self.run(phase, self.host)
        return self.temp_arrays['event021_active_accepted_rows']


class RemnantLifetimeTests(unittest.TestCase):
    def test_caller_owned_membership_and_count_survive_measurement(self):
        rt = MapRuntime()
        rt.temp_arrays.update(event021_active_excluded_states=[], event021_active_remnant_reach=[])
        rt.temporary.update(event021_active_remnant_reached=Decimal(0), event021_active_remnant_growth=Decimal(0))
        rt.call('event021_parent_measure_active_source_remnant', rt.host)
        self.assertEqual(rt.temp_arrays['event021_active_remnant_reach'], rt.states)
        self.assertEqual(rt.temporary['event021_active_remnant_reached'], 4)
        self.assertTrue(all(not state.flags for state in rt.states))

    def test_connected_leaf_region_keeps_the_two_state_remnant(self):
        rt = MapRuntime()
        self.assertEqual(rt.retention_phase(rt.states[2:]), [Decimal(0)])
        self.assertEqual(rt.temporary['event021_active_remnant_reached'], 2)
        self.assertTrue(all(not state.flags for state in rt.states))

    def test_articulation_region_is_rejected_and_markers_are_cleared(self):
        rt = MapRuntime()
        self.assertEqual(rt.retention_phase(rt.states[1:3]), [])
        self.assertEqual(rt.temp_arrays['event021_active_excluded_states'], [])
        self.assertTrue(all(not state.flags for state in rt.states))


if __name__ == '__main__':
    unittest.main()
