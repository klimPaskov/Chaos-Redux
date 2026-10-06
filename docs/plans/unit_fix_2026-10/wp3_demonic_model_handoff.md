# WP3 demonic zombies model preflight handoff

Status: `blocked` for model production pending the parent-owned demonic material comparison and explicit release of the shared Blender slot. This file records read-only preflight only; geometry, UVs, rig, weights, actions, checkpoints, and runtime bytes were not changed in this turn.

## Scope and ownership

The authorized model scope is `demonic_zombies` geometry, rig, actions, and UV evidence under `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/`. The user-authored unit-fix plan authorizes its WP3 repairs, and the parent narrowed this worker's task to that existing model. The parent currently reserves the sole Blender slot for `wp3_model_resume` to finish the mutant and bounded demonic material comparison; this worker did not inspect or alter those in-progress preview files. The texture worker owns `wp3_textures_20261006/`, the audio worker owns WP3 audio candidates, and the parent owns runtime installation, wiring, commits, and final acceptance.

No Meshy work is required for this existing-model repair, so no `MESHY_API_KEY` check, provider route, balance probe, download, or paid operation was performed. No Blender process, adapter operation, Lab socket probe, desktop, or game was started by this worker.

## Inputs and baseline

The task brief is `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/unit_fix_plan.md`, section `Common rules` (lines 74–80), `WP3 / demonic_zombies` (lines 247–253), and cross-cutting section 3 (lines 422–458). The user-authorized plan hash recorded by the WP3 report is `1939b400cba160c6d4903e37952e8e55efdb1bfeacf0b4ab061e89c8792c79b2`.

The current installed mesh is `gfx/models/units/chaosx_demonic_zombies/chaosx_demonic_zombies.mesh`, SHA-256 `776595014bd9960a69bacd9d32b1dd8dbe914b3ae019a903c9e919b82026f47d`. The read-only native-import checkpoint is `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/blender/checkpoints/reimport_installed_776595014bd9960a.blend`, SHA-256 `F59E63B4CF0716D93AF087268C1441E5C0E8702E56C25ADEDF489C1357EAD92A`, with receipt `validation/reimport_installed_776595014bd9960a.json`, SHA-256 `20C4CAE80C0F597F6821485F791E0EB32622EE946C9A622A391867334E451D15`. Its proof scope is geometry/skeleton/action import only; it does not approve appearance, deformation, or actions.

The historical repair input checkpoint named by `blender/working/v1/intake_manifest.json` exists at `blender/working/v1/blender/checkpoints/05_pre_export.blend`, SHA-256 `847C4424562E9CC6BE3FE4464AC1DE503B093CD0387A07A470EAB17E5A0E2241`. The existing intake manifest and report preserve provider rig/action lineage, but the model root currently has no `job.yaml`, `manifest.md`, or `history.jsonl`; these files must be introduced as new repair intake metadata before adapter authoring, after the parent comparison is frozen. Do not replace the historical intake or select a mutable checkpoint until its source hash is rechecked.

The installed audit identifies 44 bones, 30,931 triangles, 38,298 vertices, four material streams, source height `7.3518247604`, entity scale `0.8`, effective runtime height `5.8814598083`, forward `-Y`, up `+Z`, and ground contact at `z-min`. The source-tolerance geometry gate is blocked at 50 boundary and 36 non-manifold edges with two same-direction edges; the stricter raw corner representation contains many seam duplicates and must not be broadly welded. The installed mesh remains the one frozen baseline hash above.

The installed-action baseline has 1 passing role and 7 blocked roles across idle, move, retreat, defend, death, training, attack, and support attack; the attack has 1,568 single-frame-limit violations. This is a measurement baseline, not proof that the in-progress preview or any action has been repaired.

## Locked route preflight

The observed dependency lock SHA-256 is `CB8D29299776135E33ACB5FED4DA5CF1F3188719704C0D9C81AD6E52A0A51856`, and the adapter config SHA-256 is `788858E3DC9E7D43A1717C419815F23935DC031F7BEEB1D50B13601E8AEB8543`. Static read-only verification found adapter id `chaosx_blender_hoi4`, lock/config version `1.11.0`, exact agreement for all 32 published operations, and no mismatch among the 36 locked adapter source hashes. The compatibility archive `blender-io_pdx_mesh-0.91-py313.zip` matches the locked SHA-256 `508643626FEFE78511903B1894B8B4D68C387EDD6228AD70487699A866886702`; the installed `io_pdx_mesh` manifest reports version `0.91.0`, and all three locked installed patch-file hashes match.

The same-day route evidence already recorded in `docs/assets/002_zombie_outbreak/models_3d/zombies/validation/wp3_model_repair_route_verification_20261006.json` reports Blender `5.2.2`, build `d13f752e3b9c`, adapter `1.11.0`, Lab route `1.0.3` at port `9877`, a live 26-tool Lab listing, and successful isolated mesh/animation export and reimport probes. This worker did not re-run health or probe the bridge because the Blender slot is reserved. Current tool exposure includes the locked `mcp__blender_hoi4__chaosx_blender_hoi4_*` route and Lab `mcp__blender_lab_dev__execute_blender_code`; exposure is not a new session-health result.

## Required production gates after slot release

The ticket requires forearm/hand skinning on Arm/ForeArm/Hand only with at most two adjacent influences and no Spine/Wing influence; measured elbow and wrist centers must lie inside the arm geometry. Blend wing membrane weights over three or four neighboring struts, feather strut roots into `WingX_Arm`, and cap adjacent-strut spread at 35 degrees. All eight actions must be rebaked on the accepted rig.

Attack must use a standing hip height of at least 3.8 units except for the 10-frame crouch at frames 20–30; fold wings until the slash, flare for no more than 12 frames at each claw peak, and return to the idle pose by frame 110 in the 120-frame/30-FPS role. Blend the first six frames from idle, author continuous arm quaternions over frames 30–46, and keep world joint speed at or below 0.25 units per frame. Support attack retains its leap at frames 29–47 and lands with torso pitch at or below 45 degrees.

Death must ease the fall at frames 36–46 and settle at frame 52 with six-frame wing transitions and grounded support. Training keeps three 12-frame stomps and matches frame 43 to frame 1. Idle is a real 150-frame loop with 0.15-unit chest motion, wing flutter within ±10 degrees, head turn, and claw flex. Retreat must loop-match. Move must ease the plant at frames 160–167 and prove one measured left and right plant over a 1.0–1.5 second cycle. The declared non-death root policy is `in_place_xy_preserve_z`; check death root-Z against the shared 0.2-unit ceiling.

For geometry, preserve the complete source-index/topology report; use only source-reviewed local repairs, and save every candidate as a new checkpoint. The authorized tolerance range for a specifically justified merge is 0.0005–0.002 units; it does not authorize a blanket weld across UV/material seams. Fill only reviewed holes of at most eight sides, recalculate outside only after ambiguity is resolved, and require the winding inspector to pass on the final decoded bytes.

The texture owner's current skin/head candidate is bound to mesh `776595014bd9960a69bacd9d32b1dd8dbe914b3ae019a903c9e919b82026f47d` and the current weight-derived UV selection. Any selected mesh or UV change requires notifying `wp3_texture_resume` to regenerate the face-ID/UV-region evidence and rebind its receipts. Do not edit or replace that worker's candidate maps or receipts.

Each accepted mesh and all eight accepted actions require export through the locked adapter/extension, actual-byte reimport, checkpoint and hash receipts, multi-view and deformation evidence, role-specific frame/contact measurements, and a final source-to-runtime crosswalk. Parent runtime installation and user live-game acceptance remain separate gates.

## Parent review update on 2026-10-06

The parent froze and installed the current-mesh diffuse and normal comparison in commit `69e22df402f1505a628fc9366d280a1fb942a7f7`.
The mesh remains `776595014bd9960a69bacd9d32b1dd8dbe914b3ae019a903c9e919b82026f47d`; installed diffuse is `319386bae79a81b50cc5afa9463ce2bf57b5463c321054db440e06cb0094926d`, and normal is `addb26aef0993f1e6d4a84b48ad1d42f86d4f8e467a864f7a61604dda77f9c73`.
The preview reservation is released; production is queued behind the single active mutant Blender worker.
The historical preflight below is retained, but the preview comparison is no longer a dependency.
New rig, UV or weight changes must rebind material-region evidence against the original preimage grade basis, without darkening the installed graded map a second time.
The unsupported specular recipe remains an external pipeline capability gap described in `wp3_pipeline_capability_handoff.md`.

## Current blockers and next step

Production is blocked solely on the parent-owned comparison closing and the explicit Blender-slot release. The repair intake metadata (`job.yaml`, `manifest.md`, `history.jsonl`) is also absent and must be created as new files before authoring, with the selected source/checkpoint and preview-install receipt frozen in that intake. The next owner should first confirm the parent's final demonic preview/install receipt and its exact selected mesh, map, checkpoint, and UV hashes, then prepare the repair intake and acquire the serialized worker slot before any Blender operation. If UVs change, coordinate receipt rebinding with the texture owner before final map acceptance.

No geometry, UV, rig, weight, action, texture, runtime, or audio work is claimed complete by this preflight. No simplification or fallback was used. No files were committed.
