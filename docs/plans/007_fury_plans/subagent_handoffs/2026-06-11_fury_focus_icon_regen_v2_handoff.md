# Fury focus icon regeneration v2 handoff

Date: 2026-06-11

Scope: replace only the eight Fury focus goal DDS files and add the requested asset docs package for this regeneration pass.

## Changed files

Replaced final DDS assets:

- `gfx/interface/goals/fury/goal_fury_war_office.dds`
- `gfx/interface/goals/fury/goal_fury_target_files.dds`
- `gfx/interface/goals/fury/goal_fury_depots.dds`
- `gfx/interface/goals/fury/goal_fury_occupation_registers.dds`
- `gfx/interface/goals/fury/goal_fury_pact.dds`
- `gfx/interface/goals/fury/goal_fury_rivalry.dds`
- `gfx/interface/goals/fury/goal_fury_all_borders.dds`
- `gfx/interface/goals/fury/goal_fury_world_end.dds`

Added asset package:

- `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_war_office_source.png`
- `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_target_files_source.png`
- `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_depots_source.png`
- `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_occupation_registers_source.png`
- `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_pact_source.png`
- `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_rivalry_source.png`
- `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_all_borders_source.png`
- `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_world_end_source.png`
- `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_war_office.png`
- `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_target_files.png`
- `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_depots.png`
- `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_occupation_registers.png`
- `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_pact.png`
- `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_rivalry.png`
- `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_all_borders.png`
- `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_world_end.png`
- `docs/assets/007_fury/focus_icons_regen_v2/fury_focus_icon_contact_sheet.png`
- `docs/assets/007_fury/focus_icons_regen_v2/manifest.md`

## Visual direction used

- Focus icons were regenerated as a distinct asset family from Fury idea icons.
- The set leans on symbolic HOI4-style emblems, fire, border posts, heraldic conflict, and scorched world imagery instead of desk paperwork and official-paper compositions.
- No readable text, modern logos, or UI mockups were used.

## Validation

- Reference focus art was inspected in `.agents/skills/chaos-redux-event-assets/assets/focuses/` before generation and processing.
- `identify` confirmed all eight processed PNG previews are `94x86`.
- `identify` confirmed all eight final DDS files are `94x86`.
- `identify` confirmed processed PNG previews and DDS files preserve transparency (`opaque=false`).
- The contact sheet was visually reviewed for family consistency and for the requested shift away from paper-heavy concepts.

## Blockers

- None.

## Notes

- Current Fury gameplay focus DDS files were not used as source art.
- Fury idea icons were not used as source art.
- The chroma-key helper required Pillow, so a temporary venv was created at `/tmp/fury_focus_venv` to complete alpha cleanup. This did not change repo files.
