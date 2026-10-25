"""Execute the pulse's evolution hazard branches, not scheduling or UI."""
import re
import unittest

from test_event025_custody import CustodyRuntime
from test_event025_evolution_callbacks import TRACKS
from test_event025_final_recovery import ROOT, Country, block

GATES = (ROOT / "common/scripted_triggers/025_alien_technology_in_antarctica_evolution_gate_triggers.txt").read_text(encoding="utf-8-sig")
RUNTIME = (ROOT / "common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt").read_text(encoding="utf-8-sig")
HOLDER = re.sub(r"#[^\n]*", "", (ROOT / "common/scripted_effects/025_alien_technology_in_antarctica_holder_effects.txt").read_text(encoding="utf-8-sig"))
PULSE = block("chaosx_nr25_run_bounded_pulse", re.sub(r"#[^\n]*", "", RUNTIME))
# Evolution track -> the pulse helper that carries its hazard.
PULSE_HELPERS = {
    "active_signal": "chaosx_nr25_signal_pulse",
    "something_survived": "chaosx_nr25_survivor_pulse",
    "militarised_antarctica": "chaosx_nr25_militarisation_pulse",
    "wreck_breaking_apart": "chaosx_nr25_wreck_pulse",
}
HELPER_SOURCES = {
    "chaosx_nr25_signal_pulse": "025_alien_technology_in_antarctica_signal_effects.txt",
    "chaosx_nr25_survivor_pulse": "025_alien_technology_in_antarctica_survivor_effects.txt",
    "chaosx_nr25_militarisation_pulse": "025_alien_technology_in_antarctica_militarisation_effects.txt",
    "chaosx_nr25_wreck_pulse": "025_alien_technology_in_antarctica_wreck_effects.txt",
}


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
        # The shared accident body, minus its report event, which is scheduling.
        self.effects["chaosx_nr25_trigger_dependence_accident"] = [
            (key, data) for key, data in block("chaosx_nr25_trigger_dependence_accident", HOLDER)
            if key != "country_event"]
        # Report and news dispatch are scheduling, outside this hazard test.
        self.effects["chaosx_nr25_publish_dependence_crisis"] = []
        self.effects["chaosx_nr25_report_outpost_lost"] = []
        self.temporary["casualty_calls"] = 0
        # The four evolution hazards run in their own effect files (global
        # signal, survivor incidents, militarisation exposure, wreck decay).
        # Their bodies roll random numbers and read MTTH values, so the pulse
        # branch test records each call; the files' own gating is checked by
        # source below.
        for helper in PULSE_HELPERS.values():
            self.effects[helper] = [("add_to_temp_variable", [(helper + "_calls", "1")])]
            self.temporary[helper + "_calls"] = 0
        policy = (ROOT / "common/scripted_triggers/025_alien_technology_in_antarctica_custody_policy_triggers.txt").read_text(encoding="utf-8-sig")
        self.triggers["chaosx_nr25_active_material_incidents_allowed"] = block("chaosx_nr25_active_material_incidents_allowed", policy)

    def calls(self, track):
        return self.temporary.get(PULSE_HELPERS[track] + "_calls", 0)

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
        # Race-time hazards; the holder watch owns them after the race.
        rt.global_flags.add("chaosx_nr25_active")
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
                for tested, track in enumerate(TRACKS[:4], 1):
                    self.assertEqual(rt.calls(track), 0 if tested == stage else 1, track)
                if stage == 1:
                    self.assertNotIn("chaosx_nr25_signal_intensity", rt.global_values)
                if stage == 2:
                    self.assertEqual(actor.values["chaosx_nr25_crew"], 100)
                    self.assertNotIn("chaosx_nr25_survivor_profile", rt.global_values)
                if stage == 3:
                    self.assertNotIn("chaosx_nr25_outpost_lost", actor.flags)
                    self.assertEqual(actor.values["chaosx_nr25_outpost_security"], 50)
                    self.assertNotIn("chaosx_nr25_militarisation", rt.global_values)
                if stage == 4:
                    self.assertEqual(actor.values["chaosx_nr25_wreck_integrity"], 100)
                    self.assertNotIn("chaosx_nr25_wreck_integrity", rt.global_values)
                if stage == 5:
                    self.assertEqual(actor.values["chaosx_nr25_dependence"], 90)
                    self.assertEqual(rt.casualty_calls, 0)
                    self.assertNotIn("chaosx_nr25_dependence_accident", actor.flags)

    def test_all_disabled_tracks_leave_hazard_state_untouched(self):
        rt, actor = self.fixture(range(1, 6))
        values, flags = actor.values.copy(), actor.flags.copy()
        global_values = rt.global_values.copy()
        rt.execute(hazard_branches(PULSE), actor)
        self.assertEqual((actor.values, actor.flags), (values, flags))
        self.assertEqual(rt.global_values, global_values)
        self.assertEqual(rt.casualty_calls, 0)
        for track in TRACKS[:4]:
            self.assertEqual(rt.calls(track), 0, track)

    def test_earned_hazards_do_not_require_a_second_chaos_threshold(self):
        rt, actor = self.fixture()
        rt.execute(hazard_branches(PULSE), actor)
        for track in TRACKS[:4]:
            self.assertEqual(rt.calls(track), 1, track)
        # Signal exposure, militarised exposure and wreck exposure all land.
        self.assertGreater(actor.values["chaosx_nr25_exposure_risk"], 90)
        self.assertIn("chaosx_nr25_outpost_lost", actor.flags)
        self.assertEqual(rt.casualty_calls, 1)

    def test_pulse_uses_only_exact_in_force_guards(self):
        body = RUNTIME.split("chaosx_nr25_run_bounded_pulse = {", 1)[1].split("chaosx_nr25_begin_evacuation = {", 1)[0]
        self.assertNotRegex(body, r"has_global_flag\s*=\s*chaosx_nr25_evolution_(?:" + "|".join(TRACKS) + r")\b")
        # Signal, survivor, militarisation and wreck pulses, race-time
        # Dependence, the militarised camp loss and the Dependence accident.
        self.assertEqual(len(hazard_branches(PULSE)), 7)

    def test_global_hazard_helpers_keep_their_own_gates(self):
        # A helper reached from outside the pulse cannot move a global hazard
        # while its evolution is not in force.
        for helper, path in HELPER_SOURCES.items():
            with self.subTest(helper=helper):
                text = re.sub(r"#[^\n]*", "", (ROOT / "common/scripted_effects" / path).read_text(encoding="utf-8-sig"))
                self.assertRegex(text, r"\b" + helper + r"\s*=\s*\{")
        signal = re.sub(r"#[^\n]*", "", (ROOT / "common/scripted_triggers/025_alien_technology_in_antarctica_signal_triggers.txt").read_text(encoding="utf-8-sig"))
        self.assertIn("'chaosx_nr25_active_signal_evolution_in_force', 'yes'", block("chaosx_nr25_strong_pulse_possible", signal).__repr__())
        survivor = re.sub(r"#[^\n]*", "", (ROOT / "common/scripted_triggers/025_alien_technology_in_antarctica_survivor_triggers.txt").read_text(encoding="utf-8-sig"))
        self.assertIn("'chaosx_nr25_something_survived_evolution_in_force', 'yes'", block("chaosx_nr25_survivor_incident_possible", survivor).__repr__())
        militarisation = re.sub(r"#[^\n]*", "", (ROOT / "common/scripted_effects/025_alien_technology_in_antarctica_militarisation_effects.txt").read_text(encoding="utf-8-sig"))
        self.assertIn("'chaosx_nr25_militarised_antarctica_evolution_in_force', 'yes'", block("chaosx_nr25_change_militarisation", militarisation).__repr__())
        wreck = re.sub(r"#[^\n]*", "", (ROOT / "common/scripted_effects/025_alien_technology_in_antarctica_wreck_effects.txt").read_text(encoding="utf-8-sig"))
        self.assertIn("'chaosx_nr25_wreck_breaking_apart_evolution_in_force', 'yes'", block("chaosx_nr25_damage_wreck", wreck).__repr__())


if __name__ == "__main__":
    unittest.main()
