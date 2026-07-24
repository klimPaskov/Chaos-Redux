# Runtime crosswalk: anomaly signal beacon

| Requirement | Source evidence | Runtime surface | State |
| --- | --- | --- | --- |
| One Meshy input image | `refs/original/meshy_input.png`, SHA-256 `19D9A3824C1299EE7A28720E058309FFA77F007A3C9470FD8B2FE87ECE9F617F` | Meshy image-to-3D request | complete |
| Occult beacon geometry | `provider/downloads/generation_model.glb`; `blender/checkpoints/05_pre_export.blend` | `chaosx_anomaly_signal_beacon_mesh` | complete |
| PDX material channels | `blender/reports/textures_dds.json`, `blender/reports/pdx_material_pack.json` | `Image_0.dds`, `Image_1.dds`, `Image_2.dds`; GFX object `Mesh_0.002` | complete |
| Texture size gate | `blender/reports/textures_dds.json`; 1024 x 1024 DDS headers | `Image_0.dds`, `Image_1.dds`, `Image_2.dds` | corrected; pending live check |
| `.mesh` export | `export/mesh/chaosx_anomaly_signal_beacon.mesh` | `gfx/models/chaosx_3d_model_pilots/chaosx_anomaly_signal_beacon.mesh` | complete |
| Reimport proof | `validation/reimport_chaosx_anomaly_signal_beacon_mesh.json` | exporter/importer path | complete |
| Static runtime consumer | `common/buildings/chaosx_3d_model_pilots.txt` | `anomaly_signal_beacon_pilot` | registered |
| Live runtime placement | `common/scripted_effects/chaosx_3d_model_pilot_showcase_effects.txt`; `common/on_actions/chaosx_3d_model_pilot_showcase_on_actions.txt`; `map/buildings.txt`; `history/states/64-Brandenburg.txt` | Brandenburg state 64, province 9560 at map coordinate `2998, 9.70, 1552` using `building_anomaly_signal_beacon_pilot_spawn`; the effect selects `province = { id = 9560 }` | wired; pending live check |
| In-game renderer proof | `runtime/screenshots/` | building entity | pending |
