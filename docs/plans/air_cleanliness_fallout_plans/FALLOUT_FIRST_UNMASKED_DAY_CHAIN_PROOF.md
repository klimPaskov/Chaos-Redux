# Fallout The First Unmasked Day chain proof

## Ownership and ids

- Event file: `events/fallout_world_end_events.txt`
- Namespace: `add_namespace = chaosx.fallout`
- Event ids: `471` through `477`
- Candidate: `471`
- Transaction key: `710041`
- Route: `7141`
- Event Log history: `9146`
- No zombie id, file, asset, audio, sprite, or path is reused.

## Selection proof

`fallout_event_pilot_first_unmasked_day_state_is_current` requires a current Fallout state identity and durable resource row, a produced Air Winter snapshot, thaw-eligible normal-map provenance, global Air Contamination above the spread threshold and below the severe-winter threshold, intact infrastructure, low state supply access, surviving population, adaptation, reclamation, and owner resources. It also requires high disease pressure and less than maximum water security so the exposure choice has a real health cost. The candidate producer chooses the lowest valid owned state id.

## Chain proof

The opening has four branch policies with government-aware option gates. Both human and hidden AI lanes use the same branch scheduler and cost logic. The result is delayed by 35 days. A 365-day callback revisits the exposure memory. Result and callback failures use `apply_exact_state_civilian_population_loss`, with rail or infrastructure damage through native building effects. Success and partial lanes update Air Winter, resources, manpower, stability, war support, and the exposure ledgers. The global Air Contamination value is not rewritten by this ordinary event.

The cleanup event releases both delayed receipts only after the issued ticket matches the stored result or callback ticket. It marks the memory closed, clears branch, registry, frozen-ledger, and route-ledger values, and clears the registry-committed state flag. Durable branch and exposure-failure state flags remain as country memory so later scheduler rows can read the first opening.

## Presentation proof

The dedicated report art is `GFX_report_event_fallout_first_unmasked_day`. Event localisation covers the opening, four branch result lanes, the callback, tooltips, Event Log name, Event Log detail, and fifteen Event Log payloads.

## Activation status

The chain is dormant and contributes zero blocks to the release floor. Scheduler activation, host authority, save recovery, multiplayer delivery, full-screen blackout ownership, and runtime Event Log delivery remain unproven.
