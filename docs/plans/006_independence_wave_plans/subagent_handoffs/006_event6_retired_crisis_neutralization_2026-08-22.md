# Event 006 retired-crisis neutralization handoff

Date: 2026-08-22.

The pre-event Independence Wave crisis is retired. `common/scripted_triggers/006_independence_wave_crisis_triggers.txt` already fail-closes every pressure, barrier, opening, and cost trigger with `always = no`; this tranche neutralizes the corresponding legacy effects as well.

`common/scripted_effects/006_independence_wave_crisis_effects.txt` now keeps the eleven historical helper identifiers as empty compatibility stubs: `independence_wave_pay_crisis_cost`, `independence_wave_set_crisis_cooldown`, `independence_wave_clear_crisis_runtime`, `independence_wave_apply_crisis_blocked_consequence`, `independence_wave_record_crisis_history`, `independence_wave_record_crisis_resolution_history`, `independence_wave_queue_crisis_release`, `independence_wave_clear_crisis_retry`, `independence_wave_resolve_pre_wave_crisis`, `independence_wave_cancel_pre_wave_crisis`, and `independence_wave_recover_crisis_requester_loss`.

This removes the old manpower, army-experience, command-power, equipment, stability, resistance, cooldown, queue, event-log, and retry side effects. A stale reference can still parse, but it cannot create a player-facing category, mission, cost, pressure, queue, history row, or early Event 006 request.

No active reference to any retired crisis effect remains outside the compatibility file, and the hidden `chaosx.nr6.3` endpoint remains cleanup-only. The public `chaosx.nr6.1` root remains the sole release entry point and still presents `chaosx.nr6.2` only after a committed positive presentation count.

The change is committed as `6b457fb60` (`fix(event006): neutralize retired crisis effects`). No decision, localisation, package, asset, or central admission surface was changed by this handoff.
