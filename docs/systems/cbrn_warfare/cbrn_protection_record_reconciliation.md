# CBRN protection record reconciliation

## What it does

The occupied distribution programme and the protective-equipment export both reserve real respirator models before they deliver anything, and both measure every native stockpile movement instead of trusting a nominal amount.
When a measured movement falls outside its bounds, or when a service fee cannot be recorded or settled, the route stops and keeps its exact evidence rather than inventing a success.
Reconciliation is the player action that closes such a stopped record, so the decision family becomes usable again.

Without it the occupied programme and the affected export partner were lost for the rest of the game: the occupied block sits behind a hidden trigger inside the selection predicate, and the export preflight refuses a recipient whose shipment record is still open.

## Occupied distribution

**Audit the Occupied Mask Accounts** (`cbrn_reconcile_occupied_mask_records`) is a country decision in the CBRN programme category.
It is visible only while `cbrn_occupied_country_can_reconcile` holds: the donor carries the pending block and no occupied programme is running, so a live reservation can never be returned by mistake.
The player-facing requirement is stated through `custom_trigger_tooltip`, so the raw block flag is never shown.

`cbrn_occupied_reconcile_held_records` runs these steps in order.

1. The pending block is released so the step below can re-set it only through the normal measured path.
2. Every state holding a reservation receipt owned by this donor and marked for recovery is visited. Its quarantine marks are cleared and the existing measured refund `cbrn_refund_occupied_state_mask_reservation` runs once more. Each confirmed credit reduces its own recorded row, so a model can never be returned twice, and a repeated native refusal re-quarantines the state exactly as before.
3. A receipt the engine refuses a second time is written off by `cbrn_occupied_write_off_state_escrow`. The written-off rows are counted, zeroed and closed, and nothing is credited to the stockpile, so an unverified movement never reads as a delivery.
4. `cbrn_occupied_reconcile_recorded_fees` walks the recorded transactions in `cbrn_occupied_recovery_transactions`. A failed settlement is settled once more; whatever still cannot be settled, and any fee that was charged but never recorded, is written off and its rows are cleared. No credit is retried for a movement the cost framework never acknowledged, so the same fee cannot be returned twice.
5. The block is released, the audit result is stored for the decision description and the mask snapshot is refreshed from real stock.

States that carry a healthy active reservation have neither recovery mark and are never visited.
Delivered coverage, the shared transaction arrays, the recorded achievement rows and the programme selection cooldown are untouched.

The state pass uses `every_state` with the recovery predicate as its limit so a receipt in a state the donor no longer controls is also closed.
This is a single player action, not a periodic or world-wide hook.

## Export shipments

**Audit the Shipment to \<partner\>** (`cbrn_reconcile_export_shipment_records`) is a targeted decision over `global.enabled_countries_list`.
Its actor gate is the existing actor-only owned-record count, because the recipient is not established until native target iteration.
The target gate `cbrn_export_transaction_has_recovery_work` requires an owned record for that exact recipient, no shipment under way, and either the native mismatch mark or the recovery mark.

`cbrn_export_transaction_reconcile` clears the mismatch and transfer marks, measures the held total, runs the existing `cbrn_export_transaction_refund_held` once more and reports the difference as returned.
Whatever the engine still refuses is written off by `cbrn_export_write_off_held_models`, which zeroes the held rows and records their exact count without crediting stock.
The fee is then closed through the existing settle helper; if it still cannot close and a fee was actually charged, the amount is written off, its allocation marker is released and the fee is marked closed.
Ownership release then runs unchanged: it requires a zero held total, no mismatch and a closed fee, so it clears the active and owned marks, decrements the owner count and clears the recovery mark.
The recipient can be supplied again from the next tick.

Delivered totals, the partner's recorded aid, the opinion modifier and the Condemnation compliance credit are never altered, so an audit cannot turn a loss into aid.

## Tuning and identifiers

| Value | Where |
| --- | --- |
| `cbrn_protection_decision_timing.records_reconciliation_reenable_days` | `common/script_constants/cbrn_system_constants.txt` |
| `cbrn_protection_ai.base_reconciliation` | `common/script_constants/cbrn_system_constants.txt` |

Both audits carry an AI weight so an AI country also clears a stopped record instead of losing the route permanently.

Owner files:

- `common/scripted_effects/cbrn_occupied_transaction_effects.txt`
- `common/scripted_effects/cbrn_export_transaction_effects.txt`
- `common/scripted_triggers/cbrn_occupied_transaction_triggers.txt`
- `common/scripted_triggers/cbrn_export_transaction_triggers.txt`
- `common/decisions/cbrn_protection_decisions.txt`
- `common/scripted_localisation/cbrn_occupied_transaction_localisation.txt`
- `common/scripted_localisation/cbrn_export_transaction_localisation.txt`
- `localisation/english/cbrn_protection_l_english.yml`

## Icons

No new art is required.
The occupied audit reuses `GFX_decision_cbrn_supply_occupied_population` and the export audit reuses `GFX_decision_cbrn_export_protective_equipment`, both defined in `interface/cbrn_protection.gfx` with their existing DDS files under `gfx/interface/decisions/stage_2_protective_equipment/decisions/`.
If a distinct audit icon is wanted later, it belongs in the same `.gfx` file under the names `GFX_decision_cbrn_reconcile_occupied_mask_records` and `GFX_decision_cbrn_reconcile_export_shipment_records`, with the DDS files beside the existing protection decision art, and the two `icon =` lines in `common/decisions/cbrn_protection_decisions.txt` updated in the same change.

## Interaction with the rest of the package

- The occupied selection predicate `cbrn_occupied_country_selection_ready` still refuses a start while the block is set; the audit is the only route that clears it.
- The export preflight still refuses a recipient with an open record; ownership release is the only route that reopens it, and the audit guarantees that release terminates.
- The measured escrow primitives in `common/scripted_effects/cbrn_state_escrow_native_effects.txt` are unchanged. The audit calls them through the existing state wrapper rather than reimplementing a credit.
- Automatic protection maintenance reads the same real stock, so each audit ends with a mask-snapshot refresh.

## Future work

- Surface the written-off totals in the protection overview window so a player can see accumulated losses without opening the decision.
- Give the export audit a per-recipient summary instead of the single most recent audit line, once a per-partner display exists.
- If the measured native route is ever proven exact for every model, the write-off branch can become an explicit error report instead of a loss.
