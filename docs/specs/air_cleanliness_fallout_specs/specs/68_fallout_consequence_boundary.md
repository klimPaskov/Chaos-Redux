# Fallout consequence boundary and population-loss contract

## Status

This correction is accepted for implementation. Fallout is a world consequence transition. It is not a normal Event Details row, an evolution entry, or an ordinary super-event. The transition may still use country events for blackout presentation, phase scheduling, recovery, and later survivor chains. Those later chains are ordinary post-consequence content and may keep their own event history.

## Public ownership

`common/scripted_effects/chaosx_events_log_effects.txt` is the public Event Details registry. Its initialization intentionally omits `world_end_scenario_id.fallout`. The stable numeric id remains in `common/script_constants/world_end_scenario_registry_constants.txt` for request gates and settings ledgers. It is not a public event identity.

The public Event Details scripted localisation has no Fallout title, owner, or details branch. The Fallout-specific Event Details card preparation hook is absent. The New Zealand survivor card remains a post-consequence card and no longer embeds a world-end scenario description. The super-event title selector uses the dedicated `fallout_world_end_blackout_title` key while the blackout still uses its dedicated sound path.

## Air Cleanliness shutdown

`fallout_air_cleanliness_disabled` is a durable global transition flag. The standard coordinator sets it when the request envelope is admitted, before host reconciliation, and keeps it through the locked transition. A temporary `fallout_air_cleanliness_request_paused` flag records that early ownership and restores the ordinary mechanic if validation rejects the pending envelope. Save migration restores the durable flag whenever `world_end_fallout` is already present. The manual scenario sets it when a valid sweep starts and clears it when that sweep fails before Fallout ownership is established.

The flag is consumed by the Air Cleanliness boundary surfaces:

- `air_winter_system_enabled` rejects all future Air Winter updates, decisions, and events. The mapmode remains a historical view of the last valid Air Winter receipts and receives no further updates.
- `air_winter_suspend_all_states_for_fallout` removes active phase, disease, railway, airbase, response-project, and pending-event effects while preserving the last valid Air Winter phase and survival ledgers for that historical map view.
- The monthly Air Cleanliness coordinator does not begin or update Air Winter, treaty pulses, or Air Winter dispatch after the flag is set.
- Natural wildfire smoke, volcanic ash, and ashfall aftermath registration returns zero after the flag. The monthly natural source reservoir and pulse are cleared.
- `air_contamination_apply_delta_bp` ignores later Air Cleanliness deltas. It does not rewrite the committed 100 percent contamination state.
- State-wide Air Cleanliness modifiers and country pressure ideas are removed by `air_contamination_apply_state_modifier`.
- Treaty membership eligibility, pending invitations, decision visibility, and host lifecycle pulses reject the flag and close operational routes.
- The Air Cleanliness settings checkbox and exported settings row show the system as disabled. The settings toggle cannot re-enable it.

The shutdown is deliberately separate from the final-silence lock. Fallout is terminal for Air Cleanliness even if a previous settings state or final-silence branch would otherwise reopen a monthly pulse.

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

## Manual sweep population loss

The manual scenario captures every state's pre-strike population before native strike callbacks. Each struck state is then processed by `fallout_manual_apply_state_aggregate_consequence`. The aggregate death percentage is clamped between `fallout_manual_aggregate.death_percent_base` and `fallout_manual_aggregate.death_percent_max`, which are the approved 90 and 95 percent endpoints.

The effect computes the exact remaining-population target, supplies the state population-loss contract, and calls `apply_exact_state_civilian_population_loss`. It records the applied state delta in `global.fallout_manual_total_civilian_deaths` and `chaos_state_civilian_deaths_total`. After the state loop, `fallout_manual_apply_aggregate_consequences` calls `chaos_meter_register_deaths` with civilian mode enabled and state population application disabled because the exact state mutations have already occurred. This prevents double deletion while keeping the complete loss in the Deaths system.

## Engine-sensitive proof boundary

The state mutation and Deaths routing are source-proven by the effects named above. The exact engine-native sweep across every valid installed-map province remains a separate runtime proof requirement for the manual scenario. Until that sweep is proven in a live consumer session, the manual scenario remains dormant and the completion report must retain that blocker. No variable-only fallout, one-strike-per-state substitute, or public Event Details registration may be presented as equivalent proof.

## Review checklist

- Fallout has no public Event Details registry entry.
- Fallout has no public Event Details title, owner, or details localisation branch.
- Fallout has no evolution registration.
- Fallout blackout title and audio remain dedicated to the consequence transition.
- Air Cleanliness is disabled by a durable Fallout-owned flag.
- Wildfire, volcanic, ashfall, Air Winter, treaty, settings, and delta boundaries consume that flag.
- Standard and manual state population loss both use the approved 90 to 95 percent band.
- Both paths record civilian losses through Deaths after state population mutation.
- The exact native manual sweep remains explicitly unproven until live runtime evidence exists.
