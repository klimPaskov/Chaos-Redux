# Event 021 parent transaction effects

This file documents the parent execution effects in `021_random_civil_war_parent_effects.txt`.

The parent layer is the only owner of target-to-actor planning, route selection, connected-region planning, Event 006 and same-tag adapters, front publication, scheduler dispatch, evolution record dispatch, settlement callbacks, scenario commits, and final cleanup.

## Runtime contract

`event021_parent_initialize_global_runtime` seeds the global arrays from a bounded existing-country scope and initializes the rework-ready release gate fail-closed exactly once per runtime generation. The owner can deliberately publish the ready flag only after final certification; routine registration and scheduler calls do not revoke that publication.

`event021_parent_global_scheduler_pulse` runs only from the existing Chaos global host pulse. Evolution III gates its capped broad-country registration, due-country openings, and Critical queue launches; earlier stages use the same bounded review only for countries explicitly registered by live crisis paths.

Critical queue admission is independent from current theater capacity. A launch claims the queue row with a global lock and `random_civil_war_critical_launch_pending`; hidden callback `chaosx.nr21.18` owns the immediate opening attempt and records `launched`, `stabilized`, or `invalidated` before dequeueing. A still-valid Critical target remains queued after a failed preflight, while stale or recovered rows are removed with an exit receipt. Separate centralized admission and launch budgets bound both operations in one pulse.

`event021_parent_process_evolution_schedule` calls each evolution wrapper once when its shared unlock is present and its record is not yet written.
Before any sample or dispatch it builds each stage's Events Log context through `event021_parent_prepare_stage_evolution_context` and checks `is_current_evolution_enabled` for that stage.
A stage switched off in the Events Log settings is never sampled, fired, activated, or recorded, and any stale due date is cleared.
Evolution II needs Evolution I to be recorded or switched off, and Evolution III needs both earlier stages to be recorded or switched off, so stages stay in order while a switched-off stage never blocks a later one.
`event021_apply_evolution_ii` and `event021_apply_evolution_iii` enable only their own mechanics, and the parent wrappers accept a switched-off earlier stage through `event021_evolution_i_disabled` and `event021_evolution_ii_disabled`, so a later stage never switches on a disabled stage's mechanics.
Re-enabling a stage returns it to normal scheduling: it samples a due date and fires through its own wrapper even if a later stage already ran.
This follows Event 004's independent per-stage `is_current_evolution_enabled` checks in `common/scripted_effects/004_random_war_effects.txt`.

The schedule uses hidden callback events `chaosx.nr21.11`, `.12`, and `.13`, while the bounded registered-country review and scenario loops use `.14`, `.15`, and the host-bound preparation callback `.19`. Same-tag dispatch uses `.16`, Critical launch dispatch uses `.18`, and reconstruction cleanup uses `.10`, so the event file remains the callback boundary for these scoped transactions.

`event021_global_review_current_country` performs one country review, removes stale neighboring-exposure receipts when their source crisis is no longer usable, closes due same-tag contests, reviews fronts, and applies settlement or reconstruction when due. Critical queueing and bounded launch claims are additionally gated by active Evolution III; review itself never opens a due country outside the Critical queue.

`event021_parent_update_front_resolution_receipts` reads every active durable front row whose crisis ID matches the current country. It inspects opposition actors and their immediate opponents, then publishes `random_civil_war_internal_fronts_resolved` only when no registered opposition relationship remains at war and no planned row remains pending. The country is the input scope, its crisis ID is the only required input, and absent crisis identity or misaligned front actor, crisis, or status arrays fail closed. It does not mutate the registry, end wars, annex actors, clear sibling fronts, or change tuning. A registered opposition actor with no immediate-opponent pointer also remains unresolved; government rows do not require such a pointer. Example: call the helper after front review during the bounded country review; it evaluates all registered opposition fronts of that crisis regardless of which actor was most recently stored in a compatibility pointer.

`event021_parent_find_registered_front_source` accepts a source front id and the current crisis id on the host country, then saves the matching active registered opposition actor as `random_civil_war_dynamic_front_source_country`. Misaligned registry arrays, a missing row, a closed row, or mismatched actor receipts return no source and cause the optional row to be rejected. It does not change registry rows.

`event021_parent_activate_planned_optional_front_rows` runs on a committed crisis host after the primary front and serially visits every optional planned row through array iteration.
Ordinary rows resolve their source front id, stage the exact row state span, and call the ordinary adapter; Event 006 rows stage their package, anchor, and origin receipt and call the complete-package adapter.
The dynamic candidate writer admits variable-length disjoint viable regions and complete package receipts, not a fixed optional-row count.
Registration consumes the row only after exact receipt validation; rejection changes global row status without rebinding the host to the child row.
Each row's transfer markers are cleared before the next iteration, and the activation flag prevents legacy recursion from consuming a sibling.

`event021_parent_copy_planned_front_state_span` runs on a newly created ordinary secondary actor and copies only states in its exact row that are owned and controlled by that actor.
It publishes a count only when the entire frozen span is verified; a missing or partial row leaves an empty receipt and is never reconstructed from generic markers.
The secondary initializer validates that receipt before registry publication and reverses an invalid created child into its exact recorded source.
After optional openings, the host and actors refresh retained membership and measured force receipts from the transaction-owned ledger; historical opening provenance stays separate.
See [`021_random_civil_war_front_ledger_effects.md`](021_random_civil_war_front_ledger_effects.md) for scope, input, output, cleanup, and validation limits.

`event021_parent_review_registered_ordinary_fronts` runs on the crisis host and snapshots all same-crisis AI ordinary secondary actors whose immediate wars have ended. It then closes those actors from the stable temporary snapshot, allowing each close to unregister its durable row without mutating the array under enumeration. It accepts the host's crisis ID, changes only eligible actor and host lifecycle state through `event021_parent_close_secondary_front`, and has no fixed actor count or tuning inputs. An absent crisis ID is rejected by its public caller. Example: the bounded country review calls `event021_parent_review_secondary_front`, which delegates to this helper and can close several resolved nested claimants in one pass.

`event021_parent_refresh_ordinary_secondary_presence` runs on the crisis host after one ordinary secondary front closes. Its inputs are the host crisis ID and aligned durable front actor, crisis, and status arrays. It rebuilds the host's ordinary secondary presence flag and compatibility actor pointer from active registered same-crisis actors still at war with their recorded immediate opponents. It does not mutate registry rows or other countries. With no surviving actor, both receipts stay absent. Example: closing one nested claimant leaves a second live claimant discoverable for later review and settlement checks.

`event021_parent_review_event6_secondary_front` snapshots same-crisis registered Event 006 secondary actors whose host war has ended, records their independence outcome, and clears only those actors' active secondary role. Its temporary snapshot is separate from the durable registry, so settlement and cleanup may remove registry rows without changing the array under iteration. `event021_parent_refresh_event6_secondary_presence` then rebuilds the host's presence flag and compatibility pointer from still-warring registered package actors. `event021_parent_finalize_event6_secondary_actor` snapshots all same-crisis actors with the durable secondary-package origin role and finalizes each independently at host cleanup. These helpers require the host crisis ID, use no fixed package count, and do not initialize, alter, or duplicate Event 006 packages. Example: two complete package fronts can have independent war outcomes while the host keeps a pointer to a surviving one, and both receive their own cleanup receipts after the host reconstructs.

The same review gives a country opened after Evolution II the bounded neighboring-exposure and strange-incident pass, and emits the multi-front presentation once per crisis when its host is known. The Evolution III record emits the country report and the nonterminal Global Fracture news presentation once, subject to the shared Event Log setting.

## Opening transaction

`event021_parent_reject_secondary_transfer` accepts COUNTRY scope on the recorded source of the current serial secondary transaction.
It clears the existing pending-force scratch, marks the source's secondary attempt rejected, clears the pending secondary flag and route receipt, and releases the pending anchor/source global targets and front ID/goal/archetype.
Both the initial receipt gate and the final revalidation gate use this one cleanup path.
It creates no country, moves no state or unit, changes no tuning or weighted selection, and does not unregister a living front.
The starter alone owns the following common marker cleanup.
Example: call the rejection helper from the false branch of `event021_secondary_transfer_valid` after receipt validation.
The final positive branch surrounds ratio publication, missile preflight, and every native government branch, including its fallback.

The Event 006 selected actor and anchor remain regular event targets and expire with their effect chain.
`event021_parent_prepare_route_evidence` and `event021_parent_find_event6_package` bind `random_civil_war_event6_selection_owner` to the actual host and clear its `random_civil_war_event6_selected_actor_valid` and `random_civil_war_event6_selected_anchor_valid` country flags before selection.
The finder publishes each validity flag only with the corresponding pointer; every selected Event 006 anchor excludes the host capital, reserved states, active-front states, and scenario-reserved states on both primary and secondary paths. A valid anchor with no actor remains the supported dormant-carrier absence case.
`independence_wave_capture_event021_adapter_actor` resets actor validity and publishes it only with a matching existing carrier, preserving failed-release detection even when a previous actor pointer remains in the chain.
Every selected-target presence gate also requires the matching flag through the selection-owner target, including actor-scoped package preparation.
`event021_parent_capture_event6_previous_capital` enters `capital_scope` only after proving the carrier owns a capital, then retains that state as a chain-local rollback target. Both Event 006 opening rollback paths return the anchor first and restore the prior capital only if the saved state still belongs to the selected carrier. The adapter capital transfer also sets `remember_old_capital = yes` for engine-side recovery if the newly assigned anchor is later lost.
`event021_parent_prepare_event6_adapter_actor` marks the carrier while the shared Event 006 package setup is open and snapshots any pre-existing Event 021 generation value. `event021_parent_cleanup_failed_event6_adapter_actor` calls the documented generation-local `independence_wave_reset_current_generation` while the carrier is still in scope, restores that prior generation value, clears Event 021's package, opening, route, and crisis transaction values, and clears the transient preparation/package-ready bridge flags before a newly released carrier is annexed or a dormant pre-existing carrier is returned. The marker and snapshot are cleared by the common transaction cleanup after a successful opening or rollback.
`event021_parent_clear_event6_package_transaction` invalidates the selected-actor and selected-anchor flags plus the prior-capital guard on the host after success or rollback; rollback consumes the pointers before invalidation.
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

`event021_parent_plan_connected_states` selects a viable capital or anchor and adds connected controlled states within the dynamic severity-and-region budget while preserving the remnant.

`event021_parent_build_front_plan` writes an aligned pre-commit ledger before any opening mutation. Its row arrays store the front id, source-front id, archetype, anchor and capital scopes, objective, status, source or carrier scope, actor type, generation, route provenance, Event 006 package id plus region/depth/package-archetype receipts, flattened state membership with row offsets, force and stockpile envelopes, naval and air shares, and the front relationship.

The normal row order is host remnant, primary claimant, and every optional candidate row admitted by the dynamic state/package ledger. Ordinary row count follows distinct viable state anchors, while Event 006 row count follows complete package receipts; route archetypes may repeat across independent anchors. The host remnant uses the distinct `administrative_continuity` objective, while the primary, nested, independence, and same-tag rows retain their route-specific terminal objectives.

`event021_parent_validate_front_plan` rejects missing, misaligned, empty, or over-cap plans before the start effect. Automatic and lower-intensity scenario candidates use the live state-derived crisis capacity and shared global front cap; Maximum scenario plans use a temporary front envelope derived from the complete eligible roster, current active fronts, and remaining normal capacity. `event021_parent_load_planned_primary_front` and `event021_parent_load_planned_secondary_front` rehydrate a selected row rather than recalculating against a changed map. The plan remains available until every row is consumed or explicitly rejected, then `event021_parent_clear_front_plan` removes every aligned array during rollback or final cleanup.

`event021_register_front`, `event021_set_priority_front`, and the secondary review and close paths bind live actors back to their planned row. Failed optional ordinary or Event 006 starters mark their row rejected, and settlement review remains unresolved while any planned row is neither consumed nor rejected. `event021_parent_activate_planned_optional_front_rows` iterates optional rows by front id, resolves each ordinary source through the same-crisis registry, and stages only that row's state or package receipt before activation.

`event021_parent_freeze_scenario_plan` records the selected scenario archetype, severity, anchor, bounded connected-state set, and a variable-length optional-front receipt on the target country before any scenario country commits. `event021_parent_freeze_scenario_optional_front_rows` stores aligned route, actor, anchor, state-span, package, and score arrays; `event021_parent_load_scenario_optional_front_rows` rehydrates that exact receipt and rejects stale state ownership/control or misaligned rows without searching for a replacement. The scenario controller reserves mandatory front capacity as countries are selected, and optional rows consume only the remaining shared capacity. The old named scenario secondary fields are compatibility-cleanup receipts and do not control row count or replay.

`random_civil_war_trigger_manual_scenario` maintains separate confirmation-time snapshots for eligible selected countries and frozen commit-eligible countries. Maximum enumerates every eligible normal-human country, derives mandatory front reservations from same-tag versus ordinary topology, and establishes a temporary front envelope large enough for those openings plus current normal spare capacity without changing the shared normal cap. Each selected country's primary and variable-length optional plan freezes through `chaosx.nr21.19`, and `chaosx.nr21.15` reaches only the resulting commit set. `global.random_civil_war_scenario_eligible_count`, `global.random_civil_war_scenario_requested_count`, `global.random_civil_war_scenario_preflight_count`, `global.random_civil_war_scenario_plan_eligible_count`, and `global.random_civil_war_scenario_preflight_skipped_count` preserve eligibility, request, freeze, and commit counts separately; a failed freeze is accounted for as a skip and cannot be replaced by a post-mutation reroll.

`event021_parent_prepare_maximum_scenario_front_envelope` accepts the normal spare-front count and topology-derived mandatory-front total, then adds the current active count to publish a scenario-local total cap. An uninitialized active count defaults to no existing active rows, and the effect never writes the shared stage-specific global cap.
Each frozen scenario plan also holds one dynamic tag per new ordinary claimant through `event021_reserve_scenario_dynamic_tags`; a plan the free pool cannot cover is skipped with `cap_reached`, and the controller releases each hold right after that country's commit.

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

`event021_parent_record_force_state_context` runs in one selected state scope and writes only the host's local-unit, population, depot, arsenal, port, and airfield evidence flags; its caller supplies either one frozen scenario state span or the current connected transaction plan.

`event021_parent_prepare_dynamic_force_package` scans that bounded state source, then combines its observations with actor identity, equipment availability, external war, and severity. During `random_civil_war_scenario_force_preflight_active`, it reads the exact confirmation-time frozen state region; otherwise it reads `global.random_civil_war_plan_states`. It clears all prior force-readiness receipts before recomputation and publishes capped army, manpower, stockpile, air, and naval receipts; air and naval shares remain zero without both a suitable base and live assets, and Event 006 retains its package-owned force profile.

`event021_parent_capture_actual_actor_force_receipt` runs in the created actor scope after the engine split or Event 006 package setup. It records actual actor divisions, manpower, and equipment availability into the actor record and immutable opening-log arrays, while `event021_parent_clear_pending_force_transaction` consumes and clears the temporary cross-scope ratio receipts on success and rollback.

`event021_parent_validate_opening_plan` checks the actor, capital, state, front, package, and capacity requirements.
For every opening except Event 006 and same-tag contests it also requires a free dynamic civil-war tag from `event021_count_free_dynamic_tags`; a full pool rejects the opening with the `cap_reached` skip reason. See `021_random_civil_war_dynamic_tag_effects.md`.

`event021_parent_dispatch_opening` is the single public launch path for hidden entry, bounded queue, manual scenario, and Wars cluster launches. After any successful opening marks the target active, the dispatcher removes that country from the Critical queue through the aligned dequeue helper; the `.18` callback then records the terminal Critical exit and releases the launch lock. Failed openings retain later-review eligibility.

`event021_parent_prepare_crisis_identity`, `event021_parent_assign_government_profile`, and the opposition initialization effects prepare the ordinary claimant without duplicating a persistent country identity.

`event021_parent_prepare_crisis_identity` is also the only writer of the frozen `random_civil_war_external_war_at_opening` receipt, so later route reviews cannot change achievement history.

Generation allocation is provisional until the core opening commits.
Identity preparation stores `random_civil_war_generation_before_plan`, and core rollback restores it and releases the generation-seeded flag if the opening fails.
`event021_parent_commit_generation_history` consumes the prior recurrence window and its eligibility only after success, preserving the previous window on failed preflight.
It clears the provisional snapshot but keeps the committed generation and recurrence memory.
Core crisis cleanup releases `random_civil_war_generation_seeded` so a later eligible crisis can advance one generation within the existing generation gate.
Example: a failed generation-two attempt from generation one restores generation one; a successful attempt retains generation two and consumes the prior recurrence window.
`event021_prepare_recurrence` opens a single earliest-to-latest window only after reconstruction and only when the recurrence score is high enough. Its date base is no earlier than the stored target-cooldown or successor-grace expiry, and it sets the next country review to the earliest date. Low-risk countries receive no recurrence window. Later due reviews preserve those stored dates; an unsuccessful final-window review schedules one bounded expiry check after the latest date.

`event021_parent_prepare_route_evidence` clears and recomputes recoverable political-competition, military-loyalty, regional-grievance, and state-capacity receipts from current conditions before every route selection, preventing stale weakness from renewing its own pressure or eligibility.

`event021_parent_commit_same_tag_takeover` consumes the same core opening transaction as territorial routes before it starts the loyalty contest. This publishes the plan-owner/theater receipts and releases the global planning lock and state reservations without creating or transferring a country.

`event021_parent_bind_current_crisis_targets` rebuilds transaction-only global host and actor pointers from the current side's durable country-scoped pointers before settlement or cleanup fallbacks, preventing simultaneous theaters from consuming another crisis's most recent pointers.

`event021_parent_start_ordinary_civil_war` invokes the dynamic vanilla civil-war adapter after plan validation.

`event021_parent_start_event6_front` invokes the existing complete setup contract for the selected one of 32 content-attested Event 006 packages, applies the Event 021 origin receipt, and does not publish the actor or host-side pointer until an actual war with the host is present.
`event021_parent_find_event6_package` derives its scan bound from the initialized package array's live `^num`, begins at a normalized rotating cursor, and admits a row only after checking the current host, anchor ownership/control, state reservations and fronts, and package runtime preflight. The finite package-ID array is the authored complete-content crosswalk, not a live country eligibility roster.

`event021_parent_clear_event6_package_transaction` consumes the package selection and adapter-pending receipts on success or rollback without clearing the ordinary crisis identity or force transaction.

`event021_parent_commit_same_tag_takeover` uses the same-tag contest route for unsafe one-state and all-island countries without releasing a duplicate tag.

`event021_parent_rollback_transaction` clears all provisional target, state, front, force, and reservation state when validation fails. It preserves a still-valid pre-adoption external-war snapshot or post-adoption successor queue, clears invalid continuity receipts, and refreshes target-pool membership only after provisional eligibility receipts are cleared.

`event021_parent_record_system_log` writes one Events Log crisis record. Its opening-status field carries a skip reason only for a `failed_opening` payload whose skip receipt (`global.random_civil_war_cluster_skip_reason`) was written in the same transaction, which `event021_parent_record_cluster_skip` stamps with today's date. Opening, multi-front, exposure, settlement, reconstruction, and Evolution III records show none, so an older skip elsewhere never appears as a later crisis's opening status.

## Active fronts and extensions

`event021_parent_reserve_current_archetype`, `event021_parent_prepare_secondary_route`, and `event021_parent_reserve_pending_secondary_route` give each ordinary belligerent one distinct live route receipt and reserve it only after actor initialization succeeds.

`event021_parent_try_secondary_front`, `event021_parent_start_secondary_civil_war`, `event021_parent_review_secondary_front`, and `event021_parent_close_secondary_front` implement Evolution I multi-front expansion within the route, front, and theater caps. A large map without another proven route stops at two belligerents instead of manufacturing an archetype. Each ordinary secondary actor receives the AI role matching its reserved archetype: command claimants use the command profile, legal and regional fronts use the constitutional profile, and ideological fronts use the revolutionary profile.

`event021_parent_try_event6_secondary_front` may consume one complete dormant Event 006 package as a distinct additional independence front after an ordinary opening. It requires a noncapital unreserved package anchor, an available front and theater slot, a preserved host remnant, the multi-front gate, and a proved war before registration. Its rollback returns only that anchor, releases only that partial package actor, and leaves the committed ordinary crisis intact. When a scenario freeze contains both secondary receipts, the Event 006 front and ordinary front are consumed as separate planned openings rather than competing through an if/else selection branch.

`event021_parent_review_event6_secondary_front` and `event021_parent_finalize_event6_secondary_actor` close the additional package front through its own host pointer and preserve its durable Event 006 identity after recognition.

`event021_parent_expose_neighbor`, `event021_parent_propagate_exposure`, and `event021_parent_roll_strange_incident` implement Evolution II’s bounded regional exposure, distinct civilian relief and armed support, sponsor records, and rate-limited strange incident.
A successful roll calls `event021_parent_start_strange_incident`, which binds `random_civil_war_strange_incident_state` (the anchor state while the side controls it, otherwise its capital), stores one of five `event021_strange_incident_variant` values from equal centralized weights, adds the matching practice idea and `event021_strange_incident_strain` as timed ideas, and fires `chaosx.nr21.21`. `event021_strange_incident_active` (parent triggers) blocks a second roll while either idea runs. The three responses and `event021_cleanup_strange_incident` live in the decision effects file, and crisis cleanup calls the cleanup. The propagation pass binds and clears its dedicated source target inside the bounded neighbor iteration.

The sponsor helper carries recipient and front identifiers through normal country-scoped bridge variables before recording the commitment, because temporary variables cannot persist across the nested country scopes used by the neighbor pass.

`event021_parent_apply_evolution_i`, `event021_parent_apply_evolution_ii`, and `event021_parent_apply_evolution_iii` are the history-writing wrappers for the three Event Log and Event Details evolution records.
The first recorded Evolution I also calls `event021_parent_attach_active_evolution_i_reviews`, which queues one review of every war that was already running and unlocks its Evolution I management phase.
The global scheduler pulse ends with `event021_parent_process_active_evolution_i_reviews`, which dispatches a bounded slice of those reviews through `chaosx.nr21.20`.
The review, its candidate collector, its government-owned receipt, and its commit through the secondary adapters are documented in `021_random_civil_war_active_evolution_effects.md`.
While that commit holds `random_civil_war_active_front_commit_in_progress`, `event021_parent_load_planned_secondary_front`, `event021_parent_copy_planned_front_state_span`, and `event021_parent_copy_opening_state_receipts` read the reviewing government's own receipt instead of the global opening template; outside that lock they are unchanged.
`event021_parent_apply_settlement` removes Evolution I management access from every side of the crisis, and `event021_parent_cleanup_crisis` clears the review and management receipts on the country it cleans.

`event021_parent_apply_settlement` also settles signed terms while the war is still being fought: `event021_decision_offer_settlement` sets `event021_settlement_pending` and `event021_settlement_talks_open`, and the `chaosx.nr21.5` option calls the apply (or `event021_parent_resolve_same_tag_takeover` for a same-tag contest) while the pending marker is still set.
With talks open, `event021_parent_select_settlement_terms` never selects a government military victory: at or above `strong_settlement_threshold` it selects merger when `random_civil_war_merger_topology_ready` holds, autonomy on a regional route, or coalition, and below it selects partition when `random_civil_war_partition_topology_ready` holds and coalition otherwise.
`event021_parent_close_ordinary_opposition` also runs for an Event 006 host that signed terms, after `event021_parent_end_event6_war`, and its per-actor filter leaves Event 006 actors on their independence path.
`event021_parent_preserve_partition_successors` makes each successor peace with ROOT and with its recorded immediate opponent, so a nested front fighting its source claimant also stops.
`event021_settlement_offer_blocked` (parent triggers) keeps the offer unavailable while a package-owned Event 006 secondary front is active or any live opposing side is player-controlled.
`event021_settlement_offer_ready` keeps it unavailable until the war has lasted `minimum_war_days` from `random_civil_war_crisis_start_date`. The opening commit and successor adoption call `event021_record_settlement_offer_baseline`, and both host opening paths call `event021_record_opening_held_states` after their optional fronts have taken their states, so the AI can judge lost ground.

`event021_parent_reconstruction_tick` is a finite postwar tick that records settlement obligations and calls cleanup only after reconstruction is complete and the obligation is no longer open.
The global review calls it whenever `event021_parent_reconstruction_due` holds: at the reconstruction deadline, at the terms-hold date while the obligation is still open (whether or not reconstruction has finished), and once more when reconstruction is complete and the obligation is already fulfilled or breached but `random_civil_war_reconstruction_resolved` is not yet set.
The final block (administration restored, recurrence prepared, reconstruction record, `chaosx.nr21.10` cleanup) runs once per crisis generation because it requires `random_civil_war_reconstruction_resolved` to be absent, so an Event 006 actor that host cleanup already finalized is only judged on its obligation.
With `reconstruction_days = 120` and `settlement_terms_hold_days = 180`, reconstruction completes on the first review at or after day 120, the obligation is judged held or breached on the first review at or after day 180, and the same tick fires `chaosx.nr21.10`, which unregisters the theater and clears `random_civil_war_active`, releasing global capacity.
An obligation breached early, for example by a failed terms mission, is resolved by that mission and reaches cleanup on the first review after reconstruction completes.
`event021_parent_review_settlement_obligation` treats a terms mission that confirmed the objective (`random_civil_war_settlement_obligation_objective_met`) as sufficient at the hold date, matching the fulfilled branch, and closes the settlement phase once the obligation is no longer open.
While Upholding the Settlement runs (`event021_settlement_terms_mission_active`), the review leaves both hold-date branches to the mission, whose timer ends on the hold date. Early breaches (a failed objective or a committed recurrence) still resolve at once and cancel the hold.
No periodic hook is added: the tick rides the existing global-host review pulse.

`event021_parent_finalize_event6_actor` closes the primary Event 006 side state while preserving the durable Event 006 package and origin history.

`event021_parent_promote_ordinary_successor` requires an ordinary opposition actor and a distinct living predecessor with the same nonmissing crisis ID.
An absent country-scoped predecessor may be restored from the global host pointer only after the same-crisis check; an existing stale pointer is never silently replaced by another theater.
The helper copies predecessor achievement history, marks the successor, prepares its surviving-front roster, snapshots the predecessor's live external enemy-country scopes, and only then makes white peace and annexes the explicit chain-local predecessor target.
It does not run predecessor core cleanup before annexation, because `on_annex` needs the old host and front receipts to transfer surviving fronts through `event021_handle_annexed_country`.
Example: claimant A replaces government B while front C survives; the annex callback rebinds C to A rather than unregistering C as collateral cleanup.
The external-war snapshot is relation-only: after roster adoption, a human successor may choose a currently valid new core- or claimed-state war goal against each opponent whose relation is missing, or decline; AI successors fail closed. It does not preserve or claim the predecessor's exact war identity or goal.
This documents the scripted promotion path; natural engine civil-war annexation, continuing-front obligations, and runtime ordering still require their own evidence.

`event021_parent_prepare_annex_successor` runs from the vanilla `on_civil_war_end_before_annexation` and `on_annex` contexts, with ROOT as winner and FROM as the annexed country.
Before FROM cleanup, it recognizes a surviving ordinary opposition actor only when its explicit host pointer names FROM, FROM retains the government role, and both countries have matching crisis IDs.
It copies historical receipts and marks succession without annexing, declaring war, or granting an award.
This covers natural engine victory before the next bounded settlement review; Event 006 independence actors and unrelated annexers do not receive ordinary-successor status.
The subsequent lifecycle helper owns surviving-front pointer transfer. The ordinary-successor external-war helper keeps an idempotent snapshot of the predecessor's live enemy relations across the repeated pre-annex/annex callbacks and dispatches dynamic player goal choices only after successful roster adoption; the exact named wars are not continued, and runtime ordering remains Needs Testing.

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
The existing failure branch consumes the remaining selection budget.
On success, `event021_parent_remove_scenario_target_tickets` traverses the complete scope array into a separate retained-ticket array, then rebuilds the pool after iteration.
It removes all selected-country tickets and preserves every other ticket's order and multiplicity without changing base major/load weights or the draw budget.
The exact 2,005-entry arithmetic fixture retains FRA's 999 and BRA's 1,002 tickets and removes all four GER tickets; the previous numeric traversal left three GER tickets.
This is a source/arithmetic uniqueness check, not engine execution or a numeric campaign probability certificate.
The flag is cleared after the loop and the regular target expires with the event chain.
No delayed event reads the draw flag.
