# Event 014 Cannibal Bone Guard 3D handoff

> Historical blocked handoff. Superseded by the accepted installed Bone Guard runtime receipt and current package manifest; retain this file for the original provider failure evidence only.

Status: **incomplete; blocked by Meshy pose estimation before skeletal export**.

The generated source lineage described below is superseded by the parent’s final artwork gate. The old input, geometry, and descendants remain rejection evidence only; current work requires actual sourced or user-supplied artwork followed by faithful enhancement without redesign.

## Outcome

The Bone Guard has an approved exact-one reference, a selected Meshy 7 geometry candidate with the required poleaxe and bone-armour identity, measured vanilla scale, seven-view geometry evidence, 1024 PDX material DDS files, a complete licensed six-role audio package, and a linked bespoke three-surface counter package. The selected complete geometry failed the Meshy humanoid rig endpoint. Consequently, all eight required provider-sourced actions, `.mesh`/`.anim` exports, and reimport proof remain blocked. No runtime files were changed and no in-game completion is claimed.

## Source and provider lineage

- Superseded generated input: `docs/assets/014_cannibalism/models_3d/cannibal_bone_guard/refs/original/meshy_input.png`.
- Input SHA-256: `0966093155490EC1C8121C17D3E3054ACCD4B646BC4A0385EBC98C65598FB52D`.
- Decoded input: 1148x1722 RGBA with a transparent outer border; heavy two-handed bone-handled poleaxe is visible.
- Provenance: a text-only adaptation of Vornyx’s modern artwork `The Bone Hunter`; source pixels were not passed to ImageGen. Source remains reference-only/all-rights-reserved evidence, and the generated adaptation is rejected under the current faithful-enhancement gate.
- Rejected original generation: `01a02942-75a0-730f-9206-12250094a62f`, heavy poleaxe omitted.
- Rejected original rig: `01a0295b-f18f-79bc-9b10-e35324146164`; retained only as a possible professional animation-source rig, never as selected geometry.
- Rejected original conversion: `01a0295e-3396-7a76-91be-4f27e2f76db2`.
- Rejected T-pose replacement: `01a02986-ad90-77b6-bb1b-4cac978e64e5`, prop-stripping risk.
- Selected recovery generation: `01a02992-3227-70d8-9930-f8b6e3bb28db`.
- Selected GLB SHA-256: `904150E92B78713A6B283F197B472F1D8E8F162CBCBD882F9D0F5FE4FD01F00D`.
- Selected FBX SHA-256: `4A1A3B113BEE22FF082ABED797ADDB919F570093BA8002C4171F51F43382DAB6`.

Existing lineage records report 90 earlier generation/recovery credits, 5 earlier rejected-rig credits, and 1 earlier conversion credit. In this tranche, the live balance before rigging was 820. The single estimated 5-credit rig call failed HTTP 422 with `Pose estimation failed, please provide a valid model`, returned no task id, and recorded no confirmed consumption. No animation credits were spent.

Provider request/response evidence:

- `provider/requests/001_meshy_check_balance.json`
- `provider/responses/001_meshy_check_balance.json`
- `provider/requests/002_meshy_rig.json`
- `provider/responses/002_meshy_rig.json`
- `provider/credits/001_meshy_check_balance.json`
- `provider/credits/002_meshy_rig.json`

## Locked environment

- Meshy MCP: official `@meshy-ai/meshy-mcp-server` 0.4.0 through `.tools/3d_pipeline/wrappers/run_meshy_mcp.cmd`.
- Meshy compatibility: `meshy-7-v4`; exact verified generation identifier `meshy-7`.
- Meshy git head: `d8c77ffbe5f1149fb3d2b435802639440107a48d`.
- MCP SDK: 1.29.0.
- Blender: 5.1.2, build `ec6e62d40fa9`.
- Blender adapter: `chaosx_blender_hoi4` 1.8.1.
- Health request: `c403356ac0754cea9bdd0afc55878380`.
- io_pdx_mesh: 0.91.0, locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Fresh repository environment verification returned zero findings before Blender work. Exact Meshy wrapper/node processes were zero after lease release.
- Detailed hashes and route evidence: `docs/assets/014_cannibalism/models_3d/cannibal_bone_guard/evidence/dependency_lock_receipt.json`.

## Geometry, scale, materials, and rig

- Working candidate: 30,000 triangles, 14,850 vertices, one visible working object.
- Dimensions: `4.309507 x 3.023676 x 7.351825`; minimum ground Z `0`.
- Topology: zero non-manifold edges and zero degenerate faces; 236 loose boundary edges across 56 boundary components remain. Bounded closure was rolled back because it risked visible geometry. This remains an export-risk finding.
- Vanilla reference: installed `western_european_infantry.mesh#polySurface106`, source height `7.351824797689915`, forward `-Y`, up `+Z`.
- Entity precedent: installed `units_infantry.asset#infantry_rifle_entity`, scale `0.8` exactly once, effective height `5.881459838151932`.
- Geometry report: `blender/reports/cannibal_bone_guard_prepare.json`.
- Scene audit request: `da3c9fd96aa24c168c1b5bcf8004f6f3`.
- Seven-view previews: `blender/previews/cannibal_bone_guard_{front,rear,left,right,three_quarter,top,underside}.png`.

Final candidate texture hashes:

| Map | Path | SHA-256 |
| --- | --- | --- |
| Diffuse | `textures/processed/cannibal_bone_guard_diffuse.dds` | `7BF6FE5B44766304A839187C8FC499110FFBD977C1378803AB54FCB63C953632` |
| PDX specular pack | `textures/processed/cannibal_bone_guard_specular.dds` | `4370691BE9A66A80657A385185F8AFEDD8962465A24426DA7EE77AF51AEA8643` |
| PDX normal | `textures/processed/cannibal_bone_guard_normal.dds` | `AE5CE458A33262D766CA045A2C9AB7442DADA7ADBFD180850F2309621079560E` |

All three are 1024x1024 legacy one-level uncompressed BGRA DDS files with complete 128-byte headers and exact 4,194,432-byte lengths. The PDX pack derives from the immutable provider maps and is not raw roughness used as specular. Adapter texture rewrite request: `4955e781558346a388c191b9e5f77481`.

After the provider rig failure, `author_humanoid_rig` produced `blender/checkpoints/03_provider_motion_target.blend` as an allowed skeleton-preparation target only. It has 24 bones, zero unweighted vertices, and three influences per vertex. Request id: `e45c30b0ebe246c088ecb94d8c34e1e1`. The prior local action set is explicitly rejected and cannot be exported.

## Required action status

| Role | Intended verified Meshy action | Status |
| --- | --- | --- |
| idle | 335 `Axe_Breathe_and_Look_Around` | Blocked: no paid animation call made. |
| move | 672 `Spear_Walk_inplace` | Blocked. |
| attack | 237 `Charged_Axe_Chop` | Blocked; must visibly include aim/charge, overhead chop, impact, recoil, and recovery. |
| defend | 85 `Axe_Stance` | Blocked. |
| support_attack | 99 `Reaping_Swing` | Blocked. |
| retreat | 688 `Walk_Fight_Back_inplace` | Blocked. |
| training | 327 `kettlebell_swing` | Blocked; must be reviewed as semantically acceptable rather than accepted by name alone. |
| death | 188 `Fall_Dead_from_Abdominal_Injury` | Blocked; must show articulated collapse and settling. |

The ids/names were selected from the official Meshy animation library. They are plans, not completed action evidence. No static, transform-only, local replacement, or semantic reuse is accepted.

## Sourced audio

The audio package is complete at the asset-handoff boundary. All derived files are PCM s16le, 44.1 kHz, mono. No audio was generated, synthesized, recorded, or replaced with a placeholder.

| Role | Source/license | Derived file | SHA-256 | Proposed sync |
| --- | --- | --- | --- | --- |
| Selection/acknowledgement | HaelDB, `Male Grunt/Yelling Sounds`, CC0 option | `audio/derived/cannibal_bone_guard_selection.wav` | `d86b198e177d8bbea93d791b0fc0a7993526da3ba08749f1f7c6f354a9033727` | Country/original-tag voice consumer, not per-subunit. |
| Idle vocal | HaelDB, same CC0 source | `audio/derived/cannibal_bone_guard_idle_vocal.wav` | `3cecf191c8c50dbf4f6a1793bb9a9670f7a22c19f4ecde0def495c71cc597fcb` | Occasional one-shot, not a seamless loop. |
| Movement | GboxMikeFozzy, `Footsteps`, CC0 | `audio/derived/cannibal_bone_guard_movement.wav` | `8dbbfe7e5e719f17cf8a551e0bfefbcfcabd209231245e5` | Move contact frames 0 and 12 after final timing. |
| Poleaxe swing | artisticdude, `Swishes Sound Pack`, CC0 | `audio/derived/cannibal_bone_guard_weapon_attack.wav` | `b2a4ca45195a127153304a3b3339dc018d879611d72599de4c3fc89bb993cd74` | Heavy downswing near frame 12 after final timing. |
| Impact | rubberduck, `100 CC0 Metal and Wood SFX`, CC0 | `audio/derived/cannibal_bone_guard_weapon_impact.wav` | `8e0d679d129215a58fd2b94fb22d588753349c7f93948a8776945b1218f787b0` | Contact near frame 16 after final timing. |
| Death | stilgar, `Male Pain Grunts`, public domain | `audio/derived/cannibal_bone_guard_death.wav` | `3d292d23cde81ee4869665f93fbeea6b4561a324e7936db61866dd59db7a078a` | Collapse interval approximately frames 12-36. |

Exact source-page and direct-download URLs, immutable originals, original hashes, attribution, licenses, transformations, durations, and archived HTML paths are in `evidence/audio_sources/provenance_manifest.json` and `ffprobe_and_hash_receipt.json`.

## Bespoke counters

- Large: `GFX_unit_cannibal_bone_guard_icon_medium` -> `gfx/interface/counters/divisions_large/unit_cannibal_bone_guard_icon.dds`, SHA-256 `4189a8e5f1f943151d90847a003484bed676805606b2eecdf347616345da62d1`.
- On-map: `GFX_unit_cannibal_bone_guard_icon_medium_white` -> `gfx/interface/counters/divisions_small/onmap_unit_cannibal_bone_guard_icon.dds`, SHA-256 `21aa17a7c2d3d0e366f9ef42b307d3f4dbd77a8dc1381929eb5464715e313bba`.
- Texticon: `GFX_unit_cannibal_bone_guard_icon_small` -> `gfx/texticons/unit_cannibal_bone_guard_icon_small.dds`, SHA-256 `c3b380aaf7d42bfa6e838ab172db313762fab7e68913c9693fc41f175ee5ed32`.
- Large canvas: 152x42, two 76x42 frames. Small/texticon: 60x12, two 30x12 frames.
- Installed definitions: `interface/subuniticons.gfx` and `interface/texticons.gfx`; installed DDS precedents are the infantry large/on-map and irregular-infantry texticon strips.
- Matching skill-local reference families: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/` and `map_counters/`.
- Palette evidence: dominant normal large/texticon green `(73,106,73)`, neutral grayscale on-map normal state, pale selected state, transparent unused canvas.
- Detailed audit: `docs/assets/014_cannibalism/models_3d/cannibal_bone_guard/evidence/counter_audit.md`.
- Parent handoff: `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_cannibal_counter_art_handoff.md`.

No shared counter or GFX file was edited in this tranche.

## Files created or changed in owned scope

- `job.yaml`
- `history.jsonl`
- `manifest.json`
- `runtime/handoff.md`
- `evidence/dependency_lock_receipt.json`
- `evidence/counter_audit.md`
- `evidence/audio_sources/provenance_manifest.json`
- `textures/processed/cannibal_bone_guard_{diffuse,specular,normal}.{png,dds}`
- `blender/checkpoints/02_materials_approved.blend` (texture paths rewritten through adapter)
- `blender/checkpoints/03_provider_motion_target.blend`
- adapter request/result logs for health, scene audit, texture rewrite, and skeleton preparation
- Meshy request/response/credit evidence for balance and failed rig
- this parent handoff

## Meaningful validation and blockers

- Reference checksum and decoded format/dimensions verified.
- Environment lock verified with zero findings; live adapter health confirms Blender/io_pdx_mesh.
- Selected geometry inspected through the adapter and reviewed in seven rendered views.
- Final DDS headers, dimensions, masks, lengths, and hashes verified.
- Six derived audio files decoded and verified as 44.1 kHz mono PCM s16le.
- Bespoke counter consumers, references, palettes, frames, and runtime hashes linked to their passing art evidence.
- Provider rig failed before a task id existed; therefore animation generation, deformation review, action timing, `.mesh`/`.anim` export, and io_pdx_mesh reimport proof were meaningfully skipped rather than substituted.

The package is incomplete. Remaining parent work is to authorize/serialize the provider animation-source recovery route, review all eight results, complete adapter transfer/cleanup/export/reimport, copy accepted assets to runtime, wire entity/GFX/sound consumers, and perform live in-game validation.

## Skills used

- `chaos-redux-3d-model-pipeline`
- `chaos-redux-event-assets`
- `chaos-redux-subagents`

## 2026-08-24 recovery-v6 dependency-lock blocker

Status: **required installation/verification; no provider, ImageGen, or Blender production call made in this tranche**.

The recovery-v6 parent brief requires the checksum-verified Blender HOI4 adapter at version `1.8.9`. The repository-owned dependency lock and adapter configuration both currently resolve version `1.9.0`. The current 1.9.0 source/config checksums match their lock exactly, so this is a parent-brief-versus-repository-lock conflict rather than a corrupt local installation. Pipeline policy forbids silently substituting a different adapter version.

- `.tools/3d_pipeline/config/dependencies.lock.json`: SHA-256 `5A952D9D9871CB68023F24BE16E74D2E5C035866DC22326B1C462EB17AE2C839`; `routes.blender_hoi4_adapter.version = 1.9.0`.
- `.tools/3d_pipeline/config/blender_hoi4_adapter.json`: SHA-256 `ECF95D17F7CA824082DFABE4D53E46D57076902C430DEAB784AC7C8A3D74A84A`; `adapter_version = 1.9.0`.
- Locked adapter source files all matched their recorded SHA-256 values: `chaosx_blender_hoi4_mcp.py`, `blender_worker.py`, and `blender_client.py`.
- `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`: SHA-256 `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`.
- The approved CMON source bytes are present as `refs/source/recovery_v5/selected_umkator_warrior_3.jpg`, SHA-256 `DB4164F9435588C85672B51CE0F81AF4B47A950CE43686755FB6406D8F1D7F41`. The parent-named sibling `refs/source/recovery_v5/selected_source.jpg` does not currently exist; the hash unambiguously identifies the existing file.
- `MESHY_API_KEY` passed the nonblank process-environment gate. No balance check or paid operation followed.

Required resolution: the parent must explicitly reconcile the required adapter version with the repository lock, either by authorizing the currently locked 1.9.0 route or by restoring and checksum-locking the required 1.8.9 route. After that reconciliation, recovery-v6 can resume from faithful native-ImageGen cleanup of the approved CMON source and proceed through Meshy 7 generation, eight verified provider actions, adapter processing, export, and reimport.

No commit was created because the worker package remains incomplete and the dependency gate stopped production before an isolated complete tranche existed.
