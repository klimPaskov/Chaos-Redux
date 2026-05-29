# Soviet Collapse Focus Rework Audit, Filter Patch, and Layout Handoff

Subagent: Chaos Redux focus tree subagent  
Date: 2026-05-29  
Scope:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`

The audit target is a full rework standard for all Soviet Collapse focus trees in the scoped files. I only patched local defects that were safe inside this fork: invalid focus filters and three endpoint coordinate nudges. Broader route depth, overpowered chaos-country behavior, expansion/coring systems, decision loops, and Ukraine reflow remain parent-owned.

## References Used

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline Paradox wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`.
- Vanilla focus precedent scan: national focus syntax, `ai_will_do`, rewards, prerequisites, and mutual exclusions under `~/projects/Hearts of Iron IV/common/national_focus/`.

## Files Changed

| File | Change |
| --- | --- |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Replaced invalid `FOCUS_FILTER_ARMY`, `FOCUS_FILTER_AIR`, and `FOCUS_FILTER_NAVY` usages with vanilla-valid `FOCUS_FILTER_ARMY_XP`, `FOCUS_FILTER_AIR_XP`, and `FOCUS_FILTER_NAVY_XP`. |
| `common/national_focus/005_soviet_collapse_republics.txt` | Moved `caucasus_soviet_collapse_the_compact_holds_the_ridge`, `moldova_soviet_collapse_republic_of_crossings`, and `moldova_soviet_collapse_the_river_state` down one row to clear same-row prerequisite pathlines outside Ukraine. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_soviet_collapse_focus_rework_audit_filters_layout.md` | This handoff. |

Other modified files in the worktree were outside scope and were not touched.

## Changed Focus IDs

Coordinate fixes:

| Focus id | Before | After |
| --- | --- | --- |
| `caucasus_soviet_collapse_the_compact_holds_the_ridge` | `x = 12`, `y = 7`; same row as prerequisite `caucasus_soviet_collapse_tbilisi_baku_yerevan_talks`. | `x = 12`, `y = 8`; pathline now runs downward. |
| `moldova_soviet_collapse_republic_of_crossings` | `x = 21`, `y = 9`; same row as prerequisite `moldova_soviet_collapse_eastern_buffer_missions`. | `x = 21`, `y = 10`; pathline now runs downward. |
| `moldova_soviet_collapse_the_river_state` | `x = 14`, `y = 10`; became same row with `moldova_soviet_collapse_republic_of_crossings` after the endpoint nudge. | `x = 14`, `y = 11`; pathline now runs downward. |

Filter-only fixes:

- `FOCUS_FILTER_ARMY`: 493 instances changed to `FOCUS_FILTER_ARMY_XP`.
- `FOCUS_FILTER_AIR`: 3 instances changed to `FOCUS_FILTER_AIR_XP`.
- `FOCUS_FILTER_NAVY`: 12 instances changed to `FOCUS_FILTER_NAVY_XP`.
- 505 focus IDs were affected because several focuses already had one valid XP filter beside one invalid generic filter.

Patched filter IDs by tree:

| Tree | Count | Focus ids |
| --- | ---: | --- |
| `FTH_soviet_collapse_focus_tree` | 26 | `FTH_first_guard`, `FTH_stores`, `FTH_rival`, `FTH_doctrine`, `FTH_special_arm`, `FTH_supply`, `FTH_enemy_front`, `FTH_radical_turn`, `FTH_war_plan`, `FTH_dnieper_commune_watch`, `FTH_don_steppe_contacts`, `FTH_free_territory_defense_council`, `FTH_free_rail_communes`, `FTH_commune_supply_ledger`, `FTH_grain_and_rifle_stores`, `FTH_field_hospital_routes`, `FTH_bread_and_rifle_ledger`, `FTH_hidden_doctrine`, `FTH_extreme_gate`, `FTH_tachanka_front`, `FTH_tachanka_column_oaths`, `FTH_black_flag_signal_posts`, `FTH_steppe_airstrips`, `FTH_extreme_path`, `FTH_communes_without_capitals`, `FTH_endgame` |
| `PRA_soviet_collapse_focus_tree` | 7 | `PRA_omsk_station_guard`, `PRA_armored_train_directorate`, `PRA_switchyard_denial_posts`, `PRA_armored_train_schools`, `PRA_claim_the_branch_lines`, `PRA_seize_the_junction_cities`, `PRA_rails_over_capitals` |
| `TSC_soviet_collapse_focus_tree` | 7 | `TSC_the_committee_of_signs`, `TSC_observatory_guard`, `TSC_perimeter_regiments`, `TSC_night_survey_columns`, `TSC_claim_the_impact_zone`, `TSC_sky_over_siberia`, `TSC_starfall_mandate` |
| `RMC_soviet_collapse_focus_tree` | 8 | `RMC_cadres_of_resurrection`, `RMC_blood_oath_requisitions`, `RMC_reliquary_guard`, `RMC_dead_volunteer_columns`, `RMC_hagiographers_of_every_front`, `RMC_claim_the_burial_roads`, `RMC_procession_columns`, `RMC_resurrection_without_state` |
| `DSC_soviet_collapse_focus_tree` | 10 | `DSC_call_the_dead_soldiers_congress`, `DSC_voronezh_rearguard_archives`, `DSC_revenant_staff_line`, `DSC_grave_ordnance_claims`, `DSC_field_hospital_memorials`, `DSC_dead_regiment_columns`, `DSC_maps_of_lost_armies`, `DSC_claim_the_soldiers_road`, `DSC_armies_that_do_not_demobilize`, `DSC_congress_of_the_dead_army` |
| `NRF_soviet_collapse_focus_tree` | 12 | `NRF_signal_from_lost_convoys`, `NRF_murmansk_dead_muster`, `NRF_arkhangelsk_ice_registers`, `NRF_revenant_admiralty`, `NRF_salvage_the_dark_berths`, `NRF_icebound_marine_guard`, `NRF_dead_convoy_supply_board`, `NRF_ghost_convoy_escorts`, `NRF_maps_of_sunken_routes`, `NRF_claim_the_white_sea_lane`, `NRF_fleet_that_does_not_dock`, `NRF_northern_revenant_fleet` |
| `ICD_soviet_collapse_focus_tree` | 8 | `ICD_commissars_who_do_not_die`, `ICD_black_seal_requisitions`, `ICD_funeral_guard`, `ICD_memorial_battalions`, `ICD_archives_of_every_front`, `ICD_claim_the_unburied_front`, `ICD_grave_columns_march`, `ICD_commissariat_without_end` |
| `BSC_soviet_collapse_focus_tree` | 22 | `BSC_first_guard`, `BSC_stores`, `BSC_rival`, `BSC_doctrine`, `BSC_special_arm`, `BSC_caravan_officer_schools`, `BSC_supply`, `BSC_enemy_front`, `BSC_war_plan`, `BSC_desert_pass_offices`, `BSC_caravan_supply_hubs`, `BSC_well_guard_posts`, `BSC_hidden_road_depots`, `BSC_kyrgyz_raid_watch`, `BSC_central_asian_defense_council`, `BSC_raiding_column_oaths`, `BSC_pack_train_signals`, `BSC_desert_airstrips`, `BSC_radical_turn`, `BSC_hidden_doctrine`, `BSC_extreme_gate`, `BSC_extreme_path` |
| `TNC_soviet_collapse_focus_tree` | 21 | `TNC_first_guard`, `TNC_stores`, `TNC_rival`, `TNC_doctrine`, `TNC_special_arm`, `TNC_railway_officer_schools`, `TNC_supply`, `TNC_enemy_front`, `TNC_war_plan`, `TNC_canal_guard_posts`, `TNC_oasis_supply_hubs`, `TNC_southern_pass_offices`, `TNC_kyrgyz_contact_posts`, `TNC_central_asian_defense_council`, `TNC_city_militia_charter`, `TNC_timetable_signal_bureaus`, `TNC_airfields_for_the_council`, `TNC_radical_turn`, `TNC_hidden_doctrine`, `TNC_extreme_gate`, `TNC_extreme_path` |
| `ALA_soviet_collapse_focus_tree` | 20 | `ALA_first_guard`, `ALA_stores`, `ALA_rival`, `ALA_doctrine`, `ALA_special_arm`, `ALA_alash_officer_schools`, `ALA_supply`, `ALA_enemy_front`, `ALA_war_plan`, `ALA_rail_spine_to_south`, `ALA_kyrgyz_pass_guards`, `ALA_depot_cavalry_columns`, `ALA_mobile_airstrips`, `ALA_steppe_supply_hubs`, `ALA_officer_oath_boards`, `ALA_border_minority_patrols`, `ALA_radical_turn`, `ALA_hidden_doctrine`, `ALA_extreme_gate`, `ALA_extreme_path` |
| `BBH_soviet_collapse_focus_tree` | 28 | `BBH_first_guard`, `BBH_stores`, `BBH_rival`, `BBH_doctrine`, `BBH_foreign_fear_mediation`, `BBH_black_banner_war_council`, `BBH_special_arm`, `BBH_column_schools`, `BBH_supply`, `BBH_enemy_front`, `BBH_war_plan`, `BBH_mobile_court_posts`, `BBH_armored_car_raids`, `BBH_prison_break_networks`, `BBH_roving_artillery_crews`, `BBH_scorched_prison_roads`, `BBH_radical_turn`, `BBH_captured_rail_stores`, `BBH_column_supply_ledgers`, `BBH_red_and_black_depots`, `BBH_field_hospital_columns`, `BBH_hidden_doctrine`, `BBH_black_column_registers`, `BBH_railway_state_sabotage`, `BBH_borderless_column_schools`, `BBH_banner_without_borders`, `BBH_extreme_gate`, `BBH_extreme_path` |
| `KRS_soviet_collapse_focus_tree` | 19 | `KRS_first_guard`, `KRS_stores`, `KRS_rival`, `KRS_doctrine`, `KRS_special_arm`, `KRS_enemy_front`, `KRS_war_plan`, `KRS_petrograd_signal_watch`, `KRS_sailor_worker_defense_council`, `KRS_convoy_escort_ledger`, `KRS_fortress_hospital_stations`, `KRS_gulf_battery_posts`, `KRS_naval_infantry_oaths`, `KRS_red_fleet_signal_posts`, `KRS_gulf_mine_watch`, `KRS_coastal_air_patrols`, `KRS_port_guard_schools`, `KRS_every_harbor_a_soviet`, `KRS_endgame` |
| `UDC_soviet_collapse_focus_tree` | 26 | `UDC_first_guard`, `UDC_stores`, `UDC_rival`, `UDC_doctrine`, `UDC_special_arm`, `UDC_emergency_staff_college`, `UDC_front_dispatch_school`, `UDC_military_district_passes`, `UDC_mobile_order_columns`, `UDC_counter_secession_cells`, `UDC_radio_command_posts`, `UDC_no_unit_left_unassigned`, `UDC_every_district_a_command`, `UDC_supply`, `UDC_staff_car_workshops`, `UDC_enemy_front`, `UDC_war_plan`, `UDC_command_bunker_vaults`, `UDC_loyal_train_orders`, `UDC_league_observer_corridors`, `UDC_signal_truck_yards`, `UDC_winter_order_routes`, `UDC_radical_turn`, `UDC_hidden_doctrine`, `UDC_extreme_gate`, `UDC_extreme_path` |
| `SDZ_soviet_collapse_focus_tree` | 26 | `SDZ_first_guard`, `SDZ_stores`, `SDZ_rival`, `SDZ_doctrine`, `SDZ_special_arm`, `SDZ_internal_troop_school`, `SDZ_informant_cipher_schools`, `SDZ_checkpoint_identity_cards`, `SDZ_internal_troop_convoys`, `SDZ_black_site_transfer_logs`, `SDZ_radio_intercept_rooms`, `SDZ_no_file_burned_order`, `SDZ_every_office_a_watchpost`, `SDZ_supply`, `SDZ_document_cart_workshops`, `SDZ_enemy_front`, `SDZ_war_plan`, `SDZ_archive_bunker_vaults`, `SDZ_prison_train_ledgers`, `SDZ_league_inspection_corridors`, `SDZ_signal_van_yards`, `SDZ_winter_file_routes`, `SDZ_radical_turn`, `SDZ_hidden_doctrine`, `SDZ_extreme_gate`, `SDZ_extreme_path` |
| `GAC_soviet_collapse_focus_tree` | 24 | `GAC_first_guard`, `GAC_stores`, `GAC_rival`, `GAC_doctrine`, `GAC_special_arm`, `GAC_forest_column_school`, `GAC_rail_siding_ambushes`, `GAC_green_column_oaths`, `GAC_captured_artillery_caches`, `GAC_forest_radio_runners`, `GAC_partisan_airstrip_meadows`, `GAC_no_requisition_border`, `GAC_every_village_a_front`, `GAC_supply`, `GAC_blacksmith_carts`, `GAC_forest_depot_clearings`, `GAC_seed_and_rifle_stores`, `GAC_winter_hay_roads`, `GAC_enemy_front`, `GAC_war_plan`, `GAC_radical_turn`, `GAC_hidden_doctrine`, `GAC_extreme_gate`, `GAC_extreme_path` |
| `DHC_soviet_collapse_focus_tree` | 23 | `DHC_first_guard`, `DHC_stores`, `DHC_rival`, `DHC_doctrine`, `DHC_novocherkassk_field_staff`, `DHC_special_arm`, `DHC_river_patrol_school`, `DHC_cavalry_remount_yards`, `DHC_steppe_watch_posts`, `DHC_volunteer_host_schools`, `DHC_supply`, `DHC_enemy_front`, `DHC_war_plan`, `DHC_southern_crossing_batteries`, `DHC_manych_rear_area`, `DHC_host_staff_map`, `DHC_grain_convoy_escorts`, `DHC_winter_road_columns`, `DHC_radical_turn`, `DHC_hardline_against_commissars`, `DHC_hidden_doctrine`, `DHC_extreme_gate`, `DHC_extreme_path` |
| `KHC_soviet_collapse_focus_tree` | 24 | `KHC_first_guard`, `KHC_stores`, `KHC_rival`, `KHC_doctrine`, `KHC_ekaterinodar_field_staff`, `KHC_special_arm`, `KHC_crossing_patrol_school`, `KHC_cavalry_remount_yards`, `KHC_steppe_watch_posts`, `KHC_volunteer_line_schools`, `KHC_supply`, `KHC_enemy_front`, `KHC_war_plan`, `KHC_mountain_crossing_batteries`, `KHC_laba_rear_area`, `KHC_line_staff_map`, `KHC_krasnodar_workshop_contracts`, `KHC_grain_corridor_escorts`, `KHC_winter_corridor_columns`, `KHC_radical_turn`, `KHC_hardline_against_requisition`, `KHC_hidden_doctrine`, `KHC_extreme_gate`, `KHC_extreme_path` |
| `FEV_soviet_collapse_focus_tree` | 24 | `FEV_first_guard`, `FEV_stores`, `FEV_rival`, `FEV_amur_field_staff`, `FEV_ussuri_rail_court`, `FEV_doctrine`, `FEV_special_arm`, `FEV_railway_militia_charter`, `FEV_supply`, `FEV_enemy_front`, `FEV_trans_siberian_dispatch_board`, `FEV_radical_turn`, `FEV_harbor_fortress_line`, `FEV_sikhote_alin_watch_posts`, `FEV_war_plan`, `FEV_winter_rail_columns`, `FEV_razdolnoye_rear_area`, `FEV_amur_buffer_posts`, `FEV_hidden_doctrine`, `FEV_extreme_gate`, `FEV_no_foreign_command_on_the_line`, `FEV_far_eastern_staff_map`, `FEV_extreme_path`, `FEV_endgame` |
| `SZA_soviet_collapse_focus_tree` | 24 | `SZA_first_guard`, `SZA_stores`, `SZA_rival`, `SZA_omsk_field_staff`, `SZA_novosibirsk_rail_court`, `SZA_doctrine`, `SZA_special_arm`, `SZA_city_militia_charter`, `SZA_supply`, `SZA_enemy_front`, `SZA_trans_siberian_dispatch_board`, `SZA_radical_turn`, `SZA_station_fortress_line`, `SZA_war_plan`, `SZA_winter_column_registers`, `SZA_tomsk_omsk_switchyards`, `SZA_baikal_rear_area`, `SZA_irkutsk_depth_stores`, `SZA_hidden_doctrine`, `SZA_extreme_gate`, `SZA_no_requisition_west_of_the_urals`, `SZA_siberian_staff_map`, `SZA_extreme_path`, `SZA_endgame` |
| `UWD_soviet_collapse_focus_tree` | 24 | `UWD_first_guard`, `UWD_stores`, `UWD_rival`, `UWD_doctrine`, `UWD_special_arm`, `UWD_security_school`, `UWD_supply`, `UWD_enemy_front`, `UWD_war_plan`, `UWD_radical_turn`, `UWD_perm_field_staff`, `UWD_tagil_machine_tool_ledger`, `UWD_factory_militia_charter`, `UWD_rail_yard_repair_trust`, `UWD_blast_furnace_guard_posts`, `UWD_kama_foundry_contracts`, `UWD_trans_ural_dispatch_board`, `UWD_rail_belt_armored_patrols`, `UWD_kurgan_rear_area`, `UWD_no_shipments_without_council`, `UWD_committee_staff_map`, `UWD_hidden_doctrine`, `UWD_extreme_gate`, `UWD_extreme_path` |
| `MRC_soviet_collapse_focus_tree` | 26 | `MRC_first_guard`, `MRC_stores`, `mrc_close_the_passes`, `MRC_rival`, `MRC_doctrine`, `mrc_reject_moscow_border_troops`, `mrc_raid_lowland_depots`, `MRC_special_arm`, `MRC_supply`, `MRC_enemy_front`, `MRC_radical_turn`, `MRC_terek_field_staff`, `MRC_pass_court_registers`, `MRC_aul_militia_charter`, `MRC_caucasus_pack_train_board`, `MRC_pass_fortress_line`, `MRC_grozny_workshop_bargain`, `MRC_sunzha_valley_watch_posts`, `MRC_war_plan`, `MRC_winter_pass_columns`, `MRC_argun_rear_area`, `MRC_hidden_doctrine`, `MRC_extreme_gate`, `MRC_no_border_troops_without_council`, `MRC_mountain_staff_map`, `MRC_extreme_path` |
| `IUL_soviet_collapse_focus_tree` | 26 | `IUL_first_guard`, `IUL_stores`, `IUL_rival`, `IUL_doctrine`, `IUL_special_arm`, `IUL_supply`, `IUL_enemy_front`, `IUL_radical_turn`, `IUL_ufa_field_commissars`, `IUL_samara_crossing_ledger`, `IUL_tatar_bashkir_courier_board`, `IUL_kama_workshop_trust`, `IUL_volga_fortified_crossings`, `IUL_bashkir_cavalry_roads`, `IUL_oilfield_security_cordon`, `IUL_no_requisition_without_federal_vote`, `IUL_rail_and_river_patrols`, `IUL_bashkir_rear_camps`, `IUL_corridor_staff_map`, `IUL_war_plan`, `IUL_kazan_ufa_workshop_cordon`, `IUL_orenburg_approach_posts`, `IUL_hidden_doctrine`, `IUL_extreme_gate`, `IUL_extreme_path`, `IUL_endgame` |
| `BAC_soviet_collapse_focus_tree` | 24 | `BAC_first_guard`, `BAC_stores`, `BAC_rival`, `BAC_doctrine`, `BAC_special_arm`, `BAC_supply`, `BAC_enemy_front`, `BAC_radical_turn`, `BAC_war_plan`, `BAC_birobidzhan_archive_workshops`, `BAC_amur_relief_posts`, `BAC_amur_field_staff`, `BAC_militia_training_yards`, `BAC_grain_and_relief_escorts`, `BAC_border_crossing_batteries`, `BAC_taiga_watch_posts`, `BAC_winter_road_columns`, `BAC_obluchye_rear_area`, `BAC_hardline_against_border_troops`, `BAC_commune_staff_map`, `BAC_hidden_doctrine`, `BAC_extreme_gate`, `BAC_extreme_path`, `BAC_endgame` |
| `ARD_soviet_collapse_focus_tree` | 24 | `ARD_first_guard`, `ARD_stores`, `ARD_rival`, `ARD_doctrine`, `ARD_special_arm`, `ARD_supply`, `ARD_enemy_front`, `ARD_radical_turn`, `ARD_war_plan`, `ARD_murmansk_dockyard_sheds`, `ARD_kola_denial_posts`, `ARD_kola_field_staff`, `ARD_naval_infantry_yards`, `ARD_fuel_and_convoy_escorts`, `ARD_kola_battery_posts`, `ARD_tundra_watch_posts`, `ARD_winter_convoy_columns`, `ARD_kandalaksha_rear_area`, `ARD_hardline_against_fleet_commissars`, `ARD_directorate_staff_map`, `ARD_hidden_doctrine`, `ARD_extreme_gate`, `ARD_extreme_path`, `ARD_endgame` |
| `NLC_soviet_collapse_focus_tree` | 22 | `NLC_first_guard`, `NLC_stores`, `NLC_rival`, `NLC_doctrine`, `NLC_special_arm`, `NLC_ice_watch_school`, `NLC_supply`, `NLC_enemy_front`, `NLC_war_plan`, `NLC_radical_turn`, `NLC_ice_watch_training_yards`, `NLC_ration_and_signal_escorts`, `NLC_station_battery_posts`, `NLC_tundra_watch_posts`, `NLC_winter_road_columns`, `NLC_apatity_rear_area`, `NLC_volunteer_station_schools`, `NLC_hardline_against_southern_commissars`, `NLC_commune_staff_map`, `NLC_hidden_doctrine`, `NLC_extreme_gate`, `NLC_extreme_path` |

## Audited Focus Tree IDs

| File | Focus tree id | Focus count | Audit result |
| --- | --- | ---: | --- |
| republics | `soviet_collapse_ukraine_focus_tree` | 83 | Broadest tree; has real branch families, but layout and reward/mechanic quality still require full rework. |
| republics | `soviet_collapse_breakaway_focus_tree` | 36 | Simplified generic breakaway shell. |
| republics | `soviet_collapse_internal_republic_focus_tree` | 62 | Broad internal republic shell, but heavily helper-driven. |
| republics | `soviet_collapse_baltic_focus_tree` | 42 | Compact regional tree; needs expansion/League/fighting mechanics. |
| republics | `soviet_collapse_caucasus_focus_tree` | 40 | Compact regional tree; one pathline fixed, still needs neighbor-conflict depth. |
| republics | `soviet_collapse_central_asia_focus_tree` | 45 | Has the only direct scoped `add_state_claim` focus rewards found; still lacks full expansion/postwar loop. |
| republics | `soviet_collapse_moldova_focus_tree` | 48 | Two pathline endpoints fixed; route payoffs still mostly helper/stat rewards. |
| republics | `soviet_collapse_belarus_focus_tree` | 53 | Needs stronger security, army, expansion, and League conflict payoffs. |
| republics | `soviet_collapse_kazakhstan_focus_tree` | 92 | Large but reward-heavy; needs clearer route consequences and aggression mechanics. |
| custom splinters | `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` focus trees | 47 each | Present but structurally templated; needs bespoke dangerous behavior, expansion, decisions, AI, and postwar handling. |
| custom splinters | `PRA_soviet_collapse_focus_tree` | 22 | Shallow crisis ladder. |
| custom splinters | `TSC_soviet_collapse_focus_tree` | 18 | Shallow crisis ladder. |
| custom splinters | `RMC_soviet_collapse_focus_tree` | 18 | Shallow crisis ladder; far below requested death-state threat. |
| custom splinters | `DSC_soviet_collapse_focus_tree` | 18 | Shallow crisis ladder; far below requested dead-congress aggression. |
| custom splinters | `NRF_soviet_collapse_focus_tree` | 18 | Shallow crisis ladder. |
| custom splinters | `ICD_soviet_collapse_focus_tree` | 18 | Shallow crisis ladder. |

## Route Coverage Table

| Required route/content area | Implemented coverage in scoped files | Status | Required redesign |
| --- | --- | --- | --- |
| Political branches | Present in Ukraine, regional republics, and most custom 47-focus templates. | Partial | Political choices need visible leader/advisor/law/party/cosmetic consequences, not mostly flags plus shared helpers. |
| Industry branches | Present as factory/rail/depot focuses. | Partial | Replace one-factory and repeated construction rewards with construction programs, state-targeted decisions, supply projects, resource extraction, and route-locked growth. |
| Military branches | Present in almost every tree. | Partial | Add templates, OOBs, special units, war plans, command structures, and AI aggression. |
| Diplomacy branches | Present through League/foreign/channel focuses. | Partial | Add recognition missions, sponsor risk, League votes, guarantees, intervention, aid corridors, and anti-puppet consequences. |
| Expansion branches | Weak. Central Asia has limited direct claims; most trees have no direct war goals, cores, claims, or integration hooks in the focus files. | Fails full target | Add focus-unlocked expansion decisions, war goals, cores/claims, state integration missions, protectorate/league settlement, and postwar cleanup. |
| League and republic fighting | League focus names exist, but focus-level war/settlement mechanics are thin. | Fails full target | League/republic routes need rivalry decisions, member votes, joint wars, arbitration, betrayals, and neighbor-specific AI strategies. |
| Chaos countries as dangerous actors | Custom splinter trees have identity branches, but no direct focus-level `create_wargoal`, `declare_war_on`, `add_state_core`, `add_state_claim`, or `add_ai_strategy` effects. | Fails full target | Add aggressive expansion packages. `DSC` should gain immediate neighboring war goals/cores/integration and AI attack pressure. Similar packages are needed for RMC, NRF, ICD, TSC, ARD, NLC, BBH, FTH, BSC, PRA, BAC, GAC, DHC, KHC. |
| Construction directorate/factory growth | Civilian Factory of Russia is outside these two scoped files, likely in `005_soviet_collapse_factory_successors.txt`. | Out of scope here | Parent should audit that file against the requirement for major civilian factory growth and overpowered construction-state mechanics. |
| Focus pathline cleanliness | Non-Ukraine same-row issues found by this pass were fixed. | Partial | Ukraine still has 2 same-row and 6 upward prerequisite paths; it needs a broader reflow, not a one-focus nudge. |

## Missing or Simplified Content

1. Direct idea spam in these two files is currently not the main problem: no focus directly uses `add_ideas`, `add_timed_idea`, or `swap_ideas`, and no duplicate direct idea grants were found.
2. The reward clutter problem has shifted into repeated helpers and flat effects. Across 1506 focuses: 354 use `add_building_construction`, 195 use `add_equipment_to_stockpile`, 222 use `add_stability`, 124 use `army_experience`, 118 use `add_political_power`, 103 use `add_manpower`, and 68 use `add_war_support`.
3. Shared helper overuse remains the dominant pattern: `soviet_collapse_apply_focus_legal_recognition` appears 297 times, `soviet_collapse_apply_focus_depot_and_supply_control` 254 times, `soviet_collapse_apply_focus_military_consolidation` 248 times, `soviet_collapse_apply_focus_league_preparation` 220 times, `soviet_collapse_apply_focus_foreign_channel` 175 times, and `soviet_collapse_apply_focus_high_chaos_identity` 94 times.
4. Direct expansion mechanics are almost absent from the focus files. The audit found 0 `create_wargoal`, 0 `declare_war_on`, 0 `add_state_core`, 0 `annex_country`, 0 `transfer_state_to`, and only the Central Asia Khwarazm focus cluster has direct `add_state_claim` lines.
5. No focus directly activates decisions or missions in the scoped files (`activate_decision`, `activate_mission`, `unlock_decision_tooltip` not found). That is a major mismatch with the spec requirement that focuses evolve decision categories.
6. The 18-focus and 22-focus splinter trees (`PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`) are shallow ladders, not full fixed-purpose crisis trees.
7. The 47-focus custom splinter trees are too template-like. They have identity labels but not enough bespoke political, industry, military, diplomacy, expansion, and endgame mechanics.

## Icon Coverage Table

| Metric | Result |
| --- | ---: |
| Focuses audited | 1506 |
| Focuses with icon assignments | 1506 |
| Focus icons missing sprite definitions in mod/vanilla interface scan | 0 |
| Unique focus icon IDs | 1346 |
| Icon IDs reused more than twice | 29 |

Repeated icons are a quality issue rather than a load-breaker. Highest-priority repeated icon clusters include `GFX_focus_soviet_collapse_guard_the_radio_stations`, `GFX_ukr_soviet_collapse_democratic`, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`, `GFX_focus_soviet_collapse_steppe_supply_congress`, `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`, `GFX_central_asia_soviet_collapse_steppe_federation`, `GFX_moldova_soviet_collapse_ukrainian_corridor`, `GFX_focus_FEV_diplomatic_plan`, `GFX_focus_SZA_diplomatic_plan`, `GFX_focus_MRC_civil_rule`, `GFX_focus_MRC_foreign`, `GFX_focus_IUL_supply`, and `GFX_focus_IUL_war_plan`.

## Localisation and Reward Mismatch List

| Area | Result |
| --- | --- |
| Focus name keys | 0 missing among 1506 focus IDs. |
| Focus description keys | 0 missing among 1506 focus IDs. |
| Focus tree name/description keys | 0 missing among 34 focus tree IDs. |
| Filter patch localisation | No localisation change needed; patched filters are vanilla filter IDs. |
| Coordinate patch localisation | No localisation keys changed. |
| Reward mismatch | Many descriptions imply institutions, wars, mandates, leagues, or dangerous state-building, but rewards are mostly flags, shared helpers, flat stats, factories, or equipment. This is the key content mismatch for parent rework. |

## AI Behavior Gaps

1. Every audited focus has an `ai_will_do` block, but 304 have simple flat blocks without local modifiers.
2. No focus in the scoped files directly adds `add_ai_strategy`.
3. High-chaos and death-state tags do not have enough AI behavior for the requested dangerous role. They need focus or decision hooks that drive neighbor antagonism, war goals, declarations, coring, and consolidation.
4. League and republic AI should be route-aware: form or join leagues, fight rivals, accept/reject foreign sponsorship, pursue expansion when strong, and avoid impossible goals when surrounded or collapsing.
5. Adding smarter weights to the current shallow crisis ladders would lock in weak design. Redesign the branches first, then add AI strategies.

## High-Priority Fixes

Completed in this pass:

1. Fixed invalid generic military/air/naval focus filters in `005_soviet_collapse_custom_splinters.txt`.
2. Fixed same-row non-Ukraine prerequisite pathlines for `caucasus_soviet_collapse_the_compact_holds_the_ridge`, `moldova_soviet_collapse_republic_of_crossings`, and `moldova_soviet_collapse_the_river_state`.

Parent high-priority work:

1. Reflow Ukraine. Remaining topology findings are all in `soviet_collapse_ukraine_focus_tree`: two same-row prerequisite paths and six upward prerequisite paths.
2. Redesign `DSC`, `RMC`, `NRF`, `ICD`, `TSC`, and `PRA` as full crisis trees. `DSC` especially needs immediate neighboring war goals/cores, aggressive AI, and dead-army postwar integration.
3. Add focus-decision integration across republic and League branches. Focuses should unlock expansion, coring, integration, recognition, aid, military, and industrial programs.
4. Convert repeated helper/stat rewards into route-specific mechanics and bespoke effects.
5. Add expansion and postwar systems for League/republic conflicts: claims, cores, war goals, state integration, protectorate options, and rivalry AI.
6. Audit `005_soviet_collapse_factory_successors.txt` separately for the construction directorate/civilian factory growth requirement; it is outside this subagent scope but explicitly called out by the parent task.

## Remaining Layout Risks

Ukraine unresolved pathline findings:

- Same row: `ukr_soviet_collapse_foreign_advisers_in_plain_coats` -> `ukr_soviet_collapse_purge_moscow_loyalists`.
- Same row: `ukr_soviet_collapse_grain_loan` -> `ukr_soviet_collapse_officer_patronage_lists`.
- Upward: `ukr_soviet_collapse_socialist_republic_without_moscow` -> `ukr_soviet_collapse_peasant_socialist_congress`.
- Upward: `ukr_soviet_collapse_socialist_republic_without_moscow` -> `ukr_soviet_collapse_workers_congress_in_kharkiv`.
- Upward: `ukr_soviet_collapse_kyiv_leads_the_front` -> `ukr_soviet_collapse_provincial_governors_or_elected_radas`.
- Upward: `ukr_soviet_collapse_league_of_equals` -> `ukr_soviet_collapse_provincial_governors_or_elected_radas`.
- Upward: `ukr_soviet_collapse_border_states_accept_kyiv` -> `ukr_soviet_collapse_provincial_governors_or_elected_radas`.
- Upward: `ukr_soviet_collapse_carpathian_security_belt` -> `ukr_soviet_collapse_dead_fields_living_columns`.

These are not safe one-line fixes because they sit in the broad Ukraine political/League/Black Banner layout. Parent should reflow that whole section together.

## Validation Run

- Focus parse/topology audit: 34 focus trees, 1506 focuses.
- Duplicate/missing focus audit: 0 duplicate focus IDs found by parser; 0 missing prerequisite IDs in scoped files.
- Filter audit after patch: no `FOCUS_FILTER_ARMY`, `FOCUS_FILTER_AIR`, or `FOCUS_FILTER_NAVY` remains in either scoped focus file.
- Unsupported operator audit: no `<=` or `>=` remains in either scoped focus file.
- Localisation audit: 0 missing focus names, 0 missing focus descriptions, 0 missing tree name/description keys.
- Icon audit: 0 missing icon assignments; 0 missing sprite definitions in mod/vanilla interface scan.
- Reward duplicate audit: 0 duplicate simple direct reward lines in individual focus blocks.
- Idea reward audit: 0 direct `add_ideas`, `add_timed_idea`, or `swap_ideas` in the two scoped files.
- Brace check: both scoped files ended at depth 0 with 0 early closes.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt` passed.

## Skipped Validation

- No in-game HOI4 load test was run from this subagent.
- No full mod-wide validator was run because the worktree contains many unrelated parent/user changes.
- No localisation encoding rewrite was performed because no localisation files were edited.
- No Git commit was created from this subagent pass because the parent worktree is actively dirty with many unrelated files; the parent should commit the final integrated goal.

## Remaining Route Risks

- This pass does not complete the full Soviet Collapse focus rework. It only removes filter breakage, clears a few local pathline issues, and documents the route/design gaps.
- The scoped focus files still do not satisfy the requirement that chaos countries be extremely overpowered and dangerous.
- League and republic expansion/fighting mechanics remain mostly absent from focus rewards.
- The shallow crisis splinters are not acceptable as final full-rework content.
- Repeated helper rewards still make many focuses feel generic even though direct idea spam is absent.
- Construction Directorate/Civilian Factory growth was not audited because it is outside the two files named in this subagent scope.

## Handoff Path

`docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_soviet_collapse_focus_rework_audit_filters_layout.md`
