# Event 016 Mengele Computation Incident Effects

## Overview

This owner-local core models one private corrupted-model incident for the Mengele Computation provider and one concrete paid technical recovery.
It is deliberately separate from the existing Kruger incident system, the public Directorate meter, native special-project completion, and neutral learned-technology state.
The parent must call `brilliant_scientist_mengele_dispatch_computation_incident` only after an actual provider stage output has settled or after the native risky Computation Prototype option has settled.

## Helper map

| Identifier | Scope and inputs | Outputs | Side effects and call sites |
| --- | --- | --- | --- |
| `brilliant_scientist_mengele_load_computation_incident_pressure` | Country scope; temporary `mengele_event016_requested_stage` selector. | Temporary `mengele_event016_computation_incident_pressure` and complement. | Reads the existing four stage-capacity values and four accident factors, multiplies and clamps them, and does not persist state. Called only by the dispatch helper. |
| `brilliant_scientist_mengele_record_computation_incident` | Country scope; provider validity and the four-stage temporary selector are checked internally. | Temporary `mengele_event016_computation_incident_recorded` result. | Creates one active private incident, records permanent incident history/count, and adds the private penalty modifier. Called by the incident random branch. |
| `brilliant_scientist_mengele_dispatch_computation_incident` | Country scope; private stage selector plus a caller-authenticated real output. | Temporary `mengele_event016_computation_incident_dispatched` result, set only when the incident branch records an incident. | Uses the pressure/complement `random_list`, refuses invalid or active states, and never writes Kruger fields. Parent stage output and native risky Prototype callbacks are the only callers. |
| `brilliant_scientist_mengele_clear_computation_incident` | Country scope; no selector. | None. | Clears only the private active flag and private dynamic modifier while retaining all history and learned knowledge. Used by recovery success and cleanup. |
| `brilliant_scientist_mengele_begin_computation_incident_recovery` | Native decision callback in country scope; incident active, valid provider, no recovery receipt, and inclusive direct affordability after native admission. | Temporary `mengele_event016_computation_incident_recovery_started` result. | Stores and debits exactly 35 Political Power, 300 Support Equipment, and 500 fuel, then sets one active receipt. The decision's native modifier owns 2 civilian factories for 60 days. |
| `brilliant_scientist_mengele_cancel_computation_incident_recovery` | Country scope; exact active direct receipt. | Temporary `mengele_event016_computation_incident_recovery_cancelled` result. | Snapshots and clears the receipt before refunding all three direct payments once; invalid-provider cancellation also clears transient incident state. Decision `cancel_effect` and parent cleanup call it. |
| `brilliant_scientist_mengele_finish_computation_incident_recovery` | Country scope; exact active receipt, active incident, and valid provider. | Temporary `mengele_event016_computation_incident_recovery_finished` result. | Clears the receipt and private penalty, then records permanent recovery history/count once. Decision `remove_effect` calls it. |
| `brilliant_scientist_mengele_cleanup_computation_incident` | Country scope; no selector. | Temporary `mengele_event016_computation_incident_cleanup_completed` result. | Exposed parent cleanup wrapper; refunds an exact receipt before clearing transient state and is idempotent. It preserves provider receipts, native history, neutral knowledge, and both histories. |

## Pressure and probability

The pressure table is authoritative from existing shared constants.

| Requested stage | Existing capacity | Existing accident factor | Intrinsic pressure | Complement |
| --- | ---: | ---: | ---: | ---: |
| Theory | `constant:brilliant_scientist_project_board.capacity_theory` = 10 | `constant:brilliant_scientist_accident.theory_stage_factor` = 0.50 | 5 | 95 |
| Prototype | `constant:brilliant_scientist_project_board.capacity_prototype` = 10 | `constant:brilliant_scientist_accident.prototype_stage_factor` = 1.00 | 10 | 90 |
| Deployment | `constant:brilliant_scientist_project_board.capacity_deployment` = 15 | `constant:brilliant_scientist_accident.deployment_stage_factor` = 1.25 | 18.75 | 81.25 |
| Weaponization | `constant:brilliant_scientist_project_board.capacity_weaponization` = 15 | `constant:brilliant_scientist_accident.weaponization_stage_factor` = 1.60 | 24 | 76 |

The computed pressure is clamped to `constant:brilliant_scientist_accident.minimum` and `constant:brilliant_scientist_accident.maximum` before the weighted roll.
The `random_list` uses `var:mengele_event016_computation_incident_pressure` and `var:mengele_event016_computation_incident_complement` weights, matching the offline effects documentation and the vanilla `common/scripted_effects/001_communism_spread_effects.txt` temporary-variable precedent.
The complement branch is an explicit empty `random_list` outcome, so an incident is not created when the roll misses.
Invalid or missing `mengele_event016_requested_stage`, invalid provider state, an already active incident, and an active recovery receipt all fail closed.
The new random surface is design-backed by `E016_MENGELE_COMPUTATION_STAGE_INCIDENT_BASELINE_2026_09_02.scenarios.json` with SHA256 `9a6548a02519ec1d92a53cc246996a2b552604e04e74d7c115ec999bb33f532b`, not engine acceptance evidence.

## Recovery transaction

The recovery begin helper is a native-decision callback, not a standalone reservation API.
Decision admission checks all four burdens, including free civilian factories.
After admission, the callback rechecks provider, incident, receipt, and the three direct payments but does not require the same factories to remain free after the native modifier may have reserved them.
This preserves exact-cost starts regardless of whether native reservation occurs before or after `complete_effect`; no script adds or refunds factories.
The general affordability tooltip retains the four-burden predicate.

The decision uses the existing `mengele_clone_army_category` and the reused generated icon `GFX_decision_brilliant_scientist_project_computational_mathematics_prototype`.
The icon is already defined by `interface/016_brilliant_scientist_project_icons.gfx`, so no asset or sprite registration is required.
The four cost axes are the native 2-civilian-factory reservation plus the three private direct receipts for Political Power, Support Equipment, and fuel.
The inclusive affordability trigger is shared by `available` and `custom_cost_trigger` through `brilliant_scientist_mengele_computation_incident_recovery_can_pay`.
No trucks or manpower are charged or refunded.
`cancel_if_not_visible = no` keeps the decision instance under its explicit cancel trigger so invalid provider cleanup can refund the receipt.
The cancel and finish paths use the exact private recovery receipt, clear receipt state before settlement, and therefore cannot refund or record success twice.
An incomplete receipt cannot award a refund or successful recovery, but normal expiry still reaches cancellation and clears its orphaned payment fields and active recovery flag.
The incident itself remains unresolved while its provider is valid, allowing another properly funded response.
Native completion of the Computational Engine remains valid while the private incident is active, and the core never revokes learned knowledge or invalidates the provider project.

## State and cleanup contract

Transient state uses `mengele_event016_computation_incident_active`, `mengele_event016_computation_incident_recovery_active`, and the three direct-cost variables.
Permanent history uses `mengele_event016_computation_incident_history`, `mengele_event016_computation_incident_history_count`, `mengele_event016_computation_recovery_history`, and `mengele_event016_computation_recovery_history_count`.
No event target is needed because the incident and recovery are country-local and the native decision owns its own timer lifecycle.
Program cleanup calls `brilliant_scientist_mengele_cleanup_computation_incident` before any broader provider cleanup clears identity or receipt state.
Cleanup first cancels and refunds an exact direct receipt, then clears the active incident and modifier, and leaves every provider-stage receipt and learned package untouched.

## Migration and integration

The stage decision worker's four wrappers already set `mengele_event016_requested_stage` for begin, cancel, and finish.
The parent should call the dispatch helper while that same private stage selector is bound immediately after successful stage output, then clear the selector as usual.
The parent should set the same private selector to `constant:brilliant_scientist_project_stage.prototype` for the native risky Prototype branch and call the same dispatch helper only after the native option has actually settled.
The parent owns the native callback, provider modifier transition, and program-cleanup call sites.
This core contains no event ID, project definition, GUI, public meter, technology, spirit, asset generation, Kruger state, or new world pulse.

## Validation and limitations

The required offline wiki core and vanilla effects/triggers/decision/modifier/localisation/project documentation were read before implementation.
The focused read-only Event 016 inspection returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics, but its workspace-wide unresolved helper/lifecycle diagnostics mean it is source-navigation evidence only.
The post-edit `hoi4.probability_inspect` discovery found the two-entry `random_list` pool with no unresolved source entries and recorded source hash `8fe18d0f422106b07d15a0e5b95141bae5f9576223d30bbbe07b6aa209d237` in artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c550d26b2c271ff52b280c40d58cba799000638dec308b15df440dae82f9d4d/6216faff5e87c88b5bf45bb588d124c9920f8594580d31e3b35f6d30e154394b/probability-inspect-8fe18e3d0f42.json`.
The matching evaluate pass used all fourteen named scenarios from `E016_MENGELE_COMPUTATION_STAGE_INCIDENT_BASELINE_2026_09_02.scenarios.json`, produced twenty-eight candidate rows with zero diagnostics, and left two dynamic `var:` weights unresolved because the analyzer cannot derive temporary pressure/complement values from the fixture.
The incident same-source compare returned zero changes with two unresolved dynamic weights; it is a capability receipt, not a pre/post balance result.
The original implementation handoff did not obtain `chaosx_ai_probability_auditor` acceptance, and its prepatch inspection recorded absent-source results for this new file.
That historical evidence gap is not a claim that the auditor route is currently unavailable.
The unchanged native baseline is `E016_MENGELE_COMPUTATION_BASELINE_2026_09_02.scenarios.json` with SHA256 `3c197628aa74eb4dba902f771ec0eba18e2dcf66cf0b1f886858a5632d5bb99e`.
No engine acceptance claim is made by this owner-local source implementation.

The 2026-09-08 recovery correction separates four-cost admission from three-payment debit and makes malformed expiry retire recovery remnants without an inferred refund or success.
The current `.tools/audit_mengele_conventional_incident_contract.mjs` source/API regression passes 165 scenarios across Computation and five conventional incident families, including exact civilian-factory affordability under both modeled reservation orders and missing-payment-component expiry for all six families.
Provider validity is stubbed, native timer and factory ordering are modeled rather than executed, and engine resource caps are not modeled.
These checks do not replace the outstanding MCP lifecycle comparison or establish in-game acceptance.

## Future plans

Future incident families may reuse the lifecycle shape only after each family receives its own approved private pressure, penalty, receipt, and recovery contract.
Any shared helper extraction must preserve the current owner-local boundary and must not merge private provider incidents with Kruger ledgers or public Directorate state.
