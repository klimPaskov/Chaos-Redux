# Event 016 Terminal World-End and Fallout Causality Audit Handoff

Date: 2026-07-24.

Scope: static audit of Laboratory World, Strategic Singularity, shared Fallout request/lock integration, terminal exclusivity, duplicate prevention, stale ledger risk, and the six Event 016 super-event queue paths. No gameplay files were changed and no runtime completion claim is made.

## Evidence reviewed

- `common/scripted_effects/016_brilliant_scientist_effects.txt` (commit, terminal preparation, terminal markers, transient target cleanup).
- `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt` (six queue call sites, terminal execution, Fallout finalization).
- `common/scripted_triggers/016_brilliant_scientist_triggers.txt` and `common/scripted_triggers/016_brilliant_scientist_super_event_triggers.txt` (terminal and super-event gates).
- `common/scripted_effects/fallout_world_end_effects.txt` and `common/scripted_triggers/fallout_world_end_triggers.txt` (request envelope, coordinator, lock, and map-return cleanup).
- `common/script_constants/chaos_meter_constants.txt`, `common/script_constants/016_brilliant_scientist_constants.txt`, and `common/script_constants/world_end_scenario_registry_constants.txt` (thresholds and stable IDs).
- `common/scripted_effects/chaosx_events_log_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`, and `interface/016_brilliant_scientist_super_events.gfx` (world-end registry, history/presentation selectors, and six image assets).
- `common/scripted_effects/016_brilliant_scientist_directorate_outcome_effects.txt` and `common/scripted_triggers/016_brilliant_scientist_directorate_outcome_triggers.txt` (confirmed these files do not own terminal resolution).

Offline Paradox wiki pages for data structures, triggers, effects, scopes, event targets, and on actions were consulted alongside the required vanilla script-concept, effects, and triggers documentation. This handoff is source inspection only; no in-game save, MCP trace, or runtime acceptance test was available.

## Causality result

### Laboratory World: threshold and route lock pass

`brilliant_scientist_lab_world_terminal_is_ready` requires the KRG route commitment, current terminal map-audit proof, sufficient map control, administration, submission, an enabled scenario, no armed or fail-deadly Singularity, and `global.chaos_meter_value >= constant:chaos_meter_tier_range.tier_final.plus` (`1001`) at `common/scripted_triggers/016_brilliant_scientist_triggers.txt:956-1003`. The resolver calls the preparer again before setting `world_end`, `world_end_brilliant_scientist_laboratory_world`, owner event `16`, terminal marker, cleanup, and visible super-event `93` (`common/scripted_effects/016_brilliant_scientist_super_event_effects.txt:580-599`). The shared registry contains scenario `11` and maps it to super-event `93` (`common/scripted_effects/chaosx_events_log_effects.txt:1161-1172`), and Event Details uses the scenario-specific active flag (`common/scripted_effects/chaosx_events_log_effects.txt:1264-1266`).

This route does not use Fallout; that is consistent with the distinct Laboratory World terminal contract. It still cannot bypass the shared chaos threshold or the opposing Singularity lock.

### Strategic Singularity: threshold and shared Fallout pipeline pass

`brilliant_scientist_prepare_singularity_terminal_commit` computes the deficit to `tier_final.plus` (`1001`) and clamps it at zero (`common/scripted_effects/016_brilliant_scientist_effects.txt:3329-3344`). The execution path applies the deficit through `add_chaos_meter_value` with Event 016 reason `216`, custom-history mode, and the KRG actor, then checks `global.chaos_meter_value > tier_final.min` (`1000`) before submitting a strategic-singularity Fallout request (`common/scripted_effects/016_brilliant_scientist_super_event_effects.txt:503-563`). Therefore a device that is prepared at an earlier tier cannot enter the terminal path without first raising chaos above the normal world-collapse threshold.

The request carries `fallout_request_source.strategic_singularity` and maximum intensity into `fallout_request_aftermath`. The canonical coordinator records the pending envelope, validates it, and only at `fallout_lock_transition` sets `world_end` and `world_end_fallout`; the source-aware callback then invokes `brilliant_scientist_finalize_singularity_after_fallout_lock` (`common/scripted_effects/fallout_world_end_effects.txt:18-64`, `162-187`). That finalizer sets scenario flag `world_end_brilliant_scientist_singularity`, owner event `16`, terminal marker, and visible super-event `94` only after the Fallout lock (`common/scripted_effects/016_brilliant_scientist_super_event_effects.txt:566-578`). Registry scenario `12` and super-event `94` are present (`common/scripted_effects/chaosx_events_log_effects.txt:1174-1185`).

### Mutual exclusion and duplicate terminal rewards: pass with call-site dependence

Commitment gates reject an already locked route, the opposite terminal marker, prior permanent cancellation, `world_end`, and `world_end_disabled` (`common/scripted_triggers/016_brilliant_scientist_triggers.txt:887-915`). Singularity commitment clears the Laboratory commitment; Laboratory commitment clears the Singularity commitment (`common/scripted_effects/016_brilliant_scientist_effects.txt:3284-3324`). The two terminal marker effects permanently cancel the opposing route, lock all KRG actions, and clear armed, fail-deadly, arming, disarmament, and detonation-protocol flags (`common/scripted_effects/016_brilliant_scientist_effects.txt:3359-3381`).

Singularity consequences are guarded by `brilliant_scientist_singularity_consequences_recorded`; request submission is guarded by `brilliant_scientist_singularity_fallout_request_submitted`; post-lock finalization is guarded by `brilliant_scientist_singularity_terminal_fired`; Laboratory World requires both the opposing terminal guards and a final preparer recheck. The six mapped IDs are stable as `90` recognition, `91` formation, `92` global threat, `93` Laboratory World, `94` Strategic Singularity, and `95` qualifying defeat (`common/script_constants/016_brilliant_scientist_constants.txt:922-934`). Their image and scripted-localisation selectors are aligned (`common/scripted_localisation/chaosx_scripted_localisation_super_events.txt:253-258`, `interface/016_brilliant_scientist_super_events.gfx:4-26`).

The queue is paired FIFO arrays and dispatches only while `super_event_visible` is absent (`common/scripted_effects/016_brilliant_scientist_super_event_effects.txt:15-74`). Recognition, formation, global threat, and qualifying defeat all set a permanent fired flag/date before queuing and have `NOT = { has_global_flag = world_end }` readiness gates. Laboratory World queues only after its terminal marker; Strategic Singularity queues only from the post-Fallout-lock finalizer. This makes the current six call sites mutually safe, but the generic queue helper itself has no world-end or duplicate guard because terminal callers must queue after `world_end`; future callers must preserve the same call-site discipline.

## Findings requiring parent follow-up

### High-risk recovery gap: irreversible Singularity side effects precede Fallout lock

`brilliant_scientist_apply_singularity_terminal_consequences` sets `brilliant_scientist_singularity_consequences_recorded` before chaos, deaths, contamination, condemnation, and treaty effects, while `brilliant_scientist_singularity_fallout_request_submitted` is set only afterward and the shared request may remain pending until a later coordinator pulse (`common/scripted_effects/016_brilliant_scientist_super_event_effects.txt:503-560`). If a pending strategic request is later rejected or cleared by the shared envelope validator, `fallout_clear_pending_request_envelope` removes the request ledger (`common/scripted_effects/fallout_world_end_effects.txt:85-93`) but Event 016 has no rollback or retry path because both Event 016 receipts remain set. The normal happy path reaches the lock, but static inspection cannot prove rejection recovery. The parent should either stage irreversible consequences until the canonical lock is accepted or add an explicit request-rejection recovery/repair path that cannot duplicate deaths, contamination, or chaos history.

### Medium-risk stale target: super-event actor pointer is never cleared

Queue dispatch saves `brilliant_scientist_super_event_actor` as a global event target (`common/scripted_effects/016_brilliant_scientist_super_event_effects.txt:50-62`), but `rg` finds no consumer or cleanup outside that assignment, and `brilliant_scientist_cleanup_transient_targets_after_world_end` does not clear it (`common/scripted_effects/016_brilliant_scientist_effects.txt:3383-3405`). The paired queue arrays are removed correctly, so this does not duplicate a visible package today, but it leaves stale actor state in saves and can misattribute a later consumer. Clear the target when the queue is empty or when the visible presentation expires, unless a future presentation owner explicitly adopts it.

### Medium-risk finalizer defense-in-depth

`brilliant_scientist_singularity_fallout_finalize_is_ready` checks only the Event 016 request-submitted flag, Fallout lock flags, and the absence of the terminal marker (`common/scripted_triggers/016_brilliant_scientist_super_event_triggers.txt:157-162`). Source identity and actor identity are enforced only by the caller in `fallout_lock_transition` (`common/scripted_effects/fallout_world_end_effects.txt:181-187`). The current single caller is correct, but if a stale actor target, save migration, or future caller invokes the finalizer under another explicit source, Fallout can complete without Event 016 scenario flag `12` or super-event `94`, and no repair receipt is written. Add source/actor/route assertions inside the finalizer trigger or a failure receipt that leaves the queue retryable.

## Parent resolution

All three findings were resolved in the 2026-07-24 terminal repair tranche without changing the accepted threshold or canonical Fallout ownership.

The Singularity now records its chaos-threshold crossing through the separate one-time `brilliant_scientist_singularity_prelock_chaos_recorded` receipt, then rechecks that the Fallout ledger is free before recording the one-time Deaths, Air Contamination, Condemnation, unconventional-use, and treaty consequences.
Those consequences still precede `fallout_request_aftermath`, so the canonical pretransition Fallout snapshot includes the Singularity contamination and grading inputs required by the source-of-truth prompt.
If another request occupies the ledger after the threshold change, Event 016 does not claim submission or replay consequences; hidden event `chaosx.nr16.901` retries the same KRG transaction.
The terminal preparer uses `brilliant_scientist_singularity_terminal_commit_state_is_ready`, which preserves every route, component, command, threshold, and settings proof except the shared free-ledger predicate, so a competing Fallout request that appears during the timed detonation protocol cannot silently consume the action.
The public readiness trigger wraps that commit-state proof with `fallout_request_ledger_is_free`, preserving the normal decision and failsafe gate.

`fallout_clear_pending_request_envelope` now invokes `brilliant_scientist_recover_rejected_singularity_fallout_request` through the preserved strategic request actor before deleting the shared source, actor, and pending ledger.
The recovery effect clears only the submission receipt, records rejection and retry count, and schedules `.901`; the chaos, detonation date, and consequence receipts remain, so no retry can duplicate chaos history, deaths, contamination, condemnation, or treaty effects.
The intake call also checks for a no-pending and no-locked return, which repairs a rejected synchronous request through the same path.
Malformed envelopes without the original strategic source and actor fail closed; no country-retargeting fallback was added.

`brilliant_scientist_singularity_fallout_finalize_is_ready` now requires the KRG identity, Singularity commitment, durable pre-lock threshold receipt, consequence receipt, submission receipt, detonation date, `fallout_request_locked`, `fallout_transition_active`, `world_end`, `world_end_fallout`, the strategic source, the surviving request actor, and exact actor-tag equality.
Only the canonical source-aware lock callback satisfies that complete proof.

Super-event dispatch now clears any old Event 016 actor and cleanup receipt before binding the next queued actor.
Hidden event `chaosx.nr16.902` clears the actor after the visible presentation expires, rescheduling one day at a time while any super-event still owns the shared visible slot.
The shared `super_event_close_click` path also clears the Event 016 actor and cleanup receipt immediately before dispatching another queued package.

The nonterminal disarmament race is also closed. A controlled disarmament decision that was already running when Event 016 submitted its strategic Fallout request now fails its continuation trigger because `brilliant_scientist_krg_controlled_singularity_disarmament_can_continue` rejects `brilliant_scientist_singularity_fallout_request_submitted`; the disarmament-hold mission has the same submitted-request cancellation guard. The durable settlement certifier rejects the submitted request through `brilliant_scientist_krg_can_verify_durable_nonterminal_settlement`, and `brilliant_scientist_verify_singularity_nonterminal` repeats the guard before clearing `brilliant_scientist_terminal_commitment_singularity`. A pending strategic request therefore cannot be converted into a nonterminal settlement before the Fallout lock callback finalizes Event 016.

The finalizer no longer re-reads the mutable live chaos meter after lock. Its required `brilliant_scientist_singularity_prelock_chaos_recorded` receipt is the durable proof that Event 016 crossed the `tier_final.min` threshold during pre-lock execution, while the commit-state and execute/retry gates still reject a new submission when `settings_chaos_meter_disabled` is active. Toggling the meter after an accepted request therefore cannot strand a correctly locked strategic Fallout transition, and it does not reopen pre-submission terminal execution.

The retry scheduler also requires `brilliant_scientist_singularity_scenario_is_enabled`. Disabling the Strategic Singularity scenario while hidden `.901` is pending now stops the retry without creating a one-day loop; re-enabling it leaves a deliberate explicit execution requirement, consistent with the other terminal disable switches.

### Static recovery matrix

| Scenario | Required state transition | Duplicate and stale-state proof |
|---|---|---|
| First valid submission | Raise chaos to at least `1001`, record the one-time terminal consequences, bind KRG as the request actor, then enter `fallout_request_aftermath`. | Separate chaos and consequence receipts are set before intake, while the terminal marker and super-event remain absent until Fallout owns the lock. |
| Ledger becomes busy | Leave the pre-lock chaos receipt intact, do not set submission or consequence receipts for a request the ledger cannot accept, and schedule `.901`. | Retry recomputes a zero chaos deficit and cannot duplicate the threshold history. |
| Pending request is rejected or cleared | Recover through the preserved strategic actor before the shared envelope is erased, clear submission, record the rejection, and schedule `.901`. | Chaos, detonation date, and consequence receipts survive, so retry submits only the envelope. |
| A terminal system is explicitly disabled | Do not schedule another `.901` while `world_end_disabled` or `settings_chaos_meter_disabled` is active. | The disabled setting remains authoritative and no one-day retry loop persists; a later explicit valid terminal execution is required after re-enabling. |
| Canonical lock succeeds | Require locked and active Fallout, exact strategic source and actor equality, then set Event 016 scenario `12`, terminal history, and visible package `94`. | The strict finalizer rejects stale locks, other Fallout sources, and another actor. |
| Presentation closes or expires | Clear the Event 016 actor immediately on manual close or through `.902` after shared visibility ends. | A later Event 016 or unrelated super-event cannot inherit the stale actor pointer. |

## Cleanup and history notes

The Fallout request actor and source are preserved through lock and copied to cause-memory on map return before request targets and source variables are cleared (`common/scripted_effects/fallout_world_end_effects.txt:4470-4490`). Event 016 terminal actor preparation uses regular targets, so it survives the request/lock event chain without becoming a permanent pointer. Recognition, formation, threat, defeat, and both terminal branches persist their fired flags and dates before presentation; queue dispatch is therefore presentation state, not the sole history record.

No terminal duplicate, threshold bypass, opposing-route reopening, or missing ID/selector was found in the current six call sites. The three follow-up items above are static recovery/hygiene risks, not runtime-confirmed failures.

## Validation and limitations

- Performed targeted `rg` call-site and identifier scans across Event 016, Fallout, world-end registry, Event Details, scripted localisation, and super-event GFX files.
- Traced both terminal paths from readiness through mutation, request/lock, marker, cleanup, queue, and persistent registry/history surfaces.
- Confirmed the directorate outcome package contains no terminal resolver or Fallout call.
- Confirmed Event 016 event IDs remain unique after reserving hidden recovery IDs `.901` and `.902`.
- Refreshed the HOI4 event graph successfully, but a narrow trace could not complete because the repository-wide event issue count exceeded the tool's fixed 20,000-result ceiling.
- Skipped live scenario execution, save-state mutation, MCP event tracing, and map-control acceptance because no runtime test scenario was available.

No gameplay simplification or fallback was introduced. The three static findings are resolved in source; runtime acceptance remains outstanding and the parent remains responsible for the final completion claim.
