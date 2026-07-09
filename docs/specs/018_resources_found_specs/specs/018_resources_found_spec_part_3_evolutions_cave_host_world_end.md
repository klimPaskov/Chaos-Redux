# Event 018 Resources Found, Part 3 Evolutions, Cave Host, and World-End Scenario

All names in this file are working labels only. They are not final localisation.

## Baseline stages versus evolutions

The event has ordinary baseline stages and four evolution stages. Ordinary stages describe the lifecycle of one resource field. Evolutions change what the event can become and how a first firing opens under high-chaos conditions.

Ordinary baseline stages:

| Stage | Role |
| --- | --- |
| Discovery | The field is found and resources are added. |
| Boom | The owner invests, surveys, trades, and protects the site. |
| Politicized | Foreign interest, concessions, smuggling, and border pressure grow. |
| Deepened | The owner pushes below ordinary extraction and below pressure rises. |
| Sickened | Workers suffer unexplained symptoms and population loss begins. |
| Public danger | Monsters become public and attacks reach settlements. |
| Breach countdown | The owner has a final chance to close, evacuate, or collapse shafts. |
| Host emergence | Evolution IV creates the Cave Host if the site remains open. |
| War and aftermath | The Cave Host expands, is contained, is defeated, or reaches world-end conditions. |

These are not all logged as evolutions. Evolution logs should record the actual evolution milestones, not every ordinary stage.

## Evolution entry path rule

Each evolution has two possible entry paths.

Active-event evolution means the event has already created a field. The evolution changes that active field through new decisions, incidents, values, or actors.

Pre-fire evolved opening means the event has not fired yet in the campaign or has no active primary deep site. The first or next firing opens in a more intense form because the world state has already reached the evolution level.

The implementation must not make evolutions happen instantly just because chaos reaches a threshold. Evolutions should use pacing and chance, usually with mean-time logic influenced by extraction pressure, field richness, foreign interest, worker safety, public panic, and chaos tier. Pre-fire evolved openings can be instant at event firing because they change the opening package rather than mutating an active field.

## Evolution I, larger discovery and international pressure

Working label: rich seam evolution.

### Role

Evolution I makes the discovery larger and politically important. The site becomes a strategic prize. The deposit can be richer, foreign countries become more active, and demilitarized field pressure can appear.

### Active-event evolution

If a field is already active, Evolution I can add another large discovery inside the same state. The new resource roll is random. It can select the same resource type as before. Repeated same-resource rolls stack. The field richness rises, foreign interest rises, and the owner receives new decisions around concessions, nationalization, border commissions, and demilitarized pressure.

Active changes:

- add one or more additional resource deposits to the active state
- raise field richness and local dependence
- unlock richer concession offers
- unlock demilitarized field pressure if the state is near a border
- increase chance of border crisis and smuggling
- add state boom modifier upgrade
- record an evolution log with actor owner and state context

### Pre-fire evolved opening

If Event 018 has not fired before, the first firing at Evolution I opens as a larger discovery. It should add several large deposits in the same state. Resource type is rolled separately each time. If the same type appears more than once, that resource becomes absurdly high in the state. The owner still sees an ordinary public discovery, but the event detail and decision category immediately make the field feel nationally important.

Pre-fire package:

| Element | Direction |
| --- | --- |
| Resource additions | Several large rolls in one valid state. |
| First popup | Discovery is larger and attracts immediate outside attention. |
| Owner decisions | Survey, concession, security, and border commission families open immediately. |
| Foreign interest | Starts higher than baseline. |
| Hidden danger | Slightly higher below pressure, but no public strange content yet. |

### AI and containment

AI countries can benefit from Evolution I without pushing the cave branch. Stable AI should often accept foreign trade or survey confidence. Aggressive AI can militarize the site and risk border crises.

## Evolution II, sickness and the Wasting Cut

Working label: wasting cut evolution.

### Role

Evolution II introduces the first clear unnatural consequences. Workers become sick. Equipment corrodes or becomes brittle. People near lower galleries lose strength. Population loss begins in the resource state if the owner keeps the site active. Cave incidents are still not fully public. Workers, doctors, miners, and security crews know something is wrong, but ordinary civilians may only see funerals, cordons, and closed roads.

The spec should avoid final prose that says the event is a warning. It should show fear and uncertainty through symptoms, disappearances, strange mine conditions, and local behaviour.

### Active-event evolution

Evolution II can trigger on an active deepened field when extraction pressure and below pressure are high enough. It unlocks sickness decisions and population loss. It also increases the reward for continuing extraction because more resource may be found in deeper strata.

Active changes:

- unlock worker safety and medical decision tier
- start ticking population loss in the state if the site remains active
- add sickness incidents tied to worker safety and extraction pressure
- allow more resource to be found suddenly by deep crews
- add cave incident events where workers vanish or are attacked underground
- expose below pressure indirectly through dynamic status text
- increase foreign concern if concession workers are affected
- record evolution log with owner actor and state context

Population loss should use the shared deaths system. It should be meaningful but not instantly catastrophic. It should scale with state population, extraction pressure, worker safety, local dependence, and chaos tier.

### Pre-fire evolved opening

If the event opens for the first time at Evolution II, it should still start with a discovery and not immediately show public monsters. The opening field is larger than baseline and begins with unsafe-extraction flags. Worker sickness appears sooner after exploitation starts. The player should get time to respond with safety actions and closure before public danger.

Pre-fire package:

| Element | Direction |
| --- | --- |
| Resource additions | Several large deposits, possibly concentrated in repeated resource types. |
| Starting field status | Starts closer to deepened, not public danger. |
| First decisions | Safety, medical camps, and cautious extraction are available early. |
| Hidden danger | Below pressure starts higher. |
| First strange content | Worker health and underground incidents appear after a short stage, not in the first popup. |

### Monster-in-cave incidents

Evolution II underground monster content should remain local to the site. It can include missing workers, damaged galleries, strange wounds, and security patrol losses. It should not use public city attacks yet. It should create decisions to send armed teams, seal lower galleries, rotate workers, and compensate families.

Mechanically, these incidents:

- reduce state population or manpower through deaths system
- lower worker safety
- raise public panic only slightly or not at all
- raise below pressure if ignored
- reduce extraction pressure if the owner chooses safety
- raise field richness if the owner exploits the newly exposed galleries

## Evolution III, public attacks and every-resource surge

Working label: public breach evolution.

### Role

Evolution III makes the discovery unusually rich and chaotic. If it appears as a pre-fire opening, the state gains a very large deposit of every resource. If it evolves during an active field, the site begins producing strange finds and public attacks. Monsters become visible outside the caves. People leave cities, population drops, and the owner must decide between evacuation, hunts, and closure.

The site can still be closed during Evolution III. Closure removes all event-added resources from the state and prevents Evolution IV. This is mandatory.

### Active-event evolution

Active changes:

- add large deposits, possibly every resource if the field has reached very high below pressure
- unlock public panic value
- unlock evacuation decisions
- unlock armed cave hunts and city protection missions
- unlock emergency closure and shaft-collapse decisions
- start monster attack events in the discovery state and nearby high-population or VP areas
- cause population loss in cities and mining settlements
- create refugee pressure or local construction disruption
- increase chance of foreign military interest and intervention
- record evolution log with owner actor and state context

The player should be able to manage this stage until Evolution IV. Hunts and evacuations are costly but viable. Closing is expensive and removes the resources, but it is the surest prevention route.

### Pre-fire evolved opening

If the event first fires during Evolution III, the state receives a very large deposit of every resource. The opening must still be gradual. The first popup should be a massive discovery, not immediate public monster war. Strange events should begin soon after, then escalate quickly. The player must still have a visible chance to close the site before the final breach.

Pre-fire package:

| Element | Direction |
| --- | --- |
| Resource additions | Very large deposit of every resource in one state. |
| First popup | Enormous find that can change global trade routes. |
| First decisions | Exploitation, safety, foreign interest, and closure all open quickly. |
| Strange stage | Worker sickness and underground incidents appear early. |
| Public stage | Monster attacks escalate quickly if the owner keeps the site open. |
| Final prevention | Closure remains possible before the Cave Host appears. |

### Public monster attacks

Public attacks should create map-level fear. They can target:

- the discovery state
- the state capital or highest VP in the state
- nearby urban states
- rail hubs connected to the extraction route
- concession towns if foreign companies are present

Attack outcomes should scale with panic, worker safety, cave hunt success, state population, and local military presence. A strong military presence with anti-tank, artillery, or hard attack support should reduce monster impact. Ordinary infantry alone should be less effective.

Attack effects:

- population loss through deaths system
- public panic increase
- temporary state construction and production disruption
- local dependence shock
- foreign evacuation or concession withdrawal
- chance of foreign country receiving a news or report event
- Cave Host breach progress if attacks are not contained

### Hunts and evacuation

The monster hunt decision family should be expensive and concrete. It should use divisions in state, infantry equipment, support equipment, artillery or anti-tank, command power, and possibly army XP. A hunt can succeed, partially succeed, or fail.

Hunt success:

- reduces public panic
- lowers below pressure or breach progress
- lowers attack frequency for a time
- may reveal stronger monster armour, which points to hard attack weakness
- can increase military casualties

Hunt failure:

- military deaths
- public panic
- worker safety collapse
- local dependence shock
- faster breach countdown

Evacuation does not defeat monsters. It reduces population loss and panic. Evacuating the state should lower industry and construction output because workers are leaving. A player can choose to save people and lose economic output.

## Evolution IV, Cave Host emergence

Working label: Cave Host evolution.

### Role

Evolution IV creates the nonhuman cave monster country. It appears in the discovery state, led by a cave monster, and declares war immediately on every neighbouring country. It is aggressive, slow, and extremely difficult to push back without severe hard attack. It does not use manpower or equipment. It grows automatically from the resources it controls.

### Trigger direction

Evolution IV should require:

- active public danger stage or high below pressure
- site not closed
- breach countdown failed or was ignored
- chaos high enough or evolution enabled
- not already having a Cave Host active unless the implementation supports multiple hosts
- origin state still valid
- no terminal world-end conflict already blocking it

The branch should not be a random punishment before the player sees public danger. The player should have had chances to reduce pressure, evacuate, hunt, or close.

### Spawn outcome

When Evolution IV fires:

- the origin state transfers to the Cave Host
- the previous owner loses the state and receives crisis consequences
- the Cave Host receives a cave monster leader and nonhuman country package
- the Cave Host gets initial divisions based on origin exploitation
- the Cave Host declares war on the previous owner and every neighbouring country with a land border to the origin state
- neighbouring countries receive a public crisis event or news event
- the world threat framework receives the Cave Host threat source
- a super-event fires for the emergence
- event log records the evolution with Cave Host as actor if possible, and original owner as context in event history

### Initial army size

The initial base army size depends on how exploited the starting state was. It is capped at around 30 divisions. Those starting divisions do not count toward future captured-resource calculations.

Recommended formula direction:

| Origin exploitation score | Initial Cave Host divisions |
| --- | --- |
| Low but breach happened | 8 to 12 slow armored divisions |
| Moderate exploitation | 13 to 20 divisions |
| Heavy exploitation | 21 to 27 divisions |
| Extreme exploitation or Evolution III all-resource field | 28 to 30 divisions |

Inputs to the score:

- field richness
- extraction pressure
- below pressure
- public panic
- number of expansion decisions taken
- whether every-resource surge happened
- whether closure was attempted and failed
- chaos tier

The cap should stay around 30 as the user requested. The origin state resource value can be absurd, but the initial spawn must not exceed the cap.

### Future division capacity

After emergence, Cave Host divisions are deployed automatically from captured resources. They cannot be trained manually. They do not use manpower or equipment. Controlled non-origin states provide capacity.

User rule translated into design:

- every 10 total resources in a controlled state can provide 1 cave monster division
- each controlled non-origin state contributes at most 10 divisions
- the origin state's initial army contribution is stored separately and does not count toward future calculations
- if a state has more than 100 total resource value, it still contributes only 10 future divisions
- if the Cave Host loses a resource state, its future capacity drops

The implementation should decide how to handle excess divisions when capacity drops. Preferred design: excess non-origin divisions decay through attrition, retreat underground, or receive a shrinking penalty over time rather than being instantly deleted in a confusing way.

### Division type

Cave monster divisions should be unique. They should be slow and heavily armored.

Design direction:

| Attribute | Direction |
| --- | --- |
| Speed | Very slow. They advance like a heavy siege mass. |
| Armor | Extremely high for the era. Ordinary infantry should struggle. |
| Hardness | High enough that hard attack matters. |
| Soft attack | Dangerous, but not the main identity. |
| Breakthrough | High in resource-rich terrain or near cave states. |
| Defense | High, especially in mountains, hills, caves, mines, and resource states. |
| Organization | Moderate. They should be hard to push, not fast. |
| Supply | Strange. They should not use normal equipment, but state resources should determine spawn capacity. |
| Manpower | None. |
| Equipment | None. |
| Weakness | Severe hard attack, anti-tank, heavy artillery, CAS, fort lines, resource denial, shaft collapse decisions. |

The player should understand through tooltips and combat results that anti-tank and hard attack are effective.

### Cave Host country behavior

The Cave Host is a special chaos country and an actual nonhuman country. It should be excluded from ordinary events that target normal civilian politics, human disease politics, migration diplomacy, or ideology spread unless a system explicitly supports nonhuman targets.

Country behavior:

- declares war on immediate neighbours
- prioritizes resource-rich states
- advances slowly toward high-resource and high-VP targets
- does not negotiate ordinary peace
- does not join normal factions
- does not use ordinary manpower or production
- receives automatic divisions based on resources
- can receive focus or decision upgrades that improve its monsters, movement, tunnels, and resource detection
- becomes a world threat source
- can trigger world-end scenario if it controls enough of a continent at chaos over 1000

### Cave Host defeat

If the Cave Host is defeated before the world-end scenario, the origin site can be sealed permanently. The victor or previous owner should get aftermath decisions to rebuild, remove monster state modifiers, decide whether to keep a small safe resource residue, and handle survivor settlements. The full event-added deposit should not simply return without consequence. If a defeated Cave Host had controlled many states or caused a broad war, a defeat aftermath super-event may be justified.

Defeat outcomes can include:

- global threat source removed
- Cave Host country annexed or deleted through designed cleanup
- origin state receives sealed depths modifier
- event-added resources in origin remain removed or reduced
- surviving resource states that Cave Host captured may keep damage modifiers
- countries that fought the Cave Host gain anti-monster lessons, reconstruction decisions, or hard attack research bonuses
- event log records defeat milestone

## Cave Host focus tree architecture

The Cave Host is a fixed-purpose nonhuman country, but it still needs route depth. It can have one central purpose and multiple internal methods.

Working tree identity: a slow siege organism that turns resource deposits into bodies.

Architecture map:

| Lane | Role | Mechanical payoff |
| --- | --- | --- |
| Opening trunk | Establish the Host after emergence and stabilize origin state. | Sets nonhuman rules, unlocks resource capacity display, starts neighbour war logic. |
| Hunger lane | Improves resource detection, target selection, and automatic division spawn timing. | Better resource-state prioritization and more reliable broods from captured resources. |
| Stone hide lane | Improves armor, defense, and resistance to ordinary infantry. | Stronger but slower units, higher hard attack requirement. |
| Tunnel lane | Improves movement in mountains, hills, mines, and resource states, not open blitz speed. | Reduced penalties and limited underground redeploy between controlled resource states. |
| Brood hierarchy lane | Alters division quality and spawn pattern. | Fewer stronger monsters or more weaker monsters, mutually exclusive internal method. |
| Surface terror lane | Increases panic, population flight, and enemy disruption around occupied states. | Strong enemy penalties and greater world threat, but stronger anti-monster coalition response. |
| Continental maw lane | Late route toward world-end threshold. | Marks continental consumption, unlocks stronger intercontinental spawn when world-end fires. |

Focus rewards should not be generic political power or stability. The Cave Host does not care about ordinary politics. Rewards should change spawn capacity, unit stats, target logic, terrain behavior, threat effects, enemy panic, and world-end progress.

## World-end scenario

Working label: continental breach world-end.

### Trigger direction

The world-end scenario triggers if the Cave Host owns or controls enough of a continent and global chaos is over 1000. The user specified that owning some continent should trigger world end. Implementation should choose a robust continent-consumption trigger that works with HOI4 state and continent data.

Recommended trigger direction:

- Cave Host controls more than half of the states in one continent, with a minimum state count so tiny island continents do not qualify too easily
- or Cave Host controls a strong majority of that continent's resource value
- and Cave Host holds at least one major VP or several resource states in the continent
- and global chaos is over 1000
- and no world_end flag is already set

The implementation should document the exact continent rule.

### World-end effects

When world-end fires:

- set global world-end flag
- set scenario-specific Cave Host world-end flag
- trigger world-end super-event
- mark Cave Host threat as terminal
- spawn stronger Cave Host outbreaks in other continents from resource-rich states
- grant Cave Host stronger monster division variants
- reduce or freeze incompatible ordinary event branches
- create emergency final-resistance decisions for surviving countries if implementation supports post-world-end play
- update event docs and spreadsheet world-end field

The world-end should not feel like an ordinary escalation. It should communicate that the world has learned the resource seams are connected and that the Cave Host can surface wherever the ground is rich enough.

### Intercontinental emergence

World-end intercontinental spawns should prefer resource-rich states outside the consumed continent. They can appear as deep gates, cave wounds, or resource nests. Each new continent should receive stronger monsters than ordinary captured-resource broods. The Cave Host should start appearing where the world economy is most dependent on resources, turning the original economic windfall into a global failure.

Spawn direction:

| Intensity | Spawn pattern |
| --- | --- |
| Minimum terminal | One to two resource-rich states on each other major continent. |
| Strong terminal | Multiple resource states and nearby high-population targets. |
| Maximum terminal | Resource-rich states across every eligible continent, stronger monster templates, and high panic effects. |

The world-end is allowed to be brutal. It is a terminal condition.

## Super-event roles

Super-event text, quotes, cultural remarks, and audio must be researched through the super-event workflow. This spec gives role direction only.

| Super-event role | Trigger | Direction |
| --- | --- | --- |
| Cave Host reveal | Evolution IV creates the Cave Host. | First public recognition that the resource field birthed a nonhuman country. Image should show the Host emerging from the excavated state. Quote and title require research. |
| World-end | Cave Host consumes a continent at chaos over 1000. | Terminal realization that the underground network is global. Image should show multiple continents or resource seams opening through earth. Quote and title require research. |
| Defeat aftermath | Cave Host defeated after becoming a global or near-global threat. | Reflection on victory with permanent damage and sealed depths. Use only if the threat lasted long enough and caused broad consequences. Quote and title require research. |

## World threat integration

The Cave Host should be integrated into the shared world-threat framework. It should not create a parallel one-off global threat flag as the only source of cooperation logic.

Threat source direction:

- add a Cave Host source flag
- refresh aggregate world threat while Cave Host exists and controls resource states or is at war
- clear source on full defeat and cleanup
- keep world-end source active permanently after terminal scenario
- document source in dynamic triggers documentation during implementation

Other events that affect normal countries should exclude Cave Host through shared special chaos and nonhuman classifications.

## Connections with other events

Event 018 can connect to other Chaos Redux systems without forcing dependency.

Possible connections:

| Other system or event type | Connection direction |
| --- | --- |
| Chemical and biological warfare | Sickness is not ordinary biowarfare, but deaths and contamination-adjacent panic can use shared death tracking. |
| Black Plague or disease systems | Nonhuman Cave Host should be excluded from ordinary disease politics, but human states near the site can suffer panic. |
| Natural disasters | Earthquakes, cave-ins, and ruptures can increase below pressure or expose shafts if both events are active. |
| Diplomatic panic | High foreign interest or border crisis can feed diplomatic panic cluster behaviour. |
| Economy negative events | Resource crash or sabotage events can interact with local dependence. |
| Formables or pacts | Countries threatened by Cave Host can form temporary anti-monster pacts if implementation adds this as broader content. |
| Zombies or other world threats | Multiple world threats should raise cooperation logic and avoid duplicate global threat flags. |

## Aftermath and reclamation

After the Cave Host is defeated, aftermath should depend on how far it spread.

Local aftermath:

- sealed origin state
- removal or reduction of event-added resources
- rebuilding decisions
- survivor compensation
- anti-monster guard missions
- long-term local fear modifier
- possible limited safe extraction only after heavy investment

Regional aftermath:

- countries that fought the Cave Host gain experience against armored nonhuman enemies
- hard attack or anti-tank research bonus direction can appear
- border states receive reconstruction missions
- foreign concessions are canceled or renegotiated
- local resource markets destabilize

Global aftermath:

- use only if Cave Host controlled many states or triggered world threat for long enough
- defeat super-event can fire
- postwar compact or resource inspection regime can appear
- world may gain a lasting suspicion of massive resource booms
- Event 018 future firings can have lower chance to reach deep branch because governments learned closure protocols, unless chaos is high

## Balance direction

The Cave Host should be frightening, not fair in ordinary terms. It is a special chaos country. Its units can be overpowered if the route earned them. Balance should come from slow movement, hard attack weakness, resource dependency, closure prevention before spawn, and the fact that its reinforcements depend on captured resource states.

Ordinary resource owners should have strong rewards because the baseline event is positive. The danger branch should be avoidable through costs and sacrifice. The final world-end branch should be terminal and harsh.
