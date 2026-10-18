# Exact Civilian Transfer Primitive

Status: neutral low-level contract shared by migration and other explicitly authorized movement owners.

## Boundary

`civilian_transfer_*` is not a third player-facing mechanic and has no decision category or mapmode. It is a neutral physical primitive because exact state-to-state population movement must have one authoritative debit and credit path.

## Required proof

A caller supplies an exact origin state, destination state, people amount, route, border, transport, safety, actor, destination food, destination reception, cohort, generation, and route-role proof bundle as required by the selected contract. Missing proof fails closed.

Shared object validation also requires that a country actually exists, including a country reached through a stored variable or event target.
Scope existence alone cannot authorize a dormant or annexed country as an actor, owner, controller, donor, or destination host.
`common/scripted_triggers/humanitarian_validation_triggers.md` documents this read-only country/state validation contract; the transfer owner still requires the complete independent transaction receipt.

## Conservation

The primitive reads live origin population through the exact state-population API and applies one measured origin debit through the population-loss helper that does not create recruitable manpower.

Route deaths are part of that debit. They are entered in the Deaths ledger with population application disabled because the physical debit already occurred.

Only survivors are credited to the destination. Incidental recruitable-manpower effects are corrected for the destination owner/controller.

If the destination credits fewer survivors than requested, the exact residual is restored to the origin and incidental recruitable-manpower effects from restoration are corrected.

The finalized identity is:

`actual origin debit = route deaths + actual survivor credit`.

A transaction is valid only with a positive measured debit and zero conservation residual. Movement is never counted as death, and deaths are never credited as arrivals.

## Ownership

The movement owner supplies the cohort and route meaning. The transfer primitive owns physical population mutation and conservation only. The original hazard owner retains direct mortality ownership, and the migration owner retains cohort, reception, settlement, and return state.

The only non-movement hook is `mysterious_people_on_civilian_transfer`, called once at the origin after a valid projection. It reads the measured debit, survivor credit and destination population to keep the Event 037 newcomer ledger inside real population and changes no population itself.

## Scheduling

The primitive executes only from an exact owner transaction. It has no recurring scan or independent pacing.
After a valid finalize receipt, the transaction wrapper publishes both exact endpoint states to their current owners and distinct controllers; staged and rolled-back transfers do not publish a movement result.
