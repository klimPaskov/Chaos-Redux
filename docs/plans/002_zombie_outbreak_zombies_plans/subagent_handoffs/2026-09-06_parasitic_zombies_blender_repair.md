# Parasitic zombie Blender repair

Disposition: blocked, updated 2026-09-08.
The accepted scope is the existing non-firearm repair recorded in `docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md` and the parent’s explicit four-variant resume assignment.
The job root is `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies`.

The recovered runtime bytes remain immutable; every file in `evidence/runtime_copy_provenance.json` was rehashed successfully on September 8.
The measured 22-bone humanoid source remains `blender/checkpoints/04_measured_rig_v2.blend`; its broad weights still produce stretched strips in the recorded death pose.
Source height is 7.356198310852051, against installed infantry visible height 7.351824797689915 excluding collision geometry; retain entity scale 0.8 exactly once.
See `evidence/vanilla_scale_crosswalk.json` for exact runtime and vanilla paths and hashes.

## Actual work and rejection

`evidence/exact_anatomical_weight_candidates.json` contains 29,891 source-index candidate assignments using the measured skeleton and compact adjacent-joint blending, with no arm-to-leg blending.
The left-arm selection was rendered and visually reviewed: request `db44fc891bdf4f169f0ed398c06e343b`, `blender/previews/component_review_db44fc891bdf4f169f0ed398c06e343b_front.png` and companion views.
It follows the arm and shoulder growth without selecting the neighboring leg; this is partial ownership evidence, not final whole-body weight approval.
The first 20,000-row application through adapter 1.10.27 saved `blender/checkpoints/04_exact_weights_v3_part1.blend` but failed save/reopen fingerprint verification.
That checkpoint is explicitly rejected and must not be a production source.
Request `b6e8317be2e74ecd91bf6e96a37bbd76` and its log under `logs/adapter/` contain the exact failure.
The rejected v3, v4 and v5 attempts remain preserved and cannot be promoted.
The coherent adapter 1.10.31 resolved the preservation defect without bypassing fingerprints.
Requests `87e7c915160d4867933e8bda27e89c06` and `5782733f2829486bac58f12b8af4586f` successfully saved/reopened all 29,891 assignments in `blender/checkpoints/04_exact_weights_v6_part2.blend`.
Actual manual death authoring request `13b890303c5d413f8f2fa3b2d3e787c7` saved `05_exact_v6_death.blend`.
Frame-49 original/clay/culling comparison `b2f24582d4bf497a94f1c35e5477f62c` still fails deformation: large strips connect arms and thighs, and the collapse contact is unsuitable.
`evidence/exact_v6_death_stretch_trace.json` reconstructs skinning from native rest/phase matrices with maximum bone-endpoint discrepancy below 0.000001 source units.
It identifies a maximum 192.30-fold triangle-edge stretch where neighboring source vertices are assigned Hand.R and Thigh.R.
Normalized exact weights therefore do not establish correct anatomical ownership.
Offline source-section and connected-component candidates `exact_section_v7_weight_candidates.json` and `exact_component_v8_weight_candidates.json` remain unapproved and have never been applied to Blender.
Their phase reconstructions still show maximum edge stretches of 215.99 and 47.43 respectively; these numerical failures prevent promotion and require further joint/ownership refinement.

## Connected-surface candidate for native review

`evidence/exact_geodesic_v15_weight_candidates.json` is the selected next review candidate, SHA256 `6bdd6e35eca25045fc228a8923cd33481ff87e62e2fc8212dc134c38bf819efb`.
It contains all 29,891 unique source indices with at most four normalized influences.
`surface_connectivity_probe.json` proves that 0.01-source-unit analytical proximity links reconnect nearly all exported UV patches; 16 remaining tiny islands attach across explicitly recorded gaps no larger than 0.06.
These are analysis links only: no source position, triangle, UV, rig or action was changed.
Reviewed contour guides seed each arm; circumferential torso seeds prevent a one-sided surface shortcut; exact triangle-edge gradient projections preserve continuous joint transitions.
The shared part of left/right thigh influences transfers continuously to their existing Pelvis parent.
`evidence/exact_geodesic_v15_weight_region_audit.json` records exact memberships, bounds and hashes: zero arm/leg influence pairs above 1%, zero opposite-limb pairs above 1%, and zero triangles bridging arm and leg dominant regions.

`evidence/exact_geodesic_v15_weight_native_phase_comparison.json` validates reconstructed bone endpoints against every saved native death phase, then compares candidate skinning with the failed exact-v6 skin without altering keys.
Across frames 1/9/17/25/37/49, candidate maximum edge ratios are 1.178/1.742/2.395/2.671/2.531/2.510; the baseline reaches 197.043.
At frame 25, median/90th/95th/99th/max ratios are 1.005/1.136/1.284/1.629/2.671.
The worst-ratio head/neck edge grows from 0.063295 to 0.169073 source units; the largest absolute extension anywhere is 0.303344.
At frame 49, the five original hand/thigh failure faces are approximately 1.00-fold rather than stretched sheets.
The JSON includes exact worst edges, source/deformed absolute lengths, bone labels, vertex weights, and separate largest-absolute-extension cases.
This is numerical improvement, not native visual approval.
`evidence/exact_geodesic_v15_weight_eight_role_stress_review.json` also evaluates every preserved manual phase design against the saved native rest matrices without authoring or changing a pose.
Maximum edge ratios for idle/move/attack/defend/support_attack/retreat/training/death are 1.206/1.526/2.248/2.091/2.032/1.647/1.769/2.671; all blended skin linear determinants remain positive, with overall minimum 0.1869.
This design-level stress review does not prove that unauthored roles exist in Blender and does not certify silhouette, self-intersection, contacts or surface orientation.

The concrete next operation is two independently scheduled, checksum-bound `edit_explicit_mesh_vertices` batches into new siblings `04_exact_weights_geodesic_v15_part1.blend` and `04_exact_weights_geodesic_v15_part2.blend`, followed by unchanged death authoring and original/clay extreme-phase previews.
The adapter owner released one native slot for the first batch only.
Request `e0f5091386cc40c8b0d44bd8ddc672f5` through coherent adapter 1.10.38 applied exactly 20,000 rows and saved `blender/checkpoints/04_exact_weights_geodesic_v15_part1.blend`, SHA256 `80ED8731C1BD90AD0B07E8D5D5688E44A3BEBC78FCD15FDD3D47D19F1E2B48E1`, independently rehashed.
`evidence/exact_weights_geodesic_v15_part1_receipt.json` records requested-value verification, zero position edits, preserved remaining vertices/UVs/topology/rig/actions/materials and a passed save/reopen proof.
The complete geometry remains 29,891 vertices, 30,000 triangles and 90,000 corners.
The first slot was released after receipt review.
The partial checkpoint mixes revised and prior weights and must never be used as the final skin or export source.
The next released tranche completed the remaining 9,891 rows through request `0292023822f34af29a85973c55d21487`, preserving the full geometry/UV/rig/actions/materials and passing save/reopen verification.
The complete weight source is `blender/checkpoints/04_exact_weights_geodesic_v15_part2.blend`, SHA256 `1D5B5F1D75D7AB108D3D2FACCDFB36C4BA15D6585DF402B4E8106C70F3825248`.
Exact saved death replay `a6b25d5497cb4f289db1ec7045d83b14` saved `blender/checkpoints/05_geodesic_v15_death.blend`, SHA256 `F187EA8D6AFFB7DBC2C041C16A567B93106E1486F38633CA17FB7D776796E7E1`.
`evidence/geodesic_v15_death_exact_replay_proof.json` proves identical complete input specification and phase keys; canonical specification SHA256 is `64c90726bf42c3c21731186ac4d20c1dd90c8af6374ea28f27b39d8a246666a7`.
The unchanged automatic vertical contact policy recalculates ground correction from the revised skin, without authored motion adjustment.
Native frame-25 original/clay front/three-quarter comparison `f478b510fa5b406b8acad54854c9ba4f` under `blender/previews/qa_05_geodesic_v15_death_025_*` visibly removes the long arm-to-leg sheets.
This is one-phase native ownership evidence, not complete skin/action approval.
The separate death-pose defect is exposed clearly: the impact pose suspends torso and legs on the hands/forearms.
Exact support reconstruction records torso minimum height 0.820, left/right knee minima 0.457/0.743, and left/right foot minima 0.348/0.853 while only left hand/forearm vertices lie within 0.04 source units of the ground.
The death action remains rejected for contact and semantic impact; source surface gaps are unresolved.
The parent accepted preserving the v15 weight source and requested data-only articulated impact/settle correction using actual support vertices, with no root-only lowering.
The selected correction design is `evidence/action_specs_contact_v19/death.json`; earlier v16/v17/v18 contact studies are superseded by this candidate and remain non-production evidence.
`evidence/death_contact_v19_support_review.json` records actual indexed skin contacts for impact/settle/still, including source positions, deformed positions, weights and projected support hull vertices.
Frames 1/9/17 retain their original collapse keys; frames 25/37/49 articulate shoulders, elbows, wrists, torso, head, hips, knees and ankles while preserving the complete v15 skin.
`evidence/death_contact_v19_interpolated_support_review.json` evaluates every integer frame 25–49 using the adapter's linear quaternion-channel interpolation and unchanged ground policy.
Torso, left forearm and right knee support persist within the 0.04-source-unit band throughout those 25 frames; the left foot joins at frames 48–49.
Torso minimum height ranges from 0.0025 to 0.0327 instead of the rejected pose's 0.820–0.955; projected support hull area ranges from 0.728 to 8.923 square source units.
These hull measurements describe geometric support extent and do not claim physical mass/stability simulation.
Corrected key-phase edge stretch remains no greater than 2.901-fold with unchanged weights.
V19 has not been authored in Blender; native impact and settle views, contact persistence, silhouette and self-intersection review remain required before accepting the death role.
The actual attack/death extreme poses, silhouette, source-region highlights and contact must pass review before any export.

## Independent surface defect

Neutral rig previews with culling enabled already show the missing-looking patches, independently of action deformation.
Disabling culling exposes back surfaces and is not evidence that flipping faces is correct.
`evidence/seam_orientation_diagnosis.json` spatially matches edges at six and five decimal places and finds 31,644 paired edges with zero conflicting orientations and 26,712 unpaired edges.
An isolated 17-face source shell passed full local ray-parity checks and was flipped only in the diagnostic sibling `blender/checkpoints/04_surface17_probe.blend`, request `9f92c49341284206a8fd0160d9166026`.
Its save/reopen evidence preserves positions, UV corners, weights, actions and materials; it is not incorporated into the v6 skin branch.
Neutral comparison `56ff1370aa2944bdac16e5706450a01a` does not establish an overall surface fix.
No blanket flips, caps, topology deletion, or two-sided runtime override were applied.
Surface repair remains unresolved.

## Required roles and promotion

All eight final roles remain blocked: idle, move, attack, defend, support_attack, retreat, training, death.
Eight explicit phase designs exist under `evidence/action_specs`; the actual v6 death candidate and historical attack/death checkpoints failed deformation review.
There is no accepted final mesh, animation export, reimport proof, runtime copy manifest, or revised sound timing.
Existing role bytes remain preserved.

Blender 5.1.2 build `ec6e62d40fa9` and loaded io_pdx_mesh 0.91.0 exporters were verified; socket 9876 was listening.
Each wrapper mutation has its own dependency hash receipt; successful v6 exact edits used the coherent 1.10.31 lock.
No Meshy operation, source-art generation, or paid call occurred; estimated and consumed credits are zero.
Existing counter DDS hashes, exact consumers, installed vanilla references, palette evidence, shared audio hashes and inherited audio provenance gaps remain in `evidence/inherited_companions.json`.
Specialized archived audio originals remain missing; no replacement audio or counters were created.

The parent owns source acceptance, runtime copies, entity/GFX/animation/sound wiring and commits.
No completion or live-game claim is made; omissions are the unresolved surface repair and anatomical weighting, full action production/QA, export/reimport, final synchronization, and inherited companion provenance gaps.
Skills applied: chaos-redux-3d-model-pipeline, chaos-redux-event-assets, chaos-redux-subagents; none modified.
