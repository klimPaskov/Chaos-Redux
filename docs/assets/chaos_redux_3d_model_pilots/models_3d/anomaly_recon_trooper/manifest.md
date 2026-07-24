# anomaly_recon_trooper model manifest

Status: needs_user_review

## Identity

- Asset ID: `chaosx.model.pilot.anomaly_recon_trooper`
- Profile: `humanoid_unit`
- Provider: Meshy `@meshy-ai/meshy-mcp-server` `0.4.0`, model `meshy-6`
- Runtime stem: `chaosx_anomaly_recon_trooper`
- Candidate selection: one generation, one controlled remesh, one rig, two requested provider actions, and one Blender-authored locomotion action; no paid generation retry

## One-image gate

- Meshy input: `refs/original/meshy_input.png`
- Image count: `1`
- SHA-256: `2965C0B7A50F79CA8D48CB59ED2707553BB81194CAB801B4EC5F706AF73907EC`
- Source mode: built-in image generation, user-authorized pilot reference
- Side-profile sheet: not created
- Multi-view/turnaround board: not created

## Provider lineage

- Image-to-3D task: `019f8a68-1c0b-776d-aac7-9ff5a0981548`
- Generation candidate: 420,480 triangles; archived in `provider/downloads/generation_model.glb`; its controlled 30,000-triangle reduction is the watertight final geometry source
- Remesh task: `019f8a6e-f10a-77f4-adb2-03573928de88`; 250,000-target rig source in `provider/downloads/remesh_model.glb`
- Rig task: `019f8a71-3c36-7999-b9ce-fc1b31b70b67`; provider signed artifact fetched to `provider/downloads/rigged_provider_model.glb`
- Idle task/action: `019f8a7b-c072-7320-ab44-c0e19f5a2f53`, provider action `0`, 24 fps, loop
- Attack task/action: `019f8a7f-aebc-78fe-98c8-7727b0eabd9c`, provider action `4`, 24 fps, non-loop
- Provider signed-artifact transport: `assets.meshy.ai` URLs were host-validated and fetched into the job root; no REST/API fallback was used
- Requests/responses/tasks/credit records: `provider/requests/`, `provider/responses/`, `provider/tasks/`, `provider/credits/`
- Exploratory `meshy_convert` records remain append-only lineage only; their static outputs were not selected for the rig or action artifacts

## Blender, rig, and geometry evidence

- Blender: `5.1.2` (`ec6e62d40fa9`)
- Adapter: `chaosx_blender_hoi4` `1.0.0`
- Exporter: `io_pdx_mesh` `0.91.0`, archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`
- Export preset: selected working mesh/armature only, triangulated, `exp_selected=true`, shared-vertex export with `split_verts=false`; this keeps the final 30,000-triangle mesh at 14,970 source vertices and avoids the 90,000-vertex per-loop stream consistent with the live stretched-geometry symptom
- Source and rig/action checkpoints: `blender/checkpoints/`; corrected dual-source checkpoints are `attack_runtime_candidate_dual_20260724.blend`, `idle_runtime_candidate_dual_20260724.blend`, and `move_runtime_candidate_dual_20260724.blend`
- Vanilla reference staging: `blender/reference/western_european_infantry.mesh`; source checksum and read-only staging evidence are in `blender/reports/vanilla_reference_stage.json`
- Working geometry: watertight generation geometry from `provider/downloads/generation_model.glb` is bound to the provider armature with 24-bone weight transfer; one Blender mesh object `Mesh_0.001` is exported as `.mesh` object `Mesh_0.001`, with 30,000 triangles, 14,970 source vertices, one UV layer, one explicitly textured PDX material, and one armature
- Vanilla source measurement: the read-only infantry reference measures `7.351824` source units; the pilot's calibrated mesh is authored at `1.8379560709` source units so the runtime entity can remain neutral
- QA: 0 non-manifold edges, 0 degenerate faces, no negative scale objects
- Topology gate: the final working generation geometry has 0 loose boundary edges, 0 non-manifold edges, and 0 degenerate faces; raw `io_pdx_mesh` reimport exposes 6,772 UV/normal seam edges, but its position-welded audit returns 0 loose boundary edges and 0 non-manifold edges
- Provider-only `Icosphere` and `Icosphere.001` objects are explicitly excluded from working/render/export collections; the source remains preserved for audit
- The final shared-vertex payload reimports at 18,521 attribute-split vertices with the same 30,000 triangles and calibrated bounds; the position-welded reimport proof resolves to 14,970 vertices with closed topology, and the post-fix live renderer check remains pending because HOI4 was not launched.
- Vanilla calibration reference: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`
- Vanilla entity reference only: `gfx/entities/units_infantry.asset#infantry_rifle_entity`, vanilla runtime `scale = 0.8`; the pilot uses the vanilla mesh only as a read-only measurement reference
- Reference measurement: main imported `polySurface106` height `7.3518248` source units, collision geometry excluded, `-Y` forward and `+Z` up; effective runtime height `5.8814594` units
- Corrected pilot calibration: Blender mesh target `1.8379560709` source units, neutral entity `scale = 1.0`, expected effective runtime height `1.8379560709`, and final evaluated reimport height `1.8376898766`
- Transform mismatch repair: the mesh data absorbed the `94.7711071693` mesh-to-armature scale ratio before parenting, and the exporter now bakes the remaining uniform armature object scale `0.0102108670` into armature data while preserving the calibrated mesh world transform.
- Animation sanitation: the provider working actions had 72 root/bone scale F-curves removed, non-unit `Hips` pose scale reset to `(1, 1, 1)`, the authored move action was created without scale channels, and the exporter emits unit-scale armature bind data with mesh-unit translations without applying a second translation multiplier.

## Textures and PDX exports

- DDS evidence: `blender/reports/textures_dds.json`
- DDS backend: repository `convert_to_dds.py` using its verified ffmpeg backend; the texture report records each conversion log
- Runtime DDS dimensions: `1024 x 1024`, one-level uncompressed BGRA; the prior `2048 x 2048` texture exceeded the observed HOI4 model-texture limit
- Runtime textures: `textures/dds/texture_0.dds` (diffuse), `textures/dds/texture_normal.dds` (normal), and `textures/dds/texture_specular.dds` (PDX packed specular/roughness)
- PDX material shader: `PdxMeshAdvanced`, with explicit diffuse, normal, and specular bindings
- PDX normal packing: red `0`, green source tangent X, blue `0`, alpha source tangent Y; source maps and checksums are recorded in `blender/reports/pdx_normal_pack.json`
- PDX specular packing: red `0`, green `32` specular level, blue metallic, alpha roughness; final generation source maps are recorded in `blender/reports/pdx_generation_specular_pack.json`
- Mesh: `export/mesh/chaosx_anomaly_recon_trooper.mesh`, 1,844,376 bytes, SHA-256 `8B95A61E34A0A0351A3F2A083D0BE3A42724793ED0B6A51E8DE5E283ABC1F300`
- Runtime DDS: `textures/dds/texture_0.dds`, 4,194,432 bytes, SHA-256 `9566E784975C50215A947953385F77B3C393B2A7953FA1C83F2DF52C8AA4FC6B`
- Runtime normal DDS: `textures/dds/texture_normal.dds`, 4,194,432 bytes, SHA-256 `7C69F76A312AA1A581B8399D6C9104CCC74B6742B62255041DEACAE3A0D16607`
- Runtime specular DDS: `textures/dds/texture_specular.dds`, 4,194,432 bytes, SHA-256 `33E91684976EE5B502CF6A60E43273AA22696A3D9915E3305999584258C0786C`
- Idle action: `export/anim/chaosx_anomaly_recon_trooper_idle.anim`, 77,395 bytes, SHA-256 `307F846C30EA94322A1A8CDEEB969EB40BEC3FD74F5B8D35E119622DE238DDE5`, frames `0-97`, 24 fps, loop, no scale channels
- Attack action: `export/anim/chaosx_anomaly_recon_trooper_attack.anim`, 55,123 bytes, SHA-256 `4A812559E170AAB411BB45430E0005177703ECABF1F282ABDF01BA9E08D73F7B`, frames `0-68`, 24 fps, non-loop, unit root scale
- Move action: `export/anim/chaosx_anomaly_recon_trooper_move.anim`, 21,331 bytes, SHA-256 `3BF7981688259779C84A6608A05C1445072CD18D004B76C10AE96994DEAAF2E5`, frames `0-24`, 24 fps, loop, Blender-authored in place with a root translation channel and no scale channels
- Mesh reimport: current proof files are `validation/reimport_chaosx_anomaly_recon_trooper_attack.json`, `validation/reimport_chaosx_anomaly_recon_trooper_idle.json`, and `validation/reimport_chaosx_anomaly_recon_trooper_move.json`; archived dual-source reports remain historical evidence
- Corrected reimport bounds: `validation/reimport_evaluated_bounds_corrected.json` records bounded Blender depsgraph measurements for idle, attack, and move proof scenes after `io_pdx_mesh` reimport
- Action export reports: provider idle and attack reports plus `blender/reports/author_locomotion_action.json` and the move export report

## Runtime handoff state

- Production entity registration: `gfx/entities/chaosx_3d_model_pilots.gfx` and `gfx/entities/chaosx_3d_model_pilots.asset`; the GFX meshsettings name is `Mesh_0.001`, matching the exported mesh object
- Unit texticon registration: `interface/chaosx_3d_model_pilots.gfx` maps `unit_chaosx_anomaly_recon_trooper_icon_small` to the verified vanilla infantry icon
- Production animation registration: `gfx/models/units/chaosx_3d_model_pilots/animation_chaosx_3d_model_pilots.asset`
- Production consumer definition: `common/units/chaosx_3d_model_pilots.txt`, token `chaosx_anomaly_recon_trooper`
- Runtime artifacts: `gfx/models/chaosx_3d_model_pilots/chaosx_anomaly_recon_trooper.mesh`, `gfx/models/chaosx_3d_model_pilots/texture_0.dds`, `gfx/models/chaosx_3d_model_pilots/texture_normal.dds`, `gfx/models/chaosx_3d_model_pilots/texture_specular.dds`, and `gfx/models/units/chaosx_3d_model_pilots/*.anim`
- Proposed entity: `chaosx_anomaly_recon_trooper_entity`
- Live consumer evidence: prepared isolated showcase consumer; the offline repair also removes the prior move-scale collapse, material-channel mismatch, and stale building placement.
- The source/runtime defects are corrected offline: the final mesh uses the vanilla-supported `PdxMeshAdvanced` material route, the GFX object name matches the exported mesh, the PDX packed material channels are installed, the export-time armature bind transform is unit-stable, explicit diffuse/normal/specular maps are installed, the watertight geometry source is bound to the provider rig, the pilot mesh carries its calibrated runtime height with neutral entity scale `1.0`, and a real move action is registered.
- Crosswalk: `runtime/crosswalk.md`
- Parent handoff: `runtime/handoff.md`

Completion note: provider lineage, vanilla scale calibration, Blender checkpoints, resized texture, `.mesh`, `.anim`, reimport proof, and runtime handoff are current.
The pilot remains `needs_user_review` until the corrected unit is visibly confirmed in the live HOI4 showcase.

## Runtime issue record

- `MAX_TEXTURE_SIZE`: fixed by rebuilding `texture_0.dds`, `texture_normal.dds`, and `texture_specular.dds` at `1024 x 1024`.
- Missing `unit_chaosx_anomaly_recon_trooper_icon_small`: fixed by registering the custom texticon in `interface/chaosx_3d_model_pilots.gfx`.
- Unit-size mismatch: the vanilla infantry mesh remains a read-only reference at `7.351824` source units, while the pilot mesh is baked to `1.8379560709` source units and uses neutral entity scale `1.0` for the same expected effective height.
- White/black material and missing-surface symptom: fixed offline by packing Meshy metallic and roughness maps into the PDX `spec` channel layout, binding the generated diffuse/normal/specular maps, and matching `meshsettings.name` to the exported `Mesh_0.001` object.
- Moving disappearance: fixed offline by baking the uniform armature object scale into armature data, preserving mesh-unit animation translations, and exporting a dedicated 24-frame in-place move action with no scale channels; live confirmation remains pending.
