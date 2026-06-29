# Event 013 Natural Disasters individual disaster playbooks

All labels in this file are working labels and are not final localisation. This file replaces shallow catalogue lists with disaster family playbooks. The implementation agent should treat each playbook as a mechanic slice with its own target logic, effects, aftermaths, recovery category, AI behaviour, asset needs, and validation checks.

## Global rules for every playbook

Each affected state calculates deaths separately from the current state population. The implementation must never pick a fixed casualty number for a state. The shape is:

```text
state_current_population times final_dynamic_loss_rate = civilian_deaths_for_that_state
```

The final dynamic loss rate is built from disaster family, severity, evolution, warning success, preparedness, local supply, infrastructure, state density, war state, terrain, building concentration, and unresolved aftermath. Dense states produce much higher absolute deaths than sparse states under the same rate. Great disasters can produce millions of deaths when they hit dense states, several neighboring dense states, or a dense region followed by famine, exposure, ashfall, floodwater disease, or refugee collapse.

Every large disaster that directly hits a country opens a disaster specific decision category for that country. The generic Natural Disaster Recovery office is only the overview and small local incident surface. Big disasters must not all share one generic recovery list.

## Category scale tiers

| Tier | Meaning | Decision category rule |
| --- | --- | --- |
| Local | One state or small area with limited damage. | Use generic overview or a compact family mini category if the country is the player. |
| Serious | One important state, capital area, port, or industrial district. | Open the family specific category. |
| Regional | Several neighboring states or a multi country belt. | Open the family specific category for every directly hit country and give the regional overview to the sequence owner. |
| Catastrophic | Dense state chain, capital region, massive evolution, or manual high intensity barrage. | Open the family specific category, use emergency missions, enable international relief, and consider meaningful news. |
| Abnormal | Evolution III disaster physics or high chaos path. | Use family specific category plus Disaster Operations Map state tracking. |

## Flood

### Role

Floods are the baseline hydrological disaster. They should be common enough to teach the system, but dangerous when they hit river valleys, deltas, dense plains, or cities with weak infrastructure.

### Target logic

Valid states include river states, lowlands, coastal plains, wetlands, dam areas, dense agricultural basins, and states already affected by heavy rain, tropical cyclone, wet mass movement, or damaged infrastructure. Weight rises when neighboring states recently flooded, when rail and infrastructure are weak, when the country is at war, when stability is low, or when another disaster damaged pumps, levees, bridges, or ports.

### Sequence shape

Baseline floods can be one to three impacts across five to ten days. Evolution I can chain river states with delayed reports. Evolution II can create a flood basin with neighboring state damage and displaced population. Evolution III can create abnormal river reversals, dam cascade, or continental flood corridors, but it still is not a world end branch.

### Immediate effects

Floods damage infrastructure, rail, supply hubs, civilian factories, dockyards if coastal, ports, and local resources. Military factories can be damaged when the state is highly industrialized or the flood is catastrophic. Supply penalties should be strong because flooded rail and roads are the main gameplay pain.

### Death model

Flood loss rates should rise sharply in dense lowland states, river cities, deltas, states with poor infrastructure, active war zones, and states without warning. Deaths can continue through contaminated water, shelter failure, famine, or disease pressure. The first impact can kill fewer people than the aftermath if relief fails.

### Unique aftermaths

Floodwater contamination, blocked rail belt, dike breach fear, submerged depots, damaged housing, lost harvest, trapped refugees, and disease risk.

### Warning and response

Warnings use river advisory, dam strain reports, rainfall watch, and upstream flood reports. Successful warning reduces immediate population loss and saves rail or industry, but can raise refugee pressure because people move.

### Country hit category

Working category label: Flood Relief Authority.

Visible values: floodwater depth pressure, blocked rail states, displaced population, water safety, dike stability, relief corridor access.

Key decisions: reinforce levees, release emergency reservoirs, evacuate lowlands, deploy pumps, send rail engineers, open field kitchens, chlorinate wells, request convoy or train relief, rebuild bridges.

Key missions: hold and repair the river rail belt, reopen the flooded port, keep relief trains supplied, prevent dike breach in named states, shelter the displaced before winter or famine.

Failure outcomes: famine pressure, refugee spread to neighboring states, second rail collapse, disease deaths, local stability loss, reduced recruitable population through real population loss.

AI behaviour: majors prioritize rail belts, capitals, ports, and military industry. Minors prioritize population and supply. AI at war should protect supply first unless the capital state is hit.

Asset direction: report image with flooded rail or city street, decision category icon with broken levee and rescue boat, state modifier icon for floodwater contamination.

## Tropical cyclone

### Role

Tropical cyclones are the major coastal storm family. They should feel different from generic storms because they combine wind, storm surge, inland flood, port damage, airbase disruption, and coastal evacuation.

### Target logic

Valid states include warm coastal states, islands, ports, dockyard regions, Caribbean, Pacific island chains, Bay of Bengal, South China Sea, Japanese and Philippine coasts, Gulf and Atlantic coasts, Indian Ocean coasts, and any modded warm coastline. Weight rises for islands, capitals on coasts, high dockyard concentration, and prior warm ocean season variables.

### Sequence shape

A cyclone should have a forecast track when possible. Baseline uses one landfall and one inland flood report. Evolution I can add secondary landfall and storm surge. Evolution II can cross several neighboring states. Evolution III can become a moving storm corridor with animated map tracking, forecast state, and next hit state.

### Immediate effects

Damage ports, naval bases, dockyards, airbases, infrastructure, civilian factories, anti air, radar, and coastal forts. Apply supply collapse in landfall and inland flood states. Add strong temporary naval and air operation disruption in affected coastal areas.

### Death model

Cyclone deaths come from storm surge, building collapse, inland flood, and failed evacuation. Dense coastal states and deltas can suffer very high absolute losses. Prepared evacuation can cut the loss rate heavily, but failure in dense coastal states can push deaths into the hundreds of thousands or millions in catastrophic scenarios.

### Unique aftermaths

Storm surge debris, port closure, saltwater contamination, displaced coastal population, dead livestock, inland flood corridor, downed radio networks, isolated islands.

### Country hit category

Working category label: Cyclone Emergency Command.

Visible values: forecast confidence, landfall window, surge risk, port closure, evacuation capacity, inland flood risk.

Key decisions: order coastal evacuation, close ports, disperse air wings, anchor or sortie fleet, stage relief convoys, reinforce sea walls, deploy radio repair teams, reopen dockyards, clear storm surge debris.

Key missions: keep the main port connected, evacuate island states before landfall, reopen naval base, prevent inland flood from cutting the supply route, shelter coastal refugees.

Failure outcomes: port wreckage lasts longer, convoy disruption, dockyard shutdown, refugee pressure, famine on islands, higher death logs.

AI behaviour: naval powers protect dockyards and ports. Island countries evacuate first. Countries at war may risk fleets if enemy naval threat is high, but the AI should avoid trapping fleets in a closing port when the storm has high forecast confidence.

Asset direction: black and white news image of coastal wreckage, cyclone track UI marker, port closure icon, animated storm spiral for Evolution III.

## Ordinary storm and thunderstorm outbreak

### Role

Ordinary storms and thunderstorm outbreaks are medium incidents that can branch into hail, extreme wind, flood, tornado, or wildfire ignition. They keep the baseline varied without making every sequence catastrophic.

### Target logic

Valid states include plains, urban regions, warm humid states, coasts, river basins, and airbase heavy states. Thunderstorm outbreaks should prefer regions where several neighboring states can share a storm line.

### Sequence shape

Baseline storm hits one state, then may create a delayed debris or flood report. Evolution I lets the storm split into hail, wind, lightning fire, or local flood. Evolution II can create a storm line across several states. Evolution III converts to the moving storm corridor playbook instead of staying ordinary.

### Immediate effects

Damage infrastructure, airbases, radar, anti air, civilian industry, and local supply. Hail branches damage airbases and agricultural output more than population. Lightning branches raise wildfire risk.

### Death model

Ordinary storm deaths should be low to medium rates. Deaths rise in dense urban states, weak infrastructure, active combat, and failed shelter actions. Hail has very low direct loss rates, but can worsen famine through crop damage.

### Unique aftermaths

Debris fields, downed power and radio lines, damaged airfields, flash flood pocket, crop damage, storm shelter pressure.

### Country hit category

Working category label: Severe Storm Office.

Visible values: storm line severity, airfield damage, debris clearance, flash flood risk, crop damage.

Key decisions: open storm shelters, ground aircraft, clear debris, repair radar and anti air, protect harvest stores, dispatch emergency medical trains.

Key missions: clear the airbase belt, hold supply through storm line states, prevent flash flood follow up, repair radio stations.

Failure outcomes: local supply penalty, crop loss, storm spawned flood or wildfire, lower air mission efficiency.

AI behaviour: AI uses cheap shelter and airfield repair. It should not overspend if the storm is local and no key state is hit.

Asset direction: storm damaged airbase report image, decision icon with lightning over a rail yard, hail crop damage state icon.

## Hailstorm

### Role

Hailstorms are small to medium disasters that mainly attack agriculture, aircraft, windows, radar, and fragile infrastructure. They should not become a mass death tool unless chained into famine after repeated disasters.

### Target logic

Valid states include agricultural plains, airbase heavy states, warm storm regions, and storm outbreak child states. Weight rises in spring or summer if seasonal logic exists, after thunderstorm warnings, and in states with high airbase level.

### Sequence shape

Usually one impact, sometimes followed by crop loss or airfield repair report. Evolution I can pair hail with thunderstorm outbreak. Evolution II can create regional crop damage across neighboring states.

### Immediate effects

Damage airbases, radar, anti air, infrastructure lightly, and resources or crop abstractions. Low direct factory damage unless the state has high civilian industry and high severity.

### Death model

Direct death rate is very low. Delayed deaths can occur through famine if hail destroys crops in a region already under drought, war, blockade, or refugee pressure. No fixed famine death count is allowed.

### Unique aftermaths

Damaged harvest stores, shattered airfield surface, repair glass shortage, aircraft dispersal, livestock losses.

### Country hit category

Working category label: Hail Damage Board.

Visible values: crop damage, airfield damage, replacement material need, famine linkage risk.

Key decisions: repair airfield surfaces, protect harvest stores, release seed reserves, salvage damaged aircraft, import glass and roofing.

Key missions: recover agricultural output before drought season, keep key airbase operational, prevent crop shock from becoming famine.

Failure outcomes: local supply and stability loss, delayed famine pressure if drought or blockade is active.

AI behaviour: only serious hail opens the category for AI. AI should fix airbases if at war or if the state hosts important aircraft.

Asset direction: decision icon with cracked crop and hailstones, small airfield damage marker.

## Extreme wind event

### Role

Extreme wind covers derechos, downbursts, straight line winds, and violent non tropical storm damage. It is the bridge between storms and the abnormal moving tornado corridor.

### Target logic

Valid states include plains, airbase heavy states, infrastructure corridors, urban belts, coasts, and thunderstorm outbreak child states. Weight rises with severe storm lines and high chaos.

### Sequence shape

Baseline one impact plus debris report. Evolution I can hit several connected states. Evolution II can create a regional wind swath. Evolution III transforms into Storm Corridor or Tornado Corridor.

### Immediate effects

Damage airbases, infrastructure, anti air, radar, civilian factories, and rail. Apply movement and supply penalties. Damage forts only in severe or abnormal variants.

### Death model

Loss rates are medium in dense urban states and low in sparse states. Deaths rise when warnings fail, shelters are absent, or the wind swath crosses several high population states.

### Unique aftermaths

Downed rail signals, ruined airstrips, wind debris, collapsed factories, blocked roads, local panic.

### Country hit category

Working category label: Wind Damage Control.

Visible values: wind swath damage, airfield closure, rail signal failure, shelter capacity.

Key decisions: ground aircraft, clear roads, reinforce shelters, repair rail signals, requisition trucks, deploy medical columns.

Key missions: restore the airbase network, reopen the wind cut supply line, clear industrial debris.

Failure outcomes: air mission penalties, additional infrastructure damage, higher refugee pressure from damaged housing.

AI behaviour: air powers fix airbases first. Land powers fix supply and rail first.

Asset direction: wind damaged hangar, broken telegraph or rail signal icon.

## Tornado corridor and moving storm corridor

### Role

This is the Evolution III abnormal storm system. It should be large, unique, visually tracked, and much more dangerous than an ordinary wind event. It represents a moving path of destructive vortices or storm cells that can cross countries over days.

### Target logic

Starts in storm prone plains or warm storm belts, but high chaos can let it ignore normal climate bounds. It needs a current corridor state, forecast next states, path memory, and possible branch points. It should prefer connected land states and avoid oceans except as a cyclone or waterspout transition.

### Sequence shape

The corridor moves every one to three days. It can damage a current state, mark one or more forecast states, then roll path change after player and AI response. The scripted GUI map should show current position, next possible states, danger level, and whether observation or intervention changed the path.

### Immediate effects

Heavy infrastructure, military factory, civilian factory, airbase, radar, anti air, supply hub, and rail damage along the path. It can destroy small amounts of many building types instead of only one type. The strongest variants can repeatedly damage the same region if the path loops.

### Death model

The corridor can produce very high deaths if it crosses dense states. The loss rate is applied per state on each hit. A dense industrial belt hit by several corridor impacts can reach million scale deaths without a fixed casualty number.

### Unique aftermaths

Moving debris wall, shattered rail junctions, destroyed shelters, displaced storm belt, emergency forecast panic, repeated hit trauma.

### Country hit category

Working category label: Storm Corridor Command.

Visible values: current corridor state, forecast states, path confidence, shelter readiness, rail vulnerability, observation coverage.

Key decisions: activate storm observation net, evacuate forecast corridor, reinforce rail junctions, ground aircraft in projected path, deploy mobile hospitals, attempt corridor disruption with high cost, reroute supply trains.

Key missions: protect a named forecast belt, keep capital connected while corridor passes, reopen shattered junction, shelter displaced people before the next movement tick.

Failure outcomes: next state hit with higher rate, aftershock style repeat impact, emergency stability loss, news threshold rise, refugee spillover.

AI behaviour: AI should act only on forecast states it owns or controls. It should prioritize capital, supply hub, high industry, and port states. It should avoid spending on states already lost to enemies unless it still controls the corridor path.

Asset direction: animated storm path marker, forecast arrow sprites, warning pulse border, disaster map panel state cards.

## Earthquake

### Role

Earthquakes are the core seismic disaster. They should be sudden, destructive, and varied by terrain, urban concentration, building density, and preparedness. They are no longer a separate Earth Earthquake event.

### Target logic

Valid states include mountainous regions, urban high building states, fault heuristic regions, volcanic regions, coastal subduction regions, and states already strained by mining, dams, or previous quakes. A hidden fault group list should be preferred over pure random selection where practical.

### Sequence shape

Baseline quake is sudden impact plus aftershock inspection. Evolution I can include a neighboring aftershock or landslide. Evolution II can damage several neighboring states with aftershocks, refugee pressure, and infrastructure collapse. Evolution III can become Great Rupture Wave with delayed tsunamis, moving seismic wave reports, and special map presentation.

### Immediate effects

Heavy damage to infrastructure, civilian factories, military factories, rail, supply hubs, forts, anti air, radar, and state buildings. Coastal states can mark tsunami risk. Mountain states can mark landslide risk.

### Death model

Earthquake death rate depends on population, urban concentration, building density, terrain collapse, night or surprise flag if modeled, preparedness, and aftershock response. Dense Chinese, Japanese, Indian, Anatolian, Iranian, Italian, Balkan, Californian, Andean, or Javanese states can produce extremely high absolute deaths if the rate is high. Evolution III massive rupture can create million scale totals when several dense states are hit.

### Unique aftermaths

Aftershock pressure, bridge collapse, collapsed hospitals, damaged water, rail tunnel collapse, landslide trigger, tsunami warning, uninspected masonry, emergency burial strain.

### Country hit category

Working category label: Seismic Emergency Authority.

Visible values: aftershock risk, bridge integrity, hospital damage, rubble rescue progress, tsunami risk if coastal, landslide risk if mountainous.

Key decisions: shut down damaged bridges, deploy rescue engineers, open field hospitals, inspect aftershocks, evacuate coastal districts, secure rail tunnels, requisition heavy equipment, invite foreign seismologists.

Key missions: clear the capital rubble, keep the rail tunnel open, inspect aftershocks before the next tremor, evacuate coast before tsunami, rebuild hospital capacity.

Failure outcomes: aftershock damage, landslide, delayed tsunami, additional percentage based deaths, stability shock, war support loss if the state is a capital or front line.

AI behaviour: AI must prioritize capital and supply hubs. It should take coastal tsunami precautions when forecast confidence exists. It should not ignore aftershock inspection in dense states.

Asset direction: earthquake report image with collapsed rail or city block, state modifier icons for aftershock risk and bridge collapse, seismic pulse map animation for Evolution III.

## Great rupture wave

### Role

Great Rupture Wave is the Evolution III earthquake branch that replaces the old Earth Earthquake idea. It is a unique abnormal seismic sequence, not a generic stronger earthquake. It can roll across a fault belt with several delayed impacts and then spawn tsunamis or mass movements.

### Target logic

Needs a rupture anchor and a chain of neighboring or related states. It should prefer known seismic belts, coastal subduction style states, mountain belts, and high chaos regions. It should use state groups and adjacency where possible.

### Sequence shape

Impact one hits the anchor. One to three days later, aftershocks or rupture jumps hit neighboring states. A coastal anchor can create delayed tsunami warnings. Mountain states can create wet or dry mass movement. The Disaster Operations Map should show rupture origin, current stress front, next possible impact, and tsunami watch states.

### Immediate effects

Very heavy infrastructure, rail, supply, factory, fort, port, and airbase damage across multiple states. Apply local recovery lockouts until rubble missions begin. Heavy state modifier durations should vary by severity and preparedness.

### Death model

This is one of the branches that must support million scale deaths. Each state uses dynamic percentage loss. Dense states hit by the rupture and then by aftershock, tsunami, or landslide can generate layered deaths through separate per state calculations. Do not collapse the sequence into one fixed total.

### Unique aftermaths

Regional aftershock grid, tsunami wave train, collapsed pass, trapped rail belt, ruined hospitals, refugee corridor, state capital loss.

### Country hit category

Working category label: Great Rupture Command.

Visible values: stress front, aftershock count, tsunami watch, rescue capacity, rail tunnel survival, regional death pressure.

Key decisions: create seismic exclusion zones, commit national engineer corps, choose capital rescue priority, open international rescue corridor, evacuate the tsunami watch coast, stabilize dams, mobilize field hospitals.

Key missions: hold relief supply through a destroyed rail belt, clear three priority cities, evacuate coast before delayed wave, prevent dam failure, restore a capital supply hub.

Failure outcomes: second wave damage, dam failure flood, tsunami impact, regional famine and refugee chain, major news threshold.

AI behaviour: AI treats this as national emergency. It should spend major resources even during war if capital, port, or large population states are hit.

Asset direction: animated seismic wave on map, cracked ground category icon, report image with rail tunnel collapse.

## Tsunami

### Role

Tsunamis are coastal follow up disasters most often caused by earthquakes, volcanic eruptions, or underwater landslides. They should be rare, severe, and heavily dependent on warning and evacuation.

### Target logic

Valid states are coastal states connected to the trigger basin or coastal states selected by an abnormal high chaos wave. Islands and dense ports have higher severity. Tsunami should not hit landlocked states.

### Sequence shape

A tsunami should usually be delayed after its cause. The delay gives player and AI a window for evacuation. Evolution II can hit several coastal neighboring states. Evolution III can create a wave train that crosses seas and hits multiple countries with news throttle.

### Immediate effects

Heavy port, naval base, dockyard, coastal fort, infrastructure, civilian factory, and population damage. Apply temporary coastal supply and convoy disruption.

### Death model

Tsunami deaths depend strongly on coastal population, warning time, evacuation capacity, port density, island isolation, and prior quake or cyclone damage. Dense ports and deltas can produce massive deaths. A delayed wave that hits several dense states can cross million scale totals.

### Unique aftermaths

Saltwater intrusion, shattered harbor, missing fishing fleet, floating debris, contaminated wells, island isolation, coastal refugee belt.

### Country hit category

Working category label: Tsunami Coastal Command.

Visible values: wave arrival estimate, evacuation trains, port damage, island isolation, contaminated wells, harbor clearance.

Key decisions: order coastal evacuation, commandeer trains, move fleet out of harbor, close port, prepare shelters on high ground, send coastal engineers, clear harbor wreckage, rebuild fishing fleet.

Key missions: evacuate the forecast coast before wave arrival, restore the main port, reconnect isolated islands, clear contaminated wells, keep relief convoys moving.

Failure outcomes: high population loss rate, port closure, famine on islands, refugee spillover, secondary disease pressure.

AI behaviour: if warning exists, evacuate first. If no warning, rescue and port reopening follow. Naval AI should sortie or shelter fleet based on enemy threat and forecast confidence.

Asset direction: tsunami report image with ruined harbor, wave arrival map marker, coastal command icon.

## Volcanic eruption

### Role

Volcanoes are rare geophysical disasters that can be local, regional, or abnormal. They combine direct eruption damage, ashfall, lahars, air disruption, agriculture loss, and possible tsunami.

### Target logic

Prefer a curated volcanic state list. If the implementation lacks a full list, use mountain island arcs, volcanic islands, known volcanic regions, and high chaos abnormal anchors. Do not let every mountain state count as volcanic unless Evolution III abnormal logic justifies it.

### Sequence shape

Baseline is a local eruption or ashfall incident. Evolution I adds neighboring ashfall or lahar. Evolution II creates regional ash cloud, airbase disruption, crop stress, and refugee pressure. Evolution III can create Massive Volcano or Volcanic Ring Awakening with several eruption spots and animated map state.

### Immediate effects

Damage infrastructure, airbases, civilian factories, resources, supply hubs, and rail. Nearby ports can close from ash and pumice. Severe eruptions can destroy buildings directly and create impassable state modifiers.

### Death model

Deaths come from eruption proximity, pyroclastic flows if modeled abstractly, lahars, ash roof collapse, respiratory stress, water contamination, and famine from crop damage. Dense volcanic regions and islands can produce high deaths. Massive eruptions can produce global or multi regional indirect percentage deaths through ash winter and famine pressure, but Event 13 still has no world end branch.

### Unique aftermaths

Ashfall, lahar path, roof collapse risk, grounded aircraft, poisoned water, crop ash, island evacuation, volcanic refugee pressure.

### Country hit category

Working category label: Volcanic Crisis Office.

Visible values: eruption stage, ash cloud spread, lahar risk, airfield closure, water safety, evacuation route.

Key decisions: evacuate volcano slopes, ground aircraft, clear ash from roofs, protect water sources, build lahar barriers, evacuate island ports, request foreign volcanologists, create ash disposal crews.

Key missions: keep ash from collapsing industry roofs, reopen airfields, protect river valleys from lahars, evacuate island settlements, feed the ash covered crop belt.

Failure outcomes: lahar follow up, airbase closure, famine pressure, ash deaths, port isolation, stronger refugee flows.

AI behaviour: AI should ground aircraft and clear ash when airbases matter. Island AI prioritizes evacuation and port reopening.

Asset direction: volcanic eruption report image, ashfall state icon, lahar warning icon, animated eruption marker.

## Massive volcano and volcanic ring awakening

### Role

This is the Evolution III volcano branch. It should be one of the signature abnormal disasters. It is not just a volcano with higher numbers. It can select several volcanic anchors, create moving ash clouds, trigger lahars, close air regions abstractly, create harvest stress, and reshape recovery for many countries.

### Target logic

Select one main volcanic region or several high chaos eruption spots. Each spot needs an affected state group, ashfall neighboring states, possible coastal tsunami if island or submarine context applies, and a country hit list.

### Sequence shape

First eruption, then ashfall in neighboring states, then lahars or roof collapse, then food and refugee aftermath. A severe version can create repeated eruption pulses over several weeks. News appears only for meaningful milestones, not every ash state.

### Immediate effects

High building damage in eruption state. Medium to high ash damage in neighboring states. Strong airbase and supply penalties. Agriculture and resource stress. Possible global or regional air traffic and weather style penalty through state modifiers, not a world end state.

### Death model

Each state gets its own percentage loss. The eruption state has the highest immediate loss. Ashfall states have lower immediate loss but can suffer delayed deaths through roof collapse, water poisoning, exposure, and famine. Million scale totals are possible when dense volcanic regions or dense ash belts are hit.

### Unique aftermaths

Ash winter pressure, lahar belts, buried towns, destroyed ports, roof collapse, respiratory hospitals, ash famine, observatory panic.

### Country hit category

Working category label: Massive Eruption Command.

Visible values: eruption pulse count, ash cloud map, lahar belts, crop pressure, airbase closure, water safety, evacuation capacity.

Key decisions: national ash clearing, evacuate eruption zone, create lahar diversions, mobilize respiratory hospitals, close ash filled airspace, reroute supply, import food, request international observatory mission.

Key missions: clear ash from capital roofs, keep a port open under ashfall, feed the ash covered region, prevent lahar in named valleys, restore airbase operations.

Failure outcomes: famine, respiratory deaths, lahar disaster, multi state refugee pressure, long air operations penalty.

AI behaviour: Treat as severe regional crisis. AI should spend large resources if it owns an eruption state or a capital in ashfall.

Asset direction: animated ash cloud and eruption markers, report image with ash covered city, category seal with volcano and crossed railway.

## Wildfire

### Role

Wildfires are climatological disasters that interact strongly with drought, heat, wind, forests, and war. They can be local at baseline and regional in evolved forms.

### Target logic

Valid states include forests, hills, dry states, drought states, heat wave aftermath states, thunderstorm lightning states, and war damaged states. Weight rises with drought, heat, low infrastructure, active bombing, and prior wind event.

### Sequence shape

Baseline wildfire hits one state and may threaten a neighbor. Evolution I can create several fire fronts. Evolution II can create regional smoke, refugee pressure, and repeated spread. Evolution III can create firestorm belts or combine with moving storm corridor.

### Immediate effects

Damage infrastructure, civilian factories, resources, airbases, and supply. Forest or resource state modifiers can be reduced. Apply movement and attrition style local penalties.

### Death model

Immediate death rate is low to medium in sparse forests, high in dense urban wildfire interface states, and very high if evacuation fails under high winds. Delayed deaths can come from smoke, shelter failure, and famine if farms burn.

### Unique aftermaths

Fire front, smoke layer, burned rail bridges, destroyed villages, evacuated settlements, crop and timber loss.

### Country hit category

Working category label: Firefront Command.

Visible values: fire spread chance, wind support, fuel and water access, evacuation progress, smoke pressure, burned infrastructure.

Key decisions: cut firebreaks, evacuate threatened towns, deploy army fire crews, requisition fuel and trucks, ground aircraft through smoke, protect ammunition depots, create controlled burns.

Key missions: contain the active fire front, protect the rail bridge, evacuate a named town belt, keep the front from reaching an industrial state, clear smoke from airfields.

Failure outcomes: fire spreads to neighbor, industry burns, smoke deaths, supply collapse, stability loss.

AI behaviour: AI should contain fires threatening high industry, capital, ports, or supply hubs. AI avoids high cost controlled burns unless severe.

Asset direction: wildfire report image, firefront state icon, animated flame edge for GUI.

## Drought

### Role

Drought is slow disaster pressure. It does less immediate building damage, but it creates water scarcity, crop failure, supply stress, migration, and famine risk.

### Target logic

Valid states include arid, agricultural, warm, low infrastructure, water stressed, recent heat wave, or wildfire affected states. Weight rises during repeated heat, low stability, blockade, war, and poor infrastructure.

### Sequence shape

Baseline drought is a local water crisis followed by a delayed crop stress report. Evolution I spreads to several agricultural states. Evolution II unlocks famine and refugee chain. Evolution III can create mega drought belts across continents.

### Immediate effects

Apply supply, stability, construction, and resource penalties. Damage infrastructure lightly through land degradation. Reduce population through heat and water stress only as a dynamic percentage.

### Death model

Drought has low immediate death rate and potentially high delayed death rate if famine, water failure, or refugee pressure is not contained. It should be one of the main ways ordinary disasters can grow into mass death without using fixed numbers.

### Unique aftermaths

Water table collapse, crop failure, livestock death, ration queues, refugee pressure, famine risk, wildfire ignition risk, sandstorm risk.

### Country hit category

Working category label: Drought and Famine Office.

Visible values: water reserve, crop survival, ration strain, famine pressure, refugee outflow, wildfire risk.

Key decisions: water rationing, dig emergency wells, import grain, protect seed reserves, requisition trucks for water, open relief corridors, prioritize cities or countryside, subsidize livestock slaughter, request foreign food aid.

Key missions: feed the drought belt, keep water convoys running, prevent famine in named agricultural states, protect seed reserves until next season, keep refugees housed.

Failure outcomes: famine deaths, refugee spread, wildfire risk, stability loss, war support loss, lower recruitable population through real population loss.

AI behaviour: AI prioritizes famine prevention when deaths are rising. It should seek foreign relief if domestic stockpiles are low and it is not blocked by war or ideology logic.

Asset direction: drought report image with dry reservoir or crop field, decision icon with cracked earth and ration card.

## Extreme heat wave

### Role

Extreme heat in Event 13 is local or regional, not the global Event 51 Heat Wave. It should interact with drought, urban density, infrastructure, and power or water systems. It must not stack with Event 51.

### Target logic

Valid states include hot, urban, dry, agricultural, desert edge, or drought states. Dense urban states and states with poor infrastructure are more dangerous. If Event 51 global Heat Wave is active for the same state, Event 13 should choose a different family or convert to drought, wildfire, water emergency, or heat aftermath without applying duplicate heat modifiers.

### Sequence shape

Baseline heat wave lasts as a short local emergency. Evolution I adds neighboring heat stress and water shortages. Evolution II can cause regional grid collapse, famine pressure, and refugee movement. Evolution III can create abnormal heat domes that move slowly and amplify wildfire or drought.

### Immediate effects

Apply supply, stability, war support, production, and local population stress. It should not destroy many buildings directly, but it can damage infrastructure through grid strain or rail buckling if severe.

### Death model

Deaths depend on population, urban density, infrastructure, warning, water access, and relief shelter success. Dense urban states can suffer very high deaths during severe heat. Delayed deaths continue while water emergency or grid collapse is unresolved.

### Unique aftermaths

Heat shelter pressure, water rationing, power grid strain, rail buckling, urban mortality, crop stress, wildfire risk.

### Country hit category

Working category label: Heat Emergency Office.

Visible values: heat stress, water reserve, shelter capacity, grid strain, wildfire risk, active Event 51 non stacking guard.

Key decisions: open cooling shelters, ration water, protect hospitals, shift factory hours, move rail traffic at night, import water, suspend desert maneuvers, activate city emergency broadcasts.

Key missions: keep the city shelters open, restore water convoys, prevent grid collapse, protect harvest under heat, stop heat deaths from continuing.

Failure outcomes: high delayed death rate, drought follow up, wildfire ignition, stability loss, production penalties.

AI behaviour: AI should open shelters in dense states and water convoys in drought states. It should not waste resources in sparse states unless key industry or supply is at risk.

Asset direction: heat shimmer category icon, report image with crowded shelter or dry city street, water reserve meter.

## Extreme cold wave and blizzard

### Role

Cold disasters target supply, fuel, rail, attrition, and exposed populations. They are especially dangerous during war, in low infrastructure regions, and where rail is already damaged.

### Target logic

Valid states include cold, northern, mountain, high altitude, winter affected, low infrastructure, or front line states. Weight rises when supply is low, fuel is low, rail is damaged, or refugees are already present.

### Sequence shape

Baseline blizzard hits one state and delays transport. Evolution I spreads to neighboring states. Evolution II creates regional freeze, stranded divisions, exposure deaths, and rail collapse. Evolution III can create abnormal cold fronts that move and combine with global darkness or sun distance events without stacking duplicate modifiers.

### Immediate effects

Damage infrastructure and rail, reduce supply, disrupt airbases, add movement penalty, increase attrition like local modifier, and damage local population through exposure.

### Death model

Deaths depend on population, shelter quality, fuel access, supply, infrastructure, and refugee pressure. Dense states with fuel shortage can suffer heavy deaths. Sparse mountain states suffer lower absolute deaths but can have severe army and supply effects.

### Unique aftermaths

Frozen rail switches, fuel shortage, stranded trains, blocked mountain passes, refugee exposure, frozen ports, hospital heating crisis.

### Country hit category

Working category label: Winter Emergency Directorate.

Visible values: fuel reserve, shelter heat, rail clearance, stranded population, mountain pass closure, frozen port.

Key decisions: allocate heating fuel, clear rail switches, reopen mountain pass, shelter refugees, suspend offensives in affected state, import coal or fuel, deploy field kitchens, thaw port equipment.

Key missions: keep the capital heated, clear the frozen rail belt, rescue stranded trains, hold supply through mountain pass, shelter refugees before the second freeze.

Failure outcomes: exposure deaths, rail damage, supply collapse, war support loss, unit attrition pressure.

AI behaviour: AI at war fixes rail first if front supply is at risk. Peaceful AI protects population and fuel.

Asset direction: blizzard report image, frozen rail icon, fuel reserve meter.

## Sandstorm and dust storm

### Role

Sandstorms belong to Event 13. Event 99 is not the source. Sandstorms should focus on visibility, supply, airfields, movement, and equipment wear. They usually have low deaths, but severe evolved dust crises can kill through exposure, transport collapse, and refugee failure.

### Target logic

Valid states include desert, arid, steppe, dust basin, dry coastal desert, drought affected, or war damaged arid states. Weight rises with drought, heat, low infrastructure, and high wind.

### Sequence shape

Baseline sandstorm disrupts one state. Evolution I can create a dust belt across neighboring arid states. Evolution II can create supply crisis and refugee pressure. Evolution III can create abnormal dust wall or moving sandstorm front with map tracking.

### Immediate effects

Damage infrastructure lightly, airbases moderately, radar and anti air lightly, supply strongly, and movement strongly. Reduce division intel or combat visibility where supported. Damage aircraft readiness and convoy or truck reliability abstractly through equipment loss if helper exists.

### Death model

Direct death rate is very low unless the state is dense, supply is cut, or refugees are exposed. Severe dust belt can cause delayed deaths through water failure, transport collapse, and famine. No fixed deaths.

### Unique aftermaths

Airfield burial, dust clogged engines, visibility collapse, water contamination, caravan or convoy loss, rail drift, desert refugee pressure.

### Country hit category

Working category label: Dust Emergency Office.

Visible values: visibility, airfield closure, water safety, convoy route, dust belt movement, engine damage.

Key decisions: ground aircraft, clear airfields, issue masks and filters, reroute convoys, close desert roads, secure wells, deploy rail plows, pause desert offensives.

Key missions: reopen the airfield, keep the desert supply route active, protect wells, clear the rail drift, shelter exposed refugees.

Failure outcomes: longer supply penalty, airbase damage, equipment loss, water crisis, refugee deaths.

AI behaviour: air powers fix airfields. Desert front countries protect supply. AI should not treat sandstorm as mass death unless severe aftermath exists.

Asset direction: dust wall report image, airfield dust icon, animated dust front marker for Evolution III.

## Wet mass movement

### Role

Wet mass movements cover landslides, mudslides, debris flows, and slope failures after heavy rain, flood, quake, or volcano. They are narrow but can destroy rail and towns.

### Target logic

Valid states include mountains, hills, high rainfall states, recently flooded states, volcanic slopes, earthquake aftermath states, and states with rail or supply hubs in mountain terrain.

### Sequence shape

Usually a follow up after rain, flood, quake, or volcano. Evolution I can hit a neighboring state. Evolution II can close passes and rail belts. Evolution III can chain with Great Rupture Wave or Massive Volcano.

### Immediate effects

Damage rail, supply hubs, infrastructure, forts, resources, and local population. Factories are damaged if the state is urban or industrial.

### Death model

Loss rates are high in affected settlements but applied to whole state population through a tuned rate. Dense mountain valley states can suffer high deaths. Sparse mountain regions have lower absolute deaths but severe supply effects.

### Unique aftermaths

Buried rail pass, dammed river, isolated valley, blocked tunnel, unstable slope, contaminated river.

### Country hit category

Working category label: Landslide Rescue Office.

Visible values: buried rail, isolated settlements, slope instability, river blockage, rescue access.

Key decisions: clear mountain pass, stabilize slope, rescue buried settlements, divert blocked river, deploy tunnel crews, reopen supply hub.

Key missions: reconnect isolated valley, clear the pass before winter, prevent river blockage flood, inspect slopes after earthquake.

Failure outcomes: flood follow up, starvation in isolated states, supply hub loss, extra deaths from trapped population.

AI behaviour: prioritize passes and supply hubs. Avoid spending heavily on isolated low value states unless population loss is high.

Asset direction: landslide report image, buried rail icon, slope instability marker.

## Dry mass movement

### Role

Dry mass movements cover rockfalls, desert slope collapse, dust landslides, and post drought or post quake slope failures. They are less water focused and more about rail, roads, mines, and passes.

### Target logic

Valid states include arid mountains, dry hills, mining regions, earthquake aftermath states, and desert infrastructure corridors.

### Sequence shape

Often a follow up to earthquake, drought, heat, or sandstorm. Evolution II can create a pass closure crisis. Evolution III can chain with rupture waves.

### Immediate effects

Damage infrastructure, rail, resources, supply hubs, and mountain forts. Lower direct population loss than wet mass movement unless dense settlement is present.

### Death model

Low to medium loss rate, higher in mining towns, dense valleys, and rail refugee corridors. Delayed deaths if the pass closure cuts food or fuel.

### Unique aftermaths

Rockfall corridor, crushed mine galleries, desert road burial, pass closure, rail tunnel instability.

### Country hit category

Working category label: Slope Collapse Response.

Visible values: pass closure, mine collapse, rail tunnel risk, isolated population, repair equipment.

Key decisions: reopen desert road, rescue miners, stabilize tunnel, clear pass, reroute supply, inspect quake damaged slopes.

Key missions: reopen the pass before supply fails, rescue trapped mine workers, keep the desert rail open.

Failure outcomes: resource penalty, supply collapse, delayed population deaths, further rockfall.

AI behaviour: mining states and supply corridors get priority.

Asset direction: rockfall icon, mine collapse report image.

## Meteor shower and skyfall field

### Role

Meteor showers are Evolution III and manual scenario material. They are not Event 28 Asteroid Incoming. They represent multiple impacts, airbursts, shock waves, fires, crater fields, and atmospheric panic across separated or clustered states.

### Target logic

Meteor showers can hit almost anywhere, but baseline access is only rare by manual scenario or high chaos. Target selection should mix clustered impact fields and separated airburst states. Dense urban states, airbases, rail hubs, and capitals create higher news weight.

### Sequence shape

A meteor shower should have multiple delayed impacts over one to three days at high intensity or several days at moderate intensity. It may include skywatch warning, first airburst, crater impact, fire follow up, dust and ash like airfield disruption, and refugee aftermath. It should never become the Asteroid Incoming prediction event.

### Immediate effects

Damage infrastructure, civilian factories, military factories, airbases, radar, anti air, forts, and local supply. Apply crater field modifiers and possible wildfire ignition. Strong airburst variants damage buildings and population without radioactive fallout. Possibly sets the state category to wasteland.

### Death model

Meteor loss rate can be medium to severe in impact states and lower in airburst shock states. Dense states can produce million scale deaths if severe impacts hit city regions. Several dense states hit by a shower can produce very large totals. No absolute caps.

### Unique aftermaths

Crater fields, glass storm, airburst shock, fire ignition, rail crater, sky panic, meteor dust, observatory credibility crisis.

### Country hit category

Working category label: Skyfall Emergency Bureau.

Visible values: impact count, skywatch confidence, crater fields, fire risk, dust in airfields, shelter capacity, observatory reports.

Key decisions: activate skywatch network, open impact shelters, evacuate predicted impact area, clear cratered rail, contain fires, ground aircraft through meteor dust, investigate fragments, secure observatories.

Key missions: keep capital shelters open, clear cratered rail line, prevent fire spread after airburst, recover observatory instruments, shelter displaced survivors.

Failure outcomes: high deaths, fire chain, crater field duration extension, airbase closure, public panic, refugee pressure.

AI behaviour: AI treats dense predicted impact states as top priority. It should not spend heavily on skywatch if the shower has already ended and only cleanup remains.

Asset direction: meteor report image, animated meteor track, crater field state icon, skywatch map marker.

## Meteor storm barrage

### Role

Meteor Storm Barrage is the maximum manual Disaster Barrage or late Evolution III variant. It is the spectacle disaster branch that can damage several continents without becoming a terminal world end scenario.

### Target logic

Select a main hemisphere or several clusters. Avoid hitting every state. Use meaningful high value states, dense states, and rail or industrial corridors while respecting news throttle.

### Sequence shape

Several airbursts and crater impacts over one to three days. Follow with fires, crater cleanup, refugee pressure, and observatory or scientific aftermath. Only a few meaningful news reports should appear.

### Immediate effects

Severe infrastructure, factory, rail, airbase, radar, and supply damage in hit states. Some states receive crater field modifiers. Neighboring states can receive refugee pressure and sky panic without direct building damage.

### Death model

This branch must allow multi million deaths when dense state clusters are hit. Death rates still apply state by state. No fixed totals and no absolute death cap.

### Country hit category

Working category label: Meteor Storm Command.

Visible values: impact clusters, crater severity, active fires, survivor shelter, rail craters, scientific salvage.

Key decisions: national shelter order, triage impact zones, clear cratered rail, suppress impact fires, secure meteor fragments, request international relief, close airspace.

Key missions: restore one main rail corridor, clear the largest crater field, keep survivors sheltered, prevent fire chain in neighboring state.

Failure outcomes: deaths, fire spread, long infrastructure damage, international refugee pressure, military supply collapse.

AI behaviour: AI spends more than ordinary disaster budget. It should not attempt scientific salvage until rescue and rail are under control.

Asset direction: high chaos super event optional image direction, meteor storm map sprites, crater category seal.

## Flood borne famine and refugee chain

### Role

This is an aftermath family, not an initial disaster. It appears after flood, drought, cyclone, heat, volcano ash, earthquake, or any disaster that destroys harvest, shelter, water, or transport.

### Target logic

Eligible states have unresolved displacement, lost harvest, water contamination, transport collapse, refugee pressure, or supply failure. It can cross borders if neighboring countries have open borders, same faction, low stability, or occupied territory flows.

### Sequence shape

After a delay of weeks to months, not days. It should be newsworthy only when severe, international, or million scale deaths occur.

### Effects

Population loss through starvation, disease, exposure, or camp like overcrowding. Stability and war support damage. Supply strain. Refugee pressure state modifiers. Possible foreign relief decisions.

### Death model

All deaths are dynamic percentages of affected state populations. This is one of the main paths to millions of deaths after a disaster, especially in dense countries and war zones.

### Country hit category

Working category label: Famine and Displacement Commission.

Visible values: food reserve, refugee pressure, disease risk, shelter capacity, transport access, foreign relief access.

Key decisions: import food, requisition trains, open refugee camps, relocate civilians, ask faction for grain, protect medical supply, ration cities, ration army supply.

Key missions: keep the relief corridor open, feed the displaced before winter, prevent disease in shelters, stabilize refugee border states.

Failure outcomes: continuing deaths, chaos increase through deaths system, refugee spillover, local revolt or unrest if later systems support it.

AI behaviour: AI should seek foreign relief and stabilize food if death rate rises. It should not prefer production protection over famine prevention once deaths cross major thresholds.

Asset direction: refugee and ration icon, relief corridor map marker.

## Extreme cold darkness interaction

### Role

If another event creates global darkness or sun distance effects, Event 13 cold disasters should not duplicate those modifiers. It can still use local cold disaster aftermaths if the state has a unique blizzard, frozen rail, or refugee exposure incident.

### Target logic

Only use unique local effects when global cold is already active.

### Category rule

Use Winter Emergency Directorate, but text direction must avoid saying this is a new global cold event. It is a local disaster inside a wider cold state.

## Event family validation rule

Every implemented family must pass three checks.

1. It has family specific target logic and does not fire in nonsense states unless Evolution III abnormal logic says why.
2. It uses per state dynamic percentage deaths, not fixed death numbers.
3. Serious, regional, catastrophic, and abnormal hits open a family specific country category, not only the generic Natural Disaster Recovery category.
