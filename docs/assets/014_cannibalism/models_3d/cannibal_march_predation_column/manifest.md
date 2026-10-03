# CURRENT Reconciled Model Manifest: cannibal_march_predation_column

Reconciled 2026-10-03 from the accepted runtime handoff, the installed-binding receipt, the package job, and retained package records. This is a new current reconciliation, not a recovered original manifest.

**Status: needs_user_review.** The mesh and eight animation exports match their installed bytes. The approved reference image, provider downloads, package texture/audio source files, and named reimport checkpoints are absent; upstream source provenance and semantic/live acceptance remain unresolved.

## Package and consumer

- Profile: humanoid_unit; asset cannibal_march_predation_column, Event 014 cannibalism.
- Unit consumer: common/units/014_cannibalism_irregular_infantry.txt#cannibal_march_predation_column.
- Entity: cannibal_march_predation_column_entity; runtime model root: gfx/models/units/014_cannibalism/cannibal_march_predation_column/.
- Current installed-binding receipt: docs/plans/014_cannibalism_plans/evidence/2026-10-03_runtime_unit_bindings_after.json. It states that its scope is runtime bindings without visual or in-game acceptance.
- Primary accepted selection/runtime handoff: docs/plans/014_cannibalism_plans/subagent_handoffs/event014_cannibal_march_predation_column_runtime_wiring_2026-08-25.md.

## Selection and source provenance

- The accepted handoff and job.yaml record parent approval for refs/original/meshy_input.png at SHA-256 9523DBF13601E7AE8ACB3B58013700209D19BCA6C3866B8932FB6E8D18C91289 and record source mode reference_only_user_authorized.
- The approved image file is absent, so its recorded SHA cannot be recalculated.
- The accepted underlying artwork page, title, creator/publisher, stated terms, retrieval date, exact-art authorization record, exact ImageGen prompt, and source-to-refinement comparison remain unknown.
- The modern source manifest records unlicensed Mobalytics artwork as research-only with no provider-input approval. The other source manifest and gfx_handoff.md identify Fernand Cormon’s archival work as superseded. Neither is promoted as the accepted source.
- The surviving ImageGen prompt summary is not bound to the accepted image and cites a different final image hash. This reconciliation preserves the accepted exact-SHA selection record and does not substitute an older candidate.

## Selected files and current hash reconciliation

The selected package mesh and action exports were established from the accepted runtime handoff plus their exact export and reimport receipts before comparing source and destination bytes. All nine package export SHA-256 values match the installed runtime files and the 2026-10-03 after receipt.

| Role | Package source | Installed runtime path | SHA-256 | Result |
|---|---|---|---|---|
| Mesh | docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/exports/cannibal_march_predation_column.mesh | gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column.mesh | dc6d2f19c25c8c2e2ee83d7ea01124248c3917d203e41c9b5368f563225cbc9e | source/runtime match |
| Diffuse | source file absent | gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column_diffuse.dds | 10c45d8582d60acaa0f9401d0ac7a1d94f6fe198977ed1bbdfaf9ad70411a6bf | runtime/receipt match; source link unknown |
| Normal | source file absent | gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column_normal.dds | 4a306cdb30f82fd14e264ecdc52257e28790b265d1d58402e59feae8b139c4f2 | runtime/receipt match; source link unknown |
| Specular | source file absent | gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column_specular.dds | 8b42e70bb0fd8371c0d7287776d1729e2c6eed9dcb29b478115dd9202657ffce | runtime/receipt match; source link unknown |
| Idle | docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/exports/cannibal_march_predation_column_idle.anim | gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column_idle.anim | a26093c954e64e3d42535d3cd268ab182e912fa101f8721ce6bf6a07348efb87 | source/runtime match |
| Move | docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/exports/cannibal_march_predation_column_move.anim | gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column_move.anim | 38bee278c0870ee3c93498490298a7592458200003760a173e5a004a889c067e | source/runtime match |
| Attack | docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/exports/cannibal_march_predation_column_attack.anim | gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column_attack.anim | 2113c2ecfd40e0c4da51cb23082e4fd4ab8f26e93d9edd60acaa2e8d527e9822 | source/runtime match |
| Defend | docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/exports/cannibal_march_predation_column_defend.anim | gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column_defend.anim | 2b66262a82e93d8700fefdcaf930dd99b03dcf1077aa18750470ee75fec2537c | source/runtime match |
| Support attack | docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/exports/cannibal_march_predation_column_support_attack.anim | gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column_support_attack.anim | f6209d3e27d7a16d3a32a491746025115ad9ec18a02f07f2814544db7870d408 | source/runtime match |
| Retreat | docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/exports/cannibal_march_predation_column_retreat.anim | gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column_retreat.anim | 99bfcbb207f589893717b6516994c97c15f14126627955f014265809c47087ec | source/runtime match |
| Training | docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/exports/cannibal_march_predation_column_training.anim | gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column_training.anim | fd1304e22cfa6f008c116ef69c97ec74904afa725bbe57bf57c717cf8c998e6f | source/runtime match |
| Death | docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/exports/cannibal_march_predation_column_death.anim | gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column_death.anim | 1ef861b647ee72786e39bb70dfebd921c632fa0d23292a7941699dcbe6c85a84 | source/runtime match |

The installed DDS maps are 1024x1024 RGBA per the after receipt. Their package-side DDS sources and copy records are absent, so only installed-file-to-receipt hashes are verified.

## Animation and rig evidence

| Role | Frames | Export/installed FPS | Job-declared FPS, loop, root policy |
|---|---:|---:|---|
| Idle | 177 | 30 | 24, loop, in_place |
| Move | 35 | 30 | 24, loop, in_place |
| Attack | 152 | 30 | 24, non-loop, in_place |
| Defend | 152 | 30 | 24, non-loop, in_place |
| Support attack | 22 | 30 | 24, non-loop, in_place |
| Retreat | 45 | 30 | 24, loop, in_place |
| Training | 157 | 30 | 24, non-loop, in_place |
| Death | 67 | 30 | 24, non-loop, contact_corrected_collapse |

The package records eight Meshy action provenance JSON files with source reference IDs, action IDs, source names, FPS, and hashes. The provider/v9_task_lineage.json file is absent. The generation task, rig task, GLB hash, and FBX hash exist only as job.yaml records; the GLB and FBX files are absent.

The accepted runtime handoff says the live adapter 1.10.14 exported the grounded mesh and eight actions. job.yaml still records an adapter 1.10.3 versus 1.10.4 pause, and older dependency evidence records 1.8.1. Current adapter or extension verification was outside this metadata-only task. The job’s 24 fps action contract conflicts with the accepted handoff and installed/export receipts at 30 fps.

Export and reimport JSON reports are retained. The named reimport Blend checkpoints are absent. Report existence does not establish visual, semantic, contact, deformation, or live acceptance. The accepted handoff explicitly leaves exact bow draw/release semantics as a visual-source caveat.

The mesh export and reimport reports record node char1.002, 24 bones, 30,000 triangles, 39,977 reimport vertices, zero reported non-manifold edges, and zero degenerate faces. The export report also records 14,885 position-weld diagnostic vertices and 126 loose boundary edges. These are retained report values, not a fresh geometry audit.

Job-recorded vanilla scale calibration uses western_european_infantry.mesh#polySurface106: source height 7.351824797689915, entity scale 0.8, effective runtime height 5.881459838151932, forward -Y, and up +Z. No recalibration was performed.

## Sourced sound package

The source URLs, recorded attribution/terms, and mechanical transformation notes remain in evidence/audio_sources/provenance.md; format and source/derived hashes are in evidence/audio_sources/ffprobe_and_hash_receipt.json. Installed audio paths and hashes are in the reconciliation receipt.

The 2026-10-03 after receipt hashes match the installed bytes for all six model-scoped files. The package’s derived and original audio files are absent. Five installed audio hashes equal the derived hashes in the retained ffprobe receipt; the death WAV differs: installed/after-receipt SHA-256 is 6cfc465fe458edcc3b8d072fc68cc00eff6a292eb445f3505097623425431c67, while the retained derived-file receipt records 98a0dfee4b55b921f103d067edb7492e751466a13894d4a04a30398299acf158. The copy relation is unresolved.

The provenance describes a selection/acknowledgement candidate, but it is absent from the model-scoped installed audio entries. Its active runtime binding is unknown.

## Counter handoff

The existing counter audit records three bespoke consumers: large GFX_unit_cannibal_march_predation_column_icon_medium at 152x42 with two 76x42 frames; on-map GFX_unit_cannibal_march_predation_column_icon_medium_white at 60x12 with two 30x12 frames; and texticon GFX_unit_cannibal_march_predation_column_icon_small at 60x12 with two 30x12 frames.

The audit records installed vanilla subuniticons.gfx and texticons.gfx inspection, infantry large/on-map/texticon DDS precedents, the matching skill-local counter reference families, and palette anchor RGB(73,106,73). It records the bespoke art package as existing with parent wiring pending. This pass did not re-audit counter bytes or wiring.

## Reconciliation evidence and limits

The detailed SHA-256 source/runtime receipt and exact proof-record paths are in evidence/manifest_reconciliation_2026-10-03/reconciliation_receipt.json.

Missing upstream artifacts are the accepted reference image, provider GLB/FBX and lineage JSON, package DDS sources, original and derived audio bytes, and named reimport Blend checkpoints. The current archive reports no archival manifest before this reconciliation.

No source was substituted, no feature requirement was simplified, and no 3D/provider/health/game operation or runtime/gameplay wiring edit was made. This manifest does not claim overall Event 014 completion or live-game acceptance.
