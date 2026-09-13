# Stone Cohorts and Forest Giants 3D finalize handoff

Status: in progress; native Blender work is paused by the parent’s transport hold while adapter 1.10.48 is prepared.
This document records the current source selection and open work; it is not a package-completion claim.
It supersedes the current-state and provider-action requirements in the two 2026-09-06 repair handoffs while retaining those files as production history.

Owner: `/root/stone_forest_finalize`, GPT-6-astra.
Scope is limited to the two package roots, their matching handoffs, and package-local evidence.
No gameplay, GFX, entity, sound-definition, or other shared runtime file was changed by this worker.

## Current checkpoints

| Package | Current source | SHA-256 | State |
|---|---|---|---|
| Stone Cohorts | `docs/assets/012_africa/models_3d/stone_cohorts/blender/checkpoints/66_forearm_chip_solid_finalize_20260912.blend` | `FC0BD069B529C9EB597821EB5B52A6231A107B8ED57434D7F9DF6AA9F3C4C2D5` | Solid forearm-chip repair and winding pass; body weights, final QA, partition, export and reimport remain open |
| Forest Giants | `docs/assets/012_africa/models_3d/forest_giants/blender/checkpoints/17_death_grounded_v7_finalize_20260912.blend` | `418457D2CFDA3B6F155EEAB1A43D11C9C6E7E87DA3800E0ECAFF76AAB672CCB5` | V7 articulated death authored and reopened; body weight corrections, native review, final QA, export and reimport remain open |

Neither checkpoint is selected for runtime promotion.
There is no accepted final `.mesh` or five-action `.anim` export set from this repair yet.
The Stone failed partition request did not create checkpoint 67; its report and exact fingerprint difference remain preserved.

## Source and generation lineage

These are Blender-only repairs of accepted existing non-firearm geometry.
No Meshy key, provider, balance, generation, rigging, or animation call was made in this resumed repair; estimated and consumed credits are both zero.
All retained and repaired skeletal actions use the authorized manual GPT-6-astra Blender route.

Stone uses the accepted dark ornate guardian and polearm identity, Meshy task `01a0351e-c350-74ce-ac5f-4a1d158a87ee`.
Its retained body GLB is `provider/downloads/generation_2_t_pose/stone_cohorts_meshy7_t_pose.glb`, SHA-256 `4ffbbca6c2fd3fac1c8f20cbf95162e6bb30aa9036e2cc78ddff05c23c260e13`.
Its accepted refinement is `refs/original/meshy_input.png`, SHA-256 `79ec9e39148d734468e20171391c7068704a877c014562cd85b1a1afacc19ccb`.
The selected modern artwork, actual-artwork authorization, source terms, refinement prompt, transparency fallback, and approval lineage remain in the package’s `refs/source/provenance.json` and reference evidence.
The retained August 24 source record identifies FromSoftware’s “ER Golem w Halberd.jpg / Guardian Golem (Halberd),” published by Bandai Namco and hosted on [Eldenpedia](https://eldenring.wiki.gg/wiki/File:ER_Golem_w_Halberd.jpg), under the recorded `reference_only_user_authorized` basis.
Its transient source hash is `c3ebde674062fed399dbcc7fab27965d9b1c2125544164802d027fd22d180833`; source bytes were discarded under the recorded fair-use/reference-only archive decision and are not runtime art.

Forest uses the accepted woody giant, broad axe, bound log, and crown mantle identity, Meshy task `01a04333-952c-7726-a8c9-8e9ae388049a`.
Its retained body GLB is `provider/downloads/meshy7_generation_4_tpose/forest_giants_meshy7_tpose.glb`, SHA-256 `60e01f77e07e0efd6e2ff00f76a34184deee606af2307c5c17c6122f5c4923b1`.
Its accepted refinement is `refs/original/meshy_input.png`, SHA-256 `24cab4399f694daa0390ac8ad91fc48b8ed5ff260878ba883f0b714345f1da41`.
The authorized DM Stash modern miniature reference and non-shipping source bytes, source terms, refinement prompt, transparency fallback, and approval lineage remain in its `refs/source/provenance.json` and reference evidence.
The retained August 24 record identifies DM Stash’s “Trostaka the Vengeful - Treant of Hatred,” corroborated by the [named design page](https://mitznsimz.com/products/treant-of-hatred-trostaka-the-vengeful-by-dm-stash) and the recorded [Etsy landing page](https://www.etsy.com/market/tree_bark_armor).
It records copyrighted professional artwork, parent-relayed explicit reference-only authority, no incompatible restriction found on the reviewed surfaces, and non-shipping `refs/source/untouched.jpg`, SHA-256 `45a412cc66f5f302de2efb7ee7752e8bb291401f06f4250ef3f2c1ac55d35f15`.
The cleanup prompt is `refs/briefs/replacement_source_faithful_cleanup_prompt.md`.

## Geometry, scale, materials and rigs

The installed vanilla source is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/asian_infantry.mesh`, used by `asian_gfx_infantry_entity` at scale 0.8 in `gfx/entities/units_infantry.asset`.
The visible vanilla source height is 7.390917778 and effective runtime height is 5.912734222; the collision-only `pCube1` is excluded.
Retain the accepted custom source body heights of 11.275205 for Stone and 18.792008 for Forest, with custom entity scale 1.0 applied once, +Z up and -Y forward.

Stone has a 29-bone `chaosx_stone_measured_rig`, 23,802 body triangles and an 876-triangle rigid `stone_ornate_polearm`, totaling 24,678 triangles below the 25,000-triangle package budget.
The former isolated duplicate reverse-wound forearm triangle is a closed four-face solid chip; all retained vertex positions, UVs, weights, rig and action data were preserved in native request `4adde0f8961c44fea0c2accc872340df`.
Native winding request `3510cc95ea5b4b589d884e1e950ae11d` reports no ambiguous winding and no required flips for either working mesh.

Forest has a 27-bone `forest_giant_rig`, a 23,500-triangle body, broad axe, bound log and grip-vine components, totaling 24,836 triangles below the 25,000-triangle budget.
The crown mantle is retained in the skinned provider body; axe and log use separate rigid controls.
V7 death native request `b3b1fb8136de450aa3ecfcd91babaa41` saved and reopened the source with native action SHA-256 `7BBB814FF11BAA1D022D215ECE26748EFD772979A695FD3FA6CDE62CEDE4F507`.
Its numerical support positions do not establish acceptance because retained wrist/shoulder weight discontinuities still require correction.

Both packages retain immutable provider maps and the existing 1,024-pixel PDX body DDS conversion receipts under `textures/blender_repair_20260906/` and `evidence/blender_repair_20260906/`.
Final texture visibility, final material bindings, and actual exported/reimported DDS use remain open.

## Weight corrections prepared during the hold

The data-only studies reconstruct recorded native action/phase geometry within 4.5e-6 world units; they do not operate Blender or replace native visual acceptance.
They identified actual discontinuities at anatomical boundaries that older weight-count and normalization checks did not detect.
Every candidate preserves source geometry and the current skeleton and uses at most four normalized influences without mixed-side or spatial opposite-side assignments.

| Package | Candidate | Changed existing body vertices | Maximum phase edge-length ratios after the candidate |
|---|---|---:|---|
| Stone | `evidence/finalize_20260912/stone_skin_local_v6_candidate_rows.json` | 8,254 | idle 2.21, move 2.21, attack 2.28, recovery 2.68, death 2.53 |
| Forest | `evidence/finalize_20260912/forest_skin_anatomical_v2_candidate_rows.json` | 10,035 | idle 2.18, move 2.18, attack 2.40, emergence 2.28, death 3.02 |

Stone’s baseline maxima reached 17.89 at recovery and 16.51 at death; Forest’s baseline death reached 35.51 at a wrist/thumb boundary.
The Stone data inventory predates the added chip apex in checkpoint 66; refresh that native inventory and include its new vertex before creating the final exact skin specification.
Both candidates still require source-explicit native topology and selection proof, per-vertex repair, all-frame contact and deformation checks, loop checks, rigid attachment review, and textured/clay visual review.

## Required actions

All actions are 30 FPS and remain editable skeletal actions in the checkpoints.

| Package | Role | Current action | Frames | Loop |
|---|---|---|---|---|
| Stone | idle | `chaosx_stone_idle` | 1–61 | yes |
| Stone | move | `chaosx_stone_move` | 1–49 | yes |
| Stone | attack | `chaosx_stone_attack` | 1–61 | no |
| Stone | recovery | `chaosx_stone_collapse_recovery` | 1–79 | no |
| Stone | death | `chaosx_stone_death_contact_v8` | 1–79 | no |
| Forest | idle | `chaosx_forest_giant_idle` | 1–61 | yes |
| Forest | move | `chaosx_forest_giant_move_repaired` | 1–49 | yes |
| Forest | attack | `chaosx_forest_giant_attack` | 1–61 | no |
| Forest | emergence | `chaosx_forest_giant_concealment_emergence` | 1–76 | no |
| Forest | death | `chaosx_forest_giant_death_grounded_v7` | 1–91 | no |

After weight changes, recheck ground correction against actual deformed geometry and refresh each action’s acceptance evidence.
The current action names and frame timings are candidates until that review is complete.
Each package’s `action_semantics_lineage.json` records five distinct native action hashes and phase-varying articulated bones: Stone has 15/14/17/16/16 for idle/move/attack/recovery/death; Forest has 4/10/8/15/18 for idle/move/attack/emergence/death.

The parent-owned registrations are `chaosx_stone_cohorts_entity` / `chaosx_stone_cohorts_mesh` and `chaosx_forest_giants_entity` / `chaosx_forest_giants_mesh`.
Their current model destinations are `gfx/models/units/012_africa_stone_cohorts/chaosx_stone_cohorts.mesh` and `gfx/models/units/012_africa_forest_giants/chaosx_forest_giants.mesh`.
Retain the existing registered animation type names `chaosx_stone_<role>_animation` and `chaosx_forest_giant_<role>_animation` from `gfx/models/units/animation_012_africa_strange_forces.asset`, using generic role export filenames even where the editable action has a repair suffix.
The current legacy `Mesh_0.001` meshsettings must be replaced by the exact final stream/material names returned by the new export and actual-byte reimport; those names cannot be finalized before the exports exist.
The current Stone and Forest death states still transition to idle and their sound events have no phase time.
Parent integration must reconcile terminal non-looping death behavior and all event times with the selected final actions and the audio handoff.

## Sourced audio and original counters

Each package’s `audio/manifest.md`, `audio/handoff.md`, and `audio/evidence/source_research.md` now point to its current `audio/finalize_20260912/` delivery candidates.
The two machine-readable `source_to_cue_ledger.json` files record 13 current WAV cues, exact source and output hashes, source excerpts, transformation filters, codec receipts, sound/soundeffect identifiers, action phases and proposed event times.
All cues are source-derived mono 44,100 Hz signed 16-bit PCM WAV; there is no generated, synthesized, newly recorded, pitched or layered audio.
Commons public-domain, CC BY 4.0 and CC BY-SA 4.0 originals are preserved; Forest additionally retains official Freesound CC0 public HQ source downloads for dry-wood creaks and actual axe strikes.
The distributed cues require the accompanying attribution/change notices, including CC BY-SA 4.0 for Stone’s metal derivatives.
Numerical signal/codec checks were performed; listening acceptance is not asserted.
Final animation synchronization and runtime sound wiring remain open.
The mandatory selection/acknowledgement role has an explicit blocker: the inspected installed selection wrapper is global `select_army`, and no exact per-subunit selection hook has been established.

The parent visually accepted and promoted all four bespoke counter DDS outputs in commit `9fd0240264dfab28ca89cf1f8b780734957ccf57`.
Both package-local `counter_parent_promotion_receipt.json` files verify current staged/runtime byte equality.
The detailed counter handoff is `2026-09-12_stone_forest_counter_handoff.md`; manifests and `gfx_handoff.md` under each `counters/finalize_20260912/` record the exact installed vanilla definitions, DDS references, two-frame sizes and order, sampled green/neutral palette, native-alpha sources and round-trip evidence.
The existing parent-owned registration is `interface/012_africa_strange_force_counters.gfx`, with large `GFX_unit_<slug>_icon_medium` and map `GFX_unit_<slug>_icon_medium_white` consumers, each using `noOfFrames = 2`.
This worker made no runtime counter edit and claims no in-game validation.

## Dependency and continuation gate

Blender is the locked 5.1.2 build `ec6e62d40fa9`; io_pdx_mesh is the checksum-locked 0.91.0 deployment.
The accepted deployed-source receipt `.tools/3d_pipeline/reports/io_pdx_deployed_source_verification_20260912.json`, SHA-256 `9498FB8E634D53C3E290B4542E19A3AB7888DC672C4C3EB4999618AF78687866`, records 37 exact present matches, three exact expected absences and zero mismatches.
Each package-local runner call verifies the lock-selected source set, wrapper schema, source checkpoint hash, deployed exporter and independent port 9876 bridge connection.
The stale direct MCP route returning adapter 1.10.44 is prohibited for current work; use the fresh lock-selected `BlenderAdapterClient` wrapper.
Native requests through 1.10.45 are preserved with their exact version and request identity; future requests must match the parent’s released coherent lock rather than reuse a fixed version.

The failed Stone partition request `567ac9b2043b48d182ff2dbe1c6ccde2` reported only verified material-clone image-consumer bookkeeping differences and no checkpoint save.
Its immutable evidence is `stone_partition_result.json`, `stone_partition_fingerprint_delta.json`, and `blender/reports/67_export_partition_finalize_20260912_partition.json`.
The parent accepted the operation-scoped repair in 1.10.46 and the bounded skin/winding/corner-normal additions in committed 1.10.47 at `f8cf13409`.
The verified 1.10.47 release receipt is `.tools/3d_pipeline/reports/explicit_batch_repair_1_10_47_release.json`, SHA-256 `746CEFF7A94F190EA71E19B1F8A2A1170EAE36E623163961EDEC4A9D32C72678`; its config and dependency-lock hashes are `7E132374548AB958B46EA2F15517E2653DB222627AB7869E8260CAEAC45BF5DF` and `4BCB145321C06B527C70E6BE06F9745D5C7C0B43D2152DA43CAC2D880AF22547`.
The fresh package wrapper returned all 51 operations, but the parent reinstated a transport hold after another worker reproduced an intermittent stdin EOF/response race.
No Blender mutation, export, or inspection request was dispatched between those temporary releases or during this hold.
Each package’s `transport_hold_source_disposition.json` records a fresh byte check of the unchanged selected source and zero newly dispatched native requests.
The next native requests require the parent-released coherent 1.10.48 lock and wrapper transport.

## Remaining work and limits

Complete native skin selection/repair and visual review, refresh all-frame contact/deformation and loop evidence for all ten actions, confirm material visibility and winding, partition the skeletal export streams where needed, export the actual selected `.mesh` and ten role `.anim` files, stage the exact referenced DDS files and reimport those actual bytes.
Only a passing final source/export/reimport/hash set can establish a runtime promotion list.
The parent owns final model, animation, entity and sound wiring and reviews the returned package evidence.
No requested component or action has been intentionally omitted or replaced with a static alias; the package remains incomplete while these explicit checks and blockers are open.
No in-game completion is claimed, and no incomplete 3D package commit has been created by this worker.
Each package’s `evidence/finalize_20260912/held_state_checksum_manifest.json` is a point-in-time inventory of the exact created, restored and reconciled files, sizes, hashes and tracked-file status, including native request logs.
It is explicitly a held-state inventory, not a final shipping or acceptance manifest.
