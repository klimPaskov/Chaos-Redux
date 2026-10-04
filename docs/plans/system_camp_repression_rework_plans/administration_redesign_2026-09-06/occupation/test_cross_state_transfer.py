"""Accounting scenarios for the route-gated occupation transfer; not engine execution."""
from dataclasses import dataclass
from decimal import Decimal as D
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[5]
SOURCE = (ROOT / "common/scripted_effects/camp_administration_occupation_effects.txt").read_text()


@dataclass
class Row:
    root: int
    origin: int
    host: int
    authority: str
    living: D
    dead: D = D(0)
    released: D = D(0)
    moved_out: D = D(0)
    moved_in: D = D(0)


class Ledger:
    def __init__(self):
        self.population = {43: D(1000), 88: D(1000), 44: D(1000)}
        self.rows = [Row(1, 43, 43, "GER", D(300)), Row(2, 44, 44, "GER", D(200))]
        self.death_entries = []

    def move(self, row, destination, requested, credited=None, controlled=True):
        requested = D(requested)
        if not controlled or requested <= 0 or requested > row.living or requested != requested.to_integral_value():
            return False
        if self.population[row.host] - requested < D(".001"):
            return False
        credited = requested if credited is None else D(credited)
        source = row.host
        self.population[source] -= requested
        self.population[destination] += credited
        if credited != requested:
            self.population[destination] -= credited
            self.population[source] += requested
            return False
        row.living -= requested
        row.moved_out += requested
        self.rows.append(Row(row.root, row.origin, destination, row.authority, requested, moved_in=requested))
        return True

    def death(self, row, amount):
        amount = D(amount)
        assert 0 < amount <= row.living
        self.population[row.host] -= amount
        row.living -= amount
        row.dead += amount
        self.death_entries.append((row.host, row.origin, row.authority, amount))

    def release(self, host):
        for row in self.rows:
            if row.host == host:
                row.released += row.living
                row.living = D(0)


class CrossStateOccupationTests(unittest.TestCase):
    def test_partial_split_preserves_original_state_and_authority(self):
        ledger = Ledger()
        row = ledger.rows[0]
        self.assertTrue(ledger.move(row, 88, 100))
        self.assertEqual((row.living, ledger.rows[-1].living), (D(200), D(100)))
        self.assertEqual((ledger.rows[-1].root, ledger.rows[-1].origin, ledger.rows[-1].authority), (1, 43, "GER"))
        self.assertEqual((ledger.population[43], ledger.population[88]), (D(900), D(1100)))
        self.assertEqual(ledger.death_entries, [])

    def test_two_origins_at_one_destination_remain_distinct(self):
        ledger = Ledger()
        self.assertTrue(ledger.move(ledger.rows[0], 88, 100))
        self.assertTrue(ledger.move(ledger.rows[1], 88, 60))
        self.assertEqual({row.origin for row in ledger.rows if row.host == 88}, {43, 44})
        self.assertEqual(ledger.population[88], D(1160))

    def test_later_death_uses_actual_destination_once(self):
        ledger = Ledger()
        self.assertTrue(ledger.move(ledger.rows[0], 88, 100))
        ledger.death(ledger.rows[-1], 10)
        self.assertEqual(ledger.population[43], D(900))
        self.assertEqual(ledger.population[88], D(1090))
        self.assertEqual(ledger.death_entries, [(88, 43, "GER", D(10))])
        self.assertEqual(ledger.rows[0].dead, 0)

    def test_short_destination_credit_rolls_back_both_physical_states(self):
        ledger = Ledger()
        before = dict(ledger.population)
        self.assertFalse(ledger.move(ledger.rows[0], 88, 100, credited=80))
        self.assertEqual(ledger.population, before)
        self.assertEqual(len(ledger.rows), 2)
        self.assertEqual(ledger.death_entries, [])

    def test_capture_rejects_before_debit(self):
        ledger = Ledger()
        before = dict(ledger.population)
        self.assertFalse(ledger.move(ledger.rows[0], 88, 100, controlled=False))
        self.assertEqual(ledger.population, before)

    def test_release_does_not_restore_previous_death(self):
        ledger = Ledger()
        self.assertTrue(ledger.move(ledger.rows[0], 88, 100))
        ledger.death(ledger.rows[-1], 10)
        before = dict(ledger.population)
        ledger.release(88)
        self.assertEqual(ledger.population, before)
        self.assertEqual(ledger.rows[-1].released, 90)
        self.assertEqual(ledger.rows[-1].dead, 10)

    def test_annexation_releases_host_without_reassigning_original_authority(self):
        ledger = Ledger()
        self.assertTrue(ledger.move(ledger.rows[0], 88, 100))
        ledger.release(88)
        self.assertEqual(ledger.rows[-1].living, 0)
        self.assertEqual(ledger.rows[-1].released, 100)
        self.assertEqual((ledger.rows[-1].origin, ledger.rows[-1].authority), (43, "GER"))
        self.assertEqual(ledger.death_entries, [])

    def test_source_gates_receipts_before_metadata_and_no_transfer_death(self):
        transfer = SOURCE.split("camp_occ_transfer_survivors_exact = {", 1)[1].split("camp_occ_commit_transfer_rows = {", 1)[0]
        self.assertLess(transfer.index("camp_occ_apply_population_debit = yes"), transfer.index("camp_occ_apply_population_credit = yes"))
        self.assertLess(transfer.index("check_variable = { camp_occ_transfer_destination_credit_people = camp_occ_transfer_source_debit_people }"), transfer.index("camp_occ_commit_transfer_rows = yes"))
        self.assertIn("camp_occ_transfer_destination = { camp_occ_apply_population_debit = yes }", transfer)
        self.assertNotIn("chaos_meter_register_deaths", transfer)



if __name__ == "__main__":
    unittest.main()
