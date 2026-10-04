"""Actual terminal unregister, closure, projection and reform source.
Native primitives and unrelated migration/display consumers are explicit mocks.
"""
from pathlib import Path
import copy
import json
import sys
from origin_parent_lifecycle_source_tests import LifecycleRuntime
from origin_observer_owner_integration_source_tests import ROOT, foundation, custody

HERE = Path(__file__).resolve().parent


class ArchiveRuntime(LifecycleRuntime):
    def __init__(self):
        super().__init__()
        for category, _, body in foundation.parse((ROOT / "common/script_constants/camp_repression_rework_constants.txt").read_text()):
            if isinstance(body, list):
                for key, _, value in body:
                    if key != "schema" and not isinstance(value, list):
                        self.constants[category + "." + key] = float(value)
        for name in ("camp_administration_ui_triggers", "camp_administration_integration_triggers", "camp_administration_country_triggers"):
            self.triggers.update({k: b for k, _, b in foundation.parse((ROOT / f"common/scripted_triggers/{name}.txt").read_text())})
        legacy = {k: b for k, _, b in foundation.parse((ROOT / "common/scripted_effects/camp_repression_rework_effects.txt").read_text())}
        for name in ("camp_rework_unregister_inactive_site", "camp_rework_validate_selected_state", "camp_rework_clear_selected_state", "camp_rework_select_state_for_display", "camp_rework_resolve_site_evidence", "camp_rework_on_country_annexed", "camp_rework_cancel_selected_dismantlement_on_terminal", "camp_rework_clear_ledger_arrays", "camp_rework_run_versioned_migration", "camp_rework_open_ledger"):
            self.effects[name] = legacy[name]
        self.effects.update({k: b for k, _, b in foundation.parse((ROOT / "common/scripted_effects/camp_repression_colonial_country_effects.txt").read_text()) if k in ("camp_rework_italy_end_security_sweep_state", "camp_rework_clear_legacy_closure_attempt")})
        self.triggers.update({k: b for k, _, b in foundation.parse((ROOT / "common/scripted_triggers/camp_repression_rework_triggers.txt").read_text()) if k in ("has_camp_category_visible_action", "camp_rework_country_is_eligible")})
        self.effects["chaosx_refresh_camp_visual_anchor"] = []
        self.effects["genocide_try_discover_state_atrocity"] = []
        self.effects["camp_rework_clear_country_gui_action_display"] = legacy["camp_rework_clear_country_gui_action_display"]
        self.temp_arrays = {}
        self.register_calls = 0
        self.display_rebuild_calls = 0
        for name in ("migration_persecution_prepare_camp_terminal", "migration_persecution_clear_owner_state", "camp_rework_recalculate_country_values", "camp_rework_rebuild_display_values", "camp_rework_refresh_state_site_profile"):
            self.effects[name] = []

    def run(self, name, scope, params=None, prev=None):
        self.register_calls += name == "camp_rework_register_country_for_monthly_pulse"
        self.display_rebuild_calls += name == "camp_rework_rebuild_display_values"
        return super().run(name, scope, params, prev)

    def execute(self, block, scope, prev=None):
        for i, (key, op, value) in enumerate(block):
            if key in ("every_country", "every_controlled_state", "set_global_flag", "clear_temp_array", "add_to_temp_array", "set_building_level") or (key == "for_each_scope_loop" and foundation.get(value, "array") in self.temp_arrays):
                super().execute(block[:i], scope, prev)
                if key in ("every_country", "every_controlled_state"):
                    destinations = [k for k, v in self.scopes.items() if ("state_population_k" not in v if key == "every_country" else v.get("controller") == scope)]
                    for destination in destinations:
                        if self.cond(foundation.get(value, "limit", []), destination, scope):
                            self.execute([x for x in value if x[0] != "limit"], destination, scope)
                elif key == "set_global_flag":
                    self.global_flags.add(value)
                elif key == "clear_temp_array":
                    self.temp_arrays[value] = []
                elif key == "add_to_temp_array":
                    name, _, token = value[0]
                    self.temp_arrays.setdefault(name, []).append(self.val(token, scope, prev))
                elif key == "set_building_level":
                    self.scopes[scope][foundation.get(value, "type")] = self.val(foundation.get(value, "level"), scope, prev)
                else:
                    for destination in list(self.temp_arrays[foundation.get(value, "array")]):
                        self.execute([x for x in value if x[0] != "array"], destination, scope)
                self.execute(block[i + 1:], scope, prev)
                return
            if key == "remove_from_array":
                super().execute(block[:i], scope, prev)
                name = foundation.get(value, "array")
                array = self.scopes[scope]["arrays"].setdefault(name, [])
                if foundation.get(value, "index") is not None:
                    array.pop(int(self.val(foundation.get(value, "index"), scope, prev)))
                else:
                    target = self.val(foundation.get(value, "value"), scope, prev)
                    array[:] = [item for item in array if item != target]
                self.execute(block[i + 1:], scope, prev)
                return
        super().execute(block, scope, prev)


def fixture():
    r = ArchiveRuntime()
    c = r.country("GER")
    r.country("POL")
    a = r.state(88, "GER", population=100, buildings=2)
    r.state(87, "GER", population=100, buildings=2)
    custody(r, [10, 10], origins=[87, 88])
    c["arrays"]["camp_active_site_states"] = [88]
    c["arrays"]["camp_occ_states"] = []
    r.run("camp_origin_observe_host", 88)
    a.update(state_population_k=90, chaos_state_civilian_deaths_total=10000)
    r.run("camp_origin_observe_host", 88)
    return r, c, a


def reproduce():
    r, c, a = fixture()
    rows = copy.deepcopy(a["arrays"])
    r.run("camp_admin_project_origin_uncertainty", "GER")
    before = c["camp_admin_gui_uncertain_locations"]
    ready_before = r.cond(r.triggers["camp_admin_country_sites_ready_for_reform"], "GER")
    r.run("camp_rework_unregister_inactive_site", 88)
    r.run("camp_admin_project_origin_uncertainty", "GER")
    result = {"closed": "camp_admin_closed" in a["flags"], "uncertain_rows_retained": a["arrays"] == rows,
              "active_states": c["arrays"]["camp_active_site_states"], "evidence_states": c["arrays"].get("camp_evidence_states", []),
              "civilian_states": c["arrays"].get("camp_admin_civilian_states", []), "warning_before": before,
              "warning_after": c["camp_admin_gui_uncertain_locations"], "reform_ready_before": ready_before,
              "reform_ready_after": r.cond(r.triggers["camp_admin_country_sites_ready_for_reform"], "GER"),
              "physical_debits": r.debits, "death_receipts": r.logged}
    assert result["closed"] and result["uncertain_rows_retained"] and not result["active_states"]
    return result


def run_cases():
    cases = []
    result = reproduce()
    assert result["warning_before"] == result["warning_after"] == 1
    # Agent decision 2026-10-04: sticky uncertainty closes with incomplete
    # records under reform instead of stranding it before or after removal.
    assert result["reform_ready_before"] and result["reform_ready_after"]
    assert result["physical_debits"] == result["death_receipts"] == 0
    cases.append("actual terminal unregister preserves custody-only uncertainty warning, frozen rows and no receipts; sticky uncertainty does not strand reform before or after active registry removal")

    r, c, a = fixture()
    c["camp_selected_state_id"] = 88
    c["camp_admin_mandate"] = r.constants["camp_admin_mandate.coercive"]
    a["camp_admin_role"] = r.constants["camp_admin_role.labor"]
    assert r.cond(r.triggers["camp_admin_has_selected_operating_site"], "GER")
    assert not r.cond(r.triggers["camp_admin_has_selected_proven_operating_site"], "GER")
    assert not r.cond(r.triggers["camp_admin_can_toggle_selected_work"], "GER")
    assert not r.cond(r.triggers["camp_admin_can_release_selected_site"], "GER")
    cases.append("current open mixed uncertainty also fails selected operational work/release proof before terminal teardown")

    r, c, a = fixture()
    rows = copy.deepcopy(a["arrays"])
    population = a["state_population_k"]
    assert r.cond(r.triggers["camp_origin_host_records_incomplete"], 88)
    assert r.cond(r.triggers["camp_admin_country_sites_ready_for_reform"], "GER")
    r.run("camp_admin_begin_reform", "GER")
    assert "camp_admin_reforming" in c["flags"]
    assert {"camp_admin_closed", "camp_origin_ambiguity_terminal", "camp_admin_closed_records_incomplete"} <= a["flags"]
    assert a["arrays"] == rows and a["camp_admin_detainees_k"] == 20 and a.get("camp_admin_total_released_k", 0) == 0
    assert a["state_population_k"] == population and r.debits == r.logged == 0
    assert a.get("camp_admin_civilian_target_k", 0) == 0 and "camp_admin_civilian_conversion_pending" not in a["flags"]
    kinds = c["arrays"].get("camp_admin_history_kinds", [])
    assert kinds.count(r.constants["camp_admin_history_kind.records_incomplete_closure"]) == 1
    r.run("camp_admin_reform_site", 88)
    assert c["arrays"].get("camp_admin_history_kinds", []) == kinds and a["arrays"] == rows
    assert not r.cond(r.triggers["camp_origin_host_provenance_ready"], 88)
    cases.append("national reform closes an open sticky-ambiguous host once with a records-incomplete entry: no survivor release, civilian target, population change, debit or death, rows frozen and origin orders still unproven")

    for route in ("capture", "evidence", "annexation"):
        r, c, a = fixture()
        # A is the only actual active custody host; B is an origin fixture.
        c["arrays"]["camp_admin_known_site_states"] = [88]
        before_rows = copy.deepcopy(a["arrays"])
        if route == "capture":
            a["controller"] = "POL"
            r.run("camp_rework_unregister_inactive_site", 88)
        elif route == "evidence":
            c["arrays"]["camp_evidence_states"] = [88]
            r.run("camp_rework_resolve_site_evidence", 88)
            assert "genocide_responsible_country" not in a and not c["arrays"]["camp_evidence_states"]
        else:
            c["exists"] = False
            a["controller"] = "POL"
            r.run("camp_rework_on_country_annexed", "GER")
        assert c["arrays"]["camp_admin_known_site_states"] == [88]
        assert a["arrays"] == before_rows and a["camp_admin_responsible_country"] == "GER"
        assert "camp_admin_closed" in a["flags"] and not c["arrays"]["camp_active_site_states"]
        r.run("camp_admin_project_origin_uncertainty", "GER")
        assert c["camp_admin_gui_uncertain_locations"] == 1
        assert r.cond(r.triggers["camp_admin_country_sites_ready_for_reform"], "GER")
        assert r.debits == r.logged == 0
        cases.append(f"actual {route} callback retains original-country metadata and frozen rows without a death/release receipt; the closed records-incomplete host does not strand reform")

    r, c, a = fixture()
    c["arrays"]["camp_admin_known_site_states"] = [88]
    r.run("camp_rework_unregister_inactive_site", 88)
    for name in ("camp_admin_register_known_site", "camp_admin_integration_close_site", "camp_rework_unregister_inactive_site"):
        r.run(name, 88)
    assert c["arrays"]["camp_admin_known_site_states"] == [88]
    assert len(c["arrays"]["camp_admin_history_ids"]) == 1 and r.logged == r.debits == 0
    cases.append("repeated archive/close/unregister is idempotent and does not duplicate material closure or receipts")

    r, c, a = fixture()
    c["arrays"]["camp_admin_known_site_states"] = [88]
    a["controller"] = "POL"
    r.run("camp_rework_unregister_inactive_site", 88)
    c["flags"].discard("camp_admin_initialized")
    c["camp_gui_requested_state_id"] = 88
    r.run("camp_rework_select_state_for_display", "GER")
    assert c["camp_selected_state_id"] == 88
    r.run("camp_admin_refresh_interface", "GER")
    assert c["arrays"]["camp_admin_gui_states"] == [88]
    assert c["camp_admin_gui_site_detainees_k"] == 20
    assert r.cond(r.triggers["has_camp_category_visible_action"], "GER")
    assert not r.cond(r.triggers["camp_admin_has_selected_operating_site"], "GER")
    assert not r.cond(r.triggers["camp_admin_has_selected_proven_operating_site"], "GER")
    assert not r.cond(r.triggers["camp_admin_country_action_1_available"], "GER")
    assert not r.cond(r.triggers["camp_admin_can_release_selected_site"], "GER")
    assert not r.cond(r.triggers["camp_admin_can_toggle_selected_work"], "GER")
    for name in ("all", "labor", "attention"):
        c["camp_admin_location_filter"] = r.constants["camp_admin_filter." + name]
        r.run("camp_admin_refresh_interface", "GER")
        assert c["arrays"]["camp_admin_gui_states"] == [88]
    r.run("camp_admin_refresh_interface", "POL")
    assert not r.scopes["POL"]["arrays"]["camp_admin_gui_states"]
    assert not r.cond(r.triggers["camp_admin_integration_has_continuing_work"], "GER")
    r.run("camp_rework_open_ledger", "GER")
    assert "camp_repression_ledger_open" in c["flags"]
    assert c["camp_admin_view"] == r.constants["camp_admin_view.records"]
    assert "camp_admin_initialized" not in c["flags"]
    assert r.register_calls == r.display_rebuild_calls == 0
    for trigger, requested in (("camp_admin_can_set_priority", "camp_admin_priority.works"), ("camp_admin_can_set_budget", "camp_admin_budget.development"), ("camp_admin_can_set_mandate", "camp_admin_mandate.coercive")):
        r.temp["camp_admin_control_requested"] = r.constants[requested]
        assert not r.cond(r.triggers[trigger], "GER")
    cases.append("captured closed record is selectable and filtered for original actor; metadata-only category grants no policy/work/release or periodic registry work")

    r, c, a = fixture()
    c["arrays"]["camp_admin_known_site_states"] = []
    c["exists"] = False
    a["controller"] = "POL"
    a["flags"].add("camp_admin_closed")
    # Missing authority cannot be inferred from current controller/owner.
    missing = r.scopes[87]
    missing["controller"] = "POL"
    missing.pop("camp_admin_responsible_country", None)
    c["arrays"]["camp_active_site_states"] = []
    before = copy.deepcopy(a)
    # The current legacy schema must not suppress the accepted startup archive pass.
    r.temp["global.camp_rework_schema_version"] = r.constants["camp_rework_schema.current"]
    r.run("camp_rework_run_versioned_migration", "POL")
    assert c["arrays"]["camp_admin_known_site_states"] == [88]
    assert a == before and not r.scopes["POL"]["arrays"].get("camp_admin_known_site_states")
    r.run("camp_rework_run_versioned_migration", "POL")
    assert c["arrays"]["camp_admin_known_site_states"] == [88]
    assert "camp_admin_known_sites_bootstrapped" in r.global_flags
    assert r.debits == r.logged == 0 and not c["arrays"].get("camp_admin_history_ids")
    cases.append("single metadata bootstrap handles closed site under another controller and ceased original actor, skips missing authority and creates no dated history")

    c["exists"] = True
    a["controller"] = "GER"
    a.update(camp_admin_works_k=20, camp_admin_construction_factor=0.4, camp_admin_extraction_factor=0.4)
    c["camp_selected_state_id"] = 88
    r.run("camp_admin_refresh_interface", "GER")
    assert c["camp_admin_gui_works_sites"] == c["camp_admin_gui_extraction_sites"] == 0
    assert c["camp_admin_gui_site_workforce_k"] == c["camp_admin_gui_site_construction"] == c["camp_admin_gui_site_extraction"] == 0
    assert a["camp_admin_works_k"] == 20 and a["camp_admin_construction_factor"] == 0.4
    cases.append("archive-only closed stale output is not projected as productive workers or economic contribution and archive writes leave source values untouched")

    r = ArchiveRuntime()
    c = r.country("GER")
    a = r.state(88, "GER")
    r.run("camp_admin_close_site", 88)
    assert r.cond(r.triggers["camp_admin_country_sites_ready_for_reform"], "GER")
    assert a["camp_admin_detainees_k"] == 0
    cases.append("valid healthy empty terminal archive does not strand national reform")

    r = ArchiveRuntime()
    c = r.country("GER")
    a = r.state(88, "GER")
    foundation.prime_existing_custody(r, 88, 10)
    r.run("camp_admin_close_site", 88)
    assert a["camp_admin_total_released_k"] == 10 and a["arrays"]["camp_admin_row_amounts_k"] == [0]
    a["state_population_k"] -= 1
    a["chaos_state_civilian_deaths_total"] = 1000
    before = copy.deepcopy(a)
    r.run("camp_admin_project_origin_uncertainty", "GER")
    assert c["camp_admin_gui_uncertain_locations"] == 0 and a == before
    assert r.cond(r.triggers["camp_admin_country_sites_ready_for_reform"], "GER")
    assert not r.cond(r.triggers["camp_origin_host_provenance_ready"], 88)
    assert c["arrays"]["camp_admin_known_site_states"] == [88] and r.debits == r.logged == 0
    for flag in ("camp_origin_ambiguous", "camp_origin_records_unresolved", "camp_origin_baseline_unverified", "camp_origin_transaction_unresolved", "camp_origin_counter_regressed", "camp_origin_single_origin_reconciliation_pending"):
        a["flags"].add(flag)
        r.run("camp_admin_project_origin_uncertainty", "GER")
        assert c["camp_admin_gui_uncertain_locations"] == 1 and flag in a["flags"]
        a["flags"].remove(flag)
    cases.append("real exact 10k release leaves aligned zero-live history: unrelated later 1k territorial/shared loss warns no missing held people, while every explicit sticky/structural reason remains visible and action freshness stays false")

    r = ArchiveRuntime()
    c = r.country("GER")
    a = r.state(88, "GER")
    foundation.prime_existing_custody(r, 88, 10)
    a["camp_admin_detainees_k"] = 0
    r.run("camp_rework_unregister_inactive_site", 88)
    r.run("camp_admin_project_origin_uncertainty", "GER")
    assert "camp_admin_closed" in a["flags"] and c["camp_admin_gui_uncertain_locations"] == 1
    assert a["arrays"]["camp_admin_row_amounts_k"] == [10]
    assert not r.cond(r.triggers["camp_admin_country_sites_ready_for_reform"], "GER")
    assert r.debits == r.logged == 0
    cases.append("malformed zero aggregate with retained live closed row remains visible and fails complete archive reform preflight")

    r = ArchiveRuntime()
    c = r.country("GER")
    for state_id in range(10000, 11001):
        r.state(state_id, "GER")["flags"].add("camp_admin_closed")
    c["arrays"]["camp_active_site_states"] = []
    r.scopes[11000]["flags"].add("camp_origin_ambiguous")
    r.run("camp_admin_refresh_interface", "GER")
    assert len(c["arrays"]["camp_admin_known_site_states"]) == 1001
    assert len(c["arrays"]["camp_admin_gui_states"]) == 1001
    assert c["camp_admin_gui_uncertain_locations"] == 1
    assert r.cond(r.triggers["camp_admin_country_sites_ready_for_reform"], "GER")
    r.scopes[11000]["flags"].discard("camp_origin_ambiguous")
    r.scopes[11000]["arrays"]["camp_admin_row_amounts_k"] = [5]
    r.scopes[11000]["camp_admin_row_count"] = 1
    assert not r.cond(r.triggers["camp_admin_country_sites_ready_for_reform"], "GER")
    cases.append("native array iterators retain all 1001 declared archive entries and inspect the final host without source row caps: sticky uncertainty there is reformable, a malformed unflagged ledger is not")
    return cases


if __name__ == "__main__":
    cases = [] if "--before" in sys.argv else run_cases()
    result = reproduce() if "--before" in sys.argv else {"count": len(cases), "cases": cases, "limits": "Parsed production callbacks with explicit native mocks; no native ceased-country setter, GUI pixel or runtime proof."}
    destination = "origin_closed_archive_reproduction_before.json" if "--before" in sys.argv else "origin_closed_archive_source_results.json"
    (HERE / destination).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
