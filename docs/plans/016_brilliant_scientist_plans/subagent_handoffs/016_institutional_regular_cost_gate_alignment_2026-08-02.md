# Event 016 Institutional Regular-Cost Gate Alignment Handoff

Date: 2026-08-02

## Status

Patched one bounded availability defect in the committed Directorate Institutions governance tranche.

No commit was created or staged.

No models, assets, GUI, event chain, focus, category, constants, scripted helper, or localisation files were changed.

## Issue list

### Medium, fixed: five governance actions rejected the exact political power shown as their cost

The five new timed governance decisions each use a regular `cost = constant:...` political-power cost.

Their `available` blocks also used `has_political_power >` with the exact same cost constant.

The strict comparison made an action unavailable at exactly its displayed cost despite the engine's regular decision-cost gate being able to pay that amount.

The redundant strict gates have been removed, so the normal `cost` field is now the sole political-power availability check.

No further safe, explicitly required non-model decision or mission gap was identified in this second bounded pass.

## Changed file and identifiers

| File | Identifier | Regular political-power cost |
| --- | --- | ---: |
| `common/decisions/016_brilliant_scientist_directorate_institutions.txt` | `brilliant_scientist_award_national_science_chair` | 35 |
| Same file | `brilliant_scientist_rotate_grants_among_institutions` | 25 |
| Same file | `brilliant_scientist_let_kruger_select_institutions` | 25 |
| Same file | `brilliant_scientist_protect_dissenting_scientists` | 30 |
| Same file | `brilliant_scientist_dismiss_ethics_chair` | 30 |

The removed conditions were `has_political_power >` checks against the same central constant used by each decision's `cost` field.

## Before and after behavior

Before, the National Science Chair action cost 35 political power but remained unavailable at exactly 35 political power.

The grant-rotation and Kruger-selection actions cost 25 but remained unavailable at exactly 25, while the dissent and ethics-chair actions cost 30 but remained unavailable at exactly 30.

After, each becomes selectable once the ordinary engine cost is payable, without changing its political-power amount or any other requirement.

## Directorate decision category lifecycle notes

The three appointment-method decisions remain visible only to the current host after it has chartered the university research network and before a method receipt is selected.

They share `brilliant_scientist_institutional_appointment_in_progress`, set the method lock on success, and remain one-shot decisions.

National Chair, grant rotation, and Kruger selection respectively run for 90, 60, and 45 days.

The two institutional-conflict decisions remain visible only to the current host after it has established a Directorate institution and before either policy receipt is recorded.

They share `brilliant_scientist_institutional_conflict_in_progress`, have mutually exclusive terminal policy flags, and each runs for 60 days.

Every affected action still cancels if the country stops hosting the Directorate or loses control, clearing only its in-progress flag without applying the policy or appointment receipt.

## Mission quality notes

This patch touches no HOI4 mission entry.

The affected timed decisions are mission-like actions with a complete lifecycle: host and route requirement, timed production burden, one terminal receipt, cancellation cleanup, and duplicate protection.

The appointment actions operate at country scope and require the university-network route, while the conflict actions operate at country scope and require an established institution.

Their only duplicate risks are repeat policy or method rewards, which the existing one-shot flags, shared in-progress flags, method lock, and mutually exclusive conflict receipts already prevent.

## Cost and requirement clarity

Regular decision `cost` is the player-facing and engine-enforced political-power requirement for each affected action.

The remaining availability checks retain the meaningful non-PP requirements: current host control, no active sibling action, support equipment, manpower where applicable, and the appropriate network or institution receipt.

The existing timed consumer-goods and production-efficiency burdens, material spends, and modifiers are unchanged.

## AI validity and route-lock notes

All five decisions retain their existing `ai_will_do` blocks.

Using the standard `cost` field keeps the engine-aware regular political-power cost available to AI selection rather than introducing a custom-cost contract.

The university-network, institution-established, method-selected, policy-selected, current-host, and control-lost checks continue to prevent invalid routes and stale host targets.

## Localisation and tooltip notes

No localisation keys changed because the visible regular costs and all decision or effect tooltips were already correct.

Removing the redundant hidden availability check aligns the UI's displayed cost with actual selection behavior.

## Cleanup and exploit-risk notes

The patch does not change material or manpower spending, timers, temporary modifiers, completion flags, or cancellation effects.

The existing shared in-progress flags still block parallel appointment or conflict actions.

The existing terminal receipts still block repeat policy or method rewards, so this correction creates no political-power, equipment, unit, project-stage, or capacity loop.

## Validation

Reviewed the offline Decision Modding reference, which documents `cost = <int>` as the regular political-power cost for a decision.

Reviewed the current Event 016 formal-recognition precedent in `common/decisions/016_brilliant_scientist_kruger_state_foreign_integration_decisions.txt`, which relies on its regular `cost` without a stricter duplicate political-power gate.

Reviewed the core-runtime map's explicit statement that formal-recognition decisions should rely on the engine cost gate instead of `political_power > cost`.

Ran a focused static lifecycle check for all five changed decision IDs, confirming that each retains its exact central `cost`, `fire_only_once`, completion effect, cancellation effect, removal effect, and AI block.

Scanned every Event 016 decision file and confirmed that no strict `has_political_power >` availability gate remains beside a regular decision cost.

## Skipped meaningful validation

No live game session was launched because live validation belongs to the user.

No scripted GUI inspection or render was needed because no decision-owned GUI surface changed.

No localisation validation was run because no localisation file changed.

## Remaining issues and uncertainty

This correction does not re-evaluate the policy vectors, timed logistics burden, AI preference weights, or containment-score effects of the institutional governance tranche.

The accepted country-specific settlement pilot remains event-driven and intentionally forbids a new decision, focus, GUI, route, or model package.

No models were created or modified.

No fallback or simplification was used.

## Plan handoff path

This file is the implementation handoff.
