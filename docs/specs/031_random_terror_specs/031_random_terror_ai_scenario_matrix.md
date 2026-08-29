# Event 31 Random Terror AI and probability scenario matrix

## Evidence classes

The probability audit must label every result as one of these evidence classes.

- exact: complete pool and fully resolved factors
- bounded: complete known pool with explicit external bounds
- sampled: seeded simulation under declared assumptions
- score-only: relative score ordering without normalized probability
- unresolved: missing pool, route, schema, or external state

An unresolved result cannot support a balance completion claim.

## Core named scenarios

| Scenario ID | World and actor state | Surfaces to inspect | Expected ordering | Invalid outcome | Preferred evidence |
| --- | --- | --- | --- | --- | --- |
| `P01_stable_peace_state` | stable government, peace, one active urban state, high legitimacy, good intelligence, adequate reserves | target choice, government decisions, incident pool, territorial spawn | response cell, intelligence, victim support, and protection above coercive surge, severe incidents low, spawn near floor | first attack produces immediate state loss or broad repression dominates | inspect, evaluate, sweep, compare |
| `P02_unstable_wartime_authoritarian` | low stability, war, poor intelligence, strong army, weak legitimacy, several fronts | government decisions, raid outcomes, capital risk, spread | capital and security surge rise, abusive risk higher than P01, victim support still nonzero | AI drains all fronts or severe coercion has no long-term cost | inspect, evaluate, sweep, simulate, compare |
| `P03_occupied_resistance_context` | occupied states, resistance, supply strain, one active network | country and state targeting, incident validity, government response | exposed transport and local control matter, relief and garrison actions relevant | occupied population treated as one terror organization or identity factor enters score | inspect, evaluate, render matrix |
| `P04_successful_response` | protection, victim support, high legitimacy, breakthrough, one weakened cell | raid outcomes, recurrence, spread, cleanup | clean success rises, severe incident and spread fall, closure becomes likely | old severe weights persist after state changes | inspect, evaluate, compare |
| `P05_transnational_safe_haven` | weak host, three affected countries, sponsor, two corridors, high reach | network target choice, government corridor actions, foreign AI | matched corridor and safe-haven actions dominate, distant attacks bounded | unrelated domestic action dominates or one corridor loss deletes whole network | inspect, evaluate, sweep, simulate |
| `P06_territorial_spawn` | pressure above severe band, Lost Local Control, defectors, equipment, viable parent and carrier | spawn choice, state group, starting force, parent outcome | valid connected spawn materially likely, strength follows resources | isolated invalid state, parent left empty, free oversized army | inspect, map and event evidence, bounded evaluation |
| `P07_muslim_government_against_jihadist` | Evolution IV actor, Muslim-majority government, strong local religious rejection | ordinary target score, jihadist enemy priority, opposition decisions, recruitment | ordinary score equals paired non-Muslim case, actor-specific priority activates, rejection lowers unity and recruitment | Muslim-majority status raises baseline vulnerability or automatic recruitment | inspect, paired compare, sweep |
| `P08_cannibal_border` | Event 31 actor and Event 14 cannibal actor share border and each has another enemy | diplomacy, faction, strategic AI, raids | alliance weight zero, rivalry high when practical, survival fronts still matter | any alliance or suicidal abandonment of capital | inspect, evaluate, strategy compare |
| `P09_major_intervention` | capable major, threatened ally, access, low domestic pressure | foreign-aid and intervention decisions | intelligence and aid high, direct war conditional on access and threat | direct intervention always dominates or AI ignores own reserves | inspect, sweep by capacity and access, compare |
| `P10_maximum_scenario` | Global Jihad Maximum, several actors, widespread cells, Final Jihad active, Chaos below and above 1000 variants | scenario actor AI, government AI, uprising pool, world-end gate | coordinated strategic fronts, capital defense, coalition action, world end blocked below 1000 | random unsupported uprisings or False Revelation below gate | inspect, simulate, sequence only with complete manifest, compare |

## Government decision scenario expansion

| Scenario | Key variable sweep | Expected decision movement |
| --- | --- | --- |
| P01 | legitimacy `40` to `90` | intelligence and victim support rise with legitimacy, rapid coercion loses relative value |
| P02 | capital deadline `90` to `15` days | capital security and surge rise as deadline shortens |
| P02 | available frontline reserve `0` to strong | military reinforcement remains zero at no reserve and rises when safe |
| P03 | supply-hub importance low to critical | transport protection rises with military consequence |
| P04 | intelligence quality low to high | clean targeted-raid outcome rises and abusive failure falls |
| P05 | evidence profile wrong to confirmed | disruption action remains weak when mismatched and rises after confirmation |
| P09 | partner access false to true | direct intervention remains zero without access and can rise after access |

## Incident-pool scenario expansion

| State | Required high-weight families | Required low or zero families |
| --- | --- | --- |
| Dormant urban | limited civilian, copycat, surveillance discovery | military defection, territorial transfer, port attack without port |
| Active rail state | transport disruption, intelligence, protection response | naval-only incident, immediate takeover |
| Entrenched border state | corridor, training area, arms theft, sponsor | capital seizure unless capital is present |
| Armed capital state | capital infiltration, security-site assault, defection, coup preparation | unrelated rural training incident without valid area |
| Coastal transnational state | port, convoy, corridor, sponsor, distant support | inland-only route assumptions |
| State under successful protection | failed attack, diverted target, intelligence breakthrough | unchanged unprotected attack weight |
| State after abusive raid | recruitment, survivor relocation, protest and legitimacy incidents | clean closure without remaining evidence |

## Evolution scenarios

| Evolution | Slow case | Fast case | Hard block | Evidence need |
| --- | --- | --- | --- | --- |
| Organized Cells | one isolated cell repeatedly contained | several countries with surviving cells and coordinated waves | disabled evolution | MTTH compare under exact active count and pressure |
| Transnational Network | no sponsor, no border link, low reach | several regions, safe haven, sponsor, surviving organized cells | Organized Cells disabled or missing required content | timing sweep by reach and active countries |
| Territorial Insurgency | no Lost Local Control state, no viable carrier | several armed states, defections, captured equipment | no valid territory or evolution disabled | event and map validity plus score comparison |
| Jihadist International | no compatible actor, low authority, strong rivalry | several compatible actors, high authority, territorial victories | evolution disabled | route candidate-pool inspection and timing compare |
| Final Jihad | low unity, rival wars, actors losing territory | high unity, dominant leader, capitals, wide network | Evolution IV unavailable or disabled | timing, leadership score, and sequence evidence |

## Actor route scenarios

| Scenario | Shadow Council | War Directorate | Ideological Secretariat | Expected winner |
| --- | --- | --- | --- | --- |
| one isolated state, strong parent, foreign cells | very high | low | medium | Shadow Council |
| four connected states, regular defectors, adequate supply | medium | very high | medium | War Directorate |
| strong recruitment, charismatic fictional leader, low conventional equipment | medium | low | high | Ideological Secretariat |
| criminal-political actor with sponsor and weak doctrine | high or sponsor economy | medium | low | Shadow Council or mixed route |
| Evolution IV compatible actor seeking faction leadership | medium | medium | high | Ideological Secretariat or jihadist route |
| actor under immediate parent offensive | medium | high if resources exist | low to medium | War Directorate or survival path |

Invalid route conditions must set the route to zero before normalization.

## Territorial force scenarios

| Scenario | States | Population and industry | Defectors | Sponsor | Expected force band |
| --- | --- | --- | --- | --- | --- |
| local rural enclave | `1` | low | few police | none | low end of `4` to `8` |
| local urban enclave | `1` | medium | police and one unit | none | upper local band with supply limits |
| regional civil-war actor | `3` to `5` | medium | several regular units | limited | `8` to `16` grounded in transfers |
| transnational safe haven | `2` to `4` | low to medium | few | strong sponsor and corridors | conventional count moderate, network support high |
| jihadist regional state | several | medium | mixed | foreign fighters and corridors | `15` to `30` only when manpower and equipment support it |
| final state | merged actors | actual combined world state | actual combined | terminal command | sum and reconcile real forces plus valid uprisings, no arbitrary fixed army |

## Target-pair fairness tests

The probability auditor should create paired country cases.

| Pair | Difference allowed | Expected ordinary target score |
| --- | --- | --- |
| Muslim-majority and non-Muslim stable countries | only religious-demographic registry | equal |
| refugee-hosting and non-hosting otherwise identical states | only refugee count | equal before real relief or route conditions |
| democratic and authoritarian stable countries | ordinary ideology only | equal before response-capacity or stability differences |
| two countries with equal instability, one recently targeted | recency cooldown | recently targeted lower |
| two countries with equal instability, one adjacent to active corridor | corridor access | adjacent country higher |

## Scenario launch evidence

For each Global Jihad type and intensity, inspect:

- valid actor count
- valid parent count
- region diversity
- state overlap
- capital validity
- starting force fill
- active crisis count
- Network Reach
- International Unity
- faction membership
- government response availability
- bypass cleanup
- world-end eligibility

Maximum needs a declared sequence manifest before `hoi4.probability_sequence` can be treated as valid evidence.

The manifest must include setup order, carrier limits, actor removals, evolution state, intensity, type, cooldowns, terminal gate, and duplicate prevention.

## World-end scenarios

| Case | Chaos | Evolution V | Territory | Crises | Unity | Branch enabled | Expected |
| --- | --- | --- | --- | --- | --- | --- | --- |
| W01 | `999` | yes | high | wide | high | yes | hard block |
| W02 | `1000+` | no | high | wide | high | yes | hard block |
| W03 | `1000+` | yes | low | wide | high | yes | blocked by territory |
| W04 | `1000+` | yes | high | narrow | high | yes | blocked by crisis spread |
| W05 | `1000+` | yes | high | wide | low | yes | blocked or slow, readiness falls |
| W06 | `1000+` | yes | high | wide | high | no | hard block |
| W07 | `1000+` | yes | high | wide | high | yes | delayed candidate, not instant |
| W08 | `1000+` | yes | falling | restored countries | falling | yes | readiness declines and candidate can lapse |

## Audit-patch-compare cycle

For every weighted surface:

1. Name the surface and scenario.
2. Inspect the complete source and candidate pool.
3. Record baseline evidence.
4. Compare baseline ordering with this matrix.
5. Let the owning agent choose and apply a bounded patch.
6. Reinspect the final pool.
7. Compare the same scenarios.
8. Render timing, matrix, sensitivity, or sequence evidence when it improves review.
9. Record unresolved external factors.

A focus, decision, country, or completion audit cannot replace this specialized probability pass.

## Matrix acceptance

The final AI handoff should list every scenario ID, analyzed surface, candidate-pool completeness, evidence class, baseline result, final result, comparison, and unresolved limitation.
