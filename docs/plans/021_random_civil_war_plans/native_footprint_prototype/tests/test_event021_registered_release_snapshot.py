"""Execute production territory snapshot preparation on declared worlds.

This tests the owner-held journal, source parameter restoration and complete
membership. It does not execute release, admission, allocations or rollback.
"""
from decimal import Decimal
import operator
import unittest

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), *['..']*5, '.tools'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_event021_native_footprint_query import Country, State, Runtime, EFFECTS
from test_event021_evolution_log import load


PARENT = dict(load('docs/plans/021_random_civil_war_plans/native_footprint_prototype/script/021_random_civil_war_registered_release_effects.txt'))
PREPARE = 'event021_parent_prepare_registered_release_snapshot'
PREFIX = 'random_civil_war_release_'


def native_comparisons(nodes):
    """Model literal native >/< triples emitted by the shared simple parser."""
    result, index = [], 0
    while index < len(nodes):
        key, data = nodes[index]
        if data is None and index + 2 < len(nodes) and nodes[index + 1][0] in ('>', '<'):
            result.append(('check_variable', [('var', key), ('value', nodes[index + 2][0]),
                                              ('compare', 'greater_than' if nodes[index + 1][0] == '>' else 'less_than')]))
            index += 3
        else:
            result.append((key, data))
            index += 1
    return result


class SnapshotRuntime(Runtime):
    def __init__(self):
        super().__init__()
        self.owner = self.root
        for country in self.world:
            country.flags = set()
        self.previous = None
        carrier = self.tags['SCO']
        self.states = [State(i, self.source, self.source, {carrier, self.source}) for i in (120, 121, 133, 136)]
        self.states.append(State(933, self.source, self.other, {carrier}))
        self.anchor = self.states[1]
        self.owner.values.update(random_civil_war_release_source_scope=self.source,
                                 random_civil_war_event6_package_id=self.packages[0][0],
                                 random_civil_war_event6_anchor_state=self.anchor,
                                 random_civil_war_release_authorized_states=[])

    def value(self, token, actor):
        if token == 'PREV':
            return self.previous
        if token.startswith('event_target:') and '.' in token[13:]:
            name, rest = token[13:].split('.', 1)
            return self.value(rest, self.targets[name])
        return super().value(token, actor)

    def condition(self, nodes, actor):
        for key, data in native_comparisons(nodes):
            if key == 'has_country_flag':
                result = data in actor.flags
            elif key == 'AND':
                result = self.condition(data, actor)
            elif key == 'OR':
                result = any(self.condition([node], actor) for node in native_comparisons(data))
            elif key == 'has_state_flag':
                result = data in actor.flags
            elif key == 'any_neighbor_state':
                result = any(self.condition(data, neighbor) for neighbor in actor.neighbors)
            elif key.startswith('var:'):
                result = self.condition(data, self.value(key[4:], actor))
            elif key in ('is_owned_by', 'is_controlled_by'):
                result = (actor.owner if key == 'is_owned_by' else actor.controller) is self.value(data, actor)
            elif key == 'check_variable':
                fields = dict(data)
                result = {'equals': operator.eq, 'greater_than': operator.gt, 'less_than': operator.lt,
                          'greater_than_or_equals': operator.ge}[fields['compare']](
                    self.value(fields['var'], actor), self.value(fields['value'], actor))
            else:
                result = super().condition([(key, data)], actor)
            if not result:
                return False
        return True

    def scoped(self, body, target, caller):
        previous = self.previous
        self.previous = caller
        try:
            self.run(body, target)
        finally:
            self.previous = previous

    def call(self, name, actor=None):
        actor = actor or self.owner
        scalars, arrays = set(self.temp), set(self.arrays)
        self.run((PARENT if name in PARENT else EFFECTS)[name], actor)
        self.temp = {k: v for k, v in self.temp.items() if k in scalars}
        self.arrays = {k: v for k, v in self.arrays.items() if k in arrays}

    def run(self, nodes, actor):
        taken = False
        for key, data in nodes:
            if key in ('if', 'else_if', 'else'):
                if key == 'if':
                    taken = False
                if not taken and (key == 'else' or self.condition(dict(data)['limit'], actor)):
                    self.run([(k, v) for k, v in data if k != 'limit'], actor)
                    taken = True
            elif key == 'set_variable':
                name, token = data[0]
                actor.values[name] = self.value(token, actor)
            elif key == 'clear_variable':
                actor.values.pop(data, None)
            elif key == 'clear_array':
                actor.values[data] = []
            elif key == 'add_to_array':
                fields = dict(data)
                actor.values[fields['array']].append(self.value(fields['value'], actor))
            elif key in ('set_country_flag', 'clr_country_flag'):
                (actor.flags.add if key == 'set_country_flag' else actor.flags.discard)(data)
            elif key in ('set_state_flag', 'clr_state_flag'):
                (actor.flags.add if key == 'set_state_flag' else actor.flags.discard)(data)
            elif key in ('add_to_temp_variable', 'subtract_from_temp_variable'):
                name, token = data[0]
                self.temp[name] += self.value(token, actor) * (1 if key == 'add_to_temp_variable' else -1)
            elif key == 'capital_scope':
                self.scoped(data, actor.values['capital'], actor)
            elif key.startswith('var:'):
                self.scoped(data, self.value(key[4:], actor), actor)
            elif key.startswith('event_target:'):
                self.scoped(data, self.value(key, actor), actor)
            elif key == 'for_each_scope_loop':
                fields = dict(data)
                for target in list(self.value(fields['array'], actor)):
                    self.scoped([(k, v) for k, v in data if k != 'array'], target, actor)
            elif key in ('owner', 'controller'):
                target = getattr(actor, key)
                if target is not None:
                    self.scoped(data, target, actor)
            elif key == 'every_owned_state':
                for state in self.states:
                    if state.owner is actor and self.condition(dict(data).get('limit', []), state):
                        self.scoped([(k, v) for k, v in data if k != 'limit'], state, actor)
            elif key.isdecimal():
                target = next((state for state in self.states if state.id == int(key)), None)
                if target is None:
                    raise AssertionError('Registered state missing from declared snapshot fixture: ' + key)
                self.scoped(data, target, actor)
            elif key in PARENT or key in EFFECTS:
                self.call(key, actor)
            else:
                super().run([(key, data)], actor)


class RegisteredReleaseSnapshotTests(unittest.TestCase):
    def test_full_dormant_membership_is_persistent_with_owner_controller_and_core_journal(self):
        rt = SnapshotRuntime()
        rt.call(PREPARE)
        self.assertIn(PREFIX + 'snapshot_ready', rt.owner.flags)
        self.assertEqual([s.id for s in rt.owner.values[PREFIX + 'transfer_states']], [120, 121, 133, 136, 933])
        self.assertEqual(rt.owner.values[PREFIX + 'previous_owners'], [rt.source] * 5)
        self.assertEqual(rt.owner.values[PREFIX + 'previous_controllers'], [rt.source] * 4 + [rt.other])
        self.assertEqual([s.id for s in rt.owner.values[PREFIX + 'source_core_states']], [120, 121, 133, 136])
        self.assertEqual(rt.temp, {})
        self.assertEqual(rt.arrays, {})

    def test_borrowed_source_input_preserves_presence_and_zero(self):
        for original in (None, Decimal(0), Decimal(999)):
            with self.subTest(original=original):
                rt = SnapshotRuntime()
                name = 'independence_wave_event021_adapter_package_id'
                rt.source.values.pop(name)
                if original is not None:
                    rt.source.values[name] = original
                rt.call(PREPARE)
                self.assertEqual(name in rt.source.values, original is not None)
                if original is not None:
                    self.assertEqual(rt.source.values[name], original)

    def test_noncore_authorized_anchor_is_in_union_once(self):
        rt = SnapshotRuntime()
        extra = State(234, rt.source, rt.source, {rt.source})
        rt.states.append(extra)
        rt.owner.values['random_civil_war_event6_anchor_state'] = extra
        rt.owner.values[PREFIX + 'authorized_states'] = [extra, extra]
        rt.call(PREPARE)
        self.assertEqual([s.id for s in rt.owner.values[PREFIX + 'transfer_states']], [120, 121, 133, 136, 933, 234])

    def test_missing_controller_or_foreign_authorized_owner_never_publishes_ready(self):
        for change in ('controller', 'owner'):
            with self.subTest(change=change):
                rt = SnapshotRuntime()
                if change == 'controller':
                    rt.states[0].controller = None
                else:
                    foreign = State(777, rt.other, rt.other, set())
                    rt.states.append(foreign)
                    rt.owner.values[PREFIX + 'authorized_states'] = [foreign]
                rt.call(PREPARE)
                self.assertNotIn(PREFIX + 'snapshot_ready', rt.owner.flags)

    def test_existing_mutation_journal_is_not_overwritten(self):
        rt = SnapshotRuntime()
        rt.owner.flags.add(PREFIX + 'mutation_active')
        rt.owner.values[PREFIX + 'transfer_states'] = [rt.states[-1]]
        before = dict(rt.owner.values)
        rt.call(PREPARE)
        self.assertEqual(rt.owner.values, before)

    def test_living_dynamic_package_keeps_baseline_and_uses_registered_increment(self):
        rt = SnapshotRuntime()
        package = next(package for package, tag in rt.packages if tag == 'AFX')
        actor = Country('D01', 501, True, {'independence_wave_package_id': package, 'army_experience': Decimal(77)}, original_tag='AFX')
        actor.flags = set()
        rt.world.append(actor)
        increment = State(34, rt.source, rt.source, {rt.source, rt.tags['AFX']})
        baseline = State(900, actor, actor, {actor})
        rt.states.extend((increment, baseline))
        rt.owner.values.update(random_civil_war_event6_package_id=package, random_civil_war_event6_anchor_state=increment)
        before = dict(actor.values)
        rt.call(PREPARE)
        self.assertIn(PREFIX + 'snapshot_ready', rt.owner.flags)
        self.assertEqual(rt.owner.values[PREFIX + 'transfer_states'], [increment])
        self.assertEqual(rt.owner.values[PREFIX + 'recipient_baseline_states'], [baseline])
        self.assertEqual(rt.owner.values[PREFIX + 'recipient_core_states'], [])
        self.assertEqual(actor.values, before)
        self.assertFalse(rt.tags['AFX'].exists)


class RegisteredReleaseTerritoryTests(unittest.TestCase):
    def fixture(self):
        rt = SnapshotRuntime()
        # A held mainland chain plus a disconnected island remains a full debit.
        rt.states[-1].controller = rt.source
        retained = [State(i, rt.source, rt.source, {rt.source}) for i in (126, 127)]
        rt.states.extend(retained)
        for state in rt.states:
            state.flags = set()
            state.neighbors = []
            state.values = {'building_level@industrial_complex': Decimal(1),
                            'building_level@arms_factory': Decimal(0), 'building_level@dockyard': Decimal(0),
                            'state_population_k': Decimal(1000), 'supply_node': Decimal(0), 'infrastructure': Decimal(1)}
        chain = retained + rt.states[:4]
        for first, second in zip(chain, chain[1:]):
            first.neighbors.append(second)
            second.neighbors.append(first)
        rt.source.values['capital'] = retained[0]
        rt.globals.update(random_civil_war_reserved_states=[], random_civil_war_scenario_reserved_states=[])
        rt.arrays['event021_parent_dynamic_optional_front_selected_states'] = []
        rt.call(PREPARE)
        return rt

    def validate(self, rt):
        rt.call('event021_parent_validate_registered_release_territory')
        self.assertTrue(all('event021_release_remnant_reach' not in state.flags for state in rt.states))
        self.assertNotIn('event021_release_remnant_exclusion_active', rt.owner.flags)
        return PREFIX + 'territory_ready' in rt.owner.flags

    def test_complete_mainland_and_island_debit_keeps_supplied_industrial_remnant(self):
        self.assertTrue(self.validate(self.fixture()))

    def test_nonanchor_capital_overlap_and_occupied_core_are_rejected_without_trimming(self):
        for change in ('capital', 'occupation', 'reservation'):
            with self.subTest(change=change):
                rt = self.fixture()
                before = list(rt.owner.values[PREFIX + 'transfer_states'])
                if change == 'capital':
                    rt.source.values['capital'] = rt.states[2]
                elif change == 'occupation':
                    rt.states[2].controller = rt.other
                else:
                    rt.globals['random_civil_war_reserved_states'].append(rt.states[2])
                self.assertFalse(self.validate(rt))
                self.assertEqual(rt.owner.values[PREFIX + 'transfer_states'], before)

    def test_remnant_industry_loss_is_not_counted_from_departing_homeland(self):
        rt = self.fixture()
        for state in rt.states[-2:]:
            state.values['building_level@industrial_complex'] = Decimal(0)
        self.assertFalse(self.validate(rt))


if __name__ == '__main__':
    unittest.main()
