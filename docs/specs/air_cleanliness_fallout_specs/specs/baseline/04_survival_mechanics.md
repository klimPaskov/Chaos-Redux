# Air Cleanliness and Fallout World-End Source Spec, Part 4 Fallout Mechanics for Ten More Years

Canonical status: accepted baseline design, corrected for independent Fallout ownership and extended by the living-world specs in this package.

Working label, not final localisation: `fallout_survival_decade`.

## Core post-Fallout loop

The Fallout campaign loop is survival, recovery, mutation, conquest, and memory. A country should have enough to do for another decade.

| Loop | What the player does | What changes |
| --- | --- | --- |
| Survival | Secure food, water, shelter, medicine, power, and routes | Prevents population collapse and keeps industry alive. |
| Salvage | Enter dead cities, reactor ruins, depots, ports, and battlefields | Gains scrap, equipment, fuel, research leads, and danger. |
| Governance | Decide who rules after the old state failed | Unlocks focus routes, laws, leaders, parties, legitimacy, and repression. |
| Mutation | Contain, exploit, accept, or worship altered populations | Unlocks mutant units, risks instability, creates new identities. |
| Reclamation | Rebuild selected states and reopen routes | Restores infrastructure, state category, and population capacity. |
| War | Fight over water, seed banks, bunkers, reactors, ports, and old capitals | Changes map and can create new country identities. |
| Memory | Decide what the old world means | Affects legitimacy, diplomacy, achievements, and final endgame. |

## Survival resources

Fallout needs resources that matter. These can be variables shown in a custom interface, decision category, or national spirit tooltips.

| Resource | Main source | Spent on | Failure consequence |
| --- | --- | --- | --- |
| Food | Greenhouses, rural refuges, fishing ports, stockpiles | Population survival, army supply, diplomacy | Famine deaths, riots, cannibal routes, refugee flight |
| Clean water | Rivers, aquifers, desalination, mountain snow | Medicine, population, farming | Disease, unrest, migration, mutant exposure |
| Medicine | Hospitals, labs, salvage, foreign doctors | Radiation sickness, plagues, leader survival | Death ticks, commander loss, mutation events |
| Scrap | Dead cities, factories, battlefields | Buildings, weapons, vehicles, filters | Industry stagnation and weak army growth |
| Fuel | Oil states, synthetic plants, scavenging | Convoys, vehicles, generators | Immobilized armies and dead power grids |
| Power | Hydro, reactors, coal, wind, generators | Greenhouses, labs, bunker life | Shelter collapse, food loss, night raids |
| Filters | Factory output, treaty stockpiles, scavenged masks | Clean-air states and armies | Higher deaths and attrition |
| Shelter capacity | Bunkers, tunnels, converted factories | Population protection | Shelter riots and preventable deaths |
| Recognition | Radio, envoys, old legitimacy, relief | Diplomacy, alliances, trade | Isolation and warlord stigma |

## Accepted opening survival ledger

Every state receives a frozen 0 to 100 opening score for the nine resources above. Every successor receives an immutable `initial` profile and a separate mutable `current` profile. The opening calculation uses only transition receipts from Air Winter, state grading, population loss, permanent building loss, supply collapse, frozen deposits, frozen specialty buildings, frozen state category, and finalized successor ownership.

For each state resource, weighted normalized components sum to a numerator between 0 and 10,000. The denominator is 100. The state score is rounded once after the final division and clamped to 0 through 100. Air Winter not-applicable states receive a typed zero row and do not enter country coverage, population weight, or hub selection.

| Resource | Accepted weighted components |
| --- | --- |
| Food | 45 Food Reserve, 20 rural identity, 10 port capacity, 10 Reclamation, 15 Access |
| Clean water | 50 Water Security, 15 Shelter Capacity, 15 logistics, 10 Adaptation, 10 Access |
| Medicine | 25 urban identity, 25 surviving industry, 20 Recovery, 15 Adaptation, 15 Access |
| Scrap | 35 salvage, 20 surviving industry, 20 material deposits, 25 Access |
| Fuel | 50 fuel source, 20 logistics, 15 surviving industry, 15 Access |
| Power | 50 power source, 20 surviving industry, 15 logistics, 15 Access |
| Filters | 40 surviving industry, 20 Shelter Capacity, 15 Adaptation, 10 Reclamation, 15 Access |
| Shelter capacity | 55 Shelter Capacity, 15 logistics, 10 urban identity, 10 Adaptation, 10 Access |
| Recognition | 35 communications, 25 administrative identity, 15 urban identity, 15 Recovery, 10 Access |

Country coverage uses each produced state's unrounded score and a survivor-population weight of `fallout_population_after_loss_k / 1000`, clamped from 0.001 to 8. The strongest unrounded state score supplies the hub term. Food, Clean water, Medicine, Filters, and Shelter capacity blend 90 percent coverage with 10 percent hub. Scrap, Fuel, and Power blend 75 percent coverage with 25 percent hub. Recognition blends 70 percent coverage with 30 percent hub.

Government archetype modifies only final Recognition. It cannot create physical resources. Region and country memory apply no hidden opening bonus. Their later effects must come from manually reviewed focus, decision, event, and package content. The complete coefficient contract and arithmetic proof are recorded in `docs/plans/air_cleanliness_fallout_plans/FALLOUT_SURVIVAL_NUMERICAL_CONTRACT_PROPOSAL.md` and `FALLOUT_SURVIVAL_NUMERICAL_TRANSACTION_PROOF.md`.

## State classes after Fallout

The world map should feel new. State classes replace ordinary state identity as the main strategic layer.

| Fallout class | What it means | Strategic role |
| --- | --- | --- |
| Bunker city | Old command center or shelter network survived | Government core, high shelter, low food |
| Dead city | City destroyed but salvage-rich | Equipment source, high danger, low population |
| Greenhouse refuge | Protected agriculture and controlled air | Food engine, vulnerable target |
| Ash farm | Rural land under dim sky | Weak food, local manpower, disease risk |
| Scavenger badlands | Sparse ruins and roads | Irregular armies, convoy raids, scrap |
| Forbidden zone | Extreme radiation or impossible terrain | Rare salvage, mutants, research, death |
| Mutant biosphere | Biological or altered ecology dominates | Mutant countries, strange resources, hostile spread |
| Port remnant | Harbor still functions | Trade, refugees, piracy, naval recovery |
| Hydro enclave | Power system survived | Electricity, diplomacy, strategic target |
| Reactor keep | Reactor or atomic facility survived | Power and science, meltdown risk |
| Rail spine | Key route still passable | Logistics, war goals, regional federation path |

## Survival decisions

Decision families should be actionable and costly. Political power alone is not enough.

| Family | Example actions | Costs and risks | Long-term payoff |
| --- | --- | --- | --- |
| Shelter life | Expand bunks, ration air, seal lower tunnels | Support equipment, manpower, stability | Higher population survival and bunker legitimacy |
| Greenhouse command | Convert factories, protect glass, assign grow-lights | Civilian factories, power, fuel, water | Food production and political legitimacy |
| Salvage expeditions | Dead-city crawl, depot recovery, reactor entry | Manpower, trucks, medicine, filters | Scrap, equipment, tech, leader traits |
| Water wars | Secure aquifer, repair pump, escort convoy | Infantry equipment, fuel, divisions in states | Water supply and war goals |
| Radiation medicine | Iodine stockpiles, bone marrow clinics, triage boards | Medicine, support equipment, stability | Lower deaths and mutation risk |
| Refugee policy | Admit, screen, recruit, or expel | Food, shelter, stability, ideology pressure | Manpower, advisors, route shifts, unrest |
| Mutant policy | Quarantine, integrate, weaponize, worship | Medicine, legitimacy, command power, ethics risk | Mutant units or containment stability |
| Old-world archives | Restore records, burn archives, use propaganda | Power, scholars, stability | Claims, legitimacy, focus route unlocks |
| Convoy corridors | Open road, arm escorts, build radio posts | Fuel, trucks, infantry equipment | Trade, diplomacy, expansion missions |
| Reactor discipline | Cool core, strip parts, restart plant | Engineers, water, medicine, risk | Power, nuclear research, meltdown danger |

## Special mechanics

### Survival Cohesion

A country-level value that measures whether the surviving population still accepts the government. It rises from food security, shelter fairness, successful missions, and old legitimacy. It falls from famine, shelter riots, failed expeditions, forced labour, and mutant persecution.

Cohesion unlocks reforms, integration, diplomacy, and higher manpower. Low cohesion unlocks coups, cult routes, warlordism, and splinter states.

### Radiation Burden

A country and state value that measures accumulated exposure. High burden increases deaths, mutation events, attrition, and leader sickness. It can also unlock radical routes and mutant units.

### Reclamation Capacity

A country value showing ability to restore state categories and rebuild. It depends on engineers, power, scrap, rail, and focuses. It controls how many states can be actively restored at once.

### Old World Memory

A country value or route identity. Some countries worship the prewar state. Some reject it. Some use it as a legal claim. Some mutate it into cults, protocols, or myths. Memory shapes focus trees, diplomacy, achievements, and cosmetic names.

## Government archetypes

Every surviving country receives a government archetype. The archetype sets focus tree lanes, laws, decisions, leader types, and AI behaviour.

| Archetype | Identity | Strong gameplay | Weakness |
| --- | --- | --- | --- |
| Continuity government | Claims legal survival from pre-Fallout state | Legitimacy, archives, old officers | Brittle politics and old enemies |
| Bunker authority | Shelters and protocols rule | High defense, shelter capacity, tech | Low food, authoritarian pressure |
| Warlord command | Armed survival hierarchy | Fast armies, raids, conquest | Low legitimacy, faction instability |
| Food compact | Farmers, ports, and ration boards lead | Food, diplomacy, refugees | Weak early military |
| Scavenger syndicate | Salvage guilds and convoy gangs | Scrap, mobility, black markets | Corruption and weak institutions |
| Technate | Engineers and reactor crews rule | Power, labs, reclamation | Meltdown risk and elitism |
| Mutant polity | Altered populations form a state | Unique units and adaptation | Isolation, fear, instability |
| Religious refuge | Faith institutions become government | Cohesion and morale | Technology suspicion or zealotry |
| Quarantine republic | Medical and police rule | Disease control and medicine | Civil liberties conflict, low diplomacy |
| Maritime remnant | Ports and ships preserve order | Trade, naval recovery, refugees | Fuel dependence and piracy |
| Nomad convoy | Mobile government around routes | Evasion, raids, trade | Hard to hold cities |
| Machine protocol | Automated or semi-automated command survives | Production and defense | Human legitimacy crisis |

## Mutant countries

Mutant countries are fictional Chaos Redux content. Radiation can damage genetic material in reality, but immediate organized mutant polities are not realistic. The mod should treat them as high-chaos Fallout fiction caused by radiation, biological disasters, chemical saturation, secret projects, and world-end weirdness.

| Mutant polity working label | Spawn conditions | Gameplay identity |
| --- | --- | --- |
| Glassborn March | Vitrified zones near major cities | High attrition immunity, low diplomacy, glass-scar units |
| Pale Commonwealth | Bunker populations with high radiation burden | Strong shelter governance, weak sunlight warfare |
| Cobalt Apostles | Reactor keeps and cult memory | Radiation weapons, dangerous stability |
| Underpeople | Metro, tunnel, and bunker states | Urban defense, underground expansion |
| Mycelial League | Biological cause memory plus wet regions | Spread through forests and ruins, food through fungus |
| Strontium Children | High child-survivor events and medicine failure | Morale horror, unique youth militia debate, high instability |
| Rad Shepherds | Rural fallout and livestock mutation | Mobility, ash farms, strange cavalry or beast units |
| Chrome Choir | Machine protocol plus altered humans | Production and obedience, low manpower freedom |
| Black Lung Confederacy | Chemical saturation and industrial ruins | Gas resistance, toxic infantry, poor diplomacy |
| Glow Court | Old capital with extreme exposure | Prestige, fear, elite mutated guard, assassination risk |
| Bone Orchard | Mass graves and biological memory | Manpower from death cult mechanics, severe diplomatic hatred |
| Saltwater Changed | Island fallout and contaminated seas | Amphibious raiders, fishing mutations, disease risk |

## Country focus-tree archetype package

Every country gets a focus tree. To make this feasible without creating thousands of hand-built trees, Fallout should use archetype trees with mandatory country-specific overlays. A country may share an archetype skeleton, but it must not play or read as generic.

Each focus tree contains:

1. Opening survival branch.
2. Government route branch.
3. Food, water, and shelter branch.
4. Military and militia branch.
5. Reclamation or mutation branch.
6. Diplomacy and recognition branch.
7. Expansion or route-control branch.
8. Late-game ambition branch.
9. Country-specific memory branch based on old tag, region, capital, cause memory, and state classes.

## Late-game ambitions

After ten years, a successful Fallout country should have absurd ambitions.

| Ambition | Who pursues it | Payoff |
| --- | --- | --- |
| Rebuild the world map | Continuity and food compact states | Restore categories, create a new world organization, suppress warlords. |
| Rule the ruins | Warlords and scavenger syndicates | Conquest, forced tribute, dead-city empire. |
| Seal the surface | Bunker and machine protocol states | Underground megastate, low diplomacy, high survival. |
| Become the new species | Mutant polities | Mutant formables, adaptation, global fear. |
| Light the reactors | Technates | Power grid restoration, nuclear renaissance, meltdown risk. |
| Burn the old names | Religious, cult, and radical refuges | New ideology family, old tags erased, high cohesion or fanaticism. |
| Open the sea roads | Maritime remnants | Port federation, convoy world, piracy suppression or empire. |
| Green the black soil | Food compacts and greenhouse refuges | Food victory, population recovery, diplomatic leverage. |

## Acceptance criteria

Fallout is not complete unless normal post-1936 gameplay is meaningfully replaced. Old country trees should not remain unchanged. Old diplomacy should not remain the main diplomatic system. State classes, survival resources, new decisions, new focus trees, new governments, and new country identities must appear everywhere.
