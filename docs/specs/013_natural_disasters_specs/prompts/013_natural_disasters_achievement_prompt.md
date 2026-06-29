
# Achievement prompt for Event 013 Natural Disasters

Use this file to implement Event 13 achievements and hand achievement icon needs to the asset workflow. All title labels are working labels and are not final localisation.

## Achievement list

| Working key | Title direction | Eligible country | Unlock conditions | Disqualifiers | Visibility | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| achievement_nd_prepared_capital | Direction about saving a capital through preparation. | Any player country. | Receive a warning for a disaster that targets the capital state, take at least two relevant preparation actions before impact, and keep capital industry damage and deaths below the family threshold. | Capital changes before impact, no real warning phase, or using force-trigger debug mode. | Visible. | Medium. | Protected capital and warning siren. |
| achievement_nd_no_deaths_sequence | Direction about completing a sequence with minimal civilian loss. | Any player country. | Be directly targeted by an Event 13 sequence with at least two incidents, complete all recovery missions, and keep disaster deaths below a strict scaled threshold. | Sequence contains only one light incident, or deaths tracking disabled. | Hidden or rare. | Hard. | Rescue emblem over protected crowd. |
| achievement_nd_tame_the_barrage | Direction about surviving the manual barrage. | Any player country. | Launch Disaster Barrage at High or Maximum, remain independent, keep capital controlled, and clear all active ledgers within a long deadline. | World-end state from another event begins before cleanup, or player changes tag. | Visible. | Hard. | Disaster map with cleared markers. |
| achievement_nd_firebreak_master | Direction about stopping a wildfire chain. | Any player country with wildfire impact. | Prevent a wildfire or heat-to-wildfire chain from spreading to any neighboring state after the first warning. | No wildfire spread risk existed. | Visible. | Medium. | Firebreak line. |
| achievement_nd_aftershock_control | Direction about mastering earthquake aftermath. | Any player country. | Suffer a severe earthquake or quake-wave, complete aftershock inspections, prevent tsunami if applicable, and repair transport damage before deadline. | No severe seismic impact. | Visible. | Hard. | Reinforced cracked bridge. |
| achievement_nd_skyfall_survivor | Direction about surviving meteor shower. | Any player country. | Be directly hit by an Evolution III meteor shower or Skyfall Crisis, protect at least one high-value state through warning or recovery, and clear crater aftermath. | Manual Low or Medium scenario if no true skyfall impact occurs. | Hidden. | Hard. | Meteor over shelter. |
| achievement_nd_global_relief | Direction about becoming a global relief coordinator. | Major or faction leader. | Send relief to at least five different countries during Event 13 aftermaths and have at least three accepted relief outcomes. | Relief recipients were puppets only, if the implementation treats that as too easy. | Visible. | Medium to hard. | Relief train and convoy. |
| achievement_nd_no_world_end | Direction about holding chaos below terminal outcome after maximum disaster season. | Any player country. | Launch Maximum Disaster Barrage or experience an Evolution III abnormal season, clear all player-country ledgers, and avoid any world-end scenario for a defined period. | World-end disabled through debug or settings if achievement rules disallow that. | Hidden. | Very hard. | Globe under storm held stable. |

## Tracking notes

- Achievements must not unlock just because Event 13 fired.
- Use flags or variables that track preparedness actions, impact severity, recovery completion, deaths, and active ledgers.
- If deaths tracking is disabled, achievements that require death thresholds should be unavailable or use a clear alternate blocker.
- Manual scenario achievements should track scenario intensity and type at launch.
- Hidden achievements should not reveal secret abnormal wording before the player sees Evolution III.
- Asset handoff must include completed icon directions for every achievement.
