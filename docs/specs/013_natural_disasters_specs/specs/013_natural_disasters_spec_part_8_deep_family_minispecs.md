# Event 013 Natural Disasters, Part 8, deep disaster family mini-specs

This file expands the first family playbook pass into implementation-ready design direction. It still does not write final localisation. All decision keys, card fields, report labels, news labels, and state modifier labels are working labels only.

Every disaster family must keep its own warning logic, aftermath card, AI priority, report direction, news threshold, state modifier profile, and chain routes. If the implementation makes two families use the same target list, same damage profile, same recovery tasks, and same report direction, one of those families should become a follow-up chain instead of a separate family.

## Shared aftermath card contract

Every active disaster card should use the same player-readable field set so the UI remains predictable. The field values differ by family.

| Card field | Purpose |
| --- | --- |
| `family_key` | Internal family key used by scripted localisation, icons, reports, and chain logic. |
| `family_group` | Broad hazard group for filters and visual grouping. |
| `primary_state` | Main affected state, with optional linked states displayed below it. |
| `impact_signature` | Short direction for the visual damage identity. This is not final text. |
| `severity_band` | Local, severe, regional, abnormal, or barrage. |
| `primary_damage_profile` | What the player should understand was damaged. |
| `death_driver_summary` | Visible reasons deaths rose, without exposing hidden formulas. |
| `visible_disruption` | The main disruption the player must manage now. |
| `primary_recovery_need` | The first recovery need that should guide decisions. |
| `risk_badges` | Follow-up risks that can appear as compact icons or text tags. |
| `cleanup_state` | Warning pending, impact pending, rescue active, stabilization active, reconstruction active, or closed. |
| `next_reassessment` | Dynamic date or countdown for the next impact, chain check, or recovery pulse. |
| `foreign_relief_state` | Current relief state when a foreign variant is active. |

## Family mini-specs

### Earthquake

| Design field | Direction |
| --- | --- |
| Family group | ground and seismic |
| Availability | baseline onward, with regional and rupture-adjacent forms in higher evolutions |
| Target fit | dense urban states, capitals, high infrastructure states, rail chokepoints, mountain and fault proxies, port states after offshore origin rolls |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_earthquake_rail_crews` | working label, not final localisation | railway crews, station staff, bridge tenders, trains, support equipment, short civilian capacity |
| `013_warn_earthquake_open_squares` | working label, not final localisation | civilians moved away from heavy masonry districts, manpower, trucks, stability strain |
| `013_warn_earthquake_port_withdrawal_watch` | working label, not final localisation | coastal or offshore seismic origins, convoys and naval access, reduces delayed tsunami losses |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `earthquake` |
| `family_group` | ground and seismic |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | collapsed structures, cracked roads, buckled rails |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | civilian factories, military factories, infrastructure, supply hubs, railways, forts in mountain or urban states |
| `death_driver_summary` | population density, urban proxy, infrastructure level, weak stability, previous devastation, night impact flag |
| `visible_disruption` | blocked rail access and shelter shortage |
| `primary_recovery_need` | search work, temporary shelter, bridge inspection, rail bracing |
| `risk_badges` | aftershock, landslide, port wave risk if coastal, urban fire |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

Capital and supply hub hits outrank ordinary rural hits. AI spends first on rescue and rail clearing when at war, then shelter and factory inspection. Offshore chain risk makes coastal evacuation outrank factory repair for one cycle.

#### Unique report direction

Use cracked streets, tilted buildings, broken bridges, cut rail, damaged workshops, and rescue work in the named state. Avoid generic casualty bulletin tone.

#### Unique news direction

Early news only when a city, port, capital, or major rail belt is hit. Regional and abnormal variants can mention aftershock sequences or coast withdrawal if visible.

#### State modifier direction

Reduce construction repair speed, supply flow, railway throughput, and factory output. Use short intense baseline, longer damaged-ground Evolution II, and severe rupture Evolution III.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `aftershock` | reduced repeat damage and panic refresh |
| `seismic_landslide` | mountain or hill proxy blocks supply |
| `offshore_tsunami` | coastal or island origin |
| `urban_fire` | dense factory state |


### Flood

| Design field | Direction |
| --- | --- |
| Family group | hydrological and river |
| Availability | baseline onward, regional river systems in Evolution II |
| Target fit | river states, lowland proxies, coastal floodplains, high infrastructure basins, dense agricultural and factory states, already storm hit states |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_flood_raise_embankments` | working label, not final localisation | infantry equipment, support equipment, civilian capacity, protects infrastructure and factories |
| `013_warn_flood_move_rolling_stock` | working label, not final localisation | trains and fuel, protects rail, supply, evacuation routes |
| `013_warn_flood_clean_water_stores` | working label, not final localisation | trucks, coastal convoys, medical capacity direction, reduces disease chain |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `flood` |
| `family_group` | hydrological and river |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | waterline marks, submerged depots, broken roads |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | infrastructure, railways, supply hubs, civilian factories, ports when coastal |
| `death_driver_summary` | low infrastructure, high population, poor supply, damaged rail, no warning, follow-up disease |
| `visible_disruption` | washed roads and contaminated water |
| `primary_recovery_need` | clean water, bridge repair, pumping, shelter and ration transport |
| `risk_badges` | disease, refugee pressure, crop loss, dam failure, wet landslide |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI treats floods as logistics threats. At war it prioritizes rail and supply hub recovery. At peace it prioritizes clean water and shelter. Disease risk makes water and medical decisions outrank factory repair.

#### Unique report direction

Show water behaviour, floating debris, damaged bridges, submerged tracks, and civilian movement to high ground. The place name must be specific.

#### Unique news direction

News for flash floods in dense states, regional river floods, capital floods, and flood chains after cyclones or surge. Routine small floods later stay report-only.

#### State modifier direction

Reduce supply, construction speed, local resources, and movement. Disease-risk variant adds recovery drag until clean water succeeds.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `waterborne_disease` | neglected clean water or high severity |
| `refugee_pressure` | adjacent safer connected states |
| `crop_loss` | agricultural proxy |
| `dam_failure_flash` | rare high-impact infrastructure follow-up |


### Tropical cyclone

| Design field | Direction |
| --- | --- |
| Family group | meteorological coastal storm |
| Availability | Evolution I onward, regional and multi-state in Evolution II |
| Target fit | coasts, islands, ports, dockyards, airfields, naval bases, coastal capitals, coastal supply corridors |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_tropical_cyclone_close_ports` | working label, not final localisation | convoys, fuel, naval access, protects ports, dockyards, ships |
| `013_warn_tropical_cyclone_dispersed_aircraft` | working label, not final localisation | fuel, trucks, air XP direction, protects airbases |
| `013_warn_tropical_cyclone_coastal_evacuation` | working label, not final localisation | manpower, trucks, stability strain, reduces surge and wind deaths |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `tropical_cyclone` |
| `family_group` | meteorological coastal storm |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | broken harbor works, roofs stripped from warehouses, airfields under water |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | ports, dockyards, airfields, infrastructure, coastal civilian factories, supply hubs |
| `death_driver_summary` | coastal population, storm surge chain, low infrastructure, no port closure, poor stability |
| `visible_disruption` | port closure, airfield damage, coastal rail breaks |
| `primary_recovery_need` | harbor clearance, runway repair, evacuation, fuel and food corridor |
| `risk_badges` | storm surge, inland flood, disease, refugee pressure |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI closes ports when dockyards or naval bases matter, disperses aircraft when airbase level is high, and evacuates dense states. Naval or island countries weight this family heavily.

#### Unique report direction

Use harbor wreckage, grounded vessels, torn hangars, flooded runways, and relief boats rather than broad weather phrasing.

#### Unique news direction

News for named coasts, islands, naval bases, or capital coastlines. Evolution II can describe one track crossing states, not every local hit.

#### State modifier direction

Reduce port throughput, dockyard output, airbase efficiency, and supply. Storm surge add-on extends coastal disruption.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `storm_surge` | coastal lowland or port |
| `inland_flood` | river neighbors |
| `disease` | shelter and water failure |
| `supply_collapse` | island or port-dependent country |


### Extreme wind event

| Design field | Direction |
| --- | --- |
| Family group | meteorological wind |
| Availability | baseline local form and Evolution I stronger form |
| Target fit | plains, exposed coasts, airfields, radar and anti-air states, light industry belts, open rail corridors |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_extreme_wind_anchor_aircraft` | working label, not final localisation | fuel, air XP, trucks, protects airfields |
| `013_warn_extreme_wind_secure_roofs` | working label, not final localisation | support equipment and civilian capacity, protects factories and infrastructure |
| `013_warn_extreme_wind_pause_exposed_trains` | working label, not final localisation | trains and temporary supply disruption, reduces rail damage |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `extreme_wind` |
| `family_group` | meteorological wind |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | stripped roofs, fallen poles, derailed cars, torn hangars |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | airfields, infrastructure, railways, anti-air, radar, light industry |
| `death_driver_summary` | exposed population, urban density, lack of shelter, rail accident chain |
| `visible_disruption` | transport interruptions and exposed depots |
| `primary_recovery_need` | roof repair, line clearing, aircraft recovery, depot cover |
| `risk_badges` | wildfire spread, rail accidents, shelter shortage |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI prioritizes aircraft and rail protection if those assets exist. At war, front supply routes come before factory repair.

#### Unique report direction

Show wind through objects and movement: roofs, hangars, telegraph poles, train cars, exposed depots. Avoid cyclone language unless chained.

#### Unique news direction

News only for severe capital damage, airfield disasters, major rail damage, or abnormal wind corridors.

#### State modifier direction

Hit airbase efficiency, local supply, repair speed, and movement. Short duration unless repeated by moving corridor.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `wildfire_spread` | forest or dry state |
| `rail_derailment` | rail state without train pause |
| `transport_collapse` | supply hub with war pressure |


### Tornado outbreak

| Design field | Direction |
| --- | --- |
| Family group | moving severe storm |
| Availability | rare Evolution II precursor and Evolution III abnormal path system |
| Target fit | plains, rail belts, open agricultural states, dense town lines, long corridors with factories or airfields |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_tornado_outbreak_spotter_line` | working label, not final localisation | command direction, trucks, local manpower, improves path forecast |
| `013_warn_tornado_outbreak_shelter_belt` | working label, not final localisation | support equipment and civilian capacity, reduces deaths in next-hit states |
| `013_warn_tornado_outbreak_clear_airfields` | working label, not final localisation | fuel and air XP, protects airbase and aircraft damage |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `tornado_outbreak` |
| `family_group` | moving severe storm |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | narrow destroyed corridors, splintered rail yards, scattered aircraft frames |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | railways, airfields, infrastructure, military factories, civilian factories along path |
| `death_driver_summary` | town density along path, low warning accuracy, no shelter belt, night impact |
| `visible_disruption` | path based destruction and rolling shelter demand |
| `primary_recovery_need` | corridor clearing, shelter belt, depot triage, rail reroute |
| `risk_badges` | moving path, wildfire, refugee pressure, severe thunderstorm renewal |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI reads the next-hit path. It protects capital and supply nodes first, then rail, then airfields. If resources are scarce, it evacuates the most populated upcoming state.

#### Unique report direction

Describe a damage corridor and named states. Focus on narrow destruction, missing trains, broken hangars, and towns cut into strips.

#### Unique news direction

Large outbreaks need news and GUI support. News mentions moving corridor and next threatened region by direction only.

#### State modifier direction

Narrow but severe repair penalties, rail disruption, supply interruption, and possible airbase outage.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `severe_thunderstorm_tail` | hail or flash flood |
| `wildfire_line` | dry or forest states |
| `refugee_pressure` | line of damaged towns |


### Thunderstorm

| Design field | Direction |
| --- | --- |
| Family group | local severe weather |
| Availability | baseline onward |
| Target fit | humid or river states, airfields, light infrastructure, forest edges, states with recent heat |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_thunderstorm_ground_aircraft` | working label, not final localisation | fuel, trucks, short air activity penalty, protects airbases |
| `013_warn_thunderstorm_lightning_patrol` | working label, not final localisation | manpower and support equipment, reduces fire chain |
| `013_warn_thunderstorm_drainage_crews` | working label, not final localisation | civilian capacity and trucks, reduces flash flood risk |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `thunderstorm` |
| `family_group` | local severe weather |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | lightning fires, flooded ditches, damaged runways, hail mixed into storm reports |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | airfields, infrastructure, local factories, supply hub minor damage |
| `death_driver_summary` | local exposure, airfield accidents, flash flood chain, fire chain |
| `visible_disruption` | sudden local interruptions and scattered damage |
| `primary_recovery_need` | runway clearing, patrols, drainage, temporary shelter |
| `risk_badges` | flash flood, hailstorm, wildfire ignition |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI usually uses the cheapest relevant warning. It should not overpay at low severity unless airfields, critical rail, or forest fire risk exist.

#### Unique report direction

Keep it local and sudden. Mention lightning, downed field lines, flash water, damaged planes, and short-lived chaos.

#### Unique news direction

Rare later news, limited to unusual lightning fires, capital airfield damage, or chain into flood or wildfire.

#### State modifier direction

Short duration low to medium disruption, stronger chain modifiers if flood, hail, or fire follows.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `hailstorm` | severe cell |
| `flash_flood` | river or lowland |
| `wildfire_ignition` | forest, heat, drought |


### Hailstorm

| Design field | Direction |
| --- | --- |
| Family group | severe weather and agricultural damage |
| Availability | baseline onward |
| Target fit | farmland proxy, airfields, light industry, exposed depots, livestock and crop regions |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_hailstorm_cover_aircraft` | working label, not final localisation | fuel, trucks, air XP, protects airfields |
| `013_warn_hailstorm_cover_depots` | working label, not final localisation | support equipment and temporary supply strain, protects stores |
| `013_warn_hailstorm_food_reserve` | working label, not final localisation | convoys or trains and civilian capacity, reduces crop loss |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `hailstorm` |
| `family_group` | severe weather and agricultural damage |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | shattered greenhouse glass, dented aircraft, ruined fields, exposed depots |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | airfields, infrastructure, local resources, civilian factories tied to agriculture proxy |
| `death_driver_summary` | exposed population, poor shelter, crop loss leading to famine pressure |
| `visible_disruption` | aircraft damage and food pressure |
| `primary_recovery_need` | airfield repair, depot covers, food transport, livestock recovery |
| `risk_badges` | crop failure, aircraft losses, ration pressure |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI prioritizes airfields in airbase states and food reserve in high population or drought-adjacent states. Low severity rural hits should not drain all resources.

#### Unique report direction

Make hail physical and local: damaged aircraft, broken roof glass, field loss, roads covered in ice. Avoid generic storm wording.

#### Unique news direction

News only for severe stones, large crop loss, important airbase damage, or early novelty. Later small hail is report-only.

#### State modifier direction

Reduce airbase efficiency, local supply, and food recovery values. Country famine pressure can appear after several agricultural hits.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `ration_pressure` | agricultural proxy |
| `airfield_accident` | airbase with no cover |
| `thunderstorm_return` | storm disruption remains |


### Blizzard

| Design field | Direction |
| --- | --- |
| Family group | winter storm |
| Availability | Evolution I onward, baseline only in cold special targeting if externally called |
| Target fit | cold regions, mountain passes, rail corridors, northern ports, supply hub states, fronts in winter |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_blizzard_fuel_corridor` | working label, not final localisation | fuel, trains, coastal convoys, reduces deaths and supply penalties |
| `013_warn_blizzard_rail_snow_crews` | working label, not final localisation | manpower, support equipment, trains, protects rail |
| `013_warn_blizzard_winter_shelter` | working label, not final localisation | support equipment and civilian capacity, reduces civilian deaths |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `blizzard` |
| `family_group` | winter storm |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | blocked passes, snowed railheads, frozen depots, closed ports |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | infrastructure, railways, supply hubs, ports in cold coast states, factories through outage |
| `death_driver_summary` | low supply, fuel shortage, poor infrastructure, war zone, cold wave chain |
| `visible_disruption` | supply freeze and transport paralysis |
| `primary_recovery_need` | fuel corridor, rail clearing, winter shelter, depot warming |
| `risk_badges` | cold wave, supply collapse, refugee exposure |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

At war, AI treats blizzard as a front supply threat and clears rail first. At peace, shelter and fuel corridor are favored.

#### Unique report direction

Focus on blocked passes, frozen rail yards, closed harbors, fuel lines, and civilians trapped by snow.

#### Unique news direction

News for major rail or port shutdown, capital isolation, or chained cold wave. Small regional blizzards remain reports.

#### State modifier direction

Reduce supply, movement, repair speed, port throughput, and local factory output. Cold exposure variant can continue deaths until shelter succeeds.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `extreme_cold_wave` | temperature pressure continues |
| `supply_collapse` | rail or hub failure |
| `refugee_exposure` | shelter failure |


### Extreme cold wave

| Design field | Direction |
| --- | --- |
| Family group | extreme temperature |
| Availability | baseline local in cold regions, wider in Evolution I and II |
| Target fit | cold regions, high population states, low infrastructure, states already hit by blizzard, fronts with supply shortage |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_extreme_cold_wave_heat_shelters` | working label, not final localisation | fuel, support equipment, civilian capacity, reduces deaths |
| `013_warn_extreme_cold_wave_protect_water_lines` | working label, not final localisation | manpower and infrastructure repair capacity, reduces local disruption |
| `013_warn_extreme_cold_wave_frontline_rotation` | working label, not final localisation | command direction, army XP, supply, reduces exposure near fronts |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `extreme_cold_wave` |
| `family_group` | extreme temperature |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | frozen pipes, fuel queues, closed roads, hospitals under heating strain |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | infrastructure, local supply, factories through power and fuel loss |
| `death_driver_summary` | population density, low fuel, low infrastructure, blizzard or supply collapse, war zone |
| `visible_disruption` | heating and water failure |
| `primary_recovery_need` | fuel, shelter, water line repair, ration transport |
| `risk_badges` | blizzard renewal, supply collapse, disease from shelter crowding |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI uses shelter and fuel decisions first in dense states. War states may use frontline rotation if active combat or border pressure exists.

#### Unique report direction

Show cold through infrastructure and civilians: fuel corridors, frozen pipes, closed roads, overcrowded shelters.

#### Unique news direction

News only for severe multi-country cold, capitals, or chain after blizzards. Ordinary local cold stays report-only.

#### State modifier direction

Reduce local supply, factory output, repair speed, and population recovery. Can add gradual deaths if ignored.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `blizzard_followup` | pattern deepens |
| `shelter_disease` | crowded shelters |
| `supply_collapse` | fuel or rail failure |


### Extreme heat wave

| Design field | Direction |
| --- | --- |
| Family group | extreme temperature |
| Availability | baseline local in hot regions, wider in Evolution I and II, gated away from active Event 051 Heat Wave stacking |
| Target fit | hot or dry states, dense cities, low infrastructure, drought states, wildfire risk states, desert supply corridors |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_extreme_heat_wave_water_points` | working label, not final localisation | trucks, convoys or trains, civilian capacity, reduces deaths and drought risk |
| `013_warn_extreme_heat_wave_shift_work_hours` | working label, not final localisation | temporary factory output loss, reduces death and stability pressure |
| `013_warn_extreme_heat_wave_fire_watch` | working label, not final localisation | manpower and support equipment, reduces wildfire chain |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `extreme_heat_wave` |
| `family_group` | extreme temperature |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | empty water carts, overheated factories, stalled trains, fire watches on dry roads |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | infrastructure, factories through heat shutdown, supply hubs, local resources in dry regions |
| `death_driver_summary` | dense population, poor infrastructure, drought, weak stability, no water points, war supply strain |
| `visible_disruption` | water shortage and productivity collapse |
| `primary_recovery_need` | water points, cooling shelters, fire watches, altered work schedule |
| `risk_badges` | wildfire, drought, disease, unrest |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI must check Event 051 and avoid stacking. If separate heat is active, bridge or skip. Dense states prioritize water and shelter. Forest or dry states prioritize fire watch.

#### Unique report direction

Distinguish from Event 051 by focusing on a specific place, local heat deaths, work disruption, water lines, and fire risk.

#### Unique news direction

News for severe dense-state heat, heat linked to wildfire, or widespread Evolution II pulses. Smaller heat is report-only later.

#### State modifier direction

Reduce output, supply, population recovery, and movement. Include anti-stack tag for Event 051 compatibility.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `wildfire` | dry or forest state |
| `drought` | prolonged heat |
| `unrest` | water stress and weak stability |


### Drought

| Design field | Direction |
| --- | --- |
| Family group | climatological dryness |
| Availability | Evolution I onward, stronger regional behavior in Evolution II |
| Target fit | dry regions, agricultural proxy states, high population food belts, river states with low recovery, states after heat wave |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_drought_water_trains` | working label, not final localisation | trains, fuel, civilian capacity, reduces deaths and food pressure |
| `013_warn_drought_crop_salvage` | working label, not final localisation | manpower, trucks, stability strain, reduces famine chain |
| `013_warn_drought_firebreaks` | working label, not final localisation | infantry equipment, support equipment, manpower, reduces wildfire risk |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `drought` |
| `family_group` | climatological dryness |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | dry wells, cracked fields, idle mills, guarded water trains |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | local resources, infrastructure, factories through water shortage, supply hubs through ration pressure |
| `death_driver_summary` | duration, population density, crop proxy, low imports, war disruption, famine chain |
| `visible_disruption` | food pressure and water transport strain |
| `primary_recovery_need` | water trains, crop salvage, ration imports, firebreaks |
| `risk_badges` | famine, wildfire, refugee pressure, heat renewal |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI favors water trains when rail exists and ration imports when port or convoy access exists. It does not treat drought as solved after one click if duration remains high.

#### Unique report direction

Slow and material: wells, livestock loss, ration lines, idled mills, guarded transport. Avoid one-day storm tone.

#### Unique news direction

Sparse news. Use only for large regional drought, famine chain, strategic agricultural belt, or drought feeding major wildfire.

#### State modifier direction

Long duration output loss, resource loss, supply strain, and stability pressure. Removable only after water and food work mature.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `famine_pressure` | failed crop salvage |
| `wildfire` | dry forest or wind |
| `refugee_pressure` | long duration and low recovery |


### Sandstorm and dust storm

| Design field | Direction |
| --- | --- |
| Family group | dust and visibility |
| Availability | Evolution I onward, with Event 099 as placeholder or bridge only |
| Target fit | desert, dry plains, drought states, supply corridors, airfields, military front states, oil or resource states |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_sandstorm_dust_convoy_spacing` | working label, not final localisation | trucks, fuel, command direction, reduces supply and movement disruption |
| `013_warn_sandstorm_dust_seal_airfields` | working label, not final localisation | support equipment and air XP, protects airfields and aircraft |
| `013_warn_sandstorm_dust_cover_water_stores` | working label, not final localisation | manpower and support equipment, reduces disease and water pressure |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `sandstorm_dust` |
| `family_group` | dust and visibility |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | dust-darkened roads, stalled convoys, fouled airfields, covered water stores |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | airfields, infrastructure, supply hubs, resources, radar and anti-air visibility support |
| `death_driver_summary` | low water, poor shelter, front supply strain, drought chain, disease pressure |
| `visible_disruption` | visibility collapse and contaminated stores |
| `primary_recovery_need` | airfield clearing, convoy spacing, water protection, engine repair |
| `risk_badges` | drought, disease, supply collapse, heat renewal |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI prioritizes supply corridors and airfields. Desert-front AI spends more on convoy spacing. Civilian-only desert hits use water store cover first.

#### Unique report direction

Use dust on vehicles, dark skies, clogged engines, and water contamination. Do not preserve old Event 099 text structure.

#### Unique news direction

News for large dust walls, major front disruption, capital blackout, or abnormal regional dust. Event 099 should not generate separate standalone news if bridged.

#### State modifier direction

Reduce supply, movement, recon, airbase efficiency, and resource extraction. Temporary combat visibility penalties where supported.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `drought` | repeated dust |
| `disease` | water contamination |
| `heat_wave` | only if Event 051 compatibility permits |


### Wildfire

| Design field | Direction |
| --- | --- |
| Family group | fire and smoke |
| Availability | baseline onward, regional fire seasons in Evolution II |
| Target fit | forest proxy, dry states, heat or drought states, wind states, resource and infrastructure belts, low response states |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_wildfire_firebreaks` | working label, not final localisation | manpower, infantry equipment, support equipment, reduces spread and building damage |
| `013_warn_wildfire_evacuation_columns` | working label, not final localisation | trucks, fuel, stability strain, reduces deaths and refugee shock |
| `013_warn_wildfire_protect_power_lines` | working label, not final localisation | civilian capacity and support equipment, reduces factory and infrastructure outages |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `wildfire` |
| `family_group` | fire and smoke |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | red night skies, burned rail sleepers, smoke over factories, evacuated roads |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | infrastructure, civilian factories, military factories, resources, railways, airfields through smoke |
| `death_driver_summary` | forest density proxy, wind, heat, drought, no evacuation, poor infrastructure |
| `visible_disruption` | fire spread and smoke disruption |
| `primary_recovery_need` | firebreaks, evacuation, line repair, smoke medical work |
| `risk_badges` | smoke illness, refugee pressure, drought renewal, wind spread |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI prioritizes firebreaks if neighbors are at risk. Dense or capital fires prioritize evacuation. Industrial states protect power lines after rescue.

#### Unique report direction

Show fire light, smoke, rail sleepers, forests, farms, and workers moving equipment from the path. Avoid generic wording.

#### Unique news direction

News for large fires, capital smoke, multi-state spread, or wildfire after drought and wind. Small starts stay local.

#### State modifier direction

Damage buildings, reduce supply, movement or attrition where sensible, and apply smoke disruption to airbase or output.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `smoke_illness` | dense or low medical recovery |
| `refugee_pressure` | evacuation columns |
| `drought_feedback` | water pressure worsens |


### Dry mass movement

| Design field | Direction |
| --- | --- |
| Family group | landslide and slope failure |
| Availability | baseline small form, Evolution I wider |
| Target fit | mountains, hills, dry slopes, rail cuts, road passes, mines, infrastructure chokepoints, earthquake or drought states |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_dry_mass_movement_slope_watch` | working label, not final localisation | manpower and support equipment, reduces deaths and road damage |
| `013_warn_dry_mass_movement_pass_closure` | working label, not final localisation | command direction and temporary supply penalty, protects rail and roads |
| `013_warn_dry_mass_movement_mine_evacuation` | working label, not final localisation | resource proxy, trucks and civilian capacity, reduces deaths and resource outage |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `dry_mass_movement` |
| `family_group` | landslide and slope failure |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | dust clouds on slopes, blocked passes, buried sidings, damaged mines |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | infrastructure, railways, resources, supply hubs in mountain states |
| `death_driver_summary` | mountain population, rail and mine workers, no pass closure, earthquake or drought precursor |
| `visible_disruption` | blocked passes and mine closure |
| `primary_recovery_need` | slope clearing, pass reopening, mine rescue, temporary route diversion |
| `risk_badges` | aftershock, supply isolation, resource outage |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI values pass closure if the state feeds a front. Resource states trigger mine evacuation. Low-value rural slopes wait behind higher priority disasters.

#### Unique report direction

Focus on slopes, passes, sidings, mines, and dust. Do not sound wet or flood-like.

#### Unique news direction

News only for strategic passes, rail isolation, major mine disasters, or earthquake chains.

#### State modifier direction

Hit infrastructure, rail, resource extraction, and supply movement. Duration depends on clearing mission success.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `supply_isolation` | pass or rail chokepoint |
| `aftershock_damage` | earthquake chain |
| `resource_shutdown` | mine proxy |


### Wet mass movement

| Design field | Direction |
| --- | --- |
| Family group | landslide and mud movement |
| Availability | Evolution I onward, common as flood or storm chain |
| Target fit | mountains, hills, wet regions, river valleys, rain-heavy states, earthquake or flood states, rail cuts |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_wet_mass_movement_valley_evacuation` | working label, not final localisation | trucks and manpower, reduces deaths in valley states |
| `013_warn_wet_mass_movement_bridge_watch` | working label, not final localisation | support equipment and civilian capacity, reduces bridge and rail damage |
| `013_warn_wet_mass_movement_channel_clearance` | working label, not final localisation | manpower and equipment, reduces flood renewal and lahar-adjacent chains |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `wet_mass_movement` |
| `family_group` | landslide and mud movement |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | mud-choked valleys, torn bridges, buried road bends, flooded sidings |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | infrastructure, railways, supply hubs, resources, civilian factories in valleys |
| `death_driver_summary` | valley population, flood precursor, weak warning, low infrastructure, night flag |
| `visible_disruption` | blocked valleys and bridge loss |
| `primary_recovery_need` | valley evacuation, channel clearing, bridge repair, road clearing |
| `risk_badges` | flood renewal, disease, supply isolation |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI prioritizes bridge watch if rail or supply hubs exist, valley evacuation in dense mountain states, and channel clearance when flood risk remains active.

#### Unique report direction

Emphasize mud, valleys, bridges, and sudden road burial. It must read wetter and heavier than dry slope failure.

#### Unique news direction

News for deadly valley disasters, flood chains, and strategic rail cuts. Routine landslides later stay reports.

#### State modifier direction

Reduce infrastructure, supply, and movement. Wet variant increases disease or water contamination chain chance if ignored.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `flood_renewal` | blocked channels |
| `disease` | mud and contaminated water |
| `supply_isolation` | bridge or rail loss |


### Volcanic eruption

| Design field | Direction |
| --- | --- |
| Family group | volcanic activity |
| Availability | Evolution I rare signal, Evolution II serious regional, Evolution III massive crisis route |
| Target fit | volcanic arcs, island chains, mountain volcanic proxies, dense states near volcanic regions, airfield and port states |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_volcanic_eruption_observatory_watch` | working label, not final localisation | civilian capacity, research investment direction, support equipment, improves warning |
| `013_warn_volcanic_eruption_exclusion_zone` | working label, not final localisation | stability strain, manpower, trucks, reduces deaths around vent |
| `013_warn_volcanic_eruption_ash_airfield_closure` | working label, not final localisation | air XP and temporary airbase loss, reduces airfield damage |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `volcanic_eruption` |
| `family_group` | volcanic activity |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | ash plume, blocked roads, hot deposits, evacuated slopes, closed airfields |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | infrastructure, airfields, civilian factories, resources, ports if coastal, supply hubs |
| `death_driver_summary` | vent proximity, population density, no exclusion zone, lahar or ash chain, weak recovery |
| `visible_disruption` | ash, evacuation, airfield closure, road and port contamination |
| `primary_recovery_need` | exclusion zone, ash clearing, slope evacuation, airfield closure, food corridor |
| `risk_badges` | ashfall, lahar, tsunami if coastal collapse, famine, disease |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI invests in observatory warning if volcanic risk recurs. During active eruption, exclusion zone comes before ash cleanup when population is high. Air powers close airfields.

#### Unique report direction

Visual and local: ash plume, slope evacuation, blackened fields, closed airfields, movement away from rivers and valleys.

#### Unique news direction

News for known volcanic region, dense island, capital, or air route. Massive crisis uses super-event handoff.

#### State modifier direction

Reduce airbase efficiency, local output, infrastructure, supply, and resources. Add long ash cleanup until late recovery succeeds.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `ashfall` | downwind states |
| `lahar` | river valleys |
| `tsunami` | island collapse or coast |
| `famine_pressure` | ash over crops and closed ports |


### Ashfall

| Design field | Direction |
| --- | --- |
| Family group | volcanic air and surface contamination |
| Availability | Evolution II onward as volcanic chain, Evolution III regional plume |
| Target fit | downwind from volcanic origin, airfields, crop proxy states, ports, dense cities, states with exposed machinery |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_ashfall_ground_air_traffic` | working label, not final localisation | air XP, fuel, temporary airbase shutdown, protects aircraft |
| `013_warn_ashfall_cover_machinery` | working label, not final localisation | support equipment and civilian capacity, protects factories and resources |
| `013_warn_ashfall_food_and_water_cover` | working label, not final localisation | manpower, trucks, convoys or trains, reduces food and disease pressure |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `ashfall` |
| `family_group` | volcanic air and surface contamination |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | gray roofs, fouled engines, quiet runways, ash-covered fields |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | airfields, infrastructure, factories, resources, supply hubs, crop proxy |
| `death_driver_summary` | ash thickness, dense population, poor water cover, disease chain, eruption severity |
| `visible_disruption` | air shutdown and machinery contamination |
| `primary_recovery_need` | runway clearing, machinery cover, water cover, ash removal |
| `risk_badges` | respiratory deaths, famine, transport closure, lahar if rain arrives |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI closes airfields if airbase value exists. Industrial states cover machinery. Agricultural or dense states cover food and water.

#### Unique report direction

Focus on ash on roofs, rail, airfields, water, and machines. Do not write it as smoke or ordinary fog.

#### Unique news direction

News for large plumes, capital ashfall, flight collapse, or food disruption across regions. Small ash drift remains a report.

#### State modifier direction

Reduce airbase efficiency, output, local supply, and resource extraction. Longer if cleanup fails or eruption remains active.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `respiratory_deaths` | dense state |
| `famine_pressure` | crop proxy |
| `lahar` | rain on ash-heavy slopes |


### Lahar and volcanic mudflow

| Design field | Direction |
| --- | --- |
| Family group | volcanic water and mud |
| Availability | Evolution II onward as volcanic follow-up, Evolution III severe regional chain |
| Target fit | river valleys below volcano proxy, wet volcanic slopes, settlement valleys, rail and bridge corridors |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_lahar_valley_sirens` | working label, not final localisation | support equipment and manpower, reduces deaths |
| `013_warn_lahar_bridge_cordon` | working label, not final localisation | command direction and temporary rail or road disruption, reduces bridge collapse |
| `013_warn_lahar_channel_clearance` | working label, not final localisation | manpower and civilian capacity, reduces repeat flow and flood chain |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `lahar` |
| `family_group` | volcanic water and mud |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | hot mud in river valleys, broken bridges, buried villages, blocked culverts |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | infrastructure, railways, supply hubs, bridges, population in valleys |
| `death_driver_summary` | valley density, warning failure, eruption severity, rain or snow melt, weak bridge cordon |
| `visible_disruption` | valley burial and river blockage |
| `primary_recovery_need` | valley sirens, bridge cordon, channel clearing, medical response |
| `risk_badges` | flood, disease, supply isolation, renewed volcanic flow |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI evacuates valleys first, then protects bridge corridors if they feed supply. It should not repair factories before clearing lahar channels.

#### Unique report direction

Tie it to volcanic ash, hot mud, river valleys, and eruption aftermath. Distinguish from ordinary landslide.

#### Unique news direction

News for deadly volcanic valley flows, strategic bridge destruction, or chains after major eruptions. Small local flows are report-only.

#### State modifier direction

Severely reduce infrastructure and supply, with lingering river blockage until cleanup succeeds.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `flood` | blocked rivers |
| `disease` | contaminated water |
| `supply_isolation` | bridge and rail losses |


### Tsunami

| Design field | Direction |
| --- | --- |
| Family group | coastal wave |
| Availability | Evolution II onward, major abnormal chains in Evolution III |
| Target fit | coastal states, islands, ports, dockyards, coastal capitals, offshore earthquake or ocean impact origin |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_tsunami_coast_withdrawal_alarm` | working label, not final localisation | manpower, convoys, coast watch direction, reduces deaths |
| `013_warn_tsunami_close_quays` | working label, not final localisation | port closure, convoys, fuel, reduces port and dockyard damage |
| `013_warn_tsunami_inland_corridors` | working label, not final localisation | trucks and stability strain, reduces refugee and death pressure |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `tsunami` |
| `family_group` | coastal wave |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | withdrawn harbors, wrecked quays, boats inland, silent coastal roads |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | ports, dockyards, infrastructure, coastal factories, naval bases, supply hubs |
| `death_driver_summary` | coastal population, warning delay, port density, low infrastructure, origin severity |
| `visible_disruption` | coastal access loss and port destruction |
| `primary_recovery_need` | evacuation, quay closure, medical corridor, port salvage, water cleanup |
| `risk_badges` | disease, refugee pressure, naval disruption, coastal famine |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI evacuates dense coasts first and closes quays if ports or dockyards matter. Island AI prioritizes inland corridors and port salvage.

#### Unique report direction

Focus on coast behaviour, wave origin if known, silent harbors, inland boats, damaged quays, and missing port workers. Avoid generic flood language.

#### Unique news direction

Meaningful news, but throttle repeats in global chains. Delayed news may reference origin by direction only.

#### State modifier direction

Severely reduce port throughput, dockyard output, infrastructure, supply, and population recovery. Disease or water cleanup can persist.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `disease` | contaminated water |
| `refugee_pressure` | inland movement |
| `naval_disruption` | closed ports |
| `coastal_famine` | islands |


### Storm surge

| Design field | Direction |
| --- | --- |
| Family group | coastal storm water |
| Availability | Evolution I onward with cyclones and severe coastal storms |
| Target fit | coastal lowlands, ports, dockyards, cyclone path states, island states, river mouths |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_storm_surge_quay_closure` | working label, not final localisation | convoys, fuel, temporary port throughput loss, reduces port damage |
| `013_warn_storm_surge_sandbag_low_roads` | working label, not final localisation | infantry equipment, support equipment, manpower, reduces infrastructure damage |
| `013_warn_storm_surge_evacuate_marsh_edge` | working label, not final localisation | trucks and stability strain, reduces deaths |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `storm_surge` |
| `family_group` | coastal storm water |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | water through quays, marsh roads gone, warehouses flooded, coastal rail under debris |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | ports, dockyards, infrastructure, coastal railways, supply hubs, local factories |
| `death_driver_summary` | low coast density, cyclone severity, weak evacuation, port concentration |
| `visible_disruption` | coastal flood and port downtime |
| `primary_recovery_need` | quay closure, road sandbagging, marsh evacuation, pump and debris cleanup |
| `risk_badges` | flood, disease, port closure, refugee pressure |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI uses quay closure for ports and evacuates dense low coasts. It understands surge as cyclone-linked and does not duplicate tsunami response unless tsunami is active.

#### Unique report direction

Tie water to storm winds, tide, harbors, and low roads. Distinct from tsunami by cause and timing.

#### Unique news direction

News when surge damages major ports, islands, capital coasts, or follows a cyclone track direction. Otherwise affected report only.

#### State modifier direction

Reduce port throughput, infrastructure, supply, and repair speed, shorter than tsunami unless chained into flood.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `flood` | water remains inland |
| `disease` | contaminated shelter water |
| `port_supply_collapse` | islands |


### Meteor impact

| Design field | Direction |
| --- | --- |
| Family group | extra-terrestrial impact |
| Availability | Evolution III abnormal |
| Target fit | random land or ocean target with scenario bias, high visibility states for major impact, ocean if tsunami chain desired |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_meteor_impact_observatory_tracking` | working label, not final localisation | research investment direction and civilian capacity, improves forecast |
| `013_warn_meteor_impact_crater_evacuation` | working label, not final localisation | trucks, fuel, stability strain, only with target confidence |
| `013_warn_meteor_impact_fire_perimeter` | working label, not final localisation | manpower, support equipment, infantry equipment, reduces blast fire chain |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `meteor_impact` |
| `family_group` | extra-terrestrial impact |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | crater, blast ring, burning outskirts, broken rail lines, strange fragments |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | all buildings near primary state, infrastructure, airfields, ports if coastal, rail, factories, supply hubs |
| `death_driver_summary` | direct impact severity, population density, evacuation success, night flag, ocean impact tsunami chain |
| `visible_disruption` | crater exclusion, blast damage, fire spread, panic movement |
| `primary_recovery_need` | evacuation, fire perimeter, medical triage, crater cordon, rail restoration |
| `risk_badges` | wildfire, dust, tsunami if ocean, refugee pressure, fragment shower |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI spends heavily when forecast confidence identifies a dense state or capital. If confidence is low, broad fire perimeter appears only when affordable.

#### Unique report direction

Present the impossible object through traces, not exposition: crater, flash, fires, rail breaks, fragments. Keep final quotes blocked.

#### Unique news direction

Major impact always gets meaningful news and may get super-event treatment. Minor fragments can be one abnormal chain without spam.

#### State modifier direction

Severe crater devastation, long repair penalties, possible local exclusion, fire or dust add-ons.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `wildfire` | dry land impact |
| `dust_veil` | high severity |
| `tsunami` | ocean impact |
| `meteor_shower` | fragment field |


### Meteor shower and skyfire hail

| Design field | Direction |
| --- | --- |
| Family group | extra-terrestrial multi-impact |
| Availability | Evolution III abnormal |
| Target fit | multi-state clusters, visible night path, airfields, rail corridors, dry states, high-value industry states |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_meteor_shower_observer_net` | working label, not final localisation | civilian capacity and local manpower, improves forecast cards |
| `013_warn_meteor_shower_shelter_lights_out` | working label, not final localisation | stability strain and manpower, reduces deaths across states |
| `013_warn_meteor_shower_fire_patrols` | working label, not final localisation | support equipment and trucks, reduces wildfire chain |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `meteor_shower` |
| `family_group` | extra-terrestrial multi-impact |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | many small craters, roof fires, airfield sparks, night sightings across states |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | airfields, infrastructure, factories, railways, supply hubs, population across clustered states |
| `death_driver_summary` | number of states, fragment density, shelter success, fire chains, urban density |
| `visible_disruption` | wide scattered impact and fire starts |
| `primary_recovery_need` | shelters, fire patrols, fragment triage, rail inspection, airfield checks |
| `risk_badges` | wildfire, transport collapse, panic, crater contamination direction |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI prioritizes clustered states with capitals, airfields, or supply hubs. It should save capacity for chain fires rather than overcommit to low-value fragments.

#### Unique report direction

Carry multiple places under one Event 013 season. Mention night sightings, small craters, roof fires, and rail inspections as direction only.

#### Unique news direction

One meaningful news event for the cluster and reports for affected countries. Avoid news per fragment.

#### State modifier direction

Medium to severe scattered modifier, careful stacking with fire and transport collapse, no infinite fragment loops.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `wildfire` | dry states |
| `transport_collapse` | rail and airfield checks fail |
| `meteor_impact` | rare larger fragment |


### Whole-earth rupture wave

| Design field | Direction |
| --- | --- |
| Family group | abnormal global seismic |
| Availability | Evolution III only, replaces the old Earth Earthquake concept without reusing its logic |
| Target fit | global or continental pass with regional anchors, dense belts, ports, mountains, rail arteries, capitals, already damaged states |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_whole_earth_rupture_global_rail_standdown` | working label, not final localisation | trains, fuel, major temporary supply penalty, reduces rail damage |
| `013_warn_whole_earth_rupture_coastal_tide_watch` | working label, not final localisation | convoys and coast watch direction, reduces delayed tsunami deaths |
| `013_warn_whole_earth_rupture_regional_triage` | working label, not final localisation | civilian capacity, trucks, manpower, stability strain, reduces deaths in priority regions |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `whole_earth_rupture` |
| `family_group` | abnormal global seismic |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | several regions shaking in waves, broken rail arteries, damaged ports, repeated aftershock reports |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | railways, infrastructure, ports, supply hubs, factories, airfields, population across many states |
| `death_driver_summary` | global severity, density, existing devastation, poor recovery, coastal tsunami chain, aftershock count |
| `visible_disruption` | multi-region infrastructure failure and delayed chains |
| `primary_recovery_need` | regional triage, rail standdown, coastal watch, aftershock rescue, port closure |
| `risk_badges` | aftershock, tsunami, landslide, urban fire, regional supply collapse |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI uses the GUI priority queue or hidden equivalent. It cannot solve all states. It prioritizes capital, supply hub, ports, and highest population. At war, rail standdown outranks all but tsunami warning.

#### Unique report direction

Local reports per country but connected to the same rupture season. Show rupture traces and delayed aftershocks. Never claim Event 046 logic returned.

#### Unique news direction

Super-event candidate with throttled global news and delayed reports. Do not spam news per state.

#### State modifier direction

Severe regional rupture damage, rail artery breakage, port disruption, and lingering aftershock risk.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `global_aftershocks` | several delayed impacts |
| `delayed_tsunami_chain` | coasts |
| `regional_landslides` | mountains |
| `urban_fire` | dense industry |


### Massive eruption crisis

| Design field | Direction |
| --- | --- |
| Family group | abnormal volcanic crisis |
| Availability | Evolution III only |
| Target fit | major volcanic arc, island chain, densely populated volcanic region, coastal volcanic collapse area, air and port network states |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_massive_eruption_exclusion_ring` | working label, not final localisation | major civilian capacity, trucks, manpower, stability strain, reduces deaths near vent and valleys |
| `013_warn_massive_eruption_air_shutdown` | working label, not final localisation | air XP, fuel, temporary air activity loss, protects airbases |
| `013_warn_massive_eruption_food_corridors` | working label, not final localisation | convoys, trains, fuel, civilian capacity, reduces famine pressure |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `massive_eruption` |
| `family_group` | abnormal volcanic crisis |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | towering ash plume, buried slopes, closed sky routes, darkened fields, lahars in valleys |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | airfields, infrastructure, ports, factories, resources, supply hubs, regional population |
| `death_driver_summary` | vent proximity, lahar risk, ash thickness, island dependency, famine chain, evacuation success |
| `visible_disruption` | regional ash, valley flows, air shutdown, port and food stress |
| `primary_recovery_need` | exclusion ring, ash clearing, valley evacuation, food corridors, air and port reroute |
| `risk_badges` | ashfall, lahar, tsunami, famine, disease, long air disruption |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI treats this as multi-cycle. It must not spend all capacity on the first state if ash plume and lahar cards remain. It protects food corridors early.

#### Unique report direction

Combine local volcanic damage with ash and valley consequences. Use concrete effects on slopes, rivers, airfields, ports, and food transport.

#### Unique news direction

Super-event candidate with one global news direction and many delayed local reports. Quote, title, remark, and audio are research-gated.

#### State modifier direction

Long, severe, multi-layered modifiers. Separate ash, vent, lahar, port, and food pressure can be peeled away by recovery missions.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `regional_ashfall` | downwind states |
| `lahar` | valleys |
| `tsunami` | coastal collapse |
| `famine_pressure` | ash and closed ports |


### Moving storm corridor

| Design field | Direction |
| --- | --- |
| Family group | abnormal moving weather corridor |
| Availability | Evolution III only |
| Target fit | long path across multiple states, rail belts, coastal-to-inland routes, plains, airfields, dry forests, dense corridors |

#### Warning and preparation decisions

| Working decision key | Status | Family-specific purpose and cost direction |
| --- | --- | --- |
| `013_warn_moving_storm_corridor_path_forecast` | working label, not final localisation | civilian capacity, local observers, command direction, improves next-hit cards |
| `013_warn_moving_storm_corridor_rail_reroute` | working label, not final localisation | trains, fuel, temporary supply loss, reduces rail and supply damage |
| `013_warn_moving_storm_corridor_layered_evacuation` | working label, not final localisation | trucks, manpower, stability strain, reduces deaths in next-hit states |

#### Exact aftermath card fields

| Card field | Family-specific value direction |
| --- | --- |
| `family_key` | `moving_storm_corridor` |
| `family_group` | abnormal moving weather corridor |
| `primary_state` | Main affected state, with linked states displayed only when the family uses a path, coast, plume, or regional chain. |
| `impact_signature` | forecast path, rolling damage corridor, rail reroutes, repeated storm cores, changing next-hit cards |
| `severity_band` | local, severe, regional, abnormal, or barrage according to the caller and evolution. |
| `primary_damage_profile` | infrastructure, railways, supply hubs, airfields, factories, ports if coastal segment, population |
| `death_driver_summary` | path accuracy, state density, warning lead time, rail reroute success, repeated hits, chain fires or floods |
| `visible_disruption` | moving path and repeated next-state pressure |
| `primary_recovery_need` | path forecast, layered evacuation, rail reroute, airfield dispersal, corridor cleanup |
| `risk_badges` | flood, tornado, wildfire, storm surge, refugee pressure |
| `cleanup_state` | warning pending, impact pending, rescue active, stabilization active, reconstruction active, closed. |
| `next_reassessment` | dynamic date from severity, recovery score, and active mission cap. |
| `foreign_relief_state` | none, requested, convoy pledged, delayed, arrived, misdirected, refused, converted to dependency risk. |

#### AI priorities

AI uses scripted GUI path queue or non-GUI equivalent. It protects next capital or supply state first, then rail, then airfields. It ignores safe states while the path remains active.

#### Unique report direction

Describe a moving corridor and named states it has crossed or threatens. Avoid single-state wording while active.

#### Unique news direction

One meaningful news event for corridor reveal and later only major path changes. Country reports handle each affected state.

#### State modifier direction

Apply path damage, lingering debris, and temporary corridor fear. Clear state by state through recovery missions.

#### Follow-up chain routes

| Chain route | Route direction |
| --- | --- |
| `tornado_outbreak` | plains segment |
| `flood` | rain and river state |
| `wildfire` | dry lightning |
| `storm_surge` | coastal segment |

