# Air Cleanliness and Fallout World-End Source Spec, Part 6 Focus Trees, Decisions, Missions, and AI

Canonical status: accepted baseline design, corrected for independent Fallout ownership and extended by the living-world specs in this package.

Working label, not final localisation: `fallout_focus_tree_framework`.

## Focus tree structure for all countries

Every surviving country gets a Fallout focus tree. The tree may use an archetype base, but the implementation must attach country-specific overlays. A country using a shared tree without unique route names, local decisions, AI weights, and asset direction is not complete.

## Universal opening branch

Every tree begins with a survival opening. The focus names are implementation-owned. The branch roles are:

| Focus group role | Purpose | Rewards and unlocks |
| --- | --- | --- |
| Count the living | Establish population, shelters, and food status | Opens survival interface, sets starting resources. |
| Secure the air | Immediate filters, masks, shelter cycling | Reduces death tick, unlocks filter decisions. |
| Guard the stores | Protect food, medicine, fuel, and scrap | Starts depot missions, adds security units. |
| Choose emergency law | First political split | Locks or leans toward government archetype branch. |
| Restore a route | Pick rail, port, road, or tunnel priority | Unlocks state-targeted reconstruction decisions. |
| Raise first cadres | Starting army fix | Converts militia into usable templates. |

## Archetype branch maps

### Continuity government

| Lane | What it does |
| --- | --- |
| Legal memory | Restores claims, archives, courts, and old advisors. |
| Emergency cabinet | Chooses democracy, military protocol, or technocratic emergency law. |
| Reclamation bureau | Restores state categories and old capitals. |
| Old enemies | Claims against breakaways and warlords, with diplomatic backlash. |
| New charter | Late-game reform that either preserves or rewrites the old state. |

### Bunker authority

| Lane | What it does |
| --- | --- |
| Seal discipline | Shelter capacity, rationing, internal order. |
| Tunnel economy | Underground factories, medicine labs, power. |
| Surface sorties | Salvage and recon missions, high attrition. |
| Protocol politics | Director, council, machine-assisted rule, or revolt. |
| Subterranean nation | Late-game state class transformation and underground formable route. |

### Warlord command

| Lane | What it does |
| --- | --- |
| Arms first | Fast divisions, depot seizures, coercive recruitment. |
| Tribute roads | Convoy raids and forced tolls. |
| Camp followers | Refugee recruitment, black markets, legitimacy problems. |
| Rule by fear or oath | Split between brutal repression and warrior-code cohesion. |
| Crown of ruins | Late-game empire of dead cities and tribute states. |

### Food compact

| Lane | What it does |
| --- | --- |
| Seed and water | Food, greenhouses, irrigation, livestock survival. |
| Ration citizenship | Politics of who eats and who belongs. |
| Defend the farms | Local militias and anti-raid missions. |
| Trade calories | Diplomacy and food leverage. |
| Breadbasket federation | Late-game compact, recognition, and humanitarian empire. |

### Mutant polity

| Lane | What it does |
| --- | --- |
| Name the changed | Defines whether mutants are citizens, caste, army, faith, or ruling body. |
| Altered bodies | Unique units and adaptation ideas. |
| Fear outside | Diplomacy, propaganda, terror, or outreach. |
| Breed true or stay human | Route split between integration, dominance, and containment. |
| New species order | Absurd late-game route with extreme strengths and severe diplomacy. |

### Technate

| Lane | What it does |
| --- | --- |
| Power first | Hydro, reactor, grid, generators. |
| Engineer rule | Council politics and elitism. |
| Salvage science | Dead-city tech, experiments, tools. |
| Atomic bargain | Reactor risk, radiation medicine, nuclear renaissance. |
| Switch the lights on | Late-game grid restoration and power diplomacy. |

## Decision category layout

The post-Fallout decision layer should avoid clutter. Use categories or subviews by task.

| Category | Human use | AI equivalent |
| --- | --- | --- |
| Survival ledger | View resources and first priorities | AI weighted pulse picks resource deficit action. |
| State recovery | Select one or a few states for reconstruction | AI scores states by capital, food, power, and rail. |
| Salvage expeditions | Target dead cities, depots, reactors | AI only uses safe targets unless desperate. |
| Refugee and population | Move, admit, screen, or recruit refugees | AI uses capacity and ideology. |
| Mutant policy | Quarantine, integrate, weaponize, or negotiate | AI based on archetype and pressure. |
| Diplomacy and recognition | Radio treaties, compacts, aid, war claims | AI based on range, resources, and threat. |
| Late ambition | Formables, global projects, extreme routes | AI uses route and high-chaos flags. |

## Mission design examples

| Mission family | Requirement style | Success | Failure |
| --- | --- | --- | --- |
| Hold the waterworks | Place supplied divisions in water states for 120 to 180 days | Clean water rises, local cohesion rises | Disease, unrest, or rival water claim |
| Open the rail spine | Control and repair named route states | Supply and trade route opens | Rail bandits spawn or state class worsens |
| Guard the seed vault | Maintain shelter, power, and units around seed state | Food recovery bonus and achievement tracking | Food compact loses late-game option |
| Reactor cooling watch | Spend water, engineers, and medicine over a deadline | Power increases and radiation burden falls | Reactor keep becomes forbidden zone |
| Dead-city expedition | Commit manpower, medicine, filters, trucks | Scrap, equipment, tech lead | Casualties, mutation, or leader sickness |
| Refugee winter | House a population wave without famine | Manpower, workers, legitimacy | Riot, disease, splinter militia |
| Mutant truce | Keep violence below threshold while talks continue | Mutants become citizens or allies | Mutant rebellion or purge route opens |

## Starting forces

Every survivor country expected to fight receives forces based on its state classes and archetype.

| Source | Unit type direction | Scaling factor |
| --- | --- | --- |
| Bunker city | Security detachments and trained cadres | Shelter capacity and old military presence |
| Dead city | Scavenger infantry and salvage gangs | Scrap and population remnants |
| Food compact | Farm guards and convoy escorts | Food output and rural population |
| Warlord | Raider infantry, trucks, captured guns | Depot control and coercion |
| Technate | Engineer guards and reactor police | Power and labs |
| Maritime remnant | Marine detachments and sailors | Port class and convoys |
| Mutant polity | Mutant irregulars, altered shock troops | Radiation burden and mutant route |
| Continuity | Old army cadres and state guards | Legitimacy and surviving officers |

## AI strategy matrix

| AI context | What it should prioritize | What it should avoid |
| --- | --- | --- |
| Low food | Food states, trade, greenhouse focuses | Long wars unless food objective is critical |
| Low water | Water missions and aquifer wars | Refugee admission without capacity |
| High radiation burden | Medicine and filters, or mutant route if archetype supports it | Ordinary manpower-heavy warfare |
| Warlord neighbour | Fortify, ally, or pre-emptively raid | Leaving depots undefended |
| Strong food compact nearby | Seek trade or conquest depending ideology | Destroying food state unless fanatical |
| Mutant neighbour | Quarantine, negotiate, or purge by ideology | Blind alliance without route support |
| Old capital nearby | Continuity states try reclamation | Far expansion without supply route |
| Island or port state | Convoys and naval survival | Inland conquest without fuel |
| Technate with reactor | Cool and exploit reactor | Meltdown gamble unless desperate |

## Achievement hooks

Achievements should reward difficult route mastery. Scenario launch alone does not qualify.

| Working achievement id | Route | Unlock condition direction | Difficulty |
| --- | --- | --- | --- |
| `fallout_keep_the_lights_on` | Technate | Restore a regional power grid without a reactor meltdown. | Hard |
| `fallout_no_empty_bunks` | Bunker | Survive ten years without shelter riot and with positive population growth. | Hard |
| `fallout_bread_for_the_black_sky` | Food compact | Feed three other countries through compacts while keeping own cohesion high. | Hard |
| `fallout_the_old_flag_still_flies` | Continuity | Reclaim old capital and restore a national charter. | Medium hard |
| `fallout_crown_of_ruins` | Warlord | Unite multiple dead-city regions by force. | Hard |
| `fallout_new_species_order` | Mutant polity | Complete mutant late-game route and force recognition from human states. | Very hard |
| `fallout_no_more_ground_zero` | Any | Clean or stabilize a set number of high-grade wasteland states. | Very hard |
| `fallout_the_sea_roads_open` | Maritime | Build a port compact across three regions. | Hard |
| `fallout_last_seed` | Any | Save a seed vault and use it to restore a major food state. | Medium hard |
| `fallout_after_final_silence` | Final Silence cause memory | Survive the Fallout aftermath as a non-cult successor. | Very hard |

## Focus tree acceptance criteria

The focus-tree layer is incomplete if most countries use the same generic tree, if branches only give modifiers, if no state-targeted decisions are unlocked, if AI lacks route behavior, if mutant countries have no unique routes, if continuity countries cannot decide what the old world means, or if all countries still use normal pre-Fallout diplomacy as their main path.
