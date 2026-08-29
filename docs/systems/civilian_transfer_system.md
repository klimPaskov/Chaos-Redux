# Exact Civilian Transfer Primitive

Status: neutral low-level contract shared by migration and other explicitly authorized movement owners.

## Boundary

`civilian_transfer_*` is not a third player-facing mechanic and has no decision category or mapmode. It is a neutral physical primitive because exact state-to-state population movement must have one authoritative debit and credit path.

## Required proof

A caller supplies an exact origin state, destination state, people amount, route, border, transport, safety, actor, destination food, destination reception, cohort, generation, and route-role proof bundle as required by the selected contract. Missing proof fails closed.

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

## Scheduling

The primitive executes only from an exact owner transaction. It has no recurring scan or independent pacing.
