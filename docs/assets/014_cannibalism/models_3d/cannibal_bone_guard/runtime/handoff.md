# Cannibal Bone Guard runtime handoff

Status: **package complete; parent runtime wiring installed**.

The approved exact-one reference and selected Meshy 7 recovery geometry are complete, normalized, textured for the PDX material contract, and documented. Eight verified Meshy animation sources were imported through the saved-scale 24-bone target, corrected through root-only contact grounding, exported with the checksum-locked Blender/`io_pdx_mesh` adapter, and reimported against the final mesh.

## Parent-owned consumer

- Gameplay consumer: `common/units/014_cannibalism_irregular_infantry.txt#cannibal_bone_guard`.
- Proposed entity: `cannibal_bone_guard_entity`.
- Proposed runtime model root: `gfx/models/units/014_cannibalism/cannibal_bone_guard/`.
- Runtime wiring is present in `gfx/entities/014_cannibalism_units.gfx`, `gfx/entities/014_cannibalism_units.asset`, `sound/014_cannibalism_units_sound.asset`, and `gfx/models/units/014_cannibalism/cannibal_bone_guard/`.
- Parent still owns gameplay, localisation, country-level voice integration, and live in-game validation.

## Selected geometry and scale

- Meshy 7 recovery task: `01a02992-3227-70d8-9930-f8b6e3bb28db`.
- GLB: `provider/downloads/recovery_weapon_preserved_model.glb`, SHA-256 `904150E92B78713A6B283F197B472F1D8E8F162CBCBD882F9D0F5FE4FD01F00D`.
- FBX: `provider/downloads/recovery_weapon_preserved_model.fbx`, SHA-256 `4A1A3B113BEE22FF082ABED797ADDB919F570093BA8002C4171F51F43382DAB6`.
- Geometry: 30,000 triangles, 14,850 vertices, dimensions `4.309507 x 3.023676 x 7.351825`, ground Z `0`, zero non-manifold edges, zero degenerate faces.
- Open-surface evidence: 236 boundary edges across 56 components. Bounded closure was rolled back because it threatened visible armour/weapon topology; deformation/export approval remains withheld.
- Identity review: scarred humanoid, layered skull/rib/long-bone armour, invented culture-neutral paint, and the heavy two-handed poleaxe are visibly preserved in the seven-view preview set.
- Vanilla reference: installed `western_european_infantry.mesh#polySurface106`, source height `7.351824797689915`, forward `-Y`, up `+Z`.
- Runtime reference: `units_infantry.asset#infantry_rifle_entity`, entity scale `0.8` applied exactly once, effective runtime height `5.881459838151932`.

## Materials

- `textures/processed/cannibal_bone_guard_diffuse.dds`, SHA-256 `7BF6FE5B44766304A839187C8FC499110FFBD977C1378803AB54FCB63C953632`.
- `textures/processed/cannibal_bone_guard_specular.dds`, SHA-256 `4370691BE9A66A80657A385185F8AFEDD8962465A24426DA7EE77AF51AEA8643`.
- `textures/processed/cannibal_bone_guard_normal.dds`, SHA-256 `AE5CE458A33262D766CA045A2C9AB7442DADA7ADBFD180850F2309621079560E`.
- Each final candidate is 1024x1024, legacy one-level uncompressed BGRA DDS with a 128-byte header and exact 4,194,432-byte length.
- The specular map is the provider-derived PDX pack, not raw grayscale roughness. Immutable provider base/PBR maps remain under `provider/downloads/recovery_weapon_preserved_model_textures/`.

## Rig and actions

The earlier locally authored rig and action reports remain rejected evidence and were not exported. The eight final roles use verified provider-sourced actions imported and retargeted through the saved-scale target:

- `idle`
- `move`
- `attack` — genuine overhead poleaxe charge, chop, impact, recoil, and recovery
- `defend`
- `support_attack`
- `retreat`
- `training`
- `death` — articulated collapse and settling

The current proof set is under `blender/checkpoints/reimport_cannibal_bone_guard_*_reimport_grounded_v2.blend`. The saved checkpoint correction reports show body-motion keys retained and only the root location channel corrected. The final exported actions are 30 fps provider clips; their minimum reimport ground contacts are within the adapter tolerance, with lifted limbs allowed during attack/defend/death poses.

## Sound package

All required sourced roles exist as 44.1 kHz mono PCM s16le candidates. See `evidence/audio_sources/provenance_manifest.json` and `ffprobe_and_hash_receipt.json` for source pages, direct-download URLs, creators, licenses, source/derived checksums, transformations, durations, and proposed synchronization.

Selection/acknowledgement is a country/original-tag infantry voice consumer in installed HOI4, not an honest per-subunit sound. Parent must map it at country level. Poleaxe swing/impact and movement/death events can remain entity/action specific after final action timing is known.

## Counter package

The bespoke large, on-map, and texticon package exists and is registered outside this model job. `evidence/counter_audit.md` records exact tokens, DDS paths/hashes, frame dimensions, installed references, palette/state treatment, skill-local reference families, and validation evidence. No shared counter or GFX file was edited here.

## Blocker and acceptance boundary

The complete package has valid `.mesh`/`.anim` exports and eight reimport proofs. Open-surface boundary counts remain documented as diagnostic topology evidence, while position-welded topology has zero non-manifold and degenerate faces. No live in-game validation is claimed here.
