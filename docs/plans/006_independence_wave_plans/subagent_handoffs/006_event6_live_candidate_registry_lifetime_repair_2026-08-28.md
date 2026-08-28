# Event 006 live candidate registry lifetime repair

## Scope

This bounded repair addresses the user-reported result where manually triggering `chaosx.nr6.1` produced no countries even though admitted package rows existed. The local HOI4 data-structures reference states that temporary arrays are cleared when their defining effect or trigger block ends. The previous automatic-capacity repair populated `independence_wave_runtime_possible_countries` inside nested scripted effects, then asked later allocator effects to read it after that nested block returned. That made the live readiness wrappers vulnerable to an empty registry and an `insufficient_pool` terminal receipt.

## Changes

- `common/scripted_effects/006_independence_wave_package_planner_effects.txt`
  - `independence_wave_prepare_runtime_possible_country_registry` now clears and populates durable `global.independence_wave_plan_possible_countries` with `every_possible_country` before the generic capacity probe.
  - The existing contribution setup continues to rebuild the same durable registry before live package scoring and reservation.
  - Existing temporary-registry writes and cleanup remain harmless compatibility cleanup while no readiness wrapper depends on their lifetime.
- `common/scripted_triggers/006_independence_wave_triggers.txt`
  - All 32 `is_independence_wave_runtime_automatic_package_iw_*_ready` wrappers now evaluate their exact carrier through `global.independence_wave_plan_possible_countries`.
  - Absent carriers remain addressable through `every_possible_country`, and nested scripted-effect return no longer removes the scope registry used by live allocation.
- `common/scripted_effects/chaosx_logic_effects.txt`
  - The Event 006 pre-selection cleanup clears the durable global registry as well as the legacy temporary registry after the capacity probe.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`
  - Current authority text now describes the durable-registry repair and supersedes the earlier temporary-array wording.

## Behavior

Before this repair, a nested `independence_wave_begin_plan_contribution` could populate a temporary array that was no longer available when `independence_wave_select_one_automatic_package` called the 32 readiness wrappers. The allocator could therefore report an empty pool and never reach country instantiation. After this repair, the capacity probe and the live allocator use the same durable registry. The registry is cleared after pre-selection and during normal contribution cleanup, so stale candidate scopes do not survive a completed or failed transaction.

## Validation

- `python -B .tools/audit_event6_allocator.py --strict` passed with 149 publishers, 126 automatic/high-chaos selectable rows, 32 content-attested packages, 29 compatible groups, 40 adapters, 161 unattested rows, and the 3/4/5/7/10 ladder including World Collapse 10.
- `python -B .tools/audit_event6_country_api.py --strict` passed with zero missing or duplicate country API rows.
- `python -B .tools/audit_event6_flags.py --strict` passed with 102 complete flag families.
- `python -B .tools/audit_event6_form16.py --strict` passed for ARM, GEO, and AZR mutation and rollback paths.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 cells and 8 edge cases.
- Source assertions confirm 32 wrapper definitions and 32 durable-array references, the pre-selection durable seed and cleanup, and the unchanged committed-only public presentation gate.
- Fresh `hoi4_event_inspect` and `hoi4_event_render` retries for `chaosx.nr6.1` remain blocked by `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with zero returned artifacts. No engine, live-save, GUI, or probability completion claim is made.

## Remaining risks

The user must confirm the actual country instantiation in a live session because the installed MCP event routes cannot currently provide an engine artifact. Event 006 remains PARTIAL/HOLD at the existing admission boundary. Unattested package rows, weighted-probability evidence, GUI evidence, and full save-load validation remain outside this narrow repair.

## Simplifications

None were introduced. No package was admitted, no pre-event category or pressure surface was restored, and no fallback country or generic release path was added.
