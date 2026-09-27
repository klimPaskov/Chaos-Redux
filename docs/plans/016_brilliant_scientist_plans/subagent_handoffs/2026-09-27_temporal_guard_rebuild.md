# Temporal guard rebuild (2026-09-27)

Disposition: `implemented` — the temporal guard model, eight standard actions, textures, and timed entity are installed; in-game validation belongs to the user.
Acceptance basis: the user approved the unit-model rework on 2026-09-27 and asked that every remaining model be finished thoroughly.
This supersedes the model package described in `2026-09-08_temporal_guard_runtime_integration.md`.

## Why it was replaced

A fixed triage of the shipped package showed the move action walking with both arms locked out in a T-pose.
Three of its ten actions (`entrain`, `temporal_anchor`, `synchronization`) were bound to entity states the engine never enters, and no `training` state existed; the editable repair checkpoints are no longer in the working tree, so the arms could not be re-keyed in place.

## Route

The reference `docs/assets/chaos_redux_3d_model_pilots/models_3d/temporal_guard/refs/original/meshy_input_v3.png` keeps the legacy design (riveted gunmetal plate over brown leather, domed visor helmet with cyan lenses, brass chrono-core with glowing coolant tubes), drawn from a render of the legacy model.
Meshy 7 body, one rig, six presets (Idle 5, Confident Strut, Walk Fight Back, Block 1, Strangled and Fall Forward, Relax Arms Then Strike Battle Pose), and two prime text-to-motion actions (a palm freeze followed by a backhand; lifting an unseen weight and slamming it down) — 79 credits, recorded in the credit ledger.

## Runtime

`gfx/models/units/temporal_guard/` holds the new mesh, eight `.anim` files, and `chaosx_temporal_guard_diffuse/specular/normal.dds`; the retired `entrain`, `temporal_anchor`, and `synchronization` actions and the old maps are removed.
`gfx/entities/temporal_guard.gfx` registers the mesh; `gfx/entities/temporal_guard.asset` defines `chaosx_temporal_guard_entity` with eight distinct states and keeps the `temporal_guard_entity` clone the sprite resolves to.
The existing sourced clock, footstep, contact, impact, death, and temporal cues are retimed to the measured phases of the new actions.

## Remaining limits

- The selection and acknowledgement cues still have no supported consumer in mixed-tag armies.
- Counter art was not changed.
