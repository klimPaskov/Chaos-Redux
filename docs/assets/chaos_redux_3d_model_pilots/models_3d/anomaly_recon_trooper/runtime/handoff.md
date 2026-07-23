# Runtime handoff: anomaly recon trooper

Status: runtime consumer repaired; in-game renderer proof pending.

The standalone showcase originally relied on history-only seeding, which did not produce a visible division in the user's Germany run.
The active showcase copy now creates the locked pilot template, places the division at startup, and retries through a Germany-only daily repair hook for an already-open save.
The template is created in Germany's country scope, and the live `create_unit` call executes directly in state 64, where the effect is valid.

## Production registration

- Object type: `chaosx_anomaly_recon_trooper_mesh`
- Source `.mesh`: `export/mesh/chaosx_anomaly_recon_trooper.mesh`
- Runtime `.mesh`: `gfx/models/chaosx_3d_model_pilots/chaosx_anomaly_recon_trooper.mesh`
- Entity: `chaosx_anomaly_recon_trooper_entity`
- Entity definition: `gfx/entities/chaosx_3d_model_pilots.asset`
- Object definition: `gfx/entities/chaosx_3d_model_pilots.gfx`
- Unit consumer: `chaosx_anomaly_recon_trooper` in `common/units/chaosx_3d_model_pilots.txt`
- Live consumer effect: `common/scripted_effects/chaosx_3d_model_pilot_showcase_effects.txt`
- Live consumer hooks: `common/on_actions/chaosx_3d_model_pilot_showcase_on_actions.txt`
- Live unit placement: Germany, province 6521, division `Chaos Redux Pilot Trooper`; the beacon building is placed separately in Brandenburg state 64, province 11219 at map coordinate `2996, 9.70, 1588`, using the custom `building_anomaly_signal_beacon_pilot_spawn` row where the map building table has no vanilla row.
- Animation asset: `gfx/models/units/chaosx_3d_model_pilots/animation_chaosx_3d_model_pilots.asset`
- Idle binding: `idle` -> `chaosx_anomaly_recon_trooper_idle_animation` -> `chaosx_anomaly_recon_trooper_idle.anim`
- Attack binding: `attack` -> `chaosx_anomaly_recon_trooper_attack_animation` -> `chaosx_anomaly_recon_trooper_attack.anim`
- Move binding: `move`/`retreat` -> `chaosx_anomaly_recon_trooper_move_animation` -> `chaosx_anomaly_recon_trooper_move.anim`; the action is a 24-frame in-place Blender-authored walk cycle
- Texture channels: `texture_0.dds` diffuse, `texture_normal.dds` normal, and `texture_specular.dds` PDX packed specular/roughness with red `0`, green `32`, blue metallic, and alpha roughness; shader `PdxMeshAdvanced`, final DDS `1024 x 1024` uncompressed BGRA for each map
- Exported mesh object: `char1.002`; `gfx/entities/chaosx_3d_model_pilots.gfx` uses the same `meshsettings.name`
- Vanilla scale reference: `gfx/models/units/western_european_infantry.mesh` against `gfx/entities/units_infantry.asset#infantry_rifle_entity`; source mesh target `7.351824`, entity scale `0.8`, effective runtime target `5.881459`
- Unit texticon: `interface/chaosx_3d_model_pilots.gfx` registers `unit_chaosx_anomaly_recon_trooper_icon_small` against the vanilla infantry icon
- Animation stability: the Blender worker removed all provider scale F-curves and reset the imported `Hips` pose scale; all three exported actions contain no scale channels and unit root scale values.

## Provenance and evidence

The source reference is the one-image file `refs/original/meshy_input.png`.
Meshy generation, remesh, rigging, idle, and attack task IDs are recorded in the manifest and append-only provider lineage; the move action is recorded as Blender-authored production evidence.
The official rig/animation MCP results were signed provider URLs; the job stores the downloaded artifacts and checksums, rather than leaving remote URLs as the only copy.
The exported mesh and all three skeletal actions were reimported through `io_pdx_mesh` proof scenes.
The installed vanilla infantry mesh was staged read-only and imported into each humanoid preparation scene for scale and orientation comparison.

The source provider collection retains two unwanted `Icosphere` objects, but the working/render/export collections explicitly exclude them.
The exclusion is recorded in `job.yaml`, worker reports, and this handoff so the clean live model is reproducible without editing the provider archive.

## Parent verification

The standalone showcase copy is the runtime consumer proof path.
Its unit placement and template model override are now explicit.
The user-reported texture-size, missing-texticon, scale, material-binding, and movement defects have been repaired offline; `runtime/screenshots/` remains empty until the repaired consumer is visually verified in HOI4.
