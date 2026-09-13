# Undead zombie geometry and actions, 12 September 2026

Disposition: in progress; runtime selection and exports remain blocked by unresolved surface, skin, and contact defects.
Parent authorization covers direct Blender repair of the existing non-firearm `002_zombie_outbreak/undead_zombies` identity, with no Meshy generation, source substitution, or paid recovery.
The worker owns only this model job outside `counters/` and `sound/`, plus this handoff.
Runtime definitions, companion production, shared dependencies, and commits remain parent-owned.

## Current verified source and route

Immutable runtime recovery remains under `refs/recovered_runtime/`, with exact copy lineage in `evidence/repair_2026-09-06/source_copy_provenance.json`.
Historical artwork, original provider tasks, and original texture-generation provenance remain unavailable and were not invented.
Estimated and consumed provider credits for this tranche are zero.
No provider operation was performed.

The reviewed rest source is `blender/checkpoints/repair_2026-09-06_measured_rig_v2.blend`, SHA-256 `578BEC412D72054C08A2C437683B839558ECBDE009CF9232DEAD962996D0E4B6`.
The saved chest/calf/knee trial is `blender/checkpoints/repair_2026-09-08_chest_calf_knee_trial32.blend`, SHA-256 `0D2FD7EC948E5B16E0D08EE8A14FB5D9C63386D024741F2CD650FD6474B417A5`.
The parent explicitly imposed a mutation/export hold during publication of adapter 1.10.45 and then explicitly released it on September 12.
No Blender call was made by this worker during that hold.
Fresh wrapper schema, locked source hashes, separate TCP bridge probe, and native health passed after release in `evidence/repair_2026-09-12/route_verification_1.10.45.json`, `live_tools_1.10.45.json`, and `health_1.10.45.json`.
Native health request `3c056efeaa974cc58320fb0a9e81d58e` confirms adapter 1.10.45 and Blender 5.1.2.
After that release, the worker's source guard detected a changed `skeletal_export_partition.py` before the next native call.
The parent confirmed a new global hold covering adapter 1.10.46 maintenance and then continued the hold into 1.10.47 batch-variant work.
No native call has been made during this subsequent hold.
The parent subsequently released coherent adapter 1.10.47 with config SHA-256 `7E132374548AB958B46EA2F15517E2653DB222627AB7869E8260CAEAC45BF5DF`, dependency-lock SHA-256 `4BCB145321C06B527C70E6BE06F9745D5C7C0B43D2152DA43CAC2D880AF22547`, and release receipt SHA-256 `746CEFF7A94F190EA71E19B1F8A2A1170EAE36E623163961EDEC4A9D32C72678`.
This worker rechecked those bytes, all 18 locked adapter sources, and TCP `127.0.0.1:9876` successfully.
Fresh official-wrapper `tools/list` then failed three times with no JSON-RPC response, exit 0, and `ListToolsRequest` on stderr; the parent independently reproduced the same failure and paused dependent calls pending fresh schema evidence or shared transport resolution.
`evidence/repair_2026-09-12/schema_transport_failure_1.10.47.json` records those failed discovery attempts.
The parent then supplied a successful fresh sibling schema receipt, SHA-256 `90054E6AF95754CFF3A017EAE4A09B1402360DFE8F4C8501519F9553AB250DB7`, which was independently rehashed and copied exactly to `live_tools_1.10.47.json`.
Fresh own health request `a80c5e5285a445c4b9020c1883d6dbde` and three source-explicit read-only selection previews returned adapter 1.10.47 successfully.
The parent subsequently reinstated a global transport hold after reproducing an intermittent EOF/async response race.
The final outstanding read-only request `63f29cb696eb439ab219c13895522377` completed successfully and was drained; the source checkpoint hash remained exactly `B8BDA2273F5EFC27DC17F66C6B18EE7096DA61EB0070B02905273AFD4643D258`.
No native mutation, new checkpoint, or export was performed under 1.10.47, and no Blender call remains outstanding.

`evidence/repair_2026-09-12/io_pdx_current_bytes_verification.json` independently rehashes the accepted deployed io_pdx_mesh set against `.tools/3d_pipeline/reports/io_pdx_deployed_source_verification_20260912.json`.
The report checksum is the expected `9498FB8E634D53C3E290B4542E19A3AB7888DC672C4C3EB4999618AF78687866`.
All 37 present files and three expected absences match, with zero mismatches.
The accepted deployed modernization is io_pdx_mesh 0.91.0 under the parent-reviewed September 6 alien-infantry reconciliation; it is not claimed to be byte-identical to the original release archive.
Blender lock selection and native worker output agree on 5.1.2, build `ec6e62d40fa9`.

The calibration remains installed `gfx/models/units/western_european_infantry.mesh`, visible object `polySurface106` with collision `pCube1` excluded, and `gfx/entities/units_infantry.asset` / `infantry_rifle_entity`.
The source height is 7.346600770950317, vanilla source height 7.351824797689915, ratio 0.9992894244784997, and entity scale 0.8 is applied exactly once.
The source geometry remains 30,000 triangles and 28,444 vertices; axes remain +Z up and -Y forward.

## Surface review and bounded candidates

The parent-created adapter 1.10.44 paired review request `696bf8b4375146d489138ef5615f2aa3` is retained under `logs/adapter/`.
This worker reviewed all front/rear/left clay culling pairs plus the original-material front preview under `blender/previews/repair_2026-09-12_calf_knee_review_*`.
The 139-face chest and 280-face calf/knee repairs improve their named surfaces, but shoulders, skull, sleeve/cuff, ankle, and rear-shoulder gaps remain visible.
The combined trial is not accepted as final geometry.

`analyze_saved_panels.py` reads only the immutable adapter-emitted `evidence/repair_2026-09-08/rest_landmarks.json` and produces `source_connected_panels.json`.
It finds 816 complete source-index-connected panels and records face indices, source bounds, area, geometric and stored-normal comparisons, and anatomical-axis diagnostics.
These are numerical diagnostics, not accepted selections or Blender mutations.

`analyze_panel_occlusion.py` adds double-sided triangle-ray evidence for explicitly named candidates in `explicit_panel_ray_diagnostics.json`.
The large shoulder panel `c_v17758` contains 234 triangles and has 99.97% reverse-exterior ray evidence.
The posterior neck/shoulder panel `c_v15845` contains 125 triangles and has 99.39% reverse-exterior evidence.
Both correspond to visible rest-pose culling gaps and are the next bounded native group-review candidates.
Native exact-index rest preview `419e5ded981d43c29b337be012b353cf` subsequently highlighted all 359 shoulder/rear-neck triangles, with 304 selected vertices and zero mixed faces, through `preview_explicit_skin_selection`.
The worker viewed its front, right, and three-quarter evidence and confirmed the outer shoulder and rear-neck surface identity.
No winding repair was applied before the subsequent global hold.
Skull crown panels `c_v10942`, `c_v13767`, and `c_v13885` retain their individual evidence and require native review before any trial.

The earlier apparent outer-jacket candidate `c_v2291` is deliberately excluded from winding trials: only 0.056% of its area has unobstructed rays along the proposed reverse-normal direction.
Further anatomy calculations identify an inner right sleeve/forearm hypothesis: its normals align 0.952 with the local arm radial direction and -0.818 with the torso radial direction, and its mean distance to the arm axis is 0.305 versus 0.732 to the torso axis.
Its local surface identity still needs native exact-index review before weight repair.
An inward radial score alone does not establish reversed exterior winding.
No blanket flip, weld, cap, geometry omission, or material-culling workaround was performed.
`remaining_panel_ray_diagnostics.json` inspects 73 additional explicitly named connected panels; twenty have more than 80% exterior-reversal evidence and remain native-review candidates.
Interior sleeve/cuff and jacket candidates are retained individually, including rejected orientation hypotheses.

## Skin and action findings

All eight selected current specs use 24 FPS, including idle V2, move V2, attack V2, defend V3, support_attack V2, retreat V2, training V2, and death V3.
Their exact source-spec hashes, action names, ranges, loop flags, phases, and frame-to-second mappings are in `evidence/repair_2026-09-12/candidate_phase_timings.json`.
These timing rows are provisional until native phase/contact review accepts the corresponding selected clips.

`analyze_saved_actions.py` reconstructs linear skinning from the saved adapter rest matrices, actual vertex weights, and exact manual key specifications without Blender mutation.
The predicted phase bounds match the existing native receipts within 0.00000117 source units across all roles.
`saved_action_support_predictions.json` retains per-frame clearance predictions and per-phase dominant-bone support, bounds, longest-edge strain, and native comparison error.
This is strong diagnostic evidence, but it does not replace native visual or actual-byte reimport review.

One explicit defective connected edge is source vertices 2574–2720.
Vertex 2574 at `[-0.7665746212, 0.4468325078, 4.2419509888]` follows RightForeArm at 0.8892467022, RightArm at 0.0658659562, and RightHand at 0.0448873490.
Its adjacent vertex 2720 at `[-0.7454064488, 0.4423926771, 4.2675065994]` follows Spine02 at 0.4239242077, Hips at 0.4057163894, and Spine01 at 0.1703593880.
The abrupt arm/trunk boundary stretches this short connected edge roughly fiftyfold in grasp, guard, support, and impact phases.
Native component review must establish the intended local surface assignment before applying explicit smoothly blended weights.
The lower-elbow defend V3 pose alone does not clear this skin defect.
`arm_trunk_discontinuity_panels.json` records 21 connected sleeve/torso panels crossing the original hard weight boundary.
`skin_weight_data_candidate.json` contains 8,087 exact draft replacements, preserving original expected weights, for those panels and the diagnosed shoulder, neck/skull, pelvis, and waist interfaces.
The current numerical phase audit in `skin_weight_data_deformation_prediction.json` reduces the largest tested rest-edge ratios to about 1.38 idle, 1.50 move, 2.46 attack, 2.25 defend, 2.89 support attack, 1.57 retreat, 1.90 training, and 3.90 on the still-unrepaired Death V3 poses.
These figures locate remaining deformation risk; they are not semantic, native visual, or export acceptance.
All skin replacements remain unapplied and need native selection and posed comparison evidence.
`native_selection_review_1.10.47.json` records the subsequently viewed front/right/three-quarter native highlights for the sleeve strips, sewn shoulder interfaces, and shoulder/neck/lower-head transition.
Those nine images support the named local anatomical assignments for a weight trial; they do not establish final posed deformation or winding acceptance.
The pelvis/waist, isolated inner-sleeve seam, and skull-crown reviews remain unrun because of the reinstated transport hold.

Death V3 frame 85 is not anatomically grounded.
Its Head-weighted vertex 13744 alone sets the 0.001 minimum; Hips support remains about 0.208, hands about 0.808/0.827, and feet about 0.687/0.694 source units above the fixed floor.
The terminal pose requires coordinated articulated torso, head, arm, leg, and foot settling; whole-body lowering cannot satisfy this requirement.
No final death pose, phase set, mesh export, animation export, or reimport was accepted during this tranche.
`source_spec_quaternion_continuity.json` finds two negative quaternion pairs in Death V3, both lower legs between frames 26 and 39; the other seven selected source specs have none.
`prepare_death_supported_candidate.py` preserves the original phase-key orientations through frame 39 while correcting those two interpolation hemispheres, then authors explicit world joint trajectories, continuous signed knee extension, descending torso support, and an articulated impact response.
Its `action_spec_death_supported_v4_data_candidate.json` is designed against the exact pending weight draft, keeps 24 FPS and the original semantic phase frames, and remains data-only.
The current terminal prediction has hips near 0.020, head 0.026, hands 0.012/0.028, calves 0.013/0.009, and feet 0.039/0.027 source units above the fixed floor.
The supported ending requires native full-phase and intermediate-frame review; the original fall's anatomical motion also remains subject to that review.
`data_draft_rejections.json` records rejected terminal-only, rotation-interpolation, knee-pole, and weight-boundary drafts and the reasons they were not promoted.

## Remaining work

The static component-review route rejects this rigged checkpoint, and the original rest rig has no active action binding for the detailed region inspector.
Both read-only rejections are retained in adapter requests `19d99679561b4f7f9564b170b3e4091c` and `57d46b7d898844ff8a033a0a0cbd57c4`.
The separate `blender/checkpoints/repair_2026-09-12_idle_panel_review_v4.blend` preserves the combined repaired geometry and uses the exact existing idle V2 keys at 24 FPS under a review-specific action name.
Its SHA-256 is `B8BDA2273F5EFC27DC17F66C6B18EE7096DA61EB0070B02905273AFD4643D258`, with native action hash `E8DAABF70610D1A3995B0727E86704D6B39937DD7EC96F28EDB8E0EE11D551AF`.
The source-index topology hash obtained by native region inspection is `5E7C7C1DFB828367D955C95B1962F7C9AD3FD3D6A13E4D52BC4151B4B685515C`.
Authoring request `a6d21cfed3fb479daa0259258b61cf85` and native region inspection `9d06449770d6428f96ab86247c90e2a1` establish a valid inspection context without stripping the source rig.
The read-only explicit skin-selection preview supports this rigged source and is used to highlight reviewed source-index panels in rest geometry.
Repair only reviewed explicit selections in new sibling checkpoints, preserving normals, UVs, weights outside selected repairs, skeleton, and immutable sources.
Complete the culling, full-body material, local weight, and anatomical support review before generating final mesh/action candidates.
Every required role still needs complete native phase/loop/contact/deformation evidence, export, actual-byte reimport, and a selected final hash.
Any weight or geometry repair must propagate through the selected action checkpoints and invalidate their earlier deformation acceptance.
The current action crosswalk is `evidence/repair_2026-09-12/candidate_action_crosswalk.json`; all eight original checkpoint hashes were rechecked and remain intact.
Prepared source-index native review requests are `skin_sleeves_selection_request.json` (478 vertices), `sewn_shoulder_interface_selection_request.json` (970), `shoulder_neck_skull_interfaces_selection_request.json` (2,337), and `central_pelvis_bridge_and_waist_interfaces_selection_request.json` (4,302), all under the September 12 evidence folder.
The current native sender is guarded by the accepted 1.10.47 version and exact config/lock hashes and has the parent-supplied verified fresh schema receipt.
It must remain paused until the parent explicitly releases the transport hold and supplies any revised coherent route guards.

Companion audio and counter workers own their respective folders.
This worker supplies exact accepted animation synchronization timings once the clips pass review.
The parent explicitly confirmed on September 12 that `armored_undead_zombies` is an existing shared-model consumer of sprite `chaosx_undead_zombies` and the same entity as `undead_zombies`.
Both consumers retain the same calibrated source geometry, single entity scale of 0.8, skeleton, and eight action roles; this confirmation does not introduce a separate armored model or rig scope.
The companion icon worker audits the distinct `armored_undead_zombies` large and map counter pair.
The parent owns final model path `gfx/models/units/chaosx_undead_zombies`, `chaosx_undead_zombies` mesh/action stems, proposed `undead_zombies_entity` binding verification, active runtime copies, GFX/entity/sound wiring, and source-to-runtime hash synchronization.
No live game was launched and no in-game completion is claimed.

Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, and `chaos-redux-subagents`.
No skill or shared tool was modified, no commit was created, and no simplification was accepted.
