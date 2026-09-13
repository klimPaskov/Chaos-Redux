# Black Plague weaponized runtime bridge

This file is the shared runtime boundary for an already-authorized weaponized Black Plague exposure. It joins Event 016 decision-led release and native weaponization delivery to the existing Event 020 state machine without creating a second transaction or a natural-outbreak root.

The bridge is intentionally narrow. The caller remains responsible for authorization, target selection, ordinary biological proof, native payload reservation or debit, public attribution, Event 016 history, and any caller-specific consequences.

## Helper registry

| Identifier | Scope | Inputs | Outputs and side effects |
| --- | --- | --- | --- |
| `black_plague_apply_weaponized_exposure_runtime` | STATE, with `ROOT` as the release country | Required temporary `black_plague_exposure_provenance = constant:black_plague_provenance.weaponized`; optional `black_plague_exposure_amount` and `black_plague_exposure_route` | Returns temporary `black_plague_weaponized_runtime_bridge_result` as the exact shared `black_plague_exposure_result` value, bootstraps the existing runtime only when safe and not started, calls `black_plague_apply_exposure` once, and invokes scheduler reconciliation only for an accepted exposure. |
| `black_plague_weaponized_runtime_bridge_ensure_scheduler` | STATE | Accepted exposure in the current state and existing shared runtime flags | Reuses a valid global scheduler anchor, repairs an invalid receipt in place, or binds the accepted state as the anchor and schedules one pulse. It performs no world scan. |

The companion trigger file provides `black_plague_weaponized_runtime_bridge_target_is_valid`, `black_plague_weaponized_runtime_scheduler_anchor_is_active`, and `black_plague_weaponized_runtime_scheduler_receipt_is_valid` for the two effects.

## Exposure contract

The bridge accepts only a live receivable state passing the existing `black_plague_state_can_receive_exposure` predicate and an explicit weaponized provenance input. It also rejects world end, an active or completed terminal takeover, a capitulated release country, and a started-but-inactive runtime.

When the runtime has not started, the bridge calls `black_plague_initialize_runtime` in `ROOT` before exposure, but only when pulse suppression is absent. The initializer is already idempotent and its one-time state pass is treated as bootstrap, not a new periodic loop.

The bridge snapshots all three exposure inputs before bootstrap and restores them before both the post-bootstrap validity check and the shared exposure call. Missing amount or route values retain the defaults implemented by `black_plague_apply_exposure`; the caller's explicit values are not replaced by bootstrap side effects.

`black_plague_apply_exposure` remains the only exposure mutation. Its temporary `black_plague_exposure_result` is copied immediately to `black_plague_weaponized_runtime_bridge_result`; temporary variables are scope-less, so the country-scope caller reads that result directly after the state block returns. A value of `constant:black_plague_value.one` is the only accepted result.

The wrapper does not call `bio_lifecycle_dispatch_seed`, `black_plague_start_natural_outbreak`, or `black_plague_weaponization_deliver_to_state`. It does not debit or refund payload, fabricate an origin, set a recognition/report flag, or create public attribution history. The existing shared exposure effect owns weaponized state provenance and state registration.

## Scheduler receipt contract

Scheduler reconciliation runs only after the exact shared exposure result is one. A valid receipt requires the global `black_plague_scheduler_anchor_state` target to exist, retain `black_plague_scheduler_anchor`, match the global runtime generation and scheduler ticket, and hold `black_plague_scheduler_due_num_days` at or after `global.num_days`.

When that receipt is valid, the bridge does nothing, so a repeated release cannot invalidate the queued `chaosx.nr20.900` callback by refreshing its ticket or due day.

When the anchor state is live but its generation, ticket, or due receipt is missing or invalid, the bridge calls the existing `black_plague_schedule_next_pulse` once in that same state. The existing scheduler increments the shared ticket and writes the repaired elapsed-day receipt.

When the global anchor is absent or points to a state without the anchor flag, the bridge clears only the reachable old state's anchor flag and receipt fields, clears the global target, binds the accepted current state, sets its anchor flag, and calls the existing scheduler once. It never uses `every_state` to search for stale anchors.

Pulse suppression remains scenario-owned. An active suppressed runtime may still accept the exposure, but the scheduler reconciliation is skipped and no suppression flag or scenario anchor is changed. A suppressed unstarted runtime cannot bootstrap because the existing initializer would clear the suppression flag; the target predicate fails closed instead.

The bridge does not block on `black_plague_system_eradicated`. The existing active runtime and eradication history remain authoritative, allowing the documented weaponized return after natural eradication without clearing history or invoking the natural root.

## Call-site integration

`brilliant_scientist_dispatch_black_plague_release` retains the existing ordinary lifecycle proof, then calls `black_plague_apply_weaponized_exposure_runtime` after assigning the weaponized exposure inputs. Event 016 gates its Black Plague provenance and weaponization history on `black_plague_weaponized_runtime_bridge_result = constant:black_plague_value.one`, not on ordinary lifecycle proof alone.

The native `black_plague_weaponization_deliver_to_state` call site uses the same wrapper before its own payload, support-equipment, Command Power, and fuel debits. Exact bridge acceptance gates the native payment, attribution, history, cooldown, condemnation, and report effects, so a rejected state cannot consume a public-delivery package.

Both call sites must invoke the helper in the target STATE scope with the actor country as `ROOT` and set the same temporary amount, route, and weaponized provenance inputs that they currently pass to `black_plague_apply_exposure`.

## Constants and tuning

No constants or weighted surfaces are added. The bridge reuses `black_plague_value.zero`, `black_plague_value.one`, `black_plague_provenance.weaponized`, the existing `black_plague_timing.pulse_days` through `black_plague_schedule_next_pulse`, and the parent-repaired `black_plague_scheduler_due_num_days` elapsed-day receipt.

## Event targets and cleanup

The bridge uses the existing global `black_plague_scheduler_anchor_state` target because that is the Event 020 scheduler's authoritative pointer. It clears only a reachable old target during repair and leaves the target owned by the shared scheduler thereafter. No new global target, origin pointer, periodic on-action, or cleanup pass is introduced.

Queued stale state events are invalidated by the shared generation and ticket checks rather than by an unsupported event cancellation effect. A stale anchor flag whose state cannot be reached through the global pointer is intentionally outside the bridge's bounded cleanup boundary.

## Validation and evidence limits

The source audit reviewed the accepted Event 016 closure contract, the Event 016 biological dispatch, the Event 020 initializer, exposure effect, scheduler, callback, scenario scheduler precedent, and native weaponization delivery. Focused read-only Event Inspector evidence was collected for `chaosx.nr16.1` and `chaosx.nr20.900`; both returned `status: ok` with `analysisMode = focused`, no tool blockers, and deferred large-workspace helper/lifecycle analysis. The scan artifact and trace artifact are recorded in the implementation handoff.

This bridge has no AI weight, MTTH, random selection, or other probability-bearing surface, so no probability auditor or comparison is required. No GUI, map, focus, localisation, asset, spreadsheet, or in-game validation surface is introduced.

## Future plans and suggestions

If the engine later exposes a stable receipt for queued state-event cancellation or post-transfer event invalidation, the scheduler cleanup can record that evidence explicitly. Until then, generation and ticket checks remain the supported stale-callback recovery mechanism.

If a future scenario requires weaponized exposure while the runtime is not started and pulses are already suppressed, it needs an accepted scenario-owned bootstrap contract because the existing initializer clears suppression by design. This bridge deliberately does not invent that transition.
