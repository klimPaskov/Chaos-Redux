# Missile operations lifecycle contracts

`032_missiles_operations_effects.txt` owns missile operation calculations, damage receipts, capture/inheritance transactions, and warning closure.

Scratch temporaries are unscoped; a helper output must already be initialized by its consuming caller to survive that helper's return.
The reach stage, reserve-after-operation and AI reserve floor, four guidance components, population cap, disaster reserve loss calculation, ally half threshold, warning schedule days, inherited/captured reserve amount, civil-war site pool and child reserve, and annex site receipt are initialized before their reads on each applicable execution path.
Their consumers copy durable results into country/state variables before return; they are not presence sentinels.
Training contribution is read only inside its initializing training branch.
The capture caller initializes `missiles_captured_reserve_amount` before `missiles_transfer_captured_reserve` calculates it, then caps, debits, and credits that exact result.
The separate caller-owned `missiles_recaptured_reserve_amount` moves an existing sealed receipt from the former controller's held ledger before the new controller receives it.
Both biological reservation and direct consumption initialize `missiles_biological_payload_debit_proof` before the debit helper, so a successful physical debit remains visible when the caller records escrow or consumption.
Warning scheduling consumes its temporary duration when queuing `chaosx.nr32.82`; the delayed event uses stored warning dates and recomputes the duration on a later scheduling call.
Nested helpers do not read any of these names after their terminal use without a fresh initializer; loop iterations recompute their scratch values.
No manual temporary-clear effect exists.

## Physical custody and site-loss transactions

`missiles_rebalance_site_custody` runs in the programme COUNTRY and projects its available `missiles_operational_reserve` onto its controlled registered sites.
Its STATE iterator uses `PREV` for the owning country, so a foreign event `ROOT` cannot receive the allocation or have its stock changed.
Foreign-controlled stale entries are skipped without clearing that other controller's physical stock.
`missiles_site_can_hold_program_reserve` is a STATE-only storage predicate for scuttled, captured, rogue and destroyed conditions; callers separately prove control.
`missiles_site_can_receive_project` combines that same predicate with its existing `ROOT` control requirement.

For a live matching operation receipt, each site's free storage room is `capacity - operation allocation`, floored at zero.
Preparation writes the operation markers before projecting free custody.
The durable country output `missiles_unallocated_reserve` records free missiles not assigned to any usable site; it is part of the aggregate reserve, not a second grant or spendable pool.
For valid whole-number input ledgers, site free stock plus matching escrow fits capacity and site free stock plus unallocated reserve equals the country's available reserve.
The helper grants and destroys nothing and clears its remaining-stock scratch variable before return.
Removed-country cleanup clears the unallocated projection.

`missiles_settle_lost_site_allocation` consumes the exact STATE target `missiles_lost_allocation_site` and caller-initialized temporary `missiles_allocation_loss_mode`.
It validates the uncommitted operation/site identity, returns the operation reservation, debits the lost site's assigned missiles in loss mode, then clears the operation receipt.
During that sequence `missiles_site_settlement_in_progress` suppresses cleanup's network/custody/phase refresh so the outer capture, scuttle, isolation or disaster transaction can still consume the site's original free-stock snapshot.
The flag is cleared before return; every caller finishes the physical mutation before its final controller-bound refresh, and isolation explicitly restores its phase.
Normal cancellation retains immediate cleanup refresh.
This example starts with 12 free missiles and 4 assigned to a capacity-10 site: that site holds 6 free and 4 assigned, a second capacity-10 site holds the remaining 6 free, and destruction loses precisely the first site's 10 missiles while leaving 6.

On recapture, sealed stock is bounded by both the physical site's held receipt and the former controller's `missiles_captured_reserve_held` ledger.
That amount is debited from the former held ledger before the site receipt is replaced, then added to the new captured receipt after the ordinary-reserve debit.
It never passes through the former controller's available reserve.
The controller-id guard prevents repeat callbacks from transferring it twice.

`missiles_recalculate_network` accumulates into the current country through `PREV` inside its controlled states, including when an attacker originated the event.
Incoming site-damage recording validates `missiles_incoming_damage_state` as an event target controlled by the recipient and copies the damage facts directly from that state's receipt before its producer clears them.
The final `chaosx.nr32.7` receiver refreshes the defender's status and phases under the defender's `ROOT`.
No new asset, recurring scan, timer or world-end owner is introduced by these APIs.

`missiles_initialize_scenario_package` consumes country-scoped `missiles_scenario_package_stage`, `reserve`, `readiness`, `control`, and `site_capacity` inputs from `missiles_scenario_apply_country_package`.
Missing inputs retain the helper's existing defaults; a supplied zero readiness or control remains distinct from an absent input.
State iteration deliberately reads `PREV.missiles_scenario_package_site_capacity` from the country owning the transaction.
The scenario adapter clears all nine package input variables at country completion and again in bounded transaction cleanup.

`missiles_close_root_incident` tests the global warning root with `has_event_target` and clears that global target through `clear_global_event_target` after closure.
`missiles_register_conventional_military_losses` uses file-local `@missiles_division_presence_floor = 0` because the `divisions_in_state.size` parser does not support a script-constant token.
The strict greater-than condition and impact-state reference remain intact.
The incident inspection threshold uses existing `missiles_attribution.unknown = 4`; comparison and assigned highly-likely value are unchanged.

These repairs add no helper or call site and change no weighted pool, weight, random draw, duration formula, reserve allocation formula, asset, or localisation.
See `docs/testing/live_qa/20260913_main_menu_startup/script_missile_handoff.md` and its exact-token reference companion for repair evidence and validation limits.

## Evolution consumer contracts

The Event Details shared toggle uses `events_log_disabled_evolution_32_32_<stage>` for the five Event 32 tracks.
`missiles_set_evolution_log_context` (input temp `missiles_evolution_log_stage_input`, a `missiles_evolution` value) sets `events_log_evolution_event_id` to the event id, `events_log_evolution_type` to `missiles_event.evolution_type` (32), `events_log_evolution_stage` to the catalog number, and `events_log_evolution_tier` to the track's tier constant; the unlock record and the commit gate both call it, so the shared gate and the logged row name the same track.
The `missiles_*_enabled` triggers read that flag without changing any state.
The matching `missiles_*_active` triggers also require the retained country adoption receipt.
They are country-scoped read-only gates and hide implementation flag names from player requirements.
Absent disable flags mean enabled, while absent adoption receipts mean inactive.

`missiles_operation_tracks_are_enabled` consumes the frozen strike profile, operation type, payload, rogue provenance, and current enable/adoption state.
It gates saturated, special-payload, automatic-response, and rogue-origin operations at preparation and commitment, while conventional ordinary operations remain independent of those tracks.
`missiles_operation_has_reliable_payload_custody` retains its policy, integration, and exact site-custody requirements and rejects special delivery when its track is inactive.

`missiles_create_operation_receipt` records `missiles_operation_rogue_origin` before the transient bypass flag clears.
The origin persists only for that operation and `missiles_cleanup_operation` clears it with the operation receipt.
Disabling Rogue Launch Commands therefore cannot let a queued strategic operation lose its rogue identity and bypass the track gate.
Disabled rogue timeouts close their incident while retaining compromise and without launching or transferring inventory.
Disabled scheduled automatic responses settle their existing queue receipt through the warning resolver without creating a launch.

AI preferences refresh at operation preflight so an obsolete retained evolution profile cannot govern a new operation.
Physical cap and inheritance records remain retained adoption data, and suspension changes neither site custody nor stockpiles.
Validation and the same-scenario probability evidence limits are recorded in `docs/plans/032_missiles_plans/032_evolution_toggle_binding_repair_2026-10-03.md`.

## Stored dates

Every Event 032 due date, deadline, cooldown, and expiry is a stored date: `global.date` plus an offset in date units, where one game hour is 0.00001.
Day counts from script constants or day variables pass through the shared `chaosx_convert_days_to_date_offset` helper before they are added, and the caller sets `chaosx_date_offset` before each call.
This covers the five evolution due dates, the rogue crisis deadline and incident cooldown, survey, secondary-site, repair and warning-verification due dates, the operation ready date, the launch cooldown, the warning expiry and response dates, the retaliation delay, and the achievement deadlines in `032_missiles_achievement_effects.txt`.
`missiles_set_warning_deadlines` is the single COUNTRY-scope writer of a new warning's expiry and posture-dependent response dates, used by operation impact warnings and by the Retaliation Network scenario seed.
`missiles_schedule_warning_response` converts the remaining warning window back to whole days with `chaosx_convert_date_offset_to_days` before it delays `chaosx.nr32.82`, and still waits at least one day.
The Long Reach hold compares the elapsed date offset with the converted 180-day offset, and records the elapsed whole days in `chaosx_032_long_reach_clock_days`.
Native `days =` fields, mission timeouts, and timed flags stay in days.

## Scope-bound writes

`missiles_suspend_damaged_site` runs in the damaged STATE and writes the repair flags, incident site, and repair due date on its program country `ROOT`, where the repair mission and cleanup read them.
`missiles_establish_secondary_site` runs in COUNTRY scope at mission completion and registers only its stored `missiles_secondary_site_state`; it never evaluates state triggers against the country.
The natural-disaster bridge runs every programme write under the site controller's ROOT; its readiness, command, guidance-backlog, and false-warning penalties are applied inside that ROOT block from the unscoped temporaries it calculated, because a temporary variable cannot be read through `PREV.`.

## Natural-disaster bridge (Event 013)

Event 013's state-scope building-damage helper `natural_disaster_apply_family_building_damage`, which serves the primary, repeated, neighbour, and chain-arrival impacts, ends with one guarded call: `if = { limit = { missiles_state_has_registered_site = yes } missiles_natural_disaster_damage_site = yes }`.
`missiles_natural_disaster_damage_site` (STATE scope, ROOT is Event 013's ROOT) validates the registered site and its proven controller, reads the impact severity from Event 013's unscoped temporary `natural_disaster_current_severity` with `check_variable` only, stores the strongest pending severity on the state as `missiles_disaster_pending_severity`, queues the state in the controller's `missiles_disaster_pending_sites` array, and fires the hidden immediate receiver `chaosx.nr32.9` on the controller; it makes no programme write.
`missiles_process_natural_disaster_receipts` (COUNTRY, ROOT is the controller) applies `missiles_apply_natural_disaster_site_damage` to every queued state once and empties the queue, so a second receiver for the same impacts does nothing.
`missiles_apply_natural_disaster_site_damage` (STATE, ROOT is the controller) revalidates control, settles the percentage reserve loss through `missiles_remove_reserve`, settles a reserving order through `missiles_settle_lost_site_allocation` (refund mode, or loss mode when the hit wrecks the site), applies site damage and capacity loss, settles a wreck once through `missiles_scuttle_site_from_current_controller`, and then applies the controller's readiness, command, guidance-backlog, and false-warning losses, the repair request, a site-damage incident when none is open (its phase offers suspension and repair), network, custody, phase, and achievement updates; the pending severity is always cleared.
Severity tiers use `natural_disaster_severity` (local 1 to abnormal 5) and the loss table `missiles_natural_disaster`. A disaster never unlocks an evolution, and Event 013 keeps its own history, deaths, and reports.
`.tools/test_event32_state_scope.py` (`NaturalDisasterBridge`) pins the Event 013 call, the queue-only adapter, the receiver, and the controller-ROOT routing.

## Site and command project missions

Six native missions are goal-style projects: survey, secondary-site construction, site repair, rogue-site recovery, warning verification, and retaliation-network restoration.
Each activating decision first calls its COUNTRY-scope begin effect, which stores the project's own state pointer, sets its in-progress flag, and stamps a converted due date from `missiles_evolution_timing`; the decision activates the mission only when that flag is set.

| Mission | Begin effect | Stored state | Due date (days) | Completion effect | Cancel and timeout effect |
| --- | --- | --- | --- | --- | --- |
| Launch-State Survey | `missiles_begin_survey` | `missiles_survey_site_state` | `survey_mission_days` (60) | `missiles_complete_survey` registers the surveyed state as a launch site | `missiles_cancel_site_survey` |
| Secondary-Site Construction | `missiles_begin_secondary_site` | `missiles_secondary_site_state` | `secondary_site_mission_days` (90) | `missiles_establish_secondary_site` registers the site and sets `missiles_secondary_site_established` | `missiles_cancel_secondary_site_project` |
| Launch-Site Recovery (repair) | `missiles_suspend_damaged_site` (STATE) | `missiles_repair_site_state` | `repair_mission_days` (45) | `missiles_complete_site_repair` calls `missiles_finish_site_repair`: damage cleared, one capacity-recovery step, site active again | `missiles_cancel_site_repair_project` releases the suspended site in its current condition |
| Rogue-Site Recovery | `missiles_begin_site_recovery` | `missiles_recovery_site_state` | `site_recovery_mission_days` (14) | `missiles_complete_site_recovery` retakes the site and closes the rogue incident | `missiles_cancel_site_recovery_project` |
| Warning Verification | `missiles_verify_warning` | none | `warning_response_days` (3) | `missiles_complete_warning_verification` verifies or exposes the warning | `missiles_cancel_warning_verification` |
| Retaliation-Network Restoration | `missiles_begin_network_restoration` | none | `network_restore_days` (60) | `missiles_restore_retaliation_network` clears severance and returns to Supervised when the network is available | `missiles_cancel_network_restoration` |

The mission `available` blocks combine the matching `*_is_due` trigger with the project's objective: the surveyed or construction state is still owned, controlled, and suitable; the repair site is still controlled and not captured, rogue, or scuttled; the same country-owned garrison and current recovery receipt apply to both humans and AI; the warning is still actionable; or Command Control, readiness, an active site, and the absence of a rogue command allow restoration.
Survey success additionally requires a fully funded current payer/site receipt, and cancellation returns its observed unused payment according to purchased progress.
Cancel triggers depend on the project and its objective, never on the current program phase, so a war, peace, incident, or warning does not abort unrelated construction or repair.
A suspended site carries `missiles_site_suspended`, which `missiles_site_can_launch` rejects; routine `missiles_restore_readiness` maintenance leaves a site under an active repair mission to that mission.
`.tools/test_event32_project_missions.py` pins the producer, due-date, timeout, completion, and cancellation contract for all six missions.

## Captured-site resolution

`missiles_handle_site_control_changed` marks a captured site with `missiles_site_captured`, credits its surviving reserve to the new controller's `missiles_captured_reserve_held`, sets `missiles_captured_site_unresolved`, and selects the decision focus with `missiles_select_next_captured_site`.
The handler runs in STATE scope with ROOT as the new controller and never reads FROM, which can resolve to the state inside that block.
Its caller binds the former controller as the regular event target `missiles_capture_former_controller`: `on_state_control_changed` saves the on_action's own FROM before entering `FROM.FROM`, and `missiles_reconcile_released_country_sites` saves each site's stored `missiles_site_current_controller`, because the release on_action's FROM is the releasing overlord rather than the site's last holder.
The handler requires that target to exist as a country other than ROOT and uses it for every former-controller read and write; the target clears when the callback chain ends.
Every write of `missiles_site_controller_id` stores the same country in `missiles_site_current_controller`, and every reset clears it, so the release pass always has the site's last holder.
The four STATE-scope resolutions are `missiles_guard_captured_site`, `missiles_study_captured_site`, `missiles_integrate_captured_site`, and `missiles_scuttle_captured_site`; each is gated by `missiles_site_awaits_capture_resolution` so a state resolves once.
Guard and study set `missiles_site_capture_resolved` and keep the site isolated and inactive with its weapons still held; integration clears the capture and moves `missiles_site_captured_reserve` into Operational Reserve once; scuttling reuses `missiles_scuttle_site`, which debits the held receipt once and retires the state.
Every route ends in `missiles_finish_captured_site_resolution`, which refocuses the next awaiting state, clears `missiles_captured_site_unresolved` when none remains, and closes the current incident only when it is the site-capture incident.
Lifecycle code that runs under another country's ROOT (the former controller in the capture handler, and the controller in `missiles_scuttle_site_from_current_controller`) fires the immediate hidden receiver `chaosx.nr32.7`, whose `missiles_refresh_program_from_receiver` recalculates that country's network, custody, captured-site marker, and requested rogue closure with ROOT bound correctly.
`missiles_cleanup_operation` matches site allocations against `PREV.missiles_active_operation_id`, so it clears the right markers when another country's ROOT calls it.
`.tools/test_event32_captured_sites.py` pins the decision, resolution, reserve, budget, and receiver contract.

## Special-payload reservation

`missiles_reserve_operation_resources` calls `missiles_reserve_operation_payload` once the missile escrow is accepted; a refused warhead returns the missile escrow through `missiles_refund_operation_reserve` and rejects the order.
Nuclear and thermonuclear warheads are held with `add_nuclear_bombs`, biological warheads through `missiles_debit_biological_payload`; both record `missiles_operation_payload_escrow`, its type, the biological agent, and `missiles_operation_payload_escrow_active`.
Chemical preparation calls `missiles_reserve_chemical_payload_receipt`, which freezes the exact agent and obtains a CBRN-owned receipt for the measured stock debit, operation nonce, source site and target.
`missiles_commit_operation` requires the same full receipt and current technology, policy, profile and physical custody; replacement free stock is neither required nor debited at launch.
A refused commitment aborts without consequences, returns the missile allocation and records `missiles_preparation_failure.chemical_agent`.
Chemical consumption closes the held receipt once and supplies its frozen agent and paid quantity to the shared consequence pipeline.
Cancellation recovers chemical stock only at its intact controlled source; capture transfers sealed custody, proven destruction discards the held quantity, and isolation or uncertain recovery retains a pending CBRN receipt.
Repair, captured-site integration and country-removal hooks settle the same exact-site records, including partial or orphaned receipts, without creating replacement payloads.
Reserved chemical stock remains visible to shared stockpile inspections and proportional destruction, and unresolved native measurements cannot earn compliance rewards.
The API and its evidence limits are documented in [Chemical payload reservations](../../docs/systems/cbrn_warfare/chemical_payload_reservations.md).
Nuclear and biological escrow still use their separate owners; their physical loss and succession audit remains open and is not established by the chemical receipt tests.
`.tools/test_event32_special_payload.py` pins the order decisions, event wiring, reservation, release, and consumption contract.

## Paid site work and loyal recovery

The [site-work transaction contract](../../docs/events/032_missiles/systems/site_work_transactions.md) documents payment, native quantity measurements, progress refunds, context identity and cleanup.
`missiles_begin_survey` delegates to the paid survey owner; its completion requires a funded current receipt and due valid state, and cancellation settles the original payer before active fields are cleared.
`missiles_begin_site_recovery` requires the accepted concrete two-owned-division garrison and inclusive quote before charging once and storing its actor/site/rogue context.
`missiles_complete_site_recovery` rechecks that exact context, due date and garrison before any recovery reward or crisis closure.
Country removal and ordinary rogue closure retire the appropriate project and native mission; survey balances that lack a measured credit remain pending instead of being copied to a successor.
The native resource readers, shared cost dispatch and actor-owned output lifetimes are detailed in the linked contract.

## Evolution pacing

The [evolution pacing contract](../../docs/events/032_missiles/systems/evolution_pacing.md) documents finite observations, native clocks, exclusive waiting modes, queue receipts, setting changes and validation limits.
`missiles_register_program` retains live membership in `global.missiles_program_registry`; exact initialization/removal and settled programme/world mutations notify one coalesced `chaosx.nr32.192` observation.
`missiles_measure_evolution_pressure` publishes durable global counts, ratios, date and generation, distinguishes operational/mature/response capability and counts unordered hostile pairs once.
`missiles_evaluate_evolution_unlocks` observes and arms or disarms; it never commits merely because an ordinary deadline elapsed.
Native MTTH events `.201` through `.205` use the live day scales from `common/mtth/032_missiles_evolution_mtth.txt`, and their recurring gates perform no registry iteration.
Only the first-high-chaos exception uses finite `.190` due dates, with earliest-job coalescing, obsolete-host rejection and seven-day spacing for overdue successful commitments.
Retired `.191` deliveries and the unused watch API are cancellation sinks, not polling fallbacks.
A fresh precommit observation, the shared enabled gate and the recorder's fresh acknowledgement protect once-only actorless logging and `.8` country adoption dispatch.
Native changes without a supported exact notification remain discoverable at a later permitted pulse, not continuously; native trigger-check latency and source-model/MCP limitations remain explicit.

## Whole-missile site allocation

`missiles_reserve_operation_resources` calls `missiles_project_operation_site_allocations`, a bounded water-fill over `missiles_operation_sites` that writes whole `missiles_site_planned_allocation` values summing to `missiles_operation_missile_cost`; `missiles_operation_projected_site_allocations_fit` requires the projection and the summed launchable capacity to cover the cost.
`missiles_mark_operation_sites_reserved` copies each planned allocation to `missiles_site_operation_allocation` and removes a site that received none; `missiles_operation_sites_remain_valid` checks each site's operation id, a positive allocation, and capacity.
`missiles_settle_lost_site_allocation` (COUNTRY scope, regular target `missiles_lost_allocation_site`, temp `missiles_allocation_loss_mode`) ends a prepared operation tied to a lost site and, in loss mode, debits that site's exact allocation once after the abort refund; capture, scuttling, destruction by strike, and a wrecking natural disaster call it.

## Repair-programme isolation

`missiles_state_has_registered_site` includes `missiles_site_suspended`, so a site under its repair programme is still struck, captured, inherited, split, and cleaned up like any registered site.
`missiles_record_incoming_operation_site_damage` writes the repair flags and `missiles_site_repair_due_date` only when no `missiles_site_repair_mission` is active, and `missiles_country_can_start_survey` waits for that mission, so damage elsewhere never postpones or cancels a running repair.
A transferred site leaves its former owner's programme unsuspended: `missiles_handle_site_control_changed`, `missiles_finalize_civil_war_split_child`, `missiles_finalize_planned_inheritance`, and both receipts in `missiles_cleanup_removed_country` clear `missiles_site_suspended` while marking the site compromised and isolated, so `missiles_site_can_be_suspended` lets the new controller repair it; `missiles_finalize_civil_war_split_parent` keeps the parent's own suspended site under its running programme.
The former owner's repair and recovery missions cancel through `NOT = { missiles_repair_target_is_valid = yes }` and `NOT = { missiles_recovery_target_is_valid = yes }` once the state is lost; `missiles_cancel_site_repair_project` releases a suspended site only while `ROOT` still controls it, then clears its own flags, due date, and pointer, and `missiles_cancel_site_recovery_project` clears only its own flag, due date, and pointer.

## Rogue site pointer and isolation

`missiles_select_rogue_incident_site` writes the candidate into `missiles_rogue_site_state` (never `missiles_incident_site`) and leaves an open crisis's pointer alone; a candidate that opens no crisis is cleared by the firing evaluation and the Command Breakdown scenario seed.
`missiles_open_rogue_incident` records `missiles_rogue_site_id` from that pointer, and the launch, timeout, custody-payload, recovery, and achievement paths read `missiles_rogue_site_state`, so a damage, disaster, or capture incident opened during the crisis keeps `missiles_incident_site`.
`missiles_close_rogue_incident` closes the general incident record (`missiles_last_incident_closed`, `missiles_incident_active`, `missiles_active_incident_id`) only while the current incident type is rogue preparation or rogue launch, and never clears `missiles_incident_site`.
`missiles_site_is_rogue_incident_site` (STATE, ROOT is the programme) matches the recorded site by id; the rogue isolate and scuttle decisions target it from `missiles_launch_site_states`, and `missiles_isolate_site`, `missiles_scuttle_site`, and `missiles_scuttle_site_from_current_controller` close the crisis only for that site.
`missiles_isolate_site` settles a reserving order through `missiles_settle_lost_site_allocation` in refund mode before isolating, and `missiles_refresh_site_flags` never re-hardens an isolated site; `missiles_site_can_be_suspended` accepts isolated sites and `missiles_finish_site_repair` lifts the isolation.
`missiles_site_suspension_is_offered` also covers the establishment phase (outside a capture shell), because a program whose only sites are isolated or damaged has no working site and falls back to establishment; without it a single-site program could never repair its isolated site.
`missiles_isolate_retaliation_site` lets a human cut off any working site, while its AI weight is zero for a site that is not compromised.
`missiles_cleanup_removed_country` releases the removed country's open rogue crisis from `global.missiles_rogue_active_incidents` and clears its rogue site pointer and id.
`.tools/test_event32_captured_sites.py` (`RogueSiteResolution`) pins these contracts.

## Retaliation warning responses

`missiles_retaliation_response_can_be_accepted` (COUNTRY scope) is the single gate for every route that answers a warning: the `chaosx.nr32.80` accept option, the Accept the Current Response decision, and the Delegated or Automatic posture in `missiles_process_scheduled_warning_response`.
It requires an actionable warning not yet answered, the chain caps, an open retaliation launch slot, a launch-capable controlled site, the retaliation reserve, and `missiles_country_can_prepare_operation`; `missiles_accept_retaliation_response` uses it as its limit.
`missiles_accept_retaliation_response` saves the current target choice with `missiles_save_target_choice_for_retaliation` (including `missiles_pending_target_state` and `missiles_requested_target_profile`) before writing the attacker, and clears that pending state and requested profile when the attacker is not the saved enemy, as `missiles_select_target` does; when `missiles_operation_preflight_result` is not accepted it clears the pending parent, root, root-country, and generation values and the retaliation operation type, strike profile, payload, and target-state id, then `missiles_restore_target_choice_after_retaliation` restores the saved enemy, objective, target state, and objective lock or calls `missiles_clear_target` when there was none; the warning is not resolved and no outcome flag is set.
`missiles_clear_warning_outcome_flags` clears the per-warning outcome flags (`missiles_warning_delayed`, `missiles_warning_false_or_conflicting`, `missiles_warning_expired_without_launch`, `missiles_retaliation_response_accepted`) when a warning opens, when it resolves, and in removed-country cleanup; each route sets its outcome flag after `missiles_resolve_warning_queue_receipt`, so the record describes the last warning only.
`missiles_false_warning_history` is the long-term record and is never cleared by a new warning.
`.tools/test_event32_retaliation_warning.py` pins the shared gate, the clearing points, and the outcome ordering.
