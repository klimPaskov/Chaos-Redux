# CBRN chemical doomsday effects reference

This file documents the country-scoped chemical doomsday resolver and its native raid callback in `common/scripted_effects/cbrn_chemical_doomsday_effects.txt`. The raid definition is `chemical_stockpile_doomsday_raid` in `common/raids/cbrn_doomsday_raids.txt`, under the existing `chemical_raids` category.

## `cbrn_chemical_doomsday_release`

Scope: country scope, called only by `cbrn_chemical_doomsday_native_raid_outcome` after a successful or critical native raid result.

Inputs: the country must satisfy extreme-use authority, the last-resort and selected-state gates, and the native raid must have reserved at least one each of the Chlorine, Phosgene, Mustard, and Lewisite cylinder archetypes. The selected state authenticates the raid; it does not restrict the catastrophe to that state.

Outputs: every exact eligible controlled state receives an allocation from the real debited cylinder stock through `cbrn_prepare_chemical_action_record` and `cbrn_dispatch_chemical_action_record`.

Native `essential_equipment` reserves one lot of each supported cylinder archetype during fourteen days of preparation. On a valid successful callback, the resolver debits only the remaining national stock and includes the four reserved lots in its accounting before distributing each agent's real total across the exact controlled-state array. It refuses to create an action when the stock debit, target array, protection receipt, victim country, release receipt, or shared action record is missing.

The committed terminal release order supplies release efficiency only. The engine does not expose live weather, terrain, density, forecast, command, or friendly-risk inputs for this route, so those optional modifiers remain absent rather than receiving a fixed or neutral receipt.

Accepted dispatches use the shared chemical exposure pipeline for disruption, protection-adjusted deaths, contamination, medical saturation, evidence, attribution, history, treaty response, and Condemnation. The adapter supplies one bounded batch Condemnation amount, prorated across agent lots and attached to the first accepted state for each agent.

The original identifier `chem_apply_state_contamination_doomsday` remains inert for compatibility. The former doomsday decision and category are retired; no alternate contamination or consequence path remains in that surface. A valid callback sets `cbrn_chemical_doomsday_raid_committed` before any irreversible dispatch so a second prepared raid cannot repeat a partial release.

## Private helpers

`cbrn_chemical_doomsday_collect_target_states` builds the exact state array for the current releasing country.

`cbrn_chemical_doomsday_capture_and_consume_arsenal` reads and debits the remaining four supported cylinder equipment types, adds the native reserved lot of each to the release record, and records debit proof.

`cbrn_chemical_doomsday_set_batch_condemnation` and `cbrn_chemical_doomsday_set_agent_condemnation_share` centralize the bounded gameplay-tuning consequence calculation.

`cbrn_chemical_doomsday_set_release_receipt` supplies the committed release-order efficiency without manufacturing environmental inputs.

`cbrn_chemical_doomsday_resolve_current_state` binds one exact target, prepares the shared action record, and dispatches only after all validation passes.

`cbrn_chemical_doomsday_dispatch_current_agent` allocates one agent's real stock across the exact state array without duplication.

## Tuning and engine limits

The route, release, and consequence values live in `common/script_constants/cbrn_system_constants.txt` and `common/script_constants/cbrn_chemical_doomsday_constants.txt`.

The 150 to 500 Condemnation range is gameplay tuning with low historical confidence because a legacy cylinder is an operation-sized gameplay unit rather than a fixed chemical mass.

The adapter intentionally does not retain an estimator. Continuous chemical air missions remain rejected until a verified current-version activity hook exists.

The native raid has a selected state, supply-node origin, assigned three-infantry or three-motorized division, army-intelligence category, fourteen-day preparation, and 25 Command Power allocation. Failure and limited success do not enter this resolver or create the catastrophe, news, one-shot flag, or manual stock debit. The installed raid documentation does not prove cancellation refunds or the final destruction behavior of reserved equipment after each outcome; these remain engine-evidence and user live-validation limits. No raid inspect/render or same-scenario weighted-probability comparison was available for this route.

## Example

```txt
cbrn_chemical_doomsday_native_raid_outcome = yes
```

The example is the native raid-instance outcome callback, which saves the actor and selected-state targets before calling the country-scoped `cbrn_chemical_doomsday_release = yes` resolver. It is not a player decision and does not call the legacy direct contamination helper.
