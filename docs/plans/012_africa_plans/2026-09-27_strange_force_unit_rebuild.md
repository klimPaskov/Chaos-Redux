# Africa strange-force unit rebuild: forest giants, stone cohorts, pan sappers, gorilla heavy infantry, oracle recon, riverborn (2026-09-27)

Disposition: `implemented` — six rebuilt models, eight actions each, separately generated held items, textures, entities, and timed sounds are installed; in-game validation belongs to the user.
Acceptance basis: the user approved the unit-model rework on 2026-09-27 (Meshy body, one rig and preset set, separately generated held items, full wiring, reimport QA) and asked that every remaining model be finished thoroughly.

## Why the old models were replaced

The shipped models had five actions each and aliased `defend`, `support_attack`, `retreat`, and `training` onto them; the forest giants were static T-poses, and the weapons were fused into the bodies.

## References

Each unit has an item-free full-body reference `docs/assets/012_africa/models_3d/<unit>/refs/original/meshy_input_v3.png` built from the unit's existing art, and one item-only reference per held item under `refs/equipment/<item>/`.
The halberd and shield were regenerated once (`meshy_input_v2.png`) because the first versions carried artifacts.

## Provider route and credits

Meshy 7 body, one rig, six presets, and two prime text-to-motion actions per unit, plus one Meshy 7 task per held item.
The stone cohort's first death preset (Knock Down) flipped the heavy golem legs over head and was replaced by Fall Dead from Abdominal Injury (preset 188).
Every task and cost is in `docs/plans/system_unit_model_rework_plans/credit_ledger.json`: 79 credits for the item-free pan sappers, 109–112 for the one-item units, and 139 for the riverborn with spear and shield, against the 105-credit route B ceiling.
The forest giants, stone cohorts, and gorilla are built 1.3×, 1.25×, and 1.15× the vanilla infantry source height (`prepare.height_scale`), so they tower over infantry at the shared entity scale.

| Unit | Held items | Carrying bone |
| --- | --- | --- |
| forest giants | vine-bound stone axe | right hand |
| stone cohorts | iron halberd (two-handed) | right hand, left hand measured on the shaft |
| pan sappers | none (charges are worn on the coat) | — |
| gorilla heavy infantry | riveted warhammer (two-handed) | right hand, left hand measured on the shaft |
| oracle recon | skull-crowned staff | right hand |
| riverborn | spear and spiral bronze shield | right hand; left forearm |

## Item fitting

`lab_items.py` fitted each item, packed body and item textures into one atlas per unit, and joined the items to the body with a rigid weight on the carrying bone.
Its measured floor correction re-keyed only the carrying bone on frames where an item sank below the floor (slams, deaths, prostrations); per-action fixed frame counts are in each `blender/working/v3/review/items_v2/items_report.json`.

## Export and runtime

Each unit was grounded with `lab_finalize`, partitioned, exported, and reimport-proven for all eight roles with `export_package.py`, then installed hash-identical into `gfx/models/units/012_africa_<unit>/` and registered with `wire_unit.py`, which retired the old blocks from the shared `012_africa_strange_forces` files (only the plague carriers remain there).
Entities are `gfx/entities/chaosx_<unit>.asset`; the riverborn keeps the entity name `riverborn_entity` that its `sprite = riverborn` resolves to.
Event times come from the phase review, one event per measured strike, plant, slam, or landing, using each unit's existing sourced sound effects in `sound/012_africa_strange_forces_sound.asset`.

## Remaining limits

- Two-handed weapons follow the provider's empty-handed arm motion: the gorilla's and stone cohort's off hand reaches the shaft in the strikes (0.2–0.3 units) but drifts away in idle and walking poses.
- The gorilla's two-fisted ground pound still dips the hammer head 0.3 units (about 4% of height) below the floor, because the wrist itself touches the ground there.
- The forest giant's axe-slam training reimports 0.1 units below the floor at the impact frame.
- Counter art was not changed; the rebuilt bodies follow the same designs, but a counter refresh may be wanted.
- No listening tool can confirm loudness balance in game.
