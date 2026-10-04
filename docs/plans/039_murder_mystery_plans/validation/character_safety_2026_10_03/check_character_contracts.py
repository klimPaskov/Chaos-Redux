"""Read-only source-contract checks. No Clausewitz engine behavior is simulated."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[5]


def source(path):
    return (ROOT / path).read_text(encoding="utf-8-sig")


def body(text, name):
    match = re.search(r"(?m)^" + re.escape(name) + r"\s*=\s*\{", text)
    assert match, name
    depth = 1
    for end in range(match.end(), len(text)):
        depth += (text[end] == "{") - (text[end] == "}")
        if not depth:
            return text[match.end():end]
    raise AssertionError(name)


runtime = source("common/scripted_effects/039_murder_mystery_runtime_effects.txt")
integration = source("common/scripted_effects/039_murder_mystery_integration_effects.txt")
character = source("common/scripted_effects/039_murder_mystery_character_effects.txt")
triggers = source("common/scripted_triggers/039_murder_mystery_runtime_triggers.txt")

registration = body(runtime, "murder_mystery_register_safe_target")
assert registration.count("is_character = event_target:murder_mystery_target_registration_character") == 2
assert "event_target:murder_mystery_target_registration_character = { exists = yes }" not in registration

validation = body(runtime, "murder_mystery_validate_selected_target")
assert "save_event_target_as = murder_mystery_target_validation_actor" in validation
assert "tag = event_target:murder_mystery_target_validation_actor" in validation
assert "tag = ROOT" not in validation and "ROOT =" not in validation
assert "clear_global_event_target = murder_mystery_selected_target_character" in validation
for term in ["selected_target_used", "selected_target_generation", "selected_target_expected_generation"]:
    assert "murder_mystery_" + term in validation
assert "add_to_temp_variable = { murder_mystery_target_registry_match" in validation
assert "murder_mystery_target_registry_match value = constant:murder_mystery_value.one compare = equals" in validation
assert "first_knife_target_id" in validation and "murder_mystery_selected_character_is_recruited = yes" in validation
assert "murder_mystery_selected_target_protected" in validation
assert "murder_mystery_target_disposition.permanently_protected" in validation
assert "murder_mystery_target_disposition.owner_managed" in validation

for predicate in ["murder_mystery_selected_target_allows_named_action", "murder_mystery_selected_target_allows_opening_action"]:
    assert "murder_mystery_selected_character_is_recruited = yes" in body(triggers, predicate)
assert "selected_target_expected_generation" in body(triggers, "murder_mystery_selected_target_is_registered")
assert "maximum_target_rows compare = less_than_or_equals" in body(triggers, "murder_mystery_target_registry_is_aligned")
assert "murder_mystery_selected_target_is_core_offender" not in body(runtime, "murder_mystery_prepare_safe_target_action")
assert "clr_country_flag = murder_mystery_selected_target_is_core_offender" in body(runtime, "murder_mystery_clear_selected_target_context")

anchor = body(character, "murder_mystery_capture_current_ruling_character")
assert "murder_mystery_ruling_selection_authorized" in anchor
assert anchor.index("add_country_leader_trait") < anchor.index("every_character") < anchor.index("remove_country_leader_trait")
assert "random_character" not in anchor and "retire =" not in anchor
assert "matches value = constant:murder_mystery_value.one compare = equals" in anchor
creation = body(integration, "murder_mystery_create_assassin_state_candidate")
assert "is_country_leader = yes" not in creation
founder = body(character, "murder_mystery_register_candidate_founder")
assert "murder_mystery_capture_current_ruling_character = yes" in founder
assert "murder_mystery_register_safe_target = yes" in founder
commit = body(integration, "murder_mystery_commit_assassin_state_creation")
assert commit.index("murder_mystery_assassin_state_transfer_applied") < commit.index("murder_mystery_register_candidate_founder = yes")
assert "has_country_flag = murder_mystery_first_knife_registered" in commit
assert "has_country_flag = murder_mystery_ruling_character_resolved" in commit
before_transfer = commit[:commit.index("murder_mystery_transfer_split_states_to_assassin_state = yes")]
assert "event_target:murder_mystery_assassin_state_candidate = { exists = yes }" not in before_transfer
assert "murder_mystery_assassin_candidate_is_reserved = yes" in before_transfer
begin = body(runtime, "murder_mystery_begin_assassin_state_transaction")
assert "event_target:murder_mystery_assassin_state_candidate = { exists = yes }" not in begin
assert "murder_mystery_assassin_candidate_is_reserved = yes" in begin
assert "set_capital" not in creation
assert commit.index("murder_mystery_assassin_state_transfer_applied") < commit.index("set_capital")
reconciliation = body(runtime, "murder_mystery_reconcile_target_registry")
assert re.search(r"limit\s*=\s*\{\s*OR\s*=\s*\{\s*check_variable\s*=\s*\{\s*var = murder_mystery_target_registry_row_id", reconciliation)

selector = body(integration, "murder_mystery_select_operation_target")
assert "murder_mystery_baseline_core_target_id" in selector
assert "murder_mystery_baseline_core_target_generation" in selector
assert "murder_mystery_territorial_state_ever_created" in selector
assert "NOT = { has_global_flag = murder_mystery_core_capture_committed }" in selector
assert "ROOT.murder_mystery_operation_target_id" not in selector
resolution = body(integration, "murder_mystery_apply_safe_target_resolution")
assert "exists = yes has_character_flag" not in resolution
assert resolution.index("murder_mystery_install_movement_successor = yes") < resolution.index("retire = yes")
assert "murder_mystery_selected_character_is_recruited = yes" in resolution
assert "set_global_flag = murder_mystery_core_capture_committed" in resolution

shock = body(character, "murder_mystery_apply_live_central_capture_shock")
for forbidden in ["retire", "declare_war_on", "cleanup_runtime", "finalize_runtime", "every_country", "inheritance_transaction"]:
    assert forbidden not in shock
assert "num_of_owned_states > constant:murder_mystery_value.zero" in shock
assert "murder_mystery_capture_shock_applied" in shock
assert "constant:murder_mystery_capture_shock.cohesion_ratio" in shock
outcome = body(integration, "murder_mystery_resolve_investigation_outcome")
assert "murder_mystery_apply_live_central_capture_shock = yes" in outcome
assert "NOT = { has_country_flag = murder_mystery_live_central_after_capture }" in outcome
assert outcome.count("murder_mystery_apply_live_central_capture_shock = yes") == 2

print("PASS: owner-local receipts, recruited-roster checks, used/generation rejection, bounded rows, exact-ruler selection, immutable baseline, successor-before-retire, core tombstone and live-central continuation source contracts.")
print("LIMIT: no engine execution, roster/route approval, probability, inheritance, persistence or Part18 acceptance is inferred.")
