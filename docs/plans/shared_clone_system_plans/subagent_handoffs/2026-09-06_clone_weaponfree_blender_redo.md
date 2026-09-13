# Clone infantry weapon-free Meshy 7 and Blender firearm rebuild

Status: in progress.
The parent approved exact prepared-input SHA-256 `1941ab6df4b4422d92fbdee69dc81da965d5127b14756f7ac5c34a0f7ba3b4c9` after comparing it against the immutable original soldier reference.
The parent released the temporary provider hold after reviewing the installed io_pdx_mesh compatibility changes; binary and skin layout behavior were unchanged.
Meshy 7 body task `01a07650-77c9-7244-ad86-b0434c78452c` succeeded and consumed 30 credits from this worker's 75-credit reservation.
Its approved sole input was used with `ai_model = meshy-7`, T-pose, PBR, triangular integrated remesh at a 28,000-triangle target, GLB and FBX output, and no Meshy rigging or animation.

The accepted scope is `docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md`.
The deterministic model root is `docs/assets/shared_clone_system/models_3d/clone_infantry`.
All production evidence belongs to `attempts/20260906_weaponfree_blender/`, the sole approved input is `refs/derived/20260906_weaponfree_body.png`, and replacement export candidates belong to `export/20260906_weaponfree_blender/`.
Prior body, rifle, action, runtime, audio and counter sources remain preserved.

## Evidence available

- `attempts/20260906_weaponfree_blender/input_manifest.json` records source identity, hashes, exact ImageGen prompts, native-alpha failures, fallback and explicit parent approval.
- `attempts/20260906_weaponfree_blender/alpha_fallback.json` records installed rembg 2.0.61, checksum of its existing isnet model, alpha settings, 1122×1402 RGBA output and review files.
- `attempts/20260906_weaponfree_blender/dependency_preflight.json` records matching package/integrity/archive/adapter checks and the separate listening probe for bridge port 9876.
- Four `meshy_schema*.json` receipts prove exact `meshy-7`, two consecutive and two concurrent wrapper probes, idempotent SDK entry bytes and no surviving owned process IDs.
- `attempts/20260906_weaponfree_blender/blender_schema.json` and `blender_health.json` record 28 actual operations, Blender 5.1.2, loaded io_pdx_mesh exporters and adapter 1.10.21 health request `a81985e1638642be8ef8c5411407b65b`.
- `attempts/20260906_weaponfree_blender/action_plan.md` records the nine consumed roles, separate rifle/bolt controls, contact requirements, initial phase plan, source height/entity scale and preserved audio/counter companions.
- `attempts/20260906_weaponfree_blender/provider/` preserves exact paid requests, redacted responses, task inspection, downloads, checksums and credit reconciliation.
- `attempts/20260906_weaponfree_blender/provider/downloads/clone_weaponfree_meshy7.glb` is 9,698,156 bytes with SHA-256 `bd9322faa168b217b141ebd5462e255e268528ba65485c9641a6d1d391e626de`.
- `attempts/20260906_weaponfree_blender/provider/downloads/clone_weaponfree_meshy7.fbx` is 14,132,604 bytes with SHA-256 `44ee8f57dc7fab739869739a475ea4d0c5943125e54fc8e18f4b22b6c57c73ed`.
- `attempts/20260906_weaponfree_blender/parent_dependency_release.json` records the paid release and the alien worker's source-comparison evidence SHA-256 `bcbcf4482639180dda8651896e1c0a05f2816f18705d6999e6ff2c1ce30195d9`.
- `attempts/20260906_weaponfree_blender/preserved_companions.json` and `audio_source_review.md` record existing runtime sound and counter bytes; `recovered_audio_sources.json` proves exact-hash recovery of the five missing original 2011 recorded soldier-voice OGG files.
- `attempts/20260906_weaponfree_blender/blender_schema_1_10_24_1edf5e73.json` records the parent-released 40-operation adapter 1.10.24 schema and matching source locks; health request `f0061f31419e47f980538f3665067fc7` verifies Blender 5.1.2 and loaded io_pdx_mesh.
- `attempts/20260906_weaponfree_blender/working_pbr/blender/checkpoints/05_pre_export.blend`, SHA-256 `57157251b5765059993fef0e7277f94d0f27ddc03a204cbf052cb300b7b92670`, is the selected body working import with conventional provider PBR preview maps.
- `body_pbr_geometry_comparison.json` proves that corrected preview materials preserve every source vertex, triangle and UV corner from the first import; front, rear, left, right, top and three-quarter views were personally reviewed.
- `material_preparation.json` and `dds_manifest.json` record six pixel-exact BGRA DDS maps, correct RRxG normal packing and specular alpha glossiness, with immutable provider maps retained.
- `rig/clone_fitted_rig_spec.json`, `rig_draft_v1_response.json` and the source-preserved `clone_weaponfree_rig_draft_v1.blend` checkpoint record 44 measured bones, 23 explicit skin regions, zero unweighted vertices, at most four influences and zero rest-geometry displacement.
- `components/geometry_design_report.json`, `component_texture_manifest.json`, `component_texture_prompt.txt` and the four `assemble_*_response.json` receipts record the separate 600-triangle stock, steel parts, bolt and sling package.
- The assembled working checkpoint is `attempts/20260906_weaponfree_blender/working_pbr/blender/checkpoints/clone_weaponfree_assembled_4.blend`, SHA-256 `0e757477d780a7958ec3b27d7ba3f39c37a37858ae58791e478a5afb0409e2c2`, with 29,729 total triangles across body and four rigid components.
- `rig/clone_clothing_patch_spec.json` and `clone_clothing_patch_design.json` prepare exact centroid caps for three tiny clothing seam holes; their 13 added triangles would bring the complete assembled package to 29,742 triangles.

The initial dependency receipt verifies the locked archive and installed manifest; it does not establish equality of every installed exporter source file with that archive.
The parent accepted the documented installed Python 3 and Blender compatibility modernization; final actual-byte mesh/action export and reimport remain mandatory before promotion.

## Scope and remaining work

### 2026-09-08 resumed production

The resumed worker uses the same immutable Meshy 7 body and spends zero additional provider credits.
The final rig candidate is `attempts/20260906_weaponfree_blender/working_pbr/blender/checkpoints/clone_weaponfree_rig_v3.blend`, SHA-256 `f3b6a4155b041d74bed41493d27e2b4b6aa4c5b31e189939d6bd065a10104e59`.
Its 44 measured rest-bone transforms and 23 skin regions preserve the 29,129-triangle body without vertex displacement; independent hand controls are parented to Chest and both measured IK poles follow Chest, preventing fixed-world poles during collapse.
The actual rig inventory is `evidence/clone_weaponfree_rig_v3_rest.json`, SHA-256 `ad1c951fa8bae09c3fcd9bb8bcb35eeacbcf4deec8476387994e61f6a2d10c66`.
The original successful rig receipt is `logs/adapter/2a3fc0554ed5458f9d716a7d092bef00.result.json`; a transport retry returned an existing-output rejection, and `attempts/20260906_weaponfree_blender/rig_v3_recovered_receipt.json` proves recovery without repeating the mutation.
The job-owned dispatcher now uses one `call_stdio` dispatch through the verified repository wrapper and stops on uncertain transport rather than automatically retrying mutations.

Body checkpoints contain personally authored idle, move, attack, defend, support_attack, retreat, training and wounded v3 actions, plus death v5 with an independently keyed buckle, fall, impact and settling sequence.
The action-bearing source for assembly is `attempts/20260906_weaponfree_blender/working_pbr/blender/checkpoints/clone_weaponfree_training_v3.blend`, SHA-256 `83e013edfe1bfb4ed575db882e1edff8fb32059656f039fc58243f7698dacaff`; its successful request is `19c8141d15a84049bd6b115fc0cc0415` under adapter 1.10.31.
All actions retain editable authored curves plus native-IK baked curves, at 24 FPS, with individual specs, contact plans and receipts in the attempt folder.
None is promoted to final semantic acceptance until the complete assembly passes multi-frame review and actual-byte export/reimport.
Adapter 1.10.31 added fitted training phase support, and the distinct 73-frame training v3 action succeeded under request `19c8141d15a84049bd6b115fc0cc0415`.
Actual per-frame contact audit then identified a 0.130-unit right-wrist shortfall in training v3 and a 0.092-unit left-wrist shortfall in retreat v3.
The personally revised retreat v4 and training v4 actions succeeded on the assembled source under requests `08c6b95aaa504225b44a15da697785d0` (adapter 1.10.34) and `0c39c30639c4462a89ba8732b086276f` (adapter 1.10.35).
Their maximum measured wrist errors are 0.000099484 and 0.000232638 source units respectively, replacing the rejected v3 grip candidates.
The corrected training checkpoint SHA-256 is `2e016e2a765ded6c9a0079a59558256166653a475935c7693bc784741c818843`; its ready/present/inspect/recover phases are frames 1/19/43/73 at 24 FPS.
The other seven roles have maximum measured native IK wrist error at or below 0.000262 source units.
Death v1/v3/v4 are superseded settling drafts; death v5 is the current candidate, with floor-region request `db39fadf843d4fda93a05eb7321e833c` proving 272 posed source-index vertices within 0.1 units of ground and minimum returned Z of 0.0000004768.
This numeric contact proof does not substitute for complete assembled multi-frame review.
The measurements and exact source report hashes are in `attempts/20260906_weaponfree_blender/authored_contact_audit.json`.

The finite assembly sequence `run_final_assembly.py` attaches the exact existing wood, steel, bolt and sling components, applies the explicitly authored three seam centroids and 13 triangles, then binds the six verified DDS maps.
The v4 attachment was rejected by save/reopen fingerprint comparison and is preserved as rejected evidence.
The v5 wood, steel, bolt and sling attachments all passed the repaired save/reopen proof, with respective request IDs `fd13f2004a084065b6c895791517c0e0`, `7f7aa7fdbe434da98ae57a3d047e89b8`, `6117bdb5b06443778822780dc0448454` and `cc4e52647bf343ccba3efb00abd51dd6`.
The complete action-bearing pre-cap assembly is `attempts/20260906_weaponfree_blender/working_pbr/blender/checkpoints/clone_weaponfree_assembled_v5_4.blend`.
It preserves the 29,129-triangle body and 600-triangle separate rifle package, totaling 29,729 triangles before the 13 seam-cap triangles.
The v5 seam patch succeeded under adapter 1.10.32 request `3bd45f9058054a7aa65a0c667f5392de`, producing `attempts/20260906_weaponfree_blender/working_pbr/blender/checkpoints/clone_weaponfree_capped_v5.blend`, SHA-256 `212e98f1d7ec0415af7a5e343ff7c67818cd57f96648260f17856324d684e30c`.
The report records 29,742 triangles, 14,852 vertices, zero boundary edges, zero non-manifold edges, zero degenerate faces and unchanged bounds, with retained positions, weights, UVs, rig, actions and materials preserved and save/reopen proof passed.
The initial resource hold drained all clone calls before the parent explicitly released one slot for the bounded material, grip-correction and locator tranche.
The parent release allowed removal of the clone-only hold sentinel; this tranche dispatches only one heavy call at a time.
Packed material binding succeeded under adapter 1.10.33 request `45c5389781c447c2bfa573c5da8a9328`, checkpoint `attempts/20260906_weaponfree_blender/working_pbr/blender/checkpoints/clone_weaponfree_material_v5.blend`, SHA-256 `ae4037d645dc226b94aa0cb3b60441daba00d5fcf3f36cd541e197d73c270ce1`.
The corrected grip actions and both rifle locators are saved and numerically verified; complete semantic/contact/material review, exports, reimports and runtime-copy manifest remain unfinished.
The current complete assembly source is `attempts/20260906_weaponfree_blender/working_pbr/blender/checkpoints/clone_weaponfree_cartridge_v5.blend`, SHA-256 `c066ebaa61daea1c557ec656ba02e20ec6561818cc9ef7e725ee90762c48fef4`.
Muzzle request `bbefeea453e047e5a19ed516672a800f` and cartridge request `b0f276f3e5514623a96b2e650fee078f` bind the registered locators to RifleControl; both succeeded under adapter 1.10.35.
Native full-assembly views of training frame 43 and retreat frame 13 were reviewed under requests `b364b2cff2234709a060f52ea4781f9e` and `6b9515e642944c3c987dfb40dcd8d78d`; the corrected holds and packed materials look coherent in these bounded views.
The exact source hash remained unchanged after both read-only reviews; the runtime meshes have zero unweighted vertices, at most four influences and 29,742 triangles with zero open/non-manifold edges.
`attempts/20260906_weaponfree_blender/bounded_material_grip_locator_review.json` records this limited acceptance and remaining work; no full action, export or runtime acceptance is implied.
This bounded tranche has drained and the Blender slot was released to the parent for Portal, with zero queued or outstanding calls.
The exact firing-state timing and existing vanilla particle/light/sound identifiers are in `attempts/20260906_weaponfree_blender/firing_synchronization_draft.md`.
The locator and per-frame review request preparations are job-owned declarative helpers; their completed bounded outputs and validation limits are recorded above.
The shared adapter owner retains all shared source/lock maintenance, including fingerprint and normal preservation fixes.

Consumed roles are idle, move, attack, defend, support_attack, retreat, training, wounded and death.
The parent excluded the unconsumed historical entrain wish from this redo.
The body target is 28,000 triangles beneath the historical 30,000 total after separate rifle addition.
The source body height is 7.3518242835 with a single runtime scale of 0.8 and effective height 5.8814594268, matching installed western European infantry without collision geometry.
The preserved original defines one period-compatible bolt-action wood-stock rifle and identity-neutral uniform/kit.

Fresh Meshy 7 body generation and immediate GLB/FBX download are complete.
Body views, source/working checkpoints, measured draft rig, all separate firearm components and final packed DDS maps exist.
The three tiny clothing seam loops are closed in capped_v5; final visual and export/reimport review remains required.
The underside preview preset was occluded by its ground plane and is not accepted as underside proof.
Complete multi-frame rig deformation and firearm-phase review, exact firing/audio synchronization and actual-byte export/reimport remain outstanding; material binding and numerical contact checks are complete.
The current attack v3 choreography passes the numerical hand-contact audit; final assembled aim, discharge, recoil and recovery review remains required.
This worker owns the explicit cap and material requests; the shared recovery owner owns their adapter implementations and locks.
The inherited rifle audio source is explicitly described by its publisher as an Audacity simulation using popped balloons, so it fails the current recorded-source-only audio rule.
The parent directed this worker to preserve runtime audio and record this as a separate unresolved companion gap without delaying the physical model repair or researching a replacement in this tranche.
Technology Tree Viewer availability is unverified and outside this model-only scope.
The parent owns runtime copy promotion, `.gfx`, `.asset`, entity, action, particle/light/sound/voice wiring and final acceptance.
No in-game completion is claimed.

Skills used: chaos-redux-3d-model-pipeline, chaos-redux-event-assets, chaos-redux-subagents and imagegen.
No skill or shared adapter/configuration file was edited by this worker.

### Final sequence rejection and prepared death v6 correction

The final assembled death v5 impact/settling views at frames 37 and 61 are rejected: both boots and much of the lower body remain visibly raised in a rigid horizontal pose.
`attempts/20260906_weaponfree_blender/death_v5_visual_rejection.md` records the native evidence and explicitly supersedes any implication that sole-back contact approved final settling.
The parent authorized a data-only correction using actual native source vertices and weights across head, upper back, pelvis, both calves and both boots, while preserving rifle/fingers and the other eight actions.
`death_v6_surface_fit.json` measures the rejected v5 pelvis gap at 0.30118 source units and boot gaps at 0.26448/0.13887 above back support.
The fitted candidate reduces head/pelvis gaps to 0.03557/0.04546 and calf/boot gaps to 0.01314–0.01722; these analytical values are draft evidence only and require native posed-region and visual acceptance.
`actions/death_v6_spec.json`, `death_v6_design.json` and `death_v6_call.json` prepare the bounded candidate without mutating the current checkpoint.
The scheduler has been notified; no native candidate or export has yet been dispatched after this rejection.
Attack, defend and support_attack have complete bounded phase views with coherent standing, guarded and kneeling firing silhouettes; remaining nonfiring full-sequence views are unfinished.
### Parent-accepted death v6 source

The v6 native candidate succeeded under adapter 1.10.40 request `264e86d443494831a5a6ffbad69022e9`.
The selected source is `attempts/20260906_weaponfree_blender/working_pbr/blender/checkpoints/clone_weaponfree_death_v6.blend`, SHA-256 `90fd3f31ef0e95a101e40bae0e3e44ffcf9d664131ccd14dc5946a75c58f2afd`.
The parent viewed final61 left/three-quarter and explicitly accepted improved broad support with retained rifle, native 521 near-floor vertices and the exact 14 source-index supports spanning all seven body regions.
Native request `ffed7fefbcea4da18fed61cfe93d0465` requires every one of the 14 measured source indices to lie within WORLD Z -0.01 to 0.075 independently of pagination; its seven-region support centroids are at Z 0.020778 and 0.022997.
Maximum actual wrist IK error is 0.000249023; geometry/UV/material preservation passes and the other eight selected action summary records remain identical.
`death_v6_native_acceptance.json` and `final_source_selection.json` record the acceptance basis, exact source and selected nine actions.
The parent forbids further death pose edits absent actual failure and authorized final sequence checks plus mesh/nine-action export/reimport through the scheduled slot.
No final runtime or in-game completion is implied by source acceptance.