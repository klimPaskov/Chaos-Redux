# Fallout consequence boundary and Deaths proof

## Scope

This record covers the accepted correction that Fallout is a consequence transition rather than a normal event, Event Details row, evolution, or ordinary super-event. It also records the Air Cleanliness shutdown and the state population loss routing.

## Public registration proof

Static source inspection shows that `initialize_world_end_scenario_registry` in `common/scripted_effects/chaosx_events_log_effects.txt` registers the public world-end rows without `world_end_scenario_id.fallout`. No Fallout title, owner, or details branch remains in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`. The Fallout-specific Event Details card preparation hooks were removed from the registry refresh, detail open, and toggle paths.

The stable `world_end_scenario_id.fallout = 2` entry remains in `common/script_constants/world_end_scenario_registry_constants.txt`. It is used by internal request and settings gates and is not inserted into the public registry. The generic `GetWorldEndScenario` selector resolves Fallout to `chaos_tier_end_fallout` without exposing a Fallout title. The Chaos Meter uses consequence-neutral terminal wording, while the world-end tooltip selects the same consequence label. The dedicated blackout GUI uses its own sequential display text. Fallout blackout audio remains owned by `fallout_dispatch_blackout_audio` in `common/scripted_effects/fallout_world_end_effects.txt`.

Fallout post-consequence survivor chains still use normal country events and their own event history. This is intentional. Those are ordinary survivor stories after the consequence and are not a registration of the consequence itself.

## Air Cleanliness shutdown proof

The standard path sets `fallout_air_cleanliness_disabled` in `fallout_queue_request_envelope` as soon as the request is admitted, records temporary ownership in `fallout_air_cleanliness_request_paused`, and closes the host-reconciliation gap before `fallout_lock_transition` runs. The Air request trigger accepts the durable flag only while this temporary admission marker is present, so recording shutdown ownership cannot make a valid 100 percent request reject itself. The lock keeps the durable flag after `fallout_snapshot_epoch_is_ready_to_lock` succeeds, clears the temporary ownership flag, and calls `air_contamination_apply_state_modifier` so existing country pressure ideas and state modifiers do not linger until the next monthly pass. A rejected pending envelope clears the temporary ownership and restores the ordinary modifier surface. `fallout_world_end_migrate_save` restores the flag and performs the same immediate modifier cleanup for saves with `world_end_fallout`. The manual path sets the flag in `fallout_manual_initialize_sweep` after intensity validation, clears current modifiers before native strikes, refreshes the stored contamination display after the sweep without running the generic threshold-news updater, and clears the flag only on a pre-Fallout sweep failure, where it refreshes the ordinary Air Cleanliness modifiers together with the temporary Air Winter shutdown receipt.

Static consumers of the flag are:

- `air_winter_system_enabled` in `common/scripted_triggers/air_cleanliness_winter_triggers.txt`.
- `air_contamination_monthly_update` in `common/scripted_effects/chaos_meter_effects.txt`.
- `air_contamination_apply_delta_bp` and `air_contamination_apply_state_modifier` in `common/scripted_effects/chaos_meter_effects.txt`.
- Natural wildfire, volcanic, and ashfall source registration in `common/scripted_effects/air_cleanliness_natural_source_effects.txt`.
- Treaty membership, invitation, decision, and host lifecycle surfaces in the Air Cleanliness treaty files.
- The Air Cleanliness settings checkbox and exported settings row.

The monthly pass no longer starts or updates Air Winter after the flag. `air_winter_suspend_all_states_for_fallout` runs once at the lock, removes registered country operations, state phase, disease, railway, airbase, response-project, and pending-event effects, removes regional entities and the normal-map proof entity, preserves the last valid Air Winter phase and survival ledgers for the historical mapmode, then records `fallout_air_winter_shutdown_complete`. Natural source reservoir and pulse are zeroed. Later contamination deltas are ignored. Existing global Air Cleanliness state modifiers and country pressure ideas are cleared. Treaty operations pause and new membership or invitation surfaces fail their eligibility checks.

Cleaning Day start and delayed-project validity now also check `fallout_air_cleanliness_disabled` directly. A project that was opened before a Fallout request cannot reduce Air Contamination after request-time shutdown, even before the transition lock or host pause pulse is observed.

## Standard state loss proof

The approved loss ladder is `90`, `91`, `92`, `93`, `94`, and `95` in `fallout_population_loss_percent` under `common/script_constants/fallout_world_end_constants.txt`. `fallout_apply_transition_phase_population_loss` iterates every state row that is not current. Each row calls `fallout_apply_state_population_loss`, which calculates a grade-specific request from the frozen pre-transition population and mutates state population through `apply_state_population_loss_without_recruitable_manpower_gain`.

`fallout_reconcile_population_loss_receipt` calculates the observed live loss after the state mutation. It calls `chaos_meter_register_deaths` with `chaos_deaths_reason = fallout_aftermath`, civilian mode enabled, state population application disabled, and the original-owner target. The generation-bound state receipt is the idempotency guard. This proves state deletion and Deaths registration are two parts of one transaction.

Fallout-owned Deaths registration is mandatory even when the general Deaths setting is disabled. The shared registration effect and exact state-loss helper admit the request-time Air shutdown, Fallout transition, active Fallout, and manual scenario flags as an explicit Fallout exception. Non-Fallout population loss remains gated by the general setting. The stored receipt therefore has only zero-loss or registered-loss outcomes for new Fallout transitions.

The shared `air_contamination_update_threshold_flags` effect now refuses to rebuild Air Cleanliness threshold flags or fire ordinary contamination news while `fallout_air_cleanliness_disabled` is set. This closes the stale GUI, terminal-caller, and save-recovery paths after Fallout request intake. Fallout keeps its own blackout presentation and does not reopen the Air Cleanliness threshold surface.

## Manual state loss proof

`fallout_manual_capture_population_baselines` records the pre-strike population for every state before native strike callbacks. `fallout_manual_apply_state_aggregate_consequence` clamps the aggregate direct loss between `fallout_manual_aggregate.death_percent_base = 0.900` and `fallout_manual_aggregate.death_percent_max = 0.950`. It computes the exact requested loss against the captured baseline and supplies the exact state population contract to `apply_exact_state_civilian_population_loss`.

The effect records the applied state delta in `global.fallout_manual_total_civilian_deaths` and `chaos_state_civilian_deaths_total`. `fallout_manual_apply_aggregate_consequences` then calls `chaos_meter_register_deaths` with civilian mode enabled and state population application disabled. This prevents double deletion while retaining the complete manual loss in the Deaths system.

## Engine-sensitive blocker

The source contract proves the state population mutation, the 90 to 95 percent range, and the Deaths receipt. It does not prove the exact engine-native sweep across every valid installed-map province. The manual scenario remains dormant until a live runtime audit proves that native thermonuclear strike effects cover every valid province, complete the batch, and preserve the exact seven-day countdown before the standard blackout and rewrite. No fallback sweep is being claimed.

## Static checks performed

- Removed Fallout public Event Details references were searched in the registry effect, Event Details scripted localisation, and GUI localisation.
- The new consequence boundary spec and this proof record contain no em dash or semicolon.
- Braces were counted in the changed Fallout, Air Winter, treaty, natural-source, registry, and trigger files, including `chaos_meter_effects.txt`. The inspected worktree files are brace-balanced.
