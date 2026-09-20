# Event 021 parent transaction effects

This file documents the parent execution effects in `021_random_civil_war_parent_effects.txt`.

The parent layer is the only owner of target-to-actor planning, route selection, connected-region planning, Event 006 and same-tag adapters, front publication, scheduler dispatch, evolution record dispatch, settlement callbacks, scenario commits, and final cleanup.

## Runtime contract

`event021_parent_initialize_global_runtime` seeds the global arrays from a bounded existing-country scope and initializes the rework-ready release gate fail-closed exactly once per runtime generation. The owner can deliberately publish the ready flag only after final certification; routine registration and scheduler calls do not revoke that publication.

`event021_parent_global_scheduler_pulse` runs only from the existing Chaos global host pulse. Evolution III gates its capped broad-country registration, due-country openings, and Critical queue launches; earlier stages use the same bounded review only for countries explicitly registered by live crisis paths.

Critical queue admission is independent from current theater capacity. A launch claims the queue row with a global lock and `random_civil_war_critical_launch_pending`; hidden callback `chaosx.nr21.18` owns the immediate opening attempt and records `launched`, `stabilized`, or `invalidated` before dequeueing. A still-valid Critical target remains queued after a failed preflight, while stale or recovered rows are removed with an exit receipt. Separate centralized admission and launch budgets bound both operations in one pulse.

`event021_parent_process_evolution_schedule` calls each evolution wrapper once when its shared unlock is present and its record is not yet written.

The schedule uses hidden callback events `chaosx.nr21.11`, `.12`, and `.13`, while the bounded registered-country review and scenario loops use `.14`, `.15`, and the host-bound preparation callback `.19`. Same-tag dispatch uses `.16`, Critical launch dispatch uses `.18`, and reconstruction cleanup uses `.10`, so the event file remains the callback boundary for these scoped transactions.

`event021_global_review_current_country` performs one country review, removes stale neighboring-exposure receipts when their source crisis is no longer usable, closes due same-tag contests, reviews fronts, and applies settlement or reconstruction when due. Critical queueing and bounded launch claims are additionally gated by active Evolution III; review itself never opens a due country outside the Critical queue.

The same review gives a country opened after Evolution II the bounded neighboring-exposure and strange-incident pass, and emits the multi-front presentation once per crisis when its host is known. The Evolution III record emits the country report and the nonterminal Global Fracture news presentation once, subject to the shared Event Log setting.

## Opening transaction

The Event 006 selected actor and anchor remain regular event targets and expire with their effect chain.
`event021_parent_prepare_route_evidence` and `event021_parent_find_event6_package` bind `random_civil_war_event6_selection_owner` to the actual host and clear its `random_civil_war_event6_selected_actor_valid` and `random_civil_war_event6_selected_anchor_valid` country flags before selection.
The finder publishes each validity flag only with the corresponding pointer; a valid anchor with no actor remains the supported dormant-carrier absence case.
`independence_wave_capture_event021_adapter_actor` resets actor validity and publishes it only with a matching existing carrier, preserving failed-release detection even when a previous actor pointer remains in the chain.
Every selected-target presence gate also requires the matching flag through the selection-owner target, including actor-scoped package preparation.
`event021_parent_prepare_event6_adapter_actor` marks the carrier while the shared Event 006 package setup is open and snapshots any pre-existing Event 021 generation value. `event021_parent_cleanup_failed_event6_adapter_actor` calls the documented generation-local `independence_wave_reset_current_generation` while the carrier is still in scope, restores that prior generation value, clears Event 021's package, opening, route, and crisis transaction values, and clears the transient preparation/package-ready bridge flags before a newly released carrier is annexed or a dormant pre-existing carrier is returned. The marker and snapshot are cleared by the common transaction cleanup after a successful opening or rollback.
`event021_parent_clear_event6_package_transaction` invalidates both flags on the host after success or rollback; rollback consumes the pointers before invalidation.
No target is rebound to a null stand-in or converted to a global target.
Inputs are the existing package registry and host; outputs are the selected targets and explicit validity flags, with absent flags as the default.
There are no tuning constants, weights, or player-facing changes in this lifecycle contract.
Example: select a package, release and capture its carrier, consume the guarded targets synchronously, then call `event021_parent_clear_event6_package_transaction = yes` in the host.
The presentation continuation `chaosx.nr21.8` does not consume either selection target; durable actor and anchor receipts are copied before transaction cleanup.

`event021_parent_prepare_route_evidence` derives ideological, legal, regional, command, same-tag, dormant Event 006, and existing Event 006 evidence flags.

`event021_parent_select_archetype` calls the centralized route weights and records one archetype.

`event021_parent_select_severity` calls the core severity helper and applies route-specific stress overrides.

`event021_parent_prepare_target` selects the target or publishes the N/A and zero-weight fallback. A reserved Critical callback may reuse its queued country without opening a second selection transaction.

`event021_parent_report_no_target` presents a concise notification only for a direct human entry that finds no target. Automatic scheduler and Wars-cluster calls remain silent, and the notification cannot reserve a country or create an actor.

`event021_parent_begin_target_transaction` saves the target and host scopes and claims the shared target reservation.

`event021_parent_plan_connected_states` selects a viable capital or anchor and adds only connected controlled states below the centralized plan cap.

`event021_parent_build_front_plan` now writes a bounded aligned pre-commit ledger before any opening mutation. Its row arrays store the front id, archetype, anchor and capital scopes, objective, status, source or carrier scope, actor type, generation, route provenance, Event 006 package id, flattened connected-state membership with row offsets, force and stockpile envelopes, naval and air shares, and the front relationship.

The normal row order is host remnant, primary claimant, up to two frozen ordinary secondaries, and one frozen Event 006 secondary, with optional rows appended only when their independent receipts already exist. The host remnant uses the distinct `administrative_continuity` objective, while the primary, nested, independence, and same-tag rows retain their route-specific terminal objectives.

`event021_parent_validate_front_plan` rejects missing, misaligned, empty, or over-cap rows before the start effect. `event021_parent_load_planned_primary_front` and `event021_parent_load_planned_secondary_front` rehydrate the selected row rather than recalculating against the changed map. The plan remains available until all rows are consumed or explicitly rejected, then `event021_parent_clear_front_plan` removes every aligned array during rollback or final cleanup.

`event021_register_front`, `event021_set_priority_front`, and the secondary review and close paths bind live actors back to their planned row. Failed optional ordinary or Event 006 starters mark their frozen row rejected, and settlement review remains unresolved while any planned row is neither consumed nor rejected. The bounded release admits at most five rows; the second ordinary row is limited to severe or critical major targets with at least three opening states and uses a smaller force envelope.

`event021_parent_freeze_scenario_plan` records the selected scenario archetype, severity, anchor, bounded connected-state set, and high-intensity ordinary and Event 006 secondary receipts on the target country before the confirmation callback. The ordinary secondary state is stored as a country-scoped state pointer, not a chain-local target, so the receipt survives into the callback. `event021_parent_apply_frozen_scenario_plan` rehydrates both independent receipts into the single global transaction and rechecks each state through `event021_reserve_state`; it never searches for a replacement after the opening begins.

`random_civil_war_trigger_manual_scenario` maintains separate confirmation-time snapshots for preflight-selected countries and frozen commit-eligible countries. Maximum enumerates every country that passes the normal-human, topology, route-type, capacity, and opening-state preflight, freezes all of those rows through `chaosx.nr21.19`, and sends `chaosx.nr21.15` only to the resulting commit set. `global.random_civil_war_scenario_preflight_count`, `global.random_civil_war_scenario_plan_eligible_count`, and `global.random_civil_war_scenario_preflight_skipped_count` expose the distinction; a failed freeze is accounted for as a skip and cannot be replaced by a post-mutation reroll.

The scenario confirmation reservation uses `global.random_civil_war_scenario_reserved_states` and `global.random_civil_war_scenario_reserved_event6_packages` to prevent overlapping state or package selections while the one-shot setup is running. `event021_parent_clear_scenario_plan_receipt` removes those reservations and state markers on rollback, successful dispatch cleanup, or crisis cleanup without touching durable crisis history.

`event021_parent_mark_opening_states` records opening core and remnant state information before any transfer.

`event021_parent_copy_opening_state_receipts` runs in the receiving country and copies the two global transaction state arrays into that country's opening-state arrays.
Its inputs are `global.random_civil_war_event21_opening_states` and `global.random_civil_war_event21_original_core_states`; its outputs replace `random_civil_war_opening_core_states` and `random_civil_war_opening_all_core_states` on the caller.
There are no default states: an empty transaction array produces an empty receipt array, and the achievement review refuses to count an empty original-core set as full reintegration.
The helper saves the chain-local `random_civil_war_receipt_owner` target, enters each stored state, then returns to the receiving country with the state supplied explicitly as `PREV`.
This prevents scheduler-host `ROOT` or the iterated state from becoming the owner of a country's receipt array.
Primary ordinary and Event 006 actors copy both transaction arrays; secondary actors replace only their detached-state array with their exact anchor while retaining the original-core receipt.
Example: call `event021_parent_copy_opening_state_receipts = yes` in the newly initialized claimant after the opening transaction is populated and before settlement review can run.

`event021_parent_record_achievement_receipts` evaluates reintegration and current-capital control against its explicit country target, not the originating event ROOT, and clears its recomputable positive receipts before each evaluation.
The dedicated helpers in `021_random_civil_war_achievement_effects.md` own capital continuity and authority-minimum receipts; current-capital control alone does not prove continuity.
Successor receipt transfer, complete generation reset, and runtime certification remain separate lifecycle gates.

`event021_parent_prepare_dynamic_force_package` scans only the bounded connected plan for local divisions, population support, depots, arsenals, ports, and airfields, then combines that evidence with actor identity, equipment availability, external war, and severity. It clears all prior force-readiness receipts before recomputation and publishes capped army, manpower, stockpile, air, and naval receipts; air and naval shares remain zero without both a suitable base and live assets, and Event 006 retains its package-owned force profile.

`event021_parent_capture_actual_actor_force_receipt` runs in the created actor scope after the engine split or Event 006 package setup. It records actual actor divisions, manpower, and equipment availability into the actor record and immutable opening-log arrays, while `event021_parent_clear_pending_force_transaction` consumes and clears the temporary cross-scope ratio receipts on success and rollback.

`event021_parent_validate_opening_plan` checks the actor, capital, state, front, package, and capacity requirements.

`event021_parent_dispatch_opening` is the single public launch path for hidden entry, bounded queue, manual scenario, and Wars cluster launches. After any successful opening marks the target active, the dispatcher removes that country from the Critical queue through the aligned dequeue helper; the `.18` callback then records the terminal Critical exit and releases the launch lock. Failed openings retain later-review eligibility.

`event021_parent_prepare_crisis_identity`, `event021_parent_assign_government_profile`, and the opposition initialization effects prepare the ordinary claimant without duplicating a persistent country identity.

`event021_parent_prepare_crisis_identity` is also the only writer of the frozen `random_civil_war_external_war_at_opening` receipt, so later route reviews cannot change achievement history.

Generation allocation is provisional until the core opening commits.
Identity preparation stores `random_civil_war_generation_before_plan`, and core rollback restores it and releases the generation-seeded flag if the opening fails.
`event021_parent_commit_generation_history` consumes the prior recurrence window and its eligibility only after success, preserving the previous window on failed preflight.
It clears the provisional snapshot but keeps the committed generation and recurrence memory.
Core crisis cleanup releases `random_civil_war_generation_seeded` so a later eligible crisis can advance one generation within the existing generation gate.
Example: a failed generation-two attempt from generation one restores generation one; a successful attempt retains generation two and consumes the prior recurrence window.

`event021_parent_prepare_route_evidence` clears and recomputes recoverable political-competition, military-loyalty, regional-grievance, and state-capacity receipts from current conditions before every route selection, preventing stale weakness from renewing its own pressure or eligibility.

`event021_parent_commit_same_tag_takeover` consumes the same core opening transaction as territorial routes before it starts the loyalty contest. This publishes the plan-owner/theater receipts and releases the global planning lock and state reservations without creating or transferring a country.

`event021_parent_bind_current_crisis_targets` rebuilds transaction-only global host and actor pointers from the current side's durable country-scoped pointers before settlement or cleanup fallbacks, preventing simultaneous theaters from consuming another crisis's most recent pointers.

`event021_parent_start_ordinary_civil_war` invokes the dynamic vanilla civil-war adapter after plan validation.

`event021_parent_start_event6_front` invokes the existing complete setup contract for the selected one of 32 content-attested Event 006 packages, applies the Event 021 origin receipt, and does not publish the actor or host-side pointer until an actual war with the host is present.

`event021_parent_clear_event6_package_transaction` consumes the package selection and adapter-pending receipts on success or rollback without clearing the ordinary crisis identity or force transaction.

`event021_parent_commit_same_tag_takeover` uses the same-tag contest route for unsafe one-state and all-island countries without releasing a duplicate tag.

`event021_parent_rollback_transaction` clears all provisional target, state, front, force, and reservation state when validation fails.

## Active fronts and extensions

`event021_parent_reserve_current_archetype`, `event021_parent_prepare_secondary_route`, and `event021_parent_reserve_pending_secondary_route` give each ordinary belligerent one distinct live route receipt and reserve it only after actor initialization succeeds.

`event021_parent_try_secondary_front`, `event021_parent_start_secondary_civil_war`, `event021_parent_review_secondary_front`, and `event021_parent_close_secondary_front` implement Evolution I multi-front expansion within the route, front, and theater caps. A large map without another proven route stops at two belligerents instead of manufacturing an archetype. Each ordinary secondary actor receives the AI role matching its reserved archetype: command claimants use the command profile, legal and regional fronts use the constitutional profile, and ideological fronts use the revolutionary profile.

`event021_parent_try_event6_secondary_front` may consume one complete dormant Event 006 package as a distinct additional independence front after an ordinary opening. It requires a noncapital unreserved package anchor, an available front and theater slot, a preserved host remnant, the multi-front gate, and a proved war before registration. Its rollback returns only that anchor, releases only that partial package actor, and leaves the committed ordinary crisis intact. When a scenario freeze contains both secondary receipts, the Event 006 front and ordinary front are consumed as separate planned openings rather than competing through an if/else selection branch.

`event021_parent_review_event6_secondary_front` and `event021_parent_finalize_event6_secondary_actor` close the additional package front through its own host pointer and preserve its durable Event 006 identity after recognition.

`event021_parent_expose_neighbor`, `event021_parent_propagate_exposure`, and `event021_parent_roll_strange_incident` implement Evolution II’s bounded regional exposure, distinct civilian relief and armed support, sponsor records, and rate-limited strange incident. The propagation pass binds and clears its dedicated source target inside the bounded neighbor iteration.

The sponsor helper carries recipient and front identifiers through normal country-scoped bridge variables before recording the commitment, because temporary variables cannot persist across the nested country scopes used by the neighbor pass.

`event021_parent_apply_evolution_i`, `event021_parent_apply_evolution_ii`, and `event021_parent_apply_evolution_iii` are the history-writing wrappers for the three Event Log and Event Details evolution records.

`event021_parent_reconstruction_tick` is a finite postwar tick that records settlement obligations and calls cleanup only after reconstruction is complete.

`event021_parent_finalize_event6_actor` closes the primary Event 006 side state while preserving the durable Event 006 package and origin history.

`event021_parent_promote_ordinary_successor` requires an ordinary opposition actor and a distinct living predecessor with the same nonmissing crisis ID.
An absent country-scoped predecessor may be restored from the global host pointer only after the same-crisis check; an existing stale pointer is never silently replaced by another theater.
The helper copies predecessor achievement history, marks the successor, and makes white peace before annexing the explicit chain-local predecessor target.
It does not run predecessor core cleanup before annexation, because `on_annex` needs the old host and front receipts to transfer surviving fronts through `event021_handle_annexed_country`.
Example: claimant A replaces government B while front C survives; the annex callback rebinds C to A rather than unregistering C as collateral cleanup.
This documents the scripted promotion path; natural engine civil-war annexation, continuing-front obligations, and runtime ordering still require their own evidence.

`event021_parent_prepare_annex_successor` is restricted to the vanilla `on_annex` context, with ROOT as winner and FROM as annexed country.
Before FROM cleanup, it recognizes a surviving ordinary opposition actor only when its explicit host pointer names FROM, FROM retains the government role, and both countries have matching crisis IDs.
It copies historical receipts and marks succession without annexing, declaring war, or granting an award.
This covers natural engine victory before the next bounded settlement review; Event 006 independence actors and unrelated annexers do not receive ordinary-successor status.
The subsequent lifecycle helper owns surviving-front pointer transfer; continuity of the remaining wars still requires separate verification.

`event021_parent_cleanup_crisis` removes temporary ideas, missions, flags, targets, registry entries, scenario bypass, and front state while retaining settlement, recurrence, achievement, and Event 006 history.

## Scenario contract

`random_civil_war_trigger_manual_scenario` and `event021_parent_prepare_scenario_country` consume the selected SCN-018 type and intensity.

`random_civil_war_trigger_manual_scenario` first freezes the unique selected country set, then sends `chaosx.nr21.19` to each selected country for host-correct route, actor, capital, state, package, and force planning. Only after every selected country has completed that preparation pass does the controller send `chaosx.nr21.15` to consume each immutable receipt through `event021_parent_commit_scenario_country`. A failed confirmation plan clears the target-ready flag and records a scenario skip rather than falling back to a post-mutation selection. The preparation pass can retain both an ordinary secondary route and a complete Event 006 package route for one host; the commit pass consumes each receipt independently after the primary plan is frozen.

The Maximum intensity caller owns the explicit all-eligible-country selection required by the scenario specification. It freezes every eligible country's plan before the first ownership mutation and retains the exact requested/committed/skipped counts. Low, Medium, and High use the same two-phase contract after their weighted ticket draw. Low applies a centralized 4:1 minor-to-major ticket ladder, Medium is neutral at 2:2, and High applies a 1:3 ladder before the shared individual-crisis load adjustment; Maximum bypasses this ladder because it selects the frozen eligible set directly.

No delayed fallback is present because the implementation has no measured performance failure that would justify one.

## Manual scenario draw validity

The manual picker clears `random_civil_war_scenario_target_draw_succeeded` on the calling country before every draw.
The `random_scope_in_array` success body saves the real selected-country target and sets that flag through PREV, which is the picker country.
The dispatch gate requires both the flag and the local target; an empty eligible subset therefore cannot reuse a preceding successful draw's target.
The existing failure branch consumes the remaining selection budget, while the success branch preserves the existing ticket-removal count and selected-count increment.
The flag is cleared after the loop and the regular target expires with the event chain.
No delayed event reads the draw flag.
