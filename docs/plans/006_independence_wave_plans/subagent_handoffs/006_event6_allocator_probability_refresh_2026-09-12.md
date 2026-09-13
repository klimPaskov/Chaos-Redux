# Event 006 allocator probability refresh — 2026-09-12

Status: bounded read-only post-repair probability receipt. The allocator source repair and the strict Event 021 origin gate are separate owner-applied source changes; this handoff records only the fresh MCP evidence after those changes. No weights, package admission, fallback, player surface, or tuning target was added here. No live game, save/load, campaign-balance, or complete before/after claim is made.

## Fresh outer inspection

The mandatory first weighted call used `hoi4.probability_inspect` with adapter `random_list`, source `common/scripted_effects/006_independence_wave_effects.txt`, `refresh = yes`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.

The receipt was `PROBABILITY_SOURCE_INSPECTED` with `poolComplete = true`, 14 candidates, 14 required inputs, zero unresolved inputs, and zero available candidates under the empty fixture. The MCP source revision was `24638467a21a0185ce7eea277f8e695238b3a487dbbf91bf484c6c6e6f8e05e9`; the source hash was `c2476a82a86e16000c5085f85a95eb32ed9540fda3777d99ff712a2c2448801f`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/20274934732c72ca0abe92b5e8551336821dd06f26cbc74f1da4eb5129aa8e0d/a1f71905bbbe4462db865d8c65cd10f2ab5bf8efb02adb65871d089825e9567f/probability-inspect-c2476a82a86e.json`.

The MCP candidate identifiers are source-entry IDs (`common/scripted_effects/006_independence_wave_effects.txt:3571.entry.1` through `:3571.entry.14`), not the dynamic weight-variable names. A first compare using the variable names therefore returned `PROBABILITY_SURFACE_EMPTY`; the corrected source-entry pool was used for the bounded control below.

## Same-source comparison control

`hoi4.probability_compare` was run with adapter `random_list`, the corrected 14 source-entry IDs, the current source path on both `before` and `after`, and the named scenario set `E006_ALLOCATOR_LADDER_2026_09_12_POST_REPAIR_CONTROL` containing `ALLOC_UNIFORM_COMPLETE`, `ALLOC_CALM_3`, `ALLOC_RISING_5`, and `ALLOC_WORLD_COLLAPSE_10`.

The route returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-3e2af12640997f6bf6024509`, source revision `24638467a21a0185ce7eea277f8e695238b3a487dbbf91bf484c6c6e6f8e05e9`, source hash `c2476a82a86e16000c5085f85a95eb32ed9540fda3777d99ff712a2c2448801f`, scenario hash `c0c7a8af1fd970a487c7270dfd099602d2821606d524d6a5bb4263dbb6b587dd`, 4 scenarios, 56 candidate-scenario rows, 14 unresolved items, zero diagnostics, and `comparisonChanges = 0`.

Artifacts:

- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f135a434709e81469d1730fe654e9a5121f0717bd0f647a9c5d769ed6830bb3b/d887ac72cf45431d32dde6f63f07ee9a5091a31c0b030cdf1211e51466b60d40/probability-3e2af12640997f6bf6024509.json`
- comparison SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/936fc26b06f67d291cd739468543a8047b5df14233b0ae98426e05aa73f90af3/probability-probability-3e2af12640997f6bf6024509-comparison.svg`
- comparison PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a1fd8e11d21dd2414c85f7412d454fa53b5b857ed9fb09593caa20f6277f498f/b6f72942c5a6fd44448f7fea55696e33c4a44003b1eb3c7f74856fdc6e68ac0a/probability-probability-3e2af12640997f6bf6024509-comparison.png`
- unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b376452dd35a669b20b3ba5787e6af6347617460240eb4e6e0da2f2ae9a45962/c8ce495e9a1bd06eeae246f486e90ebacdda22bf2afd817d9af8e3bd6eb1768d/probability-probability-3e2af12640997f6bf6024509-unresolved.svg`
- unresolved PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/443748d25cfe2d3c7c73f1357d1647f95e14a3a02a6d877b89d4c6a07af3fc50/4d6f9d2c09c86d8998ca3a111f0bbc781d5c635b211d08905f671332e56ee454/probability-probability-3e2af12640997f6bf6024509-unresolved.png`

This is a same-source capability/control receipt only. The installed adapter cannot address a pre-repair source revision through a revision-qualified path, so `comparisonChanges = 0` must not be read as proof that the allocator repair has no semantic effect. The 14 unresolved items and the empty fixture also prevent a campaign probability or balance conclusion.

As a separate structural receipt on the same checkout, a narrow `hoi4.event_inspect` lint for selector `{kind: event, eventId: chaosx.nr6.1}` returned `EVENT_INSPECTED_PARTIAL` at revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`, graph hash `24f73f1a61d57d7a3c99c927d106bf7fd7fe21299898bf43d3d8eab152165819`, 9,741 events, 15,167 options, 1,159 entries, 30,451 state accesses, and one deferred-workspace blocking diagnostic. The matching overview render returned `EVENT_RENDERED_PARTIAL` with layout hash `118888ec7d6771854b8f62f596ed4f25c9bbdcb117a9e47a91f177e7fec7a571`, three selected nodes, and 42,569 omitted nodes. Lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6eeb66681b9568658ee015638fba6e28360858104df2e5b19e03112a74699b51/4433437331be222dba4df3da25608c7855a59cab3a3e326e9abcee7ecf0d4d44/event-lint-4bccb6ec7fe1.json`; render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7061ca853a1bc761f1b6ff99c6d16ddd29def90d88bdbef7fa3f268f4b5f45b7/8184738e0ba48c893ed74aec3aa1060e7b33960fc3801d8d43b93fe07593d3f0/event-overview-4bccb6ec7fe1-manifest.json`. These artifacts are structural only; helper/lifecycle projection remains deferred.

A later narrow `state_flow` retry for the same root returned the exact MCP error `INTERNAL_ERROR / Unexpected internal error` with no artifact. This is recorded as an engine-tool limitation rather than source proof of the reported zero-country symptom.

## Disposition and next owner

The outer declared pool is current and complete for source discovery. Nested package selection, typed external gate state, package-level normalization, and live release remain unresolved. Preserve the exact `3/4/5/7/10` ladder and World Collapse 10 fail-closed contract.

The next weighted pass requires a revision-capable before/after source pair or an approved pre-repair snapshot, plus a typed manifest for package existence, attestation, host/anchor control, reservation collisions, prior-wave arrays, capacity, Event 005 collision state, attempts, and terminal transitions. Until then, this handoff authorizes no numeric weight or balance change.
