# Custom unit recording inventory

Status: source inventory only; no unit has been observed or recorded in game.
The bounded repository explorer mapped the families below from unit definitions, entity registrations and `docs/testing/chaosx_test_country.md`.
Reconcile this snapshot against current files before recording, especially ongoing Events 6, 12, 16 and 23.
This is not a complete runtime model audit and does not establish working animation, material, scale, counter or sound behavior.

Use a dedicated CXT save and the documented `e chaosx_test` entry after startup is stable.
The static roster is created by `chaosx_test_country_create_unit_roster` in `common/scripted_effects/chaosx_test_country_unit_effects.txt`.
Registered packages are dispatched by `common/scripted_effects/chaosx_test_country_effects.txt`.
Record entity identity, displayed unit name, save, location, actual actions observed, media path and a clear feature caption for each accepted clip.
Shared meshes may share a close-up clip, but every mapped unit must still be checked for selecting the intended model.

| Family | Mapped subunits or entities | Primary source |
| --- | --- | --- |
| Death ghosts | `death_weak_ghost_host`, `death_hollow_ghost_host`, `death_last_shore_ghost_host` share `death_ghost_entity` | `gfx/entities/010_death_ghost_hosts.asset` and `.gfx` |
| Africa forces | `gorilla_heavy_infantry`, `pan_sappers`, `stone_cohorts`, `riverborn`, `forest_giants`, `oracle_recon`, `plague_carriers` | `gfx/entities/012_africa_strange_forces.asset` and `.gfx` |
| Cannibal forces | `cannibal_scavenger_warband`, `cannibal_feast_guard`, `cannibal_feast_cohort`, `cannibal_bone_guard`, `cannibal_island_reavers`, `cannibal_siege_eaters`, `cannibal_march_predation_column` | `gfx/entities/014_cannibalism_units.asset` and `.gfx` |
| Cave broods | `cave_monster_brood`, `cave_stone_phalanx_brood`, `cave_burrow_war_brood`, `cave_scree_tide_brood`, `cave_anchor_guard_brood` share the canonical cave mesh through aliases | `gfx/entities/018_resources_found_cave_monster.asset` and `.gfx` |
| Plague rats | `rat_swarm`, `rat_brutes`, `rat_burrowers`, `rat_tunnelers`, `rat_carrion_guard`, `rat_dock_stowaways` share `black_plague_rat_entity` | `gfx/entities/020_black_plague_rat.asset` and `.gfx` |
| Zombies | `zombies`, `infected_zombies`, `rabid_zombies`, `parasitic_zombies`, `mutant_zombies`, `undead_zombies`, `necrotic_zombies`, `demonic_zombies` | Corresponding `gfx/entities/chaosx_*.asset` and `.gfx` families |
| Clones | `clone_infantry_entity` | `gfx/entities/clone_infantry.asset` and `.gfx` |
| Robots | `autonomous_robot_entity` | `gfx/entities/autonomous_robot.asset` and `.gfx` |
| Alien landing forces | `alien_infantry_entity`; locked landing setup requires separate confirmation | `gfx/entities/alien_infantry.asset` and `.gfx` |
| Paleogenetic creatures | `chaosx_paleogenetic_creature_entity`, conventional alias `paleogenetic_creature_entity` | `gfx/entities/paleogenetic_creature.asset` and `.gfx` |
| Chaos Battalion | `chaos_battalion_entity` uses `chaos_assault_battalion_mesh` | `gfx/entities/chaos_assault_battalion.asset` and `.gfx` |

For each family, inspect its actual state declarations before planning idle, movement, attack, defence, support attack, retreat, death and training footage.
Do not assume every family implements every state independently.
The Africa package also declares bespoke sapper, concealment, observation, water-transition and deployment actions; verify their actual consumers and available activation paths before claiming coverage.

## Unresolved inventory entries

- Zombie armored and wendigo mappings still need extraction from `common/units/zombies.txt`.
- `disaster_wardens` has a model directory, but its exact entity registration was not confirmed by the bounded exploration.
- `chaosx_elephant` uses vanilla `elephantry`; the separate custom model directory is not proof of a current runtime consumer.
- `coal_golem`, `cannibal_bone_riders` and `cannibal_network_cadre` use generic infantry or cavalry sprites.
- `aryan_clone_infantry_entity` clones vanilla `GER_infantry_entity`.
- Event 016 `portal_raider`, `xenobiological_assault_organism` and `temporal_guard` did not have confirmed custom entity files in the captured evidence.
- Event 039 assassin forces have CXT/provider wiring, but custom entity registrations were not confirmed.
- Chemical tank variants, Livens projector variants and CBRN support families need exact sprite-to-entity reconciliation.
- Exact `essential` and `need` equipment fields remain to be mapped where division composition determines the displayed entity.
- The building beacon `building_anomaly_signal_beacon_pilot` is a separate facility showcase, not a land-unit recording entry.

These entries remain pending checks, not confirmed missing-asset bugs.
All clips and teaser captions remain pending the clean-startup gate and actual runtime observation.
