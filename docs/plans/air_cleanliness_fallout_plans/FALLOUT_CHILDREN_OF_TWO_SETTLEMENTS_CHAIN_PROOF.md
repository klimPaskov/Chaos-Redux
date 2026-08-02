# Children of Two Settlements chain proof

This proof covers the reviewed dormant ordinary Fallout tranche for candidate `915`.

## Owned runtime surfaces

- Candidate registry: `common/script_constants/fallout_world_end_event_constants.txt` and `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`.
- Dedicated constants: `common/script_constants/fallout_world_end_children_of_two_settlements_constants.txt`.
- Triggers and effects: `common/scripted_triggers/fallout_world_end_children_of_two_settlements_event_triggers.txt` and `common/scripted_effects/fallout_world_end_children_of_two_settlements_event_effects.txt`.
- Events: `events/fallout_world_end_events.txt`, ids `chaosx.fallout.1037` through `chaosx.fallout.1043`.
- Event Log: `common/scripted_localisation/fallout_world_end_children_of_two_settlements_event_log_scripted_localisation.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, and the dedicated localisation file.
- Art: `interface/fallout_world_end.gfx` and `gfx/event_pictures/children_of_two_settlements/report_event_fallout_children_of_two_settlements.dds`.

## Static audit

The focused audit checked balanced Clausewitz blocks in the owned source surfaces, forbidden comparison operators, semicolons, em dashes, stale predecessor and branch tokens, exactly one definition of each event id `1037` through `1043`, all seven dedicated constant groups, global id reservations, candidate producer wiring, the `fallout_event_908_memory_closed` predecessor gate, localisation key coverage and BOM, Event Log and GFX tokens, processed image dimensions, and DDS header dimensions.

Result: `AUDIT_OK`.

The dedicated constant reference audit found `342` constant references and `378` definitions with `missing []`. This includes all `fallout_event_915_*` branch, timing, transaction, cost, threshold, modifier, and log references used by the triggers, effects, event log, event block, and candidate producer.

## Event Inspector evidence

The read-only focused Event Inspector lint query used selector `event:chaosx.fallout.1037`, `mode:lint`, `expandHelpers:false`, `maxDepth:1`, `maxNodes:8`, `maxEdges:12`, `refresh:true`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.

The returned status was `ok` with code `EVENT_INSPECTED_PARTIAL` and `blockers: []`. The report recorded `blockingDiagnostics: 0`, `events: 9406`, `options: 14517`, `entries: 1042`, `unresolvedNodes: 8027`, `issues: 2092`, `diagnostics: 2092`, and `skippedSources: 0`. The report's workspace-wide analysis was partial because helper projections and lifecycle passes were deferred, which is not a source blocker for this focused tranche.

Revision: `abfe5414d8b87c016015e8dbcb76a4601c24ce418d0d12245c6a06941ad11fda`

Graph hash: `5810d1145f0799c6107330db6dc511ef706741b3684b4c649dc274508c8bc8b6`

Artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8b9c6952b59cae8283478eef287f5e1cac9a6479c5f4b68491668c963dccf61/900d77ce0e731549840096aac001ea53ba7a27355d4864170651784d9dfcd9ef/event-lint-abfe5414d8b8.json`

## Boundary and unresolved proof

The chain is dormant and Fallout-owned. It does not request Fallout, register Fallout as an ordinary Event Log entry or evolution, create a country, transfer population between states, or add a recurring scheduler. The report image is dedicated and the source, processed preview, runtime DDS, prompt, manifest, and GFX handoff are present.

No Hearts of Iron IV process was launched. Scheduler activation, host authority, save recovery, delayed queue delivery, multiplayer behavior, player-visible Event Log rendering, and the exact engine-native all-valid-province thermonuclear sweep remain unproven and are not claimed by this tranche.
