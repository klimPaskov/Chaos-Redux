# Event 41 evolutions and international spread specification

## Evolution structure

Disease in Divisions has two true evolutions.

- Evolution I is Camp Fever Across the Trenches at 200 or more Chaos.
- Evolution II is War Plague at 600 or more Chaos.

Baseline pressure stages continue independently from the evolution track. A country can suffer an army crisis without activating an evolution. An evolution changes transmission rules and available responses. Evolution activation itself gives no Chaos.

Each evolution supports two entry paths:

- active-event evolution changes an outbreak that is already running
- pre-fire evolved opening changes the next Event 41 firing when the evolution is already active

The evolution should arrive through paced event logic. It should not unlock on the same instant that Chaos crosses the threshold unless the event has not yet fired and the evolved opening is being prepared.

## Evolution I: Camp Fever Across the Trenches

### Playable purpose

Camp Fever Across the Trenches turns one country's sector epidemic into a military-network problem. Large concentrations, depots, headquarters, reserve areas, expeditionary forces, and sustained contact across a front can carry the disease between armies.

The evolution should make troop concentration and coalition logistics dangerous. It should not create immediate civilian transmission.

### Eligibility and pacing

The evolution becomes eligible from 200 Chaos when Event 41 is enabled.

For an active episode, the evolution should become more likely when:

- pressure is moderate or high
- several military nodes are active
- the outbreak has lasted for many weeks
- affected formations remain in combat
- the sector contains allied or enemy forces in sustained contact
- large camps, depots, or transport hubs are involved
- quarantine and sanitation have failed

Strong early containment should lower the chance that an active episode mutates before resolution.

The ordinary pacing target should be measured in months, with a shorter delay for a severe crowded front and a longer delay for a contained episode.

### Active-event entry

When the evolution activates during an episode, it should immediately:

- record the evolution milestone with the affected country as actor
- upgrade the transmission model for active military nodes
- allow reserve and rear-area military nodes to become infected
- mark coalition and enemy contact routes as eligible
- increase the value of dispersal, intelligence warning, quarantine, and transport control
- unlock the international military spread reports and response actions
- preserve the existing sick, recovery, and death ledgers without resetting them

The activation should not seed every connected army at once. It creates a short danger window in which the source country's conditions and foreign protections determine whether transmission occurs.

### Pre-fire evolved opening

When Evolution I is already active before Event 41 fires, the opening should change in four ways.

1. The seed group is wider, while remaining bounded to a coherent operational network.
2. Initial pressure is higher than an ordinary baseline opening.
3. One rear-area military node can begin exposed.
4. A valid allied or enemy army can receive an early exposure test during the first weeks.

The first foreign exposure test should remain a chance shaped by actual contact. A country with no sustained military link to the source cannot be selected.

## Evolution I military transmission routes

### Same-front allied spread

Allied armies can be exposed through:

- expeditionary forces
- allied formations fighting in the same state group
- shared military access
- common supply hubs
- common ports and staging areas
- coalition hospital or transport networks

### Same-front enemy spread

Enemy armies can be exposed through:

- prolonged combat in the same states
- captured trenches and positions
- overrun hospitals
- prisoners and battlefield collection points
- repeated advance and retreat through the same cities
- contaminated camps and supply stores left behind

Enemy transmission should require sustained contact or a concrete transfer event. A single brief battle should not routinely infect another country.

### Rear-area military spread

Reserve formations, headquarters, airbase personnel, and logistics units can become part of the military epidemic when they share an infected node. These groups can increase national pressure and carry exposure to another front.

They remain within the military event model. Civilian cases are still unavailable until Evolution II.

## Secondary national outbreaks

A valid foreign military transmission creates a secondary Event 41 outbreak in the receiving country.

The receiving country gets:

- its own Army Infection Pressure
- its own temporary decision category
- its own affected military nodes
- its own sick, recovery, and death accounting
- a visible source relationship to the originating episode
- a warning benefit when the source outbreak was already publicly known

### Reduced opening severity

Secondary outbreaks should usually begin weaker than the source because the receiving army has warning and can isolate the first cases.

Opening severity should rise when:

- the receiving army has poor intelligence or no warning
- the exposure occurred through overrun hospitals or mass prisoner movement
- the receiving country has low medical capacity
- the receiving front is already undersupplied
- the source country is at very high pressure

Opening severity should fall when:

- the country has strong intelligence and medical preparation
- it has recent-survivor resistance
- the shared front is well supplied
- it can separate expeditionary forces quickly

### Generation and duplication control

Each secondary outbreak needs a generation link to the source episode. The same source-target pair should not create repeated openings without a new and distinct exposure after the previous receipt has been resolved.

A foreign country already running Event 41 should absorb the new exposure into its current episode through a bounded pressure or node increase. It should not receive a duplicate category or duplicate sick ledger.

## Evolution I response additions

### Inspect Allied Formations

A country sharing a front with an infected ally can spend intelligence or command resources to gain early warning, reduce opening severity, and identify exposed expeditionary formations.

### Separate Coalition Camps

Faction members can divide camps, hospitals, and supply areas. This costs logistics flexibility and support equipment, but lowers allied transmission.

### Exchange Field Medical Reports

Countries with sufficient relations, faction ties, or intelligence can share profile and exposure information. The action improves secondary warning and response efficiency. It should not reveal hidden raw profile variables to the player.

### Restrict Military Access

A country can temporarily restrict infected allied movement through its territory. This lowers transmission risk and damages coalition flexibility and relations.

These actions should appear only when a real foreign military link exists. They should not clutter the category in an isolated national outbreak.

## Evolution I containment

Evolution I remains contained when:

- the source country lowers pressure
- active military nodes are isolated
- no new country is exposed for a sustained period
- existing secondary outbreaks are controlled
- coalition movement restrictions and warnings are no longer needed

The evolution itself remains globally unlocked for later firings. The episode can close when its own transmission chain is quiet.

## Evolution II: War Plague

### Playable purpose

War Plague breaks the military boundary. Sick soldiers, hospitals, transport hubs, refugee routes, demobilization, ports, and ruined rear areas can carry disease into civilian populations. Coalition logistics can also move the military epidemic between distant theaters.

The evolution should create a dangerous international wartime epidemic while keeping a clear containment path. It should use the existing civilian outbreak, Deaths, Air Cleanliness, Famine, and Migration systems through their owning adapters.

### Eligibility and pacing

War Plague becomes eligible from 600 Chaos when Event 41 is enabled and Evolution II is enabled.

For an active episode, it should become more likely when:

- pressure is high
- the episode spans several countries
- civilian transport hubs overlap infected military nodes
- military hospitals are overloaded
- infrastructure and sanitation are ruined
- famine and refugee pressure are present
- chemical or biological warfare has affected the theater
- heavy strategic bombing or disaster damage has created mass displacement
- the source country continues offensive operations through severe infection

Strong international containment should delay or prevent active-event evolution before the episode ends.

### Active-event entry

When War Plague activates during an episode, it should immediately:

- record the evolution milestone with the primary source country as actor
- enable civilian spillover checks in eligible military nodes
- enable distant military transmission through coalition logistics
- increase the consequence of ports, hospital trains, and demobilization routes
- unlock military district, port, allied access, and civilian-protection actions
- preserve all existing episode and secondary outbreak ledgers
- avoid creating civilian cases until a valid state and adapter contract are proven

### Pre-fire evolved opening

When War Plague is active before Event 41 fires, the opening can begin with:

- a wider military footprint
- Evolution I cross-border military risk
- one exposed rear-area transport node
- immediate civilian spillover risk in the opening node
- a stronger international warning report when several countries share the theater

Civilian spillover should still require a valid state and a successful handoff. The opening should not create an untracked civilian population loss.

## Civilian spillover model

Event 41 owns the military source and the proof that a civilian state has been exposed. It does not own the civilian outbreak runtime.

### Spillover source conditions

A military node can submit a civilian spillover request when it has:

- sufficient military infection pressure
- a valid civilian state connection
- a sustained exposure route
- no active duplicate request for the same episode and state

### Strong spillover routes

- military hospitals inside populated states
- hospital trains and evacuation terminals
- ports handling infected troops
- large military camps near cities
- demobilized or returning soldiers
- refugee routes crossing military nodes
- contaminated rear-area supply hubs
- prisoner and displaced-person camps
- bombed cities with damaged water and sanitation

### State vulnerability

Spillover becomes more likely in states with:

- high population
- low medical capacity
- damaged infrastructure
- famine pressure
- trapped or displaced population
- chemical contamination
- existing biological exposure
- sustained bombardment
- crowded ports and transport hubs

### Adapter contract

The Event 41 adapter should submit:

- source episode proof
- source country
- exposed state
- military pressure band
- hidden profile family or safe profile mapping
- exposure route
- severity request
- one-shot generation identifier

The receiving biological outbreak system should validate the request, decide whether a compatible civilian outbreak is created or strengthened, and return a receipt.

Event 41 should read only the receipt and high-level status needed for military decisions. It should not read or rewrite the civilian system's primary ledger.

### Existing civilian outbreak

When the state already has a compatible biological outbreak, the adapter should strengthen or link the existing outbreak according to owner rules. It should not create a duplicate state disease.

### Civilian deaths and contamination

Civilian deaths are owned and registered by the civilian outbreak system. Air Cleanliness contribution is also owned by the civilian or biological system. Event 41 must not register the same deaths or contamination again.

## Famine and Migration interaction

War Plague can worsen existing humanitarian conditions without owning them.

### Famine

Military infection can:

- reduce relief access when ports or railways close
- raise local need through hospital and camp demand
- worsen vulnerability where supply systems are damaged
- make field sanitation more difficult

Event 41 should publish a bounded disease-risk fact or adapter input. It should not modify the famine ledger directly unless the famine owner exposes a specific public adapter.

### Migration

Military disease can:

- create quarantine restrictions
- reduce reception capacity
- make a corridor medically unsafe
- require controlled medical reception
- increase trapped populations when borders close

Movement does not become a death event by itself. The Migration system retains ownership of cohort transfer and forced-displacement deaths.

## Distant-theater military transmission

War Plague permits military transmission between distant theaters through proven coalition and transport links.

Valid routes can include:

- expeditionary forces returning home
- troop transports between ports
- shared convoy routes
- reinforcement routes through a faction hub
- hospital ships or strategic evacuation routes
- long-distance air or rail redeployment

Distant transmission should be rarer than same-front spread. It becomes important when the source country has high pressure, weak screening, and frequent troop movement.

## War Plague response additions

### Close Military Ports

The country can close one or more infected military ports to troop movement. This sharply reduces distant spread and weakens overseas supply, evacuation, and reinforcement.

### Isolate a Military District

The Evolution II version also reduces civilian spillover from the district. It creates larger local supply and movement costs than the baseline crisis action.

### Restrict Allied Access

The country can deny infected allied formations entry or transit. This lowers transmission and harms coalition relations and military coordination.

### Controlled Demobilization

When a war ends or formations return home, the country can stage their return through screening and quarantine. This costs transport, support equipment, and time while reducing civilian spillover.

### Protect Civilian Transport Hubs

The country separates military evacuation and troop movement from civilian rail, port, and urban traffic. This uses civilian capacity and transport flexibility. It reduces spillover probability.

### Request International Medical Coordination

Faction members or threatened neighbors can share warnings, quarantine standards, and medical transport. The action should strengthen receiving-country protection and lower duplicate spread. It should carry diplomatic or material obligations.

## International episode state

One War Plague episode can contain several national military outbreaks and several civilian outbreak receipts.

The source episode should track only the relationships needed to:

- prevent duplicate transmission
- display the international scope
- determine whether the chain is growing or quiet
- apply one-shot Chaos milestones
- close the military episode when all linked military outbreaks resolve

It should not become a second world disease ledger.

## War Plague containment

An international episode is contained when:

- every active military outbreak in the generation has resolved or entered its final recovery window
- no new military transmission has occurred for a sustained period
- no unacknowledged civilian spillover request remains
- active civilian outbreaks continue under their owner without needing Event 41 military processing
- ports, access restrictions, and military district controls can be removed safely

The military Event 41 episode can close while a civilian outbreak continues. The civilian owner retains its own lifecycle and cleanup.

## War Plague failure states

### Coalition logistics collapse

Several countries close access and ports, damaging reinforcement and supply. This should create military consequences without automatically dissolving the faction.

### Medical competition

Civilian outbreaks and military cases compete for transport and hospitals. Military recovery slows, civilian systems receive higher demand, and hard choices appear.

### Abandoned theater

A country leaves an infected sector or suspends a major operation. The disease burden falls, but the enemy gains strategic opportunity.

### International epidemic

Several countries and civilian states become linked. This should trigger a major report, an event-owned Chaos milestone, and stronger coordination tools.

## Evolution disable behavior

If Evolution I is disabled, Event 41 remains a national military epidemic and cannot use cross-border military transmission.

If Evolution II is disabled, military spread can still occur under Evolution I, but civilian spillover and distant-theater transmission remain unavailable.

Disabling an evolution should not block baseline resolution. Existing foreign or civilian systems created before a setting change should finish safely under their owners, while Event 41 stops creating new evolution-gated transmissions.

## Evolution log direction

Evolution I log text should represent the recognition that camps, depots, and front contact have become a transmission network.

Evolution II log text should represent the military epidemic crossing into rear society and international transport.

The log should show the parent event, evolution stage, Chaos tier, date, and actor when present. It should not show ordinary pressure stages as evolution entries.
