# Event 006 FORM-39 civil-service factory reservation

Date: 2026-08-25

## Scope and source defect

The FORM-39 post-formation civil-service project is a 210-day decision that already displays and checks the standard two-civilian-factory requirement through `can_pay_independence_wave_form39_civil_service_cost` and `independence_wave_form39_civil_service_cost`.

Before this patch, the decision checked `num_of_civilian_factories_available_for_projects` through `can_pay_independence_wave_strategic_cost` but did not reserve factory capacity while the project was active.

This was a player-facing requirement mismatch and an exploit surface: the project could begin after checking capacity while leaving the same factories available to overlapping projects.

## Implementation

`common/decisions/006_independence_wave_formable_decisions.txt` now declares the file-scoped constant `CR_SC_INDEPENDENCE_WAVE_FORM39_CIVILIAN_FACTORY_USE = 2` and adds `modifier = { civilian_factory_use = @CR_SC_INDEPENDENCE_WAVE_FORM39_CIVILIAN_FACTORY_USE }` to `independence_wave_form39_open_regional_civil_service`.

The existing trigger, payment helper, 210-day duration, completion effect, cancellation trigger, cleanup flag, AI base, formable identity, member contract, and fail-closed admission boundary are unchanged.

The existing localisation already exposes the standard factory amount in the civil-service cost tooltip and blocked string, so no YAML wording change is required.

## Vanilla/reference basis

The installed vanilla modifier documentation defines `civilian_factory_use` as a country/war-production modifier with an integer value.

Vanilla decision precedents use `modifier = { civilian_factory_use = <integer> }` on time-bound project decisions; the Event 006 patch follows that structure while keeping its tier in a local constant.

## Validation

- The FORM-39 civil-service decision contains exactly one civilian-factory reservation modifier with value `2`.
- The reservation constant is declared exactly once in the receiver decision file.
- The civil-service trigger still requires the standard available-factory threshold and the project-active guard.
- The payment effect still pays the existing strategic and diplomatic helpers exactly once.
- No event, package admission, attestation, AI weight, formable membership, localisation key, or asset file changed.

This handoff is source and static evidence only; no live tooltip, save/load, or in-game execution claim is made.
