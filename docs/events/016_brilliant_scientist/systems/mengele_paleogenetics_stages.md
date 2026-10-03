# Directorate Paleogenetics stages

The Directorate advances Paleogenetics through four ordered paid stages in its Biological Programs decision category: Theory, Prototype, Deployment, and Weaponization.
The native Paleogenetics special project provides the Prototype with Götterdämmerung; without that presentation, a paid timed decision provides the Prototype once.
The four decisions use the private Paleogenetics family receipt and never write Kruger's project board.

## Lifecycle and interactions

Each decision requires the current Directorate provider, its exact preceding stage, an empty Paleogenetics family receipt, sufficient civilian factories, and the quoted Political Power, Support Equipment, and Fuel where required.
Starting a timed decision reserves factories through native `civilian_factory_use` and records direct payment through `brilliant_scientist_mengele_begin_project_stage`.
The matching family and stage callback settles the receipt and applies the stage output; cancellation refunds the saved direct payment and releases the native factory reservation.
The no-DLC Prototype grants Paleogenetic operational technology through the neutral custom-technology API only after its private finish succeeds; the native project uses the existing Event 016 bridge.
Deployment reconciles Paleogenetic operations through that idempotent API, and Weaponization grants its existing refinement.

## Tuning and assets

Stage durations come from `common/script_constants/016_brilliant_scientist_constants.txt`; direct prices and factory reservations come from `common/script_constants/016_brilliant_scientist_project_constants.txt` and the shared quote loader in `common/scripted_effects/016_mengele_project_stage_effects.txt`.
File-local factory modifier and AI Political Power hint values in `common/decisions/016_mengele_paleogenetics_stage_decisions.txt` mirror shared values where those decision fields reject `constant:` tokens.
The four existing icons are `GFX_decision_brilliant_scientist_project_paleogenetics_theory`, `GFX_decision_brilliant_scientist_project_paleogenetics_prototype`, `GFX_decision_brilliant_scientist_project_paleogenetics_deployment`, and `GFX_decision_brilliant_scientist_project_paleogenetics_weaponization` in `interface/016_brilliant_scientist_project_icons.gfx`.
Their textures live under `gfx/interface/decisions/016_brilliant_scientist/projects/`; no new bitmap is required for these decisions.

## Future plans and acceptance

The remaining family decisions should use the same private receipt boundary with family-specific outputs and native Prototype authority.
AI selection against the full decision pool, native factory reservation and callback order, same-family timer restart, decision-list presentation, and live Paleogenetic consumers remain acceptance work.
