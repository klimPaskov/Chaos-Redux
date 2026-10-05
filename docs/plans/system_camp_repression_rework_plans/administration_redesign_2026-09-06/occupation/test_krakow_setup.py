"""Source wiring checks for the paid post-cutover German detention-site route.

These checks establish reachability and separation of actions, not engine behavior.
"""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[5]
TRIGGERS = (ROOT / "common/scripted_triggers/camp_administration_country_triggers.txt").read_text()
EFFECTS = (ROOT / "common/scripted_effects/camp_administration_country_effects.txt").read_text()
DECISIONS = (ROOT / "common/decisions/camp_administration_country_decisions.txt").read_text()
UI_EFFECTS = (ROOT / "common/scripted_effects/camp_administration_ui_effects.txt").read_text()
LOC = (ROOT / "localisation/english/camp_administration_country_l_english.yml").read_text(encoding="utf-8-sig")
HISTORY_LOC = (ROOT / "localisation/english/camp_administration_ui_l_english.yml").read_text(encoding="utf-8-sig")


def block(source, name, next_name):
    return source.split(name + " = {", 1)[1].split(next_name + " = {", 1)[0]


class KrakowSetupTests(unittest.TestCase):
    def test_context_and_spending_are_separate_for_ai_budget(self):
        context = block(TRIGGERS, "camp_admin_ger_krakow_setup_context", "camp_admin_ger_krakow_setup_eligible")
        eligible = block(TRIGGERS, "camp_admin_ger_krakow_setup_eligible", "camp_admin_country_regime_valid")
        self.assertIn("date > 1943.5.29", context)
        self.assertIn("88 = {", context)
        self.assertIn("is_controlled_by = PREV", context)
        self.assertIn("NOT = { concentration_camp > 0 }", context)
        self.assertIn("NOT = { has_variable = genocide_responsible_country }", context)
        self.assertNotIn("camp_admin_budget", context)
        self.assertIn("camp_admin_ger_krakow_setup_context = yes", eligible)
        self.assertIn("camp_admin_budget.development", eligible)
        budget = EFFECTS.split("camp_admin_country_prepare_ai_budget = {", 1)[1]
        self.assertIn("camp_admin_ger_krakow_setup_context = yes", budget)
        self.assertIn("camp_admin_set_budget = yes", budget)

    def test_one_paid_detention_action_is_shared_by_human_and_ai(self):
        setup = block(EFFECTS, "camp_admin_ger_establish_krakow_site", "camp_admin_country_ai_ger_radical_mandate")
        decision = block(DECISIONS, "camp_admin_ger_establish_krakow_site", "camp_admin_ger_economic_authority")
        monthly = block(EFFECTS, "camp_admin_country_monthly", "camp_admin_country_action_1")
        # The site charges the Event 026 sale price of the ordinary build cost and credits one purchase.
        self.assertIn("global.black_friday_price_genocide_decision_cost_build_concentration", setup)
        self.assertNotIn("constant:genocide_decision_cost.build_concentration", setup)
        self.assertEqual(setup.count("black_friday_credit_political_power_purchase = yes"), 1)
        self.assertLess(setup.index("add_political_power = camp_admin_krakow_setup_debit"), setup.index("genocide_ensure_concentration_camp_level = yes"))
        self.assertIn("camp_rework_site_type.detention", setup)
        self.assertNotIn("genocide_auschwitz_experiment_site", setup)
        self.assertNotIn("genocide_register_extermination_site_for_root", setup)
        self.assertIn("camp_admin_ger_establish_krakow_site = yes", decision)
        self.assertIn("camp_admin_ger_establish_krakow_site = yes", monthly)
        self.assertIn("camp_admin_ger_krakow_site_established", setup)
        self.assertIn("camp_admin_ger_krakow_site_established", TRIGGERS)

    def test_later_killing_role_is_a_separately_paid_command(self):
        ai = block(EFFECTS, "camp_admin_country_ai_krakow_killing_role", "camp_admin_country_initialize")
        role = block(UI_EFFECTS, "camp_admin_set_selected_role", "camp_admin_toggle_selected_work")
        mandate = block(EFFECTS, "camp_admin_country_ai_ger_radical_mandate", "camp_admin_country_ai_krakow_killing_role")
        self.assertIn("camp_admin_set_mandate = yes", mandate)
        self.assertIn("camp_admin_mandate.radical", ai)
        self.assertIn("camp_admin_set_selected_role = yes", ai)
        self.assertIn("camp_admin_role_quote_pp", role)
        self.assertIn("genocide_register_extermination_site_for_root = yes", role)
        self.assertNotIn("camp_admin_set_selected_role = yes", block(EFFECTS, "camp_admin_ger_establish_krakow_site", "camp_admin_country_ai_ger_radical_mandate"))

    def test_quote_and_records_keys_resolve(self):
        for key in (
            "camp_admin_ger_establish_krakow_site", "camp_admin_ger_establish_krakow_site_desc",
            "camp_admin_ger_krakow_site_requirements_tt", "camp_admin_ger_krakow_site_cost",
            "camp_admin_ger_krakow_site_cost_blocked", "camp_admin_ger_krakow_site_cost_tooltip",
            "camp_admin_ger_krakow_site_effect_tt",
        ):
            self.assertRegex(LOC, r"(?m)^" + re.escape(key) + r': "')
        self.assertRegex(HISTORY_LOC, r'(?m)^camp_admin_history_site_established: "')


if __name__ == "__main__":
    unittest.main()
