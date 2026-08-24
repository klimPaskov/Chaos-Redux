# Event 016 Alien Infantry firearm recovery documentation reconciliation

## Outcome

The user authorized Meshy recovery and supplied a new API credential outside the repository. Independent V3 through V7 Meshy lineages were attempted. The V7 neutral geometry, integrated rifle, two-hand hold, remesh, and neutral 24-bone rig passed inspection, but action 690 `Walk_Forward_While_Shooting_inplace`, action 104 `Side_Shot`, and action 232 `Cowboy_Quick_Draw_Shooting` each catastrophically deformed the arms, torso, and rifle. V3 through V7 reproduced the same failure class, so the current blocker is Meshy firearm-animation capability rather than missing authorization or insufficient credits.

No Blender weapon attachment, bone repair, weight repair, constraint, hand-authored action, procedural action, semantic alias, or transform-only substitute was accepted. No discharge timestamp or muzzle node was inferred from a failed clip.

## Installed support

Commit `150c3282d` installs the sourced laser-fire, movement, idle, and death WAV files, their sound definitions, shared category registration, `alien_laser_muzzle_particle`, and `alien_laser_muzzle_flash`. These definitions are reusable support assets, not evidence of a working firearm implementation. They remain unbound until an accepted Meshy action provides a stable muzzle node and verified discharge time.

Commit `fb4fa84d2` records the compact V7 provider-capability evidence and the package-local cleanup. The cleanup removed failed downloads, transient request and response receipts, credit snapshots, and Blender source/checkpoint files after retaining task identifiers, hashes, rejection reports, and representative phase frames. It reclaimed 2,537,107,276 bytes without deleting an accepted runtime candidate.

## Superseded statements

Earlier dated handoffs that say recovery is waiting for user approval, that the only rejected candidate omitted its rifle, or that another approximately 30-credit authorization is required are historical evidence and no longer describe the current blocker. They are superseded by:

- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/manifest.md`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/runtime/handoff.md`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/runtime/crosswalk.md`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/runtime/sound_handoff.md`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/provider/rejections/generation_recovery_v7_firearm_capability.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/alien_infantry_3d_model_handoff.md`
- `docs/specs/016_brilliant_scientist_specs/matrices/016_asset_inventory.md`

## Remaining acceptance boundary

The package still lacks an accepted seven-action Meshy set, a genuine death action, packed PDX materials, `.mesh` and `.anim` exports, actual-byte reimport proof, `alien_infantry_entity`, exact sound/particle/light synchronization, and model-backed runtime evidence. Under the current Meshy-only instruction, recovery requires a newly viable Meshy lineage or a provider capability change.

The requested reusable firearm instructions must not be added to `chaos-redux-3d-model-pipeline` yet. The condition was that shooting, particles, and sound work well together; that condition has not been met, so documenting this failed route as a successful workflow would mislead future agents.
