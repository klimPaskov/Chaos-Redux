# Fallout Sealed Warehouse event addendum

## Accepted design

The Sealed Warehouse is the next reviewed global-survival tranche after Working Elevator.
It is candidate `331`, transaction `710021`, route `7121`, history `9126`, and events `331` through `337`.
It remains dormant until the Fallout scheduler activation contract is proven.

The four branches are Open Immediately, Inspect Under Quarantine, Sell the Coordinates, and Leave the Doors Sealed.
They use different costs and produce different Scrap, Medicine, Power, Filters, Recognition, Cohesion, stability, War Support, access, salvage, contamination, legitimacy, and scavenger reputation outcomes.
Failure goes through the Deaths system.
The delayed result is twenty-one days and the callback is one hundred eighty days.

## Implementation handoff

- Constants live in `common/script_constants/fallout_world_end_sealed_warehouse_constants.txt`.
- The candidate row is appended in `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`.
- Triggers, effects, modifiers, Event Log payload localisation, events, and player-facing localisation are separate Fallout-owned files or mappings.
- The report image has a dedicated source, processed preview, DDS, manifest, and GFX handoff.
- It does not reuse Zombie paths or another pilot image.
- The workbook row is `FALLOUT-331`, with the export regenerated after the implementation facts are recorded.

## Review boundary

The bounded read-only event inspector is expected to be attempted for `chaosx.fallout.331`.
If it returns `Transport closed`, that result must remain in the proof and the chain must stay dormant.
No HOI4 runtime is required for this tranche.
