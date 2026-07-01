# Event 013 Natural Disasters

Event 013 is a minor repeatable disaster-season system. One firing creates one Event Log row and then schedules delayed disaster pulses through reusable sequence slots. Individual disasters inside the season can create reports, news, deaths, state damage, recovery missions, GUI warnings, and super-events, but they do not create additional Event Log entries.

## Runtime Flow

1. `chaosx.nr13.1` starts the sequence and calls `natural_disasters_start_sequence`.
2. The controller chooses a profile from current chaos pressure unless a caller has forced `natural_disasters_start_profile`.
3. A free sequence slot stores profile, total pulse count, current pulse count, forced family, follow-up family, source, target mode, report policy, recovery/death/super-event permissions, delay bounds, and any requested target state or country.
4. Hidden slot events `chaosx.nr13.101` through `chaosx.nr13.108` run delayed pulses.
5. Each pulse selects a family and validates the target against that family's trigger, applies building damage, opens recovery, records civilian deaths through the Deaths system when allowed, schedules a delayed report according to the profile's news policy, and queues family-specific follow-ups near the same region.
6. The slot cleans itself after the final pulse. Recovery decisions and missions continue until affected states are cleared or recovery fails.

Baseline seasons usually delay five to ten days between pulses. Evolution I compresses to multi-region cadence, Evolution II uses global and multi-state cadence with throttled news, and Evolution III allows abnormal families with short cadence plus special warnings.

## Disaster Families

The family constants live in `common/script_constants/013_natural_disasters_constants.txt`.

- Baseline and evolved weather/geophysical families: earthquake, flood, tropical cyclone, thunderstorm, hailstorm, extreme wind, wildfire, drought, dust storm, blizzard, heat wave, cold wave, dry mass movement, wet mass movement, volcanic eruption, tsunami, avalanche, glacial outburst, sinkhole, and limnic eruption.
- Evolution III abnormal families: meteor shower, global rupture, massive eruption, and storm corridor.

Each family has a matching target trigger in `common/scripted_triggers/013_natural_disasters_triggers.txt`, an entry in the family-validity trigger `natural_disaster_target_current_family`, a damage block in `natural_disasters_apply_state_damage_profile`, a death percentage in `natural_disaster_deaths`, aftermath flags, and recovery hooks. Event 013 heat-wave targeting excludes states already under the separate Event 051 heat-wave system. Forced direct calls do not fall back to generic invalid states; exact, country, and regional calls resolve only if the requested scope has a valid target for the requested family.

## Deaths and Damage

Building damage is applied directly to affected states with family-specific building types and damage constants. Population loss is routed through `chaos_meter_register_state_civilian_deaths_percent` using `constant:chaos_meter_deaths_reason.natural_disaster`, so Event 013 uses the shared Deaths system rather than a cosmetic variable. Prepared response flags from rescue, route clearance, supply, food/water, firebreak, ash/dust, and evacuation decisions reduce death percentages for later follow-up or warning-state hits.

## Reports, News, and Event Log

- `chaosx.nr13.201` through `chaosx.nr13.208` are delayed visible reports tied to sequence slots.
- `chaosx.nr13.301` through `chaosx.nr13.304` are high-level news or scenario broadcasts.
- Event Log integration uses `constant:natural_disaster_event.id` and `natural_disasters_latest_actor`.
- Evolution previews for stages I-III are registered in the Event Log detail view.
- Individual pulses are deliberately not logged as separate event rows.
- Report scheduling uses `natural_disaster_report_policy`: direct calls normally report, baseline and Evolution I report early or important hits, and Evolution II/III plus SCN-007 throttle reports to first, player-relevant, major, capital, severe, or abnormal hits.

## Recovery Decisions and Missions

`common/decisions/013_natural_disasters_decisions.txt` defines concrete-cost state-targeted response actions:

- deploy rescue columns
- clear blocked routes
- restore supply lifelines
- reopen ports and airfields
- import food and water
- cut firebreaks
- clear ash and dust
- evacuate the predicted path

Costs spend command power, manpower, fuel, trains, convoys, infantry equipment, motorized equipment, and support equipment directly. There is no political-power store. Stabilization and reconstruction missions watch whether all recovery states are cleared before timeout; success gives small stability recovery, while failure applies stability or war-support pressure and disqualifies the relevant recovery achievements.

## Scripted GUI and Animated Assets

`common/scripted_guis/013_natural_disasters_scripted_gui.txt` and `interface/013_natural_disasters.gui` expose abnormal disaster warning state. Moving storm corridors mark an impact state plus neighboring path states with `natural_disaster_corridor_path_state` and `natural_disaster_corridor_warning`, allowing predicted-path evacuation before a follow-up wind hit resolves near the same regional seed. The GUI uses animated sprites from `interface/013_natural_disasters.gfx`:

- `GFX_natural_disaster_warning_pulse`
- `GFX_natural_disaster_storm_corridor_track`
- `GFX_natural_disaster_tsunami_countdown`
- `GFX_natural_disaster_eruption_ashfall`
- `GFX_natural_disaster_skyfall_alarm`

Source frames, sheets, contact sheets, static fallbacks, and previews are tracked under `docs/assets/013_natural_disasters/animations/`.

## Super-Events and Audio

Evolution III abnormal thresholds set `global.current_super_event_audio_id` and `super_event_visible` for four super-event slots:

- `67`: global rupture, `GFX_super_event_nd_great_rupture`
- `68`: massive eruption, `GFX_super_event_nd_massive_eruption`
- `69`: meteor shower, `GFX_super_event_nd_skyfall`
- `70`: moving storm corridor, `GFX_super_event_nd_storm_corridor`

Music-mode and sound-effect-mode audio are registered in `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt`, and `sound/chaosx_sound.asset`. Text research is documented in `docs/super_events/013_natural_disasters_super_event_research.md`; asset and audio paths are tracked in `docs/assets/013_natural_disasters/manifest.md`.

## Public API

Other systems can call Event 013 without duplicating disaster logic. Public request knobs are temp variables or event targets consumed by `natural_disasters_start_sequence` and persisted into the allocated slot:

- `natural_disasters_start_sequence = yes` starts a normal season from the current scope.
- `natural_disasters_call_direct_family = yes` starts a direct one-family disaster. Set `natural_disasters_start_family` first to force the family.
- `natural_disasters_call_targeted_state_family = yes` requires `natural_disasters_direct_target_state` to be saved as an event target and resolves only if that state is valid for the requested family.
- `natural_disasters_call_targeted_country_family = yes` requires `natural_disasters_direct_target_country` to be saved as an event target and chooses a valid controlled state in that country.
- `natural_disasters_call_regional_family = yes` uses `natural_disasters_direct_target_state` as a regional seed and chooses a valid neighboring state, falling back only to the seed if the seed itself is valid.
- `natural_disasters_call_world_family = yes` selects a valid world target for the requested family.
- `natural_disasters_call_direct_sandstorm = yes` preserves old sandstorm call sites while routing them into Event 013.
- `natural_disasters_start_disaster_barrage = yes` launches the SCN-007 sequence profile.
- `natural_disasters_start_total` can force pulse count; `natural_disasters_start_delay_min` and `natural_disasters_start_delay_max` can force delay bounds; `natural_disasters_start_report_policy` accepts `auto`, `quiet`, `first_only`, `important`, `always`, or `news_only`; `natural_disasters_start_recovery_allowed`, `natural_disasters_start_deaths_allowed`, and `natural_disasters_start_super_event_allowed` gate those subsystems for callers that own their own follow-up handling.

Examples:

```hoi4
set_temp_variable = { natural_disasters_start_family = constant:natural_disaster_family.earthquake }
natural_disasters_call_direct_family = yes
```

```hoi4
random_controlled_state = {
	limit = { natural_disaster_target_tsunami = yes }
	save_event_target_as = natural_disasters_direct_target_state
}
set_temp_variable = { natural_disasters_start_family = constant:natural_disaster_family.tsunami }
set_temp_variable = { natural_disasters_start_report_policy = constant:natural_disaster_report_policy.important }
natural_disasters_call_targeted_state_family = yes
```

```hoi4
set_temp_variable = { natural_disasters_start_scenario_intensity = constant:triggerable_scenario_intensity.maximum }
set_temp_variable = { natural_disasters_start_family = constant:natural_disaster_family.meteor_shower }
natural_disasters_start_disaster_barrage = yes
```

## Scenario and Cluster Integration

SCN-007 Disaster Barrage uses `trigger_disaster_barrage_scenario` in `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`. It can launch mixed, skyfall, global rupture, massive eruption, or storm corridor openings. Intensity controls pulse count and cadence: low two to four pulses with four-to-seven-day cadence, medium five to eight with two-to-five-day cadence, high eight to fourteen with one-to-four-day cadence, and maximum twelve to twenty with one-to-three-day cadence.

The Natural Disasters event cluster is `constant:event_cluster_id.natural_disasters = 5`. It can queue multiple delayed Event 013 members: a required opening season, an optional follow-up season, and a higher-chaos escalation season. Documentation lives in `docs/systems/event_clusters.md`.

## Placeholder Conversions

Event 046 Earth Earthquake and Event 099 Sandstorm are reserved placeholders after their logic is integrated into Event 013. Existing sandstorm call sites route through `natural_disasters_call_direct_sandstorm` or delayed `chaosx.nr13.109`. Event 051 Heat Wave remains separate and Event 013 heat targeting avoids stacking with its active idea.

## Achievements

Event 013 registers eight achievements in `common/achievements/chaos_redux_achievements.txt` and `localisation/english/chaosx_achievements_l_english.yml`.

- Against the Season: clear all active recovery after a season without recovery failure and keep capital control.
- Faultline Accountant: survive an earthquake-chain response with supply and port/airfield recovery.
- Eye of the Road: use predicted-path evacuation on three storm corridor states.
- Ash Winter Bureau: stabilize food/water and clear ash after a massive eruption.
- Skyfall Drill: recover local infrastructure after a meteor shower.
- Ring of Firebreaks: complete three firebreak responses.
- Dust Has No Master: restore supply and clear dust during a wartime dust storm.
- Barrage Survivor: complete maximum Disaster Barrage recovery after abnormal disasters.

Icon DDS triplets live in `gfx/achievements/` and are registered in `interface/chaosx_achievements.gfx`.

## Asset Wiring

Event 013 art is wired through:

- `interface/013_natural_disasters.gfx` for reports, news, decisions, category pictures, and animated GUI sprites.
- `interface/chaosx_super_events.gfx` for super-event images.
- `interface/chaosx_achievements.gfx` for achievement icon aliases.

The asset manifest and handoff are `docs/assets/013_natural_disasters/manifest.md` and `docs/assets/013_natural_disasters/gfx_handoff.md`.

## Future Extensions

- Add deeper regional after-effect chains for refugee movement, famine pressure, and international aid without adding per-pulse Event Log rows.
- Add more direct API examples as other events start using forced disaster calls.
- Add additional achievement art variants if the achievement UI grows a dedicated Event 013 page.
