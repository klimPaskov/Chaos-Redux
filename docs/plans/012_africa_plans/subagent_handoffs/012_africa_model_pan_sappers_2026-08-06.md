# Event 012 Pan Sappers 3D production handoff

Superseded by `012_africa_models_runtime_completion_2026-08-06.md`; the complete package is at `docs/assets/012_africa/models_3d/pan_sappers/`.

## Outcome

The corrected humanoid Pan Sappers package is `blocked` at the mandatory dependency-lock and intake gates. No provider or paid work was attempted, no fallback or simplification was used, and the stale nonhuman/24-FPS assumptions from the earlier attempt were removed.

## Files changed

- `docs/assets/012_africa/models_3d/pan_sappers/job.yaml`
- `docs/assets/012_africa/models_3d/pan_sappers/history.jsonl`
- `docs/assets/012_africa/models_3d/pan_sappers/manifest.md`
- `docs/assets/012_africa/models_3d/pan_sappers/evidence/dependency_route_blocker.md`
- `docs/assets/012_africa/models_3d/pan_sappers/runtime/handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_model_pan_sappers_2026-08-06.md`

## Exact blocker

Blender `5.1.2`, adapter `1.2.2`, the bridge at `127.0.0.1:9876`, and installed `io_pdx_mesh` `0.91.0` pass health verification. Health request `1e7d02ac31be46418ec3ea35d0f2c50f` wrote evidence inside the correct Event 012 job root.

The live adapter declaration nevertheless omits the lock-listed `import_animation_action`, `retime_animation_action`, `correct_action_grounding`, `offset_action_root`, and `sanitize_runtime_candidate` operations. Those calls are necessary for real 30-FPS skeletal `idle`, `move`, `sabotage`, and `construction` actions with audited root motion, contacts, sanitization, export, and reimport. The exposed locomotion authoring call cannot replace the three non-locomotion actions. The role forbids unrestricted Blender or another route.

The context-complete intake is also missing exact vanilla infantry model/entity/material/animation/texture paths, exact installed-vanilla large/map counter definition and DDS paths, matching skill-local counter-family paths, and numeric extra-recovery limits. The role expressly forbids guessing these inputs.

## Corrected accepted contract

- Profile: `humanoid_unit`
- Exact runtime consumer: `chaosx_pan_sappers`
- Exact subunit token: `pan_sappers`
- Scale: `1.0x` the installed vanilla infantry source height, with entity scale applied exactly once
- Geometry: one exact single-image Meshy input; complete unseen rear details
- Actions: `idle`, `move`, `sabotage`, `construction`, real skeletal actions at 30 FPS with documented loop and root-channel policies
- Country identity: existing tag/carrier mapping only; no new country tag
- Audio: only clearly licensed or public-domain sourced recordings with infantry/engineering precedents, checksums, transformations, and synchronization table
- Counters: bespoke vanilla-green large/map DDS art after exact installed reference and skill-family inspection; no fallback

## Source and provider lineage

- Reference image: not generated; dependency and intake verification must pass first.
- Meshy balance: not queried.
- Provider tasks/response IDs: none.
- Downloads/checksums: none.
- Credits estimated: not evaluated.
- Credits consumed: `0`.

## Geometry, material, rig, action, export, audio, and counter results

All production requirements remain blocked before creation. There are no GLB, FBX, `.blend`, `.mesh`, `.anim`, texture PNG/DDS, preview, reimport, audio, or counter artifacts. No sound URL/license or animation synchronization point was invented. No counter token/path was guessed from the stale earlier intake.

## Meaningful validation

- Confirmed the process Meshy key is nonblank without recording it.
- Read and applied the 3D model, event-assets, and subagent contracts plus the offline entity/graphical/unit references.
- Compared the three lock/config files with the live Meshy and Blender adapter declarations.
- Probed `127.0.0.1:9876` independently; it is listening.
- Called the locked adapter health route for `pan_sappers`; Blender, adapter, and `io_pdx_mesh` passed.
- Recorded exact dependency/config/manifest/executable hashes and the adapter request ID in the blocker evidence.

## Skipped meaningful validation

Reference preflight, Meshy balance/generation, geometry review, vanilla source-height measurement, texture conversion, rig/weight tests, action previews, export/reimport, Internet audio research/download, and counter inspection/art were skipped because the hard gates failed before those stages.

## Required parent action

Redeploy the locked adapter with its complete declared animation operation surface and provide the missing exact vanilla/counter paths and numeric recovery limits. Then resume this same deterministic job before any provider spend.

Gameplay/GFX/entity/sound-definition/localisation/spreadsheet wiring and in-game validation remain parent-owned. No in-game completion is claimed.

Simplifications, omissions, and fallbacks: no simplification or fallback was used; every unproduced requirement is explicitly blocked above.
