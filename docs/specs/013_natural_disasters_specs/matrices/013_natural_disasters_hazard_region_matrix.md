# Natural Disasters Hazard Profile and Region Planning Matrix

This matrix gives the implementation agent region and terrain direction. It intentionally avoids exact HOI4 state ids because those should be built by inspecting the current map files and existing state groups.

## Hazard profile groups

| Profile | Families using it | Geographic logic | Fallback logic |
| --- | --- | --- | --- |
| Seismic belt | Earthquake, tsunami, dry mass movement, global rupture | Plate-boundary approximations, mountain arcs, subduction zones, Mediterranean, Anatolia, Caucasus, Himalayas, Andes, Japan, Indonesia, Caribbean, New Zealand, California, Alaska | Mountain or coastal high-building states |
| Volcanic arc | Volcanic eruption, massive eruption, tsunami, lahar | Island arcs, volcanic mountains, Pacific Ring of Fire, Mediterranean volcanoes, East African Rift, Iceland, Andes, Japan, Indonesia | Mountain states with seismic profile |
| River basin and floodplain | Flood, wet mass movement, drought aftermath, glacial outburst | Major rivers, deltas, lowlands, monsoon basins, flood-prone plains | Low infrastructure or high population lowland states |
| Tropical cyclone basin | Tropical cyclone, flood, wet mass movement | Warm-water coasts, islands, Caribbean, Gulf, Bay of Bengal, western Pacific, Indian Ocean, South Pacific, east Asian coasts | Coastal tropical or subtropical states |
| Severe storm belt | Thunderstorm, hail, extreme wind, tornado corridor | Plains, humid continental or subtropical regions, seasonal storm tracks | Agricultural or high-airbase plains states |
| Desert and dust belt | Sandstorm, dust storm, drought, heat | Sahara, Sahel, Arabian Peninsula, Iranian Plateau, Central Asia, Gobi, Australian interior, southwestern North America, Atacama-like drylands | Arid terrain and low-rainfall state groups |
| Wildfire belt | Wildfire, heat, drought, post-thunderstorm fire | Forested drylands, Mediterranean climates, drought-hit regions, low humidity, windy states | Forest terrain with active heat or drought pressure |
| Winter and blizzard belt | Blizzard, cold wave, avalanche | High latitudes, mountain winters, Siberia, Canada, Scandinavia, Alps, Himalayas, Andes highlands | Cold terrain, mountain, or snow climate states |
| Mountain slope | Dry mass movement, wet mass movement, avalanche, glacial lake outburst | Mountain and hill states, rail passes, valleys, volcanic slopes, burned slopes | High terrain states with rail or hub buildings |
| Coastal surge and tsunami | Tsunami, cyclone surge, storm corridor coast steps | Coastal states with ports, naval bases, dockyards, dense population, island chains | Any coastal state with port or naval base |
| Urban vulnerability | Earthquake, heat, cold, flood, wind, meteor | High population or high factory states, capitals, major VPs | High building count or capital states |
| Abnormal skyfall | Meteor shower | Random global with weight to high visibility targets, coasts for tsunami profiles, urban for high-stakes impacts | Random valid state, with cooldown protection |
| Moving corridor | Storm corridor | Neighboring state path logic, regional bands, ocean-to-land transitions if modeled | State list path built from active hazard map |

## State cooldown rules

- Recently hit states should receive a cooldown to avoid repeated ordinary disasters.
- Follow-up disasters can bypass this cooldown when they are causally tied to the first hit.
- Cooldown should be shorter for minor storms and longer for severe earthquakes, tsunamis, massive eruptions, and meteor impacts.
- The storm corridor uses its own path memory instead of ordinary random cooldown alone.

## Regional specificity goals

Each family should feel geographically plausible without blocking gameplay. If exact state groups are not available at first implementation, use a staged approach:

1. Build high-confidence state groups for major hazard regions.
2. Use terrain, coastal, climate, population, and building fallbacks.
3. Document every fallback and improve the hazard map later.
4. Avoid invalid targets such as tsunamis in inland deserts or blizzards in equatorial lowlands.

## Neighbor and path spread

Multi-state disasters need spread logic.

- Earthquakes spread to adjacent states around epicenter.
- Floods spread downstream or through neighboring lowlands.
- Cyclones draw a landfall and inland path.
- Tsunamis spread along coastlines after a delay.
- Ash clouds spread to neighboring or downwind regions if wind abstraction exists.
- Wildfires spread through forests and dry neighboring states.
- Storm corridors move through weighted path steps and can turn or split.
