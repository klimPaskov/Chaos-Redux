"""Execute actual active/ordinary row bind and reject dispatch on fixtures.

This validates routing and stored metadata, not native war creation.
Country/global saved state is separate from conservative helper temporaries.
"""
from decimal import Decimal
import unittest

from test_event021_active_front_receipt import ACTIVE, ReceiptRuntime
from test_event021_evolution_log import Country, load


CORE = dict(load('common/scripted_effects/021_random_civil_war_effects.txt'))


class RoutingRuntime(ReceiptRuntime):
    def __init__(self):
        super().__init__()
        self.side = Country(3)
        self.global_flags = {'random_civil_war_active_front_commit_in_progress', 'random_civil_war_front_plan_ready'}
        self.targets['random_civil_war_active_front_commit_owner'] = self.host
        self.host.values.update(random_civil_war_active_front_ids=[101], random_civil_war_active_front_statuses=[1],
                                random_civil_war_active_front_archetypes=[4], random_civil_war_active_front_relationships=[3],
                                random_civil_war_active_front_routes=[4], random_civil_war_active_front_package_ids=[0],
                                random_civil_war_active_front_state_counts=[2], random_civil_war_active_front_source_ids=[9])
        self.globals.update(random_civil_war_planned_front_ids=[101], random_civil_war_planned_front_status_entries=[1],
                            random_civil_war_planned_front_archetype_entries=[2], random_civil_war_planned_front_relationship_entries=[1],
                            random_civil_war_planned_front_route_entries=[2], random_civil_war_planned_front_package_entries=[0],
                            random_civil_war_planned_front_state_counts=[7], random_civil_war_planned_front_actor_type_entries=[2],
                            random_civil_war_planned_front_source_ids=[88])
        self.temporary.update(event021_planned_front_id_to_mark=Decimal(101), event021_planned_front_status_to_mark=Decimal(2))

    def condition(self, nodes, actor):
        for key, data in nodes:
            if key == 'has_global_flag':
                result = data in self.global_flags
            elif key == 'has_event_target':
                result = data in self.targets
            else:
                result = super().condition([(key, data)], actor)
            if not result:
                return False
        return True

    def call(self, name, actor):
        scalars, arrays = set(self.temporary), set(self.temp_arrays)
        self.run((CORE if name in CORE else ACTIVE)[name], actor)
        self.temporary = {k: v for k, v in self.temporary.items() if k in scalars}
        self.temp_arrays = {k: v for k, v in self.temp_arrays.items() if k in arrays}

    def run(self, nodes, actor):
        taken = False
        for key, data in nodes:
            if key in ('if', 'else_if', 'else'):
                if key == 'if':
                    taken = False
                should_run = not taken and (key == 'else' or self.condition(dict(data)['limit'], actor))
                if should_run:
                    self.run([(k, v) for k, v in data if k != 'limit'], actor)
                    taken = True
            elif key.startswith('event_target:'):
                self.run(data, self.targets[key[13:]])
            elif key == 'set_variable':
                name, token = data[0]
                store = self.globals if name.startswith('global.') else actor.values
                name = name.removeprefix('global.')
                if '^' in name:
                    name, index = name.split('^', 1)
                    store[name][int(self.value(index, actor))] = self.value(token, actor)
                else:
                    store[name] = self.value(token, actor)
            elif key in CORE or key in ACTIVE:
                self.call(key, actor)
            else:
                super().run([(key, data)], actor)


class ActiveRowRoutingTests(unittest.TestCase):
    def test_active_bind_wins_over_a_ready_outer_plan_with_the_same_id(self):
        rt = RoutingRuntime()
        rt.call('event021_bind_front_plan_row', rt.side)
        self.assertEqual(rt.host.values['random_civil_war_active_front_statuses'], [2])
        self.assertEqual(rt.globals['random_civil_war_planned_front_status_entries'], [1])
        self.assertEqual(rt.side.values['random_civil_war_front_plan_row_state_count'], 2)
        self.assertEqual(rt.side.values['random_civil_war_source_front_id'], 9)

    def test_active_reject_changes_only_the_current_owner_row(self):
        rt = RoutingRuntime()
        rt.call('event021_reject_pending_front_plan_row', rt.side)
        rejected = rt.value('constant:random_civil_war_planned_front_status.rejected', rt.side)
        self.assertEqual(rt.host.values['random_civil_war_active_front_statuses'], [rejected])
        self.assertEqual(rt.globals['random_civil_war_planned_front_status_entries'], [1])

    def test_missing_active_owner_never_falls_back_to_outer_plan(self):
        for helper in ('event021_bind_front_plan_row', 'event021_reject_pending_front_plan_row'):
            with self.subTest(helper=helper):
                rt = RoutingRuntime()
                del rt.targets['random_civil_war_active_front_commit_owner']
                rt.call(helper, rt.side)
                self.assertEqual(rt.globals['random_civil_war_planned_front_status_entries'], [1])
                self.assertNotIn('random_civil_war_front_plan_row_bound', rt.side.flags)

    def test_normal_opening_binding_still_uses_the_outer_plan(self):
        rt = RoutingRuntime()
        rt.global_flags.remove('random_civil_war_active_front_commit_in_progress')
        rt.call('event021_bind_front_plan_row', rt.side)
        self.assertEqual(rt.globals['random_civil_war_planned_front_status_entries'], [2])
        self.assertEqual(rt.side.values['random_civil_war_front_plan_row_state_count'], 7)


if __name__ == '__main__':
    unittest.main()
