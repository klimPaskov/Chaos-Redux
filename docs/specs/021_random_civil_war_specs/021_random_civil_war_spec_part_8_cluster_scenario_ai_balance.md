# Cluster, Scenario, AI, Balance, and Performance

## Wars cluster integration

Event 021 joins Cluster ID `1`, Wars.

Proposed membership:

- Event 004 Random War
- Event 007 Fury
- Event 021 Random Civil War

Event 021 member severity is `Medium`.

The current catalog export lists Event 004 and Event 007 only. Cluster membership and wording should be changed in the authoritative workbook after implementation wording is final. The CSV exports remain generated snapshots.

## Cluster identity

The Wars cluster represents different ways armed conflict can erupt during one wider shock.

- Event 004 creates external war.
- Event 007 creates expansionist Fury actors.
- Event 021 creates internal war.

The cluster must preserve those identities. It should not turn them into one generic war event.

## Cluster pacing

A cluster firing counts as one global pacing event.

Each member still:

- applies its own gameplay
- records its own history
- changes its own event state
- changes repeatable cap or weight where relevant
- records fired or skipped reason
- appears in Event Details
- respects event and evolution settings

The members do not each advance the timer or major-event gain separately.

## Cluster preparation order

All cluster members should reserve targets before any permanent change.

Recommended planning order:

1. prepare Random War actors and targets
2. prepare Fury actor and targets
3. prepare Event 021 target, regions, and actor package
4. detect collisions
5. reroll or skip invalid members
6. commit the full cluster transaction

The implementation may use another stable order if the reservation and rollback guarantees remain equivalent.

## Cluster collision rules

### Default separation

At Calm World and Gathering Storm, use different primary countries when enough candidates exist.

### Intentional overlap

At Rising Chaos or higher, Event 021 can fracture a country already entering an external cluster war when:

- Fracture Pressure is high
- the internal opening remains viable
- the overlap is visible in the event framing
- the country does not capitulate instantly
- AI can handle both conflicts
- all state and force plans were made before commitment

This overlap should be uncommon and should feel like war pressure causing domestic collapse.

### Fury overlap

A newly created Fury actor should not normally become the Event 021 target in the same cluster transaction.

A previously established human Fury actor can later suffer Event 021 only when:

- it is not actual nonhuman
- its package permits domestic politics
- its Fury progression remains valid
- a distinct actor exists
- the event does not erase Fury identity

### Event 006 collision

A cluster cannot create an Event 006 actor whose tag, territory, or anchor is already reserved by another cluster member or live country.

### Skip reasons

The cluster log should distinguish:

- event disabled
- evolution disabled
- no valid target
- target collision
- package incomplete
- tag collision
- actor capacity
- active-front cap
- protected country
- terminal conflict
- performance cap
- no viable territory
- incompatible bespoke crisis

## Cluster scaling

### Low cluster intensity

- usually one external war plus one internal crisis
- Fury can be skipped or use a distant actor
- no intentional overlap

### Medium cluster intensity

- all three members attempted
- minor countries preferred
- Event 021 uses baseline or early Evolution I strength

### High cluster intensity

- major countries possible
- intentional external and internal overlap possible
- stronger Fury and Event 021 openings
- cluster transaction must still preserve viability

The exact cluster tier system should follow the live cluster framework.

## Triggerable scenario

Working scenario name: `The Fracture Cascade`.

The scenario ID is not locked by this package. `SCN-014` is the next visible number after the supplied export, but implementation must verify the authoritative workbook and live registry before reserving it.

The scenario is separate from:

- `SCN-008 Every Banner Rises`, which releases Event 006 packages
- `SCN-013 The Unbidden Muster`, which creates immediate formation revolts from Event 019
- normal Event 021 timing
- Evolution III automatic review

## Scenario purpose

The scenario creates immediate civil-war plans across a chosen share of eligible normal human countries.

It can create:

- political uprisings
- rival legal governments
- command schisms
- Event 006 independence fronts
- regional secessions
- multi-way wars
- nested crises at higher intensity

The scenario does not set a terminal world state.

## Scenario types

### Political Fracture

Prioritizes:

- ideological uprisings
- rival legal governments
- coalition breakdown
- constitutional disputes
- same-tag takeovers for small countries

Independence packages remain uncommon.

### Independence Cascade

Prioritizes:

- complete Event 006 packages
- regional secession
- nested independence
- former-host wars
- recognition and separation

It does not mark Event 006 as fired.

### Command Collapse

Prioritizes:

- broad command schisms
- arsenal seizure
- military districts
- officer loyalty
- same-tag military takeover

It remains distinct from Event 019, Event 127, and Event 131.

### Universal Fragmentation

Uses the broadest valid mix:

- ideological claimants
- legal rivals
- command schisms
- Event 006 independence actors
- regional secession
- nested crises where safe

This is the default full challenge.

## Scenario intensity

### Low

- affects roughly 10 percent of eligible normal human countries
- prioritizes minors
- normally one opponent per country
- limited territory and force shares
- at most a small number of Event 006 actors
- no automatic nested crisis
- same-day setup

### Medium

- affects roughly 25 percent
- allows some majors
- medium and large countries can receive two opponents
- regular Event 006 package use
- stronger forces and foreign pressure
- same-day or tightly bounded setup

### High

- affects roughly 50 percent
- majors are common
- multi-way wars
- several Event 006 actors
- stronger foreign intervention
- some nested crises
- high tested front cap
- immediate commitment

### Maximum

- commits every eligible normal human country at confirmation
- uses the strongest sustainable multi-way opening
- attempts valid Event 006 packages in suitable hosts
- allows nested independence and successor pressure
- keeps actual nonhuman countries unaffected
- uses same-tag takeover for one-state countries
- bypasses normal evolution waits
- leaves the terminal world-end flag untouched

## Scenario setup and batching

The preferred launch is immediate.

If a measured one-frame setup causes a reproducible engine stall, the scenario may:

1. lock every selected target and actor plan at confirmation
2. show that the scenario has begun
3. commit deterministic batches
4. finish all planned launches within seven in-game days
5. keep the selected type, intensity, targets, actors, and maps unchanged
6. clear the scenario bypass when setup finishes

This is a performance contingency. It is not permission to reduce coverage, skip actors, or change the scenario after confirmation.

## Scenario launch flow

1. Open the scenario row.
2. Select type.
3. Select Low, Medium, High, or Maximum.
4. Press launch.
5. Show a confirmation summary with affected share, major eligibility, front intensity, independence emphasis, and performance load.
6. Confirm.
7. Set a tightly scoped launch flag.
8. build target and actor plans
9. reserve tags, territories, and front capacity
10. commit immediate or validated batches
11. clear the bypass
12. record scenario history
13. open the relevant player category and initial reports

The launch button and launch effect must use the same eligibility trigger.

## Scenario blockers

Valid blockers:

- active terminal state
- no normal human countries
- missing required registry
- no actor capacity
- unresolved tag collision
- invalid package initialization
- current scenario setup lock
- proven engine safety failure for the selected intensity

Invalid blockers:

- low chaos
- wrong date
- Event 021 never fired
- Event 006 never fired
- evolutions not reached
- Event 021 cooldown
- ordinary target weight
- earlier super-event history
- the selected player country being stable

## AI architecture

Event 021 needs role-specific AI.

### Consolidator government

Prefers:

- capital defense
- rail and depot security
- integration of loyal formations
- one decisive front
- limited concessions
- reconstruction

Avoids:

- fighting every front equally
- unlimited repression
- expensive foreign commitments
- concessions that dissolve the country

### Hardliner government

Prefers:

- loyalty reviews
- arsenal seizure
- repression
- emergency requisition
- military victory
- trials

Avoids:

- broad coalition
- recognition
- autonomy unless defeat is near

Risk:

- lower State Authority
- stronger recurrence
- additional fronts
- diplomatic isolation

### Negotiator government

Prefers:

- autonomy
- amnesty
- coalition
- ceasefire
- mediation
- disarmament

Avoids:

- unconditional surrender
- settlements that leave the capital exposed
- repeated concessions without enforcement

### Revolutionary claimant

Prefers:

- capital seizure
- mass recruitment
- ideological allies
- absorption of compatible fronts
- national succession

Avoids:

- permanent regional partition
- foreign domination
- autonomy that leaves the old government intact

### Constitutional claimant

Prefers:

- legal recognition
- coalition
- parliament or convention
- officer integration
- limited war aims

Avoids:

- destructive total war
- unsupported radical allies
- foreign terms that undermine legitimacy

### Independence actor

Prefers:

- regional capital
- recognition
- defensible border
- package-specific reinforcement
- autonomy as fallback
- Event 006 formables after survival

Avoids:

- national-capital offensive without a package reason
- annexing unrelated territory
- giving up its core identity for generic bonuses

### Command claimant

Prefers:

- arsenals
- rail hubs
- integration of regular units
- capital control
- emergency government

Avoids:

- militia spam
- foreign sponsor dependence
- long political negotiation when military victory is near

### Opportunistic sponsor

Prefers:

- one useful side
- equipment it can spare
- strategic access
- ideological fit
- a likely survivor

Avoids:

- several incompatible clients
- support during desperate own war
- actors that cannot reach administration or recognition

### Containment neighbor

Prefers:

- arms-route control
- civilian relief
- limited government aid
- border missions
- early mediation

Avoids:

- collective punishment
- expensive permanent mobilization
- arming rival sides

### Neutral mediator

Prefers:

- observer mission
- relief corridor
- prisoner exchange
- ceasefire
- settlement conference

Avoids:

- covert military aid
- recognition before basic administration
- unenforceable guarantees

### Survivalist successor

Prefers:

- resolve remaining fronts
- rebuild State Authority
- restore administration
- demobilize
- reduce sponsor debt
- delay expansion

Avoids:

- immediate aggressive war
- opening another internal rivalry
- free unit overexpansion

## AI decision inputs

AI should evaluate:

- current role
- State Authority
- front strength
- capital and supply
- equipment
- manpower
- fuel
- industry
- war state
- external enemy
- ideology
- public objective
- territorial viability
- sponsor relations
- foreign dependence
- settlement quality
- recurrence
- generation
- country size
- active-front cap
- current mission
- target validity

Invalid routes receive zero weight.

Complex weights, random lists, MTTH, and target selection require the specialized probability auditor before and after implementation.

## Probability design

Probability validation should cover:

- automatic target ordering
- stable versus unstable countries
- minor versus major targeting after Evolution I
- player versus AI targeting
- recent-target suppression
- regional variety
- archetype selection
- Event 006 package frequency
- severity bands
- number of fronts
- active-war evolution timing
- neighbor exposure
- sponsor choice
- strange-incident frequency
- settlement choice
- recurrence
- Critical queue order
- cluster overlap
- scenario target share
- scenario archetype mix

Exact event-selection probability cannot be claimed without the complete event pool and event-system state.

## Balance principles

### Limited war must remain limited

A stable small country should usually recover without losing half its land and army.

### Severe war must matter

A deeply unstable country should face a large territorial, military, administrative, and political crisis.

### More sides add negotiation difficulty

Multi-front wars should create distinct aims and harder settlement, not merely more divisions.

### Strong actions need aftermath

Emergency requisition, mass mobilization, foreign aid, repression, and strange practices create later costs.

### Independence actors preserve identity

Event 006 actors use their own strengths, weaknesses, and ambitions.

### Prevention reshapes risk

Preventive play can delay, shrink, redirect, or settle a front. It should not guarantee total immunity.

### Victory does not erase obligations

Postwar administration, disarmament, sponsor debt, and political settlement remain important.

### Recurrence is conditional

Unresolved conditions can return. Successful reconstruction and agreement can end the cycle.

## Exploit review

Check for:

- free unit loops
- repeated equipment capture
- depot farming
- recurrence farming
- sponsor aid loops
- recognition farming
- repeated autonomy grants
- instant annexation of unrelated sides
- duplicated focus rewards
- duplicate Event 006 initialization
- decision clicks after target death
- stale selected fronts
- repeated scenario launch
- package tag reuse
- country generation bypass
- cleanup that refunds and retains the same resources
- free State Authority gain
- repeated strange buff
- coalition settlement that keeps every reward

## Performance review

Required test worlds:

- baseline minor
- severe medium country
- Evolution I major with three fronts
- Evolution II region with five exposed neighbors
- Evolution III normal world
- world with many Event 006 countries
- late game with many dynamic tags
- Maximum scenario
- multiplayer with several human countries
- several specialized civil-war events active

Measure:

- review-pulse time
- active theater count
- active front count
- country registry size
- Critical queue size
- decision count
- mission count
- event count
- tag capacity
- save size
- cleanup
- orphan targets
- UI responsiveness
- game-speed impact

## Acceptance

Part 8 is accepted only when:

- Wars cluster membership and collision behavior are implemented
- skip reasons are visible
- scenario ID is verified
- scenario bypass clears
- all four types and intensities work
- Maximum remains a challenge scenario within tested limits and does not become an unbounded crash route
- AI profiles create distinct behavior
- probability ordering matches the named scenarios
- the scheduler stays within tested performance
- balance and exploit checks are documented
