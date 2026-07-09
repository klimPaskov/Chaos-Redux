# Event 018 Resources Found, Part 5 Cave Host Focus Tree Design

All focus labels are working labels only. They are not final localisation. The implementation agent owns final focus names, descriptions, coordinates, prerequisites, and exact focus count.

## Focus tree role

The Cave Host is a fixed-purpose nonhuman country. It does not need normal democratic, communist, fascist, or neutral political routes. It does need a real focus tree because it is a persistent fighting country that can reshape the campaign. The tree should make the Host play differently from ordinary countries by changing resource capacity, brood shape, terrain behavior, enemy panic, and world-end progression.

The player or AI should look at the tree and understand that the country is a slow underground war organism. The tree should not grant political power, ordinary stability, normal factories, or normal recruitment as primary rewards. Its reward language should be resource hunger, stone armor, tunnel movement, brood organization, surface terror, and continental breach.

## Opening trunk

The opening trunk stabilizes the Host after emergence.

Working focus group: first breach.

Purpose:

- establish nonhuman country rules
- set origin nest state identity
- reveal or initialize the resource capacity mechanic
- start neighbour war behavior
- unlock the main branches
- define the Cave Host as a world threat source

Focus role map:

| Role | Gameplay direction | Unlocks |
| --- | --- | --- |
| Origin nest anchor | Strengthens origin state and stores initial host capacity. | resource capacity display, origin defence bonus |
| First surface war | Directs Host toward neighbouring states and resource targets. | target selection AI, neighbour war event cleanup |
| Bodies from the seam | Explains automatic resource-based broods. | capacity refresh, brood deployment logic |
| The slow host | Gives first armor and slow speed identity. | stone hide branch |
| Hunger remembers | Reveals resource-state target priority. | hunger branch |
| The lower roads | Opens limited tunnel logic. | tunnel branch |
| Brood forms | Opens internal brood method choice. | brood hierarchy branch |

The trunk should not be a long vertical checklist. It should branch into at least three lanes within the first few focuses. The first focus can be mandatory, but the player should quickly choose what kind of Host it becomes.

## Hunger lane

The hunger lane improves the relationship between captured resources and new broods.

Narrative role: the Host learns to identify useful seams beyond the origin state.

Mechanical role:

- improves resource target weighting
- speeds capacity refresh after state capture
- improves brood spawn reliability
- can add stronger effects when capturing states with the originally discovered resource
- increases world threat and foreign alarm

Focus group map:

| Focus group | Purpose | Reward direction | Risk or tradeoff |
| --- | --- | --- | --- |
| Scent of ore | Marks adjacent resource-rich states as preferred targets. | AI targeting, visible war goal or target marker if supported | enemy gets clearer warning |
| Rich ground calling | Improves capacity from mid-value resource states. | faster automatic brood from 20 to 99 resource states | stronger anti-Host coalition interest |
| Old resource memory | Gives special benefit for states with same resource as origin. | temporary attack or spawn speed near matching resource | narrow target bias |
| Empty ground disdain | Reduces incentive to occupy resource-poor states. | fewer wasted fronts, better AI | may ignore strategic empty corridors |
| Hunger capstone | Improves resource capacity refresh and late-game world-end progress. | capacity stability, continental maw progress | higher world threat |

The lane should not break the user's capacity cap. It can speed deployment or improve quality, but a non-origin state still caps at 10 divisions.

## Stone hide lane

The stone hide lane makes divisions harder to damage.

Narrative role: cave bodies harden through minerals and pressure.

Mechanical role:

- increases armor and hardness
- reduces speed or supply flexibility
- raises enemy need for hard attack
- unlocks defensive state modifiers in hills, mountains, mines, and resource states
- can introduce a weakness to concentrated anti-tank, CAS, or heavy artillery if the implementation can show it

Focus group map:

| Focus group | Purpose | Reward direction | Tradeoff |
| --- | --- | --- | --- |
| Hardened bodies | Improves base armor of cave monster divisions. | armor, hardness | lower speed |
| Bullets on stone | Reduces soft attack effectiveness against Host. | defence, breakthrough against infantry | enemy anti-tank preparation becomes more important |
| Deep plates | Stronger elite bodies. | fewer but stronger division variant if paired with elder brood route | slower reinforcement |
| Mineral wounds close | Improves recovery in resource states. | reinforce rate or recovery near resources | weaker outside resource states |
| Stone hide capstone | Makes Host very hard to push without hard attack. | extreme defensive identity | major enemy anti-monster decisions unlock faster |

The implementation should make the counterplay clear. Players should see that hard attack, anti-tank, heavy artillery, CAS, and resource denial matter.

## Tunnel lane

The tunnel lane does not make the Host fast in open warfare. It lets the Host reduce some terrain and logistical penalties, and possibly shift between controlled resource states.

Narrative role: the Host moves through lower roads and old seams.

Mechanical role:

- improves movement or attack in hills, mountains, forests, resource states, and mining terrain
- enables limited underground redeployment between controlled resource states if implementation supports it
- improves defence of tunnel-linked states
- can create surprise attacks near resource clusters

Focus group map:

| Focus group | Purpose | Reward direction | Limitation |
| --- | --- | --- | --- |
| Lower road sense | Reduces penalties in rough terrain. | terrain modifiers | no open blitz speed |
| Mine rail ghosts | Uses existing extraction and rail routes for movement. | limited movement or planning bonus near rail and resource states | requires controlled route |
| Burrowed reserves | Moves broods between controlled resource states. | redeployment event or decision | cooldown and resource state requirement |
| Under the forts | Helps against static lines slowly. | siege or fort reduction | still slow |
| Tunnel capstone | Makes resource clusters hard to isolate. | defensive network among resource states | resource denial becomes more important |

The tunnel lane should support the Host fantasy without letting it become a fast tank army.

## Brood hierarchy lane

This lane contains the main internal choice. It should have mutually exclusive methods.

Mutual exclusive branch A, working label: swarm broods.

- more frequent smaller divisions
- faster capacity fill
- lower individual armor or organization
- better at covering wide fronts
- weaker against prepared hard attack

Mutual exclusive branch B, working label: elder broods.

- fewer stronger divisions
- slower capacity fill
- higher armor, breakthrough, and defence
- better at cracking fortified resource states
- worse at covering many fronts

Shared lead-in:

| Focus group | Purpose | Reward direction |
| --- | --- | --- |
| Brood ordering | Opens choice between swarm and elder routes. | shows current capacity and spawn method |
| Resource wombs | Improves origin nest support. | spawn quality or cooldown |
| Claim the deep hierarchy | Locks route method. | branch choice |

Swarm route payoff:

- reduces delay between captured resource and new division
- increases number of low-strength broods up to capacity
- may increase enemy encirclement opportunities because units are weaker
- good AI if Host has many fronts and moderate resource states

Elder route payoff:

- creates elite armored broods from high-resource states
- may use more capacity per division if implementation supports it
- good AI if Host faces fortified majors or anti-tank lines
- should not exceed the state capacity cap without a clearly documented conversion rule

## Surface terror lane

This lane affects enemy countries and population pressure.

Narrative role: the Host becomes public terror across settlements and cities.

Mechanical role:

- increases enemy panic in nearby or occupied states
- creates population flight or local disruption
- weakens enemy stability or state output near Cave Host fronts
- raises world threat and coalition response
- can unlock harsher evacuation and anti-monster decisions for humans

Focus group map:

| Focus group | Purpose | Reward direction | Backlash |
| --- | --- | --- | --- |
| First city fear | Adds enemy panic near captured VPs. | state disruption near front | foreign response grows |
| Emptying streets | Increases evacuation pressure and population flight. | enemy local output loss | stronger anti-Host decisions |
| Night roads | Disrupts enemy movement near Host fronts. | planning or speed penalty to enemies | limited by terrain and state control |
| Names in the shelters | Increases global fear if Host has killed many civilians. | world threat pressure | accelerates alliances against Host |
| Surface terror capstone | Makes Host a global fear actor. | strong enemy disruption | major world reaction and super-event aftermath threshold |

This lane should be strong. It also makes the world more willing to cooperate against the Host.

## Continental maw lane

This is the late route toward world-end.

Narrative role: the Host stops being a state invader and becomes a continental underground system.

Mechanical role:

- tracks continent control progress
- improves resource target logic within the chosen continent
- unlocks stronger effects when holding resource clusters
- increases world-end readiness
- changes world threat and super-event eligibility

Entry conditions should require meaningful success:

- Host controls several resource-rich states
- Host has stable origin or replacement nest
- Host controls a land corridor or enough territory on one continent
- chaos is high enough for late progression
- world-end not already fired

Focus group map:

| Focus group | Purpose | Reward direction |
| --- | --- | --- |
| Roots of the continent | Marks the continent where Host is strongest. | continent progress display or hidden tracker |
| Resource knots | Targets high-resource states in the same continent. | war goals or AI priority |
| Beneath every border | Reduces border relevance inside the continent. | movement, planning, or state pressure |
| The continent opens | Prepares world-end trigger. | world-end progress and super-event readiness |
| Continental maw capstone | Supports terminal world-end if continent control and chaos conditions are met. | world-end scenario branch |

The capstone should not fire world-end by focus alone. It should support the trigger. The world-end still requires the mapped world state.

## Branch interaction

The tree should reward combinations:

| Combination | Result |
| --- | --- |
| Hunger plus swarm broods | many resource-driven fronts, weaker individual units |
| Hunger plus elder broods | fewer strong monsters from high-resource states |
| Stone hide plus elder broods | terrifying siege units, very slow |
| Tunnel plus swarm broods | broad pressure through resource clusters |
| Surface terror plus continental maw | faster global response and higher world-end pressure |
| Stone hide plus surface terror | hard-to-kill city attackers, but human anti-armor response grows |
| Tunnel plus hunger | resource-state hopping and better target selection |

Branches should not all be mutually exclusive. The brood method branch is the main mutually exclusive path. Other lanes can combine, with route pacing and focus prerequisites controlling depth.

## Focus AI

Cave Host AI branch preferences:

| AI situation | Preferred branches |
| --- | --- |
| many weak neighbours | hunger, swarm, tunnel |
| major fortified neighbour | stone hide, elder broods, tunnel |
| resource-rich continent | hunger, continental maw |
| losing fronts | stone hide, tunnel, elder broods |
| surrounded but resource states nearby | tunnel, hunger |
| high civilian population nearby | surface terror if high chaos, otherwise hunger |
| near world-end threshold | continental maw, hunger, surface terror |
| enemy has strong hard attack | tunnel, swarm, resource targeting rather than direct siege |

AI should not take continental maw if the Host is tiny, lacks resource states, or the world-end branch is disabled.

## Focus icon assignment

Use the asset prompt and focus icon reference folder.

| Lane | Icon count direction | Motif direction |
| --- | --- | --- |
| Opening trunk | 5 to 7 | origin nest, cave mouth, first brood, mineral crown |
| Hunger lane | 5 to 7 | ore scent, resource vein, claw over resource, glowing seam |
| Stone hide lane | 5 to 7 | stone plates, bullets breaking, heavy shell, mineral armor |
| Tunnel lane | 5 to 7 | lower road, mine rail, underground route, cracked fort |
| Brood hierarchy | 6 to 8 | many brood shapes, elder shape, nest cluster |
| Surface terror | 5 to 7 | abandoned street, evacuation lanterns, city shadow |
| Continental maw | 5 to 6 | continent cracks, resource nodes, multiple cave mouths |

The implementation can create more or fewer focuses if it preserves branch function and depth. Every final focus needs a proper icon.

## Cave Host focus completion standard

The Cave Host tree is incomplete if:

- it is a single vertical line
- it uses ordinary political or industry rewards as filler
- it lacks an opening trunk, method branches, and late world-end route
- it lacks AI weights
- it has no icon direction or repeated generic icons
- it does not interact with resource capacity
- it does not change Cave Host unit behavior
- it does not support the world-end branch
