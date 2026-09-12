# Event 006 current MCP evidence baseline — 2026-09-12

## Disposition

Implemented as read-only evidence. No gameplay, GUI, focus, event, asset, localisation, or catalog source was changed.

This handoff records fresh current-checkout evidence for the root event, shared focus tree, Statehood Ledger GUI, and package-planner probability surface. It does not promote Event 006 beyond the existing HOLD / PARTIAL boundary and does not claim live game, save/load, or runtime transaction completion.

## Event root

The focused `hoi4.event_inspect` request used selector `event:chaosx.nr6.1`, `mode = lint`, `expandHelpers = no`, `maxDepth = 2`, `maxNodes = 300`, and `maxEdges = 500`. It returned `EVENT_INSPECTED_PARTIAL` with one source-linked lint artifact:

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/db00371cb3714eec0ac6e613ef38b6a5cc8519f141acf2a26f55cdbac054b754/e648a8281580508e333678b18e5e1804e52b201c60e19de504ed6abf19a2e7d5/event-lint-4bccb6ec7fe1.json`
- Graph revision: `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`
- Graph hash: `24f73f1a61d57d7a3c99c927d106bf7fd7fe21299898bf43d3d8eab152165819`
- Workspace counts: 9,741 events, 15,167 options, 38,369 edges, 8,737 unresolved nodes, 2,199 diagnostics, and one blocking diagnostic in the aggregate workspace analysis.
- Limitation: helper/lifecycle projections were deferred, so this is partial source-linked evidence rather than a complete event-chain proof.

The matching `hoi4.event_render` overview returned `EVENT_RENDERED_PARTIAL` with source-linked JSON, SVG, and PNG artifacts:

- Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8e01c808fa5fe8a7c56b7624fe2b3dcaee3a006769f19561cef4a38dce627353/5ae4ea50cd5dccc1531baf8d0ffeeec74fb78a17027786e9671451c898d594d3/event-overview-4bccb6ec7fe1-manifest.json`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/adb241308733a54ab7193444647b3f79f54969995684fe2d2ab1700905109318/ee89cedc091df2e2c3a65057a9f0f143ba9e834be66d70a6298e6eea841da016/event-overview-4bccb6ec7fe1.svg`
- PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/76a6b0a1485d8f4109f07404805a6ce3e1f27dcacc7ef0d7a24619ca958d530d/65297e438f94411a72b5fa753216fcda4104d7ccce3a342d299832c9620c545b/event-overview-4bccb6ec7fe1.png`
- Layout hash: `3ba5f18a64912a9ece6fe76dde07333dd05321a92381135e629786aae491844d`

The event inspect and render share the same graph revision and remain explicitly partial.

## Shared focus tree

The focused `hoi4.focus_inspect` request targeted `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, and returned `FOCUS_INSPECTED` with validation passed.

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bdc30f89331349afab947fb784e0e5777b3d31e16f0e5e2b11dc8486e669d372/945eede58d1851cc1d44c219062ca6ce63f30cc2eab1b36571f9b9fbb4ac06e5/focus-inspect.a62b4724125f17da.json`
- Focus count: 184.
- Connector count: 196.
- Crossings: 0.
- Node intersections: 0.
- Too-close same-row pairs: 0.
- Maximum horizontal span: 10 columns; one long connector warning remains for the shared military-to-reclamation path.
- Layout hash: `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`.
- The only other diagnostic is an unrelated vanilla continuous-focus localisation warning.

The matching `hoi4.focus_render` returned `FOCUS_RENDERED` with source-linked HTML, SVG, JSON, source-map, and plan artifacts:

- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/febdb7cdc0279bc4bd153479733d6eb67210692dd0b3fda9a3e7c38faf0ada4d/independence_wave_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e40d7bffd70e2530e888d825101629c15ea64856e4676919fa6fffe1f4eb656/5637f8796e64f0a5bad36b6d3c1b31b8e17109701adaff9fab323ce000523ec1/independence_wave_focus_tree.focus.json`
- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78edab8a1b6417a000bea5996757dab5470a6dbb187c44e87e0d67174cc06a66/397f460c65572c7002fd8f5d1aac91228101b5b87bddc5ba7ba7adb5529c2a5e/independence_wave_focus_tree.focus.html`

No focus rewrite was justified by this evidence.

## Statehood Ledger GUI

The exact accepted baseline fixture was used for `independence_wave_status_window`:

```json
{"id":"event006_status_repair_baseline","resolution":{"width":1920,"height":1080},"uiScale":1}
```

`hoi4.gui_inspect` returned `GUI_INSPECTED` with 48 inspected Event 006 elements, zero missing resources, and validation passed. The source graph is complete for the bounded fixture, but the renderer reports 64 non-blocking visible-overlap findings, four unsupported blend-frame cases, four static-fallback resolution warnings, and twelve unresolved fidelity entries. The fixture does not exercise hover, selected, locked, disabled, warning, active, completed, list-boundary, long-text, or missing-localisation states.

- Inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/540a34c94852d79e8ed27fe44a3f29dea658df2230b8216a2e3b34b233dff2a0/a6ab97621a8fd8553454c3383c4c171727af641bc5c22a7d5e14b0d57f0dd831/gui-inspect.002afb7d0452a975.json`
- Rendered full PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b69c93a2569d4392d07bd27e1e37652f29cc4edbbecb1d183e58f5d02b41c284/72604e23c1b95e76d97e59f78a75b721d66153847bf8c7df44081d45e80aa01a/independence_wave_status_window-full.png`
- Cropped PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/85019c3dc77eaec0799fe1b0d0806d2f2942cddebc8fa67357627747fa5a77e4/68ac62d34bb57adb8694860362c145d1a1bc002db964a01b8a1306595fa6d3d1/independence_wave_status_window-cropped.png`
- Click-region PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6eb93da154f832d2b6df86dfb764b56b893af485e1ce1e537e5135601b85f24/ff886b54de42c1c1c8d620a1050e2c4e3eea3b5cdc2cd5aa92a11fffaf3baf64/independence_wave_status_window-click-regions.png`
- State matrix JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f75154ec46d0073b647f78f1d870ffea41d5add0b538d832ca2e02cee057978a/84f964bdf4a9f1e8e788e29afe024ae28b0d1662daf4ec3369fd257e1ea5996b/independence_wave_status_window-state-matrix.json`

The matching `hoi4.gui_render` returned `GUI_RENDERED` with 27 artifacts, one explicit state, one scenario, and one resolution. Its `changedPixels = 0` comparison is the renderer's self-comparison and is not a repair proof. Dynamic tab visibility, click-region behaviour, blend-frame playback, and live consumer behavior remain unresolved; no layout edit or fallback was introduced.

## Weighted package planner

The mandatory first probability call used adapter `custom_weighted_pool` against `common/scripted_effects/006_independence_wave_package_planner_effects.txt`. It returned `PROBABILITY_SOURCE_INSPECTED` with no discovered candidates and `poolComplete = false`.

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/964217d5fb77dad1e3925ae9aae8f3a67a59ea9802d8651b1b78908362b5940d/9f89bd705cc64075f2439454f359e0137f87ca73c4450131d8597427361cb244/probability-inspect-b8d529ef8404.json`
- Source revision: `fa97953a5f8a1d617e6a3036bc856fd08628fac7c4b7a75d673cef7c1a4b0442`.
- Candidates: 0.
- Available candidates: 0.
- Pool complete: false.
- No quantitative balance patch or comparison is justified by this result.

## Source validators

The focused source validators remain the authoritative static checks: allocator strict mode, country API, strict flag families, FORM-16, GUI semantic matrix, and SCN-008 scenario matrix all pass at the current boundary of 32 attested packages, 29 compatible groups, 40 adapters, and 161 unattested selectable rows. These checks do not prove live release, save/load, or dynamic GUI behavior.

## Remaining blockers

Event 006 remains HOLD / PARTIAL. The current evidence still leaves the 161 unattested package rows, adapter-only fail-closed packages, dynamic GUI fixtures/playback, grounded portrait rights and consumer gates, flag provenance/ownership, formable and league emblem identity, super-event audio 23 rights/reachability, super-event 24 reachability, typed probability scenarios, and live/runtime transaction proof unresolved. No fallback or simplification was introduced.
