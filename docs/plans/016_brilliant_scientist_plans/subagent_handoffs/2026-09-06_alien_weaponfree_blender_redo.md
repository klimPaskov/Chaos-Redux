# Alien infantry weapon-free body and Blender assembly

Status: in progress; fresh body downloaded, Blender preparation and assembled replacement remain pending.
Owner: `/root/alien_weaponfree_redo`, GPT-6-astra.
The parent owns runtime copying, GFX/entity/animation registration, sound/effect wiring, and final runtime review.
Historical V13 sources, evidence, and runtime files remain preserved.

The explicit 2026-09-06 user instruction authorizes a new weapon-free Meshy 7 body followed by manual Blender rigging, weights, separate required firearm modeling, and all seven semantic actions.
It supersedes old fused-firearm and provider-only action restrictions for this attempt.
No Meshy rig or animation call is permitted or used in this firearm route.

The deterministic production root is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/attempts/20260906_weaponfree_blender/`.
Its `job.json` records source authorization, calibrated vanilla height, full geometry budget, action roles, outputs, and ownership.
The original source and V13 authority remain `attempts/v13_firearm_preset/final_manifest.md` and the 2026-09-05 V13 runtime closure handoff.

The approved single image is `refs/derived/20260906_weaponfree_body.png`, SHA256 `E54AD4A5A625A709025DBAA65924C32DE81A7F7FE5FC984777D437351EFA8928`.
The parent visually approved its retained alien identity, empty open hands, full anatomy, A pose, and clean alpha against light and dark backgrounds.
Two native ImageGen edits were used; native alpha failed, and the documented installed rembg/isnet fallback preserved the accepted generated RGB while repairing alpha.
Exact prompts, source hashes, generated hashes, model hash, alpha statistics, and comparison evidence are in `reference/imagegen_prompts.md`, `reference/alpha_fallback.json`, `reference/alpha_refinement.json`, and `reference/body_alpha_comparison_final.png`.
The original retro right-handed ray pistol remains a required separate Blender component with cyan muzzle, gunmetal receiver, brass rings, grip, and trigger guard.

Meshy task `01a07659-5c46-71ee-b05f-8cb3fa8cc1d4` succeeded with exact `meshy-7`, one local image, integrated triangular remesh target 52,000, PBR texturing, GLB/FBX outputs, and no automatic real-world sizing.
Provider-reported consumption is 30 credits, matching the estimate; live balance was 422 before and 392 after.
The package reserve is 75 credits, leaving 45 before parent coordination.
The approved official route is `@meshy-ai/meshy-mcp-server` 0.4.0 through the locked repository wrapper, with MCP SDK 1.29.0 and compatibility revision `meshy-7-v5`.
Some legacy MeshyClient history metadata says v4; the live wrapper, locked patched-file hashes, and archived tools/list are the actual route evidence.
The process key was sourced from Windows User environment for provider processes and was never recorded.

| Download | Bytes | SHA256 |
| --- | ---: | --- |
| `provider/source/alien_weaponfree_body.glb` | 10146816 | `A80C68DA73C2152AF30B958358EDC4062F6CF1FC92C1282C303A3978E75D055F` |
| `provider/source/alien_weaponfree_body.fbx` | 14720636 | `51BC2F8A76BC95907B71DCDA6E1A7C9910D76E27958FE42DCE397233161DA0E8` |

Blender 5.1.2 and deployed io_pdx_mesh manifest 0.91.0 were verified through the adapter and socket route.
The installed extension contains accepted Python/Blender modernization relative to the checksum-locked release archive; its exact deployed author/commit remains unresolved, and it is not claimed to be stock archive bytes.
`io_pdx_reconciliation/source_comparison.json` preserves every inspected source checksum and normalized differences, while `io_pdx_reconciliation/reconciliation.md` records the parent's acceptance and concrete compatibility evidence.
The current adapter reimported the preserved V13 mesh, 24-bone rig, muzzle locator, and laser action with five sampled frames; missing adjacent old-probe DDS made that limited probe magenta, so it does not prove texture appearance.
The replacement still requires its own current-byte mesh/animation export and reimport proof.

The scale precedent is installed `gfx/models/units/western_european_infantry.mesh`, selected mesh `polySurface106`, collision excluded, and `gfx/entities/units_infantry.asset#infantry_rifle_entity`.
Source height is 7.3518242835, entity scale is 0.8 exactly once, and effective runtime height is 5.8814594268, forward -Y and up +Z.
The complete body plus pistol ceiling is 59,999 triangles.

Required roles remain idle, move, laser_attack, defend, support_attack, retreat, and death.
`weapon_and_action_brief.md` records deliberate draft phase plans; these are not accepted final animation timings.
Final discharge, recoil, footfall, impact, locator, and sound timing rows will be measured from reviewed new actions.

The six existing sourced CC0 sound roles are preserved.
`companion_evidence.json` verifies all 12 original/derived audio checksums against `evidence/audio/provenance/audio_sources.json`.
Per-subunit selection/acknowledgement remains subject to the existing tag-wide vanilla consumer limitation.
The existing large and small bespoke counters are preserved with matching checksums and inspected vanilla dimensions/palette.
`reference/retained_counter_comparison.png` exposes a dark green rectangular matte in the current alien normal frames; this is flagged for parent visual review and no counter replacement was authorized in this bounded redo.

Remaining work: body geometry/material QA, measured rig and weights, separately controlled pistol and muzzle, seven reviewed skeletal actions, final packed textures, current-byte exports/reimports, sound/locator crosswalk, final file manifest, and parent runtime integration.
No completed-package or in-game claim is made.
No simplification has been accepted; incomplete requirements remain explicitly pending.

## 2026-09-08 resumed Blender repair evidence

Owner `/root/alien_resume` resumed with GPT-6-astra and no provider operations.
Incremental credits consumed: 0; retained Meshy body consumption remains 30.
The assembled editable source is `attempts/20260906_weaponfree_blender/blender/checkpoints/11_move_v2_working.blend`.
The move checkpoint exists although the interrupted preceding owner did not save `actions/move_v2_result.json`; it remains subject to action inspection.
The earlier idle-v2 and laser-v1 views show the preserved alien identity and separate retro pistol, but do not replace final multi-frame review.

The coherent adapter 1.10.25 tools/list and checksum evidence is `attempts/20260906_weaponfree_blender/preflight/blender_tools_1_10_25.json`.
`resume_health_request_result.json` records Blender 5.1.2 and loaded io_pdx_mesh exporters; `resume_health_request_route.json` records the lock and a separately successful bridge socket probe.
The exact rest inventory at `evidence/20260906_weaponfree_resume_rest_inventory.json` records actual source weights, UVs, normals, and rig bones, with receipt `resume_inventory_request_result.json`.
All body positions, polygons and UV corner values exactly match the original body inventory.
`resume_cap_request.json` converts the reviewed 25 four-edge holes to 100 fan triangles with actual interpolated source weights, removes only source flap faces 27192 and 34265, and preserves the 59,999 complete-model triangle ceiling.
The expected repaired total is 55,150 triangles; it is a proposal until the adapter succeeds and the resulting file passes review.

The exact patch validated its geometry contract but stopped before editing at the known empty-image fingerprint check: `logs/adapter/dee9f6a22d384e908fe7d9db4d8316a2.result.json` reports `Promotion texture image must be packed or inside the same job.`
The shared adapter owner was notified and owns the correction.
Further action authoring subsequently stopped at the dependency checksum gate while that owner was staging shared-source changes; no gate was bypassed.
No final source selection, runtime copy, export/reimport, or complete-package claim has been made.

`attempts/20260906_weaponfree_blender/resume_weight_audit.json` independently checks the adapter-recorded rest weights of checkpoint SHA-256 `AA6F1A368B659333EE0D13C9F932C44BD1A9BFB9CED9817EFBD6C81106D4FFE6`.
All 26,028 body vertices have normalized skin weights on the 52-bone rig: 5,023 have one influence, 15,328 have two, and 5,677 have three; zero vertices have no weights or simultaneous left/right influences.
This is rest-weight evidence only and does not claim final deformation, hand contact, or export acceptance.

Adapter 1.10.27 was published and the resumed live schema records 45 operations in `preflight/blender_tools_1_10_27.json`.
The original move worker report was recovered from `blender/reports/11_move_v2_working.json`, verified against the checkpoint hash, and restored as `actions/move_v2_result.json` with explicit receipt-recovery provenance.
The frame-9 move front/side/three-quarter views show an articulated swing foot, knee flexion, preserved pistol grip and free-arm motion; opposite-swing and mid-idle review are underway.
`resume_spec_audit.json` records seven distinct manual draft actions with 9, 16, 11, 10, 17, 15 and 32 varying bones respectively; all intended loops close exactly at the drafted keys.
The planned firing times remain attack frame 19 (0.6 seconds), support frames 21 and 53 (0.666667 and 1.733333 seconds), pending actual final action acceptance.
The 1.10.27 patch and action routes encounter an additional empty-path image case, `Empty-path image requires local loaded FILE/GENERATED pixels.`, recorded in adapter receipts `877b9665d45a46b7bebd46346389a1df` and `172884901484461fb2ee3b6509256a15`.
No repaired or new firing checkpoint was saved by those failures; the adapter owner is correcting the case while the asset worker continues read-only pose review.
This is an active dependency pause, not a terminal asset disposition.


## 2026-09-08 saved-state continuation

Disposition: active implementation; this section supersedes the earlier temporary adapter-pause and proposed-cap status above.
No new provider calls were made; the fresh weapon-free body remains task `01a07659-5c46-71ee-b05f-8cb3fa8cc1d4`, with 30 credits previously consumed and zero additional credits in this continuation.

The exact cap repair succeeded through adapter 1.10.30 in receipt `fc244f372f7c4e53802aa3963b9738df` and `resume_cap20_request_result.json`.
Checkpoint `21_body_caps_working.blend` has 52,098 body triangles and 3,052 separate pistol triangles, totaling 55,150 below the 59,999 ceiling, with zero nonmanifold edges and degenerate faces.
The 25 seam-aware fan caps and two flap removals preserve unrelated source positions, weights, UVs, materials and actions through save/reopen comparison.

All seven semantic roles have native authored actions; final acceptance remains pending the checks below.
The recovered laser v2 receipt explicitly distinguishes its missing original worker report from native checkpoint/action and exact rest-inventory verification.
Body PDX material rebinding passed at checkpoint `26_body_material_working.blend`, and checkpoint `28_muzzle_working.blend` adds the real `muzzle` locator rigidly parented to `RightWeapon`.
The body uses unchanged provider diffuse, RRxG normal packing and RGB specular with inverse-roughness gloss alpha.

Checkpoint `29_export_batches_working.blend` passed material-only partition and save/reopen proof at receipt `4fc9022793f84ac68da127b6a00fac77`.
Its SHA-256 is `D27627F496234EA3463F273FC260AACA6BA6A5678125B21FAFF0D17FBA93F956`.
It contains seven body export material streams and one pistol stream without changing the 55,150 triangles.
The expected exported body object name is `mesh.002`, with material indices 0 through 6; the pistol is `AlienRayPistol`, index 0.
Actual final export parsing must confirm those names before parent runtime wiring.

Death v2 and v3 impact poses were rejected because the torso floated.
Native v3 frame-43 floor measurements found 194 nearby vertices, all on the left shin or foot, and zero pistol vertices, identifying the extended leg as the actual support problem.
Death v4 changes the late articulated leg poses and retains the raised gun arm; it was authored successfully through adapter 1.10.32 at receipt `a69b7180a9324e06a2d5538be70f3447`.
Checkpoint `30_death_v4_working.blend` SHA-256 is `564657D00CC95F0A3B1E41661400ACC60A2105EE2ED5C833E9F4B2B154F4E8E6`, and native action SHA-256 is `E2531CEEE68C2425984CFA877B61047A5A534AAE25DF76349E40A4F5813B3403`.
This saved checkpoint is not accepted until native floor measurements and uncropped multiframe views confirm the articulated collapse, impact and settled torso contact.

The three native laser frame-19 hand selectors completed with 166 middle-finger, 143 index-finger and 99 thumb-region vertices, with no pagination omissions.
`resume_grip_surface_audit.json` measures those evaluated vertices against every face and edge of the actual modeled grip and trigger in the measured weapon-bone coordinate frame.
Middle-finger, index-finger and thumb minimum grip-surface distances are 0.000168, 0.000892 and 0.000657 calibrated source units; index-to-trigger minimum distance is 0.001762.
There are 54, 26 and 12 sampled vertices respectively within 0.015 source units of the grip.
These unsigned distances support contact proximity but do not alone establish acceptable penetration or complete visual hand contact.

At the latest parent resource hold, both outstanding alien scripts completed and no alien Blender operation remains active.
New heavy calls and renders are paused until the parent releases shared capacity; no processes were killed and no mutation was retried.
Remaining work is death v4 contact and phase review, firing recovery and support recoil evidence, focused hand/muzzle review, actual mesh and seven animation exports with reimport evidence, final source selection and exact copy manifest.
The existing six sourced audio roles remain retained, with laser discharge at frame 19 and support discharge at frames 21 and 53 pending final action acceptance.
The inherited dark-matte counter concern and selection/acknowledgement consumer limitation remain explicit parent review items.
No final runtime copy, in-game completion, complete asset-package claim or commit has been made by this worker.


### Reviewed export candidate: death v5 and final grip

The shared capacity hold was released and calls resumed serially through coherent adapter 1.10.33.
The live 45-operation schema is `preflight/blender_tools_1_10_33.json`, SHA-256 `301201212C05D0E6710C4243E02EFC70B8ABD1731C23CA70800935A1A532025A`, with captured lock SHA-256 `0FA4D7696C836F34C127D1AC445826BCAFBF3FEA3DAD88ACEE62CE29B611DDAB`.

Death v4 was rejected after full-body framing revealed a small back gap supported by both boots.
Death v5 raises the ankles relative to the pelvis using explicit lower-leg bone poses; no geometry or identity changes were made.
Checkpoint `31_death_v5_working.blend` SHA-256 is `452E4C5AF63460597BE7FE98BD6E5E009D2783B29D11DF868BEA32C225C4AA0D`, and native death action SHA-256 is `0785A5B9BB068607FDC05D6B302AD5CE208D1D4D0BC463A4819B69B2A8625FA4`.
Receipt `6d0c43756aa84a889a435d5c9577e9a5` records body-geometry preservation.
Complete pagination at frame 43 measures 374 body vertices within 0.05 calibrated source units of the floor: 125 LeftShoulder, 100 RightShoulder, 126 Spine02 and 23 Hips dominant weights.
The pistol has zero floor-region vertices.
Frame 61 has 337 floor matches; its first 256 establish continued support by both shoulders and upper spine without requiring the remaining page for that presence claim.
`resume_death_contact_acceptance.json` records the numeric and buckle/impact/settle visual review.

Focused frame-19 firing-hand views at `blender/previews/alien_wf_laser_f19_grip_focus_focused_78b5423d99fa_left.png` and `_three_quarter.png` show fingers wrapping the grip, index contact with the trigger and an opposing thumb without visible grip separation.
The native receipt also proves the frame-19 muzzle position at approximately (-0.670, -3.044, 5.701), with forward -Y at the emitter.
The support discharge keys at frames 21 and 53 preserve the exact same finger and RightWeapon local poses as the reviewed laser frame 19.

`resume_action_candidate_reviews.json` records distinct native action hashes, FPS, ranges, loop policies, reviewed frames and semantic judgments for all seven roles.
Additional reviewed views show laser recovery at frame 31, defend guard at frame 1, support shot/recoil/recovery at frames 21/23/28 and 53/55/59, and retreat opposite step at frame 28.
All seven actions are accepted as export candidates, with actual-byte reimport still pending.
The actual mesh export has started with `split_verts = false` and an explicit new sibling checkpoint `32_exported_working.blend`; prepared animation and reimport requests have not yet been treated as completed outputs.


## Final handoff: ready for parent integration

Disposition: model production implemented and actual-byte validated; parent runtime integration pending.
The authoritative final package is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/attempts/20260906_weaponfree_blender/final_manifest.md`.
Its adjacent `runtime_copy_manifest.json` supplies all 14 selected file paths, byte counts and SHA-256 hashes, exact eight mesh/material stream rows, seven entity-role mappings, muzzle matrices and event timing.
The final mesh SHA-256 is `842F0FCA441F9FF14C8A32AC4EF3E9D93C998195D7ACB49CEBD6A1C2BC822E21`.
The final source remains checkpoint 31, SHA-256 `452E4C5AF63460597BE7FE98BD6E5E009D2783B29D11DF868BEA32C225C4AA0D`.

`final_reimport_acceptance.json` verifies seven distinct actual animation binaries with the exact final mesh, 52 bones, 55,150 triangles, source height 7.3518242835, 35 sampled ground contacts at approximately 0.001, closed position-welded topology, and no invalid normals or degenerate geometry.
All selected source hashes remain unchanged after reimport.
The native export has eight bounded streams; maximum vertex count is 8,929 and maximum index-array length 24,000.
All seven reimport deformation views were reviewed, and the parent separately accepted actual-byte laser25quarter, support49quarter, death61left and the focused grip views on 2026-09-08.

`final_firing_locator_evidence.json` proves the actual imported locator on `io_pdx_rig/RightWeapon` at laser frame 19 and support frames 21/53, facing -Y at approximately (-0.670, -3.044, 5.701).
Laser frame 21 has rearward muzzle movement and approximately 7 degrees upward recoil.
The actual-byte body has zero unweighted vertices and no more than three influences; all 8,929 serialized pistol vertices have exactly one influence.
Use `(frame - 1) / 30` for events: attack 0.6; support 0.666667 and 1.733333; move footsteps 0 and 0.533333; retreat footsteps 0 and 0.6; death onset 0 and impact 1.4 seconds.
Idle entry is a one-shot at 0 seconds, and defend has no discharge.
The attack and support clips are non-looping; idle, move, defend and retreat loop; death does not loop.
The parent owns any entity playback repetition of a non-looping combat clip.

Final exports and the first five reimports used coherent adapter 1.10.33; retreat/death reimports and exact-frame locator inspections used 1.10.34.
Both live 45-operation schemas and their dependency-lock hashes are captured in attempt `preflight/`; no route gate was bypassed.
Blender remains 5.1.2 with the checksum-locked io_pdx_mesh manifest 0.91.0 reconciliation already documented in the attempt.
No additional provider credits were consumed and no new paid tasks were submitted.

All six source and derived sound hashes are preserved in `resume_preserved_audio_hashes.json`.
The inherited selection/acknowledgement consumer blocker and counter dark-matte review remain explicit companion limitations; no required 3D component or action was simplified or omitted.
The existing job manifest and runtime/sound handoffs now point to this replacement source of truth while retaining their V13 sections as historical evidence.
Files changed are confined to the alien package and this handoff.
No runtime assets, entity definitions, GFX, gameplay files or commits were changed by this worker.
No Blender calls remain active.
The parent owns exact source-to-runtime copy/hash comparison, stream/material and state wiring, synchronized particle/light/audio event replacement, final integration disposition and commit.
No in-game completion is claimed.
