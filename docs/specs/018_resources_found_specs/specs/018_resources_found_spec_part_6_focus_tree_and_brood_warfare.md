# Event 018 Resources Found Specification, Part 6

## Cave-country focus tree and brood warfare

All names in this file are working labels for design structure. They are not final localisation.

## Tree purpose

The cave country needs a real focus tree because it can survive for years, fight several states, and become a world-ending threat. The tree must make the player choose how the brood hierarchy governs, how it converts resources into formations, how it fights on the surface, how it adapts without losing its core weaknesses, and how it completes continental consumption.

The tree should not imitate a normal human national focus tree with renamed factories and political power. Its rewards should alter resource anchors, brood capacity, armor, movement, tunnel networks, enemy counterplay, state consumption, and war behavior.

The tree is fixed-purpose but not linear. It should have incompatible command philosophies, several military doctrines, shared resource and adaptation support branches, and a late continental route that converges after the country proves control over enough resource anchors.

## Tree scale and pacing

A suitable implementation should create a major-country tree with enough content for early, middle, and late play. The exact focus count belongs to implementation. The architecture supports roughly 45 to 65 focuses if every group is developed properly.

Pacing should follow three acts:

- **Emergence** secures the origin, organizes the starting broods, and teaches the resource-capacity system.
- **Surface War** chooses hierarchy and doctrine, builds anchor networks, adapts to enemies, and expands across the continent.
- **Continental Consumption** completes strategic objectives, transforms the cave country, and opens the world-end route.

The player should gain new decisions and map actions throughout. The tree cannot be a ladder of passive ideas.

## Architecture overview

The tree uses seven interacting lanes:

1. Emergence and origin stabilization
2. Brood hierarchy
3. Resource economy and anchor network
4. Surface war doctrine
5. Adaptation and enemy study
6. Continental expansion and state consumption
7. World-end transformation

The hierarchy lane and doctrine lane contain meaningful route choices. The resource, adaptation, and expansion lanes remain compatible with all routes but change their rewards according to the selected philosophy.

## Lane 1: Emergence and origin stabilization

### Purpose

This opening branch gives the country a functional capital, explains its special economy, organizes the starting army, and creates the first strategic goals.

### Opening focus group: The First Breach, working label

Role:

- confirms the Event 018 origin
- applies the starting exploitation package
- creates or repairs origin supply
- reveals the resource-anchor interface
- grants the first cave-country decisions
- identifies current neighboring enemies

The completion reward should be mostly system activation rather than raw modifiers.

### Origin chamber group

This group develops the starting state as the protected brood heart.

Possible focus roles:

- repair and deepen the origin anchor
- convert surviving field infrastructure into cave supply
- establish a central command chamber
- secure surface exits
- create the first reserve brood space
- map nearby resource-bearing states

Map effects can include infrastructure repair, local supply, forts, and a cave-specific state modifier. The origin should become defensible but not impossible to assault.

### First war-brood group

This group reorganizes the dynamically spawned starting divisions.

Possible rewards:

- unlock a second template variant
- create one or two fictional brood commanders
- improve organization and command
- add an anchor-guard formation that is slower but defensive
- reveal enemy hard-attack capabilities
- unlock a decision to replace destroyed origin broods over time

The branch must not grant a free repeated division loop. Unit rewards should use the protected origin allocation or capacity system.

### Neighbor assessment group

This group evaluates current land neighbors and creates initial offensive priorities.

It can unlock:

- target ranking by nearby resource value
- a decision to mark the richest neighboring state
- temporary planning bonuses against current neighbors
- tunnel reconnaissance missions
- an AI strategy plan for concentrated attack

The focus should not create duplicate wars because the emergence effect already declares them.

### Opening branch payoff

The end of the opening lane should leave the country with:

- stable origin supply
- visible capacity information
- a functioning decision category
- organized starting divisions
- a selected first strategic resource target
- access to hierarchy, doctrine, resource, and adaptation lanes

## Lane 2: Brood hierarchy

### Purpose

This lane decides how command and resource allocation work inside the cave polity. It is the closest equivalent to politics. The routes should change leader identity, decision costs, spawn behavior, and the relationship between the origin and captured anchors.

### Route A: One Maw, working label

Narrative role:

A single sovereign creature and central chamber control every brood. Resources are gathered toward the origin, orders are rigid, and formations fight as extensions of one command.

Mechanical identity:

- stronger central planning
- better organization and coordination
- faster reinforcement near the origin
- lower autonomy for distant anchors
- slower activation of remote resource states
- powerful origin defense
- stronger penalties if the origin is lost

Focus groups:

#### Central resonance

Improves command range, planning, and organization. Can modify the leader portrait or trait to show centralization.

#### Count every vein

Creates strict capacity accounting, reduces wasted capacity, and improves spawn reliability. It can allow fractional progress from resource totals to carry between states without changing the one-per-ten rule.

#### Origin above all

Deepens the origin state, creates a powerful capital modifier, and increases protected allocation recovery. It also increases strategic dependence on the origin.

#### Directed broods

Unlocks precise target orders, faster concentration, and better AI control of anchor guards.

#### Route payoff: The Singular Hunger

Creates the strongest coherent army and the most powerful leader identity. It should not simply grant broad combat bonuses. It should improve command, reinforce concentrated fronts, and enable a late decisive offensive decision.

Tradeoff:

Remote anchors activate more slowly and capacity loss hurts more. A successful enemy strike against the origin can cripple the country.

### Route B: Many Chambers, working label

Narrative role:

Each resource anchor develops a semi-independent brood chamber. The polity becomes resilient, distributed, and difficult to decapitate.

Mechanical identity:

- faster activation of distant anchors
- stronger local recovery
- reduced origin dependence
- weaker global planning and coordination
- more defensive anchor formations
- easier replacement after losing one region

Focus groups:

#### Local brood memory

Allows anchors to retain partial progress after temporary loss and improves local defense.

#### Chamber autonomy

Unlocks regional spawn queues and reduces the penalty from a distant front.

#### Distributed command

Adds commander capacity and improves simultaneous fronts, while lowering concentrated planning bonuses.

#### A second deep capital

Allows one replacement deep capital or secondary origin after controlling a major resource complex. This should be a difficult route payoff rather than an early safety button.

#### Route payoff: The Host Without a Head

Makes the country hard to destroy through one capital seizure and improves recovery across several anchors.

Tradeoff:

Broods have lower coordinated breakthrough, and AI can spread too thin if not carefully weighted.

### Route C: Hoard the Veins, working label

Narrative role:

The hierarchy treats resources as sacred stores. Expansion is deliberate, anchor defense is extreme, and the country seeks the richest states rather than broad territorial control.

Mechanical identity:

- stronger benefits per active anchor
- improved defense and fortification in resource states
- slower expansion through poor states
- stronger state consumption decisions
- fewer but more resilient formations
- high world-end progress from rich-state control

Focus groups:

#### Mineral tithe

Converts captured factory and resource value into anchor strength.

#### Guard the feeding chambers

Creates powerful anchor defense and local recovery.

#### Refuse barren ground

Improves movement or combat toward marked resource targets, while imposing penalties in low-resource regions.

#### Preserve every plate

Improves unit survival and recovery rather than raw spawn count.

#### Route payoff: Vaults Beneath the Continent

Turns a network of rich anchors into a strong continental control system and accelerates late consumption milestones.

Tradeoff:

Poor regions remain difficult to cross and the army grows more slowly when rich states are scarce.

### Route locks

The three hierarchy routes should be mutually exclusive because they represent incompatible command structures. Their early choice should be visible and consequential.

The tree can allow a late crisis focus to abandon one route after origin loss or severe capacity collapse, but route switching should sacrifice accumulated benefits and cannot be used to collect all capstones.

## Lane 3: Resource economy and anchor network

### Purpose

This shared lane improves how captured resources become capacity, supply, fortification, and state transformation. It is the economic heart of the country.

### Survey the surface seams group

Unlocks better resource-state targeting and displays capacity potential before occupation.

Rewards can include:

- map highlighting of high-resource targets
- AI target priorities
- reduced activation time for accurately surveyed states
- intelligence events about enemy demolition plans

### Anchor activation group

Improves the 30-day consolidation process without removing it.

Possible upgrades:

- lower activation time after adjacent anchor control
- preserve partial activation after brief interruption
- stronger local defense during activation
- one emergency decision to accelerate a critical anchor at a combat cost

### Brood queue group

Improves automatic spawning.

Possible focus roles:

- create a visible spawn queue
- reduce the interval between formations
- prioritize replacement of destroyed divisions
- select defensive or assault template preference
- reserve capacity for anchor guards

The one-division-per-ten-resources rule remains intact. Focuses change pacing, template mix, and reliability rather than silently increasing the capacity ratio.

### Consumed industry group

Defines what captured factories do.

Possible choices:

- convert civilian factories into anchor construction
- convert military factories into carapace repair and adaptation
- consume infrastructure for emergency brood progress
- preserve rail and hubs for faster advance

The player should choose between preserving human infrastructure and consuming it for immediate strength.

### Tunnel network group

Creates strategic movement and supply links between nearby active anchors.

A tunnel route should require:

- two active anchors
- geographic proximity or connected states
- time and construction-like resource commitment
- no instant teleportation across a continent

Benefits can include local supply, faster movement between anchors, and reduced encirclement risk. Enemy capture of one end can disable the link.

### Resource economy payoff

The shared capstone should make a mature anchor network operate smoothly. It can:

- improve spawn queue transparency
- reduce activation friction
- strengthen supply between connected anchors
- unlock continental consumption projects

It must not remove the need to capture resources.

## Lane 4: Surface war doctrine

### Purpose

The cave army needs distinct ways to fight. The doctrine routes should change templates, terrain behavior, assault decisions, and AI strategy.

### Doctrine A: Stone Phalanx, working label

Identity:

- slow, dense, highly armored formations
- strong defense and breakthrough
- excellent in deliberate attacks
- poor pursuit and encirclement response

Focus groups:

- interlocking carapaces
- anchor artillery resistance
- deliberate front advance
- siege posture
- heavy brood template

Capstone:

A powerful slow assault system that can break fortified lines when supplied from anchors.

Counterplay:

High hard attack, encirclement, infrastructure denial, and retreat before the phalanx arrives.

### Doctrine B: Burrow War, working label

Identity:

- tunneling, infiltration, and local bypass
- stronger combat in hills, mountains, forests, and urban terrain
- weaker open-field armor concentration
- ability to disrupt supply or emerge behind a nearby line through prepared decisions

Focus groups:

- listen beneath the roads
- undermine the rail junctions
- hidden approach chambers
- urban cellar networks
- burrow assault template

Capstone:

A limited state-targeted infiltration action that requires adjacent active anchors and preparation. It should not become unrestricted teleportation.

Counterplay:

Guarded supply hubs, anti-tunnel missions, controlled demolition, and strong garrisons.

### Doctrine C: Scree Tide, working label

Identity:

- more numerous lighter broods
- faster movement relative to other cave units
- lower armor and individual staying power
- strong exploitation of broken fronts
- higher capacity pressure

Focus groups:

- split the great broods
- lighter plates
- follow the retreat
- swarm the crossings
- raiding brood template

Capstone:

Allows the country to use capacity for a larger number of lighter formations and improve pursuit after a breakthrough.

Counterplay:

Prepared defensive lines, soft attack becomes more useful against lighter variants, and loss of anchors creates severe excess-capacity penalties.

### Doctrine route locks

The three doctrine routes are mutually exclusive at their main commitment point. A small shared opening can improve basic command before the choice.

The player can still unlock one support template from another doctrine through a late adaptation focus, but cannot gain every doctrine capstone.

## Lane 5: Adaptation and enemy study

### Purpose

This shared lane lets the cave country respond to enemy countermeasures without erasing its intended weaknesses. It also creates a military intelligence contest for human opponents.

### Study the broken weapons group

Captured anti-tank guns, tanks, mines, and explosives teach the broods what threatens their armor.

Requirements should include fighting an enemy with meaningful hard attack or capturing industrial states. The reward can improve defense against piercing or reduce the shock of first contact.

### Grow denser plates group

Improves armor and reliability at the cost of speed and spawn time. This is a tradeoff, not a free universal upgrade.

### Lighter jointing group

Improves movement and terrain access at the cost of some armor or defense. It supports Burrow War and Scree Tide more strongly.

### Surface senses group

Improves reconnaissance, planning, and performance in weather or darkness. It can also reduce air-superiority penalties within limits.

### Anti-air adaptation group

The cave country can develop dispersed movement, buried staging, or hardened plates against air attack. It should not gain an air force.

### Recover from hard attack group

Allows better organization recovery after pierced combat and improves anchor repair. It must not make hard attack irrelevant.

### Adaptation capstone

The shared capstone lets the player choose one final adaptation package based on the enemies faced:

- heavier armor
- faster movement
- urban infiltration
- stronger anchor recovery
- air-attack resilience

The choice should be exclusive or costly enough to preserve counterplay.

## Lane 6: Continental expansion and consumption

### Purpose

This lane turns ordinary conquest into a strategic campaign for the continent. It defines what counts as consumption, how the player tracks progress, and what happens to captured states.

### Mark the richest route group

The player selects a strategic axis toward high-resource regions. The AI uses the same score. This unlocks temporary objectives rather than free war goals, since the country is already at war with neighbors.

### Break the first ring group

Requires control of several adjacent states or the defeat of the first neighboring country. It rewards operational reach and unlocks expanded anchor decisions.

### Consume an industrial belt group

Targets a named cluster of industrial or resource states on the origin continent. The exact region is generated from campaign geography rather than one fixed historical area.

Rewards can include:

- faster factory conversion
- stronger anchor activation
- a new commander
- a state consumption project

### Seal the coast group

The cave country learns to hold ports, coastlines, and narrow approaches. It does not gain a navy. The purpose is to prevent easy containment and secure the continent’s landmass.

### Break continental coalitions group

Unlocks AI and decisions for concentrating against faction leaders, guarantees, and coordinated containment. It can reduce penalties from fighting several neighbors but should not grant universal combat power.

### Continental progress interface

The player needs a visible progress summary showing:

- eligible states on the origin continent
- controlled eligible states
- remaining enemy-held eligible states
- excluded impassable or tiny offshore states
- active resource anchors
- total current capacity
- world-end chaos requirement

The interface should name the continent and explain why a state is excluded.

### Consume the last resistance group

Becomes available near full continental control. It creates missions to secure remaining capitals, ports, and resource states rather than waiting passively.

### Continental capstone

Completing continental consumption requires actual map control and the world-end conditions from Part 7. The focus can prepare the transformation, but the terminal effect should fire only after the scripted condition is met.

## Lane 7: World-end transformation

### Purpose

This late lane becomes visible only after the cave country is close to consuming the origin continent and global chaos is above the required threshold.

The lane should not reveal exact cross-continent emergence details too early. It can show that the brood is preparing to spread beyond the landmass.

### Deepen the continental heart group

Transforms the origin and strongest anchors into a continental command network. It increases resilience and records the mature threat.

### Listen beneath distant shores group

Begins research or ritual-like geological sensing of other continents. The presentation should remain physical and subterranean rather than magical unless final lore deliberately establishes another mechanism.

### Choose the first foreign rupture group

The player can influence but not freely select any state in the world. Candidate footholds should be high-resource, valid, and geographically distributed.

### Terminal preparation group

Requires:

- continent consumption condition
- chaos above 1000
- no existing world-end flag
- active cave country
- no successful global defeat state

### World-end capstone

Triggers the terminal scenario, super-event, cross-continent footholds, stronger unit forms, and event-system freeze described in Part 7.

## Cave-country decisions unlocked by the tree

The focus tree should progressively unlock a decision system rather than contain every action in focus completion effects.

### Resource-target decisions

- mark high-value state
- prioritize one anchor activation
- guard a rich state
- consume local industry
- preserve rail for advance
- collapse infrastructure behind retreat

### Brood management decisions

- choose next template in spawn queue
- reserve capacity for anchor guards
- replace destroyed origin allocation
- reorganize excess broods after capacity loss
- designate a secondary deep capital on the distributed route

### Warfare decisions

- prepare a phalanx assault
- undermine a rail hub
- create a burrow approach
- release lighter raiding broods
- harden against a studied enemy weapon

### Continental decisions

- declare a region fully consumed after objective completion
- convert a continental capital into an anchor
- suppress a liberated resource corridor
- prepare distant rupture candidates

The category should use phases and selected targets. It must not show every state decision simultaneously.

## Idea lifecycle

The cave country should use staged ideas tied to routes.

| Institution or condition | Starting role | Route development | Failure or counterplay | Late form |
| --- | --- | --- | --- | --- |
| Mineral Carapaces | Strong armor and hardness | Denser or lighter plates | Enemy piercing research and captured remains | Route-specific armor form |
| Slow Blood | Severe movement weakness | Terrain adaptation or lighter joints | Infrastructure denial and encirclement | Reduced but never removed |
| Resource-Born Broods | Capacity-based automatic army | Faster queues and template control | Capacity loss creates unfed broods | Continental brood network |
| Surface Starvation | Weak away from anchors | Tunnel links and local supply | Anchor liberation and denial | Weakened in world-end form |
| Untranslatable Command | Blocks ordinary diplomacy | Hierarchy route changes command | Origin loss or distributed-command crisis | Terminal continental identity |

The implementation can combine or rename these, but every important starting condition needs an upgrade and a counterplay state.

## AI focus behavior

AI route choice should react to geography and enemies.

### Hierarchy choice

One Maw is favored when:

- the origin is centrally located and defensible
- the country has few fronts
- nearby targets are concentrated
- the leader trait supports central command

Many Chambers is favored when:

- the continent is broad
- the country faces several fronts
- active anchors are dispersed
- the origin is threatened

Hoard the Veins is favored when:

- rich resource states are clustered
- poor terrain separates valuable regions
- the AI can defend a small number of anchors
- world-end progress can be gained through concentrated resource control

### Doctrine choice

Stone Phalanx is favored against fortified or armor-poor enemies.

Burrow War is favored in mountains, hills, forests, or dense urban regions and against strong front lines with vulnerable supply.

Scree Tide is favored when the country has high capacity, open terrain, and several weakened enemies.

### Focus validity

AI must not choose focuses requiring:

- a missing origin state
- nonexistent resource anchors
- a continent condition that no longer applies
- an enemy weapon profile it has not encountered
- a disabled evolution or world-end route
- a dead target country
- an impossible coastal or regional objective

## Focus localisation direction

The tree’s writing should reflect nonhuman perception without becoming unreadable.

Useful direction:

- focus on pressure, vibration, mineral taste, depth, heat, armor, and collective command
- describe states through resource and terrain significance
- keep military intent clear to the player
- use original vocabulary consistently
- avoid human parliamentary language unless describing captured institutions
- avoid meme cave language and generic monster growling
- avoid final super-event quotations or cultural references in focus text

## Icon direction

Every focus or focus family needs its own icon direction. Coordinated families can share motifs without resizing one icon type into another.

Major motifs:

- origin breach
- mineral crown or command crest
- distributed chambers
- guarded resource vein
- heavy carapace phalanx
- tunneling assault
- lighter scree swarm
- captured anti-tank weapon study
- active resource anchor
- tunnel network
- consumed industrial district
- continental silhouette with underground veins
- distant rupture

All focus icons are generated fictional assets at 94 by 86 and must use the focus reference folder.

## Tree completion standard

The tree is complete only when it has real branch depth, hierarchy and doctrine choices, route-specific AI, resource-anchor decisions, adaptation counterplay, continent objectives, world-end preparation, idea lifecycles, varied map and mechanic rewards, icon coverage, localisation, and a route coverage audit. A single vertical conquest ladder or repeated combat modifiers does not satisfy this specification.
