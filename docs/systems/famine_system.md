# Famine System

Status: implemented; current status, balance arithmetic and evidence limits are in [the 10 October improvement plan](../plans/famine_and_migration_system_plans/improvement_plan_2026-10-10.md).

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

A historical crisis profile (Henan 1942, Bengal 1943, Vietnam and Java 1944, Greece 1941, Leningrad, the Dutch Hunger Winter and early-1940s Spain) reactivates under its historical owner or controller, and when the war reaches the state itself or a food shock is recorded. Every profile except Spain also needs its owner or controller to be at war.
`famine_resolve_local_war_evidence` requires the state's controller to be at war and the state to be occupied, to border a state held by an enemy of its controller, to be under a harsher-than-standard occupation rule, to be a cut-off island, or to have lost local supply.
Bengal counts as one food region, because its rice came from Burma through East Bengal: an enemy-held state on the border of either Bengal anchor (Arakan, for example) opens the profile in both East and West Bengal.
A country fighting far from Bengal, Leningrad or Spain therefore does not starve those regions, which keeps Part 5's rule that a crisis does not fire once the campaign has removed its causes.

Trapped-population need is population-scaled as `clamp((trapped people / live state population) * 100, 0, 100)`. It enters need and vulnerability only through the explicit migration adapter.

## Mortality and Deaths ownership

`famine_apply_mortality` runs only after the severe-stage exposure and due-date contract passes. It reads live population through the exact state-population API, applies the stage rate and bounded exposure, vulnerability, relief, extraction, environment, access, and governance factors, and respects the protected population floor.

The stage rates are 0.03 percent of the population every 14 days for acute shortage, 0.08 percent every 7 days for famine, and 0.2 percent every 3 days for catastrophic famine. The product of the vulnerability, access, policy, environment and governance factors is capped at 2.5, exposure in the current stage adds 1 percent a day up to 2.8 times at the 180-day exposure cap, and relief reduces the pulse in proportion. Unmanaged famine therefore removes about 1.5 percent of a state's population each month, and catastrophic famine without relief removes a third or more over five months, while the protected floor keeps at least 15 percent of the state's population after every pulse.

The famine owner performs one population debit and records the same applied amount under `constant:chaos_meter_deaths_reason.famine`, localized as `From famine`. No migration or adapter path applies a second debit for that mortality.

The formula uses no fixed historical death total. Historical profiles provide starting context and bounded eligibility, while current state population and current conditions determine outcomes.

## Blockade proof

Island blockade famine is not inferred from island status. The blockade branch requires current war, geographic isolation, maritime dependence, port or route disruption, convoy or escort shortage, inadequate local supply, and absence of a proven relief corridor. Missing evidence fails closed.

Local supply is inadequate when the reserve covers fewer than 7 days, or fewer than 14 days while local production pressure is at least 20. While every physical clause except local supply holds (`famine_blockade_isolation_proof`), the island's imports are cut and its reserve drains, so an ordinary island reaches the full proof once its stock runs low. A proven blockade adds transport, need and vulnerability pressure that grows by 0.5 a day up to 40.

## Decisions and missions

Famine owns its own category and nine actions: Release Food Stores, Import Food (arranges a foreign land donor and delivers in one paid action), Restore Relief, Escort Relief and Airlift Relief for blockaded islands, Requisition Food from a safe neighbouring state, Evacuate, Conceal Hunger and Continue Requisitions.
Each is offered only by its own selected-state conditions; no action hides another country-wide.

Reserve release targets any registered state at supply strain or worse, or under a live food shock, that holds stock to release (`famine_state_can_release_reserves`). Released food keeps counting as covered days for reserve exhaustion and decays more slowly than stock drawn by a famine, so releasing early protects a state's food rather than shortening it.

AI urgency for Release Food Stores, Import Food, Escort Relief and Airlift Relief rises by 1.5, 2.5 and 4 times for acute shortage, famine and catastrophic famine in the selected state, Release Food Stores rises by half again at war, Import Food doubles for democracies and rises when trapped people add to a state's need, and Conceal Hunger and Continue Requisitions fall to half in famine and to a tenth in catastrophic famine (`famine_decision_ai`).

Conceal Hunger hides one state's crisis from the public for `famine_national_crisis.conceal_days` (90): it stops counting toward the national food crisis, its food shock rises by `conceal_pressure` (10), and the first famine deaths there are condemned as a cover-up. Continue Requisitions adds `extraction_pressure` (15) and war support. Both shocks are clamped to the 0–100 component range.

Famine missions own relief-route security and reserve-failure deadlines. Migration missions are never counted in famine mission slots or presented as famine actions.

Legacy action fees use `humanitarian_legacy_cost_constants.txt` and the exact inclusive country-payer bundle predicates documented in `humanitarian_legacy_cost_triggers.md`.
The stable cost getters and texticons display country-local quote values refreshed at existing phase and exact active-state registration boundaries; cached display values do not authorize payment or refunds.
Delayed work requires its own action/state/payer paid receipt, and relief actions additionally bind the exact paid contract generation, mode and donor before continuation.
Rejected uncharged setup cannot deliver reserves or claim a refund; funded work keeps its existing risks, and famine evacuation refunds only its matching paid tuple when measured origin debit is zero.
These are action costs and private ownership evidence, not additional player-facing famine values or a shared decision category.

## National food crisis

A famine is a national problem, not only a local one. Every visible state at acute shortage costs its owner 1% stability, every famine state 2% stability and 1% war support, and every catastrophic state 4% stability and 2% war support, through the `famine_national_food_crisis` country modifier (icon: the vanilla state-of-famine spirit), capped at −15% stability and −10% war support (`famine_national_crisis`).
Concealed states do not count until their concealment ends. The modifier disappears as soon as no visible state remains in crisis.

## Sparse runtime

The runtime processes registered historical anchors, candidates, active famine states and the countries that own or control them (`global.famine_active_countries`) through the existing host-only coordinator. The country job refreshes the famine decision phase and the national food crisis, independently of migration, and drops the country once its phase has settled. State changes and exact owner callbacks register or invalidate only affected scopes. No whole-world daily, weekly, or monthly scan is added.

Famine retirement is owner-local: a stable, pressure-free, non-blockaded state with no positive famine-owned reception-demand projection and no stored shortage at supply strain leaves only the famine registry and clears only famine state. It neither waits for migration obligations nor reconciles or cleans migration cohorts; any migration registry entry created through the survivor-flight adapter continues under migration ownership.

## Adapters

Deliberately blocking relief from a famine or catastrophic famine state is condemned as relief obstruction. A receiving country that rejects an evacuation corridor from such a state, or lets the request lapse unanswered, while its safe front and reception capacity had room for everyone the corridor carried, is condemned for the corridor's measured people; a receiver that could not have accepted is not condemned; a country that captures the donor state of a live relief contract and breaks it is condemned for the people that contract would have fed. Each corridor or contract generation condemns only once, and the request values are cleared after every attempt.

Famine accepts explicit, owner-proven changes from occupation conduct, extraction, camps, forced labor, bombing, nuclear damage, fallout, outbreaks, natural disasters, war, relief, condemnation, and relevant event or scenario owners. An adapter must provide the state, actor, source, amount or normalized component, and the required generation/revision proof. Missing facts remain API-only blockers and do not produce a guessed pressure pulse.

Famine can create a migration flight request only after the famine state and affected people are proven. That connection does not merge the two mechanics.

A successful Hunger Lines launch (Event 014, scenario SCN-010) calls `famine_apply_hunger_lines_scenario_pressure` once from the shared scenario launcher.
It reads only Event 014's node registry and launch intensity. Each live node state receives a scenario food shock and a scenario food context on production, transport, governance and vulnerability that lasts 120 days, loses its local stores to the seizure, and enters its starting stage on the day of the launch: acute shortage at Low, famine at Medium and above. The owner sees the Famine category, the map colours and the famine report at once, and the stage transition sends the ordinary famine survivor flight to migration.
With the stores gone the context holds that stage for the whole window (day-one scores of about 59, 79, 86 and 92 by intensity); imports, requisition, a restored route or evacuation bring it down through the ordinary recovery windows. A relaunch inside a state's 120-day window adds nothing to that state.
The values sit in `famine_hunger_lines_scenario` in `famine_adapter_constants.txt`.

A hostile capture of a state queues one food-safety assessment through `famine_enqueue_food_observation_assessment` from the hostile-capture adapter in `common/scripted_effects/humanitarian_capture_effects.txt`.
The ordinary food job then reads the occupation law through `famine_resolve_occupation_profile` and decides whether a real food problem exists; the capture itself adds no famine stage and no deaths.

Every assessed state collects local-war evidence through `famine_resolve_local_war_evidence`.
War adds 8 transport pressure and 4 unmet-need pressure only where the war reaches that state and its owner and controller are at war.
That contribution alone scores 5.2 against the supply-strain threshold of 25, so war elsewhere and standard occupation alone do not impose famine.

An accepted Black Plague food request sustains lost farm labor, disrupted transport, vulnerability, and unsafe-water pressure for 30 days.
An accepted Natural Disaster or Acid Rain food request sustains crop loss, damaged transport, and unmet need for 60 days.
The two context groups each contribute an unrelieved score of 28.4 before current stores, the food shock, exhaustion, relief, and other causes are applied.
Prepared stores buffer the interruption, while poor stores permit shortage as they run down.
Repeated accepted requests extend the corresponding window without stacking another copy of its pressure, and the next assessment drops the contribution when its date expires.
Retirement clears the dates.
The duration and component values are centralized in `famine_surface_context`, with no new scan, population debit, or incident popup.

China policy, Ceara, and Congo profiles use identical present-cause gates in selection and mapping.
All require positive live food pressure and their existing regional ownership or control.
Henan under CHI or PRC also requires extraction, concealment, forced labor, restricted departure, or occupation conduct.
Ceara under BRA also requires a disaster/resource-shortage cause, an open disaster food window, restricted departure, or an active camp.
Congo under BEL or FRA also requires occupation, non-core colonial ownership, local war, forced labor, or an active camp.
Those causes can occur in domestic states without resistance-based occupation, while peaceful zero-pressure historical anchors stay dormant.

Break the Blockade tracks concealed positive famine mortality against the credited country's exact blockade state and generation.
State-to-country achievement calls compare that country through nested `PREV`, independent of the effect chain's root.
A new tracked blockade generation clears the disqualifier, and an unrelated state, stale generation, or zero-loss pulse cannot set it.

The famine evacuation action proves an active famine problem and route request, then crosses narrow migration-owned availability, trapped-obligation, exact-transfer, and mission-finalization seams. Famine decision script does not inspect or mutate migration reception load, preparation state, displacement state, cohort records, mission subjects, deadlines, slot ledgers, or mission flags.

Famine also owns the versioned `famine_to_migration_*` destination-food-safety projection. It publishes only from initialized famine facts and otherwise invalidates the receipt; it never treats an untracked state as implicitly stable. Migration consumes this projection for bounded registered reception states and adjacent destination candidates without reading raw famine variables.

Famine blockade evaluation refreshes neutral physical railway damage through `civilian_transfer_refresh_route_damage_projection` from the famine sparse state job. It does not depend on a migration registry pulse. Relief donor and safer-state decisions consume migration-owned persecution, reception-policy, and native-hazard triggers rather than raw migration flags or variables.

The reverse connection uses `migration_to_famine_reception_demand_*`. Migration publishes the exact trapped people amount, cause, schema, generation, revision, and proof; famine validates it and stores `famine_reception_demand_population`. Food need and vulnerability normalize only that famine-owned receipt against live state population.

Event 037 Mysterious People tops up a food-need shock in crowded states at Overpopulation Pressure 60 or more through `famine_request_event_pressure` (source `event`), raising the state's food need toward the pressure minus 40 (`mysterious_people_adapter` constants). Famine decides what the shock does to the food state.

## Assets and mapmode

Famine assets use `famine_*` filenames and sprite identifiers. `interface/famine_system.gfx` owns the category, decision, state-modifier, and achievement sprites; `interface/chaosx_texticons.gfx` owns the famine Deaths texticon; `interface/famine_report_pictures.gfx` and `interface/famine_report_header.gui` own the compact famine report art consumer; `interface/mapmodes_interface.gfx` owns the two famine mapmode button states.

The famine mapmode uses five food-security fills and independent borders for blockade proof, relief access, and pressure direction.

The current documentation inventory contains 61 declared final DDS outputs across the package: 50 root-manifest assets, seven report images, and four mapmode buttons. Category-asset closure reconciles the famine and migration category consumers, and the parent contact-sheet review accepted every visual family. Live in-game consumer validation remains user-owned.

## CXT fixture

`famine_register_cxt_test_content` registers `chaosx_cxt_extension_famine`. Its idempotent apply effect writes three capital-state inputs at `famine_cxt_fixture.input_pressure` with `input_relief` relief and an empty reserve, which settles in supply strain with no migration route, population transfer, severe famine, or mortality transaction.

## Validation limits

Source review and bounded script checks cover the current behaviour; live campaign timing, native rendering and AI frequencies are user-run checks. The current record is section 6 of [the 10 October improvement plan](../plans/famine_and_migration_system_plans/improvement_plan_2026-10-10.md).

## Future extensions

Future depth should prefer new exact owner adapters, regional relief logistics, and historically grounded starting profiles over additional player-facing meters. Any extension must preserve population scaling, sparse scheduling, single Deaths ownership, and the separate famine namespace.
