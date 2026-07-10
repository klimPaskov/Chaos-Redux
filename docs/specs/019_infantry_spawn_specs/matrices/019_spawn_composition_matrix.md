# Event 19 Spawn Composition Matrix

All labels are working design labels unless they are stable system terms.

## Stage coverage

| Stage | Automatic country effect | Typical selected-state behavior | Template logic | Main burden |
| --- | --- | --- | --- | --- |
| Baseline | One generation for every valid country | One division in most selected states | Weighted family archetypes | Audit, equipment debt, local command |
| Evolution I | Better organized generation | Similar state count with larger coherent lots | Stronger archetypes and support | Officer capacity, permanent reserve pressure |
| Evolution II | Serious and strange armies | One or more divisions in high-capacity states | Advanced, mobile, armored, specialist, narrow lots | Supply, fuel, unsupported equipment |
| Evolution III | No normal automatic generation by default | Player or AI requests formation lots | Fully random valid combat and support composition | Absurdity, claimant control, command fracture |
| Evolution IV | Registered Chaos families enter request and spawn pools | Family rules can create separate lots | Registry-gated family templates | Containment, saturation, derivative revolt |

## Diminishing state-coverage targets

| Eligible controlled states | Typical coverage target | Minimum behavior | Design note |
| ---: | ---: | --- | --- |
| 1 to 5 | 90 to 100 percent | Normally at least one state | Microstates feel the event everywhere |
| 6 to 15 | 75 to 90 percent | Smooth transition | Small powers gain broad coverage |
| 16 to 35 | 55 to 75 percent | No hard cap | Medium powers gain many units but visible gaps |
| 36 to 70 | 40 to 60 percent | No hard cap | Major powers receive large absolute armies |
| 71 or more | 25 to 45 percent | No hard cap | Continental empires do not spawn on every state |

The implementation should use a smooth dynamic curve rather than hard jumps at band boundaries.

## State-to-family weighting

| State context | Higher family weights | Main risks |
| --- | --- | --- |
| Capital or administrative center | coherent infantry, reserve staff, support-rich lots | claimant takeover, political leverage |
| Industrial state | artillery, engineers, motorized, armor, golem sustainment | equipment debt, factory burden |
| Rail junction or supply hub | larger and better supplied lots | network congestion, depot seizure |
| Port or naval base | marines, coastal defense, motor transport, foreign-looking equipment | convoy burden, island stranding |
| High population or urban | infantry mass, militia, support, claimant networks | requisition anger, training saturation |
| Mountain | light infantry, pack support, cavalry, mountain-capable elements | low supply, slow standardization |
| Desert | cavalry, camels, motorized patrols | fuel or animal sustainment |
| Jungle | irregulars, light infantry, engineers | disease, low supply, communications |
| Steppe or open plains | cavalry, motorized, armor | fuel and broad-front command |
| Occupied or resistant | local auxiliaries, irregulars, garrisons | defection, local loyalty, mutiny |
| Front-adjacent | higher readiness, combat support | immediate disruption, casualties |
| Remote rear | weaker reserve and local forces | slow audit, transport cost |

## Baseline family matrix

| Family | Combat core | Support direction | Best use | Failure mode |
| --- | --- | --- | --- | --- |
| Local Rifle Cadre | infantry | zero or one basic support | retraining, local defense | understrength line unit |
| Irregular Column | irregular or light infantry | minimal | remote defense, low-supply roles | poor organization and standardization |
| Mounted Patrol | cavalry or camel | minimal reconnaissance | security and mobility | weak against heavy opposition |
| Light Gun Brigade | infantry plus artillery | artillery or logistics | field combat | ammunition and supply burden |
| Support-Rich Reserve | small infantry core | several valid supports | specialist reserve | expensive support on weak core |
| Garrison Shell | one to several infantry | none by default | static role or cadre | negligible field value |

## Evolution I family matrix

| Family | Core identity | Conditional weight | Burden |
| --- | --- | --- | --- |
| Line Infantry Regiment | coherent infantry | stable command and adequate rifles | replacement demand |
| Gun Line Group | infantry and artillery | artillery industry, front pressure | ammunition and supply |
| Mobile Reserve | mounted or motorized | terrain and mobility context | fuel, animals, transport |
| Engineer Reserve | infantry and engineers | rivers, forts, industry, front | support equipment |
| Anti-Armor Detachment | infantry and anti-tank | armored enemy threat | technology and equipment compatibility |
| Air Defense Reserve | infantry and anti-air | bombing or enemy air superiority | anti-air equipment |
| Composite Territorial Division | mixed local defense | broad border or occupation need | limited offensive use |

## Evolution II family matrix

| Family | Example composition direction | Technology behavior | Main decision |
| --- | --- | --- | --- |
| Armored Reserve Group | tanks plus mobile support | initial finite equipment, no unlock | preserve, cannibalize, or reverse engineer |
| Mechanized Column | mechanized or mixed motorized | finite unsupported replacement | field temporarily or standardize |
| Motor Rifle Formation | motorized infantry plus support | normal only if equipment exists | reserve corridor and fuel |
| Assault Gun Group | infantry plus self-propelled support | finite special equipment | concentrate or dismantle |
| Armored Car Screen | armored-car-heavy | narrow but potentially sustainable | security role or retraining |
| Air-Mobile Detachment | valid helicopter-heavy lot | no implicit technology unlock | preserve under strict sustainment |
| Amphibious Reserve | amphibious tanks, marines, or amphibious mechanized | finite if technology absent | coastal deployment |
| Heavy Support Formation | small core and many support companies | equipment-specific | specialist preservation |
| Single-Arm Curiosity | one dominant unusual family | depends on family | accept narrow role or recombine |

## Evolution III random composition bands

| Band | Typical combat battalions | Family behavior | Support behavior | Political risk |
| --- | ---: | --- | --- | --- |
| Coherent | 4 to 18, weighted around practical sizes | one dominant and one compatible secondary | role-matched | low |
| Strained | 4 to 20 | two or three partly compatible families | one mismatch possible | moderate |
| Absurd | 2 to 23 | many unrelated families or narrow extremes | eclectic or overbuilt | high |
| Catastrophic | 1 to 25 | minimal, bloated, or severely incompatible | expensive-on-tiny-core or none-on-huge-core | very high |

The safe final range must be verified against the installed game. The design target is one to 25 combat battalions and zero to five unique support companies.

## Evolution III composition inputs

| Input | Effect on generator |
| --- | --- |
| High Muster Control | raises coherent logic and material-quality weights |
| Low Muster Control | raises absurd and catastrophic weights |
| High Army Congestion | raises bloat, mismatch, and informal-command weight |
| Spaced requests | improves control and cost efficiency |
| Repeated same-generation requests | widens both weak and powerful tails |
| Ask for Numbers | raises battalion and division count, lowers fill |
| Ask for Discipline | lowers count, raises coherence and training |
| Ask for Firepower | raises armor, artillery, anti-tank, anti-air, support |
| Ask for Mobility | raises mounted, bicycle, motorized, mechanized, armored-car, valid air-mobile |
| Ask for Anything | full pool and strongest risk multipliers |
| Active claimant | increases attachment and political-risk weights |
| High saturation | allows registered anomalous results at Evolution IV |

## Initial equipment accounting

| Source model | Use | Constraint |
| --- | --- | --- |
| Stockpile requisition | ordinary compatible equipment | actual stockpile burden |
| Muster debt | large or sudden issue | lowers future reinforcement or production |
| Unidentified finite issue | technology-locked equipment | cannot replenish normally |
| Local industrial requisition | industrial states | temporary factory or construction burden |
| Scenario grant | triggerable setup | must carry scenario balance cost |

## Lot data contract

Every lot needs:

- generation number
- stable local lot index
- origin state or region
- template identity
- division count
- material-quality score
- coherence score or band
- training state
- equipment state and debt
- supply burden
- mobility mismatch
- command owner
- integration state
- claimant link when present
- anomalous family link when present
- closeout state
