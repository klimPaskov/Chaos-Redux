# Adapter 1.10.45 image-retention handoff

Disposition: implemented within the parent-authorized shared adapter repair.
The parent explicitly accepted reconciliation of a surviving image's consumer release after the exact source inspection proved that its packed pixels and image datablock survive.
Actual image disappearance remains a failure.

## Defect and repair

The 1.10.44 fingerprint collected image records only from material texture nodes.
The source checkpoint contains zero-user `boy_Rigging_Fwd:lambert4`, whose only image consumer reference points to packed `boy_Rigging_Fwd:file1`.
Blender drops the material while retaining the image with identical content and packed bytes, reducing its user count from one to zero.
The previous node-only image inventory incorrectly reported lost image content.

The 1.10.45 fingerprint hashes every `bpy.data.images` record and inventories native ID consumers, explicit material node bindings, embedded tree retention, user counts, local/library status, fake and extra users, protection flags, packed hashes, and external file evidence.
Native viewer buffers use the existing bounded, finite, exact pixel hashing procedure.
The exact all-images hash remains mandatory.
The only permitted inventory transition is complete release of the consumers belonging to the exact material IDs already accepted as removable orphans, with unchanged image identity, settings, content hash, packed hashes, path, file hash, and independent retention evidence.
The receipt records both complete before and after image rows and the reason for accepting that release.
Image disappearance, image addition, content drift, a new consumer, retained material consumption, protected or fake-user data, externally consumed trees, and packed-state or packed-byte changes remain failures.

## Files changed by this repair

- `.tools/3d_pipeline/adapter/blender_worker.py`: complete image content fingerprint, deterministic consumer inventory, and exact orphan-consumer reconciliation.
- `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py`: phase-patch tool contract description.
- `.tools/3d_pipeline/config/blender_hoi4_adapter.json`: adapter version 1.10.45.
- `.tools/3d_pipeline/config/dependencies.lock.json`: matching version and 17 source hashes.
- `.tools/3d_pipeline/tests/test_reimport_promotion_contract.py`: image collection in the existing Blender test double.
- `.tools/3d_pipeline/tests/test_orphan_image_retention.py`: 12 focused regression tests.
- `.tools/3d_pipeline/tests/blender_orphan_image_retention_integration.py`: disposable native save/reopen regression.
- `.tools/3d_pipeline/reports/orphan_image_retention_1_10_45.json`: native positive and negative evidence.
- `.tools/3d_pipeline/reports/orphan_image_production_readonly_1_10_45.json`: immutable source/candidate replay evidence.
- `.tools/3d_pipeline/reports/environment_report.json`: normal environment verifier output with no findings.
- This handoff.

The adapter, MCP declaration, config, and lock already contained uncommitted parent changes before this repair; those were preserved.
No provider route, Meshy operation, production model file, action, or other worker's fixture was changed.
No commit was created because the shared adapter files include the parent's earlier uncommitted work and the parent owns the final reviewed commit.

## Validation

All 73 focused unit tests passed: 12 image-retention tests, 29 promotion tests, 13 action-phase tests, and 19 release consistency/import closure tests.
The final native fixture ran successfully on locked Blender 5.1.2.
It proves one native save drops the orphan material while retaining identical packed image bytes, and rejects a later native save that actually drops the zero-user packed image.
It also rejects retained-image disappearance, retained-image content changes, and changed external texture file bytes.
The environment verifier returned `findings: []`.
Operation arrays match, the 17 locked source hashes match, the local import closure is complete, and Git-clean source bytes agree with raw working-tree bytes.

The full original-scene replay of `repair_2026-09-09_death_text_to_motion_v1.blend` against the already-saved `repair_2026-09-09_death_motion_manual_v2.blend` passes, excluding only the existing candidate's new action `zombies_death_motion_manual_v2`.
Both checkpoints remained byte-identical throughout this read-only inspection.
Their complete image hash is identical: `DF61220512EDEEC297222794A420FAB9DF82F402C672D3B20D4F6CC94D275464`.
The retained packed orphan image hash is `251D19FF2C1319CAE198F364282A00DEB1D626AA31CEF365B9298BAD9609A5AB`.

## Release checksums and limits

Adapter version: `1.10.45`.
Worker SHA-256: `690EAF9B3C33C37F8EEFB7CA5B737EFD47DE7FA24677F03CF494196927CF84A0`.
Dependency-lock SHA-256: `3911B1AAEA062ABACDEDA21639A5A3C33472574E79500234F77403F60EE38680`.

No simplifications were made to the final parent-approved repair.
The repair deliberately does not approve any image loss or alter retention flags to manufacture persistence.
This is adapter preservation evidence and does not establish animation quality, runtime model acceptance, or in-game completion.
The source/candidate replay did not rerun or modify the production action patch; model workers can generate their next checkpoint through the reviewed release.
Skill used: `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`.
