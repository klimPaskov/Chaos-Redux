# Variant zombie adapter capability brief

Status: implementation request to the parent-owned adapter maintainer.
This brief does not add callable tool names, relax guards, approve geometry or actions, or authorize a runtime promotion.
The four package workers remain on the parent's global maintenance hold until coherent adapter hashes are published.
These are Blender-only repairs with zero provider operations and zero credits.

## Practical multi-mesh requirements

The Demonic package contains 296 mesh objects sharing three source texture images through many material graphs.
The first explicit winding transaction took 143.865 seconds for 37 faces on `mesh.007`; the second took 121.790 seconds for 47 faces on `mesh.009`.
Both completed with native save/reopen preservation evidence.
The current single-mesh operations repeatedly fingerprint all 296 graphs and their repeated image content.
After these two transactions, 5,455 reviewed winding candidates remain across 58 meshes, and the current skin candidate changes 25,989 vertices across 296 meshes.
The largest individual skin mesh has 3,229 vertices (`mesh.155`).
Neither winding nor the candidate skin is accepted as a finished package.

The smallest independent performance improvement is snapshot-local memoization of immutable image content during `_promotion_fingerprint`.
Cache image pixel, packed-file and source-file byte reads only within one fingerprint snapshot; every node/material consumer and its settings must still be serialized separately.
Start a fresh cache for the after-mutation snapshot and again after reopening the saved checkpoint.
Do not reuse a cache across operations, source loads, mutations or checkpoints.
The cached and uncached complete fingerprint structures and SHA-256 values must be identical on representative sources.
Report cache hits/misses and timing without excluding image consumers, image settings, content or packed bytes from any invariant.
This improvement does not require widening the public mutation contract.

Batch operations would additionally avoid repeated source loads, saves, reopens and full-scene checks.
The following schema names are proposals for the maintainer, not claims about deployed tools.

### Explicit winding batch

Retain the existing `repair_explicit_mesh_winding` semantics, applied to an explicit per-mesh map in one source-bound transaction.
Top-level fields: `job_id`, `blend_rel`, `checkpoint_rel`, `expected_source_sha256`, and `meshes`.
Each mesh entry should contain exactly:

```json
{
  "mesh_name": "mesh.014",
  "expected_topology_sha256": "<native inventory hash>",
  "face_indices": [0, 1],
  "angular_tolerance_degrees": 0.25,
  "review_evidence": "<job-relative evidence path and hash>"
}
```

The example indices illustrate the contract only; the actual accepted candidate face lists come from the cited job evidence.
Require unique exact local working mesh names, no protected/shared/library data, exact source/topology matches, unique existing face indices, triangular topology, explicit aggregate mesh/face limits and no inferred selection.
Validate every entry before changing any mesh.
Preserve all vertex positions, face-to-vertex membership, UV associations, material indices, weights, group identities, object matrices/parents/modifiers, rig/bones, locators, actions/curves/NLA, materials, image content/consumers and scene settings.
Only the listed triangle orientation and its explicitly permitted corner-normal sign may change.
Keep the default 0.25-degree guard and require a separately evidenced per-job exception for values up to the existing absolute 0.5-degree ceiling.
Do not auto-flip other components, weld vertices, reset normals, fill holes or normalize transforms.
Return exact input-map and per-mesh face-list hashes, source/final checkpoint hashes, each topology before/after, preserved-section hashes, and every mesh's maximum native/reopened corner error and worst corner.
Save one new sibling checkpoint, reopen it once, and repeat all exact-target and full-scene preservation checks.
The output remains pending native culling-on/off visual and export/reimport review.

### Explicit skin batch

Prefer retaining the existing file-based `repair_explicit_skin` contract, with a hash-bound aggregate JSON containing explicit per-mesh specifications.
Top-level fields: `job_id`, `blend_rel`, `checkpoint_rel`, `expected_source_sha256`, `skin_spec_rel`, `expected_skin_spec_sha256`.
The aggregate JSON should contain `meshes`, each using the current exact per-mesh schema:

```json
{
  "mesh": "mesh.155",
  "rig": "chaosx_demonic_zombies_rig",
  "topology_sha256": "<native _mesh_region_topology hash>",
  "review_evidence": "<explicit visual ownership review path and hash>",
  "vertices": [
    {
      "index": 0,
      "expected": {"Chest": 0.5, "Spine": 0.5},
      "replacement": {"Chest": 0.75, "Spine": 0.25}
    }
  ]
}
```

These example weights are schematic, not approved Demonic vertex assignments.
The native inventory must supply every actual prior weight, topology hash and vertex index before a production specification is accepted.
Retain the existing 1–4 positive finite named influences, already-normalized sum within 1e-6, prior-value comparison within 1e-7, exact existing bone/group identities, unique indices, no no-op rows and per-mesh 20,000-vertex cap.
Add explicit finite aggregate mesh/vertex/spec-byte limits that accommodate this measured 296-mesh/25,989-vertex job; do not make inputs unbounded.
Preflight every prior expectation and dependency before changing any vertex.
Only listed weights may change; preserve all geometry, vertex/edge/loop/polygon identities and positions, UVs, corner normals, material bindings/content/images, skeleton, actions, constraints, transforms and every unselected weight.
The existing allowance for selected meshes' derived deformed bounds may remain; it must not hide rest geometry or object-transform changes.
Return per-mesh changed-vertex counts, topology/prior/replacement/untouched-weight hashes, exact source/spec/final-checkpoint hashes and full invariant proof before and after reopening.
On a failed guard, do not publish a checkpoint as accepted or silently process a subset.
The output remains pending native limb ownership, contact/deformation, semantic action and actual-byte export/reimport review.

### Native inventory needed for exact skin expectations

`inspect_mesh_landmarks` already accepts up to 16 explicit meshes and emits vertices, triangles and optional weights.
Add the exact `_mesh_region_topology(mesh.data)` hash per mesh to the same read-only inventory, with the hash policy version documented.
Include the underlying indexed edge, loop and polygon/material records if required to make that hash independently reviewable; retain bounded pagination/file-output limits.
Keep the source SHA-256, mesh names, counts, vertices, weights and source-unchanged proof.
This avoids 296 additional single-mesh inspections solely to obtain the topology token required by `repair_explicit_skin`.
Do not substitute a different faces-only hash for the existing topology contract.

## Representative evidence

Paths below are relative to `docs/assets/002_zombie_outbreak/models_3d/` unless stated otherwise.

| Package | Evidence and measured outcome |
|---|---|
| Mutant | `mutant_zombies/blender/reports/04_exact_weights_geodesic_v15_part1.json` and `...part2.json`; native requests `5849b99fffe0455794b2e28188dade1d` and `6ab354bcffa446198ccb6952d7bc477e` applied 25,774 explicit normalized weight records in two batches and preserved topology/UVs/rig/actions/materials. |
| Mutant | `mutant_zombies/evidence/finalize_2026-09-12/orientation_ray_review.json` contains the 4,351-face exact list; `blender/reports/04_exact_weights_v15_winding_v1.json` verifies all 90,000 corners before/after reopening, maximum 0.4281466899 degrees under the documented 0.45-degree exception. Source positions, UVs, skin, rig, actions and materials are preserved. |
| Mutant | Selected winding checkpoint `mutant_zombies/blender/checkpoints/04_exact_weights_v15_winding_v1.blend`, SHA-256 `C35FDC44D199F36F377844644D6B143F5D7FBB2248E7480B41853F07F06C67CF`; native request `2610016d0ace490dbdc0a4e37116d24a`. Paired previews use prefixes `seam_winding_before` and `seam_winding_after`; before request `85ecfec11c9a48b1bfa5a511ecfd72a4`, after `8a25b8dbdb1947f0b2dfe2265fac75eb`. Viewed original front/rear and clay ON/OFF show the large face/chest/thigh/ankle gaps removed. |
| Mutant | `mutant_zombies/evidence/20260912T154314511853Z_chaosx_blender_hoi4_inspect_scene.json`, request `df6c3407302b4634be630f0e87667874`, checks all 53 attack frames: minimum surface Z 0.000999719–0.001000270, all 25,774 vertices normalized with at most four influences and no unweighted vertices. Native attack views show the former arm-to-leg sheets removed. Death remains under articulation repair; no final action export approval. |
| Necrotic | `necrotic_zombies/evidence/necrotic_finalize_child_2026-09-12/baseline_landmarks.json`, native request `cf4a4f06a74849d8ac1dd0e1f9fc99e7`, supplies measured native rest/weights. `declared_phase_audit.json` records baseline attack maximum edge stretch 188.24×. Native attack request `2ab5db7b20d94e0ca56c8abf5b84e64c` and `blender/previews/necrotic_child_attack_v1_020_focused_2ab5db7b20d9_three_quarter.png` show the failing bands. |
| Necrotic | `necrotic_zombies/evidence/necrotic_finalize_child_2026-09-12/connected_skin_weights_v1.npy` and `connected_skin_candidate_review_v1.json` describe 20,154 changed vertices with at most four normalized weights. Numeric candidate attack maximum is 2.37×, and idle/move/training are below 1.57×; these numbers are not native acceptance. The owner is preparing exact JSON prior/replacement records. |
| Necrotic | `necrotic_zombies/blender/checkpoints/04_necrotic_child_winding_main_v2.blend`, SHA-256 `60051F662A3E548BF4F13636C53FFA8220E59F218EB237D1BB59F7AC31C28D4B`, native request `19a1c8bb52c54a78a5cce69371aa26b1`, retains the exact 5,479-face candidate with maximum native/reopened corner drift 0.488178 degrees under its documented 0.5-degree exception. Paired after request `5ba261a8a3dc48ed8c73a145f345b1fa` shows continuous face/torso/limbs. |
| Demonic | Current working source `demonic_zombies/blender/checkpoints/06_df_winding_02.blend`, SHA-256 `0C0D094809547615EF27587612C44761FE5D78D5612DE285AC43FD84B214B8BB`. Winding01 request `490f81f00c264fdaa69726d0ff38fd5e` took 143.865 seconds; winding02 `c7ee20ad561747b4a6646a22506384c7` took 121.790 seconds. Receipts live in `demonic_zombies/evidence/demonic_finalize_child_2026-09-12/receipts/`. |
| Demonic | `demonic_zombies/evidence/finalize_2026-09-12/orientation_ray_review.json#candidate_faces_by_mesh` contains the original 60-mesh/5,539-face candidate; `mesh.007` and `mesh.009` are already applied, leaving 58 meshes/5,455 faces. Each remaining face list still requires its per-mesh native/reopened/culling proof. |
| Demonic | `demonic_zombies/evidence/demonic_finalize_child_2026-09-12/surface_skin_refined.npz`, `surface_skin_refined_design.json`, `surface_skin_design.json`, and `surface_skin_refined_role_stress.json` contain numeric candidate/provenance/stress evidence for 25,989 vertices across 296 meshes. The inherited baseline death has p99 edge stretch 5.62× and maximum 61.50×, with numeric native reconstruction error around 4e-6. Native exact prior weights and per-mesh topology tokens remain required before mutation. |

## Separate Parasitic selected-corner normal requirement

The current blocked call is `repair_explicit_mesh_winding` request `71548b44eb9e49c29738b0a316f53eeb`, from `parasitic_zombies/blender/checkpoints/05_contact_v19_death.blend`.
Its exact 4,838-face list is in `parasitic_zombies/evidence/finalize_2026-09-12/orientation_ray_review.json#candidate_faces_by_mesh`.
The worker rejected native encoding drift of 0.5442289240 degrees at selected face 24825 / vertex 24819 before saving; `05_contact_v19_death_winding_v1.blend` does not exist.
No tolerance above 0.5 degrees is proposed or permitted.
The complete failure evidence is `parasitic_zombies/logs/adapter/71548b44eb9e49c29738b0a316f53eeb.result.json` and its paired request/driver receipt.

The exact triangle is `[24820, 24838, 24819]`.
Two of its edges are open source-index/UV seams; only edge `[24819, 24820]` has a second source face, 24806.
Consequently the closed-boundary `repair_explicit_mesh_patch` contract cannot replace this one triangle solely to correct its normal.
Do not widen the patch boundary, add geometry, delete the face, omit its required winding repair or modify unrelated source components to evade the normal guard.

At the failed corner, the intended sign-corrected normal was `[0.7312900424, 0.2002395689, -0.6520114541]` and native encoding returned `[0.7338870764, 0.1911046505, -0.6518349648]`.
The original source corner direction is the negative of that intended vector because the face was explicitly selected for reversal.
The corner's source vertex position from the protected native inventory is `[1.0709046125, -0.1973058730, 3.7612671852]`.
This is an encoding limitation, not permission for a broad normal reset.

The required new narrow contract is explicit selected-corner normal replacement, either as its own transaction or a tightly scoped extension of exact winding repair.
Require a source/checkpoint SHA guard, exact mesh/topology, exact face/vertex corner identity, expected source normal and explicit reviewed target unit vector or a separately declared geometric-normal mode for that selected face.
Any geometric mode must calculate the direction from the actual indexed face under the declared post-flip orientation; it must not infer other targets.
An unknown/duplicate/mismatched corner, non-unit/nonfinite vector, singular transform, unreviewed corner, or native encoding beyond the existing 0.5-degree ceiling must fail closed before publishing.
Preserve every nonselected corner direction and all positions, connectivity, UVs, weights, rig, actions, materials, images and object/scene settings.
Report each selected corner's original, requested, encoded and reopened vectors and angular deltas, plus all untouched-corner and full-scene invariant hashes.
The package owner will obtain native corner/UV evidence, select any proposed replacement deliberately, and review original/clay culling views after the capability is verified; this brief does not choose an uninspected final normal.

## Verification and ownership

Use the fresh lock-selected wrapper and `BlenderAdapterClient`, not the stale direct MCP session route that still advertised adapter 1.10.44.
The last accepted 1.10.45 lock hash before this maintenance hold was `3911B1AAEA062ABACDEDA21639A5A3C33472574E79500234F77403F60EE38680`; worker hash was `690EAF9B3C33C37F8EEFB7CA5B737EFD47DE7FA24677F03CF494196927CF84A0`.
These are historical receipt anchors, not authority to call a source tree under modification.
Publish coherent new source/schema/lock hashes and run valid/rejected fixtures, a representative native save/reopen transaction and source-immutability checks before releasing workers.
Do not replay uncertain mutations blindly: inspect saved reports/checkpoint bytes and use a fresh source-bound read-only verification first.
All capability implementation and shared adapter/config/lock changes belong to the parent or its adapter maintainer.
All runtime wiring remains parent-owned, and no in-game validation is claimed.
