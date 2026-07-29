# CBRN chemical doomsday effects reference

This file documents the explicit chemical doomsday decision adapter in `common/scripted_effects/cbrn_chemical_doomsday_effects.txt`.

## `cbrn_chemical_doomsday_release`

Scope: country scope, called by the decision-facing `chem_unleash_stockpile_doomsday` compatibility identifier.

Inputs: the country must satisfy the unrestricted-use policy, control at least one state with a positive native population value, and own at least one of the four supported legacy cylinder models: chlorine, phosgene, mustard, or lewisite.

Outputs: every exact eligible controlled state receives an allocation from the real debited cylinder stock through `cbrn_prepare_chemical_action_record` and `cbrn_dispatch_chemical_action_record`.

The adapter consumes each supported cylinder model exactly once before dispatch. It distributes each agent's real lot across the exact controlled-state array and refuses to create an action when the stock debit, target array, protection receipt, victim country, release receipt, or shared action record is missing.

The committed terminal release order supplies release efficiency only. The engine does not expose live weather, terrain, density, forecast, command, or friendly-risk inputs for this route, so those optional modifiers remain absent rather than receiving a fixed or neutral receipt.

Accepted dispatches use the shared chemical exposure pipeline for disruption, protection-adjusted deaths, contamination, medical saturation, evidence, attribution, history, treaty response, and Condemnation. The adapter supplies one bounded batch Condemnation amount, prorated across agent lots and attached to the first accepted state for each agent.

The original identifier `chem_apply_state_contamination_doomsday` remains inert for compatibility. The former direct doomsday implementation is retained as an unreachable legacy block and is not an active consequence path.

## Private helpers

`cbrn_chemical_doomsday_collect_target_states` builds the exact state array for the current releasing country.

`cbrn_chemical_doomsday_capture_and_consume_arsenal` reads and debits the four supported cylinder equipment types and records debit proof.

`cbrn_chemical_doomsday_set_batch_condemnation` and `cbrn_chemical_doomsday_set_agent_condemnation_share` centralize the bounded gameplay-tuning consequence calculation.

`cbrn_chemical_doomsday_set_release_receipt` supplies the committed release-order efficiency without manufacturing environmental inputs.

`cbrn_chemical_doomsday_resolve_current_state` binds one exact target, prepares the shared action record, and dispatches only after all validation passes.

`cbrn_chemical_doomsday_dispatch_current_agent` allocates one agent's real stock across the exact state array without duplication.

## Tuning and engine limits

The route, release, and consequence values live in `common/script_constants/cbrn_system_constants.txt` and `common/script_constants/cbrn_chemical_doomsday_constants.txt`.

The 150 to 500 Condemnation range is gameplay tuning with low historical confidence because a legacy cylinder is an operation-sized gameplay unit rather than a fixed chemical mass.

The adapter intentionally does not retain an estimator. Continuous chemical air missions remain rejected until a verified current-version activity hook exists.

## Example

```txt
chem_unleash_stockpile_doomsday = yes
```

The decision-facing wrapper resolves to `cbrn_chemical_doomsday_release = yes` and does not call the legacy direct contamination helper.
