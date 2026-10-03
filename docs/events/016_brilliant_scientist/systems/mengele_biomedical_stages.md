# Directorate Biomedical stages

The Directorate advances Biomedical research through Theory, Prototype, Deployment, and Weaponization in its Biological Programs decision category.
Theory, Deployment, and Weaponization use the established conventional provider decisions.
The native Biomedical Acceleration special project provides the Prototype with Götterdämmerung; without that presentation, a paid timed decision provides the Prototype once.
All four stages settle through the private Biomedical family receipt rather than Kruger's project board.

## Lifecycle and interactions

The no-DLC Prototype requires current Directorate authority, a completed private Biomedical Theory, an empty family receipt, civilian factory capacity, and its direct Political Power, Support Equipment, and Fuel payment.
Native `civilian_factory_use` reserves two factories for the 240-day timer, while `brilliant_scientist_mengele_begin_project_stage` records and debits the direct payment.
The exact family and Prototype callback settles the receipt; cancellation refunds the saved direct payment and releases the native factory reservation.
The Prototype records authorized research history and its existing modifier; the later Deployment decision grants the complete conventional Biomedical package, and Weaponization adds its fourth-stage effects through the shared API.

## Tuning and assets

Prototype duration comes from `common/script_constants/016_brilliant_scientist_constants.txt`, and its price and factory reservation come from `common/script_constants/016_brilliant_scientist_project_constants.txt` through the shared stage quote loader in `common/scripted_effects/016_mengele_project_stage_effects.txt`.
The two file-local literals in `common/decisions/016_mengele_biomedical_prototype_decision.txt` mirror the shared factory reservation and Political Power hint where the decision fields reject `constant:` tokens.
The existing `GFX_decision_brilliant_scientist_project_biomedical_acceleration_prototype` sprite is defined in `interface/016_brilliant_scientist_project_icons.gfx` and points to `gfx/interface/decisions/016_brilliant_scientist/projects/biomedical_acceleration_prototype.dds`.
The three established stage sprites remain in that GFX file; no new bitmap is required.

## Future plans and acceptance

The other conventional families need their own no-DLC Prototype decisions or exact native alternatives under the accepted portfolio plan.
AI selection, native reservation and callback order, same-family timer restart, cost presentation, and the Biomedical runtime consumers remain acceptance work.
