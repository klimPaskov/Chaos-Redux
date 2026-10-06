# Event 002 zombie 3D package audit — 2026-10-06

Disposition: the read-only audit is complete, but the model packages remain unresolved for release acceptance. Current runtime meshes and actions match the existing decoded/export receipts, while the live adapter version, weight and action-channel evidence, texture source synchronization, and per-variant intake manifests remain open.

## Critical findings

- The current dependency lock selects adapter 1.11.0, but the connected health route returned adapter 1.10.51. The health operation also found two current adapter source files that do not match the 1.11.0 lock; I stopped before scene inspection or reimport.
- Another model agent replaced all 24 runtime DDS maps during the audit. The final snapshot shows the expected 512-square DXT1 diffuse and DXT5 normal/specular formats with ten mip levels, but none of those current hashes matches the previous export/runtime-sync record or a current DDS file in its package root.
- The currently wired Wendigo subunit still uses sprite = infantry at common\units\zombies.txt:497–505. No custom Wendigo entity, mesh, or action package is present.
- The seven variant roots have no per-model job.yaml, model manifest, input manifest, provider task directory, history, or runtime crosswalk. The base job.yaml and input manifest point to the older September 25 input/task lineage rather than the current soldier rebuild.
- The variant action files have unique hashes and non-static sampled bounds, but the available receipts do not contain per-bone channel inventories or exact per-role action-source receipts. Semantic similarity and formulaic reuse therefore remain unverified.
- The decoded topology reports have zero raw non-manifold edges and zero degenerate faces, but their separate position-welded diagnostics retain non-manifold and boundary counts that need the seam-aware checker before acceptance.
- The configured humanoid profile lists 24 FPS for idle, move, and attack, while all selected zombie exports and the entity timing comments use 30 FPS. Resolve this contract before changing event times or rebinding actions.

## Runtime package evidence

The checked-out unit consumers map the base zombie and seven specialized subunits to separate runtime entity packages. Each selected package has one mesh, eight registered action IDs, eight entity states, four material stream settings for char1.001, and three texture paths; every entity uses scale 0.8.

Current runtime mesh hashes match both the installed-mesh reimport receipt and selected export-report mesh hash for all eight models. Current runtime animation hashes match the selected export-report hashes for all 64 role files, and no two action files share an exact SHA-256. Existing action reimport reports cover eight roles per package with five distinct sampled bounds each; these checks rule out byte-identical aliases and static sampled bounds, but they do not replace per-bone channel or semantic review.

| Unit | Triangles | Decoded bones | Mesh height | Position-welded diagnostic: non-manifold / boundary edges |
|---|---:|---:|---:|---:|
| zombies | 31,054 | 24 | 7.351824 | 129 / 129 |
| infected_zombies | 31,039 | 24 | 7.351824 | 312 / 201 |
| rabid_zombies | 31,119 | 24 | 7.351824 | 112 / 81 |
| parasitic_zombies | 30,783 | 24 | 7.351824 | 554 / 296 |
| mutant_zombies | 31,282 | 24 | 7.351824 | 4 / 8 |
| undead_zombies | 30,474 | 24 | 7.351824 | 330 / 251 |
| necrotic_zombies | 31,153 | 24 | 7.351824 | 73 / 84 |
| demonic_zombies | 30,931 | 44 | 7.351825 | 36 / 50 |

The decoded heights align with the installed vanilla western_european_infantry.mesh baseline at 7.351824 units, infantry_rifle_entity scale 0.8, and effective runtime height about 5.881459 units. The measured vanilla mesh SHA-256 is F00FBADFDACDD1046F7119E62E2C47D644EA7A92D0F686B71D230BC843AEF8BA, and its entity is in the installed gfx\entities\units_infantry.asset.

The raw topology fields in the old reimport receipts report zero non-manifold and degenerate edges. The position-welded fields are a separate diagnostic after merging seam-split positions; I am not treating those counts as proven holes or authorizing any automatic weld or repair. Fresh seam-aware geometry analysis is blocked with the current live-versus-lock adapter mismatch.

The action reports show 30 FPS and varied frame ranges for the eight consumers: idle, move, attack, defend, support_attack, retreat, training, and death. The action proofs expose one imported io_pdx_rigAction name and sampled bounds, not the underlying per-bone curve inventory. Seven runtime meshes report 24 bones, and the demonic mesh reports 44; the receipts do not list bone names or vertex-weight coverage. The old September 25 base rig review found missing finger, thumb, and jaw segments on its earlier candidate, but that finding does not prove the same defect in the September 27 soldier replacement.

The October 3 demonic repair handoff documents a 44-bone wing rig and restored airborne attack/support-attack phases; the current runtime mesh and selected r2_v2 action hashes match that repair package. The September 27 variant handoff also records that a mutant knockdown flip was flattened by grounding. I found no later mutant repair receipt in the bounded package, and the handoff does not name the affected role, so this remains an unresolved semantic-motion review item.

The final texture header snapshot at 2026-10-06 03:27:15 +03 confirms that all 24 runtime maps now have 512×512 dimensions, DXT1 diffuse or DXT5 normal/specular encoding, and ten mip levels. Those structural properties meet the current BC1/BC3 full-mip delivery contract. The current runtime hashes do not match prior selected export/runtime-sync records, and no current-hash source DDS copy exists in the eight audited model roots; packed-channel semantics, compression error, and rendered material review remain unresolved.

## Source, job, and credit lineage

The base job at docs\assets\002_zombie_outbreak\models_3d\zombies\job.yaml still records the pre-rework 64-credit lineage and the September 25 refs\original\meshy_input.png hash 3723991B3EFC92D573CA1CB94CDC6177EB1D501EE5F207DB1613D4E50C3EB3BB. Its input manifest says source_search was not run and approves only that earlier candidate. The current base reference described by the September 27 handoff is refs\original\meshy_input_v3_soldier.png, SHA-256 26FC9188D6E497113EB483F79EF295696EC744A0C4BA8EC8D607B67577587D54; the current task and approval lineage is not reconciled into the base job or input manifest.

The seven variant directories contain source reference PNGs, including alternate infected and parasitic inputs, but they do not contain per-model input manifests, source URLs, creator/license terms, search records, refinement prompts, source-to-refinement comparisons, or approval receipts. The September 27 variant handoff describes portrait and legacy-model references, but the exact submitted input for each provider body task is not recorded per package.

The shared docs\plans\system_unit_model_rework_plans\credit_ledger.json lists 33 tasks and 470 credits across these eight job IDs. It lists body, rig, and two prime Text-to-Motion tasks for most jobs, plus an extra rejected body generation for infected_zombies. The September 27 base and variant handoffs also describe six preset actions per model, but the filtered ledger has no matching six-per-model meshy_animate task IDs. The old base job records 64 credits, while the September 27 ledger records a separate 55-credit base tranche, so cumulative provider spend is not reconciled. This audit used zero provider credits.

## Runtime coverage and companion packages

The eight current subunit mappings appear in common\units\zombies.txt at the base and specialized entries. The three armored variants reuse their specialized parent sprites. Wendigo remains on the vanilla infantry sprite and has no custom model package; keep it explicitly blocked pending an accepted package and runtime entity.

The seven specialized counter packages have large and on-map two-frame DDS files, but their handoff marks them needs_user_review pending parent visual approval. The base counter remains the prior runtime asset. The sourced unit-audio handoff contains CC0/public-domain candidates for the seven variants, but selection/order voice binding is blocked because the owning country or original tags and their full infantry consumers are unresolved; exact action-frame sync also remains pending. The base audio source manifest says role classification and source-to-runtime synchronization are still pending. These 2D/audio companion facts were read from the named handoffs only; no artwork or audio was changed or independently re-researched.

## Dependency and inspection limit

The current dependency lock hash is 1A1BCF6193231B3937C82C4E989E58D7C4E6B865C7B4D5A34DBE3E0E687E1341. The adapter config hash 788858E3DC9E7D43A1717C419815F23935DC031F7BEEB1D50B13601E8AEB8543 and its 32-operation array match the lock, but the locked 1.11.0 adapter source hashes currently disagree for two files:

- .tools\3d_pipeline\adapter\blender_worker.py: locked EA00AE8131A2C4AE042157FA8CB5A0BA88697048512821E054505C17B0C34142; current 387BB07463B9774FA47176F2C09A26068F6F15243E37AB358BCFBB5AAC121552.
- .tools\3d_pipeline\adapter\delivery_policy.py: locked A51E3DAF0BACCE281D4DF35DB4064F577C6668A88FC5E611964B52A0651F47D5; current DD0A2FE2506F14088BC811B418BE129579D3C9585FEE0EDF200B2F7FA32CEB91.

The live health response for request 7fcd966fee4a4112b2997b4e6ec0cd84 reported adapter 1.10.51, not the locked 1.11.0. That response verified Blender 5.2.2, io_pdx_mesh 0.91.0 loaded from the locked Blender 5.2 extension manifest, four enabled operators, and export_meshfile/export_animfile availability. The compatible archive hash 508643626FEFE78511903B1894B8B4D68C387EDD6228AD70487699A866886702 matches the lock. I stopped before inspect_scene, reimport_export, or any other adapter operation because the connected adapter version and two locked source hashes do not match.

The health receipt is docs\assets\002_zombie_outbreak\models_3d\zombies\logs\adapter\7fcd966fee4a4112b2997b4e6ec0cd84.result.json. No Blender Lab bridge was started, no HOI4 process or visible desktop window was opened, and no provider key check was needed because no Meshy operation was performed.

## Evidence created and parent follow-up

This audit created only the handoff and bounded read-only evidence in docs\plans\002_zombie_outbreak_plans\subagent_handoffs\models_audit_20261006_evidence\. The evidence includes current runtime mesh/action hashes, the matching prior reimport/export records, sampled action bounds, DDS headers and hashes, job/source/reference files, the filtered provider-ledger rows, and the dependency/health snapshot.

Meaningful validation completed: SHA-256 comparisons for all eight runtime meshes against existing installed-mesh reimport receipts and selected export reports; all 64 runtime actions against their selected export hashes; current DDS dimensions, FourCCs, and mip headers; source/entity/GFX/animation registration cross-checks; vanilla scale reference review; and source/task-manifest inventory.

Meaningful validation skipped: fresh per-bone action-channel and vertex-weight inspection, new decoded topology analysis, current material channel and compression-error review, and visual review of the new DDS maps. The connected adapter did not match the lock, so using its scene-inspection route would not be verified evidence.

The parent should first synchronize the connected adapter with the current lock and source files. Then re-run read-only mesh/animation inspection for bone names, influence histograms, per-bone channels, root motion, and seam-aware topology; bind the current 24 DDS hashes to a source manifest and verify packed PDX channels and decoded materials; reconcile the base and variant job/reference/provider manifests and action task IDs; verify the 24-versus-30 FPS profile conflict; and resolve the recorded mutant motion simplification. Parent review of counters, unit-audio selection consumers, action sound timing, live runtime wiring, and user in-game evidence remains outstanding.

I made no paid call or source/runtime/GFX/entity/gameplay edit, service restart, desktop action, or commit.

## Guidance and references read

Read AGENTS.md, .agents\skills\chaos-redux-3d-model-pipeline\SKILL.md, .agents\skills\chaos-redux-event-assets\SKILL.md, .agents\skills\chaos-redux-subagents\SKILL.md, .tools\3d_pipeline\README.md, the current job.yaml and dependency/profile configuration, and the named September 27 and October 3 zombie-model handoffs.
Read paradox_wiki\Entity modding - Hearts of Iron 4 Wiki.md sections on mesh registration (lines 25–43), entities (52–60 and 112–136), and animation registration (169–183).
Read paradox_wiki\Graphical asset modding - Hearts of Iron 4 Wiki.md, Object Types section (lines 246–281); it contains no pdxmesh model syntax.
Read installed vanilla gfx\entities\units_infantry.asset lines 12–52, gfx\entities\infantry.gfx lines 76–100, and gfx\models\units\animation.asset lines 235–292.
The installed game documentation folder contains no model, mesh, entity, or skeletal-animation documentation file, so the local vanilla definitions and offline Entity modding page were the available engine references.
Skills applied: chaos-redux-3d-model-pipeline, chaos-redux-event-assets, and chaos-redux-subagents.

## Evidence files

- docs\plans\002_zombie_outbreak_plans\subagent_handoffs\models_audit_20261006_evidence\runtime_bytes_and_existing_decode.json records per-unit runtime, reimport, action, entity, material-stream, texture-header, and source-image hashes.
- docs\plans\002_zombie_outbreak_plans\subagent_handoffs\models_audit_20261006_evidence\source_job_and_provider_lineage.json records the per-package job/reference-manifest inventory and filtered shared credit-ledger rows.
- docs\plans\002_zombie_outbreak_plans\subagent_handoffs\models_audit_20261006_evidence\dependency_route_snapshot.json records current locked adapter source checksums, the live health request, and the adapter-version blocker.

A parallel model agent changed the runtime textures during this audit; those changes are recorded as an observed current snapshot and remain owned by that agent. The parent should review the agent’s final source manifest and copy receipt after its work settles.
