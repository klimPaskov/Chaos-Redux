# Fury idea icon regeneration v2 handoff

Date: 2026-06-11

Scope: Fury idea and national-spirit icons only.

## Changed files

Replaced final DDS assets:

- `gfx/interface/ideas/fury/idea_fury_national_fury.dds`
- `gfx/interface/ideas/fury/idea_fury_hardened_fury.dds`
- `gfx/interface/ideas/fury/idea_fury_overextension.dds`
- `gfx/interface/ideas/fury/idea_fury_compliance_drive.dds`
- `gfx/interface/ideas/fury/idea_fury_pact_command.dds`
- `gfx/interface/ideas/fury/idea_fury_rival_doctrine.dds`
- `gfx/interface/ideas/fury/idea_fury_world_in_fury.dds`
- `gfx/interface/ideas/fury/idea_anti_fury_border_watch.dds`
- `gfx/interface/ideas/fury/idea_anti_fury_emergency_aid.dds`
- `gfx/interface/ideas/fury/idea_anti_fury_staff_talks.dds`
- `gfx/interface/ideas/fury/idea_anti_fury_supply_denial.dds`

Added asset package files:

- `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_fury_national_fury_source.png`
- `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_fury_hardened_fury_source.png`
- `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_fury_overextension_source.png`
- `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_fury_compliance_drive_source.png`
- `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_fury_pact_command_source.png`
- `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_fury_rival_doctrine_source.png`
- `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_fury_world_in_fury_source.png`
- `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_anti_fury_border_watch_source.png`
- `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_anti_fury_emergency_aid_source.png`
- `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_anti_fury_staff_talks_source.png`
- `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_anti_fury_supply_denial_source.png`
- `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_fury_national_fury.png`
- `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_fury_hardened_fury.png`
- `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_fury_overextension.png`
- `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_fury_compliance_drive.png`
- `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_fury_pact_command.png`
- `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_fury_rival_doctrine.png`
- `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_fury_world_in_fury.png`
- `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_anti_fury_border_watch.png`
- `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_anti_fury_emergency_aid.png`
- `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_anti_fury_staff_talks.png`
- `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_anti_fury_supply_denial.png`
- `docs/assets/007_fury/idea_icons_regen_v2/fury_idea_icon_contact_sheet.png`
- `docs/assets/007_fury/idea_icons_regen_v2/manifest.md`

## Validation

- Inspected `.agents/skills/chaos-redux-event-assets/assets/ideas` before generation and processing.
- Generated all source art with the built-in `$imagegen` path; no existing Fury DDS or Fury focus icons were used as source art.
- Reprocessed the full set after the first sheet exposed retained green chroma spill on several icons.
- Parent review later found a dark rectangular matte behind the icons; near-black semi-transparent matte pixels were removed, all 11 DDS files were reconverted, and the contact sheet was rebuilt.
- `identify` verified every processed PNG preview is `64x64`.
- `identify` verified every replaced DDS is `64x64`.
- Contact sheet created for all 11 icons and visually checked for a compact HOI4 idea-icon read.
- No `.gfx`, gameplay, localisation, scripts, spreadsheets, decision assets, achievement assets, or focus DDS files were edited.

## Blockers

- None.
