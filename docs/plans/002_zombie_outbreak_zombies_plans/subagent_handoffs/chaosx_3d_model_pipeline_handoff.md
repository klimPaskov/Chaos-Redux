# Zombies 3D model pipeline handoff

Status: complete asset package and runtime registration. User-owned live HOI4 verification remains pending.

## Package and gates

- Exact job root: `docs/assets/002_zombie_outbreak/models_3d/zombies/`
- Exactly one generated provider reference: `refs/original/meshy_input.png`
- Reference SHA-256: `7A37CCD412827E4672D94D6AA788EA7C590D3EAFAA09EA17328107914C068DD3`
- Vanilla calibration: `western_european_infantry.mesh`, object `polySurface106`, source height `7.351824797689915`, entity scale `0.8`, forward `-Y`, up `+Z`
- Final geometry: one watertight `30,000`-triangle, `14,950`-vertex mesh with one UV layer and no boundary, non-manifold, degenerate, or negative-scale issues
- Rig: one 24-bone humanoid armature with complete weight coverage
- Material: `PdxMeshAdvanced`; diffuse, packed specular, and normal DDS maps are 1024x1024; packed channels are red zero mask, green specular, blue metallic, alpha roughness

## Provider lineage and spend

| Stage | Task ID | Credits | Outcome |
| --- | --- | ---: | --- |
| Image-to-3D | `019f9932-c2e0-72c5-be74-ecdd2cf5b52c` | 30 | succeeded |
| Remesh | `019f994f-9cd7-735a-8f0e-6824f32756dc` | 5 | succeeded; same candidate |
| Rig | `019f9957-7590-758c-905a-98f5fb0803d0` | 5 | succeeded; 24 bones |
| Idle | `019f9962-22c1-7f1d-ba0e-3d587a514c56` | 3 | passed |
| Move/shamble | `019f9965-8417-7e18-9b45-ef1fc898e807` | 3 | passed; minor sampled sole-contact risk |
| Attack | `019f9968-b449-79e2-95f6-f4a4344d1ab6` | 3 | corrected in place after initial gate failure |
| Death | `019f9ad8-afaa-7c3a-b04d-8156ad459141` | 3 | succeeded; passed |

Initial balance was `1031`; the post-death balance check is `979`; actual spend is `52` of the authorized `52` credits. The credit evidence is `docs/assets/002_zombie_outbreak/models_3d/zombies/evidence/provider_credit_reconciliation_52.json`.

## Corrective pass

The original attack action failed at frame `35` with minimum Z `0.6203422546386719`. The parent added and verified the allowlisted adapter operation `correct_action_grounding` at adapter version `1.1.0`. It edits only integer-frame Z keys on the existing `Hips` root, preserves body motion, creates no model or rig, and makes no provider call. The corrected checkpoint is `blender/checkpoints/06_attack_grounding_corrected.blend`; the after-gate range is `-0.000010014` to `0.000007153` source units. Evidence is `blender/reports/correct_action_grounding.json`.

## Final exports and proof

- Mesh: `export/mesh/chaosx_zombies.mesh`, SHA-256 `A23F8C6CC7C85B2686E02DFA6AC92B29B553D534ECBB53F0BA8E650ADFB8DAEB`
- Idle: `export/anim/chaosx_zombies_idle.anim`, SHA-256 `4E12BBCC29A840CEC6B4EDB67D5191CF10F119A028EE238E6C9FFEB589986A43`
- Move: `export/anim/chaosx_zombies_move.anim`, SHA-256 `AE730339C4691C6CB2205F8C95D01075CA0CD328AA81799AC09255EC49CEDB87`
- Attack: `export/anim/chaosx_zombies_attack.anim`, SHA-256 `C4E7BB3FB0D2F6834F2D01E9D0C9EB179AE0A868167D2FD708B1E9B4AE5F6513`
- Death: `export/anim/chaosx_zombies_death.anim`, SHA-256 `70C585CB303A321D97A78B5B0A4FAEC59C747CE6B2AC98C55522FBDCBFAA8436`
- Exact output count is one `.mesh` and four `.anim` files; no variant or fallback asset was created.
- Actual-byte parse and Blender reimport proof is `validation/export_byte_parse.json`, with per-action proof blends under `validation/` and `blender/checkpoints/`.
- Textures and material proof are in `textures/processed/`, `textures/dds/`, `blender/reports/pdx_runtime_texture_processing.json`, `blender/reports/textures_dds.json`, and `blender/reports/final_working_material_inspect.json`.

## Runtime registration

- The base `zombies` sub-unit now uses `sprite = zombies` in `common/units/zombies.txt`; all named variants remain on `sprite = infantry`.
- `gfx/entities/chaosx_zombies.gfx` registers `chaosx_zombies_mesh` and its four PDX animation IDs.
- `gfx/entities/chaosx_zombies.asset` registers `zombies_entity` at scale `0.8` with attack, defend, support_attack, move, retreat, death, idle, and training states.
- `gfx/models/units/chaosx_zombies/animation_chaosx_zombies.asset` registers the four `.anim` files.
- The mesh, four animations, and three DDS maps are synchronized under `gfx/models/units/chaosx_zombies/`; hash proof is `docs/assets/002_zombie_outbreak/models_3d/zombies/validation/runtime_wiring.json`.
- Runtime state and file crosswalks are in `runtime/handoff.md` and `runtime/crosswalk.md`.
- User owns live HOI4 verification; Hearts of Iron IV was not launched.
- The move action's sampled mid-cycle sole penetration of `0.087125` source units remains the only recorded simplification/risk. No other requested simplification or omission was made.
