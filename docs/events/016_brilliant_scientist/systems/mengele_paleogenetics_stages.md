# Directorate Paleogenetics stages

The Directorate advances Paleogenetics through four ordered paid stages in its Biological Programs decision category: Theory, Prototype, Deployment, and Weaponization.
The native Paleogenetics special project provides the Prototype with Götterdämmerung; without that presentation, a paid timed decision provides the Prototype once.
The four decisions use the private Paleogenetics family receipt and never write Kruger's project board.

## Lifecycle and interactions

Each decision requires the current Directorate provider, its exact preceding stage, an empty Paleogenetics family receipt, sufficient civilian factories, and the quoted Political Power, Support Equipment, and Fuel where required.
Starting a timed decision reserves factories through native `civilian_factory_use` and records direct payment through `brilliant_scientist_mengele_begin_project_stage`.
The matching family and stage callback settles the receipt and applies the stage output, with a separate retained construction receipt for Deployment.
Cancellation releases the native factory reservation, and work with no construction attempt refunds its recorded direct payment once.
The no-DLC Prototype grants Paleogenetic operational technology through the neutral custom-technology API only after its private finish succeeds; the native project uses the existing Event 016 bridge.
Deployment commissions the actor's freely selected reserve and distinct hatchery, and Weaponization grants its existing refinement.
The reserve receives one infrastructure level and the hatchery one civilian factory through measured native construction increments.
The 130 PP, 975 support equipment, 1,500 fuel, four-factory commitment and 480-day schedule fund both components.
The selected pair is frozen at payment and cannot be replaced by later map selection.
Each attempt records the native building level immediately before and after construction, so competing construction cannot count as the paid output.
Successful components are never repeated, and a missing slot can delay only the outstanding component.
If either component has been delivered, the remaining work stays funded for free completion after the native timer ends.
An uncertain payment, construction or refund is suspended with its retained receipt and visible status, without a blind retry or full refund.
No Kruger reserve, hatchery, handler, recruitment, breeding or crisis history is written by this private transaction.

## Tuning and assets

Stage durations come from `common/script_constants/016_brilliant_scientist_constants.txt`; direct prices and factory reservations come from `common/script_constants/016_brilliant_scientist_project_constants.txt` and the shared quote loader in `common/scripted_effects/016_mengele_project_stage_effects.txt`.
File-local factory modifier and AI Political Power hint values in `common/decisions/016_mengele_paleogenetics_stage_decisions.txt` mirror shared values where those decision fields reject `constant:` tokens.
The four existing icons are `GFX_decision_brilliant_scientist_project_paleogenetics_theory`, `GFX_decision_brilliant_scientist_project_paleogenetics_prototype`, `GFX_decision_brilliant_scientist_project_paleogenetics_deployment`, and `GFX_decision_brilliant_scientist_project_paleogenetics_weaponization` in `interface/016_brilliant_scientist_project_icons.gfx`.
Their textures live under `gfx/interface/decisions/016_brilliant_scientist/projects/`; no new bitmap is required for these decisions.
Free selection uses map-only native state decisions with the existing Deployment icon.
The country list adds at most one reset action alongside its five stage rows, or one recovery action while the family receipt is busy.
The resource colours share the same inclusive predicates as native admission.
Frozen site names, delivered components and suspended work appear in native tooltips, with no dedicated scripted GUI.
The existing CXT ownership probe observes these receipts without granting or settling content.

## Future plans and acceptance

The accepted [full deployment contract](../../../plans/016_brilliant_scientist_plans/016_private_paleogenetics_deployment_acceptance_2026-10-08.md) also requires a real allocated handler/veterinary workforce, measured transport infrastructure and bounded breeding with returnable handling kits.
Those supplemental actions remain accepted and queued, and the paired-construction tranche is not completion of the full private Paleogenetics payoff.
AI selection against the full decision pool, native factory reservation and callback order, same-family timer restart, decision-list presentation, and live Paleogenetic consumers remain acceptance work.
