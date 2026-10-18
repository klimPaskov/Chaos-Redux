# Event 021 reusable scripted effects

This file documents the core Event 021 state and registry effects in `021_random_civil_war_effects.txt`.

The core file owns country pressure and authority, target and state reservations, actor admission, front and theater registries, evolution state, bounded global review, settlement, recurrence, scenario bypass, achievement receipts, and cleanup.

The parent transaction in `021_random_civil_war_parent_effects.txt` supplies route-specific planning and commit behavior.

## Scope and conventions

Country-scope effects run on the country whose Event 021 state is being changed.

State-scope effects are called through the `random_civil_war_current_state` variable or a saved state target.

ANY-scope effects that write global arrays are called from a bounded host or from a saved target transaction and never perform an implicit world scan.

All tuning values are read from `common/script_constants/021_random_civil_war_constants.txt`.

## Public effect contracts

`event021_initialize_country_state` initializes hidden pressure, visible authority, recurrence memory, and safe default phase values.

`event021_refresh_country_state` clamps and republishes pressure and authority bands, derives the current phase, and refreshes the dynamic decision and detail text inputs.

`event021_reduce_pressure` consumes `random_civil_war_pending_pressure_delta` in country scope and adds it to the lasting `random_civil_war_pressure_modifier`, clamped to `modifier_minimum` and `modifier_maximum` (-30 to 30), before refreshing the bounded pressure value. This keeps decision, mission, settlement, and reconstruction changes intact when the derived live-country inputs are refreshed.

`event021_decay_pressure_modifier` runs only inside the due branch of `event021_review_current_country` and moves the modifier one `modifier_decay_per_review` step (6) toward zero without crossing it, so relief and strain from earlier actions fade and the pressure band returns to the one its live conditions describe. The settlement's relief enters the modifier once; no separate settlement-relief condition repeats it. Example: a settled government whose actions left the modifier at the -30 floor returns to its condition-driven band after five due reviews, and two prevention actions every 180 days can hold an Exposed country about one band lower but cannot keep the modifier at its floor.

`event021_add_authority` consumes `random_civil_war_pending_authority_delta` in country scope and applies exactly that delta, then clamps State Authority and refreshes its band. It never adds a standing condition, so every tooltip constant equals the change it describes, and without a pending delta it changes nothing.

State Authority conditions change State Authority once per transition. `event021_authority_capital_lost` sets `random_civil_war_capital_lost` and applies `capital_lost` only when the flag is new, and `event021_authority_capital_regained` clears it and applies `capital_secured` only when it was set. `event021_authority_supply_state_lost` and `event021_authority_supply_state_regained` take the temporary input `event021_authority_supply_change` (1 when the caller has just set or cleared one of the per-state flags `random_civil_war_rail_state_lost` or `random_civil_war_front_state_lost`), apply `rail_or_depot_lost` or `supply_secured` once for that change, and keep `random_civil_war_supply_lost` set while any bound supply state is lost.

`event021_clear_authority_conditions` removes every condition flag, the contested-state count, and the recorded crisis capital without changing State Authority. Crisis cleanup, the annexation teardown, and both new-role helpers (`event021_commit_opening_evolution_provenance` and `event021_inherit_crisis_opening_evolution_provenance`) call it, so no condition from an earlier war reaches a later crisis. The Hold the Center capital receipt `random_civil_war_capital_secured` is not an authority condition: only `event021_parent_record_achievement_receipts` writes it, and `event021_begin_achievement_history` clears it when a new crisis begins.

Example: a government at 54 that loses its crisis capital drops to 42 once, however many later actions it takes; retaking the capital raises it by 8 once, and Reconstruct the Administration then adds exactly its 8.

`event021_apply_government_opening_authority` runs inside `event021_random_civil_war_commit_opening` after the achievement history starts: it caps State Authority at `default`, applies the opening-severity loss (`opening_limited_loss` to `opening_critical_loss`), and records the crisis capital through `event021_record_authority_capital`. `event021_apply_claimant_opening_authority` sets a claimant to `claimant_opening` or an Event 006 front to `independence_front_opening` and records its crisis capital. Every claimant initializer calls it.

`event021_authority_review_lost_state` and `event021_authority_review_gained_state` run from `on_state_control_changed` on the old (FROM) and new (ROOT) controller while `event021_authority_follows_control` holds (a live crisis side not yet settled). They read the changed state from `event021_mission_control_changed_state`, apply the capital and bound supply-state transitions, and call `event021_review_held_territory`.

`event021_review_held_territory` compares `num_owned_controlled_states` with `random_civil_war_opening_held_state_count`, stores the shortfall in `random_civil_war_contested_state_count`, applies `territory_state_lost` for each state of change since the last measurement, and refreshes `random_civil_war_contested_territory`, `random_civil_war_key_state_lost` (from `key_territory_states`), and `random_civil_war_capital_supply_risk`. `event021_record_opening_held_states` calls it after every baseline write, so states taken by the opening's own fronts are returned when the baseline is recorded again. `event021_review_crisis_conditions` runs from the bounded country review: it records a missing baseline, re-measures territory, and ends an intervention that is no longer live.

`event021_authority_foreign_intervention_started` (input event target `event021_foreign_sponsor`) records the sponsor in `random_civil_war_foreign_sponsor_scope` and applies `foreign_intervention` once while `random_civil_war_foreign_intervention_active` is set; `event021_end_foreign_intervention` clears it without a change. `event021_authority_talks_opened` applies `negotiation` once per crisis role when a neighbour's mediation first reaches the government. `event021_apply_settlement_outcome_authority` runs inside `event021_apply_settlement`: `victory` for the side whose war aims prevailed, `defeat` for a government that lost the war or territory to the settlement, nothing for a negotiated settlement, and it ends the territory and capital-risk conditions.

`event021_update_authority_band` and `event021_update_pressure_band` convert the current values into the stable band variables used by triggers and localisation.

`event021_random_civil_war_prepare_target` computes the live target weight and clears it to the minimum when the candidate is invalid. A proven route is enough for pre-commit target selection because ordinary opposition actors are created by the validated opening transaction. The opening validator still has to prove the final leader, force, capital, and Event 006 package contract.

`event021_prepare_archetype_weights` publishes the six route weights used by the parent random-list selection.

`event021_prepare_opening_severity` derives a limited, serious, severe, or critical opening from current pressure, authority, occupation, war, and administration evidence.

`event021_reserve_target`, `event021_reserve_state`, and `event021_begin_opening_transaction` establish idempotent global and country reservations before mutations.

`event021_record_anchor_state` and `event021_prepare_parent_remnant` preserve the opening capital, anchor, and protected remnant information.

`event021_prepare_force_package` computes the bounded manpower in thousands, division, equipment envelope, and opening size consumed by the parent civil-war adapter. Its normal manpower input is `random_civil_war_requested_force_manpower_k`, which uses the same unit as `manpower_k`. It clears the previous ready/invalid receipts before every computation so a rejected package cannot inherit stale validation.

`event021_random_civil_war_commit_opening` is the core commit boundary and publishes active theater state only after the parent plan has passed validation.

`event021_rollback_opening` clears the target transaction without leaving an actor, front, or partial transfer.

`event021_register_active_theater`, `event021_unregister_active_theater`, `event021_register_front`, `event021_unregister_front`, `event021_set_priority_front`, and `event021_clear_priority_front` maintain bounded global theater and front registries.
`event021_register_front` appends the host, anchor/capital, generation, crisis, archetype, route source, Event 006 package, region count, goal, status, settlement, and registration date alongside every core front row.
`event021_unregister_front` removes those aligned rows by front ID and falls back to actor/anchor removal when a legacy row is missing, so old saves cannot leave metadata attached to a different front.
`event021_bind_front_plan_row` matches a live front id to the aligned pre-commit plan, copies its row metadata to the actor, and updates the row status.
`event021_bind_current_front_plan_row` is the idempotent consumed-status wrapper used by registration, priority selection, and secondary closure.
`event021_bind_front_plan_row` clears and rewrites the bound receipt only when a plan is published, so a later priority decision keeps the row binding made at registration; during an Evolution I review commit it binds through `event021_bind_active_front_row` instead.
`event021_set_priority_front` uses the chain-local `random_civil_war_anchor_state` target that opening chains save, and writes `random_civil_war_priority_front_state` and its id to the country it runs on, not to the chain ROOT, so every side initialized in one opening or Evolution I review keeps its own priority front and an opposition side can use Seize an Opposition Depot on its own anchor. A decision has no such target, so the setter first calls `event021_resolve_priority_front_target`, which picks the taker's own anchor, the shared opening anchor, its capital, or the first held state of its current front, each checked by `event021_priority_front_state_candidate`. The Set the Priority Front decision gates its availability on the same `event021_priority_front_target_valid` trigger, so its command-power cost is never paid without a target, and its tooltip names the chosen state through `event021_GetPriorityFrontCandidateName`.
`event021_reject_pending_front_plan_row` marks a frozen optional row rejected when its bounded starter rolls back, preventing the resolution review from waiting on a front that never materialised.

`event021_prepare_event6_admission`, `event021_confirm_event6_identity`, `event021_record_event6_origin`, and `event021_apply_event6_origin_adapter` carry the Event 006 admission and origin receipt without mutating Event 006 lifecycle state.

`event021_prepare_same_tag_route`, `event021_cleanup_same_tag_route`, `event021_apply_regional_exposure`, `event021_advance_regional_exposure`, `event021_cleanup_regional_exposure`, `event021_clear_received_sponsor_commitment_receipt`, and `event021_clear_sponsor_commitment_receipt` own same-tag and neighboring exposure state. Same-tag cleanup also removes the route and all-island receipts so a resolved contest cannot seed a later target review. Sponsor recording stores the actual redirected recipient scope on the sponsor, and exposure cleanup clears that recipient through the recipient-only helper plus the source-side and exposed-neighbour receipts before dropping the source pointer; durable settlement and achievement receipts are preserved.
`event021_apply_regional_exposure` publishes both the durable exposure marker and the `random_civil_war_neighbor_exposure` presentation marker, so the category, decision, and AI surfaces follow the same live state. `event021_parent_review_exposure_lifecycle` runs from the bounded registered-country review and calls cleanup when the source crisis is no longer usable; cleanup removes both markers, route and role receipts, separate relief/support action state, and the saved source pointer before applying the centralized cooldown.

`event021_sync_evolution_state` publishes the current stage and the three evolution unlock flags from the Chaos tier.

Stages switched off in the Events Log settings are handled by the parent scheduler, which never samples, fires, or records them; see `021_random_civil_war_parent_effects.md`.

`event021_prepare_evolution_log_context`, `event021_apply_evolution_i`, `event021_apply_evolution_ii`, and `event021_apply_evolution_iii` own the reusable evolution flags and threat-source state.
Each apply effect switches on only its own stage, so a later stage never activates the mechanics of an earlier stage that is switched off.
Before calling `event021_prepare_evolution_log_context`, preinitialize the temporary event ID and type outputs in the caller so their assignments survive return.
Preinitialize stage and tier as well if consuming those helper outputs rather than replacing them with the callback's explicit stage and tier.
The three parent callbacks preserve the event ID and type outputs, then select a verified live actor through `event021_select_verified_evolution_log_actor` immediately before the shared recorder, as documented in `021_random_civil_war_evolution_log_effects.md`.

`event021_schedule_country_review`, `event021_refresh_global_capacity`, `event021_register_global_country`, `event021_unregister_global_country`, `event021_refresh_target_pool_membership`, `event021_global_review_batch`, `event021_review_current_country`, `event021_finish_global_review_batch`, `event021_queue_critical_country`, `event021_dequeue_critical_country`, `event021_launch_critical_country`, and `event021_finish_critical_launch` implement the bounded review and Critical queue contract. Registered and Critical removals conservatively rewind their cursors by one row so a shifted successor is never skipped until wrap; a repeated bounded row is acceptable. Critical admission uses a centralized batch budget.

`event021_handle_annexed_country` is the narrow `on_annex` lifecycle callback documented in `021_random_civil_war_lifecycle_effects.md`.
It removes the disappearing country's own memberships and rebinds surviving host-linked front/theater records only after explicit same-crisis successor proof; unrelated annexation uses teardown.
Scope rebinding is not proof that the engine transferred actual wars.

`event021_apply_settlement` records terms and starts finite reconstruction. After reconstruction and settlement obligations are complete, `event021_prepare_recurrence` scores the durable outcome and schedules a bounded post-cooldown review window; `event021_reconstruction_tick` applies the interim recovery changes.
`event021_apply_settlement_aftermath` gives the settled country the aftermath idea of its settlement family, and `event021_clear_settlement_aftermath` removes every aftermath idea. A battlefield government victory instead waits for one of `event021_postwar_direction_amnesty`, `_reform`, `_harsh`, or `_emergency`, called from The Fighting Stops, each of which adds its idea, changes State Authority, and records the deferred achievement receipts through `event021_finish_postwar_direction`. Only the harsh and emergency directions set the harsh and failed settlement flags. `event021_resolve_pending_postwar_direction` applies the profile default when the direction is still pending at the end of reconstruction.
`event021_prepare_recurrence` adds `tolerate_recurrence_pressure` for a tolerated strange incident and `terms_upheld_recurrence_relief` for a settlement upheld through Hold the Settlement Terms.

`event021_update_achievement_state` writes achievement receipts only when normal-campaign eligibility remains true.

`event021_prepare_scenario_bypass` and `event021_clear_scenario_bypass` isolate manual scenario origin from ordinary automatic pacing. The parent controller keeps the bypass and confirmation reservation alive across the complete selected-set preparation and commit phases, then clears it after the final callback.

`event021_queue_critical_country` and `event021_dequeue_critical_country` keep the Critical queue row aligned with the country receipt, and the scheduler removes stale or recovered rows. The scheduler does not dispatch a new civil war from the Critical queue, and no `chaosx.nr21.18` callback exists. `event021_launch_critical_country` and `event021_finish_critical_launch` are dormant compatibility helpers with no caller.

`event021_cleanup_crisis`, `event021_cleanup_global_registry`, and `event021_clear_global_threat_source` remove temporary state after a completed or rejected transaction. Crisis cleanup first recovers an interrupted Event 006 adapter transaction: an adapter that already recorded both completion receipts only loses its Event 021 transaction marker, while an incomplete preparation invokes the parent-owned generation reset and restores the carrier's prior Event 021 generation. Both branches clear the preparation and package-ready bridge flags. Crisis cleanup also clears every transient Event 021 AI role profile so settled or rejected actors cannot retain crisis behavior. Decision-state cleanup clears the priority-front mirror and rail receipt, while global cleanup clears the persistence carrier. Clearing the Evolution III threat also empties the Critical queue, removes its country receipts, and resets its cursor and count.

Ordinary crisis cleanup preserves the completion and identity receipts of a living, fully proven Event 021-origin Event 006 package, using `is_independence_wave_event021_package_country`.
That predicate extracts the existing complete-adapter branch from `is_independence_wave_package_content_active` without widening the strict Event 006 active-origin classifier.
Its required inputs are the four completed/setup-proven/origin-recorded/origin-adapter-complete receipts, package ID, existence, and non-active/non-ended Event 006 origin; it has no side effects or default admission.
Incomplete actors still lose partial completion receipts, and actual annexation/formable absorption retain their separate teardown path.
This keeps package-local predicates alive after reconstruction without marking Event 006 fired, changing its accounting, or enabling league participation.
Example: a recognized Event 021-created package survives reconstruction with package content active and `is_independence_wave_active_country = no`.
The shared Event 006 local-content and player-surface predicates now accept this complete Event 021-origin package, so its reused focus, category, decision, formable, and AI surfaces remain available after setup without changing Event 006 lifecycle state.
That source bridge still requires live package/runtime validation for every admitted package and does not certify save/reload, settlement, or player-facing consumer behavior.

`event021_review_current_country` removes a recovered queued country before re-evaluating Critical admission, routes an invalid registered country through `event021_dequeue_critical_country` before `event021_unregister_global_country`, and the parent queue pass repeats that validity check, keeping the Critical queue array, country receipt, and count aligned.

`event021_register_fracture_evidence` stores regional, command, and Event 006 actor/package/region identity in source-specific receipts. Callers may provide the normal scope input `event021_evidence_actor_scope`; refresh invalidates the source receipt if that referenced actor no longer exists. Settlement completion produces its own finite settlement receipt, and all receipt families expire through the shared refresh helper.

## Side-effect rules

The effects do not create an actual nonhuman country, duplicate an Event 006 tag or character, or enroll an Event 006 package in league systems.

The global arrays are capacity bounded by `random_civil_war_capacity` and are cleared only when their registered scopes are no longer valid.

The explicit manual scenario request may enumerate eligible countries once to build Low, Medium, and High target pools, while Maximum selects every eligible country directly. Selection and host-bound plan preparation complete before the immediate commit pass; ordinary and recurring review paths never use `every_country`.

## Example

An ordinary parent call prepares a target, reserves it, plans connected states, calls `event021_prepare_force_package`, validates the plan, and then calls the appropriate parent commit adapter.

The parent passes `random_civil_war_opening_size`, `random_civil_war_opening_army_ratio`, `random_civil_war_opening_navy_ratio`, and `random_civil_war_opening_air_ratio` to the vanilla civil-war adapter.

## Active receipt routing

`event021_bind_front_plan_row` and `event021_reject_pending_front_plan_row` remain COUNTRY-scoped consumers of caller-owned `event021_planned_front_id_to_mark`; binding also consumes `event021_planned_front_status_to_mark`.
While the active commit lock is held, they use only the reviewing government's receipt through the proved global owner target.
A missing active owner fails closed without falling through to a global opening plan.
Outside an active commit the existing global opening-row behavior remains unchanged.
Binding writes the taker's normal bound-row metadata and the matching owner row status; rejection changes only that owner row's status and creates no actor or resource effect.
The routing fixtures prove a ready outer opening plan with the same row ID remains untouched by active binding and rejection.
