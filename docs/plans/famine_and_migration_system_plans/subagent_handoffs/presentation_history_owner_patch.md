# Presentation and ordinary-history owner patch

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Status: bounded implementation and source audit complete; no commit was made.

This tranche preserves the frozen atomic transfer transaction and adds only presentation receipt integration, presentation cleanup, and ordinary hosted-destination visit-history eligibility. The famine food lifecycle and the migration cohort/transfer lifecycle remain separate mechanics connected only through the existing explicit refresh and state-registration seams.

## Changed files and identifiers

- `common/scripted_effects/chaosx_famine_migration_effects.txt`: `famine_migration_finalize_exact_transfer`, `famine_migration_preflight_exact_transfer`, `famine_migration_request_organized_evacuation`, `famine_migration_evaluate_voluntary_return`, `famine_migration_force_return_cohort`, `famine_migration_cleanup_route_request`, `famine_migration_clear_dynamic_modifiers`, and `famine_migration_cleanup_state_registration`.
- `common/scripted_triggers/chaosx_famine_migration_triggers.txt`: `famine_migration_state_has_migration_obligations` and `famine_migration_terminal_state_references_clear`.
- `common/scripted_effects/famine_migration_presentation_effects.txt`: the six exact projection record APIs, six role-specific clear APIs, `famine_migration_presentation_clear_all_projections`, and the ten-phase refresh contract are wired as the presentation API surface.
- `common/scripted_effects/famine_migration_destination_selection_effects.txt`: `famine_migration_destination_selection_prepare_history_exclusion` and the two-pass `famine_migration_destination_selection_run_weighted_pool` history guards.
- `common/scripted_triggers/famine_migration_destination_selection_triggers.txt`: `famine_migration_destination_selection_history_candidate_is_allowed` is included in `famine_migration_destination_selection_candidate_is_valid`.
- `common/scripted_effects/famine_migration_decision_owner_effects.txt` and `.md`: `famine_migration_decision_preflight_destination_history` is a read-only positive-match guard, and the new-origin organized owner records its exact organized projection.
- `common/scripted_effects/famine_migration_corridor_effects.txt`: `famine_migration_prepare_corridor_contract` records exact preparing input and `famine_migration_corridor_cleanup` clears only preparing/organized role receipts.
- `common/decisions/famine_migration_decisions.txt`: `fm_distribute_arrivals` and `fm_transit_only` enable the same ordinary-history requirement around shared selector calls; AI `ai_will_do` values and decision numeric weights are unchanged.
- `common/scripted_effects/chaosx_dynamic_effects.md`: documents the central finalizer seam, paired-array history bridge, ordinary exceptions, and cleanup ownership.

The spontaneous and forced movement files retain their existing calls to the atomic wrapper. Their presentation receipts are emitted centrally by `famine_migration_finalize_exact_transfer`, so no per-lane duplicate presentation call was added.

## Ten-phase producer and clear table

| Phase | Exact producer or derivation | Exact metadata and denominator | Clear/lifecycle boundary |
| --- | --- | --- | --- |
| Preparing to leave | `famine_migration_request_organized_evacuation` and `famine_migration_prepare_corridor_contract` record the exact request or corridor amount before a cohort is necessarily present. | `people = displacement_request_amount` or `famine_migration_corridor_transfer_people`; `denominator = round(state_population_k * constant:chaos_meter_deaths.people_per_k)`; generation is the initialized transfer generation or exact corridor route generation; role is organized evacuation; cohort is omitted/zero unless the corridor already has one. | Request failure clears preparing; corridor cleanup clears preparing and organized; successful organized execution clears both at the finalizer terminal. |
| Active exodus | Existing refresh derives it only from the equal positive flight pair and active displacement proof. | `people` is the equal live `famine_migration_flight_pressure`/`famine_migration_state_flight_population` pair; denominator is the current rounded state population in people units. | No projection receipt; each authoritative flight refresh rebuilds it. |
| Organized evacuation | `famine_migration_request_organized_evacuation` and `famine_migration_decision_execute_new_origin_organized_evacuation` record the exact prepared/request amount after the cohort ID is proven. | Exact people amount, current rounded state denominator, positive cohort ID, current transfer generation, and organized-evacuation role. | Invalid new-origin staging clears preparing and organized; successful finalization clears both exact role receipts. |
| Depopulated districts | The shared finalizer calls `famine_migration_presentation_record_depopulated_projection` immediately after a valid `famine_migration_record_transfer_projection`. | `people = famine_migration_transfer_actual_origin_debit`; `denominator = famine_migration_transfer_origin_population_before`; cohort is the final cohort ID; generation is `global.famine_migration_transfer_generation`; role is the final transfer role. | Durable receipt survives ordinary cleanup and is cleared only by `famine_migration_presentation_clear_all_projections` at complete state-history retirement/reset. |
| Reception | Existing refresh derives the live reception load after exact reception settlement. | `people = famine_migration_state_reception_load`; denominator is the current rounded state population in people units. | No projection receipt; rebuilt from the live reception ledger. |
| Overcrowded reception | Existing refresh derives the live reception load only under the validated overcrowding context. | Same exact live reception load and current rounded state denominator; no synthetic capacity deficit is used as people. | No projection receipt; rebuilt from live reception/capacity context. |
| Trapped population | Existing refresh derives the exact trapped ledger. | `people = famine_migration_state_trapped_population`; denominator is the current rounded state population in people units; route deaths remain separate. | No projection receipt; rebuilt from the live trapped ledger. |
| Transit | The shared finalizer records destination transit only for a positive survivor transfer with a positive destination post-credit population. | `people = famine_migration_transfer_survivor_credit`; `denominator = famine_migration_transfer_destination_population_after`; final cohort ID, global transfer generation, and transit role. | The origin transit receipt is cleared on transit/resettlement/return finalization; the hosted destination receipt remains until the cohort's next exact terminal or complete state-history retirement. |
| Return readiness | `famine_migration_evaluate_voluntary_return` and `famine_migration_force_return_cohort` record the exact resolved cohort amount before the return transaction. | `people = famine_migration_cohort_resolved_amount`; `denominator = round(host_state_population_k * constant:chaos_meter_deaths.people_per_k)`; requested cohort ID, current transfer generation, and voluntary-return or forced-return role. | Cleared on the corresponding return finalizer or route-request cleanup; no ordinary destination-history gate is applied to these return lanes. |
| Resettlement/return | The shared finalizer records destination survivor credit for resettlement, voluntary return, and forced return only when survivor credit and destination post-credit population are positive. | `people = famine_migration_transfer_survivor_credit`; `denominator = famine_migration_transfer_destination_population_after`; final cohort ID, global transfer generation, and the exact resettlement/return role. | Durable receipt survives ordinary cleanup and is cleared only by complete state-history retirement/reset. |

Every non-live receipt is recorded only from an exact positive people/denominator pair and exact generation/cohort/role metadata. The presentation share is `clamp(people / denominator, 0, 1)`. No receipt changes population, reception, Deaths, cohort rows, history arrays, route targets, or rewards.

## Central cumulative depopulation

`famine_migration_finalize_exact_transfer` is the only presentation depopulation callsite outside the record API definition. It calls `famine_migration_record_transfer_projection` first and proceeds only on its valid receipt.

For a valid transfer, let `D = famine_migration_transfer_actual_origin_debit`, `N_origin = famine_migration_transfer_origin_population_before`, `S = famine_migration_transfer_survivor_credit`, and `N_destination = famine_migration_transfer_destination_population_after`. The cumulative depopulated receipt adds `D / N_origin` to its exact people/denominator projection, accepts each positive generation only when `generation > famine_migration_presentation_depopulated_projection_last_generation`, preserves the first positive `N_origin` as its cumulative denominator, and records the latest exact cohort/generation/role. A replayed generation adds nothing. An all-death transfer still has positive `D`, positive `N_origin`, a valid generation, and therefore records depopulation once; `S <= 0` prevents any destination transit or resettlement/return receipt. Route deaths are never substituted for `D` or `S`.

The five missing presentation modifier removals are now in `famine_migration_clear_dynamic_modifiers`: preparing, organized evacuation, depopulated districts, transit, and return readiness. `famine_migration_presentation_clear_state` still removes all ten derived presentation modifiers before refresh, while the role-specific clears remove only their own receipts.

## Ordinary history proof

`fm_distribute_arrivals` and `fm_transit_only` set `famine_migration_destination_selection_history_required = 1` around their shared destination selector and reset it immediately afterward. Return, forced movement, local integration, and third-country resettlement do not set this requirement.

`famine_migration_destination_selection_prepare_history_exclusion` is a bounded state-scope paired-array bridge. It requires a positive current cohort ID, the initialized positive global history count, `famine_migration_cohort_history_arrays_are_aligned`, and `famine_migration_cohort_history_live_ledger_arrays_are_aligned`. It loops the aligned history IDs and states, increments a match count for every matching cohort ID, appends every matching valid state scope to `famine_migration_destination_selection_history_states`, and marks the contract invalid if a matching state scope is invalid. The contract succeeds for a positive match count, not exactly one, because origin plus current-host receipts and later append-only visits are legitimate. The existing history writer remains the owner of duplicate live-row detection and aligned live-row validation.

`famine_migration_destination_selection_history_candidate_is_allowed` passes when history is not required. When required, it requires a valid prepared contract and rejects `THIS` when it is in the temporary visited-state array. `famine_migration_destination_selection_candidate_is_valid` invokes this gate, and both `every_neighbor_state` passes in `famine_migration_destination_selection_run_weighted_pool` invoke that same candidate trigger. No numeric weight, random weight, or candidate scoring term changed.

After the draw binds `famine_migration_route_destination`, the selector calls `famine_migration_decision_preflight_destination_history` before writing route proofs or success. The preflight is read-only, requires initialized positive aligned history/live arrays and at least one matching receipt, and invalidates when any matching receipt's state equals the exact bound destination. Its match-count test is also positive so a normal A→B→C cohort with multiple receipts remains eligible. `famine_migration_preflight_exact_transfer` repeats this preflight immediately before the atomic wrapper can debit population for organized safe-rebind and ordinary transit safe-rebind roles, and includes the result in its all-proof gate.

Static history model proof with visited states `[A, B]`:

- A→B→C: C is absent from the exclusion array, the positive history count is valid, the post-bind destination comparison finds no C receipt, and the final preflight remains valid.
- A→B→A: A is present in the exclusion array, so both weighted passes omit it; a stale/manual bind is rejected by the post-bind and final exact-destination comparisons before any atomic mutation.
- A rejected repeat therefore performs no population debit/credit, reception change, Deaths write, cohort-row mutation, history append, presentation receipt update, achievement/reward update, or ordinary decision outcome mutation.

Missing history initialization, missing count, misaligned arrays, or invalid matching history scopes fail closed for hosted ordinary distribution/transit. The preflight does not call `famine_migration_initialize_cohort_history`, repair arrays, or backfill old saves. This preserves the no-mutation property for rejected attempts and avoids reconstructing visit order.

The explicit exceptions remain separate: persisted-origin voluntary return uses its exact return-origin resolver and resettlement rebind contract; forced return uses the forced-rebind contract; terminal local integration is a local owner operation rather than an ordinary destination selector; and third-country resettlement uses its explicit resettlement role and safe rebind. None is blocked by the ordinary history requirement or the ordinary final-preflight branch.

The human and AI surfaces for distribute-arrivals and transit-only share the same decision `remove_effect` and selector path. Their existing `ai_will_do` blocks remain unchanged, so the history rule applies to both without adding an AI-only proxy or changing probability targets.

## Famine/migration lifecycle separation audit

Food-stage lifecycle remains owned by `famine_migration_clear_food_dynamic_modifiers`, food evaluation, historical-profile context, and the food registry. That narrow food clear removes only the four food-stage modifiers and cannot erase migration presentation modifiers or migration receipts.

Migration presentation and cohort cleanup remain guarded by migration obligations. `famine_migration_state_has_migration_obligations` and `famine_migration_terminal_state_references_clear` include only transient presentation receipts (preparing, organized, transit, and return-readiness) alongside live ledgers, rows, reception, missions, and corridors; durable depopulated and resettlement/return receipts are intentionally excluded so they do not block terminal cleanup. `famine_migration_cleanup_state_registration` reaches `famine_migration_presentation_clear_all_projections` only after that exact migration-obligation predicate is empty.

The full dynamic refresh is an explicit adapter: `famine_migration_refresh_state_modifiers` first runs the existing food/context compatibility refresh and then the migration presentation refresh from exact live/projection inputs. This does not merge food and migration ledgers. Famine retirement cannot clear migration obligations because the guarded branch preserves live migration rows and receipts; migration role cleanup cannot clear famine state while a migration obligation exists because the narrow food clear is used first and the full clear is deferred to the no-obligation boundary. No mapmode, event, pulse, or cross-mechanic global scan was added.

## Old-save behavior and fallbacks

Old saves without a history registry or with missing/misaligned history fail closed for hosted ordinary distribution/transit. No history array is initialized or repaired by selection or final preflight. Existing live presentation phases continue to derive only from authoritative ledgers/context, and absent non-live receipts are not replaced with guessed people, denominators, route deaths, or reconstructed history.

Preparing is deliberately pre-cohort and may carry cohort zero. `fm_prepare_evacuation` remains a flag-only decision without an exact amount/denominator, so it does not synthesize a presentation receipt; exact request and corridor preparation seams are the producers. This is an intentional evidence boundary, not a fallback estimate.

The existing resettlement/return read-only durable-counter fallback remains available only while its exact context flags are active and does not invent a people amount. Existing idempotent refresh duplication after a destination receipt is harmless and does not alter authoritative state.

No simplification was made to the atomic transfer, survivor/all-death gates, route-death separation, cohort/history ownership, decision count, or AI numeric tuning. The only engine limitation retained is the absence of a trigger-level indexed paired-array query; the bounded temporary state-scope array bridge is used consistently in both selector passes, and no `route_unsafe` proxy is used.

## Validation and blockers

- Touched gameplay files have balanced braces and no literal unsupported `<=` or `>=` operators.
- The six record APIs and six role-specific clear APIs plus `famine_migration_presentation_clear_all_projections` were census-checked; each has its definition and expected callsites.
- `famine_migration_transfer_civilians_exact = yes` remains one executable call in the shared wrapper, and `famine_migration_finalize_exact_transfer = yes` remains one executable call. The five source wrapper lanes remain corridor, new-origin/hosted decision owner, spontaneous movement, and forced movement; the parent atomic handoff's twelve physical lanes remain routed through the shared transaction.
- Both weighted selector passes use the same candidate trigger, the positive history contract is present, the post-bind preflight is present, and the atomic final preflight repeats the ordinary history rule.
- Static A→B→C/A→B→A history evaluation produced allowed/rejected respectively, with the repeat rejected before mutation.
- Durable depopulated/resettlement flags are absent from both state obligation and terminal-reference predicates, while the four transient presentation flags remain gates. The complete no-obligation cleanup branch visibly reaches `famine_migration_presentation_clear_all_projections`.
- `famine_migration_decisions.txt` retains 34 `fm_*` entries: 26 primary decisions, 2 response decisions, and 6 missions.
- No whole-world recurring scan, event ID, event registration, pacing pulse, mapmode, scripted GUI, `route_unsafe` proxy, or numeric AI/MTTH/random-weight change was introduced.
- No Hearts of Iron IV launch was performed, as required.

The required initial weighted MCP inspection was called before editing, but the workspace reported zero available adapters/candidates. The recorded aggregate artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee5dd83f47cf589cf1de1d96b68931a20a1c349e41a3a3b97c8d143cb53ef507/096805e177cb7920a229d0a445b884edd44ab4c8f02a60e43ad27ec68ec3264f/probability-inspect-187e663a01be.json`, with source hash `187e663a01be197531391843f18b204521689d39ea0db30d8fd1f849632a3c0c`. No callable `chaosx_ai_probability_auditor` route was available. The callable `hoi4_probability_compare` route rejected the available pre/post source/hash representations at schema validation before analysis, so no post-change probability comparison artifact exists; the parent must run the valid same-scenario comparison once its captured pre-change hashes and final source representation are accepted by the route.

No gameplay or documentation work remains in this bounded ownership tranche. The probability compare schema blocker and the absence of live HOI4 execution remain external validation blockers, not source fallbacks.
