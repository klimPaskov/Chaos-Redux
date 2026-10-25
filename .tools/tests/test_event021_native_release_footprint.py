"""Execute the Event 021 native release footprint helpers on declared fixtures.

The Event 006 crosswalk trigger and collector, the Event 021 footprint
effects and eligibility trigger, the candidate appender, and the opening-plan
validity trigger come from repository source. Ownership, cores, controllers
and the ledger arrays are explicit fixtures, not engine observations: native
`release` itself is modelled only as "the donor's owned cores move", the rule
the helpers rely on (installed effects documentation, `release`).
New temporary scalars and arrays are discarded at every effect return, so a
helper that relies on an undeclared output fails here. Nothing is written.
"""
from decimal import Decimal
import unittest

from test_event021_active_front_receipt import ACTIVE
from test_event021_active_remnant_lifetime import MapRuntime
from test_event021_evolution_log import load

SCRIPTED = {}
for path in (
        'common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt',
        'common/scripted_effects/021_random_civil_war_event6_footprint_effects.txt',
        'common/scripted_effects/021_random_civil_war_dynamic_front_candidate_effects.txt',
        'common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt',
        'common/scripted_triggers/021_random_civil_war_event6_footprint_triggers.txt',
        'common/scripted_triggers/021_random_civil_war_triggers.txt'):
    SCRIPTED.update(dict(load(path)))
CONSTANTS = dict(load('common/script_constants/021_random_civil_war_constants.txt'))
CONSTANTS.update(dict(load('common/script_constants/006_independence_wave_constants_registry.txt')))

ONE = 'constant:random_civil_war_value.one'
PACKAGE_SCO = 1
PACKAGE_WLS = 2
STUBBED_TRIGGERS = {'event021_external_queue_blocks_new_crisis': False,
                    'random_civil_war_parent_remnant_valid': True}


class Country:
    def __init__(self, tag, exists=True):
        self.tag, self.exists, self.values, self.flags = tag, exists, {}, set()

    def __repr__(self):
        return self.tag


class State:
    def __init__(self, ident, owner=None, controller=None, cores=(), capital=False):
        self.id, self.owner, self.controller = ident, owner, controller or owner
        self.cores, self.capital, self.flags = set(cores), capital, set()

    def __repr__(self):
        return f'S{self.id}'


class World:
    def __init__(self):
        self.donor, self.enemy = Country('GBR'), Country('GER')
        self.carriers = {'SCO': Country('SCO', exists=False), 'WLS': Country('WLS', exists=False)}
        self.states = []
        self.globals = {'random_civil_war_reserved_states': [], 'random_civil_war_front_states': [],
                        'random_civil_war_scenario_reserved_states': [], 'random_civil_war_plan_states': [],
                        'random_civil_war_plan_state_count': 0, 'random_civil_war_planned_front_state_entries': [],
                        'independence_wave_event021_complete_package_ids': [PACKAGE_SCO, PACKAGE_WLS]}
        self.global_flags, self.temp, self.temp_arrays, self.targets = set(), {}, {}, {}
        self.donor.values['random_civil_war_event6_package_id'] = PACKAGE_SCO

    def state(self, ident, owner='donor', **kw):
        owner = self.donor if owner == 'donor' else owner
        state = State(ident, owner, **kw)
        self.states.append(state)
        return state

    def owned(self, country):
        return [state for state in self.states if state.owner is country]

    # ---- value and condition evaluation -------------------------------
    def value(self, token, scope, chain):
        if token.startswith('constant:'):
            group, name = token[9:].split('.', 1)
            return int(dict(CONSTANTS[group])[name])
        if token.startswith('event_target:'):
            return self.targets[token[13:]]
        if token == 'THIS':
            return scope
        if token == 'PREV':
            return chain[-2]
        if token == 'num_owned_states':
            return len(self.owned(scope))
        if token.startswith('global.'):
            return self.globals.get(token[7:], 0)
        if '^' in token:
            name, index = token.split('^', 1)
            rows = self.value(name, scope, chain)
            return len(rows) if index == 'num' else rows[int(self.value(index, scope, chain))]
        if token in self.temp_arrays:
            return self.temp_arrays[token]
        if token in self.temp:
            return self.temp[token]
        try:
            return int(token)
        except ValueError:
            return getattr(scope, 'values', {}).get(token, 0)

    def condition(self, nodes, scope, chain):
        ops = {'equals': lambda a, b: a == b, 'greater_than': lambda a, b: a > b,
               'greater_than_or_equals': lambda a, b: a >= b}
        for key, data in nodes:
            if key == 'limit':
                continue
            if key in ('AND', 'OR', 'NOT', 'hidden_trigger'):
                # hidden_trigger only hides its tooltip; it is evaluated like AND.
                parts = (self.condition([node], scope, chain) for node in data)
                result = {'AND': all, 'hidden_trigger': all, 'OR': any}.get(key, lambda p: not any(p))(parts)
            elif key == 'check_variable':
                f = dict(data)
                result = ops[f['compare']](self.value(f['var'], scope, chain), self.value(f['value'], scope, chain))
            elif key == 'has_variable':
                result = data in getattr(scope, 'values', {}) or data in self.temp
            elif key == 'has_event_target':
                result = data in self.targets
            elif key == 'has_country_flag':
                result = data in scope.flags
            elif key == 'has_global_flag':
                result = data in self.global_flags
            elif key == 'state':
                result = scope is self.value(data, scope, chain)
            elif key == 'is_in_array':
                f = dict(data)
                array = f['array']
                rows = self.globals.get(array[7:], []) if array.startswith('global.') else (
                    self.temp_arrays.get(array) or getattr(scope, 'values', {}).get(array, []))
                result = self.value(f['value'], scope, chain) in rows
            elif key == 'is_owned_by':
                result = scope.owner is self.value(data, scope, chain)
            elif key == 'is_controlled_by':
                result = scope.controller is self.value(data, scope, chain)
            elif key == 'is_capital':
                result = scope.capital == (data == 'yes')
            elif key == 'country_exists':
                result = data in self.carriers and self.carriers[data].exists
            elif key == 'is_core_of':
                result = data in scope.cores
            elif key.startswith('event_target:'):
                target = self.targets[key[13:]]
                result = self.condition(data, target, chain + [target])
            elif key in STUBBED_TRIGGERS:
                result = STUBBED_TRIGGERS[key]
            elif key in SCRIPTED and data == 'yes':
                result = self.condition(SCRIPTED[key], scope, chain)
            else:
                raise AssertionError(f'Unmodelled condition: {key}')
            if not result:
                return False
        return True

    # ---- effect execution ---------------------------------------------
    def call(self, name, scope):
        scalars, arrays = set(self.temp), set(self.temp_arrays)
        self.run(SCRIPTED[name], scope, [scope])
        self.temp = {k: v for k, v in self.temp.items() if k in scalars}
        self.temp_arrays = {k: v for k, v in self.temp_arrays.items() if k in arrays}

    def run(self, nodes, scope, chain):
        taken = False
        for key, data in nodes:
            if key == 'limit':
                continue
            if key in ('if', 'else_if', 'else'):
                if key == 'if':
                    taken = False
                limit = dict(data).get('limit', []) if key != 'else' else []
                if not taken and self.condition(limit, scope, chain):
                    self.run(data, scope, chain)
                    taken = True
            elif key == 'set_temp_variable':
                name, token = data[0]
                self.temp[name] = self.value(token, scope, chain)
            elif key == 'clear_temp_array':
                self.temp_arrays[data] = []
            elif key == 'add_to_temp_array':
                f = dict(data)
                self.temp_arrays.setdefault(f['array'], []).append(self.value(f.get('value', 'THIS'), scope, chain))
            elif key == 'add_to_temp_variable':
                name, token = data[0]
                self.temp[name] = self.temp.get(name, 0) + self.value(token, scope, chain)
            elif key == 'for_each_scope_loop':
                f = dict(data)
                body = [(k, v) for k, v in data if k not in ('array', 'break')]
                for row in list(self.value(f['array'], scope, chain)):
                    self.run(body, row, chain + [row])
            elif key == 'every_owned_state':
                limit = dict(data).get('limit', [])
                for state in self.owned(scope):
                    if self.condition(limit, state, chain + [state]):
                        self.run(data, state, chain + [state])
            elif key == 'save_event_target_as':
                self.targets[data] = scope
            elif key.startswith('event_target:'):
                target = self.targets[key[13:]]
                self.run(data, target, chain + [target])
            elif key == 'set_variable':
                name, token = data[0]
                value = self.value(token, scope, chain)
                if name.startswith('global.'):
                    self.globals[name[7:]] = value
                else:
                    scope.values[name] = value
            elif key == 'clear_variable':
                scope.values.pop(data, None)
            elif key == 'set_country_flag':
                scope.flags.add(data)
            elif key == 'clr_country_flag':
                scope.flags.discard(data)
            elif key == 'clear_array':
                scope.values[data] = []
            elif key == 'add_to_array':
                f = dict(data)
                row = self.value(f.get('value', 'THIS'), scope, chain)
                if f['array'].startswith('global.'):
                    self.globals.setdefault(f['array'][7:], []).append(row)
                else:
                    scope.values.setdefault(f['array'], []).append(row)
            elif key == 'add_to_variable':
                name, token = data[0]
                row = self.value(token, scope, chain)
                if name.startswith('global.'):
                    self.globals[name[7:]] = self.globals.get(name[7:], 0) + row
                else:
                    scope.values[name] = scope.values.get(name, 0) + row
            elif key in SCRIPTED and data == 'yes':
                self.call(key, scope)
            else:
                raise AssertionError(f'Unmodelled effect: {key}')

    # ---- declared fixture of the cross-scope native release -----------
    def native_release(self, tag):
        """Declared model of `release = TAG`: the donor's owned cores move."""
        carrier = self.carriers[tag]
        carrier.exists = True
        for state in self.owned(self.donor):
            if tag in state.cores:
                state.owner = carrier
                state.controller = state.controller if state.controller is not self.donor else carrier
        return carrier


def scotland():
    """Donor owns the anchor and two more Scottish cores plus unrelated land."""
    world = World()
    world.capital = world.state(10, capital=True, cores={'GBR'})
    world.anchor = world.state(11, cores={'SCO', 'GBR'})
    world.east = world.state(12, cores={'SCO', 'GBR'})
    world.isles = world.state(13, cores={'SCO'})
    world.england = world.state(14, cores={'GBR'})
    world.donor.values['random_civil_war_event6_package_id'] = PACKAGE_SCO
    world.targets['random_civil_war_event6_selected_anchor'] = world.anchor
    return world


def collect(world, check_rows=0):
    world.temp.update(event021_event6_footprint_valid=0, event021_event6_footprint_input_package_id=PACKAGE_SCO,
                      event021_event6_footprint_check_rows=check_rows)
    world.temp_arrays['independence_wave_event021_footprint_states'] = []
    world.targets['event021_event6_footprint_anchor'] = world.anchor
    world.call('event021_parent_collect_event6_native_footprint', world.donor)
    return world.temp_arrays['independence_wave_event021_footprint_states'], world.temp['event021_event6_footprint_valid']


class NativeFootprintCollectionTests(unittest.TestCase):
    def test_every_donor_owned_carrier_core_is_collected_regardless_of_controller(self):
        world = scotland()
        states, valid = collect(world)
        self.assertEqual(states, [world.anchor, world.east, world.isles])
        self.assertEqual(valid, 1)

    def test_other_packages_and_unrelated_cores_stay_out(self):
        world = scotland()
        world.temp.update(event021_event6_footprint_input_package_id=PACKAGE_WLS)
        world.state(15, cores={'WLS'})
        world.temp_arrays['independence_wave_event021_footprint_states'] = []
        world.temp.update(event021_event6_footprint_valid=0, event021_event6_footprint_check_rows=0)
        world.targets['event021_event6_footprint_anchor'] = world.anchor
        world.call('event021_parent_collect_event6_native_footprint', world.donor)
        self.assertEqual([s.id for s in world.temp_arrays['independence_wave_event021_footprint_states']], [15])

    def test_existing_carrier_makes_the_release_a_no_op_with_an_empty_footprint(self):
        world = scotland()
        world.carriers['SCO'].exists = True
        states, valid = collect(world)
        self.assertEqual((states, valid), ([], 1))

    def test_unsafe_members_reject_the_whole_package(self):
        cases = {
            'host capital is a carrier core': lambda w: w.capital.cores.add('SCO'),
            'a core occupied by another country': lambda w: setattr(w.east, 'controller', w.enemy),
            'a core reserved by the primary plan': lambda w: w.globals['random_civil_war_reserved_states'].append(w.isles),
            'a core that is another front anchor': lambda w: w.globals['random_civil_war_front_states'].append(w.east),
            'a core held by a scenario reservation': lambda w: w.globals['random_civil_war_scenario_reserved_states'].append(w.isles),
        }
        for name, change in cases.items():
            with self.subTest(name):
                world = scotland()
                change(world)
                self.assertEqual(collect(world)[1], 0)

    def test_frozen_scenario_reservation_of_the_donor_is_accepted(self):
        world = scotland()
        world.globals['random_civil_war_scenario_reserved_states'].append(world.isles)
        world.donor.values['random_civil_war_scenario_frozen_states'] = [world.isles]
        self.assertEqual(collect(world)[1], 1)

    def test_candidate_row_overlap_only_blocks_while_rows_are_assembled(self):
        world = scotland()
        world.temp_arrays['event021_parent_dynamic_optional_front_selected_states'] = [world.east]
        self.assertEqual(collect(world, check_rows=1)[1], 0)
        self.assertEqual(collect(world, check_rows=0)[1], 1)


class FootprintLedgerTests(unittest.TestCase):
    def test_candidate_row_spans_the_anchor_and_every_native_core(self):
        world = scotland()
        world.targets['random_civil_war_dynamic_candidate_host'] = world.donor
        world.temp_arrays.update({name: [] for name in (
            'event021_parent_dynamic_optional_front_archetypes', 'event021_parent_dynamic_optional_front_routes',
            'event021_parent_dynamic_optional_front_anchors', 'event021_parent_dynamic_optional_front_sources',
            'event021_parent_dynamic_optional_front_actor_scopes', 'event021_parent_dynamic_optional_front_actor_types',
            'event021_parent_dynamic_optional_front_relationships', 'event021_parent_dynamic_optional_front_goals',
            'event021_parent_dynamic_optional_front_packages', 'event021_parent_dynamic_optional_front_package_regions',
            'event021_parent_dynamic_optional_front_package_depths', 'event021_parent_dynamic_optional_front_package_archetypes',
            'event021_parent_dynamic_optional_front_state_weights', 'event021_parent_dynamic_optional_front_state_counts',
            'event021_parent_dynamic_optional_front_state_offsets', 'event021_parent_dynamic_optional_front_selected_routes',
            'event021_parent_dynamic_optional_front_selected_states')})
        world.targets['random_civil_war_event6_selected_actor'] = world.carriers['SCO']
        world.donor.values.update(random_civil_war_event6_candidate_region=3, random_civil_war_event6_candidate_depth=1,
                                  random_civil_war_event6_candidate_archetype=2)
        prefix = 'event021_parent_dynamic_optional_front_'
        # Declared fixture: the anchor scorer's own helper is outside this test.
        SCRIPTED['event021_parent_score_anchor_state'] = []
        world.call('event021_parent_append_dynamic_event6_front_candidate', world.donor)
        self.assertEqual(world.temp_arrays[prefix + 'selected_states'], [world.anchor, world.east, world.isles])
        self.assertEqual(world.temp_arrays[prefix + 'state_counts'], [3])
        self.assertEqual(world.temp_arrays[prefix + 'state_offsets'], [0])
        self.assertEqual(world.temp_arrays[prefix + 'anchors'], [world.anchor])
        self.assertEqual(world.temp_arrays[prefix + 'packages'], [PACKAGE_SCO])
        # An unsafe footprint adds no row at all instead of falling back to the anchor.
        blocked = scotland()
        blocked.east.controller = blocked.enemy
        blocked.targets['random_civil_war_dynamic_candidate_host'] = blocked.donor
        blocked.temp_arrays.update({k: [] for k in world.temp_arrays})
        blocked.donor.values.update(world.donor.values)
        blocked.call('event021_parent_append_dynamic_event6_front_candidate', blocked.donor)
        self.assertEqual(blocked.temp_arrays[prefix + 'selected_states'], [])
        self.assertEqual(blocked.temp_arrays[prefix + 'anchors'], [])

    def test_plan_reserves_the_footprint_and_an_unsafe_one_blocks_the_opening(self):
        world = scotland()
        world.globals.update(random_civil_war_plan_states=[world.anchor], random_civil_war_reserved_states=[world.anchor],
                             random_civil_war_plan_state_count=1)
        world.call('event021_parent_reserve_event6_native_footprint', world.donor)
        self.assertEqual(world.globals['random_civil_war_plan_states'], [world.anchor, world.east, world.isles])
        self.assertEqual(world.globals['random_civil_war_reserved_states'], [world.anchor, world.east, world.isles])
        self.assertEqual(world.globals['random_civil_war_plan_state_count'], 3)
        self.assertNotIn('random_civil_war_event6_footprint_blocked', world.donor.flags)
        blocked = scotland()
        blocked.east.controller = blocked.enemy
        blocked.globals.update(random_civil_war_plan_states=[blocked.anchor], random_civil_war_reserved_states=[blocked.anchor],
                               random_civil_war_plan_state_count=1)
        blocked.call('event021_parent_reserve_event6_native_footprint', blocked.donor)
        self.assertEqual(blocked.globals['random_civil_war_plan_states'], [blocked.anchor])
        self.assertIn('random_civil_war_event6_footprint_blocked', blocked.donor.flags)
        for scenario, expected in ((world, True), (blocked, False)):
            scenario.global_flags.add('random_civil_war_plan_active')
            scenario.targets.update(random_civil_war_host_country=scenario.donor, random_civil_war_anchor_state=scenario.anchor)
            self.assertEqual(scenario.condition(SCRIPTED['random_civil_war_opening_plan_valid'], scenario.donor, [scenario.donor]), expected)

    def test_mutation_gate_requires_every_native_core_in_a_frozen_ledger_row(self):
        world = scotland()
        world.globals['random_civil_war_planned_front_state_entries'] = [world.anchor, world.east, world.isles]
        world.temp['event021_event6_footprint_covered'] = 0
        world.call('event021_parent_prove_event6_footprint_in_ledger', world.donor)
        # The proof's output is a caller-declared temporary, so it survives the return.
        self.assertEqual(world.temp['event021_event6_footprint_covered'], 1)
        for ledger, label in (([world.anchor], 'anchor-only row'), ([world.anchor, world.east], 'one core missing')):
            with self.subTest(label):
                world = scotland()
                world.globals['random_civil_war_planned_front_state_entries'] = ledger
                world.temp['event021_event6_footprint_covered'] = 1
                world.call('event021_parent_prove_event6_footprint_in_ledger', world.donor)
                self.assertEqual(world.temp['event021_event6_footprint_covered'], 0)

    def test_mutation_gate_accepts_the_reviewing_governments_active_row(self):
        world = scotland()
        world.donor.values['random_civil_war_active_front_state_entries'] = [world.anchor, world.east, world.isles]
        world.targets['random_civil_war_active_front_commit_owner'] = world.donor
        world.temp['event021_event6_footprint_covered'] = 0
        world.call('event021_parent_prove_event6_footprint_in_ledger', world.donor)
        self.assertEqual(world.temp['event021_event6_footprint_covered'], 1)

    def test_carrier_records_the_states_it_actually_received(self):
        world = scotland()
        world.targets['random_civil_war_event6_selection_owner'] = world.donor
        carrier = world.native_release('SCO')
        world.targets['random_civil_war_event6_selected_actor'] = carrier
        world.call('event021_parent_publish_event6_release_footprint', world.donor)
        self.assertEqual(world.donor.values['random_civil_war_event6_opening_state_count'], 3)
        self.assertEqual(world.globals['random_civil_war_event6_pending_opening_state_count'], 3)
        world.call('event021_parent_record_event6_actor_footprint', carrier)
        self.assertEqual(carrier.values['random_civil_war_opening_core_states'], [world.anchor, world.east, world.isles])
        self.assertEqual(carrier.values['random_civil_war_opening_state_count'], 3)
        # A living carrier is reused: the release did nothing, only the anchor changed hands.
        living = scotland()
        living.carriers['SCO'].exists = True
        living.targets.update(random_civil_war_event6_selection_owner=living.donor,
                              random_civil_war_event6_selected_actor=living.carriers['SCO'])
        living.donor.flags.add('random_civil_war_event6_actor_preexisted')
        living.anchor.owner = living.carriers['SCO']
        living.call('event021_parent_publish_event6_release_footprint', living.donor)
        living.call('event021_parent_record_event6_actor_footprint', living.carriers['SCO'])
        self.assertEqual(living.globals['random_civil_war_event6_pending_opening_state_count'], 1)
        self.assertEqual(living.carriers['SCO'].values['random_civil_war_opening_core_states'], [living.anchor])


class ActiveRemnantFootprintTests(unittest.TestCase):
    """The active builder proves the remnant against the row's whole span."""

    @staticmethod
    def accepted_rows(span):
        rt = MapRuntime()  # four-state chain, capital at the first state, remnant minimum two
        rt.temp_arrays.update(event021_parent_dynamic_optional_front_archetypes=[Decimal(1)],
                              event021_parent_dynamic_optional_front_state_offsets=[Decimal(0)],
                              event021_parent_dynamic_optional_front_state_counts=[Decimal(len(span))],
                              event021_parent_dynamic_optional_front_selected_states=[rt.states[i] for i in span])
        body = next(data for key, data in ACTIVE['event021_parent_build_active_front_rows'] if key == 'if')
        phase = []
        for node in body:
            if node[0] == 'limit':
                continue
            if node == ('set_temp_variable', [('event021_active_weight_remaining', 'constant:random_civil_war_value.zero')]):
                break
            phase.append(node)
        rt.run(phase, rt.host)
        return rt.temp_arrays['event021_active_accepted_rows']

    def test_anchor_only_span_hides_a_release_that_strands_the_capital(self):
        # Native release also hands over the two states between the capital and the anchor.
        self.assertEqual(self.accepted_rows([3]), [Decimal(0)])

    def test_complete_span_rejects_the_same_package(self):
        self.assertEqual(self.accepted_rows([3, 1, 2]), [])

    def test_complete_span_that_keeps_a_connected_remnant_is_accepted(self):
        self.assertEqual(self.accepted_rows([3, 2]), [Decimal(0)])


if __name__ == '__main__':
    unittest.main()
