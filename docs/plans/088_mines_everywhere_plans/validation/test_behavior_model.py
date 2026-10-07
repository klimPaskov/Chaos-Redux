"""Run locally with: python -m unittest -v test_behavior_model.py"""
from copy import deepcopy
from itertools import product
import random
import unittest

from behavior_model import (
    World, fire, remove_for_test, UnsupportedConfiguration, IncompleteApplication,
)


class Event088ModelTests(unittest.TestCase):
    def test_full_cartesian_coverage(self):
        world = World({'A', 'B', 'C'}, {0, 5, 99})
        receipt = fire(world)
        self.assertEqual(set(world.fields), set(product(world.eligible_owners, world.valid_regions)))
        self.assertEqual(receipt.new_calls, 9)
        self.assertEqual(set(world.fields.values()), {1000})

    def test_duplicate_input_sets_do_not_duplicate_writes(self):
        world = World({'A'}, {0, 7})
        fire(world, ['A', 'A'], [7, 0, 7])
        self.assertEqual(world.pair_calls, [('A', 0), ('A', 7)])

    def test_sparse_new_region_and_zero_are_covered(self):
        world = World({'A'}, {0, 9, 99999})
        fire(world)
        self.assertEqual(len(world.fields), 3)
        self.assertEqual(world.fields[('A', 99999)], 1000)

    def test_standard_cap_examples(self):
        for before in (0, 250, 995, 1000):
            with self.subTest(before=before):
                world = World({'A'}, {1}, {('A', 1): before})
                fire(world)
                self.assertEqual(world.fields[('A', 1)], 1000)

    def test_raised_cap_still_adds_exactly_one_thousand(self):
        world = World({'A'}, {1}, {('A', 1): 250}, default_cap=2000)
        fire(world)
        self.assertEqual(world.fields[('A', 1)], 1250)

    def test_lower_cap_is_respected(self):
        world = World({'A'}, {1}, {('A', 1): 250}, default_cap=750)
        fire(world)
        self.assertEqual(world.fields[('A', 1)], 750)

    def test_over_cap_rejects_before_any_write(self):
        world = World({'A', 'B'}, {1}, {('B', 1): 1500})
        before = deepcopy(world)
        with self.assertRaises(UnsupportedConfiguration):
            fire(world)
        self.assertEqual(world, before)

    def test_owner_fields_remain_independent(self):
        world = World({'A', 'B'}, {1}, {('A', 1): 900, ('B', 1): 100})
        fire(world)
        self.assertEqual(world.fields, {('A', 1): 1000, ('B', 1): 1000})

    def test_excluded_owner_does_not_remove_geography(self):
        world = World({'A'}, {1, 2}, {('INELIGIBLE', 1): 50})
        fire(world)
        self.assertEqual(world.fields[('INELIGIBLE', 1)], 50)
        self.assertEqual(world.fields[('A', 2)], 1000)

    def test_unrelated_fields_are_untouched(self):
        world = World({'A'}, {1}, {('X', 88): 155})
        fire(world)
        self.assertEqual(world.fields[('X', 88)], 155)

    def test_missing_region_or_owner_rejects(self):
        for owners, regions in [(['A'], [1, 2]), (['A', 'B'], [1])]:
            world = World({'A', 'B'}, {1, 2})
            before = deepcopy(world)
            with self.assertRaises(UnsupportedConfiguration):
                fire(world, owners, regions)
            self.assertEqual(world, before)

    def test_extra_invalid_region_rejects(self):
        world = World({'A'}, {1})
        with self.assertRaises(UnsupportedConfiguration):
            fire(world, regions=[1, 2])
        self.assertEqual(world.status, 'unfired')

    def test_unverified_map_rejects_without_consumption(self):
        world = World({'A'}, {1})
        with self.assertRaises(UnsupportedConfiguration):
            fire(world, coverage_verified=False)
        self.assertEqual((world.status, world.chaos, world.history_entries), ('unfired', 0, 0))

    def test_empty_sets_reject_without_history(self):
        for c, r in [(set(), {1}), ({'A'}, set()), (set(), set())]:
            world = World(c, r)
            with self.assertRaises(UnsupportedConfiguration):
                fire(world)
            self.assertEqual(world.history_entries, 0)

    def test_invalid_cap_or_amount_rejects(self):
        for before, cap in [(-1, 1000), (1, 0), (1, -1), (1, True)]:
            world = World({'A'}, {1}, {('A', 1): before}, default_cap=cap)
            before_world = deepcopy(world)
            with self.assertRaises(UnsupportedConfiguration):
                fire(world)
            self.assertEqual(world, before_world)

    def test_duplicate_dispatch_changes_nothing(self):
        world = World({'A'}, {1}, default_cap=5000)
        fire(world)
        before = deepcopy(world)
        self.assertFalse(fire(world).committed)
        self.assertEqual(world, before)

    def test_reentry_after_test_clearance_does_not_refill(self):
        world = World({'A', 'B'}, {1})
        fire(world)
        remove_for_test(world, ('B', 1), 1000)
        fire(world)
        self.assertEqual(world.fields[('B', 1)], 0)
        self.assertEqual(world.fields[('A', 1)], 1000)

    def test_material_chaos_once_not_per_pair(self):
        world = World({f'C{i}' for i in range(50)}, set(range(100)))
        receipt = fire(world)
        self.assertEqual(receipt.new_calls, 5000)
        self.assertEqual((world.chaos, world.history_entries), (20, 1))
        fire(world)
        self.assertEqual((world.chaos, world.history_entries), (20, 1))

    def test_all_full_consumes_without_chaos(self):
        world = World({'A'}, {1}, {('A', 1): 1000})
        receipt = fire(world)
        self.assertEqual((receipt.changed_fields, receipt.chaos_delta), (0, 0))
        self.assertEqual((world.status, world.history_entries), ('committed', 1))

    def test_partial_failure_does_not_rollback_and_blocks_retry(self):
        world = World({'A'}, {1, 2, 3}, {('A', 1): 50}, default_cap=5000)
        with self.assertRaises(IncompleteApplication):
            fire(world, fail_after=1)
        self.assertEqual(world.fields[('A', 1)], 1050)
        self.assertNotIn(('A', 2), world.fields)
        self.assertEqual((world.status, world.chaos, world.history_entries), ('incomplete', 0, 0))
        before = deepcopy(world)
        with self.assertRaises(IncompleteApplication):
            fire(world)
        self.assertEqual(world, before)

    def test_legacy_consumption_does_not_add_global_fields(self):
        world = World({'A'}, {1, 2}, {('A', 1): 1000}, status='legacy-consumed')
        before = deepcopy(world)
        fire(world)
        self.assertEqual(world, before)

    def test_copied_save_state_retains_consumption(self):
        world = World({'A'}, {1})
        fire(world)
        restored = deepcopy(world)  # Abstract state copy, not a HOI4 save/load.
        remove_for_test(restored, ('A', 1), 1000)
        fire(restored)
        self.assertEqual(restored.fields[('A', 1)], 0)
        self.assertEqual(restored.history_entries, 1)

    def test_late_country_is_not_automatically_granted_fields(self):
        world = World({'A'}, {1})
        fire(world)
        world.eligible_owners.add('NEW')
        fire(world)
        self.assertNotIn(('NEW', 1), world.fields)

    def test_one_thousand_seeded_random_worlds(self):
        rng = random.Random(880922)
        for _ in range(1000):
            c = {f'C{i}' for i in range(rng.randint(1, 8))}
            r = set(rng.sample(range(0, 10000), rng.randint(1, 12)))
            caps = {pair: rng.choice([500, 750, 1000, 2000, 5000]) for pair in product(c, r)}
            values = {pair: rng.randint(0, cap) for pair, cap in caps.items()}
            world = World(c, r, values.copy(), caps)
            receipt = fire(world)
            self.assertEqual(len(world.pair_calls), len(c)*len(r))
            self.assertEqual(len(set(world.pair_calls)), len(world.pair_calls))
            for pair, cap in caps.items():
                self.assertEqual(world.fields[pair], min(cap, values[pair] + 1000))
                self.assertGreaterEqual(world.fields[pair], values[pair])
            self.assertEqual(receipt.chaos_delta, 20 if any(world.fields[k] > values[k] for k in values) else 0)
            before_retry = deepcopy(world)
            fire(world)
            self.assertEqual(world, before_retry)


if __name__ == '__main__':
    unittest.main(verbosity=2)
