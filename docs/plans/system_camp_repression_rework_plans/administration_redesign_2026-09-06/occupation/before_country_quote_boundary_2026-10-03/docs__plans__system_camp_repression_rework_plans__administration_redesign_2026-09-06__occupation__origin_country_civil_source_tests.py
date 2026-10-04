"""Country/civil caller production source with explicit engine primitives.
No game launch, archival inference or simulated AI click probability.
"""
from pathlib import Path
import sys
import json
import copy
import datetime

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from major_countries_source_tests import CountryRuntime, new_country
from foundation_source_tests import ROOT, parse, prime_existing_custody


class CallerRuntime(CountryRuntime):
    def __init__(self):
        super().__init__()
        self.release_fault = None
        self.release_calls = 0
        self.root_country = "GER"
        self.triggers.update({key: body for key, _, body in parse((ROOT / "common/scripted_triggers/camp_administration_civil_triggers.txt").read_text())})
        self.effects.update({key: body for key, _, body in parse((ROOT / "common/scripted_effects/camp_administration_civil_effects.txt").read_text())})
        # Dispatch registration and visual refresh are external consumers.
        self.effects["camp_rework_register_country_for_monthly_pulse"] = []
        self.effects["camp_administration_civil_cancel_routine_projects"] = []
        self.effects["camp_administration_civil_refresh_ideas"] = []
        self.effects["camp_rework_usa_cancel_security_sunset"] = []

    def target(self, value, scope, prev):
        return self.root_country if value == "ROOT" else super().target(value, scope, prev)

    def val(self, value, scope, prev=None):
        return self.root_country if value == "ROOT" else super().val(value, scope, prev)

    def run(self, name, scope, params=None, prev=None):
        if name == "camp_admin_release_detainees":
            self.release_calls += 1
            if self.release_fault == "reject":
                self.temp["camp_admin_release_actual_k"] = 0
                self.temp["camp_admin_release_requested_k"] = 0
                return
        result = super().run(name, scope, params, prev)
        if name == "camp_admin_release_detainees" and self.temp.get("camp_admin_release_actual_k", 0) > 0:
            if self.release_fault == "category":
                self.scopes[self.root_country]["held_bonuses"] = {"engineers_tech"}
            if self.release_fault == "cap":
                self.scopes[self.root_country]["camp_admin_research_awards_this_year"] = 2
            if self.release_fault == "capture":
                self.scopes[scope]["controller"] = "POL"
        return result


def setup(tag="GER", programme="ger_inspectorate", held=20):
    r = CallerRuntime()
    r.root_country = tag
    r.date = datetime.date(1944, 2, 1) if tag == "SOV" else datetime.date(1943, 6, 1)
    c = r.country(tag)
    c.update(original_tag=tag, government="communism" if tag == "SOV" else "fascism",
             camp_admin_budget=2, camp_admin_mandate=2, camp_admin_country_program=0,
             camp_admin_country_authority_pressure=0, camp_admin_budget_support_remaining=100,
             camp_admin_budget_pp_remaining=20)
    c["flags"].add("camp_admin_country_programs_authorized")
    if tag == "SOV":
        c["flags"].add("camp_admin_country_oversight_authorized")
    a = r.state("A", tag, population=1000, buildings=4)
    if tag == "SOV":
        a["gulag_labor_camp_network"] = 2
    prime_existing_custody(r, "A", held)
    a["camp_admin_support_ratio"] = 1
    r.run("camp_origin_observe_host", "A")
    return r, c, a


def mixed_loss(r, c, site):
    r.state("B", r.root_country, population=1000, buildings=4)
    site["arrays"]["camp_admin_row_amounts_k"][0] -= 10
    r.temp.update(camp_admin_append_origin="B", camp_admin_append_authority=r.root_country,
                  camp_admin_append_root_id=0, camp_admin_append_amount_k=10)
    r.run("camp_admin_append_row", "A")
    r.run("camp_origin_observe_host", "A")
    site["state_population_k"] -= 1
    site["chaos_state_civilian_deaths_total"] = 1000
    r.run("camp_admin_refresh_capacity", "A")
    assert "camp_origin_ambiguous" in site["flags"]


def complete(r, c, programme):
    r.start_program(r.root_country, programme)
    assert "camp_admin_institution_slot_active" in c["flags"]
    c["camp_admin_institution_progress"] = c["camp_admin_institution_target"]


def unrelated_occupation_uncertainty(r, c):
    owner = r.root_country
    held = r.state("O", owner, population=1000, buildings=2)
    r.state("X", owner, population=1000, buildings=2)
    c["arrays"]["camp_active_site_states"] = ["A"]
    c["flags"].update({"camp_occ_initialized", "camp_occ_rows_initialized"})
    c["arrays"]["camp_occ_states"] = ["O"]
    fields = {"ids": [1, 2], "root_ids": [1, 2], "origins": ["O", "X"],
              "hosts": ["O", "O"], "authorities": [owner, owner], "profiles": [2, 2],
              "amounts_k": [10, 10], "statuses": [1, 1]}
    for name in ("deaths_k", "removed_k", "released_k", "moved_out_k", "moved_in_k"):
        fields[name] = [0, 0]
    for key, value in fields.items():
        c["arrays"]["camp_occ_row_" + key] = value
    c.update(camp_occ_row_count=2, camp_occ_next_row_id=3)
    held["flags"].add("camp_occ_registered")
    held.update(camp_occ_responsible_country=owner, camp_occ_remaining_k=20)
    r.run("camp_origin_observe_host", "O")
    held.update(state_population_k=999, chaos_state_civilian_deaths_total=1000)
    r.run("camp_occ_reconcile_external_population", "O")
    assert "camp_origin_ambiguous" in held["flags"]
    return held


def tests():
    cases = []
    r, c, a = setup()
    mixed_loss(r, c, a)
    r.scopes["B"]["flags"].add("camp_admin_closed")
    before = (c["support"], c["political_power"], r.debits, r.logged)
    r.start_program("GER", "ger_inspectorate")
    assert "camp_admin_institution_slot_active" not in c["flags"]
    assert before == (c["support"], c["political_power"], r.debits, r.logged) and not r.awards
    cases.append("selected mixed provenance blocks programme target start without cost or reward")

    for issue in ("mixed", "authority", "support"):
        r, c, a = setup()
        complete(r, c, "ger_inspectorate")
        if issue == "mixed":
            mixed_loss(r, c, a)
        elif issue == "authority":
            a["controller"] = "POL"
        else:
            a["camp_admin_support_ratio"] = 0.74
        before = (c["support"], c["political_power"], c["camp_admin_research_awards_this_year"])
        r.run("camp_admin_country_award_program_ger_inspectorate", "GER")
        r.run("camp_admin_country_tick_institution", "GER")
        assert not r.awards and "camp_admin_done_ger_inspectorate" not in c["flags"]
        assert before == (c["support"], c["political_power"], c["camp_admin_research_awards_this_year"])
        r.run("camp_admin_country_halt", "GER")
        assert "camp_admin_country_programs_authorized" not in c["flags"] and "camp_admin_institution_slot_active" not in c["flags"]
        cases.append(f"fresh {issue} blocks selected-site tick/final grant while independent halt remains usable")

    r, c, a = setup()
    r.start_program("GER", "ger_inspectorate")
    r.run("camp_admin_country_award_program_ger_inspectorate", "GER")
    assert not r.awards
    c["camp_admin_institution_progress"] = 6
    r.run("camp_admin_country_award_program_ger_wvha", "GER")
    assert not r.awards
    r.run("camp_admin_country_award_program_ger_inspectorate", "GER")
    assert len(r.awards) == 1 and 0.5 <= r.awards[0]["bonus"] <= 1 and r.awards[0]["uses"] == 1
    r.run("camp_admin_country_award_program_ger_inspectorate", "GER")
    assert len(r.awards) == 1 and c["camp_admin_research_awards_this_year"] == 1
    cases.append("incomplete/wrong direct award grants nothing and matching complete programme grants one bounded single-use award")

    r, c, a = setup("SOV", held=0.5)
    complete(r, c, "sov_engineer_release")
    population = a["state_population_k"]
    r.run("camp_admin_country_award_program_sov_engineer_release", "SOV")
    assert r.release_calls == 1 and a["camp_admin_detainees_k"] == 0
    assert c["camp_admin_country_last_engineers_released_k"] == 0.5
    assert len(r.awards) == 1 and "camp_admin_done_sov_engineer_release" in c["flags"]
    assert a["state_population_k"] == population and r.debits == 0 and r.logged == 0
    r.run("camp_admin_country_award_program_sov_engineer_release", "SOV")
    assert r.release_calls == 1 and len(r.awards) == 1
    cases.append("all held engineers can release first and their measured positive receipt supports one award at the now-zero-held site")

    r, c, a = setup("SOV")
    complete(r, c, "sov_engineer_release")
    r.release_fault = "reject"
    r.run("camp_admin_country_award_program_sov_engineer_release", "SOV")
    assert not r.awards and c["camp_admin_research_awards_this_year"] == 0
    assert "camp_admin_done_sov_engineer_release" not in c["flags"] and "camp_admin_country_engineers_released" not in c["flags"]
    assert a["camp_admin_detainees_k"] == 20
    cases.append("execution-time zero release withholds engineer award, annual count and completion flags")

    for deferred in ("category", "cap", "capture"):
        r, c, a = setup("SOV")
        complete(r, c, "sov_engineer_release")
        r.release_fault = deferred
        before = (c["support"], c["political_power"], a["state_population_k"])
        r.run("camp_admin_country_award_program_sov_engineer_release", "SOV")
        assert not r.awards and r.release_calls == 1 and a["camp_admin_detainees_k"] == 19.5
        assert "camp_admin_country_engineer_release_pending" in c["flags"]
        r.run("camp_admin_country_tick_institution", "SOV")
        assert not r.awards and r.release_calls == 1 and before == (c["support"], c["political_power"], a["state_population_k"])
        r.release_fault = None
        c["held_bonuses"] = set()
        a["controller"] = "SOV"
        if deferred == "cap":
            r.date = datetime.date(1945, 2, 1)
        r.run("camp_admin_country_tick_institution", "SOV")
        assert len(r.awards) == 1 and r.release_calls == 1
        assert before == (c["support"], c["political_power"], a["state_population_k"])
        assert c["camp_admin_research_awards_this_year"] == 1
        cases.append(f"measured engineer receipt deferred by {deferred} retains identity and later grants without repeated release/payment")

    r, c, a = setup("SOV")
    complete(r, c, "sov_engineer_release")
    r.release_fault = "category"
    r.run("camp_admin_country_award_program_sov_engineer_release", "SOV")
    before = (c["support"], c["political_power"], a["camp_admin_total_released_k"], a["state_population_k"])
    r.run("camp_admin_country_halt", "SOV")
    assert "camp_admin_country_engineer_release_pending" in c["flags"]
    r.run("camp_admin_country_start_oversight", "SOV")
    assert "camp_admin_country_engineer_release_pending" not in c["flags"]
    assert not any(k.startswith("camp_admin_country_engineer_receipt_") for k in c)
    assert c["camp_admin_country_program"] == 0 and "camp_admin_institution_state_id" not in c
    assert "camp_admin_country_oversight_active" in c["flags"] and not r.awards and r.release_calls == 1
    assert before == (c["support"], c["political_power"], a["camp_admin_total_released_k"], a["state_population_k"])
    cases.append("ordinary halt preserves a completed pending receipt; intentional oversight abandonment clears it without release, payment or bonus")

    r, c, a = setup("SOV")
    complete(r, c, "sov_engineer_release")
    r.release_fault = "category"
    r.run("camp_admin_country_award_program_sov_engineer_release", "SOV")
    other = r.state("C", "SOV", population=1000, buildings=2)
    other["gulag_labor_camp_network"] = 1
    prime_existing_custody(r, "C", 20)
    other["camp_admin_support_ratio"] = 1
    c["camp_admin_institution_state_id"] = "C"
    c["held_bonuses"] = set()
    r.run("camp_admin_country_award_program_sov_engineer_release", "SOV")
    assert not r.awards and r.release_calls == 1
    assert other["camp_admin_detainees_k"] == 20
    cases.append("a pending completed engineer receipt cannot substitute another healthy host")

    r, c, a = setup()
    unrelated_occupation_uncertainty(r, c)
    r.start_program("GER", "ger_inspectorate")
    assert c["camp_admin_institution_state_id"] == "A"
    for _ in range(6):
        c.update(camp_admin_budget_support_remaining=100, camp_admin_budget_pp_remaining=20)
        r.run("camp_admin_country_tick_institution", "GER")
    assert len(r.awards) == 1 and c["support"] == 10000 - 72 and c["political_power"] == 70
    assert not r.cond(r.triggers["camp_admin_country_sites_ready_for_reform"], "GER")
    before = (c["support"], c["political_power"], a["camp_admin_detainees_k"])
    r.run("camp_admin_country_reform", "GER")
    assert "camp_admin_country_reformed" not in c["flags"]
    assert before == (c["support"], c["political_power"], a["camp_admin_detainees_k"])
    cases.append("unrelated occupation-only ambiguity blocks national reform while a proven selected-site programme continues for six exact funded months")

    r, c, a = setup()
    complete(r, c, "ger_inspectorate")
    c["camp_admin_total_deaths_k"] = 1000
    c["camp_admin_institution_progress"] = 0
    r.run("camp_admin_country_finish_program", "GER")
    assert not r.awards
    cases.append("large corpse totals do not substitute for funded programme completion")

    r = CallerRuntime()
    r.root_country = "ENG"
    r.date = datetime.date(1943, 1, 1)
    c = r.country("ENG")
    c.update(government="democratic", war=True, camp_admin_budget=2,
             camp_admin_budget_support_remaining=100, camp_admin_budget_pp_remaining=20)
    a = r.state("A", "ENG", population=1000, buildings=4)
    prime_existing_custody(r, "A", 20)
    r.run("camp_administration_civil_initialize", "ENG")
    c["flags"].add("camp_admin_civil_policy_authorized")
    unrelated_occupation_uncertainty(r, c)
    before = (c["support"], c["political_power"], a["camp_admin_detainees_k"])
    r.run("camp_administration_civil_action_two", "ENG")
    assert "camp_admin_civil_review_active" not in c["flags"] and "camp_admin_reforming" not in c["flags"]
    assert before == (c["support"], c["political_power"], a["camp_admin_detainees_k"])
    # A previously started production review also carries its reform/frozen
    # policy state, preventing an unrelated custody-intake policy installment.
    c["flags"].update({"camp_admin_civil_review_active", "camp_admin_reforming", "camp_rework_expansion_frozen"})
    c["camp_admin_civil_review_progress"] = 0
    r.run("camp_administration_civil_monthly", "ENG")
    assert c["camp_admin_civil_review_progress"] == 0 and before == (c["support"], c["political_power"], a["camp_admin_detainees_k"])
    c["camp_admin_civil_review_progress"] = r.constants["camp_admin_civil.review_months"]
    r.run("camp_administration_civil_finish_review", "ENG")
    assert "camp_admin_civil_review_complete" not in c["flags"] and "camp_rework_reformed_legacy" not in c["flags"]
    cases.append("civil reform/paid review/final settlement reject an unrelated occupation-only uncertain host before payment or flags")

    r = CallerRuntime()
    r.root_country = "ENG"
    r.date = datetime.date(1943, 1, 1)
    c = r.country("ENG")
    c.update(government="democratic", war=True, camp_admin_budget=2,
             camp_admin_budget_support_remaining=100, camp_admin_budget_pp_remaining=20)
    a = r.state("A", "ENG", population=1000, buildings=4)
    prime_existing_custody(r, "A", 20)
    r.run("camp_administration_civil_initialize", "ENG")
    c["flags"].add("camp_admin_civil_policy_authorized")
    r.run("camp_administration_civil_action_two", "ENG")
    assert "camp_admin_civil_review_active" in c["flags"] and a["camp_admin_total_released_k"] == 20
    r.run("camp_administration_civil_finish_review", "ENG")
    assert "camp_admin_civil_review_complete" not in c["flags"]
    for month in range(1, 4):
        r.date = datetime.date(1943, month, 1)
        c.update(camp_admin_budget_support_remaining=100, camp_admin_budget_pp_remaining=20)
        r.run("camp_administration_civil_monthly", "ENG")
    assert "camp_admin_civil_review_complete" in c["flags"] and c["support"] == 10000 - 45 and c["political_power"] == 76
    before = (c["support"], c["political_power"], a["camp_admin_total_released_k"])
    r.run("camp_administration_civil_finish_review", "ENG")
    assert before == (c["support"], c["political_power"], a["camp_admin_total_released_k"])
    cases.append("healthy civil reform releases once, completes three exact funded review months and rejects premature/repeated settlement")
    return cases


if __name__ == "__main__":
    cases = tests()
    payload = {"status": "passed", "count": len(cases), "scenarios": cases,
               "limitations": "Parsed production bodies. Explicit native primitives and post-release fault injection, not runtime or archival proof."}
    (HERE / "origin_country_civil_source_results.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
