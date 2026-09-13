# Chaos Assault Battalion repair continuation

Status: incomplete working package; adapter maintenance hold continues through coherent 1.10.47 release at this checkpoint.
The parent owns runtime model/entity/GFX/sound wiring and final asset acceptance.
No in-game validation is claimed.

The package source of truth for this continuation is `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/manifest.json`.
The September 6 handoff remains historical evidence and must not be read as final acceptance of the assembly.
The old system document `docs/systems/3d_model_pipeline/chaosx_chaos_assault_battalion_model.md` still describes superseded action aliases and requires parent reconciliation after final model selection.

## Current candidate

`blender/checkpoints/attack_flexible_hose_20260912.blend`, SHA-256 `71CE1516C069969F2DABBE50191E5F36F3878952C94450CE501AE521E3AD5D96`, is the latest working assembly.
It has 30,362 triangles: the repaired body, a separate 858-triangle source-faithful held projector, and a closed 192-triangle flexible hose added to the body mesh with explicit Hips/RightHand weights.
The skeleton remains `io_pdx_rig`, 24 bones.
The old fused projector was removed before attachment, so no second complete projector remains at the hip.
The visible coarse cap left under that extraction still needs garment reconstruction.
The hose has not yet passed posed preview, full contact/deformation review or export/reimport.

The exact source-faithful projector attachment is `evidence/projector_component_attach_response_20260912.json`, request `a7631957ee1e4b70bce1c86329cf4e8f`.
Its 770 source faces are distinguished from 88 inferred underside closure faces.
The explicit boundary alias repair is `evidence/boundary_alias_response_20260912.json`, request `91c57e0e6be6415c84eb3e76a31d4310`.
It merged 230 coincident aliases through 342 exact source-corner remaps, preserved source positions/weights/UVs and passed save/reopen; maximum native normal direction drift was 0.00534 degrees against 0.25 degrees allowed by the adapter.
The hose patch is `evidence/flexible_hose_patch_response_20260912.json`, request `5179e32ec44147c0a231aa3cdf9fe7e8`.
It added 98 explicitly positioned and weighted vertices and closed one clear four-edge rear-shell pinhole in the same finite patch.
The complete assembly remains below the 30,500-triangle ceiling.

The source height remains 7.3518238068 versus measured vanilla `western_european_infantry.mesh` body height 7.3518247977.
`polySurface106` is the vanilla body; collision `pCube1` is excluded.
Apply vanilla entity scale 0.8 exactly once; effective heights are 5.8814590454 and 5.8814598382.
`evidence/scale_crosswalk.json` is the numeric evidence.

## Exact outstanding topology and contact work

`evidence/positional_nonmanifold_disposition_20260912.json` attributes defects separately.
Before the hose patch, the body had 118 genuine physical boundary edges over 29 regions and 38 same-direction shared edges, with no physical edge having more than two incident faces.
The projector has two four-face positional edges caused by coincident split vertex pairs 128/426 and 296/427 meeting inferred underside-cap center 428.
The adapter winding inspection stopped with `Non-manifold positional edges are ambiguous for orientation repair`, request `2440171d589841feb0a67b4da76a3ebe`.
That global error must not be misreported as a body-only non-manifold diagnosis.
No broad winding reset was applied.

`evidence/boundary_local_reconstruction_proposal_20260912.json` records a bounded local repair proposal, not a Blender result.
Replacing 196 exact torn/inconsistent source faces yields 32 simple consistently directed boundaries comprising 212 edges and zero direction-conflict boundary vertices in the numerical proposal.
Those faces are approximately 0.67 percent of the body.
The proposal must be remapped onto the current checkpoint, each ring closed explicitly and the result visually reviewed.
`evidence/coat_under_projector_reconstruction_20260912.json` records measured opposite-coat surface references for restoring the extraction patch; it is also not applied.

The current projector preview shows a held horizontal object but open/splayed fingers remain an unresolved contact issue.
Complete trigger-hand/support-hand contact, aim/muzzle locators, source-cap repair, hose endpoint continuity, coat/connector clearance and full eight-role deformation/contact checks before export.
The eight distinct role candidates in `evidence/action_candidate_manifest.json` remain unselected for the assembled replacement.
They must not be promoted as aliases or treated as final simply because an earlier body-only export exists.

## Sourced audio

`audio/recovery_20260912/sound_handoff.md` contains exact source pages, authors, license evidence, source/derived paths, proposed destination basenames, sound names/wrappers and action synchronization requirements.
Eight source downloads and fourteen derived WAVs exist with SHA-256 receipts in `source_file_receipts.json` and `derived_manifest.json`.
The CC0 source families are footsteps by GboxMikeFozzy, breathing by primbal, death vocals by Exewin, a real spray recording by Soundkrampf and a body-fall recording by Joseph SARDIN with Kellian F. and Yoann B.
Only trimming, fades, channel averaging, resampling, normalization and PCM encoding were applied.
Every derived candidate is mono 44.1 kHz PCM16 with zero clipped samples.
The spray source is the public HQ MP3 derivative; the login-gated lossless original was not obtained.
The body-fall WAV came through the published public download form after the page playback WAV link returned 404.
No generated or synthesized audio was used.

Perceptual listening remains `needs_user_review` because the tool runtime did not expose audio playback to the model.
Final exact action/sound synchronization remains blocked by final model-action selection.
Selection and acknowledgement have candidate bytes but no verified per-subunit voice consumer; vanilla national infantry voice routing is shared.
No active sound definition or runtime WAV was changed by this worker.

## Bespoke counters

The icon-artist child delivered `counters/replacement_20260912/` with native transparent sources, processing, final DDS, exact vanilla reference comparisons and pixel-exact DDS roundtrip proof.
The parent visually accepted and promoted the large and map strips and committed `cc2176dae`.
`evidence/counter_final_sync_20260912.json` records a fresh worker verification of both source/destination byte matches after that promotion.
Large: `gfx/interface/counters/divisions_large/unit_chaos_battalion_icon.dds`, SHA-256 `B4192708623E1ABE687F11C627E567CD47C5A798B183E7A50544205EF5A9D09F`.
Map: `gfx/interface/counters/divisions_small/onmap_unit_chaos_battalion_icon.dds`, SHA-256 `94890A08E7292F16322B61A27A1FCFD418C59BB5FC1696527CF738F794A916A8`.
The large strip is 152 by 42, two 76 by 42 frames; the map strip is 60 by 12, two 30 by 12 frames.
The large normal frame uses the sampled vanilla green; the white-consumer map normal remains pale.
The alternate schematic state is original art.
Existing registrations `GFX_unit_chaos_battalion_icon_medium` and `GFX_unit_chaos_battalion_icon_medium_white` retain `noOfFrames = 2`.
No further runtime counter edits are required by this worker.

## Dependency and provenance limits

All Blender operations used the lock-selected wrapper/BlenderAdapterClient route.
The last completed mutations used adapter 1.10.45, Blender 5.1.2 build ec6e62d40fa9 and io_pdx_mesh 0.91.0.
`evidence/dependency_verification_adapter_11045_20260912.json` records all 17 source hashes, socket 9876 and fresh wrapper health request `e4ef975fc6de4836b724bd07214436ea`.
The already-exposed direct MCP route was stale at 1.10.44 and was not used for those mutations.
Parent acceptance of the deployed Blender-5.1/Python-3 io_pdx compatibility source set is linked by `evidence/io_pdx_prior_acceptance_check_20260912.json`.
Shared receipt `.tools/3d_pipeline/reports/io_pdx_deployed_source_verification_20260912.json`, SHA-256 `9498FB8E634D53C3E290B4542E19A3AB7888DC672C4C3EB4999618AF78687866`, verifies 37 exact present files and three expected absences.
The upstream locked ZIP remains SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
No shared addon or tool file was changed by this worker.

This is an existing Blender repair: zero Meshy calls and zero estimated/consumed credits during the continuation.
Historical recovered provider lineage is Meshy-6, not Meshy-7; original source-art/reference bytes and original provider PBR history are unavailable and were not invented.
The exact historical task identifiers and reference checksum are in the package manifest.
Standalone Technology Tree Viewer was absent from the scoped registered-app/install-directory inspection; exposed technology MCP routes were not treated as standalone-viewer evidence.

The package remains incomplete, with no authorized scope reduction or concealed simplification.
Model geometry, contacts, eight-role QA, final selected exports/reimport and model/audio copy synchronization are still required.
No assembled model export or active model/audio copy is selected for promotion.
This worker has not made a completion commit for the unfinished 3D repair.

## Intermediate-frame action finding

Read-only parsing of the eight existing candidate `.anim` files exposed intermediate arm rotation failures that were absent at the previously rendered phase frames.
`evidence/candidate_bytes_diagnostic_20260912.json` cross-checks the attack projector bounds against all eight prior native phase-frame measurements within 0.00000136 source units, while other intermediate attack frames produce 1.53 units of support-hand drift and collapse the proposed hose ring radius to 0.014.
Support and training show similar intermediate failures.
`evidence/continuous_role_pose_design_20260912.json` prepares all eight roles with measured arm solutions at every integer frame and stable limb roll, preserving their distinct source body performances.
`evidence/continuous_role_numeric_preflight_20260912.json` records positive adjacent quaternion dot products, support-hand translation drift below 0.00001 and retained hose ring radii near 0.072 and 0.07776 for the proposed poses.
These specifications have not been applied in Blender and are not native action acceptance.
The fresh exact-data body proposal is `evidence/local_body_current_boundary_plan_20260912.json`: 208 local defective faces, 31 simple boundaries and 350 exact alias corner remaps, requiring native landmark comparison before use.
