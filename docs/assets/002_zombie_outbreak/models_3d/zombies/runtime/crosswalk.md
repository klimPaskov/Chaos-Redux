# Requirement-to-runtime crosswalk

| Requirement | Evidence | Runtime status |
| --- | --- | --- |
| Exactly one base zombie model | `job.yaml`, `evidence/one_image_gate.json`, `refs/original/meshy_input.png` | source identity complete |
| Complete human corpse silhouette | `blender/previews/chaosx_zombies_rig_gate_front.png`, `blender/previews/chaosx_zombies_rig_gate_three_quarter.png` | visual gate passed |
| Vanilla-calibrated scale | `validation/reimport_vanilla_infantry_calibration.json`, `evidence/geometry_gate.json`, `validation/runtime_wiring.json` | runtime entity scale `0.8` registered exactly once |
| Manifold 30k final mesh | `blender/reports/final_working_material_inspect.json`, `validation/export_byte_parse.json` | `.mesh` exported and reimport evidence passed |
| PdxMeshAdvanced textures | `blender/reports/pdx_runtime_texture_processing.json`, `blender/reports/textures_dds.json`, exported mesh text | processed PNG/DDS and material binding complete |
| Humanoid rig | `provider/downloads/rigged_provider_model.glb`, `blender/checkpoints/03_rig_approved.blend` | rig gate passed |
| Idle | `provider/downloads/animation_idle.glb`, `export/anim/chaosx_zombies_idle.anim`, `validation/reimport_chaosx_zombies_idle.json` | passed |
| Move/shamble | `provider/downloads/animation_move.glb`, `export/anim/chaosx_zombies_move.anim`, `validation/reimport_chaosx_zombies_move.json` | passed with minor sampled sole-contact risk |
| Attack | `blender/reports/correct_action_grounding.json`, `export/anim/chaosx_zombies_attack.anim`, `validation/reimport_chaosx_zombies_attack.json` | corrected existing action and passed |
| Death | `provider/downloads/animation_death.glb`, `export/anim/chaosx_zombies_death.anim`, `validation/reimport_chaosx_zombies_death.json` | passed |
| Actual-byte export reimport | `validation/export_byte_parse.json` | passed for one mesh and four animations |
| Runtime registration | `validation/runtime_wiring.json`, `gfx/entities/chaosx_zombies.gfx`, `gfx/entities/chaosx_zombies.asset`, `common/units/zombies.txt` | registered for the base `zombies` unit only |
| Live HOI4 verification | none | user-owned and pending; game was not launched |
