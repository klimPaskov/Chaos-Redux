# Adapter 1.10.47 bounded repair release

Status: validated coherent adapter 1.10.47; the parent controls lifting the global maintenance hold.

The adapter adds `repair_explicit_mesh_winding_batch`, `repair_explicit_skin_batch`, and `replace_explicit_corner_normals`.
Each operation opens one SHA-256-bound immutable source, checks every mesh precondition before mutation, captures one full before/after/reopened scene fingerprint, and saves one new sibling with a unique report.
The operation accepts only `blend_rel`, `checkpoint_rel`, `expected_source_sha256`, `repair_spec_rel`, and `expected_repair_spec_sha256` in its payload.
The spec is a bounded UTF-8 JSON object containing only `meshes`, a list of 1â€“512 unique exact mesh records.
Each mesh record requires `mesh`, `rig`, `topology_sha256`, `selection_sha256`, and `review_evidence`.
All targets must exist locally, be approved working objects, use one exact existing armature modifier, and be free of shared mesh data, shape keys, mesh animation, constraints, library overrides and protected source flags.

Winding records also contain explicit `face_indices` and `angular_tolerance_degrees`, with a positive ceiling of 0.5 degrees, at most 100,000 faces per mesh and 200,000 per transaction.
No faces or undefined source normals are inferred.
The operation preserves source edge sharp values and attribute presence, positions, face membership, UV corner associations and all other attributes, then checks selected normal sign inversion and unselected directions within the declared native encoding tolerance.

Skin records also contain `vertices`, each with the existing exact `index`, `expected` and `replacement` fields.
Every expected and replacement map contains 1â€“4 finite positive weights whose sum is within 0.000001 of one; automatic normalization, zero weights and no-op rows are rejected.
Each term must remain positive when represented as native float32; underflow is rejected before mutation.
Source group indices are copied to ordinary integers before removal, so mutation does not depend on live RNA group references.
The maximum is 20,000 vertices per mesh and 200,000 per transaction.
All unselected weights remain exact.
Only selected weight entries and their derived deformed object bounds are excluded from the protected comparison.
The dimension vector occurs both at the object's top level and inside scalar RNA `settings`; both copies are excluded only for explicitly selected skin meshes.
The posed native fixture asserts that both copies actually change while all transforms and other settings remain exact.

Normal records also contain `corners`, each with `face_index`, zero-based `corner_index`, `vertex_index`, `expected_before` and `requested_after`.
Both vectors must be explicit finite unit triples; the operation never chooses or normalizes them.
Existing native `CORNER INT16_2D` storage is required.
The operation restores every unselected native short pair and source edge sharp value/presence after Blender encodes the selected directions, then verifies every unselected decoded direction and raw pair exactly.
Each selected raw pair must actually change, and each selected decoded direction must remain within the unchanged 0.5-degree ceiling of its requested direction before save and after reopen.
All positions remain exact, including selected vertices; only derived point normals at vertices incident to explicitly selected corners may change.
The maximum is 4,096 corners per transaction.

## Selection hashes and inventory

Hash canonical JSON with sorted object keys, compact separators, UTF-8 bytes and SHA-256, as implemented by `_promotion_digest`.
No vector or weight rounding is permitted.
The function `explicit_batch_repair.selection_records` is the executable contract.

- Winding: sorted selected face indices become records containing `face`, ordered `vertices`, and ordered source `normals` for that face's corners.
- Skin: sorted selected vertex indices become records containing `index` and sorted `[bone_name, weight]` pairs under `weights`.
- Normals: sort by `(face_index, corner_index)` and emit `face`, `corner`, actual `vertex` and the actual decoded source `normal`.

`inspect_mesh_landmarks` supplies the exact `_mesh_region_topology` hash, indexed topology records, decoded corner vectors and complete existing raw normal storage alongside its existing vertices, UVs and weights.
Its 16-mesh inventory bound is unchanged.

## Image memoization and focused material review

Each `_promotion_fingerprint` call owns a fresh image-datablock content cache.
Every material node and image consumer is still serialized; only identical image-content computation is reused inside that snapshot.
An optional uncached path and optional out-of-digest statistics provide equality and timing evidence.
Image contents, packed bytes, external paths and file hashes remain exact protected data.
The shared orphan and operation-scoped partition reconciliation policies remain unchanged.

The read-only `material_visibility` branch forwards the already accepted and validated `preview_region` and `preview_resolution` into all three original/clay culling-on/clay culling-off renderer calls.
Its receipt records identical framing and the source is reopened without any checkpoint save.

## Validation and limits

Native fixture: `.tools/3d_pipeline/reports/explicit_batch_repair_1_10_47_native.json`.
Production preflight: `.tools/3d_pipeline/reports/explicit_batch_repair_1_10_47_production.json`.
The fixture exercises two-mesh save/reopen transactions for all three operations, cached/uncached full fingerprint equality, deliberately corrupted protected surfaces, bad final-row preconditions before any mutation, and a different float vector that encodes to an unchanged raw pair.
Production checks use source files read-only and unsaved Blender memory only; no production checkpoint or runtime file is written.
Demonic winding uses its exact remaining reviewed per-mesh face lists; its skin preflight uses the explicitly mapped candidate supplied by the model worker.
The initial v5 skin preflight rejected a positive `Chest` weight of `1.5715232249491843e-49` because native storage became zero; the exact observed map is in `explicit_batch_repair_1_10_47_v5_skin_rejection.json`.
The adapter does not change candidate weights to avoid that guard.
The positive full skin preflight uses the author's `surface_skin_v6_nativefloat32.npz` and explicit metadata mapping, preserving those candidate values exactly through native float32 storage.
Mutant's already accepted weights and winding receive inventory/equality checks without another repair.
Parasitic's source corner, neighboring faces, UVs and raw storage receive read-only inventory; this release does not approve any requested replacement vector or claim visual/export acceptance.

No provider calls or runtime/model asset changes are included.
No simplification of the requested adapter safeguards is made.
Actual model shading, deformation, animation, export and reimport acceptance remain with the model workers and parent after the release hold clears.
The repository 3D model pipeline skill was used; no skill files were edited by this adapter worker.

## Files in this release

Adapter: `explicit_batch_repair.py` (new), `blender_worker.py`, `manual_creature_rig.py`, `material_visibility_probe.py`, `chaosx_blender_hoi4_mcp.py`.
Publication: `config/blender_hoi4_adapter.json`, `config/dependencies.lock.json` and the verifier-generated `reports/environment_report.json`.
Tests: `test_explicit_batch_repair.py`, `blender_explicit_batch_repair_integration.py`, and `blender_explicit_batch_production_preflight.py`.
Receipts: the native, production, release checksum JSON files and this handoff.
The production preflight also retains `demonic_skin_batch_source_preconditions_1_10_47.json` and `demonic_native_skin_inventory_1_10_47.json` for the worker's hash-bound continuation, along with the observed v5 underflow rejection and the exact derived-object diagnostic delta.
Existing concurrent edits are preserved; the parent owns the shared final commit.

## Final validation

The aggregate focused suite passed 121 tests with zero failures, errors or skips.
The published-build native fixture passed all three two-mesh sibling transactions and 32 deliberate guard failures, with exact save/reopen fingerprints.
Demonic production preflights passed 58 meshes / 5,455 winding faces and 296 meshes / 25,989 exact native-float32 skin replacements without saving a checkpoint.
The final source fingerprint used five image-content computations with 885 cache hits, versus 890 uncached computations; the entire fingerprint was identical.
Final measured elapsed times were 7.31 seconds cached and 69.27 seconds uncached.
The full source import closure contains 18 locked files, and verify_environment returned findings = [].
Release checksums and receipt hashes are recorded in explicit_batch_repair_1_10_47_release.json.
