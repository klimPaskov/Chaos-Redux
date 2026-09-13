# Stone cohorts Blender repair handoff

Status: in progress; no repaired asset is accepted or copied to runtime.
Accepted scope is `docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md` and the parent instruction to preserve the current dark ornate ember-lit guardian.
The pale legacy model is not selected.
The repair uses GPT-6-astra through the repository Blender adapter; provider calls and repair credits are zero.

Source, reference authorization, provider lineage, vanilla calibration, companions and runtime consumers are recorded in `docs/assets/012_africa/models_3d/stone_cohorts/manifest_blender_repair_20260906.md`.
Current source height remains 11.275205 with entity scale 1.0.
The historical V2 assembly had 23,799 body plus 876 polearm triangles; the repaired assembly has 23,800 body plus 876 polearm triangles, totaling 24,676 with the same 27-bone measured rig.
Five distinct V2 semantic actions exist in checkpoint `34_death_v2_blender_repair_20260906.blend`.

## Resume implementation

Health request `68c11995ba5f4ce5831128bec8441e61` verified Blender 5.1.2, loaded io_pdx_mesh and mesh/animation exporters under coherent adapter 1.10.25.
Evidence is `evidence/blender_repair_20260906/resume_health_20260908.json`; the live structured schema is `resume_schema_20260908.json` in that directory.
Per-call dependency and separate socket receipts are retained as `lock_receipt_*.json`.

V3 collapse/recovery checkpoint `40_collapse_recovery_v3_blender_repair_20260906.blend` has SHA-256 `9BAF90369A28E618256CF139230938148D2EA8AF446D1FD103465EDE03459F17`, request `9f6eda62308040088b790505ab61b88b`.
V3 death checkpoint `41_death_v3_blender_repair_20260906.blend` has SHA-256 `ACB447EB875CDF798F11FB58F9CC0CFCB61A9246ECF0CBD33E566FD784BC0D65`, request `8d3e3512241d49d7a93f5e615f6f52a5`.
Both preserve editable keys and use 30 FPS, in-place motion with vertical contact correction.
The death revision rolls the polearm 90 degrees, and the frame-79 preview confirms the blade is flat.
That preview still shows excessive body clearance; the death is not accepted.
A V4 declarative authoring script raises the final gripping wrist relative to the body to remove the polearm as the sole lowest support.
Its attempt failed before checkpoint save with `Empty-path image requires local loaded FILE/GENERATED pixels` in the adapter fingerprint, request `071cdd9b7bf24b218874c4acfaee3f48`.
The adapter owner has the exact receipt and is resolving the empty image preservation contract; no successful V4 checkpoint is claimed.
V3 frames 21/43/79 for death and 25/39 for collapse/recovery exist; the remaining render stopped at a shared checksum mismatch.

## Implemented source topology repair

`evidence/blender_repair_20260906/local_topology_reconstruction_candidate.json` is a proposal based on immutable source checkpoint 00 and hash-bound component report `blender/reports/component_review_a01aae91d0534af49fbb5e0a80978f89.json`.
It targets 835 source faces (3.34 percent), 83 boundary loops and 722 replacement triangles, predicting 24,886 body triangles before the required prop budget reduction.
The orientation solution applies 18,863 exact face reversals derived from connected edge constraints and component signed volume, not a blanket flip.
The source guarded 64-loop plus 19-loop patch completed with second-stage vertex indices translated from the first-stage preservation receipt.
Final repaired source `blender/checkpoints/04_local_patch_resume_20260908.blend` has SHA-256 `9BD45037B602185CC82B0ED6383E2265794800818F1117E9056D86286BD9602F`.
Its 24,886 triangles have zero boundary edges, non-manifold edges, degenerate faces, orientation conflicts or requested orientation reversals in both exact-position and source-index diagnostics.
All original bounds are preserved, and front/rear/three-quarter previews retain the selected dark ornate guardian and amber details.
Evidence is `04_patch_visual_resume_20260908.json` and `04_patch_winding_resume_20260908.json` in the repair evidence directory.
Requests are `c8f62b26c78b463ba8d0187cda048e0c` for winding, `066e2bc94054449faea00117b0a9ba07` for the first patch and `90335577811242b089f4321539f83c0b` for the second patch.

The measured-rig rebuild applies the approved 23,800-triangle body target to reserve room for the required 876-triangle polearm.
Checkpoint `50_repaired_measured_rig_resume_20260908.blend`, SHA-256 `EB0D60DEA7E667BF42F80B45ED156B9639D63A846553C76A0AFA73E9A9E5C983`, has exactly 23,800 body triangles with zero boundary/non-manifold/degenerate findings.
Dedicated PDX polearm checkpoint `51c_repaired_polearm_resume_20260908.blend`, SHA-256 `0F148E9DBC93BE2AEEC785BAAF47FF616194976E0271AE0B42D03E66B5F4637B`, passed source-preservation and save/reopen proof under adapter 1.10.31.
Earlier attachment checkpoints 51 and 51b failed stale-bound preservation checks and are retained as rejected evidence.
The original polearm UV design and dedicated material slot remain intact; parent confirms that shared underlying body-map bytes are allowed for the intentional dark stone/metal and amber grip regions.
All five action roles rebuilt on the repaired assembly, and checkpoint 57 completed the body PDX material binding while preserving the dedicated polearm slot.
Checkpoint 58, SHA-256 `F0BA248D35E5DFD1573240E6B48F7A8F808E09E2DEC25E39845E48FB810BDA4C`, contains death contact V5 with the polearm blade rolled flat.
The final death preview still shows excessive torso clearance; this action is not accepted.
Renderer source places its floor at the evaluated geometry minimum, so this clearance must be resolved in the pose rather than dismissed as a floor-placement issue.
Actual idle and move animation files exported successfully under adapter 1.10.32; their hash-bound receipts are `export_idle_result_resume_20260908.json` and `export_move_result_resume_20260908.json`.
Mesh export request `cb8b16f2204d436992ed89e839e479fb` wrote diagnostic bytes but failed the conservative 65,535 triangle-index-entry batch gate: the body stream contains 71,400 entries for 23,800 triangles.
The next mesh operation is the discovered `partition_skeletal_mesh_export_batches`, which changes only identical material copies and polygon material assignments, preserving the assembled geometry, weights and actions.
No mesh export, reimport or runtime promotion is accepted.
New Blender calls are paused under the parent resource hold; idle and move success receipts are preserved and the export runner checks an explicit hold file before any additional call.

## Remaining work

Continue on the coherent published adapter lock, checking every call; the fingerprint and stale attachment-bound blockers were repaired by the shared adapter owner.
Complete final death/contact/deformation review, then recheck the assembled reduced topology, material appearance and visual silhouette.
Export the assembled mesh and all five required actions, reimport actual bytes and record source-to-runtime copy hashes for parent selection.
Retain inherited audio/counter issues in the existing companion audit and hand off accepted action synchronization times.
The parent owns runtime copy/promotion, entity/GFX/sound bindings and commit.
No required components or roles have been omitted from scope; the package remains incomplete.

## Bounded contact tranche under adapter 1.10.33

Read-only request `1210755cb3aa44389cc216c372f807e6` identified twelve right-toe vertices as the final lowest support in V5.
V6 extends both feet rearward in prone impact/settle phases while preserving earlier collapse keys, grip and the flat polearm.
Checkpoint `61_death_contact_v6_resume_20260908.blend`, SHA-256 `8F15065B69CDD3947ECC81B844D472AC9C4E83D840179AAC781653616E59E726`, passed save/reopen proof, request `965457b8d7cc4bb89dbb21e5cb06c538`.
Final contact request `80c2c3289c0b448883adeb98cbf239aa` found nine pelvis-weighted body vertices within z=0.001–0.059; the toes no longer determine the ground correction.
Quarter/right preview request `a08909875fb7421581d57885f087d728` saved `stone_death_v6_f79_resume_20260908_*.png`.
Numerical contact is improved, but standard-frame previews are dark and small; closer visual and multi-phase acceptance remain required.
One attempted combined region/render request `38cfffc7639f4611a2f3102fc083a540` was rejected because mesh-region queries are read-only without rendering; subsequent separate calls passed.
The next partition draft targets checkpoint 61, with a conservative 60,000-entry batch budget and no geometry changes.

## Focused parent review

The two focused 1024-pixel corpse/polearm preview requests completed under adapter 1.10.37 with unchanged materials: `ff6935f6078f450cbe8a9221dc9e54e0` and `c12192f27f0d49b2b8e63a229c0a9713`.
The parent reviewed the focused corpse right view and rejected V6 because the head/chest and both ends remain visibly elevated despite numerical pelvis contact.
The parent directed continued forward settle and required spine/limb articulation, preserving weapon world orientation and thick armor contact surfaces, without additional approval.
`63_death_v7_request_draft_resume_20260908.json` and `63_death_v7_pose_solve_draft_resume_20260908.json` contain a finite unexecuted candidate: forward spine/head settle, lowered rearward feet through unclamped IK, lowered gripping wrist with a flat weapon, and laterally braced elbows.
The shared Blender slot was released after the two focused previews; no V7 call has been made.
Final evidence must distinguish the renderer plane, actual lowest body and weapon values, and visible head/torso/pelvis/limb contact; a scalar minimum alone is insufficient.
