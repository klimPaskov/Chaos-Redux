# Migration System

Status: implemented source ledger pending the remaining probability, adapter, and completion audits. This is not a gameplay-completion claim.

## Ownership

Migration is an independent cohort, route, reception, and settlement mechanic. Its gameplay identifiers, variables, flags, effects, triggers, decisions, missions, localisation, sprites, and CXT fixture use the `migration_*` namespace.

Famine can be one proven cause of movement, and migration can create trapped-population pressure that worsens famine. Neither mechanic owns the other's primary ledger or decision category.

Famine survivor displacement enters through `migration_accept_famine_survivor_request`; migration alone reconciles cohorts, reserves existing obligations, applies the protected population floor, caps the accepted amount, writes flight ledgers, and refreshes its category. Trapped-population food demand travels in the opposite direction through the versioned `migration_to_famine_reception_demand_*` receipt.

When the famine category offers organized evacuation, migration-owned availability helpers expose only whether reception and preparation permit the request. Migration then stages the trapped obligation and cohort, runs the exact transfer, and owns mission subject, cohort, deadline, slot, report, and trapped-state cleanup. The famine surface receives only the neutral transaction receipt and never owns migration lifecycle data.

Migration exposes narrow positive triggers for humanitarian-open reception policy, active persecution, and native destination safety. Famine relief and evacuation consumers use those seams rather than reading migration policy or hazard ledgers. Railway damage is a neutral physical projection refreshed independently by both sparse mechanics.

The ordinary player surface is `migration_decision_category`. It is hidden at campaign start unless a country has a genuine starting displacement problem. Otherwise it appears only after a large incident, two distinct incident episodes, or sustained flight, trapped-population, corridor, or reception evidence reaches the centralized threshold.

Durable resettled and returned population totals remain available to the mapmode, history, documentation, and achievement consumers, but they cannot reveal or reopen the decision category after the live migration problem has resolved.

The dedicated `migration_state_map_mode` remains available from campaign start.

`migration_register_initial_incident` is a migration accounting and presentation seam called after a proven new displacement-pressure episode. It records bounded state presentation and selects migration report context only; it does not create an event object, event ID, event-pool entry, event-log row, pacing pulse, random event, or population transaction.

The deleted `events/migration_incidents.txt` file and its incident constants are deliberate. Earlier incident-event and incident-option probability wording is superseded and is not a current implementation requirement.

## Player-facing values

The migration surface presents one primary value and no more than two supporting values:

- Displacement Load: active people requiring movement, protection, reception, or resolution.
- Reception Capacity: the current ability to receive and support arrivals.
- Border Policy: humanitarian open, controlled, transit, closed, or violent enforcement as applicable.

Cohort IDs, generations, exact transfer proofs, and registry rows remain internal evidence, not player homework.

## Canonical player-facing value count

Migration exposes exactly three canonical player-facing values: Displacement Load, Reception Capacity, and Border Policy.

Destination and reception safety consume the proven, versioned `famine_to_migration_*` food-safety projection. Migration does not initialize famine or read raw famine stage, pressure, transport, governance, production, exposure, or incident fields. Missing or invalid projection facts fail closed.

Internal conceptual components and ledgers, including cohorts, routes, reception load and capacity components, custody and return receipts, generations, revisions, and scheduler state, are implementation evidence rather than additional player-facing mechanics.

Raw variables, flags, temporary values, transaction receipts, and diagnostic tooltip details do not increase the canonical count; mapmode and report context remains contextual presentation.

## Movement lifecycle

Migration supports internal displacement, cross-border flight, organized evacuation, deportation, reception, controlled medical reception, transit, local integration, third-country resettlement, voluntary return, and forced return.

Movement is never a death. Every physical route delegates to the neutral exact transfer primitive, which debits the origin once, records route deaths as a slice of that debit, and credits only surviving people to the destination.

Migration owns cohort identity, current host, historical origin, route role, generation, status, reception load, integration, resettlement, and return state. Exact aligned registries and generation checks prevent stale-host resolution, duplicated cohorts, and transfer cycling.

## Borders and trapped populations

Closed borders do not erase a cohort. A valid closure creates or maintains trapped population and produces real humanitarian, diplomatic, security, political, reception, and mortality consequences through their respective owners.

Violent pushback and unsafe forced return can create route deaths under `constant:chaos_meter_deaths_reason.forced_displacement`, localized as `From forced displacement`. The exact transfer transaction logs those deaths without applying a second population debit.

## Decisions and missions

Migration owns its own category and phased actions for departure policy, evacuation preparation and priority, corridor negotiation, reception policy, controlled medical reception, distribution, transit, border closure and enforcement, integration, resettlement, voluntary return, and forced repatriation.

Migration missions own corridor, evacuation-transport, reception-observation, and safe-return deadlines. Famine missions are never counted in migration mission slots or presented as migration actions.

The AI uses the same availability, route, capacity, safety, policy, and owner-proof gates as the player. Ideology is a bounded weight after validity; persecution, camps, genocide, bombing, occupation conduct, famine, contamination, route danger, and lack of capacity can override ideological affinity.

## Sparse runtime

The runtime processes only registered active migration states and countries through the existing host-only coordinator. Exact on-actions and owner callbacks add or invalidate affected rows. No whole-world daily, weekly, or monthly scan is added.

## Adapters

Migration accepts exact owner-proven pressure and transaction requests from persecution, occupation, camps, gulags, forced labor, genocide, deportation, bombing, nuclear damage, fallout, outbreaks, natural disasters, war, peace, relevant events, clusters, and scenarios.

An adapter must prove state, people, actor, cause, route or custody context, generation, revision, and request ownership as required by the receiving contract. An event flag, generic severity, or ideology is not a substitute for those facts.

## Assets and mapmode

Migration assets use `migration_*` filenames and sprite identifiers. `interface/migration_system.gfx` owns the category, decision, state-modifier, and achievement sprites; `interface/chaosx_texticons.gfx` owns the migration Deaths texticon; `interface/migration_report_pictures.gfx` and `interface/migration_report_header.gui` own the compact migration report art consumer; `interface/mapmodes_interface.gfx` owns the two migration mapmode button states.

The migration mapmode colors lifecycle state and independently marks trapped populations, overcrowding, border status, corridor safety, reception pressure, and flight pressure. It does not read famine relief state.

The current documentation inventory contains 61 declared final DDS outputs across the package: 50 root-manifest assets, seven report images, and four mapmode buttons. Category-asset closure reconciles the famine and migration category consumers, and the parent contact-sheet review accepted every visual family. Live in-game consumer validation remains user-owned.

## CXT fixture

`migration_register_cxt_test_content` registers `chaosx_cxt_extension_migration`. Its idempotent apply effect gives the test country bounded reception capacity without creating a cohort, route, population transfer, famine problem, or mortality transaction.

## Event 149 retirement

Event 149 `Immigrations` is retired and absorbed into this system. No replacement event ID, event object, event-pool registration, flat population drain, event-log row, or event-pacing pulse is permitted, and state/accounting pulses are not event pacing.

## Open evidence gates

- Complete all named probability comparison scenarios for border policy, destination selection, outbreak reception, evacuation, corridor acceptance, return, integration, resettlement, opposition, and cleanup through a callable `chaosx_ai_probability_auditor`; direct MCP inspection remains evidence only.
- Close only external adapters whose owners provide exact receipts; retain missing owner data as explicit blockers.
- Obtain supported runtime visual evidence for the hardcoded mapmode window if the tooling exposes it.
- Reconcile the remaining specialist audit routes whose current handoffs are frozen snapshots; current direct inspect artifacts, typed-fixture limits, and unavailable custom-pool routes are recorded in `ai_probability_current.md`.

## Future extensions

Future depth should prefer richer exact route ownership, bilateral reception agreements, and cohort-specific political consequences over new headline meters. Any extension must preserve sparse scheduling, exact transfer conservation, shared validity for human and AI choices, and the separate migration namespace.
