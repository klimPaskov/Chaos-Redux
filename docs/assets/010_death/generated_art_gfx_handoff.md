# Event 010 Death generated-art GFX handoff

These notes were the original `.gfx` handoff. Final wiring has been applied in the implementation files listed below.

## Country flags

- `DTH`
  - Final paths:
    - `gfx/flags/DTH.tga`
    - `gfx/flags/medium/DTH.tga`
    - `gfx/flags/small/DTH.tga`
  - Gameplay use: default Death country flag
  - Use notes: no `.gfx` sprite needed; wire through normal country/cosmetic tag flag usage

- `herald_of_zol`
  - Final paths:
    - `gfx/flags/death_herald_of_zol.tga`
    - `gfx/flags/medium/death_herald_of_zol.tga`
    - `gfx/flags/small/death_herald_of_zol.tga`
  - Gameplay use: Herald of Zol cosmetic route flag
  - Use notes: no `.gfx` sprite needed; stable filename suggestion is `death_herald_of_zol` unless the parent later decides to mirror a cosmetic-tag id exactly

- `black_apostolate`
  - Final paths:
    - `gfx/flags/death_black_apostolate.tga`
    - `gfx/flags/medium/death_black_apostolate.tga`
    - `gfx/flags/small/death_black_apostolate.tga`
  - Gameplay use: Black Apostolate cosmetic hidden-route flag
  - Use notes: no `.gfx` sprite needed; stable filename suggestion is `death_black_apostolate` unless the parent later decides to mirror a cosmetic-tag id exactly

## Leader portrait

- `leader_zol`
  - Final DDS path: `gfx/leaders/010_death/portrait_DTH_zol.dds`
  - Sprite name: `GFX_portrait_DTH_zol`
  - Final `.gfx` file: `interface/chaosx_characters.gfx`
  - Related gameplay use: DTH leader Zol
  - Use notes: portrait reads as nonhuman/ungendered; keep institutional name `Zol`

## Event pictures

- `report_event_death_missing_island`
  - Final DDS path: `gfx/event_pictures/report_event_death_missing_island.dds`
  - Sprite name: `GFX_report_event_death_missing_island`
  - Final `.gfx` file: `interface/chaosx_pictures.gfx`
  - Related gameplay use: impossible shoreline / vanished island report image
  - Use notes: regenerated with a wrong-reading coastline and black surf so the absence reads immediately at HOI4 report size

- `report_event_death_mail_boat`
  - Final DDS path: `gfx/event_pictures/report_event_death_mail_boat.dds`
  - Sprite name: `GFX_report_event_death_mail_boat`
  - Final `.gfx` file: `interface/chaosx_pictures.gfx`
  - Related gameplay use: empty pier/mail boat report image
  - Use notes: regenerated with visible mail sacks, lit cabin, and no crew so the harbor reads as recently abandoned rather than merely quiet

- `report_event_death_lighthouse`
  - Final DDS path: `gfx/event_pictures/report_event_death_lighthouse.dds`
  - Sprite name: `GFX_report_event_death_lighthouse`
  - Final `.gfx` file: `interface/chaosx_pictures.gfx`
  - Related gameplay use: lighthouse/empty settlement report image
  - Use notes: regenerated with a stronger beam and swallowed shoreline silhouette for better report-card readability

- `report_event_death_census`
  - Final DDS path: `gfx/event_pictures/report_event_death_census.dds`
  - Sprite name: `GFX_report_event_death_census`
  - Final `.gfx` file: `interface/chaosx_pictures.gfx`
  - Related gameplay use: abandoned census office report image
  - Use notes: regenerated with shocked officials and wrecked record storage while keeping all papers unreadable

- `news_event_death_mainland_reveal`
  - Final DDS path: `gfx/event_pictures/news_event_death_mainland_reveal.dds`
  - Sprite name: `GFX_news_event_death_mainland_reveal`
  - Final `.gfx` file: `interface/chaosx_pictures.gfx`
  - Related gameplay use: public mainland reveal news image

- `news_event_death_defeated`
  - Final DDS path: `gfx/event_pictures/news_event_death_defeated.dds`
  - Sprite name: `GFX_news_event_death_defeated`
  - Final `.gfx` file: `interface/chaosx_pictures.gfx`
  - Related gameplay use: defeat aftermath news image

## Super-events

- Audit status: `2026-06-15` recheck confirmed exactly five active Death super-event image sprites are wired through `interface/chaosx_super_events.gfx` and `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`, all with final DDS outputs at `457x328`
- Audit note: no additional `Dark Methods` super-event image slot is currently registered; the optional fifth Death-specific route image remains `super_event_death_black_oath`
- Review contact sheet: `docs/assets/010_death/contact_sheets/death_super_events_contact.png`

- `super_event_death_reveal`
  - Final DDS path: `gfx/super_events/super_event_death_reveal.dds`
  - Sprite name: `GFX_super_event_death_reveal`
  - Final `.gfx` file: `interface/chaosx_super_events.gfx`
  - Related gameplay use: mainland reveal super-event

- `super_event_death_world_end`
  - Final DDS path: `gfx/super_events/super_event_death_world_end.dds`
  - Sprite name: `GFX_super_event_death_world_end`
  - Final `.gfx` file: `interface/chaosx_super_events.gfx`
  - Related gameplay use: world-end super-event

- `super_event_death_defeat_aftermath`
  - Final DDS path: `gfx/super_events/super_event_death_defeat_aftermath.dds`
  - Sprite name: `GFX_super_event_death_defeat`
  - Final `.gfx` file: `interface/chaosx_super_events.gfx`
  - Related gameplay use: defeat aftermath super-event

- `super_event_death_world_consumed`
  - Final DDS path: `gfx/super_events/super_event_death_world_consumed.dds`
  - Sprite name: `GFX_super_event_death_world_consumed`
  - Final `.gfx` file: `interface/chaosx_super_events.gfx`
  - Related gameplay use: whole-world-consumed super-event

- `super_event_death_black_oath`
  - Final DDS path: `gfx/super_events/super_event_death_black_oath.dds`
  - Sprite name: `GFX_super_event_death_black_oath`
  - Final `.gfx` file: `interface/chaosx_super_events.gfx`
  - Related gameplay use: Herald oath reveal super-event
  - Use notes: composition is built around a central oath-table scene with restrained supernatural witness behind the officials; no readable text in the sealed document area

## Death Black Atlas UI package

- `death_black_atlas_background`
  - Final DDS path: `gfx/interface/death/black_atlas/death_black_atlas_background.dds`
  - Sprite name: `GFX_death_black_atlas_background`
  - Suggested `.gfx` file: `interface/010_death.gfx`
  - Related gameplay use: Black Atlas main background

- `death_black_atlas_header`
  - Final DDS path: `gfx/interface/death/black_atlas/death_black_atlas_header.dds`
  - Sprite name: `GFX_death_black_atlas_header`
  - Suggested `.gfx` file: `interface/010_death.gfx`
  - Related gameplay use: Black Atlas static header fallback

- `death_black_atlas_header_animated`
  - Final static DDS path: `gfx/interface/death/black_atlas/death_black_atlas_header.dds`
  - Final sheet DDS path: `gfx/interface/death/black_atlas/death_black_atlas_header_animated.dds`
  - Final sheet PNG path: `docs/assets/010_death/animations/death_black_atlas_header/sheets/death_black_atlas_header_sheet.png`
  - Proposed static sprite name: `GFX_death_black_atlas_header`
  - Proposed animated sprite name: `GFX_death_black_atlas_header_animated`
  - Suggested `.gfx` file: `interface/010_death.gfx`
  - Target frame size: `500x36`
  - Calculated sheet size: `4000x36`
  - Frame count: `8`
  - Animation rate: `8 fps`
  - Looping: `yes`
  - `play_on_show`: `yes`
  - Use notes: decorative atlas registry swell; static fallback is safe for non-animated states

- `death_coastal_risk_pulse`
  - Final static DDS path: `gfx/interface/death/black_atlas/death_coastal_risk_pulse_static.dds`
  - Final sheet DDS path: `gfx/interface/death/black_atlas/death_coastal_risk_pulse.dds`
  - Final sheet PNG path: `docs/assets/010_death/animations/death_coastal_risk_pulse/sheets/death_coastal_risk_pulse_sheet.png`
  - Static sprite name: `GFX_death_coastal_risk_pulse_static`
  - Animated sprite name: `GFX_death_coastal_risk_pulse`
  - `.gfx` file: `interface/010_death.gfx`
  - Target frame size: `36x36`
  - Calculated sheet size: `288x36`
  - Frame count: `8`
  - Animation rate: `8 fps`
  - Looping: `yes`
  - `play_on_show`: `yes`
  - Use notes: decorative/state-driven risk marker; static fallback is the lowest-risk ring state

- `death_wither_target_frame`
  - Final static DDS path: `gfx/interface/death/black_atlas/death_wither_target_frame_static.dds`
  - Final sheet DDS path: `gfx/interface/death/black_atlas/death_wither_target_frame.dds`
  - Final sheet PNG path: `docs/assets/010_death/animations/death_wither_target_frame/sheets/death_wither_target_frame_sheet.png`
  - Static sprite name: `GFX_death_wither_target_frame_static`
  - Animated sprite name: `GFX_death_wither_target_frame`
  - `.gfx` file: `interface/010_death.gfx`
  - Target frame size: `36x36`
  - Calculated sheet size: `288x36`
  - Frame count: `8`
  - Animation rate: `8 fps`
  - Looping: `yes`
  - `play_on_show`: `yes`
  - Use notes: decorative/state-driven target frame; static fallback is the dormant bracket state

- `death_compact_warning_pulse`
  - Final static DDS path: `gfx/interface/death/black_atlas/death_compact_warning_pulse_static.dds`
  - Final sheet DDS path: `gfx/interface/death/black_atlas/death_compact_warning_pulse.dds`
  - Final sheet PNG path: `docs/assets/010_death/animations/death_compact_warning_pulse/sheets/death_compact_warning_pulse_sheet.png`
  - Static sprite name: `GFX_death_compact_warning_pulse_static`
  - Animated sprite name: `GFX_death_compact_warning_pulse`
  - `.gfx` file: `interface/010_death.gfx`
  - Target frame size: `36x36`
  - Calculated sheet size: `288x36`
  - Frame count: `8`
  - Animation rate: `8 fps`
  - Looping: `yes`
  - `play_on_show`: `yes`
  - Use notes: decorative/state-driven compact warning pulse; static fallback is the dim seal state

## Expanded focus lane icons

- The expanded Death focus tree is wired through `interface/010_death.gfx`.
- All active focus sprites have stable final ids, source PNGs, processed PNGs, and final DDS files.
- The regenerated pass standardizes the entire Death focus family at `100x88` with transparent outer alpha and HOI4-style badge framing. Existing sprite names and texture paths remain valid, so no `.gfx` edit is required for this art pass.
- Contact sheet: `docs/assets/010_death/contact_sheets/death_focus_icons_contact.png`
- Final files:
  - `gfx/interface/goals/death/focus_death_the_first_silence.dds`
  - `gfx/interface/goals/death/focus_death_country_on_the_island.dds`
  - `gfx/interface/goals/death/focus_death_shroud_whispers.dds`
  - `gfx/interface/goals/death/focus_death_no_mail_before_spring.dds`
  - `gfx/interface/goals/death/focus_death_weather_on_paper.dds`
  - `gfx/interface/goals/death/focus_death_island_pattern.dds`
  - `gfx/interface/goals/death/focus_death_hunger_shore.dds`
  - `gfx/interface/goals/death/focus_death_lowest_names_first.dds`
  - `gfx/interface/goals/death/focus_death_ports_without_voices.dds`
  - `gfx/interface/goals/death/focus_death_mainland_smell.dds`
  - `gfx/interface/goals/death/focus_death_black_census.dds`
  - `gfx/interface/goals/death/focus_death_no_graves_needed.dds`
  - `gfx/interface/goals/death/focus_death_first_ghost_muster.dds`
  - `gfx/interface/goals/death/focus_death_public_death.dds`
  - `gfx/interface/goals/death/focus_death_tide_learns_roads.dds`
  - `gfx/interface/goals/death/focus_death_another_shoreline.dds`
  - `gfx/interface/goals/death/focus_death_no_ferry_returns.dds`
  - `gfx/interface/goals/death/focus_death_wasteland_roads.dds`
  - `gfx/interface/goals/death/focus_death_every_road_slows.dds`
  - `gfx/interface/goals/death/focus_death_empty_supply.dds`
  - `gfx/interface/goals/death/focus_death_state_without_state.dds`
  - `gfx/interface/goals/death/focus_death_mourning_host.dds`
  - `gfx/interface/goals/death/focus_death_ruin_host.dds`
  - `gfx/interface/goals/death/focus_death_orders_without_breath.dds`
  - `gfx/interface/goals/death/focus_death_last_shores.dds`
  - `gfx/interface/goals/death/focus_death_world_consumed.dds`

## Route achievement and idea icons

- `GFX_achievement_death_friend_of_zol`
  - Final paths: `gfx/achievements/death_friend_of_zol.dds`, `gfx/achievements/death_friend_of_zol_grey.dds`, `gfx/achievements/death_friend_of_zol_not_eligible.dds`
  - `.gfx` file: `interface/chaosx_achievements.gfx`
- `GFX_achievement_death_book_burner`
  - Final paths: `gfx/achievements/death_book_burner.dds`, `gfx/achievements/death_book_burner_grey.dds`, `gfx/achievements/death_book_burner_not_eligible.dds`
  - `.gfx` file: `interface/chaosx_achievements.gfx`
- `GFX_achievement_death_black_apostolate`
  - Final paths: `gfx/achievements/death_black_apostolate.dds`, `gfx/achievements/death_black_apostolate_grey.dds`, `gfx/achievements/death_black_apostolate_not_eligible.dds`
  - `.gfx` file: `interface/chaosx_achievements.gfx`
- `GFX_idea_death_black_book_offices`
  - Final path: `gfx/interface/ideas/death/idea_black_book_offices.dds`
  - `.gfx` file: `interface/chaosx_ideas.gfx`
- `GFX_idea_death_black_oath`
  - Final path: `gfx/interface/ideas/death/idea_black_oath.dds`
  - `.gfx` file: `interface/chaosx_ideas.gfx`
- `GFX_idea_death_public_death`
  - Final path: `gfx/interface/ideas/death/idea_public_death.dds`
  - Processed PNG: `docs/assets/010_death/processed_png/idea_public_death.png`
  - Source PNG: `docs/assets/010_death/source_png/idea_public_death_source.png`
  - Target size: `64x64`
  - `.gfx` file: `interface/chaosx_ideas.gfx`
  - Use notes: fully regenerated as an official public notice or bulletin sheet with a void-black seal and dead-coast public-recognition motif; existing registered path remains valid and no `.gfx` edit is required

## Registered animated portrait

- `leader_zol_world_end_animated`
  - Final static DDS path: `gfx/leaders/010_death/portrait_DTH_zol_world_end.dds`
  - Final sheet DDS path: `gfx/leaders/010_death/portrait_DTH_zol_world_end_animated.dds`
  - Final sheet PNG path: `docs/assets/010_death/animations/portrait_DTH_zol_world_end/sheets/portrait_DTH_zol_world_end_sheet.png`
  - Source frames: `docs/assets/010_death/source_png/portrait_DTH_zol_world_end_frame_00_source.png` through `docs/assets/010_death/source_png/portrait_DTH_zol_world_end_frame_07_source.png`
  - Processed frames: `docs/assets/010_death/processed_png/portrait_DTH_zol_world_end_frame_00.png` through `docs/assets/010_death/processed_png/portrait_DTH_zol_world_end_frame_07.png`
  - Contact/preview: `docs/assets/010_death/contact_sheets/portrait_DTH_zol_world_end_contact.png`, `docs/assets/010_death/previews/portrait_DTH_zol_world_end_preview.gif`
  - Registered static sprite name: `GFX_portrait_DTH_zol_world_end`
  - Registered animated sprite name: `GFX_portrait_DTH_zol_world_end_animated`
  - `.gfx` file: `interface/chaosx_characters.gfx`
  - Target frame size: `156x210`
  - Calculated sheet size: `1248x210`
  - Frame count: `8`
  - Animation rate: `4 fps`
  - Looping: `yes`
  - `play_on_show`: `yes`
  - Local precedent: mirrors the existing `frameAnimatedSpriteType` portrait pattern already used for `GFX_portrait_THR_buddha_mandate_animated` and `GFX_portrait_THR_empty_seat_animated`
  - Use notes: static fallback remains the existing unchanged portrait and is applied to Zol at world-end; portrait reads as nonhuman/ungendered and should keep institutional name `Zol`; rebuilt animation is eyes-glow-only with no composition drift; validation confirmed all frames are `156x210`, the final sheet is `1248x210`, the preview loop stays subtle, and no parent `.gfx` update is needed because the registered 8-frame 4 FPS setup still matches the rebuilt sheet

## Export note

- The repository helper `.tools/convert_to_dds.py` failed in this environment on its FFmpeg fallback path. Final DDS files above were exported with ImageMagick `convert -define dds:compression=none`, and file dimensions were verified afterward.
