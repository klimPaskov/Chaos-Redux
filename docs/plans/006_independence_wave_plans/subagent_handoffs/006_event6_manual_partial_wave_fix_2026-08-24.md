# Event 006 standalone partial-wave recovery

Date: 2026-08-24.

Status: **SOURCE-APPLIED / LIVE RECEIPT PENDING**.

## User-directed behavior

The manual `chaosx.nr6.1` invocation must be able to resolve the admitted candidates that were successfully frozen even when the unfinished package pool cannot fill the nominal automatic band. A non-empty, aligned standalone selection therefore commits a bounded wave at its actual selected count. The event still fails closed when no candidate is selected, metadata arrays are misaligned, execution fails, or a joint Event 005 + Event 006 plan is short.

This is a narrow runtime exception for the user's explicit manual-trigger request. It does not add a generic country, nearby anchor, substitute identity, broad regional admission, or pre-event surface. Joint plans retain exact-count fail-closed behavior.

## Source change

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt` now gates the selected-count rewrite on `global.liberation_plan_mode = constant:liberation_plan_mode.automatic`, `independence_wave_plan_pool_exhausted`, and `global.independence_wave_plan_selected_count > 0`. The branch sets the target and shared expected count to the frozen selected count, then requires the existing aligned-array witness before publishing contribution readiness.

The joint collision path uses `liberation_plan_mode = constant:liberation_plan_mode.cluster_joint`, so it remains on the exact-count failure branch. The zero-selected path still records `constant:liberation_plan_reject_reason.insufficient_pool` and does not publish contribution readiness.

## Evidence and limitations

- `python .tools/audit_event6_allocator.py` passes after the source change.
- A bounded `hoi4.event_inspect` lint for `chaosx.nr6.1` returned status `ok` with zero blocking diagnostics; the large-workspace helper graph remains partial by adapter policy.
- No live Hearts of Iron IV run was performed; the user owns live save verification and terminal receipt evidence.
- The whole Event 006 goal remains HOLD / PARTIAL because package admission, live terminal release, typed probability comparison, GUI acceptance, super-event slot 23 rights, and 13 supplied portraits still have open evidence or identity-safe consumer blockers.
