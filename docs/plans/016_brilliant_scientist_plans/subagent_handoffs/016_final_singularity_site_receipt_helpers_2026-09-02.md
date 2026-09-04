# Event 016 Singularity physical-site receipt helpers — 2026-09-02

## Status

The bounded private site-receipt helper tranche is implemented in four new source/documentation files and one new handoff-owned constants file.

No existing decision, event, on-action, terminal, GUI, map, asset, cost, duration, AI, or gameplay file was edited.

No commit or staging was performed because the parent explicitly requested no commit for this tranche.

The parent must wire the state-targeted construction decisions and lifecycle consumers before these helpers affect runtime behavior.

## Owned files

- `common/scripted_effects/016_brilliant_scientist_singularity_site_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_singularity_site_effects.md`
- `common/scripted_triggers/016_brilliant_scientist_singularity_site_triggers.txt`
- `common/script_constants/016_brilliant_scientist_singularity_site_constants.txt`
- This handoff.

## Exact interface contract

All effects run in the receipt-owning COUNTRY scope.

All state selection uses the regular event target `brilliant_scientist_singularity_site_selected_state`.

The selected role is temporary `brilliant_scientist_singularity_site_selected_role` and must equal the existing `brilliant_scientist_singularity_component.command_core` or `.power_link` constant.

The selected quantity is temporary `brilliant_scientist_singularity_site_selected_quantity` and is fixed to integer `1` per paid completion, allowing multiple rows at the same state.

### Start / reservation

`brilliant_scientist_singularity_site_reserve_construction` validates the selected state pointer, current ownership/control, actual qualifying facility level, role, quantity, receipt-array alignment, and absence of any pending flag, metadata, or pending row.

On success it appends one aligned row with the exact state scope, role, quantity `1`, status `pending`, and history `none`.

The effect stores the row index and exact state pointer in the pending metadata and sets `brilliant_scientist_singularity_site_pending`.

Temporary output `brilliant_scientist_singularity_site_reservation_applied` is `1` only when a row was appended.

The effect owns no payment, factory occupation, timer, project stage, or reward.

### Commit / completion

`brilliant_scientist_singularity_site_complete_pending_construction` requires the same selected state event target and temporary role that the parent bound to the timer callback.

Its `brilliant_scientist_singularity_site_pending_callback_is_valid` guard first requires the pending flag, aligned row, exact state pointer, exact role, and fixed quantity through `brilliant_scientist_singularity_site_pending_callback_matches_receipt`, then requires a currently owned-and-controlled intact qualifying facility.

On success it snapshots the row index, clears pending flag and metadata before changing output state, marks that row `live`, marks durable row history `constructed`, reconciles live counters, and sets temporary `brilliant_scientist_singularity_site_completion_applied = 1`.

The parent awards the existing result only after observing that completion output.

An invalid, stale, duplicate, captured, destroyed, or wrong-role callback is a no-op and awards nothing.

### Cancel

`brilliant_scientist_singularity_site_cancel_pending_construction` accepts any pending flag, metadata, or pending row even when the selected state is already captured or destroyed.

It clears pending metadata first, then removes all pending rows from every aligned array using a tail loop, and reconciles counters.

No pending row receives constructed history and no completion output is produced.

Temporary output `brilliant_scientist_singularity_site_cancellation_applied` is `1` whenever pending state was consumed.

When arrays are malformed, metadata is still cleared and reconciliation fails closed, but row removal is skipped to avoid pairing values from different arrays; a future bounded migration must repair malformed pre-existing data without erasing durable history.

### Invalidate selected state / row

`brilliant_scientist_singularity_site_invalidate_selected_state` accepts a selected state pointer without requiring current ownership/control, cancels a matching pending row, and marks every live row at that state `invalidated`.

`brilliant_scientist_singularity_site_invalidate_selected_row` additionally accepts temporary `brilliant_scientist_singularity_site_selected_row_index` plus temporary marker `brilliant_scientist_singularity_site_selected_row_index_supplied = 1`, and marks only the exact aligned live row invalidated.

The row query rounds a temporary copy with documented `round_temp_variable` and rejects fractional indices before indexed access; the supplied marker rejects missing input rather than allowing an absent value to default to row zero.

Both preserve quantity and constructed history, clear their live contribution through reconciliation, and return temporary `brilliant_scientist_singularity_site_invalidation_applied = 1` only when a live row changed.

Use state-wide or exact-row invalidation only for an explicit destruction/disarmament receipt.

For ordinary capture/control loss, call reconciliation without invalidation so an intact row can contribute again after the original state is recovered.

### Query / reconciliation

`brilliant_scientist_singularity_site_receipt_arrays_are_aligned` checks all five parallel arrays.

`brilliant_scientist_singularity_site_selected_input_is_valid` validates a parent start input and current physical facility.

`brilliant_scientist_singularity_site_pending_callback_matches_receipt` validates only exact delayed identity: pending flag, aligned pending row, selected state pointer, selected role, and fixed quantity `1`. It remains usable for owner cancellation after capture or facility loss.

`brilliant_scientist_singularity_site_pending_callback_is_valid` composes that identity query with current physical validity and is the completion guard.

`brilliant_scientist_singularity_site_current_live_quantities_are_rebuildable` initializes temporary command and power quantities to zero and scans only aligned registered rows with `all_of`, `if`, and `add_to_temp_variable`.

An aligned empty ledger returns a valid zero reconstruction; an unaligned ledger returns false.

`brilliant_scientist_singularity_site_has_minimum_live_network` applies the existing two-node and two-power-link thresholds to the temporary reconstruction without persistent writes.

`brilliant_scientist_singularity_site_reconcile_receipts` writes the existing display counters from the reconstruction and sets the existing live-network flag only when both thresholds are met.

`brilliant_scientist_singularity_site_retire_all` cancels pending state, changes live or invalidated rows to retired, preserves all durable row history, and reconciles the legacy counters and network flag to zero.

## Ledger and physical predicates

The aligned arrays are `brilliant_scientist_singularity_site_state_entries`, `...role_entries`, `...quantity_entries`, `...status_entries`, and `...history_entries`.

Status constants are `none = 0`, `pending = 1`, `live = 2`, `invalidated = 3`, and `retired = 4`.

History constants are `none = 0` and `constructed = 1`.

Roles reuse `brilliant_scientist_singularity_component.command_core` and `.power_link`; no private duplicate role IDs were introduced.

Live quantities are rebuilt from rows whose status is live, whose role is one of the two existing component roles, whose quantity is exactly `1`, and whose stored state still satisfies the physical predicate.

The physical predicate enters a state from one country scope and requires `scope_exists = yes`, nonzero state, `is_owned_and_controlled_by = PREV`, and an actual positive `land_facility`, `air_facility`, `nuclear_facility`, or `biowarfare_facility` level.

The predicate does not use `exists = yes`, state flags, a generic destroyed flag, or old country counters.

`PREV` is deliberate because an on-action callback may have a different `ROOT` participant; parent callers must preserve the one-level country-to-state scope contract.

The existing three-distinct-facility predicate `brilliant_scientist_has_required_singularity_facilities` remains parent-owned for arming and terminal readiness, and this helper does not write its audit flag.

## Named source scenarios

| Scenario | Helper result |
| --- | --- |
| Valid start at an owned, controlled state with an actual qualifying facility | One pending row, one reservation output, no live-counter change. |
| Second start while pending | No append and no payment-owned output because pending receipt presence blocks reservation. |
| Same-state second paid completion after first commit | A second independent row is allowed; no one-per-state restriction is introduced. |
| Timer callback with wrong state target or role | Pending callback guard fails; no clear, live status, history, or reward. |
| Native cancel callback after state loss with matching state/role/quantity | Identity-only callback trigger passes even though physical validity fails; the native caller may then invoke authoritative cancellation. |
| Native cancel callback with wrong state or role | Identity-only callback trigger fails; the native caller must not invoke cancellation, so a newer receipt cannot be cleared by a stale callback. |
| Timer callback after capture or facility loss | Current physical guard fails; no completion; parent can invoke cancellation. |
| Valid callback | Pending metadata clears first; exact row becomes live and constructed; counters rebuild from physical state. |
| Cancel after capture, annexation, or facility destruction | Pending state clears without requiring ownership/control; no constructed history is created. |
| Ordinary capture followed by reconciliation | Live row contributes zero while unavailable and can contribute again when the same intact state is recovered. |
| Explicit destruction or disarmament receipt | Selected state or exact row becomes invalidated and cannot auto-resurrect after reacquisition. |
| Partial loss with duplicate same-state rows | Exact-row invalidation removes only the selected row's contribution. |
| Whole-state destruction with duplicate same-state rows | State-wide invalidation marks every live row at that state invalidated. |
| Terminal retirement | Pending state is cancelled; live and invalidated rows become retired; quantity/history remains durable; counters and network flag clear. |
| Repeated completion, cancellation, invalidation, or retirement callback | No duplicate reward or status transition; reconciliation is deterministic. |
| Unaligned arrays | Read query returns false and reconciliation clears legacy counters/network; pending row surgery is skipped. |
| Empty aligned arrays | Read query returns true with zero rebuilt quantities; minimum network gate fails. |
| Negative/zero/non-one quantity input | Reservation rejects it before any parent payment step. |
| Pending row with invalid role or quantity other than one | Structural pending-row and callback-identity queries fail closed; no completion or callback cancellation is authorized. |
| Missing or fractional selected row index | Supplied-marker or rounded-copy check fails before indexed row access; no exact-row invalidation occurs. |

## Parent integration map

The parent should convert both existing construction decisions to bind a real state target and temporary role/quantity before calling reservation.

The parent should charge existing costs only after `reservation_applied = 1` and should preserve the frozen duration and AI baseline.

The parent should rebind the same state target and role for the native timer callback, call completion, and award the existing construction output only on `completion_applied = 1`.

The native decision must evaluate `brilliant_scientist_singularity_site_pending_callback_matches_receipt` before calling cancellation, preventing a stale callback with the wrong state or role from clearing a newer receipt. The cancellation effect itself remains authoritative owner cleanup and is deliberately ungated so capture, annexation, facility loss, and terminal cleanup can consume orphaned state without a live physical target. Owner cleanup must never use the identity guard as a substitute for ownership scope.

The parent should call cancellation from native cancel callbacks and from bounded owner cleanup, never by reconstructing a state from a country counter.

The parent should call reconciliation on ordinary state capture/control changes and use explicit state/row invalidation only when a proven destruction or disarmament receipt exists.

The parent should combine the existing three-distinct-facility predicate with the live-network query or reconciled counters at arming, fail-deadly, and final-commit boundaries.

The parent should call terminal retirement after existing final-result settlement while preserving the shared final-commit capitulation failsafe.

No call site was changed in this tranche.

## Source evidence

Binding specification: `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`, terminal subsection requiring current owned-and-controlled qualifying facilities, physical site/role/quantity receipts, and separate permanent history.

Binding audit: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_terminal_current_review_2026-09-02.md`, T1 identified the country-only construction counters at `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1354-1360`, the existing facility audit at `:1338-1352`, and the uncalled destruction helper at `:1320-1336`.

Current inspected source hashes were `common/scripted_effects/016_brilliant_scientist_project_effects.txt` SHA256 `6406E3E8087CD475193A6CA470A81F2976E889A6831098897B9AD334CBA349D1`, `common/decisions/016_brilliant_scientist_directorate_project_board.txt` SHA256 `6D58F497F4CB2E76537B15904ACB51B75B117AF0319259CB5F87D7A6B94F596B`, `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt` SHA256 `5B82CB6B8A816DB6039F7EAB08637CA62C9FBE667487E140DDD11A89216A05E8`, and `common/script_constants/016_brilliant_scientist_constants.txt` SHA256 `ADFEE7FE6093933C394C34C8A6A162795D4BDB4575512C476B417C1173B6E4A6`.

Repository pointer and aligned-array precedents include `common/scripted_effects/006_independence_wave_decision_effects.txt:620-621,670-672`, `common/scripted_effects/006_independence_wave_effects.txt:1031-1052`, `common/scripted_effects/006_independence_wave_effects.txt:1089-1099`, and `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:1541`.

Required vanilla documentation was read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`, including `add_to_temp_variable` at `:713-725`, `all_of` at `:1036-1049`, `if` at `:5166-5174`, `round_temp_variable` at `:7440-7448`, `set_temp_variable` at `:7482-7500`, `scope_exists` at `:7450-7468`, `is_controlled_by` at `:5381-5388`, `is_owned_by` at `:6088-6095`, and `is_owned_and_controlled_by` in the same ownership section.

Required offline Paradox wiki core pages and relevant State and Building modding pages were consulted before source work.

## Bounded map inspection

The mandatory narrow map inspection used workspace `mod_chaos_redux_ea3b2d67c2c0` and state IDs `64`, `70`, and `1`.

MCP result was `status = ok`, `code = MAP_INSPECTED`, and `inspectedStateCount = 3`.

Artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b616cc8563f42cca259f15810a089158264e9f16024a35d8f809debf8e40ac0/825230da3a69737bd8d6a06837c5c2232e1103a2b0fe2aa73fff8427da8b6f92/map-inspect.d64d08d1b4ec7e58ef39ed16e46d65316fb9307164e4ada7f9b1b0f04916d790`.

Artifact SHA256 is `6b616cc8563f42cca259f15810a089158264e9f16024a35d8f809debf8e40ac0` and map revision is `d64d08d1b4ec7e58ef39ed16e46d65316fb9307164e4ada7f9b1b0f04916d790`.

Vanilla state history identifies state 64 as Brandenburg with a positive `land_facility = 1` representative at province 3499, while states 70 Slovakia and 1 France provide negative static-history examples for this narrow qualifying-facility check.

The map artifact also returned unrelated existing building-position and floating-harbor adjacency diagnostics.

This is source/map evidence only and is not an engine acceptance claim.

## Validation and limits

The new scripts were inspected after writing, and the helper/trigger braces and forbidden operator patterns are being checked with bounded repository commands.

No HOI4 engine launch, log inspection, event rendering, live map mutation, or user-owned live-game acceptance was performed.

No probability or weighted surface was changed, so no probability inspection was applicable to this helper-only tranche.

No no-DLC construction/presentation claim is made here; the parent owns decision exposure and no-DLC evidence.

The fixed one-per-paid-row quantity is the current contract for the one-component paid completion shape, not a balancing simplification; malformed, fractional, or arbitrary quantity input is rejected.

The parent remains responsible for wiring all existing callers, state destruction consumers, lifecycle hooks, CXT setup, localisation, terminal gates, and final runtime acceptance.
