# Event 013 Natural Disasters art manifest

Event id: `013`
Event slug: `natural_disasters`
Source mode summary: generated event art, generated icons, and regenerated frame-animation source art through official `image_gen`
Scope note: this manifest covers Event 13 report, news, decision-category picture, decision icon, decision-category icon, idea icon, and animated scripted-GUI assets.
Prompt record: `docs/assets/013_natural_disasters/prompts/generated_event_art_prompts.md`
Report contact sheet: `docs/assets/013_natural_disasters/contact_sheets/013_natural_disasters_report_contact_sheet.png`
News contact sheet: `docs/assets/013_natural_disasters/contact_sheets/013_natural_disasters_news_contact_sheet.png`
Decision category picture contact sheet: `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_category_pictures_contact.png`
Decision category icon contact sheet: `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_category_icons_contact.png`
Decision icon contact sheet: `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_decision_icons_contact.png`
Idea icon contact sheet: `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_idea_icons_contact.png`
Validation note: `docs/assets/013_natural_disasters/notes/report_news_validation.md`

## Complete

### Super-event radio art and audio

These are 457x328 super-event radio images wired through `interface/chaosx_super_events.gfx`, separate from Event 13 report images, news images, decision category pictures, and decision category button icons.

| Asset | Super-event slot | Source PNG | Processed PNG | Final DDS path | Sprite name | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `super_event_nd_great_rupture` | `67` | `docs/assets/013_natural_disasters/source_png/super_event_nd_great_rupture_source.png` | `docs/assets/013_natural_disasters/processed_png/super_event_nd_great_rupture.png` | `gfx/super_events/013_natural_disasters/super_event_nd_great_rupture.dds` | `GFX_super_event_nd_great_rupture` | `complete` |
| `super_event_nd_massive_eruption` | `68` | `docs/assets/013_natural_disasters/source_png/super_event_nd_massive_eruption_source.png` | `docs/assets/013_natural_disasters/processed_png/super_event_nd_massive_eruption.png` | `gfx/super_events/013_natural_disasters/super_event_nd_massive_eruption.dds` | `GFX_super_event_nd_massive_eruption` | `complete` |
| `super_event_nd_skyfall` | `69` | `docs/assets/013_natural_disasters/source_png/super_event_nd_skyfall_source.png` | `docs/assets/013_natural_disasters/processed_png/super_event_nd_skyfall.png` | `gfx/super_events/013_natural_disasters/super_event_nd_skyfall.dds` | `GFX_super_event_nd_skyfall` | `complete` |
| `super_event_nd_storm_corridor` | `70` | `docs/assets/013_natural_disasters/source_png/super_event_nd_storm_corridor_source.png` | `docs/assets/013_natural_disasters/processed_png/super_event_nd_storm_corridor.png` | `gfx/super_events/013_natural_disasters/super_event_nd_storm_corridor.dds` | `GFX_super_event_nd_storm_corridor` | `complete` |

| Super-event slot | Music file | Sound file | Source handoff | Status |
| --- | --- | --- | --- | --- |
| `67` | `music/super_event_natural_disasters_great_rupture.ogg` | `sound/chaosx_super_event_natural_disasters_great_rupture.wav` | `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-06-29_event013_super_event_audio_handoff.md` | `complete` |
| `68` | `music/super_event_natural_disasters_massive_eruption.ogg` | `sound/chaosx_super_event_natural_disasters_massive_eruption.wav` | `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-06-29_event013_super_event_audio_handoff.md` | `complete` |
| `69` | `music/super_event_natural_disasters_skyfall.ogg` | `sound/chaosx_super_event_natural_disasters_skyfall.wav` | `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-06-29_event013_super_event_audio_handoff.md` | `complete` |
| `70` | `music/super_event_natural_disasters_storm_corridor.ogg` | `sound/chaosx_super_event_natural_disasters_storm_corridor.wav` | `docs/assets/013_natural_disasters/audio_research/processed/event013_moving_storm_corridor_candidate.ogg` | `complete` |

### Decision category picture derivatives

These are the large left-side decision-category pictures. They use generated family-specific disaster scene sources resized to vanilla `114x101` category-picture canvases. The completed source-art pass is documented in `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-01_event013_category_picture_source_art_handoff.md`.

| Asset | Source report | Source PNG | Processed PNG | Final DDS path | Sprite name | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `decision_cat_picture_nd_recovery_overview` | `report_event_nd_barrage` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_recovery_overview_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_recovery_overview.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_recovery_overview.dds` | `GFX_decision_cat_picture_nd_recovery_overview` | `complete` |
| `decision_cat_picture_nd_flood` | `report_event_nd_flood` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_flood_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_flood.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_flood.dds` | `GFX_decision_cat_picture_nd_flood` | `complete` |
| `decision_cat_picture_nd_cyclone` | `report_event_nd_storm` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_cyclone_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_cyclone.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_cyclone.dds` | `GFX_decision_cat_picture_nd_cyclone` | `complete` |
| `decision_cat_picture_nd_severe_storm` | `report_event_nd_storm` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_severe_storm_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_severe_storm.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_severe_storm.dds` | `GFX_decision_cat_picture_nd_severe_storm` | `complete` |
| `decision_cat_picture_nd_hail` | `report_event_nd_storm` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_hail_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_hail.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_hail.dds` | `GFX_decision_cat_picture_nd_hail` | `complete` |
| `decision_cat_picture_nd_wind` | `report_event_nd_storm` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_wind_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_wind.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_wind.dds` | `GFX_decision_cat_picture_nd_wind` | `complete` |
| `decision_cat_picture_nd_corridor` | `report_event_nd_moving_corridor` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_corridor_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_corridor.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_corridor.dds` | `GFX_decision_cat_picture_nd_corridor` | `complete` |
| `decision_cat_picture_nd_earthquake` | `report_event_nd_earthquake` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_earthquake_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_earthquake.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_earthquake.dds` | `GFX_decision_cat_picture_nd_earthquake` | `complete` |
| `decision_cat_picture_nd_rupture` | `report_event_nd_rupture_wave` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_rupture_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_rupture.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_rupture.dds` | `GFX_decision_cat_picture_nd_rupture` | `complete` |
| `decision_cat_picture_nd_tsunami` | `report_event_nd_tsunami` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_tsunami_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_tsunami.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_tsunami.dds` | `GFX_decision_cat_picture_nd_tsunami` | `complete` |
| `decision_cat_picture_nd_volcano` | `report_event_nd_volcano` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_volcano_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_volcano.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_volcano.dds` | `GFX_decision_cat_picture_nd_volcano` | `complete` |
| `decision_cat_picture_nd_massive_eruption` | `report_event_nd_volcano` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_massive_eruption_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_massive_eruption.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_massive_eruption.dds` | `GFX_decision_cat_picture_nd_massive_eruption` | `complete` |
| `decision_cat_picture_nd_firefront` | `report_event_nd_wildfire` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_firefront_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_firefront.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_firefront.dds` | `GFX_decision_cat_picture_nd_firefront` | `complete` |
| `decision_cat_picture_nd_drought` | `report_event_nd_drought_famine` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_drought_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_drought.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_drought.dds` | `GFX_decision_cat_picture_nd_drought` | `complete` |
| `decision_cat_picture_nd_heat` | `report_event_nd_drought_famine` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_heat_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_heat.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_heat.dds` | `GFX_decision_cat_picture_nd_heat` | `complete` |
| `decision_cat_picture_nd_winter` | `report_event_nd_winter` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_winter_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_winter.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_winter.dds` | `GFX_decision_cat_picture_nd_winter` | `complete` |
| `decision_cat_picture_nd_dust` | `report_event_nd_dust_sandstorm` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_dust_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_dust.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_dust.dds` | `GFX_decision_cat_picture_nd_dust` | `complete` |
| `decision_cat_picture_nd_landslide` | `report_event_nd_landslide` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_landslide_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_landslide.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_landslide.dds` | `GFX_decision_cat_picture_nd_landslide` | `complete` |
| `decision_cat_picture_nd_slope` | `report_event_nd_landslide` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_slope_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_slope.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_slope.dds` | `GFX_decision_cat_picture_nd_slope` | `complete` |
| `decision_cat_picture_nd_skyfall` | `report_event_nd_skyfall` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_skyfall_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_skyfall.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_skyfall.dds` | `GFX_decision_cat_picture_nd_skyfall` | `complete` |
| `decision_cat_picture_nd_meteor_storm` | `report_event_nd_skyfall` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_meteor_storm_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_meteor_storm.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_meteor_storm.dds` | `GFX_decision_cat_picture_nd_meteor_storm` | `complete` |
| `decision_cat_picture_nd_famine` | `report_event_nd_drought_famine` | `docs/assets/013_natural_disasters/source_png/decision_cat_picture_nd_famine_source.png` | `docs/assets/013_natural_disasters/processed_png/decision_cat_picture_nd_famine.png` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_famine.dds` | `GFX_decision_cat_picture_nd_famine` | `complete` |

### Decision category icon correction

The `GFX_decision_category_nd_*` category button icons were regenerated and processed into non-square `53x40` DDS canvases. Chroma green was removed before resizing, and the icons remain separate from the `114x101` category pictures.

- Asset count: 22 category button icons
- Live DDS folder: `gfx/interface/decisions/013_natural_disasters/`
- Package DDS folder: `docs/assets/013_natural_disasters/dds/`
- Source PNG folder: `docs/assets/013_natural_disasters/source_png/`
- Processed PNG folder: `docs/assets/013_natural_disasters/processed_png/`
- Contact sheet: `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_category_icons_contact.png`

### Decision icon regeneration

The `GFX_decision_nd_*` response decision icons were regenerated as transparent `32x32` decision-symbol assets rather than resized focus or category art.

- Asset count: 17 decision icons
- Live DDS folder: `gfx/interface/decisions/013_natural_disasters/`
- Package DDS folder: `docs/assets/013_natural_disasters/dds/`
- Source PNG folder: `docs/assets/013_natural_disasters/source_png/`
- Processed PNG folder: `docs/assets/013_natural_disasters/processed_png/`
- Contact sheet: `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_decision_icons_contact.png`
- Handoff: `docs/plans/013_natural_disasters_plans/subagent_handoffs/icon_asset_regeneration_2026_07_01.md`

### Idea icon regeneration

The visible country-level disaster-pressure ideas use dedicated `64x64` national-spirit icons. They do not replace the state dynamic modifiers that carry disaster damage and recovery. The current set was regenerated from fresh official `image_gen` source art as transparent compact spirit silhouettes without circular medallion frames, badge rims, coin borders, opaque square backdrops, or the previous purple alpha/matte.

| Asset | Final DDS path | Sprite name | Status |
| --- | --- | --- | --- |
| `idea_013_disaster_aftermath` | `gfx/interface/ideas/013_natural_disasters/idea_013_disaster_aftermath.dds` | `GFX_idea_013_disaster_aftermath` | `complete` |
| `idea_013_refugee_pressure` | `gfx/interface/ideas/013_natural_disasters/idea_013_refugee_pressure.dds` | `GFX_idea_013_refugee_pressure` | `complete` |
| `idea_013_famine_pressure` | `gfx/interface/ideas/013_natural_disasters/idea_013_famine_pressure.dds` | `GFX_idea_013_famine_pressure` | `complete` |
| `idea_013_broken_infrastructure` | `gfx/interface/ideas/013_natural_disasters/idea_013_broken_infrastructure.dds` | `GFX_idea_013_broken_infrastructure` | `complete` |
| `idea_013_disaster_recovery_mobilization` | `gfx/interface/ideas/013_natural_disasters/idea_013_disaster_recovery_mobilization.dds` | `GFX_idea_013_disaster_recovery_mobilization` | `complete` |

Contact sheet: `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_idea_icons_contact.png`
Validation: processed PNGs, package DDS copies, and live DDS files are `64x64` with alpha, transparent corners, and zero visible green, magenta, or purple key pixels.

### Animated scripted-GUI alpha cleanup

All Event 013 scripted-GUI animation packages were regenerated from per-frame source art with clean transparency. Each package has 8 source frames, 8 processed frames, a `288x36` frame sheet, a `36x36` static fallback, DDS copies under both the package folder and live `gfx/interface/animated/013_natural_disasters/`, a GIF preview, and a contact sheet.

| Asset | Frame sheet | Static fallback | Handoff |
| --- | --- | --- | --- |
| `natural_disaster_warning_pulse` | `gfx/interface/animated/013_natural_disasters/natural_disaster_warning_pulse_sheet.dds` | `gfx/interface/animated/013_natural_disasters/natural_disaster_warning_pulse_static.dds` | `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-01_event013_animation_alpha_cleanup_handoff.md` |
| `natural_disaster_storm_corridor_track` | `gfx/interface/animated/013_natural_disasters/natural_disaster_storm_corridor_track_sheet.dds` | `gfx/interface/animated/013_natural_disasters/natural_disaster_storm_corridor_track_static.dds` | `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-01_event013_animation_alpha_cleanup_handoff.md` |
| `natural_disaster_tsunami_countdown` | `gfx/interface/animated/013_natural_disasters/natural_disaster_tsunami_countdown_sheet.dds` | `gfx/interface/animated/013_natural_disasters/natural_disaster_tsunami_countdown_static.dds` | `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-01_event013_animation_alpha_cleanup_handoff.md` |
| `natural_disaster_eruption_ashfall` | `gfx/interface/animated/013_natural_disasters/natural_disaster_eruption_ashfall_sheet.dds` | `gfx/interface/animated/013_natural_disasters/natural_disaster_eruption_ashfall_static.dds` | `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-01_event013_animation_alpha_cleanup_handoff.md` |
| `natural_disaster_skyfall_alarm` | `gfx/interface/animated/013_natural_disasters/natural_disaster_skyfall_alarm_sheet.dds` | `gfx/interface/animated/013_natural_disasters/natural_disaster_skyfall_alarm_static.dds` | `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-01_event013_animation_alpha_cleanup_handoff.md` |

### `report_event_nd_flood`

- Asset type: report event image
- Intended in-game use: reusable local or regional flood report
- Source mode: generated
- Source note: Event 13 needs a reusable period-documentary flood family image rather than one real historical flood photo
- Era-fit note: WW2-era rail, clothing, carts, and townscape were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_nd_flood_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_nd_flood.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_flood.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/report_event_nd_flood.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_nd_flood`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 flood family
- Notes: report-card treatment applied locally
- Asset status: `complete`

### `report_event_nd_storm`

- Asset type: report event image
- Intended in-game use: reusable storm or thunderstorm outbreak report
- Source mode: generated
- Source note: generated to preserve a distinct damaged-airfield storm identity
- Era-fit note: period aircraft and telegraph infrastructure were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_nd_storm_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_nd_storm.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_storm.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/report_event_nd_storm.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_nd_storm`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 storm family
- Notes: report-card treatment applied locally
- Asset status: `complete`

### `report_event_nd_earthquake`

- Asset type: report event image
- Intended in-game use: reusable earthquake report
- Source mode: generated
- Source note: generated to stage inspectable masonry collapse without tying the image to one real archive city
- Era-fit note: period clothing, rubble, and street geometry were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_nd_earthquake_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_nd_earthquake.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_earthquake.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/report_event_nd_earthquake.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_nd_earthquake`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 earthquake family
- Notes: report-card treatment applied locally
- Asset status: `complete`

### `report_event_nd_drought_famine`

- Asset type: report event image
- Intended in-game use: reusable drought and famine pressure report
- Source mode: generated
- Source note: generated to show shortage, relief queues, and cracked irrigation without relying on one specific archival famine photo
- Era-fit note: period square, ox cart, barrels, and clothing were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_nd_drought_famine_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_nd_drought_famine.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_drought_famine.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/report_event_nd_drought_famine.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_nd_drought_famine`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 drought family
- Notes: report-card treatment applied locally
- Asset status: `complete`

### `report_event_nd_wildfire`

- Asset type: report event image
- Intended in-game use: reusable wildfire report
- Source mode: generated
- Source note: generated to keep firebreak operations and evacuation readable at report scale
- Era-fit note: period rail line, carts, and firefighting crews were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_nd_wildfire_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_nd_wildfire.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_wildfire.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/report_event_nd_wildfire.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_nd_wildfire`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 wildfire family
- Notes: report-card treatment applied locally
- Asset status: `complete`

### `report_event_nd_winter`

- Asset type: report event image
- Intended in-game use: reusable winter disaster report
- Source mode: generated
- Source note: generated to center the snowbound rail rescue subject
- Era-fit note: period locomotive, coats, sleds, and signals were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_nd_winter_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_nd_winter.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_winter.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/report_event_nd_winter.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_nd_winter`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 winter family
- Notes: report-card treatment applied locally
- Asset status: `complete`

### `report_event_nd_dust_sandstorm`

- Asset type: report event image
- Intended in-game use: reusable dust or sandstorm report
- Source mode: generated
- Source note: generated to stage the dust wall and airfield/convoy disruption cleanly
- Era-fit note: period trucks, aircraft, and protective clothing were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_nd_dust_sandstorm_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_nd_dust_sandstorm.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_dust_sandstorm.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/report_event_nd_dust_sandstorm.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_nd_dust_sandstorm`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 dust and sandstorm family
- Notes: report-card treatment applied locally
- Asset status: `complete`

### `report_event_nd_volcano`

- Asset type: report event image
- Intended in-game use: reusable volcanic eruption or ashfall report
- Source mode: generated
- Source note: generated to keep the ash-covered rail town distinct from general storm or fire scenes
- Era-fit note: period town, rail line, ash cleanup crews, and street scale were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_nd_volcano_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_nd_volcano.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_volcano.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/report_event_nd_volcano.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_nd_volcano`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 volcano family
- Notes: report-card treatment applied locally
- Asset status: `complete`

### `report_event_nd_landslide`

- Asset type: report event image
- Intended in-game use: reusable landslide report
- Source mode: generated
- Source note: generated to focus on a buried pass and tunnel rather than a generic rubble pile
- Era-fit note: mountain rail engineering scene was explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_nd_landslide_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_nd_landslide.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_landslide.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/report_event_nd_landslide.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_nd_landslide`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 landslide family
- Notes: report-card treatment applied locally
- Asset status: `complete`

### `report_event_nd_skyfall`

- Asset type: report event image
- Intended in-game use: reusable skyfall report
- Source mode: generated
- Source note: generated because Event 13 skyfall is fictional and should not be tied to a real meteor archive image
- Era-fit note: period rail, telegraph poles, soldiers, and observers were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_nd_skyfall_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_nd_skyfall.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_skyfall.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/report_event_nd_skyfall.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_nd_skyfall`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 skyfall family
- Notes: report-card treatment applied locally
- Asset status: `complete`

### `report_event_nd_tsunami`

- Asset type: report event image
- Intended in-game use: reusable tsunami report
- Source mode: generated
- Source note: generated to stage harbor destruction with a clear thrown-boat silhouette
- Era-fit note: period harbor district, rescue crews, and quay damage were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_nd_tsunami_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_nd_tsunami.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_tsunami.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/report_event_nd_tsunami.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_nd_tsunami`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 tsunami family
- Notes: report-card treatment applied locally
- Asset status: `complete`

### `report_event_nd_moving_corridor`

- Asset type: report event image
- Intended in-game use: reusable moving corridor report
- Source mode: generated
- Source note: generated because the corridor scene is alternate-history and needed a strong path-reading composition
- Era-fit note: period embankment, freight cars, and observers were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_nd_moving_corridor_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_nd_moving_corridor.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_moving_corridor.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/report_event_nd_moving_corridor.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_nd_moving_corridor`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 moving corridor family
- Notes: report-card treatment applied locally
- Asset status: `complete`

### `report_event_nd_rupture_wave`

- Asset type: report event image
- Intended in-game use: reusable rupture-wave report
- Source mode: generated
- Source note: generated because the great-rupture regional wave is fictionalized and needs a basin-scale crack scene
- Era-fit note: period rail, bridges, and engineering crews were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_nd_rupture_wave_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_nd_rupture_wave.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_rupture_wave.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/report_event_nd_rupture_wave.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_nd_rupture_wave`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 rupture-wave family
- Notes: report-card treatment applied locally
- Asset status: `complete`

### `report_event_nd_barrage`

- Asset type: report event image
- Intended in-game use: reusable disaster barrage report
- Source mode: generated
- Source note: generated to depict stacked hazards in one readable regional relief scene
- Era-fit note: period rail junction, trucks, and relief workers were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_nd_barrage_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_nd_barrage.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_barrage.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/report_event_nd_barrage.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_nd_barrage`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 manual barrage and high-chaos barrage family
- Notes: report-card treatment applied locally
- Asset status: `complete`

### `news_event_nd_regional_floods`

Family-specific meaningful-hit news events reuse the report-event picture set for their matching disaster groups. The dedicated news images in this section remain assigned to abnormal broadcasts and the SCN-007 barrage.

- Asset type: news event image
- Intended in-game use: throttled regional flood broadcast
- Source mode: generated
- Source note: generated because the image needed a broad basin crisis composition rather than one real newspaper photo
- Era-fit note: WW2-era bridge, boats, crowding, and embankment details were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/news_event_nd_regional_floods_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/news_event_nd_regional_floods.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/news_event_nd_regional_floods.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/news_event_nd_regional_floods.dds`
- Target size: `397x153`
- Sprite name: `GFX_news_event_nd_regional_floods`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 regional floods news
- Notes: processed to black-and-white press-photo treatment
- Asset status: `complete`

### `news_event_nd_great_rupture`

- Asset type: news event image
- Intended in-game use: throttled great-rupture broadcast
- Source mode: generated
- Source note: generated because the Event 13 great rupture is an alternate-history disaster family rather than a single historical earthquake photo
- Era-fit note: WW2-era soldiers, engineers, river crossing, and rail damage were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/news_event_nd_great_rupture_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/news_event_nd_great_rupture.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/news_event_nd_great_rupture.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/news_event_nd_great_rupture.dds`
- Target size: `397x153`
- Sprite name: `GFX_news_event_nd_great_rupture`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 great rupture news
- Notes: processed to black-and-white press-photo treatment
- Asset status: `complete`

### `news_event_nd_meteor_showers`

- Asset type: news event image
- Intended in-game use: throttled meteor-shower broadcast
- Source mode: generated
- Source note: generated because Event 13 meteor showers are fictionalized and need a controlled period-news scene
- Era-fit note: period skyline, anti-air silhouettes, rail yard, and observers were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/news_event_nd_meteor_showers_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/news_event_nd_meteor_showers.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/news_event_nd_meteor_showers.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/news_event_nd_meteor_showers.dds`
- Target size: `397x153`
- Sprite name: `GFX_news_event_nd_meteor_showers`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 meteor-shower news
- Notes: processed to black-and-white press-photo treatment
- Asset status: `complete`

### `news_event_nd_massive_eruption`

- Asset type: news event image
- Intended in-game use: throttled massive-eruption broadcast
- Source mode: generated
- Source note: generated to stage a basin-wide plume and harbor evacuation without tying the image to one archive volcano
- Era-fit note: period harbor, ships, rooftops, and ash plume were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/news_event_nd_massive_eruption_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/news_event_nd_massive_eruption.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/news_event_nd_massive_eruption.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/news_event_nd_massive_eruption.dds`
- Target size: `397x153`
- Sprite name: `GFX_news_event_nd_massive_eruption`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 massive eruption news
- Notes: processed to black-and-white press-photo treatment
- Asset status: `complete`

### `news_event_nd_disaster_barrage`

- Asset type: news event image
- Intended in-game use: throttled disaster-barrage broadcast
- Source mode: generated
- Source note: generated because the barrage is a composite Event 13 escalation scene rather than one archival moment
- Era-fit note: period rail junction, relief teams, floodwater, smoke, and debris were explicitly prompted
- Source PNG: `docs/assets/013_natural_disasters/source_png/news_event_nd_disaster_barrage_source.png`
- Processed PNG: `docs/assets/013_natural_disasters/processed_png/news_event_nd_disaster_barrage.png`
- Final DDS path: `gfx/event_pictures/013_natural_disasters/news_event_nd_disaster_barrage.dds`
- Package DDS path: `docs/assets/013_natural_disasters/dds/news_event_nd_disaster_barrage.dds`
- Target size: `397x153`
- Sprite name: `GFX_news_event_nd_disaster_barrage`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: Event 13 disaster barrage news
- Notes: processed to black-and-white press-photo treatment
- Asset status: `complete`
