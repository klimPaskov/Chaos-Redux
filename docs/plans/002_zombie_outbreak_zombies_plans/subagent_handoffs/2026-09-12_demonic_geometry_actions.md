# Demonic zombie geometry and skeletal actions

Status: unresolved while native repair and export work continues.
Owner: `demonic_geometry_actions`, GPT-6-astra.
Scope: `002_zombie_outbreak`, `demonic_zombies`; child-owned `blender/`, `export/`, `validation/`, and `evidence/demonic_finalize_child_2026-09-12/` only.
The parent owns aggregate job/manifest files, final runtime copies, entities, GFX, unit bindings, and integration; separate children own sound and counters.

The parent authorized existing-runtime recovery and Blender repair on 2026-09-06 and resumed the same work on 2026-09-12.
The model is a non-firearm skeletal creature with its original skull, long claws, and paired bat wings.
No Meshy operation, key gate, provider substitution, or paid recovery is required or used: estimated and consumed credits are zero.
Historical Internet artwork, creator, license, ImageGen refinement, and provider task lineage are missing; the existing source/runtime bytes and present copy provenance are preserved rather than given invented lineage.

## Current native checkpoint

The latest accepted transaction checkpoint is `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/blender/checkpoints/07_df_winding_complete.blend`, SHA-256 `C89DC133185433516F17FD263EBA0B0CF0805432C8BEB8337802A4CBF6AD7CA7`.
It contains the original 30-bone measured rig `chaosx_demonic_zombies_rig`, 296 mesh objects, 25,989 vertices, and 30,000 triangles.
Two exact winding transactions flipped the reviewed 37 faces of `mesh.007` and 47 faces of `mesh.009` while preserving positions, corner UV associations, every other mesh, materials, rig, weights, and actions through native save/reopen.
Maximum measured normal drift was 0.005977° and 0.007370°, respectively, within the retained 0.25° guard.
Native request IDs are `490f81f00c264fdaa69726d0ff38fd5e` and `c7ee20ad561747b4a6646a22506384c7`.
Their elapsed wrapper/preflight intervals were 143.865 and 121.790 seconds.

The completed batch winding transaction contains 5,455 exact face indices across 58 mesh objects in `evidence/demonic_finalize_child_2026-09-12/native_preconditions_1_10_47/winding_spec_source02_reviewed.json`, SHA-256 `5B8109AE1FFD2671B96B7CE6E9690C1CCA21C3CD5702B0BDEF7C3432EDAF63AC`.
The adapter owner supplied source-bound native topology, selected-corner preconditions, and a successful unsaved production preflight.
Native corner encoding measured 0.432124° on `mesh.070`, 0.376427° on `mesh.126`, and 0.296376° on `mesh.178`; those three exact objects use a reviewed 0.45° guard, while the remaining 55 retain 0.25°.
After explicit parent release of adapter 1.10.47, native request `dca33446919946259e84dbdd3c1c8484` saved and reopened the complete winding checkpoint in 33.259 seconds including route guards.
All 40,137 corners passed the declared directional guards, maximum measured drift remained 0.432124°, and complete protected snapshots and the reopened scene matched with zero discrepancies.
The resulting report is `blender/reports/07_df_winding_complete_repair_explicit_mesh_winding_batch.json`.
Matching culling and original-material review are still required.
A later temporary transport hold pauses further native work because two other workers received no JSON-RPC response to tool listing.
This child's tool listing, health, and saved winding calls returned successfully through the fresh wrapper, and no native call is running as this handoff checkpoint is written.

## Review findings and prepared repairs

Native original and opaque-clay culling ON/OFF baseline images are under `blender/previews/df_before_*`.
The exact winding list is supported by the source orientation/seam/ray diagnosis, but the full repaired surface still needs matched native post-repair review.
No weld, hole fill, triangle reduction, geometry rotation, or broad normal reset has been performed.

The original measured spatial weighting rules produce abrupt neighboring weight swaps between arms, torso, thighs, and wings.
Numeric replay of the recorded native source and deterministic weight rule matches the known native mesh weights and old death bounds to a few millionths of a source unit.
The old death draft has only claw support, a torso surface minimum around 1.44 source units above ground, and severe edge stretching; a global 1 mm minimum alone is insufficient acceptance evidence.
The torso, head, legs, and wing membrane support have been inspected as separate anatomical regions.

`surface_skin_v6_nativefloat32.npz` contains explicit candidate replacement weights for all 25,989 source vertices; `skin_candidate_v6_nativefloat32_metadata.json` records the complete flat vertex/index map and 30 bone columns.
Its SHA-256 is `47DA36D33C7C8777DA4EB8D839F5C2527931584CDE09EADB24467E1BF07D02B1`; the metadata SHA-256 is `A15B408D16865253340A78FBF38A26B769BB576725B1FA69FD22369CBB06CB5C`.
An unsaved adapter-owner preflight rejected v5 because a positive coefficient of approximately 1.57e-49 became zero in Blender's float32 representation.
The author explicitly removed coefficients below 1e-8, renormalized each row, and encoded every remaining requested value to its exact float32 value.
`skin_candidate_v6_nativefloat32_removal_ledger.json`, SHA-256 `54AD456C06B59DFF7B3BC51C0EA6CE18DC3E69CACEFB224CA89D69111E8EC2CC`, enumerates all 4,819 removed terms and the complete replacement values for the 4,212 affected vertices.
Maximum discarded row mass is 9.9478e-9, maximum complete v5-to-native coefficient change is 3.7421e-8, minimum positive weight is 1.0015677176511417e-8, and maximum native row-sum error is 4.89345e-8.
No adapter-side normalization, silent weight dropping, or saved native mutation is represented by this candidate correction.
Earlier surface-skin candidates, including the unquantized v6 variant, are superseded numerical drafts.
They use measured surface-distance seeds, analytic seam links without changing geometry, continuous four-influence truncation, and bounded local weight gradients.
The candidate has at most four normalized influences, zero opposite arm/leg/wing pairs, and zero simultaneous arm/leg influences.
It also excludes erroneous arm influences on the rear wing membranes through measured anatomical depth constraints.
Numeric phase stress over the original eight role designs improves the worst 99th-percentile edge stretch to 1.6559× and maximum to 2.9005×; these are planning measurements, not native deformation acceptance.
The adapter owner's full unsaved production preflight passed all 296 meshes and 25,989 requested vertex rows with the exact float32 v6 candidate.
The exact native source priors are copied to `native_preconditions_1_10_47/demonic_native_skin_inventory_1_10_47.json`, SHA-256 `E5E3BF930D9A508B5E7D9601A6240A42F7468794DE4B3AF42F6E38007B6C25DF`.
The complete exact indexed skin specification is `native_preconditions_1_10_47/demonic_skin_batch_source_preconditions_1_10_47.json`, SHA-256 `8C5015EAC8EC903C6928B463F73B86FAB88397E14BD388687ADE4D7EB6FF82B4`.
Those original preconditions bind checkpoint `06_df_winding_02.blend`.
The actual saved winding transaction's 58 reopened topology hashes have been used to create `native_preconditions_1_10_47/skin_spec_after_winding_nativefloat32_v6.json`, SHA-256 `2F01A871144244096CE60548518FF1783CF89CEA6C8A1D6B31C1480A171BBC52`, bound to current checkpoint `07_df_winding_complete.blend`.
The complete 25,989 replacement rows were compared to the exact v6 NPZ with no difference; `skin_source_binding_v6.json` records that proof and the native prior preservation chain.
All prior weights remain native measurements, and no inferred prior weights are used.
The preserved parent report is `.tools/3d_pipeline/reports/explicit_batch_repair_1_10_47_production.json`, SHA-256 `929F64E61CD3D477D612EF53558263D4994F5CFD020419E5094D491F8B23B5FB`; its relevant contents and hashes are copied in `native_preconditions_1_10_47/adapter_owner_demonic_preflight.json`.
Actual indexed mutation, reopened proof, and native deformation acceptance remain required.

Seven refined standing-role JSON specifications are prepared under `evidence/demonic_finalize_child_2026-09-12/action_specs/refined/`.
Move now has alternating planted stance and clear return swings, retreat has independent backward guarded steps, and attack/defend/support_attack receive bounded ankle articulation for two-foot stance without limb translations.
Idle and training retain independent chest, head, arm, and wing movement.
The action names are unique, the loop endpoints match, and numeric quaternion hemisphere checks find no adjacent-key sign discontinuity.

The death candidate is `evidence/demonic_finalize_child_2026-09-12/action_specs/death_contact_v4.json`.
It retains the original first three collapse phases, adds knee impact and chest impact, then articulates the shoulders, elbows, wrists, hips, knees, ankles, neck, skull, and all eight wing bones through settling.
Numeric terminal support includes torso, head, both arms, and both legs; the original wing-droop ground-strut error is removed.
With the v5 skin, the terminal candidate predicts minimum source-unit heights of 0.00494 for the torso, 0.039 for the head, 0.00525 and 0.001 for the arms, and approximately 0.041 and 0.017 for the legs.
The death contact candidate remains unapproved until it is authored on the repaired native skin and reviewed at impact, settling, intervening frames, and actual-byte reimport.

## Source calibration and dependencies

The named vanilla precedent is `gfx/models/units/western_european_infantry.mesh#polySurface106`, excluding collision `pCube1`, and `gfx/entities/units_infantry.asset#infantry_rifle_entity` at entity scale 0.8.
The Demonic source height is 7.36240029335022, rest ground is 0.43564486503601074, and effective height is 5.889920234680176.
Vanilla source height is 7.351824797689915 and effective height is 5.881459838151932, a ratio of 1.0014384858115264.
Geometry height remains unchanged, grounding is separate, and entity scale is applied once by the parent.
Anatomical transverse is `(X-Y)/sqrt(2)`, depth is `(X+Y)/sqrt(2)`, and Z is up.

The latest native calls use locked adapter 1.10.47, released in parent commit `f8cf13409`, through the fresh `.tools/3d_pipeline/wrappers/run_blender_hoi4_adapter.cmd` route, Blender 5.1.2 build `ec6e62d40fa9`, and io_pdx_mesh 0.91.0.
The configuration SHA-256 is `7E132374548AB958B46EA2F15517E2653DB222627AB7869E8260CAEAC45BF5DF`, dependency-lock SHA-256 is `4BCB145321C06B527C70E6BE06F9745D5C7C0B43D2152DA43CAC2D880AF22547`, and release-receipt SHA-256 is `746CEFF7A94F190EA71E19B1F8A2A1170EAE36E623163961EDEC4A9D32C72678`.
Fresh wrapper tool listing returned 51 tools with schema SHA-256 `90054E6AF95754CFF3A017EAE4A09B1402360DFE8F4C8501519F9553AB250DB7`; native health request `c2479406166a43289728d1578eb60bbe` confirmed the expected Blender and loaded export functions.
The upstream ZIP checksum is `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
The accepted deployed modernization is separately verified by `.tools/3d_pipeline/reports/io_pdx_deployed_source_verification_20260912.json`, SHA-256 `9498FB8E634D53C3E290B4542E19A3AB7888DC672C4C3EB4999618AF78687866`, with 37 exact present files, three expected absences, and zero mismatches.
Each child native call verifies the current coherent lock and source files, separately probes socket 9876, captures a request receipt, and verifies the response adapter version.
The stale directly exposed 1.10.44 session route is not used.

Original 1024-square diffuse, packed specular, and normal DDS maps remain unchanged.
Installed `gfx/FX/pdxmesh.shader` uses alpha for gloss, green for strength, and blue for metal; the historical source-map inversion lineage is unclear, so no blind inversion is made.
The exact original/source/runtime byte audit is `evidence/finalize_2026-09-12/source_material_dependency_audit.json`.
Standalone Technology Tree Viewer absence on checked surfaces is separately recorded through the shared hashed evidence link `evidence/demonic_finalize_child_2026-09-12/viewer_evidence_link.json`; technology tool exposure is not treated as application or service-health proof.

## Remaining work and validation limits

- Finish exact winding and review matching original/clay culling ON/OFF native views.
- Capture fresh native indexed weights and topology, apply the explicit skin candidate, and review extreme deformations and anatomical ownership.
- Actually author all eight refined semantic actions on the final native rig; inspect native contact, stance/swing timing, loops, intermediate poses, and death support.
- Export the final mesh and all eight animations with the locked exporter, reimport the actual bytes, and compare facing, bounds, material references, native motion, and contacts.
- Record selected export paths and hashes for parent synchronization and integration.

No final source or export is selected, no role is claimed complete from a JSON specification, and no in-game completion is claimed.
The package remains incomplete pending those native repairs and validations.
No incomplete commit is made.
