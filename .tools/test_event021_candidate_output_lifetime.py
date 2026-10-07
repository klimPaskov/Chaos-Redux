"""Execute candidate helpers with conservative temporary call-frame cleanup.

The candidate bodies and route/goal mappers come from repository source.
State adjacency, eligibility, anchor scores, free tags and admitted Event 006
packages are explicit fixtures, not HOI4 behavior or balance evidence.
New temporary scalar AND array storage is discarded at every helper return.
Normal country/global state and chain-local scope targets remain separate.
CHAOSX_EVENT021_TEST_REVISION selects a read-only Git baseline via the shared
source loader. No files, logs, game process or Git state are written.
"""
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP
import operator
import unittest

from test_event021_evolution_log import Country, load


PATH = 'common/scripted_effects/021_random_civil_war_dynamic_front_candidate_effects.txt'
CANDIDATES = dict(load(PATH))
PARENT = dict(load('common/scripted_effects/021_random_civil_war_parent_effects.txt'))
CONSTANTS = dict(load('common/script_constants/021_random_civil_war_constants.txt'))
PREFIX = 'event021_parent_dynamic_optional_front_'
ALIGNED = tuple(PREFIX + name for name in (
    'archetypes', 'routes', 'anchors', 'sources', 'actor_scopes', 'actor_types',
    'relationships', 'goals', 'packages', 'package_regions', 'package_depths',
    'package_archetypes', 'state_weights', 'state_counts', 'state_offsets',
    'selected_routes', 'selected_states'))
SCRATCH = tuple(data for key, data in
                CANDIDATES['event021_parent_reset_dynamic_optional_front_candidates']
                if key == 'clear_temp_array')
MAPPERS = ('event021_parent_set_planned_route_source',
           'event021_parent_set_planned_front_goal')


@dataclass(eq=False)
class State:
    id: int
    score: Decimal
    neighbors: list = field(default_factory=list)
    flags: set = field(default_factory=set)
    values: dict = field(default_factory=dict)


class CandidateRuntime:
    def __init__(self):
        self.host = Country(1, values={'random_civil_war_archetype': Decimal(1),
                                      'random_civil_war_belligerent_cap': Decimal(4),
                                      'random_civil_war_requested_force_divisions': Decimal(6)})
        self.carrier = Country(2)
        self.states = [State(i, Decimal(100 - i * 10)) for i in range(1, 5)]
        for first, second in zip(self.states, self.states[1:]):
            first.neighbors.append(second)
            second.neighbors.append(first)
        self.temporary = {}
        self.temp_arrays = {}
        self.globals = {'random_civil_war_max_active_fronts': Decimal(20),
                        'random_civil_war_active_front_count': Decimal(2),
                        'random_civil_war_pending_opposition_front_id': Decimal(12),
                        'random_civil_war_pending_host_front_id': Decimal(11),
                        'random_civil_war_plan_states': self.states,
                        'random_civil_war_scenario_reserved_states': [],
                        'independence_wave_event021_complete_package_ids': []}
        self.global_flags = set()
        primary = State(0, Decimal(0))
        self.targets = {'random_civil_war_dynamic_candidate_host': self.host,
                        'random_civil_war_dynamic_primary_anchor': primary,
                        'random_civil_war_global_anchor_state': primary}
        self.packages = []
        self.calls = []
        self.predicates = {
            'event021_parent_multifront_setup_available': True,
            'event021_parent_secondary_state_candidate': True,
            'event021_parent_dynamic_region_state_candidate': True,
            'random_civil_war_regional_route_valid': True,
            'random_civil_war_command_route_valid': True,
            'random_civil_war_legal_route_valid': False,
            'random_civil_war_ideological_route_valid': False,
        }

    def constant(self, group, key):
        return Decimal(dict(CONSTANTS[group])[key])

    def own_outputs(self):
        self.temp_arrays.update({name: [] for name in ALIGNED})
        self.temporary.update(event021_parent_dynamic_optional_front_valid=Decimal(0),
                              event021_parent_dynamic_optional_front_count=Decimal(0))

    def value(self, token, actor):
        if token == 'THIS':
            return actor
        if token.startswith('event_target:'):
            return self.targets[token[13:]]
        if token.startswith('constant:'):
            return self.constant(*token[9:].split('.', 1))
        if '^' in token:
            name, index = token.split('^', 1)
            rows = self.value(name, actor)
            if rows == 0:
                rows = []
            return Decimal(len(rows)) if index == 'num' else rows[int(self.value(index, actor))]
        if token.startswith('global.'):
            return self.globals.get(token[7:], Decimal(0))
        if token in self.temporary:
            return self.temporary[token]
        if token in self.temp_arrays:
            return self.temp_arrays[token]
        try:
            return Decimal(token)
        except Exception:
            return actor.values.get(token, Decimal(0))

    def condition(self, nodes, actor):
        comparisons = {'equals': operator.eq, 'less_than': operator.lt,
                       'less_than_or_equals': operator.le, 'greater_than': operator.gt,
                       'greater_than_or_equals': operator.ge}
        for key, data in nodes:
            if key in ('OR', 'AND', 'NOT'):
                results = [self.condition([node], actor) for node in data]
                result = any(results) if key == 'OR' else (all(results) if key == 'AND' else not any(results))
            elif key == 'check_variable':
                fields = dict(data)
                result = comparisons[fields['compare']](self.value(fields['var'], actor),
                                                        self.value(fields['value'], actor))
            elif key == 'has_variable':
                result = data[7:] in self.globals if data.startswith('global.') else data in actor.values or data in self.temporary
            elif key == 'has_global_flag':
                result = data in self.global_flags
            elif key in ('has_country_flag', 'has_state_flag'):
                result = data in actor.flags
            elif key == 'has_event_target':
                result = data in self.targets
            elif key == 'is_in_array':
                fields = dict(data)
                result = self.value(fields['value'], actor) in (self.value(fields['array'], actor) or [])
            elif key == 'state':
                result = actor is self.value(data, actor)
            elif key == 'any_neighbor_state':
                result = any(self.condition(data, neighbor) for neighbor in actor.neighbors)
            elif key in self.predicates:
                result = self.predicates[key]
            else:
                raise AssertionError(f'Unmodelled candidate predicate: {key}')
            if not result:
                return False
        return True

    def call(self, name, actor):
        scalars, arrays = set(self.temporary), set(self.temp_arrays)
        self.calls.append((name, scalars, arrays))
        if name in CANDIDATES:
            self.run(CANDIDATES[name], actor)
        elif name in MAPPERS:
            self.run(PARENT[name], actor)
        elif name == 'event021_parent_score_anchor_state':
            self.temporary['event021_anchor_state_score'] = actor.score
        elif name == 'event021_count_free_dynamic_tags':
            self.temporary['event021_dynamic_tag_free'] = Decimal(10)
        elif name == 'event021_parent_find_event6_package':
            self.temporary['event021_parent_event6_package_found'] = Decimal(bool(self.packages))
            if self.packages:
                package_id, anchor = self.packages.pop(0)
                actor.values.update(random_civil_war_event6_package_id=Decimal(package_id),
                                    random_civil_war_event6_candidate_region=Decimal(3),
                                    random_civil_war_event6_candidate_depth=Decimal(1),
                                    random_civil_war_event6_candidate_archetype=Decimal(2))
                self.targets.update(random_civil_war_event6_selected_anchor=anchor,
                                    random_civil_war_event6_selected_actor=self.carrier)
        elif name in ('event021_parent_save_event6_host_identity',
                      'event021_parent_restore_event6_host_identity',
                      'event021_parent_clear_event6_package_transaction'):
            # Fixture boundary: package admission/identity transactions are not
            # executed or certified here. They must not produce candidate rows.
            pass
        else:
            raise AssertionError(f'Unmodelled candidate helper: {name}')
        self.temporary = {k: v for k, v in self.temporary.items() if k in scalars}
        self.temp_arrays = {k: v for k, v in self.temp_arrays.items() if k in arrays}

    def run(self, nodes, actor):
        branch_taken = False
        for key, data in nodes:
            if key in ('if', 'else_if', 'else'):
                fields = dict(data)
                if key == 'if':
                    branch_taken = False
                take = not branch_taken and (key == 'else' or self.condition(fields['limit'], actor))
                if take:
                    self.run([(k, v) for k, v in data if k != 'limit'], actor)
                    branch_taken = True
            elif key in ('set_temp_variable', 'add_to_temp_variable', 'subtract_from_temp_variable',
                         'multiply_temp_variable', 'divide_temp_variable'):
                name, token = data[0]
                number = self.value(token, actor)
                current = self.temporary.get(name, Decimal(0))
                operations = {'set_temp_variable': lambda: number, 'add_to_temp_variable': lambda: current + number,
                              'subtract_from_temp_variable': lambda: current - number,
                              'multiply_temp_variable': lambda: current * number,
                              'divide_temp_variable': lambda: current / number}
                self.temporary[name] = operations[key]()
            elif key == 'round_temp_variable':
                self.temporary[data] = self.temporary[data].quantize(Decimal(1), rounding=ROUND_HALF_UP)
            elif key == 'clear_temp_array':
                self.temp_arrays[data] = []
            elif key == 'add_to_temp_array':
                fields = dict(data)
                self.temp_arrays.setdefault(fields['array'], []).append(self.value(fields.get('value', 'THIS'), actor))
            elif key in ('for_each_loop', 'for_each_scope_loop'):
                fields = dict(data)
                body = [(k, v) for k, v in data if k not in ('array', 'value', 'index', 'break')]
                for index, row in enumerate(list(self.value(fields['array'], actor) or [])):
                    if key == 'for_each_loop':
                        self.temporary[fields['value']] = row
                        if 'index' in fields:
                            self.temporary[fields['index']] = Decimal(index)
                    self.run(body, row if key == 'for_each_scope_loop' else actor)
                    if self.temporary.get(fields.get('break', ''), Decimal(0)):
                        break
            elif key == 'find_highest_in_array':
                fields = dict(data)
                rows = self.value(fields['array'], actor)
                index = max(range(len(rows)), key=rows.__getitem__)
                self.temporary[fields['value']] = rows[index]
                self.temporary[fields['index']] = Decimal(index)
            elif key == 'save_event_target_as':
                self.targets[data] = actor
            elif key.startswith('event_target:'):
                self.run(data, self.targets[key[13:]])
            elif key.startswith('var:'):
                self.run(data, self.value(key[4:], actor))
            elif key == 'clr_state_flag':
                actor.flags.discard(data)
            elif key == 'set_global_flag':
                self.global_flags.add(data)
            elif key == 'clr_global_flag':
                self.global_flags.discard(data)
            elif key.startswith('event021_'):
                self.call(key, actor)
            else:
                raise AssertionError(f'Unmodelled candidate effect: {key}')


class CandidateOutputLifetimeTests(unittest.TestCase):
    def test_ordinary_route_goal_metadata_survives_mapper_returns(self):
        expected = {'regional': ('regional', 'regional_recognition'),
                    'command': ('command', 'command_seizure'),
                    'legal': ('legal', 'constitutional_restoration'),
                    'ideological': ('political', 'ideological_change')}
        for archetype, (route, goal) in expected.items():
            with self.subTest(archetype=archetype):
                rt = CandidateRuntime()
                rt.own_outputs()
                rt.temp_arrays['event021_parent_dynamic_candidate_region_states'] = rt.states[:2]
                rt.temporary.update(event021_dynamic_candidate_archetype=rt.constant('random_civil_war_archetype', archetype),
                                    event021_dynamic_candidate_region_weight=Decimal(170))
                rt.call('event021_parent_append_dynamic_ordinary_front_candidate', rt.states[0])
                self.assertEqual(rt.temp_arrays[PREFIX + 'routes'], [rt.constant('random_civil_war_evidence_source', route)])
                self.assertEqual(rt.temp_arrays[PREFIX + 'goals'], [rt.constant('random_civil_war_front_goal', goal)])
                self.assertEqual(rt.temp_arrays[PREFIX + 'archetypes'], [rt.constant('random_civil_war_archetype', archetype)])
                self.assertEqual(rt.temp_arrays[PREFIX + 'actor_types'], [rt.constant('random_civil_war_planned_actor_type', 'ordinary_claimant')])
                self.assertEqual(rt.temp_arrays[PREFIX + 'sources'], [12])
                self.assertEqual(rt.temp_arrays[PREFIX + 'actor_scopes'], [rt.host])
                self.assertEqual(rt.temp_arrays[PREFIX + 'packages'], [0])
                self.assertEqual(rt.temp_arrays[PREFIX + 'state_counts'], [2])
                self.assertEqual(rt.temp_arrays[PREFIX + 'selected_states'], rt.states[:2])
                self.assertNotIn('event021_planned_front_route', rt.temporary)

    def test_opening_collector_forwards_two_complete_rows_through_all_calls(self):
        rt = CandidateRuntime()
        rt.own_outputs()
        rt.temporary['unrelated_cursor'] = Decimal(777)
        rt.call('event021_parent_collect_dynamic_optional_front_candidates', rt.host)
        self.assertEqual(rt.temporary['event021_parent_dynamic_optional_front_count'], 2)
        self.assertEqual(rt.temporary['event021_parent_dynamic_optional_front_valid'], 1)
        self.assertEqual(rt.temp_arrays[PREFIX + 'state_counts'], [2, 2])
        self.assertEqual(rt.temp_arrays[PREFIX + 'state_offsets'], [0, 2])
        self.assertEqual(rt.temp_arrays[PREFIX + 'state_weights'], [170, 130])
        self.assertEqual(rt.temp_arrays[PREFIX + 'selected_states'], rt.states)
        for name in ALIGNED[:-1]:
            self.assertEqual(len(rt.temp_arrays[name]), 2, name)
        self.assertEqual(rt.temporary['unrelated_cursor'], 777)
        reset_call = next(call for call in rt.calls if call[0] == 'event021_parent_reset_dynamic_optional_front_candidates')
        self.assertEqual(len(SCRATCH), 27)
        self.assertTrue(set(SCRATCH) <= reset_call[2])
        for name, scalars, arrays in rt.calls:
            if name == 'event021_parent_score_anchor_state':
                self.assertIn('event021_anchor_state_score', scalars)
            if name == 'event021_parent_append_dynamic_ordinary_front_candidate':
                self.assertTrue(set(ALIGNED) <= arrays)
        self.assertEqual(set(rt.temp_arrays), set(ALIGNED))

    def test_active_grower_spends_returned_span_count_without_resetting_prior_rows(self):
        rt = CandidateRuntime()
        rt.own_outputs()
        rt.temporary.update(event021_dynamic_candidate_archetype=rt.constant('random_civil_war_archetype', 'regional'),
                            event021_dynamic_candidate_region_weight=Decimal(15))
        rt.temp_arrays['event021_parent_dynamic_candidate_region_states'] = [rt.states[3]]
        rt.call('event021_parent_append_dynamic_ordinary_front_candidate', rt.states[3])
        rt.temp_arrays.update(event021_parent_dynamic_optional_source_states=rt.states[:2],
                              event021_parent_dynamic_route_types=[rt.constant('random_civil_war_archetype', 'command')],
                              event021_parent_dynamic_anchor_state_pool=rt.states[:2],
                              event021_parent_dynamic_anchor_score_pool=[state.score for state in rt.states[:2]])
        rt.temporary.update(event021_parent_dynamic_active_mode=Decimal(1),
                            event021_parent_dynamic_region_state_budget=Decimal(1),
                            event021_parent_dynamic_optional_front_count=Decimal(1),
                            event021_parent_dynamic_ordinary_front_count=Decimal(1),
                            event021_parent_dynamic_optional_front_capacity=Decimal(3),
                            event021_parent_dynamic_ordinary_front_capacity=Decimal(3))
        rt.call('event021_parent_grow_dynamic_ordinary_front_regions', rt.host)
        self.assertEqual(rt.temporary['event021_parent_dynamic_region_state_budget'], 0)
        self.assertEqual(rt.temporary['event021_parent_dynamic_optional_front_count'], 2)
        self.assertEqual(rt.temp_arrays[PREFIX + 'selected_states'], [rt.states[3], rt.states[0]])
        self.assertEqual(rt.temp_arrays[PREFIX + 'state_offsets'], [0, 1])

    def test_event6_package_loop_preserves_metadata_and_scorer_outputs(self):
        rt = CandidateRuntime()
        rt.own_outputs()
        anchors = [State(90, Decimal(37)), State(91, Decimal(41))]
        rt.packages = list(zip((101, 102), anchors))
        rt.globals['independence_wave_event021_complete_package_ids'] = [101, 102]
        rt.temporary.update(event021_parent_event6_package_count=Decimal(2),
                            event021_parent_dynamic_optional_front_capacity=Decimal(2))
        rt.call('event021_parent_collect_dynamic_event6_front_candidates', rt.host)
        self.assertEqual(rt.temporary['event021_parent_dynamic_optional_front_count'], 2)
        self.assertEqual(rt.temp_arrays[PREFIX + 'packages'], [101, 102])
        self.assertEqual(rt.temp_arrays[PREFIX + 'package_regions'], [3, 3])
        self.assertEqual(rt.temp_arrays[PREFIX + 'package_depths'], [1, 1])
        self.assertEqual(rt.temp_arrays[PREFIX + 'package_archetypes'], [2, 2])
        self.assertEqual(rt.temp_arrays[PREFIX + 'sources'], [11, 11])
        self.assertEqual(rt.temp_arrays[PREFIX + 'routes'], [rt.constant('random_civil_war_evidence_source', 'event006')] * 2)
        self.assertEqual(rt.temp_arrays[PREFIX + 'goals'], [rt.constant('random_civil_war_front_goal', 'independence')] * 2)
        self.assertEqual(rt.temp_arrays[PREFIX + 'state_weights'], [37, 41])
        self.assertEqual(rt.temp_arrays[PREFIX + 'actor_scopes'], [rt.carrier, rt.carrier])
        self.assertEqual(rt.temp_arrays[PREFIX + 'state_offsets'], [0, 1])
        self.assertEqual(rt.temp_arrays[PREFIX + 'selected_states'], anchors)
        for name in ALIGNED[:-1]:
            self.assertEqual(len(rt.temp_arrays[name]), 2, name)
        for name, scalars, arrays in rt.calls:
            if name == 'event021_parent_score_anchor_state':
                self.assertIn('event021_anchor_state_score', scalars)
            if name == 'event021_parent_append_dynamic_event6_front_candidate':
                self.assertTrue(set(ALIGNED) <= arrays)

    def test_unowned_outer_outputs_are_discarded_instead_of_certified(self):
        rt = CandidateRuntime()
        rt.call('event021_parent_collect_dynamic_optional_front_candidates', rt.host)
        self.assertEqual(rt.temporary, {})
        self.assertEqual(rt.temp_arrays, {})


if __name__ == '__main__':
    unittest.main()
