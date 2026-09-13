# Event 55 Specification, Part 2

## Geographic Candidate Generation

## Purpose

The proposal system turns the selected country's current map, economy, diplomacy, and logistics into a short list of plausible megaprojects.

The player should not receive generic buttons called railway, highway, or port. A proposal should have a real route or facility footprint and a clear reason for existing. A railway may connect a remote mineral state to a steel-consuming industrial region. A highway may connect a capital to a distant frontier. A port may serve a large naval base, an island supply network, or an international freight route.

Candidate generation can use detailed hidden scoring. Its output must remain simple. The normal player sees three proposals from different families, each with a clear map purpose.

## Proposal set size

A normal proposal set contains three candidates.

A fourth candidate can appear only when a later evolution unlocks a rare project family and the normal set would otherwise hide it. This fourth candidate should replace a weaker ordinary proposal whenever possible. It should not become a permanent extra row.

When the country has reached its active project limit, new project proposals should hide. The category should show active missions, urgent repairs, and one survey-management action instead of letting the player queue projects it cannot begin.

When a project slot opens, the stored valid proposals return or the system generates a fresh set if the old routes are no longer valid.

## Candidate diversity

The generator should prefer one proposal from each of three broad roles:

- national integration or military logistics
- economic extraction or trade
- a geography-specific opportunity

Examples of a diverse set include:

- a continental railway
- a resource corridor
- a grand port

or:

- a strategic highway
- an international trade corridor
- a major bridge unlocked by Evolution II

The same project family should not occupy two rows in one proposal set unless fewer than three families are valid. A duplicate family should still use a different strategic purpose and route footprint.

## Candidate lifecycle

A proposal has its own generation identity. It remains valid until one of these events occurs:

- the player authorizes it
- the proposal refresh cooldown ends and the player orders a new survey
- a critical state changes owner or controller
- a required partner becomes invalid or refuses the route
- the relevant port, resource area, or crossing no longer exists in a usable form
- a new evolution changes the candidate family pool
- another completed project makes it redundant
- the host loses the ability to supervise the project

A proposal should not reroll every day or every time the category opens. Stable proposals let the player plan.

## Proposal refresh

The category includes a bounded survey action that replaces the current proposal set.

The survey action should require a reasonable bureaucratic and material commitment. Political power fits part of the cost because ministries, land rights, and planning approval are political tasks. It should also consume a small amount of support equipment, trucks, trains, or convoys according to the country and expected candidate pool.

Suggested cooldowns:

| Event state | Normal survey refresh cooldown |
| --- | --- |
| Baseline | `180` days |
| Evolution I | `120` days |
| Evolution II | `90` days |
| Evolution III | `60` days |

An invalidated proposal set refreshes automatically without charging the player. The paid survey action is for replacing still-valid proposals.

The survey action should not be available when it would produce no useful change, when all project slots are occupied, or when the country lacks any valid candidate family.

## Candidate record

Every generated proposal should preserve enough information to remain stable and to become a persistent project if authorized.

The conceptual record contains:

- proposal generation identity
- project family
- host country
- origin node
- destination node
- route states or critical facility state
- required crossing token when relevant
- proposed partner countries
- industrial, military, relief, trade, or resource purpose
- difficulty band
- duration band
- phase cost profile
- risk profile
- expected permanent effect family
- candidate score explanation for internal audit

These fields are design requirements. The implementation can store them through arrays, variables, event targets, flags, or other safe event-owned structures.

## Node selection

Projects should begin and end at meaningful nodes.

Eligible origin and destination nodes include:

- the capital state
- a high-industry state
- a high-population state
- an important naval base
- a coastal state with strong trade value
- a state containing important resources
- an isolated state group
- a supply hub or major rail junction
- a distant land border
- an allied capital or industrial region
- a state under active famine or migration pressure when a relief route is relevant

A node should be selected because it creates a useful route. Population, industry, resources, ports, supply, distance, terrain, and strategic isolation can all contribute to hidden scoring.

The system should avoid choosing a node that is already well served by a completed Event 55 project unless the new proposal clearly extends the network.

## Route construction

The route between origin and destination should use connected states where the engine and map can prove continuity.

A route can cross:

- states owned and controlled by the host
- states owned by willing partner countries
- subject territory when the autonomy relationship allows the host to negotiate and operate the route
- allied or faction territory when the owner explicitly accepts the project

A route cannot silently use:

- hostile territory
- neutral foreign territory without consent
- a sea gap without a registered crossing or maritime segment
- an impassable state connection
- territory owned by an invalid special actor
- a segment whose continued operation cannot be checked

When several valid routes connect the same nodes, the generator should consider length, terrain, border count, current rail coverage, supply demand, political reliability, and strategic exposure.

The shortest route is not always the best route. A slightly longer domestic route can be preferable to a short route through a hostile or unstable transit country.

## Route length bands

Project scale should use bands rather than exposing exact internal distance math.

| Working band | Route character | Typical use |
| --- | --- | --- |
| Local grand work | One key state or a short two-state connection | Port complex, bridge, metropolitan link, resource spur |
| Regional corridor | Several connected states | Industrial to port route, frontier highway, national rail spine |
| National trunk | Distant parts of one country | Coast-to-coast route, capital to remote resource area |
| Continental route | Very long route or several large countries | Transcontinental railway, multinational freight corridor |
| World network segment | One component of an Evolution III system | Continental network, linked port chain, strait sequence |

Length affects duration, civilian burden, equipment requirements, incident exposure, and final benefit. It should not simply multiply every cost without a cap.

## Terrain difficulty

Terrain changes the project type and risk.

Important terrain factors include:

- mountains
- hills
- deserts
- jungle
- marsh
- arctic or severe winter regions
- major rivers
- islands and straits
- dense urban regions

At baseline, the generator should avoid a route dominated by extreme terrain when a reasonable alternative exists.

Evolution I allows more difficult rail and highway routes. Evolution II unlocks deliberately extreme engineering through terrain that would normally disqualify a proposal. Evolution III can combine several difficult segments when the network value justifies them.

Terrain should influence the visible proposal summary. The player should understand that a mountain crossing is slower and riskier without reading raw terrain weights.

## National integration score

A railway or highway proposal gains national integration value when it connects:

- opposite coasts
- the capital to a distant border
- separate industrial regions
- an isolated state group to the national network
- old territory to newly integrated territory
- distant supply hubs
- a large population center to a national port

The score should rise with distance and isolation, then fall when the route duplicates an existing Event 55 project.

A project should not be selected only because the country is large. It needs meaningful endpoints.

## Military logistics score

A proposal gains military logistics value when it connects:

- the capital or main industrial region to an active front
- a major port to a supply hub
- a vulnerable frontier to the national rail network
- an isolated army region to a secure rear area
- a theater with poor rail access to a production center

Wartime need can increase the score, but a country under immediate collapse may lack the capacity to begin a grand project. The AI should distinguish an urgent but feasible lifeline from a fantasy project started during defeat.

Military scoring must not turn every candidate into a front-line route. Peaceful economic countries should still receive trade, integration, and resource proposals.

## Resource score

A resource corridor gains value when a remote resource state has one or more of these conditions:

- weak railway access to the capital or industrial center
- no strong route to a port
- high resource output with low local industry
- strategic resources that the host imports despite owning deposits
- a new discovery from Event 18
- difficult terrain that currently isolates extraction

The resource corridor should link the source state to a real destination, usually an industrial region, supply hub, or export port.

The generator should not create new deposits without a separate source. It improves access, extraction conditions, and route capacity around existing resources or a valid Event 18 discovery.

## Port score

A grand port proposal gains value when the candidate coastal state has:

- a strong position on a major sea route
- a large existing naval base that can be expanded
- an industrial or resource hinterland
- island supply responsibility
- convoy congestion or overseas military demand
- allied trade corridor potential
- poor rail connection to the interior

The generator should avoid placing a grand port in a minor coastal state with no strategic or economic reason when a better site exists.

A country with no coast cannot receive a grand port unless it gains one before the proposal refreshes.

## International corridor score

An international corridor needs more than adjacency.

It gains value from:

- friendly relations
- faction or alliance links
- active trade interest
- complementary industry and resources
- a shared threat
- existing rail or port nodes that can be joined
- a need to bypass hostile transit
- famine or migration pressure that makes a humanitarian route valuable

It loses value from:

- war or active claims between partners
- embargoes
- hostile ideology combined with low trust
- unstable control of border states
- repeated partner withdrawal
- a route that gives almost all benefits to one country

A candidate should not appear as ready for authorization before the likely partners have at least a plausible reason to negotiate.

## Strait and fixed-link score

A bridge or tunnel candidate requires a registered crossing token that proves all of these facts:

- the two terminal states are geographically suitable
- the crossing is narrow enough for the event's evolution level
- the map can support a real strategic connection
- ownership and control of both approaches can be checked
- shipping and naval behavior have a defined treatment
- the route has a valid permanent or toggled engine consumer

The generator must never infer a fixed link from simple visual proximity on the map.

A valid crossing can favor a bridge, a tunnel, or a hybrid design according to shipping lanes, air approaches, terrain, route length, and engineering evolution.

## Candidate score composition

Each project family can calculate a hidden score from common factors:

- strategic value
- economic value
- integration value
- relief value
- route length suitability
- terrain difficulty
- partner reliability
- construction feasibility
- duplication penalty
- active war risk
- evolution access
- project family diversity

The final proposal pool should use weighted selection among candidates that have already passed hard validity checks.

A low score should reduce selection chance. It should not rescue an invalid route.

## Hard validity and soft preference

The design separates hard validity from soft preference.

Hard validity answers whether the project can exist. Examples include a real coast, connected route states, a valid crossing token, a living partner, and a free project slot.

Soft preference answers whether this valid project is currently attractive. Examples include high trade value, supply need, friendly relations, or strong civilian industry.

This separation is important for AI and testing. An invalid bridge must have zero chance. A valid but expensive bridge can remain in the candidate pool with a low score.

## Proposal summary

Each proposal should communicate:

- the route or facility location
- its strategic purpose
- its project family
- the expected duration band
- the initial authorization costs
- the later cost categories that can arise
- the National Works Capacity threshold
- the construction method choices
- the main permanent benefit
- the main failure or disruption risk

The summary should not list every hidden score or future incident.

Dynamic localisation should name the actual states, ports, resources, and partner countries.

## Proposal map feedback

The player should receive map feedback when inspecting a proposal.

Preferred presentation includes:

- highlighting the origin and destination states
- highlighting critical route states where supported
- centering the map on the route or facility
- a concise tooltip that names the route

The proposal should not require a full custom map GUI. Existing decision targeting and map highlighting are enough if they show the route clearly.

## Candidate generation performance

Generation occurs at bounded moments:

- first Event 55 firing for a country
- a paid survey refresh
- automatic replacement of an invalid proposal set
- project completion or abandonment
- evolution activation
- a direct integration event such as a new Event 18 resource discovery

The system should not rescan every country or every state each day.

Countries with Event 55 can use a sparse registered owner list for monthly capacity refresh and active project processing. Route updates should prefer event-driven notices from state control changes, project incidents, disaster adapters, and embargo adapters.

## Candidate acceptance criteria

A generated proposal is acceptable only when:

- its family is unlocked
- its host is valid
- its origin and destination are meaningful
- its route or facility footprint is proven
- its benefits fit the selected nodes
- its costs and duration reflect scale and terrain
- its partner list is valid
- it is not a near duplicate of a completed project
- it can become a persistent project object without losing its scope references
- it can be invalidated and cleaned up safely
- its player-facing summary can name the actual geography
