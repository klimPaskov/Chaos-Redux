# Zombies runtime handoff

Status: asset package complete; parent-owned runtime registration and user-owned live HOI4 verification are pending.

## Proposed stable identifiers

- Unit sprite identifier: `zombies`
- Entity: `zombies_entity`
- PDX mesh: `chaosx_zombies_mesh`
- Material: `chaosx_zombies_pdx_material`
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

The future entity should use scale `0.8` exactly once. The mesh coordinates are calibrated to the measured vanilla source height of `7.3518242835`; do not compensate with another model scale.

## Exported runtime assets

| Artifact | Relative path | SHA-256 |
| --- | --- | --- |
| Mesh | `export/mesh/chaosx_zombies.mesh` | `A23F8C6CC7C85B2686E02DFA6AC92B29B553D534ECBB53F0BA8E650ADFB8DAEB` |
| Idle | `export/anim/chaosx_zombies_idle.anim` | `4E12BBCC29A840CEC6B4EDB67D5191CF10F119A028EE238E6C9FFEB589986A43` |
| Move | `export/anim/chaosx_zombies_move.anim` | `AE730339C4691C6CB2205F8C95D01075CA0CD328AA81799AC09255EC49CEDB87` |
| Attack | `export/anim/chaosx_zombies_attack.anim` | `C4E7BB3FB0D2F6834F2D01E9D0C9EB179AE0A868167D2FD708B1E9B4AE5F6513` |
| Death | `export/anim/chaosx_zombies_death.anim` | `70C585CB303A321D97A78B5B0A4FAEC59C747CE6B2AC98C55522FBDCBFAA8436` |

Material texture binding in the exported mesh is `PdxMeshAdvanced` with `texture_0.dds`, `texture_specular.dds`, and `texture_normal.dds`. The packed specular channels are red unused mask zero, green specular, blue metallic, and alpha roughness.

## Parent-owned next step

Register the proposed identifiers in the appropriate Chaos Redux entity/material/GFX surfaces and perform the user's live HOI4 verification. This handoff intentionally does not edit those runtime files.
