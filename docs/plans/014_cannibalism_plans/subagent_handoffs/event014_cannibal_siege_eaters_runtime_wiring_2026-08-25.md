# Event 014 Siege Eaters runtime handoff

Status: accepted parent-owned runtime tranche.

The approved source-informed Meshy input is unchanged at `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/refs/original/meshy_input.png`. The live `chaosx_blender_hoi4` 1.10.14 adapter exported the 29,999-triangle Meshy 7 mesh and all eight provider actions, then corrected only root-location channels with the `per_frame_root_contact_zero_clearance` policy on `Hips` and reimported every action successfully.

Grounded proof checkpoints are:

- `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/blender/checkpoints/reimport_cannibal_siege_eaters_idle_grounded_v3.blend`
- `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/blender/checkpoints/reimport_cannibal_siege_eaters_move_grounded_v3.blend`
- `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/blender/checkpoints/reimport_cannibal_siege_eaters_attack_grounded_v3.blend`
- `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/blender/checkpoints/reimport_cannibal_siege_eaters_defend_grounded_v3.blend`
- `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/blender/checkpoints/reimport_cannibal_siege_eaters_support_attack_grounded_v3.blend`
- `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/blender/checkpoints/reimport_cannibal_siege_eaters_retreat_grounded_v3.blend`
- `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/blender/checkpoints/reimport_cannibal_siege_eaters_training_grounded_v3.blend`
- `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/blender/checkpoints/reimport_cannibal_siege_eaters_death_grounded_v3.blend`

Runtime files were copied to `gfx/models/units/014_cannibalism/cannibal_siege_eaters/` and `sound/014_cannibalism/units/cannibal_siege_eaters/`. Parent-owned wiring now exists in `gfx/entities/014_cannibalism_units.gfx`, `gfx/entities/014_cannibalism_units.asset`, and `sound/014_cannibalism_units_sound.asset`, with eight action states, snow/desert clones, seven sourced 44,100 Hz mono sound roles, and action-timed effects. The unit definition already consumes `cannibal_siege_eaters_entity`.

Adapter diagnostics report zero non-manifold and degenerate faces after position-weld inspection, with 77 loose boundary edges across 16 open components preserved as documented source seams. No in-game validation is claimed.

Changed files: runtime model/sound binaries, `gfx/models/units/014_cannibalism/cannibal_siege_eaters/animation_cannibal_siege_eaters.asset`, the three parent entity/GFX/sound registries, the package manifest, and the package runtime handoff.
