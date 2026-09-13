# Event 016 temporal guard runtime closure — 2026-09-05

## Disposition and boundary

This handoff records the existing-geometry 3D closure tranche for `temporal_guard`. The preserved model, recovered 24-bone rig, materials, provider-derived actions, bounded action-phase recovery, grounded exports, actual-byte reimports, sourced audio package, and parent-reviewed counter package are evidenced below.

The 3D evidence tranche is implemented, but the asset is not claimed to be live in-game complete. Parent-owned entity/GFX/action binding, temporal particle/light consumers, sound/soundeffect/wrapper wiring, runtime file placement, and live consumer validation remain open. The bounded phase-recovery reports intentionally retain `semantic_acceptance: false` and `runtime_acceptance: false` for parent review.

No geometry was regenerated, substituted, remeshed, re-rigged, or replaced in this closure. No gameplay, entity, GFX, sound definition, localisation, spreadsheet, GUI, or unrelated documentation file was edited. No action was aliased, made static, reduced to a whole-rig transform, or authored through a generic procedural generator. Nothing was staged or committed.

## Job inputs and accepted recovery plan

Job root: `docs/assets/chaos_redux_3d_model_pilots/models_3d/temporal_guard`.

Primary existing-geometry input: `blender/checkpoints/03_rig_approved.blend`, 3,639,713 bytes, SHA-256 `E9D2C8B100A5764231CC2F3793B7D3A2C907763FEDD45C999B6039640129BD49`.

The source and recovery records consulted were `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/temporal_guard_meshy7_handoff_2026-08-27.md` and `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/2026-08-27_manual_existing_mesh_rig_recovery_final.md`. The accepted bounded manual phase-recovery contract is described in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_action_phase_patch_adapter_2026-09-02.md`.

The accepted route retained provider-derived `attack` and `move` motion, cloned each source into a unique target action, and changed only explicit local quaternion phase channels through the locked `patch_existing_humanoid_action_phases` adapter operation. Grounding then changed only the existing `Hips` root location channel per frame. This is the authorized recovery exception for the two absent dedicated provider roles; it is not a general local-animation fallback.

## Locked environment and route evidence

The required credential gate passed before repository intake; the secret was never printed or persisted. No new Meshy call was made in this closure tranche and no new provider credits were consumed. Historical Meshy lineage, task IDs, and prior planned cost remain in the dated Meshy 7 handoff and provider receipts.

The lock files and exact SHA-256 evidence used here are:

| Item | Locked value | Evidence SHA-256 |
| --- | --- | --- |
| Official Meshy MCP | `@meshy-ai/meshy-mcp-server` `0.4.0`, git `d8c77d1cb897e345eb41d38b510b8391b1664346`, compatibility `meshy-7-v5`, exact model `meshy-7` | `.tools/3d_pipeline/config/dependencies.lock.json`, `B68663B74AA51CD3D191AA98C0EB0BD2E7C3612E238B87D7867C923093C1EA92` |
| Meshy live schema | schema `1.0.0`, revision `meshy-7-compat-live-declaration-2026-08-21`, SDK `1.29.0` | `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`, `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233` |
| Blender | `5.1.2`, build `ec6e62d40fa9`, `C:/Program Files/Blender Foundation/Blender 5.1/blender.exe` | dependency lock |
| HOI4 adapter | `chaosx_blender_hoi4` `1.10.21`; adapter config SHA `C68298F02A04084F9A0EF48196BE7AE4806EE746D9C7A290A3C27F3D202EA6FC` | `.tools/3d_pipeline/config/blender_hoi4_adapter.json` |
| PDX extension | `io_pdx_mesh` `0.91.0`, archive SHA `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2` | installed manifest SHA `C6865CEB3CE323BD54255BB37FF860E03607BD2AABED4057E9DCBE04C29682EC` |
| Environment report | adapter/Blender/io_pdx probes returned no findings | `.tools/3d_pipeline/reports/environment_report.json`, SHA `D4EF0EA91B6F3FFB50A2176EFB08FF988B7337AC7EF171A19063B873324F56F3` |

The repository-owned bridge was separately probed at `127.0.0.1:9876` and was listening. Adapter health request `d344c3f726bc46bc8437a46d872b29e6` reported Blender `5.1.2`, adapter `1.10.21`, and all required io_pdx operations. All Blender inspection, mutation, export, grounding, and reimport calls used the allowlisted adapter route.

Important closure request IDs are retained in `logs/adapter/`:

- Attack transfer `44b91d8b65424942a076a92d0d6af68d`; attack weight-only sanitization `0964354ccc16405d987022c0bc26c0e0`.
- Support phase patch `8b704bea69b14abd90b1b1d81a020164`; support grounding `3393ac673dd0406c91ec6a06b5a54ec1`; support export `b1c306f3280048e4baaceb9edd25988b`; support channel inspection `bfbd6d534b154eff94c547cfa6ce65e6`; support grounded reimport `3876d8644df043ae914c63023028878d`.
- Move transfer `5d393ca3e21c439ebe5b9ad878609e46`; move weight-only sanitization `60c81a2c5bc94051aedd1195255d0425`.
- Retreat phase patch `3cbd656e8ee94e379c191a579cbd0f23`; retreat grounding `90f2ac1828e4421e935fe53a9fe8606b`; retreat export `477e27ed232b4d24816336f4f10acd70`; retreat channel inspection `fee741a6eee4435694a6f78d816dab1e`; retreat grounded reimport `c2a2720f101a49b587ba6a198412630b`.
- The phase result hashes are `logs/adapter/8b704bea69b14abd90b1b1d81a020164.result.json` SHA `BB02C23C7FEB01CBBB65ADAC94AC5D1E555DE419A3C3CEF766298820F11B3EEC` and `logs/adapter/3cbd656e8ee94e379c191a579cbd0f23.result.json` SHA `611C4BFE30A4530B852F7EFF1D2500BD86FD4B5139C24595551193F24E2CB58C`.

## Provider lineage and action verification

The eight existing actions were checked against the existing provider receipts, actual exported bytes, and prior parser/reimport evidence rather than accepted from filenames alone. Their provider lineage is:

| Role | Meshy action/task lineage | Native range/FPS | Existing runtime `.anim` SHA-256 |
| --- | --- | --- | --- |
| `idle` | provider action `0 Idle`, task `01a04288-d5d7-777b-ac48-eb6ae717a2b1` | 1–97 / 24 | `C2BE045CF4079A647E012EFF8145B07CFE69CF3018E9F616FC898E90EF603563` |
| `move` | rig-included walking, task `01a04284-b375-7973-909c-8abd29417e11` | 1–32 / 24 existing export; recovered source transfer for `retreat` is 30 FPS | `E3839142F49EA48A5182DB4145CAF04A462EAFEE9ABB8F39B42FF53DE947DAE4` |
| `attack` | provider action `198 Punch_Combo`, task `01a04288-ea5c-788f-ac52-ea205f248456` | 1–60 / 24 | `F22DF39A34FADEF4ECA718102E966EA7AC704E3B3D89244D715D619CE406B3DF` |
| `defend` | provider action `138 Block1`, task `01a04288-e297-7a72-ace5-2bcc301fa63b` | 1–84 / 24 | `F468CB8B13041D18FC8D894557F82E70E3E31B79E0D15B2C53EBABC582655128` |
| `entrain` | provider action `89 Combat_Stance`, task `01a04288-ee21-789c-a0e0-ec81633d2d6a` | 1–40 / 24 | `E130DDEF7FD1650C6D62E44F496F44CAF89784BF3575AA402306AD55AD6D7FEE` |
| `death` | provider action `184 Shot_and_Fall_Forward`, task `01a04288-da2e-7e21-b11d-47325b6d390f` | 1–53 / 24 | `409714D9C162A0A2C072781327BBA73869021BC5CAA115A732EBFDCFE4494133` |
| `temporal_anchor` | provider action `125 Charged_Spell_Cast`, task `01a04288-de40-777f-be17-dd4e11ce44fc` | 1–65 / 24 | `CF35348B9AE481D606240EFCA2722ACBB5CDACB4F5A858FBACAC4A37F28A715A` |
| `synchronization` | provider action `126 Charged_Spell_Cast_1`, task `01a04288-e67c-7a73-aa64-95c67a8b27d7` | 1–104 / 24 | `1DE85573412CE3A4A121AC6D4B6A5178EC308B3B37FD1FF1F4047E61B331624B` |

The existing parser/reimport reports retain `io_pdx_rigAction`, a 24-bone armature, quaternion/location channels, sampled frame bounds, grounded contacts, and the PDX material. Existing action names are not being reused to fill the two missing roles.

The corrected provider receipts added or corrected for this tranche are:

- `provider/tasks/receipts/attack_runtime_corrected.json`, SHA `DCA6757D85AA09467FD57EFDEFA74A865020DC0ED5A4DC3BE9E07E6F1F35C49C`. Exact source action `Armature|Armature|Armature|Armature|Armature|Punch_Combo|baselayer`, provider reference `01a04288-ea5c-788f-ac52-ea205f248456`, source FBX `provider/downloads/animations/attack/attack_24fps.fbx`, source SHA `31C752CC1D772E33C4CF0B8FCBBC010825D87980ACA99AFC38C738EB2FF68621`.
- `provider/tasks/receipts/move_runtime_corrected.json`, SHA `0B0BCFD62BFC0B4FE6168709A0EA9313B27BFD17EF71C46643C785CDEB960798`. Exact source action `Armature|Armature|Armature|walking_man|baselayer`, provider reference `01a04284-b375-7973-909c-8abd29417e11`, source FBX `provider/downloads/rig_01a04284/walking.fbx`, source SHA `F6F8C4EAD6340F5A6458B3AA244C22595CCC8B3E376D2F4181E5789A5528D918`.

## Distinct `support_attack` and `retreat` evidence

### `support_attack`

The source was the verified provider-derived `chaosx_temporal_guard_attack` action. The phase adapter cloned it to `chaosx_temporal_guard_support_attack` with source action native hash `954D55549C7A86DB36A212A494DA4810DDC715BEDAB1029C1CB883CE6EB1D504`. The patch report records source checkpoint SHA `E9D017B8D59D3FFDBD5C7297FD458A696D91793845465F95C1553F524358CD5A`, target pre-ground native action hash `5AF3B01988B8DF1E7A5785B3D5D24E5AD03AB117EA70947E44B96303C99741F2`, target record hash `510F1D24CCFA9FE0129B57A77D8AC87CD5951CF9E4366091E9E799A9034BBC3E`, and exact reopen comparison acceptance with no mismatches.

The action runs at 24 FPS over frames 1–60 with phase frames `ready=1`, `aim=12`, `discharge=24`, `recoil=36`, and `recovery=60`. It has 168 f-curves and 65 explicit quaternion vector keys across 13 non-root and upper-body bones: `Spine`, `Spine01`, `Spine02`, `neck`, `Head`, `LeftShoulder`, `LeftArm`, `LeftForeArm`, `LeftHand`, `RightShoulder`, `RightArm`, `RightForeArm`, and `RightHand`. All declared phase transitions have nonzero articulated basis deltas, including maximum deltas of 1.1643503 on `LeftArm`, 1.0946063 on `RightArm`, and 1.0620743 on `LeftForeArm`. The report records `manual_or_procedural_replacement_authored=true`, `procedural_generator_used=false`, `new_provider_call=false`, and `original_actions_unchanged=true`.

The grounded final checkpoint is `blender/checkpoints/runtime_support_attack_grounded.blend`, 2,417,253 bytes, SHA `52BE347032FBF23F1AC9B5D08F4642C41853CCFECCA389E0AD42C62AE1F7ABF2`. Final read-only channel inspection returned native action SHA `B0EE1CB59C789A393F644B7180B904EC4A061357F545E4946CEC90C9E5D831A8`, integrity SHA `B13D991A8CAC81F40BD5AC92E19813FF91D4168C24A39E920EE1C34224D00E20`, 168 rows, `io_pdx_rig`, quaternion rotation mode, and no new provider call.

The grounding report `blender/reports/correct_action_grounding_chaosx_temporal_guard_support_attack.json` records only the `Hips` root location channel corrected across 60 frames, body motion retained, 168 curves before and after, and post-correction contacts from `-9.5693e-7` to `+7.3458e-7` source units. Its SHA is `07522C83422BBDF3529577144A5885767ABCFC4325B295D4376203065A10A3D6`.

The final export is `export/anim/chaosx_temporal_guard_support_attack_grounded.anim`, 48,211 bytes, SHA `5591274702F3A998ED02F281CBCF975A405C320DCF0E532358289B5589BBB917`. The io_pdx export report has FPS 24, frames 1–60, armature scale `[1,1,1]`, zero scale/translation normalization changes, and no warnings. Actual-byte reimport request `3876d8644df043ae914c63023028878d` wrote `validation/reimport_reimport_runtime_support_attack_grounded_actual.json`, SHA `3196F4CC78A659CE83817660A7A06AC069D7985AB56EFE3B850BB939083A091A`, and proof blend `blender/checkpoints/reimport_reimport_runtime_support_attack_grounded_actual.blend`, SHA `662B1D4FB6CF58529E70DB931349A05D0DE0932261AA22A702B461E1CF45A2A1`. The reimport contains 24 bones, action `io_pdx_rigAction`, 30,000 polygons, 38,906 seam-split vertices, `PDXmat_char1.002`, and sampled contacts at frames 1/16/30/45/60 of approximately `-1.5851e-6` to `+1.0873e-6` metres.

### `retreat`

The source was the verified provider-derived `chaosx_temporal_guard_move` action. The phase adapter cloned it to `chaosx_temporal_guard_retreat` with source action native hash `92D3321A31DDDD3E7D348CD66AE00124A6D784F6199FDEDDB006F566635BAA41`. The patch report records source checkpoint SHA `91E3E20D3AD0270A62D043091C48C48FD0DFFD1895B2D6690105E9F330916949`, target pre-ground native action hash `086F862ADA57A7459CC7FDABB1B68C5DCF51B206A58C8733CE9F0B9BE99963D4`, target record hash `6D27A7951C914EAFBEA7B7F57EC0234B7A39D8B9B9E36FD0AC4BE435E126814B`, and exact reopen comparison acceptance with no mismatches.

The action runs at 30 FPS over frames 1–32 with phase frames `disengage=1`, `withdrawal=14`, and `recovery=32`. It has 168 f-curves and 42 explicit quaternion vector keys across 14 bones. The required contiguous non-root motion chain is `LeftUpLeg -> LeftLeg -> LeftFoot`; all chain members have genuinely changed local channels at a named phase. Additional articulated changes cover `RightUpLeg`, `RightLeg`, `RightFoot`, `Spine`, `Spine01`, `Spine02`, both arms, forearms, and `Head`. Maximum reported deltas include 1.3639424 on `RightLeg`, 0.7898860 on `LeftLeg`, and 0.6373554 on `RightArm`. The report records `manual_or_procedural_replacement_authored=true`, `procedural_generator_used=false`, `new_provider_call=false`, and `original_actions_unchanged=true`.

The grounded final checkpoint is `blender/checkpoints/runtime_retreat_grounded.blend`, 2,397,559 bytes, SHA `278E729370459FDDBCED8A3B5D69017329B0C890E1B0F715A056FC2B1D1DBF22`. Final read-only channel inspection returned native action SHA `4E109FC00D3E42FD14D8E17E39829DB72C87546861A5E78D400E82897AA94DE6`, integrity SHA `776F66C535A2E57ABD1B4BBD54A3E746B295261D4787C352BE8EA9115D7033BD`, 168 rows, `io_pdx_rig`, quaternion rotation mode, and no new provider call.

The grounding report `blender/reports/correct_action_grounding_chaosx_temporal_guard_retreat.json` records only the `Hips` root location channel corrected across 32 frames, body motion retained, 168 curves before and after, and post-correction contacts from `-4.4145e-7` to `+3.6508e-7` source units. Its SHA is `C86D58B428B472A11457AA3CC4C37553FAAC8F7A4B12286EBEF2DC67D28208C8`.

The final export is `export/anim/chaosx_temporal_guard_retreat_grounded.anim`, 26,707 bytes, SHA `03CE8BC9EF27671CCF9323422A26841C2A058A739D6CF23A3309AA802425A972`. The io_pdx export report has FPS 30, frames 1–32, armature scale `[1,1,1]`, zero scale/translation normalization changes, and no warnings. Actual-byte reimport request `c2a2720f101a49b587ba6a198412630b` wrote `validation/reimport_runtime_retreat_grounded_actual.json`, SHA `956221E43A6D5B3B61253E1DB5DCB32430FE6711CB986A735E4D5B1D99EB4789`, and proof blend `blender/checkpoints/reimport_runtime_retreat_grounded_actual.blend`, SHA `0847AB55408E13E055FB8F6D5CEE9BEEF6FAF7F036835C70115CE58AA765513C`. The reimport contains 24 bones, action `io_pdx_rigAction`, 30,000 polygons, 38,906 seam-split vertices, `PDXmat_char1.002`, and sampled contacts at frames 1/9/16/24/32 of approximately `-6.0350e-7` to `+2.1725e-6` metres.

## Geometry, bind/rest pose, weights, scale, and materials

The provider geometry and recovered 24-bone rig were retained. The weight-only runtime sanitation request `60c81a2c5bc94051aedd1195255d0425` and its report `blender/reports/weights_sanitized.json` preserved geometry and rest bones while removing only excess influences. The final mesh has 14,997 position-welded source vertices, 30,000 triangles, 38,906 exported seam-split vertices, dimensions `5.8751373 x 1.6126238 x 7.3518243`, zero degenerate faces, zero non-manifold edges, and 38 diagnostic loose boundary edges in ten closed components after position-weld inspection.

The sanitized deforming mesh has zero zero-weight vertices, normalized weights, and a maximum of four influences per vertex. Its influence histogram is 1:2,624, 2:5,841, 3:2,831, and 4:3,701 on the base sanitized copy; the transferred sanitized copies retain the same max-four normalized contract. The original approved checkpoint had 2,297 over-four vertices; those were repaired by the bounded weight-only sanitation step, not by geometry substitution.

The working armature is `io_pdx_rig` with 24 bones. Bind/rest-pose data and bone count were preserved through transfer, phase patch, grounding, export, and reimport. Armature and mesh world scales are `[1,1,1]`; the export reports show no scale or translation normalization changes. Vanilla calibration remains the installed `western_european_infantry.mesh` precedent with `+Z` up, `-Y` forward, source height `7.351824797689915`, entity scale `0.8`, and effective runtime height `5.881459838151932`. The temporal guard source geometry height is `7.3518242835998535`, giving the calibrated effective height `5.881459426879883` after the parent applies the entity scale exactly once.

The selected PDX material is `PDXmat_char1.002`. The relinked runtime DDS channels remain `textures/dds/texture_0.dds` SHA `82071750202D2435542841E8354313DDB4B46BFD4B23CEBA0308CE4DE6DB4044`, `textures/dds/texture_normal.dds` SHA `508EF722D43C7E09E4BECB753AA88923B89BDE8734F8C0EF5F07B83ABA1AA30F`, and `textures/dds/texture_specular.dds` SHA `DBFD8E36D649BFD7B75E371DA6B133E7EC7B31874A370CF815327542247BD37B`. Actual-byte reimports staged these three files without copying because the job-relative staged bytes were already hash-identical.

## Mesh export and actual-byte reimport

The accepted canonical mesh remains `export/mesh/chaosx_temporal_guard.mesh`, 3,475,175 bytes, SHA `EA0C72AAC11CDA1B1A46CF74C6DC6A38EF3DC9833EC35DFE984E82D7FFD59516`. It was exported through the locked io_pdx route and has prior mesh/material and eight-action parser/reimport evidence. A fresh clean mesh export attempt from the promoted checkpoint was intentionally not promoted: request `eb82a3f77fb443619c3fd951894c89d3` reached the io_pdx stream guard with 90,000 vertices in stream 0, over the 65,535 limit, despite 30,000 triangles. The existing accepted canonical mesh was retained rather than changing geometry or substituting a regenerated asset.

Both new grounded actions were reimported against that exact canonical mesh. The actual-byte reports retain the 24-bone armature, `io_pdx_rigAction`, 30,000 polygons, material `PDXmat_char1.002`, one `map1` UV layer, zero degenerate faces, zero non-manifold edges, zero-length normals, and three-view previews at the role-specific sample frames. The reimport proof blends and validation reports are listed in the action sections above.

## Proposed entity and action mapping

The parent-owned consumer is `common/units/016_brilliant_scientist_project_forces.txt#temporal_guard`. Proposed stable identifiers are:

| Runtime role | Proposed action identifier | Source/evidence |
| --- | --- | --- |
| idle | `chaosx_temporal_guard_idle` | existing provider action 0 |
| move | `chaosx_temporal_guard_move` | existing provider walking action |
| attack | `chaosx_temporal_guard_attack` | existing provider `Punch_Combo` |
| support attack | `chaosx_temporal_guard_support_attack` | grounded bounded phase recovery above |
| defend | `chaosx_temporal_guard_defend` | existing provider `Block1` |
| entrain | `chaosx_temporal_guard_entrain` | existing provider `Combat_Stance` |
| death | `chaosx_temporal_guard_death` | existing provider `Shot_and_Fall_Forward` |
| temporal anchor | `chaosx_temporal_guard_temporal_anchor` | existing provider charged-cast action |
| synchronization | `chaosx_temporal_guard_synchronization` | existing provider distinct charged-cast action |
| retreat | `chaosx_temporal_guard_retreat` | grounded bounded phase recovery above |

Proposed entity and mesh identifiers are `chaosx_temporal_guard_entity` and `chaosx_temporal_guard_mesh`. The current repository inventory found no active 3D entity/model consumer for `temporal_guard`, so these identifiers are handoff proposals and are not claimed as wired.

The `temporal_anchor` and `synchronization` actions are verified articulated source actions, but no active entity-side particle/light consumer was present for this subtask. The parent must bind the exact temporal particle and light effect identifiers to the corresponding action phases and verify them in the entity consumer. No guessed effect token is recorded here.

## Sourced audio and synchronization handoff

The existing package is retained under `audio/originals/`, `audio/derived/`, and `audio/provenance.md`. All derived candidates are mechanical transforms of licensed originals, not generated or manually authored audio. The provenance file records the source pages, direct files, creators, terms, retrieval evidence, checksums, and transformations.

| Role | Source and terms | Original SHA-256 | Derived candidate and SHA-256 | Proposed sync |
| --- | --- | --- | --- | --- |
| selection/idle ambient | `https://commons.wikimedia.org/wiki/File:60Hz_hum_square.ogg`, BPK, public-domain dedication | `A4230848B204D806671A4EF858626013DC66C8CA57F941AB979A6118740BA7CA` | `audio/derived/chaosx_temporal_guard_selection_idle_ambient.wav`, `19242D45E5AFB50CD85CA3C112BF255B183754F2D18CBC699788C1CEF4446EAB` | selection start; idle loop after parent loop-point review |
| move | `https://commons.wikimedia.org/wiki/File:ZapSibAudio-Steps.ogg`, MaksimPinigin, CC BY-SA 4.0 | `BE1BA9D77C6D6ADF5630BAFCB8CF88E092DC0BD0575DEB25364B8AC2A2346ACE` | `audio/derived/chaosx_temporal_guard_move.wav`, `28113D0850B1FD13C2696FF215AC0FDF66F06C512062C68D6D2A68D30F55BE07` | grounded walk contacts around frames 1/16 and 16/32 |
| attack/contact | `https://commons.wikimedia.org/wiki/File:Metal_Clanging_Noises.ogg`, Camshaft64, CC BY-SA 4.0 | `B3F1A16F5DDA28D20C8B16689050647478812D92EE3C06A66EC4A425A85BB408` | `audio/derived/chaosx_temporal_guard_attack_contact.wav`, `307922722E6F2C1E19B778B5B5EE473B03C6AFB46457DA9C310CC76C865B0C8E` | support/attack contact candidate near attack frame 30 |
| impact | `https://commons.wikimedia.org/wiki/File:Dropmetalthing.ogg`, Secretlondon, package elects CC BY-SA 3.0 | `ED01D6F0AC2183580572D02CE63E61592CE8670645F1508B607793F913D20822` | `audio/derived/chaosx_temporal_guard_impact.wav`, `EF4A4CCBB6D9EF9025AFD09580690FC2C950DBE5A8E0198F573466A85E311860` | defend/received impact or attack contact after parent review |
| temporal special | `https://commons.wikimedia.org/wiki/File:Aggressive_electric_buzzing.ogg`, stephan, public-domain release | `5B6DEBCA8737418009BC5A098BA68DE2998E8E971ED0CD3D42C7DCA43A2B1819` | `audio/derived/chaosx_temporal_guard_temporal_special.wav`, `C38BCD38F24F82596A8D504EE0F03B58D4F76C979844EBCBADBC25B64BB7AE62` | temporal anchor frame 44 and synchronization frame 52 candidates |
| death | same Camshaft64 original, CC BY-SA 4.0 | same `B3F1A16F5DDA28D20C8B16689050647478812D92EE3C06A66EC4A425A85BB408` | `audio/derived/chaosx_temporal_guard_death.wav`, `6E113CAB0E712B886EFD60537BC5CCABF6B936144F95FC9AD7B9DE2154CE3FAD` | death impact frame 36 and settling tail through frame 53 |

Stable proposed sound IDs are `chaosx_temporal_guard_selection`, `chaosx_temporal_guard_ambient_loop`, `chaosx_temporal_guard_move`, `chaosx_temporal_guard_attack_contact`, `chaosx_temporal_guard_impact`, `chaosx_temporal_guard_temporal_special`, and `chaosx_temporal_guard_death`. The parent owns exact sound, soundeffect, wrapper, attribution, and runtime consumer wiring.

## Bespoke vanilla-green counter handoff

The parent-reviewed counter package is retained and was not changed in this tranche. Its handoff is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_generic_counter_completion_2026-09-01.md`, with icon-artist boundary evidence in `counters/gfx_handoff.md`.

The exact installed-vanilla definition is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`. The matching land references use `noOfFrames = 2`, large canvas `152x42` with `76x42` frames, and on-map canvas `60x12` with `30x12` frames. The inspected green palette is the muted vanilla infantry family, including samples around RGB `(72,104,72)`, `(73,106,73)`, and `(181,197,181)`.

Final temporal counter outputs are:

- `gfx/interface/counters/divisions_large/unit_temporal_guard_icon.dds`, 152x42, 25,664 bytes, SHA `50622212016AC090ADD2D076E3E0B40896B932BCDA6A124083D0B1D0DDBF7C78`.
- `gfx/interface/counters/divisions_small/onmap_unit_temporal_guard_icon.dds`, 60x12, 3,008 bytes, SHA `995FF164E56AC3BBA23315203EBFA8D72CBCCF92D74F66485D718BA42BAFF8D7`.

Parent-owned sprite tokens are `GFX_group_temporal_guard_icon`, `GFX_unit_temporal_guard_icon_medium`, and `GFX_unit_temporal_guard_icon_medium_white`, with the land-unit consumer `temporal_guard`. No vanilla counter was reused or renamed as final art.

## Files created or changed in this closure

The following job-local files were created or updated by the production operations and evidence work. Adapter request and result logs are retained under the job-local `logs/adapter/` directory.

- Corrected provenance receipts: `provider/tasks/receipts/attack_runtime_corrected.json` and `provider/tasks/receipts/move_runtime_corrected.json`.
- Transfer/sanitization checkpoints: `blender/checkpoints/runtime_attack_transferred.blend`, `runtime_attack_transferred_sanitized.blend`, `runtime_move_transferred.blend`, and `runtime_move_transferred_sanitized.blend`.
- Distinct-action checkpoints: `blender/checkpoints/runtime_support_attack_phased_clean.blend`, `runtime_support_attack_grounded.blend`, `runtime_retreat_phased.blend`, and `runtime_retreat_grounded.blend`.
- Actual-byte proof checkpoints: `blender/checkpoints/reimport_reimport_runtime_support_attack_grounded_actual.blend` and `blender/checkpoints/reimport_runtime_retreat_grounded_actual.blend`.
- Final grounded animation files and parser text: `export/anim/chaosx_temporal_guard_support_attack_grounded.anim`, its `.txt`, `export/anim/chaosx_temporal_guard_retreat_grounded.anim`, and its `.txt`.
- Verification reports: `blender/reports/weights_sanitized.json`, `blender/reports/correct_action_grounding_chaosx_temporal_guard_support_attack.json`, `blender/reports/correct_action_grounding_chaosx_temporal_guard_retreat.json`, `blender/reports/export_anim_chaosx_temporal_guard_support_attack.json`, `blender/reports/export_anim_chaosx_temporal_guard_retreat.json`, `validation/reimport_reimport_runtime_support_attack_grounded_actual.json`, and `validation/reimport_runtime_retreat_grounded_actual.json`.
- This handoff file.

The accepted canonical mesh and existing eight action exports were preserved, not replaced. Existing audio, counter, runtime, and gameplay files outside the job evidence root were not edited.

## Validation completed and intentionally skipped

Completed validation includes the hard credential gate, dependency/schema/adapter lock review, separate socket probe, adapter health, source-receipt byte checks, geometry and topology audit, max-four normalized weight sanitation, bind/rest-pose and 24-bone preservation, vanilla height/axis calibration, material/DDS relink evidence, provider-action transfer, exact action-channel inspection, explicit multi-phase difference checks, per-frame root-contact correction, io_pdx animation export, canonical mesh reuse after the fresh stream-cap failure, and actual-byte reimport with hashes and multi-view previews.

The following meaningful validations remain parent-owned or blocked: semantic parent acceptance of the bounded phase-recovered roles; exact entity `.asset` and unit consumer wiring; temporal particle/light consumer identifiers and timing; sound/soundeffect/wrapper installation and live synchronization; runtime copy synchronization into active `gfx/models/` paths; installed counter consumer review in the live UI; source-art/ImageGen authorization and full prior credit reconciliation; and live HOI4 validation. HOI4 was not launched.

## Remaining risks and blockers

- The phase adapter proves distinct articulated motion and exact native preservation, but its own reports correctly do not make semantic or runtime acceptance claims. Parent review must confirm that `support_attack` reads as supporting contact/attack motion and `retreat` reads as withdrawal in the live entity context.
- The grounded support action's final native hash is `B0EE1CB59C789A393F644B7180B904EC4A061357F545E4946CEC90C9E5D831A8`, and the grounded retreat action's final native hash is `4E109FC00D3E42FD14D8E17E39829DB72C87546861A5E78D400E82897AA94DE6`. These final hashes supersede the pre-ground phase-patch hashes for runtime selection.
- The fresh clean mesh export remains blocked by the io_pdx 65,535 stream-vertex guard at 90,000 vertices. The approved canonical mesh remains the runtime mesh; no geometry fallback was used.
- The dated Meshy 7 source-art record still carries the previously documented missing URL/title/terms/authorization/ImageGen-response evidence and incomplete historical credit reconciliation. This closure did not invent or silently repair those records.
- The repository inventory still has no active temporal guard 3D entity/model consumer. Parent must wire the proposed entity and all ten action identifiers without aliasing the new roles.
- Temporal particle/light consumers are not present in the current entity surface. Parent must identify exact effect tokens and synchronize them to `temporal_anchor`/`synchronization` phases.
- The sourced audio and bespoke counter packages exist with provenance and checksums, but parent owns final runtime installation, attribution, consumer mapping, and live validation.

No simplification was substituted for the requested existing-geometry closure. The only exception is the explicitly accepted bounded manual phase recovery, which preserves provider body motion, changes declared local channels only, and is clearly marked for parent semantic review.
