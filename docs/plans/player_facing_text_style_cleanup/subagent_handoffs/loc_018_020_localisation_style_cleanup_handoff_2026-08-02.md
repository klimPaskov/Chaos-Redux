# Localisation style cleanup handoff for Events 018, 019, and 020

## Scope

This pass covered the English localisation files whose names begin with `018_`, `019_`, or `020_`.

The pass preserved gameplay meaning, localisation keys, formatting tokens, dynamic scopes, and sourced quotations.

The required repository guidance, Chaos Redux event guidance, subagent guidance, offline Paradox localisation references, and vanilla localisation documentation were reviewed before editing.

## Changed files

- `localisation/english/018_random_resource_l_english.yml`
- `localisation/english/018_resources_found_decisions_l_english.yml`
- `localisation/english/018_resources_found_system_l_english.yml`
- `localisation/english/019_infrantry_spawn_l_english.yml`
- `localisation/english/020_black_plague_evolutions_l_english.yml`
- `localisation/english/020_black_plague_rat_decisions_l_english.yml`
- `localisation/english/020_black_plague_rat_focus_l_english.yml`
- `localisation/english/020_black_plague_reports_l_english.yml`
- `localisation/english/020_black_plague_response_l_english.yml`
- `localisation/english/020_black_plague_scenario_l_english.yml`
- `localisation/english/020_black_plague_super_events_l_english.yml`
- `localisation/english/020_black_plague_weaponization_l_english.yml`

`020_black_death_l_english.yml` and `020_black_plague_rat_countries_l_english.yml` were reviewed and did not require edits.

## Changed key groups

Event 018 received prose cleanup for survey, contract, cave, and Oth-Kesh reports, plus clearer resource decision tooltips and system descriptions.

Event 019 received a concise formation-origin report at `chaosx.nr19.918.d`.

Event 020 evolution, focus, decision, report, response, scenario, super-event, and weaponisation surfaces received prose cleanup.

The Event 020 scenario report variants retain all original scenario counter tokens while presenting them as world-state information.

The Event 020 super-event description at `chaosx_super_event.87.d` now uses the approved aftermath wording.

The exact changed keys are `chaosx.nr18.2.d`, `chaosx.nr18.4.d`, `chaosx.nr18.54.d`, `chaosx.nr18.55.d`, `chaosx.nr18.58.d`, and `chaosx.nr18.7.d` in Event 018.

The exact changed keys are `resources_found_begin_partial_closure_decision_tt`, `resources_found_cave_containment_rivalry`, `resources_found_cave_prepare_world_end_ruptures_tt`, `resources_found_cave_release_raiding_broods_tt`, `resources_found_install_heavy_machinery_desc`, and `resources_found_maximum_shifts_desc` in the Event 018 decision file.

The exact changed keys are `DHO_consume_captured_industry_desc`, `DHO_mark_the_richest_route_desc`, and `DHO_study_broken_weapons_desc` in the Event 018 system file.

The exact changed key is `chaosx.nr19.918.d` in Event 019.

The exact changed keys are `black_plague.evolution.stage_5.prefire.body` and `black_plague.evolution.summary` in the Event 020 evolution file.

The exact changed keys in the Event 020 Rat decisions file are `black_plague_rat_devour_rival_desc`, `black_plague_rat_king_close_the_harbors_terminal_desc`, `black_plague_rat_king_crown_the_continent_cost`, `black_plague_rat_king_crown_the_continent_cost_blocked`, `black_plague_rat_king_crown_the_continent_mission_desc`, `black_plague_rat_king_execute_terminal_takeover_cost`, `black_plague_rat_king_execute_terminal_takeover_cost_blocked`, `black_plague_rat_king_execute_terminal_takeover_desc`, `black_plague_rat_king_mark_terminal_preparation_cost_blocked`, `black_plague_rat_king_select_target_continent_cost_blocked`, `black_plague_rat_king_select_target_continent_desc`, and `black_plague_rat_king_send_the_royal_strike_cost`.

The exact changed keys are `black_plague_rat_cartography_of_capitals_desc`, `black_plague_rat_cross_sea_cargo_desc`, and `black_plague_rat_four_mouths_desc` in the Event 020 Rat focus file.

The exact changed Event 020 report keys are `chaosx.nr20.20.a`, `chaosx.nr20.3.a`, `chaosx.nr20.3.d`, `chaosx.nr20.3.t`, `chaosx.nr20.44.d`, `chaosx.nr20.45.d.distributed`, `chaosx.nr20.48.d.giant_mutation`, `chaosx.nr20.6.d`, `chaosx.nr20.60.d`, `chaosx.nr20.63.d`, `chaosx.nr20.73.d`, `chaosx.nr20.76.d`, `chaosx.nr20.77.d`, `chaosx.nr20.80.d`, `chaosx.nr20.81.d`, `chaosx.nr20.84.d`, `chaosx.nr20.88.d`, `chaosx.nr20.90.d`, `chaosx.nr20.90.d.high`, `chaosx.nr20.90.d.low`, `chaosx.nr20.90.d.maximum`, `chaosx.nr20.90.d.medium`, `chaosx.nr20.91.d`, `chaosx.nr20.93.d`, `chaosx.nr20.94.d`, and `chaosx.nr20.95.d`.

The exact changed Event 020 response keys are `black_plague_activate_doctor_wu_protocol_desc`, `black_plague_clean_city_rats_complete_tt`, `black_plague_clean_city_rats_desc`, `black_plague_demolish_infested_blocks_complete_tt`, `black_plague_establish_quarantine_cost_tooltip`, `black_plague_establish_quarantine_desc`, `black_plague_raise_army_cordon_cost_tooltip`, `black_plague_request_doctor_wu_access_desc`, `black_plague_shared_last_response_hold_mission_desc`, `black_plague_shared_last_response_refuge_mission_desc`, `black_plague_shared_liberate_and_quarantine_desc`, `black_plague_shared_seal_royal_burrows_mission_desc`, `black_plague_shared_start_last_response_hold_desc`, `black_plague_shared_start_last_response_refuge_desc`, `black_plague_shared_strike_royal_node_desc`, `black_plague_shared_strike_the_crown_desc`, and `black_plague_shared_strike_the_crown_mission_desc`.

The exact changed Event 020 scenario keys are `chaosx.nr20.4.a`, `chaosx.nr20.4.d`, and `chaosx.nr20.4.t`.

The exact changed super-event key is `chaosx_super_event.87.d`.

The exact changed weaponisation keys are `black_plague_weaponization_destroy_stockpile_desc`, `black_plague_weaponization_dual_use_desc`, `black_plague_weaponization_safety_first_desc`, `chaosx_nr20_weaponization.1.d`, `chaosx_nr20_weaponization.2.d.dual_use`, `chaosx_nr20_weaponization.2.d.military_acceleration`, `chaosx_nr20_weaponization.3.d`, `chaosx_nr20_weaponization.3.d.crisis`, `chaosx_nr20_weaponization.4.d`, `chaosx_nr20_weaponization.5.d`, and `chaosx_nr20_weaponization.6.d`.

## Sourced quotation audit

No sourced or attributed quotation key was changed.

The audited sourced quotation keys are `chaosx_super_event.82.q`, `chaosx_super_event.83.q`, `chaosx_super_event.84.q`, `chaosx_super_event.85.q`, `chaosx_super_event.86.q`, and `chaosx_super_event.87.q`.

The Event 020 super-event quotation at `chaosx_super_event.87.q` remains verbatim, including its line break, quotation marks, attribution, and punctuation.

No `.q` key in the owned diff was modified.

The button at `chaosx_super_event.87.a` was not treated as a sourced quotation key, and its selected wording remains aligned with the research handoff.

## Missing key list

No missing key was identified in the direct owned-file localisation key and reference pass.

This is a static localisation-surface result, not a claim that every unrelated script reference in the repository has been exhaustively linted.

## Duplicate key list

No duplicate key was found across the owned 018, 019, and 020 English localisation files.

## Scripted localisation issue list

No new unresolved scripted-localisation method was introduced by this pass.

Existing dynamic methods such as `[resources_found_field_state.GetName]`, `[resources_found_field_state.GetResourcesFoundLastResourceName]`, `[GetBlackPlagueRatKingTargetContinentName]`, and `[black_plague_weaponization_delivery_state.GetName]` were preserved.

Existing constant and variable formatters in Event 020 response and scenario text were preserved.

## Dynamic text opportunities

Event 020 scenario report variants now expose selected-continent, established-state, brood, and royal-basin counters through their existing dynamic tokens.

Several older Event 020 response cost rows still display literal civilian-factory counts such as `£civ_factory §Y1§!` or `£civ_factory §Y2§!` while their decision logic uses tunable factory values.

Those cost rows are a future centralisation opportunity and should be handled with the owning decision or scripted-cost pass.

Event 018 state and resource names already use dynamic scopes and need no new helper for this copyedit.

## Cross-surface mismatch notes

The exact docs/specs/020 file is `docs/specs/020_black_plague_specs/matrices/catalog_update_draft.md`.

Its Scenario Details row still says `A sudden Black Plague crisis spreads across several continents. New outbreaks appear, internal rat basins grow, and a Rat King emerges while the final world-end path remains closed.`

Its Intensity Scaling row still says `Low, Medium, High, and Maximum spread the crisis across more continents, states, brood basins, and Rat King territory while increasing severity. The scenario never creates more than the two established rat countries.`

The docs owner should replace those two `while` constructions with direct sentences while keeping the catalog facts aligned with the runtime strings.

Some older Event 020 report and response keys still use implementation-facing route terms such as `terminal route`, `terminal preparations`, or explicit Evolution gates because those strings describe active gameplay requirements.

The most visible hidden-route wording was reduced in the edited target-continent, terminal-order, scenario, and last-response strings.

The pre-existing `resources_found_cave_containment_rivalry` addition at the end of `018_resources_found_decisions_l_english.yml` was preserved.

## File encoding concerns

All twelve changed localisation files retain UTF-8 with BOM encoding.

Git may report its normal LF-to-CRLF working-tree normalization warning for these files.

## Recommended follow-up fixes

- Rewrite the two docs/specs/020 catalogue sentences identified above in `docs/specs/020_black_plague_specs/matrices/catalog_update_draft.md`.
- Consider a decision-owned dynamic-cost pass for the literal factory counts in `localisation/english/020_black_plague_response_l_english.yml`.
- Review the remaining route-state wording in `chaosx.nr20.64.d`, `chaosx.nr20.66.d`, `chaosx.nr20.68.d`, `chaosx.nr20.83.d`, `black_plague_shared_start_last_response_hold_effect_tt`, and related Event 020 requirement strings if the project wants every internal route label hidden from players.

## Validation

The owned localisation scan reports no semicolons or em dashes after the pass.

The duplicate-key scan reports no duplicates across the owned files.

The source-quotation diff audit reports no changed `.q` key and confirms that `chaosx_super_event.87.q` is unchanged.

UTF-8 BOM checks were run on the changed files.

The changed-key dynamic-token comparison reports no bracket-token differences between the original and edited values.

No live Hearts of Iron IV session or consumer GUI validation was run because live validation remains user-owned.

## Unresolved wording decisions

Natural temporal uses of `while` remain in several gameplay descriptions where they describe an active condition rather than a rhetorical contrast.

Some older route and Evolution labels remain where removing them would risk hiding a real requirement without a connected gameplay tooltip change.

No separate plan handoff was needed beyond this audit handoff.
