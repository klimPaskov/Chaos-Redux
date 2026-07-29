# Fallout consequence boundary and Deaths proof

## Scope

This record covers the accepted correction that Fallout is a consequence transition rather than a normal event, ordinary Event Log row, evolution, or ordinary super-event. Fallout replaces the retired Final Silence world-end selector row. It also records the permanent 99 percent Air Contamination lock and the state population loss routing.

## Public registration proof

The ordinary super-event GUI now rejects `world_end_fallout` in its visibility trigger. A prior generic overlay therefore cannot remain visible over the Fallout-owned full-screen blackout. The dedicated blackout GUI and dramatic audio are the only transition presentation surfaces.

Static source inspection shows that `initialize_world_end_scenario_registry` in `common/scripted_effects/chaosx_events_log_effects.txt` registers Fallout as the appended replacement for the retired Final Silence world-end row. Fallout has no ordinary Event Log row or evolution branch. The Fallout-specific ordinary Event Details card preparation hooks remain absent from the registry refresh, detail open, and toggle paths.

The stable settings-ledger value `fallout_consequence_id.settings_ledger = 2` lives in `common/script_constants/fallout_world_end_constants.txt`. The world-end selector uses appended Fallout id 13, while ordinary Event Log and evolution registries remain untouched. The dedicated blackout GUI uses its own sequential display text. Fallout blackout audio remains owned by `fallout_dispatch_blackout_audio` in `common/scripted_effects/fallout_world_end_effects.txt`.

The separate manual sandbox launch surface uses raw triggerable-scenario id 14, the next live id after 13. It is not an ordinary Fallout Event Log row, evolution, Event Details card, or ordinary super-event and remains launch-gated by the exact native province-sweep proof.

Fallout post-consequence survivor chains still use normal country events and their own event history. This is intentional. Those are ordinary survivor stories after the consequence and are not a registration of the consequence itself.

## Permanent Air Contamination proof

The standard path sets `fallout_air_contamination_permanent_99` through the idempotent Fallout-owned lock after request admission and records temporary ownership in `fallout_air_cleanliness_request_paused` before admission. The lock writes exactly 9,900 basis points, assigns all 9,900 basis points to `global.air_contamination_fallout_bp`, zeros chemical, biological, natural, decay, and last-delta inputs, and clears both temporary pause markers. The permanent flag and the 9,900 value are authoritative. After the snapshot is ready, `fallout_lock_transition` calls `fallout_lock_air_cleanliness_after_fallout_admission`, which delegates to that permanent lock and closes treaty operations before blackout scheduling. A rejected pending envelope clears only the temporary ownership and restores the ordinary modifier surface. `fallout_world_end_migrate_save` calls the same permanent lock for saves with `world_end_fallout`. The manual path calls it after intensity validation and after the prestrike population ledger is frozen, before native strikes. A failure after a valid sweep has been admitted leaves the 99 percent lock in place, even if the native sweep later enters the dormant error state.

Startup reconstruction also re-enters the same idempotent lock when the permanent Fallout flag is already present. This rebuilds the 9,900 basis-point read model and prevents a stale zero-percent display from replacing the saved 99 percent state.

The manual population replay measures the live `state_population_k` after native strike callbacks and the exact aggregate consequence. The standard population phase therefore requests only the remaining delta to the frozen 90 to 95 percent survivor target. A state that already reached its target requests zero, and its reconciliation receipt cannot register a second Fallout Deaths row. The frozen `fallout_pretransition_population_k` remains provenance and is not reused as a second live loss input.

The population receipt gate now authenticates that manual replay baseline against the generation-bound preflight `fallout_manual_population_contract_preflight_frozen_current_people` value. Ordinary Fallout rows continue to require the frozen pretransition baseline. This keeps the manual exception narrow and prevents a stale or unproven replay from passing as a normal population receipt.

The host manual reconciliation repairs the same durable flag when a save resumes with an admitted manual transaction. The repair accepts only an active sweep, synthetic strike batch, completed native sweep, seven-day countdown, sent request, or current launcher receipt. An invalid-intensity error has none of those admission receipts and therefore does not acquire the shutdown through recovery.

Save reconciliation retires any stale active `world_end_final_silence` and `world_end_final_silence_thermonuclear` runtime flags before queuing the same Fallout request. The completed Final Silence cause-memory flag remains intact, while old wave callbacks lose their active trigger. A save already marked `world_end_fallout` receives the same legacy-flag cleanup without clearing the Fallout world-end flag.

After the locked snapshot is ready, `fallout_stop_old_world_wars_at_admission` settles exiles, volunteers, civil-war targets, and all active wars before the blackout is exposed. Its generation-bound receipt is separate from `fallout_reset_old_world_diplomacy`, which still owns subjects, access, markets, trade, intelligence, and exhaustive map-return validation.

Static consumers of the flag are:

- `air_contamination_monthly_update`, `air_contamination_apply_delta_bp`, and `air_contamination_apply_state_modifier` in `common/scripted_effects/chaos_meter_effects.txt`.
- Chemical and biological Air contribution update, clear, and rebuild helpers.
- Natural wildfire, volcanic, ashfall, and Black Plague source registration.
- `air_winter_system_enabled` in `common/scripted_triggers/air_cleanliness_winter_triggers.txt`, where the permanent flag overrides a disabled pre-Fallout player setting.
- Treaty membership, invitation, decision, and host lifecycle surfaces in the Air Cleanliness treaty files.
- The Air Cleanliness settings checkbox and exported settings row. The scripted GUI click trigger rejects `fallout_air_contamination_permanent_99`, so the post-Fallout value is visibly non-toggleable.

The monthly pass pauses Air Winter while `fallout_transition_active` owns the frozen transition snapshot. It does not clear the Air Winter state ledger or regional normal-map entities as a permanent shutdown. After the transition flag clears, the same host-owned monthly pass resumes phase calculation, survival ledgers, building damage, state-category degradation, supply, military effects, disease, Deaths, mapmode data, and regional ordinary-map visuals against the fixed 9,900-basis-point atmosphere. The global Air Cleanliness state modifier and country pressure ideas also remain active at their fixed-value tiers. Treaty operations remain paused because Fallout owns that diplomatic system.

Cleaning Day and other ordinary reduction routes cannot change the permanent value because every delta delegates back to `fallout_enforce_permanent_air_contamination`. Retired Final Silence callbacks cannot replace the Fallout owner.

## Standard state loss proof

The approved loss ladder is `90`, `91`, `92`, `93`, `94`, and `95` in `fallout_population_loss_percent` under `common/script_constants/fallout_world_end_constants.txt`. `fallout_apply_transition_phase_population_loss` iterates every state row that is not current. Each row calls `fallout_apply_state_population_loss`, which calculates a grade-specific request from the frozen pre-transition population and mutates state population through `apply_state_population_loss_without_recruitable_manpower_gain`.

`fallout_reconcile_population_loss_receipt` calculates the observed live loss after the state mutation. It calls `chaos_meter_register_deaths` with `chaos_deaths_reason = fallout_aftermath`, civilian mode enabled, state population application disabled, and the original-owner target. The generation-bound state receipt is the idempotency guard. This proves state deletion and Deaths registration are two parts of one transaction.

Fallout-owned Deaths registration is mandatory even when the general Deaths setting is disabled. The shared registration effect and exact state-loss helper admit the request-time Air pause, Fallout transition, active Fallout, and manual scenario flags as an explicit Fallout exception. Non-Fallout population loss remains gated by the general setting. The stored receipt therefore has only zero-loss or registered-loss outcomes for new Fallout transitions.

The shared `air_contamination_update_threshold_flags` effect retains historical threshold flags but suppresses ordinary contamination news while `fallout_air_contamination_permanent_99` is set. This closes the stale GUI, terminal-caller, and save-recovery mutation paths after Fallout request intake. Fallout keeps its own blackout presentation and does not reopen the Air Cleanliness threshold surface.

The Black Plague source refresh follows the same durable boundary. Once Fallout owns the fixed source, the refresh clears its natural-source reservoir and previous contribution instead of reintroducing disease-derived Air Contamination during a later disease pulse.

Late source callbacks also consume the boundary. Ordinary nuke-drop handling and the Air Winter reactor-failure helper cannot change the fixed global value after `fallout_air_contamination_permanent_99`.

Chemical contamination remains an independent CBRN state surface, but its global Air contribution cannot change the fixed Fallout source.

Natural disaster input is deliberately small before Fallout. Regional wildfire smoke adds `0.10 bp`, rising only to `0.20 bp` at catastrophic and `0.35 bp` at abnormal severity. The largest volcanic or massive-eruption single impact is `1.25 bp`, while settled-ash aftermath peaks at `0.25 bp`. Every natural-source receipt is clamped through the shared `4 bp` monthly reservoir ceiling, equal to `0.04 percent`, and every source returns zero after the permanent lock.

## Manual state loss proof

`fallout_manual_capture_population_baselines` records the pre-strike population for every state before native strike callbacks. `fallout_manual_apply_state_aggregate_consequence` clamps the aggregate direct loss between `fallout_manual_aggregate.death_percent_base = 0.900` and `fallout_manual_aggregate.death_percent_max = 0.950`. It computes the exact requested loss against the captured baseline and supplies the exact state population contract to `apply_exact_state_civilian_population_loss`.

The state provenance receipt then measures the complete pre-strike-to-post-strike loss after native strike callbacks and the exact reconciliation. It records that observed total in `global.fallout_manual_total_civilian_deaths` and `chaos_state_civilian_deaths_total`. `fallout_manual_apply_aggregate_consequences` calls `chaos_meter_register_deaths` with civilian mode enabled and state population application disabled. This prevents double deletion while retaining the complete observed manual loss in the Deaths system rather than only the direct mod adjustment.

After each state records its synthetic Fallout intensity and expiry ledger, `fallout_manual_apply_state_aggregate_consequence` removes the ordinary `nuclear_fallout_state` modifier. This prevents a native strike's daily nuclear contamination and Deaths source from duplicating the permanent Fallout source.

## Engine-sensitive blocker

The source contract proves the state population mutation, the 90 to 95 percent target band, and the reconciled Deaths receipt. The vanilla documentation describes `launch_nuke` inputs but does not prove the exact engine-native sweep across every valid installed-map province. The manual scenario remains dormant behind its static proof gate because no verified native all-province sweep surface has been found. No fallback sweep is being claimed. Live playtesting remains a later user validation handoff and is not a completion condition for the static core-mechanics tranche.

## Static checks performed

- Removed Fallout public Event Details references were searched in the registry effect, Event Details scripted localisation, and GUI localisation.
- The new consequence boundary spec and this proof record contain no em dash or semicolon.
- Braces were counted in the changed Fallout, Air Winter, treaty, natural-source, registry, and trigger files, including `chaos_meter_effects.txt`. The inspected worktree files are brace-balanced.
