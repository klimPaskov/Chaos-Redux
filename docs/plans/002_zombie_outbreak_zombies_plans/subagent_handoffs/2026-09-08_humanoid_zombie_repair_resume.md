# Humanoid zombie repair resume — 8 September 2026

Status: in progress; no runtime promotion and no package completion claim.
Parent acceptance basis: direct GPT-6-astra Blender repair of the existing non-firearm base, undead, rabid and infected zombie visuals under the accepted existing-unit repair plan.
Ownership remains the four job folders under `docs/assets/002_zombie_outbreak/models_3d/` and this handoff.
Shared adapter code, final runtime copies and definitions, and Git commits remain parent-owned.

## Source and routes

Each job retains immutable recovered `.mesh`, `.anim` and `.dds` files under `refs/recovered_runtime/`, with original recovery lineage in `evidence/repair_2026-09-06/source_copy_provenance.json`.
No Meshy, ImageGen or other provider operation was used in this resume; estimated and consumed credits are both zero.
Historical source artwork and original provider provenance remain unavailable rather than invented.
The initial live route was adapter 1.10.25 with Blender 5.1.2 and the locked io_pdx_mesh exporters; a separate TCP probe established bridge reachability.
The subsequent lock/schema verification and exact source hashes are in `zombies/evidence/repair_2026-09-08/route_verification.json` and `live_tools.json`.
Refresh that evidence when the adapter owner publishes another coherent lock.
All scene authoring, inspection, exports and reimports use the repository adapter; the small job-local Python drivers only construct structured requests and read returned evidence.
The exact vanilla precedent remains `gfx/models/units/western_european_infantry.mesh` and `gfx/entities/units_infantry.asset`, `infantry_rifle_entity`, scale 0.8 applied once.
Original measured scale evidence remains in each September 6 evidence directory.

## Base zombie actions

The correct existing 24-bone rig and 30,000-triangle source geometry remain unchanged.
The four September 6 added roles (`defend`, `support_attack`, `retreat`, `training`) retain their editable checkpoints and actual-byte reimport evidence.
The recovered idle, move and death clips could satisfy a minimum-Z bound while displaying inappropriate contact, so new articulated drafts use measured limb targets rather than another root-only correction.

- `blender/checkpoints/repair_2026-09-08_idle_manual_v3.blend`: new authored idle; its actual `.anim` export and reimport passed the inspected front contact/deformation comparison.
- `runtime/candidates/repair_2026-09-08/chaosx_zombies_idle_v3.anim`: exported candidate; `validation/reimport_repair_2026-09-08_idle_v3.json` records five sampled ground heights from 0.000998262 to 0.000999003 source units.
- `blender/checkpoints/repair_2026-09-08_move_manual_v3.blend`: authored shuffle; source front/three-quarter frame 11 shows one planted foot and one lifted foot with coherent hands and torso.
- `blender/checkpoints/repair_2026-09-08_death_manual_v3.blend`, `v4`, and `v5`: retained rejected contact drafts; none is final or approved for runtime.
- `blender/checkpoints/repair_2026-09-08_death_manual_v6.blend`: latest editable death draft with extended legs and corrected prone foot orientation; full contact/deformation and byte-reimport review remains required.

The unchanged previously partitioned mesh candidate is `runtime/candidates/repair_2026-09-06/v2/chaosx_zombies.mesh`.
Its four material streams retain the 8,000/8,000/8,000/6,000 triangle partition with no reduction.
The new action exports use this same mesh for actual-byte reimport, preserving skeleton correspondence.
The recovered attack candidate still requires final contact/deformation review; it is not implicitly accepted by idle validation.

## Specialized rigs and roles

The measured V2 rigs in `undead_zombies`, `rabid_zombies`, and `infected_zombies` preserve the complete existing geometry and correct the prior unrelated rig anatomy.
The V2 standing culling-OFF previews no longer show the prior finger-strip pull; this is limited standing-pose evidence, not all-role weight acceptance.
The undead V2 grasp frame 24 preserves fingers and articulated arm motion, but culling holes remain visible.
All three packages now have V2 idle, move, attack, defend, support_attack, retreat and training drafts in `blender/checkpoints/repair_2026-09-06_<role>_manual_v2.blend`.
The existing action specs are per-identity pose plans; none of these roles is a static alias or whole-rig transform substitute.
New death V3 requests preserve the individual standing/hit/collapse sequence and explicitly adjust final pelvis, feet and hand contacts.
Every specialized role still needs full phase visual review, contact and loop review where applicable, export/reimport, and final manifest selection.

## Culling diagnosis and exact repair blocker

`undead_zombies/evidence/repair_2026-09-08/rest_visibility.json` and its front/rear/left preview pairs establish that the large missing chest, face and trouser patches already exist in neutral rest geometry, with no evaluated action.
They match the patches missing in posed V2 culling-ON renders.
Culling-OFF completeness alone has not been accepted as a fix.
The 18,115,250-byte `rest_landmarks.json` contains complete positions, topology, UVs, weights, face normals and corner normals.
The adapter wrote the valid file but its MCP response failed with exit 0 and no JSON-RPC response; this was reported to the adapter owner, and no successful receipt was invented.
Corner normals align with geometric winding on most faces, so they cannot independently prove outward orientation.

The initial 252-face anatomical chest slab was a rejected diagnostic trial because it cut across connected strips and increased inconsistent shared edges; no checkpoint was saved.
The refined selection is one complete 139-triangle anterior chest panel (component seed 24833), bounded by X 0.015–0.678, Y -0.521–-0.024, Z 4.968–5.522.
Its area-weighted direction is approximately [-0.627, 0.550, 0.029] and 96.94% of its area faces inward +Y, unlike the adjacent mirror panel.
The exact list and reason are in `chest_connected_trial_selection.json`; this is a reviewable local orientation trial, not blanket flipping.
Adapter 1.10.30 added selected-only corner-normal sign inversion and preservation of unaffected corners.
Its native trial failed safely before saving because measured normal restoration error was 0.002412897762696663 against the 0.001 limit.
The exact failure is `undead_zombies/logs/adapter/17ffbd2083904f3cb85bfa287a48945d.result.json` and was sent to the adapter owner for diagnosis.
No blanket weld, caps, hidden doublesided material, source overwrite, or global normal reset was accepted.

## Remaining work and companion limitations

All four model packages remain incomplete.
Finish the exact orientation repair and remaining anatomy-specific surface review, specialized phase QA, base death/contact corrections, all actual-byte exports/reimports, final hashes and requirement-to-runtime crosswalks, and parent review before selecting runtime copies.
The prone death camera currently crops the ends in left view because the preview horizontal fit margin is insufficient for a flat wide pose; the adapter owner has the exact renderer issue and example path.
Do not accept a cropped view as complete contact evidence.
Existing audio and counters remain retained under the parent's repair scope; this resume creates no new sound or counter assets and does not clear inherited provenance/consumer limitations.
Animation sound synchronization must be revised for selected final clips after their timing is accepted.
No live-game validation was performed.
Skills used: chaos-redux-3d-model-pipeline, chaos-redux-event-assets, chaos-redux-subagents.
No skill was edited by this worker; the parent owns shared workflow corrections.
No scope simplification was accepted; the listed unfinished repairs and companion limitations remain explicit.

## Latest verified results

All four `evidence/repair_2026-09-08/candidate_action_crosswalk.json` files enumerate eight candidate roles with exact existing artifact hashes and explicit remaining review status.
The base idle V3, move V3 and death V6 animations all completed actual-byte export and reimport against the unchanged 30,000-triangle partitioned mesh.
Move V3 sampled contact Z is 0.000997962–0.000998999 across frames 1/11/21/31/41.
Death V6 sampled contact Z is 0.000998306–0.000999451 across frames 1/22/43/64/85; the minimum alone is not full contact acceptance.
The final death frame is 85; earlier source previews labeled `end` at frame 59 were impact/settling diagnostics, not final-frame evidence.
The actual final reimport image is `zombies/blender/previews/reimport_repair_2026-09-08_death_v6_frame_085_left.png` and remains limited by the recorded cropping issue.
All three specialized death V3 drafts now exist.
Rabid's death request produced a valid checkpoint/report but a repeated transport attempt hit the no-overwrite guard; the existing checkpoint hash and exact action spec were checked and the recovered report is `rabid_zombies/evidence/repair_2026-09-08/authored_death_v3_recovered_receipt.json`.
No failed-response retry was treated as another authorized geometry mutation.

The parent approved a measured native normal angular tolerance of 0.25 degrees, and adapter 1.10.32 recorded exact source normal lengths and selected/unselected direction comparisons.
The 139-face chest repair passed before and after save/reopen with a worst selected-corner angle of 0.138248889 degrees.
The source retained 90,000 corner normal associations, the same 25,256 boundary edges, zero inconsistent shared edges and zero nonmanifold edges.
The checkpoint is `undead_zombies/blender/checkpoints/repair_2026-09-08_chest_connected_trial32.blend`, SHA-256 `8575330253C4B71C7DD4317428583EECF51EF4716D88947F24B2D8B6EDF7E8E2`.
The exact successful receipt is `undead_zombies/evidence/repair_2026-09-08/chest_connected_trial32_receipt.json`, adapter request `36bcfd7d31c346f78d72b2944553215f`.
Front clay culling-ON and original-material views confirm restoration of the large anterior chest panel; other missing surface patches remain unresolved.
A separate local trial addresses two complete trouser panels only (215 calf triangles and 65 knee triangles), selected from measured leg-axis and complete component evidence; its result must be reviewed before acceptance.

Undead defend V2 is rejected for the dramatic stretched armpit/jacket shape at the raised guard phase.
The new V3 guard uses explicit lower elbow targets while retaining the required raised-hand guard and phase timings.
`undead_zombies/blender/previews/repair_2026-09-08_undead_guard_v3_front.png` removes that dramatic distortion without changing geometry or weights.
It remains a candidate pending the other guard phases and culling repair; standing or one-phase evidence does not establish all-role skin acceptance.

The parent imposed a memory-pressure hold after the adapter owner observed 13 Blender processes and approximately 3 GiB free RAM.
This worker stopped launching new heavy operations and will let its one outstanding local trouser validation drain before yielding Blender priority to the other assigned packages.
No process belonging to another worker was killed.

## Resource-hold stopping point

All zombie Blender calls have drained; no further heavy call was launched after the parent hold.
The 280-face calf/knee mutation itself passed adapter 1.10.32 preservation and save/reopen checks, with a maximum normal angle of 0.032958918 degrees.
Its saved unreviewed checkpoint is `undead_zombies/blender/checkpoints/repair_2026-09-08_chest_calf_knee_trial32.blend`, SHA-256 `0D2FD7EC948E5B16E0D08EE8A14FB5D9C63386D024741F2CD650FD6474B417A5`.
The successful mutation receipt is `undead_zombies/evidence/repair_2026-09-08/calf_knee_trial_receipt.json`, request `6db4ca576bed4f27ac63a06bc67f5fe5`.
The following read-only paired preview failed with exit 11 and `EXCEPTION_ACCESS_VIOLATION` in `atio6axx.dll`, before producing any matching previews.
The adapter evidence is `undead_zombies/logs/adapter/2bd512322d7d43c9a827850432954661.result.json`.
No retry was launched; this mutation must not be accepted on its numeric proof alone.
The chest-only checkpoint remains the last orientation trial with complete visual evidence.

After the parent releases capacity, render the saved calf/knee trial without repeating its mutation, review front/rear/left culling pairs, and accept or reject the exact patch selection from those views.
Continue the other explicitly unresolved local surface patches, then specialized eight-role phase/weight/contact review and actual-byte export/reimport.
Re-render the base final death at frame 85 after the camera framing fix is published, with a complete body view and clear pelvis, hand, knee and foot contact evidence.
During the hold, read-only image review also covered base retained attack frames 35/69 and the existing reimported defend 17, support_attack 21, retreat 17 and training 37.
Those samples show coherent articulated hands/clothing and grounded feet; they are additional partial evidence and do not clear the remaining culling or all-frame checks.
No runtime files were copied or wired, and no commit was made for the incomplete package.

### Parent rejection and data-only corpse correction preparation

Parent review explicitly rejected actual base death V6 frame 85: the cropped preview does not establish full-body acceptance and the visible torso/legs float above the floor.
V6 remains rejected; the earlier numerical minimum-Z result does not clear it.
During the global Blender resource hold, no new Blender call was made.
Existing emitted mesh text, its 90,000 weighted export vertices, measured rest matrices, and V6 explicit final keys were reconstructed by numerical linear blend skinning in `zombies/evidence/repair_2026-09-06/corpse_support_analysis.py`.
The reconstructed bounding box matches the native frame-85 report within 0.0000010451 source units, providing a strong cross-check of bone order, coordinate conversion, weights, and pose evaluation.
Evidence is `zombies/evidence/repair_2026-09-08/corpse_v6_support_analysis.json` and `corpse_v6_skin_data.npz`.

The actual lowest support is Head-weighted source vertex 11182 at source position [0.0868951455, -0.6012433171, 6.7359890938], posed at [0.0971788769, -2.5416733354, 0.0009989464].
Its exported split copies include indices 48122, 48667 and 49086, each weighted 100% to Head.
Thus the cropped view's apparent cloth support was incomplete evidence: the head forces the automatic +0.3208061-unit root correction.
Lowest Hips and Spine02 support vertices are source indices 9293 and 11547 at Z 0.02956 and 0.03715.
Left/right hand support vertices 20743/119 remain at Z 0.48353/0.47673; left/right foot support vertices 16045/6013 remain at Z 0.50558/0.55601.
The JSON includes exact source coordinates, posed coordinates, weights and zero-distance source matches for all dominant-bone support groups.

A first downward-limb numerical trial was rejected because elbow penetration caused a larger contact lift.
The bounded articulated contact draft instead coordinates pelvis pitch/height, spine/head settling, ankle reach, asymmetric hand targets and elbow direction.
It changes no geometry, skin weights or materials, and is not a root-only correction.
`corpse_settling_v7_fitted_draft.json` records all proposed parameters and explicit local bone keys.
Final predicted support heights are Hips 0.00662, Spine02 0.01419, Head 0.02543, hands 0.00542/0.03167, calves 0.00100/0.02331 and feet 0.04591/0.02489; the automatic contact offset is only -0.01035 units.
These support heights do not prove acceptable corpse anatomy or silhouette; raised thigh/toe surfaces and all intervening frames remain review requirements.
`action_spec_death_v7.json` preserves every V6 collapse key through frame 39 identically and replaces only impact, rebound, settling and final still phases with coordinated skeletal poses.
`corpse_settling_v7_phase_prediction.json` records those four phase predictions and preservation proof.
The V7 spec has not been authored in Blender, rendered, exported, reimported or accepted.

After explicit parent capacity release, refresh the coherent adapter lock, author the prepared V7 spec into a new sibling checkpoint from the immutable correct-rig working source, and inspect fully framed corpse views plus intermediate impact/settling deformation and every-frame contacts.
Only a successful source review should proceed to a new `.anim` export and actual-byte reimport against the unchanged base mesh.
Do not promote V6, use a root-only lowering shortcut, lower the whole body through cloth, or treat the numerical fit as completed animation QA.
Provider costs for this data-only tranche remain zero.


### September 9 Text-to-Motion source and manual ending integration

The user explicitly authorized one standalone Meshy Text-to-Motion trial; endpoint owner submitted task `01a084a7-4d94-72da-8518-b777e95399bf`, prime mode, 3000 ms, consuming 10 credits.
This worker made no provider call.
Source `zombies/evidence/20260909_text_to_motion/death_prime_3s.fbx` has SHA-256 `22FD74C9A610F9AAD5B2D959050647FDA92D3F95E52B729AC89785267EF688B6`, independently verified against its download receipt.
Native hash-bound inspection identified armature `Reference`, action `Reference|SMPLH_Animation|Base Layer`, 30 FPS, frames 1–90, and 52 source bones.
Evidence, exact 22-control mapping, root-span measurements and verified provenance are under `zombies/evidence/repair_2026-09-09/text_to_motion_*.json`.
The existing target's `head_end` and `headfront` are unweighted Head children; source individual finger channels cannot map to absent target finger controls.
No body, rig, geometry or weight replacement is authorized or performed.

The 1.10.42 transfer failed before checkpoint creation because its motion guard mixed raw source translation magnitudes with scaled target units.
Version 1.10.43 separates angular and world-root checks; its retry successfully created `zombies/blender/checkpoints/repair_2026-09-09_death_text_to_motion_v1.blend` and action `zombies_death_text_to_motion_v1`.
Source/target angular peaks are 15.9248325434 and 15.9248421979 radians summed over mapped controls; maximum world-root error is 0.000000298396 units.
Measured world pelvis-to-ankle ratio is 4.1045212930, applied once through target world/rest-basis conversion.
The source checkpoint's prior action hash remains preserved, all imported provider bodies/rigs were removed after motion transfer, and the separate V7 draft remains preserved.

Actual native whole-body previews at frames 1, 23, 46, 68 and 90 show falling/rolling followed by standing recovery.
Parent viewed frame 46 and 90 and explicitly rejected the full clip as death.
Parent authorized the existing manual Blender fallback: retain the usable fall, replace the get-up with articulated impact/rebound/settling and terminal hold in a new sibling action, and never spend a second provider attempt.
The frame-46 raised legs cannot be frozen as the terminal pose, and a whole-body lowering cannot substitute for articulated settling.
No death export or runtime promotion has been performed.
The pending derived edit requires the adapter's exact native key inventory and death support in the clone/phase-patch route, plus explicit unmapped-tip reset proof.
Floor QA must use the original calibrated world Z=0 plane; preview plane placement is not contact evidence.
