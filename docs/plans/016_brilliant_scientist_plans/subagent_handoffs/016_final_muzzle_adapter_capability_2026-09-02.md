# Event 016 bounded muzzle-locator adapter capability

Status: narrow RNA-equality correction frozen for parent relock and native rerun; 32 isolated contracts passed.
The parent's first native fixture run passed author/save/reopen preservation and posed locator-follow checks, then failed before mesh export on the first-root RNA identity check; no native end-to-end or production acceptance is claimed.

This change provides adapter engineering for the accepted no-regeneration recovery.
It does not produce, alter, export, or wire an Alien asset.
The accepted V13 mesh and seven provider actions remain the authority recorded in `016_final_alien_muzzle_recovery_2026-09-02.md`, including the non-firing `defend` stance.
The rejected manual-recovery checkpoint, its unnamed parent bone, and its muzzle coordinates are not used.

## Owned files changed

| File | Change |
|---|---|
| `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py` | Adds the bounded MCP declaration `chaosx_blender_hoi4_author_locator`. |
| `.tools/3d_pipeline/adapter/blender_worker.py` | Adds locator request/ownership/parent/transform validation, one-Empty authoring, approved locator export selection and coordinate handling, and inspect/reimport locator evidence. |
| `.tools/3d_pipeline/config/blender_hoi4_adapter.json` | Adds only `author_locator` to the operation allowlist. |
| `.tools/3d_pipeline/tests/test_locator_adapter_contract.py` | Adds 32 isolated validation, control-flow, RNA-wrapper equality, exact client-forwarding, and Codex tool-visibility tests without starting Blender or a provider. |
| `.tools/3d_pipeline/tests/blender_locator_adapter_integration.py` | Adds a disposable synthetic-fixture native Blender test with a raw-byte lock gate and actual mesh/action export/reimport assertions; the parent's first run failed before export and awaits rerun. |
| This handoff | Records the contract, source evidence, tests, and remaining gates. |

No runtime configuration, dependency/schema lock, installation/bootstrap script, `.gitattributes`, client wrapper, model, texture, action, GFX, entity, sound, counter, gameplay, or spreadsheet file was edited by this subagent.
No commit or staging was performed.
Other working-tree changes, including the parent's LF attributes, were preserved.

## Authoring contract

Operation: `author_locator`.
MCP tool: `chaosx_blender_hoi4_author_locator`.

| Required argument | Meaning |
|---|---|
| `job_id` | Existing configured job; lowercase snake_case for this operation. |
| `blend_rel` | Existing job-relative `.blend` checkpoint. |
| `checkpoint_rel` | New, non-existing sibling `.blend` checkpoint in the same directory as the input. |
| `target_armature_name` | Exact existing scene armature name; no fuzzy selection or promotion. |
| `parent_bone` | Exact existing data/pose bone name in that armature. |
| `locator_name` | Stable lowercase snake_case, 1–63 ASCII characters. |
| `bone_local_position` | Exactly three finite numeric coordinates measured in the checkpoint's Blender bone-head-local units. |
| `bone_local_rotation_xyzw` | Exactly four finite numbers forming a unit quaternion in x/y/z/w order, in Blender axes. |

The operation accepts no additional payload fields, arbitrary Python, shell, URL, or external write path.
It rejects absolute, traversal, wrong-extension, missing-input, input/output-equal, existing-output, and non-sibling output paths.
Sibling output is deliberate: `copy=True, relative_remap=False` preserves the source's relative material/image paths and does not repoint the open source file.
Opening the checkpoint passes `use_scripts=False`.

It creates only one Empty with `data=None` or updates the exact existing registered Empty.
Its parent is the caller-named armature and existing bone; no bone, geometry, material, weight, action, rig scale, or weapon attachment is created or edited.
It never calls `save_blend`, because that helper sets every action's fake-user flag.
An input containing an action with no users and no fake user is rejected before locator mutation instead of silently losing the action on a subsequent save.
Existing action key/handle snapshots are compared before save, the source checkpoint SHA-256 is checked unchanged, and the saved checkpoint's byte count and SHA-256 are returned.
These checks do not replace post-save Blender reopening and source-data comparison.

Registration is stored on the Empty using `chaosx_export_locator`, `chaosx_locator_registry_version`, `chaosx_locator_owner_job`, `chaosx_locator_owner_root`, `chaosx_locator_name`, `chaosx_locator_armature`, and `chaosx_locator_parent_bone`.
The root owner is the hash of the resolved normalized job root, so a foreign job with the same slug does not inherit ownership.
The stable stored name and stored parent must match the actual object; automatic renaming, adoption of an unregistered Empty, and automatic reparenting are forbidden.
Linked, overridden, protected-source, protected-reference, wrong-type, non-leaf, animated, constrained, modified, or instancing collisions fail closed.
The Blender data-block user map also rejects a locator referenced by another object, modifier/constraint owner, node tree, material, or other non-scene/non-collection data-block, keeping it a non-deforming leaf rather than an input to the model.
Locator names colliding with skeleton bones are rejected.
Duplicate exact locator or armature names are rejected instead of allowing Blender to choose or suffix a collision.
Zero, reflected/negative, or nonuniform armature world scale is rejected because the existing export-coordinate conversion requires a positive uniform scale; a positive uniform scale other than one is supported without changing scale during authoring.

The supplied transform is composed at the bone head and assigned through world space after exact bone parenting.
This lets Blender account for its bone-tail parenting offset without mislabeling `Object.matrix_local` as bone-local.
The operation measures `(current bone world matrix)^-1 * locator world matrix` and fails if the requested local matrix differs by more than `1e-5`.
It does not normalize an invalid quaternion or infer a muzzle position or orientation.

## Export selection and coordinate behavior

`export_mesh` still calls the installed `io_pdx_mesh` exporter with `exp_mesh=True`, `exp_skel=True`, `exp_locs=True`, and `exp_selected=True`.
The worker loads the installed extension's `list_scene_pdx_meshes` helper to identify meshes that actually have PDX materials.
A locator is eligible only when its fully matching job registration belongs to an approved `chaosx_working` armature used by the first armature modifier of an approved PDX-material mesh selected for export.
That first-modifier relationship matches the installed exporter's `get_rig_from_mesh` behavior.

Unregistered Empty objects are not selected, and registered locators on other rigs are not selected.
Malformed or foreign registrations fail closed rather than being silently accepted.
The parent bone must be reachable from the exporter's first root and outside any `pdxIgnoreJoint`-excluded child branch; ambiguous parent names across exported rigs and locator/bone name collisions fail.
Installed version 0.91.0 unconditionally includes the first root itself even if that root has `pdxIgnoreJoint=True`; only children are filtered before recursion.
The adapter deliberately matches that source behavior, with both an isolated contract and an unrun native assertion; no root-flag rejection was added.
After deselection, the selected object names must equal exactly the approved working mesh names plus eligible registered locator names.
The report includes `selected_export_objects` and the exact locator records used at serialization.

The installed exporter derives a locator's local transform from the bone's rest matrix, not its current pose matrix.
For locator-bearing exports the adapter therefore evaluates only the approved locator rigs in `REST` for serialization and restores their prior pose-display state in `finally`, including exporter failure.
No action keys are authored by this step.
The existing export-coordinate normalization can bake a positive uniform armature scale into the rig data; registered bone-local locator offsets receive that same factor and are reapplied after conversion so they do not drift when the rig object scale is removed.
This coordinate-preservation branch is source-reviewed and covered by a scale-aware test double, but still requires execution of the written native Blender fixture with non-unit rig scale.

## Inspect and reimport evidence

Inspect object rows and reimport object rows include `parent`, `parent_type`, and `parent_bone`.
Both reports include a dedicated `locators` list with name, parent fields, frame, world matrix, basis matrix, parent-inverse matrix, current bone-head-local matrix, rest-bone-relative matrix, and registration/owner indicators.
Reimport animation-bound samples also include locator records for each sampled frame.
The existing `imp_locs=True` import path is retained.

The current bone-local matrix and the rest-relative matrix are intentionally separate because a posed locator can have different values under those reference frames.
`registered_for_export` is registration evidence only, not a runtime acceptance verdict.
The PDX format does not preserve the adapter's custom ownership properties, so reimported locators are reported but are not automatically adopted into the export registry.
Use the original authored working checkpoint for further edits/exports; treat actual-byte reimport checkpoints as proof scenes.
Attempting to update an unregistered reimported `muzzle` through `author_locator` will correctly reject the collision.

## Direct installed-source verification

Installed extension root: `C:/Users/klimp/AppData/Roaming/Blender Foundation/Blender/5.1/extensions/user_default/io_pdx_mesh`.
The installed `blender_manifest.toml` reports version `0.91.0`.
The existing lock records archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`; no archive was downloaded or replaced.
The directly read `pdx_blender/blender_import_export.py` has raw SHA-256 `FCBE2EDFC6C24A72450CB1F398C88EDCAA970556B1448224DCE4074A961A2799`.

Reviewed installed definitions:

- `get_rig_from_mesh` at line 106 selects the first armature modifier.
- `list_scene_pdx_meshes` at line 120 and `check_mesh_material` at line 163 require an owning PDX material.
- `get_mesh_skeleton_info` at line 438 and `get_skeleton_hierarchy` at line 524 export the first root hierarchy and skip excluded child branches, without testing the first root's own ignore flag.
- `get_locators_info` at line 476 emits `name`, position `p`, quaternion `q` in x/y/z/w order, optional transform `tx`, and bone parent `pa` from `obj.parent_bone`.
- Its local transform is `(rig.matrix_world * bone.matrix_local)^-1 * obj.matrix_world` before coordinate-space conversion.
- `create_locator` at line 754 reconstructs a `PLAIN_AXES` Empty with `parent`, `parent_bone`, and `parent_type='BONE'`, then restores the coordinate-converted transform.
- `export_meshfile` at line 1273 selects Empty objects by `data is None`, intersects them with `select_get()` when `exp_selected=True`, and writes them under the locator root.
- `import_meshfile` at line 1186 uses `imp_locs=True` to reconstruct locator records.

The offline core wiki pages and complete Graphical Asset/Entity Modding pages were consulted.
Installed vanilla `documentation/effects_documentation.md` entity/model material was consulted, and `gfx/entities/units_infantry.asset` supplied the exact node-bound effect and attachment precedent.
The bundled Blender API reference for `BlendData.user_map` and `wm.save_as_mainfile` was read directly.
The [Blender Object API](https://docs.blender.org/api/5.0/bpy.types.Object.html) confirms that `matrix_local` is relative to the armature object, not the actual parent bone.

## Tests and review

Executed from the mod root:

```powershell
python -B -m unittest discover -s .tools/3d_pipeline/tests -p test_locator_adapter_contract.py -v
```

Latest result: 32 tests passed in 5.123 seconds with the system Python 3.9 interpreter after the RNA-equality correction.
They exercise finite numeric and unit-quaternion validation, exact payload/name contracts, path containment and existing sibling-save collision preservation, exact rig/bone selection and duplicate-name rejection, zero/nonuniform/negative scale rejection, protected/foreign/renamed/wrong-type/wrong-parent/animated/non-leaf/reference collisions, orphan-action rejection, one-Empty create/update control flow, copied checkpoint save arguments, no extension load for authoring, registry-filtered export eligibility, first-root and excluded-child skeleton behavior, exact selected object names, one-time uniform-scale offset conversion, REST serialization state and restoration after failure, inspect/reimport `parent_bone`/locator report fields, exact AST-loaded client forwarding, and Codex enabled-tool visibility.
The added regression uses distinct Python wrappers with equality for the same underlying simulated RNA data, covering scene rig lookup, scene locator lookup, actual parent comparison, and first-root bone comparison; genuinely different rig/root data still fails even when names match.
The first run after adding the config assertion exposed that system Python 3.9 lacks `tomllib`; the fast test was corrected to inspect only the explicit enabled-tools section with the existing standard-library AST/regex strategy, then all 31 tests passed.
The fixtures are explicitly not `.blend` files and the diagonal-scale/translation matrix double is not Blender transform evidence.
The mocked exporter deliberately raises a test sentinel; no mock result is described as successful live export or actual-byte reimport.
The modified source was reviewed with `git diff --ignore-space-at-eol` to separate implementation changes from the parent's concurrent LF policy.

### Native fixture failure and narrow correction

This subagent syntax-parsed but did not execute `blender_locator_adapter_integration.py`.
After the initial freeze, the parent updated config/lock to `1.10.15`, normalized the reviewed sources to LF, reported environment verification `findings=[]`, and obtained a fresh MCP schema exposing the exact `author_locator` contract.
The parent then ran the native fixture with Blender 5.1.2.
According to the parent's captured failure, authoring, save/reopen invariant comparison, and source posed-frame follow checks passed, but `approved_export_locators` failed at worker line 3791 with `ValueError: Locator parent is outside the exporter's first-root skeleton.`
That failure was caused by using Python `is not` on two RNA Bone wrappers for the same underlying bone.
The worker correction replaces that comparison and the three corresponding new scene-object/parent comparisons with RNA `!=`, while preserving `is None` checks and exact registration/name constraints.
No naming-only identity fallback, hierarchy change, promotion, geometry/action edit, or broader export change was added.
The parent's process returned exit code zero despite the traceback and produced no `status=pass`; it was correctly treated as a failed fixture, not success.
The retry command below includes `--python-exit-code 1`, and successful process exit must still be accompanied by the fixture's structured `status=pass` result.
It asserts adapter/config/lock version `1.10.15`, exact operation-list equality, all locked adapter raw-byte source hashes, locked Blender version/build, io_pdx_mesh `0.91.0`, and the reviewed installed exporter SHA-256 before creating fixture data.
It does not refresh locks or install anything.

The fixture creates a temporary tetrahedron, PDX material and 2x2 test texture, two-bone rig with a non-axis-aligned/rolled weapon bone, a retained synthetic test action sampled at frames 1/6/12, an unregistered decoy Empty, and uniform rig scale 1.75.
It requests a nonidentity measured quaternion and nonzero bone-local offset while the rig is posed at frame 6.
It saves and reopens the authored checkpoint, compares mesh topology/UVs/weights/modifiers, materials/images, rig/bone/pose transforms, action keys/handles/fake-user state, frame, scale, and decoy invariants, and verifies parent/local/world evidence and pose follow.
It then calls the installed exporter through the adapter, checks exact selection and REST restoration, reopens the normalized export checkpoint, exports the retained synthetic action, inspects the actual binary locator parent record, clears the disposable scene, and imports the actual `.mesh` and `.anim` bytes.
The final assertions verify bone-local transform preservation, parent identity, material shader, decoy exclusion, registry metadata non-adoption, and world-space pose follow against the exported checkpoint across all three frames.
Authoring tolerance is `1e-5`; actual-byte round-trip tolerance is `2e-4` for float serialization.
It prints structured test-only evidence and file hashes, then removes its temporary fixture.
This synthetic geometry/action is strictly tooling regression data, not a model candidate, replacement action, or production asset.

Parent-only invocation after review and successful lock verification:

```powershell
& 'C:/Program Files/Blender Foundation/Blender 5.1/blender.exe' --background --factory-startup --python-exit-code 1 --python .tools/3d_pipeline/tests/blender_locator_adapter_integration.py
```

No native pass result is claimed; assertion failures must be reviewed before any production use.

## Lock/version handoff and LF handling

The parent has synchronized adapter configuration and dependency lock to `1.10.15` and registered the operation; this subagent did not revise the version or lock.
The corrected worker checksum intentionally differs from the previously verified lock until the parent reviews and relocks this narrow change.
Do not invoke the production route before that gate passes.

The parent normalized the reviewed files to LF before the first native run.
The corrected worker and updated focused test remain LF, and their raw-byte and LF-normalized SHA-256 values match at this freeze.
Preserve LF when producing new raw-byte lock digests and staging.
Do not change the locked `normalization_convergence.py` hash to the CRLF digest: its LF-normalized bytes must remain `91AC1D4BA9BE4D39AB4697F9044060A9F119A8998E1DADA8F4A8E6F58A5F9ED5`.
No checksum normalizer, Git attributes, lock file, or installation script was edited here.

Current LF-normalized review hashes after the parent version bump and narrow RNA correction:

| File | SHA-256 of LF-normalized UTF-8 bytes |
|---|---|
| `adapter/chaosx_blender_hoi4_mcp.py` | `65A652028A7F9FE934C7D3AA06BA5976267BFAE2E43A531A1EDD44A33811E16D` |
| `adapter/blender_worker.py` | `F5F6F335C1A62EA5B5C4E2A6CA57EED414258A0E561A216742792A4FB6FFF6BF` |
| `config/blender_hoi4_adapter.json` | `B3DB95EED28B98557319831823CAD563A6F078C06CD3DA2E59D4E64A14D17CD9` |
| `tests/test_locator_adapter_contract.py` | `BEB838CBC008083E6E4FE4C17B16B91D475993B292C2A386D28F04B44DEB19DB` |
| `tests/blender_locator_adapter_integration.py` | `EC029201079057E209D666A8F50DA45E99CD0EB20F4E25792D3A42E7FF3CAB04` |

All five paths in this table are relative to `.tools/3d_pipeline/`.
The parent must recompute after any edits; these are review fingerprints, not an automatic lock refresh instruction.

Parent-owned remaining integration steps:

1. Review the four RNA-equality corrections and new focused regression, then refresh the worker's `1.10.15` source hash through the approved repository-owned lock workflow.
2. Preserve the already synchronized operation lists, versions, unchanged reviewed sources, and LF policy; do not substitute a CRLF digest.
3. Review the parent's added `BlenderAdapterClient.author_locator` forwarding wrapper and Codex enabled-tools registration, both covered by the fast contracts; no Codex/Qoder/Cursor runtime config or client wrapper was changed by this subagent.
4. Rerun `.tools/3d_pipeline/verify_environment.py` after relock; the parent already reported a clean pre-fix environment and fresh exact `tools/list` schema, but that does not cover the corrected worker bytes.
5. Rerun the native fixture above after the lock gate and review real Blender parenting, save/reopen invariants, and actual-byte export/reimport results before production use.
6. Only after those gates, measure the actual accepted V13 gun-bearing bone and muzzle position/axis; no caller values are supplied or inferred by this engineering task.
7. Perform the accepted V13 mesh/material/weight/scale and seven-action comparisons and the exact frame-145/frame-50 muzzle-follow proof before runtime wiring.

## Simplifications, omissions, and blockers

No geometry regeneration, replacement motion, inferred muzzle coordinates, source fallback, counter regeneration, or runtime substitution was introduced.
The implementation intentionally requires a retained-action source checkpoint, sibling output, exact existing parent, and registered leaf Empty; it does not expose a general bone/weapon authoring operation or arbitrary Blender execution.
It does not silently add `chaosx_working` approval to reimported rigs or meshes.
Parent intake reports that no approved V13 working checkpoint survives, only the accepted actual-byte proof scene with `io_pdx_rig` and `char1.002`; explicit audited-checkpoint promotion remains a separate parent-owned blocker.
Do not invoke `import_animation_action` merely to obtain its promotion side effect, because that operation also rewrites actions.
Do not adopt the rejected manual-recovery geometry, action set, parent name, or coordinates as a workaround.

The parent reports native synthetic author/save/reopen and posed follow success before the first-root check failed, plus pre-correction schema/environment verification; these partial results do not prove mesh export or actual-byte reimport.
Native execution after the RNA correction, actual `.mesh` locator bytes, all seven production `.anim` reimports, contact/axis preview acceptance, and relocked environment verification remain pending with the parent.
The 32 isolated tests are source-level evidence only and do not close those gates.
The user owns all in-game acceptance, and no game was launched.

Skills used: `chaos-redux-3d-model-pipeline` for the bounded adapter/export/evidence contract; required supporting `chaos-redux-event-assets` and `chaos-redux-subagents` for preservation and ownership boundaries.
No skill was created or updated.

## Parent verification and reviewed adapter integration

The parent promoted the adapter/configuration/operation contract to version `1.10.15`, registered `chaosx_blender_hoi4_author_locator` in the Codex tool allowlist, and added the exact `BlenderAdapterClient.author_locator` argument-forwarding method.
Qoder and Cursor configuration was not changed.
Locked adapter Python, the client, and configuration JSON use explicit LF attributes; the parent normalized only the reviewed locked text paths and retained the existing canonical `normalization_convergence.py` digest.
No provider package, Blender installation, or io_pdx_mesh installation was replaced.
This was a reviewed local adapter lock refresh, not a claim that a latest-dependency bootstrap ran.

After the RNA equality correction below, the final worker digest is `F5F6F335C1A62EA5B5C4E2A6CA57EED414258A0E561A216742792A4FB6FFF6BF`.
The MCP declaration digest is `65A652028A7F9FE934C7D3AA06BA5976267BFAE2E43A531A1EDD44A33811E16D`, client digest is `AFE8989DB395E657E6B2F6A3E853FE02F398C4371B4A6ED6EECFD5A0535612D5`, and adapter configuration digest is `B3DB95EED28B98557319831823CAD563A6F078C06CD3DA2E59D4E64A14D17CD9`.
`.tools/3d_pipeline/verify_environment.py` completed with no findings against these actual raw bytes; its report is `.tools/3d_pipeline/reports/environment_report.json`.
Meshy was not probed and no credits were spent.
A fresh process through the configured wrapper exposed exactly the eight required locator arguments, fixed-length three-coordinate/four-quaternion arrays, and no arbitrary execution input.

The parent reran all 32 locator contracts, all five bounded BVH-import regressions, and all 12 animation-processing regressions successfully.
The animation suites include native import/save/reopen, dual-source action preservation, nearest-face weights, and normalization regressions, preserving the current animation-processing path.
The native locator fixture was run with:

```powershell
& 'C:/Program Files/Blender Foundation/Blender 5.1/blender.exe' --background --factory-startup --python-exit-code 1 --python '.tools/3d_pipeline/tests/blender_locator_adapter_integration.py'
```

It returned `status: pass`, `fixture_only: true`, and `production_asset_acceptance: false` under Blender `5.1.2` and io_pdx_mesh `0.91.0`.
Authoring and save/reopen preserved the fixture's geometry, materials, UVs, weights, rig, retained action keys, scale, and unrelated Empty.
The actual exported `.mesh` contained only the registered `fixture_muzzle` locator with parent `fixture_weapon_bone`, and the unregistered decoy was excluded.
The locator survived actual `.mesh` and `.anim` byte reimport and followed the moving, rotated bone after a `1.75` uniform rig-scale conversion.
Maximum world-matrix errors at frames 1, 6, and 12 were respectively `3.725290298461914e-07`, `5.960464477539062e-07`, and `2.682209014892578e-07`, below the fixture tolerance `2e-4`.
The fixture mesh digest was `8F149DD0C60978FE20951422C723CC2CA69191CA080BB8CC0C712D74DEBC2F15` and animation digest was `0E752DAC920B0A85F7A560EEA808590A5E89B139913347D3CA5F33563154E637`.
The disposable test directory was cleaned by the fixture; these are test-artifact fingerprints, not shipping model files.
The only reported compatibility warning was Blender's deprecation notice for `Material.use_nodes` in the test setup; it did not prevent export or reimport.

This parent evidence supersedes the earlier unrun local-environment, schema, native-fixture, and lock-refresh gates in this handoff.
It does not supersede the missing accepted V13 working checkpoint, actual muzzle measurement, seven accepted-action reimports with the new locator, source-audio and particle/light integration, or final runtime package review.
No production model was changed, no geometry was regenerated, and no game was launched.
