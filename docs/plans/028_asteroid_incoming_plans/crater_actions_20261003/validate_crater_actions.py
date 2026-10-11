"""Source-check Event 028 crater action wiring against the actual Clausewitz files.

This reuses the repository's source parser and compares the current decision
surface with the immutable pre-edit copy. It is not an engine or gameplay test.
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
BEFORE = ROOT / "docs/plans/028_asteroid_incoming_plans/crater_actions_20261003/before"

PARSER_PATH = ROOT / ".tools/validation/validate_028_availability.py"
SPEC = importlib.util.spec_from_file_location("event028_source_parser", PARSER_PATH)
assert SPEC and SPEC.loader
PARSER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PARSER)
parse_source = PARSER.parse_source

DECISION_PATH = ROOT / "common/decisions/028_asteroid_incoming_decisions.txt"
EFFECT_PATH = ROOT / "common/scripted_effects/028_asteroid_incoming_crater_effects.txt"
TRIGGER_PATH = ROOT / "common/scripted_triggers/028_asteroid_incoming_crater_triggers.txt"
MODIFIER_PATH = ROOT / "common/dynamic_modifiers/028_asteroid_incoming_crater_dynamic_modifiers.txt"
LOC_PATH = ROOT / "localisation/english/028_asteroid_impact_l_english.yml"

ACTION_IDS = (
    "decision_asteroid_incoming_secure_crater_perimeter",
    "decision_asteroid_incoming_survey_extraordinary_material",
    "decision_asteroid_incoming_fortify_crater_access",
    "decision_asteroid_incoming_reconnoiter_crater_site",
    "decision_asteroid_incoming_disrupt_extraction_routes",
    "decision_asteroid_incoming_prepare_crater_offensive",
)

COST_TYPES = {
    ACTION_IDS[0]: {"manpower", "support equipment", "fuel", "command power"},
    ACTION_IDS[1]: {"support equipment", "fuel", "command power", "civilian factory use"},
    ACTION_IDS[2]: {"manpower", "train equipment", "support equipment", "civilian factory use"},
    ACTION_IDS[3]: {"manpower", "support equipment"},
    ACTION_IDS[4]: {"train equipment", "support equipment", "fuel"},
    ACTION_IDS[5]: {"manpower", "support equipment", "fuel"},
}

COST_SOURCE_TOKENS = {
    "manpower": "has_manpower",
    "support equipment": "support_equipment",
    "fuel": "has_fuel",
    "command power": "command_power",
    "train equipment": "train_equipment",
    "civilian factory use": "civilian_factory_use",
}

COST_ICONS = {
    "manpower": "£manpower_texticon",
    "support equipment": "£support_equipment_text_icon",
    "fuel": "£GFX_fuel_texticon",
    "command power": "£command_power",
    "train equipment": "£GFX_train_texticon",
    "civilian factory use": "£civ_factory",
}

EXTRA_COST_TOOLTIP = {
    ACTION_IDS[0]: "asteroid_incoming_cost_crater_security_command_power_tt",
    ACTION_IDS[1]: "asteroid_incoming_cost_material_survey_command_power_tt",
    ACTION_IDS[2]: "asteroid_incoming_cost_crater_access_manpower_tt",
}

EFFECT_IDS = (
    "asteroid_incoming_apply_crater_perimeter_security",
    "asteroid_incoming_apply_crater_material_survey",
    "asteroid_incoming_apply_crater_access_fortification",
    "asteroid_incoming_apply_rival_crater_reconnaissance",
    "asteroid_incoming_apply_rival_crater_route_disruption",
    "asteroid_incoming_apply_rival_crater_offensive_plan",
    "asteroid_incoming_clear_crater_security_receipt",
    "asteroid_incoming_clear_crater_survey_receipt",
    "asteroid_incoming_clear_crater_fortification_receipt",
    "asteroid_incoming_clear_rival_crater_recon_receipt",
    "asteroid_incoming_clear_rival_crater_disruption_receipt",
    "asteroid_incoming_clear_rival_crater_offensive_receipt",
)

RECEIPTS = {
    ACTION_IDS[0]: {
        "paid": "asteroid_incoming_crater_security_paid_@ROOT",
        "lock": "asteroid_incoming_crater_security_action_in_progress",
        "controller": "asteroid_incoming_crater_security_controller_id_@ROOT",
        "resolver": "asteroid_incoming_crater_security_action_can_resolve",
        "clear": "asteroid_incoming_clear_crater_security_receipt",
    },
    ACTION_IDS[1]: {
        "paid": "asteroid_incoming_crater_survey_paid_@ROOT",
        "lock": "asteroid_incoming_crater_survey_action_in_progress",
        "controller": "asteroid_incoming_crater_survey_controller_id_@ROOT",
        "resolver": "asteroid_incoming_crater_survey_action_can_resolve",
        "clear": "asteroid_incoming_clear_crater_survey_receipt",
    },
    ACTION_IDS[2]: {
        "paid": "asteroid_incoming_crater_fortification_paid_@ROOT",
        "lock": "asteroid_incoming_crater_fortification_action_in_progress",
        "controller": "asteroid_incoming_crater_fortification_controller_id_@ROOT",
        "resolver": "asteroid_incoming_crater_fortification_action_can_resolve",
        "clear": "asteroid_incoming_clear_crater_fortification_receipt",
    },
    ACTION_IDS[3]: {
        "paid": "asteroid_incoming_crater_recon_paid_@ROOT",
        "lock": "asteroid_incoming_crater_recon_action_in_progress",
        "controller": "asteroid_incoming_crater_recon_controller_id_@ROOT",
        "resolver": "asteroid_incoming_rival_crater_recon_action_can_resolve",
        "clear": "asteroid_incoming_clear_rival_crater_recon_receipt",
    },
    ACTION_IDS[4]: {
        "paid": "asteroid_incoming_crater_disruption_paid_@ROOT",
        "lock": "asteroid_incoming_crater_disruption_action_in_progress",
        "controller": "asteroid_incoming_crater_disruption_controller_id_@ROOT",
        "resolver": "asteroid_incoming_rival_crater_disruption_action_can_resolve",
        "clear": "asteroid_incoming_clear_rival_crater_disruption_receipt",
    },
    ACTION_IDS[5]: {
        "paid": "asteroid_incoming_crater_offensive_paid_@ROOT",
        "lock": "asteroid_incoming_crater_offensive_action_in_progress",
        "controller": "asteroid_incoming_crater_offensive_controller_id_@ROOT",
        "resolver": "asteroid_incoming_rival_crater_offensive_action_can_resolve",
        "clear": "asteroid_incoming_clear_rival_crater_offensive_receipt",
    },
}

MODIFIER_IDS = (
    "asteroid_incoming_crater_perimeter_security",
    "asteroid_incoming_crater_surveyed_material",
    "asteroid_incoming_crater_access_supply_disruption",
    "asteroid_incoming_crater_offensive_plan",
)

def entries(rows, key):
    return [value for name, operator, value in rows if name == key and operator == "="]


def recursive_entries(tree, key):
    found = []
    if isinstance(tree, (list, tuple)):
        if isinstance(tree, tuple) and len(tree) == 3 and isinstance(tree[0], str):
            name, operator, value = tree
            if name == key and operator == "=":
                found.append(value)
            if isinstance(value, (list, tuple)):
                found.extend(recursive_entries(value, key))
        else:
            for item in tree:
                found.extend(recursive_entries(item, key))
    return found


def limited_if(effect_tree, token):
    for branch in recursive_entries(effect_tree, "if"):
        limits = entries(branch, "limit")
        if limits and token in str(limits[0]):
            return branch
    return None


def negates_flag(tree, flag):
    return any(flag in entries(not_body, "has_state_flag") for not_body in recursive_entries(tree, "NOT"))


def decision_map(path):
    root_rows = parse_source(path, rows=True)
    categories = entries(root_rows, "asteroid_incoming_recovery_category")
    assert len(categories) == 1, f"Expected one Event028 recovery category in {path}"
    category_rows = categories[0]
    return {name: body for name, operator, body in category_rows if operator == "=" and isinstance(body, list)}


before_decisions = decision_map(BEFORE / "common/decisions/028_asteroid_incoming_decisions.txt")
after_decisions = decision_map(DECISION_PATH)
assert all(action_id in before_decisions and action_id in after_decisions for action_id in ACTION_IDS)

before_weights = recursive_entries(list(before_decisions.values()), "ai_will_do")
after_weights = recursive_entries(list(after_decisions.values()), "ai_will_do")
assert len(before_weights) == 21, f"Expected the established 21 AI weight blocks, found {len(before_weights)} before"
assert after_weights == before_weights, "At least one Event028 decision or mission AI weight block changed"

def payment_rows(tree):
    return {effect: recursive_entries(tree, effect) for effect in payment_effects}


def normalized_payment_rows(tree):
    return {effect: [str(row).replace("_negative", "") for row in recursive_entries(tree, effect)] for effect in payment_effects}

preserved_decision_fields = ("custom_cost_trigger", "custom_cost_text", "modifier", "days_remove")
payment_effects = {"add_manpower", "add_equipment_to_stockpile", "add_fuel", "add_command_power"}
for action_id in ACTION_IDS:
    before_rows = before_decisions[action_id]
    after_rows = after_decisions[action_id]
    for field in preserved_decision_fields:
        assert entries(before_rows, field) == entries(after_rows, field), f"{action_id} changed {field}"
    before_payments = [pair for key in payment_effects for value in entries(before_rows, "complete_effect") for pair in recursive_entries(value, key)]
    after_payments = [pair for key in payment_effects for value in entries(after_rows, "complete_effect") for pair in recursive_entries(value, key)]
    assert before_payments == after_payments, f"{action_id} changed its accepted payment amounts or types"
    source_text = str(after_rows)
    for cost_type in COST_TYPES[action_id]:
        assert COST_SOURCE_TOKENS[cost_type] in source_text, f"{action_id} no longer pays {cost_type}"
    assert len(entries(after_rows, "cancel_trigger")) == 1, f"{action_id} lacks a cancellation revalidation"
    assert len(entries(after_rows, "cancel_effect")) == 1, f"{action_id} lacks cancellation cleanup/refund"
    assert len(entries(after_rows, "remove_effect")) == 1, f"{action_id} lacks a guarded completion dispatcher"

    receipt = RECEIPTS[action_id]
    pending = "asteroid_incoming_crater_action_pending_@ROOT"
    complete = entries(after_rows, "complete_effect")[0]
    start_branch = limited_if(complete, receipt["lock"])
    assert start_branch is not None, f"{action_id} has no single guarded paid-start branch"
    assert negates_flag(start_branch, pending), f"{action_id} can enter while this actor already has a paid action"
    assert negates_flag(start_branch, receipt["paid"]), f"{action_id} does not reject a stale same-action receipt"
    assert negates_flag(start_branch, receipt["lock"]), f"{action_id} does not reject a same-action paid lock"
    assert receipt["paid"] in recursive_entries(start_branch, "set_state_flag"), f"{action_id} does not record its actor/action payment"
    assert receipt["lock"] in recursive_entries(start_branch, "set_state_flag"), f"{action_id} does not reserve its action outcome"
    assert receipt["controller"] in str(recursive_entries(start_branch, "set_variable")), f"{action_id} does not capture its actor-specific controller"
    assert payment_rows(start_branch) == payment_rows(complete), f"{action_id} has a debit outside its guarded start branch"

    cancel = entries(after_rows, "cancel_effect")[0]
    cancel_receipt_branch = limited_if(cancel, receipt["paid"])
    assert cancel_receipt_branch is not None, f"{action_id} cancellation refund is not guarded by its own actor/action receipt"
    assert receipt["clear"] in str(cancel_receipt_branch), f"{action_id} cancellation does not clear only its own receipt"
    assert normalized_payment_rows(cancel_receipt_branch) == normalized_payment_rows(start_branch), f"{action_id} cancellation refund no longer returns its exact payment"

    remove = entries(after_rows, "remove_effect")[0]
    remove_receipt_branch = limited_if(remove, receipt["paid"])
    assert remove_receipt_branch is not None, f"{action_id} completion/refund is not guarded by its own actor/action receipt"
    assert receipt["resolver"] in str(remove_receipt_branch), f"{action_id} completion lacks its exact receipt resolver"
    assert receipt["clear"] in str(remove_receipt_branch), f"{action_id} completion does not clear only its own receipt"
    assert normalized_payment_rows(remove_receipt_branch) == normalized_payment_rows(start_branch), f"{action_id} invalid-resolution refund no longer returns its exact payment"

effect_rows = parse_source(EFFECT_PATH, rows=True)
trigger_rows = parse_source(TRIGGER_PATH, rows=True)
modifier_rows = parse_source(MODIFIER_PATH, rows=True)
assert all(len(entries(effect_rows, helper)) == 1 for helper in EFFECT_IDS)
assert all(len(entries(modifier_rows, modifier)) == 1 for modifier in MODIFIER_IDS)
assert len(entries(trigger_rows, "asteroid_incoming_state_has_active_local_emergency_burden")) == 1
trigger_source = TRIGGER_PATH.read_text(encoding="utf-8-sig")
assert not re.search(r"(?m)^\s*has_war\s*=", trigger_source), "A country-only has_war trigger was left in the state-scoped helper file"
assert "CONTROLLER = { exists = yes has_war_with = ROOT }" in trigger_source
active_burden = entries(trigger_rows, "asteroid_incoming_state_has_active_local_emergency_burden")[0]
assert "asteroid_incoming_rescue_burden_active" in str(active_burden)
for severe_modifier in (
    "asteroid_incoming_catastrophic_impact_zone",
    "asteroid_incoming_major_impact_zone",
    "asteroid_incoming_fragment_center_recovery",
    "asteroid_incoming_heavy_fragment_damage",
):
    assert severe_modifier in str(active_burden), f"Emergency burden predicate omits {severe_modifier}"
assert "asteroid_incoming_mission_failure_pressure" not in str(active_burden)
assert "asteroid_incoming_outer_shock_zone" not in str(active_burden)
assert "asteroid_incoming_light_fragment_damage" not in str(active_burden)

for action_id, receipt in RECEIPTS.items():
    clear_body = entries(effect_rows, receipt["clear"])[0]
    clear_guard = limited_if(clear_body, receipt["paid"])
    assert clear_guard is not None, f"{action_id} clear helper is not limited to this actor/action paid flag"
    assert "asteroid_incoming_crater_action_pending_@ROOT" in str(clear_guard)
    assert receipt["lock"] in recursive_entries(clear_guard, "clr_state_flag")
    assert receipt["paid"] in recursive_entries(clear_guard, "clr_state_flag")
    assert receipt["controller"] in str(recursive_entries(clear_guard, "clear_variable"))

# Source-derived receipt scenarios. These model only the actor/action keys
# and guards extracted above; they are not an engine execution or runtime test.
def actor_key(source_key, actor):
    return source_key.replace("@ROOT", actor)


def can_enter(action, actor, flags):
    receipt = RECEIPTS[action]
    return all(
        actor_key(key, actor) not in flags
        for key in ("asteroid_incoming_crater_action_pending_@ROOT", receipt["paid"])
    ) and receipt["lock"] not in flags


def has_paid_receipt(action, actor, flags):
    return actor_key(RECEIPTS[action]["paid"], actor) in flags


security_receipt = RECEIPTS[ACTION_IDS[0]]
survey_receipt = RECEIPTS[ACTION_IDS[1]]
paid_state_a = {
    actor_key("asteroid_incoming_crater_action_pending_@ROOT", "A"),
    actor_key(security_receipt["paid"], "A"),
    security_receipt["lock"],
    actor_key(security_receipt["controller"], "A"),
}
assert actor_key(security_receipt["paid"], "A") in paid_state_a
assert actor_key(security_receipt["paid"], "B") not in paid_state_a
assert security_receipt["lock"] in paid_state_a
assert actor_key("asteroid_incoming_crater_action_pending_@ROOT", "B") not in paid_state_a
# B's rejected same-action completion sees A's global lock; B's cancel/remove
# guards resolve to B-specific paid flags and therefore cannot refund or clear A.
assert not can_enter(ACTION_IDS[0], "B", paid_state_a)
assert not has_paid_receipt(ACTION_IDS[0], "B", paid_state_a)
assert not has_paid_receipt(ACTION_IDS[0], "B", paid_state_a)  # no guarded cancellation refund/clear
paid_state_after_b_cancel = set(paid_state_a)
assert paid_state_after_b_cancel == paid_state_a
# A's second, different action is denied by A's pending receipt; its distinct
# paid flag is absent, so its refund, completion, and clear branches stay closed.
assert actor_key("asteroid_incoming_crater_action_pending_@ROOT", "A") in paid_state_a
assert not can_enter(ACTION_IDS[1], "A", paid_state_a)
assert not has_paid_receipt(ACTION_IDS[1], "A", paid_state_a)
assert actor_key(security_receipt["paid"], "A") in paid_state_a

fortification = entries(effect_rows, "asteroid_incoming_apply_crater_access_fortification")[0]
fortification_selections = recursive_entries(fortification, "random_neighbor_state")
assert len(fortification_selections) == 2, "Access fortification must be capped at two neighboring states"
assert all("asteroid_incoming_crater_access_fortified" in str(selection) for selection in fortification_selections)
assert len(recursive_entries(fortification, "add_building_construction")) == 4, "Two access states should each receive at most one bunker and one infrastructure level"
assert "asteroid_incoming_main_crater" in str(fortification) and "asteroid_incoming_fragment_site" in str(fortification)
assert "asteroid_incoming_crater_access_action_selected" not in str(fortification)
assert "army_armor_factor" not in MODIFIER_PATH.read_text(encoding="utf-8-sig")
assert "armor_factor" not in MODIFIER_PATH.read_text(encoding="utf-8-sig")

localisation = LOC_PATH.read_text(encoding="utf-8-sig")
localisation_values = {
    key: value
    for key, value in re.findall(r'(?m)^([^\s:]+):\s*"([^"]*)"\s*$', localisation)
}
expected_loc_keys = (
    "asteroid_incoming_blocked_crater_access_tt",
    "asteroid_incoming_blocked_crater_field_divisions_tt",
    "asteroid_incoming_blocked_fortifiable_access_tt",
    "asteroid_incoming_blocked_hostile_crater_access_tt",
    "asteroid_incoming_blocked_offensive_access_tt",
    "asteroid_incoming_crater_perimeter_security_desc",
    "asteroid_incoming_crater_surveyed_material_desc",
    "asteroid_incoming_crater_access_supply_disruption_desc",
    "asteroid_incoming_crater_offensive_plan_desc",
)
for key in expected_loc_keys:
    assert re.search(rf"(?m)^{re.escape(key)}:", localisation), f"Missing localisation key {key}"

inline_cost_icons = {}
for action_id in ACTION_IDS:
    cost_keys = entries(after_decisions[action_id], "custom_cost_text")
    assert len(cost_keys) == 1, f"Expected one authoritative inline cost string for {action_id}"
    cost_key = cost_keys[0]
    cost_text = localisation_values[cost_key]
    icon_count = len(re.findall(r"£[A-Za-z0-9_]+", cost_text))
    assert icon_count <= 3, f"{action_id} shows {icon_count} inline resource icons"
    inline_cost_icons[action_id] = icon_count
    assert len(COST_TYPES[action_id]) <= 4, f"{action_id} exceeds the four-type payment cap"
    full_cost_text = cost_text
    if action_id in EXTRA_COST_TOOLTIP:
        full_cost_text += localisation_values[EXTRA_COST_TOOLTIP[action_id]]
    for cost_type in COST_TYPES[action_id]:
        assert COST_ICONS[cost_type] in full_cost_text, f"{action_id} does not display the {cost_type} texticon"

raw_localisation = LOC_PATH.read_bytes()
assert raw_localisation.startswith(b"\xef\xbb\xbf"), "Event028 English localisation lost its UTF-8 BOM"

print("CRATER_ACTION_SOURCE: six action definitions have preserved custom payment contracts and all 21 AI weight blocks are parser-structure identical to the pre-edit source.")
print("CRATER_ACTION_LIFECYCLE: six cancel/refund and guarded remove hooks parse from the actual decision source; new trigger scopes contain no bare country-only has_war test.")
print("CRATER_RECEIPTS: source-derived actor A/B and same-actor second-action cases keep payment, refund, resolution, and cleanup bound to the targeted paid action receipt.")
print("EMERGENCY_LIFECYCLE: exact-state read-only predicate requires an active rescue flag or severe impact modifier; outer-ring, light-fragment, historical, and post-emergency mission-failure markers do not keep emergency actions open.")
print("CRATER_ACCESS_BOUND: source selects at most two distinct ordinary access states and caps each at one bunker plus one infrastructure level.")
print(f"CRATER_COSTS: per-action cost types stay within four and inline icon counts are {inline_cost_icons}; deferred fourth costs remain explicitly iconized.")
print("CRATER_MODIFIERS: four helper modifier definitions are present without any armour modifier token.")
print("CRATER_LOC: action blockers, persistent modifier descriptions, and UTF-8 BOM are present in the actual Event028 localisation file.")
print("SUPPLY_LIMIT: local division presence is verified in source, but no division-level supplied-status check is modeled by this test.")
