"""Execute physical destruction and its source dispatch with strict temp frames.

Shared Chaos, Board refresh and achievements use explicit invocation spies.
This does not emulate HOI4 scheduling, UI, native stockpiles or save/reload.
"""
import re
import unittest

from test_event025_custody import CustodyRuntime, PREFIX, TRIGGERS
from test_event025_active_hazards import hazard_branches, PULSE
from test_event025_final_recovery import ROOT, Country, block


def source(path):
    return re.sub(r"#[^\n]*", "", (ROOT / path).read_text(encoding="utf-8-sig"))


POLICY = source("common/scripted_effects/025_alien_technology_in_antarctica_custody_policy_effects.txt")
GATES = source("common/scripted_triggers/025_alien_technology_in_antarctica_custody_policy_triggers.txt")
EVOLUTION = source("common/scripted_triggers/025_alien_technology_in_antarctica_evolution_gate_triggers.txt")
RUNTIME = source("common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt")
DYNAMIC = source("common/scripted_effects/chaosx_dynamic_effects.txt")
CONSTANTS = source("common/script_constants/025_alien_technology_in_antarctica_custody_constants.txt")
HOLDER_TRIGGERS = source("common/scripted_triggers/025_alien_technology_in_antarctica_holder_triggers.txt")
HOLDER_EFFECTS = source("common/scripted_effects/025_alien_technology_in_antarctica_holder_effects.txt")


class PolicyRuntime(CustodyRuntime):
    def __init__(self, countries):
        super().__init__(countries)
        self.effects.update({name: block(name, POLICY) for name in re.findall(r"^(chaosx_nr25_\w+)\s*=\s*\{", POLICY, re.M)})
        for name in ("chaosx_nr25_execute_evolution_action", "chaosx_nr25_execute_evolution_action_unchecked", "chaosx_nr25_clamp_values"):
            self.effects[name] = block(name, RUNTIME)
        self.effects["remove_support_equipment_from_stockpile"] = block("remove_support_equipment_from_stockpile", DYNAMIC)
        for name in ("chaosx_nr25_raise_chaos", "chaosx_nr25_prepare_board_slots",
                     "chaosx_nr25_update_achievement_tracking", "chaosx_nr25_check_evolution_gates"):
            self.effects[name] = [("add_to_variable", [(name + "_observed_calls", "1")])]
        self.triggers.update({name: block(name, GATES) for name in re.findall(r"^(chaosx_nr25_\w+)\s*=\s*\{", GATES, re.M)})
        self.triggers.update({name: block(name, HOLDER_TRIGGERS) for name in re.findall(r"^(chaosx_nr25_\w+)\s*=\s*\{", HOLDER_TRIGGERS, re.M)})
        for name in re.findall(r"^(chaosx_nr25_\w+_evolution_in_force)\s*=\s*\{", EVOLUTION, re.M):
            self.triggers[name] = block(name, EVOLUTION)
        self.effects["chaosx_nr25_record_casualties"] = [("add_to_temp_variable", [("casualty_calls", "1")])]
        self.effects["chaosx_nr25_check_dependence_accident"] = block("chaosx_nr25_check_dependence_accident", HOLDER_EFFECTS)
        # The accident body without its report event, which is scheduling.
        self.effects["chaosx_nr25_trigger_dependence_accident"] = [
            (key, data) for key, data in block("chaosx_nr25_trigger_dependence_accident", HOLDER_EFFECTS)
            if key != "country_event"]
        self.effects["chaosx_nr25_publish_dependence_crisis"] = []
        self.temporary["casualty_calls"] = 0
        # chaosx_nr25_order_ready is the shared action-cooldown check that
        # chaosx_nr25_base_action_available reads.
        for name in ("chaosx_nr25_evolution_technology_changes_users_action_available",
                     "chaosx_nr25_base_action_available", "chaosx_nr25_order_ready",
                     "chaosx_nr25_aftermath_action_available",
                     "chaosx_nr25_evolution_v_holder_valid", "chaosx_nr25_v_material_holder_valid"):
            self.triggers[name] = block(name, TRIGGERS)
        for key, value in re.findall(r"^\s*(\w+)\s*=\s*(-?\d+(?:\.\d+)?)\s*$", CONSTANTS, re.M):
            self.constants["constant:chaosx_nr25_custody_policy." + key] = float(value)
        self.removed_missions = []

    def execute(self, nodes, actor):
        # Preserve the entire if/else sequence when extending primitive effects.
        # The inherited dispatcher recursively invokes this method for bodies.
        adapted = []
        for key, data in nodes:
            if key in ("add_equipment_to_stockpile", "add_stability", "clamp_variable", "remove_mission"):
                token = "policy_primitive_" + str(len(self.effects))
                self.effects[token] = [("policy_native_primitive", (key, data))]
                adapted.append((token, "yes"))
            elif key == "policy_native_primitive":
                native, argument = data
                if native == "add_equipment_to_stockpile":
                    args = dict(argument)
                    var = "num_equipment@" + args["type"]
                    actor.values[var] = actor.values.get(var, 0) + self.value(args["amount"], actor)
                elif native == "add_stability":
                    actor.values["has_stability"] += self.value(argument, actor)
                elif native == "remove_mission":
                    self.removed_missions.append(argument)
                elif native == "clamp_variable":
                    args = dict(argument)
                    value = actor.values.get(args["var"], 0)
                    if "min" in args: value = max(value, self.value(args["min"], actor))
                    if "max" in args: value = min(value, self.value(args["max"], actor))
                    actor.values[args["var"]] = value
            else:
                adapted.append((key, data))
        super().execute(adapted, actor)


class DestructionPolicyTests(unittest.TestCase):
    def fixture(self, dependence=90):
        actor = Country(1, flags={"chaosx_nr25_participant", "chaosx_nr25_aftermath_open",
                                 PREFIX + "event025_recorded", "learned_technology"})
        actor.values.update({"num_equipment@support_equipment": 50, "has_stability": 0.02,
                             "chaosx_nr25_dependence": dependence, "chaosx_nr25_scientific_capacity": 1,
                             "chaosx_nr25_action_cooldown": 0, "chaosx_nr25_last_action": 9,
                             "chaosx_nr25_dependence_safe_days": 50, "chaosx_nr25_dependence_stable_days": 50})
        rt = PolicyRuntime([actor])
        rt.targets[PREFIX + "event025_owner"] = actor
        rt.global_flags = {PREFIX + "event025_claimed", "chaosx_nr25_final_recovery_resolved",
                           "chaosx_nr25_evolution_technology_changes_users", "chaosx_nr25_aftermath_active"}
        rt.run(PREFIX + "ledger_initialize_core_custody", actor)
        rt.temporary["chaosx_nr25_evolution_action"] = rt.constants["constant:chaosx_nr25_evolution_action.destroy"]
        rt.temporary["chaosx_nr25_destruction_applied"] = 0
        return rt, actor

    def run_policy(self, rt, actor):
        rt.run("chaosx_nr25_execute_evolution_action", actor)

    def test_exact_resources_retire_material_and_pay_once(self):
        rt, actor = self.fixture()
        self.run_policy(rt, actor)
        self.assertEqual(actor.values["num_equipment@support_equipment"], 0)
        self.assertAlmostEqual(actor.values["has_stability"], 0)
        self.assertEqual(actor.values["chaosx_nr25_dependence"], 30)
        self.assertEqual(rt.temporary["chaosx_nr25_destruction_applied"], 1)
        self.assertIn(PREFIX + "core_destroyed", rt.global_flags)
        self.assertNotIn(PREFIX + "core_custodian", rt.targets)
        self.assertIs(rt.targets[PREFIX + "event025_owner"], actor)
        self.assertIn("learned_technology", actor.flags)
        self.assertFalse(rt.condition(rt.triggers["chaosx_nr25_active_material_incidents_allowed"], actor))
        paid_values = actor.values.copy()
        self.run_policy(rt, actor)
        self.assertEqual(actor.values, paid_values)
        self.assertEqual(rt.temporary["chaosx_nr25_destruction_applied"], 0)

    def test_rejected_clicks_have_no_cost_cooldown_or_policy_mutation(self):
        for reason in ("support", "stability", "disabled", "cooldown", "staff", "capitulated", "subject", "no_material"):
            with self.subTest(reason=reason):
                rt, actor = self.fixture()
                if reason == "support": actor.values["num_equipment@support_equipment"] = 49
                if reason == "stability": actor.values["has_stability"] = 0.019
                if reason == "disabled": rt.global_flags.add("events_log_disabled_evolution_25_25_5")
                if reason == "cooldown": actor.values["chaosx_nr25_action_cooldown"] = 20
                if reason == "staff": actor.values["chaosx_nr25_scientific_capacity"] = 0
                if reason == "capitulated": actor.capitulated = True
                if reason == "subject": actor.subject = True
                if reason == "no_material": rt.targets.pop(PREFIX + "core_custodian")
                values, flags = actor.values.copy(), actor.flags.copy()
                self.run_policy(rt, actor)
                self.assertEqual((actor.values, actor.flags), (values, flags))
                self.assertEqual(rt.temporary["chaosx_nr25_destruction_applied"], 0)

    def test_lower_dependence_is_clamped_and_running_containment_is_cancelled(self):
        rt, actor = self.fixture(5)
        actor.flags.update({"chaosx_nr25_phase_mission_active", "chaosx_nr25_contain_systems_attempted"})
        actor.values["chaosx_nr25_phase_mission_kind"] = rt.constants["constant:chaosx_nr25_phase_mission.contain_alien_systems"]
        self.run_policy(rt, actor)
        self.assertEqual(actor.values["chaosx_nr25_dependence"], 0)
        self.assertNotIn("chaosx_nr25_phase_mission_active", actor.flags)
        self.assertEqual(rt.removed_missions, ["chaosx_nr25_contain_alien_systems_mission"])
        self.assertEqual(actor.values["chaosx_nr25_dependence_safe_days"], 0)
        self.assertEqual(actor.values["chaosx_nr25_dependence_stable_days"], 0)

    def test_fragment_holder_can_destroy_during_active_race_containment(self):
        rt, actor = self.fixture()
        rt.global_flags.discard("chaosx_nr25_final_recovery_resolved")
        rt.global_flags.discard("chaosx_nr25_aftermath_active")
        rt.global_flags.add("chaosx_nr25_active")
        rt.targets.pop(PREFIX + "core_custodian")
        actor.flags.discard(PREFIX + "core_holder")
        actor.flags.discard(PREFIX + "event025_recorded")
        rt.temporary.update({PREFIX + "fragment_assigned": 0, PREFIX + "fragment_id": 1, PREFIX + "fragment_role": 1})
        rt.run(PREFIX + "ledger_assign_fragment", actor)
        actor.flags.add("chaosx_nr25_phase_mission_active")
        actor.values["chaosx_nr25_phase_mission_kind"] = rt.constants["constant:chaosx_nr25_phase_mission.contain_alien_systems"]
        self.run_policy(rt, actor)
        self.assertEqual(actor.values["chaosx_nr25_fragment_count"], 0)
        self.assertNotIn("chaosx_nr25_phase_mission_active", actor.flags)
        self.assertEqual(rt.temporary["chaosx_nr25_destruction_applied"], 1)

    def test_ledger_rejection_cannot_charge_or_publish_success(self):
        rt, actor = self.fixture()
        rt.effects[PREFIX + "ledger_destroy_physical_custody"] = []
        values, flags = actor.values.copy(), actor.flags.copy()
        self.run_policy(rt, actor)
        self.assertEqual((actor.values, actor.flags), (values, flags))
        self.assertEqual(rt.temporary["chaosx_nr25_destruction_applied"], 0)

    def test_unrelated_phase_projects_reject_destruction_in_race_and_aftermath(self):
        for active_race in (False, True):
            with self.subTest(active_race=active_race):
                rt, actor = self.fixture()
                if active_race:
                    rt.global_flags.discard("chaosx_nr25_final_recovery_resolved")
                    rt.global_flags.add("chaosx_nr25_active")
                actor.flags.add("chaosx_nr25_phase_mission_active")
                actor.values["chaosx_nr25_phase_mission_kind"] = rt.constants["constant:chaosx_nr25_phase_mission.organize"]
                values, flags = actor.values.copy(), actor.flags.copy()
                self.run_policy(rt, actor)
                self.assertEqual((actor.values, actor.flags), (values, flags))
                self.assertEqual(rt.removed_missions, [])

    def test_corrupt_fragment_receipt_rejects_destruction_without_payment(self):
        rt, actor = self.fixture()
        rt.temporary.update({PREFIX + "fragment_assigned": 0, PREFIX + "fragment_id": 1, PREFIX + "fragment_role": 1})
        rt.run(PREFIX + "ledger_assign_fragment", actor)
        rt.global_values[PREFIX + "fragment_1_role"] = 7
        values, flags = actor.values.copy(), actor.flags.copy()
        self.run_policy(rt, actor)
        self.assertEqual((actor.values, actor.flags), (values, flags))
        self.assertIs(rt.targets[PREFIX + "core_custodian"], actor)
        self.assertIs(rt.targets[PREFIX + "fragment_owner_1"], actor)

    def test_native_blocked_cost_and_risk_consequence_have_localisation(self):
        loc = (ROOT / "localisation/english/025_alien_technology_in_antarctica_l_english.yml").read_text(encoding="utf-8-sig")
        self.assertRegex(loc, re.compile(r'^chaosx_nr25_dependence_destroy_cost_blocked: "\[This.GetChaosxNr25DestroyMaterialCost\]"$', re.M))
        effect = re.search(r'^chaosx_nr25_dependence_destroy_effect: "([^"]+)"', loc, re.M)[1]
        self.assertIn("raises Exposure Risk", effect)

    def test_retired_material_rejects_even_a_stale_integration_dispatch(self):
        rt, actor = self.fixture()
        self.run_policy(rt, actor)
        rt.temporary["chaosx_nr25_evolution_action"] = rt.constants["constant:chaosx_nr25_evolution_action.integrate"]
        values, flags = actor.values.copy(), actor.flags.copy()
        self.run_policy(rt, actor)
        self.assertEqual((actor.values, actor.flags), (values, flags))

    def test_new_material_rearms_incidents_after_an_earlier_retirement(self):
        rt, actor = self.fixture()
        self.run_policy(rt, actor)
        actor.values["chaosx_nr25_dependence"] = 90
        # After the race, accidents come from the holder watch.
        rt.run("chaosx_nr25_check_dependence_accident", actor)
        self.assertEqual(actor.values["chaosx_nr25_dependence"], 90)
        self.assertEqual(rt.temporary["casualty_calls"], 0)
        rt.temporary.update({PREFIX + "fragment_assigned": 0, PREFIX + "fragment_id": 2, PREFIX + "fragment_role": 2})
        rt.run(PREFIX + "ledger_assign_fragment", actor)
        self.assertTrue(rt.condition(rt.triggers["chaosx_nr25_active_material_incidents_allowed"], actor))
        self.assertEqual(actor.values["chaosx_nr25_fragment_count"], 1)
        actor.flags.add("chaosx_nr25_dependence_started")
        rt.run("chaosx_nr25_check_dependence_accident", actor)
        self.assertEqual(rt.temporary["casualty_calls"], 1)
        self.assertIn("chaosx_nr25_dependence_accident", actor.flags)

    def test_policy_retires_owned_fragments_without_touching_a_second_country(self):
        rt, actor = self.fixture()
        other = Country(2, flags=set())
        for slot, owner in ((1, actor), (2, other), (3, actor)):
            rt.temporary.update({PREFIX + "fragment_assigned": 0, PREFIX + "fragment_id": slot, PREFIX + "fragment_role": slot})
            rt.run(PREFIX + "ledger_assign_fragment", owner)
        self.run_policy(rt, actor)
        self.assertEqual(actor.values["chaosx_nr25_fragment_count"], 0)
        self.assertEqual(other.values["chaosx_nr25_fragment_count"], 1)
        self.assertIs(rt.targets[PREFIX + "fragment_owner_2"], other)
        for slot in (1, 3):
            rt.temporary.update({PREFIX + "fragment_assigned": 0, PREFIX + "fragment_id": slot, PREFIX + "fragment_role": slot})
            rt.run(PREFIX + "ledger_assign_fragment", other)
            self.assertEqual(rt.temporary[PREFIX + "fragment_assigned"], 0)
        self.assertEqual(rt.global_values["chaosx_nr25_fragment_status"], [0, 2, 0, 0, 0, 0])

    def test_uninitialized_helper_output_does_not_escape_its_call_frame(self):
        rt, actor = self.fixture()
        rt.temporary.pop("chaosx_nr25_destruction_applied")
        rt.run("chaosx_nr25_execute_destroy_material", actor)
        self.assertNotIn("chaosx_nr25_destruction_applied", rt.temporary)
        self.assertIn("chaosx_nr25_material_destroyed", actor.flags)

    def test_native_decision_and_dispatch_use_the_same_preflight(self):
        decisions = (ROOT / "common/decisions/025_alien_technology_in_antarctica_evolution_decisions.txt").read_text(encoding="utf-8-sig")
        decision = block("chaosx_nr25_dependence_destroy", decisions)
        self.assertIn(("custom_cost_text", "chaosx_nr25_dependence_destroy_cost"), decision)
        self.assertIn("chaosx_nr25_destroy_material_context_valid", repr(decision))
        self.assertIn("chaosx_nr25_dependence_destroy_cost_available", repr(decision))
        self.assertIn("chaosx_nr25_execute_evolution_action", repr(decision))
        self.assertIn("chaosx_nr25_destroy_material_available", repr(block("chaosx_nr25_execute_destroy_material", POLICY)))


if __name__ == "__main__":
    unittest.main()
