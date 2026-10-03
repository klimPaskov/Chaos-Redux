# Event 012 strange-force unit runtime notes

Unit definitions are in `common/units/012_africa_strange_forces.txt`, with equipment in `common/units/equipment/012_africa_strange_force_equipment.txt`.

The orchestrator's live QA on 2026-10-03 confirms that `pan_sappers` and `oracle_recon` are support companies.
HOI4 displays a division's line-battalion entity on the map, so these two support companies' custom models do not appear as division models.
Their support-company gameplay, equipment, counters, and icon consumers remain applicable.
This is a known native display limitation, not proof of missing model files or a reason to promote the support companies into line battalions.
No unit redesign, composition change, model replacement, or animation change is made by this note.

## Elephant map model blocker

Disposition: `blocked` for players without the DLC that supplies the vanilla Elephantry entity.
The orchestrator's live CXT QA on 2026-10-03 at 19:15 found every Africa elephant division displayed as the engine's placeholder box, with 24 occurrences of `[provincegraphics.cpp:248]: Missing entity for 'chaosx_elephant or elephantry' deploying placeholder box!`.
`common/units/012_africa_elephant_forces.txt` binds `chaosx_elephant` to `sprite = elephantry`, and the committed mod has no `chaosx_elephant_entity` fallback.
The vanilla entity therefore does not provide a model for this no-DLC configuration.

The parent is commissioning a real shared `chaosx_elephant` model under row 18 of [the unit model rework plan](../../plans/system_unit_model_rework_plans/unit_model_rework_plan.md).
That deliverable is `accepted and queued` on the orchestrator's explicit 2026-10-03 instruction; the rendering blocker remains open until the commissioned mesh, actions, and entity are shipped and their division consumer is verified.
The archival `docs/assets/012_africa/models_3d/elephant_shared_base/` package is not a runtime fallback.
This documentation records the supplied live evidence and leaves model production and runtime wiring with the parent.
