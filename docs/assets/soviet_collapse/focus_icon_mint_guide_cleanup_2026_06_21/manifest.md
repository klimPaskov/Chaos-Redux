# Soviet Collapse Focus Icon Mint Guide Cleanup Manifest

- Asset type: focus icons
- Package path: `docs/assets/soviet_collapse/focus_icon_mint_guide_cleanup_2026_06_21/`
- Source mode: live regenerated DDS extracted to PNG, then targeted mint guide cleanup
- Target size: `94x86`
- Final live DDS folder: `gfx/interface/goals/soviet_collapse/`
- Reference inspection:
  - `.agents/skills/chaos-redux-event-assets/assets/focuses/`
  - `~/projects/Hearts of Iron IV/gfx/interface/goals/`
- User-reported issue addressed: visible crop/guide marks on regenerated Soviet Collapse focus icons.
- Processing summary:
  - extracted the nine affected live DDS files to `source_png/`
  - removed pale mint guide pixels matching the exported crop-line profile
  - preserved the underlying focus art, alpha, and `94x86` focus icon canvas
  - converted package DDS copies and replaced the owned live DDS files in `gfx/interface/goals/soviet_collapse/`
- Contact sheet:
  - `contact_sheets/mint_cleanup_before_after_checker_contact_sheet.png`
- Validation:
  - `validation/mint_cleanup_summary.txt`
  - `validation/component_cleanup_summary.txt` records the rejected connected-component-only attempt and why the color-specific cleanup was used.

| Asset | Live DDS | Processed PNG | Package DDS | Status | Removed guide pixels |
| --- | --- | --- | --- | --- | --- |
| `kaz_soviet_collapse_common_steppe_passports` | `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_common_steppe_passports.dds` | `processed_png/kaz_soviet_collapse_common_steppe_passports.png` | `dds/kaz_soviet_collapse_common_steppe_passports.dds` | `complete` | `300` |
| `kaz_soviet_collapse_kyrgyz_mountain_liaisons` | `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_kyrgyz_mountain_liaisons.dds` | `processed_png/kaz_soviet_collapse_kyrgyz_mountain_liaisons.png` | `dds/kaz_soviet_collapse_kyrgyz_mountain_liaisons.dds` | `complete` | `271` |
| `kaz_soviet_collapse_league_cavalry_school` | `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_league_cavalry_school.dds` | `processed_png/kaz_soviet_collapse_league_cavalry_school.png` | `dds/kaz_soviet_collapse_league_cavalry_school.dds` | `complete` | `81` |
| `kaz_soviet_collapse_southern_deputies_seats` | `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_southern_deputies_seats.dds` | `processed_png/kaz_soviet_collapse_southern_deputies_seats.png` | `dds/kaz_soviet_collapse_southern_deputies_seats.dds` | `complete` | `232` |
| `kaz_soviet_collapse_southern_republics_do_not_kneel` | `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_southern_republics_do_not_kneel.dds` | `processed_png/kaz_soviet_collapse_southern_republics_do_not_kneel.png` | `dds/kaz_soviet_collapse_southern_republics_do_not_kneel.dds` | `complete` | `199` |
| `kaz_soviet_collapse_southern_republics_write_together` | `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_southern_republics_write_together.dds` | `processed_png/kaz_soviet_collapse_southern_republics_write_together.png` | `dds/kaz_soviet_collapse_southern_republics_write_together.dds` | `complete` | `258` |
| `kaz_soviet_collapse_southern_shield` | `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_southern_shield.dds` | `processed_png/kaz_soviet_collapse_southern_shield.png` | `dds/kaz_soviet_collapse_southern_shield.dds` | `complete` | `228` |
| `kaz_soviet_collapse_steppe_defense_council` | `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_steppe_defense_council.dds` | `processed_png/kaz_soviet_collapse_steppe_defense_council.png` | `dds/kaz_soviet_collapse_steppe_defense_council.dds` | `complete` | `302` |
| `kaz_soviet_collapse_tajik_pass_agreements` | `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_tajik_pass_agreements.dds` | `processed_png/kaz_soviet_collapse_tajik_pass_agreements.png` | `dds/kaz_soviet_collapse_tajik_pass_agreements.dds` | `complete` | `117` |

The cleanup is intentionally narrow: it removes pale mint crop-guide pixels and does not redesign or regenerate the Soviet focus art.
