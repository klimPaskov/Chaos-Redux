# Fury decision icon regeneration v2 manifest

Date: 2026-06-11

Status: converted and ready for parent review.

Scope: regenerate only the Fury decision and decision-category icons as a distinct decision-style asset family. This pass keeps all existing DDS filenames and target dimensions unchanged and does not require `.gfx` edits.

## Package paths

- Source PNGs: `docs/assets/007_fury/decision_icons_regen_v2/source_png/`
- Processed PNG previews: `docs/assets/007_fury/decision_icons_regen_v2/processed_png/`
- Contact sheet: `docs/assets/007_fury/decision_icons_regen_v2/fury_decision_icon_contact_sheet.png`
- Final DDS files: `gfx/interface/decisions/fury/`

## Source mode

- Source mode: generated
- Generation tool: built-in `image_gen`
- Reference inspection: `.agents/skills/chaos-redux-event-assets/assets/decisions/`
- Transparency workflow: flat `#00ff00` chroma-key background removed locally with `remove_chroma_key.py`, then cropped and normalized to `32x32` or `52x40`
- Local DDS conversion: `convert -define dds:compression=none`

## Final assets

| DDS file | Source PNG | Processed PNG | Final DDS | Prompt/source mode | Notes |
| --- | --- | --- | --- | --- | --- |
| `decision_category_fury_war_office.dds` | `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_category_fury_war_office_source.png` | `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_category_fury_war_office.png` | `gfx/interface/decisions/fury/decision_category_fury_war_office.dds` | generated; iron stamp over burning frontier plaque with crossed command batons | Wider decision-category emblem, active war-office symbol, avoids paperwork-only framing. |
| `decision_category_anti_fury.dds` | `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_category_anti_fury_source.png` | `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_category_anti_fury.png` | `gfx/interface/decisions/fury/decision_category_anti_fury.dds` | generated; anti-Fury shield with firebreak band and turned-back front arrows | Defensive category read built from one compact emblem rather than a full scene. |
| `decision_fury_target.dds` | `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_fury_target_source.png` | `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_fury_target.png` | `gfx/interface/decisions/fury/decision_fury_target.dds` | generated; black target reticle over burning border fragment | Strong central silhouette tuned for 32x32 and distinct from focus-icon composition. |
| `decision_fury_depots.dds` | `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_fury_depots_source.png` | `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_fury_depots.png` | `gfx/interface/decisions/fury/decision_fury_depots.dds` | generated; heavy supply crate with fire bursting from one side | Kept to one supply object with flame accent for quick recognition. |
| `decision_fury_settlement.dds` | `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_fury_settlement_source.png` | `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_fury_settlement.png` | `gfx/interface/decisions/fury/decision_fury_settlement.dds` | generated; red settlement seal over captured ground | Compact occupation/settlement read without shrinking a larger focus-style scene. |
| `decision_fury_coring.dds` | `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_fury_coring_source.png` | `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_fury_coring.png` | `gfx/interface/decisions/fury/decision_fury_coring.dds` | generated; brutal branding stamp over scorched territorial mark | Uses the requested branding motif to read as coring at icon size. |
| `decision_fury_terminal_reserves.dds` | `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_fury_terminal_reserves_source.png` | `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_fury_terminal_reserves.png` | `gfx/interface/decisions/fury/decision_fury_terminal_reserves.dds` | generated; reserve crate with skull insignia | Dark reserve/final-stockpile read kept to one blunt container shape. |
| `decision_fury_terminal_fronts.dds` | `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_fury_terminal_fronts_source.png` | `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_fury_terminal_fronts.png` | `gfx/interface/decisions/fury/decision_fury_terminal_fronts.dds` | generated; three aggressive front arrows on armored plate | Simple offensive arrow family intended to stay legible at 32x32. |
| `decision_anti_fury_response.dds` | `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_anti_fury_response_source.png` | `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_anti_fury_response.png` | `gfx/interface/decisions/fury/decision_anti_fury_response.dds` | generated; anti-Fury shield with diagonal firebreak through flames | Readable defensive counter-symbol with high contrast and limited detail. |

## Validation

- `identify` confirmed all processed PNG previews exist at the expected dimensions:
  - Decision category icons: `52x40`
  - Ordinary decision icons: `32x32`
- `identify` confirmed all final DDS files exist at the expected dimensions:
  - Decision category icons: `52x40`
  - Ordinary decision icons: `32x32`
- `identify` confirmed processed PNG previews and final DDS files preserve transparency (`opaque=false`).
- The contact sheet was visually reviewed for decision-style family consistency, strong silhouette, and the requested shift away from focus-icon composition.
- No `.gfx`, gameplay, localisation, script, spreadsheet, achievement, idea, or focus files were edited in this package.

## Notes

- Current Fury decision DDS files were replaced but not used as source art.
- Fury focus, goal, and idea icons were not used as source art.
- A temporary venv at `/tmp/fury_decision_icons_venv` was created to provide `Pillow` for the chroma-key helper. This did not change repo files.
