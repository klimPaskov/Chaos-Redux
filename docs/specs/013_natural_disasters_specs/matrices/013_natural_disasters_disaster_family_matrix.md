
# Event 013 disaster family matrix

All labels are working labels and are not final localisation. Values are design direction, not exact script constants.

| Family | Baseline | Evo I | Evo II | Evo III | Primary targets | Main damage | Dynamic loss-rate profile | Warning | Recovery focus | Chain risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Flood | Yes | Yes | Yes | Yes | River, lowland, coast, urban. | Infrastructure, rail, civilian industry, supply. | Medium rate, high rate in dense floodplains and cities. | River advisory. | Pumps, rail clearance, shelters. | Wet movement, water stress, refugees. |
| Storm | Yes | Yes | Yes | Yes | Coast, plains, airbase states. | Airbases, infrastructure, civilian industry. | Low to medium rate. | Storm warning. | Debris clearance, shelters. | Flood, wind, hail. |
| Earthquake | Yes | Yes | Yes | Yes | Urban, mountain, built-up states. | Buildings, infrastructure, rail. | Medium to very high rate, with multi-million outcomes possible in dense states. | Seismic alert if prepared. | Inspections, engineers. | Aftershock, tsunami, bridge collapse. |
| Drought | Yes | Yes | Yes | Yes | Dry, warm, rural or supply-poor states. | Supply, stability, population over time. | Low immediate rate, higher delayed rate if relief fails. | Seasonal advisory. | Water rationing, relief corridors. | Famine, wildfire, refugees. |
| Wildfire | Yes | Yes | Yes | Yes | Forest, hills, dry, drought states. | Infrastructure, civilian industry, population. | Medium rate, high rate in dense or poorly evacuated states. | Fire weather alert. | Firebreaks, evacuation. | Smoke, spread, refugee pressure. |
| Blizzard | Yes | Yes | Yes | Yes | Cold, mountain, winter states. | Infrastructure, rail, supply. | Low to medium rate, higher with low fuel and blocked rail. | Winter advisory. | Heating fuel, rail clearance. | Exposure deaths, stranded transport. |
| Hailstorm | No | Yes | Yes | Yes | Plains, farms, airbase states. | Airbases, infrastructure, light industry. | Very low rate. | Storm warning. | Airfield dispersal, repair crews. | Flood or wind if storm outbreak. |
| Sandstorm | No | Yes | Yes | Yes | Desert and arid regions. | Supply, airbases, infrastructure. | Very low to low rate, with delayed exposure only when supply collapses. | Dust alert. | Dust clearance, airfield dispersal. | Transport disruption. |
| Thunderstorm outbreak | No | Yes | Yes | Yes | Warm, humid, plains, urban. | Mixed local damage. | Low to medium rate. | Weather alert. | Family-specific follow-up. | Flood, hail, wind, fire. |
| Extreme wind | No | Yes | Yes | Yes | Plains, coast, airbase states. | Airbase, infrastructure, civilian industry. | Low to medium rate. | Wind warning. | Shelters, aircraft dispersal. | Tornado corridor at Evo III. |
| Tropical cyclone | No | Yes | Yes | Yes | Warm coast, islands, ports. | Ports, dockyards, airbases, infrastructure. | Medium to high rate, with very large absolute deaths in dense coastal states. | Cyclone warning. | Coastal evacuation, port closure. | Flood, storm surge, refugees. |
| Wet mass movement | No | Yes | Yes | Yes | Mountain, hill, heavy rain. | Rails, infrastructure, supply hubs. | Medium rate. | Rain and slope alert. | Rail and road clearance. | Flood and refugee pressure. |
| Dry mass movement | No | Yes | Yes | Yes | Mountain, hill, dry or quake states. | Rails, infrastructure, supply hubs. | Low to medium rate. | Slope alert. | Engineering cleanup. | Aftershock or drought chain. |
| Volcano | No | Rare | Yes | Yes | Volcanic region list or fallback states. | Infrastructure, airbases, population, supply. | Medium to high rate, with delayed ash and lahar rates. | Observatory alert. | Ash cleanup, evacuation. | Ashfall, lahar, tsunami, crop stress. |
| Tsunami | No | Rare | Yes | Yes | Coastal states after quake, volcano, meteor. | Ports, dockyards, infrastructure, population. | High rate, with multi-million regional totals possible on dense coasts. | Coastal wave warning. | Evacuation, port closure. | Refugees, water stress. |
| Extreme heat wave | No | Yes | Yes | Yes | Hot, dry, urban or drought states. | Supply, population, stability. | Low immediate rate, medium delayed rate in dense or poorly supplied states. | Heat advisory. | Water rationing, shelters. | Drought and wildfire. |
| Extreme cold wave | No | Yes | Yes | Yes | Cold, northern, mountain states. | Supply, infrastructure, population. | Medium rate if fuel and rail fail. | Cold advisory. | Fuel, shelters, rail. | Exposure and transport collapse. |
| Glacial lake outburst | No | Rare | Yes | Yes | Mountain and glacial state groups. | Infrastructure, rail, population. | Medium rate. | Mountain water alert. | Evacuation, rail repair. | Wet mass movement, flood. |
| Meteor shower | No | No | Rare only by scenario | Yes | Several separated or clustered states. | Infrastructure, factories, airbases, population. | Medium to severe rate, with multi-million totals possible in dense clusters. | Skywatch alert. | Shelters, crater cleanup, firebreaks. | Fire, crater fields, refugee pressure. |
| Airburst field | No | No | No | Yes | High-chaos selected states. | Airbases, infrastructure, population. | Medium to severe rate. | Skywatch alert. | Shelters, rescue engineers. | Fire and panic. |
| Massive quake-wave | No | No | No | Yes | Regional seismic chain. | Many buildings, rail, ports, infrastructure. | Severe rate, explicitly allowed to create multi-million deaths in dense regions. | Seismic alert if prepared. | Inspections, rail, evacuation. | Aftershock and tsunami. |
| Moving storm corridor | No | No | No | Yes | Forecast path across several states. | Infrastructure, airbases, factories, population. | Medium to severe rate, summed across each state on the path. | Corridor forecast. | Track path, shelters, dispersal. | Follow-up floods and wind damage. |

## Death-rate interpretation

All death profiles are rates, not fixed death counts. Apply the selected family and severity rate to each affected state population separately. A sparse mountain state and a dense Chinese coastal state can share a family and severity, but the dense state must produce a much larger absolute death count because its population is larger. The implementation may cap the state-population percentage lost for balance, but it must not cap the absolute victims at a fixed number.
