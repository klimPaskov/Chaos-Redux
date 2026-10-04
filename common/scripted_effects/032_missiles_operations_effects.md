# Missile operations lifecycle contracts

`032_missiles_operations_effects.txt` owns missile operation calculations, damage receipts, capture/inheritance transactions, and warning closure.

Scratch temporaries are unscoped and live for the enclosing effect evaluation.
The reach stage, reserve-after-operation and AI reserve floor, four guidance components, population cap, disaster reserve loss calculation, ally half threshold, warning schedule days, inherited/captured reserve amount, civil-war site pool and child reserve, and annex site receipt are initialized before their reads on each applicable execution path.
Their consumers copy durable results into country/state variables before return; they are not presence sentinels.
Training contribution is read only inside its initializing training branch.
Capture amount is initialized in `missiles_transfer_captured_reserve` before the caller caps, debits, and credits it; the helper output must remain alive throughout that caller.
Warning scheduling consumes its temporary duration when queuing `chaosx.nr32.82`; the delayed event uses stored warning dates and recomputes the duration on a later scheduling call.
Nested helpers do not read any of these names after their terminal use without a fresh initializer; loop iterations recompute their scratch values.
No manual temporary-clear effect exists.

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

The Event Details shared toggle uses `events_log_disabled_evolution_32_<type>_1` for the five Event 32 tracks.
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
The natural-disaster adapter applies its readiness, command, guidance-backlog, and false-warning penalties to the controller from the unscoped temporaries it calculated, because a temporary variable cannot be read through `PREV.`.

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

The mission `available` blocks combine the matching `*_is_due` trigger with the project's objective: the surveyed or construction state is still owned, controlled, and suitable; the repair site is still controlled and not captured, rogue, or scuttled; loyal divisions stand in the rogue site's state, with AI countries exempt; the warning is still actionable; or Command Control, readiness, an active site, and the absence of a rogue command allow restoration.
Cancel triggers depend on the project and its objective, never on the current program phase, so a war, peace, incident, or warning does not abort unrelated construction or repair.
A suspended site carries `missiles_site_suspended`, which `missiles_site_can_launch` rejects; routine `missiles_restore_readiness` maintenance leaves a site under an active repair mission to that mission.
`.tools/test_event32_project_missions.py` pins the producer, due-date, timeout, completion, and cancellation contract for all six missions.

## Captured-site resolution

`missiles_handle_site_control_changed` marks a captured site with `missiles_site_captured`, credits its surviving reserve to the new controller's `missiles_captured_reserve_held`, sets `missiles_captured_site_unresolved`, and selects the decision focus with `missiles_select_next_captured_site`.
The four STATE-scope resolutions are `missiles_guard_captured_site`, `missiles_study_captured_site`, `missiles_integrate_captured_site`, and `missiles_scuttle_captured_site`; each is gated by `missiles_site_awaits_capture_resolution` so a state resolves once.
Guard and study set `missiles_site_capture_resolved` and keep the site isolated and inactive with its weapons still held; integration clears the capture and moves `missiles_site_captured_reserve` into Operational Reserve once; scuttling reuses `missiles_scuttle_site`, which debits the held receipt once and retires the state.
Every route ends in `missiles_finish_captured_site_resolution`, which refocuses the next awaiting state, clears `missiles_captured_site_unresolved` when none remains, and closes the current incident only when it is the site-capture incident.
Lifecycle code that runs under another country's ROOT (the former controller in the capture handler, and the controller in `missiles_scuttle_site_from_current_controller`) fires the immediate hidden receiver `chaosx.nr32.7`, whose `missiles_refresh_program_from_receiver` recalculates that country's network, custody, captured-site marker, and requested rogue closure with ROOT bound correctly.
`missiles_cleanup_operation` matches site allocations against `PREV.missiles_active_operation_id`, so it clears the right markers when another country's ROOT calls it.
`.tools/test_event32_captured_sites.py` pins the decision, resolution, reserve, budget, and receiver contract.

## Special-payload reservation

`missiles_reserve_operation_resources` calls `missiles_reserve_operation_payload` once the missile escrow is accepted; a refused warhead returns the missile escrow through `missiles_refund_operation_reserve` and rejects the order.
Nuclear and thermonuclear warheads are held with `add_nuclear_bombs`, biological warheads through `missiles_debit_biological_payload`; both record `missiles_operation_payload_escrow`, its type, the biological agent, and `missiles_operation_payload_escrow_active`.
Chemical agent is only proven sufficient by `missiles_check_chemical_payload_stock`, which builds the same CBRN action context as the release-time debit without debiting.
`missiles_consume_special_payload` consumes a held warhead first and clears the escrow before any direct debit path; `missiles_release_operation_payload`, called once from `missiles_cleanup_operation`, returns any warhead still held after an abort, cancellation, invalidation, capture, or removed-country cleanup.
`.tools/test_event32_special_payload.py` pins the order decisions, event wiring, reservation, release, and consumption contract.
