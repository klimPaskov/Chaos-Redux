# Event 006 allocator runtime probe — no-change handoff

Date: 2026-08-30

Mode: read-only bounded source audit

Scope: the automatic selector and reservation path for `chaosx.nr6.1`, including the Event 006 planner, package-region registry, shared liberation-release reservation effects, relevant triggers, and standalone reset/phase handling.

## Disposition

No source-level false gate was proven, so no gameplay patch is recommended.

The reported zero-country result remains an engine/runtime observation that this source-only audit cannot attribute to one concrete predicate. No fallback, generic candidate, pre-event surface, pressure path, or runtime character recruitment was added.

## Source chain evidence

- `events/006_independence_wave.txt:11-14` defines the hidden, triggered-only root event, and `events/006_independence_wave.txt:47-52` dispatches a direct invocation to `independence_wave_prepare_and_execute_standalone_incident`.
- `common/scripted_effects/006_independence_wave_execution_effects.txt:930-981` clears a stale Event 006 standalone plan only when it is pre-execution and non-joint; `:989-1032` clears terminal state, seeds the standalone frame, begins an automatic Event 006 plan, enters allocation, and calls `independence_wave_allocate_automatic_packages` after the collecting-to-allocating phase check.
- `common/scripted_effects/006_independence_wave_effects.txt:3528-3555` gates the allocator on allocating phase plus the Event 006 inclusion flag, rebuilds contribution state, and loops selector attempts while selected count is below target and attempts remain; `:3556-3610` publishes success or the bounded failure result.
- `common/scripted_effects/006_independence_wave_effects.txt:3299-3352` predeclares selector/package/region/weight/reservation temporary outputs before nested region and package callbacks; `:3497-3525` prepares all fourteen region totals, draws from the regional random list, and marks the pool exhausted only when the aggregate weight is zero.
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt:65-78` builds `global.independence_wave_plan_possible_countries` with `every_possible_country`; `:80-104` repeats that durable registry before contribution reservation. The offline wiki and vanilla documentation define `every_possible_country` as including countries not currently present on the map.
- `common/scripted_triggers/006_independence_wave_triggers.txt:601-611` gives IW-006 an explicit runtime wrapper requiring AFX in the durable possible-country array, exact and ready tag availability, runtime preflight, and anchor state 34 availability. `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:44-50` applies the ordinary open-plan, slot, duplicate-package, and wrapper gates.
- `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:83-99` loads IW-006 through `every_possible_country` with `limit = { tag = AFX }`, then saves AFX, state 34, and its owner as event targets. The loader is present once and the p6 region callback includes its weight and reservation path.
- `common/scripted_effects/chaosx_liberation_release_effects.txt:122-176` initializes a fresh plan and sets `liberation_release_plan_includes_event6`; `:186-196` enters allocation. The shared country reservation gate at `:458-520` requires an open plan, allowed owner, all three candidate event targets, a dormant target country, an unreserved package/group, an anchor owned by the primary host, and a host marker matching the current plan before appending synchronized arrays and marking the target reserved.
- For the p6 witness, vanilla state 34 is Wallonie owned by BEL and vanilla BEL capital is state 6. IW-006's AFX shell has no starting states, so the dormant-country and absent/zero-state identity branches are admissible in source. The p6 force constants provide profile 2, military tradition 61, a five-bit reinforcement mask, zero inheritance, zero research, and earliest chaos band 0; these do not create a static zero-weight condition in the planner's normal calm band.

## Evidence and limitations

The required first weighted pass used `hoi4_probability_inspect` before evaluation. The random-list adapter found fourteen regional lists, but the computed weights remain unresolved because they are produced by effect-derived temporary values; the custom-pool adapter has no manifest and returned zero candidates. The required `chaosx_ai_probability_auditor` route is not callable in this runtime, so no typed auditor evidence exists.

The required event MCP inspections were attempted, but the workspace-scale trace/render/state passes are partial: helper projection and lifecycle execution remain unresolved, and the tools do not execute a live 1936 save. These artifacts therefore cannot prove a reservation rejection or release failure. No source-level conclusion should be upgraded to engine proof.

The remaining engine-sensitive points are the behavior of an event target saved from an absent `every_possible_country` scope, propagation of predeclared temporary values through nested scripted effects and dynamic `meta_effect` interpolation, and the live values of the shared rejection/receipt ledger. The offline wiki and vanilla examples support the source patterns, but only the game runtime can distinguish a valid zero-weight pool from a failed absent-scope or nested-value operation.

## Recommendation

Do not weaken the selector gates or add a fallback. Preserve the current source and obtain one live receipt/diagnostic snapshot exposing `global.liberation_plan_phase`, `global.liberation_plan_expected_country_count`, `global.liberation_plan_selected_country_count`, `independence_wave_plan_pool_exhausted`, the selected/rejection arrays, and the p6 wrapper/weight outputs. A patch is justified only after that evidence identifies a specific failing condition.

No gameplay files were changed and no commit is required for this no-change audit.
