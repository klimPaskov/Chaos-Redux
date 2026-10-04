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
`missiles_establish_secondary_site` runs in COUNTRY scope at mission completion and registers only its stored `missiles_pending_site_state`; it never evaluates state triggers against the country.
The natural-disaster adapter applies its readiness, command, guidance-backlog, and false-warning penalties to the controller from the unscoped temporaries it calculated, because a temporary variable cannot be read through `PREV.`.
