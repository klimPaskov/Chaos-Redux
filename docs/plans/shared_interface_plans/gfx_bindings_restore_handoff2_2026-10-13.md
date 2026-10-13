# GFX binding restoration handoff 2 — 13 October 2026

Historical bindings and original art are restored for the assigned GFX rows, and the current Famine/Migration aliases continue to serve their existing consumers. The parent-authorized Independence Wave pass restored 77 category icon fields to their exact per-category a4-parent sprite IDs while preserving every non-icon field.

No new art was generated, no portrait sprite registration was edited, no GUI was rendered, and Hearts of Iron IV was not launched. The exact historical texture bytes were restored or verified from Git/LFS without substitutes.

## Files and exact choices

| Surface | Action and source |
| --- | --- |
| `interface/028_asteroid_incoming.gfx` | Restored four existing bindings from parent `b0dcc9f5b9a09679879927eb60f9f3eb22be4fc6`: preparedness, fragment-center recovery, rival disruption, and rival offensive. Both rival actions again share the exact reconnaissance DDS as before. |
| `interface/025_alien_technology_in_antarctica.gfx` | Left unchanged. The existing idea DDS files already match all ten pre-redraw LFS hashes from `5b6ed2ce585b^`; the discovery news image and evolution category picture remain exact assets added at `5b6ed2ce585b` and have live consumers. |
| `interface/031_random_terror.gfx` | Restored the three existing category aliases to their exact parent `2782e3b12fd5160e90bd72e73e8a909ba1dbb339` texture paths. |
| `interface/chaosx_decision_icon_fits.gfx` | Left unchanged as an add-only fitted decision-icon registry. |
| `interface/chaosx_texticons.gfx` | Kept the current `GFX_famine_deaths` and `GFX_migration_deaths_forced_displacement` IDs, rebound them to the exact former `fm_deaths` textures, and restored the two removed `GFX_fm_deaths_*` aliases alongside them. |
| `interface/countrystateview.gfx` | No edit was needed; `GFX_terrain_water_shallow_sea_day` was already present with the exact historical vanilla texture path. |
| `interface/famine_and_migration_system.gfx` and `interface/famine_and_migration_system_event_pictures.gfx` | Restored both deleted GFX registries byte-for-byte from parent `baabf661afddcc459648b0715f1d4a3a92183d14`, including 45 combined-system sprites and 7 report pictures. |
| `interface/famine_system.gfx`, `interface/migration_system.gfx`, `interface/famine_report_pictures.gfx`, and `interface/migration_report_pictures.gfx` | Kept the current split-system sprite names and rewired each existing shared Famine/Migration visual to the matching exact pre-split texture. New Famine-only category/picture and evacuation art remain on their current names and textures. |
| `interface/visual_consistency_repair.gfx` | Kept all current sprite IDs. Repointed 32 unambiguous prior mod-art bindings to their exact parent textures and restored seven existing zombie-category pictures to the original portrait texture paths without editing portrait definitions. The shared Independence Wave categories are restored at their individual category fields below. |
| `common/decisions/categories/006_independence_wave_categories.txt` | Restored 77 `icon` tokens to the exact per-category sprite IDs from the a4 parent. The saved before/after comparison proves every other byte in the source files is unchanged relative to the pre-edit snapshots. |

The restored famine/migration sprite table maps each historical ID to the current consumer ID and exact texture path. The current aliases stay registered for all C11 consumers.

### Event 028 and Event 031

| Current GFX file | Restored sprite ID | Historical parent texturefile |
| --- | --- | --- |
| `interface/028_asteroid_incoming.gfx` | `GFX_decision_028_rival_disruption` | `gfx/interface/decisions/028_asteroid_incoming/reconnoiter_crater_site.dds` |
| `interface/028_asteroid_incoming.gfx` | `GFX_decision_028_rival_offensive` | `gfx/interface/decisions/028_asteroid_incoming/reconnoiter_crater_site.dds` |
| `interface/028_asteroid_incoming.gfx` | `GFX_idea_asteroid_incoming_fragment_center_recovery` | `gfx/interface/state_modifiers/028_asteroid_incoming/fragment_crater.dds` |
| `interface/028_asteroid_incoming.gfx` | `GFX_idea_asteroid_incoming_preparedness` | `gfx/interface/ideas/028_asteroid_incoming/asteroid_dust_protection.dds` |
| `interface/031_random_terror.gfx` | `GFX_decision_category_031_random_terror_actor_command` | `gfx/interface/decisions/031_random_terror/random_terror_actor_command_category.dds` |
| `interface/031_random_terror.gfx` | `GFX_decision_category_031_random_terror_false_revelation` | `gfx/interface/decisions/031_random_terror/random_terror_false_revelation_category.dds` |
| `interface/031_random_terror.gfx` | `GFX_decision_category_031_random_terror_government_response` | `gfx/interface/decisions/031_random_terror/random_terror_government_response_category.dds` |

### Famine and Migration crosswalk

| Current GFX file | Current consumer ID | Historical sprite ID | Exact restored texturefile |
| --- | --- | --- | --- |
| `interface/chaosx_texticons.gfx` | `GFX_famine_deaths` | `GFX_fm_deaths_famine` | `gfx/texticons/fm_deaths_famine.dds` |
| `interface/chaosx_texticons.gfx` | `GFX_migration_deaths_forced_displacement` | `GFX_fm_deaths_displacement` | `gfx/texticons/fm_deaths_displacement.dds` |
| `interface/famine_report_pictures.gfx` | `GFX_report_event_famine_generic` | `GFX_report_event_famine_migration_generic_famine` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_generic_famine.dds` |
| `interface/famine_report_pictures.gfx` | `GFX_report_event_famine_island_blockade` | `GFX_report_event_famine_migration_island_blockade` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_island_blockade.dds` |
| `interface/famine_report_pictures.gfx` | `GFX_report_event_famine_relief_arrival` | `GFX_report_event_famine_migration_relief_arrival` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_relief_arrival.dds` |
| `interface/famine_system.gfx` | `GFX_achievement_famine_bread_across_the_front` | `GFX_achievement_famine_migration_bread_across_the_front` | `gfx/achievements/famine_migration_bread_across_the_front.dds` |
| `interface/famine_system.gfx` | `GFX_achievement_famine_bread_across_the_front_grey` | `GFX_achievement_famine_migration_bread_across_the_front_grey` | `gfx/achievements/famine_migration_bread_across_the_front_grey.dds` |
| `interface/famine_system.gfx` | `GFX_achievement_famine_bread_across_the_front_not_eligible` | `GFX_achievement_famine_migration_bread_across_the_front_not_eligible` | `gfx/achievements/famine_migration_bread_across_the_front_not_eligible.dds` |
| `interface/famine_system.gfx` | `GFX_achievement_famine_break_the_blockade` | `GFX_achievement_famine_migration_break_the_blockade` | `gfx/achievements/famine_migration_break_the_blockade.dds` |
| `interface/famine_system.gfx` | `GFX_achievement_famine_break_the_blockade_grey` | `GFX_achievement_famine_migration_break_the_blockade_grey` | `gfx/achievements/famine_migration_break_the_blockade_grey.dds` |
| `interface/famine_system.gfx` | `GFX_achievement_famine_break_the_blockade_not_eligible` | `GFX_achievement_famine_migration_break_the_blockade_not_eligible` | `gfx/achievements/famine_migration_break_the_blockade_not_eligible.dds` |
| `interface/famine_system.gfx` | `GFX_achievement_famine_the_grain_stayed_home` | `GFX_achievement_famine_migration_the_grain_stayed_home` | `gfx/achievements/famine_migration_the_grain_stayed_home.dds` |
| `interface/famine_system.gfx` | `GFX_achievement_famine_the_grain_stayed_home_grey` | `GFX_achievement_famine_migration_the_grain_stayed_home_grey` | `gfx/achievements/famine_migration_the_grain_stayed_home_grey.dds` |
| `interface/famine_system.gfx` | `GFX_achievement_famine_the_grain_stayed_home_not_eligible` | `GFX_achievement_famine_migration_the_grain_stayed_home_not_eligible` | `gfx/achievements/famine_migration_the_grain_stayed_home_not_eligible.dds` |
| `interface/famine_system.gfx` | `GFX_famine_decision_airlift` | `GFX_fm_dec_airlift` | `gfx/interface/decisions/famine_and_migration_system/fm_dec_airlift.dds` |
| `interface/famine_system.gfx` | `GFX_famine_decision_release_reserves` | `GFX_fm_dec_release_reserves` | `gfx/interface/decisions/famine_and_migration_system/fm_dec_release_reserves.dds` |
| `interface/famine_system.gfx` | `GFX_famine_decision_relief_convoy` | `GFX_fm_dec_relief_convoy` | `gfx/interface/decisions/famine_and_migration_system/fm_dec_relief_convoy.dds` |
| `interface/famine_system.gfx` | `GFX_famine_state_acute_shortage` | `GFX_fm_state_acute_shortage` | `gfx/interface/state_modifiers/famine_and_migration_system/fm_state_acute_shortage.dds` |
| `interface/famine_system.gfx` | `GFX_famine_state_catastrophic_famine` | `GFX_fm_state_catastrophic_famine` | `gfx/interface/state_modifiers/famine_and_migration_system/fm_state_catastrophic_famine.dds` |
| `interface/famine_system.gfx` | `GFX_famine_state_famine` | `GFX_fm_state_famine` | `gfx/interface/state_modifiers/famine_and_migration_system/fm_state_famine.dds` |
| `interface/famine_system.gfx` | `GFX_famine_state_supply_strain` | `GFX_fm_state_supply_strain` | `gfx/interface/state_modifiers/famine_and_migration_system/fm_state_supply_strain.dds` |
| `interface/migration_report_pictures.gfx` | `GFX_report_event_migration_closed_border` | `GFX_report_event_famine_migration_closed_border` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_closed_border.dds` |
| `interface/migration_report_pictures.gfx` | `GFX_report_event_migration_nuclear_evacuation` | `GFX_report_event_famine_migration_nuclear_evacuation` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_nuclear_evacuation.dds` |
| `interface/migration_report_pictures.gfx` | `GFX_report_event_migration_return` | `GFX_report_event_famine_migration_return` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_return.dds` |
| `interface/migration_report_pictures.gfx` | `GFX_report_event_migration_wartime_evacuation` | `GFX_report_event_famine_migration_wartime_evacuation` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_wartime_evacuation.dds` |
| `interface/migration_system.gfx` | `GFX_achievement_migration_a_place_at_the_table` | `GFX_achievement_famine_migration_a_place_at_the_table` | `gfx/achievements/famine_migration_a_place_at_the_table.dds` |
| `interface/migration_system.gfx` | `GFX_achievement_migration_a_place_at_the_table_grey` | `GFX_achievement_famine_migration_a_place_at_the_table_grey` | `gfx/achievements/famine_migration_a_place_at_the_table_grey.dds` |
| `interface/migration_system.gfx` | `GFX_achievement_migration_a_place_at_the_table_not_eligible` | `GFX_achievement_famine_migration_a_place_at_the_table_not_eligible` | `gfx/achievements/famine_migration_a_place_at_the_table_not_eligible.dds` |
| `interface/migration_system.gfx` | `GFX_achievement_migration_hungry_not_contagious` | `GFX_achievement_famine_migration_hungry_not_contagious` | `gfx/achievements/famine_migration_hungry_not_contagious.dds` |
| `interface/migration_system.gfx` | `GFX_achievement_migration_hungry_not_contagious_grey` | `GFX_achievement_famine_migration_hungry_not_contagious_grey` | `gfx/achievements/famine_migration_hungry_not_contagious_grey.dds` |
| `interface/migration_system.gfx` | `GFX_achievement_migration_hungry_not_contagious_not_eligible` | `GFX_achievement_famine_migration_hungry_not_contagious_not_eligible` | `gfx/achievements/famine_migration_hungry_not_contagious_not_eligible.dds` |
| `interface/migration_system.gfx` | `GFX_achievement_migration_no_one_left_at_the_gate` | `GFX_achievement_famine_migration_no_one_left_at_the_gate` | `gfx/achievements/famine_migration_no_one_left_at_the_gate.dds` |
| `interface/migration_system.gfx` | `GFX_achievement_migration_no_one_left_at_the_gate_grey` | `GFX_achievement_famine_migration_no_one_left_at_the_gate_grey` | `gfx/achievements/famine_migration_no_one_left_at_the_gate_grey.dds` |
| `interface/migration_system.gfx` | `GFX_achievement_migration_no_one_left_at_the_gate_not_eligible` | `GFX_achievement_famine_migration_no_one_left_at_the_gate_not_eligible` | `gfx/achievements/famine_migration_no_one_left_at_the_gate_not_eligible.dds` |
| `interface/migration_system.gfx` | `GFX_achievement_migration_roads_home` | `GFX_achievement_famine_migration_roads_home` | `gfx/achievements/famine_migration_roads_home.dds` |
| `interface/migration_system.gfx` | `GFX_achievement_migration_roads_home_grey` | `GFX_achievement_famine_migration_roads_home_grey` | `gfx/achievements/famine_migration_roads_home_grey.dds` |
| `interface/migration_system.gfx` | `GFX_achievement_migration_roads_home_not_eligible` | `GFX_achievement_famine_migration_roads_home_not_eligible` | `gfx/achievements/famine_migration_roads_home_not_eligible.dds` |
| `interface/migration_system.gfx` | `GFX_achievement_migration_the_country_did_not_empty` | `GFX_achievement_famine_migration_the_country_did_not_empty` | `gfx/achievements/famine_migration_the_country_did_not_empty.dds` |
| `interface/migration_system.gfx` | `GFX_achievement_migration_the_country_did_not_empty_grey` | `GFX_achievement_famine_migration_the_country_did_not_empty_grey` | `gfx/achievements/famine_migration_the_country_did_not_empty_grey.dds` |
| `interface/migration_system.gfx` | `GFX_achievement_migration_the_country_did_not_empty_not_eligible` | `GFX_achievement_famine_migration_the_country_did_not_empty_not_eligible` | `gfx/achievements/famine_migration_the_country_did_not_empty_not_eligible.dds` |
| `interface/migration_system.gfx` | `GFX_migration_category` | `GFX_fm_cat_displacement` | `gfx/interface/decisions/famine_and_migration_system/fm_cat_displacement.dds` |
| `interface/migration_system.gfx` | `GFX_migration_category_picture` | `GFX_fm_pic_displacement` | `gfx/interface/decisions/famine_and_migration_system/fm_pic_displacement.dds` |
| `interface/migration_system.gfx` | `GFX_migration_decision_close_border` | `GFX_fm_dec_close_border` | `gfx/interface/decisions/famine_and_migration_system/fm_dec_close_border.dds` |
| `interface/migration_system.gfx` | `GFX_migration_decision_distribute` | `GFX_fm_dec_distribute` | `gfx/interface/decisions/famine_and_migration_system/fm_dec_distribute.dds` |
| `interface/migration_system.gfx` | `GFX_migration_decision_evacuate` | `GFX_fm_dec_evacuate` | `gfx/interface/decisions/famine_and_migration_system/fm_dec_evacuate.dds` |
| `interface/migration_system.gfx` | `GFX_migration_decision_integrate` | `GFX_fm_dec_integrate` | `gfx/interface/decisions/famine_and_migration_system/fm_dec_integrate.dds` |
| `interface/migration_system.gfx` | `GFX_migration_decision_open_border` | `GFX_fm_dec_open_border` | `gfx/interface/decisions/famine_and_migration_system/fm_dec_open_border.dds` |
| `interface/migration_system.gfx` | `GFX_migration_decision_quarantine` | `GFX_fm_dec_quarantine` | `gfx/interface/decisions/famine_and_migration_system/fm_dec_quarantine.dds` |
| `interface/migration_system.gfx` | `GFX_migration_decision_return` | `GFX_fm_dec_return` | `gfx/interface/decisions/famine_and_migration_system/fm_dec_return.dds` |
| `interface/migration_system.gfx` | `GFX_migration_state_exodus` | `GFX_fm_state_exodus` | `gfx/interface/state_modifiers/famine_and_migration_system/fm_state_exodus.dds` |
| `interface/migration_system.gfx` | `GFX_migration_state_overcrowded` | `GFX_fm_state_overcrowded` | `gfx/interface/state_modifiers/famine_and_migration_system/fm_state_overcrowded.dds` |
| `interface/migration_system.gfx` | `GFX_migration_state_reception` | `GFX_fm_state_reception` | `gfx/interface/state_modifiers/famine_and_migration_system/fm_state_reception.dds` |
| `interface/migration_system.gfx` | `GFX_migration_state_return` | `GFX_fm_state_return` | `gfx/interface/state_modifiers/famine_and_migration_system/fm_state_return.dds` |
| `interface/migration_system.gfx` | `GFX_migration_state_trapped_border` | `GFX_fm_state_trapped_border` | `gfx/interface/state_modifiers/famine_and_migration_system/fm_state_trapped_border.dds` |

### Shared visual registry crosswalk

Each row keeps the current sprite ID and restores its earlier texture path. For the four shared Independence Wave groups, the texture is selected per category in the next table rather than choosing one representative image for every consumer.

| Current sprite ID | Earlier consumer sprite ID(s) | Exact restored texturefile |
| --- | --- | --- |
| `GFX_decision_cat_picture_independence_wave_iw043_middle_volga_congress` | `GFX_decision_category_independence_wave_iw043_middle_volga_congress` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_category_independence_wave_iw043_middle_volga_congress.dds` |
| `GFX_decision_cat_picture_independence_wave_iw058_council_of_communities` | `GFX_decision_category_independence_wave_iw058_council_of_communities` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_category_independence_wave_iw058_council_of_communities.dds` |
| `GFX_decision_cat_picture_independence_wave_iw093_asante_compact` | `GFX_decision_category_independence_wave_iw093_asante_compact_category` | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw093_asante_compact_category.dds` |
| `GFX_decision_cat_picture_independence_wave_iw098_sokoto_compact` | `GFX_decision_category_independence_wave_iw098_sokoto_compact_category` | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw098_sokoto_compact_category.dds` |
| `GFX_decision_cat_picture_weaponized_zombie_demonic` | `GFX_portrait_ZZZ_weaponized_demonic` | `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_demonic.dds` |
| `GFX_decision_cat_picture_weaponized_zombie_infected` | `GFX_portrait_ZZZ_weaponized_infected` | `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_infected.dds` |
| `GFX_decision_cat_picture_weaponized_zombie_mutant` | `GFX_portrait_ZZZ_weaponized_mutant` | `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_mutant.dds` |
| `GFX_decision_cat_picture_weaponized_zombie_necrotic` | `GFX_portrait_ZZZ_weaponized_necrotic` | `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_necrotic.dds` |
| `GFX_decision_cat_picture_weaponized_zombie_parasitic` | `GFX_portrait_ZZZ_weaponized_parasitic` | `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_parasitic.dds` |
| `GFX_decision_cat_picture_weaponized_zombie_rabid` | `GFX_portrait_ZZZ_weaponized_rabid` | `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_rabid.dds` |
| `GFX_decision_cat_picture_weaponized_zombie_undead` | `GFX_portrait_ZZZ_weaponized_undead` | `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_undead.dds` |
| `GFX_decision_category_012_africa_charter_ledger` | `GFX_decision_012_africa_charter_ledger` | `gfx/interface/decisions/012_africa/core/decision_012_africa_charter_ledger.dds` |
| `GFX_decision_category_fallout_food_security` | `GFX_idea_fallout_state_grade` | `gfx/interface/ideas/fallout_world_end/idea_fallout_state_grade.dds` |
| `GFX_decision_category_independence_wave_death_survey` | `GFX_decision_death_survey_boat` | `gfx/interface/decisions/010_death/decision_death_survey_boat.dds` |
| `GFX_decision_category_independence_wave_network` | `GFX_decision_independence_wave_network_aid` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_network_aid.dds` |
| `GFX_decision_category_repair_011_secret_alliance_coalition_crisis` | `GFX_decision_category_011_secret_alliance_coalition_crisis` | `gfx/interface/decisions/011_secret_alliance/decision_category_coalition_crisis.dds` |
| `GFX_decision_category_repair_011_secret_alliance_foreign_interference` | `GFX_decision_category_011_secret_alliance_foreign_interference` | `gfx/interface/decisions/011_secret_alliance/decision_category_foreign_interference.dds` |
| `GFX_decision_category_repair_012_africa_priority_member` | `GFX_decision_012_africa_priority_member_category` | `gfx/interface/decisions/012_africa/priority_members/decision_012_africa_priority_member_category.dds` |
| `GFX_decision_category_repair_cannibalism_achievement_tracker` | `GFX_decision_category_cannibalism_achievement_tracker` | `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_achievement_tracker.dds` |
| `GFX_decision_category_repair_cannibalism_containment` | `GFX_decision_category_cannibalism_containment` | `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_containment.dds` |
| `GFX_decision_category_repair_cannibalism_international_response` | `GFX_decision_category_cannibalism_international_response` | `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_international_response.dds` |
| `GFX_decision_category_repair_cannibalism_network_alerts` | `GFX_decision_category_cannibalism_network_alerts` | `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_network_alerts.dds` |
| `GFX_decision_category_repair_cannibalism_reconstruction` | `GFX_decision_category_cannibalism_reconstruction` | `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_reconstruction.dds` |
| `GFX_decision_category_repair_cannibalism_unified_command` | `GFX_decision_category_cannibalism_unified_command` | `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_unified_command.dds` |
| `GFX_decision_category_repair_cannibalism_unified_global_campaign` | `GFX_decision_category_cannibalism_unified_global_campaign` | `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_unified_global_campaign.dds` |
| `GFX_decision_category_repair_cannibalism_unified_larder` | `GFX_decision_category_cannibalism_unified_larder` | `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_unified_larder.dds` |
| `GFX_decision_category_repair_cannibalism_unified_war_machine` | `GFX_decision_category_cannibalism_unified_war_machine` | `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_unified_war_machine.dds` |
| `GFX_decision_category_repair_cannibalism_unified_world_end` | `GFX_decision_category_cannibalism_unified_world_end` | `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_unified_world_end.dds` |
| `GFX_decision_category_repair_cannibalism_warlord_command` | `GFX_decision_category_cannibalism_warlord_command` | `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_warlord_command.dds` |
| `GFX_decision_category_repair_cannibalism_wendigo_command` | `GFX_decision_category_cannibalism_wendigo_command` | `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_wendigo_command.dds` |
| `GFX_decision_category_repair_cannibalism_wendigo_counterwar` | `GFX_decision_category_cannibalism_wendigo_counterwar` | `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_wendigo_counterwar.dds` |
| `GFX_decision_category_repair_death_country` | `GFX_decision_category_death_country` | `gfx/interface/decisions/010_death/decision_category_death_country.dds` |
| `GFX_decision_category_repair_fallout_usa_continuity_projects` | `GFX_decision_category_fallout_usa_continuity_projects` | `gfx/interface/goals/fallout_successor_b7_usa/federal_continuity_ledger.dds` |
| `GFX_decision_category_repair_random_faction_bloc_pressure` | `GFX_decision_category_random_faction_bloc_pressure` | `gfx/interface/decisions/017_random_faction/decision_category_random_faction_bloc_pressure.dds` |
| `GFX_decision_category_repair_resources_found_anti_cave` | `GFX_decision_category_resources_found_anti_cave` | `gfx/interface/decisions/018_resources_found/decision_category_resources_found_anti_cave.dds` |
| `GFX_decision_category_repair_resources_found_cave` | `GFX_decision_category_resources_found_cave` | `gfx/interface/decisions/018_resources_found/decision_category_resources_found_cave.dds` |
| `GFX_decision_category_repair_resources_found_containment` | `GFX_decision_category_resources_found_containment` | `gfx/interface/decisions/018_resources_found/decision_category_resources_found_containment.dds` |
| `GFX_decision_category_repair_resources_found_field` | `GFX_decision_category_resources_found_field` | `gfx/interface/decisions/018_resources_found/decision_category_resources_found_field.dds` |
| `GFX_decision_category_repair_resources_found_trade` | `GFX_decision_category_resources_found_trade` | `gfx/interface/decisions/018_resources_found/decision_category_resources_found_trade.dds` |

### Independence Wave category icon fields

Each changed field returns to the sprite ID used by that category in the a4 parent. The original sprite’s historical texture path is recorded for each row.

| Category ID | Current shared sprite before restore | Restored category sprite ID | Original texturefile |
| --- | --- | --- | --- |
| `independence_wave_afx_industrial_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_agx_waterline_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_army_integration_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_army_integration_actions.dds` |
| `independence_wave_ajx_saar_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_altai_mountain_compact_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_arx_sardinia_category` | `GFX_decision_category_independence_wave_borders` | `GFX_decision_independence_wave_arx_shipping` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_arx_shipping.dds` |
| `independence_wave_asx_sicily_category` | `GFX_decision_category_independence_wave_borders` | `GFX_decision_independence_wave_asx_port` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_asx_port.dds` |
| `independence_wave_axx_banat_council_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_bashkiria_frontier_compact_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_bax_thrace_council_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_bay_state_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_bbx_epirus_council_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_borders_category` | `GFX_decision_category_independence_wave_borders` | `GFX_decision_independence_wave_border_arbitration` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_border_arbitration.dds` |
| `independence_wave_bos_drina_council_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_bri_brittany_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_buryatia_frontier_compact_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_cat_industrial_compact_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_cor_corsica_category` | `GFX_decision_category_independence_wave_borders` | `GFX_decision_independence_wave_cor_customs` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_cor_customs.dds` |
| `independence_wave_evolution_incident_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_fer_railway_compact_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_fij_founding_congress_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_form0124_membership_category` | `GFX_decision_category_independence_wave_diplomacy` | `GFX_decision_independence_wave_league_votes` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_league_votes.dds` |
| `independence_wave_form01_congress_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_formable_proclamation` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_formable_proclamation.dds` |
| `independence_wave_form03_low_countries_category` | `GFX_decision_category_independence_wave_diplomacy` | `GFX_decision_independence_wave_league_votes` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_league_votes.dds` |
| `independence_wave_form04_league_category` | `GFX_decision_category_independence_wave_borders` | `GFX_decision_independence_wave_border_arbitration` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_border_arbitration.dds` |
| `independence_wave_form05_charter_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_form05_charter` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_charter.dds` |
| `independence_wave_form08_danube_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_form09_balkan_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_form16_integration_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_form39_invitation_category` | `GFX_decision_category_independence_wave_diplomacy` | `GFX_decision_independence_wave_league_votes` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_league_votes.dds` |
| `independence_wave_form48_invitation_category` | `GFX_decision_category_independence_wave_diplomacy` | `GFX_decision_independence_wave_league_votes` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_league_votes.dds` |
| `independence_wave_formable_transaction_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_formable_proclamation` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_formable_proclamation.dds` |
| `independence_wave_formables_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_formable_proclamation` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_formable_proclamation.dds` |
| `independence_wave_founding_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_fsm_micronesia_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_glc_iberian_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_government_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_hbx_california_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_high_chaos_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_host_relations_category` | `GFX_decision_category_independence_wave_diplomacy` | `GFX_decision_independence_wave_former_host_negotiations` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_former_host_negotiations.dds` |
| `independence_wave_ice_north_atlantic_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_iw005_flanders_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_iw022_dalmatia_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_iw025_vojvodina_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_iw035_livonia_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_iw059_mesopotamia_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_iw085_cyrenaica_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_iw101_kongo_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_iw102_kuba_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_iw105_loango_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_iw156_moluccan_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_iw196_antilles_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_iw197_mapuche_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_iw204_restoration_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_karelia_crimea_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_khakassia_frontier_compact_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_komi_northern_compact_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_kub_mounted_compact_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_kurdistan_mountain_compact_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_league_category` | `GFX_decision_category_independence_wave_diplomacy` | `GFX_decision_independence_wave_league_votes` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_league_votes.dds` |
| `independence_wave_mac_vardar_council_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_mari_forest_compact_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_mnt_mountain_compact_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_nav_iberian_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_patron_category` | `GFX_decision_category_independence_wave_diplomacy` | `GFX_decision_independence_wave_patron_aid` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_patron_aid.dds` |
| `independence_wave_recognition_category` | `GFX_decision_category_independence_wave_diplomacy` | `GFX_decision_independence_wave_recognition_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_recognition_actions.dds` |
| `independence_wave_rhi_corridor_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_rival_bloc_category` | `GFX_decision_category_independence_wave_diplomacy` | `GFX_decision_independence_wave_league_votes` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_league_votes.dds` |
| `independence_wave_rut_mountain_compact_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_sakha_arctic_compact_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_scenario_ledger_category` | `GFX_decision_category_independence_wave_borders` | `GFX_decision_independence_wave_border_arbitration` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_border_arbitration.dds` |
| `independence_wave_sco_state_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_security_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_army_integration_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_army_integration_actions.dds` |
| `independence_wave_tat_river_compact_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_tra_danube_council_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_transcaucasus_reconstruction_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `independence_wave_udm_industrial_forest_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |
| `independence_wave_wls_state_category` | `GFX_decision_category_independence_wave_government` | `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |

| Shared current alias | Restored category fields | Historical sprite IDs selected per category |
| --- | ---: | --- |
| `GFX_decision_category_independence_wave_borders` | 6 | `GFX_decision_independence_wave_arx_shipping` × 1; `GFX_decision_independence_wave_asx_port` × 1; `GFX_decision_independence_wave_border_arbitration` × 3; `GFX_decision_independence_wave_cor_customs` × 1 |
| `GFX_decision_category_independence_wave_diplomacy` | 9 | `GFX_decision_independence_wave_former_host_negotiations` × 1; `GFX_decision_independence_wave_league_votes` × 6; `GFX_decision_independence_wave_patron_aid` × 1; `GFX_decision_independence_wave_recognition_actions` × 1 |
| `GFX_decision_category_independence_wave_government` | 31 | `GFX_decision_independence_wave_form05_charter` × 1; `GFX_decision_independence_wave_formable_proclamation` × 3; `GFX_decision_independence_wave_government_actions` × 27 |
| `GFX_decision_category_independence_wave_integration` | 31 | `GFX_decision_independence_wave_army_integration_actions` × 2; `GFX_decision_independence_wave_integration_missions` × 29 |

| Retained category field | a4-parent icon field | Current sprite ID | Reason |
| --- | --- | --- | --- |
| `independence_wave_atj_aceh_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_atx_venice_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_bar_kuta_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_blc_kalat_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_bli_bali_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_brd_kingdom_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_cin_chechnya_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_clx_circassia_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_cux_hejaz_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_dag_dagestan_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_don_millerovo_charter_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_dsx_oyo_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_dux_bornu_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_fdx_punjab_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_form11_host_category` | None | `GFX_decision_category_independence_wave_integration` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_fox_assam_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_fux_minangkabau_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_gcx_shan_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_gmx_turkestan_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_gzx_newfoundland_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_har_city_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_hcx_texas_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_hyd_deccan_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_iax_mon_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_ibx_kachin_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_imo_imamate_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_iw095_first_footprint_category` | `GFX_decision_category_independence_wave_integration` | `GFX_decision_category_independence_wave_integration` | Parent and current category already use the same GFX ID. |
| `independence_wave_kas_kashmir_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_kos_cantonal_compact_category` | `GFX_decision_category_independence_wave_state_foundation` | `GFX_decision_category_independence_wave_government` | Historical `state_foundation` GFX ID had no definition; kept the current registered government-category alias. |
| `independence_wave_lao_laos_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_leb_settlement_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_mad_island_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_men_mongol_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_mpu_manipur_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_mys_mysore_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_okn_ryukyu_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_pal_mandate_end_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_psh_frontier_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_que_quebec_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_ras_south_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_ready_formable_integration_category` | None | `GFX_decision_category_independence_wave_integration` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_ready_formable_routes_category` | None | `GFX_decision_category_independence_wave_integration` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_remnant_petition_category` | None | `GFX_decision_category_independence_wave_diplomacy` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_rif_republic_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_rwa_kingdom_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_sam_samoa_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_sin_sindh_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_som_sultanates_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_tig_highlands_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_uga_buganda_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |
| `independence_wave_yuc_yucatan_category` | None | `GFX_decision_category_independence_wave_government` | No category icon binding in the a4 parent; retained the current alias for the later category/mechanic. |

One historical GFX token, `GFX_decision_category_independence_wave_state_foundation`, had no definition in the a4-parent interface tree. Its category therefore remains on the current registered `GFX_decision_category_independence_wave_government` sprite, avoiding a dangling binding. The other 49 categories with no prior icon entry and the one category already using the same icon retain their current aliases.

## Asset and registry verification

| Check | Result |
| --- | --- |
| Historical DDS paths decoded with Pillow | 109 unique paths; 0 decode failures. |
| Exact content duplicate groups among those paths | 0. |
| Touched GFX sprite IDs checked | 173; 0 duplicate mod definitions, 0 missing IDs, and 0 missing texture paths. |
| Authorized Independence Wave category source changes | 77 exact icon-only edits; snapshot replay = True. |
| Event 025 protected idea DDS originals | 10 / 10 match the pre-redraw SHA-256 values. |
| Event 025 retained discovery/evolution art | Discovery `397x153` and evolution category picture `114x101` both strictly decoded; both are exact to `5b6ed2ce585b` and have current consumers. |
| Original GFX registries | `interface/famine_and_migration_system.gfx`: 45 sprites, SHA-256 `948b285d7fab0a4f96cce2d523e37196a806cfbb41506c3a25f4759e7d35c1c5` (byte-exact to parent).; `interface/famine_and_migration_system_event_pictures.gfx`: 7 sprites, SHA-256 `5873fd2dcb709385c65024d8c97eb127b2f7416b9bb2e96227d4e32fa45587df` (byte-exact to parent). |

The exact 109-path SHA-256, dimensions, source revisions, and decode results are in [`final_asset_and_wiring_checks.json`](../../../.tmp/interface_restore_handoff2/final_asset_and_wiring_checks.json) and [`final_restore_manifest.json`](../../../.tmp/interface_restore_handoff2/final_restore_manifest.json). Current GFX aliases and their parent texture paths are in [`consumer_repoint_manifest.json`](../../../.tmp/interface_restore_handoff2/consumer_repoint_manifest.json).

Pre-edit GFX bytes are preserved under `.tmp/interface_restore_handoff2/gfx/`. The Independence Wave category snapshots and pre-edit Git diffs are in `.tmp/interface_restore_handoff2/gfx/source_snapshots/` and `.tmp/interface_restore_handoff2/gfx/preedit_diffs/`.

No portrait binding was changed. The seven existing zombie-category-picture aliases now point at the same exact DDS paths as their pre-a4 `GFX_portrait_ZZZ_weaponized_*` pictures; `interface/chaosx_characters.gfx` remains untouched. The existing header comment in `visual_consistency_repair.gfx` still describes the newer dedicated category and picture scales; the historical texture sizes vary by their original source, including `156x210` portraits for the seven zombie category pictures scaled by the existing consumer. The comment was left unchanged because the assigned scope was historical bindings.

## Consumer and mechanic decisions

Event 025’s `chaosx_nr25_evolution_category` remains backed by the new evolution picture because the category is live for the five Evolution V outcomes, and `GFX_news_event_025_discovery` remains backed by the new discovery news image because it is used by both `events/025_alien_technology_in_antarctica.txt` and `events/_chaosx_news.txt`.

The split Famine and Migration sprite aliases and their C11 categories remain in place. Only same-role visuals that existed in the combined system returned to the original art; Famine-only category art and the distinct Famine evacuation action keep their current assets. This follows the C11 history report, which identifies Hunger Lines, the independent famine-country registry, and the separate Famine crisis modifier as added systems while preserving the earlier cohort, corridor, reception, donor, and return owners.

`GFX_decision_category_repair_utopia_*` and `GFX_decision_category_repair_repression_ledger` remain registered as add-only entries with no current category caller. The 49 Independence Wave categories without a parent icon entry also keep their current registered aliases. Existing `GFX_decision_category_independence_wave_*` aliases remain available to those later callers.

No art, sprite IDs, or GFX files were deleted. No gameplay, costs, effects, availability, cooldowns, localisation, GUI, or event code were edited. No simplification or substitute art was introduced.

## Reference evidence and limits

`hoi4.reference_context` and `hoi4.reference_read` returned the installed `common/decisions/_documentation.md`, lines 1–46, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`; the offline Decision modding page, icon lines 111–127 and picture lines 182–185, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`; and the offline Graphical asset modding page, `spriteType` lines 30–100, revision `f8e3d4ad382f4e5f8e170492a484d090bad62e3711cabfb5d3bf84e58ab32dd9`.

The installed vanilla precedent `interface/decisions.gfx`, lines 6–9, defines `GFX_decision_category_generic` against `gfx/interface/decisions/decision_category_generic.dds`. `hoi4.source_lookup` indexed it at revision `d3e4afc2aeb4fe944812c1529fce9553574e2760f46889d18164c0aa1ed49713`. The same index returned the restored Event 031 sprite in `interface/031_random_terror.gfx`, lines 785–788, and the historical Independence Wave decision icon at `interface/006_independence_wave.gfx`, line 79, revision `a6c5f7c48b4238a0188c162808b0d039a87edb48bae371eb39c443560b32a737`.

The owner restoration plan’s A5 and A7 decisions are in `docs/plans/chaos_redux_restore_plan_2026-10-12.md`, lines 28 and 30; the exact-asset evidence is in `docs/plans/chaos_redux_restore_assets_audio_2026-10-12.md`, A5 lines 41–50 and A7 lines 205–211. The C11 history evidence in `docs/plans/migration_famine_history_2026-10-13.md`, lines 21–31, confirms which deeper Famine/Migration owners and newer October systems remain active.

`GFX_terrain_water_shallow_sea_day` is present once in the mod at `interface/countrystateview.gfx`, lines 454–457, and uses the exact vanilla texture. The installed file contains two same-name entries at lines 454–457 and 459–462 with that same path; the mod source index reports the mod definition active and the vanilla definitions shadowed. The restored famine death texticon alias is present once in `interface/chaosx_texticons.gfx`, lines 381–385.

One initial `hoi4.source_lookup` call was rejected because it requested `maxDefinitions = 5` above the tool limit of 3; the corrected call at 3 succeeded and returned the exact indexed definitions. No further retry was needed.

No GUI renderer or live-game check was run, per the parent’s instruction. Source history, current consumers, source index ownership, exact DDS hashes, path existence, sprite-name uniqueness, and strict DDS decoding are the limits of this handoff.

Skills used: `chaos-redux-event-assets`, `chaos-redux-subagents`, and `chaos-redux-decisions-missions`. No skill was created or updated. No commit or push was made.
