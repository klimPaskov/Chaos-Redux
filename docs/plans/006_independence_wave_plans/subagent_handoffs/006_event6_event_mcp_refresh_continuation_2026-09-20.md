# Event 006 event MCP refresh continuation (2026-09-20)

## Disposition

`IMPLEMENTED STRUCTURAL EVIDENCE / RUNTIME AND LIFECYCLE OPEN`.

This receipt records a fresh read-only Event MCP inspection of the Event 006 root, publication event, and SCN-008 carrier against the current workspace. It does not promote package admission, allocation, release, formable reachability, probability, GUI, save/load, or live-runtime completion.

## Inspection scope

The workspace was `mod_chaos_redux_ea3b2d67c2c0`.

The inspected selectors were `{ kind = event eventId = chaosx.nr6.1 }`, `{ kind = event eventId = chaosx.nr6.2 }`, and `{ kind = event eventId = chaosx.triggerable_scenarios.80 }`.

Each `hoi4.event_inspect` call used `mode = lint`, `direction = both`, `expandHelpers = no`, `maxDepth = 2`, `maxNodes = 300`, `maxEdges = 900`, and `refresh = yes`.

## Inspection evidence

All three selectors converged on revision `a2e598a947202af38ebdfe2a72c6a8429e76df2403d31aef64b286a0cfeebc75` and graph hash `d15306b4fcafbeb1bbc71e8ffba5f60a6446412c6099e96a4f75c5ab0bd90e08`.

The focused reports contain 9,745 events, 15,179 options, 1,160 entries, zero helper projections, 8,771 unresolved nodes, 7,768 terminals, 38,416 edges, 30,548 state accesses, 2,198 aggregate issues, zero blocking diagnostics, and zero skipped sources.

The adapter reports that the large-workspace helper and lifecycle projections remain deferred, so `validation.passed` is false for that coverage reason rather than because a blocking diagnostic was found.

The three linked lint artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93788f20b903b4f014110528de0cd0a90a31bb68b24f280ca3746a27f5a954ca/6f54ba72a9e72824682bc26e4ee115e615992c76516774018b32a78e926981cb/event-lint-a2e598a94720.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/53adbeccc88551715d14e17f72313e4f327687960c614ace2a49f99df1864194/3bf7af676571cc51cb4bf5d90a4b5beb5bde0b431ab24052d0f12993a63349ff/event-lint-a2e598a94720.json`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f79fe6803018f1873898f2ffc5f241f29da9b674a110621729f249c9bf437dee/adcbf4ce5950aa243f252a7924b0a389734dfe2b4647d5521413b77d5be87dde/event-lint-a2e598a94720.json`.

## Render attempt

The first overview request was rejected by the live schema because `maxNodes = 300` exceeds the native render cap of 240.

A corrected read-only `hoi4.event_render` request used `view = overview`, the Event 006 root selector, `direction = both`, `expandHelpers = no`, `maxDepth = 2`, `maxNodes = 200`, and `refresh = yes`.

The corrected render timed out while awaiting the service's 180-second tool-call limit and produced no render artifact.

No visual or render acceptance claim follows from this attempt, and no source fallback or GUI change was introduced.

## Bounded option render

A narrower read-only `hoi4.event_render` request used `view = options`, selector `{ kind = event eventId = chaosx.nr6.2 }`, `direction = downstream`, `expandHelpers = no`, `maxDepth = 1`, `maxNodes = 20`, and `refresh = no`.

The request returned `EVENT_RENDERED_PARTIAL` at revision `316825c8445e7868f05adbf83dd97f211030552e30b1ca364eb0c1b0084471fd`, graph hash `0dd8e81476fcc416cf28b005f3cfbbb47673171dd484601e27aa04e981dd309e`, and layout hash `642304747a6f09986be77c2b7543bfc6337755f5249f1238b2d31e14b362deaa`.

The result reports 9,744 events, 15,179 options, 1,160 entries, zero helper projections, 8,770 unresolved nodes, 7,768 terminals, 38,414 edges, 30,541 state accesses, 2,198 aggregate issues, zero blocking diagnostics, zero skipped sources, three selected nodes, and 42,618 omitted nodes.

The returned diagnostics contain only the non-blocking `MCP_INLINE_FILES_TRUNCATED` condition, with 374 total diagnostics and 64 returned inline; no branch render was produced.

The render artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b8d925b2ea22705af57bb03dcb81e652e3be6907d8a756009b9659007449922f/f92d1799e6eaaa76ab0f64e5ae6fa01c55ad7295e31bf06ea69796833b3b4292/event-options-316825c8445e-manifest.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ae11d20e16322646d43fd8af82b114668567e35400a6c7a95254f298ac7cc83/563021e2a54a9348e32421f123f9dda1ced479e50ce91072662c148d5b36e51d/event-options-316825c8445e.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1c1f2c62da730fac2fe2bd34ef068767b524938eaa692055559844fd88b26b2/e1faf5ceec2ec663444be8a91b6b24e9d7c9d6b52ebe3f819a4b38cb816709cd/event-options-316825c8445e.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4325a80409081705a2177cc15f820f05a689126633e4398eb552c6c269e5e5f4/92694e9ad8c6e96f6a9aef0c0614f87e1b66a04b872436ec3babc5f9e7333a15/event-options-316825c8445e.png`.

This bounded result adds option-surface render evidence only; the selected-node and omitted-node counts, helper/lifecycle deferral, and absent branch render keep native visual acceptance, runtime execution, save/load, and live validation open.

## Remaining boundary

The inspection is structural evidence only. Helper expansion, lifecycle projection, typed weighted fixtures, package and rights admission, native decision-row rendering, scripted GUI fidelity, ordinary and joint firing, slot-23 human audition, save/load behavior, and user live validation remain open under the current `HOLD / PARTIAL` authority.

No gameplay, localisation, asset, GUI, spreadsheet, or registry file was changed by this receipt.
