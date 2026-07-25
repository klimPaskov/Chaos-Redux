# Zombies runtime handoff

Status: asset package and runtime registration complete; user-owned live HOI4 verification remains pending.

## Stable identifiers

- Unit sprite identifier: `zombies`
- Entity: `zombies_entity`
- PDX mesh: `chaosx_zombies_mesh`
- Material binding: `PdxMeshAdvanced` through the `Mesh_0.001` meshsettings entry
- Idle animation: `chaosx_zombies_idle_animation`
- Move animation: `chaosx_zombies_move_animation`
- Attack animation: `chaosx_zombies_attack_animation`
- Death animation: `chaosx_zombies_death_animation`

## Vanilla state mapping

| Vanilla infantry state | Custom action | Package evidence |
| --- | --- | --- |
| idle | `chaosx_zombies_idle_animation` | `export/anim/chaosx_zombies_idle.anim`; 98 frames at 24 fps; reimport passed |
| moving | `chaosx_zombies_move_animation` | `export/anim/chaosx_zombies_move.anim`; 73 frames at 24 fps; reimport passed; minor sampled sole-contact risk recorded |
| attack | `chaosx_zombies_attack_animation` | `export/anim/chaosx_zombies_attack.anim`; 69 frames at 24 fps; corrected Hips root contact; reimport passed |
| death | `chaosx_zombies_death_animation` | `export/anim/chaosx_zombies_death.anim`; 73 frames at 24 fps; provider and reimport gates passed |

The registered `zombies_entity` uses scale `0.8` exactly once. The mesh coordinates are calibrated to the measured vanilla source height of `7.3518242835`; do not compensate with another model scale.

## Exported runtime assets

| Artifact | Relative path | SHA-256 |
| --- | --- | --- |
| Mesh | `export/mesh/chaosx_zombies.mesh` | `A23F8C6CC7C85B2686E02DFA6AC92B29B553D534ECBB53F0BA8E650ADFB8DAEB` |
| Idle | `export/anim/chaosx_zombies_idle.anim` | `4E12BBCC29A840CEC6B4EDB67D5191CF10F119A028EE238E6C9FFEB589986A43` |
| Move | `export/anim/chaosx_zombies_move.anim` | `AE730339C4691C6CB2205F8C95D01075CA0CD328AA81799AC09255EC49CEDB87` |
| Attack | `export/anim/chaosx_zombies_attack.anim` | `C4E7BB3FB0D2F6834F2D01E9D0C9EB179AE0A868167D2FD708B1E9B4AE5F6513` |
| Death | `export/anim/chaosx_zombies_death.anim` | `70C585CB303A321D97A78B5B0A4FAEC59C747CE6B2AC98C55522FBDCBFAA8436` |

Material texture binding in the exported mesh is `PdxMeshAdvanced` with `texture_0.dds`, `texture_specular.dds`, and `texture_normal.dds`. The packed specular channels are red unused mask zero, green specular, blue metallic, and alpha roughness.

## Registered runtime paths

| Surface | Registered path | SHA-256 or binding |
| --- | --- | --- |
| Unit sprite consumer | `common/units/zombies.txt` | base `zombies` block uses `sprite = zombies`; variants remain `sprite = infantry` |
| Mesh GFX | `gfx/entities/chaosx_zombies.gfx` | `chaosx_zombies_mesh`; object `Mesh_0.001`; `PdxMeshAdvanced` |
| Entity asset | `gfx/entities/chaosx_zombies.asset` | `zombies_entity`; scale `0.8` |
| Animation asset | `gfx/models/units/chaosx_zombies/animation_chaosx_zombies.asset` | four action registrations |
| Mesh copy | `gfx/models/units/chaosx_zombies/chaosx_zombies.mesh` | `A23F8C6CC7C85B2686E02DFA6AC92B29B553D534ECBB53F0BA8E650ADFB8DAEB` |
| Idle copy | `gfx/models/units/chaosx_zombies/chaosx_zombies_idle.anim` | `4E12BBCC29A840CEC6B4EDB67D5191CF10F119A028EE238E6C9FFEB589986A43` |
| Move copy | `gfx/models/units/chaosx_zombies/chaosx_zombies_move.anim` | `AE730339C4691C6CB2205F8C95D01075CA0CD328AA81799AC09255EC49CEDB87` |
| Attack copy | `gfx/models/units/chaosx_zombies/chaosx_zombies_attack.anim` | `C4E7BB3FB0D2F6834F2D01E9D0C9EB179AE0A868167D2FD708B1E9B4AE5F6513` |
| Death copy | `gfx/models/units/chaosx_zombies/chaosx_zombies_death.anim` | `70C585CB303A321D97A78B5B0A4FAEC59C747CE6B2AC98C55522FBDCBFAA8436` |
| Diffuse copy | `gfx/models/units/chaosx_zombies/texture_0.dds` | `C16E4239EB88969A5BEA53A8C367FDE346E6251CE5F3E773F26FA9B56A4E33BE` |
| Packed specular copy | `gfx/models/units/chaosx_zombies/texture_specular.dds` | `6915B734D0475D91265B928F31C149AF1BDA379F92FC8C2BDB7B1DA3B40EFE76` |
| Normal copy | `gfx/models/units/chaosx_zombies/texture_normal.dds` | `9BA3DB2CC6AAF43BCD5B3B968FDCFF07B99BF0A242C9F814CB93DD3972D37A4F` |

The runtime state mapping is attack for attack/defend/support_attack, move for move/retreat, death for death, idle for idle, and idle for training. The live consumer is the base `zombies` unit; named variants are intentionally not wired to this model in this task.

User-owned live HOI4 verification remains pending; Hearts of Iron IV was not launched by the agent.
