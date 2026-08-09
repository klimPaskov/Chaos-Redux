# Event 012 Stone Cohorts 3D Model Handoff

Superseded by `012_africa_models_runtime_completion_2026-08-06.md`; the complete package is at `docs/assets/012_africa/models_3d/stone_cohorts/`.

## Outcome

The package is `blocked`, not complete. Meshy 6 generated and downloaded the provider candidate successfully. The repository-owned Blender HOI4 adapter now resolves the correct Event 012 job root and passes health, but its live MCP declaration exposes only 9 of the 18 operations in the dependency lock. Work stopped before Blender mutation or any further paid tranche because required creature/hybrid rig, action, grounding/root-motion, retime/import, calibration, segmentation, and sanitization operations are not callable.

## Files created or changed

- `docs/assets/012_africa/models_3d/stone_cohorts/job.yaml`
- `docs/assets/012_africa/models_3d/stone_cohorts/history.jsonl`
- `docs/assets/012_africa/models_3d/stone_cohorts/manifest.md`
- `docs/assets/012_africa/models_3d/stone_cohorts/refs/original/meshy_input.png`
- `docs/assets/012_africa/models_3d/stone_cohorts/refs/original/input_manifest.json`
- `docs/assets/012_africa/models_3d/stone_cohorts/refs/briefs/meshy_input_prompt.md`
- `docs/assets/012_africa/models_3d/stone_cohorts/provider/requests/image_to_3d_request.json`
- `docs/assets/012_africa/models_3d/stone_cohorts/provider/responses/image_to_3d_response.json`
- `docs/assets/012_africa/models_3d/stone_cohorts/provider/credits/generation_credits.json`
- `docs/assets/012_africa/models_3d/stone_cohorts/provider/downloads/stone_cohorts_meshy6_source.glb`
- `docs/assets/012_africa/models_3d/stone_cohorts/provider/downloads/stone_cohorts_meshy6_source.fbx`
- `docs/assets/012_africa/models_3d/stone_cohorts/provider/downloads/stone_cohorts_meshy6_source_textures/*`
- `docs/assets/012_africa/models_3d/stone_cohorts/evidence/dependency_lock_evidence.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_model_stone_cohorts_2026-08-06.md`

## Provider lineage and credits

- Tool: `meshy_image_to_3d` through official `@meshy-ai/meshy-mcp-server` `0.4.0`.
- Live model: `meshy-6`; triangle topology; PBR; T-pose; one local `file_path`; multiview disabled.
- Task id: `019fd7ae-83a0-792c-8a2e-c1199c678f6d`.
- Result: succeeded.
- Estimate: `20` credits; actual: `30` credits.
- Balance: `554` before, `524` after.
- No remesh, rig, convert, animation, or retry credits were spent.
- Extra recovery allowance remains `0` credits and `0` attempts.

## Source and provider hashes

| Artifact | SHA-256 |
| --- | --- |
| `refs/original/meshy_input.png` | `9A03A8057E8A11BAFA3642B707636825F3C3EE104B68F0B4275837CB3AC0B4B0` |
| `provider/downloads/stone_cohorts_meshy6_source.glb` | `E84736BEC9FFB0C71913BBFC2EB6969635030EDAA2B9D2954DFAAFB2814CE667` |
| `provider/downloads/stone_cohorts_meshy6_source.fbx` | `4180B6DEF99E08AD3372B68A26BB63D4505B36D6B64D0DC5DA41955B7CF6A037` |
| `base_color.png` | `D5335573A9E1BF6ADD67319F5818BAF6E02208FAD53072C306076DA55EDA3E28` |
| `metallic.png` | `46FEE7B3C5658928124DF25B8B83B83DE538B47774513FCDBA88DD0645DE9FB9` |
| `roughness.png` | `40EDD085D2A4C162452464106958FF02A08A809D5B6A6E0FCFE87523D8BFA2EA` |
| `normal.png` | `72036D9A45A7DFBB2E844F39B08A3FDEEE4E809FA80600E4B4741A54D62D4DAA` |
| `emission.png` | `81886BE583CC4A4FD76DD0E9552D417590F20B08F5BCC750B626722A7893EFB4` |

## Dependency evidence

- Meshy MCP `0.4.0`, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`.
- Blender `5.1.2`, build `ec6e62d40fa9`.
- Adapter `chaosx_blender_hoi4` `1.2.2`.
- `io_pdx_mesh` `0.91.0`, archive checksum verified.
- Dependency lock and schema hashes are in `evidence/dependency_lock_evidence.md`.
- `127.0.0.1:9876` listened successfully.
- `chaosx_blender_hoi4_health(job_id = stone_cohorts)` passed on retry, request id `9c67305d2fa943b88e27c25a7e8becf4`.
- Live callable adapter operations: `health`, `prepare_candidate`, `inspect_scene`, `process_textures`, `export_mesh`, `export_animation`, `author_locomotion_action`, `reimport_export`, and `save_checkpoint`.
- Missing locked operations: `import_animation_action`, `retime_animation_action`, `segment_creature_components`, `calibrate_creature_scale`, `author_creature_rig`, `author_creature_action`, `correct_action_grounding`, `offset_action_root`, and `sanitize_runtime_candidate`.

## Reference correction

The parent explicitly approved `gfx/models/units/020_black_plague_rat/black_plague_rat.mesh` after the originally named `rat_ground_unit_shared.mesh` was found not to exist. This is an approved path correction, not a fallback.

## Geometry, scale, materials, rig, actions, and export

These stages remain blocked. The provider output has not passed the generation gate because the live adapter capability set does not match the locked route. No measurements, repairs, texture conversions, armature, weights, action previews, `.mesh`, `.anim`, or reimport proof exist.

Requested action rows remain blocked:

- `chaosx_stone_idle`, 30 FPS, frames 0-47, looping, root motion required.
- `chaosx_stone_move`, 30 FPS, frames 0-47, looping, root motion required.
- `chaosx_stone_attack`, 30 FPS, frames 0-35, non-looping, root motion required.
- `chaosx_stone_collapse_recovery`, 30 FPS, frames 0-47, non-looping, root motion required.

## Sound package

No Internet candidate was downloaded because dependency-gate policy required stopping at the adapter mismatch. Required roles remain selection, stone movement/impact, attack, collapse/recovery, and death, with the brief's move frames 0/24, attack frame 18, collapse lowest frame, and death final-frame synchronization points. No generated, placeholder, manually authored, or unlicensed audio was used.

## Counter package

The installed `interface/subuniticons.gfx` definition and infantry DDS paths exist, and the large reference uses two frames. Production did not proceed to the icon artist after the dependency mismatch. Required tokens remain `unit_stone_cohorts_icon`, `unit_stone_cohorts_icon_small`, and `onmap_unit_stone_cohorts_icon`; final targets remain the parent-provided large and small DDS paths. No copied vanilla or arbitrary-green counter was created.

## Required installation or verification

Reload or restart the locked Blender HOI4 adapter MCP service from the current adapter `1.2.2` source so its live tool declaration exposes all operations listed in `.tools/3d_pipeline/config/dependencies.lock.json`. Verify the nine missing operations above are callable, then rerun `chaosx_blender_hoi4_health` before any new paid tranche or Blender stage.

## Parent-owned remaining work

After the adapter is healthy, resume geometry review, scale calibration, custom rig/actions, PDX textures, exports/reimport, sourced audio, counter-artist handoff, and final evidence. The parent still owns gameplay, GFX, entity, sound-definition, localisation, spreadsheet, runtime-copy, live-consumer, and in-game validation. No gameplay-readiness setter was created.

## Simplifications and fallbacks

None.
