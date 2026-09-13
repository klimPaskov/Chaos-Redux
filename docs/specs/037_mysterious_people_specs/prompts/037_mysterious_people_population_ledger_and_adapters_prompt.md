# Prompt: Event 037 population ledger and shared adapters

Implement the reusable scripted-system layer required by Event 037, Mysterious People.

Read the complete Event 037 specification pack, especially Parts 1, 2, 3, and 6, the system-flow diagram, balance matrix, probability scenarios, and acceptance criteria. Read `AGENTS.md`, the event skill, the scripted-effects and scripted-triggers registries, the current Famine, Migration, Deaths, Camp and Repression, Condemnation, Event Logs, and civilian-classifier sources. Consult required offline wiki pages, installed vanilla documentation, and a local population precedent before editing.

Use `chaosx_scripted_system_architect` with a complete context prompt and no inherited thread context. The parent remains responsible for final integration.

## Required system behavior

Create one event-owned population-creation transaction that:

- snapshots each valid state's real pre-fire population
- calculates the current-stage grant from centralized constants
- applies real state population gain exactly once
- returns the amount actually applied
- increases Event 037 state provenance by the applied amount
- updates country and world totals incrementally
- records one transaction identity so delayed reports, cluster calls, multiplayer clients, and reload cannot replay it
- fails closed on invalid state or incomplete contract

First prove the supported engine route for positive real state population gain. Reuse an existing neutral helper when it fits. If a new cross-system helper is genuinely required, give it a behavior-based name, keep it neutral, and document purpose, scope, inputs, outputs, defaults, side effects, and example in the shared dynamic-effects documentation. Do not place Event 037 lifecycle inside the shared registry.

## Provenance invariants

Implement state provenance, country totals, world total, latest-firing total, lifetime-created total, and guarded one-shot demographic milestones.

Guarantee:

- provenance never below zero
- provenance never above real state population
- repeated firings add to one living state total
- ownership and control changes update country views without changing state total
- general civilian loss reduces provenance by the pre-loss mysterious share of actual applied loss
- targeted loss or movement reduces provenance by the exact applied targeted amount
- no ledger-only population removal
- no double Deaths entry
- no double destination credit
- safe rounding and population floors
- save and reload persistence
- bounded reconciliation from authoritative state data

Use the existing exact civilian-population loss contract for actual deaths. Add a narrow Event 037 provenance callback or adapter only where the owner can provide applied loss proof.

## Migration adapter

Create a versioned, proof-carrying Event 037 composition contract for Migration.

It must support:

- ordinary proportional composition
- explicitly targeted mysterious cohorts
- origin debit
- route deaths
- survivors
- destination credit
- trapped population
- failed and invalid route
- ownership or controller change
- idempotent receipt consumption

Event 037 updates provenance only from an applied Migration result. It does not mutate the Migration primary ledger.

## Famine adapter

Publish Event 037 population burden and support facts in the format the current Famine owner can consume. Famine remains responsible for Food Security, reserves, relief access, stages, decisions, missions, and mortality.

When Famine applies deaths, reconcile Event 037 provenance from the exact applied loss once. Do not create a second food value or death reason.

## Camp and atrocity adapter

Expose living mysterious population as a valid targeted cohort only through the existing Camp and Repression route.

Require exact applied deaths, transfers, releases, and survivors before provenance changes. Preserve evidence, discovery, Condemnation, resistance, Migration, Deaths, and perpetrator history under their current owners.

## Pressure and active registries

Implement sparse active-state and active-country processing. One bounded world pass is allowed at Event 037 firing. Do not add recurring full-world country or state scans.

Overpopulation Pressure must aggregate state burden into one country value from `0` to `100`, with public thresholds `20`, `40`, `60`, and `80`. Keep detailed factors internal. Refresh after creation, population loss, movement, ownership, policy, capacity, Famine, and occupation changes.

## Validation

Write an implementation handoff listing files, identifiers, helpers, constants, adapters, call sites, before and after behavior, meaningful tests, unresolved engine questions, and skipped evidence.

Validate the acceptance scenarios for baseline grant, cap and floor, repeated firing, ordinary deaths, targeted deaths, internal and cross-border movement, trapped cohorts, ownership change, nonhuman exclusion, save and reload, duplicate prevention, reconciliation, and sparse-registry cleanup.

Do not claim completion without engine proof for positive state population gain and final parent review.
