# Event002 Zombie Model Fresh Audit

**Disposition:** unresolved for release acceptance. This read-only audit confirms the locked Blender route, normalized skinning in the selected export checkpoints, and byte identity for all current model and animation files. Source lineage, full per-role motion review, current texture provenance and several runtime companion requirements remain open.

## Scope and cost

The audit covered the base zombie and the infected, rabid, parasitic, mutant, undead, necrotic and demonic packages under docs/assets/002_zombie_outbreak/models_3d, plus their current unit, entity, GFX and model consumers. Wendigo is recorded as a separate unresolved consumer because common/units/zombies.txt still assigns it sprite = infantry.

This was Blender-only inspection. The audit estimated and consumed 0 provider credits, made no Meshy or balance call, used no ImageGen, and did not inspect MESHY_API_KEY. No model, runtime asset, gameplay or tool/config source was edited. The adapter wrote its normal result receipts under the named model job roots; this handoff and its evidence files are under docs/plans/002_zombie_outbreak_plans/subagent_handoffs.

The existing base job states 64 of 64 approved credits were consumed. The previous audit handoff records a separate shared ledger of 470 credits across 33 task records for the eight model IDs, while the base job records 64 credits under its own lineage. That historical spend reconciliation was not repeated here.

## Dependency and route evidence

The current dependency lock, adapter configuration and Meshy schema lock hashes are CB8D29299776135E33ACB5FED4DA5CF1F3188719704C0D9C81AD6E52A0A51856, 788858E3DC9E7D43A1717C419815F23935DC031F7BEEB1D50B13601E8AEB8543 and D11E83F737CBB24596A81AE57D1FA202EDA5B18A4672916BEE426FBBA549D8D1. All 36 adapter source files match the checksums in the lock.

One fresh read-only health request returned adapter 1.11.0, Blender 5.2.2 build d13f752e3b9c, loaded io_pdx_mesh 0.91.0, four available exporter operators, and export_meshfile/export_animfile. The installed extension manifest reports 0.91.0, and the selected compatibility archive matches the locked SHA-256 508643626FEFE78511903B1894B8B4D68C387EDD6228AD70487699A866886702. No service was started or restarted.

Eight selected export checkpoints passed the adapter scene-inspection route. Three detailed action-channel inventories also completed and were hash-bound to the exact source checkpoints. A supplemental inspection request for the already reimported base mesh checkpoint remained without a result after more than 13 minutes; its source checkpoint hash stayed unchanged, and I stopped waiting without retrying or restarting the service. The existing reimport receipt hashes remain unchanged.

## Geometry, rig and skin weights

The selected Blender export checkpoints all use the primary skinned object char1.001 with an Armature.001 modifier. The weight report shows one group per armature bone, no weighted non-bone groups, no zero-weight vertices, no vertices above four influences, and weight sums within about 1.3e-7 of 1. The detailed names of every vertex group were not returned by this route, so exact one-to-one group-name equality remains unproven.

| Package | Triangles | Primary vertices | Bones/groups | Influences with 1 / 2 / 3 / 4 bones | Weight sum range |
| --- | ---: | ---: | ---: | --- | --- |
| zombies | 31,054 | 40,749 | 24 / 24 | 8,300 / 11,852 / 6,164 / 14,433 | 0.9999998811.000000125 |
| infected_zombies | 31,039 | 49,862 | 24 / 24 | 5,199 / 12,760 / 8,094 / 23,809 | 0.9999998701.000000119 |
| rabid_zombies | 31,119 | 42,466 | 24 / 24 | 5,092 / 8,677 / 14,230 / 14,467 | 0.9999998661.000000119 |
| parasitic_zombies | 30,783 | 55,298 | 24 / 24 | 2,424 / 4,646 / 7,903 / 40,325 | 0.9999998551.000000123 |
| mutant_zombies | 31,282 | 27,055 | 24 / 24 | 8,140 / 8,212 / 3,610 / 7,093 | 0.9999998661.000000111 |
| undead_zombies | 30,474 | 40,875 | 24 / 24 | 6,454 / 11,761 / 3,467 / 19,193 | 0.9999998691.000000123 |
| necrotic_zombies | 31,153 | 42,382 | 24 / 24 | 11,972 / 11,290 / 5,824 / 13,296 | 0.9999998711.000000119 |
| demonic_zombies | 30,931 | 37,321 | 44 / 44 | 9,012 / 9,056 / 6,176 / 13,077 | 0.9999998761.000000119 |

The current scene inspections report zero raw non-manifold edges, zero degenerate faces and no negative-scale objects. The selected exports remain calibrated to the installed western_european_infantry.mesh reference at source height 7.351824, with infantry_rifle_entity scale 0.8 and effective runtime height about 5.881459. The previous exact-position-weld diagnostics still show nonzero boundary counts for all eight models; those counts are seam-sensitive diagnostics and do not prove holes. No welding or geometry repair was attempted.

## Action and export evidence

The current source checkpoint hashes for all eight packages still match the blend hashes in their selected export reports. The current runtime meshes match both the selected exported mesh copies and selected export-report hashes for all eight packages. Their existing installed-mesh reimport receipt hashes are unchanged.

All 64 runtime .anim files match their selected export files and report hashes. All 64 action hashes are unique, and all 64 existing role reimport receipt hashes remain unchanged. Each package has eight runtime roles: idle, move, attack, defend, support_attack, retreat, training and death. The selected export and receipt records report 30 FPS.

Detailed per-bone channel inspection completed for base idle, base attack and infected attack. Each inspected action has 24 keyed bones with 168 curves containing pose-bone location and quaternion channels. Base attack and infected attack each contain 20,160 keyframes over frames 3122, with 85 varying and 83 static curves; their native action digests differ from each other and from base idle. The read-only receipts report unchanged action data, unchanged rotation modes and immutable source checkpoints.

Only those three of 64 roles received detailed channel inventories. Seven existing phase contact sheets were visually reviewed; the base phase sheet is missing. The sheets are sparse static evidence and do not establish full loop, contact, attack, death or role-separation requirements. The infected attack result arrived in the adapter log after the client wait had ended; no result was inferred before the actual receipt appeared. Further detailed channel requests were not run because that request took more than nine minutes to return.

The base job and all seven specialized intake manifests assign humanoid_unit. Its current asset_profiles.json contract sets idle, move and attack to 24 FPS, while all 64 selected action exports and reimport records are 30 FPS. The profile does not define timing and loop policy for defend, support_attack, retreat, training or death. The demonic intake manifest also assigns humanoid_unit to a 44-bone winged rig; review this classification against the separate winged-biped profile. Resolve the frame-rate and role contract before acceptance.

The base job requires a move_shamble semantic role while its runtime state and selected export are named move. The base intake manifest records a later move task ID and local move.fbx; these differ from the paid action candidates in the job and are not reconciled to the approved move_shamble role or final export checkpoint. The base input manifest still marks the earlier included walk and paid Frankenstein walk as rejected for move_shamble.

## Materials and texture lineage

All 24 current runtime DDS headers meet the current 512-square, ten-mip contract: diffuse maps are DXT1 and normal/specular maps are DXT5. This supersedes the previous 1024-square uncompressed header finding.

None of the 24 current runtime hashes matches its latest package texture-manifest output hash, and none has a same-named current-hash DDS copy in its package root. The manifests still point to older outputs and source hashes; the current runtime map source bytes and packed-channel derivation are not bound to them. Header checks did not decode or assess the new channels, compression error, roughness/gloss semantics or material appearance. Current DDS delivery is structurally compliant but its source and material validation remain unresolved.

## Source lineage and consumers

The base job.yaml says runtime_wired and points to the earlier 30k export from checkpoint 65c_export_batches_slots.blend. Its input manifest says the base package is blocked and selects the 2026-09-25 source-free meshy_input.png with SHA-256 3723991B3EFC92D573CA1CB94CDC6177EB1D501EE5F207DB1613D4E50C3EB3BB. The current selected export instead comes from soldier_v3b/blender/checkpoints/21b_export_batches.blend. The additional meshy_input_v3_soldier.png exists with SHA-256 26FC9188D6E497113EB483F79EF295696EC744A0C4BA8EC8D607B67577587D54, but its source and approval are not reconciled into the job or input manifest. The soldier_v3b intake manifest records eight role task IDs and local FBX sources, but its action IDs differ from the base job candidates and are not hash-linked to the selected final checkpoint. The job status and input-manifest status therefore disagree.

All seven specialized packages lack their own job.yaml and reference input_manifest.json. Each existing intake manifest records humanoid_unit, a rig task ID, eight action task IDs, local FBX paths and preset or motion-task identifiers; all 64 local action FBX files exist and were hashed. The variant roots also contain rigged.glb files and eight body GLB downloads, but the intake manifests omit body-generation task IDs. No provider request/response JSON or animation download receipts were found in those variant roots, and no hash crosswalk connects the intake FBXs and checkpoint chain to the selected final .anim exports. The previous handoff statement that no variant action task IDs existed is superseded by this manifest reread. No source URL, creator/license terms, retrieval record or approval was newly researched in this read-only audit.

Current source hashes for common/units/zombies.txt and the eight entity, GFX and animation-registration files are captured in runtime_consumer_sources.json. The eight unit definitions use their eight custom sprite tokens and resolve to the named entity and model folders recorded there. Wendigo remains at common/units/zombies.txt line 497 with sprite = infantry and no custom model in this audit scope.

The prior audit handoff reports that bespoke variant counters still await parent visual review, while base and variant sound selection, exact runtime consumer binding and action-frame synchronization remain unresolved. Those audio and counter packages were not reaudited here.

## Simplifications, omissions and blockers

This audit made no model simplification or fallback. The model packages remain unresolved for release acceptance because:

- Detailed per-bone channel inventory covers only three actions; semantic validation of all 64 actions and exact vertex-group name mapping remain open.
- Full action contact, loop and role-specific motion validation remains open, including the prior mutant knockdown grounding concern.
- The base 24-versus-30 FPS profile mismatch and move_shamble-to-move role mapping need reconciliation.
- The base source/job lineage is stale against the selected export; variant action task IDs and FBXs are recorded, but provider response receipts, body-task IDs and source-to-export hash crosswalks are missing.
- All current DDS files meet header requirements, but none is hash-bound to its latest package texture manifest or a current package source copy; packed channels and material appearance remain unchecked.
- Prior seam-aware topology diagnostics and the parent-owned audio/counter handoffs still need review.
- Wendigos infantry sprite remains unresolved.
- No in-game consumer validation was performed; the user owns that validation and the parent owns the completion claim.

## Evidence files

- [Dependency and scene-inspection evidence](models_final_fresh_20261006_evidence/dependency_health_and_scene_inspections.json)
- [Runtime mesh and action byte comparison](models_final_fresh_20261006_evidence/runtime_mesh_action_bytes.json)
- [Texture lineage snapshot](models_final_fresh_20261006_evidence/texture_lineage_snapshot.json)
- [Action channels and visual review](models_final_fresh_20261006_evidence/action_channels_and_visual_review.json)
- [Animation contract and open gaps](models_final_fresh_20261006_evidence/animation_contract_and_open_gaps.json)
- [Source, job and consumer lineage](models_final_fresh_20261006_evidence/source_job_and_consumer_lineage.json)
- [Provider intake task and FBX lineage](models_final_fresh_20261006_evidence/provider_intake_task_lineage.json)
- [Current runtime consumer source hashes](models_final_fresh_20261006_evidence/runtime_consumer_sources.json)

Skills applied: chaos-redux-3d-model-pipeline, chaos-redux-event-assets and chaos-redux-subagents.