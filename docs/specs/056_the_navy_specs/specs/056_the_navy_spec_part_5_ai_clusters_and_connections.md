# Event 056: AI, Clusters, and Connections

## AI design principle

AI countries receive the same random package identities as human countries. The event must not quietly give the AI a fleet chosen for its doctrine or war plan.

AI intelligence applies after the package is rolled. It determines how the country commissions the force, organizes it, supports it, and adjusts its future naval behavior.

This preserves the event's central unfairness while preventing obviously unusable AI outcomes.

## AI commissioning choices

### Full Commissioning preference

The AI should prefer immediate full commissioning when several of these conditions are true:

- the country is at war
- it has a meaningful active naval theater
- fuel reserves and income can support the package for an initial operating period
- commissioning ports have adequate repair capacity
- enemy naval or invasion pressure is immediate
- the package fills an urgent role, such as escorts under submarine attack
- the country has aircraft support for a carrier package
- the defining ships can join an existing operational force safely

Full commissioning should dominate for an island state under invasion pressure that receives escorts or a balanced fleet.

### Phased Commissioning preference

The AI should prefer phased commissioning when several of these conditions are true:

- the country is at peace
- fuel is scarce
- naval bases are small or heavily damaged
- the package contains several heavy ships or carriers
- carrier aircraft are incomplete
- commissioning ports face enemy air attack
- the country's repair queue is already overloaded
- the package is large relative to the existing navy
- the country needs time to reorganize task forces

Phased commissioning should be the normal cautious response for a small peacetime country that receives a capital or carrier package.

### Break Up preference

The AI should consider partial breakup when several of these conditions are true:

- the country is committed to a severe land war and cannot support a major naval diversion
- usable fuel is critically low
- there is no plausible operational sea route or nearby naval objective
- the package duplicates an already overwhelming concentration
- the country lacks a safe base for the defining heavy component
- a carrier package has no credible aircraft route and cannot be delayed safely
- the country needs convoys and repair capacity more than the surplus heavy hulls

Breakup must remain a bounded fallback. AI countries should not dismantle most gifted fleets simply because they are non-naval minors.

## AI decision hierarchy

The AI should evaluate commissioning in this order:

1. Confirm the package can be delivered legally.
2. Identify immediate survival needs, especially convoy defense and invasion pressure.
3. Measure fuel, port, repair, and aircraft constraints.
4. Compare the package with the existing fleet and current naval theater.
5. Choose full, phased, or breakup handling.
6. Create usable task forces around the package identity.
7. Adjust future production and mission priorities for a bounded period.

The identity roll is already complete before this process begins.

## AI task-force organization

The delivered package should begin in a limited set of coherent task forces so the AI is not required to repair a completely random organization.

### Balanced Surface Fleet

- one main surface group with full screening
- one patrol or escort group when enough light ships exist
- submarines remain separate

### Submarine Raiding Fleet

- several bounded submarine groups
- surface support remains separate
- no submarine group is attached to a slow capital force

### Destroyer Swarm

- several escort and patrol groups
- a light cruiser leader can accompany larger groups
- avoid one huge task force containing every destroyer

### Convoy-Heavy Escort Fleet

- escort groups sized for convoy protection
- reserve escorts can remain near the main port
- no attempt to use convoys as combat units

### Cruiser-Focused Fleet

- cruiser action group with screens
- optional patrol group
- heavy and light cruiser roles remain coherent

### Capital-Ship Fleet

- one battle group with sufficient screens
- surplus escorts can form a separate patrol or convoy group
- capital ships should not deploy without safe screening

### Carrier-Focused Fleet

- one or more carrier groups with complete screens
- carrier aircraft assigned before high-risk deployment where possible
- carriers should avoid surface missions that ignore their aviation role

### Coastal Defense Fleet

- small patrol and interception groups near home waters
- submarines remain separate
- avoid long-range missions the designs cannot support

### Invasion-Support Fleet

- transport escort group
- bombardment or cover group
- carrier or air support attached only where functional

### Sea-Denial Fleet

- minelaying groups where available
- patrol and cover groups
- avoid mine missions in irrelevant or inaccessible regions

## AI naval strategy after delivery

The event can influence AI behavior for a bounded period so the new fleet is used rather than ignored.

The response should change priorities, not force suicidal orders.

### Production reaction

- reduce construction of a ship class when the package already creates a large short-term surplus
- continue production where replacement, screening, or aircraft support remains necessary
- increase carrier-air production after receiving carriers if compatible technology and industry exist
- increase convoy or escort support when the package creates new overseas capacity
- avoid cancelling nearly completed valuable ships merely because a package arrived

### Mission reaction

- escort packages raise convoy-protection priority where routes exist
- submarine packages raise raiding priority against valid wartime targets
- coastal packages raise home-water patrol and interception priority
- invasion packages raise interest in legal amphibious operations only when land forces, targets, and supply support exist
- carrier and capital packages raise fleet-in-being or strike activity only when fuel and air conditions permit

### Repair reaction

- protect heavily damaged gifted ships from immediate redeployment
- use phased commissioning when repair capacity cannot support the whole force
- avoid cycling damaged heavy ships through exposed ports

### Fuel reaction

- conserve fuel when the new fleet exceeds sustainable use
- keep part of the force in reserve rather than running every task force continuously
- do not consume the entire support grant through meaningless peacetime patrols

## AI invalidity rules

AI handling must refuse actions that rely on:

- a lost or enemy-controlled port
- missing carrier aircraft with no legal support route
- an inaccessible sea region
- a dead or annexed recipient
- a package already delivered or converted
- disabled evolution content
- unregistered experimental assets
- a special country that cannot use ordinary fleets

An invalid choice should not remain available with low weight. It should be removed from the AI's legal set.

## AI probability acceptance scenarios

The detailed probability matrix lives in `quality/ai_probability_scenario_matrix.md`. The required ordering is summarized here.

| Scenario | Expected ordering |
| --- | --- |
| Wartime major with fuel, ports, and an active naval front | Full above Phased, Phased above Break Up |
| Peacetime minor with weak ports and a capital-heavy package | Phased above Break Up, Break Up above Full |
| Land-war minor with almost no fuel and a submarine package | Phased or Break Up above Full |
| Island country under blockade pressure with an escort package | Full strongly dominant |
| Carrier package with no legal air group | Phased above Break Up, Full remains rare or invalid |
| Existing top-tier navy receiving a duplicate destroyer swarm | Phased or Break Up above Full |
| Permitted special Chaos country | Owner strategy decides among legal options |

These are ordering requirements rather than invented exact percentages. Exact results require inspection of the complete candidate pool and external AI factors.

## Primary cluster: Sudden Abundance

### Cluster promise

Sudden Abundance groups events in which countries receive a major quantity of people, equipment, wealth, military capacity, or fortification without ordinary preparation.

The cluster should feel generous and destabilizing. Its members give the world resources or power that can be useful immediately but create uneven strategic results.

### Proposed membership

| Event | Name | Role in Sudden Abundance | Member severity |
| ---: | --- | --- | --- |
| 19 | Soldiers from Nowhere | Sudden manpower and formations | Medium |
| 29 | Riches Found | Sudden wealth and productive power | Medium |
| 32 | Missiles | Sudden strategic weapons and delivery capacity | Medium |
| 37 | Mysterious People | Sudden civilian population | Medium |
| 42 | Equipment from Heavens | Sudden general equipment | Low |
| 56 | The Navy | Sudden naval forces | Medium |
| 64 | Border Fortifications | Sudden defensive construction | Medium |

The severity belongs to this cluster membership. Another cluster can use a different role only if the catalog and runtime support per-membership severity cleanly.

### Cluster behavior proposal

- type: Minor Repeatable
- cluster Chaos level: 1
- working cooldown target: 540 days
- working selected-member cluster-entry target: about 15 percent before probability audit
- the originally selected event always remains the required member
- other members are optional and use bounded participation rolls
- one cluster firing counts as one pacing event
- each participating member still applies its own history, repeatable cap, effects, and eligibility

### Optional member participation targets

These are relative design weights for later probability inspection:

| Event | Relative participation weight |
| ---: | ---: |
| 19 | 70 |
| 29 | 65 |
| 32 | 55 |
| 37 | 65 |
| 42 | 45 |
| 56 | 60 |
| 64 | 55 |

The weights should create varied abundance waves. They must not cause every cluster firing to deliver all seven members.

### Event 56 inside the cluster

When Event 56 participates, it performs one ordinary global firing under its current repeat and evolution rules. It does not increase package size merely because the cluster fired.

If another cluster member grants equipment, population, missiles, money, or forts, those effects stay separate. Cross-event support can occur only through defined adapters.

## Additional cluster: Military Preparation

### Cluster promise

Military Preparation groups incidents that suddenly improve the world's ability to fight before governments have chosen a coherent strategy. The cluster can fill arsenals, add missiles, create fleets, and harden borders at the same time.

Its result should raise military capability without directly starting wars.

### Proposed membership

| Event | Name | Role in Military Preparation | Member severity |
| ---: | --- | --- | --- |
| 32 | Missiles | Strategic strike capacity | Medium |
| 42 | Equipment from Heavens | General military stockpiles | Low |
| 56 | The Navy | Naval force projection | Medium |
| 64 | Border Fortifications | Defensive readiness | Medium |

### Cluster behavior proposal

- type: Minor Repeatable
- cluster Chaos level: 2
- working cooldown target: 720 days
- working selected-member cluster-entry target: about 10 percent before probability audit
- the selected event remains required
- other members are optional
- the cluster raises capability and readiness, but does not issue war declarations

The Chaos level 2 proposal lets Event 56 fire normally during Calm World while reserving the broader military buildup wave for Gathering Storm and later.

### Optional member participation targets

| Event | Relative participation weight |
| ---: | ---: |
| 32 | 65 |
| 42 | 55 |
| 56 | 60 |
| 64 | 65 |

## Dual-cluster membership

Event 56 belongs to two clusters. One selection of Event 56 can trigger at most one cluster transaction.

When only Sudden Abundance is available, Event 56 can roll only that cluster.

When both clusters are available, the event should resolve one exclusive cluster-entry result from the valid candidate set. It must not fire Sudden Abundance and Military Preparation together from one selected event.

A suitable working distribution at 200 or higher is:

- no cluster outcome remains dominant
- Sudden Abundance has the higher entry share
- Military Preparation has the lower entry share

The exact combined method and weights require probability inspection against the cluster system's actual selection contract.

Manual cluster firing remains separate. A manual Sudden Abundance launch can include Event 56 once. A manual Military Preparation launch can include Event 56 once.

## Cluster history and detail

A cluster history row should identify:

- cluster name
- date
- selected event
- current Chaos tier
- participating members
- skipped members and reasons
- total member count
- actor only where the cluster framework has a meaningful actor

Event 56 contributes one member result showing recipient count and package-delivery status. It must not create a second pacing row for every recipient.

## Event connection: Gift from Scientists

Event 54 can change which naval technologies a country possesses before a later Event 56 firing.

The connection works through legal package content:

- an advanced researched hull can widen the country's legal design pool
- compatible aircraft technology can improve carrier support
- unusual technology explicitly marked safe by its owner can enter an evolved package

Event 56 does not call Event 54, count Event 54 as fired, or grant the research itself.

## Event connection: The Great Infrastructure Project

Event 55 can improve ports, railways, infrastructure, and logistics before Event 56 fires.

This affects:

- preferred commissioning ports
- how many ports a large package needs
- whether heavy ships can enter service immediately
- repair and supply pressure
- the need for an emergency commissioning facility

Event 55 does not influence package identity. A country with excellent ports can still receive a convoy package or a coastal fleet.

## Event connection: Riches Found

Event 29 can make it easier for a country to absorb the new fleet through stronger construction and economic capacity.

The connection should appear through ordinary resources and existing event effects. Riches Found does not increase Event 56 package size and does not alter the identity roll.

## Event connection: Equipment from Heavens

Event 42 can supply equipment related to naval operations only through a defined compatibility adapter.

Possible compatible support includes:

- carrier or naval aircraft
- repair-related stockpiles
- support equipment used by an existing naval system

The adapter cannot duplicate the same support already granted by Event 56 during one cluster transaction.

## Event connection: Missiles

Event 32 can widen the evolved naval pool when its owning system explicitly registers compatible guided-weapon ships, submarines, or naval equipment.

The permission belongs to Event 32 or the relevant special-project owner. Event 56 cannot infer that every missile technology is safe for ship delivery.

## Famine connection

New fleets can create real blockades through ordinary war and naval control. Those blockades can contribute to famine only when the Famine system's full live requirements are satisfied.

Event 56 never applies famine pressure merely because submarines or capital ships appeared. Island status, package size, or a theoretical capacity to blockade is insufficient.

This prevents a double event effect and preserves Famine ownership.

## Natural disaster and damage connections

New ports and ships remain vulnerable to ordinary damage, combat, air attack, and disaster systems.

Event 56 does not protect its fleets from later events. It also does not duplicate a disaster effect by damaging them directly after delivery.

## Event history connection

Later Event 56 reports can refer to prior manifestations at a high level. The writing direction may acknowledge that governments recognize the pattern or have prepared contingency plans.

The event still does not explain the source. Repetition should deepen public familiarity with the phenomenon without resolving it.
