# Catalog identity (part 1)

Verbatim part of [021_random_civil_war_master_spec.md](021_random_civil_war_master_spec.md), which indexes this specification.

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

The event remains disabled by default while its catalog status is unreworked or unavailable. Once the complete rework is implemented for test entry, it enters the reworked-event default allowlist while retaining `Needs Testing` until acceptance certification is complete.

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
