# Pack-donkey rig, cargo and action integration

Status: requested 3D repair implemented; inherited counter identity and audio-source archive gaps remain explicit.
The user authorized GPT-6-astra Blender repair of faulty existing rigs/actions and automatic completion of missing physical components.
The accepted 25-bone pack-donkey body has 24,880 triangles plus a 120-triangle hinged wooden cargo closure.
Selected editable source remains checkpoint16, SHA B4E16129CA828C644ABF0077C4CA2B5F577EBAE21D560FCF8439A44B3A06E020.

Nine exact payloads are installed in gfx/models/units/012_africa_plague_carriers/.
The four material streams are mesh.001 indices0/1 (21,845/3,035 triangles), plague_carriers_cargo_hatch_frame index0 (72) and plague_carriers_cargo_hatch index0 (48).
All use texture_0.dds, texture_normal.dds and the selected gloss-packed texture_specular.dds with PdxMeshAdvanced.
The existing plague_carriers_entity uses scale1.0 once and retains all five animation registry IDs.
Only this unit's blocks changed in the shared Africa entity files after the Gorilla integration commit.
Death is terminal; idle/move loop, and the other actions return to idle.

The five actual-byte reimports retain all25bones,25,000triangles, correct facing and distinct idle/walk/cargo/death actions.
The source yaw proof covered305frames with maximum vertex error8.5963e-7.
A confirmed exporter mismatch originally dropped constant rig-world yaw from the initial animation root.
Release1.10.40 corrects only initial root translation/quaternion using the same locked world-space conversion as samples; child/sample payload and serialized readback checks pass.
All five corrected exported animations passed native reimport; rejected pre-fix files are excluded.
Parent reviewed final death81left/quarter and accepted the articulated side collapse and cargo support.
Actual death support places pack_L atZ.0009994507 and hanging_basket atZ.0120003223.
The wooden closure opens68degrees atframes29–35 and closes by53.

Seven registered sourced WAVs are PCM16 mono44.1kHz with documented trim/fade recipes and zero clipping.
Idle/training use a state-entry accent; movement/retreat cue at.333333; cargo-settle cues at1.4; hatch-opening at.933333 and hatch-closing impact at1.733333; death at1.333333seconds.
Selected cue durations fit their role windows without overlapping the next movement cycle or hatch-closing phase.
These are inherited equipment/vocal sources, not claims of species-accurate donkey calls or hoof recordings.
Source evidence and exact copies: docs/assets/012_africa/models_3d/plague_carriers/validation/plague_carriers_blender_repair_20260906/final_runtime_copy_manifest.json and audio/final/20260908_synced_pcm16/copy_manifest.json.
Independent runtime audit is 2026-09-08_donkey_runtime_audit.md.
The audit passed all sixteen payload hashes, five action chains, four material streams and eleven cue windows.
The existing plague-carrier spawn branch calls `chaosx_plague_carriers_select_sfx` in `common/scripted_effects/012_africa_action_effects.txt`; this is a spawn cue rather than a generic unit-selection callback.

## Verified runtime payloads

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `gfx/models/units/012_africa_plague_carriers/chaosx_plague_carrier_death.anim` | 64438 | `D8B61ECBF3712DC483CB5E9970297C54F815BF7BC995A642B077C8C8B27B3D10` |
| `gfx/models/units/012_africa_plague_carriers/chaosx_plague_carrier_deploy.anim` | 44923 | `7AC50DEA1EE533C96F28F142AF4E5F8AB97C66E3F9110005EB207E562E2CE063` |
| `gfx/models/units/012_africa_plague_carriers/chaosx_plague_carrier_idle.anim` | 12422 | `FA0606B675F48F46D041D8DECEE8B6D7120CB15CC4DD31E84E7B4F9FF58BBAF3` |
| `gfx/models/units/012_africa_plague_carriers/chaosx_plague_carrier_move.anim` | 30923 | `0BE90261BDFBB4949EBBD17A1B4142DD1478C87A9F3D5E0DD65551F12CF65B46` |
| `gfx/models/units/012_africa_plague_carriers/chaosx_plague_carrier_release_containment.anim` | 44923 | `0EAE6E35D86487AB39DEE7D568DA700DEAD3C287EDD60C460D39E6CC7A191527` |
| `gfx/models/units/012_africa_plague_carriers/chaosx_plague_carriers.mesh` | 2091186 | `EAE6702AB88559A6F9194939DE91C63AF2AF1CC95E37DD0DF15642920982B2CF` |
| `gfx/models/units/012_africa_plague_carriers/texture_0.dds` | 4194432 | `082B9E3B57BE4396B23E8716BE03393ABEFDC1604C84BFB7EF070AF46568758A` |
| `gfx/models/units/012_africa_plague_carriers/texture_normal.dds` | 4194432 | `059B71BCABEDF1F8F49BCE4005B687FFB05F7DE948FB5E806E3070F060E48074` |
| `gfx/models/units/012_africa_plague_carriers/texture_specular.dds` | 4194432 | `764862278C87C3E866808A824C6DB2EE826E889B851E1F04DAF46B8E61C94344` |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_select.wav` | 141198 | `BCCE79F413EF09980760B29D8609510F7F5A4178FC914E6F624660255770AF6D` |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_idle.wav` | 176478 | `07A17640CE9623603F7B619195F731BA337210A3E01DF277DCB864432E85BCB2` |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_move.wav` | 88278 | `F2DE930650CB0C69AC18655B69A0691296990FB42E79B4171B090A00059E1190` |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_deploy.wav` | 52998 | `16F30D575A1E9BBA3830C697DA8C52CB7CADA9E2BC52BA518AF13FCE3C588378` |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_release_containment.wav` | 67698 | `BFCF0F3B4AC1C223C0796A70D0FC6B2C697D08E25D0F7445EA47E14235228A87` |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_impact.wav` | 23598 | `54D89B852702DCEC97796DDC69D6FB2B30BADC584049256916E55044AA7A3407` |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_death.wav` | 117678 | `BF2D33AD765776C9A74F9C0148C3F15C55C37E169B8C537C347E38647D971C46` |

## Simplifications, omissions, and blockers

No required 3D component or authored action was omitted.
The inherited counter depicts an armored creature rather than this pack donkey and remains unresolved.
Three historical original audio downloads remain absent; existing derivative hashes, source URLs, creator/license records and new mechanical conversion evidence are retained.
Auditory suitability is unverified.
The source and unmerged exported topology are closed; a diagnostic position-only weld merges coincident separate frame timbers and reports four nonmanifold edges, so that diagnostic does not describe the shipping connectivity.
No new provider calls or credits were used for this model repair, and no live-game result is claimed.
