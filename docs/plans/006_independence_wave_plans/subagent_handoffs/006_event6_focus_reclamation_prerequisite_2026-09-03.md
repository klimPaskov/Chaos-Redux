# Event 006 reclamation focus prerequisite repair — 2026-09-03

## Status

Applied one bounded source repair to the shared Event 006 focus tree. No new route, reward, icon, localisation, or AI weight was introduced.

## Change

`common/national_focus/006_independence_wave_focus.txt` now gives `independence_wave_adopt_reclamation_doctrine` the visible prerequisite connector `independence_wave_adopt_military_archetype_program`, matching its existing `available` completion gate and all sibling military choices.

## Evidence

The pre-change read-only focus audit identified the missing connector while confirming the completion gate, mutual exclusion, icon, localisation, reward, and AI block were already present. The post-change HOI4 MCP focus inspect returned `FOCUS_INSPECTED` with 184 focuses, 196 connectors, zero crossings, zero node intersections, and one expected long connector from the wide authored layout; layout hash remained `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bff645ef336838cfbcbd549b10361477c2bb3d833d180738c54af4c0bcf9a9db/b918382418fbe9383da3e252f8ae8bc6ce41ae43d71065529950ee41baf9df71/focus-inspect.6956e78df8f18fe2.json`.

The focused Event 006 allocator and SCN-008 scenario matrix audits still pass with 149 publishers, 126 automatic/high-chaos selectable packages, 40 runtime adapters, 32 attestations, 29 reservation groups, and the exact 3/4/5/7/10 ladder.

## Limits

The post-change inspect reports the pre-existing authored-layout long-connector warning for this 10-column route span and the unrelated vanilla `continuous_restrict_freedom_desc` localisation warning. Typed national-focus AI probability evaluation and same-scenario comparison remain unavailable because the custom probability-auditor route is not exposed in this runtime. No live HOI4 or save/load evidence is claimed.

No other files were intentionally changed by this tranche.
