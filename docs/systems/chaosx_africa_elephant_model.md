# Event 012 shared elephant model package

The package preserves one shared oversized elephant body for possible future logistics and shock consumers. Event 012 deliberately leaves this custom body dormant; any currently available elephant battalion remains on the installed vanilla unit path. The rider is calibrated to one full installed vanilla infantry runtime model, so the exported creature is intentionally monumental rather than a miniature unit marker.

## Runtime package

The parent-owned runtime files live under `gfx/models/units/chaosx_elephants/`. The mesh is `chaosx_elephant_shared_base.mesh`, the packed maps are `elephant_shared_base_diff.dds`, `elephant_shared_base_spec.dds`, and `elephant_shared_base_n.dds`, and the six skeletal actions are registered by `animation_chaosx_elephants.asset`.

`gfx/entities/chaosx_elephants.gfx` registers the mesh and action names. `gfx/entities/chaosx_elephants.asset` provides the shared entity with `scale = 0.8`; it has no live unit-definition or division-template consumer by design.

The exact source, checkpoints, provider lineage, scale crosswalk, reimport proofs, previews, and audio provenance remain in `docs/assets/012_africa/models_3d/elephant_shared_base/` and the tracked handoff under `docs/plans/012_africa_plans/subagent_handoffs/`.

## Scale and actions

The vanilla infantry source mesh is `7.3518242835` units high and uses entity scale `0.8`, giving an effective rider height of `5.8814594268`. The exported elephant source height is `33.5147094727` units. Parent consumers must apply the entity scale exactly once.

The six real skeletal actions are `idle`, `move`, `deploy`, `supply_load`, `attack`, and `impact`. All six have exported `.anim` files and reimport proofs. If a future design activates the package, logistics and shock variants can share this body; they may differ through parent-owned formation, cargo, or role logic without commissioning a second elephant body.

## Audio

`sound/chaosx_elephants_sound.asset` declares the six role-specific soundeffects and runtime WAVs under `sound/012_africa/elephant/`. The originals, licenses, transformations, checksums, and animation synchronization points are recorded in the job audio handoff. No audio was synthesized.

The custom-unit counter companion is registered in `interface/chaosx_subuniticons.gfx` and uses `gfx/interface/counters/divisions_large/unit_elephant_shared_base_icon.dds` plus `gfx/interface/counters/divisions_small/onmap_unit_elephant_shared_base_icon.dds`, both with the installed two-frame land-counter contract. No current unit consumes these counter bytes; they are retained for a future approved consumer.

## Dormant status

The model package does not add a new country tag or a second elephant model. Parent unit/template wiring is intentionally deferred, so the custom entity must remain unselected until a future Africa formation design approves its use. The provider shell's recorded open-boundary topology and the shared silhouette remain review items in the job manifest.
