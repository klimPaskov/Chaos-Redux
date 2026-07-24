# Runtime handoff: anomaly signal beacon

Status: runtime consumer repaired; in-game renderer proof pending.

The standalone showcase originally relied on history-only seeding, which did not produce a visible building in the user's Germany run.
The active showcase copy now applies the building at startup and through a Germany-only daily repair hook, so a live save can receive the consumer without a history-file override.
The building write is isolated in a state-scoped effect; it is not combined with the country-scoped template setup.

## Production registration

- Object type: `chaosx_anomaly_signal_beacon_mesh`
- Source `.mesh`: `export/mesh/chaosx_anomaly_signal_beacon.mesh`
- Runtime `.mesh`: `gfx/models/chaosx_3d_model_pilots/chaosx_anomaly_signal_beacon.mesh`
- Entity: `building_anomaly_signal_beacon_pilot_spawn`
- Entity definition: `gfx/entities/chaosx_3d_model_pilots.asset`
- Entity scale: `3.280031` for both the visible entity and spawn entity, matching the vanilla special-project facility rendered height of `4.929816` source units
- Object definition: `gfx/entities/chaosx_3d_model_pilots.gfx`
- Consumer: `anomaly_signal_beacon_pilot` in `common/buildings/chaosx_3d_model_pilots.txt`
- Live consumer effect: `common/scripted_effects/chaosx_3d_model_pilot_showcase_effects.txt`
- Live consumer hooks: `common/on_actions/chaosx_3d_model_pilot_showcase_on_actions.txt`
- Live placement: Brandenburg state 64, province 9560 at map coordinate `2995, 9.70, 1556`, level 1; the coordinate is an interior pixel of province 9560 using the map's bottom-up Z convention. The scripted effect selects the exact province with `province = { id = 9560 }`, and province 9560 has no province-specific building in the vanilla state history.
- Diffuse channel: `Image_0.dds`
- Specular channel: `Image_1.dds`
- Normal channel: `Image_2.dds`
- Final texture size: `1024 x 1024` for each runtime map; the earlier 2048 maps were rejected by the engine texture ceiling
- Shader: `PdxMeshAdvanced`
- Exported mesh object: `Mesh_0.002`; `gfx/entities/chaosx_3d_model_pilots.gfx` uses the same `meshsettings.name`.

## Provenance and evidence

The source reference is the one-image file `refs/original/meshy_input.png`.
Meshy task `019f8a2f-796c-719f-bee6-5fd4e362d1c1` produced the archived GLB/FBX candidate.
The selected Blender working collection was exported with the locked `io_pdx_mesh` `0.91.0` extension and reimported successfully.
The loose-boundary edge warning is carried forward in the manifest and QA summary; it is not hidden behind the successful export.

## Parent verification

The standalone showcase copy is the runtime consumer proof path.
Its building placement is now explicit and idempotent; `runtime/screenshots/` remains empty until the repaired consumer is visually verified in HOI4.
