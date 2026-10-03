"""Source-execution checks for Event 025 pulse ownership and archive closure."""
from pathlib import Path
import re
import unittest

from test_event025_final_recovery import ROOT, Country, Runtime, block

LIFECYCLE = ROOT / "common/scripted_effects/025_alien_technology_in_antarctica_lifecycle_effects.txt"
SOURCE = re.sub(r"#[^\n]*", "", LIFECYCLE.read_text(encoding="utf-8-sig"))


class LifecycleRuntime(Runtime):
    effects = {
        **Runtime.effects,
        **{name: block("chaosx_nr25_" + name, SOURCE) for name in (
            "schedule_participant_pulse", "close_country_analysis",
            "update_dependence_streaks",
        )},
    }


class LifecycleTests(unittest.TestCase):
    def test_containment_interval_resets_when_dependence_leaves_safe_band(self):
        actor = Country(1)
        actor.flags.add("chaosx_nr25_dependence_contained")
        actor.values["chaosx_nr25_dependence"] = 20
        rt = LifecycleRuntime([actor])
        rt.run("update_dependence_streaks", actor)
        self.assertEqual(actor.values["chaosx_nr25_dependence_safe_days"], 12)
        actor.values["chaosx_nr25_dependence"] = 60
        rt.run("update_dependence_streaks", actor)
        self.assertEqual(actor.values["chaosx_nr25_dependence_safe_days"], 0)

    def test_integration_interval_resets_after_an_accident(self):
        actor = Country(1)
        actor.flags.update({"chaosx_nr25_dependence_started",
                            "chaosx_nr25_dependence_integrate_route"})
        actor.values["chaosx_nr25_dependence"] = 75
        rt = LifecycleRuntime([actor])
        rt.run("update_dependence_streaks", actor)
        self.assertEqual(actor.values["chaosx_nr25_dependence_stable_days"], 12)
        actor.flags.add("chaosx_nr25_dependence_accident")
        rt.run("update_dependence_streaks", actor)
        self.assertEqual(actor.values["chaosx_nr25_dependence_stable_days"], 0)

    def test_one_outstanding_pulse_despite_three_schedule_calls(self):
        actor = Country(1)
        rt = LifecycleRuntime([actor])
        for _ in range(3):
            rt.run("schedule_participant_pulse", actor)
        self.assertEqual(rt.reports, [(1, "chaosx.nr25.280")])
        self.assertIn("chaosx_nr25_pulse_pending", actor.flags)

    def test_receiving_a_pulse_allows_exactly_one_next_callback(self):
        actor = Country(1)
        rt = LifecycleRuntime([actor])
        rt.run("schedule_participant_pulse", actor)
        actor.flags.remove("chaosx_nr25_pulse_pending")
        rt.run("schedule_participant_pulse", actor)
        rt.run("schedule_participant_pulse", actor)
        self.assertEqual(len(rt.reports), 2)

    def test_losing_holder_has_an_independent_aftermath_clock(self):
        actor = Country(1)
        actor.flags.update({"chaosx_nr25_terminal", "chaosx_nr25_aftermath_open"})
        rt = LifecycleRuntime([actor])
        rt.global_flags.clear()
        rt.run("schedule_participant_pulse", actor)
        self.assertEqual(rt.reports, [(1, "chaosx.nr25.280")])
        self.assertNotIn("chaosx_nr25_recovery_winner", actor.flags)

    def test_closed_holder_does_not_reschedule(self):
        actor = Country(1)
        actor.flags.update({"chaosx_nr25_terminal", "chaosx_nr25_aftermath_open",
                            "chaosx_nr25_aftermath_closed"})
        rt = LifecycleRuntime([actor])
        rt.global_flags.clear()
        rt.run("schedule_participant_pulse", actor)
        self.assertFalse(rt.reports)

    def test_nonparticipant_cannot_open_a_pulse_chain(self):
        actor = Country(1)
        actor.flags.remove("chaosx_nr25_participant")
        rt = LifecycleRuntime([actor])
        rt.run("schedule_participant_pulse", actor)
        self.assertFalse(rt.reports)

    def test_first_archive_closure_preserves_other_country_analysis(self):
        first, second = Country(1), Country(2)
        first.flags.add("chaosx_nr25_analysis_sealed")
        second.flags.add("chaosx_nr25_aftermath_open")
        rt = LifecycleRuntime([first, second])
        rt.global_flags = {"chaosx_nr25_aftermath_active"}
        rt.global_values["chaosx_nr25_phase"] = 6
        rt.run("close_country_analysis", first)
        self.assertIn("chaosx_nr25_aftermath_active", rt.global_flags)
        self.assertNotIn("chaosx_nr25_closed", rt.global_flags)
        self.assertIn("chaosx_nr25_aftermath_open", second.flags)
        self.assertEqual(rt.global_values["chaosx_nr25_phase"], 6)

    def test_last_archive_closure_closes_shared_analysis(self):
        first, second = Country(1), Country(2)
        first.flags.add("chaosx_nr25_analysis_sealed")
        second.flags.add("chaosx_nr25_analysis_sealed")
        rt = LifecycleRuntime([first, second])
        rt.global_flags = {"chaosx_nr25_aftermath_active"}
        rt.run("close_country_analysis", second)
        self.assertNotIn("chaosx_nr25_aftermath_active", rt.global_flags)
        self.assertIn("chaosx_nr25_closed", rt.global_flags)
        self.assertEqual(rt.global_values["chaosx_nr25_phase"], 7)

    def test_orphaned_registry_scope_does_not_hold_analysis_open(self):
        actor, gone = Country(1), Country(2, exists=False)
        actor.flags.add("chaosx_nr25_analysis_sealed")
        rt = LifecycleRuntime([actor, gone])
        rt.run("close_country_analysis", actor)
        self.assertIn("chaosx_nr25_closed", rt.global_flags)


if __name__ == "__main__":
    unittest.main()
