# Facility mesh deformation repair handoff

Status: implemented, exported, reimported, visually reviewed, and synchronized to runtime; user-owned live HOI4 confirmation remains.

Superseded for active runtime packaging by `2026-08-21_facility_render_stream_repair.md` after live screenshots proved that the earlier exports still used unsafe stream density and incomplete `meshsettings` registration. This file remains the historical record of the transform-bake repair.

## Reported defect

The chemical and biological facility map models rendered as stretched triangle webs in HOI4. Runtime wiring, entity scale, texture selection, building definitions, and dedicated spawn pools were already unique and correct, so the repair remained confined to the two model jobs, the static-building export adapter, and the two runtime `.mesh` files.

## Root cause and rejected routes

Both old pre-export checkpoints retained non-identity anisotropic transforms introduced by height normalization and footprint fitting. The old chemical export also placed 89,403 seam-split vertices in one PDX mesh stream, exceeding the 65,535 index boundary.

Aggressive collapse reduction was not accepted as a substitute. A 7,000-triangle biological candidate and chemical candidates down to the 42,912-triangle topology floor produced large faceted or spiky shells in reimport renders. Those candidates were rejected and never synchronized to runtime.

## Adapter repair

The locked repository adapter is now `chaosx_blender_hoi4` 1.5.0. It adds:

- `bake_static_mesh_transforms`, which bakes location, rotation, and scale into approved static-building mesh data, requires exact identity transforms afterward, and proves zero bounds drift, preserved names, UV layers, materials, and protected source objects;
- iterative target enforcement for bounded decimation, including hard failure on stalled or over-target passes;
- `partition_static_mesh_export_batches`, which preserves accepted static geometry while assigning unchanged triangles to texture-identical material batches beneath the same object;
- actual PDX text-export parsing with a hard failure if any individual mesh stream exceeds 65,535 vertices.

The dependency/config lock was refreshed and `python .tools/3d_pipeline/verify_environment.py --probe-meshy` completed with no findings after the final adapter change. No Meshy generation, remesh, rig, animation, paid recovery, replacement model, or cross-profile fallback was used.

## Biological facility result

- Accepted source checkpoint: `docs/assets/chaos_warfare_system/models_3d/biowarfare_facility/blender/checkpoints/2026-08-15_pre_repair_deformed.blend`.
- Transform-baked checkpoint: `blender/checkpoints/05b_static_transforms_baked_30k.blend`.
- Object: `Mesh_0.001`, exact identity location/rotation/scale, zero measured bounds drift.
- Geometry: 30,000 triangles, 13,788 working vertices.
- PDX streams: one stream, 28,844 vertices, below 65,535.
- Reimport: 30,000 triangles, 28,844 vertices, dimensions `[6.4689607620, 6.6628217697, 3.4620125294]`, no armature or actions, clean position-welded topology.
- Reimport proof: `validation/reimport_biowarfare_facility_fixed.json` and `blender/checkpoints/reimport_biowarfare_facility_fixed.blend`.
- Reviewed renders: front, left, rear, right, top, underside, and three-quarter views under `blender/previews/reimport_biowarfare_facility_fixed_*.png`.
- Canonical staged/runtime SHA-256: `2CB9EC7927860DA695DF7E6F9E9A43F04C8297019D158A99625170B3102A4A66`.

## Chemical facility result

- Accepted source checkpoint: `docs/assets/chaos_warfare_system/models_3d/cw_facility/blender/checkpoints/2026-08-15_pre_repair_deformed.blend`.
- Transform-baked checkpoint: `blender/checkpoints/05b_static_transforms_baked_58k.blend`.
- Export-batched checkpoint: `blender/checkpoints/05c_static_export_batched_58k.blend`.
- Object: `Mesh_0.001`, exact identity location/rotation/scale, zero measured bounds drift.
- Geometry: 58,004 triangles, 20,807 working vertices; geometry, UVs, normals, bounds, textures, and object identity were unchanged by batching.
- PDX streams: 20,000 triangles / 31,255 vertices; 20,000 / 31,625; 18,004 / 26,988. Maximum stream size is 31,625, below 65,535.
- Reimport: 58,004 triangles, 89,868 total joined vertices, dimensions `[6.6687164307, 6.6690034866, 3.4658875465]`, no armature or actions, clean position-welded topology.
- Reimport proof: `validation/reimport_cw_facility_fixed.json` and `blender/checkpoints/reimport_cw_facility_fixed.blend`.
- Reviewed renders: front, left, rear, right, top, underside, and three-quarter views under `blender/previews/reimport_cw_facility_fixed_*.png`.
- Canonical staged/runtime SHA-256: `6C535B7BA7314A2E02968FBBD795648AA20ACAA3169A3A1585FAB01B695273B0`.

## Runtime synchronization

On 2026-08-15T18:21:26+03:00, the canonical staged meshes were copied with PowerShell `Copy-Item -LiteralPath` to:

- `gfx/models/buildings/biowarfare_facility.mesh`;
- `gfx/models/buildings/cw_facility.mesh`.

Source and destination SHA-256 hashes match for both files. Existing `gfx/entities/chaosx_buildings.gfx`, `gfx/entities/chaosx_buildings.asset`, `common/buildings/chaosx_buildings.txt`, and `common/buildings/chaosx_3d_model_spawns.txt` remain the active unique runtime chain. Existing textures, scale 0.6, `PdxMeshAdvancedSnow`, `Mesh_0.001`, and the dedicated `chaosx_biowarfare_facility_spawn` and `chaosx_cw_facility_spawn` pools were retained.

## Remaining validation boundary

The agent does not launch Hearts of Iron IV. Live map rendering is therefore user-owned validation; no in-game completion claim is made in this handoff.

No fallback, substitute model, cross-type asset, texture replacement, or gameplay simplification was used.
