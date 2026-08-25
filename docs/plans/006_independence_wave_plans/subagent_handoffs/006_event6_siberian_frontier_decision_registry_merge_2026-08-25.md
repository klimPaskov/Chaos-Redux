# Event 006 Siberian frontier decision registry merge

Date: 2026-08-25.

## Scope

The Udmurtia, Komi, Tatarstan, and Ruthenia package decision files are now appended to `common/decisions/006_independence_wave_siberian_decisions.txt`.

Their package trigger and effect files remain separate because those surfaces retain package-local ownership and active maintenance boundaries.

## Source-equivalence receipt

- The receiver now contains eight category roots and 88 decision definitions.
- All 88 decision identifiers are unique.
- The receiver has balanced braces at 1,940 opening and 1,940 closing braces.
- Each source body from `common/decisions/006_independence_wave_udm_decisions.txt`, `common/decisions/006_independence_wave_komi_decisions.txt`, `common/decisions/006_independence_wave_tatarstan_decisions.txt`, and `common/decisions/006_independence_wave_ruthenia_decisions.txt` matches its marked receiver section after line-ending normalization.
- The four package-specific civilian-factory constants remain distinct and are preserved in their marked source sections.

## Boundaries

Decision identifiers, category identifiers, costs, timers, triggers, effects, cancellation, cleanup, AI weights, package gates, and admission behavior are unchanged.

This source-layout consolidation does not promote Komi, Udmurtia, Tatarstan, or Ruthenia into central Event 006 attestation and does not alter package trigger/effect ownership.

## Validation

The static source receipt above was generated from the receiver and `git show HEAD:<source>` snapshots before the four source files were removed.

