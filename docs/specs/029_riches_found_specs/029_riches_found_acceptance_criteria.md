# Event 029: Acceptance criteria and test scenarios

## Status of this file

These are implementation and live-test acceptance criteria.

They have not been executed in this planning environment.

The implementation agent must satisfy the source-review, MCP, audit, asset, documentation, and catalog requirements before claiming Event 029 complete.

The user owns live HOI4 validation unless the autonomous debug-playtest skill is explicitly invoked in a later task.

## Source review gate

Before editing the repository, the implementation agent must read:

- repository `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
- relevant portions of `CHAOS_REDUX_MECHANICS`
- this complete spec package
- current Event 018 implementation and docs
- current event log, Event Details, repeatable-event, controller-transfer, state-modifier, Deaths, Condemnation, and dynamic-effect patterns
- relevant offline Paradox wiki pages
- relevant installed vanilla documentation
- at least one vanilla event, decision, mission, dynamic modifier, occupation transfer, and state-control precedent

The implementation agent must inspect the actual repository and cannot treat this package as proof of current file names or engine behavior.

## MCP gate

Use the installed HOI4 MCP routes for every supported surface.

Required Event 029 evidence includes:

- `hoi4.event_inspect` on the existing Event 029 entry and any reworked chain
- `hoi4.event_render` for the final event chain
- `hoi4.event_compare` against the pre-rework source
- `hoi4.probability_inspect` on every complex weighted surface
- probability evaluation, sweeps, rendering, and compare evidence from the named scenario file
- GUI inspection only if the final implementation changes a shared category attachment or creates a justified event-owned GUI, which this spec does not require
- map inspection when a decision builds or validates a rail, port, or state route through exact map data

If a required MCP route is unavailable, record the exact blocker.

Source-only review is not equivalent evidence.

## Event registration

Event 029 must:

- retain entry identity `chaosx.nr29.1`
- be registered as Minor Repeatable
- use the shared repeatable weight recovery and cap-halving system
- remain outside every cluster unless the user approves a later change
- have one reusable valid-target gate
- show `N/A` when no valid country and state pair exists
- return to the default-enabled allowlist only when the rework is ready for ordinary selection
- resolve its visible name in normal event, debug, log, and Event Details selectors

## Initial firing

A normal firing passes when:

- exactly one valid ordinary country is selected
- exactly one suitable owned and controlled state is selected
- the state is not already an Event 018 site or Event 029 mine
- the recipient receives exactly 1,000 political power once
- the state receives one persistent Event 029 identity
- the mine registry receives one aligned entry
- original discoverer and current controller are stored
- initial quality, commodity profile, values, and operating state are initialized
- the report names the correct country and state
- the event history records Event 029 once with the correct actor
- the decision category becomes available to the controller
- no unrelated country receives the positive modifier or decisions

Failure conditions include:

- two states selected
- grant applied twice
- invalid special or nonhuman country selected
- Event 018 state selected
- mine state created without a registry entry
- event history recorded before a valid actor can be resolved
- raw localisation keys or placeholder images

## Suitable-state tests

### `RF_TEST_STATE_01_CORE_INLAND`

Setup: Ordinary country with several core inland states.

Expected result: A populated, buildable, connected state is selected through weighted randomness.

The capital is possible but not forced.

### `RF_TEST_STATE_02_ISLAND`

Setup: Country owns a populated island with a usable port and an empty remote island.

Expected result: The populated usable state can qualify.

The empty remote island receives zero or near-zero suitability and must not be selected when a better state exists.

### `RF_TEST_STATE_03_NO_VALID_STATE`

Setup: Existing country whose owned states are all excluded, ruined, already reserved, or uncontrolled.

Expected result: Event 029 is unavailable and shows `N/A`.

No queue or partial event state is created.

### `RF_TEST_STATE_04_EVENT_018_CONFLICT`

Setup: State has Event 018 persistent resource-site identity.

Expected result: State is ineligible for Event 029.

### `RF_TEST_STATE_05_EXISTING_MINE`

Setup: Country already controls one Event 029 mine and has one other valid state.

Expected result: Later firing can select the other state and cannot select the first mine again.

## Persistent state and controller transfer

### `RF_TEST_TRANSFER_01_OCCUPATION`

Setup: Country A controls an active mine. Country B occupies the state during war.

Expected result:

- Country A loses the mine contribution once
- Country B gains a reduced occupation contribution once
- state values, development, damage, contracts, and evolution history remain
- Country B receives occupation-appropriate decisions
- Country A's mine-specific missions cancel
- no duplicate controller exists

### `RF_TEST_TRANSFER_02_RECAPTURE`

Setup: Country A recaptures the mine.

Expected result:

- Country B loses the contribution
- Country A regains a contribution based on current damage and state, not the prewar value
- completed projects remain completed
- damage remains until repaired

### `RF_TEST_TRANSFER_03_ANNEXATION`

Setup: Country B annexes Country A and gains the state.

Expected result: One clean transfer, one current controller, one surviving local state, and one contract evaluation.

### `RF_TEST_TRANSFER_04_RELEASE`

Setup: Country B releases Country C with the mine state.

Expected result: Country C gains the ongoing system and does not receive another 1,000 political power unless selected by a separate future Event 029 firing.

### `RF_TEST_TRANSFER_05_CIVIL_WAR`

Setup: Mine state changes between civil-war sides.

Expected result: Contribution follows actual controller and cannot be counted for both sides.

### `RF_TEST_TRANSFER_06_MULTI_MINE`

Setup: Country A controls three mines, then loses one.

Expected result: Aggregate recalculates from two controlled mines with the correct diminishing-return order and no stale contribution.

## Visible values

The category passes when:

- Extraction Pressure, Mine Development, Local Order, and Revenue Legitimacy display as whole, readable values
- each value has a concise tooltip explaining meaning, main causes, next threshold, consequence, and player response
- value colors and icons remain consistent across category, decisions, missions, events, modifiers, and tooltips
- hidden capture, concession exposure, deep excavation, Gold Disease pressure, and supernatural pressure are not exposed as raw numbers
- visible incidents and decisions still explain why the hidden state matters
- values persist through save and reload
- values follow the mine state through controller transfer

## Baseline progression

### Discovery and claims

Pass conditions:

- one claims policy is chosen or one default policy is established
- Survey the Discovery can complete
- claim incidents respond to the policy
- a claims mission can succeed, partially succeed, or fail
- failure starts a more violent rush and does not delete the mine

### Rush

Pass conditions:

- camp administration, labor, services, and settlement actions use meaningful costs
- migration and settlement pressure appear through incidents and modifiers
- public projects improve the state through one-time or mission-backed changes
- no repeatable free building loop exists
- local and imported workforce routes produce different consequences

### Development

Pass conditions:

- geography controls rail, port, convoy, and transport decisions
- deep-mine safety projects affect collapse risk
- Drive Deeper raises reward ceiling and pressure
- project failure can damage time and resources
- completed projects cannot be duplicated after controller transfer or cancellation

### Revenue settlement

Pass conditions:

- dividend, local share, central receipts, stabilization fund, participation, and patronage produce distinct short-term and long-term effects
- a one-time dividend does not erase entrenched corruption
- stabilization reserves cannot be withdrawn repeatedly for free rewards
- centralization improves current receipts and raises dependence when oversight is weak

### Concessions

Pass conditions:

- foreign actor pool is plausible and bounded
- hostile actors cannot sign cooperative contracts unless a coercive route is valid
- one exclusive concession maximum exists per mine
- limited contracts remain compatible only when their terms do not conflict
- contract disclosure and beneficial-owner checks affect risk
- nationalization, buyout, expiry, renewal, transfer, and collapse cleanup work
- infrastructure rewards cannot duplicate through contract cycling

### Security and raids

Pass conditions:

- mine police, private guards, army cordon, armed workers, negotiation, and military clearing produce distinct order and legitimacy outcomes
- army actions require actual units, supply, and bounded physical costs where specified
- raids target a concrete asset or route
- deaths and damage apply once
- private guards can become a political problem
- obsolete security decisions hide after resolution

### Closure and recovery

Pass conditions:

- temporary closure stops positive output and lowers pressure through time or mission state
- reopening requires a valid recovery route
- partial sealing lowers output and deep risk
- permanent sealing ends ordinary reopening
- collapse severity is tied to state and pressure
- repairs restore damaged development without duplicating project rewards

## Decision category clarity

The category passes when:

- one selected mine is clear
- one primary value and three supporting values remain readable
- current phase normally exposes three to five primary decisions
- six primary decisions is never exceeded in one phase
- one to three active missions are visible
- emergency actions replace obsolete ordinary actions
- multiple mines use selected-mine management instead of duplicate walls of decisions
- every button-shaped element is a real action or clearly disabled state
- no fake controls appear in the category picture
- headers remain concise
- one action tooltip normally fits within two to four short lines unless a complex contract needs a justified longer explanation

## Cost tests

Every action passes when:

- it uses no more than four spendable cost types
- the visible cost string uses correct texticons
- non-cost requirements are separated from spendable costs
- dynamic costs use the same calculation in tooltip, availability, AI, and effect
- blocked reasons identify the missing resource, route, unit, state, contract, or value
- command-power costs remain conservative and below the project maximum
- physical projects do not default to political power

## Mission tests

Every mission passes when:

- the objective requires real player or AI action
- duration matches difficulty
- success, partial success where used, and failure call distinct logic
- the mission does not auto-complete from a condition already satisfied before it began unless the start effect intentionally records a fresh requirement
- target states and route states are named through dynamic localisation
- loss of control cancels or transfers the mission safely
- duplicate missions cannot run for the same mine and objective

Required mission scenarios:

- Secure the First Rush
- Open the Railhead or valid port equivalent
- Protect the Pay Train
- Break the Claim War
- Restore the Shaft
- Hold the Mine During War
- Complete the Public Settlement
- Audit the Concession

## Evolution I tests

### `RF_TEST_EVO1_01_DELAYED_MANAGED`

Setup: Chaos 600+, high legitimacy, high order, moderate pressure, public settlement.

Expected result: Evolution I remains possible but heavily delayed or starved while management remains strong.

### `RF_TEST_EVO1_02_CAPTURED`

Setup: Chaos 600+, high pressure, exclusive concession, private guards, failed audit, low legitimacy.

Expected result: The Resource Curse enters through paced timing, records once, and opens its evolved decisions and controller idea stage.

### `RF_TEST_EVO1_03_DISABLED`

Setup: Evolution I disabled before conditions are met.

Expected result: No evolution record, evolved idea, Gilded Sovereignty route, or hidden activation flag.

Baseline corruption incidents can still occur.

### `RF_TEST_GILDED_01`

Setup: Resource Curse active, high development, private authority, government dependence, very low legitimacy.

Expected result: The Gilded Sovereignty appears as a late crisis outcome without a fourth evolution-log stage.

### `RF_TEST_GILDED_02_RECOVERY`

Setup: Gilded Sovereignty active.

Expected result: A non-destructive reform or buyout can restore public administration and keep the mine operating.

## Evolution II tests

### `RF_TEST_EVO2_01_ENTRY`

Setup: Chaos 800+, high pressure, low order, repeated theft, private guards.

Expected result: Gold Disease enters through a paced incident, records once, and does not use the biological outbreak system.

### `RF_TEST_EVO2_02_CONTAINMENT`

Setup: Gold Disease active.

Expected result: Revenue sharing, controlled access, closure, and sealed sections reduce pressure across several steps.

One click does not cure it.

### `RF_TEST_EVO2_03_MOVEMENT`

Setup: Affected workforce or shipment moves through a defined event route.

Expected result: One bounded follow-up incident can occur in the destination context.

No whole-world scan or biological outbreak state appears.

### `RF_TEST_EVO2_04_MASS_VIOLENCE`

Setup: Military clearing or guard mutiny causes deaths.

Expected result: Exact population or military deaths are recorded once, public evidence feeds Condemnation, and no positive farming reward appears.

### `RF_TEST_EVO2_05_DISABLED`

Expected result: No syndrome state, quarantine action, movement route, or Gold Disease report can activate.

## Evolution III tests

Before any Evolution III scenario, verify that 1,000+ chaos alone does not bypass an active incompatible `world_end` state. New Event 029 evolution jobs must remain blocked after that terminal state begins unless the terminal owner explicitly permits continuation.

### `RF_TEST_EVO3_01_ENTRY`

Setup: Chaos 1,000+, deep mine, high pressure, repeated deepening, opened section.

Expected result: Demons Beneath the Mine enters through paced local conditions and records once.

It does not call Event 018 caves, Oth-Kesh, or The World Opens Below.

### `RF_TEST_EVO3_02_CONTAINMENT`

Setup: Supernatural mine with completed evacuation and intact sealing route.

Expected result: Permanent sealing can end positive output and most active incidents with bounded aftermath.

### `RF_TEST_EVO3_03_ASSISTANCE`

Setup: Valid scientific, religious, or occult assistance route.

Expected result: The route changes Event 029 containment only.

It does not create Event 016 project history or unsupported real religious claims.

### `RF_TEST_ACCOUNT_01_ENTRY`

Setup: Supernatural agreement accepted under high pressure and dependence.

Expected result: The Bottomless Account appears as a late outcome inside Evolution III, not as Evolution V or a world-end scenario.

### `RF_TEST_ACCOUNT_02_NO_DEATH_FARMING`

Setup: Unrelated combat, bombing, genocide, or disease deaths occur.

Expected result: They cannot satisfy an account obligation.

### `RF_TEST_EVO3_04_DISABLED`

Expected result: No supernatural pressure, report, bargain, or late account route can activate.

## Shared-system tests

### Deaths

Every Event 029 population-loss route must:

- calculate one exact bounded amount
- use the correct civilian or military classification
- use a distinct Event 029 reason
- remove population once
- create one Deaths log entry when the system is enabled
- avoid recruitable-manpower gain from negative state population

### Condemnation

Test exposed:

- forced labor
- massacre
- private-security abuse
- military purge
- forced entombment
- blocked inspection
- destroyed records
- coverup

Expected result: Public responsibility adds the correct source and tier pressure.

Hidden evidence stays hidden until exposure.

### Chaos

Test:

- managed public settlement
- claim war
- major raid
- massacre
- catastrophic collapse
- demonic bargain

Expected result: Each source changes chaos once and uses event-specific severity.

### Event 013

Expected result: Only a valid exact-state physical disaster call uses the public Event 013 API.

Ordinary mine collapse remains Event 029-owned.

### Event 016

Expected result: Assistance changes Event 029 state without creating Event 016 host, project, technology, facility, or log history unless a separately accepted adapter explicitly permits one reward.

### Event 018

Expected result: State markers are mutually exclusive and no Event 018 branch is inherited.

### Event 019

Expected result: No new unit-family registration exists unless implementation added a real custom combat subunit, which would require a separate accepted scope.

## Repeatable-event tests

### `RF_TEST_REPEAT_01_TWO_COUNTRIES`

Fire Event 029 twice through ordinary or controlled test setup for two countries.

Expected result: Two independent mine states, two one-time grants, separate values, separate controllers, shared global event weight behavior.

### `RF_TEST_REPEAT_02_SAME_COUNTRY`

Fire Event 029 twice for one country with two valid states.

Expected result: Two mine entries, one grant per firing, diminishing aggregate, one category with selected-mine flow.

### `RF_TEST_REPEAT_03_WEIGHT`

Expected result: Event 029 uses shared repeatable cap-halving and recovery.

It does not create a private recovery timer.

## Aggregate balance tests

Test one, two, three, and four controlled mines at equal quality and condition.

Expected ordering:

- total benefit rises with each mine
- marginal benefit falls with each mine
- country cap is never exceeded
- local state value remains meaningful
- losing one mine recalculates cleanly
- closing one mine removes only its contribution
- occupied mine contributes less than a secure core mine

The first mine must feel significant.

Three or more mines must not replace a full national economic route.

## Exact 1,000 political-power tests

Record political power before and after one firing for:

- player democracy
- player authoritarian state
- AI major
- AI minor
- country near any engine or scripted cap
- country with active political-power spending systems

Expected result: The event attempts to grant exactly 1,000 once.

Any engine cap or loss is documented.

The implementation must not conceal a smaller actual grant behind the event text.

AI behavior should be observed over a bounded period to identify law, advisor, and decision spikes.

A balance problem must be reported to the user before changing the amount.

## AI probability acceptance

Use every scenario in `029_riches_found_ai_probability_scenarios.md`.

A weighted surface passes when:

- invalid choices have zero effective availability or weight
- intended first choice ranks first under the named state
- plausible alternatives are not starved without a design reason
- dangerous routes require their intended ideology, desperation, crisis, or chaos conditions
- evolution timing responds materially to pressure and containment
- incident pools do not spam one result
- foreign actors require plausible access and interest
- post-patch compare evidence uses the same scenarios

## Localisation acceptance

Every visible key must have final in-world wording.

Required surfaces include:

- entry event
- reports
- news only when implementation adds a valid global report
- decisions
- missions
- costs
- blocked costs
- requirements
- dynamic selected-state text
- dynamic foreign-actor text
- state modifiers
- controller idea stages
- evolution names and details
- Event Details
- event log names
- achievement titles and descriptions
- asset tooltips where used
- catalog-facing wording

The localisation audit must find:

- no missing keys
- no duplicate conflicting keys
- no placeholder directions copied from the spec
- no raw variables or raw triggers
- no implementation-history wording
- no false biological language for Gold Disease
- no copied living religious or mining tradition presented as demonic fact
- no unsupported exact effect claim

## Asset acceptance

Every required asset row must have:

- stable runtime basename
- source mode
- source image or generated source
- prompt or provenance
- processed PNG
- final DDS
- correct runtime folder
- sprite handoff
- manifest or promoted permanent evidence
- contact-sheet review
- native-size readability
- correct alpha treatment
- no generated text
- no primitive placeholder
- no icon-type substitution

The implementation must wire every sprite and consumer.

A final asset remaining as a placeholder is a blocker unless the user explicitly approved that state.

## Achievement acceptance

Every achievement must have:

- stable ID
- root registry entry
- exact eligibility and disqualifier tracking
- save-persistent historical flags or variables
- unlock trigger
- localisation
- completed, grey, and not-eligible icons
- docs
- route or evolution hooks
- test scenario

Hard achievements must not unlock from a simple final state that ignores their historical route.

## Event log acceptance

Event 029 passes log integration when:

- normal firing appears once in History
- actor name and flag are correct
- Event Details premise is complete
- live weight and fired count are correct
- unavailable target state shows `N/A`
- three evolution catalog rows exist
- each enabled evolution records once when it enters
- disabled evolutions do not record or unlock content
- main Evolutions and selected History details show real date, source event, evolution name, tier, stage, actor, and enabled state
- Event Details evolution previews do not show fake history metadata
- ordinary phases do not appear as evolutions
- Gilded Sovereignty and Bottomless Account do not create fourth or fifth evolution rows

## Catalog acceptance

The authoritative workbook is updated after implementation facts are known.

Required fields include:

- event status
- type
- chaos level
- cluster state
- event detail
- three evolution details
- any testing status used by the workbook

The workbook remains the only editable source.

After saving it, run `python .tools/export_event_catalog_csv.py`.

Do not edit the CSV exports directly.

Catalog wording must match Event Details and evolution-detail localisation.

## Save and reload scenarios

Save and reload after:

- first discovery
- project mission start
- concession signing
- controller transfer
- temporary closure
- Resource Curse entry
- Gold Disease containment
- Demons entry
- Gilded Sovereignty
- Bottomless Account obligation
- permanent sealing
- three-mine aggregate

Expected result: State, controller, values, missions, contracts, evolutions, contributions, and decisions remain coherent.

## Cleanup scenarios

Test cleanup after:

- mine state lost
- country annexed
- country released
- concession actor annexed
- war ends
- mission target invalidates
- mine permanently sealed
- mine catastrophically destroyed
- selected human mine becomes invalid
- evolution disabled before entry
- event disabled before another firing

No stale decision, mission, event target, contribution, modifier, or foreign contract may remain.

## Performance acceptance

The implementation must identify every recurring hook.

It passes when:

- no unauthorized whole-world daily, weekly, or monthly scan is added
- mine processing is bounded to registered mines and relevant controllers
- incident jobs and transfer refreshes are event-driven or use a proven scoped pattern
- multiple mines do not create runaway popup or log spam
- aggregate rebuilding occurs only when relevant state changes

## Completion audits

Before completion claim, use:

- `chaosx_ai_probability_auditor` for weighted and timing surfaces
- `chaosx_decision_mission_auditor` for decisions, missions, costs, clutter, cleanup, and exploits
- `chaosx_localisation_auditor` for all player-facing text
- `chaosx_event_completion_auditor` for full spec-versus-implementation review
- asset subagents and parent review for every visible asset
- `chaosx_spreadsheet_doc_worker` after implementation wording is final

A broad design gap found by an auditor goes to `chaosx_improvement_loop_planner` only after this accepted specification has been implemented or formally queued, rejected, or amended.

## Completion report content

The final implementation report must list:

- files changed
- event and helper IDs
- decisions and missions
- values and tuning files
- controller-transfer behavior
- AI and probability evidence
- evolution behavior
- Deaths and Condemnation integration
- Event 018 separation
- assets created and wired
- achievements
- event log and Event Details
- docs and workbook updates
- task-specific validation findings
- unresolved blockers
- simplifications, fallbacks, or omissions

If any accepted route, decision family, mission, evolution, late outcome, asset, AI behavior, achievement, log surface, documentation row, or controller-transfer behavior is missing, the event is incomplete.
