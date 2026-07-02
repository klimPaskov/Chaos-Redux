# Event 014 Cannibalism Decision Icon Imagegen Handoff

Status: complete for the narrowed decisions-only slice.

This handoff covers only final paths under `gfx/interface/decisions/014_cannibalism/*.dds`. It does not cover, generate, process, or validate any `gfx/interface/ideas/014_cannibalism/*` idea or national-spirit icon paths.

Package path used: `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/`

Contact sheet:

- `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/contact_sheets/event014_decision_icons_contact_sheet.png`

Validation record:

- `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/decision_icon_validation.tsv`

Scope confirmations:

- Every listed source image was produced with `$imagegen`.
- No final asset in this slice was produced from primitive local drawing, simple/procedural shapes, placeholder charts, or non-imagegen substitution.
- Local scripts were used only for chroma-key alpha removal, crop, resize/pad, DDS export, contact-sheet assembly, and validation.
- `gfx/leaders/014_cannibalism/hannibal.dds` was not touched or replaced.
- No `.gfx`, `.gui`, gameplay, localisation, history, country, focus, decision script, spreadsheet, or non-asset documentation files were edited by this slice.

Validation summary:

- 24 requested decision/category assets are present.
- DDS dimensions verified from the final live DDS files.
- 23 assets are `32x32`.
- `decision_cat_picture_cannibalism_frontline_hunger.dds` is `114x101`, matching the existing live category-picture target size.
- All final DDS files opened as RGBA through the repository's Pillow DDS workflow.
- All final DDS files have transparent corners after alpha processing.
- Visual readability was checked through the contact sheet listed above.

Changed files in this slice:

- `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/*.png`
- `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/alpha_png/*.png`
- `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/*.png`
- `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/dds/*.dds`
- `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/contact_sheets/event014_decision_icons_contact_sheet.png`
- `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/reference_contact_sheets/decisions_reference_contact_sheet.png`
- `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/reference_contact_sheets/ideas_reference_contact_sheet.png`
- `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/decision_icon_validation.tsv`
- `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/manifest.md`
- `gfx/interface/decisions/014_cannibalism/*.dds`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-07-01_event014_decision_idea_icon_imagegen_handoff.md`

Note: the idea reference contact sheet was created before the user narrowed the slice. It is a review/reference artifact only and is not an idea icon output.

## Asset Table

| Asset | Source mode | Source PNG | Processed PNG | Final DDS | Target |
|---|---|---|---|---|---|
| `decision_category_cannibalism_frontline_hunger` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_category_cannibalism_frontline_hunger_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_category_cannibalism_frontline_hunger.png` | `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_frontline_hunger.dds` | `32x32` |
| `decision_cat_picture_cannibalism_frontline_hunger` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cat_picture_cannibalism_frontline_hunger_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cat_picture_cannibalism_frontline_hunger.png` | `gfx/interface/decisions/014_cannibalism/decision_cat_picture_cannibalism_frontline_hunger.dds` | `114x101` |
| `decision_cannibalism_field_kitchens` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_field_kitchens_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_field_kitchens.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_field_kitchens.dds` | `32x32` |
| `decision_cannibalism_rotate_units` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_rotate_units_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_rotate_units.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_rotate_units.dds` | `32x32` |
| `decision_cannibalism_ration_convoy` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_ration_convoy_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_ration_convoy.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_ration_convoy.dds` | `32x32` |
| `decision_cannibalism_hospital_audit` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_hospital_audit_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_hospital_audit.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_hospital_audit.dds` | `32x32` |
| `decision_cannibalism_military_police` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_military_police_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_military_police.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_military_police.dds` | `32x32` |
| `decision_cannibalism_prison_freeze` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_prison_freeze_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_prison_freeze.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_prison_freeze.dds` | `32x32` |
| `decision_cannibalism_chaplain_work` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_chaplain_work_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_chaplain_work.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_chaplain_work.dds` | `32x32` |
| `decision_cannibalism_truth_commission` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_truth_commission_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_truth_commission.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_truth_commission.dds` | `32x32` |
| `decision_cannibalism_island_inspection` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_island_inspection_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_island_inspection.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_island_inspection.dds` | `32x32` |
| `decision_cannibalism_emergency_evacuation` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_emergency_evacuation_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_emergency_evacuation.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_emergency_evacuation.dds` | `32x32` |
| `decision_cannibalism_break_ritual_cell` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_break_ritual_cell_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_break_ritual_cell.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_break_ritual_cell.dds` | `32x32` |
| `decision_cannibalism_retake_commune` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_retake_commune_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_retake_commune.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_retake_commune.dds` | `32x32` |
| `decision_cannibalism_stop_copying` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_stop_copying_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_stop_copying.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_stop_copying.dds` | `32x32` |
| `decision_cannibalism_dismantle_terror` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_dismantle_terror_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_dismantle_terror.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_dismantle_terror.dds` | `32x32` |
| `decision_cannibalism_exploit_terror` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_exploit_terror_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_exploit_terror.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_exploit_terror.dds` | `32x32` |
| `decision_cannibalism_break_cult` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_break_cult_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_break_cult.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_break_cult.dds` | `32x32` |
| `decision_cannibalism_world_end_route` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_world_end_route_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_world_end_route.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_world_end_route.dds` | `32x32` |
| `decision_cannibalism_containment_deadline` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_containment_deadline_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_containment_deadline.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_containment_deadline.dds` | `32x32` |
| `decision_cannibalism_cbl_last_table_map` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_cbl_last_table_map_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_cbl_last_table_map.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_cbl_last_table_map.dds` | `32x32` |
| `decision_cannibalism_cbl_region_project` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_cbl_region_project_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_cbl_region_project.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_cbl_region_project.dds` | `32x32` |
| `decision_cannibalism_cbl_pact_courier` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_cbl_pact_courier_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_cbl_pact_courier.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_cbl_pact_courier.dds` | `32x32` |
| `decision_cannibalism_cbl_solitary_raid` | `$imagegen` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/source_png/decision_cannibalism_cbl_solitary_raid_source.png` | `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/processed_png/decision_cannibalism_cbl_solitary_raid.png` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_cbl_solitary_raid.dds` | `32x32` |

Remaining risks and blockers:

- None for the completed decision/category asset package.
- Final `.gfx` registration and any gameplay/localisation references remain outside this slice by instruction.
