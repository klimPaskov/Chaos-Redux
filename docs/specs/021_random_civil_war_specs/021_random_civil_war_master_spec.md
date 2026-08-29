# Event 021 Random Civil War Master Specification

This convenience copy compiles the ten numbered source-spec parts in reading order.

The numbered files remain the source-of-truth units for review and implementation. When this compiled file and a numbered part differ, the numbered part controls.


---

<!-- Source: 021_random_civil_war_spec_part_1_core.md -->


# Event 021 Random Civil War

## Catalog identity

- Event ID: `21`
- Working name: `Random Civil War`
- Canonical entry event: `chaosx.nr21.1`
- Type: `Minor Repeatable`
- Status before implementation: `Unavailable`
- Event chaos level: `1`, Calm World
- Cluster: `1`, Wars
- Cluster severity: `Medium`

## Event promise

A country fractures according to conditions that already exist inside it.

A stable country should face a limited revolt, a failed coup, or one compact breakaway. A country weakened by occupation, war exhaustion, divided politics, regional exclusion, damaged administration, or uncertain military loyalty can lose larger regions and more forces. Later evolutions add rival camps, full independence movements, foreign sponsors, political exposure in nearby countries, nested crises, and a global climate in which every normal human country must manage internal risk.

The event is repeatable because different countries and different political structures should produce different wars. Repeatability must spread varied crises around the world. It must not trap one country in continuous civil war.

## Framework ownership

Event 021 owns:

- dynamic domestic-fracture target selection
- ordinary ideological uprisings
- rival legal governments
- broad command schisms that are not centered on one named commander
- regional secessions
- insertion of complete human Event 006 independence packages
- multi-front civil-war registration
- active-war escalation from Event 021 evolutions
- neighboring political exposure
- foreign support, containment, and mediation around Event 021 wars
- successor and recurrence memory
- the global fracture evolution
- the manual global fracture scenario
- reusable civil-war planning and cleanup helpers that specialized events may later call through explicit contracts

Event 021 does not absorb the unique identity of specialized events.

It must remain distinct from:

- Event 005 Soviet Union Collapse
- Event 006 Independence Wave
- Event 095 Occupation Revolt
- Event 117 Five-Way Civil War
- Event 127 Warlords
- Event 131 Widespread Mutiny
- Event 134 Duchies
- Event 142 Partisans
- Event 144 Freedom or Death
- Event 019 Soldiers from Nowhere and its formation revolts

Those events keep their own triggers, actors, presentation, progression, and outcomes. Shared helpers are allowed only after an explicit integration pass.

## Event family

The final event chain should contain separate families for these roles:

| Family | Design role |
| --- | --- |
| Dispatcher | Select a valid country, calculate hidden Fracture Pressure, select an archetype, plan the opening, and prepare log context |
| Affected-country opening | Present the visible rupture and activate the correct category phase |
| Opposition opening | Establish each claimant's public goal, capital, force base, and first objective |
| Additional-front incidents | Create or reveal Evolution I fronts without erasing current sides |
| Neighbor incidents | Open Evolution II exposure, support, containment, and mediation |
| Strange incidents | Deliver rare uncertain practices with bounded material consequences |
| Settlement events | Resolve surrender, autonomy, coalition, partition, recognition, merger, and demobilization |
| Victory and succession | Transfer legitimate government, preserve unresolved fronts, apply settlement memory, and start reconstruction |
| Evolution III incidents | Maintain global risk bands, critical-country queues, nested crises, and world reactions |
| Scenario wrapper | Launch the manual global fracture setup with selected type and intensity |
| Debug entry points | Offer bounded development triggers that never become ordinary player content |

The final numbering belongs to implementation. The structure must keep state, actor, and cleanup ownership clear.

## Availability

Event 021 is eligible from Calm World.

A normal automatic firing requires at least one valid target and at least one valid opposition route. When no valid target exists:

- the event has no live selection weight
- the Events list displays `N/A`
- the automatic picker does not queue it
- normal manual triggering explains that no valid country can currently fracture
- force-trigger testing may bypass ordinary target preference but may not create an invalid actor, broken map, duplicate country, or unsafe terminal conflict

The event remains disabled by default while its catalog status is unreworked or unavailable. It enters the reworked-event default allowlist only after the complete package is implemented.

## Universal exclusions

A country is excluded when any of these conditions apply:

- it is classified by the shared `is_actual_nonhuman_country` trigger
- it is in a terminal state incompatible with normal event play
- it has no valid split, claimant, or same-tag takeover route
- it is inside a short creation, annexation, cleanup, or succession lock
- it is already in an incompatible bespoke civil-war chain
- a safe capital, force package, or parent remnant cannot be created
- every possible independence package is incomplete, blocked, duplicated, or territorially invalid
- its only possible territory is controlled by unrelated third parties and belongs to another event's uprising logic
- the active-front or actor-capacity gate cannot admit another crisis

The broader `is_special_chaos_country` trigger must not be used as blanket immunity. Human Event 006 countries, restored states, unusual human governments, subjects, and human chaos-created countries remain eligible after their grace periods.

## Repeat behavior

After a firing:

- the event uses the standard repeatable weight and cap system
- the affected country receives a country-specific cooldown
- Event 021 can still target other countries
- active Event 021 wars can evolve
- the former target cannot return until both cooldown and successor grace have expired
- recurrence weight depends on the settlement, surviving armed networks, remaining divisions, territorial disputes, State Authority, and later chaos
- a rapid victory does not itself justify an immediate second crisis

A country that reaches a durable settlement and rebuilds authority should become a poor target for a long period. A harsh or incomplete settlement can leave recurrence risk, but the recurrence must still pass normal timing and validity.

## Evolution structure

| Stage | Chaos requirement | Main change |
| --- | ---: | --- |
| Baseline | Calm World | One primary opponent with severity based on country conditions |
| Evolution I | Gathering Storm | Multiple fronts, low-weight major targeting, and regular use of full independence packages |
| Evolution II | Rising Chaos | Regional political exposure, foreign sponsorship, stronger sides, and rare strange incidents |
| Evolution III | Chaos Tier | Persistent global fracture risk, bounded critical-country processing, nested crises, and systemic world reactions |
| Higher chaos | Totalen Chaos and World Collapse | Faster and broader Evolution III behavior within tested performance caps |

Each evolution has two entry routes.

### Active-war evolution

A live Event 021 crisis can change after an evolution becomes available. The transition uses the shared MTTH evolution process and records one evolution entry. It must not happen instantly without a scenario or other accepted immediate route.

### Prefire evolved opening

When an evolution is already active before Event 021 fires, the opening uses the evolved rules immediately. This is not a second event identity and does not require the country to pass through a weaker opening first.

## Nonterminal rule

Evolution III creates a persistent world threat and may register an Event 021 source with the shared world-threat aggregate. It does not set `world_end`, freeze normal events, or resolve the campaign into a terminal state.

The Event 021 threat source should exist only while the global fracture evolution is active and capable of creating or sustaining Event 021 crises. Cleanup must clear the source and refresh the aggregate when the evolution is disabled or no longer active.

## Public information boundary

The player should understand:

- the country's current State Authority stage
- the visible causes of the crisis
- which regions, capitals, commands, depots, railways, or ports matter
- what each public claimant wants
- which action spends which resources
- the objectives and deadlines of active missions
- the broad settlement being offered
- why a new front has appeared
- why a nearby war creates domestic pressure
- why a postwar state remains unsettled

The player should not see:

- raw target scores
- hidden Fracture Pressure formulas
- secret future package candidates
- exact strange-incident chances
- hidden sponsor plans
- actor-pool slots
- implementation flags
- future achievements
- unconfirmed supernatural explanations
- technical cleanup or performance state

## Completion boundary

A single working civil-war popup is not completion.

The event is complete only when the full baseline, three evolutions, decisions, missions, AI, Event 006 integration, cluster behavior, scenario, assets, achievements, event logs, Event Details, documentation, cleanup, probability checks, performance checks, and acceptance scenarios are finished without hidden fallback.


---

<!-- Source: 021_random_civil_war_spec_part_2_targeting_and_baseline.md -->


# Targeting and Baseline Opening

## Hidden Fracture Pressure

Event 021 uses a hidden country-level score called `Fracture Pressure`.

It measures how easy it is for a viable organized opponent to turn domestic conflict into armed conflict. It should never be reduced to stability alone, ideology popularity alone, or a random equal chance for every country.

Fracture Pressure is recalculated when:

- Event 021 builds its automatic target pool
- a country enters the Evolution III review queue
- a major preventive action succeeds or fails
- a relevant territory, capital, depot, or rail condition changes
- a war ends
- a settlement is signed
- an active Event 021 crisis reaches a bounded review point
- a country is created, transformed, annexed, or released
- a nearby Event 021 war begins or ends during Evolution II or III

It does not require an unrestricted daily scan of every country.

## Pressure components

| Component | Conditions that raise pressure | Conditions that lower pressure |
| --- | --- | --- |
| Political stability | low stability, rapid government change, failed coup, collapsing coalition, severe legitimacy loss | high stability, a durable coalition, trusted institutions, recent constitutional settlement |
| War exhaustion | long external war, low war support during war, heavy casualties, convoy loss, lost cores, repeated strategic defeat | recent peace, successful defense, restored manpower, functioning demobilization |
| Political competition | one strong excluded opposition, several organized rival blocs, rapid ideology swing, banned movement with real support | broad governing coalition, opposition integrated into legal politics, low organized support |
| Political exclusion | removal of a large regional or ideological bloc from power, destroyed autonomy, dissolved institutions, recent loss of representation | negotiated access, local institutions, power-sharing, recognized autonomy |
| Territorial control | occupied home states, high resistance, isolated regions, lost rail links, disconnected administration | secure cores, connected administration, viable local government, restored communications |
| Military loyalty | officer purges, divided commands, unpaid or undersupplied formations, encircled military districts, politically split units | integrated command, supplied armies, trusted officers, successful loyalty objectives |
| State capacity | weak infrastructure, noncontiguous territory, no dependable route to the periphery, broken civil service | functioning rail and supply, administrative reach, protected arsenals, responsive regional services |
| Regional identity | complete Event 006 package, historic regional institutions, coherent territorial claim, autonomy movement | accepted local settlement, integrated institutions, no safe package or region |
| Country scale | many states, many military districts, several viable capitals, several distinct regions | microstate or one-state structure, which routes to a limited takeover |
| Nearby conflict | active Event 021 front across a border, related armed network, arms route, returning cadres, competing sponsors | controlled border routes, successful mediation, demobilized neighboring movements |
| Event memory | harsh settlement, unresolved partition, surviving front, old arms stock, exiled claimant, prior recurrence | long peace, reintegration, disarmament, trusted guarantees |
| Other Chaos Redux systems | documented command fracture, liberation pressure, occupation strain, mutiny history, active human crisis actor nearby | successful containment or resolved shared condition |
| Chaos state | access to later evolutions, wider global fracture climate | Calm World and no nearby or historic crisis |

The model must distinguish political diversity from organized conflict. Ethnic, regional, ideological, religious, or class diversity by itself adds no pressure. A group matters only when it has a plausible political grievance or goal, organizational capacity, leadership, territorial or institutional access, and a valid actor package.

## Target weighting

The automatic picker builds a weighted pool of valid countries.

Weight should reflect:

- Fracture Pressure
- opening viability
- availability of at least one distinct actor
- country-specific cooldown
- recent regional variety
- recent archetype variety
- whether a major is currently allowed
- whether the player country is valid
- global active-front capacity
- current scenario or cluster reservations
- country generation and successor grace
- whether Event 006 offers a complete relevant package

The highest pressure country should not always be selected. The pool needs enough randomness to create campaign variety, but pressure ordering must remain visible in probability tests.

A stable country can remain in the pool at low weight. If selected, it receives a smaller opening.

A player country uses the same rules. It should not be protected merely because it is human, and it should not receive an artificial weight boost merely because it is human.

## Baseline target policy

Before Evolution I:

- minor countries are the normal target pool
- majors are excluded from ordinary automatic selection
- countries already fighting a serious external war remain eligible when war exhaustion is a meaningful cause and the opening remains playable
- countries with one state or unsafe island geography use a same-tag takeover route
- subjects can be targeted when their domestic politics and overlord relationship support a valid crisis
- ordinary human Event 006 countries are eligible after their creation grace period
- a country already in a compatible small domestic crisis can receive an Event 021 escalation only through an explicit adapter, not through a second blind firing

## Opening severity

After target selection, Event 021 derives an opening severity from Fracture Pressure, country scale, territory viability, military loyalty, actor capacity, and current war context.

| Severity | Typical conditions | Opening direction |
| --- | --- | --- |
| Limited | stable government, compact opposition, intact command, weak regional organization | small region or failed-coup theater, modest defections, short crisis pressure |
| Serious | visible political division, local organization, some military doubt, viable regional base | one connected opposition region, usable capital, regular force package, active crisis decisions |
| Severe | low stability, long war, occupied cores, strong exclusion, divided command | large viable region, meaningful force share, depot and rail pressure, foreign attention |
| Critical | major structural failure, several organized blocs, broad command collapse, high chaos | one powerful baseline opponent, or an immediate Evolution I multi-front opening when that evolution is active |

Baseline normally creates one primary opponent. A critical baseline target receives a strong opponent, not several weak actors. Multiple fronts belong to Evolution I.

## Baseline archetypes

The dispatcher selects one valid archetype after it has chosen the country and severity.

### Ideological uprising

An organized non-ruling ideology challenges the government.

Preferred conditions:

- meaningful ideology popularity
- legal exclusion or recent repression
- coherent regional or urban base
- available political leadership
- compatible military or militia support

The actor should have a distinct public program. It must not exist only to switch the ruling ideology.

Possible goals:

- replace the national government
- establish a revolutionary government
- restore a constitutional order
- overthrow a dictatorship
- defend a threatened ruling coalition from a rival takeover
- create a temporary coalition and call elections after victory

### Rival legal government

A second government claims constitutional, dynastic, parliamentary, judicial, military, or electoral legitimacy.

Preferred conditions:

- disputed succession
- failed government transition
- dissolved parliament
- competing constitutional authority
- exile or regional government that remains inside home territory
- leadership split inside the ruling bloc

This route uses the same national identity unless a verified cosmetic route is required. It should feel different from a generic ideological revolt because its claim is about legal continuity and institutions.

### Regional secession

A coherent region demands autonomy, federation, or independence.

Preferred conditions:

- connected territory
- valid regional capital
- political institutions or organized movement
- historical, cultural, legal, economic, or administrative identity
- defensible leadership
- no complete Event 006 package that should own the identity instead

A temporary regional actor cannot remain indefinitely with a vague generic identity. It needs a defined postwar disposition, such as autonomy, merger, reintegration, promotion into a complete package, or rejection before permanent independence.

### Event 006 independence actor

A complete human Event 006 package rises inside the selected country.

Preferred conditions:

- Event 006 registry contains a valid package
- package territory is compatible with the current host
- tag is free or safely reusable
- leader, flags, focus tree, forces, AI, decisions, and assets are complete
- no protected collision prevents a viable homeland
- the package remains human

The Event 006 contract is defined in Part 7.

### Broad command schism

Military districts, command staffs, arsenals, or formations break from the government without the event being centered on one named warlord.

Preferred conditions:

- low military loyalty
- large army
- officer purges or command rivalry
- isolated formations
- vulnerable arsenals
- severe war exhaustion
- weak civilian authority

Its public goal can be emergency rule, restoration of order, replacement of civilian leadership, defense of an old constitution, or a temporary military council.

This route must remain distinct from Event 127 Warlords and Event 131 Widespread Mutiny.

### Same-tag takeover

A one-state country, very small island country, or unsafe map structure cannot support a normal territorial split.

The event instead creates:

- a public loyalty contest
- armed cells or mutinous units
- a timed control mission
- foreign sponsor pressure
- a possible leader, ruling-party, law, subject, or ideology change
- a failed-coup or successful-takeover outcome
- limited casualties and disruption appropriate to the scale

It must not create a second invalid tag, zero-state actor, or impossible capital.

## Leader and identity resolution

Every opposition route must resolve leadership before the map changes.

Preferred order:

1. a valid existing character whose ownership and role permit transfer
2. an existing institutional council or legal body with appropriate identity
3. a valid Event 006 leader from the complete package
4. an established engine generic civil-war route that does not require a new custom portrait, after local precedent is verified
5. another archetype or another target

A grounded polity must not receive an invented face. A real character must not be cloned across live countries. A blocked leader blocks that actor unless another defensible leadership route exists.

Ordinary claimants should reuse the parent country's flag or a verified existing civil-war variant. Event 021 does not authorize a library of generic generated flags.

## Territory planning

The framework plans every territorial change before it commits ownership or control.

A planned opposition region should:

- be connected where geography permits
- contain a viable capital or emergency capital
- contain enough population and industry to sustain the assigned role
- have a usable route to supply
- avoid isolated single-province fragments
- avoid taking unrelated third-party occupied territory
- respect Event 006 package state maps and collision rules
- leave the parent country a viable remnant
- preserve at least one parent capital route
- avoid immediate automatic capitulation unless the selected outcome is a same-tag takeover
- prefer coherent administrative, military, regional, rail, or geographic groupings
- reserve every selected state before another front can claim it

The allocator should plan the full opening in one transaction. It should not transfer states one at a time while later choices depend on the already changed map.

## Parent remnant protection

The original government must retain enough territory to remain playable.

Protection should consider:

- at least one state
- capital or safe replacement capital
- minimum industrial and population base
- supply route
- access to a port when the remaining geography requires it
- a meaningful force package
- no instant trapped capital
- no complete loss of every core state through a random roll

A scenario or severe evolved opening can create a desperate remnant, but the result must still be a real belligerent.

## Force allocation

The event must not blindly split half the army.

Force allocation should consider:

- current unit location
- controlling region
- commander and officer ties
- ideology or claimant affinity
- command district
- supply status
- encirclement
- naval base or airbase control
- depot access
- severity
- state population and local support
- existing Event 006 force profile
- current external war
- minimum viable parent and opposition force

The opening may transfer or create:

- local militia
- defecting regulars
- border guards
- capital defense units
- railway guards
- port guards
- mountain detachments
- cavalry
- sailors
- foreign-trained cadres
- package-specific Event 006 formations

A force package needs enough equipment and manpower to function. It should also carry realistic weaknesses, such as poor training, low supply, limited support equipment, officer shortages, or dependence on one depot.

## Stockpile, air, and naval allocation

Stockpiles follow territory, units, arsenals, depots, and severity.

The opposition should not receive a fixed percentage of all equipment without context. It should receive enough basic equipment to operate, then depend on captured depots, local production, foreign aid, and reinforcement decisions.

Air and naval assets should split only when:

- the actor controls relevant airfields, ports, or commands
- the engine route is safe
- the transfer produces useful gameplay
- the parent retains a viable force
- the identity of the actor supports those assets

A landlocked regional uprising should not receive a decorative navy. An island command schism can receive ships when it controls their base and command.

## Opening State Authority

`State Authority` is the one main visible crisis value.

Range:

- `70-100`: Cohesive
- `40-69`: Contested
- `15-39`: Failing
- `0-14`: Collapse

These are working stage labels.

State Authority represents:

- administrative reach
- command obedience
- control of railways and depots
- cooperation of local officials
- ability to deliver orders and supply
- credibility of the current or successor government

It changes through:

- capital control
- mission results
- rail and depot control
- supplied formations in named regions
- negotiations
- repression
- civilian administration
- foreign intervention
- settlement terms
- victory
- loss of key territory

High authority improves containment and reduces additional-front pressure. Low authority worsens supply, mission difficulty, defection, recurrence, and the chance of active-war Evolution I escalation.

Fracture Pressure remains hidden. The player sees the causes that they can act on through concise tooltips and decisions, not the raw target formula.

## Baseline crisis ideas

Event 021 should have no more than three event-owned national spirits active on one country.

| Working idea | Role | Lifecycle |
| --- | --- | --- |
| Fractured Command | military coordination, loyalty, command, and reinforcement strain | worsens when fronts multiply, improves through integration, removed or replaced after settlement |
| War-Torn Administration | production, civil service, transport, and reconstruction pressure | changes with territory and mission outcomes, replaced by reconstruction or removed after full recovery |
| Unsettled Settlement | postwar recurrence, legitimacy, disarmament, and constitutional memory | appears only after the war, changes by settlement type, eventually removed through durable peace |

Short side effects should use timed or dynamic modifiers. The design should not create a separate national spirit for every action, sponsor, front, or battlefield incident.

## Baseline outcomes

A baseline crisis can end through:

- government military victory
- opposition military victory and national succession
- recognized independence
- negotiated autonomy
- coalition or constitutional settlement
- armistice and temporary partition
- merger into a complete related Event 006 package
- escalation into Evolution I when a new front becomes viable

The outcome system is detailed in Part 3.


---

<!-- Source: 021_random_civil_war_spec_part_3_decisions_missions_and_outcomes.md -->


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


---

<!-- Source: 021_random_civil_war_spec_part_4_evolution_i.md -->


# Evolution I: Multi-Front Civil Wars

`Multi-Front Civil Wars` is a working label, not final localisation.

## Role

Evolution I turns one internal rupture into a conflict between several incompatible political projects.

The normal viable large-country structure has at least three total belligerents:

- the original government
- one ordinary political or command opponent
- one additional rival, often an independence movement, regional secession, or competing ideology

The evolution also allows major countries to enter normal automatic selection at reduced weight.

A small country can remain two-sided when a third actor cannot receive viable territory, capital, forces, and objectives. The event must never create a broken third side merely to meet a numeric rule.

## Availability and pacing

- Chaos requirement: Gathering Storm
- Active-war transition uses the shared evolution MTTH process
- Base timing direction: roughly 60 to 120 days
- Timing becomes shorter when the war lasts, State Authority falls, several valid regions remain, the country is large, foreign support rises, or the current conflict reaches stalemate
- Timing becomes longer when one side is near defeat, the map cannot sustain another actor, settlement is progressing, or active-front capacity is tight
- Prefire evolved openings use the multi-front rules immediately
- Event 021 records one Evolution I log entry
- One active crisis cannot record the same evolution twice

## Active-war transition

When Evolution I becomes available during a baseline Event 021 war, the framework reviews the theater.

The review asks:

- Is there a coherent unassigned region?
- Is there a complete Event 006 package?
- Does another strong ideological or legal claimant exist?
- Has a military district remained outside both current commands?
- Is one front fragmenting into rival projects?
- Can every actor receive a viable capital, territory, force, and objective?
- Will another side produce distinct gameplay?
- Can the active-front and tag capacity support it?
- Does a developing settlement leave room for a separate claimant?
- Would a new side duplicate another event?

If a valid side exists, the event starts a preparation period or opens the front directly according to the current crisis.

If no valid side exists, the evolution can still unlock stronger front management, major targeting for future fires, and prevention actions. It should not create a fake actor.

## Prefire multi-front opening

When Event 021 fires after Evolution I is active:

- the allocator plans all regions before ownership changes
- the archetype pool selects distinct goals
- the government receives one coherent remnant
- every side receives a viable capital and force package
- side relationships are planned before war declaration
- Event 006 packages use their registered territory and identity rules
- major-country safety gates apply
- one-state and unsafe island countries still use a same-tag takeover
- a small country can receive one opponent when that is the only valid plan

## Side-count model

Side count should depend on:

- number of states
- number of coherent regions
- population
- industry
- military districts
- number of viable leaders and institutions
- number of valid Event 006 packages
- Fracture Pressure
- State Authority
- external war
- current active fronts
- performance caps
- tag capacity
- chaos tier
- scenario intensity

Design direction:

| Country profile | Normal evolved result |
| --- | --- |
| Small and coherent | two belligerents |
| Medium with two distinct regions or blocs | three belligerents |
| Large with several viable actors | three or four belligerents |
| Major with many regions and severe pressure | three to five belligerents within tested caps |
| Manual Maximum scenario | strongest sustainable plan under the scenario's global front cap |

A side that cannot fight, negotiate, or survive should not be created.

## Actor composition

Good combinations include:

- government, ideological opposition, independence movement
- government, rival legal government, regional secession
- government, left opposition, right opposition
- government, command schism, independence movement
- government, Event 006 actor, rival Event 006 actor
- government, ideological opposition, rival legal claimant
- successor government, old-regime restoration, nested independence movement

Weak combinations include:

- two identical ideological rebels with the same goal
- several small generic rebels with no territory
- a named warlord route that belongs to Event 127
- a mass mutiny route that belongs to Event 131
- an occupation uprising that belongs to Event 095
- an unresearched national identity
- two fronts that share the same leader or tag
- a regional actor with no permanent disposition

## Major-country targeting

Majors enter normal automatic selection only after Evolution I.

Rules:

- majors receive a lower base weight than comparable minors
- the target needs at least two viable opposition actors
- the country must pass stricter region, force, AI, and performance gates
- an incompatible bespoke civil war blocks selection
- an external war does not automatically block selection when war exhaustion is a cause
- the plan must preserve a viable government remnant
- the event must avoid instant capitulation from random state allocation
- a player major uses the same safety rules
- country size must not make the same major dominate repeated target selection
- a major with no distinct actors remains invalid

Probability tests must show that unstable minors still dominate ordinary selection while unstable majors become possible.

## Independence fronts

Evolution I makes complete Event 006 packages a regular front type.

### Candidate order

1. Complete registered Event 006 packages with valid territory, leader, focus, forces, AI, and assets
2. Existing vanilla countries that Event 006 already supports and that can be reused safely
3. Researched regional packages whose accepted route begins with limited civil-war territory
4. Unusual grounded packages already accepted by Event 006
5. Incomplete, blocked, duplicate, nonhuman, or unresearched packages are excluded

### Civil-war opening package

An Event 006 actor created through Event 021 receives an Event 021 civil-war opening profile.

Opening strength depends on:

- Event 021 severity
- Event 006 package profile
- controlled states
- local population
- host army presence
- depots and arsenals
- terrain
- ports
- foreign support
- independent Event 006 evolution state
- current world chaos

After stabilization, the country uses its normal Event 006 reinforcement and focus routes.

## Prevention before an independence front

When a valid independence actor is preparing, the host can receive a small set of preventive actions.

Possible actions:

- negotiate an autonomy charter
- appoint a regional cabinet
- restore local civil administration
- transfer equipment to loyal regional guards
- reinforce regional rail and supply
- offer revenue sharing or investment
- rotate suspect commanders
- recognize local legal or cultural rights
- arrest organizers through a high-risk crackdown

An action can:

- delay the front
- reduce its opening territory
- reduce its force share
- improve a future settlement
- turn independence into autonomy
- split moderates from hardliners
- prevent that specific package

It should not guarantee that the whole Event 021 crisis disappears.

Heavy repression can suppress one front while lowering State Authority, raising resistance, damaging diplomacy, and increasing recurrence.

## Multi-front territory plan

All front regions are selected in one planning pass.

The plan should:

1. reserve the parent remnant
2. reserve mandatory Event 006 anchor states
3. build coherent candidate regions
4. assign viable capitals
5. prevent state collisions
6. ensure supply and access
7. assign local industry and population
8. check third-party control
9. check protected states
10. assign front objectives
11. calculate force shares
12. commit only after the full plan passes

A failed plan must roll back every reservation. It must not leave transferred states, duplicate capitals, or orphaned actors.

## Front objectives

Every side should have a distinct goal.

Possible goals:

- take the national capital
- hold a regional capital and gain recognition
- restore an old constitutional government
- replace the current ruling ideology
- secure autonomy
- defend a federation
- seize the army command
- unite several regional movements
- destroy a rival claimant
- preserve an armistice line
- merge into a related country
- complete an Event 006 formation route

The objective affects AI, settlement, missions, diplomacy, and victory.

## Relations among opposition sides

Opposition sides do not need to be natural allies.

Possible opening relations:

- temporary nonaggression while both fight the government
- active three-way war
- shared capital offensive
- disputed territory with delayed conflict
- recognition pact
- coalition government agreement
- ideological hostility
- sponsor-backed rivalry
- independence actors that ignore each other until borders meet
- a legal claimant that recognizes autonomy but rejects independence

Relationships should depend on ideology, territory, public goals, sponsors, history, and current balance.

## Separate front resolution

One front can settle or be defeated without ending the whole crisis.

When one front exits:

- its states transfer according to the outcome
- its units disarm, integrate, retreat, merge, or remain under a surviving actor
- its equipment is accounted for
- its sponsor record closes or transfers
- its claims are resolved or inherited
- selected-front lists update
- other fronts recalculate objectives and settlement
- a victorious rebel government becomes the new parent-side government when appropriate
- the war continues against unresolved fronts

A front's defeat must never annex unrelated sides.

## Rebel-on-rebel escalation

Rival opposition sides can fight each other when:

- they claim the same territory
- they have incompatible national programs
- one attacks a neutral corridor
- a sponsor pushes escalation
- a coalition breaks
- one side captures the old capital
- one rejects an accepted settlement

The event should not force every rival to fight immediately. Some conflicts should begin with strategic cooperation or armed neutrality.

## Front strength and adaptation

A side becomes stronger through:

- captured depots
- controlled population and industry
- recruitment
- integrated officers
- foreign support
- held objectives
- Event 006 focus progress
- recognition
- surviving long enough to establish administration

Strength should not come from a flat random buff unrelated to play.

## Evolution I decisions

Additional actions can include:

- select the priority front
- offer a separate peace
- coordinate two fronts
- deny transit to a rival
- recognize one claimant
- trade territory for neutrality
- integrate a defeated side's units
- create a joint capital assault
- negotiate a regional congress
- threaten a crackdown before the front opens

The visible category remains phased and front-specific.

## Evolution I AI

### Government AI

The government should:

- protect the capital
- identify the most dangerous front
- avoid fighting every front equally
- seek separate peace where useful
- avoid concessions that guarantee total collapse
- use autonomy when an independence actor is too strong to defeat
- prevent a new front when the cost is acceptable
- consider the external war

### Opposition AI

Each side should:

- pursue its own objective
- secure supply
- preserve a viable capital
- decide whether to cooperate
- reject settlements that destroy its public claim
- avoid suicidal expansion against every rival
- seek recognition when survival depends on it

### Event 006 AI

An Event 006 actor uses the Event 021 opening AI until it stabilizes, then resumes its package-specific Event 006 strategy while remaining aware of the former-host war and other fronts.

## Evolution I acceptance

Evolution I is accepted only when:

- active and prefire entry paths work
- major-country targeting is rare but real
- every extra side has a distinct goal
- the map is planned before commitment
- the parent remains viable
- force allocation follows the planned regions and command conditions
- Event 006 packages are reused safely
- one front can settle or die independently
- rebel victory preserves unresolved wars
- front selection does not become stale
- side AI behaves differently
- no specialized event is duplicated
- global front and performance caps are respected


---

<!-- Source: 021_random_civil_war_spec_part_5_evolution_ii.md -->


# Evolution II: Regional Contagion

`Regional Contagion` is a working label, not final localisation.

## Role

Evolution II allows a civil war to change politics beyond its borders.

The evolution does not assume that civilians, displaced people, or cultural similarity automatically produce violence. Cross-border risk comes from organized armed networks, sponsors, returning combatants, weapons routes, political emulation, disputed territory, weak administration, and unresolved regional claims. Civilian displacement creates humanitarian, transport, housing, food, and administrative pressure that needs separate responses.

Active Event 021 sides also gain stronger operational and political tools. A small number of rare strange incidents can appear, but their cause remains uncertain and their effects remain bounded.

## Availability and pacing

- Chaos requirement: Rising Chaos
- Active-war transition uses the shared evolution MTTH process
- Timing direction: roughly 90 to 180 days after a live Event 021 war has survived long enough to create regional effects
- Faster timing can come from active cross-border arms routes, foreign sponsors, victory by a movement with related neighbors, long border length, several open crossings, failed containment, or current multi-front war
- Slower timing can come from strong neighboring institutions, controlled corridors, successful mediation, distant geography, early settlement, or lack of any related movement
- Prefire evolved openings can begin with neighbor exposure already active
- One Evolution II log entry is recorded for Event 021
- The same regional spread does not record the evolution repeatedly

## Neighbor eligibility

A neighboring or nearby country can enter the Evolution II exposure system when:

- it shares a land border, short maritime route, political network, or verified regional connection
- at least one live Event 021 side has an external route into it
- the country is a normal human actor
- it is not in a short creation or cleanup lock
- it has a valid domestic pressure channel
- the exposure category can offer at least one meaningful action
- the event does not need to pretend that every neighbor faces the same problem

Possible exposure channels:

- arms smuggling
- returning volunteers
- sponsor competition
- related ideology
- related autonomy or independence movement
- disputed border
- shared military institution
- shared party network
- interrupted trade
- refugee and civilian-support burden
- foreign intelligence activity
- propaganda and political emulation
- cross-border sanctuary
- collapsed local administration

## Neighbor presentation

A neighboring country receives a normal decision category or an Event 021 phase inside its existing category.

The presentation shows:

- source civil war
- relevant border or route
- one current exposure stage
- the public cause of exposure
- current humanitarian or security objective
- a small set of valid actions
- up to two active neighbor missions

It does not expose another permanent numeric meter unless implementation proves that a stage label cannot communicate the state.

Working exposure stages:

- Observed
- Pressured
- Penetrated
- Mobilizing

These labels are not final localisation.

## Neighbor action families

### Monitor the crossings

Role:

- identify arms, cadres, or sponsor routes
- reveal the strongest exposure source
- prepare a targeted response
- avoid a broad expensive crackdown

Costs can include intelligence exposure, support equipment, manpower, and time.

### Seal an arms route

Role:

- reduce military traffic through a named border region
- weaken one sponsor or side
- lower domestic armed-network pressure
- create trade, diplomacy, and humanitarian costs

The action should name the route or region. It must not target civilians as a collective enemy.

### Register and support displaced civilians

Role:

- create transport, housing, food, medical, and administrative capacity
- reduce local competition and exploitation
- prevent armed groups from controlling relief routes
- improve relations and postwar stability

Costs can include civilian factory burden, trains, convoys, stability management, and local administration.

The action treats civilians as people requiring protection. Security risk comes from armed infiltration, coercion, smuggling, and failed administration.

### Open a controlled relief corridor

Role:

- allow food, medicine, evacuation, or neutral transport
- reduce humanitarian pressure
- create a monitored route
- improve mediation credibility

The corridor can be attacked, exploited, or politicized. Its risks should be shown without framing relief itself as the cause of war.

### Open a military aid corridor

Role:

- send equipment, training, or volunteers to one side
- raise sponsor influence
- strengthen one selected actor
- increase retaliation and domestic exposure

The military corridor is separate from civilian relief.

### Counter recruitment networks

Role:

- disrupt armed recruitment, coercion, and illegal training
- reduce one domestic pressure channel
- protect legal political activity from being treated as armed conspiracy

Costs can include manpower, police equipment, intelligence exposure, and local trust.

### Support the existing government

Possible support:

- equipment
- trains
- trucks
- fuel
- officers
- intelligence
- recognition
- volunteers where normal rules allow

Support creates influence and can prolong the conflict. AI must consider distance, ideology, war state, equipment, and diplomatic risk.

### Support an opposition side

The sponsor must select a valid front.

Support can include:

- recognition
- equipment
- training
- intelligence
- transport
- political sanctuary
- volunteers
- industrial credit

Support creates dependency, rival sponsorship, and possible postwar demands.

### Mediate a local ceasefire

Role:

- suspend one border front
- exchange prisoners
- create a corridor
- open settlement talks
- separate two opposition sides

The mediator needs access, relations, credibility, and enough political capacity.

### Expose foreign intervention

Role:

- reveal another sponsor's public role
- reduce covert influence
- change opinion and recognition
- create news
- trigger sponsor withdrawal or escalation

The action should require evidence and risk diplomatic failure.

## Political spread channels

### Ideological emulation

A movement copies organization, demands, or tactics from a surviving side.

Requirements:

- related ideology or political program
- visible success
- domestic organization
- some route for communication or support
- weak or provocative domestic response

Possible effects:

- stronger future ideological archetype
- preventive decisions
- pressure on ruling coalition
- sponsor competition
- increased Event 021 target weight

### Regional or national emulation

A surviving independence actor makes another researched regional movement more confident.

Requirements:

- complete grounded Event 006 package or accepted regional identity
- relevant historical, political, territorial, or institutional link
- viable domestic territory
- real leadership route

Possible effects:

- reveal autonomy talks
- raise package eligibility
- strengthen a future Event 021 opening
- create local institutions
- increase foreign recognition efforts

Event 006 remains unfired unless selected independently.

### Command imitation

Military officers study a successful command schism.

Requirements:

- low military loyalty
- related military institution
- foreign liaison, volunteers, or shared training
- visible success by the original command side

Possible effects:

- depot-security missions
- officer transfer
- stronger command-schism archetype
- increased arsenal pressure

### Sponsor rivalry

Two or more powers back different sides.

Possible effects:

- aid competition
- stronger fronts
- longer war
- conflicting settlement demands
- rival recognition
- volunteer escalation
- intelligence conflict
- postwar dependency
- rebel-on-rebel conflict

The event should not manufacture an external war merely because sponsors exist. Normal diplomacy and faction rules decide whether escalation crosses that line.

### Border dispute activation

A civil war weakens an old border settlement.

Possible effects:

- local mobilization
- recognition of a regional actor
- territorial claims
- armed incidents
- mediation
- Event 006 package eligibility

It must not transfer states without a validated war, settlement, or country route.

## Active-side strengthening

Evolution II gives live sides ways to adapt.

### Operational adaptation

A side can specialize in:

- rail warfare
- mountain defense
- urban defense
- mobile columns
- port control
- dispersed militia
- conventional army integration
- foreign equipment
- intelligence and infiltration

Specialization comes through decisions, missions, controlled terrain, and existing package identity.

### Administrative consolidation

A side that holds territory can:

- establish tax and supply systems
- restore rail service
- recruit local officials
- regulate requisition
- create courts or councils
- open schools or propaganda systems
- manage refugees and civilian transport
- prepare recognition

Long-lived sides need political administrations, military forces, and meaningful institutions.

### Foreign dependence

A side can become stronger through sponsorship, but dependence rises.

Dependence can affect:

- settlement autonomy
- faction choice
- resource concessions
- military access
- postwar advisors
- ideology
- future foreign decisions
- recognition
- domestic legitimacy

A side should not accept every sponsor automatically.

### Rival integration

A stronger side can absorb:

- defeated militia
- surrendered regulars
- local committees
- officers
- regional administrations
- temporary coalition partners

Integration needs manpower, equipment, political compromise, and time.

## Strange incidents

Evolution II permits rare incidents in which a side appears to gain power through practices that witnesses cannot explain.

The incidents should remain:

- uncommon
- uncertain
- limited to one active strange incident per side
- limited by cooldown
- counterable
- materially costly
- distinct from other supernatural events
- free of direct confirmation that dark forces exist
- free of gore and cheap shock

Possible directions:

### Night assemblies

Units gather at ruined shrines, abandoned factories, forests, or trenches and emerge with unusual discipline.

Possible effect:

- temporary organization or planning
- improved concealment
- local recruitment
- lower desertion

Possible cost:

- equipment loss
- officer conflict
- casualties
- lower State Authority
- political radicalization

### Oath circles

A unit swears loyalty through a repeated ritual that creates extreme cohesion.

Possible effect:

- temporary morale
- refusal to retreat
- stronger defense

Possible cost:

- severe losses
- poor reinforcement
- infighting with ordinary units
- postwar refusal to demobilize

### Relic processions

A movement carries an old banner, object, or remains through its territory.

Possible effect:

- local support
- recruitment
- recognition among a specific movement

Possible cost:

- factional exclusion
- diplomatic damage
- rival claim
- target for enemy raids

### Impossible endurance rumors

Soldiers report that one formation does not sleep, eat, or break as expected.

Possible effect:

- temporary movement or recovery
- enemy fear
- propaganda

Possible cost:

- later attrition
- medical collapse
- desertion when the rumor breaks
- internal investigation

### Signal fires and repeated symbols

Unexplained signs appear along a route before coordinated attacks.

Possible effect:

- faster mobilization
- improved local intelligence
- surprise

Possible cost:

- foreign exposure
- lost secrecy
- rival infiltration
- civilian panic

The event text should show observed behavior and consequences. It should not confirm magic, demons, gods, or a universal occult organization.

## Countermeasures to strange incidents

Possible responses:

- rotate affected units
- investigate the organizers
- protect or remove the object
- cut the ritual route
- offer medical and rest support
- challenge the leadership
- expose material fraud
- tolerate the practice for temporary power
- redirect the movement into official ceremony

Responses need tradeoffs. A crackdown can destroy cohesion. Tolerance can create a stronger postwar faction.

## Regional event family

Evolution II can produce:

- report about public foreign aid
- report about a discovered arms route
- news when a second country enters Event 021 through regional pressure
- report about successful mediation
- report about a neighboring autonomy movement
- report about a strange battlefield practice
- news about major foreign sponsorship
- report about humanitarian collapse around a border route

Text direction should use named towns, railways, ports, units, political groups, and routes. It should not rely on generic official denial or generic map-change framing.

## Full civil-war transition in a neighbor

Regional exposure does not automatically create a war.

It can:

- increase target weight
- shorten an evolved opening
- reveal a related archetype
- strengthen a movement
- unlock prevention
- create a small domestic incident
- create a sponsor conflict
- decay after containment

A neighbor enters a full civil war only through:

- a normal Event 021 firing
- the Evolution III critical-country process
- a manual scenario
- another specialized event with its own ownership

## Evolution II AI

### Containment neighbor

Prefers:

- border monitoring
- arms-route control
- civilian support
- limited aid to the government
- preventing domestic recruitment
- early mediation when cheap

Avoids:

- arming several sides
- expensive permanent mobilization
- collective punishment

### Opportunistic sponsor

Prefers:

- one strategically useful side
- equipment it can spare
- influence, access, or ideology
- a side likely to survive
- public recognition after administration exists

Avoids:

- supporting every front
- support during a desperate own war
- a side hostile to its long-term interests

### Neutral mediator

Prefers:

- observer mission
- relief corridor
- prisoner exchange
- local ceasefire
- settlement conference
- delayed recognition

Avoids:

- covert military sponsorship
- settlement terms that cannot be enforced

### Active side

Uses adaptation and foreign aid according to terrain, objective, equipment, and political identity.

## Cleanup

When the source war ends:

- military corridors close or convert
- relief routes close or become reconstruction actions
- sponsor records resolve
- volunteers created by the event return or transfer legally
- border missions end
- exposure begins to decay
- armed-network flags update
- civilians remain eligible for postwar assistance without continued security framing
- strange-incident effects end or convert into a postwar political consequence
- invalid actors leave arrays
- mediation and ceasefire targets clear
- domestic recurrence memory persists only when justified

## Evolution II acceptance

Evolution II is accepted only when:

- neighbor exposure is readable
- relief and military aid remain separate
- refugees and civilians are not treated as automatic violence sources
- organized networks, sponsors, borders, political access, and state weakness drive spread
- neighbor actions have concrete costs and AI
- active sides gain playable adaptation
- strange incidents remain rare, uncertain, bounded, and counterable
- unusual independence actors come only from complete researched packages
- exposure changes future risk without forcing every neighbor into war
- all cross-border targets and routes clean up


---

<!-- Source: 021_random_civil_war_spec_part_6_evolution_iii.md -->


# Evolution III: Global Fracture

`Global Fracture` is a working label, not final localisation.

## Role

Evolution III turns Event 021 into a persistent global risk system.

Every normal human country must manage some level of domestic fracture. Stable countries receive limited prevention and can usually contain their risks. Countries with low State Authority, active regional exposure, long war exhaustion, unresolved settlements, occupied territory, strong organized opposition, or several viable actors face harder prevention and a shorter path to crisis.

The system does not create one simultaneous automatic global civil war. The manual scenario owns that setup.

Evolution III creates a world in which new countries, old countries, subjects, restored states, and human Event 006 countries can all fracture under the same broad rules.

## Availability and pacing

- Chaos requirement: Chaos Tier
- The evolution records once when the global system activates
- An active Event 021 crisis can trigger the activation record through the normal MTTH route
- A prefire evolved opening uses the global risk rules immediately
- Totalen Chaos and World Collapse strengthen the same evolution without new evolution records
- The manual scenario can activate its own immediate setup through a tightly scoped bypass
- Normal Event 021 and global-evolution launches remain distinct for event-weight accounting

## Shared world-threat state

Evolution III should register Event 021 as a source in the shared world-threat aggregate.

The source represents persistent worldwide internal-war risk.

The source should be present when:

- Evolution III is active
- the global risk scheduler can process countries
- at least one country can remain in a risk band, active crisis, or critical queue

The source should clear when:

- Evolution III is disabled
- its global state is fully removed
- a terminal system suppresses normal Event 021 behavior
- cleanup proves that no active or queued Event 021 global state remains

After setting or clearing the source, the shared threat aggregate must refresh.

Event 021 does not become an actual nonhuman or special-chaos country system.

## Global risk bands

Every eligible country belongs to one of four bands.

| Band | Public experience | Normal behavior |
| --- | --- | --- |
| Stable | compact status, limited risk, one targeted preventive action only when needed | long review interval and low crisis weight |
| Exposed | one or more domestic or regional pressures need attention | targeted prevention and moderate review interval |
| Fractured | several serious pressures, weak authority, or nearby armed networks | full prevention layer, strong Event 021 weight, possible critical progression |
| Critical | crisis conditions can sustain a real actor and opening | enters the bounded launch queue or awaits normal Event 021 selection |

The player sees the stage and actionable cause, not the hidden score.

A Stable country should not be forced to click repetitive maintenance every month.

## Global risk inputs

The global model uses the baseline Fracture Pressure components plus:

- number of active Event 021 wars nearby
- shared border with a live Event 021 side
- related victorious movement
- foreign sponsorship networks
- prior Event 021 generation
- recent government or rebel victory
- unresolved autonomy or partition
- human independence actors inside or near the country
- failed neighbor missions
- active strange incident nearby
- current war density
- country count
- world chaos
- global theater capacity

Risk falls through:

- durable settlement
- long peace
- high State Authority
- integrated command
- restored civil administration
- demobilization
- controlled arms routes
- successful neighboring mediation
- strong local institutions
- completed reconstruction
- expired recurrence memory

## Eligibility

A country enters the global system when:

- it exists
- it is a normal human political actor
- it is not an actual nonhuman country
- it is not in a short creation, annexation, or cleanup lock
- it is not in an incompatible bespoke crisis
- it has at least one valid split, opposition, or takeover route
- its event and evolution settings allow Event 021 global behavior
- the world is not in a terminal state that freezes the event

The global system includes:

- Event 006 countries
- human chaos-created countries
- restored historical states
- regional independence countries
- subjects with domestic politics
- countries created through Event 021
- one-state countries through same-tag takeover
- human Fury or other unusual countries only when their package allows internal politics and the overlap does not break the owning event

The system excludes only actual nonhuman countries as a universal class.

## Bounded scheduler

The global system must avoid an unrestricted daily iteration across every country.

Recommended behavior:

1. Maintain a registry of eligible countries.
2. Rebuild or repair the registry after country creation, annexation, major transformation, evolution activation, or periodic bounded maintenance.
3. Assign countries to review buckets or stored next-review dates.
4. Process a limited batch on a slower global pulse.
5. Recalculate only countries whose review is due or whose relevant state changed.
6. Place Critical countries into a bounded queue.
7. Launch only when global theater and local viability caps permit.
8. Keep a processing lock that prevents duplicate launches.
9. Store enough debug counters for performance review.
10. Remove dead, annexed, nonhuman, or invalid countries from the registry.

The implementation route must follow the live repository's on-action rules. A broad default country iteration requires explicit approval and should not be used when a queue can do the work.

## Review cadence

Direction:

- Stable countries receive long review intervals.
- Exposed countries receive moderate review intervals.
- Fractured countries receive frequent but bounded reviews.
- Critical countries remain in a visible queue and receive emergency actions until launched or stabilized.

A country should move between bands when its real conditions change. The system should not create permanent stage labels that ignore recovery.

## Stable-country play

Stable countries see:

- current band
- one short resilience summary
- one or two preventive actions only when a real source exists
- a long-term mission only when exposure persists
- no front selector
- no full crisis category

Possible actions:

- maintain reserve loyalty
- protect arsenals and communications
- review regional administration
- fund local civil services
- monitor an arms route
- prepare a constitutional consultation
- support a neighboring settlement

These actions use resources and should not become routine spam.

## Exposed-country play

Exposed countries receive decisions tied to the strongest pressure.

Examples:

- border exposure produces corridor, relief, arms-route, and local-administration actions
- low military loyalty produces officer, depot, and command actions
- strong opposition produces coalition, political access, and security actions
- war exhaustion produces leave, supply, demobilization, or peace-pressure actions
- postwar memory produces amnesty, veteran, constitutional, and integration actions

The system should not display every possible prevention family at once.

## Fractured-country play

Fractured countries receive the full prewar crisis layer.

They can:

- reduce the opening territory
- reduce the force share
- prevent one actor
- change independence into autonomy
- strengthen the parent remnant
- choose a political or military posture
- secure a capital
- seek foreign support
- prepare a negotiated settlement
- raise or sacrifice State Authority

The player must understand that prevention can reshape the crisis even when it cannot always remove all risk.

## Critical-country launch

A Critical country can enter a civil war through:

- a normal Event 021 repeatable firing
- the Evolution III critical-country process
- the manual scenario

The Evolution III process is an evolution-owned launch, not a second random-event firing.

It must still:

- respect event and evolution enable state
- use normal target safety
- create Event 021 history or an evolution-linked incident record
- respect global theater and front caps
- avoid duplicate launch
- use the same actor, map, force, decision, AI, and cleanup systems
- keep repeatable event weight accounting separate
- record why the country left the queue

## Global theater cap

The system needs a tested cap on active Event 021 theaters and fronts.

The cap should scale with:

- number of existing countries
- average country count after other events
- active Event 021 theaters
- total active fronts
- major wars
- current game phase
- scenario intensity
- host performance testing
- multiplayer load

A normal Evolution III world should have enough simultaneous crises to be visible across regions without overwhelming the game.

Totalen Chaos can raise the cap and shorten queue intervals.

World Collapse can use the highest tested sustainable cap.

The manual Maximum scenario can commit all eligible countries at confirmation, then use its own validated setup process.

A queued Critical country must receive emergency play. It should not be silently protected forever by the cap.

## Nested crises

A country created through Event 006 or Event 021 can fracture again after a grace period.

### Eligibility

- package initialization complete
- spawn grace expired
- at least one valid actor
- territory can split or same-tag takeover works
- country remains human
- no incompatible country-specific crisis is active
- global generation cap allows another descendant
- the result will not create an actor identity collision

### Nested independence

A new independence country can contain smaller historic, regional, ideological, or command movements.

A nested independence actor still requires a complete package. The event does not invent a new nationality because a smaller region exists.

### Nested ordinary crisis

A young state can face:

- rival legal government
- old elite restoration
- ideological revolt
- military takeover
- autonomy movement
- regional secession
- coalition breakdown

### Generation cap

The design should track civil-war lineage.

Default direction:

- ordinary automatic play supports up to two descendant generations inside one lineage
- later generations require stronger pressure and longer grace
- a scenario can override the limit within its own performance contract
- merger, annexation, or durable settlement closes the lineage
- the cap prevents infinite internal wars inside newly created microstates

The exact cap belongs in constants and testing.

## Successor crises

A rebel victory can create a successor state that inherits:

- unresolved rival fronts
- a damaged administration
- foreign obligations
- disputed regions
- unreconciled officers
- an old legal claimant
- an independence promise
- revolutionary factions

A successor crisis should not begin instantly after ordinary victory.

Direction:

- settlement and warning decisions begin immediately
- earliest ordinary continuation around 45 days
- normal recurrence around 60 to 180 days in high-risk cases
- strong settlement can delay beyond a year or remove the risk
- scenario behavior can be immediate

## One-state and microstate route

Every normal human country needs a valid Evolution III response.

For a one-state or unsafe all-island country:

- use a same-tag loyalty contest
- show State Authority
- create armed-cell or command events
- run a timed control mission
- use foreign sponsor pressure
- allow leader, ideology, law, party, or subject change
- apply real casualties and administrative damage at a scale fitting the country
- do not create a zero-state actor
- do not invent an impossible second capital

## Global reactions

### Faction leaders

Faction leaders can:

- monitor vulnerable members
- send equipment or observers
- mediate
- pressure a settlement
- prepare for leadership succession
- limit support to one side
- respond to a member government changing

They should not automatically join every internal war against every front.

### Major powers

Majors can:

- choose a regional influence priority
- support one side
- contain the conflict
- mediate
- compete with another sponsor
- recognize a country
- demand postwar access
- reduce support when their own war deteriorates

They should not sponsor more sides than their industry, diplomacy, and strategy support.

### Neighbors

Neighbors maintain the Evolution II exposure logic and can face their own band changes.

### Subjects and overlords

A subject can fracture without automatically triggering Event 144.

The overlord can:

- support the government
- support a rival
- mediate
- allow separation
- recognize independence
- tighten control
- negotiate autonomy

An overlord's own civil war can change subject loyalty, but should not automatically release every subject.

## High-chaos side power

Surviving sides can gain unusually strong tools at higher chaos.

Possible tools:

- mass regional mobilization
- emergency industry conversion
- foreign arsenal access
- captured national command
- rapid rail repair
- integrated rival formations
- revolutionary, restoration, or independence fervor
- expanded militia networks
- strange doctrine escalation
- national recruitment after taking the old capital

Each tool needs:

- a visible objective
- concrete cost
- aftermath
- AI conditions
- cleanup
- cap or one-time gate
- no conflict with Event 006 identity

An Event 006 actor should become powerful through its own tree, decisions, formables, and force systems where possible.

## Global event directions

### Activation report

Show several specific countries experiencing different political, military, and regional pressures. Avoid a generic world map.

### First nested crisis

A young human state fractures, showing that independence does not create immunity.

### Major rupture

A major country enters a multi-front crisis with visible city, command, regional, and foreign consequences.

### Durable settlement

A country lowers risk through an enforceable agreement, showing that the system can be managed.

### Successor fracture

A victor faces another crisis because the first victory did not settle the country.

### Strange escalation

Several active sides use unexplained practices. The report remains uncertain and does not reveal a global occult truth.

## Higher chaos scaling

### Totalen Chaos

- shorter review intervals
- more Exposed and Fractured states
- higher theater cap
- more multi-front openings
- broader Event 006 candidate use
- more foreign sponsorship
- shorter successor grace
- higher strange-incident chance within its cap

### World Collapse

- highest tested sustainable theater cap
- faster Critical queue
- major countries common
- nested crises more likely
- strongest complete human independence packages
- negotiated settlement remains possible
- actual nonhuman countries remain immune
- Event 021 remains nonterminal

## Evolution III AI

### Stable AI

- uses prevention only for a real pressure
- avoids wasting equipment on permanent readiness
- supports nearby settlement when useful

### Exposed AI

- addresses the strongest source
- secures arsenals and routes
- avoids repression when authority is already weak
- uses concessions when compatible

### Fractured AI

- commits more resources
- prioritizes capital and supply
- chooses a political or military posture
- seeks one useful sponsor
- avoids several incompatible prevention actions

### Critical AI

- prepares one or two achievable opening objectives
- does not stall the queue
- follows strict route validity
- considers current external war
- preserves a viable force

### Successor AI

- resolves old fronts
- restores administration
- manages sponsors
- avoids immediate aggressive expansion while internally weak
- chooses recurrence prevention according to ideology and settlement

## Evolution III acceptance

Evolution III is accepted only when:

- every normal human country has a valid band or takeover route
- actual nonhuman immunity uses the shared narrow trigger
- human Event 006 countries remain vulnerable
- the scheduler is bounded
- Critical countries cannot be silently stuck forever
- theater and generation caps are tested
- nested crises have grace and identity safety
- State Authority and prevention remain readable
- global reactions use role-specific AI
- the shared world-threat source sets and clears correctly
- normal event firing continues
- Event 021 does not set a terminal state
- cleanup removes global records when the evolution is disabled or suppressed


---

<!-- Source: 021_random_civil_war_spec_part_7_event_006_country_packages_and_focus_handling.md -->


# Event 006 Country Packages and Focus Handling

## Country-package principle

Event 021 has three actor routes.

1. Ordinary national claimants preserve the parent country's identity and national content.
2. Temporary regional actors use a bounded crisis identity and must resolve into a permanent disposition.
3. Independence actors use a complete Event 006 country package.

This split prevents Event 021 from creating a large library of shallow permanent tags while still allowing the researched Independence Wave countries to appear throughout Chaos Redux.

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

`assets/vanilla_reference/icons/decision_categories/pictures`

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

## Achievement set

Event 021 uses six achievements.

All names are working labels.

Achievements should normally be unavailable when force-trigger, debug setup, or a manual scenario bypasses the required normal conditions. The implementation can define a scenario-specific exception only through an accepted change to this package.

### 1. Hold the Center

Working ID:

`021_random_civil_war_hold_the_center`

Eligible country:

- original affected government
- player-controlled

Unlock direction:

- win an Event 021 civil war
- retain the original or validated replacement capital throughout the decisive war
- State Authority never enters the Collapse stage after the opening
- no force-trigger or scenario bypass

Difficulty:

- hard

Why it is not trivial:

- the player must defend the capital while stabilizing authority and fighting the war

Icon direction:

- fortified capital building with divided banners held outside the center

Tracking needs:

- original capital
- replacement-capital validity
- minimum State Authority reached
- final government victory
- disqualifiers

### 2. No State Left Behind

Working ID:

`021_random_civil_war_no_state_left_behind`

Eligible country:

- original government or legitimate successor

Unlock direction:

- resolve an Evolution I multi-front crisis
- recover or peacefully reintegrate every original core state that belonged to the country at the Event 021 opening
- use no harsh settlement route
- no unresolved partition remains
- no scenario or force trigger

Difficulty:

- very hard

Why it is not trivial:

- the player must settle several fronts while preserving reintegration and avoiding the easiest punitive route

Icon direction:

- several broken pieces fitted around a central state seal

Tracking needs:

- opening core-state set
- front count
- harsh-settlement disqualifier
- partition status
- final control and integration

### 3. A Flag of Our Own

Working ID:

`021_random_civil_war_a_flag_of_our_own`

Eligible country:

- player-controlled human Event 006 package created through Event 021

Unlock direction:

- win recognized independence from the former host
- survive the immediate postwar period
- complete one Event 006 formation, formable, recognition, or national consolidation milestone defined by that package
- remain independent
- no scenario or force trigger

Difficulty:

- hard

Why it is not trivial:

- the player must win the civil war and continue into the package's normal national content

Icon direction:

- a newly raised regional flag above a defended assembly, using no specific real flag unless the final icon is package-neutral

Tracking needs:

- Event 021 origin
- former host
- recognized independence
- survival period
- Event 006 milestone
- independence status

### 4. War Within a War

Working ID:

`021_random_civil_war_war_within_a_war`

Eligible country:

- original government or legitimate successor
- player-controlled

Unlock direction:

- enter Event 021 while fighting a major external war
- defeat or settle every Event 021 front
- remain in existence
- avoid capitulation to the external enemy during the civil war
- no scenario or force trigger

Difficulty:

- very hard

Why it is not trivial:

- the player must survive two strategic wars at once

Icon direction:

- two crossed fronts, one facing inward and one outward, around a defended capital

Tracking needs:

- qualifying external war at opening
- Event 021 front list
- external capitulation state
- full internal resolution
- final existence

### 5. The Terms Hold

Working ID:

`021_random_civil_war_the_terms_hold`

Eligible country:

- any player-controlled signatory to a negotiated Event 021 settlement

Unlock direction:

- conclude a coalition, autonomy, recognition, or armistice settlement
- keep the settlement intact for a long defined period
- complete required disarmament or constitutional obligations
- prevent Event 021 recurrence in the signatory countries during that period
- no scenario or force trigger

Difficulty:

- hard

Why it is not trivial:

- peace must survive after the fighting ends

Icon direction:

- signed agreement protected by stacked surrendered weapons and an intact seal

Tracking needs:

- settlement type
- signatories
- obligations
- violation
- recurrence
- survival duration

### 6. Fractals of Sovereignty

Working ID:

`021_random_civil_war_fractals_of_sovereignty`

Eligible country:

- player-controlled human Event 006 country
- country must itself have been created before the nested Event 021 crisis

Unlock direction:

- suffer a nested Event 021 crisis
- preserve independent statehood
- resolve every nested front
- retain or recover the package's core homeland
- remain human
- no scenario or force trigger

Difficulty:

- very hard

Why it is not trivial:

- the player must survive an internal crisis inside a young independence country without losing the identity it previously won

Icon direction:

- a smaller fractured seal contained inside a larger intact national emblem

Tracking needs:

- Event 006 identity
- Event 021 generation greater than zero
- nested-front list
- package homeland
- final independent status
- actual nonhuman exclusion

## Achievement presentation rules

Each achievement needs:

- final localisation
- completed icon
- grey icon
- not-eligible icon
- exact tracking
- disqualifiers
- documentation
- route and origin hooks
- no automatic easy unlock
- one root registry entry under the existing achievement unique ID
- event grouping in the project achievement registry

The completed icon is designed first. Variants follow the achievement workflow.

## Asset acceptance

Assets are accepted only when:

- every authorized runtime asset has source art
- source mode is recorded
- final PNG and DDS exist
- transparency is correct
- dimensions match the verified consumer
- distinct icon families use distinct source art
- static category picture contains no fake UI
- Event 006 identity assets are reused
- no grounded portrait is invented
- every achievement has a full triplet
- runtime and documentation paths agree
- temporary asset workspace is cleaned only after durable evidence and runtime wiring are reconciled


---

<!-- Source: 021_random_civil_war_spec_part_10_acceptance_and_implementation_handoff.md -->


# Acceptance and Implementation Handoff

## Source-of-truth order

Implementation should use this order when two sources differ:

1. User corrections in the current accepted task
2. This revised Event 021 specification package
3. Current repository `AGENTS.md`
4. Current relevant Chaos Redux skills
5. Current live Chaos Redux implementation and shared contracts
6. Installed vanilla documentation and vanilla precedents
7. Offline Paradox wiki snapshot
8. Prior Event 021 planning package where it does not conflict with this revision
9. Catalog CSV exports as read-only snapshots

The authoritative event catalog workbook remains the only editable catalog source.

## Required implementation preflight

Before editing:

- read repository `AGENTS.md`
- read this complete Event 021 package
- read the current Event 021 files if any
- inspect Event 006 specs, registry, carriers, package initializers, focus assignment, forces, reinforcement, formables, AI, assets, and docs
- inspect Event 004 and Event 007 cluster behavior
- inspect Event 019 formation revolt boundaries
- inspect the specialized overlap events listed in Part 7
- read the required offline wiki pages
- read relevant installed vanilla documentation
- inspect vanilla civil-war, decision, mission, country, character, subject, faction, and asset precedents
- inspect existing Chaos Redux civil-war and dynamic-country precedents
- inspect the live HOI4 MCP schemas
- verify the authoritative workbook
- verify a free scenario ID
- run tag and character ownership audits
- spawn project subagents with `fork_context=false`

The implementation must not invent unavailable tool names or treat source review as equivalent to required MCP evidence.

## Recommended implementation tranches

### Tranche 1: Repository and contract map

Output:

- Event 021 current-state map
- Event 006 reusable API map
- overlap event boundaries
- cluster and scenario registry
- expected gameplay files
- asset consumers
- documentation and workbook surfaces
- blocker list

Use `chaosx_repo_explorer`.

### Tranche 2: Shared architecture

Output:

- script constants
- target and viability triggers
- hidden Fracture Pressure
- visible State Authority
- actor and front registry
- territory planner
- force planner
- Event 006 adapter
- cleanup
- recurrence
- generation tracking

Use `chaosx_scripted_system_architect` for reusable helper design and narrow implementation.

### Tranche 3: Baseline event

Output:

- entry dispatcher
- target pool
- six archetypes
- baseline map and force planning
- opening events
- government and opposition category phases
- baseline AI
- baseline outcomes
- event log and Event Details
- docs

Run event MCP inspection and baseline probability tests.

### Tranche 4: Decisions and missions

Output:

- phased category
- State Authority presentation
- government actions
- opposition actions
- selected-front flow
- missions
- costs
- success, failure, partial success
- AI
- cleanup
- localisation

Use `chaosx_decision_mission_auditor` after the owner implements the system.

### Tranche 5: Event 006 integration

Output:

- idempotent Event 021 origin adapter
- candidate validation
- Event 006 package creation
- former-host war
- focus loading
- force and reinforcement
- formation decisions
- recognition and diplomacy
- package cleanup
- nested eligibility

Use `chaosx_country_package_auditor`. Use the focus auditor only if focus files or loading behavior change.

### Tranche 6: Evolution I

Output:

- active and prefire paths
- major targeting
- multi-front plan
- distinct side objectives
- independent front settlement
- prevention actions
- AI and probability tests
- event and evolution logs

### Tranche 7: Evolution II

Output:

- neighbor exposure
- civilian relief
- arms-route control
- sponsorship
- mediation
- active-side adaptation
- strange incidents
- cleanup
- AI and probability tests

### Tranche 8: Evolution III

Output:

- world-threat source
- eligible-country registry
- risk bands
- bounded scheduler
- Critical queue
- theater cap
- nested crises
- generation cap
- high-chaos scaling
- global reactions
- cleanup
- performance tests

### Tranche 9: Wars cluster and manual scenario

Output:

- Event 021 cluster membership
- reservation and collision behavior
- skip reasons
- verified scenario ID
- four types
- four intensities
- confirmation
- immediate setup
- measured batch contingency
- bypass cleanup
- scenario docs and workbook fields

### Tranche 10: Presentation and achievements

Output:

- report and news assets
- static category picture
- category, decision, mission, idea, and achievement icons
- final localisation
- six achievements
- manifests and handoffs
- documentation

Use the proper asset subagents. Do not create unauthorized portraits or animation.

### Tranche 11: Improvement and completion review

After meaningful implementation:

- run `chaosx_improvement_loop_planner`
- resolve the addendum, closure handoff, or rejection
- run probability comparison
- run decision, country, focus where applicable, localisation, and completion audits
- run documentation curation
- update the authoritative workbook through the spreadsheet worker
- export CSV snapshots
- run acceptance scenarios
- report every blocker or simplification
- commit the completed plan as one intentional Git commit

Do not deploy another improvement loop for Event 021 while an earlier Event 021 addendum remains unresolved.

## Expected gameplay surfaces

The final exact file map belongs to repository exploration.

Likely event-owned or shared surfaces include:

- event definitions
- event registration and availability
- script constants
- scripted triggers
- scripted effects
- on-actions or bounded pulse adapters
- decisions and categories
- ideas or dynamic modifiers
- AI strategy and templates
- event logs and Event Details
- evolution logs
- cluster registry and logging
- scenario registry and UI
- country collections and Event 006 adapters
- characters and portrait references only when required
- focus loading only when required
- localisation and scripted localisation
- report and news sprites
- decision and idea sprites
- achievements
- event docs
- system docs
- authoritative workbook

Do not create a new file merely to match this list when an existing subsystem file owns the behavior.

## MCP requirements

### Event chains

Use the event inspection, rendering, and comparison routes for:

- dispatcher
- active-war evolution
- settlements
- scenario launch
- cluster integration
- cleanup
- actor and scope flow

### Probability

Every complex weighted surface requires:

1. baseline `hoi4.probability_inspect`
2. named scenario evaluation
3. sweeps where thresholds can reverse ordering
4. owner-applied patch
5. `hoi4.probability_compare` on the same scenarios
6. rendering when a matrix, timing graph, sensitivity view, or comparison improves review

Use simulation only for declared uncertain inputs.

Use sequence analysis only when the complete pool, cadence, recovery, caps, cooldowns, removals, resets, and terminal states are declared.

### Focus

If focus files or focus loading change:

- inspect the tree
- render the relevant branch
- review filters and navigation
- compare source changes
- run focus audit

### GUI

The accepted design does not require a new dedicated scripted GUI. Do not route the event to `chaosx_event_ui_worker` unless a later accepted addendum proves that normal decisions cannot present the system.

### Map

If the region planner requires map rewriting, inspect map data and use the supported map route. Ordinary state selection and transfer should remain gameplay scripting where possible.

## Probability acceptance scenarios

The full named matrix is in `021_random_civil_war_probability_scenario_matrix.md`.

Minimum required comparisons:

- stable minor versus unstable minor
- unstable minor versus stable major after Evolution I
- unstable major versus stable minor
- recent target versus comparable fresh target
- ordinary ideological actor versus complete Event 006 actor at baseline
- Event 006 actor at Evolution I
- one viable actor versus three viable actors
- negotiated settlement versus harsh settlement recurrence
- neighboring active war versus distant comparable country
- strange-incident chance in an ordinary side versus a long-lived high-chaos side
- Critical queue ordering
- scenario shares by intensity
- cluster overlap by chaos tier

The implementation owner chooses the intended tuning. The probability auditor reports actual behavior.

## Acceptance scenarios

### Baseline stable minor

Expected:

- limited opening
- one opponent
- coherent small region
- low force share
- clear category
- winnable government defense
- no irrelevant major systems

### Baseline unstable minor

Expected:

- serious or severe opening
- stronger opponent
- larger region
- State Authority pressure
- useful decisions and missions

### One-state country

Expected:

- same-tag takeover
- no invalid actor
- leader or government outcome
- real mission and consequences
- complete cleanup

### Subject country

Expected:

- valid overlord choices
- no automatic global subject revolt
- safe faction and war handling

### Evolution I medium country

Expected:

- three total belligerents when viable
- distinct goals
- separate front selection
- independent settlement
- rebel victory preserves unresolved fronts

### Evolution I major

Expected:

- strict viability
- several fronts
- viable government remnant
- safe external-war handling
- acceptable performance

### Event 006 independence front

Expected:

- complete package
- Event 021 origin
- former-host war
- Event 006 tree and decisions
- no Event 006 fire or evolution state change
- no duplicate identity

### Evolution II border region

Expected:

- exposure category
- relief and military aid separated
- sponsor and mediation AI
- no forced war in every neighbor
- cleanup after source war

### Strange incident

Expected:

- one active incident per side
- uncertain text
- visible effect and cost
- countermeasure
- no overlap with another event
- cleanup

### Evolution III stable country

Expected:

- compact band
- no decision wall
- long review interval
- easy containment

### Evolution III Critical country

Expected:

- visible emergency state
- queue entry
- no duplicate launch
- launch when capacity permits
- full Event 021 opening

### Nested human independence country

Expected:

- grace period
- valid actor
- generation tracking
- package identity preserved
- no actual nonhuman immunity

### Actual nonhuman country

Expected:

- excluded from automatic Event 021 and global risk
- no visible prevention category
- no scenario target

### Wars cluster

Expected:

- all members reserve before commitment
- correct collision behavior
- one pacing event
- useful skip reasons
- each member keeps identity

### Scenario Low

Expected:

- about one tenth of eligible countries
- minors
- limited fronts
- no evolution prerequisites

### Scenario Maximum

Expected:

- every eligible normal human country committed
- strongest sustainable plans
- actual nonhuman exclusion
- immediate or measured seven-day batch completion
- no terminal flag
- acceptable save and game-speed behavior

### Settlement and recurrence

Expected:

- every settlement type changes aftermath
- negotiated settlement can remain durable
- harsh settlement can raise recurrence
- no automatic immediate second war
- stale fronts and targets removed

### Save and reload

Expected:

- front registry persists
- selected-front state rebuilds safely
- State Authority persists
- missions persist correctly
- Event 006 origins persist
- scenario and evolution state persists
- cleanup remains complete

## AI acceptance

AI is accepted only when:

- role profiles produce different decisions
- governments defend capitals and supply
- independence actors pursue package goals
- sponsors limit commitments
- mediators do not arm sides
- neighbors separate relief from security
- successors rebuild before expansion
- invalid routes receive zero weight
- AI does not create unit, aid, or recognition loops
- AI responds to external war and equipment
- AI can use every player-facing action through an equivalent route

## Asset acceptance

Asset completion requires:

- final static source art
- processed PNG
- final DDS
- correct path
- correct sprite handoff
- manifest
- contact sheet where required
- correct transparency
- asset-type separation
- achievement triplets
- no animation requirement
- no custom 3D requirement
- Event 006 identity reuse
- no invented grounded portrait

## Documentation and workbook acceptance

Update:

- Event 021 event documentation
- shared civil-war system documentation if helpers become public
- Event 006 integration documentation
- Wars cluster documentation
- triggerable scenario documentation
- asset and achievement crosswalks
- Event Details and evolution wording
- authoritative workbook
- exported CSV snapshots

The workbook worker should mirror final in-game wording. It must not invent implementation facts.

## Completion report

The final implementation report should include:

- files changed
- systems implemented
- route and archetype coverage
- Event 006 package coverage
- AI profiles
- probability evidence
- performance evidence
- cluster and scenario evidence
- assets
- achievements
- documentation
- workbook export
- audit results
- accepted improvement-loop disposition
- remaining blockers
- simplifications and fallbacks

If no simplifications or fallbacks remain, state that explicitly and support it with evidence.

## Planning-environment disclosure

All files supplied in this task, all catalog CSV exports, and every TOML definition inside `subagents.zip` were read fully.

The live Chaos Redux repository, offline wiki snapshot, installed vanilla documentation, vanilla files, Workshop references, HOI4 MCP, and subagent execution interfaces were not available in this planning environment. They remain mandatory implementation gates.

The July 25 Event 021 File Library package was reviewed through its compiled master specification and key supporting records. Its loose package was not mounted for direct byte-level comparison. The revision file records which design decisions this package retains and changes.
