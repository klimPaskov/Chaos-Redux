# Air Cleanliness and Fallout World-End Source Spec, Part 9 Country Package Matrix

Canonical status: accepted baseline design, corrected for independent Fallout ownership and extended by the living-world specs in this package.

Working labels are not final localisation. Public country names in implementation must stay readable map names and should avoid administrative office names as country names.

## Country package rules

Every surviving or spawned country package needs:

- Origin memory, such as continuity, shelter, warlord, mutant, food, port, reactor, or machine.
- State class base, such as bunker city, dead city, greenhouse refuge, port remnant, rail spine, or mutant biosphere.
- Starting leader or council direction.
- Starting politics and ruling party direction.
- Starting ideas with lifecycle.
- Starting units and reinforcement routes.
- Survival resource profile.
- Focus tree archetype plus country-specific overlay.
- Cosmetic tag and flag needs.
- AI route preference.
- Failure state.

## Package template

| Field | Required design |
| --- | --- |
| Spawn condition | Which pre-Fallout state grades, old tag memory, and cause memory create the country. |
| Territory | Core state cluster, claimed nearby ruins, forbidden zones, and fallback capital. |
| Government | Archetype, leader direction, party direction, ideology, and route alternatives. |
| Starting ideas | One to four deep ideas, not a pile of small modifiers. |
| Starting army | Dynamic unit families and source of equipment. |
| Resource profile | Food, water, medicine, scrap, fuel, power, filters, shelter, recognition. |
| Decisions | First survival decisions and unique regional actions. |
| Focus overlay | Country memory branch, local resource branch, and ambition branch. |
| Assets | Flag source mode, leader or council portrait, icon motifs, report images. |
| AI | Preferred routes and route blockers. |
| Failure | How the country fragments, mutates, starves, or is conquered. |

## Continuity government package

| Field | Design |
| --- | --- |
| Spawn condition | Old capital survived as bunker city or old government had continuity protocol. |
| Territory | Capital shelter, nearby administrative states, one old military depot if available. |
| Government | Emergency cabinet, legal continuity council, military caretaker, or technocratic regency. |
| Starting ideas | Broken Mandate, Sealed Archives, Ration Legitimacy. |
| Starting army | State guards, old officers, bunker security, understrength regulars. |
| Reinforcement | Restore registries, recall officers, arm refugees, reopen depots. |
| Resource profile | High recognition, medium power, low food, medium shelter. |
| Decisions | Reissue citizenship, restore courts, ration law, capital reclamation survey. |
| Focus overlay | Old flag memory, charter dispute, claim legitimacy, capital return. |
| Assets | Old flag damaged variant, emergency council portrait, archive and bunker icons. |
| AI | Prefers legal reconstruction if cohesion is high, military emergency if enemies nearby. |
| Failure | Legitimacy collapse creates warlord or bunker splinter. |

## Bunker authority package

| Field | Design |
| --- | --- |
| Spawn condition | Shelter capacity exceeds surface population or capital relocated underground. |
| Territory | Bunker city, tunnel states, mountain or metro adjacent states. |
| Government | Director, shelter council, protocol board, military wardens. |
| Starting ideas | Airlock State, Bunk Rationing, Surface Blindness. |
| Starting army | Security detachments, tunnel guards, engineer cadres. |
| Reinforcement | Train wardens, recruit tunnel scouts, convert shelter workers into militia. |
| Resource profile | High shelter, medium medicine, low food, low diplomacy. |
| Decisions | Open or seal levels, ration air, send surface parties, expand bunks. |
| Focus overlay | Protocol politics, tunnel economy, surface policy, underground nation. |
| Assets | Bunker seal, director or council portrait, animated door seal. |
| AI | Avoids surface wars until food is low or salvage need is extreme. |
| Failure | Shelter riot or air failure creates civil conflict or mass death. |

## Warlord command package

| Field | Design |
| --- | --- |
| Spawn condition | Military depot, state guards, dead city salvage, low legitimacy. |
| Territory | Depot state, road nodes, nearby towns, dead-city edge. |
| Government | Commander, bandit prince, militia oath council, convoy marshal. |
| Starting ideas | Rule of Ammunition, Hungry Followers, Loot Economy. |
| Starting army | Raider infantry, militia trucks, captured artillery if depot survives. |
| Reinforcement | Tribute levies, depot seizures, prisoner recruitment, vehicle raids. |
| Resource profile | High scrap, medium weapons, low recognition, unstable food. |
| Decisions | Demand tribute, raid convoy, seize pump station, absorb gang. |
| Focus overlay | Fear or oath route, tribute roads, crown of ruins ambition. |
| Assets | Scrap crown, militia banner, warlord portrait. |
| AI | Aggressive if food or water deficit can be solved by conquest. |
| Failure | Followers defect or form rival warband. |

## Food compact package

| Field | Design |
| --- | --- |
| Spawn condition | Greenhouse refuge, breadbasket, fishing port, seed vault, or low damage rural cluster. |
| Territory | Food state, water source, defensive town, port if coastal. |
| Government | Ration board, farmers congress, seed council, port granary league. |
| Starting ideas | The Ledger of Mouths, Seed Debt, Farm Guard Autonomy. |
| Starting army | Farm guards, convoy escorts, local rifle clubs. |
| Reinforcement | Recruit harvest guards, trade food for weapons, train convoy militia. |
| Resource profile | High food, medium water, low weapons, high refugee pressure. |
| Decisions | Ration citizenship, protect seed vault, export food, arm grain convoy. |
| Focus overlay | Feed or fortress route, breadbasket federation, refugee covenant. |
| Assets | Greenhouse wheat, ration board portrait, food compact flag. |
| AI | Seeks defense and trade before expansion unless raided repeatedly. |
| Failure | Famine, hoarding revolt, or warlord takeover. |

## Scavenger syndicate package

| Field | Design |
| --- | --- |
| Spawn condition | Dead city with salvage value and weak old authority. |
| Territory | Dead city core, rail yard, scrap fields, market camp. |
| Government | Salvage guild, black market syndicate, auction council. |
| Starting ideas | Everything Has a Price, Unlicensed Medicine, Rust Currency. |
| Starting army | Scavenger infantry, armored cars if scrap is high, tunnel runners. |
| Reinforcement | Buy gangs, convert salvage crews, repair prewar vehicles. |
| Resource profile | High scrap, medium medicine, low legitimacy, variable food. |
| Decisions | Open salvage market, hire escorts, strip factory, sell relics. |
| Focus overlay | Guild law, black market diplomacy, city of scrap ambition. |
| Assets | Salvage guild emblem, masked trader portrait, dead-city icon family. |
| AI | Opportunistic and trade-focused unless threatened. |
| Failure | Corruption coup, gang war, or mutant breach from deep ruins. |

## Technate package

| Field | Design |
| --- | --- |
| Spawn condition | Reactor keep, hydro enclave, old research center, intact industrial bunker. |
| Territory | Power state, lab state, defended worker housing, resource site. |
| Government | Engineer council, reactor priesthood if radical, grid authority, science directorate. |
| Starting ideas | Power Before Bread, Engineer Franchise, Dangerous Core. |
| Starting army | Engineer guards, plant police, technical militia. |
| Reinforcement | Build powered workshops, arm technicians, deploy maintenance brigades. |
| Resource profile | High power, high scrap, low food, high meltdown risk. |
| Decisions | Cool reactor, restart turbine, ration grid, salvage instruments. |
| Focus overlay | Engineer rule, atomic bargain, grid restoration, science caste politics. |
| Assets | Reactor lamp, engineer council portrait, animated warning light. |
| AI | Protects power first and avoids reactor gambles unless desperate. |
| Failure | Meltdown, worker revolt, or military seizure. |

## Mutant polity package

| Field | Design |
| --- | --- |
| Spawn condition | Altered biosphere, extreme radiation, biological or chemical cause memory, failed medicine. |
| Territory | Mutant biosphere, forbidden zone edge, bunker breach, contaminated food cluster. |
| Government | Mutant assembly, changed court, prophet strain, militia brood, medical caste. |
| Starting ideas | Marked Bodies, Human Fear, Adapted Hunger. |
| Starting army | Mutant irregulars, adapted scouts, high-attrition shock units. |
| Reinforcement | Acceptance route recruits citizens, dominance route breeds warriors, containment route trains mixed units. |
| Resource profile | Lower filter need, high isolation, high instability, strange food source. |
| Decisions | Recognition talks, quarantine line, mutation clinics, altered battalions. |
| Focus overlay | Citizen, weapon, faith, or species route. |
| Assets | Fictional flags, generated leaders, animated leader overlay for major reveal. |
| AI | Only pursues extreme species route when high chaos, isolation, or persecution is high. |
| Failure | Purge, internal split, biological collapse, or human crusade. |

## Maritime remnant package

| Field | Design |
| --- | --- |
| Spawn condition | Port remnant, island state, navy survived, coastal food source. |
| Territory | Port, island, fishing waters, fuel depot or dry dock. |
| Government | Port admiralty, island parliament, convoy council, pirate republic. |
| Starting ideas | The Harbor Decides, Salt Rations, Empty Sea Lanes. |
| Starting army | Marines, sailors, port guards, convoy escorts. |
| Reinforcement | Recruit crews, restore dockyard, seize fuel, train boarding parties. |
| Resource profile | Medium food, high trade potential, fuel dependence, refugee pressure. |
| Decisions | Open sea road, quarantine harbor, escort convoy, raid pirate nest. |
| Focus overlay | Rescue, exclusion, piracy, or port federation route. |
| Assets | Port flag, admiral or council portrait, convoy icon family. |
| AI | Trades if safe, turns pirate if food and fuel collapse. |
| Failure | Harbor riot, pirate coup, or disease ship disaster. |

## Machine protocol package

| Field | Design |
| --- | --- |
| Spawn condition | Automated bunker, command network, machine-route event memory, high EMP survival. |
| Territory | Data bunker, factory ruins, power state, guarded human settlement. |
| Government | Protocol state, automated council, human interface committee. |
| Starting ideas | Orders Without Officers, Human Exception Queue, Cold Production. |
| Starting army | Security robots if available, disciplined guards, factory militia. |
| Reinforcement | Restore production lines, reactivate depots, recruit human auxiliaries. |
| Resource profile | High production and defense, low legitimacy, power dependence. |
| Decisions | Reboot node, assign human priority, enforce protocol, override safety. |
| Focus overlay | Human command, machine command, cold caretaker, or extermination protocol route. |
| Assets | Machine seal, council interface portrait, animated monitor. |
| AI | Defensive until power and production are secure, extreme only with hostile neighbours. |
| Failure | Protocol loop, human revolt, or power starvation. |

## Idea lifecycle examples

| Idea | Start | Mitigation | Upgrade | Failure |
| --- | --- | --- | --- | --- |
| Broken Mandate | Continuity starts with low legitimacy | Restore records and ration law | New Charter | Warlord splinter |
| Airlock State | Bunker starts sealed | Expand bunks and public councils | Underground Nation | Shelter Riot |
| Loot Economy | Warlord starts with scrap income and corruption | Oath law route | Tribute Realm | Gang War |
| Seed Debt | Food compact owes food to refugees | Ration citizenship | Breadbasket Federation | Hoarder Coup |
| Dangerous Core | Technate has power and meltdown risk | Cool reactor | Regional Grid | Forbidden Zone |
| Human Fear | Mutant polity has diplomacy penalty | Recognition talks | Changed Citizenship | Purge War |

## Starting force scaling

Each package should define weak, normal, severe, and terminal openings.

| Opening | Meaning | Force principle |
| --- | --- | --- |
| Weak | Low survivable states or low shelter | Small militia and defensive decisions. |
| Normal | One secure state class and one resource source | Defensive army plus one special unit family. |
| Severe | Strong state class but hostile region | Larger starting force, stronger shortages. |
| Terminal | Manual scenario or extreme grade | Strongest weird units or bunkers, but huge resource deficits. |

No country expected to fight should start empty unless the spec explicitly marks it as nonmilitary.
