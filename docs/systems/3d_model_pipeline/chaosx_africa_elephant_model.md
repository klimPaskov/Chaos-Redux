# Event 012 elephant visual disposition

The Event 012 armoured elephant formation reuses the installed vanilla elephantry visual by explicit user direction. Its gameplay identity remains custom through `chaosx_elephant`, its equipment, armour values, and technology bridge, but no custom Meshy model, rig, skeletal action set, or entity is required.

## Active runtime

- `common/units/012_africa_elephant_forces.txt` sets `sprite = elephantry` on `chaosx_elephant`.
- Host and Action 102 member templates leave `override_model` unset, allowing mixed divisions to resolve each regiment's own visual instead of forcing an elephant entity over the full division.
- The vanilla consumer is `infantry_rifle_entity` from `gfx/entities/units_infantry.asset`, backed by `generic_western_european_rifle_infantry_mesh` and its registered `elephantry_idle` and `elephantry_move` variants.
- The former custom registrations in `gfx/entities/chaosx_elephants.gfx`, `gfx/entities/chaosx_elephants.asset`, and `gfx/models/units/chaosx_elephants/animation_chaosx_elephants.asset` are retired. Remaining custom binary files and the evidence workspace are retained only for provenance and must not be synchronized.

## Historical evidence

The superseded package record remains under `docs/assets/012_africa/models_3d/elephant_shared_base/` and `docs/plans/012_africa_plans/subagent_handoffs/012_africa_elephant_meshy7_redo.md`. It documents the prior reference cleanup, provider feasibility checks, and candidate files, but it is not a current production or promotion target.

## Gameplay and asset boundary

The custom unit still consumes `chaosx_elephant_equipment_1`, keeps its armour and combat profile, and remains used by the host and Action 102 member formation helpers. Existing equipment art and any bespoke unit counter may remain as gameplay-facing identity assets, but they do not imply a custom 3D entity or custom animation package.

The elephant achievement remains separately gated by its movement, supply, destruction, and war-purpose witnesses. Reusing the vanilla visual does not claim live campaign completion for those gameplay proofs.
