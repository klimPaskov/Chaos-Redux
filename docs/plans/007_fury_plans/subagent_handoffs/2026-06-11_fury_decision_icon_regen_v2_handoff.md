# Fury decision icon regeneration v2 handoff

Date: 2026-06-11

Scope: replace only the two Fury decision-category DDS files and seven Fury decision DDS files, plus the requested decision icon docs package.

## Changed files

Replaced final DDS assets:

- `gfx/interface/decisions/fury/decision_category_fury_war_office.dds`
- `gfx/interface/decisions/fury/decision_category_anti_fury.dds`
- `gfx/interface/decisions/fury/decision_fury_target.dds`
- `gfx/interface/decisions/fury/decision_fury_depots.dds`
- `gfx/interface/decisions/fury/decision_fury_settlement.dds`
- `gfx/interface/decisions/fury/decision_fury_coring.dds`
- `gfx/interface/decisions/fury/decision_fury_terminal_reserves.dds`
- `gfx/interface/decisions/fury/decision_fury_terminal_fronts.dds`
- `gfx/interface/decisions/fury/decision_anti_fury_response.dds`

Added asset package:

- `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_category_fury_war_office_source.png`
- `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_category_anti_fury_source.png`
- `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_fury_target_source.png`
- `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_fury_depots_source.png`
- `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_fury_settlement_source.png`
- `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_fury_coring_source.png`
- `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_fury_terminal_reserves_source.png`
- `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_fury_terminal_fronts_source.png`
- `docs/assets/007_fury/decision_icons_regen_v2/source_png/decision_anti_fury_response_source.png`
- `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_category_fury_war_office.png`
- `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_category_anti_fury.png`
- `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_fury_target.png`
- `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_fury_depots.png`
- `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_fury_settlement.png`
- `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_fury_coring.png`
- `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_fury_terminal_reserves.png`
- `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_fury_terminal_fronts.png`
- `docs/assets/007_fury/decision_icons_regen_v2/processed_png/decision_anti_fury_response.png`
- `docs/assets/007_fury/decision_icons_regen_v2/fury_decision_icon_contact_sheet.png`
- `docs/assets/007_fury/decision_icons_regen_v2/manifest.md`

## Visual direction used

- The set was rebuilt as a distinct decision-icon family, not as shrunken focus or goal art.
- Ordinary decision icons use one compact central symbol with strong silhouette, painterly texture, transparent unused pixels, and limited micro-detail for `32x32`.
- Decision-category icons stay wider but use the same emblem-driven decision-category style at `52x40`.
- The motifs lean on reticles, crates, stamps, seals, arrows, shields, and firebreak imagery rather than papers, desks, or scene-heavy compositions.

## Validation

- Decision reference art was inspected in `.agents/skills/chaos-redux-event-assets/assets/decisions/` before generation and processing.
- `identify` confirmed all processed PNG previews are the expected size:
  - `decision_category_fury_war_office.png` and `decision_category_anti_fury.png`: `52x40`
  - all seven ordinary decision previews: `32x32`
- `identify` confirmed all nine final DDS files match those same dimensions.
- `identify` confirmed processed PNG previews and DDS files preserve transparency (`opaque=false`).
- The contact sheet was visually reviewed for family consistency and for the requested move away from focus-icon styling.

## Blockers

- None.

## Notes

- Existing Fury decision DDS files were replaced but were not used as source art.
- Existing Fury focus, goal, and idea icons were not used as source art.
- The chroma-key helper required `Pillow`, so a temporary venv was created at `/tmp/fury_decision_icons_venv` to complete alpha cleanup. This did not change repo files.
