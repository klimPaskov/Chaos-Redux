# Event 20 Black Plague Specification, Part 2

## Shared disease crisis board, mapmode, containment, and recovery

All labels in this file are working labels, not final localisation.

## Design rule

The Black Plague does not receive a duplicate decision category. It registers as a disease inside the existing biological warfare and disease containment interface. Generic disease actions remain shared. The Black Plague also adds its own separate decision entries inside that general category when the selected disease and target state make them relevant. These include city rat clearing, food-store sealing, sewer and burrow clearance, shelter treatment, transport-hub vermin control, and harsh district demolition.

Shared and Black Plague-specific actions read the selected disease, selected country, selected state, local status, nearby exposure, cure progress, Rat Infestation, and current evolution stage. The category should feel like a changing crisis board. It must not show a permanent wall of every possible response. The visible action set changes as the country moves from Prepared to Threatened, Infected, Contained, Recovery, or Cured status.

## Interface layout

The existing disease interface should be expanded only as much as needed to make the Black Plague legible. The implementation agent should preserve the established visual structure when the live repository already has one.

### Global strain strip

The top strip shows the selected disease and world state.

- current Black Plague evolution
- total active infected states
- total contained states
- total countries with active infection
- event-attributed civilian deaths
- global countermeasure knowledge
- known weaponization status when publicly attributed
- world threat status

The strip should not reveal hidden weaponization projects, hidden incubation states, future Rat King conditions, or secret world-end thresholds.

### Country response strip

The selected country area shows:

- national preparedness
- national medical capacity
- national Black Plague countermeasure progress
- number of threatened, infected, contained, and recovering states
- border and port exposure summary
- current emergency burden
- current economic and military cost of active containment

Preparedness and medical capacity must have readable breakdown tooltips. The player should understand which laws, hospitals, decisions, war conditions, and infrastructure factors are changing the values.

### Selected state card

The selected state card shows the state name, owner or controller, and current status. It should display:

- disease load
- mortality pressure
- outgoing spread pressure
- containment
- treatment coverage
- relapse risk when relevant
- Rat Infestation when Black Plague is selected
- current death rate band
- strongest incoming exposure routes
- active local measures
- whether the state is under Rat Nation control
- whether the known outbreak has weaponized provenance

The death rate should use a descriptive band and projected range rather than claiming a precise number when daily script factors can change. A detailed tooltip can show the main positive and negative factors.

### State list

The country list should prioritize the most urgent current states.

1. Collapsed
2. Severe Crisis
3. Infected
4. Incubating when known to the owner
5. Threatened
6. Contained at relapse risk
7. Recovery
8. Cured states still under monitoring

The list needs filters by status, owner, region, and urgency. Human players should be able to select one state at a time. AI should evaluate every valid state without using the human selection flow.

### Disease switcher

If several diseases are active, the player can switch the selected disease. The Black Plague uses the shared board and does not replace other disease entries.

## Disease mapmode

The existing disease mapmode is the authoritative spatial view. It updates whenever a state changes disease status, containment status, cure status, weaponized provenance, or Rat Nation control.

### Visual state families

When Black Plague is the selected disease, every state with established Black Plague uses a black base fill instead of the normal generic disease colour. The base fill identifies the disease. Outlines, patterns, status icons, and tooltips identify the current phase.

| State status | Map direction | Purpose |
| --- | --- | --- |
| Clear | normal mapmode neutral | No active Black Plague state |
| Threatened | existing amber-brown warning tint | Exposure exists without established infection |
| Incubating, known to owner | dark charcoal to the authorized viewer | Early infection is known but not yet publicly established |
| Infected | black base fill with a thin infected outline or icon | Active recognized Black Plague |
| Severe Crisis | black base fill with a strong severe-crisis outline or pattern | High mortality and spread |
| Collapsed | black base fill with a broken crisis edge | Human containment has failed |
| Contained | black base fill with a blue containment outline | Disease remains but spread is suppressed |
| Recovery | black base fill with a green recovery outline | Disease load is declining but cleanup is incomplete |
| Cured and monitored | black fill removed, monitored status shown with the existing recovery colour | Active disease cleanup is complete |
| Weaponized provenance | black base fill with a purple weaponized border or symbol | Known deliberate deployment |
| Rat controlled | black base fill with a rat-control accent and status icon | Nonhuman control with active plague |

The Black Plague colour resolver takes priority over the normal disease fill only while Black Plague is selected. Other diseases keep their existing mapmode colours. Exact outline colours must match the live palette and remain readable for color-impaired players. Status icons and tooltips must carry the same information so black is not the only signal.

### Refresh contract

Every state transition calls one shared disease map refresh path. Infection effects, spread effects, containment decisions, cure milestones, rat occupation, rat annexation, and weapon deployment must not each maintain separate mapmode logic.

The mapmode refresh should update only affected states where the existing system permits it. A full world rebuild should be reserved for initialization, load repair, explicit global view reconstruction, or the triggerable scenario bootstrap after all multi-continent seed states have been registered.

## Black fog visual experiment

The user requested black fog over diseased states when possible. This is an optional engine-dependent visual enhancement, not a replacement for the mandatory mapmode.

The implementation team should run a narrow prototype against the live HOI4 interface and map object systems.

### Desired appearance

- low, dark particulate fog within the infected state area
- slow movement rather than a flashing pulse
- density tied to Infected, Severe Crisis, Collapsed, and Rat-Controlled status
- no screen-wide obstruction
- no interference with unit selection, borders, or map labels
- static disabled state when the disease is hidden or cured
- settings-aware performance option if the effect is expensive

### Asset expectation

A final animated fog package requires real source frames, a horizontal frame sheet, a static fallback, a preview GIF for review, a manifest, and verified game wiring. Transforming one still image with opacity or offset is not acceptable final art.

### Feasibility gate

If the engine cannot anchor an animated effect to dynamic state areas without global performance or map readability problems, the black fog item is marked `blocked by engine surface`. The implementation report must name the tested surface and result. The mapmode and crisis board remain mandatory and must still communicate every status.

## Country crisis phases

The country phase is derived from its states and nearby exposure. It controls which shared decisions appear.

### Prepared

The country has no current threatened or infected states and does not border an active infection. It sees low-clutter prevention actions.

### Exposed

The country borders an infected state, has a threatened port or troop route, or has a known infected trade or faction connection. It gains stronger border, transport, and medical buildup actions.

### Infected

At least one owned or controlled state is Incubating, Infected, Severe Crisis, or Collapsed. It gains state-targeted quarantine, treatment, cordon, and emergency actions.

### Containment

All active infections are Contained or Recovery and no uncontrolled source is present. The action set changes from emergency suppression to monitoring and controlled reopening.

### Recovered

The country has no active infection but retains monitored states and demographic scars. It sees rebuilding and optional permanent prevention actions.

A country can move backward when a new infection or relapse occurs.

## Prepared-state actions

Prepared actions are limited and strategic. They are not a checklist that every country can complete cheaply.

### Build sentinel surveillance

**Purpose**: increase the chance of seeing Incubating states before public recognition and identify incoming transport exposure.

**Costs and tradeoffs**:

- civilian factory burden
- support equipment and trucks for mobile teams
- small ongoing administrative cost
- possible stability loss in authoritarian crackdowns when surveillance is coercive

**Dynamic scaling**:

- more expensive for large countries and countries with many ports or border states
- cheaper when the country has strong medical technology, hospitals, or an existing disease program
- slower during war or severe supply disruption

**Result**:

- national preparedness increase
- earlier local reveal
- lower chance that a Threatened state jumps directly to public Infected status

### Stockpile medical and protective supplies

**Purpose**: create a reserve used by later hospital, quarantine, and treatment actions.

**Costs**:

- support equipment
- trucks
- civilian factory output
- consumer goods pressure when the reserve is large

**Result**:

- raises emergency medical reserve
- lowers activation cost for the first response in each state
- creates accident or theft risk only when the wider biowarfare system already models stockpile problems

### Inspect transport hubs

**Purpose**: reduce hidden exposure through rail hubs, ports, and major redeployment routes.

**Costs**:

- trains or rail throughput
- convoy or port throughput
- slower strategic redeployment
- administrative burden

**Result**:

- lowers transport spread pressure
- can reveal a Threatened or Incubating hub

### Strengthen disease prevention law

**Purpose**: establish a long-term national posture.

**Costs**:

- political and economic opportunity cost
- consumer goods burden
- possible war support loss from restrictions

**Result**:

- persistent preparedness increase
- lower origin and infection severity weight
- modifies future shared disease actions

The law should be part of the shared disease prevention framework and should protect against other compatible diseases. It is not a Black Plague-only law.

## Exposed-state actions

### Close a threatened border corridor

**Target**: one border region or exposed state group rather than every border at once.

**Purpose**: sharply reduce cross-border civilian spread.

**Costs**:

- trade reduction
- supply and reinforcement friction
- opinion loss with affected neighbors
- stability or war support cost depending political system
- increased resistance pressure when the corridor passes through occupied territory

**Result**:

- strong cross-border spread reduction
- little protection against domestic troop or rail movement unless paired with route restrictions

### Impose port inspections

**Target**: threatened coastal states or port groups.

**Costs**:

- convoy throughput
- dockyard or port capacity
- trade efficiency
- civilian factory burden

**Result**:

- reduces local port exposure before Evolution II
- strongly reduces overseas jump risk after Evolution II
- can reveal hidden infected cargo or troop return events

### Restrict troop routes

**Target**: threatened states crossed by active military movement.

**Costs**:

- command power at a conservative level
- planning and reinforcement penalties
- strategic redeployment restrictions
- possible local front weakness

**Result**:

- reduces military spread pressure
- creates a real choice during active war

### Pre-position field hospitals

**Target**: threatened state.

**Costs**:

- support equipment
- trucks
- civilian factory days
- supply consumption

**Result**:

- raises treatment coverage immediately if the state becomes infected
- shortens the delay before emergency hospitals are effective

### Suspend civilian travel

**Target**: exposed region or selected threatened states.

**Costs**:

- construction and factory output loss
- stability pressure
- lower local supply movement

**Result**:

- strong reduction to civilian movement spread
- reduced effectiveness against army and occupation routes

## Infected-state actions

The interface should show only the actions relevant to the selected state and country capacity. Expensive actions can be mutually limiting through a national emergency burden cap.

### Declare state quarantine

**Requirements**:

- selected state is Incubating, Infected, Severe Crisis, or Collapsed
- country can reach the state administratively
- no existing quarantine of equal or stronger level

**Costs**:

- local factory, construction, and supply penalties
- stability and compliance pressure
- consumer goods burden
- possible relations damage when foreign nationals are trapped

**Effects**:

- major reduction to outgoing civilian spread
- moderate increase to containment
- treatment becomes more effective if relief access remains open
- disease load can worsen if quarantine is imposed without supplies

This action must not be an unconditional good button. A poorly supplied quarantine can trap people with the disease and increase mortality.

### Deploy an army cordon

**Requirements**:

- divisions present in or adjacent to the state
- sufficient equipment and supply
- state not already under a stronger cordon

**Costs**:

- tied-down divisions
- infantry and support equipment attrition
- command power
- local resistance and compliance damage
- front readiness loss

**Effects**:

- strongest immediate containment increase
- reduces border and troop-route spread
- can prevent a Severe Crisis state from becoming Collapsed
- can create a military infection incident if divisions lack protection

The cordon must use real unit presence or a clear unit commitment abstraction. It should not be bought only with political power.

### Construct emergency hospitals

**Requirements**:

- selected state is reachable by supply
- sufficient civilian industry, trucks, and medical reserve

**Costs**:

- civilian factory burden for a meaningful duration
- trucks and support equipment
- local supply draw

**Effects**:

- large treatment coverage increase
- strong mortality reduction after a buildup delay
- accelerates national countermeasure progress through case data
- vulnerable to state collapse, bombing, and loss of control

### Open a relief corridor

**Purpose**: maintain food, medicine, and evacuation access through a quarantine.

**Costs**:

- convoys or trains depending geography
- escorting divisions or air cover
- intelligence exposure
- chance of creating an outgoing spread route if inspections fail

**Effects**:

- lowers quarantine mortality
- protects treatment coverage
- can raise spread pressure if underfunded or sabotaged

### Organize burial and sanitation crews

**Purpose**: lower disease load and prevent secondary collapse.

**Costs**:

- manpower commitment without granting combat units
- trucks, trains, and support equipment
- stability and war support strain
- increased worker infection risk without protection

**Effects**:

- disease load reduction
- lower mortality acceleration
- lower relapse risk later
- additional cure progress from organized reporting

The final text direction should treat mass death with severity and avoid jokes.

### Run vector and shelter control

This remains a generic shared disease action. When Black Plague is selected, the category also exposes the more specific actions below. The specific actions are separate decision entries, not hidden aliases of one generic button.

**Purpose**: target local shelters, bedding, flea pressure, and temporary housing conditions that sustain the outbreak.

**Costs**:

- civilian factory output
- local construction delay
- support equipment, medical reserve, and transport

**Effects**:

- lowers local spread, mortality pressure, and Rat Infestation
- stronger in dense civilian states, camps, ports, and refugee receiving areas
- less effective after state collapse unless paired with a cordon

## Black Plague-specific urban and rat-control decisions

These decisions appear only inside the general disease category while Black Plague is selected. They supplement shared quarantine, hospitals, relief, and treatment. They never create a dedicated Black Plague category.

### Clean the City of Rats

**Target**: an urban, port, or densely populated Black Plague state with meaningful Rat Infestation and human control.

**Costs**:

- manpower committed to sanitation and trapping teams
- support equipment, trucks, and medical reserve
- civilian factory days
- local stability or resistance pressure

**Effects**:

- large Rat Infestation reduction
- lower local spread and mortality pressure
- lower Evolution III basin pressure
- improved effectiveness of burial, sanitation, and treatment actions

**Failure and tradeoff**:

A rushed campaign without sealed transport, shelter treatment, or food-store control can scatter infected rats into nearby states. Partial success lowers the local value but creates temporary exposure along rail, road, or refugee routes. The action is repeatable only through a cooldown and rising local cost until infestation falls below the visible threshold.

### Seal Granaries, Markets, and Warehouses

**Target**: an infected or threatened state with food storage, trade, port, rail, or major urban value.

**Costs**:

- consumer goods and local food-distribution pressure
- civilian factory and inspection burden
- reduced port, rail, or market throughput
- possible stability loss from shortages

**Effects**:

- slows Rat Infestation growth
- reduces cargo, rail, and port transmission
- protects medical and relief stores from contamination
- weakens future Dock Brood and Urban Warren emergence pressure

### Clear Sewers and Burrow Shafts

**Target**: an urban, port, rail, liberated rat, or high-infestation state.

**Requirements**:

- engineers or equivalent construction capacity
- human control of the target
- adequate protection for work teams

**Costs**:

- support equipment, construction capacity, and time
- damage to local infrastructure and movement
- worker casualty risk

**Effects**:

- reduces Rat Infestation sharply
- removes hidden burrow contribution when present
- lowers Rat Nation resurgence risk after liberation
- improves the long-term result of city rat clearing

### Flea, Shelter, and Bedding Control

**Target**: an Infected, Severe Crisis, Contained, or Recovery state.

**Costs**:

- medical reserve and civilian production
- transport and temporary housing capacity
- emergency burden

**Effects**:

- immediate mortality reduction
- lower household and shelter transmission
- improved treatment coverage
- lower relapse risk during Recovery

### Purge Vermin from Rail Yards and Docks

**Target**: a Black Plague state with a port, rail hub, supply hub, or major transport route.

**Costs**:

- trains, convoys, port throughput, fuel, and inspection manpower
- temporary reinforcement and supply delays

**Effects**:

- lower local Rat Infestation
- lower internal transport and Evolution II spread
- reduced chance of rat stowaway jumps
- stronger protection for returning troops and relief shipments

### Demolish Infested Blocks

This is an emergency overreaction option for an urban Severe Crisis or Collapsed state. It is intentionally powerful and damaging.

**Costs**:

- major construction loss and civilian factory burden
- forced displacement
- stability, compliance, and resistance damage
- large emergency burden

**Effects**:

- sharp reduction to Rat Infestation and local Disease Load
- destruction of hidden nest and shelter sources
- reduced Rat Nation emergence pressure in the target state

**Failure and tradeoff**:

Without a cordon and screened receiving states, demolition can push displaced civilians and vermin into surrounding states. The decision can save a city medically while destroying its economy and political order.

### Distribute treatment reserves

**Purpose**: use stored medicine and medical capacity to reduce deaths immediately.

**Costs**:

- consumes national medical reserve
- civilian factory replenishment burden
- can deprive another infected state if reserves are limited

**Effects**:

- immediate treatment coverage increase
- reduced mortality pressure
- effect strength scales with national countermeasure progress

### Seal transport and troop access

**Purpose**: combine civilian and military movement restrictions for a critical state.

**Costs**:

- severe supply, rail, reinforcement, and industry damage
- tied transport capacity
- war support and stability loss

**Effects**:

- strongest outgoing spread reduction short of complete loss of control
- high risk of humanitarian failure without a relief corridor

### Evacuate a threatened perimeter

This is available only before full state collapse and only when the country has safe receiving states.

**Costs**:

- trains, trucks, and convoys
- temporary population and factory disruption in receiving states
- refugee exposure risk
- resistance and stability pressure

**Effects**:

- reduces the population exposed to the worst future mortality
- can move infection to receiving states if surveillance and transport inspections are weak

This decision should be risky and should not create population from nowhere.

## Contained-state actions

### Maintain containment

Continues the cordon and treatment package. It costs industry, supply, and units but keeps relapse risk low.

### Begin controlled reopening

Releases some economic penalties and unit commitments. It raises relapse risk for a period. Cure progress and monitoring determine whether the reopening succeeds.

### Trace residual clusters

Consumes medical reserve and civilian capacity to lower hidden disease load. It is most valuable when the state is near Recovery.

### Rotate exhausted personnel

Reduces hospital and cordon fatigue at a manpower, transport, and training cost. It prevents long containment from losing effectiveness automatically.

## Recovery and Cured-state actions

### Restore local administration

Rebuilds state capacity, compliance control, construction efficiency, and resistance management. It does not restore population directly.

### Rebuild hospitals and transport

Repairs medical capacity, infrastructure, rail connections, and local supply. The player chooses whether to prioritize disease resilience or economic reopening.

### Support surviving households

Improves population growth recovery, stability, and local production over time. It uses civilian industry and consumer goods.

### Preserve sentinel surveillance

Converts emergency measures into a lower-cost permanent prevention bonus. It protects against relapse and other compatible diseases.

### Remove emergency restrictions

Ends remaining containment penalties when the state is Cured. Removing them too early is unavailable rather than merely risky.

## National emergency burden

The player should not activate every harsh response everywhere without limit. A national emergency burden value measures the total economic and military strain of active containment.

### Sources

- quarantined population
- number and severity of active cordons
- divisions tied to containment
- hospital construction and operation
- closed border corridors
- inspected ports
- restricted troop routes
- relief corridors
- national medical reserve consumption

### Consequences

Low burden is manageable. High burden increases consumer goods, production disruption, stability loss, supply penalties, and decision costs. Extreme burden can cause compliance problems, illegal movement, local protest, and policy failure events.

A large rich country can sustain more burden than a small poor one. The cap should scale with industry, state count, stability, and medical capacity. It should still be possible for a major power to overreact.

## Dynamic preparedness

Preparedness is a national value shown in the disease interface. It is not a universal shield.

### Increases from

- prevention laws
- surveillance
- medical reserve
- hospitals
- transport inspection programs
- recent successful disease response
- shared research and foreign aid

### Decreases from

- active war
- low stability
- occupied territory
- supply collapse
- repeated epidemic fatigue
- deliberate underfunding
- lab accidents and coverups

Preparedness reduces the probability and opening strength of infection. It also increases the chance of recognizing Incubating states. It should not make a country immune.

## Local medical capacity

Medical capacity is evaluated nationally and locally. A strong national system can still fail in an isolated, occupied, or blockaded state.

Local capacity depends on:

- infrastructure and supply access
- hospital projects
- state control and resistance
- available medical reserve
- nearby safe states
- bombing and front conditions
- cure progress
- foreign relief access

The interface should explain why a hospital program is not reaching the population when a state is encircled or collapsed.

## International assistance

Countries can aid an infected ally, faction member, neighbor, subject, or recognized crisis partner through shared disease actions.

### Aid forms

- medical equipment shipment
- field hospital mission
- convoy or rail relief corridor
- scientist exchange
- quarantine advisors
- evacuation transport

### Costs and risks

- equipment, trucks, trains, convoys, and civilian industry
- intelligence exposure
- domestic infection risk
- foreign influence or relations consequences
- aid diversion or capture in collapsed states

Aid should improve treatment or countermeasure progress. It should not instantly cure a state.

## Human counter-rat actions after Evolution III

Once Rat Nations appear, the shared disease board gains a narrow set of military anti-rat and post-liberation response actions. They appear as separate Black Plague decision entries inside the same general disease category. These remain part of the same crisis system because retaking rat territory does not remove the disease or Rat Infestation.

### Fortify the cordon line

Requires divisions, forts or engineering capacity, supply, and equipment. It slows rat expansion from infected states.

### Purge the warrens and seal the burrow network

Targets a liberated, threatened, or heavily infested state. It uses engineers, support equipment, construction capacity, sanitation teams, and military protection to remove nests, lower Rat Infestation, reduce rat spawn, stop tunnel movement, and prevent resurgence.

### Armored clearance operation

Requires armored or motorized strength and adequate supply. It is effective against rat swarms but can spread disease through returning units if decontamination is weak.

### Air and reconnaissance sweep

Uses air capacity and fuel to reveal rat concentrations and reduce surprise attacks. It does not cure the disease.

### Liberate and quarantine

Applies immediate quarantine and medical relief when a rat-controlled state is retaken. Without this action, the state remains a dangerous spread source and can produce a resurgence.

### International extermination coordination

Available when the shared world-threat flag is active. It supports intelligence, aid, and synchronized operations without creating a new faction automatically.

## Cleanup and category lifecycle

The shared category must remove or convert obsolete actions.

- Prepared actions are hidden while emergency actions are active when they would duplicate stronger versions.
- Threatened actions disappear when the exposure route is gone.
- Infected actions disappear when no selected state qualifies.
- Containment actions replace emergency actions after all infection is suppressed.
- Recovery actions disappear when cleanup completes.
- Anti-rat actions disappear when no rat country or eligible resurgence basin remains.
- Weaponization actions stay in the existing biowarfare project and delivery surfaces, not in the containment list.

The category remains available as a prevention surface after eradication only when the country has chosen a continuing prevention law or has another active disease.

## AI equivalence

Every button available to a human player needs an AI path that does not depend on selected-state GUI interaction. AI scoring is specified in Part 8 and the AI matrix. The key rule is that AI chooses a response package based on disease severity, capacity, war pressure, state value, and neighbor exposure instead of clicking every action.

## Acceptance criteria for the crisis board

The crisis board is complete only when:

- Event 20 appears inside the shared disease interface
- the state list updates on every status transition
- established Black Plague states use a black base colour in the existing mapmode and the state card shows the same status
- known Incubating states are visible only to authorized countries
- Prepared, Exposed, Infected, Containment, and Recovery action sets change dynamically
- Black Plague-specific city, rat, sewer, shelter, warehouse, transport, and liberation decisions appear inside the shared category
- no dedicated Black Plague category is created
- costs use real resources and strategic sacrifices
- quarantine without relief can increase mortality
- cordons require unit or military commitment
- cure progress reduces mortality and spread without instant cleanup
- rat occupation preserves the plague state
- liberated rat states require cleanup
- AI has equivalent actions
- obsolete actions and targets are cleaned up
- black fog feasibility is tested and reported separately from mandatory mapmode behavior
