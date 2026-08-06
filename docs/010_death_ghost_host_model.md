# Death Ghost Host Shared Unit Model

## Purpose

Death is intended to use one dedicated spectral infantry model for every Death ghost host sub-unit.

The shared binding preserves separate gameplay values for the weak host, hollow host, and Last Shore host while giving them one consistent battlefield appearance.

## Intended consumers

The complete Death consumer set is `death_weak_ghost_host`, `death_hollow_ghost_host`, and `death_last_shore_ghost_host` in `common/units/010_death_ghost_hosts.txt`.

The intended shared sprite is `death_ghost`, and the intended shared entity is `death_ghost_entity`.

All three unit definitions use the shared `death_ghost` sprite, which resolves to `death_ghost_entity`.

## Model package

The deterministic production job is `docs/assets/010_death/models_3d/ghost_hosts/`.

The package uses one native ImageGen reference at `refs/original/meshy_input.png`, Meshy 6 generation, Blender 5.1.2, the locked `chaosx_blender_hoi4` adapter, and `io_pdx_mesh`.

The mesh was calibrated against the installed western European infantry reference at source height `7.3518242835` with entity scale `0.8`, giving effective runtime height `5.8814594268`.

The candidate exports and evidence are preserved under `export/`, `textures/`, `blender/`, `provider/`, `runtime/`, `sound/`, and `validation/` in the job root.

The existing candidate passed the correction and reimport gates without model regeneration. The final working weights have a maximum of four influences, move and death pass ground-contact checks, and the preserved provider run action was retimed from 30 FPS to an accepted 24 FPS retreat action through the locked adapter route.

The exact evidence is recorded in `docs/assets/010_death/models_3d/ghost_hosts/validation/package_report.md` and the resolved route record is in `docs/assets/010_death/models_3d/ghost_hosts/validation/correction_route_blocker.md`.

## Intended runtime files

After correction, the parent-owned runtime destinations are `gfx/entities/010_death_ghost_hosts.gfx`, `gfx/entities/010_death_ghost_hosts.asset`, and `gfx/models/units/death_ghost_hosts/animation_death_ghost_hosts.asset`.

The model destination is `gfx/models/units/death_ghost_hosts/death_ghost_hosts.mesh`.

The texture destinations are `gfx/models/units/death_ghost_hosts/death_ghost_hosts_diffuse.dds`, `gfx/models/units/death_ghost_hosts/death_ghost_hosts_specular.dds`, and `gfx/models/units/death_ghost_hosts/death_ghost_hosts_normal.dds`.

The intended state mapping is idle and training to idle, move to move, attack/defend/support attack to attack, retreat to retreat, and death to death.

The accepted mesh, five animations, three model textures, six sourced WAVs, and three counter DDS files are copied into runtime. The rejected overweight mesh remains isolated under `docs/assets/010_death/models_3d/ghost_hosts/export/mesh/rejected/` and is not referenced by runtime.

## Counters and icons

The bespoke counter package is complete as a separate parent handoff under `docs/assets/010_death/models_3d/ghost_hosts/counter_handoff/`.

The large counter is `counter_handoff/dds/gfx/interface/counters/divisions_large/unit_death_ghost_icon.dds` and is intended to register as `GFX_unit_death_ghost_icon_medium` in `interface/chaosx_subuniticons.gfx`.

The on-map counter is `counter_handoff/dds/gfx/interface/counters/divisions_small/onmap_unit_death_ghost_icon.dds` and is intended to register as `GFX_unit_death_ghost_icon_medium_white` in `interface/chaosx_subuniticons.gfx`.

The small text counter is `counter_handoff/dds/gfx/texticons/unit_death_ghost_icon_small.dds` and is intended to register as `GFX_unit_death_ghost_icon_small` in `interface/chaosx_texticons.gfx`.

All three counter surfaces use the same two-frame vanilla-green source family and have DDS round-trip evidence in `counter_handoff/validation/dds_roundtrip.json`.

## Audio

The model job contains source-only Internet audio candidates and provenance for selection, movement, idle, attack, impact, and death roles.

Audio source pages, licenses, checksums, conversions, and proposed sound identifiers are recorded in `docs/assets/010_death/models_3d/ghost_hosts/sound/handoff.md`.

Parent-owned runtime sound definitions and entity sound events are wired in `sound/010_death_ghost_hosts_sound.asset` and `gfx/entities/010_death_ghost_hosts.asset`. The death candidate remains a creative-review item because the source is a recognizable Wilhelm scream.

## Future plans

The first accepted package should keep one shared ghost silhouette across all three Death stages and vary only gameplay stats and host context.

Later work can add controlled visual progression, spectral effects, and bespoke equipment silhouettes without changing the shared entity contract.

Live HOI4 rendering, consumer verification, counter appearance, and final audio balance remain user-owned because the coding agent does not launch the game.
