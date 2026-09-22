# Chaos Redux visual consistency contract

This document records the runtime visual-family rules and the repairs applied across the mod's event and decision surfaces.

## Runtime contracts

`country_event` blocks use report-family artwork, normally a 210x176 event card such as `GFX_report_event_*`.

`news_event` blocks use news-family artwork, normally a 397x153 news strip such as `GFX_news_event_*`.

The report family also contains a small set of legacy names such as `GFX_fallout_seed_vault_report`; those are report-card assets by their registered dimensions and consumer use even though the name does not begin with `GFX_report_event_`.

Decision-category `icon` fields use category-scale artwork rather than a normal decision icon.

Decision-category `picture` fields use category-panel artwork rather than a portrait or an event card.

Normal decision `icon` fields remain decision-scale artwork and are not replaced by category icons.

National focus `icon` fields use focus-scale artwork at a native 94x86 canvas with native transparency, which is the dominant size in `gfx/interface/goals/` and the size the Chaos Redux focus trees are authored against.

A focus icon is registered twice: the base sprite and a `_shine` sprite that reuses the icon's own DDS as the animation mask and `gfx/interface/goals/shine_overlay.dds` as the scrolling overlay, following the vanilla `interface/goals_shine.gfx` pattern.

Dynamic picture selectors used by country events must resolve to report-family artwork unless the selector is explicitly used for a country-leader portrait.

## Event repairs

The event-family pass updated the affected country events in `events/005_soviet_collapse.txt`, `events/011_secret_alliance.txt`, `events/012_africa_world_order.txt`, `events/012_africa_world_package_asia_north_america.txt`, `events/012_africa_world_package_crossroads_europe.txt`, `events/018_random_resource.txt`, `events/020_black_death.txt`, `events/079_the_master.txt`, `events/chaosx_triggerable_scenarios.txt`, `events/biowarfare_events.txt`, `events/germany_mengele.txt`, and the related event files.

Country events that had news-family pictures now use existing or registered report-family art.

News events that had report-family pictures now use existing or registered news-family art.

The Soviet splinter reports now use the registered `GFX_report_breakaway_mobilization` sprite.

The Master reports now use the existing `GFX_report_event_generic_handshake` sprite.

The Africa world-order country reports use the dedicated Africa report sprites where available and `GFX_report_event_generic_conference` for conference variants without a more specific package image.

The resources-found chain now uses the registered `GFX_report_event_018_*` family according to discovery, breach, hunt, evacuation, sealing, and cleanup context.

The Event 19 first-family selector in `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt` resolves to the registered `GFX_report_event_infantry_spawn_*` family.

The two Mengele country reports use `GFX_report_event_GER_himmler`, while the nested country-leader portrait in the Malta file remains a leader portrait and is not an event-picture reference.

## Decision-category repairs

The affected category definitions in `common/decisions/categories/006_independence_wave_categories.txt` now use the dedicated category icon family `GFX_decision_category_independence_wave_*`.

The Africa charter categories now use `GFX_decision_category_012_africa_charter_ledger`.

The death-survey category now uses `GFX_decision_category_independence_wave_death_survey`.

The Fallout food-security category now uses `GFX_decision_category_fallout_food_security`.

The disease-containment decision in `common/decisions/biowarfare_disease_containment_decisions.txt` now uses the normal decision sprite `GFX_decision_black_plague_quarantine`.

The weaponized-zombie category panels no longer use portrait sprites.

The independence-wave category panels no longer use category-icon sprites as pictures.

## Category asset registry

All newly generated category visuals are registered in `interface/visual_consistency_repair.gfx`.

Category icons live under `gfx/interface/decisions/visual_consistency_repair/categories/` and use the following code names and runtime files.

| Code name | Runtime DDS |
| --- | --- |
| `GFX_decision_category_independence_wave_integration` | `decision_category_independence_wave_integration.dds` |
| `GFX_decision_category_independence_wave_government` | `decision_category_independence_wave_government.dds` |
| `GFX_decision_category_independence_wave_diplomacy` | `decision_category_independence_wave_diplomacy.dds` |
| `GFX_decision_category_independence_wave_network` | `decision_category_independence_wave_network.dds` |
| `GFX_decision_category_independence_wave_borders` | `decision_category_independence_wave_borders.dds` |
| `GFX_decision_category_independence_wave_death_survey` | `decision_category_independence_wave_death_survey.dds` |
| `GFX_decision_category_012_africa_charter_ledger` | `decision_category_012_africa_charter_ledger.dds` |
| `GFX_decision_category_fallout_food_security` | `decision_category_fallout_food_security.dds` |

Each category icon is authored at the 52x40 category scale with native transparency.

The expanded repair package adds dedicated category-scale icons for the remaining legacy category consumers.

| Code name | Runtime DDS |
| --- | --- |
| `GFX_decision_category_repair_012_africa_priority_member` | `decision_category_012_africa_priority_member.dds` |
| `GFX_decision_category_repair_011_secret_alliance_foreign_interference` | `decision_category_011_secret_alliance_foreign_interference.dds` |
| `GFX_decision_category_repair_011_secret_alliance_coalition_crisis` | `decision_category_011_secret_alliance_coalition_crisis.dds` |
| `GFX_decision_category_repair_cannibalism_achievement_tracker` | `decision_category_cannibalism_achievement_tracker.dds` |
| `GFX_decision_category_repair_cannibalism_containment` | `decision_category_cannibalism_containment.dds` |
| `GFX_decision_category_repair_cannibalism_international_response` | `decision_category_cannibalism_international_response.dds` |
| `GFX_decision_category_repair_cannibalism_network_alerts` | `decision_category_cannibalism_network_alerts.dds` |
| `GFX_decision_category_repair_cannibalism_reconstruction` | `decision_category_cannibalism_reconstruction.dds` |
| `GFX_decision_category_repair_cannibalism_unified_command` | `decision_category_cannibalism_unified_command.dds` |
| `GFX_decision_category_repair_cannibalism_unified_global_campaign` | `decision_category_cannibalism_unified_global_campaign.dds` |
| `GFX_decision_category_repair_cannibalism_unified_larder` | `decision_category_cannibalism_unified_larder.dds` |
| `GFX_decision_category_repair_cannibalism_unified_war_machine` | `decision_category_cannibalism_unified_war_machine.dds` |
| `GFX_decision_category_repair_cannibalism_unified_world_end` | `decision_category_cannibalism_unified_world_end.dds` |
| `GFX_decision_category_repair_cannibalism_warlord_command` | `decision_category_cannibalism_warlord_command.dds` |
| `GFX_decision_category_repair_cannibalism_wendigo_command` | `decision_category_cannibalism_wendigo_command.dds` |
| `GFX_decision_category_repair_cannibalism_wendigo_counterwar` | `decision_category_cannibalism_wendigo_counterwar.dds` |
| `GFX_decision_category_repair_death_country` | `decision_category_death_country.dds` |
| `GFX_decision_category_repair_repression_ledger` | `decision_category_repression_ledger.dds` |
| `GFX_decision_category_repair_fallout_usa_continuity_projects` | `decision_category_fallout_usa_continuity_projects.dds` |
| `GFX_decision_category_repair_random_faction_bloc_pressure` | `decision_category_random_faction_bloc_pressure.dds` |
| `GFX_decision_category_repair_resources_found_anti_cave` | `decision_category_resources_found_anti_cave.dds` |
| `GFX_decision_category_repair_resources_found_cave` | `decision_category_resources_found_cave.dds` |
| `GFX_decision_category_repair_resources_found_containment` | `decision_category_resources_found_containment.dds` |
| `GFX_decision_category_repair_resources_found_field` | `decision_category_resources_found_field.dds` |
| `GFX_decision_category_repair_resources_found_trade` | `decision_category_resources_found_trade.dds` |
| `GFX_decision_category_repair_utopia_defense` | `decision_category_utopia_defense.dds` |
| `GFX_decision_category_repair_utopia_district` | `decision_category_utopia_district.dds` |
| `GFX_decision_category_repair_utopia_formation` | `decision_category_utopia_formation.dds` |
| `GFX_decision_category_repair_utopia_governance` | `decision_category_utopia_governance.dds` |
| `GFX_decision_category_repair_utopia_island` | `decision_category_utopia_island.dds` |
| `GFX_decision_category_repair_utopia_league` | `decision_category_utopia_league.dds` |
| `GFX_decision_category_repair_utopia_ledger` | `decision_category_utopia_ledger.dds` |
| `GFX_decision_category_repair_utopia_necessary_ground` | `decision_category_utopia_necessary_ground.dds` |
| `GFX_decision_category_repair_utopia_stewardship` | `decision_category_utopia_stewardship.dds` |

The expanded icons retain the same native-transparent 52x40 treatment and are registered in the same `.gfx` file.

Category pictures live under `gfx/interface/decisions/visual_consistency_repair/pictures/` and use the following code names and runtime files.

| Code name | Runtime DDS |
| --- | --- |
| `GFX_decision_cat_picture_weaponized_zombie_infected` | `decision_cat_picture_weaponized_zombie_infected.dds` |
| `GFX_decision_cat_picture_weaponized_zombie_rabid` | `decision_cat_picture_weaponized_zombie_rabid.dds` |
| `GFX_decision_cat_picture_weaponized_zombie_parasitic` | `decision_cat_picture_weaponized_zombie_parasitic.dds` |
| `GFX_decision_cat_picture_weaponized_zombie_mutant` | `decision_cat_picture_weaponized_zombie_mutant.dds` |
| `GFX_decision_cat_picture_weaponized_zombie_undead` | `decision_cat_picture_weaponized_zombie_undead.dds` |
| `GFX_decision_cat_picture_weaponized_zombie_necrotic` | `decision_cat_picture_weaponized_zombie_necrotic.dds` |
| `GFX_decision_cat_picture_weaponized_zombie_demonic` | `decision_cat_picture_weaponized_zombie_demonic.dds` |
| `GFX_decision_cat_picture_independence_wave_iw043_middle_volga_congress` | `decision_cat_picture_independence_wave_iw043_middle_volga_congress.dds` |
| `GFX_decision_cat_picture_independence_wave_iw058_council_of_communities` | `decision_cat_picture_independence_wave_iw058_council_of_communities.dds` |
| `GFX_decision_cat_picture_independence_wave_iw093_asante_compact` | `decision_cat_picture_independence_wave_iw093_asante_compact.dds` |
| `GFX_decision_cat_picture_independence_wave_iw098_sokoto_compact` | `decision_cat_picture_independence_wave_iw098_sokoto_compact.dds` |

Each category picture is authored at the 114x101 category-panel scale.

The source prompts, processed PNGs, DDS round-trip evidence, hashes, and handoff notes are kept in `docs/assets/visual_consistency_repair/category_icons/`, `docs/assets/visual_consistency_repair/category_icons_expanded/`, and `docs/assets/visual_consistency_repair/category_pictures/`.

## Chaos identity focus icons

`interface/chaos_focus_icons.gfx` carries the shared chaos identity focus icon family that is not owned by a single event package.

Icons live under `gfx/interface/goals/chaos/` and use the following code names and runtime files.

| Code name | Runtime DDS |
| --- | --- |
| `GFX_goal_chaos_the_unmaking` | `goal_chaos_the_unmaking.dds` |
| `GFX_goal_chaos_the_unmaking_shine` | `goal_chaos_the_unmaking.dds` |

The icon is authored at the native 94x86 focus scale with native transparency, a 4px transparent margin, and a subject centre within 0.5px of the canvas centre.

The house style for this family is read from the live chaos focus trees rather than from generic icon art: a dark heraldic medallion, a laurel or chain ring, one bold central emblem, a small shield or plaque, a desaturated storm field, and a single hot accent colour.

Source art, the processed candidate, the rejection record, the round-trip contact sheet, and the reference sheets taken from `gfx/interface/goals/010_death/` and `gfx/interface/goals/005_soviet_collapse/` are kept in `docs/assets/chaos_focus_icon/`.

The sprite has no focus consumer yet; binding it to a focus id, its localisation, and any AI weighting remain separate implementation work.

## Identifier and localisation repairs

The missing Event 100 and news 79-80 localisation keys are now present in `localisation/english/_chaosx_events_l_english.yml`.

The Greater Hui state-puzzle localisation keys now match the runtime category identifiers in `localisation/english/chaosx_formable_state_puzzles_l_english.yml`.

The duplicate scripted-localisation name in `common/scripted_localisation/fallout_consolidated_scripted_localisation.txt` now has a distinct `FalloutBridgeThatMovedEventLogPayload` identifier.

The duplicate active `GFX_terrain_water_shallow_sea_day` definition was removed from `interface/countrystateview.gfx`.

## Audit evidence and maintenance

The source-level event audit finds zero `country_event` blocks with `GFX_news*` pictures and zero `news_event` blocks with `GFX_report*` pictures.

The category audit finds zero portrait-family pictures in decision-category definitions and zero normal `GFX_decision_*` icons in category files, apart from established category sprites whose legacy names end in `_category` and the intentional `generic_formable_nations` alias.

The active interface-name audit finds no duplicate sprite names after ignoring commented-out vanilla alternatives.

All 42 category icon DDS files and all 11 category picture DDS files exist at the paths registered by `interface/visual_consistency_repair.gfx`.

Existing semantically appropriate report and news sprites were reused where the mod already had a valid family asset, so no new event art was introduced solely to replace a compatible existing image.

The old 32x32 sprite definitions remain registered where they no longer have active category consumers, preserving compatibility for any external or future references; the active category sources use only the repaired category-scale ids.

Future visual additions should register the consumer sprite before wiring source files, keep the consumer dimensions in the asset manifest, and run the event-family and category-family scans before handoff.
