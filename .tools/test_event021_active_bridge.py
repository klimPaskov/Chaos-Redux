"""Execute the active bridge and actual adapter cleanup on declared fixtures.

Global/country scalars, global/regular targets, flags, normal arrays, temporary
scalars and temporary arrays are separate stores. Helper return conservatively
drops newly introduced temporaries. Adapter overwrites and durable publication
are declared inputs, not simulated civil wars or engine proof.
"""
from dataclasses import dataclass, field
from decimal import Decimal
import operator
from pathlib import Path
import unittest

from test_event021_evolution_log import parse, load


ROOT = Path(__file__).resolve().parents[1]


def source(name):
    return dict(load('common/scripted_effects/' + name))


BRIDGE = source('021_random_civil_war_active_bridge_effects.txt')
PARENT = source('021_random_civil_war_parent_effects.txt')
ACTIVE = source('021_random_civil_war_active_evolution_effects.txt')
CONSTANTS = dict(load('common/script_constants/021_random_civil_war_constants.txt'))
LEDGER = source('021_random_civil_war_front_ledger_effects.txt')
SAVE = 'event021_parent_save_active_transaction_bridge'
RESTORE = 'event021_parent_restore_active_transaction_bridge'
PRIVATE = 'event021_active_transaction_'
PREFIX = 'random_civil_war_'
SCALARS = tuple(PREFIX + name for name in (
    'pending_generation', 'pending_severity', 'pending_crisis_id',
    'pending_archetype', 'pending_opposition_front_id', 'pending_opening_size',
    'pending_army_ratio', 'pending_navy_ratio', 'pending_air_ratio',
    'pending_secondary_front_id', 'pending_secondary_anchor_state_id',
    'pending_secondary_opening_size', 'pending_secondary_opening_state_count',
    'pending_secondary_army_ratio', 'pending_secondary_navy_ratio',
    'pending_secondary_air_ratio', 'pending_secondary_archetype',
    'pending_secondary_front_goal', 'planned_secondary_archetype',
    'planned_secondary_front_goal', 'event6_pending_package_id',
    'event6_pending_region', 'event6_pending_depth', 'event6_pending_archetype',
    'event6_pending_opening_state_count', 'pending_event6_secondary_front_id',
    'event6_secondary_planned_package_id', 'event6_secondary_planned_region',
    'event6_secondary_planned_depth', 'event6_secondary_planned_archetype'))
TARGETS = tuple(PREFIX + name for name in (
    'global_host_country', 'secondary_anchor_state', 'secondary_source_country',
    'preplanned_secondary_anchor_state', 'event6_secondary_planned_anchor',
    'event6_secondary_planned_actor', 'active_front_commit_owner'))
FLAGS = tuple(PREFIX + name for name in (
    'secondary_front_pending', 'secondary_route_prepared',
    'secondary_front_preplanned', 'event6_secondary_search_active',
    'event6_secondary_front_pending', 'event6_secondary_front_preplanned',
    'dynamic_front_activation_active', 'active_front_commit_in_progress'))


@dataclass(eq=False)
class Object:
    id: int
    kind: str = 'country'
    exists: bool = True
    scalars: dict = field(default_factory=dict)
    arrays: dict = field(default_factory=dict)
    flags: set = field(default_factory=set)


def flatten(nodes):
    for key, data in nodes:
        yield key, data
        if isinstance(data, list):
            yield from flatten(data)


class Runtime:
    def __init__(self):
        self.host = Object(1)
        self.other = Object(2)
        self.state = Object(11, 'state')
        self.new_state = Object(12, 'state')
        self.dead = Object(3, exists=False)
        self.globals = {}
        self.global_arrays = {'durable_front_ids': [101, 102]}
        self.global_targets = {}
        self.regular_targets = {}
        self.global_flags = set()
        self.temporary = {'caller_result': Decimal(7)}
        self.temp_arrays = {'caller_rows': [self.state]}
        self.previous = None
        self.helpers = {**PARENT, **ACTIVE, **BRIDGE}

    def scalar_store(self, name, actor):
        return (self.globals, name[7:]) if name.startswith('global.') else (actor.scalars, name)

    def value(self, token, actor):
        if token.startswith('constant:'):
            group, key = token[9:].split('.', 1)
            return Decimal(dict(CONSTANTS[group])[key])
        if token.startswith('event_target:'):
            name = token[13:]
            return self.regular_targets.get(name, self.global_targets.get(name))
        store, name = self.scalar_store(token, actor)
        if name in store:
            return store[name]
        if token in self.temporary:
            return self.temporary[token]
        try:
            return Decimal(token)
        except Exception as error:
            raise AssertionError('Undeclared fixture value: ' + token) from error

    def condition(self, nodes, actor):
        for key, data in nodes:
            if key == 'has_variable':
                store, name = self.scalar_store(data, actor)
                result = name in store
            elif key == 'has_country_flag':
                result = data in actor.flags
            elif key == 'has_global_flag':
                result = data in self.global_flags
            elif key == 'has_event_target':
                result = data in self.global_targets or data in self.regular_targets
            elif key == 'NOT':
                result = not any(self.condition([node], actor) for node in data)
            elif key == 'check_variable':
                fields = dict(data)
                result = {'equals': operator.eq, 'greater_than': operator.gt}[fields['compare']](
                    self.value(fields['var'], actor), self.value(fields['value'], actor))
            elif key.startswith('event_target:'):
                previous = self.previous
                self.previous = actor
                try:
                    result = self.condition(data, self.value(key, actor))
                finally:
                    self.previous = previous
            elif key == 'tag' and data == 'PREV':
                result = actor is self.previous
            else:
                raise AssertionError('Unsupported fixture condition: ' + key)
            if not result:
                return False
        return True

    def call(self, helper, actor=None):
        actor = actor or self.host
        scalar_keys, array_keys = set(self.temporary), set(self.temp_arrays)
        self.execute(self.helpers[helper], actor)
        self.temporary = {key: value for key, value in self.temporary.items() if key in scalar_keys}
        self.temp_arrays = {key: value for key, value in self.temp_arrays.items() if key in array_keys}

    def execute(self, nodes, actor):
        taken = False
        for key, data in nodes:
            if key == 'if':
                taken = self.condition(dict(data).get('limit', []), actor)
                if taken:
                    self.execute([(k, v) for k, v in data if k != 'limit'], actor)
            elif key == 'else':
                if not taken:
                    self.execute(data, actor)
            elif key in ('set_variable', 'clear_variable'):
                name, token = data[0] if key == 'set_variable' else (data, None)
                store, name = self.scalar_store(name, actor)
                if key == 'set_variable':
                    store[name] = self.value(token, actor)
                else:
                    store.pop(name, None)
            elif key in ('set_country_flag', 'clr_country_flag', 'set_state_flag', 'clr_state_flag'):
                if key.startswith('set_'):
                    actor.flags.add(data)
                else:
                    actor.flags.discard(data)
            elif key in ('set_global_flag', 'clr_global_flag'):
                if key == 'set_global_flag':
                    self.global_flags.add(data)
                else:
                    self.global_flags.discard(data)
            elif key == 'save_global_event_target_as':
                self.global_targets[data] = actor
            elif key == 'clear_global_event_target':
                self.global_targets.pop(data, None)
            elif key.startswith('var:'):
                target = actor.scalars[key[4:]]
                assert isinstance(target, Object), 'Scope pointer required'
                self.execute(data, target)
            elif key.startswith('event_target:'):
                target = self.value(key, actor)
                assert isinstance(target, Object), 'Scope pointer required'
                self.execute(data, target)
            elif key == 'set_temp_variable':
                name, token = data[0]
                self.temporary[name] = self.value(token, actor)
            elif key == 'clear_temp_array':
                self.temp_arrays[data] = []
            elif key in self.helpers and data == 'yes':
                self.call(key, actor)
            else:
                raise AssertionError('Unsupported fixture effect: ' + key)


class BridgeTests(unittest.TestCase):
    def seed(self, runtime, pattern, phase=0):
        for index, name in enumerate(SCALARS):
            mode = (index + phase) % 3 if pattern == 'mixed' else {
                'absent': 0, 'zero': 1, 'present': 2}[pattern]
            if mode:
                runtime.globals[name] = Decimal(0) if mode == 1 else Decimal('-12.34567') + index
            # A country variable with the same name must not supply a global copy.
            runtime.host.scalars[name] = Decimal(999)
        for index, name in enumerate(TARGETS):
            if pattern != 'absent' and (pattern != 'mixed' or (index + phase) % 2):
                runtime.global_targets[name] = (runtime.state if 'anchor' in name else runtime.dead)
        for index, name in enumerate(FLAGS):
            if pattern != 'absent' and (pattern != 'mixed' or (index + phase) % 2):
                runtime.global_flags.add(name)

    def borrowed(self, runtime):
        return ({k: runtime.globals[k] for k in SCALARS if k in runtime.globals},
                {k: runtime.global_targets[k] for k in TARGETS if k in runtime.global_targets},
                runtime.global_flags.intersection(FLAGS))

    def assert_clean(self, runtime):
        self.assertFalse([key for key in runtime.host.scalars if key.startswith(PRIVATE)])
        self.assertFalse([key for key in runtime.host.flags if key.startswith(PRIVATE)])

    def test_restore_after_actual_success_and_rejection_cleanup(self):
        for path in ('ordinary_success', 'ordinary_rejection', 'event6_success', 'event6_rejection'):
            for pattern, phase in [('absent', 0), ('zero', 0), ('present', 0),
                                   ('mixed', 0), ('mixed', 1), ('mixed', 2)]:
                with self.subTest(path=path, pattern=pattern, phase=phase):
                    runtime = Runtime()
                    self.seed(runtime, pattern, phase)
                    before = self.borrowed(runtime)
                    runtime.call(SAVE)
                    # Declared ordinary/Event6 adapter overwrites, followed by
                    # execution of the current parent-owned cleanup source.
                    runtime.globals.update({name: Decimal(87) for name in SCALARS})
                    runtime.global_targets.update({name: runtime.new_state if 'anchor' in name else runtime.other
                                                   for name in TARGETS})
                    runtime.global_flags.symmetric_difference_update(FLAGS)
                    if path.startswith('ordinary'):
                        helper = ('event021_parent_reject_secondary_transfer' if path.endswith('rejection')
                                  else 'event021_parent_clear_pending_force_transaction')
                        runtime.call(helper)
                        runtime.call('event021_parent_clear_preplanned_secondary_opening')
                    else:
                        runtime.call('event021_parent_clear_event6_secondary_pending')
                    runtime.globals['random_civil_war_next_front_id'] = Decimal(104)
                    runtime.global_arrays['durable_front_ids'].append(103)
                    runtime.global_targets['random_civil_war_priority_front_state'] = runtime.new_state
                    runtime.global_flags.add('random_civil_war_priority_front_active')
                    runtime.call(RESTORE)
                    self.assertEqual(before, self.borrowed(runtime))
                    self.assert_clean(runtime)
                    self.assertEqual(Decimal(104), runtime.globals['random_civil_war_next_front_id'])
                    self.assertEqual([101, 102, 103], runtime.global_arrays['durable_front_ids'])
                    self.assertIs(runtime.new_state, runtime.global_targets['random_civil_war_priority_front_state'])
                    self.assertIn('random_civil_war_priority_front_active', runtime.global_flags)
                    self.assertEqual({'caller_result': Decimal(7)}, runtime.temporary)
                    self.assertEqual({'caller_rows': [runtime.state]}, runtime.temp_arrays)
                    self.assertTrue(all(runtime.host.scalars[name] == 999 for name in SCALARS))
                    runtime.call(RESTORE)
                    self.assertEqual(before, self.borrowed(runtime))

    def test_no_snapshot_and_wrong_country_are_noops(self):
        runtime = Runtime()
        self.seed(runtime, 'present')
        before = self.borrowed(runtime)
        runtime.call(RESTORE)
        self.assertEqual(before, self.borrowed(runtime))
        runtime.call(SAVE)
        runtime.call(RESTORE, runtime.other)
        self.assertEqual(before, self.borrowed(runtime))
        self.assertIn(PRIVATE + 'bridge_saved', runtime.host.flags)
        runtime.call(RESTORE)
        self.assert_clean(runtime)

    def test_parent_wrapper_order_and_round_trip(self):
        runtime = Runtime()
        self.seed(runtime, 'mixed')
        before = self.borrowed(runtime)
        runtime.call('event021_parent_save_active_commit_bridge')
        runtime.globals.update({name: Decimal(88) for name in SCALARS})
        runtime.call('event021_parent_restore_active_commit_bridge')
        self.assertEqual(before, self.borrowed(runtime))
        self.assert_clean(runtime)
        outer = dict(ACTIVE['event021_parent_commit_active_front_rows'])['if']
        order = [key for key, _ in outer]
        save = order.index('event021_parent_save_active_commit_bridge')
        restore = order.index('event021_parent_restore_active_commit_bridge')
        self.assertNotIn(('clr_global_flag', 'random_civil_war_active_front_commit_in_progress'), outer)
        for index, (key, data) in enumerate(outer):
            if key in ('set_global_flag', 'save_global_event_target_as'):
                self.assertLess(save, index)
            if key in ('clr_global_flag', 'clear_global_event_target'):
                self.assertLess(index, restore)

    def test_borrowed_preplanned_flags_do_not_override_active_loader_branches(self):
        runtime = Runtime()
        runtime.globals['random_civil_war_pending_secondary_front_id'] = Decimal(0)
        runtime.host.scalars['random_civil_war_front_id'] = Decimal(12)
        runtime.global_flags.add('random_civil_war_active_front_commit_in_progress')
        runtime.global_targets['random_civil_war_active_front_commit_owner'] = runtime.host
        cases = (
            (PARENT, 'event021_parent_load_planned_secondary_front',
             'event021_parent_load_active_secondary_front'),
            (PARENT, 'event021_parent_copy_planned_front_state_span',
             'event021_parent_copy_active_front_state_span'),
            (PARENT, 'event021_parent_copy_opening_state_receipts', None),
            (LEDGER, 'event021_parent_validate_secondary_transfer_receipt',
             'event021_parent_validate_active_secondary_transfer_receipt'))
        for borrowed in (False, True):
            if borrowed:
                runtime.global_flags.update(('random_civil_war_secondary_front_preplanned',
                                             'random_civil_war_secondary_route_prepared',
                                             'random_civil_war_front_plan_ready'))
            for registry, name, call in cases:
                branch = next(data for key, data in registry[name] if key == 'if')
                with self.subTest(borrowed=borrowed, helper=name):
                    self.assertTrue(runtime.condition(dict(branch)['limit'], runtime.host))
                    if call:
                        self.assertIn((call, 'yes'), branch)

    def test_active_cleanup_preserves_borrowed_marker_and_unrelated_actor(self):
        runtime = Runtime()
        marker = 'random_civil_war_secondary_transfer_state'
        runtime.state.flags.add(marker)
        runtime.global_targets['random_civil_war_preplanned_secondary_anchor_state'] = runtime.state
        runtime.regular_targets['random_civil_war_event6_selected_actor'] = runtime.other
        generation = 'random_civil_war_event6_adapter_previous_generation'
        runtime.other.scalars[generation] = Decimal(0)
        runtime.call(SAVE)
        runtime.global_flags.add('random_civil_war_active_front_commit_in_progress')
        runtime.call('event021_parent_clear_active_secondary_pending')
        runtime.call('event021_parent_clear_event6_package_transaction')
        runtime.call(RESTORE)
        self.assertIs(runtime.state, runtime.global_targets['random_civil_war_preplanned_secondary_anchor_state'])
        self.assertIn(marker, runtime.state.flags)
        self.assertEqual(runtime.other.scalars[generation], 0)

    def test_actor_cleanup_requires_current_owner_validity_and_matching_package(self):
        for mismatch in (None, 'owner', 'validity', 'package'):
            with self.subTest(mismatch=mismatch):
                runtime = Runtime()
                package = 'random_civil_war_event6_package_id'
                generation = 'random_civil_war_event6_adapter_previous_generation'
                runtime.host.scalars[package] = Decimal(23)
                runtime.host.flags.add('random_civil_war_event6_selected_actor_valid')
                runtime.other.scalars.update({package: Decimal(23), generation: Decimal(0)})
                runtime.regular_targets.update(random_civil_war_event6_selection_owner=runtime.host,
                                               random_civil_war_event6_selected_actor=runtime.other)
                if mismatch == 'owner':
                    runtime.regular_targets['random_civil_war_event6_selection_owner'] = runtime.other
                elif mismatch == 'validity':
                    runtime.host.flags.clear()
                elif mismatch == 'package':
                    runtime.other.scalars[package] = Decimal(24)
                runtime.call('event021_parent_clear_event6_package_transaction')
                self.assertEqual(generation in runtime.other.scalars, mismatch is not None)

    def test_save_clears_old_copies_and_helper_return_drops_new_temporaries(self):
        runtime = Runtime()
        self.seed(runtime, 'present')
        runtime.call(SAVE)
        runtime.globals.clear()
        runtime.global_targets.clear()
        runtime.global_flags.clear()
        runtime.call(SAVE)
        runtime.helpers['fixture_borrow'] = [
            ('set_temp_variable', [('callee_value', '4')]),
            ('clear_temp_array', 'callee_rows')]
        runtime.call('fixture_borrow')
        self.assertNotIn('callee_value', runtime.temporary)
        self.assertNotIn('callee_rows', runtime.temp_arrays)
        runtime.globals.update({name: Decimal(1) for name in SCALARS})
        runtime.global_targets.update({name: runtime.other for name in TARGETS})
        runtime.global_flags.update(FLAGS)
        runtime.call(RESTORE)
        self.assertEqual(({}, {}, set()), self.borrowed(runtime))
        self.assert_clean(runtime)

    def test_explicit_contract_covers_actual_serial_mutations(self):
        saved_scalars = {data for key, data in flatten(BRIDGE[SAVE])
                         if key == 'has_variable' and data.startswith('global.')}
        saved_targets = {data for key, data in flatten(BRIDGE[SAVE]) if key == 'has_event_target'}
        saved_flags = {data for key, data in flatten(BRIDGE[SAVE]) if key == 'has_global_flag'}
        self.assertEqual({'global.' + name for name in SCALARS}, saved_scalars)
        self.assertEqual(set(TARGETS), saved_targets)
        self.assertEqual(set(FLAGS), saved_flags)
        bodies = [PARENT[name] for name in (
            'event021_parent_clear_pending_force_transaction',
            'event021_parent_clear_preplanned_secondary_opening',
            'event021_parent_clear_event6_package_transaction',
            'event021_parent_start_secondary_civil_war',
            'event021_parent_reject_secondary_transfer',
            'event021_parent_try_event6_secondary_front',
            'event021_parent_initialize_secondary_opposition_actor')]
        bodies += [ACTIVE['event021_parent_commit_active_front_rows'],
                   ACTIVE['event021_parent_commit_active_front_row'],
                   ACTIVE['event021_parent_load_active_secondary_front']]
        for body in bodies:
            for key, data in flatten(body):
                if key == 'set_variable' and data[0][0].startswith('global.'):
                    name = data[0][0]
                    if name != 'global.random_civil_war_next_front_id':
                        self.assertIn(name, saved_scalars)
                elif key == 'clear_variable' and data.startswith('global.'):
                    self.assertIn(data, saved_scalars)
                elif key in ('save_global_event_target_as', 'clear_global_event_target'):
                    self.assertIn(data, saved_targets)
                elif key in ('set_global_flag', 'clr_global_flag'):
                    self.assertIn(data, saved_flags)

    def test_native_storage_contract_and_durable_exclusion(self):
        for body in BRIDGE.values():
            for key, data in flatten(body):
                self.assertNotIn(key, ('meta_effect', 'set_temp_variable', 'clear_array',
                                       'clear_temp_array', 'add_to_array', 'add_to_temp_array'))
                if key == 'set_variable':
                    name, value = data[0]
                    self.assertTrue(name.startswith(PRIVATE) or name in {'global.' + n for n in SCALARS})
                    self.assertNotIn('$', value)
                elif key.startswith('var:'):
                    self.assertTrue(key.startswith('var:' + PRIVATE))


if __name__ == '__main__':
    unittest.main(verbosity=2)
