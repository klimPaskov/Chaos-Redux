# Demonic Zombies model manifest

## Current production disposition

Status: `ready_for_user_live_validation`.

This package uses one approved portrait-matched reference image and Meshy 7 geometry. It is complete through Blender processing, PDX material conversion, rigging, real skeletal actions, `.mesh`/`.anim` export, per-action reimport proof, runtime promotion, sound handoff, and bespoke counter promotion.

- Sub-unit: `demonic_zombies`.
- Mesh stem: `chaosx_demonic_zombies`.
- Entity: `chaosx_demonic_zombies_entity`.
- PDX mesh: `chaosx_demonic_zombies_mesh`.
- Provider model: `meshy-7`, recorded in `job.yaml#provider_plan.resolved_ai_model`.
- Sole provider input: `refs/original/meshy_input.png`; its one-image gate and checksum remain recorded in `input_manifest.json`.
- Rig/action route: `custom winged-biped creature rig/action route`.
- The creature segmentation report retains 296 renderable components and records 47 discarded zero-face fragments. Each creature action passed the positive ground-clearance gate.

## Export and runtime surfaces

- Mesh: `export/mesh/chaosx_demonic_zombies.mesh` and `gfx/models/units/chaosx_demonic_zombies/chaosx_demonic_zombies.mesh`.
- Actions: `export/anim/chaosx_demonic_zombies_{idle,move,attack,death}.anim` and matching runtime files.
- Materials: `textures/dds/texture_0.dds`, `texture_normal.dds`, and `texture_specular.dds`, synchronized into the runtime model folder.
- Reimport evidence: `validation/reimport_chaosx_demonic_zombies_*.json`.
- Entity/GFX: `gfx/entities/chaosx_demonic_zombies.asset` and `gfx/entities/chaosx_demonic_zombies.gfx`.
- Unit binding: `common/units/zombies.txt#demonic_zombies` uses `sprite = chaosx_demonic_zombies`.
- Counters: bespoke large and small DDS files are promoted to the paths registered in `interface/chaosx_subuniticons.gfx`.
- Audio: action states use the zombie soundeffects, and selection uses the exact `ZZZ_infantry_idle` consumer in the `Voices` category. Selection is intentionally tag/original-tag scoped because HOI4 infantry selection voices are not sprite-specific.

## Preservation boundary

The base `zombies` unit remains on `sprite = zombies`. The armored undead, necrotic, and demonic variants intentionally reuse their matching specialized parent sprites while retaining `map_icon_category = armored`. Runtime package readiness is proven by source/export/reimport evidence; live HOI4 playback and visual acceptance remain user-owned.
