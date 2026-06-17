# Event 013 - Natural Disasters

Event 013 is `Natural Disasters`, a minor repeatable event rooted at `chaosx.nr13.1`. It creates local, named disaster incidents that damage industry, transport, ports, airfields, and population without acting as a world-end event. The system is built around warning, impact, aftermath, recovery, and evolved burst phases, with all target selection, damage, recovery costs, achievements, and cleanup routed through the Event 013 helper layer.

## Flow

The hidden root event prepares a valid country and state target, records the current evolution stage, rolls a disaster family, severity, and warning chance, then schedules the warning and impact events. Warnings name the affected state and open the Disaster Response Office so the controller can pre-position relief trains, evacuate industrial districts, reinforce floodworks, close ports, move air wings, ration grain and water, inspect dams and tunnels, or activate observatory alerts before the impact arrives.

The impact event applies family-specific building damage, population loss, cooldown memory, a visible state aftermath modifier, event-log data, and recovery cost variables. Baseline disasters stay local and recoverable. Evolution I adds varied local bursts, Evolution II increases regional pressure, Evolution III adds chained aftermath risk, and Evolution IV opens abnormal variants such as meteor showers, massive storm, tsunami, volcano, and earthquake-wave incidents. Evolution IV can fire the researched super-event package but does not start a world-end scenario.

Manual `Disaster Barrage` launches through the triggerable scenarios system. It bypasses normal random-event pacing, lets the player select Random Barrage, Geological Crisis, Weather Crisis, Skyfall Crisis, or Full Catalogue types, and scales incident count and severity by Low, Medium, High, or Maximum intensity. Low rolls 3-5 baseline local incidents, Medium rolls 6-9 local or regional incidents, High rolls 10-14 chained incidents with one possible abnormal variant, and Maximum rolls 16-24 incidents with Evolution IV variants enabled. Scenario context is scoped by flags and global variables that are cleared by the scenario cleanup event.

Event 046 is no longer a duplicate active earthquake system. Its file remains only as an inactive `Unknown Placeholder` for catalog compatibility, while seismic gameplay routes through Event 013.

## Gameplay Surfaces

- Event script: `events/013_natural_disasters.txt`
- Event 046 placeholder: `events/046_great_earthquake.txt`
- Constants: `common/script_constants/013_natural_disasters_constants.txt`
- Effects: `common/scripted_effects/013_natural_disasters_effects.txt`
- Triggers: `common/scripted_triggers/013_natural_disasters_triggers.txt`
- State modifiers: `common/dynamic_modifiers/013_natural_disasters_state_modifiers.txt`
- Decisions and missions: `common/decisions/013_natural_disasters_decisions.txt`
- Event-family scripted localisation: `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`
- Event log, details, and evolution details: shared `chaosx_events_log` effects and scripted localisation
- Triggerable scenario: SCN-007 in the shared triggerable scenario files
- Cluster: Natural Disasters cluster with Event 13 as the only Low-severity member
- Super-event assets/audio: shared super-event scripted localisation, `interface/chaosx_super_events.gfx`, `music/chaosx_super_event_music.*`, and `sound/chaosx_sound.asset`
- Localisation: `localisation/english/013_natural_disasters_l_english.yml`, plus shared GUI, achievements, event-name, scenario, and Event 046 files

## Decisions, Missions, And AI

The Disaster Response Office is visible only when a country has an active warning, active aftermath, or active manual barrage context. Warning decisions target warned states. Recovery decisions target affected states. The decisions use dynamic equipment, fuel, manpower, command power, army experience, stability, and war-support costs derived from the current severity; political power is not the default cost.

Warning decisions:

- `natural_disaster_preposition_relief_trains`
- `natural_disaster_evacuate_industrial_districts`
- `natural_disaster_reinforce_flood_barriers`
- `natural_disaster_close_vulnerable_ports`
- `natural_disaster_move_air_wings_inland`
- `natural_disaster_grain_and_water_rationing`
- `natural_disaster_inspect_dams_and_tunnels`
- `natural_disaster_observatory_alert`

Recovery and impact decisions:

- `natural_disaster_dispatch_emergency_engineers`
- `natural_disaster_send_medical_columns`
- `natural_disaster_emergency_railway_repair`
- `natural_disaster_firebreak_mobilisation`
- `natural_disaster_shoreline_rescue`
- `natural_disaster_open_relief_convoys`
- `natural_disaster_temporary_shelter_program`
- `natural_disaster_ash_clearance_crews`
- `natural_disaster_controlled_factory_shutdown`

Cross-border and regional aid decisions:

- `natural_disaster_offer_relief_mission_to_FROM`
- `natural_disaster_military_bridge_teams_to_FROM`
- `natural_disaster_international_ash_warning_to_FROM`
- `natural_disaster_joint_river_commission_with_FROM`
- `natural_disaster_accept_disaster_refugees_from_FROM`
- `natural_disaster_seal_border_camps_against_FROM`

Timed missions open from country-level mission flags created when a matching aftermath appears and a real objective surface exists. Each mission marks the affected state as its live objective: transport missions require a marked rail, supply, or infrastructure state; dam-watch, mountain-pass, and crater-survey missions require controlled divisions still present in the marked state; port missions require a marked coastal, port, or dockyard state; ash missions require a marked airbase, supply, or infrastructure state; population missions require a marked meaningfully populated state. They complete only when the marked objective state is actually recovered and still satisfies the relevant surface check; passive expiry of a timed state modifier does not satisfy the mission.

Timed missions:

- `natural_disaster_restore_main_line_mission`
- `natural_disaster_hold_dam_watch_mission`
- `natural_disaster_keep_port_open_mission`
- `natural_disaster_feed_dry_belt_mission`
- `natural_disaster_guard_mountain_passes_mission`
- `natural_disaster_clear_ash_fields_mission`
- `natural_disaster_rehouse_displaced_mission`
- `natural_disaster_survey_crater_belt_mission`

AI weights prioritise capital states, factory states, supply hubs, ports, railways, airbases, high-population states, and war-front logistics. Expensive convoy, train, and stability decisions are weighted down when the AI lacks the matching resources or stability.

## Achievements

Event 013 achievement state is recorded from warning mitigation, full recovery, family-specific recovery, manual scenario recovery, meteor-shower outcomes, port and rail responses, chained aftermath recovery, and no-world-end Evolution IV cleanup. Rail and port achievements require transport or port objective proof, `The Sea Walked Back` requires mitigated warning, restored ports, and civilian losses below the high-loss threshold, `No World End Required` requires recovery while the Chaos Meter remains below the terminal threshold, and `Still Standing in Four Seasons` lets manual Disaster Barrage recoveries count for only one family. Achievements are registered in `common/achievements/chaos_redux_achievements.txt`, localised in `localisation/english/chaosx_achievements_l_english.yml`, and use icon sprites in `interface/chaosx_achievements.gfx`.

Registered Event 013 achievements:

- `ACH_ND_RING_THE_BELL`
- `ACH_ND_ENGINEERS_OF_THE_RUBBLE`
- `ACH_ND_THE_TRAINS_ARRIVED`
- `ACH_ND_NO_PORT_LEFT_BEHIND`
- `ACH_ND_GRAIN_AGAINST_THE_DUST`
- `ACH_ND_ASH_ON_THE_RUNWAY`
- `ACH_ND_SKY_ARTILLERY_SURVIVOR`
- `ACH_ND_THE_SEA_WALKED_BACK`
- `ACH_ND_NOT_ONE_MORE_AFTERSHOCK`
- `ACH_ND_DISASTER_LEDGER_CLOSED`
- `ACH_ND_NO_WORLD_END_REQUIRED`
- `ACH_ND_STILL_STANDING_IN_FOUR_SEASONS`

## Assets

Event report and news images are registered in `interface/013_natural_disasters.gfx`:

- `GFX_report_event_natural_disaster_baseline`
- `GFX_report_event_natural_disaster_warning`
- `GFX_report_event_natural_disaster_impact`
- `GFX_report_event_natural_disaster_recovery`
- `GFX_report_event_natural_disaster_earthquake`
- `GFX_report_event_natural_disaster_flood`
- `GFX_report_event_natural_disaster_storm`
- `GFX_report_event_natural_disaster_drought`
- `GFX_report_event_natural_disaster_wildfire`
- `GFX_report_event_natural_disaster_landslide`
- `GFX_report_event_natural_disaster_volcano`
- `GFX_report_event_natural_disaster_tsunami`
- `GFX_report_event_natural_disaster_meteor`
- `GFX_news_event_regional_disaster_system`
- `GFX_news_event_disaster_chains`
- `GFX_news_event_abnormal_disaster_age`

Decision sprites are registered in `interface/013_natural_disasters.gfx` and live under `gfx/interface/decisions/natural_disasters/`. State-modifier idea sprites are registered in the same `.gfx` file and live under `gfx/interface/ideas/natural_disasters/`. Achievement icons live under `gfx/achievements/` and use the achievement ID as the filename stem with `_grey` and `_not_eligible` variants.

Super-event `67` uses `GFX_super_event_natural_disasters_abnormal_disaster_age`, music `super_event_natural_disasters_abnormal_disaster_age.ogg`, and sound asset `chaosx_super_event_67_track`. Text research selected `The Unquiet Earth`, the Bacon quote, and the Hamlet button line; audio research selected the public-domain Beethoven storm excerpt package.

Asset details and source files:

- `docs/assets/013_natural_disasters/manifest.md`
- `docs/assets/013_natural_disasters/gfx_handoff.md`
- `docs/assets/013_natural_disasters/achievement_icons/manifest.md`
- `docs/super_events/013_natural_disasters_super_event_research.md`
- `docs/super_events/013_natural_disasters_super_event_audio_research.md`

State-modifier idea sprites:

- `GFX_idea_recent_earthquake_damage`
- `GFX_idea_flooded_transport_belt`
- `GFX_idea_crop_failure_pressure`
- `GFX_idea_storm_wreckage`
- `GFX_idea_burned_districts`
- `GFX_idea_unstable_mountain_passes`
- `GFX_idea_volcanic_ashfall`
- `GFX_idea_tsunami_scoured_coast`
- `GFX_idea_meteor_scars`
- `GFX_idea_disaster_recovery_pressure`

## Future Plans

- Add a dedicated Disaster Ledger scripted GUI if the event grows beyond state-targeted decisions and missions.
- Replace generated static art without changing sprite names or final paths.
