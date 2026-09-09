# Meshy standalone motion endpoint

The user requested use of the new Meshy animation endpoint on 2026-09-09.
The parent accepted a bounded extension of the existing official MCP compatibility route and one prime, three-second standalone motion generation for the base zombie death candidate, with a ten-credit maximum and no additional paid attempts.
This acceptance applies to a source motion candidate; it does not approve replacement geometry, rigs, existing actions, or runtime promotion.

## Official contract and implementation

The [Text-to-Motion API](https://docs.meshy.ai/en/api/text-to-motion) creates standalone motion at `/openapi/v1/text-to-motion`; prime produces FBX for ten credits and swift produces BVH for three credits.
The prompt limit is 400 characters and duration is two to ten seconds in half-second steps.
Successful outputs expire after three days and must be downloaded immediately.
The [Animation API](https://docs.meshy.ai/en/api/animation) accepts a rig task with exactly one preset action ID or generated motion task ID; generated motion requires a biped rig, and optional post-processing can fail on GLB-only results.

The implementation remains inside the locked official `@meshy-ai/meshy-mcp-server` 0.4.0 runtime with SDK 1.29.0.
The compatibility patch adds explicit standalone motion tools and extends `meshy_animate` with exclusive `motion_task_id` input.
No client REST fallback is introduced.
The existing official client performs HTTP transport beneath the MCP handlers.
The new motion and animation POST endpoints cannot automatically retry after an ambiguous response.
Paid client submissions record a UUID journal before transport; uncertain submissions require task-list recovery.
Download uses the status response's exact format, permits only the Meshy asset host, refuses an existing destination, and verifies the returned task ID and SHA-256 against local bytes.

## Ownership and evidence

Changed sources are `.tools/3d_pipeline/meshy_client.py`, `.tools/3d_pipeline/wrappers/patch_meshy_mcp.mjs`, and `.tools/3d_pipeline/wrappers/meshy_motion_compat.mjs`.
Bounded regression coverage lives in `test_meshy_motion_endpoint.py` and the existing artifact compatibility fixture copy list.
The parent granted this lane narrow Meshy-only dependency-lock ownership to publish and verify the six compatibility file hashes; Blender fields remain with the adapter owner.
The schema lock now contains the five added tools' exact live declarations and the extended animation input schema.
Pre-existing wrapper lifecycle changes are preserved and are not attributed to this endpoint patch.

The deterministic pilot evidence root is `docs/assets/002_zombie_outbreak/models_3d/zombies/evidence/20260909_text_to_motion/`.
Its authorization record, upfront submission journal, request and response receipts, paid ledger, schema probes, task record, output receipt, and immutable source FBX form the pilot lineage.
The target rig handoff is `docs/assets/002_zombie_outbreak/models_3d/zombies/evidence/repair_2026-09-09/text_to_motion_target_handoff.json`.
The target remains `io_pdx_rig` with 24 bones in the protected calibrated checkpoint; the source bone map must come from actual FBX inspection.

## Validation and remaining work

Three no-spend tests pass: input bounds and exclusivity, upfront uncertain-request journaling, and actual runtime handlers including one-attempt POST transport.
Consecutive direct patch runs return identical six-file hashes.
Current read-only dependency checks match all sixteen adapter source hashes at 1.10.40, Blender 5.1.2 build `ec6e62d40fa9`, io_pdx_mesh 0.91.0 archive and installed manifest, and official package/SDK integrity.
Two consecutive and one concurrent pair of live tools/list probes passed with identical six-file hashes and zero surviving owned wrapper/provider processes.
The parent authorized bridge startup after the initial refused socket; an empty Blender process inventory preceded hidden bridge PID 17924, and its socket then passed.
The live balance was 392 before the sole submission and 382 afterward.
Task `01a084a7-4d94-72da-8518-b777e95399bf` succeeded in prime mode with 3000 ms duration and provider-reported consumption of exactly ten credits.
Its source was immediately downloaded as `death_prime_3s.fbx` with SHA-256 `22fd74c9a610f9aad5b2d959050647fda92d3f95e52b729ac89785267ef688b6`, matching the MCP download receipt and local bytes.
There were no additional paid calls, body generations, rig submissions, or provider retarget calls.
Two existing artifact compatibility regression tests also passed, retaining generation, rig, animation download and task inference behavior.

Retargeting, root-basis conversion, semantic death review, contact and deformation validation, export/reimport, sound synchronization, and runtime integration remain parent or Blender-owner work.
No final model, mesh, rig, action, audio, counter, or runtime file has been replaced, and no in-game completion is claimed.
No model identity or action requirement has been simplified.
The existing job's audio and counter provenance gaps remain inherited parent work; standalone motion sourcing does not satisfy them.

Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, and `chaos-redux-subagents`.

Both owned MJS sources have canonical LF bytes and identical raw versus Git-clean blob IDs; the exact hashes are recorded in the pilot evidence `git_clean_byte_proof.json`.
The parent added `.tools/3d_pipeline/wrappers/*.mjs text eol=lf` to `.gitattributes` to preserve checksum stability across Windows checkouts.
