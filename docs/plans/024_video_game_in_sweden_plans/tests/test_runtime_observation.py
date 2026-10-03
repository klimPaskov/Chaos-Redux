"""Execute bounded Event 24 observer source with explicit native predicates.

This is a conservative source regression, not HOI4, probability, save, or
per-division supply evidence. Delayed events are recorded, never delivered.
"""
from decimal import Decimal
import importlib.util
from pathlib import Path
import unittest

TESTS = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("e24_lifetime", TESTS / "lifetime/actual_source_lifetime_audit.py")
life = importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name] = life
spec.loader.exec_module(life)

runtime = life.parse(life.REPO / "common/scripted_effects/024_video_game_in_sweden_runtime_effects.txt")
life.APIS.update({n.key: n for n in runtime})
life.CONSTANTS["video_game_in_sweden_timing.runtime_watch_days"] = Decimal(1)


class ObserverModel(life.FrameModel):
    def __init__(self):
        super().__init__()
        self.native_predicates = {
            "video_game_in_sweden_is_current_host": True,
            "video_game_in_sweden_is_valid_host": True,
            "video_game_in_sweden_is_disabled": False,
            "video_game_in_sweden_no_active_mission": False,
            "video_game_in_sweden_has_committed_field_resources": True,
            "video_game_in_sweden_has_campaign_supply_gap": False,
            "video_game_in_sweden_has_front_presence": True,
            "video_game_in_sweden_has_full_reality_audit_field_package": True,
            "video_game_in_sweden_is_severe_campaign_crisis": False,
        }
        self.scheduled, self.called = [], []
        self.modifier_grants = []
        self.dispatch_only = False
        self.native_nodes = {}
        self.facts.update({("SWE", "has_war", "no"): False,
                           ("SWE", "has_global_flag", "world_end"): False,
                           ("SWE", "has_global_flag", "events_log_disabled_evolution_24_24_3"): False,
                           ("SWE", "owns_state", "constant:video_game_in_sweden_event.stockholm_state"): True,
                           ("SWE", "controls_state", "constant:video_game_in_sweden_event.stockholm_state"): True})

    def run(self, nodes):
        # Bridge only declared native commands through the parent's call hook.
        # The AST's body, position, control flow and if/else grouping are retained.
        bridged = []
        for n in nodes:
            if n.key in ("clr_country_flag", "country_event", "FROM.FROM", "state", "is_core_of",
                         "clear_global_event_target", "remove_mission", "remove_decision", "remove_ideas",
                         "every_unit_leader", "has_dynamic_modifier", "divide_temp_variable", "clamp_variable", "add_dynamic_modifier"):
                name = f"__native_{n.path}_{n.start}_{n.key}"
                self.native_nodes[name] = n
                life.APIS[name] = n
                bridged.append(life.Node(name, n.op, n.body, n.start, n.end, n.path))
            else:
                bridged.append(n)
        return super().run(bridged)

    def call(self, name):
        if self.dispatch_only and name.endswith("_apply_current"):
            self.called.append(name)
            return True
        if name in self.native_nodes:
            n = self.native_nodes[name]
            if n.key == "clr_country_flag":
                self.flags.setdefault(self.actor, set()).discard(n.body)
                return True
            if n.key == "country_event":
                self.scheduled.append((life.field(n.body, "id"), self.number(life.field(n.body, "days"))))
                return True
            if n.key == "FROM.FROM":
                return self.scope("141", n.body)
            if n.key == "state":
                return self.actor == "141" and self.number(n.body) == Decimal(141)
            if n.key == "is_core_of":
                return self.actor == "141" and n.body == "SWE"
            if n.key == "clear_global_event_target":
                self.targets.pop(n.body, None)
                self.called.append(n.key + ":" + n.body)
                return True
            if n.key in ("remove_mission", "remove_decision", "remove_ideas"):
                self.called.append(n.key)
                return True
            if n.key == "every_unit_leader":
                # Explicit empty-roster fixture, not native retirement evidence.
                return True
            if n.key == "has_dynamic_modifier":
                # Explicit absent-modifier fixture.
                return False
            if n.key == "divide_temp_variable":
                variable = life.field(n.body, "var", n.body[0].key)
                divisor = life.field(n.body, "value", n.body[0].body)
                self.temp[variable] = self.temp[variable] / self.number(divisor)
                return True
            if n.key == "clamp_variable":
                variable = life.field(n.body, "var")
                key = (self.actor, variable)
                self.saved[key] = min(self.number(life.field(n.body, "max")),
                                      max(self.number(life.field(n.body, "min")), self.saved[key]))
                return True
            if n.key == "add_dynamic_modifier":
                self.modifier_grants.append((life.field(n.body, "modifier"), self.number(life.field(n.body, "days"))))
                return True
        if name in self.native_predicates:
            return self.native_predicates[name]
        if name in ("video_game_in_sweden_open_trust_reassessment", "video_game_in_sweden_update_trust_model_progress"):
            self.called.append(name)
            return True
        return super().call(name)


class ObservationSourceTests(unittest.TestCase):
    def model(self):
        model = ObserverModel()
        model.flags["SWE"] = {"video_game_in_sweden_host_selected", "video_game_in_sweden_program_active"}
        return model

    def test_daily_elapsed_is_one_not_monthly(self):
        model = self.model()
        model.flags["SWE"].add("video_game_in_sweden_field_validation_active")
        model.saved[("SWE", "video_game_in_sweden_mission_elapsed_days")] = Decimal(89)
        model.call("video_game_in_sweden_observe_runtime")
        self.assertEqual(model.saved[("SWE", "video_game_in_sweden_mission_elapsed_days")], Decimal(90))
        self.assertEqual(model.scheduled, [("chaosx.nr24.91", Decimal(1))])
        maintenance = life.APIS["video_game_in_sweden_maintenance"]
        self.assertFalse(any(n.key == "add_to_variable" and life.field(n.body, "video_game_in_sweden_mission_elapsed_days") is not None
                             for n in life.walk(maintenance.body)))

    def test_interruption_cannot_be_erased_by_later_recovery(self):
        for active, receipts in (
                ("video_game_in_sweden_field_validation_active", {"video_game_in_sweden_field_validation_resource_interrupted",
                                                                   "video_game_in_sweden_field_validation_region_interrupted"}),
                ("video_game_in_sweden_reality_audit_active", {"video_game_in_sweden_reality_audit_supply_interrupted",
                                                             "video_game_in_sweden_reality_audit_region_interrupted"})):
            model = self.model()
            model.flags["SWE"].add(active)
            model.native_predicates["video_game_in_sweden_has_campaign_supply_gap"] = True
            model.native_predicates["video_game_in_sweden_has_front_presence"] = False
            model.native_predicates["video_game_in_sweden_has_full_reality_audit_field_package"] = False
            model.call("video_game_in_sweden_observe_runtime")
            self.assertTrue(receipts <= model.flags["SWE"])
            model.native_predicates["video_game_in_sweden_has_campaign_supply_gap"] = False
            model.native_predicates["video_game_in_sweden_has_front_presence"] = True
            model.native_predicates["video_game_in_sweden_has_full_reality_audit_field_package"] = True
            model.call("video_game_in_sweden_observe_runtime")
            self.assertTrue(receipts <= model.flags["SWE"])

    def test_only_one_next_watch_is_queued(self):
        model = self.model()
        model.call("video_game_in_sweden_start_runtime_watch")
        model.call("video_game_in_sweden_start_runtime_watch")
        self.assertEqual(model.scheduled, [("chaosx.nr24.91", Decimal(1))])

    def test_stockholm_loss_is_a_permanent_disqualifier(self):
        model = self.model()
        model.flags["SWE"].update({"video_game_in_sweden_reality_check_stockholm_held",
                                  "video_game_in_sweden_trust_model_stockholm_continuous",
                                  "video_game_in_sweden_reality_check_reliance_timer"})
        model.call("video_game_in_sweden_record_control_loss")
        self.assertIn("video_game_in_sweden_reality_check_disqualified", model.flags["SWE"])
        self.assertIn("video_game_in_sweden_according_to_plan_disqualified", model.flags["SWE"])
        self.assertNotIn("video_game_in_sweden_reality_check_reliance_timer", model.flags["SWE"])
        self.assertNotIn("video_game_in_sweden_trust_model_stockholm_continuous", model.flags["SWE"])

    def test_crisis_queues_reassessment_without_waiting_for_monthly_tick(self):
        model = self.model()
        model.flags["SWE"].add("video_game_in_sweden_trust_model_active")
        model.native_predicates["video_game_in_sweden_has_campaign_supply_gap"] = True
        model.call("video_game_in_sweden_observe_runtime")
        self.assertIn("video_game_in_sweden_open_trust_reassessment", model.called)
        self.assertIn(("chaosx.nr24.50", Decimal(1)), model.scheduled)

    def test_stale_closing_actor_cannot_clear_the_selected_hosts_pointers(self):
        model = self.model()
        model.root, model.actor = "NOR", "NOR"
        model.flags["NOR"] = {"video_game_in_sweden_host_selected", "video_game_in_sweden_program_active"}
        pointers = {"video_game_in_sweden_host": "SWE", "video_game_in_sweden_foreign_partner": "GER",
                    "video_game_in_sweden_last_partner": "FIN", "video_game_in_sweden_rulebook_commander": "Swedish general",
                    "video_game_in_sweden_trust_model_opponent": "SOV"}
        model.targets.update(pointers)
        model.call("video_game_in_sweden_close_program")
        self.assertEqual(model.targets, pointers)
        self.assertIn("video_game_in_sweden_program_closed", model.flags["NOR"])
        self.assertNotIn("video_game_in_sweden_program_closed", model.flags["SWE"])

    def test_late_close_ignores_an_already_closed_receipt(self):
        model = self.model()
        model.flags["SWE"].add("video_game_in_sweden_program_closed")
        model.call("video_game_in_sweden_close_program")
        self.assertEqual(model.called, [])

    def test_annex_callback_ignores_a_cloned_host_selected_flag(self):
        model = self.model()
        model.root, model.actor = "GER", "NOR"
        model.flags["NOR"] = {"video_game_in_sweden_host_selected"}
        model.targets["video_game_in_sweden_host"] = "SWE"
        model.call("video_game_in_sweden_record_actor_loss")
        self.assertEqual(model.targets["video_game_in_sweden_host"], "SWE")
        self.assertNotIn("video_game_in_sweden_program_closed", model.flags["NOR"])

    def test_enforcement_receipts_have_distinct_boundaries_and_no_reserve_gate(self):
        for days, count in ((19, 0), (20, 1), (39, 1), (40, 2), (59, 2), (60, 3)):
            model = self.model()
            model.saved[("SWE", "video_game_in_sweden_mission_elapsed_days")] = Decimal(days)
            model.flags["SWE"].update({"video_game_in_sweden_restriction_active", "video_game_in_sweden_restriction_orders_issued"})
            model.saved[("SWE", "video_game_in_sweden_active_mission")] = Decimal(4)
            model.facts.update({"has_political_power": Decimal(0), "has_stability": Decimal(0), "has_war_support": Decimal(0)})
            model.call("video_game_in_sweden_register_restriction_enforcement")
            receipts = {"video_game_in_sweden_official_leagues_closed", "video_game_in_sweden_policy_exclusions_enforced",
                        "video_game_in_sweden_public_facilities_withdrawn"}
            self.assertEqual(len(receipts & model.flags["SWE"]), count)
            self.assertEqual(model.call("video_game_in_sweden_restriction_objectives"), days == 60)

    def test_restriction_closes_without_a_validated_methods_reward(self):
        model = self.model()
        model.targets["video_game_in_sweden_host"] = "SWE"
        model.flags["SWE"].add("video_game_in_sweden_restriction_active")
        model.saved[("SWE", "video_game_in_sweden_active_mission")] = Decimal(4)
        model.call("video_game_in_sweden_complete_restriction_mission")
        self.assertIn("video_game_in_sweden_program_closed", model.flags["SWE"])
        self.assertNotIn("video_game_in_sweden_program_active", model.flags["SWE"])
        self.assertNotIn("video_game_in_sweden_recovery_active", model.flags["SWE"])
        self.assertEqual(model.modifier_grants, [("video_game_in_sweden_restriction_backlash", Decimal(90))])
        model.call("video_game_in_sweden_complete_restriction_mission")
        model.call("video_game_in_sweden_timeout_restriction_mission")
        self.assertEqual(model.modifier_grants, [("video_game_in_sweden_restriction_backlash", Decimal(90))])
        self.assertEqual(model.scheduled, [("chaosx.nr24.34", Decimal(1))])

    def test_native_factory_reservations_match_their_terms(self):
        decisions = next(n.body for n in life.SOURCES["common/decisions/024_video_game_in_sweden_decisions.txt"]
                         if n.key == "video_game_in_sweden_program_category")
        league = next(n for n in decisions if n.key == "video_game_national_league")
        self.assertEqual(life.field(league.body, "days_remove"), "var:video_game_in_sweden_national_league_native_days")
        model = self.model()
        setup = next(n for n in life.walk(life.APIS["video_game_in_sweden_initialize_program"].body)
                     if n.key == "set_variable" and n.body[0].key == "video_game_in_sweden_national_league_native_days")
        model.run([setup])
        durations = [model.number("video_game_in_sweden_national_league_native_days")]
        for _ in range(4):
            model.run(life.field(league.body, "remove_effect"))
            durations.append(model.number("video_game_in_sweden_national_league_native_days"))
        self.assertEqual(durations, [Decimal(45), Decimal(60), Decimal(75), Decimal(90), Decimal(90)])
        for decision_id, duration_key in (("video_game_foreign_licenses", "foreign_license_burden_days"),
                                          ("video_game_dual_track", "dual_track_burden_days")):
            decision = next(n for n in decisions if n.key == decision_id)
            self.assertEqual(life.field(decision.body, "days_remove"), "constant:video_game_in_sweden_timing." + duration_key)
            self.assertEqual(model.number(life.field(decision.body, "days_remove")), Decimal(30))

    def test_full_and_narrow_audit_text_selects_the_actual_proof(self):
        texts = life.SOURCES["common/scripted_localisation/024_video_game_in_sweden.txt"]
        definition = next(n for n in texts if life.field(n.body, "name") == "GetVideoGameAuditProofRequirements")
        for narrow, key in ((False, "video_game_full_audit_proof_requirements"),
                            (True, "video_game_narrow_audit_proof_requirements")):
            model = self.model()
            if narrow:
                model.flags["SWE"].add("video_game_in_sweden_narrow_reality_audit_started")
            chosen = next(n for n in definition.body if n.key == "text" and model.run(life.field(n.body, "trigger")))
            self.assertEqual(life.field(chosen.body, "localization_key"), key)

    def test_wrong_mission_and_closed_callbacks_cannot_dispatch(self):
        for stem, active_flag, mission_id in (("field_validation", "field_validation", 1),
                                             ("reality_audit", "reality_audit", 2),
                                             ("dual_track", "dual_track", 3)):
            for outcome in ("complete", "timeout", "failed"):
                callback = f"video_game_in_sweden_{outcome}_{stem}" + ("" if outcome == "failed" else "_mission")
                for closed, enum in ((False, 4), (True, mission_id)):
                    model = self.model()
                    model.dispatch_only = True
                    model.flags["SWE"].add(f"video_game_in_sweden_{active_flag}_active")
                    if closed:
                        model.flags["SWE"].discard("video_game_in_sweden_program_active")
                        model.flags["SWE"].add("video_game_in_sweden_program_closed")
                    model.saved[("SWE", "video_game_in_sweden_active_mission")] = Decimal(enum)
                    model.saved[("SWE", "video_game_in_sweden_mission_elapsed_days")] = Decimal(47)
                    model.call(callback)
                    self.assertEqual(model.called, [])
                    self.assertEqual(model.scheduled, [])
                    self.assertEqual(model.saved[("SWE", "video_game_in_sweden_mission_elapsed_days")], Decimal(47))
                model = self.model()
                model.dispatch_only = True
                model.flags["SWE"].add(f"video_game_in_sweden_{active_flag}_active")
                model.saved[("SWE", "video_game_in_sweden_active_mission")] = Decimal(mission_id)
                model.call(callback)
                self.assertEqual(model.called, [callback + "_apply_current"])

    def test_invalid_restriction_records_failure_without_a_backlash_reward(self):
        model = self.model()
        model.targets["video_game_in_sweden_host"] = "SWE"
        model.flags["SWE"].add("video_game_in_sweden_restriction_active")
        model.saved[("SWE", "video_game_in_sweden_active_mission")] = Decimal(4)
        model.native_predicates["video_game_in_sweden_is_current_host"] = False
        model.call("video_game_in_sweden_timeout_restriction_mission")
        self.assertIn("video_game_in_sweden_restriction_failed", model.flags["SWE"])
        self.assertIn("video_game_in_sweden_program_closed", model.flags["SWE"])
        self.assertEqual(model.modifier_grants, [])
        self.assertEqual(model.scheduled, [("chaosx.nr24.34", Decimal(1))])


if __name__ == "__main__":
    unittest.main(verbosity=2)
