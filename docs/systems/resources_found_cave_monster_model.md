# Event 018 cave-monster model contract

The Oth-Kesh cave country uses one shared custom land-unit model with five role-specific counter families. The selected creature is a low-slung, slate-and-ochre armored quadruped generated from one approved fictional reference and calibrated against the installed western-European infantry mesh.

## Runtime model

- Canonical mesh identifier: `resources_found_cave_monster_mesh`.
- Canonical entity: `resources_found_cave_monster_entity`.
- Runtime model folder: `gfx/models/units/018_resources_found_cave_monster/`.
- Entity scale: `0.8` exactly once; measured source height `7.3518247977`, effective runtime height `5.8814598382`.
- Mesh: 30,000 triangles, 14,998 working vertices, one UV map, 17-bone nonhumanoid rig, no zero-weight deforming vertices.
- Material: `PdxMeshAdvanced` with the stable diffuse, normal, and specular DDS maps in the same runtime folder.

The unit system resolves a sub-unit `sprite` through `<sprite>_entity`. The five aliases below clone the canonical entity so every cave-brood role receives the same mesh, actions, scale, and sound states without duplicate model packages:

| Sub-unit sprite | Resolving entity | Counter pair |
| --- | --- | --- |
| `cave_monster_brood` | `cave_monster_brood_entity` | `cave_monster_brood_icon` |
| `cave_stone_phalanx_brood` | `cave_stone_phalanx_brood_entity` | `cave_stone_phalanx_brood_icon` |
| `cave_burrow_war_brood` | `cave_burrow_war_brood_entity` | `cave_burrow_war_brood_icon` |
| `cave_scree_tide_brood` | `cave_scree_tide_brood_entity` | `cave_scree_tide_brood_icon` |
| `cave_anchor_guard_brood` | `cave_anchor_guard_brood_entity` | `cave_anchor_guard_brood_icon` |

The aliases live in `gfx/entities/018_resources_found_cave_monster.asset`. The five large counters are `152x42` two-frame DDS strips and the five on-map counters are `60x12` two-frame DDS strips, registered in `interface/chaosx_subuniticons.gfx` and copied to the two runtime counter folders.

## Skeletal actions

All actions are 24 FPS, in-place, grounded, and reimported through the repository-locked `io_pdx_mesh` route. The hard-weighted semantic rig uses a restrained angle envelope to preserve clean plated silhouettes without mesh shear.

| Runtime action | Frames | Loop | Runtime binding |
| --- | ---: | --- | --- |
| `resources_found_cave_monster_idle` | 0-48 | yes | idle/training |
| `resources_found_cave_monster_move` | 0-24 | yes | move/retreat |
| `resources_found_cave_monster_attack` | 0-32 | no | attack/defend/support attack |
| `resources_found_cave_monster_death` | 0-36 | no | death |

The final source-to-runtime action hashes are recorded in the model handoff and the temporary validation ledger. Static reimports contain the 17-bone rig and 30,000-polygon mesh with contact ranges within approximately `+/-0.000015 m`.

## Sound synchronization

The four immutable sources are public-domain or CC0 recordings preserved with attribution and checksums in the active evidence handoff. The parent runtime uses mechanically converted PCM WAVs only:

- Idle ambience is a state-entry bed that stops on state change.
- Move and retreat trigger four short gravel contacts at `0.125`, `0.375`, `0.625`, and `0.875` seconds.
- Attack, defend, and support attack trigger a bounded roar at `0.60` seconds, shortly before frame 16.
- Death triggers a bounded gravel collapse at `0.75` seconds, at frame 18.

Definitions are in `sound/chaosx_resources_found_cave_monster_sound.asset`, and the timed events are in the canonical entity asset. No generated, synthesized, placeholder, or unlicensed sound is permitted.

## Validation boundary

The model, actions, materials, counters, aliases, and sound definitions have static and adapter/reimport evidence. Live HOI4 consumer validation remains user-owned: verify one division of each locked Oth-Kesh template at normal map zoom, confirm grounded idle/move/attack/death states, and confirm the five distinct large/on-map counter pairs. The user explicitly does not require this task to launch HOI4.

During active work, detailed provider files, previews, licenses, hashes, manifests, and reports remain in the event-scoped temporary evidence workspace under `docs/assets/018_resources_found/`. Once the full Event 018 goal is complete and those durable facts are retained here and in the plan handoffs, that temporary workspace must be deleted.
