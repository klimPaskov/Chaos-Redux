"""Mathematical reference tests for a proposed design, NOT HOI4 validation.

Uses Python integers/Decimal and in-memory records. No game APIs, native save
parser, Clausewitz evaluator, multiplayer runner, or MCP connection is involved.
Run: python 094_half_gone_reference_model.py
"""
from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
from pathlib import Path
import io
import json
import random
import unittest


def half_count_loss(count: int, odd_bit: int) -> int:
    """One fixed rounding choice. An odd count has two equiprobable losses."""
    if type(count) is not int or count < 0 or odd_bit not in (0, 1):
        raise ValueError('Expected a nonnegative integer and a rounding bit.')
    return count // 2 + (odd_bit if count % 2 else 0)


def half_scalar(value: Decimal) -> Decimal:
    if not value.is_finite() or value < 0:
        raise ValueError('Only finite nonnegative owned quantities qualify.')
    return value / 2


def population_losses(states: dict[int, int], seed: int) -> dict[int, int]:
    """National rounding and uniform residual assignment to odd states."""
    if any(type(v) is not int or v < 0 for v in states.values()):
        raise ValueError('Population inputs must be nonnegative integers.')
    rng = random.Random(seed)
    result = {key: value // 2 for key, value in states.items()}
    odd = sorted(key for key, value in states.items() if value % 2)
    rng.shuffle(odd)
    total = sum(states.values())
    loss = half_count_loss(total, rng.randrange(2))
    residue = loss - sum(result.values())
    assert 0 <= residue <= len(odd)
    for key in odd[:residue]:
        result[key] += 1
    return result


def eligible_union(majors: set[str], humans: set[str], live: set[str],
                   carriers: set[str]) -> list[str]:
    return sorted((majors | humans) & live - carriers)


def extra_families(chaos: int, enabled: set[int]) -> set[str]:
    result: set[str] = set()
    for tier, threshold, family in ((1, 200, 'reserves'),
                                    (2, 400, 'national'),
                                    (3, 600, 'people')):
        if chaos >= threshold and tier in enabled:
            result.add(family)
    return result


def normalized(weights: dict[str, int], present: set[str]) -> dict[str, Fraction]:
    selected = {k: v for k, v in weights.items() if k in present and v > 0}
    total = sum(selected.values())
    return {k: Fraction(v, total) for k, v in selected.items()} if total else {}


def nonconflicting_categories(categories: dict[str, frozenset[str]],
                              selected: str) -> set[str]:
    claimed = categories[selected]
    return {key for key, members in categories.items()
            if key != selected and members.isdisjoint(claimed)}


def commit_once(incident: str, current: Decimal,
                receipts: dict[str, dict[str, str]]) -> Decimal:
    if incident in receipts:
        return current  # Do not reset a replenished reserve to its old receipt.
    after = half_scalar(current)
    receipts[incident] = {'before': str(current), 'after': str(after)}
    return after


def restoration_grant(before: Decimal, lost: Decimal, current: Decimal) -> Decimal:
    if min(before, lost, current) < 0:
        raise ValueError('Negative restoration input.')
    return min(lost, max(Decimal(0), before - current))


def chaos_increment(old_mark: int, actual_severity: int) -> tuple[int, int]:
    new_mark = max(old_mark, actual_severity)
    return new_mark, new_mark - old_mark


class ReferenceTests(unittest.TestCase):
    def test_integer_bounds_and_unbiased_pair(self):
        for n in range(10001):
            low, high = half_count_loss(n, 0), half_count_loss(n, 1)
            self.assertEqual(low + high, n)
            self.assertTrue(0 <= low <= high <= n)
            self.assertLessEqual(high - low, 1)

    def test_last_identity_is_not_immune_or_always_lost(self):
        self.assertEqual({half_count_loss(1, b) for b in (0, 1)}, {0, 1})

    def test_scalar_percentages_and_rejection(self):
        self.assertEqual(half_scalar(Decimal('0.8')), Decimal('0.4'))
        self.assertEqual(half_scalar(Decimal('0.2')), Decimal('0.1'))
        self.assertEqual(half_scalar(Decimal('95')), Decimal('47.5'))
        for value in (Decimal('-1'), Decimal('NaN'), Decimal('Infinity')):
            with self.assertRaises(ValueError):
                half_scalar(value)

    def test_population_national_and_local_bounds(self):
        rng = random.Random(94004)
        for trial in range(500):
            states = {i: rng.randrange(0, 10_000_000_001)
                      for i in range(rng.randrange(0, 101))}
            losses = population_losses(states, trial)
            self.assertEqual(set(losses), set(states))
            self.assertLessEqual(abs(2 * sum(losses.values()) - sum(states.values())), 1)
            for key, value in states.items():
                self.assertTrue(0 <= losses[key] <= value)
                self.assertLessEqual(abs(2 * losses[key] - value), 1)

    def test_population_reproducible_fixed_draw(self):
        states = {1: 1, 2: 3, 3: 5, 4: 7, 5: 9, 6: 0}
        self.assertEqual(population_losses(states, 94), population_losses(states, 94))
        self.assertEqual(population_losses({}, 0), {})

    def test_country_union_deduplicates_human_major(self):
        self.assertEqual(eligible_union({'A', 'B', 'SYSTEM'}, {'A', 'C', 'DEAD'},
                                        {'A', 'B', 'C', 'SYSTEM'}, {'SYSTEM'}),
                         ['A', 'B', 'C'])

    def test_thresholds_and_independent_settings(self):
        all_enabled = {1, 2, 3, 4}
        for chaos, expected in ((199, set()), (200, {'reserves'}),
                                (399, {'reserves'}), (400, {'reserves', 'national'}),
                                (599, {'reserves', 'national'}),
                                (600, {'reserves', 'national', 'people'})):
            self.assertEqual(extra_families(chaos, all_enabled), expected)
        self.assertEqual(extra_families(800, {1, 2, 4}), {'reserves', 'national'})
        self.assertEqual(extra_families(800, {4}), set())
        self.assertEqual(extra_families(600, {3}), {'people'})
        self.assertEqual(extra_families(100, all_enabled), set())

    def test_family_reference_probability_is_conditional(self):
        weights = {'reserves': 35, 'national': 35, 'people': 30}
        all_present = normalized(weights, set(weights))
        self.assertEqual(all_present['people'] * Fraction(1, 4), Fraction(3, 40))
        only_people = normalized(weights, {'people'})
        self.assertEqual(only_people['people'], 1)
        self.assertEqual(normalized(weights, set()), {})

    def test_aliases_and_role_overlap_excluded(self):
        categories = {'scientists': frozenset({'person_a', 'person_b'}),
                      'advisors': frozenset({'person_a', 'person_c'}),
                      'admirals': frozenset({'person_d'}),
                      'fuel': frozenset({'fuel_stock'})}
        self.assertEqual(nonconflicting_categories(categories, 'scientists'),
                         {'admirals', 'fuel'})
        stocks = {'baseline': frozenset({'train0', 'tank_variant_foreign'}),
                  'trains': frozenset({'train0'}),
                  'free_convoys': frozenset({'separate_convoy_reserve'})}
        self.assertEqual(nonconflicting_categories(stocks, 'baseline'), {'free_convoys'})

    def test_current_repeat_and_duplicate_after_replenishment(self):
        receipts: dict[str, dict[str, str]] = {}
        self.assertEqual(commit_once('first', Decimal(100), receipts), Decimal(50))
        self.assertEqual(commit_once('first', Decimal(80), receipts), Decimal(80))
        self.assertEqual(commit_once('second', Decimal(80), receipts), Decimal(40))
        self.assertEqual(receipts['first']['before'], '100')
        self.assertEqual(receipts['second']['before'], '80')
        plain: dict[str, dict[str, str]] = {}
        a = commit_once('a', Decimal(100), plain)
        self.assertEqual(commit_once('b', a, plain), Decimal(25))

    def test_reference_receipt_json_roundtrip(self):
        receipts: dict[str, dict[str, str]] = {}
        current = commit_once('sample', Decimal(100), receipts)
        restored = json.loads(json.dumps(receipts))
        self.assertEqual(commit_once('sample', current, restored), current)
        self.assertEqual(restored, receipts)

    def test_restoration_deficit_and_loss_limits(self):
        self.assertEqual(restoration_grant(Decimal(100), Decimal(50), Decimal(70)), Decimal(30))
        self.assertEqual(restoration_grant(Decimal(100), Decimal(50), Decimal(0)), Decimal(50))
        self.assertEqual(restoration_grant(Decimal(100), Decimal(50), Decimal(120)), Decimal(0))

    def test_severity_high_water_not_repeated_reward(self):
        mark = total = 0
        for severity in (5, 5, 10, 5, 15, 20, 20):
            mark, delta = chaos_increment(mark, severity)
            total += delta
        self.assertEqual((mark, total), (20, 20))

    def test_model_does_not_mutate_fielded_fixture(self):
        stock = {('rifle', 'old', 'foreign'): 9, ('train', 'base', 'domestic'): 10}
        fielded = {('rifle', 'old', 'foreign'): 91, ('train', 'base', 'domestic'): 30}
        original = fielded.copy()
        after = {key: count - half_count_loss(count, 1) for key, count in stock.items()}
        self.assertEqual(fielded, original)
        self.assertEqual(after[('rifle', 'old', 'foreign')], 4)
        self.assertEqual(after[('train', 'base', 'domestic')], 5)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ReferenceTests)
    log = io.StringIO()
    result = unittest.TextTestRunner(stream=log, verbosity=2).run(suite)
    report = {
        'evidence_class': 'Python mathematical reference model only',
        'native_HOI4_validation': False,
        'MCP_executed': False,
        'subagents_executed': 0,
        'tests_run': result.testsRun,
        'failures': len(result.failures),
        'errors': len(result.errors),
        'successful': result.wasSuccessful(),
        'limits': ['Python integers do not prove native precision',
                   'JSON roundtrip is not a native save-game test',
                   'Fixture separation is not native issued-equipment proof',
                   'No multiplayer or dispatcher timing test'],
        'test_log': log.getvalue(),
    }
    target = Path(__file__).with_name('094_half_gone_reference_results.json')
    target.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(log.getvalue())
    raise SystemExit(0 if result.wasSuccessful() else 1)
