"""Execute the pulse's evolution hazard branches, not scheduling or UI."""
import re
import unittest

from test_event025_custody import CustodyRuntime
from test_event025_evolution_callbacks import TRACKS
from test_event025_final_recovery import ROOT, Country, block

GATES = (ROOT / "common/scripted_triggers/025_alien_technology_in_antarctica_evolution_gate_triggers.txt").read_text(encoding="utf-8-sig")
RUNTIME = (ROOT / "common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt").read_text(encoding="utf-8-sig")
PULSE = block("chaosx_nr25_run_bounded_pulse", re.sub(r"#[^\n]*", "", RUNTIME))


def hazard_branches(nodes):
    result = []
    for key, data in nodes:
        if not isinstance(data, list):
            continue
        limit = dict(data).get("limit", [])
        if key == "if" and any(k.endswith("_evolution_in_force") for k, _ in limit):
            result.append((key, data))
        else:
            result.extend(hazard_branches(data))
    return result


class HazardRuntime(CustodyRuntime):
    def __init__(self, countries):
        super().__init__(countries)
        self.triggers.update({f"chaosx_nr25_{track}_evolution_in_force":
                              block(f"chaosx_nr25_{track}_evolution_in_force", GATES)
                              for track in TRACKS})
        # Deliberate receipt spy: shared Deaths internals are out of scope.
        self.effects["chaosx_nr25_record_casualties"] = [
            ("add_to_temp_variable", [("casualty_calls", "1")])]

    @property
    def casualty_calls(self):
        return self.temporary.get("casualty_calls", 0)


class ActiveHazardTests(unittest.TestCase):
    def fixture(self, disabled=()):
        actor = Country(1, flags={"chaosx_nr25_participant", "chaosx_nr25_aftermath_open",
                                 "chaosx_nr25_dependence_started", "chaosx_nr25_outpost_established"})
        actor.values.update({"chaosx_nr25_crew": 100, "chaosx_nr25_exposure_risk": 90,
                             "chaosx_nr25_wreck_integrity": 100, "chaosx_nr25_dependence": 90,
                             "chaosx_nr25_entry_order": 1, "chaosx_nr25_outpost_security": 50})
        rt = HazardRuntime([actor])
        rt.global_flags = {f"chaosx_nr25_evolution_{track}" for track in TRACKS}
        rt.global_flags.update(f"events_log_disabled_evolution_25_25_{stage}" for stage in disabled)
        rt.global_values["chaos_meter_value"] = 0
        return rt, actor

    def test_each_active_track_is_independently_suppressed(self):
        for stage in range(1, 6):
            with self.subTest(stage=stage):
                rt, actor = self.fixture((stage,))
                for tested, track in enumerate(TRACKS, 1):
                    self.assertEqual(rt.condition(rt.triggers[f"chaosx_nr25_{track}_evolution_in_force"], actor), tested != stage)
                before = rt.global_flags.copy()
                rt.execute(hazard_branches(PULSE), actor)
                self.assertEqual(rt.global_flags, before)
                if stage == 1:
                    self.assertNotIn("chaosx_nr25_signal_profile_initialized", actor.flags)
                    self.assertEqual(actor.values.get("chaosx_nr25_signal_intensity", 0), 0)
                if stage == 2:
                    self.assertEqual(actor.values["chaosx_nr25_crew"], 100)
                    self.assertNotIn("chaosx_nr25_survivor_profile_initialized", actor.flags)
                if stage == 3:
                    self.assertNotIn("chaosx_nr25_outpost_lost", actor.flags)
                    self.assertEqual(actor.values["chaosx_nr25_outpost_security"], 50)
                if stage == 4:
                    self.assertEqual(actor.values["chaosx_nr25_wreck_integrity"], 100)
                if stage == 5:
                    self.assertEqual(actor.values["chaosx_nr25_dependence"], 90)
                    self.assertEqual(rt.casualty_calls, 0)
                    self.assertNotIn("chaosx_nr25_dependence_accident", actor.flags)

    def test_all_disabled_tracks_leave_hazard_state_untouched(self):
        rt, actor = self.fixture(range(1, 6))
        values, flags = actor.values.copy(), actor.flags.copy()
        rt.execute(hazard_branches(PULSE), actor)
        self.assertEqual((actor.values, actor.flags), (values, flags))
        self.assertEqual(rt.casualty_calls, 0)

    def test_earned_hazards_do_not_require_a_second_chaos_threshold(self):
        rt, actor = self.fixture()
        rt.execute(hazard_branches(PULSE), actor)
        self.assertGreater(actor.values["chaosx_nr25_signal_intensity"], 0)
        self.assertLess(actor.values["chaosx_nr25_crew"], 100)
        self.assertEqual(actor.values["chaosx_nr25_survivor_profile"], rt.constants["constant:chaosx_nr25_cost.survivor_profile_default"])
        self.assertIn("chaosx_nr25_outpost_lost", actor.flags)
        self.assertLess(actor.values["chaosx_nr25_wreck_integrity"], 100)
        self.assertEqual(rt.casualty_calls, 1)

    def test_pulse_uses_only_exact_in_force_guards(self):
        body = RUNTIME.split("chaosx_nr25_run_bounded_pulse = {", 1)[1].split("chaosx_nr25_cleanup_invalid_participant = {", 1)[0]
        self.assertNotRegex(body, r"has_global_flag\s*=\s*chaosx_nr25_evolution_(?:" + "|".join(TRACKS) + r")\b")
        self.assertEqual(len(hazard_branches(PULSE)), 9)


if __name__ == "__main__":
    unittest.main()
