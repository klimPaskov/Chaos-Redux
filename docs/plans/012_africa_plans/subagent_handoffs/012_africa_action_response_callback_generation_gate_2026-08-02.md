# Event 12 offer-response mission timeout handoff

Date: 2026-08-02

## Problem

`chaosx.nr12.210` was scheduled as an independent delayed country event. Country-event timers pause when a country ceases to exist, so a resumed callback could outlive the original action and be rebound to a later offer.

## Changes

- `common/scripted_effects/012_africa_action_effects.txt`
  - Removed the independent delayed country-event schedule and callback receipt variables.
  - Added `africa_timeout_current_action`, which dispatches the response event from the shared mission timeout only while the current offer and host generation are valid; all other rows use the existing resolver.
- `common/scripted_triggers/012_africa_triggers.txt`
  - Added `africa_action_response_is_current`, requiring the live offer-response kernel and current committed host generation.
- `events/012_african_union.txt`
  - `chaosx.nr12.210` now uses the shared current-response trigger; options resolve the still-active mission without a mutable callback receipt.
- `common/decisions/012_africa_decisions.txt`
  - All four shared mission timeout paths call the lifecycle dispatcher.
- `docs/events/012_africa/action_duration_objective_contract.md`
  - Documents mission-bound response dispatch and the no-backlog invariant.

## Acceptance disposition

Static source wiring is installed. The remaining live scenario proofs are the shared mission timer, one-time response resolution, host transfer cancellation, target disappearance cancellation, and independent simultaneous targets. The old delayed-event backlog race is removed by construction.

No new country tags, portraits, models, event IDs, currencies, or parallel mission families were added.
