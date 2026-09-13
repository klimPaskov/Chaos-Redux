# Rabid and infected zombie geometry and action repair

Status: in progress; all new native calls paused under the parent’s reinstated shared transport hold after the accepted 1.10.47 release.
This document records evidence and unapplied drafts, and does not approve a model, animation, runtime promotion, or in-game result.

## Ownership and source

The worker owns only `docs/assets/002_zombie_outbreak/models_3d/rabid_zombies/` and `infected_zombies/`, excluding each package’s `sound/` and `counters/`, plus this handoff.
The parent owns runtime mesh/action promotion, entities, GFX, sound definitions, shared adapter configuration, and completion claims.
No commits or shared files were changed by this worker.

Source mode is `existing_runtime_recovery_user_authorized`.
The exact recovered bodies are the identity reference; neither is firearm-bearing.
Historical Internet artwork, original provider jobs, creator attribution, reference refinement, and provider task lineage are unavailable archival gaps.
No replacement provenance is inferred or invented.
Provider operations, estimated credits, consumed credits, and recovery credits are all zero.
The Meshy key gate does not apply to this authorized Blender-only repair.

Both packages retain their immutable `refs/recovered_runtime/` bytes and `evidence/repair_2026-09-06/source_copy_provenance.json`.
Fresh `evidence/repair_2026-09-12/source_texture_byte_verification.json` verifies all eight recovered source files and their current runtime counterparts against the archived hashes, plus the three texture aliases.
All copies match at this checkpoint.
The diffuse, specular and normal maps remain 1024 × 1024.
Rabid’s recovered maps have distinct packed specular channels and tangent normal data in green/alpha.
Infected’s original specular is entirely grayscale with opaque alpha, and its normal is conventional opaque RGB tangent data; both are rejected for the installed PDX channel contract.
The parent authorized packed derivatives that preserve the original files and diffuse atlas.
The infected normal repair uses `R=0, G=source.R, B=0, A=source.G`.
The specular repair deliberately treats the recovered grayscale as scalar roughness variation for nonmetallic skin and cloth, and uses `R=0, G=32, B=0, A=255-source.R`.
The historical grayscale semantics are unproven, so this is a documented reconstruction decision rather than a recovered provider claim.
Repository packing and DDS conversion evidence is recorded in `infected_zombies/evidence/repair_2026-09-12/material_repair_v1_channel_evidence.json`; native material binding and lit comparison remain required.

## Required references and route evidence

Read AGENTS.md, the complete 3D pipeline, event-assets and subagents skills, both job files, the September 8 resume with September 9 appendices, the relevant offline wiki pages, installed vanilla documentation, and the exact infantry entity precedent.
The vanilla scale reference is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`, source height 7.351824797689915.
The installed `infantry_rifle_entity` scale is 0.8 and must be applied once by the parent’s entity consumer.
Rabid source height is 7.353147983551025 (ratio 1.0001799806031186); infected source height is 7.353663921356201 (ratio 1.0002501587996036).
There is no arbitrary 1.8 m rescale.

Successful native calls used the fresh official wrapper and locked `BlenderAdapterClient`, adapters 1.10.45 and 1.10.47, Blender 5.1.2 build `ec6e62d40fa9`, independently probed socket 127.0.0.1:9876, and io_pdx_mesh 0.91.0.
Each call has a package-local request, preflight proof and response receipt.
The 1.10.45 lock SHA-256 was `3911B1AAEA062ABACDEDA21639A5A3C33472574E79500234F77403F60EE38680`.
The accepted deployed io_pdx verification report SHA-256 is `9498FB8E634D53C3E290B4542E19A3AB7888DC672C4C3EB4999618AF78687866`; every one of its 37 present and three expected-absent source rows is checked before a call, along with the archive and linked acceptance/comparison hashes.
The archive SHA-256 is `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
The exposed direct MCP route was stale at 1.10.44 and was not used for mutations.

The source guard subsequently caught the parent’s in-progress 1.10.46 partition edit before any Blender call.
The parent extended the global hold into 1.10.47 batch repair work.
The parent released coherent adapter 1.10.47 at commit `f8cf13409`, with configuration SHA-256 `7E132374548AB958B46EA2F15517E2653DB222627AB7869E8260CAEAC45BF5DF`, dependency-lock SHA-256 `4BCB145321C06B527C70E6BE06F9745D5C7C0B43D2152DA43CAC2D880AF22547`, and release-receipt SHA-256 `746CEFF7A94F190EA71E19B1F8A2A1170EAE36E623163961EDEC4A9D32C72678`.
Fresh wrapper discovery succeeded for both packages and recorded 51 tools in each `evidence/repair_2026-09-12/live_tools.json`, SHA-256 `90054E6AF95754CFF3A017EAE4A09B1402360DFE8F4C8501519F9553AB250DB7`.
Native health request `7bed15da41e044eebf902196dad0bff2` and the subsequent read-only inspections returned adapter 1.10.47.
The root then reinstated a global hold after reproducing an intermittent fresh-wrapper `tools/list` EOF/async response race in sibling sessions.
This worker drained its single outstanding read-only call and made no new Blender call after the hold.
Its last receipt is infected `skin_v5_left_review_receipt.json`, request `73da851ba063471493f5fd6dc2dcb91c`, SHA-256 `3D8B1A1B6CE73EE4F1FE1E5D3BA64A2B26AF3C5C5DE013EE0FA92D7DD9B5BDCC`.
The inspected infected source checkpoint rehashed unchanged at `C28B886803F1F723176DDE9AB04113AD803DF421D32A666272EEF00C9C6B202B`; no checkpoint was saved and no Blender mutation was requested.
An explicit coherent release and refreshed source/schema verification are required before further native work.
Technology Tree Viewer is outside this 3D-only package scope per the parent’s explicit instruction.

## Native inspections completed

Both packages have fresh full source-index `rest_landmarks.json` inventories with vertices, triangular faces, UVs, face and corner normals, all native skin weights and rig matrices.
Rabid inventory SHA-256: `A712475AB40EDD4DEC90263538AC94DCAB9CDB28E6A00C80C306EB620A2E632C`, request `6f0db5d24135417687838464608ffaa3`.
Infected inventory SHA-256: `9ABA69503D70353927C7E8D67F8D7DDA9097D4BD5EB5B34C1166B64090028B8F`, request `fbb817d8a66f4484bb10b516f558b267`.
Each mesh has 30,000 triangles; rabid has 26,601 vertices and infected 30,240.
Both use `mesh.003` and the measured 24-bone `chaosx_<slug>_rig`.

Rabid’s native rest visibility evidence compares original material with opaque clay, backface culling on and off, from front, rear and left.
The missing smooth face, chest and knee panels already exist in the rest source and appear when culling is disabled; animation alone did not create this defect.
Disabling culling is diagnostic only and is not an accepted repair.
Infected rest visibility completed after the 1.10.47 release with request `ff2feee762994197add33ac3390ecfab` and the same front/rear/left original/clay culling comparison.
The saved front culling-on/off views confirm existing chest, neck and ankle panel gaps at rest.

The static component-review route rejected the rigged rabid source with request `f1b21d1c896a47029f60bb4a1d0eecdb`: “Component review requires an unparented unrigged static mesh without modifiers, shape keys, constraints, or animation.”
The rejection is retained in the adapter log.
The parent approved supported rest/culling and explicit skin-selection previews without stripping the rig.
Native selected-index previews `b615ff8b7eb74b32ab7101f02dd1a162` and `4c8e1459ae324a939c85afdb988ddf8b` identify the problematic rabid inner sleeve and adjacent jacket areas.
Native V5 selections identify rabid left sleeve and axilla (`63841d3be7784f3fa91ddbf63f61951e`), rabid right sleeve and axilla (`bb9c46ff55964b5697656959648f9920`), and infected left sleeve and axilla (`73da851ba063471493f5fd6dc2dcb91c`).
Their saved front and three-quarter views show continuous intended sleeve ownership with localized mixed boundaries; head, hands, main torso and opposite arm remain outside the solid-red arm selection.
These views support the anatomical selection only; they do not prove the unapplied weight values, their deformation, or the winding repair.
The infected right selection is prepared but has not run.

## Diagnosed defects and unapplied repair drafts

Saved-action reconstruction agrees with original native phase bounds within approximately 0.00000146 source units before any candidate weights are substituted.
It provides a numerical diagnostic, not native or visual acceptance.
The original hard skin-region boundaries produce maximum triangle-edge expansion of about 95.5× for rabid defend and 58.5× for infected defend.
Exact native source edges cross from torso groups to forearm or upper-arm groups over a few hundredths of a source unit.
Rabid examples include vertices 24520–24521 and 24492–24577; infected examples include 27934–27996 and 2284–2285.

Unapplied V1–V4 weight drafts were rejected for remaining nearby-bone attraction or cross-panel discontinuities.
V5 uses the saved source surface to blend anatomical arm/trunk families and only adjacent joints, with exact seed indices and replacement rows recorded.
Its analysis-only proximity graph does not weld or modify any geometry.
The V5 every-frame diagnostic reduces maximum nearby cross-panel opening to approximately 0.026 rabid and 0.049 infected source units across the original eight action drafts.
Within-panel maximum edge expansion is approximately 3.95× and 4.38×; native deformation review must still determine whether those local joint folds are acceptable.
The exact replacement specifications are `skin_candidate_v5.json`, with family evidence and every-frame seam reports alongside them.
They contain more than 20,000 changed vertices, requiring supported bounded split tranches or a verified batch route.
None has been applied.

Winding review is source-index based.
`winding_panel_selection_v1_rationale.json` records a small initial set of visible chest, jaw, neck and knee panels.
`winding_radial_component_diagnostic.json` adds anatomical radial hypotheses for prioritizing other inward panels; those hypotheses require native selected-index and culling review and do not authorize a blanket flip.
Intentional tears, layered collars and genuine open boundaries must remain distinguishable from reversed panels.

Death V3 fails anatomical support review: rabid rests mainly on its head while its pelvis and feet float, and infected leaves most hands, lower legs and feet unsupported.
`action_spec_death_v4_draft.json` and V5 fitting files are unapplied proposals that preserve the original 24 FPS, frame ranges and eight named collapse phases while adjusting real skeletal articulation through impact and settling.
They require native whole-body, terminal-contact and every-frame review before selection.

The V5 terminal fit places sampled skull, torso, pelvis, hands, calves and feet within approximately 0.024 source units of the floor in both packages; it is still an unapplied numerical candidate.
The full-frame analysis also exposed opposite-sign consecutive quaternion keys in original defend, infected training, and death drafts.
`action_spec_<role>_v6_draft.json` chooses equivalent Euler representations within the adapter’s ±360° bounds, preserving phase orientations while changing their intervening interpolation.
`role_specs_v6_interpolation_crosswalk.json` records every changed representation, per-bone consecutive quaternion dot minima and maximum interpolated angular steps.
These are new candidates requiring native full-frame review and are not aliases or accepted actions.
V6 still raises the pelvis between death phases when a limb swings below the floor; correcting quaternion signs alone does not resolve that trajectory.
The unapplied V7 collapse experiment also fails its intended knee-buckle trajectory and is rejected.
The last data-only candidate, `action_spec_death_v8_draft.json`, retains the named phase skeletons and uses articulated two-bone arm/leg solutions between wrist and ankle goals with an explicit bounded pelvis descent.
`death_v8_ik_support_predictions.json` records every frame: minimum Z is approximately 0.001, endpoint reach error is below 3e-16, and maximum pelvis step is approximately 0.152 rabid and 0.123 infected source units per frame.
V8 uses `ground_contact = none` because its skeletal root keys and limb contact corrections are authored explicitly; its source predicts the floor contact and does not rely on whole-body lowest-point repositioning.
The follow-up `death_v8_interpolation_audit.json` rejects V8 for a local LeftLeg rotation step of 172.714° between frames 18–19 for rabid and 153.294° between frames 26–27 for infected.
Positive consecutive quaternion dots and bounded root/floor metrics do not establish anatomical branch continuity.
V8 is preserved unchanged as a rejected diagnostic candidate and cannot be promoted.
The parent requires exact native poses on both sides of those intervals, followed by anatomical branch or path-constraint correction before any export.
Every subsequent candidate must record maximum per-bone angular step and world endpoint motion in addition to contact, bounds and native visual evidence.
The parent instructed the worker to preserve these candidates and make further revisions only after new native evidence following the shared adapter release.

## Remaining implementation and handoff

After the coherent adapter release: refresh source guards and schemas; inspect the V5 seed and transition selections; apply reviewed explicit weights; review and repair exact reversed panels; render matching original/clay culling-on/off views; retain the 30,000-triangle budget; author or preserve and revalidate all eight role actions on the corrected body.
Required roles are idle, move, attack, defend, support_attack, retreat, training and death.
No action is approved for final promotion yet.
The death terminal must settle without a return to standing, and all other actions must retain their intended in-place policy, loop/contact behavior and role-specific articulation.

Package-local PDX mesh and animation export, actual-byte reimport, complete phase/endpoint evidence, editable checkpoints, final hashes, promotion sources and runtime identifiers remain outstanding.
Sound and bespoke counter siblings retain ownership of their companion packages.
Final action FPS, frames, phases and timing must be sent to the parent for sound synchronization after native acceptance.
No final sound/counter status or parent runtime wiring is silently closed by this geometry handoff.

Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, `chaos-redux-subagents`.
No skill was modified within this worker’s package-only ownership.
