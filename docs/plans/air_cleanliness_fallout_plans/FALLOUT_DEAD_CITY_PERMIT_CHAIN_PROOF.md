# Fallout Dead City Permit chain proof

## Static evidence

- Candidate row: `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`, candidate `338`.
- Trigger contract: `common/scripted_triggers/fallout_world_end_dead_city_permit_event_triggers.txt`.
- Transaction effects: `common/scripted_effects/fallout_world_end_dead_city_permit_event_effects.txt`.
- Event ids `338` through `344`: `events/fallout_world_end_events.txt`.
- Constants: `fallout_event_338_*` groups in the dedicated constants file plus the shared event identity and candidate reservation groups.
- Event Log history `9127`: shared type and name-detail mappings plus the dedicated fifteen-payload mapping.
- Report asset: generated source, processed preview, DDS, manifest, and GFX handoff under `docs/assets/air_cleanliness_fallout/fallout_dead_city_permit/`.

The touched script files have balanced braces, no unsupported `<=` or `>=` operators, and no non-ASCII script tokens.
Events `338` through `344` are defined once.
Localisation is BOM encoded and branch, result, callback, modifier, and Event Log keys are checked by static scan.

## Engine-sensitive evidence

The bounded read-only `hoi4.event_inspect` lint request for `chaosx.fallout.338`, with helper expansion disabled and bounded nodes and edges, returned `EVENT_ISSUE_LIMIT` with 23,001 issues against a fixed ceiling of 20,000 and produced no artifact.
The same result occurred when the request was narrowed to `events/fallout_world_end_events.txt`, so exact engine-side reachability of the delayed result, state-scoped effects, host authority, save recovery, multiplayer delivery, and Event Log opening remains unproven.
No HOI4 runtime was launched for this task.

## Release-floor disposition

The Dead City Permit is a dormant reviewed pilot and contributes zero countable blocks to the 660-block release floor until scheduler activation and engine-sensitive delivery surfaces are proven.
