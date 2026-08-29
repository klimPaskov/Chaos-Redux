# Event 020 additional free rat source handoff

Date: 2026-08-24.

Status: incomplete and blocked at the dependency-locked Blender route.

## Outcome

Meshy cannot supply this nonhumanoid rat's eight required animations under the zero-spend constraint. The official route has only character/humanoid rigging and a three-credit `meshy_animate(rig_task_id, action_id)` call, while this job has no completed provider rig or animation output to reuse. The live balance was read as 1,250 credits; estimated and consumed credits remain zero.

The two Sketchfab candidates did not pass anonymous acquisition. Official Sketchfab documentation requires account-authenticated OAuth before download and exposes only converted glTF/GLB/USDZ, not original FBX/Blend. Shintokin supplies only a run action. CharlieCatling is marked NoAI and its Fab source acquisition requires an account transaction. No credentials, transactions, or source bytes were used.

The official Quaternius Easy Enemy Pack did pass the source gate. Its CC0 public Drive anonymously supplied an exact `Rat.blend` without account action or cost:

- source page: `https://quaternius.com/packs/easyenemy.html`;
- public folder: `https://drive.google.com/drive/folders/1VbJIslXPWK-1KybQN6yezZrfJcw608qe?usp=sharing`;
- file: `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/evidence/free_animation_sources/originals/quaternius_easy_enemy_rat.blend`;
- bytes: 1,212,184;
- SHA-256: `8B79283A01763CBFF54F4774A3B80DE8AA121B8484FD04C77EE369439DC7A446`;
- file signature: Blender 2.79;
- runtime status: immutable non-shipping evidence only.

## Blocking evidence

`python -B .tools/3d_pipeline/verify_environment.py` passed against the repository's adapter 1.10.0 lock. However, live Blender MCP health requests `61841dce57224393b0f43071b018597f` and `69ab5c085718407880f27162697e6dc2` both returned adapter 1.9.2. The live schema also omits exact source armature and direct-mesh selection fields. The dependency-lock gate forbids substituting or mutating through that stale route, so the new rat source was not opened, inspected, weighted, rendered, exported, or reimported.

The br-n518 four-nearest route remains rejected. The allowlisted adapter contains no nearest-triangle/barycentric or proxy-cage transfer operation. The exact remaining built-in alternatives are `chaosx_blender_hoi4_prepare_candidate` with `geometry_weight_mode=automatic_bone_heat` and `geometry_weight_mode=bone_distance`. Neither may be tested until the live MCP route reports locked adapter 1.10.0.

## Safe continuation order

1. Restart or refresh the Blender HOI4 MCP server and prove health reports adapter 1.10.0 with the fresh schema.
2. Inspect the Quaternius Easy Enemy `Rat.blend`, selecting its exact armature and direct mesh consumers; record all actions, frame ranges, FPS, curve hashes, and NLA suppression evidence.
3. If it has a substantive native Walk, run the topology-preserving Walk-only common-rig bind using the original audited Meshy rat geometry, exact prior scale/material inputs, and `automatic_bone_heat`; use `bone_distance` only if the first built-in route structurally fails.
4. Require 32,909 vertices, 29,999 triangles, no zero weights, no more than four influences, visible start/mid/end phase differences, intact anatomy, grounded paws, and no sheet stretching or pinching before evaluating other roles.
5. If the new exact rat lacks eight distinct roles, retain only visually and semantically validated roles and search or retarget other approved free sources solely for genuinely missing roles after the common-rig Walk gate passes. Never alias or relabel duplicates.

## Files changed

- `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/evidence/free_animation_sources/originals/quaternius_easy_enemy_rat.blend`
- `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/evidence/free_animation_sources/quaternius_easy_enemy_source_receipt.md`
- `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/evidence/free_animation_sources/2026-08-24_additional_source_search.md`
- `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/history.md`
- `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/manifest.md`
- `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/rat_ground_unit_shared_model_job.yaml`
- this handoff.

No runtime model, animation, GFX, entity, sound, localisation, gameplay, or spreadsheet file was changed. No commit was created. The required eight-role package and Walk gate remain incomplete.
