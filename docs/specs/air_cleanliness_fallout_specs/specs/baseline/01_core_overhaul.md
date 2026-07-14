# Air Cleanliness and Fallout World-End Source Spec, Part 1 Core

Canonical status: accepted baseline design, corrected for independent Fallout ownership and extended by the living-world specs in this package.

Working event folder label, not final localisation: `docs/specs/air_cleanliness_fallout_specs/`.

This spec expands the existing Air Cleanliness system into a visible atmospheric crisis layer and makes Fallout a true campaign overhaul. Air Cleanliness continues to track contamination in basis points and uses the accepted 25, 50, 75, and 100 percent escalation bands. At 100 percent, Fallout becomes eligible through the dedicated Fallout request system. Legacy non-Fallout hooks and normal super-event wiring are migration targets. The campaign continues through a total map, government, economy, focus-tree, country-package, and event-layer rewrite.

## Design promise

Air Cleanliness must stop being only a number in the Chaos Meter. It becomes the atmosphere that every country lives inside. Players should see winter bands on a mapmode, watch state categories collapse, decide whether to spend scarce resources on filters and shelter agriculture, and understand why the world becomes impossible to govern before the final Fallout transition.

Fallout is a shared terminal-overhaul scenario available to several collapse causes. Any route that destroys the air can send the world into Fallout. The normal path is gradual collapse after contamination exceeds 100 percent. The cinematic path is instant collapse, such as Final Silence or a manual scenario that uses a thermonuclear strike on every province and then fires Fallout after one week.

## Trigger doctrine

Fallout can begin through three paths.

| Path | Trigger idea | What the player sees |
| --- | --- | --- |
| Gradual atmospheric collapse | Global contamination exceeds 100 percent and the world fails the terminal stabilization roll. Higher contamination, severe winter, global deaths, and ruined food states increase the chance. | The black-screen sequence interrupts ordinary play after escalating winter flavour and map damage. |
| Scripted apocalypse bridge | A world-end event such as Final Silence explicitly requests Fallout as its aftermath. | The previous event produces its own ending beat, then the Fallout black screen begins after a short delay. |
| Manual scenario | The manual Fallout scenario uses the next free live scenario id, thermonuclear-strikes every valid province, waits seven days, then requests Fallout. | The map is visibly destroyed first. The black screen then covers the processing and narrative transition. |

The user instruction overrides the old world-end rule that required chaos above 1000. Fallout can use chaos above 1000 as one possible pressure source, but it must not require it. Air contamination above 100 percent or a scripted terminal event is enough.

## Legacy Fallout presentation cleanup

Remove every legacy Fallout caller and presentation hook outside the dedicated Fallout system. All Fallout events belong in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`. Fallout uses a black scripted GUI overlay, timed centered text, and the world rewrite. It does not use a normal super-event slot, quote, button, image, or audio id.

## Air Cleanliness system layers

Air Cleanliness is split into four readable layers.

| Layer | Scope | Player purpose | Main effects |
| --- | --- | --- | --- |
| Global contamination | Global basis points | Shows whether the world can recover | Thresholds, treaty pressure, world-end eligibility |
| Winter phase | State and global summary | Shows how the sky affects a place | Population loss, building damage, supply, food, movement, attrition |
| Fallout exposure | State variable | Shows radiation and dust danger | Deaths, mutations, wasteland drift, shelter demand |
| Recovery infrastructure | Country and state | Gives players agency before collapse | Filters, shelters, greenhouse agriculture, decontamination, evacuation |

## Natural atmospheric sources

Large wildfire smoke, volcanic eruptions, ashfall, and massive-eruption aftermath contribute to global Air Contamination through Event 013 physical impacts. Wildfire contributions begin at regional severity. Volcanic and ash families can contribute at every resolved severity because their smallest values remain negligible.

All natural sources feed one decaying global reservoir with a hard `4 bp` monthly ceiling, equal to `0.04 percent` Air Contamination. No number of affected states may raise that monthly contribution above the ceiling. The reservoir must use physical impact identity to reject duplicate registration, include regional spread and chained ash impacts, and decay through the existing host-owned monthly Air Cleanliness update. It must not add another periodic world iterator.

Natural sources may reinforce an existing atmospheric crisis, but they are not a fast independent route to Fallout. Chemical contamination and nuclear fallout remain the dominant sustained sources.

## Global atmospheric thresholds

The existing basis-point thresholds remain, but each threshold now activates visible gameplay.

| Contamination | Global name, working label | Player-facing behaviour |
| ---: | --- | --- |
| 0 to 24 percent | Ordinary air | Recovery can still win without extraordinary policy. Local contaminated states still matter. |
| 25 to 49 percent | Stinging air | Outbreak spread and respiratory events increase. Cities begin mask and clinic flavour events. |
| 50 to 64 percent | First winter | Mild winter phases begin in vulnerable states. Agriculture, movement, and repair suffer. |
| 65 to 74 percent | Dirty summer | Some warmer states skip snow but suffer dark rain, crop rot, and coastal fog. |
| 75 to 89 percent | Severe winter | Treaty systems harden. Winter phases become visible in most of the map. State population begins monthly loss in high exposure regions. |
| 90 to 99 percent | Terminal sky | Strong winter, food collapse, supply failures, and government-break events become common. |
| 100 percent and above | Irreversible atmosphere | Contamination cannot naturally recover below 100 percent. State categories degrade toward wasteland. Fallout world-end checks begin. |
| Above 100 percent | Deepening terminal pressure | Fallout eligibility remains active. Higher contamination changes urgency, state grades, winter severity, and request chance, but no separate 1000-percent threshold is required. |

## State winter phase ladder

Every state stores a winter phase. The global phase is a summary. The mapmode should show each state's phase.

| Phase | Working label | Typical causes | Core state effects |
| ---: | --- | --- | --- |
| 0 | Clear interval | Low contamination, strong recovery, low fallout exposure | No winter modifier. |
| 1 | Haze | 25 percent contamination, chemical clusters, nearby fallout | Small monthly population pressure, local clinic events, slight construction and training penalties. |
| 2 | Soot veil | 50 percent contamination, high industrial smoke, repeated fallout | Lower supply throughput, slower repairs, mild crop and manpower loss, air mission disruption. |
| 3 | Black snow | Severe winter, high latitude, state fallout intensity | Real monthly death tick, building damage chance, stronger attrition, infrastructure decay. |
| 4 | Long winter | 75 percent plus, repeated fallout, food collapse | State category decay begins. Civilian factories and infrastructure can be disabled or damaged. Refugee pressure rises. |
| 5 | Dead sky | 100 percent plus or scripted terminal aftermath | Population loss, heavy building damage, resources disrupted, category downgrades, ordinary recruitment collapses. |
| 6 | Fallout night | Active Fallout world-end | State is rewritten into a Fallout terrain class. It may become wasteland, dead city, bunker city, greenhouse refuge, mutant biosphere, or scavenger zone. |

## Regional climate and exposure logic

The phase should not be random global punishment. It should use state identity.

| State trait | Winter tendency | Special design note |
| --- | --- | --- |
| High latitude continental breadbasket | Faster severe winter | Hardest crop collapse and high refugee pressure. |
| Dense metropolis or industrial center | Faster soot and fallout | More building damage, higher death spikes, more dead-city salvage later. |
| Rural low-target region | Slower direct damage | Can still suffer hunger through trade and supply collapse. |
| Southern Hemisphere island or coastal refuge | Lower winter severity | Can become late-game food or naval survival center, but piracy and isolation matter. |
| Mountain state | Slower fallout drift but harsher winter | Strong shelter survival, weak agriculture, good bunker countries. |
| Desert state | Less snow, worse water | Dirty sun and water scarcity replace black snow events. |
| Jungle or tropical state | Less cold, more disease | Rot, fungal outbreaks, contaminated floodwater, and mutant flora events. |
| Major port | Cleaner air if remote, severe collapse if targeted | Can become a rationing port city, convoy fortress, or dead harbor. |

## State population effects

Winter phases must reduce real state population through the existing Deaths system when appropriate. Phase 1 should be mostly flavour and small pressure. Phase 3 and higher should be visibly harmful. Deaths should scale by state population, buildings, shelters, healthcare, local winter phase, state category, and whether the state has active fallout.

Population effects should distinguish direct deaths from displacement. Direct deaths feed the Deaths tab. Displacement can lower local population and add refugee pressure to adjacent or safer states. Refugee pressure can unlock new decisions, local unrest, manpower recovery, and faction recruitment.

## Buildings and state category effects

The winter phases must affect more than country modifiers.

| Target | Phase 1 to 2 | Phase 3 to 4 | Phase 5 to 6 |
| --- | --- | --- | --- |
| Infrastructure | Small repair speed and supply penalties | Damage chance, rail disruption missions | Large damage, state may lose rail value, wasteland conversion possible |
| Civilian factories | Output malus in severe states | Damage chance and conversion to shelters | Many factories disabled, later salvageable as ruins |
| Military factories | Slower output and worker illness | Damage chance, resource shortage | Disabled or converted into scrap depots, bunker workshops, or mutant forges |
| Dockyards | Port throughput pressure | Dead harbor events, convoy loss | Port may close unless sheltered or defended |
| Airbases | Air mission disruption | Ground crew loss and runway ice | Airbase disabled or becomes scavenger runway |
| Supply hubs | Throughput loss | Emergency rail missions | Critical survival objective or destroyed depot |
| State category | No change | One-step downgrade chance after sustained phase 4 | Stepwise downgrade toward wasteland or special Fallout category |

State category degradation should be slow before Fallout. The player must have time to react. After Fallout, the map rewrite can change categories immediately based on damage grade.

## Recovery and adaptation

Before Fallout, recovery must be hard but playable. Countries should have decisions and missions that target state-level problems.

| Response family | Costs | Best use | Risk |
| --- | --- | --- | --- |
| City filter retrofits | Civilian factories, support equipment, stability | Dense population and industry | Can fail if bombed or if power grid collapses |
| Mask and clinic drives | Infantry equipment, support equipment, political capital | Phase 1 to 3 state pressure | Raises demand and can create panic events |
| Greenhouse conversions | Civilian factories, fuel, steel, electricity proxies | Food survival in severe winter | High output if protected, severe loss if the state is bombed |
| Shelter agriculture | Building slots, manpower, support equipment | Bunker states and mountain states | Low productivity but resilient |
| Ash clearing battalions | Command power, trucks, infantry equipment | Railways and cities | Attrition, casualties, and condemnation if forced labour is used |
| Controlled evacuation | Trains, convoys, stability, receiving-state capacity | Save population from phase 4 and 5 states | Refugee politics and disease risk |
| International cleaning days | Treaty members, convoys, support equipment | Reverse phase 1 to 3 in selected states | Fails in phase 5 unless protected by shelters |

## Flavour event families with real effects

These are event families, not final localisation. Implementation should write final in-world text from these directions.

| Event family | Trigger | Actual effect |
| --- | --- | --- |
| Grey milk | Rural state enters Phase 2 | Adds short food pressure, lowers local population growth, unlocks livestock culling decision. |
| The first ash school | High-population state enters Phase 2 or 3 | Adds temporary stability hit, lowers recruitable population in state, can be mitigated by shelter schools. |
| Rail crews in masks | Rail or supply hub state reaches Phase 3 | Damages infrastructure or starts a timed mission to protect the rail crews. Success improves supply throughput. |
| Frozen transformer yard | Industrial state reaches Phase 3 in winter climate | Damages civilian or military factory. Power retrofit decision can block repeats. |
| Hospital airlock | City state with clinics reaches Phase 3 | Costs support equipment to reduce death tick, failure increases deaths and panic. |
| The orchard inventory | Food-producing state reaches Phase 3 | Player chooses to burn, ration, or preserve crops. Each changes food, stability, and local mortality. |
| Dirty harbor | Port state reaches Phase 3 or fallout exposure | Convoy losses, dockyard damage, or port closure mission. |
| The masks market | Any country with several Phase 1 states | Black market event adds corruption or grants short mask stockpile at stability cost. |
| The children cough in code | Phase 4 state with high fallout | Adds a strange research lead and population loss. Can seed mutant-country later if ignored. |
| Greenhouse miracle | Protected state in Phase 4 survives six months | Upgrades state to greenhouse refuge candidate, improves food and national morale. |
| Shelter riot | Shelter capacity below population pressure | Damages buildings, creates deaths, and can spawn a bunker militia. |
| Clean day betrayal | Treaty cleaning operation in a state owned by a violator | Ends treaty aid and increases condemnation. |
| Snow over the desert | Desert state reaches severe global winter | Water scarcity and local unrest replace ordinary crop failure. |
| Warm island rumours | Remote island has low phase while world is high phase | Migration pressure, naval raids, and possible refuge-government route. |
| The dead station | State with damaged infrastructure and high deaths | Opens salvage mission after Fallout or immediate repair mission before Fallout. |

## Fallout as a shared aftermath

Fallout should be a common terminal aftermath for multiple world-end sources. The cause should be recorded.

| Cause memory | Example source | How the aftermath differs |
| --- | --- | --- |
| Nuclear exchange | Manual scenario or mass nuke use | More dead cities, EMP collapse, military bunkers, blast wastelands. |
| Air collapse | Contamination passes 100 percent through gradual pollution | More sick cities, plague-adjacent events, treaty remnants, slow government failure. |
| Final Silence | Holy Realm terminal aftermath | More black-screen religious dread, more impossible landscapes, altered survivor cults. |
| Chemical saturation | Massive doomsday chemical releases | Toxic fog, gas-mask societies, chemical brigades, poisoned rivers. |
| Biological follow-through | Extreme world disease plus air collapse | Quarantine city-states, sterilization regimes, mutant disease countries. |

The core Fallout map rewrite stays shared. Cause memory changes flavour, state grades, successor identity pools, focus-route availability, achievements, and the first decade of content.
