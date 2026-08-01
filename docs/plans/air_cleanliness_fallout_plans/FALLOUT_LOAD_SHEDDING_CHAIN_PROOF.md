# Fallout Load Shedding chain proof

## Scope

Load Shedding is a dormant ordinary Fallout technate chain. It uses candidate `803`, transaction `710086`, route `7204`, history `9192`, events `803` through `809`, and no world-end scenario id.

## Source surfaces

- Candidate producer: `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`
- Constants: `common/script_constants/fallout_world_end_event_constants.txt` and `common/script_constants/fallout_world_end_load_shedding_constants.txt`
- Triggers: `common/scripted_triggers/fallout_world_end_load_shedding_event_triggers.txt`
- Effects: `common/scripted_effects/fallout_world_end_load_shedding_event_effects.txt`
- Events: `events/fallout_world_end_events.txt`
- Localisation: `localisation/english/fallout_world_end_load_shedding_l_english.yml`
- Event Log routing: `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` and `common/scripted_localisation/fallout_world_end_load_shedding_event_log_scripted_localisation.txt`
- Presentation: `interface/fallout_world_end.gfx` and the dedicated report DDS

## Mechanics proof

The candidate is restricted to the East Asia region, Manchurian Reactor Keeps country memory, the technate archetype, a closed Engineer Franchise state memory, Air Winter, Supply Access, a power or industrial building, and an external neighbor. It selects the lowest eligible owned state and uses the existing Fallout scheduler row contract.

The four branches use distinct survival costs and sector outcomes. The delayed result freezes the state and country receipts, resolves after `28` days, applies Air Winter, Supply Access, Medicine, Recognition, Cohesion, Stability, War Support, sector memory, bilateral opinion, and bounded Deaths failure. The callback resolves after `240` days and grades every load and material ledger before authenticated cleanup.

Hidden AI uses the same four branches, affordability checks, delayed tickets, result and callback effects, Event Log payloads, and cleanup path as human play.

## Static audit record

The tranche is audited for unique event ids `803` through `809`, preservation of the preceding `789` through `802` rows, balanced Clausewitz braces and quotes in the dedicated scripts, unresolved dedicated constant references, unresolved Event Log localisation references, no unsupported comparison operators in authored sources, no em dashes or semicolons in authored prose, and UTF-8 BOM on the dedicated localisation file.

The source image, processed report PNG, DDS header, dimensions, hashes, sprite registration, and event picture consumers are recorded in `docs/assets/803_load_shedding/manifest.md` and `gfx_handoff.md`.

The read-only Event Inspector lint returned `EVENT_INSPECTED_PARTIAL` for `chaosx.fallout.803` with zero blocking diagnostics. Its workspace-wide helper and lifecycle projection was deferred, so the report's unresolved-node and issue totals are not treated as tranche defects. It is not a live campaign acceptance claim. No Hearts of Iron IV process is launched. Scheduler activation, save recovery, host authority, multiplayer delivery, and live Event Log presentation remain unproven by design because those checks belong to the user's campaign validation.
