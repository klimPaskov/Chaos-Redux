# Event 20 Black Plague Specification, Part 5

## Rat Nation country package and shared focus tree

All country names, route names, focus names, idea names, unit names, decision names, and asset names in this file are working labels, not final localisation.

## Country role

RTA is the persistent nonhuman Rat Nation carrier created by Evolution III. It is not a temporary rebel stack and must not disappear after one battle. Each internal brood begins in a catastrophic infection basin with a strong initial army allocation, grows new mutated rat formations through timed pulses, infects every state it occupies, and competes with other broods through dominance and absorption while remaining under the RTA carrier.

Rat Nations have one fixed strategic purpose: expand the plague ecology and survive long enough to become the dominant brood. They do not need ordinary human ideological pluralism. They still need internal choices around hierarchy, mutation, territory, military method, proto-sentience, and rivalry.

## Two-tag country package and internal brood pool

The system uses exactly two country tags: RTA for every non-sentient Rat Nation brood and RTX for the separate sentient Rat King. Internal brood identity is represented by state markers, basin variables, strength pools, and capped RTA army allocations. No additional Rat Nation country tags are created.

### Country-package rules

- RTA and RTX must be checked against vanilla, Chaos Redux, and approved mod conflicts
- both tags have a country definition, history setup, flag set, localisation family, and focus tree access
- both tags remain dormant until a valid basin and state package exists
- internal broods are assigned only when a valid basin and state package exist
- absorbed or destroyed internal broods clear their state markers, strength values, unit allocations, and event targets safely
- RTA reuse preserves no old state, leader, focus, AI, immunity, route, or dominance data

RTA is reusable only after its retirement quarantine clears all old state, leader, focus, AI, immunity, route, unit, and dominance data. RTX is a separate one-at-a-time royal package and is not a second brood carrier.

## Public identity

RTA should have a short map-readable public name drawn from a brood naming pool. Names should evoke warrens, broods, teeth, burrows, plague, ash, carrion, docks, fields, or ruined cities. They should not use administrative office language.

The RTA public name can vary by origin archetype through scripted localisation, while RTX retains its royal identity. Basin markers and tooltips distinguish multiple RTA broods without inventing country names or tags.

### Leader identity

A base Rat Nation uses a collective or institutional leader portrait showing a dominant brood, nest council, or mass of mutated rats. The leader name should be an institutional brood identity rather than a random human personal name.

This avoids pairing one fictional portrait with an arbitrary human name and communicates that base broods have not yet produced a fully sentient monarch.

### Government presentation

Base Rat Nations use the existing ideology framework through a dedicated nonhuman subideology or the closest established special-country pattern. They should not require a new global ideology family only for this event.

Party and government text should describe instinctive hierarchy, dominant scent, brood command, or emergent cunning. Final wording belongs to implementation localisation.

## Shared country classification

Every Rat Nation must be registered in:

- the shared special chaos country classifier
- the shared actual nonhuman country classifier

Systems that normally affect human population, politics, migration, ordinary disease, or manpower should use those shared classifiers. No event-local duplicate classifier should be created.

## State package at emergence

A Rat Nation begins with:

- one capital in the emergence state
- one to three states depending basin severity
- plague status preserved on every transferred state
- core or ownership treatment that prevents immediate invalid release behavior
- no human manpower dependence
- no ordinary equipment production requirement
- a strong initial army generated from basin conditions
- the shared base rat focus tree
- one origin archetype
- initial Brood Mass, Hunger, and Coherence values
- event-created origin flag so the tree and systems do not load on an unrelated tag instance

The package must be playable when a human takes control. A human rat player uses the focus tree and disease board but still cannot manually deploy normal divisions.

## Triggerable scenario opening

The triggerable scenario creates several full internal RTA broods immediately and creates or preserves the separate RTX package. Each brood uses the same valid state, army allocation, focus, portrait, flag, mechanic, and AI rules as a naturally emerged RTA brood. Scenario broods are not reduced temporary versions and do not consume extra country tags.

The scenario distributes broods among selected continents and assigns one origin archetype from the local basin. Independent broods remain visible during the initial royal-consolidation grace period even though the Rat King also exists. Dominance timers and royal absorption resume after that grace period.

## Map and state safety

- the emergence effect must never delete the last viable human state of a player country without explicit player-facing handling
- the new capital must be in owned and controlled territory
- railways, supply nodes, ports, and buildings remain in the state unless the emergence effect intentionally damages them
- Rat Nations do not receive human cores across an entire country
- occupied human states remain populated and continue to die from plague
- release or annexation must not leave invalid controllers or stranded units
- Rat Nation destruction transfers or liberates states through normal war outcomes, but plague cleanup remains separate

## Core rat mechanic values

### Brood Mass

Brood Mass represents the living volume available for future unit pulses. It grows from controlled plague states, deaths, food access, focus choices, and absorbed rivals. It falls from catastrophic military losses, starvation outside plague territory, anti-rat operations, and nest destruction.

Brood Mass determines:

- number of formations in the next pulse
- access to larger mutant templates
- ability to resist absorption by a stronger brood
- eligibility for late focus branches

### Hunger

Hunger creates pressure to expand. It rises when the brood remains stationary, loses access to populous states, or controls cleaned low-population territory. It falls after conquest, mass death, captured food regions, or focus actions.

High Hunger should not be a simple bonus. It increases attack drive and brood growth while reducing Coherence and defensive stability. Extreme Hunger can force AI expansion or cause uncontrolled state damage.

### Coherence

Coherence measures how well the swarm follows one command pattern. It begins low and improves through hierarchy, absorbed rivals, stable territory, and proto-sentience.

Low Coherence produces:

- less reliable strategic movement
- weaker coordination and planning
- more variable brood pulses
- greater chance of a smaller brood splitting away when a new basin qualifies

High Coherence produces:

- stronger planning and reinforcement
- more predictable unit pulses
- higher absorption strength
- access to Rat King candidacy

### Disease Dominion

Disease Dominion is derived from controlled plague states and average disease load. It is not a fourth manually managed meter unless the UI needs one. It modifies growth, supply, and occupation strength.

## Three-spirit lifecycle

A Rat Nation should never exceed the focus-tree national spirit cap. Its identity is carried by three deep staged spirits.

### Working spirit 1: Uncounted Brood

**Starting role**:

- removes human manpower dependence
- removes ordinary equipment dependence
- disables normal recruit and deploy use
- establishes timed brood pulses

**Upgrades**:

- larger pulse cap
- reduced pulse interval
- access to specialist mutant templates

**Failure form**:

- reduced growth after nest destruction or isolation

**Final transition**:

- replaced by the Rat King population system after unification

### Working spirit 2: Born of Pestilence

**Starting role**:

- immunity to Black Plague penalties
- growth and supply benefits in infected states
- automatic infection of occupied states
- severe weakness in clean isolated territory

**Upgrades**:

- stronger plague-state movement
- faster infection establishment
- overseas stowaway access for Dock Broods

**Failure form**:

- anti-rat cleanup can temporarily suppress the benefits in liberated or heavily treated states

**Final transition**:

- replaced by a Rat King plague mastery spirit

### Working spirit 3: Fractured Instinct

**Starting role**:

- low planning and command efficiency
- limits advanced military templates
- creates dominance and split risk

**Mitigation paths**:

- hard hierarchy
- distributed swarm intelligence
- emergent sentience

**Failure form**:

- extreme Hunger and low Coherence can worsen fragmentation

**Final transition**:

- removed or transformed during Rat King coronation

## Rat supply model

Rat units do not consume ordinary equipment, but they still need a territorial logistics rule so they are powerful without becoming mechanically unbounded.

### Plague-state sustenance

Rat units receive their best organization, recovery, and movement in:

- Rat-Controlled plague states
- adjacent active plague states
- heavily infected enemy states

### Clean-territory strain

When advancing deep into clean, low-population territory without establishing plague:

- recovery drops
- organization regeneration slows
- attrition rises
- brood pulse contribution falls
- Hunger rises

This encourages the rat AI to spread the disease alongside conquest and gives human players a reason to clean and defend corridors.

### Burrow network

Controlled infected states gradually become established burrow nodes. Nodes provide local supply and unit growth. Human anti-rat clearance removes them after liberation through a timed action.

The burrow network should reuse state flags or a compact state status rather than creating a separate building unless the live engine and asset pattern make a building worthwhile.

## Initial unit families

Rat Nation units are fictional special formations. Exact statistics belong to implementation balance, but their battlefield roles must be distinct.

### Swarm Columns

- main line formation
- high soft attack and organization
- strong urban, forest, marsh, and ruined-state combat
- weak armor and air defense
- large front presence

### Mutated Brutes

- lower unit count
- high breakthrough, hardness pressure, and fort assault
- slow movement
- vulnerable to concentrated armor, air, and anti-rat operations

### Burrowers

- strong movement through difficult terrain
- reduced river, fort, and entrenchment penalties
- weaker in open ground
- useful for encirclement and surprise routes

### Carrion Guard

- defensive formation around capitals and established burrow nodes
- high recovery and defense in plague states
- limited offensive reach

### Dock Stowaways

Available only to Dock Broods or later shared unlocks.

- support sea-route establishment
- enable scripted overseas seeding or coastal transfer
- not an ordinary navy replacement

## Starting army composition by archetype

| Archetype | Primary formations | Secondary formations | Battlefield identity |
| --- | --- | --- | --- |
| Urban Warren | Swarm Columns | Burrowers, Carrion Guard | city pressure and tunnels |
| Field Brood | Swarm Columns | Mutated Brutes | wide land movement and encirclement |
| Dock Brood | Swarm Columns | Dock Stowaways, Burrowers | port seizure and overseas spread |
| War Brood | Mutated Brutes | Swarm Columns, Carrion Guard | frontline shock and depot capture |

Every starting package should include at least two roles. The implementation must not create many visually different templates that play identically.

## Timed brood growth

The brood growth pulse is the central reinforcement pathway.

### Pulse calculation

The expected batch should be derived from:

- base amount by evolution and Chaos value
- controlled plague state count
- total Brood Mass
- recent human deaths in controlled states
- number of established burrow nodes
- origin archetype
- focus upgrades
- absorbed rival bonuses
- current Hunger and Coherence
- global division and performance cap

### Pulse output

The pulse chooses from unlocked templates. It should not always spawn the strongest unit.

- low Coherence favors basic swarms
- high Brood Mass unlocks brutes
- tunnel focuses add Burrowers
- defensive crisis can add Carrion Guard
- Dock Broods can gain stowaway support

### Human rat player presentation

The decision category or country mechanic panel should show:

- days until next pulse
- expected unit range
- current contributing states
- template pool
- factors reducing growth

The player cannot spend political power to buy normal units. Focuses and decisions change the pulse conditions instead.

## Rat military growth decisions

Rat decisions are not a shop. They alter territory, risk, and pulse behavior.

### Strip the outer districts

Targets a controlled populated state. It raises Brood Mass and accelerates deaths while damaging state value and increasing Hunger relief. Repeated use can destroy the state's future contribution.

### Establish a burrow node

Requires control of an infected state for a period. It consumes time and exposes the state to human counterattack. Success improves local supply and future pulses.

### Follow the refugee road

Targets a neighboring threatened or infected state with a valid movement route. It increases attack and spread pressure while risking overextension.

### Concentrate the brood

Delays the next pulse to produce fewer stronger mutant units. It raises local vulnerability during the delay.

### Scatter the brood

Produces more weak swarms and increases split risk. It suits large front expansion.

### Devour the wounded rival

Available during rat dominance standoff. It raises the chance of absorbing the weaker brood but commits units and can lower Coherence if the score is close.

## Base rat focus tree purpose

The shared tree should contain roughly forty to fifty focus roles. The implementation agent chooses the exact focus count and layout. The tree must feel like a country identity and not like a vertical list of rat buffs.

The tree has seven interacting lanes.

1. awakening and survival
2. origin adaptation
3. hierarchy and Coherence
4. brood growth and mutation
5. territorial plague economy
6. military method
7. rival absorption and proto-sentience

## Opening survival lane

The opening focuses solve immediate problems created by emergence.

### Focus group roles

- secure the emergence capital
- establish the first burrow node
- convert initial disease deaths into stable Brood Mass
- protect the first growth pulse
- reveal nearby human counter-rat strength
- choose whether to expand immediately or consolidate

### Rewards

- state fortification or burrow defenses
- controlled first pulse
- selected unit mix
- local disease load stabilization
- short-term defensive bonuses
- decision unlocks

The lane should not grant ordinary factories or equipment that rats cannot use.

## Origin adaptation lane

Each origin archetype receives a short distinctive module.

### Urban Warren route

**Narrative role**: turn sewers, basements, ruins, and dense blocks into a connected nest.

**Mechanical role**:

- urban combat
- faster burrow construction
- larger growth from high-population states
- stronger city infection
- greater vulnerability to prolonged bombardment and clearance

**Decision unlocks**:

- undermine a city defense
- open sewer routes
- consume an abandoned district

### Field Brood route

**Narrative role**: spread through farmland, villages, granaries, and riverbanks.

**Mechanical role**:

- movement and encirclement
- lower clean-territory strain in rural states
- stronger growth from food regions
- weaker immediate city assault

**Decision unlocks**:

- overrun the granaries
- nest along the river
- migrate the brood front

### Dock Brood route

**Narrative role**: use warehouses, ships, quay walls, and cargo routes.

**Mechanical role**:

- port capture
- overseas exposure after Evolution II
- convoy and coastal pressure
- faster threat to islands

**Decision unlocks**:

- infest outgoing cargo
- seize the harbor tunnels
- follow a convoy route

### War Brood route

**Narrative role**: grow from trenches, field hospitals, depots, and abandoned battlefields.

**Mechanical role**:

- stronger initial shock units
- supply hub and rail seizure
- faster growth after battles
- higher Hunger and lower Coherence

**Decision unlocks**:

- consume a battlefield
- collapse the depot line
- follow the retreat

## Hierarchy lane

The brood chooses one of three command methods. The routes are mutually exclusive because they create different Coherence systems.

### Dominant Beast route

A single enormous breeder or alpha presence controls the swarm through fear and scent.

- fastest early Coherence gain
- stronger capital defense and brute units
- high vulnerability if the capital or leader condition is lost
- lower proto-sentience ceiling
- strong dominance score against nearby broods

### Distributed Instinct route

The brood coordinates through many local nests.

- resilient Coherence across wide territory
- more stable unit pulses
- slower absorption and weaker concentrated offense
- easier recovery after capital loss
- strongest defensive network

### Emergent Cunning route

The brood begins using captured tools, patterns, maps, and human behavior.

- slower early military power
- highest proto-sentience progress
- better planning, infiltration, and target selection
- direct Rat King eligibility support
- creates internal instability as instincts change

## Brood growth and mutation lane

This lane changes the timed pulse and unit pool.

### Mass swarm path

- more formations per pulse
- lower individual strength
- faster infection of occupied states
- higher supply and Hunger pressure

### Giant mutation path

- unlocks stronger Mutated Brutes
- fewer formations
- higher breakthrough and fort pressure
- slower recovery and movement

### Burrow warfare path

- unlocks advanced Burrowers
- improves river, fort, mountain-pass, and urban movement
- creates surprise attack events and local tunnel decisions
- weaker open-field defense

The tree can allow one primary path and limited secondary crossover. It should not let one brood obtain every peak unit upgrade before Rat King unification.

## Territorial plague economy lane

Rat Nations do not use ordinary economic branches. Their economy is the transformation of territory into nests, food, disease, and movement.

### Focus group roles

- establish burrow nodes
- convert ruins into shelter
- exploit ports or granaries according to archetype
- maintain plague load in controlled states
- extend sustenance along the front
- choose between preserving population for long-term growth or consuming it for immediate Brood Mass

### Central tradeoff

#### Preserve the Herd

- lower immediate death rate
- more stable long-term state contribution
- slower Hunger relief
- higher Coherence and proto-sentience

#### Consume the State

- rapid deaths and Brood Mass
- stronger short-term pulses
- state exhaustion and later starvation
- faster world-threat and Rat King death thresholds

The final player-facing text must not make the mass death route comedic.

## Military method lane

### Flood the Front

- wide swarm warfare
- faster reinforcement and combat width presence
- greater losses and Brood Mass consumption

### Break the Strongpoints

- brute and burrow assault
- fort, city, and supply hub focus
- slower territorial coverage

### Hunt the Roads

- encirclement, retreat pursuit, and transport disruption
- increases troop-route infection
- weaker direct assault

### Hold the Nest

- defensive burrow network
- strong resistance to human counteroffensives
- slower dominance and expansion

Support focuses can connect these methods to origin archetypes. The route should avoid repeated tiny percentage bonuses. Major nodes unlock units, decisions, movement rules, state effects, or pulse changes.

## Rival absorption lane

This lane activates when another Rat Nation exists.

### Focus group roles

- sense neighboring broods
- compare dominance
- undermine weaker rivals
- resist a stronger rival
- integrate captured units and burrow nodes
- record absorbed brood count
- claim the right to rule all broods

The lane should use decisions and timed standoffs rather than normal war goals.

## Proto-sentience lane

This late lane turns a successful brood into a Rat King candidate.

### Requirements

- high Coherence
- several controlled states
- at least one absorbed rival or a high global dominance score
- sufficient event-attributed deaths and Brood Mass
- Evolution IV is enabled or can begin rolling

### Focus group roles

- recognize symbols and command patterns
- preserve captured knowledge
- develop a stable leader identity
- establish communication between nests
- interpret maps and borders
- prepare a coronation challenge

### Payoff

The brood becomes an eligible Rat King candidate. It does not become the Rat King through a base-tree focus alone. Evolution IV selects the strongest valid candidate and transfers the world rat package into the separate Rat King country.

## Branch interaction

- Origin adaptation changes which military and economy focuses are most valuable.
- Hierarchy changes pulse reliability and absorption behavior.
- Mutation path changes the unit pool used by growth pulses.
- Territorial policy changes death pace and long-term sustainability.
- Rival absorption feeds proto-sentience and Rat King candidacy.
- High Hunger can force expansion even when a defensive focus route was chosen.

The final layout should show these interactions and convergence points. The tree should not contain disconnected columns.

## Focus reward standards

Appropriate rewards include:

- unit template unlocks
- brood pulse changes
- burrow node effects
- state infection and occupation behavior
- command and AI changes
- decision families
- dominance and absorption mechanics
- proto-sentience progress
- route-specific leader or portrait changes
- port, tunnel, and supply rules

Inappropriate filler includes:

- ordinary equipment grants
- human manpower
- repeated political power
- repeated generic stability or war support
- ordinary research bonuses without a rat-specific purpose
- a new national spirit for every branch
- weak one-focus dead ends

## Rat research and technology

Base Rat Nations should not use a normal broad human research tree. Their focus and decision systems provide the core progression.

If engine requirements leave research slots active, the package should restrict useful access to a narrow set of captured or mutation technologies. It should not allow a base brood to research and produce a conventional navy, strategic bombers, or a modern human economy.

Emergent Cunning can unlock selected captured knowledge in a controlled way. The Rat King receives the deeper sentient technology treatment in Part 6.

## Rat production

Rat Nations do not need ordinary military factories for equipment. Controlled factories can still matter as:

- ruined shelter and burrow capacity
- captured human facilities used by a sentient route later
- strategic targets for humans
- sources of state value and deaths

The implementation should avoid giving free conventional equipment merely because factories exist.

## Leaders and portraits

### Base collective portraits

At least four generated collective portraits should exist, one for each origin archetype. They should be period-compatible HOI4 leader portraits with a clear central brood or dominant creature, no text, no comedy framing, and no modern laboratory imagery.

### Archetype variants

- Urban Warren: sewer or ruined city setting
- Field Brood: granary, field, or riverbank setting
- Dock Brood: warehouse or quay setting
- War Brood: trench, depot, or ruined battlefield setting

These portraits use institutional leader names. They do not require gendered personal name pools.

### Proto-sentience visual change

A late-tree portrait variant can show a more organized central figure or council. It should remain a base Rat Nation portrait and not duplicate the Rat King reveal.

## Flags

Every registered rat tag needs a readable base flag in normal, medium, and small sizes. Because the tags are fictional, generated art is appropriate.

### Flag design rules

- unique central symbol for each RTA brood marker, with one shared RTA flag family
- common visual family so the player recognizes Rat Nations
- no simple recolors of one flag
- readable at 10 by 7 pixels
- no generated text
- motifs can include tails, teeth, burrow spirals, grain, docks, trenches, crowns denied, or plague marks
- ideology variants are created only when the country package can actually display them

A complete two-tag country package with distinct RTA brood markers is better than a larger pool with duplicated flags.

## Diplomacy and peace

Base Rat Nations cannot join ordinary factions, become puppets, sign white peace, or accept human guarantees. They are a world-threat enemy.

Human countries can still:

- coordinate against them through existing world-threat systems
- liberate and quarantine occupied states
- send volunteers or aid to threatened countries
- negotiate no ordinary peace that leaves a stable rat state unless a future accepted plan explicitly adds such a route

Rat countries can absorb one another through dominance. They do not use human diplomacy for that process.

## AI behavior

### Strategic priorities

1. preserve the emergence capital until the first pulse
2. capture adjacent infected and high-population states
3. establish burrow nodes
4. spread plague ahead of the army
5. avoid deep clean territory without a route to infect it
6. attack weak human cordons and supply hubs
7. challenge weaker adjacent broods through dominance
8. pursue proto-sentience when strong enough

### Archetype priorities

- Urban Warren targets cities and rail hubs.
- Field Brood seeks wide connected rural territory and food regions.
- Dock Brood prioritizes ports and overseas routes.
- War Brood follows fronts, depots, and retreating armies.

### Risk limits

- do not throw every division into an armored fortified front
- do not abandon the capital before the first pulse unless encircled
- do not create overseas exposure without a valid port route
- do not begin an absorption challenge against a clearly stronger brood
- do not select proto-sentience when the brood is collapsing

Detailed weights appear in the AI matrix.

## Human playability

A human Rat Nation player needs clear control despite the unusual army system.

The player can:

- choose focus routes
- move and command existing rat units
- manage Brood Mass, Hunger, and Coherence
- select territory and pulse decisions
- establish burrow nodes
- choose mutation and hierarchy
- challenge or resist rival absorption
- pursue Rat King candidacy

The player cannot:

- recruit ordinary divisions manually
- rely on human manpower or equipment
- cure controlled plague states through human disease decisions
- enter normal diplomacy with human countries
- bypass the timed pulse with cheap decisions

## Defeat and cleanup

When a Rat Nation loses all states:

- surviving units are destroyed or transferred only if a valid absorbing Rat Nation owns the state package
- its focus and decision systems close
- its tag state is cleaned
- absorbed brood history remains with the winner when applicable
- liberated states keep their disease status and burrow cleanup requirement
- resurgence protection begins only after human clearance succeeds

If the Rat King already exists, base Rat Nation destruction follows the Rat King unification and successor rules rather than returning independently.

## Asset and localisation coverage

The base rat package requires:

- tag names and adjectives
- institutional leader names
- party and subideology text
- origin archetype text
- focus tree title and descriptions
- decision category and decision text
- unit names and template descriptions
- mechanic value names and tooltips
- four collective portraits plus optional late variants
- unique tag flag sets
- base focus icon family
- unit and decision icons
- report and news images for first emergence and major absorption

Text direction should communicate animal movement, territorial instinct, emerging command, and nonhuman pressure. It should avoid jokes about ordinary pet rats and avoid presenting the broods as cute mascots.

## Acceptance criteria for Rat Nations

- finite conflict-checked RTA/RTX country package exists
- both tags have complete flags, localisation, history setup, focus access, and cleanup
- base countries use collective rat portraits and institutional leader names
- shared nonhuman classifiers are updated
- starting territory is valid and remains plagued
- initial armies scale with basin severity and are strong enough to survive
- no ordinary manpower or equipment is used
- normal recruit and deploy is unavailable
- brood pulse is visible, dynamic, and performance-capped
- four origin archetypes play differently
- three deep spirit lifecycles replace many shallow ideas
- plague-state supply creates strengths and counterplay
- shared focus tree has real interacting lanes and late Rat King candidacy
- rat diplomacy remains hostile to humans and nonviolent toward other rat countries
- dominance annexation transfers units and history safely
- defeated territory requires human plague and burrow cleanup
- AI can survive, expand, absorb, and pursue proto-sentience
