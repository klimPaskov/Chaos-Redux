# Event 006 player-surface origin gate

Date: 2026-09-03

Scope: bounded repair of the Event 006 country-local player-surface predicates after the no-pre-event decision was reaffirmed.

Disposition: `implemented source repair` / no package, cost, allocator, or Event 021 admission change.

## Source change

`common/scripted_triggers/006_independence_wave_triggers.txt:29-36` now defines `is_independence_wave_event6_local_content_active` as `exists = yes` plus `is_independence_wave_active_country = yes`. The helper no longer treats a completed Event 021 origin-neutral package as Event 006 local content.

`common/scripted_triggers/006_independence_wave_triggers.txt:56-67` now keeps `is_independence_wave_event6_player_surface_allowed` behind the same active-origin predicate and the existing four adapter-receipt exclusions. Its Event 021 branch was removed, so completed or stale Event 021 receipts cannot expose an Event 006 category, decision, mission, cost, queue, or history surface.

The separate `is_independence_wave_package_content_active` predicate remains unchanged as the bounded internal setup bridge for Event 021 adapters. It is not used as the player-facing category/local-content gate.

## Contract alignment

This matches the accepted no-pre-event rule in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_2_event_flow_and_evolutions.md:35-41` and `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md:9-15`: before the public `chaosx.nr6.1` report creates an active Event 006 origin, the player sees no category, mission, pressure value, cost, queue, history indication, or early wave request.

The strict active-origin classifier remains `is_independence_wave_active_country` at `common/scripted_triggers/006_independence_wave_triggers.txt:9-14`. Event 021 origin-neutral receipts remain explicitly non-active at `:18-27` and are still available only to the internal package-content bridge.

## Validation

- `python -B .tools/audit_event6_allocator.py --strict` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 40 adapters, 32 content attestations, 29 compatible groups, the exact `3 / 4 / 5 / 7 / 10` ladder, and no pre-event category, mission, cost, or queue.
- `python -B .tools/audit_event6_flags.py --strict` passed with 102 registered tags and 102 complete flag families.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 mode/intensity cells and eight edge cases.
- `python -B .tools/audit_event6_form16.py` passed the ARM/GEO/AZR consent, mutation, rollback, cleanup, and readiness contract.
- The bounded decision-surface audit confirms all 88 Event 006 categories remain gated by either a direct active-origin predicate or this strict shared helper.

The post-change read-only Event MCP lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics at revision `3278b34c53341a910d3959107765bb43be6cba2fb27f8562b8b0557d20fefc2f`. The linked lint artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1319948f149cd1bc07274446fe65b8fc4a62ebd6b1623dbed487be825ebbe4b1/0cb6b671441d328bbaab9e74007937705f740961f85784f0b94169e266fb79e8/event-lint-3278b34c5334.json`. The partial status reflects deferred workspace-wide helper/lifecycle projection only; it is not a selected Event 006 blocker.

No central adapter, attestation, Join order, automatic weight, package roster, Event 021 internal setup, localisation, asset, or fallback was changed.

Live engine, save/load, and player-session behavior remain user-owned verification surfaces; this handoff makes no such claim.
