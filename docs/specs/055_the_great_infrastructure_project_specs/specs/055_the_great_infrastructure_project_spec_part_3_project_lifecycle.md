# Event 55 Specification, Part 3

## Project Lifecycle and Management

## Lifecycle overview

Every authorized project follows a staged lifecycle. The stages turn the project into a long commitment and create points where geography, diplomacy, equipment, war, and prior choices matter.

The normal lifecycle is:

1. Authorization
2. Survey and charter
3. Right of way and partner agreement
4. Procurement and mobilization
5. Main construction
6. Commissioning
7. Operation and maintenance
8. Damage, repair, rerouting, or closure when required

A domestic project can skip most foreign negotiation. A multinational corridor can spend much longer in the agreement stage. A fixed link needs a stronger survey and safety stage. A wartime emergency route can shorten early stages by accepting greater risk.

The project should not create one decision for every small construction action. Each stage should contain one main objective and only the interventions that change its outcome.

## Authorization

Authorization converts one stable proposal into an active project.

The player chooses the construction method and accepts the first cost package. The project records its route, family, scale, partners, expected duration, and critical nodes.

Authorization should require:

- a free project slot
- the required National Works Capacity stage
- control or lawful access to the route's initial critical states
- no unresolved duplicate project
- the first phase cost package
- a valid project owner

The project should not consume all equipment and industrial burden at once. Costs are divided across stages so later war, embargo, or partner changes can alter the commitment.

A project can use more than four cost types over its full lifetime. A single decision or action can use no more than four spendable cost types.

## Cost model

Costs should match the project family and stage.

Common spendable costs include:

- political power for charters, land rights, treaties, and ministry coordination
- trains for railway work and route operation
- trucks for highways, remote construction, and repair crews
- convoys for ports, island links, maritime surveys, and imported materials
- support equipment for surveying, communications, field workshops, and safety systems
- fuel for heavy construction and emergency acceleration
- command power only for projects under active military administration
- stability or war support as a visible consequence of forced schedules, displacement, or failed prestige promises

Civilian factory commitment should usually appear through a timed construction burden or consumer-goods effect. It should not be represented as a tiny political power fee.

Steel and other industrial resources do not exist as normal stockpiles. Their role should be modeled through resource access requirements, import arrangements, partner contributions, and timed industrial diversion. The event should not pretend to remove a steel stockpile that the game does not track.

## Scale bands and normal duration

Suggested total duration bands before method, capacity, terrain, evolution, and incident changes:

| Project family | Typical total duration |
| --- | --- |
| Strategic highway | `240` to `540` days |
| Resource corridor | `300` to `600` days |
| National railway | `360` to `720` days |
| Grand port | `360` to `720` days |
| International corridor | `540` to `1080` days |
| Great bridge or tunnel | `600` to `1080` days |
| Evolution III continental network | `900` to `1440` days |

A short local grand work can fall below these ranges. An extreme terrain or multi-country project can exceed them when the player is warned before authorization.

The player should see a duration band before choosing. Once the survey stage finishes, the project can reveal a more precise expected completion date.

## Survey and charter stage

The first active mission establishes the route in detail.

This stage can require:

- holding the origin and destination states
- maintaining access to the route
- a small support equipment or truck commitment
- a political charter
- a survey period based on route length and terrain

The survey can discover:

- a shorter route
- severe geology
- an unexpected river or marsh crossing
- a better port site
- a politically sensitive settlement
- a valuable resource spur
- a weak bridge approach
- an unsafe tunnel alignment

A discovery should alter the same project rather than replace it with an unrelated random event.

Survey outcomes include:

- approved alignment
- improved alignment with lower duration or cost
- difficult alignment with higher risk
- route redesign choice
- reduced-scope recommendation
- cancellation before major procurement

Early cancellation should recover most equipment because the main works have not begun. Political power and survey effort remain spent.

## Right of way

Domestic projects may need state control and a public land policy choice. International projects need explicit foreign consent.

Possible domestic right-of-way approaches include:

### Negotiated acquisition

Longer preparation, lower political damage, and lower sabotage risk.

### Emergency public works authority

Faster access, higher stability or resistance risk, and stronger local opposition incidents.

### Military route designation

Available only when the route has a real wartime purpose. It can use command power and complete quickly, but its peacetime economic payoff is weaker until converted later.

These approaches are working design roles. Final names and text belong to implementation.

The event should not create a detailed landowner simulation. The choice exists to shape risk and timing.

## Partner agreement stage

An international project starts a bounded negotiation with every required partner.

Partners can:

- accept the proposal
- accept with a requested contribution change
- offer transit rights without full investment
- delay while demanding better terms
- refuse

The host can:

- accept a counteroffer
- increase its own share
- seek a substitute partner
- reroute around the refusing country
- reduce project scope
- abandon the proposal

Negotiation should have a deadline. A project cannot occupy a slot indefinitely while one partner remains undecided.

Partner contributions can include:

- civilian construction burden
- trains
- trucks
- convoys
- resource access
- border and customs cooperation
- route security

No partner action should display more than four spendable cost types.

## Procurement and mobilization

This stage commits the main equipment and industrial burden.

The exact package depends on project family:

- railways emphasize trains, support equipment, and industrial burden
- highways emphasize trucks, fuel, and industrial burden
- ports emphasize convoys, support equipment, and coastal construction burden
- tunnels and bridges emphasize support equipment, fuel, imported resource access, and long civilian burden
- resource corridors emphasize trains or trucks, resource access, and local industrial construction

The procurement mission can fail or slow when:

- stockpiles fall below the promised reserve
- an embargo blocks imports
- war consumes the assigned trains, trucks, convoys, or fuel
- a partner misses its contribution
- industrial bombing damages the host's capacity

The player can accept delay, buy emergency imports where allowed, reduce scope, or divert national resources at a wider cost.

## Main construction mission

The main mission is the central project timer.

It should show:

- the project route or facility
- the current construction stage
- the expected deadline
- the main requirement currently at risk
- the consequence of success
- the consequence of failure or suspension

The mission should not require the player to click a second completion button after satisfying its conditions. It should complete automatically when the timer and conditions are met.

Construction progress can accelerate from:

- high National Works Capacity
- the accelerated method
- later evolutions
- strong partner contributions
- a successful survey
- secure route control
- relevant completed projects

Progress can slow from:

- difficult terrain
- war damage
- missing equipment
- embargo
- partner disputes
- sabotage
- local resistance
- cost overrun incidents
- route redesign

The implementation can model progress through mission duration changes, staged missions, or hidden progress values. The player should experience one clear active objective rather than several overlapping timers for the same project.

## Milestone incidents

A project can receive a limited number of incidents at meaningful construction milestones.

The normal incident budget should be small:

- one possible incident during survey
- one possible incident during procurement
- one or two possible incidents during main construction
- one commissioning issue for difficult or rushed projects

A long continental network can support more incidents, but repeated events should use cooldowns and avoid text spam.

Incident families include:

### Engineering discovery

A better alignment, unexpected rock, groundwater, unstable soil, severe climate, or a hidden river channel changes cost and time.

### Material shortage

The project lacks trains, trucks, support equipment, convoys, fuel, or industrial inputs. The player can delay, import, reduce scope, or divert resources.

### Contractor failure

Corruption, false reporting, weak workmanship, or a failed subcontractor threatens the schedule. The response can favor speed, investigation, or replacement.

### Labor and local conflict

Working conditions, forced acquisition, wage disputes, displacement, or military control create local tension. The player can negotiate, repress, redesign, or compensate.

### Sabotage and intelligence concern

A hostile country, resistance network, criminal group, or rival contractor damages work. The response can use security, repair, or diplomatic pressure.

### Natural disruption

Flood, storm, landslide, earthquake, wildfire, ash, or severe winter damages the route. A real Event 13 disaster should take priority when one already affects the states.

### Breakthrough

A successful engineering method, local initiative, volunteer contribution, or partner delivery reduces time or improves the final project.

Each incident should change an existing stage, risk, cost, relationship, or route. Avoid incidents that only give a tiny modifier.

## Cost overruns

Cost overruns are a project state, not a random punishment with no warning.

Risk rises from:

- accelerated construction
- long routes
- extreme terrain
- weak National Works Capacity
- corruption outcomes
- partner delay
- embargo
- active war
- repeated redesign

Risk falls from:

- conservative engineering
- successful surveys
- strong project institutions
- experienced completion history
- stable partner contributions
- later engineering evolutions

When an overrun occurs, the player can:

- approve additional burden and preserve full scope
- extend the schedule
- reduce the route or facility scope
- seek partner finance
- suspend construction

A single overrun should not always force abandonment. Repeated overruns can create an overextended works condition that lowers National Works Capacity until the project is resolved.

## Partial and reduced completion

A project can finish at reduced scope when the player chooses a controlled compromise.

Examples include:

- a railway ends at an intermediate industrial node
- a highway stops before the most difficult terrain
- a port opens with fewer advanced facilities
- a multinational corridor loses one outer partner but retains the core route
- a bridge project becomes a rail and ferry terminal rather than a fixed link only when the final player-facing promise is rewritten before authorization

The last example is allowed only as an explicit redesign choice. The game must never silently replace a promised land connection with a modifier.

Reduced completion should preserve an option to extend the project later when conditions improve.

## Suspension

A project enters suspension when construction cannot continue but physical work remains.

Suspension can result from:

- loss of a critical state
- partner withdrawal
- economic collapse
- prolonged shortage
- major disaster damage
- failed cost overrun response
- host capitulation

A suspended project consumes less active burden than a live construction mission, but it still lowers National Works Capacity and occupies a project slot until formally mothballed, transferred, redesigned, or abandoned.

The player should see the reason for suspension and the actions that can resolve it.

## Abandonment and salvage

Abandonment ends the project and clears its active slot.

Salvage depends on stage:

| Stage | Normal salvage direction |
| --- | --- |
| Survey | Most unspent equipment returns. Political and survey costs remain spent. |
| Procurement | Part of stored trains, trucks, convoys, and support equipment returns. |
| Main construction | Limited equipment returns. Most industrial effort is sunk. |
| Commissioning | Very little direct salvage. Partial works may remain as a weaker local modifier. |

Abandonment can reduce trust with foreign partners and create a cooldown before the same route is proposed again.

The event should not grant more equipment through salvage than the project consumed.

## Commissioning

The commissioning stage checks whether the completed work can operate.

It verifies:

- control of critical states
- required partner agreements
- railway, port, crossing, or route consumers
- minimum equipment and convoy support
- no unresolved severe construction defect

A conservative project should be more likely to open directly as Operational. An accelerated project can open as Strained and need a follow-up maintenance action.

Commissioning can create a local or international news report when the project is historically large, spans several countries, or completes an Evolution III network. Most projects need only a national report event and event log update.

## Operation

An operational project gives its full mapped benefits.

Operation should depend on the physical and political route. The project checks its critical nodes through sparse event-owned updates and direct integration callbacks.

A project can become Strained when equipment, fuel, convoys, or maintenance are weak. It can become Partially Disrupted when one noncritical segment is lost. It becomes Severed when a critical state, crossing, port, or agreement is unavailable.

The project should recover automatically when the cause is simple and fully restored, such as a temporarily missing train reserve. Serious physical damage should require repair.

## Maintenance

Maintenance should exist as a persistent obligation without turning the category into constant clicking.

Normal maintenance is abstracted through the completed project's operational checks and small ongoing national burden.

A maintenance decision appears only when:

- the project is Strained for a sustained period
- a critical segment is damaged
- a partner has stopped contributing
- an extreme engineering project reaches a scheduled overhaul point

Maintenance actions can use trains, trucks, support equipment, convoys, fuel, and civilian burden according to the project.

Routine projects should not demand a manual payment every month.

## Repair

Repair is a timed mission with a clear target and cost.

A repair can cover:

- damaged route states
- a damaged port node
- a bridge or tunnel approach
- bombed railway levels
- disaster damage
- sabotage damage
- a failed safety system

The repair mission should name the affected states or facility. It should restore only the Event 55 project and the ordinary buildings that the repair package explicitly covers.

A project that is physically intact but diplomatically dormant needs renegotiation, not a repair mission.

## Rerouting

A reroute is available when a route has lost a segment but another connected path can reach the same strategic purpose.

Rerouting should:

- generate one or two replacement alignments
- preserve the original project identity and completion history
- require a new survey and limited construction
- reduce or suspend benefits until the new segment opens
- update partner shares and route states

Rerouting should not become a cheap way to claim a second completed project for achievements.

## Transfer of ownership

When the host is annexed, released, or transformed, the project needs a safe ownership decision.

A domestic project can transfer to the controller of its critical route when that controller uses normal civilian systems and accepts the project. Otherwise it becomes Dormant.

An international project can appoint a new host from surviving partners. Partner approval, route access, and project generation identity must remain intact.

A transfer should never duplicate permanent benefits or leave the old owner with an active category and project record.

## Project experience

Completed projects improve the country's ability to manage later works.

This experience can:

- raise National Works Capacity within a cap
- reduce survey time
- reduce overrun risk
- improve maintenance
- unlock difficult candidates after the relevant evolution

Experience should come from completed and sustained projects, not from repeatedly authorizing and abandoning work.

## Lifecycle acceptance criteria

The lifecycle is complete when every project can:

- move from proposal to authorization
- select a construction method
- pass through relevant survey, agreement, procurement, construction, and commissioning stages
- display one clear active mission at a time
- suffer bounded incidents that alter the project
- finish at full or reduced scope
- suspend without corrupting the category
- be abandoned with stage-based salvage
- operate only while its route or facility remains valid
- become strained, disrupted, severed, dormant, repaired, rerouted, or transferred
- clean up its active costs, flags, targets, and partner records exactly once
