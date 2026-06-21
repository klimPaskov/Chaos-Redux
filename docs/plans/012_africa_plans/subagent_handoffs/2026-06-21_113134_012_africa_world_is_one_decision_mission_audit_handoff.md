# Event 012 Africa World Is One Decision/Mission Audit Handoff

Date: 2026-06-21 11:31 UTC

Mode: patched small local issue after bounded audit.

## Scope

Audited the ordinary World Is One proof chain only:

- four external continent-unifier timed proof decisions
- continent-unifier certification decision
- World Is One gate-preparation decision
- `AFR_the_world_is_one` final focus gate

The direct manual `SCN-008 World Is One` terminal helper was treated as out of scope except where it could confuse ordinary-route documentation.

## Changed Files

- `common/scripted_localisation/012_africa_scripted_localisation.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/plans/012_africa_plans/2026-06-20_targeted_scenario_validation_matrix.md`

## Changed IDs and Helpers

- Scripted localisation:
  - `GetAfricaExternalProofStatus`
- Localisation:
  - added `africa_external_proof_status.awaiting_external_mandates`
- Documentation:
  - normal-route World Is One validation matrix wording for external proof audits

No decision IDs, mission IDs, scripted effects, scripted triggers, focus IDs, assets, or workbook rows were changed.

## Issue List

1. Medium: `GetAfricaExternalProofStatus` displayed `All proofs verified` from the stored `africa_external_continent_unifier_proofs_ready` country flag even if the validated gate trigger `has_africa_external_continent_unifier_proofs_ready` would fail because an external mandate flag or proof component was no longer valid.
2. Low: the validation matrix called the four external proof timers "missions" even though the implementation uses timed decisions with `days_remove`, `remove_effect`, and `cancel_trigger`, not `days_mission_timeout`.

No high-severity ordinary-gate exploit was found statically.

## Before and After Behavior

Before:

- The actual certification, preparation, and final focus gates already required the validated `has_africa_external_continent_unifier_proofs_ready = yes` path.
- The sponsor category header could still show `All proofs verified` from a stale stored ready flag even when the ordinary World Is One gate would correctly block.
- The matrix blurred timed proof decisions with missions.

After:

- `GetAfricaExternalProofStatus` shows `All proofs verified` only when `has_africa_external_continent_unifier_proofs_ready = yes` passes.
- If the stored proof-ready flag exists but the validated proof trigger fails, the status shows `Awaiting external mandates`.
- The validation matrix now calls the four route checks timed proof decisions/audits.

## Category Lifecycle Notes

`africa_continent_sponsor_category` is visible once `africa_continent_sponsor_office_open` is set. The ordinary World Is One chain then progresses through sponsor readiness, cross-continent charters, dynamic union proclamation, proof ledger, certification, preparation, and final focus.

The four external proof timers are revalidated at start and at timer removal. The preparation decision sets only `africa_world_is_one_gate_prepared`; it does not start the terminal branch. `AFR_the_world_is_one` remains the only ordinary-route terminal starter and calls `africa_mark_world_is_one_gate_ready`, which is guarded by `can_africa_start_world_is_one_gate`.

## Mission Quality Notes

| Surface | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate Risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `africa_verify_middle_east_unifier_proof` | Africa unifier | `africa_continent_sponsor_category` | Middle East | sponsored charter, dynamic union, proof ledger, external mandate, no world-end, costs | `constant:africa_decision_days.external_unifier_proof` | records Middle East proof and refreshes proof count | failure pressure if route invalidates before timer ends | Low |
| `africa_verify_asia_unifier_proof` | Africa unifier | `africa_continent_sponsor_category` | Asia | sponsored charter, dynamic union, proof ledger, external mandate, no world-end, costs | same timed audit duration | records Asia proof and refreshes proof count | failure pressure if route invalidates before timer ends | Low |
| `africa_verify_europe_unifier_proof` | Africa unifier | `africa_continent_sponsor_category` | Europe | sponsored charter, World Root, dynamic union, proof ledger, external mandate, no world-end, costs | same timed audit duration | records Europe proof and refreshes proof count | failure pressure if route invalidates before timer ends | Low |
| `africa_verify_south_atlantic_unifier_proof` | Africa unifier | `africa_continent_sponsor_category` | South Atlantic | sponsored charter, Pan-Atlantic Congress, dynamic union, proof ledger, external mandate, no world-end, costs | same timed audit duration | records South Atlantic proof and refreshes proof count | failure pressure if route invalidates before timer ends | Low |

These are timed decisions, not HOI4 missions. The identical proof duration is acceptable for this narrow audit because the four regions vary by route prerequisites and resource costs; broader pacing variety can remain a balance follow-up if live proof shows sameness feels flat.

## Cost and Requirement Clarity Notes

- Custom cost text matches the click-time triggers and spend effects for the four proof audits, certification, and gate preparation.
- Certification and gate preparation repeat their prerequisite and resource checks inside `complete_effect`, so stale UI availability cannot spend resources or set readiness markers after invalidation.
- The patched proof status text now matches validated gate behavior.

## AI Validity and Route-Lock Notes

- AI weights are bounded by decision availability and route-ready modifiers.
- The proof audit decisions cannot be completed unless the matching route-ready trigger and resource gate pass.
- The final focus AI still reads `can_africa_start_world_is_one_gate = yes`; the focus completion reward also calls a guarded helper, so loss of prerequisites during focus progress does not set terminal flags.

## Cleanup and Exploit-Risk Notes

- Stale active proof timers fail closed because `cancel_trigger` and `remove_effect` both recheck the matching `can_africa_keep_*_unifier_proof_active` trigger.
- Stale external proof-ready flags do not advance the gate because `has_africa_external_continent_unifier_proofs_ready` requires all four proof flags, the proof counter, runtime context, and all four external world-end readiness flags.
- Stale `africa_world_is_one_gate_prepared` does not advance the gate by itself because `can_africa_start_world_is_one_gate` revalidates `can_africa_prepare_world_is_one_gate`.
- No free unit, equipment farming, war-goal spam, core spam, or repeatable reward loop was found in this bounded chain.

## Validation Performed

- Reconciled `available`, `custom_cost_trigger`, `complete_effect`, `remove_effect`, `cancel_trigger`, `can_africa_*` triggers, and `AFR_the_world_is_one` completion logic for the ordinary chain.
- Checked that `GetAfricaExternalProofStatus` now uses the same validated proof trigger as the gate display.
- Confirmed the new localisation key is referenced and `localisation/english/012_african_union_l_english.yml` still begins with UTF-8 BOM.
- Ran scoped diff whitespace validation on the three touched files.

## Skipped Validation

- No live in-game proof was run. The existing validation matrix still correctly marks live proof pending for all ordinary-route World Is One gates.
- No workbook edit was made; the task explicitly excluded workbook changes.

## Remaining Blockers and Follow-Up

- Live proof remains required for the four timed proof audits, certification, gate preparation, and `AFR_the_world_is_one`.
- If live proof shows the four 75-day proof timers feel too uniform, vary `constant:africa_decision_days.external_unifier_proof` into region-specific durations in a later balance pass. That is a balance-depth follow-up, not a static gate safety blocker.
