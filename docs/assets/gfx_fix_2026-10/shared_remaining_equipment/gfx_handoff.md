# GFX Handoff: Shared Equipment

This handoff covers the eight transferred original review rows across seven production tasks. The other owner retains the payload cylinders, seven tank-shell icons, and 27 chemical-air variants.

The asset worker edited no `.gfx` or `.gui` files. Parent-owned GFX wiring was re-read from the shared current tree immediately before these leaf mappings; current hashes at that point were `interface/chaosx_equipment.gfx` `6E21186E8653353A8ACFB23386D4B95E66D70EBA8B2FC4254F86251E280E4C3D`, `interface/chaosx_techtree.gfx` `8F16FFBC33CD29F7BCEEF23CCDB91728A2B9ED90750D0F3975E2CCE77EFBE8ED`, and `interface/equipmentdesigner/livens_projector.gui` `E3459B0A667FFA19D22B4DED40B4804F8DA695B91A945FF65FB47CD5054F8827`.

| Sprite leaf | Current or accepted texture path | Asset status |
|---|---|---|
| `GFX_coal_golem_equipment_medium`, `GFX_coal_golem_equipment_1_medium` | `gfx/interface/technologies/coal_golem_equipment.dds` | Same-path replacement promoted and included in parent commit `55b2efa0263a0a016f023dff5e2a3485525a123d` |
| `GFX_EMI_livens_tabun_projectile` | `gfx/interface/equipmentdesigner/modules/tabun_projectile.dds` | Parent repointed this leaf; new56×42 file was promoted and included in the same commit |
| `GFX_archetype_livens_projector_equipment_medium` | `gfx/interface/archetypes/archetype_livens_projector_equipment.dds` | Same-path replacement promoted and included in the same commit |
| `GFX_tularemia_bomb_equipment`, `GFX_tularemia_bomb_equipment_medium` | Reserved `gfx/interface/technologies/equipment_wide/tularemia_bomb_equipment.dds` | No file produced; do not repoint while the asset remains blocked |
| `GFX_tularemia_bomb_delivery_systems_medium` | Existing `gfx/interface/technologies/tularemia_bomb_equipment.dds` | Protected64×64 research consumer and DDS are unchanged |
| `GFX_livens_projector_equipment_medium`, `_1_medium`, `GFX_livens_projector_tech_medium` | `gfx/interface/technologies/livens_projector.dds` | Existing path replacement promoted |
| `GFX_livens_projector_equipment_2_medium`, `GFX_improved_livens_projector_medium` | `gfx/interface/technologies/livens_projector_improved.dds` | Existing path replacement promoted |
| `GFX_livens_projector_equipment_3_medium`, `GFX_advanced_livens_projector_medium` | `gfx/interface/technologies/livens_projector_advanced.dds` | Existing path replacement promoted |
| `GFX_zombie_cure_bomb_equipment`, `GFX_zombie_cure_bomb_equipment_medium` | `gfx/interface/technologies/zombie_cure_bomb_equipment.dds` | Direct131×52 replacement promoted; no other GFX reference to this DDS was found, and the special-project icon uses a separate DDS |
| `GFX_livens_projector_chassis_blueprint` | `gfx/interface/equipmentdesigner/generic_livens_projector_blueprint.dds` | Existing path replacement promoted |
| `GFX_livens_projectile_slot` | `gfx/interface/equipmentdesigner/projectile_slot.dds` | Existing path replacement promoted with the corrected filled contour mask, three connected shapes, max alpha128, and no internal holes |

`interface/equipmentdesigner/livens_projector.gui` defines `equipment_designer_livens_projector_chassis` at exactly508×248. The blueprint and hover `iconType`s both draw at position `{ x=0 y=0 }` on full-canvas containers, so the delivered panel and overlay preserve those exact bounds and require no GUI edit.

The final exact source, processed PNG, staged DDS, runtime, baseline, prompt, reference, and parent-review evidence is in `evidence/final_asset_lineage.json`; strict DDS and round-trip checks are in `evidence/first_tranche_dds_validation.json`, `evidence/second_tranche_dds_validation.json`, and `evidence/second_tranche_v2_dds_validation.json`.

Tularemia was blocked after built-in ImageGen refused two attempts. No source, preview, or replacement DDS exists for its wide equipment leaf, and the64×64 research texture remains at SHA-256 `8817DC595C2A3C45C728253E54AB8E6C972448B2F32BF79D14D76831E6172C12`.

The task parent reported that the HOI4 `reference`, `gui`, and `tech` MCP routes returned `Transport closed`; this asset handoff has no engine render or in-game acceptance claim.
