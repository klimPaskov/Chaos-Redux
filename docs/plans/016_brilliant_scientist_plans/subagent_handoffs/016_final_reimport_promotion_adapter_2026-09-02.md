# Guarded accepted-reimport working-copy adapter

Status: frozen after successful disposable native execution and focused regression tests.
The 22 isolated promotion contracts and 32 existing locator contracts pass.
Blender 5.1.2 completed the real synthetic mesh/animation round-trip, producer reimport receipt, metadata-only promotion, and independent reopening checks with exit code 0, `status=pass`, and `promotion_status=pass`.
The previously observed mathutils `Vector` and mesh-attribute `INT16_2D` fingerprint failures are resolved by this native pass, not merely by isolated tests.
No production model, Meshy/provider operation, runtime asset, runtime configuration, or gameplay file was changed or invoked.
Only the disposable tooling fixture used Blender and imported/exported synthetic action and mesh bytes.
The parent explicitly authorized this native recovery loop and exclusive refresh of the changed worker hash in the dependency lock.

## Scope and changed files

This implements the guarded working-copy design in `016_final_alien_muzzle_recovery_2026-09-02.md` without event-specific paths, identities, hashes, counts, or muzzle coordinates in production code.
The operation changes only declared metadata on exactly one accepted rig and one to sixteen explicitly named accepted meshes in a new sibling checkpoint.
It does not approve exports, promote other objects, import or merge actions, generate geometry, normalize transforms, change materials, or infer a weapon attachment.

| File | Change |
|---|---|
| `.tools/3d_pipeline/adapter/blender_worker.py` | Hashed receipt/input validation, exact target checks, deterministic preservation fingerprints, metadata-only copy/save/reopen, success/failure evidence, and non-exporter dispatch for `promote_accepted_reimport`. |
| `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py` | Exact `chaosx_blender_hoi4_promote_accepted_reimport` tool declaration. |
| `.tools/3d_pipeline/blender_client.py` | Exact `BlenderAdapterClient.promote_accepted_reimport` forwarding wrapper. |
| `.tools/3d_pipeline/tests/test_reimport_promotion_contract.py` | Twenty-two isolated, non-Blender validation, forwarding, preservation-fingerprint, sequence/attribute serialization, and control-flow tests. |
| `.tools/3d_pipeline/tests/blender_locator_adapter_integration.py` | Gate deliberately advances to parent-selected `1.10.16`, requires the promotion operation, extends the disposable actual-byte locator regression with a real reimport receipt followed by promotion and independent copy reopening, and exposes a schema-only RNA diagnostic mode. |
| `.tools/3d_pipeline/config/dependencies.lock.json` | Only the changed worker's `source_sha256` entry was refreshed during this authorized recovery loop. |
| This handoff | Contract, source evidence, tested cases, fingerprints, compatibility limits, and completed native evidence. |

The existing dirty/staged source state was preserved.
No staging, commit, reset, checkout, runtime configuration, operation allowlist configuration, `.gitattributes`, install/bootstrap script, existing handoff, or asset file was edited.
The parent owns the operation allowlist, Codex visibility, adapter version, and other lock entries.
The existing verifier regenerated `.tools/3d_pipeline/reports/environment_report.json`; that report is generated verification evidence, not a manual source edit.

## Exact operation schema

Operation: `promote_accepted_reimport`.
MCP tool: `chaosx_blender_hoi4_promote_accepted_reimport`.
All arguments are required; there is no arbitrary code, URL, shell, import, conversion, action-remapping, or metadata-dictionary argument.

| Argument | Type and meaning |
|---|---|
| `job_id` | String; configured job identifier, lowercase snake_case for this operation. |
| `blend_rel` | Existing same-job `.blend` proof checkpoint. |
| `expected_source_sha256` | Explicit 64-hex SHA-256 of that immutable proof. |
| `validation_rel` | Existing same-job `.json` reimport receipt. |
| `expected_validation_sha256` | Explicit SHA-256 of the immutable receipt bytes. |
| `checkpoint_rel` | New, nonexisting `.blend` in the same directory as `blend_rel`. |
| `target_armature_name` | Exact single existing local scene armature name. |
| `target_mesh_names` | List of one to sixteen exact, unique existing local scene mesh names. |
| `mesh_rel` | Exact same-job `.mesh` named by the receipt. |
| `expected_mesh_sha256` | Explicit SHA-256 of that immutable mesh. |
| `anim_rel` | Exact same-job `.anim` named by the receipt. |
| `expected_anim_sha256` | Explicit SHA-256 of that immutable animation. |

Paths must be job-relative, use forward slashes, have the required suffix, and contain no traversal or external path.
All four input hashes and nonempty files are checked before opening Blender data.
The new checkpoint and derived `blender/reports/promote_<checkpoint-stem>.json` must both be absent.
Existing checkpoints and reports are never overwritten.
The operation opens both source and output using `use_scripts=False` and saves with `copy=True, relative_remap=False`.
It does not call the existing `save_blend` helper, which would change all action fake-user flags.

## Legacy receipt evidence and binding

The accepted receipt was read directly at `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/validation/reimport_v13_firearm_preset_laser_attack_final.json`.
It contains `proof_blend`, `mesh`, `anim`, `objects`, `meshes`, `armatures`, `actions`, `geometry`, `animation_bounds`, `previews`, and `runtime_texture_staging`.
It does not contain a `status` field or source/mesh/animation hashes.
The current `reimport_export` producer was inspected directly: it imports actual files, samples and previews them, saves the proof, constructs those fields, writes the receipt, and returns it.

The parent approved explicit mesh and animation paths/hashes as additional arguments because the historical receipt cannot supply them.
The operation does not invent, insert, or rewrite legacy status or hashes.
It requires the complete successful producer shape, rejects explicit non-`pass` status or error fields, rejects duplicate JSON keys and NaN/Infinity, binds all three recorded file paths to the explicitly hashed input files, and rejects conflicting embedded hashes if newer receipts contain them.
It verifies unique exact object/mesh/rig/action identities, positive receipt counts, material-slot names, numeric animated bounds, and populated producer preview evidence.
Preview paths are retained as producer evidence, not re-rendered or independently visually accepted by this operation.

The accepted receipt's mesh/action/proof hashes remain caller-supplied authority tied to the separately hash-verified receipt.
This is not a signature or an independent reconstruction of historical provenance.
It cannot infer whether an arbitrary unreviewed receipt is genuinely accepted; the caller/parent must supply the reviewed hashes.

## Target guards and preservation

The receipt must name exactly the requested armature and mesh set, and the current scene inventory must match the receipt.
The armature bone count, material-slot identities, polygon count, and complete existing action-name set must match.
Each target mesh must have exactly one modifier, an armature modifier consuming the exact accepted rig, and local PDX node-based material bindings.
Object lookups and parent/modifier references use RNA equality, not Python wrapper identity.
Linked, overridden, source-protected, reference-protected, ambiguous, already-working, or conflicting-promotion targets are rejected.
Protection checks include target objects, their data, and owning collections.
Transforms must be finite, positive, nonsingular, and unreflected; promotion does not rescale them.

The current Blender vertex count is measured, reported, and compared unchanged before and after.
It is intentionally not forced to equal the historical exported-stream vertex count.
The regression uses receipt count 27 and current count 3 to ensure this distinction remains deliberate.

The only permitted object properties are:

- `chaosx_working = true`
- `chaosx_promotion_operation = promote_accepted_reimport`
- `chaosx_promotion_source`
- `chaosx_promotion_source_sha256`
- `chaosx_promotion_validation`
- `chaosx_promotion_validation_sha256`
- `chaosx_promotion_job`

Only the exact named rig/meshes receive those fields.
Any other custom properties, including action source provenance, participate in the preservation fingerprints.
The report identifies the target names, previous values or absence, and exact permitted new values.

Fingerprint sections cover:

- Object identities, data and parent references, parent bone/type, matrices, bounds, dimensions, scalar RNA settings, modifiers, animation settings, and custom properties.
- Mesh positions, vertex/corner/polygon normals, custom-normal state, edge indices/seam/sharp flags, polygon indices/material assignments/smoothing, loops, all supported mesh attributes, UV values/settings/active layer, vertex-group names, weights, materials, and mesh custom/settings data.
- Armature rest bone identities, parents, head/tail/rest matrices, settings/custom properties, and current pose/basis matrices and settings.
- Material settings, custom properties, node identities/settings/default socket values, links, image references, color spaces, alpha mode, dimensions, packed bytes or same-job file hashes, and image custom properties.
- Every action name, frame range, fake-user state, custom provenance, scalar settings, F-curve paths/indices/settings, every key and both handles, interpolation/handle settings, sampled points, action slots, and layer/strip/channelbag mapping.
- Scene FPS and FPS base, current frame/subframe, playback range, custom properties, and collection object/child membership/custom properties.

The comparison is exact deterministic JSON-derived SHA-256, not a tolerance-based geometric comparison.
The same fingerprints are computed before metadata assignment, after assignment before save, and after reopening the copied checkpoint.
All sections and measured counts must be identical.
The permitted metadata is separately verified after reopening.
All four immutable input byte lengths and hashes are rechecked before success.

## Reports and failure behavior

A successful report returns `status=pass`, `new_provider_call=false`, input paths/hashes/sizes, output path/hash/size, exact target metadata, before/after fingerprints, measured mesh counts, existing actions, and source/all-input immutability.
This status means only that the guarded working-copy derivation passed.
It is not mesh export approval, role-motion acceptance, or in-game acceptance.

Invalid payloads, missing paths, receipt/hash mismatches, or preexisting destinations fail before a report path is trusted or Blender is opened.
Failures after accepted preflight write `status=fail`, the exception, fingerprints available so far, input immutability checks, and any output hash/size, then raise a hard error.
A failed saved copy is retained as evidence but has `output_approved=false`; it must never be used as an approved working source.
Neither a failed copy nor its report is overwritten automatically on retry.

## Tests performed

Executed without Blender, exporters, providers, or fresh runtime processes:

```powershell
python -B -m unittest discover -s .tools/3d_pipeline/tests -p test_reimport_promotion_contract.py -v
python -B -m unittest discover -s .tools/3d_pipeline/tests -p test_locator_adapter_contract.py -v
```

Latest results after the native attribute correction: promotion 22/22 passed in 3.840 seconds; locator 32/32 passed in 5.299 seconds.
The new tests cover exact MCP/client forwarding, immutable legacy receipt handling, all four hashes, path escapes/traversal/absolute paths, sibling/output/report collisions, bounded unique names, malformed/duplicate/nonfinite/failing receipts, recorded path/hash conflicts, current-versus-exported vertex counts, exact rig binding and material/action/topology identity, protected/linked/duplicate/already-working targets, metadata-only copy-save/reopen control flow, each fingerprint-section drift, changed immutable inputs, and dispatch without loading the exporter.
The real fingerprint function is exercised directly for unretained-action rejection and changes to action handles, interpolation, provenance, and FPS.
Two additional tests cover sequence-protocol values without a `__iter__` attribute, nested matrix rows, exact numeric precision, the RNA-scalar call path, and continued rejection of nonfinite/unsupported nested values without a `repr` fallback.
Two attribute tests hash both signed components at the 16-bit and 32-bit bounds, detect either component changing, preserve text and raw-byte sequence values without lossy decoding, and reject unknown attribute kinds.
Large geometry/material/rig field coverage is source-contract evidence and the save/reopen control-flow tests use explicit test doubles; these are not native Blender acceptance.

The extended native fixture was executed successfully after source hash verification.
It retains the rotated/posed/scaled locator actual-byte round-trip test and then clears the disposable scene, calls the actual `reimport_export` producer on the synthetic `.mesh`/`.anim`, obtains its real receipt and preview evidence, hashes the four files, and calls the promotion operation on that proof.
It requires matching pre/post fingerprints, reopens the derived working copy independently, verifies only named rig/meshes received working flags, verifies the locator did not receive working metadata, rechecks all immutable hashes, and reopens the original proof to prove its flags remain unmodified.
The fixture gate now requires version `1.10.16`, both operation registrations, current raw-byte source hashes, and the same verified Blender/io_pdx_mesh stack.

### Native failures, exact RNA correction, and successful verification

The parent reports that config and lock were synchronized to `1.10.16`, the operation and exact Codex tool were registered, and environment verification returned `findings=[]` before the native test.
The native test completed the synthetic actual `.mesh`/`.anim` round-trip and the real reimport producer's preview stage, then failed in the fixture's pre-promotion fingerprint.
The exact reported trace was `_promotion_fingerprint` line 3766 → `_promotion_scalars` line 3599 → `_promotion_value` line 3585: `ValueError: Unsupported promotion fingerprint value: Vector`.
No promotion pass was reached or claimed.

The previous serializer tested only for `__iter__`, but Blender 5.1 mathutils values can expose length/index access without that attribute.
The narrow correction recognizes explicit sequence protocol (`__len__` and `__getitem__`), indexes every element, and recursively applies the existing finite-value and ID/property rules.
It does not round values, stringify unsupported objects, use `repr`, modify geometry, or bypass a preservation comparison.
The parent's next run passed that value serialization but failed at `_promotion_fingerprint` line 3782 with `ValueError: Unsupported promotion mesh attribute: INT16_2D` before promotion.
Blender 5.1.2 had created that attribute in the actual synthetic producer proof.
This failure prompted inspection of the installed Blender RNA, not a skipped attribute or a weaker fingerprint.

The native fixture's `-- --schema-only` mode inspected these exact writable fields and completed with exit code 0:

| Blender RNA value type | Field | Property type and extent |
|---|---|---|
| `Short2AttributeValue` | `value` | `INT`, array length 2 |
| `Int2AttributeValue` | `value` | `INT`, array length 2 |
| `StringAttributeValue` | `value` | `STRING`, scalar |
| `Float2AttributeValue` | `vector` | `FLOAT`, array length 2 |
| `Float4x4AttributeValue` | `value` | `FLOAT`, array length 16 |
| `QuaternionAttributeValue` | `value` | `FLOAT`, array length 4 |

The installed `Short2AttributeValue` documentation confirms two signed integer components with range -32768 through 32767.
The explicit field map adds `INT16_2D`, `INT32_2D`, and `STRING` through their observed `value` fields and preserves existing exact vector/color/scalar mappings.
Every ordered element and component is recursively serialized and hashed along with attribute domain/type; unsupported types still fail closed.
There is no type-name stringification, precision reduction, component omission, attribute skipping, or geometry modification.

With the parent's exclusive lock-entry permission, the worker source hash was refreshed to `883B50EE15CB8460F3B8350AC716D8DAE15933A1391D4F1628718682BCFF5F7F`.
`python -B .tools/3d_pipeline/verify_environment.py` then exited 0 with `findings=[]` at `2026-09-02T13:08:15Z`.
The verifier did not use `--probe-meshy`; its current `meshy.route` was `not_probed`.

Executed native command:

```powershell
& 'C:/Program Files/Blender Foundation/Blender 5.1/blender.exe' --background --factory-startup --python-exit-code 1 --python .tools/3d_pipeline/tests/blender_locator_adapter_integration.py
```

The native process exited 0 and emitted structured `status=pass`, `promotion_status=pass`, `fixture_only=true`, and `production_asset_acceptance=false` on Blender 5.1.2 with io_pdx_mesh 0.91.0 and adapter 1.10.16.
The command completed in approximately 7.96 seconds.
It reported `author_invariants_preserved=true`, `root_own_ignore_flag_included=true`, `parent_bone=fixture_weapon_bone`, and the exact export selection `[FixtureBody, fixture_muzzle]` without the unregistered decoy.
Actual-byte reimport world-transform maximum errors were `3.725290298461914e-07`, `5.960464477539062e-07`, and `2.682209014892578e-07` at frames 1, 6, and 12 respectively, below the fixture's `2e-4` tolerance.
Promotion preserved the measured reimport topology of 12 vertices, 4 polygons, and 12 loops, retained `io_pdx_rigAction`, and compared all seven fingerprint sections exactly before assignment, before save, after reopening, and in the fixture's independent reopened comparison.
The original proof and all four hashed input files remained immutable, and the original proof's rig/meshes remained unmarked as working.
The temporary fixture was deleted at completion; no production checkpoint was used.

Successful-run preservation fingerprint hashes:

| Section | SHA-256 |
|---|---|
| Actions | `CBCF792052D6734D2279CFFB9946ADDECCD7EEB7F876208555C70E97A04B670A` |
| Geometry | `F987B70E3AC9160BD7EE270A26C0BAEBB3CBE73C4D79EFDEB438847B7FA7D44F` |
| Images | `44CF72777FF873DB7D38E551FA53234E04CB0DD8C5EC0580B12DF1FF8889F16B` |
| Materials | `E911FCE1D68F0D379408BE9F452900F634CCA7C82D823283B22BD012B0926BB9` |
| Objects | `75190C16E8826687BDEDE443D96D5AB83CB5FB8B4ADBEA5132B29717D8DDC4AF` |
| Rigs | `97B61C0624A76881EF1BFE898D79D389153BEDB0178E2381698CF8ABAE18D867` |
| Scene | `C9D9070849C92D8E43F6A4329A05196976B9C2184B1695AA7776349FCF5CDDD2` |

The run's disposable actual `.mesh` hash was `8F149DD0C60978FE20951422C723CC2CA69191CA080BB8CC0C712D74DEBC2F15`, its `.anim` hash was `0E752DAC920B0A85F7A560EEA808590A5E89B139913347D3CA5F33563154E637`, its promotion-source proof hash was `1A6E3270C56D6DF3C8CCA8DACC2D4FAE6E69DA5BEE4F529CC10018C092BF2F40`, and its producer receipt hash was `240418A63A4F4201299F6A03DDFF01DAC00987044167FAEA4F357F4344878581`.
The derived working copy hash was `1AE28F75EA4DFD29FB0D5CDF6FEB697B2C51DF627AA753899F15EB9FFB917195`.
These are captured test-run receipts for deleted temporary data, not reusable production authority.

## Frozen source hashes

Raw bytes and LF-normalized bytes match for all six files below; none contains CR at freeze.
Paths are relative to `.tools/3d_pipeline/`.

| File | SHA-256 |
|---|---|
| `adapter/blender_worker.py` | `883B50EE15CB8460F3B8350AC716D8DAE15933A1391D4F1628718682BCFF5F7F` |
| `adapter/chaosx_blender_hoi4_mcp.py` | `BF0FDAB9EFF479CCFA45181A4CF2EA46A0C870C615E91CDBA2071F21153B0403` |
| `blender_client.py` | `0835A34501866C7992698A9878B379D7A296FE4A38C80BDC89286C7437AB7D1C` |
| `tests/test_reimport_promotion_contract.py` | `C6040705B2451F1A4D25CA969226CE79A591BA5FF6CA37F23F220A30ABDF14BA` |
| `tests/blender_locator_adapter_integration.py` | `F23166E02859ACF0B7360A2EF5103ED6216AEA5CC3801B45E0F2A7AE077588CA` |
| `config/dependencies.lock.json` | `15FF9B87DCB37B300C8596B1CE6704C488F181F8FDC7B13F82C8094FAB0763A6` |

The parent has already synchronized config/lock version `1.10.16`, registered `promote_accepted_reimport`, and enabled the exact Codex tool.
The corrected worker hash is synchronized, the environment verifier accepted those exact bytes, and the disposable native fixture passed.
This subagent did not update version, operation configuration, runtime visibility, or any other lock entry during the native recovery loop.
The locked `normalization_convergence.py` LF hash is unchanged and must not be replaced by a CRLF hash.

## Simplifications, compatibility limits, and remaining gates

No simplifications were made within this bounded metadata-only adapter capability, and no geometry, action, source, or runtime fallback was introduced.
Promotion remains deliberately limited to animated `reimport_export` proof scenes with one rig and one to sixteen named mesh consumers.
It rejects shape keys, extra/non-armature modifiers on target meshes, object or pose constraints, driver/NLA animation, modified action curves, linked/overridden data, grouped material node trees, unsupported mesh-attribute types, non-node materials, and missing or external unpacked texture files.
Those features are not silently ignored, flattened, baked, or repaired.
This bounded support matches the inspected simple io_pdx_mesh proof structure but still requires native execution against the actual accepted checkpoint before production reliance.

The operation does not merge the seven accepted Alien actions into one proof, does not rename `io_pdx_rigAction`, does not certify firing roles, and does not change the non-firing defend stance.
After verified promotion, the parent still needs accepted gun-bone/muzzle measurement, locator authoring, export selection evidence, and all required actual-byte action reimports and contact/axis checks.
There is no in-game acceptance claim; that remains the user's responsibility.

Skills used: `chaos-redux-3d-model-pipeline`, with previously read required `chaos-redux-event-assets` and `chaos-redux-subagents` preservation/ownership guidance.
No skill was changed.
