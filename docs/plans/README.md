# Plans, audits, and handoffs

This directory is the working documentation area.
Accepted design belongs in `docs/specs/`, and evidence-backed implementation summaries belong in `docs/events/`.
An old plan, prompt, or handoff does not authorize a new task or prove current behavior.

## Folder convention

- Event work uses `<event_id>_<slug>_plans/`.
- Shared systems and workflows use descriptive `<slug>_plans/` directories.
- Subagent handoffs remain under `subagent_handoffs/`.
- New dated files use `YYYY-MM-DD_<scope>_<type>.md`.
- Historical audit and handoff filenames are preserved to avoid breaking evidence references.
- Large packages should provide `documentation_state.md`, `source_of_truth_map.md`, or an equivalent current-state index.
  Plan workspaces do not require a boilerplate README.

## Plan dispositions

Use the package's existing state or resume record to track every active plan or addendum.
Record the decision basis and relevant implementation evidence separately.

| Disposition | Required basis |
| --- | --- |
| Implemented | Exact implementation evidence and remaining validation limits. |
| Promoted into an accepted spec | Acceptance basis and the named destination specification. |
| Accepted and queued | Acceptance basis and the reason implementation remains queued. |
| Rejected | Recorded rejection and its reason. |
| Superseded | Named replacement and the requirements or durable evidence retained there. |
| Blocked | Exact missing input, capability, or unresolved authority that prevents the work. |
| Unresolved | The decision or evidence still needed. Absence of approval is not rejection. |

Do not promote detailed proposals merely because they look complete.
Preserve useful historical findings with their dates and source context.

## Event plan groups

| Event | Plan folder |
| --- | --- |
| 001 Communism Spread | [`001_communism_spread_plans/`](001_communism_spread_plans/) |
| 002 Zombie Outbreak | [`002_zombie_outbreak_zombies_plans/`](002_zombie_outbreak_zombies_plans/) |
| 003 Holy Realm | [`003_holy_realm_plans/`](003_holy_realm_plans/) |
| 005 Soviet Collapse | [`005_soviet_collapse_plans/`](005_soviet_collapse_plans/) |
| 006 Independence Wave | [`006_independence_wave_plans/`](006_independence_wave_plans/) |
| 007 Fury | [`007_fury_plans/`](007_fury_plans/) |
| 008 Tensions Rising | [`008_tensions_rising_plans/`](008_tensions_rising_plans/) |
| 009 White Peace | [`009_white_peace_plans/`](009_white_peace_plans/) |
| 010 Death ghost hosts | [`010_death_ghost_hosts_plans/`](010_death_ghost_hosts_plans/) |
| 010 Death | [`010_death_plans/`](010_death_plans/) |
| 011 Secret Alliance | [`011_secret_alliance_plans/`](011_secret_alliance_plans/) |
| 012 Africa | [`012_africa_plans/`](012_africa_plans/) |
| 013 Natural Disasters | [`013_natural_disasters_plans/`](013_natural_disasters_plans/) |
| 014 Cannibalism | [`014_cannibalism_plans/`](014_cannibalism_plans/) |
| 015 Utopia Manifesto | [`015_utopia_manifesto_plans/`](015_utopia_manifesto_plans/) |
| 016 Brilliant Scientist | [`016_brilliant_scientist_plans/`](016_brilliant_scientist_plans/) |
| 017 Random Faction | [`017_random_faction_plans/`](017_random_faction_plans/) |
| 018 Resources Found | [`018_resources_found_plans/`](018_resources_found_plans/) |
| 019 Infantry Spawn | [`019_infantry_spawn_plans/`](019_infantry_spawn_plans/) |
| 020 Black Plague | [`020_black_plague_plans/`](020_black_plague_plans/) |
| 021 Random Civil War | [`021_random_civil_war_plans/`](021_random_civil_war_plans/) |
| 023 Soviet Nuclear Bombs | [`023_sov_nuclear_bombs_plans/`](023_sov_nuclear_bombs_plans/) |
| 024 Video Game in Sweden | [`024_video_game_in_sweden_plans/`](024_video_game_in_sweden_plans/) |
| 025 Alien Technology in Antarctica | [`025_alien_technology_in_antarctica_plans/`](025_alien_technology_in_antarctica_plans/) |
| 026 Black Friday | [`026_black_friday_plans/`](026_black_friday_plans/) |
| 027 Doctrine Research | [`027_doctrine_research_plans/`](027_doctrine_research_plans/) |
| 028 Asteroid Incoming | [`028_asteroid_incoming_plans/`](028_asteroid_incoming_plans/) |
| 029 Riches Found | [`029_riches_found_plans/`](029_riches_found_plans/) |
| 031 Random Terror | [`031_random_terror_plans/`](031_random_terror_plans/) |
| 032 Missiles | [`032_missiles_plans/`](032_missiles_plans/) |
| 033 Acid Rain | [`033_acid_rain_plans/`](033_acid_rain_plans/) |
| 035 Great Depression | [`035_great_depression_plans/`](035_great_depression_plans/) |
| 039 Murder Mystery | [`039_murder_mystery_plans/`](039_murder_mystery_plans/) |
| 040 Lawrence of Arabia | [`040_lawrence_of_arabia_plans/`](040_lawrence_of_arabia_plans/) |
| 046 The Great Shuffle | [`046_the_great_shuffle_plans/`](046_the_great_shuffle_plans/) |
| 047 BOOM | [`047_boom_plans/`](047_boom_plans/) |
| 050 The Great Embargo | [`050_the_great_embargo_plans/`](050_the_great_embargo_plans/) |
| 059 The Offensive | [`059_the_offensive_plans/`](059_the_offensive_plans/) |
| 061 Return to Peacetime | [`061_return_to_peacetime_plans/`](061_return_to_peacetime_plans/) |
| 064 Border Fortifications | [`064_border_fortifications_plans/`](064_border_fortifications_plans/) |
| 065 Random Trait | [`065_random_trait_plans/`](065_random_trait_plans/) |

These links identify existing workspaces.
They do not establish acceptance, current implementation, or a completed review of the documents inside them.

## Shared plan groups

| Scope | Plan folder |
| --- | --- |
| Achievement asset workflow | [`achievement_asset_workflow_plans/`](achievement_asset_workflow_plans/) |
| Air Cleanliness and Fallout | [`air_cleanliness_fallout_plans/`](air_cleanliness_fallout_plans/) |
| Chaos Meter | [`chaos_meter_plans/`](chaos_meter_plans/) |
| Chaos levels | [`event_chaos_levels_plans/`](event_chaos_levels_plans/) |
| Chaos Warfare | [`chaos_warfare_system_plans/`](chaos_warfare_system_plans/) |
| Decision system | [`decision_system_plans/`](decision_system_plans/) |
| Event clusters | [`event_cluster_system_plans/`](event_cluster_system_plans/) |
| Famine and Migration | [`famine_and_migration_system_plans/`](famine_and_migration_system_plans/) |
| Formable state puzzles | [`formable_state_puzzle_plans/`](formable_state_puzzle_plans/) and [`decision_category_formable_state_puzzle_plans/`](decision_category_formable_state_puzzle_plans/) |
| Germany Mengele path | [`germany_mengele_path_plans/`](germany_mengele_path_plans/) |
| GFX, icon, flag, and map-mode cleanup | [`gfx_icon_flag_mapmode_cleanup_plans/`](gfx_icon_flag_mapmode_cleanup_plans/) |
| Player-facing text style | [`player_facing_text_style_cleanup/`](player_facing_text_style_cleanup/) |
| Repository cleanup | [`repo_cleanup/`](repo_cleanup/README.md) |
| Repression ledger | [`repression_ledger_plans/`](repression_ledger_plans/) |
| Shared GFX asset integrity | [`shared_gfx_asset_integrity_plans/`](shared_gfx_asset_integrity_plans/) |
| Super-event audio audit | [`super_event_audio_audit_plans/`](super_event_audio_audit_plans/) |
| System camp repression rework | [`system_camp_repression_rework_plans/`](system_camp_repression_rework_plans/) |
| Test country | [`chaosx_test_country_plans/`](chaosx_test_country_plans/) |
| World-end scenarios | [`world_end_scenarios_plans/`](world_end_scenarios_plans/) |

## Workflow and model packages

| Scope | Plan folder |
| --- | --- |
| 3D model pilot work | [`chaos_redux_3d_model_pilots_plans/`](chaos_redux_3d_model_pilots_plans/) |
| 3D model workflow handoff | [`chaos_redux_3d_model_workflow_skill_handoff/`](chaos_redux_3d_model_workflow_skill_handoff/) |
| ComfyUI workflow | [`comfyui_workflow/`](comfyui_workflow/) |
| Event-system workflow | [`event_system_plans/`](event_system_plans/) |
