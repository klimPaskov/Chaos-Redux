"""Joined owned production helpers with declared actor eligibility and engine mocks.
No HOI4 launch or runtime proof. Calls real registration, death, movement,
retirement, release and close helpers rather than replacing their results.
"""
from pathlib import Path
import copy
import json
import datetime
from origin_observer_helper_source_tests import OriginRuntime, ROOT, foundation, fixture, occupation, custody


class JoinedRuntime(OriginRuntime):
    def __init__(self):
        super().__init__()
        self.credits = 0
        self.credit_fraction = 1
        self.fail_inverse = False
        self.fail_source_commit = False
        self.date = datetime.date(1944, 8, 20)
        # Country campaign eligibility is an explicitly declared external actor
        # assumption. All owned route, row, scope, physical and bind gates run.
        self.triggers["camp_occ_authority_has_campaign"] = [("has_country_flag", "=", "origin_test_campaign_eligible")]
        # The same declared assumption opens the campaign: the production monthly pass
        # then records camp_occ_campaign_opened on its first run, and the day-count
        # gates (campaign age, held age, partner windows) run against that real date.
        self.triggers["camp_occ_campaign_can_open"] = [("has_country_flag", "=", "origin_test_campaign_eligible")]
        self.triggers["camp_admin_country_regime_valid"] = []
        self.effects["camp_rework_register_country_for_monthly_pulse"] = []
        self.effects["origin_test_add_manpower"] = []
        self.after_bind = False

    def run(self, name, scope, params=None, prev=None):
        if name == "origin_test_add_manpower":
            amount = self.val(params["amount"], scope, prev)
            if "state_population_k" in self.scopes[scope]:
                self.scopes[scope]["state_population_k"] += amount / 1000
                self.credits += amount > 0
            return
        if name == "camp_occ_apply_population_credit" and scope == 88 and self.credit_fraction != 1:
            self.temp["camp_occ_credit_request_people"] *= self.credit_fraction
        if name == "camp_admin_inverse_import_bind" and self.fail_inverse:
            self.temp["camp_admin_import_inverse_accepted_people"] = 0
            return
        result = super().run(name, scope, params, prev)
        if name == "camp_admin_bind_import" and self.fail_source_commit and not self.after_bind:
            self.after_bind = True
            # Mock a changed physical route authority after destination bind.
            self.scopes[87]["controller"] = "POL"
        return result

    def execute(self, block, scope, prev=None):
        def credit_primitive(entries):
            return [("origin_test_add_manpower", op, [("amount", "=", value)]) if key == "add_manpower"
                    else (key, op, credit_primitive(value) if isinstance(value, list) else value)
                    for key, op, value in entries]
        return super().execute(credit_primitive(block), scope, prev)


def routed_fixture():
    r = JoinedRuntime()
    country = r.country("GER")
    country["flags"].add("origin_test_campaign_eligible")
    r.country("POL")
    source = r.state(87, "GER", population=100, buildings=2)
    destination = r.state(88, "GER", population=100, buildings=2)
    source["flags"].add("camp_occ_origin_assigned")
    r.temp.update(camp_occ_source_proven=1, camp_occ_source_requested_k=10,
                  camp_occ_source_membership_k=10, camp_occ_source_authority="GER",
                  camp_occ_source_profile=r.constants["camp_occ_profile.germany"])
    r.run("camp_occ_register_cohort", 87)
    assert source["camp_occ_remaining_k"] == 10 and "camp_origin_ambiguous" not in source["flags"]
    destination.update(extermination_camp=1, camp_admin_role=r.constants["camp_admin_role.killing"])
    return r, country, source, destination


def transfer(r, custody_route=True, people=5000, source_state=87, destination_state=88, row_id=1):
    if custody_route:
        r.run("camp_occ_stage_custody_destination", destination_state)
        r.temp.update(camp_occ_custody_route_proven=1, camp_occ_custody_row_id=row_id, camp_occ_custody_requested_people=people)
        r.run("camp_occ_transfer_to_custody_exact", source_state)
        return r.temp["camp_occ_custody_result"]
    r.run("camp_occ_stage_transfer_destination", destination_state)
    r.temp.update(camp_occ_transfer_route_proven=1, camp_occ_transfer_row_id=row_id, camp_occ_transfer_requested_people=people)
    r.run("camp_occ_transfer_survivors_exact", source_state)
    return r.temp["camp_occ_transfer_result"]


def tests():
    results = []
    for family in (occupation, custody):
        r = fixture(population=200)
        family(r, [10, 10])
        r.run("camp_origin_observe_host", 88)
        host = r.scopes[88]
        rows = copy.deepcopy(r.scopes["GER"]["arrays"] if family is occupation else host["arrays"])
        host.update(state_population_k=190, chaos_state_civilian_deaths_total=10000)
        r.run("camp_occ_reconcile_external_population" if family is occupation else "camp_admin_refresh_capacity", 88)
        assert "camp_origin_ambiguous" in host["flags"]
        assert rows == (r.scopes["GER"]["arrays"] if family is occupation else host["arrays"])
        assert host["camp_occ_remaining_k" if family is occupation else "camp_admin_detainees_k"] == 20
        assert host.get("camp_admin_external_attrition_k", 0) == 0
        assert host.get("camp_occ_total_exposure_removed_k", 0) == 0
        assert r.debits == 0 and r.logged == 0
        results.append(f"{family.__name__} outside owner wrapper freezes mixed A/B rows and aggregate without cause or physical receipt")

    for family in (occupation, custody):
        r = fixture()
        family(r, [20], origins=[101], roots=[1])
        r.run("camp_origin_observe_host", 88)
        host = r.scopes[88]
        host.update(state_population_k=90, chaos_state_civilian_deaths_total=10000)
        wrapper = "camp_occ_reconcile_external_population" if family is occupation else "camp_admin_refresh_capacity"
        r.run(wrapper, 88)
        assert host["camp_occ_remaining_k" if family is occupation else "camp_admin_detainees_k"] == 10
        assert "camp_origin_ambiguous" not in host["flags"]
        assert "camp_origin_single_origin_reconciliation_pending" not in host["flags"]
        before = copy.deepcopy(r.scopes)
        r.run(wrapper, 88)
        assert before == r.scopes
        assert r.debits == 0 and r.logged == 0
        results.append(f"{family.__name__} real unique-row retirement commits one exact outside receipt and repeat is inert")

    r = fixture()
    custody(r, [10, 10])
    r.run("camp_origin_observe_host", 88)
    host = r.scopes[88]
    host.update(state_population_k=105, chaos_state_civilian_deaths_total=10000)
    r.run("camp_admin_refresh_capacity", 88)
    assert "camp_origin_ambiguous" in host["flags"] and host["camp_admin_detainees_k"] == 20
    results.append("custody owner detects growth-masked shared loss below physical capacity shortfall")

    r, country, source, destination = routed_fixture()
    assert transfer(r) == 1
    assert source["state_population_k"] == 95 and destination["state_population_k"] == 105
    assert source["camp_occ_remaining_k"] == 5 and destination["camp_admin_detainees_k"] == 5
    assert destination["arrays"]["camp_admin_row_origins"] == [87]
    assert destination["arrays"]["camp_admin_row_occupation_roots"] == [1]
    assert r.debits == 1 and r.credits == 1 and r.logged == 0
    r.temp.update(camp_admin_death_requested_k=1, camp_admin_death_contract=1,
                  camp_admin_death_cause=r.constants["camp_admin_cause.violence"], camp_admin_death_row_id=1)
    r.run("camp_admin_record_deaths", 88)
    assert destination["state_population_k"] == 104 and destination["camp_admin_detainees_k"] == 4
    assert destination["chaos_state_civilian_deaths_total"] == 1000
    assert source.get("chaos_state_civilian_deaths_total", 0) == 0
    assert r.debits == 2 and r.credits == 1 and r.logged == 1
    r.run("camp_occ_reconcile_external_population", 87)
    r.run("camp_admin_refresh_capacity", 88)
    assert "camp_origin_ambiguous" not in source["flags"] | destination["flags"]
    assert destination["camp_admin_external_attrition_k"] == 0
    assert country["camp_admin_total_violence_deaths_k"] == 1 and country["camp_occ_total_deaths_k"] == 0
    results.append("real occupation-to-custody transfer then selected destination death preserves original/root/authority and one death projection")

    r, country, source, destination = routed_fixture()
    assert transfer(r) == 1
    before_population = destination["state_population_k"]
    r.temp["camp_admin_release_requested_k"] = 3
    r.run("camp_admin_release_detainees", 88)
    assert destination["camp_admin_detainees_k"] == 2 and destination["camp_admin_total_released_k"] == 3
    assert destination["arrays"]["camp_admin_row_released_k"] == [3]
    assert destination["state_population_k"] == before_population and r.logged == 0
    results.append("bound incoming custody releases only three proved survivors in place without population creation or death entry")

    for custody_host in (False, True):
        r, country, source, destination = routed_fixture()
        if custody_host:
            assert transfer(r) == 1
        second = r.state(101, "GER", population=200, buildings=2)
        second["flags"].add("camp_occ_origin_assigned")
        r.temp.update(camp_occ_source_proven=1, camp_occ_source_requested_k=10,
                      camp_occ_source_membership_k=10, camp_occ_source_authority="GER",
                      camp_occ_source_profile=r.constants["camp_occ_profile.germany"])
        r.run("camp_occ_register_cohort", 101)
        assert transfer(r, custody_route=custody_host, people=10000, source_state=101,
                        destination_state=88 if custody_host else 87, row_id=2) == 1
        host = destination if custody_host else source
        host["state_population_k"] -= 1
        host["chaos_state_civilian_deaths_total"] = 1000
        actual_before = (r.debits, r.credits, r.logged)
        if custody_host:
            r.temp.update(camp_admin_death_requested_k=1, camp_admin_death_contract=1,
                          camp_admin_death_cause=1, camp_admin_death_row_id=1)
            r.run("camp_admin_record_deaths", 88)
            assert r.temp["camp_admin_death_actual_k"] == 0
            r.temp["camp_admin_release_requested_k"] = 5
            r.run("camp_admin_release_detainees", 88)
            assert r.temp["camp_admin_release_actual_k"] == 0
            r.temp.update(camp_admin_admission_proven=1, camp_admin_admission_source_k=2, camp_admin_admission_requested_k=2)
            r.run("camp_admin_admit_detainees", 88)
            assert r.temp["camp_admin_admission_accepted_k"] == 0
            assert host["camp_admin_total_released_k"] == 0 and "camp_admin_census_intake_closed" not in host["flags"]
        else:
            r.temp.update(camp_occ_active_row_id=1, camp_occ_active_row_index=0,
                          camp_occ_requested_k=1, camp_occ_loss_contract=1,
                          camp_occ_loss_cause=r.constants["camp_occ_cause.campaign_violence"])
            r.run("camp_occ_record_deaths", 87)
            assert r.temp["camp_occ_actual_k"] == 0
            assert transfer(r, custody_route=False) == 0
        assert "camp_origin_ambiguous" in host["flags"]
        assert actual_before == (r.debits, r.credits, r.logged)
        assert country["camp_admin_total_deaths_k"] == 0 and country["camp_occ_total_deaths_k"] == 0
        results.append(f"{'custody' if custody_host else 'occupation'} actual mixed-host execution rejects deaths and origin actions while retaining original cause records")

    r, country, source, destination = routed_fixture()
    assert transfer(r, custody_route=False) == 1
    assert source["camp_occ_remaining_k"] == 5 and destination["camp_occ_remaining_k"] == 5
    assert country["arrays"]["camp_occ_row_origins"] == [87, 87]
    assert r.debits == 1 and r.credits == 1 and r.logged == 0
    assert "camp_origin_ambiguous" not in source["flags"] | destination["flags"]
    results.append("generic occupation movement commits both original-lineage endpoints before common baseline adjustment")

    r, country, source, destination = routed_fixture()
    r.credit_fraction = 0.5
    assert transfer(r) == 0
    assert source["state_population_k"] == 100 and destination["state_population_k"] == 100
    assert source["camp_occ_remaining_k"] == 10 and destination["camp_admin_detainees_k"] == 0
    assert r.temp["camp_occ_custody_rollback_complete"] == 1
    assert source["camp_origin_observed_population_k"] == 100 and destination["camp_origin_observed_population_k"] == 100
    assert "camp_origin_ambiguous" not in source["flags"] | destination["flags"]
    assert r.logged == 0
    results.append("partial destination credit follows complete measured physical inverse without a false outside observation")

    r, country, source, destination = routed_fixture()
    r.fail_source_commit = True
    r.fail_inverse = True
    assert transfer(r) == 0
    assert source["state_population_k"] == 95 and destination["state_population_k"] == 105
    assert source["camp_occ_remaining_k"] == 10 and destination["camp_admin_detainees_k"] == 5
    assert "camp_origin_ambiguous" in source["flags"] and "camp_origin_ambiguous" in destination["flags"]
    assert source["camp_origin_observed_population_k"] == 100 and destination["camp_origin_observed_population_k"] == 100
    assert source["camp_origin_transaction_observed_population_k"] == 95
    assert destination["camp_origin_transaction_observed_population_k"] == 105
    assert source["camp_occ_custody_failed_source_debit_people"] == 5000
    assert destination["camp_occ_custody_failed_bind_people"] == 5000
    assert r.debits == 1 and r.credits == 1 and r.logged == 0
    r.run("camp_occ_reconcile_external_population", 87)
    r.run("camp_admin_refresh_capacity", 88)
    assert source["camp_origin_total_observed_net_decline_k"] == 0
    destination.update(state_population_k=104, chaos_state_civilian_deaths_total=1000)
    r.run("camp_admin_refresh_capacity", 88)
    assert destination["camp_origin_unresolved_shared_loss_k"] == 1
    assert country["camp_admin_total_deaths_k"] == 0 and country["camp_occ_total_deaths_k"] == 0
    results.append("failed bind inverse preserves both endpoint canonical openings and partial receipts, with subsequent external loss separately observed")

    r = fixture()
    custody(r, [10, 10])
    host = r.scopes[88]
    r.run("camp_origin_observe_host", 88)
    host["arrays"]["camp_admin_row_amounts_k"][0] = 9
    r.run("camp_admin_refresh_capacity", 88)
    assert "camp_origin_records_unresolved" in host["flags"] and "camp_origin_ambiguous" not in host["flags"]
    host["arrays"]["camp_admin_row_amounts_k"][0] = 10
    r.run("camp_admin_refresh_capacity", 88)
    assert "camp_origin_records_unresolved" not in host["flags"]
    host["arrays"]["camp_admin_row_amounts_k"][0] = 9
    host.update(state_population_k=90, chaos_state_civilian_deaths_total=10000)
    r.run("camp_admin_refresh_capacity", 88)
    first_epoch = host["camp_origin_ambiguity_sequence"]
    host["arrays"]["camp_admin_row_amounts_k"][0] = 10
    r.run("camp_admin_refresh_capacity", 88)
    assert "camp_origin_ambiguous" in host["flags"] and host["camp_origin_ambiguity_sequence"] == first_epoch
    results.append("structural repair without loss can resume, while structural repair after outside loss cannot clear sticky provenance ambiguity")

    r, country, source, destination = routed_fixture()
    second = r.state(101, "GER", population=200, buildings=2)
    second["flags"].add("camp_occ_origin_assigned")
    r.temp.update(camp_occ_source_proven=1, camp_occ_source_requested_k=10,
                  camp_occ_source_membership_k=10, camp_occ_source_authority="GER",
                  camp_occ_source_profile=r.constants["camp_occ_profile.germany"])
    r.run("camp_occ_register_cohort", 101)
    assert transfer(r, custody_route=False, people=10000, source_state=101, destination_state=87, row_id=2) == 1
    country["arrays"]["camp_active_site_states"] = [88]
    second.update(state_population_k=180, chaos_state_civilian_deaths_total=10000)
    # Source 101 is an exact empty registry entry after the committed transfer.
    # Later territorial losses cannot produce any survivor release there.
    assert r.cond(r.triggers["camp_admin_country_sites_ready_for_reform"], "GER")
    source.update(state_population_k=109, chaos_state_civilian_deaths_total=1000)
    assert not r.cond(r.triggers["camp_admin_country_sites_ready_for_reform"], "GER")
    r.run("camp_occ_reconcile_external_population", 87)
    assert "camp_origin_ambiguous" in source["flags"]
    # Agent decision 2026-10-04: sticky provenance no longer strands reform.
    # Origin orders stay paused, and reform closes the host with incomplete records.
    assert not r.cond(r.triggers["camp_origin_host_provenance_ready"], 87)
    assert r.cond(r.triggers["camp_admin_country_sites_ready_for_reform"], "GER")
    occ_rows = copy.deepcopy(country["arrays"])
    before = (source["state_population_k"], source["camp_occ_remaining_k"], source.get("camp_occ_total_released_k", 0), r.debits, r.credits, r.logged)
    r.run("camp_occ_close_state", 87)
    assert {"camp_occ_closed", "camp_origin_ambiguity_terminal"} <= source["flags"]
    assert before == (source["state_population_k"], source["camp_occ_remaining_k"], source.get("camp_occ_total_released_k", 0), r.debits, r.credits, r.logged)
    assert country["arrays"] == occ_rows
    results.append("national reform union includes an occupation-only mixed host, permits valid empty terminal history despite later unrelated territorial loss, and closes a sticky-ambiguous host with incomplete records and no release, debit or death")

    r, country, source, destination = routed_fixture()
    country["arrays"]["camp_active_site_states"] = [88]
    source["camp_occ_remaining_k"] = 0
    source["flags"].discard("camp_occ_registered")
    assert not r.cond(r.triggers["camp_admin_country_sites_ready_for_reform"], "GER")
    source.pop("camp_occ_responsible_country")
    assert not r.cond(r.triggers["camp_admin_country_sites_ready_for_reform"], "GER")
    assert "camp_occ_responsible_country" not in source
    assert r.temp["camp_origin_inspect_occupation_owner_override"] == 0
    results.append("national reform checks the actual owner registry when a host loses its registered flag, zeroes its aggregate or drops its authority pointer")

    r, country, source, destination = routed_fixture()
    assert transfer(r) == 1
    destination["arrays"]["camp_admin_row_origins"].append(87)
    destination["controller"] = "POL"
    r.run("camp_admin_close_site", 88)
    assert {"camp_admin_closed", "camp_origin_ambiguity_terminal"} <= destination["flags"]
    assert destination["camp_admin_detainees_k"] == 5 and destination["camp_admin_total_released_k"] == 0
    assert destination["state_population_k"] == 105 and r.logged == 0
    before = (destination["state_population_k"], destination["camp_admin_total_released_k"], r.debits, r.credits, r.logged)
    r.run("camp_admin_close_site", 88)
    assert before == (destination["state_population_k"], destination["camp_admin_total_released_k"], r.debits, r.credits, r.logged)
    results.append("captured uncertain custody closes operations idempotently while retaining living snapshot and zero claimed releases")
    return results


if __name__ == "__main__":
    cases = tests()
    payload = {"status": "passed", "scenarios": len(cases), "cases": cases,
               "limitations": "Parsed owned production bodies, declared campaign eligibility, mocked engine physical/manpower primitives and inverse faults. No live or archival proof."}
    (Path(__file__).parent / "origin_observer_owner_integration_source_results.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
