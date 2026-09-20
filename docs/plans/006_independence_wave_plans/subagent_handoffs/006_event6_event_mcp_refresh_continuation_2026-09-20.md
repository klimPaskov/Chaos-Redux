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

## Remaining boundary

The inspection is structural evidence only. Helper expansion, lifecycle projection, typed weighted fixtures, package and rights admission, native decision-row rendering, scripted GUI fidelity, ordinary and joint firing, slot-23 human audition, save/load behavior, and user live validation remain open under the current `HOLD / PARTIAL` authority.

No gameplay, localisation, asset, GUI, spreadsheet, or registry file was changed by this receipt.
