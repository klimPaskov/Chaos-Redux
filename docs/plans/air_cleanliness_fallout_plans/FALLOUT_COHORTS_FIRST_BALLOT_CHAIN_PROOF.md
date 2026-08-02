# Fallout chain proof: The Cohort's First Ballot

This proof records the reviewed implementation boundary for candidate `922`. The chain is owned by `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`. It is an ordinary dormant consequence chain and does not register Fallout as an Event Log event, evolution, or super-event.

## Static source audit

The source audit covered the candidate producer, shared event constants and Event Log routing, the dedicated constants, scripted triggers, scripted effects, dynamic modifiers, opinion modifiers, event block, localisation, GFX registration, asset manifest, spec, matrix, plan ledger, scheduler proof, source map, and catalog row.

The audit confirms one predecessor gate `fallout_event_915_memory_closed`, one candidate producer for `922`, one event block for each id `1044` through `1050`, one history id `9209`, four branch tokens, human and hidden AI parity, result and callback cleanup lanes, bounded Deaths requests, and no stale Children of Two Settlements branch tokens in the dedicated runtime files. The localisation file has a UTF-8 BOM and covers all opening, result, callback, Event Log, and dynamic result labels. The asset package contains a generated source, a processed 210x176 RGBA report image, a runtime DDS, prompt, manifest, hashes, and GFX handoff.

The static audit also confirms that the producer is limited to the mutant-polity Congo Green Basin country memory, selects the lowest eligible ward, stores one idempotent state target, and does not request Fallout, create a country, transfer population between states, or add a recurring scheduler.

## Focused Event Inspector evidence

The read-only focused Event Inspector lint query used selector `{ kind: event, eventId: chaosx.fallout.1044 }`, `mode = lint`, `expandHelpers = false`, `maxDepth = 1`, `maxNodes = 8`, `maxEdges = 12`, `refresh = true`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.

The returned status was `ok` with code `EVENT_INSPECTED_PARTIAL` and `blockers: []`. The report recorded `blockingDiagnostics: 0`, `events: 9416`, `options: 14526`, `entries: 1042`, `unresolvedNodes: 8039`, `terminals: 7590`, `edges: 36618`, `issues: 2095`, `diagnostics: 2095`, and `skippedSources: 0`. The report's workspace-wide analysis was partial because helper projections and lifecycle passes were deferred, which is a tooling boundary rather than a source blocker for this focused tranche.

The authoritative artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/60a8c0c0f565cc38fe0252af1d1b1e9d1fee5130b6b6c7fcd27bcdaba87c0f1b/537f5e48be39efc1fbf4e99b314d1219b90dea12dddeafb1b9f7ae9fb2725ab2/event-lint-9a15393ff4ee.json`. The revision is `9a15393ff4eede78c424d63f9ca5af41987103ce8232d10b0916bbb9fbde51e8` and the graph hash is `10e61ac87ecfc1a95d6515e765ab68da0c9c36db178fa5f043a5991f073b7574`.

## Explicit boundary

The chain remains dormant and outside release-floor credit until the Fallout scheduler, host authority, save recovery, delayed delivery, multiplayer presentation, and runtime Event Log surfaces are proven by the later system pass. This tranche does not claim a Hearts of Iron IV launch or live campaign validation. The exact engine-native all-valid-province thermonuclear sweep remains a separate blocker and is not claimed here.
