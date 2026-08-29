# Famine System

Status: implemented source ledger pending the remaining probability, adapter, and completion audits. This is not a gameplay-completion claim.

## Ownership

Famine is an independent state mechanic. Its gameplay identifiers, variables, flags, effects, triggers, decisions, missions, localisation, sprites, and CXT fixture use the `famine_*` namespace.

The mechanic may submit explicit displacement pressure to migration when hunger causes people to move, but migration does not own food security, food reserves, relief access, or famine mortality.

The ordinary player surface is `famine_decision_category`. It is hidden while a country has no real food-security problem and appears for a genuine starting problem or supply strain and worse. Stable monitoring and migration activity alone do not reveal it.

`famine_register_initial_incident` is a famine accounting and presentation seam called from a proven upward state transition. It records the bounded state presentation and selects famine report context only; it does not create an event object, event ID, event-pool entry, event-log row, pacing pulse, random event, or population transaction.

The deleted `events/famine_incidents.txt` file and its incident constants are deliberate. Earlier incident-event and incident-option probability wording is superseded and is not a current implementation requirement.

The dedicated `famine_state_map_mode` remains available from campaign start so its legend and state colors can be understood before a crisis.

## Player-facing values

The decision surface presents one primary value and no more than two supporting values:

- Food Security: stable, supply strain, acute shortage, famine, or catastrophic famine.
- Food Reserves: the state-owned reserve ledger and capacity.
- Relief Access: current access and recovery direction.

These are presentation outputs. The evaluator retains additional internal components for causality and balance without requiring the player to learn a wall of meters.

## Canonical player-facing value count

Famine exposes exactly three canonical player-facing values: Food Security, Food Reserves, and Relief Access.

Internal conceptual components and ledgers, including food inputs, reserve capacity and consumption, relief receipts, mortality receipts, profile generations, revisions, and scheduler state, are implementation evidence rather than additional player-facing mechanics.

Raw variables, flags, temporary values, transaction receipts, and diagnostic tooltip details do not increase the canonical count; mapmode and report context remains contextual presentation.

## Food-security formula

Each input is clamped to 0 through 100. The normalized score is:

`clamp(((1.15 * production) + (1.10 * transport) + (1.25 * extraction) + (1.00 * need) + (0.80 * environment) + (0.90 * vulnerability) + (0.95 * governance) - (1.20 * relief)) / 7.15, 0, 200)`.

Stable is below 25. Supply strain begins at 25, acute shortage at 50, famine at 75, and catastrophic famine at 100.

Upward exposure durations are 7 days for supply strain, 14 for acute shortage, 21 for famine, and 30 for catastrophic famine. Recovery uses lower thresholds of 20, 40, 60, and 80 plus longer 14, 21, 30, and 45 day confirmation windows to prevent oscillation.

Trapped-population need is population-scaled as `clamp((trapped people / live state population) * 100, 0, 100)`. It enters need and vulnerability only through the explicit migration adapter.

## Mortality and Deaths ownership

`famine_apply_mortality` runs only after the severe-stage exposure and due-date contract passes. It reads live population through the exact state-population API, applies the stage rate and bounded exposure, vulnerability, relief, extraction, environment, access, and governance factors, and respects the protected population floor.

The famine owner performs one population debit and records the same applied amount under `constant:chaos_meter_deaths_reason.famine`, localized as `From famine`. No migration or adapter path applies a second debit for that mortality.

The formula uses no fixed historical death total. Historical profiles provide starting context and bounded eligibility, while current state population and current conditions determine outcomes.

## Blockade proof

Island blockade famine is not inferred from island status. The blockade branch requires current war, geographic isolation, maritime dependence, port or route disruption, convoy or escort shortage, inadequate local supply, and absence of a proven relief corridor. Missing evidence fails closed.

## Decisions and missions

Famine owns its own category and phased actions, including reserve release, emergency imports, route repair, escorted relief convoy, emergency airlift, invited relief, famine evacuation, safer-state requisition, concealment, and extraction policy.

Famine missions own relief-route security and reserve-failure deadlines. Migration missions are never counted in famine mission slots or presented as famine actions.

## Sparse runtime

The runtime processes registered historical anchors, candidates, and active famine states through the existing host-only coordinator. State changes and exact owner callbacks register or invalidate only affected scopes. No whole-world daily, weekly, or monthly scan is added.

Famine retirement is owner-local: a stable, pressure-free, non-blockaded state with no positive famine-owned reception-demand projection leaves only the famine registry and clears only famine state. It neither waits for migration obligations nor reconciles or cleans migration cohorts; any migration registry entry created through the survivor-flight adapter continues under migration ownership.

## Adapters

Famine accepts explicit, owner-proven changes from occupation conduct, extraction, camps, forced labor, bombing, nuclear damage, fallout, outbreaks, natural disasters, war, relief, condemnation, and relevant event or scenario owners. An adapter must provide the state, actor, source, amount or normalized component, and the required generation/revision proof. Missing facts remain API-only blockers and do not produce a guessed pressure pulse.

Famine can create a migration flight request only after the famine state and affected people are proven. That connection does not merge the two mechanics.

The famine evacuation action proves an active famine problem and route request, then crosses narrow migration-owned availability, trapped-obligation, exact-transfer, and mission-finalization seams. Famine decision script does not inspect or mutate migration reception load, preparation state, displacement state, cohort records, mission subjects, deadlines, slot ledgers, or mission flags.

Famine also owns the versioned `famine_to_migration_*` destination-food-safety projection. It publishes only from initialized famine facts and otherwise invalidates the receipt; it never treats an untracked state as implicitly stable. Migration consumes this projection for bounded registered reception states and adjacent destination candidates without reading raw famine variables.

Famine blockade evaluation refreshes neutral physical railway damage through `civilian_transfer_refresh_route_damage_projection` from the famine sparse state job. It does not depend on a migration registry pulse. Relief donor and safer-state decisions consume migration-owned persecution, reception-policy, and native-hazard triggers rather than raw migration flags or variables.

The reverse connection uses `migration_to_famine_reception_demand_*`. Migration publishes the exact trapped people amount, cause, schema, generation, revision, and proof; famine validates it and stores `famine_reception_demand_population`. Food need and vulnerability normalize only that famine-owned receipt against live state population.

## Assets and mapmode

Famine assets use `famine_*` filenames and sprite identifiers. `interface/famine_system.gfx` owns the category, decision, state-modifier, and achievement sprites; `interface/chaosx_texticons.gfx` owns the famine Deaths texticon; `interface/famine_report_pictures.gfx` and `interface/famine_report_header.gui` own the compact famine report art consumer; `interface/mapmodes_interface.gfx` owns the two famine mapmode button states.

The famine mapmode uses five food-security fills and independent borders for blockade proof, relief access, and pressure direction.

The current documentation inventory contains 61 declared final DDS outputs across the package: 50 root-manifest assets, seven report images, and four mapmode buttons. Category-asset closure reconciles the famine and migration category consumers, and the parent contact-sheet review accepted every visual family. Live in-game consumer validation remains user-owned.

## CXT fixture

`famine_register_cxt_test_content` registers `chaosx_cxt_extension_famine`. Its idempotent apply effect submits a capital-state supply-strain surface with no migration route, population transfer, severe famine, or mortality transaction.

## Open evidence gates

- Complete the named probability comparison scenarios for famine responses, relief donors, requisition donors, blockade response, extraction, opposition, and cleanup through a callable `chaosx_ai_probability_auditor`; direct MCP inspection remains evidence only.
- Close only those external adapters whose owners can supply the exact required receipt; retain all other blockers explicitly.
- Obtain supported runtime visual evidence for the hardcoded mapmode window if the tooling exposes it.
- Reconcile the remaining specialist audit routes whose current handoffs are frozen snapshots; current direct inspect artifacts, typed-fixture limits, and unavailable custom-pool routes are recorded in `ai_probability_current.md`.

## Future extensions

Future depth should prefer new exact owner adapters, regional relief logistics, and historically grounded starting profiles over additional player-facing meters. Any extension must preserve population scaling, sparse scheduling, single Deaths ownership, and the separate famine namespace.
