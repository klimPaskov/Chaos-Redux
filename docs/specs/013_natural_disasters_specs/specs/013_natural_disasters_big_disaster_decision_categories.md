# Event 013 Natural Disasters big disaster decision categories

All labels in this file are working labels and are not final localisation.

## Design change from the earlier package

The earlier package overused one generic recovery category. That is not enough. The generic Natural Disaster Recovery overview remains as the small local incident surface and routing hub. Every big disaster that hits a country must open its own disaster specific decision category for that country.

A country can have more than one active disaster category if it is hit by multiple big disasters. To avoid clutter, each category must hide when no active warning, impact, aftermath, or recovery marker from that family remains. The overview category should show which family categories are active and which state or region each category is handling.

## Category lifecycle

| Phase | Category behaviour |
| --- | --- |
| Warning | Category appears with warning actions, evacuation, closures, resource staging, and forecast details. |
| Impact | Category shifts to rescue, triage, shutdown, and emergency supply actions. |
| Recovery | Category shows missions, repairs, shelters, and follow up risk. |
| Aftermath | Category stays active for famine, refugees, ash, fire, floodwater, aftershock, or corridor pressure. |
| Closure | Category hides after cleanup, recovery missions, state modifiers, and family variables are cleared. |

A category should not be a store. It must have a readable current crisis, a limited action list, at least one objective or mission for serious disasters, AI behaviour, and cleanup.

## Shared category values

Each big disaster category may show different values, but all should support a common data model so scripted localisation can reuse helper logic.

| Shared value | Purpose |
| --- | --- |
| active disaster family id | Routes localisation, icons, category open state, and cleanup. |
| primary state target | Names the worst affected state in text. |
| affected state count | Lets the UI explain whether it is local or regional. |
| current death pressure | Shows whether follow up deaths are still active. |
| recovery progress | Tracks mission and decision completion. |
| relief access | Shows whether domestic, faction, foreign, or no relief is available. |
| logistics strain | Helps costs scale with rail, ports, trains, trucks, convoys, and fuel. |
| warning quality | Reduces initial loss rate if warning actions succeeded. |
| unresolved aftermath count | Keeps category visible until the crisis is truly cleaned. |

## Category registry

| Working category id | Opens for | Main gameplay identity |
| --- | --- | --- |
| nd_cat_flood_relief_authority | Serious or larger flood, flood basin, flood aftermath. | Water, rail, dikes, wells, housing, food. |
| nd_cat_cyclone_emergency_command | Serious or larger tropical cyclone, storm surge, island landfall. | Forecast track, evacuation, ports, dockyards, airfields. |
| nd_cat_severe_storm_office | Serious thunderstorm outbreak, hailstorm, ordinary storm, extreme wind. | Debris, airfields, radar, crop damage, flash flood prevention. |
| nd_cat_storm_corridor_command | Evolution III moving tornado or storm corridor. | Current path, forecast states, shelter, moving danger. |
| nd_cat_seismic_emergency_authority | Serious earthquake or aftershock chain. | Rubble, bridges, hospitals, aftershocks, tsunami watch. |
| nd_cat_great_rupture_command | Evolution III great rupture wave. | Stress front, multiple states, dams, tsunami, rail collapse. |
| nd_cat_tsunami_coastal_command | Tsunami warning or impact. | Wave timing, coast evacuation, port recovery, islands. |
| nd_cat_volcanic_crisis_office | Volcanic eruption, ashfall, lahar. | Ash, airfields, water, lahar valleys, evacuation. |
| nd_cat_massive_eruption_command | Evolution III massive volcano or volcanic ring. | Multiple eruption pulses, ash cloud map, famine, regional air closure. |
| nd_cat_firefront_command | Serious wildfire or firestorm. | Fire spread, water, fuel, evacuation, smoke. |
| nd_cat_drought_famine_office | Serious drought, famine risk, water emergency. | Water reserve, crops, food imports, refugees. |
| nd_cat_heat_emergency_office | Serious local or regional extreme heat. | Shelters, water, grid strain, non stacking with Event 51. |
| nd_cat_winter_emergency_directorate | Serious blizzard, extreme cold, frozen rail. | Fuel, shelters, rail switches, ports, exposure. |
| nd_cat_dust_emergency_office | Serious sandstorm, dust belt, abnormal dust wall. | Visibility, airfields, wells, desert supply. |
| nd_cat_landslide_rescue_office | Wet mass movement and landslide. | Buried rail, valleys, rivers, pass closure. |
| nd_cat_slope_collapse_response | Dry mass movement, rockfall, mine collapse. | Mines, tunnels, desert roads, rail passes. |
| nd_cat_skyfall_emergency_bureau | Meteor shower and skyfall field. | Impact shelters, cratered rail, fire, skywatch. |
| nd_cat_meteor_storm_command | Maximum meteor barrage. | Several impact clusters, national sheltering, crater cleanup. |
| nd_cat_famine_displacement_commission | Follow up famine, refugee, shelter collapse. | Food, shelter, disease, transport, cross border pressure. |

## Cost model for all categories

Costs must be dynamic and physical. Political power is allowed only when the action is administrative, diplomatic, or public order oriented. Command power is allowed only for military coordination and must remain conservative.

Use these cost pools.

- Support equipment for engineers, pumps, hospitals, shelters, masks, and repairs.
- Infantry equipment for civil defense, emergency guards, shelter supply, and firefighting teams.
- Trucks for evacuation, water, food, and debris operations.
- Trains for mass evacuation, relief corridors, rail recovery, and food transport.
- Convoys for island relief, port recovery, and international aid.
- Fuel for pumps, aircraft relocation, water convoys, firefighting, and rail clearing.
- Manpower for rescue crews, field hospitals, evacuation staff, and shelter operations.
- Army XP for engineer coordination, rescue doctrine, and bridge inspection.
- Air XP for airfield repair, aircraft dispersal, and ash or dust flight protocol.
- Navy XP for port closure, fleet movement, harbor salvage, and coastal evacuation.
- Stability and war support for rationing, forced evacuation, factory shutdown, and public panic.
- Civilian factory burden for rebuilding, shelters, levees, repairs, and supply hubs.
- Local state requirements such as control, supply connection, rail access, port access, or divisions present.

## Flood Relief Authority

### Values

Floodwater depth pressure, blocked rail states, contaminated water, dike stability, displaced population, relief train access.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Reinforce the dikes | Support equipment, civilian factory burden, manpower. | Lowers flood spread and dike breach chance. |
| Deploy pumping columns | Fuel, trucks, support equipment. | Speeds floodwater removal and protects infrastructure. |
| Evacuate lowland districts | Trains, trucks, fuel, stability cost. | Reduces deaths, raises displaced population until shelters exist. |
| Chlorinate wells | Support equipment and medical style resource if present. | Lowers delayed death pressure and disease risk. |
| Open relief rail | Trains, rail state control, support equipment. | Opens relief access and mission progress. |
| Prioritize industry district | Civilian factory burden and stability risk. | Saves factories but can slow housing recovery. |
| Prioritize housing district | Manpower and support equipment. | Lowers refugee pressure but saves fewer factories. |

### Mission families

- Clear the river rail belt.
- Keep relief trains supplied.
- Repair the dike before the next rain report.
- Shelter the displaced before famine pressure begins.

### Failure package

Floodwater contamination adds delayed deaths. Dike failure hits one neighbor. Relief failure adds refugee pressure and local stability loss.

## Cyclone Emergency Command

### Values

Forecast confidence, landfall timer, surge risk, evacuation capacity, port closure, inland flood risk, relief convoy access.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Coastal evacuation order | Trains, trucks, convoys for islands, fuel, stability. | Greatly lowers deaths if used before landfall. |
| Close threatened ports | Navy XP, convoys, dockyard burden. | Lowers port and dockyard damage, disrupts trade and fleet operations. |
| Disperse air wings | Air XP and temporary air mission penalty. | Lowers airbase and aircraft loss. |
| Reinforce sea walls | Civilian factory burden, support equipment. | Lowers storm surge damage. |
| Stage island relief convoys | Convoys, fuel, naval access. | Prevents island famine and opens recovery. |
| Clear harbor wreckage | Dockyard burden, support equipment, convoys. | Reopens port and naval base. |

### Mission families

- Evacuate the island chain before landfall.
- Reopen the main naval base.
- Keep inland flood from cutting supply.
- Shelter the coast until relief convoys arrive.

### Failure package

Storm surge deaths increase. Port remains closed. Island famine pressure starts. Refugees move inland.


## Severe Storm Response Board

### Values

Storm line severity, debris clearance, flash flood risk, crop damage, airfield damage, radar damage, shelter pressure.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Open storm shelters | Manpower, support equipment, stability. | Lowers population loss in dense states. |
| Ground threatened aircraft | Air XP and temporary air mission loss. | Reduces airbase and aircraft damage. |
| Clear debris roads | Trucks, fuel, manpower. | Restores supply and movement. |
| Repair radar and anti air | Support equipment and air XP. | Restores air defense assets. |
| Protect harvest stores | Infantry equipment, support equipment. | Lowers crop shock and famine risk. |
| Prepare flash flood pumps | Support equipment, fuel. | Lowers flood follow up chance. |

### Mission families

- Clear the airbase belt.
- Restore storm cut roads.
- Prevent flash flood follow up.
- Protect harvest stores before spoilage.

### Failure package

Flash flood, crop shock, local supply penalty, airbase closure, delayed deaths in shelters if severe.

## Hail Damage Board

### Values

Crop damage, airfield surface damage, aircraft exposure, roofing shortage, famine linkage risk.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Repair airfield surfaces | Air XP, support equipment, trucks. | Reopens airbases and lowers aircraft damage. |
| Salvage exposed aircraft | Air XP and manpower. | Reduces aircraft disruption if equipment helpers exist. |
| Protect harvest stores | Support equipment, manpower. | Lowers delayed famine risk. |
| Release seed reserves | Stability or food reserve pressure, if modeled. | Speeds crop recovery. |
| Import roofing material | Trains or convoys, civilian burden. | Lowers shelter and factory damage. |

### Mission families

- Recover agricultural output before drought season.
- Keep key airbase operational.
- Prevent crop shock from becoming famine.

### Failure package

Crop loss feeds famine pressure if drought, blockade, refugee pressure, or war supply failure exists. Airbase damage lasts longer.

## Wind Damage Control

### Values

Wind swath damage, airbase closure, rail signal failure, shelter damage, industrial debris, supply route obstruction.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Reinforce public shelters | Support equipment, manpower. | Lowers population loss in forecast swath. |
| Clear industrial debris | Trucks, manpower, civilian burden. | Restores civilian and military industry faster. |
| Repair rail signals | Support equipment, trains, army XP. | Restores supply and movement. |
| Ground aircraft | Air XP and temporary air mission loss. | Lowers airfield and aircraft damage. |
| Requisition emergency trucks | Trucks, fuel, stability. | Speeds rescue and road clearance. |

### Mission families

- Restore the airbase network.
- Reopen the wind cut supply line.
- Clear industrial debris before production stalls.

### Failure package

Air mission penalties, infrastructure damage extension, refugee pressure from housing damage, follow up fire if high heat or drought is active.

## Storm Corridor Command

### Values

Current corridor state, forecast next states, path confidence, shelter readiness, rail vulnerability, observation coverage, next movement timer.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Activate observation net | Air XP, fuel, radar or civilian burden. | Improves forecast confidence and path display. |
| Evacuate forecast corridor | Trains, trucks, fuel, stability. | Lowers deaths in forecast states. |
| Reinforce rail junctions | Support equipment, trains, army XP. | Lowers rail destruction in likely path. |
| Ground aircraft in projected path | Air XP and temporary air mission loss. | Reduces airfield and aircraft damage. |
| Deploy mobile hospitals | Support equipment, trucks, manpower. | Lowers ongoing death pressure after impact. |
| Attempt corridor disruption | Very high fuel, air XP, command power, risk. | Can lower path severity or fail and waste resources. |

### Mission families

- Protect the forecast belt.
- Keep the capital connected while corridor passes.
- Reopen the shattered rail junction.
- Shelter displaced people before the next movement tick.

### Failure package

The next state is hit with weaker warning, damage rates rise, refugee pressure spreads, and corridor map danger increases.

## Seismic Emergency Authority

### Values

Aftershock risk, rubble rescue progress, bridge integrity, hospital damage, water safety, tsunami watch, landslide watch.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Deploy heavy rescue engineers | Support equipment, army XP, manpower. | Reduces delayed deaths and speeds rubble clearance. |
| Shut down damaged bridges | Stability and supply penalty. | Prevents bridge collapse follow up. |
| Open field hospitals | Support equipment, manpower, trucks. | Lowers death pressure and stability shock. |
| Inspect aftershock zones | Army XP, support equipment. | Lowers aftershock damage. |
| Evacuate coastal districts | Trains, trucks, fuel. | Prepares for delayed tsunami if coastal. |
| Stabilize rail tunnels | Support equipment, civilian burden. | Protects supply hub and rail. |

### Mission families

- Clear capital rubble.
- Inspect aftershocks before the next tremor.
- Keep the rail tunnel open.
- Evacuate the coast before the delayed wave.

### Failure package

Aftershock damages same or neighbor state. Bridge collapse adds deaths and supply damage. Coastal failure can call Tsunami Coastal Command.

## Great Rupture Command

### Values

Stress front, aftershock count, destroyed rail belt, dam stability, tsunami watch, regional rescue capacity.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| National engineer mobilization | Large support equipment, army XP, manpower, civilian burden. | Speeds regional recovery and lowers multiple follow up risks. |
| Evacuate tsunami watch coast | Trains, trucks, convoys, fuel. | Lowers delayed wave deaths. |
| Stabilize dams | Support equipment, civilian factories, fuel. | Prevents dam failure flood. |
| Create exclusion zones | Stability and production penalty. | Lowers deaths in aftershock states. |
| Request international rescue | Relations or faction access, convoys, political cost. | Adds recovery support and possible foreign influence. |

### Mission families

- Hold relief supply through the broken rail belt.
- Clear three priority cities.
- Prevent dam failure in the damaged basin.
- Restore capital supply hub.

### Failure package

Dam failure spawns flood branch. Tsunami branch can fire. Regional famine or refugee chain starts.

## Tsunami Coastal Command

### Values

Wave arrival estimate, evacuation readiness, harbor wreckage, island isolation, contaminated wells, fishing fleet loss.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| High ground evacuation | Trains, trucks, convoys, fuel. | Major death rate reduction if warning exists. |
| Move fleet out of harbor | Navy XP and fuel. | Reduces naval base and ship disruption. |
| Close the port gates | Dockyard burden and trade disruption. | Lowers port damage. |
| Prepare high ground shelters | Support equipment, manpower. | Reduces deaths and refugee pressure. |
| Clear harbor wreckage | Convoys, dockyards, support equipment. | Reopens port. |
| Restore wells | Support equipment, trucks. | Removes saltwater and disease pressure. |

### Mission families

- Evacuate the forecast coast.
- Reconnect isolated islands.
- Restore the main port.
- Clear contaminated wells.

### Failure package

Mass deaths, island famine, port closure, refugee pressure, coastal economy damage.

## Volcanic Crisis Board

### Values

Eruption stage, ash cloud spread, lahar risk, airfield closure, water safety, evacuation route.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Evacuate volcano slopes | Trucks, trains, manpower, stability. | Reduces direct eruption and lahar deaths. |
| Ground ash exposed aircraft | Air XP and air mission penalty. | Reduces airbase and aircraft disruption. |
| Clear ash from roofs | Manpower, support equipment, civilian burden. | Lowers roof collapse deaths and factory damage. |
| Protect water sources | Support equipment, trucks. | Lowers delayed deaths. |
| Build lahar barriers | Civilian factory burden, support equipment. | Lowers lahar follow up chance. |
| Request volcanology mission | Political cost, foreign access. | Improves warning and reduces follow up risk. |

### Mission families

- Reopen ash covered airfields.
- Prevent lahar in named valley states.
- Feed the ash covered crop belt.
- Evacuate island settlements.

### Failure package

Lahar impact, ash deaths, airfield closure, crop failure, refugee pressure.

## Massive Eruption Command

### Values

Eruption pulse count, ash cloud map, lahar belts, crop pressure, air closure, water safety, evacuation capacity.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| National ash clearing | Large manpower, trucks, support equipment, fuel. | Lowers ash deaths and building damage across many states. |
| Close ash filled airspace | Air XP and air operation penalty. | Prevents aircraft and airbase losses. |
| Divert lahars | Civilian factory burden, support equipment. | Prevents valley destruction. |
| Import emergency food | Convoys or trains, political cost, relations. | Prevents ash famine. |
| Mobilize respiratory hospitals | Support equipment and manpower. | Lowers ongoing deaths. |
| Evacuate eruption zone | Trains, trucks, convoys for islands, stability. | Reduces direct deaths and refugee pressure. |

### Mission families

- Clear ash from capital roofs.
- Keep a port open under ashfall.
- Feed the ash covered region.
- Restore airbase operations.

### Failure package

Regional famine, respiratory deaths, long air operations penalty, multi state refugee crisis.

## Firefront Command

### Values

Fire spread chance, wind support, water access, evacuation progress, smoke pressure, burned infrastructure.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Cut firebreaks | Infantry equipment, support equipment, manpower. | Lowers spread chance. |
| Deploy army fire crews | Command power, manpower, fuel, trucks. | Speeds containment, can strain front readiness. |
| Evacuate threatened towns | Trucks, trains, fuel, stability. | Lowers deaths and raises shelter load. |
| Protect ammunition depots | Army XP, support equipment. | Prevents secondary explosion or military factory damage. |
| Ground smoke trapped aircraft | Air XP and temporary mission loss. | Prevents air losses and accident aftermath. |
| Controlled burns | Fuel, command power, risk. | Can stop spread or worsen fire if wind changes. |

### Mission families

- Contain the fire front.
- Protect the rail bridge.
- Keep the fire from reaching industry.
- Clear smoke from airfields.

### Failure package

Fire spreads, industry burns, smoke deaths, refugee pressure, supply penalty.

## Drought and Famine Board

### Values

Water reserve, crop survival, ration strain, famine pressure, refugee outflow, wildfire and sandstorm risk.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Water rationing | Stability, trucks, local infrastructure. | Slows deaths and drought escalation. |
| Emergency wells | Civilian factory burden, support equipment. | Restores water reserve. |
| Grain imports | Convoys or trains, political cost, relations. | Lowers famine pressure. |
| Protect seed reserves | Infantry equipment, support equipment, stability. | Improves recovery and prevents long crop penalty. |
| Water convoys | Trucks, fuel, manpower. | Lowers immediate deaths. |
| City first ration plan | War support or stability impact. | Saves urban population, raises rural crop failure risk. |
| Countryside first ration plan | War support or stability impact. | Saves harvest, raises urban heat death risk. |

### Mission families

- Feed the drought belt.
- Keep water convoys running.
- Protect seed reserves until the next season.
- Shelter drought refugees.

### Failure package

Famine deaths, refugee pressure, wildfire risk, sandstorm risk, local unrest.

## Heat Emergency Board

### Values

Heat stress, water reserve, shelter capacity, grid strain, wildfire risk, Event 51 guard state.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Open cooling shelters | Manpower, support equipment, stability. | Lowers death rate in dense states. |
| Hospital heat protection | Support equipment, trucks, fuel. | Lowers delayed deaths. |
| Shift factory hours | Production penalty and stability. | Lowers worker death pressure and grid strain. |
| Water import convoys | Trucks, fuel, convoys or trains. | Lowers water death pressure. |
| Night rail routing | Fuel and rail capacity. | Prevents rail buckling and supply loss. |
| Suspend desert maneuvers | Command power or war support. | Lowers army attrition pressure. |

### Mission families

- Keep city shelters open.
- Prevent grid collapse.
- Restore water convoys.
- Protect harvest under heat.

### Failure package

Delayed heat deaths, drought branch, wildfire branch, stability loss, production penalty.

## Winter Emergency Directorate

### Values

Fuel reserve, shelter heat, rail switch status, stranded population, mountain pass closure, frozen port.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Allocate heating fuel | Fuel and stability. | Lowers exposure deaths. |
| Clear rail switches | Trains, fuel, support equipment. | Restores supply. |
| Shelter refugees | Manpower, support equipment, stability. | Lowers deaths and refugee pressure. |
| Reopen mountain pass | Support equipment, trucks, fuel. | Restores supply and movement. |
| Thaw port machinery | Navy XP, fuel, dockyard burden. | Reopens frozen port. |
| Suspend winter offensive | Command power, war support or attack penalty. | Lowers military and civilian exposure pressure. |

### Mission families

- Keep the capital heated.
- Clear the frozen rail belt.
- Rescue stranded trains.
- Hold supply through the mountain pass.

### Failure package

Exposure deaths, rail collapse, front supply crisis, refugee death pressure.

## Dust Emergency Board

### Values

Visibility, airfield closure, water safety, convoy route, dust belt movement, engine damage.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Ground aircraft | Air XP and temporary air mission loss. | Reduces airbase and aircraft damage. |
| Clear airfields | Trucks, fuel, support equipment. | Removes airfield closure. |
| Issue masks and filters | Support equipment and manpower. | Lowers delayed deaths and supply penalties. |
| Reroute desert convoys | Trucks, fuel. | Keeps supply active. |
| Secure wells | Infantry equipment and support equipment. | Prevents water contamination and refugee deaths. |
| Close desert roads | Supply and movement penalty. | Prevents convoy loss and death pressure. |

### Mission families

- Reopen the desert airfield.
- Keep the desert supply route active.
- Protect wells.
- Clear rail drift.

### Failure package

Airbase damage, engine damage, supply collapse, water crisis, refugee deaths.

## Landslide Rescue Board and Slope Collapse Response

### Values

Buried rail, isolated valley, slope instability, river blockage, mine collapse, rescue access.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Clear the mountain pass | Support equipment, trucks, manpower. | Restores supply and movement. |
| Rescue buried settlements | Manpower, support equipment. | Lowers death pressure. |
| Stabilize slope | Civilian burden, support equipment. | Prevents repeat collapse. |
| Divert blocked river | Fuel, support equipment, civilian burden. | Prevents flood follow up. |
| Rescue miners | Support equipment, manpower, army XP. | Restores resource output and lowers deaths. |
| Stabilize tunnel | Support equipment, army XP. | Protects rail. |

### Mission families

- Reconnect isolated valley.
- Clear pass before winter.
- Prevent river blockage flood.
- Rescue trapped mine workers.

### Failure package

Flood follow up, resource loss, starvation in isolated valley, repeated collapse.

## Skyfall Emergency Bureau

### Values

Impact count, skywatch confidence, crater fields, fire risk, dust in airfields, shelter capacity, observatory reports.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Activate skywatch network | Air XP, civilian burden, research or observatory state if available. | Improves warning and forecast state. |
| Open impact shelters | Support equipment, manpower, stability. | Lowers meteor deaths in predicted states. |
| Evacuate predicted impact area | Trains, trucks, fuel. | Lowers deaths, raises refugee pressure. |
| Clear cratered rail | Support equipment, trucks, manpower. | Restores supply. |
| Contain impact fires | Fuel, support equipment, infantry equipment. | Prevents wildfire follow up. |
| Ground aircraft through dust | Air XP and air mission penalty. | Prevents airbase and aircraft damage. |
| Secure fragments | Army XP or research investment. | Grants research or intelligence only after rescue needs are handled. |

### Mission families

- Keep capital shelters open.
- Clear cratered rail.
- Prevent fire spread after airburst.
- Recover observatory instruments.

### Failure package

Crater field persists, fire spreads, death rate rises, airfield closes, refugee pressure increases.

## Meteor Storm Command

### Values

Impact clusters, national shelter order, crater severity, fire chains, rail craters, airspace closure, scientific salvage.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| National shelter order | Stability, manpower, support equipment. | Lowers deaths across predicted clusters. |
| Triage impact zones | Manpower, trucks, support equipment. | Reduces ongoing death pressure. |
| Close national airspace | Air XP and air operation penalty. | Lowers aircraft losses. |
| Clear largest crater field | Large support equipment, trucks, fuel, manpower. | Restores key state and lowers supply penalty. |
| Suppress impact fire chain | Fuel, support equipment, infantry equipment. | Prevents wildfire spread. |
| International relief appeal | Political cost, relations, convoys. | Adds relief and possible dependency. |
| Scientific salvage after rescue | Research or civilian burden. | Grants research only if death pressure is under control. |

### Mission families

- Restore one main rail corridor.
- Clear the largest crater field.
- Keep survivors sheltered.
- Prevent fire chain in neighbor states.

### Failure package

Mass deaths, long infrastructure loss, fire chain, major news, refugee pressure.

## Famine and Displacement Commission

### Values

Food reserve, shelter load, disease pressure, refugee outflow, relief route, border strain.

### Decision set

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Import food | Convoys, trains, relations, political cost. | Lowers famine deaths. |
| Requisition army trucks | Trucks, fuel, command power. | Opens internal food routes. |
| Open temporary shelters | Support equipment, manpower, stability. | Lowers exposure and disease deaths. |
| Relocate civilians | Trains, trucks, stability. | Lowers deaths in one state, raises pressure elsewhere. |
| Request faction grain | Relations or faction access, convoys. | Lowers famine pressure and may create obligation. |
| Protect medical supply | Support equipment, manpower. | Lowers disease pressure. |

### Mission families

- Keep the relief corridor open.
- Feed the displaced before winter.
- Prevent disease in shelters.
- Stabilize refugee border states.

### Failure package

Continuing dynamic percentage deaths, chaos through death system, border strain, local unrest where supported.

## Category clutter and active cap

The overview category may show many active disaster summaries, but family categories must limit visible actions.

Recommended visible action cap per family category:

- Warning phase: three to five decisions.
- Impact phase: three to six decisions.
- Recovery phase: two to four decisions plus one to three missions.
- Regional crisis: four to six decisions plus capped mission list.
- Abnormal corridor: map panel plus two to four current path actions.

Hidden decisions can exist for AI or backend routing. Player visible categories must remain curated.

## Cleanup requirements

Every category must clear:

- active family flags,
- selected target state variables,
- forecast state variables,
- category open flags,
- active mission flags,
- temporary cost variables,
- relief access flags that belong only to the disaster,
- aftermath count variables,
- stale map markers,
- stale scripted GUI selection states.

Cleanup should occur after recovery completion, tag annexation, state ownership loss where the country no longer has responsibility, event system reset, world end terminal state, or manual scenario cleanup.
