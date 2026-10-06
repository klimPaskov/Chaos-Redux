# Shared Equipment Asset Manifest

This package covers the eight transferred original `shared_chaosx_equipment` findings across seven production tasks; the seven tank-shell sprites, the 27 chemical-air variants, and the payload cylinders belong to the other asset owner.

The source review was `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md` with SHA-256 `A7D534DCA813E1BD8E9245F80DB02FB54DA5A76A548662950FCFBBFD4A3A46C3`, plus `gfx_issues.json` with SHA-256 `0E3B24B887C7A3EC1148E023A05D9FF3D059DF906B10540391CAAA4B5F4701DC`.

The canonical equipment reference family is `.agents/skills/chaos-redux-event-assets/assets/gfx_references/units/equipment/technology_art/`; its contact sheet was inspected before its individual references and has SHA-256 `B8A2F2CD641BBA79B9F49D71DF3B4B3FBAB7DF05FF6C5787DA750121391EA80E`.

| Sprite or deliverable | Target and background | Source PNG | Processed PNG | Final DDS path | Prompt record / status |
|---|---|---|---|---|---|
| `GFX_coal_golem_equipment_medium`, `GFX_coal_golem_equipment_1_medium` | 131×52, native transparent | `source_png/coal_golem_equipment_v5.png` | `processed_png/coal_golem_equipment_v5_131x52.png` | `gfx/interface/technologies/coal_golem_equipment.dds` | `prompts/coal_golem_equipment_v5.json`; parent-approved, promoted and committed |
| `GFX_EMI_livens_tabun_projectile` | 56×42, native transparent | `source_png/tabun_projectile_v1.png` | `processed_png/tabun_projectile_v1_56x42.png` | `gfx/interface/equipmentdesigner/modules/tabun_projectile.dds` | `prompts/tabun_projectile_v1.json`; parent-approved, promoted and committed |
| `GFX_archetype_livens_projector_equipment_medium` | 58×40, native transparent | `source_png/archetype_livens_projector_v1.png` | `processed_png/archetype_livens_projector_v1_58x40.png` | `gfx/interface/archetypes/archetype_livens_projector_equipment.dds` | `prompts/archetype_livens_projector_v1.json`; parent-approved, promoted and committed |
| `GFX_tularemia_bomb_equipment`, `GFX_tularemia_bomb_equipment_medium` | 131×52, native transparency requested; blocked | — | — | Reserved `gfx/interface/technologies/equipment_wide/tularemia_bomb_equipment.dds`; no file exists | `prompts/tularemia_bomb_equipment_wide_v1.json`, `..._v2.json`; blocked after two ImageGen refusals; protected research file unchanged |
| `GFX_livens_projector_equipment_medium`, `_1_medium`, `GFX_livens_projector_tech_medium` | 94×45, native transparent | `source_png/livens_projector_single_tube_v1.png` | `processed_png/livens_projector_single_tube_v1_94x45.png` | `gfx/interface/technologies/livens_projector.dds` | `prompts/livens_projector_single_tube_v1.json`; parent-approved, promoted; commit pending |
| `GFX_livens_projector_equipment_2_medium`, `GFX_improved_livens_projector_medium` | 94×45, native transparent | `source_png/livens_projector_framed_battery_v1.png` | `processed_png/livens_projector_framed_battery_v1_94x45.png` | `gfx/interface/technologies/livens_projector_improved.dds` | `prompts/livens_projector_framed_battery_v1.json`; parent-approved, promoted; commit pending |
| `GFX_livens_projector_equipment_3_medium`, `GFX_advanced_livens_projector_medium` | 94×45, native transparent | `source_png/livens_projector_carriage_battery_v1.png` | `processed_png/livens_projector_carriage_battery_v1_94x45.png` | `gfx/interface/technologies/livens_projector_advanced.dds` | `prompts/livens_projector_carriage_battery_v1.json`; parent-approved, promoted; commit pending |
| `GFX_zombie_cure_bomb_equipment`, `GFX_zombie_cure_bomb_equipment_medium` | 131×52, native transparent | `source_png/zombie_cure_bomb_equipment_v1.png` | `processed_png/zombie_cure_bomb_equipment_v1_131x52.png` | `gfx/interface/technologies/zombie_cure_bomb_equipment.dds` | `prompts/zombie_cure_bomb_equipment_v1.json`; parent-approved, promoted; commit pending |
| `GFX_livens_projector_chassis_blueprint` | 508×248, consumer-opaque | `source_png/livens_projector_chassis_blueprint_v2.png` | `processed_png/livens_projector_chassis_blueprint_v2_508x248.png` | `gfx/interface/equipmentdesigner/generic_livens_projector_blueprint.dds` | `prompts/livens_projector_chassis_blueprint_v2.json`; parent-approved, promoted; commit pending |
| `GFX_livens_projectile_slot` | 508×248, native transparent technical mask derived from blueprint | `source_png/projectile_slot_source_overlay_v2.png` and `source_png/projectile_slot_source_mask_v2.png` | `processed_png/projectile_slot_v2_508x248.png` | `gfx/interface/equipmentdesigner/projectile_slot.dds` | `evidence/blueprint_overlay_lineage_v2.json`; parent-approved, promoted; commit pending |

Original DDS snapshots, decoded pre-edit PNGs, and inspection-only vanilla conversions are under `originals/` and `evidence/`; generated tool outputs remain at their reported ImageGen paths and were also copied into `source_png/` immediately after generation.

Generated sources are kept separate from processed PNGs and staged DDSs; exact prompt files, input-reference roles and hashes, and tool output paths are recorded in the lineage JSON packets.

The first-tranche native and smooth 4× sheets are `contact_sheets/first_tranche_native.png` and `contact_sheets/first_tranche_smooth_4x.png`.

The final second-tranche native and smooth 4× sheets are `contact_sheets/second_tranche_final_native.png` and `contact_sheets/second_tranche_final_smooth_4x.png`; earlier sheets preserve the rejected first hover-mask candidate and its dark texture gap.

Every promoted DDS uses the repository converter and passes the strict one-level uncompressed BGRA layout check, exact target dimensions, intended alpha range, and pixel-identical Texconv round-trip; `evidence/first_tranche_dds_validation.json`, `evidence/second_tranche_dds_validation.json`, and `evidence/second_tranche_v2_dds_validation.json` contain the results.

The corrected hover layer uses the exact source canister contours, with three connected filled silhouettes and no internal holes, the existing lavender RGB `#959DF0`, maximum alpha 128, and smooth antialiased edges; `evidence/blueprint_overlay_lineage_v2.json` records the source ROI, components, and aligned full-canvas mapping.

Tabun uses the parent-approved dark-olive body and the sampled Tabun oxblood `#55181E` as a narrow physical band; the capsule contains no label or letters.

The Livens tier set uses three different apparatus drawings: a fixed single tube, a framed three-tube battery, and a wheeled three-tube carriage; none contains tier numerals or text.

The cure-bomb icon uses one integrated physical glass ampoule as its sole cure motif and contains no `Z`, lettering, or corner stamps.

The blueprint panel is consumer-opaque because the exact equipment designer background consumer fills its 508×248 window; it contains no pseudo-writing or rat sketch.

The reference library has no `contact_sheet.png` under the vanilla `design_and_organization` interface shelf; exact installed tank and plane blueprint DDSs and their owning GFX files were inspected directly, and scoped sheets for those exact sprite groups are retained under `contact_sheets/vanilla_blueprint_reference/`.

The matching `visual_components/CATALOG.md` search found no equipment or blueprint component appropriate to these assets; no component layers were used.

## Blocked item

The two Tularemia generation attempts were refused by built-in ImageGen moderation: request `0b974903-8fc1-4b95-85c3-ef326f216c6f` at the output stage and request `9d495f4c-63fe-40de-848f-a229bda92fba` at the output stage.

No source PNG, processed PNG, or DDS was produced for the blocked wide Tularemia item; the existing 64×64 `gfx/interface/technologies/tularemia_bomb_equipment.dds` remains at SHA-256 `8817DC595C2A3C45C728253E54AB8E6C972448B2F32BF79D14D76831E6172C12` for the protected `GFX_tularemia_bomb_delivery_systems_medium` research consumer.

The initial blueprint prompt with supplied image references was refused at ImageGen input moderation, request `4c2be953-0f32-4d85-a3b6-3143973907ab`; the same built-in ImageGen route succeeded with the recorded text-only v2 prompt and required no fallback.

## Evidence packet

`evidence/first_tranche_lineage.json` contains the accepted first-tranche source, processed, DDS, baseline, alias, and five-call coal candidate lineage hashes.

`evidence/final_asset_lineage.json` contains the transferred-row accounting, current parent-owned GFX snapshot, blocked Tularemia evidence, all source/PNG/DDS hashes, and promotion records.

`evidence/blueprint_overlay_lineage_v2.json` records the corrected source-based contour fill, component coordinates, alpha bounds, and composite hashes.
