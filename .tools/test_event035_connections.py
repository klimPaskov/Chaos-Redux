"""Event 35 shared-owner connections: famine, contamination and sanctions.

Runs the production certification hold, hidden pressure and cost surcharge
through the Event 35 source executor. Owner state (food stage, contamination,
sanction participants) is declared fixture data; the owners' own logic is not
emulated.
"""
import unittest

from test_event035_center_projects import registered_case, pay_action

PAUSED = "great_depression_center_project_paused"
FOOD_FLAG = "famine_food_stage_acute_shortage"


class CertificationHoldTests(unittest.TestCase):
    def start_reopening(self):
        runtime, owner, site = registered_case("shuttered")
        runtime.run_effect("great_depression_refresh_costs", owner, root=owner)
        self.assertTrue(pay_action(runtime, owner, site, "great_depression_reopen_selected_center",
                                   "great_depression_center_reopen_target_is_valid", "great_depression_can_pay_center_reopen"))
        required = site.values["great_depression_center_project_required_work_days"]
        certification_start = site.values["great_depression_center_project_certification_start_work_days"]
        self.assertLess(certification_start, required)
        return runtime, owner, site, required, certification_start

    def process(self, runtime, owner, site):
        runtime.run_effect("great_depression_process_center_project", site, root=owner)

    def test_food_problem_holds_certification_until_it_clears(self):
        runtime, owner, site, required, start = self.start_reopening()
        runtime.advance(int(start))
        self.process(runtime, owner, site)
        self.assertIn("great_depression_center_project_certification", site.flags)
        site.flags.add(FOOD_FLAG)
        runtime.advance(1)
        self.process(runtime, owner, site)
        self.assertIn(PAUSED, site.flags)
        self.assertNotIn("great_depression_center_project_completed_receipt", site.flags)
        site.flags.discard(FOOD_FLAG)
        runtime.advance(1)
        self.process(runtime, owner, site)
        self.assertNotIn(PAUSED, site.flags)
        runtime.advance(int(required))
        self.process(runtime, owner, site)
        self.assertIn("great_depression_center_project_completed_receipt", site.flags)

    def test_a_hold_that_never_lifts_fails_the_project(self):
        runtime, owner, site, required, start = self.start_reopening()
        runtime.advance(int(start))
        self.process(runtime, owner, site)
        site.flags.add(FOOD_FLAG)
        runtime.advance(1)
        self.process(runtime, owner, site)
        self.assertIn(PAUSED, site.flags)
        runtime.advance(int(runtime.constants["constant:great_depression_event.center_project_pause_fail_days"]))
        self.process(runtime, owner, site)
        self.assertNotIn("great_depression_center_project_completed_receipt", site.flags)
        self.assertIn("great_depression_center_project_failed_receipt", site.flags)

    def test_severe_contamination_holds_certification(self):
        runtime, owner, site, required, start = self.start_reopening()
        runtime.advance(int(start))
        self.process(runtime, owner, site)
        runtime.advance(1)
        site.values["cbrn_chemical_contamination"] = 50
        self.assertTrue(runtime.test_trigger("great_depression_center_certification_is_blocked", site, root=owner))
        self.process(runtime, owner, site)
        self.assertIn(PAUSED, site.flags)
        site.values["cbrn_chemical_contamination"] = 49
        self.assertFalse(runtime.test_trigger("great_depression_center_certification_is_blocked", site, root=owner))
        site.values["cbrn_chemical_contamination"] = 0
        site.modifiers.add("nuclear_fallout_state")
        self.assertTrue(runtime.test_trigger("great_depression_center_state_is_contaminated", site, root=owner))

    def test_early_work_is_not_held(self):
        runtime, owner, site, required, start = self.start_reopening()
        site.flags.add(FOOD_FLAG)
        self.assertFalse(runtime.test_trigger("great_depression_center_certification_is_blocked", site, root=owner))
        self.process(runtime, owner, site)
        self.assertNotIn(PAUSED, site.flags)

    def test_protection_is_never_held(self):
        runtime, owner, site, required, start = self.start_reopening()
        site.values["great_depression_center_project_type"] = runtime.constants["constant:great_depression_center_project.protection"]
        runtime.advance(int(start))
        self.process(runtime, owner, site)
        site.flags.add(FOOD_FLAG)
        runtime.advance(1)
        self.process(runtime, owner, site)
        self.assertNotIn(PAUSED, site.flags)
        self.assertFalse(runtime.test_trigger("great_depression_center_certification_is_blocked", site, root=owner))


class SanctionCostTests(unittest.TestCase):
    def quote(self, sanctioned, doctrine):
        runtime, owner, site = registered_case("shuttered")
        owner.values["great_depression_doctrine"] = runtime.constants[f"constant:great_depression_doctrine.{doctrine}"]
        if sanctioned:
            owner.values["condemnation_active_sanctions"] = 2
        runtime.run_effect("great_depression_refresh_costs", owner, root=owner)
        return owner.values["great_depression_cost_convoys"], owner.values["great_depression_cost_political_power"]

    def test_finance_and_trade_pays_more_under_sanctions(self):
        base = self.quote(False, "stabilize_finance_and_trade")
        sanctioned = self.quote(True, "stabilize_finance_and_trade")
        self.assertGreater(sanctioned[0], base[0])
        self.assertGreater(sanctioned[1], base[1])

    def test_other_doctrines_keep_the_quote(self):
        self.assertEqual(self.quote(True, "emergency_public_works"), self.quote(False, "emergency_public_works"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
