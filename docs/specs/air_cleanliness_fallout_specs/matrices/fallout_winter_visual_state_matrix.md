# Air Winter Normal-Map Visual State Matrix

Working descriptions are asset and implementation direction. They are not player-facing localisation.

| Regional presentation class | Phase | Normal-map cue | Weather cue | Gameplay emphasis | Event eligibility |
| --- | --- | --- | --- | --- | --- |
| Boreal and continental | 0 | Normal seasonal snow only. | Normal weather. | No winter-phase penalty. | Ordinary seasonal incidents. |
| Boreal and continental | 1 | Cold blue light, thin frost, darker forests. | More frost and low cloud. | Heating and air-operation friction. | First haze, fuel demand, forecast error. |
| Boreal and continental | 2 | Persistent snow expansion, frozen soil. | Snow and cold snaps. | Food and rail pressure begins. | Livestock loss, seed concern, rural movement. |
| Boreal and continental | 3 | Deepening snow, ice on transport and water where supported. | Blizzard risk and poor visibility. | Supply, construction, and repair penalties. | Rail ice, transformer failure, port freeze. |
| Boreal and continental | 4 | Dark noon, heavy snow, abandoned lighting. | Severe cold and whiteout. | Population and building damage. | Black harvest, roof collapse, evacuation. |
| Boreal and continental | 5 | Dirty snow, buried roads, frozen ports, dead industrial vapor. | Persistent severe cold. | State-category damage and government strain. | Sealed districts, armed food corridors. |
| Boreal and continental | 6 | Near-black soot sky, extreme snow or ash-snow, terminal zones. | Highest cold and visibility loss. | Wasteland and Fallout pressure. | Underground survival, terminal abandonment. |
| Temperate maritime | 0 | Normal rain, cloud, and seasonal frost. | Normal weather. | No winter-phase penalty. | Ordinary maritime incidents. |
| Temperate maritime | 1 | Grey sea, cold rain, pale light. | Cool rain and fog. | Heating and air-operation friction. | Damp shelter, first port delay. |
| Temperate maritime | 2 | Sleet, wet snow, weakened vegetation. | Cold rain and occasional snow. | Crop and fishery pressure. | Orchard loss, fish movement, damp disease. |
| Temperate maritime | 3 | Persistent wet snow, icy roads, rough sea. | Storm, sleet, fog. | Port, convoy, and rail penalties. | Dirty harbor, bridge ice, transformer failure. |
| Temperate maritime | 4 | Frozen harbor edges, dark sea, flooded shelters. | Severe cold storms. | Population and building damage. | Port closure, evacuation, hospital overload. |
| Temperate maritime | 5 | Heavy wet snow, damaged roofs, blocked ports. | Persistent severe storms. | Category damage and maritime isolation. | Refuge ships, ice commission, district abandonment. |
| Temperate maritime | 6 | Black rain and snow mixture, terminal coastal darkness. | Extreme cold storm state. | Fallout pressure and coastal wasteland. | Harbor collapse, sealed shore, survivor flotilla. |
| Mediterranean | 0 | Normal dry or wet seasonal pattern. | Normal weather. | No winter-phase penalty. | Ordinary agricultural incidents. |
| Mediterranean | 1 | Pale low sun, valley frost, cold wind. | Cool rain and mountain snow. | Heating and aviation friction. | First frost, fuel shortage. |
| Mediterranean | 2 | Orchard discoloration, highland snow, colder coast. | Frost and cold rain. | Perennial crop and food pressure. | Orchard inventory, livestock shelter. |
| Mediterranean | 3 | Repeated frost, snow at lower elevations, damaged roads. | Sleet, mountain storm. | Transport and repair penalties. | Pass closure, transformer and water failures. |
| Mediterranean | 4 | Severe valley frost, dark sea, abandoned groves. | Persistent cold and snow in uplands. | Population and building damage. | Food riots, rural evacuation, port strain. |
| Mediterranean | 5 | Dead orchards, damaged roofs, snow in exceptional lowlands. | Severe regional cold. | Category damage and migration. | State abandonment, mountain refuge politics. |
| Mediterranean | 6 | Ash-dark sky, terminal cold state with region-fit snow and frost. | Highest anomaly. | Fallout pressure and forbidden zones. | Sealed valleys, dead city, underground refuge. |
| Desert and arid plateau | 0 | Normal dry climate. | Normal weather. | No winter-phase penalty. | Ordinary water incidents. |
| Desert and arid plateau | 1 | Cold dust haze, long shadows, frost near pipes. | Cold nights and dry wind. | Heating, water, and transport friction. | First frozen pump, livestock shelter. |
| Desert and arid plateau | 2 | More frequent frost, rare highland snow, dim sun. | Cold nights and occasional sleet. | Water and livestock pressure. | Well queue, pipeline failure, crop loss. |
| Desert and arid plateau | 3 | Frozen pipes, cold dust storms, rare lowland snow in severe cases. | Dry cold storm and poor visibility. | Supply, pumping, and repair penalties. | Water convoy, generator failure, road isolation. |
| Desert and arid plateau | 4 | Severe cold nights, damaged settlements, frozen wells. | Persistent cold and dust. | Population and building damage. | Refugee mortality, well seizure, fuel ration. |
| Desert and arid plateau | 5 | Long severe cold, abandoned oases, darkened refineries. | Extreme arid cold. | Category damage and migration. | Oasis abandonment, water war, sealed refinery. |
| Desert and arid plateau | 6 | Terminal cold dust and ash, local snow only where plausible. | Highest anomaly and low visibility. | Fallout pressure and dead zones. | Buried convoy, sealed well, wasteland corridor. |
| Tropical coast and monsoon | 0 | Normal warm rain and monsoon cycle. | Normal weather. | No winter-phase penalty. | Ordinary crop and port incidents. |
| Tropical coast and monsoon | 1 | Cooler rain, low cloud, dimmed sea. | Cold rain and fog. | Aviation and crop-timing friction. | Unusual chill, port delay. |
| Tropical coast and monsoon | 2 | Persistent cold rain, highland frost, weaker canopy. | Delayed or failed monsoon. | Food, disease, and fishery pressure. | Rot tide, crop timing failure, migration. |
| Tropical coast and monsoon | 3 | Cold storms, landslides, damaged roads, rough grey sea. | Storm and low visibility. | Port, supply, and repair penalties. | Bridge washout, clinic overload, fish movement. |
| Tropical coast and monsoon | 4 | Severe crop failure, highland snow, dark coastal cities. | Prolonged cold rain or dry monsoon failure. | Population and building damage. | Famine, port quarantine, mass movement. |
| Tropical coast and monsoon | 5 | Canopy dieback, isolated ports, persistent cold anomaly. | Severe disrupted weather. | Category damage and state abandonment. | Refuge islands, river disease, armed food routes. |
| Tropical coast and monsoon | 6 | Ash-dark tropical sky, cold rain or dry chill, terminal zones. | Highest anomaly. | Fallout pressure and altered ecology gates. | Sealed coast, dead port, fictional ecology. |
| Equatorial rainforest | 0 | Normal warm wet forest. | Normal weather. | No winter-phase penalty. | Ordinary river and forest incidents. |
| Equatorial rainforest | 1 | Chilled mist, darker rivers, reduced flowering. | Cool rain and persistent cloud. | Food gathering and aviation friction. | Unusual mist, first fruit loss. |
| Equatorial rainforest | 2 | Canopy discoloration, cold highlands, wet ash. | Rain disruption and cold mist. | Food, river, and disease pressure. | Canopy cold, fungal disease, river delay. |
| Equatorial rainforest | 3 | Landslides, dark rivers, damaged canopy, ash accumulation. | Cold storm or rain failure. | Supply and repair penalties. | River convoy loss, clinic crisis, isolated town. |
| Equatorial rainforest | 4 | Severe dieback, failed fruit, settlement movement. | Persistent cold and rain disruption. | Population and building damage. | Basin evacuation, food conflict, disease. |
| Equatorial rainforest | 5 | Large dead zones, altered wetlands, isolated river states. | Severe anomaly. | Category damage and fictional ecology eligibility. | River silence, protected orchard, high-chaos ecology. |
| Equatorial rainforest | 6 | Terminal dark canopy, ash wetlands, severe cold mist. | Highest anomaly. | Fallout pressure and forbidden basin. | Sealed river, altered polity, wasteland jungle. |
| Mountain and highland | 0 | Normal elevation snow and pass conditions. | Normal weather. | No winter-phase penalty. | Ordinary pass incidents. |
| Mountain and highland | 1 | Snow line descends, frost and cold light. | More snow and fog. | Pass and aviation friction. | First closure, shelter demand. |
| Mountain and highland | 2 | Persistent snow, avalanche concern, frozen water. | Snowstorm risk. | Food, hydro, and transport pressure. | Tunnel school, dam ice, pass census. |
| Mountain and highland | 3 | Deep snow, blocked passes, avalanche scars. | Blizzard and low visibility. | Supply and repair penalties. | Avalanche rescue, rail tunnel failure. |
| Mountain and highland | 4 | Severe whiteout, isolated valleys, damaged roofs. | Persistent severe snow. | Population and building damage. | Mountain evacuation, shelter conflict. |
| Mountain and highland | 5 | Buried routes, failing tunnels, hydro isolation. | Extreme snow. | Category damage and local government breakdown. | Tunnel state, pass war, sealed valley. |
| Mountain and highland | 6 | Terminal highland ice and soot, extreme isolation. | Highest cold anomaly. | Fallout pressure and refuge survival. | Underground polity, dead pass, forbidden peak. |
| Island and oceanic | 0 | Normal ocean weather. | Normal weather. | No winter-phase penalty. | Ordinary island incidents. |
| Island and oceanic | 1 | Darker sea, cooler wind, ash rain. | Cool storm and fog. | Port and aviation friction. | First fish shift, refugee boat. |
| Island and oceanic | 2 | Cold storms, high-island frost, rougher sea. | Storm and changed currents. | Food, fishery, and convoy pressure. | Fish move, quarantine anchorage, crop chill. |
| Island and oceanic | 3 | Persistent rough sea, icy highlands, ash accumulation. | Severe storm. | Port, convoy, and repair penalties. | Cyclone in cold sea, dock failure. |
| Island and oceanic | 4 | Severe food and port crisis, dark island settlements. | Persistent cold storm. | Population and building damage. | Lifeboat law, evacuation, pirate pressure. |
| Island and oceanic | 5 | Isolated archipelagos, failed crops, damaged ports. | Extreme oceanic anomaly. | Category damage and migration. | Refuge fleet, island abandonment, radio chain. |
| Island and oceanic | 6 | Terminal ash sea and cold storm state. | Highest anomaly. | Fallout pressure and maritime survivor routes. | Floating polity, dead harbor, sealed atoll. |
| Polar and subpolar | 0 | Normal polar cold and ice. | Normal weather. | No winter-phase penalty. | Ordinary station incidents. |
| Polar and subpolar | 1 | Longer darkness, thicker frost, early ice. | More cold and wind. | Fuel and radio friction. | Fuel horizon, weather balloon. |
| Polar and subpolar | 2 | Sea-ice expansion, more whiteout, buried stores. | Snow and wind. | Food, fuel, and route pressure. | Ice road, station ration. |
| Polar and subpolar | 3 | Severe whiteout, buried runway, damaged antenna. | Blizzard and extreme cold. | Supply and repair penalties. | Runway rescue, radio loss. |
| Polar and subpolar | 4 | Extreme darkness, isolated stations, structural damage. | Persistent extreme cold. | Population and building damage. | Station vote, evacuation, mutiny. |
| Polar and subpolar | 5 | Buried facilities, failed fuel, long isolation. | Severe persistent cold. | Category damage and protocol breakdown. | Machine contact, crew conflict, station collapse. |
| Polar and subpolar | 6 | Terminal polar night, soot-dark ice, complete isolation. | Highest anomaly. | Fallout pressure and rare survivor state. | Polar polity, lost station, high-chaos signal. |
