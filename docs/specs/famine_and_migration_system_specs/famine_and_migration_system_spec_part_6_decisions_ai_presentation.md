# Famine and Migration Mechanics

## Part 6: Decisions, missions, AI, and presentation

> **Current design clarification (2026-08-25):** The user clarification and accepted split implementation supersede any shared mechanic, category, or runtime-namespace wording retained below as historical design context. The current implementation uses independent `famine_*` and `migration_*` mechanics, `famine_decision_category` and `migration_decision_category`, and `famine_state_map_mode` and `migration_state_map_mode`; no combined mechanic, category, runtime namespace, or mapmode is current. Use [source_of_truth_map.md](../../plans/famine_and_migration_system_plans/source_of_truth_map.md) and [completion_report.md](../../plans/famine_and_migration_system_plans/completion_report.md) for current status, including the incomplete blockers.

> **Superseded incident-layer and probability note (2026-08-25):** Any historical wording in this specification about incident events, event-option probability, `famine_incident.1`, `migration_incident.1`, `fm_*`, or combined `famine_migration_*` planning IDs is superseded. The register helpers are accounting/presentation seams only; the incident event files and constants were deliberately deleted.

## Presentation choice

The two mechanics should use their own ordinary state modifiers, accounting/presentation seams, report context, decision categories, concise scripted localisation, and map highlighting.

A full dedicated scripted GUI is not justified. Famine presents Food Security as its primary value with Food Reserves and Relief Access as its two supporting values. Migration presents Displacement Load as its primary value with Reception Capacity and Border Policy as its two supporting values. Each normal decision category uses its own static category picture, compact dynamic header, state-targeted decisions, and clear tooltips.

The famine category can show Food Security, Food Reserves, and Relief Access. The migration category can show Displacement Load, Reception Capacity, and Border Policy. Neither category should become a full mechanic window, and the two categories must not be united.

## Presentation families

The system uses several report and presentation families. They are not event objects, do not receive an event ID, and do not enter the random-event pool.

### Food-security incident reports

These appear when a state crosses a meaningful threshold or a new source becomes dominant.

Possible report roles:

- first supply strain
- acute shortage
- first famine state
- catastrophic famine
- island blockade
- siege hunger
- relief corridor opened
- relief convoy lost
- concealed crisis exposed
- famine recovery
- renewed famine after failed recovery

The report should name the state, current controller, main pressure, and available public response.

### Civilian-flight incident reports

Possible roles:

- civilians preparing to leave
- spontaneous internal exodus
- organized evacuation request
- cross-border arrival
- border closure and trapped population
- nuclear evacuation
- camp or genocide escapees
- outbreak flight
- famine flight
- strategic-bombing evacuation
- forced deportation
- return request
- host integration dispute

The first proven transitions use concise report context and standing-category guidance so the system can be understood before each decision category appears; they do not create event options.

### Foreign response events

Foreign countries can receive bounded responses when they are directly relevant as:

- neighboring destination
- faction partner
- guarantor
- relief donor
- occupier
- blockade enforcer
- third-country resettlement candidate
- country accused of deliberate starvation or forced return

The system should not broadcast every local movement to every country.

### Political consequence events

Political events appear when famine, displacement, unequal relief, repression, or border policy creates a material domestic consequence.

Possible roles:

- bread riot
- rural refusal of requisition
- local relief committee
- military mutiny over civilian starvation
- nationalist or separatist organization
- religious sanctuary network
- host-country anti-refugee agitation
- solidarity campaign
- labor integration dispute
- forced-return scandal
- evidence exposure

These events should use current ideology, party support, regional identity, and prior choices.

## Decision-category lifecycle

### Hidden phase

The category is hidden at game start.

A country can receive accounting/presentation context and use only valid owner-local actions before its own standing category appears.

### Emerging issue phase

The category becomes eligible after a meaningful threshold such as:

- two or more displacement incidents in the recent window
- one large flow
- one severe trapped-population crisis
- one organized national evacuation
- one mass foreign arrival
- sustained famine-driven movement

The first category-opening event explains why the issue now requires a standing policy.

### Active management phase

The category shows:

- current Displacement Load
- current Reception Capacity
- current Border Policy
- up to three urgent state or border missions
- three to five relevant actions

The actions depend on whether the country is mainly an origin, destination, transit state, occupier, or mixed case.

### Resolution phase

When the issue becomes manageable, the category shifts toward return, integration, resettlement, and cleanup.

### Dormant phase

The category closes when no material issue remains. It can reopen later with prior policy memory intact.

## Famine response decision family

Famine decisions appear in the existing or shared humanitarian category when a state enters acute shortage or worse. They should not require the migration category unless displacement is also material.

### Release reserves and impose rationing

Narrative role:

The government redirects stored food and controls distribution.

Likely costs:

- civilian factory burden
- stability or war support risk
- military supply opportunity cost
- reserve depletion represented through an existing or system stock value

Effects:

- immediate reduction in food pressure
- lower mortality risk
- possible black-market and fairness consequences

AI preference:

High when the state is populated, mortality is active, reserves exist, and the war front can tolerate the cost.

### Emergency food imports

Narrative role:

The country secures food from a foreign source.

Likely costs:

- convoys
- fuel
- trade or diplomatic obligation
- civilian factories

Requirements:

- valid donor or market access
- functioning port or land route
- no complete blockade

Effects:

- reduces availability pressure
- can create dependence or foreign influence

### Repair the relief route

Narrative role:

The country commits trains, trucks, fuel, engineers, and units to restore access.

Likely costs:

- trains
- trucks
- fuel
- support equipment or civilian factory burden

Objective:

Repair or secure named rail, port, bridge, hub, or corridor states.

The action should create a timed mission when the player must hold or repair actual locations.

### Escorted relief convoy

Narrative role:

The country attempts to break an island or coastal blockade.

Likely costs:

- convoys
- fuel
- naval or air escort commitment
- supplies

Outcome factors:

- hostile naval and air pressure
- port damage
- escort strength
- weather
- route distance

The result can be full delivery, partial delivery, delay, or loss.

### Emergency airlift

Narrative role:

The country uses transport aircraft and fuel to deliver limited high-priority relief.

The airlift should be expensive and limited. It can save vulnerable groups or prevent a stage increase. It should not replace a functioning sea or rail route for a dense state.

### Invite international relief

Narrative role:

The government accepts foreign aid, observers, and logistical access.

Tradeoffs:

- lower mortality
- improved diplomacy
- reduced concealment
- possible exposure of camps, requisition, or corruption
- foreign influence or inspection pressure

### Organize famine evacuation

Narrative role:

The country moves a bounded cohort to a safe state.

The action calls the migration system and requires a destination, transport, and reception capacity.

### Requisition from safer states

Narrative role:

The government shifts food from one region to another.

Effects:

- reduces pressure in the target
- increases pressure and grievance in the donor
- can become abusive when the donor is occupied, persecuted, or already strained

### Conceal the shortage

Narrative role:

The government suppresses reporting and delays public action.

Effects:

- lower immediate public pressure
- delayed foreign response
- higher hidden cover-up evidence
- higher mortality and exposure risk

### Maintain extraction

Narrative role:

The government prioritizes military, export, occupation, or ideological goals.

Effects:

- short-term resource or supply benefit
- higher famine pressure
- opposition and evidence
- possible forced movement

This option should be available only when a real extraction policy exists.

## Migration origin decision family

### Prepare an evacuation plan

The country selects priority states, destination capacity, and transport reserves before the crisis peaks.

Preparation reduces later route deaths and congestion.

### Evacuate vulnerable civilians

The country moves a smaller, high-need cohort.

Costs can include trains or convoys, support equipment, fuel, and reception capacity.

### Evacuate industrial workers and machinery support staff

The country preserves critical labor and production knowledge.

Tradeoff:

- lower origin production
- better destination production recovery
- vulnerable civilians receive less transport priority

The decision should not physically move factories unless a separate industry relocation system supports that action.

### Open civilian departure routes

The country permits and supports spontaneous flight.

This lowers trapped pressure but creates less controlled destination selection.

### Restrict civilian departure

The country holds labor and population in place.

This can preserve local production and secrecy. It increases trapped pressure when danger remains.

### Negotiate a humanitarian corridor

The country targets an enemy, neutral, faction partner, or neighbor.

The action can create a timed diplomatic mission with acceptance factors based on ideology, condemnation, war goals, route value, and military advantage.

### Organize maritime evacuation

The country uses ports, convoys, fuel, and escorts to move civilians.

### Abandon the state

The government orders rapid withdrawal and accepts high property loss and disorder.

This can move more people quickly when a route exists. It creates severe local economic and political consequences.

## Migration destination decision family

### Open emergency reception

The country accepts arrivals and assigns temporary shelter.

### Distribute arrivals among safe states

The country reduces border-state overload by moving people through its internal network.

Requirements:

- valid safe states
- transport
- receiving capacity

### Establish controlled medical reception

The country accepts exposed arrivals through quarantine and medical support.

This should reduce outbreak risk without treating all migrants as diseased.

### Prioritize vulnerable groups

The country accepts children, elderly people, injured civilians, or persecuted cohorts first.

Excluded groups remain in the route system and can become trapped.

### Prioritize skilled workers or co-nationals

The country selects people who fit labor or national policy.

This can improve long-term integration while creating diplomatic and moral consequences.

### Allow transit

The country provides route access to a confirmed destination.

### Close the border

The country prevents normal entry.

The decision must explain the expected reduction in inflow and the risk of trapped populations, irregular crossings, and foreign pressure.

### Enforce the closure

The country commits units, equipment, and political authority to stop irregular crossings.

The action can become violent depending on policy and AI. It should never be a harmless free toggle.

### Establish internment or labor reception

The country detains or exploits arrivals.

This can reduce security pressure or provide labor. It creates resistance, condemnation, forced-labor, and atrocity risks.

### Begin local integration

The country converts a long-term displaced population into normal local population over time.

Costs can include housing construction, civilian factories, food, administration, and stability work.

### Seek third-country resettlement

The country asks partners or neutral states to accept part of the population.

### Support voluntary return

The country provides transport and reconstruction aid after the origin becomes safe.

### Force repatriation

The country sends people back regardless of willingness.

The action can create route deaths and condemnation when the origin remains dangerous.

## Border and corridor missions

Missions should require real action.

### Keep the corridor open

Objective examples:

- control named border states
- maintain rail or port access
- keep a route supplied
- hold a ceasefire condition
- prevent hostile control of a route state

### Protect the evacuation trains

Objective examples:

- maintain rail control
- assign units to named states
- keep infrastructure above a threshold
- avoid loss of the destination hub

### Deliver relief before reserves fail

Objective examples:

- complete a convoy or import decision
- restore a port
- secure a rail hub
- achieve a minimum relief level before the deadline

### Prevent reception collapse

Objective examples:

- distribute arrivals
- add shelter or infrastructure
- improve food security
- avoid an outbreak in the reception state

### Prepare the return route

Objective examples:

- clear fallout or contamination below the return threshold
- restore housing and infrastructure
- remove active persecution and camp threats
- restore food security

Mission durations should vary with distance, damage, and severity. Large logistical objectives need enough time for the player and AI to act.

## Decision costs

A decision or gameplay-changing action uses no more than four spendable cost types.

The cost should fit the action.

Useful cost types include:

- trains
- convoys
- trucks
- support equipment
- fuel
- civilian factory burden
- manpower for administration or medical support
- stability
- war support
- army, navy, or air experience when the action is a specialized military operation
- tied-down divisions as a requirement or commitment
- local reception capacity
- food reserve or relief stock value

Political power can support political and diplomatic actions. It should not be the only cost for transport, relief, evacuation, or reception.

## Initial event choices

Before the category unlocks, report context and state-targeted guidance should explain the immediate situation; no incident event or event-option pool is created.

Examples for an arriving refugee flow:

- admit and shelter
- admit vulnerable groups only
- permit transit
- close the border

Examples for a bombed state:

- organize evacuation
- open voluntary departure routes
- keep workers in place and expand shelters
- deny that evacuation is needed

Examples for an island shortage:

- commit a relief convoy
- begin rationing
- evacuate vulnerable civilians
- prioritize the garrison

The options should communicate visible consequences without exposing hidden probability or future surprise branches.

## State selection and clutter control

A country can have many affected states. The category should not show one permanent decision for every state.

Use:

- urgent state cap
- selected-state target flow
- regional grouping
- highest-severity priority
- rotating secondary reports
- hidden resolved decisions

The main category should normally show no more than three active state missions and six primary actions.

## Map presentation

The system should support clear map highlighting when a decision or report targets states.

Useful state colors include:

- food-security stage
- origin flight pressure
- valid internal destinations
- overloaded receiving states
- open or blocked corridors
- trapped border states
- return-ready origins

The player should never need to memorize raw state IDs.

## State modifier presentation

Each modifier should show:

- current stage or role
- main active causes
- direction of change
- major gameplay effects
- next threshold or recovery requirement
- current government response when one is active

The tooltip should remain concise. Detailed component calculations can appear in a secondary breakdown when the player needs them.

## AI goals

AI should answer the same practical questions as the player.

### Famine AI

The AI should:

- prioritize populated famine states
- prefer relief when resources and routes exist
- repair the cheapest effective route
- use evacuation when relief cannot arrive in time
- avoid draining another state into famine without a high-priority reason
- consider military survival before diverting all transport
- accept foreign relief when mortality and collapse risk exceed secrecy or ideological cost
- conceal or maintain extraction according to regime profile, war pressure, condemnation, and opposition risk
- stop a failed policy when evidence and mortality become severe unless the regime is deliberately exterminatory

### Origin AI

The AI should:

- evacuate from imminent front collapse, nuclear fallout, catastrophic famine, camps, or severe bombing
- prefer internal destinations when safe
- use allies, guarantees, neighbors, and historical ties for foreign destinations
- preserve transport for military survival
- prioritize vulnerable cohorts when mortality is immediate
- prioritize workers when national survival depends on critical industry
- avoid routing civilians into another active crisis
- seek corridors when no safe route exists

### Destination AI

The AI should:

- compare load with capacity
- prefer open or controlled entry for allies, co-nationals, persecuted groups, and manageable flows
- use quarantine reception for proven outbreak exposure
- distribute arrivals away from overloaded border states
- close borders when capacity is exhausted or the route is militarily impossible
- avoid violent pushback unless ideology, policy, and regime behavior support it
- avoid forced return to a known extermination, famine, or active-combat zone unless the regime is willing to accept condemnation and resistance
- begin integration when return is unlikely and capacity exists
- support return when the origin is safe

### Occupation AI

The AI should:

- choose extraction according to war need, ideology, manpower, resistance, and condemnation
- understand that severe extraction can destroy future production and increase resistance
- use protected administration when it needs stable long-term control
- use forced labor and deportation only when policy and strategy justify the cost
- accept relief when famine threatens control unless deliberate starvation is part of the regime policy

## AI archetypes

Useful archetypes include:

- humanitarian democracy
- capacity-limited democracy
- neutral sanctuary
- authoritarian security state
- fascist occupation regime
- communist mobilization state
- colonial extraction regime
- collapsing government
- revolutionary administration
- special high-chaos human regime

The archetype modifies preference. Current resources and danger remain decisive.

## Weighted behavior and probability plan

Every complex AI choice, event option, destination pool, route pool, and political-outcome pool requires a named probability audit.

The package includes a scenario matrix covering:

- island blockade relief
- severe urban famine
- Soviet extraction and concealment
- democratic border response
- capacity-exhausted border response
- outbreak quarantine reception
- nuclear evacuation
- genocide escapees
- forced return
- postwar voluntary return
- opposition ideology selection
- destination starvation and invalid-route protection

The implementation agent should use the HOI4 probability tools to inspect, evaluate, sweep, simulate, render, and compare the final source according to the matrix.

## Player-facing writing direction

### Famine reports

Viewpoint:

Civilians, local relief workers, transport staff, doctors, farmers, and affected local authorities.

Visible information:

Food queues, ration changes, closed routes, empty markets, abandoned farms, convoy failure, hidden stores, relief arrivals, and the physical condition of the population.

Tone:

Serious and concrete. Administrative euphemism can appear when a government conceals or exploits the crisis.

Avoid:

Generic world-ending language, cheap jokes, invented casualty certainty, and text that calls itself a warning.

### Migration reports

Viewpoint:

Families on the road, railway staff, border guards, local officials, relief workers, host communities, and returning residents.

Visible information:

What caused movement, where people are trying to go, which route is failing, and what the government is deciding.

Tone:

Concrete and human. Ideology and policy should appear through actions and expected treatment.

Avoid:

Describing migrants as a faceless threat by default, presenting refugees as inherently diseased, or reducing movement to map statistics.

### Atrocity and forced-movement reports

Viewpoint:

Targeted civilians, escapees, witnesses, occupiers, camp administrators, foreign observers, and liberators.

Tone:

Severe. Official euphemism, denial, and self-damning bureaucratic language can reveal responsibility.

Avoid:

Humor, spectacle, graphic detail for its own sake, and final legal claims that the research does not support.

## Asset presentation direction

The system needs a coordinated visual family, including:

- famine state-modifier icons for each visible stage
- displacement state-modifier icons for active exodus, reception, trapped border, and return
- separate `famine_category` and `migration_category` decision category icons
- separate `famine_category_picture` and `migration_category_picture` static decision category pictures
- decision icons for famine relief, convoy, airlift, famine evacuation, migration evacuation, border opening, border closure, quarantine reception, distribution, integration, and return
- Deaths reason icons or texticons when the current Deaths UI supports them
- report images for generic famine, island blockade, wartime evacuation, border closure, relief arrival, nuclear evacuation, and return

The asset prompt defines source modes and target surfaces.

## Acceptance outcomes for decisions and AI

This part is complete only when:

- the category is hidden until the issue becomes sustained
- initial accounting seams present meaningful context without an event object, event ID, event-pool entry, or pacing pulse
- the category shows one primary value and at most two supporting values
- each phase shows only current actions
- decisions use concrete costs and no more than four spendable types
- missions require real state, route, transport, or relief action
- state selection avoids decision walls
- map highlighting shows exact targets and routes
- AI has equivalent actions
- weighted pools receive probability audits
- player-facing text explains cause and response without exposing hidden calculations
- the system uses ordinary UI layers unless implementation evidence proves that a compact attached display is needed
