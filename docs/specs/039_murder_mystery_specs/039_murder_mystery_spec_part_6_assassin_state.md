# Murder Mystery Specification Part 6: Assassin State Country Package

## Country role

The Assassin State is the territorial form of Event 39. It appears when the hidden movement decides that assassination alone cannot dismantle organized government. It is a real fighting country with a viable economy, army, intelligence system, focus tree, decisions, AI, capital, supply, and defeat path.

`Assassin State` is the planning label. Player-facing country names should derive from the original host or occupied region. Examples of direction include `[Host adjective] Brotherhood`, `Brotherhood of [Region]`, or a route-specific public identity. Final localisation must be written during implementation.

## Identity boundaries

The country is a fictional high-chaos movement. It must not be represented as the Nizari Ismailis, a real religious community, a real ethnicity, or anarchism as a whole. Its imagery should use an invented broken-chair, severed-command-knot, empty-dais, masked-hand, or crossed-key motif. Avoid crescents, Alamut imagery, hashish legends, stereotyped Middle Eastern clothing, generic ninja costumes, and borrowed real extremist symbols.

The movement's public faction is provisionally named `The Veiled Compact`. The final terminal identity can shift toward a broader world brotherhood through route-aware localisation.

## Tag and carrier audit

No country tag is selected in this spec. Before implementation, audit vanilla, Chaos Redux, all installed Workshop reference mods, sibling local mods, protected dynamic carrier collections, and Event 006 or Soviet Collapse carriers. Reserve one compatible original Assassin State carrier only after the audit.

Foreign Assassin derivatives should use an existing bounded dynamic carrier framework when one can preserve origin, parent, and package identity. If no suitable framework exists, reserve a small audited pool with explicit maximum concurrent derivatives. Never allocate one fixed tag per possible country.

The tag audit must happen before flag, portrait, focus, country, or 3D asset production so runtime identifiers remain stable.

## Public political identity

The default government should use a dedicated Event 39 subideology inside the most compatible existing ideology group, likely non-aligned unless the live repository establishes a better shared pattern. The event does not need an entirely new global ideology family merely to express one country.

Working political elements:

- movement name direction: The Brotherhood
- ruling party direction: Brotherhood Council or Central Cell
- leader title direction: The First Knife, The Hidden Hand, or a route-specific office
- legislature direction: Assembly of Cells, Campaign Council, or no public legislature under the centralized route
- faction direction: The Veiled Compact
- subject identity direction: Regional Cell Administration, Brotherhood Territory, or local route name

The original murderer is wholly fictional. Once revealed, the portrait can use native ImageGen under the fictional high-chaos portrait route. The design should be memorable and grounded in 1930s to 1940s clothing and material culture. It should avoid a generic masked ninja face.

## Dynamic split goals

The original split must leave two playable countries. The Assassin State needs a defensible capital, connected territory where possible, population, industry, supply, and room to maneuver. The original government needs a capital, industry, population, supply, and a realistic path to resist.

The split should normally transfer 15 to 35 percent of the host's viable core territory. The exact share scales with Network Reach, cult maturity, host stability, host war state, current control, scenario intensity, and Chaos. Higher share does not automatically mean better movement balance because exposed territory and weak Cohesion can make a large revolt difficult to hold.

## State selection algorithm

### Candidate anchor filtering

A candidate anchor state must:

- be owned and normally controlled by the host or have an explicit occupied-state allowance
- be part of the host's viable core homeland or accepted event-owned integration area
- have population
- not be the host's current capital unless no alternative exists and a valid remnant capital is prepared
- not be protected by another active country or event transaction
- not be an isolated empty island unless the host is an archipelagic country and the cluster can remain viable
- have at least one useful adjacency, port, rail, supply, industry, or victory-point feature
- not create an impossible enclave after transfer

### Anchor scoring

Score anchors by population, victory points, military and civilian factories, infrastructure, rail access, supply hubs, ports, terrain, urban value, adjacency depth, distance from the host capital, local cell maturity, investigation failures, and current garrison weakness.

Select from the top few anchors with weighted variation. The split should replay differently without ignoring viability.

### Cluster growth

Grow the Assassin cluster through adjacent valid states. Each added state should improve population, industry, supply, defensive shape, or route access. Avoid thin snakes and scattered islands. Prefer a compact cluster with at least one internal connection to the capital.

### Remnant validation

After each proposed transfer, validate that the original government retains a capital or valid fallback, population, industry, supply, connected core territory where possible, and at least one route to fight. If the remnant fails, shrink or move the Assassin cluster.

### Final transaction

Only after both packages pass validation should the event transfer states, set capitals, create the country, apply cores or claims, assign stockpiles and units, initialize focus and decision state, and declare war. A failed final validation restores the preflight state and does not record Evolution III.

## Capital selection

The Assassin capital should favor:

- central position inside the transferred cluster
- urban or defensible terrain
- rail and supply access
- local movement maturity
- sufficient population and industry
- a strong visual identity for the public reveal

The host capital should remain with the original government when possible. If it falls inside the only valid Assassin cluster, the original government must receive a verified historical or strategic fallback capital before transfer.

Both capitals need later relocation rules. A captured Assassin capital should relocate to the best controlled connected state. A captured original capital follows the country's existing dynamic-capital system.

## Core and claim policy

The Assassin State receives provisional cores on its starting transferred states so it can recruit and function. It receives claims, not free cores, on the rest of the original host. Integration after conquest should use route-aware decisions and missions.

Foreign derivatives receive provisional cores on their revolt cluster. They do not receive automatic cores on the whole parent country. Central support and postwar route choices decide whether conquered land becomes a subject administration, staged integration, occupied territory, or a local decentralized cell system.

## Starting economy

The country inherits the real factories, resources, infrastructure, rail, ports, airbases, and supply in transferred states. It receives only bounded emergency adjustments needed to make the package viable.

Emergency support can include:

- one temporary off-map civilian or military capacity carrier that expires through focus or decision progression
- a small stockpile based on starting battalions and local capture
- trains, trucks, fuel, and convoys based on actual route needs
- temporary construction and repair capacity
- local workshop output for Assassin equipment
- a short consumer-goods or production strain representing clandestine conversion

Do not grant a fixed large factory package unrelated to transferred territory. The event should preserve the value of map selection and make small states solve real constraints.

## Starting laws and national spirits

The country should begin with no more than three deep Event 39 national spirits:

### Underground Becomes Government

Represents improvised administration, hidden stores, intelligence access, weak tax collection, and uncertain industrial control. It improves infiltration and local resistance support while penalizing ordinary state capacity. The focus tree can centralize, decentralize, or pragmatically replace it.

### Cells Under Arms

Represents elite cadres, low manpower use, strong organization, and a limited ability to form Assassin units. It also carries reinforcement, equipment, and formation-cap constraints. Military branches transform it. Permanent spirit stacking is prohibited.

### Leadership Is a Crime

Represents the movement's anti-hierarchy doctrine and its command contradiction. It affects Cohesion, legitimacy, officer recruitment, subject relations, and route access. Every political route resolves it differently.

Ordinary economic, trade, conscription, and mobilization laws should reflect the transferred economy, war state, ideology, and route. The country should not receive maximal laws for free.

## Starting technology

The Assassin State inherits a bounded technology set from the original host based on captured institutions, local industry, movement preparation, and date. It should normally receive:

- current or slightly reduced infantry weapons appropriate to the host
- support equipment and motorization needed by starting templates
- radio and reconnaissance capability
- basic industry, construction, and electronics appropriate to the date
- Event 39 Assassin doctrine and equipment unlocks already earned by evolution or scenario intensity
- no automatic advanced armor, aircraft, naval, nuclear, chemical, biological, or special-project technology

A captured-knowledge ledger should prevent both technology loss that makes the country unusable and total inheritance that erases the cost of state formation.

## Starting stockpiles

Stockpiles derive from starting formations, captured local depots, host equipment availability, movement preparation, scenario intensity, and transferred industry. Each stockpile should cover a defined opening period and leave production decisions meaningful.

Required categories include infantry equipment, support equipment, trucks, trains, fuel, and Assassin-specific equipment if the family uses it. Mechanized equipment appears only at later evolution or route gates.

## Starting army

The package creates a mix of custom and ordinary formations:

- several Assassin Cadre divisions scaled to transferred population and industry
- one Shadow Company or Silent Guard only when maturity and economy support it
- local irregular or ordinary infantry formations for holding fronts
- no Master Assassin or Mechanized Assassin unit before its unlock
- a reserve equipment and manpower path for reinforcement

The country must have enough units to hold a compact front but not enough to overwhelm the original host automatically. The relative starting force considers host division count, front length, transferred terrain, scenario intensity, and other wars.

## Army growth

Reinforcement comes through local recruitment, captured depots, clandestine workshops, cell volunteers, foreign support, subject levies, battlefield salvage, focus routes, and decisions. Custom units require real equipment and training. Free recurring unit spawns are tightly capped and tied to concrete cell or territory milestones.

## Commanders

The original murderer is a political leader, not automatically a field commander. The country receives one or more fictional high-chaos commanders through the approved portrait route only when the package needs them. Institutional command can be used instead of inventing several named people.

Commander traits should support infiltration, night operations, urban or rough-terrain action, reconnaissance, and rapid exploitation without granting universal combat superiority.

## Navy and air force

The country inherits ships and aircraft only through verified transferred ownership, captured bases, defections, or route content. It does not receive a generic navy or air force.

A coastal Assassin State can use sabotage, mines, small craft, port infiltration, and convoy raiding through ordinary or event-owned decisions. A landlocked state receives no token naval branch. Air development should focus on reconnaissance, liaison, interception support, and later conventional adaptation when industry allows.

## Intelligence agency

The Assassin State receives an intelligence identity even without La Résistance. With the DLC, it should have a real agency, appropriate upgrades, operatives, and operations tied to foreign cells. Without the DLC, equivalent decisions and hidden capacity provide the same core gameplay.

The country should excel at infiltration, target analysis, resistance support, and cell contact. It should be weaker at broad industrial espionage, decryption races, and expensive global operations until the focus tree invests in them.

## Domestic politics and Cohesion

The movement has three internal political answers:

- centralized command under the revealed leader
- decentralized cells with autonomous local authority
- pragmatic temporary state institutions for survival

Brotherhood Cohesion is the common pressure. Centralization improves military command and subject control while strengthening accusations that the movement has betrayed its doctrine. Decentralization improves cells and resistance while weakening production, supply, and synchronized war. Pragmatism improves ordinary administration and diplomacy while reducing radical recruitment and terminal-route support.

## Subject and faction behavior

At Evolution IV, the central Assassin State creates or leads the Veiled Compact. Foreign Assassin derivatives become subjects and members. The central state can coordinate operations, send equipment, demand intelligence, transfer cadres, and arbitrate local leadership.

The faction requires real goals, membership rules, expulsion or defection behavior, shared decisions, cohesion consequences, and postwar handling. Ordinary countries cannot join merely because relations are high. A country must be an Event 39 derivative or follow an explicit high-chaos conversion route.

## Diplomacy

Before Evolution IV, ordinary governments should treat the Assassin State according to war alignment, evidence, ideology, and public murders. The state may receive covert sympathy or opportunistic aid, but normal diplomatic recognition should be difficult.

The pragmatic route can seek limited recognition, trade, nonaggression, or temporary alliances. These agreements create Cohesion and legitimacy costs. The centralized and decentralized routes rely more on covert networks, subjects, and captured resources.

## Defeat and capitulation

If the original host defeats the Assassin State before Evolution IV, the country is dismantled, its leader is captured, killed, or lost according to the final battle state, and surviving cells enter a cleanup campaign. A complete defeat can end Event 39 when no mature foreign cells survive.

If the Assassin State defeats the original host, it gains the movement's core homeland objective, inherits or dismantles relevant host institutions, and begins staged administration. It does not receive instant free cores on all conquered land. The original government's exile or successor handling follows existing country systems.

If the Assassin State capitulates after Evolution IV, the movement inheritance test in Part 5 runs once. Foreign subjects can defect, seek autonomy, surrender, or support a viable heir.

## Playability after terminal victory

World of Anarchy victory does not remove the player's country. The central movement retains a playable command shell and faces a post-victory contradiction. Route outcomes can create autonomous territories, temporary campaign councils, or a hidden central administration. The final state must have economy, units, decisions, and a clear end-state presentation. The campaign must continue responding.

## Country package acceptance

The Assassin State package is accepted only when tag safety, territory, capital, cores, claims, population, economy, laws, technology, stockpiles, units, commanders, focus loading, decisions, agency behavior, DLC branches, AI, diplomacy, subjects, faction, flags, portraits, 3D consumers, defeat, inheritance, and cleanup have all been specified and implemented without placeholders or generic empty-tag fallbacks.
