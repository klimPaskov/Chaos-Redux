# Repo Explorer Handoff

## Scope read
- Parent task: diagnose the reported B032 / SCN-008 “Every Banner Rises” launch from a fresh USA 1936 start, where the failure report shows code `10` / `invalid_scope` and no countries released; trace the shared scenario dispatcher and Event 006’s hook, then recommend the smallest repair and owner.
- Explicit constraints: read-only except this report; no gameplay, workbook, CSV, or GUI edits; no game launch or desktop control; no web wiki; no `refresh = true`; no wide MCP queries. The parent owns shared framework work and a separate agent owns Event 006.
- Files or ids requested: SCN-008, `triggerable_scenario_id.independence_wave`, `chaosx.triggerable_scenarios.8`, `.80`, `.81`, and the shared Liberation plan bridge.
- Skills or docs read: `AGENTS.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `docs/systems/event_system/triggerable_scenarios.md`, `docs/events/006_independence_wave/systems/triggerable_scenario.md`, and `docs/plans/006_independence_wave_plans/agent_decisions_2026-10-04.md` (D9).
- Reference sections read directly after connected reference requests did not return: `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:27-35,198-217`, `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:263-307`, `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:260-263`, and installed `documentation/effects_documentation.md:2943-2967,6496-6503` under the vanilla game root.

## Primary findings

The shared settings GUI uses `context_type = player_context`; its confirmation action calls `trigger_selected_chaosx_scenario`. The shared dispatcher’s independence-wave branch copies the selected type, intensity, and rule onto the player country, sets `independence_wave_scenario_launch_queued`, and schedules the one-day country event `chaosx.triggerable_scenarios.8` (`common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:1105,1199-1207`; GUI call sites in `common/scripted_guis/chaosx_scripted_gui_settings.txt:2726,2836`).

The hidden event `.8` is a `country_event` and checks the queued flag before calling `independence_wave_trigger_scenario` (`events/006_independence_wave.txt:617-665`). The installed effect documentation says `country_event` is supported in country scope, and the offline event page says the event’s ROOT is the recipient and a fired event inherits the firing block’s ROOT as FROM. The source therefore gives no evidence of a scope loss at the shared GUI-to-event bridge.

Event 006 supplies shared plan arguments `triggerable_scenario`, `independence_wave`, and `bound_package_count = 138`, then begins the shared plan (`common/scripted_effects/006_independence_wave_scenario_effects.txt:1334-1360`; `common/script_constants/006_independence_wave_constants_registry.txt:8658-8659`). The shared guard accepts that mode/owner and any expected country count above zero through `maximum_event6_packages = 206` (`common/scripted_triggers/chaosx_liberation_release_triggers.txt:60-74`; `common/script_constants/chaosx_liberation_release_constants.txt:182-185`). These source values are internally valid; they do not support a shared argument typo as the cause.

The shared `liberation_release_begin_plan` writes `invalid_scope` when its begin trigger fails while a plan is otherwise resettable (`common/scripted_effects/chaosx_liberation_release_effects.txt:127-187`). Later, the Event 006 executor also maps ordered package-validation failures to the same rejection enum, so the player-visible `10` alone does not identify the failing stage. The executor has separate diagnostics: `global.independence_wave_execution_last_failure_detail` and `global.independence_wave_execution_last_failure_package_id`. In that separate detail enum, value `10` means `missing_country_target`, while `global.independence_wave_execution_last_failure = 10` is the shared rejection reason `invalid_scope` (`common/scripted_effects/006_independence_wave_execution_effects.txt:264-402,488-502`; `common/script_constants/006_independence_wave_constants_registry.txt:802-830`; `common/script_constants/chaosx_liberation_release_constants.txt:109`).

The repo records an exact earlier SCN-008 live failure with `independence_wave_execution_last_failure = 10`, `liberation_plan_last_failure = 0`, a locked plan, and zero releases. D9 traced it to the reserved anchor being rejected by an Event 006 exact-identity preflight that reused the pre-reservation predicate. Its surgical fix is already present: `is_independence_wave_exact_package_anchor_available` permits the same Event 006 plan’s reservation only when package id and carrier match, and IW-033 / KAR uses it for state 146 (`docs/plans/006_independence_wave_plans/agent_decisions_2026-10-04.md:176-208`; `common/scripted_triggers/006_independence_wave_package_triggers.txt:27-53`; `common/scripted_triggers/006_independence_wave_karelia_crimea_package_triggers.txt:27-33`).

The current Event 006 failure branch copies the executor reason when present, otherwise the shared plan reason, freezes the failed summary, and sends the existing player result event `.81` (`common/scripted_effects/006_independence_wave_scenario_effects.txt:1400-1445`; `events/006_independence_wave.txt:704-724`). That path already explains a failed/no-release run, so wiring the separate forced-event feedback popup into the generic scenario dispatcher would duplicate reporting and would not repair the release failure. The new feedback helper’s handoff also requires an explicit manual-request target and request flags; the generic SCN-008 launch does not establish that context (`docs/plans/shared_interface_plans/subagent_handoffs/forced_feedback_hook_20261005.md`).

The reported fresh USA run cannot be proven to match D9 because it omits `liberation_plan_phase`, `liberation_plan_last_failure`, `independence_wave_execution_last_failure_detail`, and `_package_id`. The exact new failing block therefore remains unresolved. If D9’s failed package was KAR/IW-033, the source fix is already present; if a later package fails, the package id and detail code identify the narrow Event 006 predicate to inspect.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `common/scripted_guis/chaosx_scripted_gui_settings.txt` | Confirms the scenario confirmation window runs in player context and dispatches the selected scenario. | `scenario_confirm_launch_button_click` calls `trigger_selected_chaosx_scenario`; `context_type = player_context` near line 2836. |
| `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt` | Shared launch router; the Event 006 branch stores queued selection and schedules `.8`. | `trigger_selected_chaosx_scenario` near line 1105; independence-wave branch at lines 1199-1207. |
| `events/006_independence_wave.txt` | Event 006 delayed launch barrier and player-facing success/failure results. | `.8` calls the Event 006 transaction at line 636; failure `.81` begins at line 704. |
| `common/scripted_effects/006_independence_wave_scenario_effects.txt` | Event 006 bridge to the shared Liberation plan, including failure-code propagation and cleanup. | `independence_wave_trigger_scenario` begins at line 1334; records executor/shared failure at lines 1400-1408. |
| `common/scripted_effects/chaosx_liberation_release_effects.txt` and `common/scripted_triggers/chaosx_liberation_release_triggers.txt` | Shared plan begin behavior and the guard that can write reason 10. | Begin effect lines 127-187; reset/begin guard lines 50-74. |
| `common/scripted_effects/006_independence_wave_execution_effects.txt` | Ordered executor checks and the separate detail/package diagnostics. | Validation starts at line 264; failure reason/detail are published at lines 488-502. |
| `common/scripted_triggers/006_independence_wave_package_triggers.txt` and `common/scripted_triggers/006_independence_wave_karelia_crimea_package_triggers.txt` | Existing Event 006 repair for anchors reserved by their own plan. | New same-package/same-carrier reservation exception at lines 36-54; IW-033 exact trigger calls it for state 146 at lines 27-33. |
| `docs/plans/006_independence_wave_plans/agent_decisions_2026-10-04.md` | Records the prior SCN-008 runtime failure, root cause, and applied Event 006 fix. | D9 at lines 176-208. |
| `docs/events/006_independence_wave/systems/triggerable_scenario.md` and `docs/systems/event_system/triggerable_scenarios.md` | Define the frozen SCN-008 transaction, rejection behavior, and 138-row scope. | SCN-008 transaction section near lines 1-40; shared scenario catalog SCN-008 section near lines 122-130. |

## Existing patterns

SCN-008 is intentionally a queued exception in the shared scenario router because it requires a one-day revalidation barrier before a large frozen transaction. The queue is country-owned; the shared global plan and package ledgers are created only after `.8` validates and the Event 006 effect begins the plan.

The existing player failure result `.81` is the SCN-008 failure surface. The shared forced-event report is a distinct opt-in request callback, not an automatic event-dispatch observer. No SCN-008 launch flags or regular requester target are set by the current router, and adding the helper to the shared router would both miss that contract and blur ownership.

The nearest repair pattern for the prior failure is package-owned: ordinary candidate-anchor checks remain strict before reservation, while exact execution preflight accepts only that row’s own current-plan reservation. This preserves duplicate and protected-state rejection.

## Vanilla or reference precedents

`paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:27-35` documents the event ROOT as the receiving country and the event sender as FROM; lines 198-217 describe delayed `country_event` invocation and that the event trigger is checked when it fires. This matches the `.8` country-scoped barrier and its flag recheck.

`paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:260-263` defines ROOT, THIS, and PREV; `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:303-307` documents regular event-target lifetime and inheritance into events fired by an effect chain.

Installed `documentation/effects_documentation.md:2943-2967` defines `country_event` as a country-scope effect with optional delay, and `:6496-6503` documents `save_event_target_as` as valid in any scope. The offline wiki and installed documentation were read locally because the connected reference routes did not return results in this task.

## Likely edit order for the parent

1. Read the current failure diagnostics before changing the shared dispatcher: `global.independence_wave_execution_last_failure`, `global.independence_wave_execution_last_failure_detail`, `global.independence_wave_execution_last_failure_package_id`, `global.liberation_plan_phase`, and `global.liberation_plan_last_failure`.
2. If the plan never left idle/collecting and only `liberation_plan_last_failure = 10` is set, check the live `liberation_call_mode`, `liberation_call_plan_owner`, `liberation_call_expected_country_count`, and the opening-report pending flag at `.8` before modifying the shared guard. Current source inputs are valid.
3. If the plan locked and the executor reason is 10, use `_detail` and `_package_id` to route the failing package. For an anchor/preflight failure, ask the Event 006 owner to inspect that package’s exact identity trigger against the existing same-package/same-carrier reservation helper. Do not change the shared allocator without evidence that its plan arrays or event-target binding failed.
4. Keep the `.81` result as the sole SCN-008 popup unless a separate accepted design explicitly asks for the forced-event report. If that report is required, the Event 006 owner owns the failure-branch call site and the shared-framework owner owns any request-context setup; review the interaction with `.81` before adding it.

## Validation checks

- After an Event 006 package-trigger repair, run the existing `python .tools/audit_event6_allocator.py` check and confirm it still recognizes the strict pre-reservation pool plus the exact current-plan reservation exception.
- Retry the narrow read-only Event MCP requests after the connected service responds: inspect event `chaosx.triggerable_scenarios.8` upstream at depth 1, then render the same event’s scope view; retain returned diagnostics, source revision, and artifact URIs.
- Reproduce the same fresh USA 1936 SCN-008 launch and record the globals listed in step 1. The user owns live-game validation; no game was launched during this exploration.
- No source patch, dry-run, allocator audit, or gameplay validation was performed by this read-only explorer.

## Risks and blockers

Confirmed: the exposed connected tool list includes the event and reference routes, but tool exposure alone does not prove service health. With the corrected narrow selector `{ kind: "event", eventId: "chaosx.triggerable_scenarios.8" }`, `hoi4.event_inspect` remained pending for more than 90 seconds and was terminated; a parallel `hoi4.event_render` scope request and short `hoi4.reference_context` request remained pending for several minutes and were terminated. No event artifacts, reference ids, revisions, or useful MCP diagnostics were returned. The source and local documentation evidence above is not a substitute for the required MCP evidence.

Unresolved: the reported value `10` is ambiguous unless its global variable is named. Shared `liberation_plan_reject_reason.invalid_scope` is 10; the separate Event 006 execution-detail enum also has a value 10, but it means `missing_country_target`. The fresh run’s `_detail`, `_package_id`, plan phase, and plan reason were not supplied.

Unresolved: D9’s previous failing package and fix are documented and present in the current source, but this task has no post-fix save or current failed-package detail to establish whether the new USA run repeats that defect, loads older source, or reaches a different package check.

No rollback is needed because no gameplay files were changed. If a new patch is warranted, first review a one-hunk dry-run against the exact diagnosed guard, have the owning agent apply it, review the final diff with the parent, then run the allocator audit and the event MCP inspect/render pass. Recovery should revert only that owner’s hunk if the targeted check or scenario evidence regresses, preserving concurrent shared-tree edits.

## Recommended next action

Have the live-run owner capture the SCN-008 failure globals from the fresh run. If they identify a package preflight, hand the package id and detail code to the Event 006 owner; if they show a plan-start/target-binding problem, the parent can patch only the shared bridge or validator implicated by those values. The known KAR/IW-033 fix is already in source, so do not reapply it blindly.
