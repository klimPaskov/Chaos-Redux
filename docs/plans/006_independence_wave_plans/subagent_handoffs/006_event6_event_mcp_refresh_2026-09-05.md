# Event 006 Event MCP refresh — 2026-09-05

## Scope and disposition

This is a read-only structural refresh of the Event 006 root event after the current worktree documentation and source reconciliation. It does not change gameplay, assets, GFX, GUI, localisation, or the package boundary. The result remains **IMPLEMENTED / SOURCE-STRUCTURAL ONLY / HOLD-PARTIAL**.

## Inspect receipt

`hoi4_event_inspect` was run with `mode = lint`, selector `event:chaosx.nr6.1`, `direction = both`, `maxDepth = 8`, `maxNodes = 1000`, `maxEdges = 3000`, `expandHelpers = yes`, and `refresh = yes` against workspace `mod_chaos_redux_ea3b2d67c2c0`.

The route returned `EVENT_INSPECTED_PARTIAL` with revision `fa39cc8b8775d170afcffd913b819e19d58668724ce547e0ec5a30ae5e8610a1` and graph hash `3f50c1f524100609b34403d4c61e9e9411f91a72356e9b2f987184d30d893fe1`. The focused projection reports 9,742 events, 15,167 options, 1,146 entries, 8,705 unresolved nodes, 7,772 terminals, 38,363 edges, 30,318 state accesses, and 2,198 diagnostics, with zero blocking diagnostics and zero skipped sources. The only validation failure is the adapter's explicit deferral of workspace-wide helper projections and lifecycle passes.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/97792c4e7c2d555d49da66f38481112e6f45274b9df8a2dfade781ebe412d8b4/6d83b870fa62351ab47a096fd36bc51d24bbce425e99794a56acfd12efb996b8/event-lint-fa39cc8b8775.json`.

## Render receipt

`hoi4_event_render` was run with `view = overview`, selector `event:chaosx.nr6.1`, `direction = both`, `maxDepth = 8`, `maxNodes = 240`, `expandHelpers = yes`, `includeHtml = no`, and `refresh = yes` against the same workspace. It returned `EVENT_RENDERED_PARTIAL` at the same revision and graph hash, with layout hash `340071ffd5797720635ee88ef724d794ec40a8b419d505221944ec59b8ab1bb8` and five selected nodes in the bounded overview. The adapter again deferred workspace-wide helper/lifecycle analysis; no live or semantic execution claim follows.

Overview manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72d63b2dc2e56dd4891e4e68e05b6df030cba512b15b0fe0701fcc7fd528e9f2/f74098b91ee27e101459bdbd7f2a592567237a3f4a7a6829b5cfac31af4db532/event-overview-fa39cc8b8775-manifest.json`.

## Interpretation and remaining limits

The refresh confirms a discoverable structural `chaosx.nr6.1` root and bounded overview path in the current source projection. It does not prove non-empty allocation, country release or materialisation, state transfer, host survival, report delivery, save/load behavior, dynamic GUI state, or live campaign balance. The exact 3/4/5/7/10 ladder, World Collapse-at-10 rule, and absolute no-pre-event surface remain governed by the existing source/static validators and authority handoffs.

No source patch is justified by this read-only refresh. No staging, commit, or live Hearts of Iron IV launch was performed.

## Same-day current-tree refresh

A second bounded read-only pass was run after the current worktree source changed, using `mode = lint`, selector `event:chaosx.nr6.1`, `direction = both`, `maxDepth = 6`, `maxNodes = 800`, `maxEdges = 1600`, `expandHelpers = no`, and `refresh = yes`.

The route again returned `EVENT_INSPECTED_PARTIAL`, now at revision `e091020adf34299c1e93af123d1bb753d635425c184ec02041ab916cb5aa8aab` and graph hash `aae5099fa1e256de5e77691cd0df5206c24064975ba60f2020a749dc840a5552`, with the same 2,198 non-blocking diagnostics, zero blocking diagnostics, and zero skipped sources.

The matching `hoi4_event_render` overview returned `EVENT_RENDERED_PARTIAL` at the same revision and graph hash with layout hash `340071ffd5797720635ee88ef724d794ec40a8b419d505221944ec59b8ab1bb8`, five selected nodes, and 42,527 omitted nodes under the bounded view.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e3ca75ed54d0e9892f1354d4902eda81b9cf527d5f44b1c348d74ac2e35b28a6/b5f2cf85fe613b95a1891c71eeb7a4c1c398acb3ed401711a98995bd02a7ddfb/event-lint-e091020adf34.json`.

Overview manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ceb9bd7658076621d9499a0119cca20e452017eb8e58a6817e68f4d147fd9e2/336086bee31cdcbfeab976915a9a816a0f707b2826b29826b6d8652a76b596b4/event-overview-e091020adf34-manifest.json`.

This refresh supersedes the earlier same-day structural hashes for current-tree traceability only; helper and lifecycle projections remain deferred, and no allocation, release, materialisation, transfer, report, save/load, or live behavior is claimed.

## Same-day state-flow retry

A bounded read-only retry used `mode = state_flow`, selector `{ kind: event, eventId: chaosx.nr6.1 }`, downstream direction, `maxDepth = 2`, `maxNodes = 120`, `maxEdges = 240`, `expandHelpers = no`, and `refresh = yes` against the same workspace. The route returned `status = error`, `code = INTERNAL_ERROR`, and no artifact after the provider timeout window. This does not replace the successful partial lint/overview receipts above and adds no semantic, runtime, or live-game evidence.
