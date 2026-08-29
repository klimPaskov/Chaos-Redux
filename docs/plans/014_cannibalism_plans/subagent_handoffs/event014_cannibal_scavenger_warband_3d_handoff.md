# Event 014 Cannibal Scavenger Warband 3D handoff

> Historical source-only handoff. Superseded by `event014_scavenger_warband_v2_runtime_handoff.md`, which records the accepted Meshy/Blender exports and runtime wiring; retain this file for rejected source-lineage evidence only.

Status: **blocked pending user approval of actual Internet-sourced artwork; no Meshy calls permitted**.

The deterministic job intake, source-only artwork audit, action-source plan, audio audit, counter crosswalk, dependency evidence and parent/runtime boundaries are recorded under `docs/assets/014_cannibalism/models_3d/cannibal_scavenger_warband/`. No gameplay, GFX, entity, localisation, sound-definition, spreadsheet or shared toolchain file was edited.

## Current source-only override

The user rejected generated references. `refs/original/meshy_input.png` (`CE1D002E66864A08F52DF1DA94C399146E16A0F90CE33BF69BE90129EF70B417`) and `provider/downloads/current_exact_input_model.glb` (`9ED62CEB4013A87DEDDF014242706B6D5844C1A9A5ADCF18582FE0164D414F6F`) are superseded evidence only. No Meshy call was made in this worker run, and there are no owned Meshy wrapper descendants to release.

The completed source audit is `refs/sourced/candidates/source_only_2026-08-22/source_audit.md`. Its recommended licensed candidate is Justin Nichol's `Raider3` concept, CC BY-SA 3.0, at `refs/sourced/candidates/source_only_2026-08-22/original/justin_raider3.jpg`, SHA-256 `6330FB23338875E9D6E71329D4AAA7E1D33A55DBAF891D1F8E55A262B72B2F90`. It is a complete single full-body scavenger with coherent contact on one long spear and no crop loss. The more aggressive Gaspard farmer concept is the runner-up, but its pitchfork leaves the frame and the artwork includes scenic marks. No candidate was promoted or modified pending user approval.

## Files created

- `job.yaml`
- `manifest.md`
- `history.jsonl`
- `runtime/crosswalk.md`
- this handoff

## Provider and dependency state

The former generated input checksum matches `input_manifest.json`: `CE1D002E66864A08F52DF1DA94C399146E16A0F90CE33BF69BE90129EF70B417` (1148×1722 RGBA). It is no longer approved and must not be used. Meshy 7 remains the only permitted future generation model after a source-only input is approved.

The initial preflight verified official `@meshy-ai/meshy-mcp-server` 0.4.0 at git head `d8c77d1cb897e345eb41d38b510b8391b1664346`; SDK 1.29.0; compatibility revision `meshy-7-v4`; Blender 5.1.2 build `ec6e62d40fa9`; the then-locked adapter 1.8.0; and io_pdx_mesh 0.91.0 with archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`. Blender health request `7094326c1fac4e2e9c659709dfb10c87` passed and the bridge was reachable on port 9876.

Concurrent shared edits changed `blender_worker.py` to SHA-256 `F2C984E97B70CC84EAAAE10D4CFE0602F67A3880B20A28A22C49135DAD313E9E` and changed the working-tree lock to adapter 1.8.1. The parent subsequently verified adapter 1.8.1 and all 25 locked wrapper operations; a fresh local `verify_environment.py` run returned zero findings. Repository-wrapper health request `b725e121cbf047e3b4c07048320c6e82` independently reports adapter 1.8.1, Blender 5.1.2, loaded io_pdx_mesh and both export functions. The reconciled `dependencies.lock.json` hash is `39BEC68E5B356D6BB0BD0B7463C9FF761F8572E0453405DB929AAAC4292289F2`, and `blender_hoi4_adapter.json` is `C8CF20F9C177D32AB0593BF9CA128BB369E9E24640BB436E310EE42EB9698F29`. This session's static MCP declaration remains stale, so Blender work must use the verified repository wrapper/client. No shared process was stopped.

An inherited earlier live Meshy probe exposed `meshy-7`, all required Meshy tool identifiers, and balance 835. This worker made no Meshy schema, balance, status, polling, download, or paid call. Credits consumed in this run: 0. The future plan remains estimated at most 65 credits, but provider work is blocked by source approval and remains subject to the parent-owned serialized lease. Earlier inherited/rejected provider lineage records 96 historical credits and remains evidence only.

## Non-paid generated-lineage QA retained as evidence

Before the user source-only override, repository adapter 1.8.1 imported and audited `current_exact_input_model.glb`. Successful prepare request `f4dc779e86d14f2783bc5e2e1acf7876` measured 29,999 triangles and 14,789 vertices, normalized source height to the vanilla 7.3518247604 target, and found no non-manifold geometry, degenerates, or negative scale. It also found 257 loose boundary edges, no armature, and no actions. Segmentation request `569f934284704f3bb52883402245ac2c` found one 29,897-polygon body component containing all back-mounted stakes and weapons plus one tiny 102-polygon accessory. Review request `5cbea0e02691405fac33bbe19154af46` confirmed no separable or hand-held spear. The associated checkpoints and multi-view previews are retained only to explain rejection; they cannot be promoted.

The existing recovery task `01a02992-255c-781d-b910-377d9d771a97` was also reviewed through its explicit component renders. The spear is welded into the primary humanoid component while only a tiny detached accessory forms component 1. It belongs to the obsolete `5CBD...` reference lineage rather than the approved `CE1D...` exact input and remains rejected evidence only.

## Action source plan

All roles use distinct official Meshy library candidates: idle 89, move 672, spear-thrust attack 240, defend 149, support attack 92, retreat 688, training 199, and death 184. Every result remains subject to semantic, weapon-contact, deformation, ground-contact, root, FPS, loop and reimport review. No existing local `humanoid_action_*` report is accepted as final motion.

## Companion packages

The sourced audio package covers selection/acknowledgement, movement, idle, spear attack, impact and death. All six derived WAVs are signed 16-bit PCM, 44100 Hz, mono, with immutable originals, source pages, licences and checksums in `evidence/audio_sources/`. Final synchronization points remain conditional on accepted final action frames.

The bespoke counter package is present and registered for all three consumers. The audited hashes are `82DB80534E536E7714B68082F044A9B9B14B7BB64C00AC7A59880944A09D9B7A` (large), `7593F9E064A4FD28923216AC3C5204FEE7584A4A222A19D966ECDD5CD9665411` (on-map), and `51527B0DF60D23B5876EDF8A0D47B08E51104DD1C53AA83D8E19F83449E114CB` (texticon). Installed vanilla consumer/reference and sampled palette evidence are recorded in the existing Event 014 counter handoff.

## Remaining work

- obtain user approval of one clearly licensed actual Internet-sourced artwork candidate
- after approval, mechanically prepare the exact-one input only if crop, padding, background, or alpha cleanup is necessary, then record its immutable source relationship and checksum
- only then obtain the parent-granted serialized Meshy lease for any provider call
- accept/reject geometry from multi-view Blender evidence, then rig and produce all eight distinct provider actions
- prepare PDX materials, audit geometry/rig/weights/actions, export one `.mesh` and eight `.anim`, and retain locked reimport proof
- reconcile final audio phases against accepted action frames
- record final task IDs, response IDs, credits, checksums, previews, export results and synchronization handoff
- parent to perform runtime copy and `.gfx`/`.asset`/entity/sound-definition wiring, live consumer review and in-game validation

No simplification or fallback has been accepted. The package is incomplete because source selection, geometry, materials, rig, all eight professional-source actions, mesh/animation exports, reimports, and final audio synchronization remain blocked. No in-game completion is claimed.
