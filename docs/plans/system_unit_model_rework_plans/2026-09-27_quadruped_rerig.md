# Quadruped re-rig: Oth-Kesh cave monster and plague carrier donkey (2026-09-27)

Disposition: `implemented` — both quadrupeds keep their shipped meshes and textures and now play eight distinct authored actions; in-game validation belongs to the user.
Acceptance basis: the user approved the unit-model rework on 2026-09-27 and asked that every remaining model be finished thoroughly.

## Why

The provider rig and motion route only covers bipeds.
A triage with the fixed review tool showed the cave monster completely static in all four actions (it was skinned to an elephant template rig with trunk, howdah, and rider bones) and the plague carrier donkey barely moving its legs in its walk, with near-static idle and deploy.
Both meshes were worth keeping, so no provider credits were spent.

## Route

`lab_limbs.py` `import` brought each shipped `.mesh` into a working blend (images packed, objects tagged for the adapter).
The cave monster got a new 19-bone creature skeleton on joints measured from its leg pieces (`skeleton` mode, whole-mesh heat weights); the donkey kept its sensible 25-bone rig, with explicit ground tips for the stub-tailed hooves.
Eight actions per creature were authored with `keys`: a four-beat walk (rear right, front left, rear left, front right) with body bob, its reverse for retreat, idle, a defensive crouch or shy, and creature-specific attacks (the cave monster's lunge and bite, rear-and-slam, and pawing; the donkey's stamping with the basket swinging, rear-and-stamp release, and pawing), and a collapse for the death.
The measured `floor` pass then kept every leg chain on the ground; all eight actions of both creatures reimport with 4 mm contact except the cave monster's death, whose belly settles about 0.1 unit into the ground.

## Runtime

- Cave monster: `gfx/models/units/018_resources_found_cave_monster/`, `gfx/entities/018_resources_found_cave_monster.gfx/.asset` (the five brood aliases are kept); contract `docs/systems/3d_model_pipeline/resources_found_cave_monster_model.md`.
- Plague carriers: `gfx/models/units/012_africa_plague_carriers/`, `gfx/entities/chaosx_plague_carriers.gfx/.asset` (entity `plague_carriers_entity`, accepted scale 1.0 kept); the emptied shared `012_africa_strange_forces` files are removed.
- Both use their existing sourced sounds, timed to the authored beats.

## Out of scope

The Africa elephant uses the vanilla elephantry visual by the user's explicit direction; its leftover loose files in `gfx/models/units/chaosx_elephants/` have no consumer.

## Remaining limits

- The walks are authored keyframe cycles, not motion capture; stride and bob are tuned from side renders at review size.
- Counter art was not changed.
