# Kuznetsk Mining Board

## Overview

The Kuznetsk Mining Board is a high-chaos Soviet Collapse successor built around resource sovereignty. It spawns from the Kuznetsk basin when high-chaos successor pressure is active and Khakassia is not already present.

The Board treats coal, metals, oil-shale work, rail dispatches, and concession ledgers as state authority. It is meant to play as an aggressive resource state rather than another generic breakaway republic.

## Gameplay Flow

1. High-chaos release logic checks `can_soviet_collapse_spawn_kmb`.
2. State 569 transfers to `KMB`, receives a core, and loads `KMB_soviet_collapse_focus_tree`.
3. `soviet_collapse_setup_kmb_successor` applies the `kmb_subsoil_quota_state` idea, basin-scale resource expansion, manpower, equipment, assault columns, coal-golem columns, and the high-chaos evolution log.
4. The focus tree unlocks decisions for progressive subsoil expansion, coal-for-machine exchange, export auctions, resource treaties, oil-for-truck barter, and forced mining concessions.
5. Forced concessions use neighboring war-plan logic, while trade decisions improve resources, industry, fuel, trucks, coal-golem equipment, liaison reach, market access, resource-rights deals, and foreign-supply planning.

## Resource And Unit Identity

KMB is tuned as an absurd high-chaos resource state, not a normal breakaway. The setup and opening focus add very large resource values to state 569:

- coal as the primary resource surge
- steel, tungsten, chromium, aluminum, oil, and rubber as secondary board-controlled quotas
- extra infrastructure, civilian industry, arms industry, and synthetic capacity

The recurring extraction decision uses `soviet_collapse_kmb_resource_expansion_stage` and the `soviet_collapse_kmb_balance` script constants. Each completion adds a large all-resource package, then adds extra coal and secondary-resource steps as the stage rises, capped by `resource_expansion_stage_cap`.

The export auction and treaty decisions use opinion, market access, and state 569 resource-rights deals so KMB can convert its resource glut into external industrial support instead of only stacking local deposits.

Coal golems are KMB's unique shock unit:

- equipment file: `common/units/equipment/coal_golems.txt`
- subunit file: `common/units/coal_golems.txt`
- template helper: `soviet_collapse_kmb_create_coal_golem_template`
- spawn helpers: `soviet_collapse_kmb_spawn_coal_golem_columns`, `soviet_collapse_kmb_spawn_focus_coal_golem_columns`, and `soviet_collapse_kmb_spawn_mass_coal_golem_columns`

`KMB_raise_furnace_columns` is the dedicated focus for a mass coal-golem call-up. Ordinary focus rewards spawn several columns, while this focus spawns a larger furnace-column wave. Manpower support is calculated from the number of spawned columns and `coal_golem_manpower_per_column`.

Coal golems are slow infantry-format battalions with tank-like armor, piercing, hard attack, breakthrough, and hardness. Their limiting factor is production: `coal_golem_equipment_1` costs a large amount of coal plus steel, chromium, and tungsten.

## Files

- `common/country_tags/chaosx_countries.txt`
- `common/countries/Kuznetsk Mining Board.txt`
- `history/countries/KMB - Kuznetsk Mining Board.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/decisions/categories/005_soviet_collapse_categories.txt`
- `common/ideas/005_soviet_collapse_ideas.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/units/equipment/coal_golems.txt`
- `common/units/coal_golems.txt`
- `interface/chaosx_equipment.gfx`
- `interface/chaosx_subuniticons.gfx`
- `events/005_soviet_collapse.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `localisation/english/chaosx_countries_l_english.yml`
- `localisation/english/chaosx_units_l_english.yml`

## Assets

The current idea icon reuses `gfx/interface/ideas/soviet_collapse/005_uwd_custom_splinter_idea.dds` through `GFX_idea_kmb_subsoil_quota_state`.

The KMB leader portrait is a generated miner portrait:

- sprite: `GFX_portrait_KMB_mine_foreman`
- texture: `gfx/leaders/005_soviet_collapse/KMB_leader.dds`

The KMB country flags use a generated mining-board flag under:

- `gfx/flags/KMB*.tga`
- `gfx/flags/medium/KMB*.tga`
- `gfx/flags/small/KMB*.tga`

Coal-golem assets:

- equipment icon: `gfx/interface/technologies/coal_golem_equipment.dds`
- large counter: `gfx/interface/counters/divisions_large/unit_coal_golem_icon.dds`
- small counter: `gfx/interface/counters/divisions_small/onmap_unit_coal_golem_icon.dds`

Future art pass:

- optional dedicated KMB idea, focus, and decision icon set.

## Future Depth

- Add targeted concession decisions against specific neighboring resource states once a safe dynamic target UI is available.
- Add treaty chains where foreign industrial powers compete for Kuznetsk output.
- Add late-game integration choices for conquered basins: direct board rule, concession puppet, or resource corridor.
