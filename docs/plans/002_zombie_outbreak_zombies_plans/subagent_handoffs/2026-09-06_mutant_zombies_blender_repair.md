# Mutant zombie Blender repair

Disposition: blocked, updated 2026-09-08.
Accepted scope and dependency rules are `docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md` and the parent’s four-variant resume assignment.
Job root: `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies`.
All recovered source files were rehashed against `evidence/runtime_copy_provenance.json` successfully; no runtime copy changed.

The measured source is `blender/checkpoints/04_measured_rig_v2.blend`.
The existing overhead attack still shows stretched strips, so its weights/actions are not approved.
`evidence/exact_anatomical_weight_candidates.json` contains 25,774 exact source-index candidates with adjacent-joint-only blending.
Request `b2b8b870598245df89dd171c02f8ac1f` inspected topology `79FF70E0E3B5D4DABFDA074A72C56FF41BE0661DEFDC10D75341F9B5EDF17F8F`.
Request `9cf3af233e134dfeaf8d88c5cc794a7c` produced the left-arm ownership views under `blender/previews/component_review_9cf3af233e134dfeaf8d88c5cc794a7c_*`.
The front selection follows the long arm and excludes the adjacent leg, with the torso junction still requiring deformed review.
After the adapter preservation repair, requests `94cca89a711c4a64a2930df1298be725` and `581755b19c5548f390f26eedfddeb242` saved/reopened all exact assignments in `blender/checkpoints/04_exact_weights_v6_part2.blend` under coherent adapter 1.10.31.
Manual attack authoring `dd3574537459429f835954cd773d72b9` saved `05_exact_v6_attack.blend`.
Frame-17 comparison `eb0b98b1d2594f5ba194c3f3b47bf465` was visually reviewed and fails: long sheets extend from the raised arm toward the thigh even with clay culling disabled.
The exact skin and attack remain rejected for production despite passing preservation checks.

`evidence/exact_geodesic_v15_weight_candidates.json` is the next native-review candidate, SHA256 `c281650115b0aac3b9032f44683dd838d98e1e1bff79b5d34867c1a07fda45bd`.
All 25,774 indices are unique, with at most four normalized influences.
Analytical links across 0.01-source-unit UV-seam gaps connect the complete saved surface without welding or modifying any mesh.
Exact source cross-sections in `measured_joint_sections.json` guide arm seeds, including the right hand's positive depth offset that the old centerline missed.
Connected surface distances establish ownership; local triangle-edge gradient projections smooth joint transitions; shared left/right thigh influence transfers continuously to the existing Pelvis parent.
`exact_geodesic_v15_weight_region_audit.json` reports zero arm/leg pairs above 1%, zero opposite-limb pairs above 1%, and zero triangles with arm/leg dominant-region bridges, with exact region indices and bounds retained for native highlights.
`exact_geodesic_v15_weight_native_phase_comparison.json` verifies reconstructed bone endpoints against every unchanged saved native attack phase.
Candidate maximum edge ratios for frames 1/9/17/22/27/39/53 are 1.174/2.422/2.911/2.604/1.940/2.030/1.174; the failed v6 baseline reaches 928.476.
At frame 17, median/90th/95th/99th/max ratios are 1.008/1.177/1.401/1.901/2.911.
The worst-ratio neck edge grows from 0.008840 to 0.025736 source units; the largest absolute extension anywhere is 0.243389.
The JSON separates worst ratios from largest absolute extensions and records exact source/deformed lengths, anatomical bone labels and weights.
No action key, rest joint, geometry or material changed in this data-only work.
`exact_geodesic_v15_weight_eight_role_stress_review.json` evaluates all preserved manual phase designs against saved native rest matrices, with maximum edge ratios for idle/move/attack/defend/support_attack/retreat/training/death of 1.270/1.492/2.911/2.711/2.495/2.353/2.764/2.865.
Every blended skin linear determinant remains positive; the overall minimum is 0.1225.
These are data-only design checks, not proof of native authoring, contact, silhouette, self-intersection or surface-orientation acceptance.
V15 remains a candidate requiring two checksum-bound native weight batches, unchanged attack/death extreme-phase previews, region/silhouette review and contact QA after the resource slot is released.

The independent neutral surface gaps remain unresolved.
Spatial seam analysis found 34,503 matched geometric edges without orientation conflicts at six/five decimal precision and 20,994 unpaired edges.
The lone conflict after coarse four-decimal rounding is insufficient winding evidence.
No blanket flips, caps, topology reduction, or two-sided runtime override was used.

All eight final roles remain blocked: idle, move, attack, defend, support_attack, retreat, training, death.
Eight candidate phase designs exist in `evidence/action_specs`; actual authored attack checkpoints are unapproved and other roles have no accepted production checkpoint.
No final mesh/animation export or reimport was attempted while geometry and weights remain unapproved.
Keep measured scale unchanged, with exact installed infantry comparison in `evidence/vanilla_scale_crosswalk.json` and runtime entity scale 0.8 applied once.
Existing counters and audio were preserved; `evidence/inherited_companions.json` records exact paths, tokens, hashes, vanilla palette/reference evidence, and missing specialized original audio/provenance.
Final role-to-sound synchronization and parent-owned runtime copy manifest are absent because no action is accepted.

Blender 5.1.2 and checksum-locked io_pdx_mesh 0.91.0 are the production route; fresh wrapper receipts verify each selected lock.
Provider operations and credits estimated/consumed: zero.
No final source-to-runtime synchronization occurred.
The parent owns runtime wiring, acceptance and commits.
This package is incomplete; the unresolved surface/weight defects, eight roles, export/reimport and inherited companion provenance are explicit omissions.
Skills applied: chaos-redux-3d-model-pipeline, chaos-redux-event-assets, chaos-redux-subagents; none modified.
