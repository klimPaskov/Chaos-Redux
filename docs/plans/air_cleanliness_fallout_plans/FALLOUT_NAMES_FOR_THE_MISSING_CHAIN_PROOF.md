# Names for the Missing chain proof

## Static implementation proof

- Candidate id: 269
- Transaction key: 710013
- Scheduler route: 7113
- Event ids: 269 through 281
- Event namespace: `chaosx.fallout`
- Event Log history: 9118
- Target type: `fallout_event_subject_type.none`
- Target value: zero
- Result delay: 21 days
- Callback delay: 180 days
- Human opening visible budget: 3 units for the full opening, result, and callback envelope
- Human delayed-row visible budget: 1 unit per visible result or callback
- Hidden AI delayed-row visible budget: 0 units
- Failure population requests: Deaths API only
- Activation state: dormant

The candidate producer appends the row only for a current country registry with high recorded civilian deaths, incomplete Recognition, and at least one affordable branch. The opening consumes one ordinary receipt, freezes the country values, and reserves one delayed result. Human and AI result events share the same outcome effect and callback scheduler. Cleanup releases the callback and result receipts in either completion order, then clears temporary registry variables while retaining durable memory and exposure.

## Branch and outcome proof

The four branches have authored costs and distinct effects. Deterministic viability is calculated from frozen Recognition, frozen Cohesion, and the bounded severity formula `clamp(Deaths * 0.001, 0, 100)`. The result and callback each record success, partial, or failure payloads in history 9118. The result can alter Food, Scrap, Power, Recognition, Cohesion, Stability, War Support, and intelligence exposure. Result failure requests 0.4 percent of each owned state's remaining population through `apply_exact_state_civilian_population_loss`. Callback failure uses a separate helper at 0.2 percent.

## Asset and Event Log proof

`GFX_report_event_fallout_names_missing` is registered in `interface/fallout_consolidated.gfx` and points to the dedicated 210 by 176 DDS. Source, processed preview, manifest, provenance, hashes, and the sprite handoff are under `docs/assets/air_cleanliness_fallout/fallout_names_missing/`. History 9118 has central Event Log name and detail mappings, plus fifteen payload detail keys.

## Unproven runtime surfaces

This is static proof only. The exact native all-valid-province thermonuclear sweep remains blocked. The candidate is dormant, so no live ordinary receipt, delayed queue, blackout, host-authority, save-recovery, multiplayer input, or scheduler activation behavior is claimed. The overall Fallout release floor remains 0 of 660 countable reviewed blocks.
