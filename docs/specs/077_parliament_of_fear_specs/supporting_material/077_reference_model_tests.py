"""Run with Python. Results apply only to this abstract planning model."""
import importlib.util
from pathlib import Path
import random
import dataclasses
import unittest
import sys

spec = importlib.util.spec_from_file_location("reference077", Path(__file__).with_name("077_reference_model.py"))
model = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = model
spec.loader.exec_module(model)


def country(support=60, filled=100, paranoia=20):
    seats = [model.Seat(filled=i < filled, support="loyal" if i < support else "opposed") for i in range(100)]
    return model.Crisis(instance=1, seats=seats, paranoia=paranoia)


class PlanningInvariantTests(unittest.TestCase):
    def test_apportion_exact_conservation(self):
        rng = random.Random(77)
        for _ in range(1000):
            weights = [rng.randrange(1000) for _ in range(rng.randrange(6, 9))]
            self.assertEqual(sum(model.apportion(weights)), 100)
            self.assertTrue(all(x >= 0 for x in model.apportion(weights)))

    def test_apportion_zero_input_is_deterministic(self):
        self.assertEqual(model.apportion([0]*6), [17,17,17,17,16,16])

    def test_apportion_rejects_invalid(self):
        for values in ([], [1,-1], [1,1.5]):
            with self.assertRaises(ValueError):
                model.apportion(values)

    def test_accusation_keeps_support(self):
        c=country()
        c.accuse(0)
        self.assertEqual(c.support,60)
        self.assertEqual(c.seats[0].evidence,"accused")

    def test_clearing_opposition_does_not_make_it_loyal(self):
        c=country()
        c.seats[70].evidence="cleared"
        self.assertEqual(c.support,60)

    def test_purging_opposition_does_not_shrink_majority(self):
        c=country(support=45)
        c.purge(range(45,100))
        self.assertEqual(c.filled,45)
        self.assertFalse(c.has_majority())
        self.assertEqual(len(c.seats),100)

    def test_purging_supporters_loses_support(self):
        c=country()
        c.purge(range(10))
        self.assertEqual(c.support,50)
        self.assertEqual(c.filled,90)

    def test_suspension_loses_function_and_support(self):
        c=country()
        c.seats[0].suspended=True
        self.assertEqual((c.support,c.filled),(59,99))

    def test_appointment_restores_only_vacancy(self):
        c=country()
        c.purge([0])
        c.appoint(0,"dependable")
        self.assertEqual((c.support,c.filled),(60,100))
        with self.assertRaises(ValueError):
            c.appoint(0,"loyal")

    def test_original_truth_is_immutable(self):
        case=model.CaseIdentity("case1","fabricated","source1")
        with self.assertRaises(dataclasses.FrozenInstanceError):
            case.original_truth="genuine"

    def test_new_plot_keeps_original_case(self):
        c=country()
        c.cases["old"]=model.CaseIdentity("old","fabricated","oldsource")
        c.prepared_plot=True
        self.assertEqual(c.cases["old"].original_truth,"fabricated")

    def test_exact_affordability_and_single_debit(self):
        c=country()
        self.assertTrue(c.debit_once("a1",100))
        self.assertEqual(c.political_power,0)
        self.assertFalse(c.debit_once("a1",100))
        self.assertFalse(c.debit_once("a2",25))

    def test_zero_cost_action_is_still_single_commit(self):
        c=country()
        self.assertTrue(c.debit_once("review",0))
        self.assertFalse(c.debit_once("review",0))

    def test_safe_interval_closes_on_day21(self):
        c=country()
        for _ in range(20):
            self.assertFalse(c.advance_day())
        self.assertTrue(c.advance_day())
        self.assertFalse(c.active)

    def test_unsafe_day_resets_interval(self):
        c=country()
        for _ in range(20):
            c.advance_day()
        c.paranoia=25
        c.advance_day()
        self.assertEqual(c.safe_days,0)
        c.paranoia=20
        for _ in range(20):
            self.assertFalse(c.advance_day())

    def test_prepared_plot_blocks_closure(self):
        c=country()
        c.prepared_plot=True
        for _ in range(30):
            c.advance_day()
        self.assertTrue(c.active)
        self.assertEqual(c.safe_days,0)

    def test_filled_and_support_are_both_required(self):
        self.assertFalse(country(support=55,filled=79).safe_today())
        self.assertFalse(country(support=54,filled=100).safe_today())
        self.assertTrue(country(support=55,filled=80).safe_today())

    def test_cleanup_idempotent_and_history_preserved(self):
        c=country()
        c.persistent_history["recovery_tracker"]=True
        c.close()
        c.close()
        self.assertEqual(c.release_count,1)
        self.assertTrue(c.persistent_history["recovery_tracker"])

    def test_callback_requires_current_active_instance(self):
        c=country()
        self.assertTrue(c.callback_valid(1))
        c.instance=2
        self.assertFalse(c.callback_valid(1))
        c.close()
        self.assertFalse(c.callback_valid(2))

    def test_chaos_same_transaction_not_double_counted(self):
        ledger=model.ChaosLedger()
        self.assertEqual(ledger.add("wave1",5),5)
        self.assertEqual(ledger.add("wave1",5),0)
        self.assertEqual(ledger.added,5)

    def test_chaos_reversal_bounded_and_guarded(self):
        ledger=model.ChaosLedger()
        ledger.add("opening",2)
        self.assertEqual(ledger.reverse("closure",5),2)
        self.assertEqual(ledger.reverse("closure",5),0)
        self.assertEqual(ledger.reverse("another",5),0)
        self.assertEqual(ledger.reversed,ledger.added)

    def test_repeated_seat_mutations_conserve_capacity(self):
        rng=random.Random(77077)
        c=country()
        for _ in range(1000):
            i=rng.randrange(100)
            if c.seats[i].filled:
                c.purge([i])
            else:
                c.appoint(i,rng.choice(["loyal","dependable","uncertain","opposed"]))
            self.assertEqual(len(c.seats),100)
            self.assertLessEqual(c.support,c.filled)
            self.assertTrue(0 <= c.filled <= 100)


if __name__ == "__main__":
    unittest.main(verbosity=2)
