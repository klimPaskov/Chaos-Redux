# Air Cleanliness and Fallout World-End Source Spec, Part 10 Focus Tree Architecture Maps

Canonical status: accepted baseline design, corrected for independent Fallout ownership and extended by the living-world specs in this package.

This file gives path-level focus design. Implementation owns exact focus names, positions, durations, prerequisites, and final localisation.

## Shared layout principle

Every Fallout focus tree should look like a broken nation trying to decide what survival means. The opening branch should sit above the route split. Political branches should alter survival decisions, army recruitment, diplomacy, and state recovery. Industry branches should change the map. Expansion branches should fight over concrete resources such as water, food, power, ports, rails, seed vaults, and dead cities.

## Universal tree lane map

| Lane | Early | Middle | Late |
| --- | --- | --- | --- |
| Survival | Count people, secure stores, filter air | Expand shelters, stabilize food and water | Population recovery or hard triage route |
| Politics | Emergency law | Archetype route split | New constitution, protocol, cult, or compact |
| Economy | Salvage and repair | State class economy | Regional production system |
| Military | Cadres and guards | Route units and commanders | Army doctrine of the ruins |
| Diplomacy | Radio contact | Recognition and compacts | New order or isolation doctrine |
| Expansion | Secure nearby resource | Claims on route states | Formable or regional ambition |
| Special | Air, mutation, reactor, sea, or bunker mechanic | Deep route mechanics | Absurd high-chaos or restoration capstone |

## Continuity government tree

| Branch | Unlocks | Tradeoff | Failure state |
| --- | --- | --- | --- |
| Legal Memory | Claims, old officers, archives, court decisions | Old legitimacy helps diplomacy but angers splinters | Archive scandal and legitimacy crash |
| Emergency Cabinet | Civilian, military, or technate caretaker route | Faster recovery versus political freedom | Cabinet coup or military seizure |
| Reclamation Bureau | Restore state categories and old capital projects | High resource cost | Failed reclamation creates dead-zone revolt |
| Old Enemies | War goals or negotiations with breakaways | Reunification pressure raises threat | Overreach creates anti-continuity league |
| New Charter | Final political settlement | Locks identity and late-game diplomacy | Incomplete charter leaves permanent instability |

## Bunker authority tree

| Branch | Unlocks | Tradeoff | Failure state |
| --- | --- | --- | --- |
| Seal Discipline | Shelter expansion, air rationing, police | Survival at freedom cost | Shelter riot |
| Tunnel Economy | Underground factories and medicine | Low food, high power need | Tunnel sickness |
| Surface Sorties | Salvage and recon | Casualties and mutation risk | Lost expedition panic |
| Protocol Politics | Director, council, machine, or revolt | Stability versus legitimacy | Protocol purge or democracy uprising |
| Subterranean Nation | Underground formable and state class conversion | Weak surface diplomacy | Surface coalition forms against the bunker |

## Warlord command tree

| Branch | Unlocks | Tradeoff | Failure state |
| --- | --- | --- | --- |
| Arms First | Fast units, raiding, depot seizures | Low legitimacy and food burn | Follower mutiny |
| Tribute Roads | Road tolls, convoy raids, puppet demands | More enemies and less recognition | Trade blockade |
| Camp Followers | Manpower from refugees | Food and shelter pressure | Camp disease or revolt |
| Fear or Oath | Brutal rule or warrior law | Repression power versus cohesion | Gang fracture |
| Crown of Ruins | Dead-city empire path | Permanent diplomatic hatred | Coalition war |

## Food compact tree

| Branch | Unlocks | Tradeoff | Failure state |
| --- | --- | --- | --- |
| Seed and Water | Seed vaults, irrigation, greenhouses | Needs power and defense | Seed vault loss |
| Ration Citizenship | Who gets food and rights | Stability versus refugee manpower | Hoarder coup |
| Defend the Farms | Farm guard units and fortification | Lower food exports | Warlord raids |
| Trade Calories | Food diplomacy and recognition | Convoy risk | Food betrayal scandal |
| Breadbasket Federation | Regional compact and humanitarian leverage | Military weakness if overextended | Member famine exit |

## Scavenger syndicate tree

| Branch | Unlocks | Tradeoff | Failure state |
| --- | --- | --- | --- |
| The Auction Law | Scrap economy and markets | Corruption rises | Guild war |
| Licensed Salvage | Safer expeditions and better yields | Slower gains | Illegal deep salvage |
| Rust Diplomacy | Trade with many archetypes | Recognition remains fragile | Market blockade |
| City of Scrap | Dead city development | Health and mutation danger | Ruin breach |
| Buy the Future | Tech purchase and mercenary route | Dependency on trade | Syndicate collapse |

## Technate tree

| Branch | Unlocks | Tradeoff | Failure state |
| --- | --- | --- | --- |
| Power First | Grid repair, hydro, generators | Food neglected | Worker hunger strike |
| Engineer Franchise | Elitist or public science politics | Efficiency versus legitimacy | Technician coup |
| Salvage Science | Labs, expeditions, special projects | Radiation risk | Research accident |
| Atomic Bargain | Reactor route | Power versus meltdown | Forbidden zone creation |
| Switch the Lights On | Regional grid formable | Target for all neighbours | Grid war |

## Mutant polity tree

| Branch | Unlocks | Tradeoff | Failure state |
| --- | --- | --- | --- |
| Name the Changed | Citizenship, caste, army, or faith route | Internal unity versus outside fear | Identity civil war |
| Altered Bodies | Mutant units and adaptation | Instability and medicine demand | Degeneration event chain |
| Fear Outside | Diplomacy, terror, or outreach | Recognition versus strength | Human crusade |
| Breed True or Stay Human | Species route split | Extreme power versus isolation | Purge or collapse |
| New Species Order | Late-game mutant formable | Absurd military strength, severe diplomacy | Global containment war |

## Maritime remnant tree

| Branch | Unlocks | Tradeoff | Failure state |
| --- | --- | --- | --- |
| Keep the Harbor | Port survival and dockyard repair | Fuel demand | Harbor riot |
| Convoy Law | Trade and escort systems | Pirate risk | Convoy famine |
| Refugee Boats | Rescue or exclusion politics | Manpower versus stability | Quarantine crisis |
| Sea Road Compact | Regional port diplomacy | Needs many ports | Compact betrayal |
| Admiralty of the Ash Sea | Naval late-game route | Inland weakness | Landward siege |

## Machine protocol tree

| Branch | Unlocks | Tradeoff | Failure state |
| --- | --- | --- | --- |
| Reboot Node | Production and defense | Power dependence | Shutdown loop |
| Human Exception | Human rights or cold protocol | Legitimacy versus output | Human revolt |
| Automated War | Special units and defense | Low diplomacy | Protocol panic |
| Factory Mind | Industry route | Resource hunger | Machine famine |
| Final Directive | Caretaker or extermination route | Extreme route lock | World coalition or self-termination |

## Focus rewards that must appear across trees

- State-targeted decisions.
- Building restoration and state category recovery.
- Unit templates, commanders, and special unit families.
- Leader or council changes.
- Flag or cosmetic identity changes where routes transform the state.
- Claims and war goals over meaningful resource states.
- Diplomacy actions with recognition, compacts, and route-specific refusal logic.
- Survival resource changes and visible mechanic thresholds.
- Achievements for rare and difficult route completion.

## Focus audit requirements

A focus-tree implementation report must include a route coverage table for each archetype and each major country overlay. A branch is missing if it only gives small modifiers, if it lacks decisions, if it has no AI, if it has no visible route consequence, or if it does not interact with survival resources.
