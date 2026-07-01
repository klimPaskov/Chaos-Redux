# Event 013 Natural Disasters art handoff

Active `.gfx` file: `interface/013_natural_disasters.gfx`

All sprite names below are wired through Event 13 gameplay files.

## Super-event radio images

These use the shared super-event radio frame and are wired through `interface/chaosx_super_events.gfx`, not `interface/013_natural_disasters.gfx`.

- `GFX_super_event_nd_great_rupture`
  - Final DDS path: `gfx/super_events/013_natural_disasters/super_event_nd_great_rupture.dds`
  - Package DDS path: `docs/assets/013_natural_disasters/dds/super_event_nd_great_rupture.dds`
  - Super-event slot: `67`
  - Use notes: fault split, broken rail, collapsed crossing, and dense urban damage fit the abnormal great-rupture chain.
- `GFX_super_event_nd_massive_eruption`
  - Final DDS path: `gfx/super_events/013_natural_disasters/super_event_nd_massive_eruption.dds`
  - Package DDS path: `docs/assets/013_natural_disasters/dds/super_event_nd_massive_eruption.dds`
  - Super-event slot: `68`
  - Use notes: ash plume, airfield closure, port disruption, and evacuee movement fit the abnormal massive eruption chain.
- `GFX_super_event_nd_skyfall`
  - Final DDS path: `gfx/super_events/013_natural_disasters/super_event_nd_skyfall.dds`
  - Package DDS path: `docs/assets/013_natural_disasters/dds/super_event_nd_skyfall.dds`
  - Super-event slot: `69`
  - Use notes: meteor streaks, crater field, rail yard, observatory, and urban fires fit the abnormal meteor cluster chain.
- `GFX_super_event_nd_storm_corridor`
  - Final DDS path: `gfx/super_events/013_natural_disasters/super_event_nd_storm_corridor.dds`
  - Package DDS path: `docs/assets/013_natural_disasters/dds/super_event_nd_storm_corridor.dds`
  - Super-event slot: `70`
  - Use notes: mapped storm front, damaged rail corridor, and period response crews support the moving-path hazard reveal.

## Report event pictures

- `report_event_nd_flood`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_flood.dds`
  - Proposed sprite name: `GFX_report_event_nd_flood`
  - Use notes: flooded rail and street composition reads clearly at report size.
- `report_event_nd_storm`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_storm.dds`
  - Proposed sprite name: `GFX_report_event_nd_storm`
  - Use notes: airfield and rail debris makes this distinct from flood and barrage images.
- `report_event_nd_earthquake`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_earthquake.dds`
  - Proposed sprite name: `GFX_report_event_nd_earthquake`
  - Use notes: collapsed masonry and rescue line stay readable after the report-card tilt.
- `report_event_nd_drought_famine`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_drought_famine.dds`
  - Proposed sprite name: `GFX_report_event_nd_drought_famine`
  - Use notes: relief queue and dry canal emphasize shortage rather than a generic rural scene.
- `report_event_nd_wildfire`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_wildfire.dds`
  - Proposed sprite name: `GFX_report_event_nd_wildfire`
  - Use notes: smoke wall and firebreak crews remain legible at small size.
- `report_event_nd_winter`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_winter.dds`
  - Proposed sprite name: `GFX_report_event_nd_winter`
  - Use notes: snowbound locomotive gives an immediate winter-disaster read.
- `report_event_nd_dust_sandstorm`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_dust_sandstorm.dds`
  - Proposed sprite name: `GFX_report_event_nd_dust_sandstorm`
  - Use notes: dust wall and covered convoy separate this from the ordinary storm family.
- `report_event_nd_volcano`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_volcano.dds`
  - Proposed sprite name: `GFX_report_event_nd_volcano`
  - Use notes: ash plume and rail town silhouette carry the family.
- `report_event_nd_landslide`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_landslide.dds`
  - Proposed sprite name: `GFX_report_event_nd_landslide`
  - Use notes: buried tunnel mouth is the key subject.
- `report_event_nd_skyfall`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_skyfall.dds`
  - Proposed sprite name: `GFX_report_event_nd_skyfall`
  - Use notes: crater and onlookers keep the meteor family grounded and non-terminal.
- `report_event_nd_tsunami`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_tsunami.dds`
  - Proposed sprite name: `GFX_report_event_nd_tsunami`
  - Use notes: boat thrown ashore gives a fast tsunami read.
- `report_event_nd_moving_corridor`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_moving_corridor.dds`
  - Proposed sprite name: `GFX_report_event_nd_moving_corridor`
  - Use notes: advancing wall cloud and wrecked rail line suggest path movement.
- `report_event_nd_rupture_wave`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_rupture_wave.dds`
  - Proposed sprite name: `GFX_report_event_nd_rupture_wave`
  - Use notes: regional crack and bridge failures fit the great-rupture family.
- `report_event_nd_barrage`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/report_event_nd_barrage.dds`
  - Proposed sprite name: `GFX_report_event_nd_barrage`
  - Use notes: combined flood, fire, and logistics collapse composition is the strongest reusable barrage card.

## News event pictures

Meaningful individual-hit news events `chaosx.nr13.305` through `chaosx.nr13.317` reuse the existing `GFX_report_event_nd_*` disaster-family sprites so the broadcast image follows the family that struck. The dedicated `GFX_news_event_nd_*` sprites remain for abnormal broadcasts and the SCN-007 barrage.

- `news_event_nd_regional_floods`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/news_event_nd_regional_floods.dds`
  - Proposed sprite name: `GFX_news_event_nd_regional_floods`
  - Use notes: wide bridge and basin rescue activity fit throttled regional broadcast use.
- `news_event_nd_great_rupture`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/news_event_nd_great_rupture.dds`
  - Proposed sprite name: `GFX_news_event_nd_great_rupture`
  - Use notes: long rupture line and collapsed crossing read immediately at news width.
- `news_event_nd_meteor_showers`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/news_event_nd_meteor_showers.dds`
  - Proposed sprite name: `GFX_news_event_nd_meteor_showers`
  - Use notes: sky streaks are visible without turning the scene into a world-end tableau.
- `news_event_nd_massive_eruption`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/news_event_nd_massive_eruption.dds`
  - Proposed sprite name: `GFX_news_event_nd_massive_eruption`
  - Use notes: basin-wide ash plume gives this the strongest broadcast silhouette.
- `news_event_nd_disaster_barrage`
  - Final DDS path: `gfx/event_pictures/013_natural_disasters/news_event_nd_disaster_barrage.dds`
  - Proposed sprite name: `GFX_news_event_nd_disaster_barrage`
  - Use notes: crowded junction and stacked hazards make this the right capstone news image.

## Decision category pictures

These are the large left-side decision-category pictures. They are not decision icons. They use generated family-specific disaster scene sources resized to vanilla `114x101` category-picture canvases. Source-art completion is documented in `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-01_event013_category_picture_source_art_handoff.md`.

`natural_disaster_response_recovery_overview` keeps `GFX_decision_cat_picture_nd_recovery_overview` as its static category picture. `interface/013_natural_disasters.gui` also overlays the same picture family through scripted GUI elements named `natural_disaster_category_picture_*`, so the left side of the category reflects the most recent open disaster family without changing the static decision-category definition.

| Sprite | Final DDS path |
| --- | --- |
| `GFX_decision_cat_picture_nd_recovery_overview` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_recovery_overview.dds` |
| `GFX_decision_cat_picture_nd_flood` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_flood.dds` |
| `GFX_decision_cat_picture_nd_cyclone` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_cyclone.dds` |
| `GFX_decision_cat_picture_nd_severe_storm` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_severe_storm.dds` |
| `GFX_decision_cat_picture_nd_hail` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_hail.dds` |
| `GFX_decision_cat_picture_nd_wind` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_wind.dds` |
| `GFX_decision_cat_picture_nd_corridor` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_corridor.dds` |
| `GFX_decision_cat_picture_nd_earthquake` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_earthquake.dds` |
| `GFX_decision_cat_picture_nd_rupture` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_rupture.dds` |
| `GFX_decision_cat_picture_nd_tsunami` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_tsunami.dds` |
| `GFX_decision_cat_picture_nd_volcano` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_volcano.dds` |
| `GFX_decision_cat_picture_nd_massive_eruption` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_massive_eruption.dds` |
| `GFX_decision_cat_picture_nd_firefront` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_firefront.dds` |
| `GFX_decision_cat_picture_nd_drought` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_drought.dds` |
| `GFX_decision_cat_picture_nd_heat` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_heat.dds` |
| `GFX_decision_cat_picture_nd_winter` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_winter.dds` |
| `GFX_decision_cat_picture_nd_dust` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_dust.dds` |
| `GFX_decision_cat_picture_nd_landslide` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_landslide.dds` |
| `GFX_decision_cat_picture_nd_slope` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_slope.dds` |
| `GFX_decision_cat_picture_nd_skyfall` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_skyfall.dds` |
| `GFX_decision_cat_picture_nd_meteor_storm` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_meteor_storm.dds` |
| `GFX_decision_cat_picture_nd_famine` | `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_famine.dds` |

## Decision category icons

The `GFX_decision_category_nd_*` sprites remain category button icons. Their final canvases are non-square `53x40` DDS files, separate from the `114x101` category pictures above.

## Idea icons

These sprites back the country-level natural-disaster pressure ideas. The ideas are visible national-pressure summaries; per-state dynamic modifiers remain the primary disaster damage and recovery mechanic.

The current DDS files were regenerated from fresh official `image_gen` source art as compact transparent national-spirit silhouettes without circular medallion frames, badge rims, coin borders, opaque square backdrops, or the previous purple alpha/matte. Sprite names and paths remain unchanged.

| Sprite | Final DDS path |
| --- | --- |
| `GFX_idea_013_disaster_aftermath` | `gfx/interface/ideas/013_natural_disasters/idea_013_disaster_aftermath.dds` |
| `GFX_idea_013_refugee_pressure` | `gfx/interface/ideas/013_natural_disasters/idea_013_refugee_pressure.dds` |
| `GFX_idea_013_famine_pressure` | `gfx/interface/ideas/013_natural_disasters/idea_013_famine_pressure.dds` |
| `GFX_idea_013_broken_infrastructure` | `gfx/interface/ideas/013_natural_disasters/idea_013_broken_infrastructure.dds` |
| `GFX_idea_013_disaster_recovery_mobilization` | `gfx/interface/ideas/013_natural_disasters/idea_013_disaster_recovery_mobilization.dds` |

Validation note: each processed PNG, package DDS copy, and live DDS file is `64x64` with alpha, transparent corners, and zero visible green, magenta, or purple key pixels. No `.gfx` edits are needed because the registered sprite names and texture paths stayed stable.
