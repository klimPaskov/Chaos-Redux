# Event 059 interaction matrix

## Purpose

This matrix identifies deliberate connections with existing Chaos Redux systems and nearby catalog events. Most interactions arise from shared campaign state. Explicit code hooks should be added only when ordinary state cannot express the connection.

| System or event | Connection | Event 059 behavior | Guard against overreach |
| --- | --- | --- | --- |
| Diplomacy cluster | Primary cluster home | High-severity member using the authoritative cluster role, chance, and minimum-tier defaults | Fire-Once removal, one cluster pacing event, no duplicate activation, no separate Diplomatic Panic alias |
| Random War | Creates new legal wars and fronts | Baseline and later layers improve AI conduct inside the generated conflict | Do not add another declaration or refire Random War |
| Fury | Creates aggressive special actors and border wars | Compatible front pressure can assist Fury AI | Fury owner targeting and production rules remain dominant |
| White Peace | Ends selected wars | Event 059 accepts the settlement and remains active for future valid conflicts | No immediate arbitrary redeclaration |
| Tensions Rising | Creates diplomatic hostility and possible frontier pressure | Evolution II can value legal opportunities produced by the event | Hostility text alone is not a war goal |
| A Faction Comes Calling | Creates faction membership and calls | AI can answer useful calls and defend strategic faction interests more readily | Distant or impossible calls remain rejectable |
| Industrial Boom | Raises industrial capacity | Offensive production and operation scale can grow when stockpiles, manpower, fuel, and supply also support it | Factory count alone does not remove safety gates |
| Great Depression 2.0 | Damages production and capacity | Operations narrow, replacement and recovery gain priority | Aggression cannot ignore collapse |
| Acid Rain and natural disasters | Damage states, supply, population, or air conditions | Affected fronts become less feasible until conditions improve | No attack through disaster-driven logistical failure |
| Third Balkan War | Opens a dense regional conflict | AI uses concentration, intervention, and finishing logic on valid fronts | Do not create extra camps or wars |
| The Great Embargo | Creates resource and fuel pressure | Evolution II can value resource-security objectives, while shortages reduce present feasibility | No free war goal against embargo participants |
| Intel Leaked | Provides temporary knowledge of target weakness | Valid rivals can receive a higher opportunity and front-confidence score | Intelligence does not create legal authority |
| Gift from Scientists | Can unlock useful military or logistics technology | AI may use newly feasible equipment through normal production planning | No Event 059 technology grant or forced research path |
| The Great Infrastructure Project | Improves rail and infrastructure | Main-front feasibility can rise where the new network supports it | No unrelated global attack increase |
| The Navy | Provides fleet, convoys, or carrier capacity | Maritime plans and invasions can become viable after full capacity checks | A fleet package does not guarantee supply or home defense |
| The Black Market | Can provide equipment, fuel, convoys, or vehicles | AI buyers can prefer items that close a current offensive readiness gap | Event 059 does not create free purchases or bypass market rules |
| Research Failure | Removes research capacity and can regress equipment | AI must revise force and production plans toward usable technology | No plan may depend on lost technology |
| Return to Peacetime | Converts military capacity and demobilises | Feasibility gates reduce or delay offensive plans until rearmament | The posture remains active but material limits govern behavior |
| Allies Backstab | Expels weak faction members and starts wars | Remaining AI allies can coordinate attacks more actively | Expelled targets do not receive extra enemies from Event 059 |
| Subjects Break Free | Creates independent countries and possible wars | New AI countries inherit active layers and fight according to their capacity | Human-controlled breakaways remain unaffected |
| Independence Wave | Creates or releases ordinary countries | Same dynamic inheritance as other country creation | No duplicate tag or setup ownership |
| Civil wars | Creates new tags and immediate fronts | Each AI side uses valid layers after registration | Human side remains under player control, owner-specific civil-war rules remain valid |
| Special Chaos country registry | Identifies actors with unusual rules | Generic layers apply only when compatible | Hard owner rules and forbidden targets win |
| Event Logs | Shows activation, evolutions, cluster participation | One history entry, ordered evolution entries, correct global actor handling | No duplicate history from player fan-out reports |
| Chaos Meter | Measures first manifestation and later shared consequences | One bounded initial gain, ordinary shared gains afterward | No Chaos for evolution activation and no duplicate war or death gains |
| Multiplayer | Shares global state across players | Every human receives reports, control changes gate behavior | No local random state or desynchronised control flag |
| Event settings | Controls event and evolution eligibility | Event toggle governs pre-fire selection, evolution toggles govern unactivated stages | A post-fire event toggle is not a rollback mechanism |
| Save migration | Preserves old Event 059 state | Map legacy fired state to the new global activation once | No second report, history row, or Chaos grant |

## Explicit hook candidates

Only these connections are likely to need direct integration beyond ordinary campaign state:

1. New-country and release registration when a fully declarative AI plan cannot cover later tags.
2. Special-actor precedence through the existing shared classifier or owner-provider contract.
3. Intel Leaked target confidence, if the intelligence state is not already visible to native AI scoring.
4. Black Market AI purchase priorities, only if that event exposes an owner API for item preferences.
5. Legacy Event 059 save migration.

All other interactions should emerge from current wars, supply, stockpiles, technology, diplomacy, faction state, and target validity.
