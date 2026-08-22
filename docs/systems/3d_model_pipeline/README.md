# 3D model pipeline documentation

This directory contains shared 3D production contracts and durable runtime handoffs for models or sound packages used by Chaos Redux.

## Pipeline contracts

- [`overview.md`](overview.md) describes the shared production, conversion, export, and validation workflow.
- [`chaosx_3d_runtime_contract.md`](chaosx_3d_runtime_contract.md) records the runtime ownership boundary for model, entity, animation, material, and consumer wiring.

## Shared and event-consumed packages

- [`chaos_warfare_facility_models.md`](chaos_warfare_facility_models.md) documents the shared Chaos Warfare facility models.
- [`chaosx_camp_building_models.md`](chaosx_camp_building_models.md) documents the shared camp-building model family.
- [`chaosx_chaos_assault_battalion_model.md`](chaosx_chaos_assault_battalion_model.md) documents the Chaos Assault Battalion model package.
- [`clone_equipment_and_infantry.md`](clone_equipment_and_infantry.md) documents shared clone equipment and infantry presentation.
- [`chaosx_africa_elephant_model.md`](chaosx_africa_elephant_model.md) documents the Event 012 elephant package that is maintained through the shared pipeline.
- [`resources_found_cave_monster_model.md`](resources_found_cave_monster_model.md) documents the Event 018 cave-monster runtime contract.
- [`chaosx_zombie_unit_sound_design.md`](chaosx_zombie_unit_sound_design.md) documents the zombie unit sound package associated with its model consumer.

Event-specific design intent remains in the owning event package. This directory keeps the reusable production contract and durable runtime package facts.
