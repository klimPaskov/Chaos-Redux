# Event005 Soviet Collapse Focus Tree Auditor Full Goal Audit

Date: 2026-06-05
Subagent role: `chaosx_focus_tree_auditor`
Scope: Event005 Soviet Collapse focus trees only.

## References consulted

- Repo instructions: `/home/klim/projects/chaos_redux/AGENTS.md`
- Repo skill: `hoi4-focus-trees`
- Related repo skill opened for focus-decision connections: `hoi4-decisions-missions`
- Offline Paradox wiki snapshot pages:
  - `Data structures - Hearts of Iron 4 Wiki.md`
  - `Triggers - Hearts of Iron 4 Wiki.md`
  - `Effect - Hearts of Iron 4 Wiki.md`
  - `Modifiers - Hearts of Iron 4 Wiki.md`
  - `Localisation - Hearts of Iron 4 Wiki.md`
  - `Scopes - Hearts of Iron 4 Wiki.md`
  - `On actions - Hearts of Iron 4 Wiki.md`
  - `Event modding - Hearts of Iron 4 Wiki.md`
  - `Decision modding - Hearts of Iron 4 Wiki.md`
  - `Idea modding - Hearts of Iron 4 Wiki.md`
  - `AI modding - Hearts of Iron 4 Wiki.md`
  - `National focus modding - Hearts of Iron 4 Wiki.md`
- Vanilla documentation:
  - `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/modifiers_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/script_collection_input.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/script_collection_operator.md`
- Vanilla precedent inspected:
  - `/home/klim/projects/Hearts of Iron IV/common/national_focus/generic.txt`

Relevant syntax points used during the audit:

- Multiple focuses inside one `prerequisite = { ... }` block are OR prerequisites. Multiple `prerequisite` blocks are AND prerequisites.
- A prerequisite focus should sit above its dependent focus. The focus tree renderer can draw bad or confusing path sprites when this is violated.
- Duplicate focus IDs can break path lines.
- Focus rewards are effect blocks; a focus is not considered complete until its reward finishes.
- Decision `allowed` conditions are checked only once; `visible` and `available` are dynamic.

## Files inspected

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

No separate Event005 League focus file was found. League and special-country focus content is embedded in the republics, custom splinters, factory successors, and ancient restorations files above.

## Files changed

- Added this handoff:
  - `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_focus_tree_auditor_full_goal_audit.md`

No gameplay focus files were changed. No Event006 files were changed. No flag assets, flag sprites, or `gfx/flags` files were touched.

## Tree inventory

Current parsed inventory: 41 focus trees.

`common/national_focus/005_soviet_collapse_republics.txt`

- Line 19: `soviet_collapse_ukraine_focus_tree`, 83 focuses.
- Line 2326: `soviet_collapse_breakaway_focus_tree`, 36 focuses.
- Line 3138: `soviet_collapse_internal_republic_focus_tree`, 62 focuses.
- Line 4658: `soviet_collapse_baltic_focus_tree`, 42 focuses.
- Line 5621: `soviet_collapse_caucasus_focus_tree`, 40 focuses.
- Line 6542: `soviet_collapse_central_asia_focus_tree`, 45 focuses.
- Line 7678: `soviet_collapse_moldova_focus_tree`, 48 focuses.
- Line 8820: `soviet_collapse_belarus_focus_tree`, 53 focuses.
- Line 10146: `soviet_collapse_kazakhstan_focus_tree`, 92 focuses.

`common/national_focus/005_soviet_collapse_custom_splinters.txt`

- Line 16: `FTH_soviet_collapse_focus_tree`, 47 focuses.
- Line 1382: `PRA_soviet_collapse_focus_tree`, 22 focuses.
- Line 2022: `TSC_soviet_collapse_focus_tree`, 18 focuses.
- Line 2532: `RMC_soviet_collapse_focus_tree`, 18 focuses.
- Line 3010: `DSC_soviet_collapse_focus_tree`, 18 focuses.
- Line 3550: `NRF_soviet_collapse_focus_tree`, 18 focuses.
- Line 4056: `ICD_soviet_collapse_focus_tree`, 18 focuses.
- Line 4526: `BSC_soviet_collapse_focus_tree`, 47 focuses.
- Line 5670: `TNC_soviet_collapse_focus_tree`, 47 focuses.
- Line 6805: `ALA_soviet_collapse_focus_tree`, 47 focuses.
- Line 7916: `BBH_soviet_collapse_focus_tree`, 47 focuses.
- Line 9110: `KRS_soviet_collapse_focus_tree`, 47 focuses.
- Line 10335: `UDC_soviet_collapse_focus_tree`, 47 focuses.
- Line 11543: `SDZ_soviet_collapse_focus_tree`, 47 focuses.
- Line 12793: `GAC_soviet_collapse_focus_tree`, 47 focuses.
- Line 13960: `DHC_soviet_collapse_focus_tree`, 47 focuses.
- Line 15159: `KHC_soviet_collapse_focus_tree`, 47 focuses.
- Line 16324: `FEV_soviet_collapse_focus_tree`, 47 focuses.
- Line 17515: `SZA_soviet_collapse_focus_tree`, 47 focuses.
- Line 18684: `UWD_soviet_collapse_focus_tree`, 47 focuses.
- Line 19871: `MRC_soviet_collapse_focus_tree`, 47 focuses.
- Line 21044: `IUL_soviet_collapse_focus_tree`, 47 focuses.
- Line 22184: `BAC_soviet_collapse_focus_tree`, 47 focuses.
- Line 23317: `ARD_soviet_collapse_focus_tree`, 47 focuses.
- Line 24516: `NLC_soviet_collapse_focus_tree`, 47 focuses.

`common/national_focus/005_soviet_collapse_factory_successors.txt`

- Line 19: `CFR_soviet_collapse_focus_tree`, 47 focuses.
- Line 1048: `OGB_soviet_collapse_focus_tree`, 23 focuses.
- Line 1611: `MFR_soviet_collapse_focus_tree`, 58 focuses.

`common/national_focus/005_soviet_collapse_ancient_restorations.txt`

- Line 14: `KZR_soviet_collapse_ancient_focus_tree`, 16 focuses.
- Line 424: `SOG_soviet_collapse_ancient_focus_tree`, 16 focuses.
- Line 828: `KHW_soviet_collapse_ancient_focus_tree`, 16 focuses.
- Line 1236: `ALN_soviet_collapse_ancient_focus_tree`, 16 focuses.

## Current state summary

The Event005 focus surface is much larger than a generic placeholder pass. Major republic trees such as Ukraine, Kazakhstan, the internal republic tree, Belarus, Moldova, and the factory successors have meaningful focus counts and several connections to Event005 mechanics, including League preparation, release pressure, expansion pressure, unit spawns, railway and supply work, and decision unlocks.

The main remaining problem is not absence of content everywhere. It is uneven depth and a reward model that leans too hard on repeated generic helper bundles. Several special concept countries are still too shallow for the user's target: railway countries, dead-congress states, naval directorates, observatory/revenant concepts, and ancient restorations need stronger country-specific mechanics instead of compact templates.

No duplicate focus IDs were found. No missing `completion_reward` blocks were found. No nonreciprocal mutual exclusions were found. No same-tree missing prerequisites were found. No prerequisite focus was found below its dependent focus. The remaining structural issues are primarily pathline and visual layout problems.

## Structural and layout findings

### Same-row focuses too close together

These pairs are one grid column apart on the same row and should be separated to avoid crowding, overlap, or unreadable branch geometry.

- `common/national_focus/005_soviet_collapse_republics.txt` line 1144: `ukr_soviet_collapse_republican_deep_battle` and line 1465: `ukr_soviet_collapse_advisers_without_flags`, both at row `y = 8`, columns `x = 26` and `x = 27`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 3881: `internal_soviet_collapse_crimean_tatar_councils` and line 4085: `internal_soviet_collapse_taiga_steppe_self_rule`, both at row `y = 5`, columns `x = 20` and `x = 21`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 6936: `central_asia_soviet_collapse_desert_scout_columns` and line 7446: `central_asia_soviet_collapse_the_basmachi_amnesty_ledger`, both at row `y = 6`, columns `x = 7` and `x = 6`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 7016: `central_asia_soviet_collapse_bishkek_pass_council` and line 7492: `central_asia_soviet_collapse_khwarazm_restoration_debate`, both at row `y = 8`, columns `x = 8` and `x = 9`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 7194: `central_asia_soviet_collapse_negotiate_with_the_mountain_bands` and line 7276: `central_asia_soviet_collapse_the_cotton_question`, both at row `y = 4`, columns `x = 4` and `x = 3`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 7901: `moldova_soviet_collapse_river_guard_brigades` and line 8020: `moldova_soviet_collapse_ukrainian_grain_road`, both at row `y = 5`, columns `x = 14` and `x = 15`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 8120: `moldova_soviet_collapse_reject_the_union_question` and line 8553: `moldova_soviet_collapse_tiraspol_depot_belt`, both at row `y = 7`, columns `x = 15` and `x = 14`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 9828: `blr_soviet_collapse_join_the_league_when_war_comes` and line 10070: `blr_soviet_collapse_the_green_rail_pact`, both at row `y = 10`, columns `x = 21` and `x = 22`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 10396: `kaz_soviet_collapse_the_alash_courts` and line 10608: `kaz_soviet_collapse_the_steppe_arsenal`, both at row `y = 5`, columns `x = 22` and `x = 23`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 10533: `kaz_soviet_collapse_domestic_resource_state` and line 10923: `kaz_soviet_collapse_no_concession_without_a_republic`, both at row `y = 7`, columns `x = 20` and `x = 21`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 10556: `kaz_soviet_collapse_league_resource_pool` and line 11472: `kaz_soviet_collapse_local_notable_compacts`, both at row `y = 8`, columns `x = 23` and `x = 24`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 10817: `kaz_soviet_collapse_steppe_federation_charter` and line 11930: `kaz_soviet_collapse_call_the_steppe_congress`, both at row `y = 6`, columns `x = 10` and `x = 9`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 10923: `kaz_soviet_collapse_no_concession_without_a_republic` and line 11684: `kaz_soviet_collapse_copper_and_chrome_ledgers`, both at row `y = 7`, columns `x = 21` and `x = 22`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 11093: `kaz_soviet_collapse_the_written_alash_program` and line 11539: `kaz_soviet_collapse_mining_workers_councils`, both at row `y = 7`, columns `x = 26` and `x = 27`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 11093: `kaz_soviet_collapse_the_written_alash_program` and line 11563: `kaz_soviet_collapse_collective_farm_bargains`, both at row `y = 7`, columns `x = 26` and `x = 25`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 11403: `kaz_soviet_collapse_the_southern_republics_write_together` and line 11951: `kaz_soviet_collapse_uzbek_supply_delegates`, both at row `y = 8`, columns `x = 7` and `x = 6`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 11403: `kaz_soviet_collapse_the_southern_republics_write_together` and line 11966: `kaz_soviet_collapse_kyrgyz_mountain_liaisons`, both at row `y = 8`, columns `x = 7` and `x = 8`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 11456: `kaz_soviet_collapse_semey_legal_circle` and line 11563: `kaz_soviet_collapse_collective_farm_bargains`, both at row `y = 7`, columns `x = 24` and `x = 25`.
- `common/national_focus/005_soviet_collapse_factory_successors.txt` line 2009: `MFR_rifles_before_speeches` and line 2531: `MFR_workers_must_not_flee`, both at row `y = 10`, columns `x = 7` and `x = 6`.
- `common/national_focus/005_soviet_collapse_factory_successors.txt` line 2009: `MFR_rifles_before_speeches` and line 2555: `MFR_builders_waste_steel`, both at row `y = 10`, columns `x = 7` and `x = 8`.
- `common/national_focus/005_soviet_collapse_factory_successors.txt` line 2076: `MFR_standardize_the_rifle_line` and line 2624: `MFR_iron_liturgy_watches`, both at row `y = 11`, columns `x = 10` and `x = 9`.

### Focuses placed between mutually exclusive alternatives

These focus positions sit horizontally between mutually exclusive alternatives. Even where script logic is valid, the layout can imply that the middle focus belongs to both sides or can cause confusing pathline geometry.

- `common/national_focus/005_soviet_collapse_republics.txt` line 777: `ukr_soviet_collapse_free_soil_compromise` is between mutually exclusive focuses line 256: `ukr_soviet_collapse_socialist_republic_without_moscow` and line 287: `ukr_soviet_collapse_black_banner_compact`.
- `common/national_focus/005_soviet_collapse_republics.txt` line 9400: `blr_soviet_collapse_foreign_aid_through_brest` is between mutually exclusive focuses line 9004: `blr_soviet_collapse_national_council_of_minsk` and line 9032: `blr_soviet_collapse_socialist_autonomy_without_moscow`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 893: `FTH_industry_plan` is between mutually exclusive focuses line 544: `FTH_settlement` and line 582: `FTH_radical_turn`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 1761: `PRA_passport_of_the_moving_state` is between mutually exclusive focuses line 1536: `PRA_the_board_overrules_ministers` and line 1568: `PRA_armored_train_directorate`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 2256: `TSC_observatory_guard` is between mutually exclusive focuses line 2188: `TSC_the_committee_of_instruments` and line 2221: `TSC_the_committee_of_signs`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 2722: `RMC_reliquary_guard` is between mutually exclusive focuses line 2634: `RMC_communes_of_witnesses` and line 2667: `RMC_cadres_of_resurrection`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 3222: `DSC_field_hospital_memorials` is between mutually exclusive focuses line 3138: `DSC_witness_officers` and line 3172: `DSC_revenant_staff_line`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 3747: `NRF_icebound_marine_guard` is between mutually exclusive focuses line 3648: `NRF_living_harbor_committees` and line 3682: `NRF_revenant_admiralty`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 4244: `ICD_funeral_guard` is between mutually exclusive focuses line 4156: `ICD_commissars_of_last_addresses` and line 4190: `ICD_commissars_who_do_not_die`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 8737: `BBH_industry_plan` is between mutually exclusive focuses line 8671: `BBH_settlement` and line 8704: `BBH_radical_turn`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 9839: `KRS_hidden_doctrine` is between mutually exclusive focuses line 9474: `KRS_settlement` and line 9505: `KRS_radical_turn`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 13465: `GAC_hidden_mill_ledgers` is between mutually exclusive focuses line 13756: `GAC_settlement` and line 13792: `GAC_radical_turn`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 13490: `GAC_blacksmith_carts` is between mutually exclusive focuses line 13756: `GAC_settlement` and line 13792: `GAC_radical_turn`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 13830: `GAC_industry_plan` is between mutually exclusive focuses line 13756: `GAC_settlement` and line 13792: `GAC_radical_turn`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 14723: `DHC_winter_road_columns` is between mutually exclusive focuses line 14870: `DHC_settlement` and line 14906: `DHC_radical_turn`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 14993: `DHC_industry_plan` is between mutually exclusive focuses line 14870: `DHC_settlement` and line 14906: `DHC_radical_turn`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 15913: `KHC_winter_corridor_columns` is between mutually exclusive focuses line 16056: `KHC_settlement` and line 16092: `KHC_radical_turn`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 16176: `KHC_industry_plan` is between mutually exclusive focuses line 16056: `KHC_settlement` and line 16092: `KHC_radical_turn`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 18204: `SZA_industry_plan` is between mutually exclusive focuses line 18019: `SZA_settlement` and line 18052: `SZA_radical_turn`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 20903: `MRC_industry_plan` is between mutually exclusive focuses line 20394: `MRC_settlement` and line 20427: `MRC_radical_turn`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 23783: `ARD_industry_plan` is between mutually exclusive focuses line 23658: `ARD_settlement` and line 23689: `ARD_radical_turn`.
- `common/national_focus/005_soviet_collapse_factory_successors.txt` line 1253: `OGB_friday_schools_and_court_records` is between mutually exclusive focuses line 1126: `OGB_scholars_guard_the_charter` and line 1150: `OGB_clerics_guard_the_charter`.
- `common/national_focus/005_soviet_collapse_factory_successors.txt` line 1771: `MFR_armorers_elect_delegates` is between mutually exclusive focuses line 1740: `MFR_officers_chair_the_board` and line 1797: `MFR_merchants_of_ammunition`.
- `common/national_focus/005_soviet_collapse_factory_successors.txt` line 1830: `MFR_eternal_arsenal` is between mutually exclusive focuses line 1740: `MFR_officers_chair_the_board` and line 1797: `MFR_merchants_of_ammunition`.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 288: `KZR_khazar_charter` is between mutually exclusive focuses line 211: `KZR_symbolic_crossing_state` and line 238: `KZR_expansionist_steppe_levy`.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 696: `SOG_sogdian_city_charter` is between mutually exclusive focuses line 620: `SOG_symbolic_city_league` and line 646: `SOG_expansionist_merchant_claims`.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 1094: `KHW_khwarazmian_water_charter` is between mutually exclusive focuses line 1019: `KHW_symbolic_oasis_authority` and line 1044: `KHW_expansionist_water_claims`.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 1505: `ALN_alan_pass_charter` is between mutually exclusive focuses line 1428: `ALN_symbolic_pass_principality` and line 1453: `ALN_expansionist_mountain_claims`.

### Vertical pathline crossing

- `common/national_focus/005_soviet_collapse_republics.txt` line 2978: `soviet_collapse_rail_hub_or_mountain_pass` has a vertical prerequisite path from line 2418: `soviet_collapse_depot_repair_crews` that passes through line 2806: `soviet_collapse_old_underground_branch` at position `x = 14`, `y = 4`. This is in the fallback breakaway focus tree.

## Reward-spam and helper-spam findings

Top repeated reward helpers found in Event005 focus files:

- 142 calls: `soviet_collapse_apply_focus_depot_and_supply_control`
- 131 calls: `soviet_collapse_apply_focus_military_consolidation`
- 108 calls: `soviet_collapse_apply_focus_legal_recognition`
- 92 calls: `soviet_collapse_apply_focus_republican_compact_plan`
- 67 calls: `soviet_collapse_apply_objective_source_pressure_delta`
- 66 calls: `soviet_collapse_apply_focus_foreign_channel`
- 64 calls: `soviet_collapse_apply_focus_security_supply_plan`
- 54 calls: `soviet_collapse_apply_focus_high_chaos_identity`
- 51 calls: `soviet_collapse_apply_focus_league_preparation`
- 46 calls: `soviet_collapse_apply_focus_chaos_assault_plan`
- 42 calls: `soviet_collapse_apply_focus_foreign_recognition_plan`
- 40 calls: `soviet_collapse_apply_focus_foreign_league_plan`
- 32 calls: `soviet_collapse_apply_focus_chaos_legitimacy_plan`
- 31 calls: `soviet_collapse_apply_focus_lawful_supply_plan`
- 27 calls: `soviet_collapse_apply_custom_splinter_enemy_front_identity`
- 26 calls each:
  - `soviet_collapse_apply_custom_splinter_expansion_claims`
  - `soviet_collapse_apply_custom_splinter_league_identity`
  - `soviet_collapse_apply_focus_chaos_supply_plan`
  - `soviet_collapse_apply_focus_league_security_plan`
  - `soviet_collapse_apply_high_chaos_neighbor_expansion_plan`
- 24 calls each:
  - `soviet_collapse_add_republic_focus_recovery_progress`
  - `soviet_collapse_apply_focus_civil_military_authority_plan`
- 23 calls each:
  - `soviet_collapse_apply_focus_socialist_sovereignty`
  - `soviet_collapse_spawn_custom_splinter_assault_columns_payload`
- 20 calls each:
  - `soviet_collapse_apply_focus_foreign_security_plan`
  - `soviet_collapse_apply_focus_foreign_supply_plan`
- 19 calls: `soviet_collapse_apply_focus_league_logistics_plan`
- 17 calls each:
  - `soviet_collapse_apply_breakaway_neighbor_conflict_plan`
  - `soviet_collapse_spawn_custom_splinter_assault_columns`
- 16 calls: `soviet_collapse_apply_focus_diplomatic_plan`

This is not automatically invalid. Shared helpers are useful for keeping Event005 tuning central. The problem is that many focus rewards are several generic helpers plus direct effects, so the player's focus choice can feel like a repeated payload template instead of a country-defining branch. The next pass should keep the power level high but collapse repeated bundles into fewer tag-specific scripted effects with clear decision, army, core, construction, rail, or naval consequences.

Representative dense rewards that should be reviewed first:

- `common/national_focus/005_soviet_collapse_republics.txt` line 2051: `ukr_soviet_collapse_endgame_a_ukraine_outside_the_old_map`, 3 helper calls.
- `common/national_focus/005_soviet_collapse_republics.txt` line 3286: `internal_soviet_collapse_security_council`, 3 helper calls plus decision unlock.
- `common/national_focus/005_soviet_collapse_republics.txt` line 9061: `blr_soviet_collapse_military_transit_directorate`, 4 helper calls plus decision unlock.
- `common/national_focus/005_soviet_collapse_republics.txt` line 9601: `blr_soviet_collapse_partisans_or_army`, 3 helper calls plus multiple direct effects.
- `common/national_focus/005_soviet_collapse_republics.txt` line 9795: `blr_soviet_collapse_prepare_league_freight_tables`, 3 helper calls plus rail, building, and decision unlock effects.
- `common/national_focus/005_soviet_collapse_republics.txt` line 11064: `kaz_soviet_collapse_the_southern_republics_do_not_kneel`, 3 helper calls.
- `common/national_focus/005_soviet_collapse_republics.txt` line 11899: `kaz_soviet_collapse_army_of_the_open_horizon`, 2 helper calls plus 6 direct effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 51: `FTH_first_guard`, 4 helper calls plus 4 direct effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 90: `FTH_stores`, 4 helper calls plus 3 direct effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 130: `FTH_legitimacy`, 5 helper calls.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 278: `FTH_league`, 7 helper calls.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 317: `FTH_foreign`, 6 helper calls.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 416: `FTH_supply`, 5 helper calls plus 3 direct effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 1308: `FTH_communes_without_capitals`, 4 helper calls plus war support.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 1568: `PRA_armored_train_directorate`, 4 helper calls plus rail and building effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 1684: `PRA_switchyard_denial_posts`, 4 helper calls plus 5 direct effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 1880: `PRA_seize_the_junction_cities`, 4 helper calls plus 6 direct effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 1923: `PRA_rails_over_capitals`, 3 helper calls plus wargoal and AI effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 2447: `TSC_starfall_mandate`, 4 helper calls plus wargoal and AI effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 2948: `RMC_resurrection_without_state`, 4 helper calls plus wargoal and AI effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 3017: `DSC_call_the_dead_soldiers_congress`, 6 helper calls plus 6 direct effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 3510: `DSC_memorial_frontier_state`, 2 helper calls plus 8 direct effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 3934: `NRF_fleet_that_does_not_dock`, 3 helper calls plus naval direct effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 3994: `NRF_northern_revenant_fleet`, 4 helper calls plus naval, wargoal, AI, and decision effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 4463: `ICD_commissariat_without_end`, 4 helper calls plus wargoal and AI effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 4902: `BSC_war_plan`, 3 helper calls.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 5566: `BSC_hidden_doctrine`, 3 helper calls.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` lines 10490, 10563, 10589, 10615, 10950, 11432, and 11459: UDC command-network focuses repeatedly pair generic helpers with `soviet_collapse_apply_udc_command_network_focus`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 23722: `ARD_war_plan`, 4 helper calls plus naval or direct effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 23754: `ARD_diplomatic_plan`, 3 helper calls.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 24018: `ARD_naval_infantry_yards`, 1 helper call plus 7 direct effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 25640: `NLC_hidden_doctrine`, 3 helper calls plus 4 direct effects.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 25673: `NLC_extreme_gate`, 4 helper calls plus 4 direct effects.
- `common/national_focus/005_soviet_collapse_factory_successors.txt` line 346: `CFR_rails_first`, dense construction and rail payload.
- `common/national_focus/005_soviet_collapse_factory_successors.txt` line 516: `CFR_the_first_new_district`, dense construction-state payload.
- `common/national_focus/005_soviet_collapse_factory_successors.txt` line 810: `CFR_the_state_that_builds`, concept-appropriate but dense state-building payload.
- `common/national_focus/005_soviet_collapse_factory_successors.txt` line 1567: `OGB_endgame_*`, dense endgame payload.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 240: `KZR_expansionist_steppe_levy`, dense expansion payload.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 356: `KZR_returned_names_endgame`, dense endgame payload.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 381: `KZR_road_beyond_the_caspian`, dense expansion payload.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 648: `SOG_expansionist_merchant_claims`, dense expansion payload.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 760: `SOG_returned_names_endgame`, dense endgame payload.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 785: `SOG_cities_beyond_the_desert`, dense expansion payload.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 1046: `KHW_expansionist_water_claims`, dense expansion payload.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 1168: `KHW_returned_names_endgame`, dense endgame payload.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 1193: `KHW_delta_without_a_center`, dense expansion payload.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 1455: `ALN_expansionist_mountain_claims`, dense expansion payload.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 1570: `ALN_returned_names_endgame`, dense endgame payload.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` line 1596: `ALN_every_pass_a_border`, dense expansion payload.

## Highest-priority route redesign work

1. `DSC`, dead soldiers congress, starts at `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 3010.

   Current status: It has aggressive and thematic rewards, especially `DSC_call_the_dead_soldiers_congress` at line 3017 and `DSC_memorial_frontier_state` at line 3510, but the tree is only 18 focuses and does not yet have enough route depth for the user's target. It should become a deliberately overpowered expansion and coring country with a dead-congress mechanic at the center.

   Implementation-ready work:
   - Split into at least politics, memorial economy, undead/revenant army, expansion, coring, and League-pressure branches.
   - Add focuses that unlock or strengthen decisions for claiming, coring, and forcibly integrating bordering Soviet successor states.
   - Make the congress mechanic produce escalating costs and payoffs: manpower, compliance, cores, unit spawns, resistance suppression, and war goals.
   - Replace repeated generic reward bundles with `DSC`-specific scripted effects that describe congressional war mandates, corpse-roll mobilization, memorial logistics, and border incorporation.

2. `NRF`, northern revenant fleet, starts at `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 3550.

   Current status: It has naval identity in `NRF_fleet_that_does_not_dock` at line 3934 and `NRF_northern_revenant_fleet` at line 3994, but the tree is only 18 focuses. Naval directorates should have a full naval war route, not only naval XP and endgame effects.

   Implementation-ready work:
   - Add shipyard, convoy, naval invasion, mine warfare, raiding, port seizure, and Baltic/Arctic sea-lane branches.
   - Tie naval expansion to Event005 war and League mechanics through decisions for naval evacuation, convoy seizure, coastal claims, and expeditionary port access.
   - Add overpowered but concept-specific naval payloads: dockyards, naval invasion capacity, marines, admirals, convoy raiding bonuses, port supply, coastal state claims, and naval combat ideas.
   - Move generic helper bundles into fewer `NRF`-specific effects.

3. `PRA`, railway country, starts at `common/national_focus/005_soviet_collapse_custom_splinters.txt` line 1382.

   Current status: It has railway and supply identity, including `PRA_armored_train_directorate` at line 1568, `PRA_switchyard_denial_posts` at line 1684, `PRA_seize_the_junction_cities` at line 1880, and `PRA_rails_over_capitals` at line 1923. At 22 focuses, it is still too small for the requested railway-country fantasy.

   Implementation-ready work:
   - Deepen into rail authority, armored train, supply hub, corridor war, League transit, and industrial evacuation branches.
   - Add focus-decision connections for building rails and supply hubs in controlled and claimed states.
   - Let the country weaponize infrastructure: state modifiers, enemy supply disruption, strategic redeployment bonuses, armored train templates, and war goals against rail junctions.
   - Reduce helper spam by creating one or two `PRA` rail-network payload effects that combine the intended overpowered rail/supply package.

4. Ancient restorations: `KZR`, `SOG`, `KHW`, and `ALN`, in `common/national_focus/005_soviet_collapse_ancient_restorations.txt`.

   Current status: Each tree has only 16 focuses. The symbolic and expansionist alternatives are visible, but the post-choice content converges too quickly and the common charter focuses sit between mutually exclusive alternatives:
   - `KZR_khazar_charter` line 288 between line 211 and line 238.
   - `SOG_sogdian_city_charter` line 696 between line 620 and line 646.
   - `KHW_khwarazmian_water_charter` line 1094 between line 1019 and line 1044.
   - `ALN_alan_pass_charter` line 1505 between line 1428 and line 1453.

   Implementation-ready work:
   - Expand each to distinct symbolic/diplomatic and expansionist/militarist routes.
   - Add local economy and military branches tied to the ancient concept: river and oasis management for `KHW`, caravan/city wealth for `SOG`, steppe levy and Caspian routes for `KZR`, mountain pass military control for `ALN`.
   - Keep expansion branches aggressively overpowered with claims, war goals, cores, and route-specific units, but make the symbolic branches use League diplomacy, legitimacy, and federation mechanics.
   - Reposition convergence focuses so they do not sit between mutually exclusive choices.

5. Factory successors: `CFR`, `OGB`, and `MFR`, in `common/national_focus/005_soviet_collapse_factory_successors.txt`.

   Current status: `CFR` is one of the stronger concept matches. `CFR_the_state_that_builds` at line 810 gives the construction-state fantasy a clear mechanical center. `MFR` is aggressive and heavily industrialized, but has several layout findings and dense rewards. `OGB` is shorter at 23 focuses and should be checked for whether its concept warrants full-depth expansion.

   Implementation-ready work:
   - Preserve `CFR`'s construction-state identity and deepen decision hooks around district construction, infrastructure, repair, and state development.
   - Fix `MFR` close-position issues around lines 2009, 2531, 2555, 2076, and 2624.
   - Separate `MFR` officer, merchant, worker, arsenal, and war-production branches visually and mechanically.
   - Review `OGB` for additional education, court, charter, and militia mechanics if it remains a special successor rather than a minor fallback.

6. Custom 47-focus splinter family in `common/national_focus/005_soviet_collapse_custom_splinters.txt`.

   Current status: Many 47-focus trees have enough raw size, but still share a common skeleton: birth, first guard, stores, legitimacy, rival, League, foreign, supply, war plan, hidden doctrine, industry plan, settlement, radical turn. This is useful scaffolding but too visible as repeated content.

   Implementation-ready work:
   - Keep the branch skeleton only where it supports readability.
   - Add tag-specific route mechanics and rewards to high-priority concept countries before adding more generic focuses.
   - Start with tags that already show specific mechanics or user priority: `FTH`, `BSC`, `UDC`, `GAC`, `DHC`, `KHC`, `ARD`, and `NLC`.
   - Replace repeated helper bundles with tag-specific scripted effects that include the common baseline internally and add unique consequences.

7. Republic trees in `common/national_focus/005_soviet_collapse_republics.txt`.

   Current status: Ukraine, Kazakhstan, internal republics, Belarus, Moldova, Central Asia, Caucasus, Baltic, and the fallback breakaway tree all have broader content than the small special trees. Kazakhstan and Ukraine are especially deep. Remaining work is mainly layout cleanup, reducing repeated helper bundles, and tightening country-specific links to Event005 decisions, League coordination, release pressure, expansion, cores, and units.

   Implementation-ready work:
   - Fix Kazakhstan crowding around lines 10396 through 11966.
   - Fix Central Asia and Moldova same-row close focuses.
   - Review Ukraine and Belarus focuses placed between mutual-exclusive alternatives.
   - Treat `soviet_collapse_breakaway_focus_tree` at line 2326 as an emergency fallback only. It should not be relied on as the full tree for any named Event005 country.

## Recommended implementation order

1. Run a layout-only pass on the listed close-focus and between-mutex findings. This is bounded, reviewable, and should not alter gameplay.
2. Expand `DSC`, `NRF`, and `PRA` into full concept trees because they map directly to the user's stated requirements: dead congress, naval directorate, and railway country.
3. Expand the ancient restoration trees and fix their convergence layout.
4. Reduce helper spam in the custom splinter family by creating tag-specific scripted effects for repeated helper bundles. Keep power level high.
5. Polish republic and factory successor trees by tying remaining generic political, industrial, and expansion branches to Event005 decisions, League mechanics, war goals, cores, unit templates, and release-pressure systems.

## Validation

Validation performed:

- Parsed all four Event005 focus files for focus trees, focus IDs, prerequisites, mutual exclusions, coordinates, and completion reward presence.
- Found 41 focus trees.
- Found no duplicate focus IDs.
- Found no missing `completion_reward` blocks.
- Found no nonreciprocal mutual exclusions.
- Found no missing same-tree prerequisite references.
- Found no prerequisite focus below its dependent focus.
- Found 50 layout findings:
  - 21 same-row close-focus pairs.
  - 28 focuses placed between mutually exclusive alternatives.
  - 1 vertical pathline crossing.

Validation not performed:

- No live in-game validation was performed by this subagent. The task requested a current-state code audit and handoff. Live session verification remains with the parent/user.

No fallback or simplification was used in this audit. No broad tree redesign was bulk-generated. No gameplay patches were made because the remaining high-impact work is broad and should be implemented deliberately by the parent with route-specific mechanics.

## Explicit asset and flag statement

No flags were touched. This subagent did not edit `gfx/flags`, flag sprites, flag files, or any Event006 files. This subagent only added the handoff document listed above.

## Skills used, created, or updated

- Used: `hoi4-focus-trees`
- Used for decision-link audit context: `hoi4-decisions-missions`
- Created: none
- Updated: none
