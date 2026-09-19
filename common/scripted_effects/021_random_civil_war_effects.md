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

`event021_reduce_pressure` consumes `random_civil_war_pending_pressure_delta` in country scope and adds it to the persistent `random_civil_war_pressure_modifier` before refreshing the bounded pressure value. This keeps decision, mission, settlement, and reconstruction changes intact when the derived live-country inputs are refreshed.

`event021_add_authority` consumes `random_civil_war_pending_authority_delta` in country scope and applies a bounded authority change.

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

`event021_prepare_event6_admission`, `event021_confirm_event6_identity`, `event021_record_event6_origin`, and `event021_apply_event6_origin_adapter` carry the Event 006 admission and origin receipt without mutating Event 006 lifecycle state.

`event021_prepare_same_tag_route`, `event021_cleanup_same_tag_route`, `event021_apply_regional_exposure`, `event021_advance_regional_exposure`, and `event021_cleanup_regional_exposure` own same-tag and neighboring exposure state. Same-tag cleanup also removes the route and all-island receipts so a resolved contest cannot seed a later target review.
`event021_apply_regional_exposure` publishes both the durable exposure marker and the `random_civil_war_neighbor_exposure` presentation marker, so the category, decision, and AI surfaces follow the same live state and cleanup removes both markers together.

`event021_sync_evolution_state` publishes the three evolution stages and invokes disabled-evolution safety.

`event021_apply_disabled_evolution_safety` withdraws active consumers for explicitly disabled stages while leaving history flags intact.

`event021_prepare_evolution_log_context`, `event021_apply_evolution_i`, `event021_apply_evolution_ii`, and `event021_apply_evolution_iii` own the reusable evolution flags and threat-source state.

`event021_schedule_country_review`, `event021_refresh_global_capacity`, `event021_register_global_country`, `event021_unregister_global_country`, `event021_refresh_target_pool_membership`, `event021_global_review_batch`, `event021_review_current_country`, `event021_finish_global_review_batch`, `event021_queue_critical_country`, `event021_dequeue_critical_country`, `event021_launch_critical_country`, and `event021_finish_critical_launch` implement the bounded review and Critical queue contract. Registered and Critical removals conservatively rewind their cursors by one row so a shifted successor is never skipped until wrap; a repeated bounded row is acceptable. Critical admission and launch use separate centralized batch budgets.

`event021_handle_annexed_country` is the narrow `on_annex` lifecycle callback documented in `021_random_civil_war_lifecycle_effects.md`.
It removes the disappearing country's own memberships and rebinds surviving host-linked front/theater records only after explicit same-crisis successor proof; unrelated annexation uses teardown.
Scope rebinding is not proof that the engine transferred actual wars.

`event021_apply_settlement`, `event021_prepare_recurrence`, and `event021_reconstruction_tick` move a completed theater through terms, recurrence memory, and finite reconstruction.

`event021_update_achievement_state` writes achievement receipts only when normal-campaign eligibility remains true.

`event021_prepare_scenario_bypass` and `event021_clear_scenario_bypass` isolate manual scenario origin from ordinary automatic pacing. The parent controller keeps the bypass and confirmation reservation alive across the complete selected-set preparation and commit phases, then clears it after the final callback.

`event021_queue_critical_country`, `event021_dequeue_critical_country`, `event021_launch_critical_country`, and `event021_finish_critical_launch` keep the Critical queue row aligned while a claimed target is dispatched through `chaosx.nr21.18`. Queue exits are centralized as launched, stabilized, or invalidated receipts; a still-valid Critical target is retained for a later bounded launch budget.

`event021_cleanup_crisis`, `event021_cleanup_global_registry`, and `event021_clear_global_threat_source` remove temporary state after a completed or rejected transaction. Crisis cleanup also clears every transient Event 021 AI role profile so settled or rejected actors cannot retain crisis behavior. Clearing the Evolution III threat also empties the Critical queue, removes its country receipts, and resets its cursor and count.

Ordinary crisis cleanup preserves the completion and identity receipts of a living, fully proven Event 021-origin Event 006 package, using `is_independence_wave_event021_package_country`.
That predicate extracts the existing complete-adapter branch from `is_independence_wave_package_content_active` without widening the strict Event 006 active-origin classifier.
Its required inputs are the four completed/setup-proven/origin-recorded/origin-adapter-complete receipts, package ID, existence, and non-active/non-ended Event 006 origin; it has no side effects or default admission.
Incomplete actors still lose partial completion receipts, and actual annexation/formable absorption retain their separate teardown path.
This keeps package-local predicates alive after reconstruction without marking Event 006 fired, changing its accounting, or enabling league participation.
Example: a recognized Event 021-created package survives reconstruction with package content active and `is_independence_wave_active_country = no`.
The shared Event 006 local-content and player-surface predicates now accept this complete Event 021-origin package, so its reused focus, category, decision, formable, and AI surfaces remain available after setup without changing Event 006 lifecycle state.
That source bridge still requires live package/runtime validation for every admitted package and does not certify save/reload, settlement, or player-facing consumer behavior.

`event021_review_current_country` removes a recovered queued country before re-evaluating Critical admission, routes an invalid registered country through `event021_dequeue_critical_country` before `event021_unregister_global_country`, and the parent queue pass repeats that validity check at launch time, keeping the Critical queue array, country receipt, and count aligned. A claimed row is not dequeued until the owner-aware callback resolves it.

`event021_register_fracture_evidence` stores regional, command, and Event 006 actor/package/region identity in source-specific receipts. Callers may provide the normal scope input `event021_evidence_actor_scope`; refresh invalidates the source receipt if that referenced actor no longer exists. Settlement completion produces its own finite settlement receipt, and all receipt families expire through the shared refresh helper.

## Side-effect rules

The effects do not create an actual nonhuman country, duplicate an Event 006 tag or character, or enroll an Event 006 package in league systems.

The global arrays are capacity bounded by `random_civil_war_capacity` and are cleared only when their registered scopes are no longer valid.

The explicit manual scenario request may enumerate eligible countries once to build Low, Medium, and High target pools, while Maximum selects every eligible country directly. Selection and host-bound plan preparation complete before the immediate commit pass; ordinary and recurring review paths never use `every_country`.

## Example

An ordinary parent call prepares a target, reserves it, plans connected states, calls `event021_prepare_force_package`, validates the plan, and then calls the appropriate parent commit adapter.

The parent passes `random_civil_war_opening_size`, `random_civil_war_opening_army_ratio`, `random_civil_war_opening_navy_ratio`, and `random_civil_war_opening_air_ratio` to the vanilla civil-war adapter.
