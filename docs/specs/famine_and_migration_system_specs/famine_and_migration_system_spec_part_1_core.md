# Famine and Migration Mechanics

## Part 1: Core design

> **Current design clarification (2026-08-25):** The user clarification and accepted split implementation supersede any shared mechanic, category, or runtime-namespace wording retained below as historical design context. The current implementation uses independent `famine_*` and `migration_*` mechanics, `famine_decision_category` and `migration_decision_category`, and `famine_state_map_mode` and `migration_state_map_mode`; no combined mechanic, category, runtime namespace, or mapmode is current. Use [source_of_truth_map.md](../../plans/famine_and_migration_system_plans/source_of_truth_map.md) and [completion_report.md](../../plans/famine_and_migration_system_plans/completion_report.md) for current status, including the incomplete blockers.

> **Superseded incident-layer and probability note (2026-08-25):** Any historical wording in this specification about incident events, event-option probability, `famine_incident.1`, `migration_incident.1`, `fm_*`, or combined `famine_migration_*` planning IDs is superseded. The register helpers are accounting/presentation seams only; the incident event files and constants were deliberately deleted.

## System identity

This is a shared Chaos Redux system. It has no event ID and it does not enter the random event pool.

The system models how war, occupation, environmental damage, repression, outbreaks, trade isolation, state collapse, and relief policy can turn food stress into mass famine and turn civilian fear into internal displacement or cross-border flight.

Its purpose is to make civilian population loss and population movement react to the actual campaign. A state under siege should not behave like a peaceful agricultural state. A state hit by bombers, a nuclear strike, an outbreak, a camp network, or repeated requisition should not retain an unchanged civilian population until a scripted event removes a flat number. A receiving country should face real choices when large civilian flows reach its borders.

The system is built around five linked questions:

1. Can people in a state obtain enough food?
2. Can they safely remain where they live?
3. Can they reach another safe state?
4. Will another authority allow them to enter or settle?
5. How do relief, repression, concealment, and political choices change the result?

## Design promise

The player should be able to recognize the cause of a crisis, understand which public action can improve it, and see the human cost when the crisis is neglected or exploited.

A famine is not a cosmetic modifier. Severe stages remove real population and can destabilize a country. A migration flow is not a random population penalty. People leave one state, travel through a route, and arrive in another state when a valid destination exists. The origin loses population and productive capacity. The destination gains population and pressure. Dangerous travel, blocked borders, disease exposure, bombing, and forced movement can create additional deaths.

The design avoids fixed historical casualty scripts. Historical settings and profiles change the starting pressures, valid routes, administrative behavior, and likely severity. Actual deaths depend on population, duration, access to food, transport, relief, repression, environmental conditions, and player or AI choices.

## Player experience

### The first signs

The player normally encounters the system through a state report, a war report, or a response event.

Examples include:

- food queues and rationing after rail and port damage
- civilians leaving a front-line state after repeated strategic bombing
- a city losing access to its normal supply corridor
- an island state reporting dwindling reserves while hostile naval pressure cuts shipping
- displaced families arriving from a neighboring country
- people gathering at a border that has been closed
- camp escapes and deportation columns moving toward safer territory
- an outbreak causing voluntary flight, quarantine, and border disputes
- fallout forcing evacuation from a damaged state

`famine_register_initial_incident` and `migration_register_initial_incident` record accounting and presentation context after proven state transitions. They do not create event objects, event IDs, event-pool entries, event-log rows, random events, or pacing pulses. Famine and migration categories are separate, and each category appears only for its own genuine problem or threshold.

### The national issue

The famine category is `famine_decision_category`, and the migration category is `migration_decision_category`. The umbrella planning filename is documentation-only and is not a runtime identifier.

The category appears when at least one of these conditions is met:

- the country has a meaningful active internal displacement population
- the country has received a meaningful foreign refugee population
- the country has a large outward flow
- one or more borders contain a trapped population
- the country is conducting an organized evacuation or deportation program
- a famine state reaches its famine-owned threshold, or migration records a large, repeated, trapped, corridor, or reception issue within its own evidence window

The category remains concise. It shows the current role of the country, the primary pressure, the next relevant threshold, and three to five useful actions. It does not show every possible migration action at once.

### Crisis escalation

Food insecurity and displacement can reinforce each other.

- A famine creates flight.
- Flight removes agricultural and industrial labor from the origin.
- Crowding in receiving states increases shelter and supply pressure.
- Damaged transport blocks relief and evacuation.
- A closed border leaves people exposed in the origin or along the route.
- Repression can suppress movement while increasing deaths and opposition.
- A poorly managed return can reopen disease, housing, and food crises.

A well-managed response can break this cycle through rationing, transport repair, relief corridors, safe evacuation, distributed reception, and voluntary return.

## System layers

### State food security

Every affected state can hold a hidden food security score and one visible famine stage. The score is not shown as a raw number. The visible state modifier communicates the current stage, main causes, and recovery direction.

Food pressure comes from local production loss, import loss, transport loss, requisition, occupation policy, environmental damage, labor loss, disease, and governance failure. Relief, reserves, functioning routes, local substitution, medical support, and fair distribution reduce pressure.

### Civilian safety and flight pressure

Every affected state can hold a hidden flight pressure score and a visible displacement state when movement becomes material.

Flight pressure comes from front proximity, loss of control, bombing, nuclear damage, fallout, camps, genocide, forced labor, famine, outbreaks, harsh occupation, natural disaster, repression, and fear of the incoming authority.

The system should distinguish fear that creates voluntary flight from an order that forces movement. Organized evacuation, spontaneous flight, deportation, forced relocation, and camp transfer are separate causes with separate consequences.

### Population cohorts

The system does not need a detailed demographic simulator. It should still distinguish several functional cohorts when the distinction changes gameplay:

- general civilians
- vulnerable civilians, including children, elderly people, and the medically dependent
- industrial and transport workers
- agricultural workers
- persecuted political, ethnic, religious, or national groups
- camp, prison, gulag, and forced-labor populations
- military dependants and administrative evacuees

A response can prioritize one cohort. This creates a visible tradeoff. Evacuating skilled industrial workers protects production knowledge but leaves vulnerable civilians exposed. Prioritizing vulnerable civilians saves more lives but may require more transport and medical support. Forced labor or targeted persecution can block a cohort from normal evacuation routes.

### Route and border state

Every movement request resolves through a route state:

- safe internal route
- strained internal route
- safe international route
- contested international route
- maritime evacuation route
- smuggling or irregular route
- blocked border
- forced return route
- no valid route

The route affects how many people move, how long movement takes, what equipment or transport is required, and whether route deaths can occur.

### Reception and durable outcome

Arrival is not the end of the system. The receiving state can provide temporary shelter, distribute arrivals, integrate them, place them in transit, intern them, exploit their labor, or force them to return.

A displaced cohort eventually reaches one of four broad outcomes:

- voluntary return to the origin
- local integration in the receiving country
- organized resettlement to a third country
- prolonged displacement without a durable outcome

The system remembers enough origin and destination information to support return, property disputes, labor recovery, political movements, and postwar settlement.

## Core variables visible to the player

The system should expose no more than three country-level values in its main presentation.

### Displacement load

This is the primary value. It summarizes the current population that the country must transport, shelter, receive, monitor, integrate, or return.

The value rises through inflow, internal displacement, trapped groups, overcrowding, and unresolved long-term settlement. It falls through safe distribution, voluntary return, integration, resettlement, and restored origin conditions.

### Reception capacity

This supporting value summarizes available shelter, food, transport, local administration, sanitation, and medical support in the current receiving network.

It is not a permanent national statistic. It matters only while the country has an active displacement issue.

### Border policy state

This supporting state communicates the current national posture, such as open humanitarian entry, controlled entry, transit only, closed border, or emergency quarantine.

It should be a clear policy state with direct effects. It should not become a second numerical meter.

State-level famine stages and state-level displacement modifiers remain visible in affected states. The country category does not repeat every state number.

## Shared state progression

### Food security stages

The visible progression uses these functional stages:

1. Supply strain
2. Acute shortage
3. Famine
4. Catastrophic famine

A state without meaningful pressure has no famine modifier.

The internal food security score can move continuously. The visible stage changes only when thresholds are crossed with enough persistence to avoid daily flicker.

### Displacement stages

The visible progression uses cause-specific state modifiers. There is no universal ladder:

- population preparing to leave
- active civilian exodus
- organized evacuation
- depopulated districts
- displaced population reception
- overcrowded reception
- trapped at the border
- return and resettlement in progress

Only the modifiers relevant to the current state are shown.

## Crisis memory

Famine and displacement should leave memory after the immediate modifier disappears.

State memory can include:

- famine mortality memory
- relief success or abandonment memory
- forced requisition memory
- camp or deportation memory
- border closure memory
- origin and destination relationship
- abandoned property and return claims
- local political radicalization
- labor loss or labor arrival

Memory should not create a permanent stack of penalties. It should change later event weights, local opposition, relief trust, return willingness, and the response to renewed policy pressure.

## Political consequences

### Hunger politics

Famine can produce political opposition, but it does not automatically create one ideology.

The system should identify the most credible opposition channel from the current country and state:

- existing opposition parties
- rural or peasant movements
- worker organizations
- separatist or national movements
- religious relief networks
- anti-colonial organizations
- military or garrison mutiny
- local councils and food committees
- foreign-backed underground groups

The outcome depends on ruling ideology, local party support, relief fairness, repression, visible blame, prior movement presence, foreign sponsorship, and whether the population sees the crisis as natural, military, administrative, or deliberate.

A democratic country that protects one group while abandoning another can still generate radical opposition. A communist country fighting another communist country may see lower fear from ideology alone, but bombing, forced requisition, camps, national persecution, and direct violence can overwhelm that affinity.

### Host-country politics

Large inflows can affect the receiving country through:

- relief solidarity
- labor integration
- housing conflict
- ration competition
- security panic
- ideological recruitment
- local resentment
- diplomatic pressure
- pressure for border closure
- demands for repatriation

These effects should be based on actual load and policy. A small, well-supported inflow should not destabilize a major country. A large unmanaged inflow into damaged states can become a serious issue.

## Failure states

The system has several forms of failure. They are not all equivalent.

### Administrative failure

The country has resources but fails to distribute food, organize transport, or coordinate receiving states. This increases deaths, congestion, and opposition.

### Capacity failure

The country lacks food, transport, shelter, convoys, trains, medical support, or safe states. It can seek foreign relief, negotiate corridors, reduce other commitments, or accept a partial outcome.

### Military failure

A route is cut, a city is encircled, an island is blockaded, or a reception state becomes a front line. The player must restore access, evacuate, or accept a worsening crisis.

### Deliberate exploitation

The government uses hunger, forced labor, deportation, closed borders, or forced return as policy. This can provide short-term control, labor, extraction, or military advantage. It creates deaths, hidden or public atrocity evidence, condemnation, resistance, and long-term instability.

### Concealment failure

A government suppresses reports or falsifies food data. The visible crisis can appear smaller for a time. Relief arrives later and the eventual exposure increases blame, opposition, and condemnation.

### Cascade failure

Famine, disease, displacement, bombing, and environmental damage combine. A cascade can spread across several neighboring states or along a major evacuation route. It should remain understandable through a cause breakdown and specific response actions.

## Success states

### Stabilized food access

The state has enough local supply, imports, routes, and relief to stop the mortality stage. Recovery continues until the acute modifier can be removed.

### Safe displacement management

People move from an unsafe origin to a valid receiving state with low route deaths, adequate reception, and a clear durable plan.

### Restored home conditions

The origin no longer has the active cause that forced flight. Housing, food, infrastructure, safety, and political protection are sufficient for voluntary return.

### Successful integration

A receiving country converts a long-term displaced population into normal state population without leaving a permanent crisis modifier. Integration can improve labor and population while requiring time, housing, food, and political work.

### International relief network

Several countries cooperate through corridors, convoys, aid, sponsorship, or resettlement. This should create a meaningful diplomatic benefit and reduce deaths. It should not erase the receiving burden for free.

## Pacing

The system should react quickly to major shocks and slowly to structural decline.

- Nuclear strikes, camp evacuations, front collapse, city capture, and severe bombing can create immediate movement requests.
- Blockade, occupation requisition, transport failure, drought, crop loss, and air contamination build pressure over time.
- Famine deaths occur in scheduled state pulses while the state remains in a mortality stage.
- Migration flows resolve in bounded cohorts. One large instant transfer is reserved for a direct evacuation or expulsion event that requires it.
- Recovery takes longer than the initial relief action. One decision can stop worsening without instantly restoring normal conditions.

## Performance model

The design uses event-driven requests and bounded active registries.

A state enters the food-security registry when a qualifying source creates material pressure. A state leaves after recovery and memory settlement. A country enters the displacement registry when it has an active origin, destination, route, or trapped cohort. Only registered states and countries receive scheduled processing.

Relevant hooks include state-control change, occupation-law change, strategic bombing aftermath, nuclear aftermath, outbreak creation or escalation, camp and gulag changes, disaster effects, event adapters, war and peace transitions, route restoration, and direct decisions.

The system should not depend on a whole-world daily, weekly, or monthly iteration.

## Exclusions and safeguards

Ordinary civilian logic should exclude special Chaos countries and actual nonhuman countries when they do not represent a normal human civilian society. Such countries can still create flight pressure in neighboring human states.

Population transfers must fail closed when the origin, destination, amount, route, or ownership context cannot be proven. The system must never duplicate population, remove population twice, or count movement as death.

A state should not lose more civilians than its protected population floor allows. A destination should receive only the amount actually removed from the origin, minus separately recorded route deaths.

The same physical death must have one owner in the Deaths ledger. The source ownership rules are defined in Part 4 and in the death-reason matrix.

## Final design standard

The system succeeds when a player can look at a state or decision category and answer these questions:

- Why are people hungry or leaving?
- How serious is the current state?
- Which route or resource is failing?
- What can the country do now?
- What will happen if the country delays, refuses, represses, or helps?
- Where did the displaced population go?
- Which deaths came from famine, occupation, deportation, route exposure, bombing, nuclear effects, outbreaks, or camps?

The system fails if it becomes a random population drain, a hidden score with vague events, a permanent decision store, or a fixed historical casualty script.
