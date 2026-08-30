# Event 006 SCN-008 publication-boundary re-audit handoff — 2026-08-30

Date: 2026-08-30

Owner: `/root/event6_scn008_publication_repair`

Status: READY FOR PARENT REVIEW.

## Scope and disposition

This bounded re-audit covers the SCN-008 scenario publication receipt, the Event 006 result and ledger exposure boundary, the scenario ledger category, and the three zero-cost ledger navigation decisions.

The owned gameplay files already contain the accepted P0 repair at the audited revision, so no gameplay source change was necessary.

The existing static validator now contains the requested narrow setter/call-site census and publication-order assertions.

## Issue list sorted by severity

- P0: None in the owned SCN-008 publication surface.
- P1: None in the owned category or ledger controls; each requires the current committed receipt, rejects both scenario failure receipts, and requires the ledger-visible country flag.
- P2: The GUI MCP generated the ordinary `decision_category` scenario but reported that no dedicated `decision_category` window was found and returned truncated workspace diagnostics; no GUI rewrite is in scope for this standard decision surface.
- Informational: `global.independence_wave_scenario_last_failure` is populated while the failed summary is assembled and is not cleared by the final reset call; it is not a visibility gate, commit receipt, or public ledger array, the failed path dispatches no result event, and the next generation clears it at launch. Changing this diagnostic variable would require parent-owned event/UI review and was intentionally left untouched.

## Decision category lifecycle notes

`independence_wave_trigger_scenario` resets the prior ledger before beginning a new plan, and `liberation_release_begin_plan` clears the shared joint-plan receipt for the new generation.

The success gate requires the committed plan phase, the current scenario plan id matching `global.liberation_plan_id`, Independence Wave plan ownership, `liberation_release_joint_plan_executed`, and no execution, scenario, or finalization failure flag before setting `independence_wave_scenario_committed`.

Only the successful branch freezes the published summary and dispatches `chaosx.nr6.2` followed by the delayed `chaosx.triggerable_scenarios.80`.

The failure or rollback branch clears `independence_wave_scenario_committed`, performs existing rollback or abort handling, and calls `independence_wave_scenario_reset_summary` before returning.

The reset clears `independence_wave_scenario_ledger_visible`, ledger cursors, summary dates, released and blocked package arrays, rejection reasons, country rows, and summary counts.

The parent-owned queued-launch failure branch in `events/006_independence_wave.txt` also clears the commit receipt and resets the summary without dispatching `.80`.

## Cognitive-load notes

The SCN-008 category is hidden unless a committed generation has a non-empty blocked-package ledger and the result event has explicitly opened the ledger flag.

The visible action count is three zero-cost controls: previous row, next row, and close ledger.

The controls are navigation and close actions rather than competing gameplay choices, and the AI weight is zero for all three.

There are no SCN-008 missions or extra tabs attached to this surface, and no category exceeds the six-primary-action limit.

The result event exposes the summary counts and scenario identity before the player opens the bounded row ledger; each row is represented by aligned package, country, and rejection-reason arrays.

## Mission quality notes

No mission was added, removed, or changed in this bounded repair, so owner, category, region, requirement, duration, success, failure, and duplicate-risk review is not applicable to the changed surface.

## Cost and requirement clarity

No gameplay-changing cost was introduced or changed.

The three ledger controls have `cost = 0`, so their spendable cost count is zero and no texticon coverage is required.

The category and controls separate visibility requirements from the zero-cost navigation action, and no cost string spells out a resource name or hides a fifth spendable cost.

## AI validity and route locks

The ledger controls retain `ai_will_do = { base = 0 }` and cannot be selected by AI.

The scenario route checks current plan identity, plan owner, shared joint-plan execution receipt, phase, and failure flags before publication, preventing stale-plan or failed-generation publication.

The delayed `.80` event trigger and option `.80.a` independently require the committed, non-failed receipt before displaying or opening the ledger.

## Localisation and tooltip gaps

No localisation, tooltip, title, art, cost, mission, or gate text was changed.

Existing result localisation and scripted localisation remain parent-owned and continue to describe the committed summary; no failure result event is dispatched from the failed branch.

The GUI MCP fidelity artifact reports `GUI window decision_category was not found`, so no production layout or click-region claim is made for the ordinary decision category.

## Cleanup and exploit-risk notes

The failed path clears the commit receipt and summary surface before returning, preventing a stale country flag or blocked-array residue from exposing the category.

The shared plan-begin effect clears the previous joint-plan execution receipt, and the success gate requires the newly executed receipt.

The publication census found one global scenario-commit setter, one ledger-visible country setter, one SCN-008 result-event dispatch, one scenario log dispatch, and zero `.2` or `.80` dispatches in the failure branch.

No free reward, cost bypass, repeated publication, war-goal loop, stale target, or cooldown exploit was introduced.

## Changed files and identifiers

- `.tools/audit_event6_scenario_matrix.py`: added brace-aware block extraction plus explicit SCN-008 setter, dispatch, order, failure-branch, result-trigger, category, and control visibility assertions.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_scn008_publication_boundary_reaudit_2026-08-30.md`: this evidence handoff.

The following owned gameplay files were inspected and remained unchanged because the accepted repair was already present: `common/scripted_effects/006_independence_wave_scenario_effects.txt`, `common/decisions/categories/006_independence_wave_categories.txt`, and `common/decisions/006_independence_wave_decisions.txt`.

No gameplay identifier changed in this re-audit.

## Before and after behavior

Before this re-audit, the current source already had the accepted P0 behavior: only the successful SCN-008 branch set the publication receipt, dispatched `.2` then `.80`, and allowed the result event to open the ledger.

After this re-audit, gameplay behavior is unchanged and the validator fails if a second setter or result dispatch appears, if publication order changes, if the failure branch dispatches either event, or if the result/category/control receipt gates are weakened.

## Validation and evidence

- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases.
- The validator publication census reported `commit_setter_count=1`, `ledger_visible_setter_count=1`, `scenario_result_dispatch_count=1`, `scenario_log_dispatch_count=1`, order `chaosx.nr6.2 -> chaosx.triggerable_scenarios.80`, and zero failed-branch `.2` or `.80` dispatches.
- `python -B .tools/audit_event6_allocator.py` passed the Event 006 allocator and 138-package SCN-008 ranked-registry checks.
- Source census witnesses are `common/scripted_effects/006_independence_wave_scenario_effects.txt:1380` for the sole commit setter, `:1389-1390` for successful publication order, `:1394` for failure receipt clearing, `events/006_independence_wave.txt:600` for the sole ledger-visible setter, `common/decisions/categories/006_independence_wave_categories.txt:634-646` for category gating, and `common/decisions/006_independence_wave_decisions.txt:937-1026` for the three gated controls.
- `hoi4.gui_inspect` returned `GUI_INSPECTED` in workspace `mod_chaos_redux_ea3b2d67c2c0`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2b89a8fca0f54ba7206f9942b28def54fd14f99aff608c2cbf25ce9b5d9fdbe3/dd280df07f33b0f7dd41bedfe7c8cd3c7c0dd057fa06b9a38a90f1cde406b684/gui-inspect.2a05546918cbd9a8.json` records the standard decision-category inspection and global graph diagnostics.
- `hoi4.gui_render` returned `GUI_RENDERED` with five states and two requested resolutions; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9aeba909b09e0513d4ea67625eec2b76b1e8e1414f88519815b87e0de3a20ea2/4a469545dad400ecdf7e08ea00292a5884af96c72de028811c14e6c7133d7915/decision_category-fidelity.json` records the exact missing-window blocker, and the render is marked `offlineRepresentation=true`.
- `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL` for `chaosx.triggerable_scenarios.80`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2fde060b8b6d75a57c6752db8f34fa23a8f059c72c3cbda0bf54e39c65155998/ddc81c8532dafe01f0f3c1ae5138c74fc542ca54524564b3b886d6f949f55d18/event-state_flow-d4de198c1706.json` reports a focused state-flow analysis with four blocking diagnostics from the broader workspace analysis.
- `hoi4.event_render` returned `EVENT_RENDERED_PARTIAL`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c88baa545a645f3b28bd35ff814b1c2ec7a3ea71feb9f19990e6cb27dcbdf1d7/09e0ea7aafd41bba5c7af3586fee23bae75bb79a017b005406049bd6a5dc3109/event-state-d4de198c1706-manifest.json` records the bounded state render and deferred workspace-wide helper analysis.

## Skipped validation, blockers, and remaining work

HOI4 was not launched, and no live-save or live gameplay claim is made.

The GUI route could not provide one-to-one standard decision-category fidelity because the MCP reported no `decision_category` window and global diagnostics were truncated; no GUI rewrite was authorized or required for this source-only boundary repair.

The event MCP routes were available only as partial workspace analyses with deferred helper projections, so source/static validator evidence remains the authoritative result for this bounded repair.

No probability audit was required because this re-audit changed no AI weight, score, MTTH, random selection, or balance target.

No plan handoff was written because no broader mechanic or design change was necessary.

No simplification, fallback, unlocalized gameplay change, asset substitution, or unrelated source change was made.
