"""Run condition-scaled Event035 project source, not a native game scheduler."""
import unittest

from test_event035_bank_lifecycle import BankRuntime
from test_event035_center_projects import ROOT, first, lex, parse_nodes, registered_case, uncomment


class DurationRuntime(BankRuntime):
    def _effects(self, nodes, scope):
        # Native targeted-decision FROM is explicitly bound to the fixture site.
        nodes = [type(n)("event_target:duration_test_from", n.op, n.value, n.line) if n.key == "FROM" else n for n in nodes]
        return super()._effects(nodes, scope)


class ProjectDurationTests(unittest.TestCase):
    def prepared(self, stage="idled"):
        _, actor, site = registered_case(stage)
        runtime = DurationRuntime()
        site.buildings["infrastructure"] = 5
        actor.values["great_depression_depression_severity"] = 40
        runtime.targets["duration_test_from"] = site
        runtime.run_effect("great_depression_refresh_costs", actor)
        return runtime, actor, site

    def quote(self, runtime, actor, site, kind="public_works", delta=0):
        runtime.root, runtime.scope_stack = actor, [site]
        runtime.temp_frames[0].update({
            "great_depression_duration_quote_days": 0,
            "great_depression_duration_quote_type": runtime.constants["constant:great_depression_center_project." + kind],
            "great_depression_duration_preview_delta": delta,
        })
        runtime._call_effect("great_depression_quote_center_project_duration", site)
        return runtime.temp_frames[0]["great_depression_duration_quote_days"]

    def authorize(self, runtime, actor, site, kind="transport_integration"):
        actor.values["great_depression_pending_center_project"] = runtime.constants["constant:great_depression_center_project." + kind]
        runtime.run_effect("great_depression_authorize_center_project", site)

    def test_each_real_condition_changes_quote_and_bounds_hold(self):
        cases = ((None, None, 133), ("damage", 3, 154), ("severity", 80, 153),
                 ("infrastructure", 2, 145), ("war", True, 147), ("failures", 2, 147))
        for factor, value, expected in cases:
            with self.subTest(factor=factor):
                runtime, actor, site = self.prepared()
                if factor == "damage":
                    site.values["damaged_building_level@industrial_complex"] = value
                elif factor == "severity":
                    actor.values["great_depression_depression_severity"] = value
                elif factor == "infrastructure":
                    site.buildings["infrastructure"] = value
                elif factor == "war":
                    actor.values["war"] = value
                elif factor == "failures":
                    actor.values["great_depression_project_failure_count"] = value
                self.assertEqual(self.quote(runtime, actor, site), expected)
        runtime, actor, site = self.prepared()
        site.values["damaged_building_level@industrial_complex"] = 1000
        site.buildings["infrastructure"] = 0
        actor.values.update({"great_depression_depression_severity": 100, "war": True, "great_depression_project_failure_count": 1000})
        self.assertEqual(self.quote(runtime, actor, site), 245)
        self.assertEqual(actor.values["great_depression_project_failure_count"], 1000)

    def test_fractional_damage_and_protection_interval(self):
        runtime, actor, site = self.prepared()
        site.values["damaged_building_level@industrial_complex"] = 0.5
        actor.values["great_depression_depression_severity"] = 41
        self.assertEqual(self.quote(runtime, actor, site), 137)
        self.assertEqual(self.quote(runtime, actor, site, "protection"), 42)

    def test_accepted_work_is_frozen_and_cannot_finish_at_old_anchor(self):
        runtime, actor, site = self.prepared()
        actor.values.update({"great_depression_depression_severity": 80, "war": True})
        site.buildings["infrastructure"] = 2
        site.values["damaged_building_level@industrial_complex"] = 3
        self.authorize(runtime, actor, site)
        required = site.values["great_depression_center_project_required_work_days"]
        self.assertEqual(required, 200)
        self.assertEqual(site.values["great_depression_center_project_certification_start_work_days"], required - 42)
        actor.values.update({"great_depression_depression_severity": 40, "war": False})
        site.buildings["infrastructure"] = 5
        site.values["damaged_building_level@industrial_complex"] = 0
        runtime.advance(133)
        runtime.run_effect("great_depression_process_center_project", site)
        self.assertNotIn("great_depression_center_project_completed_receipt", site.flags)
        self.assertEqual(site.values["great_depression_center_project_required_work_days"], required)
        runtime.advance(required - 133)
        runtime.run_effect("great_depression_process_center_project", site)
        self.assertIn("great_depression_center_project_completed_receipt", site.flags)

    def test_malformed_duration_and_certification_are_rejected_without_requoting(self):
        for malformed in ("missing_required", "missing_cut", "zero_cut", "fractional", "over_cap"):
            with self.subTest(record=malformed):
                runtime, actor, site = self.prepared()
                self.authorize(runtime, actor, site)
                if malformed == "missing_required":
                    del site.values["great_depression_center_project_required_work_days"]
                elif malformed == "missing_cut":
                    del site.values["great_depression_center_project_certification_start_work_days"]
                elif malformed == "zero_cut":
                    site.values["great_depression_center_project_certification_start_work_days"] = 0
                elif malformed == "fractional":
                    site.values["great_depression_center_project_required_work_days"] = 133.5
                else:
                    site.values["great_depression_center_project_required_work_days"] = 246
                before = dict(site.values)
                self.assertFalse(runtime.test_trigger("great_depression_center_project_duration_is_coherent", site, root=actor))
                runtime.advance(300)
                runtime.run_effect("great_depression_complete_center_project", site)
                self.assertNotIn("great_depression_center_project_completed_receipt", site.flags)
                self.assertEqual(site.values, before)

    def test_native_timer_binds_paid_work_and_replay_does_not_extend(self):
        runtime, actor, site = self.prepared()
        actor.values.update({"great_depression_depression_severity": 80, "great_depression_mission_reopen_center_state_id": site,
                             "great_depression_mission_reopen_center_episode_id": actor.values["great_depression_active_episode_id"]})
        runtime.root, runtime.scope_stack = actor, [actor]
        runtime._native_effect("activate_mission", "great_depression_reopen_depression_center", actor, 0)
        self.authorize(runtime, actor, site)
        deadline = site.values["great_depression_center_project_due_day"] + 7
        self.assertEqual(actor.values["native_mission_deadlines"]["great_depression_reopen_depression_center"], deadline)
        self.assertEqual(actor.values["great_depression_mission_reopen_center_authorization_id"], site.values["great_depression_center_project_authorization_id"])
        runtime.advance(10)
        runtime.run_effect("great_depression_sync_center_project_mission", actor)
        self.assertEqual(actor.values["native_mission_deadlines"]["great_depression_reopen_depression_center"], deadline)

    def test_owner_activation_synchronizes_immediately_and_scope_loss_cancels_without_pressure(self):
        runtime, actor, site = self.prepared()
        self.authorize(runtime, actor, site)
        self.assertIn("great_depression_reopen_depression_center", actor.values["active_missions"])
        self.assertEqual(actor.values["native_mission_deadlines"]["great_depression_reopen_depression_center"], site.values["great_depression_center_project_due_day"] + 7)
        severity = actor.values["great_depression_depression_severity"]
        from test_event035_center_projects import country
        site.controller = country("OCC")
        runtime.run_effect("great_depression_process_center_mission", actor)
        self.assertNotIn("great_depression_reopen_depression_center", actor.values["active_missions"])
        self.assertEqual(actor.values["great_depression_depression_severity"], severity)

    def test_expired_owner_resolution_and_late_callback_add_pressure_once(self):
        runtime, actor, site = self.prepared()
        self.authorize(runtime, actor, site)
        runtime.advance(int(site.values["great_depression_center_project_required_work_days"]) + 7)
        before = actor.values["great_depression_depression_severity"]
        runtime.run_effect("great_depression_sync_center_project_mission", actor)
        after = actor.values["great_depression_depression_severity"]
        self.assertGreater(after, before)
        runtime.run_effect("great_depression_timeout_reopen_depression_center", actor)
        self.assertEqual(actor.values["great_depression_depression_severity"], after)

    def test_actual_regional_works_tooltip_quote_matches_accepted_duration(self):
        runtime, actor, site = self.prepared("reopened")
        # The current works contract requires a genuine selected-state need.
        site.buildings["infrastructure"] = 2
        actor.values["great_depression_selected_center_state"] = site
        actor.values["great_depression_depression_severity"] = 80
        path = ROOT / "common/decisions/035_great_depression_decisions.txt"
        nodes, _ = parse_nodes(lex(uncomment(path.read_text(encoding="utf-8-sig"))), 0, str(path))
        category = next(n.value for n in nodes if n.key == "great_depression_category")
        action = next(n.value for n in category if n.key == "great_depression_launch_regional_works_program")
        runtime.root, runtime.scope_stack = actor, [actor]
        runtime._effects(first(action, "complete_effect"), actor)
        self.assertEqual(actor.values["great_depression_tt_project_days"], site.values["great_depression_center_project_required_work_days"])

    def test_historical_unbound_success_and_early_timeout_are_inert(self):
        runtime, actor, site = self.prepared("reopened")
        site.flags.add("great_depression_center_project_completed_receipt")
        site.values["great_depression_center_project_completed_authorization_id"] = 3
        actor.values.update({"great_depression_mission_reopen_center_state_id": site,
                             "great_depression_mission_reopen_center_episode_id": actor.values["great_depression_active_episode_id"],
                             "great_depression_mission_reopen_center_deadline_day": runtime.globals["num_days"] + 135})
        before = actor.values["great_depression_depression_severity"]
        runtime.run_effect("great_depression_complete_reopen_depression_center", actor)
        runtime.run_effect("great_depression_timeout_reopen_depression_center", actor)
        self.assertEqual(runtime.resource_writes, [])
        self.assertEqual(actor.values["great_depression_depression_severity"], before)
        self.assertNotIn("great_depression_mission_reopen_depression_center_complete", actor.flags)
        self.assertNotIn("great_depression_mission_reopen_depression_center_failed", actor.flags)

    def test_protection_never_binds_a_reopening_deadline_or_success(self):
        runtime, actor, site = self.prepared()
        self.authorize(runtime, actor, site, "protection")
        self.assertNotIn("great_depression_mission_reopen_center_authorization_id", actor.values)
        self.assertEqual(actor.values["great_depression_mission_reopen_center_deadline_day"], runtime.globals["num_days"] + 135)
        runtime.advance(49)
        before = actor.values["great_depression_depression_severity"]
        runtime.run_effect("great_depression_timeout_reopen_depression_center", actor)
        self.assertEqual(actor.values["great_depression_depression_severity"], before)
        actor.values["great_depression_mission_reopen_center_authorization_id"] = site.values["great_depression_center_project_authorization_id"]
        self.assertFalse(runtime.test_trigger("great_depression_reopen_depression_center_context_is_valid", actor))

    def test_returning_row_reuses_real_index_at_and_below_cap(self):
        from test_event035_center_projects import append_existing_center_row, state
        for row_count in (2, 4):
            with self.subTest(rows=row_count):
                runtime, actor, site = self.prepared()
                self.authorize(runtime, actor, site)
                for index in range(1, row_count):
                    other = state(200 + index, actor)
                    other.values["great_depression_center_episode_id"] = actor.values["great_depression_active_episode_id"]
                    append_existing_center_row(actor, other, 2)
                actor.flags.discard("great_depression_center_project_active")
                site.flags.update({"great_depression_center_transfer_receipt", "great_depression_center_transfer_contract_open", "great_depression_center_project_paused"})
                site.values.update({"great_depression_center_episode_id": 77, "great_depression_center_project_episode_id": 77,
                                    "great_depression_center_registry_index": 99, "great_depression_center_transfer_episode_id": 77})
                work = site.values["great_depression_center_project_required_work_days"]
                runtime.run_effect("great_depression_adopt_transferred_center", site, root=actor)
                self.assertIn("great_depression_center_transfer_adopted_receipt", site.flags)
                self.assertEqual(site.values["great_depression_center_registry_index"], 0)
                self.assertEqual(actor.values["great_depression_center_count"], row_count)
                self.assertTrue(all(len(array) == row_count for name, array in actor.arrays.items() if name.startswith("great_depression_center_")))
                self.assertEqual(actor.arrays["great_depression_center_project_due_day_entries"][0], site.values["great_depression_center_project_due_day"])
                self.assertEqual(site.values["great_depression_center_project_required_work_days"], work)

    def test_returning_selector_matches_existing_row_capacity_and_authority_cases(self):
        from test_event035_center_projects import append_existing_center_row, country, state
        for existing, count, foreign, closed in ((True, 4, False, False), (True, 2, False, False),
                                                (False, 4, False, False), (False, 2, False, False),
                                                (True, 4, True, False), (True, 4, False, True)):
            with self.subTest(existing=existing, rows=count, foreign=foreign, closed=closed):
                runtime, actor, site = self.prepared()
                if not existing:
                    for name in actor.arrays:
                        actor.arrays[name] = []
                    actor.values["great_depression_center_count"] = 0
                while len(actor.arrays["great_depression_center_state_ids"]) < count:
                    other = state(400 + len(actor.arrays["great_depression_center_state_ids"]), actor)
                    append_existing_center_row(actor, other, 2)
                site.values["great_depression_center_episode_id"] = 77
                site.flags.update({"great_depression_center_transfer_receipt", "great_depression_center_transfer_contract_open"})
                if foreign:
                    site.controller = country("OTHER")
                if closed:
                    site.flags.discard("great_depression_center_transfer_contract_open")
                    site.flags.discard("great_depression_center_transfer_receipt")
                actual = runtime.test_trigger("great_depression_center_is_valid_selector_target", site, root=actor)
                self.assertEqual(actual, not foreign and not closed and (existing or count < 4))

    def test_source_retirement_preserves_only_exact_open_foreign_transfer(self):
        from test_event035_center_projects import country
        runtime, actor, site = self.prepared()
        self.authorize(runtime, actor, site)
        holder = country("HOLDER")
        site.owner = holder
        site.controller = holder
        runtime.run_effect("great_depression_reconcile_center_transfer", site, root=actor)
        before = {k: v for k, v in site.values.items() if k.startswith("great_depression_center_project_")}
        runtime.run_effect("great_depression_clear_registered_center_runtime", actor)
        self.assertIn("great_depression_center_transfer_contract_open", site.flags)
        self.assertEqual(before, {k: v for k, v in site.values.items() if k.startswith("great_depression_center_project_")})
        site.owner = actor
        site.controller = actor
        runtime.run_effect("great_depression_clear_registered_center_runtime", actor)
        self.assertNotIn("great_depression_center_project_required_work_days", site.values)

    def test_matching_paid_completion_callback_charges_once_and_late_success_is_inert(self):
        runtime, actor, site = self.prepared()
        runtime.run_effect("great_depression_reopen_selected_center", site, root=actor)
        runtime.advance(int(site.values["great_depression_center_project_required_work_days"]))
        runtime.run_effect("great_depression_process_center_project", site, root=actor)
        self.assertTrue(runtime.test_trigger("great_depression_reopen_depression_center_objective_is_met", actor))
        runtime.run_effect("great_depression_complete_reopen_depression_center", actor)
        snapshot = (list(runtime.resource_writes), actor.values["great_depression_depression_severity"])
        runtime.run_effect("great_depression_complete_reopen_depression_center", actor)
        self.assertEqual((runtime.resource_writes, actor.values["great_depression_depression_severity"]), snapshot)
        runtime, actor, site = self.prepared()
        runtime.run_effect("great_depression_reopen_selected_center", site, root=actor)
        runtime.advance(int(site.values["great_depression_center_project_required_work_days"]))
        runtime.run_effect("great_depression_process_center_project", site, root=actor)
        runtime.advance(7)
        snapshot = list(runtime.resource_writes)
        runtime.run_effect("great_depression_complete_reopen_depression_center", actor)
        self.assertEqual(runtime.resource_writes, snapshot)
        self.assertNotIn("great_depression_mission_reopen_depression_center_complete", actor.flags)


if __name__ == "__main__":
    unittest.main(verbosity=2)
