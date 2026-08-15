# Air Cleanliness and Fallout World-End Source Spec, Part 2 Winter Mapmode and Atmospheric Gameplay

Canonical status: accepted baseline design, corrected for independent Fallout ownership and extended by the living-world specs in this package.

Working label, not final localisation: `air_winter_mapmode`.

## Mapmode purpose

The new mapmode exists because the sky must be visible. The player should be able to open the mapmode and understand which states are still livable, which states are becoming dead, which states can feed people, and which states will become Fallout cores after the world-end transition.

The mapmode should not simply color every country by the same global value. It must be state-based.

## Mapmode presentation

Air Winter owns one state-based mapmode. Winter phase is the only color layer. Exposure and survival remain live state values shown inside the same viewer-gated tooltip rather than separate mapmode buttons or keyboard-cycled views.

| Surface | What it shows | Tooltip must include |
| --- | --- | --- |
| Air Winter | State phase 0 to 6 | Phase label, monthly death pressure, supply impact, building damage risk, category drift, Fallout intensity, expected exposure movement, contamination, shelter, survival value, food, water, reclamation, recovery, adaptation, and refugee pressure |

The mapmode legend must show six to seven phase bands with readable contrast. Exact colors belong to UI implementation, but the progression should move from clean blue or green into grey, black, sick yellow, and harsh red.

## Tooltip content direction

The tooltip should answer the player's practical question. It should not expose raw script internals first.

Useful ordering:

1. State winter phase.
2. Immediate local effects.
3. Population danger.
4. Building and category danger.
5. Why this phase exists.
6. Player action available, if any.
7. Fallout-aftermap classification forecast, hidden unless the world is already past 90 percent contamination or the player has built relevant monitoring infrastructure.

## Forecasting and uncertainty

Early in the crisis, states should not always show their future Fallout category. Forecasting requires monitoring capacity.

| Monitoring level | Who has it | What is visible |
| --- | --- | --- |
| None | Most countries | Current winter phase only. |
| Basic sampling | Countries with air decisions or treaty membership | Current phase and one-month trend. |
| Atmospheric office | Countries that invest in monitoring | Trend, cause breakdown, and likely phase next season. |
| Terminal modelling | Late crisis countries and great powers | Possible Fallout category forecast. |

## Mapmode gameplay hooks

The mapmode must support decisions. Clicking a state in this mapmode should make the relevant decision category show actions for that state or state group.

| State condition | Decision families unlocked |
| --- | --- |
| Phase 1 and 2 | Mask distribution, clinic expansion, local sampling, crop testing |
| Phase 3 | Ash clearing, rail protection, airbase closure, evacuation planning |
| Phase 4 | Emergency shelter law, greenhouse conversion, controlled evacuation, state triage |
| Phase 5 | Abandonment vote, bunker closure, final evacuation, decontamination gamble |
| Fallout exposure high | Shelter lockdown, radiation medicine, salvage ban, mutant incident response |
| Survival value high | Protect seed banks, defend waterworks, fortify port, preserve hydro plants |

## Seasonal winter pulses

Winter flavour should arrive in seasons. Monthly ticks update numbers, but seasonal pulses create story.

| Pulse | Timing | Uses |
| --- | --- | --- |
| First frost pulse | First state enters Phase 2 in a year | Regional report event, small country decisions. |
| Dark harvest pulse | Agricultural season after Phase 3 | Crop failure, food riots, greenhouse route. |
| Ash thaw pulse | After a Phase 3 to 4 state begins recovery | Refugee return, corpse disease risk, salvage. |
| Second winter pulse | Same region repeats severe winter | Stronger population loss and state category damage. |
| Terminal season pulse | World above 90 percent | Government collapse events and Fallout setup. |

## State category ladder

State category degradation is a core feature. It should preserve an audit trail so restoration or post-Fallout salvage can know what was lost.

| Original category | First downgrade | Severe downgrade | Fallout rewrite candidates |
| --- | --- | --- | --- |
| Metropolis | Large city | City | Dead city, bunker city, shattered capital |
| Large city | City | Town | Dead city, scavenger ruins, shelter belt |
| City | Town | Rural | Scavenger zone, empty town, fortified town |
| Town | Rural | Sparse rural | Rural refuge, contaminated village, ash farm |
| Rural | Sparse rural | Wasteland | Greenhouse refuge, badlands, mutant biosphere |
| Wasteland | Wasteland | Wasteland | Vitrified deadland or forbidden zone |

The transition should not be a single hard cliff except during the Fallout rewrite. Before Fallout, a state should normally need sustained phase 4 or phase 5 pressure before category downgrade.

## Population and refugee interaction

Every state gets a temporary survival pressure score. It comes from winter phase, fallout exposure, shelter capacity, local food, infrastructure, port access, and whether the state is under active combat.

| Pressure result | State effect | Country effect |
| --- | --- | --- |
| Low pressure | No population loss | Ordinary politics continue. |
| Elevated pressure | Small Deaths tick and local support hit | Refugee concern events. |
| Crisis pressure | Deaths tick, local resistance, building damage | Decisions for evacuation or hardline order. |
| Collapse pressure | Severe Deaths tick and category degradation chance | Government legitimacy loss, possible state abandonment. |
| Terminal pressure | Fallout rewrite candidate | Survivor factions may spawn after black screen. |

Refugees should not be only a penalty. Refugee movement can provide manpower, skilled workers, scientists, officers, and future faction leaders to safer states if the receiving country has capacity.

## Pre-Fallout government strain

As air contamination rises, governments should change before the final black screen. This gives the player narrative buildup and helps create more varied Fallout successors.

| Strain level | Trigger | Effects |
| --- | --- | --- |
| Administrative fatigue | Several Phase 2 states | Small stability and bureaucracy decisions. |
| Emergency governance | Phase 3 in core population states | Emergency law decisions, opposition events, shelter budgets. |
| Winter cabinet | Phase 4 in capital or industry | Leader trait changes, cabinet replacement, ration board. |
| Continuity protocol | Phase 5 or 90 percent global contamination | Capital evacuation, bunker capital, emergency tag memory. |
| State abandonment | Phase 5 sustained and low infrastructure | State can become a future warlord, refuge, or mutant polity. |

## Winter flavour events by biome

| Biome or state identity | Event family | Effects |
| --- | --- | --- |
| Breadbasket | Seed vault argument | Spend political capital and factories to preserve seed stock. Failure worsens food recovery after Fallout. |
| Coal or heavy industry | Furnace rationing | Keep factories running at population and stability cost, or shut them down to reduce exposure. |
| Hydroelectric region | Dam ice crisis | Protect power and water with engineers, or risk infrastructure damage. |
| Oil region | Black refinery snow | Fuel output falls, fire risk rises, refinery can become post-Fallout oil fortress. |
| Tropical coast | Rot tide | Dockyards and convoys suffer. Medical spending can limit deaths. |
| Desert city | Water convoy crisis | Trains and trucks decide whether the city survives. |
| Mountain capital | Tunnel schools | Shelter capacity rises and population loss falls, but industry suffers. |
| Island state | Refugee boats | Choose rescue, quarantine, or naval exclusion. Each changes population, stability, and later country identity. |
| Dead city candidate | Night salvage | Risk early salvage before Fallout for equipment, with high death and mutation chance. |
| Reactor state | Cooling pond emergency | Spend engineers and power to avoid state fallout spike. |

## Treaty integration

The treaty should become more than an opinion and embargo system once winter phases exist. Treaty members can run coordinated operations that target mapmode states.

| Treaty operation | Available when | Effects |
| --- | --- | --- |
| Shared sampling grid | 75 percent treaty formed | Improves mapmode forecasting for members. |
| Joint filter convoy | Member owns Phase 3 state | Lowers death pressure if convoy route is safe. |
| Seed archive exchange | Member has breadbasket or seed vault | Improves winter food resilience and post-Fallout greenhouse start. |
| Evacuation corridor | Member borders Phase 4 or Phase 5 state | Moves population and creates refugee pressure in receiving state. |
| Sanction the burners | Non-member caused severe contamination recently | Adds condemnation and embargo, but may push violator toward Fallout radical routes. |

## AI behaviour for winter

AI countries must not ignore the mapmode. AI should weigh decisions by survival value.

| AI country type | Priority |
| --- | --- |
| Major industrial power | Protect capital, power, rail, and military factories. Shift industry to less exposed states. |
| Small island | Protect ports and food, refuse refugees if shelter capacity is low, accept treaty help if democratic or neutral. |
| Agrarian country | Preserve food states, seed banks, and rural manpower. |
| Fascist or desperate regime | More likely to use forced clearing, abandonment, and doomsday chemical options. |
| Democratic treaty founder | More likely to fund sampling, convoys, evacuation, and public reports. |
| Communist state | More likely to centralize ration boards and mass labour clearing. |
| High-chaos cult or special country | May exploit severe winter for radical paths. |

## Acceptance criteria for this system

The Air Cleanliness expansion is not complete until the winter phase is visible in a mapmode, at least one seasonal event family exists for each major phase group, state population loss is connected to Deaths, building and state-category effects exist, AI has usable responses, and the player can take state-targeted action from the mapmode or matching decision categories.
