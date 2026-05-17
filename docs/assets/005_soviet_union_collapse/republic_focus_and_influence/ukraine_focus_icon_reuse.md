# Ukraine Focus Icon Reuse Ledger

This ledger documents the expanded Ukraine runtime focus icon assignments in `common/national_focus/005_soviet_collapse_republics.txt`.

The tree currently uses 122 focuses and 12 branch-level sprites defined in `interface/005_soviet_collapse_ukraine_icons.gfx`. Each sprite points to a dedicated branch DDS derived from existing generated Event 005 focus art with matching subject matter. This is a deliberate branch-icon reuse package for the current expanded implementation, not evidence that the older literal 208-focus target is implemented.

## Sprite Mapping

| Branch | Sprite | Final DDS | Reuse rationale |
| --- | --- | --- | --- |
| survival | `GFX_ukr_soviet_collapse_survival` | `gfx/interface/goals/ukr_soviet_collapse_survival.dds` | Emergency government art fits the opening ministry, radio, reserve, supply, depot, and survival-cabinet focuses. |
| democratic | `GFX_ukr_soviet_collapse_democratic` | `gfx/interface/goals/ukr_soviet_collapse_democratic.dds` | Republican legality art fits Central Rada memory, elections, parties, courts, press, guarantees, and constitutional focuses. |
| socialist | `GFX_ukr_soviet_collapse_socialist` | `gfx/interface/goals/ukr_soviet_collapse_socialist.dds` | Socialist sovereignty art fits workers, village soviets, militia schools, social property, and internationalist focuses. |
| directory | `GFX_ukr_soviet_collapse_directory` | `gfx/interface/goals/ukr_soviet_collapse_directory.dds` | General-staff art fits military directory, screening, front command, discipline, trains, field police, and reserve-corps focuses. |
| foreign | `GFX_ukr_soviet_collapse_foreign` | `gfx/interface/goals/ukr_soviet_collapse_foreign.dds` | External mission art fits liaison offices, foreign notes, observers, credit files, recognition, patronage-risk, and patronage-safeguard focuses. |
| bread | `GFX_ukr_soviet_collapse_bread` | `gfx/interface/goals/ukr_soviet_collapse_bread.dds` | Grain-and-rail art fits ration ministries, silos, grain convoys, port elevators, quotas, bakeries, and granary-fortress focuses. |
| league | `GFX_ukr_soviet_collapse_league` | `gfx/interface/goals/ukr_soviet_collapse_league.dds` | League liaison art fits republic delegates, cipher rooms, shared arms, border mediation, refugee statutes, and congress security. |
| expansion | `GFX_ukr_soviet_collapse_expansion` | `gfx/interface/goals/ukr_soviet_collapse_expansion.dds` | Black Sea and Dniester art fits ports, customs, corridors, regional staff maps, and beyond-Union ambitions. |
| armed_forces | `GFX_ukr_soviet_collapse_armed_forces` | `gfx/interface/goals/ukr_soviet_collapse_armed_forces.dds` | Field battalion art fits rifle corps, stockpiles, air defense, flotilla watch, cavalry screens, engineers, and doctrine. |
| industry | `GFX_ukr_soviet_collapse_industry` | `gfx/interface/goals/ukr_soviet_collapse_industry.dds` | Factory-committee art fits Donbas, Kharkiv, Dnipro, Odessa, Luhansk, tractors, coal, repair brigades, and procurement. |
| black_banner | `GFX_ukr_soviet_collapse_black_banner` | `gfx/interface/goals/ukr_soviet_collapse_black_banner.dds` | Huliaipole black-flag art fits village committees, free soviet posts, anarchist depot bargains, sabotage, and Black International focuses. |
| identity | `GFX_ukr_soviet_collapse_identity` | `gfx/interface/goals/ukr_soviet_collapse_identity.dds` | Survival-order art fits language, memory, churches, veterans, schools, citizenship, monuments, diaspora, and post-crisis identity. |

## Historical Per-Focus Draft Entries

The entries below belong to the older large-tree draft ledger and should not be read as current implemented focus count evidence. The active implementation uses the compact focus file and docs as the source of truth.

## Per-Focus Entries

| Focus id | Sprite | Status |
| --- | --- | --- |
| `ukr_soviet_collapse_emergency_rada` | `GFX_ukr_soviet_collapse_survival` | deliberate thematic reuse |
| `ukr_soviet_collapse_seal_the_ministry_doors` | `GFX_ukr_soviet_collapse_survival` | deliberate thematic reuse |
| `ukr_soviet_collapse_kyiv_radio_watch` | `GFX_ukr_soviet_collapse_survival` | deliberate thematic reuse |
| `ukr_soviet_collapse_oblast_commissars_accounted` | `GFX_ukr_soviet_collapse_survival` | deliberate thematic reuse |
| `ukr_soviet_collapse_railway_guard_oath` | `GFX_ukr_soviet_collapse_survival` | deliberate thematic reuse |
| `ukr_soviet_collapse_first_reserve_rolls` | `GFX_ukr_soviet_collapse_survival` | deliberate thematic reuse |
| `ukr_soviet_collapse_city_supply_boards` | `GFX_ukr_soviet_collapse_survival` | deliberate thematic reuse |
| `ukr_soviet_collapse_oblast_defense_lines` | `GFX_ukr_soviet_collapse_survival` | deliberate thematic reuse |
| `ukr_soviet_collapse_depot_receipts_in_ukrainian_hands` | `GFX_ukr_soviet_collapse_survival` | deliberate thematic reuse |
| `ukr_soviet_collapse_first_winter_authority` | `GFX_ukr_soviet_collapse_survival` | deliberate thematic reuse |
| `ukr_soviet_collapse_survival_cabinet_settled` | `GFX_ukr_soviet_collapse_survival` | deliberate thematic reuse |
| `ukr_soviet_collapse_restore_the_central_rada_memory` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_municipal_ballot_registers` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_legal_parties_reopen` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_court_the_jurists` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_civil_press_charter` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_minority_guarantee_decrees` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_local_governor_elections` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_constitutional_commission` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_watch_the_security_ministry` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_republic_day_plebiscite` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_constitutional_republic` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_soviets_without_moscow` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_workers_guard_the_plants` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_red_ukrainian_manifesto` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_unionists_inside_the_republic` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_factory_wage_guarantees` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_village_soviet_congress` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_red_militia_schools` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_social_property_statutes` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_purge_central_loyalists_carefully` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_internationalist_broadcasts` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_socialist_sovereign_republic` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_directory_of_national_defense` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_front_command_kyiv` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_officer_screening_boards` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_discipline_the_volunteers` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_river_line_plans` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_armored_train_sections` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_airfield_disarmament_orders` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_field_police_compacts` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_reserve_corps_statute` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_general_staff_without_moscow` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_directory_state` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_open_the_liaison_offices` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_warsaw_transit_notes` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_bucharest_grain_bargain` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_ankara_black_sea_cables` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_london_observer_mission` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_paris_medical_columns` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_washington_credit_files` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_berlin_border_calculus` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_japanese_far_east_probe` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_patronage_risk_board` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_recognized_but_unowned` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_grain_ledger_emergency` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_guard_the_silos` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_bread_card_ministries` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_rail_grain_convoys` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_port_elevator_authority` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_village_quota_bargains` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_ration_police_limits` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_military_bakery_network` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_food_as_recognition` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_granaries_as_fortresses` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_the_bread_state` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_invite_republic_liaisons` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_common_cipher_rooms` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_league_supply_timetable` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_mediate_border_claims` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_league_volunteer_passports` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_anti_reconquest_staff` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_shared_refugee_statutes` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_league_arms_board` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_constitutional_congress_security` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_no_capital_above_the_others` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_league_of_equal_republics` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_black_sea_security_claim` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_dniester_forward_files` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_protect_the_port_approaches` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_carpathian_corridor_watch` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_danube_contact_groups` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_black_sea_protectorate_theory` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_border_referendum_offices` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_secure_the_southern_customs` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_league_alarm_over_kyiv` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_regional_staff_maps` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_map_larger_than_the_union` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_regularize_defense_battalions` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_dnipro_operational_school` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_territorial_rifle_corps` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_armored_stockpile_claims` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_air_defense_over_kyiv` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_black_sea_flotilla_watch` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_cossack_cavalry_screens` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_engineer_bridge_commands` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_partisan_counter_orders` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_combined_front_doctrine` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_army_of_the_republic` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_donbas_factory_accounting` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_kharkiv_design_tables` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_dnipro_steel_contracts` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_odessa_repair_yards` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_luhansk_munitions_cells` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_tractor_plants_to_prime_movers` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_coal_for_the_war_cabinet` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_depot_repair_brigades` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_technical_university_mobilization` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_republican_procurement_board` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_industrial_sovereignty` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_reports_from_huliaipole` | `GFX_ukr_soviet_collapse_black_banner` | deliberate thematic reuse |
| `ukr_soviet_collapse_village_committee_envoys` | `GFX_ukr_soviet_collapse_black_banner` | deliberate thematic reuse |
| `ukr_soviet_collapse_no_requisition_without_receipts` | `GFX_ukr_soviet_collapse_black_banner` | deliberate thematic reuse |
| `ukr_soviet_collapse_free_soviet_border_posts` | `GFX_ukr_soviet_collapse_black_banner` | deliberate thematic reuse |
| `ukr_soviet_collapse_anarchist_depot_bargain` | `GFX_ukr_soviet_collapse_black_banner` | deliberate thematic reuse |
| `ukr_soviet_collapse_black_banner_rail_sabotage` | `GFX_ukr_soviet_collapse_black_banner` | deliberate thematic reuse |
| `ukr_soviet_collapse_committee_courts_problem` | `GFX_ukr_soviet_collapse_black_banner` | deliberate thematic reuse |
| `ukr_soviet_collapse_kyiv_or_no_capitals_debate` | `GFX_ukr_soviet_collapse_black_banner` | deliberate thematic reuse |
| `ukr_soviet_collapse_southern_free_zone_statute` | `GFX_ukr_soviet_collapse_black_banner` | deliberate thematic reuse |
| `ukr_soviet_collapse_black_international_channels` | `GFX_ukr_soviet_collapse_black_banner` | deliberate thematic reuse |
| `ukr_soviet_collapse_no_masters_but_the_front` | `GFX_ukr_soviet_collapse_black_banner` | deliberate thematic reuse |
| `ukr_soviet_collapse_what_the_republic_is_for` | `GFX_ukr_soviet_collapse_identity` | deliberate thematic reuse |
| `ukr_soviet_collapse_language_of_command` | `GFX_ukr_soviet_collapse_identity` | deliberate thematic reuse |
| `ukr_soviet_collapse_memory_of_famine_and_war` | `GFX_ukr_soviet_collapse_identity` | deliberate thematic reuse |
| `ukr_soviet_collapse_churches_under_emergency_law` | `GFX_ukr_soviet_collapse_identity` | deliberate thematic reuse |
| `ukr_soviet_collapse_veterans_of_three_flags` | `GFX_ukr_soviet_collapse_identity` | deliberate thematic reuse |
| `ukr_soviet_collapse_schools_for_a_state_at_war` | `GFX_ukr_soviet_collapse_identity` | deliberate thematic reuse |
| `ukr_soviet_collapse_citizenship_for_the_uncertain` | `GFX_ukr_soviet_collapse_identity` | deliberate thematic reuse |
| `ukr_soviet_collapse_monuments_without_moscow` | `GFX_ukr_soviet_collapse_identity` | deliberate thematic reuse |
| `ukr_soviet_collapse_diaspora_return_offices` | `GFX_ukr_soviet_collapse_identity` | deliberate thematic reuse |
| `ukr_soviet_collapse_republic_after_the_crisis` | `GFX_ukr_soviet_collapse_identity` | deliberate thematic reuse |
| `ukr_soviet_collapse_ukraine_after_the_union` | `GFX_ukr_soviet_collapse_identity` | deliberate thematic reuse |
| `ukr_soviet_collapse_audit_the_patron_ledgers` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_border_promises_registry` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_volunteer_rolls_under_state_seal` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_embassy_observer_limits` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_intelligence_firebreak_rooms` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_credit_without_concessions` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_arms_for_fronts_not_clients` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_league_review_of_patrons` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_diaspora_subscription_bonds` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_neutral_mission_protocols` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_publish_the_foreign_accounts` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_sovereign_patrons_doctrine` | `GFX_ukr_soviet_collapse_foreign` | deliberate thematic reuse |
| `ukr_soviet_collapse_audit_emergency_decrees` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_coalition_ombudsmen` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_provincial_courts_reopen` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_war_crimes_registry` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_exile_precinct_ballots` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_civilian_command_statute` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_demobilization_calendar` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_republic_accountable_to_law` | `GFX_ukr_soviet_collapse_democratic` | deliberate thematic reuse |
| `ukr_soviet_collapse_soviet_trade_councils` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_unionist_amnesty_commissions` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_workers_defense_exports` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_communes_without_commissars` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_socialist_volunteer_charter` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_red_federal_terms` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_anti_bureaucrat_purge_limits` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_republican_socialist_commonwealth` | `GFX_ukr_soviet_collapse_socialist` | deliberate thematic reuse |
| `ukr_soviet_collapse_front_tribunals` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_officer_oath_renewals` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_mobilization_districts` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_strategic_rail_command` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_staff_college_at_war` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_emergency_rank_reforms` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_victory_transition_pledge` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_state_of_the_directory` | `GFX_ukr_soviet_collapse_directory` | deliberate thematic reuse |
| `ukr_soviet_collapse_ration_courts` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_grain_export_licenses` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_fortress_granary_districts` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_famine_memory_safeguards` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_rail_ration_priority` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_farmers_bargain_congress` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_hungry_cities_compact` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_granary_state_doctrine` | `GFX_ukr_soviet_collapse_bread` | deliberate thematic reuse |
| `ukr_soviet_collapse_rotating_secretariat` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_common_frontier_fund` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_disputed_ministries_arbitration` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_league_refugee_bank` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_member_army_standards` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_sanctions_against_patronage` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_charter_of_equal_capitals` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_league_permanent_council` | `GFX_ukr_soviet_collapse_league` | deliberate thematic reuse |
| `ukr_soviet_collapse_black_sea_customs_mission` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_odessa_security_conference` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_dniester_observer_line` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_danube_guarantee_notes` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_protectorate_without_annexation` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_border_plebiscite_commissions` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_league_containment_bargain` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_dnipro_commonwealth` | `GFX_ukr_soviet_collapse_expansion` | deliberate thematic reuse |
| `ukr_soviet_collapse_reserve_rotation_law` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_river_flotilla_cadres` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_air_warning_belt` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_depot_artillery_schools` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_railway_corps_command` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_intelligence_platoon_net` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_veteran_settlement_rolls` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_national_defense_army` | `GFX_ukr_soviet_collapse_armed_forces` | deliberate thematic reuse |
| `ukr_soviet_collapse_mine_safety_boards` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_machine_tool_census` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_port_cranes_priority` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_electrical_grid_guards` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_wartime_patents_bureau` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_foreign_contracts_audit` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_reconstruction_bonds` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
| `ukr_soviet_collapse_arsenal_economy` | `GFX_ukr_soviet_collapse_industry` | deliberate thematic reuse |
