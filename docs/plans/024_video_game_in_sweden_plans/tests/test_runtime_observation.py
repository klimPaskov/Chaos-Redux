"""Execute bounded Event 24 observer source with explicit native predicates.

This is a conservative source regression, not HOI4, probability, save, or
per-division supply evidence. Delayed events are recorded, never delivered.
"""
from decimal import Decimal, ROUND_HALF_UP
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
# The shared day-to-date converter and its unit constants run as written.
dynamic = life.parse(life.REPO / "common/scripted_effects/chaosx_dynamic_effects.txt")
life.APIS.update({n.key: n for n in dynamic if n.key == "chaosx_convert_days_to_date_offset"})
for group in life.parse(life.REPO / "common/script_constants/chaosx_date_units_constants.txt"):
    for item in group.body:
        if item.key != "schema" and isinstance(item.body, str):
            life.CONSTANTS[group.key + "." + item.key] = Decimal(item.body)


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
            "video_game_in_sweden_has_field_mission_running": False,
        }
        self.scheduled, self.called = [], []
        self.modifier_grants = []
        self.dispatch_only = False
        self.native_nodes = {}
        # Helpers recorded instead of executed. A case may clear an entry to run
        # the real source of that helper.
        self.stubs = {"video_game_in_sweden_open_trust_reassessment", "video_game_in_sweden_update_trust_model_progress",
                      "video_game_in_sweden_refresh_crisis_state"}
        # Explicit enemy roster for random_enemy_country, in selection order.
        self.enemies = []
        self.facts.update({("SWE", "has_war", "no"): False,
                           ("SWE", "has_war", "yes"): False,
                           ("SWE", "has_war_with_major", "yes"): False,
                           ("SWE", "has_global_flag", "world_end"): False,
                           ("SWE", "has_global_flag", "events_log_disabled_evolution_24_24_3"): False,
                           ("SWE", "owns_state", "constant:video_game_in_sweden_event.stockholm_state"): True,
                           ("SWE", "controls_state", "constant:video_game_in_sweden_event.stockholm_state"): True})

    def run(self, nodes):
        # Bridge only declared native commands through the parent's call hook.
        # The AST's body, position, control flow and if/else grouping are retained.
        bridged = []
        for n in nodes:
            if n.key == "set_country_flag" and isinstance(n.body, list):
                # Timed flag: the age is native, the flag name is recorded.
                self.flags.setdefault(self.actor, set()).add(life.field(n.body, "flag"))
                continue
            if n.key in ("clr_country_flag", "country_event", "FROM.FROM", "state", "is_core_of",
                         "clear_global_event_target", "remove_mission", "remove_decision", "remove_ideas",
                         "every_unit_leader", "has_dynamic_modifier", "divide_temp_variable", "clamp_variable", "add_dynamic_modifier",
                         "clear_array", "force_update_dynamic_modifier", "clamp_temp_variable", "clear_variable",
                         "round_temp_variable",
                         "random_enemy_country", "any_enemy_country", "save_global_event_target_as"):
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
                value = self.saved[key]
                if life.field(n.body, "min") is not None:
                    value = max(self.number(life.field(n.body, "min")), value)
                if life.field(n.body, "max") is not None:
                    value = min(self.number(life.field(n.body, "max")), value)
                self.saved[key] = value
                return True
            if n.key == "add_dynamic_modifier":
                days = life.field(n.body, "days")
                # A package without days lasts until the programme removes it.
                self.modifier_grants.append((life.field(n.body, "modifier"), None if days is None else self.number(days)))
                return True
            if n.key in ("clear_array", "force_update_dynamic_modifier"):
                return True
            if n.key == "clamp_temp_variable":
                # One-sided clamps are native; a missing side does not bound.
                variable = life.field(n.body, "var")
                value = self.temp[variable]
                if life.field(n.body, "min") is not None:
                    value = max(self.number(life.field(n.body, "min")), value)
                if life.field(n.body, "max") is not None:
                    value = min(self.number(life.field(n.body, "max")), value)
                self.temp[variable] = value
                return True
            if n.key == "clear_variable":
                self.saved.pop((self.actor, n.body), None)
                return True
            if n.key == "round_temp_variable":
                self.temp[n.body] = self.temp[n.body].to_integral_value(rounding=ROUND_HALF_UP)
                return True
            if n.key == "save_global_event_target_as":
                self.targets[n.body] = self.actor
                return True
            if n.key == "any_enemy_country":
                return any(self.scope(enemy, n.body) for enemy in self.enemies)
            if n.key == "random_enemy_country":
                limit = life.field(n.body, "limit", [])
                for enemy in self.enemies:
                    if self.scope(enemy, limit):
                        self.scope(enemy, [c for c in n.body if c.key != "limit"])
                        break
                return True
        if name in self.native_predicates:
            return self.native_predicates[name]
        if name in self.stubs:
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
        # Before the full report a lost capital is a finding against the
        # cabinet; only after it does Reality Check end (R2-6).
        for full_report in (False, True):
            model = self.model()
            model.flags["SWE"].update({"video_game_in_sweden_reality_check_stockholm_held",
                                      "video_game_in_sweden_trust_model_stockholm_continuous",
                                      "video_game_in_sweden_reality_check_reliance_timer"})
            model.saved[("SWE", "video_game_in_sweden_reality_check_proof_end_date")] = Decimal(1)
            if full_report:
                model.flags["SWE"].add("video_game_in_sweden_reality_audit_full_success")
            model.call("video_game_in_sweden_record_control_loss")
            self.assertNotIn(("SWE", "video_game_in_sweden_reality_check_proof_end_date"), model.saved)
            self.assertEqual("video_game_in_sweden_reality_check_disqualified" in model.flags["SWE"], full_report)
            self.assertIn("video_game_in_sweden_cabinet_found_wanting", model.flags["SWE"])
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
        # The untimed programme package is detached again by the closure; the
        # absent-modifier fixture cannot observe that removal, so it is excluded.
        timed = lambda: [g for g in model.modifier_grants if g[0] != "video_game_in_sweden_program_package"]
        self.assertEqual(timed(), [("video_game_in_sweden_restriction_backlash", Decimal(90))])
        model.call("video_game_in_sweden_complete_restriction_mission")
        model.call("video_game_in_sweden_timeout_restriction_mission")
        self.assertEqual(timed(), [("video_game_in_sweden_restriction_backlash", Decimal(90))])
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

    # Switched-off next stage (R3-1). Package, stage-idea and achievement
    # refreshes are recorded, not executed.
    def stage_model(self, phase, disabled):
        model = self.model()
        model.stubs |= {"video_game_in_sweden_refresh_program_package", "video_game_in_sweden_refresh_stage_idea",
                        "video_game_in_sweden_update_achievement_tracking"}
        model.saved[("SWE", "video_game_in_sweden_phase")] = Decimal(phase)
        for stage in (1, 2, 3):
            model.facts[("SWE", "has_global_flag", f"events_log_disabled_evolution_24_24_{stage}")] = stage in disabled
        return model

    def change(self, model, delta):
        model.temp["video_game_in_sweden_reliance_delta"] = Decimal(delta)
        model.call("video_game_in_sweden_change_reliance")
        return model.saved[("SWE", "simulation_reliance")]

    def test_switched_off_next_stage_holds_reliance_below_its_gate(self):
        # Evolution II with Evolution III off from the start never reaches Worldview.
        model = self.stage_model(3, {3})
        model.saved[("SWE", "simulation_reliance")] = Decimal(70)
        self.assertEqual([self.change(model, d) for d in (14, 6, -18, 14)],
                         [Decimal(74), Decimal(74), Decimal(56), Decimal(70)])
        self.assertIn("video_game_in_sweden_reliance_doctrine", model.flags["SWE"])
        # With Evolution III on, the same gain crosses into Worldview.
        model = self.stage_model(3, set())
        model.saved[("SWE", "simulation_reliance")] = Decimal(70)
        self.assertEqual(self.change(model, 14), Decimal(84))
        # Evolution I with Evolution II off stops at Habit; a value already
        # above the ceiling holds but cannot rise, and losses still apply.
        model = self.stage_model(2, {2})
        model.saved[("SWE", "simulation_reliance")] = Decimal(40)
        self.assertEqual(self.change(model, 9), Decimal(49))
        model.saved[("SWE", "simulation_reliance")] = Decimal(62)
        self.assertEqual([self.change(model, d) for d in (9, -10, 9)], [Decimal(62), Decimal(52), Decimal(52)])
        # A commercial baseline with Evolution I off may still grow into
        # Evolution II unless that stage is off as well.
        for commercial, disabled, expected in ((False, {1}, 49), (True, {1}, 53), (True, {1, 2}, 49)):
            model = self.stage_model(1, disabled)
            if commercial:
                model.flags["SWE"].add("video_game_in_sweden_commercial_route")
            model.saved[("SWE", "simulation_reliance")] = Decimal(45)
            self.assertEqual(self.change(model, 8), Decimal(expected))

    def test_step_back_from_a_switched_off_stage_lands_in_the_conclusion_band(self):
        # Evolution III switched off during a Trust the Model surge.
        model = self.stage_model(4, {3})
        model.flags["SWE"].update({"video_game_in_sweden_evolution_iii_active", "video_game_in_sweden_evolution_ii_recorded",
                                   "video_game_in_sweden_trust_model_active", "video_game_in_sweden_model_surge_active",
                                   "video_game_in_sweden_protected_shifts"})
        model.saved[("SWE", "simulation_reliance")] = Decimal(100)
        model.saved[("SWE", "video_game_in_sweden_program_days")] = Decimal(600)
        model.call("video_game_in_sweden_handle_disabled_evolution")
        self.assertEqual(model.saved[("SWE", "video_game_in_sweden_phase")], Decimal(3))
        self.assertEqual(model.saved[("SWE", "simulation_reliance")], Decimal(49))
        self.assertIn("video_game_in_sweden_evolution_ii_active", model.flags["SWE"])
        self.assertNotIn("video_game_in_sweden_trust_model_active", model.flags["SWE"])
        self.assertIn("video_game_in_sweden_refresh_program_package", model.called)
        model.native_predicates["video_game_in_sweden_no_active_mission"] = True
        self.assertTrue(model.call("video_game_in_sweden_can_conclude_low_value"))
        # Evolution II switched off at Doctrine steps back to Evolution I at Habit.
        model = self.stage_model(3, {2})
        model.flags["SWE"].update({"video_game_in_sweden_evolution_ii_active", "video_game_in_sweden_evolution_i_recorded"})
        model.saved[("SWE", "simulation_reliance")] = Decimal(74)
        model.call("video_game_in_sweden_handle_disabled_evolution")
        self.assertEqual(model.saved[("SWE", "video_game_in_sweden_phase")], Decimal(2))
        self.assertEqual(model.saved[("SWE", "simulation_reliance")], Decimal(49))

    # Trust the Model victories (R3-2). The surging host is at war with GER.
    def trust_model(self):
        model = self.model()
        model.flags["SWE"].update({"video_game_in_sweden_trust_model_active", "video_game_in_sweden_model_surge_active"})
        model.targets["video_game_in_sweden_host"] = "SWE"
        model.facts["global.date"] = Decimal(100)
        model.saved[("SWE", "video_game_in_sweden_trust_model_reassessment_deadline")] = Decimal(465)
        return model

    def test_opponent_capitulation_is_recorded_before_an_annexing_peace(self):
        captured = {"video_game_in_sweden_trust_model_meaningful_war", "video_game_in_sweden_trust_model_opponent_snapshot",
                    "video_game_in_sweden_trust_model_stockholm_continuous", "video_game_in_sweden_trust_model_war_seen"}
        annexed = {("GER", "has_war_with", "ROOT"): False, ("GER", "has_capitulated", "yes"): False}

        def annex_then_review(model):
            # The peace conference removes GER before the next monthly check,
            # and the sampled war score never crossed the threshold.
            model.root, model.actor = "SWE", "SWE"
            model.stubs.discard("video_game_in_sweden_update_trust_model_progress")
            model.facts.update(annexed)
            model.facts[("SWE", "has_war", "yes")] = False
            model.facts["global.date"] = Decimal(120)
            model.call("video_game_in_sweden_update_trust_model_progress")

        # Control: the monthly review alone cannot see the victory.
        model = self.trust_model()
        model.targets["video_game_in_sweden_trust_model_opponent"] = "GER"
        model.flags["SWE"].update(captured)
        annex_then_review(model)
        self.assertNotIn("video_game_in_sweden_trust_model_opponent_victory", model.flags["SWE"])

        for loser, date, recorded in (("GER", 110, True), ("ITA", 110, False), ("GER", 470, False)):
            model = self.trust_model()
            model.targets["video_game_in_sweden_trust_model_opponent"] = "GER"
            model.flags["SWE"].update(captured)
            model.facts[("SWE", "has_war_with", "PREV")] = True
            model.facts["global.date"] = Decimal(date)
            model.root, model.actor = loser, loser
            model.call("video_game_in_sweden_record_opponent_capitulation")
            self.assertEqual("video_game_in_sweden_trust_model_opponent_victory" in model.flags["SWE"], recorded)
            if not recorded:
                continue
            self.assertEqual(model.saved[("SWE", "video_game_in_sweden_trust_model_victory_date")], Decimal(110))
            annex_then_review(model)
            self.assertIn("video_game_in_sweden_trust_model_opponent_victory", model.flags["SWE"])
            model.call("video_game_in_sweden_mark_trust_reassessment")
            self.assertIn("video_game_in_sweden_trust_model_favorable_result", model.flags["SWE"])

    def test_war_declared_and_won_between_monthly_checks_is_recorded(self):
        model = self.trust_model()
        model.stubs.discard("video_game_in_sweden_update_trust_model_progress")
        model.enemies = ["GER"]
        model.facts.update({("SWE", "has_war", "yes"): True, ("SWE", "has_war_with_major", "yes"): True,
                            ("SWE", "any_war_score", "constant:video_game_in_sweden_event.trust_model_favorable_war_score"): True,
                            ("GER", "has_war_with", "ROOT"): True, ("GER", "has_capitulated", "yes"): False,
                            ("GER", "surrender_progress", "constant:video_game_in_sweden_effect.maximum_risk_surrender_progress"): False,
                            ("GER", "is_major", "yes"): True})
        # Day one of the war: the daily watch stores the opponent and war score.
        model.call("video_game_in_sweden_observe_runtime")
        self.assertEqual(model.targets["video_game_in_sweden_trust_model_opponent"], "GER")
        self.assertTrue({"video_game_in_sweden_trust_model_meaningful_war", "video_game_in_sweden_trust_model_war_seen",
                         "video_game_in_sweden_trust_model_war_score_reached"} <= model.flags["SWE"])
        # Days later GER signs a peace without capitulating, still inside the month.
        model.facts.update({("SWE", "has_war", "yes"): False, ("SWE", "has_war", "no"): True,
                            ("GER", "has_war_with", "ROOT"): False})
        model.facts["global.date"] = Decimal(112)
        model.call("video_game_in_sweden_observe_runtime")
        self.assertIn("video_game_in_sweden_trust_model_opponent_victory", model.flags["SWE"])
        self.assertEqual(model.saved[("SWE", "video_game_in_sweden_trust_model_victory_date")], Decimal(112))
        self.assertIn(("chaosx.nr24.50", Decimal(1)), model.scheduled)

    # Manual and forced dispatch (R4-1). The requester is ROOT in the shared
    # dispatcher; the opening event then initializes the selected host.
    def dispatch(self, requester="SWE", manual=False, force=False, bypass=False, model=None):
        model = model or self.model()
        model.native_predicates["video_game_in_sweden_can_receive_program"] = True
        model.targets["video_game_in_sweden_host"] = "SWE"
        model.root, model.actor = requester, requester
        model.flags.setdefault(requester, set())
        if manual:
            model.temp["events_log_manual_event_detail_trigger"] = Decimal(1)
        if force:
            model.flags[requester].add("force_trigger_mode_enabled")
        if bypass:
            model.saved[(requester, "temp_bypass_checks")] = Decimal(1)
        model.temp["video_game_in_sweden_prefire_ready"] = Decimal(0)
        model.call("video_game_in_sweden_prepare_random_event_fire")
        self.assertEqual(model.temp["video_game_in_sweden_prefire_ready"], Decimal(1))
        self.assertIn("video_game_in_sweden_prefire_opening_pending", model.flags["SWE"])
        # The dispatcher resets its temporary inputs after the call.
        model.temp.pop("events_log_manual_event_detail_trigger", None)
        model.flags[requester].discard("force_trigger_mode_enabled")
        model.saved.pop((requester, "temp_bypass_checks"), None)
        return model

    def open_cabinet(self, model):
        model.root, model.actor = "SWE", "SWE"
        model.flags["SWE"] |= {"video_game_in_sweden_normal_campaign", "video_game_in_sweden_achievement_eligible"}
        model.call("video_game_in_sweden_record_normal_campaign")
        model.facts.update({("SWE", "is_ai", "no"): True, ("SWE", "original_tag", "SWE"): True})
        return model.call("video_game_in_sweden_is_eligible_for_achievement")

    def test_manual_or_forced_dispatch_disqualifies_the_achievements(self):
        for requester, signal in (("SWE", "manual"), ("SWE", "force"), ("SWE", "bypass"), ("NOR", "manual"),
                                  ("NOR", "force"), ("NOR", "bypass")):
            model = self.dispatch(requester, **{signal: True})
            self.assertIn("video_game_in_sweden_debug_invalid", model.flags["SWE"])
            self.assertFalse(self.open_cabinet(model))
            self.assertNotIn("video_game_in_sweden_achievement_eligible", model.flags["SWE"])
            self.assertNotIn("video_game_in_sweden_normal_campaign", model.flags["SWE"])
            self.assertIn("video_game_in_sweden_according_to_plan_disqualified", model.flags["SWE"])

    def test_ordinary_dispatch_keeps_achievement_eligibility(self):
        for requester in ("SWE", "NOR"):
            model = self.dispatch(requester)
            self.assertTrue(self.open_cabinet(model))
            self.assertNotIn("video_game_in_sweden_according_to_plan_disqualified", model.flags["SWE"])
        # A manual preparation that never opened the cabinet leaves no mark on
        # a later ordinary dispatch.
        model = self.dispatch("SWE", manual=True)
        model.flags["SWE"].discard("video_game_in_sweden_prefire_opening_pending")
        model = self.dispatch("SWE", model=model)
        self.assertNotIn("video_game_in_sweden_debug_invalid", model.flags["SWE"])
        self.assertTrue(self.open_cabinet(model))

    # Reality Check proof year (R4-2). Stored dates count one hour as 0.00001.
    @staticmethod
    def days(n):
        return Decimal(n) * 24 / Decimal(100000)

    def test_reality_check_proof_year_completes_on_day_365(self):
        start = Decimal("1940.5")
        model = self.model()
        # The programme has closed after the full report; only the watch runs.
        model.flags["SWE"] = {"video_game_in_sweden_host_selected", "video_game_in_sweden_reality_audit_full_success",
                              "video_game_in_sweden_reality_audit_started", "video_game_in_sweden_evolution_iii_recorded",
                              "video_game_in_sweden_achievement_eligible", "video_game_in_sweden_normal_campaign"}
        model.native_predicates["video_game_in_sweden_is_current_host"] = False
        model.saved[("SWE", "simulation_reliance")] = Decimal(40)
        model.facts.update({"global.date": start, ("SWE", "is_ai", "no"): True, ("SWE", "original_tag", "SWE"): True})
        model.call("video_game_in_sweden_observe_runtime")
        self.assertIn("video_game_in_sweden_reality_check_reliance_timer", model.flags["SWE"])
        self.assertEqual(model.saved[("SWE", "video_game_in_sweden_reality_check_proof_end_date")], start + self.days(365))
        self.assertEqual(model.scheduled, [("chaosx.nr24.91", Decimal(1))])
        for day, complete in ((1, False), (364, False), (365, True)):
            model.flags["SWE"].discard("video_game_in_sweden_runtime_watch_pending")
            model.scheduled.clear()
            model.facts["global.date"] = start + self.days(day)
            model.call("video_game_in_sweden_observe_runtime")
            # The stored end date never moves while the year runs.
            self.assertEqual(model.saved[("SWE", "video_game_in_sweden_reality_check_proof_end_date")], start + self.days(365))
            self.assertEqual(model.call("video_game_in_sweden_reality_check_is_complete"), complete)
            # The daily watch continues until the year is complete.
            self.assertEqual(model.scheduled, [] if complete else [("chaosx.nr24.91", Decimal(1))])
        # A return to Doctrine before the end clears the timer and its date.
        model = self.model()
        model.flags["SWE"] |= {"video_game_in_sweden_reality_audit_full_success"}
        model.native_predicates["video_game_in_sweden_is_current_host"] = False
        model.saved[("SWE", "simulation_reliance")] = Decimal(40)
        model.facts["global.date"] = start
        model.call("video_game_in_sweden_update_achievement_tracking")
        model.saved[("SWE", "simulation_reliance")] = Decimal(80)
        model.facts["global.date"] = start + self.days(200)
        model.call("video_game_in_sweden_update_achievement_tracking")
        self.assertIn("video_game_in_sweden_reality_check_disqualified", model.flags["SWE"])
        self.assertNotIn("video_game_in_sweden_reality_check_reliance_timer", model.flags["SWE"])
        self.assertNotIn(("SWE", "video_game_in_sweden_reality_check_proof_end_date"), model.saved)

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
