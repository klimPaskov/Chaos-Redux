# Directorate Electronics, Rocketry, and High Energy Prototypes

The Directorate pursues Electronics, Rocketry, and High Energy through Theory, Prototype, Deployment, and Weaponization in its existing clone-army decision category.
The established conventional decision file owns Theory, Deployment, and Weaponization for all three families.
With Götterdämmerung, each family's mapped native special project provides the Prototype; without it, a paid timed decision provides the same private Prototype receipt.

## Lifecycle and interactions

The no-DLC Prototype requires current Directorate authority, its completed private Theory, an empty family receipt, civilian factory capacity, and Political Power, Support Equipment, and Fuel.
Native `civilian_factory_use` reserves the factories for the Prototype timer while `brilliant_scientist_mengele_begin_project_stage` records and debits the direct payment.
Exact family and Prototype callbacks settle the receipt, and cancellation refunds the saved direct payment while the native decision lifecycle releases the factories.
The Prototype records its family history and modifier; the later Deployment decision grants the conventional operational package, and Weaponization applies its existing upgrade.
Electronics, Rocketry, and High Energy Deployment accept the paid provider route without the DLC after the private Prototype, while their native project and research prerequisites remain active with the DLC.
Electronics Weaponization similarly accepts the no-DLC paid route after Deployment; Rocketry and High Energy Weaponization already had that no-DLC branch.

## Tuning and assets

Durations come from `common/script_constants/016_brilliant_scientist_constants.txt`, and prices and factory reservations come from `common/script_constants/016_brilliant_scientist_project_constants.txt` through `common/scripted_effects/016_mengele_project_stage_effects.txt`.
The file-local factory and Political Power hint aliases in `common/decisions/016_mengele_remaining_conventional_prototype_decisions.txt` mirror the shared quote for native decision fields that reject `constant:` tokens.
The existing Electronics Guidance, Rocketry Propulsion, and High Energy Physics Prototype sprites are defined in `interface/016_brilliant_scientist_project_icons.gfx` and point to matching DDS files under `gfx/interface/decisions/016_brilliant_scientist/projects/`.
No new bitmap is required for these Prototype decisions.

## Future plans and acceptance

Exact later native-stage settlement with the DLC remains a separate accepted portfolio requirement.
Both DLC-state decision visibility, native reservation and callback order, same-family timer restart, AI selection, and operational consumers remain acceptance work.
