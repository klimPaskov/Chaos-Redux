# Event 20 Black Plague Specification, Part 4

## Evolution tracks and Rat Nation emergence

All labels in this file are working labels, not final localisation.

## Evolution structure

Event 20 has five true evolutions. Ordinary disease states such as Incubating, Severe Crisis, Collapse, Containment, and Recovery are baseline progression and must not be logged as evolutions.

Each evolution belongs to one Chaos Meter tier and enters through dynamic mean-time pacing. Chaos unlocks the possibility. Actual outbreak conditions decide whether the evolution can occur and how quickly it arrives.

| Evolution | Chaos tier | Core change |
| --- | --- | --- |
| Evolution I | Gathering Storm, 200 to 399 | more lethal strain, faster crisis growth, harder countermeasure work |
| Evolution II | Rising Chaos, 400 to 599 | overseas port and sea-route spread |
| Evolution III | Chaos Tier, 600 to 799 | Rat Nations emerge from connected uncontrolled infection basins |
| Evolution IV | Totalen Chaos, 800 to 999 | separate Rat King country unifies the broods and becomes sentient government |
| Evolution V | World Collapse, 1000 or more | world-end focus path unlocks after enough conquest and death |

No evolution happens instantly merely because the chaos threshold is crossed. Evolution V can record its unlock after its own pacing, while the final world-end scenario fires only when the Rat King completes the required route and controls a continent.

## Common evolution entry rules

Each evolution supports two ordinary entry paths. The triggerable scenario defined in Part 9 is an explicit third entry. During its tightly scoped bootstrap, Evolutions I through IV resolve immediately in order and ignore ordinary Chaos gates, eligibility, and mean-time pacing. The scenario does not record Evolution V and does not change the natural evolution rules after bootstrap cleanup.

### Active-event evolution

The outbreak already exists. The evolution changes active states, countries, decisions, AI behavior, focus routes, assets, and future incident pools without requiring Event 20 to fire again.

### Pre-fire evolved opening

The world reaches a high chaos tier before Event 20 fires. The event begins with the relevant evolution permissions already available. The opening is stronger and later thresholds arrive sooner, but the chain still begins from one mainland state and does not skip the core outbreak story.

Pre-fire evolved openings should not spawn the Rat King or trigger the world end immediately. They compress access to later evolution conditions rather than replacing those conditions.

## Evolution pacing model

The target base mean time is around ninety to one hundred eighty days after an evolution becomes genuinely eligible. It can be shorter or longer based on outbreak conditions.

### Factors that accelerate evolutions

- more infected states
- more countries with active infection
- higher event-attributed deaths
- higher share of infected states in Severe Crisis or Collapse
- repeated containment failures
- active war and occupation
- weak global countermeasure knowledge
- known weapon deployment
- rat territorial growth after Evolution III

### Factors that delay evolutions

- strong global countermeasure knowledge
- most infected states Contained or in Recovery
- successful international assistance
- low event-attributed deaths
- high preparedness among exposed countries
- no valid geographic or political condition for the next evolution

An evolution should not remain eligible while the required actor or state no longer exists. Its timer should pause or rebuild rather than firing into an invalid context.

# Evolution I

## Working role

**The strain becomes more virulent and less responsive to early protocols.**

This evolution fulfills the user requirement that the Black Plague becomes harder to cure, more dangerous, and somewhat faster to spread.

## Eligibility

Evolution I can begin rolling when all of the following are true.

- Chaos is at least 200.
- Event 20 has fired.
- At least one Infected or worse state exists.
- The outbreak has remained active for a minimum establishment period.
- The disease has produced either a meaningful death count, a multi-state spread, or a major containment failure.

The roll accelerates when several states are Severe Crisis, when a country has deliberately weaponized the strain, or when countermeasure work is poorly coordinated.

## Active-event changes

### Mortality

- the mortality curve steepens after the early phase
- Severe Crisis and Collapsed states reach high-loss bands faster
- treatment still matters, but a partially developed countermeasure loses some effectiveness until adapted

### Spread

- outgoing land spread pressure increases moderately
- incubation tends to shorten
- relapse risk rises
- troop movement and occupied territory become more dangerous

### Countermeasures

- existing country progress remains intact
- countries must complete an adaptation milestone before regaining full treatment strength
- global knowledge provides less automatic protection until the adaptation is shared
- projects that hoarded data face a larger setback than cooperative programs

### Presentation

- infected state art and UI status become darker and more urgent
- the event log records one evolution entry with the affected world context
- the crisis board shows strain evolution without exposing the exact hidden multiplier

## Pre-fire evolved opening

At Chaos 200 or higher, Event 20 can begin with Evolution I permission active.

- the origin state starts with a higher disease load
- incubation is shorter
- nearby threatened states receive stronger exposure
- the first countermeasure milestone requires adaptation from the beginning
- early deaths remain gradual rather than becoming an opening mass casualty effect

## Containment response

Evolution I is not irreversible. Countries can adapt the countermeasure, strengthen hospitals, and restore lower spread. Successful adaptation should feel like a major medical achievement.

# Evolution II

## Working role

**The Black Plague can cross seas through ports, convoys, military transport, and rat-infested cargo.**

## Eligibility

Evolution II can begin rolling when all of the following are true.

- Chaos is at least 400.
- Evolution I is recorded or the pre-fire opening has Evolution II permission.
- At least one active infection exists in a coastal state with a valid port route.
- The outbreak has reached more than one country or more than one large connected region.
- Port inspection and travel control have failed to reduce global sea exposure below the threshold.

A known biological deployment through aircraft or naval delivery can accelerate the roll because the world has already demonstrated long-range transmission.

## Active-event changes

### Overseas route engine

- infected ports can generate overseas exposure attempts
- destination ports are selected from real convoy, trade, faction supply, access, troop return, or other established connection data where available
- islands and disconnected coastal states become valid targets
- port inspections, travel restrictions, convoy controls, and surveillance can reduce or reveal the route

### Disease behavior

- natural sea jumps usually create Threatened or Incubating status
- Severe Crisis ports can seed a higher opening load
- rat-controlled ports later receive special stowaway and swarm transport behavior

### Strategic choices

- countries can close ports at major economic cost
- navies and overseas empires must choose between supply continuity and disease protection
- isolated islands can become refuges if ports remain controlled
- blockaded or occupied ports can become death traps when relief cannot enter

### Presentation

- the mapmode can show likely sea exposure lines when the country has enough surveillance
- global news triggers when the first confirmed overseas state becomes Infected
- the event log records Evolution II once, not once per port jump

## Pre-fire evolved opening

At Chaos 400 or higher, the origin still begins in one mainland state. If the origin has a port, one valid overseas destination can begin as Threatened after a short delay. If the origin has no port, Evolution II waits for the disease to reach one.

The event must not violate the user's rule by selecting an island as the initial state.

## Counterplay

- port inspections
- temporary port closures
- convoy route changes
- quarantine islands
- troop return screening
- maritime relief protocols
- countermeasure sharing with overseas territories

# Evolution III

## Working role

**Connected uncontrolled plague basins produce Rat Nations.**

This is the first supernatural evolution. The event should clearly transition from an extreme disease crisis into a nonhuman country crisis without claiming that normal plague biology creates organized mutant states.

## Basin eligibility

A Rat Nation can emerge only inside a qualifying connected infection basin.

A basin is a group of adjacent or strongly connected states that meet the following broad conditions.

- at least three connected states are Infected, Severe Crisis, Collapsed, or Rat-Controlled
- at least one state is Collapsed or near collapse
- the basin has suffered a large absolute or relative population loss
- local human containment is weak
- the basin contains enough remaining population and disease load to support a large brood
- no active rat emergence cooldown protects the same basin
- the state is controlled by a human country or by a rat country eligible for a new rival brood

Evolution III can begin rolling when:

- Chaos is at least 600
- Evolution II is recorded or the pre-fire opening has Evolution III permission
- at least one qualifying basin exists
- global Black Plague deaths and active duration pass meaningful thresholds

## Emergence pacing

The first Rat Nation should not appear the day a basin qualifies. A hidden emergence pressure grows through:

- connected infected state count
- average disease load
- proportion of Collapsed states
- event-attributed deaths
- urban density, ports, sewers, trenches, ruined supply systems, and abandoned infrastructure
- low containment and weak military presence

Strong cordons, successful cleanup, and retaking local administration reduce pressure. A basin can lose eligibility before the emergence occurs.

## Selecting the first rat state

The emergence state is selected from the worst states in the basin.

### Strong preferences

- highest disease load
- largest cumulative death share
- Collapsed status
- large surviving population
- dense urban or port environment
- ruined or occupied infrastructure
- low human unit presence
- existing black fog severity

### Exclusions

- states already controlled by a rat country unless creating a distinct rival is specifically allowed
- states in final Recovery or Cured status
- states protected by an active anti-rat clearance memory
- states that would create an invalid country with no controlled territory

## Territory package

A new Rat Nation receives the emergence state and may receive one or two adjacent qualifying states when the basin is severe enough. Human owners lose control of those states through a clear breakaway effect.

The transferred states keep the Black Plague modifier and current disease load. No cure, population restoration, or state cleanup occurs.

A newly created Rat Nation should not automatically take an entire country. It begins as a dangerous local state and grows by occupation.

## Initial army scaling

The initial rat army is intentionally strong. It scales with the basin rather than using one flat division count.

### Scaling inputs

- population remaining in the emergence state
- cumulative population deaths in the basin
- number of connected infected states
- average disease load
- urban, port, frontline, or rural archetype
- Chaos value within the tier
- Evolution I severity
- presence of weaponized provenance
- strength of nearby human armies

### Target bands

| Basin condition | Initial rat divisions | Intended pressure |
| --- | ---: | --- |
| Minimum qualifying basin | 10 to 16 | dangerous local breakaway |
| Established severe basin | 17 to 28 | regional military crisis |
| Catastrophic basin | 29 to 45 | major front that requires coordinated response |
| World-collapse basin | 46 to 70 | high-chaos army that can overwhelm an unprepared region |

The implementation can use several templates inside the total. Rat divisions should be stronger than ordinary infantry in their preferred terrain and against soft targets.

## Rat unit rules

- rat units use no human manpower
- rat units consume no ordinary equipment stockpile
- rat units cannot be deployed manually through the normal recruit and deploy interface
- new units arrive through a timed brood growth pulse
- units are immune to Black Plague disease penalties
- units remain subject to designed supply, terrain, air, armor, fire, and anti-rat counterplay
- units should not be invulnerable merely because they do not use manpower or equipment

The no-manpower and no-equipment rule requires a dedicated scripted unit-generation system and unit templates that do not create hidden equipment demand.

## Brood growth pulse

Every Rat Nation receives a visible or tooltip-explained brood growth cycle. The player cannot click to train units.

### Growth sources

- controlled plague states
- disease load in those states
- recent human deaths
- captured population centers
- brood focus upgrades
- absorbed rival rat nations
- Rat King global effects after unification

### Growth limits

- each pulse has a dynamic cap
- recently conquered states need time before contributing fully
- low-population or cleaned states contribute little
- isolated rat armies outside plague territory suffer growth and supply penalties
- performance caps prevent unlimited division creation

### Target cadence

A normal pulse should occur roughly every thirty days. Severe and late-game branches can reduce the interval or increase the batch. Growth should remain predictable enough that human players can plan containment offensives.

## Plague occupation rule

Every state occupied by a Rat Nation becomes a Black Plague state.

- Clear states become Incubating or Infected based on rat army strength and duration
- Threatened states become Infected
- existing infected states receive higher disease load
- human population deaths continue through normal disease ticks
- rat units and rat countries remain immune
- the mapmode updates immediately
- the state contributes to future brood growth after an establishment delay

Occupation does not create a second disease effect or duplicate death tick.

## Rat diplomacy

Rat Nations are hostile to every human country. They do not use ordinary alliances, guarantees, trade, or peace behavior.

Rat Nations are not hostile to other Rat Nations. When two rat countries become adjacent, they enter a dominance comparison rather than a normal war.

## Rat dominance and annexation

### Dominance score

The score uses:

- controlled plague states
- current rat divisions and unit quality
- cumulative brood growth
- disease load and deaths in controlled territory
- absorbed rival count
- proto-sentience progress
- age of the brood

### Border absorption

When two Rat Nations share a border for a sustained period:

- the stronger brood begins an absorption countdown
- the weaker brood can gain temporary resistance through focus or event choices
- if the score remains decisive, the stronger rat country annexes the weaker
- all weaker units transfer to the stronger country
- disease states and modifiers remain
- the stronger country gains absorption history and Rat King eligibility

A close score can delay the merge and create a territorial standoff. Rat countries should not repeatedly declare wars that waste units and break the user's unification rule.

## Multiple emergences

Evolution III can create several Rat Nations in separate uncontrolled basins. The system should avoid excessive tag spam.

### Limits

- use a finite pre-registered tag pool
- global active Rat Nation cap scales with Chaos tier and map size
- basin cooldown prevents repeated creation in the same small area
- after the tag pool is exhausted, new qualifying basins reinforce the nearest compatible rat country or produce a resurgence incident instead of an invalid tag

The final tag pool count should be chosen after live repository conflict checks. A planning target of twelve to sixteen tags gives enough global variety without requiring unlimited country creation.

## Rat country origin archetypes

A new brood receives one of four origin archetypes from its state context.

### Urban Warren

- high population city or major victory point
- stronger initial swarm count
- urban combat and tunnel advantages
- higher food pressure and faster local deaths

### Field Brood

- rural, agricultural, or low-density connected basin
- wider movement and forage advantages
- slower initial sentience
- stronger state expansion and encirclement behavior

### Dock Brood

- port or coastal origin
- sea-route and convoy stowaway behavior after Evolution II
- faster overseas threat
- weaker inland starting strength than an Urban Warren of equal size

### War Brood

- frontline, occupied, trench, depot, or ruined supply origin
- stronger military templates
- higher equipment-independent breakthrough
- more aggressive AI
- lower initial administrative cohesion

These archetypes use one shared base focus tree with origin-specific branches, localisation direction, AI weights, unit mixes, and assets.

## Human response to emergence

The first Rat Nation triggers a major global milestone.

- the Black Plague world-threat source activates
- nearby countries unlock anti-rat actions in the shared crisis board
- major powers can send aid, volunteers, air support, or medical missions through existing systems
- all human countries gain intelligence on Rat-Controlled states in the disease mapmode
- cure work remains essential because retaking states does not remove plague

The event should not create a separate rat-crisis decision category when the disease board can host the needed actions.

## Rat resurgence

Destroying a Rat Nation does not guarantee safety. A liberated basin can produce a resurgence when:

- Evolution III remains enabled
- several connected states remain Severe Crisis or Collapsed
- the basin was not cleared through anti-rat cleanup
- enough time passes after military liberation
- no resurgence protection is active

Resurgence creates a smaller but experienced brood or reinforces a surviving neighboring rat country. Each basin has escalating cleanup requirements and a cooldown to prevent endless immediate respawn.

## Defeating the rat phase

The rat phase is resolved when:

- no Rat Nation exists
- no Rat King exists
- no qualifying resurgence basin remains
- every previously rat-controlled state is at least Contained
- global rat emergence pressure stays below threshold for a sustained monitoring period

The plague can still remain active after the rat phase is defeated. Full eradication requires ordinary disease cleanup.

## Pre-fire Evolution III opening

At Chaos 600 or higher, Event 20 still begins in one mainland state. The origin starts with Evolution I severity and Evolution II permission. Rat emergence pressure begins at a higher baseline once a connected basin forms.

The ordinary opening should not create a Rat Nation before the player has seen disease spread, state collapse, and the first basin form. The delay can be shorter than a low-chaos campaign, but the chain remains legible. The triggerable scenario is the deliberate exception and creates several full Rat Nation packages immediately.

## Evolution III presentation

### First emergence report

The report direction should focus on abandoned streets, animal movement, missing corpses, broken barricades, and organized attacks. It should not explain sentience before the rats have shown it.

### News milestone

The first internationally recognized Rat Nation receives a news event and event log entry. Additional broods are shown through mapmode, logs, and selective reports rather than one global popup each.

### Assets

- fictional period-documentary report image for the first emergence
- generated collective rat leader portrait for each archetype family
- unique rat flags or emblems from the registered tag pool
- rat unit and state status icons
- possible animated black fog escalation

## Acceptance criteria for evolutions I to III

- every evolution is distinct from baseline state progression
- each evolution has active-event and pre-fire entry behavior
- evolution pacing uses outbreak conditions and dynamic mean time
- Evolution I increases mortality, spread, relapse, and cure difficulty without deleting progress
- Evolution II uses real port and sea connections and preserves mainland-only origin selection
- Evolution III requires connected uncontrolled infection and large population loss
- Rat Nations spawn with strong dynamic armies
- rat units use no human manpower or ordinary equipment and cannot be manually deployed
- brood growth happens through timed pulses
- rat occupation infects states and continues human population deaths
- rat countries ignore plague penalties
- rat countries do not fight each other normally
- stronger adjacent rat countries annex weaker ones and inherit units
- destroyed rat territory remains diseased and can resurge until cleared
- all rat tags use shared nonhuman and special chaos country classification
