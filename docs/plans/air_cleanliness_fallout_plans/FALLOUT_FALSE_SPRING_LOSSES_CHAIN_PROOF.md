# Fallout False Spring Losses chain proof

Status: implemented as a dormant reviewed tranche, not release-floor credit.

Events `chaosx.fallout.478` through `.484` are defined once in `events/fallout_world_end_events.txt`. The root uses the Fallout namespace and the opening description has a unique `chaosx.fallout.478.intro` key so it cannot collide with option `d`.

Candidate `478` uses transaction `710042`, route `7142`, and history `9147`. The producer selects the lowest owned state that passes `fallout_event_478_false_spring_state_is_current`. That trigger requires a produced current-generation Air Winter snapshot, a valid first-frost marker, a thaw-eligible normal-map visual state, a rural native category, population, adaptation, exposure, reclamation, food reserve, and low supply access.

The four branches are emergency replant, imported seed, underground reserve, and accepting a smaller harvest. The result waits `35` days. The second-sowing callback waits `240` days. Human and hidden-AI branches share the same deterministic viability calculation and cleanup path. Result and callback failures request population loss through the Deaths system and the callback closes the chain only after both cleanup receipts are authenticated.

The chain changes Food, Medicine, Cohesion, Recognition, seed reserve, frost memory, Air Winter exposure, adaptation, reclamation, supply, stability, war support, and a native building level. It records branch and outcome payloads through Event Log history `9147` and maps the detail and name surfaces through the shared Event Log localisation route.

The dedicated report image is source-reviewed, processed at `210x176`, converted to a one-level uncompressed BGRA DDS, copied into the runtime Fallout picture directory, and registered as `GFX_report_event_fallout_false_spring_losses`. The manifest records matching runtime hashes.

Static checks for this tranche found seven unique event definitions, matching localisation references, no stale predecessor branch identifiers in the new runtime files, matching asset hashes, balanced edited script blocks, and no raw unsupported comparison operators. The localisation file is BOM encoded.

The chain is dormant and contributes zero countable blocks because scheduler activation, host authority, save recovery, multiplayer delivery, full-screen Fallout blackout, and runtime Event Log delivery remain unproven. No HOI4 runtime was launched.
