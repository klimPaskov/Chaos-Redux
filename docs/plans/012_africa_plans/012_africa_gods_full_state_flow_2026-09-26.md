# Event 012 Gods full state-flow inspection

Disposition: **partial validation evidence**; the Event 012 chain remains incomplete for engine-facing acceptance.

## Query

On 2026-09-26, `hoi4.event_inspect` ran in `state_flow` mode with selector `{kind: event, eventId: chaosx.nr12.600}`, `expandHelpers = true`, `maxDepth = 5`, `maxNodes = 140`, `maxEdges = 400`, `refresh = true`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.

The tool returned `status = ok`, `code = EVENT_INSPECTED`, `analysisMode = full`, and no top-level blockers.

## Result and coverage

The inspected workspace revision is `1150ca32800674353eb7ab80a3019422c5e0ca45def2062bfc1bbc2c858177cb`, with graph hash `5084e6d083dfdad955cc1286c80eee813c90be3d8d579772f31ee53654b8c467`.

The narrowed selector still produced workspace-wide aggregate counts: 9,835 events, 19,643 helpers, 328,171 edges, 357,943 state accesses, 29,396 unresolved nodes, and 3,911 blocking diagnostics.

No source was skipped; the inline file list was limited to 64 paths, and the chunk-index manifest reports a 4,053-source inventory with a truncated retained hash list.

The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5bb4c345a1a29937edea90f2a341a054946f404b9a4a7f91bed837da075a9a00/f62a27419e169d14dae3f9b55f87af9093810ae621f34749acef297ed91a4b98/event-state_flow-1150ca328006.json.77d7289c8215af33.chunks.json`; it indexes a 464,004,942-byte four-part report.

Because the diagnostic total and helper counts are workspace-wide and the retained source inventory is truncated, this result does not establish which findings belong to Event 012 or prove its lifecycle behavior.

The earlier focused `.600` inspect/render remain partial for helper and lifecycle coverage; the broad `state_flow` run confirms that full analysis is available but is too aggregate to close this feature's event evidence.

No gameplay source was changed for this inspection, and no campaign execution, runtime activation, or live-game result is claimed.

## Remaining evidence

Event 012 still requires source-linked lifecycle and scenario evidence that isolates its owner, generation, Evolution I clock, activation gate, and teardown paths.

The accepted focus-route scope, weighted AI scenario comparisons, and live-game validation remain separate completion gates.
