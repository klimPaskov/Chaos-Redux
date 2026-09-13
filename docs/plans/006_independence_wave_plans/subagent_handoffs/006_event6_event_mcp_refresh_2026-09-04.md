# Event 006 Event MCP refresh — 2026-09-04

## Scope

This bounded read-only refresh records the installed Event Chain Viewer evidence for the Event 006 root after the current source and GUI repairs. It does not edit gameplay, assets, localisation, or UI files, and it does not claim live execution or save/load behavior.

## MCP evidence

`hoi4.event_inspect` was run with `mode = lint`, `direction = both`, `selector.kind = event`, `selector.eventId = chaosx.nr6.1`, `expandHelpers = no`, `maxDepth = 4`, `maxNodes = 64`, and `maxEdges = 128`. The route returned `EVENT_INSPECTED_PARTIAL` at revision `6d777debfa1f3690688885a2172196d2dd66154ab0219592bc1c2401e1ba2bef`, graph hash `33eb336d444ddc9ca80399973b3f8d9cd3374033681997b70ab351ebdfb4e325`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/080ef33d5cea8d26642bd29538001830b5d420e82ea9f3748b914fc082832f79/50f41a3f9aa3d1b366be1162685b0b5b672a25c4d02ef76011abe04d8142408e/event-lint-6d777debfa1f.json`. The bounded graph reports 9,727 events, 15,155 options, 1,146 entries, 7,762 terminals, 38,333 edges, 30,292 state accesses, and 2,194 issues; `blockingDiagnostics = 0` and `skippedSources = 0`. Its validation remains partial because workspace-wide helper projections and lifecycle passes were deferred, and the inline source inventory was limited to 64 of 368 paths.

`hoi4.event_render` was run with the same root selector and bounded graph limits using `view = overview`. It returned `EVENT_RENDERED_PARTIAL` at the same revision and graph hash, with layout hash `340071ffd5797720635ee88ef724d794ec40a8b419d505221944ec59b8ab1bb8`. The overview manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/39a0ecea14346c987dd8cd39ec298cfb6c232a4bd90464f13117d2cb259bee1e/37b4b31580384cb5ab7c1364766a3bfd81a443fa54f2ca1581961e44397707e4/event-overview-6d777debfa1f-manifest.json`; JSON, SVG, and PNG artifacts are listed in that manifest. The render reports five selected nodes, 42,482 omitted nodes, zero blocking diagnostics, and the same deferred-analysis limitation.

## Interpretation

The fresh receipt confirms that the root event and its bounded overview remain discoverable by the Event MCP surface without a blocking diagnostic. It does not prove that the standalone allocator selects a non-empty plan, that a carrier is released or materialized, that state transfer and host survival complete, that the exact 3/4/5/7/10 ladder fires in a campaign, or that the post-commit report is delivered after save/load. The existing source/static allocator, country API, flags, scenario, FORM-16, GUI-matrix, and no-pre-event checks remain the applicable evidence for those contracts.

## Remaining boundary

Event 006 remains **HOLD / PARTIAL**. No speculative caller, release fallback, admission change, pre-event category, pressure meter, queue, or visible crisis surface was added from this partial MCP result.
