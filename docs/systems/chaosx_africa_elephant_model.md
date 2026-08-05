# Event 012 shared elephant model package

The Africa event uses one shared oversized elephant body for the logistics and shock elephant consumers. The rider is calibrated to one full installed vanilla infantry runtime model, so the exported creature is intentionally monumental rather than a miniature unit marker.

## Runtime package

The parent-owned runtime files live under `gfx/models/units/chaosx_elephants/`. The mesh is `chaosx_elephant_shared_base.mesh`, the packed maps are `elephant_shared_base_diff.dds`, `elephant_shared_base_spec.dds`, and `elephant_shared_base_n.dds`, and the six skeletal actions are registered by `animation_chaosx_elephants.asset`.

`gfx/entities/chaosx_elephants.gfx` registers the mesh and action names. `gfx/entities/chaosx_elephants.asset` provides the shared entity with `scale = 0.8`; unit definitions remain responsible for selecting the entity through their sprite or template consumer.

The exact source, checkpoints, provider lineage, scale crosswalk, reimport proofs, previews, and audio provenance remain in `docs/assets/012_africa/models_3d/elephant_shared_base/` and the tracked handoff under `docs/plans/012_africa_plans/subagent_handoffs/`.

## Scale and actions

The vanilla infantry source mesh is `7.3518242835` units high and uses entity scale `0.8`, giving an effective rider height of `5.8814594268`. The exported elephant source height is `33.5147094727` units. Parent consumers must apply the entity scale exactly once.

The six real skeletal actions are `idle`, `move`, `deploy`, `supply_load`, `attack`, and `impact`. All six have exported `.anim` files and reimport proofs. Logistics and shock variants share this body; they may differ through parent-owned formation, cargo, or role logic without commissioning a second elephant body.

## Audio

`sound/chaosx_elephants_sound.asset` declares the six role-specific soundeffects and runtime WAVs under `sound/012_africa/elephant/`. The originals, licenses, transformations, checksums, and animation synchronization points are recorded in the job audio handoff. No audio was synthesized.

The custom-unit counter companion is registered in `interface/chaosx_subuniticons.gfx` and uses `gfx/interface/counters/divisions_large/unit_elephant_shared_base_icon.dds` plus `gfx/interface/counters/divisions_small/onmap_unit_elephant_shared_base_icon.dds`, both with the installed two-frame land-counter contract. Logistics and shock consumers intentionally share these counter bytes.

## Remaining parent wiring

The model package does not add a new country tag or a second elephant model. A parent unit/template surface still needs to select `chaosx_elephant_shared_base_entity` for the intended elephant consumers and perform live in-game validation. The provider shell's recorded open-boundary topology and the shared silhouette are retained as review items in the job manifest.
