"""Execute Event035 funded bank programs from production effects and missions.

The bounded executor records native mission activation/removal. Tests explicitly
invoke parsed native callbacks; this is not an engine scheduler, AI, save or UI test.
"""
import itertools
import unittest

from test_event035_center_projects import ROOT, first, lex, parse_nodes, registered_case, uncomment
from test_event035_reports import ReportRuntime


class BankRuntime(ReportRuntime):
    NATIVE_PRIMITIVES = ReportRuntime.NATIVE_PRIMITIVES | {"add_days_mission_timeout"}

    def _value(self, token):
        if isinstance(token, str) and token.startswith("days_mission_timeout@"):
            mission = token.split("@", 1)[1]
            return max(0, self.scope_stack[-1].values["native_mission_deadlines"][mission] - self.globals["num_days"])
        return super()._value(token)

    def _native_effect(self, key, value, scope, line):
        if key == "add_days_mission_timeout":
            mission = first(value, "mission")
            scope.values["native_mission_deadlines"][mission] += self._value(first(value, "days"))
            return
        was_active = value in scope.values.get("active_missions", set()) if key == "activate_mission" else False
        super()._native_effect(key, value, scope, line)
        if key == "activate_mission" and not was_active:
            path = ROOT / "common/decisions/035_great_depression_decisions.txt"
            nodes, _ = parse_nodes(lex(uncomment(path.read_text(encoding="utf-8-sig"))), 0, str(path))
            category = next(n.value for n in nodes if n.key == "great_depression_category")
            mission = next(n.value for n in category if n.key == value)
            scope.values.setdefault("native_mission_deadlines", {})[value] = self.globals["num_days"] + self._value(first(mission, "days_mission_timeout"))


class BankLifecycleTests(unittest.TestCase):
    def prepared(self):
        _, actor, center = registered_case("idled")
        runtime = BankRuntime()
        actor.values.update({"great_depression_doctrine": 3, "num_of_factories": 20})
        runtime.run_effect("great_depression_refresh_costs", actor)
        return runtime, actor, center

    def mission(self, name):
        path = ROOT / "common/decisions/035_great_depression_decisions.txt"
        nodes, _ = parse_nodes(lex(uncomment(path.read_text(encoding="utf-8-sig"))), 0, str(path))
        category = next(n.value for n in nodes if n.key == "great_depression_category")
        return next(n.value for n in category if n.key == name)

    def callback(self, runtime, actor, name, callback):
        runtime.root, runtime.scope_stack = actor, [actor]
        runtime._effects(first(self.mission(name), callback), actor)
        # Native completion/cancellation removes the mission. Its effects were
        # executed above from actual source, not implemented by this fixture.
        actor.values["active_missions"].discard(name)

    def audit(self, runtime, actor):
        runtime.run_effect("great_depression_declare_temporary_bank_holiday_and_audit", actor)

    def finish_audit(self, runtime, actor):
        self.audit(runtime, actor)
        runtime.advance(21)
        self.callback(runtime, actor, "great_depression_audit_viable_banks", "complete_effect")

    def test_authorization_is_paid_once_and_cannot_certify_early(self):
        runtime, actor, _ = self.prepared()
        self.audit(runtime, actor)
        writes = list(runtime.resource_writes)
        committed = actor.values["great_depression_committed_civilian"]
        self.assertTrue(writes)
        self.assertNotIn("great_depression_bank_audit_complete", actor.flags)
        self.assertIn("great_depression_bank_holiday", actor.modifiers)
        self.assertEqual(actor.values["great_depression_active_support_mission_count"], 1)
        self.audit(runtime, actor)
        runtime.run_effect("great_depression_complete_bank_audit", actor)
        runtime.advance(20)
        runtime.run_effect("great_depression_complete_bank_audit", actor)
        self.assertEqual(runtime.resource_writes, writes)
        self.assertEqual(actor.values["great_depression_committed_civilian"], committed)
        self.assertNotIn("great_depression_bank_audit_complete", actor.flags)

    def test_audit_then_recapitalization_exact_boundaries_and_no_second_payment(self):
        runtime, actor, _ = self.prepared()
        self.finish_audit(runtime, actor)
        self.assertIn("great_depression_bank_audit_complete", actor.flags)
        self.assertNotIn("great_depression_bank_holiday", actor.modifiers)
        runtime.run_effect("great_depression_recapitalize_viable_institutions", actor)
        self.assertNotIn("great_depression_viable_institutions_recapitalized", actor.flags)
        writes = list(runtime.resource_writes)
        runtime.advance(41)
        runtime.run_effect("great_depression_complete_bank_recapitalization", actor)
        self.assertNotIn("great_depression_viable_institutions_recapitalized", actor.flags)
        runtime.advance(1)
        self.callback(runtime, actor, "great_depression_certify_bank_recapitalization", "complete_effect")
        self.assertIn("great_depression_viable_institutions_recapitalized", actor.flags)
        severity = actor.values["great_depression_depression_severity"]
        runtime.run_effect("great_depression_complete_bank_recapitalization", actor)
        self.assertEqual(runtime.resource_writes, writes)
        self.assertEqual(actor.values["great_depression_depression_severity"], severity)

    def test_unaudited_or_stale_proof_cannot_recapitalize_or_guarantee(self):
        runtime, actor, _ = self.prepared()
        for effect in ("great_depression_recapitalize_viable_institutions", "great_depression_establish_durable_credit_guarantee"):
            runtime.run_effect(effect, actor)
        self.assertEqual(runtime.resource_writes, [])
        # The flag alone, or a previous episode's proof, cannot authorize new capital.
        actor.flags.add("great_depression_bank_audit_complete")
        actor.values["great_depression_bank_audit_episode_id"] = 34
        runtime.run_effect("great_depression_recapitalize_viable_institutions", actor)
        self.assertEqual(runtime.resource_writes, [])

    def test_real_policy_reviews_withdraw_current_paid_work(self):
        for effect in ("great_depression_cabinet_review", "great_depression_emergency_policy_review"):
            with self.subTest(effect=effect):
                runtime, actor, _ = self.prepared()
                self.audit(runtime, actor)
                runtime.advance(10)
                runtime.run_effect(effect, actor)
                self.assertIn("great_depression_renewed_bank_panic", actor.flags)
                self.assertNotIn("great_depression_bank_audit_active", actor.flags)
                self.assertNotIn("great_depression_bank_holiday", actor.modifiers)
                self.assertEqual(actor.values["active_missions"], set())
                self.assertEqual(actor.values["great_depression_doctrine"], 0)

    def test_recapitalization_failure_and_final_guarantee_gates(self):
        runtime, actor, _ = self.prepared()
        self.finish_audit(runtime, actor)
        runtime.run_effect("great_depression_recapitalize_viable_institutions", actor)
        runtime.advance(49)
        actor.resources["stability"] = 0.249
        self.callback(runtime, actor, "great_depression_certify_bank_recapitalization", "timeout_effect")
        self.assertIn("great_depression_bank_recapitalization_failed", actor.flags)
        self.assertNotIn("great_depression_viable_institutions_recapitalized", actor.flags)
        self.assertFalse(runtime.test_trigger("great_depression_can_start_durable_credit_guarantee", actor))
        actor.resources["stability"] = 0.7
        runtime.run_effect("great_depression_recapitalize_viable_institutions", actor)
        runtime.advance(42)
        self.callback(runtime, actor, "great_depression_certify_bank_recapitalization", "complete_effect")
        actor.values["great_depression_phase"] = runtime.constants["constant:great_depression_phase.stabilization"]
        self.assertTrue(runtime.test_trigger("great_depression_can_start_durable_credit_guarantee", actor))
        runtime.run_effect("great_depression_establish_durable_credit_guarantee", actor)
        self.assertIn("great_depression_durable_credit_guarantee", actor.flags)

    def test_observed_bank_holiday_does_not_certify_paid_audit(self):
        from test_event035_center_projects import read_definitions
        definitions = read_definitions("common/scripted_effects/035_great_depression_incident_effects.txt")
        branch = None
        for definition in definitions.values():
            for node in definition.body:
                if isinstance(node.value, list) and any(child.key == "set_country_flag" and child.value == "great_depression_bank_holiday_observed" for child in node.value):
                    branch = [child for child in node.value if child.key != "limit"]
        self.assertIsNotNone(branch)
        runtime, actor, _ = self.prepared()
        runtime.root, runtime.scope_stack = actor, [actor]
        runtime._effects(branch, actor)
        self.assertIn("great_depression_bank_holiday_observed", actor.flags)
        self.assertNotIn("great_depression_bank_audit_complete", actor.flags)
        self.assertFalse(runtime.test_trigger("great_depression_bank_audit_has_current_viability_proof", actor))

    def test_viability_failure_timeout_and_duplicate_are_bounded(self):
        for field, failed_value in (("stability", 0.249), ("capitulated", True), ("num_of_factories", 0)):
            with self.subTest(field=field):
                runtime, actor, _ = self.prepared()
                self.audit(runtime, actor)
                (actor.resources if field == "stability" else actor.values)[field] = failed_value
                runtime.advance(21)
                self.assertFalse(runtime.test_trigger("great_depression_bank_audit_objective_is_met", actor))
                runtime.advance(7)
                before = actor.values["great_depression_depression_severity"]
                self.callback(runtime, actor, "great_depression_audit_viable_banks", "timeout_effect")
                self.assertEqual(actor.values["great_depression_depression_severity"], before + 5)
                self.assertIn("great_depression_renewed_bank_panic", actor.flags)
                self.assertNotIn("great_depression_bank_holiday", actor.modifiers)
                runtime.run_effect("great_depression_fail_bank_program", actor)
                self.assertEqual(actor.values["great_depression_depression_severity"], before + 5)

    def test_exact_stability_floor_passes_and_policy_withdrawal_renews_panic_once(self):
        runtime, actor, _ = self.prepared()
        self.audit(runtime, actor)
        actor.resources["stability"] = 0.25
        runtime.advance(21)
        self.assertTrue(runtime.test_trigger("great_depression_bank_audit_objective_is_met", actor))
        before = actor.values["great_depression_depression_severity"]
        runtime.run_effect("great_depression_withdraw_bank_program", actor)
        runtime.run_effect("great_depression_withdraw_bank_program", actor)
        self.assertEqual(actor.values["great_depression_depression_severity"], before + 5)
        self.assertEqual(actor.values["active_missions"], set())
        self.assertNotIn("great_depression_bank_audit_complete", actor.flags)

    def test_retirement_and_old_episode_callbacks_never_reward_or_renew_panic(self):
        runtime, actor, _ = self.prepared()
        self.audit(runtime, actor)
        runtime.advance(28)
        actor.values["great_depression_active_episode_id"] = 36
        before = actor.values["great_depression_depression_severity"]
        runtime.run_effect("great_depression_complete_bank_audit", actor)
        runtime.run_effect("great_depression_fail_bank_program", actor)
        runtime.run_effect("great_depression_clear_bank_program_runtime", actor)
        self.assertEqual(actor.values["great_depression_depression_severity"], before)
        self.assertNotIn("great_depression_renewed_bank_panic", actor.flags)
        self.assertNotIn("great_depression_bank_audit_episode_id", actor.values)
        self.assertNotIn("great_depression_bank_holiday", actor.modifiers)

    def test_every_support_pool_subset_obeys_two_slot_limit(self):
        runtime, actor, _ = self.prepared()
        support = ("great_depression_keep_essential_freight_moving", "great_depression_national_employment_guarantee",
                   "great_depression_complete_national_recovery_plan", "great_depression_certify_cleared_economy",
                   "great_depression_restore_essential_production", "great_depression_audit_viable_banks",
                   "great_depression_certify_bank_recapitalization")
        for count in range(len(support) + 1):
            for subset in itertools.combinations(support, count):
                actor.values["active_missions"] = set(subset)
                self.assertEqual(runtime.test_trigger("great_depression_support_mission_slot_is_open", actor), count < 2)
        actor.values["active_missions"] = set(support[:2])
        self.audit(runtime, actor)
        self.assertEqual(runtime.resource_writes, [])

    def test_foreign_root_receipt_output_cost_and_mission_belong_to_actor(self):
        from test_event035_center_projects import country
        runtime, actor, _ = self.prepared()
        host = country("HOST")
        runtime.run_effect("great_depression_declare_temporary_bank_holiday_and_audit", actor, root=host)
        self.assertIn("great_depression_bank_audit_active", actor.flags)
        self.assertNotIn("great_depression_bank_audit_active", host.flags)
        self.assertTrue(all(row[0] == actor.id for row in runtime.resource_writes))

    def test_restored_timer_is_shortened_to_original_deadline_and_replay_is_inert(self):
        runtime, actor, _ = self.prepared()
        self.audit(runtime, actor)
        deadline = actor.values["great_depression_bank_audit_deadline_day"]
        runtime.advance(10)
        actor.values["active_missions"].clear()
        # The native primitive initializes from the actual static mission.
        # Production reconciliation must shorten it to the original date.
        runtime.run_effect("great_depression_process_bank_program", actor)
        self.assertEqual(actor.values["native_mission_deadlines"]["great_depression_audit_viable_banks"], deadline)
        runtime.run_effect("great_depression_process_bank_program", actor)
        self.assertEqual(actor.values["native_mission_deadlines"]["great_depression_audit_viable_banks"], deadline)
        self.assertEqual(actor.values["great_depression_active_support_mission_count"], 1)

    def test_owner_reconciliation_and_native_callback_share_one_resolution(self):
        runtime, actor, _ = self.prepared()
        self.audit(runtime, actor)
        runtime.advance(21)
        runtime.run_effect("great_depression_process_bank_program", actor)
        before = actor.values["great_depression_depression_severity"]
        self.assertIn("great_depression_bank_audit_complete", actor.flags)
        runtime.run_effect("great_depression_complete_bank_audit", actor)
        self.assertEqual(actor.values["great_depression_depression_severity"], before)
        runtime, actor, _ = self.prepared()
        self.audit(runtime, actor)
        runtime.advance(28)
        runtime.run_effect("great_depression_process_bank_program", actor)
        before = actor.values["great_depression_depression_severity"]
        self.assertIn("great_depression_bank_audit_failed", actor.flags)
        runtime.run_effect("great_depression_fail_bank_program", actor)
        self.assertEqual(actor.values["great_depression_depression_severity"], before)

    def test_funded_work_reserves_support_slot_when_native_mission_is_missing(self):
        runtime, actor, _ = self.prepared()
        self.audit(runtime, actor)
        actor.values["active_missions"] = {"great_depression_keep_essential_freight_moving"}
        self.assertFalse(runtime.test_trigger("great_depression_support_mission_slot_is_open", actor))
        runtime.run_effect("great_depression_refresh_mission_capacity_ledger", actor)
        self.assertEqual(actor.values["great_depression_active_support_mission_count"], 2)

    def test_nonhuman_or_special_actor_cannot_certify_bank_recovery(self):
        for actor_type in ("nonhuman", "special", "no_civilian_system"):
            runtime, actor, _ = self.prepared()
            self.audit(runtime, actor)
            runtime.advance(21)
            if actor_type == "no_civilian_system":
                actor.normal_civilian_systems = False
            else:
                actor.values["is_actual_nonhuman_country" if actor_type == "nonhuman" else "is_special_chaos_country"] = True
            self.assertFalse(runtime.test_trigger("great_depression_bank_audit_objective_is_met", actor))
            runtime.run_effect("great_depression_complete_bank_audit", actor)
            self.assertNotIn("great_depression_bank_audit_complete", actor.flags)
            runtime.run_effect("great_depression_fail_bank_program", actor)
            self.assertNotIn("great_depression_renewed_bank_panic", actor.flags)


if __name__ == "__main__":
    unittest.main(verbosity=2)
