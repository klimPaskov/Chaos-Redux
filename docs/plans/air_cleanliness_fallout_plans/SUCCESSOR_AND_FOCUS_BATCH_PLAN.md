# Successor and Focus Batch Plan

## Purpose

Turn the 99-country candidate matrix into a controlled implementation program. The matrix is a pool of possible identities, not a list that must all exist in one campaign. The world rewrite selects a coherent set from campaign geography, state survival, tag availability, cause memory, player reservations, and performance limits.

## Country selection layers

Every implemented country package is built from three design layers.

### Archetype skeleton

Defines the country’s core survival loop, government logic, military structure, and late-game role.

The accepted matrix contains twelve archetypes. Final internal ids must match the source matrix.

Typical archetype responsibilities:

- starting crisis value
- basic survival decisions
- political route family
- military recruitment style
- industry and salvage model
- diplomacy behavior
- late-game ambition
- AI baseline

### Regional overlay

Defines geography, climate, historical memory, resource profile, local institutions, and neighboring rivals.

Regional overlay responsibilities:

- state and resource interactions
- local expansion direction
- regional diplomacy and faction logic
- region-specific decision families
- terrain and supply adaptations
- regional visual motifs
- regional AI targets

### Country memory overlay

Defines why this specific successor exists and what it remembers from the old world.

Country memory responsibilities:

- specific founder or institutional body
- old capital, movement, military district, industrial complex, port, bunker, religious center, university, mine, or refugee corridor
- unique starting idea and lifecycle
- one real country-specific branch
- named rivals and allies
- unique incidents
- identity transformation
- unique asset requirements

A package is incomplete without all three layers.

## Tag conflict ledger

Create a repository ledger before selecting the pilot batch.

Required columns:

| Field | Purpose |
| --- | --- |
| candidate id | stable matrix row identifier |
| candidate working name | internal planning reference |
| region | regional overlay |
| archetype | skeleton assignment |
| proposed source tag | base tag, releasable, dynamic tag, or existing Chaos tag |
| source tag current owner | vanilla, DLC, Chaos event, or unused |
| current package files | focus, history, character, idea, flag, localisation, AI, decisions |
| coexistence rule | can appear with current package or requires exclusivity |
| cosmetic tag ids | visible successor identities |
| state package | exact and fallback state groups |
| capital and fallback | valid state ids after grade check |
| player eligibility | whether it can be offered to a former player |
| dynamic tag cost | whether it consumes dynamic pool capacity |
| asset status | planned, in progress, complete, blocked |
| focus status | planned, implemented, audited |
| country audit status | not run, findings open, passed |
| implementation batch | pilot or regional wave |

Do not assign a tag because its three-letter code looks convenient. Record every existing use first.

## Tag strategy order

Use the least disruptive valid identity method.

1. Surviving old tag with a Fallout cosmetic identity.
2. Existing releasable that is valid for the territory and not needed elsewhere.
3. Existing Chaos Redux tag whose current feature package is explicitly compatible or inactive in Fallout mode.
4. Civil-war or dynamic tag after dynamic pool capacity is verified.
5. New base tag only when the identity cannot be represented safely by the other methods.

Cosmetic tags are preferred for visible variation. One country can only hold one cosmetic tag at a time, so route and puppet variants need an explicit priority system.

## Existing Chaos tag pool

The current repository registers general Chaos tags and a large Soviet Collapse successor set. These tags are not automatically free.

Reuse rules:

- ZZZ, ZIN, REV, and DTH retain their existing event ownership unless a specific Fallout compatibility route is designed.
- Soviet Collapse successors may persist into Fallout when their state package survives and their existing identity fits the matrix.
- A Soviet Collapse tag may receive a Fallout cosmetic form and Fallout tree only after its old package lifecycle is recorded.
- A tag cannot be reused for an unrelated region merely because Fallout is terminal.
- Event-created nonhuman tags remain registered in shared special-country triggers.

## State package design

Every successor needs:

- primary state group
- reduced fallback group
- optional expansion claims
- capital candidates in priority order
- minimum population and survival value
- minimum connected territory or maritime access
- forbidden wasteland share
- neighbor and overlap rules

State selection runs after grading.

A candidate is valid when:

- at least one capital candidate is below the terminal grade
- enough population or special infrastructure survives
- the state group does not conflict with a higher-priority player reservation
- a valid source tag is available
- the package has a focus and country implementation for the current build

Do not spawn a country whose content is not implemented.

## Pilot batch

### Size

Twelve countries, one per archetype.

### Regional spread

Use several regions. Do not implement all twelve pilots in one continent. A useful spread might include:

- two North American packages
- two European packages
- two Eurasian interior packages
- one East Asian package
- one South Asian package
- one Middle Eastern or North African package
- one Sub-Saharan African package
- one Latin American package
- one maritime or island package

Final choices depend on tag and state validation.

### Pilot purpose

The pilot proves:

- old-government survival
- cosmetic transformation
- new successor creation
- dynamic starting forces
- shared focus composition
- country-memory uniqueness
- player continuation
- AI survival behavior
- regional diplomacy
- asset production throughput

Do not choose twelve nearly identical military warlords. The batch must exercise every archetype.

## Country package implementation order

For each country:

1. finalize source tag and state package
2. create or verify cosmetic identity
3. define capital and fallback capital
4. define leader or institutional body
5. add starting politics and party names
6. add starting ideas and lifecycle
7. add survival mechanic values
8. add starting unit templates and dynamic force count
9. add reinforcement and mobilization decisions
10. implement archetype focus skeleton
11. add regional overlay
12. add country memory branch
13. add route-specific decisions and missions
14. add AI strategy
15. add localisation
16. complete flags, portraits, icons, and report assets
17. update docs and matrix row
18. run country and focus audits

A country does not enter the active rewrite pool until all required implementation and asset surfaces are ready.

## Starting forces

Starting forces scale from:

- surviving population
- surviving depots and factories
- surviving old divisions
- command cohesion
- archetype
- local support
- foreign or old-world military memory
- state supply and terrain
- scenario intensity

Unit families may include:

- local defense committees
- surviving regular formations
- railway guards
- factory guards
- bunker security troops
- mountain and mine detachments
- port and sailor formations
- refugee militias
- technical corps
- fictional mutant formations under explicit route gates

Every fighting country gets:

- at least one valid template
- initial equipment and manpower source
- a commander or institutional command rule
- supply assumptions
- a reinforcement pathway
- AI use rules

Do not use repeated free division rewards as the main growth model.

## Starting idea lifecycle

Every package begins with a small number of deep ideas.

Recommended structure:

- survival crisis
- government legitimacy or command problem
- regional strength or resource identity
- optional special archetype condition

Each idea has:

- starting form
- mitigation path
- route-specific upgrade
- failure or radicalization form
- final form or removal condition

A large stack of unrelated modifiers is not acceptable.

## Focus composition architecture

## Option A: verified shared-focus composition

Use root-level shared focuses for reusable archetype and regional branches.

Each country tree contains:

- at least one non-shared country anchor
- archetype shared branch root
- regional shared branch root
- country-memory focuses
- country-specific layout offsets and route gates

Advantages:

- reuse of tested core logic
- easier archetype balance updates
- less duplicate scripting

Risks:

- missing shared focus can crash at load
- shared prerequisite chains can pull unexpected nodes
- global focus ids can collide
- layout can become tangled
- country-specific localisation and rewards may become generic

Required proof:

- one prototype tree loads with all three layers
- a second country using the same archetype receives distinct memory content
- completed focus behavior remains correct after runtime `load_focus_tree`
- hidden and route-locked branches do not leak

## Option B: compiled full trees

Build a reviewed full tree per country from reusable design modules.

Advantages:

- exact layout and route control
- straightforward country-specific localisation
- fewer shared-focus dependency crashes

Risks:

- more files and repeated logic
- balance updates can drift
- temptation to bulk-generate shallow copies

Mitigation:

- reusable scripted effects and triggers
- shared constant tables
- manual route coverage review
- country-specific decisions and memory branch

## Selection rule

Choose Option A only after the pilot proves it safe and readable. Otherwise use Option B. Do not force shared focuses merely to reduce file count.

## Minimum tree depth

Every long-lived active successor receives a real tree with:

- opening survival and government formation
- political route family
- industry, shelter, food, and logistics branch
- military branch
- diplomacy and recognition branch
- expansion, federation, protection, or regional ambition branch
- archetype special mechanic branch
- country memory branch
- late-game reconstruction or domination branch
- high-chaos or mutant route when supported

Fixed-purpose chaos countries may have narrower ideology, but still need choices about hierarchy, recruitment, economy, expansion method, and endgame.

## Country memory branch standard

The memory branch must include:

- several focuses or focus groups
- one mechanic or decision unlock
- one unique event family
- one idea lifecycle or institution
- one visible identity change or regional consequence
- AI behavior
- late payoff or failure state

Examples of valid memory anchors:

- surviving hydroelectric complex
- naval refuge fleet
- mountain observatory
- religious sanctuary network
- railway junction authority
- old parliament in exile
- mining federation
- civil defense bunker complex
- refugee agricultural belt
- surviving university and reactor complex

These are category directions, not final country names or localisation.

## Regional overlay standard

Every region adds real play differences.

Possible regional systems:

- North America: interstate corridors, silo belts, federal remnants, Great Lakes routes
- Europe: dense wasteland borders, old capitals, river corridors, fortified industrial belts
- Eurasian interior: rail lifelines, steppe mobility, mining settlements, extreme winter
- East Asia: coastal megacity ruins, mountain refuges, river agriculture, surviving military districts
- South Asia: monsoon disruption, river basins, high population pressure, mountain corridors
- Middle East and North Africa: water control, desert survival, oil infrastructure, pilgrimage routes
- Sub-Saharan Africa: lower direct strike density in some worlds, river and rail corridors, agricultural adaptation, old colonial infrastructure
- Latin America and the Caribbean: mountain refuges, ports, food exports, naval routes, fragmented old capitals
- Oceania and remote islands: maritime survival, convoy dependency, isolation, naval refuge, limited industry

The actual effects depend on the state grades produced by the campaign.

## AI architecture

AI country package includes:

- focus route plan
- decision priorities
- state defense priorities
- food and shelter priorities
- diplomacy and faction behavior
- expansion targets
- surrender and relocation logic
- mutant or high-chaos route gates
- invalid-route blockers

AI should not:

- attack wasteland for no strategic value
- abandon its only food state without a terminal reason
- choose a route requiring a destroyed capital or dead sponsor
- spend all trains or equipment on low-value relief
- click hidden mutant routes under ordinary conditions
- form a faction with no regional logic

## Regional batch gates

Before a regional wave begins:

- all candidate state groups are mapped
- tag conflicts are resolved
- capital candidates are valid
- flags and portraits have assigned source mode
- focus and decision architecture is approved
- AI targets are valid

Before a regional wave ends:

- every active package is playable
- no package uses generic focus content
- no country lacks a starting army when expected to fight
- no visible asset is missing
- country and focus audits are resolved
- matrix status is updated

## Ten-year content schedule

### Years 0 to 2

- immediate survival
- food, shelter, and supply emergencies
- first government consolidation
- refugee pressure
- local border conflicts

### Years 2 to 5

- regional alliances and wars
- reconstruction industries
- professional military formation
- research recovery
- integration or federation projects
- major political route commitment

### Years 5 to 8

- continental ambitions
- wasteland expeditions
- old-world infrastructure megaprojects
- advanced shelter and decontamination
- ideological blocs
- major mutant or high-chaos transformations

### Years 8 to 10 and beyond

- restored long-distance trade
- major post-Fallout factions
- second-generation political conflicts
- state restoration or permanent exclusion-zone systems
- world-order victory projects
- rare campaign-ending achievements and transformations

## Asset production batching

Each regional wave receives a separate asset manifest.

Required per country:

- normal, medium, and small flags for every implemented identity state
- leader or institutional portrait
- focus icon family
- idea icons
- decision and category icons
- event or report images where used
- faction emblem where applicable
- animated asset only when it communicates a major route or mechanic state

Historical flags and real leaders use sourced assets. Fictional flags, mutant identities, invented leaders, and symbolic bodies use generated assets. Final assets need PNG sources, processed previews, DDS or TGA outputs, manifests, and GFX handoffs.

## Completion proof

The final country matrix must show for each selected active package:

- implemented tag path
- exact state group
- leader and politics
- starting ideas
- forces
- focus tree
- decisions
- AI
- assets
- localisation
- docs
- audit status

Rows that remain candidate-only must be marked as not selected or queued. They must not be described as implemented.
