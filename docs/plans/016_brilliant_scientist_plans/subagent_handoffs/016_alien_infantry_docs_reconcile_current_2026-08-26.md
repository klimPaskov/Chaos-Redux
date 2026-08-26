# Event 016 alien-infantry evidence reconciliation handoff

Date: 2026-08-26

## Scope

This handoff records the current evidence reconciliation after the accepted Meshy V13 firearm package was promoted to the engine-facing runtime tree. It supersedes stale cleanup notes that described the package as a blocked V8, V10, V11, KayKit, or Quaternius candidate.

## Accepted runtime package

- Meshy generation task: `01a03dc3-905a-7d02-aba6-05500f877b97`.
- Meshy rig task: `01a03dcf-f0ba-7b67-b769-5a2678b03a40`.
- Meshy firearm action task: `01a03dd1-2d74-70b2-a151-e8d98c82e4de`.
- Meshy death action task: `01a03dd1-3dd9-772c-b0cd-9f7dc4de1fe4`.
- Runtime roles are `Idle`, `walking_2_inplace`, `Draw_and_Shoot_from_Back_1`, `Combat_Stance`, `Walk_Forward_While_Shooting`, `Walk_Backward_with_Gun_inplace`, and `Shot_and_Fall_Backward`.
- Blender HOI4 reinspection confirmed one fused mesh, 59,999 triangles, 24 bones, packed DDS materials, provider-authored firearm attack/recoil, and a real fall-back death action.
- The runtime package is wired under `gfx/entities/alien_infantry.asset`, `gfx/entities/alien_infantry.gfx`, `gfx/entities/animation_alien_infantry.asset`, `sound/alien_infantry_sound.asset`, and the shared sound registry.

## Compaction

- Removed only ignored files inside `docs/assets/016_brilliant_scientist/models_3d/alien_infantry` after verifying the absolute target remained under the repository root.
- Removed 2,100 redundant files totaling 3,399,046,220 bytes (3.166 GiB).
- Retained all tracked manifests, provenance, hashes, validation JSON, exports, and current runtime documentation.
- Retained seven accepted V13 reimport checkpoints: death, defend, idle, laser attack, move, retreat, and support attack.
- Retained the two current visual previews `v13_firearm_laser_attack_f145_three_quarter.png` and `v13_firearm_death_f075_three_quarter.png`.
- No runtime asset, gameplay file, source-of-truth manifest, or accepted actual-byte proof was deleted.

## Remaining explicit blockers

- No supported Meshy or Blender HOI4 adapter operation creates a muzzle locator on the fused provider mesh, so the registered laser particle and light remain intentionally unbound rather than using an inferred hand or entity-origin fallback.
- Strict sound coverage still lacks accepted selection, acknowledgement, impact, and special-action sources; the verified movement, idle, laser-fire, and death bindings remain active.
- Live in-game consumer acceptance remains the user's responsibility and is not claimed by this handoff.

## Parent follow-up

The parent agent owns gameplay wiring, final audit reconciliation, and the reviewed commit. No duplicate Meshy generation, manual weapon parenting, transform-only replacement animation, or unapproved fallback is authorized by this handoff.
