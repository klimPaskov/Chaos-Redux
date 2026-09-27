# Event 018 cave-monster model contract

The Oth-Kesh cave country uses one shared custom land-unit model with five role-specific counter families. The selected creature is a low-slung, slate-and-ochre armored quadruped generated from one approved fictional reference and calibrated against the installed western-European infantry mesh.

Current disposition: `implemented` for the static runtime package. `docs/plans/018_resources_found_plans/cave_monster_current_package_manifest.md` is the authoritative current status and hash inventory. Live HOI4 and audible behavior remain unverified, and the absent deterministic source/job package blocks strict pipeline package completion and reproducible continuation.

## Runtime model

- Canonical mesh identifier: `resources_found_cave_monster_mesh`.
- Canonical entity: `resources_found_cave_monster_entity`.
- Runtime model folder: `gfx/models/units/018_resources_found_cave_monster/`.
- Entity scale: `0.8` exactly once. Pre-export Blender working-geometry height is `7.3518247977`, giving a calibrated effective height of `5.8814598382`. Parsed exported-runtime AABB height is `7.3563573360`, giving the authoritative byte-level runtime effective vertical extent of `5.8850858688`. The disclosed delta is `0.0045325383` source units or `0.0036260306` effective units.
- Mesh: 18,927 vertices in four skinned streams on a 19-bone creature skeleton (see below), no unweighted vertices.
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

## Skeleton and actions

The creature's original rig was an elephant template (trunk, howdah, and rider bones) that the stone-plated body never fitted, so every action was near-static.
On 2026-09-27 the shipped mesh was kept and given its own 19-bone creature skeleton with `lab_limbs.py` (`import`, then `skeleton`): a non-deforming root, hips and chest along the body, neck and head, a two-bone tail, and three bones per leg placed on joints measured from the leg pieces below the belly; the whole mesh was heat-weighted to it.
Eight actions were authored with `lab_limbs.py` `keys` at 30 FPS, followed by its measured floor pass on every role:

| Action | Frames | What it shows |
| --- | ---: | --- |
| idle | 1-80 | breathing, head turning to look around, tail sway |
| move | 1-41 | four-beat walk (rear right, front left, rear left, front right) with body bob |
| retreat | 1-41 | the walk played backward |
| defend | 1-50 | drops low behind the plated shoulders, head down |
| attack | 1-60 | crouch, lunge, and jaw snap at frame 24 |
| support_attack | 1-70 | rears onto the hind legs, slams the forelimbs down, roars |
| training | 1-80 | alternate forepaw strikes with a roar between |
| death | 1-70 | staggers and collapses onto its belly, legs splayed |

All eight are reimport-proven from `docs/assets/018_resources_found/models_3d/cave_monster/export/v4/`; the death settles about 0.1 unit (1.5% of height) into the ground as the belly lands.
The runtime maps are the existing diffuse, normal, and specular DDS files.

## Sound synchronization

The four sourced effects in `sound/chaosx_resources_found_cave_monster_sound.asset` (public-domain or CC0, attribution and checksums in `docs/plans/018_resources_found_plans/subagent_handoffs/cave_monster_3d_model_handoff.md`) are timed to the authored beats: the four gravel footfalls on the four walk contacts, the bounded roar on the bite, the slam, and the pawing, the idle growl in defend and the training roar, and the gravel collapse at the start of the death with a footfall when the body lands.

## Validation boundary

The rebuilt mesh and all eight actions have adapter partition, export, and actual-byte reimport evidence under `docs/assets/018_resources_found/models_3d/cave_monster/export/v4/export_report.json`, with rendered side and three-quarter review sheets under `blender/working/v3/review/`.
The counters were not changed; their earlier mechanical inspection still applies.
All seven runtime WAVs are the existing sourced cues; their recipes are in `docs/plans/018_resources_found_plans/subagent_handoffs/event018_cave_audio_recipe_reconstruction_2026-08-10.md`.
Live HOI4 playback, map-zoom presentation, and audible balance belong to the user.
