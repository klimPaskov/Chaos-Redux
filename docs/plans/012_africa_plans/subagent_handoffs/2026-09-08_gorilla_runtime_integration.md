# Gorilla hammer rig and action integration

Status: requested 3D repair implemented; inherited companion limitations remain explicit.
The user explicitly requested a Blender-modeled hammer and hammer attack, all missing components, and direct GPT-6-astra Blender repair of the existing faulty rig/actions.
The parent accepted the overhead hammer windup, actual-byte attack/move views, packed materials and terminal support reconciliation.

The installed mesh has 24,852 triangles, 29 bones, a separately weighted 196-triangle hammer and three material streams: Mesh_0.003 indices 0/1 and Gorilla_Hammer index 0.
All three streams use the preserved 2048 br29 diffuse/normal/specular maps.
The existing five animation IDs and eight engine-state aliases are retained; attack/defend/support_attack use the accepted hammer action, retreat uses move, and training uses recovery.
Death is terminal and non-looping; entity scale 1.0 is applied once.
Only Gorilla blocks changed in gfx/entities/012_africa_strange_forces.gfx and its matching .asset; the existing animation registry required no change.

All five exported actions passed actual-byte reimport at five samples each.
Authored source frames start at zero at 30 FPS; reimport frames start at one.
The source-to-export contact reconciliation maps 328 seam vertices to 151 unique source vertices within 2.176e-6 units, with separated head/pelvis support; soft-shadow appearance is not a claim that every limb touches the floor.
Source manifest: docs/assets/012_africa/models_3d/gorilla_heavy_infantry/runtime_copy_manifest_20260908.json.
Independent audit: 2026-09-08_gorilla_runtime_audit.md.

Six loaded sound files were converted to PCM16 mono 44.1 kHz with original samples preserved, zero clipping and maximum quantization error of half a PCM16 step.
The hammer cue begins at .979955 seconds so its measured onset meets the 1.0-second strike.
The death vocal begins at .339864 for the .4-second stagger; it is not described as a collision recording.
The recovery cue begins at .984966 for the 1.0-second grip check; movement retains one equipment-rattle cue per cycle.
Runtime attribution identifies the inherited chimpanzee vocal and metal recordings, authors, changes, CC BY 4.0 and CC BY-SA 4.0 terms.

## Verified runtime payloads

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_attack.anim` | 57166 | `2570C45E371330B9D5EC2EBEEBF75AB7805A0C8D14BDD150EC910D224CF289A4` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_death.anim` | 57899 | `A80A5E2FF64A2EB9B0538E02C83E615269E36C585368E5345DEDA10D834D777A` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry.mesh` | 2885287 | `27ECA3BE70D4AA92628C80E49C74DA647A9581CDD423BA4E07BA5B948A70B70D` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_br29_diffuse.dds` | 16777344 | `0B0F72A572C7B73D8A1B63CAF942EEE25888704878DEF43C3A590189CE076C3E` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_br29_normal.dds` | 16777344 | `ED9A05BE266D98C50C3BA53B829E33CB922F53F21C745E033BEA30128E779DB8` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_br29_specular.dds` | 16777344 | `63935BD65A57F4FBEE73EE4767F6C35AD1067CE8C296934A11825970F00586C1` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_idle.anim` | 57166 | `D16FD842D9CEBCCB5CA246703FD94B3C79F095181A8652567C7CA0461BC0EF77` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_move.anim` | 47003 | `E94862455824D802B8D3193CB17021CFB0A450AA94FF154446ED77136043F2BF` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_recovery.anim` | 57166 | `5F8268C3043997B391B48AE27C493A62D531182D5742B659AC4DAC71AEA11BD1` |
| `sound/012_africa/units/gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_idle.wav` | 176444 | `94936E5E92A20769409488ED4397DF787C43E8443C364932C22CF2252C40F3C5` |
| `sound/012_africa/units/gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_move.wav` | 105884 | `560EE95A4E1746972CD2C2B8662A90AFB866631AE775FA655A3DA60CC407D26E` |
| `sound/012_africa/units/gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_attack.wav` | 124100 | `8680B07B4846A4F12379339FCBE2E65D535283BC519571A2EC87B3BBA97C5CD7` |
| `sound/012_africa/units/gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_recovery.wav` | 132344 | `5D1766C861562D487C80586784D29B2ED42EF84194DABE1E292245BB2E9DA929` |
| `sound/012_africa/units/gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_death.wav` | 194084 | `44008B58D83F26C3632299D501A3A801295573ACC375BF7015D615529AE885C5` |
| `sound/012_africa/units/gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_select.wav` | 158804 | `B96FB073C3B1478E5BFCEA0D2D51C47D4E8061788AA5DB8446189526603FF577` |

## Simplifications, omissions, and blockers

No required 3D component or authored action was omitted.
The inherited counter remains marked needs_user_review for its earlier chroma-key production exception.
Audio has mechanical format, provenance and onset evidence; auditory suitability is unverified, and equipment rattle is not footstep audio.
The selection sound is invoked by the Gorilla spawn branch in common/scripted_effects/012_africa_action_effects.txt; this is not a generic per-subunit click-selection consumer.
No provider calls or credits were consumed, and no live-game result is claimed.
