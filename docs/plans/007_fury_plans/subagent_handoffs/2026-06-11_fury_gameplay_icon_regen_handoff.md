# Fury gameplay icon regeneration handoff

Date: 2026-06-11

Scope: Fury focus, idea, decision, and decision-category icons only.

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
- `gfx/interface/decisions/fury/decision_category_fury_war_office.dds`
- `gfx/interface/decisions/fury/decision_category_anti_fury.dds`
- `gfx/interface/decisions/fury/decision_fury_target.dds`
- `gfx/interface/decisions/fury/decision_fury_depots.dds`
- `gfx/interface/decisions/fury/decision_fury_settlement.dds`
- `gfx/interface/decisions/fury/decision_fury_coring.dds`
- `gfx/interface/decisions/fury/decision_fury_terminal_reserves.dds`
- `gfx/interface/decisions/fury/decision_fury_terminal_fronts.dds`
- `gfx/interface/decisions/fury/decision_anti_fury_response.dds`

Added asset documentation package:

- `docs/assets/007_fury/gameplay_icons_regen/source_png/`
- `docs/assets/007_fury/gameplay_icons_regen/processed_png/`
- `docs/assets/007_fury/gameplay_icons_regen/fury_gameplay_icon_contact_sheet.png`
- `docs/assets/007_fury/gameplay_icons_regen/manifest.md`

## Validation

- Final DDS dimensions verified with `identify`:
  - Focus icons: `94x86`
  - Idea icons: `64x64`
  - Decision icons: `32x32`
  - Decision category icons: `52x40`
- Processed PNG previews verified with matching dimensions.
- Contact sheet visually reviewed for a HOI4-like muted, painterly icon family with no readable text, no modern logos, and no UI mockups.
- No `.gfx`, gameplay, localisation, script, or spreadsheet files were edited.

## Notes

- The icon generation agent produced the image and DDS outputs but did not finish this manifest/handoff before timing out; the main agent completed the documentation and validation.
- Temporary alpha-processing files were removed from the package before staging.
- No blockers remain for this asset package.
