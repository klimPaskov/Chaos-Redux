# Event 006 Western decision registry merge

Date: 2026-08-25.

## Scope

The Brittany, Catalonia, and Iceland package decision files were small, same-namespace parser surfaces with the same two file-scoped civilian-factory values.

They are now stored in one receiver, `common/decisions/006_independence_wave_western_decisions.txt`, with source markers for package ownership.

## Source-equivalence receipt

- The receiver contains three category roots and 34 decision definitions.
- All 34 decision identifiers are unique.
- The receiver has balanced braces at 689 opening and 689 closing braces.
- Each source body from `common/decisions/006_independence_wave_brittany_decisions.txt`, `common/decisions/006_independence_wave_catalonia_decisions.txt`, and `common/decisions/006_independence_wave_ice_decisions.txt` matches its marked receiver section after line-ending normalization.
- The shared `@CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_LIGHT = 1` and `@CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_STANDARD = 2` values are declared once in the receiver because all three sources used the same values.

## Boundaries

Decision identifiers, category identifiers, costs, timers, triggers, effects, cancellation, cleanup, AI weights, package gates, and admission behavior are unchanged.

Kosovo remains separate because its active package trigger/cost repair is still an owned working-tree surface, and Montenegro and Transylvania remain separate because their decision files use colliding file-scoped constant namespaces.

This is a source-layout consolidation only and does not widen the Event 006 admission boundary or claim live parser, AI, tooltip, or runtime evidence.

## Validation

The static source receipt above was generated from the receiver and `git show HEAD:<source>` snapshots before the three source files were removed.

