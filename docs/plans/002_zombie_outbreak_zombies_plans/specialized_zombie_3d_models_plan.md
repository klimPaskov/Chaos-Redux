# Specialized zombie 3D model production plan

Status: reference packages ready; Meshy generation is blocked by the verified provider credit gate.

This plan covers the seven requested non-armored specialized zombie sub-units. The base `zombies` model remains unchanged, and `armored_undead_zombies`, `armored_necrotic_zombies`, and `armored_demonic_zombies` are explicitly out of scope.

## Runtime scope

| Sub-unit | Portrait identity to preserve | Profile | Mesh stem | Entity | Required actions |
| --- | --- | --- | --- | --- | --- |
| `infected_zombies` | Gaunt corpse-like human with long disordered dark hair, hollow eyes, ragged long coat, and open mouth. | `humanoid_infected` | `chaosx_infected_zombies` | `chaosx_infected_zombies_entity` | idle, move, attack, death |
| `rabid_zombies` | Predatory pale humanoid with red eyes, sharp canines, slick dark hair, and a forward hunting posture. | `humanoid_rabid` | `chaosx_rabid_zombies` | `chaosx_rabid_zombies_entity` | idle, move, attack, death |
| `parasitic_zombies` | Slim, slightly hunched dark-haired humanoid with a narrow asymmetrical face and one-sided pale mauve fused growths, visible mushroom caps, and smaller parasite forms running from the temple through the neck, shoulder, and upper arm. | `humanoid_parasitic` | `chaosx_parasitic_zombies` | `chaosx_parasitic_zombies_entity` | idle, move, attack, death |
| `mutant_zombies` | Tall, lean, powerful bare-bodied pale mutant with a small-eyed head and oversized vertical mouth; no bulky tank-like torso or clothing. | `humanoid_mutant` | `chaosx_mutant_zombies` | `chaosx_mutant_zombies_entity` | idle, move, attack, death |
| `undead_zombies` | Tall narrow skull-faced humanoid with a long jaw, sparse hair, one amber eye, and a worn dark suit. | `humanoid_undead` | `chaosx_undead_zombies` | `chaosx_undead_zombies_entity` | idle, move, attack, death |
| `necrotic_zombies` | Very thin bald brown-gray mummy-like humanoid with an asymmetrically damaged face, sparse torn wraps, and dramatically elongated arms. | `humanoid_necrotic` | `chaosx_necrotic_zombies` | `chaosx_necrotic_zombies_entity` | idle, move, attack, death |
| `demonic_zombies` | Pale bald supernatural creature with blank light eyes, an exaggerated fixed grin, elongated animal-like legs, long limbs and nails, smooth skin, sparse dark wraps, and large folded ragged wings. | `nonhumanoid_winged_biped` | `chaosx_demonic_zombies` | `chaosx_demonic_zombies_entity` | idle, move, attack, death |

## Shared production gates

- Each job has exactly one clean provider input at `refs/original/meshy_input.png`.
- Each input is portrait-inspired and is recorded with a SHA-256 digest in its local `input_manifest.json`.
- Humanoid jobs use the installed vanilla `western_european_infantry.mesh` calibration crosswalk: source height `7.351824797689915`, forward `-Y`, up `+Z`, and entity scale `0.8` applied exactly once.
- Demonic uses the creature route with explicit component segmentation, a custom creature rig, armature-object ground correction, and a measured scale crosswalk; it may not be forced into the humanoid armature.
- Each package targets one coherent HOI4 unit-scale mesh with `PdxMeshAdvanced` materials, diffuse/packed-specular/normal DDS maps, no negative scale, no detached floating geometry, and no animation-only placeholder.
- Each package exports four consumed skeletal actions at 30 FPS: idle, move, attack, and death. The action meaning is unit-specific: rabid uses a low hunting sprint, while mutant and necrotic use heavy locomotion, preserving the same runtime action slots.
- Every action is reimported through Blender/io_pdx_mesh and receives an actual-byte parse, ground-contact, frame-range, and runtime-candidate report before parent wiring.
- Each unit receives a bespoke large and on-map vanilla-green counter package before its sub-unit definition is switched to a custom sprite.
- Each unit receives sourced audio for selection, idle, movement, attack, and death roles with provenance, license, checksums, normalization evidence, and action synchronization. The engine selection consumer remains the country/original-tag infantry selection event; the package still records a unit-specific selection role for the parent wiring audit.
- The pilot loader is fail-closed on route design: nonhumanoid jobs require a numeric measured scale crosswalk and a dedicated creature rig family before balance checks, paid calls, or export. The demonic package uses the `winged_biped` route with separate wing and digitigrade bones; it must never be sent through the humanoid exporter.

## Planned runtime crosswalk

| Consumer | Planned registration |
| --- | --- |
| Unit sprite | `common/units/zombies.txt` changes only for the seven named non-armored sub-units, each to its own sprite stem. |
| Mesh | `gfx/models/units/chaosx_<unit>/chaosx_<unit>.mesh`. |
| Entity | `gfx/entities/chaosx_specialized_zombies.asset` with one entity per unit and the calibrated scale. |
| Mesh registration | `gfx/entities/chaosx_specialized_zombies.gfx` with one `pdxmesh` per unit and four animation IDs per unit. |
| Animation registration | One `animation_chaosx_<unit>.asset` per unit under the matching model folder. |
| Counter icons | `gfx/interface/counters/divisions_large/unit_<unit>_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_<unit>_icon.dds`, with matching `.gfx` entries and consumer references. |
| Sound state roles | Unit entity states reference the unit's sourced idle, move, attack, and death sound package. Selection audio is audited against the engine's country/original-tag selection consumer rather than incorrectly attached to a mesh state. |

No runtime file is switched until the corresponding mesh, four animations, textures, audio receipt, counter receipt, and reimport evidence exist. This prevents missing-entity errors and prevents a reference or unrigged candidate from entering a live entity definition.

## Credit gate

The repository estimate for one complete Meshy 6 package with one generation attempt, rigging, and four animations is `47` credits. The seven requested packages require `329` credits before remeshes or recovery attempts. The latest live balance check returned `156`, leaving a verified shortfall of `173` credits. No downgrade, manual substitute, static-only model, or untracked provider attempt is authorized by this plan. The separately staged Wendigo reference remains outside this active seven-unit plan until a quadruped route is enabled.

## Exclusions

The existing base `zombies` model is not regenerated. The armored variants `armored_undead_zombies`, `armored_necrotic_zombies`, and `armored_demonic_zombies` are not regenerated, remapped, or given new model assets.
