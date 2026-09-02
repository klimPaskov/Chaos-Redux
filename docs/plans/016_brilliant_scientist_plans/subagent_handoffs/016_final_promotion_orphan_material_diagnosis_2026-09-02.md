# Promotion material-retention diagnosis and bounded correction

Status: source frozen after 29 focused promotion contracts, 32 locator contracts, and a successful native Blender 5.1.2 disposable fixture on adapter 1.10.17.
The fixture includes real orphan disappearance and real consumed-material mutation/fake-user disappearance rejection.
No production promotion was retried, no production material or checkpoint was changed, and the existing failed copy remains unapproved.

## Observed production failure

The adapter owner read the existing failure report at `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/blender/reports/promote_v13_firearm_preset_alien_locator_working_2026_09_02.json` and the model worker's bounded inspection receipts.
The six non-material fingerprint sections matched and all four inputs remained immutable.
Only the complete material-section hash changed, from `7FBC9DCCA9F50802AD566677B0E970628F6EE09A6127A555A167C4F1C65689EA` to `1C98AEF3FE1A8E8C4954A0CD91A7ED7F0BC5385E1A3A77044A7A0308D61F0ABE`.

The exact point-path evidence available in the existing bounded inspections is:

| Material path | Source receipt `080c12a86111471ea99641f36d3a651d.result.json` | Failed-copy receipt `deaffb66672645998bed0a1af5a84b14.result.json` |
|---|---|---|
| `materials[name=Material]` | Present; no images; no Base Color, Metallic, Roughness, or Normal input links | Absent |
| `materials[name=Material].principled_defaults.Metallic` | `0.0` | Material absent |
| `materials[name=Material].principled_defaults.Specular IOR Level` | `0.5` | Material absent |
| `materials[name=Material].principled_defaults.Emission Strength` | `0.0` | Material absent |
| `materials[name=PDXmat_char1.002]` | Runtime material with three image bindings and connected shader inputs | Exactly equal for every field emitted by the existing inspector |

Both receipts live under the job's `logs/adapter/` directory.
The adapter owner compared their complete reported PDX material objects as JSON and obtained equality.
The runtime bindings remain diffuse Color to Base Color, specular Alpha to Roughness, Separate Color Blue to Metallic, normal texture through Normal Map, and Principled BSDF to the same surface output.
No rendering-meaning change is observed in those reported runtime fields or in the complete image fingerprint.
The old inspector does not expose native ID user counts, fake-user flags, or every fingerprinted material field, so these old reports alone do not independently certify the complete retained-material hash or an empty native consumer set.
The corrected operation must prove those facts from native data before any production retry can pass; it does not infer an orphan from the name `Material` or from absent texture links.

The source remains `blender/checkpoints/reimport_v13_firearm_preset_laser_attack_final.blend`, SHA-256 `CFF8D96C29A91DD6ACB9E8CE638521AD70171092EB354DC8D787FC113350E748`.
The failed copy remains `blender/checkpoints/v13_firearm_preset_alien_locator_working_2026_09_02.blend`, SHA-256 `70CA01923E64DDC9FD671DD5801951973ED4FD3E7B0232CADDEAAABA8DE97185`.
Both hashes were rechecked read-only by the adapter owner.
Neither file was opened by this subagent in a production Blender process, written, deleted, relabelled, or approved.

## Parent-approved rule

The parent explicitly approved a retention-aware comparison for normal native serialization of nonconsumer material metadata.
This is not a material-repair operation, rendering tolerance, skipped material check, or permission to change an accepted model.
The complete pre-metadata versus pre-save fingerprint comparison remains exact, including all material inventory and retention facts.
The sole allowed post-reopen delta is disappearance of a material independently proven, before saving, to meet every condition below:

- Native `users` is the integer zero, with neither fake-user nor extra-user retention.
- The material is local and has no library or override.
- Neither the material nor its embedded node tree has a source/reference protection flag.
- The node tree has no fake-user, extra-user, library, or override retention.
- Blender's complete ID user map contains the material key with an empty consumer set.
- Independent scans find no slot referencing it in any mesh datablock or object material slot, including unlinked meshes.

The implementation uses `bpy.data.user_map(subset=materials)` without value-type filtering.
The installed Blender 5.1.2 native docstring was emitted by the fixture and confirms that this returns the IDs using each requested datablock.
This matches the [official Blender ID user-map contract](https://docs.blender.org/api/2.93/bpy.types.BlendData.html#bpy.types.BlendData.user_map); the installed native behavior was the tested authority.
An absent map key is an error, not evidence of no consumers.

The worker never sets a fake-user flag, removes a material, clears a user, modifies a node, changes an image, or changes material slots during promotion.
Native save/reopen alone may remove an eligible orphan.
Linked materials and the pre-existing unsupported material cases remain fail-closed.

## Report and comparison contract

The original complete `sha256.materials` section is retained unchanged, along with all other original section hashes.
`material_retention.retained_sha256` hashes the complete material records that are not proven discardable orphans.
`material_retention.inventory[material_name]` records the complete per-material record hash, native user/retention/protection facts, complete ID consumers, exact mesh/object slots, and the derived `discardable_orphan` classification.

`reopen_comparison` returns:

- `accepted`, the exact comparison result.
- `mismatches`, with specific section or material-inventory paths.
- `removed_orphan_materials`, each with its exact name, full before-inventory record including `record_sha256`, and explicit native-save disappearance reason.
- The policy identifier `exact_retained_materials_and_all_other_sections_only_proven_orphan_disappearance`.

Every retained-material record and retained aggregate hash must match exactly.
Every orphan remaining after reopening must match its complete before record exactly.
Any added material, changed orphan, newly consumed orphan, disappeared retained/fake-user/protected material, image change, or other fingerprint-section change rejects.
The comparator rechecks the native facts for each removed record rather than trusting the cached orphan boolean alone.
If no eligible orphan disappeared, the original complete material-section hash must also match exactly.
All four immutable input hashes and byte lengths remain required, and a rejected output is still reported as unapproved.

## Changed files and ownership

| File | Change |
|---|---|
| `.tools/3d_pipeline/adapter/blender_worker.py` | Read-only retention inventory, exact retained-material hash, strict post-reopen comparison, and explicit removal/mismatch evidence. |
| `.tools/3d_pipeline/tests/test_reimport_promotion_contract.py` | Seven additional contracts for native retention facts, consumer-map/slot checks, orphan-only disappearance, all prohibited mutations/removals, and exact pre-save behavior. |
| `.tools/3d_pipeline/tests/blender_locator_adapter_integration.py` | Version gate 1.10.17; native user-map docstring evidence; real producer orphan fixture; retained fake-user material; native negative checks. |
| `.tools/3d_pipeline/config/dependencies.lock.json` | Only the worker source hash was refreshed by this subagent under exclusive parent authorization. |
| This handoff | Failure evidence, explicit policy, tests, native results, source hashes, and production gate. |

The parent changed adapter/config/lock version to 1.10.17 and the config hash entry.
This subagent did not edit operation registration, MCP/client schema, runtime visibility, gameplay, assets, other lock entries, install scripts, or other handoffs.
The existing verifier regenerated `.tools/3d_pipeline/reports/environment_report.json` as generated evidence.
Existing staged and unrelated work was preserved; nothing was staged or committed by this subagent.

## Validation

Focused commands:

```powershell
python -B -m unittest discover -s .tools/3d_pipeline/tests -p test_reimport_promotion_contract.py -v
python -B -m unittest discover -s .tools/3d_pipeline/tests -p test_locator_adapter_contract.py -v
python -B .tools/3d_pipeline/verify_environment.py
```

Promotion tests passed 29/29 in 4.694 seconds; locator tests passed 32/32 in 7.234 seconds.
Environment verification returned `findings=[]` at `2026-09-02T13:31:54Z` with the exact locked worker bytes and version 1.10.17.
Meshy remained `not_probed`; no provider call or credit expenditure occurred.

Native command, run twice successfully with the final run also covering explicit native negative cases:

```powershell
& 'C:/Program Files/Blender Foundation/Blender 5.1/blender.exe' --background --factory-startup --python-exit-code 1 --python .tools/3d_pipeline/tests/blender_locator_adapter_integration.py
```

Final result: exit 0, `status=pass`, `promotion_status=pass`, `fixture_only=true`, and `production_asset_acceptance=false` on Blender 5.1.2 build `ec6e62d40fa9`, io_pdx_mesh 0.91.0, adapter 1.10.17.
The fixture creates only disposable synthetic geometry, retains real synthetic action keys, exports and reimports actual `.mesh`/`.anim` bytes, obtains the real producer proof/receipt/previews, promotes to a new copy, and independently reopens both source and copy.
An unretained mesh datablock initially references a test material, causing the material to be serialized into the producer proof while the unretained mesh itself is omitted.
On opening that proof, the test material genuinely has zero users and no ID/slot consumers; the next native save naturally omits it.
No mocked material drop or explicit adapter deletion is used for the successful path.

Observed native success facts:

- The sole removal was `FixtureUnretainedOrphan`, full record hash `AC93C592C9D459ECDADCD85855B2F48B125258557379BB5E609D865E81AEA555`.
- Its native before evidence was users 0; local true; fake-user, extra-user, protection, and tree retention false; all ID/mesh/object consumer lists empty.
- `FixtureFakeUserMaterial` remained present and exact, record hash `290B65EC4FC5513DE25EC2C20FFE2A66CAEFE8430176BE6D7A9F0C1B25EB55D3`.
- The consumed `PDXmat_FixtureBodyData` remained exact, record hash `D08E496F2BC257DFFA472212CBFC55DDCECE41A710CE708B9BBE105228C95A90`.
- The exact retained-material aggregate hash was `915C59EE7018244B1FC7FE765CEF3054705BA6F249571BCC9BD6F9AF75ED12CF`.
- All six other sections remained exact, including 12 measured vertices, 4 polygons, 12 loops, and retained action `io_pdx_rigAction`.
- All four input files remained immutable; the original proof remained unmarked as working and independently reproduced its original complete fingerprint.
- Locator pose-follow maximum error remained `5.960464477539062e-07`, below `2e-4`.

The native negative checks deliberately modify only disposable in-memory fixture state and never save corrupted checkpoints.
Changing the consumed material's actual Principled Roughness socket to `0.271` rejects with its material inventory path, retained-material hash, and complete material hash mismatches.
Removing the fake-user material rejects with `material_retention.inventory['FixtureFakeUserMaterial'].required_material_missing` plus retained/complete material hash mismatches.
The saved disposable working-copy hash is rechecked to prove those negative checks did not write it.

Final disposable artifact hashes were mesh `8F149DD0C60978FE20951422C723CC2CA69191CA080BB8CC0C712D74DEBC2F15`, animation `0E752DAC920B0A85F7A560EEA808590A5E89B139913347D3CA5F33563154E637`, producer source `B2FC83AF84FCD72ABE0542FC8BBE045F5C57D90428F312FA1CDC3CDE7F9DC564`, receipt `240418A63A4F4201299F6A03DDFF01DAC00987044167FAEA4F357F4344878581`, and derived working copy `F0F759FEF2523B6BE81706A5A4CC40C6E9C1DFEE178A357C68CF540E91ED5D78`.
The temporary fixture directory was deleted at completion; these are captured test-run receipts, not production authority.

## Frozen hashes and remaining gate

| File | SHA-256 |
|---|---|
| `.tools/3d_pipeline/adapter/blender_worker.py` | `EDC6AA3BF321E6D1922A480DF25FD844E4BAB38FC162965AEDD71742EBCD292F` |
| `.tools/3d_pipeline/tests/test_reimport_promotion_contract.py` | `448A0042CA3FD76239E75DD7A9A7E6B80302BAED8AEF6C12EC3817AE665D07BD` |
| `.tools/3d_pipeline/tests/blender_locator_adapter_integration.py` | `C8A826BF7343B40B898DD0E6499868C43E5CC3F8A23EB144316AB90E62E233AE` |
| `.tools/3d_pipeline/config/dependencies.lock.json` | `4BC905F4D453095F630CCAE3F7FF7F1E40329577C87B4C25CFFBB04968307AD4` |
| Generated environment report | `DF9101EE8DE7C38E991C15906242BEF830E1C1015235AE18A60094C76F2362FF` |

The worker, both changed tests, and lock are LF-only, with raw hashes matching LF-normalized bytes.
The generated report retains the verifier's CRLF output and is not a locked source.
The parent-owned config hash is `49C846CB221F48642A10AD528C188E1D117A39984E997F0FBC3AF51809CFEAD9`.
No source normalization exception or CRLF replacement hash was introduced.

Parent review remains required before a fresh production promotion request using a new sibling output and new report path.
The earlier failed copy and failed receipt must remain immutable and unapproved.
The production retry must independently report the exact retained-material equality and eligible orphan inventory; this native synthetic pass does not approve the Alien asset.
No simplifications, replacement geometry, new textures, material repair, action replacement, or runtime fallback were introduced.
The explicit parent-approved rule affects only native disappearance of proven unretained nonconsumer material metadata.

Skills used: `chaos-redux-3d-model-pipeline`, with its previously read required asset/subagent ownership guidance.
No skill was changed.
