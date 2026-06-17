# Event 012 Africa GFX Handoff

All names in this file were proposed because no parent-provided sprite names or texture paths were supplied.

## Parent wiring update, 2026-06-17

The main implementation wires the three animated packages through `interface/012_africa.gfx` and `interface/012_africa_scripted_gui.gui`.

- Animated sprites:
  - `GFX_africa_authority_atlas_seal_loop`
  - `GFX_africa_charter_league_banner_pulse`
  - `GFX_africa_bestiary_warning_loop`
- Static fallbacks:
  - `GFX_africa_authority_atlas_seal_static` -> `gfx/interface/animated/012_africa/authority_atlas_seal_loop_fallback_128x128.dds`
  - `GFX_africa_charter_league_banner_static` -> `gfx/interface/animated/012_africa/charter_league_banner_pulse_fallback_160x96.dds`
  - `GFX_africa_bestiary_warning_static` -> `gfx/interface/animated/012_africa/bestiary_warning_loop_fallback_96x96.dds`

The Continental Congress panel shows fallback sprites underneath route-gated animated overlays for the Charter banner, Authority Atlas seal, and Bestiary warning seal.

## Suggested static texture wiring

- Put the static icon DDS files from `docs/assets/012_africa/icons_animation/dds/` into the final mod icon folders chosen by the parent agent.
- Suggested shared `.gfx`: `interface/012_africa_icons.gfx`
- Suggested sprite pattern:
  - `GFX_focus_africa_*`
  - `GFX_idea_africa_*`
  - `GFX_decision_category_africa_*`

## Suggested UI seal wiring

- Suggested `.gfx`: `interface/012_africa_ui_seals.gfx`
- Suggested sprites:
  - `GFX_africa_visible_values_ui_seal`
  - `GFX_africa_authority_atlas_ui_seal`

## Suggested achievement wiring

- Suggested `.gfx`: `interface/012_africa_achievements.gfx`
- Suggested sprites:
  - `GFX_achievement_africa_unification`
  - `GFX_achievement_africa_unification_grey`
  - `GFX_achievement_africa_unification_not_eligible`
  - `GFX_achievement_africa_archive`
  - `GFX_achievement_africa_archive_grey`
  - `GFX_achievement_africa_archive_not_eligible`

## Suggested animated sprite wiring

- Suggested `.gfx`: `interface/012_africa_animated_icons.gfx`
- Suggested `frameAnimatedSpriteType` entries:
  - `GFX_africa_authority_atlas_seal_anim`
    - texture file: `authority_atlas_seal_loop_sheet.dds`
    - `noOfFrames = 4`
    - `animation_rate_fps = 8`
    - `looping = yes`
    - `play_on_show = yes`
  - `GFX_africa_charter_league_banner_anim`
    - texture file: `charter_league_banner_pulse_sheet.dds`
    - `noOfFrames = 4`
    - `animation_rate_fps = 8`
    - `looping = yes`
    - `play_on_show = yes`
  - `GFX_africa_bestiary_warning_anim`
    - texture file: `bestiary_warning_loop_sheet.dds`
    - `noOfFrames = 4`
    - `animation_rate_fps = 10`
    - `looping = yes`
    - `play_on_show = yes`

## Static fallbacks for animated uses

- `GFX_africa_authority_atlas_seal_static` -> `authority_atlas_seal_loop_fallback_128x128.dds`
- `GFX_africa_charter_league_banner_static` -> `charter_league_banner_pulse_fallback_160x96.dds`
- `GFX_africa_bestiary_warning_static` -> `bestiary_warning_loop_fallback_96x96.dds`

## Review previews

- Static contact sheet: `previews/all_static_sources_contact_sheet.png`
- Idea contact sheet: `previews/idea_64x64_contact_sheet.png`
- Focus contact sheet: `previews/focus_94x86_contact_sheet.png`
- Decision-category contact sheet: `previews/decision_category_32x32_contact_sheet.png`
- Animation contact sheets and GIF previews live beside the corresponding frame sheets in `previews/`
