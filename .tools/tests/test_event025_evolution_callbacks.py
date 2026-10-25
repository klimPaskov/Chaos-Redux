"""Source checks for Event 025 delayed evolution settings and Chaos guards."""
import re
import unittest

from test_event025_final_recovery import ROOT, Country, Runtime, block

SOURCE = re.sub(r"#[^\n]*", "", (
    ROOT / "common/scripted_triggers/025_alien_technology_in_antarctica_evolution_gate_triggers.txt"
).read_text(encoding="utf-8-sig"))
TRACKS = (
    "active_signal", "something_survived", "militarised_antarctica",
    "wreck_breaking_apart", "technology_changes_users",
)


class EvolutionGateTests(unittest.TestCase):
    def gate(self, stage, rt, actor):
        return rt.condition(block(f"chaosx_nr25_{TRACKS[stage - 1]}_evolution_enabled", SOURCE), actor)

    def test_each_chaos_threshold_is_inclusive(self):
        actor = Country(1)
        rt = Runtime([actor])
        for stage in range(1, 6):
            threshold = rt.constants[f"constant:chaosx_nr25_evolution_gate.{TRACKS[stage - 1]}"]
            with self.subTest(stage=stage):
                rt.global_values["chaos_meter_value"] = threshold - 1
                self.assertFalse(self.gate(stage, rt, actor))
                rt.global_values["chaos_meter_value"] = threshold
                self.assertTrue(self.gate(stage, rt, actor))

    def test_disabling_one_track_does_not_disable_the_other_four(self):
        actor = Country(1)
        rt = Runtime([actor])
        rt.global_values["chaos_meter_value"] = 1000
        for disabled in range(1, 6):
            with self.subTest(disabled=disabled):
                rt.global_flags = {f"events_log_disabled_evolution_25_25_{disabled}"}
                for tested in range(1, 6):
                    self.assertEqual(self.gate(tested, rt, actor), tested != disabled)

    def test_delayed_gate_ignores_absent_or_foreign_temporary_context(self):
        actor = Country(1)
        rt = Runtime([actor])
        rt.global_values["chaos_meter_value"] = 1000
        rt.global_flags.add("events_log_disabled_evolution_25_25_3")
        for context in ({}, {
            "events_log_evolution_event_id": 16, "events_log_evolution_type": 99,
            "events_log_evolution_stage": 5, "events_log_evolution_tier": 1,
        }):
            rt.temporary = context
            self.assertFalse(self.gate(3, rt, actor))
            self.assertTrue(self.gate(1, rt, actor))
            self.assertTrue(self.gate(5, rt, actor))

    def test_all_callbacks_and_rehome_checks_use_their_own_guard(self):
        events = (ROOT / "events/025_alien_technology_in_antarctica.txt").read_text(encoding="utf-8-sig")
        runtime = (ROOT / "common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt").read_text(encoding="utf-8-sig")
        rehome = runtime.split("chaosx_nr25_rehome_pending_evolutions = {", 1)[1].split(
            "# COUNTRY scope. Caps the three displayed", 1)[0]
        self.assertNotIn("is_current_evolution_enabled", rehome)
        for track, event_id in zip(TRACKS, (100, 130, 160, 190, 220)):
            callback = events.split(f"id = chaosx.nr25.{event_id}\n", 1)[1].split("\n\toption =", 1)[0]
            guard = f"chaosx_nr25_{track}_evolution_enabled = yes"
            self.assertIn(guard, callback)
            self.assertIn(guard, rehome)
            self.assertNotIn("is_current_evolution_enabled", callback)


if __name__ == "__main__":
    unittest.main()
