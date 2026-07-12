# Event 013 Natural Disasters visual asset audit

> Disposition, 2026-07-12: superseded as a historical gap inventory after implementation. At the time of the completion tranche, every accepted static, animated, achievement, report/news, abnormal-GUI, and six-role super-event identity had source, processed, final DDS, manifest, registration, and live-reference evidence. The current working tree retains the registered live assets but deletes the tracked `docs/assets/013_natural_disasters/` source archive as part of a concurrent repository-wide retention cleanup. Current closure therefore remains blocked on that external retention decision; use the implementation validation notes for the live-runtime evidence and this file only for historical discovery context.

Audit date: 2026-07-09

Scope: visual assets only. This audit compares the accepted Event 013 source-of-truth package with the current asset package and live DDS files. It does not assess gameplay behavior, localisation, spreadsheet content, audio, or deleted legacy Natural Disasters/Earth Earthquake logic. No generated images, downloads, asset replacements, manifest corrections, interface edits, or commits were made.

## Sources inspected

- `docs/specs/013_natural_disasters_specs/README.md`
- `docs/specs/013_natural_disasters_specs/manifest.md`
- `docs/specs/013_natural_disasters_specs/docs_alignment/013_source_of_truth_and_disposition_map.md`
- all accepted source specs in `docs/specs/013_natural_disasters_specs/specs/`
- `docs/specs/013_natural_disasters_specs/prompts/natural_disasters_asset_prompt.md`
- `docs/specs/013_natural_disasters_specs/prompts/natural_disasters_achievement_prompt.md`
- `docs/specs/013_natural_disasters_specs/prompts/natural_disasters_super_event_prompt.md`
- `docs/specs/013_natural_disasters_specs/matrices/013_news_report_direction_matrix.md`
- `docs/specs/013_natural_disasters_specs/matrices/013_super_event_research_handoff_matrix.md`
- all Markdown files, source PNGs, processed PNGs, animation frames, sheets, previews, contact sheets, and package DDS files under `docs/assets/013_natural_disasters/`
- all live Event 013 DDS files under `gfx/`
- `docs/super_events/013_natural_disasters_super_event_text_research.md` for current image-path and provenance claims
- the offline graphical asset, interface, and scripted-GUI wiki pages and vanilla `frameAnimatedSpriteType` examples for the animation acceptance model

The accepted source-of-truth map says Parts 1 through 10 remain authoritative. Where the later super-event text research note conflicts with Part 6, this audit retains Part 6 as the acceptance baseline and records the conflict for parent disposition.

## Executive conclusion

The repository contains a substantial and mostly usable static-art library, but the Event 013 visual package is **not accepted-spec complete**.

Measured current package:

| Surface | Current files | Audit result |
| --- | ---: | --- |
| Report images | 14 source PNG + 14 processed PNG + 14 DDS | Strong reusable set; accepted minimum still lacks dedicated cyclone and heat reports. |
| News images | 29 source PNG + 29 processed PNG + 29 DDS | Broad family coverage; five accepted deep-family news identities have no dedicated file. Several extra-family images reuse unrelated sources. |
| Decision category pictures | 22 source PNG + 22 processed PNG + 22 DDS | Usable derivative scene art at `114x101`; not independent source art in 20 cases. |
| Decision category icons | 22 source PNG + 22 processed PNG + 22 DDS | Readable `53x40` icons; naming and institutional framing do not match the accepted single-aftermath-category direction. |
| Decision icons | 17 source PNG + 17 processed PNG + 17 DDS | Generally usable `32x32` icons; seven exact accepted action identities are absent and two source files are reused across icon types. |
| Idea/modifier icons | 5 source PNG + 5 processed PNG + 5 DDS | Usable `64x64` core ideas; seven accepted family/state identities are absent. |
| Achievement icons | 8 individual source PNGs, two source sheets, 24 DDS variants | Obsolete eight-achievement set; no per-icon processed PNGs; does not match the accepted ten-achievement set. |
| Super-event images | 4 source PNG + 4 processed PNG + 4 DDS | High-quality and usable for rupture, eruption, skyfall, and storm corridor; two accepted Part 6 roles are absent. |
| Animation packages | 5 packages, each with 8 source frames, 8 processed frames, sheet, static fallback, DDS pair, GIF, and contact sheet | Mechanically complete as small `36x36` marker loops, but they do not satisfy the accepted abnormal-GUI overlay/frame assets or sprite handoff contract. |
| Static abnormal GUI art | none | Missing. |
| Sprite definitions/wiring | none found | `interface/013_natural_disasters.gfx` and `.gui` do not exist; no Event 013 sprite name or texture path appears in current interface files. |

All 147 package DDS files have byte-identical live counterparts after mapping package achievement names from `achievement_nd_*` to live `013_natural_disasters_*`. The file-delivery copy step therefore succeeded. The missing work is accepted coverage, provenance, format normalization, and sprite/GUI handoff rather than absent live copies.

## DDS format evidence

The current DDS dimensions and formats were read directly from their headers.

| Count | Dimensions | Format/use |
| ---: | --- | --- |
| 29 | `64x64` | 24 achievement variants plus 5 idea icons, 32-bit BGRA-style masks |
| 24 | `397x153` | specific-family news, 32-bit BGRA-style masks |
| 5 | `397x153` | older broad news images, 24-bit RGB |
| 22 | `53x40` | decision category icons, 32-bit BGRA-style masks |
| 22 | `114x101` | decision category pictures, 32-bit BGRA-style masks |
| 17 | `32x32` | decision icons, 32-bit BGRA-style masks |
| 14 | `210x176` | report cards, 32-bit BGRA-style masks |
| 5 | `288x36` | eight-frame animation sheets, 32-bit BGRA-style masks |
| 5 | `36x36` | animation static fallbacks, 32-bit BGRA-style masks |
| 4 | `457x328` | super-event images, 24-bit RGB |

The asset skill requires the normal 32-bit BGRA/B8G8R8A8 workflow. The following nine DDS files are 24-bit and should not be called format-complete until they are reconverted with an opaque alpha channel:

- `news_event_nd_disaster_barrage.dds`
- `news_event_nd_great_rupture.dds`
- `news_event_nd_massive_eruption.dds`
- `news_event_nd_meteor_showers.dds`
- `news_event_nd_regional_floods.dds`
- `super_event_nd_great_rupture.dds`
- `super_event_nd_massive_eruption.dds`
- `super_event_nd_skyfall.dds`
- `super_event_nd_storm_corridor.dds`

Route reconverted news files to `gfx/event_pictures/013_natural_disasters/` and super-event files to `gfx/super_events/013_natural_disasters/`, preserving current filenames and sprite names.

## Usable static inventory

### Report images

The 14 report images all have source PNGs, processed `210x176` RGBA report-card PNGs, 32-bit DDS files, transparent report-card corners, and readable contact-sheet evidence. Their visual identities are distinct enough for the named uses below.

| Current asset | Usable role | Qualification |
| --- | --- | --- |
| `report_event_nd_earthquake` | earthquake | Good accepted-family match. |
| `report_event_nd_flood` | flood | Good accepted-family match. |
| `report_event_nd_storm` | thunderstorm/general severe storm | Prompt and image emphasize damaged airfield/rail; not a dedicated tropical cyclone report. |
| `report_event_nd_wildfire` | wildfire | Good accepted-family match. |
| `report_event_nd_winter` | blizzard/general cold | Good blizzard match; can be a shared cold fallback only if reuse is explicitly accepted. |
| `report_event_nd_drought_famine` | drought/famine pressure | Good drought match; not a dedicated heat-wave image. |
| `report_event_nd_dust_sandstorm` | sandstorm/dust | Good accepted-family match. |
| `report_event_nd_volcano` | ordinary eruption/ash context | Good ordinary-volcano match; not a distinct massive-eruption report. |
| `report_event_nd_landslide` | general mass movement | Good dry-landslide match; wet movement/lahar are not distinct. |
| `report_event_nd_tsunami` | tsunami | Good accepted-family match. |
| `report_event_nd_skyfall` | meteor/skyfall | Good abnormal-family match. |
| `report_event_nd_moving_corridor` | moving storm/tornado corridor | Good abnormal-family match. |
| `report_event_nd_rupture_wave` | whole-earth rupture | Good abnormal-family match. |
| `report_event_nd_barrage` | regional aftermath/manual barrage | Good accepted regional/composite aftermath match. |

Accepted Part 6/asset-prompt minimum gaps:

- `report_event_nd_tropical_cyclone`
- `report_event_nd_heat_wave`

Recommended full paths for both:

```text
docs/assets/013_natural_disasters/source_png/<name>_source.png
docs/assets/013_natural_disasters/processed_png/<name>.png
docs/assets/013_natural_disasters/dds/<name>.dds
gfx/event_pictures/013_natural_disasters/<name>.dds
```

Recommended sprites: `GFX_report_event_nd_tropical_cyclone` and `GFX_report_event_nd_heat_wave` in `interface/013_natural_disasters.gfx`.

Part 8 gives every family a distinct report direction. If that is interpreted as distinct image coverage rather than distinct text over shared art, the package also needs dedicated reports for extreme wind, tornado outbreak, hailstorm, extreme cold, wet mass movement, ashfall, lahar, storm surge, meteor impact versus shower, and massive eruption. Exact recommended basenames are:

```text
report_event_nd_extreme_wind
report_event_nd_tornado_outbreak
report_event_nd_hailstorm
report_event_nd_extreme_cold_wave
report_event_nd_wet_mass_movement
report_event_nd_ashfall
report_event_nd_lahar
report_event_nd_storm_surge
report_event_nd_meteor_impact
report_event_nd_meteor_shower
report_event_nd_massive_eruption
```

This second list is a coverage decision for the parent. It is not safe to silently declare the existing shared images equivalent because Part 8 explicitly rejects families that become visually generic.

### News images

Current exact-family news basenames:

```text
news_event_nd_earthquake
news_event_nd_flood
news_event_nd_tropical_cyclone
news_event_nd_thunderstorm
news_event_nd_hailstorm
news_event_nd_extreme_wind
news_event_nd_wildfire
news_event_nd_drought
news_event_nd_dust_storm
news_event_nd_blizzard
news_event_nd_heat_wave
news_event_nd_cold_wave
news_event_nd_dry_mass_movement
news_event_nd_wet_mass_movement
news_event_nd_volcanic_eruption
news_event_nd_tsunami
news_event_nd_meteor_shower
news_event_nd_global_rupture
news_event_nd_massive_eruption_specific
news_event_nd_storm_corridor
```

Additional current news basenames:

```text
news_event_nd_regional_floods
news_event_nd_great_rupture
news_event_nd_meteor_showers
news_event_nd_massive_eruption
news_event_nd_disaster_barrage
news_event_nd_avalanche
news_event_nd_glacial_outburst
news_event_nd_sinkhole
news_event_nd_limnic_eruption
```

The accepted deep-family set has no dedicated news file for:

```text
news_event_nd_tornado_outbreak
news_event_nd_ashfall
news_event_nd_lahar
news_event_nd_storm_surge
news_event_nd_meteor_impact
```

Use the standard source/processed/package/live news paths and sprites `GFX_<basename>` in `interface/013_natural_disasters.gfx`.

Visual/provenance cautions from the contact sheets and SHA-256 comparison:

- `news_event_nd_glacial_outburst_source.png` is byte-identical to `news_event_nd_regional_floods_source.png`.
- `news_event_nd_sinkhole_source.png` is byte-identical to `report_event_nd_earthquake_source.png`; the image reads as general urban collapse, not a sinkhole.
- `news_event_nd_avalanche_source.png` is byte-identical to `report_event_nd_landslide_source.png`; there is no snow-specific avalanche identity.
- `news_event_nd_cold_wave_source.png` is byte-identical to `report_event_nd_winter_source.png`; it reads as blizzard/snow clearance rather than prolonged cold exposure.
- `news_event_nd_limnic_eruption` visually reads as a ration/relief queue, not a lake gas-release disaster.
- The singular/plural meteor, global/great rupture, and specific/general massive-eruption pairs are different processed files but create redundant naming and should be assigned explicit, non-overlapping uses or one of each pair should be retired.

These files can remain available, but they should not be counted as unique family coverage without parent approval.

### Decision category pictures

All 22 `decision_cat_picture_nd_*` assets have source PNG, processed `114x101` PNG, package DDS, and live DDS. The contact sheet shows strong readable disaster scenes. They are usable as large left-side category pictures.

Twenty category-picture source PNGs are byte-identical to specific-family news source PNGs. This is consistent with derivative UI art, but contradicts any claim that they are independent newly generated source scenes. The manifest should call them derivatives and list the actual source relationship rather than cite missing source-art handoffs.

Final route:

```text
gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_<family>.dds
```

Sprite pattern: `GFX_decision_cat_picture_nd_<family>` in `interface/013_natural_disasters.gfx`.

### Decision category icons

The 22 `nd_cat_*` icons are technically usable: each has source PNG, processed transparent `53x40` PNG, package DDS, live DDS, and contact-sheet evidence. The art is readable.

They are not accepted as the final category naming scheme. Names such as `*_authority`, `*_office`, `*_board`, `*_bureau`, `*_commission`, and `*_command` conflict with the accepted negative boundary against generic institutional framing. Part 6 and the asset prompt require one Natural Disaster Aftermath category icon, not 22 office/authority categories.

Recommended accepted category asset:

```text
docs/assets/013_natural_disasters/source_png/decision_category_013_natural_disaster_aftermath_source.png
docs/assets/013_natural_disasters/processed_png/decision_category_013_natural_disaster_aftermath.png
docs/assets/013_natural_disasters/dds/decision_category_013_natural_disaster_aftermath.dds
gfx/interface/decisions/013_natural_disasters/decision_category_013_natural_disaster_aftermath.dds
```

Recommended sprite: `GFX_decision_category_013_natural_disaster_aftermath`.

The existing family icon art may be repurposed as family markers after renaming and manifest review, but should not be treated as 22 accepted decision categories.

### Decision icons

Usable accepted-action matches:

| Accepted direction | Current usable asset |
| --- | --- |
| rescue | `decision_nd_rescue_columns` |
| evacuation | `decision_nd_evacuate_shelter` |
| rail repair | `decision_nd_repair_rail` |
| medical corridor | `decision_nd_field_hospitals` |
| winter fuel | `decision_nd_winter_convoys` |

Current related but not exact substitutes:

- `decision_nd_rebuild_ports` is port rebuilding, not pre-impact port closure.
- `decision_nd_firefighting` is active firefighting, not firebreak construction.
- `decision_nd_water_rationing` is rationing, not water-train logistics.
- `decision_nd_seismology_teams` is seismic monitoring, not a general observatory watch for volcano/meteor/tsunami.
- `decision_nd_restore_supply` is general supply restoration, not food relief.
- `decision_nd_clear_debris` is immediate clearing, not long reconstruction.

Required exact additions:

```text
decision_nd_port_closure
decision_nd_food_relief
decision_nd_firebreaks
decision_nd_ash_cleanup
decision_nd_water_trains
decision_nd_observatory_watch
decision_nd_reconstruction
```

Route each through source PNG, processed `32x32` PNG, package DDS, and `gfx/interface/decisions/013_natural_disasters/<name>.dds`; use sprite `GFX_<name>`.

Two current sources violate the icon-type separation rule:

- `decision_nd_field_hospitals_source.png` is byte-identical to `nd_cat_flood_relief_authority_source.png`.
- `decision_nd_rescue_columns_source.png` is byte-identical to `nd_cat_drought_famine_office_source.png`.

The current processed outputs are different sizes, but they still share one source work across decision and category icon types. Before claiming those icons complete, regenerate one side of each pair with an asset-type-specific source.

### Idea and state-modifier icons

Usable current mapping:

| Accepted direction | Current asset |
| --- | --- |
| damaged transport | `idea_013_broken_infrastructure` |
| refugee pressure | `idea_013_refugee_pressure` |
| famine risk | `idea_013_famine_pressure` |

`idea_013_disaster_aftermath` and `idea_013_disaster_recovery_mobilization` are usable extra summary ideas, but do not replace the remaining accepted family/state identities.

Required additions:

```text
idea_013_ashfall
idea_013_disease_risk
idea_013_blocked_ports
idea_013_scorched_state
idea_013_frozen_supply
idea_013_cracked_ground
idea_013_crater_aftermath
```

Route as `64x64` source/processed/package DDS files and final `gfx/interface/ideas/013_natural_disasters/<name>.dds`; use sprite `GFX_<name>`.

### Achievement icons

Current live achievement triplets exist for eight obsolete ids:

```text
013_natural_disasters_aftershock_control
013_natural_disasters_firebreak_master
013_natural_disasters_global_relief
013_natural_disasters_no_deaths_sequence
013_natural_disasters_no_world_end
013_natural_disasters_prepared_capital
013_natural_disasters_skyfall_survivor
013_natural_disasters_tame_the_barrage
```

Each has completed, `_grey`, and `_not_eligible` DDS files. However:

- the accepted Part 6 set contains ten different working ids;
- the achievement-specific prompt lists nine and omits `no_global_announcer`, while the accepted asset prompt explicitly says the renamed no-global-announcer asset is still required;
- no current achievement id exactly matches the accepted source ids;
- individual achievement source PNGs and two source sheets exist, but no individual processed PNGs exist;
- the manifest does not provide one complete entry per achievement with prompt, source, processed path, final triplet, exact id, overlay method, and status;
- `no_world_end` conflicts with the accepted non-terminal Event 013 direction and is not in the accepted achievement set.

Until the parent resolves the nine-versus-ten prompt inconsistency, the source-of-truth Part 6 set should be treated as ten required achievements. Recommended final root-only triplets:

```text
gfx/achievements/013_natural_disasters_after_the_sirens{,_grey,_not_eligible}.dds
gfx/achievements/013_natural_disasters_no_second_wave{,_grey,_not_eligible}.dds
gfx/achievements/013_natural_disasters_every_bridge_counts{,_grey,_not_eligible}.dds
gfx/achievements/013_natural_disasters_ashes_without_famine{,_grey,_not_eligible}.dds
gfx/achievements/013_natural_disasters_no_global_announcer{,_grey,_not_eligible}.dds
gfx/achievements/013_natural_disasters_under_the_falling_sky{,_grey,_not_eligible}.dds
gfx/achievements/013_natural_disasters_shake_the_world_back{,_grey,_not_eligible}.dds
gfx/achievements/013_natural_disasters_disaster_barrage_maximum{,_grey,_not_eligible}.dds
gfx/achievements/013_natural_disasters_not_one_more_camp{,_grey,_not_eligible}.dds
gfx/achievements/013_natural_disasters_catalogue_of_ruin{,_grey,_not_eligible}.dds
```

Source and processed PNGs should use matching `achievement_013_natural_disasters_<slug>_source.png` and `achievement_013_natural_disasters_<slug>.png` names under the Event 013 asset package. The not-eligible variant must be produced from the grey icon with the repository achievement overlay, not an improvised red treatment.

### Super-event images

The four current `457x328` images are visually strong and suitable for their roles:

| Current asset | Accepted role | Result |
| --- | --- | --- |
| `super_event_nd_great_rupture` | whole-earth rupture | Usable. |
| `super_event_nd_massive_eruption` | massive eruption | Usable. |
| `super_event_nd_skyfall` | meteor impact shower/skyfall | Usable. |
| `super_event_nd_storm_corridor` | moving storm corridor with tornado interpretation | Usable only if the route retains tornado funnels; unsuitable for straight-line-wind-only interpretation. |

All four need 32-bit DDS reconversion. `super_event_nd_storm_corridor` also lacks an exact prompt record.

Strict Part 6 gaps:

```text
super_event_nd_abnormal_disaster_age
super_event_nd_delayed_tsunami_chain
```

Route each through:

```text
docs/assets/013_natural_disasters/source_png/<name>_source.png
docs/assets/013_natural_disasters/processed_png/<name>.png
docs/assets/013_natural_disasters/dds/<name>.dds
gfx/super_events/013_natural_disasters/<name>.dds
```

Recommended sprites: `GFX_super_event_nd_abnormal_disaster_age` and `GFX_super_event_nd_delayed_tsunami_chain` in `interface/chaosx_super_events.gfx` after slots are assigned.

The current text-research note recommends only four super-events and rejects delayed tsunami by default. That is a design contradiction with accepted Part 6, not an asset fallback decision. The parent must explicitly promote the four-event interpretation into the source-of-truth spec or retain the two missing image requirements. This audit does not silently drop them.

## Abnormal GUI and animation audit

### Existing five animation packages

All five packages contain genuine drawn state variation visible in their contact sheets; none is a simple byte-duplicate or single-still transform series. Each generated `4x2` animation source sheet was sliced into eight distinct source frames, normalized into eight `36x36` processed frames, assembled into a `288x36` horizontal sheet, and paired with a `36x36` static fallback. No processed-frame hashes are duplicated within a package.

| Asset | Source frames | Processed frames | Sheet/static | GIF evidence | Accepted use assessment |
| --- | --- | --- | --- | --- | --- |
| `natural_disaster_warning_pulse` | 8, roughly `321x317`, RGBA | 8 at `36x36` | `288x36` / `36x36` | 8 frames, `36x36`, 0.96 s, about 8.33 fps | Usable auxiliary warning marker; not a card-frame warning animation. |
| `natural_disaster_storm_corridor_track` | 8, roughly `350x316`, RGBA | 8 at `36x36` | `288x36` / `36x36` | same preview timing | Usable auxiliary family marker; not a `520x24` path ribbon or wide map overlay. |
| `natural_disaster_tsunami_countdown` | 8, roughly `306x341`, RGBA | 8 at `36x36` | `288x36` / `36x36` | same preview timing | Usable auxiliary countdown marker; not the accepted tsunami path/wavefront layer. |
| `natural_disaster_eruption_ashfall` | 8, roughly `293x320`, RGBA | 8 at `36x36` | `288x36` / `36x36` | same preview timing | Usable auxiliary eruption marker; not the accepted `300x190` plume overlay. |
| `natural_disaster_skyfall_alarm` | 8, roughly `296x338`, RGBA | 8 at `36x36` | `288x36` / `36x36` | same preview timing | Usable auxiliary meteor alarm; not the accepted `320x210` meteor-rain overlay. |

### Compliance defects in the five packages

- The brief claims `9 fps`, while each GIF preview encodes `25/3 fps` (about `8.33 fps`). The final `.gfx` value cannot be verified because no sprite definition exists.
- The briefs point their static fallback PNGs to `processed_png/<asset>_static.png`; those paths do not exist. The actual static PNGs are in `animations/<asset>/sheets/`.
- No brief names a static sprite and animated sprite. It only names a suggested `.gfx` file.
- `gfx_handoff.md` contains no animation entries or ready-to-copy `frameAnimatedSpriteType` blocks.
- The manifest does not record per-frame source mode/source note, frame timing, anchor, loop behavior, sheet size, static and animated sprite names, and actual paths in one entry per animation.
- The source-sheet generation directions exist, but exact generation prompts or frame-by-frame prompt deltas are absent.
- The generated sheet was a real animation source, so slicing it is not automatically transform-only. Nevertheless, the package does not meet the stricter per-frame provenance record required by the current skills.
- No target `.gui` element, state flag/value, or verified Chaos Redux/vanilla wiring precedent is recorded.

If retained as auxiliary markers, recommended sprite pairs are:

| Asset | Static sprite | Animated sprite | Target `.gfx` |
| --- | --- | --- | --- |
| `natural_disaster_warning_pulse` | `GFX_013_warning_pulse` | `GFX_013_warning_pulse_animated` | `interface/013_natural_disasters.gfx` |
| `natural_disaster_storm_corridor_track` | `GFX_013_storm_corridor_marker` | `GFX_013_storm_corridor_marker_animated` | same |
| `natural_disaster_tsunami_countdown` | `GFX_013_tsunami_countdown` | `GFX_013_tsunami_countdown_animated` | same |
| `natural_disaster_eruption_ashfall` | `GFX_013_eruption_marker` | `GFX_013_eruption_marker_animated` | same |
| `natural_disaster_skyfall_alarm` | `GFX_013_skyfall_alarm` | `GFX_013_skyfall_alarm_animated` | same |

These proposed names do not satisfy or replace the accepted Part 9 sprite targets below.

### Missing accepted GUI static assets

No current file exists for any of the following Part 9 static targets:

| Required sprite | Recommended final DDS path |
| --- | --- |
| `GFX_013_abnormal_disaster_panel` | `gfx/interface/013_natural_disasters/013_abnormal_disaster_panel.dds` |
| `GFX_013_abnormal_disaster_panel_damaged` | `gfx/interface/013_natural_disasters/013_abnormal_disaster_panel_damaged.dds` |
| `GFX_013_disaster_card_frame` | `gfx/interface/013_natural_disasters/013_disaster_card_frame.dds` |
| `GFX_013_map_marker_impact` | `gfx/interface/013_natural_disasters/013_map_marker_impact.dds` |
| `GFX_013_map_marker_chain_risk` | `gfx/interface/013_natural_disasters/013_map_marker_chain_risk.dds` |
| `GFX_013_foreign_relief_badge` | `gfx/interface/013_natural_disasters/013_foreign_relief_badge.dds` |
| `GFX_013_recovery_progress_frame` | `gfx/interface/013_natural_disasters/013_recovery_progress_frame.dds` |
| `GFX_013_recovery_progress_fill` | `gfx/interface/013_natural_disasters/013_recovery_progress_fill.dds` |

The second-pass asset prompt also requires:

```text
013_motion_lane_normal.dds
013_motion_lane_selected.dds
013_motion_lane_warning.dds
013_motion_lane_completed.dds
013_coming_next_card_normal.dds
013_coming_next_card_urgent.dds
013_coming_next_card_hit.dds
013_coming_next_card_missed.dds
013_recovery_card_rescue.dds
013_recovery_card_stabilization.dds
013_recovery_card_reconstruction.dds
013_recovery_card_foreign_relief.dds
013_recovery_card_blocked_logistics.dds
013_recovery_card_partial_success.dds
```

Route those files to `gfx/interface/013_natural_disasters/` and register sprites `GFX_<basename>` in `interface/013_natural_disasters.gfx`.

### Missing accepted animation families

The accepted Part 9 sprite names and the second-pass target sizes should be combined into these exact deliverables:

| Accepted sprite target | Recommended frame asset basename | Per-frame target | Required outputs |
| --- | --- | ---: | --- |
| `GFX_013_disaster_card_frame_warning_animated` / `GFX_013_disaster_card_frame_warning_static` | `013_disaster_card_frame_warning` | card-frame implementation size | source frames, processed frames, sheet/static PNG+DDS, GIF, contact |
| `GFX_013_disaster_card_frame_impact_animated` / `GFX_013_disaster_card_frame_impact_static` | `013_disaster_card_frame_impact` | card-frame implementation size | same |
| `GFX_013_map_marker_next_hit_animated` / `GFX_013_map_marker_next_hit_static` | `013_impact_pulse_overlay` | `64x64` | same |
| `GFX_013_rupture_wave_sheet` / `GFX_013_rupture_wave_static` | `013_rupture_wave_overlay` | `560x130` | same |
| `GFX_013_meteor_fall_sheet` / `GFX_013_meteor_fall_static` | `013_meteor_rain_overlay` | `320x210` | same |
| `GFX_013_eruption_plume_sheet` / `GFX_013_eruption_plume_static` | `013_ash_plume_overlay` | `300x190` | same |
| `GFX_013_tsunami_train_sheet` / `GFX_013_tsunami_train_static` | `013_tsunami_path_ribbon` | `520x24` | same |
| `GFX_013_storm_corridor_sheet` / `GFX_013_storm_corridor_static` | `013_storm_corridor_path_ribbon` | `520x24` | same |
| additional tornado route layer | `013_tornado_track_ribbon` | `520x24` | same |

Final sheet/static DDS routing:

```text
gfx/interface/animated/013_natural_disasters/<basename>_sheet.dds
gfx/interface/animated/013_natural_disasters/<basename>_static.dds
```

Working packages should live under `docs/assets/013_natural_disasters/animations/<basename>/` with `brief.md`, `frame_plan.md`, `source_frames/`, `processed_frames/`, `sheets/`, and `previews/`. Every handoff must record actual frame count, calculated sheet dimensions, FPS, loop/play-on-show behavior, anchor, source note per frame, target state, sprite pair, target `.gfx`, and target `.gui` element.

## Stale or unsupported documentation claims

The following claims are not supported by the current filesystem and should be corrected only after parent review:

1. `docs/assets/013_natural_disasters/gfx_handoff.md` says the active file is `interface/013_natural_disasters.gfx` and that all sprite names are wired. That file does not exist, and no Event 013 sprite names or texture paths appear in current interface files.
2. The same handoff refers to `interface/013_natural_disasters.gui`; it does not exist.
3. `manifest.md` says the four super-event images are wired through `interface/chaosx_super_events.gfx`; none of their sprite names or texture paths appears there.
4. `manifest.md` calls all five animations complete and links a nonexistent `2026-07-01_event013_animation_alpha_cleanup_handoff.md`.
5. `manifest.md` links nonexistent category-picture and icon-regeneration handoffs under `docs/plans/013_natural_disasters_plans/subagent_handoffs/`.
6. `gfx_handoff.md` has no animation handoff section despite the manifest claiming one exists.
7. Animation briefs give nonexistent static PNG paths under `processed_png/`; the actual files are under each animation's `sheets/` folder.
8. `notes/report_news_validation.md` explicitly validates only 14 reports and 5 broad news images. It does not validate the later 24 specific-family news images, super-event images, icons, achievements, or animations.
9. The manifest's `Complete` heading obscures missing accepted GUI, achievement, super-event, idea, report, decision, and animation coverage.
10. The manifest does not inventory achievements individually and omits their missing processed PNGs.
11. `docs/super_events/013_natural_disasters_super_event_text_research.md` gives old super-event paths without the required `013_natural_disasters/` folder. The actual final paths are under `gfx/super_events/013_natural_disasters/`.
12. The text-research note correctly identifies the missing storm-corridor prompt, but its statement that only four abnormal outcomes are accepted conflicts with the accepted Part 6 six-role table.

## Provenance and rights audit

The package identifies every asset as generated through official `image_gen`; no asset is claimed to be internet-sourced. Therefore third-party archive URLs and licenses are not required for the current files, and no public-domain claim should be added. The correct rights note is that the art is repository-generated and has no third-party source image recorded.

Prompt/provenance coverage is incomplete:

- Exact prompt records exist for all 14 report images, the five broad news images, and three of four super-event images.
- The 24 specific-family news images do not have exact per-asset prompts in the prompt ledger.
- `super_event_nd_storm_corridor` has no exact generation prompt record.
- The 22 category icons have only a group description, not per-asset prompts.
- The 22 category pictures have no independent per-asset prompt record; 20 reuse specific-family news sources.
- The eight achievement sources have only two sheet directions and short labels, not one full per-icon prompt and processing record.
- The five animation source sheets have visual directions but not exact generation prompts or frame-by-frame prompt deltas.
- There are no retained generation result ids or tool-output notes that independently corroborate the source-mode claims.

Source reuse that needs explicit manifest disclosure:

- 20 category-picture sources are byte-identical to specific-family news sources.
- two decision/category icon pairs share byte-identical source PNGs, which is not acceptable icon-type separation.
- avalanche/landslide, cold/winter, glacial-outburst/regional-flood, and sinkhole/earthquake sources are reused across different hazard labels.

These are documentation and asset-identity gaps, not evidence of third-party infringement. Do not invent missing licenses or generation provenance. Recover the real generation prompt/history when available; otherwise regenerate the affected assets and record the new prompt.

## Recommended implementation order for the parent

1. Decide whether accepted Part 6 still requires six super-events or whether the later four-event text recommendation will be promoted into the specs. Do not silently omit the two images.
2. Create the abnormal GUI static pack and large animation overlays before wiring the small `36x36` marker loops.
3. Resolve the achievement source-of-truth conflict and replace the obsolete eight-id triplets with the accepted set, including processed PNGs and overlay provenance.
4. Add the two minimum report images, five missing deep-family news images, seven decision icons, seven idea/modifier icons, and one accepted aftermath category icon.
5. Regenerate the two cross-type duplicated icon sources.
6. Reconvert the nine 24-bit DDS files through the standard 32-bit workflow.
7. Recover or replace missing exact prompt records, especially the storm-corridor super-event, specific-family news, category icons, achievements, and animations.
8. Only then create or update `interface/013_natural_disasters.gfx`, `interface/013_natural_disasters.gui`, and `docs/assets/013_natural_disasters/gfx_handoff.md` from the final names and paths.
9. Replace the manifest's blanket `Complete` presentation with per-asset statuses and retain the byte-identical package/live DDS parity as delivery evidence.

## Simplifications, omissions, and blockers

- No asset was generated, downloaded, converted, renamed, or deleted.
- No manifest or handoff correction was made; all safe-looking documentation corrections are listed above for parent review as requested.
- No gameplay, `.gfx`, `.gui`, localisation, spreadsheet, achievement registry, or super-event slot file was edited.
- No deleted legacy Event 013 or Earth Earthquake implementation was inspected.
- Visual quality was assessed from current processed PNGs and contact sheets. The audit did not reconstruct missing image-generation sessions.
- Completion is blocked by accepted-source conflicts around the super-event count and achievement count/id set. The stricter accepted source-of-truth interpretation is used above so no required art is silently dropped.
