# Event 006 joint partial-wave expected-count repair

## Disposition

Implemented a bounded source repair for the synchronized Event 005 plus Event 006 release path. The standalone Event 006 allocator and central admission boundary are unchanged.

## Source change

`common/scripted_effects/005_006_liberations_collision_effects.txt` now recomputes `global.liberation_plan_expected_country_count` after the Event 006 contribution is ready, using the actual `soviet_collapse_joint_plan_selected_count` plus the actual `independence_wave_plan_selected_count`.

This preserves the nominal count when the Event 006 pool reaches its target and makes the shared contract coherent when the source-complete Event 006 pool commits a smaller valid subset. The recalculation occurs before compact or optional territory expansion and before the shared plan lock.

## Why this was required

The joint wrapper initialized the shared expected count as Event 005 selected rows plus the nominal Event 006 wave target. The Event 006 allocator can intentionally lower its own target to the selected subset when its source-complete pool is exhausted, but the joint wrapper previously left the shared expected count at the nominal value. Shared lock validation compares the global plan-array length with that expected count, so a valid joint partial contribution could be rejected before release.

## Evidence

- `python .tools/audit_event6_allocator.py` passes with 149 publishers, 40 adapters, 32 attestations, 29 compatible groups, 161 unattested selectable rows, the 3/4/5/7/10 ladder, and Event 005 anchors before Event 006 anchors.
- File-scoped `hoi4.event_inspect` for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with zero selected blocking diagnostics at revision `a0d209ec728fe48cc44e3412c64b7c86ab0d1fea28713348d4dac1ba52035c67`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ced39f6929efea62aae96d66e0807145d031331444bdc1689cb6d70f4ef842c7/ab303b231501748bcadfa19319dae94a375f92266810a1f9d7489f687811d153/event-lint-a0d209ec728f.json`.
- Bounded `hoi4.event_render` state view for `chaosx.nr6.1` returned `EVENT_RENDERED_PARTIAL` at the same revision with zero selected blocking diagnostics. SVG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b5306ec5e0895177191519a28830d95388d4ed7abcaba07ec10aa2c308fcabe/8c53cd457d9c358f9c97f66b4c1af54fe8d1fa2e53597aac79f9cd7b30fa0c1b/event-state-a0d209ec728f.svg`.
- `hoi4.event_compare` was attempted against the prior cached revision and returned `EVENT_REVISION_NOT_CACHED`, so no before/after graph delta claim is made.

## Remaining boundary

This repair does not promote any package, change content attestation, alter deterministic Join order, or close the broader Event 006 HOLD/PARTIAL boundary. Current authority remains 149 publishers, 40 adapters, 32 attestations, 29 compatible groups, and 161 unattested selectable rows.
