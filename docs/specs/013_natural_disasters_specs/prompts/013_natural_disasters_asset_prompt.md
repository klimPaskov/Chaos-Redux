# Asset Prompt for Event 013 Natural Disasters

Use `chaos-redux-event-assets` for all visual assets and `chaos-redux-frame-animation` for every animated asset. Inspect the matching reference folders before creating or processing any asset. Use generated assets for fictional or impossible disaster scenes and icons. Use sourced imagery only when the final asset must depict a real historical photograph, real archival material, or a real specific place or object.

All names below are working filenames and sprite suggestions. Keep them stable once registered, but do not treat them as final localisation.

## Required static icon families

Create coordinated icon families for the recovery decision category and major decision groups. Do not derive focus, idea, and decision icons from the same source crop. Each asset type needs its own source art.

Decision category icon:

- `decision_category_013_disaster_response`
- Target type: decision category icon, inspect `assets/decisions`
- Direction: emergency relief emblem with broken rail, rescue cross, storm mark, and construction tools, readable at category size
- Source mode: generated icon

Decision icons, 32x32:

- `decision_013_rescue_operations`
- `decision_013_evacuate_area`
- `decision_013_repair_rail_corridor`
- `decision_013_reopen_port`
- `decision_013_restore_supply_hub`
- `decision_013_food_and_water_relief`
- `decision_013_firebreaks`
- `decision_013_ash_cleanup`
- `decision_013_storm_shelters`
- `decision_013_foreign_disaster_aid`

Idea or national spirit icons, 64x64:

- `idea_013_disaster_aftermath`
- `idea_013_refugee_pressure`
- `idea_013_famine_pressure`
- `idea_013_broken_infrastructure`
- `idea_013_disaster_recovery_mobilization`

These should be compact symbolic icons with transparent unused pixels unless the existing idea pattern requires a painted backdrop.

## Report and news images

Baseline and Evolution I report images should be generated period-documentary images unless implementation chooses real disaster archive imagery for a specific family. Use report-event image rules and the report card processing script.

Working report images, 210x176:

- `report_event_013_earthquake_damage`
- `report_event_013_flooded_city`
- `report_event_013_cyclone_landfall`
- `report_event_013_wildfire_evacuation`
- `report_event_013_blizzard_railway`
- `report_event_013_dust_storm_column`
- `report_event_013_volcanic_ash`
- `report_event_013_tsunami_harbor`

Evolution II digest news images, 397x153 black and white:

- `news_event_013_global_disaster_season`
- `news_event_013_disaster_aftermath_digest`

Use generated period-authentic documentary style unless a sourced image is chosen and documented.

## Super-event images

Super-event images target 457x328. They should use generated dramatic disaster scenes because the Event 013 abnormal disasters are fictional or impossible in their scale.

Required generated super-event image packages:

- `super_event_013_meteor_shower`
- `super_event_013_global_rupture`
- `super_event_013_massive_eruption`
- `super_event_013_storm_corridor`

Avoid modern cinematic color grading, readable text, modern vehicles, modern signs, and UI overlays. The image should fit a WW2-era documentary or high-chaos period visual language while still being clearly abnormal.

## Scripted GUI and animated assets

Evolution III requires a disaster map or category-attached scripted GUI. Use `chaos-redux-frame-animation`. Every animation needs real source frames, a horizontal sheet, a static fallback, manifest entries, and `gfx_handoff.md`.

Animated storm corridor marker:

- Working asset slug: `013_storm_corridor_marker`
- Target surface: disaster map scripted GUI
- Target frame size: implementation should confirm, suggested 64x64 or 96x96
- Frame count: 8 to 12 real frames
- Loop: active rotating or twisting storm form drawn per frame, not a transformed still
- Static fallback: `GFX_013_storm_corridor_marker`
- Animated sprite: `GFX_013_storm_corridor_marker_animated`
- State logic: visible when storm corridor is active

Animated warning pulse:

- Working asset slug: `013_disaster_warning_pulse`
- Target surface: threatened next-state card or map marker
- Target frame size: confirm with GUI, suggested 64x64 or panel-specific frame
- Frame count: 6 to 10 real frames
- Loop: warning light intensity and shape should be drawn per frame
- State logic: visible for predicted next states or delayed tsunami targets

Animated eruption marker:

- Working asset slug: `013_eruption_marker`
- Target surface: active massive eruption map marker
- Target frame size: suggested 64x64
- Frame count: 8 to 12 real frames
- Loop: ash plume and lava glow source-frame sequence
- State logic: visible on massive eruption active states

Animated meteor impact marker:

- Working asset slug: `013_meteor_impact_marker`
- Target surface: active meteor shower impact states
- Target frame size: suggested 64x64
- Frame count: 8 to 12 real frames
- Loop: falling fragments and impact glow sequence
- State logic: visible during meteor shower pulses

Static GUI assets:

- Disaster map background panel.
- Family filter tab icons.
- Active disaster card frame.
- Recovery phase frame.
- Threatened state frame.
- Cleared state frame.
- Digest report icon.

## Achievement icons

Use the achievement prompt for the achievement list. Create completed 64x64 icons first, then grey and not-eligible variants if the achievement system requires them. Final DDS files go directly under `gfx/achievements/` using achievement ids.

## Manifest requirements

Create `docs/assets/013_natural_disasters/manifest.md` and `docs/assets/013_natural_disasters/gfx_handoff.md`. Each entry must include source mode, prompt or source URL, source path, processed PNG path, final DDS path, target size, sprite name, related system, status, and animation metadata when relevant.
