# Directorate Teleportation stages

The Directorate advances Quantum Transit through four ordered paid stages in its Advanced Programs decision category: Theory, Prototype, Deployment, and Weaponization.
The native Quantum Transit special project provides the Prototype when Götterdämmerung is active; without that presentation, a paid timed decision provides the Prototype once.
The four decisions use the private Teleportation family receipt, so their payment and completion history cannot write Kruger's project board.

## Lifecycle and interactions

Each decision checks its predecessor, the current Directorate provider, the empty family receipt, available civilian factories, Political Power, Support Equipment, and Fuel when its quote calls for them.
Starting a timed decision reserves factories through native `civilian_factory_use` and records a private direct-payment receipt through `brilliant_scientist_mengele_begin_project_stage`.
The exact family and stage callback finishes the receipt and applies the shared stage output; cancellation returns the saved direct payment and releases the native factory reservation.
The no-DLC Prototype grants Portal operational technology only after its private finish succeeds; native Prototype completion uses the existing Event 016 bridge.
Deployment reconciles Portal operations through the idempotent custom-technology API, and Weaponization grants the Portal refinement through that API.
The existing runtime Portal consumers use the resulting technology and upgrade flags; native consumer presentation and decision callback ordering remain acceptance checks.

## Tuning and assets

Stage durations come from `common/script_constants/016_brilliant_scientist_constants.txt`; direct prices and factory reservations come from `common/script_constants/016_brilliant_scientist_project_constants.txt`, and the shared stage quote loader reads both in `common/scripted_effects/016_mengele_project_stage_effects.txt`.
File-local factory modifier and AI Political Power hint values in `common/decisions/016_mengele_teleportation_stage_decisions.txt` mirror the shared values because those decision fields do not accept `constant:` tokens.
The AI applies its cautious factor when available civilian factories do not exceed the reservation quote of the current stage.
The four stage icons use existing `GFX_decision_brilliant_scientist_project_teleportation_theory`, `GFX_decision_brilliant_scientist_project_teleportation_prototype`, `GFX_decision_brilliant_scientist_project_teleportation_deployment`, and `GFX_decision_brilliant_scientist_project_teleportation_weaponization` definitions in `interface/016_brilliant_scientist_project_icons.gfx`.
Those sprite definitions point to the existing Event 016 project decision art under `gfx/interface/`; this tranche requires no new bitmap.

## Future plans and acceptance

The remaining custom-family stage decisions should reuse the private family receipt and exact native/fallback Prototype split, with family-specific outputs and player-facing text.
Native decision-list presentation, factory reservation and callback order, same-family restart ordering, Portal consumer entitlement, and AI selection against the full decision pool require the recorded engine and MCP acceptance work.
