# Event 020 runtime-checkpoint Rat_Walk retarget blocker

## Status

`blocked_required_installation_verification`

The requested protected-copy retarget did not begin. The repository dependency-lock gate failed before checkpoint inspection or mutation, and the live Blender HOI4 MCP declaration does not expose the lock-declared `import_animation_action` operation needed for receipt-verified source-motion transfer.

## Bounded scope and zero-spend confirmation

- Job: `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared`.
- Runtime mesh named by the parent: `gfx/models/units/020_black_plague_rat/black_plague_rat.mesh`; it was not read, copied, or changed by this pass.
- Intended source: `evidence/free_animation_sources/originals/quaternius_easy_enemy_rat.blend`, CC0-1.0, 1,212,184 bytes, SHA-256 `8B79283A01763CBFF54F4774A3B80DE8AA121B8484FD04C77EE369439DC7A446`.
- Intended source action: `Rat_Walk`, previously reported as 33 frames (`0-32`) at 24 FPS in `blender/reports/rat_quaternius_easy_enemy_bonedistance_walk_prepare.json`; this pass did not independently inspect or hash its curve payload.
- Meshy/provider calls: none.
- Marketplace authentication, purchase, trial, or download: none.
- Credits estimated: `0`; credits consumed: `0`.
- Runtime, gameplay, GFX, entity, sound, localisation, spreadsheet, adapter, configuration, and dependency-lock files changed: none.

## Hard-gate evidence

The mandatory process environment gate passed: `MESHY_API_KEY` was present and non-blank; its value was not read, printed, or used.

Locked dependencies and route facts:

- `.tools/3d_pipeline/config/dependencies.lock.json`: SHA-256 `8687900336850F46665F39359A1F87159373E8CEEF479B1E9F1404C3E7165218`.
- `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`: SHA-256 `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`.
- `.tools/3d_pipeline/config/blender_hoi4_adapter.json`: SHA-256 `32A3DE4739A4AE7DC556850EC67742F9F3EA437B9DCBB9F4219E1B908566228E`.
- Locked adapter: `chaosx_blender_hoi4` version `1.10.2`.
- Locked Blender: `5.1.2`, build `ec6e62d40fa9`.
- Locked `io_pdx_mesh`: release `0.91`, version `0.91.0`, archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Blender bridge `127.0.0.1:9876`: listening during preflight.
- Live health request id: `272d7648aeb14615b1823e4d76c6a761`.
- Live health receipt: `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/logs/adapter/272d7648aeb14615b1823e4d76c6a761.result.json`.
- Live health result: adapter `1.10.2`, Blender `5.1.2`, `io_pdx_mesh_loaded: true`, mesh and animation export functions available.

The adapter source lock is not satisfied:

| Locked file | Expected SHA-256 | Actual SHA-256 | Result |
|---|---|---|---|
| `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py` | `E36E5887795C4110816B3E903EDD235DFCA14C2FE8F2FB94412B0C5F272FA2AB` | `E36E5887795C4110816B3E903EDD235DFCA14C2FE8F2FB94412B0C5F272FA2AB` | pass |
| `.tools/3d_pipeline/adapter/blender_worker.py` | `1116CFF24E0495DC759C568E4BCD4CCB1F7F336E761BE74A66D37E0BDA66B2E7` | `DB0B0926DED11065BEF3FE839C180A01C93E2664D68D114A2FE9EEEBC204DD21` | **fail** |
| `.tools/3d_pipeline/blender_client.py` | `DC132111929BC14636194817BCDF9DFE8104EE2A484C6033E3DA6414D75FF65A` | `DC132111929BC14636194817BCDF9DFE8104EE2A484C6033E3DA6414D75FF65A` | pass |
| `.tools/3d_pipeline/config/blender_hoi4_adapter.json` | `32A3DE4739A4AE7DC556850EC67742F9F3EA437B9DCBB9F4219E1B908566228E` | `32A3DE4739A4AE7DC556850EC67742F9F3EA437B9DCBB9F4219E1B908566228E` | pass |

The dependency lock and adapter config list `import_animation_action`, but the live MCP declaration available to this agent exposes only `health`, `prepare_candidate`, `inspect_scene`, `process_textures`, `export_mesh`, `export_animation`, `reimport_export`, `save_checkpoint`, and the prohibited authoring operations among the relevant model tools. It does not expose `import_animation_action`, `retime_animation_action`, or a dedicated semantic-chain retarget operation. Therefore there is no callable receipt-verified route accepting the required explicit bone-chain mapping.

## Runtime checkpoint finding

Checkpoint: `blender/checkpoints/reimport_runtime_snapshot_reimport.blend`, 1,706,054 bytes, SHA-256 `9DADB444DFEA7998165A3EEBE763F1C5CF45DE7D57B701A9EB5D833B5C56191B`.

Fresh MCP inspection was not performed after the checksum/schema gate failed, so this pass cannot independently certify that the checkpoint has a usable, export-compatible target armature. Existing repository evidence in `runtime/crosswalk.md`, `blender/rig_map.md`, and `manifest.md` reports an `io_pdx_rig` target with 17 bones, 32,909 exported seam vertices, exactly one normalized influence per vertex, no zero-weight deforming vertices, and existing export/reimport proof request `2a0047972045416f87685cff49ed50c0`. That is strong prior evidence that a target rig exists, but it is not a fresh receipt for the requested protected-copy retarget and does not prove that the current mismatched route can target it safely.

The prior semantic target inventory is `root`, `body`, `neck`, `head`, `trunk_01`, `trunk_02`, `tail`, four upper/lower limb pairs, `howdah`, and `rider`. The prior Fox-to-target map requires multi-bone chain collapse, rest-matrix solving, and deliberate omission of control/detail bones. The older `evidence/free_animation_sources/quadruped_retarget_tooling_gap.md` records that historical `import_animation_action` required identical target bone names and could not perform that chain collapse. The current live schema provides no callable replacement proving otherwise.

## Work not performed

- No protected working copy was created because even a safe copy would have no verified retarget operation.
- No explicit source-to-target bone-chain mapping was submitted.
- No `Rat_Walk` target action, pose hashes, curve hash, or action checksum was created.
- No start/mid/end front, left, or three-quarter previews were rendered.
- No new weight, root drift, in-place, paw-contact, tail, anatomy, loop-closure, or deformation audit was run.
- No action was exported or reimported.
- No file was copied to the runtime surface.

## Ultimate fox follow-up assessment

The existing CC0 Ultimate fox package has eight provenance-stamped distinct source actions and an explicit semantic map in `evidence/free_animation_sources/quaternius_fox_to_rat_rig_map.md`. If the repository owner restores a checksum-matching adapter and exposes a receipt-verified operation that supports evaluated rest-space multi-bone chain collapse onto the accepted `io_pdx_rig`, the remaining fox actions could be attempted independently on that same target rig without changing the target skeleton or weights. This is a compatibility hypothesis only. None of the fox actions passes retarget, deformation, grounding, semantic, export, or reimport gates from this handoff.

## Required resolution

1. Reconcile `.tools/3d_pipeline/adapter/blender_worker.py` with the checksum in `dependencies.lock.json` without using this model worker to edit shared tooling.
2. Make the locked live MCP declaration expose the exact receipt-verified `import_animation_action` operation or a separately lock-recorded semantic-chain retarget operation with job-root containment, source provenance/checksum inputs, explicit source and target armatures/actions, ordered chain mapping, FPS resampling, in-place/root policy, location-scale policy, output checkpoint, pose hashes, and request receipt.
3. Rerun health and checksum/schema verification, then inspect `reimport_runtime_snapshot_reimport.blend` through MCP before any mutation.
4. Only if the target armature is freshly certified, create a protected job-root copy and run the Walk-only gate before processing any other role.

## Files changed by this subagent

- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-24_event020_runtime_checkpoint_retarget_blocker.md`

No fallback or simplification was used. The requested animation recovery remains incomplete and blocked at dependency/route verification.
