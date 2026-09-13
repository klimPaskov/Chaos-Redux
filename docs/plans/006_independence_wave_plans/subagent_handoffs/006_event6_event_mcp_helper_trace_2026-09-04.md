# Event 006 helper-expanded event trace refresh — 2026-09-04

## Scope

This bounded receipt records a fresh read-only Event Chain Viewer trace for the Event 006 root and its committed public report. It does not edit gameplay, localisation, assets, or UI files, and it does not claim live execution, country release, save/load behavior, or whole-event completion.

## MCP request

- Tool: `hoi4.event_inspect`
- Mode: `trace`
- Selector: `{ kind = event, eventId = chaosx.nr6.1 }`
- Direction: `downstream`
- From: `chaosx.nr6.1`
- To: `chaosx.nr6.2`
- `expandHelpers = yes`
- `maxDepth = 4`, `maxNodes = 96`, `maxEdges = 192`
- `refresh = no`

## Receipt

The route returned `EVENT_INSPECTED_PARTIAL` with no blockers and one linked authoritative trace artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9dc4e9d94fe584008ee7f61d1de4e9983e8c6fd35015b34dcf5481c7f3c37091/93f919b834961bf847250dc4f6c4e4d45401565a6460aaa26e7cb3af5acb0a1c/event-trace-3871d10caa18.json`

The returned graph revision is `3871d10caa18704ff48234b386737b7e2131d36ced10b152ce00da10f03a3292`, with graph hash `49bf9e4f19e502a0a29d89221525132c300d329e54232d6d2c60237d724a0060`. The bounded report contains 9,728 events, 15,156 options, 1,146 entries, 7,763 terminals, 38,335 edges, 30,292 state accesses, and 2,195 diagnostics. It reports zero blocking diagnostics and zero skipped sources, while the large-workspace helper and lifecycle projections remain deferred and the inline inventory remains limited to 64 of 368 paths.

## Interpretation

The helper-expanded route is useful structural evidence that the root-to-report boundary is discoverable in the current workspace, but its partial validation status does not establish allocator semantics, non-empty candidate selection, absent-country materialisation, host survival, synchronized transfer, report delivery, or persistence. No source patch is justified by this receipt alone. The existing no-pre-event gate and the 32-attested/29-group/40-adapter/161-unattested boundary remain unchanged.

## Validation boundary

No live game, save/load, or player-owned runtime observation was performed. Event 006 remains **HOLD / PARTIAL** pending the documented package, identity, rights, probability, GUI, asset, super-event, and central-attestation gates.
