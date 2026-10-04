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

## Prospective reception contract

The accepted first-reception repair is defined in [Part 3](../specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_3_displacement_migration_return.md), [Part 6](../specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_6_decisions_ai_presentation.md), and the [bounded implementation plan](../plans/famine_and_migration_system_plans/prospective_reception_lifecycle_plan_20261003.md).
The bounded source path is implemented and independently source-audited in [the completion handoff](../plans/famine_and_migration_system_plans/subagent_handoffs/prospective_reception_completion_audit_20261003.md).
Native execution and the required same-scenario probability comparison remain unresolved, so this is not a full-system completion claim.

A real spontaneous request first uses the existing operational internal-first destination search.
Only when that search cannot resolve the request may the sparse origin-state owner rank adjacent preparable foreign hosts, retaining actual food, native transport, ownership, control, relation, actor, and hazard checks.
No missing reception service is represented as capacity or given a capacity weight bonus.
The exact selected front, live origin cohort, and fresh contract generation are persisted in the existing humanitarian corridor and country mirrors.
The source row remains at the origin without a bound destination; a request creates no arrival, population debit, reception load, or death.

The host's existing Open Emergency Reception action prepares only the exact requested state while an offer is pending.
It uses the existing shelter and medical service setters and population-scaled shares, a single centralized three-resource payment, an inclusive affordability predicate, and exact rollback/refund on rejected paid setup.
An unchanged service receipt cannot be charged again as successful preparation.
Once fresh live-cohort and full headroom checks pass, the host may accept the request; the existing sparse spontaneous owner then delegates movement to the exact civilian-transfer transaction.
Acceptance and transfer each revalidate the actual amount, route, capacity, policy, actor, cohort, and generation.
Rejection or expiry preserves the origin obligations and can clear only matching mirrors.

One tiny incoming request does not reveal the migration category.
Large or sustained issue facts, or distinct valid incoming evacuation generations counted once in the existing incident count, use the existing reveal thresholds.
Preparation and rejection precede acceptance; these are phased uses of existing controls, not an additional category, mission, GUI, or headline value.
The pending-request priority text explains the current choice without calling the people arrivals.

Reception preparation costs live in `common/script_constants/migration_reception_preparation_constants.txt`.
The existing active-country registration and country phase provider share a display-only cost projector for `common/scripted_localisation/migration_reception_preparation_cost_scripted_localisation.txt`; fresh constants, not cached text values, govern affordability and payment.
`localisation/english/migration_l_english.yml` owns the six ready/blocked cost labels and request wording, reusing the existing `£pol_power`, `£support_equipment_text_icon`, and `£GFX_fuel_texticon` consumers.
The action retains `GFX_migration_decision_open_border`; no new art or sprite consumer is required.

## Paid decision work

The 15 legacy migration actions share neutral central fee tuning and pure inclusive cost components/profiles with the famine decision owner, without sharing a category or mechanic lifecycle.
Availability, the native custom-cost branch, resource colors and final payment use the same exact country-payer bundle; display-only quotes are not payment authority.
Immediate actions validate their whole activation before writes, while delayed paid work uses independent action/state/payer receipts before its existing continuation.
Corridor negotiation preserves deferred payment after a successful offer and rechecks its full fee before preparation, submission and debit.
Receipt cleanup touches only its matching or invalid state-local work and does not erase another state, action or valid payer's receipt.
The existing movement refunds require a matching paid action and zero measured origin debit; real physical transfer does not receive a blanket late-failure refund.
Workers' support-equipment prerequisite remains non-spendable, and no fee, cooldown, numeric AI factor, headline value, category, asset or global scheduler is added by this ownership boundary.
Native callback exclusivity, same-payer replay behavior and the mandatory probability comparison remain unresolved evidence gates, not assumed proofs.

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

Its authorized reception-capacity status uses the migration owner's complete read-only validity contract, including the current schema, clean revision, positive real capacity and candidates, and no invalid candidates.
A cached positive capacity token alone cannot label a dirty or invalid reception ledger as valid; the tooltip never recalculates or grants capacity.

Receiving fronts of evacuation corridors carry a private reception intent for their owner or controller: requested after a valid offer, prepared after paid reception preparation, and agreed after consent.
The front keeps one identity-only row per live corridor, so an older agreed passage and a newer pending request at the same front survive each other.
Measured passage and every corridor terminal retire exactly their own row, and a front that changes hands drops the rows of a receiver that lost it.
Intent never carries people, reception load, capacity or route permission, and any real trapped, arrival, hosting or overcrowded role keeps display priority.
Latest-movement labels separate actual transfers, including deportation and civilian flight transfers, from pressure-only causes, which read as pressure.
The API is documented in `common/scripted_effects/migration_reception_front_intent_effects.md` and `common/scripted_triggers/migration_reception_front_intent_triggers.md`.

The current documentation inventory contains 61 declared final DDS outputs across the package: 50 root-manifest assets, seven report images, and four mapmode buttons. Category-asset closure reconciles the famine and migration category consumers, and the parent contact-sheet review accepted every visual family. Live in-game consumer validation remains user-owned.

## CXT fixture

`migration_register_cxt_test_content` registers `chaosx_cxt_extension_migration`.
Its idempotent apply effect requests a capacity refresh; the current owner recalculates from real registered food, shelter, and medical receipts rather than granting the legacy requested aggregate amount.
This registration does not supply missing services, create a cohort or route, move population, start a famine problem, or apply mortality.
Starting and exercising a real reception case still needs its exact owner inputs; registration alone is not a capacity or execution proof.

## Event 149 retirement

Event 149 `Immigrations` is retired and absorbed into this system. No replacement event ID, event object, event-pool registration, flat population drain, event-log row, or event-pacing pulse is permitted, and state/accounting pulses are not event pacing.

## Open evidence gates

- Complete all named probability comparison scenarios for border policy, destination selection, outbreak reception, evacuation, corridor acceptance, return, integration, resettlement, opposition, and cleanup through a callable `chaosx_ai_probability_auditor`; direct MCP inspection remains evidence only.
- Close only external adapters whose owners provide exact receipts; retain missing owner data as explicit blockers.
- Obtain supported runtime visual evidence for the hardcoded mapmode window if the tooling exposes it.
- Reconcile the remaining specialist audit routes whose current handoffs are frozen snapshots; current direct inspect artifacts, typed-fixture limits, and unavailable custom-pool routes are recorded in `ai_probability_current.md`.

## Future extensions

Future depth should prefer richer exact route ownership, bilateral reception agreements, and cohort-specific political consequences over new headline meters. Any extension must preserve sparse scheduling, exact transfer conservation, shared validity for human and AI choices, and the separate migration namespace.
