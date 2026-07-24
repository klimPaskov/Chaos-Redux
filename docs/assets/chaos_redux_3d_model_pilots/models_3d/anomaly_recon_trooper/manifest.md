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
- Generation candidate: 420,480 triangles; archived in `provider/downloads/generation_model.glb`
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
- Export preset: selected working mesh/armature only, triangulated, `exp_selected=true`, shared-vertex export with `split_verts=false`; this keeps the final 30,000-triangle mesh at 32,993 exported vertices instead of the 90,000-vertex per-loop stream consistent with the live stretched-geometry symptom
- Source and rig/action checkpoints: `blender/checkpoints/`; corrected action checkpoints are `08_runtime_candidate_sanitized_attack.blend`, `08_runtime_candidate_sanitized_idle.blend`, and `08_runtime_candidate_sanitized_move.blend`
- Vanilla reference staging: `blender/reference/western_european_infantry.mesh`; source checksum and read-only staging evidence are in `blender/reports/vanilla_reference_stage.json`
- Working geometry: one Blender mesh object `char1.001` exported as `.mesh` object `char1.002`, 30,000 triangles, 36,990 source vertices, one UV layer, one explicitly textured PDX material, one armature with 24 bones
- Normalized source-mesh height: `7.351824` target units against the measured vanilla infantry mesh; corrected runtime-candidate geometry measures `7.351824` units after evaluated-vertex normalization
- QA: 0 non-manifold edges, 0 degenerate faces, no negative scale objects
- Review warning: 31,520 loose boundary edges remain in the provider geometry and are carried as a visible review item; the Blender front, rear, and three-quarter previews show the complete head, torso, limbs, gloves, trousers, and boots, but the provider mesh remains an open-surface asset rather than a watertight body
- Provider-only `Icosphere` and `Icosphere.001` objects are explicitly excluded from working/render/export collections; the source remains preserved for audit
- The final shared-vertex payload reimports at 32,993 vertices with the same 30,000 triangles and calibrated bounds; the post-fix live renderer check and screenshot remain pending because HOI4 was not launched.
- Vanilla calibration reference: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`
- Vanilla entity reference: `gfx/entities/units_infantry.asset#infantry_rifle_entity`, runtime `scale = 0.8`
- Reference measurement: main imported `polySurface106` height `7.3518248` source units, collision geometry excluded, `-Y` forward and `+Z` up; effective runtime height `5.8814594` units
- Corrected pilot normalization: Blender target `7.3518242835` source units, runtime entity scale `0.8`, and expected effective runtime height `5.8814594268` source units, matching the vanilla infantry reference calibration
- Animation sanitation: the provider working actions had 72 root/bone scale F-curves removed, non-unit `Hips` pose scale reset to `(1, 1, 1)`, the authored move action was created without scale channels, and every exported animation translation sample was divided by the uniform armature world scale so animation coordinates use mesh units

## Textures and PDX exports

- DDS evidence: `blender/reports/textures_dds.json`
- DDS backend: repository `convert_to_dds.py` using its verified ffmpeg backend; the texture report records each conversion log
- Runtime DDS dimensions: `1024 x 1024`, one-level uncompressed BGRA; the prior `2048 x 2048` texture exceeded the observed HOI4 model-texture limit
- Runtime textures: `textures/dds/texture_0.dds` (diffuse), `textures/dds/texture_normal.dds` (normal), and `textures/dds/texture_specular.dds` (PDX packed specular/roughness)
- PDX material shader: `PdxMeshAdvanced`, with explicit diffuse, normal, and specular bindings
- PDX normal packing: red `0`, green source tangent X, blue `0`, alpha source tangent Y; source maps and checksums are recorded in `blender/reports/pdx_normal_pack.json`
- PDX specular packing: red `0`, green `32` specular level, blue metallic, alpha roughness; source maps are recorded in `blender/reports/pdx_material_pack.json`
- Mesh: `export/mesh/chaosx_anomaly_recon_trooper.mesh`, 3,002,135 bytes, SHA-256 `E19341177161BF2AAA721A6A9FC77037ED77E8975ED4FB07B497C663E15D9683`
- Runtime DDS: `textures/dds/texture_0.dds`, 4,194,432 bytes, SHA-256 `FB4886FDA5FBF1FE0634556BD53BAC4A9DFAD603D2E7890B7D858F6A0F9F390D`
- Runtime normal DDS: `textures/dds/texture_normal.dds`, 4,194,432 bytes, SHA-256 `E23A43045A419AAFB61AD6F49370D946D7A5EC7A2B94D9636E90A571E4FB16F1`
- Runtime specular DDS: `textures/dds/texture_specular.dds`, 4,194,432 bytes, SHA-256 `E22BA0B1A2BD79D133DF7B5D28D5DDD65BD7D36C3AD4648D7605B15FD36B515F`
- Idle action: `export/anim/chaosx_anomaly_recon_trooper_idle.anim`, 77,395 bytes, SHA-256 `72F6C722052DC7CBDCC76CC23CB99D111252A06778724F1548E11EBF74A815CB`, frames `0-97`, 24 fps, loop, no scale channels
- Attack action: `export/anim/chaosx_anomaly_recon_trooper_attack.anim`, 55,123 bytes, SHA-256 `C42D5507BD8549C055C0840491A22A913139A0B2C488E3AB652E3A140FFC14C0`, frames `0-68`, 24 fps, non-loop, unit root scale
- Move action: `export/anim/chaosx_anomaly_recon_trooper_move.anim`, 21,331 bytes, SHA-256 `2C6D5B504887722E8588D9D666D6DF84DB097B930FD4C2C8F0C6A3982C646B74`, frames `0-24`, 24 fps, loop, Blender-authored in place with a root translation channel and no scale channels
- Mesh reimport: corrected `validation/reimport_chaosx_anomaly_recon_trooper_attack_corrected.json`, `validation/reimport_chaosx_anomaly_recon_trooper_idle_corrected.json`, and `validation/reimport_chaosx_anomaly_recon_trooper_move_corrected.json`
- Corrected reimport bounds: `validation/reimport_evaluated_bounds_corrected.json` records bounded Blender depsgraph measurements for idle, attack, and move proof scenes after `io_pdx_mesh` reimport
- Action export reports: provider idle and attack reports plus `blender/reports/author_locomotion_action.json` and the move export report

## Runtime handoff state

- Production entity registration: `gfx/entities/chaosx_3d_model_pilots.gfx` and `gfx/entities/chaosx_3d_model_pilots.asset`; the GFX meshsettings name is `char1.002`, matching the exported mesh object
- Unit texticon registration: `interface/chaosx_3d_model_pilots.gfx` maps `unit_chaosx_anomaly_recon_trooper_icon_small` to the verified vanilla infantry icon
- Production animation registration: `gfx/models/units/chaosx_3d_model_pilots/animation_chaosx_3d_model_pilots.asset`
- Production consumer definition: `common/units/chaosx_3d_model_pilots.txt`, token `chaosx_anomaly_recon_trooper`
- Runtime artifacts: `gfx/models/chaosx_3d_model_pilots/chaosx_anomaly_recon_trooper.mesh`, `gfx/models/chaosx_3d_model_pilots/texture_0.dds`, `gfx/models/chaosx_3d_model_pilots/texture_normal.dds`, `gfx/models/chaosx_3d_model_pilots/texture_specular.dds`, and `gfx/models/units/chaosx_3d_model_pilots/*.anim`
- Proposed entity: `chaosx_anomaly_recon_trooper_entity`
- Live consumer evidence: prepared isolated showcase consumer; the offline repair also removes the prior move-scale collapse, material-channel mismatch, and stale building placement.
- The source/runtime defects are corrected offline: the final mesh uses the vanilla-supported `PdxMeshAdvanced` material route, the GFX object name matches the exported mesh, the PDX packed material channels are installed, animation scale and translation tracks are unit-stable, explicit diffuse/normal/specular maps are installed, the model is normalized to the vanilla infantry source mesh, and a real move action is registered.
- Crosswalk: `runtime/crosswalk.md`
- Parent handoff: `runtime/handoff.md`

Completion note: provider lineage, vanilla scale calibration, Blender checkpoints, resized texture, `.mesh`, `.anim`, reimport proof, and runtime handoff are current.
The pilot remains `needs_user_review` until the corrected unit is visibly confirmed in the live HOI4 showcase.

## Runtime issue record

- `MAX_TEXTURE_SIZE`: fixed by rebuilding `texture_0.dds`, `texture_normal.dds`, and `texture_specular.dds` at `1024 x 1024`.
- Missing `unit_chaosx_anomaly_recon_trooper_icon_small`: fixed by registering the custom texticon in `interface/chaosx_3d_model_pilots.gfx`.
- Unit-size mismatch: the corrected Blender export is calibrated to the imported vanilla infantry mesh and the pilot entity uses the matching vanilla consumer calibration `scale = 0.8`.
- White/black material and missing-surface symptom: fixed offline by packing Meshy metallic and roughness maps into the PDX `spec` channel layout and matching `meshsettings.name` to the exported `char1.002` object.
- Moving disappearance: fixed offline by normalizing every exported animation scale sample and translation sample into mesh units and exporting a dedicated 24-frame in-place move action with no scale channels; live confirmation remains pending.
