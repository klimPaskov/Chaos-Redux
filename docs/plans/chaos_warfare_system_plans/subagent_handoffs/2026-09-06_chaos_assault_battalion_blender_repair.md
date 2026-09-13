# Chaos Assault Battalion Blender repair

Status: `in progress`; runtime promotion remains parent-owned.

## Scope and source

The parent authorized repair of the existing fictional game unit's faulty actions, retention of accepted idle/move, and completion of missing physical props using GPT-6-astra and the locked Blender adapter.
No Meshy operation was needed or performed; estimated and consumed credits are both zero.
No functional chemical mechanism, formulation, or dissemination design belongs to this visual package.
No gameplay, GFX, entity, audio definition, counter, or runtime model file was edited.

The previously named job root was absent at intake.
The runtime `.mesh`, four `.anim` files, and three DDS files were copied into `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/source/runtime_2026_09_06/` before repair.
`evidence/recovery_inventory.json` records hashes, inherited historical Meshy-6 lineage, preserved sound/counter hashes, material findings, and source limitations.
The prior source history is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_chaos_assault_battalion_animation_recovery_2026-08-22.md`.
Its expired-provider requirement is superseded for this repair by the parent's explicit manual Blender authorization.
Its source URLs, approved original image, provider downloads, and original PBR maps could not be recovered from the absent job archive and have not been invented.

## Evidence completed

The locked adapter was healthy on Blender 5.1.2, build `ec6e62d40fa9`, with io_pdx_mesh 0.91.0 loaded and the bridge independently listening on port 9876.
Adapter versions 1.10.21 and 1.10.22 appear in request receipts because the parent-owned shared adapter was updated during this run.
The initial five adapter source checksums matched the dependency lock; subsequent parent-reviewed measured-operation hashes were also verified before use.
The live wrapper tool schema is preserved in `evidence/live_tools_20260906.json`.
Every Blender operation uses the repository adapter and has a request/response ledger under `logs/adapter/`.

Actual runtime mesh and idle, move, and death bytes were reimported through io_pdx_mesh into independent source checkpoints.
Multi-frame reimport previews confirm that idle and move retain genuine skeletal motion and the old death pose visibly floats.
The source has one 30,000-triangle body mesh, `Mesh1.002`, and one 24-bone rig, `io_pdx_rig`.
Its weight audit reports zero unweighted vertices, no vertices over four influences, and weight sums within approximately 0.00000005 of one.
The inherited topology has 118 position-welded boundary edges and remains a source-geometry review issue.
Front and three-quarter inspection shows empty hands, a gas mask, coat, helmet, equipment belt, and backpack; no firearm geometry is present.
Subsequent left-view actual-byte review reveals an existing projector-like stowed attachment at the hip/backpack.
The source component audit finds one position-welded connected mesh, so simple loose-component separation cannot recover that attachment.
See `blender/previews/reimport_attack_body_roundtrip_20260906_frame_046_left.png` and `evidence/source_connected_components.json`.

The installed vanilla `gfx/models/units/western_european_infantry.mesh` was reimported separately.
Read-only vertex inspection excluded collision object `pCube1` and measured body `polySurface106` at source height 7.3518247977.
The battalion measures 7.3518238068, matching the calibrated vanilla body within approximately 0.000001 scene units.
Vanilla `gfx/entities/units_infantry.asset` defines `infantry_rifle_entity` at scale 0.8; the battalion retains that scale exactly once.
Effective heights are 5.8814598382 and 5.8814590454, respectively.
See `evidence/scale_crosswalk.json`, `evidence/vanilla_body_landmarks.json`, and `validation/reimport_vanilla_source_calibration_20260906.json`.

## Authored actions

`evidence/author_visual_repair.py` contains job-owned finite pose and prop declarations; it calls only approved structured adapter operations for Blender work.
Its IK arithmetic uses measured rest bones to place both hands and does not execute Blender Python directly.
Each role has an explicit phase specification, editable checkpoint, adapter report, and export candidate.
All roles use in-place horizontal motion at 30 FPS.

| Role | Working source | Frames | Current evidence |
| --- | --- | --- | --- |
| idle | Recovered immutable runtime clip | 1–121 | Prior acceptance retained; fresh actual-byte reimport |
| move | Recovered immutable runtime clip | 1–90 | Prior acceptance retained; fresh actual-byte reimport |
| attack | `blender/checkpoints/attack_v2_20260906.blend` | 1–61 | Authored raise, aim, effort, reaction, recovery; export exists; assembly review pending |
| defend | `blender/checkpoints/defend_grounded_20260906.blend` | 1–73 | Authored brace, duck, guard, recovery; measured root correction; export exists |
| support_attack | `blender/checkpoints/support_attack_grounded_20260906.blend` | 1–91 | Authored sight, cover, hold, effort, recovery; measured root correction; export exists |
| retreat | `blender/checkpoints/retreat_grounded_20260906.blend` | 1–49 | Authored backward-step cycle; measured root correction; export exists |
| training | `blender/checkpoints/training_v2_20260906.blend` | 1–121 | Authored present, hold, scanning, grip check, recovery; export exists |
| death | `blender/checkpoints/death_working_20260906.blend` | 1–90 | Genuine recovered collapse; correction currently blocked by recovered-action metadata gate |

Defend, support attack, and retreat root translations were calculated from each preceding adapter report's all-frame evaluated ground bounds, converted through the inverse measured Hips rest rotation, and authored once as bone-local keys.
All previously authored joint rotations were retained.
New checkpoint measurements place the lowest body point at 0.001 scene units within approximately 0.00000036 across every frame.
Attack and training stay near zero without correction.
No original idle/move clip was replaced with a static pose or semantic alias.
The new exports under `runtime_candidates/20260906/` are candidates, not approved runtime files.

## Prop and material review

The initial generic 324-triangle hand-prop draft is `rejected` after the stowed attachment was identified.
It was never successfully added to a Blender checkpoint and must not be used as a replacement identity.
The existing visible shape must instead be identified, preserved, and made controllable as appropriate.
Initial attachment also exposed a route defect because promoted runtime reimports have working flags but no `WORKING` collection; the exact failing receipt is `logs/adapter/bb258e8ea72c49c6a5bde8f71fa9c3ea.result.json`.
The parent assigned this shared adapter issue to `bounded_adapter_recovery`; this worker did not edit the adapter.

The inherited `assault_specular.dds` is exactly grayscale in RGB and has constant alpha 255.
Installed `gfx/FX/pdxmesh.shader` uses G for specular strength, B for metalness, and A for glossiness on the advanced material path.
The lost source archive contains no available original PBR channels, so this map cannot be certified as correctly packed.
It was preserved verbatim rather than silently relabeled or replaced with an assumed material.
Parent material reconstruction or recovered original channels remain required.

## Retained sound and counters

Both `unit_chaos_battalion_icon.dds` and `onmap_unit_chaos_battalion_icon.dds` exist and remain unchanged.
The nine runtime WAV files under `sound/chaos_warfare/chaos_assault_battalion/` remain unchanged.
`sound/chaos_assault_battalion_sound.asset` describes CC0 source derivation, but its referenced immutable licensing/source archive was in the absent job root and cannot be independently verified here.
No replacement audio or counter was generated.
New per-role sound timing remains parent-owned and must follow accepted animation phases rather than the old state-entry aliases.

## Remaining blockers and parent work

This package is incomplete until the separately controlled prop, grounded death, final assembled multi-frame review, and actual exported-byte reimports pass.
The earlier recovered-action metadata rejection is recorded in `logs/adapter/c9a5c88e78c84b0087845544a695b2d9.result.json`.
Parent-released adapter 1.10.24 adds hash-bound `ground_existing_action`; the actual recovered death correction and byte roundtrip are in progress.
Material packing and inherited boundary geometry remain unresolved.
The parent must repair `.gfx` texture filenames from the nonexistent `texture_*.dds` names to the actual accepted texture names and wire distinct approved role exports.
The parent owns runtime promotion, final sound/locator timing, documentation integration, and overall acceptance.
No in-game completion claim or commit is made for this unfinished package.

Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, and `chaos-redux-subagents`.
No skill was changed by this worker.

## Subsequent visual review and released route

Parent accepted preservation of the existing stowed projector after exact left/rear rest inspection.
`evidence/projector_region_page_*.json`, `projector_region_inventory.json`, and `projector_fore_region_*_response.json` hold read-only source positions, UV corners, current weights, and exact topology/action hashes for local extraction planning.
The generic duplicate draft is explicitly disabled in the job-owned script.
No projector geometry has been changed yet; exact face/vertex relocation and rebind await the second bounded adapter tranche.

Attack, defend, support attack, retreat, and training body-only exports were reimported from their actual `.anim` bytes against the immutable runtime mesh.
Their proof JSON files are `validation/reimport_<role>_body_roundtrip_20260906.json`, with five sampled frames from three views each.
Grounded role roundtrips remain within approximately 0.000002 of their intended 0.001 scene-unit clearance; attack/training remain near zero.
These prove skeletal export fidelity, not completed prop contacts.
Defend body visual review rejected an upright brace and then a tiptoe crouch despite numeric contact passing; `defend_planted_20260906.blend` corrects the ankles and preserves a visible crouch.
Training and retreat reviewed frames show distinct head, arm, and leg articulation.

Adapter 1.10.24 live schemas are saved in `evidence/live_tools_1_10_24.json`; release scope is documented in `docs/plans/3d_model_workflow_plans/2026-09-06_adapter_recovery_handoff.md`.
Blender remains 5.1.2 and io_pdx_mesh 0.91.0.
No provider calls or credits were used.

Death root correction through adapter 1.10.24 succeeds and preserves all original body keys and actions.
All 90 frames are grounded within 0.000000716 scene units, with lateral drift below 0.000000239; final source minimum drops from 1.28292191 to approximately zero.
The exported 71,251-byte candidate reimports with matching contact bounds.
However, the final pose visually remains suspended around a low coat/body contact vertex; numeric minimum-Z alone is insufficient and this candidate is not accepted as final death.
See `validation/reimport_death_grounded_body_roundtrip_20260906.json` and its final front/left/three-quarter images.
Defend planted byte reimport is reviewed at frames 19, 37 and 55 with flat soles and distinct crouch-to-rise articulation.
`evidence/action_candidate_manifest.json` records current candidate hashes and explicitly marks every final assembly unaccepted.

`evidence/source_boundary_regions.json` records all 118 position-welded boundary edges as 29 localized regions, with canonical original vertex indices and measured bounds.
There are 28 closed small loops and one seven-vertex branched region; they are candidates for explicit local closure, not blanket garment filling.
A separate fully articulated side-collapse comparison is authored in `blender/checkpoints/death_side_raw_20260906.blend` by `evidence/author_side_collapse.py`; it has not passed contact or semantic review.
The recovered death and its root-only corrected copy remain preserved.

## 2026-09-08 resumed repair evidence

The parent reconfirmed that the hose-connected silver stowed attachment is the intended projector exterior and requires handheld control while preserving its backpack connection.
The parent committed the three actual `assault_*.dds` texture bindings in `469bb2f0bc`; this worker has not promoted runtime models, actions, or textures.
The parent also accepted explicit artistic reconstruction of missing material response, without presenting it as recovered provider PBR.

Adapter health and source-lock checks passed at resume on Blender 5.1.2 (`ec6e62d40fa9`) and io_pdx_mesh 0.91.0, with the independently probed bridge listening on 9876.
Shared adapter releases progressed from 1.10.25 through 1.10.30 while this worker used only structured repository adapter calls.
No provider call was performed; estimated and consumed Meshy credits remain zero.

Material inspection found that the preserved normal DDS stores conventional RGB normals with constant alpha 255.
`evidence/pack_material_candidate_20260908.py` packs a derived RRxG normal and creates explicitly inferred G-specular, B-metalness, A-glossiness response from bounded existing detail and a small neutral-bright diffuse mask.
This is artistic reconstruction, not recovered roughness or certified source PBR.
The diffuse remains byte-identical.
`evidence/material_reconstruction_20260908.json` records immutable input and candidate output hashes, channel definitions, and the inferred-mask fraction.
The candidate DDS files retain the parent-fixed runtime basenames under `textures/dds/20260908_reconstructed/`.

The first material bind failed its preservation invariant in receipt `8dafc13d9c19449da854702a7c654b04`; the shared adapter owner repaired that route.
The successful bind is `b6d6e4a064414e0ea76193b13356503d`, with editable checkpoint `blender/checkpoints/attack_material_20260908.blend` and SHA-256 `7C201174AE1FEB36F4FADD28ABDF72C9C587F3E27E052CF0D4A79D99DA232CFD`.
The parent reviewed `blender/previews/attack_material_20260908_left.png` and accepted the matte olive cloth/leather and distinct silver projector direction with explicit inference provenance.
Final mesh-byte texture-reference proof and completed assembly remain necessary before promotion.

Exact source-index projector selection previews V1 and V2 exposed a cut shell and then a coat-connected boundary.
The expanded V3 preview first failed its read-only invariant in receipt `e2b4c04b0cb442b6885b5c5270a329f0`; its refreshed successful evidence is `306dcef7dc81491799cb66558bb64e1d`.
The broader selection includes a coat sliver, so none of those selections authorizes broad AABB relocation.
No projector vertex has been moved and no duplicate projector has been created.
Further exact exterior and flexible connection selection remains in progress.

The reviewed front-coat highlight `52ed5967e1c7443ea975b2e5c7184ab7` isolates 905 front-skirt vertices without boots or projector.
`evidence/repair_coat_weights_20260908.py` declares exact replacement weights, feathering hip support into retained boundary weights and upper-leg sharing through the center.
`evidence/coat_weight_design_20260908.json` records every edited source index and the design basis.
The exact vertex repair passed requested-value, preserved-neighbor, and save/reopen fingerprint checks in receipt `704281a034fc419e9fba1c9ea7f93124`.
Its editable checkpoint is `blender/checkpoints/attack_coat_20260908.blend`, SHA-256 `D451BB4CCC15ACED783DA78792DC04D866D1BD58FD107266C49BFCB3FECD52AF`.
Geometry, UVs, topology, rig, actions, and material identity were preserved; motion deformation and actual-byte review remain required.

Side-collapse V2, V3, and V4 were visually rejected because the leg spread or hand contact left the torso suspended.
Backward-collapse V1 and V2 were comparison candidates; V3 improved broad backpack support and V4 adjusted final legs.
All original recovered collapse and earlier candidates remain preserved.
The current comparison is `blender/checkpoints/death_back_v4_grounded_20260906.blend`, with action `assault_death_back_v4`, 30 FPS, frames 1–90, non-looping, in-place horizontal policy, and genuine separately articulated stagger, buckle, fall, impact, and settling phases.
`evidence/death_back_v4_contact_response.json` identifies 588 final-pose vertices within 0.15 source units of ground; the first 256 are broad backpack contact rather than a single front-coat hem vertex.
This does not alone establish all-frame acceptance or a completed assembled death clip.

The 29 inherited localized boundary regions remain unresolved; no blanket filling, simplification, or hidden source deletion was applied.
The package remains incomplete pending exact projector control and contacts, completed role-specific assembly review, inherited boundary disposition, final exported-byte reimports, synchronization, and parent runtime promotion.
Existing sourced audio and bespoke counters remain preserved under the bounded repair scope.

## Current resumable state after the resource hold

The parent accepted the material direction after reviewing the side preview and committed the existing runtime texture-name corrections separately.
`evidence/action_candidate_manifest.json` records the accepted material candidate, exact coat repair, new death candidate, and remaining assembly blockers.
`evidence/repair_artifact_hashes_20260908.json` records the selected checkpoints, binary exports, and exact assembly specifications.
No runtime candidate has been promoted.

The unpartitioned body export produced 90,000 corner vertices in one stream and failed the 65,535 vertex gate; its output is rejected.
The existing skeletal partition operation preserved all 30,000 triangles and passed in receipt `d5ac941c03824503a2347d4c03ffcba0`.
The subsequent export passed in receipt `b1dd3743b5a14658a921dd197ad7257e`, with two streams of 60,000 and 30,000 vertices and no exporter warnings.
The candidate is `runtime_candidates/20260908/chaos_assault_battalion_body_partitioned.mesh`, 7,563,021 bytes, SHA-256 `1DA2D00BE8745333E6780CE4BFF34298C67FDA3EB37FCEC6335288C7A9D9C2CC`.
The death export is `runtime_candidates/20260908/chaos_assault_battalion_death_back_v4.anim`, 71,251 bytes, SHA-256 `2AF1665772AA32C76FA3B46840A8EFC35C7679505E75208B069735696E881442`.
The exact accepted-material DDS copies beside those binaries are recorded by `evidence/texture_staging_copy_20260908.json`; reimport must use `stage_default_textures = false`.
The parent paused new heavy calls for shared-memory recovery and prioritized other packages.
No heavy call remains outstanding for this worker.
Actual-byte reimports of this mesh/death pair and coat-deformation checks on retained idle/move are queued under that hold, not claimed complete.

Existing-route composition was evaluated before requesting an adapter extension.
The proposed projector removal initially comprised 770 faces, below the 1,500-face limit, but its 88 welded interface edges split into 32 open raw-index paths across UV seams.
Adding four explicitly named local body-closure faces (`13252`, `13255`, `16873`, `17497`) resolves the welded branch points while remaining at 774 removed faces.
`evidence/projector_alias_rim_spec_20260908.json` contains 33 exact alias groups with 71 original vertex indices, 97 retained face-corner remaps, and three post-alias simple rim loops of 64, 6, and 18 representatives.
The maximum position difference and maximum bone-weight difference within each proposed alias group are both exactly zero.
UVs and custom corner normals must remain distinct and unchanged; no averaging is authorized.
The adapter owner has the finite specification and has queued the bounded alias-aware repair capability.
The source for that specification is `blender/checkpoints/attack_coat_20260908.blend`; no projector geometry has been mutated.

`evidence/projector_source_corner_uvs_20260908.json` preserves all corners of all 770 selected source faces with zero missing UV records.
`evidence/projector_component_source_spec_20260908.json` prepares a faithful reconstruction from those faces, with two coincident source-coordinate vertex-fan splits and 88 inferred hidden closure triangles.
The prepared component has 429 vertices and 858 triangles, every edge incident to two faces, and minimum triangle area approximately 0.0000688076 source units squared.
Those numerical checks do not establish visual acceptance of the inferred closure surface.
`evidence/projector_component_spec_20260908.json` is the finite `attach_rigid_component` declaration after transforming that geometry through the inspected RightHand rest/posed matrices.
`evidence/projector_component_transform_20260908.json` records its artistic grip pivot, source-to-rest transform, exact matrix evidence, and outstanding contact requirements.
It must be applied only after original fused-source removal and body closure, with the preserved backpack connection restored, so the runtime never contains a duplicate projector.
The inferred closure faces, restored connection, and all eight action contacts require Blender review before export.

The latest captured route schema and checksum verification are `evidence/live_tools_resume_20260908.json` and `evidence/dependency_verification_resume_20260908.json` (adapter 1.10.32 at capture).
Every mutation and inspection still uses the repository-owned adapter; no unrestricted Blender Python, provider operation, generated sound, or replacement counter was used.
The remaining required work is the alias-aware body patch, reviewed faithful projector and flexible connection assembly, all-role grip/deformation/contact QA, disposition of the 29 inherited boundary regions, final export/reimport and copy manifest, synchronization handoff, and parent runtime promotion.
The package is incomplete, with no accepted simplification or scope reduction.

A proposed body-rim cap was deliberately rejected before any Blender call.
`evidence/prepare_body_cap_template_20260908.py` attempted ear clipping in each rim's best-fit plane while prohibiting existing retained diagonals, but returned `No safe ear; do not improvise closure`.
No `projector_body_patch_original_index_template_20260908.json` was emitted and no closure triangle is approved by that attempt.
The 64-vertex rim spans approximately 0.101 by 0.486 by 1.179 source units and is not exactly planar; the smaller 6- and 18-vertex rims are also nonplanar.
The finite alias specification remains valid as a topology proposal, but simple closed raw-index loops alone do not establish a visually safe cap.
Resume must inspect the actual remapped rim and author a reviewed local surface closure before attaching the prepared prop.
Resource hold and the pending alias operation prevent the next required Blender mutation and preview; they are recorded blockers, not completion evidence.

Adapter owner published `repair_explicit_vertex_remap` in coherent 1.10.35 and requested preparation only until a Blender slot is released.
`evidence/projector_vertex_remap_request_20260908.json` is the exact current-schema request, generated without a Blender call.
It remaps 79 changed corners, including 30 on faces intended for later projector removal, and removes 38 unused aliases across the 33 reviewed groups.
The earlier 97 retained-corner evidence rows included unchanged representative corners; these no-ops are excluded from the executable request.
The expected remap result is 30,427 vertices and the original 30,000 faces.
`evidence/projector_vertex_remap_preflight_20260908.json` confirms every removed alias incident corner is covered, no original vertex was unused, no mapped triangle is degenerate or duplicated, and exact world coordinates and full named weights match within each group.
Native local-coordinate, group-index-weight, edge-attribute, per-corner preservation, save/reopen, and old/new mapping proofs remain pending.
This request has not been executed and does not remove faces, close the body, extract the projector, or approve the assembled model.

The first 1.10.35 dependency lock omitted the new operation from its list despite matching source hashes; the adapter owner corrected that metadata.
The corrected lock SHA-256 is 592996B554BADEE6AE56DD8BC882576D3C5D0029A40989B4E06E78001FF6904B, with 46 operations and matching source checksums.
Both the rejected observation and corrected verification are preserved in evidence/vertex_remap_dependency_verification_20260908.json.
The resource hold remains in force and no native remap call has been attempted.

Native alias remap passed under coherent adapter 1.10.39 after the adapter owner released one slot.
Receipt `0c0792645d754415aebc33a1c25a624b` created `blender/checkpoints/attack_projector_aliases_20260908.blend`, SHA-256 `26C7C36E0B9E6469239ABC860E2E5FD35C1510C1B5D2C8D9FC8F021A746AFEC8`.
The result contains 30,427 vertices and all 30,000 original triangles; all 79 changed corners and 38 removed aliases match the finite request.
Positions, weights, corner UVs, face materials, rig, actions, and material/image references passed native preservation checks.
All 90,000 custom corner normals passed the adapter's direction-preservation check, with maximum angular error approximately 0.005496 degrees against a 0.25-degree native encoding tolerance.
Save/reopen passed, and `blender/reports/attack_projector_aliases_20260908.json` contains both-direction vertex and face maps.
The call drained successfully; no extraction or body closure was included.

`evidence/projector_body_patch_request_20260908.json` prepares the next finite patch using those actual native maps and the new checkpoint hash.
It removes 774 mapped source faces, adds 84 inferred cap triangles and one explicitly weighted center vertex, and would leave 29,310 body triangles.
The 64- and 18-vertex rims use consistently oriented minimum-area 3D source-vertex triangulations; the tiny 6-vertex rim uses one mean-coordinate center with the top four normalized averaged source weights.
The locked adapter's pure `validate_patch` function accepted the complete boundary winding, interior edge incidence, occupied-diagonal exclusion, explicit UVs, material slot, weights, and triangle budget.
An additional source-coordinate screen rejected earlier cap variants that crossed nearby retained geometry, and the rejected source-index triangles and crossing history are retained in `evidence/projector_body_cap_rejected_triangles_20260908.json`.
The refined candidate excludes those crossings; `evidence/projector_body_cap_intersections_20260908.json` records zero detected strict nonadjacent noncoplanar crossings among 230 candidate pairs.
That numerical screen excludes shared-vertex faces, coplanar overlaps, and near-edge contacts; it does not establish native or visual acceptance.
The cap request remains unexecuted and requires native preservation and multiple-view body review before the faithful held prop is attached.
The adapter owner received the result and drain report; additional heavy calls await the next released slot.

The body-cap candidate was applied after the adapter owner released the next serial slot.
Native patch receipt `390d9756923a4d9fabb0c7afb4a8f597` created `blender/checkpoints/attack_projector_body_cap_20260908.blend`, SHA-256 `FF561494ACDDA8095FFD57A077964A52512AFD0C04E40233B9F9165F8D1F7D0C`.
The checkpoint has 29,688 vertices and 29,310 triangles, unchanged source bounds, no degenerate faces, no zero-length normals, and no nonmanifold edges under the adapter's raw-index metrics.
The native patch report confirms retained positions, weights, UVs, rig, actions, and materials were preserved.
This older patch operation does not emit a full `save_reopen_proof` fingerprint field, so no such fingerprint proof is claimed for this mutation.
Read-only preview receipt `bf1152f73c574e9d9f82a7527f0b7fa7` reopened the saved checkpoint and returned matching geometry counts, with front, left, and three-quarter PNGs under `blender/previews/attack_projector_body_cap_20260908_*.png`.
These views show the coat surface closed and the backpack preserved; remaining right-hip connector strands still require assembly with the faithful held projector.
The body patch is accepted locally as an assembly candidate, with cap deformation and final mesh reimport still pending.
Both calls drained and the adapter owner received the result; no component was attached in this tranche.
`evidence/projector_component_attach_request_20260908.json` prepares the exact next sibling checkpoint and source hash for the 858-triangle source-faithful exterior component, which would bring the assembly to 30,168 triangles before connection repair.
Its original 770 source faces and UVs remain documented separately from the 88 inferred closure faces; the latter still require visual review in the held assembly.
