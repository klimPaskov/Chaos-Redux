# The Adaptation Rite chain proof

This proof covers the reviewed dormant ordinary Fallout tranche for candidate `908`.

## Owned runtime surfaces

- Candidate registry: `common/script_constants/fallout_world_end_event_constants.txt` and `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`.
- Dedicated constants: `common/script_constants/fallout_world_end_adaptation_rite_constants.txt`.
- Triggers and effects: `common/scripted_triggers/fallout_world_end_adaptation_rite_event_triggers.txt` and `common/scripted_effects/fallout_world_end_adaptation_rite_event_effects.txt`.
- Events: `events/fallout_world_end_events.txt`, ids `chaosx.fallout.1030` through `chaosx.fallout.1036`.
- Event Log: `common/scripted_localisation/fallout_world_end_adaptation_rite_event_log_scripted_localisation.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, and the dedicated localisation file.
- Art: `interface/fallout_world_end.gfx` and `gfx/event_pictures/fallout/report_event_fallout_adaptation_rite.dds`.

## Static audit

Command:

`python .tmp/audit_908.py`

Result: `AUDIT_OK`.

The audit checked balanced Clausewitz blocks in the owned source surfaces, forbidden comparison operators, semicolons, em dashes, stale predecessor and branch tokens, exactly one definition of each event id `1030` through `1036`, all seven dedicated constant groups, global id reservations, candidate producer wiring, the `fallout_event_901_memory_closed` predecessor gate, localisation key coverage and BOM, Event Log and GFX tokens, catalog row `292`, processed image dimensions, and DDS header dimensions.

The dedicated constant reference audit found `342` constant references and `378` definitions with `missing []`. This includes all `fallout_event_908_*` branch, timing, transaction, cost, threshold, modifier, and log references used by the triggers, effects, event log, event block, and candidate producer.

## Event Inspector evidence

The read-only focused Event Inspector lint query used selector `event:chaosx.fallout.1030`, `mode:lint`, `expandHelpers:false`, `maxDepth:1`, `maxNodes:8`, `maxEdges:12`, `refresh:true`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.

The returned status was `ok` with code `EVENT_INSPECTED_PARTIAL` and `blockers: []`. The report recorded `blockingDiagnostics: 0`, `events: 9399`, `options: 14511`, `entries: 1042`, `unresolvedNodes: 8014`, `issues: 2092`, `diagnostics: 2092`, and `skippedSources: 0`. The report's workspace-wide analysis was partial because helper projections and lifecycle passes were deferred, which is not a source blocker for this focused tranche.

Revision: `03f7bbea9d490786193ace4632110cd854c17aa3e0e9467af5af278ef2ccb3ca`

Graph hash: `c1763bc48df9a00de7555d1e6be96beca4a85570ccbf26e090279089b4249279`

Artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed7609c1669624bec3dd556eee48ca86a4860f7d8b49a33fa06b21f79c56a9de/131cbe6c083d5b1ef150297bb8fb1d1ea5fcca3b370a2a4d3664745b61fb9603/event-lint-03f7bbea9d49.json`

## Boundary and unresolved proof

The chain is dormant and Fallout-owned. It does not request Fallout, register Fallout as an ordinary Event Log entry or evolution, create a country, transfer population between states, or add a recurring scheduler. The report image is dedicated and the source, processed preview, runtime DDS, prompt, manifest, and GFX handoff are present.

No Hearts of Iron IV process was launched. Scheduler activation, host authority, save recovery, delayed queue delivery, multiplayer behavior, player-visible Event Log rendering, and the exact engine-native all-valid-province thermonuclear sweep remain unproven and are not claimed by this tranche.
