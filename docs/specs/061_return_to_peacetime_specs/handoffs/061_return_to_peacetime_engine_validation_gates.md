# Event 061 engine validation gates

## Purpose

These questions require local repository and installed Hearts of Iron IV evidence before implementation can be accepted.

The source design does not guess the final engine syntax.

## Gate 1: Physical building conversion

Prove:

- exact state-scope effect for removing one military factory level
- exact state-scope effect for adding one civilian factory level
- behavior at building-slot ceiling
- behavior with damaged building levels
- whether removal and addition can be validated before mutation
- safe rollback or precheck when the target addition cannot succeed
- current repository precedent for one-for-one building conversion

Required tests:

- zero, one, two, and many factories
- fully used state slots
- damaged factories
- ownership change during a decision
- save reload at completion

## Gate 2: State ledger persistence

Prove:

- state variables persist through ownership and control change
- the variable can be read by current owner decisions
- zero-value cleanup is safe
- state transfer does not duplicate a country cache
- supported ownership or control change hook for bounded reconciliation

## Gate 3: Economy and conscription law definitions

Prove:

- exact database and group used by current vanilla laws
- correct syntax for adding Peacetime Economy and No Army
- icon and localisation consumer paths
- adjacent law movement effect
- availability and AI handling
- law ranking across custom country systems
- behavior under subjects, governments in exile, and replaced law groups

## Gate 4: Law modifiers

Confirm that the intended modifier roles exist and behave as expected:

- military factory output
- dockyard output
- military factory construction speed
- civilian-to-military conversion cost or speed
- military-to-civilian conversion cost or speed
- production efficiency cap
- civilian construction speed
- repair speed
- recruitable population
- army training availability or training time
- army experience gain
- mobilization speed

Replace unsupported modifiers with the nearest clear mechanic and record the deviation.

## Gate 5: Safe conventional division disband

Prove with installed documentation and a live controlled test:

- exact scripted effect that disbands a selected division
- manpower return behavior
- equipment return behavior
- handling of unit leaders and army assignment
- behavior in combat, transport, encirclement, expeditionary status, and volunteers
- behavior for locked and event-owned special units
- reliable unit-scope eligibility tests

A destructive delete effect fails this gate.

## Gate 6: Division selection data

Confirm available script access for:

- division experience
- strength and equipment percentage
- combat state
- transport state
- encirclement
- state location
- assignment or front relevance
- template age or unit creation date
- owner markers for special unit families

When a desired input is unavailable, use a documented simpler selector and preserve hard exclusions.

## Gate 7: Stockpile inspection and exact debit

Prove:

- exact positive stockpile query by supported archetype
- current reinforcement and training need when available
- variant or generation selection support
- exact debit for artillery, anti-tank, anti-air, mechanized, armour, aircraft, and other planned ordinary families
- safe interaction with captured variants and lend-lease commitments
- actual completed debit result for reward calculation

Unsupported families remain excluded until a safe helper exists.

## Gate 8: Temporary civilian factory commitment

Confirm the universal cost framework supports:

- dynamic commitment amount
- long-running decision duration
- cancellation
- invalid target cleanup
- annexation cleanup
- subject and controller change
- multiple Event 61 projects under a project cap
- exact player tooltip and AI affordability

Do not create a second commitment system if the shared framework already owns the behavior.

## Gate 9: Staged idea lifecycle

Confirm the cleanest local precedent for:

- three timed stages
- repeat firing returning to stage one
- remaining duration cap
- save-safe scheduled transition
- conditional Readiness mitigation
- one visible idea family without stacking

## Gate 10: Evolution enable and active-transition hook

Confirm:

- shared Event 61 evolution activation variables
- enabled or disabled state
- how an evolution activation notifies an already active event owner
- how activation and later cycle application are guarded
- evolution history recorder contract

## Gate 11: Cluster execution

Confirm:

- current Cluster 4 registry source
- member order representation
- member skip logging
- one pacing event behavior
- member history and repeat-state preservation
- workbook and generated export linkage

## Gate 12: Event Logs

Confirm:

- history recorder input contract
- aggregate variable lifetime
- global actor representation
- evolution type, stage, tier, and actor contract
- Event Details metadata selectors
- member navigation for the Peace cluster

## Gate 13: Achievements

Confirm:

- single achievement registry and unique ID policy
- player-only tracking pattern
- persistent continuous timers
- tag continuity mapping
- war initiator and result proof
- state-ledger denominator updates
- debug and force-trigger disqualifier pattern
- icon consumer path

## Gate 14: Performance

Profile:

- one global firing with a late-game country count
- factory conversion across a major with many states
- Evolution I across a large stockpile
- Evolution II across a very large army
- 30-day pulses across every currently active affected country
- repeat-cycle mission merge

No permanent whole-world daily, weekly, or monthly iteration is permitted without a separately accepted performance plan.

## Gate 15: Probability tools

Run:

- `hoi4.probability_inspect`
- `hoi4.probability_eval`
- `hoi4.probability_sweep`
- `hoi4.probability_simulate` when interactions remain uncertain
- `hoi4.probability_compare` after weight changes

Use every named scenario in the AI probability research file.

## Gate result format

For every gate record:

| Field | Required content |
| --- | --- |
| Gate | number and name |
| Local sources | exact documentation and precedent paths |
| Tested source | exact Event 61 file and identifier |
| Method | parser, scripted test, probability tool, or live test |
| Result | pass, failed, blocked, or replaced |
| Evidence | path or output |
| Design deviation | exact change and reason |
| Follow-up | owner and acceptance step |
