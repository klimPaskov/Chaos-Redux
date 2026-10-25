"""Actual-source remnant measurement and state-retention regressions.

Only the builder's state-retention phase and complete measurement helper run.
Adjacency and ownership are declared fixtures, not engine observations.
Force allocation, country creation and commit are not modeled.
"""
from decimal import Decimal, ROUND_HALF_UP
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
            if key == 'AND':
                result = self.condition(data, actor)
            elif key.startswith('event_target:'):
                result = self.condition(data, self.targets[key[13:]])
            elif key == 'capital_scope':
                result = self.condition(data, actor.values['capital'])
            elif key == 'exists':
                result = actor.exists == (data == 'yes')
            elif key == 'has_capitulated':
                result = getattr(actor, 'capitulated', False) == (data == 'yes')
            elif key == 'has_event_target':
                result = data in self.targets
            elif key == 'has_state_flag':
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
            elif key == 'multiply_temp_variable':
                name, token = data[0]
                self.temporary[name] *= self.value(token, actor)
            elif key == 'round_temp_variable':
                self.temporary[data] = self.temporary[data].quantize(Decimal(1), rounding=ROUND_HALF_UP)
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


class LiveRemnantProofTests(unittest.TestCase):
    def fixture(self):
        rt = MapRuntime()
        rt.source.values.update(random_civil_war_generation=Decimal(0), num_divisions=Decimal(6))
        rt.temporary.update(event021_active_commit_row=Decimal(0), event021_active_commit_generation=Decimal(0),
                            event021_active_review_row_generation=Decimal(0), event021_active_source_divisions=Decimal(6),
                            event021_active_commit_remnant_valid=Decimal(0), event021_active_commit_markers_expected=Decimal(0))
        rt.host.values.update(random_civil_war_active_front_state_entries=rt.states,
                              random_civil_war_active_front_state_offsets=[Decimal(2)],
                              random_civil_war_active_front_state_counts=[Decimal(2)],
                              random_civil_war_active_front_force_divisions=[Decimal(2)])
        return rt

    def prove(self, rt):
        rt.call('event021_parent_validate_active_source_remnant_now', rt.host)
        self.assertTrue(all(not state.flags for state in rt.states))
        self.assertEqual(rt.temp_arrays, {})
        return rt.temporary['event021_active_commit_remnant_valid']

    def test_current_leaf_and_reserved_force_are_proven(self):
        self.assertEqual(self.prove(self.fixture()), 1)

    def test_live_capital_generation_and_division_changes_reject(self):
        cases = {
            'lost capital control': lambda r: setattr(r.states[0], 'controller', r.host),
            'lost capital ownership': lambda r: setattr(r.states[0], 'owner', r.host),
            'generation changed': lambda r: r.source.values.update(random_civil_war_generation=Decimal(1)),
            'registered generation changed': lambda r: r.temporary.update(event021_active_review_row_generation=Decimal(1)),
            'division loss': lambda r: r.source.values.update(num_divisions=Decimal(5)),
            'capitulated': lambda r: setattr(r.source, 'capitulated', True),
            'borrowed marker': lambda r: r.states[2].flags.add('random_civil_war_secondary_transfer_state'),
        }
        for name, change in cases.items():
            with self.subTest(name=name):
                rt = self.fixture()
                change(rt)
                if name == 'borrowed marker':
                    rt.call('event021_parent_validate_active_source_remnant_now', rt.host)
                    self.assertEqual(rt.temporary['event021_active_commit_remnant_valid'], 0)
                    self.assertIn('random_civil_war_secondary_transfer_state', rt.states[2].flags)
                else:
                    self.assertEqual(self.prove(rt), 0)

    def test_failed_prior_leaf_does_not_allow_its_bridge_to_detach(self):
        rt = self.fixture()
        # capital/retained -> bridge -> leaf; the leaf's prior attempt failed.
        rt.states = [State(i, rt.source, rt.source) for i in range(1, 7)]
        for index, state in enumerate(rt.states):
            state.flags = set()
            state.neighbors = rt.states[max(0, index - 1):index] + rt.states[index + 1:index + 2]
        rt.source.values.update(capital=rt.states[0], owned_states=rt.states, num_divisions=Decimal(20))
        rt.temporary['event021_active_source_divisions'] = Decimal(20)
        rt.host.values['random_civil_war_active_front_state_entries'] = rt.states
        # Detaching states 3/4 leaves two reachable capital states, but isolates 5/6.
        self.assertEqual(self.prove(rt), 0)
        # If the prior leaf really left, removing the bridge no longer cuts retained states.
        for state in rt.states[4:]:
            state.owner = state.controller = rt.host
        rt.source.values['num_divisions'] = Decimal(18)
        self.assertEqual(self.prove(rt), 1)

    def test_original_reserve_is_not_rebased_after_an_earlier_split(self):
        rt = self.fixture()
        rt.temporary['event021_active_source_divisions'] = Decimal(20)
        reserve = (Decimal(20) * rt.value('constant:event021_active_review.remnant_division_share', rt.host)).to_integral_value(rounding='ROUND_CEILING')
        rt.source.values['num_divisions'] = reserve + Decimal(1)
        # The live count exceeds the requested two, but its remainder would
        # fall one division below the original constant-backed reserve.
        self.assertEqual(self.prove(rt), 0)


if __name__ == '__main__':
    unittest.main()
