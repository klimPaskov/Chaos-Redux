# Event 012 Africa — Disaster Wardens Meshy 7 redo handoff

Status: `blocked_provider_rig_failed_90_percent_refunded`.

## Current bounded Meshy 7 tranche — 2026-08-25

The active reference is the parent-approved `refs/original/meshy_input.png` at SHA-256 `B5C29A3DB993E5C88E980B0C12F79E4EE60E8958D907AA5DBAB0EEFBA70BA146`; all earlier reference and provider lineage remains quarantined under `provider/rejected/`.

The single bounded Meshy 7 generation task `01a038b8-9bc6-758a-9981-2a5c7dd65ac8` consumed 30 credits, accepted the 25,000-triangle geometry, and was downloaded immediately as GLB SHA-256 `1B73A95B382F8B9F780778BCA9FE4528976DC37FDCDFABBC2C3CC7F0BE525945` and FBX SHA-256 `652D99A6220907295F86ED1657ECAE906103EA0C95E76FE4281184A18FC59A38`.

The accepted candidate passed the complete firearm gate and geometry QA at 25,000 triangles, 12,503 vertices, four loose boundary edges, zero degenerates, and zero non-manifold edges.

The named vanilla calibration file `refs/vanilla/asian_infantry.mesh` measures 7.516803 m, while the stale job declaration remains 7.351825 m; the target source and effective runtime height remains 9.18978125 m at entity scale 1.0.

Rig task `01a038be-66f7-79aa-bd55-f9bd97eadc60` was first observed at 90% `IN_PROGRESS` after timeout and then reached terminal `FAILED` with `unexpected_error`, no download, and no action route. The final structured result consumed 0 credits and refunded the transient 5-credit estimate/lock; the observed live balance is 13, so the earlier timeout state and estimate remain historical evidence rather than final spend.

All required actions, export, reimport, and runtime promotion remain blocked because no terminal rig or approved action source exists; no `.mesh` or `.anim` runtime candidate was promoted and no in-game completion is claimed.

The package's current attributed total is 180 credits, comprising the 150 credits of quarantined old lineage and the 30-credit active generation; no further generation or animation spend followed the failed rig task.

The 2026-08-24 sections below are historical evidence only and are superseded by this current state; their task IDs, artifacts, hashes, and rejection reasons remain quarantined and must not be promoted.

## Historical final recovery and route isolation update — 2026-08-24

The adapter mismatch was isolated without terminating shared concurrent processes. The canonical direct repository wrapper/client passed health as adapter `1.10.0`, Blender `5.1.2`, io_pdx loaded, bridge listening, zero environment findings, and zero new surviving children in request `90e8b90d88dc4e389a180d1ab0a0f754`. The stale shared registered MCP route remains excluded. Full evidence is `docs/assets/012_africa/models_3d/disaster_wardens/evidence/adapter_route_isolation_2026-08-24.md`.

Recovery 5 task `01a03429-ae8c-7253-b32c-65eb6d80b05f` succeeded for 30 credits and was downloaded immediately (GLB `C620F2BC432AEBE804DB82970882B87785AC8FC34D84F0338E4DEA70E07A4F8D`; FBX `B054E54046F34D9C90B74C81C53029F4892BF259BF857A2E7C57CB0E1F8321ED`). Direct adapter `1.10.0` QA rejected it because A-pose removed the rifle and 742 loose boundary edges remain. Recovery 6 then attempted the remaining T-pose/provider-remesh/enhancement-off combination, but the direct Meshy wrapper returned no JSON-RPC response twice before task creation. No task ID or charge exists, and post-failure inspection found zero newly surviving Meshy route processes. The package stops blocked after five completed/rejected Meshy 7 generations and `150` package credits; no rig, action, conversion, export, or runtime promotion occurred. See `validation/evidence/meshy7_recovery_5_and_transport_stop_2026-08-24.md`.

## Historical provider recovery update — 2026-08-24

Fresh recovery authority produced three further non-identical Meshy 7 tasks from the unchanged approved input. Tasks `01a03402-77f9-7d7f-938e-cf6fae54148d`, `01a0340f-4af0-78be-a3f5-60157d98df46`, and `01a03419-e76f-7cd3-996d-d0d3ec181b5f` each succeeded and consumed a reconciled 30 credits, moving the balance `1500→1470→1440→1410`. All GLB/FBX outputs were downloaded immediately and checksum locked. The first two no-pose recoveries retained 16,643 and 16,339 loose boundary edges. The third enabled provider-side 25,000-triangle remeshing and reduced the post-repair count to 1,201, but did not close the model. All three also retain an action-infeasible rifle relationship: the butt is planted on the ground, the only contact is near/above the muzzle, and there is no trigger-hand, foregrip, or shoulder-stock contact. They were rejected before rigging.

The live Meshy schema has no literal `pose_mode=none`; omitting the optional argument is its compliant no-pose equivalent and was recorded for all three recoveries. The final variation kept that omission to avoid the first attempt's T-pose weapon relocation and enabled provider remesh specifically for topology. It still failed both hard gates.

The recovery-4 dependency mismatch was a historical stop gate. It was later resolved for this task by isolating the canonical direct repository wrapper/client at adapter `1.10.0`; the stale shared registered route remains excluded. Detailed task IDs, costs, hashes, QA metrics, previews, and immutable snapshots for recoveries 2–4 are recorded in `docs/assets/012_africa/models_3d/disaster_wardens/validation/evidence/meshy7_recovery_attempts_2_to_4_2026-08-24.md`.

## Historical outcome before the active reference replacement

The parent-approved reference was first submitted through the locked Meshy route with exact `ai_model=meshy-7`. Task `01a033db-bbd0-74b5-b7f3-f2aec86cb89c` succeeded and consumed 30 provider-reported credits. GLB and FBX outputs were downloaded immediately and checksum locked. That candidate preserves the disaster suit, respirator, hose, packs, complete humanoid anatomy, and palette, but it was rejected before rigging because Meshy relocated the source-held rifle into a waist/back intersection and the locally reduced working mesh retained 16,476 loose boundary edges. Fresh authority then permitted four completed recoveries; none passed. A sixth intended variation failed at the provider transport before task creation.

## Files changed or added

- `docs/assets/012_africa/models_3d/disaster_wardens/job.yaml`
- `docs/assets/012_africa/models_3d/disaster_wardens/manifest.md`
- `docs/assets/012_africa/models_3d/disaster_wardens/refs/source/source_search_2026-08-24.md`
- `docs/assets/012_africa/models_3d/disaster_wardens/refs/source/provenance.json`
- `docs/assets/012_africa/models_3d/disaster_wardens/refs/briefs/meshy_input_prompt.md`
- `docs/assets/012_africa/models_3d/disaster_wardens/refs/original/input_manifest.json`
- `docs/assets/012_africa/models_3d/disaster_wardens/refs/original/meshy_input.png` (parent-approved checksum-locked reference)
- `docs/assets/012_africa/models_3d/disaster_wardens/refs/derived/meshy_input_cleanup_candidate_2026-08-24.png`
- `docs/assets/012_africa/models_3d/disaster_wardens/refs/derived/meshy_input_cleanup_rembg_2026-08-24.png`
- `docs/assets/012_africa/models_3d/disaster_wardens/provider/rejected/reference_period_gate/kifir_firefighter_tip_a_cleanup_rejected_modern_4d48c5cc.png`
- `docs/assets/012_africa/models_3d/disaster_wardens/validation/evidence/reference_processing_2026-08-24.md`
- `docs/assets/012_africa/models_3d/disaster_wardens/validation/evidence/reference_cleanup_comparison_2026-08-24.jpg`
- `docs/assets/012_africa/models_3d/disaster_wardens/validation/evidence/reference_cleanup_comparison_recovery_2026-08-24.jpg`
- `docs/assets/012_africa/models_3d/disaster_wardens/validation/evidence/reference_cleanup_alpha_review_2026-08-24.jpg`
- `docs/assets/012_africa/models_3d/disaster_wardens/history.jsonl`
- `docs/assets/012_africa/models_3d/disaster_wardens/evidence/meshy7_redo_gate_2026-08-24.md`
- This handoff.

Previously licensed source candidates remain archived under `refs/source/`. The selected WWII-82 source was downloaded only transiently and deleted after review because the publisher states no archival permission; its fingerprint and a bounded source-to-cleanup review comparison are retained. The rejected substantially-original candidate remains quarantined under `provider/rejected/reference_cleanup_rule_violation/` and is not `meshy_input.png`. Existing audio and counter packages were not edited. No runtime, `.gfx`, `.asset`, sound definition, entity, gameplay, localisation, GUI, or spreadsheet file was changed.

## Historical dependency and provider evidence

The dependency and provider gates were rerun for this production tranche.

- First-process key gate: passed without exposing the key.
- Environment bootstrap: passed with no findings.
- Meshy: official pinned MCP `0.4.0`, exact `meshy-7` schema available, required tools present, and process-cleanup probe passed after cleaning only the first probe's explicitly identified descendants.
- Credits: balance `313` immediately before task creation; task-reported consumption `30`; post-task balance `253`. The 60-credit shared-account delta does not reconcile to this task and remains explicitly recorded as a mismatch.
- Blender: Blender `5.1.2`; adapter `1.9.2`; io_pdx_mesh `0.91.0`; adapter health request `59a748506fcb45c5810fd217ac2f7d4a`; installed vanilla source remeasured at `7.351824798`.
- Provider archives: GLB SHA-256 `9F1F9F6A7B43A3B74E1079D90BA46E5A8CC06F1885D1C4033F6CFFFA8CC9BAF2`; FBX SHA-256 `D27A1219AC69ED50A703AA4E7A14C0203934F21A757292AE2630E0C188DA0725`.
- Current route evidence: `docs/assets/012_africa/models_3d/disaster_wardens/evidence/provider_route_and_dependency_gate_2026-08-24.md`; consecutive and concurrent live schema SHA-256 `60B8EA7B35CFFBB43B8A07D4EF09CC53A6F835976C2BF90AF735731112660741`.
- Full lock, schema, request, checksum, source, runtime, sound, and counter evidence is in `evidence/meshy7_redo_gate_2026-08-24.md`.

## Historical parent approval — superseded reference

`docs/assets/012_africa/models_3d/disaster_wardens/refs/original/meshy_input.png` is present, 1254x1254 RGBA, SHA-256 `B73E80781FEC249AA7C96C95CC06BDBB499A3F6E1FD7EE5A601B27A75606AE80`. Parent visual review approved this exact checksum on 2026-08-24 after the color, period, fidelity, complete-subject, and genuine-alpha gates passed. Any byte change invalidates the approval. The source front-view fingerprint is `964C4C6DA29E9D0041F0C81F69066B2BCC75A53378FBC140DB3839C56D9331B0`. Review evidence is `validation/evidence/reference_cleanup_comparison_recovery_2026-08-24.jpg`, SHA-256 `B809B4921BC675B086DDF7969B1F3AD3511C2BA20802425AD3654F9DB20A2FA3`, and `validation/evidence/reference_cleanup_alpha_review_2026-08-24.jpg`, SHA-256 `082685CDB71173E34C3CA8FB1722B32801622573DF304692A769EFB51C2F782F`.

The single native cleanup returned opaque RGB with a flattened checkerboard, SHA-256 `4123D18419996FC75EDDD062506267EF43C249CD87C63CC391DA6A34D9A83525`. The authorized `rembg 2.0.61` fallback preserved those RGB bytes exactly and supplied deterministic alpha, producing the approved hash above. No Meshy or paid provider call was made while recording approval.

## Historical blocked production requirements

- Another provider recovery cannot begin while the live adapter reports `1.8.8` against locked `1.10.0`. Even after route reconciliation, the next attempt must remain non-identical and must pass both closed-topology and action-feasible trigger-hand/foregrip/shoulder weapon-contact gates before rig spend.
- Rig, weight validation, packed PDX material conversion, `.mesh` export/reimport, and ten distinct Meshy-sourced actions at 30 FPS are canceled for this rejected candidate.
- Rebind and resynchronize the accepted six sourced sound cues against the final provider actions.
- Parent-copy selected final source artifacts to the actual runtime root `gfx/models/units/012_africa_disaster_wardens` and update the current five-action registrations to ten distinct action files. Parent must record selected source/destination hashes.

## Preserved package decisions

- Audio: accepted for source provenance and file integrity. Originals and all six derived cues match the recorded hashes; `ffprobe` verifies their formats. Each derived cue is byte-identical to its current runtime copy. Existing frame numbers are stale until the ten final actions exist.
- Counters: accepted. Consumers are `unit_disaster_wardens_icon` and `onmap_unit_disaster_wardens_icon`; final DDS hashes are `328A801B131B59C9D8E0837B802DE7AF1F9501F9BED22890F265CC477982F22A` and `D86EE0F9F87C6212776864227F8E0C4EA189B04226397AA7E13222305E1D6AEE`. Both current runtime copies are byte-identical. No replacement `chaosx_icon_artist` handoff is needed.

## Historical completion boundary

The 3D redo remains incomplete and blocked after five successful but rejected Meshy 7 generations plus one provider-transport failure before task creation. Geometry was inspected and rejected; rigging, weights, final material conversion, animations, `.mesh`/`.anim` exports, and reimport validation were intentionally not performed. No in-game completion is claimed.
