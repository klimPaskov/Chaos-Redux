# Event 014 Cannibal Bone Guard manifest reconciliation

Disposition: implemented as a metadata-only reconciliation of the interrupted package manifest; package status remains `needs_user_review`.

## Scope and ownership

This pass covered only `cannibal_bone_guard` in `docs/assets/014_cannibalism/models_3d/cannibal_bone_guard/`.

Parent scope retained nine gameplay families, seven bespoke model packages, approved cavalry and infantry reuse, and no animation toggle; this handoff changes none of those decisions and leaves Feast Cohort and every other package untouched.

No Meshy route, key, balance, or provider operation was checked or called, and no Blender, adapter, geometry, rig, weight, keyframe, export, reimport, runtime asset, wiring, or game operation was performed.

No commit was created.

## Files created or changed

- `docs/assets/014_cannibalism/models_3d/cannibal_bone_guard/manifest.json` — revised the existing partial draft into a clearly labelled current reconciliation and retained `needs_user_review`.
- `docs/assets/014_cannibalism/models_3d/cannibal_bone_guard/manifest.md` — replaced the partial summary with the accepted source basis, current consumer, reconciled bytes, conflicts, costs, and explicit unknowns.
- `docs/plans/014_cannibalism_plans/evidence/2026-10-03_cannibal_bone_guard_manifest_reconciliation.json` — records selected-input facts, exact source/task/action hashes, rechecked file-copy hashes, report paths, and remaining gaps; SHA-256 `cac4f78d33c73b46d1044ee6060de9d6c6ad39d5588686ed770ed96d1405ec2b`.
- `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_cannibal_bone_guard_manifest_recovery.md` — this handoff.

Existing `job.yaml`, old 3D handoff, reports, source receipts, runtime files, and other roots were read-only.

## Selected artwork and input basis

The recorded source is CMON / CoolMiniOrNot's *Um'Kator Warrior #3 for the Um'Kator Tribe, HATE board game*, credited to CMON / CoolMiniOrNot, Adrian Smith concept, Patrick Masson sculpt, and Angel Giraldez painting; recorded source SHA-256 is `DB4164F9435588C85672B51CE0F81AF4B47A950CE43686755FB6406D8F1D7F41`.

The package records source pages `https://www.cmon.com/hate-the-um-kator-tribe/` and `https://patrickmasson.artstation.com/projects/m2zR1?album_id=36250`, retrieval date 2026-08-24, and copyrighted/all-rights-reserved terms without a reuse or AI-use license; parent authorization is recorded for that exact source hash in `reference_only_user_authorized` mode.

The 2026-09-25 rebuild record says no explicit NoAI or no-derivatives restriction was found on the reviewed pages; that finding does not grant a license and remains separate from the exact-hash parent authorization.

The raw source bytes are absent at `refs/source/recovery_v5/selected_umkator_warrior_3.jpg`, so the hash is recorded but cannot be reverified from this package.

Parent-approved separate inputs dated 2026-09-25 are the item-free body `refs/prepared/body/candidate_02.png`, SHA-256 `B2493A5D71079261B301BEDE22D25DD0B3A91272721B0192453E9E7767B3F752`, and isolated poleaxe `refs/equipment/poleaxe/meshy_input.png`, SHA-256 `F464391AF83A97FC256D6FE1F8E248FB1B41D4E9191A571EDEFA68E5D89CF0FC`.

The parent approval and source-to-prepared comparison are in `refs/prepared/rebuild_2026-09-25_source_and_inputs.md`, SHA-256 `526e6b0e76019b1099e98c09f02ba47adaa0da7227723e5686f65c93bb886073`; its ImageGen prompts are summaries, not verbatim tool-call strings.

The older approved one-image reference `refs/original/meshy_input.png`, SHA-256 `1CE0692A404194C80358CE5B05A5CC1BBCED8E48328D1EE4CB0245084A64F74A`, is superseded as the body-generation input by the separated 2026-09-25 approvals.

`refs/processing_manifest.md`, SHA-256 `35081dc63ddd5d4c952b6842bcee2cdf9c2a0c4a6a51d7e88bfd3d8d78519680`, names older different source and input hashes and remains a conflicting historical record; it was not promoted into the current selection.

The earlier Vornyx *The Bone Hunter* research remains unrelated and unselected.

## Provider and export lineage

`job.yaml`, SHA-256 `64c14f09b1738257c297e85bf034fc9b3f272f30b799ab47af82565b99e8097a`, still has status `recovery_v6_scale_aware_retarget_in_progress` and names selected generation task `01a033f3-60c4-77a8-ad80-3f667b277422` from the older one-image input.

The job/history records that task's recovery-v6 GLB as `provider/downloads/generation_recovery_v6_retry3_weapon_model.glb`, SHA-256 `8A79DA3C164F42167F6E1F0A6A9ED8F0548F67C04020012FFEDABDFFD8829A7C`, but that file is absent; the named recovery-v6 rig input is also absent.

The package does retain `provider/downloads/cannibal_bone_guard_body_meshy7.glb`, SHA-256 `8CE1F66504AADF9C2BB635A06B28354BE06D970E27FBC7407C3C377BEAA70BC2`, without a retained generation task id or a link to the final export.

No poleaxe geometry task id or poleaxe GLB output is retained, so the approved item-only input is not connected to the exported assembly.

`blender/reports/export_mesh.json` names the absent weapon-inclusive recovery-v6 generation and rig sources; therefore the report does not establish that the installed mesh descends from the currently approved separate body and poleaxe inputs.

The historical job records recovery-v6 consumption of 94 Meshy credits; this reconciliation spent zero Meshy credits and made zero Blender operations.

## Installed binary identity and provider actions

The named export and installed runtime SHA-256 values were recomputed for the mesh and all eight actions; all nine pairs match the current runtime binding receipt `docs/plans/014_cannibalism_plans/evidence/2026-10-03_runtime_unit_bindings_after.json`, SHA-256 `a9dc4753057922ff00d1c06c0658625a8c79b75a90d8325a394555f91c0ebb76`.

The selected mesh is `exports/cannibal_bone_guard.mesh` to `gfx/models/units/014_cannibalism/cannibal_bone_guard/cannibal_bone_guard.mesh`, SHA-256 `89c9bac619a98753ac0d9510a51e3b8abdaa371a26a3f9ed767d74083937acc0`.

The eight verified provider action source records and matching hash-bound Blender import receipts are:

| Role | Provider task / action | Provider source SHA-256 |
| --- | --- | --- |
| idle | `01a03403-7774-7cae-ae5a-4a67baac54ac` / 335 | `082C7AE7B48EE3D7A61C7B331B4D26C83BBD30C6015093EF66AB397DAFE8C75D` |
| move | `01a03403-8321-7caf-9f90-714a561d99c5` / 672 | `06B1267BD7C8060EE360E31960578CC26F6883AE09C92D2B8B00896BBB78ECA1` |
| attack | `01a03403-90a9-754c-b2e5-bccece9b2f52` / 237 | `A190787250539481F45D77118C4144C9BA5386E6E3F150667F22453240ED7C5C` |
| defend | `01a03403-9b9b-7dbe-995e-fe4a0f74ef90` / 85 | `2F3AABA4178B08BD8D14E307A546E296E18EC81EE204BC4650C3D399367E9F93` |
| support_attack | `01a03403-a9cf-7489-961e-98c4d49e2f0c` / 99 | `D4151B9CF20673FD1A4BC6A9D8067CEC3C27FCF1DA73D3B9EA97C33999216E12` |
| retreat | `01a03403-bdb4-7cbc-bf62-328bc7a55a5a` / 688 | `61377F6B592F8382B5D535423DF5A7495937DA9A6F3EBE117D4207EE4334F1DA` |
| training | `01a03403-ce19-7dc8-8c32-876cca20c20a` / 327 | `E3937DAEFD41249FC1558E017C3444DFEC4A5DD91792B022544BDA1971884310` |
| death | `01a03403-dbdf-7499-89bf-b2e0f04a2554` / 188 | `1D731AA1C6E45362D9C3B6EDE80B4EA24FBF5A63452482E04E35063AB763AA7C` |

Each import receipt's `source_reference_id` and `source_sha256` match the corresponding action manifest record; the retained action FBX bytes are not present in the current provider tree, while the task IDs and provider artifact hashes remain in `history.jsonl` and `runtime/action_manifest.json`.

Runtime actions decode at 30 FPS; the source action manifest records 24 FPS, and its status remains pending. The runtime audit and source action manifest are recorded separately rather than silently harmonized.

The full runtime action paths/hashes and all eight import/reimport report hashes are listed in `manifest.json` and the reconciliation evidence JSON.

## Materials, audio, and counters

Installed diffuse `f9224aa4223ba5f34b19f1b9a636af0aaf7d14f4f3b6b4a1260b48297b02c24c`, normal `8f2ac8a8029f4845f6b437b051991518e545be2309d2c53877d3323ac9eec54c`, and specular `77193b163e9ea8ad2773c497d33fcb9ba8765a13d5c71ff8677a5524bd180d6d` maps rehash to the corresponding hashes in `evidence/recovery_v6_texture_receipt.json`; the processed DDS files are not retained in the job root.

Six derived audio files match six installed per-unit WAVs: idle vocal `3cecf191c8c50dbf4f6a1793bb9a9670f7a22c19f4ecde0def495c71cc597fcb`, movement `8dbbfe7e5e719f17cf8a551e0bf7e312d3db406a21bfefbcfcabd209231245e5`, poleaxe swing `b2a4ca45195a127153304a3b3339dc018d879611d72599de4c3fc89bb993cd74`, impact `8e0d679d129215a58fd2b94fb22d588753349c7f93948a8776945b1218f787b0`, training `9d1fee6a60b2cb084d6d0f1bf8418c9e082654c21824ea80ea180cff32de9469`, and death `3d292d23cde81ee4869665f93fbeea6b4561a324e7936db61866dd59db7a078a`.

The selection/acknowledgement derived WAV SHA-256 is `d86b198e177d8bbea93d791b0fc0a7993526da3ba08749f1f7c6f354a9033727`; its provenance assigns it to a country/original-tag voice consumer, and the named per-unit runtime audit has no matching per-unit path.

The large, on-map, and texticon counter files rehash to `4189a8e5f1f943151d90847a003484bed676805606b2eecdf347616345da62d1`, `21aa17a7c2d3d0e366f9ef42b307d3f4dbd77a8dc1381929eb5464715e313bba`, and `c3b380aaf7d42bfa6e838ab172db313762fab7e68913c9693fc41f175ee5ed32`; the counter handoff records their tokens and consumer paths, with live review pending.

## Calibration and limits

The selected vanilla calibration is `western_european_infantry.mesh#polySurface106` with `infantry_rifle_entity` scale `0.8`, source height `7.351824797689915 m`, effective runtime height `5.881459838151932 m`, forward `-Y`, and up `+Z`.

The export report records `7.355273246765137 m`, a `0.0034484490752220154 m` delta, 30,000 triangles, 14,934 checkpoint vertices, and zero source-report boundary, non-manifold, or degenerate findings.

The grounded attack reimport report records 23,957 export vertices and 16,444 raw loose boundary edges across 745 components; its separate position-weld diagnostic reports zero loose boundary and non-manifold edges, and this discrepancy remains for review.

The retained 2026-08-22 dependency receipt records Blender 5.1.2 build `ec6e62d40fa9`, adapter 1.8.1, add-on 1.0.0, and `io_pdx_mesh` 0.91.0 with archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`; a later recovery report mentions adapter 1.10.7, and the current export report does not identify its adapter version.

The complete paths, hashes, report links, and explicit unknowns are in `manifest.json` and `docs/plans/014_cannibalism_plans/evidence/2026-10-03_cannibal_bone_guard_manifest_reconciliation.json`.

No visual geometry/action acceptance, audio timing approval, live counter review, or in-game consumer acceptance is inferred from file existence, hashes, or retained parser reports.
