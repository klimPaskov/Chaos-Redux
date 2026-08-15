# Shared Autonomous Robot System

## Purpose

The Autonomous Robot family is a provider-neutral military API for Event 016, Event 019, and future events.

The runtime identifiers are `autonomous_robot`, `autonomous_robot_equipment`, and `autonomous_robot_equipment_1`; none of them encode Warren Kruger or another provider.

## Gameplay behavior

`autonomous_robot` is a two-width armored line battalion combining infantry-like organization with tank-grade protection and assault power. It belongs to both the armor and mechanized-infantry modifier families, so appropriate bonuses from either family affect the chassis.

Its production equipment provides 88% hardness, 70 armor, 60 breakthrough, 50 defense, 36 soft attack, 30 hard attack, 75 piercing, 8 air attack, 7 km/h speed, and 92% reliability before technology bonuses.

Each battalion requires 50 combat robots and 10 support equipment, uses only 50 manpower, and retains terrain penalties in forests, jungles, and marshes so the family remains strongest in open mechanized warfare.

The hidden operational technology `brilliant_scientist_robot_formations_tech` enables the generic equipment and battalion and grants a further +75% hard attack, +75% breakthrough, +60% defense, and +10 organization.

The dependency-safe upgrade `brilliant_scientist_robot_formations_weaponization_tech` adds another +75% hard attack, +75% breakthrough, and +35% reliability.

## Provider API

Event 016 grants the operational and weaponization technologies through `chaosx_grant_custom_operational_technology` and `chaosx_grant_custom_technology_upgrade` with the robot-family selectors documented in `docs/events/016_brilliant_scientist/systems/custom_technology_api.md`.

Other events may use those same public effects without creating Kruger, setting Directorate state, or duplicating the technology ledger.

Event 019 provider family 505 consumes the same battalion and equipment definitions for spawn, training, sustainment, derivative inheritance, accounting, and cleanup.

## Visual and audio implementation

The generic 3D consumer is `autonomous_robot_entity`, backed by `autonomous_robot_mesh` and reimport-proven idle, move, attack, defend, support-attack, retreat, training, and destruction actions.

The installed model is a retro-industrial armored humanoid with a machine gun integrated into each forearm and no provider, country, or event insignia. It uses a 29,971-triangle working mesh, a 24-bone sanitized rig, 1024-pixel packed PDX textures, and entity scale 0.8 against the installed vanilla infantry calibration.

The counter sprites are `GFX_group_autonomous_robot_icon`, `GFX_unit_autonomous_robot_icon_medium`, and `GFX_unit_autonomous_robot_icon_medium_white` in `interface/autonomous_robot_system.gfx`.

The equipment art sprite is `GFX_autonomous_robot_equipment_medium` and the operational and weaponization technology icons use their exact `<technology>_medium` sprite names.

Runtime model files are installed under `gfx/models/units/autonomous_robot/`, entity definitions under `gfx/entities/`, sourced audio under `sound/shared_robot_system/autonomous_robot/`, and sound definitions under `sound/autonomous_robot_sound.asset`.

Move and retreat synchronize the licensed servo and armored-footfall package. Attack and support attack synchronize the licensed dual-MG burst to the visible forearm recoil, idle uses the mechanical loop, and death uses the destruction recording. The immutable evidence derivatives remain OGG files; runtime copies are deterministically converted to the installed positional-unit precedent of 44.1 kHz, mono, 16-bit PCM WAV. The provider-neutral selection one-shot is registered as `autonomous_robot_select_sfx`; HOI4 exposes ordinary land-unit selection through country/original-tag infantry voice templates rather than a subunit entity callback, so it is deliberately not assigned to a country-wide voice token that would replace ordinary infantry voices.

The production manifest, provider lineage, animation contact sheets, io_pdx_mesh reimport evidence, source-audio licences, transformations, and checksums are preserved under `docs/assets/shared_robot_system/models_3d/autonomous_robot/`. The permanent production handoff is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/autonomous_robot_3d_model_handoff.md`.

## Required icons

- `gfx/interface/technologies/shared_robot_system/autonomous_robot_equipment.dds` — `GFX_autonomous_robot_equipment_medium` in `interface/autonomous_robot_system.gfx`.
- `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_robot_formations.dds` — `GFX_brilliant_scientist_robot_formations_tech_medium` in `interface/016_brilliant_scientist_hidden_technologies.gfx`.
- `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_robot_formations_weaponization.dds` — `GFX_brilliant_scientist_robot_formations_weaponization_tech_medium` in the same GFX file.
- `gfx/interface/counters/divisions_large/unit_autonomous_robot_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_autonomous_robot_icon.dds` — the three counter sprites in `interface/autonomous_robot_system.gfx`.

## Future plans

Future events can add alternate robot refinements by granting new dependency-safe hidden technologies that modify `autonomous_robot`; they should not fork the subunit, equipment, entity, counter, or base model unless their gameplay and silhouette are genuinely different.

Possible extensions include robot-specific repair logistics, electronic-warfare disruption, captured production-line recovery, and specialized anti-fortification or anti-air variants.
