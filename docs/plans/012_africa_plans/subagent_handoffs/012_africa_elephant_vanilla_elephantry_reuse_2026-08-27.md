# Event 012 elephant vanilla-elephantry reuse handoff — 2026-08-27

Status: `implemented_source_reuse_pending_parent_live_validation`.

The user explicitly directed the Event 012 armoured elephant formation to reuse the installed vanilla elephantry model instead of generating a duplicate custom elephant package.

## Active wiring

- `common/units/012_africa_elephant_forces.txt` keeps the custom `chaosx_elephant` unit, equipment, armour, and combat profile, but sets `sprite = elephantry`.
- `common/scripted_effects/012_africa_elephant_effects.txt` and `common/scripted_effects/012_africa_elephant_operation_effects.txt` no longer force a custom elephant entity on host or operation templates.
- `common/scripted_effects/012_africa_priority_member_force_effects.txt` no longer forces a custom elephant entity on the five mixed member formation profiles.
- Vanilla `gfx/entities/units_infantry.asset` supplies `infantry_rifle_entity`, and vanilla `gfx/entities/infantry.gfx` supplies the `elephantry_idle` and `elephantry_move` animation variants on `generic_western_european_rifle_infantry_mesh`.
- The former custom registrations `gfx/entities/chaosx_elephants.gfx`, `gfx/entities/chaosx_elephants.asset`, and `gfx/models/units/chaosx_elephants/animation_chaosx_elephants.asset` were retired from active loading; remaining custom binaries are historical evidence only.

## Validation evidence

The installed vanilla sources were checked directly and contain the `elephantry` sub-unit sprite plus its idle and move animation registrations. A repository-wide active-source scan finds no remaining `override_model = chaosx_elephant_shared_base_entity`, `sprite = chaosx_elephant_shared_base`, or active custom elephant entity reference outside historical documentation and retained evidence.

The custom model workspace at `docs/assets/012_africa/models_3d/elephant_shared_base/` is marked `custom_model_not_required_existing_elephantry_reuse` and records zero new provider spend for this decision. Its source images, candidate mesh, actions, audio, and counter records are not promotion targets.

## Remaining owner boundary

The parent owns ordinary live consumer validation for the vanilla infantry entity and the separate gameplay acceptance of the elephant achievement's movement, supply, destruction, and war-purpose witnesses. Reusing the vanilla visual does not claim those gameplay proofs are complete.
