# Alien infantry weapon-free body and Blender action integration

Status: requested body, separate pistol, skeletal action and firing-cue repair implemented; inherited counter and selection-consumer limitations remain explicit.
Acceptance basis: the user instructed regeneration of firearm-bearing custom bodies without firearms, followed by GPT-6-astra Blender rigging, separately modeled held objects and real skeletal animation.
The approved weapon-free Meshy7 body was generated once for 30 credits; no additional generation or paid rig/action attempts were used.

The assembled model has 55,150 triangles, a measured 52-bone rig, seven body material streams and a separate 3,052-triangle ray pistol stream.
The export contains `mesh.002` indices 0 through 6 and `AlienRayPistol` index 0.
Each object uses its dedicated packed diffuse/normal/specular maps with `PdxMeshAdvanced`.
The source remains calibrated to 7.351824 units and receives entity scale 0.8 once.

Seven distinct Blender actions replace the fused-weapon provider actions: idle, move, laser attack, defend, support attack, retreat and death.
Runtime `attack` maps to the laser-attack clip.
Idle, move, defend and retreat loop; attack and support attack return to idle after one shot sequence; death remains terminal.
The support action includes two separately articulated shots and recoveries.

All seven exported animation binaries were reimported against the actual final mesh and reviewed for material, anatomy, grip and ground contact.
The parent reviewed actual-byte laser attack frame25, support attack frame49, death frame61 and the focused firing-hand view.
The accepted corpse is supported by its upper back/shoulders and pelvis; the pistol does not prop it above the floor.
The separate grip is wrapped by articulated fingers, with the index finger at the trigger.

The exported muzzle survives actual-byte reimport on `RightWeapon`, with bone-local translation approximately (0,1.039,-0.38) and basis diag(1,-1,-1).
Four exact firing/recoil frame inspections verify the locator before runtime marker synchronization.

## Runtime cue timing

| State | Source frame | Seconds | Cue |
| --- | --- | --- | --- |
| attack | 19 | 0.600000 | Laser sound, muzzle particle and light |
| support_attack | 21, 53 | 0.666667, 1.733333 | Two laser sound/particle/light events |
| move | 1, 17 | 0.000000, 0.533333 | Existing sourced footsteps |
| retreat | 1, 19 | 0.000000, 0.600000 | Existing sourced footsteps |
| death | 1, 43 | 0.000000, 1.400000 | Death vocalization and body impact |

Times use (frame-1)/30 and match the selected action phases.
The existing particle/light/sound definitions and six audio payloads are preserved.

## Payload verification

The parent independently verified every source and runtime SHA-256 and byte count.

| Runtime file | Bytes | SHA-256 |
| --- | ---: | --- |
| `gfx/models/units/alien_infantry/alien_infantry.mesh` | 5109871 | `842F0FCA441F9FF14C8A32AC4EF3E9D93C998195D7ACB49CEBD6A1C2BC822E21` |
| `gfx/models/units/alien_infantry/alien_infantry_idle.anim` | 83824 | `5E0F1F35F79E7E296621B80E9E78F859BDF8EC93985B5384A353CF0AA75C4572` |
| `gfx/models/units/alien_infantry/alien_infantry_move.anim` | 57351 | `B5343BE0ABA8393B7B84CD2FA6E91D91F53A68BB3CD1D5AE7676AEA3041E030A` |
| `gfx/models/units/alien_infantry/alien_infantry_laser_attack.anim` | 69794 | `A5BF8880DC846F76A0E0FC5E55DEA56C9C05C5798F096FF69401FCE5C8732F5A` |
| `gfx/models/units/alien_infantry/alien_infantry_defend.anim` | 69794 | `75A699234B44286B9DC156A9CC48C4F8DD4E36DF68A4F53D8F2511593761390D` |
| `gfx/models/units/alien_infantry/alien_infantry_support_attack.anim` | 106989 | `5B01C35DC0FDA1A13F3B9A0EA50ABC27AF383DC9F5797C355505F9B52F2D82EC` |
| `gfx/models/units/alien_infantry/alien_infantry_retreat.anim` | 62861 | `8B821E6DB187179BE96EB1D18AEA7592EFB486B507E6780F49DC7440FA81A826` |
| `gfx/models/units/alien_infantry/alien_infantry_death.anim` | 104839 | `76BB4385E3FDEED97B0E222F4AF74A6AE3A7DE2775E85592B484E4D9A8BD0BD7` |
| `gfx/models/units/alien_infantry/alien_infantry_body_diffuse.dds` | 4194432 | `BEED16104FF19B99918FBC1756BB75B85CDCA64585D6725F17C47B9FF6F380E7` |
| `gfx/models/units/alien_infantry/alien_infantry_body_normal.dds` | 4194432 | `EC82AA4B8F62FCC54A1D8881AC5F65C6878A48BBF1191A059DB01DC1CB589DB8` |
| `gfx/models/units/alien_infantry/alien_infantry_body_specular.dds` | 4194432 | `9F6DBE1F6E6F501AE1592B9F307E54326A9F717EFB5A32EA5DEA81156A005559` |
| `gfx/models/units/alien_infantry/alien_infantry_pistol_diffuse_square.dds` | 1048704 | `8EC5A0CAB6FF3C96B78C53E7FDAC46135A086B8AEB43EDFD4D70594210416B15` |
| `gfx/models/units/alien_infantry/alien_infantry_pistol_normal_square.dds` | 1048704 | `078F0720244274138CBF4940E76853063B528944B6E59C621767A27F7193DE4C` |
| `gfx/models/units/alien_infantry/alien_infantry_pistol_specular_square.dds` | 1048704 | `4018D26C5314CA3245584A0DFC4F4EBD75FE12BFDA80F0E19CD62641D714BFD2` |

## Evidence and limits

Final model evidence lives under `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/attempts/20260906_weaponfree_blender/`: `final_manifest.md`, `runtime_copy_manifest.json`, `final_reimport_acceptance.json`, `final_firing_locator_evidence.json`, `resume_death_contact_acceptance.json`, `resume_preserved_audio_hashes.json` and `parent_runtime_copy_receipt.json`.
Runtime definitions are `gfx/entities/alien_infantry.gfx`, `gfx/entities/alien_infantry.asset`, and `gfx/models/units/alien_infantry/animation_alien_infantry.asset`.
No unapproved simplifications were used for the requested body/rig/action/held-object repair.
The inherited counter review and per-subunit selection-audio consumer limitation remain open; this tranche does not claim those unrelated completion gates passed.
Visual proof samples exported action phases and exact firing frames; no live-game completion is claimed.
