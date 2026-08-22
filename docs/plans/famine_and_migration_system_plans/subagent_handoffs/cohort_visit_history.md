# Cohort Visit History Ledger Handoff

## Scope and ownership

This tranche adds a sparse, aligned global receipt ledger for exact famine and migration cohort visits.

The ledger proves A→B→A and any later repeated-state visit without touching population, the Deaths ledger, the live cohort row, event IDs, event pools, pacing pulses, mapmodes, GUI, localisation, decisions, on_actions, or workbook data.

Only the following new files are owned by this tranche: `common/scripted_effects/famine_migration_cohort_history_effects.txt`, `common/scripted_triggers/famine_migration_cohort_history_triggers.txt`, and this handoff.

The parent remains responsible for callsite wiring, dynamic-effect documentation, and final cross-system validation.

## Helper map

| Identifier | Scope | Inputs | Outputs | Side effects |
| --- | --- | --- | --- | --- |
| `famine_migration_initialize_cohort_history` | Any | None | None | Sets `famine_migration_cohort_history_initialized` once and derives a missing history count from the existing ID-array length without clearing or rewriting either history array. |
| `famine_migration_cohort_history_arrays_are_aligned` | Any trigger | None | Boolean | Requires equal history ID/state lengths and `global.famine_migration_cohort_history_count` equal to that length. |
| `famine_migration_cohort_history_live_ledger_arrays_are_aligned` | Any trigger | None | Boolean | Requires all eight existing live cohort arrays and `global.famine_migration_cohort_count` to align, then requires the history arrays to align. |
| `famine_migration_record_cohort_history_visit` | State | Positive temporary `famine_migration_cohort_history_id_request`; `THIS` is the actual state being recorded. | Temporary `famine_migration_cohort_history_record_result`, `..._cycle_result`, `..._append_result`, and `..._alignment_result`. | Appends one aligned ID/state receipt when the newest receipt is a different state; calls the existing achievement failure effect in the exact persisted owner country on a prior-state revisit; clears the one-shot request. |
| `famine_migration_cleanup_cohort_visit_history` | Any | Positive temporary `famine_migration_cohort_history_id_request`. | Temporary `famine_migration_cohort_history_cleanup_result`, `..._removed_count`, and `..._alignment_result`. | Removes every matching history row by descending aligned index, preserves all other cohorts and their relative order, updates the history count, and clears the one-shot request. |

The record result uses `constant:famine_migration_route_result.valid` for an accepted append or valid no-op and `invalid` for a missing row, invalid state, invalid owner/host, duplicate live ID, or broken alignment.

The record cycle output is `one` only when a new state differs from the newest receipt and an older receipt for the same cohort and exact state exists.

The record append output is `one` for the first receipt or a new-state receipt and `zero` for a consecutive duplicate no-op.

The cleanup result is valid when the explicit positive request and aligned history arrays are valid, including the intentional no-op where the requested ID has no receipts; `..._removed_count` remains zero in that case.

## Storage and invariants

The new global arrays are `global.famine_migration_cohort_history_ids` and `global.famine_migration_cohort_history_states`.

For every valid save, `global.famine_migration_cohort_history_ids^num = global.famine_migration_cohort_history_states^num = global.famine_migration_cohort_history_count`.

Array index is append order, so removing rows by the same descending index from both arrays preserves the relative order of all remaining visits without a separate sequence array.

Each append performs exactly one `add_to_array` on each aligned array at the end and then derives the count from the ID-array length.

Each cleanup removes both aligned entries at the same index and derives the count from the remaining ID-array length.

The record trigger also requires every existing live cohort array to align with `global.famine_migration_cohort_ids^num` and requires `global.famine_migration_cohort_count` to match that length.

The record scans all live rows to reject an absent ID and to reject a duplicated live ID rather than choosing an ambiguous owner.

The record scans only history rows belonging to the requested ID and reads the newest matching row by descending index.

The cycle formula is `append_target_state != newest_recorded_state AND an earlier same-cohort receipt has append_target_state`.

The consecutive-duplicate formula is `newest_recorded_state = append_target_state AND live_host = append_target_state`; it returns valid with `append_result = 0` and `cycle_result = 0`.

The first receipt is a special seed case: when the cohort has no history rows, the true origin can be appended even though the live host is also the origin.

No fixed cohort total, population estimate, state-owner inference, random state, province, country, or world enumeration is used.

## Alignment failure and diagnostics

The read-only alignment triggers fail closed when either history array length differs, when the history count differs, when any live array length differs, or when the live count differs.

The effects set persistent `famine_migration_cohort_history_alignment_broken` when a required alignment trigger fails and never repair mismatched arrays by inventing values.

The record also preserves explicit diagnostics for duplicate live IDs, invalid live rows, invalid stored history state scopes, and a host/history mismatch through the flags `famine_migration_cohort_history_duplicate_live_id`, `famine_migration_cohort_history_live_row_invalid`, `famine_migration_cohort_history_invalid_state_scope`, and `famine_migration_cohort_history_host_mismatch`.

Those diagnostic flags are evidence only; the helper does not clear them or treat an old diagnostic flag as a reason to block a later independently valid row.

## Owner and state scope contract

The record receives the actual state in `THIS` and saves it as the regular effect-chain target `famine_migration_cohort_history_request_state`.

The live row is located only by the explicit positive ID in `famine_migration_cohort_history_id_request` against `global.famine_migration_cohort_ids`.

The owner is loaded from `global.famine_migration_cohort_owners` at that exact live-row index and saved as the regular target `famine_migration_cohort_history_owner`.

On a cycle, the helper invokes `famine_migration_achievement_record_transfer_cycle_failure = yes` inside that owner target and never derives a country from `OWNER`, `CONTROLLER`, or ownership of the visited state.

The live host is checked from the aligned `global.famine_migration_cohort_hosts` row and is used only to recognize a duplicate or an inconsistent newest receipt.

The regular event targets are intentionally short-lived and therefore require no global-target cleanup.

The one-shot request must be a temporary variable set immediately before the call; the helper clears it at the end with `set_temp_variable` and does not clear a durable caller variable.

## Parent callsite patch list

### Cohort creation and origin seed

After each successful `famine_migration_record_displaced_cohort = yes`, set `famine_migration_cohort_history_id_request = famine_migration_cohort_id_result` and call `famine_migration_record_cohort_history_visit = yes` inside the true origin state scope.

The shared creation effect begins at `common/scripted_effects/chaosx_famine_migration_effects.txt:50`, and the four request adapters currently call it near lines `3798`, `3830`, `3866`, and `3902`.

The owner must be the same owner proof used by the live row, and the first receipt must be the true origin before any destination receipt is submitted.

Decision-owned creation after a successful exact transfer must still call the history helper in `event_target:famine_migration_transfer_origin` so the origin is not accidentally replaced by the destination state.

The initial destination slot in the live row remains the existing origin placeholder under `active`; the history helper does not reinterpret that placeholder as a visit.

### Successful regular transfer

The narrowest shared insertion point is `common/scripted_effects/chaosx_famine_migration_effects.txt:1300`, inside `event_target:famine_migration_route_destination` immediately before `famine_migration_update_cohort_host_after_transfer = yes`.

Call the history helper only after `famine_migration_transfer_civilians_exact` has returned valid conservation and the destination credit is the actual positive survivor credit.

Set the history request from the explicit cohort ID already carried by the transfer request, use the actual destination scope as `THIS`, and call the helper before the live host overwrite so the old host remains available for duplicate/order reasoning.

If a caller creates a cohort only after the transfer, the creation seed is separate and the destination bind/arrival path must submit the first destination receipt after the exact transfer succeeds.

The helper must not be called on a rejected route, a conservation residual, a zero survivor credit, or a destination selected only as a candidate.

### Safe resettlement rebind

The shared rebind effect begins at `common/scripted_effects/chaosx_famine_migration_effects.txt:218`, with decision consumers near `common/decisions/famine_migration_decisions.txt:2322`, `2456`, and `2847`.

When the safe rebind represents an accepted cohort move into the actual new destination, call the history helper in that destination scope after the rebind proof and accepted transaction are valid.

If an exact transfer already recorded the same destination in the same effect chain, the second call is an intentional no-op; it must not be treated as a second visit or cycle.

If the rebind is merely a route-target preparation before an exact transfer, defer the history call until the exact transaction succeeds.

The rebind must preserve the live owner, origin, survivor amount, and status; the history helper only records the destination state and does not duplicate the resettled population.

### Safe and forced destination binds

The safe bind begins at `common/scripted_effects/chaosx_famine_migration_effects.txt:107` and the forced bind begins at `:163`.

The current safe-bind destination consumers are near `common/decisions/famine_migration_decisions.txt:1427`, `1573`, and `1727`.

Submit the actual destination receipt after the accepted exact transfer or accepted host transition, not when a destination candidate is merely saved.

For an initial cohort that has no destination receipt yet, the bind destination becomes the next receipt after the origin seed.

For a forced bind, preserve the unsafe status and use the same explicit cohort ID; forced status is not permission to infer a state or bypass conservation.

### Voluntary return and later repeats

The voluntary-return preparation begins at `common/scripted_effects/chaosx_famine_migration_effects.txt:1747`, with exact-return consumers near `common/decisions/famine_migration_decisions.txt:2557` and `3121` and exact transfer blocks near `:2581` and `3169`.

After a valid return transfer reaches the persisted origin state and before any host overwrite or row removal, submit the origin state with the same cohort ID.

For A→B→A, the sequence is origin seed A, successful transfer receipt B, and successful return receipt A; the third receipt returns `cycle_result = 1` and calls the exact persisted owner achievement hook.

The same rule catches later A→B→C→B or any other repeated state, not only the original origin.

### Every row-removal path

Before the zero-survivor branch removes all eight live arrays in `famine_migration_update_cohort_host_after_transfer` near `:1500`, set the explicit row ID and call `famine_migration_cleanup_cohort_visit_history = yes`.

Before normal resolution removes a live row through `famine_migration_cleanup_cohort_record` at `:357`, call the history cleanup with the same ID; the current decision cleanup consumers are near `common/decisions/famine_migration_decisions.txt:2595`, `2706`, `2868`, `3013`, and `3185`.

The cleanup helper may also run after a live row has already disappeared because it validates only the history arrays, but calling it before the live removal makes the lifecycle evidence explicit.

Before each matching row is removed by `famine_migration_cleanup_cohort_records_for_state` at `:395`, capture that row's `global.famine_migration_cohort_ids^famine_migration_cohort_cleanup_index`, set the history request, call cleanup, and then remove every aligned live array at the same index.

The state invalidation path must repeat this per matching cohort ID and must not clear the entire history ledger.

Use a caller-local row-ID variable distinct from the helper's `famine_migration_cohort_history_cleanup_*` variables because temporary variables are unscoped across nested effects.

Normal resolution, zero-survivor removal, explicit cleanup, and state invalidation must all remove every receipt for exactly one ID and never another cohort's rows.

## Migration plan

No existing live cohort array is changed by this tranche, so existing save rows remain valid and no population migration or backfill is required.

The parent should wire the origin seed and transaction-time receipts first, then add cleanup calls before any main-row removal.

Existing rows from a save created before this ledger was wired have no fabricated history; their first explicit successful receipt seeds the state actually observed at that callsite.

A whole-world backfill is intentionally not permitted because it could not recover exact visit order without an authoritative transaction record.

The helper uses the existing constants `famine_migration_runtime.zero`, `.one`, and `.array_index_increment`, `famine_migration_route_result.invalid` and `.valid`, and the existing active/destination-bound/unsafe cohort status values.

No new script-constants file is needed.

## Dynamic helper documentation insertion

The parent must add the public API documentation to `common/scripted_effects/chaosx_dynamic_effects.md` in the existing `## Border, reception, return, and cohort contracts` section.

Insert the new history-ledger paragraph immediately after the current paragraph ending `State selection is authoritative for host decisions; the country selection is only a bounded owner-side convenience and is cleared on zero or ambiguous rows.` at the current area around line `745`, and before the `famine_migration_set_border_policy` paragraph.

The documentation must list the initializer, both alignment triggers, record inputs/outputs, cleanup inputs/outputs, diagnostic flag, exact-owner achievement side effect, no-population guarantee, append/no-op/cycle formulas, and all lifecycle callsites.

The dynamic docs table of contents currently lists the broader cohort-contract section rather than individual effect anchors, so no new top-level section is required unless the parent chooses to add one.

## Validation evidence

The offline Paradox wiki pages for data structures, event targets, arrays, triggers, effects, variables, scopes, on actions, localisation, modifiers, event modding, decision modding, idea modding, and AI modding were read before implementation.

Vanilla documentation for arrays, `add_to_array`, `remove_from_array`, `while_loop_effect`, `save_event_target_as`, `set_temp_variable`, `set_variable`, `check_variable`, `has_variable`, variable scopes, script constants, and `var:` scope usage was read before implementation.

Repository aligned-array precedents in `common/scripted_effects/006_independence_wave_effects.txt`, `006_independence_wave_rival_bloc_effects.txt`, and `014_cannibalism_effects.txt` were inspected and the descending same-index removal pattern was reused.

Static validation confirmed equal brace counts in the new effect file (`177/177`) and trigger file (`12/12`), no unsupported `<=` or `>=` operators, and no accidental uppercase constant token after review.

The add/no-op/revisit/later-repeat cases were checked symbolically against the append and descending cleanup branches.

The multi-row cleanup case was checked with interleaved cohort IDs to ensure only matching IDs are removed and both arrays remain aligned.

The alignment-failure case was checked to leave arrays untouched, return invalid outputs, and set `famine_migration_cohort_history_alignment_broken`.

The dynamic array references use the existing repository/vanilla `global.array^temporary_index` and `var:global.scope_array^temporary_index` forms; no unsupported string-built index or dynamic effect name was introduced.

No MCP probability, GUI, map, focus, event, or weighted-logic route was used because this tranche changes no such surface.

No Hearts of Iron IV runtime was launched, and no parent callsite or live-save integration was claimed in this handoff.

## Limitations and blockers

The new files intentionally contain no parent callsites because existing gameplay files are outside this subagent's ownership.

The dynamic-effect documentation is intentionally not edited here because the parent owns that existing file; the exact insertion point and required content are recorded above.

The two dedicated famine/migration mapmodes are intentionally untouched; this tranche supplies no map projection and does not add a third mapmode.

No backfill can prove visits that occurred before the first explicit history call, so the parent must wire the origin seed and every successful transaction receipt before claiming complete cycle coverage.

Runtime parser and live-save validation remain parent-owned because this subagent cannot launch the game and has not altered the core transaction file.

Overall famine/migration system completion is not claimed by this handoff.
