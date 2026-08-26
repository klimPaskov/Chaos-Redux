# Alien infantry V13 firearm-preset final manifest

Status: model, Meshy rig, seven distinct Meshy preset actions, PDX export, actual-byte reimport evidence, and static entity/GFX/animation/sound references are present. The missing authored muzzle locator, unbound particle/light definitions, strict audio-role gaps for selection/acknowledgement/impact/special action, and live in-game acceptance remain parent-owned blockers outside this package's completed 3D exports.

Commit `0e724fb8a` promoted byte-identical V13 mesh, animation, texture, entity, GFX, and animation-registration files into the engine-facing runtime tree. This manifest remains provider evidence and does not by itself prove runtime playback or live game acceptance.

## Approved source and provider lineage

- Exact provider input: `refs/original/meshy_input_v13_tpose_right_pointing_colored.png`.
- Input SHA-256: `2D72EEB020C8989B463F214D4B5FC1C29C4AB313AEEE9F033B71E6DE1881BF3A`.
- Source mode: user-supplied and explicitly approved exact input; one image only; no T/A-pose variant was created.
- Meshy model: exact locked identifier `meshy-7`.
- Rejected generation: `01a03dbc-7913-7257-961a-56dea6cf6b04`, 30 credits; the provider omitted the firearm. Its downloads and checksums remain preserved.
- Accepted recovery generation: `01a03dc3-905a-7d02-aba6-05500f877b97`, 30 credits; the integrated right-hand pistol, empty left hand at rest, and cyan muzzle cap were retained.
- Remesh: `01a03dc9-8951-79ad-bc08-ae94ad607dfe`, 5 credits, triangular target 100,000; bounded Blender export recovery reduced the working duplicate to 59,999 triangles after the first 99,857-triangle PDX export exceeded the 65,535 streamed-vertex limit.
- Meshy rig: `01a03dcf-f0ba-7b67-b769-5a2678b03a40`, 5 credits, 24 bones.
- Starting Meshy balance: 103. Consumed: 91. Final verified balance: 12.
- Machine-readable lineage: `attempts/v13_firearm_preset/provider_lineage.json` and the seven `*_animation_provenance.json` files in the same folder.

## Calibration and geometry

- Installed vanilla reference: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`.
- Entity precedent: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset#infantry_rifle_entity`.
- Vanilla source geometry height: 7.3518242835; entity scale: 0.8; effective runtime height: 5.8814594268; forward: -Y; up: +Z.
- Final V13 source geometry height: 7.3518023491; apply entity scale 0.8 exactly once at runtime.
- Final geometry: 59,999 triangles, 59,451 exported vertices / 30,035 position-welded source positions, one UV layer, zero degenerate faces, zero negative-scale objects, and no zero-length normals in reimport inspection.
- The pistol is fused to the source mesh and retained in every action. No separate weapon object, manual parenting, constraint, or weight repair was used.

## Final files

- `export/v13_firearm_preset/alien_infantry.mesh` — 5,478,802 bytes — SHA-256 `D03EA316E2C5DCC4BD3224AE7D3C62DF3F86E4CADA77A6A7535C15D74BDF8342`.
- `export/v13_firearm_preset/alien_infantry_idle.anim` — SHA-256 `D6936AE996DBE998DBEE0633B4DCAC346B6C5D974FC643ACA62AAC73719CB2EF`.
- `export/v13_firearm_preset/alien_infantry_move.anim` — SHA-256 `727BCA51B68EEA445198C1029331FF06F15F69215358ABC9CC29A4064096217F`.
- `export/v13_firearm_preset/alien_infantry_laser_attack.anim` — SHA-256 `288209BC4B9CBB3D19A629C2277DF7816CDF33B475EA68BF0D368F7C2E2150F0`.
- `export/v13_firearm_preset/alien_infantry_defend.anim` — SHA-256 `F07A8BC46D68F72DD622014CE31BA9420A3CC1FF419BF3690D44D5F42E9E3A73`.
- `export/v13_firearm_preset/alien_infantry_support_attack.anim` — SHA-256 `DADC3823EA4C2FE5F21F10DAE310F52D54E5379A124C01CDEE3AA954F4EE3061`.
- `export/v13_firearm_preset/alien_infantry_retreat.anim` — SHA-256 `DB9E72F782A19C84A7C4C8CF429654D0BAAAC59A7999B381CA9267DD598BD2DC`.
- `export/v13_firearm_preset/alien_infantry_death.anim` — SHA-256 `D8D26A8B7A6F01ADCB64103885171C837DB36CB7BBB6A6A15EB6C2D66F15D7A0`.
- `export/v13_firearm_preset/alien_infantry_v13_diffuse.dds` — SHA-256 `0A44479B3205D2E732A5E4A9D1ECFC45BC61830E38244C06D1C028A89A62D3AA`.
- `export/v13_firearm_preset/alien_infantry_v13_normal.dds` — SHA-256 `DF1F9C947B64478BA5B739BC215D18400EC38272B2325D2F19E395C108873E39`.
- `export/v13_firearm_preset/alien_infantry_v13_specular.dds` — SHA-256 `5F1224A4443C20432182668DB6F567CCAD02B9D8143F57F08DFB88183CCE755D`.

## Actions and semantic validation

| Role | Meshy action | Provider task | Frames/FPS | Validation |
| --- | --- | --- | --- | --- |
| idle | 0 `Idle` | `01a03dd1-23a5-7728-9c09-f09683d64ffe` | 121 / 30 | Genuine breathing/body motion; pistol retained; loop candidate. |
| move | 692 `walking_2_inplace` | `01a03dd1-28ea-7ba5-b6cc-dde26e5b2d01` | 37 / 30 | Distinct in-place walk; grounded contacts; pistol retained; loop. |
| laser_attack | 223 `Draw_and_Shoot_from_Back_1` | `01a03dd1-2d74-70b2-a151-e8d98c82e4de` | 236 / 30 | Draw, aim, discharge, visible recoil, and recovery; right-hand grip retained; left hand becomes genuine support contact during firing; cyan muzzle remains visible. |
| defend | 89 `Combat_Stance` | `01a03dd1-31cc-7729-9612-26eb8f7d44c3` | 51 / 30 | Distinct defensive stance motion; firearm contact retained. |
| support_attack | 234 `Walk_Forward_While_Shooting` | `01a03dd1-35e5-7f37-a601-70982bdf5f74` | 99 / 30 | Genuine advancing fire; visible aiming and recoil; firearm contact retained. |
| retreat | 685 `Walk_Backward_with_Gun_inplace` | `01a03dd1-3a02-7f38-8f3c-0236be3dc57e` | 31 / 30 | Distinct backward in-place motion; grounded contacts; pistol retained; loop. |
| death | 183 `Shot_and_Fall_Backward` | `01a03dd1-3dd9-772c-b0cd-9f7dc4de1fe4` | 106 / 30 | Visible hit, backward collapse, impact, and settled pose; pistol remains attached through the fall. |

Every final action was imported from its exact Meshy FBX, received only per-frame root-Z grounding correction, was exported through io_pdx_mesh, and was reimported from the actual `.anim` bytes with the final `.mesh`. Blender did not author replacement motion. Final reimport request IDs are `135501327e2d41eeaa6d02288a590442` (idle), `16b2e84c426e4f87b952e032513e5be1` (move), `d0a7b69a74d34f8d90a45fbbf74f3c66` (laser attack with final material staging), `0170c12bab23470e9179cb26756cd561` (defend), `1f55f798bb714cedbb2c0857dc178e64` (support attack), `4c8c301143e440b3a9029c2f12dc892f` (retreat), and `24ff4f5352654a11b4d66ea73b57ae98` (death).

## Toolchain and evidence

- Meshy MCP 0.4.0; pinned package git head `d8c77`; SDK 1.29.0; live schema SHA-256 `F7B9FB26D676DE2033BAB72BCFAE58DB5F7699C684E91B15345BFC8425BAFE6D`.
- Blender 5.1.2, build `ec6e62d40fa9`; Chaos Redux Blender HOI4 adapter 1.10.14; adapter live schema SHA-256 `C95235FCF880209187F559047953A35EF469A2D9F6018572F30E9BE4EFDAB5B6`; health request `221a034ed7a14b95afe1943024564ca9`.
- io_pdx_mesh 0.91.0; locked extension ZIP SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Lock hashes: `dependencies.lock.json` `C27768297FB7AD5ACC9C555E7C83DC77856908E2C628BF16D9A420095C64266A`; `meshy_tool_schema.lock.json` `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`; `blender_hoi4_adapter.json` `4BC97CA0B07580F5AA04B49E7B9FBD1C07EC88DF5C4D56CD3BA8846E630117AB`.
- Export/reimport reports are in `validation/reimport_v13_firearm_preset_*_final.json`; visual proofs are in `blender/previews/reimport_v13_firearm_preset_*_final*`; source and proof checkpoints are in `blender/checkpoints/`.

## 2026-08-26 firearm revalidation

- Live status checks through the locked Meshy MCP route returned `SUCCEEDED` for the accepted generation, remesh, rig, and all seven animation task IDs above. The live balance was 12 credits; revalidation consumed 0 credits.
- The official Meshy download operation restored the accepted generation GLB, remesh GLB, rig FBX, and seven preset-action FBX files under `provider/downloads/v13_firearm_revalidation/`; `download_manifest.json` records exact tasks, paths, byte lengths, and SHA-256 hashes.
- Fresh locked-adapter reimport of the final `.mesh` plus each final `.anim` regenerated actual-byte reports `validation/reimport_revalidation_2026_08_26_*.json`. The adapter request IDs are `14f0da7ee55c42d6b156cf830afa3dbd`, `494d325dd20d4d649f2b40cc40fdfe26`, `557e9557048540f4bba7cd975989d21d`, `dfbb5f5300c84133ab6ce3b41af1ead9`, `2b1f46f9e6984a158342add202ba8dbc`, `d25ea42ad0a54a38bad95bc8e02940af`, and `45f84dfe4b6a4412a0a37aedaad0f6ff` in role order.
- Reimported attack frames 1, 60, 118, 177, and 236 show rest, draw, two-hand aim/support, recoil/recovery, and return to rest with the same fused cyan-tipped firearm. Curated discharge evidence remains frame 145. Reimported death frames 1, 27, 54, 80, and 106 show reaction, backward collapse, impact, and settled supine pose with the firearm retained.
- The accepted V13 output remains the best valid package. No regeneration, re-rigging, new animation purchase, manual weapon attachment, or Blender-authored replacement motion was justified.

## Remaining blockers and parent work

- No engine muzzle/effect locator was authored because the locked adapter exposes no locator-create operation and manual firearm parenting is forbidden. The fused cyan muzzle cap supplies a clear visual effect point only. Parent must bind or create the runtime effect point without altering the accepted weapon integration.
- Audio is sourced and licensed for laser discharge, movement, idle, and death. Per-subunit selection is blocked by tag-wide vanilla consumers; no accepted sourced impact or special-action candidate exists. See `runtime/sound_handoff.md` and `evidence/audio/provenance/audio_sources.json`.
- Bespoke vanilla-green large and on-map counters already exist and were not overwritten. See `runtime/counter_handoff.md`; live display acceptance remains parent/user-owned.
- Commit `0e724fb8a` copied the accepted binary exports and static entity/GFX/animation registrations out of `docs/assets` into the engine-facing runtime tree; the promotion handoff records the byte-identical hashes, and no runtime consumer may point into this evidence tree.
- Parent owns final review of the promoted `.asset`/entity/GFX/sound/gameplay consumers, supported effect-point binding, strict audio-role decisions, state-event timing review, and live in-game validation. This package does not claim live in-game acceptance.
