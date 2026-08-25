# Cannibal Feast Cohort runtime handoff

Status: **package complete; parent runtime wiring installed**.

## Parent-owned consumer

- Gameplay consumer: `common/units/014_cannibalism_irregular_infantry.txt#cannibal_feast_cohort`.
- Entity: `cannibal_feast_cohort_entity`.
- Runtime model root: `gfx/models/units/014_cannibalism/cannibal_feast_cohort/`.
- Wiring is present in `gfx/entities/014_cannibalism_units.gfx`, `gfx/entities/014_cannibalism_units.asset`, `sound/014_cannibalism_units_sound.asset`, and the runtime model root.
- Parent still owns gameplay, localisation, country-level voice integration, and live in-game validation.

## Geometry and calibration

- The approved recovery-v6 source, Meshy 7 geometry, provider rig, and eight provider action artifacts are retained in this package.
- The saved runtime checkpoint is `blender/checkpoints/recovery_v6_11_runtime_sanitized_11014.blend` and was processed through adapter `chaosx_blender_hoi4` `1.10.14`.
- The exported mesh is `exports/cannibal_feast_cohort_11014.mesh`, with 29,999 triangles, zero non-manifold edges, zero degenerate faces, and normalized source height `7.351824760`.
- Runtime calibration follows `western_european_infantry.mesh#polySurface106`, forward `-Y`, up `+Z`, entity scale `0.8`, and effective runtime height `5.881459838`.
- Position-weld diagnostics report 21,571 loose boundary edges across 578 components. Closure was not applied because it can damage visible weapon and armour seams; no live consumer claim is made from this diagnostic alone.

## Rig and actions

All eight actions are provider-sourced, preserved at 24 fps, corrected with the root-only per-frame contact policy, exported, and re-imported against the current mesh. Body motion was retained in every correction pass.

- `idle` — 42 frames; `blender/checkpoints/reimport_cohort_idle_11014.blend`.
- `move` — 29 frames; `blender/checkpoints/reimport_cohort_move_11014.blend`.
- `attack` — 70 frames; `blender/checkpoints/reimport_cohort_attack_11014.blend`.
- `defend` — 149 frames; `blender/checkpoints/reimport_cohort_defend_11014.blend`.
- `support_attack` — 74 frames; `blender/checkpoints/reimport_cohort_support_attack_11014.blend`.
- `retreat` — 44 frames; `blender/checkpoints/reimport_cohort_retreat_11014.blend`.
- `training` — 90 frames; `blender/checkpoints/reimport_cohort_training_11014.blend`.
- `death` — 55 frames; `blender/checkpoints/reimport_cohort_death_11014.blend`.

The final runtime files are `cannibal_feast_cohort.mesh`, eight role-named `.anim` files, and the `animation_cannibal_feast_cohort.asset` registry under the runtime root.

## Materials and sound

The runtime ships bespoke diffuse, specular, and normal DDS maps under the Feast Cohort model root. The seven sourced roles are installed as 44.1 kHz mono PCM WAV files: selection, movement, idle vocal, training swish, weapon attack, weapon impact, and death. Source pages, licenses, transformations, and hashes remain in `evidence/audio_sources/source_provenance.md` and the package receipts.

Entity event timings are bounded by the final 24 fps action lengths. The training cue uses the documented CC0 swish source and is not a transform-only cosmetic substitute.

## Counter and acceptance boundary

The bespoke counter package remains parent-wired under the existing Event 014 counter registration and is not modified by this handoff. No live in-game validation is claimed here; the parent must perform consumer validation after the normal game reload.
