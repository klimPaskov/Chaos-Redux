"""Check the authorization source's resource budget, not live payment."""
import re
import unittest

from test_event025_final_recovery import ROOT, block


class AuthorizationBudgetTests(unittest.TestCase):
    def test_authorization_has_four_spendable_types_including_industry(self):
        raw = (ROOT / "common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt").read_text(encoding="utf-8-sig")
        source = re.sub(r"#[^\n]*", "", raw)
        executor = block("chaosx_nr25_execute_action", source)
        authorize = next(body for key, body in executor if key == "if" and
                         "constant:chaosx_nr25_action.authorize" in repr(dict(body).get("limit")))
        costs = set()
        for key, data in authorize:
            if key == "add_equipment_to_stockpile": costs.add(dict(data)["type"])
            if key == "add_fuel": costs.add("fuel")
            if key == "add_timed_idea" and dict(data)["idea"] == "chaosx_nr25_civilian_commitment": costs.add("civilian_industry")
            if key == "add_political_power": costs.add("political_power")
        self.assertEqual(costs, {"convoy", "fuel", "support_equipment", "civilian_industry"})
        ideas = (ROOT / "common/ideas/025_alien_technology_in_antarctica_ideas.txt").read_text(encoding="utf-8-sig")
        commitment = block("chaosx_nr25_civilian_commitment", re.sub(r"#[^\n]*", "", ideas))
        self.assertEqual(set(dict(dict(commitment)["modifier"])), {"consumer_goods_factor"})
        mirror = float(re.search(r"@NR25_CIVILIAN_COMMITMENT_FACTOR\s*=\s*([\d.]+)", ideas)[1])
        tuning = (ROOT / "common/script_constants/025_alien_technology_in_antarctica_constants.txt").read_text(encoding="utf-8-sig")
        self.assertEqual(mirror, float(re.search(r"civilian_commitment_goods_factor\s*=\s*([\d.]+)", tuning)[1]))

    def test_political_authorization_fee_has_no_remaining_consumer(self):
        for path in ("common/script_constants/025_alien_technology_in_antarctica_constants.txt",
                     "common/scripted_triggers/025_alien_technology_in_antarctica_triggers.txt",
                     "common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt"):
            self.assertNotIn("pp_authorize", (ROOT / path).read_text(encoding="utf-8-sig"))

    def test_native_cost_has_three_upfront_values_and_industry_hover(self):
        loc = (ROOT / "localisation/english/025_alien_technology_in_antarctica_l_english.yml").read_text(encoding="utf-8-sig")
        for suffix in ("", "_blocked"):
            text = re.search(r'^chaosx_nr25_authorize_cost' + suffix + r': "([^"]+)"', loc, re.M)[1]
            self.assertEqual(text.count("[This.GetChaosxNr25Authorize"), 3)
            self.assertNotIn("pol_power", text)
        hover = re.search(r'^chaosx_nr25_authorize_cost_tooltip: "([^"]+)"', loc, re.M)[1]
        self.assertIn("civilian_commitment_days", hover)

    def test_inclusive_component_gates_and_display_share_identifiers(self):
        gates = (ROOT / "common/scripted_triggers/025_alien_technology_in_antarctica_authorization_triggers.txt").read_text(encoding="utf-8-sig")
        display = (ROOT / "common/scripted_localisation/025_alien_technology_in_antarctica_authorization_scripted_localisation.txt").read_text(encoding="utf-8-sig")
        for component in ("convoys", "fuel", "support"):
            self.assertIn("chaosx_nr25_authorize_" + component + "_available = yes", display)
        self.assertEqual(gates.count("compare = greater_than_or_equals"), 2)
        self.assertRegex(gates, r"NOT\s*=\s*\{\s*has_fuel\s*<\s*constant:chaosx_nr25_cost.fuel_authorize_required\s*\}")


if __name__ == "__main__":
    unittest.main()
