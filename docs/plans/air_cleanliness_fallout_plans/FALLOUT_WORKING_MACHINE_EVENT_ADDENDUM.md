# Fallout The Working Machine Event Addendum

## Accepted design

The Working Machine is the reviewed global-survival tranche after The Manual Nobody Read.
It is candidate `352`, transaction `710024`, route `7124`, history `9129`, and events `352` through `358`.
It remains dormant until the Fallout scheduler activation contract is proven.

The four branches are Integrate the Machine, Dismantle the Machine, Venerate the Protocol Council, and Isolate the Facility.
They use distinct resource costs and produce distinct Power, Scrap, Medicine, Recognition, Cohesion, Stability, War Support, reclamation, supply, exposure, building, and state-memory outcomes.
Result failure and callback failure use the Deaths system in the selected native state.
The result delay is forty-nine days and the callback delay is three hundred days.

## Implementation handoff

- Constants live in `common/script_constants/fallout_world_end_working_machine_constants.txt`.
- The candidate row is appended in `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`.
- Triggers, effects, modifiers, Event Log payload localisation, events, and player-facing localisation are Fallout-owned surfaces.
- The report image has a dedicated generated source, processed preview, DDS, manifest, and GFX handoff.
- It does not reuse Zombie paths, Air Winter report images, or another Fallout chain's source.
- The workbook row is `FALLOUT-352`, with CSV export regenerated after implementation facts are recorded.

## Review boundary

The bounded read-only event inspector is required for `chaosx.fallout.352`.
If it returns the known fixed issue ceiling without an artifact, the chain remains dormant and the exact engine-side receipt, host, save recovery, multiplayer, and target delivery surfaces remain unproven.
No HOI4 runtime is required for this tranche.
