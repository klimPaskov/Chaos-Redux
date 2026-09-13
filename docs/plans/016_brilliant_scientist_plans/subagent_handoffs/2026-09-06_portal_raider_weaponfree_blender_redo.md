# Portal raider weapon-free body and Blender rebuild

Status: **asset ready; fourteen selected files and ten distinct skeletal actions exported, reimported and reviewed; parent runtime integration pending**.
Owner: `/root/portal_resume`, GPT-6-astra, continuing preserved worker outputs.
Authority: `docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md` and the parent's explicit firearm dispatch.
The parent accepted final-byte trigger/support grip, stock contact, rigid pack and preserved armored-coat identity on 2026-09-08.
Existing close-view glove/scarf faceting is explicitly accepted; no further smoothing, geometry reduction or provider retry is requested.

## Selected integration packet — 2026-09-08

All paths below are relative to `docs/assets/chaos_redux_3d_model_pilots/models_3d/portal_raider`.
`final_asset_manifest.json` is the current selection authority; `runtime_copy_manifest.json` lists fourteen exact source hashes and destination basenames; `final_action_crosswalk.json` supplies ten actions, loops, roots, source/proof frames, phases and sound event seconds.
Selected mesh: `export/20260906_weaponfree_blender/portal_raider_v2.mesh`, SHA-256 `3B63FF39642713334223C8820F500E0DC48251DCE093876F1AC2F711E9CB68B9`, 3,506,453 bytes.
Copy this selected mesh to the stable runtime basename `portal_raider.mesh`; never promote the rejected first export `export/20260906_weaponfree_blender/portal_raider.mesh` or historical `exports/portal_raider.mesh`.
The other thirteen selected files are ten `portal_raider_<role>.anim` files and diffuse/normal/specular DDS siblings in the same selected export folder.
Editable export-matching checkpoint: `attempts/20260906_weaponfree_blender/blender/checkpoints/wf_export2.blend`, SHA-256 `83E485A27A23ED688FCD7BC0F4F51A2A345E6A92C6B9E6ABC9951B467DC5F1BC`.

The final assembly has 29,662 triangles (28,630 body and 1,032 separate rifle), 14,844 position vertices and a 45-bone rig with articulated fingers/thumbs and a rigid pack.
Closed source geometry and diagnostic position-welded reimports have zero boundary/non-manifold edges or degenerate faces.
UV/normal export seams explain 39,259 reimport vertices and must not be merged in the shipping model.
An identical-material partition produces 20,000/8,630/1,032-triangle streams without geometry reduction, preserving all geometry, rig and action fingerprints.
The failed first export exceeded the adapter's conservative triangle-index batch ceiling; the final second export passes with no warnings (request `1debd230e9874512a2e821a94e358d6b`).
Source height is 7.3518242835998535 against installed western European infantry 7.351824760437012; apply entity scale 0.8 exactly once for approximately 5.881459 effective height.

All ten roles use genuine GPT-6-astra authored skeletal motion at 24 FPS: idle, move, attack, defend, support_attack, retreat, guard, portal_arrival, wounded and death.
The selected arrival action is `portal_raider_portal_arrival_contact_v2`; selected death is `portal_raider_death_settle`.
Arrival retains its airborne entrance and grounded compression/rebound; death includes articulated collapse, impact, rebound and shoulder/pack-supported settling with folded upper leg and held rifle clearance.
`attempts/20260906_weaponfree_blender/reimport_numeric_audit_v1.json` passes all ten actual-byte reimports and fifty sampled frames, with maximum source/proof ground difference approximately 0.0000118278.
All ten animation binaries have distinct hashes and no exporter warnings.
Seven additional exact firing/contact inspections bring saved final-byte previews to 171; exact defend 27, support 19/41, arrival 17, death 47/57 quarter views were visually reviewed and retain the accepted source progression.
Source frame zero maps to proof frame one; event seconds are source frame divided by 24 at animation speed 1.0.
Do not schedule duplicate loop-closure footsteps; idle/guard use a bounded one-second sourced electrical pulse with loop=no, allowing at most a one-second tail after early state exit.
The muzzle effect node is `portal_raider_muzzle_locator`, rigidly parented to `weapon`; actual mesh node transforms match the aperture within native float precision and survive reimport.

Actual-byte full-body appearance: `blender/previews/pdx_portal_defend27_exact_three_quarter.png`.
Parent-accepted final-byte focused grip: `blender/previews/pdx_portal_attack21_grip_focused_aac2106c68c2_three_quarter.png` and corresponding `_left.png`.
Material proof: `material_bind_v1_response.json`, `partition_v1_response.json`, `material_dds_v1.json`, final mesh text and all ten reimport receipts under the attempt root.
All three exported streams use `PdxMeshAdvanced` and the selected 1024-pixel DDS basenames; no default textures are staged in proof reimports.
Culling proof: `attempts/20260906_weaponfree_blender/caps3_culling_comparison_v1.json` and `pwf_caps3_attack20_opaque_clay_culling_{on,off}` previews preserve the closed silhouette; small pixel differences are recorded honestly.
Native preview ground planes auto-follow evaluated bounds, so airborne/contact claims use measured world bounds rather than inferred rendered plane position.

Blender 5.1.2 build ec6e62d40fa9, checksum-locked io_pdx_mesh 0.91.0 and adapter 1.10.39 produced the final packet.
Every native tranche records live schema and lock checks in its `_route.json`; no unrestricted Blender script or shared adapter edits were used by this owner.
Fresh Meshy 7 task `01a07650-f80a-7523-b547-7d1f7ccc0221` consumed 30 credits; this continuation consumed zero provider credits and did not regenerate or retry paid rigging/animation.
Source attribution, original/refinement approval, transparency fallback and task lineage remain in the preserved sections below.

The retained companion audit verifies 24 original/derived sourced audio hashes and both bespoke vanilla-green counters.
Audio licensing and mechanical transformations are in `evidence/audio/licensing/source_ledger.md` and `evidence/audio/audio_manifest.md`; the selected fresh-body timings are in `final_action_crosswalk.json`.
Counter consumers, inspected vanilla definitions/DDS, palette and frame evidence are in `evidence/counter/manifest.json`, `manifest.md` and `gfx_handoff.md`.
No audio was synthesized and no counter was substituted.
Selection audio requires a supported dedicated consumer; the parent must not use a tag-wide infantry voice override as a substitute.

No asset-production simplification or omitted role remains.
Remaining parent work: copy and verify the selected payload hashes, wire all ten entity/action states and muzzle/sourced-sound events, review retained counter consumers, complete documentation integration and commit.
No in-game validation or completion is claimed; the user owns live consumer validation.
`attempts/20260906_weaponfree_blender/runtime_integration_values.json` records exact meshsettings names/indices and exported PDX locator values.
`evidence/audio/runtime_proposal/runtime_sound_copy_manifest.json` and its `.asset.proposal` provide twelve copy-ready sound files with durations, hashes, measured onsets and bounded electrical policy.
All Portal native calls are drained.
The following sections preserve provenance and stage history; historical pending/rejected statuses do not override the selected packet above.

## Scope and selected paths

The only production root is `docs/assets/chaos_redux_3d_model_pilots/models_3d/portal_raider`, addressed by adapter job `portal_raider_meshy7_recovery`.
The legacy `shared_portal_raider_system` package is historical identity/role evidence only and does not trigger duplicate generation.
New evidence and production instructions are in `attempts/20260906_weaponfree_blender/`.
Proposed new final outputs belong in `export/20260906_weaponfree_blender/`.
The parent owns runtime copies, entity/GFX/action/sound wiring, integration, commits, and final review.

## Prepared image and approval

The parent visually compared the original approved reference, the empty-handed derivative, and the magenta alpha review, then approved the exact prepared hash on 2026-09-06.
Selected provider input: `refs/derived/20260906_weaponfree_body.png`, SHA-256 `C8A3350C8F89D7BC492BBA725B105DCAD6ECEF7EFE1EE8DE9812BFF77A328B07`, RGBA 1024×1536, alpha range 0–255.
The derivative preserves the riveted helmet, green goggles, respirator, scarf, charcoal field jacket, olive trousers, weathered gloves/boots, belts/pouches and compact green-coil pack.
It removes the rifle, holstered firearm and weapon hose, restores the obscured body, and provides full-body separated A-pose anatomy with empty hands.
The original rifle remains separate reconstruction evidence at `refs/original/meshy_input.png`, SHA-256 `40B4E7EAE15208322881408671A48204E4AB61FD4223200BC0F8377F8E243D84`.
The accepted job requires one rifle and prohibits extra weapons, so the historical reference's holstered extra firearm is not a required final component.

Original Internet concept: [Sci Fi Soldier and Guns](https://opengameart.org/content/sci-fi-soldier-and-guns), DasBilligeAlien, CC0 1.0, retrieved 2026-08-27.
Its immutable non-shipping source is `refs/source/untouched.png`, SHA-256 `B704CC7286C3F76DC20A80D9DDEF44EADE350DA535E35B9DA64D02246A03F4DC`.
The recorded CC0 provenance permits generative reference use; no new concept source was selected.
The intentional period exceptions are the accepted retro-futurist teleportation pack and energy rifle.

The initial native ImageGen result was RGB with a painted checkerboard, and the targeted transparency edit was RGB with an opaque gradient.
Both are preserved under `refs/derived/`.
The installed official `remove_chroma_key.py` fallback used white tolerance 26, edge contraction 1 and feather 0.4; a mechanical alpha repair restored small enclosed original highlight regions without repainting the subject.
The repaired result was visually checked on magenta and accepted by the parent.
Exact prompt, source comparison, authorization, pipeline route, component list and planned budgets are recorded in `attempts/20260906_weaponfree_blender/intake.json`.
Fallback code and measurements are `repair_alpha.py` and `alpha_repair.json` in that folder.

## Dependency evidence and current hold

Job-local preflight verifies current adapter 1.10.21 source hashes, Blender 5.1.2 build `ec6e62d40fa9`, configured socket 9876, official io_pdx_mesh 0.91.0 manifest and locked archive hash.
The archive SHA-256 is `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
The parent separately reconciled installed io_pdx_mesh changes against the archive and explicitly released the provider hold: the differences are Python 3/Blender compatibility modernization without binary/skin-layout changes.
Reconciliation evidence is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/attempts/20260906_weaponfree_blender/io_pdx_reconciliation/source_comparison.json`, SHA-256 `BCBCF4482639180DDA8651896E1C0A05F2816F18705D6999E6FF2C1CE30195D9`.
Actual-byte mesh and animation export/reimport remain required before package acceptance.

`environment_preflight.json` records dependency-lock SHA-256 `779DB77DD8255BF4809E31807FEA707191B875FFB86FD8AA78A666EC249CCA39` and Meshy schema-lock SHA-256 `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`.
Four locked Meshy wrapper schema probes—two consecutive, then a concurrent pair—expose exact `meshy-7` and the required official tool names with no newly surviving processes.
Full schemas and lifecycle receipts are `meshy_schema_probe_1.json` through `meshy_schema_probe_4.json`.
Selected official server: `@meshy-ai/meshy-mcp-server` 0.4.0, git `d8c77d1cb897e345eb41d38b510b8391b1664346`, MCP SDK 1.29.0, repository compatibility revision `meshy-7-v5`.
Blender health request `99d1eabf6f454b6babd70a5eea436c90` confirmed both mesh and animation exporters load; `blender_health.json` and `blender_live_tools.json` retain that evidence.
The credential is read only from the authorized Windows environment and is absent from all saved arguments/evidence.

## Fresh provider body

The sole approved image was submitted once to exact `meshy-7` through the locked official MCP route, task `01a07650-f80a-7523-b547-7d1f7ccc0221`.
The task succeeded and explicitly reports `consumed_credits = 30`.
The initial call requested textured PBR output, triangular remeshing toward 28,000 triangles, A-pose, GLB/FBX, and no multi-view thumbnails.
No separate remesh, rig or animation task was submitted.
Both body formats and four PBR textures were downloaded and checksummed immediately.

| Artifact under `attempts/20260906_weaponfree_blender/provider/downloads/` | Bytes | SHA-256 |
| --- | --- | --- |
| `weaponfree_body.glb` | 9,935,096 | `BE2DB369FDEEC09364058D8D0C1221046AD44A406FD51E414EAD6540CA77B61B` |
| `weaponfree_body.fbx` | 13,678,380 | `B42E9DD9D658CA343AAEBBA9A938E88A495093C8E3ACB5475461BD9D02DEE5CA` |

`provider_artifacts.json` contains every texture and model checksum, while the nested `provider/requests`, `provider/responses` and `provider/credits` directories preserve exact tool arguments/responses and spend lineage.
Raw GLB metadata reports one triangular body primitive, 29,211 triangles, 36,064 seam-split vertices, one material, no skin and no animation.
This metadata is not Blender geometry, anatomical or material acceptance.
The slight excess over the requested body target requires bounded local reduction to make room for the separate rifle inside the 30,000 assembled ceiling.
The pre-call shared account balance was 512 and the post-call balance was 422 because other workers also generated bodies; this package's provider-confirmed consumption is 30.

## Components, scale and actions

### Native production progress

Short `blender/` and `materials/` paths in this subsection are relative to the new `attempts/20260906_weaponfree_blender/` root, unless an explicit full job-relative path is given.

Namespaced import `ce7c18056ca2461681676be90b858c54` succeeded on adapter 1.10.22 after shortening the source filename for Windows.
No existing source checkpoint was overwritten; the first failed save created no `.blend` and only its empty new source directory was removed before retrying.
The new root is `attempts/20260906_weaponfree_blender/blender/`.
The parent visually accepted the imported `portal_wf_front.png` body silhouette for rig work, and the worker also inspected right, rear and three-quarter views.
Native measurement reproduces vanilla source height `7.351824797689915`; the new body height is `7.3518242835998535`, with entity scale `0.8` applied once for effective runtime height `5.881459426879883`.

The measured rig revision in `blender/checkpoints/wf_rig3.blend` was authored by request `310c839e8ae14a599fe143fa2be90294` on adapter 1.10.24.
It contains 45 bones, including individual two-joint chains for every finger and thumb, and separate chest-parented pack and hand-parented weapon controls.
Each final finger region has positive native vertex coverage; rear pack and capacitor regions use only the rigid pack bone.
Seam welding and 1.46% reduction of the welded body leave 14,343 vertices and 28,749 triangles with no degenerate faces, negative scales or non-manifold edges.
However, 57 boundary edges in 12 small regions remain unresolved because the shared cap routine rolled back its cap pass.
Exact native source indices, directed boundary edges, adjacent faces and coordinates are in `attempts/20260906_weaponfree_blender/boundary_evidence.json`; bounded closure is requested from the shared adapter owner.
This is a remaining geometry blocker, not accepted final topology.

Rifle assembly request `2c5dad23a4ff45c58154bbcfe2f98ee2` created `blender/checkpoints/wf_gun.blend` with 1,032 additional triangles across 31 explicitly modeled closed parts.
The complete candidate totals 29,781 triangles, leaving 219 triangles for small required repairs under the 30,000 ceiling.
The separate rifle retains the source's tapered shoulder stock, chamfered receiver, forged trigger guard, fore-end, green ceramic coil bank, shrouded muzzle and iron sights.
The first actual grip-review action `portal_grip_review` in `blender/checkpoints/wf_grip.blend` was authored by `27ab2022404146f5a17466e6a923b942`, then rendered at the closed-hand phase by `a9de90c286ec4740b307ae4fe75d3880`.
Those native front, right and three-quarter renders show stable pack deformation and a genuine articulated two-hand hold, but the rifle height, head cant and trigger-finger placement require refinement.
The grip-review clip is QA evidence only and is not a substitute for any requested runtime role.
Revision-two rifle/hand preparation is in progress in sibling checkpoints.

Working PBR textures are independently downsampled to 1024 pixels from immutable 2048-pixel provider maps.
Installed `gfx/FX/pdxmesh.shader:478` explicitly reads alpha as glossiness, so the shipping specular candidate is `materials/packed/portal_raider_specular_gloss.png`, with `A = 255 - roughness`, not the superseded direct-roughness alpha candidate.
`material_preparation.json` and `specular_gloss_reconciliation.json` record the source maps, independent scalar-channel resize, channel ranges, shader checksum and corrected output hash.
DDS round-trip and final reimported material review are still pending.

Final assembly must include a separately modeled and controllable retro energy rifle: stock, receiver, grip, trigger guard, coil barrel, shroud and continuous muzzle axis.
The pack must remain rigidly attached to the torso, without arm influences.
Every firing role requires measured trigger grip, support-hand/fore-end contact, shoulder stock contact, muzzle locator and genuine aim/discharge/recoil/recovery.
The body target is 28,000 triangles with 2,000 reserved for rifle/required components inside the existing 30,000 total ceiling.
Texture ceiling is 1024 and shader is `PdxMeshAdvanced` with verified packed maps.

Vanilla precedent is `gfx/models/units/western_european_infantry.mesh`, object `polySurface106` excluding collision, registered by `gfx/entities/infantry.gfx#generic_western_european_rifle_infantry_mesh` and `gfx/entities/units_infantry.asset#infantry_rifle_entity`.
The source height is 7.3518242835; entity scale 0.8 applies once, yielding effective height 5.8814594268; forward is `-Y`, up is `+Z`.
A fresh measured read-only vanilla import is still required with the generated body before export.

The parent explicitly retained all ten roles: idle, move, attack, defend, support_attack, retreat, guard, portal_arrival, wounded and death.
`action_direction.md` records distinct intended role phases and the sound/effect relationship at 24 FPS.
Those planned timings are not accepted motion or final synchronization evidence.
Current adapter capability gaps were sent to `/root/gorilla_blender_repair`, the exclusive shared adapter owner: measured custom rig and explicit weights, separate rigid weapon assembly, safe sibling prepare output, and bounded manual creation of all ten roles.
The current `prepare_candidate` operation writes fixed `00_imported_candidate`, `01_geometry_approved`, `02_materials_approved`, `03_rig_approved` and `05_pre_export` checkpoint names already occupied by preserved pilot history.
It has no output-prefix argument, so this worker has not run it over the current package.
The currently inspected humanoid action tool creates only four hard-coded roles, and its existing-action patch supports only attack, support_attack, defend and retreat.
No template or static/whole-object substitute has been accepted.

## Retained sound and counters

The companion audit found six absent historical footstep OGG originals in both the pilot and legacy roots, although their derived WAVs remain present.
The exact six originals were recovered from the recorded [Footsteps](https://opengameart.org/content/footsteps-0) page by GboxMikeFozzy, which still states CC0 and unrestricted reuse.
They are saved under `attempts/20260906_weaponfree_blender/evidence/audio/`, with source URLs recorded before download in `recovery_sources.json`.
Every recovered original matches its historical SHA-256 exactly.
All 24 original/derived audio hashes and all twelve mono 44.1 kHz signed 16-bit WAV containers pass the retained companion audit.
No audio was authored, synthesized, recorded or changed.
The complete per-file hashes, actual paths and recovery lineage are in `retained_companion_audit.json`.
Other source URLs/attribution/licenses remain in `evidence/audio/licensing/source_ledger.md`.
The existing audio manifest's old “accepted actions” and frame claims conflict with the current blocked model and are superseded for this rebuild; fresh numerical synchronization is pending actual new actions.
Selection must bind through the actual selection consumer, independently of entity idle-state sound.

The two existing bespoke vanilla-green counter DDS outputs still match their runtime copies exactly: large `4236DF5183605AF540D44339EED96F29B2B59A40D9F82E1472C5178963EF920E`; map `FB009C5EEED40C1AAD867D15C066422CB142AA24DC2C38D7311857BFA284D85E`.
The recorded tokens are `unit_portal_raider_icon` and `onmap_unit_portal_raider_icon`, with two 76×42 frames on a 152×42 large strip and two 30×12 frames on a 60×12 map strip.
The installed vanilla definitions/DDS and matching skill-local counter families were consulted, and the existing contact sheet was visually reviewed.
The audit preserves exact installed-reference hashes, alpha ranges and sampled palette evidence.
No new counter art or runtime GFX edits were made.

## Remaining work and cost

### Resume evidence, 2026-09-08

The resume uses the completed fresh body and performs no provider operation.
`resume_preflight.json` verifies the coherent adapter 1.10.25 source checksums, dependency-lock checksum `4263569B1DED51511F5FA869F2CB5FE67D5725CB896431EA8A2CE5A05DD362D2`, and separately listening bridge port 9876.
Health request `0617db4c71a847df9a876c7c1cea1c03` confirms Blender 5.1.2 and loaded io_pdx_mesh mesh and animation exporters.
The selected aiming checkpoint is `attempts/20260906_weaponfree_blender/blender/checkpoints/wf_grip2.blend`, action `portal_grip_review2`, frame 24.
Its side preview confirms shoulder-height rifle presentation, but full-body 512-pixel previews do not resolve final trigger-finger, support-hand and stock contact sufficiently.
A focused upper-torso/rifle/face preview request was sent to the shared adapter owner; contact approval remains pending.

The first explicit low-ready idle action is authored in `attempts/20260906_weaponfree_blender/blender/checkpoints/wf_idle1.blend`, request `8153298438e54cd79fe04e356545a099`.
It has five intentional phases at frames 0, 18, 36, 54 and 72, 24 FPS, with chest/spine breathing and head scanning while both hands retain the rifle.
Native inspection request `1f76524d436d40f0880a6175863dddbd` retains three views at frame 18 under `blender/previews/pwf_idle1_18_*`; the three-quarter view shows stable low-ready carriage and pack shape.
This is a review candidate, with complete multi-phase visual review, contact acceptance, geometry closure and export/reimport still pending.
The same inspection measures zero zero-weight vertices on the working body and rifle, normalized body weights within floating-point tolerance, at most three body influences, and exactly one rifle influence.
It also confirms the read-only vanilla `polySurface106` height as `7.351824760437012` and repeats the unresolved 57 boundary edges on the assembled 29,781-triangle candidate.

`attack_v1_request.json` contains seven explicit ready/aim/discharge/recoil/absorption/recovery/lower phases, and `author_move_v1.py` contains nine measured contact/passing/swing gait phases.
The attack adapter call stopped before execution because shared `blender_worker.py` and `blender_hoi4_adapter.json` no longer matched the published lock during maintenance.
The next Blender call requires a coherent release from the exclusive shared adapter owner; no hash check is bypassed.
`job.yaml` records the selected rebuild authority, preserves the prior acceptance basis separately, restores the required guard role, and corrects the vanilla entity reference.

The coherent 1.10.27 release allowed native attack and move authoring to proceed.
Attack request `a24dd827dad14ecda3b8844e8fef98b8` saved `wf_attack1.blend`, SHA-256 `891245B5F0295B4646D7164990755D6EA5B0E0BE1D9CBAF508DAE5F6C903CBDA`, but its response was lost in transport.
The successful native report was recovered into `attack_v1_response.json`; the subsequent source-preserving overwrite rejection `5d04328a90ae48128f69cad274b05f37` is recorded without repeating successful authoring.
Move request `6732db65580442ba96f9efd6acb8a810` saved `wf_move1.blend`, with nine explicit alternating boot contact, loading, passing and swing phases, frames 0–32 at 24 FPS.
Neither clip is final export/reimport evidence.
The parent reviewed `pwf_grip2_24_three_quarter.png` and accepted the broad shoulder-stock placement, two-hand carriage, head sightline and rigid pack as a working pose; focused finger/trigger acceptance remains pending.

Full native inventory request `886484bb313d42dfbf7b04b1d427dacd` records exact vertices, triangle indices, corner UVs, weights, material slots and normals in `blender/reports/pwf_cap_inventory_v1.json`.
It reveals 245 inconsistent interior edge pairs and eleven orientation contradictions near the small open regions, so the original simple-cap proposal was rejected before mutation.
The exact local proposal in `winding_v2_request.json` and `caps_v2_spec.json` replaces 240 small damaged face-neighborhood triangles with 121 caps and adds no vertices, while explicitly orienting the assembled surface outward.
The indexed proposal has zero boundary, non-manifold and inconsistently directed edges, positive signed volume `10.24848013193483`, and 29,662 assembled triangles.
This is still a caller-data proposal, pending native execution, culling/material/deformation review and export/reimport.
`local_topology_feasibility_v1.json`, `winding_conflicts_v1.json` and `caps_v2_design.json` preserve the exact source indices, failed initial proposals and successful bounded design.

All seven remaining role specifications pass finite measured two-bone reach calculations in `author_remaining_role_v1.py`, with separate defensive firing, advancing support fire, backward withdrawal, sentry scanning, portal landing, asymmetric hit reaction and articulated collapse phases.
They require rebinding to the final repaired checkpoint, native authoring and individual multi-phase review.
The three 1024-pixel final-stage DDS maps exist under `export/20260906_weaponfree_blender/textures/`.
`material_dds_v1.json` proves decoded RGBA equality to each selected packed PNG, including `normal.G`, `normal.A` and inverted roughness in `specular.A`; native material binding and reimport review remain pending.
The coherent 1.10.32 adapter is available and native work has resumed; earlier winding attempts remain preserved as failed evidence.

Current Meshy spend: **30 credits**, explicitly confirmed by the completed provider task.
Coordinated reservation: 75 credits; initial body estimate 30, optional remesh estimate 5; Meshy rigging and animation calls are prohibited for this firearm route.
Fresh provider body geometry, PBR textures, task lineage and immediate artifact checksums exist.
The new body, rig, weights, separate rifle, grip review, six native action candidates (idle, move, attack, defend, support attack and retreat) and packed DDS maps exist; final material binding and action review remain pending.
Focused contact review, bounded boundary closure, all ten accepted semantic actions, final export bytes, reimport proof and exact runtime/audio synchronization remain incomplete.
The historical package and runtime remain preserved.
No simplification was accepted and no in-game validation or runtime completion is claimed.

Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and native `imagegen`.
No skill, shared adapter, config, dependency lock, gameplay, entity/GFX, localisation, spreadsheet or runtime file was edited.

### Native continuation, 2026-09-08

Six native action candidates are recorded in `attempts/20260906_weaponfree_blender/action_progress_20260908.json`: idle, move, attack, defend, support attack and retreat.
Support attack preserves two distinct discharge/recoil cycles at frames 18/21 and 40/43; its saved checkpoint was recovered from the native report after transport ambiguity, with matching SHA-256 `068C39036C566C893C126B520DAC5EFBE1D39D5EDC5CF39C002070932884D010` and no duplicate authoring.
Retreat is a nine-phase backward contact cycle, native request `5125cb899bc648c6a448a8e7af401b3f`.
The action candidates require full multi-phase deformation/contact review and export/reimport before approval.

Outward winding repair passed native save and reopen through coherent adapter 1.10.32, request `63cef30c2a2d4c59a19e8ca2be5d1cf7`.
The checkpoint is `attempts/20260906_weaponfree_blender/blender/checkpoints/wf_winding3.blend`, SHA-256 `308188B2A95A607CC01F51A167C38B09ED1930C9015DB8C0B21B109582119EDA`.
Positions, corner UVs, rig, weights, actions and materials are preserved.
The measured worst normal quantization is 0.180851 degrees within the parent-approved 0.25-degree native directional tolerance; nine selected unset source corners use their own valid geometric face normals, with exact evidence in `winding_v3_response.json`.
This intermediate checkpoint intentionally retains the original 57 boundary edges and 59 winding conflicts on faces scheduled for replacement.
The prepared `caps_v3_request.json` applies the exact 240-face removal and 121-triangle replacement from `caps_v2_spec.json`; its native execution remains pending.
The indexed proposal yields 29,662 assembled triangles, closed manifold topology and positive volume, but those numerical predictions do not substitute for native repair/reimport evidence.

No portal Blender call remains active after the winding receipt.
New heavy calls are paused under the shared resource hold until the adapter owner releases capacity.
`audio_phase_draft_v1.json` maps retained licensed recordings to the authored phases and explicitly remains pending native contact and final export review.
Guard, portal arrival, wounded and death have measured explicit phase specifications and await native execution after repair.
No additional provider call or credit spend occurred in this continuation.