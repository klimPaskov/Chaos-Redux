# Kuznetsk Mining Board

## Overview

The Kuznetsk Mining Board is a high-chaos Soviet Collapse successor built around resource sovereignty. It spawns from the Kuznetsk basin when high-chaos successor pressure is active and Khakassia is not already present.

The Board treats coal, metals, oil-shale work, rail dispatches, and concession ledgers as state authority. It is meant to play as an aggressive resource state rather than another generic breakaway republic.

## Gameplay Flow

1. High-chaos release logic checks `can_soviet_collapse_spawn_kmb`.
2. State 569 transfers to `KMB`, receives a core, and loads `KMB_soviet_collapse_focus_tree`.
3. `soviet_collapse_setup_kmb_successor` applies the `kmb_subsoil_quota_state` idea, basin-scale resource expansion, manpower, equipment, assault columns, coal-golem columns, and the high-chaos evolution log.
4. The sixteen-focus tree unlocks decisions for progressive subsoil expansion, coal-for-machine exchange, export auctions, resource treaties, oil-for-truck barter, targeted forced mining concessions, foreign industrial tenders, and conquered-basin policy.
5. Forced concessions target an explicitly selected eligible neighboring country, while trade decisions improve resources, industry, fuel, trucks, coal-golem equipment, liaison reach, market access, resource-rights deals, and foreign-supply planning.
6. Conquest of states 570, 571, 572, and 578 opens a mutually exclusive policy choice between direct board rule, a Khakass concession authority, and a resource corridor.

## Resource And Unit Identity

KMB is tuned as an absurd high-chaos resource state, not a normal breakaway. The setup and opening focus add very large resource values to state 569:

- coal as the primary resource surge
- steel, tungsten, chromium, aluminum, oil, and rubber as secondary board-controlled quotas
- extra infrastructure, civilian industry, arms industry, and synthetic capacity

The recurring extraction decision uses `soviet_collapse_kmb_resource_expansion_stage` and the `soviet_collapse_kmb_balance` script constants. Each completion adds a large all-resource package, then adds extra coal and secondary-resource steps as the stage rises, capped by `resource_expansion_stage_cap`.

The export auction and treaty decisions use opinion, market access, and state 569 resource-rights deals so KMB can convert its resource glut into external industrial support instead of only stacking local deposits.

Coal golems are KMB's unique shock unit. Their equipment archetype uses `can_be_produced = { tag = KMB }`, so only the Kuznetsk Mining Board can produce any coal-golem equipment variant:

- equipment file: `common/units/equipment/coal_golems.txt`
- subunit file: `common/units/coal_golems.txt`
- template helper: `soviet_collapse_kmb_create_coal_golem_template`
- spawn helpers: `soviet_collapse_kmb_spawn_coal_golem_columns`, `soviet_collapse_kmb_spawn_focus_coal_golem_columns`, and `soviet_collapse_kmb_spawn_mass_coal_golem_columns`

`KMB_raise_furnace_columns` is the dedicated focus for a mass coal-golem call-up. Ordinary focus rewards spawn several columns, while this focus spawns a larger furnace-column wave. Manpower support is calculated from the number of spawned columns and `coal_golem_manpower_per_column`.

Coal golems are slow infantry-format battalions with tank-like armor, piercing, hard attack, breakthrough, and hardness. Their limiting factor is production: `coal_golem_equipment_1` costs a large amount of coal plus steel, chromium, and tungsten. The battalion remains globally inactive and is instantiated only through KMB's dedicated template and spawn helpers.

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

The KMB identity idea uses the dedicated `gfx/interface/ideas/005_soviet_collapse/005_kmb_subsoil_quota_state.dds` texture through `GFX_idea_kmb_subsoil_quota_state`.

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

Dedicated KMB focus, decision, and identity-idea icons are installed with source PNGs, processed previews, DDS files, contact sheets, hashes, and an exact wiring manifest under `docs/assets/005_soviet_collapse/`.

## Completed Follow-Up Package (2026-08-09)

- `kmb_force_mining_concession` is a country-targeted decision. Every decision instance names and scopes its eligible neighboring target instead of selecting a random neighbor at completion.
- `kmb_accept_machine_tool_bid` and `kmb_accept_armaments_bid` form a mutually exclusive foreign tender competition for Kuznetsk output.
- `kmb_integrate_conquered_basin` applies direct board rule and cores the conquered basin.
- `kmb_establish_concession_authority` releases a KHA concession puppet across the conquered basin while preserving KMB control of state 569 and giving KMB resource rights.
- `kmb_establish_resource_corridor` develops and claims the basin as an armed extraction corridor without direct integration.
- All decision costs, resource steps, factory grants, equipment grants, crisis pressure, and policy flags use centralized Event 005 constants and helpers.

## Implemented shared-crisis and AI hooks (2026-07-11)

The six Mining Board decision costs are centralized. A signed resource treaty raises KMB depot control while increasing Moscow's Depot Vulnerability and Foreign Appetite and prioritizing Corridors and Depots. A successful forced concession raises Moscow's Depot Vulnerability, Republic Confidence, and Foreign Appetite and prioritizes both corridor and settlement work. These hooks use the existing decisions and add no focus node or release timer.

KMB AI now protects state 569, allocates infantry and train production, reserves one coal-golem factory after Guard the Pitheads and two after Raise Furnace Columns, avoids opportunistic wars while isolated on the treaty route, and enters concession posture only when a valid neighboring target exists and KMB exceeds the shared 1.25 strength ratio. The targeted concession decision and strategy use the same reusable target triggers. Its direct-rule, concession-authority, and resource-corridor policy weights respond to war, stability, and faction context, while tender weights distinguish peacetime industrial investment from wartime armaments demand.
