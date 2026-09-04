# Handoff 016 Final Mengele Computation Incident Core

Date: 2026-09-02
Owner: scripted-system architecture subagent
Parent: `/root`
Status: bounded source core complete; parent integration and final auditor review remain explicitly pending.

## Scope and boundary

This handoff covers one private corrupted-model incident and one concrete technical recovery for the Event 016 Mengele Computation provider.
The implementation does not add an event ID, native project, GUI, public meter, technology, spirit stack, asset, model, world pulse, timeout mission, or Kruger state mutation.
The separate Computation stage provider core and four-stage decision surface were read for integration contracts but were not edited.

The core never reads or writes Kruger Exposure, accident pressure, ledger, incident, or related public state.
It never invalidates the native provider, revokes native completion, or removes learned knowledge.
Native completion may settle while this private incident is active.

## Files changed

- `common/scripted_effects/016_mengele_computation_incident_effects.txt`
- `common/scripted_effects/016_mengele_computation_incident_effects.md`
- `common/scripted_triggers/016_mengele_computation_incident_triggers.txt`
- `common/decisions/016_mengele_computation_incident_decisions.txt`
- `common/dynamic_modifiers/016_mengele_computation_incident_modifiers.txt`
- `localisation/english/016_mengele_computation_incident_l_english.yml`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/handoff016_final_mengele_computation_incident_2026-09-02.md`

No other files were intentionally changed by this subtask, and no staging or commit was performed.

## Helper map and integration contract

### Pressure and incident dispatch

- `brilliant_scientist_mengele_load_computation_incident_pressure` is country-scoped and reads only the existing temporary selector `mengele_event016_requested_stage`.
- `brilliant_scientist_mengele_record_computation_incident` requires the valid four-stage temporary selector, then creates one active private incident, records permanent incident history/count, and adds the private penalty modifier.
- `brilliant_scientist_mengele_dispatch_computation_incident` validates the actual provider and selector, derives pressure, rolls an explicit complement `random_list` no-op, and sets its temporary result only when the incident branch records an incident.
- `brilliant_scientist_mengele_clear_computation_incident` removes only the private active flag and private modifier.

The parent must call `brilliant_scientist_mengele_dispatch_computation_incident = yes` only after an actual successful stage output has settled, while the stage core still has `mengele_event016_requested_stage` bound.
The native risky Computation Prototype branch must set that same private selector to `constant:brilliant_scientist_project_stage.prototype` and call the same dispatch helper only after the native risky option has actually settled.
The helper itself is fail-closed for a missing or invalid selector, invalid provider, active incident, or active recovery receipt.

### Recovery transaction

- `brilliant_scientist_mengele_begin_computation_incident_recovery` stores and debits the direct receipt once.
- `brilliant_scientist_mengele_cancel_computation_incident_recovery` snapshots and clears a matching receipt before refunding it once.
- `brilliant_scientist_mengele_finish_computation_incident_recovery` resolves only a matching receipt with an active incident and valid provider, then records recovery history once.
- `brilliant_scientist_mengele_cleanup_computation_incident` is the parent-facing cleanup wrapper.

The recovery decision `mengele_event016_computation_incident_recovery` is reopened under the existing `mengele_clone_army_category`.
The decision remains visible while the private incident is active, including the invalid-provider window needed to run the cancel/refund guard.
It uses `cancel_if_not_visible = no` and an explicit cancel trigger for missing incident, missing exact receipt, or invalid provider.
The custom affordability trigger is shared by `available` and `custom_cost_trigger`, and uses inclusive equality for every axis.

The four cost axes are exactly:

| Axis | Amount | Owner | Settlement |
| --- | ---: | --- | --- |
| Civilian factories | 2 | Native decision | Native `modifier` for 60 days and native release on removal |
| Political Power | 35 | Private receipt | Debited by begin helper and refunded by cancel/cleanup |
| Support Equipment | 300 | Private receipt | Debited by begin helper and refunded by cancel/cleanup |
| Fuel | 500 | Private receipt | Debited by begin helper and refunded by cancel/cleanup |

The decision does not charge trucks or manpower.
Its native two-factory field uses the file-scoped `@CR_SC_MENGELE_COMPUTATION_INCIDENT_RECOVERY_FACTORIES = 2` because the native decision modifier field rejects `constant:` tokens in this project surface.
The political power, support equipment, fuel, and duration values reuse the existing `brilliant_scientist_project_board.response_technical_*` constants.

On native removal, the finish helper first requires the exact receipt, active incident, and valid provider.
If that exact receipt exists but either incident or provider is no longer valid, the matching-receipt fallback calls cancellation/refund once and does not write recovery history.
This protects a paid receipt when a provider-invalid callback wins the same tick as decision removal.
The `can_start` trigger excludes the active recovery flag independently of receipt completeness, so malformed active costs cannot be overwritten.

The parent should call `brilliant_scientist_mengele_cleanup_computation_incident = yes` from program cleanup before broader provider identity or receipt cleanup.
Cleanup refunds a matching direct receipt before clearing malformed transient receipt fields and the private incident modifier.
Cleanup leaves both permanent history sets, provider stage receipts, native completion, and learned knowledge intact.

## State lifecycle

Transient flags and variables are:

- `mengele_event016_computation_incident_active`
- `mengele_event016_computation_incident_recovery_active`
- `mengele_event016_computation_incident_recovery_cost_political_power`
- `mengele_event016_computation_incident_recovery_cost_support_equipment`
- `mengele_event016_computation_incident_recovery_cost_fuel`

Permanent history is:

- `mengele_event016_computation_incident_history`
- `mengele_event016_computation_incident_history_count`
- `mengele_event016_computation_recovery_history`
- `mengele_event016_computation_recovery_history_count`

All selectors and roll intermediates are temporary variables.
No event target is required because the incident and recovery decision are country-local and the native decision owns its own timer.

## Probability and tuning contract

Pressure is derived from existing constants and clamped to the existing 0..100 accident range before the roll.

| Stage | Existing capacity | Existing accident factor | Pressure | Complement |
| --- | ---: | ---: | ---: | ---: |
| Theory | 10 | 0.50 | 5 | 95 |
| Prototype | 10 | 1.00 | 10 | 90 |
| Deployment | 15 | 1.25 | 18.75 | 81.25 |
| Weaponization | 15 | 1.60 | 24 | 76 |

The implementation uses `var:mengele_event016_computation_incident_pressure` and `var:mengele_event016_computation_incident_complement` as the two `random_list` weights.
The temporary-variable form is supported by the offline effects documentation and the vanilla `common/scripted_effects/001_communism_spread_effects.txt` random-list precedent, which also uses `var:` weights and an explicit complement branch.
The stage core uses the same temporary-variable syntax for its dynamic weights and arithmetic.

The private modifier `brilliant_scientist_mengele_computation_incident` is enabled only by the active private incident and strict actual-provider predicate.
It reuses `constant:brilliant_scientist_project_modifier.accident_penalty_major` for decryption and `constant:brilliant_scientist_project_modifier.accident_penalty_standard` for planning speed.
The existing generated Computation-stage icon `GFX_decision_brilliant_scientist_project_computational_mathematics_prototype` is reused.

## Required source references

Before editing, the following were read: repository `AGENTS.md`; `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents` skill instructions; the offline Paradox wiki core pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding; the relevant offline scripted-GUI pages; and the vanilla documentation for effects, triggers, script concepts/constants, modifiers, projects, decisions, and localisation behavior.
Existing `common/scripted_effects/chaosx_dynamic_effects.txt` and its documentation were checked first; no existing dynamic helper matched this private incident boundary.

## Validation evidence and unsupported analysis

The frozen native baseline is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/E016_MENGELE_COMPUTATION_BASELINE_2026_09_02.scenarios.json` with SHA256 `3c197628aa74eb4dba902f771ec0eba18e2dcf66cf0b1f886858a5632d5bb99e`.
The incident/stage fixture is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/E016_MENGELE_COMPUTATION_STAGE_INCIDENT_BASELINE_2026_09_02.scenarios.json` with SHA256 `9a6548a02519ec1d92a53cc246996a2b552604e04e74d7c115ec999bb33f532b` and covers the four pressures, peace/war, native no-DLC, exact/one-short affordability, active incident, invalid provider, and native risky safe options.

The focused pre-edit Event 016 inspect returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and source-navigation artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b631bb83abc677017586d3bdad8965705ebb12e6178bb12407336d0a111b25d/063ff754ae621b811dcd53283c6dd3fb7b86e5084da50c4f267a950b3810e57c/event-trace-46be3d59f3cc.json`.
The post-edit workspace scan returned `EVENT_INSPECTED` with broad workspace diagnostics and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d4244e549c5094eefa99e3fa94d58ebadba0b471051ff8e82495cd50947d2180/e63d424d281669c34f698e4ed90119ba5517871a873c0c44c89a8f3c8f549e21/event-scan-e535a3f1177b.json`; it is not a focused engine acceptance result.

The mandatory probability workflow was run through the available read-only HOI4 MCP routes.
`hoi4.probability_inspect` on the incident found a complete two-entry pool with source hash `8fe18d0f422106b07d15a0e5b95141bae5f9576223d30bbbe07b6aa209d237` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c550d26b2c271ff52b280c40d58cba799000638dec308b15df440dae82f9d4d/6216faff5e87c88b5bf45bb588d124c9920f8594580d31e3b35f6d30e154394b/probability-inspect-8fe18e3d0f42.json`.
The incident evaluate pass used all fourteen fixture scenarios and produced twenty-eight candidate rows with zero diagnostics, but two dynamic `var:` values remained unresolved because the analyzer cannot calculate temporary pressure/complement variables from the scenario state; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0775417aedb1fb86df735b8dcf74e82700d48032c586a02e0b7c975da5bcbc0d/6015537492b4d509966316bf5df146a0aca9bb5290c2276eb2a8c7c20087cbcc/probability-965abbd19e091eee6924dd83.json`.
The decision inspect discovered that the requested `decision_ai_will_do` adapter was empty in this runtime and suggested `mission_ai_will_do`; this is recorded as an adapter limitation, not silently treated as a decision acceptance result.
The decision evaluate pass returned eight score-only rows with raw AI score 25 and one unresolved eligibility trigger because the fixture does not declare the decision's `custom_trigger_tooltip` blocks; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/de6cc4aeb0dec33115615c1883542370e5e68a181c24375abd3bb09efd6e24f0/d900e0338691d14a03d6cb3beb06b128fe888684b354f8db30d13977a6ad11d0/probability-64d1eb3910ed52909c188927.json`.

Same-source compare capability receipts were obtained for both weighted surfaces, but no true before/after balance compare exists because the new files were absent at the prepatch source revision `5f31c83ce66f1c00fbf21f7a120f7ba2d1f25d55`.
The incident same-source compare returned zero changes with two unresolved dynamic weights in artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bf21897bb237399671ee1412d25a4d9b239c5274c4aaab2cc56beea4f10fe8c5/55e1308b532072a032ad540d58b4fc6c3519ff75b76861ce2cced1d454bcbe43/probability-8e875c1bcb31e31453ec1dec.json`.
The decision same-source compare returned zero changes with one unresolved eligibility trigger in artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5a1b3d35f6bded9a6bab7bdff70affc3be085b9085cc180bb3ffd77e06f46550/5916c9bff3f09293ff53f3f973c67607b75f6a0fea08b9a8fdeb166048bf5ab8/probability-2c762ef57fbc595a0bd98916.json`.
The requested `chaosx_ai_probability_auditor` subagent/tool route was not present in the callable inventory, so the parent must obtain its read-only inspect/evaluate/compare evidence after wiring and must not claim engine acceptance from these partial MCP results.
No game launch, game log, config edit, or live consumer test was performed.

## Simplifications, omissions, and follow-up

No gameplay simplification or fallback was introduced.
The only unresolved items are external to this bounded core: parent wiring of the stage-output and native-risk callbacks, parent cleanup call placement, the separate four-stage decision/provider integration, the unavailable auditor route, and analyzer inability to resolve dynamic temporary weights or decision custom tooltips from the current fixtures.
The parent should preserve the exact private selector binding and call order described above when integrating.
