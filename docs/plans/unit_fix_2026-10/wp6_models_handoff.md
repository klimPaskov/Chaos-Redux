# WP6 model production handoff

Current disposition: preparatory production delivered; required live model authoring queued behind an unavailable exclusive Blender session, package incomplete.
The parent assignment authorizes repairs of five existing unit packages, model candidates and evidence, with runtime wiring and commits retained by the parent.
No Hearts of Iron IV process, sound download, sound synthesis, runtime registry edit or commit has been made by this worker.
Audio processing belongs to the parent's `wp5_wp6_audio` specialist; cannibal WAVs and definitions remain WP2-owned.

## Delivered preparatory candidates

Eleven copies of existing actions have lossless quaternion-sign normalization under each registered job's `export/wp6/sign_continuity/` folder.
The shared `anim_signs.py` route removed 49 negative-dot sample discontinuities, preserving every bone, frame, translation, scale, initial record and orientation.
Parser readback verifies exact equality of all non-quaternion data and exact component-wise equality or whole-quaternion negation of each sample.
These candidates have not been installed, natively reimported or accepted as finished reworks.
Their original motion, role, loop, root and contact defects remain open.
Per-role receipts and gates sit beside the candidates, and the complete source/destination SHA-256 ledger is `.tmp/wp6_models/sign_cleanup_receipts.json`.

| Registered job | Corrected candidate roles | Negative-dot discontinuities removed |
| --- | --- | --- |
| `cannibal_bone_guard` | attack, support_attack, death | 10 |
| `cannibal_siege_eaters` | idle, move, defend, support_attack, training, death | 32 |
| `ghost_hosts` | attack, death | 7 |

The active registration's exact UV triangles produced fifteen 512-pixel occupancy masks with zero unbound-stream or unsupported-wrap findings.
They are preparatory masks bound to the current mesh and registration hashes, not material-class masks or finished textures.
The manifest is `.tmp/wp6_models/uv_masks/manifest.json`.

## Current selected repair sources

The approved repair route uses the installed-byte geometry checkpoints below.
Their exact complete path/hash records, all retained provider GLB/FBX archives, and all alternate checkpoint paths/hashes are `.tmp/wp6_models/intake.json`.
The current consumer/material/action inventory is `.tmp/wp6_models/inventory.json`.
All five current skeletons contain 24 bones and lack articulated finger chains.
Each package requires idle, move, attack, defend, support_attack, retreat, training and death, with no semantic aliases.

| Unit | Registered job root under `docs/assets/` | Selected geometry checkpoint | Runtime entity | Current source mesh SHA-256 |
| --- | --- | --- | --- | --- |
| cannibal_bone_guard | `014_cannibalism/models_3d/cannibal_bone_guard/` | `blender/checkpoints/reimport_installed_89c9bac619a98753.blend` | `cannibal_bone_guard_entity` | `89c9bac619a98753ac0d9510a51e3b8abdaa371a26a3f9ed767d74083937acc0` |
| cannibal_siege_eaters | `014_cannibalism/models_3d/cannibal_siege_eaters/` | `blender/checkpoints/reimport_installed_a632f115a093421a.blend` | `cannibal_siege_eaters_entity` | `a632f115a093421a1ac8dee441692d72d8799c097b9d7c9c2f16abd4a6bd9772` |
| cannibal_march_predation_column | `014_cannibalism/models_3d/cannibal_march_predation_column/` | `blender/checkpoints/reimport_installed_dc6d2f19c25c8c2e.blend` | `cannibal_march_predation_column_entity` | `dc6d2f19c25c8c2e2ee83d7ea01124248c3917d203e41c9b5368f563225cbc9e` |
| death_hollow_ghost_host | `010_death/models_3d/ghost_hosts/` | `blender/checkpoints/reimport_installed_bcdeedaaa8b86d48.blend` | `death_ghost_entity` | `bcdeedaaa8b86d48a0235209ea57a79a52844b488ce042900d3d9973a3bdfb86` |
| chaos_battalion | `chaos_warfare_system/models_3d/chaos_assault_battalion/` | `blender/checkpoints/reimport_installed_bc1183e2f31c45dc.blend` | `chaos_battalion_entity` | `bc1183e2f31c45dce4fa38874eb64a354d125b3368a4cb88a7d7a910eb32fa1f` |

## Baseline diagnostics

Read-only current-byte inspection uses the installed parser and current calibrated delivery gates.
It finds six action passes and thirty-four blocked actions; an apparent numeric pass does not prove intended role semantics, assembled grips, floor contacts or visual acceptance.
For example, Siege Eaters attack passes the generic motion gate while its requested overhead club swing remains absent.
The complete decoded geometry and forty action measurements, including loop seams, root drift and motion peaks, are `.tmp/wp6_models/baseline_audit/summary.json` and its model/action reports.

| Unit | Positional boundary / non-manifold edges at 0.0005 | Geometry gate | Action passes / 8 |
| --- | --- | --- | --- |
| Bone Guard | 0 / 0 | pass | 1 |
| Siege Eaters | 77 / 0 | blocked | 1 |
| March Predation Column | 126 / 0 | blocked | 2 |
| Hollow Ghost Host | 58 / 36 | blocked | 0 |
| Chaos Battalion | 105 / 95 | blocked | 2 |

Current `.mesh` material node names are `mesh.001` for Bone Guard, `mesh.002` for Siege Eaters, `char1.002` for March, and `char1.001` for Ghost and Battalion.
The latter two currently have four and five material streams respectively.
Final node names, stream indices and texture names will come from the selected candidate exports; current labels must not select a future mesh by filename alone.
The decoded current Battalion mesh exports `lance_nozzle` parented to `RightHand`, PDX local position `[0.0000155568122864, 0.00000616908073425, 2.42614221573]`, xyzw quaternion `[0.707106769085, -0.0000000316101420594, -0.00000000263418042934, 0.707106769085]`.
The old discharge handoff's proposed `assault_projector_muzzle` is not the current exported locator.
This readback establishes the current transform and parent only; final nozzle/barrel axis and per-frame contacts still need assembled authoring review.
The current support_attack terminal-to-defend first-frame local pose comparison has Hips 53.39 degrees, LeftArm 97.29 degrees, LeftHand 116.92 degrees angular gaps and a maximum local translation gap of 0.0830 units.
Changing `next_state` to defend alone therefore does not establish the accepted braced transition on current bytes.
The source-bound comparison is `.tmp/wp6_models/battalion_transition.json`; an authored kneel-return remains the selected repair plan unless evaluated blend and contact evidence supports the alternate route.

## Dependency and reference evidence

The process Meshy key gate was nonblank; its value was neither read nor stored.
The original read-only preparation needed no paid provider calls; the separately authorized existing-model PBR recovery below now has provider requests and fresh balance evidence.
Its paid lineage is separate from the unchanged historical geometry, rig and action budgets.
Initial adapter/textures source-hash mismatches were reported to the parent and cleared through its prerequisite commit `40a075ac2`.
The refreshed intake checks every locked adapter source, texture source, compatibility archive and installed `io_pdx_mesh` patch file with no mismatches; adapter operation arrays agree.
The live bounded adapter `tools/list` probe exposes all 32 locked operations and launches no Blender worker.
Its schemas and stdio lifecycle receipt are `.tmp/wp6_models/adapter_schema.json`.
The selected dependencies remain those in the exact intake-bound lock: adapter 1.11.0, Blender 5.2.2 build `d13f752e3b9c`, Blender Lab MCP/add-on 1.0.3, `io_pdx_mesh` 0.91 with the recorded compatibility archive.
Current native export/reimport and live Lab authoring verification remain pending the exclusive process window; earlier compatibility evidence is not a new WP6 production proof.

The connected tool inventory lacks `hoi4.reference_context`, `reference_search`, `reference_read` and `source_lookup`, so targeted local reads were used.
The read spans and complete source SHA-256 revisions are retained in `intake.json`: Entity modding lines 25-185, Graphical asset modding's empty Object Types section at lines 246-248, installed effects documentation lines 6826-6842, installed `infantry.gfx` lines 1713-1743, and `units_infantry.asset` base infantry and GER definitions.
The exact installed `GER_infantry.mesh` remains the next read-only native calibration source, with retained entity scale 0.8.
The parent/WP5 decoded reference excludes collision geometry and measures GER source height 7.414978411; the intended profile instead uses `western_european_infantry.mesh` height 7.351824284.
Fresh native measurement will confirm the selected reference when the exclusive window is acquired; this difference does not authorize changing existing model dimensions.

## Exact material-source preparation

Bone Guard's exact original processed DDS files survive as hash-verified shared texture-CAS preimages, even though the named raw v6 PBR images and selected provider geometry are absent.
The original diffuse is `f9224aa4223ba5f34b19f1b9a636af0aaf7d14f4f3b6b4a1260b48297b02c24c`, normal `8f2ac8a8029f4845f6b437b051991518e545be2309d2c53877d3323ac9eec54c`, and specular `77193b163e9ea8ad2773c497d33fcb9ba8765a13d5c71ff8677a5524bd180d6d`.
All three match the v6 receipt and shared CAS ledger; their current runtime maps match that ledger's installed after-hashes.
The active consumer remains `cannibal_bone_guard_mesh`, `mesh.001` stream 0, shader `PdxMeshAdvanced`, with the unchanged original mesh hash and explicit diffuse/normal/specular overrides.
Current-source binding, exact missing paths, receipt revisions, archive/current DDS hashes and decoded previews are `.tmp/wp6_models/bone_guard_textures/preflight.json`.
Three visually selected partial `dry_skin` mask proposals cover 6,091 occupied texels on the exact archived 1024 atlas; their polygons, physical basis, source/mesh/registration/mask hashes and review overlay are `.tmp/wp6_models/bone_guard_textures/material_proposals.json`.
An ambiguous fourth patch was removed during producer review; anatomical UV assignment and parent review remain pending.
The proposals do not classify bone, leather, rough gear or the axe head and are not a full-atlas recipe.
No PBR recipe or finished material map is staged from those incomplete masks; missing raw v6 roughness/metalness prevents that direct source route.
The separate 2.76-million-triangle body is excluded from direct map substitution, while its potential as a deliberate native high-poly bake source remains open for grouped identity/anatomy/projection comparison and parent review.
Its recorded source is CMON HATE Um'Kator Warrior #3, attribution CMON/CoolMiniOrNot, concept Adrian Smith, sculpt Patrick Masson and painting Angel Giraldez; the exact source-image bytes and provider task linkage are unavailable, while the parent-approved separated input hashes and source permission record remain retained.

Original Ghost body GLB `780f12111d883818c6f71f2936e2ea9eb8a917358f1cc6cedbbeb1fb9bd75b70` matches all 31,133 current triangles with unique unchanged UVs, no ambiguous mapping and no geometry exceptions above 0.00001 source-mesh units.
Its maximum fitted position residual is about 0.00000231 units with uniform scale about 3.863640 and the documented glTF-to-PDX axis reflection.
Original Battalion body GLB `f0c81641af111e548aa9124dc525c7891d7289b95092b0ef66cc213e0ee43c74` matches all 30,982 body triangles uniquely with `V_runtime = 0.75 * V_source + 0.25`, observed maximum UV difference 0.0000000298 under the explicit 0.0000002 tolerance.
The 4,112 unmatched runtime triangles correspond to the separate lance count; body-source maps cannot be applied to that item region.
Six Battalion triangles 5436, 5492, 5528, 5692, 5726 and 5767 surround the same native point `[-0.6701031923, 4.3293418884, -0.2910158932]` and differ geometrically by up to 0.00316194 units; these remain explicit source-correspondence exceptions, while p99 position residual is about 0.00000148 units.
The source/runtime hashes, every matched triangle, explicit geometry exceptions, source affine fit and exact UV transform are retained once in `.tmp/wp6_models/body_runtime_correspondence.json`.
This is source-map correspondence evidence, not native deformation, tangent handedness, physical material classification or live-game acceptance.

Ghost and Battalion each now have four canonical mechanically extracted PBR maps under their job's `textures/source/wp6_original_body/`, bound to the original GLB material's embedded images and channels.
Exact embedded JPEG/PNG bytes are preserved beside the extracts, and reopened canonical PNG pixels equal the selected embedded base color, roughness G, metallic B and normal RGB values.
The existing standalone PNGs retain their own hashes: their normal pixels match exactly, while color/roughness/metallic differ from the embedded JPEG pixels by less than one 8-bit level on average, so byte/pixel equality is not asserted for those peer maps.
The embedded JPEG source quality and canonical selection are recorded for review; the untouched peer PNGs remain available.
Each job's `validation/wp6/source_maps.json` supplies source GLB/image/map hashes, roles, dimensions, channel binding, peer-map differences and runtime geometry/UV correspondence.
These verified material sources remain eligible for live physical-class review; the rig GLBs' missing PBR links are not a source blocker.
Parent shared-tool commit `17d0c080c` adds physical `bone` and `worn_steel` recipes, metal-mask union and hash-bound known-class range overrides without changing old defaults.
The updated texture contract was read and the raw locked source hashes verified: conventions `24f5d1114b6f3dc4e73c5698513cbdb4430224d0ff2b7f489ebce88cc279e320`, delivery `2e857fd1ccbc7e4f3602858811378cdc72f90eb1d49abacc2964910649764129`.
Ghost's accepted ticket calibration is cloth G40-70/A70-100, bone G110-140/A70-100, worn steel G150-180/A70-100, and source-reviewed leather using its shared G120-160 range with the ticket A70-100.
The numerical basis, exact user-plan SHA, recipe overrides and current tool hashes are in `ghost_hosts/validation/wp6/ticket_material_calibration.json`; no material conversion has run and complete disjoint physical masks remain mandatory.

Ghost's current-byte tangent diagnostic binds all 31,133 source/runtime triangle pairs and 93,399 corners to the exact normal/tangent buffers.
The measured source-to-native basis determinant is approximately -1, while source/native normal directions all align positively and the native bitangent aligns positively with the transformed source UV-derived bitangent on 93,351 corners, negatively on 48, with 400 low-confidence corners where the absolute alignment is below 0.5.
Per-face UV derivatives are an orientation diagnostic and do not replace the required native MikkTSpace evaluation; the original GLB has no explicit `TANGENT` accessor.
The installed shader is material: `standardfuncsgfx.fxh` lines 311-318 negate decoded packed alpha's signed Y after `2*A-1`; `pdxmesh.shader` lines 258-260 and 471-496 build the bitangent from `cross(N,T)*ta.w` and apply that TBN.
The [Khronos glTF specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html) defines normal RGB as signed XYZ and recommends MikkTSpace reconstruction when tangents are absent.
The diagnostic suggests that packing original glTF G directly into PDX A requires explicit handedness resolution; no green/alpha sign change has been made or accepted from this partial diagnostic or a plausible preview.
The source hashes/spans, exact affine basis, every triangle/corner comparison, ambiguity rows and limits are `.tmp/wp6_models/ghost_tangent_basis.json`.
Native source-versus-candidate tangent evaluation and post-repair reimport must determine the final channel sign and are invalidated by geometry/normal repairs.

The parent approved an actual exported fixed root above Ghost's Hips within this repair scope, allowing the requested 1-unit anatomical glide while the actor root stays in place.
The existing Hips-root hierarchy cannot satisfy both that glide and the shared 0.2-unit maximum planar root excursion gate.
The new root must appear in the decoded exported skeleton and animation records, with reviewed bind matrices, preserved deliberate weights and all eight downstream action/export/reimport checks.
The 50-bone limit remains binding; only exact zero-influence/no-locator/no-consumer helper bones may be removed, with the proof retained.
No ignored control, root-gate relaxation or omission of required anatomy/finger motion is approved.
The current native helper audit finds exactly zero positive influences, zero weight sums and zero maximum weights for both `head_end` and `headfront` across all four material streams, no decoded locators, and no helper-name references in the scoped active Ghost entity/GFX/animation registrations.
That source-bound evidence is `.tmp/wp6_models/ghost_helper_bone_audit.json`; live constraint, driver, hierarchy, modifier and action-channel review remains required before removing either helper.
The locked exporter's `get_skeleton_hierarchy` begins at `rig.data.bones[0]` and walks only that bone's children, so merely appending a parent Root above existing Hips would not export the Root.
The parent selected a deliberate native operation: author Root in a same-transform armature, then evaluate native Join of the preserved source armature into that active Root armature and parent Hips while preserving the authored source data.
Before/after proof must compare every old bone rest/world matrix, parent relation, weight assignment, source action pose, modifier and constraint target; parity failure discards only the owned candidate and preserves the immutable source.
The resulting actual exported Root must occupy bone index 0 and every required bone must reach the decoded output.
No skeleton generation from a repository manifest/formula or patch of the signed shared exporter is part of this route.
The bundled official API declarations for native `object.join`, `armature_add`, mode changes, edit-bone parenting/rest matrices and action slots were read locally; exact paths, spans, hashes and excerpts are `.tmp/wp6_models/ghost_root_native_api_readiness.json`.
This establishes declared operations for the planned native evaluation, not successful hierarchy authoring or export.

## Exact existing-model PBR recovery

The parent explicitly authorized one 10-credit Meshy7 original-UV PBR recovery for each existing installed Bone Guard and March mesh while the native session is occupied.
These repairs upload only hash-bound current geometry; no old artwork, new source-free image, generated body, rig, weights or keys is supplied.
The bounded WP5-owned serializer independently decodes its actual written GLB and inversely proves exact float32 positions, normals, UVs and oriented triangle order for the complete single logical object.
Bone Guard input GLB is 947,796 bytes, SHA-256 `1839246939874d79515c1979707f12310d44445f59ce564c2d03385f9ad040c5`, with 23,957 records and 30,000 triangles.
March input GLB is 1,460,444 bytes, SHA-256 `4b2e228851e5d2897f0e0b5fc9dddaac9ee6ea024700d34401cd053b25a641a9`, with 39,977 records and 30,000 triangles.
Each job retains `provider/inputs/wp6_retexture_1_source.json` and `wp6_retexture_1_original_glb_conversion.json`; fit factor remains 1 and runtime entity scale remains 0.8.
The fresh nonblank key, locked wrapper/package/SDK hashes and live 29-tool retexture schema gate are `.tmp/wp6_models/retexture_schema_probe.json`; no Blender process was used.
The call requests `meshy-7`, original UVs, PBR and 2K, with a concise physical material prompt and no image style input.
The full tools/call UTF-8 envelope, an additional 2,048-byte guard, exact input hashes, fresh balance, one-attempt limit and no automatic retry are journaled before dispatch under each job `provider/wp6_retexture_1/`.
Independent post-dispatch reconstruction of the maintained client's complete three-message stdin confirms totals 1,264,802 bytes for Bone and 1,948,381 for March; the 228-byte initialize/notification overhead fits inside the unchanged upfront guard.
Each recovery folder retains `transport_written_envelope_proof.json`, binding the exact maintained client hash and serialization while omitting model data URIs.
Bone Guard task `01a12a8d-6f8e-76f6-ad7f-ddca5579f584` succeeded, consumed 10 credits, and its GLB plus four original downloaded PBR PNGs were immediately archived with individual checksums in `provider/wp6_retexture_1/archive_receipt.json`.
The exact returned GLB hash is `861be33d12198fe66da4b626bd5500a7e2c4dcef53edd666f6e9e05e23b0ea98`; source-map material acceptance remains pending.
Its full tools/call envelope was 1,264,574 UTF-8 bytes before the 2,048-byte guard.
March task `01a12a90-1648-77f0-b996-47c7656dca83` succeeded, consumed 10 credits, and its GLB plus four original downloaded PBR PNGs were immediately archived with individual checksums in its job `provider/wp6_retexture_1/archive_receipt.json`.
Its exact returned GLB hash is `2cb736b4ce777f1441c9c6fd0d7cbadc8124d506361d87e46fd3d10da5d5a41f`, and its full tools/call envelope was 1,948,153 UTF-8 bytes before the 2,048-byte guard.
March source-map material acceptance remains pending.
Fresh balances were 345 before Bone, 335 before March and 325 after completion; each completed task confirms consumed credits 10, total new paid cost 20.
No paid retry, second dispatch, new body generation, rig or action attempt occurred.
Both actual-byte provider audits restore all 30,000 original oriented corner-identity triangles with exact UV values and zero missing, extra, unmatched or ambiguous records.
Bone maximum restored position residual is 0.000000243172 units; March is 0.000000267656, under a measured uniform source fit applied only in read-only comparison.
All active mesh-node instances and primitives were included; nonidentity ancestor/node transforms, omitted meshes, skins and unsupported accessor/primitive forms are rejected by this bounded audit.
The exact proofs are each job `evidence/wp6/retexture_correspondence.json`; the task-cost fields distinguish actual completed-task cost from concurrent global balance changes.
Roughness/metallic original-UV transfer is eligible on that proof, while provider normals differ by up to 128.3296 degrees for Bone and 179.8018 for March.
Provider output geometry and normals remain unselected; the recovered normal map requires explicit native tangent-basis proof or rebake and diffuse requires identity/color review.
Each job `validation/wp6/retexture_source_maps.json` binds four canonical 2048-pixel maps under `textures/source/wp6_retexture_1/` to the actual returned GLB material texture indices and embedded channels, with preserved exact embedded JPEG bytes.
Reopened canonical PNG pixels equal those declared embedded source channels; the separately downloaded PNGs are immutable peer maps with recorded JPEG-related pixel differences, never asserted byte-equal.
All recovered maps remain unaccepted material candidates until full disjoint physical masks, source-normal/tangent resolution, final DDS gates and actual-byte native visual review.
The current runtime geometry and textures remain selected and unchanged.
Successful artifacts must be archived immediately with individual map checksums because provider URLs expire.
Siege is excluded from upload: the retained Hadfield NoAI research-only reference and explicit rejected-descendant record conflict with an unsubstantiated later approval label, and the current geometry has no independent eligible source lineage.
This is an unresolved provenance bar, not proof that the current mesh descends from that artwork; existing-byte native repair remains allowed.
No attempt limit was reset, no provider rig/action retry was used, and no runtime material was installed.

## Outstanding production and source constraints

WP5 saved its clean Cave source at `wp5_13_paused_source.blend` (SHA-256 `81106d8a53e41b37f51e7ebb5250ea95cfa978457b1ee0877c06216ef4402221`), cleared its action/pose and released both locks.
The parent explicitly transferred the next window to WP6 for Ghost; however, before WP6 acquired either lock, `%TEMP%/chaosx_blender.lock` contained competing owner `wp3_leftovers infected_zombies 2026-10-11T11:37:30`.
WP6 reported that race and has not created, deleted or leased a lock, loaded a model or called Blender Lab.
The parent has authorized atomic WP6 acquisition when the competing owner genuinely releases; no foreign lock may be removed and the borrowed PID 41392 must never be terminated by WP6.
The competing TEMP lock subsequently advanced to `wp3_leftovers parasitic_zombies 2026-10-11T12:22:31`, and `Get-Process -Id 41392` returned no process.
Live Lab discovery must therefore occur after owning the coordinated window instead of assuming the old PID still exists.
The prior WP5 ownership of PID 41392 and both locks is historical, not the current TEMP-lock claim.
Historical readiness checks recorded the former external WP1/WP4 owner, persistent PID 41392, and temporary workers 21868 and 54096; those observations are not current ownership claims.
This is a shared production-resource dependency, not a missing provider generation requirement or an unavailable optional check.

Every model still needs real live authored corrections, assembled role/contact review, candidate material delivery, native export/reimport, previews and final exact binding handoff.
Bone Guard needs the short readable poleaxe swing, two-hand retention and full finger grip, support/defend/training fixes, source-backed normal/material repair.
Siege Eaters needs root-policy and collapse repair, a real two-hand club swing, full finger grips, measured stride cycle, torso-hole and winding repair, source-backed material detail.
The Siege Eaters ticket contains a literal acceptance contradiction: its attack step asks for a 50-80 degrees per-frame RightArm/Spine strike and its acceptance asks for a RightArm peak of at least 50 degrees per frame, while the same acceptance requires zero single-frame rotations above 40 degrees.
Those numerical criteria cannot all hold for the same measured strike.
The parent directed a readable smooth real swing under the shared calibrated limits, preserving the unresolved literal threshold instead of widening strike windows or silently waiving a criterion.
Final review must report the measured strike speed and this unresolved acceptance condition separately from role readability and export-gate results.
March needs deliberate coat weights and silhouette correction, separate rigid bow controls and finger grips, bow draw/release performances, pinhole/winding repair and source-backed coat/material correction.
Ghost needs the authored hovering idle and chest-height rakes, articulated claws, skirt and topology repair and readable greatcoat/bone/helmet materials.
Battalion needs closed attack/support loops, kneel and coat deformation repair, real retained hose geometry and rigid separate lance with finger contacts, independent material stream, all firing-state locator/phase handoff.
Skeletal changes will invalidate every downstream weight/action/export approval and require all eight roles to be rechecked.
Gait plant counts and event times remain unmeasured; nominal quarter cycles must not be installed as measured contacts.

At baseline intake, Siege and March retained no original provider GLB/FBX files; their installed geometry checkpoints remain usable for authorized repair.
March has the newly archived existing-model retexture GLB described above, which does not replace its selected runtime geometry.
Siege's old generated-input source eligibility is unresolved, with retained NoAI research-only artwork and missing approved input; this prevents a fresh provider generation from that source, not repair of existing installed bytes.
Bone Guard has a retained item-free body archive and parent-approved separated body/poleaxe images, but the archive lacks exact provider task linkage and the selected installed mesh follows a different historical source.
Its generation sources are not interchangeable with the installed mesh.
Read-only GLB metadata finds 2,763,616 triangles and no skin in the retained Bone Guard body archive, so it is a high-resolution unrigged geometry source, not a replacement runtime rig or an action source.
Ghost's v3 body/rig each retain 31,133 triangles, Battalion's v3 body/rig each retain 30,982, and the separate spray lance retains 4,112; each rig archive has 24 joints.
Exact container/material/image-channel records and archive hashes are `.tmp/wp6_models/provider_glb_metadata.json`; these counts establish metadata only and do not approve a source switch, topology, licensing or deformation.
Ghost and Battalion retain v3 provider bodies, rigs and role FBXs with intake task records; re-rigging or paid action retries must not reset their historical one-attempt limits.
No provider substitution, scope reduction, static action or alias has been used.
Existing counter provenance is retained; this repair assignment has not requested replacement counter art, and no counter acceptance is claimed from the model-only preparation.

## Changed files and parent work

Maintained worker documentation: this single current handoff; parent owns staging and commits.
Ignored worker changes: intake/schema/source-correspondence scripts and JSON evidence, current inventory and baseline audit, UV occupancy masks, three-region physical mask proposals and archive/current DDS previews, canonical original-body PBR extracts with map receipts, two exact compact GLB recovery inputs and bounded provider journals, and eleven candidate `.anim` files with receipt/gate JSON under registered job roots.
No game-visible file is changed.
The parent must review the finished candidate package before installation, compare active meshsettings against decoded selected streams and texture hashes, wire event times/particles/audio from authored phase and contact evidence, integrate the separate audio handoff, and create the requested isolated per-model commits.
The user owns live consumer validation; it is neither requested nor awaited by this worker.
Skills applied: `chaos-redux-3d-model-pipeline` and its start/export/audio/rebuild references, `chaos-redux-event-assets` and relevant provenance/unit/reference guidance, `chaos-redux-subagents`, and the parent's named `chaos-redux-shared-git-commit` guidance.
