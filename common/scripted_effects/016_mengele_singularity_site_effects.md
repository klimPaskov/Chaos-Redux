# Event 016 Mengele Singularity physical site receipts

## Purpose and scope

These COUNTRY-scope helpers hold the registered Mengele Directorate's private command-node and power-link site receipts. They do not construct a facility, charge a cost, start a timer, grant a Singularity component, or enter Fallout. The paid timer decisions and callbacks are in `common/decisions/016_mengele_singularity_construction_decisions.txt` and `common/scripted_effects/016_mengele_singularity_construction_effects.txt`.

All persistent variables and flags use `mengele_event016_`. The helpers use the existing `brilliant_scientist_singularity_component.command_core` and `.power_link` role IDs, `brilliant_scientist_singularity_site_status` and `.history` row states, `brilliant_scientist_value` values, and the existing two-node and two-link minimums. No new tuning category or threshold is introduced.

The selected state is the regular event target `mengele_event016_singularity_site_selected_state`. A COUNTRY caller must bind it in the same effect chain as reservation or the matching timer callback. The target is never global and these helpers never clear it. The parent must carry or rebind it for callbacks and let it expire with that chain.

## Receipt schema and defaults

The aligned country arrays are `mengele_event016_singularity_site_state_entries`, `_role_entries`, `_quantity_entries`, `_status_entries`, and `_history_entries`. A paid completion creates exactly one row with quantity `constant:brilliant_scientist_value.one`. The initial row status is `pending` and its independent history is `none`. Successful completion changes status to `live` and history to `constructed`. Invalidation or retirement changes status only. Permanent construction history is never erased by transient cleanup.

The one pending transaction uses country flag `mengele_event016_singularity_site_pending` and normal variables `mengele_event016_singularity_site_pending_state`, `_role`, `_quantity`, and `_row`. There is no inferred pending default. Missing or mismatched metadata fails completion closed. A pending flag, metadata field, or pending row prevents a second reservation until cleanup settles it.

The rebuilt temporary counts default to zero on each query. `brilliant_scientist_mengele_singularity_site_has_minimum_live_network = yes` requires the registered provider gate, aligned arrays, at least two valid command-node rows, and at least two valid power-link rows. It reads the physical ledger directly. It never accepts `mengele_event016_singularity_live_command_node_count`, `mengele_event016_singularity_power_link_count`, or `mengele_event016_singularity_live_command_network` as evidence.

Each counted row must have status `live`, the exact role, quantity one, and a saved state that the querying country currently owns and controls. That state must still have positive `land_facility`, `air_facility`, `nuclear_facility`, or `biowarfare_facility`. The STATE predicate is entered directly from the receipt-owning COUNTRY so `PREV` is that country. Several separately paid rows may refer to one intact state. Captured or facility-less rows stop counting, and an intact recovered state can count again until its row is explicitly invalidated.

## Helper map

| Helper | Scope and inputs | Output and side effects | Intended parent call site |
| --- | --- | --- | --- |
| `brilliant_scientist_mengele_singularity_site_selected_input_is_valid` | COUNTRY, selected-state event target, temporary selected role and quantity one | Read-only check of provider, role, state, ownership, control, and facility | Construction visibility and pre-payment gate |
| `brilliant_scientist_mengele_singularity_site_reserve_construction` | COUNTRY, same inputs, no existing pending receipt, aligned arrays | Appends one pending row, stores exact state/role/quantity/row metadata, sets temporary `mengele_event016_singularity_site_reservation_applied` to one on success | Paid construction begin after the parent has authenticated the action |
| `brilliant_scientist_mengele_singularity_site_pending_callback_matches_receipt` | COUNTRY, callback-selected target, role, and quantity one | Read-only identity guard, valid even after capture or facility loss | Timer cancellation or finish before touching the parent's payment receipt |
| `brilliant_scientist_mengele_singularity_site_complete_pending_construction` | COUNTRY, matching callback and currently valid provider and physical state | Clears pending metadata first, marks its exact row live and constructed, reconciles private counters, sets temporary `mengele_event016_singularity_site_completion_applied` to one on success | Timer finish, before any parent reward |
| `brilliant_scientist_mengele_singularity_site_cancel_pending_construction` | COUNTRY, owner cleanup after callback identity check or authoritative orphan cleanup | Clears pending metadata and aligned pending rows, reconciles counts, sets temporary `mengele_event016_singularity_site_cancellation_applied` when anything was consumed | Matching timer cancel, provider shutdown, or orphan cleanup |
| `brilliant_scientist_mengele_singularity_site_invalidate_selected_state` | COUNTRY, selected-state event target | Cancels a matching pending row, invalidates all live rows at that state, preserves construction history, reconciles counts | Explicit facility destruction or disarmament |
| `brilliant_scientist_mengele_singularity_site_invalidate_selected_row` | COUNTRY, selected-state target, temporary exact row index and `_selected_row_index_supplied = 1` | Invalidates only that live row, preserves sibling rows and history, reconciles counts | Exact partial-loss receipt |
| `brilliant_scientist_mengele_singularity_site_reconcile_receipts` | COUNTRY, no input | Rebuilds private display counters and network flag from live physical rows, or zeros them on malformed alignment | Capture, control change, facility change, or presentation refresh |
| `brilliant_scientist_mengele_singularity_site_retire_all` | COUNTRY, no input | Cancels pending and retires live or invalidated rows, preserving history and quantities | Confirmed provider terminal cleanup |
| `brilliant_scientist_mengele_singularity_site_has_minimum_live_network` | COUNTRY, no input | Read-only private physical readiness trigger | Private terminal readiness |
| `brilliant_scientist_mengele_singularity_site_needs_command_node` and `_needs_power_link` | COUNTRY, no input | Read-only checks against existing minimums | Parent construction lane visibility |

`brilliant_scientist_mengele_singularity_site_receipt_arrays_are_aligned`, `_pending_row_is_valid`, `_selected_row_is_valid`, and `_current_live_quantities_are_rebuildable` are internal read-only validation helpers. `brilliant_scientist_mengele_singularity_site_clear_pending_receipt_metadata` and `_remove_pending_rows` are internal effects. A malformed aligned-array set is not repaired by these helpers because indiscriminate repair could pair unrelated state and history values. Live readiness fails closed.

## Example call sequence

```hoi4
# COUNTRY scope. The parent selects an owned, controlled facility state and
# binds it with save_event_target_as = mengele_event016_singularity_site_selected_state.
set_temp_variable = { mengele_event016_singularity_site_selected_role = constant:brilliant_scientist_singularity_component.command_core }
set_temp_variable = { mengele_event016_singularity_site_selected_quantity = constant:brilliant_scientist_value.one }
if = {
	limit = { brilliant_scientist_mengele_singularity_site_selected_input_is_valid = yes }
	brilliant_scientist_mengele_singularity_site_reserve_construction = yes
}
# The parent starts and pays its own timer only if reservation_applied is one.
# Its exact matching callback rebinds the same target, role, and quantity.
brilliant_scientist_mengele_singularity_site_complete_pending_construction = yes
# The paid callback treats completion_applied as the proof of a live site row.
```

## Migration, cleanup, and integration limits

The parent must migrate any earlier private count-only state into authenticated physical rows only when it has exact state and payment provenance. Neutral component research flags and Mengele's six-component registry do not prove a construction site. No Kruger rows, flags, variables, terminal receipts, or KRG migration are read or written here.

The construction actions bind their selected state, check reservation before payment, and verify callback identity before refunding. The existing state-control hook reconciles affected participants, provider cleanup retires rows after payment settlement, and terminal readiness pairs this live-network trigger with the separate required-facility and DLC-appropriate component gates. The helper does not call a periodic on-action or scan all countries.

There are no new icons, sprites, or localisation keys in this private helper layer. The construction decisions reuse vanilla `GFX_decision_generic_research` and have their own localisation file. No 3D geometry, entity, asset, or map locator is touched. A later provider-specific physical construction presentation could show each site's role and intact status without changing this ledger.
