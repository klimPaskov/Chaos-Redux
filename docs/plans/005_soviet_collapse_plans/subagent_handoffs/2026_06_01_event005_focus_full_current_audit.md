# Event005 Soviet Collapse focus full current-state audit

Date: 2026-06-01

Scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Flags constraint:
- No `gfx/flags`, flag sprite, or flag asset files were inspected for editing or changed.

## Summary

The current Event005 focus set is much healthier than the worst complaint implies in two narrow areas: duplicate focus IDs are not present, every focus has `ai_will_do`, every focus has `search_filters`, and no focus currently duplicates the same `add_ideas` or `add_timed_idea` within its own reward block.

The main complaint is still valid at scale. Across 1,698 focuses, 202 focuses still directly grant stockpiled equipment and 159 focuses still have a single-building-only reward. The shallowest identity trees are the 16-23 focus high-chaos/special successors and ancient restorations. Several 47-focus custom splinters have better branch shape than before, but many still use repeated support equipment, convoy, rail, or one-building rewards instead of route-specific mechanics. Ukraine is not actually linear by count, but its coordinates create a tangled, hard-to-read tree. Belarus has real spacing/pathline problems around the rail/forest/league crossings.

I did not patch because the remaining issues are broad route-quality and reward-architecture work, not a narrow local focus-file defect.

## Route Coverage Table

| File | Tree | Focuses | Coverage judgment | Main gap |
|---|---:|---:|---|---|
| republics | `soviet_collapse_ukraine_focus_tree` | 83 | Large, multi-route | Visually tangled; early route coordinates create long crossing pathlines; strong branch count but awkward layout. |
| republics | `soviet_collapse_breakaway_focus_tree` | 36 | Moderate generic breakaway | Still generic support/reconstruction branch, weak identity. |
| republics | `soviet_collapse_internal_republic_focus_tree` | 62 | Broad regional coverage | Many one-building regional rewards; internal regional identities need deeper mechanics. |
| republics | `soviet_collapse_baltic_focus_tree` | 42 | Playable regional tree | Some good legal/port/forest framing, but several single-building rewards. |
| republics | `soviet_collapse_caucasus_focus_tree` | 40 | Playable regional tree | Oil/mountain mechanics mostly expressed as stockpile/building rewards. |
| republics | `soviet_collapse_central_asia_focus_tree` | 45 | Playable regional tree | 12 one-building-only rewards; cotton/rail/water loop should drive decisions more. |
| republics | `soviet_collapse_moldova_focus_tree` | 48 | Playable regional tree | Better decision hooks than average, but equipment/convoy rewards remain frequent. |
| republics | `soviet_collapse_belarus_focus_tree` | 53 | Real route family | Rail/forest/league pathlines are messy; spacing causes likely crossing/visual clutter. |
| republics | `soviet_collapse_kazakhstan_focus_tree` | 92 | Large, multi-route | Strongest republic tree by depth; still has 11 one-building-only rewards. |
| custom splinters | `FTH_soviet_collapse_focus_tree` | 47 | Moderate custom tree | Repeated one-building rewards and support equipment. |
| custom splinters | `PRA_soviet_collapse_focus_tree` | 22 | Compact identity tree | Has rail variables/decisions, but still too short for a major high-chaos rail state. |
| custom splinters | `TSC_soviet_collapse_focus_tree` | 18 | Shallow | Needs science/lab event or special-project loop, not just compact route. |
| custom splinters | `RMC_soviet_collapse_focus_tree` | 18 | Shallow | Reliquary/dead-volunteer identity needs mechanic depth. |
| custom splinters | `DSC_soviet_collapse_focus_tree` | 18 | Shallow but mechanized | Dead-soldier variables/decisions exist; focus route is still too compressed. |
| custom splinters | `NRF_soviet_collapse_focus_tree` | 18 | Shallow but mechanized | Fleet variables/decisions exist; naval identity needs naval/dockyard/route expansion. |
| custom splinters | `ICD_soviet_collapse_focus_tree` | 18 | Shallow | Death-commissariat identity mostly spirits/equipment, needs coercive politics and expansion loop. |
| custom splinters | `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` | 47 each | Template-sized route trees | Better than shallow stubs, but many are still reward-template variants with repeated equipment/buildings. |
| factory successors | `CFR_soviet_collapse_focus_tree` | 47 | Medium-depth mechanic tree | Has construction mandate variables/decisions; governance/strategy choices use hidden locks instead of visible mutual exclusivity. |
| factory successors | `OGB_soviet_collapse_focus_tree` | 23 | Compact restoration tree | Needs deeper identity/Volga trade or restoration mechanics. |
| factory successors | `MFR_soviet_collapse_focus_tree` | 58 | Stronger factory tree | Better branch depth; still some building-only rewards and needs route payoff polish. |
| ancient restorations | `KZR_soviet_collapse_ancient_focus_tree` | 16 | Shallow | Needs restoration-specific decision/formable/postwar loop. |
| ancient restorations | `SOG_soviet_collapse_ancient_focus_tree` | 16 | Shallow | Needs oasis/city-league mechanics beyond compact branch. |
| ancient restorations | `KHW_soviet_collapse_ancient_focus_tree` | 16 | Shallow | Water/canal identity should become an irrigation/river authority loop. |
| ancient restorations | `ALN_soviet_collapse_ancient_focus_tree` | 16 | Shallow | Alan pass/mountain restoration needs claims, pass missions, and culture/legitimacy loop. |

## Reward Spam Counts

Mechanical counts from current files:
- Focuses audited: 1,698.
- Duplicate focus IDs: 0.
- Missing `ai_will_do`: 0.
- Missing `search_filters`: 0.
- Duplicate `add_ideas` or `add_timed_idea` within one focus: 0.
- Long idea reward lists, using 4 or more `add_ideas`/`add_timed_idea` in one focus: 0.
- Direct `add_equipment_to_stockpile` focus rewards: 202.
- Single-building-only focus rewards: 159.

### Direct Equipment / Stockpile Rewards

The highest-spam trees by direct stockpile focus count are:
- `ARD_soviet_collapse_focus_tree`: 14, mostly `convoy_1`.
- `KHC_soviet_collapse_focus_tree`: 13, mostly `support_equipment_1`.
- `UWD_soviet_collapse_focus_tree`: 11, heavy artillery/support mix.
- `DHC_soviet_collapse_focus_tree`: 10, convoy/support mix.
- `FEV_soviet_collapse_focus_tree`: 9, convoy/support mix.
- `BSC_soviet_collapse_focus_tree`: 7, `BAC`: 7, `IUL`: 7, `NLC`: 7, `PRA`: 7.

Concrete direct-equipment focus IDs:
- `soviet_collapse_ukraine_focus_tree`: `ukr_soviet_collapse_seal_the_grain_ledgers:80`, `ukr_soviet_collapse_count_the_depot_keys:102`, `ukr_soviet_collapse_black_sea_port_ledgers:1217`.
- `soviet_collapse_breakaway_focus_tree`: `soviet_collapse_military_defense_council:2523`, `soviet_collapse_foreign_liaison_government:2561`.
- `soviet_collapse_internal_republic_focus_tree`: `internal_soviet_collapse_far_eastern_port_authority:4190`, `internal_soviet_collapse_republic_volunteer_standards:4485`.
- `soviet_collapse_baltic_focus_tree`: `baltic_soviet_collapse_the_baltic_customs_desk:5075`, `baltic_soviet_collapse_latvian_port_guard_boards:5456`.
- `soviet_collapse_caucasus_focus_tree`: `caucasus_soviet_collapse_black_sea_observer_desks:5755`, `caucasus_soviet_collapse_baku_oilfield_guard:5913`, `caucasus_soviet_collapse_mountain_artillery_schools:6009`, `caucasus_soviet_collapse_yerevan_relief_networks:6030`.
- `soviet_collapse_central_asia_focus_tree`: `central_asia_soviet_collapse_pamir_pass_fortresses:6879`, `central_asia_soviet_collapse_the_oasis_arsenal:7143`, `central_asia_soviet_collapse_the_oasis_guard:7312`, `central_asia_soviet_collapse_desert_republic_settlement:7502`.
- `soviet_collapse_moldova_focus_tree`: `moldova_soviet_collapse_river_guard_brigades:7769`, `moldova_soviet_collapse_romanian_aid_without_annexation:7816`, `moldova_soviet_collapse_neutral_bridge_statute:8153`, `moldova_soviet_collapse_prut_relief_depots:8290`, `moldova_soviet_collapse_river_command_reserve:8470`, `moldova_soviet_collapse_smugglers_and_border_committees:8570`.
- `soviet_collapse_kazakhstan_focus_tree`: `kaz_soviet_collapse_oil_field_protection_orders:10329`, `kaz_soviet_collapse_the_steppe_arsenal:10483`, `kaz_soviet_collapse_caspian_security_detachments:11716`, `kaz_soviet_collapse_army_of_the_open_horizon:11758`, `kaz_soviet_collapse_iranian_caspian_notes:11927`.
- `FTH_soviet_collapse_focus_tree`: `FTH_ukrainian_border_letters:541`, `FTH_anti_puppet_commune_clause:637`, `FTH_commune_court_registers:966`.
- `PRA_soviet_collapse_focus_tree`: `PRA_count_the_locomotives:1269`, `PRA_the_board_overrules_ministers:1345`, `PRA_mobile_workshops:1454`, `PRA_armored_train_schools:1509`, `PRA_charge_for_safe_passage:1577`, `PRA_league_transit_bargain:1604`, `PRA_the_pale_line_endures:1752`.
- `TSC_soviet_collapse_focus_tree`: `TSC_portable_laboratory_trains:1905`, `TSC_perimeter_regiments:2016`.
- `RMC_soviet_collapse_focus_tree`: `RMC_lipetsk_reliquary_workshops:2300`, `RMC_blood_oath_requisitions:2412`, `RMC_dead_volunteer_columns:2488`.
- `DSC_soviet_collapse_focus_tree`: `DSC_call_the_dead_soldiers_congress:2734`, `DSC_voronezh_rearguard_archives:2784`, `DSC_revenant_staff_line:2872`, `DSC_field_hospital_memorials:2942`.
- `NRF_soviet_collapse_focus_tree`: `NRF_count_the_drowned_crews:3370`, `NRF_living_harbor_committees:3394`, `NRF_revenant_admiralty:3419`, `NRF_maps_of_sunken_routes:3566`, `NRF_port_republic_of_the_living:3704`.
- `ICD_soviet_collapse_focus_tree`: `ICD_penza_memorial_workshops:3840`, `ICD_black_seal_requisitions:3950`, `ICD_memorial_battalions:4024`, `ICD_letters_to_grieving_cities:4080`.
- `BSC_soviet_collapse_focus_tree`: `BSC_first_guard:4292`, `BSC_caravan_officer_schools:4546`, `BSC_mountain_route_envoys:4845`, `BSC_tajik_pass_bargains:4888`, `BSC_raiding_column_oaths:4977`, `BSC_desert_airstrips:5021`, `BSC_radical_turn:5223`.
- `TNC_soviet_collapse_focus_tree`: `TNC_tajik_relief_corridors:6019`, `TNC_city_militia_charter:6108`.
- `ALA_soviet_collapse_focus_tree`: `ALA_turkmen_route_bargain:7173`, `ALA_mobile_airstrips:7260`, `ALA_steppe_supply_hubs:7286`.
- `BBH_soviet_collapse_focus_tree`: `BBH_column_schools:8042`, `BBH_armored_car_raids:8179`, `BBH_roving_artillery_crews:8229`, `BBH_column_supply_ledgers:8485`, `BBH_red_and_black_depots:8533`, `BBH_borderless_column_schools:8654`.
- `KRS_soviet_collapse_focus_tree`: `KRS_baltic_worker_letters:9341`, `KRS_anti_party_soviet_clause:9432`, `KRS_icebound_supply_ledger:9622`, `KRS_gulf_mine_watch:9836`, `KRS_port_guard_schools:9887`, `KRS_free_port_conference:9913`.
- `UDC_soviet_collapse_focus_tree`: `UDC_birth:10046`, `UDC_staff_car_workshops:10572`, `UDC_war_plan:10625`, `UDC_radical_turn:11041`.
- `SDZ_soviet_collapse_focus_tree`: `SDZ_every_office_a_watchpost:11691`, `SDZ_document_cart_workshops:11774`, `SDZ_archive_bunker_vaults:11858`, `SDZ_witness_protection_cells:12062`, `SDZ_secure_court_dockets:12088`, `SDZ_signal_van_yards:12162`.
- `GAC_soviet_collapse_focus_tree`: `GAC_green_column_oaths:12965`, `GAC_captured_artillery_caches:12985`, `GAC_partisan_airstrip_meadows:13028`, `GAC_blacksmith_carts:13151`, `GAC_forest_depot_clearings:13174`, `GAC_seed_and_rifle_stores:13203`, `GAC_war_plan:13302`.
- `DHC_soviet_collapse_focus_tree`: `DHC_host_court_registers:13890`, `DHC_cavalry_remount_yards:14032`, `DHC_war_plan:14160`, `DHC_rostov_workshop_contracts:14337`, `DHC_grain_convoy_escorts:14364`, `DHC_convoy_autonomy_guarantees:14414`, `DHC_river_port_tolls:14440`, `DHC_league_passage_bargain:14466`, `DHC_radical_turn:14573`, `DHC_river_and_steppe_compact:14633`.
- `KHC_soviet_collapse_focus_tree`: `KHC_birth:14845`, `KHC_cavalry_remount_yards:15235`, `KHC_war_plan:15363`, `KHC_mountain_crossing_batteries:15393`, `KHC_laba_rear_area:15420`, `KHC_stanitsa_oath_boards:15517`, `KHC_krasnodar_workshop_contracts:15539`, `KHC_grain_corridor_escorts:15563`, `KHC_grain_passage_guarantees:15611`, `KHC_river_port_tolls:15635`, `KHC_league_corridor_bargain:15661`, `KHC_radical_turn:15768`, `KHC_steppe_and_mountain_compact:15828`.
- `FEV_soviet_collapse_focus_tree`: `FEV_customs_house_ledger:16318`, `FEV_railway_militia_charter:16362`, `FEV_radical_turn:16556`, `FEV_harbor_fortress_line:16589`, `FEV_winter_rail_columns:16750`, `FEV_razdolnoye_rear_area:16809`, `FEV_siberian_factory_letters:16837`, `FEV_pacific_observer_missions:16917`, `FEV_sakhalin_ferry_protocols:16940`.
- `SZA_soviet_collapse_focus_tree`: `SZA_radical_turn:17726`, `SZA_winter_column_registers:17904`, `SZA_baikal_rear_area:17959`, `SZA_ural_factory_letters:17986`.
- `UWD_soviet_collapse_focus_tree`: `UWD_birth:18373`, `UWD_war_plan:18714`, `UWD_output_guarantees:18792`, `UWD_radical_turn:18873`, `UWD_perm_field_staff:18930`, `UWD_tagil_machine_tool_ledger:18952`, `UWD_factory_militia_charter:18978`, `UWD_magnitogorsk_steel_quota:19005`, `UWD_kama_foundry_contracts:19134`, `UWD_volga_steel_letters:19189`, `UWD_kurgan_rear_area:19267`.
- `MRC_soviet_collapse_focus_tree`: `mrc_raid_lowland_depots:19825`, `MRC_aul_militia_charter:20234`, `MRC_grozny_workshop_bargain:20328`, `MRC_argun_rear_area:20435`.
- `IUL_soviet_collapse_focus_tree`: `IUL_radical_turn:21103`, `IUL_samara_crossing_ledger:21176`, `IUL_kama_workshop_trust:21241`, `IUL_volga_fortified_crossings:21261`, `IUL_no_requisition_without_federal_vote:21387`, `IUL_rail_and_river_patrols:21420`, `IUL_volga_trade_letters:21446`.
- `BAC_soviet_collapse_focus_tree`: `BAC_war_plan:22274`, `BAC_observer_relief_conference:22408`, `BAC_birobidzhan_council_records:22432`, `BAC_grain_and_relief_escorts:22561`, `BAC_winter_road_columns:22661`, `BAC_far_eastern_letters:22709`, `BAC_autonomy_statute:22845`.
- `ARD_soviet_collapse_focus_tree`: `ARD_birth:23021`, `ARD_first_guard:23037`, `ARD_radical_turn:23378`, `ARD_war_plan:23409`, `ARD_diplomatic_plan:23442`, `ARD_kola_denial_posts:23526`, `ARD_murmansk_port_records:23580`, `ARD_convoy_court_registers:23639`, `ARD_fuel_and_convoy_escorts:23746`, `ARD_winter_convoy_columns:23853`, `ARD_white_sea_port_tolls:23949`, `ARD_league_convoy_bargain:23972`, `ARD_port_neutrality_statute:24042`, `ARD_arctic_port_endurance:24070`.
- `NLC_soviet_collapse_focus_tree`: `NLC_diplomatic_plan:24423`, `NLC_ice_road_customs:24861`, `NLC_heated_workshop_contracts:24962`, `NLC_winter_road_columns:25011`, `NLC_apatity_rear_area:25043`, `NLC_ice_port_tolls:25122`, `NLC_hidden_doctrine:25318`.
- `CFR_soviet_collapse_focus_tree`: none.
- `OGB_soviet_collapse_focus_tree`: `OGB_notables_and_workshops:1377`.
- `MFR_soviet_collapse_focus_tree`: `MFR_the_arsenal_state:2813`.
- Ancient restorations: `KZR_old_border_files:166`, `KZR_expansionist_steppe_levy:225`, `KZR_khazar_charter:269`, `SOG_expansionist_merchant_claims:606`, `KHW_canal_recognition_letters:879`, `KHW_expansionist_water_claims:977`, `KHW_khwarazmian_water_charter:1021`, `KHW_delta_without_a_center:1108`.

### Generic Single-Building Rewards

159 focuses have exactly one `add_building_construction`, no direct equipment, and no idea reward. The most visible clusters:
- `soviet_collapse_internal_republic_focus_tree`: 15.
- `soviet_collapse_central_asia_focus_tree`: 12.
- `soviet_collapse_kazakhstan_focus_tree`: 11.
- `MRC_soviet_collapse_focus_tree`: 9.
- `BSC_soviet_collapse_focus_tree`: 8.
- `FTH_soviet_collapse_focus_tree`: 7.
- `TNC_soviet_collapse_focus_tree`: 7.
- `CFR_soviet_collapse_focus_tree`: 6.
- `KRS_soviet_collapse_focus_tree`: 6.
- `SZA_soviet_collapse_focus_tree`: 6.
- `soviet_collapse_baltic_focus_tree`: 6.

Concrete examples that should be swapped first:
- `CFR_the_trust_office_takes_the_seal:46`, `CFR_emergency_cement_accounts:90`, `CFR_the_first_new_district:574`, `CFR_a_civilian_factory_in_every_capital:600`, `CFR_the_state_that_builds:877`, `CFR_rebuild_russia_without_moscow:1118`.
- `PRA_switchyard_denial_posts:1486`, `PRA_rails_over_capitals:1685`.
- `DSC_dead_regiment_columns:2997`.
- `NRF_arkhangelsk_ice_registers:3346`, `NRF_ghost_convoy_escorts:3541`, `NRF_fleet_that_does_not_dock:3669`.
- `soviet_collapse_internal_republic_focus_tree`: `internal_soviet_collapse_northern_timber_rail_fund:3336`, `internal_soviet_collapse_forest_border_guard_posts:3363`, `internal_soviet_collapse_komi_mine_and_timber_contracts:3484`, `internal_soviet_collapse_northern_republic_accord:3533`, `internal_soviet_collapse_volga_oil_and_workshops:3559`, `internal_soviet_collapse_ural_cavalry_roads:3595`, `internal_soviet_collapse_kazan_ufa_workshop_board:3615`, `internal_soviet_collapse_volga_crossing_militias:3640`, `internal_soviet_collapse_bashkir_oilfield_security:3734`, `internal_soviet_collapse_sevastopol_road_watch:3852`, `internal_soviet_collapse_lena_baikal_relay_posts:4053`, `internal_soviet_collapse_yakut_lena_resource_board:4113`, `internal_soviet_collapse_yakut_arctic_resource_compacts:4162`, `internal_soviet_collapse_tuvan_steppe_guard:4341`, `internal_soviet_collapse_depot_mutual_defense_clauses:4521`.
- `soviet_collapse_central_asia_focus_tree`: `central_asia_soviet_collapse_local_republic_council:6551`, `central_asia_soviet_collapse_tashkent_emergency_ministries:6642`, `central_asia_soviet_collapse_turkestan_city_congress:6721`, `central_asia_soviet_collapse_southern_pass_reserve:6798`, `central_asia_soviet_collapse_desert_scout_columns:6823`, `central_asia_soviet_collapse_dushanbe_mountain_sovereignty:6851`, `central_asia_soviet_collapse_tian_shan_horse_routes:6932`, `central_asia_soviet_collapse_foreign_border_patronage:6956`, `central_asia_soviet_collapse_clear_the_mountain_bands:7110`, `central_asia_soviet_collapse_the_cotton_question:7167`, `central_asia_soviet_collapse_federation_state:7266`, `central_asia_soviet_collapse_ashgabat_desert_authority:7454`.
- `soviet_collapse_kazakhstan_focus_tree`: `kaz_soviet_collapse_the_army_that_crosses_distance:10631`, `kaz_soviet_collapse_turkmen_rail_and_desert_talks:10655`, `kaz_soviet_collapse_british_and_american_engineers:10771`, `kaz_soviet_collapse_uzbek_industrial_bargain:11141`, `kaz_soviet_collapse_mining_workers_councils:11407`, `kaz_soviet_collapse_planned_economy_without_center:11462`, `kaz_soviet_collapse_karaganda_coal_accounting:11499`, `kaz_soviet_collapse_emergency_oil_boards:11521`, `kaz_soviet_collapse_guard_the_mine_heads:11568`, `kaz_soviet_collapse_steppe_defense_council:11870`, `kaz_soviet_collapse_british_mining_observers:11961`.
- `MRC_soviet_collapse_focus_tree`: `mrc_summon_mountain_elders:19778`, `MRC_vladikavkaz_assembly_records:20140`, `MRC_terek_field_staff:20164`, `MRC_pass_court_registers:20188`, `MRC_mountain_market_pledges:20260`, `MRC_caucasus_pack_train_board:20282`, `MRC_pass_fortress_line:20303`, `MRC_winter_pass_columns:20409`, `MRC_dagestan_road_guarantees:20507`.

## Layout and Mutual-Exclusion Findings

No duplicate focus IDs were found, and no mutual exclusion currently has a missing reciprocal reference in the four audited files.

Likely pathline/layout problems:
- `ukr_soviet_collapse_first_republican_line:121` sits at `x=26 y=2` but depends on `ukr_soviet_collapse_count_the_depot_keys:102` at `x=17 y=1`, creating an early long horizontal path. This makes Ukraine feel ugly even though it has 83 focuses.
- Ukraine's foreign/military section mixes `ukr_soviet_collapse_foreign_courts_notice_kyiv:754`, `ukr_soviet_collapse_open_the_liaison_offices:209`, `ukr_soviet_collapse_black_sea_port_ledgers:1217`, and `ukr_soviet_collapse_general_staff_war_college:603` across `x=22-31`, causing likely line clutter through the military branch.
- Ukraine route locks are lore-readable but not cleanly separated: `ukr_soviet_collapse_black_banner_compact:269`, `ukr_soviet_collapse_socialist_republic_without_moscow:232`, `ukr_soviet_collapse_elections_under_shellfire:312`, and `ukr_soviet_collapse_officers_above_parties:538` form a partial exclusion web instead of one clean route family.
- Belarus opening has direct children spread from `blr_soviet_collapse_the_corridor_everyone_wants:9767` at `x=5 y=1` to `blr_soviet_collapse_forest_committees_report_in:8761` at `x=22 y=1`, while the join node `blr_soviet_collapse_which_road_is_belarus:8796` sits at `x=16 y=2`. This creates wide opening lines.
- Belarus has major crossing risks at `blr_soviet_collapse_armored_train_workshops:9860`, which requires `blr_soviet_collapse_minsk_central_dispatch`, `blr_soviet_collapse_brest_is_not_a_gift`, `blr_soviet_collapse_league_supply_timetables`, and `blr_soviet_collapse_swamp_roads_closed` from distant columns.
- Belarus late forest state `blr_soviet_collapse_the_forest_state_rumor:9787` requires `blr_soviet_collapse_the_league_depot_at_minsk`, `blr_soviet_collapse_decentralized_detachments`, and `blr_soviet_collapse_forest_ammunition_hides`, again spanning `x=17-28`.
- CFR governance choices (`CFR_elect_the_site_committees:133`, `CFR_publish_the_planners_charter:163`, `CFR_invite_the_foreign_contract_board:192`, `CFR_the_concrete_committee:220`) use hidden `available` locks but no visible `mutually_exclusive` arrows. Same issue for strategy choices (`CFR_cities_first:347`, `CFR_rails_first:376`, `CFR_factories_first:415`, `CFR_contracts_first:462`). The locks work, but path structure is not visually clean.

## Icon Coverage Table

| Metric | Count |
|---|---:|
| Focus icon assignments | 1,698 |
| Unique icon IDs | 1,498 |
| Reused icon IDs | 140 |
| Missing sprite definitions in `interface/*.gfx` | 0 |

Notable repeated icons:
- 4 uses: `GFX_focus_soviet_collapse_guard_the_radio_stations`, `GFX_ukr_soviet_collapse_democratic`, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`, `GFX_focus_soviet_collapse_steppe_supply_congress`, `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`, `GFX_central_asia_soviet_collapse_steppe_federation`, `GFX_moldova_soviet_collapse_ukrainian_corridor`, `GFX_focus_FEV_diplomatic_plan`, `GFX_focus_SZA_diplomatic_plan`, `GFX_focus_MRC_civil_rule`, `GFX_focus_MRC_foreign`, `GFX_focus_IUL_supply`, `GFX_focus_IUL_war_plan`, `GFX_focus_soviet_collapse_ancient_workshop_compact`, `GFX_focus_soviet_collapse_ancient_guard_old_routes`, `GFX_focus_soviet_collapse_ancient_league_bargain`, `GFX_focus_soviet_collapse_ancient_old_border_files`, `GFX_focus_soviet_collapse_ancient_symbolic_state`, `GFX_focus_soviet_collapse_ancient_restoration_survives`, `GFX_focus_soviet_collapse_ancient_returned_names_endgame`.
- 3 uses: `GFX_focus_soviet_collapse_republican_general_staff`, `GFX_ukr_soviet_collapse_industry`, `GFX_focus_soviet_collapse_secure_ministry_ledgers`, `GFX_baltic_soviet_collapse_wire_rooms`, `GFX_baltic_soviet_collapse_restoration_pact`, `GFX_caucasus_soviet_collapse_defense_compact`, `GFX_moldova_soviet_collapse_eastern_buffer_compact`, `GFX_focus_SZA_economy`, `GFX_focus_UWD_legitimacy`, `GFX_focus_UWD_doctrine`, `GFX_focus_UWD_enemy_front`, `GFX_focus_UWD_civil_rule`, `GFX_focus_IUL_league`, `GFX_focus_IUL_inner_faction`, `GFX_focus_IUL_enemy_front`, `GFX_focus_IUL_diplomatic_plan`, `GFX_focus_CFR_municipal_board_elections`, `GFX_focus_CFR_concrete_republic`, `GFX_focus_CFR_the_builder_state`, `GFX_focus_CFR_civilian_hegemony_project`.

Icon conclusion: icon wiring is valid, but repeated icons still reinforce the user's "generic" complaint in template splinters and ancient restorations.

## Localisation and Reward Mismatches

Mechanical localisation coverage:
- Missing focus name keys: 0.
- Missing focus description keys: 0.

Mismatch/risk list:
- `PRA_count_the_locomotives:1269`, `PRA_armored_train_schools:1509`, `PRA_league_transit_bargain:1604`, `PRA_the_pale_line_endures:1752`: localisation describes rail sovereignty, routes, and recognition; rewards still lean on `train_equipment` and rail buildings. Replace some with state-targeted rail control missions, rail authority thresholds, claims on junction cities, or railway integration decisions.
- `DSC_call_the_dead_soldiers_congress:2734`, `DSC_voronezh_rearguard_archives:2784`, `DSC_revenant_staff_line:2872`: localisation implies supernatural/dead-soldier state power; rewards still include plain infantry equipment. Swap to dead army mobilization variables, special units/templates, war goals, or casualty-roll mechanics.
- `NRF_count_the_drowned_crews:3370`, `NRF_living_harbor_committees:3394`, `NRF_revenant_admiralty:3419`, `NRF_maps_of_sunken_routes:3566`, `NRF_port_republic_of_the_living:3704`: localisation promises convoy ghosts, dead crews, port authority; rewards include plain infantry/convoys. Add naval invasion capacity, ghost convoy missions, port-state claims, dockyard repair decisions, or admirality variable payoffs.
- `CFR_the_trust_office_takes_the_seal:46`, `CFR_emergency_cement_accounts:90`, `CFR_the_first_new_district:574`, `CFR_a_civilian_factory_in_every_capital:600`, `CFR_the_state_that_builds:877`, `CFR_rebuild_russia_without_moscow:1118`: localisation promises construction-state sovereignty, but these remain single-building rewards. CFR has a good mandate/decision system; more focuses should feed or alter it instead of granting one building.
- `ARD_*` convoy-heavy route: 14 direct equipment rewards make the Arctic/White Sea state feel like convoy stockpile buttons instead of an ice-port authority.
- `KHC_*` and `DHC_*`: Cossack/host corridor localisation is stronger than reward behavior; repeated support equipment/convoy rewards should become host councils, cavalry/river missions, claims, or border compacts.

## AI Behavior Gaps

Strengths:
- Every audited focus has `ai_will_do`.
- Several important trees use route-aware modifiers tied to flags, stability, war, and Soviet Collapse variables.

Gaps:
- Many compact 18-23 focus trees still rely mostly on `base` weights plus a few route flags. They do not yet have AI strategy-plan level behavior for aggressive high-chaos outcomes.
- CFR governance/strategy forks use hidden availability locks, but no visible mutual exclusion. AI can choose routes through weights, but player-visible route intent is weaker than the underlying logic.
- Template-sized custom splinters often have route labels (`war_plan`, `diplomatic_plan`, `radical_turn`, `settlement`, `endgame`) but their AI behavior is not clearly tied to geographic objectives, war state, League status, or neighboring opportunities.
- PRA/DSC/NRF have decision integration, but their compact trees should push AI into the decision loop more explicitly by weighting focus choices based on `pra_rail_authority`, `pra_rolling_stock`, `dsc_roll_call_legitimacy`, `dsc_revenant_mobilization`, `nrf_revenant_fleet_authority`, and `nrf_port_muster`.

## Highest-Priority Rework Targets

1. CFR construction state
   - Keep the existing `cfr_construction_mandates`, site registry, contract network, and decisions.
   - Replace single-building rewards with mandate economy, site registry milestones, construction-client targets, temporary construction burdens, and protectorate/rebuild decision unlocks.
   - Add visible `mutually_exclusive` between governance choices and strategy choices.
   - Make `CFR_rebuild_russia_without_moscow` a real end-state payoff: claims/cores/integration decisions or a reconstruction protectorate network, not one factory.

2. PRA Pale Railway Authority
   - Keep existing variables/decisions: `pra_rail_authority`, `pra_rolling_stock`, `pra_consolidate_timetable_courts`, `pra_repair_the_branch_lines`, `pra_drive_the_junction_columns`, `pra_declare_the_moving_state`.
   - Replace repeated train stockpile rewards with targeted rail-junction missions, railway-control claims, armored train unit/template rewards, rail toll decisions, and corridor recognition.
   - Add final split between corridor authority and rail-over-capitals conquest with different postwar handling.

3. DSC Dead Soldiers Congress
   - Keep `dsc_roll_call_legitimacy` and `dsc_revenant_mobilization`.
   - Replace infantry/support stockpile rewards with dead-regiment divisions, veteran town missions, casualty-roll legitimacy thresholds, old-front road claims, and controlled core conversion.
   - The extreme route should be overpowered through manpower/recovery/special units and war goals, not plain equipment.

4. NRF Northern Revenant Fleet
   - Keep `nrf_revenant_fleet_authority` and `nrf_port_muster`.
   - Replace infantry/convoy stockpiles with dead-convoy patrol missions, dockyard resurrection projects, naval invasion and convoy escort modifiers, White Sea lane claims, port-state decisions, and ghost-fleet naval units.
   - The route needs a naval/port expansion branch; current 18-focus size is too small.

5. Factory successors
   - `MFR_soviet_collapse_focus_tree` is the strongest of the factory successors but still needs route payoff polish and fewer plain building rewards.
   - `OGB_soviet_collapse_focus_tree` is too compact at 23 focuses and should gain Volga trade/cultural restoration decisions or a formable/state integration loop.

6. Template splinters with high reward spam
   - Prioritize `ARD`, `KHC`, `UWD`, `DHC`, `FEV`, `BSC`, `BAC`, `IUL`, `NLC`, `KRS`.
   - Convert stockpile-heavy rewards into identity mechanics: convoy court for `ARD`, host/cavalry/river missions for `DHC`/`KHC`, steel quota/arms client ledger for `UWD`, Far Eastern port/ferry diplomacy for `FEV`, mountain/desert route control for `BSC`, Amur relief/autonomy missions for `BAC`, Volga-Ural federal compact for `IUL`, polar science/weather logistics for `NLC`, Baltic free-port navy for `KRS`.

7. Ancient restorations
   - All four 16-focus ancient trees (`KZR`, `SOG`, `KHW`, `ALN`) need broader route families or a shared ancient-restoration decision layer.
   - Suggested swaps: KZR toll/steppe charter decisions, SOG oasis-city league recognition, KHW irrigation/canal authority, ALN mountain pass guard and old-border integration.

8. Ukraine and Belarus layout
   - Ukraine should be re-laid around visibly separated political, military, foreign, industry, and expansion lanes; do not reduce content count.
   - Belarus should be re-spaced to keep rail, forest, league, and foreign-corridor branches from crossing. The worst nodes are `blr_soviet_collapse_armored_train_workshops:9860` and `blr_soviet_collapse_the_forest_state_rumor:9787`.

## Validation Run

Commands/criteria run:
- Read `AGENTS.md`.
- Read `hoi4-focus-trees`, `chaos-redux-events`, `hoi4-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents` skills.
- Consulted offline Paradox wiki snapshots: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Consulted vanilla HOI4 documentation: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`; checked vanilla `common/national_focus/generic.txt` prerequisite/mutual-exclusion examples.
- Brace balance on all four audited focus files: final depth 0, no negative lines.
- Unsupported operators: `rg '<=|>='` found none in the four audited focus files.
- Duplicate focus/non-tree IDs: 0.
- Localisation key coverage for focus names/descriptions: 0 missing.
- Icon definitions: 0 missing sprite definitions for assigned focus icons.
- `git status --short -- gfx/flags interface/flags`: no flag or flag-sprite diff shown.

Skipped validation:
- No in-game focus-tree rendering validation was run.
- No gameplay patch was made, so no live scenario validation was run.

## Changed Files

Changed by this audit:
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_01_event005_focus_full_current_audit.md`

Not changed:
- Gameplay focus files.
- Localisation.
- Interface/GFX.
- `gfx/flags` or any flag sprites.

