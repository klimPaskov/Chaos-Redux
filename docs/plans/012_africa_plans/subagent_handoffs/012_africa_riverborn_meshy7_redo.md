# Event 012 Riverborn Meshy 7 recovery handoff

Status: `blocked_generation_recovery_2_rejected_identity_and_topology`.

## Bounded work performed

The mandatory `MESHY_API_KEY` gate passed without exposing the secret. The repository-owned environment verification passed with no findings: official `@meshy-ai/meshy-mcp-server` `0.4.0`, locked SDK `1.29.0`, compatibility revision `meshy-7-v5`, exact image model `meshy-7`, Blender `5.1.2` build `ec6e62d40fa9`, `chaosx_blender_hoi4` adapter `1.10.14`, and checksum-locked `io_pdx_mesh` `0.91.0` archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`. Blender health request `bb402e93a8074d3daec9d40713eee904` passed and the bridge was listening at `127.0.0.1:9876`.

Dependency-lock SHA-256 was `C27768297FB7AD5ACC9C555E7C83DC77856908E2C628BF16D9A420095C64266A`; Meshy schema-lock SHA-256 was `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`; adapter-config SHA-256 was `4BC97CA0B07580F5AA04B49E7B9FBD1C07EC88DF5C4D56CD3BA8846E630117AB`.

The exact parent-approved input remained `refs/original/meshy_input.png`, SHA-256 `FB44F05C9F19740802AB446B851678766B64C6D9DB8BCB9902CEC65C2ADF4521`. The selected source remains Grinding Gear Games' *Kiloava Chieftain Concept Art* in `reference_only_user_authorized` mode, with source, rights, fingerprint, refinement prompt, comparison, alpha fallback, and non-shipping status preserved in the existing provenance package.

One user-authorized recovery generation was submitted with A-pose, image enhancement disabled, multiview disabled, triangle topology, 25,000 target, integrated remesh, textured PBR, GLB/FBX outputs, and exact `meshy-7`. The live schema exposes no geometry prompt; the recorded texture prompt was not treated as geometry control.

## Provider lineage and credits

- Task: `01a03d69-fcfd-7d8d-8d8c-c267c5c2990d`.
- Status: provider `SUCCEEDED`; package `rejected`.
- Estimated and consumed: 30 credits.
- Live balance: 153 immediately before; 123 immediately after; exact delta 30.
- GLB: `provider/downloads/generation_recovery_2/riverborn_generation_recovery_2.glb`, SHA-256 `463B827749866B524DCC89C7E077864CE4963B44878BB9595A1FA343F9B2C72C`.
- FBX: `provider/downloads/generation_recovery_2/riverborn_generation_recovery_2.fbx`, SHA-256 `67E01241C8B14430253C6BB30165617D2D35B23C5AB3CD0599CAEAC4CF6392A6`.
- Full texture checksums: `provider/downloads/generation_recovery_2/download_manifest.json`.
- Signed provider URLs were not recorded.

## Blender and QA results

Adapter request `d1c64a45ca5f48a68fbe0da1e7dc4d18` imported the GLB, protected provider source, read-only imported the named vanilla infantry reference, normalized the model to `9.396003723` m at entity scale `1.0`, placed ground contact at `0.0`, and retained 24,498 triangles. The full prepare report is `blender/reports/chaosx_riverborn_recovery_2_prepare.json`, SHA-256 `960C71838520F85F6FAF8B184FABE2B0CB257EECF107D40B68037390C6417CBA`.

Identity failed in all seven adapter views: the required carved shield is absent and the required spear is absent. There is therefore no valid one-hand or two-hand weapon retention relationship. Topology also failed after bounded repair with 1,920 loose boundary edges across 354 components, including 84 branched components. The rejection is documented in `blender/reports/generation_recovery_2_rejection.md`.

Generation 1 Blender evidence was copied to `blender/rejected/generation_1_snapshot/` before the recovery adapter pass so the prior rejected lineage remains reviewable.

## Work deliberately not performed

No separate remesh, provider rig, provider animation, retexture, conversion, PDX texture conversion, `.mesh` export, `.anim` export, or reimport was performed. Remeshing cannot restore absent required equipment, and the skills forbid spending rig or animation credits on rejected geometry. No blind generation retry was made.

All five semantic actions remain blocked: `chaosx_riverborn_idle`, `chaosx_riverborn_move`, `chaosx_riverborn_attack`, `chaosx_riverborn_water_transition`, and `chaosx_riverborn_death`. Existing locally authored actions and old `.anim` files are historical evidence only and are forbidden as replacement motion.

## Parent-owned follow-up

Do not synchronize or wire `export/mesh/chaosx_riverborn.mesh` or any existing `export/anim/*.anim`; they are legacy outputs. Keep model/entity readiness false. Existing sourced audio and bespoke counter packages may remain preserved, but their final action synchronization and runtime GFX/entity/sound wiring are blocked behind an accepted Meshy 7 model and verified provider action package.

A future recovery needs a newly parent-approved exact-one-image reference whose visible composition makes the complete shield and spear unmistakably inseparable from the humanoid silhouette while remaining riggable. Reusing the unchanged input for another blind paid attempt is not recommended. No in-game completion is claimed.

## Files changed or created

- `docs/assets/012_africa/models_3d/riverborn/job.yaml`
- `docs/assets/012_africa/models_3d/riverborn/history.jsonl`
- `docs/assets/012_africa/models_3d/riverborn/manifest.md`
- `docs/assets/012_africa/models_3d/riverborn/runtime/handoff.md`
- `docs/assets/012_africa/models_3d/riverborn/provider/requests/generation_recovery_2.json`
- `docs/assets/012_africa/models_3d/riverborn/provider/responses/generation_recovery_2_submission.json`
- `docs/assets/012_africa/models_3d/riverborn/provider/tasks/generation_recovery_2.json`
- `docs/assets/012_africa/models_3d/riverborn/provider/credits/generation_recovery_2_preflight.json`
- `docs/assets/012_africa/models_3d/riverborn/provider/credits/generation_recovery_2_postflight.json`
- `docs/assets/012_africa/models_3d/riverborn/provider/downloads/generation_recovery_2/`
- `docs/assets/012_africa/models_3d/riverborn/blender/source/chaosx_riverborn_recovery_2_provider_source.blend`
- `docs/assets/012_africa/models_3d/riverborn/blender/checkpoints/`
- `docs/assets/012_africa/models_3d/riverborn/blender/previews/chaosx_riverborn_recovery_2_*.png`
- `docs/assets/012_africa/models_3d/riverborn/blender/reports/chaosx_riverborn_recovery_2_prepare.json`
- `docs/assets/012_africa/models_3d/riverborn/blender/reports/generation_recovery_2_rejection.md`
- `docs/assets/012_africa/models_3d/riverborn/blender/rejected/generation_1_snapshot/`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_riverborn_meshy7_redo.md`
