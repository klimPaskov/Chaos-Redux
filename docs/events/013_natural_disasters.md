# Event 013 - Natural Disasters

Event 013 is `Natural Disasters`, a minor repeatable event rooted at `chaosx.nr13.1`. It has no world-end branch. It uses one hidden Event 13 entry to start a delayed disaster sequence, then runs warning, impact, aftermath, and recovery reports through triggered subevents that do not write new random-event history rows.

Event 13 follows `docs/specs/013_natural_disasters_specs/` as the source package. It has three non-terminal Evolution III super-events for the largest abnormal disaster families: `The Great Rupture` in slot `67`, `The Mountain Unsealed` in slot `68`, and `Stones from Heaven` in slot `69`. These broadcasts mark catastrophic disaster escalation and do not create a world-end branch.

## Flow

The hidden entry event records the sequence context, chooses the evolution stage, determines how many incidents are planned, and schedules the first incident report without showing a preparation popup. The hidden scheduler `chaosx.nr13.10` prepares the next family, scores owned states for the current family, selects the strongest valid target, and rolls whether the incident has usable warning. Warned incidents fire the state warning event, open the family response category, and schedule the impact. Missed-warning incidents skip the warning event and fire the impact after a short delay. The impact event applies building damage, state disruption, percentage-based population loss, civilian-death logging, aftermath flags, family objective state, and any regional follow-up. When all planned incidents are complete, `chaosx.nr13.30` cleans sequence context and may send one throttled family-routed news item for severe, deadly, abnormal, or scenario-scale sequences.

Baseline sequences use two incidents with 5 to 10 day spacing. Larger evolved sequences use more reports and shorter spacing through constants in `common/script_constants/013_natural_disasters_constants.txt`. The cluster queue also uses delayed member spacing. If a Natural Disasters cluster member comes due while another Event 13 sequence is active, the cluster waits and retries the same member instead of advancing past it.

One Event 13 sequence creates one Event 13 log row. Delayed subdisasters inside that sequence do not call the random-event dispatcher again. Natural Disasters cluster members are separate conceptual member slots, so each member slot that truly fires creates its own Event 13 sequence and history row.

## Families And Evolutions

The family table is stored in script constants and selected through scripted effects. The baseline pool covers flood, severe storm, earthquake, drought and famine pressure, wildfire, and winter weather. Evolution I adds cyclone, hail, wind, dust and sandstorm, landslide, slope collapse, heat, and volcanic incidents. Evolution II increases regional chaining, aftermath risk, neighbor impacts, and decision urgency. Evolution III adds abnormal families: meteor storm, skyfall, great rupture wave, massive eruption, delayed tsunami, and moving storm corridor.

Family targeting is handled in `common/scripted_triggers/013_natural_disasters_triggers.txt` and `common/scripted_effects/013_natural_disasters_effects.txt`. Families prefer meaningful states, such as coasts for cyclones and tsunami, mountain or hill states for mass movement, dense or built-up states for seismic disaster, forest and dry states for firefronts, arid states for dust storms, and ports or islands for coastal systems. The score also values population, built-up states, capitals, low infrastructure, active aftermath, and maximum barrage pressure. Event 13 heat checks for the separate Event 51 heat-wave idea and redirects away from heat if that route is active, so the two systems do not stack.

Warnings are not guaranteed. Drought, heat, winter, cyclone, and similar families have better warning odds than rupture, meteor, landslide, and other sudden families. The warning score also reads country capacity and state conditions, including stability, war state, control, infrastructure, radio capacity, radar, air bases, coastal stations, prior preparation, active aftermath, evolution stage, and maximum Disaster Barrage pressure. A real warning applies the warning modifier and opens preparation decisions. A missed warning leaves the state at baseline preparedness, raises aftermath pressure, blocks no-deaths achievement progress for that sequence, and opens the family category after impact.

Evolution II and III chain controllers use hidden events `chaosx.nr13.40` through `.45`. They handle delayed tsunami warnings and impacts, moving storm corridor ticks, meteor clusters, massive rupture waves, and massive eruption ashfall or lahar follow-ups without creating extra random-event history rows.

Sandstorm gameplay is routed through Event 13. Event 99 is a compatibility bridge into an Event 13 sandstorm sequence when available. Event 28, Event 43, Event 46, Event 47, and separate meteor placeholders are not used as Event 13 logic sources. Event 46 remains inactive and unknown.

## Deaths And Damage

Population loss is always computed per affected state from current state population and a final dynamic loss rate:

```text
current_state_population * final_dynamic_loss_rate
```

The final loss rate is assembled from family base rate, severity, evolution stage, preparedness, density, infrastructure condition, war context, existing aftermath, recovery status, and percentage ceilings. There are no fixed casualty totals, fixed per-state death totals, or absolute death caps in Event 13. Dense states can therefore suffer far larger absolute losses than sparse states under the same final rate, and regional or abnormal chains can produce million-scale deaths when several dense states or failed aftermaths are involved.

Deaths are recorded through the shared deaths system with the Natural Disasters cause id. Event 13 records percentage-based state losses without a fixed absolute victim ceiling, so dense states can suffer much larger absolute losses than sparse states under the same severity. Building damage uses family-specific damage rates against infrastructure, railways, supply hubs, industry, dockyards, naval bases, air bases, forts, radar, anti-air, and resource slots where the family calls for it. State penalties are dynamic modifiers: `natural_disaster_state_disruption`, `natural_disaster_warning_disruption`, and `natural_disaster_aftershock_watch`.

## Decisions And AI

The generic `Natural Disaster Recovery` category is an overview and small incident hub. Serious, regional, catastrophic, abnormal, and scenario-scale hits open the family category that matches the current disaster. Each family category has its own warning action, recovery action, and timed aftermath mission except the famine displacement commission, which focuses on food columns and sheltering displaced people.

Family categories:

- `nd_cat_flood_relief_authority`
- `nd_cat_cyclone_emergency_command`
- `nd_cat_severe_storm_office`
- `nd_cat_hail_damage_board`
- `nd_cat_wind_damage_control`
- `nd_cat_storm_corridor_command`
- `nd_cat_seismic_emergency_authority`
- `nd_cat_great_rupture_command`
- `nd_cat_tsunami_coastal_command`
- `nd_cat_volcanic_crisis_office`
- `nd_cat_massive_eruption_command`
- `nd_cat_firefront_command`
- `nd_cat_drought_famine_office`
- `nd_cat_heat_emergency_office`
- `nd_cat_winter_emergency_directorate`
- `nd_cat_dust_emergency_office`
- `nd_cat_landslide_rescue_office`
- `nd_cat_slope_collapse_response`
- `nd_cat_skyfall_emergency_bureau`
- `nd_cat_meteor_storm_command`
- `nd_cat_famine_displacement_commission`

Costs use equipment, fuel, trains, convoys, command power, army experience, manpower, stability, and war support. Political power is not the recovery store. AI weights favor direct warning and aftermath actions when the country has active disaster flags, higher severity, a capital or core state under pressure, or severe family categories. Recovery missions clear aftermath when completed and add percentage-based follow-up deaths when they time out. Mission success and failure also route through family objective packets, including firebreak containment, aftershock inspections, ashfall clearance, floodwater cleanup, crater cordons, and failure-driven follow-up families.

Category cleanup runs from the shared Event 13 cleanup effects. Categories hide when their matching family warning and aftermath flags are gone. Scenario cleanup also waits for active aftermaths before awarding maximum barrage completion predicates.

## Cluster And Scenario

The Natural Disasters cluster contains multiple Event 13 member slots. Early slots are local, middle slots are regional, and the severe slot forces the abnormal-age context. The cluster detail text lists those conceptual slots rather than treating Event 13 as one generic member.

SCN-007 is `Disaster Barrage`. It is launchable directly from the scenario controls and has no ordinary Chaos or evolution prerequisite. The manual launch is forceable and clears any active Event 13 sequence context before queuing the barrage, while existing aftermath ledgers remain available for recovery. Manual Disaster Barrage uses a hidden state-scoped controller token for scheduler, finish, chain, and delayed tsunami warning deliveries. The token stores the launching country and exact sequence id, so stale delayed manual events self-cancel before they can mutate a newer scenario context. Normal delayed controllers are also held behind a short post-launch flush guard so pre-barrage automatic deliveries cannot wake up after the manual season finishes. The scenario has type controls for random, geological, weather, skyfall, and full catalogue barrages, plus intensity controls through the existing scenario intensity setting. Manual launch starts Event 13 through the same sequence machinery, so population loss, deaths, decisions, aftermaths, news throttling, and cleanup all use the normal system.

News uses the last affected state as context. It requires a scenario-scale sequence, abnormal sequence, severe or extreme final hit, or large recorded civilian death report, then checks the global Event 13 news cooldown and a family-specific cooldown before firing the matching family news item.

## Super-Events

The largest abnormal disasters use the shared super-event radio stack.

- `natural_disasters_start_rupture_wave_chain_from_state` can fire `The Great Rupture` once per campaign.
- `natural_disasters_start_massive_eruption_chain_from_state` can fire `The Mountain Unsealed` once per campaign.
- `natural_disasters_start_meteor_cluster_chain_from_state` can fire `Stones from Heaven` once per campaign.

Delayed follow-up impacts inside those chains do not fire more super-events and do not create extra random-event history rows. The research, quote, image, and audio package is recorded in `docs/super_events/013_natural_disasters_super_event_research.md`.

## Gameplay Surfaces

- Event script: `events/013_natural_disasters.txt`
- Sandstorm bridge: `events/099_desert_storm.txt`
- News events: `events/_chaosx_news.txt`
- Constants: `common/script_constants/013_natural_disasters_constants.txt`
- Triggers: `common/scripted_triggers/013_natural_disasters_triggers.txt`
- Effects: `common/scripted_effects/013_natural_disasters_effects.txt`
- Dynamic modifiers: `common/dynamic_modifiers/013_natural_disasters_dynamic_modifiers.txt`
- Decision categories: `common/decisions/categories/013_natural_disasters_categories.txt`
- Decisions and missions: `common/decisions/013_natural_disasters_decisions.txt`
- Scripted localisation: `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`
- Scripted GUI: `common/scripted_guis/013_natural_disasters_scripted_guis.txt`, `interface/013_natural_disasters.gui`
- Player localisation: `localisation/english/013_natural_disasters_l_english.yml`
- Assets: `interface/013_natural_disasters.gfx`, `gfx/event_pictures/013_natural_disasters/`, `gfx/interface/decisions/natural_disasters/`, `gfx/interface/animated/natural_disasters/`, and `gfx/achievements/`
- Super-event assets: `interface/chaosx_super_events.gfx`, `gfx/super_events/super_event_nd_great_rupture.dds`, `gfx/super_events/super_event_nd_massive_eruption.dds`, `gfx/super_events/super_event_nd_skyfall.dds`, `music/super_event_natural_disasters_*.ogg`, and `sound/chaosx_super_event_natural_disasters_*.wav`
- Shared integration: Chaos Meter deaths cause, event log detail pages, event cluster detail pages, triggerable scenario controls, and achievement localisation.

## Assets

The Event 13 sprite registry is `interface/013_natural_disasters.gfx`. Source, processed, and DDS package records are in `docs/assets/013_natural_disasters/`.

Report and news sprites:

- `GFX_report_event_nd_flood`
- `GFX_report_event_nd_storm`
- `GFX_report_event_nd_earthquake`
- `GFX_report_event_nd_rupture_wave`
- `GFX_report_event_nd_tsunami`
- `GFX_report_event_nd_volcano`
- `GFX_report_event_nd_wildfire`
- `GFX_report_event_nd_drought_famine`
- `GFX_report_event_nd_winter`
- `GFX_report_event_nd_dust_sandstorm`
- `GFX_report_event_nd_landslide`
- `GFX_report_event_nd_skyfall`
- `GFX_report_event_nd_moving_corridor`
- `GFX_report_event_nd_barrage`
- `GFX_news_event_generic_natural_disaster`
- `GFX_news_event_nd_regional_floods`
- `GFX_news_event_nd_great_rupture`
- `GFX_news_event_nd_massive_eruption`
- `GFX_news_event_nd_meteor_showers`

Super-event radio sprites:

- `GFX_super_event_nd_great_rupture`
- `GFX_super_event_nd_massive_eruption`
- `GFX_super_event_nd_skyfall`

Decision category sprites:

These ids include older internal category names where needed for save/script stability. Their localisation and icon art use response boards, authorities, commands, and commissions. The category button icons are non-square `53x40` assets, and the larger left-side category images are separate `114x101` report pictures.

- `GFX_decision_category_nd_recovery_overview`
- `GFX_decision_category_nd_flood`
- `GFX_decision_category_nd_cyclone`
- `GFX_decision_category_nd_severe_storm`
- `GFX_decision_category_nd_hail`
- `GFX_decision_category_nd_wind`
- `GFX_decision_category_nd_corridor`
- `GFX_decision_category_nd_earthquake`
- `GFX_decision_category_nd_rupture`
- `GFX_decision_category_nd_tsunami`
- `GFX_decision_category_nd_volcano`
- `GFX_decision_category_nd_massive_eruption`
- `GFX_decision_category_nd_firefront`
- `GFX_decision_category_nd_drought`
- `GFX_decision_category_nd_heat`
- `GFX_decision_category_nd_winter`
- `GFX_decision_category_nd_dust`
- `GFX_decision_category_nd_landslide`
- `GFX_decision_category_nd_slope`
- `GFX_decision_category_nd_skyfall`
- `GFX_decision_category_nd_meteor_storm`
- `GFX_decision_category_nd_famine`

Decision category picture sprites:

- `GFX_decision_cat_picture_nd_recovery_overview`
- `GFX_decision_cat_picture_nd_flood`
- `GFX_decision_cat_picture_nd_cyclone`
- `GFX_decision_cat_picture_nd_severe_storm`
- `GFX_decision_cat_picture_nd_hail`
- `GFX_decision_cat_picture_nd_wind`
- `GFX_decision_cat_picture_nd_corridor`
- `GFX_decision_cat_picture_nd_earthquake`
- `GFX_decision_cat_picture_nd_rupture`
- `GFX_decision_cat_picture_nd_tsunami`
- `GFX_decision_cat_picture_nd_volcano`
- `GFX_decision_cat_picture_nd_massive_eruption`
- `GFX_decision_cat_picture_nd_firefront`
- `GFX_decision_cat_picture_nd_drought`
- `GFX_decision_cat_picture_nd_heat`
- `GFX_decision_cat_picture_nd_winter`
- `GFX_decision_cat_picture_nd_dust`
- `GFX_decision_cat_picture_nd_landslide`
- `GFX_decision_cat_picture_nd_slope`
- `GFX_decision_cat_picture_nd_skyfall`
- `GFX_decision_cat_picture_nd_meteor_storm`
- `GFX_decision_cat_picture_nd_famine`

Decision sprites:

- `GFX_decision_nd_barrage_launch_controls`
- `GFX_decision_nd_firefighting`
- `GFX_decision_nd_rebuild_ports`
- `GFX_decision_nd_seismology_teams`
- `GFX_decision_nd_meteor_crater_cordon`
- `GFX_decision_nd_clear_debris`
- `GFX_decision_nd_dust_masks`
- `GFX_decision_nd_evacuate_shelter`
- `GFX_decision_nd_field_hospitals`
- `GFX_decision_nd_heat_shelters`
- `GFX_decision_nd_international_relief`
- `GFX_decision_nd_lava_diversion`
- `GFX_decision_nd_repair_rail`
- `GFX_decision_nd_rescue_columns`
- `GFX_decision_nd_restore_supply`
- `GFX_decision_nd_water_rationing`
- `GFX_decision_nd_winter_convoys`

Animated sprites and static fallbacks:

- `GFX_natural_disaster_warning_pulse_animated`, fallback `GFX_natural_disaster_warning_pulse_static`
- `GFX_natural_disaster_tsunami_countdown_animated`, fallback `GFX_natural_disaster_tsunami_countdown_static`
- `GFX_natural_disaster_storm_corridor_track_animated`, fallback `GFX_natural_disaster_storm_corridor_track_static`
- `GFX_natural_disaster_eruption_ashfall_animated`, fallback `GFX_natural_disaster_eruption_ashfall_static`
- `GFX_natural_disaster_skyfall_alarm_animated`, fallback `GFX_natural_disaster_skyfall_alarm_static`

The active decision-category indicator uses these animated sprites through `natural_disasters_decision_indicator_gui`. It selects the warning, tsunami countdown, storm corridor, ashfall, or skyfall sprite from scripted localisation and shows current family, severity, incident count, and reported civilian deaths while the recovery overview is open.

Achievement sprites:

- `GFX_achievement_achievement_nd_prepared_capital`
- `GFX_achievement_achievement_nd_no_deaths_sequence`
- `GFX_achievement_achievement_nd_tame_the_barrage`
- `GFX_achievement_achievement_nd_firebreak_master`
- `GFX_achievement_achievement_nd_aftershock_control`
- `GFX_achievement_achievement_nd_skyfall_survivor`
- `GFX_achievement_achievement_nd_global_relief`
- `GFX_achievement_achievement_nd_no_world_end`

## Achievements

Natural Disasters adds preparedness, no-death sequence, maximum barrage survival, firefront containment, aftershock control, skyfall recovery, global relief, and no world-end achievements. Unlock flags are written by Event 13 warning, impact, recovery, and scenario cleanup effects so achievements follow actual disaster outcomes. The stricter predicates track capital warning and low loss, missed-warning absence, clean recovery, family objective success, crater and aftershock cleanup, relief across family groups, maximum barrage aftermath closure, and abnormal-family resolution without a world-end state.

## Future Plans

- Expand the active decision-category indicator into a full forecast ledger with state cards once the base animation surface has live-session feedback.
- Add relief diplomacy between countries after regional disasters so unaffected allies can commit trains, convoys, field hospitals, or food columns.
- Add route-specific flavour for occupied states and collaboration governments hit by severe disasters.
- Add more family-specific news images so every abnormal family has a direct picture instead of sharing the generic severe-disaster image.
