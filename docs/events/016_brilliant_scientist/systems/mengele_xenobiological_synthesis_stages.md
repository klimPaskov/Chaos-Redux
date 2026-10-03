# Directorate Xenobiological Synthesis stages

The Directorate develops Xenobiological Synthesis through Theory, Prototype, Deployment, and Weaponization in the Biological Programs decision category.
Theory, Deployment, and Weaponization are paid timed decisions in both DLC states.
With Götterdämmerung, the native Xenobiological Synthesis special project owns the Prototype clock and payment; without it, a paid timed decision provides the Prototype.
The four stages use the private Xenobiological Synthesis family receipt and do not consume Kruger's project board.

## Lifecycle and interactions

Each decision checks Directorate authority, the preceding family stage, an empty private receipt, and the stage's factory and direct-resource requirements.
Its native `civilian_factory_use` reserves factories while `brilliant_scientist_mengele_begin_project_stage` records and debits the direct payment.
Exact family and stage callbacks settle the receipt; cancellation returns the saved direct payment and releases the native factory reservation.
The no-DLC Prototype calls the existing custom xenobiological operational grant only after a successful private finish, while native project completion supplies that grant on the DLC route.
Deployment and Weaponization use the existing custom operational and upgrade APIs through the shared private stage output.

## Tuning and assets

Durations come from `common/script_constants/016_brilliant_scientist_constants.txt`, and costs come from `common/script_constants/016_brilliant_scientist_project_constants.txt` through the shared stage quote loader in `common/scripted_effects/016_mengele_project_stage_effects.txt`.
File-local aliases in `common/decisions/016_mengele_xenobiological_synthesis_stage_decisions.txt` mirror factory reservation and AI Political Power hint values for fields that reject `constant:` tokens.
The four existing `GFX_decision_brilliant_scientist_project_xenobiological_synthesis_<stage>` sprites are defined in `interface/016_brilliant_scientist_project_icons.gfx` and point to matching DDS files in `gfx/interface/decisions/016_brilliant_scientist/projects/`.
No additional image is required for these four decisions.
The AI retains the existing low Theory, Deployment, and Weaponization bases and high Prototype base, with wartime preference and a cautious factor when available project factories do not exceed the current stage's quote of 1, 2, 5, or 7.

## Future plans and acceptance

The accepted portfolio plan still requires the remaining provider families, native completion settlement, and CXT scenario fixtures.
AI probability comparison, native reservation and callback ordering, current decision-list presentation, and live consumer behavior remain acceptance work.
