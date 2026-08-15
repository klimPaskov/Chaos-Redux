# Independence Wave, Part 3: Mechanics, decisions, and missions

All names in this file are working labels, not final localisation.

## The state survival system

Every country with active Independence Wave origin receives the same core survival system. Regional overlays, government routes, country ambitions, and package archetypes change how the values move and what they unlock.

## Pre-event surface decision

There is no pre-event Independence Wave decision category, mission, pressure meter, cost, queue, or history indication. The player sees no Event 006 decision surface until the public event has fired and created an active Event 006 origin.

Low stability, resistance, occupation, host pressure, or any other world-state condition must not expose or imply an early wave request. The normal post-event decision and mission map remains gated by the active-origin and package contracts below; the pre-event state is intentionally empty.

The old crisis helpers may remain only for parser compatibility with historical scripted references. They are not a player-facing mechanic, their opening trigger is hard-disabled, and no new code may call their category, mission, cost, queue, or pre-event history keys.

The system has five country values and three relationship layers.

### Country values

1. Founding Legitimacy
2. International Recognition
3. Government Capacity
4. Security Readiness
5. Post-Release Instability

### Relationship layers

1. Former Host Relationship
2. Patron Influence
3. Independence Network and League Standing

The values should be visible in a decision category header or dedicated scripted GUI. Normal decisions remain the main action layer. The custom interface helps the player understand the country rather than replacing decisions with decorative buttons.

## Founding Legitimacy

Founding Legitimacy measures whether residents, local institutions, political movements, military commanders, traditional authorities, and regional elites accept the new state.

### Main sources

- control of the capital and core anchor
- functioning local administration
- a constitutional or traditional settlement
- elections, congresses, councils, or recognized succession
- victory against former-host pressure
- successful public service missions
- negotiated border settlements
- fulfillment of promises made at independence
- support from local movements and communities

### Main losses

- military coups
- foreign domination
- prolonged emergency rule
- corruption
- famine, severe shortages, or unpaid troops
- losing the capital
- uncontrolled militia violence
- surrendering claimed territory without compensation
- government route contradictions
- forcing a formable without adequate consent

### Threshold behavior

| Band | Public condition | Gameplay meaning |
| --- | --- | --- |
| Disputed | The government is one claimant among several | Political branches remain unstable, militia and provincial challenges are common |
| Provisional | The state can issue orders but lacks broad confidence | Core survival decisions are available, major ambitions remain blocked |
| Established | The government has a working domestic mandate | constitutional settlement, league leadership, and stronger diplomacy open |
| Entrenched | The state has durable institutions and a national narrative | peaceful integration and advanced formables become easier |
| Foundational | The state has become the accepted center of political life | powerful capstones, succession stability, and regional leadership become possible |

## International Recognition

Recognition measures formal diplomatic acceptance and practical access to the international system.

It includes bilateral recognition, diplomatic missions, trade access, legal status, treaty acceptance, and admission to wider institutions.

### Recognition components

- bilateral recognition count and quality
- recognition by neighbors
- recognition by regional powers
- recognition by great powers
- treaty registration and diplomatic representation
- compliance with accepted international obligations
- participation in arbitration or league structures
- recognized control of territory

### Recognition states

| State | Meaning |
| --- | --- |
| Unrecognized | Other countries treat the government as temporary, rebellious, or legally uncertain |
| Observed | Trade offices, liaison missions, or informal contacts exist |
| De Facto | Several countries accept the government in practice |
| Treaty-Backed | Formal recognition and public agreements protect the state |
| Internationally Entrenched | The state has broad recognition and institutional membership |

### Recognition is not a popularity meter

A country may be widely recognized and still lack domestic legitimacy. A revolutionary government may have strong legitimacy and little recognition. A patron client may gain recognition quickly while losing independence.

## Government Capacity

Government Capacity measures whether the state can collect revenue, run ministries, maintain transport, administer law, supply the army, and communicate with its territory.

The four public pillars of statehood feed this value:

- population administration
- territorial administration
- functioning government
- external relations capacity

### Main sources

- civil service recruitment
- control of railways, ports, and telegraph routes
- currency and revenue decisions
- census and property registration
- judicial settlement
- educated exile return
- foreign technical assistance
- regional autonomy arrangements
- stable capital administration

### Main losses

- isolated territory
- destroyed infrastructure
- hostile civil service
- currency collapse
- corruption
- overlarge territorial grants at release
- annexed or contested capital
- patron officials replacing local institutions
- rapid formable integration without administration

### Capacity profile by package

A compact urban or port state may start with high capacity and low security. A broad rural restoration may start with high symbolic legitimacy and low capacity. A former federal republic may inherit institutions but face disputed loyalty. A local polity may use community institutions effectively inside a small anchor while lacking wider bureaucratic reach.

## Security Readiness

Security Readiness measures command cohesion, trained forces, equipment, supply, border control, and the ability to resist the former host or other rivals.

### Main sources

- integrated militia
- defecting host units
- secure depots
- trained officer corps
- supplied divisions in border states
- foreign arms and volunteers
- league reserves
- mountain, desert, island, or frontier defense plans
- military professionalization focuses

### Main losses

- unpaid troops
- militia factionalism
- equipment shortages
- lost depots
- capital encirclement
- overmobilization
- military political interference
- patron command missions
- failed border wars

Security can rise quickly through foreign support, but Patron Influence and instability may rise with it.

## Post-Release Instability

Instability is the main pressure value. It represents disputed authority, shortages, uncertainty, border tension, factional conflict, administrative gaps, and fear of reconquest.

High instability changes available incidents, AI willingness, coups, border wars, and the pace of state-building.

### Instability sources

- small or disconnected territory
- several disputed borders
- hostile former host
- multiple political factions
- militia autonomy
- low capacity
- low legitimacy
- high patron rivalry
- recent war or occupation
- refugees and population transfer
- forced integration
- radical high-chaos route

### Instability reduction

- successful founding missions
- recognized borders
- civil service integration
- stable government settlement
- host treaty
- league guarantee
- reliable supply
- local autonomy agreements
- fair elections or accepted traditional succession

### Instability is not meant to reach zero easily

A new country should retain some post-release tension until its early tree and decision cycle are complete. Radical routes may deliberately preserve high instability and turn it into mobilization power, at the cost of coups, wars, and diplomatic isolation.

## Former Host Relationship

Every release creates a bilateral relationship state.

### Relationship dimensions

- legal claim intensity
- military hostility
- negotiated obligations
- property and debt dispute
- population and refugee dispute
- border settlement progress
- host domestic pressure
- new-state fear of reunion or reconquest

### Relationship outcomes

#### Recognized Separation

The host accepts independence and negotiates debts, property, access, borders, and minority protections.

#### Guarded Coexistence

Both states avoid war, but claims and mobilization remain.

#### Autonomy Offer

The host offers federal status, personal union, protectorate, or restored autonomy. Acceptance can end active Independence Wave country status through voluntary reunion, or create a special associated-state route if the country remains sovereign.

#### Client Settlement

The host recognizes independence in exchange for bases, economic control, aligned leadership, or military limits.

#### Reclamation Conflict

The host prepares war or launches reconquest. The released country receives emergency missions and can seek league defense.

#### Host Collapse

The former host loses the ability to pursue claims. Released states may negotiate succession, divide debts and assets, or form a regional order.

## Patron Influence

Patron Influence is tracked separately for each major sponsor that actively supports a released country.

### Patron channels

- diplomatic recognition
- arms and equipment
- volunteers and officer missions
- industrial investment
- intelligence and security assistance
- trade and shipping access
- ideological organization
- loans and currency support
- bases and transit rights

### Dependency pressure

Support creates influence according to type, value, visibility, and the released country's capacity to absorb it.

Influence becomes dependency when:

- one patron dominates several channels
- the state lacks alternative recognition
- foreign officers control the army
- loans or investment exceed government capacity
- the patron appoints ministers or demands route changes
- the country accepts basing or resource concessions

### Anti-puppet play

The player can reduce dependency by:

- balancing several patrons
- using league institutions
- building domestic capacity
- paying down obligations
- rejecting foreign command
- diversifying trade
- exposing patron interference
- accepting slower growth for greater autonomy

A country can choose a client route. That is a real political path, not an accidental failure. It receives powerful short-term support and distinct content, but loses independent diplomatic options and can trigger domestic backlash.

## Independence Network and League Standing

Before a formal league exists, released countries participate in a loose network.

Network standing rises through:

- recognizing other Event 6 countries
- sending aid
- accepting arbitration
- rescuing a threatened member
- supporting congress preparation
- sharing civil servants and officers
- honoring bilateral guarantees

It falls through:

- annexing another Event 6 country
- becoming a host proxy
- refusing agreed arbitration
- abandoning a guaranteed member
- exploiting members through debt or territorial coercion
- supporting host reconquest

Network standing affects invitations, leadership votes, league trust, and member assistance.

## Mechanic presentation

The preferred presentation is a compact scripted GUI attached to the Event 6 decision category.

### Main panel

- five country values with current band and short breakdown
- former host status card
- strongest patron card and dependency warning
- independence network standing
- current founding phase
- active missions

### Secondary tabs

1. Government and Legitimacy
2. Recognition and Patrons
3. Security and Borders
4. League and Other Released States
5. Regional Ambitions

### State-driven visual cues

- recognition seal brightens as recognition rises
- dependency frame pulses when one patron approaches control
- instability warning appears only in dangerous bands
- league charter emblem activates when congress conditions are met
- formable seal changes from hidden, discovered, eligible, and proclaimed states

Every animated element needs a static fallback and a real frame-by-frame asset package. The interface remains readable with animation disabled.

## Decision category phases

The decision system changes as the country matures.

### Phase A: Emergency Founding

Visible immediately after release.

Main actions:

- secure the capital
- appoint an emergency cabinet or governing body
- take control of local administration
- secure one depot or transport hub
- issue a temporary legal order
- establish first revenue collection
- integrate the first armed units

### Phase B: Provisional State

Opens after minimum Government Capacity and capital control.

Main actions:

- run constitutional or traditional settlement missions
- establish ministries
- standardize currency and taxation
- choose regional autonomy arrangements
- launch recognition missions
- negotiate first host contacts
- train regular formations

### Phase C: Recognized State

Opens after De Facto recognition or a host settlement.

Main actions:

- sign treaties
- build permanent diplomatic missions
- professionalize armed forces
- seek guarantees
- enter or lead the league
- arbitrate borders
- discover regional formables

### Phase D: Regional Power

Opens after strong legitimacy, capacity, security, and route progress.

Main actions:

- pursue formables
- sponsor later Independence Wave countries
- lead league policy
- intervene in member crises
- pressure former hosts
- unlock high-chaos ambitions where allowed

## Founding mission family

### Secure the Provisional Capital

Owner: every released country

Objective:

- control the capital
- maintain supplied units there
- prevent encirclement or occupation for a dynamic duration

Costs:

- tied-down divisions
- infantry equipment
- support equipment
- train or truck burden when the capital lacks supply

Success:

- Government Capacity rises
- Instability falls
- capital administration idea improves

Failure:

- Legitimacy loss
- emergency relocation event
- military or provincial faction gains influence

### Establish a Revenue Service

Objective:

- maintain control of the main economic state
- commit civilian capacity
- avoid severe instability during the mission

Costs:

- temporary civilian factory burden
- political attention
- possible local resistance

Success:

- Government Capacity rises
- recurring state income and construction decisions open

Failure:

- currency and salary crisis
- corruption incident

### Register the Population

Objective:

- control anchor territory
- maintain local peace
- spend administrative capacity

Success:

- Legitimacy and Capacity rise
- manpower and local recruitment become more reliable

Failure:

- local leaders resist
- instability rises
- region-specific autonomy dispute may begin

### Hold the First Assembly

Objective:

- reach minimum legitimacy
- keep the capital secure
- choose delegates or constituency method

Success:

- constitutional route progresses
- government settlement becomes available

Failure:

- military, traditional, or radical faction receives an opening

### Confirm Traditional Authority

Alternative to the first assembly for suitable packages.

Objective:

- gain support from regional councils, chiefs, dynastic houses, clergy, or customary institutions
- avoid a rival claimant crisis

Success:

- traditional route gains legitimacy
- symbolic unity improves

Failure:

- succession dispute or provincial refusal

## Recognition decision family

### Send a Diplomatic Mission

Targets one country at a time.

Requirements scale with distance, route access, relations, and available diplomatic capacity.

Costs can include:

- convoys
- civilian factory burden
- fuel or transport access
- diplomatic credibility
- recognition debt to a patron

Outcomes:

- formal recognition
- informal liaison
- recognition with conditions
- refusal
- patron counteroffer

### Request Recognition from the Former Host

This is a major settlement action. It can open negotiations, trigger demands, or reveal that the host intends reconquest.

### Seek a Regional Guarantee

The target evaluates border threat, ideology, strategic interest, league membership, and patron rivalry.

### Accept Arms-Limit Recognition

The country gains recognition but accepts temporary limits on divisions, aircraft, fortification, or foreign bases.

### Build a Foreign Service

A multi-stage mission that upgrades recognition efficiency and reduces the cost of distant missions.

### Coordinate a Recognition Campaign

Available through the network or league. Several Event 6 countries jointly support one member.

## Government construction decision family

### Recruit the Civil Service

Sources can include:

- local officials
- returning exiles
- former-host administrators
- religious or customary institutions
- labor and cooperative organizations
- foreign technical missions

Each source changes patron influence, legitimacy, and route access.

### Standardize Law

The player chooses between inherited law, emergency decrees, regional autonomy, customary law integration, or a new constitutional code.

### Establish a Treasury and Currency

The route can use an independent currency, temporary use of the host currency, a patron currency link, a regional currency board, or barter and commodity backing in extreme conditions.

### Restore Communications

Targets railway, port, telegraph, river, or road connections according to region.

### Create Provincial Compacts

Reduces instability in broad or diverse countries. It can weaken central capacity or create future federal routes.

## Security and army decision family

### Integrate the Militias

Requires equipment, army experience, legitimacy, and command capacity.

Outcomes can be:

- regular army integration
- federal or regional guards
- retained autonomous militias
- demobilization
- failed integration and armed faction

### Seize or Secure a Depot

A map objective. The country must control the target and hold it with supplied units.

Success grants equipment and Security. Failure can give the former host a counterattack opportunity.

### Recall Defecting Officers

Improves command but may import host loyalties, ideological factions, or rival patron ties.

### Form Border Guards

Creates region-specific light units and border missions. Costs equipment, manpower, and command attention.

### Open a Volunteer Corridor

Requires a sponsor, neighbor, port, or league route. Uses convoys, trains, fuel, or diplomatic access.

### Raise Emergency Units

A limited crisis action. Unit count and quality scale with population, legitimacy, equipment, and chaos. Repetition increases instability and militia political power.

### Professionalize the Army

A mission family that converts militia templates over time rather than granting repeated free divisions.

## Former host decision family

### Offer a Ceasefire Line

Both parties freeze military positions and open border talks.

### Divide State Property

Settles railways, arsenals, ships, aircraft, debts, and public institutions.

### Negotiate Citizenship and Return

Handles refugees, residents, property, and migration without turning population groups into disposable modifiers.

### Accept Limited Claims

The new state renounces part of the ambition package in exchange for recognition or guarantees.

### Demand Recognition by Force

Requires security, legitimacy, and a route willing to risk war.

### Offer Association or Reunion

The host proposes autonomy, federation, personal union, or associated state status. Acceptance requires explicit player choice and a designed identity transition.

### Prepare Reclamation Defense

A timed mission triggered when host war preparation is detected.

## Patron decision family

### Accept an Arms Mission

Gains equipment and training. Creates arms influence and possible officer dependence.

### Accept Industrial Credits

Gains construction and industry support. Creates debt and investment influence.

### Invite Security Advisers

Improves counterintelligence or stability. Risks domestic legitimacy and patron control.

### Grant Base or Transit Rights

Powerful support with long-term sovereignty cost.

### Balance the Patrons

Requires at least two active sponsors. Reduces dominance but can slow aid and anger both sides.

### Buy Out a Concession

Uses civilian capacity, trade income, or league finance to reduce patron influence.

### Expose Foreign Interference

Can sharply reduce one patron's influence, but may also lose recognition, aid, and intelligence support.

### Choose a Client Future

A deliberate route commitment. It grants strong support and access to patron-linked focuses, leaders, laws, and military missions.

## League and network decision family

### Recognize a New Member

Low-cost solidarity action with diplomatic consequences toward its host.

### Send Civil Service Cadres

Improves another member's capacity and the sender's network standing.

### Contribute to the Emergency Reserve

Uses equipment, convoys, trains, fuel, or factories. Builds league reserve stock and cohesion.

### Request Collective Recognition

The network campaigns for one member.

### Request Border Arbitration

Members submit a dispute to a council. Acceptance improves cohesion. Rejection opens sanctions or exit pressure.

### Rescue a Threatened Member

Options include equipment, volunteers, guarantees, expeditionary forces, mediation, and sanctions.

### Convene a Congress

Begins the formal league formation sequence.

### Challenge League Leadership

Available to strong members with high standing. Failure can reduce cohesion or create a rival caucus.

## Border and claim decision family

Border content comes from the candidate package and regional overlay.

### Survey the Claimed Districts

Reveals public requirements and local conditions for ambition states.

### Sponsor a Plebiscite

Requires local support, control conditions, and outside observers or league arbitration.

### Negotiate a Transfer

Uses recognition, relations, guarantees, and compensation.

### Support Local Committees

Raises local support but risks host relations and foreign condemnation.

### Prepare a Border Ultimatum

Requires security and route commitment. Opens a timed crisis rather than an instant war goal.

### Integrate a Settled District

A post-transfer mission using administration, equipment, infrastructure, and local legitimacy.

## Formable decision family

Formables use shared stages.

1. Discover or assert the regional identity.
2. Build a political claim.
3. Meet territorial and member conditions.
4. Convene a congress, proclamation, coronation, union vote, or military settlement.
5. Form the country or apply the cosmetic identity.
6. Complete integration missions.
7. Resolve capital, constitution, army, and member autonomy.

Large formables grant claims first and cores through staged integration unless the participating regions voluntarily entered and the route has strong legitimacy.

## Signature transaction contract: IW-043 and IW-058

The 2026-07-18 signature tranche makes the shared formation model concrete for
the two Level 3 packages. This is a current implementation reconciliation for
the accepted design. It does not certify the wider Event 006 event.

### Paid congress and consent ledger

FORM-12 and FORM-13 are available only from the exact IW-043 carrier route.
Each requires three external sovereign Event 006 member packages, three
explicit consents, and three distinct anchors that the consenting members own
and control. FORM-18 uses the exact IW-058 carrier route and requires two
external members, two explicit consents, and two distinct controlled anchors.
Each family opens a paid 180-day congress with a frozen invitation ledger.
Human invitees answer through their authored reply events. AI invitees use the
route, threat, recognition, relation, autonomy, dispute, and instability
consent score. The terminal recount admits only consenting members and rejects
stale generations, invalid members, lost anchors, and duplicate anchors.

Failed or cancelled congresses consume committed costs, clear only the
matching carrier and family ledger, and apply the bounded retry cooldown.
Generic congress and commit decisions exclude these three signature families.

### Carrier identity and staged integration

Formation changes only the carrier's cosmetic identity. FORM-12 uses
`VOLGA_URAL_FEDERATIONX`, FORM-13 uses `IDEL_URAL_COMPACTX`, and FORM-18 uses
`MESOPOTAMIAN_FEDERATIONX`. Consenting members retain their tags, sovereignty,
Event 006 origin, territory, focus content, and units. Two post-congress
integration stages advance charter registration and defence or revenue work
for the frozen consenting members. They do not annex members, create subjects,
grant blanket cores, end member origin packages, or duplicate units.

FORM-18's military settlement method is gated before payment by a tracked
defensive former-host result, sovereign-anchor receipt, corridor-control
receipt, and the absence of an offensive-pretext marker. The negotiated method
does not need those military receipts. The sovereign-autonomy compact is a
mutually exclusive bilateral settlement mode. It records boundary,
protection, jurisdiction, transit, property, and security terms without
creating a client relationship. The final Mesopotamian settlement presentation
is written by the ratification focus after either the first federal integration
stage or the complete sovereign compact.

### Signature proof writers

The two IW-043 route proofs are mutually exclusive and have sole capstone
writers. The three IW-058 proof writers require the four-community guarantee
contract, the exact Mesopotamian settlement, and a tracked former-host conflict
or authored survival crisis. Client capture disqualifies the current IW-058
generation. Exact package cleanup clears all adapter, ledger, integration, and
proof receipts.

## High-chaos decision family

Only suitable packages and routes see these actions.

### Sponsor Another Breakaway

Uses influence, equipment, intelligence, and network standing to improve a future candidate's opening.

### Coordinate Reclamation Fronts

Several radical Event 6 countries synchronize border demands.

### Proclaim Open Sovereignty

Challenges the idea that existing borders or hosts have privileged legitimacy. It raises aggressive bloc pressure and danger milestone progress.

### Seize a Historical Capital

A high-risk mission for restoration routes. It must involve a named geographic objective, not a free claim.

### Transform the League Charter

Moves the league from mutual defense toward revolutionary or revisionist action. This can trigger the danger super-event.

## Decision clutter control

The category never shows every possible action.

Rules:

- only the current founding phase is expanded
- only one selected patron is shown to the human player at a time
- only one selected foreign recognition target is shown at a time
- border targets are grouped by region and route
- obsolete emergency decisions disappear after stabilization
- weaker decisions are replaced by mature versions
- active mission caps depend on Government Capacity
- AI can evaluate all valid targets without using the human selector
- invalid hosts, patrons, dead members, settled borders, and completed formables are cleaned up

## AI equivalence

Every human action has an AI path through decisions, weighted events, strategy plans, or periodic scripted evaluation.

The AI should not require the custom interface. It reads the same values and calls the same effect families.

## Dynamic costs and durations

No major family uses one flat political power cost.

Costs scale through:

- population and territory
- Government Capacity
- Security
- war state
- supply and infrastructure
- distance
- patron access
- chaos band
- previous success or failure
- active mission load
- league support
- local legitimacy

Durations use bands rather than one universal timer.

| Mission scale | Normal band | Examples |
| --- | --- | --- |
| Immediate emergency | 30 to 75 days | secure capital, stop coup, hold depot under attack |
| Early founding | 90 to 150 days | civil service, population registration, first assembly |
| Institutional | 150 to 270 days | treasury, army professionalization, foreign service |
| Diplomatic and border | 120 to 365 days | recognition campaign, arbitration, plebiscite |
| Formation and integration | 180 to 540 days | union congress, rail integration, provincial compact |

Dynamic factors can shorten or extend the band. Emergency timers remain rare and justified.

## Exploit controls

- emergency units use one-time pools, escalating costs, and template limits
- depot rewards require a real target and cannot repeat after depletion
- recognition cannot be farmed from the same country without a changed relationship state
- patron balancing cannot create infinite aid without influence consequences
- league reserves use contribution and withdrawal accounting
- formables cannot be repeatedly formed through cosmetic switching
- integration missions grant cores only once per state and origin
- voluntary reunion removes incompatible Event 6 decisions and origin-active content
- annexed countries cannot continue network actions
- AI cannot target nonexistent countries, dead hosts, settled borders, or impossible formables
