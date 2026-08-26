# Event 016 3D reference pose-preparation skill handoff

## Scope

This handoff records the reusable workflow update in `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` requested for source-artwork preparation before Meshy generation.

## Implemented rule

The selected Internet source remains immutable evidence and is never edited, recompressed, or sent directly to ImageGen or Meshy.

Native ImageGen operates on a separate derivative to isolate the complete subject, provide a clean plain background or genuine transparency, repair only faithful presentation defects, and preserve the original identity, design, equipment, anatomy, proportions, palette, and materials.

When feasible, the derivative attempts a neutral T-pose or A-pose by changing limb placement only; it must not redesign the subject, invent equipment, or repair a bad weapon relationship.

Each job records `pose_preparation_mode = t_pose`, `pose_preparation_mode = a_pose`, or `pose_preparation_mode = none` with the reason, along with the exact ImageGen prompt, source and prepared checksums, source-to-prepared comparison, and parent approval.

Only the approved derivative is copied to `refs/original/meshy_input.png`, and the Meshy submission remains exactly one full-body image rather than a turnaround or multi-view board.

## Firearm safety gate

Firearm-bearing sources must already show the complete weapon with trigger-hand, support-hand, stock or shoulder, and muzzle continuity before pose preparation.

T-pose or A-pose normalization is allowed only when those contacts remain intact, and it can never make an invalid firearm pose acceptable.

Meshy remains responsible for rigging and substantive attack, discharge, recoil, recovery, and death actions; Blender may not manually attach or animate a firearm.

## Validation and ownership

The skill was inspected with `rg` for stale no-repose wording and the changed file passed `git diff --check`.

No gameplay, asset, model, runtime, localisation, or event files were changed by this handoff.

The parent agent owns final review and commit of the skill and this handoff; no provider operation was run for this documentation-only change.
