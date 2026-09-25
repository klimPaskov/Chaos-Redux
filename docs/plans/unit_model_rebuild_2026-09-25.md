# Custom unit model rebuild queue

## Accepted scope and order

The 2026-09-25 inventory found 32 distinct installed custom unit meshes under `gfx/models/units`.
The autonomous robot, portal raider, alien infantry, and xenobiological assault organism remain as they are under the user's instruction.
The autonomous robot's remaining firing presentation and sound work is tracked separately in `docs/plans/shared_robot_system_plans/2026-09-25_autonomous_robot_firing_presentation.md`.
The rebuild queue contains the other 28 installed meshes, one new base zombie, and one distinct Wendigo: 30 models total.
Armored zombie battalions reuse their corresponding family models.
The base zombie is first; all other models wait until its offline export and runtime wiring evidence passes and the user has reviewed the next model's exact reference and revised credit ceiling.
The historical Bone Guard body task consumed 30 credits before the queue decision; it is an unpromoted candidate and no further Bone Guard provider work belongs to the current model.

## Current model: base zombie

The `zombies` subunit currently uses `sprite = infantry` because its old dedicated model and entity were removed.
Its new approved design brief calls for one unarmed member of a mixed civilian horde, with pale gray-green skin and muted gray, olive, and brown 1936–1945 civilian fabric.
The historical brown-jacket image and broken-model screenshots are not identity references for this new input.
Prepare one new fully colored body image with genuine alpha, a complete grounded humanoid in a relaxed rig-friendly pose, separated limbs, visible empty hands and both feet, and no prop, scene, text, or background.
The exact image must be shown to the user and accepted before a Meshy call.
The first prepared candidate (SHA-256 `843cdc9d40f0e8ff442517eb8a0e700d9e0bd6c772ec37b98d8d32c5ae830a19`, 1024 × 1536 RGBA) was rejected by the user as "too human" on 2026-09-25.
The proposed revision is `docs/assets/002_zombie_outbreak/models_3d/zombies/refs/original/meshy_input.png` (SHA-256 `3723991B3EFC92D573CA1CB94CDC6177EB1D501EE5F207DB1613D4E50C3EB3BB`, 1024 × 1536 RGBA), with unmistakable corpse-like anatomy and a complete rig-friendly biped.
The user approved the revised exact image and 64-credit ceiling on 2026-09-25, authorizing the bounded base zombie Meshy work from that SHA-256 input.
No Meshy call is authorized for the rejected image or a different revision.

The planned paid operations are one Meshy 7 textured body (30 credits), one eligible-humanoid rig attempt (5), and seven or eight suitable action presets (21–24), for 56–59 credits.
The rig's included walk counts toward movement only if it passes zombie movement review.
At most one necessary remesh raises the model ceiling to 64 credits.
The 64-credit ceiling is a review figure, not an authorization to submit a paid call before image review.
Poor rigging or an unsuitable action moves to deliberately authored Blender skeleton, weights, and full skeletal actions with no second paid attempt.
The action roles are idle, move, attack, defend, support attack, retreat, training, and death; action content and timing must fit an unarmed shambler rather than reuse a single generic loop.
The parent owns HOI4 runtime, sound and counter wiring; the model worker owns the bounded source and export package.

### Base zombie runtime preflight

`common/units/zombies.txt` supplies the current `zombies` sprite assignment, which will point to the exported custom entity only after the accepted runtime asset exists.
The model requires new `gfx/entities/chaosx_zombies.gfx` and `.asset` registrations and a matching `gfx/models/units/chaosx_zombies/` mesh, textures, action exports, and animation registration.
The existing `sound/chaosx_zombies_sound.asset` defines zombie idle, move, attack, and death soundeffects, but its header and active consumers must be reviewed when the entity is wired.
The existing `interface/chaosx_subuniticons.gfx` and `interface/chaosx_texticons.gfx` already name base zombie counter and text-icon consumers; their actual DDS art must become a distinct vanilla-green base zombie icon family derived from the accepted model identity.
The Blender adapter's job-root allowlist and dependency lock currently list specialized zombie jobs but not the new `zombies` job, so this route must be added and verified before export.
No runtime file is to point to a reference-only or unproven provider candidate.

## Full-queue planning reserve

| Operation | Provisional credits |
| --- | ---: |
| 30 textured Meshy 7 bodies | 900 |
| About 16 known separate held or carried items | 480 |
| Rigging and up to eight suitable presets per eligible humanoid | Up to 870 |
| One possible remesh per body | Up to 150 |
| **Known-scope planning reserve** | **Up to about 2,400** |

Missing references may reveal further required held items at 30 credits each.
This reserve is not spending authorization; every model receives its own revised estimate and exact reference review before generation.
Nonhumanoid creatures use a Meshy body and Blender-authored rig and actions because the provider auto-rig route is unsuitable for their anatomy.

## Later models with confirmed reference records

| Unit mesh | Approved reference within `docs/assets/` | Preflight note |
| --- | --- | --- |
| `chaosx_forest_giants` | `012_africa/models_3d/forest_giants/refs/original/meshy_input.png` | Review exact held items before estimating. |
| `chaosx_gorilla_heavy_infantry` | `012_africa/models_3d/gorilla_heavy_infantry/refs/original/meshy_input.png` | Review exact held items before estimating. |
| `chaosx_oracle_recon` | `012_africa/models_3d/oracle_recon/refs/original/meshy_input.png` | Review exact held items before estimating. |
| `chaosx_pan_sappers` | `012_africa/models_3d/pan_sappers/refs/original/meshy_input.png` | The picture shows a cleaver-like tool while the package requires a shovel; resolve this before generation. |
| `chaosx_plague_carriers` | `012_africa/models_3d/plague_carriers/refs/original/meshy_input.png` | Review exact held items before estimating. |
| `chaosx_riverborn` | `012_africa/models_3d/riverborn/refs/original/meshy_input.png` | Review exact held items before estimating. |
| `chaosx_stone_cohorts` | `012_africa/models_3d/stone_cohorts/refs/original/meshy_input.png` | Review exact held items before estimating. |
| `cannibal_feast_cohort` | `014_cannibalism/models_3d/cannibal_feast_cohort/refs/original/meshy_input.png` | Review exact held items before estimating. |
| `cannibal_march_predation_column` | `014_cannibalism/models_3d/cannibal_march_predation_column/refs/original/meshy_input.png` | Review exact held items before estimating. |
| `cannibal_scavenger_warband` | `014_cannibalism/models_3d/cannibal_scavenger_warband/refs/original/meshy_input.png` | Review exact held items before estimating. |
| `clone_infantry` | `shared_clone_system/models_3d/clone_infantry/refs/derived/20260906_weaponfree_body.png` | Use the approved weapon-free body input and separate firearm. |

## Reference blockers

`cannibal_island_reavers` has an approval record for `refs/original/meshy_input_recovery_v9_semantic_alpha.png`, but that exact file is absent.
Its extant `meshy_input.png` has a different hash and cannot be substituted without resolving the approval record.
`black_plague_rat` has a package image at `020_black_plague/models_3d/rat_ground_unit_shared/refs/original/meshy_input.png`, but the source-free route lacks a clear approval record.
The distinct `wendigo_zombies` model is a new queue entry and requires its own approved Meshy-ready image before its turn; existing Wendigo counters do not count as a model reference.

No approved reference was found for `cannibal_feast_guard`, `cannibal_siege_eaters`, `resources_found_cave_monster`, `chaos_assault_battalion`, `chaosx_infected_zombies`, `chaosx_rabid_zombies`, `chaosx_parasitic_zombies`, `chaosx_mutant_zombies`, `chaosx_undead_zombies`, `chaosx_necrotic_zombies`, `chaosx_demonic_zombies`, `death_ghost_hosts`, `chaosx_paleogenetic_creature`, or `chaosx_temporal_guard`.
Broken-model screenshots are defect evidence only and do not resolve these reference gaps.

## Acceptance evidence for each model

Record the approved image and adaptation, actual Meshy IDs and credits, rig and animation acceptance or Blender fallback, component and texture inventory, vanilla scale comparison, exported `.mesh` and `.anim` reimport reports, multiple angle and phase renders for every required action, sound and attack effect timing, unique counter wiring, and active HOI4 entity references.
Fix every visible geometry hole, outline, texture fault, scale error, and skin deformation before offline readiness.
The user owns live-game consumer validation, so offline export and runtime wiring evidence must state that limit accurately.
