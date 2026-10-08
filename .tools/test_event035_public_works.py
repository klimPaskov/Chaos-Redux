"""Execute actual PW owner source with declared native getter/map fixtures.

Native fixtures are not a campaign railway, repair queue or building-cap proof.
No Event35 production helper is stubbed. These tests verify transaction guards,
frozen plans, measured proof, replay, lifecycle and caller integration.
"""
import itertools
import unittest

from test_event035_bank_lifecycle import BankRuntime
from test_event035_center_projects import country, registered_case, state, pay_action


class PublicWorksTests(unittest.TestCase):
    def prepared(self, stage="reopened", infrastructure=2):
        _, actor, site = registered_case(stage)
        runtime = BankRuntime()
        site.buildings["infrastructure"] = infrastructure
        runtime.run_effect("great_depression_refresh_costs", actor)
        actor.values["great_depression_selected_center_state"] = site
        return runtime, actor, site

    def launch(self, runtime, actor, site):
        return pay_action(runtime, actor, site, "great_depression_launch_regional_works_program",
                          "great_depression_center_public_works_target_is_valid", "great_depression_can_pay_public_works")

    def finish(self, runtime, actor, site):
        runtime.advance(site.values["great_depression_center_project_required_work_days"])
        runtime.run_effect("great_depression_process_center_project", site, root=actor)

    def test_named_eligibility_and_abandoned_conversion_cases(self):
        for stage in ("distressed", "idled", "shuttered", "reopened", "abandoned"):
            with self.subTest(case="WKS-" + stage.upper() + "-NEED"):
                runtime, actor, site = self.prepared(stage)
                self.assertTrue(runtime.test_trigger("great_depression_center_public_works_target_is_valid", site, root=actor))
        for case in ("HEALTHY-NO-NEED", "ACTIVE-PROJECT", "FOREIGN-CONTROL", "EPISODE-MISMATCH", "LEGACY-REPEAT"):
            with self.subTest(case="WKS-" + case):
                runtime, actor, site = self.prepared(infrastructure=5 if case == "HEALTHY-NO-NEED" else 2)
                if case == "ACTIVE-PROJECT":
                    actor.flags.add("great_depression_center_project_active")
                elif case == "FOREIGN-CONTROL":
                    site.controller = country("FOREIGN")
                elif case == "EPISODE-MISMATCH":
                    site.values["great_depression_center_episode_id"] += 1
                elif case == "LEGACY-REPEAT":
                    site.flags.add("great_depression_center_public_works_receipt")
                self.assertFalse(runtime.test_trigger("great_depression_center_public_works_target_is_valid", site, root=actor))

    def test_paid_site_binding_and_one_level_frozen_outcome(self):
        runtime, actor, site = self.prepared()
        self.assertTrue(self.launch(runtime, actor, site))
        self.assertEqual(site.values["great_depression_public_works_plan_payer"], actor)
        self.assertEqual(site.values["great_depression_public_works_plan_site"], site)
        self.assertEqual(site.values["great_depression_public_works_paid_action_count"], actor.values["great_depression_successful_action_count"])
        self.assertEqual(site.buildings["infrastructure"], 2)
        deadline = site.values["great_depression_center_project_due_day"] + 28
        self.assertEqual(actor.values["great_depression_mission_reopen_center_deadline_day"], deadline)
        debit = len(runtime.resource_writes)
        self.finish(runtime, actor, site)
        self.assertEqual(site.buildings["infrastructure"], 3)
        self.assertIn("great_depression_center_public_works_completed_receipt", site.flags)
        issued = site.values["great_depression_public_works_issued_authorization_id"]
        for _ in range(3):
            runtime.run_effect("great_depression_complete_center_project", site, root=actor)
        self.assertEqual(site.buildings["infrastructure"], 3)
        self.assertEqual(len(runtime.resource_writes), debit)
        self.assertEqual(site.values["great_depression_public_works_issued_authorization_id"], issued)

    def test_prepared_but_unpaid_and_stale_payment_are_rejected(self):
        for stale in (False, True):
            runtime, actor, site = self.prepared()
            runtime.run_effect("great_depression_prepare_public_works_plan", site, root=actor)
            actor.values["great_depression_pending_center_project"] = runtime.constants["constant:great_depression_center_project.public_works"]
            if stale:
                actor.values["great_depression_successful_action_count"] = site.values["great_depression_public_works_expected_payment_count"]
                actor.values["great_depression_last_action_day"] = runtime.globals["num_days"] - 1
            runtime.run_effect("great_depression_authorize_center_project", site, root=actor)
            self.assertNotIn("great_depression_public_works_paid_receipt", site.flags)
            self.assertNotIn("great_depression_center_project_active", actor.flags)
            self.assertFalse(runtime.resource_writes)

    def test_external_completion_and_bombing_cannot_generate_extra_levels(self):
        for external, bombing in ((True, False), (False, True)):
            runtime, actor, site = self.prepared()
            self.assertTrue(self.launch(runtime, actor, site))
            if external:
                site.buildings["infrastructure"] = 3
            if bombing:
                site.values["damaged_building_level@infrastructure"] = 1
            self.finish(runtime, actor, site)
            issued = [call for call in runtime.native_calls if len(call) == 4 and call[0] == "add_building_construction" and call[2] == "infrastructure"]
            self.assertEqual(len(issued), 0 if external else 1)
            if bombing:
                self.assertNotIn("great_depression_center_public_works_completed_receipt", site.flags)
                site.buildings["infrastructure"] = 1
                runtime.run_effect("great_depression_complete_center_project", site, root=actor)
                self.assertEqual(site.buildings["infrastructure"], 1)
                self.assertEqual(site.values["great_depression_public_works_issued_level_amount"], 1)
            else:
                self.assertIn("great_depression_center_public_works_completed_receipt", site.flags)
                self.assertEqual(site.values["great_depression_public_works_issued_level_amount"], 0)

    def test_native_repair_requires_capacity_preservation_and_measured_damage(self):
        for kind in ("infrastructure", "rail_way", "naval_base"):
            for outcome in ("unchanged", "repaired", "demolished", "fractional"):
                with self.subTest(kind=kind, outcome=outcome):
                    runtime, actor, site = self.prepared(infrastructure=5)
                    site.buildings[kind] = 3
                    site.values["damaged_building_level@" + kind] = 0.5 if outcome == "fractional" else 2
                    self.assertTrue(self.launch(runtime, actor, site))
                    if outcome in ("repaired", "demolished"):
                        site.values["damaged_building_level@" + kind] = 1
                    elif outcome == "fractional":
                        site.values["damaged_building_level@" + kind] = 0
                    if outcome == "demolished":
                        site.buildings[kind] = 2
                    self.finish(runtime, actor, site)
                    self.assertEqual("great_depression_center_public_works_completed_receipt" in site.flags, outcome in ("repaired", "fractional"))
                    self.assertFalse(any(call[0] == "damage_building" for call in runtime.native_calls))

    def test_local_recovery_uses_same_measured_contribution_not_national_meter(self):
        for stage, expected in (("distressed", 1), ("idled", 2), ("shuttered", 3), ("abandoned", 4)):
            runtime, actor, site = self.prepared(stage, 5)
            actor.values["great_depression_hidden_demand_stress"] = 0
            factories = dict(site.buildings)
            self.assertTrue(self.launch(runtime, actor, site))
            self.assertEqual(site.values["great_depression_public_works_initial_local_demand"], expected)
            self.finish(runtime, actor, site)
            self.assertIn("great_depression_center_public_works_completed_receipt", site.flags)
            self.assertLess(site.values["great_depression_center_local_demand"], expected)
            self.assertEqual(site.buildings, factories)

    def test_all_local_stage_treatment_subsets_preserve_additive_demand(self):
        runtime, actor, site = self.prepared()
        names = ("distressed", "idled", "shuttered", "liquidated", "abandoned", "hollowed", "public_works", "reopened", "protected")
        for bits in itertools.product((False, True), repeat=len(names)):
            site.flags = {"great_depression_center"} | {"great_depression_center_" + key for key, active in zip(names, bits) if active}
            b = dict(zip(names, bits))
            expected = b["distressed"] + 2*b["idled"] + 3*b["shuttered"] + b["liquidated"]
            expected += 4*(b["abandoned"] + b["hollowed"]) if not b["liquidated"] else 0
            expected -= 2*b["public_works"] + int(b["reopened"] or b["protected"])
            runtime.run_effect("great_depression_measure_center_local_demand", site, root=actor)
            self.assertEqual(site.values["great_depression_center_local_demand"], expected)

    def test_pause_loss_and_invalid_actor_remove_repair_term(self):
        for condition in ("paused", "control", "actor"):
            runtime, actor, site = self.prepared(infrastructure=5)
            site.values["damaged_building_level@infrastructure"] = 2
            site.buildings["infrastructure"] = 5
            self.assertTrue(self.launch(runtime, actor, site))
            if condition == "paused":
                site.flags.add("great_depression_center_project_paused")
            elif condition == "control":
                site.controller = country("FOREIGN")
            else:
                actor.normal_civilian_systems = False
            runtime.run_effect("great_depression_update_public_works_repair_term", site, root=actor)
            self.assertNotIn("great_depression_public_works_repair_administration", site.modifiers)

    def test_unproved_work_times_out_once_in_either_callback_order(self):
        for native_first in (False, True):
            runtime, actor, site = self.prepared(infrastructure=5)
            site.values["damaged_building_level@infrastructure"] = 2
            self.assertTrue(self.launch(runtime, actor, site))
            self.finish(runtime, actor, site)
            runtime.advance(28)
            if native_first:
                runtime.run_effect("great_depression_timeout_reopen_depression_center", actor)
            runtime.run_effect("great_depression_process_center_project", site, root=actor)
            failure = actor.values["great_depression_project_failure_count"]
            severity = actor.values["great_depression_depression_severity"]
            runtime.run_effect("great_depression_timeout_reopen_depression_center", actor)
            runtime.run_effect("great_depression_process_center_project", site, root=actor)
            self.assertEqual(failure, 1)
            self.assertEqual(actor.values["great_depression_project_failure_count"], failure)
            self.assertEqual(actor.values["great_depression_depression_severity"], severity)
            self.assertNotIn("great_depression_reopen_depression_center", actor.values["active_missions"])

    def test_wrong_payer_site_or_episode_cannot_complete(self):
        for mismatch in ("owner", "site", "episode", "payment"):
            runtime, actor, site = self.prepared()
            self.assertTrue(self.launch(runtime, actor, site))
            key = {"owner": "plan_owner", "site": "plan_site", "episode": "plan_episode_id", "payment": "paid_action_count"}[mismatch]
            site.values["great_depression_public_works_" + key] = country("BAD") if mismatch == "owner" else state(999, actor) if mismatch == "site" else 0
            self.finish(runtime, actor, site)
            self.assertEqual(site.buildings["infrastructure"], 2)
            self.assertNotIn("great_depression_center_public_works_completed_receipt", site.flags)

    def rail_case(self):
        runtime, actor, site = self.prepared(infrastructure=5)
        capital = state(64, actor)
        alternate = state(65, actor)
        actor.values.update({"capital": capital, "owned_states": [site, capital, alternate],
                             "can_build_railway": {(site.id, capital.id), (site.id, alternate.id)},
                             "has_railway_connection": {(capital.id, alternate.id)}})
        site.values["neighbors"] = [capital, alternate]
        return runtime, actor, site, capital, alternate

    def test_rail_plan_freezes_one_real_neighbor_and_output_pair(self):
        runtime, actor, site, capital, alternate = self.rail_case()
        self.assertTrue(self.launch(runtime, actor, site))
        self.assertEqual(site.values["great_depression_public_works_rail_partner"], capital)
        self.finish(runtime, actor, site)
        calls = [call for call in runtime.native_calls if len(call) == 4 and call[0] == "build_railway"]
        self.assertEqual(calls, [("build_railway", actor.id, site.id, capital.id)])
        self.assertIn("great_depression_center_public_works_completed_receipt", site.flags)

    def test_rail_adjacency_control_network_and_ineffective_mutation_near_misses(self):
        for defect in ("adjacency", "control", "network", "native_result"):
            runtime, actor, site, capital, alternate = self.rail_case()
            if defect == "network":
                site.values["neighbors"] = [alternate]
            self.assertTrue(self.launch(runtime, actor, site))
            if defect == "adjacency":
                site.values["neighbors"] = [alternate]
            elif defect == "control":
                capital.controller = country("HOSTILE")
            elif defect == "network":
                actor.values["has_railway_connection"].clear()
            else:
                actor.values["fixture_rail_build_succeeds"] = False
            self.finish(runtime, actor, site)
            self.assertNotIn("great_depression_center_public_works_completed_receipt", site.flags)
            if defect != "native_result":
                self.assertFalse(any(call[0] == "build_railway" for call in runtime.native_calls))

    def test_coastal_port_and_wartime_air_protection_are_separate_paid_needs(self):
        for kind in ("port", "air"):
            runtime, actor, site = self.prepared(infrastructure=5)
            if kind == "port":
                site.values["coastal"] = True
            else:
                actor.values["war"] = True
            self.assertTrue(self.launch(runtime, actor, site))
            self.finish(runtime, actor, site)
            self.assertEqual(site.buildings["naval_base" if kind == "port" else "anti_air_building"], 1)
            self.assertIn("great_depression_center_public_works_completed_receipt", site.flags)

    def test_terminal_cleanup_preserves_issuance_but_removes_transient_proof(self):
        runtime, actor, site = self.prepared()
        self.assertTrue(self.launch(runtime, actor, site))
        self.finish(runtime, actor, site)
        history = {k: v for k, v in site.values.items() if "public_works_issued_" in k}
        runtime.run_effect("great_depression_clear_registered_center_runtime", actor)
        self.assertEqual({k: v for k, v in site.values.items() if "public_works_issued_" in k}, history)
        self.assertNotIn("great_depression_public_works_plan_active", site.flags)
        self.assertNotIn("great_depression_public_works_repair_administration", site.modifiers)

    def test_later_episode_can_pay_for_fresh_need_even_when_authorization_restarts(self):
        runtime, actor, site = self.prepared()
        site.values.update({"great_depression_public_works_issued_authorization_id": 1,
                            "great_depression_public_works_issued_episode_id": 34})
        self.assertTrue(self.launch(runtime, actor, site))
        self.assertEqual(site.values["great_depression_center_project_authorization_id"], 1)
        self.finish(runtime, actor, site)
        self.assertEqual(site.buildings["infrastructure"], 3)
        self.assertEqual(site.values["great_depression_public_works_issued_episode_id"], 35)

    def test_transfer_adoption_preserves_paid_payer_baseline_and_suspended_term(self):
        runtime, actor, site = self.prepared(infrastructure=5)
        site.values["damaged_building_level@infrastructure"] = 2
        self.assertTrue(self.launch(runtime, actor, site))
        required = site.values["great_depression_center_project_required_work_days"]
        original_auth = site.values["great_depression_center_project_authorization_id"]
        successor = country("BBB")
        successor.flags.add("great_depression_active")
        successor.values.update({"great_depression_active_episode_id": 72, "great_depression_depression_severity": 35,
                                 "great_depression_evolution_floor": 0, "great_depression_center_count": 0,
                                 "capital": site, "owned_states": [site]})
        successor.arrays.update({name: [] for name in actor.arrays})
        debit = len(runtime.resource_writes)
        site.owner = successor
        site.controller = successor
        runtime.run_effect("great_depression_reconcile_center_transfer", site, root=actor)
        self.assertNotIn("great_depression_public_works_repair_administration", site.modifiers)
        runtime.advance(10)
        runtime.run_effect("great_depression_select_center", site, root=successor)
        self.assertEqual(site.values["great_depression_public_works_plan_owner"], successor)
        self.assertEqual(site.values["great_depression_public_works_plan_payer"], actor)
        self.assertEqual(site.values["great_depression_public_works_plan_episode_id"], 72)
        self.assertEqual(site.values["great_depression_center_project_authorization_id"], original_auth)
        self.assertEqual(site.values["great_depression_center_project_required_work_days"], required)
        self.assertEqual(site.values["great_depression_public_works_initial_damage"], 2)
        self.assertNotIn("great_depression_public_works_repair_administration", site.modifiers)
        runtime.run_effect("great_depression_process_center_project", site, root=successor)
        self.assertIn("great_depression_public_works_repair_administration", site.modifiers)
        site.values["damaged_building_level@infrastructure"] = 1
        runtime.advance(required)
        runtime.run_effect("great_depression_process_center_project", site, root=successor)
        self.assertIn("great_depression_center_public_works_completed_receipt", site.flags)
        self.assertEqual(len(runtime.resource_writes), debit)

    def test_adoption_cannot_relabel_an_old_same_serial_as_current_issuance(self):
        runtime, actor, site = self.prepared()
        site.values.update({"great_depression_public_works_issued_authorization_id": 1,
                            "great_depression_public_works_issued_episode_id": 34})
        self.assertTrue(self.launch(runtime, actor, site))
        successor = country("BBB")
        successor.flags.add("great_depression_active")
        successor.values.update({"great_depression_active_episode_id": 72, "great_depression_depression_severity": 35,
                                 "great_depression_evolution_floor": 0, "great_depression_center_count": 0,
                                 "capital": site, "owned_states": [site]})
        successor.arrays.update({name: [] for name in actor.arrays})
        site.owner = site.controller = successor
        runtime.run_effect("great_depression_reconcile_center_transfer", site, root=actor)
        runtime.run_effect("great_depression_select_center", site, root=successor)
        self.assertEqual(site.values["great_depression_public_works_issued_episode_id"], 34)
        runtime.run_effect("great_depression_process_center_project", site, root=successor)
        runtime.advance(site.values["great_depression_center_project_required_work_days"])
        runtime.run_effect("great_depression_process_center_project", site, root=successor)
        self.assertEqual(site.buildings["infrastructure"], 3)
        self.assertIn("great_depression_center_public_works_completed_receipt", site.flags)

    def test_post_work_control_pause_resume_keeps_proof_and_native_deadline_equal(self):
        runtime, actor, site = self.prepared(infrastructure=5)
        site.values["damaged_building_level@infrastructure"] = 2
        self.assertTrue(self.launch(runtime, actor, site))
        self.finish(runtime, actor, site)
        old = site.values["great_depression_public_works_proof_deadline_day"]
        site.controller = country("OCCUPIER")
        runtime.advance(7)
        runtime.run_effect("great_depression_process_center_project", site, root=actor)
        self.assertIn("great_depression_center_project_paused", site.flags)
        self.assertNotIn("great_depression_public_works_repair_administration", site.modifiers)
        site.controller = actor
        runtime.advance(5)
        runtime.run_effect("great_depression_process_center_project", site, root=actor)
        self.assertNotIn("great_depression_center_project_paused", site.flags)
        self.assertIn("great_depression_public_works_repair_administration", site.modifiers)
        deadline = site.values["great_depression_center_project_due_day"] + 28
        self.assertGreater(deadline, old)
        self.assertEqual(site.values["great_depression_public_works_proof_deadline_day"], deadline)
        self.assertEqual(actor.values["great_depression_mission_reopen_center_deadline_day"], deadline)
        self.assertEqual(actor.values["native_mission_deadlines"]["great_depression_reopen_depression_center"], deadline)

    def test_invalid_actor_cannot_pay_or_directly_finish_accepted_work(self):
        for defect in ("missing", "civilian", "special", "nonhuman"):
            for paid in (False, True):
                runtime, actor, site = self.prepared()
                if paid:
                    self.assertTrue(self.launch(runtime, actor, site))
                    site.values["great_depression_center_project_work_days"] = site.values["great_depression_center_project_required_work_days"]
                if defect == "missing":
                    actor.exists = False
                elif defect == "civilian":
                    actor.normal_civilian_systems = False
                else:
                    actor.values["is_special_chaos_country" if defect == "special" else "is_actual_nonhuman_country"] = True
                debit = len(runtime.resource_writes)
                runtime.run_effect("great_depression_launch_regional_works_program" if not paid else "great_depression_complete_center_project", site, root=actor)
                self.assertEqual(site.buildings["infrastructure"], 2)
                self.assertEqual(len(runtime.resource_writes), debit)
                self.assertNotIn("great_depression_center_public_works_completed_receipt", site.flags)

    def test_foreign_root_cannot_strip_another_owners_repair_administration(self):
        runtime, actor, site = self.prepared(infrastructure=5)
        site.values["damaged_building_level@infrastructure"] = 2
        self.assertTrue(self.launch(runtime, actor, site))
        foreign = country("FOREIGN")
        foreign.flags.add("great_depression_active")
        foreign.values.update({"great_depression_active_episode_id": 99, "great_depression_depression_severity": 40,
                               "great_depression_evolution_floor": 0})
        runtime.run_effect("great_depression_process_center_project", site, root=foreign)
        self.assertIn("great_depression_public_works_repair_administration", site.modifiers)
        self.assertEqual(site.values["great_depression_public_works_plan_owner"], actor)

    def test_paid_works_cannot_be_reinterpreted_as_another_project_before_proof(self):
        runtime, actor, site = self.prepared()
        self.assertTrue(self.launch(runtime, actor, site))
        site.values["great_depression_center_project_work_days"] = site.values["great_depression_center_project_required_work_days"]
        site.values["great_depression_center_project_type"] = runtime.constants["constant:great_depression_center_project.finance_restoration"]
        runtime.run_effect("great_depression_complete_center_project", site, root=actor)
        self.assertEqual(site.buildings["infrastructure"], 2)
        self.assertNotIn("great_depression_center_project_completed_receipt", site.flags)
        self.assertNotIn("great_depression_center_finance_restored", site.flags)


if __name__ == "__main__":
    unittest.main()
