# Event 014 MCP continuation audit

Audit date: 2026-08-25.

## Scope

This continuation pass used the installed HOI4 MCP against only Event 014 surfaces that can be attributed to the package: the Event 014 event root, the three Event 014 national-focus trees, the Event 014 technology/sub-unit surface, and the five direct Event 014 scripted-GUI windows. It did not inspect or edit the shared event log, shared Event Details framework, settings UI, unrelated scripted GUIs, or other event packages.

The pass also rechecked the remaining Meshy task records without spending credits. No provider task was promoted and no model fallback was fabricated.

## Event MCP evidence

`hoi4.event_inspect` lint for `chaosx.nr14.1` returned `EVENT_INSPECTED_PARTIAL` with revision `cf24a2714b309f2f8ffbee3502ecebced0e905ed52bbd92c8e3fd9d2cd476ad4`, graph hash `a3d0aa19ed4e7a228a55b45ad27d10197bdbcc8e8e432d7828a0427403596457`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79d4ca45241df8750f9343726ae9fc8e1d639b234a83f334c7e2b7f6903ca253/861206de46b0d48ad7003b3e3fa33a8a41f2084b5067f023831b41bcb17b8511/event-lint-cf24a2714b30.json`.

The workspace scan reported 9,515 events, 14,711 options, 1,073 entries, 8,317 unresolved nodes, and 2,130 issues across the whole workspace. It retained zero blocking diagnostics and skipped no source files, but deferred helper projections because the workspace is larger than the MCP inline-analysis ceiling. This is useful root-level evidence, not complete proof of every Event 014 helper path.

A downstream trace using the same root selector returned `EVENT_INSPECTED_PARTIAL` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fd79db346b415d43553e373360ef106614e5e6e66583921a72cb8d4fba0dd834/4f146ec9d7d44bcaf33e447ce6e908fd2c145ccb26b46ea7af49011876662a62/event-trace-cf24a2714b30.json`. It retained the same revision and graph hash, no blocking diagnostics, and the same deferred helper/lifecycle limitation.

A bounded `terminals` render also returned `EVENT_RENDERED_PARTIAL`, with artifacts `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a0c2b77ce9c09a1138f0aad4fac01c04c4284833c1b28d3373de95fb91ab83d/5e90d30613aa6dd3758abacfe1da14ee4c36490d9a139dc0b50d5b38b4113e9e/event-terminals-cf24a2714b30.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/26a0c46ec50d93379f0197fb1af087a82eaa518b5d927ee0b56dfa82aa19c641/2b8adea10d1f10dc93fee1816d59f0382ecafe1f990024386c0af1c4f94ab42e/event-terminals-cf24a2714b30.png`. The renderer reported `selectedNodes = 0`, `branchRenders = 0`, and 41,267 omitted nodes, so it did not produce attributable Event 014 terminal branches. This is recorded as an adapter boundary, not as evidence that terminal branches are absent.

## Focus MCP evidence and bounded source fix

The final source keeps all three roots in `common/national_focus/014_cannibalism_focus.txt` and was inspected after the bounded Wendigo terminal-column adjustment.

| Tree | Focuses | Connectors | Crossings | Node intersections | Long connectors | Event 014 diagnostics | MCP artifact |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `cannibalism_unified_focus_tree` | 108 | 103 | 0 | 0 | 0 | 0 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69109cbf7fe26b3b1d2dd9c5c0ed63a460ea6a491482351abdc1063152dab1a5/b6295e79613f51106774c93bc466fa57a14e500d7f4383f9b2844c7e709ed2d0/focus-inspect.c155b3cf8590717f.json` |
| `cannibalism_warlord_focus_tree` | 68 | 79 | 0 | 0 | 0 | 0 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7852ef1cdc8bd6d3e9e4b96c03626d0c6cab0e96c017088e4314f8cea85d430a/2a906126a6fd801c2721bf3e658cb9ab6133bdb56ea2aef2f0b54194d9387d11/focus-inspect.c155b3cf8590717f.json` |
| `cannibalism_wendigo_focus_tree` | 28 | 28 | 0 | 0 | 0 | 0 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b706548e594b772c302b205446a240061fbda351f560db93c738eafb17fefe84/e88eb5e5159b56dd52c3a94f3b8dcfc5e61a7f83cd0c84fb40a9d5bc85d218df/focus-inspect.c155b3cf8590717f.json` |

The Wendigo tree previously drew a three-row direct connector into `ZZZ_wendigo_begin_the_countdown`. The source now places the visible terminal column at y 7–10 (`begin_the_countdown`, `designate_the_last_hunt`, `hunt_every_remaining_capital`, `the_world_beneath_winter`). The gameplay gate remains unchanged: the `available` block still requires acceleration, stabilization, winter-network, frozen-larder, and inheritance completion. The final inspect reports maximum vertical span 1, zero crossings, zero node intersections, zero long connectors, zero same-row spacing violations, and `diagnosticCount = 0` for all three trees.

The accepted final raster artifacts are:

- Unified PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7de28d8e356296f3cdf59ed0493a484414ee3cd638d9e3edb55fc08293a17e69/3ac336ca35cf1b492cdc7cb99cd63211c2d4af4d05f170e66599287140f20a52/cannibalism_unified_focus_tree.focus.png`, 3,792 × 2,212.
- Warlord PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e36d35590764bc329967bb4ac4ec5886bc24e7f39088002fd1ccfc54a27a7ad3/ff2fe4c21a5986f1184b036be354bf3894b75efe50a15c837ffcabe673ac1c3e/cannibalism_warlord_focus_tree.focus.png`, 1,872 × 2,068.
- Wendigo PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aed780aa5d38ee70a95fea59068bc8c267452e693ac2b7075d5a0dacb717e0d2/9d7d58fd52184ee694b4d5ceedf730c7da03a38fd6c0e95d6896d4e187e571d2/cannibalism_wendigo_focus_tree.focus.png`, 1,680 × 988.

All three raster calls returned `FOCUS_RASTERIZED` with the only remaining warning being the unrelated vanilla `continuous_restrict_freedom_desc` localisation reference.

An earlier compact `hoi4.focus_rewrite` experiment was rejected and reverted because it expanded the tree, introduced crossings, and created long connectors. No focus sidecar remains and the final source hash matches the bounded coordinate patch described above.

## Technology and sub-unit MCP evidence

`hoi4.tech_inspect` unlocks probes were run for `cannibal_bone_riders` and vanilla `elephantry`. The Bone Riders artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/15ca0ecbb432132662656662f912f64e2470ec73dfb3f59e08e8b538767fdf9c/c32e4f541e290f6442966beb76c8a6858336baf3ab2c57b8d17aa75633d3961a/technology-unlocks-b248d7a81afa.json`; it confirms the resolved `cannibalism_bone_riders_tech` -> `cannibal_bone_riders` unlock and two confirmed Event 014 external grants from the unified and warlord setup helpers, with no report issues. The vanilla elephant artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/29582e5434402ad7e592d23ddf703b551155f07163c81edd572dbd37f5228ab3/c5ee7b6e97f17ad4d2874707ba59a3f01a9bb2acaa321194ce85c7929d27aad3/technology-unlocks-b248d7a81afa.json`; it confirms the installed vanilla `elephantry` sub-unit and its resolved vanilla technology unlock plus Event 014 unified, warlord, and Wendigo grants, with no report issues. Both artifacts remain `complete = false` only because large-workspace helper projections are deferred, not because these selected unlocks are unresolved. A broad lint artifact, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a465e0b0eeebcb1d893ef01bc1c98bd43d8082757b9e05a04d4aff40e917c72b/4aff61af0dfb5f0060b42c03e406196fb69e21739504647fb3c5b76e12cbc692/technology-lint-493119fa53d0.json`, still reports 672 technologies, 18 folders, 457 edges, 850 unlocks, 19,806 references, and four unresolved nodes at workspace scale. The selected unlock evidence is therefore stronger than the broad lint summary, while source review remains authoritative for the hidden bridge effect design.

## Direct GUI MCP evidence

The fresh direct inspect for `cannibalism_early_header_window` in scenario `event014_early` returned 17 owned elements and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b941e30a52590df6e40a0146249c91cb2dda52f9b46dddf4a5aedd2f9d2f0ab/746ebf3b52dbaf84c8ac0c62f09434c3e666f1d691d4ca8cf2251b4cb84f2047/gui-inspect.186e6bd25a629bc9.json`.

The GUI adapter retained 1,999 diagnostics and dropped 1,654 at its global ceiling. The retained set was dominated by 1,648 unrelated index-symbol collisions and unattributed global scripted-context, overlap, clipping, text, and animation-fallback findings. Because the response omitted reliable Event 014 element attribution, no source rewrite was justified. The existing five-window GUI handoff remains authoritative: the direct GUI matrix is still partial evidence, not a visual acceptance claim.

## Meshy/provider boundary

The same continuation rechecked the four open model families without spending credits. The balance remains 10 credits. Scavenger and Island have succeeded provider geometry candidates but no accepted rig/action/reimport package; Network has no queryable action lease; Bone Riders has no accepted compound horse/rider route. The required eight substantive actions alone exceed the balance, so no static, transform-only, aliased, Blender-authored, or generic fallback was promoted.

## Disposition

The focus coordinate patch is accepted and source-owned. The event, focus, technology, GUI, and provider evidence above is recorded, but Event 014 remains incomplete until the four model/action packages pass the Meshy-to-PDX acceptance gate, the direct GUI matrix becomes attributable across supported resolutions and states, the deferred large-workspace analyses are narrowed or resolved, and live consumer validation is supplied by the user.
