# Event 021 selected actor and anchor lifecycle

Disposition: implemented, with partial MCP validation.
Acceptance basis: parent-authorized startup loader repair and complete target lifecycle remediation; no gameplay redesign or weight adjustment.

## Files and contract

- `common/scripted_effects/021_random_civil_war_parent_effects.txt`: selected actor/anchor resets, successful selection markers, and every presence gate.
- `common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt`: capture reset and all 32 successful static carrier mappings.
- Matching markdown files: lifecycle, scope, defaults, side effects, and example documented.

The real host is saved as the regular `random_civil_war_event6_selection_owner` target.
The host owns `random_civil_war_event6_selected_actor_valid` and `random_civil_war_event6_selected_anchor_valid` country flags.
The flags invalidate consumption without pretending to erase a regular target, changing its type, assigning a fake null target, or introducing global pointers.
All eight actor presence gates and four anchor presence gates require both the selected pointer and its validity flag through the owner target.
Target blocks and target-valued arguments beneath these gates retain their original synchronous scope behavior.

## Lifecycle and call sites

`event021_parent_prepare_route_evidence` resets both flags and binds the current host before candidate admission; this prevents the prior host's selection leaking into the next same-chain review when no dormant package search runs.
Its callers are current-country review, target preparation, two scenario paths, and a later candidate path in the parent effects file.
`event021_parent_find_event6_package` resets both markers at entry, publishes anchor validity with the admitted anchor, and publishes actor validity only when the admitted loader supplies a carrier.
Its failed-search branch invalidates both markers.
A valid anchor with no valid actor deliberately means a dormant carrier must be released; it does not mean the previous actor may be reused.

`event021_parent_capture_event6_selected_actor` calls the Event 006 adapter registry in the host after release.
The registry resets actor validity at entry and sets it only in the same successful branch as each of its 32 existing-carrier writers.
The registry is called only through this wrapper, by primary and secondary front creation.
Both callers use the same host as the anchor selection; the owner binding is not overwritten by nested actor setup.

Evidence registration, connected-state planning, actor package preparation, primary/secondary preexistence checks, primary/secondary materialization, and primary/secondary rollback consume guarded pointers.
Actor preparation runs in actor scope but reads host validity through the explicit owner target, avoiding a new dependence on ROOT.
Primary and secondary rollback consume selected targets before `event021_parent_clear_event6_package_transaction` invalidates both host flags.
The secondary compatibility cleanup forwards to that same transaction cleanup.
Successful creation copies durable actor and anchor receipts before cleanup.

The only presentation continuation in these creation branches is `chaosx.nr21.8` in `events/021_random_civil_war.txt`.
It checks the active-front country flag and has a presentation-only option; neither it nor localisation/scripted localisation reads the selected targets.
No delayed selected-target consumer was found in the complete `common`, `events`, and localisation identifier inventory.
Regular target pointers still expire naturally with their effect chain; validity flags are reset on each host review, search, and completed/aborted transaction.

## Validation and limits

Source-path review covered: previous success then failed search; anchor-only dormant package; failed release/capture after an earlier actor capture; successful reuse; primary rollback; secondary rollback; success cleanup; consecutive candidate hosts; nested actor preparation; and presentation continuation.
Mechanical writer/guard inventory confirmed 32 registry captures with 32 paired success flags, eight actor guards, and four anchor guards.
No constants or tuning table changes were needed; no probability fields were changed.
The selected-target clear inventory at edit time contained six remaining unsupported clears, all replaced; the parent assignment's eight-site estimate did not match the current shared file.
Other workers concurrently own unrelated changes in the parent source file.

MCP `event_inspect` returned `EVENT_INSPECTED_PARTIAL`, revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`.
Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ac783a87e55921f939fa0cabfd47d530baa659798cff87a0a3047be3df045e23/ece0358b56f55fcfcd1ca21729071eb7b513f8ec36d4d4df8d8ac1ba42b885ef/event-trace-4bccb6ec7fe1.json`.
MCP target rendering returned `EVENT_RENDERED_PARTIAL`, selectedNodes 0, with the same revision.
Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a1c310e691b59c95770ce8ac5432662db9b34b8a4832a16b26cccd45b6a294b/8a53696640d06fd89e65d1fecb0c8429311f81d4d627d2c62495bf04e67338b2/event-targets-4bccb6ec7fe1.json`.
Exact MCP limitation: `Large workspace analysis deferred workspace-wide helper projections and lifecycle passes; direct evidence is linked`.
These reports do not establish engine lifecycle correctness; source-path review is supplementary evidence only.
Comparison failed with `EVENT_REVISION_NOT_CACHED`: `Requested event graph revision is not cached`, despite using the revision returned by the baseline render.
The exact result and baseline render metadata are recorded in `selected_actor_lifecycle_mcp_evidence.json`.
No before/after engine comparison was established.
No live game control or live validation was performed.
No implementation simplification was introduced; complete MCP lifecycle validation remains unavailable under the returned large-workspace limit.

## References and recovery

Read AGENTS.md, the events and subagents skills, the required offline wiki core pages, event-target and scope behavior, vanilla effects/triggers documentation, script-constant documentation, the dynamic helper registry, and vanilla Generic event target precedent.
Skills used: `chaos-redux-events`, `chaos-redux-subagents`; no skills changed.
Original parent source baseline was supplied by the parent; the other three edited files were backed up beneath `baseline/scripts/common/scripted_effects/` before mutation.
Recovery must reverse only the selected-target patch in the shared parent source; do not restore the whole shared file over other workers' changes.
No commit was made, per parent instruction.
