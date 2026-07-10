# Event 013 Natural Disasters art handoff

Proposed target `.gfx` file: `interface/013_natural_disasters.gfx`

Integration closure, 2026-07-10: the parent implementation registered the accepted sprites, bound the GUI identities, and switched the matching report/news events to their family-specific art. The tables below remain the source identity handoff; their original asset-subtask wording is historical, while live wiring is proven by `interface/013_natural_disasters.gfx`, `interface/013_natural_disasters.gui`, and `events/013_natural_disasters.txt`.

## Accepted 2026-07-10 static completion registration

The following exact names and paths were the registration handoff for the non-animation completion pass. The parent implementation has completed the registration.

### Report-event sprites

Register these as `spriteType` entries in `interface/013_natural_disasters.gfx`.

| Sprite | Live DDS path |
| --- | --- |
| `GFX_report_event_nd_tropical_cyclone` | `gfx/event_pictures/013_natural_disasters/report_event_nd_tropical_cyclone.dds` |
| `GFX_report_event_nd_heat_wave` | `gfx/event_pictures/013_natural_disasters/report_event_nd_heat_wave.dds` |
| `GFX_report_event_nd_extreme_wind` | `gfx/event_pictures/013_natural_disasters/report_event_nd_extreme_wind.dds` |
| `GFX_report_event_nd_tornado_outbreak` | `gfx/event_pictures/013_natural_disasters/report_event_nd_tornado_outbreak.dds` |
| `GFX_report_event_nd_hailstorm` | `gfx/event_pictures/013_natural_disasters/report_event_nd_hailstorm.dds` |
| `GFX_report_event_nd_extreme_cold_wave` | `gfx/event_pictures/013_natural_disasters/report_event_nd_extreme_cold_wave.dds` |
| `GFX_report_event_nd_wet_mass_movement` | `gfx/event_pictures/013_natural_disasters/report_event_nd_wet_mass_movement.dds` |
| `GFX_report_event_nd_ashfall` | `gfx/event_pictures/013_natural_disasters/report_event_nd_ashfall.dds` |
| `GFX_report_event_nd_lahar` | `gfx/event_pictures/013_natural_disasters/report_event_nd_lahar.dds` |
| `GFX_report_event_nd_storm_surge` | `gfx/event_pictures/013_natural_disasters/report_event_nd_storm_surge.dds` |
| `GFX_report_event_nd_meteor_impact` | `gfx/event_pictures/013_natural_disasters/report_event_nd_meteor_impact.dds` |
| `GFX_report_event_nd_meteor_shower` | `gfx/event_pictures/013_natural_disasters/report_event_nd_meteor_shower.dds` |
| `GFX_report_event_nd_massive_eruption` | `gfx/event_pictures/013_natural_disasters/report_event_nd_massive_eruption.dds` |
| `GFX_report_event_nd_regional_aftermath` | `gfx/event_pictures/013_natural_disasters/report_event_nd_regional_aftermath.dds` |

### News-event sprites

Register these as `spriteType` entries in `interface/013_natural_disasters.gfx`.

| Sprite | Live DDS path |
| --- | --- |
| `GFX_news_event_nd_tornado_outbreak` | `gfx/event_pictures/013_natural_disasters/news_event_nd_tornado_outbreak.dds` |
| `GFX_news_event_nd_ashfall` | `gfx/event_pictures/013_natural_disasters/news_event_nd_ashfall.dds` |
| `GFX_news_event_nd_lahar` | `gfx/event_pictures/013_natural_disasters/news_event_nd_lahar.dds` |
| `GFX_news_event_nd_storm_surge` | `gfx/event_pictures/013_natural_disasters/news_event_nd_storm_surge.dds` |
| `GFX_news_event_nd_meteor_impact` | `gfx/event_pictures/013_natural_disasters/news_event_nd_meteor_impact.dds` |

### Decision and idea sprites

Register these as `spriteType` entries in `interface/013_natural_disasters.gfx`.

| Sprite | Live DDS path |
| --- | --- |
| `GFX_decision_nd_port_closure` | `gfx/interface/decisions/013_natural_disasters/decision_nd_port_closure.dds` |
| `GFX_decision_nd_food_relief` | `gfx/interface/decisions/013_natural_disasters/decision_nd_food_relief.dds` |
| `GFX_decision_nd_firebreaks` | `gfx/interface/decisions/013_natural_disasters/decision_nd_firebreaks.dds` |
| `GFX_decision_nd_ash_cleanup` | `gfx/interface/decisions/013_natural_disasters/decision_nd_ash_cleanup.dds` |
| `GFX_decision_nd_water_trains` | `gfx/interface/decisions/013_natural_disasters/decision_nd_water_trains.dds` |
| `GFX_decision_nd_observatory_watch` | `gfx/interface/decisions/013_natural_disasters/decision_nd_observatory_watch.dds` |
| `GFX_decision_nd_reconstruction` | `gfx/interface/decisions/013_natural_disasters/decision_nd_reconstruction.dds` |
| `GFX_decision_category_013_natural_disaster_aftermath` | `gfx/interface/decisions/013_natural_disasters/decision_category_013_natural_disaster_aftermath.dds` |
| `GFX_idea_013_ashfall` | `gfx/interface/ideas/013_natural_disasters/idea_013_ashfall.dds` |
| `GFX_idea_013_disease_risk` | `gfx/interface/ideas/013_natural_disasters/idea_013_disease_risk.dds` |
| `GFX_idea_013_blocked_ports` | `gfx/interface/ideas/013_natural_disasters/idea_013_blocked_ports.dds` |
| `GFX_idea_013_scorched_state` | `gfx/interface/ideas/013_natural_disasters/idea_013_scorched_state.dds` |
| `GFX_idea_013_frozen_supply` | `gfx/interface/ideas/013_natural_disasters/idea_013_frozen_supply.dds` |
| `GFX_idea_013_cracked_ground` | `gfx/interface/ideas/013_natural_disasters/idea_013_cracked_ground.dds` |
| `GFX_idea_013_crater_aftermath` | `gfx/interface/ideas/013_natural_disasters/idea_013_crater_aftermath.dds` |

### Abnormal-GUI static sprites

Register these as `spriteType` entries in `interface/013_natural_disasters.gfx`, then bind the same names in `interface/013_natural_disasters.gui`.

| Sprite | Live DDS path |
| --- | --- |
| `GFX_013_abnormal_disaster_panel` | `gfx/interface/013_natural_disasters/013_abnormal_disaster_panel.dds` |
| `GFX_013_abnormal_disaster_panel_damaged` | `gfx/interface/013_natural_disasters/013_abnormal_disaster_panel_damaged.dds` |
| `GFX_013_disaster_card_frame` | `gfx/interface/013_natural_disasters/013_disaster_card_frame.dds` |
| `GFX_013_map_marker_impact` | `gfx/interface/013_natural_disasters/013_map_marker_impact.dds` |
| `GFX_013_map_marker_chain_risk` | `gfx/interface/013_natural_disasters/013_map_marker_chain_risk.dds` |
| `GFX_013_foreign_relief_badge` | `gfx/interface/013_natural_disasters/013_foreign_relief_badge.dds` |
| `GFX_013_recovery_progress_frame` | `gfx/interface/013_natural_disasters/013_recovery_progress_frame.dds` |
| `GFX_013_recovery_progress_fill` | `gfx/interface/013_natural_disasters/013_recovery_progress_fill.dds` |

### Super-event sprites

Assign unused super-event slots first, then register these `spriteType` entries in `interface/chaosx_super_events.gfx`. Neither image has a slot yet.

| Sprite | Live DDS path |
| --- | --- |
| `GFX_super_event_nd_abnormal_disaster_age` | `gfx/super_events/013_natural_disasters/super_event_nd_abnormal_disaster_age.dds` |
| `GFX_super_event_nd_delayed_tsunami_chain` | `gfx/super_events/013_natural_disasters/super_event_nd_delayed_tsunami_chain.dds` |

### Achievement texture triplets

The achievement registry uses root texture basenames rather than `spriteType` registrations. For each slug below, use:

- completed: `gfx/achievements/013_natural_disasters_<slug>.dds`
- grey: `gfx/achievements/013_natural_disasters_<slug>_grey.dds`
- not eligible: `gfx/achievements/013_natural_disasters_<slug>_not_eligible.dds`

Accepted slugs: `after_the_sirens`, `no_second_wave`, `every_bridge_counts`, `ashes_without_famine`, `no_global_announcer`, `under_the_falling_sky`, `shake_the_world_back`, `disaster_barrage_maximum`, `not_one_more_camp`, and `catalogue_of_ruin`.

### Format-only replacements

No sprite-name or path change is required for the preserved identities `GFX_news_event_nd_disaster_barrage`, `GFX_news_event_nd_great_rupture`, `GFX_news_event_nd_massive_eruption`, `GFX_news_event_nd_meteor_showers`, `GFX_news_event_nd_regional_floods`, `GFX_super_event_nd_great_rupture`, `GFX_super_event_nd_massive_eruption`, and `GFX_super_event_nd_skyfall`. Their live DDS files were replaced in place with 32-bit RGB+A outputs. `GFX_super_event_nd_storm_corridor` also keeps its stable name and path, but the texture now comes from a fresh provenance-closed generated source rather than a format-only replacement.

## Abnormal scripted-GUI animation handoff

Local precedents inspected: offline `Graphical asset modding`, `Interface modding`, and `Scripted GUI modding` pages; vanilla `interface/alerts.gfx`, `interface/alerts.gui`, and `interface/mapicons.gfx`. The final HOI4 assets are horizontal DDS sheets; GIFs under `previews/` are review-only.

| State/use | GUI element proposed | Static sprite | Animated sprite | Frames / FPS | Loop / play on show | Anchor |
| --- | --- | --- | --- | --- | --- | --- |
| `warning_window` card | `natural_disaster_card_frame_warning` | `GFX_013_disaster_card_frame_warning_static` | `GFX_013_disaster_card_frame_warning_animated` | 8 / 10 | yes / yes | center |
| `impact_pending` card | `natural_disaster_card_frame_impact` | `GFX_013_disaster_card_frame_impact_static` | `GFX_013_disaster_card_frame_impact_animated` | 10 / 11 | yes / yes | center |
| selected next-hit state | `natural_disaster_map_marker_next_hit` | `GFX_013_map_marker_next_hit_static` | `GFX_013_map_marker_next_hit_animated` | 8 / 8 | yes / yes | center |
| `rupture_wave_layer` | `natural_disaster_rupture_wave_layer` | `GFX_013_rupture_wave_static` | `GFX_013_rupture_wave_sheet` | 12 / 8 | yes / yes | center |
| `meteor_path_layer` | `natural_disaster_meteor_path_layer` | `GFX_013_meteor_fall_static` | `GFX_013_meteor_fall_sheet` | 12 / 10 | yes / yes | bottom-center |
| `eruption_plume_layer` | `natural_disaster_eruption_plume_layer` | `GFX_013_eruption_plume_static` | `GFX_013_eruption_plume_sheet` | 12 / 8 | yes / yes | bottom-center |
| `tsunami_train_layer` | `natural_disaster_tsunami_train_layer` | `GFX_013_tsunami_train_static` | `GFX_013_tsunami_train_sheet` | 10 / 8 | yes / yes | center, fixed coast at right |
| `storm_corridor_layer` | `natural_disaster_storm_corridor_layer` | `GFX_013_storm_corridor_static` | `GFX_013_storm_corridor_sheet` | 14 / 10 | yes / yes | center, fixed route studs |

Static fallbacks should occupy the same GUI position and size as their animated pair. The scripted GUI should show the animated element only for the listed state and show the static element when animation is disabled, unsupported, or intentionally hidden. The accepted sprite names ending in `_sheet` are still `frameAnimatedSpriteType` names; the suffix is part of the accepted Part 9 contract.

Ready-to-copy `.gfx` definitions:

```txt
spriteTypes = {
	spriteType = {
		name = "GFX_013_disaster_card_frame_warning_static"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_disaster_card_frame_warning_static.dds"
	}
	frameAnimatedSpriteType = {
		name = "GFX_013_disaster_card_frame_warning_animated"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_disaster_card_frame_warning_sheet.dds"
		noOfFrames = 8
		animation_rate_fps = 10
		looping = yes
		play_on_show = yes
		pause_on_loop = 0.0
		alwaystransparent = yes
	}
	spriteType = {
		name = "GFX_013_disaster_card_frame_impact_static"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_disaster_card_frame_impact_static.dds"
	}
	frameAnimatedSpriteType = {
		name = "GFX_013_disaster_card_frame_impact_animated"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_disaster_card_frame_impact_sheet.dds"
		noOfFrames = 10
		animation_rate_fps = 11
		looping = yes
		play_on_show = yes
		pause_on_loop = 0.0
		alwaystransparent = yes
	}
	spriteType = {
		name = "GFX_013_map_marker_next_hit_static"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_impact_pulse_overlay_static.dds"
	}
	frameAnimatedSpriteType = {
		name = "GFX_013_map_marker_next_hit_animated"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_impact_pulse_overlay_sheet.dds"
		noOfFrames = 8
		animation_rate_fps = 8
		looping = yes
		play_on_show = yes
		pause_on_loop = 0.0
		alwaystransparent = yes
	}
	spriteType = {
		name = "GFX_013_rupture_wave_static"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_rupture_wave_overlay_static.dds"
	}
	frameAnimatedSpriteType = {
		name = "GFX_013_rupture_wave_sheet"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_rupture_wave_overlay_sheet.dds"
		noOfFrames = 12
		animation_rate_fps = 8
		looping = yes
		play_on_show = yes
		pause_on_loop = 0.0
		alwaystransparent = yes
	}
	spriteType = {
		name = "GFX_013_meteor_fall_static"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_meteor_rain_overlay_static.dds"
	}
	frameAnimatedSpriteType = {
		name = "GFX_013_meteor_fall_sheet"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_meteor_rain_overlay_sheet.dds"
		noOfFrames = 12
		animation_rate_fps = 10
		looping = yes
		play_on_show = yes
		pause_on_loop = 0.0
		alwaystransparent = yes
	}
	spriteType = {
		name = "GFX_013_eruption_plume_static"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_ash_plume_overlay_static.dds"
	}
	frameAnimatedSpriteType = {
		name = "GFX_013_eruption_plume_sheet"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_ash_plume_overlay_sheet.dds"
		noOfFrames = 12
		animation_rate_fps = 8
		looping = yes
		play_on_show = yes
		pause_on_loop = 0.0
		alwaystransparent = yes
	}
	spriteType = {
		name = "GFX_013_tsunami_train_static"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_tsunami_path_ribbon_static.dds"
	}
	frameAnimatedSpriteType = {
		name = "GFX_013_tsunami_train_sheet"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_tsunami_path_ribbon_sheet.dds"
		noOfFrames = 10
		animation_rate_fps = 8
		looping = yes
		play_on_show = yes
		pause_on_loop = 0.0
		alwaystransparent = yes
	}
	spriteType = {
		name = "GFX_013_storm_corridor_static"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_storm_corridor_path_ribbon_static.dds"
	}
	frameAnimatedSpriteType = {
		name = "GFX_013_storm_corridor_sheet"
		texturefile = "gfx/interface/animated/013_natural_disasters/013_storm_corridor_path_ribbon_sheet.dds"
		noOfFrames = 14
		animation_rate_fps = 10
		looping = yes
		play_on_show = yes
		pause_on_loop = 0.0
		alwaystransparent = yes
	}
}
```

Auxiliary marker sprite pairs are also ready for optional wiring. They do not replace the accepted assets above:

| Proposed GUI element | Static / animated sprite | DDS basename | Frames / FPS |
| --- | --- | --- | --- |
| `natural_disaster_warning_pulse_marker` | `GFX_013_warning_pulse` / `GFX_013_warning_pulse_animated` | `natural_disaster_warning_pulse` | 8 / 8.333 |
| `natural_disaster_storm_corridor_marker` | `GFX_013_storm_corridor_marker` / `GFX_013_storm_corridor_marker_animated` | `natural_disaster_storm_corridor_track` | 8 / 8.333 |
| `natural_disaster_tsunami_countdown_marker` | `GFX_013_tsunami_countdown` / `GFX_013_tsunami_countdown_animated` | `natural_disaster_tsunami_countdown` | 8 / 8.333 |
| `natural_disaster_eruption_marker` | `GFX_013_eruption_marker` / `GFX_013_eruption_marker_animated` | `natural_disaster_eruption_ashfall` | 8 / 8.333 |
| `natural_disaster_skyfall_alarm_marker` | `GFX_013_skyfall_alarm` / `GFX_013_skyfall_alarm_animated` | `natural_disaster_skyfall_alarm` | 8 / 8.333 |

Use the same static-plus-`frameAnimatedSpriteType` pattern shown above, with texture paths under `gfx/interface/animated/013_natural_disasters/`, `noOfFrames = 8`, `animation_rate_fps = 8.333`, `looping = yes`, and `play_on_show = yes`. The corrected briefs name the exact static and sheet paths. Their original exact image-generation prompts were not retained; package provenance notes record that limitation.

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
  - Source PNG: `docs/assets/013_natural_disasters/source_png/super_event_nd_storm_corridor_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/super_event_nd_storm_corridor.png`
  - Prompt provenance: `docs/assets/013_natural_disasters/prompts/2026-07-10_static_completion_prompts.md`, result `exec-f951d9ec-e1c4-49e2-bab7-fbdee7797b5a.png`
  - Use notes: broad storm shelf, four separated funnels, continuous rail/road damage path, multiple towns, and period response convoy support the accepted sustained multi-state moving storm/tornado corridor. The replacement is not a local-storm fallback.

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

Meaningful individual-hit news events `chaosx.nr13.305` through `chaosx.nr13.328` use dedicated `397x153` black-and-white news sprites. They are separate from report-event pictures; verify their current registrations in `interface/013_natural_disasters.gfx` during parent integration.

Specific family headline sprites:

- `GFX_news_event_nd_earthquake` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_earthquake.dds`
- `GFX_news_event_nd_flood` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_flood.dds`
- `GFX_news_event_nd_tropical_cyclone` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_tropical_cyclone.dds`
- `GFX_news_event_nd_thunderstorm` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_thunderstorm.dds`
- `GFX_news_event_nd_hailstorm` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_hailstorm.dds`
- `GFX_news_event_nd_extreme_wind` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_extreme_wind.dds`
- `GFX_news_event_nd_wildfire` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_wildfire.dds`
- `GFX_news_event_nd_drought` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_drought.dds`
- `GFX_news_event_nd_dust_storm` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_dust_storm.dds`
- `GFX_news_event_nd_blizzard` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_blizzard.dds`
- `GFX_news_event_nd_heat_wave` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_heat_wave.dds`
- `GFX_news_event_nd_cold_wave` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_cold_wave.dds`
- `GFX_news_event_nd_dry_mass_movement` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_dry_mass_movement.dds`
- `GFX_news_event_nd_wet_mass_movement` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_wet_mass_movement.dds`
- `GFX_news_event_nd_volcanic_eruption` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_volcanic_eruption.dds`
- `GFX_news_event_nd_tsunami` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_tsunami.dds`
- `GFX_news_event_nd_avalanche` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_avalanche.dds`
- `GFX_news_event_nd_glacial_outburst` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_glacial_outburst.dds`
- `GFX_news_event_nd_sinkhole` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_sinkhole.dds`
- `GFX_news_event_nd_limnic_eruption` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_limnic_eruption.dds`
- `GFX_news_event_nd_meteor_shower` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_meteor_shower.dds`
- `GFX_news_event_nd_global_rupture` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_global_rupture.dds`
- `GFX_news_event_nd_massive_eruption_specific` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_massive_eruption_specific.dds`
- `GFX_news_event_nd_storm_corridor` -> `gfx/event_pictures/013_natural_disasters/news_event_nd_storm_corridor.dds`

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

Validation note: each preserved processed PNG, package DDS copy, and live DDS file is `64x64` with alpha, transparent corners, and zero visible green, magenta, or purple key pixels. This production pass made no `.gfx` edit; the five historical sprite names and texture paths in this legacy section stayed stable.
