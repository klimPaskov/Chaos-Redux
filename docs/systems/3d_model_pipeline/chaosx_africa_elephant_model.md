# Event 012 shared elephant model package

The package preserves one shared oversized elephant body for the live Event 012 armoured elephant subunit. `chaosx_elephant` is a custom unit distinct from vanilla `elephantry`; its logistics and shock roles share this body and differ through the parent-owned formation and equipment contract. The rider is calibrated to one full installed vanilla infantry runtime model, so the exported creature is intentionally monumental rather than a miniature unit marker.

## Runtime package

The parent-owned runtime files live under `gfx/models/units/chaosx_elephants/`. The mesh is `chaosx_elephant_shared_base.mesh`, the packed maps are `elephant_shared_base_diff.dds`, `elephant_shared_base_spec.dds`, and `elephant_shared_base_n.dds`, and the six skeletal actions are registered by `animation_chaosx_elephants.asset`.

`gfx/entities/chaosx_elephants.gfx` registers the mesh and action names. `gfx/entities/chaosx_elephants.asset` provides the shared entity with `scale = 0.8`; `common/units/012_africa_elephant_forces.txt` consumes it through `sprite = chaosx_elephant_shared_base`.

The exact source, checkpoints, provider lineage, scale crosswalk, reimport proofs, previews, and audio provenance remain in `docs/assets/012_africa/models_3d/elephant_shared_base/` and the tracked handoff under `docs/plans/012_africa_plans/subagent_handoffs/`.

## Scale and actions

The vanilla infantry source mesh is `7.3518242835` units high and uses entity scale `0.8`, giving an effective rider height of `5.8814594268`. The exported elephant source height is `33.5147094727` units. Parent consumers must apply the entity scale exactly once.

The six real skeletal actions are `idle`, `move`, `deploy`, `supply_load`, `attack`, and `impact`. All six have exported `.anim` files and reimport proofs. The live unit uses the same action set for host and Action 102 member guards; future logistics and shock loadouts may continue to share this body without commissioning a second elephant model.

## Audio

`sound/chaosx_elephants_sound.asset` declares the six role-specific soundeffects and runtime WAVs under `sound/012_africa/elephant/`. The originals, licenses, transformations, checksums, and animation synchronization points are recorded in the job audio handoff. No audio was synthesized.

The custom-unit counter companion is registered in `interface/chaosx_subuniticons.gfx` under both the shared body token and the live `chaosx_elephant` token. It uses `gfx/interface/counters/divisions_large/unit_elephant_shared_base_icon.dds` plus `gfx/interface/counters/divisions_small/onmap_unit_elephant_shared_base_icon.dds`, both with the installed two-frame land-counter contract.

## Runtime status

The model package does not add a new country tag or a second elephant model. Event 012 calls `africa_elephant_prepare_host_guard` for the preserved host and `africa_elephant_prepare_member_guard` for every promoted Action 102 member. The five member force profiles each include one `chaosx_elephant` regiment, while the host receives the two-battalion Africa Charter Elephant Guard. The provider shell's recorded open-boundary topology and the shared silhouette remain review items in the job manifest.
