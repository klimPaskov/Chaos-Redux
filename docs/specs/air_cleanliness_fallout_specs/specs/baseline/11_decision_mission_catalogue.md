# Air Cleanliness and Fallout World-End Source Spec, Part 11 Decision and Mission Catalogue

Canonical status: accepted baseline design, corrected for independent Fallout ownership and extended by the living-world specs in this package.

This file expands decision families. Final IDs, titles, descriptions, and tooltips belong to implementation.

## Air phase decisions before Fallout

| Family | Visible in | Action direction | Cost palette | Effect direction |
| --- | --- | --- | --- | --- |
| Mask drives | Phase 1 to 3 states | Distribute masks and basic filters | Support equipment, infantry equipment, stability | Lower local death and illness pressure. |
| Clinic expansion | Phase 1 to 4 cities | Convert clinics into respiratory wards | Support equipment, medicine, civilian factories | Lower deaths and panic, improve monitoring. |
| Ash clearing | Phase 3 to 5 rail or city states | Clear ash from rails and roofs | Trucks, manpower, command power, filters | Repair infrastructure, risk worker deaths. |
| Greenhouse conversion | Phase 3 plus food or city states | Convert factories and halls to controlled agriculture | Civilian factories, power, fuel, water | Creates food source and greenhouse refuge candidate. |
| Shelter agriculture | Bunker or mountain states | Grow food in tunnels and sealed rooms | Power, water, support equipment | Low food but resilient. |
| Controlled evacuation | Phase 4 to 5 states | Move population to safer states | Trains, convoys, food, receiving shelter | Reduces death but creates refugee pressure. |
| Abandonment vote | Sustained Phase 5 | Decide whether to abandon the state | Stability, legitimacy, units present | Saves resources but creates dead-zone memory. |
| Treaty convoy | Treaty members | Send aid to member Phase 3 plus state | Convoys, support equipment, filters | Improves target state and treaty cohesion. |

## Fallout survival decisions

| Family | Action direction | Cost palette | Success | Failure or risk |
| --- | --- | --- | --- | --- |
| Expand shelter | Build bunks, airlocks, and sealed wards | Scrap, support equipment, power | Shelter capacity rises | Shelter riot if delayed |
| Ration ledger | Adjust ration fairness | Food, cohesion, ideology | Stabilizes food use | Black market or unrest |
| Water route | Repair pumps, escort water trucks, secure aquifers | Trucks, fuel, units, engineers | Clean water rises | Disease or water war |
| Medicine triage | Treat radiation and disease | Medicine, support equipment, stability | Death tick falls | Legitimacy loss if harsh |
| Salvage dead city | Send crews into ruins | Manpower, filters, trucks, medicine | Scrap, equipment, tech lead | Casualties, mutation, leader sickness |
| Repair rail spine | Rebuild route states | Scrap, trains, units in state | Supply and trade route | Bandit spawn or failed route |
| Secure seed vault | Guard seed state and power | Units, food, power, engineers | Food future improves | Vault lost or raided |
| Cool reactor | Prevent meltdown | Water, engineers, medicine, power | Power and research | Forbidden zone |
| Admit refugees | Accept a wave | Food, shelter, stability | Manpower and workers | Riot, disease, faction pressure |
| Screen refugees | Slow but safer admission | Medicine, manpower, legitimacy | Lower disease and spies | Refugee resentment |
| Recruit refugees | Form units | Food, infantry equipment, training time | New units | Low cohesion if abused |
| Mutant truce | Negotiate with altered group | Medicine, legitimacy, security | Mutant integration path | Rebellion or purge pressure |
| Mutant battalion | Weaponize altered survivors | Medicine, command power, stability | Special units | Diplomatic fear and instability |
| Radio recognition | Contact another survivor | Power, radio state, convoy route | Diplomacy opens | Ambush or humiliation |
| Compact vote | Create local alliance | Recognition, food, shared threat | Compact or faction | Members refuse or betray |
| Restore state category | Reclaim a ruined state | Reclamation capacity, scrap, power, units | State improves | Waste of resources or relapse |

## Mission catalogue

| Mission | Owner | Objective | Duration band | Success | Failure |
| --- | --- | --- | --- | --- | --- |
| Keep the capital air clean | Any capital in Phase 3 plus | Maintain filters, power, and support equipment | 120 to 180 days | Capital deaths fall, cohesion rises | Capital panic and category drift |
| Guard the waterworks | Water-stressed country | Keep supplied divisions in water state | 120 to 180 days | Clean water rises | Disease event and water war claim |
| Protect the seed vault | Food compact or any vault owner | Hold and power seed state | 180 to 365 days | Greenhouse route improves | Seed vault lost |
| Escort the ash convoy | Any with convoy route | Keep route states controlled and supplied | 90 to 150 days | Trade opens | Convoy massacre |
| Cool the reactor | Reactor keep | Spend resources and keep engineers alive | 120 to 240 days | Reactor stable | Meltdown and forbidden zone |
| Open the tunnel road | Bunker authority | Control entrance states and spend engineers | 90 to 180 days | Surface sorties safer | Tunnel collapse |
| Pacify the shelter | Bunker or continuity | Keep food, shelter, and cohesion above floor | 90 to 180 days | Shelter riot avoided | Riot and building damage |
| Dead-city push | Scavenger or warlord | Complete salvage without losing too many crews | 90 to 150 days | Scrap and equipment | Mutant breach or casualties |
| Recognition by radio | Continuity or maritime | Keep power and contact target | 90 to 180 days | Recognition value | Humiliation and isolation |
| Mutant ceasefire | Mutant or neighbour | Prevent border violence and maintain talks | 120 to 240 days | Diplomacy or citizenship path | Purge war |

## Clutter control

Use selected targets and active caps. The player should not see every state decision at once.

| System | Clutter rule |
| --- | --- |
| State recovery | One selected state group per category view, plus emergency states. |
| Salvage | Active expedition cap based on Reclamation Capacity and archetype. |
| Refugees | Show current wave, receiving states, and policy decisions only. |
| Mutants | Show policy decisions only when mutant pressure exists or route unlocks. |
| Diplomacy | Show contacted states and nearby signals first. |
| Late ambition | Hidden until route and state requirements are close. |

## Exploit controls

- Salvage cannot repeatedly farm the same dead city without escalating danger or depletion.
- Refugee recruitment cannot create free units without food, equipment, and cohesion cost.
- State category restoration requires sustained investment and cannot be spammed globally.
- Mutant battalions require route support and raise diplomatic consequences.
- Food export cannot be used if domestic famine is active unless route explicitly embraces sacrifice.
- Warlord tribute can trigger resistance, coalitions, and convoy ambushes.
- Reactor power has meltdown risk and water cost.

## Localisation direction

Decision text should describe concrete action. Use state names, resource icons, and dynamic values. Do not expose hidden future routes. Do not copy working labels from this spec as final names.
