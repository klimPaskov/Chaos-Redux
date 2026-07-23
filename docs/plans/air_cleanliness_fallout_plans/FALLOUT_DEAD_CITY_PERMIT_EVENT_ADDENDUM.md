# Fallout Dead City Permit event addendum

## Accepted design

The Dead City Permit is the next reviewed global-survival tranche after Sealed Warehouse.
It is candidate `338`, transaction `710022`, route `7122`, history `9127`, and events `338` through `344`.
It remains dormant until the Fallout scheduler activation contract is proven.

The four branches are State Expedition, Licensed Guilds, Military Seizure, and Forbid Entry.
They use different costs and produce different Scrap, Medicine, Fuel, Power, Recognition, Cohesion, stability, War Support, reclamation, supply, contamination, and state-memory outcomes.
Failure goes through the Deaths system in the selected state.
The delayed result is twenty-eight days and the permit review is two hundred ten days.

## Implementation handoff

- Constants live in `common/script_constants/fallout_world_end_dead_city_permit_constants.txt`.
- The candidate row is appended in `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`.
- Triggers, effects, modifiers, Event Log payload localisation, events, and player-facing localisation are separate Fallout-owned files or mappings.
- The report image has a dedicated source, processed preview, DDS, manifest, and GFX handoff.
- It does not reuse Zombie paths or the Air Winter dead-city salvage image.
- The workbook row is `FALLOUT-338`, with the export regenerated after implementation facts are recorded.

## Review boundary

The bounded read-only event inspector was attempted for `chaosx.fallout.338` and returned `EVENT_ISSUE_LIMIT` with 23,001 issues against a fixed ceiling of 20,000.
The chain stays dormant because the inspector produced no artifact and cannot prove the required engine-sensitive surfaces.
No HOI4 runtime is required for this tranche.
