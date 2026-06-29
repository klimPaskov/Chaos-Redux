
# Asset prompt for Event 013 Natural Disasters

Use `chaos-redux-event-assets` for all static assets. Use `chaos-redux-frame-animation` for animated assets. Split actual production through the proper asset subagents.

- Use `chaosx_icon_artist` for decision icons, decision category icons, idea icons, achievement icons, and scripted GUI small symbols.
- Use `chaosx_generated_event_art` for generated fictional or period-documentary disaster report, news, super-event, and GUI art.
- Use `chaosx_asset_source_researcher` only if the implementation deliberately wants a real archival disaster image, real historical symbol, or sourced visual reference.

Inspect the relevant reference folders before producing any asset.

- Ideas: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/ideas`
- News event images: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- Report event images: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- Super-event images: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/super_event_images`
- Decisions: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/decisions`
- Achievements: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/achievements`

All asset names below are stable working filenames and sprite directions, not final localisation.

## Decision category and decision icons

Target sizes follow the asset skill. Decision icons are 32 by 32. Idea and national spirit icons are 64 by 64. Decision category icon size should follow the existing category pattern.

| Asset slug | Type | Source mode | Use | Visual direction |
| --- | --- | --- | --- | --- |
| decision_category_natural_disaster_recovery | Decision category icon | Generated icon | Natural Disaster Recovery category. | Recovery overview emblem with storm, cracked ground, and rescue mark. No text. |
| decision_evacuate_disaster_zone | Decision icon | Generated icon | Evacuation decision. | Train and shelter silhouette, readable at small size. |
| decision_rescue_engineers | Decision icon | Generated icon | Rescue engineers. | Helmet, bridge, wrench, or rescue beam. |
| decision_open_relief_corridor | Decision icon | Generated icon | Foreign relief. | Convoy or train corridor with aid crate. |
| decision_flood_barriers | Decision icon | Generated icon | Flood defenses. | Sandbags and waterline. |
| decision_firebreaks | Decision icon | Generated icon | Wildfire containment. | Firebreak line and axe or shovel. |
| decision_airfield_dispersal | Decision icon | Generated icon | Hail, wind, ash, dust, and airfield warning. | Aircraft under shelter or hangar dispersal. |
| decision_close_port | Decision icon | Generated icon | Coastal and cyclone preparation. | Port crane and warning wave. |
| decision_water_rationing | Decision icon | Generated icon | Drought and heat response. | Water canteen and ration mark. |
| decision_ash_dust_clearance | Decision icon | Generated icon | Ash, sandstorm, smoke, meteor dust cleanup. | Masked worker and ash shovel. |
| decision_aftershock_inspection | Decision icon | Generated icon | Earthquake follow-up prevention. | Cracked bridge with inspection lamp. |
| decision_shelter_displaced | Decision icon | Generated icon | Refugee and shelter pressure. | Tents and family silhouette. |
| decision_abnormal_corridor_survey | Decision icon | Generated icon | Evolution III tracking. | Weather radar or telescope with map arc. |

## Idea and state modifier icons

| Asset slug | Type | Source mode | Use | Visual direction |
| --- | --- | --- | --- | --- |
| idea_disaster_transport_damage | State modifier icon | Generated icon | Damaged rail, roads, bridges. | Broken rail and cracked road. |
| idea_disaster_population_pressure | State modifier icon | Generated icon | Rescue overload and displaced population. | Shelter crowd with warning mark. |
| idea_disaster_drought_stress | State modifier icon | Generated icon | Drought and water stress. | Dry field, cracked soil, water canteen. |
| idea_disaster_coastal_inundation | State modifier icon | Generated icon | Tsunami, storm surge, port flooding. | Wave over port silhouette. |
| idea_disaster_ashfall | State modifier icon | Generated icon | Ash, dust, smoke. | Dark cloud over town and airfield. |
| idea_disaster_fire_front | State modifier icon | Generated icon | Wildfire spread. | Fire line over trees or hills. |
| idea_disaster_crater_fields | State modifier icon | Generated icon | Meteor aftermath. | Crater and rail damage. |
| idea_disaster_refugee_pressure | State modifier icon | Generated icon | Displaced people and shelter strain. | Tents and route marker. |
| idea_disaster_recovery_overview | National spirit or category icon | Generated icon | Country-level recovery overview if used. | Ledger, radio, rescue helmet, and map. |

## Report event images

Report images are 210 by 176 and should use report-card processing. Use generated period-documentary scenes unless the implementation asks for real archival imagery. Do not use modern disaster photographs unless sourced and approved.

| Asset slug | Source mode | Use | Scene direction |
| --- | --- | --- | --- |
| report_event_disaster_flood | Generated report image | Local flood or regional flood report. | 1930s or 1940s black and white documentary scene of flooded rail or town, no readable text. |
| report_event_disaster_earthquake | Generated report image | Earthquake and aftershock report. | Rubble, cracked road, rescue workers, period clothing. |
| report_event_disaster_cyclone | Generated report image | Cyclone or coastal storm. | Damaged port or coastal town after storm. |
| report_event_disaster_wildfire | Generated report image | Wildfire or firebreak report. | Fire line near rural settlement, emergency crews. |
| report_event_disaster_drought | Generated report image | Drought and water rationing. | Dry field, empty canal, ration queue, period style. |
| report_event_disaster_blizzard | Generated report image | Blizzard or cold wave. | Snowbound rail or town, rescue party. |
| report_event_disaster_sandstorm | Generated report image | Sandstorm or dust storm. | Desert road or airfield under dust cloud, period vehicles. |
| report_event_disaster_volcano | Generated report image | Volcanic eruption or ashfall. | Ash-covered town or rail line under volcanic plume. |
| report_event_disaster_tsunami | Generated report image | Tsunami or coastal wave aftermath. | Damaged harbor and flooded streets, no modern props. |
| report_event_disaster_meteor | Generated report image | Meteor shower or crater aftermath. | Cratered field, damaged rail, observers and soldiers, high-chaos but period-authentic. |

## News images

News images are 397 by 153 and black and white.

| Asset slug | Source mode | Use | Scene direction |
| --- | --- | --- | --- |
| news_event_regional_disaster_system | Generated news image | First Evolution II regional system. | Broad disaster response scene with rail, refugees, and emergency crews. |
| news_event_abnormal_disaster_age | Generated news image | First Evolution III abnormal disaster season. | Dramatic but period-authentic scene of sky impacts or storm corridor over city. No generated text. |
| news_event_massive_volcano | Generated news image | Massive volcano news gate. | Large ash plume over settlement or port, black and white. |
| news_event_moving_storm_corridor | Generated news image | Moving storm corridor news. | Storm wall over plains or city outskirts, period documentary look. |
| news_event_tsunami_basin_warning | Generated news image | Major tsunami warning. | Coastal evacuation, port closure, and signal station. |

## Super-event image

Only needed if the implementation uses the optional non-terminal Evolution III super-event.

| Asset slug | Source mode | Use | Scene direction |
| --- | --- | --- | --- |
| super_event_abnormal_disaster_age | Generated super-event image | First true abnormal disaster season. | Strong central composition of a 1930s to 1940s city, port, or observatory under unnatural skyfall and storm pressure. It must feel like a hostile natural era, not a world-end title card. No readable text. |

## Scripted GUI static assets

| Asset slug | Type | Source mode | Target direction |
| --- | --- | --- | --- |
| disaster_operations_map_panel | GUI panel | Generated or UI art | Period map desk with disaster pins, no readable text. |
| disaster_state_card_warning | GUI card | UI art | Warning state card frame. |
| disaster_state_card_impact | GUI card | UI art | Impact state card frame. |
| disaster_state_card_recovery | GUI card | UI art | Recovery state card frame. |
| disaster_map_marker_warning | GUI marker | Generated icon | Small hazard marker. |
| disaster_map_marker_impact | GUI marker | Generated icon | Small impact marker. |
| disaster_map_marker_recovery | GUI marker | Generated icon | Small recovery marker. |
| disaster_map_marker_abnormal | GUI marker | Generated icon | High-chaos abnormal marker. |

## Animated GUI assets

Use `chaos-redux-frame-animation`. Each animated asset needs source frames, processed frames, horizontal sheet PNG, sheet DDS, static fallback DDS, preview GIF, manifest entry, and `gfx_handoff.md`.

| Asset slug | Target surface | Frame direction | State logic | Static fallback |
| --- | --- | --- | --- | --- |
| disaster_warning_pulse | Map marker and state card. | 6 to 8 frame pulse loop. | Active warning and impact pending. | disaster_map_marker_warning |
| disaster_impact_flash | Map marker. | 6 frame non-looping flash or short loop. | New impact in recent update. | disaster_map_marker_impact |
| disaster_recovery_shimmer | Recovery board. | 8 frame subtle progress shimmer. | Active recovery mission. | static progress frame. |
| disaster_flood_waterline | Flood and tsunami cards. | 8 frame waterline motion. | Flood or coastal danger active. | static waterline marker. |
| disaster_fire_front_loop | Fire cards. | 8 frame fire and smoke loop. | Fire spread risk active. | static fire marker. |
| disaster_ash_plume_loop | Ash, dust, smoke. | 8 to 10 frame plume drift. | Ash or dust active. | static ash marker. |
| disaster_storm_corridor_loop | Evolution III map. | 8 to 12 frame moving storm icon. | Moving storm current state and next forecast. | static corridor marker. |
| disaster_meteor_track_loop | Evolution III map. | 8 to 12 frame meteor streaks. | Meteor shower warning or impact. | static skyfall marker. |
| disaster_tsunami_wave_loop | Tsunami basin warning. | 8 frame wave band. | Delayed tsunami is scheduled. | static wave marker. |
| disaster_volcanic_spot_loop | Volcano map. | 8 to 10 frame plume or glow. | Active eruption. | static volcano marker. |

## Achievement icons

Create completed 64 by 64 icons first. Grey and not-eligible variants can be derived later if the achievement system needs them.

| Working achievement key | Icon direction |
| --- | --- |
| achievement_nd_prepared_capital | Capital skyline protected by shelter and warning siren. |
| achievement_nd_no_deaths_sequence | Rescue emblem over protected crowd. |
| achievement_nd_tame_the_barrage | Disaster map with many markers crossed by recovery lines. |
| achievement_nd_firebreak_master | Fire line stopped at a rail or river. |
| achievement_nd_aftershock_control | Cracked bridge reinforced by engineers. |
| achievement_nd_skyfall_survivor | Meteor streaks over intact capital shelter. |
| achievement_nd_global_relief | Relief train and convoy crossing map. |
| achievement_nd_no_world_end | Chaos meter or globe held below a disaster sky. |

## Manifest requirements

The asset manifest must list source mode, source prompt or URL, source path, processed PNG path, final DDS path, target size, sprite name, suggested `.gfx` file, related event or decision id, animation frame count when relevant, static fallback path when relevant, and status.

Do not wire assets in the asset subagent. The main implementation agent owns `.gfx`, `.gui`, localisation, event, decision, and scripted GUI references.


## V3 big disaster category asset expansion

The asset pass must no longer treat the recovery interface as one generic overview. Big disaster categories need their own category icon, category picture, or header motif, with static and animated variants where the UI state benefits from motion.

Required category icon or header motifs:

- Flood Relief Authority: broken levee, rescue boat, flooded rail.
- Cyclone Emergency Command: storm spiral, port light, evacuation route.
- Severe Storm Response Board: lightning over airfield or rail yard.
- Storm Corridor Command: animated moving storm marker and forecast path.
- Seismic Emergency Authority: cracked bridge, rescue lamp, rubble.
- Great Rupture Command: animated seismic wave and cracked region marker.
- Tsunami Coastal Command: wave over harbor and high ground marker.
- Volcanic Crisis Board: ash cloud, lahar valley, volcano silhouette.
- Massive Eruption Command: animated ash cloud and eruption pulse.
- Firefront Command: fire line, smoke, rail bridge.
- Drought and Famine Board: cracked reservoir, grain ration, dry field.
- Heat Emergency Board: heat shelter, water reserve, grid strain.
- Winter Emergency Directorate: frozen rail switch, fuel reserve, shelter.
- Dust Emergency Board: dust wall over airfield, filter mask, well marker.
- Landslide Rescue Board: buried rail pass, unstable slope.
- Slope Collapse Response: mine collapse, rockfall tunnel.
- Skyfall Emergency Bureau: meteor streak, shelter, cratered rail.
- Meteor Storm Command: crater cluster, national shelter, airspace closure.
- Famine and Displacement Commission: relief corridor, ration depot, shelter line.

Every animated map marker must follow `chaos-redux-frame-animation` with real source frames, a static fallback, frame sheet DDS, preview GIF for review only, manifest entry, and gfx handoff. Do not make transform only pulses or recolour loops as final animation.
