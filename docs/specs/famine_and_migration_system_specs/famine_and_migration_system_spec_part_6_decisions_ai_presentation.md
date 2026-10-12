# Famine and Migration Mechanics

## Part 6: Decisions, missions, AI, and presentation

> **Authority and status:** Read [README.md](README.md) for the accepted split, event-free presentation contract and current continuation record.
> The source parts and matrices preserve design and historical planning; their presence does not establish approval or completion.

> **Superseded incident-layer and probability note (2026-08-25):** Any historical wording in this specification about incident events, event-option probability, `famine_incident.1`, `migration_incident.1`, `fm_*`, or combined `famine_migration_*` planning IDs is superseded. The register helpers are accounting/presentation seams only; the incident event files and constants were deliberately deleted.

## Presentation choice

### Accepted first-reception presentation boundary (2026-10-03)

Acceptance basis: the original user goal requires complete valid player and AI reception responses with delayed problem visibility, and the parent reviewed and accepted the [prospective reception plan](../../plans/famine_and_migration_system_plans/prospective_reception_lifecycle_plan_20261003.md) as a repair of the existing first-host loop.
Famine and migration remain independent mechanics, categories, namespaces, and start-available mapmodes.

A current evacuation request can reveal the migration category only through the existing large, repeated, or sustained issue thresholds; a quiet food observation, a relief-only offer, or one tiny positive pending row cannot do so.
Distinct valid incoming evacuation generations may increment the existing migration incident count once per generation, without adding a public metric or an event-pacing entry.
The preparation phase uses the existing Open Emergency Reception and rejection controls; acceptance becomes available only after the exact operational contract passes.
The category retains Displacement Load, Reception Capacity, and Border Policy, at most six primary actions, and the existing three-mission limit.

Paid preparation retains its three spendable resources and existing population-scaled service shares.
One central cost table governs inclusive affordability and payment, with display-only quoted values projected by the existing bounded phase provider; cached display amounts never govern a debit.
Preparation must make a real service or policy improvement, and a rejected paid setup refunds every charged resource and restores only its own changed receipts.
No new event, GUI, category, mapmode, asset family, mission family, free native service, or numeric AI weight change is authorized by this clarification.
The owner must still obtain the frozen baseline, source patch, and same-scenario probability comparison and report missing native evidence explicitly.

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

Each category is hidden at game start and appears only for its own genuine problem: a famine-owned stage threshold for famine, and a large, repeated, trapped, corridor or reception issue for migration.
A country can receive accounting and presentation context and use valid owner-local actions before its category appears.

The emerging, active, resolution and dormant phases are presentation for the category header and the missions.
They lock no ordinary decision: every decision is shown by its own state, route and capacity conditions, so a departure policy can be reversed during a crisis and a country that both hosts arrivals and has its own displaced people can act on both.
The famine phase is refreshed from the famine country registry, independently of migration.
A category closes when no material issue remains and can reopen later with prior policy memory intact.

When active, a category shows its one primary and two supporting values, up to three urgent missions, and the decisions whose own conditions hold.

## Famine response decision family

Famine decisions belong to `famine_decision_category`; they do not require `migration_decision_category`.
The [decision map](famine_and_migration_system_decision_map.csv) is the canonical inventory; this section states each decision's role.

| Decision | Role | Effect and risk |
| --- | --- | --- |
| Release Food Stores | Ration and release a state's reserve | Immediate relief; the reserve is spent |
| Import Food | Arrange a foreign land donor and deliver in one paid action | Relief points over the delivery window; needs a valid donor and route, so a blockade can deny it |
| Restore Relief | Repair or secure the named route into a state | Restores relief access; creates a route mission when actual locations must be held |
| Escort Relief | Break an island or coastal blockade with an escorted convoy | Full, partial or lost delivery depending on hostile naval and air pressure |
| Airlift Relief | Deliver limited priority aid by air | Prevents a stage rise for a small or isolated state; never replaces a sea or rail route for a dense state |
| Requisition Food | Shift food from a safer neighbouring state | Relief for the target, pressure and grievance in the donor; abusive when the donor is occupied, persecuted or strained |
| Evacuate (famine) | Move a bounded cohort out of a famine state through Migration | Lowers need; requires a destination, and reception that is not already over capacity |
| Conceal Hunger | Hide one state's crisis from the public for 90 days | The state stops counting toward the national food crisis but its food shock rises by 10; the first famine deaths there are condemned as a cover-up |
| Continue Requisitions | Keep extracting from a hungry state | Adds 15 extraction pressure for war support and supply at the cost of deeper famine; available only where a real extraction policy exists |

Costs use the physical transport contract and preserved equipment requirements recorded in the [famine system document](../../systems/famine_system.md); political power is not charged.
Request Relief retains the separate foreign-donor invitation, while Import Food remains the delivery action.

### Invite international relief

Narrative role:

The government accepts foreign aid, observers, and logistical access.

Tradeoffs:

- lower mortality
- improved diplomacy
- reduced concealment
- possible exposure of camps, requisition, or corruption
- foreign influence or inspection pressure
Each decision checks the selected state.
Request Relief retains its historical reserve-first country role and waits until no reserve-release target remains.

## Migration origin decision family

| Decision | Role |
| --- | --- |
| Open Departure | Permit and support spontaneous flight; lowers trapped pressure with less control over destinations |
| Restrict Departure | Hold the population in place; preserves labor and secrecy, raises trapped pressure while danger remains |
| Request Passage | Ask an enemy, neutral, partner or neighbour for a humanitarian corridor; the counterpart answers with Accept or Refuse Passage, and rejecting a corridor it could have received is condemned through the famine owner |

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

Evacuation is blocked only when national reception is already over capacity.

## Migration destination decision family

| Decision | Role | Availability |
| --- | --- | --- |
| Open Emergency Reception | Admit arrivals and assign temporary shelter | Needs spare capacity |
| Screen Incoming Civilians | Controlled medical and security reception for exposed arrivals, without treating all migrants as diseased | Needs spare capacity |
| Distribute Arrivals | Move arrivals from an overloaded border or port state to safer states | Available to an overloaded host |
| Permit Transit | Allow passage to a confirmed onward destination | Available to an overloaded host |
| Close the Border | Refuse ordinary entry; explains reduced inflow and the risk of trapped people, irregular crossings and foreign pressure | Available to an overloaded host |
| Enforce the Closure | Commit units and authority to stop irregular crossings; can turn violent by policy | Available to an overloaded host |
| Local Integration | Settle a long-term hosted cohort as ordinary population | Available to an overloaded host |
| Resettle Abroad | Transfer part of a hosted population to an accepting third country | Available to an overloaded host |
| Help Families Return | Transport and aid for voluntary return to a safe origin | Available to an overloaded host |
| Force Repatriation | Send people back regardless of willingness; route deaths and condemnation when the origin is dangerous | Available to an overloaded host |

Actions that relieve a host stay available when it is overloaded; actions that admit more people need spare capacity.

## Source proposals outside the current inventory

The source design also described maritime evacuation, abandoning a state, prioritized entry for vulnerable groups or skilled co-nationals, and internment or labor reception.
None of them is in the current decision inventory, and no acceptance record makes them requirements.
Disposition: unresolved; any revival needs a distinct mechanical effect rather than a priced copy of an existing decision.

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
- import food when mortality and collapse risk exceed secrecy or ideological cost
- conceal or maintain extraction according to regime profile, war pressure, condemnation, and opposition risk
- stop a failed policy when evidence and mortality become severe unless the regime is deliberately exterminatory

### Origin AI

The AI should:

- evacuate from imminent front collapse, nuclear fallout, catastrophic famine, camps, or severe bombing
- prefer internal destinations when safe
- use allies, guarantees, neighbors, and historical ties for foreign destinations
- preserve transport for military survival
- evacuate first where mortality is immediate or people are trapped
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

- the category is hidden until the issue becomes sustained, and its phases never lock an ordinary decision
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

## C11 acceptance and implementation boundary

The owner’s 13 October restore request supersedes the merged-action restriction in `e40587520` and accepts recovery of the three evacuation lanes and separate relief invitation from `839850b0d^`.
Their recovered source wording is preserved above.
The current source implements their historical preparation, stock requirements, equipment fees and exact movement/relief contracts, plus the owner’s local-pressure and fuel/convoy rules.
The earlier demographic-priority and worker-recovery narratives did not have distinct cohort-selection or machinery-transfer code in that parent; no absent implementation is claimed to have been recovered.
Unimplemented maritime evacuation, abandonment, entry-priority and internment proposals remain unresolved outside C11.
