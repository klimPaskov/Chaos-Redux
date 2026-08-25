# cannibal_siege_eaters runtime handoff

Status: **package complete; parent runtime wiring installed**.

The parent-approved source-informed reference remains `refs/original/meshy_input.png`, SHA-256 `1AC18B9B008CCCC70BC0AF30605CA72ADCC9030A1C233732559400C9A6744F75`. The Meshy 7 provider mesh and genuine provider animations are retained; no transform-only replacement actions were authored.

The live `chaosx_blender_hoi4` 1.10.14 adapter exported the 29,999-triangle mesh and eight provider actions at 24 fps. Each action was corrected with the adapter's `per_frame_root_contact_zero_clearance` policy using root bone `Hips`, retaining body-motion keys and changing only root location channels. The grounded exports were reimported successfully with proofs and rendered previews:

- `blender/checkpoints/reimport_cannibal_siege_eaters_idle_grounded_v3.blend`
- `blender/checkpoints/reimport_cannibal_siege_eaters_move_grounded_v3.blend`
- `blender/checkpoints/reimport_cannibal_siege_eaters_attack_grounded_v3.blend`
- `blender/checkpoints/reimport_cannibal_siege_eaters_defend_grounded_v3.blend`
- `blender/checkpoints/reimport_cannibal_siege_eaters_support_attack_grounded_v3.blend`
- `blender/checkpoints/reimport_cannibal_siege_eaters_retreat_grounded_v3.blend`
- `blender/checkpoints/reimport_cannibal_siege_eaters_training_grounded_v3.blend`
- `blender/checkpoints/reimport_cannibal_siege_eaters_death_grounded_v3.blend`

Ground-contact evidence is within adapter tolerance for all eight reimports. The mesh reports zero non-manifold and degenerate faces after position-weld diagnostics; 77 loose boundary edges remain across 16 open components because exported UV and normal seams are preserved.

Runtime files are installed under `gfx/models/units/014_cannibalism/cannibal_siege_eaters/` with unique diffuse, specular, and normal DDS maps, and under `sound/014_cannibalism/units/cannibal_siege_eaters/` with seven sourced PCM s16le 44,100 Hz mono WAV roles. `gfx/entities/014_cannibalism_units.gfx`, `gfx/entities/014_cannibalism_units.asset`, and `sound/014_cannibalism_units_sound.asset` bind the eight actions, terrain clones, and action-timed sound effects. The parent-owned unit definition already maps `cannibal_siege_eaters` to `cannibal_siege_eaters_entity`.

No live in-game consumer validation is claimed. The remaining package note is the documented open-surface boundary diagnostic; it is not silently treated as a topology pass.
