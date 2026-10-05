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

Each input is clamped to 0 through 100. The score is:

`clamp(((1.15 * production) + (1.10 * transport) + (1.25 * extraction) + (1.00 * need) + (0.80 * environment) + (0.90 * vulnerability) + (0.95 * governance) - (1.20 * relief)) / 2.5, 0, 200)`.

The divisor (`famine_food_weight.pressure_normalizer`) is deliberately smaller than the sum of the weights: two or three strongly pressed causes reach acute shortage or famine without every component being high at once.

Stable is below 25. Supply strain begins at 25, acute shortage at 50, famine at 75, and catastrophic famine at 100.

The committed stage moves one step at a time. Each step upward needs its requested stage held for 7 days (supply strain), 14 (acute shortage), 21 (famine) or 30 (catastrophic famine), so a state passes at least 42 days of warning before famine. Each step down needs the score below 20, 40, 60 or 80 for 14, 21, 21 or 30 days, so recovery is gradual and a 35-day relief delivery can lift a famine or catastrophic famine by one stage.

### Reserves and exhaustion

Reserves are thousand-person-days. A state's first assessment seeds half of its reserve target (30 days of need scaled by delivery efficiency), and reserve stock adds up to 35 relief points.

The unrelieved shortage, the same sum before relief, is stored as `famine_food_deficit_score`. While it is at supply strain or above, the reserve is drawn by 25, 50, 75 or 100 percent of daily need for the matching stage, even when the reserve still holds the visible score below supply strain, and a cut-off island draws at least 60 percent of daily need. Only a settled stable state with no shortage replenishes, and a state whose stored shortage is still at supply strain stays registered.

When the reserve covers fewer than 7 days under a real shortage or a proven island blockade, unmet need rises in proportion to the missing days, up to 55 points. This is the step that turns a buffered shortage into a deeper stage once stocks run out.

### Expected outcomes

A scratch model of these formulas with the current constants (recorded in `docs/plans/famine_and_migration_system_plans/agent_decisions_2026-10-04.md`, decision 17) gives:

- Peacetime states, islands at war with a working port and escorts, standard occupation, and every historical anchor at the 1936 start stay stable.
- A proven island blockade with a low reserve reaches supply strain in about two weeks, acute shortage in about six weeks, and famine after about three months; Air Contamination or camps can push it to catastrophic famine.
- Extraction and forced-labour occupation reach acute shortage; collective-punishment and exterminatory occupation reach famine.
- A normal or thermonuclear strike reaches acute shortage.
- Reactivated Leningrad, Bengal, Henan, Greece and Ethiopia profiles reach famine; Spain and the Soviet memory profile under a live shock reach acute shortage; the Irish memory profile reaches supply strain.
- A relief delivery lifts the state at least one stage, and sustained relief holds a reactivated profile at acute shortage.

Trapped-population need is population-scaled as `clamp((trapped people / live state population) * 100, 0, 100)`. It enters need and vulnerability only through the explicit migration adapter.

## Mortality and Deaths ownership

`famine_apply_mortality` runs only after the severe-stage exposure and due-date contract passes. It reads live population through the exact state-population API, applies the stage rate and bounded exposure, vulnerability, relief, extraction, environment, access, and governance factors, and respects the protected population floor.

The stage rates are 0.03 percent of the population every 14 days for acute shortage, 0.08 percent every 7 days for famine, and 0.2 percent every 3 days for catastrophic famine. The product of the vulnerability, access, policy, environment and governance factors is capped at 2.5, exposure adds up to a threefold multiplier over 200 days, and relief reduces the pulse in proportion. Unmanaged famine therefore removes about 1.5 percent of a state's population each month, and catastrophic famine without relief removes a third or more over five months, while the protected floor keeps at least 15 percent of the state's population after every pulse.

The famine owner performs one population debit and records the same applied amount under `constant:chaos_meter_deaths_reason.famine`, localized as `From famine`. No migration or adapter path applies a second debit for that mortality.

The formula uses no fixed historical death total. Historical profiles provide starting context and bounded eligibility, while current state population and current conditions determine outcomes.

## Blockade proof

Island blockade famine is not inferred from island status. The blockade branch requires current war, geographic isolation, maritime dependence, port or route disruption, convoy or escort shortage, inadequate local supply, and absence of a proven relief corridor. Missing evidence fails closed.

Local supply is inadequate when the reserve covers fewer than 7 days, or fewer than 14 days while local production pressure is at least 20. While every physical clause except local supply holds (`famine_blockade_isolation_proof`), the island's imports are cut and its reserve drains, so an ordinary island reaches the full proof once its stock runs low. A proven blockade adds transport, need and vulnerability pressure that grows by 0.5 a day up to 40.

## Decisions and missions

Famine owns its own category and phased actions, including reserve release, emergency imports, route repair, escorted relief convoy, emergency airlift, invited relief, famine evacuation, safer-state requisition, concealment, and extraction policy.

Famine missions own relief-route security and reserve-failure deadlines. Migration missions are never counted in famine mission slots or presented as famine actions.

Legacy action fees use `humanitarian_legacy_cost_constants.txt` and the exact inclusive country-payer bundle predicates documented in `humanitarian_legacy_cost_triggers.md`.
The stable cost getters and texticons display country-local quote values refreshed at existing phase and exact active-state registration boundaries; cached display values do not authorize payment or refunds.
Delayed work requires its own action/state/payer paid receipt, and relief actions additionally bind the exact paid contract generation, mode and donor before continuation.
Rejected uncharged setup cannot deliver reserves, grant invitation rewards or claim a refund; funded work keeps its existing risks, and famine evacuation refunds only its matching paid tuple when measured origin debit is zero.
These are action costs and private ownership evidence, not additional player-facing famine values or a shared decision category.

## Sparse runtime

The runtime processes registered historical anchors, candidates, and active famine states through the existing host-only coordinator. State changes and exact owner callbacks register or invalidate only affected scopes. No whole-world daily, weekly, or monthly scan is added.

Famine retirement is owner-local: a stable, pressure-free, non-blockaded state with no positive famine-owned reception-demand projection and no stored shortage at supply strain leaves only the famine registry and clears only famine state. It neither waits for migration obligations nor reconciles or cleans migration cohorts; any migration registry entry created through the survivor-flight adapter continues under migration ownership.

## Adapters

Deliberately blocking relief from a famine or catastrophic famine state is condemned as relief obstruction. A receiving country that rejects an evacuation corridor from such a state, or lets the request lapse unanswered, while its safe front and reception capacity had room for everyone the corridor carried, is condemned for the corridor's measured people; a receiver that could not have accepted is not condemned; a country that captures the donor state of a live relief contract and breaks it is condemned for the people that contract would have fed. Each corridor or contract generation condemns only once, and the request values are cleared after every attempt.

Famine accepts explicit, owner-proven changes from occupation conduct, extraction, camps, forced labor, bombing, nuclear damage, fallout, outbreaks, natural disasters, war, relief, condemnation, and relevant event or scenario owners. An adapter must provide the state, actor, source, amount or normalized component, and the required generation/revision proof. Missing facts remain API-only blockers and do not produce a guessed pressure pulse.

Famine can create a migration flight request only after the famine state and affected people are proven. That connection does not merge the two mechanics.

A successful Hunger Lines launch (Event 014, scenario SCN-010) calls `famine_apply_hunger_lines_scenario_pressure` once from the shared scenario launcher.
It reads only Event 014's node registry and launch intensity, and gives each live node state a scenario food shock, a scenario food context on production, transport, governance and vulnerability that lasts 120 days, and scenario flight pressure for migration.
The lowest intensity reaches supply strain (and acute shortage only after the reserve runs out), and the maximum reaches famine about 44 days after launch; a relaunch inside a state's 120-day window adds nothing to that state.
The values sit in `famine_hunger_lines_scenario` in `famine_adapter_constants.txt`.

A hostile capture of a state queues one food-safety assessment through `famine_enqueue_food_observation_assessment` from the hostile-capture adapter in `common/scripted_effects/humanitarian_capture_effects.txt`.
The ordinary food job then reads the occupation law through `famine_resolve_occupation_profile` and decides whether a real food problem exists; the capture itself adds no famine stage and no deaths.

The famine evacuation action proves an active famine problem and route request, then crosses narrow migration-owned availability, trapped-obligation, exact-transfer, and mission-finalization seams. Famine decision script does not inspect or mutate migration reception load, preparation state, displacement state, cohort records, mission subjects, deadlines, slot ledgers, or mission flags.

Famine also owns the versioned `famine_to_migration_*` destination-food-safety projection. It publishes only from initialized famine facts and otherwise invalidates the receipt; it never treats an untracked state as implicitly stable. Migration consumes this projection for bounded registered reception states and adjacent destination candidates without reading raw famine variables.

Famine blockade evaluation refreshes neutral physical railway damage through `civilian_transfer_refresh_route_damage_projection` from the famine sparse state job. It does not depend on a migration registry pulse. Relief donor and safer-state decisions consume migration-owned persecution, reception-policy, and native-hazard triggers rather than raw migration flags or variables.

The reverse connection uses `migration_to_famine_reception_demand_*`. Migration publishes the exact trapped people amount, cause, schema, generation, revision, and proof; famine validates it and stores `famine_reception_demand_population`. Food need and vulnerability normalize only that famine-owned receipt against live state population.

## Assets and mapmode

Famine assets use `famine_*` filenames and sprite identifiers. `interface/famine_system.gfx` owns the category, decision, state-modifier, and achievement sprites; `interface/chaosx_texticons.gfx` owns the famine Deaths texticon; `interface/famine_report_pictures.gfx` and `interface/famine_report_header.gui` own the compact famine report art consumer; `interface/mapmodes_interface.gfx` owns the two famine mapmode button states.

The famine mapmode uses five food-security fills and independent borders for blockade proof, relief access, and pressure direction.

The current documentation inventory contains 61 declared final DDS outputs across the package: 50 root-manifest assets, seven report images, and four mapmode buttons. Category-asset closure reconciles the famine and migration category consumers, and the parent contact-sheet review accepted every visual family. Live in-game consumer validation remains user-owned.

## CXT fixture

`famine_register_cxt_test_content` registers `chaosx_cxt_extension_famine`. Its idempotent apply effect writes three capital-state inputs at `famine_cxt_fixture.input_pressure` with `input_relief` relief and an empty reserve, which settles in supply strain with no migration route, population transfer, severe famine, or mortality transaction.

## Open evidence gates

- Complete the named probability comparison scenarios for famine responses, relief donors, requisition donors, blockade response, extraction, opposition, and cleanup through a callable `chaosx_ai_probability_auditor`; direct MCP inspection remains evidence only.
- Close only those external adapters whose owners can supply the exact required receipt; retain all other blockers explicitly.
- Obtain supported runtime visual evidence for the hardcoded mapmode window if the tooling exposes it.
- Reconcile the remaining specialist audit routes whose current handoffs are frozen snapshots; current direct inspect artifacts, typed-fixture limits, and unavailable custom-pool routes are recorded in `ai_probability_current.md`.

## Future extensions

Future depth should prefer new exact owner adapters, regional relief logistics, and historically grounded starting profiles over additional player-facing meters. Any extension must preserve population scaling, sparse scheduling, single Deaths ownership, and the separate famine namespace.
