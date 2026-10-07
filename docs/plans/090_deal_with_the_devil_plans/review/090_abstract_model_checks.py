"""Abstract checks for selected Event 090 design invariants.

This is not HOI4 script, an engine emulator, or a live-game validation suite.
It deliberately omits territory, timing queues, diplomacy, actual disease state,
assets, costs, probability calibration, and the shared system implementations.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
import unittest

@dataclass(frozen=True)
class State:
    accepted: int = 0
    clean_refusals: int = 0
    phase: str = "courtship"
    reconsidered: bool = False
    side_history: int = 0
    person_changes: int = 0
    active_institutions: int = 0
    delivered_benefits: frozenset[str] = frozenset()

LIVE = {"courtship", "patronage", "reconsideration"}

def accept_main(state: State, benefit: str, *, delivered: bool = True,
                has_evidence: bool = False, evidence_days: int = 0) -> State:
    if state.phase not in LIVE or not 0 <= state.accepted < 5:
        raise ValueError("No principal acceptance is available in this state.")
    if not delivered or not benefit:
        raise ValueError("A failed principal promise cannot count as fulfilled.")
    if benefit in state.delivered_benefits:
        raise ValueError("The same principal delivery cannot be paid twice.")
    if state.accepted == 4 and (not has_evidence or evidence_days < 60):
        raise ValueError("The final offer is not permitted before counterplay.")
    count = state.accepted + 1
    return replace(state, accepted=count,
                   phase="peaceful_possession" if count == 5 else "patronage",
                   active_institutions=state.active_institutions + 1,
                   delivered_benefits=state.delivered_benefits | {benefit})

def refuse(state: State) -> State:
    if state.phase not in LIVE:
        raise ValueError("No principal offer is pending in this phase.")
    if state.accepted == 0:
        count = state.clean_refusals + 1
        if count > 5:
            raise ValueError("Clean courtship has already closed.")
        return replace(state, clean_refusals=count,
                       phase="manifestation_pending" if count == 5 else "courtship")
    if state.accepted == 1:
        return replace(state, reconsidered=True,
                       phase="early_settlement_pending" if state.reconsidered else "reconsideration")
    if state.accepted in (2, 3):
        return replace(state, phase="partial_settlement_pending")
    if state.accepted == 4:
        return replace(state, phase="major_confrontation_pending")
    raise ValueError("No post-possession early refusal route exists.")

def side_favor(state: State) -> State:
    # Cumulative resolved favors; this is not concurrent open-favor capacity.
    return replace(state, side_history=state.side_history + 1)

def unsigned_gift(state: State, *, explicitly_adopted: bool = False,
                  benefit: str = "unsigned_principal", **kwargs) -> State:
    return accept_main(state, benefit, **kwargs) if explicitly_adopted else state

def change_leader(state: State) -> State:
    return replace(state, person_changes=state.person_changes + 1)

def settle_early(state: State) -> State:
    if state.accepted != 1:
        raise ValueError("This abstract operation covers the early route only.")
    # Real sacrifice removes active institutional authority, not delivered cures.
    return replace(state, phase="closed_after_settlement", active_institutions=0)

def accept_n(state: State, n: int) -> State:
    for i in range(n):
        state = accept_main(state, f"principal_{state.accepted + 1}",
                            has_evidence=True, evidence_days=60)
    return state

class DesignInvariantTests(unittest.TestCase):
    def test_five_acceptances_are_peaceful(self):
        state = accept_n(State(), 5)
        self.assertEqual(state.accepted, 5)
        self.assertEqual(state.phase, "peaceful_possession")
        self.assertNotIn("civil_war", state.phase)

    def test_early_refusals_do_not_consume_acceptances(self):
        for prefix in range(5):
            with self.subTest(clean_refusals=prefix):
                state = State()
                for _ in range(prefix):
                    state = refuse(state)
                state = accept_n(state, 5)
                self.assertEqual(state.phase, "peaceful_possession")
                self.assertEqual(state.accepted, 5)

    def test_total_clean_refusal_has_no_infiltrated_institutions(self):
        state = State()
        for _ in range(5):
            state = refuse(state)
        self.assertEqual(state.phase, "manifestation_pending")
        self.assertEqual(state.accepted, 0)
        self.assertEqual(state.active_institutions, 0)
        with self.assertRaises(ValueError):
            accept_main(state, "late_sixth_bid")

    def test_partial_refusals_retain_distinct_routes(self):
        expected = {1: "reconsideration", 2: "partial_settlement_pending",
                    3: "partial_settlement_pending", 4: "major_confrontation_pending"}
        for count, phase in expected.items():
            with self.subTest(accepted=count):
                self.assertEqual(refuse(accept_n(State(), count)).phase, phase)
        self.assertEqual(refuse(refuse(accept_n(State(), 1))).phase,
                         "early_settlement_pending")

    def test_resolved_side_favors_never_advance_main_count(self):
        for count in range(5):
            state = accept_n(State(), count)
            for _ in range(100):
                state = side_favor(state)
            self.assertEqual(state.accepted, count)
            self.assertNotEqual(state.phase, "peaceful_possession")

    def test_unsigned_receipt_requires_explicit_adoption(self):
        state = State()
        self.assertEqual(unsigned_gift(state), state)
        self.assertEqual(unsigned_gift(state, explicitly_adopted=True).accepted, 1)

    def test_failed_or_duplicate_delivery_cannot_count(self):
        original = State()
        with self.assertRaises(ValueError):
            accept_main(original, "promise", delivered=False)
        self.assertEqual(original.accepted, 0)
        delivered = accept_main(original, "promise")
        with self.assertRaises(ValueError):
            accept_main(delivered, "promise")
        self.assertEqual(delivered.accepted, 1)

    def test_final_offer_requires_evidence_and_time(self):
        state = accept_n(State(), 4)
        for evidence, days in [(False, 0), (False, 60), (True, 0), (True, 59)]:
            with self.subTest(evidence=evidence, days=days):
                with self.assertRaises(ValueError):
                    accept_main(state, "final", has_evidence=evidence, evidence_days=days)
        self.assertEqual(accept_main(state, "final", has_evidence=True,
                                    evidence_days=60).phase, "peaceful_possession")

    def test_leader_change_does_not_reset_history_or_rewards(self):
        state = accept_n(State(), 3)
        successor = change_leader(state)
        self.assertEqual(successor.accepted, state.accepted)
        self.assertEqual(successor.delivered_benefits, state.delivered_benefits)
        self.assertEqual(successor.active_institutions, state.active_institutions)

    def test_early_settlement_preserves_delivered_cure(self):
        state = accept_main(State(), "genuine_cure")
        settled = settle_early(state)
        self.assertEqual(settled.active_institutions, 0)
        self.assertEqual(settled.accepted, 1)  # Historical acceptance is not erased.
        self.assertIn("genuine_cure", settled.delivered_benefits)
        with self.assertRaises(ValueError):
            accept_main(settled, "repeat_reward")

if __name__ == "__main__":
    unittest.main(verbosity=2)
