# Read-only mesh-region inspection capability

## Scope and status

This adapter-only change extends the existing `inspect_scene` operation with an optional `mesh_region` object.
It reads the existing checkpoint and evaluates one explicitly named action/frame without saving a checkpoint, rendering, generating geometry, importing actions, changing materials, invoking a provider, or producing an approved muzzle transform.
The normal job-bound adapter request/result receipt is the only report writer.
Existing calls that omit `mesh_region` retain the original payload and inspection behavior.

The parent reviewed and locked the source as adapter version `1.10.18`; the parent retains configuration, operation-lock hashes, version refresh, and production-call authorization.
The synthetic native fixture passed under that exact lock, with its measured evidence recorded below.
No production checkpoint has been opened by this worker during this capability task.

## Exact API

Use the existing `chaosx_blender_hoi4_inspect_scene` tool, or `BlenderAdapterClient.inspect_scene`, with the existing `job_id` and job-relative `blend_rel`.
Region mode additionally requires exact nonempty `target_armature_name`, exact `action_name`, and an integer `preview_frame` within that action's native frame range.
The frame must be between zero and one million inclusive.
`render_previews` must be false; `runtime_stem` and `preview_view_names` must be empty.

The `mesh_region` object accepts only the following fields.

| Field | Contract |
| --- | --- |
| `mesh_name` | Required exact local mesh object name, at most 128 characters. |
| `bone_name` | Required exact existing bone in the named armature; defines the reported posed/rest bone-local spaces. |
| `expected_source_sha256` | Required 64-hex SHA-256 of the existing `.blend` bytes; checked before opening and after inspection with the unchanged byte count. |
| `expected_action_sha256` | Required native inspection fingerprint described below, not an exported `.anim` file hash. |
| `aabb` | Optional exact object with `space` equal to `WORLD` or `BONE_LOCAL` and finite three-number `min`/`max` arrays; bounds are inclusive, ordered, and within plus/minus one million units. |
| `weight` | Optional exact object with `bone_name`, `min`, and `max`; the bone and mesh vertex group must exist, and the inclusive finite range must be ordered within zero through one. |
| `offset` | Optional matched-vertex offset, default zero, bounded zero through one million. |
| `limit` | Optional requested page size, default 64, bounded one through 256 vertices. |
| `measurement` | Optional exact object containing `origin_vertex_indices` and `endpoint_vertex_indices`, each a list of one through 64 unique source-vertex indices. |

At least one selector (`aabb` or `weight`) is required.
When both selectors are supplied, a vertex must satisfy both.
Weight membership is measured from the original source mesh, while spatial membership is measured at the requested evaluated pose.
Measurement sets must be disjoint, and every named index must match the complete selector even if that vertex is outside the requested page.
The adapter rejects missing measurement indices, overlapping sets, nonfinite values, and zero-length centroid axes.

## Native action identity and receipt lineage

First call ordinary read-only `inspect_scene` on the same source checkpoint with the exact target armature, action, and frame, without rendering.
Read its existing `inspected_action_sha256` and pass that value as `mesh_region.expected_action_sha256` in the constrained query.
The fingerprint preserves the existing curve traversal order and hashes canonical JSON records containing curve slot identifier, data path, array index, and every key's frame, value, and interpolation.
The JSON uses sorted object keys, compact separators, and SHA-256 with an uppercase hexadecimal result.
This is deliberately the existing native action identity, not the SHA-256 of any accepted exported `.anim` file.

The region receipt reports `native_action_sha256`, its explicit policy identifier, the source checkpoint SHA-256/byte count, and a separate complete in-memory action-integrity fingerprint including key handles and native settings.
Existing action provenance is echoed as `action_provenance`, so any stored source-animation path/hash identity remains distinct from the native action fingerprint.
Existing promotion keys on the exact rig and mesh are echoed as `source_receipt_metadata`, including the original proof and validation-receipt paths/hashes where present.
That metadata is bound by the verified source checkpoint hash; the region operation does not fabricate, mutate, or independently revalidate the historical receipt.

## Returned measurements and boundedness

Each returned vertex keeps its original vertex index and original corner-loop/polygon indices.
Records include original mesh-local position, original world position, rest-bone-local position, evaluated world position, posed-bone-local position, original/evaluated normals, per-corner original/evaluated UVs, material index/name, and all original vertex-group memberships and weights.
The report includes mesh world/inverse matrices and posed/rest bone world/inverse matrices.
Normals use inverse-transpose coordinate transforms, including the world-to-bone-local normal transform, so positive nonuniform scale is not replaced by a uniform-scale approximation.
Negative and singular transforms are rejected.

The source and evaluated mesh must have identical indexed vertices, edges, loops, polygon membership, polygon material indices, and UV-layer identities.
The report records that topology fingerprint, source vertex/loop/polygon counts, total matched vertices, and a hash of the complete ordered matched-index list.
The source caps are one million vertices, six million loops, eight UV layers, and 256 vertex groups.
Pages contain at most 256 vertices and 8,192 complete corners; a corner cap ends the page before a partial vertex record, and a single vertex that exceeds the corner cap is rejected.
`returned_vertices`, `returned_corners`, `truncated`, `corner_cap_reached`, and `next_offset` explicitly describe pagination.
An offset beyond the matched count is rejected.

Optional measurement uses the caller-selected vertices' evaluated centroids, returns both complete index sets and counts, and reports origins, endpoints, and normalized axes in world and requested bone-local space, plus the world-space length.
It does not infer a gun, choose a muzzle face, fit a semantic weapon axis, supply roll, or create a quaternion.
`rotation_quaternion` is null and `semantic_muzzle_approval` is false.
These values are observed geometry evidence for the parent to review, not permission to author a locator.

## Read-only dependency boundary

Region mode supports one exact local mesh with exactly one active Armature modifier consuming the exact named local rig.
Linked/library-override objects or datablocks, object/pose constraints, shape keys, mesh-object animation, REST display, NLA tracks, drivers, multiple action slots, and modified action curves are rejected.
The rig must have no parent; the mesh may have no parent or an object-parent relationship to the exact named rig.
Animated mesh or armature datablocks are rejected so an external dependency cannot silently influence the sample.
Harmless source-protection metadata and an unused local material are not rejection grounds for this read-only operation.

The temporary evaluated mesh is released in `finally`, and the original action binding, action slot, frame, and subframe are restored.
The operation verifies that all native actions and the bound source file remain unchanged.
No scene or source data are persisted by the sampler.

## Files and validation

- `.tools/3d_pipeline/adapter/blender_worker.py`: strict region validation, dependency guards, native action identity, evaluated indexed records, measured centroids, restoration, and read-only receipt fields.
- `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py`: optional structured argument and forwarding on the existing tool.
- `.tools/3d_pipeline/blender_client.py`: optional structured forwarding on the existing client method.
- `.tools/3d_pipeline/tests/test_mesh_region_inspection.py`: fast path/schema/hash/topology/dependency/forwarding contracts.
- `.tools/3d_pipeline/tests/blender_mesh_region_integration.py`: disposable native deformation and rejection fixture, never a production input.
- This handoff.

Fast validation command: `python -B -m unittest discover -s .tools/3d_pipeline/tests -p test_mesh_region_inspection.py -q`.
The final 14-test focused suite passed in 1.439 seconds, including the dependency-guard additions.
The existing promotion suite passed 29 tests in 5.481 seconds, and the existing locator contract suite passed 32 tests in 4.973 seconds.
Those fast checks do not constitute native geometry acceptance.

The native fixture ran after version/config/locked-source verification using `C:/Program Files/Blender Foundation/Blender 5.1/blender.exe --background --factory-startup --python-exit-code 1 --python .tools/3d_pipeline/tests/blender_mesh_region_integration.py`.
It creates a disposable four-vertex synthetic rigged fixture, a real native action, non-axis-aligned bone, positive nonuniform mesh/rig scales, UVs, material assignments, protection metadata, and an unused material.
It obtains the native action hash through the original inspector, verifies a known single-bone-deformed vertex and inverse-transpose corner normals, round-trips world/bone-local positions, checks source UVs/material/weights, measures centroids outside the paged subset, and tests a narrow bone-local AABB.
Rejections cover path escape, nonfinite selector, unmatched measurement indices, zero axis, negative/singular transforms, wrong action hash, external animated parent, and a topology-changing modifier.
The fixture verifies the original file hash and action/frame restoration, including a measurement failure path.
No production geometry, provider, or exported model is consumed by this fixture.

The locked-source candidate hashes are worker `7BEF3DA1EB6B0E17321AC6B087D8FE805742E9CEB91EA0D402FE714CF9BE08B7`, MCP adapter `2AA8598061CB59704BFBFBADD4F9691D86A644FBC0E7792CAF50FF384D3F32E6`, and client `D316E3B4EF2D6C2BCB2ACC06B43333747177FEE7170BCB65357578EDDC5F2C11`.
All three locked-source candidates are LF-only.
The fast test hash is `798DCC1A3085DDA22D43285605C23963CA0F2C97B85C150A8356BEC102378054` and the native fixture hash is `8383513E9353201148E149D09C213A754D785C7037FF3358548B2874F24EE9AC`.
### Native result

`python -B .tools/3d_pipeline/verify_environment.py` returned exit code zero and `findings: []`, without `--probe-meshy`.
Its normal generated artifact is `.tools/3d_pipeline/reports/environment_report.json`.
The parent-owned version/config gate was `1.10.18`, with config SHA-256 `A38A124144AAF48CCBE7F66EF12BDAF4CACA38C4A787318A3AD71512FCA94A15` and lock SHA-256 `A7410AE07A80872F52C5833DB593DB975207497059E2B89EF3851961631CDFD5` at authorization.

The native command returned exit code zero in 9.4836 seconds under Blender `5.1.2`, build `ec6e62d40fa9`.
Its structured result was `status: pass`, `fixture_only: true`, and `production_asset_acceptance: false`.
No source correction or lock relaxation was needed after the native run.

| Native assertion | Measured error |
| --- | --- |
| Known single-bone-deformed vertex | `1.8431718463976653e-7` |
| Bone-local/world position round trip | `2.457562461863554e-7` |
| Maximum inverse-transpose world corner-normal error | `1.999200562387517e-7` |
| Maximum bone-local corner-normal error | `1.698202297324333e-7` |
| Endpoint centroid using two vertices outside the page | `1.228781230931777e-7` |
| Measured centroid axis | `7.939763920734493e-8` |

The fixture's assertion threshold was `2e-5`; this is a synthetic numeric test threshold, not a relaxed production fingerprint comparison.
The page contained source vertex index one and all three of its corners, reported four complete selector matches, and returned `next_offset: 2` with `truncated: true`.
The measured endpoint set remained exactly `[2, 3]`, despite both endpoint vertices being outside the page.
The narrow bone-local AABB selected exactly the previously observed vertex.
All nine explicit rejection cases passed: path escape, nonfinite selector, unmatched measurement vertex, zero axis, negative transform, singular transform, wrong native action hash, external animated parent, and topology-changing modifier.
The fixture also asserted exact source UVs, evaluated UVs, material name/index, weight membership, source-protection metadata, echoed receipt metadata, full action integrity, restored frame/action binding, and unchanged source bytes.

The disposable source hash for this run was `006D123A2BBC143451F9BDDD0BB5E200C4ACD16E30A2348FC7ACC8768FA2EF19` and its native action hash was `09824A39B6A985DF72B6ED3665C8DE3671366BC82BA46CBC844C6A8B8101C31E`.
Those identities belong only to the temporary synthetic fixture, which was removed by its normal temporary-directory cleanup.
They are not Alien asset hashes or production coordinates.

## Remaining production gate

The accepted working checkpoint and its approved source hash remain the only eligible production input; earlier failed paths and rejected manually guessed coordinates remain ineligible.
The parent/model worker must obtain the native action identity, visually select a bounded region on the preserved fused firearm, inspect the measured vertex/corner records at the agreed action frames, and approve the exact endpoint/axis evidence before a separate locator operation.
This capability does not resolve roll, merge the seven accepted actions, author replacement motion, change the fused weapon, or approve a final in-game muzzle result.
No simplification or material/geometry fallback is introduced; unsupported dependency configurations fail closed.
The `chaos-redux-3d-model-pipeline` skill governed preservation, source binding, the verified adapter boundary, and evidence separation throughout this tooling task.
