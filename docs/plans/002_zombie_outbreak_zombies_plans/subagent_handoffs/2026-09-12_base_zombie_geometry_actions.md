# Base Zombie geometry and action repair

Status: `in progress; no runtime promotion approved`.

The parent authorized completing the existing non-firearm Base Zombie package through the verified Blender adapter, preserving the source geometry and valid actions, restoring missing components, and supplying sourced audio and bespoke counters.
This handoff owns only `docs/assets/002_zombie_outbreak/models_3d/zombies/` and this model-specific note.
Shared gameplay, GFX, entity, sound-definition, and runtime copying remain parent-owned.

## Current source and route

The source mode is `existing_runtime_recovery_user_authorized`.
Immutable runtime sources and their byte-copy lineage are recorded in `refs/recovered_runtime/` and `evidence/repair_2026-09-06/source_copy_provenance.json`.
Historical original concept-art and Meshy geometry lineage were not present in the recovered package and are not reconstructed by assumption.
No provider operation or paid retry was performed in this resumed tranche; cost is zero.

The measured installed reference is `western_european_infantry.mesh`, with source height `7.351824797689915` and `infantry_rifle_entity` scale `0.8`.
The Base Zombie source geometry height is `7.3513383865356445`; the entity scale must be applied once.
The source has a 24-bone rig, 20,798 source vertices, and 30,000 triangles.
The emitted mesh has four material streams containing 8,000, 8,000, 8,000, and 6,000 triangles.
The prior actual-byte reimport's position-welded diagnostic reports no open boundaries, non-manifold edges, degenerate faces, or zero normals; raw export vertex seams remain intact.
There are no expected firearms or held props, and the reviewed source shows a complete clothed humanoid with both hands and feet.

Adapter `1.10.45` was verified through the fresh repository wrapper and `BlenderAdapterClient` with Blender `5.1.2`, build `ec6e62d40fa9`, and accepted deployed `io_pdx_mesh 0.91.0`.
The parent-accepted deployed exporter verification is `.tools/3d_pipeline/reports/io_pdx_deployed_source_verification_20260912.json`, SHA-256 `9498FB8E634D53C3E290B4542E19A3AB7888DC672C4C3EB4999618AF78687866`.
It records 37 exact present files and three expected absences, with zero mismatches.
Job-local verification is in `evidence/repair_2026-09-12/route_verification_1_10_45.json`, `health_wrapper_1_10_45.json`, and `io_pdx_reconciliation_verification.json`.
The already-exposed direct MCP health route returned stale adapter `1.10.44`; all subsequent native calls use the fresh wrapper.
The parent accepted `1.10.47` in commit `f8cf13409` and briefly released the hold.
The Base worker verified its configuration SHA-256 `7E132374548AB958B46EA2F15517E2653DB222627AB7869E8260CAEAC45BF5DF`, dependency-lock SHA-256 `4BCB145321C06B527C70E6BE06F9745D5C7C0B43D2152DA43CAC2D880AF22547`, and all 18 locked source hashes.
Fresh schema capture intermittently returned no JSON-RPC response, so the exact successful 51-tool sibling receipt was copied with provenance in `schema_copy_provenance_1_10_47.json`.
Base fresh health request `2872fa5a929843d7bad8553231b850a6` returned adapter `1.10.47` and Blender `5.1.2`.
The parent then reinstated a transport maintenance hold after reproducing the stdin EOF/async-response race.
No Base mutation or export was sent during that brief release; `transport_hold_1_10_47.json` confirms the three existing death checkpoints are byte-identical and the V4 checkpoint is absent.
At this draft's writing all new native calls remain held pending the transport release.
The unrelated Technology Tree Viewer is outside this 3D-only task by explicit parent instruction.

## Seven retained action candidates

`evidence/repair_2026-09-12/base_saved_candidate_review.json` records exact source, `.anim`, emitted text, and actual-byte reimport proof hashes for idle, move, attack, defend, support_attack, retreat, and training.
Every listed artifact was rehashed against the prior candidate crosswalk.
All seven emitted animations are 24 FPS.
Front, left, and three-quarter contact sheets were assembled from unchanged adapter previews and visually inspected.
Their source-image hashes are recorded in `saved_action_review_inventory.json` and `saved_action_side_review_inventory.json`.

The idle contains breathing, head motion, and a shoulder sag; move is an alternating shamble; attack has an overhead two-hand windup and forceful diagonal downward strike; defend raises and braces the forearms; support_attack reaches, pins, rakes, and releases; retreat reverses the shuffle with a protective hand posture; training uses a low shift, alternating reaches, regrouping, and a scan.
No static alias or whole-object transform substitutes these roles.
The six manually authored candidates have identical first and last sampled joint positions.
The recovered attack's finite sequence returns close to its combat stance and is treated as a one-shot.
`saved_export_quaternion_continuity.json` audits all emitted quaternion samples, beyond the five preview phases.
Idle, move, defend, support_attack, retreat, and training contain no negative adjacent quaternion pairs.
Recovered attack contains four negative pairs and a 100.42-degree right-arm change at frame 28; focused frames 24–30 must be reviewed before accepting or repairing that interval.
Its saved phase-level semantic review does not approve those intermediate frames.

Fresh surface/culling and full-frame checks remain pending.
The old front attack frame 35 preview needs replacement framing, although left and three-quarter views show the complete articulated strike.
Some old native authoring reports contain floor values inconsistent with the sampled exported reimport, so those old report values are retained as diagnostic evidence and are not promoted to a fresh final floor approval.
`candidate_phase_timings.json` supplies exact candidate timing, with pending status preserved for the audio owner.

## Death repair

The sole historical Meshy Text-to-Motion task was `01a084a7-4d94-72da-8518-b777e95399bf`.
Its transferred fall was retained, while the get-up ending was rejected.
Its historical cost was 10 credits; this worker made no provider call.

The immutable transfer checkpoint is `blender/checkpoints/repair_2026-09-09_death_text_to_motion_v1.blend`, SHA-256 `6B6F451A25E54AF2CF7BD0552E6C16DE1F6E1A87400C7876BA9B1EF1848CAC09`.
The failed manual V2 checkpoint remains byte-preserved at `blender/checkpoints/repair_2026-09-09_death_motion_manual_v2.blend`, SHA-256 `642E3F5E9A92096198619B34AE4AF3C927D41DD3A01DE3089BEF5768E708697B`.

The accepted adapter preservation repair was exercised by request `6aeb94d602b24b3ea5fe0c49dd468edc` into the new sibling `blender/checkpoints/repair_2026-09-12_death_motion_manual_v3.blend`, SHA-256 `5841BD42D1C343C44AC99276F864BFD930BCADEF3002CCE691A223EF8BF7309C`.
Its target action reopens exactly with native action SHA-256 `58C63592454E9D8BEEED4392309E6BDA39FB95745F9D0DC4B4D333220320ABD5`.
The receipt permits only release of the orphan material's image consumer: the image ID, content record, and packed hash `251D19FF2C1319CAE198F364282A00DEB1D626AA31CEF365B9298BAD9609A5AB` are retained exactly.
Geometry, rig, original actions, retained materials, and other images remain preserved.
The receipt and complete before/after image records are in `evidence/repair_2026-09-12/death_motion_manual_v3_response.json`.

The full 90-frame native scan returned floor minima from `0.0009989738464355469` to `0.0010012350976467133` source units.
Numerical skinning of the same authored keys matches native bounds within `0.00000250` source units.
Impact and rebound are articulated, and frames 78–90 hold a prone corpse with hip, hand, head, calf, and boot support near the floor.
However, V3 is rejected for promotion because its interpolated frame 70 raises the torso into an unsupported horizontal pose while a fingertip sets the floor minimum.
The native evidence is retained in `death_v3_impact_review.json` and `death_v3_f46_response.json`, `death_v3_f70_response.json`, and `death_v3_f90_response.json`.

The replacement V4 request is a data-only draft at `evidence/repair_2026-09-12/death_v4_patch_request.json`.
`prepare_death_supported_ending.py` retains the fall poses through rebound frame 46, authors world limb-endpoint and middle-joint trajectories while lowering the torso, smooths the explicit skeletal curves, and holds the proven prone ending at frames 78–90.
The quaternion continuity audit found 40 adjacent negative-hemisphere pairs in the unexecuted draft.
Equivalent quaternion signs are corrected across the entire new action, preserving every keyed orientation while selecting the short interpolated arcs.
The uncorrected request is preserved as `death_v4_patch_request_pre_hemisphere.json`, and `death_quaternion_hemisphere_draft.json` records the correction.
`death_supported_ending_draft.json` records every predicted frame and the largest adjacent rotation steps.
The revised draft's largest post-rebound local rotation step is about 16.49 degrees, and its predicted floor range is `0.00099990`–`0.00100022` source units.
The continuity correction changes no keyed orientation modulo quaternion sign, and the minimum consecutive normalized quaternion dot is `0.92325`.
`death_supported_subframe_draft.json` retains the half-frame interpolation checks, whose predicted floor range is `-0.02554`–`0.05312` source units against the source height `7.35134`.
These small between-frame deviations remain part of native contact review and are not hidden by the integer-frame floor correction.
It is not native-authored, visually accepted, exported, or reimported yet.
The new sibling target is `blender/checkpoints/repair_2026-09-12_death_motion_manual_v4.blend`; the source remains immutable V1.

## Companion packages and remaining work

The scoped audio child delivered 32 licensed PCM candidates across the four humanoid packages, and this parent independently rehashed and checked their formats in `audio_intake_verification.json`.
For Base and Infected, the selected physical cues are `attack_impact_02` from Delta12 Studio's CC0 punch recording and `death_body_02` from remaxim's explicitly described falling-body recording under CC-BY-SA 3.0.
Their old unlabeled vocal `_01` alternatives remain preserved and rejected for physical-contact semantics.
The body-fall attribution, source links, license copies, transformations, and hashes must accompany any parent-promoted audio; exact shipping text is in `sound/runtime_attribution.txt`.
The runtime supports a tag-wide infantry selection route; unique per-subunit selection is not assumed.
Agent-side audio input is unavailable, so successful machine playback is not reported as semantic listening acceptance.

The scoped icon artist owns the four `counters/` companion folders and its model-specific handoff.
Exact installed large and small infantry DDS definitions, frame dimensions, alpha, palette samples, and skill-local reference families are recorded in `counter_reference_inspection.json`.
The icon artist delivered all eight large/map strips, but parent review rejected the inactive frame's transparent treatment.
The normal identity frame is accepted and must remain byte-identical; only inactive frame 1 is being corrected to the inspected vanilla opaque pale plate with a concise dark role schematic.
Counter acceptance awaits DDS-decoded neutral-matte proofs and unchanged-normal-frame hashes.
The parent also authorized preserve-or-repair counter audits for the shared-model consumers `wendigo_zombies` and `armored_undead_zombies`; their distinct large/map definitions and DDS files are included in the icon child's scope.

`runtime_consumer_and_texture_review.json` records hashes of the four existing entity/GFX/animation consumer families and all recovered DDS channels.
The existing consumers still alias defend and support_attack to attack, retreat to move, and training to idle; the parent handoff requires distinct registrations for all eight roles.
The Base candidate mesh uses four streams of `Mesh_0.001` with embedded `texture_0.dds`, `texture_specular.dds`, and `texture_normal.dds`; final material overrides must cover the actual emitted streams.

Remaining Base work is the V4 native action patch and intermediate corpse review, fresh body culling and full-frame action checks including the sharp recovered attack interval, actual-byte death export/reimport, final audio timing, counter intake, final manifest/crosswalk, and exact promotion handoff.
No shared runtime file was changed, no Git commit was created, and no in-game validation is claimed.
