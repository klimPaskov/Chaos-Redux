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

## Leader portrait

- `leader_zol`
  - Final DDS path: `gfx/leaders/010_death/portrait_DTH_zol.dds`
  - Sprite name: `GFX_portrait_DTH_zol`
  - Final `.gfx` file: `interface/chaosx_characters.gfx`
  - Related gameplay use: DTH leader Zol
  - Use notes: portrait reads as nonhuman/ungendered; keep institutional name `Zol`

## Event pictures

- `report_event_death_mail_boat`
  - Final DDS path: `gfx/event_pictures/report_event_death_mail_boat.dds`
  - Sprite name: `GFX_report_event_death_mail_boat`
  - Final `.gfx` file: `interface/chaosx_pictures.gfx`
  - Related gameplay use: empty pier/mail boat report image

- `report_event_death_lighthouse`
  - Final DDS path: `gfx/event_pictures/report_event_death_lighthouse.dds`
  - Sprite name: `GFX_report_event_death_lighthouse`
  - Final `.gfx` file: `interface/chaosx_pictures.gfx`
  - Related gameplay use: lighthouse/empty settlement report image

- `report_event_death_census`
  - Final DDS path: `gfx/event_pictures/report_event_death_census.dds`
  - Sprite name: `GFX_report_event_death_census`
  - Final `.gfx` file: `interface/chaosx_pictures.gfx`
  - Related gameplay use: abandoned census office report image

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

## Expanded focus lane placeholders

- The expanded Death focus tree is wired through `interface/010_death.gfx`.
- These focus sprites have stable final ids and load-safe DDS files, but several are copied placeholders from the first Death icon package and should be replaced by bespoke lane art when available.
- Replacement files should keep the current paths:
  - `gfx/interface/goals/death/focus_death_the_first_silence.dds`
  - `gfx/interface/goals/death/focus_death_country_on_the_island.dds`
  - `gfx/interface/goals/death/focus_death_no_mail_before_spring.dds`
  - `gfx/interface/goals/death/focus_death_weather_on_paper.dds`
  - `gfx/interface/goals/death/focus_death_island_pattern.dds`
  - `gfx/interface/goals/death/focus_death_lowest_names_first.dds`
  - `gfx/interface/goals/death/focus_death_ports_without_voices.dds`
  - `gfx/interface/goals/death/focus_death_mainland_smell.dds`
  - `gfx/interface/goals/death/focus_death_no_graves_needed.dds`
  - `gfx/interface/goals/death/focus_death_first_ghost_muster.dds`
  - `gfx/interface/goals/death/focus_death_public_death.dds`
  - `gfx/interface/goals/death/focus_death_tide_learns_roads.dds`
  - `gfx/interface/goals/death/focus_death_another_shoreline.dds`
  - `gfx/interface/goals/death/focus_death_no_ferry_returns.dds`
  - `gfx/interface/goals/death/focus_death_every_road_slows.dds`
  - `gfx/interface/goals/death/focus_death_empty_supply.dds`
  - `gfx/interface/goals/death/focus_death_state_without_state.dds`
  - `gfx/interface/goals/death/focus_death_ruin_host.dds`
  - `gfx/interface/goals/death/focus_death_orders_without_breath.dds`

## Blocked optional assets

- `leader_zol_world_end_animated`: no final sheet/static package produced; missing approved animation brief inputs and target surface
- `herald_of_zol`, `black_apostolate`, `super_event_death_black_oath`: route implementation not confirmed by prompt
- `death_black_atlas_*`: missing exact target sizes, final paths, and target GUI surface/wiring

## Export note

- The repository helper `.tools/convert_to_dds.py` failed in this environment on its FFmpeg fallback path. Final DDS files above were exported with ImageMagick `convert -define dds:compression=none`, and file dimensions were verified afterward.
