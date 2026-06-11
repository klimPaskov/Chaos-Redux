# Fury gameplay icon regeneration manifest

Date: 2026-06-11

Status: converted and ready for review.

This package replaces the Fury gameplay icon set with a generated HOI4-style icon family. The pass keeps all existing code-facing filenames stable and does not require `.gfx` changes.

## Source and processing

- Source PNGs: `docs/assets/007_fury/gameplay_icons_regen/source_png/`
- Processed PNG previews: `docs/assets/007_fury/gameplay_icons_regen/processed_png/`
- Contact sheet: `docs/assets/007_fury/gameplay_icons_regen/fury_gameplay_icon_contact_sheet.png`
- Final DDS files: `gfx/interface/goals/fury/`, `gfx/interface/ideas/fury/`, `gfx/interface/decisions/fury/`

The generated source family uses muted parchment, maps, ledgers, seals, crossed batons, supply crates, globes, and war-office furniture. The icons avoid text, modern logos, national flags, and UI mockups.

## Final assets

| Surface | Processed PNG | Final DDS | Size |
| --- | --- | --- | --- |
| Focus | `goal_fury_war_office.png` | `gfx/interface/goals/fury/goal_fury_war_office.dds` | 94x86 |
| Focus | `goal_fury_target_files.png` | `gfx/interface/goals/fury/goal_fury_target_files.dds` | 94x86 |
| Focus | `goal_fury_depots.png` | `gfx/interface/goals/fury/goal_fury_depots.dds` | 94x86 |
| Focus | `goal_fury_occupation_registers.png` | `gfx/interface/goals/fury/goal_fury_occupation_registers.dds` | 94x86 |
| Focus | `goal_fury_pact.png` | `gfx/interface/goals/fury/goal_fury_pact.dds` | 94x86 |
| Focus | `goal_fury_rivalry.png` | `gfx/interface/goals/fury/goal_fury_rivalry.dds` | 94x86 |
| Focus | `goal_fury_all_borders.png` | `gfx/interface/goals/fury/goal_fury_all_borders.dds` | 94x86 |
| Focus | `goal_fury_world_end.png` | `gfx/interface/goals/fury/goal_fury_world_end.dds` | 94x86 |
| Idea | `idea_fury_national_fury.png` | `gfx/interface/ideas/fury/idea_fury_national_fury.dds` | 64x64 |
| Idea | `idea_fury_hardened_fury.png` | `gfx/interface/ideas/fury/idea_fury_hardened_fury.dds` | 64x64 |
| Idea | `idea_fury_overextension.png` | `gfx/interface/ideas/fury/idea_fury_overextension.dds` | 64x64 |
| Idea | `idea_fury_compliance_drive.png` | `gfx/interface/ideas/fury/idea_fury_compliance_drive.dds` | 64x64 |
| Idea | `idea_fury_pact_command.png` | `gfx/interface/ideas/fury/idea_fury_pact_command.dds` | 64x64 |
| Idea | `idea_fury_rival_doctrine.png` | `gfx/interface/ideas/fury/idea_fury_rival_doctrine.dds` | 64x64 |
| Idea | `idea_fury_world_in_fury.png` | `gfx/interface/ideas/fury/idea_fury_world_in_fury.dds` | 64x64 |
| Idea | `idea_anti_fury_border_watch.png` | `gfx/interface/ideas/fury/idea_anti_fury_border_watch.dds` | 64x64 |
| Idea | `idea_anti_fury_emergency_aid.png` | `gfx/interface/ideas/fury/idea_anti_fury_emergency_aid.dds` | 64x64 |
| Idea | `idea_anti_fury_staff_talks.png` | `gfx/interface/ideas/fury/idea_anti_fury_staff_talks.dds` | 64x64 |
| Idea | `idea_anti_fury_supply_denial.png` | `gfx/interface/ideas/fury/idea_anti_fury_supply_denial.dds` | 64x64 |
| Decision category | `decision_category_fury_war_office.png` | `gfx/interface/decisions/fury/decision_category_fury_war_office.dds` | 52x40 |
| Decision category | `decision_category_anti_fury.png` | `gfx/interface/decisions/fury/decision_category_anti_fury.dds` | 52x40 |
| Decision | `decision_fury_target.png` | `gfx/interface/decisions/fury/decision_fury_target.dds` | 32x32 |
| Decision | `decision_fury_depots.png` | `gfx/interface/decisions/fury/decision_fury_depots.dds` | 32x32 |
| Decision | `decision_fury_settlement.png` | `gfx/interface/decisions/fury/decision_fury_settlement.dds` | 32x32 |
| Decision | `decision_fury_coring.png` | `gfx/interface/decisions/fury/decision_fury_coring.dds` | 32x32 |
| Decision | `decision_fury_terminal_reserves.png` | `gfx/interface/decisions/fury/decision_fury_terminal_reserves.dds` | 32x32 |
| Decision | `decision_fury_terminal_fronts.png` | `gfx/interface/decisions/fury/decision_fury_terminal_fronts.dds` | 32x32 |
| Decision | `decision_anti_fury_response.png` | `gfx/interface/decisions/fury/decision_anti_fury_response.dds` | 32x32 |

## Validation

- `identify` confirmed all final DDS files exist at the expected dimensions.
- `identify` confirmed all processed PNG previews exist at matching dimensions.
- The contact sheet was visually reviewed for broad motif consistency and lack of text/logos.
- No `.gfx`, localisation, gameplay, or script files were changed for this package.
