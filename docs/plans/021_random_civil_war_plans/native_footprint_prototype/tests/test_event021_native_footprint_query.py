"""Execute real blueprint/native-footprint query bodies on declared maps.

Country objects exist independently of map existence in this fixture, and
owner/controller/core relationships are declared inputs, not engine evidence.
This does not execute release, resource allocation, birth or rollback.
"""
from dataclasses import dataclass, field
from decimal import Decimal
import operator
import unittest

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), *['..']*5, '.tools'))
from test_event021_evolution_log import load


EFFECTS = dict(load('docs/plans/021_random_civil_war_plans/native_footprint_prototype/script/006_independence_wave_event021_footprint_effects.txt'))
REGISTRY = dict(load('common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt'))
CONSTANTS = dict(load('common/script_constants/006_independence_wave_constants_registry.txt'))
CONSTANTS.update(dict(load('docs/plans/021_random_civil_war_plans/native_footprint_prototype/script/006_independence_wave_event021_footprint_constants.txt')))
CONSTANTS.update(dict(load('common/script_constants/021_random_civil_war_constants.txt')))
QUERY = 'independence_wave_query_event021_carrier_blueprint'
COLLECT = 'independence_wave_collect_event021_native_footprint'


@dataclass(eq=False)
class Country:
    tag: str
    id: int
    exists: bool = False
    values: dict = field(default_factory=dict)
    original_tag: str = ''
    nonhuman: bool = False


@dataclass(eq=False)
class State:
    id: int
    owner: Country
    controller: Country
    cores: set = field(default_factory=set)


class Runtime:
    def __init__(self):
        self.source = Country('ENG', 1, True)
        self.other = Country('FRA', 2, True)
        self.root = Country('CXT', 99, True)  # Deliberately not the donating source.
        self.tags = {}
        self.packages = []
        for index, (key, body) in enumerate(REGISTRY['independence_wave_release_event021_adapter_actor']):
            if key == 'if':
                token = next(value[0][1] for name, value in dict(body)['limit'] if name == 'check_variable')
                tag = dict(body)['release']
                self.tags[tag] = Country(tag, 100 + index)
                self.packages.append((self.value(token, self.source), tag))
        self.source.values['independence_wave_event021_adapter_package_id'] = self.packages[0][0]
        self.flags = {'independence_wave_event021_adapter_registry_initialized'}
        self.globals = {'independence_wave_event021_complete_package_ids': [value for value, _ in self.packages]}
        self.targets = {}
        self.temp = {}
        self.arrays = {}
        self.states = []
        self.world = [self.source, self.other, self.root] + list(self.tags.values())

    def own_outputs(self):
        self.temp.update({name: Decimal(0) for name in (
            'event021_release_query_status', 'event021_release_carrier_id', 'event021_release_queried_package_id',
            'event021_release_native_status', 'event021_release_native_count',
            'event021_release_live_status', 'event021_release_live_count')})
        self.arrays.update({name: [] for name in (
            'event021_release_native_states', 'event021_release_prior_controllers', 'event021_release_source_core_states',
            'event021_release_live_matches', 'event021_release_live_identity_statuses')})

    def value(self, token, actor):
        if token == 'THIS':
            return actor
        if token == 'id':
            return Decimal(actor.id)
        if token.startswith('constant:'):
            group, name = token[9:].split('.', 1)
            return Decimal(dict(CONSTANTS[group])[name])
        if token.startswith('event_target:'):
            return self.targets[token[13:]]
        if '^' in token:
            name, index = token.split('^', 1)
            values = self.value(name, actor)
            return Decimal(len(values)) if index == 'num' else values[int(self.value(index, actor))]
        if token.startswith('global.'):
            return self.globals[token[7:]]
        if token in self.temp:
            return self.temp[token]
        if token in self.arrays:
            return self.arrays[token]
        if token in getattr(actor, 'values', {}):
            return actor.values[token]
        return Decimal(token)

    def condition(self, nodes, actor):
        for key, data in nodes:
            if key == 'exists':
                result = actor.exists == (data == 'yes')
            elif key == 'has_variable':
                result = data in actor.values or data in self.temp
            elif key == 'has_global_flag':
                result = data in self.flags
            elif key == 'has_event_target':
                result = data in self.targets
            elif key == 'is_in_array':
                fields = dict(data)
                result = self.value(fields['value'], actor) in self.value(fields['array'], actor)
            elif key == 'check_variable':
                fields = dict(data)
                result = {'equals': operator.eq}[fields['compare']](self.value(fields['var'], actor), self.value(fields['value'], actor))
            elif key == 'is_core_of':
                result = self.value(data, actor) in actor.cores
            elif key == 'is_actual_nonhuman_country':
                result = actor.nonhuman == (data == 'yes')
            elif key.startswith('event_target:'):
                result = self.condition(data, self.value(key, actor))
            elif key == 'OR':
                result = any(self.condition([node], actor) for node in data)
            elif key == 'NOT':
                result = not any(self.condition([node], actor) for node in data)
            else:
                raise AssertionError('Unmodelled query predicate ' + key)
            if not result:
                return False
        return True

    def call(self, name, actor=None):
        scalars, arrays = set(self.temp), set(self.arrays)
        self.run(EFFECTS[name], actor or self.source)
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
            elif key == 'set_temp_variable':
                name, token = data[0]
                self.temp[name] = self.value(token, actor)
            elif key == 'clear_temp_array':
                self.arrays[data] = []
            elif key == 'add_to_temp_array':
                fields = dict(data)
                self.arrays[fields['array']].append(self.value(fields['value'], actor))
            elif key == 'save_event_target_as':
                self.targets[data] = actor
            elif key in self.tags:
                self.run(data, self.tags[key])
            elif key.startswith('event_target:'):
                self.run(data, self.value(key, actor))
            elif key == 'every_owned_state':
                for state in self.states:
                    if state.owner is actor and self.condition(dict(data)['limit'], state):
                        self.run([(k, v) for k, v in data if k != 'limit'], state)
            elif key == 'controller':
                if actor.controller is not None:
                    self.run(data, actor.controller)
            elif key == 'every_country_with_original_tag':
                fields = dict(data)
                for country in self.world:
                    if (country.original_tag or country.tag) == fields['original_tag_to_check'] and self.condition(fields['limit'], country):
                        self.run([(k, v) for k, v in data if k not in ('original_tag_to_check', 'limit')], country)
            elif key.startswith('var:'):
                self.run(data, self.value(key[4:], actor))
            elif key in EFFECTS and data == 'yes':
                self.call(key, actor)
            else:
                raise AssertionError('Unmodelled query effect ' + key)


class NativeFootprintQueryTests(unittest.TestCase):
    def test_every_registered_static_carrier_resolves_while_dormant(self):
        rt = Runtime()
        rt.own_outputs()
        self.assertEqual(len(rt.packages), 32)
        for package, tag in rt.packages:
            with self.subTest(tag=tag):
                rt.source.values['independence_wave_event021_adapter_package_id'] = package
                rt.call(QUERY)
                self.assertIs(rt.targets['event021_release_carrier_blueprint'], rt.tags[tag])
                self.assertFalse(rt.tags[tag].exists)
                self.assertEqual(rt.temp['event021_release_carrier_id'], rt.tags[tag].id)
                self.assertEqual(rt.temp['event021_release_query_status'], 1)

    def test_complete_core_footprint_keeps_occupied_state_and_source_core_subset(self):
        rt = Runtime()
        rt.own_outputs()
        carrier = rt.tags['SCO']
        rt.states = [State(i, rt.source, rt.source, {carrier, rt.source}) for i in (120, 121, 133, 136)]
        rt.states.append(State(933, rt.source, rt.other, {carrier}))
        rt.states.append(State(126, rt.source, rt.source, {rt.source}))
        rt.states.append(State(999, rt.other, rt.other, {carrier}))
        before = [(state.owner, state.controller, set(state.cores)) for state in rt.states]
        rt.call(QUERY)
        rt.call(COLLECT)
        self.assertEqual([state.id for state in rt.arrays['event021_release_native_states']], [120, 121, 133, 136, 933])
        self.assertEqual(rt.arrays['event021_release_prior_controllers'], [rt.source] * 4 + [rt.other])
        self.assertEqual([state.id for state in rt.arrays['event021_release_source_core_states']], [120, 121, 133, 136])
        self.assertEqual(rt.temp['event021_release_native_count'], 5)
        self.assertEqual(rt.temp['event021_release_native_status'], 1)
        self.assertEqual(before, [(state.owner, state.controller, set(state.cores)) for state in rt.states])

    def test_live_static_carrier_has_no_native_release_debit(self):
        rt = Runtime()
        rt.own_outputs()
        rt.tags['SCO'].exists = True
        rt.states = [State(121, rt.source, rt.source, {rt.tags['SCO']})]
        rt.call(QUERY)
        rt.call(COLLECT)
        self.assertEqual(rt.temp['event021_release_native_count'], 0)
        self.assertEqual(rt.temp['event021_release_native_status'], 1)

    def test_fresh_world_cores_are_not_trimmed_to_an_anchor_or_package_csv(self):
        rt = Runtime()
        rt.own_outputs()
        rt.states = [State(121, rt.source, rt.source, {rt.tags['SCO']})]
        rt.call(QUERY)
        rt.call(COLLECT)
        rt.states.append(State(235, rt.source, rt.other, {rt.tags['SCO'], rt.source}))
        rt.call(COLLECT)
        self.assertEqual([state.id for state in rt.arrays['event021_release_native_states']], [121, 235])
        self.assertEqual(rt.temp['event021_release_native_count'], 2)

    def test_stale_target_missing_input_and_identity_change_fail_closed(self):
        rt = Runtime()
        rt.own_outputs()
        rt.call(QUERY)
        rt.source.values['independence_wave_event021_adapter_package_id'] = rt.packages[1][0]
        rt.call(COLLECT)
        self.assertEqual(rt.temp['event021_release_native_status'], 5)
        rt.source.values['independence_wave_event021_adapter_package_id'] = Decimal(999999)
        rt.call(QUERY)
        self.assertEqual(rt.temp['event021_release_query_status'], 2)
        rt.call(COLLECT)
        self.assertEqual(rt.arrays['event021_release_native_states'], [])
        del rt.source.values['independence_wave_event021_adapter_package_id']
        rt.call(QUERY)
        self.assertEqual(rt.temp['event021_release_query_status'], 0)

    def test_unowned_temporary_outputs_do_not_survive_helper_return(self):
        rt = Runtime()
        rt.call(QUERY)
        self.assertEqual(rt.temp, {})
        self.assertIn('event021_release_carrier_blueprint', rt.targets)

    def test_all_six_original_tag_dynamic_carriers_are_resolved_without_static_birth(self):
        for tag in ('AFX', 'AGX', 'AJX', 'ARX', 'ASX', 'HBX'):
            with self.subTest(tag=tag):
                rt = Runtime()
                rt.own_outputs()
                package = next(package for package, carrier in rt.packages if carrier == tag)
                rt.source.values['independence_wave_event021_adapter_package_id'] = package
                dynamic = Country('D01', 501, True, {'independence_wave_package_id': package}, original_tag=tag)
                rt.world.append(dynamic)
                rt.call(QUERY)
                rt.call('independence_wave_resolve_event021_live_carrier')
                self.assertEqual(rt.temp['event021_release_live_status'], 7)
                self.assertEqual(rt.temp['event021_release_live_count'], 1)
                self.assertIs(rt.targets['event021_release_live_carrier'], dynamic)
                self.assertFalse(rt.tags[tag].exists)

    def test_static_and_dynamic_living_identity_collision_is_not_hidden_by_precedence(self):
        rt = Runtime()
        rt.own_outputs()
        package = rt.packages[0][0]
        rt.tags['SCO'].exists = True
        rt.tags['SCO'].values['independence_wave_package_id'] = package
        rt.world.append(Country('D02', 502, True, {'independence_wave_package_id': package}, original_tag='SCO'))
        rt.call(QUERY)
        rt.call('independence_wave_resolve_event021_live_carrier')
        self.assertEqual(rt.temp['event021_release_live_status'], 8)
        self.assertEqual(rt.temp['event021_release_live_count'], 2)

    def test_unattested_or_nonhuman_living_identity_never_looks_dormant(self):
        for mode in ('missing_package', 'wrong_package', 'nonhuman'):
            with self.subTest(mode=mode):
                rt = Runtime()
                rt.own_outputs()
                package = rt.packages[0][0]
                actor = Country('D03', 503, True, original_tag='SCO')
                if mode != 'missing_package':
                    actor.values['independence_wave_package_id'] = package if mode == 'nonhuman' else Decimal(999)
                actor.nonhuman = mode == 'nonhuman'
                rt.world.append(actor)
                before = dict(actor.values)
                rt.call(QUERY)
                rt.call('independence_wave_resolve_event021_live_carrier')
                self.assertEqual(rt.temp['event021_release_live_status'], 9)
                self.assertEqual(rt.temp['event021_release_live_count'], 1)
                self.assertEqual(actor.values, before)


if __name__ == '__main__':
    unittest.main()
