# Bounded adapter recovery draft

Status: first tranche published as adapter 1.10.24 after parent review and exact baseline recheck; dependency lock refresh and actual Blender route tests remain parent coordinated.
The parent accepted the schema scope, requested BGRA/packed-map corrections, granted publication, and owns lock review, runtime evidence and commit.
Drafts are in `docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/`, with `recovery.patch`, exact source `baseline_hashes.json`, staged Python files, and draft-only build/validation scripts.

## Proposed interfaces

- `export_mesh` adds optional `checkpoint_rel`; when supplied it must be a new sibling `.blend`, checked before export, preserving the accepted `06_exported.blend`.
- `promote_accepted_reimport` permits 1–512 explicitly named meshes; existing complete receipt matching, same-rig validation and exact save/reopen fingerprints remain mandatory.
- Measured rig and component operations create an empty local `WORKING` collection only when approved local working objects exist; existing objects stay in their existing collections and promotion stays metadata-only.
- Weight regions accept optional `mesh_names` as an exact bounded list, allowing overlapping rigid props and body regions to be distinguished without changing geometry.
- Component specifications accept optional `material_spec = {shader: PdxMeshAdvanced, normal_packing: RRxG, specular_packing: rgb_specular_alpha_glossiness, maps: {diffuse: {path_rel,sha256},normal: {path_rel,sha256},specular: {path_rel,sha256}}}`.
- New component materials and images require unique names, job-contained DDS files and matching SHA-256, matching bounded texture dimensions, alpha-capable packed maps, fixed existing PDX shader bindings and no caller shader code.
- `repair_explicit_mesh_winding(job_id, blend_rel, checkpoint_rel, expected_source_sha256, mesh_name, face_indices)` flips only the explicit reviewed triangle list, preserves per-vertex corner UV association, geometry positions, weights, material bindings, rig and all action fingerprints, and recomputes geometric normals.
The distinct name preserves the concurrently published `repair_mesh_winding` planner and `mesh_winding_repair.py` without changing their contracts.
- `ground_existing_action(job_id, blend_rel, checkpoint_rel, expected_source_sha256, target_armature_name, source_action_name, expected_action_sha256, target_action_name, root_bone, excluded_contact_bones=[])` copies an explicitly hash-bound action, preserves original actions and all non-root curves, measures the full root-location world basis per frame and corrects world Z without lateral displacement.
- Existing measured action contact uses root-local translation instead of rig-object location; Euler/quaternion source mode remains unchanged.
- `action_provenance` accepts manual GPT-6-astra actions only with retained source-checkpoint and declarative-spec SHA-256, without pretending they are provider actions.
- Animation export report filenames use a bounded action prefix and hash suffix to avoid the observed Windows path-length failure.
- `reimport_export` adds `stage_default_textures=True`; explicit `False` preserves caller-prestaged adjacent DDS candidates and records every retained file hash instead of overwriting corrected maps from old job defaults.
- Component DDS validation accepts exact A8R8G8B8/BGRA bitmasks and payload sizes, or alpha-capable BC3/BC7, with a maximum 1024-square unit canvas.
- Component previews decode specular G into strength, B into metallic, and one minus alpha into roughness; packed normal G/A reconstruct tangent X/Y/Z through a fixed node graph.
The exporter still discovers the original engine-packed map filenames by its installed first-linked-input traversal; no source DDS pixels change.
Normal preview mapping follows installed `io_pdx_mesh` G/A-to-Blender-tangent mapping and reconstructs Z.
The engine's `UnpackRRxGNormal` additionally negates decoded Y in its own tangent convention; equivalence across exported UV/tangent conventions still requires actual comparison and is not asserted from the node graph alone.

## Source and validation

Required AGENTS, offline wiki core pages plus Entity/Graphical asset pages, 3D pipeline/event-assets/subagents skills and dependency/config files were consulted.
The installed `gfx/FX/pdxmesh.shader` improved Blinn–Phong branch reads specular alpha as glossiness and `UnpackRRxGNormal`; the component builder preserves those engine channels and the existing exporter Roughness socket convention.
The repository adapter baseline is 1.10.22, Blender line 5.1.2, io_pdx_mesh 0.91.0 with dependency archive SHA-256 A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2.
Concurrent `split_verts`, fitted humanoid repair and skeletal partition changes are preserved.
Draft syntax and existing declarative rig/component/action rejection tests are run against staged files, plus optional exact-mesh region rejection cases.
No Blender inspection, mutation, export or reimport was run by this worker during the draft/publication phase.
No Meshy operations or credits were used.

## Release and unresolved scope

The three adapter Python files and config were published after baseline validation; only `repair_explicit_mesh_winding` and `ground_existing_action` were added to the config allowlist.
Exact published hashes are in `adapter_recovery_drafts/published_hashes.json`.
Changed functions: worker `_promotion_inputs`, `export_mesh`, `action_provenance`, `export_animation` report path, `reimport_export`, and manual-operation dispatch; MCP export/reimport signatures and the two added tool declarations; manual `validate_regions`, `validate_component`, `author_measured_creature_rig`, `attach_rigid_component`, `author_measured_creature_action`, plus bounded recovery helpers and the two operation implementations.
The parent must refresh dependency-lock version, operation list and reviewed hashes before release to asset workers.
The parent subsequently verified and released the coherent 1.10.24 dependency lock with 40 operations, then requested broadcast to all active model workers.
The release was broadcast to all 14 active model workers, including the forest child, with requests for actual request IDs and errors.
Actual success feedback includes measured rigging, dedicated component materials, recovered-death root grounding and source-action preservation; package owners retain the actual export/reimport and visual evidence.
The live manual contract tests passed 4 cases and promotion contract tests passed 29 cases after publication.
Tool listing and Blender job-level tests are still required after publication; source tests are not export or engine evidence.
The proposed winding operation deliberately does not fill boundaries or repair non-orientable topology.
Temporal Guard's measured 66-face inner-thigh reconstruction, small source boundary caps, the assault unit's existing prop split/rebind and preview-only packed-map decoding are additional concrete requested operations not implemented in this first draft.
Material pixel packing is declared and hash-bound; semantic texture/palette review remains with the asset owner.
No asset package or in-game completion is claimed.

## September 8 recovery releases and native evidence

Status: implemented bounded adapter releases through 1.10.31; native package work remains owned by each model worker and the parent.
No Meshy calls, credits, runtime wiring, asset-job edits, or commit were made by this adapter worker.
Used AGENTS, offline core/graphical references, installed shader/documentation, and the 3D pipeline, event-assets, and subagents skills.
The parent explicitly approved the third tranche, finite missing-image sentinel, dependency-graph persistence correction, custom-normal preservation, and fitted training semantic tuple.
The concurrent external 1.10.26 `explicit_skin_repair` and `preview_explicit_skin_selection` addition was reviewed by the parent and preserved without reverting it.

- `third_tranche/published_hashes.json`: 1.10.27, 45 operations, 48 contract tests passed; exact vertex positions/weights and existing PDX material rebind added.
- `fourth_tranche/published_hashes.json`: 1.10.28, 20 contract tests passed; exact missing-image sentinel added for inherited empty vanilla texture datablocks, without invented pixels or material-validity claims.
- `fifth_tranche/published_hashes.json`: 1.10.29, 21 contract tests passed; image dimensions resolve before metadata snapshot, and file-backed decoded-cache load state no longer causes a false image mutation while file path/checksum/source/settings remain protected.
- `sixth_tranche/published_hashes.json`: 1.10.30, two targeted tests passed; exact winding preserves unaffected corner normals and negates selected corners, verifies source association and native save/reopen normal signs.
- `seventh_tranche/published_hashes.json`: 1.10.31, two persistence tests passed; evaluated bounds are refreshed before save fingerprints, exact object-field deltas accompany failures, fitted training accepts ready/present/inspect/recover, and normal failures report their worst corner vectors without increasing the 0.001 tolerance.

All release manifests above are relative to `adapter_recovery_drafts/`.
They retain exact source/config/lock SHA-256 values, baseline evidence, staged source, and test artifacts.
Publication checks the current full lock before replacing reviewed source, then replaces the lock atomically and retains concurrent unrelated fields.
Blender remains the lock-selected 5.1.2 and io_pdx_mesh remains the existing checksum-locked installation; these adapter changes do not replace either dependency.
Bridge read-only evidence found 127.0.0.1:9876 listening under PID 21564; the additional PID 25632 was left intact, with no unrelated processes terminated.

### Usable operation contracts

`chaosx_blender_hoi4_edit_explicit_mesh_vertices(job_id, blend_rel, checkpoint_rel, expected_source_sha256, mesh_name, target_armature_name, vertex_edits)` accepts 1–20000 exact existing rows `{index, world_position?: [x,y,z], weights?: [{bone,weight}]}`.
Weight targets must be existing deform bones and existing groups; each row has 1–4 explicit positive normalized weights, with no automatic normalization or bone creation.
Requested values are read back with bounded float tolerance, untouched vertex fields/topology/UVs/rig/actions/materials are checked, and a new sibling checkpoint requires save/reopen proof.
Position changes retain source custom normals and require owner review; this is not a prop-extraction or automatic normal-rotation operation.

`chaosx_blender_hoi4_bind_existing_pdx_material(job_id, blend_rel, checkpoint_rel, expected_source_sha256, target_mesh_names, source_material_name, material_name, material_spec)` replaces only the named source slots on exact local unshared working meshes.
The new material uses the existing component material specification with job-relative DDS paths, SHA-256 values, PdxMeshAdvanced, RRxG normals and rgb_specular_alpha_glossiness.
Original material/maps remain preserved; the original material gains an explicit fake-user retention flag so it survives save/reopen after rebinding.
The operation does not declare semantic map correctness or final shading acceptance.

`repair_explicit_mesh_patch` and full rest landmark inventory from 1.10.25 remain available through the locked stdio wrapper.
Live session tool exposure can lag a newly published wrapper; owners discover the actual stdio tool list and use `BlenderAdapterClient.call` with its structured schema.

### Reported native successes

- Stone winding `c8f62b26c78b463ba8d0187cda048e0c` on 1.10.29 saved checkpoint02 SHA-256 `786E823DF081792F29DE9090E79B3BBA9666AA48D35E653A60254766F5FB56BD`.
- Stone two local patches completed under receipt `90335577811242b089f4321539f83c0b`, checkpoint04 SHA-256 `9BD45037B602185CC82B0ED6383E2265794800818F1117E9056D86286BD9602F`; rig rebuild `a0a0ffe0c23c490199943226663bd321` reports closed 23800-triangle geometry.
- Gorilla exact smoothing succeeded with native save/reopen proof in `60_smooth24_br26.blend`; owner evidence `smooth24_v29_result.json` retains the exact receipt.
- Alien exact cap request `fc244f372f7c4e53802aa3963b9738df` saved `21_body_caps_working.blend`, preserving positions/weights/UV/rig/actions/materials and missing-image persistence proof.
- Robot material rebind `4ceb31e8944846e9b576ea1fcb4bedbf` saved `31_material` SHA-256 `9E503301B23A79B9E48079D608446CC6A13E65F8E2EE3AC8E822D255AA3C64DA`.
- Zombie variant exact 17-face winding `9f92c49341284206a8fd0160d9166026` passed native source and reopened normal preservation.
- Temporal original-source winding `d943fc9e775d44e2b65f6b2592468ea1` passed image persistence and source preservation under 1.10.29; that earlier normal policy recomputed normals, so it does not prove the later corner-retention contract.

These are owner-reported native receipts, not independent adapter-worker reruns or final package acceptance.
Model-level visual, action/contact, export/reimport and runtime evidence remain with the package owner and parent.

### Remaining bounded work and rejected results

Parasitic exact-weight request `73ca42e5c6764c09aa439b5906efab8b` failed objects-only save/reopen preservation; 1.10.31 adds an evaluated-bounds flush and exact field diagnostics, pending a new native result.
Stone/clone attachment save/reopen mismatches are also pending the 1.10.31 native checks.
Temporal, undead and Pan native normal encoding exceeded the retained 0.001 vector tolerance with errors approximately 0.001513, 0.002413 and 0.003616; outputs remain rejected and 1.10.31 records worst-corner data for diagnosis.
No wider tolerance or global normal clearing was substituted.
The parent approved queued finite robot vertex-fan splitting, donkey calibrated whole-assembly yaw, bounded focused preview ROI, and disabling automatic mutation retry after uncertain transport.
Those capabilities are not implemented by these releases and must not be inferred from the released tool list.
Transport drops can occur after successful native saves; package owners preserve the first result and do not repeat a mutation merely because a wrapper response was lost.
No asset or in-game completion is claimed.


## 2026-09-08 authoritative continuation: released 1.10.37

Disposition: implemented adapter routes, with native asset acceptance tracked separately.
Parent authorized every bounded tranche below; no Meshy operation or cost occurred, no runtime files edited, and no commit made by this worker.
The current dependency inventory is `adapter_recovery_drafts/tenth_tranche/released_dependency_inventory.json`; it lists every released source hash and tracked/untracked status needed for a coherent parent-owned commit.
Preserve external `explicit_skin_repair` and other existing operations.
Unreferenced external `mesh_winding_seam.py` and `pdx_skin_membership.py` are excluded from this release inventory and remain untouched.

- 1.10.32: measured 0.25-degree normal direction serialization tolerance, selected unset-normal sentinel policy, no global custom-normal reset.
- 1.10.33: normalized desired normals before native encoding; read-only evaluated camera framing and optional finite world AABB/resolution; uncertain mutations no longer automatically retried by BlenderAdapterClient.
- 1.10.34: explicit request angular_tolerance_degrees up to 0.5, default 0.25 preserved, for measured Gorilla 0.493285626-degree native encoding drift; existing body material binding inherits up to2048 dimensions from retained original atlas while component default stays1024.
- 1.10.35: finite exact source vertex fan duplication and coincident alias corner remapping, explicit unused-vertex removals, unchanged triangles/positions/fullweights/cornerUV/normals/materials/rig/actions, forward/reverse maps, save/reopen proof.
The lock operations array was initially omitted from this additive publication; corrected before native acceptance to match46 config operations.
- 1.10.36: explicit rigid world-Z assembly yaw, selected working parent/descendant closure, no geometry bake, all requested integer action frames compare every evaluated working vertex to rotated source within2e-5, protected source untouched, full save/reopen.
- 1.10.37: native Robot receipt0478b3eb52044dc8bf465bf8d959261e rejected before save because BMLoop.copy_from invalidated the loop wrapper.
Removed redundant loop.copy_from and its unused scratch layer; UV and normals remain independently reconstructed/read back from declared source face/corner.
Native37 retry is pending; no Robot remap checkpoint is accepted yet.

Current lock SHA256: `512F41E60A1A76887BAE62A5B4577140F2E407CFF54EB31DB30637EDCB5EE90F`.
There are47 operations in both config and dependency lock.
Release manifests/baselines reside in `tenth_tranche/gorilla_release`, `remap_release`, `yaw_release`, and `remap_loop_fix`.
Focused tests: `python docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/tenth_tranche/test_gorilla_limits.py` (3), `test_remap.py` (5), `test_yaw.py` (3).
These are validator/serialization fixtures; actual Blender proof belongs to native asset requests.

Native evidence received: Gorilla exactweights60 passed; parasitic exactweights request87e7c915160d4867933e8bda27e89c06 passed after dependency-update fix; Clone rifle attachmentfd13f2004a084065b6c895791517c0e0 and training19c8141d15a84049bd6b115fc0cc0415 passed; Clone caps3bd45f9058054a7aa65a0c667f5392de closed13 boundaries.
Alien capfc244f372f7c4e53802aa3963b9738df passed and all7 actual-byte action reimports drained successfully; parent owns runtime audit.
Temporal all10 actual-byte reimports drained and parent integrated commitde0d91057.
Robot partition6fb0f6c76fe04399a1f5fbcff0c85f57 and material4ceb31e8944846e9b576ea1fcb4bedbf passed, finite fan repair remains pending.
Pan cape8734d0ea1f44d338014c33eb019bdf5 gives24916tri/zero boundary/nonmanifold/degenerates; River capd5a223... gives24964tri/zero boundaries with preservation.
Portal outward winding63cef30c2a2d4c59a19e8ca2be5d1cf7 and subsequent exact caps passed; all10 roles exist but final contact review remains owned by Portal.
Donkey materials4691c8045cff4ec3aaf8a86faff3ee9e and partitiona9c92301966e480da1618a18174de34a passed; yaw native proof remains pending.

Resource discipline: at most3 heavy Blender calls globally and one per released owner; never kill active renders and never retry uncertain mutations.
Million-vertex protected provider meshes explain some expensive full-scene fingerprints; working-only yaw sampling explicitly excludes them.
At this entry the reserved slots are Gorilla, Donkey, and one Robot remap retry; other owners must request rotation after a drain.
Remaining blockers: native Gorilla34+ winding/material proof; Robot37 lifecycle proof then exact caps; Assault alias proof/extraction and reviewed nonplanar body closure; Donkey yaw/export/reimport axis proof; remaining owner contact/deformation QA.
No in-game completion or asset completeness is claimed by this adapter handoff.


### Subsequent native proof and current 1.10.38 lock

Gorilla winding70 PASSED native and reopened proof in1.10.37, request `f187af380a65452ca4245b2ff34a4062`, checkpoint SHA `BED028758760BE427F6FD8DA70D2B85692887D2787C8AF5D8E7422C15A25323B`.
The maximum0.493285626-degree encoding difference was identical before/after reopen; positions/cornerUV/rig/weights/actions/materials preserved.
Prepared topology patches remain owner work.
Robot37 passed the BMLoop lifecycle step but rejected before save at measured0.2803338269240694-degree normal encoding drift, request `16057a9505624b8594085934718be7b1`.
Parent authorized the same explicit per-request0.5-degree maximum/default0.25 policy for this measured remap case.
Release1.10.38 adds `angular_tolerance_degrees` to the remap operation (outside remap_spec), with finite positive<=0.5 validation and exact worst-corner reporting.
Four targeted encoding/DDS tests include both actual Gorilla and Robot vectors.
Current47-operation lock SHA is `B553D3A5E42BFD6344CE2987ED157060404039A8E8C48BFD4BE62F5C8DB67B49`; manifest `tenth_tranche/remap_tolerance/published_hashes.json` and dependency inventory are current.
Donkey yaw request `a7751d4b618e4edd9073b314e7f068eb` is running on1.10.38; no acceptance claimed before receipt.
Stone/Forest focused tranche drained; Robot38 retry receives that slot, with Gorilla and Donkey the other two owners.


Robot finite44fan remap38 PASSED native and reopened proof, request `b7a903ab9c1946e6a84f89086cb03d59`.
Output `37_seam_fans.blend` SHA `165E370FE2B1137871A7355F7A36E7DE6BCDA837D3FF5DFF45DCB29EBFD23CFB`; all78426 corner normals checked, maximum0.2803338269 degrees within explicit0.5, full unchanged position/weight/UV/rig/action/material proof.
Gorilla patch71 passed; patch72 caller-data duplicate cap rejected before save, owner is rebuilding only3tiny cap loops with6netextra triangles and remains responsible for native validation.


### Release1.10.39 and consistency guard

Donkey yaw request `a7751d4b618e4edd9073b314e7f068eb` failed before save at redundant RNA matrix settings classification after the all-frame Q check.
Parent approved counting only `matrix_world`, `matrix_local`, and `matrix_basis` as transform metadata alongside the already verified explicit final world matrices.
Release1.10.39 applies that narrow classification fix; no deformation, rest-bind, geometry, action or protected-object guard was removed.
Current lock SHA `EAC981D22B8D778A4B8B94AB9C8BDD3C4D7C7032D79946BE55A931A1BF4360F1`; native retry pending.
`python docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/tenth_tranche/test_release_consistency.py` passes3 tests: exact config/lock version+operation-list parity, every locked source checksum, and local import closure locked/present.
This directly guards the previously caught35 lock operations omission.
Inventory and release manifests are current; no parent-owned commit performed here.
Parasitic full weights and unchanged death replay passed native checks, eliminating arm-to-leg sheets in extreme preview; contact pose remains owner-rejected and incomplete.


Gorilla2048 existing-body material binding PASSED request `34179246ba174447b596fc6f0d8d9d8c` under1.10.38.
Report `blender/reports/75_pdx_material_br38.json` records `texture_dimension_budget:2048` and all3 retained source image dimensions `[2048,2048]`.
Output75 SHA `242D8AEEA63D030B5474CD5CE91970A38B9BBD1A4B41AAAF01153AC2E71D4B28`; geometry/UV/weights/rig/actions/old materials preserved.
Parent accepted original/culling-on attack22 surface coherence; final export/reimport remains package-owned.


### Native yaw proof closes the published repair tranche

Donkey yaw1.10.39 PASSED native/save-reopen request `a27353881d0a4f318f2c48492b003959`.
Output16 SHA `B4E16129CA828C644ABF0077C4CA2B5F577EBAE21D560FCF8439A44B3A06E020`.
All305 integer action frames verified exact whole-working-assembly +90Z yaw, maximum world vertex error8.5963e-7, with local geometry/UV/weights/rest bind/actions/materials/protected source preserved.
The actual exported/reimported forward-axis proof remains Donkey owner work; this native checkpoint alone is not an in-game completion claim.
The shared source release1.10.39 is ready for parent-owned coherent tooling commit using `tenth_tranche/released_dependency_inventory.json` and the listed targeted tests.
All code changes in this tranche are bounded repairs; no Meshy credits consumed, no asset-job geometry was edited by the adapter owner, and no runtime wiring was performed here.
No requested repair was replaced with a global normal reset, broad weld/remesh, source omission, or texture downsample.
Remaining asset contact/action/closure/export decisions stay with their named package owners and parent.
At this final adapter proof, active slots are Donkey serial exports, Portal actual-byte reimports, and Gorilla bounded read-only corpse support comparison.


### Committable live regression suite

Use `python .tools/3d_pipeline/tests/test_adapter_recovery_release.py` as the durable regression command; all15 tests pass against the LIVE published adapter modules.
The suite asserts imported module paths, uses exact measured Gorilla/Robot normal vectors, checks source direction/sign and unset-normal rejection,2048 body/default1024 component DDS limits and payload length, exact fan/alias validation including independently varied positions and weights, cardinal yaw validation, exact config/lock operation parity, all locked checksums, and local import closure.
Only Python standard-library unittest/mock facilities are used, with no Blender process or new dependency.
Draft test/source directories are not required to run this suite and need not be included wholesale in the tooling commit.
The dependency inventory includes this one committable test file plus released source/config/lock paths; parent also includes this durable handoff.
No adapter behavior, release version, or locked source bytes changed during test consolidation.


### Exported initial-root coordinate correction:1.10.40

Actual Donkey idle reimport `1ef50612e94b4d83a587a1b09e864443` exposed a downstream exporter defect despite the native yaw preservation proof: rest mesh was yawed but constant root animation channels reverted the original XY orientation.
The locked io_pdx_mesh0.91 `get_scene_animdata` uses POSE-to-WORLD transforms for sampled root channels; `export_animfile` uses rig-local POSE matrices for initial root t/q.
When root rotation is constant it has no sample channel, so the initial value omits rig object yaw.
Parent approved a narrow adapter-owned post-export correction; the locked extension is unchanged.
`animation_root_export.py` derives initial root translation/quaternion using the SAME locked world-space conversion as samples, changes only those root fields, preserves every child/sample/non-pose field, and verifies serialized readback before accepting output.
No scene rig, rest bind, keyframes or mesh is changed.
Already aligned exports remain unchanged.
Corrected Donkey outputs must reimport and pass actual-byte axis proof for all5 roles; this integration proof is pending at publication.

Release1.10.40 remains47 operations; lock SHA `F064F689543939ED09F836964B76B3EDDC0149ACD515CCC73FFD60C309C725B9`.
All19 live regression tests pass, including constant-root yaw, float32 readback, child/sample preservation, aligned no-op and malformed root rejection.
Six locked sources had CRLF working bytes despite existing repository `eol=lf` attributes; normalized ONLY those released sources to LF and refreshed hashes.
Every locked source now has equal raw and Git-clean blob hashes, recorded in `tenth_tranche/root_export_release/published_hashes.json`.
The current dependency inventory includes the new module and runnable live test file; no draft source tree is required for the coherent commit.
No other module behavior or external package changed.
Native corrected idle/export proof is assigned to Donkey first, followed by the remaining4 roles on pass.


### All corrected Donkey role reimports passed

Release1.10.40 initial-root coordinate correction now has actual-byte proof for all5 roles against the accepted yawed mesh:

- idle: `bfc9807f6ebb44ae88c54f58d18791a1`
- move: `5c85401143f44845ac5450f471a396df`
- deploy: `176afdf136984e1a99eb9ec6d4b5cd1b`
- release: `407581583e9b43bc8c34d1c9371e8ef0`
- death: `f64104587a974212b6978223803c1ee3`

Final actual-byte death contact receipt `7581691597944fb2899998596fcccc12` confirms pack_L Z0.00099945 and hanging_basket Z0.01200032.
All Donkey native calls drained; its final copy manifest remains package-owned.
The shared release remains stable at1.10.40 with19 passing live tests and canonical LF hashes; parent owns the coherent tooling commit after the existing Git index lock clears.
No index lock was deleted, process killed, alternate index used, or module behavior changed during final packaging.

### Coherent release committed

Parent committed the complete release 1.10.40 dependency closure, live regression tests, this handoff, and the reviewed skill update as `898b3ea86` after the existing Git index lock released naturally.
All 19 live regression tests passed again after the commit.
All five corrected Donkey actual-byte reimport receipts above are included in the committed proof; the earlier pending-commit statement is superseded.
No shared adapter source changes remain pending, and no additional paid operations were used.
Package production and runtime integration remain separate parent-owned acceptance tasks.

### Text-to-Motion retarget release 1.10.41

The September 9 user request explicitly authorized use of the new Meshy Text-to-Motion endpoint.
The separate endpoint owner produced the sole 10-credit prime pilot and committed its Meshy route fields as `63cc686`; this Blender publication preserves those fields.
Blender release 1.10.41 has 48 operations and dependency-lock SHA `727BFCFCE03F409A086B5FD8CA9518FE151FE148EF4D4E5571E7F0990406F535`.
The additive `inspect_animation_source` operation reads a checksum-bound job-local FBX skeleton and action inventory in a disposable scene, with no target checkpoint mutation.
The import/export provenance allowlists accept the accurate `meshy_text_to_motion` source kind.
Transfer requires explicit source and target rest-joint head pairs for anatomical root displacement scaling, retaining calibrated target geometry.
The source root is measured through its evaluated hierarchy in world coordinates; scaled world X/Y displacement is removed and world Z is converted through the inverse target armature/rest-root basis.
Rotation deltas are conjugated through both armature object orientations.
Every authored frame verifies target world root displacement against the scaled source vertical displacement within 0.00002 source units.
The route requires a new target action and checkpoint, checks retained action curve hashes, and avoids modifying retained scale channels.
Four live coordinate regressions and all 19 prior release regressions pass; native source inspection and candidate transfer remain pending at publication and must be recorded separately.
Owned changed files are `adapter/blender_worker.py`, `adapter/chaosx_blender_hoi4_mcp.py`, new `adapter/retarget_root_motion.py`, new `tests/test_animation_retarget.py`, `config/blender_hoi4_adapter.json`, and only the Blender branch of `config/dependencies.lock.json`, all under `.tools/3d_pipeline/`.
No paid provider operation was performed by the adapter owner.

### Native source inspection and release 1.10.42

Native read-only Text-to-Motion source inspection `8814ce9906054ec7a751c4a27fc2c3c1` passed on the downloaded pilot: armature `Reference`, action `Reference|SMPLH_Animation|Base Layer`, 52 bones, 30 FPS, frames 1–90, object scale 0.01 and +90-degree X orientation.
The zombie owner measured source Pelvis-to-L_Ankle world rest-head span 0.873956497489 and target Hips-to-LeftFoot span 3.5871728982, producing anatomical displacement ratio 4.10452111576.
Release 1.10.42 adds a fail-closed per-frame static source/target object-matrix guard so cached object orientations cannot conceal animated object transforms.
The coherent lock SHA is `D024EF6888904F38BE315D2617D1361B9FE7723A2E35C05892B33B75257ECC03`, with 48 operations and preserved Meshy fields.
All 24 tests pass: four coordinate regressions, 19 release regressions, and the existing native Blender scale-aware integration.
The native integration fixture previously keyed pose-local Z on a root whose local Z points world-horizontal, and incorrectly called local-Z times object scale a world-vertical peak.
Its fixture now keys a genuinely world-vertical displacement through the source rest basis, and asserts horizontal suppression, evaluated vertical retention, inverse-scale behavior, accessory binding and export preservation.
This fixture correction is in `.tools/3d_pipeline/tests/blender_scale_aware_retarget_integration.py`.
The actual pilot transfer remains a separate candidate proof owned by the zombie worker; inspection and passing synthetic tests do not establish its semantic/contact acceptance.

### Actual pilot static-motion guard correction, release 1.10.43

Actual pilot transfer request `2f8e84d30d3e44cebf12a5e4432cf8cf` stopped before save because the legacy static-motion guard added raw source pose-basis translation units to angular radians and compared that total against target units.
Its source peak 313.181 versus target peak 17.5146 was dimensionally inconsistent despite the independently passing world-root displacement proof and closely matching joint rotations.
Release 1.10.43 compares per-joint angular motion in radians only and retains the unchanged static-motion threshold; root translation retains its separate exact per-frame world-space proof.
Five pure coordinate/angular tests, 19 release tests, and the native scale-aware integration pass, including explicit rejection of missing target angular motion.
The coherent 48-operation lock SHA is `1DC3CD7CC323A26B79323DDE61A699E7BB595702E65E4C00130D7CEC6D3C546B`.
The failed request produced no accepted checkpoint; the zombie owner owns the new local candidate retry and visual acceptance.

### Native transfer proof and bounded follow-up inspection, release 1.10.44

The actual 1.10.43 pilot transfer passed with source angular peak 15.9248325434 radians, target peak 15.9248421979, and maximum per-frame world-root displacement error 0.00000029839552.
Its receipt is `docs/assets/002_zombie_outbreak/models_3d/zombies/evidence/repair_2026-09-09/text_to_motion_transfer_receipt_v1.json`.
The generated clip rises again by frame 90 and is not accepted as a complete death action.
Parent authorized retaining its usable fall and manually deriving a terminal settle in a new sibling, preserving the original provider clip and accepted assets.
Live wrapper schemas are archived as `live_tools_1_10_41.json` and `live_tools_1_10_43.json` in that same zombie evidence directory.

Release 1.10.44 retains 48 operations and lock SHA `ABEBC252014EF5C9D7F6F3F45F1760B8192DE7E7A2A81D7D26E7EEB18B3601A2`.
The existing `inspect_scene` now honors its explicitly selected action regardless of action-name prefix, with optional 1–241 distinct integer `evaluated_frames` constrained to that action range.
It records evaluated whole-working-assembly and individual working-mesh world bounds and restores action, slot, and frame.
The existing hash-bound action-channel inventory exposes exact key coordinates, interpolation and handles, plus current named pose-local values, bounded to 500000 keys.
The existing explicit phase patch accepts death phases `standing`, `falling`, `impact`, `rebound`, `settling`, `terminal_hold`, requiring distinguishable non-root articulation through settling while allowing a still terminal hold.
Future source transfers explicitly neutralize unmapped local controls and record their names; this does not alter the accepted 1.10.43 candidate or its provider-prefix evidence.
The actual pilot's unmapped `head_end` and `headfront` are unweighted children of Head and are intended to inherit its motion at identity local transforms.
Six pure tests, 19 release tests and the existing native scale-aware integration pass.
Robot all-frame floor evidence and Zombie exact-key/native ending proof remain package-owned follow-up checks against the original constant calibrated ground, not each preview's recentered plane.

The final live pure suite also tests death-phase articulation versus a still terminal hold, bringing the verified total to 27 tests (seven pure, 19 release, one native scale integration).
Native 1.10.44 exact-key inventory succeeded for the pilot candidate.
Fixed-ground weighted-surface analysis found absolute body minima of 0.881 at frame 1, 0.379 at frame 36, 0.780 at frame 46 and 0.981 at frame 90.
These gaps are not accepted as ground contact; recentered preview floors cannot substitute for the original constant ground plane.
The zombie owner is preserving the usable provider fall rotations and solving a derived articulated terminal settle with explicit per-frame contact correction before its next native candidate.
