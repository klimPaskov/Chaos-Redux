# Event 016 alien infantry Meshy runtime promotion

## Scope

This handoff promotes the accepted Meshy V13 firearm-bearing alien infantry export into the runtime `gfx` tree. The mesh contains the retro laser firearm as part of the provider-authored skinned body, so no local weapon attachment, parenting, weighting, or replacement motion was authored.

## Provider and actions

- Meshy V13 source export: `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/`.
- Genuine provider actions: `223 Draw_and_Shoot_from_Back_1` for attack, `234 Walk_Forward_While_Shooting` for support attack, `0 Idle`, `692 walking_2_inplace`, `685 Walk_Backward_with_Gun_inplace`, and `183 Shot_and_Fall_Backward` for death.
- The attack action contains aim, discharge, recoil, and recovery motion; the support action contains the provider-authored armed firing motion. The death action is an articulated fall, not a transform-only mockup.
- The locked Blender HOI4 adapter exported and reimported the actual bytes with the provider rig and packed material set. Source/provider evidence remains under `docs/assets/.../alien_infantry/`.

## Runtime files

- `gfx/models/units/alien_infantry/alien_infantry.mesh`
- `gfx/models/units/alien_infantry/alien_infantry_idle.anim`
- `gfx/models/units/alien_infantry/alien_infantry_move.anim`
- `gfx/models/units/alien_infantry/alien_infantry_laser_attack.anim`
- `gfx/models/units/alien_infantry/alien_infantry_defend.anim`
- `gfx/models/units/alien_infantry/alien_infantry_support_attack.anim`
- `gfx/models/units/alien_infantry/alien_infantry_retreat.anim`
- `gfx/models/units/alien_infantry/alien_infantry_death.anim`
- `gfx/models/units/alien_infantry/alien_infantry_diffuse.dds`
- `gfx/models/units/alien_infantry/alien_infantry_normal.dds`
- `gfx/models/units/alien_infantry/alien_infantry_specular.dds`
- `gfx/entities/alien_infantry.gfx`
- `gfx/entities/alien_infantry.asset`
- `gfx/models/units/alien_infantry/animation_alien_infantry.asset`

The GFX registration uses the exported material slot `char1.002` and `PdxMeshAdvanced`. Entity states resolve all expected HOI4 consumers, including idle, move, attack, defend, support attack, retreat, training, wounded, and death; training/wounded fall back to already-registered genuine idle/defend actions because the unit is not trainable and no separate provider clips were requested.

## Promotion hashes

The source export and runtime copy are byte-identical for the promoted binary files.

| Runtime file | SHA-256 |
| --- | --- |
| `alien_infantry.mesh` | `D03EA316E2C5DCC4BD3224AE7D3C62DF3F86E4CADA77A6A7535C15D74BDF8342` |
| `alien_infantry_idle.anim` | `D6936AE996DBE998DBEE0633B4DCAC346B6C5D974FC643ACA62AAC73719CB2EF` |
| `alien_infantry_move.anim` | `727BCA51B68EEA445198C1029331FF06F15F69215358ABC9CC29A4064096217F` |
| `alien_infantry_laser_attack.anim` | `288209BC4B9CBB3D19A629C2277DF7816CDF33B475EA68BF0D368F7C2E2150F0` |
| `alien_infantry_defend.anim` | `F07A8BC46D68F72DD622014CE31BA9420A3CC1FF419BF3690D44D5F42E9E3A73` |
| `alien_infantry_support_attack.anim` | `DADC3823EA4C2FE5F21F10DAE310F52D54E5379A124C01CDEE3AA954F4EE3061` |
| `alien_infantry_retreat.anim` | `DB9E72F782A19C84A7C4C8CF429654D0BAAAC59A7999B381CA9267DD598BD2DC` |
| `alien_infantry_death.anim` | `D8D26A8B7A6F01ADCB64103885171C837DB36CB7BBB6A6A15EB6C2D66F15D7A0` |
| `alien_infantry_diffuse.dds` | `0A44479B3205D2E732A5E4A9D1ECFC45BC61830E38244C06D1C028A89A62D3AA` |
| `alien_infantry_normal.dds` | `DF1F9C947B64478BA5B739BC215D18400EC38272B2325D2F19E395C108873E39` |
| `alien_infantry_specular.dds` | `5F1224A4443C20432182668DB6F567CCAD02B9D8143F57F08DFB88183CCE755D` |

## Sound and effects

The entity binds the sourced alien laser, movement, idle, and death sound effects. Discharge timing is frame 145 / 4.8000 seconds for attack and frame 50 / 1.6333 seconds for support attack, matching the provider action evidence.

The model export has no stable muzzle/effect locator; only the fused rifle geometry and normal hand bones are present. Consequently `alien_laser_muzzle_particle` and `alien_laser_muzzle_flash` remain registered but intentionally unbound rather than being placed at the entity origin or an inferred hand point. Exact muzzle particle/light synchronization is an explicit remaining runtime blocker and must be resolved through a provider/adapter-supported locator before it is wired.

## Validation and remaining risk

The runtime registrations were compared against the existing clone and autonomous-robot entity conventions, and all referenced animation and sound identifiers resolve to files/definitions in this package. The binary promotion was hash-checked source-to-destination. HOI4 MCP render/inspection and live consumer validation remain blocked by the bounded MCP timeout and are not replaced by source review.
