# Achievement prompt for Air Cleanliness and Fallout

Canonical status: accepted baseline prompt, subject to the corrected ownership and living-world source specs in this package.

Implement achievements only after the core Fallout systems, focus routes, and country packages exist. Achievements must not unlock simply because the scenario launches.

Planned achievement working ids:

| ID | Route | Unlock direction | Disqualifiers | Icon direction |
| --- | --- | --- | --- | --- |
| `fallout_keep_the_lights_on` | Technate | Restore a regional power grid without reactor meltdown. | Any owned reactor meltdown. | Reactor lamp in black snow. |
| `fallout_no_empty_bunks` | Bunker | Survive ten years with no shelter riot and positive population trend. | Shelter riot or famine collapse. | Bunker door with warm light. |
| `fallout_bread_for_the_black_sky` | Food compact | Feed three other countries while keeping high cohesion. | Famine policy or food betrayal. | Greenhouse wheat under dark sky. |
| `fallout_the_old_flag_still_flies` | Continuity | Reclaim old capital and pass a new charter. | Abandon old identity route. | Tattered flag over rebuilt capitol. |
| `fallout_crown_of_ruins` | Warlord | Unite several dead-city regions by force. | Puppet shortcut or non-warlord route. | Crown made of scrap. |
| `fallout_new_species_order` | Mutant | Complete mutant late-game route and force recognition. | Purge or containment route. | Glowing hand over map. |
| `fallout_no_more_ground_zero` | Any | Stabilize or clean a major set of wasteland states. | Uses forbidden annihilation route. | Decontamination crew in ruins. |
| `fallout_the_sea_roads_open` | Maritime | Build a port compact across three regions. | Piracy empire route. | Convoy through ash fog. |
| `fallout_last_seed` | Any | Save a seed vault and restore a food state with it. | Seed vault lost. | Seed jar with cracked glass. |
| `fallout_after_final_silence` | Final Silence cause memory | Survive as a non-cult successor for ten years. | Accepts terminal cult route. | Black sky with shelter candle. |
| `air_clean_world_for_one_more_year` | Air pre-Fallout | Keep contamination above 75 but below 100 for one year through treaty and cleaning actions. | Uses unconventional weapon during the year. | Mask and treaty seal. |
| `black_snow_harvest` | Air winter | Keep a Phase 4 breadbasket alive through winter and prevent category downgrade. | State downgrades or famine. | Wheat in ash snow. |

Each achievement needs completed, grey, and not eligible icon variants when wired. Achievement text direction must be implementation-written and must not reveal hidden routes before discovery.
