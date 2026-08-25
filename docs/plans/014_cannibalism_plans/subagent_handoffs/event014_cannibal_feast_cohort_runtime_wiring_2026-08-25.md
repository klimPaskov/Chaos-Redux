# Event 014 Feast Cohort runtime wiring handoff

Status: **installed and source-verified; no live in-game validation claimed**.

## Changed files

- `gfx/models/units/014_cannibalism/cannibal_feast_cohort/` — final Meshy/Blender `.mesh`, eight `.anim` actions, three DDS maps, and animation registry.
- `gfx/entities/014_cannibalism_units.gfx` — Feast Cohort PDX mesh registration with all eight action identifiers and unique texture names.
- `gfx/entities/014_cannibalism_units.asset` — Feast Cohort entity states, terrain clones, and action-timed movement, attack, training, impact, vocal, and death cues.
- `sound/014_cannibalism_units_sound.asset` — seven Feast Cohort source/effect definitions.
- `sound/014_cannibalism/units/cannibal_feast_cohort/` — seven sourced 44.1 kHz mono PCM WAV roles.
- `docs/assets/014_cannibalism/models_3d/cannibal_feast_cohort/manifest.json` — current package status, adapter, exports, re-import proofs, topology diagnostics, audio, and runtime consumer.
- `docs/assets/014_cannibalism/models_3d/cannibal_feast_cohort/runtime/handoff.md` — current parent consumer handoff.
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_cannibal_feast_cohort_3d_handoff.md` — stale adapter-blocked handoff reconciled to the accepted current package.

## Evidence

- Adapter health and every action correction/re-import report identify `chaosx_blender_hoi4` `1.10.14`.
- Mesh export contains 29,999 triangles, zero non-manifold edges, and zero degenerate faces.
- Eight provider actions were corrected with `per_frame_root_contact_zero_clearance`, excluded hand/head contacts, and body-motion retention. Re-import proof checkpoints are the eight `blender/checkpoints/reimport_cohort_*_11014.blend` files in the package.
- Sound sources and licenses are documented in `evidence/audio_sources/source_provenance.md`; runtime probes remain 44,100 Hz, mono, signed 16-bit PCM.

## Remaining boundary

Position-weld diagnostics report 21,571 loose boundary edges across 578 components; no closure was applied because it risks damaging visible weapon/armour seams. The parent has not claimed live in-game validation and still owns consumer validation, country-level voice mapping, and any later visual-quality review.
