# Requirement-to-runtime crosswalk

| Requirement | Evidence / runtime | Status |
| --- | --- | --- |
| one approved Meshy input | `refs/original/meshy_input.png`, SHA-256 `671e5197...4905dc` | complete |
| generic retro-WW2 biped and twin integrated arm MGs | accepted candidate and action contact sheets under `previews/` | passed |
| calibrated scale | vanilla source `7.3518247977`; final `7.3518247604`; entity scale `0.8` once | passed |
| topology and weights | 29,971 triangles, 0 degenerate/non-manifold, 0 negative scale, 0 zero weights, 0 vertices over four influences | passed; 1,973 intentional open panel/component edges recorded |
| idle | `autonomous_robot_idle.anim`, 24 FPS, frames 0-97, in-place loop | passed/reimported |
| move | `autonomous_robot_move.anim`, 24 FPS, frames 0-26, in-place loop | passed/reimported |
| attack | `autonomous_robot_attack.anim`, 24 FPS, frames 0-68, both armed forearms recoil | passed/reimported |
| defend | `autonomous_robot_defend.anim`, 24 FPS, frames 0-32 | passed/reimported |
| support attack | `autonomous_robot_support_attack.anim`, 24 FPS, frames 0-97 | passed/reimported |
| retreat | `autonomous_robot_retreat.anim`, bundled real running action, 24 FPS, frames 0-16, in-place loop | passed/reimported |
| training | `autonomous_robot_training.anim`, 24 FPS, frames 0-27 | passed/reimported |
| death | `autonomous_robot_death.anim`, 24 FPS, frames 0-72, grounded root correction | passed/reimported |
| PDX textures | 1024 DDS diffuse plus packed PDX normal/specular | complete |
| sourced sound | six licensed derived OGGs and frame sync in `evidence/audio/`; six 44.1 kHz mono PCM runtime WAVs | installed; entity action references resolve |
| bespoke green counters | `autonomous_robot_counter_art_handoff.md` | installed and registered |
| runtime entity | `autonomous_robot_entity`, scale 0.8 | installed with snow and desert clones |
