# Event 012 strange-force unit runtime notes

Unit definitions are in `common/units/012_africa_strange_forces.txt`, with equipment in `common/units/equipment/012_africa_strange_force_equipment.txt`.

The orchestrator's live QA on 2026-10-03 confirms that `pan_sappers` and `oracle_recon` are support companies.
HOI4 displays a division's line-battalion entity on the map, so these two support companies' custom models do not appear as division models.
Their support-company gameplay, equipment, counters, and icon consumers remain applicable.
This is a known native display limitation, not proof of missing model files or a reason to promote the support companies into line battalions.
No unit redesign, composition change, model replacement, or animation change is made by this note.

## Package availability

The eight strange formations (gorilla heavy infantry, pan sappers, stone cohorts, riverborn, forest giants, oracle recon, disaster wardens, and plague carriers) are installed and available.
`africa_register_strange_force_asset_manifests` in `common/scripted_effects/012_africa_strange_force_manifest_effects.txt` sets the 32 per-family model, entity, counter, and audio receipts and then `africa_strange_formation_package_ready` in one effect.
It runs on startup, so new games and loaded saves receive the flags, and again when the Event 012 host is initialised.

| Formation | Template entity (`override_model`) | Technology | Counter |
| --- | --- | --- | --- |
| Gorilla Heavy Infantry | `chaosx_gorilla_heavy_infantry_entity` | `africa_gorilla_heavy_infantry_tech` | `GFX_unit_gorilla_heavy_infantry_icon_medium` |
| Pan Sappers | `chaosx_pan_sappers_entity` | `africa_pan_sappers_tech` | `GFX_unit_pan_sappers_icon_medium` |
| Stone Cohorts | `chaosx_stone_cohorts_entity` | `africa_stone_cohorts_tech` | `GFX_unit_stone_cohorts_icon_medium` |
| Riverborn | `riverborn_entity` | `africa_riverborn_tech` | `GFX_unit_riverborn_icon_medium` |
| Forest Giants | `chaosx_forest_giants_entity` | `africa_forest_giants_tech` | `GFX_unit_forest_giants_icon_medium` |
| Oracle Recon | `chaosx_oracle_recon_entity` | `africa_oracle_recon_tech` | `GFX_unit_oracle_recon_icon_medium` |
| Disaster Wardens | `infantry_entity` (accepted vanilla override) | `africa_disaster_wardens_tech` | `GFX_unit_disaster_wardens_icon_medium` |
| Plague Carriers | `plague_carriers_entity` | `africa_plague_carriers_tech` | `GFX_unit_plague_carriers_icon_medium` |

The open gate enables Actions 74-76, every `africa_strange_force_spawn_guard` caller (the Riverborn focus route, the promoted Tier A calls, and the Event 013 Disaster Warden follow-up), the AI strange-force action pool, and nonhuman-formation achievement credit.
The eight-formation cap and per-family cooldowns in the spawn guard still apply.
The agent decision and its basis are recorded as L2 in `docs/plans/012_africa_plans/agent_decisions_2026-10-04.md`.

## Elephant map model blocker

Disposition: `blocked` for players without the DLC that supplies the vanilla Elephantry entity.
The orchestrator's live CXT QA on 2026-10-03 at 19:15 found every Africa elephant division displayed as the engine's placeholder box, with 24 occurrences of `[provincegraphics.cpp:248]: Missing entity for 'chaosx_elephant or elephantry' deploying placeholder box!`.
`common/units/012_africa_elephant_forces.txt` binds `chaosx_elephant` to `sprite = elephantry`, and the committed mod has no `chaosx_elephant_entity` fallback.
The vanilla entity therefore does not provide a model for this no-DLC configuration.

The parent is commissioning a real shared `chaosx_elephant` model under row 18 of [the unit model rework plan](../../plans/system_unit_model_rework_plans/unit_model_rework_plan.md).
That deliverable is `accepted and queued` on the orchestrator's explicit 2026-10-03 instruction; the rendering blocker remains open until the commissioned mesh, actions, and entity are shipped and their division consumer is verified.
The archival `docs/assets/012_africa/models_3d/elephant_shared_base/` package is not a runtime fallback.
This documentation records the supplied live evidence and leaves model production and runtime wiring with the parent.
