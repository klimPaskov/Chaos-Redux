# Event 12 delayed offer callback generation gate

Date: 2026-08-02

## Problem

`chaosx.nr12.210` is scheduled for the quoted offer-response delay. Before this patch, cancelling an offer after the ordinary 30-day target cooldown allowed a new offer to start while the old delayed event still existed; the old callback could then resolve the newer active record. Host transfer created the same cross-generation risk.

## Changes

- `common/scripted_effects/012_africa_action_effects.txt`
  - Offer-response launch now refuses only when the selected target still carries an outstanding `africa_action_response_callback_pending` receipt.
  - The delayed event snapshots `africa_action_response_callback_generation` and `africa_action_response_callback_host_generation` on the target.
  - The receipt lasts for `africa_active_action_response_days + 1` and is intentionally not cleared by ordinary action cleanup.
  - Added `africa_clear_action_response_callback` for the accepted response options.
- `common/scripted_triggers/012_africa_triggers.txt`
  - Added `africa_action_response_callback_is_current`, requiring the pending receipt, offer-response kernel, matching action/host generations, and current committed host generation.
- `events/012_african_union.txt`
  - `chaosx.nr12.210` now uses the shared current-callback trigger and clears the receipt immediately before each accepted full, partial, or failure resolution.
- `docs/events/012_africa/action_duration_objective_contract.md`
  - Documents the target-owned callback receipt, generation matching, expiry, and offer-only relaunch gate.

## Acceptance disposition

Static source wiring is installed. The following live scenario proofs remain open: current callback resolves once; a cancelled 60-day offer cannot have its old callback resolve a later offer after day 30; host generation change fails closed; annex/release backlog fails closed; different targets remain independent.

No new country tags, portraits, models, event IDs, currencies, or parallel mission families were added.
