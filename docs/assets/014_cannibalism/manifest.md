# Event 014 Cannibalism Asset Manifest

This manifest is the top-level asset map for Event 014. Final Event 014 visual assets are generated fictional art produced through imagegen source packages, then processed into HOI4 DDS/TGA outputs. Local processing only crops, removes chroma-key backgrounds, resizes, assembles frame sheets or contact sheets, and converts formats.

This file and its linked package manifests supersede the 2026-07-11 live gap map and remaining-static ledger as current asset truth. Historical handoffs retain their checkpoint status and are not rewritten.

## Protected Legacy Portrait

- Protected file: `gfx/leaders/014_cannibalism/hannibal.dds`
- Expected SHA256: `5C48C9A5B503C3185DCB38EE1AABC403D7668094079B78A20010323930D10B88`
- Rule: do not overwrite this archival file during Event 014 asset regeneration. It is not registered by the live Event 014 interface. The accepted animated reveal package uses `leader_CBL_hannibal_static.dds` and `leader_CBL_hannibal_sheet.dds`.

## Source Packages

- Historical generated-art source/processed provenance: `docs/assets/014_cannibalism/generated_art_sources/generated_art_manifest.md`. This archival ledger does not own live runtime paths; its retained selections are promoted through the current packages below.
- Frozen 13-family flag package, selected source sheets, 65 source crops, 195 live TGAs, prompt provenance, contact sheets, validation, and hashes: `docs/assets/014_cannibalism/flags_imagegen/manifest.md`
- Accepted 56-portrait feral regional matrix and provenance: `docs/assets/014_cannibalism/warlord_portraits_imagegen/manifest.md` and `docs/plans/014_cannibalism_plans/014_warlord_regional_portrait_repair.md`. Europe, Asia, Africa, the Middle East, North America, South America, and Oceania each have eight distinct slot portraits.
- Four-super-event kinetic action regeneration: `docs/assets/014_cannibalism/static_event_art_imagegen/`. The former static tableau images are superseded.
- Independently generated ordinary and Wendigo reveal-portrait frames, sheets, fallbacks, previews, and handoff: `docs/assets/014_cannibalism/gui_animation_portraits/`.
- Decision, decision-category, and decision-picture icons: `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/manifest.md`
- Ideas: `docs/assets/014_cannibalism/static_icons_imagegen/ideas/manifest.json`
- Achievements: `docs/assets/014_cannibalism/achievements_imagegen/manifest.md`
- Opening focus icons: `docs/assets/014_cannibalism/static_icons_imagegen/focuses_core_opening/manifest.md`
- Command and military focus icons: `docs/assets/014_cannibalism/static_icons_imagegen/focuses_command_military/validation/focuses_command_military_validation.tsv`
- Island, pact, and Last Table focus icons: `docs/assets/014_cannibalism/static_icons_imagegen/focuses_islands_pact_last_table/manifest.md`
- Accepted animated portraits, scripted-GUI pieces, sheets, and static fallbacks: `docs/assets/014_cannibalism/gui_animation_portraits/manifest.md`
- Retired six-experiment animation source provenance only: `docs/assets/014_cannibalism/animations_imagegen/manifest.md`
- Final 21-surface objective, tracker, hunt, Pack-receipt, and inherited-cell closure package: `docs/assets/014_cannibalism/static_icons_imagegen/closure_2026-07-12/manifest.md`

## Live Output Folders

- Event/news pictures: `gfx/event_pictures/014_cannibalism/`
- Super-event pictures: `gfx/super_events/014_cannibalism/` (four kinetic action scenes: public reveal, ordinary world end, global defeat, and Wendigo world end)
- Event 014 CBA-CBH, CBL route, and public Hannibal cosmetic flags: `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`
- Decision icons: `gfx/interface/decisions/014_cannibalism/`
- Idea icons: `gfx/interface/ideas/014_cannibalism/`
- Focus icons: `gfx/interface/goals/014_cannibalism/`
- Achievement icons: `gfx/achievements/`
- Animated scripted-GUI DDS sheets and static fallbacks: `gfx/interface/animated/014_cannibalism/`
- Accepted ordinary and transformed Hannibal portrait sheets/fallbacks: `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds`, `gfx/leaders/014_cannibalism/leader_CBL_hannibal_static.dds`, `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds`, and `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_static.dds`
- Accepted CBA-CBH European feral portraits: `gfx/leaders/014_cannibalism/leader_CBA_warlord.dds` through `leader_CBH_warlord.dds`
- Accepted regional runtime variants: `gfx/leaders/014_cannibalism/leader_<SLOT>_warlord_<REGION>.dds` for six non-European regions across eight slots. Together with Europe this is the complete 56-portrait matrix

## Wiring

- Event/news/report sprites: `interface/chaosx_pictures.gfx`
- Event decision, focus, idea, portrait, and animation sprites: `interface/014_cannibalism.gfx`
- Achievement sprite registration: `interface/014_cannibalism_achievements.gfx`
- Animated GUI layout: `interface/014_cannibalism_frontline_hunger.gui`
- Animated GUI visibility: `common/scripted_guis/014_cannibalism_scripted_gui.txt`
- CBA-CBH portrait sprite and character handoff: `docs/assets/014_cannibalism/warlord_portraits_imagegen/gfx_handoff.md`

## Imagegen Compliance

The live Event 014 asset set does not use primitive-shape, deterministic PIL, local procedural drawing, placeholder chart, CSS/SVG-only, contact-sheet-strip, or transform-only final art. Animation finals are built from separate imagegen source frames with sheet DDS files, static fallback DDS files, GIF previews, and contact sheets.

The final GFX closure scan found 816 Event 014 texture references across nine `.gfx` files, 598 unique texture paths, and zero missing runtime files. The two leader animations contain 12 ordinary and 16 transformed independently generated source frames.

The superseded procedural animation DDS files `cannibalism_table_pulse_*`, `cannibalism_warning_larder_*`, and `cannibalism_signal_map_*` were removed after the imagegen animation set was wired.

The fourteen unregistered report/news textures from the superseded broad scene contract were removed from the runtime folder on 2026-07-12. Their generated source packages remain as historical provenance only. Every live Event 014 report/news DDS now has an exact registered sprite and current scene assignment.

Nineteen unregistered and unreferenced idea DDS files from an earlier naming pass were removed from the runtime folder on 2026-07-12. The live idea folder now contains only sprites registered in `interface/014_cannibalism.gfx`. The accepted 27-idea imagegen package remains the source of truth.
