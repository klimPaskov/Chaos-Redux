# Event 018 cave-monster model contract

The Oth-Kesh cave country uses one shared custom land-unit model with five role-specific counter families. The selected creature is a low-slung, slate-and-ochre armored quadruped generated from one approved fictional reference and calibrated against the installed western-European infantry mesh.

## Runtime model

- Canonical mesh identifier: `resources_found_cave_monster_mesh`.
- Canonical entity: `resources_found_cave_monster_entity`.
- Runtime model folder: `gfx/models/units/018_resources_found_cave_monster/`.
- Entity scale: `0.8` exactly once. Pre-export Blender working-geometry height is `7.3518247977`, giving a calibrated effective height of `5.8814598382`. Parsed exported-runtime AABB height is `7.3563573360`, giving the authoritative byte-level runtime effective vertical extent of `5.8850858688`. The disclosed delta is `0.0045325383` source units or `0.0036260306` effective units.
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

The final source-to-runtime action hashes and static reimport conclusions are recorded in `docs/plans/018_resources_found_plans/subagent_handoffs/cave_monster_3d_model_handoff.md` and `docs/plans/018_resources_found_plans/018_cave_monster_3d_integration_addendum.md`. Static reimports contain the 17-bone rig and 30,000-polygon mesh with contact ranges within approximately `+/-0.000015 m`.

## Sound synchronization

The four immutable sources are public-domain or CC0 recordings documented with attribution and checksums in `docs/plans/018_resources_found_plans/subagent_handoffs/cave_monster_3d_model_handoff.md`. The parent runtime uses mechanically converted PCM WAVs only:

- Idle ambience is a state-entry bed that stops on state change.
- Move and retreat trigger four short gravel contacts at `0.125`, `0.375`, `0.625`, and `0.875` seconds.
- Attack, defend, and support attack trigger a bounded roar at `0.60` seconds, shortly before frame 16.
- Death triggers a bounded gravel collapse at `0.75` seconds, at frame 18.

Definitions are in `sound/chaosx_resources_found_cave_monster_sound.asset`, and the timed events are in the canonical entity asset. No generated, synthesized, placeholder, or unlicensed sound is permitted.

## Validation boundary

The model, actions, materials, counters, aliases, and sound definitions have static and adapter/reimport evidence. A 2026-08-10 runtime-byte reimport freshly confirmed the 17-bone, 30,000-triangle mesh and all four actions. Fresh mesh, attack, death, and five-frame idle/move previews rendered from temporary byte-identical runtime copies. Idle and move quarter phases visibly differ while midpoint and end frames return exactly to the neutral decoded pixels; sampled contacts remain between approximately `-0.00000020` and `+0.00001316` source units. The combined idle/move contact sheet SHA-256 is `FC5D8A8AB3CCA0BE8143B7767DC55EE710E60CC7D4691C825958C8C5E03258AB`.

The same reconstruction mechanically inspected all ten counter strips and passed both frames, alpha bounds, family differentiation, vanilla olive-green large frame 0, grayscale disabled large frame 1, and the grayscale on-map precedent. Parent visual review also passed the contact sheet. All seven runtime WAVs are mono 44.1 kHz 16-bit PCM with zero clipped samples. The four immutable source hashes, source intervals, fades, unity-gain finding, sample-addressed attack trim, and normalized FFmpeg commands are preserved in `docs/plans/018_resources_found_plans/subagent_handoffs/event018_cave_audio_recipe_reconstruction_2026-08-10.md`; six current cues reproduce byte-for-byte and movement foot 02 differs only at its final sample by one least-significant 16-bit unit. Auditory balance, idle overlap, and live action synchronization remain unproven.

Static model/action visual closure is complete under the user's explicit no-HOI4-testing override. Live HOI4 consumer validation and audible playback were not performed, so normal-map-zoom presentation, entity-state transitions, sound synchronization, and runtime audible density are not claimed as in-game evidence.

The bounded `docs/assets/018_resources_found/models_3d/cave_monster_static_closure/` workspace retains the reconstructed counter, audio, provenance, and tool-call evidence while the overall Event 018 goal is active. The locked adapter's exact `cave_monster` root was also temporarily reconstructed from runtime-byte copies to retain reimport proofs; neither workspace is a runtime dependency.
