# Fury focus icon regeneration v2 manifest

Date: 2026-06-11

Status: converted and ready for parent review.

Scope: regenerate only the eight Fury focus goal icons with a more symbolic, painterly, HOI4-style family. This pass keeps the existing DDS filenames and target dimensions unchanged and does not require `.gfx` edits.

## Package paths

- Source PNGs: `docs/assets/007_fury/focus_icons_regen_v2/source_png/`
- Processed PNG previews: `docs/assets/007_fury/focus_icons_regen_v2/processed_png/`
- Contact sheet: `docs/assets/007_fury/focus_icons_regen_v2/fury_focus_icon_contact_sheet.png`
- Final DDS files: `gfx/interface/goals/fury/`

## Source mode

- Source mode: generated
- Generation tool: built-in `image_gen`
- Transparency workflow: flat `#00ff00` chroma-key background removed locally with `remove_chroma_key.py`, then cropped and normalized to `94x86`
- Local DDS conversion: `convert -define dds:compression=none`

## Final assets

| Goal DDS | Source PNG | Processed PNG | Final DDS | Prompt/source mode | Notes |
| --- | --- | --- | --- | --- | --- |
| `goal_fury_war_office.dds` | `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_war_office_source.png` | `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_war_office.png` | `gfx/interface/goals/fury/goal_fury_war_office.dds` | generated; black command case, bronze dagger, crossed batons, furnace fire | Stronger war-office emblem, avoids paperwork stack look. |
| `goal_fury_target_files.dds` | `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_target_files_source.png` | `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_target_files.png` | `gfx/interface/goals/fury/goal_fury_target_files.dds` | generated; scorched map disk inside iron gunsight | Targeting reads symbolically without relying on dossiers or readable documents. |
| `goal_fury_depots.dds` | `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_depots_source.png` | `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_depots.png` | `gfx/interface/goals/fury/goal_fury_depots.dds` | generated; burning depot crate with fire bursting from one side | Kept one clear central supply object with stronger flame silhouette. |
| `goal_fury_occupation_registers.dds` | `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_occupation_registers_source.png` | `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_occupation_registers.png` | `gfx/interface/goals/fury/goal_fury_occupation_registers.dds` | generated; iron registry stamp branding a glowing town-grid seal | Occupation/control idea kept symbolic rather than document-heavy. |
| `goal_fury_pact.dds` | `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_pact_source.png` | `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_pact.png` | `gfx/interface/goals/fury/goal_fury_pact.dds` | generated; clasped gauntlets over crossed sabres and wreath | Alliance emblem separated clearly from rivalry. |
| `goal_fury_rivalry.dds` | `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_rivalry_source.png` | `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_rivalry.png` | `gfx/interface/goals/fury/goal_fury_rivalry.dds` | generated; split opposing war crests with crossed maces | More hostile heraldic composition than the pact icon. |
| `goal_fury_all_borders.dds` | `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_all_borders_source.png` | `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_all_borders.png` | `gfx/interface/goals/fury/goal_fury_all_borders.dds` | generated; scorched globe ringed by border posts and frontier markers | Emphasizes encirclement and frontier control. |
| `goal_fury_world_end.dds` | `docs/assets/007_fury/focus_icons_regen_v2/source_png/goal_fury_world_end_source.png` | `docs/assets/007_fury/focus_icons_regen_v2/processed_png/goal_fury_world_end.png` | `gfx/interface/goals/fury/goal_fury_world_end.dds` | generated; cracked globe collapsing into a flaming skull | Most extreme icon in the family; uses skull/fire imagery requested by parent prompt. |

## Validation

- `identify` confirmed all processed PNG previews are `94x86`.
- `identify` confirmed all final DDS files are `94x86`.
- `identify` confirmed processed PNG previews and final DDS files are `opaque=false`.
- Contact sheet created to compare all eight regenerated focus icons side by side.
- No `.gfx`, gameplay, localisation, script, spreadsheet, achievement, idea, or decision files were edited in this package.

## Notes

- The current Fury focus DDS files were not used as source art.
- Fury idea icons were not used as source art.
- One local setup step was required: a temporary venv at `/tmp/fury_focus_venv` was created to provide Pillow for the chroma-key helper.
