# Runtime crosswalk: anomaly recon trooper

| Requirement | Source evidence | Runtime surface | State |
| --- | --- | --- | --- |
| One Meshy input image | `refs/original/meshy_input.png`, SHA-256 `2965C0B7A50F79CA8D48CB59ED2707553BB81194CAB801B4EC5F706AF73907EC` | Meshy image-to-3D request | complete |
| Standard humanoid geometry | `provider/downloads/rigged_provider_model.glb`; action checkpoints | `chaosx_anomaly_recon_trooper_mesh` | complete |
| Rig | provider rig task `019f8a71-3c36-7999-b9ce-fc1b31b70b67`; 24-bone reimport proof | humanoid entity armature | complete |
| Idle action | `export/anim/chaosx_anomaly_recon_trooper_idle.anim`, 24 fps, frames 0-97 | entity state `idle` | complete |
| Attack action | `export/anim/chaosx_anomaly_recon_trooper_attack.anim`, 24 fps, frames 0-68 | entity states `attack`/`defend`/`support_attack` | complete |
| Move action | `export/anim/chaosx_anomaly_recon_trooper_move.anim`, 24 fps, frames 0-24, Blender-authored in place | entity states `move`/`retreat` | complete |
| PDX material channels | `blender/reports/textures_dds.json`, `blender/reports/pdx_material_pack.json`; diffuse and normal maps plus PDX packed specular layout | `texture_0.dds`, `texture_normal.dds`, `texture_specular.dds`; GFX object `char1.002` | complete |
| Texture size gate | `blender/reports/textures_dds.json`; 1024 x 1024 DDS headers | `gfx/models/chaosx_3d_model_pilots/texture_0.dds`, `texture_normal.dds`, `texture_specular.dds` | corrected; pending live check |
| Vanilla unit scale | `western_european_infantry.mesh` source height 7.351824; reference entity scale 0.8; pilot consumer scale 0.8; expected effective pilot height 5.881459 | `chaosx_anomaly_recon_trooper_entity` | corrected; pending live check |
| Unit texticon | `interface/chaosx_3d_model_pilots.gfx` | `unit_chaosx_anomaly_recon_trooper_icon_small` | registered; pending live check |
| `.mesh` export | shared-vertex `export/mesh/chaosx_anomaly_recon_trooper.mesh`, 32,993 vertices | runtime `.mesh` | complete |
| Reimport proof | idle/attack/move validation JSON and proof `.blend` files | exporter/importer path | complete |
| Live unit consumer | `common/units/chaosx_3d_model_pilots.txt` | `chaosx_anomaly_recon_trooper` | registered |
| Animation translation units | Corrected Blender worker export reports; translation samples divided by uniform armature world scale after provider actions were authored in armature units | idle, attack, and move `.anim` files | corrected; pending live check |
| Live runtime placement | `common/scripted_effects/chaosx_3d_model_pilot_showcase_effects.txt`; `common/on_actions/chaosx_3d_model_pilot_showcase_on_actions.txt`; `map/buildings.txt`; `history/states/64-Brandenburg.txt` | Troop in Germany province 6521; beacon in Brandenburg state 64, province 9560 at map coordinate `2995, 9.70, 1556` using the `anomaly_signal_beacon_pilot_spawn` spawn-point row and registered `building_anomaly_signal_beacon_pilot_spawn` entity | wired; pending live check |
| In-game renderer proof | `runtime/screenshots/` | unit entity | pending |
