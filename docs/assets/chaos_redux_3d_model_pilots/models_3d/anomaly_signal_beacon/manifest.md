# anomaly_signal_beacon model manifest

Status: needs_user_review

## Identity

- Asset ID: `chaosx.model.pilot.anomaly_signal_beacon`
- Profile: `static_prop`
- Provider: Meshy `@meshy-ai/meshy-mcp-server` `0.4.0`, model `meshy-6`
- Runtime stem: `chaosx_anomaly_signal_beacon`
- Candidate selection: the single generated Meshy image-to-3D result; no paid retry

## One-image gate

- Meshy input: `refs/original/meshy_input.png`
- Image count: `1`
- SHA-256: `19D9A3824C1299EE7A28720E058309FFA77F007A3C9470FD8B2FE87ECE9F617F`
- Source mode: built-in image generation, user-authorized pilot reference
- Side-profile sheet: not created
- Multi-view/turnaround board: not created

## Provider lineage

- Image-to-3D task: `019f8a2f-796c-719f-bee6-5fd4e362d1c1`
- Request/response/task/credit records: `provider/requests/`, `provider/responses/`, `provider/tasks/generation.json`, `provider/credits/`
- Canonical provider files: `provider/downloads/generation_model.glb` and `provider/downloads/generation_model.fbx`
- Provider candidate gate: `validation/provider_candidate_gate.json`
- Paid generation: one attempt; no paid retry

## Blender and geometry evidence

- Blender: `5.1.2` (`ec6e62d40fa9`)
- Adapter: `chaosx_blender_hoi4` `1.0.0`
- Exporter: `io_pdx_mesh` `0.91.0`, archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`
- Export preset: selected working mesh only, triangulated, `exp_selected=true`, `split_verts=true`; the split-vertex setting is required for the pinned 0.91 exporter to avoid its quadratic unsplit-vertex path
- Source checkpoint: `blender/checkpoints/00_imported.blend`
- Pre-export checkpoint: `blender/checkpoints/05_pre_export.blend`
- Export checkpoint: `blender/checkpoints/06_exported.blend`
- Working geometry: one Blender mesh object, `Mesh_0.001`, exported as `.mesh` object `Mesh_0.002`, 5,202 triangles, 4,711 source vertices, one UV layer, one PDX material
- Bounds: approximately `0.668 x 0.619 x 1.503 m`; normalized height target `1.5 m`
- QA: 0 non-manifold edges, 0 degenerate faces, no negative scale objects
- Review warning: 3,586 loose boundary edges remain in the provider geometry and are carried as a visible review item
- Rendered preview set: `blender/previews/`; parent visual review recorded in `validation/provider_candidate_gate.json`

## Textures and PDX export

- Processed source maps: `textures/processed/`
- DDS evidence: `blender/reports/textures_dds.json`
- DDS backend: repository `convert_to_dds.py` using its verified ffmpeg backend; the texture report records each conversion log
- Runtime DDS dimensions: `1024 x 1024` for `Image_0.dds` through `Image_3.dds`; the prior `2048 x 2048` maps exceeded the observed HOI4 model-texture limit
- DDS SHA-256: `Image_0` `1C51F4468EEC000A3706930FF598BAB8A2926B943AEB75BB7BD2E5DDA634A534`; `Image_1` `EABC8186B94A6D51E2C36B543B28C9EAD82CFF091A794633526BF891B822E2C7`; `Image_2` `9FCE01EB4B6B417E836D06CC670A21602D038DA6AA876FC01D889D5AA545892F`; auxiliary `Image_3` `F5D9DDB268DB8AB4CFD7CA4AEC315628B06C7CA90A08B8E0C1F6D8ACA65235A0`
- Runtime maps: `Image_0.dds` diffuse, `Image_1.dds` specular, `Image_2.dds` normal; `Image_3.dds` retained as extracted auxiliary evidence
- PDX material shader: `PdxMeshAdvanced`, with the three runtime texture channels explicitly registered in the entity GFX
- PDX normal packing: red `0`, green source tangent X, blue `0`, alpha source tangent Y
- Mesh export: `export/mesh/chaosx_anomaly_signal_beacon.mesh`
- Mesh bytes: `811835`
- Mesh SHA-256: `93D6DF50C8F58192CF597CF708DB144DDF80A0A132E8841BDBF4DE402937E9E6`
- Export report: `blender/reports/export_mesh.json`
- Reimport proof: `blender/checkpoints/reimport_chaosx_anomaly_signal_beacon_mesh.blend`
- Reimport report: `validation/reimport_chaosx_anomaly_signal_beacon_mesh.json`

## Runtime handoff state

- Production entity registration: `gfx/entities/chaosx_3d_model_pilots.gfx` and `gfx/entities/chaosx_3d_model_pilots.asset`; entity `building_anomaly_signal_beacon_pilot_spawn` uses the GFX meshsettings name `Mesh_0.002`, matching the exported mesh object
- Production consumer definition: `common/buildings/chaosx_3d_model_pilots.txt`, token `anomaly_signal_beacon_pilot`
- Runtime artifact: `gfx/models/chaosx_3d_model_pilots/chaosx_anomaly_signal_beacon.mesh`
- Runtime maps: `Image_0.dds`, `Image_1.dds`, and `Image_2.dds`; each final map is `1024 x 1024` one-level uncompressed BGRA
- Proposed entity: `building_anomaly_signal_beacon_pilot_spawn`
- Live consumer evidence: prepared isolated showcase consumer; the beacon map row is `64;anomaly_signal_beacon_pilot_spawn;2996.00;9.70;1588.00;0.00;0` inside Brandenburg state 64 and province 11219, with no vanilla building row at that coordinate. Live HOI4 renderer launch and screenshot capture were explicitly waived by the user on 2026-07-22.
- Crosswalk: `runtime/crosswalk.md`
- Parent handoff: `runtime/handoff.md`

Completion note: provider lineage, Blender checkpoints, corrected texture maps, `.mesh`, reimport proof, and runtime handoff are current.
The pilot remains `needs_user_review` until the corrected building is visibly confirmed in the live HOI4 showcase.
