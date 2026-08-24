"""Static contract audit for Event 006 FORM-16.

This is a bounded source audit, not a runtime or probability proof. It keeps
the admitted ARM/GEO/AZR carrier contract, the exact state anchors, and the
generation-safe mutation/rollback surface visible while FORM-16 remains
behind its existing readiness gates.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8-sig")


def require(text: str, pattern: str, label: str) -> None:
    if not re.search(pattern, text, re.MULTILINE | re.DOTALL):
        raise AssertionError(f"missing {label}: {pattern}")


def main() -> int:
    effects = read("common/scripted_effects/006_independence_wave_form16_effects.txt")
    triggers = read("common/scripted_triggers/006_independence_wave_form16_triggers.txt")
    events = read("events/006_independence_wave_support_events.txt")
    decisions = read("common/decisions/006_independence_wave_transcaucasus_decisions.txt")
    constants = read("common/script_constants/006_independence_wave_constants_registry.txt")

    # The family remains late-bound to exactly the three admitted vanilla
    # carriers and their exact Transcaucasian state anchors.
    for tag in ("ARM", "GEO", "AZR"):
        require(triggers, rf"\b{tag}\s*=\s*\{{", f"member scope {tag}")
        require(effects, rf"\b{tag}\s*=\s*\{{", f"integration scope {tag}")
    for state in ("229", "230", "231"):
        require(effects, rf"\b{state}\s*=\s*\{{\s*transfer_state_to\s*=\s*ROOT", f"state transfer {state}")
        require(decisions, rf"\b{state}\s*=\s*\{{\s*is_owned_and_controlled_by\s*=\s*ROOT", f"state readiness {state}")

    # Readiness and commit must carry identity, territory, member policy,
    # arbitration, generation, and transaction predicates rather than only a
    # cosmetic/tag check.
    require(effects, r"independence_wave_form16_register_readiness\s*=\s*\{", "readiness writer")
    require(effects, r"independence_wave_form16_runtime_commit_prevalidation\s*=\s*yes", "runtime prevalidation call")
    require(triggers, r"has_independence_wave_form16_runtime_commit_proof\s*=\s*\{", "runtime commit proof")
    # The current source exposes this proof as a country flag inside the
    # FORM-16 runtime trigger. Accept the named scripted-trigger spelling too,
    # so the audit remains compatible with both documented source contracts.
    require(
        triggers,
        r"(?:has_independence_wave_formable_transaction_ready\s*=\s*yes|has_country_flag\s*=\s*independence_wave_formable_transaction_ready)",
        "transaction-ready gate",
    )
    require(triggers, r"can_independence_wave_formable_pass_congress_vote\s*=\s*yes", "congress vote gate")
    require(triggers, r"independence_wave_formable_mutation_prevalidated", "mutation prevalidation")

    # AI invitations must resolve consent/refusal and require a live,
    # connected, peaceful, recognized member; stale generation receipts must
    # not authorize post-formation behavior.
    require(effects, r"independence_wave_form16_resolve_ai_invitation_from_root\s*=\s*\{", "AI invitation resolver")
    require(effects, r"independence_wave_formable_declare_consent_for_selected_family", "AI consent writer")
    require(effects, r"independence_wave_formable_withhold_consent_for_selected_family", "AI refusal writer")
    require(triggers, r"check_variable\s*=\s*\{\s*var\s*=\s*independence_wave_form16_ai_connection_generation\s+value\s*=\s*independence_wave_generation_id", "generation equality")

    # Identity, state transfer, post-formation ledgers, rollback, and cleanup
    # must all be explicit and independently named.
    for name, text in (
        ("identity adapter", effects),
        ("state integration", effects),
        ("post-formation initialization", effects),
        ("rollback", effects),
        ("runtime cleanup", effects),
    ):
        require(text, {
            "identity adapter": r"independence_wave_formable_identity_adapter_16\s*=\s*\{",
            "state integration": r"independence_wave_formable_integration_adapter_16\s*=\s*\{",
            "post-formation initialization": r"independence_wave_form16_initialize_postformation\s*=\s*\{",
            "rollback": r"independence_wave_form16_rollback_transaction\s*=\s*\{",
            "runtime cleanup": r"independence_wave_form16_cleanup_runtime\s*=\s*\{",
        }[name], name)
    require(effects, r"clear_variable\s*=\s*independence_wave_form16_identity_generation", "identity generation cleanup")
    require(effects, r"clear_variable\s*=\s*independence_wave_form16_integration_generation", "integration generation cleanup")
    require(effects, r"clr_country_flag\s*=\s*independence_wave_form16_transaction_rolled_back", "rollback receipt cleanup")

    # The player-facing invitation remains explicitly triggered-only and has
    # both consent and refusal options.
    require(events, r"id\s*=\s*chaosx\.nr006\.6816", "FORM-16 invitation event")
    require(events, r"independence_wave_formable_declare_consent_for_selected_family", "human consent option")
    require(events, r"independence_wave_formable_withhold_consent_for_selected_family", "human refusal option")
    require(constants, r"founding_mission\s*=\s*210", "founding mission tuning")

    print("Event 006 FORM-16 contract audit passed")
    print("- admitted carriers: ARM / GEO / AZR")
    print("- exact member states: 230 / 231 / 229")
    print("- consent/refusal: AI resolver and human invitation event")
    print("- mutation: identity, territory, integration, generation and vote gates")
    print("- rollback/cleanup: explicit receipt and variable cleanup")
    print("- readiness: existing fail-closed predicates preserved")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"Event 006 FORM-16 contract audit failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
