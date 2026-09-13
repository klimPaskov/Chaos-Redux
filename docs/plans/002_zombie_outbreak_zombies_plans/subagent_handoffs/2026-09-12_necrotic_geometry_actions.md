# Necrotic geometry and skeletal actions

Status: in progress; no runtime promotion or in-game completion claim.
Owner: `/root/variant_zombies_finalize/necrotic_geometry_actions`, GPT-6-astra.
This child owns only the Necrotic job's Blender, export, validation, child evidence folder and this handoff.
The parent owns `job.yaml`, the aggregate manifest, runtime definitions/copies, package completion and commits.
Audio and counters have independent workers and remain outside this child's edits.

The current parent transport hold prohibits new Blender inspections, mutations and exports while adapter 1.10.48 is prepared.
Version 1.10.47 at commit `f8cf13409` was explicitly released by `/root` and the parent, and this child successfully used that release before the transport hold was reinstated.
Its config SHA-256 is `7E132374548AB958B46EA2F15517E2653DB222627AB7869E8260CAEAC45BF5DF`, dependency lock SHA-256 is `4BCB145321C06B527C70E6BE06F9745D5C7C0B43D2152DA43CAC2D880AF22547`, and release receipt SHA-256 is `746CEFF7A94F190EA71E19B1F8A2A1170EAE36E623163961EDEC4A9D32C72678`.
The fresh wrapper exposed 51 tools and the independent bridge probe found port 9876 listening.
All calls have drained; this child experienced no transport failure and will make no native call until another explicit release.
The exact three mutations sent during the 1.10.47 release, their receipts, source/checkpoint hashes and current dispositions are recorded in `evidence/necrotic_finalize_child_2026-09-12/transport_hold_mutation_inventory_20260912.json`.
Every completed native call used the repository wrapper through `BlenderAdapterClient`, with pre/post source and dependency guards and request receipts under `evidence/necrotic_finalize_child_2026-09-12/receipts`.
The stale direct-session Blender MCP route was not used.
The last released native health check reported Blender 5.1.2 build `ec6e62d40fa9` and loaded `io_pdx_mesh` 0.91.0 import/export operators.
The upstream extension ZIP SHA-256 is `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
The parent-accepted modernized deployment is verified through `.tools/3d_pipeline/reports/io_pdx_deployed_source_verification_20260912.json`, SHA-256 `9498FB8E634D53C3E290B4542E19A3AB7888DC672C4C3EB4999618AF78687866`, with 37 exact deployed matches, three expected absences and zero mismatches.
The wrapper driver verifies every deployed file and all locked adapter source hashes before and after each native call; it also verifies explicit input file hashes without relying on process presence as bridge evidence.

## Source, authorization and calibration

The source mode is `existing_runtime_recovery`, authorized on 2026-09-06 and explicitly resumed on 2026-09-12 for existing geometry, rig/weight repairs, missing components and all eight skeletal roles.
Upstream artwork URL, author, terms, provider task, source image and generation lineage are not recoverable from this package.
They are unknown, and this repair does not invent them or regenerate the asset.
The immutable recovered runtime bytes remain in `source/runtime`.
No Meshy operation is planned or consumed; estimated and consumed credits are zero.

The starting corrected skeleton/weight source is `blender/checkpoints/04_exact_weights_depth_v3_part2.blend`, SHA-256 `3A2F4D205E4C06F9BA2724721FB269AD75AF8F26F61088B740E863A92BC53246`.
The exact mesh is `mesh.003`, with 25,481 vertices and 30,000 triangles, bound to `chaosx_necrotic_zombies_rig`.
The emaciated, hunched zombie identity, hands/fingers, limbs and tattered waist covering remain intact.
No missing physical component has been proven so far; no geometry has been removed, simplified, welded or filled.

The installed vanilla reference is `gfx/models/units/western_european_infantry.mesh`, visible `polySurface106`, excluding collision-only `pCube1`, with `gfx/entities/units_infantry.asset#infantry_rifle_entity` and `gfx/entities/infantry.gfx`.
The vanilla source height is 7.351824797689915 and effective height is 5.881459838151932 at entity scale 0.8.
Necrotic source height is 7.351516008377075, rest-ground minimum is approximately 0.0010797977, and effective height is 5.881212806701661; the effective ratio is 0.9999579982764365.
The source geometry height is preserved and the parent must apply entity scale 0.8 exactly once.
The source-to-runtime scale crosswalk is `evidence/vanilla_scale_crosswalk.json`.

The original 1024 DDS maps remain unchanged.
The installed `gfx/FX/pdxmesh.shader` establishes packed green specular strength, blue metalness and alpha gloss for this `PdxMeshAdvanced` material; stale profile wording about alpha roughness does not justify inversion.
The material and source-copy audit is `evidence/finalize_2026-09-12/source_material_dependency_audit.json`.

## Native work completed

The exact 5,479-face main orientation repair uses the zero-contradiction approximate-seam component whose selected set is stable at 0.003 and 0.01 numerical tolerances.
This numerical graph classifies source faces only and does not weld geometry.
The selected checkpoint is `blender/checkpoints/04_necrotic_child_winding_main_v2.blend`, SHA-256 `60051F662A3E548BF4F13636C53FFA8220E59F218EB237D1BB59F7AC31C28D4B`.
The successful native request is `19a1c8bb52c54a78a5cce69371aa26b1`, with its saved/reopened report at `blender/reports/04_necrotic_child_winding_main_v2.json`.
All 90,000 corner normals were checked, and source vertices, UV corner association, rig, weights, actions, materials and images were preserved.

The first 0.25-degree normal guard rejected request `f4ca74a379f54e0aa6cdd8ac3254a87f` before saving any checkpoint.
It measured 0.4881781759620176 degrees of native split-normal encoding drift at selected face 17180 / vertex 14566.
The parent explicitly accepted the skill's bounded per-job 0.5-degree exception with exact source, reopened and visual evidence.
The successful retry used the same immutable source and exact face list; it did not compound a prior normal rewrite.
The evidence record is `evidence/necrotic_finalize_child_2026-09-12/winding_review_basis.json`.

Paired original-material and opaque-clay culling ON/OFF previews from request `5ba261a8a3dc48ed8c73a145f345b1fa` show continuous major face, torso and limb surfaces after repair.
Their prefix is `blender/previews/necrotic_child_after_main_v2`.
Fresh 1.10.47 focused original-material and clay culling ON/OFF reviews covered forearms from front/left/right and head/shoulders from front/left/rear.
Requests `863b254e49754804b9b883db23ef2538` and `82124ff4df02464a94ac187b9e7d5a99` show continuous forearms, wrappings and skull surfaces; eye, nasal and mouth cavities and folded wrappings do not justify further face flips.
The final rest-geometry selection therefore retains the main 5,479-face repair and adds zero extra faces, as documented in `evidence/necrotic_finalize_child_2026-09-12/geometry_selection_review_47.json`.
Fresh landmark request `e31331388b3e4342bfc938e406d1792b` reports exact topology SHA-256 `58BC4F4D83285596117D19973DBF6DF1EB4B9DE90CB879CE536DA21D1057016D`.
The independent emitted-array audit `selected_winding_corner_audit_47.json` confirms exact vertex positions, triangle membership, groups/weights, rigs/materials and per-vertex corner UV association; all 90,000 corner vectors remain within the reviewed 0.5-degree native-storage envelope.
Posed and exported-byte geometry review remains required.

A native attack candidate was authored and then rejected because its source weights stretch bands between torso and hands, and between the feet.
The rejected checkpoint is `blender/checkpoints/05_necrotic_child_attack_v1.blend`, SHA-256 `E86E8BC0E9CA4D1FEF2C3DACCF8BCD940BE7C39ABF0AAEF27D4E2BDA0CA3C6EC`.
Authoring request `0164233d21e94be789779bdabe69cdb6` and visual request `2ab5db7b20d94e0ca56c8abf5b84e64c` are preserved as diagnosis, not final action approval.
The decisive image is `blender/previews/necrotic_child_attack_v1_020_focused_2ab5db7b20d9_three_quarter.png`.

## Repair data prepared during maintenance

Fresh native landmark request `cf4a4f06a74849d8ac1dd0e1f9fc99e7` emitted the exact rest mesh, rig, corner normals and existing weights into `evidence/necrotic_finalize_child_2026-09-12/baseline_landmarks.json`.
Ordinary Python analyses use those emitted arrays and do not import Blender or change `.blend` files.
The rejected attack's maximum geometric edge stretch is 188.24 times its source length; normalized sums alone had concealed anatomical ownership errors.

The revised candidate classifies exact vertices through connected surface regions, preserving left/right identity where the left foot crosses the raw X axis.
It blends shoulder and pelvis boundaries through a numerical surface graph and projects upper-back/neck weights through the measured oblique bone axes.
It changes 20,153 explicit vertices, retains at most four influences, and has no zero-weight vertices.
Candidate files are `connected_skin_weights_v2.npy` and `connected_skin_candidate_review_v2.json` under the child evidence folder.
The applied, hash-locked batch specifications are `connected_skin_v2_batch_part1.json` and `connected_skin_v2_batch_part2.json`, with 10,077 and 10,076 exact expected/replacement rows respectively.
Earlier draft and v1 files are retained as superseded preparation and must not be applied.
The candidate attack maximum is 2.37 times source edge length at a small set of shoulder-joint edges, while idle, move and training have no flagged stretched/compressed edges under the recorded numerical test.
Native highlighted selections confirmed each full arm/hand and each leg/foot without torso, opposite-limb or waist-cloth misassignment.
The selection requests are `bf0105cad1a140679a313f6260ac83ea`, `ef0d098afbe44d0aaab2e99fc313dee0`, `030cf51d449e4f80ad6a5970cc381654` and `d7b1f6a47afd4d1b81145ba513196da4`.
The acceptance record is `skin_selection_acceptance_47.json`.

Both skin parts were applied successfully during the explicit 1.10.47 release, before the reinstated hold.
Request `f312d4e7dbe44d4d8955c391d6ffb70e` wrote `blender/checkpoints/06_necrotic_connected_skin_v2_part1.blend`, SHA-256 `24BB5DB8DC86FAF4B0878E719FDFAA2DFF9CE21DF51C3AF3AE680CE913972834`.
Request `98f8d62133a34993884f68b7e9a5ca27` wrote `blender/checkpoints/07_necrotic_connected_skin_v2_part2.blend`, SHA-256 `3B7058F11930198126E05E0581EBE603FBC0AD6ACA3434D803EA7C355213A0D1`.
Both native reports passed saved/reopened protected-invariant checks, preserved source bytes and exact topology, and changed only their declared vertex weights.
The reports are `blender/reports/06_necrotic_connected_skin_v2_part1_repair_explicit_skin_batch.json` and `blender/reports/07_necrotic_connected_skin_v2_part2_repair_explicit_skin_batch.json`.
The new skin still requires posed visual review and exported-byte validation.

Eight separate role specifications are prepared under `evidence/necrotic_finalize_child_2026-09-12/action_specs_connected_v5`.
Attack has been natively authored on the new skin; the other seven still require native authoring, and none is an exported animation yet.
The roles are idle, move, attack, defend, support_attack, retreat, training and death, all 30 FPS with in-place XY and native skeletal Z contact correction to 0.001 source units.
The support attack has a two-hand reach, clutch, haul and release; retreat and training have independent articulated poses and timing.
Death has knees giving, a braced fall, prone impact, recoil and settling, replacing the rejected hand-supported floating pose.
Its final numerical candidate has chest minimum 0.001, pelvis 0.00893, head 0.00129, hands approximately 0.008, and knees approximately 0.007 source units.
The candidate still needs native multi-frame deformation and actual-byte contact proof.
The matching native/reimport camera and frame plan is `evidence/necrotic_finalize_child_2026-09-12/native_action_review_plan_v5.json`.
It includes first, quarter, middle, three-quarter and final frames for every loop, full semantic attack/death phases, fixed camera regions and numerical anatomical support records for every frame.
All six loop candidates have identical first/last posed vertices in this numerical model; native curves, decoded renders and actual exported bytes still need to confirm that result.

Attack authoring request `4f2d0eb582b8456fabf75f53525814b5` was already in flight when the hold arrived and drained successfully.
It wrote `blender/checkpoints/08_necrotic_connected_attack_v5.blend`, SHA-256 `D89A9E7D1F10FFE440C4B02730B6E2C919F8056C0268C8861CFDCC61CEBEA97B`.
The action is `chaosx_necrotic_zombies_attack_connected_v5`, native action SHA-256 `62AAE722B38B5F1ED722091DFA18B3CD0ACE7F824169CDF77319B2056FFD5651`, 30 FPS, frames 1–51, non-looping.
Its native authoring report preserves body geometry and records all 51 ground minima between 0.0009997077286243439 and 0.0010003484785556793 source units.
Seven sampled native bounds agree with the emitted-array design within 0.000001026 source units.
The report review is `evidence/necrotic_finalize_child_2026-09-12/attack_v5_authoring_report_review_47.json`; visual semantics, joint deformation, anatomical support and actual-byte proof remain pending.

## Remaining work and parent handoff

- Wait for the explicit parent adapter release, refresh schemas and verify every locked source, Blender build, deployed extension and socket route.
- Resume from the saved `08_necrotic_connected_attack_v5.blend`; do not repeat the completed skin mutations or attack authoring.
- Review native attack contact frame 20 in matching front/three-quarter views, with source-bound topology/contact evidence and the rejected old attack available for comparison.
- Author the supported prone death and the remaining six roles into new sibling checkpoints, preserving the attack and every prior editable action.
- Review all eight real editable skeletal actions; inspect all-frame contacts, limb ownership, joint deformation, loop closure and prone collapse/impact/settling, with the fixed frame/camera plan.
- Partition the complete 30,000-triangle mesh for the PDX stream index limit without reducing geometry; each stream must remain within 65,535 triangle-index entries as well as vertices.
- Export the actual `.mesh` and all eight `.anim` files with `split_verts=False`, reimport those exact bytes, and collect matching multi-frame visual and contact evidence with final hashes.
- Give the parent all partition mesh settings, exact runtime action identifiers, selected-source/export hashes, DDS dependencies and validation limits.

The parent-owned runtime paths are `gfx/entities/chaosx_necrotic_zombies.gfx`, `gfx/entities/chaosx_necrotic_zombies.asset`, `gfx/models/units/chaosx_necrotic_zombies` and the Necrotic consumer in `common/units/zombies.txt`.
Stable proposed animation registration names are `chaosx_necrotic_zombies_<role>_animation`, with files `chaosx_necrotic_zombies_<role>.anim` in the existing runtime model folder and registration in `animation_chaosx_necrotic_zombies.asset` there.
Current role aliases in the existing entity are historical and must be replaced with the eventual eight distinct action exports.
The Necrotic counter consumers are `GFX_unit_necrotic_zombies_icon_medium` and `_medium_white`; the dedicated counter worker owns the original vanilla-green 152×42 large strip and 60×12 map strip package.
Armored Necrotic shares the model sprite but has a separate counter consumer outside this child's scope.
The independent audio and counter handoffs must be reviewed by the parent before any overall custom-unit package completion claim.

No requested role has been silently omitted or replaced with an alias.
The package remains incomplete while the native repair, exports, actual-byte proof and parent promotion are outstanding.
No live game was launched, and no in-game completion is claimed.
Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, and `chaos-redux-subagents`.
This child has not changed shared skills or committed incomplete work.
