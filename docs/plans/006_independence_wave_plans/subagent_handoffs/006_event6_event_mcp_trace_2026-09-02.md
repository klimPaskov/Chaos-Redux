# Event 006 bounded event MCP trace

Date: 2026-09-02

## Scope

This handoff records a fresh bounded read-only HOI4 MCP trace of the Event 006 root event `chaosx.nr6.1`. It adds no gameplay, localization, asset, admission, allocator, decision, category, or pre-event behavior changes.

## Request

The call used `hoi4_event_inspect` with `mode = trace`, `selector = { kind = event, eventId = chaosx.nr6.1 }`, `direction = downstream`, `maxDepth = 2`, `maxNodes = 80`, `maxEdges = 160`, `expandHelpers = false`, `refresh = true`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.

## Result

The route returned `status = ok` and `code = EVENT_INSPECTED_PARTIAL`. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bad097f83a5c3d3af401f543b5da46eb9a84f24250e626dfe0175450369f96bd/2adde93d4402b62b4ce775aa182594756a418685afa896e607bd43476c25799a/event-trace-2725045f62d1.json`.

The returned revision is `2725045f62d14f3536e32f1662ce2fae9f2fae9933ff462de6a8c867d1401570` and the graph hash is `e6c16ff300aa88dfed3e6f55481fdb8ad1e5bb697e6cf3ca888bd82178d7d62d`.

The bounded projection reported 9,722 events, 15,150 options, 1,133 entries, zero helper projections because helper expansion was disabled, 8,680 unresolved nodes, 7,771 terminals, 38,320 edges, zero derived edges, 30,284 state accesses, 2,206 issues or diagnostics, one blocking diagnostic, and one artifact.

## Limitation

The result is partial because the large workspace deferred helper projections and lifecycle passes, and the source inventory was truncated to 64 paths from 367 total paths. The single blocking diagnostic is therefore not treated as an isolated root-event defect without the deferred projections. This artifact is useful engine-linked evidence that the route is inspectable, but it is not full event validation, semantic helper proof, save-load proof, or live gameplay proof.

## Follow-up

A bounded matching `hoi4_event_render` overview was then run with the same selector, downstream direction, depth 2, node limit 80, helper expansion disabled, refresh enabled, and workspace. It returned `status = ok`, `code = EVENT_RENDERED_PARTIAL`, and four artifacts: the manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9d0728a343e2865fb7b50ba7c4cade929c9d23e2ba89ed16d5a0ab717228404/01f656d5fb7bfeb4600be2b2e5e4a55b2b556d794f8dba5038d2191e8b0b3009/event-overview-2725045f62d1-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8e97a32a48b8c3044db6a31bb0d88ac42fcd13abb3c0a0f07f10d9e44758ba07/a5ea51c305e026b1ac363eebf2621fd4aa94adc6aed5cd3b3f99e0c1ece054a6/event-overview-2725045f62d1.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aefda0eb3acc96f94e7feaf9a666c4a63e86706580d2314ac6c52fad7fc3ea3b/4c4ce70fa114326df1f6a7d4c457ed82771a8db0942c518d0e6d1224461f191c/event-overview-2725045f62d1.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4485f2a3eb5a3808becf49f5360fedb17b3fb0788a2e6af14f9c37f523b69059/55096b7e1c459244e4df69183ea9e28408536a8aba873c41b205b4ad32cc5d13/event-overview-2725045f62d1.png`. The render layout hash is `3ba5f18a64912a9ece6fe76dde07333dd05321a92381135e629786aae491844d`; the JSON, SVG, and PNG hashes are `8e97a32a48b8c3044db6a31bb0d88ac42fcd13abb3c0a0f07f10d9e44758ba07`, `aefda0eb3acc96f94e7feaf9a666c4a63e86706580d2314ac6c52fad7fc3ea3b`, and `4485f2a3eb5a3808becf49f5360fedb17b3fb0788a2e6af14f9c37f523b69059` respectively.

The render reports the same deferred workspace-wide helper and lifecycle limitation as the trace and contains no blockers beyond that deferred analysis. These inspect and render artifacts are engine-linked source evidence, not full event validation, semantic helper proof, save-load proof, or live gameplay proof. The Event 006 whole-goal disposition remains HOLD / PARTIAL pending complete country packages, formables, typed probability evidence, GUI evidence, super-event audio rights for slot 23, asset provenance, and broader engine evidence.

A single helper-expanded follow-up used `hoi4_event_inspect` with `mode = state_flow`, the same root selector and workspace, downstream direction, `maxDepth = 1`, `maxNodes = 30`, `maxEdges = 60`, `expandHelpers = true`, and `refresh = true`. It ran to the provider timeout window and returned `status = error`, `code = INTERNAL_ERROR`, `artifactCount = 0`, and blocker `Unexpected internal error`. No source or runtime files changed, and no helper-expanded or lifecycle claim is made from this failed retry.
