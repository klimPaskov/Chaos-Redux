"""Bounded physical/custody conservation scenarios; source checks are not engine proof."""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[5]
SOURCE = (ROOT / "common/scripted_effects/camp_administration_occupation_effects.txt").read_text()
FOUNDATION = (ROOT / "common/scripted_effects/camp_administration_effects.txt").read_text()
MAJOR = (ROOT / "common/scripted_effects/camp_repression_major_country_effects.txt").read_text()
DECISIONS = (ROOT / "common/decisions/genocide_crisis_decisions.txt").read_text()
TRIGGERS = (ROOT / "common/scripted_triggers/camp_administration_occupation_triggers.txt").read_text()
LOCALISATION = (ROOT / "localisation/english/chaosx_decisions_l_english.yml").read_text(encoding="utf-8-sig")
SCRIPTED_LOCALISATION = (ROOT / "common/scripted_localisation/camp_administration_country_localisation.txt").read_text()


class Scenario:
    def __init__(self):
        self.source_population = 200_000
        self.destination_population = 200_000
        self.source_occupation = 100_000
        self.destination_occupation = 0
        self.destination_custody = 20_000
        self.origin = 87
        self.authority = "GER"
        self.custody_rows = []
        self.deaths = []
        self.rollback_failed = False

    def transfer(self, requested, source_debit=None, destination_credit=None, bind=True,
                 source_commit=True, custody_inverse=True):
        if self.rollback_failed or requested <= 0 or requested > self.source_occupation:
            return False
        source_debit = requested if source_debit is None else source_debit
        self.source_population -= source_debit
        credited = 0
        if source_debit == requested:
            credited = requested if destination_credit is None else destination_credit
            self.destination_population += credited
        bound = requested if credited == requested and bind else 0
        if bound:
            self.destination_custody += bound
            self.custody_rows.append([self.origin, self.authority, bound])
        if source_debit == credited == bound == requested and source_commit:
            self.source_occupation -= requested
            return True
        if bound:
            if not custody_inverse:
                self.rollback_failed = True
                return False
            self.destination_custody -= bound
            self.custody_rows[-1][2] = 0
        self.destination_population -= credited
        self.source_population += source_debit
        return False

    def custody_death(self, amount):
        row = self.custody_rows[-1]
        assert 0 < amount <= row[2]
        row[2] -= amount
        self.destination_custody -= amount
        self.destination_population -= amount
        self.deaths.append((88, row[0], row[1], amount))


class OccupationCustodyTransferTests(unittest.TestCase):
    def test_exact_bind_moves_membership_once_without_destination_occupation(self):
        s = Scenario()
        before = s.source_population + s.destination_population
        self.assertTrue(s.transfer(10_000))
        self.assertEqual((s.source_population, s.destination_population), (190_000, 210_000))
        self.assertEqual(s.source_occupation, 90_000)
        self.assertEqual(s.destination_custody, 30_000)
        self.assertEqual(s.destination_occupation, 0)
        self.assertEqual(sum(row[2] for row in s.custody_rows), 10_000)
        self.assertEqual(s.source_population + s.destination_population, before)
        self.assertEqual(s.deaths, [])

    def test_short_source_debit_restores_source_without_destination_bind(self):
        s = Scenario()
        self.assertFalse(s.transfer(10_000, source_debit=8_000))
        self.assertEqual((s.source_population, s.destination_population, s.destination_custody), (200_000, 200_000, 20_000))
        self.assertEqual(s.source_occupation, 100_000)
        self.assertEqual(s.custody_rows, [])

    def test_short_destination_credit_reverses_both_physical_receipts(self):
        s = Scenario()
        self.assertFalse(s.transfer(10_000, destination_credit=8_000))
        self.assertEqual((s.source_population, s.destination_population, s.destination_custody), (200_000, 200_000, 20_000))
        self.assertEqual(s.source_occupation, 100_000)

    def test_rejected_bind_reverses_physical_without_membership_change(self):
        s = Scenario()
        self.assertFalse(s.transfer(10_000, bind=False))
        self.assertEqual((s.source_population, s.destination_population, s.destination_custody), (200_000, 200_000, 20_000))
        self.assertEqual(s.custody_rows, [])

    def test_postbind_source_failure_inverses_custody_before_population(self):
        s = Scenario()
        self.assertFalse(s.transfer(10_000, source_commit=False))
        self.assertEqual((s.source_population, s.destination_population, s.destination_custody), (200_000, 200_000, 20_000))
        self.assertEqual(s.custody_rows[-1][2], 0)
        self.assertEqual(s.source_occupation, 100_000)

    def test_failed_custody_inverse_quarantines_physical_rollback(self):
        s = Scenario()
        self.assertFalse(s.transfer(10_000, source_commit=False, custody_inverse=False))
        self.assertTrue(s.rollback_failed)
        self.assertEqual((s.source_population, s.destination_population), (190_000, 210_000))
        self.assertEqual(s.destination_custody, 30_000)
        self.assertFalse(s.transfer(10_000))

    def test_later_destination_death_uses_origin_row_and_one_entry(self):
        s = Scenario()
        self.assertTrue(s.transfer(10_000))
        s.custody_death(1_000)
        self.assertEqual(s.deaths, [(88, 87, "GER", 1_000)])
        self.assertEqual(s.source_population, 190_000)
        self.assertEqual(s.destination_population, 209_000)
        self.assertEqual(s.destination_custody, 29_000)

    def test_two_origins_remain_distinct_in_one_custody_destination(self):
        s = Scenario()
        self.assertTrue(s.transfer(10_000))
        s.origin = 86
        self.assertTrue(s.transfer(5_000))
        self.assertEqual(s.custody_rows, [[87, "GER", 10_000], [86, "GER", 5_000]])
        self.assertEqual(s.destination_custody, 35_000)
        self.assertEqual(s.destination_occupation, 0)
        s.custody_death(1_000)
        self.assertEqual(s.custody_rows, [[87, "GER", 10_000], [86, "GER", 4_000]])
        self.assertEqual(s.deaths, [(88, 86, "GER", 1_000)])

    def test_source_order_and_foundation_contract(self):
        body = SOURCE.split("camp_occ_transfer_to_custody_exact = {", 1)[1].split("camp_occ_commit_transfer_to_custody = {", 1)[0]
        self.assertLess(body.index("camp_admin_preflight_import = yes"), body.index("camp_occ_apply_population_debit = yes"))
        self.assertLess(body.index("camp_occ_apply_population_debit = yes"), body.index("camp_occ_apply_population_credit = yes"))
        self.assertLess(body.index("camp_occ_apply_population_credit = yes"), body.index("camp_admin_bind_import = yes"))
        self.assertLess(body.index("camp_admin_bind_import = yes"), body.index("camp_occ_commit_transfer_to_custody = yes"))
        rollback = SOURCE.split("camp_occ_rollback_custody_transaction = {", 1)[1].split("camp_occ_transfer_to_custody_exact = {", 1)[0]
        self.assertLess(rollback.index("camp_admin_inverse_import_bind = yes"), rollback.index("camp_occ_apply_population_debit = yes"))
        self.assertNotIn("chaos_meter_register_deaths", body)
        self.assertNotIn("camp_occ_append_row = yes", body)
        self.assertIn("camp_admin_import_bind_pending_inverse", FOUNDATION)

    def test_dated_lodz_route_uses_live_membership_and_capacity(self):
        match = re.search(r"lodz_auschwitz_living_share\s*=\s*([0-9.]+)",
                          (ROOT / "common/script_constants/camp_administration_occupation_constants.txt").read_text())
        self.assertIsNotNone(match)
        living_share = float(match.group(1))
        s = Scenario()
        free_capacity = 20_000
        requested = round(min(s.source_occupation * living_share, free_capacity))
        before = s.source_population + s.destination_population
        self.assertTrue(s.transfer(requested))
        self.assertEqual(requested, 20_000)
        self.assertEqual(s.source_occupation, 80_000)
        self.assertEqual(s.destination_custody, 40_000)
        self.assertEqual(s.source_population + s.destination_population, before)
        self.assertEqual(s.deaths, [])
        s.custody_death(1_000)
        self.assertEqual(s.deaths, [(88, 87, "GER", 1_000)])
        self.assertEqual(s.source_population + s.destination_population, before - 1_000)

    def test_paid_manual_order_uses_living_row_and_pays_after_receipt(self):
        constants = (ROOT / "common/script_constants/camp_administration_occupation_constants.txt").read_text()
        share = float(re.search(r"manual_auschwitz_living_share\s*=\s*([0-9.]+)", constants)[1])
        s = Scenario()
        requested = min(int(s.source_occupation * share), 20_000)
        self.assertEqual(requested, 5_000)
        before = s.source_population + s.destination_population
        self.assertTrue(s.transfer(requested))
        self.assertEqual(s.source_population + s.destination_population, before)
        self.assertEqual(s.custody_rows, [[87, "GER", requested]])
        self.assertEqual(s.deaths, [])
        s.custody_death(1_000)
        self.assertEqual(s.deaths, [(88, 87, "GER", 1_000)])
        self.assertEqual(s.source_population + s.destination_population, before - 1_000)
        ordered = SOURCE.split("camp_occ_try_manual_auschwitz_transfer = {", 1)[1].split("camp_occ_try_lodz_auschwitz_transfer = {", 1)[0]
        paid = MAJOR.split("camp_rework_germany_apply_exact_cohort_transfer = {", 1)[1].split("camp_rework_germany_assign_rail_capacity = {", 1)[0]
        self.assertIn("camp_occ_custody_row_id = camp_occ_native_row_id", ordered)
        self.assertIn("var:camp_occ_manual_source_state_id = { camp_occ_manual_transfer_live_source_ready = yes }", ordered)
        self.assertIn("camp_occ_custody_row_before_k", ordered)
        self.assertIn("camp_occ_manual_share_headroom_k", ordered)
        self.assertIn("camp_occ_manual_source_margin_limit", ordered)
        self.assertIn("max = camp_occ_custody_source_aggregate_people", ordered)
        self.assertIn("camp_occ_value.manual_order_minimum_people", ordered)
        self.assertIn("camp_admin_value.maximum_population_share", ordered)
        self.assertIn("camp_occ_transfer_to_custody_exact = yes", ordered)
        self.assertNotIn("camp_occ_custody_requested_people = state_population_k", ordered)
        self.assertNotIn("migration_execute_forced_transfer_exact", ordered)
        self.assertLess(paid.index("camp_occ_try_manual_auschwitz_transfer = yes"), paid.index("add_equipment_to_stockpile = { type = support_equipment_1"))
        self.assertIn("camp_occ_custody_result = constant:camp_occ_value.transfer_valid", paid)
        self.assertIn("camp_occ_custody_committed_people > 0", paid)
        share_source = (ROOT / "common/script_constants/camp_administration_constants.txt").read_text()
        maximum_share = float(re.search(r"maximum_population_share\s*=\s*([0-9.]+)", share_source)[1])
        full_share = Scenario()
        full_share.destination_custody = int(full_share.destination_population * maximum_share)
        self.assertEqual(max(0, int(full_share.destination_population * maximum_share) - full_share.destination_custody), 0)
        self.assertEqual(full_share.custody_rows, [])

    def test_manual_decision_uses_one_availability_quote_and_success_payment(self):
        decision = DECISIONS.split("germany_transfer_prisoners_to_experiment_site = {", 1)[1].split("genocide_restricted_chemical_site_escalation = {", 1)[0]
        paid = MAJOR.split("camp_rework_germany_apply_exact_cohort_transfer = {", 1)[1].split("camp_rework_germany_assign_rail_capacity = {", 1)[0]
        cost = TRIGGERS.split("camp_occ_manual_transfer_can_pay = {", 1)[1]
        self.assertIn("custom_cost_trigger = { camp_occ_manual_transfer_can_pay = yes }", decision)
        self.assertIn("custom_cost_text = germany_transfer_prisoners_to_experiment_site_cost", decision)
        self.assertIn("ai_hint_pp_cost = @GENOCIDE_TRANSFER_AI_PP_HINT", decision)
        self.assertIn("camp_occ_manual_transfer_country_prerequisites_ready = yes", decision)
        self.assertIn("camp_occ_manual_transfer_any_source_ready = yes", decision)
        self.assertIn("88 = { camp_occ_manual_transfer_destination_ready = yes }", decision)
        self.assertIn("camp_occ_manual_transfer_can_pay = yes", decision)
        self.assertIn("camp_rework_germany_apply_exact_cohort_transfer = yes", decision)
        self.assertNotIn("state_target =", decision)
        self.assertNotIn("target_trigger =", decision)
        self.assertNotIn("target_root_trigger =", decision)
        self.assertNotIn("camp_rework_country_under_ai_site_cap", decision)
        self.assertNotIn("camp_rework_country_under_ai_experiment_cap", decision)
        self.assertNotIn("cost = constant:genocide_decision_cost.german_experiment_transfer", decision)
        self.assertNotIn("migration_execute_forced_transfer_exact", decision)
        self.assertNotIn("camp_rework_germany_apply_prisoner_transfer = yes", decision)
        # The check and the payment read the same Event 026 sale prices.
        for term in ("global.black_friday_price_genocide_decision_cost_german_experiment_transfer ", "global.black_friday_price_genocide_decision_cost_german_experiment_transfer_army_xp",
                     "camp_rework_can_pay_support_equipment = yes", "camp_rework_can_pay_trains = yes"):
            self.assertIn(term, cost)
        for term in ("global.black_friday_price_genocide_decision_cost_german_experiment_transfer ", "global.black_friday_price_genocide_decision_cost_german_experiment_transfer_army_xp",
                     "global.black_friday_price_camp_rework_equipment_cost_support_equipment", "global.black_friday_price_camp_rework_equipment_cost_trains"):
            self.assertIn(term, paid)
        self.assertEqual(paid.count("camp_rework_credit_sale_order = yes"), 1)
        self.assertLess(paid.index("camp_occ_custody_result = constant:camp_occ_value.transfer_valid"), paid.index("add_political_power = camp_occ_manual_transfer_debit_pp"))
        self.assertLess(paid.index("camp_occ_custody_committed_people > 0"), paid.index("add_equipment_to_stockpile = { type = support_equipment_1"))
        self.assertEqual(paid.count("add_equipment_to_stockpile = { type = support_equipment_1"), 1)
        self.assertEqual(paid.count("add_equipment_to_stockpile = { type = train_equipment_1"), 1)
        self.assertNotIn("add_manpower", paid)
        self.assertIn("genocide_activate_crisis = yes", paid)
        self.assertIn("genocide_escalation = constant:genocide_crisis_value.terror_escalation", paid)
        self.assertIn("hidden_atrocity_score = constant:genocide_crisis_value.foreign_experimentation_hidden_atrocity", paid)
        self.assertNotIn("germany_mengele_add_cloning_project_progress", paid)
        for key in ("germany_transfer_prisoners_to_experiment_site", "germany_transfer_prisoners_to_experiment_site_desc",
                    "germany_transfer_prisoners_to_experiment_site_cost", "germany_transfer_prisoners_to_experiment_site_cost_blocked",
                    "germany_transfer_prisoners_to_experiment_site_cost_tooltip", "germany_transfer_prisoners_to_experiment_site_requirements_tt",
                    "germany_transfer_prisoners_to_experiment_site_source_tt", "germany_transfer_prisoners_to_experiment_site_destination_tt",
                    "germany_transfer_prisoners_to_experiment_site_effect_tt"):
            self.assertRegex(LOCALISATION, r"(?m)^" + key + r': "')
        self.assertIn("[This.GetCampOccManualTransferCostStatus]", LOCALISATION)
        self.assertRegex(LOCALISATION, r'(?m)^germany_transfer_prisoners_to_experiment_site_cost_blocked: "\[This\.GetCampOccManualTransferCostStatus\]"')
        self.assertIn("name = GetCampOccManualTransferCostStatus", SCRIPTED_LOCALISATION)
        self.assertIn("[This.GetCampOccManualSourceName]", LOCALISATION)
        self.assertIn("name = GetCampOccManualSourceName", SCRIPTED_LOCALISATION)
        for key in ("camp_occ_manual_transfer_short_pp", "camp_occ_manual_transfer_short_xp",
                    "camp_occ_manual_transfer_short_support", "camp_occ_manual_transfer_short_trains",
                    "camp_occ_manual_transfer_cost_ready"):
            self.assertRegex(LOCALISATION, r"(?m)^" + key + r': "')
            self.assertIn("localization_key = " + key, SCRIPTED_LOCALISATION)

    def test_manual_route_is_dated_and_requires_a_live_occupied_source(self):
        prerequisites = TRIGGERS.split("camp_occ_manual_transfer_country_prerequisites_ready = {", 1)[1].split("camp_occ_manual_transfer_country_ready = {", 1)[0]
        country = TRIGGERS.split("camp_occ_manual_transfer_country_ready = {", 1)[1].split("camp_occ_manual_transfer_destination_ready = {", 1)[0]
        destination = TRIGGERS.split("camp_occ_manual_transfer_destination_ready = {", 1)[1].split("camp_occ_manual_transfer_source_ready = {", 1)[0]
        source = TRIGGERS.split("camp_occ_manual_transfer_source_ready = {", 1)[1].split("camp_occ_manual_transfer_can_pay = {", 1)[0]
        for required in ("has_country_flag = camp_admin_initialized", "original_tag = GER", "camp_occ_authority_has_campaign = yes",
                         "date > 1943.5.29", "germany_mengele_program_active = yes", "germany_mengele_restricted_program_active = yes"):
            self.assertIn(required, prerequisites)
        self.assertIn("camp_occ_manual_transfer_any_source_ready = yes", country)
        killing_site = TRIGGERS.split("camp_occ_killing_destination_active = {", 1)[1].split("camp_occ_manual_transfer_destination_ready = {", 1)[0]
        for required in ("state = 88", "camp_admin_site_is_operational = yes", "extermination_camp > 0",
                         "camp_admin_role.killing", "camp_admin_support_ratio"):
            self.assertIn(required, killing_site)
        for required in ("camp_occ_killing_destination_active = yes", "camp_admin_site_rows_reconciled = yes",
                         "camp_occ_manual_destination_free_k", "camp_occ_manual_destination_share_k",
                         "camp_occ_manual_destination_uncommitted_k", "camp_occ_value.manual_order_minimum_people"):
            self.assertIn(required, destination)
        for required in ("camp_occ_state_has_current_authority = yes", "camp_occ_native_row_id > 0",
                         "camp_occ_remaining_k", "is_on_continent = europe", "NOT = { is_core_of = GER }",
                         "original_tag = GER"):
            self.assertIn(required, source)
        self.assertNotIn("is_germany_core_prisoner_source_fallback", source)

    def test_compact_national_order_selects_oldest_valid_row_and_refreshes_on_change(self):
        selector = SOURCE.split("camp_occ_refresh_manual_transfer_source = {", 1)[1].split("camp_occ_try_manual_auschwitz_transfer = {", 1)[0]
        country = TRIGGERS.split("camp_occ_manual_transfer_country_ready = {", 1)[1].split("camp_occ_manual_transfer_destination_ready = {", 1)[0]
        self.assertIn("clear_variable = camp_occ_manual_source_state_id", selector)
        self.assertIn("array = camp_occ_states", selector)
        self.assertIn("PREV = { NOT = { has_variable = camp_occ_manual_source_state_id } }", selector)
        self.assertIn("camp_occ_preflight_custody_source = yes", selector)
        self.assertIn("camp_occ_custody_source_valid = constant:camp_occ_value.transfer_valid", selector)
        self.assertIn("camp_occ_value.manual_order_minimum_people", selector)
        self.assertIn("camp_occ_value.manual_auschwitz_living_share", selector)
        self.assertIn("set_variable = { camp_occ_manual_source_state_id = PREV }", selector)
        self.assertIn("camp_occ_manual_transfer_any_source_ready = yes", country)
        self.assertIn("camp_occ_manual_transfer_live_source_ready = yes", selector)
        self.assertIn("camp_occ_manual_source_margin_limit", selector)
        self.assertIn("max = camp_occ_custody_source_aggregate_people", selector)
        self.assertIn("camp_occ_refresh_manual_transfer_source = yes", SOURCE.split("camp_occ_monthly_country = {", 1)[1])
        self.assertIn("camp_occ_refresh_manual_transfer_source = yes", SOURCE.split("camp_occ_on_state_control_changed = {", 1)[1])
        self.assertIn("clear_variable = camp_occ_manual_source_state_id", SOURCE.split("camp_occ_close_country = {", 1)[1])
        enrollment = SOURCE.split("camp_occ_register_cohort = {", 1)[1].split("camp_occ_backfill_cohort_origin = {", 1)[0]
        self.assertLess(enrollment.index("camp_occ_native_row_id = camp_occ_appended_row_id"), enrollment.index("camp_occ_refresh_manual_transfer_source = yes"))
        paid = MAJOR.split("camp_rework_germany_apply_exact_cohort_transfer = {", 1)[1].split("camp_rework_germany_assign_rail_capacity = {", 1)[0]
        self.assertLess(paid.index("camp_occ_refresh_manual_transfer_source = yes"), paid.index("camp_occ_try_manual_auschwitz_transfer = yes"))
        self.assertLess(paid.index("camp_admin_record_history = yes"), paid.rindex("camp_occ_refresh_manual_transfer_source = yes"))
        self.assertIn("any_of_scopes = {", SCRIPTED_LOCALISATION)
        self.assertIn("camp_occ_manual_transfer_live_source_ready = yes", SCRIPTED_LOCALISATION)
        self.assertIn("camp_occ_manual_display_source = THIS", SCRIPTED_LOCALISATION)
        constants = (ROOT / "common/script_constants/camp_administration_occupation_constants.txt").read_text()
        share = float(re.search(r"manual_auschwitz_living_share\s*=\s*([0-9.]+)", constants)[1])
        minimum_people = int(re.search(r"manual_order_minimum_people\s*=\s*(\d+)", constants)[1])
        first_meaningful_row = round(minimum_people / share)
        self.assertLess(int((first_meaningful_row - 1) * share), minimum_people)
        self.assertGreaterEqual(int(first_meaningful_row * share), minimum_people)

    def test_manual_order_skips_a_one_person_valid_row_without_full_order_headroom(self):
        constants = (ROOT / "common/script_constants/camp_administration_occupation_constants.txt").read_text()
        share = float(re.search(r"manual_auschwitz_living_share\s*=\s*([0-9.]+)", constants)[1])
        minimum = int(re.search(r"manual_order_minimum_people\s*=\s*(\d+)", constants)[1])
        living_rows = [(100_000, 950), (60_000, 2_001)]
        eligible = [min(int(living * share), margin - 1, living) >= minimum for living, margin in living_rows]
        self.assertEqual(eligible, [False, True])
        self.assertFalse(999 >= minimum)
        self.assertTrue(1_000 >= minimum)
        live = TRIGGERS.split("camp_occ_manual_transfer_live_source_ready = {", 1)[1].split("camp_occ_manual_transfer_any_source_ready = {", 1)[0]
        destination = TRIGGERS.split("camp_occ_manual_transfer_destination_ready = {", 1)[1].split("camp_occ_manual_transfer_source_ready = {", 1)[0]
        selector = SOURCE.split("camp_occ_refresh_manual_transfer_source = {", 1)[1].split("camp_occ_try_manual_auschwitz_transfer = {", 1)[0]
        ordered = SOURCE.split("camp_occ_try_manual_auschwitz_transfer = {", 1)[1].split("camp_occ_try_lodz_auschwitz_transfer = {", 1)[0]
        self.assertIn("camp_occ_manual_source_margin_people", live)
        self.assertIn("camp_occ_manual_row_probe_people", live)
        self.assertIn("camp_occ_manual_source_margin_limit", selector)
        self.assertIn("camp_occ_manual_source_margin_limit", ordered)
        self.assertIn("camp_occ_manual_destination_free_k", destination)
        self.assertIn("camp_occ_value.manual_order_minimum_people", destination)

    def test_repeated_manual_orders_stop_at_real_destination_headroom(self):
        constants = (ROOT / "common/script_constants/camp_administration_occupation_constants.txt").read_text()
        share = float(re.search(r"manual_auschwitz_living_share\s*=\s*([0-9.]+)", constants)[1])
        s = Scenario()
        initial = s.source_population + s.destination_population
        free_capacity = 20_000
        paid_orders = 0
        for _ in range(8):
            requested = min(int(s.source_occupation * share), free_capacity)
            if requested > 0 and s.transfer(requested):
                free_capacity -= requested
                paid_orders += 1
        self.assertEqual(free_capacity, 0)
        self.assertLess(paid_orders, 8)
        self.assertEqual(sum(row[2] for row in s.custody_rows), 20_000)
        self.assertEqual(s.source_population + s.destination_population, initial)
        self.assertEqual(s.deaths, [])

    def test_manual_and_dated_lodz_orders_consume_the_same_living_row(self):
        constants = (ROOT / "common/script_constants/camp_administration_occupation_constants.txt").read_text()
        manual_share = float(re.search(r"manual_auschwitz_living_share\s*=\s*([0-9.]+)", constants)[1])
        dated_share = float(re.search(r"lodz_auschwitz_living_share\s*=\s*([0-9.]+)", constants)[1])
        s = Scenario()
        before = s.source_population + s.destination_population
        manual = int(s.source_occupation * manual_share)
        self.assertTrue(s.transfer(manual))
        dated = int(s.source_occupation * dated_share)
        self.assertTrue(s.transfer(dated))
        self.assertEqual(s.source_occupation, 100_000 - manual - dated)
        self.assertEqual(sum(row[2] for row in s.custody_rows), manual + dated)
        self.assertEqual(s.source_population + s.destination_population, before)
        self.assertEqual(s.deaths, [])

    def test_dated_route_source_gates_and_bounded_arrival_waves(self):
        body = SOURCE.split("camp_occ_try_lodz_auschwitz_transfer = {", 1)[1].split("camp_occ_monthly_country = {", 1)[0]
        monthly = SOURCE.split("camp_occ_monthly_country = {", 1)[1]
        for required in (
            "original_tag = GER", "date > 1944.8.8", "date < 1944.10.1",
            "NOT = { has_country_flag = camp_occ_lodz_auschwitz_transfer_recorded }",
            "camp_occ_authority_has_campaign = yes", "87 = {", "88 = {",
            "camp_occ_state_has_current_authority = yes",
            "camp_occ_killing_destination_active = yes", "camp_admin_support_ratio",
            "non_damaged_building_level@extermination_camp", "camp_occ_arrival.max_batches_per_month",
            "camp_occ_preflight_custody_source = yes", "camp_occ_transfer_to_custody_exact = yes",
            "set_country_flag = camp_occ_lodz_auschwitz_transfer_recorded", "camp_occ_lodz_pending_people",
            "camp_occ_lodz_source_row_id", "camp_occ_apply_killing_arrival_loss = yes",
            "camp_admin_history_kind.killing_center_transfer",
        ):
            self.assertIn(required, body)
        self.assertLess(monthly.index("camp_occ_try_lodz_auschwitz_transfer = yes"),
                        monthly.index("set_temp_variable = { camp_occ_month_row_index"))
        self.assertNotIn("chaos_meter_register_deaths", body)
        self.assertNotIn("camp_occ_record_deaths", body)
        self.assertLess(body.index("camp_occ_transfer_to_custody_exact = yes"), body.index("camp_occ_apply_killing_arrival_loss = yes"))
        self.assertLess(body.index("camp_occ_custody_result = constant:camp_occ_value.transfer_valid", body.index("camp_occ_transfer_to_custody_exact = yes")),
                        body.index("camp_occ_apply_killing_arrival_loss = yes"))
        arrival = SOURCE.split("camp_occ_apply_killing_arrival_loss = {", 1)[1].split("camp_occ_try_lodz_auschwitz_transfer = {", 1)[0]
        self.assertIn("camp_admin_death_row_id = camp_occ_custody_bound_row_id", arrival)
        self.assertIn("camp_admin_arrival_phase_contract = constant:camp_admin_value.one", arrival)
        self.assertIn("camp_occ_arrival_actual_k = camp_admin_death_actual_k", arrival)
        self.assertNotIn("camp_admin_month_arrival_deaths_k", arrival)
        self.assertEqual(body.count("camp_admin_record_history = yes"), 1)
        self.assertIn("camp_occ_lodz_monthly_moved_people > 0", body)
        self.assertLess(body.index("camp_occ_lodz_monthly_moved_people = camp_occ_custody_committed_people"),
                        body.index("camp_admin_record_history = yes"))


class ManualTransferSalePriceTests(unittest.TestCase):
    """The manual order checks and pays the Event 026 sale price through production bodies.

    The exact custody receipt has its own occupation suites; here it is a declared
    accepted result, so only the price check, payment and purchase credit run.
    """

    @staticmethod
    def runtime(ratio):
        import sys
        sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
        import black_friday_sale_prices as sale
        from foundation_source_tests import Runtime, parse, get

        class PaymentRuntime(Runtime):
            def execute(self, block, scope, previous=None):
                pending = []
                for key, op, value in block:
                    if key == "add_equipment_to_stockpile":
                        if pending:
                            super().execute(pending, scope, previous)
                            pending = []
                        stock = self.scopes[scope].setdefault("equipment", {})
                        kind = get(value, "type")
                        stock[kind] = stock.get(kind, 0) + self.val(get(value, "amount"), scope, previous)
                    else:
                        pending.append((key, op, value))
                if pending:
                    super().execute(pending, scope, previous)

        r = PaymentRuntime()
        r.country("GER")
        r.state("S1", "GER")
        sale.install(r, ratio)
        for path, categories in (("common/script_constants/genocide_crisis_constants.txt", ("genocide_crisis_value",)),
                                 ("common/script_constants/camp_repression_rework_constants.txt", ("camp_rework_germany", "camp_rework_country_value"))):
            for category, _, body in parse((ROOT / path).read_text(encoding="utf-8-sig")):
                if category in categories:
                    for key, _, value in body:
                        if key != "schema" and not isinstance(value, list):
                            r.constants[category + "." + key] = float(value)
        major = {key: value for key, _, value in parse(MAJOR) if not key.startswith("@")}
        r.effects["camp_rework_germany_apply_exact_cohort_transfer"] = major["camp_rework_germany_apply_exact_cohort_transfer"]
        r.triggers["camp_occ_manual_transfer_can_pay"] = get(parse(TRIGGERS), "camp_occ_manual_transfer_can_pay")
        r.effects["camp_occ_refresh_manual_transfer_source"] = []
        r.effects["camp_occ_try_manual_auschwitz_transfer"] = [
            ("set_temp_variable", "=", [("camp_occ_custody_result", "=", "constant:camp_occ_value.transfer_valid")]),
            ("set_temp_variable", "=", [("camp_occ_custody_committed_people", "=", "100")])]
        for name in ("genocide_activate_crisis", "camp_rework_register_evidence_state", "camp_rework_recalculate_country_values"):
            r.effects[name] = []
        r.triggers["is_germany_occupied_poland_prisoner_source"] = [("always", "=", "no")]
        ger = r.scopes["GER"]
        ger.update(political_power=100, army_experience=20, camp_occ_manual_source_state_id="S1",
                   equipment={"support_equipment_1": 500, "train_equipment_1": 50})
        return r, ger, sale

    def test_manual_order_checks_pays_and_credits_the_sale_price(self):
        for ratio in (10000, 5000, 2500):
            r, ger, sale = self.runtime(ratio)
            pp = sale.price(r, "german_experiment_transfer", "genocide_decision_cost")
            xp = sale.price(r, "german_experiment_transfer_army_xp", "genocide_decision_cost")
            support, trains = sale.stock(r, "support_equipment"), sale.stock(r, "trains")
            if ratio < 10000:
                self.assertLess(pp + support + trains, 35 + 180 + 18)
            exact = dict(political_power=pp, army_experience=xp, equipment={"support_equipment_1": support, "train_equipment_1": trains})
            ger.update(exact)
            self.assertTrue(r.cond([("camp_occ_manual_transfer_can_pay", "=", "yes")], "GER"))
            for field, kind in (("political_power", None), ("army_experience", None), ("equipment", "support_equipment_1"), ("equipment", "train_equipment_1")):
                ger.update(political_power=pp, army_experience=xp, equipment={"support_equipment_1": support, "train_equipment_1": trains})
                if kind:
                    ger[field][kind] -= 1
                else:
                    ger[field] -= 0.001 if field == "political_power" else 1
                self.assertFalse(r.cond([("camp_occ_manual_transfer_can_pay", "=", "yes")], "GER"), (ratio, field, kind))
            ger.update(political_power=100, army_experience=20, equipment={"support_equipment_1": 500, "train_equipment_1": 50})
            r.run("camp_rework_germany_apply_exact_cohort_transfer", "GER")
            self.assertAlmostEqual(ger["political_power"], 100 - pp)
            self.assertAlmostEqual(ger["army_experience"], 20 - xp)
            self.assertEqual(ger["equipment"], {"support_equipment_1": 500 - support, "train_equipment_1": 50 - trains})
            self.assertEqual(sale.credits(r), 1)
            self.assertEqual(sale.last_family(r), sale.family(r, "equipment"))


if __name__ == "__main__":
    unittest.main()
