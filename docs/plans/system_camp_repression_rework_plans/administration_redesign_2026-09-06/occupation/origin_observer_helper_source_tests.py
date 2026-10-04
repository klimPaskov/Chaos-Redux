"""Parsed production origin helpers with mocked Clausewitz primitives.
No game launch, row-policy substitute or runtime proof.
Run from the mod root with Python. Uses the existing foundation parser/runtime.
"""
from pathlib import Path
import importlib.util
import copy
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("camp_foundation", HERE.parent / "foundation_source_tests.py")
foundation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foundation)
ROOT = foundation.ROOT


class OriginRuntime(foundation.Runtime):
    def __init__(self):
        super().__init__()
        self.effects.update({key: body for key, _, body in foundation.parse((ROOT / "common/scripted_effects/camp_administration_origin_effects.txt").read_text())})
        self.triggers.update({key: body for key, _, body in foundation.parse((ROOT / "common/scripted_triggers/camp_administration_origin_triggers.txt").read_text())})
        for file in ("camp_administration_origin_constants.txt", "camp_administration_occupation_constants.txt"):
            for category, _, body in foundation.parse((ROOT / "common/script_constants" / file).read_text()):
                for key, _, value in body:
                    if key != "schema" and not isinstance(value, list):
                        self.constants[category + "." + key] = float(value)

    def cond(self, block, scope, previous=None):
        # Installed documentation permits temporary arithmetic in triggers.
        # Extend only that primitive surface of the existing source harness.
        if scope not in self.scopes:
            return False
        for key, op, value in block:
            if key == "state":
                if not self.state_scope_matches(scope, value, previous):
                    return False
            elif key in {"set_temp_variable", "add_to_temp_variable", "subtract_from_temp_variable", "multiply_temp_variable", "divide_temp_variable", "clamp_temp_variable", "round_temp_variable"}:
                self.execute([(key, op, value)], scope, previous)
            elif not super().cond([(key, op, value)], scope, previous):
                return False
        return True


def fixture(population=100, initialize=True):
    runtime = OriginRuntime()
    runtime.scopes["GER"] = {"id": "GER", "exists": True, "flags": set(), "arrays": {}, "mods": set()}
    for state_id in (88, 101, 102):
        runtime.scopes[state_id] = {"id": state_id, "state": state_id, "flags": set(), "arrays": {}, "mods": set(), "state_population_k": population, "chaos_state_civilian_deaths_total": 0}
    if initialize:
        runtime.run("camp_origin_initialize_host", 88)
    return runtime


def occupation(runtime, amounts, origins=None, roots=None):
    origins = origins or [101 + index for index in range(len(amounts))]
    country = runtime.scopes["GER"]
    country["flags"].add("camp_occ_rows_initialized")
    count = len(amounts)
    fields = {
        "ids": list(range(1, count + 1)), "root_ids": roots or list(range(1, count + 1)),
        "origins": origins, "hosts": [88] * count, "authorities": ["GER"] * count,
        "profiles": [1] * count, "amounts_k": list(amounts), "statuses": [1] * count,
    }
    for name in ("deaths_k", "removed_k", "released_k", "moved_out_k", "moved_in_k"):
        fields[name] = [0] * count
    country["arrays"] = {"camp_occ_row_" + name: values for name, values in fields.items()}
    country.update(camp_occ_row_count=count, camp_occ_next_row_id=count + 1)
    host = runtime.scopes[88]
    host["flags"].add("camp_occ_registered")
    host.update(camp_occ_responsible_country="GER", camp_occ_remaining_k=sum(amounts))


def custody(runtime, amounts, origins=None, roots=None):
    origins = origins or [101 + index for index in range(len(amounts))]
    host = runtime.scopes[88]
    host["flags"].update({"camp_admin_initialized", "camp_admin_rows_initialized"})
    count = len(amounts)
    fields = {
        "ids": list(range(1, count + 1)), "origins": origins, "authorities": ["GER"] * count,
        "occupation_roots": roots or [0] * count, "amounts_k": list(amounts), "statuses": [1] * count,
    }
    for name in ("deaths_k", "arrival_deaths_k", "released_k", "removed_k"):
        fields[name] = [0] * count
    host["arrays"] = {"camp_admin_row_" + name: values for name, values in fields.items()}
    host.update(camp_admin_responsible_country="GER", camp_admin_detainees_k=sum(amounts), camp_admin_row_count=count, camp_admin_next_row_id=count + 1)


def observe(runtime):
    runtime.run("camp_origin_observe_host", 88)
    assert runtime.debits == 0 and runtime.logged == 0
    return runtime.scopes[88]


def known(runtime, before_population, after_population, before_deaths=0, after_deaths=0, sequence=None):
    runtime.temp.update({
        "camp_origin_known_contract": 1,
        "camp_origin_known_observation_sequence": runtime.scopes[88]["camp_origin_observation_sequence"] if sequence is None else sequence,
        "camp_origin_known_before_population_k": before_population,
        "camp_origin_known_after_population_k": after_population,
        "camp_origin_known_before_state_deaths_people": before_deaths,
        "camp_origin_known_after_state_deaths_people": after_deaths,
    })
    runtime.run("camp_origin_adjust_known_receipt", 88)
    assert runtime.debits == 0 and runtime.logged == 0
    assert runtime.temp["camp_origin_known_contract"] == 0
    return runtime.temp["camp_origin_known_adjustment_accepted"]


def tests():
    results = []
    r = fixture()
    assert r.cond(r.triggers["camp_origin_host_provenance_ready"], 88)
    original = copy.deepcopy(r.scopes[88])
    r.scopes[88]["state_population_k"] += 25
    r.run("camp_origin_initialize_host", 88)
    assert r.scopes[88]["camp_origin_observed_population_k"] == original["camp_origin_observed_population_k"]
    results.append("empty opening is ready and initialization cannot rebase growth")

    for family in (occupation, custody):
        r = fixture(population=200)
        family(r, [10, 10])
        observe(r)
        rows = copy.deepcopy(r.scopes["GER"]["arrays"] if family is occupation else r.scopes[88]["arrays"])
        r.scopes[88].update(state_population_k=190, chaos_state_civilian_deaths_total=10000)
        assert not r.cond(r.triggers["camp_origin_host_provenance_ready"], 88)
        host = observe(r)
        assert "camp_origin_ambiguous" in host["flags"]
        assert r.temp["camp_origin_observed_outside_signal_k"] == 10
        assert rows == (r.scopes["GER"]["arrays"] if family is occupation else host["arrays"])
        first_epoch = host["camp_origin_ambiguity_sequence"]
        observe(r)
        assert host["camp_origin_total_observed_shared_loss_k"] == 10
        host["state_population_k"] = 250
        observe(r)
        assert "camp_origin_ambiguous" in host["flags"] and host["camp_origin_ambiguity_sequence"] == first_epoch
        results.append(f"{family.__name__}: A/B 10k outside loss freezes rows, repeated observation and growth preserve pause")

    r = fixture()
    occupation(r, [10, 10])
    observe(r)
    r.scopes[88].update(state_population_k=105, chaos_state_civilian_deaths_total=10000)
    host = observe(r)
    assert "camp_origin_ambiguous" in host["flags"] and r.temp["camp_origin_observed_net_decline_k"] == 0
    assert host["camp_origin_total_observed_shared_loss_k"] == 10
    results.append("net growth cannot mask new shared Deaths")

    r = fixture()
    occupation(r, [10], origins=[101], roots=[1])
    custody(r, [10], origins=[102], roots=[2])
    observe(r)
    r.scopes[88]["state_population_k"] = 90
    host = observe(r)
    assert "camp_origin_ambiguous" in host["flags"] and r.temp["camp_origin_live_row_count"] == 2
    assert host["camp_occ_remaining_k"] == 10 and host["camp_admin_detainees_k"] == 10
    results.append("one occupation A plus one custody B requires joint host containment")

    r = fixture(population=20)
    custody(r, [10, 10])
    host = observe(r)
    assert "camp_origin_ambiguous" in host["flags"] and host["camp_origin_current_shortfall_k"] == 1
    assert host["camp_origin_total_observed_shared_loss_k"] == host["camp_origin_total_observed_net_decline_k"] == 0
    observe(r)
    assert host["camp_origin_current_shortfall_k"] == 1
    results.append("physical headroom mismatch is current evidence rather than a repeated death")

    r = fixture(initialize=False)
    custody(r, [10, 10])
    host = observe(r)
    assert {"camp_origin_baseline_unverified", "camp_origin_ambiguous"} <= host["flags"]
    assert host["camp_origin_total_observed_shared_loss_k"] == host["camp_origin_total_observed_net_decline_k"] == 0
    results.append("live custody without opening baseline is unverified without an invented loss")

    r = fixture(initialize=False)
    custody(r, [10, 10])
    r.scopes[88]["flags"].add("camp_admin_origin_estimated")
    r.scopes[88]["camp_admin_unknown_origin_removed_k"] = 5
    host = observe(r)
    assert {"camp_origin_baseline_unverified", "camp_origin_ambiguous"} <= host["flags"]
    assert host["camp_admin_unknown_origin_removed_k"] == 5
    assert host["camp_origin_last_verified_custody_k"] == 0
    assert host["camp_origin_unresolved_shared_loss_k"] == 0
    results.append("inherited proportional estimate is preserved as unverified rather than promoted into verified rows")

    r = fixture(initialize=False)
    occupation(r, [10, 10])
    r.scopes[88].update(camp_occ_observed_population_k=100, camp_occ_observed_state_deaths=0, state_population_k=90, chaos_state_civilian_deaths_total=10000)
    host = observe(r)
    assert "camp_origin_ambiguous" in host["flags"] and "camp_origin_baseline_unverified" not in host["flags"]
    assert host["camp_origin_unresolved_shared_loss_k"] == 10
    results.append("adopted occupation opening preserves the unobserved outside interval")

    r = fixture()
    custody(r, [10, 10], origins=[101, 101], roots=[1, 2])
    observe(r)
    r.scopes[88]["state_population_k"] = 90
    assert "camp_origin_ambiguous" in observe(r)["flags"]
    results.append("same original state with distinct roots does not prove a selected row")

    for family in (occupation, custody):
        r = fixture()
        family(r, [20], origins=[101], roots=[1])
        observe(r)
        r.scopes[88].update(state_population_k=90, chaos_state_civilian_deaths_total=10000)
        host = observe(r)
        assert "camp_origin_ambiguous" not in host["flags"]
        assert "camp_origin_single_origin_reconciliation_pending" in host["flags"]
        assert host["camp_origin_pending_single_removal_k"] == 10
        observe(r)
        assert host["camp_origin_pending_single_removal_k"] == 10
        assert not r.cond(r.triggers["camp_origin_host_provenance_ready"], 88)
        rows = r.scopes["GER"]["arrays"] if family is occupation else host["arrays"]
        prefix = "camp_occ_row_" if family is occupation else "camp_admin_row_"
        # Caller retirement is deliberately a mock because this worker does not
        # own the existing outside-retirement helper or its production wiring.
        rows[prefix + "amounts_k"][0] = 10
        rows[prefix + "removed_k"][0] = 10
        host["camp_occ_remaining_k" if family is occupation else "camp_admin_detainees_k"] = 10
        r.temp.update(camp_origin_single_reconcile_contract=1, camp_origin_single_reconcile_sequence=host["camp_origin_observation_sequence"], camp_origin_single_reconcile_amount_k=9)
        r.run("camp_origin_acknowledge_single_origin_reconciliation", 88)
        assert r.temp["camp_origin_single_reconciliation_accepted"] == 0
        assert "camp_origin_single_origin_reconciliation_pending" in host["flags"]
        r.temp.update(camp_origin_single_reconcile_contract=1, camp_origin_single_reconcile_sequence=host["camp_origin_observation_sequence"], camp_origin_single_reconcile_amount_k=10)
        r.run("camp_origin_acknowledge_single_origin_reconciliation", 88)
        assert r.temp["camp_origin_single_reconciliation_accepted"] == 1
        assert "camp_origin_single_origin_reconciliation_pending" not in host["flags"]
        assert r.cond(r.triggers["camp_origin_host_provenance_ready"], 88)
        assert r.debits == 0 and r.logged == 0
        results.append(f"{family.__name__}: one unique row retains pending retirement until an exact ledger-only acknowledgment")

    r = fixture()
    custody(r, [20], origins=[101], roots=[1])
    observe(r)
    r.scopes[88].update(state_population_k=90, chaos_state_civilian_deaths_total=10000)
    host = observe(r)
    rows = host["arrays"]
    rows["camp_admin_row_amounts_k"][0] = 10
    rows["camp_admin_row_removed_k"][0] = 10
    rows["camp_admin_row_deaths_k"][0] = 1
    host["camp_admin_detainees_k"] = 10
    r.temp.update(camp_origin_single_reconcile_contract=1, camp_origin_single_reconcile_sequence=host["camp_origin_observation_sequence"], camp_origin_single_reconcile_amount_k=10)
    r.run("camp_origin_acknowledge_single_origin_reconciliation", 88)
    assert r.temp["camp_origin_single_reconciliation_accepted"] == 0
    assert "camp_origin_single_origin_reconciliation_pending" in host["flags"]
    results.append("single-origin acknowledgment rejects a matching outside amount that also fabricated a row death")

    r = fixture()
    custody(r, [10, 10])
    observe(r)
    r.scopes[88].update(state_population_k=90, chaos_state_civilian_deaths_total=10000)
    observe(r)
    r.scopes[88]["state_population_k"] = 95
    assert known(r, 90, 95, 10000, 10000) == 1
    r.scopes[88]["flags"].add("camp_admin_closed")
    observe(r)
    assert "camp_origin_ambiguous" in r.scopes[88]["flags"]
    r.temp.update(camp_origin_single_reconcile_contract=1, camp_origin_single_reconcile_sequence=r.scopes[88]["camp_origin_observation_sequence"], camp_origin_single_reconcile_amount_k=0)
    r.run("camp_origin_acknowledge_single_origin_reconciliation", 88)
    assert r.temp["camp_origin_single_reconciliation_accepted"] == 0
    assert "camp_origin_ambiguous" in r.scopes[88]["flags"]
    results.append("unrelated measured credit, closure and single-origin acknowledgment cannot clear mixed ambiguity")

    r = fixture()
    custody(r, [10, 10])
    observe(r)
    r.scopes[88]["arrays"]["camp_admin_row_amounts_k"][0] = 9
    r.scopes[88].update(camp_admin_detainees_k=19, state_population_k=99, chaos_state_civilian_deaths_total=1000)
    assert known(r, 100, 99, 0, 1000) == 1
    assert "camp_origin_ambiguous" not in r.scopes[88]["flags"]
    assert r.scopes[88]["camp_origin_total_observed_shared_loss_k"] == 0
    observe(r)
    assert r.cond(r.triggers["camp_origin_host_provenance_ready"], 88)
    results.append("selected-row own death adjusts common baseline without outside-loss attribution")

    r = fixture()
    custody(r, [10, 10])
    observe(r)
    r.scopes[88]["arrays"]["camp_admin_row_amounts_k"][0] = 9
    r.scopes[88].update(camp_admin_detainees_k=19, state_population_k=98, chaos_state_civilian_deaths_total=2000)
    assert known(r, 100, 99, 0, 1000) == 1
    host = r.scopes[88]
    assert "camp_origin_ambiguous" in host["flags"] and host["camp_origin_unresolved_shared_loss_k"] == 1
    results.append("residual outside loss after a measured own receipt is preserved and quarantined")

    r = fixture()
    observe(r)
    assert known(r, 100, 100, sequence=0) == 1
    baseline = copy.deepcopy(r.scopes[88])
    assert known(r, 100, 100, sequence=0) == 0 and baseline == r.scopes[88]
    assert known(r, 90, 100) == 0 and baseline == r.scopes[88]
    results.append("completed zero-net inverse is accepted once and stale/wrong-baseline adjustments are inert")

    r = fixture()
    occupation(r, [20], origins=[101], roots=[1])
    observe(r)
    r.scopes[88]["state_population_k"] = 95
    r.scopes[88]["flags"].add("camp_occ_custody_rollback_failed")
    assert known(r, 100, 95) == 0
    host = observe(r)
    assert {"camp_origin_ambiguous", "camp_origin_transaction_unresolved"} <= host["flags"]
    assert host["camp_occ_remaining_k"] == 20
    assert host["camp_origin_total_observed_shared_loss_k"] == 0
    assert host["camp_origin_observed_population_k"] == 100
    assert host["camp_origin_transaction_observed_population_k"] == 95
    assert not r.cond(r.triggers["camp_origin_host_provenance_ready"], 88)
    host.update(state_population_k=94, chaos_state_civilian_deaths_total=1000)
    observe(r)
    assert host["camp_origin_unresolved_shared_loss_k"] == 1
    assert host["camp_origin_unresolved_net_decline_k"] == 1
    assert host["camp_origin_observed_population_k"] == 100
    results.append("failed inverse rejects known rebase, preserves its verified opening and observes subsequent loss from a separate checkpoint")

    r = fixture()
    r.scopes[88].update(state_population_k=99, chaos_state_civilian_deaths_total=1000)
    assert known(r, 100, 99, 0, 1000) == 1
    r.scopes[88]["chaos_state_civilian_deaths_total"] = 0
    host = observe(r)
    assert {"camp_origin_ambiguous", "camp_origin_counter_regressed"} <= host["flags"]
    assert r.temp["camp_origin_observed_shared_loss_k"] == 0
    results.append("shared counter regression is quarantined without a fabricated positive loss")

    r = fixture()
    custody(r, [0] * 1000, origins=[101] * 1000)
    assert r.cond(r.triggers["camp_origin_host_rows_valid"], 88)
    assert r.temp["camp_origin_live_row_count"] == 0
    results.append("the exact 1000-row bound is fully inspected rather than rejected or truncated")

    for defect in ("shape", "duplicate", "scope", "over_limit"):
        r = fixture()
        custody(r, [10, 10])
        if defect == "shape":
            r.scopes[88]["arrays"]["camp_admin_row_origins"].pop()
        elif defect == "duplicate":
            r.scopes[88]["arrays"]["camp_admin_row_ids"][1] = 1
        elif defect == "scope":
            r.scopes[88]["arrays"]["camp_admin_row_origins"][1] = 99999
        else:
            custody(r, [0] * 1001, origins=[101] * 1001)
        assert not r.cond(r.triggers["camp_origin_host_rows_valid"], 88)
        assert "camp_origin_records_unresolved" in observe(r)["flags"]
        results.append(f"invalid registry {defect} fails closed without a prefix treated as a complete scan")

    for file in ("common/scripted_effects/camp_administration_origin_effects.txt", "common/scripted_triggers/camp_administration_origin_triggers.txt"):
        source = (ROOT / file).read_text()
        assert not any(token in source for token in ("apply_exact_state_civilian_population_loss =", "chaos_meter_register_deaths =", "add_manpower =", "add_to_array =", "set_variable = { camp_admin_row_", "set_variable = { camp_occ_row_", "clr_state_flag = camp_origin_ambiguous", "every_state", "every_country"))
    return results


if __name__ == "__main__":
    results = tests()
    payload = {"scope": "parsed owned production origin module", "engine_primitives": "mocked", "runtime_proof": False, "passed": len(results), "scenarios": results}
    (HERE / "origin_observer_helper_source_results.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
