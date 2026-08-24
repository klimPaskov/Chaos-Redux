# Event 006 manual no-country execution diagnostic

Date: 2026-08-24.

Status: read-only source diagnostic; no gameplay files were edited.

Scope: manual `event chaosx.nr6.1` entry, standalone allocator, frozen-country execution, release/state ownership, and the public report gate.

## Verdict

The current source proves a fail-closed path in which the manual event returns without creating any country when no candidate reaches the allocator, and it deliberately produces no visible report for that path. This is the strongest source-level explanation for a manual event that appears to complete without countries.

The source does not prove that `release` or `set_state_owner_to` fails for an admitted non-empty plan. A second path can release and then roll back after an ownership or finalization failure, leaving no countries, but selecting that path requires live terminal-receipt values or engine evidence that was unavailable here. No narrow gameplay patch is justified by static evidence alone.

## Proven empty-pool path

1. `events/006_independence_wave.txt:44-60` clears the stale joint marker, calls `independence_wave_prepare_and_execute_standalone_incident`, and opens `chaosx.nr6.2` only when `independence_wave_standalone_incident_committed` is set. There is no failure or cancellation report branch.
2. `common/scripted_effects/006_independence_wave_package_allocator_effects.txt:48-78` recomputes all regional weights. If every package readiness/host/anchor gate is false, the total weight is zero and only `liberation_release_plan_pool_exhausted` is set.
3. `common/scripted_effects/006_independence_wave_package_allocator_effects.txt:92-156` leaves `global.independence_wave_plan_selected_count` at zero, does not set `independence_wave_plan_contribution_ready`, and records `insufficient_pool` in the non-exact branch. The non-empty partial-wave target rewrite at lines 125-152 is therefore not entered.
4. `common/scripted_effects/006_independence_wave_execution_effects.txt:923-941` skips optional expansion and frozen execution because the contribution-ready flag is absent.
5. `common/scripted_effects/006_independence_wave_execution_effects.txt:967-981` restores host capitals, clears the contribution, aborts the plan, and sets `independence_wave_standalone_incident_cancelled_before_mutation`. No ownership-changing effect is reached.

This path explains “the event completed” as a hidden, pre-mutation cancellation rather than a country-creation attempt. The accepted Event 006 specification explicitly allows a shortfall only as a blocked wave slot (`docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md:25-40`), so broadening admission or adding a fallback would change the accepted design.

## Release and transfer path reviewed

For a non-empty aligned plan, `common/scripted_effects/006_independence_wave_execution_effects.txt:348-451` masks unplanned cores, adds the frozen Event 006 states as cores, calls `release = event_target:independence_wave_execution_country` from the former-host country only when the target is absent, and restores masked cores. Dormant custom shells intentionally skip `release` and rely on the later state transfer.

`common/scripted_effects/006_independence_wave_execution_effects.txt:474-506` then applies `set_state_owner_to` and `set_state_controller_to` to every frozen Event 006 state and increments the transfer count only when both ownership and control match. `:512-539` reapplies the anchor capital after transfer.

The vanilla effects documentation confirms that `release` is a COUNTRY-scope effect that releases a specified country as a puppet using the caller's owned states, while `set_state_owner_to` and `set_state_controller_to` are STATE-scope effects. The offline wiki confirms that registered country tags exist even when absent from the map and that mid-game countries can be materialized through country-scope core effects plus state transfer. The source's absent-target sequence is therefore plausible, but the documentation does not prove the behavior of an `event_target:` pointing at an absent country in this exact chain.

The offline scope documentation also marks `event_target:<name>` as subject to an invalid-event-target failure. Because this chain stores absent or dormant target tags in `global.liberation_plan_countries`, then later resolves them as event targets at `:466-469`, `:488-491`, and `:546-548`, this remains an engine-level uncertainty rather than a proven source bug.

## Rollback path that also leaves no countries

If a non-empty plan reaches execution, `common/scripted_effects/006_independence_wave_execution_effects.txt:739-767` requires selected-count equality, successful instantiation, complete state transfer, and frozen-ownership validation before finalization. If any of those checks fail, `:804-829` marks execution failure. The wrapper at `:947-965` marks failure after mutation and invokes the shared compensating rollback; a completed rollback removes the transient countries and restores ownership. A finalization failure at `:949-954` similarly yields no public Event 006 report.

The durable receipt added at `common/scripted_effects/006_independence_wave_execution_effects.txt:15-190` distinguishes these cases without changing gameplay. After the manual call, the meaningful fields are `global.independence_wave_terminal_receipt_selected_count`, `...target_count`, `...instantiated_count`, `...transferred_state_count`, `...last_failure`, and the flags `...cancelled_before_mutation`, `...failed_after_mutation`, `...failed_during_finalization`, and `...rolled_back_after_mutation`. A zero selected count identifies the empty-pool path; a non-zero selected count with rollback flags identifies a release/transfer/finalization failure.

## Static evidence and validation

- `python -B .tools/audit_event6_allocator.py` passed. It reports 149 publishers, 126 automatic/high-chaos selectable packages, 40 runtime adapters, 32 content-attested packages, 29 compatible reservation groups, and a 20-package static standalone witness with protected host states.
- The witness is source/static only. It does not simulate the current live map, event-target materialization, `release`, state ownership, or package setup.
- The existing non-empty partial-wave allocator fix is present at `common/scripted_effects/006_independence_wave_package_allocator_effects.txt:125-152` and is documented by `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_manual_partial_wave_fix_2026-08-24.md`. No duplicate allocator change was made.
- No target gameplay file was modified. This handoff is the only file added by this diagnostic.

## MCP blockers and unsupported analysis

- The required read-only `hoi4.event_inspect` route is available, but corrected `state_flow`, `scan`, and file `lint` calls for `chaosx.nr6.1` each timed out after 180 seconds. No event artifact or engine state-flow evidence was returned.
- The required initial `hoi4.probability_inspect` call for the custom weighted allocator accepted the source-path shape but timed out after 180 seconds. No probability artifact was returned.
- No callable `chaosx_ai_probability_auditor` route was exposed in this runtime, so no auditor evidence pass or probability comparison can be claimed.
- HOI4 was not launched, in accordance with repository instructions. Consequently, the exact live cause cannot be narrowed beyond the two source-proven terminal classes above.

## Parent handoff

Do not broaden package admission or add a generic country-creation fallback based on this diagnostic. First classify the manual run with the durable terminal receipt fields. If selected count is zero, investigate the live readiness/host/anchor gates and preserve fail-closed behavior. If selected count is non-zero and rollback occurred, the next bounded investigation should target absent/dormant event-target materialization and the `release`/state-transfer ownership assertions, with fresh MCP or user-owned live evidence before changing execution.
