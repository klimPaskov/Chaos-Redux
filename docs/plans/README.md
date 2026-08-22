# Plans, audits, and handoffs

This directory is the working documentation area. Accepted design belongs in `docs/specs/`, and current event behavior belongs in `docs/events/`.

## Folder convention

- Event work uses `<event_id>_<slug>_plans/`.
- Shared systems and workflows use descriptive `<slug>_plans/` directories.
- Subagent handoffs remain under `subagent_handoffs/`.
- New dated files use `YYYY-MM-DD_<scope>_<type>.md`.
- Historical audit and handoff filenames are preserved to avoid breaking evidence references.
- Large packages should provide `documentation_state.md`, `source_of_truth_map.md`, or an equivalent current-state index; plan workspaces do not require a boilerplate README.

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

## Shared plan groups

| Scope | Plan folder |
| --- | --- |
| Air Cleanliness and Fallout | [`air_cleanliness_fallout_plans/`](air_cleanliness_fallout_plans/) |
| Chaos Meter | [`chaos_meter_plans/`](chaos_meter_plans/) |
| Chaos levels | [`event_chaos_levels_plans/`](event_chaos_levels_plans/) |
| Chaos Warfare | [`chaos_warfare_system_plans/`](chaos_warfare_system_plans/) |
| Decision system | [`decision_system_plans/`](decision_system_plans/) |
| Formable state puzzles | [`formable_state_puzzle_plans/`](formable_state_puzzle_plans/) and [`decision_category_formable_state_puzzle_plans/`](decision_category_formable_state_puzzle_plans/) |
| Germany Mengele path | [`germany_mengele_path_plans/`](germany_mengele_path_plans/) |
| GFX, icon, flag, and map-mode cleanup | [`gfx_icon_flag_mapmode_cleanup_plans/`](gfx_icon_flag_mapmode_cleanup_plans/) |
| Player-facing text style | [`player_facing_text_style_cleanup/`](player_facing_text_style_cleanup/) |
| Repository cleanup | [`repo_cleanup/`](repo_cleanup/README.md) |
| Shared GFX asset integrity | [`shared_gfx_asset_integrity_plans/`](shared_gfx_asset_integrity_plans/) |
| System camp repression rework | [`system_camp_repression_rework_plans/`](system_camp_repression_rework_plans/) |
| World-end scenarios | [`world_end_scenarios_plans/`](world_end_scenarios_plans/) |

## Workflow and model packages

| Scope | Plan folder |
| --- | --- |
| 3D model pilot work | [`chaos_redux_3d_model_pilots_plans/`](chaos_redux_3d_model_pilots_plans/) |
| 3D model workflow handoff | [`chaos_redux_3d_model_workflow_skill_handoff/`](chaos_redux_3d_model_workflow_skill_handoff/) |
| ComfyUI workflow | [`comfyui_workflow/`](comfyui_workflow/) |
| Event-system workflow | [`event_system_plans/`](event_system_plans/) |
