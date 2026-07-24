# The Ship That Will Not Dock

This reviewed pilot covers a maritime refugee and quarantine chain in a surviving coastal state. It is Fallout-owned and remains dormant until the scheduler activation receipt, host authority, save recovery, multiplayer delivery, and final event audits are approved.

## Trigger and target

The candidate selects the lowest owned state that has a current produced Air Winter snapshot, a surviving population, a current state row, coastal geography, and a non-damaged naval base. The candidate stores the state id and its non-damaged naval-base level. It does not scan provinces or invent a port target.

The country gate requires the current Fallout generation, a durable country resource row, enough Food, Recognition, and Cohesion, a campaign day between 600 and 3200, exposure within the reviewed band, reclamation below its ceiling, and local Supply Access below its ceiling. It rejects an already committed or closed chain.

## Policies and delayed result

The opening offers four authored policies.

1. Dock under quarantine opens one sealed berth and admits passengers only through a medicine ward. It is available to democratic and neutral governments.
2. Anchor and test keeps the vessel outside the breakwater while the port laboratory checks the engine room, clinic, and water stores. It is available to democratic, neutral, and communist governments.
3. Tow it to neutral water pays a neutral tug to move the vessel away from the harbour approach. It has no government lock and records a maritime bargain.
4. Seize the manifest places the ship, cargo list, and radio crew under state custody. It is available to fascist and communist governments.

Each policy spends a different Food, Recognition, and Cohesion cost. The result is delayed for 35 days. Deterministic viability uses frozen diaspora memory, port legitimacy, quarantine cohesion, Recognition, Food, maritime trust, and ideology pressure. Every branch has separate success, partial, and failure thresholds.

## State and country effects

Success, partial, and failure write separate state memory and timed state modifiers. The chain updates Reclamation, Exposure, Supply Access, Food, Recognition, Cohesion, Stability, War Support, and Deaths. Failure damages infrastructure when it is available and otherwise damages an industrial complex through the existing repairable-building route.

Passenger transfer is branch-specific. Dock success admits three percent of the target state's surviving population, anchor success admits 1.5 percent, tow admits none, and seizure admits 0.5 percent. Partial outcomes use lower shares. The state stores the transferred cohort in `fallout_state_ship_passengers_current`, while the country stores a bounded `fallout_ship_passengers_current` share.

The country ledgers are `fallout_ship_diaspora_memory_current`, `fallout_ship_port_legitimacy_current`, `fallout_ship_quarantine_cohesion_current`, and `fallout_ship_maritime_trust_current`. They are initialized once, frozen before the delayed row, clamped after each outcome, and retained as cause memory after cleanup.

## Callback and cleanup

The first harbour review returns after 270 days. It applies separate success, partial, and failure effects, including a callback modifier and Deaths-backed failure. Event Log history `9139` records the branch outcome and the review outcome. The result and callback each use the shared delayed-result and delayed-cleanup receipts. The cleanup event releases the matching receipts, clears temporary registry and frozen values, closes the memory once both receipts are released, and leaves only the durable maritime ledgers, state memories, timed effects, and Event Log entry.

## Assets and localisation

The dedicated report image is `GFX_report_event_fallout_ship_that_will_not_dock`. Its source, processed image, DDS, prompt, manifest, and handoff live under `docs/assets/air_cleanliness_fallout/fallout_ship_that_will_not_dock/`. Player-facing text names the harbour chain, medical ward, radio crew, tug, breakwater, cargo rights, and patrol consequences. It contains no working labels, em dashes, semicolons, zombies, or reused event assets.

## Deferred surfaces

The pilot does not claim runtime activation, the full-screen Fallout blackout, host authority, save recovery, multiplayer delivery, a live bilateral partner target, a successor-country focus package, or final release-floor countability. Those surfaces remain explicit blockers in the chain proof.
