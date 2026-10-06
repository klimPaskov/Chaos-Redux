# Fallout graphics handoff - 2026-10-06

All eight fallout_consolidated rows in C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md are implemented and parent-approved. Exact prompt/source/processed/runtime hashes are in graphics_asset_crosswalk.json; prompt blocks are retained next to this handoff.

## Fix-plan dispositions

| Finding | Disposition |
|---|---|
| working_machine DDS corruption | Recovered exact-size raw BGRA pixels from the malformed 147,968-byte DDS, normalized it, and applied the shared grade/frame; original retained. |
| 33 generic focus aliases | 33 individual 94x86 painted medallions; unique base and shine aliases map to per-focus DDS. |
| Five USA decision icons | Five dedicated transparent 32x32 miniatures replace oversized focus art. |
| 23 full-bleed reports | All 23 use shared sepia and tilted frame; open_the_sealed_city was regenerated as a 1940s scene. |
| USA decision category | Dedicated 52x40 icon with 3px margin registered. |
| door_list and fever_dormitory | door_list regenerated as a 1940s shelter door with illegible marks; fever_dormitory retained and reframed/regraded. |
| Four report frame outliers | dead_city_permit, metro_republic_below, border_inspection_crisis, orchard_flowers use shared frame; rejected Dead City/Orchard sources replaced; Health Without Borders readable sign removed. |
| Two NZL rescue icons | Both replaced with larger solid-body transparent 32x32 rescue/fleet miniatures. |

The Fallout focus-art cross-cutting rule is satisfied by 33 unique focus icons. The report style is standardized across the 30 Fallout report assets in scope. The USA decision-category sizing rule is satisfied by the 52x40 texture.

## Runtime mappings

Current interface/fallout_consolidated.gfx paths and generic focus icon tokens match the mappings below. Parent owns final wiring. This subagent changed no GFX or gameplay files.

### Generic focus medallions

| Focus ID | Base and shine aliases | Runtime DDS | SHA-256 | Prompt |
|---|---|---|---|---|
| wake_the_survivors | GFX_goal_fallout_generic_wake_the_survivors / GFX_goal_fallout_generic_wake_the_survivors_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_wake_the_survivors.dds | be77d72f194ed95552dae0687e43df39014f2753ab6e9420f8d0b6e8fb38f4e1 | F01 |
| map_the_ruins | GFX_goal_fallout_generic_map_the_ruins / GFX_goal_fallout_generic_map_the_ruins_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_map_the_ruins.dds | 5d0372731d85a15859f1fdec414537c6ef640b1793838da57fef83da831f05ff | F02 |
| hold_the_capital | GFX_goal_fallout_generic_hold_the_capital / GFX_goal_fallout_generic_hold_the_capital_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_hold_the_capital.dds | 1b1b85e9fc5f278541b3596ca6aa0f766ab74ef48aa66d097c227c5e59674178 | F03 |
| civic_compact | GFX_goal_fallout_generic_civic_compact / GFX_goal_fallout_generic_civic_compact_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_civic_compact.dds | f82435579ee883771ae7f67a44024f62ca0e3547f45021d29c40453cd8b62d57 | F04 |
| ration_congress | GFX_goal_fallout_generic_ration_congress / GFX_goal_fallout_generic_ration_congress_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_ration_congress.dds | cd45e09aaf6685386dd2d33be9af862819127656405b9f4d8c79ff98e4ec8d53 | F04 |
| command_directorate | GFX_goal_fallout_generic_command_directorate / GFX_goal_fallout_generic_command_directorate_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_command_directorate.dds | 55ac35292a90313cde56ef3c551feef7d7561c3de12a5dcb5179fb8c8aa449ea | F04 |
| shelter_council | GFX_goal_fallout_generic_shelter_council / GFX_goal_fallout_generic_shelter_council_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_shelter_council.dds | 643032d0c89236550f9aa177de1124563fce8d96a85b820403a029b86c33b67a | F04 |
| publish_survival_charter | GFX_goal_fallout_generic_publish_survival_charter / GFX_goal_fallout_generic_publish_survival_charter_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_publish_survival_charter.dds | 23c16934bfce872bc3ae3e4604c87adac14a8a5d65ac147a0d1587923c40da15 | F05 |
| reopen_power_grid | GFX_goal_fallout_generic_reopen_power_grid / GFX_goal_fallout_generic_reopen_power_grid_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_reopen_power_grid.dds | 35be030408fce51f604cd3deb1531df96fe4f069a7fbbb2d19ce35cf22c8142c | F05 |
| repair_rail_spine | GFX_goal_fallout_generic_repair_rail_spine / GFX_goal_fallout_generic_repair_rail_spine_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_repair_rail_spine.dds | 31f3aa6688195955b6f5265fa509f7b7603f49ad096bffd8c8a3029b2fc87e22 | F05 |
| reclaim_workshops | GFX_goal_fallout_generic_reclaim_workshops / GFX_goal_fallout_generic_reclaim_workshops_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_reclaim_workshops.dds | 5fa40dc7f356fd07e5ed373170ec7960298bbf32b68fc22b171a959e09a4d9aa | F05 |
| raise_survivor_guard | GFX_goal_fallout_generic_raise_survivor_guard / GFX_goal_fallout_generic_raise_survivor_guard_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_raise_survivor_guard.dds | ae5764e8de7d7b4024592c620a5ed3ac7e36b1a3b6be6271081d15f3c7781bfa | F06 |
| train_frontier_columns | GFX_goal_fallout_generic_train_frontier_columns / GFX_goal_fallout_generic_train_frontier_columns_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_train_frontier_columns.dds | 8bc83d8a2754f7092170cc43ee0680d9b5de632a86e71d24968f3c433de31fa8 | F06 |
| arm_the_cordon | GFX_goal_fallout_generic_arm_the_cordon / GFX_goal_fallout_generic_arm_the_cordon_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_arm_the_cordon.dds | 702b0592e6ea51d88f9061a712a8529ad8a67cf6b364c0cb31fffbb3f7db5ea4 | F06 |
| open_radio | GFX_goal_fallout_generic_open_radio / GFX_goal_fallout_generic_open_radio_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_open_radio.dds | 419e1e0991f2ea7071f526ce691a9c84ef59a58e7921ad8aaf0b8462dfa56078 | F06 |
| settle_the_new_border | GFX_goal_fallout_generic_settle_the_new_border / GFX_goal_fallout_generic_settle_the_new_border_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_settle_the_new_border.dds | d0406718747430ba4fbb8edcbe22851cd92ec87825733b7fb3effa1f471570d2 | F08 |
| open_the_regional_ledger | GFX_goal_fallout_generic_open_the_regional_ledger / GFX_goal_fallout_generic_open_the_regional_ledger_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_open_the_regional_ledger.dds | a9e97f384dac8cd8f934b36cfc3e220031a4deb04cf464e9d87f5897a00ebaa6 | F08 |
| north_america_relay | GFX_goal_fallout_generic_north_america_relay / GFX_goal_fallout_generic_north_america_relay_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_north_america_relay.dds | a997f76176b638f250c79231c21736fefae7ce28e78bf984afb4f95340d1d6b3 | F08 |
| europe_water_councils | GFX_goal_fallout_generic_europe_water_councils / GFX_goal_fallout_generic_europe_water_councils_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_europe_water_councils.dds | 13db12fd09a54c15bab8a49979781b6d778d35f1bdddab515f94ae665d83844d | F08 |
| found_frontier_pact | GFX_goal_fallout_generic_found_frontier_pact / GFX_goal_fallout_generic_found_frontier_pact_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_found_frontier_pact.dds | c3d00af5aec37dc7891517effcaac23261671a11bc86d63a53a4fe6ca9a478ca | F09 |
| invite_neighbor_compacts | GFX_goal_fallout_generic_invite_neighbor_compacts / GFX_goal_fallout_generic_invite_neighbor_compacts_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_invite_neighbor_compacts.dds | 69ae873a428ad20eafca666246b6356476b094c1230dd819ece5d096aa8f853f | F10 |
| claim_the_empty_belt | GFX_goal_fallout_generic_claim_the_empty_belt / GFX_goal_fallout_generic_claim_the_empty_belt_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_claim_the_empty_belt.dds | 3821ee60326b91e6c7cf39f5904c4739f1b15e77fba1d1a488e54f5d436900fc | F11 |
| issue_border_ultimatum | GFX_goal_fallout_generic_issue_border_ultimatum / GFX_goal_fallout_generic_issue_border_ultimatum_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_issue_border_ultimatum.dds | d8ddfc92e0f9bbdb387e121c7562aa9e3373a5f1fcce88426589c02b2fd6e055 | F12 |
| eurasian_inland_road | GFX_goal_fallout_generic_eurasian_inland_road / GFX_goal_fallout_generic_eurasian_inland_road_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_eurasian_inland_road.dds | 0695433db1bbf96d3040fa2548f45be3504b05e13492d8dd65ab475d371f9383 | F13 |
| east_asia_seed_banks | GFX_goal_fallout_generic_east_asia_seed_banks / GFX_goal_fallout_generic_east_asia_seed_banks_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_east_asia_seed_banks.dds | 671d84e5da76ea54df4d5a90c645ff2c7282f42121e62b42c7782ea85b108b7a | F13 |
| south_asia_delta_routes | GFX_goal_fallout_generic_south_asia_delta_routes / GFX_goal_fallout_generic_south_asia_delta_routes_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_south_asia_delta_routes.dds | 690feee7e7679ae41bbf350dc416c2609fa916245bc8487d1ee846f212e3c259 | F13 |
| mena_quarantine_roads | GFX_goal_fallout_generic_mena_quarantine_roads / GFX_goal_fallout_generic_mena_quarantine_roads_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_mena_quarantine_roads.dds | 5cf151b457c1f06358e3a041e863e51ebcafb0bf89c48e28b0f0407c913b547c | F13 |
| africa_river_wards | GFX_goal_fallout_generic_africa_river_wards / GFX_goal_fallout_generic_africa_river_wards_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_africa_river_wards.dds | fba19a3e775757b9583dd228ace5c3c8e1a6163cc683cd2f364337df6087e71e | F15 |
| latin_america_water_charters | GFX_goal_fallout_generic_latin_america_water_charters / GFX_goal_fallout_generic_latin_america_water_charters_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_latin_america_water_charters.dds | c8b4d75df27813c7b957de1d5216f7be7a8bafb987566cebf36090a2d273424b | F16 |
| oceania_remote_stations | GFX_goal_fallout_generic_oceania_remote_stations / GFX_goal_fallout_generic_oceania_remote_stations_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_oceania_remote_stations.dds | 182c910f5b0f59496fa7253ea4eb6f767bd7e4fe9c5c0334be9c380496f6db99 | F17 |
| federate_survivor_leagues | GFX_goal_fallout_generic_federate_survivor_leagues / GFX_goal_fallout_generic_federate_survivor_leagues_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_federate_survivor_leagues.dds | 111b400d4de5821fe5f8a42d5cecfd752dc3945a8b1a25887edff8fd050d6cde | F18 |
| reclaim_the_heartland | GFX_goal_fallout_generic_reclaim_the_heartland / GFX_goal_fallout_generic_reclaim_the_heartland_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_reclaim_the_heartland.dds | 248f0277f544e3302e169056c7283143d16cdee68c2b70d07ef8e09fb06d5bc7 | F19 |
| year_ten_order | GFX_goal_fallout_generic_year_ten_order / GFX_goal_fallout_generic_year_ten_order_shine | gfx/interface/goals/fallout_generic/goal_fallout_generic_year_ten_order.dds | f284e2b85f5806edcbaf44ebbca8d365ad9de08843aad3214370dc50b1142934 | F20 |

### Decisions, category, Recognition texticon

| Kind | Sprite alias | Runtime DDS | Size | SHA-256 |
|---|---|---|---|---|
| decision | GFX_decision_fallout_usa_depot_belt_repair | gfx/interface/decisions/fallout_successor_b7_usa/decision_fallout_usa_depot_belt_repair.dds | 32x32 | 832ea680d052b6366b3dd146ca8f2528eb47e4f3b29192f0ff9d55befd15846f |
| decision | GFX_decision_fallout_usa_guard_muster | gfx/interface/decisions/fallout_successor_b7_usa/decision_fallout_usa_guard_muster.dds | 32x32 | 6e238b23fe0ff6f8ff9e0c9848daa1cfd6d24fc4cecae5392009e03df18692ef |
| decision | GFX_decision_fallout_usa_lakes_charter | gfx/interface/decisions/fallout_successor_b7_usa/decision_fallout_usa_lakes_charter.dds | 32x32 | 37def0d5ab035b446851162f5b78959bf269033fad57e61bfb2cd2d5066d9d8e |
| decision | GFX_decision_fallout_usa_radio_sweep | gfx/interface/decisions/fallout_successor_b7_usa/decision_fallout_usa_radio_sweep.dds | 32x32 | d658e562069334662864bea9985a5d851ecb624d41d5072c6cb15466d7999d29 |
| decision | GFX_decision_fallout_usa_reconstruction_drive | gfx/interface/decisions/fallout_successor_b7_usa/decision_fallout_usa_reconstruction_drive.dds | 32x32 | 6334b1a4743b68dc0806f1e524871bc1b381a36b621c4c451d9ab62e35d7dc1e |
| decision | GFX_decision_fallout_nzl_offer_rescue_passage | gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_offer_rescue_passage.dds | 32x32 | fecca7faf01056cca06a9e786adb21d0ff19aff2eb35fd227a3d2a0259d45878 |
| decision | GFX_decision_fallout_nzl_refugee_fleet_admission | gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_refugee_fleet_admission.dds | 32x32 | ddab361b3c66c1bde1e2f413098e597282f761094cd2642462b577c8b4c34927 |
| decision_category | GFX_decision_category_fallout_usa_continuity_projects | gfx/interface/decisions/visual_consistency_repair/categories/decision_category_fallout_usa_continuity_projects.dds | 52x40 | f86719fb035bab58544c334f6b9cf0b2b08f32d310d7e614f087abbb47979792 |
| texticon | GFX_fallout_recognition_texticon | gfx/texticons/fallout_recognition_texticon.dds | 18x19 | d03197dae4a195d871258cc2520d5a9af181bd9c70d832aa5deeedc939b1c103 |

### Report images

| Sprite alias | Runtime DDS | Size | SHA-256 |
|---|---|---|---|---|
| GFX_report_event_fallout_false_positive | gfx/event_pictures/fallout/report_event_fallout_false_positive.dds | 210x176 | 88a4b4062954e4e3954c49a3a9f6cf6627ca01a88cb9bf8a0e461fc971896cf1 |
| GFX_report_event_fallout_permit_market | gfx/event_pictures/fallout/report_event_fallout_permit_market.dds | 210x176 | 945c0f331f5eb2f09ce458f3674b469c3f1abae010318423d0a6e9a3ae0cd77b |
| GFX_report_event_fallout_doctors_coup | gfx/event_pictures/fallout/report_event_fallout_doctors_coup.dds | 210x176 | 4fb634d08d192b761e7d6e5724fa89b4b7980ab45f80feea788d8eeb87bd7dda |
| GFX_report_event_fallout_manual_nobody_read | gfx/event_pictures/fallout/report_event_fallout_manual_nobody_read.dds | 210x176 | 3a80cd37623af0d84dbfa3b70574146b8e0fd76efd9666e51028bc86f3934492 |
| GFX_report_event_fallout_vault_of_voices | gfx/event_pictures/fallout/report_event_fallout_vault_of_voices.dds | 210x176 | 75eb3398a6cb6706310ad6ac525bc02124ad8aad14bb840f1e059855f10e1f62 |
| GFX_report_event_fallout_bridge_that_moved | gfx/event_pictures/fallout/report_event_fallout_bridge_that_moved.dds | 210x176 | 58e3570189d83ed575411867a9ea2471bb8d57895328cd03e738d9106b232e7f |
| GFX_report_event_fallout_first_unmasked_day | gfx/event_pictures/fallout/report_event_fallout_first_unmasked_day.dds | 210x176 | ca7cff23a4e04e83ef5eed8113e4519ae0a1290a14e50665591850c1a60c0dbb |
| GFX_report_event_fallout_false_spring_losses | gfx/event_pictures/fallout/report_event_fallout_false_spring_losses.dds | 210x176 | 9f2ea467ee243f6d4c72a15285423c58c44618db814871fa99e7ba109500ae3f |
| GFX_report_event_fallout_desalination_night_shift | gfx/event_pictures/fallout/report_event_fallout_desalination_night_shift.dds | 210x176 | f2841c09c7cf4be2bf067dcc5b69bad5edd621fb4e5cf6f39a4ee1d09c53081d |
| GFX_report_event_fallout_ice_melt_rations | gfx/event_pictures/fallout/report_event_fallout_ice_melt_rations.dds | 210x176 | d9354a073b1502011fa860a540dc41830b856aae14444a9ae6f8bbafa2bf9569 |
| GFX_report_event_fallout_ravine_water_chemist | gfx/event_pictures/fallout/report_event_fallout_ravine_water_chemist.dds | 210x176 | b071346de993d52165102c95082ac5164723728cdf57017f498ff6a1f65ec29d |
| GFX_report_event_fallout_ashline_firebreak | gfx/event_pictures/fallout/report_event_fallout_ashline_firebreak.dds | 210x176 | 2a8b61afe4ec7494915840bce33d95af2619d62da9d635b3918d175bb3f088a2 |
| GFX_report_event_fallout_radio_island_chain | gfx/event_pictures/fallout/report_event_fallout_radio_island_chain.dds | 210x176 | b618329f65acb60c9d2ef281f4f98fea4a69097ea09b77160efdfa3dce74882d |
| GFX_report_event_fallout_tunnel_ward_committees | gfx/event_pictures/fallout/report_event_fallout_tunnel_ward_committees.dds | 210x176 | 94485c0e029cb9e95f02d010ec20c7f207b056824f38606400bb776ae3bd8b84 |
| GFX_report_event_fallout_rail_spine_vote | gfx/event_pictures/fallout/report_event_fallout_rail_spine_vote.dds | 210x176 | bdee8acedba3923c85438d7ac213794f17f55136ff46e00a7f3aa664230e95de |
| GFX_report_event_fallout_canal_schedule | gfx/event_pictures/fallout/report_event_fallout_canal_schedule.dds | 210x176 | e7a0eadccafb70b809a456b08bdce224a912f9aa40b892c890333219ca989684 |
| GFX_report_event_fallout_children_of_cordon | gfx/event_pictures/fallout/report_event_fallout_children_of_cordon.dds | 210x176 | 91cc8ecd200f9be4ee9af0e947faecb359a7046ee0483a5cd51f71cbee6456cb |
| GFX_report_event_fallout_open_the_sealed_city | gfx/event_pictures/fallout/report_event_fallout_open_the_sealed_city.dds | 210x176 | cd1bc52566757f66f16f46adb5ee47e08f65e5671db3aab5fa28e95fa54f0fc3 |
| GFX_report_event_fallout_health_without_borders | gfx/event_pictures/fallout/report_event_fallout_health_without_borders.dds | 210x176 | 7381140b18b65c62ca7d03789d71cc6a193d8aaf7321327c12986ccab1d2defb |
| GFX_report_event_fallout_cohorts_first_ballot | gfx/event_pictures/fallout/report_event_fallout_cohorts_first_ballot.dds | 210x176 | 984347e23fda851ca352b7f2aaac7e03bd0fb1efeacf5173002ea32f40d4a2a1 |
| GFX_report_event_fallout_quarantine_ultimatum | gfx/event_pictures/fallout/report_event_fallout_quarantine_ultimatum.dds | 210x176 | 79f4ccaf9f6266f9ec6c077e0d5bb5277b8adfbab9fefa61db05f64efa5a4381 |
| GFX_report_event_fallout_last_transformer | gfx/event_pictures/fallout/report_event_fallout_last_transformer.dds | 210x176 | dde9491a4fe637c809f166803f4674526fd55e06bb705a89143d0cea027d3e10 |
| GFX_fallout_seed_vault_report | gfx/event_pictures/fallout/seed_vault_report.dds | 210x176 | 15dde7a9da19f3abbdc4353817224164c786424e0ea0abd3e46216c703ac4c1e |
| GFX_report_event_fallout_working_machine | gfx/event_pictures/fallout/report_event_fallout_working_machine.dds | 210x176 | 96f987110d9c2d95be39bac64b0c2af329c3db4cfd2b52506f2424d5ed5431f6 |
| GFX_report_event_fallout_door_list | gfx/event_pictures/fallout/report_event_fallout_door_list.dds | 210x176 | 0d3642c8d5316f2d3400197dda3b9a387f565daf9bc5ebe7f132f4fa7534fc45 |
| GFX_report_event_fallout_fever_dormitory | gfx/event_pictures/fallout/report_event_fallout_fever_dormitory.dds | 210x176 | c7765b78d71b649ea16d4006c544afacd00d33f72ce5fffe74b3c99102d20914 |
| GFX_report_event_fallout_dead_city_permit | gfx/event_pictures/fallout/report_event_fallout_dead_city_permit.dds | 210x176 | de341c69eab4d330cc4625f89079764530ffabca0be3ad45052b48807047c489 |
| GFX_report_event_fallout_metro_republic_below | gfx/event_pictures/fallout/report_event_fallout_metro_republic_below.dds | 210x176 | 1bf18b4a72f1a7b80e12176b7c1a315b7e2e33f2185f044cbf0005de43dfd262 |
| GFX_report_event_fallout_border_inspection_crisis | gfx/event_pictures/fallout/report_event_fallout_border_inspection_crisis.dds | 210x176 | 5ba41daf956aad251ac730cf760946c75737703e865796f7fdb4bb9144957f89 |
| GFX_report_event_fallout_orchard_flowers | gfx/event_pictures/fallout/report_event_fallout_orchard_flowers.dds | 210x176 | 422913d35a93d47421f1359d7cbb50d86e72b68e730539a93b1619f7568ed2cc |

## Provenance and QA

Every generated asset has retained source PNG, prompt record/hash, processed preview, runtime DDS/hash in the JSON crosswalk. Focus atlases 05 and 09 were rejected because subjects touched/crossed cell boundaries; individual replacements were used. Recognition T01 is superseded; T02 is authoritative. DDS SHA d03197dae4a195d871258cc2520d5a9af181bd9c70d832aa5deeedc939b1c103 matches the exact file committed in 9ec627597.

Reports use the shared edge layer docs/assets/air_cleanliness_fallout/graphics/component_layers/report_frame_air_winter_phase_1_edge_layer.png derived from report_event_air_winter_phase_1.dds and sepia grade sampled from report_event_fallout_school_vent_room.dds. Sources, previews, archives, candidates, and sheets remain under docs/assets/air_cleanliness_fallout/graphics/.

Parent approved all focus, report, decision, category, and Recognition groups at native and 4x on 2026-10-06. Final alpha/size audits: focus 33, decisions 7, reports 30, category 1, Recognition 1; zero flagged in each group. Report DDSes decode at 210x176, round-trip from processed previews, and match the shared frame alpha mask.

Focus MCP inspection revision fc26c462576ee870f97e1292467dd1743ce100949bb7d3414e2a6e0135223f03 covered 33 nodes; five diagnostics were reported to parent. Parent's 4880x1628 raster review found zero intersections, crossings, or spacing violations; three unchanged regional fan connectors remain long.

Runtime total: 33 focus, 7 decision, 1 category, 1 texticon, 30 report DDSes. No asset item is blocked or simplified. No portraits were produced. Parent owns integration and commit; this subagent has not committed. No graphics blocker remains known.
