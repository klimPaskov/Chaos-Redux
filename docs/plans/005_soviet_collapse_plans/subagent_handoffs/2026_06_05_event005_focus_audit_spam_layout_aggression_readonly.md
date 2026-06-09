# Event005 Soviet Collapse Focus Audit Handoff

Date: 2026-06-05

Mode: read-only audit, except for this handoff file. No gameplay, localisation, gfx, flags, or image/asset files were changed.

Scope inspected:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Related helpers and localisation were read for reward/idea context.

Required references consulted:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- Offline wiki snapshot: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: effects, triggers, modifiers, script concepts.
- Vanilla precedent: `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt`.

## 1. Add-Idea Spam Or Repeated Same-Idea Touchpoints

No direct `add_ideas`, `add_timed_idea`, `swap_ideas`, or `remove_ideas` calls were found inside the four scoped focus files.

Indirect repeated same-idea focus touchpoints were found through guarded helper effects in `common/scripted_effects/005_soviet_collapse_effects.txt`. These do not stack because the helper checks `NOT = { has_idea = ... }`, but the same idea appears as the main hidden reward surface across several focuses.

Exact focus ids that indirectly ensure `cfr_construction_mandates`:

- `CFR_count_the_cranes`
- `CFR_emergency_cement_accounts`
- `CFR_the_first_new_district`
- `CFR_the_plan_is_the_law`
- `CFR_pour_the_final_foundation`

Helper chain:

- `soviet_collapse_ensure_cfr_construction_mandates_idea`
- `soviet_collapse_apply_cfr_focus_opening_crane_census`
- `soviet_collapse_apply_cfr_focus_contracting_office`
- `soviet_collapse_apply_cfr_focus_plan_is_law`
- `soviet_collapse_apply_cfr_raise_factory_city_belt`

Setup-only idea helpers observed, with no scoped focus id directly calling them:

- `soviet_collapse_ensure_mfr_arsenal_quotas_idea`
- `soviet_collapse_ensure_mfr_factory_guard_state_idea`
- `soviet_collapse_setup_mfr_successor`
- `soviet_collapse_setup_cfr_successor`

Recommendation: keep the guarded lifecycle if the ideas are intended as persistent route spirits, but stop using repeated "ensure the same idea exists" as the visible reward shape. Convert later CFR focuses to variable upgrades, timed construction bursts, state-targeted building choices, decisions, or idea modifier swaps so each focus has route meaning.

## 2. Shallow Or Repeated Reward Surfaces

The biggest issue is not direct idea stacking; it is reward repetition. Many focuses only set a flag, add small stability or political power, or call a generic hidden helper with nearly identical tooltip structure. This makes routes feel broad but shallow.

### UKR

Flag-only reward signature:

- `ukr_soviet_collapse_guard_the_telegraph_house`
- `ukr_soviet_collapse_question_of_statehood`
- `ukr_soviet_collapse_war_without_a_declaration`
- `ukr_soviet_collapse_socialist_republic_without_moscow`
- `ukr_soviet_collapse_black_banner_compact`
- `ukr_soviet_collapse_foreign_courts_notice_kyiv`
- `ukr_soviet_collapse_arms_before_exports`
- `ukr_soviet_collapse_british_caution`
- `ukr_soviet_collapse_black_soil_oath`
- `ukr_soviet_collapse_grain_census_of_everyone`
- `ukr_soviet_collapse_no_one_leaves_the_bread_line`
- `ukr_soviet_collapse_last_harvest_plan`

Repeated `add_stability` plus flag reward signature:

- `ukr_soviet_collapse_village_soviets_without_requisition`
- `ukr_soviet_collapse_re_register_the_party`
- `ukr_soviet_collapse_the_bread_line_becomes_a_border`
- `ukr_soviet_collapse_bread_state_whispers`
- `ukr_soviet_collapse_dead_fields_living_columns`
- `ukr_soviet_collapse_black_banner_takes_the_villages`

Repeated `add_political_power` plus flag reward signature:

- `ukr_soviet_collapse_workers_congress_in_kharkiv`
- `ukr_soviet_collapse_the_commander_or_the_cabinet`
- `ukr_soviet_collapse_coalition_of_three_ministries`
- `ukr_soviet_collapse_appointed_governors`
- `ukr_soviet_collapse_when_the_fields_refuse_the_state`

Repeated hidden-helper tooltip surface:

- `ukr_soviet_collapse_officer_patronage_lists`
- `ukr_soviet_collapse_general_staff_war_college`
- `ukr_soviet_collapse_rural_deputy_bloc`
- `ukr_soviet_collapse_minority_autonomy_statutes`
- `ukr_soviet_collapse_provincial_governors_or_elected_radas`

### KAZ

Flag-only reward signature:

- `kaz_soviet_collapse_the_southern_wires_are_cut`
- `kaz_soviet_collapse_steppe_district_inventories`
- `kaz_soviet_collapse_the_south_asks_for_guarantees`
- `kaz_soviet_collapse_a_state_across_distances`
- `kaz_soviet_collapse_alash_memory_restored`
- `kaz_soviet_collapse_socialist_steppe_republic`
- `kaz_soviet_collapse_resource_concessions_debate`
- `kaz_soviet_collapse_the_border_is_a_road`
- `kaz_soviet_collapse_no_concession_without_a_republic`
- `kaz_soviet_collapse_the_steppe_remembers_old_states`
- `kaz_soviet_collapse_tajik_mountain_guarantees`
- `kaz_soviet_collapse_the_steppe_arbitration_court`
- `kaz_soviet_collapse_basmachi_autonomy_offer`
- `kaz_soviet_collapse_restore_alash_names`
- `kaz_soviet_collapse_local_notable_compacts`
- `kaz_soviet_collapse_uzbek_supply_delegates`
- `kaz_soviet_collapse_kyrgyz_mountain_liaisons`
- `kaz_soviet_collapse_common_steppe_passports`
- `kaz_soviet_collapse_turkish_language_channels`

Repeated `add_stability` plus flag reward signature:

- `kaz_soviet_collapse_league_resource_pool`
- `kaz_soviet_collapse_lone_steppe_state`
- `kaz_soviet_collapse_the_southern_shield`
- `kaz_soviet_collapse_crush_the_road_militias`
- `kaz_soviet_collapse_a_state_under_open_sky`
- `kaz_soviet_collapse_teachers_of_the_new_steppe`
- `kaz_soviet_collapse_no_steppe_without_the_south`
- `kaz_soviet_collapse_the_steppe_cannot_be_encircled`
- `kaz_soviet_collapse_a_thousand_kilometers_of_defense`
- `kaz_soviet_collapse_the_steppe_keeps_many_memories`
- `kaz_soviet_collapse_the_southern_republics_write_together`
- `kaz_soviet_collapse_semey_legal_circle`
- `kaz_soviet_collapse_steppe_land_statutes`
- `kaz_soviet_collapse_soviets_of_the_steppe`
- `kaz_soviet_collapse_sovereign_steppe_socialism`
- `kaz_soviet_collapse_tajik_pass_agreements`

Repeated variable bump plus flag reward signature:

- `kaz_soviet_collapse_resource_defense_directorate`
- `kaz_soviet_collapse_karaganda_emergency_board`
- `kaz_soviet_collapse_domestic_resource_state`
- `kaz_soviet_collapse_basmachi_roads_reopen`
- `kaz_soviet_collapse_resource_sovereignty`
- `kaz_soviet_collapse_call_the_steppe_congress`
- `kaz_soviet_collapse_open_eastern_liaison_yurts`
- `kaz_soviet_collapse_japanese_far_east_approaches`
- `kaz_soviet_collapse_multi_vector_recognition`

Repeated `add_political_power` plus flag reward signature:

- `kaz_soviet_collapse_steppe_federation_charter`
- `kaz_soviet_collapse_the_last_caravan_tax`
- `kaz_soviet_collapse_the_written_alash_program`
- `kaz_soviet_collapse_southern_deputies_demand_seats`
- `kaz_soviet_collapse_constitutional_kurultai`

### BLR

Repeated `add_stability` plus flag reward signature:

- `blr_soviet_collapse_minsk_emergency_office`
- `blr_soviet_collapse_evacuation_choice`
- `blr_soviet_collapse_liaison_hotels`
- `blr_soviet_collapse_belarusian_question_answered`
- `blr_soviet_collapse_village_warning_bells`
- `blr_soviet_collapse_minsk_does_not_own_every_tree`
- `blr_soviet_collapse_a_forest_that_can_govern`
- `blr_soviet_collapse_the_corridor_everyone_wants`
- `blr_soviet_collapse_brest_is_not_a_gift`

Other shallow BLR focus ids needing reward review:

- `blr_soviet_collapse_western_corridor_switchmen`
- `blr_soviet_collapse_depot_cars_without_labels`
- `blr_soviet_collapse_timetable_state`
- `blr_soviet_collapse_league_supply_timetables`
- `blr_soviet_collapse_railway_neutrality`
- `blr_soviet_collapse_last_train_east`
- `blr_soviet_collapse_the_green_border`
- `blr_soviet_collapse_the_forest_state_rumor`
- `blr_soviet_collapse_minsk_central_dispatch`

### CFR

Flag-only reward signature:

- `CFR_elect_the_site_committees`
- `CFR_publish_the_planners_charter`
- `CFR_the_concrete_committee`
- `CFR_contracts_before_ideology`
- `CFR_housing_as_discipline`
- `CFR_the_board_becomes_the_cabinet`
- `CFR_machine_tools_from_empty_ministries`
- `CFR_client_city_charters`
- `CFR_a_civilian_factory_in_every_capital`
- `CFR_the_debt_map`
- `CFR_fortify_the_worksite_gates`
- `CFR_sappers_of_the_builder_state`
- `CFR_german_concrete_offers`
- `CFR_british_reconstruction_credit`
- `CFR_contracts_with_the_league`
- `CFR_the_city_without_citizens`
- `CFR_seal_the_dormitories`
- `CFR_no_empty_lots_no_empty_lives`
- `CFR_the_concrete_republic`
- `CFR_buy_peace_with_concrete`
- `CFR_build_the_border_bend_the_border`
- `CFR_the_workers_keep_the_keys`
- `CFR_the_plan_is_the_law`
- `CFR_pour_the_final_foundation`
- `CFR_nothing_but_foundations`
- `CFR_rebuild_russia_without_moscow`

Repeated `add_stability` plus flag reward signature:

- `CFR_minutes_from_every_workshop`
- `CFR_cities_first`
- `CFR_no_ruins_without_receipts`
- `CFR_the_crane_as_watchtower`
- `CFR_the_state_that_builds`

Repeated hidden-helper tooltip surface:

- `CFR_the_trust_office_takes_the_seal`
- `CFR_emergency_cement_accounts`
- `CFR_contracts_first`
- `CFR_apartment_blocks_for_loyalty`
- `CFR_reconstruction_protectorates`

### Custom Splinters

The shared custom splinter trees repeat the same helper/tooltip reward skeleton heavily. Representative exact ids with identical hidden-helper tooltip surface:

`ALA`:

- `ALA_stores`
- `ALA_legitimacy`
- `ALA_rival`
- `ALA_doctrine`
- `ALA_economy`
- `ALA_league`
- `ALA_foreign`
- `ALA_diplomatic_plan`
- `ALA_inner_faction`
- `ALA_special_arm`
- `ALA_supply`
- `ALA_enemy_front`
- `ALA_war_plan`
- `ALA_civil_rule`
- `ALA_propaganda`
- `ALA_settlement`
- `ALA_industry_plan`
- `ALA_hidden_doctrine`
- `ALA_extreme_gate`

`ARD`:

- `ARD_first_guard`
- `ARD_stores`
- `ARD_legitimacy`
- `ARD_rival`
- `ARD_doctrine`
- `ARD_economy`
- `ARD_league`
- `ARD_foreign`
- `ARD_inner_faction`
- `ARD_special_arm`
- `ARD_supply`
- `ARD_enemy_front`
- `ARD_civil_rule`
- `ARD_propaganda`
- `ARD_settlement`
- `ARD_industry_plan`
- `ARD_hidden_doctrine`
- `ARD_extreme_gate`

`BAC`:

- `BAC_first_guard`
- `BAC_stores`
- `BAC_legitimacy`
- `BAC_rival`
- `BAC_doctrine`
- `BAC_economy`
- `BAC_league`
- `BAC_foreign`
- `BAC_inner_faction`
- `BAC_special_arm`
- `BAC_supply`
- `BAC_enemy_front`
- `BAC_civil_rule`
- `BAC_propaganda`
- `BAC_settlement`
- `BAC_diplomatic_plan`
- `BAC_industry_plan`
- `BAC_hidden_doctrine`
- `BAC_extreme_gate`

The same pattern appears across the broader custom successor family, including `BBH`, `BSC`, `DHC`, `FEV`, `FTH`, `GAC`, `IUL`, `KHC`, `KRS`, `MRC`, `NLC`, `SDZ`, `SZA`, `TNC`, `UDC`, and `UWD`. Patch these by helper family and route role rather than by isolated focus ids.

## 3. Worst Layout And Pathline Problems

All scoped focus trees use absolute `x`/`y` positions only. No `relative_position_id` was found in any of the 1,698 parsed focuses. No duplicate coordinates were found by the audit parser, but the lack of relative positioning makes tree maintenance fragile and several hidden `available = { has_completed_focus = ... }` gates make the visible pathlines lie about route requirements.

### UKR

Worst issue: the main political route fork uses chain-style mutual exclusions instead of clear route exclusivity.

- `ukr_soviet_collapse_elections_under_shellfire`
- `ukr_soviet_collapse_socialist_republic_without_moscow`
- `ukr_soviet_collapse_black_banner_compact`
- `ukr_soviet_collapse_officers_above_parties`

The chain means lore routes are not cleanly pairwise-exclusive. Elections and officers can coexist unless another gate blocks them later, while socialist/black-banner/officer exclusions are partial. This is exactly the kind of mutually exclusive structure that should be lore-important and visually obvious.

Worst cross-route or hidden-gate focus ids:

- `ukr_soviet_collapse_free_soil_compromise`
- `ukr_soviet_collapse_the_ukrainian_commune_debate`
- `ukr_soviet_collapse_appointed_governors`
- `ukr_soviet_collapse_league_security_zone_mandates`
- `ukr_soviet_collapse_last_harvest_plan`

These connect or gate across separated political, commune, League, army, and bread-state lanes. Some may be intended endgame convergence, but the current layout makes branch identity weak and risks lines crossing through route choices.

### KAZ

Worst issue: Kazakhstan has no mutually exclusive focuses despite major lore choices that read like incompatible state identities.

Likely lore-important choices that should be explicit mutexes or intentionally convergent with visible bridge focuses:

- `kaz_soviet_collapse_alash_memory_restored`
- `kaz_soviet_collapse_socialist_steppe_republic`
- `kaz_soviet_collapse_resource_defense_directorate`
- `kaz_soviet_collapse_lone_steppe_state`
- `kaz_soviet_collapse_the_steppe_remembers_old_states`

Worst hidden-gate or misleading-pathline focus ids:

- `kaz_soviet_collapse_the_congress_chooses_a_past`
- `kaz_soviet_collapse_rail_guard_brigades`
- `kaz_soviet_collapse_the_steppe_arsenal`
- `kaz_soviet_collapse_industrial_settlement_compacts`
- `kaz_soviet_collapse_resource_sovereignty`
- `kaz_soviet_collapse_army_of_the_open_horizon`
- `kaz_soviet_collapse_the_steppe_outlives_the_union`

Specific semantic problem: `kaz_soviet_collapse_rail_guard_brigades` visibly has an OR-style prerequisite path, while its `available` gate requires both upstream focuses. `kaz_soviet_collapse_the_steppe_arsenal` and `kaz_soviet_collapse_army_of_the_open_horizon` also hide major cross-lane requirements in `available`, so the tree does not show the real completion route.

### BLR

Worst issue: Belarus has no mutually exclusive focuses despite a visible ideological/state fork.

Likely lore-important choices that should be explicit mutexes or intentionally connected by a clear compromise branch:

- `blr_soviet_collapse_national_council_of_minsk`
- `blr_soviet_collapse_socialist_autonomy_without_moscow`
- `blr_soviet_collapse_military_transit_directorate`
- `blr_soviet_collapse_foreign_corridor_administration`

Worst hidden-gate or cross-route focus ids:

- `blr_soviet_collapse_timetable_state`
- `blr_soviet_collapse_brest_is_not_a_gift`
- `blr_soviet_collapse_partisans_or_army`
- `blr_soviet_collapse_a_forest_that_can_govern`
- `blr_soviet_collapse_prepare_league_freight_tables`
- `blr_soviet_collapse_minsk_supplies_the_front`
- `blr_soviet_collapse_armored_train_workshops`

The recurring pattern is visible prerequisite lines from one lane plus hidden `available` requirements from another lane. That hides real dependencies and creates route crossings when the parent tries to fix the layout later.

## 4. Chaos Successor Trees Still Underpowered

Direct hard-war or strong aggression surfaces in the scoped focus files were found mainly in these focus ids:

- `PRA_rails_over_capitals`
- `TSC_starfall_mandate`
- `RMC_resurrection_without_state`
- `DSC_dead_regiment_columns`
- `DSC_maps_of_lost_armies`
- `DSC_congress_of_the_dead_army`
- `DSC_memorial_frontier_state`
- `NRF_revenant_admiralty`
- `NRF_maps_of_sunken_routes`
- `NRF_northern_revenant_fleet`
- `ICD_commissariat_without_end`
- `OGB_the_old_name_survives_modern_war`
- `MFR_the_arsenal_state`
- `MFR_no_peace_without_orders`
- `MFR_every_order_a_rifle`
- `MFR_eternal_arsenal_marches`
- `KZR_expansionist_steppe_levy`
- `KZR_returned_names_endgame`
- `KZR_road_beyond_the_caspian`
- `SOG_expansionist_merchant_claims`
- `SOG_returned_names_endgame`
- `SOG_cities_beyond_the_desert`
- `KHW_expansionist_water_claims`
- `KHW_returned_names_endgame`
- `KHW_delta_without_a_center`
- `ALN_expansionist_mountain_claims`
- `ALN_returned_names_endgame`
- `ALN_every_pass_a_border`

Trees that still read underpowered or under-explicit because their focus files rely on generic helper shells and lack direct, visible overpowered aggression:

- `FTH`
- `BSC`
- `TNC`
- `ALA`
- `BBH`
- `KRS`
- `UDC`
- `SDZ`
- `GAC`
- `DHC`
- `KHC`
- `FEV`
- `SZA`
- `UWD`
- `MRC`
- `IUL`
- `BAC`
- `ARD`
- `NLC`

This does not prove the helpers do nothing; it means the focus layer does not make the chaos successor fantasy legible or forceful. Parent should give each chaos country an obvious aggression spine with claims, timed attack advantages, AI strategies, assault columns, forced escalation, unique state transfers, or route-specific country spirits.

The ancient restoration trees (`KZR`, `SOG`, `KHW`, `ALN`) do have expansionist hooks, but they are only 16-focus mirrored mini trees. Their raw aggression is present; their political, industrial, and expansion depth is still shallow.

## 5. Prioritized Patch Order For Parent

1. Fix UKR/KAZ/BLR pathline semantics first. Convert hidden `available = { has_completed_focus = ... }` requirements into visible prerequisites where they are true structural requirements, move focuses to avoid crossings, and add `relative_position_id` in touched sections. KAZ's OR-visible/AND-hidden cases should be fixed before reward work.
2. Make lore-important mutual exclusions explicit. Start with KAZ and BLR because they currently have no mutexes for major incompatible identity choices. Then clean up UKR's chain mutex into intentional pairwise route logic or a documented compromise structure.
3. Replace the largest shallow reward groups in UKR/KAZ/BLR with route-defining mechanics. Prioritize focuses listed above that only set a flag, only add stability, only add political power, or only call a generic hidden helper.
4. Rework CFR's repeated construction-mandate reward surface. Keep one clear spirit lifecycle, then make later construction focuses upgrade variables, open decisions, target states, alter laws, or create industrial pressure instead of repeatedly ensuring the same idea.
5. Patch custom successor reward templates by helper family. The repeated `stores`, `legitimacy`, `rival`, `doctrine`, `economy`, `foreign`, `supply`, `enemy_front`, `settlement`, `industry_plan`, and `extreme_gate` skeleton should become bespoke per-country route payoffs.
6. Make chaos successor aggression visible and overpowered. Start with the custom successor trees that have no direct hard-war focus ids in the focus files, then tune AI strategies and claims/wargoals so they actively seek wars.
7. Decide whether ancient restorations are intended mini trees. If not, expand them beyond mirrored 16-focus structures with real political/industrial/expansion branches. If yes, document them as mini trees and still strengthen distinct rewards.
8. After parent patches, rerun a focus parser for duplicate coordinates, hidden `available has_completed_focus` gates, focus ids without localisation, unsupported operators, and repeated reward signatures.

## Validation Notes

Read-only audit commands used:

- Parsed 1,698 focuses across the four scoped focus files.
- Checked direct `add_ideas`, `add_timed_idea`, `swap_ideas`, and `remove_ideas` in scoped focus files.
- Mapped guarded idea helper calls from focus ids through scripted effects.
- Counted focus trees, missing `relative_position_id` usage, duplicate coordinates, mutex presence, and repeated reward signatures.
- Scanned direct hard-war/aggression reward surfaces: `create_wargoal`, `declare_war_on`, `add_ai_strategy`, and assault-column helper calls.

No parser duplicate coordinates were found. No direct focus-file `add_ideas` calls were found.

## Changed Files

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_event005_focus_audit_spam_layout_aggression_readonly.md`

No gameplay files were patched.

## Simplifications, Omissions, And Blockers

- This is a read-only audit handoff, not a broad focus-tree rewrite.
- I did not touch localisation, gfx, flags, or image/asset files.
- I did not run in-game validation.
- I did not fully inspect every helper's internal reward semantics for every custom successor; the handoff focuses on exact focus-layer repetition and the highest-risk helper-linked idea surfaces.
- No fallbacks were used.
