# Specification packages

Specifications are accepted design sources. They remain separate from event implementation overviews and working plans.

## Package navigation

The Event 001 through Event 020 packages are the event-specific design roots in the current cleanup scope.

| Event | Package entry point |
| --- | --- |
| 001 Communism Spread | [`001_communism_spread_specs/README.md`](001_communism_spread_specs/README.md) |
| 002 Zombie Special Project | [`002_zombie_special_project_specs/README.md`](002_zombie_special_project_specs/README.md) |
| 003 Holy Realm | [`003_holy_realm_specs/README.md`](003_holy_realm_specs/README.md) |
| 004 Random War | [`004_random_war_specs/README.md`](004_random_war_specs/README.md) |
| 005 Soviet Collapse | [`005_soviet_collapse_specs/README.md`](005_soviet_collapse_specs/README.md) |
| 006 Independence Wave | [`006_independence_wave_specs/README.md`](006_independence_wave_specs/README.md) |
| 007 Fury | [`007_fury_specs/README.md`](007_fury_specs/README.md) |
| 008 Tensions Rising | [`008_tensions_rising_specs/README.md`](008_tensions_rising_specs/README.md) |
| 009 White Peace | [`009_white_peace_specs/README.md`](009_white_peace_specs/README.md) |
| 010 Death | [`010_death_specs/README.md`](010_death_specs/README.md) |
| 011 Secret Alliance | [`011_secret_alliance_specs/README.md`](011_secret_alliance_specs/README.md) |
| 012 Africa | [`012_africa_specs/README.md`](012_africa_specs/README.md) |
| 013 Natural Disasters | [`013_natural_disasters_specs/README.md`](013_natural_disasters_specs/README.md) |
| 014 Cannibalism | [`014_cannibalism_specs/README.md`](014_cannibalism_specs/README.md) |
| 015 Utopia Manifesto | [`015_utopia_manifesto_specs/README.md`](015_utopia_manifesto_specs/README.md) |
| 016 Brilliant Scientist | [`016_brilliant_scientist_specs/README.md`](016_brilliant_scientist_specs/README.md) |
| 017 Random Faction | [`017_random_faction_specs/README.md`](017_random_faction_specs/README.md) |
| 018 Resources Found | [`018_resources_found_specs/README.md`](018_resources_found_specs/README.md) |
| 019 Infantry Spawn | [`019_infantry_spawn_specs/README.md`](019_infantry_spawn_specs/README.md) |
| 020 Black Plague | [`020_black_plague_specs/README.md`](020_black_plague_specs/README.md) |

Event 021 and later package entries are preserved design or provenance navigation only; this table does not assert current implementation status for those event-specific packages.

| Event | Package entry point |
| --- | --- |
| 021 Random Civil War | [`021_random_civil_war_specs/README.md`](021_random_civil_war_specs/README.md) |
| 023 Soviet Nuclear Bombs | [`023_sov_nuclear_bombs_specs/README.md`](023_sov_nuclear_bombs_specs/README.md) |
| 024 Video Game in Sweden | [`024_video_game_in_sweden_specs/README.md`](024_video_game_in_sweden_specs/README.md) |
| 025 Alien Technology in Antarctica | [`025_alien_technology_in_antarctica_specs/README.md`](025_alien_technology_in_antarctica_specs/README.md) |
| 026 Black Friday | [`026_black_friday_specs/README.md`](026_black_friday_specs/README.md) |
| 027 Doctrine Research | [`027_doctrine_research_specs/README.md`](027_doctrine_research_specs/README.md) |
| 028 Asteroid Incoming | [`028_asteroid_incoming_specs/028_asteroid_incoming_spec_index.md`](028_asteroid_incoming_specs/028_asteroid_incoming_spec_index.md) |
| 029 Riches Found | [`029_riches_found_specs/README.md`](029_riches_found_specs/README.md) |
| 030 Time Traveler | [`030_time_traveler_specs/030_time_traveler_spec_index.md`](030_time_traveler_specs/030_time_traveler_spec_index.md) |
| 031 Random Terror | [`031_random_terror_specs/README.md`](031_random_terror_specs/README.md) |
| 032 Missiles | [`032_missiles_specs/README.md`](032_missiles_specs/README.md) |

Shared and cross-event specification packages are indexed below.

| Scope | Package entry point |
| --- | --- |
| Air Cleanliness and Fallout | [`air_cleanliness_fallout_specs/README.md`](air_cleanliness_fallout_specs/README.md) |
| Chaos Redux 3D model workflow | [`chaos_redux_3d_model_workflow_planning_package/README.md`](chaos_redux_3d_model_workflow_planning_package/README.md) |
| Chaos Warfare | [`chaos_warfare_system_specs/README.md`](chaos_warfare_system_specs/README.md) |
| Condemnation | [`condemnation_system_specs/README.md`](condemnation_system_specs/README.md) |
| Dynamic major event weights | [`dynamic_major_event_weights_specs/README.md`](dynamic_major_event_weights_specs/README.md) |
| Famine and Migration | [`famine_and_migration_system_specs/README.md`](famine_and_migration_system_specs/README.md) |
| Camp, Repression, and Atrocity Consequences | [`system_camp_repression_rework_specs/README.md`](system_camp_repression_rework_specs/README.md) |

## Package convention

- Event packages use `docs/specs/<event_id>_<slug>_specs/`.
- System packages use a descriptive `<slug>_specs/` directory.
- Each package should provide a root `README.md` or an equivalent named root index that identifies its accepted source, status, aliases, and superseded material; the Asteroid Incoming and Time Traveler packages use their named `*_spec_index.md` files.
- New packages should use `specs/`, `research/`, `matrices/`, `prompts/`, `validation/`, and `handoffs/` only when those surfaces exist.
- Existing historical filenames are preserved until their references and authority are reconciled.
