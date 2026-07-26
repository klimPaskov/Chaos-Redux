# Event 006 DM-58 Expiry Callback Follow-up Audit

Date: 2026-07-26.

Audited callback commit: `37c4f6036` (`fix(event006): expire reclamation operation cleanly`).

Current source revision inspected: `787a08ab28b23f3f2656771da463f260d499ab09`.

Status: **PARTIAL**.

Scope: read-only follow-up of `independence_wave_coordinate_reclamation_fronts` (DM-58), the new `chaosx.nr6.309` delayed callback, coordinator event-target lifetime, early cleanup, active-origin exit, and bounded decision/mission risks.

No gameplay, GUI, or localisation source was edited.

## Disposition

Commit `37c4f6036` supersedes the previous audit's unhandled normal natural-expiry finding.

On the normal path, a successful DM-58 writes the 365-day coordination flag, saves the activating country as `independence_wave_reclamation_front_coordinator`, and schedules `chaosx.nr6.309` for the same duration.

The callback requires the current global coordinator target to equal `ROOT` and requires a positive reclamation-front row count before it calls `independence_wave_cleanup_reclamation_front_operation`.

The shared cleanup clears the coordination flag, coordinator target, state receipts, member readiness receipts, aligned arrays, and count.

The callback deliberately does not require the timed coordination flag, which is correct because that flag has expired when the 365-day delivery is due.

The coordinator guard is sufficient against a stale callback for a later operation by another country, and `fire_only_once = yes` makes DM-58 possible only once per country, so the original coordinator cannot start a later DM-58 of its own.

The source is not fully complete for a coordinator that ceases to exist before its delayed event delivers while at least the required number of other league members remains.

The active-origin end path unregisters the departing member and invokes member-count revalidation, but it does not directly invoke the shared operation cleanup.

The revalidator cleans up only when membership falls below the three-member minimum.

The offline Event modding reference documents that a delayed event for a non-existing country is held on that country's backlog instead of continuing normally, so the source does not prove that `chaosx.nr6.309` can perform its cleanup after the coordinator is gone.

## Issue list, sorted by severity

### Medium: Coordinator disappearance is not covered by a surviving cleanup owner

`independence_wave_end_active_origin` does not call `independence_wave_cleanup_reclamation_front_operation` directly.

If the coordinator leaves or is destroyed while three or more league members remain, `independence_wave_unregister_league_member` preserves the operation because revalidation finds the member minimum still satisfied.

The delayed callback is addressed to the former coordinator, and the documented delayed-event backlog behavior for a non-existing recipient means expiry cleanup is not source-proven in that scenario.

This can leave the global target, state receipt flags, arrays, and count beyond the intended active window until another shared cleanup path runs.

Finite war goals still keep their own explicit 365-day expiry, and a later DM-58 starts by clearing existing front arrays and state receipts, so this is a lifecycle and stale-state risk rather than a direct cost, claim, or war-goal farming loop.

Recommended bounded correction: make an existing Event 006 lifecycle path that is guaranteed to survive the coordinator own the expiry cleanup, or make coordinator exit explicitly invoke the shared cleanup when the coordinator owns the active operation.

Do not add a broad world-iterating `on_daily` fallback.

If the chosen solution permits a new operation before an earlier delayed callback resolves, bind the expiry path to a unique operation identity as well as a country target.

### Medium: The witness resolver still performs nested global state scans

`independence_wave_execute_reclamation_front` retains three `every_state` searches inside its witness construction.

The resolver can stop its scoped member loops, but `every_state` itself has no documented short-circuit here, so successful and failed attempts can still scan states beyond the first valid witness.

The activation preflight is evaluated daily for eligible high-chaos candidates.

No source change in `37c4f6036` worsens this behavior, but there is still no campaign-scale no-witness or dense-league performance evidence.

### Low: AI evidence remains source-only

DM-58 retains a single high `ai_will_do` base score.

Activation, the exact preflight, live revalidation, route checks, and cost checks protect the AI from invalid targets, but no named campaign-state evaluation proves when the AI chooses this expensive escalation among valid alternatives.

## Callback safety notes

| Scenario | Source result | Evidence |
| --- | --- | --- |
| Normal 365-day expiry with coordinator alive | PASS | The scheduled callback matches `ROOT` to the saved global coordinator target and calls shared cleanup. |
| Early phase/reset/member-count cleanup | PASS | Shared cleanup clears both the coordinator target and count, causing the older callback trigger to fail. |
| Later operation by a different coordinator | PASS | The prior callback's `ROOT` cannot match the current coordinator target. |
| Later operation by the same coordinator | PASS | `fire_only_once = yes` makes DM-58 possible once per country. |
| Coordinator ceases to exist before callback delivery while three members remain | PARTIAL | The callback is country-addressed, while `independence_wave_end_active_origin` has no direct shared cleanup call and revalidation only cleans below the member minimum. |
| Save/load during the 365-day wait | UNRESOLVED | No live save/load delivery evidence was available. |

## Decision category lifecycle notes

DM-58 appears only for an active, compliant radical-revisionist league member with the enabling focus, no active crisis, three or more members, and an exact witness preflight.

It is a selectable 180-day mission.

Selection invokes the resolver once, freezes and mutation-time validates the witness, and charges strategic and major-security costs only after the count reaches the three-member threshold.

No-witness resolution rolls back partial staging before any material cost.

Timeout applies the documented league penalties and crisis transition without creating reclamation receipts.

Pre-selection cancellation has no receipts or costs to reverse.

Post-success cancellation leaves the synchronized operation active intentionally, and the new callback now covers normal expiry when its coordinator remains present.

## Mission quality notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `independence_wave_coordinate_reclamation_fronts` | qualifying Event 006 league member | `independence_wave_high_chaos_category` | exact external border witnesses | three distinct eligible members, states, and owners, plus live legality and costs | 180 days to select, then 365-day finite operation | claims, finite war goals, league deltas, coordinated fronts | rollback before cost or timeout crisis | low, guarded by global coordination state and one use per country |

## Cost, requirement, and localisation notes

The mission still uses the existing strategic and major-security custom cost helpers plus the shared-reserve threshold.

The preflight is hidden behind `independence_wave_coordinate_reclamation_fronts_preflight_tt` rather than exposing raw state loops.

The hidden callback adds no player-facing localisation surface.

The lifecycle document accurately describes the normal coordinator-bound path, but its natural-expiry sentence should be qualified or revised if the coordinator-loss case remains unresolved.

## AI validity and route-lock notes

The one-candidate probability inspection completed with a complete candidate pool and no unresolved source inputs.

The surface has eight required runtime inputs, so source inspection is not equivalent to a campaign-state decision result.

Route, active-country, charter-compliance, focus, crisis, distinct-witness, and cost gates prevent a dead, closed-route, or invalid-border AI action from reaching the paid completion branch.

## Cleanup and exploit-risk notes

The callback fixes stale arrays and receipts after normal expiry and clears its own global event target through the shared helper.

No evidence was found of repeated costless claims, finite-war-goal farming, core grants, free units, or cooldown abuse in the callback addition.

The one remaining bounded stale-state path is coordinator disappearance with the member minimum still met.

## Meaningful validation

Static source contract at current revision reported: one 365-day callback schedule, one coordinator save, one callback definition, a target-existence guard, an exact coordinator-to-`ROOT` match, a positive-row guard, one shared cleanup call, and target clearing in the shared cleanup helper.

The same static check confirmed that `independence_wave_end_active_origin` contains no direct shared-operation cleanup call and that the resolver retains three `every_state` scans.

`hoi4.event_inspect` state-flow analysis for `chaosx.nr6.309` returned `EVENT_INSPECTED_PARTIAL` because the full workspace contains unrelated global graph diagnostics.

Event inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f54ca3c8fb1674b8fef3140b44793927e5de00ef6beaa0d996ab9e8b61f0df70/8039ffebd1a279ddd4ae449d114aa962de1e28b4134c9d6c385841dce492a92c/event-state_flow-c3d04e84e398.json`.

`hoi4.probability_inspect` for the current DM-58 mission AI reported `PROBABILITY_SOURCE_INSPECTED`, one complete candidate pool, eight required inputs, and zero unresolved source inputs.

Probability inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/de28610310d9ae4d52b6b14ad742800c3d9535844e21ff3dfd358a3fd89d8a7e/6c39e4768234fe432a1e3362711b0e38d79c2cb67ae2c1d6c41e4f6b5d8badf9/probability-inspect-7dd2618caf95.json`.

The relevant DM-58 decision, effects, resolver, trigger, callback event, and lifecycle document are byte-identical between `37c4f6036` and the inspected current revision.

## Skipped meaningful validation

Live delivery after exactly 365 days, coordinator annexation or disappearance, early cleanup followed by a later coordinator, save/load of the pending delayed event, no-witness resolver cost, and AI campaign-state choices were not executed because this is a source-only audit and live HOI4 validation belongs to the user.

No DM-58 scripted GUI surface exists, so GUI inspection and rendering were not applicable.

## Files reviewed

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `common/script_constants/006_independence_wave_decision_constants.txt`
- `events/006_independence_wave.txt`
- `docs/events/006_independence_wave/reclamation_front_lifecycle.md`

## Files changed

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_dm58_expiry_callback_followup_audit_2026_07_26.md`

## Follow-up for parent

Treat the prior natural-expiry finding as fixed for the normal surviving-coordinator path.

Decide whether coordinator disappearance is an accepted lifecycle simplification or needs the bounded cleanup-owner correction above.

If it is corrected, update the lifecycle document and run the five named live scenarios before claiming complete expiry coverage.
