
# Event 013 Natural Disasters specification

This is a source specification for Event 13, Natural Disasters. It is a planning handoff, not implementation code. It defines how the repeatable event should work after rework, how its disaster families escalate through evolutions, how the recovery system should play, how the cluster behaves, and how implementation should keep Event 13 aligned with the event log, deaths system, event details, decisions, assets, and the manual scenario surface.

All labels in this file are working labels and are not final player-facing localisation. The implementation pass must write final event, news, decision, mission, achievement, GUI, detail-window, and spreadsheet wording from the direction here.

## Playable promise

Natural Disasters should feel like a chain of credible disaster reports that repeatedly interrupts the world with believable local catastrophe, then escalates into regional crisis and abnormal high-chaos disaster seasons. It should not feel like a single popup that removes a few factories. One Event 13 firing creates one logged incident sequence. That sequence can contain several delayed impacts, warnings, recovery tasks, and aftermaths.

The event is low severity in the cluster because most individual sequences are local, but the repeatable nature makes it dangerous across a campaign. Its importance comes from accumulation, disruption, and timing. A country at peace can absorb a storm. A country fighting for its capital can lose a rail line, a port, or enough population to matter.

The player should learn three things.

- Disasters have families, and each family asks for different preparation.
- Recovery is a real system with costs, deadlines, and partial failures.
- Higher chaos makes the event less like weather and more like a hostile planetary pattern, without becoming a world-end branch.

## Event identity

| Field | Design value |
| --- | --- |
| Event ID | 13 |
| Event name | Natural Disasters |
| Type | Minor Repeatable |
| Cluster | Natural Disasters |
| Cluster member severity | Low at baseline, scaling upward through cluster member entries at higher chaos |
| World-end scenario | None |
| Manual scenario | Disaster Barrage, next free scenario ID, use SCN-007 if still free |
| Deprecated or boundary separate events | Event 99 Sandstorm, Event 51 Heat Wave, Event 28 Asteroid Incoming, Event 43 Massive Flood, Event 46 Unknown Placeholder, Event 47 BOOM, and any separate Meteor Shower placeholder are not Event 13 logic sources. Sandstorm active gameplay routes through Event 13. Event 46 remains inactive. Heat and meteor content use Event 13 rules where this spec says they belong. |
| Primary systems | Delayed incident scheduler, hazard family selection, state damage, population loss, deaths system, recovery decisions, aftermath missions, regional modifiers, event log, event details, cluster UI, manual scenario UI |

The event must not log every subdisaster as a separate random event. The source Event 13 firing writes one history row. Delayed subevents can show reports or news popups, but they do not call the random event history recorder again. Cluster-triggered repeated Event 13 member slots are different. Each member slot that truly fires Event 13 creates its own sequence and its own Event 13 history row, while the subevents inside that sequence stay subordinate.


## Deep disaster implementation addendum

The earlier catalogue level family list is not sufficient by itself. Implementation must also follow these source files as binding design material.

- `013_natural_disasters_external_event_boundary.md` defines the non reuse contract for Event 51 Heat Wave, Event 99 Sandstorm, Event 28 Asteroid Incoming, Event 43 Massive Flood, Event 46 Unknown Placeholder, Event 47 BOOM, and any separate Meteor Shower placeholder that exists in the repository. These entries are not valid logic sources for Event 13.
- `013_natural_disasters_individual_disaster_playbooks.md` defines the individual disaster playbooks. Each family has its own target logic, sequence shape, effect identity, aftermaths, death model, warning response, AI behaviour, category needs, and asset direction.
- `013_natural_disasters_big_disaster_decision_categories.md` defines the disaster specific country hit categories. The generic recovery overview is only a small incident hub. Serious, regional, catastrophic, and abnormal disasters must open the matching family category for the hit country.
- `013_natural_disasters_big_disaster_category_matrix.md` is the quick acceptance matrix for category coverage.

Big disasters must be big and unique. Do not implement floods, earthquakes, tsunamis, volcanoes, meteor showers, heat domes, sandstorms, wildfire fronts, drought famine chains, and moving storm corridors as the same generic effect with different text. Each needs distinct state targeting, distinct damage profile, distinct aftermath, distinct decisions, distinct missions, distinct AI priorities, and distinct visual direction.

## Core sequence model

One sequence has five conceptual layers.

| Layer | Player experience | Design notes |
| --- | --- | --- |
| Selection | The event chooses a valid anchor country, anchor state, and disaster family. | The state must be meaningful for that family. A coastal state can receive a tsunami, a desert state can receive a sandstorm, a mountain state can receive a mass movement, and a volcanic state can receive a volcano. |
| Warning | Some families can create a short warning or advisory. | Warnings should not always appear. Prepared countries, observatories, radar, good infrastructure, strong state control, and prior recovery investment increase warning chance. |
| Impact | The disaster hits one state or several states depending on intensity. | Building damage, population loss, temporary state modifiers, supply penalties, and death tracking happen here. |
| Aftermath | The country receives local or regional aftermath markers. | Aftermaths can include damaged rails, blocked ports, displaced population, water stress, ashfall, fire fronts, crater fields, contaminated water, or aftershock pressure. |
| Recovery | The country receives a limited set of decisions and missions. | Recovery can prevent chained consequences. Failed recovery can produce famine, refugees, local instability, further deaths, and renewed infrastructure damage. |

The sequence should be delayed, not instant. A baseline Event 13 firing should usually schedule two or three subdisaster reports across about 5 to 10 days. Larger evolved sequences use more subevents with shorter spacing, because a wider disaster season should feel like reports arriving from observatories, rail desks, port authorities, local governments, and relief stations at once.

## Delay model

Use a dynamic delay band based on the planned number of incidents, evolution stage, and chaos pressure.

| Sequence size | Intended delay rhythm | Rationale |
| --- | --- | --- |
| 1 incident | One report now, no internal delay needed. | Rare for a baseline light disaster. |
| 2 incidents | Second impact after 5 to 10 days. | The event feels larger than one popup without overwhelming the player. |
| 3 incidents | Delays of 4 to 8 days. | Baseline severe or early Evolution I rhythm. |
| 4 to 6 incidents | Delays of 2 to 6 days. | Regional disaster season rhythm. |
| 7 or more incidents | Delays of 1 to 4 days, with news throttling. | Evolution II, Evolution III, and manual barrage rhythm. |

The implementation should centralize delay values in script constants or a disaster tuning table. The scheduled hidden events should read a sequence variable so the UI can show that the same Event 13 sequence is still unfolding.

Delay should become shorter when chaos is higher, when a manual barrage is launched at high intensity, or when a disaster family naturally chains quickly. Tsunamis can follow major earthquakes after a short delay. Famine and refugee pressure should appear later because they are aftermaths, not immediate impacts.

## Disaster families

The disaster catalogue should be broad, but each family needs its own target logic and aftermath. The design uses natural hazard groups similar to geophysical, hydrological, meteorological, climatological, and extraterrestrial classes. The game should not show those academic labels unless they make a tooltip clearer. Player-facing text should focus on the affected place and the visible disaster.

### Baseline family set

Baseline should use a smaller set so the first version is readable.

| Working family | Valid target direction | Immediate effects | Aftermath direction |
| --- | --- | --- | --- |
| Flood | River, lowland, coastal, high rainfall, or built-up state. | Infrastructure, rail, civilian industry, local population loss, temporary supply penalty. | Floodwater cleanup, blocked rail, damaged housing, contaminated wells. |
| Storm | Coastal or inland state with enough population or buildings. | Airbase, port if coastal, infrastructure, civilian industry, local population loss. | Debris clearance, temporary air operations disruption, relief shelter pressure. |
| Earthquake | Urban, mountainous, fault-like, or high-building state. | Strong building damage, infrastructure and rail damage, population loss scaled by urban concentration. | Aftershock inspections, damaged hospitals, unstable bridges, possible delayed tsunami for coastal anchors. |
| Drought | Dry, agricultural, low infrastructure, or warm state. | Lower immediate building damage, longer population and supply pressure. | Water rationing, crop stress, famine risk, refugee pressure. |
| Wildfire | Forest, hills, dry states, or drought-affected state. | Infrastructure, civilian industry, population loss, local supply and movement penalty. | Firebreak missions, smoke damage, evacuated settlements. |
| Blizzard or cold wave | Cold, mountain, northern, or winter-affected state. | Infrastructure, rail, supply, local population loss, temporary attrition-like state modifier. | Road clearance, heating fuel shortage, stranded rail traffic. |

Baseline should usually fire one to three incidents. Only the first report needs a full popup unless a later impact hits the player, a major, a capital, or a region already strained by war.

### Expanded family set

Evolution I and later add more families. These are not all equally common.

| Working family | Target direction | Special notes |
| --- | --- | --- |
| Hailstorm | Agricultural, plains, airbase, or lightly industrial state. | Very low population-loss rate and low building damage, but can damage airfields and reduce local supply. |
| Sandstorm or dust storm | Desert, arid, Middle East, North Africa, Central Asia, Australia, and similar regions. | Replaces the separate sandstorm event. It should cause supply, airfield, visibility, and infrastructure disruption more than deaths. |
| Thunderstorm outbreak | Warm, humid, river, plains, or urban state. | Can branch into flood, hail, wind, or wildfire ignition. |
| Extreme wind event | Plains, coast, or airbase-heavy state. | Damages airbases, infrastructure, and civilian buildings. |
| Tropical cyclone | Warm coastal state, island, or port-heavy region. | Strong port, dockyard, airfield, infrastructure, and percentage-based population loss. Can apply storm surge to neighboring coastal states. |
| Wet mass movement | Mountain, hill, high rainfall, or recently flooded state. | Damages rails, infrastructure, supply hubs, and population in narrow state chains. |
| Dry mass movement | Mountain, hill, arid, or post-earthquake state. | Similar to wet movement, but more likely after drought, quake, or volcanic tremor. |
| Volcanic eruption | Volcanic region list or heuristic volcanic states. | Applies ashfall, infrastructure loss, percentage-based population loss, airfield disruption, and possible delayed lahar or tsunami. |
| Tsunami | Coastal state after quake, volcano, or meteor impact. | Strong population, port, dockyard, and infrastructure damage. Should arrive after a visible warning or delayed follow-up when possible. |
| Extreme heat wave | Hot or dry region. | Does not stack with the separate Heat Wave event. It should be local or regional and can dry out states for wildfire risk. |
| Extreme cold wave | Cold or winter region. | Stronger supply and population pressure than a blizzard, with less direct building damage. |
| Glacial lake outburst | Mountain and glacial states when state groups exist. | Rare, regional, and useful for Evolution I or II. |

### Abnormal family set

Evolution III unlocks abnormal high-chaos variants. These should be rare outside manual barrage mode.

| Working family | Gameplay identity | Important limit |
| --- | --- | --- |
| Meteor shower | Several separated impact states, crater aftermath, high population risk if urban. | It can be catastrophic, but it must not become a world-end scenario. |
| Airburst field | Medium-sized blast and shockwave over one or several states. | Keep it distinct from the BOOM event and from nuclear strikes. No condemnation. |
| Massive earthquake-wave | A regional seismic wave that damages several neighboring states. | This integrates the removed Earth Earthquake event. Event 46 becomes an unknown inactive placeholder. |
| Delayed ocean tsunami chain | A quake, volcano, or meteor impact creates delayed coastal impacts in a sea basin. | News throttling is mandatory. Only the main basin warning and major impact should be newsworthy. |
| Massive volcanic eruption | A selected volcanic region suffers strong damage, nearby states receive ashfall. | It can create temporary global or regional air and supply disruption, but no terminal volcanic winter branch. |
| Moving tornado or storm corridor | A scripted GUI map shows the forecast corridor and then the impact path updates as it moves. | The path must be state-driven and animated where possible. It should not hit every state in the world. |
| Skyfire hail or plasma storm | High-chaos rare variant using meteor and storm logic. | Use sparingly, with uncertain reports and no direct cosmic lore overexplanation. |

## Target selection philosophy

A natural disaster should hit a meaningful area, not a random empty state. The event can still choose rural states, but it should only do so when the family makes sense and when the impact produces readable consequences.

Target scoring should consider these factors.

- State population.
- Civilian factories, military factories, dockyards, ports, airbases, railways, infrastructure, supply hubs, and resources.
- Terrain and climate signals where available.
- Coastal, island, river, mountain, desert, forest, urban, and volcanic region group membership.
- Active war, front line proximity, current supply strain, and existing disaster aftermaths.
- Whether the target is the player, a major, a faction leader, or a country with high current chaos contribution.
- Avoidance of repeated hits on the same state unless an aftermath chain deliberately targets it again.

The implementation should support fallback state groups when exact climate or hazard data is not available. A family can have a primary state group and fallback heuristics. If no valid state exists for a family, that family should be skipped rather than forced onto a bad target.

## Population and death model

Event 13 must feed the shared deaths system. The population loss should reduce real state population and record civilian deaths through the shared death log. It should not only reduce manpower.

The death model must use dynamic population percentages. No state, country, disaster family, evolution, cluster slot, or manual scenario type may use a fixed absolute death amount as its impact rule. The implementation should compute a final loss rate for each affected state, then multiply that state rate by that state's current population. A state with ten times the population should take roughly ten times the absolute deaths when the same final loss rate applies. Dense Chinese, Indian, Japanese, Javanese, European, or other high-population states must therefore be capable of suffering much larger absolute death counts than sparse states hit by the same family and severity.

Use this design shape for every impact and every delayed aftermath tick.

```text
state_population_before_impact * final_dynamic_loss_rate = civilian_deaths_for_that_state
```

The final dynamic loss rate is built from family, severity, evolution stage, warning quality, evacuation state, local density, infrastructure condition, war disruption, stability, current aftermath, and recovery success. Constants may define family rate floors, family rate ceilings, severity multipliers, and modifier ladders, but they must be rate constants rather than flat victim counts. There should be no hidden absolute casualty cap that prevents a dense state from losing hundreds of thousands or millions when the dynamic rate is severe enough. Any safety ceiling should cap the percentage of that state's current population that can be lost, not the absolute number of people.

| Factor | Effect direction |
| --- | --- |
| State population | Multiplies the final loss rate into an absolute death count. It never adds a fixed number by itself. |
| Local population concentration | Raises the loss rate when dense settlements, urban concentration, ports, river deltas, or crowded evacuation routes make the disaster deadlier. |
| Building density | Raises the loss rate for earthquakes, airbursts, floods, cyclones, meteor impacts, and urban fires when built-up areas collapse or trap civilians. |
| Preparedness | Warning decisions, evacuation, shelters, observatories, firebreaks, and strong recovery lower the loss rate before the population multiplier is applied. |
| Infrastructure and rail | Strong networks reduce drought, cold, refugee, and rescue losses if intact. Damaged networks raise delayed loss rates through blocked relief and evacuation failure. |
| War state | Countries at war have worse evacuation and recovery, especially when the disaster hits a front, port, supply hub, rail artery, or occupied area. |
| Stability and war support | Low stability worsens evacuation and refugee aftermath. High war support can improve emergency mobilization but may increase exploitation of survivors for labor or military needs if routes exist later. |
| Evolution stage | Higher evolutions raise the loss-rate ceiling, unlock wider multi-state impact, and expand secondary losses. |
| Repeated aftermath | Unresolved famine, refugee pressure, ashfall, exposure, damaged water systems, or transport collapse causes additional percentage-based deaths over time. |

For multi-state incidents, calculate every affected state separately, then sum the population-derived results for the sequence. Do not calculate one fixed disaster total and divide it across states.

News thresholds should use the summed sequence deaths and affected-state importance. A sequence crossing one million deaths should always be eligible for meaningful news, subject to the existing news throttle and user settings.

Deaths should usually be modest at baseline because the rate is low and the affected area is small. Evolution II can produce very large regional totals when several populated states are hit or when relief fails. Evolution III must be allowed to cause multi-million civilian deaths when massive quakes, tsunamis, volcanic chains, moving storm corridors, or meteor showers hit dense states or several neighboring high-population states. Ordinary hail and sandstorms should usually have very low loss rates, so they should not become mass death events unless an extreme evolved aftermath creates a separate chain.

## Building and state damage model

Immediate damage should hit different building pools based on the disaster family.

| Building or value | Families that should commonly affect it |
| --- | --- |
| Infrastructure | Floods, storms, earthquakes, mass movements, wildfires, blizzards, drought aftermath, volcanoes, meteor impacts. |
| Railways and supply hubs | Floods, earthquakes, mass movements, blizzards, volcanic ash, tornado corridors, massive storm variants. |
| Civilian factories | Floods, earthquakes, cyclones, wildfires, volcanic eruption, meteor impacts. |
| Military factories | Earthquakes, cyclones, wildfires, meteor impacts, tornado corridors. |
| Dockyards and naval bases | Tropical cyclones, tsunamis, storm surge, coastal earthquake, volcanic tsunami. |
| Ports | Tropical cyclones, tsunamis, storm surge, earthquakes, volcanic ash cleanup. |
| Airbases | Hailstorms, sandstorms, storms, tropical cyclones, ashfall, extreme wind, meteor dust. |
| Forts and coastal forts | Earthquakes, tsunamis, storm surge, mass movements. |
| Anti-air and radar | Hail, wind, storms, meteor shower, ashfall. |
| Resources | Drought, wildfire, flood, volcanic ash, crater fields, mass movement. |

The player should not receive a flat factory loss every time. A flood that wrecks ports should feel different from a drought that eats stability and population over time.

## Warning and preparedness

Warnings make this event playable. They should not remove disaster danger, but they should let countries reduce losses when they invest.

Warning types by family should include these directions.

| Warning type | Families | Player action direction |
| --- | --- | --- |
| River or flood advisory | Flood, wet mass movement, tropical cyclone. | Move equipment, prepare pumps, place engineers, reduce rail and population loss. |
| Coastal evacuation | Tsunami, cyclone, storm surge. | Spend trains, trucks, convoys, fuel, and manpower to reduce deaths and port damage. |
| Seismic alert | Earthquake, volcano, tsunami. | Inspect bridges, evacuate dense districts, shut down ports, activate observatories. |
| Fire weather advisory | Wildfire, drought, heat wave, dry storm. | Build firebreaks, use fuel and support equipment, reduce wildfire spread. |
| Cold or blizzard advisory | Blizzard, cold wave. | Spend fuel, trains, and support equipment to keep supply open and reduce deaths. |
| Dust and airfield alert | Sandstorm, ashfall, meteor dust. | Ground aircraft, disperse equipment, prepare masks and airfield crews. |
| Skywatch alert | Meteor shower and airburst field. | Rare and imperfect, using observatory investment and chaos tier. |

Preparedness should scale with country capacity. A major can do more, but it may also have more high-value targets. A small country may have fewer options but can receive foreign relief earlier.

## Disaster Reports and Recovery Category

Evolution II should unlock the core recovery mechanic, but the baseline can already show limited recovery when a country is hit. The generic recovery category should be an overview and small incident hub only.

Working overview label, not final localisation: `Natural Disaster Recovery`.

The overview should show current active disaster count, worst active aftermath, recovery progress, displaced population pressure, transport damage, and whether foreign relief is open. It must not pretend that one generic list is enough for major disasters. Serious, regional, catastrophic, and abnormal disasters open a matching family specific category from `013_natural_disasters_big_disaster_decision_categories.md`. A country hit by a major flood gets Flood Relief Authority. A country hit by a major earthquake gets Seismic Emergency Authority. A country hit by a meteor shower gets Skyfall Emergency Bureau. The overview links and summarizes, while the family category owns the real decisions, missions, values, AI, and cleanup.

### Category phases

| Phase | Visibility | Content |
| --- | --- | --- |
| Quiet | Hidden or compact if no active aftermath exists. | May show a preparedness ledger only after the event has fired or after a focus or global setting unlocks it. |
| Warning | Visible during warnings. | Evacuate, reinforce, close ports, prepare hospitals, secure rail, stockpile water, observe skies. |
| Impact | Visible briefly after impact. | Rescue, clear roads, deploy field hospitals, reopen ports, ground aircraft, protect supply. |
| Recovery | Visible while state modifiers and aftermath variables remain. | Timed missions and repeatable decisions with escalating costs. |
| Regional crisis | Evolution II and III. | Shows regional ledger, refugee flows, follow-up risk, and selected target state or region. |

### Core recovery decisions

These are decision family directions. Final decision names belong to implementation.

| Decision family | Costs and requirements | Effects and risks |
| --- | --- | --- |
| Emergency evacuation | Trains, trucks, fuel, manpower, possible stability or war support cost. | Reduces civilian deaths and refugee pressure. Can damage production if overused during war. |
| Deploy rescue engineers | Support equipment, army XP, command power, manpower. | Repairs infrastructure and rail. Lowers follow-up death pressure. |
| Open relief corridors | Convoys or trains, relations or faction access, stability strain. | Allows foreign relief and reduces refugee pressure. Can increase foreign influence or dependency if later systems use that. |
| Flood barriers and pumps | Support equipment, fuel, civilian factory burden. | Reduces flood damage and wet mass movement follow-up. |
| Firebreak operations | Infantry equipment, support equipment, fuel, local supply requirement. | Reduces wildfire spread. Can fail in drought and high wind. |
| Port and airfield closures | Temporary production or mission penalty, convoys or command power. | Reduces port, dockyard, and airfield damage if used before impact. |
| Water rationing | Stability cost, war support cost, trucks, local infrastructure. | Slows drought, heat, and famine pressure. Can create unrest if repeated. |
| Ash and dust clearance | Support equipment, trucks, fuel, air XP for airfield recovery. | Removes ashfall, sandstorm, and meteor dust penalties. |
| Aftershock inspection | Army XP or command power, support equipment, engineers. | Lowers earthquake aftershock risk and bridge collapse. |
| Shelter reinforcement | Infantry equipment, support equipment, manpower. | Reduces population loss in blizzards, cyclones, and meteor showers. |

No major recovery family should rely mostly on political power. Political power can appear in diplomatic relief, public administration, and law adjustments, but the main cost palette should be physical resources, logistics, manpower, XP, stability, war support, and time.

### Missions

Missions should ask the country to do something. They should not ask the player to wait while a passive value becomes true.

| Mission family | Objective direction | Duration direction | Success | Failure |
| --- | --- | --- | --- | --- |
| Clear the rail belt | Repair or hold rail and supply state targets, possibly require supplied divisions in named states. | 90 to 180 days by scope. | Removes transport aftermath and lowers supply penalty. | Follow-up infrastructure damage and refugee pressure. |
| Reopen the port | Hold and repair the affected port state, spend convoys or dockyard burden. | 90 to 150 days. | Removes port closure and coastal relief opens. | Coastal trade penalty and local war support loss. |
| Contain the fire front | Keep required states controlled, spend fuel and equipment, prevent spread flags. | 90 to 120 days. | Stops wildfire spread and reduces deaths. | Fire spreads to a neighbor and burns industry. |
| Feed the drought belt | Maintain supply route, spend trucks and trains, keep stability above a dynamic threshold. | 120 to 240 days. | Prevents famine follow-up. | Famine and refugee pressure begin. |
| Clear ash from airfields | Spend support equipment and air XP, repair airbases. | 90 to 150 days. | Air operations normalize and ash deaths stop. | Long airbase penalty and transport disruption. |
| Inspect aftershocks | Control and repair target state, spend support equipment and army XP. | 90 to 180 days. | Lowers aftershock and collapse chance. | Aftershock damages a neighboring state or same state again. |
| Shelter the displaced | Spend manpower, trains, trucks, support equipment, and stability. | 120 to 210 days. | Refugee pressure decreases. | Neighboring states or countries receive refugee strain. |
| Track the corridor | Evolution III only, keep forecast state under observation and spend fuel or command power. | 30 to 60 days because storm corridor moves quickly. | Changes the path or reduces impact in one forecasted state. | The corridor hits with little preparedness. |

## Aftermath chains

Evolution II introduces chained aftermaths as a major feature. The chain should be family-specific.

| Primary disaster | Possible follow-up | Prevention direction |
| --- | --- | --- |
| Earthquake | Aftershocks, tsunami if coastal, bridge collapse, housing crisis. | Aftershock inspections, coastal evacuation, rail clearance. |
| Flood | Disease-like water pressure should be handled as contamination of water and displacement, not a full epidemic event. | Flood barriers, pumps, water purification, shelter mission. |
| Drought | Famine, wildfire, refugee pressure, unrest. | Water rationing, relief corridors, food stockpile missions. |
| Wildfire | Smoke damage, secondary fire spread, evacuated settlements. | Firebreaks, fuel logistics, local support, rain follow-up if random weather helps. |
| Volcano | Ashfall, lahar or wet mass movement, crop failure, tsunami if coastal. | Observatory alert, ash cleanup, coastal evacuation, rail clearance. |
| Cyclone | Flooding, storm surge, port closure, refugee pressure. | Coastal evacuation, port closure, flood barriers. |
| Blizzard or cold wave | Fuel shortage, stranded rail, local deaths, supply collapse. | Heating fuel, rail clearing, shelter reinforcement. |
| Sandstorm | Airbase closure, supply disruption, equipment loss, local population stress. | Airfield dispersal, dust clearance, convoy pause. |
| Meteor shower | Crater fields, fires, airburst shock, refugee pressure, sky panic. | Skywatch warning, shelter reinforcement, firebreaks, crater cleanup. |

Follow-ups should not all happen automatically. They should use weighted delayed events, with weights shaped by recovery progress and family variables. Fast recovery can prevent them.

## News and report policy

The player should not be spammed by every disaster, especially in Evolution II. The system should use a news gate.

A disaster report should be more likely when at least one of these is true.

- The player country is directly affected.
- The affected country is a major or faction leader.
- A capital, major port, or high-population state is hit.
- The death estimate crosses a meaningful threshold.
- A disaster chain creates refugees or famine pressure across borders.
- An Evolution II regional season begins.
- The first Evolution III abnormal disaster fires.
- The manual barrage reaches high or maximum intensity.

The report should identify the affected area clearly through dynamic state, country, or named region localisation. It should not say only that a random state was hit. The first sentence direction should name the state or region and the disaster family. Follow-up reports should name the specific secondary effect, such as a delayed wave, ashfall, fire line, or refugee movement.

## Event details window direction

The Event Details text for Event 13 should describe the premise and progression without listing raw effects. It should explain that the event records local and regional disaster sequences, that each firing can include delayed reports, that disasters can damage industry and population, and that later evolutions introduce regional damage, aftermath chains, recovery decisions, abnormal disasters, and a manual barrage. It should also state that no world-end branch belongs to this event.

It should not list exact death percentages, factory damage values, or hidden selection weights.

## Evolution architecture

Event 13 has baseline behavior and three evolution stages.

| Stage | Working label, not final localisation | Chaos and condition direction | What changes |
| --- | --- | --- | --- |
| Baseline | Local Disaster Reports | Available from the start. | One to three ordinary local disasters, delayed across a few days. Limited recovery. |
| Evolution I | Varied Local Disasters | Gathering Storm or higher, preferably after one prior Event 13 sequence or high chaos pre-fire opening. | More disaster families, more target variety, two to five incidents, slight increase in damage ceiling. |
| Evolution II | Regional Disaster Systems | Rising Chaos or Chaos Tier, with at least one prior disaster sequence or high chaos pre-fire opening. | Disasters can affect neighboring states, whole regions, and multiple countries. Recovery category becomes a central system. Aftermath chains appear. |
| Evolution III | Abnormal Disaster Age | Totalen Chaos or World Collapse, with prior regional disasters or manual high-intensity scenario. | Meteor showers, massive quake-wave, huge volcanoes, delayed tsunami chains, moving storm corridors, and animated map tracking. No world-end branch. |

### Active-event evolution

Event 13 is repeatable and usually not a persistent actor system, so active evolution means that already running sequences, active aftermath ledgers, and recovery categories receive new behavior without needing a fresh random firing.

When an evolution unlocks while active aftermaths exist, the implementation should do this.

- Mark the evolution in the Event Logs Evolutions tab once the milestone actually opens.
- Upgrade active decision category text and available recovery tools where appropriate.
- Allow future delayed follow-ups in the active sequence to use the newly unlocked family extensions if they fit the existing primary disaster.
- Do not retroactively strengthen impacts that already happened.
- Do not spawn an abnormal disaster immediately unless the manual scenario or a scheduled follow-up explicitly called for it.

### Pre-fire evolved opening

If Event 13 has not fired yet and the world is already at a higher chaos tier, the first firing can start in an evolved form.

- Evolution I pre-fire opening uses the expanded family set and a larger sequence.
- Evolution II pre-fire opening can start with a regional disaster system and immediately show the recovery category.
- Evolution III pre-fire opening can open with one abnormal family, but only if chaos and weighting make that appropriate. The first great rupture wave, first massive eruption, and first meteor cluster can each use a family-specific non-terminal super-event gate once per campaign.

## Evolution I, Varied Local Disasters

Evolution I changes the event from a small set of local hazards into a broad catalogue. The event remains low to medium severity. It still feels like observatories, transport boards, local authorities, and relief stations processing different reports, rather than the whole world breaking.

### New behavior

- Adds hailstorms, sandstorms, thunderstorm outbreaks, extreme wind, wet and dry mass movements, heat waves, cold waves, and rare volcanic signals.
- Allows multiple regions in one sequence, usually two to five incidents.
- Reduces internal delay compared to baseline when four or more incidents are selected.
- Slightly raises damage ceilings and dynamic loss-rate ceilings. These are percentage ceilings, not fixed death totals.
- Adds a basic warning phase for more families.
- Begins tracking family memory so repeated droughts, fires, floods, or storms can influence later sequence weights.

### Player pressure

The player should notice that recovery cannot be one generic button. A sandstorm asks for airfield and supply choices. A flood asks for pumps and rail repair. A cold wave asks for fuel and shelters.

### AI direction

AI should pick family-appropriate recovery actions when affected. It should prioritize capital states, supply hubs, ports, and high-population states. AI at war should prioritize supply and rail recovery over full population relief, unless the player is the affected country or the AI has high stability and enough stockpiles.

## Evolution II, Regional Disaster Systems

Evolution II makes disasters operate across regions and produces chained aftermaths. It should feel like a serious global pattern, but news must stay restrained.

### New behavior

- A primary impact can mark neighboring states for secondary damage.
- Several countries can receive related impacts in one sequence.
- Temporary supply penalties and state recovery modifiers become common.
- Recovery category shows regional aftermath values.
- Family chains unlock, such as earthquake to tsunami, drought to famine, wildfire to smoke, volcano to ash, cyclone to flood, and flood to displacement.
- Foreign relief and refugee decisions open.
- Affected countries can ask neighbors, allies, or major powers for aid.
- Neighboring countries can accept displaced people, harden borders, send relief trains, or exploit an enemy disaster through limited war readiness effects.

### Regional targeting

Regional systems should use an anchor state and a region set.

- Neighbor states are the first ring.
- Coastal sea basin targets are used for tsunamis and cyclones.
- River, mountain, and desert region groups are used when available.
- If the region contains too few valid states, the event should reduce scope instead of forcing bad targets.

### News throttle

Only the sequence opener, the worst impact, or the cross-border aftermath should show a major news event. Smaller impacts should be visible in the affected country's recovery category, local popups, and event details history, but not through world news spam.

### Recovery as a mechanic

At Evolution II, recovery becomes the main player-facing loop. The player should see what is unresolved, what can chain, and which decisions can prevent a worse phase.

## Evolution III, Abnormal Disaster Age

Evolution III escalates the event into high-chaos disasters that appear impossible in normal history. The player should still understand the system as disasters, not as magic countries or a terminal world end.

### New behavior

- Unlocks meteor showers, airburst fields, massive earthquake-waves, huge volcanoes, delayed ocean tsunami chains, and moving tornado or storm corridors.
- Allows map forecasts for storm corridors, volcano ash, tsunami basin warnings, and meteor shower clusters.
- Uses animated map assets where they clarify moving or spreading disaster state.
- Raises damage ceilings and dynamic death-rate ceilings for severe variants. These ceilings cap percentages, not absolute victims.
- Allows several states to take building damage in one abnormal incident.
- Creates stronger recovery missions and longer aftermaths.
- May fire a family-specific non-terminal super-event once each for the first great rupture wave, first massive eruption, and first meteor cluster. Later delayed impacts and later repeats should not fire additional super-events.

### Earth Earthquake integration

The separate Earth Earthquake event should be removed as active content and converted into an unknown inactive placeholder. All seismic warnings, massive quake-wave variants, delayed tsunamis, aftershock inspections, and seismic recovery ledgers belong to Event 13.

The placeholder should say in its catalog direction that no independent gameplay is active and that seismic disaster content is handled by Natural Disasters.

### Sandstorm integration

The separate sandstorm event should become a placeholder or routed wrapper. The active sandstorm gameplay belongs to Event 13 as a family-specific disaster.

### Moving storm corridor

The moving tornado or storm corridor should use the scripted GUI map.

- The forecast path appears first with low confidence.
- The path can shift after a short delay.
- Countries on the path can spend resources to reinforce shelters, disperse aircraft, or clear rail chokepoints.
- The storm then hits several states in order, damaging buildings and population along the route.
- The map updates where the storm has been, where it is now, and which states are next.

This is a strong candidate for animated presentation because motion communicates danger better than text.

### Meteor shower

Meteor showers should not be a clone of an asteroid impact event. They are multiple smaller or medium impacts across a region or several separated states.

- A weak shower creates crater fields, fire starts, and rail damage.
- A severe shower can hit several states and generate refugee pressure.
- A maximum manual barrage shower can hit many states in a short sequence.
- Meteor airbursts can damage airbases, infrastructure, and population without creating radioactive fallout.
- The event must not create condemnation, because the disaster is not caused by a country.

### Massive volcanic eruption

Massive volcanic eruption variants should choose from volcanic region groups if those are implemented. The effect should be strong near the volcano and broader through ashfall.

- Anchor state receives building damage, population loss, infrastructure damage, and ashfall.
- Neighboring states receive ashfall, airfield closures, supply penalties, and possible wet mass movement or lahar follow-up.
- Farther regions can receive temporary air route or supply disruption if the eruption is extreme.
- The system should not create a terminal volcanic winter.

## World-end scenario rule

Event 13 has no world-end scenario. It can become severe and global in presentation, but it should not set the shared `world_end` flag, should not stop all random events, and should not own a terminal scenario.

If the Chaos Meter passes the world-end threshold during or after a disaster season, the shared world-end selection system can choose another scenario according to its own rules. Event 13 should only feed chaos and deaths into that wider system.

## Cluster behavior

The Natural Disasters cluster is unusual because Event 13 can appear multiple times as separate member slots. This cluster should model a disaster season rather than a one-off bundle.

### Cluster membership structure

The cluster should contain multiple conceptual Event 13 entries.

| Cluster member slot | Chaos direction | Severity display | Behavior |
| --- | --- | --- | --- |
| Baseline local slot A | Calm and above | Low | One ordinary local sequence. |
| Baseline local slot B | Calm and above | Low | Optional second local sequence. |
| Baseline local slot C | Gathering Storm and above | Low | Optional third local sequence. |
| Evolution I slot | Gathering Storm and above | Medium | Expanded family sequence. |
| Evolution II slot | Rising Chaos or Chaos Tier and above | High | Regional disaster system sequence. |
| Evolution III slot | Totalen Chaos or World Collapse | Severe | Abnormal disaster sequence. |

The exact number of cluster rows can be tuned, but the cluster should show that higher chaos unlocks stronger member entries. A cluster firing can queue several Event 13 sequences. Each sequence should log as one Event 13 history row if it truly fires. The cluster history row can summarize the season and member outcomes.

### Cluster roll chance

The base roll chance for the Natural Disasters cluster should be high compared with narrow clusters, because the event is repeatable and low-severity at baseline. Higher chaos should increase both cluster chance and the chance that more Event 13 member slots participate.

### What not to include

Do not add Heat Wave, Sandstorm, Earth Earthquake, Asteroid, Massive Flood, or other separate disaster-like event IDs as cluster members yet. Those events can become placeholders or remain separate by design, but the current cluster should list Event 13 only until the user decides to merge other IDs.

## Manual triggerable scenario

Working scenario label, not final localisation: `Disaster Barrage`.

The scenario is a sandbox and challenge setup. It should launch directly from the scenario UI without requiring chaos tier, prior evolutions, prior Event 13 history, or the event being randomly selected.

### Scenario type options

| Type | Behavior |
| --- | --- |
| Random Barrage | Uses the full allowed catalogue for the selected intensity. |
| Geological Crisis | Prioritizes earthquakes, volcanoes, mass movements, tsunamis, and abnormal quake-wave variants at high intensity. |
| Weather Crisis | Prioritizes floods, storms, cyclones, hail, wind, heat, cold, blizzards, and drought. |
| Skyfall Crisis | Prioritizes meteor shower, airburst, plasma storm, and skyfire variants, only meaningful at high and maximum intensity. |
| Full Catalogue | Runs a broad disaster season with many families and minimal repetition controls. Maximum should fire nearly everything in a short period. |

### Intensity stops

| Intensity | Incident count direction | Abnormal access | Delay direction |
| --- | --- | --- | --- |
| Low | 3 to 5 local incidents. | No abnormal variants. | 3 to 6 days between incidents. |
| Medium | 6 to 9 local or regional incidents. | No abnormal variants unless type is Skyfall and user confirms high-chaos behavior is desired. | 2 to 5 days. |
| High | 10 to 14 incidents. | One abnormal variant can appear. | 1 to 4 days. |
| Maximum | 16 to 24 incidents and near full catalogue sweep. | Meteor showers, massive volcanoes, massive quake-wave, tsunami chains, and moving storm corridor can all appear. | 1 to 3 days, with strict news throttle. |

Maximum intensity should feel like a disaster week, but it still must not start a world-end scenario.

## Event interactions

### Heat Wave

Extreme heat waves in Event 13 should not stack with the separate Heat Wave event. If a state or country is under the global Heat Wave event, Event 13 should either choose a different family or turn the heat incident into drought, wildfire risk, or heatwave aftermath without double-applying the same local heat modifier.

### Sandstorm

The separate Sandstorm event becomes a placeholder. Event 13 owns active sandstorm gameplay.

### Earth Earthquake and Event 46

Event 46 should become an inactive unknown placeholder. It should not have separate seismic gameplay. Event 13 owns earthquakes, massive quake-wave variants, aftershocks, and delayed tsunamis.

### Asteroid and BOOM

Event 13 meteor showers must stay distinct from the Asteroid Incoming and BOOM events. Meteor showers are natural high-chaos hazard sequences with multiple smaller impacts. Asteroid and BOOM can remain separate if their designs require a single named object or mysterious explosion.

### Deaths system

All population loss from Event 13 feeds civilian deaths. Every immediate and follow-up death calculation must be percentage-based per affected state. Follow-up deaths from famine, exposure, refugee camps, ashfall, or damaged water systems should also feed civilian deaths by applying dynamic loss rates to the current affected-state population.

### Air cleanliness

Event 13 should avoid using the global air cleanliness contamination system unless a later implementation has a clear natural-air-quality bridge. Ashfall, smoke, dust, and meteor dust can use local state modifiers without counting as chemical, biological, nuclear, or thermonuclear contamination.

### Condemnation

Natural disasters should not add condemnation. If a country exploits a disaster through repression, forced displacement, or weapon use, that belongs to the other relevant system, not the disaster impact itself.

## AI strategy matrix

| Actor | Default behavior | High chaos behavior | Avoid |
| --- | --- | --- | --- |
| Affected player country | Receives clear warnings, decisions, and missions. | Receives corridor map, regional ledger, and stronger recovery tools. | Hidden unavoidable losses without response windows. |
| Affected AI major | Prioritizes capital, ports, rails, supply hubs, and high-population states. | Uses more expensive recovery and foreign relief if stability permits. | Spending all stockpiles on low-value rural damage. |
| Affected AI minor | Uses cheaper rescue and shelter options, asks for aid earlier. | Accepts dependency risk if disaster threatens survival. | Expensive decisions that bankrupt the country. |
| Neighboring ally | Sends relief if route access, convoys, trains, or relations allow. | Accepts refugees when stable and not under severe war pressure. | Sending aid to enemies without designed diplomatic reason. |
| Neighboring rival | May harden borders, prepare for instability, or exploit supply weakness through limited readiness. | More willing to exploit if high chaos and at war already. | Free war goals or disaster farming. |
| Faction leader | Coordinates relief for member states and key ports. | Can open a faction relief mission if several members are hit. | Repeated free factories or free equipment. |
| Isolationist or low-stability AI | Avoids costly foreign relief. | Hardens borders and focuses on internal recovery. | Overcommitting to refugees when internal collapse is likely. |

AI should read dynamic costs and not take decisions that are invalid because the country lacks trains, convoys, fuel, equipment, state access, or route access.

## Balance direction

Event 13 should be dangerous because it damages real map assets and population, not because every firing is huge. The baseline impact should be survivable. Evolution II should create serious regional recovery work. Evolution III should be rare and memorable.

Recommended balance direction.

- Baseline local disasters should often remove or damage a few buildings, reduce local population through low family-specific loss rates, and apply temporary modifiers.
- Severe baseline families like earthquakes or cyclones can produce more damage and higher population-derived deaths, especially in high-value and high-population states.
- Evolution I increases variety and incident count more than raw strength.
- Evolution II adds regional spread, supply penalties, follow-up risk, and multi-state population-derived deaths.
- Evolution III raises raw strength, affected-state count, and dynamic death-rate ceilings, but still uses warning, recovery, and news throttles.
- Recovery should be cheaper than rebuilding from total ruin, but not free.
- Preparedness should matter, but it should not make disasters irrelevant.
- Repeated hits on a neglected aftermath should be punishing.

## Implementation acceptance criteria

The rework is complete only when all listed surfaces are aligned.

| Surface | Acceptance criteria |
| --- | --- |
| Event script | Event 13 fires as Minor Repeatable, schedules delayed subevents, and writes one random event history row per Event 13 sequence. |
| Family catalogue | Baseline, Evolution I, Evolution II, and Evolution III families exist with target logic and skip behavior. |
| Effects | Disasters damage buildings, reduce real state population, feed civilian deaths, apply state modifiers, and schedule aftermaths. |
| Recovery | Decision category, relevant decisions, timed missions, AI decisions, costs, successes, failures, and cleanup exist. |
| Evolutions | Evolution logs, active-event evolution behavior, pre-fire evolved openings, and event detail previews are wired. |
| Cluster | Natural Disasters cluster can queue multiple Event 13 member slots, with severity and chaos gating. |
| Manual scenario | Disaster Barrage scenario launches directly, reads type and intensity controls, and bypasses normal prerequisites only during setup. |
| GUI | Disaster map or category presentation shows active warnings, impacts, aftermaths, and abnormal corridors when relevant. |
| Assets | Decision icons, category icon, idea icons, report or news images, GUI assets, animated assets, and static fallbacks are produced or explicitly blocked. |
| Super-event | First great rupture wave, first massive eruption, and first meteor cluster can each fire a non-terminal super-event with research-gated text, generated radio art, and licensed or public domain audio. |
| Docs | Event doc, event details, cluster details, scenario details, and spreadsheet rows match the implemented in-game wording. |
| Validation | Completion audit verifies no log spam, no world-end branch, no placeholder active disaster events, no missing localisation, no missing assets, and no recovery exploit loops. |

## Non-goals

Event 13 should not create new countries, focus trees, formables, faction systems, or a world-end scenario. It can affect countries, decisions, recovery, refugees, and regional stability, but it is not a country package event.

It should not become an excuse to merge every disaster-adjacent event immediately. Heat Wave, Asteroid, BOOM, and Massive Flood can remain separate until the user decides otherwise. Sandstorm and Earth Earthquake are the clear integration targets named by this specification.
