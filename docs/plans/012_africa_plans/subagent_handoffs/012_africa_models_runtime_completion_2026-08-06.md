# Event 012 Africa strange formations model completion handoff

Date: 2026-08-06.

Status: the eight historical model packages are complete through their archived Meshy provider lineage, Blender/io_pdx_mesh export, five 30 FPS skeletal actions, DDS processing, and reimport proof. Parent integration installed the entity, bespoke counter, source-audio, and readiness receipts after this bounded model handoff. Meshy 7 is required for future generation.

## Shared production contract

Each package uses exactly one archived reference image, archived Meshy image-to-3D GLB and FBX outputs, the measured vanilla `asian_infantry.mesh` height of `7.516803`, entity scale `1.0`, a `25,000` triangle runtime candidate, semantic rigging, root-channel grounding, PDX `.mesh`, five `.anim` exports, DDS maps, and per-action Blender reimport proofs. No new country tag, generic visual alias, copied runtime mesh, generated audio, or placeholder counter was used.

## Completed packages

| Subunit | Runtime mesh | Entity token | Target height | Actions | Provider task |
| --- | --- | --- | ---: | --- | --- |
| `gorilla_heavy_infantry` | `chaosx_gorilla_heavy_infantry` | `chaosx_gorilla_heavy_infantry_entity` | 10.147684 | idle, move, attack, recovery, death | `019fd7f3-6f53-73d5-a5d3-1f46256b2759` |
| `pan_sappers` | `chaosx_pan_sappers` | `chaosx_pan_sappers_entity` | 7.516803 | idle, move, sabotage, construction, death | `019fd7f9-ee23-7510-82c6-7685ec2e3089` |
| `stone_cohorts` | `chaosx_stone_cohorts` | `chaosx_stone_cohorts_entity` | 11.275205 | idle, move, attack, collapse recovery, death | `019fd7ae-83a0-792c-8a2e-c1199c678f6d` |
| `forest_giants` | `chaosx_forest_giants` | `chaosx_forest_giants_entity` | 18.792008 | idle, move, attack, concealment/emergence, death | `019fd806-1803-7d29-9e52-82c49d6c7a2d` |
| `oracle_recon` | `chaosx_oracle_recon` | `chaosx_oracle_recon_entity` | 8.268483 | idle, move, recon, observation, death | `019fd806-23e2-7ecf-88e9-4d8e9e884a80` |
| `riverborn` | `chaosx_riverborn` | `riverborn_entity` | 9.396004 | idle, move, attack, water transition, death | `019fd806-2e78-78aa-8876-fca8862d729d` |
| `disaster_wardens` | `chaosx_disaster_wardens` | `disaster_wardens_entity` | 9.396004 | idle, move, rescue, containment, death | `019fd806-39bf-7d2c-9c77-5dd1cad77011` |
| `plague_carriers` | `chaosx_plague_carriers` | `plague_carriers_entity` | 8.268483 | idle, move, deploy, release/containment, death | `019fd7b5-ab43-7715-8dc8-d4a3bc8fcabe` |

## Runtime staging

The final mesh, five animations, three DDS maps, and source/final manifests are present in each `docs/assets/012_africa/models_3d/<subunit>/` package. The same binary outputs are staged under `gfx/models/units/012_africa_<subunit>/`. Entity and mesh registrations are in `gfx/entities/012_africa_strange_forces.asset` and `gfx/entities/012_africa_strange_forces.gfx`; animation registrations are in `gfx/models/units/012_africa_strange_forces/animation_012_africa_strange_forces.asset`.

## Parent activation completion

The bespoke counters are registered in `interface/012_africa_strange_force_counters.gfx`, the final DDS files are installed under `gfx/interface/counters/`, and all 49 sourced sound roles are defined in `sound/012_africa_strange_forces_sound.asset`. Animation events, formation-entry cues, and the plague-carrier impact cue provide a runtime consumer for every soundeffect ID. Startup calls `africa_register_strange_force_asset_manifests`, which sets each exact model, entity, counter, and audio receipt before setting `africa_strange_formation_package_ready`. The existing scripted spawn guards still refuse cleanly if any receipt is absent, and no branch substitutes another model or unit.

The runtime cross-reference audit found zero missing mesh, animation, pdxmesh, sound, or counter paths. Every entity animation ID resolves to its registered mesh animation, and every one of the 49 soundeffect IDs has an entity or scripted consumer. Live visual and audio validation remains outside the agent task by user direction.
