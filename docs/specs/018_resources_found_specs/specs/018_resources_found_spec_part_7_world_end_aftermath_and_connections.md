# Event 018 Resources Found Specification, Part 7

## World-end scenario, defeat aftermath, and event connections

All names in this file are working labels for design structure. They are not final localisation.

## Terminal scenario role

The cave country becomes a world-end threat only after it consumes an eligible continent. Ordinary emergence, regional conquest, and even control of several countries are major crisis stages rather than the terminal state.

The world-end branch represents a change in the species’ reach. Once the cave country has converted an entire continental resource network into one connected brood system, similar ruptures begin on other continents. The new footholds are stronger and appear with knowledge gained from the first campaign.

The branch must satisfy the shared Chaos Redux world-end contract. It sets the global terminal state, displays a unique super-event, stops incompatible automatic event progression, and transforms the campaign into a resolved end-state scenario.

## World-end prerequisites

All of the following are required:

- global chaos is above 1000
- no other world-end scenario is active
- the Event 018 cave country exists
- the cave country controls the required eligible territory on its origin continent
- the continent-consumption condition has been stable for a short verification period
- the cave country has completed or bypassed the late preparation route
- the scenario’s evolution and world-end settings are enabled

The world-end effect must not fire from a temporary front-line occupation that lasts a few hours. A verification period gives defenders one final opportunity to liberate a qualifying state.

## Defining a consumed continent

A consumed continent should be defined through eligible states rather than a loose percentage of world land.

### Eligible states

Include states that:

- belong to the origin continent under the game’s continent mapping
- are not impassable
- are part of the main landmass or a strategically connected island group that normal land warfare can reasonably reach
- have a valid owner or controller
- are not engine-only map fragments

### Exclusions

Exclude:

- impassable states
- tiny uninhabited offshore rocks that would make completion impossible
- remote micro-islands with no strategic connection unless the cave country has a designed route to reach them
- states removed or invalidated by another terminal system
- map artifacts that cannot host normal control

The exclusion list should be data-driven or use a documented state group. It must not be hidden guesswork.

### Control standard

The cave country must own and control every eligible state, or meet the project’s accepted definition of total control if occupied ownership is technically safer. The preferred condition is owned and controlled to avoid a world-end trigger from a temporary occupation network.

### Resistance and governments in exile

Governments in exile do not block the map condition when all eligible home states are consumed. Surviving countries outside the continent can still participate in the world-end campaign.

### Continent progress

The cave-country interface should show:

- eligible state count
- cave-controlled eligible state count
- remaining states
- remaining countries with eligible land
- active anchors
- total brood capacity
- chaos requirement status
- world-end preparation status

This progress should be available before the final threshold without revealing exact cross-continent spawn locations.

## Final continental stage

As the cave country approaches completion, the campaign should intensify.

Possible milestones:

- first quarter of eligible states controlled
- half of eligible states controlled
- three quarters controlled
- all major resource regions controlled
- last continental capital captured
- final eligible state consumed

These are ordinary progress milestones, not separate evolutions. They can unlock events, AI changes, focus branches, and foreign cooperation.

At high progress:

- remaining countries gain stronger containment decisions
- foreign aid and hard-attack equipment become easier to coordinate
- the cave AI concentrates against the remaining qualifying states
- inactive resource anchors accelerate
- the global world-threat framework recognizes the cave country as an existential source

## Shared world-threat integration

The cave country should register a cave-specific threat source within the shared world-threat framework.

The source is active when:

- the cave country exists and controls its origin
- or it controls enough resource anchors to remain a strategic threat

The source can clear after:

- the cave country is fully defeated
- no cave footholds remain
- no active world-end state prevents cleanup

The aggregate `world_in_threat` behavior remains owned by the shared system. Event 018 should not create a parallel global crisis flag.

World-threat status can influence:

- AI willingness to cooperate
- faction invitations against the cave country
- emergency hard-attack aid
- ceasefires between ordinary countries
- priority of anti-cave military focuses
- trade and resource-denial decisions

These reactions should not force universal peace. Rival countries can continue their wars while still responding to the threat.

## Terminal transformation

When all prerequisites are satisfied, the world-end effect performs a coordinated transformation.

### Global state

- set the shared `world_end` flag
- set an Event 018 cave-world scenario flag
- set the matching super-event visibility
- set the unique super-event audio identifier
- use settings-aware playback
- stop incompatible automatic event selection and evolution checks
- prevent new ordinary Event 018 fields
- convert cave-country AI to terminal expansion behavior

### Cave-country transformation

The cave country receives a terminal identity with:

- stronger resource-anchor activation
- faster brood spawning
- a stronger but still readable unit upgrade
- improved adaptation to overseas climates and terrain
- reduced dependence on the original continent
- cross-continent rupture decisions or effects
- a changed country name, cosmetic identity, leader form, or national spirit where appropriate

The transformation should feel absurdly powerful because it is a completed special chaos route. It still needs coherent rules and counterplay in the remaining campaign.

### Origin continent

The consumed continent becomes the secure deep heart of the species.

Possible effects:

- every qualifying resource state becomes a mature anchor
- ordinary resource exports from the continent collapse
- remaining human industry is converted or suppressed
- the cave country gains strong local supply and recovery
- enemy liberation missions become harder but remain possible

Do not permanently erase map resources unless the implementation provides a reliable restoration path after liberation. Dynamic state modifiers are safer for reversible consumption.

## Cross-continent emergence

### Selection principle

The world-end branch opens cave footholds on other continents. It should select strategically meaningful states rather than random barren provinces.

Candidate weighting should favor:

- high total strategic resources
- several resource types
- major industrial or transport value
- interior positions that can sustain a front
- geographic distribution across different continents
- countries capable of responding
- states not already controlled by the cave country

Negative weighting should apply to:

- impassable or invalid states
- tiny islands
- states with no meaningful land campaign
- states already occupied by another terminal nonhuman actor when conflict rules are undefined
- states whose transfer would instantly delete a protected scenario without a designed interaction

### Number of footholds

The terminal opening should create several footholds, distributed rather than stacked in one region. The exact number should scale with the number of remaining inhabited continents and campaign state.

A practical design direction is:

- at least one major foothold on each selected continent
- additional footholds in very large continents or high-chaos conditions
- no same-day occupation of an entire country
- enough starting units to establish a dangerous local front

### Foothold strength

World-end footholds are stronger than the first origin breach because the species has learned how to organize surface war.

Strength can depend on:

- resource total in the rupture state
- global cave capacity
- completed hierarchy and doctrine routes
- number of mature anchors on the origin continent
- remaining world industrial strength
- chaos value above 1000

Each foothold receives an initial brood allocation and immediately begins its local anchor activation. The persistent cave country remains the owner. Separate cave tags are unnecessary unless engine geography makes one tag impossible to manage.

### War declarations

The cave country declares war on every new land neighbor created by footholds. The existing neighbor-refresh rule continues.

### Player information

The super-event announces the global rupture. Follow-up news and state events identify new fronts. The exact state-selection formula remains internal, but the player should understand that rich resource states are at risk.

## World-end super-event

The terminal transition deserves a unique super-event because it changes the campaign from a continental crisis into global subterranean emergence.

### Role

World-end revelation and irreversible global escalation.

### Trigger moment

After continent consumption, chaos above 1000, terminal verification, and creation of the first cross-continent footholds.

### Text direction

The description should focus on simultaneous ruptures, collapsing resource centers, organized nonhuman armies, and the realization that the first continent became a template for expansion. It should not list mechanics or thresholds.

The title, button remark, quote, and cultural reference require research through the super-event text workflow. No draft wording in this spec is implementation-ready.

### Image direction

Generated fictional super-event art at 457 by 328. The composition should show an organized mineral-armored host emerging through a shattered industrial or mining landscape, with evidence of several distant ruptures or a global scale without relying on a map as the central subject.

### Audio direction

Unique final music with a documented license, source, creator, duration, and 44.1 kHz game-ready file. The mood should move from subterranean weight to overwhelming organized advance. Pure drones, generated tones, and placeholder tracks are forbidden.

### Wiring

The final implementation needs:

- unique slot or deliberately chosen existing slot
- unique image sprite
- unique audio ID and track
- title, description, button, and quote keys
- settings-aware playback
- event trigger
- event documentation
- music table entry
- spreadsheet alignment

## Emergence super-event

Evolution IV can also deserve a major reveal super-event when the cave country first appears. The reveal is globally important because a nonhuman state with an armored army has replaced a resource field.

### Role

First public emergence of the cave country.

### Trigger

The state transfer and creation of the cave country after the final breach.

### Text direction

Focus on the fall of the excavation zone, organized formations, loss of the state, and immediate attacks on neighboring borders. Keep world-end details hidden.

### Image direction

Generated period-documentary or painterly HOI4 super-event art showing the first armored cave formations leaving a vast excavation breach. The leader can be implied, but the image should prioritize the organized host and the ruined field.

### Audio direction

Unique licensed music separate from the world-end track. The mood should communicate revelation, weight, and a slow military advance.

## Cave defeat states

The cave country can be defeated before world end or after a global crisis.

### Regional containment

A regional threat is contained when:

- the cave country loses all states
- no active footholds remain
- no unsealed Event 018 breach can recreate it
- any protected origin allocation is destroyed

The victors receive a containment event. The origin and other anchor states can enter cleanup projects.

Regional containment does not automatically justify a defeat super-event. It can use a major news event if the threat was limited and short-lived.

### Liberation of resource-anchor states

Liberated states need cleanup decisions:

- clear cave anchor modifiers
- restore resource output
- recover or destroy tunnels
- rescue survivors where plausible
- repair infrastructure
- decide whether to reopen ordinary mining

Reopening the original Event 018 origin should not recreate the same field automatically. The origin remains permanently scarred or closed unless a later accepted expansion designs a separate recovery route.

### Captured cave remains and technology

Victors can gain limited research, armor, or engineering insight. They should not receive cave divisions or a generic monster equipment system from one victory.

### Last brood incidents

A defeated regional threat can leave a small number of cleanup events about sealed tunnels, missing patrols, and surviving nests. These should end. They must not imply an unavoidable secret restart after the player completed the defeat conditions.

## Global defeat aftermath

A structured defeat aftermath is appropriate only when the cave country became global or near-global, consumed much of a continent, created cross-continent footholds, or caused severe worldwide losses.

The implemented classifier treats Event 018 world end or any created cross-continent foothold as global evidence. A complete origin-continent conquest can also qualify only when the cave campaign lasted at least 365 days. The 75-percent continental milestone remains a progression event and never authorizes global aftermath by itself. Another active world-end identity blocks the Event 018 classifier unless it is the Event 018 cave terminal state.

### Defeat super-event

A defeat super-event can fire when:

- the world-end or near-world-end cave threat is eliminated
- all cave states and footholds are gone
- the campaign lasted long enough and caused enough loss
- no other terminal state blocks the aftermath

The tone should be reflective and costly. It should not pretend the world returns to normal immediately.

Quote and music require separate research.

### Reconstruction compact

Surviving countries can create a post-crisis compact focused on:

- underground survey standards
- shared hard-attack research
- resource-site inspection
- tunnel mapping
- reconstruction aid
- emergency evacuation doctrine
- monitoring of abandoned resource basins

This can become a shared decision or tech-sharing system only if the cave war was truly global. A short regional incident should not create a new world order.

The reconstruction choice is offered once per eligible survivor only after that country completed at least three anchor-cleanup contributions, no cleanup site remains, and no live cave threat exists. Join, lead, and refuse are mutually exclusive. Completing the chosen commitment cannot reopen the choice event.

### Lasting consequences

Possible persistent aftermath effects:

- damaged resource supply
- scarred or closed states
- population loss
- reconstruction missions
- veterans and anti-armor doctrine
- memorial or vigilance events
- diplomatic credit for major contributors
- suspicion of extreme excavation projects

The aftermath should record which countries bore the greatest losses and which contributed to victory.

## Interaction with other events

Connections should remain narrow and respect each event’s identity.

### Event 2, Zombie

Both can become actual nonhuman threats, but their army and economy rules must remain distinct. The shared world-threat framework can encourage cooperation. Cave monsters should not become infected, and zombies should not provide cave brood capacity unless a later accepted cross-event design explicitly handles it.

### Event 10, Death

A terminal death-state or other nonhuman actor should be excluded from normal resource-field ownership. If both threats exist, shared nonhuman classification prevents civilian and ideology systems from applying incorrectly. Direct war behavior should use ordinary adjacency and hostility rules.

### Event 13, Natural Disasters

Earthquakes, landslides, or eruptions can damage a field, expose new seams, accelerate collapse, or complicate sealing. Event 13 owns disaster selection and effects. Event 018 supplies field-specific reactions.

A disaster must not automatically cause Evolution IV. It can increase Depth, Disturbance, or closure difficulty.

### Event 29, Riches Found

Event 29 remains abstract wealth. Event 018 uses real strategic resources, state production, trade, and excavation. A field can create commercial wealth, but it must not replace Event 29’s identity.

### Event 50, Great Embargo

Embargoed countries have stronger interest in smuggling, concessions, and alternative supply. Event 50 owns embargo rules. Event 018 adjusts foreign interest and contract behavior.

### Event 78, Border Conflict

Event 018 should reuse valid border-conflict infrastructure if Event 78 provides it. The resource field supplies the claim, value, transfer, and settlement context.

### Event 98, New Ore

Event 98 owns a unique fictional armor metal and its special market. Event 018 must use standard strategic resources and ordinary industrial development. Cave armor comes from the species’ biology and resource consumption, not from discovering Event 98’s unique ore.

### Event 139, Mysterious Creature

Event 139 is a lone hunted creature. Event 018 is an underground labor crisis that can reveal a mass species and country. Creature-hunt decisions can share hunting or reporting patterns, but the events must not merge identities.

### Chemical, biological, air-cleanliness, and deaths systems

- worker and civilian deaths use the shared Deaths system
- ordinary mine sickness does not automatically create biological contamination
- cave attacks do not raise air contamination unless a specific weapon or state effect causes it
- chemical weapons can affect cave units only according to normal or explicitly designed resistance rules
- condemnation applies to countries using unconventional weapons, not to the cave species merely existing

## Event cluster behavior

Event 018 is assigned to Economy (pos), cluster 7, at Medium severity. Cluster entry may start the ordinary baseline discovery. Field creation, enrichment, history, and later evolutions remain owned by Event 018.

## Terminal and aftermath completion standard

The terminal layer is complete only when continent eligibility is explicit, progress is visible, chaos above 1000 is enforced, the world-end state is set once, cross-continent footholds are valid and strong, all audio and image assets are unique and documented, incompatible event systems are gated, regional and global defeat states are distinct, liberated anchors restore cleanly, and cross-event links use shared systems without merging event identities.
