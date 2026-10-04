"""Focused source and arithmetic contract checks for destination custody rows; not engine execution."""
from dataclasses import dataclass
from decimal import Decimal as D
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[5]
SOURCE = (ROOT / "common/scripted_effects/camp_administration_effects.txt").read_text()


def helper(name):
    marker = name + " = {"
    start = SOURCE.index(marker)
    opening = SOURCE.index("{", start)
    depth = 0
    for offset in range(opening, len(SOURCE)):
        depth += (SOURCE[offset] == "{") - (SOURCE[offset] == "}")
        if depth == 0:
            return SOURCE[opening + 1:offset]
    raise AssertionError(f"unclosed helper: {name}")


@dataclass
class Row:
    origin: int
    authority: str
    root: int
    living: D
    dead: D = D(0)
    released: D = D(0)
    status: int = 1


class Site:
    def __init__(self):
        self.population = D(100)
        self.detainees = D(0)
        self.rows = []
        self.deaths = []

    def local_admit(self, amount):
        amount = D(amount)
        self.rows.append(Row(88, "GER", 0, amount))
        self.detainees += amount

    def import_bind(self, origin, root, amount):
        amount = D(amount)
        self.population += amount
        row = Row(origin, "GER", root, amount)
        self.rows.append(row)
        self.detainees += amount
        return row

    def inverse(self, row):
        if row.status != 1:
            return D(0)
        amount = row.living
        self.detainees -= amount
        self.population -= amount
        row.living = D(0)
        row.status = -1
        return amount

    def death(self, row, amount):
        amount = D(amount)
        assert row.status == 1 and D(0) < amount <= row.living
        self.population -= amount
        self.detainees -= amount
        row.living -= amount
        row.dead += amount
        self.deaths.append((88, row.origin, row.authority, amount))

    def release(self):
        for row in self.rows:
            row.released += row.living
            self.detainees -= row.living
            row.living = D(0)
        assert self.detainees == 0


class CustodyOriginRowsTests(unittest.TestCase):
    def test_preflight_is_side_effect_free_and_binds_to_measured_credit(self):
        preflight = helper("camp_admin_preflight_import")
        for mutation in ("set_variable =", "add_to_variable =", "subtract_from_variable =", "add_to_array =", "add_manpower =", "chaos_meter_register_deaths"):
            self.assertNotIn(mutation, preflight)
        bind = helper("camp_admin_bind_import")
        self.assertIn("camp_admin_import_after_people = camp_admin_import_requested_people", bind)
        self.assertLess(bind.index("camp_admin_import_after_people = camp_admin_import_requested_people"), bind.index("camp_admin_append_row = yes"))
        self.assertIn("camp_admin_import_preflight_origin = camp_admin_import_origin", bind)
        self.assertIn("camp_admin_import_preflight_root_id = camp_admin_import_occupation_root_id", bind)
        self.assertNotIn("add_manpower =", bind)
        self.assertNotIn("chaos_meter_register_deaths", bind)

    def test_local_admission_and_import_have_separate_origin_rows(self):
        admission = helper("camp_admin_admit_detainees")
        self.assertIn("camp_admin_append_origin = THIS", admission)
        self.assertIn("camp_admin_append_root_id = 0", admission)
        self.assertIn("camp_admin_append_row = yes", admission)
        bind = helper("camp_admin_bind_import")
        self.assertIn("camp_admin_append_origin = camp_admin_import_origin", bind)
        self.assertIn("camp_admin_append_root_id = camp_admin_import_occupation_root_id", bind)
        site = Site()
        imported = site.import_bind(87, 31, ".010")
        site.local_admit(".005")
        self.assertEqual([(row.origin, row.root, row.living) for row in site.rows], [(87, 31, D(".010")), (88, 0, D(".005"))])
        self.assertEqual(site.detainees, D(".015"))

    def test_destination_death_consumes_selected_origin_then_release_only_survivors(self):
        death = helper("camp_admin_record_deaths")
        self.assertIn("camp_admin_selected_row_id = camp_admin_death_row_id", death)
        self.assertLess(death.index("camp_admin_consume_rows = yes"), death.index("chaos_meter_register_deaths = yes"))
        self.assertEqual(death.count("chaos_meter_register_deaths = yes"), 1)
        release = helper("camp_admin_release_detainees")
        self.assertIn("camp_admin_consume_rows = yes", release)
        self.assertNotIn("add_manpower =", release)
        site = Site()
        imported = site.import_bind(87, 31, ".010")
        site.local_admit(".005")
        site.death(imported, ".003")
        before_release_population = site.population
        site.release()
        self.assertEqual(site.population, before_release_population)
        self.assertEqual((imported.dead, imported.released, imported.origin, imported.authority), (D(".003"), D(".007"), 87, "GER"))
        self.assertEqual(site.deaths, [(88, 87, "GER", D(".003"))])

    def test_two_documented_origins_keep_one_physical_movement_and_distinct_deaths(self):
        origins = {87: D(100), 11: D(80)}
        site = Site()
        initial_total = sum(origins.values()) + site.population
        for origin, root, moved in ((87, 31, D(".010")), (11, 32, D(".008"))):
            origins[origin] -= moved
            site.import_bind(origin, root, moved)
        self.assertEqual(sum(origins.values()) + site.population, initial_total)
        lodz, kaunas = site.rows
        site.death(lodz, ".003")
        site.death(kaunas, ".002")
        self.assertEqual(sum(origins.values()) + site.population, initial_total - D(".005"))
        self.assertEqual(site.deaths, [(88, 87, "GER", D(".003")), (88, 11, "GER", D(".002"))])
        before_release = site.population
        site.release()
        self.assertEqual(site.population, before_release)
        self.assertEqual([(row.origin, row.root, row.dead, row.released) for row in site.rows],
                         [(87, 31, D(".003"), D(".007")), (11, 32, D(".002"), D(".006"))])
        self.assertEqual(sum(row.dead + row.released for row in site.rows), D(".018"))

    def test_inverse_removes_only_same_chain_custody_addition_once(self):
        inverse = helper("camp_admin_inverse_import_bind")
        self.assertIn("camp_admin_row_ids^camp_admin_import_inverse_index = camp_admin_import_bound_row_id", inverse)
        self.assertIn("camp_admin_row_occupation_roots^camp_admin_import_inverse_index = camp_admin_import_occupation_root_id", inverse)
        self.assertIn("camp_admin_import_bind_pending_inverse = 0", inverse)
        self.assertNotIn("add_manpower =", inverse)
        site = Site()
        site.local_admit(".005")
        before = (site.population, site.detainees)
        imported = site.import_bind(87, 31, ".010")
        self.assertEqual(site.inverse(imported), D(".010"))
        self.assertEqual(site.inverse(imported), D(0))
        self.assertEqual((site.population, site.detainees), before)
        self.assertEqual(site.rows[0].living, D(".005"))


if __name__ == "__main__":
    unittest.main()
