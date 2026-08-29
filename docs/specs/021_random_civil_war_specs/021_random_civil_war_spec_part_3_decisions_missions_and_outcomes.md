# Decisions, Missions, Settlements, and Outcomes

## Decision-system role

Event 021 should give the affected country an active crisis to manage. A single civil-war command is insufficient.

The normal presentation uses one event-owned decision category per active country. The category changes phase and content according to the country's role.

Possible phases:

1. Opening scramble
2. Active war
3. Multi-front war
4. Settlement
5. Reconstruction
6. Neighbor exposure
7. Evolution III prevention

The player should normally see three to five primary decisions and one to three active missions. Six primary actions is the hard ceiling for one phase. Obsolete, invalid, completed, or irrelevant actions disappear.

## Category presentation

The category uses:

- a normal category icon
- one static category picture
- current State Authority stage
- one concise current objective
- active-front name when more than one front exists
- one short summary of the strongest visible pressure
- up to three active missions
- phase-appropriate decisions
- concise tooltips for nonstandard costs and requirements

A multi-front crisis can use the standard selected-target decision pattern. The human player selects one front, sees actions for that front, and can close the selection. AI evaluates every valid front without requiring the player-facing selection step.

The category should not become a custom mechanic window, tab system, map board, or text wall.

## Cost model

Important actions use concrete resources and commitments that fit the public act.

Possible cost types:

- infantry equipment
- support equipment
- artillery
- trucks
- trains
- convoys
- aircraft
- fuel
- manpower
- army XP
- navy XP
- air XP
- command power
- political power for genuinely political acts
- stability
- war support
- civilian factory burden
- military factory output
- tied-down divisions
- control of named states, depots, ports, or rail junctions
- time
- State Authority
- local support
- foreign influence or dependency

A single decision has no more than four spendable cost types.

Requirements such as controlling a state, fielding divisions, maintaining supply, or holding a route do not count as spendable costs.

Political power or command power alone should not be the default cost for military, logistical, regional, or diplomatic action.

## Original-government action families

### Secure the arsenals

Role:

- deny equipment to an emerging side
- protect the government's first reinforcement cycle
- raise State Authority when successful
- reduce the force share of a front still in preparation

Typical requirements and costs:

- support equipment
- infantry equipment
- command power or army XP
- supplied units near selected depots
- short mission or preparation period

Possible risk:

- moving equipment can expose another region
- an aggressive seizure can lower local support
- failure can arm the opposition

### Establish a capital defense command

Role:

- create a coherent capital defense area
- integrate nearby formations
- protect the government from immediate collapse
- improve reinforcement and command around the capital

The action should require actual units, equipment, and supply. It should not spawn free divisions without an institutional source.

### Restore the rail spine

Role:

- reconnect capital, depots, supply hubs, and isolated regions
- create named repair or protection objectives
- reduce War-Torn Administration
- improve the next mobilization or settlement mission

Costs can include trains, trucks, fuel, civilian factory burden, and unit commitment.

### Conduct a bounded loyalty review

Role:

- identify suspect commands
- reduce the next defection risk
- improve force integration
- reveal one public risk region

The action must have a real downside. A broad purge can reduce officer quality, lower State Authority, increase recurrence, or drive an additional front.

### Integrate loyal formations

Role:

- consolidate units that remain with the government
- repair template and equipment gaps
- reduce command penalties
- prepare a counteroffensive

Requirements should depend on current manpower, equipment, training time, and safe territory.

### Negotiate a regional guarantee

Role:

- reduce one secession or independence front
- offer autonomy, revenue, legal protection, local administration, or language and cultural guarantees where the package supports them
- change the opening strength or settlement range

The action should not erase all Event 021 pressure. It affects one actor or one region.

### Offer a limited amnesty

Role:

- split moderates from hardliners
- create a surrender route
- reduce recurrence
- open prisoner exchange or local ceasefire events

Failure can strengthen hardliners or reduce credibility.

### Call an emergency coalition

Role:

- bring a legal opposition bloc into the government
- raise State Authority
- change ruling-party support
- block an ideological front or make it smaller

The action can restrict later political choices, empower an internal rival, or create a negotiated postwar structure.

### Emergency requisition

Role:

- obtain short-term equipment, fuel, trains, or supply from controlled territory
- improve one urgent mission
- create an economic and legitimacy cost afterward

It should be a deliberate temporary gamble, not a repeatable free stockpile source.

## Opposition and independence action families

### Seize a local depot

Role:

- capture equipment tied to actual territory
- improve a weak opening force
- create a time-limited objective
- damage the opponent's next reinforcement cycle

Success depends on controlling or reaching the named depot region.

### Organize regional recruitment

Role:

- raise militia, guards, or package-specific units
- consume manpower, equipment, time, and local support
- use a force cap
- worsen supply or administration when overused

The unit family must fit the actor. Event 006 packages use their own reinforcement content.

### Integrate defecting officers

Role:

- improve command and templates
- transfer or recruit valid officers
- reduce Fractured Command
- risk internal faction conflict when the officers have a distinct political agenda

No character can exist in two live rosters.

### Establish field administration

Role:

- raise State Authority for the claimant
- improve production and supply in controlled territory
- prepare recognition or settlement
- reduce the chance that local control collapses after victory

The action requires control of a capital, administrative center, or coherent regional base.

### Open a foreign liaison

Role:

- create one sponsor channel
- request equipment, training, recognition, intelligence, or logistics
- create foreign influence and dependency
- expose the side to rival intervention

A side should not maintain unlimited sponsor channels.

### Request recognition

Role:

- seek international or regional recognition
- change settlement options
- unlock recognition missions
- create diplomatic cost for the sponsor

Recognition should depend on territory, administration, survival time, ideology, relations, and foreign interests.

### Coordinate with another opposition front

Role:

- create a temporary nonaggression pact
- coordinate a capital assault
- share a rail route
- divide settlement claims
- form a coalition government plan

The agreement needs a public scope, duration, and failure rule.

### Reject the rival claim

Role:

- preserve ideological or territorial independence
- prepare rebel-on-rebel conflict
- raise internal cohesion for one side
- reduce the chance of a joint settlement

It should never be the dominant AI choice without strategic reason.

## Mission families

### Hold the capital

Typical duration:

- 120 to 180 days

Success:

- raises State Authority
- improves recognition
- unlocks stronger administration and recruitment
- may shorten the war by breaking an enemy claim

Failure:

- lowers State Authority sharply
- can transfer legitimate succession
- can create a new capital or settlement route

### Secure the rail junctions

The mission names specific states, rail hubs, or supply routes.

Success:

- improves supply
- reduces War-Torn Administration
- protects reinforcement
- weakens the selected front

Failure:

- creates isolation
- increases equipment loss
- can make an additional front viable

### Protect the depot belt

The mission requires supplied divisions in named states and control of selected depots.

Success preserves stockpiles and reinforcement.

Failure lets the opponent seize a bounded equipment package based on the actual depots and opening plan.

### Keep the corridor open

The mission can protect:

- land supply
- foreign aid
- a port
- an evacuation route
- a humanitarian corridor
- a rail connection

Success and failure must depend on actual map control.

### Complete local mobilization

The side must field, train, equip, or position a defined force before a deadline.

Success creates or upgrades a route-specific force package.

Failure can consume part of the equipment, lower local support, or leave an understrength formation.

### Deny recognition

A government or rival front tries to stop another side from reaching a public diplomatic threshold.

Success restricts sponsors and settlement options.

Failure improves the claimant's recognition and can trigger foreign pressure.

### Preserve the civilian route

A side protects transport, food, medical access, or evacuation through named territory.

Success reduces administrative damage and postwar reconstruction.

Failure raises War-Torn Administration and local resistance. It should not create cheap comedy or treat civilians as a military resource.

## Success, failure, and partial success

Important missions need distinct outcomes.

Examples:

- the capital is held, but the rail link is lost
- the depot is secured, but local support falls after harsh requisition
- the corridor remains open, but foreign dependency rises
- a regional charter prevents independence, but grants permanent autonomy
- the rebellion is disarmed, but its legal movement survives
- a front is defeated, but its rival inherits its territory and fighters

Partial success should preserve meaningful consequences. It should not be a renamed full victory.

## Multi-front selection

When Evolution I creates several sides:

- every front receives a stable front identity
- the category shows one selected front at a time
- decisions and missions clearly name the selected front
- settlement can target one front without erasing others
- defeating one front updates the selected-front list
- stale or dead targets clear immediately
- a victorious rebel government inherits unresolved fronts
- AI evaluates every front and chooses priorities based on strength, geography, ideology, objectives, and settlement potential

The UI should not expose raw arrays or front IDs.

## Settlement families

### Government military victory

The government annexes or disarms the defeated side.

The player chooses a postwar direction:

- reintegration and amnesty
- limited trials and institutional reform
- harsh security settlement
- regional autonomy
- negotiated local administration
- continued emergency rule

The choice affects Unsettled Settlement, State Authority, recurrence, local support, diplomacy, and future actor eligibility.

### Opposition military victory

The winner becomes the successor government when it claims the whole country.

The transition must update:

- national leadership
- ruling party
- legal and ideological identity
- remaining fronts
- faction and subject relations
- advisors and commanders
- focus access
- country name and flag when an approved existing route requires it
- Event 021 generation and settlement memory

The winner does not receive instant peace with all other fronts.

### Recognized independence

An Event 006 package or complete regional package survives as a separate country.

The outcome defines:

- accepted border or disputed border
- recognition
- former-host claims
- access to Event 006 decisions and formables
- postwar demobilization
- foreign guarantees or dependency
- subject or fully sovereign status
- a reconstruction and integration period

### Negotiated autonomy

The movement remains inside the host with a public autonomy settlement.

The settlement can create:

- subject status
- local administration
- revenue or resource rights
- regional recruitment rules
- protected institutions
- future federation route
- recurrence if the host violates the terms

The autonomous region must use a real country or subject route only when the engine and package support it. Otherwise, the settlement stays inside the host through ideas, decisions, and state modifiers.

### Coalition or constitutional settlement

Rival governments agree to share, sequence, or contest power through a political process.

Possible structures:

- interim coalition
- restored parliament
- constitutional convention
- military withdrawal schedule
- election after demobilization
- council with regional representation
- temporary joint command

The route should create a visible postwar political state and real obligations.

### Armistice and temporary partition

The sides stop fighting without resolving sovereignty.

The armistice needs:

- a defined border
- ceasefire duration
- supply and access rules
- recognition state
- renewal or breakdown conditions
- settlement conference
- foreign sponsor limits
- recurrence risk

It must not leave two permanent generic actors with no future content.

### Merger

A temporary regional movement can merge into:

- a complete related Event 006 package
- another surviving country
- an autonomous federation
- the parent country after negotiated reintegration

The merger needs clear territorial, leadership, force, and identity handling.

## Postwar settlement memory

The winning or surviving country receives `Unsettled Settlement`.

Working variants:

- negotiated settlement
- integrated settlement
- harsh settlement
- revolutionary settlement
- partitioned settlement
- independence accepted
- independence reconquest
- foreign-dependent settlement

The postwar state changes through:

- disarmament
- trials
- amnesty
- local elections
- constitutional reform
- reconstruction
- veteran integration
- sponsor withdrawal
- border settlement
- renewed repression
- violation of autonomy terms

A durable peace should be achievable. The event should not punish every victory with another war.

## Recurrence

A second Event 021 crisis becomes possible only after:

- country cooldown ends
- successor grace ends
- actor and map viability return
- no incompatible crisis is active
- unresolved settlement or new pressure exists
- global active-front capacity allows it
- normal event or Evolution III timing selects the country

Normal recurrence timing direction:

- earliest warnings can appear after roughly 45 days
- ordinary recurrence MTTH begins around 60 to 180 days only in high-risk conditions
- low risk can delay recurrence beyond a year or remove it
- negotiated settlement and successful integration strongly suppress it
- harsh settlement, partition, surviving armed groups, foreign sponsorship, and low State Authority raise it
- a manual scenario can force immediate nested crises through its own rules

Exact timing belongs to constants and probability validation.

## Cleanup

Every resolved crisis must clean:

- active front arrays
- selected-front target
- front reservations
- actor creation locks
- temporary decisions
- missions
- event targets
- temporary flags
- scenario bypass
- aid routes
- sponsor records
- foreign volunteers created by the event
- ceasefire or nonaggression records
- temporary subject or faction routing
- equipment liabilities
- unit locks
- temporary capital targets
- evolution preparation
- neighbor exposure that no longer has a live source
- world-threat source when Evolution III no longer sustains it
- dynamic modifiers that have no postwar role
- temporary actor slots after annexation or merger

Cleanup must preserve:

- Event 006 country identity
- legitimate surviving countries
- permanent settlement consequences
- achievements already earned
- event history and evolution logs
- documented origin
- recurrence memory
- valid postwar claims, cores, and relations
