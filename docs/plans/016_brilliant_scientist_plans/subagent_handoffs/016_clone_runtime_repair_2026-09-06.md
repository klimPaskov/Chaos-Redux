# Event 016 preserved clone runtime repair

Status: `blocked` for runtime acceptance; bounded rig repair and initial action authoring are implemented, with remaining work below.

This handoff is an incremental resume record, not a completion claim.
The user closure plan forbids regeneration and source substitution, and the parent explicitly authorized preservation of geometry, rest-rig realignment, reweighting, genuine manual actions, and a dedicated 25th rifle bone while retaining all 24 original bone names.
The parent owns final runtime files and wiring.
No gameplay, GFX, entity, sound-definition, shared tooling, dependency-lock, or configuration files were changed by this worker, and no files were staged or committed.

## Source and actual defect

Protected source: `docs/assets/shared_clone_system/models_3d/clone_infantry/blender/checkpoints/closure_2026_09_05_locators_v2.blend`, SHA-256 `29DAAC7EFF2A884F5D34864EAFFE0DFD8383850307A31441FA2E4E5B60182C84`.
The source hash was checked again after repair and remains unchanged.
The original mesh contains 15,398 vertices and 30,409 triangles, including exactly 391 already-approved vanilla rifle vertices.

The fresh action-bound idle render `blender/previews/clone_preserved_acceptance_idle_three_quarter.png` disproves the earlier contact implication: the rifle floats diagonally across the chest while the visible hands remain separated.
The parent reviewed and rejected this grip.
Numerical hand-bone positions near the chest are not deformed-hand contact proof.

The read-only source inventory `blender/reports/clone_preserved_acceptance_landmarks.json`, request `b85a3bdb3f5c42f0a89d29daea1dca9c`, identifies the cause.
Source arm vertices from X=1.0 through 3.33 lie at Z=5.54 through 6.10 in a T-pose, whereas the old LeftArm rest tail is approximately X=2.00, Z=4.85 and the old LeftHand rest head is X=2.20, Z=4.48.
The old bind rig was an A-pose rig fitted to a T-pose mesh.
The diagnostic projection `blender/previews/clone_preserved_acceptance_source_landmarks.png` shows actual source vertices in grey, old bind bones in red, and the approved rifle in brown.
This diagnostic is derived from source geometry and is not generated replacement art.

## Geometry-preserving rig repair and initial action

All job-relative paths below are under `docs/assets/shared_clone_system/models_3d/clone_infantry/`.

The explicit measured T-pose rig declaration is retained in `clone_preserved_acceptance_rig_seed.json`, with its model-specific construction in `clone_preserved_acceptance_rig_spec.py`.
It uses `body_triangle_target = 0` and `repair_boundaries = false`; no geometry reduction, caps, or topology repair was requested.
The verified `chaosx_blender_hoi4_author_measured_creature_rig` call created `blender/checkpoints/clone_preserved_acceptance_rig_seed.blend`, SHA-256 `D1FC97A550C26AA8397C60FBB7E928C45153E6D3B62E0FE326D2153592F16609`.
Request `e4e5b66865bc458d9a9110f37f35a4d4` reports matching before/after geometry, UV, and material signatures and preserves all 15,398 vertices and 30,409 triangles.
The rig has the original 24 bone names plus `clone_rifle`, parented to `Spine02`; `head_end` was not repurposed.
The spatial body weights are a candidate seed, and the rifle is explicitly not accepted with these temporary spatial weights.

The genuine manual idle candidate is `blender/checkpoints/clone_preserved_acceptance_idle_v1.blend`, SHA-256 `C0372D3010A7D078D20AF89ACB7D991404CB291F6699086F4511502B98CA9179`.
Its action is `clone_preserved_acceptance_idle`, 24 FPS, frames 0–72, looping, with explicit ready, left scan, breath settling, right scan, and returned-ready phases at frames 0, 18, 36, 54, and 72.
The measured two-arm IK pose, independent neck/head scanning, and finite spine breathing keys are recorded in `clone_preserved_acceptance_idle_v1.json` and `clone_preserved_acceptance_idle_spec.py`.
No sine generator or whole-rig-only animation was used.
The verified authoring request is `24338e133ef54d4cbde7b9561d94a8cd` and its native action SHA-256 is `7AC0881236E589E60ED940B84046954FF2079A27A96109B303189E7BE477F88B`.
The current candidate records ground minimum and maximum of approximately −0.0000004713 at all 73 frames.
`blender/previews/clone_preserved_acceptance_refit_idle_v1_three_quarter.png` shows the visible hands responding to the corrected bind rig and converging at chest level, but also shows the expected temporary rifle deformation from spatial weighting.
This is not a passing final grip or export preview.

## Exact rifle ownership and queued rigid skin correction

Guarded read-only mesh-region requests `25023b43217f406585fa03bf7aa05557` and `7bbf7f0914bf4927bd903abdad8535a7` cover all original source indices 15007 through 15397.
There are exactly 391 indices, every returned corner belongs to material index 1, `PDXmat_MeshShape`, and no body vertex is included.
The unchanged mesh topology SHA-256 is `A40BD1993D50F3D0657D933DEEF521B969A84812DF134CB2418A02444C2F7662`.

`clone_preserved_acceptance_rifle_selection.json`, SHA-256 `600ABAAA73CF64435C6835118F242A1E96E52FE66B93377EB6C2130EC48934A7`, records this exact subset.
`clone_preserved_acceptance_rifle_skin.json`, SHA-256 `70B2D626230EA9FC46D322102FEEE423A1DF4C90AB2FEB2B97F32C36833207A3`, records every exact prior weight and its proposed rigid replacement `{ clone_rifle: 1 }`.
The parent is reviewing and integrating the robot worker’s `preview_explicit_skin_selection` and `repair_explicit_skin` helpers; neither route was guessed or called before live integration confirmation.
The next operation is to review the exact-index highlight, apply this guarded 391-vertex correction to a new sibling checkpoint, and verify all non-weight invariants after reopen.

## Restored audio and source rejection

The five original `kurt` soldier recordings from [Soldier Voice Acting](https://opengameart.org/content/soldier-voice-acting) are restored under `clone_preserved_acceptance_audio/`, byte-identical to the historical provenance hashes.
The source page was checked and lists CC BY 3.0; credit the author and source/license links for any accepted derivative.
The files are `soldierintro.ogg`, `unitselection.ogg`, `acknowledgement.ogg`, `battlecries.ogg`, and `wounded.ogg`.
Existing death/pain, marching-boots, and cartridge original WAV hashes also match the prior provenance.

The prior rifle source [Gunshots 8](https://commons.wikimedia.org/wiki/File:Gunshots_8.ogg) is rejected for weapon-identity acceptance because its source explicitly describes Audacity/popped-balloon simulated gunshots.
Its public-domain license does not make it an authentic rifle recording.

The parent approved weapon-matched audio replacement within the existing sound scope.
A CC0 [Lee–Enfield .303 recording by kyles](https://freesound.org/people/kyles/sounds/450851/) is preserved from its official high-quality MP3 preview at `clone_preserved_acceptance_audio/lee_enfield_450851_hq.mp3`, SHA-256 `3DF56B0FD86D87DC2203EEA587B2108FA6D4DF63FFCDA9507A2D1EF68FFBA256`.
The original 24-bit WAV requires login and is not claimed downloaded; the unchanged downloaded MP3 is the source artifact for this candidate.
The mechanically converted PCM signed-16-bit, 44.1 kHz mono candidate `clone_preserved_acceptance_audio/clone_preserved_acceptance_rifle.wav` has SHA-256 `7564FEF68FA6BCED44D0FAD372BD337227FE109FC7C8D14DCBD2A0230BD4E0BD`.
No synthesized or newly recorded audio was created.

`clone_preserved_acceptance_audio/audit.json` retains all source/candidate hashes, formats, durations, and exact limitations.
Attempted native audio delivery returned `audio content omitted because you do not support audio input`.
No spoken wording, transient timing, weapon identity by listening, or loop seam is claimed auditioned.
The selection candidate is not wired: the inspected vanilla voice consumer is country/original-tag scoped, not per-subunit, and global voices must not be replaced to impersonate clone-only selection.

## Remaining acceptance work and blockers

1. Apply the reviewed exact-index rifle skin correction through the live, parent-verified route.
2. Refine the actual deformed trigger-hand and support-hand contacts and pose the weapon on its dedicated bone, not only its bone-head markers.
3. Reauthor and validate all nine roles on the corrected 25-bone bind rig; only the initial idle candidate is authored so far.
4. Attack, defend, and support attack each need independently reviewed aim, discharge, recoil, recovery, shoulder/stock contact, muzzle continuity, and exact audio/particle timing.
5. Move and retreat need grounded articulated gait and foot-contact phase evidence; death needs grounded articulated collapse, impact, and settling; training and wounded must be semantically distinct rather than aliases.
6. Recreate and verify muzzle/cartridge locators on `clone_rifle`; old locator parenting is invalidated by the rig replacement.
7. Export and reimport actual `.mesh` and all nine `.anim` byte streams, record actual stream vertex/index maxima, and redo material, culling, scale, topology-risk, and bounds review.
8. Complete source audio semantic audition and final action synchronization; the new rifle candidate is not a final listening-approved sound.
9. Reconcile the existing bespoke counter package and final source hashes through parent-owned wiring, preserving Aryan clone German-infantry aliases.

No runtime-complete or all-nine-action-complete claim is made.
No regeneration, geometry substitution, topology simplification, or source overwrite was performed.
The repaired rig invalidates the earlier 24-bone action exports as final acceptance evidence, even though those earlier immutable exports remain preserved.

## Guidance and dependency evidence

Skills read and used: `chaos-redux-3d-model-pipeline`, `chaos-redux-subagents`, and `chaos-redux-event-assets`.
No skill was changed by this worker.
Required offline wiki pages were consulted, including Entity modding and Graphical asset modding, and the installed `gfx/entities/units_infantry.asset` plus relevant official console/entity documentation were inspected as reference.
Live health request `0ef89547df9944cc9acc53cc1d1dae5f` reported Blender 5.1.2, io_pdx_mesh loaded with all four PDX operators, and adapter 1.10.24.
No provider generation, rig, or animation call was made, and paid credits consumed were zero.
