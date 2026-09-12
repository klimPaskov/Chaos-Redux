# Event 006 IW-045 BSK lifecycle repair — 2026-09-12

## Disposition

Implemented a bounded lifecycle repair for admitted IW-045 Bashkiria (`BSK`).

The activation-backed founding mission `independence_wave_bsk_hold_frontier_congress` is now the sole opening action until its compact-resolution receipt exists, and the active-project helper reserves that mission while it is running.

No MEL, admission, cost, AI-weight, GUI, asset, localisation, or unrelated source surface was changed.

## Evidence

The founding mission in `common/decisions/006_independence_wave_bashkiria_mari_decisions.txt:9-58` uses daily `activation`, `available = { always = no }`, `days_mission_timeout`, success cancellation through `independence_wave_bsk_compact_crisis_resolved`, and timeout or invalidation through `independence_wave_bsk_compact_crisis_failed`.

The offline Decision Modding page explains that `activation` controls when a mission appears, `days_mission_timeout` makes the decision a mission, and `available` controls mission completion behavior.

The offline Triggers page and vanilla `triggers_documentation.md` define `has_active_mission` as the country-scoped active-mission check, while vanilla `effects_documentation.md` defines mission activation and removal behavior.

Vanilla precedent exists in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\AST.txt:2484`, where a project branch checks `has_active_mission` before proceeding.

The accepted KUB/RUT/TAT lifecycle repair in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_kub_rut_tat_lifecycle_gate_repair_2026-09-08.md` applies the same two-part contract: require the compact-resolution receipt in `project_ready` and include the founding mission in the active-project helper.

## Changed files and identifiers

- `common/scripted_triggers/006_independence_wave_bashkiria_mari_package_triggers.txt:18-30`
  - `is_independence_wave_bsk_project_ready` now requires `has_country_flag = independence_wave_bsk_compact_crisis_resolved`.
  - The existing setup, generation, and failure guards remain unchanged.
- `common/scripted_triggers/006_independence_wave_bashkiria_mari_package_triggers.txt:124-137`
  - `has_independence_wave_bsk_active_package_project` now includes `has_active_mission = independence_wave_bsk_hold_frontier_congress`.
- `common/decisions/006_independence_wave_bashkiria_mari_decisions.txt` was inspected but not edited.

## Before and after behavior

Before the repair, an active founding mission did not appear in the BSK active-project helper, and ordinary paid projects could pass their shared readiness gate before `independence_wave_bsk_compact_crisis_resolved` was set.

After the repair, all ordinary BSK project visibility and availability calls that use `is_independence_wave_bsk_project_ready` remain closed until the founding mission resolves successfully.

The active-project helper also blocks any ordinary paid project during the founding mission, including a transient state where setup or mission resolution facts are evaluated in different ticks.

After successful mission cancellation, the resolution flag is set and the mission is no longer active, so the serialized paid-project layer opens normally.

Timeout or invalidation still sets the existing failure receipt and uses the existing BSK failure effect; this patch does not alter those outcomes.

## Validation

- `python .tools/audit_event6_allocator.py --strict` passed.
- `python .tools/audit_event6_country_api.py` passed.
- `python .tools/audit_event6_flags.py --strict` passed.
- `python .tools/audit_event6_form16.py` passed.
- `python .tools/audit_event6_gui_matrix.py` passed.
- `python .tools/audit_event6_scenario_matrix.py` passed for all 32 SCN-008 cells and eight edge cases.
- Static source review confirmed the BSK founding mission remains activation-backed and that the ten paid BSK project blocks continue to call the shared readiness and active-project helpers.

## Skipped meaningful validation and runtime limits

No live Hearts of Iron IV process, save/load test, or non-empty engine transaction was run; live consumer validation remains user-owned.

No GUI inspection or render was required because this patch changes only decision lifecycle triggers and does not alter a GUI surface.

The required delegated probability auditor route was not rerun because no AI or mission weight changed; the prior BSK audit recorded the exact installation blocker `NO_CALLABLE_CHAOSX_AI_PROBABILITY_AUDITOR`, and this narrow lifecycle patch makes no quantitative balance claim.

## Remaining issues

No remaining BSK lifecycle defect was identified within the admitted scope.

The existing package audit caveats, workspace-wide engine diagnostics, and portrait source-placeholder status remain unchanged and are outside this patch.

No simplification or fallback was introduced.
