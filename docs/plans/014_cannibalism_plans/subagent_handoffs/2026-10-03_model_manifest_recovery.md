# Event 014 Feast Guard manifest and selected-export recovery

Disposition: implemented for Feast Guard archive recovery and current manifest only; the parent owns remaining model-manifest reconciliation.

The source export at docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/export/mesh/cannibal_feast_guard.mesh is a newly reconstructed exact-hash artifact, not a restored original file or a rerun Blender export.

The recovered source export is 3,712,499 bytes with SHA-256 4f2f8e22b2e479521e48b627d3769383ff48ddd6c95b8ec197639c7068fe7fee.

It was reconstructed from the read-only installed runtime mesh at gfx/models/units/014_cannibalism/cannibal_feast_guard/cannibal_feast_guard.mesh, SHA-256 be457d575838d7126db2a1da97f516814258e2116eb10e449250daba6ca6e24f, by inverse rebasing exactly three PDX length-prefixed texture strings.

The vendored io_pdx_mesh.pdx_data.parseData checks verified each string length, the preserved s/count-1 prefix, trailing NUL, exact historical source hash, decoded-tree equality after those three name changes, and an exact inverse round-trip; the runtime mesh hash remained unchanged.

The exact recovery receipt is docs/plans/014_cannibalism_plans/evidence/2026-10-03_model_manifest_recovery/feast_guard_inverse_rebase_receipt.json, SHA-256 b718a64f2ba610af10b84823163b5df93c103e1ca32b424c7c6e7c962490879f.

The current root manifest is docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/manifest.json, SHA-256 6175d186a34e8f8e10ca846a8ed7b127a6012dd11232a3e5799a8a80a586e77d.

Its human-readable counterpart is docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/manifest.md, SHA-256 65a16b6ced2e3f4bfc3e8025905b6f0c0b5ab4f711502a46ca836f5a5e30a110.

The source mode is recorded as user-provided based on docs/plans/014_cannibalism_plans/014_cannibal_model_source_direction_2026-08-22.md:19, which identifies the C67 hash as the faithful approved input.

The raw C67 source bytes remain absent; the parent reports that a bounded search across 200 current Event 014 images and the durable portrait archive found no match.

The creator, source page, stated rights, exact preparation prompt, and source-to-refinement comparison remain unresolved because the raw source is unavailable.

No retained receipt links C67 to the historical generation, rig, animation, or export tasks; the recovered mesh closes the selected-export archive gap only.

The current installed-byte audit at docs/plans/014_cannibalism_plans/evidence/2026-10-03_runtime_unit_bindings_after.json, SHA-256 a9dc4753057922ff00d1c06c0658625a8c79b75a90d8325a394555f91c0ebb76, supplies the installed mesh, action, material, audio, and consumer path/hash inventory.

The new manifest marks source rights, provider linkage to C67, action-source bytes, texture/audio source synchronization, and live consumer review according to their retained evidence; it does not claim package or in-game completion.

No Meshy, Blender, adapter health, export, reimport, runtime-copy, source-wiring, gameplay, GFX, audio-generation, or spreadsheet operation was performed; paid credits consumed in this handback are zero.

Feast Guard artifacts created or changed in this handback are docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/export/mesh/cannibal_feast_guard.mesh, docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/manifest.json, docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/manifest.md, docs/plans/014_cannibalism_plans/evidence/2026-10-03_model_manifest_recovery/feast_guard_inverse_rebase_receipt.json, and this handoff.

The previously existing Feast Cohort manifest.md bytes were preserved at docs/plans/014_cannibalism_plans/evidence/2026-10-03_model_manifest_recovery/historical_cannibal_feast_cohort_manifest_2026-10-03.md before that stale markdown was updated.

Partial files created in the other model roots before the parent narrowed this handback are docs/assets/014_cannibalism/models_3d/cannibal_feast_cohort/manifest.json, docs/assets/014_cannibalism/models_3d/cannibal_feast_cohort/manifest.md, docs/assets/014_cannibalism/models_3d/cannibal_bone_guard/manifest.json, docs/assets/014_cannibalism/models_3d/cannibal_bone_guard/manifest.md, docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/manifest.json, and docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/manifest.md.

No manifest was created for cannibal_march_predation_column, and no further work was done on those four roots after the scope reduction.

No commit was created.
