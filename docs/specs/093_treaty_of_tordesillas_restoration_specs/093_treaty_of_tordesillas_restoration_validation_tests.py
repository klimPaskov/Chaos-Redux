#!/usr/bin/env python3
"""Synthetic design-rule tests for Event 093. Not HOI4 implementation or engine proof.

Run with Python 3.10+: python <this_file.py> --json <results.json>
Only the standard library is used. No game files or network are accessed.
"""
from __future__ import annotations
import argparse
import json
import math
import unittest
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from types import MappingProxyType
from typing import Mapping, Sequence


def f(value: int | float | str | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(str(value))


def sphere(longitude: int | float | Fraction) -> str:
    """Half-open abstract longitude rule, not a game projection converter."""
    position = (f(longitude) + f('46.5')) % 360
    return 'POR' if position < 180 else 'SPA'


def state_sphere(samples: Sequence[tuple[float, float]], representative: float,
                 stable_id: int) -> str:
    if not samples or any(area <= 0 for _, area in samples):
        raise ValueError('Positive represented land areas are required')
    area = {'POR': Fraction(0), 'SPA': Fraction(0)}
    for longitude, amount in samples:
        area[sphere(longitude)] += f(amount)
    if area['POR'] != area['SPA']:
        return max(area, key=area.get)
    position = (f(representative) + f('46.5')) % 360
    if position in (0, 180):
        return 'POR' if stable_id % 2 == 0 else 'SPA'
    return sphere(representative)


@dataclass(frozen=True)
class BaselineState:
    state_id: int
    population: int
    land: int
    industry: int


class FrozenWeights:
    """Immutable synthetic weights for one sphere, excluding protected states upstream."""
    def __init__(self, states: Sequence[BaselineState]):
        if not states or len({s.state_id for s in states}) != len(states):
            raise ValueError('Nonempty unique state set required')
        if any(min(s.population, s.land, s.industry) < 0 for s in states):
            raise ValueError('Negative components are invalid')
        totals = [sum(getattr(s, k) for s in states)
                  for k in ('population', 'land', 'industry')]
        base = [f('0.50'), f('0.25'), f('0.25')]
        active = [j for j, total in enumerate(totals) if total > 0]
        if not active:
            raise ValueError('At least one nonzero component is required')
        norm = sum(base[j] for j in active)
        values = {}
        for s in states:
            components = [s.population, s.land, s.industry]
            values[s.state_id] = sum(base[j] / norm * Fraction(components[j], totals[j])
                                     for j in active)
        self.weights: Mapping[int, Fraction] = MappingProxyType(values)

    def share(self, states: Sequence[int]) -> Fraction:
        return sum((self.weights[s] for s in set(states)), Fraction(0))


def consolidation(reach: float | Fraction, integration: float | Fraction) -> Fraction:
    c, i = f(reach), f(integration)
    if not (0 <= i <= c <= 1):
        raise ValueError('Integrated controlled share must be within actual reach')
    return 100 * min(Fraction(1), c / f('0.70'), i / f('0.40'))


def activation_ready(chaos: float, spanish: tuple[float, float],
                     portuguese: tuple[float, float], confidence: int = 65,
                     stable_days: int = 90, political_valid: bool = True,
                     stage_four: bool = True, both_consented: bool = True,
                     scenario_slot_free: bool = True) -> bool:
    return (f(chaos) > 1000 and consolidation(*spanish) == 100
            and consolidation(*portuguese) == 100 and confidence >= 65
            and stable_days >= 90 and political_valid and stage_four
            and both_consented and scenario_slot_free)


def aid_fulfillment(promised: Sequence[int], delivered: Sequence[int]) -> tuple[Fraction, bool]:
    if len(promised) != 3 or len(delivered) != 3 or min(promised) <= 0 or min(delivered) < 0:
        raise ValueError('Three positive promised and nonnegative delivered components required')
    ratios = [min(Fraction(1), Fraction(d, p)) for p, d in zip(promised, delivered)]
    score = 100 * sum(w * r for w, r in zip([f('.5'), f('.3'), f('.2')], ratios))
    return score, score >= 75 and all(r >= f('.5') for r in ratios)


def ceil_quantum(value: Fraction, quantum: int = 5) -> int:
    if quantum <= 0 or value < 0:
        raise ValueError('Invalid quantization input')
    return math.ceil(value / quantum) * quantum


def integration_tier(population: int, states: int) -> str:
    if population < 0 or not 1 <= states <= 12:
        raise ValueError('Outside the ordinary reviewed region envelope')
    pop_tier = 0 if population <= 5_000_000 else 1 if population <= 20_000_000 else 2
    state_tier = 0 if states <= 3 else 1 if states <= 8 else 2
    return ['small', 'medium', 'large'][max(pop_tier, state_tier)]


def project_duration(base_days: int, recently_conquered: bool = False,
                     coercive: bool = False, focus_acceleration: bool = False,
                     concentrated: bool = False) -> int:
    if base_days <= 0:
        raise ValueError('Duration must be positive')
    days = f(base_days + (60 if recently_conquered or coercive else 0))
    if focus_acceleration:
        days *= f('.8')
    if concentrated:
        days *= f('.85')
    return max(60, ceil_quantum(days))


@dataclass
class Receipt:
    actual_paid: int
    refunded: int = 0
    cancelled: bool = False

    def __post_init__(self) -> None:
        if self.actual_paid < 0:
            raise ValueError('Cannot pay a negative amount')

    def cancel(self, completion: float, kind: str = 'equipment') -> int:
        done = f(completion)
        if not 0 <= done <= 1:
            raise ValueError('Completion must be between zero and one')
        if self.cancelled:
            return 0
        self.cancelled = True
        if kind != 'equipment':
            return 0
        due = math.floor(Fraction(self.actual_paid) * (1 - done) / 2 / 5) * 5
        due = max(0, min(due, self.actual_paid - self.refunded))
        self.refunded += due
        return due


def safe_routine_restitution(owner: str, donor: str, correct_sphere: bool,
                             protected: bool = False, native_core: bool = False,
                             explicit_consent: bool = False, standing_consent: bool = False,
                             war_disputed: bool = False) -> bool:
    return (owner == donor and correct_sphere and not protected and not war_disputed
            and (explicit_consent or (standing_consent and not native_core)))


def safe_claim_removal(preexisting: bool, another_source: bool, unknown_provenance: bool) -> bool:
    return not (preexisting or another_source or unknown_provenance)


class GeographyTests(unittest.TestCase):
    def test_atlantic_boundary(self):
        self.assertEqual(sphere(-46.5), 'POR')
        self.assertEqual(sphere(-46.5001), 'SPA')
    def test_opposite_boundary(self):
        self.assertEqual(sphere(133.5), 'SPA')
        self.assertEqual(sphere(133.4999), 'POR')
    def test_longitude_wrap(self):
        for longitude in [-540, -180, 0, 180, 540]:
            self.assertEqual(sphere(longitude), sphere(longitude + 360))
    def test_equal_arc_sampling(self):
        assigned = [sphere(-180 + n) for n in range(360)]
        self.assertEqual(assigned.count('POR'), 180)
        self.assertEqual(assigned.count('SPA'), 180)
    def test_land_majority_not_country(self):
        self.assertEqual(state_sphere([(0, 60), (-90, 40)], -90, 1), 'POR')
    def test_tie_uses_representative(self):
        self.assertEqual(state_sphere([(0, 50), (-90, 50)], -90, 2), 'SPA')
    def test_exact_line_tie_is_stable(self):
        self.assertEqual(state_sphere([(0, 50), (-90, 50)], -46.5, 2), 'POR')
        self.assertEqual(state_sphere([(0, 50), (-90, 50)], -46.5, 3), 'SPA')
    def test_invalid_land_input(self):
        with self.assertRaises(ValueError):
            state_sphere([(0, -1)], 0, 1)


class WeightTests(unittest.TestCase):
    def setUp(self):
        self.rows = [BaselineState(1, 100, 10, 2), BaselineState(2, 300, 30, 6)]
        self.snapshot = FrozenWeights(self.rows)
    def test_weights_sum_to_one(self):
        self.assertEqual(sum(self.snapshot.weights.values()), 1)
    def test_proportionate_weights(self):
        self.assertEqual(self.snapshot.weights[1], f('.25'))
    def test_duplicate_state_not_counted_twice(self):
        self.assertEqual(self.snapshot.share([1, 1]), f('.25'))
    def test_population_loss_does_not_change_snapshot(self):
        self.rows[0] = BaselineState(1, 0, 10, 0)
        self.assertEqual(self.snapshot.weights[1], f('.25'))
    def test_zero_industry_component_renormalizes(self):
        snap = FrozenWeights([BaselineState(1, 100, 10, 0), BaselineState(2, 100, 30, 0)])
        self.assertEqual(sum(snap.weights.values()), 1)
        self.assertEqual(snap.weights[1], Fraction(5, 12))
    def test_weights_cannot_be_mutated(self):
        with self.assertRaises(TypeError):
            self.snapshot.weights[1] = Fraction(1)  # type: ignore[index]
    def test_duplicate_ids_rejected(self):
        with self.assertRaises(ValueError):
            FrozenWeights([self.rows[0], self.rows[0]])


class WorldEndTests(unittest.TestCase):
    def test_exact_entry_thresholds(self):
        self.assertTrue(activation_ready(1001, (.70, .40), (.70, .40)))
    def test_exactly_1000_is_not_above(self):
        self.assertFalse(activation_ready(1000, (.90, .70), (.90, .70)))
    def test_token_second_crown_fails(self):
        self.assertFalse(activation_ready(1200, (1, 1), (.10, .05)))
    def test_reach_without_integration_fails(self):
        self.assertFalse(activation_ready(1200, (1, .10), (1, .10)))
    def test_compact_core_empire_fails_reach(self):
        self.assertLess(consolidation(.40, .40), 100)
    def test_independent_political_gate(self):
        self.assertFalse(activation_ready(1200, (1, 1), (1, 1), political_valid=False))
    def test_human_refusal_blocks(self):
        self.assertFalse(activation_ready(1200, (1, 1), (1, 1), both_consented=False))
    def test_another_scenario_blocks(self):
        self.assertFalse(activation_ready(1200, (1, 1), (1, 1), scenario_slot_free=False))
    def test_stability_period_required(self):
        self.assertFalse(activation_ready(1200, (1, 1), (1, 1), stable_days=89))
    def test_confidence_required(self):
        self.assertFalse(activation_ready(1200, (1, 1), (1, 1), confidence=64))
    def test_stage_four_required(self):
        self.assertFalse(activation_ready(1200, (1, 1), (1, 1), stage_four=False))
    def test_impossible_component_order_rejected(self):
        with self.assertRaises(ValueError):
            consolidation(.3, .4)


class AidTests(unittest.TestCase):
    def test_full_delivery(self):
        self.assertEqual(aid_fulfillment([1000, 50, 5000], [1000, 50, 5000]), (100, True))
    def test_promise_without_delivery(self):
        self.assertEqual(aid_fulfillment([1000, 50, 5000], [0, 0, 0]), (0, False))
    def test_rifles_cannot_replace_other_components(self):
        self.assertEqual(aid_fulfillment([1000, 50, 5000], [10000, 0, 0]), (50, False))
    def test_exact_earning_boundary(self):
        self.assertEqual(aid_fulfillment([1000, 50, 5000], [1000, 25, 2500]), (75, True))
    def test_total_alone_is_insufficient(self):
        score, earned = aid_fulfillment([1000, 50, 5000], [1000, 50, 0])
        self.assertEqual(score, 80)
        self.assertFalse(earned)
    def test_overdelivery_is_capped(self):
        self.assertEqual(aid_fulfillment([1000, 50, 5000], [2000, 100, 10000]), (100, True))
    def test_invalid_promise_rejected(self):
        with self.assertRaises(ValueError):
            aid_fulfillment([1000, 0, 5000], [1000, 50, 5000])


class ProjectTests(unittest.TestCase):
    def test_small_boundary(self):
        self.assertEqual(integration_tier(5_000_000, 3), 'small')
    def test_higher_state_tier_applies(self):
        self.assertEqual(integration_tier(1_000_000, 9), 'large')
    def test_higher_population_tier_applies(self):
        self.assertEqual(integration_tier(21_000_000, 2), 'large')
    def test_unreviewed_large_region_rejected(self):
        with self.assertRaises(ValueError):
            integration_tier(100, 13)
    def test_recent_conquest_adds_time(self):
        self.assertEqual(project_duration(90, recently_conquered=True), 150)
    def test_recent_and_coercive_not_double_charged(self):
        self.assertEqual(project_duration(90, recently_conquered=True, coercive=True), 150)
    def test_acceleration_rounds_up_to_five(self):
        self.assertEqual(project_duration(90, focus_acceleration=True), 75)
    def test_factors_compose_before_rounding(self):
        self.assertEqual(project_duration(90, focus_acceleration=True, concentrated=True), 65)
    def test_minimum_duration(self):
        self.assertEqual(project_duration(30, focus_acceleration=True, concentrated=True), 60)


class TransactionTests(unittest.TestCase):
    def test_ordinary_refund_example(self):
        self.assertEqual(Receipt(100).cancel(.5), 25)
    def test_discounted_receipt_not_list_price(self):
        self.assertEqual(Receipt(50).cancel(.5), 10)
    def test_no_second_refund(self):
        receipt = Receipt(100)
        self.assertEqual(receipt.cancel(.5), 25)
        self.assertEqual(receipt.cancel(.5), 0)
    def test_political_power_nonrefundable(self):
        self.assertEqual(Receipt(100).cancel(.5, 'political_power'), 0)
    def test_transfer_not_duplicated_as_refund(self):
        self.assertEqual(Receipt(1000).cancel(0, 'delivered_transfer'), 0)
    def test_completed_project_no_refund(self):
        self.assertEqual(Receipt(100).cancel(1), 0)
    def test_enemy_owned_occupation_not_transferable(self):
        self.assertFalse(safe_routine_restitution('ENEMY', 'SPA', True, standing_consent=True))
    def test_native_core_needs_explicit_consent(self):
        self.assertFalse(safe_routine_restitution('SPA', 'SPA', True, native_core=True,
                                                 standing_consent=True))
        self.assertTrue(safe_routine_restitution('SPA', 'SPA', True, native_core=True,
                                                explicit_consent=True))
    def test_protected_homeland_not_routine_restitution(self):
        self.assertFalse(safe_routine_restitution('SPA', 'SPA', True, protected=True,
                                                 explicit_consent=True))
    def test_wrong_receiving_sphere_blocks(self):
        self.assertFalse(safe_routine_restitution('SPA', 'SPA', False, explicit_consent=True))
    def test_other_claim_source_preserved(self):
        self.assertFalse(safe_claim_removal(False, True, False))
    def test_uncertain_claim_provenance_preserved(self):
        self.assertFalse(safe_claim_removal(False, False, True))
    def test_sole_event_claim_can_be_removed(self):
        self.assertTrue(safe_claim_removal(False, False, False))


class RecordingResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.records = []
    def addSuccess(self, test):
        super().addSuccess(test)
        self.records.append({'test': test.id(), 'status': 'pass'})
    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.records.append({'test': test.id(), 'status': 'failure',
                             'detail': self._exc_info_to_string(err, test)})
    def addError(self, test, err):
        super().addError(test, err)
        self.records.append({'test': test.id(), 'status': 'error',
                             'detail': self._exc_info_to_string(err, test)})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path, help='Write the actual synthetic test results')
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.loadTestsFromModule(__import__(__name__))
    result = unittest.TextTestRunner(verbosity=2, resultclass=RecordingResult).run(suite)
    output = {'scope': 'Synthetic specification-rule tests only. No HOI4 engine or specialist proof.',
              'tests_run': result.testsRun, 'failures': len(result.failures),
              'errors': len(result.errors), 'skipped': len(result.skipped),
              'successful': result.wasSuccessful(), 'tests': result.records}
    if args.json:
        args.json.write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())
