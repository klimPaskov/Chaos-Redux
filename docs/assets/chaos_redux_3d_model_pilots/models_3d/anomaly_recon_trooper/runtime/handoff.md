# Runtime handoff: anomaly recon trooper

Status: corrected offline; in-game renderer proof pending by explicit user instruction.

The standalone showcase creates the locked pilot template, places the division at startup, and retries through a Germany-only daily repair hook for an already-open save.
The template is created in Germany's country scope, and the live `create_unit` call executes directly in the state scope required by the effect.

## Production registration

- Object type: `chaosx_anomaly_recon_trooper_mesh`
- Source `.mesh`: `export/mesh/chaosx_anomaly_recon_trooper.mesh`
- Runtime `.mesh`: `gfx/models/chaosx_3d_model_pilots/chaosx_anomaly_recon_trooper.mesh`
- Humanoid entity: `chaosx_anomaly_recon_trooper_entity`
- Humanoid entity definition: `gfx/entities/chaosx_3d_model_pilots.asset`, neutral `scale = 1.0`; the calibrated mesh height is `1.8379560709` source units and the final evaluated reimport height is `1.8376898766`
- Humanoid object definition: `gfx/entities/chaosx_3d_model_pilots.gfx`
- Unit consumer: `chaosx_anomaly_recon_trooper` in `common/units/chaosx_3d_model_pilots.txt`
- Live consumer effect: `common/scripted_effects/chaosx_3d_model_pilot_showcase_effects.txt`
- Live consumer hooks: `common/on_actions/chaosx_3d_model_pilot_showcase_on_actions.txt`
- Live unit placement: Germany, province 6521, division `Chaos Redux Pilot Trooper`.
- Building consumer: `anomaly_signal_beacon_pilot` is set at province 9560 in Brandenburg state 64 by `common/scripted_effects/chaosx_3d_model_pilot_showcase_effects.txt`.
- Building entity: `building_anomaly_signal_beacon_pilot` and its spawn entity `building_anomaly_signal_beacon_pilot_spawn` are registered in `gfx/entities/chaosx_3d_model_pilots.asset`.
- Building map row: `map/buildings.txt` uses the vanilla spawn-point token `anomaly_signal_beacon_pilot_spawn` at `64;2995.00;9.70;1556.00`, an interior map pixel of province 9560 in Brandenburg under the bottom-up Z convention.
- Animation asset: `gfx/models/units/chaosx_3d_model_pilots/animation_chaosx_3d_model_pilots.asset`
- Idle binding: `idle` -> `chaosx_anomaly_recon_trooper_idle_animation` -> `chaosx_anomaly_recon_trooper_idle.anim`
- Attack binding: `attack` -> `chaosx_anomaly_recon_trooper_attack_animation` -> `chaosx_anomaly_recon_trooper_attack.anim`
- Move binding: `move`/`retreat` -> `chaosx_anomaly_recon_trooper_move_animation` -> `chaosx_anomaly_recon_trooper_move.anim`; the action is a 24-frame in-place Blender-authored walk cycle
- Texture channels: `texture_0.dds` diffuse, `texture_normal.dds` PDX normal with red `0`, green tangent X, blue `0`, and alpha tangent Y, and `texture_specular.dds` PDX packed specular/roughness with red `0`, green `32`, blue metallic, and alpha roughness; shader `PdxMeshAdvanced`, final DDS `1024 x 1024` uncompressed BGRA for each map
- Exported mesh object: `Mesh_0.001`; `gfx/entities/chaosx_3d_model_pilots.gfx` uses the same `meshsettings.name`
- Final mesh payload: shared-vertex export, 14,970 source vertices, 30,000 triangles, and 0 source loose boundary edges; the dual-source geometry comes from the watertight generation candidate while the provider armature supplies the approved actions and weights.
- Vanilla scale reference: `gfx/models/units/western_european_infantry.mesh` against `gfx/entities/units_infantry.asset#infantry_rifle_entity`; read-only source height `7.351824`, reference entity scale `0.8`, pilot mesh target `1.8379560709`, and neutral pilot entity scale `1.0`
- Transform agreement: the mesh data absorbs the `94.7711071693` mesh-to-armature scale ratio before parenting, so the exported mesh and armature share uniform world scale `0.0102108670`
- Unit texticon: `interface/chaosx_3d_model_pilots.gfx` registers `unit_chaosx_anomaly_recon_trooper_icon_small` against the vanilla infantry icon
- Animation stability: the Blender worker removes provider scale F-curves, resets the imported `Hips` pose scale, exports unit scale values, and divides exported translation samples by the uniform armature world scale so movement uses mesh units.

## Provenance and evidence

The source reference is the one-image file `refs/original/meshy_input.png`.
Meshy generation, remesh, rigging, idle, and attack task IDs are recorded in the manifest and append-only provider lineage; the move action is recorded as Blender-authored production evidence.
The official rig/animation MCP results were signed provider URLs; the job stores the downloaded artifacts and checksums, rather than leaving remote URLs as the only copy.
The corrected `.mesh` and all three corrected skeletal actions were reimported through `io_pdx_mesh` proof scenes, with 30,000 triangles, 0 position-welded loose edges, and 0 non-manifold edges recorded in the dual-source validation reports.
The installed vanilla infantry mesh was staged read-only and imported into each humanoid preparation scene for scale and orientation comparison.

The source provider collection retains two unwanted `Icosphere` objects, but the working/render/export collections explicitly exclude them.
The previous provider remesh was not exported as final geometry because its open seams became holes after reduction; the watertight generation candidate is the final geometry source, and the reimport audit distinguishes harmless UV/normal seam splits from position-welded topology.

## Parent verification

The standalone showcase copy is the runtime consumer proof path.
The source and active test-mod runtime files were synchronized and SHA-256 compared after the corrected exports.
The user-reported texture-size, missing-texticon, scale, material-binding, movement, and building-placement defects have been repaired offline; `runtime/screenshots/` remains empty because HOI4 was not launched.
