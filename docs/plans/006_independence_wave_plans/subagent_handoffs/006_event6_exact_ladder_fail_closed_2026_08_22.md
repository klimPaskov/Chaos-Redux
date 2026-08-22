# Event 006 exact automatic ladder fail-closed repair — 2026-08-22

## Scope

The automatic allocator now preserves the nominal 3/4/5/7/10 target, including World Collapse's target of 10, when the readiness-controlled package pool is exhausted before the target is reached.

## Files changed

- `common/scripted_effects/006_independence_wave_package_allocator_effects.txt`
  - Removed the pool-exhausted positive-subset branch that rewrote `global.independence_wave_plan_target_count` and `global.liberation_plan_expected_country_count` to `global.independence_wave_plan_selected_count`.
  - Pool exhaustion before exact selection now follows the existing fail-closed branch, setting `independence_wave_plan_exact_count_failed` and `liberation_plan_reject_reason.insufficient_pool` without setting contribution readiness.
- `common/scripted_effects/005_006_liberations_collision_effects.txt`
  - Removed the coupled joint partial-wave reconciliation that replaced the nominal shared expected count with the two planners' selected counts.
  - Event 005 still reserves first, Event 006 still rerolls against the frozen footprint, and compact-territory expansion still runs only after both exact contributions are ready.

## Behavior contract

An undersized automatic pool cannot become a smaller public wave. The nominal target and shared expected count remain authoritative, so no contribution readiness, optional expansion, plan lock, ownership mutation, report, evolution, achievement, or super-event hook can proceed from a short pool. Exact target selection and metadata alignment retain their existing success path; attempt-cap exhaustion remains fail-closed.

## Evidence

- The read-only completion audit `006_event6_completion_gap_audit_2026-08-22.md` identified the target rewrite as the highest-value accepted-design defect and supplied the exact two-file owner patch.
- Fresh static validation passes after this source change: the allocator audit reports the exact `3 / 4 / 5 / 7 / 10` ladder, World Collapse `10`, 32 attestations, 29 compatible groups, and the retired pre-event crisis surface; the country API, strict flag-family, SCN-008 matrix, and FORM-16 audits also pass.
- The current source-level invariant is that no `set_variable` assigns either target or expected count from `selected_count` in the removed branch; the only joint expected-count assignment is the initial Event 005 plus nominal Event 006 setup before selection validation.
- Fresh `hoi4.event_inspect` lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL`, status `ok`, zero blocking diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/66722145672f058de718c8a3d267bdfb78f17270a903d73b832bef1806c110ed/263c99bfae490e3b0728cbf12f6edac988c5783780cffce4a5fdc7269a76615a/event-lint-2be037dcc948.json`; workspace-wide helper projections remain deferred.

## Remaining evidence limits

The Event MCP namespace/single-file deep inspections and render path remain timeout or artifact-storage limited in the cited audit, and no live terminal receipt was supplied. The whole Event 006 objective remains HOLD/PARTIAL because package admission, typed probability, formable consumers, GUI/runtime, portrait finals, and super-event 23 rights/audio remain incomplete.
