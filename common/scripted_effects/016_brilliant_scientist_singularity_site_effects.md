# Event 016 Singularity site receipt effects

This document describes the private physical-site ledger declared in `016_brilliant_scientist_singularity_site_effects.txt` and its read-only queries in `common/scripted_triggers/016_brilliant_scientist_singularity_site_triggers.txt`.

## Scope and ownership

Every effect in this file runs in the receipt-owning COUNTRY scope.

The parent decision owns Political Power, equipment or fuel payments, civilian-factory occupation, the selected state UI, timer creation, timer cancellation, and the existing completion reward.

This helper owns only the site receipt lifecycle, physical validity, live counter reconstruction, and terminal retirement.

The helper never changes construction costs, durations, AI factors, project stages, component research, or the minimum thresholds.

## Ledger schema

The five normal-variable arrays are parallel and must always have the same `^num` length.

| Array | Row value | Lifetime |
| --- | --- | --- |
| `brilliant_scientist_singularity_site_state_entries` | Persistent state scope pointer | Retained for the row lifetime |
| `brilliant_scientist_singularity_site_role_entries` | Existing `brilliant_scientist_singularity_component.command_core` or `.power_link` constant | Retained for the row lifetime |
| `brilliant_scientist_singularity_site_quantity_entries` | Fixed integer quantity `1` for one paid completion | Retained for history and row identity |
| `brilliant_scientist_singularity_site_status_entries` | `none`, `pending`, `live`, `invalidated`, or `retired` | Changes through the lifecycle |
| `brilliant_scientist_singularity_site_history_entries` | `none` or `constructed` | Durable construction history; never cleared by invalidation or retirement |

The pending receipt is held separately in `brilliant_scientist_singularity_site_pending_state`, `brilliant_scientist_singularity_site_pending_role`, `brilliant_scientist_singularity_site_pending_quantity`, and `brilliant_scientist_singularity_site_pending_row`, together with the `brilliant_scientist_singularity_site_pending` country flag.

Pending and live row shape is strict: role must be one of the two existing component roles and quantity must equal integer `1`; malformed rows are ignored by live-quantity reconstruction and cannot authorize a callback or exact-row invalidation.

The new status and history constants are in `common/script_constants/016_brilliant_scientist_singularity_site_constants.txt`.

## Physical validity

`brilliant_scientist_singularity_site_state_is_intact_and_owned` is a STATE-scope predicate entered from exactly one receipt-owning country scope.

It requires `scope_exists = yes`, a nonzero state, `is_owned_and_controlled_by = PREV`, and an actual positive `land_facility`, `air_facility`, `nuclear_facility`, or `biowarfare_facility` level.

It intentionally does not use `exists = yes`, a site flag, a generic destroyed-facility flag, or the legacy country counters.

The `PREV` contract is important for on-action and timer callers: the state block must be entered directly from the owner COUNTRY scope, because `ROOT` can refer to another participant in a callback.

The existing `brilliant_scientist_has_required_singularity_facilities` query remains the parent-owned three-distinct-facility gate for arming and terminal readiness; this ledger does not set or replace its audit flag.

## Lifecycle interfaces

### `brilliant_scientist_singularity_site_reserve_construction`

Inputs are the regular event target `brilliant_scientist_singularity_site_selected_state`, temporary `brilliant_scientist_singularity_site_selected_role`, and temporary `brilliant_scientist_singularity_site_selected_quantity = 1`.

The selected input must be an intact qualifying facility owned and controlled by the caller, must use one of the two existing roles, and must not overlap any pending flag, metadata, or pending row.

When valid and all five arrays are aligned, the effect appends one `pending` row and stores the exact row index and selected state pointer in the pending metadata.

The temporary output `brilliant_scientist_singularity_site_reservation_applied` is `1` only when the row was appended.

The effect does not charge or refund anything and does not mutate live counters.

### `brilliant_scientist_singularity_site_complete_pending_construction`

The timer callback must rebind the same selected-state event target and temporary role that were used for reservation.

`brilliant_scientist_singularity_site_pending_callback_matches_receipt` is the identity-only guard for the pending flag, aligned row, exact selected state pointer, exact role, and fixed quantity `1`; it intentionally remains usable after the state has been captured or the facility has been lost.

`brilliant_scientist_singularity_site_pending_callback_is_valid` calls that identity guard and then requires the currently intact owned-and-controlled facility at the stored state before completion.

On success the effect snapshots the row index, clears the pending flag and metadata first, marks that exact row `live`, marks its independent history `constructed`, reconciles counters, and sets temporary `brilliant_scientist_singularity_site_completion_applied = 1`.

Only after that output is `1` may the parent award the existing construction result.

An invalid, stale, duplicate, captured, destroyed, or wrong-role callback is a no-op and awards nothing.

### `brilliant_scientist_singularity_site_cancel_pending_construction`

Cancellation accepts a structurally valid or orphaned pending flag, metadata, or pending row even when the selected state is no longer owned or controlled.

The cancellation effect is authoritative owner cleanup and is intentionally not identity-gated, so bounded owner cleanup can consume an orphan after state loss. A native decision callback must first pass `brilliant_scientist_singularity_site_pending_callback_matches_receipt`; this prevents a stale callback with the wrong state or role from clearing a newer receipt.

It clears pending metadata before removing pending rows and removes every pending row from all five aligned arrays by a tail loop.

No row receives `constructed` history and no completion output is produced.

The temporary output `brilliant_scientist_singularity_site_cancellation_applied` is `1` when any pending receipt state was consumed.

If arrays are already malformed, the metadata is still cleared and reconciliation fails closed, but row surgery is skipped to avoid pairing values from different arrays; a bounded migration must repair such pre-existing corruption without deleting durable history.

### `brilliant_scientist_singularity_site_invalidate_selected_state`

The caller supplies only the selected state event target.

The helper first cancels a matching pending row, then marks every live row at that state `invalidated` without requiring current ownership or control.

This is the explicit destruction or disarmament path and preserves quantity and constructed history while preventing automatic resurrection after reacquisition.

Ordinary capture or control loss should call `brilliant_scientist_singularity_site_reconcile_receipts` instead, so an intact live row contributes again if the original state is later recovered.

### `brilliant_scientist_singularity_site_invalidate_selected_row`

The caller supplies the selected state event target, temporary `brilliant_scientist_singularity_site_selected_row_index`, and temporary marker `brilliant_scientist_singularity_site_selected_row_index_supplied = 1`.

The row query rounds a temporary copy with the documented `round_temp_variable` effect and rejects any non-integral index before indexed access; the marker rejects a missing index instead of allowing an absent value to default to row zero.

The exact row must be aligned, live, use one of the two existing roles, have quantity exactly `1`, and be attached to the selected state.

Only that row becomes `invalidated`, so multiple paid rows at one state remain independent.

The temporary output `brilliant_scientist_singularity_site_invalidation_applied` is `1` only when a live row changed status.

### `brilliant_scientist_singularity_site_retire_all`

This terminal cleanup consumes any pending receipt, changes every live or invalidated row to `retired`, keeps all quantity and constructed-history values, and reconciles the legacy counters and network flag to zero.

Repeated terminal cleanup is idempotent because retired rows are not changed again and pending state is already absent.

### `brilliant_scientist_singularity_site_reconcile_receipts`

This effect invokes the read-only reconstruction trigger, writes the existing `brilliant_scientist_singularity_live_command_node_count` and `brilliant_scientist_singularity_power_link_count` from rebuilt quantities, and sets the existing live-network flag only when both existing minimum constants are met.

Every live row is counted only when its current state still satisfies the physical predicate, so captured or facility-less sites cannot authorize the terminal path solely through stale country counters.

An unaligned ledger clears both counters and the network flag rather than using partial data.

## Read-only query interfaces

`brilliant_scientist_singularity_site_receipt_arrays_are_aligned` checks all five array lengths.

`brilliant_scientist_singularity_site_selected_input_is_valid` validates the parent reservation inputs and the current selected facility.

`brilliant_scientist_singularity_site_pending_callback_matches_receipt` validates only the exact delayed receipt identity and remains usable after state loss.

`brilliant_scientist_singularity_site_pending_callback_is_valid` composes that identity query with current physical validity and is the completion guard.

`brilliant_scientist_singularity_site_selected_row_is_valid` validates an exact destruction row without requiring current ownership or control.

`brilliant_scientist_singularity_site_current_live_quantities_are_rebuildable` initializes temporary command and power quantities to zero and scans only aligned registered rows with `all_of`, `if`, and `add_to_temp_variable`.

An aligned empty ledger returns a valid zero reconstruction.

`brilliant_scientist_singularity_site_has_minimum_live_network` performs the same temporary reconstruction and checks the existing two-node and two-link thresholds without persisting a write.

`brilliant_scientist_singularity_site_needs_command_node` and `brilliant_scientist_singularity_site_needs_power_link` use the same reconstruction to expose a construction lane only while its physical live quantity remains below the existing threshold.

The trigger implementation follows the documented `set_temp_variable`, `round_temp_variable`, `add_to_temp_variable`, `all_of`, and `if` forms in the installed vanilla `documentation/triggers_documentation.md`.

## Integrated call-site map

Both existing construction decisions are state-targeted, set role and quantity to one before calling the reserve effect, and pay only after the reservation output is `1`.

Each timer callback carries the same selected state event target and role into completion and awards the physical result only when the completion output is `1`.

The native decision cancel path and bounded owner cleanup call the cancellation boundary without attempting to reconstruct a state target from a country counter.

State capture or ordinary control loss should reconcile the owner country; explicit facility destruction should use selected-state or exact-row invalidation, according to the destruction consumer's proven row identity.

Arming, fail-deadly authorization, final commitment, and Fallout handoff combine the existing three-distinct-facility predicate with `brilliant_scientist_singularity_site_has_minimum_live_network` rather than trusting the legacy live-network flag.

Terminal cleanup calls `brilliant_scientist_singularity_site_retire_all` after the existing final result has been settled, preserving the final commitment's current capitulation failsafe.

Annexation and pre-annex civil-war cleanup settle an active construction receipt before the former country disappears, and the state-control hook reconciles both documented participant countries.

## Source and engine evidence

The accepted contract requires current owned-and-controlled qualifying facilities and separate physical site, role, quantity, live infrastructure, and durable history receipts.

The T1 terminal audit identified the existing country-only counters at `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1354-1360`, the existing facility audit at `:1338-1352`, and the uncalled destruction helper at `:1320-1336`.

Repository precedents for persistent state scope pointers and indexed array records include `common/scripted_effects/006_independence_wave_decision_effects.txt:620-621,670-672`, `common/scripted_effects/006_independence_wave_effects.txt:1031-1052`, and `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:1541`.

The required vanilla documentation records `add_to_temp_variable` at `triggers_documentation.md:713-725`, `all_of` at `:1036-1049`, `if` at `:5166-5174`, `set_temp_variable` at `:7482-7500`, `is_owned_and_controlled_by` at `:6088-6095`, and state-scope pointer existence at `:7450-7468`.

The bounded map inspection used workspace `mod_chaos_redux_ea3b2d67c2c0`, state IDs `64`, `70`, and `1`, and returned artifact SHA `6b616cc8563f42cca259f15810a089158264e9f16024a35d8f809debf8e40ac0` with map revision `d64d08d1b4ec7e58ef39ed16e46d65316fb9307164e4ada7f9b1b0f04916d790`.

The inspected state count was three; vanilla state history confirms a positive `land_facility` representative in Brandenburg state 64, while Slovakia state 70 and France state 1 provide negative static-history examples for this narrow facility predicate.

The map artifact also reported unrelated pre-existing building-position and floating-harbor adjacency diagnostics; no engine acceptance claim is made from this inspection.

## Validation boundary

This tranche adds the private effects, their companion documentation, the private status/history constants, the read-only triggers, and their state-targeted decision and lifecycle integration.

The two existing decisions retain their costs, durations, civilian-factory occupation, and score factors while gaining physical targeting, exact receipts, failed-start cancellation, and custom-cost AI budgeting hints.

No HOI4 engine launch, log inspection, or live-game acceptance was performed; those remain user-owned validation gates.
