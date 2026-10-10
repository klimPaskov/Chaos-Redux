"""Execute the production seizure and restitution chain over six stored slots.

Country/event scopes, targeted receipts, meta expansion and conservative helper
temp cleanup are modeled. Native opinions, threats and event delivery are spies.
This is not native engine, expiry, UI or save/reload evidence.
"""
import re
import unittest

from test_event025_custody import CustodyRuntime, PREFIX
from test_event025_final_recovery import ROOT, Country, block


def read(path):
    return re.sub(r"#[^\n]*", "", (ROOT / path).read_text(encoding="utf-8-sig"))


MILITARY = read("common/scripted_effects/025_alien_technology_in_antarctica_militarisation_effects.txt")
INCIDENTS = read("common/scripted_effects/025_alien_technology_in_antarctica_incident_effects.txt")
RETURNS = read("common/scripted_effects/025_alien_technology_in_antarctica_seizure_return_effects.txt")
GATES = read("common/scripted_triggers/025_alien_technology_in_antarctica_seizure_return_triggers.txt")
EVOLUTIONS = read("common/scripted_triggers/025_alien_technology_in_antarctica_evolution_gate_triggers.txt")
RUNTIME = read("common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt")


class RestitutionRuntime(CustodyRuntime):
    def __init__(self, countries):
        super().__init__(countries)
        for text, names in (
            (MILITARY, ("chaosx_nr25_take_seized_material", "chaosx_nr25_change_militarisation", "chaosx_nr25_seed_militarisation")),
            (INCIDENTS, ("chaosx_nr25_demand_seizure_return", "chaosx_nr25_accept_seizure_return", "chaosx_nr25_apply_seizure_return", "chaosx_nr25_refuse_seizure_return", "chaosx_nr25_apply_seizure_refusal")),
            (RETURNS, ("chaosx_nr25_return_seized_fragments",)),
            (RUNTIME, ("chaosx_nr25_clamp_values",)),
        ):
            self.effects.update({name: block(name, text) for name in names})
        for path in ("common/script_constants/025_alien_technology_in_antarctica_militarisation_constants.txt",
                     "common/script_constants/025_alien_technology_in_antarctica_incident_constants.txt"):
            for category, body in re.findall(r"(chaosx_nr25_\w+)\s*=\s*\{(.*?)(?=\n\})", read(path), re.S):
                for name, value in re.findall(r"^\s*(\w+)\s*=\s*(-?\d+(?:\.\d+)?)\s*$", body, re.M):
                    self.constants["constant:" + category + "." + name] = float(value)
        self.triggers["chaosx_nr25_seizure_return_matches_demand"] = block("chaosx_nr25_seizure_return_matches_demand", GATES)
        self.triggers["chaosx_nr25_militarised_antarctica_evolution_in_force"] = block("chaosx_nr25_militarised_antarctica_evolution_in_force", EVOLUTIONS)
        self.global_flags.add("chaosx_nr25_evolution_militarised_antarctica")
        self.global_values["chaosx_nr25_militarisation"] = 50


class SeizureRestitutionTests(unittest.TestCase):
    def setUp(self):
        self.seizer, self.victim, self.other = (Country(n, flags=set()) for n in (1, 2, 3))
        self.rt = RestitutionRuntime([self.seizer, self.victim, self.other])
        self.victim.values.update({"chaosx_nr25_survey_evidence": 50, "chaosx_nr25_crew": 2})
        self.other.values.update({"chaosx_nr25_survey_evidence": 50, "chaosx_nr25_crew": 2})

    def acquire(self, owner, slot):
        self.rt.temporary.update({PREFIX + "fragment_assigned": 0, PREFIX + "fragment_id": slot, PREFIX + "fragment_role": slot})
        self.rt.run(PREFIX + "ledger_assign_fragment", owner)

    def seize(self, victim):
        self.rt.targets["chaosx_nr25_rival_target_scope"] = victim
        self.rt.run("chaosx_nr25_take_seized_material", self.seizer)

    def answer(self, victim, refusal=False):
        self.rt.from_country = victim
        self.rt.run("chaosx_nr25_refuse_seizure_return" if refusal else "chaosx_nr25_accept_seizure_return", self.seizer)

    def demand(self, victim):
        self.rt.from_country = self.seizer
        self.rt.run("chaosx_nr25_demand_seizure_return", victim)

    def test_production_demand_records_the_seizer_and_one_answer_window(self):
        self.demand(self.victim)
        self.assertEqual(self.victim.values["chaosx_nr25_seizure_demand_seizer"], self.seizer.id)
        flags = [item for item in self.rt.native_observations if item[1] == "set_country_flag"]
        self.assertEqual(flags, [(self.victim.id, "set_country_flag", "chaosx_nr25_seizure_demand_pending", self.rt.constants["constant:chaosx_nr25_militarisation.offer_days"])])
        self.assertEqual(self.rt.reports, [(self.seizer.id, "chaosx.nr25.173")])

    def test_two_seizures_from_one_victim_return_both_slots(self):
        self.acquire(self.victim, 1)
        self.acquire(self.victim, 3)
        self.acquire(self.seizer, 6)
        self.seize(self.victim)
        self.seize(self.victim)
        self.assertIn("chaosx_nr25_seized_fragment_1_by_1", self.victim.flags)
        self.assertIn("chaosx_nr25_seized_fragment_3_by_1", self.victim.flags)
        self.demand(self.victim)
        self.answer(self.victim)
        for slot in (1, 3):
            self.assertIs(self.rt.targets[PREFIX + f"fragment_owner_{slot}"], self.victim)
        self.assertIs(self.rt.targets[PREFIX + "fragment_owner_6"], self.seizer)
        self.assertEqual(self.victim.values["chaosx_nr25_returned_fragment_count_record"], 2)
        self.assertEqual(self.victim.values["chaosx_nr25_returned_evidence_record"], 20)
        self.assertEqual(self.victim.values["chaosx_nr25_crew"], 2)
        self.assertEqual(self.victim.values["chaosx_nr25_returned_crew_record"], 2)
        self.assertNotIn("chaosx_nr25_detained_crew_by_1", self.victim.values)

    def test_detention_is_bounded_by_actual_crew_and_release_conserves_it(self):
        for initial_crew in (0, 1, 2):
            with self.subTest(initial_crew=initial_crew):
                self.setUp()
                self.victim.values["chaosx_nr25_crew"] = initial_crew
                for _ in range(3): self.seize(self.victim)
                self.assertEqual(self.victim.values["chaosx_nr25_crew"], 0)
                self.assertEqual(self.victim.values["chaosx_nr25_detained_crew_by_1"], initial_crew)
                self.demand(self.victim)
                self.answer(self.victim)
                self.assertEqual(self.victim.values["chaosx_nr25_crew"], initial_crew)
                self.assertEqual(self.victim.values["chaosx_nr25_returned_crew_record"], initial_crew)

    def test_no_detention_receipt_cannot_create_released_crew(self):
        self.demand(self.victim)
        self.answer(self.victim)
        self.assertEqual(self.victim.values["chaosx_nr25_crew"], 2)
        self.assertEqual(self.victim.values["chaosx_nr25_returned_crew_record"], 0)

    def test_claims_from_another_victim_never_follow_this_answer(self):
        self.acquire(self.victim, 1)
        self.acquire(self.other, 2)
        self.seize(self.victim)
        self.seize(self.other)
        self.demand(self.victim)
        self.answer(self.victim)
        self.assertIs(self.rt.targets[PREFIX + "fragment_owner_1"], self.victim)
        self.assertIs(self.rt.targets[PREFIX + "fragment_owner_2"], self.seizer)
        self.assertEqual(self.other.values["chaosx_nr25_survey_evidence"], 40)
        self.assertIn("chaosx_nr25_seized_fragment_2_by_1", self.other.flags)

    def test_all_six_claims_return_with_their_original_roles(self):
        for slot in range(1, 7): self.acquire(self.victim, slot)
        for _ in range(6): self.seize(self.victim)
        self.demand(self.victim)
        self.answer(self.victim)
        self.assertEqual(self.victim.values["chaosx_nr25_returned_fragment_count_record"], 6)
        for slot in range(1, 7):
            self.assertIs(self.rt.targets[PREFIX + f"fragment_owner_{slot}"], self.victim)
            self.assertEqual(self.rt.global_values[PREFIX + f"fragment_{slot}_role"], slot)
            self.assertNotIn(f"chaosx_nr25_seized_fragment_{slot}_by_1", self.victim.flags)

    def test_partial_restitution_clears_only_the_successful_claim(self):
        self.acquire(self.victim, 1)
        self.acquire(self.victim, 2)
        self.seize(self.victim)
        self.seize(self.victim)
        self.rt.temporary[PREFIX + "fragment_role"] = 2
        self.rt.run(PREFIX + "ledger_assign_fragment_slot_2", self.other)
        self.demand(self.victim)
        self.answer(self.victim)
        self.assertEqual(self.victim.values["chaosx_nr25_returned_fragment_count_record"], 1)
        self.assertIs(self.rt.targets[PREFIX + "fragment_owner_1"], self.victim)
        self.assertIs(self.rt.targets[PREFIX + "fragment_owner_2"], self.other)
        self.assertNotIn("chaosx_nr25_seized_fragment_1_by_1", self.victim.flags)
        self.assertIn("chaosx_nr25_seized_fragment_2_by_1", self.victim.flags)

    def test_refusal_consumes_one_answer_without_releasing_custody(self):
        self.acquire(self.victim, 1)
        self.seize(self.victim)
        self.demand(self.victim)
        self.answer(self.victim, refusal=True)
        self.assertIs(self.rt.targets[PREFIX + "fragment_owner_1"], self.seizer)
        self.assertEqual(self.victim.values["chaosx_nr25_crew"], 1)
        self.assertEqual(self.victim.values["chaosx_nr25_detained_crew_by_1"], 1)
        self.assertNotIn("chaosx_nr25_seizure_demand_pending", self.victim.flags)
        pressure = self.rt.global_values["chaosx_nr25_militarisation"]
        observations = len(self.rt.native_observations)
        self.answer(self.victim, refusal=True)
        self.assertEqual(self.rt.global_values["chaosx_nr25_militarisation"], pressure)
        self.assertEqual(len(self.rt.native_observations), observations)

    def test_repeat_accept_or_refuse_has_no_further_outcome(self):
        self.acquire(self.victim, 1)
        self.seize(self.victim)
        self.demand(self.victim)
        self.answer(self.victim)
        snapshot = (self.victim.values.copy(), self.seizer.values.copy(), len(self.rt.native_observations), len(self.rt.reports), self.rt.global_values["chaosx_nr25_militarisation"])
        self.answer(self.victim)
        self.answer(self.victim, refusal=True)
        self.assertEqual(snapshot, (self.victim.values, self.seizer.values, len(self.rt.native_observations), len(self.rt.reports), self.rt.global_values["chaosx_nr25_militarisation"]))

    def test_expired_misdirected_or_invalid_demand_changes_nothing(self):
        for reason in ("expired", "other_seizer", "missing_identity", "subject", "annexed"):
            with self.subTest(reason=reason):
                self.setUp()
                self.acquire(self.victim, 1)
                self.seize(self.victim)
                self.demand(self.victim)
                if reason == "expired": self.victim.flags.discard("chaosx_nr25_seizure_demand_pending")
                if reason == "other_seizer": self.victim.values["chaosx_nr25_seizure_demand_seizer"] = 3
                if reason == "missing_identity": self.victim.values.pop("chaosx_nr25_seizure_demand_seizer")
                if reason == "subject": self.victim.subject = True
                if reason == "annexed": self.victim.exists = False
                before = (self.victim.values.copy(), self.victim.flags.copy(), self.seizer.values.copy(), self.rt.global_values["chaosx_nr25_militarisation"])
                self.answer(self.victim)
                self.assertEqual(before, (self.victim.values, self.victim.flags, self.seizer.values, self.rt.global_values["chaosx_nr25_militarisation"]))

    def test_third_holder_is_not_robbed_and_unfulfilled_claim_is_retained(self):
        self.acquire(self.victim, 1)
        self.seize(self.victim)
        self.rt.temporary[PREFIX + "fragment_role"] = 1
        self.rt.run(PREFIX + "ledger_assign_fragment_slot_1", self.other)
        self.demand(self.victim)
        self.answer(self.victim)
        self.assertIs(self.rt.targets[PREFIX + "fragment_owner_1"], self.other)
        self.assertIn("chaosx_nr25_seized_fragment_1_by_1", self.victim.flags)
        self.assertEqual(self.victim.values["chaosx_nr25_returned_fragment_count_record"], 0)
        self.assertNotIn("chaosx_nr25_seizure_fragment_returned", self.victim.flags)

    def test_legacy_single_slot_is_preserved_but_fractional_slot_is_not_rounded(self):
        for receipt in (1, 1.5, 0, 7):
            with self.subTest(receipt=receipt):
                self.setUp()
                self.acquire(self.seizer, 1)
                self.victim.values["chaosx_nr25_seized_slot_by_1"] = receipt
                self.demand(self.victim)
                self.answer(self.victim)
                self.assertIs(self.rt.targets[PREFIX + "fragment_owner_1"], self.victim if receipt == 1 else self.seizer)
                self.assertNotIn("chaosx_nr25_seized_slot_by_1", self.victim.values)


if __name__ == "__main__":
    unittest.main()
