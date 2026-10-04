# Event 012 Gods of Africa Migration reception adapter handoff

Disposition: `implemented` for the bounded Migration-owned adapter. Event 012 caller wiring and the overall protection-family goal remain parent-owned and incomplete.

## Acceptance basis and ownership

The parent request authorizes a shelter-focus capacity offer at the selected participant's capital, without moving civilians, through the existing Migration shelter and medical service APIs. This handoff implements only that owner interface. It changes no Event 012 event, focus, decision, localisation, spreadsheet, or event-documentation file.

## Files and identifiers

- `common/scripted_effects/migration_adapter_effects.txt`: added `migration_install_gods_of_africa_reception_service` and `migration_clear_gods_of_africa_reception_service`.
- `common/scripted_effects/migration_adapter_effects.md`: documented scope, preflight, amounts, owner result, receipt, cleanup, and caller example.
- This handoff.

No script constant, public variable, on-action, periodic hook, decision, event target with global lifetime, or population transfer was added. There are no Event 012 call sites in this patch. The existing `migration_reception_bootstrap` shares and `migration_capacity.people_per_k` supply all tuning.

## Helper and tuning map

| Helper | Scope and inputs | Output | Side effects | Intended caller |
| --- | --- | --- | --- | --- |
| `migration_install_gods_of_africa_reception_service` | Selected participant country; no explicit arguments. Requires no Gods receipt, valid owned and controlled capital, current Migration-consumed famine food-safety proof, stage at or below `migration_capacity.food_safe_stage`, and both service amount and proof fields absent or zero. | Temporary `migration_gods_reception_install_result = migration_capacity.one` only after both owner setters, candidate registration, installed fields, and participant receipt succeed. The hidden `migration_gods_reception_service_active` flag is the durable caller success witness. | Shelter and medical people-unit service on the capital through the owner APIs, candidate registration, owner capacity dirty marking, country-owned exact state pointer and amount/proof receipt. | Parent's selected-participant shelter-focus protection effect. |
| `migration_clear_gods_of_africa_reception_service` | Same participant country; no explicit arguments. Uses its durable `migration_gods_reception_state` pointer, never current capital. | Temporary `migration_gods_reception_cleanup_result = migration_capacity.one` only if both owner clear effects run. Always retires the hidden Gods receipt. | Clears both state services only if owner/controller, both capacities, and both owner proofs exactly match the participant receipt. Otherwise preserves both state fields. | Parent's defiance, participant archive/finalization/cancellation, host-loss, and settlement teardown paths. |

Installed amounts are `state_population_k * migration_capacity.people_per_k * migration_reception_bootstrap.shelter_population_share` and the same population basis times `medical_population_share`, rounded to positive people units. The existing shares are 0.40 and 0.10 respectively. These values describe reception capacity only. They do not authorize a route or change population, reception load, cohort rows, or Deaths accounting.

The participant-owned receipt fields are `migration_gods_reception_state`, `migration_gods_reception_shelter_amount`, `migration_gods_reception_medical_amount`, `migration_gods_reception_shelter_proof`, and `migration_gods_reception_medical_proof`, plus `migration_gods_reception_service_active`. The install helper uses only short-lived `migration_gods_reception_participant` and `migration_gods_reception_installed_state` event targets within its effect chain. The cleanup helper recreates only the short-lived participant target. A second install with a receipt returns zero without changing service. A second cleanup finds no receipt and changes no service.

## Parent migration plan and exact caller contract

The parent should call the install effect in the selected registered participant country after its Event 012 shelter capability and protection eligibility gates, then commit an Event 012 success/reward only if `migration_gods_reception_install_result` equals `constant:migration_capacity.one` and `migration_gods_reception_service_active` is present. The effect accepts no host target, origin state, destination state, cohort, or civilian count from Event 012. It checks for an owned capital before entering `capital_scope`, then chooses the participant's current capital itself.

The parent should call cleanup in that same participant scope on defiance, participant archive/finalization/cancellation, host loss, and settlement. Cleanup should run before any parent path discards the selected participant scope. If the capital moved after install, the stored state remains the only cleanup target. A failed or stale receipt is retired, and Event 012 must not infer that a foreign-owned or rewritten Migration service was removed.

This helper does not replace Event 012's material-support or diplomatic protection logic. The parent remains responsible for focus/decision gates, costs, tooltips, AI, player-facing text, and all cross-system validation.

## Inspection and validation evidence

The offline Paradox wiki core pages were consulted, with Data structures, Effects, Triggers, and Scopes used for scoped variables, event targets, `capital_scope`, and proof comparisons. Installed vanilla `documentation/effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, and `common/script_constants/documentation.md` were consulted. A vanilla capital-scope precedent appears in `common/scripted_effects/AFG_scripted_effects.txt`.

Read-only `hoi4.focus_inspect` on `africa_continental_focus_tree` returned `FOCUS_INSPECTED` in workspace `mod_chaos_redux_ea3b2d67c2c0`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9067164e1dd091cfc30dce735d221ed94c03b6fcf4608666ac321e10c9a5814e/bd5657c996fed213fd65194442c0b8d8b78761ab848f8e2051ebb3b00dd5bb20/focus-inspect.ea205181e0d4c0e8.json`. No focus source was changed. No specific map state, GUI, probability surface, or Event 012 event node is changed by this adapter, so those domain inspections were not claimed.

Task-specific source review matched all four called owner APIs and their request/result fields to `migration_capacity_effects.txt`, verified the reused tuning keys in `migration_core_constants.txt` and `migration_mission_constants.txt`, checked the new block for population/transfer and global-hook calls, and inspected its exact diff. The new scripted block's brace depth returned to zero and `git diff --check` found no whitespace error. HOI4 was not launched. Runtime effect execution, actual capacity recalculation, and Event 012 caller behavior remain untested by this subagent.

## Limits and follow-up

The current owner setter source requires `migration_reception_*_service_request_proven > constant:migration_capacity.one`, while `migration_capacity_effects.md` describes a positive proof and the existing Migration decision caller submits one. This adapter constructs a proof of two using two `migration_capacity.one` additions to satisfy the executable gate. The stored owner service proof is one. The Migration owner should reconcile the general setter documentation and other callers separately.

The owner service record has no writer identity or mutation revision. Exact amount and proof comparison cannot detect a later writer that installs identical values while leaving the Gods receipt intact. A changed value or proof is preserved by cleanup. The candidate state remains registered after owner service clearance and becomes ineligible under the existing Migration candidate predicate. No unsupported route or population movement was substituted for the accepted capacity service.
