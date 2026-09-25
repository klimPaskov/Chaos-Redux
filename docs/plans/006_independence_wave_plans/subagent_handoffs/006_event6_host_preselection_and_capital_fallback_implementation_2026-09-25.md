# Event 006 host preselection and capital fallback handoff

Disposition: **superseded** by `006_event6_complete_host_preselection_and_capital_safety_2026-09-25.md`.
This earlier patch covered primary-host preselection but omitted optional-state owners, so it does not describe the final bounded census or final capital-seat rules.
Its implementation findings are retained as historical review evidence; use the superseding handoff for current behavior and validation limits.
The user's explicit approval of Event 006 Part 1 and Part 2 is the design basis for this bounded patch.
This handoff records source behavior and limits, not engine execution or complete Event 006 readiness.
The release planner diagram still depicts host protection during each candidate attempt; it calls itself a design guide, and Part 1's explicit preselection covenant governs this patch.

## Files changed

- `common/scripted_effects/006_independence_wave_package_planner_effects.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_effects/chaosx_liberation_release_effects.txt`
- `common/scripted_triggers/006_independence_wave_package_triggers.txt`
- `common/scripted_triggers/chaosx_liberation_release_triggers.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_host_preselection_and_capital_fallback_implementation_2026-09-25.md`

## Source change and helper map

| Helper or predicate | Scope, inputs, outputs, and side effects | Call sites |
| --- | --- | --- |
| `independence_wave_preselect_automatic_hosts` | Country scope in the existing automatic allocation transaction. It reads the frozen chaos band, open plan, possible-country registry, and package readiness, uses the existing weight preparation to collect distinct primary hosts with positive eligible package weights, reserves a shared protected state for each unreserved host, and sets `independence_wave_hosts_preselected`. It changes no ownership or capital. | `independence_wave_allocate_automatic_packages`, before its first candidate draw, in both standalone and Event 005 joint transactions. |
| `independence_wave_calculate_candidate_allocation_weight` | The existing weight is unchanged. Only while `independence_wave_host_preselection_collecting` is set, a positive-weight ready package adds its primary host to `global.independence_wave_preselection_hosts`. The list is deduplicated and cleared after reservation. | Existing fourteen region weight preparers. |
| `is_independence_wave_candidate_anchor_available` | State trigger. Once preselection is frozen, the owner must have a current shared host reservation. The existing owner/control, origin, reserved-state, and protected-state gates still apply. An unprotectable host therefore contributes no candidate through the common readiness path. | Existing automatic package readiness triggers and other Event 006 anchor checks during the transaction. |
| `liberation_release_select_and_reserve_host_state` | Country effect. A previously reserved host now reuses its current protected state after checking ownership and the candidate-anchor exclusion. The preselection pass may protect the capital even when the last loaded candidate anchor names that state. Existing Event 005 shared rows remain intact. | Event 006 candidate and optional-state reservations, Event 005 shared reservations, and the new preselection pass. |
| `liberation_release_cleanup_unused_host_reservations` | Shared plan effect. It preserves all preselected rows while automatic candidates reroll and optional territory is trimmed. Event 006 clears the freeze and removes rows with no selected primary host or planned loss after optional expansion, before plan lock. | Existing candidate rollback and trim calls, plus the end of Event 006 optional expansion. |

The preselection list and its collecting, reserving, and frozen flags clear at contribution start, contribution cleanup, and shared plan scope cleanup.
The shared protected-state, original-capital, snapshot, plan-ID, and state-reservation arrays retain their prior alignment and rollback ownership.
The Event 005 joint coordinator still reserves Event 005 first, runs Event 006 preselection and exact-count selection second, completes optional passes, then locks the combined plan.

## Tuning, event targets, and migration

No constant or numeric tuning value changed.
The exact automatic count ladder remains 3/4/5/7/10, including World Collapse 10, and pool exhaustion still cancels the incomplete plan before ownership mutation.
No new event target is persisted. The existing `liberation_candidate_anchor`, `liberation_candidate_primary_host`, `liberation_candidate_host`, and `liberation_candidate_protected_state` remain short-lived transaction targets.
The new preselection list is a short-lived global plan array, and its cleanup is explicit.
The patch inserts one pass before the existing weighted selection instead of replacing the region publishers, package readiness or rights gates, exact state ledgers, or release execution.
No shared dynamic helper was introduced, so `chaosx_dynamic_effects.md` was not changed.

## Unresolved accepted requirements and design detail

The primary-host preselection pass covers hosts published by ready automatic anchor packages in the current chaos band.
An optional compact or extended state can belong to a host with no ready anchor package. That host is still protected by the existing optional-state reservation path after mandatory anchors are frozen, so the literal accepted requirement that **every possible host** be reserved before any candidate selection remains incomplete for optional-only hosts.
Closing that gap requires a reviewed package metadata path for the owners of all optional states without scanning the whole world or broadening the permitted region registry edits.

The accepted preference for the **safest owned core with a valid capital location** has no sufficiently precise engine-backed selection predicate or accepted scoring rule in the inspected offline wiki, vanilla effect/trigger documentation, or current source.
The existing fallback ordering remains controlled core, controlled owned state, uncontrolled core, then any owned state, with the first eligible state selected by the current array iteration.
This patch does not claim that iteration is a proven deterministic tie-break or that each such state is a valid `set_capital` target.
The existing pre-execution capital relocation only runs when the old capital is in the frozen release rows. An owned but uncontrolled capital or an emergency non-core remnant outside those rows still needs a specific relocation rule and source validation.
No victory-point, supply, port, or new safety weight was invented.
The added bounded readiness pass repeats the existing package-weight preparation once per incident. Its runtime cost and nested temporary-variable propagation have not been observed in the engine.

## Validation and MCP evidence

Source review traced standalone and joint call order, host-row reuse, candidate reroll cleanup, optional trimming, pre-lock host validation, and pre-mutation failure cleanup.
The bounded diff contains no changed package attestation, rights gate, count constant, region weight, ownership transfer, rollback snapshot, or periodic hook.
`git diff --check` passed for the five touched gameplay files.
No tests or HOI4 process were run, as requested. Engine execution, exact release counts, state validity for capital relocation, rollback, and save/load behavior remain unwitnessed.

Before the edit, `hoi4.probability_inspect` returned `PROBABILITY_SOURCE_INSPECTED` for the fourteen outer region entries with source revision `1f4259026a0aba06cfa9a32e9d84415c2500509a6290ab545e33034a036d3732` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3202fa7bf8df3e86a62f11b1a821dd47b0ff9934e3161ef3936660e027dbc7c0/c817e0d047cdd7d74efd43b61ebb0d9488c1cf60737d03ddb36217fe23788f3a/probability-inspect-a667469d0567.json`.
The named scenario from the prior auditor receipt remains unresolved because campaign weight inputs were unspecified; it does not establish release odds or sequence behavior.

Before the edit, `hoi4.event_inspect` on `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL`, revision `1a03026de1cf615664728b4f3e312d0520ddf15b08c3d23bdd86a569ab2cae43`, zero blocking diagnostics, deferred workspace helper and lifecycle projections, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0492ae01acec97a5130756ee01c6e2e012045dad3c45535494b0c6ee1a454c4c/8ddd629a517dbc556b6e61f712c4f2c99bbba1aa19b1074f0bf31da67f734148/event-trace-1a03026de1cf.json`.
It is bounded chain evidence, not allocator execution evidence.

Before the edit, `hoi4.map_inspect` returned `MAP_INSPECTED` at revision `54b42f4fb047eb2a60e3664400d9c07a2b3fee07d117d12de00018555b822bc6` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/05161817a6e9cc32bf31a5e23d6dbf4856d6d04b27e9dbd7a995ca89cde747d3/e13227640cb2367c5c8c697499cdc3f7929b6c56a397d2f13a4ec24574b20518/map-inspect.54b42f4fb047eb2a.json`.
The query returned no matched capital records, inspected no specific state IDs, and reported map locator/port errors with diagnostic truncation, so it supplies no proof of a valid fallback capital location.

The read-only `chaosx_ai_probability_auditor` inspected the post-patch outer pool with all fourteen region entries, `poolComplete=true`, source revision `266de92e01c1cd2e0d15f0e78aac0f68b719f1336c6b8cd56ed3fdf430e03709`, source hash `800416aa4370f500c2799e3cf8abb3cb310da3127c80e4ad01bad8e8f533c4b9`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9291eb03d552da20b320e18b6b22e55c76d6c8cd5ec767cd8a45afa2ac/576ba2ee82cb1add064ecc527f5210d737d404ea46a6c427c73d6f31234b2a22/probability-inspect-800416aa4370.json`.
My later refreshed outer inspect returned the same source hash, revision `cd2a38256c7d08bda17a132a87e99bcbbedb29147893595357a53da2e1f78ee7`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3c738bde48be8d19e5f8b3546f3a2e9eabdc4175c0bd2fd4c00a90a0a75f618e/1308132114a1bb3150f7604202197c18da0c33d7f152856e7de68a8af73bddae/probability-inspect-800416aa4370.json`.
The auditor inspected 126 nested package entries across regional pools at revision `e5a810d3e01d18151a861828a61ae6439af924361532094918ff143a6bff1ffd`, but the adapter reported `poolComplete=false`, `requiredInputs=126`, and `unresolved=1`, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/026819a0dda1372111be101b26e1dce8cbf4dcf8ad88ea401852f8655284ec5d/ef4f826bcd20207e7d6f49f51b305e64f86adbeb40449d234d60a0c685ac3672/probability-inspect-17e35c209602.json`.
An identifier probe for the region selector returned `identifier_not_found`, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6f0699ef1424244cd5bdb5a19240e1db1cc4031004dee77fc84d53031ec0da3/04b3108cfed72f95fc5957cf153e6be0dadd8a8a7bb3d05facc8953e348a4f41/probability-inspect-17e35c209602.json`.
The mandatory `hoi4.probability_compare` attempt did not reach scenario evaluation because its historical `before` reference was rejected with `Unrecognized keys: "sourceRevision", "sourceHash" at before` and then `Unrecognized key: "revision" at before`; no comparison artifact exists.
The prior named scenario had fourteen unresolved dynamic region weights, so no before/after probability, ranking, or sequence conclusion is supported.

The parent owns post-patch event and map MCP review, complete map fixtures, final integration, and the path-limited commit.
