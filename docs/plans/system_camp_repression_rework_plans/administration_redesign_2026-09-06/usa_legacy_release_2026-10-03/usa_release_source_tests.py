"""Exercise the USA release through parsed production decision/effect/trigger source.

The foundation harness is an explicit Clausewitz source interpreter mock. This
file adds only engine primitives needed by the actual selector (temporary arrays,
root scope, deterministic random choice) and a declared interleaving hook for a
stale GUI click. It does not replace production selector, dispatcher, or
cooldown helper bodies, and it is not HOI4 engine or campaign evidence.

Run from repository root:
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/usa_legacy_release_2026-10-03/usa_release_source_tests.py
"""
from pathlib import Path
import hashlib
import json
import sys

HANDOFF_DIR = Path(__file__).resolve().parent
ADMIN_PLAN_DIR = HANDOFF_DIR.parent
ROOT = HANDOFF_DIR.parents[4]
sys.path.insert(0, str(ADMIN_PLAN_DIR))

from foundation_source_tests import Runtime, get, parse, prime_existing_custody
import black_friday_sale_prices as sale


SOURCE_PATHS = [
    "common/decisions/camp_repression_colonial_country_decisions.txt",
    "common/scripted_effects/camp_repression_colonial_country_effects.txt",
    "common/scripted_effects/camp_repression_action_dispatcher_effects.txt",
    "common/scripted_effects/camp_repression_rework_effects.txt",
    "common/scripted_effects/camp_administration_civil_effects.txt",
    "common/scripted_triggers/camp_repression_rework_triggers.txt",
    "common/scripted_triggers/camp_administration_triggers.txt",
    "common/scripted_triggers/camp_administration_origin_triggers.txt",
    "common/scripted_triggers/genocide_crisis_triggers.txt",
    "common/script_constants/camp_repression_rework_constants.txt",
    "common/script_constants/camp_administration_civil_constants.txt",
    "localisation/english/camp_repression_rework_l_english.yml",
]


def remove_tooltip_wrappers(block):
    cleaned = []
    for key, op, value in block:
        if key == "custom_trigger_tooltip":
            cleaned.extend(remove_tooltip_wrappers([item for item in value if item[0] != "tooltip"]))
        elif isinstance(value, list):
            cleaned.append((key, op, remove_tooltip_wrappers(value)))
        else:
            cleaned.append((key, op, value))
    return cleaned


def find_block(block, name):
    for key, _, value in block:
        if key == name:
            return value
        if isinstance(value, list):
            found = find_block(value, name)
            if found is not None:
                return found
    return None


class ReleaseRuntime(Runtime):
    def __init__(self):
        super().__init__()
        self.root_scope = None
        self.temp_arrays = {}
        self.gui_cutover_hook = False

        for relative in SOURCE_PATHS:
            source = (ROOT / relative).read_text(encoding="utf-8-sig")
            if relative.startswith("common/scripted_effects/") or relative.startswith("common/decisions/"):
                if relative.startswith("common/scripted_effects/"):
                    self.effects.update({key: value for key, _, value in parse(source) if not key.startswith("@")})
            elif relative.startswith("common/scripted_triggers/"):
                self.triggers.update({key: value for key, _, value in parse(source)})
            elif relative.startswith("common/script_constants/"):
                for category, _, values in parse(source):
                    for key, _, value in values:
                        if key != "schema" and not isinstance(value, list):
                            self.constants[f"{category}.{key}"] = float(value)

        base_target = self.target

        def release_target(target, scope, previous):
            if target == "ROOT":
                return self.root_scope if self.root_scope is not None else scope
            return base_target(target, scope, previous)

        self.target = release_target

        base_value = self.val

        def release_value(value, scope, previous=None):
            if isinstance(value, str) and value.endswith("^num") and value[:-4] in self.temp_arrays:
                return len(self.temp_arrays[value[:-4]])
            if value == "has_political_power":
                return self.scopes[scope].get("political_power", 0)
            return base_value(value, scope, previous)

        self.val = release_value

        base_condition = self.cond

        def contains_controlled_state_iterator(block):
            return any(
                key == "any_controlled_state"
                or (isinstance(value, list) and contains_controlled_state_iterator(value))
                for key, _, value in block
            )

        def expand_controlled_state_iterators(block, scope, previous):
            expanded = []
            for key, op, value in block:
                if key == "any_controlled_state":
                    candidates = [
                        state_id for state_id, data in self.scopes.items()
                        if "state_population_k" in data and data.get("controller") == scope
                    ]
                    expanded.append(("OR", "=", [
                        (state_id, "=", expand_controlled_state_iterators(value, state_id, scope))
                        for state_id in candidates
                    ]))
                elif isinstance(value, list) and key in ("AND", "OR", "NOT", "if", "else_if", "else", "all_of", "all_of_scopes", "any_of_scopes"):
                    expanded.append((key, op, expand_controlled_state_iterators(value, scope, previous)))
                elif isinstance(value, list) and (key in ("ROOT", "PREV", "THIS", "OWNER", "CONTROLLER") or key.startswith(("var:", "event_target:")) or key.isdigit()):
                    child_scope = self.target(key, scope, previous)
                    expanded.append((key, op, expand_controlled_state_iterators(value, child_scope, scope)))
                elif isinstance(value, list):
                    expanded.append((key, op, value))
                else:
                    expanded.append((key, op, value))
            return expanded

        def release_condition(block, scope, previous=None):
            owns_root = self.root_scope is None
            if owns_root:
                self.root_scope = scope
            try:
                cleaned = remove_tooltip_wrappers(block)
                expanded = expand_controlled_state_iterators(cleaned, scope, previous) if contains_controlled_state_iterator(cleaned) else cleaned
                return base_condition(expanded, scope, previous)
            finally:
                if owns_root:
                    self.root_scope = None

        self.cond = release_condition

        base_run = self.run

        def release_run(name, scope, params=None, previous=None):
            base_run(name, scope, params, previous)
            if name == "camp_rework_gui_pay_political_cost" and self.gui_cutover_hook:
                self.scopes["USA"]["flags"].add("camp_admin_civil_initialized")
                self.gui_cutover_hook = False

        self.run = release_run

        base_execute = self.execute

        def release_execute(block, scope, previous=None):
            owns_root = self.root_scope is None
            if owns_root:
                self.root_scope = scope
            try:
                self._execute_release_primitives(block, scope, previous, base_execute)
            finally:
                if owns_root:
                    self.root_scope = None

        self.execute = release_execute

    def _execute_release_primitives(self, block, scope, previous, base_execute):
        chain = False
        for key, op, value in block:
            if key in ("if", "else_if", "else"):
                okay = (key == "if" or not chain) and (key == "else" or self.cond(get(value, "limit", []), scope, previous))
                if key == "if":
                    chain = False
                if okay:
                    self.execute([item for item in value if item[0] != "limit"], scope, previous)
                    chain = True
                continue
            if key == "clear_temp_array":
                self.temp_arrays[value] = []
                continue
            if key == "add_to_temp_array":
                if get(value, "array") is not None:
                    array, item = get(value, "array"), get(value, "value")
                else:
                    array, _, item = value[0]
                target = self.target(item, scope, previous)
                self.temp_arrays.setdefault(array, []).append(target)
                continue
            if key == "random_scope_in_array":
                candidates = self.temp_arrays.get(get(value, "array"), [])
                if candidates:
                    chosen = candidates[0]  # Deterministic mock of this engine primitive only.
                    self.execute([item for item in value if item[0] != "array"], chosen, scope)
                continue
            if key == "add_equipment_to_stockpile" and get(value, "type") == "support_equipment_1":
                amount = self.val(get(value, "amount"), scope, previous)
                equipment = self.scopes[scope].setdefault("equipment", {})
                equipment["support_equipment_1"] = equipment.get("support_equipment_1", 0) + amount
                continue
            if key in ("add_ideas", "remove_ideas"):
                ideas = self.scopes[scope].setdefault("ideas", set())
                names = [item[2] for item in value] if isinstance(value, list) else [value]
                if key == "add_ideas":
                    ideas.update(names)
                else:
                    ideas.difference_update(names)
                continue
            base_execute([(key, op, value)], scope, previous)


SALE_RATIO = sale.RATIO_BASIS


def new_release_runtime(stock=180, ai=False, rows_k=4):
    runtime = ReleaseRuntime()
    sale.install(runtime, SALE_RATIO)
    country = runtime.country("USA")
    country.update(original_tag="USA", is_ai=ai, has_war=True, eligible=True)
    country["equipment"] = {"support_equipment_1": stock}
    country["flags"].update({
        "camp_rework_usa_authority_active",
        "camp_rework_inspection_active",
        "camp_rework_managed_network_visible",
    })
    state = runtime.state("378", "USA", population=10000, buildings=2)
    state["flags"].discard("camp_rework_expanded_labor_site")
    state.update(genocide_responsible_country="USA", camp_admin_responsible_country="USA")
    prime_existing_custody(runtime, "378", rows_k)
    country["camp_active_site_count"] = len(country["arrays"]["camp_active_site_states"])
    assert country["camp_active_site_count"] == 1
    country["camp_selected_state_id"] = "378"
    country.update(
        political_power=100,
        relocation_population_disruption=20,
        wartime_security_reach=20,
        court_challenge_pressure=5,
    )
    return runtime, country, state


def load_decision():
    source = (ROOT / SOURCE_PATHS[0]).read_text(encoding="utf-8-sig")
    decision = find_block(parse(source), "usa_release_detainees_under_supervision")
    assert decision is not None
    assert get(decision, "days_re_enable") is None, "rejected native clicks must not start an unconditional engine cooldown"
    localization = (ROOT / SOURCE_PATHS[-1]).read_text(encoding="utf-8-sig")
    assert "camp_rework_usa_release_order_requirements_tt:" in localization
    assert "camp_rework_usa_release_order_effect_tt:" in localization
    assert "£support_equipment_text_icon" in localization
    assert "Security administration continues while sites remain active." in localization
    assert "Equipment is spent only on a confirmed release." in localization
    return decision


def decision_is_available(runtime, decision):
    return runtime.cond(get(decision, "available"), "USA")


def require_available(runtime, decision):
    if not decision_is_available(runtime, decision):
        origin_rows_valid = runtime.cond([("camp_origin_host_rows_valid", "=", "yes")], "378")
        provenance_parts = [
            {"trigger": key, "value": value, "result": runtime.cond([(key, op, value)], "378")}
            for key, op, value in runtime.triggers["camp_origin_host_provenance_ready"]
        ]
        row_parts = [
            {"trigger": key, "value": value, "result": runtime.cond([(key, op, value)], "378")}
            for key, op, value in runtime.triggers["camp_admin_site_rows_reconciled"]
        ]
        diagnostics = {
            name: runtime.cond([(name, "=", "yes")], "USA")
            for name in (
                "camp_rework_usa_release_country_eligible",
                "camp_rework_usa_release_order_ready",
                "camp_rework_usa_release_site_ready",
                "camp_admin_site_rows_reconciled",
                "camp_origin_host_provenance_ready",
                "has_active_camp_network",
            )
        }
        origin_temps = {key: value for key, value in runtime.temp.items() if key.startswith("camp_origin_") or key.startswith("camp_admin_reconcile_")}
        raise AssertionError(json.dumps({"available": False, "origin_rows_valid": origin_rows_valid, "provenance_parts": provenance_parts, "row_parts": row_parts, "diagnostics": diagnostics, "origin_temps": origin_temps, "country": runtime.scopes["USA"], "state": runtime.scopes["378"]}, default=str))


def native_click(runtime, decision, already_paid=False):
    if not already_paid:
        cost = runtime.val(get(decision, "cost"), "USA")
        runtime.scopes["USA"]["political_power"] -= cost  # Native decision payment primitive mock.
    runtime.execute(get(decision, "complete_effect"), "USA")


def assert_rejected(runtime, country, state, pp_before=100, support_before=180, detainees_before=4):
    assert country["political_power"] == pp_before, country["political_power"]
    assert country["equipment"]["support_equipment_1"] == support_before
    assert state["camp_admin_detainees_k"] == detainees_before
    assert state.get("camp_admin_total_released_k", 0) == 0
    assert "camp_admin_census_intake_closed" not in state["flags"]
    assert "camp_rework_site_reforming" not in state["flags"]
    assert not country["arrays"].get("camp_admin_history_kinds", [])
    assert "camp_gui_country_action_2_cooldown" not in country["flags"]
    assert country["relocation_population_disruption"] == 20
    assert country["court_challenge_pressure"] == 5
    assert runtime.temp.get("camp_rework_usa_release_order_accepted", 0) == 0
    assert sale.credits(runtime) == 0, "a refunded order earns no sale credit"


def run_tests():
    decision = load_decision()
    results = []

    # Verified native decision: the quoted exact support stock is accepted and
    # the release helper's measured positive output alone publishes effects.
    runtime, country, state = new_release_runtime(stock=180)
    require_available(runtime, decision)
    population_before = state["state_population_k"]
    native_click(runtime, decision)
    assert country["political_power"] == 100 - sale.price(runtime, "guard_pp"), (country["political_power"], sale.price(runtime, "guard_pp"), SALE_RATIO)
    assert sale.credits(runtime) == 1, "a kept release counts as one Political Power sale purchase"
    # One sale-priced support payment on a confirmed release.
    assert country["equipment"]["support_equipment_1"] == 180 - sale.stock(runtime, "support_equipment")
    assert state["camp_admin_detainees_k"] == 0
    assert state["camp_admin_total_released_k"] == 4
    assert country["camp_admin_total_released_k"] == 4
    assert country["arrays"]["camp_admin_history_kinds"] == [runtime.constants["camp_admin_history_kind.release"]]
    assert country["arrays"]["camp_admin_history_states"] == ["378"]
    assert state["state_population_k"] == population_before
    assert "camp_admin_census_intake_closed" in state["flags"]
    assert "camp_rework_site_reforming" in state["flags"]
    assert "camp_gui_country_action_2_cooldown" in country["flags"]
    assert country["relocation_population_disruption"] < 20
    assert country["wartime_security_reach"] == country["camp_active_site_count"] == 1
    assert country["court_challenge_pressure"] < 5
    max_pressure = runtime.constants["camp_rework_threshold.max_value"]
    for name in ("wartime_security_reach", "relocation_population_disruption", "court_challenge_pressure"):
        assert 0 <= country[name] <= max_pressure
    results.append("verified native decision: exact quote, one equipment debit, measured release, one history row, bounded relief/reform/cooldown, and derived reach equals the one active site")

    # Exercise the real USA bridge and its production clamps after relief with
    # a single site and low/zero pressure inputs.
    low_pressure, low_country, low_state = new_release_runtime(stock=180)
    low_country["relocation_population_disruption"] = 1
    low_country["court_challenge_pressure"] = 1
    low_country["wartime_security_reach"] = 0
    native_click(low_pressure, decision)
    assert low_country["relocation_population_disruption"] == 0
    assert low_country["court_challenge_pressure"] == 0
    assert low_country["wartime_security_reach"] == low_country["camp_active_site_count"] == 1
    low_max = low_pressure.constants["camp_rework_threshold.max_value"]
    for name in ("wartime_security_reach", "relocation_population_disruption", "court_challenge_pressure"):
        assert 0 <= low_country[name] <= low_max
    zero_pressure, zero_country, zero_state = new_release_runtime(stock=180)
    zero_country["relocation_population_disruption"] = 0
    zero_country["court_challenge_pressure"] = 0
    zero_country["wartime_security_reach"] = 0
    native_click(zero_pressure, decision)
    assert zero_country["relocation_population_disruption"] == 0
    assert zero_country["court_challenge_pressure"] == 0
    assert zero_country["wartime_security_reach"] == zero_country["camp_active_site_count"] == 1
    zero_max = zero_pressure.constants["camp_rework_threshold.max_value"]
    for name in ("wartime_security_reach", "relocation_population_disruption", "court_challenge_pressure"):
        assert 0 <= zero_country[name] <= zero_max
    results.append("low/zero pressure: actual USA monthly bridge restores derived one-site reach and clamps low or zero displacement/court pressure without underflow")

    # GUI action executes the same production release helper and cooldown route.
    gui, gui_country, gui_state = new_release_runtime(stock=180)
    gui.execute(gui.effects["camp_rework_gui_execute_country_action_2"], "USA")
    assert gui_country["political_power"] == 100 - sale.price(gui, "guard_pp")
    assert gui_country["equipment"]["support_equipment_1"] == 180 - sale.stock(gui, "support_equipment")
    assert gui_state["camp_admin_detainees_k"] == 0
    assert gui_country["arrays"]["camp_admin_history_kinds"] == [gui.constants["camp_admin_history_kind.release"]]
    assert "camp_gui_country_action_2_cooldown" in gui_country["flags"]
    results.append("GUI action: fresh shared availability, one GUI PP payment, same release debit/effects/history and accepted cooldown")

    # The actual GUI payment helper runs before a declared intervening cutover;
    # the production release gate rejects and the production caller refunds.
    stale_gui, stale_gui_country, stale_gui_state = new_release_runtime(stock=180)
    stale_gui.scopes["USA"]["camp_rework_action_id"] = stale_gui.constants["camp_rework_action.usa_release_detainees_under_supervision"]
    stale_gui.temp["camp_rework_action_id"] = stale_gui.constants["camp_rework_action.usa_release_detainees_under_supervision"]
    stale_gui.temp["camp_gui_political_cost"] = sale.price(stale_gui, "guard_pp")
    stale_gui.gui_cutover_hook = True
    stale_gui.run("camp_rework_gui_execute_prepared_country_action", "USA")
    assert_rejected(stale_gui, stale_gui_country, stale_gui_state)
    results.append("GUI stale click: actual payment and release helpers reject a cutover mutation, refund PP, and leave support, relief, reform, history and scripted cooldown untouched")

    # Rejected native clicks simulate the engine's up-front PP payment, then
    # change one required source input before complete_effect revalidates.
    rejected_cases = []
    for case_name, mutate, expected_support in [
        ("zero rows", lambda r, c, s: s.update(camp_admin_detainees_k=0), 180),
        ("mixed-origin ambiguity", lambda r, c, s: s["flags"].add("camp_origin_ambiguous"), 180),
        ("malformed aligned rows", lambda r, c, s: s["arrays"]["camp_admin_row_origins"].pop(), 180),
        ("capture", lambda r, c, s: s.update(controller="JAP"), 180),
        ("one-short support stock", lambda r, c, s: c["equipment"].update(support_equipment_1=sale.stock(r, "support_equipment") - 1), None),
        ("civil cutover", lambda r, c, s: c["flags"].add("camp_admin_civil_initialized"), 180),
    ]:
        runtime, country, state = new_release_runtime(stock=180)
        if case_name != "zero rows":
            assert decision_is_available(runtime, decision)
        mutate(runtime, country, state)
        if case_name == "one-short support stock":
            assert not decision_is_available(runtime, decision)
        native_click(runtime, decision)
        assert_rejected(
            runtime,
            country,
            state,
            support_before=expected_support if expected_support is not None else sale.stock(runtime, "support_equipment") - 1,
            detainees_before=0 if case_name == "zero rows" else 4,
        )
        rejected_cases.append(case_name)
    results.append("rejected native rechecks: " + ", ".join(rejected_cases) + "; each refunds the up-front PP mock and causes no resource debit, relief, reform, release history or scripted cooldown")

    # The actual AI selector walks the bounded active-site registry, discards a
    # captured first candidate, and selects the valid USA-controlled row.
    ai, ai_country, captured = new_release_runtime(stock=180, ai=True)
    valid = ai.state("377", "USA", population=10000, buildings=2)
    valid["flags"].discard("camp_rework_expanded_labor_site")
    valid.update(genocide_responsible_country="USA", camp_admin_responsible_country="USA")
    prime_existing_custody(ai, "377", 4)
    ai_country["camp_active_site_count"] = len(ai_country["arrays"]["camp_active_site_states"])
    captured["controller"] = "JAP"
    ai_country.pop("camp_selected_state_id", None)
    assert decision_is_available(ai, decision)
    native_click(ai, decision)
    assert captured["camp_admin_detainees_k"] == 4
    assert valid["camp_admin_detainees_k"] == 0
    assert ai_country["arrays"]["camp_admin_history_states"] == ["377"]
    assert ai_country["equipment"]["support_equipment_1"] == 180 - sale.stock(ai, "support_equipment")
    results.append("AI target: real production selector uses camp_active_site_states and the same site predicate; captured row is skipped")

    # Replay after a measured success cannot release or publish history twice,
    # even when the source cooldown is cleared to exercise the helper directly.
    replay, replay_country, replay_state = new_release_runtime(stock=180)
    native_click(replay, decision)
    first_release_total = replay_state["camp_admin_total_released_k"]
    first_history_count = len(replay_country["arrays"]["camp_admin_history_kinds"])
    first_relief = replay_country["relocation_population_disruption"]
    replay_country["flags"].discard("camp_gui_country_action_2_cooldown")
    replay_country["equipment"]["support_equipment_1"] = 180
    replay_country["political_power"] = 100
    native_click(replay, decision)
    assert replay_country["political_power"] == 100
    assert replay_country["equipment"]["support_equipment_1"] == 180
    assert replay_state["camp_admin_total_released_k"] == first_release_total == 4
    assert len(replay_country["arrays"]["camp_admin_history_kinds"]) == first_history_count == 1
    assert replay_country["relocation_population_disruption"] == first_relief
    assert "camp_gui_country_action_2_cooldown" not in replay_country["flags"]
    results.append("replay: production helper refuses zero rows and cannot repeat equipment payment, relief, release history, reform receipt or cooldown")

    return results


if __name__ == "__main__":
    checks = {}
    for ratio in sale.SALE_RATIOS:
        SALE_RATIO = ratio
        checks[f"payment_ratio_{ratio}"] = run_tests()
    source_hashes = {
        relative: hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        for relative in SOURCE_PATHS
    }
    print(json.dumps({
        "status": "passed",
        "evidence_type": "source-level production-helper interpreter with engine primitives mocked",
        "source_scenarios": checks,
        "source_sha256": source_hashes,
        "sale_ratios": list(sale.SALE_RATIOS),
        "limits": "No HOI4 engine, live save, probability service, GUI renderer, or campaign state was executed. Random selection chose the first candidate as a deterministic primitive mock. Native PP prepayment and the GUI cutover interleaving are explicit test inputs."
    }, indent=2))
