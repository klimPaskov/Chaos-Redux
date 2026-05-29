# Soviet Union Collapse Final Clean Merged Specification, Part 5
# Republic Focus Trees, Route Architecture, and Focus Quality

## Universal focus-tree rules

Every playable or long-lived Soviet Collapse country must have a real focus tree or a documented additive tree integration when it already exists and should not be replaced.

Every focus tree must have at least three distinct branch families:

- political branch
- industry branch
- expansion branch

These are the minimum, not the full design for important countries. Major countries should usually also have military, diplomacy, internal faction, intelligence or security, special mechanic, and late-game branches.

The implementation agent owns exact focus count, final names, final coordinates, and detailed prerequisites. The final tree must preserve the route families, route locks, mutual exclusions, mechanics, rewards, AI behavior, idea lifecycles, decisions, missions, and visual identity from this package.

## Branch depth and interaction

A branch does not count unless it changes gameplay.

A real branch should usually include:

- several focuses or focus groups
- a mechanical unlock
- a meaningful choice, lock, fork, or route consequence
- interaction with decisions, missions, ideas, leaders, units, buildings, diplomacy, map changes, AI, or events
- a clear payoff

Branches should not be isolated columns. Political choices should alter expansion, industry, military, diplomacy, and decision paths. Industry should support military or expansion. Expansion should create political consequences. Diplomacy should affect aid, war, factions, and sponsor risk.

## Branch payoff

Every major branch needs a payoff.

Political payoff examples:

- new government
- leader change
- ideology change
- ruling party change
- laws
- councils
- party names
- cosmetic names
- flags
- advisor roster
- legitimacy system

Industry payoff examples:

- rebuilt economy
- arsenal network
- resource system
- railway authority
- construction mechanic
- production routes
- map construction program

Expansion payoff examples:

- claims
- cores
- war goals
- protectorates
- leagues
- federation
- reunification
- liberation order
- regional settlement
- external war plan
- postwar integration

Military payoff examples:

- command structure
- doctrine
- special forces
- defensive network
- reserve system
- offensive system

Diplomacy payoff examples:

- recognition
- neutrality
- sponsor alignment
- balanced sponsorship
- anti-puppet protection
- faction creation

## Focus rewards

Focuses should unlock gameplay, not only stats.

Use varied rewards:

- civilian factories
- military factories
- dockyards
- forts
- coastal forts
- anti-air
- radar
- airbases
- infrastructure
- railways
- supply hubs
- resources
- building slots
- production lines
- equipment
- unit templates
- route-specific units
- manpower recovery
- commanders
- advisors
- advisor discounts
- laws
- technologies
- decisions
- timed missions
- claims
- cores
- war goals
- leader changes
- party popularity
- ruling party changes
- cosmetic names
- flag changes
- faction mechanics
- local leagues
- foreign aid mechanics
- crisis value changes
- achievement tracking
- events

Avoid focus trees where most focuses grant a new idea, political power, stability, war support, small flat modifiers, one civilian factory, one military factory, one anti-air, or generic equipment.

One-time rewards are allowed when they fit, but they should not be the main pattern. Important focuses should often unlock systems, decisions, missions, mechanics, advisors, production routes, or long-term branches.

## Idea lifecycle and remove-idea cleanup

New countries should start with a few meaningful negative or mixed ideas, not a large positive stack.

Common starting problems:

- broken administration
- improvised command
- disputed legitimacy
- supply confusion
- militia fragmentation
- foreign temptation
- regional rivalry
- old movement pressure
- ruined industry
- factional mistrust

Ideas should have lifecycles:

- starting negative or mixed form
- mitigated form
- route-specific upgrade
- failure or corruption form
- final form or removal

Do not create a new idea in every focus. When an idea already represents an institution, later focuses should modify, upgrade, replace, temporarily strengthen, worsen, or remove it.

Do not expose repeated remove-idea lines in focus tooltips. Use hidden effects, scripted effects, custom effect tooltips, or idea-upgrade helpers so focus hovers remain readable.

## Unique focus icons

Every focus must have a unique icon assignment.

Do not use one generic icon for many focuses. Icon families can be reused only when each focus still has a distinct variant or clearly appropriate unique sprite.

Every focus icon must match the focus identity and reward. A focus called air defense should not use a generic factory icon. A focus that unlocks a leader should not use a railway icon. The focus title, description, reward, and icon must tell the same story.

Update the asset manifest with focus icon assignments. Create missing focus icons through the asset workflow.

## Focuses and decisions

Focuses and decisions must be interconnected.

Focuses should unlock, modify, improve, or restrict decisions and missions.

Examples:

- expansion focuses unlock declarations, ultimatums, league votes, protectorate demands, border settlement decisions, war-preparation missions, and postwar integration decisions
- industry focuses unlock factory construction, rail repair, supply hub expansion, anti-air construction, airbase construction, fortification, resource extraction, and infrastructure programs
- military focuses unlock reserve mobilization, special unit training, template conversion, depot seizure, border defense, and offensive planning
- diplomacy focuses unlock recognition missions, aid corridors, advisor missions, volunteer requests, anti-puppet clauses, sponsor-balancing decisions, and foreign investment
- political focuses unlock elections, councils, purges, compromises, advisor appointments, party campaigns, reform missions, and leader changes
- League or faction focuses unlock shared reserves, common front missions, member votes, joint declarations, intervention forces, and arbitration

Decision categories should evolve with focus progress. They should not show every possible action at once.

## Political depth

Large focus trees must alter politics.

Political routes should include:

- ideology shifts
- ruling party changes
- party popularity changes
- leader changes
- new advisors
- advisor discounts
- laws
- internal faction decisions
- balance of power or equivalent mechanics where needed
- councils, congresses, juntas, committees, regencies, cabinets, or directorates
- cosmetic names
- flag changes
- AI strategy changes
- diplomacy behavior changes

A country should not remain politically static unless it is intentionally fixed by concept.

Fixed-purpose chaos countries can have narrower ideology only when the identity demands it, such as a death-state, machine-state, plague-state, or pure destruction actor. Even then, they still need internal choices around method, hierarchy, economy, recruitment, expansion, and endgame.

## Expansion branch

Every large focus tree must have a distinct expansion, liberation, reunification, settlement, federation, protectorate, or regional ambition branch. It must be separate from the main political branch and separate from the industry branch.

Expansion should include consequences and postwar handling:

- claims
- cores
- war goals
- protectorates
- guarantees
- leagues
- declarations
- ultimatums
- border incidents
- peace events
- state transfers
- integration missions
- occupation choices
- resistance risk
- diplomacy reactions
- faction consequences
- achievement tracking

Do not use a simple claim ladder with no politics or aftermath.

## Industry branch

Industry branches should be geographically grounded where possible.

They should define relevant states or regions for:

- factories
- resources
- ports
- railways
- supply hubs
- forts
- anti-air
- airbases
- dockyards
- infrastructure
- production lines

Industry branches should create map or production changes, not only country-wide modifiers.

## Route visibility and pacing

A major route should leave visible evidence: map changes, decisions, units, advisors, leaders, flags, cosmetic names, faction behavior, focus availability, diplomacy, or visible mechanics.

Large trees should have early, middle, and late pacing.

- early: survival, first institutions, first units, first industry, basic identity
- middle: route mechanics, real choices, decision families, military systems, diplomacy
- late: major payoffs, expansion, leagues, high-chaos branches, postwar settlement, world-order ambitions

Every major route needs a tradeoff and failure state. A military route may reduce legitimacy. A foreign-aid route may create dependency. Expansion may create backlash. Industry may cost civilian capacity. High-chaos paths may damage normal politics.

Do not overuse mutual exclusions. Mutually exclusive paths should represent identity changes, strategic commitments, or incompatible institutions.

## Republic focus tree requirements

### Ukraine

Ukraine must have a large, replayable tree with:

- emergency Kyiv state survival
- democratic Rada republic
- sovereign socialist republic
- military directory
- grain and industry
- Dnieper and Donbas logistics
- Black Sea and port branch
- foreign influence
- Free Republics' League leadership
- Black Sea ambition
- Black Banner and rural old movement branch
- high-chaos Bread State path

Ukraine should not play the same on democratic, socialist, directory, League, expansionist, and high-chaos routes.

### Belarus

Belarus must feel like rail, forest, corridor, and logistics country.

Required paths:

- Minsk emergency authority
- legal restoration
- rail sovereignty
- forest defense
- foreign corridor diplomacy
- League logistics command
- Pale Railway or forest high-chaos route

### Kazakhstan

Kazakhstan must be a steppe, resource, rail, and Central Asian pivot.

Required paths:

- steppe emergency authority
- Alash restoration
- socialist steppe republic
- military district state
- resource and rail economy
- southern cascade
- Central Asian League leadership
- foreign mediation
- Basmachi and high-chaos steppe pressure

### Baltic republics

Estonia, Latvia, and Lithuania require country-adapted trees with:

- legal restoration
- coast and forest defense
- foreign recognition race
- Baltic League
- exile or underground support
- anti-puppet clauses
- intervention pressure against Moscow

### Caucasus republics

Georgia, Armenia, and Azerbaijan require country-adapted trees with:

- national council route
- mountain or border defense
- oilfield and infrastructure route where relevant
- Turkish and Iranian mediation
- Caucasus League
- loyalist garrison issue
- high-chaos or restoration pressure where relevant

### Central Asian republics

Uzbekistan, Turkmenistan, Tajikistan, and Kyrgyzstan require country-adapted trees with:

- local council authority
- southern defense
- old movement or Basmachi pressure
- foreign mediation
- cotton, water, rail, pass, or resource economy
- Central Asian League
- high-chaos or ancient pressure where relevant

### Moldova

Moldova requires:

- Chisinau council route
- Dniester defense
- Romanian diplomacy
- Ukraine border settlement
- agrarian and river economy
- League observer path
- high-chaos Dniester route

### Karelia and internal republics

Karelia, Komi, Idel-Ural or Tatarstan, Bashkiria, North Caucasus or Mountain Republic, Crimea, Siberian Regional Authority, Far Eastern Republic, Yakutia, Buryatia, and Tuva require compact but meaningful trees with crisis government, local defense, economy and logistics, foreign or regional influence, League or local compact route, late-game settlement, and special or high-chaos route where supported.

## Focus tree completion proof

For every major tree, provide a route coverage table:

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |

Also report before and after focus counts, duplicate focuses removed, duplicate ideas removed, unique focus icon coverage, AI behavior, localisation, and route decisions.
