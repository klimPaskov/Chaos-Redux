# Necrotic zombie Blender repair

Disposition: blocked, updated 2026-09-08.
Accepted scope is the existing non-firearm repair plan `docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md` and parent’s four-variant resume assignment.
Job root: `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies`.
Recovered runtime sources were rehashed against `evidence/runtime_copy_provenance.json`; all remain unchanged.

`blender/checkpoints/04_measured_rig_v2.blend` retains measured joints but unapproved broad weights.
`evidence/exact_anatomical_weight_candidates.json` contains 25,481 exact source-index adjacent-joint candidates, not an accepted skin.
Topology inspection request `a2d2666ec9664370ba5a4ab735237981` returned `54BEDE09BB6E32C1EFDEDDEDB60A06CA88C6F4C759679B5BB8F7B4F64BB6D1EE`.
Exact left-arm ownership preview `27dcc4289f104c6ea9d27c4640431882` exposes residual torso-side selection beside the low hands in its front/right views.
Nearest measured segment selection therefore remains insufficient for this anatomy.
Do not apply the candidate merely because its indices are exact or its weights normalized.
Exact source triangle-plane sections in `evidence/measured_joint_sections.json` established that the source arms and legs occupy diagonal depth offsets that the old rig did not follow.
`evidence/measured_rig_spec_depth_v3.json` and `depth_v3_design_basis.json` record corrected measured joints without rotating source geometry.
Request `68c34b3f62894555b4af4176480cdb2b` authored `blender/checkpoints/04_measured_depth_v3.blend`.
The revised left-arm selection `1c3d1d703e0c48ab9426e8e1fdc4a82f` removes the broad torso selection in the reviewed front view; a thin boundary still needs deformation review.
Requests `20e0845e29fc4df38ff8208721ed39e6` and `4dc11e04f02c458e83a2e63d6a4ac882` saved/reopened exact corrected assignments into `blender/checkpoints/04_exact_weights_depth_v3_part2.blend`.
Actual rest axes inventory `evidence/depth_v3_rig_axes.json`, request `f8c0f38274014992804dee7aa67cbfa3`, supports anatomical-axis action authoring.
Eight corrected-axis declarative candidates exist in `evidence/action_specs_depth_v3`, serialized by `evidence/prepare_depth_axis_actions.py` from the preserved phase semantics and actual rest matrices.
The maximum matrix reconstruction discrepancy is 0.000012; this numerical check does not establish visual contact or deformation quality.
These are reviewable working candidates; no corrected-rig action has passed deformation/contact review.

Surface visibility is independently unresolved in neutral poses.
`evidence/seam_orientation_diagnosis.json` finds 34,868 matched geometric edges, zero orientation conflicts and 20,264 unpaired edges at six/five decimal precision.
No face flip, cap, deletion or two-sided material override was applied.

All eight final roles remain blocked: idle, move, attack, defend, support_attack, retreat, training, death.
Eight phase design JSONs exist, but only an old measured attack candidate was actually authored and no role has accepted deformation/contact evidence.
No final export/reimport or source-to-runtime synchronization exists.
Preserve source size and entity scale 0.8 exactly once, using `evidence/vanilla_scale_crosswalk.json` for the exact installed infantry calibration.
`evidence/inherited_companions.json` retains counter consumers/tokens/frames, source/runtime hashes, inspected vanilla DDS and palette/reference evidence, shared audio hashes, and missing specialized source-audio originals.
No companion asset was regenerated; role-to-sound timing remains parent-owned and pending accepted actions.

Blender 5.1.2 and checksum-locked io_pdx_mesh 0.91.0 remain the route; each wrapper call records the applicable lock.
No Meshy calls or paid operations occurred; credits estimated/consumed are zero.
The parent owns acceptance, runtime definitions/copies and commits.
This is incomplete: anatomical selection, surface repair, eight roles, export/reimport, synchronization and inherited provenance gaps are explicitly unresolved.
Skills applied: chaos-redux-3d-model-pipeline, chaos-redux-event-assets, chaos-redux-subagents; none modified.
