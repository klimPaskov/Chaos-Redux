# Paleogenetic Creature provider recovery audit

## Outcome

Status: `blocked`.

The existing source-informed Meshy 7 geometry was preserved. No ImageGen, image-to-3D, remesh, new base model, local skeleton, local weighting, local animation, semantic alias, transform-only motion, export, runtime copy, or gameplay/GFX/sound-definition wiring was performed.

No paid provider call was made. The live balance was 13 credits and the parent explicitly prohibited paid calls. The existing completed rig task remains anatomically rejected, and the live provider schema exposes no materially different multi-limbed creature-rig input.

## Locked dependency and route evidence

- `MESHY_API_KEY`: present and non-blank; the secret was not read or persisted.
- Official server: `@meshy-ai/meshy-mcp-server` 0.4.0, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, package integrity locked in `.tools/3d_pipeline/config/dependencies.lock.json`.
- MCP SDK: `@modelcontextprotocol/sdk` 1.29.0, git head `e12cbd7078db388152f6e839abdbe09ba01f3f32`.
- Dependency lock SHA-256: `C27768297FB7AD5ACC9C555E7C83DC77856908E2C628BF16D9A420095C64266A`.
- Meshy schema lock SHA-256: `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`.
- Schema revision: `meshy-7-compat-live-declaration-2026-08-21`; exact generation model remains `meshy-7`.
- Live tools: `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, and `meshy_animate`.
- `meshy_rig` inputs: exactly one of `input_task_id` or `model_url`, with optional `height_meters`, `texture_image_url`, and `response_format`. No creature family, custom joint map, extra-limb, or cranial-chain input exists.
- `meshy_animate` inputs: completed `rig_task_id` plus integer `action_id`, with optional post-processing. It cannot add missing anatomy to a completed humanoid rig.
- Environment verification report: `.tools/3d_pipeline/reports/environment_report.json`, SHA-256 `8AB8A91BED9AD3AAC98170CA684278D70CAB6F5E87C28164244BBE6EE5E94724`, no dependency findings, live balance 13.
- Wrapper lifecycle: the concurrent schema probe passed; the first consecutive-probe run had one transient schema-start failure, then the isolated two-consecutive-probe rerun passed. No persistent wrapper process leak was observed by the successful verifier receipts.
- Blender: 5.1.2 build `ec6e62d40fa9`; bridge `127.0.0.1:9876` was listening.
- Repository adapter: `chaosx_blender_hoi4` 1.10.14; all five locked adapter/config SHA-256 values matched.
- Adapter health request: `57e98866b62b44bb8da0bd86053eb80c`; result SHA-256 `BC1D091E20047ED1ECC5E37BC7407E0806F5ADFE54E41B4672FA7D552E0FE072`.
- `io_pdx_mesh`: 0.91.0; archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`; health confirmed mesh/animation export functions. Export was not authorized because the rig/action gate failed.

## Provider lineage, costs, and retained files

| Stage | Task | Status | Credits |
|---|---|---|---:|
| Existing Meshy 7 image-to-3D | `01a0427d-0a5f-746f-8270-f64b4ba409c1` | `SUCCEEDED`; live status rechecked | 30 consumed previously |
| Existing first rig submission | no completed task id | HTTP 422 pose-estimation failure | 0 consumed |
| Existing generic rig recovery | `01a04285-34b0-7d0f-b256-e2c3f0048d67` | `SUCCEEDED` technically; anatomically rejected | 5 consumed previously |
| This recovery audit | none | no paid call; live balance 13 | 0 consumed |

| File | SHA-256 |
|---|---|
| `provider/downloads/generation_01_model.glb` | `AF53CF07DE8FE610F30D8676566980DF89D420C4DC703EDB67E5DCB490F2D0FD` |
| `provider/downloads/generation_01_model.fbx` | `0390E40FBF9D943EC03F3CE92357489D99542F7A55125AFB83CB903809BEB8A1` |
| `provider/downloads/rig_01_primary.glb` | `3BCFBD1DC58E7F2542EBA4764DC78F12207F97AC4DC533A349FD56D42A4CB4D0` |
| `provider/downloads/rig_01_primary.fbx` | `595FBAFAC61222763AC35AFE4882C4814A14EF6C1A28124BDB48DDA5029F40B1` |
| `provider/downloads/rig_01_walking.fbx` | `EC0A501847193CCCE3956BCC6BDF37F14C76D8D22FEB5B662697C85A327A76D4` |
| `provider/downloads/rig_01_running.fbx` | `BC9FF6AAD1148A601DBEA5D7579B43A1D71EC98BAB827822E6560A38A8D93993` |
| `blender/source/chaosx_paleogenetic_creature_provider_source.blend` | `3EE8C3C11D9295C6CF6DA4010DCA6D57129BA74B0F9FBDB23BB5A685CFD2DB90` |
| `blender/source/chaosx_paleogenetic_creature_rigged_provider_source.blend` | `1FE6AC7E3DB9700AF1D3A8A6B1F218A48A8431DE7E931424C2B9D454DEAB8358` |
| `blender/reports/chaosx_paleogenetic_creature_prepare.json` | `431D2CD411DA72632530B243CE9702C9CE511CCE31020BA40CBA8A74BE0DCE78` |
| `blender/reports/chaosx_paleogenetic_creature_rigged_prepare.json` | `F4EEB6DC8F9DF5C3EF13B061A674435E6371D476F42BB4BA8CD3EDCDF875229D` |
| `blender/reports/creature_components.json` | `D746F0B64A4D51A471A9843D178AE32E871AC6A87E14937689CD706B93AB69A2` |

Current package-document and request-receipt hashes after this audit:

| File | SHA-256 |
|---|---|
| `job.yaml` | `CD65395058A553DB95298D9C7C87C5D97E0F596CA4880366C31D3199D7D3348A` |
| `manifest.md` | `43C0FEAFAE5CA549B003E53CCCEC616360438B7B66A75C903555C5786B2585F7` |
| `history.jsonl` | `C7EC99DADCFCE31FB555ACDF6C771E6167760C0A301F0DC505F8A4133C8B5BFB` |
| `runtime/handoff.md` | `1FCED1C03F7D8D2258521BE8DE22732B376B126E0C223372EFE369B452B0A883` |
| `runtime/crosswalk.md` | `39B8A3E2964C0B729FA423412AC4F5A76D475BA283BE3E6ED7E9C159F4754C26` |
| `audio/provenance.md` | `9EDD61404B2DF354F5B830B0E2CD4C76586098EB5D7F08A0AA9C72A62FB37771` |
| `audio/sound_handoff.md` | `CE470B5C1178D368F67C4AC0AFBB4AB73661E23F3B1E692AF689F97B56CAC6CF` |
| `counter_handoff.md` | `3ABA7744EEB35BB616A0E7B9A235A3C94CD9C164E7CABA02DCD27C4A2A4B401D` |
| `logs/adapter/57e98866b62b44bb8da0bd86053eb80c.json` | `6C4748FC2429866F006B71972FFDD7201C76EFA5F204ABE461C1F226240BB5AE` |
| `logs/adapter/57e98866b62b44bb8da0bd86053eb80c.result.json` | `BC1D091E20047ED1ECC5E37BC7407E0806F5ADFE54E41B4672FA7D552E0FE072` |
| `logs/adapter/fb386107938c496a9dcad2c0a8c36b84.json` | `2B80737BA2DAD99390327DAE373BDCCCC4BE4E6C58BD57C84F4E4AF8A8AEB9FF` |
| `logs/adapter/fb386107938c496a9dcad2c0a8c36b84.result.json` | `0D19C8E5926C4009960196442000874AF1EC40B04340DABA222D93B13AE45905` |

## Exact anatomy and animation blocker

Locked-adapter read-only inspection request `fb386107938c496a9dcad2c0a8c36b84` produced `logs/adapter/fb386107938c496a9dcad2c0a8c36b84.result.json`, SHA-256 `0D19C8E5926C4009960196442000874AF1EC40B04340DABA222D93B13AE45905`.

The rejected provider source has one 24-bone humanoid armature. Its only upper-limb chains are `LeftShoulder -> LeftArm -> LeftForeArm -> LeftHand` and `RightShoulder -> RightArm -> RightForeArm -> RightHand`. Its cranial chain is `neck -> Head -> head_end`, with no second cranial chain. It therefore lacks two required arm chains and the independent secondary cranial chain.

The rejected result also contains two geometry objects totaling 1,914,184 triangles, 637 non-manifold edges, a separate unweighted `Icosphere.001`, no accepted creature material binding, and only two 2-frame clips. The walking/running downloads are tied to this invalid humanoid result and cannot satisfy creature locomotion.

| Required semantic role | Proposed runtime id | Status |
|---|---|---|
| Idle | `chaosx_paleogenetic_creature_idle` | blocked: invalid rig; no substantive provider action |
| Stalk | `chaosx_paleogenetic_creature_stalk` | blocked: invalid rig; no substantive provider action |
| Move | `chaosx_paleogenetic_creature_move` | blocked: rejected humanoid walking cannot preserve four-arm anatomy |
| Charge | `chaosx_paleogenetic_creature_charge` | blocked: rejected humanoid running is not an accepted charge action |
| Attack | `chaosx_paleogenetic_creature_attack` | blocked: no valid rig/action source |
| Defend | `chaosx_paleogenetic_creature_defend` | blocked: no valid rig/action source |
| Support attack | `chaosx_paleogenetic_creature_support_attack` | blocked if the parent entity exposes this distinct state; no semantic alias is permitted |
| Retreat | `chaosx_paleogenetic_creature_retreat` | blocked: no valid rig/action source |
| Roar | `chaosx_paleogenetic_creature_roar` | blocked: no valid rig/action source |
| Wounded | `chaosx_paleogenetic_creature_wounded` | blocked: no valid rig/action source |
| Death | `chaosx_paleogenetic_creature_death` | blocked: no articulated collapse, impact, and settling source |

No Meshy animation call was made because every `meshy_animate` result would inherit the anatomically invalid completed rig. No Blender operation authored or replaced skeleton, weights, or motion.

## Geometry, material, export, and synchronization state

- Existing base geometry remains 29,999 triangles, 14,928 vertices, one substantive component, one UV layer, and calibrated to the recorded 7.3518242835 m source height with proposed entity scale 1.35 applied exactly once by the parent.
- The base candidate retains 59 boundary edges after bounded repair rollback. It is not promoted for export.
- Provider PBR maps remain immutable. No PDX diffuse/specular/normal DDS set was created in this recovery because the rig/action gate failed; raw roughness was not used as specular.
- No accepted weights exist. The rejected humanoid result's numeric normalized weights do not make its missing chains anatomically valid.
- No `.mesh`, `.anim`, export receipt, or reimport proof exists.
- No source-to-runtime copy occurred. The selected source GLB hash is retained as evidence only; destination hashes and synchronization receipts do not exist.

## Sourced audio verification

- Official source page: https://opengameart.org/content/monster-sound-effects-2
- Direct download: https://opengameart.org/sites/default/files/monster_sfx_pack_2.zip
- Title/creator: **Monster Sound Effects 2**, Ogrebane; published 2010-12-19.
- Stated license: CC0. The official page was rechecked on 2026-08-27 and describes 17 WAV files with monster/beast/creature, idle, attack, defend, hit, and death tags.
- Original ZIP: `audio/originals/monster_sfx_pack_2.zip`, SHA-256 `8D9831E5596446EBAFB8E6A958E757F07CBD385F9E417B4D9704D63A05A2CD63`.
- All 17 extracted originals rehashed to the values in `audio/sound_handoff.md` and re-probed as 44.1 kHz stereo signed 24-bit PCM. No derived audio exists.
- Exact selection, movement/contact, attack, impact, roar/special, wounded, and death selection remains blocked because sequential filenames contain no per-file semantics, this agent did not perform auditory approval, and valid action frames do not exist for synchronization.
- Proposed phase bindings remain evidence only: selection/idle at its exact consumer or state entry; move at planted contacts; attack/impact at visible contact; roar at the first open-mouth peak; death at body impact before settling silence.
- Parent owns the exact selection consumer, sound/soundeffect definitions, wrappers, runtime conversion after auditory approval, and live playback validation.

## Bespoke vanilla-green counter verification

- Required tokens: `GFX_unit_paleogenetic_creature_icon_medium` and `GFX_unit_paleogenetic_creature_icon_medium_white`.
- Proposed DDS paths: `gfx/interface/counters/divisions_large/unit_paleogenetic_creature_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_paleogenetic_creature_icon.dds`.
- Installed definition: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`.
- Installed large reference: `unit_infantry_icon.dds`, 152x42, two 76x42 frames, SHA-256 `B33A8E3B69CC789EB0E31BA99F4E5BA4E5B0A8B51EC1A7A7F709C3516F720C23`.
- Installed on-map reference: `onmap_unit_infantry_icon.dds`, 60x12, two 30x12 frames, SHA-256 `58AB78662C2A64A519B8D5D144582E7B2785915BD0A0A822696D87A9DE6F766C`.
- Large skill-local reference/contact sheet SHA-256: `CAF241717AF26CA1688742A86BE1A8A89C5A9B8CABA41410B4CF799827AD1972` / `CD7ABDF70B38498D03744990BA91BFFF808686B1E8891049B8A78AD58E9B4243`.
- On-map skill-local reference/contact sheet SHA-256: `5A6274E5847CBE9D030B547B9C2BB723215269B234BEF227A43F273B22DC42B9` / `23374FC38F26FC382DF60800C1086E074AC6BE46CDCD86B3EADDE686A99C8C26`.
- Verified large-counter palette evidence retains dominant opaque green RGB `73,106,73` with the documented muted shade ladder; the on-map token uses its inspected compact black/grayscale/white treatment.
- `counter_handoff.md` contains the original asymmetric two-headed/four-armed silhouette brief and exact consumer contract.
- Repository search found no Paleogenetic source PNG, processed PNG, DDS, contact sheet, manifest entry, or `chaosx_icon_artist` output. Counter production therefore remains `blocked pending bespoke icon-artist package`; a renamed/reused vanilla counter is not allowed.

## Files changed by this audit

- `.tools/3d_pipeline/reports/environment_report.json`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/job.yaml`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/manifest.md`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/history.jsonl`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/runtime/handoff.md`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/runtime/crosswalk.md`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/logs/adapter/57e98866b62b44bb8da0bd86053eb80c.json`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/logs/adapter/57e98866b62b44bb8da0bd86053eb80c.result.json`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/logs/adapter/fb386107938c496a9dcad2c0a8c36b84.json`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/logs/adapter/fb386107938c496a9dcad2c0a8c36b84.result.json`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/paleogenetic_creature_provider_recovery_audit_2026-08-27.md`

## Parent-owned remaining work

1. Keep this package blocked unless Meshy exposes a materially different compatible multi-limbed creature rig, or the user explicitly approves a licensed professional rig/action source after this provider-incapability record.
2. Do not animate the rejected humanoid rig and do not create a local replacement skeleton, weights, or motion.
3. Decide whether a distinct support-attack state is part of the final entity. If it is, require a distinct substantive provider/professional action rather than aliasing attack.
4. Route the recorded counter brief to `chaosx_icon_artist` and review its native-size contact sheet before runtime promotion.
5. Conduct an auditory approval pass for the CC0 pool, select exact role files, perform only documented mechanical conversion, and synchronize them only after valid actions exist.
6. Parent retains `.asset`, entity, `.gfx`, sound-definition, runtime copy, live-consumer, and in-game validation ownership.

## Simplifications, omissions, and blockers

- No simplification or fallback was used.
- Paid provider recovery was omitted by explicit parent instruction at 13 live credits.
- Provider animation, Blender action processing, PDX texture conversion, `.mesh`/`.anim` export/reimport, audio role selection/synchronization, bespoke counter production, runtime synchronization, and in-game validation remain blocked or parent-owned for the exact reasons above.
