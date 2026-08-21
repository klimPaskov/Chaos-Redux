# CBRN facility render-stream repair handoff

Status: repaired, exported, freshly reimported, visually reviewed, and synchronized to runtime; user-owned live HOI4 confirmation remains.

## Reported defect

Live map screenshots showed the chemical and biological facilities as stretched shard-like shells despite clean Blender reimports. The accepted models, textures, dimensions, entity scale, building definitions, and dedicated spawn pools were retained.

## Root cause

The chemical export contained three PDX streams, but `gfx/entities/chaosx_buildings.gfx` registered only stream index 0. HOI4 therefore rendered only a disconnected subset of the model.

The biological export placed all 30,000 triangles and 90,000 triangle indices in one stream. Its 28,844 exported vertices were below the nominal 65,535 vertex boundary, but its density was far beyond ordinary vanilla map-building streams. An audit of the 65 installed vanilla building meshes found a largest stream of 12,348 triangles, 12,974 vertices, and 37,044 triangle indices.

The repair therefore applies a conservative 8,000-triangle and 24,000-worst-case-index ceiling to both facilities and registers every resulting stream. It does not alter geometry, UVs, normals, bounds, object identity, textures, material appearance, origin, transforms, or scale.

## Biological facility

- Source checkpoint: `docs/assets/chaos_warfare_system/models_3d/biowarfare_facility/blender/checkpoints/05b_static_transforms_baked_30k.blend`.
- Engine-safe checkpoint: `blender/checkpoints/06_engine_safe_streams_8k.blend`.
- Geometry: 30,000 triangles and 13,788 working vertices, unchanged.
- Stream 0: 8,000 triangles, 8,357 vertices, 24,000 triangle indices.
- Stream 1: 8,000 triangles, 7,819 vertices, 24,000 triangle indices.
- Stream 2: 8,000 triangles, 7,569 vertices, 24,000 triangle indices.
- Stream 3: 6,000 triangles, 5,703 vertices, 18,000 triangle indices.
- GFX registration: indices 0 through 3, each using `Mesh_0.001`, the existing DDS set, and `PdxMeshAdvancedSnow`.
- Export: `export/mesh/biowarfare_facility_engine_safe.mesh`, 1,774,625 bytes, SHA-256 `6FB1DF91E6148A91709AAAF9F05EA379A7269F77F601ED3E7616D94F0E7FECD0`.
- Reimport: all 30,000 triangles, original dimensions `[6.4689607620, 6.6628217697, 3.4620125294]`, no armature or actions, and clean position-welded topology.
- Evidence: `validation/reimport_biowarfare_facility_engine_safe.json`, `blender/checkpoints/reimport_biowarfare_facility_engine_safe.blend`, and seven `blender/previews/reimport_biowarfare_facility_engine_safe_*.png` views.

## Chemical facility

- Source checkpoint: `docs/assets/chaos_warfare_system/models_3d/cw_facility/blender/checkpoints/05b_static_transforms_baked_58k.blend`.
- Engine-safe checkpoint: `blender/checkpoints/06_engine_safe_streams_8k.blend`.
- Geometry: 58,004 triangles and 20,807 working vertices, unchanged.
- Streams 0 through 6: 8,000 triangles each; exported vertex counts are 13,102, 12,646, 12,638, 12,987, 12,780, 12,783, and 11,596; each contains 24,000 triangle indices.
- Stream 7: 2,004 triangles, 3,213 vertices, 6,012 triangle indices.
- GFX registration: indices 0 through 7, each using `Mesh_0.001`, the existing DDS set, and `PdxMeshAdvancedSnow`.
- Export: `export/mesh/cw_facility_engine_safe.mesh`, 5,101,993 bytes, SHA-256 `CA775D75AC580704E30445FBD8F201502A2DF01962C581D28E5158FE92D54794`.
- Reimport: all 58,004 triangles, original dimensions `[6.6687164307, 6.6690034866, 3.4658875465]`, no armature or actions, and clean position-welded topology.
- Evidence: `validation/reimport_cw_facility_engine_safe.json`, `blender/checkpoints/reimport_cw_facility_engine_safe.blend`, and seven `blender/previews/reimport_cw_facility_engine_safe_*.png` views.

## Runtime synchronization

On 2026-08-21, the engine-safe exports were copied with PowerShell `Copy-Item -LiteralPath` to `gfx/models/buildings/biowarfare_facility.mesh` and `gfx/models/buildings/cw_facility.mesh`. Each runtime file exactly matches its staged source hash.

`gfx/entities/chaosx_buildings.gfx` now mirrors the vanilla building pattern by declaring one `meshsettings` block for every exported stream. The active entities, scale 0.6, textures, and dedicated `chaosx_biowarfare_facility_spawn` and `chaosx_cw_facility_spawn` pools remain unchanged.

The reusable 3D pipeline guidance now requires conservative static-building stream sizes, validates both vertex and triangle-index counts, and requires one matching GFX registration for every exported stream.

## Validation boundary

Fresh reimports and all rendered views preserve the accepted facility silhouettes and materials. The agent does not launch Hearts of Iron IV, so the corrected live map rendering remains user-owned consumer validation.

No substitute model, fallback, provider call, paid recovery, remesh, decimation, texture replacement, or gameplay simplification was used.
