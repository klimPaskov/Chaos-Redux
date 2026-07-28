# Fallout consequence boundary and Deaths proof

## Scope

This record covers the accepted correction that Fallout is a consequence transition rather than a normal event, Event Details row, evolution, or ordinary super-event. It also records the Air Cleanliness shutdown and the state population loss routing.

## Public registration proof

Static source inspection shows that `initialize_world_end_scenario_registry` in `common/scripted_effects/chaosx_events_log_effects.txt` registers the public world-end rows without Fallout. No Fallout title, owner, or details branch remains in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`. The Fallout-specific Event Details card preparation hooks were removed from the registry refresh, detail open, and toggle paths.

The stable settings-ledger value `fallout_consequence_id.settings_ledger = 2` lives in `common/script_constants/fallout_world_end_constants.txt`. It is used only by internal request and settings gates and is not inserted into the public registry. The generic `GetWorldEndScenario` selector resolves Fallout to `chaos_tier_end_fallout` without exposing a Fallout title. The Chaos Meter uses consequence-neutral terminal wording, while the world-end tooltip selects the same consequence label. The dedicated blackout GUI uses its own sequential display text. Fallout blackout audio remains owned by `fallout_dispatch_blackout_audio` in `common/scripted_effects/fallout_world_end_effects.txt`.

Fallout post-consequence survivor chains still use normal country events and their own event history. This is intentional. Those are ordinary survivor stories after the consequence and are not a registration of the consequence itself.

## Air Cleanliness shutdown proof

The standard path sets `fallout_air_cleanliness_disabled` in `fallout_queue_request_envelope` as soon as the request is admitted, records temporary ownership in `fallout_air_cleanliness_request_paused`, and closes the host-reconciliation gap before `fallout_lock_transition` runs. The Air request trigger accepts the durable flag only while this temporary admission marker is present, so recording shutdown ownership cannot make a valid 100 percent request reject itself. The lock keeps the durable flag after `fallout_snapshot_epoch_is_ready_to_lock` succeeds, clears the temporary ownership flag, and calls `air_contamination_apply_state_modifier` so existing country pressure ideas and state modifiers do not linger until the next monthly pass. A rejected pending envelope clears the temporary ownership and restores the ordinary modifier surface. `fallout_world_end_migrate_save` restores the flag and performs the same immediate modifier cleanup for saves with `world_end_fallout`. The manual path sets the flag in `fallout_manual_initialize_sweep` after intensity validation and clears current modifiers before native strikes. It refreshes the stored contamination display after the sweep without running the generic threshold-news updater. A failure after a valid sweep has been admitted leaves the durable Air shutdown in place, even if the native sweep later enters the dormant error state.

The host manual reconciliation repairs the same durable flag when a save resumes with an admitted manual transaction. The repair accepts only an active sweep, synthetic strike batch, completed native sweep, seven-day countdown, sent request, or current launcher receipt. An invalid-intensity error has none of those admission receipts and therefore does not acquire the shutdown through recovery.

Static consumers of the flag are:

- `air_winter_system_enabled` and `air_winter_event_targets_are_valid` in `common/scripted_triggers/air_cleanliness_winter_triggers.txt`.
- `air_winter_response_target_is_valid` in `common/scripted_triggers/air_cleanliness_winter_triggers.txt`, which rejects already-open terminal response events after request-time shutdown.
- `air_winter_response_mutation_is_allowed` in the same trigger file, consumed by every timed Air Winter decision removal callback so a same-day expiry releases rather than applies a result after request-time shutdown.
- `air_winter_response_controlled_evacuation_project_is_valid` and `air_winter_response_final_evacuation_project_is_valid` in the same trigger file, which reject delayed population transfers after request-time shutdown.
- `air_winter_event_apply_deaths` in `common/scripted_effects/air_cleanliness_winter_event_effects.txt`.
- `air_winter_apply_phase_modifier`, `air_winter_update_building_damage`, `air_winter_apply_state_population_loss`, and `air_winter_apply_disease_modifier` in `common/scripted_effects/air_cleanliness_winter_effects.txt`, which also fail closed when called outside the monthly coordinator.
- `air_contamination_monthly_update` in `common/scripted_effects/chaos_meter_effects.txt`.
- `air_contamination_apply_delta_bp` and `air_contamination_apply_state_modifier` in `common/scripted_effects/chaos_meter_effects.txt`.
- Natural wildfire, volcanic, and ashfall source registration in `common/scripted_effects/air_cleanliness_natural_source_effects.txt`.
- Treaty membership, invitation, decision, and host lifecycle surfaces in the Air Cleanliness treaty files.
- The Air Cleanliness settings checkbox and exported settings row.

The monthly pass no longer starts or updates Air Winter after the flag. `air_winter_suspend_all_states_for_fallout` runs once at the lock, removes registered country operations, state phase, disease, railway, airbase, response-project, and pending-event effects, removes the Air-owned global, nuclear fallout, chemical contamination, and thermonuclear modifiers that could feed the daily contamination or deaths pulse, removes regional entities and the normal-map proof entity, preserves the last valid Air Winter phase and survival ledgers for the historical mapmode, then records `fallout_air_winter_shutdown_complete`. Natural source reservoir and pulse are zeroed. Later contamination deltas are ignored. Existing global Air Cleanliness state modifiers and country pressure ideas are cleared. Treaty operations pause, late treaty violation callbacks fail closed, and new membership or invitation surfaces fail their eligibility checks.

Cleaning Day start and delayed-project validity now also check `fallout_air_cleanliness_disabled` directly. A project that was opened before a Fallout request cannot reduce Air Contamination after request-time shutdown, even before the transition lock or host pause pulse is observed. The Final Silence contamination setter has the same fail-closed guard, so a stale predecessor callback cannot restore Air pressure after Fallout owns the boundary.

Pending Air Winter terminal responses use the same durable guard. Abandonment and decontamination result events therefore fall into their stale-choice recovery path after request admission instead of changing state ledgers, country effects, or population loss.

The controlled and final evacuation completion validators also fail closed after request admission. A paid project can therefore cancel or become stale, but it cannot transfer population or refugee pressure after Fallout owns the Air boundary.

The Final Silence handoff trigger rejects the same durable flag, so a predecessor cannot reopen the Air coordinator after Fallout request admission.

## Standard state loss proof

The approved loss ladder is `90`, `91`, `92`, `93`, `94`, and `95` in `fallout_population_loss_percent` under `common/script_constants/fallout_world_end_constants.txt`. `fallout_apply_transition_phase_population_loss` iterates every state row that is not current. Each row calls `fallout_apply_state_population_loss`, which calculates a grade-specific request from the frozen pre-transition population and mutates state population through `apply_state_population_loss_without_recruitable_manpower_gain`.

`fallout_reconcile_population_loss_receipt` calculates the observed live loss after the state mutation. It calls `chaos_meter_register_deaths` with `chaos_deaths_reason = fallout_aftermath`, civilian mode enabled, state population application disabled, and the original-owner target. The generation-bound state receipt is the idempotency guard. This proves state deletion and Deaths registration are two parts of one transaction.

Fallout-owned Deaths registration is mandatory even when the general Deaths setting is disabled. The shared registration effect and exact state-loss helper admit the request-time Air shutdown, Fallout transition, active Fallout, and manual scenario flags as an explicit Fallout exception. Non-Fallout population loss remains gated by the general setting. The stored receipt therefore has only zero-loss or registered-loss outcomes for new Fallout transitions.

The shared `air_contamination_update_threshold_flags` effect now refuses to rebuild Air Cleanliness threshold flags or fire ordinary contamination news while `fallout_air_cleanliness_disabled` is set. This closes the stale GUI, terminal-caller, and save-recovery paths after Fallout request intake. Fallout keeps its own blackout presentation and does not reopen the Air Cleanliness threshold surface.

The Black Plague source refresh now follows the same durable boundary. Once Fallout owns the Air shutdown, the refresh clears its natural-source reservoir and previous contribution instead of reintroducing disease-derived Air Contamination during a later disease pulse.

Late nuclear callbacks also consume the boundary. Ordinary nuke-drop handling, Final Silence fallout helpers, and the Air Winter reactor-failure helper do not add `nuclear_fallout_state` after `fallout_air_cleanliness_disabled`. The ordinary nuke callback removes a stale modifier before it could feed the disabled Air source.

The daily contamination and outbreak Deaths pulse now rejects `nuclear_fallout_state` while the durable Air shutdown is set and removes a stale copy instead of registering another nuclear loss. Chemical contamination remains an independent CBRN surface and is not disabled by this Air-only guard.

## Manual state loss proof

`fallout_manual_capture_population_baselines` records the pre-strike population for every state before native strike callbacks. `fallout_manual_apply_state_aggregate_consequence` clamps the aggregate direct loss between `fallout_manual_aggregate.death_percent_base = 0.900` and `fallout_manual_aggregate.death_percent_max = 0.950`. It computes the exact requested loss against the captured baseline and supplies the exact state population contract to `apply_exact_state_civilian_population_loss`.

The state provenance receipt then measures the complete pre-strike-to-post-strike loss after native strike callbacks and the exact reconciliation. It records that observed total in `global.fallout_manual_total_civilian_deaths` and `chaos_state_civilian_deaths_total`. `fallout_manual_apply_aggregate_consequences` calls `chaos_meter_register_deaths` with civilian mode enabled and state population application disabled. This prevents double deletion while retaining the complete observed manual loss in the Deaths system rather than only the direct mod adjustment.

After each state records its synthetic Fallout intensity and expiry ledger, `fallout_manual_apply_state_aggregate_consequence` removes the ordinary `nuclear_fallout_state` modifier. This keeps a native strike's daily nuclear contamination and Deaths source from surviving past the durable Air Cleanliness shutdown.

## Engine-sensitive blocker

The source contract proves the state population mutation, the 90 to 95 percent target band, and the reconciled Deaths receipt. The vanilla documentation describes `launch_nuke` inputs but does not specify whether the built-in strike callback changes population or invokes this mod's Deaths ledger. The receipt therefore measures the observed final loss and submits it once, while runtime review must still confirm that the native callback does not separately write a duplicate mod Deaths entry. The source also does not prove the exact engine-native sweep across every valid installed-map province. The manual scenario remains dormant until a live runtime audit proves that native thermonuclear strike effects cover every valid province, complete the batch, and preserve the exact seven-day countdown before the standard blackout and rewrite. No fallback sweep is being claimed.

## Static checks performed

- Removed Fallout public Event Details references were searched in the registry effect, Event Details scripted localisation, and GUI localisation.
- The new consequence boundary spec and this proof record contain no em dash or semicolon.
- Braces were counted in the changed Fallout, Air Winter, treaty, natural-source, registry, and trigger files, including `chaos_meter_effects.txt`. The inspected worktree files are brace-balanced.
