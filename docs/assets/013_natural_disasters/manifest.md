# Event 013 Natural Disasters art manifest

Event id: `013`
Event slug: `natural_disasters`
Source mode summary: generated event art, generated icons, and regenerated frame-animation source art through official `image_gen`
Scope note: this manifest covers Event 13 report, news, super-event, decision-category picture, decision icon, decision-category icon, idea/state icon, achievement, static abnormal-GUI, and animated scripted-GUI assets.
Prompt records: `docs/assets/013_natural_disasters/prompts/generated_event_art_prompts.md` and `docs/assets/013_natural_disasters/prompts/2026-07-10_static_completion_prompts.md`
Report contact sheet: `docs/assets/013_natural_disasters/contact_sheets/013_natural_disasters_report_contact_sheet.png`
News contact sheet: `docs/assets/013_natural_disasters/contact_sheets/013_natural_disasters_news_contact_sheet.png`
Specific family news contact sheet: `docs/assets/013_natural_disasters/contact_sheets/013_natural_disasters_specific_news_contact_sheet.png`
Decision category picture contact sheet: `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_category_pictures_contact.png`
Decision category icon contact sheet: `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_category_icons_contact.png`
Decision icon contact sheet: `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_decision_icons_contact.png`
Idea icon contact sheet: `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_idea_icons_contact.png`
Validation note: `docs/assets/013_natural_disasters/notes/report_news_validation.md`

## 2026-07-10 accepted static completion addendum

This addendum is the current source of truth for the accepted non-animation completion pass. Earlier inventory below is retained for preserved assets and historical production context; its wiring statements are not completion proof.

Path contract for every listed non-achievement asset:

- source: `docs/assets/013_natural_disasters/source_png/<asset>_source.png`
- processed: `docs/assets/013_natural_disasters/processed_png/<asset>.png`
- package DDS: `docs/assets/013_natural_disasters/dds/<asset>.dds`
- live DDS: the system-specific path shown in `docs/assets/013_natural_disasters/gfx_handoff.md`

### Added report identities (`210x176`, sepia report cards)

| Asset | Coverage purpose | Status |
| --- | --- | --- |
| `report_event_nd_tropical_cyclone` | tropical-cyclone family report | complete |
| `report_event_nd_heat_wave` | heat-wave family report | complete |
| `report_event_nd_extreme_wind` | extreme-wind family report | complete |
| `report_event_nd_tornado_outbreak` | tornado-outbreak family report | complete |
| `report_event_nd_hailstorm` | hailstorm family report | complete |
| `report_event_nd_extreme_cold_wave` | cold-wave family report | complete |
| `report_event_nd_wet_mass_movement` | wet mass-movement family report | complete |
| `report_event_nd_ashfall` | ashfall family report | complete |
| `report_event_nd_lahar` | lahar family report | complete |
| `report_event_nd_storm_surge` | storm-surge family report | complete |
| `report_event_nd_meteor_impact` | single-impact family report | complete |
| `report_event_nd_meteor_shower` | meteor-shower family report | complete |
| `report_event_nd_massive_eruption` | massive-eruption family report | complete |
| `report_event_nd_regional_aftermath` | live gameplay reference; broad multi-province reconstruction identity | complete |

### Added news identities (`397x153`, grayscale press images)

| Asset | Status |
| --- | --- |
| `news_event_nd_tornado_outbreak` | complete |
| `news_event_nd_ashfall` | complete |
| `news_event_nd_lahar` | complete |
| `news_event_nd_storm_surge` | complete |
| `news_event_nd_meteor_impact` | complete |

### Added decision, category, and idea/state icons

| Asset | Final size | Status |
| --- | --- | --- |
| `decision_nd_port_closure` | `32x32` | complete |
| `decision_nd_food_relief` | `32x32` | complete |
| `decision_nd_firebreaks` | `32x32` | complete |
| `decision_nd_ash_cleanup` | `32x32` | complete |
| `decision_nd_water_trains` | `32x32` | complete |
| `decision_nd_observatory_watch` | `32x32` | complete |
| `decision_nd_reconstruction` | `32x32` | complete |
| `decision_category_013_natural_disaster_aftermath` | `53x40` | complete |
| `idea_013_ashfall` | `64x64` | complete |
| `idea_013_disease_risk` | `64x64` | complete |
| `idea_013_blocked_ports` | `64x64` | complete |
| `idea_013_scorched_state` | `64x64` | complete |
| `idea_013_frozen_supply` | `64x64` | complete |
| `idea_013_cracked_ground` | `64x64` | complete |
| `idea_013_crater_aftermath` | `64x64` | complete |

### Added abnormal-GUI static assets

| Asset | Final size | Status |
| --- | --- | --- |
| `013_abnormal_disaster_panel` | `760x520` | complete |
| `013_abnormal_disaster_panel_damaged` | `760x520` | complete |
| `013_disaster_card_frame` | `280x124` | complete |
| `013_map_marker_impact` | `48x48` | complete |
| `013_map_marker_chain_risk` | `48x48` | complete |
| `013_foreign_relief_badge` | `48x48` | complete |
| `013_recovery_progress_frame` | `280x24` | complete |
| `013_recovery_progress_fill` | `276x16` | complete |

### Added super-event identities (`457x328`, grayscale radio images)

| Asset | Status |
| --- | --- |
| `super_event_nd_abnormal_disaster_age` | complete; slot unassigned |
| `super_event_nd_delayed_tsunami_chain` | complete; slot unassigned |

### Accepted achievement identities

Each identity has individual source PNG, processed colour PNG, grey PNG, not-eligible PNG, package DDS triplet, and live root DDS triplet under `gfx/achievements/`. The live basename is `013_natural_disasters_<slug>`.

| Slug | Status |
| --- | --- |
| `after_the_sirens` | complete |
| `no_second_wave` | complete |
| `every_bridge_counts` | complete |
| `ashes_without_famine` | complete |
| `no_global_announcer` | complete |
| `under_the_falling_sky` | complete |
| `shake_the_world_back` | complete |
| `disaster_barrage_maximum` | complete |
| `not_one_more_camp` | complete |
| `catalogue_of_ruin` | complete |

The not-eligible treatment uses `source_png/achievement_not_eligible_overlay_recovered.png`, mathematically recovered from eight existing Event 013 repository triplets with mean reconstruction error `0.07/255`, because the skill-pack overlay file was absent.

### Storm-corridor super-event provenance closure

| Field | Current record |
| --- | --- |
| Asset | `super_event_nd_storm_corridor` |
| Event | `013_natural_disasters` |
| Asset type | generated super-event radio image |
| Intended use | slot `70`, sustained destructive multi-state moving storm/tornado corridor |
| Source mode | official built-in `image_gen`; generated fictional/composite period-documentary scene |
| Source-mode rationale | no single archival incident can honestly represent the accepted sustained Event 013 rail/road corridor, separated funnels, multiple towns, and coordinated period relief route |
| Exact prompt and result | `docs/assets/013_natural_disasters/prompts/2026-07-10_static_completion_prompts.md`; result `exec-f951d9ec-e1c4-49e2-bab7-fbdee7797b5a.png` |
| Era-fit note | 1936-1945 press-photograph treatment; period freight cars, telephone poles, small-town architecture, canvas-covered relief trucks, ambulance, railway workers, and civilian evacuees; no modern objects or branding |
| Source PNG | `docs/assets/013_natural_disasters/source_png/super_event_nd_storm_corridor_source.png` |
| Processed PNG | `docs/assets/013_natural_disasters/processed_png/super_event_nd_storm_corridor.png` |
| Package DDS | `docs/assets/013_natural_disasters/dds/super_event_nd_storm_corridor.dds` |
| Live DDS | `gfx/super_events/013_natural_disasters/super_event_nd_storm_corridor.dds` |
| Target size | `457x328` |
| Sprite | `GFX_super_event_nd_storm_corridor` |
| Target GFX file | `interface/chaosx_super_events.gfx` (unchanged; not edited by asset task) |
| Visual identity | broad storm shelf, four separated visible funnels, continuous rail/road damage path, multiple settlements, and period response convoy; the path reads as sustained geographic motion rather than one local storm |
| Status | `complete`; fresh source and exact prompt provenance recorded 2026-07-10 |

### DDS format normalization without identity changes

The following eight preserved files were reconverted from their existing processed PNGs to 32-bit RGB+A DDS in package and live locations without source or identity changes: `news_event_nd_disaster_barrage`, `news_event_nd_great_rupture`, `news_event_nd_massive_eruption`, `news_event_nd_meteor_showers`, `news_event_nd_regional_floods`, `super_event_nd_great_rupture`, `super_event_nd_massive_eruption`, and `super_event_nd_skyfall`. `super_event_nd_storm_corridor` was also normalized in that pass, but its source art has since been deliberately replaced by the provenance-closed generated package above.

## Legacy inventory and historical production status

### Super-event radio art

These are 457x328 super-event radio images wired through `interface/chaosx_super_events.gfx`, separate from Event 13 report images, news images, decision category pictures, and decision category button icons.

| Asset | Super-event slot | Source PNG | Processed PNG | Final DDS path | Sprite name | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `super_event_nd_great_rupture` | `67` | `docs/assets/013_natural_disasters/source_png/super_event_nd_great_rupture_source.png` | `docs/assets/013_natural_disasters/processed_png/super_event_nd_great_rupture.png` | `gfx/super_events/013_natural_disasters/super_event_nd_great_rupture.dds` | `GFX_super_event_nd_great_rupture` | `complete` |
| `super_event_nd_massive_eruption` | `68` | `docs/assets/013_natural_disasters/source_png/super_event_nd_massive_eruption_source.png` | `docs/assets/013_natural_disasters/processed_png/super_event_nd_massive_eruption.png` | `gfx/super_events/013_natural_disasters/super_event_nd_massive_eruption.dds` | `GFX_super_event_nd_massive_eruption` | `complete` |
| `super_event_nd_skyfall` | `69` | `docs/assets/013_natural_disasters/source_png/super_event_nd_skyfall_source.png` | `docs/assets/013_natural_disasters/processed_png/super_event_nd_skyfall.png` | `gfx/super_events/013_natural_disasters/super_event_nd_skyfall.dds` | `GFX_super_event_nd_skyfall` | `complete` |
| `super_event_nd_storm_corridor` | `70` | `docs/assets/013_natural_disasters/source_png/super_event_nd_storm_corridor_source.png` | `docs/assets/013_natural_disasters/processed_png/super_event_nd_storm_corridor.png` | `gfx/super_events/013_natural_disasters/super_event_nd_storm_corridor.dds` | `GFX_super_event_nd_storm_corridor` | `complete; provenance-closed replacement` |

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

### Accepted Part 9 abnormal-GUI animations

These eight packages contain generated source atlases, separate source-frame PNGs, processed alpha frames, horizontal sheet PNG+DDS, static PNG+DDS, review-only GIFs, contact sheets, exact retained prompts, per-frame atlas/cell provenance, briefs, frame plans, and build metadata. The DDS files are delivered to `gfx/interface/animated/013_natural_disasters/` and are wired through `interface/013_natural_disasters.gfx`, `interface/013_natural_disasters.gui`, and `common/scripted_guis/013_natural_disasters_scripted_gui.txt` with state-driven animated/static switching.

| Asset | Frames | Frame/sheet size | FPS | Sprite pair | Final sheet/static DDS | Status |
| --- | ---: | --- | ---: | --- | --- | --- |
| `013_disaster_card_frame_warning` | 8 | `540x88` / `4320x88` | 10 | `GFX_013_disaster_card_frame_warning_animated` / `GFX_013_disaster_card_frame_warning_static` | `013_disaster_card_frame_warning_{sheet,static}.dds` | `handed_off` |
| `013_disaster_card_frame_impact` | 10 | `540x88` / `5400x88` | 11 | `GFX_013_disaster_card_frame_impact_animated` / `GFX_013_disaster_card_frame_impact_static` | `013_disaster_card_frame_impact_{sheet,static}.dds` | `handed_off` |
| `013_impact_pulse_overlay` | 8 | `64x64` / `512x64` | 8 | `GFX_013_map_marker_next_hit_animated` / `GFX_013_map_marker_next_hit_static` | `013_impact_pulse_overlay_{sheet,static}.dds` | `handed_off` |
| `013_rupture_wave_overlay` | 12 | `560x130` / `6720x130` | 8 | `GFX_013_rupture_wave_sheet` / `GFX_013_rupture_wave_static` | `013_rupture_wave_overlay_{sheet,static}.dds` | `handed_off` |
| `013_meteor_rain_overlay` | 12 | `320x210` / `3840x210` | 10 | `GFX_013_meteor_fall_sheet` / `GFX_013_meteor_fall_static` | `013_meteor_rain_overlay_{sheet,static}.dds` | `handed_off` |
| `013_ash_plume_overlay` | 12 | `300x190` / `3600x190` | 8 | `GFX_013_eruption_plume_sheet` / `GFX_013_eruption_plume_static` | `013_ash_plume_overlay_{sheet,static}.dds` | `handed_off` |
| `013_tsunami_path_ribbon` | 10 | `520x24` / `5200x24` | 8 | `GFX_013_tsunami_train_sheet` / `GFX_013_tsunami_train_static` | `013_tsunami_path_ribbon_{sheet,static}.dds` | `handed_off` |
| `013_storm_corridor_path_ribbon` | 14 | `520x24` / `7280x24` | 10 | `GFX_013_storm_corridor_sheet` / `GFX_013_storm_corridor_static` | `013_storm_corridor_path_ribbon_{sheet,static}.dds` | `handed_off` |

Exact final DDS paths use `gfx/interface/animated/013_natural_disasters/<asset>_{sheet,static}.dds`. Each package records its exact paths in `brief.md` and `notes/build_metadata.json`. Ready-to-copy sprite definitions and GUI-state routing are in `gfx_handoff.md`. Implementation handoff: `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-10_event013_abnormal_animation_asset_handoff.md`.

### Retained auxiliary 36x36 animations

The five earlier packages remain usable auxiliary markers. Their generated 4x2 source sheets and eight distinct source-frame cells are retained. The original exact prompts and built-in result identifiers were not retained, so the package provenance notes explicitly record that limitation rather than inventing prompt history. Their prior manifest link pointed to a nonexistent handoff and is superseded by the handoff above.

| Asset | Frames | Frame/sheet size | Measured preview rate | Sprite pair | Status |
| --- | ---: | --- | ---: | --- | --- |
| `natural_disaster_warning_pulse` | 8 | `36x36` / `288x36` | about 8.33 fps | `GFX_013_warning_pulse_animated` / `GFX_013_warning_pulse` | `handed_off` |
| `natural_disaster_storm_corridor_track` | 8 | `36x36` / `288x36` | about 8.33 fps | `GFX_013_storm_corridor_marker_animated` / `GFX_013_storm_corridor_marker` | `handed_off` |
| `natural_disaster_tsunami_countdown` | 8 | `36x36` / `288x36` | about 8.33 fps | `GFX_013_tsunami_countdown_animated` / `GFX_013_tsunami_countdown` | `handed_off` |
| `natural_disaster_eruption_ashfall` | 8 | `36x36` / `288x36` | about 8.33 fps | `GFX_013_eruption_marker_animated` / `GFX_013_eruption_marker` | `handed_off` |
| `natural_disaster_skyfall_alarm` | 8 | `36x36` / `288x36` | about 8.33 fps | `GFX_013_skyfall_alarm_animated` / `GFX_013_skyfall_alarm` | `handed_off` |

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

Meaningful-hit news events `chaosx.nr13.305` through `chaosx.nr13.328` use dedicated `397x153` black-and-white news images. They are derived from the existing generated Event 013 family source art, processed as press-photo crops, copied into both the package DDS folder and the live Event 013 event-picture folder, and registered through `interface/013_natural_disasters.gfx`.

| Asset | Source PNG | Processed PNG | Final DDS path | Sprite name | Status |
| --- | --- | --- | --- | --- | --- |
| `news_event_nd_earthquake` | `docs/assets/013_natural_disasters/source_png/news_event_nd_earthquake_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_earthquake.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_earthquake.dds` | `GFX_news_event_nd_earthquake` | `complete` |
| `news_event_nd_flood` | `docs/assets/013_natural_disasters/source_png/news_event_nd_flood_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_flood.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_flood.dds` | `GFX_news_event_nd_flood` | `complete` |
| `news_event_nd_tropical_cyclone` | `docs/assets/013_natural_disasters/source_png/news_event_nd_tropical_cyclone_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_tropical_cyclone.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_tropical_cyclone.dds` | `GFX_news_event_nd_tropical_cyclone` | `complete` |
| `news_event_nd_thunderstorm` | `docs/assets/013_natural_disasters/source_png/news_event_nd_thunderstorm_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_thunderstorm.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_thunderstorm.dds` | `GFX_news_event_nd_thunderstorm` | `complete` |
| `news_event_nd_hailstorm` | `docs/assets/013_natural_disasters/source_png/news_event_nd_hailstorm_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_hailstorm.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_hailstorm.dds` | `GFX_news_event_nd_hailstorm` | `complete` |
| `news_event_nd_extreme_wind` | `docs/assets/013_natural_disasters/source_png/news_event_nd_extreme_wind_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_extreme_wind.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_extreme_wind.dds` | `GFX_news_event_nd_extreme_wind` | `complete` |
| `news_event_nd_wildfire` | `docs/assets/013_natural_disasters/source_png/news_event_nd_wildfire_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_wildfire.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_wildfire.dds` | `GFX_news_event_nd_wildfire` | `complete` |
| `news_event_nd_drought` | `docs/assets/013_natural_disasters/source_png/news_event_nd_drought_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_drought.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_drought.dds` | `GFX_news_event_nd_drought` | `complete` |
| `news_event_nd_dust_storm` | `docs/assets/013_natural_disasters/source_png/news_event_nd_dust_storm_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_dust_storm.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_dust_storm.dds` | `GFX_news_event_nd_dust_storm` | `complete` |
| `news_event_nd_blizzard` | `docs/assets/013_natural_disasters/source_png/news_event_nd_blizzard_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_blizzard.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_blizzard.dds` | `GFX_news_event_nd_blizzard` | `complete` |
| `news_event_nd_heat_wave` | `docs/assets/013_natural_disasters/source_png/news_event_nd_heat_wave_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_heat_wave.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_heat_wave.dds` | `GFX_news_event_nd_heat_wave` | `complete` |
| `news_event_nd_cold_wave` | `docs/assets/013_natural_disasters/source_png/news_event_nd_cold_wave_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_cold_wave.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_cold_wave.dds` | `GFX_news_event_nd_cold_wave` | `complete` |
| `news_event_nd_dry_mass_movement` | `docs/assets/013_natural_disasters/source_png/news_event_nd_dry_mass_movement_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_dry_mass_movement.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_dry_mass_movement.dds` | `GFX_news_event_nd_dry_mass_movement` | `complete` |
| `news_event_nd_wet_mass_movement` | `docs/assets/013_natural_disasters/source_png/news_event_nd_wet_mass_movement_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_wet_mass_movement.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_wet_mass_movement.dds` | `GFX_news_event_nd_wet_mass_movement` | `complete` |
| `news_event_nd_volcanic_eruption` | `docs/assets/013_natural_disasters/source_png/news_event_nd_volcanic_eruption_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_volcanic_eruption.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_volcanic_eruption.dds` | `GFX_news_event_nd_volcanic_eruption` | `complete` |
| `news_event_nd_tsunami` | `docs/assets/013_natural_disasters/source_png/news_event_nd_tsunami_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_tsunami.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_tsunami.dds` | `GFX_news_event_nd_tsunami` | `complete` |
| `news_event_nd_avalanche` | `docs/assets/013_natural_disasters/source_png/news_event_nd_avalanche_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_avalanche.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_avalanche.dds` | `GFX_news_event_nd_avalanche` | `complete` |
| `news_event_nd_glacial_outburst` | `docs/assets/013_natural_disasters/source_png/news_event_nd_glacial_outburst_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_glacial_outburst.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_glacial_outburst.dds` | `GFX_news_event_nd_glacial_outburst` | `complete` |
| `news_event_nd_sinkhole` | `docs/assets/013_natural_disasters/source_png/news_event_nd_sinkhole_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_sinkhole.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_sinkhole.dds` | `GFX_news_event_nd_sinkhole` | `complete` |
| `news_event_nd_limnic_eruption` | `docs/assets/013_natural_disasters/source_png/news_event_nd_limnic_eruption_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_limnic_eruption.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_limnic_eruption.dds` | `GFX_news_event_nd_limnic_eruption` | `complete` |
| `news_event_nd_meteor_shower` | `docs/assets/013_natural_disasters/source_png/news_event_nd_meteor_shower_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_meteor_shower.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_meteor_shower.dds` | `GFX_news_event_nd_meteor_shower` | `complete` |
| `news_event_nd_global_rupture` | `docs/assets/013_natural_disasters/source_png/news_event_nd_global_rupture_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_global_rupture.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_global_rupture.dds` | `GFX_news_event_nd_global_rupture` | `complete` |
| `news_event_nd_massive_eruption_specific` | `docs/assets/013_natural_disasters/source_png/news_event_nd_massive_eruption_specific_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_massive_eruption_specific.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_massive_eruption_specific.dds` | `GFX_news_event_nd_massive_eruption_specific` | `complete` |
| `news_event_nd_storm_corridor` | `docs/assets/013_natural_disasters/source_png/news_event_nd_storm_corridor_source.png` | `docs/assets/013_natural_disasters/processed_png/news_event_nd_storm_corridor.png` | `gfx/event_pictures/013_natural_disasters/news_event_nd_storm_corridor.dds` | `GFX_news_event_nd_storm_corridor` | `complete` |

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
