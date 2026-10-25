"""Exercise actual payment/project/retirement/refund paths with native fixtures."""
import unittest

import test_event035_public_works as public_works
from test_event035_center_projects import country


class WorksEscrowTests(unittest.TestCase):
    def prepared(self):
        helper = public_works.PublicWorksTests()
        runtime, actor, site = helper.prepared()
        before = dict(actor.resources)
        self.assertTrue(helper.launch(runtime, actor, site))
        self.assertIn("great_depression_works_escrow_open", site.flags)
        self.assertIn("great_depression_works_escrow_full_unused_return_authorized", site.flags)
        return helper, runtime, actor, site, before

    def test_payment_capture_and_partial_failure_return_exact_unused_only(self):
        helper, runtime, actor, site, before = self.prepared()
        required = site.values["great_depression_works_escrow_required_work"]
        elapsed = 48
        runtime.advance(elapsed)
        runtime.run_effect("great_depression_process_center_project", site, root=actor)
        gross = {kind: site.values["great_depression_works_escrow_gross_" + kind] for kind in ("manpower", "fuel", "trains")}
        unused = {kind: int(gross[kind]) * (int(required) - elapsed) // int(required) for kind in gross}
        runtime.run_effect("great_depression_fail_center_project", site, root=actor)
        self.assertIn("great_depression_works_escrow_settled", site.flags)
        self.assertIn("great_depression_works_escrow_retired", site.flags)
        for kind in gross:
            resource = "train_equipment" if kind == "trains" else kind
            self.assertEqual(actor.resources[resource], before[resource] - gross[kind] + unused[kind])
            self.assertEqual(site.values["great_depression_works_escrow_settlement_unused_" + kind], unused[kind])
        credits = len(runtime.resource_writes)
        failure = actor.values["great_depression_project_failure_count"]
        for _ in range(3):
            runtime.run_effect("great_depression_fail_center_project", site, root=actor)
            runtime.run_effect("great_depression_works_escrow_retire_and_settle", site, root=actor)
        self.assertEqual(len(runtime.resource_writes), credits)
        self.assertEqual(actor.values["great_depression_project_failure_count"], failure)
        runtime.advance(required)
        runtime.run_effect("great_depression_process_center_project", site, root=actor)
        self.assertEqual(site.buildings["infrastructure"], 2)

    def test_completed_work_returns_no_materials(self):
        helper, runtime, actor, site, before = self.prepared()
        after_payment = dict(actor.resources)
        helper.finish(runtime, actor, site)
        self.assertIn("great_depression_works_escrow_settled", site.flags)
        self.assertEqual(actor.resources, after_payment)
        for kind in ("manpower", "fuel", "trains"):
            self.assertEqual(site.values["great_depression_works_escrow_settlement_unused_" + kind], 0)

    def test_registered_cleanup_returns_unused_and_cannot_continue(self):
        helper, runtime, actor, site, before = self.prepared()
        runtime.run_effect("great_depression_clear_registered_center_runtime", actor)
        self.assertIn("great_depression_works_escrow_settled", site.flags)
        for kind in ("manpower", "fuel", "train_equipment"):
            self.assertEqual(actor.resources[kind], before[kind])
        self.assertNotIn("great_depression_public_works_plan_active", site.flags)
        credit_count = len(runtime.resource_writes)
        runtime.run_effect("great_depression_clear_registered_center_runtime", actor)
        runtime.run_effect("great_depression_works_escrow_retire_and_settle", site, root=actor)
        self.assertEqual(len(runtime.resource_writes), credit_count)

    def test_missing_original_payer_leaves_frozen_pending_after_cleanup(self):
        helper, runtime, actor, site, before = self.prepared()
        actor.exists = False
        runtime.run_effect("great_depression_clear_registered_center_runtime", actor)
        self.assertIn("great_depression_works_escrow_pending_return", site.flags)
        self.assertIn("great_depression_works_escrow_retired", site.flags)
        self.assertNotIn("great_depression_works_escrow_settled", site.flags)
        credits = len(runtime.resource_writes)
        actor.exists = True
        runtime.run_effect("great_depression_works_escrow_retire_and_settle", site, root=actor)
        self.assertIn("great_depression_works_escrow_settled", site.flags)
        self.assertGreater(len(runtime.resource_writes), credits)
        for kind in ("manpower", "fuel", "train_equipment"):
            self.assertEqual(actor.resources[kind], before[kind])

    def test_foreign_root_cannot_request_or_settle_valid_funding(self):
        helper, runtime, actor, site, before = self.prepared()
        foreign = country("OTHER")
        old = dict(site.values)
        debit = len(runtime.resource_writes)
        runtime.run_effect("great_depression_works_escrow_retire_and_settle", site, root=foreign)
        self.assertNotIn("great_depression_works_escrow_retired", site.flags)
        self.assertEqual(len(runtime.resource_writes), debit)
        self.assertEqual(site.values["great_depression_works_escrow_request_payer"], old["great_depression_works_escrow_request_payer"])

    def test_country_queue_keeps_unacknowledged_then_drains_original_payer(self):
        helper, runtime, actor, site, before = self.prepared()
        actor.exists = False
        runtime.run_effect("great_depression_clear_registered_center_runtime", actor)
        runtime.temp_frames[0]["break"] = 1
        runtime.temp_frames[0]["great_depression_works_escrow_sites_break"] = 1
        runtime.temp_frames[0]["great_depression_works_escrow_kept_break"] = 1
        runtime.run_effect("great_depression_works_escrow_process_retired_sites", actor)
        self.assertEqual(actor.arrays["great_depression_works_escrow_sites"], [site])
        actor.exists = True
        runtime.run_effect("great_depression_works_escrow_process_retired_sites", actor)
        self.assertEqual(actor.arrays["great_depression_works_escrow_sites"], [])
        for kind in ("manpower", "fuel", "train_equipment"):
            self.assertEqual(actor.resources[kind], before[kind])

    def test_transfer_failure_credits_original_payer_not_successor(self):
        helper, runtime, actor, site, before = self.prepared()
        runtime.advance(20)
        runtime.run_effect("great_depression_process_center_project", site, root=actor)
        successor = country("BBB")
        successor.flags.add("great_depression_active")
        # Supply the national lifecycle fields a real accepted API start creates.
        successor.values.update(actor.values)
        successor.values.update({"great_depression_active_episode_id": 72, "great_depression_depression_severity": 35,
                                 "great_depression_episode_peak_severity": 35, "great_depression_phase": 1,
                                 "great_depression_evolution_floor": 0, "great_depression_center_count": 0,
                                 "capital": site, "owned_states": [site]})
        successor.arrays.update({name: [] for name in actor.arrays})
        site.owner = site.controller = successor
        runtime.run_effect("great_depression_reconcile_center_transfer", site, root=actor)
        runtime.advance(10)
        runtime.run_effect("great_depression_select_center", site, root=successor)
        self.assertEqual(site.values["great_depression_works_escrow_live_owner"], successor)
        self.assertEqual(site.values["great_depression_works_escrow_live_episode"], 72)
        self.assertEqual(site.values["great_depression_works_escrow_funded_episode"], 35)
        self.assertEqual(site.values["great_depression_works_escrow_payer"], actor)
        successor_before = dict(successor.resources)
        runtime.run_effect("great_depression_fail_center_project", site, root=successor)
        self.assertIn("great_depression_works_escrow_settled", site.flags)
        for kind in ("manpower", "fuel", "train_equipment"):
            self.assertGreater(actor.resources[kind], before[kind] - site.values["great_depression_works_escrow_gross_" + ("trains" if kind == "train_equipment" else kind)])
        for kind in ("manpower", "fuel", "train_equipment"):
            self.assertEqual(successor.resources.get(kind, 0), successor_before.get(kind, 0))

    def test_full_refund_cannot_restore_used_auth_or_duplicate_materials(self):
        helper, runtime, actor, site, before = self.prepared()
        runtime.run_effect("great_depression_fail_center_project", site, root=actor)
        first = dict(actor.resources)
        runtime.advance(8)
        self.assertTrue(helper.launch(runtime, actor, site))
        self.assertNotIn("great_depression_works_escrow_retired", site.flags)
        debit = len(runtime.resource_writes)
        runtime.run_effect("great_depression_works_escrow_settle", site, root=actor)
        self.assertEqual(len(runtime.resource_writes), debit)
        self.assertIn("great_depression_works_escrow_open", site.flags)
        self.assertNotIn("great_depression_works_escrow_settled", site.flags)


if __name__ == "__main__":
    unittest.main()
