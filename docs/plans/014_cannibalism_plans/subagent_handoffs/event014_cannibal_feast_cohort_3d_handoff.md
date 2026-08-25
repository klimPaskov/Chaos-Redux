# Event 014 Cannibal Feast Cohort 3D handoff

Status: **accepted; runtime package installed by the parent on 2026-08-25**.

The exact-one source, Meshy 7 generation, provider remesh, provider rig, all eight distinct provider actions, seven-role sourced audio set, and bespoke counters remain archived under `docs/assets/014_cannibalism/models_3d/cannibal_feast_cohort/`. The prior adapter 1.10.3 reopen failure is rejection evidence only.

The current adapter `chaosx_blender_hoi4` 1.10.14 processed `blender/checkpoints/recovery_v6_11_runtime_sanitized_11014.blend`. Root-only per-frame contact correction was applied to all eight actions with excluded hand/head contacts; each result passed, retained body motion, and re-imported against `exports/cannibal_feast_cohort_11014.mesh`.

Runtime files are installed under `gfx/models/units/014_cannibalism/cannibal_feast_cohort/`: the 29,999-triangle `.mesh`, eight role-named `.anim` files, the animation registry, and three unique DDS maps. Parent entity/GFX definitions and seven sourced 44.1 kHz mono PCM audio roles are wired in `gfx/entities/014_cannibalism_units.gfx`, `gfx/entities/014_cannibalism_units.asset`, and `sound/014_cannibalism_units_sound.asset`. The Feast Cohort sub-unit already consumes `cannibal_feast_cohort_entity` through its Event 014 activation and recruitment paths.

The runtime handoff is `docs/assets/014_cannibalism/models_3d/cannibal_feast_cohort/runtime/handoff.md`; the package manifest records the current adapter, exports, re-import proofs, topology diagnostics, and the explicit no-live-validation boundary. No live in-game consumer validation is claimed.
