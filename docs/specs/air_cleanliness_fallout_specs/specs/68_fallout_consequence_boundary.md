# Fallout consequence boundary and population-loss contract

## Status

This correction is accepted for implementation. Fallout is a world consequence transition. It is not a normal Event Details row, an evolution entry, or an ordinary super-event. The transition may still use country events for blackout presentation, phase scheduling, recovery, and later survivor chains. Those later chains are ordinary post-consequence content and may keep their own event history.

## Public ownership

`common/scripted_effects/chaosx_events_log_effects.txt` is the public Event Details registry. Fallout is absent from that registry and from `world_end_scenario_id`. Its stable settings-ledger value lives in `fallout_consequence_id` inside `common/script_constants/fallout_world_end_constants.txt`. It is not a public event identity.

The public Event Details scripted localisation has no Fallout title, owner, or details branch. The Fallout-specific Event Details card preparation hook is absent. The New Zealand survivor card remains a post-consequence card and no longer embeds a world-end scenario description. The generic world-end selector returns the direct `chaos_tier_end_fallout` consequence label, while the blackout GUI and sound remain Fallout-owned.

## Air Cleanliness shutdown

`fallout_air_cleanliness_disabled` is a durable global transition flag. The standard coordinator sets it when the request envelope is admitted, before host reconciliation, and keeps it through the locked transition. After the snapshot is ready, `fallout_disable_air_cleanliness_after_fallout_admission` is the idempotent Fallout-owned shutdown that removes live Air pressure, suspends Air Winter, and closes treaty operations. A temporary `fallout_air_cleanliness_request_paused` flag records that early ownership and restores the ordinary mechanic only if validation rejects the pending envelope. The Air request trigger accepts the durable flag only while this temporary admission marker is present, so recording shutdown ownership cannot make a valid 100 percent request reject itself. Save migration calls the same shutdown whenever `world_end_fallout` is already present. The manual scenario calls it after a valid sweep starts and after its prestrike ledger is frozen. It never clears the durable flag from a sweep failure after admission, so an incomplete destructive sweep cannot reopen Air Cleanliness.

The host manual reconciliation also repairs the durable flag for an admitted manual transaction after save recovery. It requires a sweep, native-strike, countdown, request, or launcher receipt, so an invalid-intensity error that never admitted the sweep does not disable Air Cleanliness.

The flag is consumed by the Air Cleanliness boundary surfaces:

- `air_winter_system_enabled` rejects all future Air Winter updates and decisions, while `air_winter_event_targets_are_valid` rejects already-scheduled openings and delayed results after request-time shutdown. The mapmode remains a historical view of the last valid Air Winter receipts and receives no further updates.
- `air_winter_response_target_is_valid` rejects pending terminal response events after request-time shutdown, so an abandonment or decontamination choice that was already open cannot mutate a state, add a country effect, or register a stale death after Fallout owns the Air boundary.
- `air_winter_response_mutation_is_allowed` gates every timed Air Winter decision removal callback. A same-day expiry after Fallout admission releases the project without applying its result, while the ordinary expiry path still calls the reviewed result effect.
- The direct Air Winter phase, building-damage, population-loss, and disease-modifier helpers also reject the durable flag, so a callback outside the monthly coordinator cannot reopen those mutation surfaces.
- Controlled and final evacuation project validators reject the same flag before a delayed project can transfer population or refugee pressure after Fallout request admission.
- The shared `air_winter_event_apply_deaths` helper rejects the same durable flag, so a stale open Air Winter choice cannot register a new winter population loss after Fallout request admission.
- `air_winter_suspend_all_states_for_fallout` removes active phase, disease, railway, airbase, response-project, pending-event, Air-owned global, nuclear fallout, chemical contamination, and thermonuclear modifiers while preserving the last valid Air Winter phase and survival ledgers for that historical map view. This prevents a stale daily contamination or deaths pulse from mutating the disabled Air surface.
- The monthly Air Cleanliness coordinator does not begin or update Air Winter, treaty pulses, or Air Winter dispatch after the flag is set.
- Natural wildfire smoke, volcanic ash, and ashfall aftermath registration returns zero after the flag. The monthly natural source reservoir and pulse are cleared.
- The Black Plague Air source refresh clears its disease-derived reservoir and previous contribution after the flag, so a later disease pulse cannot repopulate the disabled Air surface.
- Ordinary nuke-drop handling, Final Silence fallout helpers, and the Air Winter reactor-failure helper reject the flag before adding `nuclear_fallout_state`. The ordinary nuke callback also removes a stale modifier before it can feed the disabled Air source.
- The daily contamination and outbreak Deaths pulse rejects `nuclear_fallout_state` while the durable Air shutdown is set and removes a stale copy instead of registering another nuclear loss. Chemical contamination remains an independent CBRN surface and is not disabled by this Air-only guard.
- `air_contamination_apply_delta_bp` ignores later Air Cleanliness deltas. It does not rewrite the committed 100 percent contamination state.
- State-wide Air Cleanliness modifiers and country pressure ideas are removed by `air_contamination_apply_state_modifier`.
- Treaty membership eligibility, pending invitations, decision visibility, host lifecycle pulses, and late violation callbacks reject the flag and close operational routes.
- The Air Cleanliness settings checkbox and exported settings row show the system as disabled. The settings toggle cannot re-enable it, and the scripted GUI click trigger rejects `fallout_air_cleanliness_disabled` so the post-Fallout control is not presented as active.

The shutdown is deliberately separate from the final-silence lock. Fallout is terminal for Air Cleanliness even if a previous settings state or final-silence branch would otherwise reopen a monthly pulse.

The Final Silence handoff trigger and its contamination setter also reject `fallout_air_cleanliness_disabled`, so a predecessor cannot reopen the coordinator or restore Air pressure after Air shutdown.

## Standard Fallout population loss

The accepted state loss ladder is defined in `common/script_constants/fallout_world_end_constants.txt` by `fallout_population_loss_percent`:

| State grade | Direct population loss |
| --- | ---: |
| Remote refuge | 90 percent |
| Scarred province | 91 percent |
| Ash zone | 92 percent |
| Dead city | 93 percent |
| Wasteland | 94 percent |
| Vitrified zone | 95 percent |

`fallout_apply_transition_phase_population_loss` scans every valid state in the frozen world snapshot. `fallout_apply_state_population_loss` computes the grade-specific target from the captured pre-transition population. `fallout_reconcile_population_loss_receipt` records the live delta and calls `chaos_meter_register_deaths` with `chaos_deaths_reason = fallout_aftermath` after the state population mutation. The receipt is generation-bound and idempotent. The standard path therefore deletes 90 to 95 percent from each state and feeds the same loss into the Deaths ledger rather than applying a variable-only shortcut.

Fallout-owned registration is mandatory even if the general Deaths setting is disabled. The shared Deaths effect and exact population-loss helper explicitly admit the request-time Air shutdown, Fallout transition, active Fallout, and manual scenario flags. Ordinary non-Fallout losses retain the setting gate. New Fallout receipts therefore resolve to zero-loss or registered-loss only.

The shared `air_contamination_update_threshold_flags` effect is also gated by `fallout_air_cleanliness_disabled`. A stale GUI, legacy terminal caller, or save-recovery pass cannot rebuild Air Cleanliness threshold flags or fire ordinary contamination news after Fallout request intake.

## Manual sweep population loss

The manual scenario captures every state's pre-strike population before native strike callbacks. Each struck state is then processed by `fallout_manual_apply_state_aggregate_consequence`. The aggregate death percentage is clamped between `fallout_manual_aggregate.death_percent_base` and `fallout_manual_aggregate.death_percent_max`, which are the approved 90 and 95 percent endpoints.

The effect computes the exact remaining-population target, supplies the state population-loss contract, and calls `apply_exact_state_civilian_population_loss`. Its provenance receipt then measures the complete pre-strike-to-post-strike loss after native callbacks and exact reconciliation, adding that observed amount to `global.fallout_manual_total_civilian_deaths` and `chaos_state_civilian_deaths_total`. After the state loop, `fallout_manual_apply_aggregate_consequences` calls `chaos_meter_register_deaths` with civilian mode enabled and state population application disabled because the exact state mutations have already occurred. This prevents double deletion while keeping the complete observed loss in the Deaths system rather than only the direct mod adjustment.

After each state records its synthetic Fallout intensity and expiry ledger, `fallout_manual_apply_state_aggregate_consequence` removes the ordinary `nuclear_fallout_state` modifier. A native strike therefore cannot leave a daily nuclear Air contamination or Deaths source behind after the durable Air shutdown.

## Engine-sensitive proof boundary

The state mutation and aggregate Deaths routing are source-proven by the effects named above. The vanilla references document `launch_nuke` inputs but do not specify whether its native callback changes population or writes this mod's Deaths ledger. Runtime review must therefore confirm that the observed aggregate receipt is not duplicated by an undocumented native callback. The exact engine-native sweep across every valid installed-map province remains a separate runtime proof requirement for the manual scenario. Until those properties are proven in a live consumer session, the manual scenario remains dormant and the completion report must retain those blockers. No variable-only fallout, one-strike-per-state substitute, or public Event Details registration may be presented as equivalent proof.

## Review checklist

- Fallout has no public Event Details registry entry.
- Fallout has no public Event Details title, owner, or details localisation branch.
- Fallout has no evolution registration.
- Fallout blackout display text and audio remain dedicated to the consequence transition.
- Air Cleanliness is disabled by a durable Fallout-owned flag.
- Wildfire, volcanic, ashfall, Air Winter, treaty, settings, and delta boundaries consume that flag.
- Standard and manual state population loss both use the approved 90 to 95 percent band.
- Both paths record the observed civilian loss through Deaths after state population mutation.
- Fallout-owned Deaths registration remains mandatory when the general Deaths setting is disabled.
- The exact native manual sweep remains explicitly unproven until live runtime evidence exists.
