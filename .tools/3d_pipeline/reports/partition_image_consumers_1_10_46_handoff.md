# Adapter 1.10.46 partition image-consumer handoff

Disposition: implemented under the parent's bounded partition-repair authorization.

## Behavior and ownership

Partition creates equivalent material clones on the approved meshes to bound skeletal export streams.
Those clones necessarily add native image users and material-node references.
The operation records each created clone's exact allocated identity, unchanged source-material hash, owned object, owned mesh, owned slot, material ID, and private embedded node-tree ID.
It verifies clone/source material equivalence and rejects outside slot consumers, outside ID consumers, unproven or externally consumed clone trees, changed source materials, and retention changes.
Image reconciliation permits exactly the added users and node/ID bindings implied by those verified clones.
Every image content hash, packed hash, file path/hash, independent retention flag, and original image consumer remains exact.
Before/after native rows and the accounted clone additions are retained in the receipt.

The projection exists only in `skeletal_export_partition._fingerprint` and requires the operation's creation evidence and original image inventory.
The default promotion comparator and worker fingerprint implementation are unchanged from 1.10.45.
The existing normal-angle guards are unchanged.

## Changed files

- `.tools/3d_pipeline/adapter/skeletal_export_partition.py`: transaction-owned clone validation, image-user reconciliation, deterministic collision-free clone names, and receipts before save and after reopen.
- `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py`: partition contract description only.
- `.tools/3d_pipeline/config/blender_hoi4_adapter.json`: version 1.10.46.
- `.tools/3d_pipeline/config/dependencies.lock.json`: matching version and changed source hashes.
- `.tools/3d_pipeline/tests/test_partition_image_consumers.py`: nine focused positive/negative tests.
- `.tools/3d_pipeline/tests/test_skeletal_export_streams.py`: missing transaction ownership must reject.
- `.tools/3d_pipeline/tests/blender_partition_image_consumers_integration.py`: disposable native save/reopen and negative mutation cases.
- `.tools/3d_pipeline/tests/blender_partition_production_preflight.py`: explicit production source inspection stopped before save, with reports redirected into adapter-owned evidence.
- `.tools/3d_pipeline/reports/partition_image_consumers_1_10_46.json`: final locked native fixture receipt.
- `.tools/3d_pipeline/reports/stone_partition_preflight_1_10_46.json`: Stone Cohorts production preflight receipt.
- `.tools/3d_pipeline/reports/environment_report.json`: verifier result with no findings.
- This handoff.

Concurrent and earlier parent edits were preserved.
No model checkpoint, runtime asset, or provider route was changed, and no provider call was made.
No commit was created because the shared adapter publication depends on the parent's earlier uncommitted changes; the parent owns that combined reviewed commit.

## Verification

All 93 focused tests passed: nine partition-consumer tests, eleven skeletal-stream/partition guards, twelve orphan-image tests, twenty-nine promotion tests, thirteen phase-patch tests, and nineteen release/import-closure checks.
The final locked Blender 5.1.2 fixture partitions one existing material into four streams, accounting for exactly three added image users, and survives save/reopen with exact normalized fingerprints.
Native negative scenarios reject changed image content, changed clone material content, an unplanned material image consumer, and a clone consumed by an outside mesh.
Unit negatives also cover source material changes, missing/extra transaction ownership, wrong owned object/mesh/slot, fake/extra/protected/library changes, lost original consumers, added/lost image IDs, changed packed/file hashes, and unproven/private-tree consumers.
The unchanged shared promotion comparator explicitly rejects those same clone additions outside partition reconciliation.

Stone Cohorts source `66_forearm_chip_solid_finalize_20260912.blend`, SHA-256 `FC0BD069B529C9EB597821EB5B52A6231A107B8ED57434D7F9DF6AA9F3C4C2D5`, passed the complete production pre-save partition invariants.
The preflight created only in-memory `stone_body_pdx_resume_20260908_skeletal_batch_02` and `_03` material clones and accounted for users 1 to 3 on each diffuse, normal, and specular image.
It stopped at the save boundary; the source remained byte-identical and no production checkpoint was written.
The preflight's partition-source checksum matches the released module.
The native final fixture is the save/reopen evidence; the production preflight does not claim a saved or approved model output.

The environment verifier returned `findings: []`.
All seventeen source locks, operation-array agreement, complete local import closure, and raw/Git-clean canonical source bytes passed release checks.

## Release checksums

Version: `1.10.46`.
Partition module SHA-256: `747BBE923740A4A3024F8A44F487C82B1FD40F855BFE742E20E5859E3FCD8406`.
MCP declaration SHA-256: `FB777AC439EABF8D1A083594B90A0326F54F516C3C454D2EF19654C096D17363`.
Worker SHA-256, unchanged: `690EAF9B3C33C37F8EEFB7CA5B737EFD47DE7FA24677F03CF494196927CF84A0`.
Dependency-lock SHA-256: `6FD328418721446D379C9F396EA479DB92CAC1FF57606B6485163ACADB967AE8`.

## Separate corner-normal request

The parent permitted finishing partition first if the additional selected-corner normal operation could not be proved cleanly during this release.
That operation is not included in 1.10.46.
The existing winding and mesh-patch helpers call `normals_split_custom_set` over the complete corner array, and the winding retention projection deliberately omits raw `custom_normal` and decoded loop-normal records.
Those helpers therefore cannot supply the newly requested exact preservation proof for every unselected corner.
A separate operation needs an explicit selected-corner/direction contract, unchanged raw-normal evidence for untouched corners, and native save/reopen tests on the open-fragment case before publication.
The reported 0.5442289-degree Parasitic Zombie corner failure remains unresolved; the 0.5-degree global ceiling was not relaxed.

No simplifications were made to the partition repair.
The separate corner-normal operation remains unimplemented for the reason above.
Skill used: `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`.
