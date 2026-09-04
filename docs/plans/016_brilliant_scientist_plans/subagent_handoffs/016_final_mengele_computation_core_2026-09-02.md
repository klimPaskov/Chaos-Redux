# Event 016 Mengele Computation core handoff

## Status

The bounded Computation-only helper core is implemented in five new owner-local artifacts. No existing decision, bridge, modifier, localisation, CXT, AI, on-action, native project, event, GUI, or shared API file was edited. No files were staged or committed, as requested by the parent task.

This handoff covers family ID 1 (`computation`) and stages 1 through 4 (`theory`, `prototype`, `deployment`, `weaponization`). Family IDs 2 through 15 remain intentionally unimplemented.

## Files changed

- `common/script_constants/016_mengele_project_stage_constants.txt` adds the fixed Mengele program provenance source `100001` and the missing Computation Prototype quote of 2 CIC, 68 PP, 200 support equipment, and 100 fuel.
- `common/scripted_triggers/016_mengele_project_stage_triggers.txt` adds the strict provider lifecycle gate, Computation request/predecessor/affordability/receipt gates, and native completion authenticity gate.
- `common/scripted_effects/016_mengele_project_stage_effects.txt` adds aligned receipt initialization, quote loading, begin/cancel/finish settlement, Computation outputs, native prototype synchronization, availability reconciliation, and provider cleanup.
- `common/scripted_effects/016_mengele_project_stage_effects.md` documents the helper contract, tuning, arrays, side effects, lifecycle, targets, API provenance, and validation limits.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_mengele_computation_core_2026-09-02.md` records this handoff and parent integration gates.

## Helper map

| Identifier | Scope and interface | Behavior and side effects |
| --- | --- | --- |
| `brilliant_scientist_mengele_project_stage_provider_is_valid` | Country trigger; no inputs | Requires existence, Mengele identity, `mengele_clone_focus_directorate_project_registry`, no Kruger host or incident, no defeated/rejected/closed/finally-expired/recently-expired program state, no Event 016 terminal or global world-end state, and either the actual scenario/victory/faction route or the existing full/restricted active-program trigger (live authority/site/idea checks). It deliberately does not reject `germany_mengele_coup_fired`, preserving the sovereign victory route. |
| `brilliant_scientist_mengele_computation_stage_request_is_valid` | Country trigger; temporary `mengele_event016_project_family` and `mengele_event016_requested_stage` | Accepts only Computation family ID 1 and the four existing stage IDs. Invalid or unsupported requests fail closed. |
| `brilliant_scientist_mengele_computation_stage_predecessor_is_valid` | Country trigger; temporary requested stage | Requires the exact previous provider completion flag and rejects a repeated current stage. |
| `brilliant_scientist_mengele_computation_stage_can_pay` | Country trigger; temporary requested stage | Checks direct PP/support/fuel resources for the selected stage. It does not check or spend CIC. |
| `brilliant_scientist_mengele_computation_stage_receipt_is_empty` | Country trigger; valid Computation request | Returns true before initialization or when the Computation receipt at array index 0 is `none`. |
| `brilliant_scientist_mengele_computation_stage_receipt_matches` | Country trigger; valid Computation callback selectors | Requires the initialized marker and exact current stage at array index 0. Wrong family/stage and repeats fail. Provider validity is intentionally absent for cleanup. |
| `brilliant_scientist_mengele_computation_native_output_is_authentic` | Country trigger; Computation selector and exact native output context | Requires strict provider validity, Theory history, no provider Prototype history, and `is_special_project_completed = sp:sp_brilliant_scientist_computational_engine`. The parent must call it only from that exact native project's `project_output` branch; an optional pending marker is presentation state, not an authentication prerequisite. |
| `brilliant_scientist_mengele_initialize_project_stage_receipts` | Country effect; caller must prevalidate provider and request | Initializes five aligned fifteen-slot arrays once and writes the boolean country flag `mengele_event016_provider_receipts_initialized`. It is never called for an invalid/unimplemented request. |
| `brilliant_scientist_mengele_load_computation_stage_quote` | Country effect; the two private selectors | Returns temporary quote values `_quote_loaded`, `_quote_duration_days`, `_quote_civilian_factories`, `_quote_political_power`, `_quote_support_equipment`, and `_quote_fuel`. Existing tables supply all values except Prototype. |
| `brilliant_scientist_mengele_begin_project_stage` | Country effect; the two private selectors | Validates provider, predecessor, stage ownership, and direct stockpiles, initializes safely, debits exactly PP/support/fuel, and stores stage plus four quote receipts. Returns `mengele_event016_stage_started`. It has no global one-active-project lock. |
| `brilliant_scientist_mengele_cancel_project_stage` | Country effect; exact callback selectors | Snapshots the three direct receipts, clears all five Computation receipt fields first, refunds PP/support/fuel once, and returns `mengele_event016_stage_cancelled`. It does not require provider validity or existence. |
| `brilliant_scientist_mengele_finish_project_stage` | Country effect; exact callback selectors | Requires the exact receipt even when the owner is invalid, clears before output/refund, applies one valid existing-provider output or refunds direct costs once, and returns `mengele_event016_stage_finished`. Invalid owner state produces no output. |
| `brilliant_scientist_mengele_apply_family_stage_output` | Country effect; internal `mengele_event016_computation_output_authorized = 1` plus exact selectors | Sets provider completion flags, reuses `brilliant_scientist_computation_theory` and `mengele_directorate_computation_prototype`, and calls the neutral API for full Deployment/Weaponization. Returns `mengele_event016_computation_output_applied`. |
| `brilliant_scientist_mengele_sync_native_project_prototypes` | Country effect; Computation selector and exact native output context | Authenticates native completion, records only provider Prototype output, clears an optional pending marker on success or stale duplicate, and returns `mengele_event016_native_prototype_synced`. Native payment and CIC are untouched. |
| `brilliant_scientist_mengele_record_native_project_prototype` | Country effect; new family selector or existing native `brilliant_scientist_project_family` selector | Routes only the Computation native callback to the adapter, preserves the older caller selector, and returns `mengele_event016_native_prototype_recorded`. The legacy-selector fallback is accepted only when the private family selector is `none`. |
| `brilliant_scientist_mengele_reconcile_project_availability` | Country effect; durable provider/native state | Sets or clears the existing `directorate_special_project_computation_available` marker and returns `mengele_event016_project_availability_reconciled`. |
| `brilliant_scientist_mengele_cleanup_provider_receipts` | Country effect; initialized provider arrays if present | Cancels the active Computation receipt without rechecking provider validity, clears pending/presentation markers, preserves completion history and neutral API entitlements, and returns `mengele_event016_provider_cleanup_applied`. |

After each entry point, `brilliant_scientist_mengele_clear_project_stage_selectors` resets only `mengele_event016_project_family`, `mengele_event016_requested_stage`, and the private index to shared `none` or zero values. It does not clear `brilliant_scientist_project_family` or unrelated caller state.

## Exact parent wrapper contract

Each parent decision callback must set the two temporary selectors immediately before invoking the matching helper. The family selector is always `set_temp_variable = { mengele_event016_project_family = constant:brilliant_scientist_project_family.computation }`; the stage selector is the literal value in the table below.

| Stage | Start effect | Completion effect | Cancel/remove effect | Active receipt fields |
| --- | --- | --- | --- | --- |
| Theory | `set_temp_variable = { mengele_event016_requested_stage = constant:brilliant_scientist_project_stage.theory }` then `brilliant_scientist_mengele_begin_project_stage = yes` | Set the same literal stage, then `brilliant_scientist_mengele_finish_project_stage = yes` | Set the same literal stage, then `brilliant_scientist_mengele_cancel_project_stage = yes` | `mengele_event016_active_project_stage_entries^0` plus the three direct-cost arrays and native-CIC quote array at `^0` |
| Prototype | `set_temp_variable = { mengele_event016_requested_stage = constant:brilliant_scientist_project_stage.prototype }` then `brilliant_scientist_mengele_begin_project_stage = yes` | Set the same literal stage, then `brilliant_scientist_mengele_finish_project_stage = yes` | Set the same literal stage, then `brilliant_scientist_mengele_cancel_project_stage = yes` | Same Computation family-1/index-0 fields |
| Deployment | `set_temp_variable = { mengele_event016_requested_stage = constant:brilliant_scientist_project_stage.deployment }` then `brilliant_scientist_mengele_begin_project_stage = yes` | Set the same literal stage, then `brilliant_scientist_mengele_finish_project_stage = yes` | Set the same literal stage, then `brilliant_scientist_mengele_cancel_project_stage = yes` | Same Computation family-1/index-0 fields |
| Weaponization | `set_temp_variable = { mengele_event016_requested_stage = constant:brilliant_scientist_project_stage.weaponization }` then `brilliant_scientist_mengele_begin_project_stage = yes` | Set the same literal stage, then `brilliant_scientist_mengele_finish_project_stage = yes` | Set the same literal stage, then `brilliant_scientist_mengele_cancel_project_stage = yes` | Same Computation family-1/index-0 fields |

The exact native callback is `brilliant_scientist_mengele_record_native_project_prototype = yes` from the existing `sp_brilliant_scientist_computational_engine` `project_output` branch. The parent may set `mengele_event016_project_family` to Computation before that call, or preserve the native callback's existing `brilliant_scientist_project_family = constant:brilliant_scientist_project_family.computation` selector when the private selector is `none`; a non-none wrong private family fails closed instead of falling back. The adapter clears only its own private selectors. It requires strict provider validity, the provider Theory completion flag, no provider Prototype completion flag, and the exact `is_special_project_completed` project gate. No project-start callback or native-payment copy is part of this contract.

## Receipt and lifecycle contract

The five regular arrays are `mengele_event016_active_project_stage_entries`, `mengele_event016_active_cost_political_power_entries`, `mengele_event016_active_cost_support_equipment_entries`, `mengele_event016_active_cost_fuel_entries`, and `mengele_event016_active_cost_civilian_factory_commitment_entries`.

The arrays are aligned to the existing fifteen family IDs at indexes 0 through 14, so Computation family ID 1 is index 0. The fifth array is a native-CIC quote only. A parent decision modifier must own `civilian_factory_use` reservation and release, and no helper in this patch calls `add_factories`.

Begin validates before receipt initialization and payment. Cancel and finish validate the exact current receipt, snapshot direct costs, clear the receipt before settlement, and then refund or output once. Repeated callbacks observe `none` and cannot repeat payment, refund, or output. The output branch checks strict provider validity, which includes existence, but the exact receipt gate is outside that branch so an accessible invalid owner still receives a safe direct-cost refund. Cancel itself has no existence or provider-validity requirement.

## Tuning and provenance

| Stage | CIC quote | PP debit | Support debit | Fuel debit | Duration |
| --- | ---: | ---: | ---: | ---: | ---: |
| Theory | Existing 1 | Existing 45 | Existing 80 | Existing 0 | Existing 120 days |
| Prototype | New 2 | New 68 | New 200 | New 100 | Existing 180 days |
| Deployment | Existing 3 | Existing 90 | Existing 600 | Existing 500 | Existing 270 days |
| Weaponization | Existing 5 | Existing 135 | Existing 1200 | Existing 1500 | Existing 360 days |

Prototype values derive from the existing base Prototype 2/75/250/500 using the Computation profile 0.80/0.90/0.80/0.20 and whole-unit rounding. The other stages read existing `brilliant_scientist_project_stage_cost` and `brilliant_scientist_project_duration` constants.

Deployment and Weaponization set the neutral API selectors, use `chaosx_grant_conventional_technology_package`, and supply the fixed `constant:mengele_event016_project_stage.provenance_mengele` source. The API owns cumulative flags, runtime modifiers, provenance arrays, and one-slot research adoption. The helper resets API selectors afterward and never inherits a caller's source.

A repository collision scan for `100001` found no current consumer outside the offline wiki's unrelated event-number example. Existing custom API sources 25 and 36 remain unaffected.

## Parent integration gates

1. Route only the parent-owned Computation branch through `brilliant_scientist_mengele_project_stage_provider_is_valid`, or add its equivalent strict lifecycle clauses to that branch. Do not broadly alias the existing nine-family `brilliant_scientist_mengele_project_provider_is_valid` gate, because the remaining family adapters retain separate lifecycle and native prerequisites. Do not define the shorter name again in the new trigger file because it already exists.
2. Parent-owned Mengele decisions must set `mengele_event016_project_family` and `mengele_event016_requested_stage` before begin, finish, or cancel. Their `civilian_factory_use` modifiers must use the four quote values and must not call an effect to add or refund factories.
3. The Theory decision must call `brilliant_scientist_mengele_begin_project_stage` with stage `theory`; its completion must call `brilliant_scientist_mengele_finish_project_stage` with the same literal receipt. Prototype follows the same pattern for stage `prototype`; Deployment and Weaponization use their exact stage selectors.
4. Decision cancellation and lifecycle closure must call `brilliant_scientist_mengele_cancel_project_stage` with the exact active stage selector. Owner-loss, program close/expiry, defeat, victory/annexation, death, and terminal cleanup must invoke `brilliant_scientist_mengele_cleanup_provider_receipts` in the original provider scope, using explicit `FROM` or a saved owner target after transfers.
5. The parent modifier owner must extend `brilliant_scientist_computation_theory` to accept `mengele_event016_computation_theory_completed` and remove the temporary provider Prototype modifier after the neutral Computation operational flag is learned.
6. The native Computation presentation path must require the strict provider gate and eligible Theory history, retain `directorate_special_project_computation_available` while native work is active, and route the exact `sp_brilliant_scientist_computational_engine` `project_output` branch to `brilliant_scientist_mengele_record_native_project_prototype`. `mengele_event016_native_computation_prototype_pending` may remain an optional presentation marker, but no project-start callback is assumed and it is not required to authenticate that exact output branch.
7. The parent must preserve the legacy native Computational Engine completion flag while avoiding duplicate payment, duplicate Prototype output, and unrelated provider stage rewards. Repeated native callbacks must clear stale pending state without applying output twice.
8. The native project's unique risky reward currently calls `brilliant_scientist_refresh_project_accident_pressure` and `brilliant_scientist_dispatch_project_accident` unconditionally. The smallest safe parent integration is an additive provider branch in that existing reward: strict Mengele providers must route to an existing provider-safe incident/recovery state or Event 016 event surface, while only the Kruger branch calls those two accident helpers. If no provider-safe incident surface exists, leave this as an explicit native-path blocker rather than silently dropping the risk. This helper intentionally leaves the native project file unchanged.
9. Parent must keep the Event 016 native completion adapter separate from the old bridge's nine-family generic prototype effect. The old bridge currently writes the legacy Computation flag/modifier directly; route the native Computation branch through the new adapter or prove an equivalent once-only dispatch without double output.
10. Parent retains responsibility for decisions, localisation and cost tooltips, bridge aliases, dynamic modifier enable/removal, native dispatch, event details/log, CXT, AI, spreadsheet/docs alignment, and live consumer acceptance.

## Migration plan

The current duplicated Mengele Computation native branch in `common/scripted_effects/016_mengele_project_bridge_effects.txt` should become a thin parent-owned dispatch into `brilliant_scientist_mengele_record_native_project_prototype`, while the new stage decisions dispatch begin/finish/cancel through the receipt core. The neutral API remains the only later-tier technology grant path. Parent lifecycle hooks then call the cleanup helper instead of reproducing three-resource refund and pending-flag cleanup logic.

No new event target is required. If a lifecycle transfer changes the current scope, parent code must preserve the provider country through its existing event target or explicit `FROM` scope and call cleanup there; this helper does not create or clear event targets.

## Validation evidence and limits

Source-level evidence covers the approved four quote rows, invalid/unimplemented request no-op ordering, one-based family-to-index-zero mapping, exact wrong-family/wrong-stage callback rejection, shortage-before-debit behavior, repeat-start suppression, owner-invalid finish refund/no-output behavior, cancel without provider validity, no `add_factories`, no Kruger board calls, and fixed source `100001` API setup.

The mandatory narrow read-only Event MCP inspection for `chaosx.nr16.1` returned partial status with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f73ba8df62da3d8579b33366762517f6aaa6585734d6ed6f72b52c2e17b7cf0c/65d6dd558cbb5c6cfd7a88b4a79c57258b7505f20ac876b55862d37f1656506e/event-trace-d9bc467fb6be.json`. Its report had `blockingDiagnostics = 0` but deferred workspace-wide helper/lifecycle projections, so it is structural evidence only and not engine execution proof.

This slice has no weighted or probability-bearing helper, so `hoi4.probability_inspect` and `chaosx_ai_probability_auditor` are not applicable. No GUI/map/focus surface is introduced. No live game launch or engine callback execution was performed. Native unique-reward isolation, parent decision wiring, provider lifecycle callers, and user live acceptance remain open gates.

The vanilla `documentation/projects/documentation.md` review documents special-project `project_output` and `iteration_output` blocks but provides no supported project-start callback token. No native start-only receipt is therefore claimed. The parent must use the exact Computation `project_output` branch plus `is_special_project_completed` and the provider Theory flag to authenticate the native Prototype; the optional pending flag is presentation state only.

## Remaining scope

Family IDs 2 through 15, terminal and singularity execution, cross-provider registry cleanup, decisions/missions, localisation, AI weights, CXT setup, shared API edits, native project edits, event log/details, and all other parent-owned Event 016 surfaces are not implemented here.

No new icon, sprite, `.gfx`, GUI, or localisation key belongs to this private core; parent-owned decision rows retain the existing Event 016 family-stage assets and text.

No fallback or unapproved simplification was introduced. The only deliberate limitation is the accepted Computation-only family boundary; unsupported family requests fail closed and leave provider paid-history state uninitialized.
