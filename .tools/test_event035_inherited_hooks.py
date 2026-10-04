"""Actual-source integration of Event35 accepted receipts and paid callbacks.

Reuse the reviewed native-fixture extension retained in the architect handoff.
This does not prove public regional validation, engine execution or salvage.
"""
from pathlib import Path
import re
import unittest

REPO = Path(__file__).resolve().parents[1]
HANDOFF = REPO / "docs/plans/035_great_depression_plans/subagent_handoffs/inherited_liability_consumer_implementation_2026-10-03.md"
code = re.search(r"```python\s*\n(.*?)\n```", HANDOFF.read_text(encoding="utf-8-sig"), re.S).group(1)
namespace = {}
exec(compile(code.split("done = []", 1)[0], str(HANDOFF), "exec"), namespace)
e35, BaseRuntime = namespace["e35"], namespace["Runtime"]
H, L, O = namespace["H"], namespace["L"], namespace["O"]


class Runtime(BaseRuntime):
    NATIVE_PRIMITIVES = BaseRuntime.NATIVE_PRIMITIVES | {"clamp_temp_variable"}

    def _native_effect(self, key, value, scope, line):
        if key == "clamp_temp_variable":
            args = {node.key: node.value for node in value}
            amount = self._variable(args["var"])
            if "min" in args:
                amount = max(amount, self._value(args["min"]))
            if "max" in args:
                amount = min(amount, self._value(args["max"]))
            self._set_temp(args["var"], amount)
            return
        super()._native_effect(key, value, scope, line)

    def _value(self, token):
        if token == "id":
            return self.current.id
        if isinstance(token, str) and token.startswith("building_level@"):
            return self.current.buildings.get(token.split("@", 1)[1], 0)
        return super()._value(token)

    def _condition(self, node, scope):
        if node.key == "has_war":
            return scope.values["fixture_at_war"] == (node.value == "yes")
        if node.key == "is_core_of":
            return self._value(node.value) in scope.values.get("fixture_core_countries", [])
        if node.key == "impassable":
            return scope.values.get("fixture_impassable", False) == (node.value == "yes")
        return super()._condition(node, scope)


def prepared():
    _, owner, site = e35.registered_case()
    rt = Runtime()
    rt.states = {site.id: site}
    rt.global_arrays["states"] = [site.id]
    site.values["fixture_core_countries"] = [owner]
    owner.values["fixture_at_war"] = False
    return rt, owner, site


def accept_region(rt, owner, site, receipt=11, **overrides):
    # Enter only the already-validated companion's real apply/append branch.
    fields = {
        "episode_id": owner.values["great_depression_active_episode_id"],
        "event34_episode_id": 7, "state_id": site.id, "role": 1,
        "project_profile": 2, "project_stage": 3, "protection": 2,
        "fragility": 2, "control": 0, "damage": 0,
        "receipt_id": receipt, "collapse_receipt_id": 70,
        "legacy_receipt_id": -1, "corridor_receipt_id": -1, "exhaustion": 0,
    }
    fields.update(overrides)
    for key, value in fields.items():
        owner.values["great_depression_region_call_" + key] = value
    owner.values["great_depression_region_resolved_state"] = site
    owner.flags.add("great_depression_region_validated")
    rt.run_effect("great_depression_apply_inherited_region", owner, root=owner)
    return len(owner.arrays[H + "receipt_id_entries"]) - 1


class InheritedHookTests(unittest.TestCase):
    def test_equal_visible_stage_separates_supplied_history_from_flat_baseline(self):
        results = []
        baseline_file = "docs/plans/035_great_depression_plans/audit_inputs/liability_hooks_2026_10_03/035_great_depression_effects_before.txt"
        for adverse in (False, True):
            rt, owner, site = prepared()
            owner.flags.add("great_depression_event34_inherited")
            accept_region(rt, owner, site, project_profile=1,
                          project_stage=3 if adverse else 2,
                          protection=2 if adverse else 1,
                          fragility=2 if adverse else 0, damage=0, exhaustion=0)
            # Declare equal current physical state; only source history varies.
            rt.run_effect("great_depression_clear_center_physical_stage", site, root=owner)
            site.flags.add("great_depression_center_distressed")
            rt.run_effect("great_depression_rebuild_hidden_components", owner)
            after = (owner.values["great_depression_hidden_credit_stress"],
                     owner.values["great_depression_hidden_industrial_stress"])
            rt.effect_defs.update(e35.read_definitions(baseline_file))
            rt.run_effect("great_depression_rebuild_hidden_components", owner)
            before = (owner.values["great_depression_hidden_credit_stress"],
                      owner.values["great_depression_hidden_industrial_stress"])
            results.append((before, after))
        self.assertEqual(results[0][0], results[1][0])
        self.assertEqual(results[1][1][0], results[0][1][0] + 1)
        self.assertEqual(results[1][1][1], results[0][1][1] + 1)

    def test_real_event34_row_keeps_baseline_hidden_pressure(self):
        # Event 34 has no regional project system: profile, project stage,
        # protection, fragility, exhaustion, legacy and corridor fields arrive
        # unavailable, while control and damage come from the live map.
        baseline_file = "docs/plans/035_great_depression_plans/audit_inputs/liability_hooks_2026_10_03/035_great_depression_effects_before.txt"
        components = ("credit", "demand", "trade", "industrial", "fiscal", "social", "war")
        for damage in (0, 1):
            with self.subTest(damage=damage):
                rt, owner, site = prepared()
                owner.flags.add("great_depression_event34_inherited")
                accept_region(rt, owner, site, project_profile=-1, project_stage=-1,
                              protection=-1, fragility=-1, control=0, damage=damage,
                              legacy_receipt_id=-1, corridor_receipt_id=-1, exhaustion=-1)
                rt.run_effect("great_depression_rebuild_hidden_components", owner)
                after = [owner.values["great_depression_hidden_%s_stress" % name] for name in components]
                after.append(owner.values["great_depression_hidden_net_pressure"])
                self.assertEqual(owner.values[O + "project_fact_count"], 0)
                rt.effect_defs.update(e35.read_definitions(baseline_file))
                rt.run_effect("great_depression_rebuild_hidden_components", owner)
                before = [owner.values["great_depression_hidden_%s_stress" % name] for name in components]
                before.append(owner.values["great_depression_hidden_net_pressure"])
                self.assertEqual(after, before)

    def test_national_hidden_rebuild_consumes_supplied_exhaustion_once(self):
        rt, owner, site = prepared()
        accept_region(rt, owner, site, project_profile=1, project_stage=2,
                      protection=1, fragility=0, damage=0, exhaustion=0)
        rt.run_effect("great_depression_rebuild_hidden_components", owner)
        before = owner.values["great_depression_hidden_demand_stress"]
        accept_region(rt, owner, site, receipt=12, project_profile=1,
                      project_stage=2, protection=1, fragility=0, damage=0,
                      exhaustion=0.25)
        rt.run_effect("great_depression_rebuild_hidden_components", owner)
        self.assertEqual(owner.values["great_depression_hidden_demand_stress"],
                         before + rt.constants["constant:great_depression_hidden_component.demand_distressed_center"])
        first = owner.values["great_depression_hidden_demand_stress"]
        rt.run_effect("great_depression_rebuild_hidden_components", owner)
        self.assertEqual(owner.values["great_depression_hidden_demand_stress"], first)

    def test_actual_append_registers_checkpoint_and_paid_completion_settles_once(self):
        rt, owner, site = prepared()
        row = accept_region(rt, owner, site)
        self.assertEqual(len(owner.arrays[L + "checkpoint_day_entries"]), 1)
        self.assertEqual(owner.arrays[L + "receipt_id_entries"][row], 11)
        self.assertEqual(owner.arrays[L + "outcome_entries"][row], 0)
        auth = namespace["paid_reopen"](rt, owner, site)
        self.assertEqual(owner.arrays[L + "outcome_entries"][row], 1)
        self.assertEqual(owner.arrays[L + "resolution_authorization_id_entries"][row], auth)
        before = list(owner.arrays[L + "outcome_entries"])
        rt.run_effect("great_depression_complete_center_project", site, root=owner)
        self.assertEqual(owner.arrays[L + "outcome_entries"], before)
        self.assertNotIn(O + "resolution_state_id", owner.values)

    def test_paid_liquidation_is_an_exact_source_disposition(self):
        rt, owner, site = prepared()
        row = accept_region(rt, owner, site)
        owner.values["great_depression_depression_severity"] = 80
        owner.values["great_depression_centers_liquidated_count"] = 0
        owner.values["great_depression_liquidation_factory_levels_lost"] = 0
        owner.values["great_depression_doctrine_switch_count"] = 0
        rt.run_effect("great_depression_refresh_costs", owner)
        before = site.buildings["industrial_complex"]
        rt.run_effect("great_depression_abandon_selected_center", site, root=owner)
        self.assertLess(site.buildings["industrial_complex"], before)
        self.assertEqual(owner.arrays[L + "outcome_entries"][row], 2)
        self.assertNotIn(O + "disposition_paid", owner.flags)

    def test_temporary_control_loss_is_not_permanent_transfer(self):
        rt, owner, site = prepared()
        row = accept_region(rt, owner, site)
        other = e35.country("BBB")
        site.controller = other
        rt.run_effect("great_depression_reconcile_center_transfer", site, root=owner)
        self.assertEqual(owner.arrays[L + "outcome_entries"][row], 0)

    def test_owner_change_settles_former_owner_without_cloning_source(self):
        rt, owner, site = prepared()
        row = accept_region(rt, owner, site)
        other = e35.country("BBB")
        site.owner = site.controller = other
        rt.run_effect("great_depression_reconcile_center_transfer", site, root=owner)
        self.assertEqual(owner.arrays[L + "outcome_entries"][row], 4)
        self.assertFalse(any(key.startswith(H) for key in other.arrays))

    def test_episode_summary_and_native_cleanup_preserve_unresolved_history(self):
        rt, owner, site = prepared()
        row = accept_region(rt, owner, site)
        rt.run_effect("great_depression_freeze_episode_summary", owner)
        self.assertEqual(owner.values[O + "last_unresolved_count"], 1)
        self.assertEqual(owner.arrays[L + "outcome_entries"][row], 0)
        rt.run_effect("great_depression_clear_registered_center_runtime", owner)
        self.assertNotIn(O + "view_episode_id", owner.values)
        self.assertEqual(owner.arrays[L + "outcome_entries"][row], 0)



if __name__ == "__main__":
    unittest.main(verbosity=2)
