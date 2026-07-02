# Event 014 Cannibalism Asset Manifest

This manifest is the top-level asset map for Event 014. Final Event 014 visual assets are generated fictional art produced through imagegen source packages, then processed into HOI4 DDS/TGA outputs. Local processing only crops, removes chroma-key backgrounds, resizes, assembles frame sheets or contact sheets, and converts formats.

## Protected Portrait

- Protected file: `gfx/leaders/014_cannibalism/hannibal.dds`
- Expected SHA256: `5C48C9A5B503C3185DCB38EE1AABC403D7668094079B78A20010323930D10B88`
- Rule: do not overwrite this file during Event 014 asset regeneration. It is the restored original Hannibal portrait.

## Source Packages

- Non-icon report, news, super-event, flag, and leader/council artwork: `docs/assets/014_cannibalism/generated_art_sources/generated_art_manifest.md`
- Decision, decision-category, and decision-picture icons: `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/manifest.md`
- Ideas: `docs/assets/014_cannibalism/static_icons_imagegen/ideas/manifest.json`
- Achievements: `docs/assets/014_cannibalism/static_icons_imagegen/achievements/manifest.md`
- Opening focus icons: `docs/assets/014_cannibalism/static_icons_imagegen/focuses_core_opening/manifest.md`
- Command and military focus icons: `docs/assets/014_cannibalism/static_icons_imagegen/focuses_command_military/validation/focuses_command_military_validation.tsv`
- Island, pact, and Last Table focus icons: `docs/assets/014_cannibalism/static_icons_imagegen/focuses_islands_pact_last_table/manifest.md`
- Animated scripted-GUI pieces and static fallbacks: `docs/assets/014_cannibalism/animations_imagegen/manifest.md`

## Live Output Folders

- Event/news pictures: `gfx/event_pictures/014_cannibalism/`
- Super-event pictures: `gfx/super_events/014_cannibalism/`
- CBL flags: `gfx/flags/`
- Decision icons: `gfx/interface/decisions/014_cannibalism/`
- Idea icons: `gfx/interface/ideas/014_cannibalism/`
- Focus icons: `gfx/interface/goals/014_cannibalism/`
- Achievement icons: `gfx/achievements/`
- Animated scripted-GUI DDS sheets and static fallbacks: `gfx/interface/animated/014_cannibalism/`
- Generated CBL table-council portrait: `gfx/leaders/014_cannibalism/CBL_table_council.dds`

## Wiring

- Event/news/report sprites: `interface/chaosx_pictures.gfx`
- Event decision, focus, idea, achievement, and animation sprites: `interface/014_cannibalism.gfx`
- Achievement sprite registration: `interface/chaosx_achievements.gfx`
- Animated GUI layout: `interface/014_cannibalism_frontline_hunger.gui`
- Animated GUI visibility: `common/scripted_guis/014_cannibalism_scripted_gui.txt`

## Imagegen Compliance

The live Event 014 asset set does not use primitive-shape, deterministic PIL, local procedural drawing, placeholder chart, CSS/SVG-only, contact-sheet-strip, or transform-only final art. Animation finals are built from separate imagegen source frames with sheet DDS files, static fallback DDS files, GIF previews, and contact sheets.

The superseded procedural animation DDS files `cannibalism_table_pulse_*`, `cannibalism_warning_larder_*`, and `cannibalism_signal_map_*` were removed after the imagegen animation set was wired.
