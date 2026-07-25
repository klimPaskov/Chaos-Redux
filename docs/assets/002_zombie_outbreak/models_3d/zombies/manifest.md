# Zombies 3D model package

Status: complete asset package and runtime registration; user-owned live HOI4 verification remains pending.

## Identity and source

- Owner: `002_zombie_outbreak`
- Asset: `chaosx.model.002_zombie_outbreak.zombies`
- Unit identifier: `zombies`
- Profile: `humanoid_unit`
- Scope: exactly one shared base zombie humanoid model
- Single provider input: `refs/original/meshy_input.png`
- Reference dimensions: `1024x1536`
- Reference bytes: `2,076,049`
- Reference SHA-256: `7A37CCD412827E4672D94D6AA788EA7C590D3EAFAA09EA17328107914C068DD3`
- One-image count: exactly `1`; no portrait, second view, multi-view board, or variant was sent

## Locked dependencies and calibration

- Meshy MCP: official `@meshy-ai/meshy-mcp-server` `0.4.0`
- Blender adapter: `chaosx_blender_hoi4` `1.1.0`
- Blender: `5.1.2`, build `ec6e62d40fa9`
- io_pdx_mesh: `0.91.0`, locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`
- Vanilla source: `blender/reference/western_european_infantry.mesh`
- Measured vanilla object: `polySurface106`; collision `pCube1` excluded
- Vanilla source height: `7.351824797689915`
- Forward/up: `-Y` / `+Z`
- Entity scale: `0.8`, applied once by the future runtime entity
- Effective reference height: `5.881459838151932`
- Dependency, schema, adapter-root, and calibration evidence are retained under `evidence/` and `validation/`

## Provider lineage and credits

| Stage | Task | Result | Credits |
| --- | --- | --- | ---: |
| Image-to-3D | `019f9932-c2e0-72c5-be74-ecdd2cf5b52c` | succeeded | 30 |
| Remesh | `019f994f-9cd7-735a-8f0e-6824f32756dc` | succeeded; same candidate | 5 |
| Rig | `019f9957-7590-758c-905a-98f5fb0803d0` | succeeded; 24-bone humanoid | 5 |
| Idle | `019f9962-22c1-7f1d-ba0e-3d587a514c56` | succeeded; gate passed | 3 |
| Move | `019f9965-8417-7e18-9b45-ef1fc898e807` | succeeded; gate passed with minor sole-contact risk | 3 |
| Attack | `019f9968-b449-79e2-95f6-f4a4344d1ab6` | succeeded; corrected in-place after initial gate failure | 3 |
| Death | `019f9ad8-afaa-7c3a-b04d-8156ad459141` | succeeded; gate passed | 3 |

Initial balance was `1031`; the post-death read-only balance was `979`. The exact `52`-credit delta matches the authorized ceiling. Evidence is `evidence/provider_credit_reconciliation_52.json` and `provider/responses/029_meshy_check_balance.json`.

## Geometry, rig, and material

- Immutable generation GLB: `provider/downloads/generation_model.glb`, SHA-256 `67D8EB3AFE9D790E337DDCD5EF6E2F3EEC90F9A1996CA80508207F8EA6A74F56`
- Remesh rig source: `provider/downloads/remesh_model.glb`, SHA-256 `78FA1175E980C78FD8223028B3AB5B80CD55158E46C874129E486E803B3365B8`
- Rigged provider source: `provider/downloads/rigged_provider_model.glb`, SHA-256 `67080A8B835356A8E00E9B70603B2AB72F28F48884C78E395480A38C13A9B3B9`
- Final retained working geometry: one mesh, `30,000` triangles, `14,950` vertices, one UV layer, zero loose boundary edges, zero non-manifold edges, zero degenerate faces, and no negative scale
- Rig: one 24-bone humanoid armature, zero unweighted final vertices, zero non-bone groups
- Provider helper object `Icosphere` was explicitly excluded and is not model geometry
- Runtime material: `PdxMeshAdvanced` with diffuse `texture_0.dds`, packed specular `texture_specular.dds`, and normal `texture_normal.dds`
- Packed specular channels: red unused mask zero, green specular, blue metallic, alpha roughness
- Processed PNG/DDS maps are 1024x1024 and retained under `textures/processed/` and `textures/dds/`

## Action gates and exports

- Idle: `98` frames, `0-97`, 24 fps, in-place loop, passed
- Move/shamble: `73` frames, `0-72`, 24 fps, in-place loop, passed with sampled mid-cycle sole penetration of `0.087125` source units; this is the package's only recorded contact risk
- Attack: `69` frames, `0-68`, 24 fps, non-loop; the original frame-35 airborne sample was corrected by the verified `correct_action_grounding` operation on the existing `Hips` root channel, preserving body motion; corrected after-gate range was `-0.000010014` to `0.000007153` source units
- Death: `73` frames, `0-72`, 24 fps, non-loop, passed
- Corrected attack checkpoint: `blender/checkpoints/06_attack_grounding_corrected.blend`
- Final material checkpoint: `blender/checkpoints/07_final_working_corrected_attack_base.blend`
- Exported mesh: `export/mesh/chaosx_zombies.mesh` (`2,026,536` bytes)
- Exported animations: `export/anim/chaosx_zombies_idle.anim`, `export/anim/chaosx_zombies_move.anim`, `export/anim/chaosx_zombies_attack.anim`, and `export/anim/chaosx_zombies_death.anim`
- Exact output count: one `.mesh` and four `.anim` files; no variant was created
- Actual-byte parse and Blender reimport proof: `validation/export_byte_parse.json` and `validation/reimport_chaosx_zombies_*.json`

## Runtime boundary

- The base `zombies` sub-unit now resolves `sprite = zombies` in `common/units/zombies.txt`; all named zombie variants remain on their existing vanilla infantry sprite.
- Runtime registration is present in `gfx/entities/chaosx_zombies.gfx`, `gfx/entities/chaosx_zombies.asset`, and `gfx/models/units/chaosx_zombies/animation_chaosx_zombies.asset`.
- Runtime copies of the selected mesh, four animations, and three DDS maps are synchronized under `gfx/models/units/chaosx_zombies/` and match the selected export hashes.
- The runtime entity preserves scale `0.8` exactly once and maps attack, defend, support_attack, move, retreat, death, idle, and training states.
- User-owned live HOI4 verification remains pending; Hearts of Iron IV was not launched.

## Runtime registration evidence

- Runtime copy and reference proof: `validation/runtime_wiring.json`
- Runtime entity: `zombies_entity`
- Runtime PDX mesh: `chaosx_zombies_mesh` with exported object `Mesh_0.001`
- Runtime state actions: `idle`, `move`, `attack`, and `death`; training uses the idle action and retreat uses the move action

## Evidence index

- Job specification and lineage: `job.yaml`, `history.jsonl`
- Credit reconciliation: `evidence/provider_credit_reconciliation_52.json`
- Geometry/action gates: `evidence/geometry_gate.json`, `evidence/action_quality_gates.json`
- Attack correction: `blender/reports/correct_action_grounding.json`
- Material and texture proof: `blender/reports/final_working_material_inspect.json`, `blender/reports/pdx_runtime_texture_processing.json`, `blender/reports/textures_dds.json`
- Export/reimport proof: `validation/export_byte_parse.json`
- Runtime registration and source-to-runtime hash proof: `validation/runtime_wiring.json`
- Deterministic file ledger: `evidence/file_manifest.json`
