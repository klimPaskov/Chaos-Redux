# WP5 model source handoff

Current disposition: source preparation and cave source authoring are present, but model production remains incomplete.
Cave authoring is paused after a safe transfer of both owned Blender locks for the parent-requested WP6 window.
Acceptance basis is the parent's explicit WP5 assignment, the accepted `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/unit_fix_plan.md` section 2.0, every WP5 ticket, section 3, and the raw `unit_defects.json` beside it.
The parent confirmed preservation of the intended existing dimensions using the profile's western European infantry baseline; the installed GER mesh is a separate diagnostic reference and does not authorize rescaling.

The model worker owns source geometry, materials, anatomy rigs, weights, all eight authored roles, source export/reimport and this handoff.
The parent owns active runtime copies, registrations, entities, particles, sourced audio synchronization, reports and commits.
Alien infantry is inventory-only because the external WP4 owner is actively editing it.
Existing bespoke counters are outside this repair assignment; no counter replacement or new gameplay is requested.

## Prepared evidence

The baseline preparation described below was read-only with respect to model and runtime data.
The subsequent cave live authoring changes only job-owned source checkpoints and evidence, as recorded in the live-stage section.
The current package evidence is `.tmp/wp5_models/evidence/`.

- `runtime_inventory.json`: resolved active pdxmesh, meshsettings/material overrides, entities, actions, texture and runtime file hashes for the five WP5 models and the separate alien inventory.
- `source_inventory.json`: hashes for existing provider archives and candidate working checkpoints, current decoded bone maps and bounds, exact current-mesh receipt matches, and the initial dependency/session observations.
- `source_export_comparison.json`: exact decoded geometry, normals, UVs, weights and skeleton parity between current installed mesh and the selected historical source export; all eight current action hashes match the selected export report for each owned model, and each report's working checkpoint hash is intact.
- `installed_audit/`: fresh decoded geometry and all registered action measurements, including the full per-frame motion tables; native import, rendered material/deformation review, measured sole contacts and live appearance are not inferred.
- `compact_baseline.json`: compact topology/action measurements, 60 immutable copied runtime files with SHA parity for the five owned models, exact local reference paths/read spans/SHA revisions, and the updated dependency verification.
- `original_runtime/<slug>/`: the preserved mesh, eight actions and three active DDS maps for each owned model; no alien runtime file was copied or modified.
- `uv_masks/manifest.json`: 21 occupancy masks from current registered PDX UVs across all six inventory models, each bound to mesh and registration hashes; no material class or tangent handedness is inferred from them.
- `sign_corrections.json`: 13 staged q/-q-only animation derivatives, with 48 negative-dot discontinuities removed and exact decoded equivalent-orientation/key-count/non-quaternion proof; all remain pending native reimport and are not selected runtime replacements.

The one-off read-only scripts are `.tmp/wp5_models/source_inventory.py`, `compact_evidence.py`, and `compare_source_exports.py`.
They do not invoke Blender, mutate meshes/actions/textures, or create bones, weights or keys.
`stage_sign_corrections.py` invokes the existing `review/anim_signs.py` only on separate source derivatives, then independently compares the original and output decoded trees.

## Current measured baseline and required repairs

Topology counts below are from decoded logical objects with material streams combined, at 0.0005 source units; 0.001 and 0.002 measurements are retained in the evidence and are equal for the five owned models.
Numerical action passes do not establish semantic performance or actual sole/strike contact.

| Model / source job | Current rig | Current source height × entity scale | Boundary / non-manifold edges | Meaningful action baseline | Requested model repairs remaining |
|---|---:|---:|---:|---|---|
| `paleogenetic_creature` / pilot job of the same name | 40 | 8.087005615 × 0.8 = 6.469604492 | 54 / 70 | All eight roles fail current numerical delivery checks; idle seam 98.43°, attack 62.97°, support 31.77°. | Deliberate ≤12° transitions, coil/lash/hold/recoil/second-lash/settle attack, loop-safe returns, mid-tentacle four-bone chains and reviewed two-influence joints, ≤1.1× extension, frame-60 flank/shoulder texel repair from provider base, exact local pinhole/shell/winding repairs and normals, all-role contacts and actual-byte proofs. |
| `xenobiological_assault_organism` / pilot job of the same name | 30 | 8.087006569 × 0.8 = 6.469605255 | 28 / 18 | Seven roles fail; training passes numerical checks; defend seam 76.77°, attack 26.13°, support 24.46°. | Deliberate ≤12° scythe transitions/contact holds, loop returns, ≤0.2-unit move root bob and ≤1.2-unit support rise/eased landing, reviewed thorax/abdomen/head holes and winding, plate edges with appropriate normals, source-derived material detail/dilation and all-role contact/reimport proofs. |
| `temporal_guard` / pilot job of the same name | 24 | 7.351823807 × 0.8 = 5.881459045 | 78 / 63 | Idle and defend pass numerical checks; six roles fail; attack seam 101.31°, support seam 41.04° / 0.779 units. | Attack/support return tails, ≤15° support steps and ≤0.15-unit root steps, shorter post-thrust pause with forward backhand performance, articulated 3–4-second choke/collapse/settle death with measured impact, exact local torso/arm/boot patches and normals, preserve diffuse identity and prove all exports. |
| `cave_monster_brood` / `cave_monster` | 19 | 7.356357336 × 0.8 = 5.885085869 | 0 / 0 | Geometry manifold gate passes; idle/attack/defend/training numerical passes; move/retreat/support/death fail. | Measure jaw hinge and add lower-jaw bone/skinning, substantive crouch/lunge with ≥3-unit forward hips and ≥50° jaw opening, support chest rise ≥1.5 units and forelimb slam, retain 30 FPS/event synchronization, preserve clean topology, provider-source stone/magma class maps, material-name agreement and complete skeleton-change export/reimport. |
| `rat_brutes` / `rat_ground_unit_shared` | 35 | 7.351824284 × 1.35 = 9.924962783 | 145 / 0 | Retreat numerical pass; move has unresolved sole contacts; six other roles fail. | Measured S-tail rest correction and per-role authored travelling wave/lag, tail-root feathering with <0.15-unit edge growth, rake/lash/slam/death easing, heavier ~45-frame move, reviewed fur-card normal attenuation from provider source with preserved handedness, belt/loincloth/toe weights, explicit snout/ear/card/winding repairs and all-role proofs. Optional lower-jaw shell remains optional under the ticket. |

No requested repair was marked delivered by the baseline preparation pass.
The later cave source changes remain unaccepted because cavity intersection findings, source material reconstruction, full role authoring and export/reimport proofs are unresolved.
Every model retains its identity and intended dimensions.
Required roles are `idle`, `move`, `attack`, `defend`, `support_attack`, `retreat`, `training`, and `death` independently; no alias or static substitute is accepted.
Parent-owned event timing must follow measured final contacts, not a strongest-motion proxy or guessed half-cycle.

Historical current-source previews inspected directly: paleogenetic v4 attack frame 60/front, xenobiological v3 attack frame 60/three-quarter, temporal v3 attack frame 60/three-quarter, cave v5 attack frame 30/three-quarter, and rat r2_v4 idle frame 1/three-quarter.
All five previews display magenta materials, so they establish anatomy/pose orientation only and cannot judge the pale flank patch, fur sparkle or final material quality.
The active runtime map files exist and are resolved in the current inventory; magenta native previews are not evidence that current runtime textures are missing.
Final native review must bind the actual active overrides and the verified PDX decoding graph, preserving both raw importer and corrected material evidence when they differ.

## Exact source roots and lineage

The three pilot job roots are `docs/assets/chaos_redux_3d_model_pilots/models_3d/<slug>/`.
Cave is `docs/assets/018_resources_found/models_3d/cave_monster/`.
Rat is `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/`.
Exact source and runtime hashes, candidate checkpoint paths, provider GLB/FBX records, and literal action/texture registration mappings are in the inventory files; filenames alone do not select a final source.

Each owned current mesh matches only its installed geometry-only native receipt, respectively `reimport_installed_d68e7ccfc165c116.json`, `reimport_installed_66830da246460cef.json`, `reimport_installed_5fc3d56f1f767d7e.json`, `reimport_installed_24987faccd09e067.json`, and `reimport_installed_c8fe70d1d10164d3.json`.
Earlier v3/v4/v5/r2 role receipts are historical and do not prove final repaired motion.
Read-only comparison subsequently proves that the following source exports carry the exact current decoded geometry, normals, UVs, weights and skeleton, and all eight current action bytes match their corresponding export report.
The referenced working checkpoints also match each report's recorded SHA-256.

| Job | Current-content source export | Hash-verified working source |
|---|---|---|
| paleogenetic | `export/v4/chaosx_paleogenetic_creature.mesh` | `blender/working/v3/blender/checkpoints/25_export_batches.blend` |
| xenobiological | `export/v3/xenobiological_assault_organism.mesh` | `blender/working/v3/blender/checkpoints/24_export_batches.blend` |
| temporal | `export/v3/chaosx_temporal_guard.mesh` | `blender/working/v3/blender/checkpoints/24_export_batches.blend` |
| cave | `export/v5/resources_found_cave_monster.mesh` | `blender/working/v3/blender/checkpoints/15_export_batches.blend` |
| rat | `export/r2_v4/black_plague_rat.mesh` | `blender/working/r2/ck/06d_partition.blend` |

Before authoring, inspect these sources natively and rebind only reviewed current texture consumers where historical embedded map names differ.
No checkpoint was promoted or falsely approved.

### Staged sign cleanup

The existing permitted serialized-sample cleanup staged 13 derivatives beneath each owning job's `export/wp5_sign_cleanup/`, leaving every preserved original and runtime file unchanged.
The exact source/destination paths and hashes, tool SHA, receipts and decoded equivalence counts are in `sign_corrections.json`.
Every quaternion group is unchanged or negated as a complete four-component group; all remaining attributes, frame counts, bones and node structure compare exactly.
Negative-dot checks on the written files are zero.

| Model | Staged roles | Negative-dot discontinuities removed |
|---|---|---:|
| rat | death | 1 |
| paleogenetic | attack, defend, retreat, death | 9 |
| temporal | support_attack | 4 |
| cave | death | 2 |
| xenobiological | idle, move, attack, defend, support_attack, death | 32 |

These are lossless orientation-sign corrections only.
They do not fix any authored pose, speed, loop, root, grip, support or strike defect and must not be installed before native reimport and the complete repaired-role review.
The source package remains incomplete.

Paleogenetic, xenobiological and temporal jobs retain `provider/downloads/body_v3.glb` and adjacent base/normal/roughness/metallic maps, with one previously used rig task and the eight role task IDs retained in `blender/working/v3/intake_manifest.json`.
The later read-only `.tmp/wp5_models/evidence/pilot_provider_uvs.json` confirms exact retained UV correspondence against those hash-bound provider GLBs and records all original 2048-pixel PBR map hashes.
All current UV records match with zero UV error and no unmatched records.
Temporal retains the complete 31,033-triangle UV multiset; Paleogenetic retains 31,158 of 31,160 source UV triangles and Xenobiological retains 31,233 of 31,241, with no extra UV triangles.
Those baseline two/eight removed source triangles remain documented differences, not approved topology repairs, and this UV-only evidence does not establish geometry, tangent-frame, material-class or action acceptance.
Rat retains its humanoid generation/remesh/rig/action archives and normal/roughness maps.
At baseline intake, Cave had no retained original GLB/FBX/provider normal/roughness archive; packed native checkpoint images had not yet been inspected.
That absent external archive alone does not require regeneration, but source-derived cave material reconstruction cannot be claimed from current DDS files.
At the baseline stage no provider call had been made and Meshy credits spent were zero.
The later single Cave retexture consumed 10 credits, as recorded below; no paid generation, rigging or action retry was used.

## Dependencies, calibration and route limits

Updated verification reads Blender 5.2.2 build `d13f752e3b9c`, Lab/add-on 1.0.3, adapter 1.11.0 and io_pdx_mesh 0.91.0 from the repository lock.
The initial two locked-source hash mismatches were reported to the parent; after the parent's shared-owner reconciliation, all adapter source hashes match and operation arrays agree.
The updated lock SHA is recorded in `compact_baseline.json`; `.tmp/wp5wp6/environment.json` is the parent's full environment verification.
No shared tool or lock source was edited by this worker.

Exact installed `GER_infantry.mesh` decoding excludes `collision_boxShape` and measures `GER_infantryShape` Y extent 7.414978411048651 (minimum -0.0327853225171566, maximum 7.382193088531494), effective extent 5.931982728838921 at entity scale 0.8.
Its active precedent is `GER_infantry_rifle_mesh` in vanilla `gfx/entities/infantry.gfx`, consumed by `GER_infantry_entity` in `units_infantry.asset`.
The approved profile calibration is instead `western_european_infantry.mesh`, source height 7.3518242835, `infantry_rifle_entity` scale 0.8.
This explains the quoted 7.352 baseline; parent explicitly directed preserving current size and recording GER separately.
No Blender reference import happened during baseline preparation.
The later cave live stage imported both exact vanilla meshes read-only and confirmed their source heights, as recorded in `head_and_calibration.json`.
The other creature numeric crosswalk/rig-route metadata remains awaiting live measurement and source acceptance rather than being filled from profile defaults.

`hoi4.reference_context`, `reference_search`, `reference_read`, and `source_lookup` are absent from the connected tool inventory.
Local offline Entity/Graphical asset wiki sections and installed documentation/vanilla mesh, entity, material shader sources were read directly, with exact line spans and SHA revisions in `compact_baseline.json`.
The parent's additional sound/entity references are `.tmp/wp5wp6/references.json`.
No Paradox wiki web request was used.

The initial external exclusive Blender lock observations remain historical evidence in the baseline records.
The parent subsequently reserved `%TEMP%/chaosx_blender.lock` for WP5, and WP5 acquired the published OS-byte lock at `.tools/3d_pipeline/staging/blender_worker.lock` using its unchanged context manager.
The own lease helper was PID 68324.
WP5 safely adopted borrowed Lab PID 41392 after verifying the foreign Pan Sappers scene was saved and clean; it did not terminate that process or modify the foreign source file.
The current handover facts are in the live-stage section below.

## Cave live stage and safe transfer

The single resumable source is `docs/assets/018_resources_found/models_3d/cave_monster/blender/checkpoints/wp5_13_paused_source.blend`, SHA-256 `81106d8a53e41b37f51e7ebb5250ea95cfa978457b1ee0877c06216ef4402221`.
It was explicitly saved with no dirty scene, no active action, closed jaw, neutral stance and export approval disabled.
At handover, borrowed Lab PID 41392 remained running on this saved checkpoint.
A later read-only process check found that PID no longer present and the advisory lock owned by `setup_promo_model_showcase 3996`; WP5 neither stopped the borrowed process nor changed the foreign lock.
The paused checkpoint was hash-verified again and remains unchanged.
The next native window requires fresh live-session/build/endpoint and saved-foreign-state verification.
The own OS lease helper exited at `2026-10-11T08:34:01.368199+00:00`, and WP5 removed only its exact own TEMP reservation after the shared OS lock was released.
The persistent OS lock file was not deleted.
The parent-requested next window is queued for WP6 Ghost; an external infected-zombies reservation acquired the advisory lock after the WP5 release.
Exact handover evidence is cave `evidence/wp5/session_handover_out.json` and `.tmp/wp5_models/session_lease/released.json`.

Source authoring performed through the verified live Lab:

- Protected body/rig copies preserve the original source.
- Exact GER and western infantry reference geometry was imported read-only; a first skeleton import reused the existing creature rig and failed, so the single corrected retry imported reference geometry without a skeleton and preserved the cave rig.
- The actual reviewed 807-face lower-jaw component was separated from the source shell, with a measured hinge at `(0, -5.5, 3.5)`, rigid jaw binding, modeled interior surfaces and original exterior UV/normal preservation.
- Eight nondeforming, exporter-ignored stance controls supplement 20 anatomy bones; no full action was authored or accepted.
- The exact source rig map already exports fixed `root` above child `hips`; anatomical lunge should use that hierarchy after fresh native verification, rather than adding an unnecessary second root.
- Exact current 512-pixel runtime maps were copied into cave `textures/wp5_bound_maps/` with unchanged hashes and the existing `_specular.dds` binding; no pixel detail or roughness was invented.
- PDX preview decoding uses the installed shader's G/A normal interpretation, gloss inversion and specular/metalness remapping; original importer previews and rejected geometry tests remain separate evidence.

The initial skin-only jaw test failed visible deformation review and is rejected.
The first radial cap design is also unaccepted.
The current quad-grid cavity removes the centre fan, but cap-only float32 segment tests at 55 degrees report 21 palate self-intersection pairs, 50 floor self-intersection pairs and 67 cross-cap pairs.
These findings require double-precision/shared-edge/coplanar disambiguation and real corrections over the required 0-60-degree range; they are not accepted as intentional geometry.
The newer source is not eligible for export or runtime installation while these findings remain unresolved.

Per-corner preservation evidence covers 87,579 retained body corners and 2,421 jaw corners against immutable source checkpoint SHA `20af1f1f84a49186ead5ccb092a216ca4ea52c8f1ce5addb140d7b8d5c614911`.
Maximum measured native drift is 0.483899 degrees on the body and 0.344050 degrees on the jaw; the default 0.25-degree guard does not pass.
The hash-bound complete before/after arrays are `evidence/wp5/source_corner_preservation_before_reopen.npz` with its JSON receipt.
The permitted per-job 0.5-degree review still requires reopened and exported-byte comparison and final visual review; it has not been claimed as accepted.

Before the recovery below, the cave job archives contained no original GLB/FBX or immutable provider roughness/metalness maps.
Packed checkpoint extraction recovered only three postprocessed DDS files, not the missing PBR sources.
That initial missing-source condition is superseded by the recovered roughness/metallic inputs below; class-mask, compatible-normal and packing review remain incomplete.
Existing clean body geometry does not justify whole-body regeneration merely to recover lineage.
After the nonblank key gate passed, the connected tool inventory did not expose `meshy_retexture`, but the unchanged pinned official wrapper's full live schema exposed it with explicit `meshy-7`, original UV preservation and 2K PBR output for 10 credits.
The schema/checksum/lifecycle evidence is `.tmp/wp5_models/evidence/retexture_schema_probe.json`.
The parent explicitly authorized one 10-credit existing-geometry retexture within the user's repair and credit scope.
The measured nonhumanoid crosswalk and dedicated quadruped rig map are cave `provider/wp5_retexture_1/preflight.json`; no regeneration or paid rig/action was requested.

The original runtime geometry was deterministically serialized to OBJ with exact written-file inverse parity across all four PDX material streams: 90,000 split position/normal/UV records and 30,000 original triangles, with no rejected cavity caps.
The OBJ is `provider/inputs/wp5_retexture_1_original.obj`, SHA `7dfd0f5aaa70dc76f45fbffbfe2c3f984dbb9162abd8fdebdb32d94882631e3c`, and its receipt is adjacent.
The first transport delivery returned no JSON-RPC response because its approximately 22.7 MB data URI exceeded the pinned MCP SDK's 10 MiB read buffer.
The official provider retexture inventory then showed no task and no further page, and balance remained 355 credits; this failure was not treated as proof of no task until reconciliation.
Exact evidence is `provider/wp5_retexture_1/uncertain_task_inventory.json`, `uncertain_balance_after.json` and the retained upfront submission journal.

The parent-authorized format conversion to binary GLB reduced the body to 3,063,828 bytes and its data URI to 4,085,141 bytes, with exact actual-byte position/normal/UV/index inverse parity for all four streams.
The GLB is `provider/inputs/wp5_retexture_1_original.glb`, SHA `eaaf7fb9d51ba68b6c47287db99c5af79de24645a31e0bb13ec2c60e9b92776c`; its adjacent receipt records the SDK limit and [glTF coordinate/UV convention](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html).
The corrected input was delivered under the same upfront journal, provider attempt 1 and transport delivery 2, with automatic retry disabled.
The official [Meshy retexture route](https://docs.meshy.ai/en/api/retexture) accepted task `01a12a37-85dd-70ca-b902-1566f7f4accd` with `ai_model=meshy-7`, `enable_original_uv=true`, `enable_pbr=true`, 2K output and GLB/OBJ targets.
The task succeeded and reported 10 consumed credits, independently confirmed by balance 355 -> 345.
Returned GLB/OBJ, all four original 2048-pixel PNG maps and the three embedded JPEG images were archived immediately under cave `provider/wp5_retexture_1/` with SHA manifests.
The GLB SHA is `edf2884ef72e0f0a7d5a86da96c31eae22e253c07758c22d5a94dc34cfa9e292`; the OBJ SHA is `dcfa70c34e9c514687c3fc49e61a31317799db9687da008916d22898cfdb77b4`.
Full actual-byte correspondence, source-map hashes and credit reconciliation are `evidence/wp5/retexture_correspondence.json`.

The provider welded/reordered 90,000 split records into 18,927 records and uniformly normalized the body, without changing its 30,000 triangles or UV values.
Read-only inverse fit is 6.545792477 with source offset `(-0.001392365, 3.675052480, -0.005904675)`; every provider vertex maps to an original position/UV record, maximum restored position error is 0.000000504 units and UV error is exactly zero.
After restoring original corner identities, the complete oriented triangle multiset has zero missing and zero extra triangles.
The preliminary quantized-grid comparisons retained in that evidence produced boundary-rounding mismatches; the exact restored-identity comparison resolves them rather than treating them as geometry defects.
Provider corner normals were recomputed, with a maximum 97.295980-degree difference; the provider geometry/normals will not replace the original source.
The recovered normal PNG is archived but is not selected or approved on the preserved original corner normals.
Its reuse requires source/output-versus-original tangent-basis proof or a deliberate native rebake onto the original geometry/normals; UV parity alone does not establish compatibility, and no global sign is inferred.
The original packed normal remains preserved and selected.

The new base color visibly lacks the established bright magma-seam identity and is not selected for the runtime diffuse.
The existing source diffuse remains selected; recovered original roughness/metallic maps provide the previously absent PBR inputs for the requested source-backed repair.
Explicit reviewed face/UV class masks and packed-map visual review remain open.
The accepted Cave ticket, `unit_fix_plan.md` WP5 `cave_monster_brood` item 3, is the literal calibration basis: stone G60-90, magma-seam G140-180, A70-100 and low B.
The initially inspected shared defaults had stone A50-70 and no magma class; parent-owned strict support commit `17d0c080c` adds the physical magma class and hashed job overrides while retaining existing defaults.
WP5 verified actual locked bytes for `textures/conventions.py` SHA `24f5d1114b6f3dc4e73c5698513cbdb4430224d0ff2b7f489ebce88cc279e320` and `textures/delivery.py` SHA `2e857fd1ccbc7e4f3602858811378cdc72f90eb1d49abacc2964910649764129`.
The current dependency-lock SHA is `ad0ff2c979e02ec02e5b3758225e931de7755973671e6bf67ff8150e82a99c66`.
After native class-mask review, the Cave provenance will use `material_recipe_overrides={"stone":{"alpha":[70,100]}}`, physical magma G140-180/A70-100 and an explicitly empty steel mask for the nonmetal body.
Complete disjoint occupied-mask coverage, immutable roughness/metallic hashes, nonwet-gloss and decoded BC3 gates remain required.
No conversion has yet been run, and no color-threshold class inference, class alias or WP5 shared-tool change was used.

Required next operations are explicit native class-mask/material review and compatible normal transfer or rebake; cavity correction and full required jaw range; engine influence cleanup; distinct supported lunge/slam and all-role authoring; measured sole/support/strike contacts; normal reopen proof; actual `.mesh`/`.anim` export/reimport; and source manifests/current runtime handoff.
The other four WP5 models retain their verified baseline sources and staged sign corrections, with all requested substantive repairs still open.

## Delivery boundary and blockers

The model production package is incomplete because the cave source has known unaccepted cavity findings, pending explicit material-class masks/packing and no completed role/export proofs; the other four source packages have not yet received substantive live repairs.
The transferred Blender window is a scheduling constraint, not acceptance of these defects.
Affected outputs include accepted geometry/material/rig/weight/action repairs, complete deformation and semantic review, measured contact/strike markers, new `.mesh`/`.anim` bytes and their native reimport proofs.
The healthy background export route cannot supply missing authored geometry, weights or motion and is not a substitute for that session.
No blanket weld, cap, normal reset, formula-generated rig/weight/key, semantically aliased role, invented audio, or unreviewed class mask has been used.
There are no implemented design simplifications; the unmet requirements are explicitly still open.

Alien infantry retains its external WP4 ownership.
Current decoding found 50 distinct bones serialized in two object skeleton streams (100 records), seven registered role files and its active `alien_infantry_entity` binding at scale 0.8.
The alien inventory is a changing external baseline and must be refreshed by its owner before acceptance; this worker neither modifies nor approves it.

The parent must retain or carry each blocker, integrate only reviewed selected source exports with source/destination SHA parity, resolve final meshsettings/texture registrations, and place audio/particle events on measured final contact times.
The parent owns the sourced sound package; no sound was downloaded, synthesized or edited here.
User-owned live appearance validation is separate from production completion and is neither requested nor awaited by this handoff.

Skills used: `chaos-redux-3d-model-pipeline`, its start-gate/Blender/export/rebuild/audio-counter references, `chaos-redux-event-assets` and its unit-visual/source/coverage sections, and `chaos-redux-subagents` ownership/single-delivery rules.
No skill, shared tooling, engine-facing source or runtime binary was changed; cave source checkpoints/evidence and 13 source-only sign derivatives were staged as documented above, and no commit was created by the worker.
