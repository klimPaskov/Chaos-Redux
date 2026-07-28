# SCN-008 scripted-system audit handoff (2026-07-28)

## Scope

This audit covers the SCN-008 allocation and setup path in `common/scripted_effects/006_independence_wave_scenario_effects.txt`, `common/scripted_triggers/006_independence_wave_scenario_triggers.txt`, `common/script_constants/006_independence_wave_scenario_constants.txt`, `events/006_independence_wave_scenario.txt`, the shared liberation-release coordinator, and the Event 006 scenario ledger decisions.

No runtime, live-save, or in-game completion claim is made here.

## Findings

- The ranked registry block contains 138 unique package IDs, and all 138 ranked IDs have both load and reserve dispatch publishers.
- `independence_wave_scenario_attempt_ranked_packages` traverses the complete ranked array once and contains no intensity-dependent candidate limit; a ready row enters the reservation adapter and an unready row records `package_unready`.
- The allocator seeds the shared target count from `bound_package_count` (138), attempts and optionally expands every ranked row, then deliberately replaces the execution target with `selected_count` and sets `liberation_plan_expected_country_count` to the same value before the contribution-ready check. The execution validator requires `selected_count == target_count`, so this is a post-allocation execution target, not a stale override.
- Intensity tuning selects territory and force levels and also applies the resource and route-access mechanics named by the SCN-008 specification. High and Maximum add the corresponding ambition and high-chaos route flags, consistent with the specification's explicit territory, forces, resources, and route access wording.
- Type application is independent of the allocation loop. `apply_type` routes Common Congress, Wars of Separation, Universal Belligerence, and Patron Worlds; per-country marking covers Sovereign Scatter and Great Partition. Universal Belligerence has three explicit rule branches: former hosts, neighboring releases, and nearby nonleague states.
- The selector wraps in eight player-facing modes: six numeric families plus Universal Belligerence's three rules. `type_next` and `type_previous` enter and leave the Universal rule ladder without dropping a mode, and the shared GUI binds both arrows to these effects.
- Lock-before-release is enforced by the shared coordinator. `liberation_release_lock_plan` validates the complete ledger before entering `locked`; execution revalidates metadata, hosts, anchors, package adapters, force mappings, and recovery snapshots before `begin_execution`. Missing host, anchor, reservation, or aligned metadata fails closed and records a rejection or abort state.
- Host protection and anchor reservations are selected through `liberation_release_select_and_reserve_host_state`, `liberation_release_reserve_host_state`, `independence_wave_reserve_candidate_anchor`, and `independence_wave_finish_package_reservation`. Failed reservations roll back candidate state and unused host reservations before the row is rejected.
- Belligerence marks are cleared at the start and end of Universal Belligerence and on failed target declarations. The first former-host war target is cleared before and after type application. Shared plan abort and compensating rollback paths clear scope marks, pending package metadata, host capitals, and Event 006 reversible package state.
- The source had one cleanup gap: `independence_wave_scenario_reset_summary` reset ledger arrays but left `independence_wave_scenario_ledger_visible`, `independence_wave_scenario_ledger_index`, and `independence_wave_scenario_ledger_display_index` live. A relaunch while the previous ledger was open could expose that old decision surface against newly reset arrays. The reset helper now clears the flag and both indices before rebuilding the summary.
- Publication is not duplicated in the SCN-008 path. A successful scenario schedules one `chaosx.nr6.2` public report and one delayed `chaosx.triggerable_scenarios.80` result/ledger event. The separate `chaosx.nr6.1` entry belongs to the normal Event 006 presentation path and is blocked by the shared joint-presentation barrier during a scenario launch.

## Existing helper map

| Helper | Scope and inputs | Outputs and side effects | SCN-008 call site |
| --- | --- | --- | --- |
| `independence_wave_scenario_attempt_ranked_packages` | Global ranked package array, dispatch package ID, candidate-country event target | Records attempts/rejections and invokes the package reservation publisher | `independence_wave_allocate_scenario_packages` |
| `independence_wave_begin_package_reservation`, `independence_wave_reserve_candidate_anchor`, `independence_wave_finish_package_reservation` | Candidate country, anchor, primary host, package metadata, reservation phase | Locks host/anchor rows, appends aligned ledger arrays, or rolls back and records a rejection | Region package reserve publishers |
| `liberation_release_lock_plan`, `independence_wave_validate_execution_metadata`, `liberation_release_commit_plan` | Global plan arrays and shared phase flags | Validate, lock, execute, finalize, and commit one frozen transaction | `independence_wave_execute_standalone_frozen_plan` |
| `independence_wave_scenario_apply_intensity_values` | Current release country and frozen intensity | Applies configured value deltas and intensity route flags | `independence_wave_scenario_mark_current_release` |
| `independence_wave_scenario_apply_type` | Frozen type and Universal rule | Starts league, host wars, belligerence, patron channels, and type-specific flags | Post-commit scenario application |
| `independence_wave_scenario_reset_summary` | Country scope plus global summary arrays | Clears old summary rows, marks, counters, and stale ledger view state | Scenario launch and stale-plan result path |

No new scripted effect or trigger was needed. Existing helper contracts are documented in their source overviews and the shared liberation-release documentation.

## Constants and tuning table

No constants changed. The source uses `independence_wave_scenario_registry.bound_package_count = 138`, `disabled_unbound_package_count = 55`, the six type values, three belligerence-rule values, four intensity values, and the existing patron/belligerence distance thresholds. The source/docs count discrepancy remains unresolved elsewhere: current source is 138 bound plus 55 disabled rows, while some Event 006 documentation still describes 149 plus 57; this audit does not change registry authority.

## Event-target and cleanup plan

- Regular candidate and host event targets are used only inside reservation and execution chains and are validated with `has_event_target` before dereference.
- Global `independence_wave_first_former_host_war_actor` is cleared before and after type application.
- `independence_wave_scenario_belligerence_targets` and each `independence_wave_scenario_belligerence_targeted` flag are cleared before selection, after successful or failed declarations, and at the end of Universal Belligerence.
- `independence_wave_clear_plan_contribution` clears pending package metadata and Event 006 planner arrays before a shared abort clears coordinator arrays.
- Shared reset, commit, abort, and compensating rollback clear coordinator scope marks and restore protected host state where execution has not crossed the finalizer boundary.
- The new reset cleanup clears the player-facing ledger flag and cursor variables before summary arrays are emptied.

## Migration and call-site impact

The only gameplay source change is the local cleanup addition in `independence_wave_scenario_reset_summary`. No call sites, package publishers, constants, decisions, localisation, or GUI source were changed.

## Validation

- `python .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, anchor/optional/lock ordering, and shared joint ordering.
- A targeted source count confirmed 138 ranked IDs, 138 unique IDs, zero ranked IDs missing load dispatch, and zero ranked IDs missing reserve dispatch.
- The read-only event inspector returned `EVENT_INSPECTED_PARTIAL` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c793fac675323e7733decd512be6600b84f4b0da4c4b918c8bfb01fb8e7067e/bc2bacf7fb072b44e659c8b0f5586cc25277312977c8fbf02cdccf9c1c0e28ec/event-scan-107e3a01cd2d.json`. The linked report is bounded and source-graph wide, so it is structural evidence only.
- The read-only event state render returned `EVENT_RENDERED_PARTIAL` with manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4d384bb24e08a50d303b0316f40127d919ec7a5066357b0ff30fe9bcc7f97b7/b41a68291356de0f42393308d717a2555681b971db894dfca9218f2fb3d58f3b/event-state-d605663e935f-manifest.json`. The render was bounded to 240 selected nodes.
- The read-only GUI inspector targeted `chaosx_scenarios_window` with scenario `SCN-008` and returned `GUI_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6996778fd6367c951121f1a2f5fac8812ebade4e5348d8df330841d2a3140a17/638df5ad46ad11492a7b2ce475c55c7871cb9c89565ee79a7111b0ef5010522e/gui-inspect.f1307cb07871be3c.json`. It reported no visible overlap for the inspected window, while retaining repository-wide GUI diagnostics outside this audit.

## Skipped meaningful validation and limitations

- No Hearts of Iron IV process was launched, and no save-game or live runtime matrix was run.
- The 32-cell SCN-008 acceptance matrix, actual map ownership and capital relocation outcomes, host-war declaration outcomes, patron reach, and rollback recovery remain parent-owned runtime checks.
- The MCP event and GUI reports intentionally include bounded or repository-wide diagnostics and must not be read as a complete gameplay or GUI completion claim.

## Files changed

- `common/scripted_effects/006_independence_wave_scenario_effects.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_scn008_scripted_system_audit_2026_07_28.md`

