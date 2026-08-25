# Event 014 March Predation Column runtime handoff

Status: accepted parent-owned runtime tranche with a documented provider-action caveat.

The parent-approved source remains `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/refs/original/meshy_input.png`, SHA-256 `9523DBF13601E7AE8ACB3B58013700209D19BCA6C3866B8932FB6E8D18C91289`. The live `chaosx_blender_hoi4` 1.10.14 adapter exported a 30,000-triangle mesh and eight genuine provider actions at 30 fps from the saved grounded checkpoints. The current proof reimports use deliberately short proof stems (`march_idle`, `march_move`, `march_attack`, `march_defend`, `march_support_attack`, `march_retreat`, `march_training`, `march_death`) because the synced OneDrive path exceeds the Windows 260-character limit when the full unit slug is embedded in each three-quarter preview filename.

Reimport proof checkpoints are:

- `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/blender/checkpoints/reimport_march_idle.blend`
- `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/blender/checkpoints/reimport_march_move.blend`
- `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/blender/checkpoints/reimport_march_attack.blend`
- `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/blender/checkpoints/reimport_march_defend.blend`
- `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/blender/checkpoints/reimport_march_support_attack.blend`
- `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/blender/checkpoints/reimport_march_retreat.blend`
- `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/blender/checkpoints/reimport_march_training.blend`
- `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/blender/checkpoints/reimport_march_death.blend`

The preview PNGs are now copied into the package's regular `blender/previews/` directory, with the short proof stems preserved. The source provider bow remains attached in the attack previews and no hand-authored transform-only replacement was introduced; exact draw/release semantics remain a visual-source caveat.

Runtime files are installed under `gfx/models/units/014_cannibalism/cannibal_march_predation_column/` with 1024px unique diffuse, specular, and normal DDS maps and eight action files. Seven sourced PCM s16le 44,100 Hz mono WAV roles are installed under `sound/014_cannibalism/units/cannibal_march_predation_column/`. Parent-owned GFX, entity, and sound registries bind all actions, terrain clones, and action-timed effects. The unit definition already consumes `cannibal_march_predation_column_entity`.

Adapter topology is zero non-manifold and zero degenerate faces after position-weld diagnostics, with 126 loose boundary edges across 31 open components preserved as source seams. No live in-game consumer validation is claimed.
