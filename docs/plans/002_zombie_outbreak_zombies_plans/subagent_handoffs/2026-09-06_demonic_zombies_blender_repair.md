# Demonic zombie Blender repair

Disposition: blocked, updated 2026-09-08.
Accepted scope is the existing non-firearm repair plan `docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md` and parent’s four-variant resume assignment.
Job root: `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies`.
All recovered runtime source bytes were rehashed successfully against `evidence/runtime_copy_provenance.json` and remain unchanged.

The existing measured checkpoint `blender/checkpoints/04_measured_rig.blend` has 30 anatomical bones, 296 meshes, 25,989 vertices and 30,000 triangles.
Neutral inspection `7bb1953f42464256be4441ef82bfb36d` preserved those counts, all UV layers and zero degenerate faces; preview files are `blender/previews/resume_demonic_neutral_front.png` and `resume_demonic_neutral_right.png`.
Both views expose substantial source surface gaps at neck, lower legs and wings before action deformation.
No whole-body rotation or rescale was applied; diagonal source axes are explicitly documented in `evidence/demonic_rig_design_basis.json`.

## Actual diagnostic action

`evidence/wing_probe_spec.json` contains a three-phase small wing articulation for deformation inspection only.
Adapter request `54b3c3a5cbd742f1a8036bea2999d941` saved `blender/checkpoints/05_wing_probe.blend` and `blender/reports/05_wing_probe.json`, preserving body geometry.
The wrapper retried after this successful saved operation and request `b8b920cfbcce439c93693b8c452dd8e9` correctly rejected the existing output.
Do not rerun the mutating probe against that same destination.
The saved action hash is `E7F37D5E3DA4CE9E4C21F90AA6D2B6185D9433600B4E164295783BE19BC0DBB1`.
Read-only inspection `6f54e0d2a01849aa805d809fc83d4f8d` confirmed the action and generated `resume_demonic_wing_probe17_front.png` and `resume_demonic_wing_probe17_right.png`.
The wing articulates, but this diagnostic does not satisfy any requested semantic role or approve wing weights/roll.

`evidence/measured_rig_axes.json`, request `bcc318e9dc684aabaae64a4e7f6b5c65`, records actual rest matrices.
Eight distinct manual phase designs under `evidence/action_specs` conjugate anatomical transverse/depth/height rotations into those exact local bone axes, including independently articulated wings.
`evidence/author_demonic_designs.py` preserves these declarative inputs and design rationales.
Death authoring request `3174f7c356e44063bc81dbc207b508b2` saved the actual skeletal candidate `blender/checkpoints/05_axes_v2_death.blend`.
This candidate awaits full-body visual deformation/contact review; the remaining seven designs are not yet actual production actions.

Spatially matching seam edges at six/five decimals yields 34,443 paired edges with zero conflicting winding and 21,114 unpaired edges.
Coarser rounding produces a few collisions and does not justify flipping source faces.
See `evidence/seam_orientation_diagnosis.json`; no winding/cap/topology/material fallback was applied.

All eight roles remain blocked: idle, move, attack, defend, support_attack, retreat, training, death.
No accepted role export, final mesh, reimport proof, synchronization, or runtime copy manifest exists.
Full wing/body skin review and the independent surface defect must be resolved before promotion.
Retain measured source scale and entity scale 0.8, with exact vanilla comparison in `evidence/vanilla_scale_crosswalk.json`.

Blender health request `e4a6231ba82d4ae9bb36a2f608d36ee7` verified Blender 5.1.2 and loaded io_pdx_mesh exporters; socket 9876 was independently listening.
The io_pdx_mesh extension is 0.91.0 under the repository lock.
Direct read-only tool hosts identified adapter 1.10.25 while fresh wrapper routes progressed to coherent 1.10.31; future work must use the currently checksum-verified wrapper.
No Meshy/provider or paid operation occurred; credits estimated/consumed are zero.
`evidence/inherited_companions.json` records preserved counters, installed vanilla/palette inspection, audio paths/hashes and missing specialized audio originals/provenance.
No new counter/audio scope was taken; final action-to-audio timing remains pending.
The parent owns final acceptance, runtime copies/definitions and commits.
This package is incomplete, with explicit surface, rig/weight, role, export/reimport and inherited companion provenance omissions.
Skills applied: chaos-redux-3d-model-pipeline, chaos-redux-event-assets, chaos-redux-subagents; none modified.
