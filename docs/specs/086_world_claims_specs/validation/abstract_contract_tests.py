"""Executable specification examples, NOT a HOI4 implementation or engine test.

Run with Python 3.10+: python validation/abstract_contract_tests.py
No third-party packages or game installation are used. These tests assume the
required claimant isolation and exact event-time observations can be represented.
They cannot prove those assumptions hold in Hearts of Iron IV.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from math import ceil, floor
from pathlib import Path
import json
import unittest


def up5(value: float) -> int:
    return 5 * ceil(value / 5)


def ring_limits(stage: int, frontier_count: int) -> list[int | None]:
    if stage not in range(6):
        raise ValueError('stage must be 0..5')
    if frontier_count <= 0:
        return []
    f = frontier_count
    if stage == 0:
        return [None]
    if stage == 1:
        return [None, min(20, max(5, up5(f / 4))) ]
    if stage in (2, 3):
        return [None, min(50, max(5, up5(f / 2))),
                min(25, max(5, up5(f / 4)))]
    return [None, None, min(100, max(5, up5(f))),
            min(50, max(5, up5(f / 2))),
            min(25, max(5, up5(f / 4)))]


def wave(graph: dict[int, set[int]], owners: dict[int, str | None],
         claimant: str, old_targets: set[int], stage: int) -> set[int]:
    """All inputs represent an immutable logical snapshot of *valid land* edges.

    Returns WC targets visited/selected by this firing, not owned territory.
    Sorted IDs replace the richer design ranking solely for reproducible tests.
    """
    owned = {s for s, owner in owners.items() if owner == claimant}

    def adjacent(states: set[int]) -> set[int]:
        return set().union(*(graph.get(s, set()) for s in states)) if states else set()

    def foreign(states: set[int]) -> set[int]:
        return {s for s in states if owners.get(s) is not None and owners[s] != claimant}

    first = foreign(adjacent(owned))
    if not first:
        return set()
    selected: set[int] = set()
    prior_layer = owned
    seen = set(owned)
    for budget in ring_limits(stage, len(first)):
        candidates = foreign(adjacent(prior_layer)) - seen
        existing = candidates & old_targets
        new = sorted(candidates - old_targets)
        accepted = existing | set(new if budget is None else new[:budget])
        selected |= accepted
        seen |= candidates  # rejected shortest-layer targets cannot reenter deeper
        prior_layer = accepted

    if stage == 5:
        # Critically uses only OLD provenance, never the just-selected targets.
        allowed = owned | old_targets
        reachable = set(owned)
        todo = set(owned)
        while todo:
            todo = (adjacent(todo) & allowed) - reachable
            reachable |= todo
        extension = foreign(adjacent(reachable)) - old_targets - selected
        limit = min(250, 100 + 25 * floor(len(owned) / 25))
        selected |= set(sorted(extension)[:limit])
    return selected


@dataclass
class Relationship:
    consumed_ceiling: int = 0
    control_start: int | None = None
    high_starts: dict[int, int | None] = field(
        default_factory=lambda: {80: None, 90: None, 95: None})

    def grant(self, current: int, ceiling: int, controls: bool,
              core: bool = False, context_ready: bool = True) -> int:
        if not (0 <= current <= 100 and 0 <= ceiling <= 100):
            raise ValueError('Compliance values must be 0..100')
        if core or not controls or not context_ready or ceiling <= self.consumed_ceiling:
            return current
        self.consumed_ceiling = ceiling
        return max(current, ceiling)

    def observe(self, day: int, controls: bool, compliance: int) -> None:
        """Requires exact observations at EVERY change, not periodic sampling."""
        if not controls:
            self.control_start = None
            self.high_starts = {80: None, 90: None, 95: None}
            return
        if self.control_start is None:
            self.control_start = day
        for threshold in self.high_starts:
            if compliance < threshold:
                self.high_starts[threshold] = None
            elif self.high_starts[threshold] is None:
                self.high_starts[threshold] = day

    def core_ready(self, day: int, stage: int, compliance: int,
                   controls: bool, credit: float = 0.0) -> bool:
        if not controls or self.control_start is None or stage not in (3, 4, 5):
            return False
        base, threshold, high_days, physical_min = {
            3: (360, 80, 60, 270), 4: (120, 90, 30, 90),
            5: (30, 95, 10, 25)}[stage]
        requirement = max(physical_min, up5(base * (1 - min(max(credit, 0), .25))))
        high_start = self.high_starts[threshold]
        return (compliance >= threshold and high_start is not None
                and day - self.control_start >= requirement
                and day - high_start >= high_days)


def percentage_met(numerator: int, denominator: int, percent: int) -> bool:
    return denominator > 0 and 100 * numerator >= percent * denominator


def assure(a_pp: int, b_pp: int, valid: bool = True) -> tuple[int, int, bool]:
    if not valid or a_pp < 25 or b_pp < 25:
        return a_pp, b_pp, False
    return a_pp - 25, b_pp - 25, True


def line_graph(size: int) -> dict[int, set[int]]:
    return {s: {n for n in (s-1, s+1) if 0 <= n < size} for s in range(size)}


class ContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.g = line_graph(30)
        self.o = {s: ('A' if s == 0 else 'B') for s in self.g}

    def test_01_baseline_immediate(self):
        self.assertEqual(wave(self.g, self.o, 'A', set(), 0), {1})

    def test_02_owned_conquest_moves_frontier(self):
        self.o[1] = 'A'
        self.assertEqual(wave(self.g, self.o, 'A', {1}, 0), {2})

    def test_03_control_does_not_enter_owned_input(self):
        # A hypothetical controller map is intentionally not a seed input.
        self.assertEqual(wave(self.g, self.o, 'A', {20}, 0), {1})

    def test_04_disconnected_owned_seed(self):
        self.o[20] = 'A'
        self.assertEqual(wave(self.g, self.o, 'A', set(), 0), {1, 19, 21})

    def test_05_no_land_neighbor_all_stages(self):
        for stage in range(6):
            self.assertEqual(wave({0: set(), 1: set()}, {0: 'A', 1: 'B'},
                                  'A', {1}, stage), set())

    def test_06_unowned_is_not_foreign(self):
        self.o[1] = None
        self.assertEqual(wave(self.g, self.o, 'A', set(), 5), set())

    def test_07_first_ring_uncapped(self):
        graph = {0: set(range(1, 151)), **{s: {0} for s in range(1,151)}}
        owners = {s: ('A' if s == 0 else 'B') for s in graph}
        self.assertEqual(len(wave(graph, owners, 'A', set(), 0)), 150)

    def test_08_stage_one_two_rings(self):
        self.assertEqual(wave(self.g, self.o, 'A', set(), 1), {1,2})

    def test_09_repeated_stage_one_not_recursive(self):
        old = wave(self.g, self.o, 'A', set(), 1)
        self.assertEqual(wave(self.g, self.o, 'A', old, 1), {1,2})

    def test_10_stage_two_three_rings(self):
        self.assertEqual(wave(self.g, self.o, 'A', set(), 2), {1,2,3})

    def test_11_stage_four_five_rings(self):
        self.assertEqual(wave(self.g, self.o, 'A', set(), 4), {1,2,3,4,5})

    def test_12_stage_five_fresh_network_not_seed(self):
        self.assertEqual(wave(self.g, self.o, 'A', set(), 5), {1,2,3,4,5})

    def test_13_stage_five_old_network_one_layer(self):
        self.assertEqual(wave(self.g, self.o, 'A', set(range(1,11)), 5),
                         {1,2,3,4,5,11})

    def test_14_detached_old_network_no_extension(self):
        result = wave(self.g, self.o, 'A', {20,21}, 5)
        self.assertNotIn(19, result)
        self.assertNotIn(22, result)

    def test_15_ring_budget_caps(self):
        self.assertEqual(ring_limits(1, 500), [None,20])
        self.assertEqual(ring_limits(2, 500), [None,50,25])
        self.assertEqual(ring_limits(4, 500), [None,None,100,50,25])

    def test_16_empty_frontier_budget(self):
        self.assertEqual(ring_limits(5, 0), [])

    def test_17_snapshot_order_invariance(self):
        first = {c: wave(self.g, self.o, c, set(), 2) for c in ['A','B']}
        second = {c: wave(self.g, self.o, c, set(), 2) for c in ['B','A']}
        self.assertEqual(first, second)

    def test_18_no_mutation_of_snapshot(self):
        before = dict(self.o)
        wave(self.g, self.o, 'A', set(), 5)
        self.assertEqual(before, self.o)

    def test_19_grant_floor(self):
        self.assertEqual(Relationship().grant(0, 25, True), 25)

    def test_20_grant_preserves_higher(self):
        r = Relationship()
        self.assertEqual(r.grant(90, 50, True), 90)
        self.assertEqual(r.consumed_ceiling, 50)

    def test_21_recapture_no_refill(self):
        r = Relationship(); r.grant(0, 25, True)
        self.assertEqual(r.grant(5, 25, True), 5)

    def test_22_upgrade_only_once(self):
        r = Relationship(); r.grant(0, 25, True)
        self.assertEqual(r.grant(10, 50, True), 50)
        self.assertEqual(r.grant(10, 50, True), 10)

    def test_23_equal_stage_ceilings_no_duplicate(self):
        r = Relationship(); r.grant(0, 75, True)
        self.assertEqual(r.grant(20, 75, True), 20)
        r.grant(20, 100, True)
        self.assertEqual(r.grant(20, 100, True), 20)

    def test_24_uncontrolled_entitlement_waits(self):
        r = Relationship()
        self.assertEqual(r.grant(0, 100, False), 0)
        self.assertEqual(r.consumed_ceiling, 0)

    def test_25_context_unready_waits(self):
        r = Relationship()
        self.assertEqual(r.grant(0, 50, True, context_ready=False), 0)
        self.assertEqual(r.consumed_ceiling, 0)

    def test_26_native_core_skips_grant(self):
        r = Relationship()
        self.assertEqual(r.grant(0, 75, True, core=True), 0)
        self.assertEqual(r.consumed_ceiling, 0)

    def test_27_separate_claimants_separate_records(self):
        # This proves only the model's separation, not native occupation isolation.
        a, b = Relationship(), Relationship()
        a.grant(0, 100, True)
        self.assertEqual(b.consumed_ceiling, 0)
        self.assertEqual(b.grant(0, 25, True), 25)

    def test_28_exact_stage_three_threshold(self):
        r=Relationship();r.observe(0,True,80)
        self.assertFalse(r.core_ready(359,3,80,True))
        self.assertTrue(r.core_ready(360,3,80,True))

    def test_29_exact_stage_four_threshold(self):
        r=Relationship();r.observe(0,True,100)
        self.assertFalse(r.core_ready(119,4,100,True))
        self.assertTrue(r.core_ready(120,4,100,True))

    def test_30_exact_stage_five_threshold(self):
        r=Relationship();r.observe(0,True,100)
        self.assertFalse(r.core_ready(0,5,100,True))
        self.assertFalse(r.core_ready(29,5,100,True))
        self.assertTrue(r.core_ready(30,5,100,True))

    def test_31_high_interval_independent(self):
        r=Relationship();r.observe(0,True,70);r.observe(355,True,80)
        self.assertFalse(r.core_ready(360,3,80,True))
        self.assertTrue(r.core_ready(415,3,80,True))

    def test_32_control_loss_resets(self):
        r=Relationship();r.observe(0,True,100);r.observe(29,False,100)
        r.observe(30,True,100)
        self.assertFalse(r.core_ready(31,5,100,True))
        self.assertTrue(r.core_ready(60,5,100,True))

    def test_33_threshold_dips_independent(self):
        r=Relationship();r.observe(0,True,100);r.observe(100,True,92)
        self.assertEqual(r.high_starts[80],0)
        self.assertEqual(r.high_starts[90],0)
        self.assertIsNone(r.high_starts[95])

    def test_34_stage_five_credit_physical_minimum(self):
        r=Relationship();r.observe(0,True,100)
        self.assertFalse(r.core_ready(24,5,100,True,.25))
        self.assertTrue(r.core_ready(25,5,100,True,.25))

    def test_35_credit_does_not_waive_high_interval(self):
        r=Relationship();r.observe(0,True,70);r.observe(269,True,80)
        self.assertFalse(r.core_ready(270,3,80,True,.25))

    def test_36_no_pre_core_stage(self):
        r=Relationship();r.observe(0,True,100)
        self.assertFalse(r.core_ready(1000,2,100,True))

    def test_37_inclusive_percentage(self):
        self.assertTrue(percentage_met(4,5,80))
        self.assertFalse(percentage_met(3,5,80))
        self.assertTrue(percentage_met(9,11,80))
        self.assertFalse(percentage_met(8,11,80))

    def test_38_empty_envelope_never_completes(self):
        self.assertFalse(percentage_met(0,0,80))

    def test_39_atomic_assurance_exact_price(self):
        self.assertEqual(assure(25,25),(0,0,True))

    def test_40_atomic_assurance_no_partial_charge(self):
        self.assertEqual(assure(24,100),(24,100,False))
        self.assertEqual(assure(100,24),(100,24,False))
        self.assertEqual(assure(100,100,False),(100,100,False))


class RecordedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.records: list[dict[str, str]] = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.records.append({'test':test.id(),'status':'passed_abstract_model_only'})

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.records.append({'test':test.id(),'status':'failed'})

    def addError(self, test, err):
        super().addError(test, err)
        self.records.append({'test':test.id(),'status':'error'})


if __name__ == '__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ContractTests)
    result=unittest.TextTestRunner(verbosity=2,resultclass=RecordedResult).run(suite)
    report={'status':'passed' if result.wasSuccessful() else 'failed',
            'scope':'Python abstract contract model only, not HOI4 engine validation',
            'tests_run':result.testsRun,'failures':len(result.failures),
            'errors':len(result.errors),'engine_gates_proven':[],
            'assumptions':['Adjacency input already contains only valid land edges.',
                           'Claimant records and native Compliance can be isolated.',
                           'Every control/Compliance change is observed at its exact time.',
                           'Snapshots and data structures in this model are available in Python, not asserted in HOI4.'],
            'cases':result.records}
    Path(__file__).with_name('abstract_test_results.json').write_text(
        json.dumps(report,indent=2)+'\n',encoding='utf-8')
    raise SystemExit(0 if result.wasSuccessful() else 1)
