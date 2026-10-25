"""Actual-source closure prerequisites, not native scheduling or UI proof."""
import unittest

import test_event035_public_works as public_works
from test_event035_center_projects import ROOT, first, lex, parse_nodes, uncomment


class WorksClosureTests(unittest.TestCase):
    def prepared(self, completed=False):
        runtime, actor, site = public_works.PublicWorksTests().prepared(infrastructure=2)
        if completed:
            helper = public_works.PublicWorksTests()
            self.assertTrue(helper.launch(runtime, actor, site))
            helper.finish(runtime, actor, site)
            runtime.advance(8)
        actor.values["great_depression_phase"] = runtime.constants["constant:great_depression_phase.stabilization"]
        return runtime, actor, site

    def test_only_current_completed_works_can_enter_closure(self):
        for case in ("paid_stable", "no_works", "failed", "stale", "panic", "closed"):
            with self.subTest(case=case):
                runtime, actor, site = self.prepared(case != "no_works")
                if case == "failed":
                    site.flags.discard("great_depression_center_public_works_completed_receipt")
                    site.flags.add("great_depression_center_project_failed_receipt")
                elif case == "stale":
                    site.values["great_depression_public_works_last_completed_episode_id"] = 34
                elif case == "panic":
                    actor.values["great_depression_phase"] = runtime.constants["constant:great_depression_phase.panic_and_contraction"]
                elif case == "closed":
                    site.flags.add("great_depression_center_lasting_capacity_completed_receipt")
                eligible = runtime.test_trigger("great_depression_center_lasting_capacity_target_is_valid", site, root=actor)
                self.assertEqual(eligible, case == "paid_stable")

    def test_direct_stale_or_unfunded_click_does_not_pay_or_begin_work(self):
        for defect in ("no_works", "panic", "stale", "depleted"):
            with self.subTest(defect=defect):
                runtime, actor, site = self.prepared(defect != "no_works")
                if defect == "panic":
                    actor.values["great_depression_phase"] = runtime.constants["constant:great_depression_phase.panic_and_contraction"]
                elif defect == "stale":
                    site.values["great_depression_public_works_last_completed_episode_id"] = 34
                elif defect == "depleted":
                    actor.resources["fuel"] = 0
                debit = len(runtime.resource_writes)
                action_count = actor.values.get("great_depression_successful_action_count", 0)
                old_auth = site.values.get("great_depression_center_project_authorization_id", 0)
                runtime.run_effect("great_depression_convert_works_into_lasting_capacity", site, root=actor)
                self.assertEqual(len(runtime.resource_writes), debit)
                self.assertEqual(actor.values.get("great_depression_successful_action_count", 0), action_count)
                self.assertEqual(site.values.get("great_depression_center_project_authorization_id", 0), old_auth)

    def test_zero_identity_bad_kind_and_active_plan_do_not_certify_a_closer(self):
        for defect in ("zero_auth", "missing_kind", "outside_kind", "active_plan", "paid_plan"):
            with self.subTest(defect=defect):
                runtime, actor, site = self.prepared(True)
                if defect == "zero_auth":
                    site.values["great_depression_public_works_last_completed_authorization_id"] = 0
                elif defect == "missing_kind":
                    del site.values["great_depression_public_works_last_completed_kind"]
                elif defect == "outside_kind":
                    site.values["great_depression_public_works_last_completed_kind"] = 10
                else:
                    site.flags.add("great_depression_public_works_plan_active" if defect == "active_plan" else "great_depression_public_works_paid_receipt")
                self.assertFalse(runtime.test_trigger("great_depression_center_lasting_capacity_target_is_valid", site, root=actor))

    def test_closer_actual_ai_formula_has_nonzero_valid_willingness(self):
        path = ROOT / "common/decisions/035_great_depression_decisions.txt"
        nodes, _ = parse_nodes(lex(uncomment(path.read_text(encoding="utf-8-sig"))), 0, str(path))
        category = first(nodes, "great_depression_category")
        ai = first(first(category, "great_depression_convert_works_into_lasting_capacity"), "ai_will_do")
        for valid in (False, True):
            runtime, actor, site = self.prepared(valid)
            actor.values["great_depression_ai_profile"] = runtime.constants["constant:great_depression_ai_profile.relief_coalition"]
            runtime.root, runtime.scope_stack = actor, [actor]
            score = runtime._value(first(ai, "base"))
            for modifier in (n.value for n in ai if n.key == "modifier"):
                predicate = [n for n in modifier if n.key not in ("add", "factor")]
                passed = True
                for node in predicate:
                    if node.key == "FROM":
                        runtime.scope_stack.append(site)
                        try:
                            passed = passed and runtime._conditions(node.value, site)
                        finally:
                            runtime.scope_stack.pop()
                    else:
                        passed = passed and runtime._condition(node, actor)
                if passed:
                    add, factor = first(modifier, "add"), first(modifier, "factor")
                    if add is not None:
                        score += runtime._value(add)
                    if factor is not None:
                        score *= runtime._value(factor)
            self.assertEqual(score > 0, valid)
            if valid:
                self.assertEqual(score, 34)


if __name__ == "__main__":
    unittest.main()
