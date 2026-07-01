# Event 013 Natural Disasters Spec, Part 2, Disaster Families

This part defines the individual disaster families. The labels are working labels for design and implementation routing. They are not final localisation keys or final event titles.

Each family should have a family profile with target eligibility, state damage, deaths profile, aftermath modifier, recovery decisions, follow-up chances, AI recovery priority, and news threshold. The implementation should avoid one generic damage effect for every family.

## Family profile schema

Every family profile should define these fields in a central tuning table or documentation-backed constants group.

| Field | Design meaning |
| --- | --- |
| family id | Stable internal id, such as `earthquake`, `flood`, or `wildfire` |
| hazard group | Geophysical, hydrological, meteorological, climatological, or extra-terrestrial |
| preferred target | State, coast, river, mountain, desert, basin, country, region, world, or corridor |
| fallback target | Safe fallback if preferred pool is empty |
| baseline damage | Buildings and population effects for ordinary firing |
| evolved damage | Stronger effects unlocked by evolutions |
| abnormal access | Whether Evolution III can create an abnormal version |
| follow-up families | Possible chained disasters |
| recovery type | Which decision and mission families open |
| news threshold | When a report, digest, or super-event can appear |
| AI urgency | How strongly AI should prioritize recovery |

## Earthquake family

Earthquakes are fast geophysical shocks. They should target fault-like regions, plate-boundary approximations, mountain belts, urban high-infrastructure states, and regions with known seismic identity. Implementation can use scripted state groups for major seismic zones and fallback to mountain, coastal, and high-building states when exact hazard mapping is not available.

Immediate effects:

- Heavy damage to infrastructure, civilian factories, military factories, railways, supply hubs, forts, urban state buildings, and state-level logistics.
- Population loss scaled by state population, building density, infrastructure, stability, and preparedness.
- Temporary supply penalties and movement penalties.
- Possible damage to airbases and radar.
- Capital-hit stability shock.

Follow-ups:

- Aftershock pulse after several days.
- Tsunami if coastal or offshore logic selects a nearby coast.
- Wet or dry mass movement in mountain states.
- Infrastructure collapse mission if railways or supply hubs are damaged.
- Refugee pressure if death or building damage crosses a threshold.

Recovery play:

- Emergency rescue teams consume support equipment, manpower, trucks, and command power.
- Clear collapsed rail corridors requires trains, support equipment, civilian factory burden, and named rail or hub control.
- Stabilize damaged cities can reduce delayed deaths and lower public panic.

Evolution notes:

- Evolution II earthquakes can hit neighboring states and leave wider supply penalties.
- Evolution III global rupture uses a separate abnormal profile described in Part 3.

## Flood family

Floods are hydrological disasters that target river basins, lowlands, deltas, monsoon zones, coastal plains, and states recently hit by storms, cyclones, wildfires, or heavy rain families. Floods should be one of the most common families in Evolution II because they chain naturally from other hazards.

Immediate effects:

- Damage to infrastructure, civilian factories, railways, supply hubs, dockyards if coastal, and airbases if severe.
- Moderate to high population loss in high-population lowlands and cities.
- Strong supply penalties.
- Temporary local production penalties.
- Possible resource output penalty for flooded farms, mines, or extraction zones.

Follow-ups:

- Wet mass movement in hills or mountains.
- Disease, famine, or contaminated water aftermath if severe.
- Refugee pressure into neighboring states.
- Repeated flooding after tropical cyclones or storm corridors.

Recovery play:

- Pumping and levee repair uses support equipment, trucks, fuel, and civilian factory burden.
- Secure river crossings requires unit presence or control of named states.
- Protect food stores reduces famine pressure.
- Emergency shelter lowers delayed deaths and stability loss.

## Tropical cyclone family

Tropical cyclones represent hurricanes, typhoons, and cyclones. They should target tropical and subtropical coastal states, island chains, warm-water coastlines, and cyclone basin state groups. They should often strike multiple neighboring coastal and inland states along a path.

Immediate effects:

- Heavy damage to ports, naval bases, dockyards, infrastructure, airbases, railways, supply hubs, and civilian factories.
- Population loss from wind, storm surge, and flooding.
- Strong local supply and movement penalties.
- Coastal convoys or naval activity can receive temporary disruption if that system is available.

Follow-ups:

- Floods in inland path states.
- Wet mass movements in mountains near the landfall path.
- Refugee pressure from coastal cities.
- Drought relief in rare cases when a drought-affected region receives rain, but flooding risk should often replace the drought pressure instead of cleanly fixing it.

Recovery play:

- Reopen ports and airfields.
- Clear roads and rail lines.
- Coastal evacuation reduces deaths when a second wave or storm surge follow-up is queued.
- International aid can use convoys and relations when a small country is hit.

## Thunderstorm family

Thunderstorms cover severe convective storms with lightning, local flash flooding, hail, and wind damage. They are smaller than tropical cyclones but can be frequent and disruptive. They should target warm, humid, plains, river, and seasonal storm regions, then use fallback targeting in high-chaos seasons.

Immediate effects:

- Damage to infrastructure, airbases, anti-air, radar, railways, and a small number of factories.
- Moderate population loss in severe variants.
- Temporary air mission disruption and supply disruption.
- Lightning can trigger wildfire in dry regions.

Follow-ups:

- Hailstorm if agricultural or plains target is selected.
- Flash flood in urban or river states.
- Extreme wind event if storm severity exceeds threshold.
- Wildfire if dry lightning triggers in drought conditions.

Recovery play:

- Repair power and communications, represented through infrastructure and radar or airbase recovery.
- Clear flash-flood damage.
- Dispatch fire crews if lightning creates a wildfire follow-up.

## Hailstorm family

Hailstorms should not be cosmetic. They are lower-death events but can devastate agriculture, aircraft, light infrastructure, livestock, and local industry. They should target plains, agricultural regions, temperate storm belts, and states with airbases or open industrial areas.

Immediate effects:

- Light to moderate building damage, focused on infrastructure, airbases, and civilian factories.
- Crop shock represented by temporary local supply, consumer goods, or stability pressure.
- Low to moderate population loss unless high severity.
- Potential aircraft or airfield disruption if supported by existing mechanics.

Follow-ups:

- Food shortage or famine pressure when repeated in the same region.
- Thunderstorm or flood continuation if part of a larger storm system.

Recovery play:

- Crop relief uses civilian factory burden, convoys for imports, or political agreements.
- Airfield repair uses support equipment, fuel, and construction capacity.
- Rural shelter reduces delayed deaths and stability loss.

## Extreme wind family

This family represents derechos, severe straight-line winds, violent windstorms, and non-cyclone wind events. It can include tornado swarms at ordinary scale, while Evolution III uses the abnormal moving storm corridor.

Immediate effects:

- Damage to infrastructure, factories, railways, airbases, radar, anti-air, supply hubs, and forts.
- Moderate population deaths, high when urban states are hit.
- Severe movement and supply disruption.
- Possible damage to ports if coastal.

Follow-ups:

- Floods if heavy rain is included.
- Wildfire if wind follows drought and fire weather.
- Tornado corridor abnormal event in Evolution III.

Recovery play:

- Clear roads and rail lines.
- Restore local command posts, represented by command power and support equipment.
- Reinforce shelters when forecasted second wind pulse appears.

## Wildfire family

Wildfires should target forests, drylands, drought-affected states, heat-wave states, and regions with low infrastructure or recent lightning storms. They should damage population and industry through fire, smoke, evacuation, and supply interruptions.

Immediate effects:

- Damage to infrastructure, civilian factories, resources, railways, and possibly military factories.
- Population loss from fire and smoke.
- Temporary supply and movement penalties.
- Local production penalty from evacuations and smoke.
- Optional natural air quality pressure if the air cleanliness system supports non-weapon smoke sources.

Follow-ups:

- Flood or wet mass movement after rain if burned slopes are hit.
- Drought and heat wave feedback.
- Refugee pressure into neighboring states.

Recovery play:

- Firebreaks require manpower, equipment, and state control.
- Evacuation corridors require trucks, trains, fuel, and supply access.
- Replant and stabilize slopes reduces future flood and landslide target weight.

## Drought family

Drought is a slow-onset climatological family. It should not always apply instant building destruction. It creates production pressure, supply stress, food pressure, population loss over time, wildfire risk, and refugee pressure.

Immediate effects:

- Local supply penalties and infrastructure strain.
- Reduced resource and agricultural productivity represented through state modifiers and country-level pressure.
- Low immediate deaths, rising delayed deaths if ignored.
- Stability and war support pressure if capital, core agricultural regions, or multiple states are affected.

Follow-ups:

- Wildfire.
- Heat wave.
- Famine pressure.
- Refugees.
- Dust storm or sandstorm in arid regions.

Recovery play:

- Water rationing is a stability tradeoff.
- Import grain uses convoys, civilian factories, and foreign access.
- Irrigation repair uses construction capacity and support equipment.
- Emergency food distribution reduces delayed deaths.

## Sandstorm and dust storm family

This family takes over the gameplay promise of the old Sandstorm event. It should target deserts, arid zones, dry plains, and drought-affected regions. It can affect combat, air operations, supply, division intel, and infrastructure without requiring the old separate event logic.

Immediate effects:

- Strong local movement, supply, air mission, and reconnaissance penalties.
- Light to moderate infrastructure and airbase damage.
- Low to moderate population deaths from exposure, crashes, and supply disruption.
- Stronger impact on motorized, armored, and air-heavy operations if implementation can support it.

Follow-ups:

- Drought continuation.
- Heat wave.
- Local famine pressure.
- Transport accidents represented through infrastructure and supply penalties.

Recovery play:

- Clear rail and road routes.
- Issue respirators and shelter orders using support equipment.
- Ground aircraft or protect airfields with a temporary combat tradeoff.

## Blizzard and severe winter storm family

Blizzards should target cold regions, high latitudes, mountains, winter climates, and states already under cold-wave pressure. They should be dangerous to supply and divisions, not only to factories.

Immediate effects:

- Damage to infrastructure, railways, supply hubs, airbases, and ports in freezing coastal states.
- Population deaths from exposure, shelter failure, and supply disruption.
- Strong supply, movement, and attrition penalties.
- Temporary air mission disruption.

Follow-ups:

- Extreme cold wave.
- Avalanche or dry mass movement in mountains.
- Flood after thaw in river regions.

Recovery play:

- Clear rail lines and mountain passes.
- Heat shelters use fuel, support equipment, manpower, and civilian factory burden.
- Protect troops requires command power and supply access.

## Extreme heat wave family

This family is similar to the separate Heat Wave event but must not stack with it. It should represent local or regional lethal heat inside the Natural Disasters season.

Immediate effects:

- Low building damage unless infrastructure fails, but high manpower, output, supply, and population pressure.
- Delayed deaths from heat exposure, water failure, and hospital overload.
- Reduced local construction, production, and division recovery.
- Stability and war support pressure when repeated or severe.

Follow-ups:

- Drought.
- Wildfire.
- Thunderstorm if heat breaks into violent storms.
- Refugee movement from high-density affected areas.

Recovery play:

- Cooling shelters consume fuel or electricity abstraction, support equipment, and civilian capacity.
- Water convoys require convoys, trucks, and access.
- Labor protection lowers output but reduces deaths.

Stacking rule:

- If the separate Heat Wave event already applies an active heat modifier to a target, Event 013 should not add a duplicate heat modifier there.
- It can route into drought, wildfire risk, or a weaker local heat stress pulse instead.

## Extreme cold wave family

Cold waves are regional cold shocks. They can appear with blizzards or separately. They should affect industry, supply, manpower, and deaths more than direct building destruction.

Immediate effects:

- Population deaths from exposure.
- Supply and movement penalties.
- Factory and construction slowdown.
- Fuel strain if modeled through decisions.
- Rail and port disruption in severe variants.

Follow-ups:

- Blizzard.
- Flood after thaw.
- Refugee or shelter pressure.

Recovery play:

- Emergency heating shelters.
- Rail thaw and repair missions.
- Food and fuel distribution.

## Dry mass movement family

Dry mass movements include landslides, rockfalls, slope failures, and avalanches without heavy rain. They should target mountains, hills, earthquake-affected slopes, drought-weakened slopes, and states with railways or supply hubs through difficult terrain.

Immediate effects:

- Damage to infrastructure, railways, supply hubs, forts, and mountain roads.
- Moderate population deaths in mountain settlements or rail corridors.
- Strong supply disruption.
- Possible military movement penalties in passes.

Follow-ups:

- Earthquake if part of a seismic chain.
- Flood if blocked rivers or later rain create a hazard.
- Refugee pressure if valleys are isolated.

Recovery play:

- Clear mountain passes.
- Rebuild rail tunnels.
- Evacuate isolated settlements.

## Wet mass movement family

Wet mass movements include mudslides, landslides from heavy rain, lahars, and debris flows. They should target mountains, wet climates, cyclone paths, flood zones, volcanic slopes, and wildfire-scarred slopes.

Immediate effects:

- Heavy local infrastructure and railway damage.
- Supply hub and road damage in mountains.
- Population loss in valleys and towns.
- Strong temporary movement penalties.

Follow-ups:

- Flood continuation.
- Volcanic lahar if tied to eruption.
- Disease or contaminated water if severe.

Recovery play:

- Stabilize slopes.
- Rebuild mountain rail and roads.
- Relocate exposed settlements with stability and construction tradeoffs.

## Volcanic eruption family

Volcanic eruptions should target defined volcanic region groups, island arcs, subduction zones, and volcanic mountain states. They should have several profiles, from local eruption to ash-producing regional disaster to Evolution III massive eruption.

Immediate effects:

- Heavy damage to infrastructure, railways, airbases, local factories, resources, and ports if coastal.
- Population deaths from lava, pyroclastic flows, lahars, ash, roof collapse, and evacuation failure.
- Ash state modifiers that reduce air missions, supply, production, and construction.
- Neighboring state ash fall for severe eruptions.

Follow-ups:

- Wet mass movement or lahar.
- Tsunami if island, coastal, flank collapse, or submarine eruption profile.
- Cold or harvest shock if ash cloud reaches high severity.
- Refugee pressure.

Recovery play:

- Evacuate volcanic slopes.
- Clear ash from airbases and rails.
- Restore water supplies.
- Ash masks and shelter decisions reduce delayed deaths.

Evolution III uses the massive eruption family described in Part 3.

## Tsunami family

Tsunamis are coastal hydrological or geophysical follow-ups. They should normally be triggered by earthquakes, volcanic eruptions, landslides, or meteor impacts. They can also appear as a direct family in evolved seasons if target logic selects a coastal hazard region.

Immediate effects:

- Heavy damage to coastal infrastructure, naval bases, dockyards, ports, civilian factories, coastal forts, and supply hubs.
- High population loss in dense coastal states.
- Port and naval disruption.
- Neighboring coast states can receive reduced wave damage after a delay.

Follow-ups:

- Floods.
- Refugee pressure.
- Disease or contaminated water aftermath.
- Port closure missions.

Recovery play:

- Coastal evacuation if warning exists before the wave.
- Reopen ports and naval bases.
- Clear debris and restore water.
- Shelter displaced coastal population.

## Avalanche family

Avalanches can be folded under dry or wet mass movement, but the system should support them as a named winter mountain profile when blizzards and cold waves strike mountainous states.

Immediate effects:

- Damage to infrastructure, railways, mountain passes, forts, and supply routes.
- Population loss in mountain settlements.
- Severe movement penalties for units crossing passes.

Follow-ups:

- Blizzard continuation.
- Isolated valley mission.

Recovery play:

- Clear passes with engineer and equipment costs.
- Rescue isolated units or civilians.

## Glacial lake outburst flood family

This family is optional but valuable for high mountain regions. It should target glaciated mountains, high-altitude lakes, and flood-prone downstream valleys. It can appear in Evolution II or high heat after cold seasons.

Immediate effects:

- Flood-like damage along downstream states.
- Heavy infrastructure and rail damage.
- Population loss in valleys.
- Supply disruption.

Follow-ups:

- Wet mass movement.
- Refugee pressure.

Recovery play:

- Drain unstable lakes.
- Reinforce mountain roads and bridges.

## Sinkhole and ground collapse family

This family can be rare. It should target karst, mining, urban infrastructure, or high-construction states when the implementation can identify them. It is useful for smaller baseline variety.

Immediate effects:

- Local infrastructure and factory damage.
- Rail or supply disruption.
- Low to moderate population deaths.

Follow-ups:

- Urban evacuation and repair missions.
- Infrastructure inspection decisions.

## Limnic eruption family

This family should be rare and region-gated. It represents gas release from volcanic lakes. It is strong for deaths but limited geographically.

Immediate effects:

- High local population loss in affected lake-adjacent state.
- Limited building damage.
- Panic and evacuation pressure.

Follow-ups:

- Refugee pressure.
- Scientific containment decisions if such systems exist.

Because it is region-specific, the implementation should skip it cleanly when no valid target exists.

## Meteor shower family

Meteor showers are Evolution III abnormal disasters by default. A smaller meteorite impact can appear rarely in Evolution II if the system wants a precursor, but the main family belongs to high chaos.

Immediate effects:

- Crater damage to infrastructure, factories, airbases, and supply hubs.
- Population deaths based on impact location.
- Fires, shockwaves, and panic.
- Possible tsunami if ocean or coastal impact profile is selected.
- Possible global news or super-event when several states are hit.

Follow-ups:

- Wildfire.
- Tsunami.
- Dust and ash-like skyfall modifier.
- Refugee pressure.

Recovery play:

- Secure impact sites.
- Fire suppression.
- Evacuate unstable craters.
- Scientific or military exploitation should be a separate future hook only if another event asks for it.

## Storm corridor abnormal family

The storm corridor is an Evolution III abnormal form of extreme wind and tornado behavior. It should move across the map over time through a scripted GUI dynamic map. The player should see the current corridor, likely next regions, uncertainty, and response options.

Immediate effects per movement step:

- Severe damage to infrastructure, railways, factories, airbases, radar, supply hubs, and population in the path.
- Neighboring states receive reduced damage and warning modifiers.
- A second path can split at high intensity.

Follow-ups:

- Floods.
- Wildfires if dry.
- Hail and thunderstorm families.
- Refugee pressure.

Recovery play:

- Issue evacuation orders along predicted path.
- Reinforce shelters and rail bridges.
- Ground aircraft before landfall.
- Divert resources from safe states to target states.

The corridor should never be only visual. The GUI must drive real choices and AI equivalents.
