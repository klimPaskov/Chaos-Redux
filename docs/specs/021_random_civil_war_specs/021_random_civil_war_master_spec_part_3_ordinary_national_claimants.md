# Ordinary national claimants (part 3)

Verbatim part of [021_random_civil_war_master_spec.md](021_random_civil_war_master_spec.md), which indexes this specification.

## Ordinary national claimants

An ordinary ideological, legal, constitutional, or command claimant represents another government for the same country.

### Identity

The side should use:

- the existing national identity
- an existing verified civil-war tag or engine route
- a route-appropriate cosmetic identity only when a safe precedent exists
- the existing adjective
- a compatible ruling party
- a valid leader or governing institution
- existing or approved flag handling
- Event 021 crisis decisions
- Event 021 crisis ideas
- route-specific AI

Public actor names should be country or government identities. Avoid names built around internal implementation bodies such as office, bureau, mission, or project unless that body is truly the state.

### Politics

Starting politics should derive from:

- selected archetype
- prewar ideology support
- legal claim
- leadership
- local support
- State Authority
- foreign sponsorship
- current government type

A claimant can begin with provisional status until it proves administration.

### Military

Starting forces should derive from:

- units in controlled territory
- command loyalty
- local depots
- severity
- current host army
- population
- terrain
- ports and airfields
- local militia and officer capacity

The side needs a reinforcement path through Event 021 decisions. It must not begin as an empty tag.

### Permanent disposition

If the claimant wins the national war, it becomes the successor government.

If it loses, it is annexed, disarmed, exiled, integrated, or removed through cleanup.

If it survives inside a settlement, it needs a defined coalition, autonomy, legal-party, subject, or partition role.

## Focus-tree handling for ordinary claimants

Ordinary claimants do not receive a generic Event 021 focus tree.

The implementation should preserve the country's meaningful existing tree where engine behavior permits.

It must prevent:

- both sides collecting the same one-time reward
- a claimant completing focuses that require dead leaders
- a side using states it does not own
- mutually incompatible ideology routes remaining active
- a temporary actor receiving another country's tree
- duplicate advisor, character, factory, technology, or war-goal rewards
- a successor losing its valid national content after victory

Possible safe approaches include:

- shared tree with completed-focus and route safeguards
- inherited tree with unavailable incompatible branches
- temporary crisis decisions carrying the war gameplay
- a small approved overlay only when the existing tree cannot represent the successor and only after a separate focus-tree design pass

A blind full tree replacement is outside the Event 021 baseline.

If focus source changes are required, the implementation must use the focus skill, HOI4 focus inspection and rendering, route filters, navigation, and a focus audit. The planning package does not authorize a generic tree rewrite.

## Temporary regional actors

A regional secession route sits between an ordinary national claimant and a complete Event 006 country.

Use it only when:

- the region is coherent
- the movement has a defensible political identity
- the territory is valid
- leadership can be resolved
- a complete Event 006 package is not the correct route
- the actor has a defined settlement and postwar disposition

Possible goals:

- autonomy
- federation
- temporary regional government
- recognized regional republic
- merger into a complete related country
- negotiated return

A temporary regional actor cannot remain indefinitely with no leader, flag, national content, or diplomatic purpose.

### Promotion

A surviving regional actor can become permanent only through:

- promotion into a complete Event 006 package
- merger into another country
- recognized autonomous subject
- an accepted future package addendum with full identity, leader, flags, forces, focus or decisions, AI, assets, and documentation

If none applies, the war must settle through reintegration, autonomy inside the host, or defeat.

## Event 006 independence-package contract

Event 021 may initialize a complete human Event 006 package even when Independence Wave has never fired.

The call must:

- select a valid registered package
- set an Event 021 release origin
- use Event 021 territory and war context
- use the Event 006 tag
- use Event 006 leadership
- use Event 006 flags and cosmetic identities
- use Event 006 politics and parties
- use Event 006 focus tree
- use Event 006 starting ideas
- use Event 006 force profiles
- use Event 006 reinforcement decisions
- use Event 006 formation and formable decisions
- use Event 006 recognition, league, and diplomacy rules
- use Event 006 AI
- use Event 006 assets
- register the country as an Event 021 front
- create or preserve the former-host war
- remain idempotent

The call must not:

- mark Event 006 as fired
- change Event 006 repeatable weight
- change Event 006 cap
- increase Event 006 fire count
- advance Event 006 evolution history
- create an Independence Wave history row
- automatically enroll the country in an Event 006 congress or league
- duplicate a living tag
- use an incomplete package
- create an actual nonhuman package
- silently replace a missing leader, flag, tree, or asset
- ignore Event 006 collision rules
- take the host's protected remnant
- grant normal peaceful-release resources when the civil-war profile should apply

## Origin record

The country package needs a stable origin value or flag.

Possible package origins across Chaos Redux include:

- normal Event 006 release
- Event 021 civil-war independence
- Event 005 Soviet collapse
- triggerable scenario
- focus or formation decision
- another accepted event

The Event 021 origin can change:

- former-host war
- opening force share
- emergency front decisions
- recognition
- inherited settlement claims
- starting State Authority
- first reinforcement cooldown
- generation memory
- reconstruction burden

It should not fork the whole Event 006 package when ordinary content can remain shared.

## Idempotence

Running the Event 006 initializer or Event 021 adapter more than once must not create:

- duplicate leaders
- duplicate flags
- duplicate focus assignment
- duplicate ideas
- duplicate units
- duplicate technology
- duplicate decisions
- duplicate formation discovery
- duplicate recognition
- duplicate league membership
- duplicate event-history state
- duplicate front registration

Package initialization may record separate completed subsurfaces so a failed partial transaction can resume safely.

## Package eligibility by stage

### Baseline

The package pool should favor:

- common complete Event 006 packages
- vanilla identities already supported by Event 006
- compact regional actors
- packages whose anchor and capital fit a limited opening

An Event 006 actor remains less common than an ordinary ideological or legal claimant before Evolution I.

### Evolution I

The package pool expands to:

- broad complete Event 006 registry
- larger actors
- militarily prepared actors
- more than one independence side in a large country
- packages with distinct regional claims
- packages with prevention decisions

### Evolution II

The package pool can include:

- unusual grounded packages
- related regional movements
- actors with stronger foreign recognition routes
- packages linked to sponsor and cross-border networks
- old national projects already accepted by Event 006

### Evolution III

The package pool can include any complete human Event 006 package with a valid map.

It can also support:

- nested independence
- high-chaos Event 006 branches
- early formable discovery where Event 006 allows it
- successor-state independence
- strong foreign patron pressure

It still cannot use actual nonhuman packages.

## Shared Event 006 systems

Event 021 should reuse:

- package registry
- candidate validation
- tag mapping
- country carrier collections
- anchor-state mapping
- protected host remnant logic
- collision resolution
- country initialization
- focus assignment
- leader and party setup
- flag and cosmetic handling
- starting force profiles
- reinforcement decisions
- formation and formable decisions
- recognition
- league and congress access
- AI
- documentation crosswalk
- asset manifests

When a reusable helper does not exist, `chaosx_scripted_system_architect` should create a shared helper. Event 021 should not copy the Event 006 package initializer into its own files.

## Tag audit

Before any new tag or carrier is assigned, implementation must audit:

- vanilla tags
- Chaos Redux tags
- Event 006 registry
- Soviet collapse carriers
- dynamic country collections
- cosmetic tags
- scenario reservations
- Workshop references
- other local mods
- living countries in the current save context

A national identity already present in vanilla should reuse the vanilla identity and preserve meaningful vanilla content.

A tag collision blocks the candidate until it is remapped. It does not justify a random substitute.

## Leadership and portrait rules

### Grounded independence actor

Use:

- attributed real leader
- existing vanilla or Chaos Redux character
- authentic governing institution
- full portrait ownership check
- source-based portrait workflow when a new portrait is required

Do not:

- generate an invented leader for a real polity
- clone a character already held by a live country
- assign mismatched gender or name metadata
- create a generic officer face
- use a portrait merely because it resembles the region

### Ordinary claimant

Prefer existing characters.

An engine generic route is acceptable only when local precedent proves that it does not create a new custom grounded identity or portrait obligation.

If leadership cannot be resolved safely, the dispatcher should select another actor or target.

## Force integration

### Event 006 actor

Uses package-specific:

- militia
- border guards
- regular defectors
- mountain formations
- cavalry
- railway guards
- port guards
- foreign volunteers
- specialist units
- package reinforcement

Event 021 supplies:

- severity
- territory
- captured depot context
- host relationship
- active front
- initial objectives
- State Authority
- sponsor state
- settlement context

### Ordinary claimant

Uses parent-compatible formations and Event 021 reinforcement.

Reinforcement requires:

- manpower
- equipment
- training time
- local support
- state control
- rail or depot access
- active force cap
- cooldown

### Temporary regional actor

Uses:

- local militia
- defecting garrisons
- regional guards
- parent-compatible equipment
- no invented exotic unit
- a promotion or settlement route

## Technology handling

Event 021 should not grant a standard package of technologies to every actor.

An Event 006 actor uses Event 006 technology rules.

An ordinary claimant preserves compatible parent technology through the safe civil-war precedent.

A temporary actor receives only what its accepted package or engine route supports.

Any technology or doctrine graph changes require a separate graph plan and MCP inspection. This event does not authorize a new technology tree.

## Focus access after victory

### Ordinary claimant victory

The successor should retain or recover a valid national tree.

Implementation must resolve:

- completed focuses
- route locks
- impossible old-government branches
- leader-dependent content
- one-time rewards
- focus AI
- national identity
- focus navigation
- hidden branches

### Event 006 victory or survival

The country continues with its Event 006 tree.

It keeps:

- package formables
- formation decisions
- reinforcement
- diplomacy
- recognition
- country-specific AI
- package identity

Event 021 origin should add only civil-war aftermath and former-host context.

### Regional settlement

A temporary actor that remains autonomous needs enough decision content to remain playable. It should not be left with a blank tree and no objectives.

## Interactions with related events

### Event 005 Soviet Union Collapse

Event 005 owns Soviet collapse waves and coalition logic.

Event 021 can:

- target a human post-collapse republic after grace
- use a valid Event 006 package inside a former Soviet state
- create an ideological or command crisis in a surviving Soviet state
- preserve origin memory

Event 021 must not:

- advance Event 005 waves
- release every Soviet republic
- consume Event 005 state
- autojoin Event 005 coalitions

### Event 006 Independence Wave

Event 021 reuses complete packages and records a separate origin.

The country remains eligible for Event 006 systems based on identity.

Its creation does not count as an Event 006 firing.

### Event 019 Soldiers from Nowhere

Event 019 can affect command loyalty or contribute compatible formations when active.

Event 021 must not:

- create Event 019 formations on its own
- advance Event 019 generation or evolution
- use nonhuman Event 019 countries as targets
- inherit Event 019 scenario identity

Ordinary human formations can defect through normal force allocation when compatible.

### Event 095 Occupation Revolt

Event 095 owns exile and occupation uprisings.

When a country exists mainly through occupied territory and an exile revolt is the correct premise, Event 095 receives priority.

Event 021 owns domestic fracture inside the current political actor's home system.

### Event 117 Five-Way Civil War

Event 117 owns a bespoke five-camp crisis.

It may later reuse Event 021 region, force, or front helpers. Event 021 must not copy its specific prevention and camp design.

### Event 127 Warlords

Event 127 owns named warlords and their political system.

Event 021's command schism is institutional and broad.

### Event 131 Widespread Mutiny

Event 131 owns a mass mutiny caused by low war support.

Event 021 can read a documented mutiny history or command condition. It must not replace the mutiny event.

### Event 134 Duchies

Event 134 keeps its own historical or political premise. Event 021 can only use a duchy package if Event 006 or another accepted country package owns it.

### Event 142 Partisans

Event 142 owns partisan divisions tied to ideological support.

Event 021 can respond to a surviving organized partisan movement only through an explicit contract.

### Event 144 Freedom or Death

Event 144 owns simultaneous global subject independence and the National Liberation Front.

Event 021 can create one subject's domestic crisis. It must not launch the global subject wave or automatically join the faction.

## Factions and subjects

A civil war needs explicit handling for:

- original faction membership
- rebel faction eligibility
- subject status
- overlord intervention
- guarantees
- military access
- volunteers
- attachés
- lend-lease
- succession after victory

Default direction:

- an ordinary claimant does not automatically inherit full faction membership
- an independence actor starts outside a faction unless its package says otherwise
- a successor rejoins or inherits through a validated path
- one live faction is not duplicated
- a subject civil war does not automatically make every overlord and every rebel side fight
- an overlord can support, mediate, recognize, tighten control, or allow separation

## Country-package acceptance

Country integration is accepted only when:

- ordinary claimants preserve national identity safely
- Event 006 actors use complete packages
- Event 006 event state is untouched
- every actor has territory, capital, leadership, politics, forces, AI, decisions, and cleanup
- no duplicate tag or character exists
- grounded actors use defensible leaders
- temporary actors have a permanent disposition
- postwar winners remain playable
- nested crises work for human independence countries
- actual nonhuman countries remain excluded
- focus behavior does not duplicate one-time rewards or expose invalid routes


---

<!-- Source: 021_random_civil_war_spec_part_8_cluster_scenario_ai_balance.md -->


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

**Parent resolution — 2026-09-25:** `SCN-018` is the assigned ID for The Fracture Cascade. The user's implementation prompt requires a verified free ID without prescribing its number. The authoritative workbook's `Scenarios` sheet contains exactly one `SCN-018` row for The Fracture Cascade and no duplicate scenario IDs. This resolves the earlier `SCN-014` candidate; the scenario remains `Needs Testing`, not finally accepted.

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


---

<!-- Source: 021_random_civil_war_spec_part_9_presentation_assets_achievements.md -->


# Presentation, Assets, and Achievements

## Presentation purpose

Event 021 should look and sound like a political and military rupture inside a specific country.

The visual and text focus should be:

- divided formations
- seized arsenals
- rail junctions under competing control
- regional assemblies
- improvised governments
- damaged administration
- interrupted civilian transport
- local mobilization
- rival public symbols
- uncertain officer loyalty
- foreign aid routes
- negotiations under military pressure

The presentation should not default to a world map, a staff table, a sealed report, a border-arrow diagram, or a generic explosion.

## Player-facing writing direction

Final localisation belongs to implementation.

The spec defines viewpoint, information, tone, and dynamic content. It does not provide pasteable lines.

### Opening event

Viewpoint:

- affected country
- government, soldiers, local officials, civilians, regional leaders, or opposition organizers

Visible information:

- location of the first rupture
- public claimant identity
- command or political institution involved
- immediate capital, depot, rail, or regional danger
- first government posture

Uncertain information:

- full size of the movement
- which units will defect
- whether another front exists
- foreign sponsorship
- whether strange practices are material, psychological, or supernatural

Tone:

- serious
- concrete
- country-specific
- restrained in a limited crisis
- fearful and disordered in a severe crisis
- dry official irony only when it does not trivialize death

Avoid:

- generic global statements
- map-change narration
- official denial contrast
- fake mystery built from paperwork
- repeated short dramatic fragments
- calling the event a warning
- explaining hidden mechanics

### Government options

Important option families should express a posture.

Possible tones:

- firm command
- constitutional response
- cautious containment
- regional negotiation
- frightened improvisation
- authoritarian certainty
- bitter official understatement

The option should communicate the chosen public response and visible consequence.

### Opposition opening

The opposition text should establish:

- public claim
- local base
- leadership or institution
- immediate objective
- relationship to the parent
- stance toward other fronts
- uncertainty over recognition and support

An Event 006 actor should use its own country tone.

### Multi-front event

The new side must have a distinct goal.

Dynamic details can include:

- region
- ideology
- leader or governing institution
- capital
- claimed settlement
- rival front
- sponsor
- depot or rail objective

The event should not read like another identical rebel spawn.

### Neighbor event

Show:

- border community
- arms route
- returning cadres
- displaced civilians and administrative burden
- disrupted trade
- political organization
- local militia concern
- foreign sponsor
- government policy

Do not treat displaced civilians as a collective security threat.

### Strange incident

Show:

- unusual discipline
- repeated symbol
- night ceremony
- impossible endurance rumor
- frightened soldiers
- unexplained coordination
- material consequence

Do not confirm an occult explanation.

### Evolution III activation

Show several countries facing different pressures.

Possible details:

- capital guards
- provincial halls
- rail yards
- ports
- barracks
- political congresses
- army districts
- regional movements
- foreign missions

Avoid one generic global sentence or literal world-map art.

## Event Details direction

Event Details should explain that:

- a country can fracture according to politics, command, territory, administration, war, and prior settlement
- later evolution can create several sides
- complete Event 006 actors can fight for independence
- neighboring countries can face exposure and choices
- high evolution makes domestic fracture a global risk
- winners can face successor problems

It should not list:

- raw score components
- exact weights
- candidate-package pools
- strange-incident chance
- achievement routes
- implementation status
- performance caps
- actor slots

## Evolution detail direction

### Evolution I

Describe several armed projects forming inside one country, including major-country vulnerability and independence fronts.

### Evolution II

Describe cross-border armed networks, sponsors, political emulation, stronger fronts, mediation, and unexplained battlefield practices.

### Evolution III

Describe a global climate in which every normal human country must manage its own domestic risk and newly independent states can also divide.

## Event-log actor

The Event 021 history row uses the original affected country as actor.

An evolution row can use a specific front only when the evolution belongs clearly to that front and the shared logger supports the actor safely.

The front registry should preserve parent, claimant, Event 006 package, successor, and generation.

## Static visual asset inventory

Event 021 uses a compact static package.

### Baseline report image

Working asset ID:

`report_event_021_random_civil_war_opening`

Target:

- `210x176`
- report-event card treatment
- generated period-documentary source
- black and white or sepia through normal processing

Scene direction:

- rail yard, barracks gate, regional government square, or city street
- divided armed formations and civilians
- 1936 to 1945 photographic technology
- period uniforms, vehicles, buildings, and equipment
- no readable generated text
- no modern props
- no map table
- no explosion-only composition

### Multi-front news image

Working asset ID:

`news_event_021_multi_front_war`

Target:

- `397x153`
- black and white
- strong period press composition

Scene direction:

- several armed groups controlling different parts of one public square, junction, or transport hub
- distinct formations and banners without fake text
- visible depth
- no modern staging

### Global fracture news image

Working asset ID:

`news_event_021_global_fracture`

Target:

- `397x153`
- black and white
- one coherent period scene

Scene direction:

- crowded international rail station, border crossing, military columns, delegations, or several movements in one setting
- communicates broad political fracture without a literal world map
- no montage labels
- no modern imagery

### Optional independence-front report image

Use only when the chosen Event 006 package has no suitable shared report asset.

Direction:

- regional assembly
- militia formation
- public declaration
- border post
- package-specific grounded identity

Event 006 asset ownership remains primary.

### Optional strange-incident report image

Create only when implementation uses enough strange-incident events to justify a distinct image.

Direction:

- soldiers at night around a ruined shrine, trench, banner, or field position
- ambiguous atmosphere
- no monster
- no gore
- no direct supernatural confirmation

## Decision-category picture

Working asset ID:

`decision_category_picture_021_civil_war`

Reference family:

`assets/gfx_references/icons/decision_categories/pictures`

Target direction:

- use the verified current category-picture canvas, with `114x101` as the current reference-family size
- static
- no fake buttons
- no meter
- no painted text
- no fake map controls

Scene direction:

- divided national standard above an improvised barricade
- broken field telephone and rail signal
- armed guards facing different directions at a junction
- one coherent political and military rupture

The picture supports atmosphere. State Authority remains real text and tooltip, not painted into the image.

## Category icon

Working asset ID:

`decision_category_021_civil_war_crisis`

Direction:

- fractured seal
- split command baton
- divided standard
- strong silhouette
- readable at the verified category size
- transparent when the local precedent requires it

## Decision icons

The final count should match implemented decisions.

Planned icon directions:

- secure arsenals
- capital defense
- restore rail route
- loyalty review
- regional charter
- emergency coalition
- local mobilization
- foreign liaison
- recognition
- ceasefire
- aid corridor
- reconstruction
- strange-incident countermeasure

Each decision icon must be designed for the decision surface. It cannot be a resized focus or idea icon.

## Mission icons

Planned directions:

- hold capital
- secure rail hubs
- protect depots
- keep corridor open
- complete local mobilization
- deny recognition

Final mission icons should match implemented mission families.

## Idea icons

### Fractured Command

Working ID:

`idea_021_fractured_command`

Direction:

- broken command baton
- divided officer insignia
- split field-telephone network
- `64x64`
- transparent spirit-style art

### War-Torn Administration

Working ID:

`idea_021_war_torn_administration`

Direction:

- damaged rail schedule
- broken civic seal
- interrupted communications
- abandoned administrative files with transport damage
- `64x64`

### Unsettled Settlement

Working ID:

`idea_021_unsettled_settlement`

Direction:

- agreement with visible fracture
- surrendered weapons beside unresolved banners
- divided assembly chamber
- `64x64`

Staged idea variants can use separate art only when the stage is visually distinct enough to justify it. Do not create many near-identical icons.

## Asset exclusions

Event 021 does not require:

- a generic rebel flag family
- new portraits for every random claimant
- advisor portraits
- a custom faction emblem
- animated category art
- animated portrait overlays
- a scripted GUI panel
- a 3D unit
- a 3D building
- custom skeletal animation
- a super-event image
- super-event audio

Event 006 flags and portraits remain Event 006 assets.
