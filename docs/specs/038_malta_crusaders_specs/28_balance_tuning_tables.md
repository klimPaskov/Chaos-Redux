# Balance tuning tables

## Status of the values

The numbers below are implementation starting bands. They define relationships, caps, and test cases. They are not permission to scatter values across event, decision, focus, and unit files. Final tuning belongs in script constants or owner-local documented tables after local vanilla, map, technology, equipment, and probability inspection.

Balance must be judged from viable campaigns, not from isolated modifiers. Malta needs enough force to survive its unusual opening, yet nearby countries must retain credible counterplay.

## Script constant groups

| Constant group | Purpose | Main consumers |
| --- | --- | --- |
| `event_038_identity` | event, evolution, scenario, terminal, and package numeric IDs | registry, logs, scenario, Event Details |
| `event_038_setup` | opening package thresholds and bounded grants | release transaction |
| `event_038_values` | Authority, Cohesion, and Legitimacy floors, caps, and thresholds | council, focus, decisions, AI |
| `event_038_orders` | order demand cadence, influence bands, headquarters limits | council runtime |
| `event_038_units` | family caps, equipment ratios, training, sustainment, spawn bounds | unit providers and AI |
| `event_038_campaign` | objective durations, route readiness, war pacing, regional limits | campaign decisions |
| `event_038_principalities` | charter, loyalty, levy, succession, integration | principality runtime |
| `event_038_relics` | expedition cost bands, result weights, custody effects | Evolution III |
| `event_038_evolutions` | minimum Chaos tiers, MTTH anchors, pre-fire packages | evolution scheduler |
| `event_038_teutonic` | negotiation, continuous membership timer, campaign cadence | hidden alliance |
| `event_038_atlantis` | betrayal eligibility, tank cap, replacement cost, regional programs | hidden betrayal |
| `event_038_holy_world` | continent proof, believer alignment, terminal force and war pacing | public world end |
| `event_038_scenario` | four intensity packages and setup limits | triggerable scenario |
| `event_038_ai` | route scores, refusal thresholds, target scores | all Event 38 AI |

## Public mechanic values

All three values use a normalized `0` to `100` display range. Hidden calculations can be more detailed.

| Value | Opening target | Stable band | Warning band | Crisis band | Typical gains | Typical losses | Major thresholds |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Crusade Authority | `45` to `60` by package | `50` to `79` | `25` to `49` | below `25` | held objectives, fulfilled campaigns, centralized command, successful settlements | defeats, abandoned fronts, refused obligations, failed command missions | `25` crisis decisions, `50` ordinary governance, `75` strong centralization, `90` rare high-authority outcomes |
| Order Cohesion | `45` to `65` by package | `50` to `79` | `30` to `49` | below `30` | fair charters, joint command, fulfilled demands, shared victories | favoritism, repeated refusal, territorial disputes, rival headquarters | `30` incident risk, `50` mixed-order operations, `75` confederal strength, `90` exceptional unity |
| Sacred Legitimacy | `30` to `55` by package | `45` to `79` | `20` to `44` | below `20` | Jerusalem custody, relief, Papal support, relic confidence, fair governance | civilian harm, exposed fraud, religious repression, loss of sacred centres | `40` broad religious support, `65` Blessed formations, `80` Papal transformation support, `90` strongest Holy World alignment |

Values should normally move in packets of `3` to `12`. One-point changes are reserved for repeated small ticks that visibly accumulate. A major campaign success or scandal can move a value by `10` to `20` once.

## Opening package bands

| Package | Valid territory count direction | Custom frontline formations | Support or militia formations | Convoy and transport posture | Equipment reserve | Industry and logistics posture | Intended opening balance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline | compact curated footprint | `8` to `14` | `3` to `6` | enough for one primary and one secondary route | `60` to `100` days of expected reinforcement | Malta plus captured ports, bounded temporary construction support | can survive with competent play, cannot overpower every owner immediately |
| Evolution I pre-fire | baseline footprint | `12` to `20` | `5` to `9` | safer two-theatre transport | `90` to `140` days | stronger workshops and order chapters | dangerous regional actor, still vulnerable to major intervention |
| Evolution II pre-fire | broader footprint and one or more valid subjects | `18` to `28` across actors | `8` to `14` | multiple fortified routes | `120` to `180` days | stronger ports, rail, supply, subject production | large regional war with several fronts, no global instant war |
| Evolution III pre-fire | Evolution II footprint plus foreign backing | `24` to `36` across actors | `10` to `18` | robust but finite network | `150` to `220` days | one relic or legitimacy equivalent, stronger support | severe regional crisis with credible coalition counterplay |

Formation counts are total bounded targets, not unconditional free-unit grants. The setup effect must scale for actual state count, population, industry, number and strength of enemies, and whether subject actors exist.

## Custom unit role bands

Exact battalion statistics require local vanilla comparison and technology inspection.

| Family | Intended comparative role | Speed direction | Armour and hardness | Organization | Supply and equipment burden | Main counter | Deployment cap direction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Armored Knights | defensive heavy assault infantry | very slow | high armour for infantry-scale unit, not tank immunity | medium | high support and armour equipment | anti-tank, air power, encirclement, poor terrain | lowest baseline cap |
| Mounted Knights | mobile breakthrough cavalry | medium to high | moderate armour | high | high horses or carrier equipment and support | tanks, anti-tank, fuel or supply strain on advanced variants | moderate cap |
| Archers | low-tech anti-personnel line and support | infantry pace | very low | medium | manpower-heavy, low fuel | armour, artillery, air | high cap with weak penetration |
| Crossbows | stronger defensive ranged formation | infantry pace | low | medium | heavier ranged equipment | armour and mobile breakthrough | moderate to high cap |
| Siege Formations | fort and urban assault support | very slow | low to moderate | low | very high siege equipment and supply | mobile warfare, counterbattery, air | strict per-army and country cap |
| Crusader Engineers | support and specialist formation | follows parent | low | support role | support equipment and engineer tools | combat exposure and equipment shortage | support attachment or small specialist cap |
| Naval Order Infantry | amphibious assault and port defence | infantry pace | low to moderate | high | convoys, naval equipment, support | naval superiority loss, coastal air | tied to ports and naval route |
| Blessed Crusaders | rare elite formation | family-dependent | improved but bounded | very high | expensive legitimacy-gated equipment and replacements | concentrated modern armour and air | strict global cap based on legitimacy and route |
| Mechanized Knight Carriers | late hybrid breakthrough | high | high | high | fuel, vehicles, armour equipment | modern tanks, fuel denial, air | technology and industry cap |
| Supreme Papal formations | terminal force | high but role-specific | extreme relative to ordinary units | very high | terminal industrial and equipment contract | coalition concentration and strategic encirclement | dynamic terminal cap, never infinite |
| Atlantean Supreme armour | hidden elite tank | very high | extreme | very high | exceptional production and fuel cost | air superiority, concentrated modern anti-tank, supply disruption | twenty initial formations, replacements through expensive production only |

## Decision cost bands

No action may have more than four spendable cost types. Every displayed cost needs the matching texticon.

| Action class | Typical cost families | Duration band | Scale factors |
| --- | --- | --- | --- |
| Council arbitration | political power, command power, Authority or concession | instant to `30` days | order count, dispute severity, government route |
| Military preparation | army XP, command power, equipment, fuel | `30` to `90` days | target strength, distance, route, current readiness |
| Port and logistics project | civilian factory burden, trains, convoys, support equipment | `60` to `180` days | state damage, distance, port level, war state |
| Foreign chapter call | convoys, equipment, political obligation, legitimacy | `60` to `150` days | relations, contributor industry, ideology, condemnation |
| Principality charter | Authority, political power, equipment, administrative burden | `30` to `120` days | region size, resistance, local identity, route |
| Integration | civilian burden, Authority, equipment, time | `180` to `540` days | population, resistance, compliance, cultural and political fit |
| Relic expedition | civilian burden, convoys, equipment, intelligence exposure | `90` to `240` days | distance, conflict, competing claimant, route security |
| Eleventh Crusade recovery | equipment, convoys, fuel, civilian burden | `60` to `365` days by stage | surviving cadres, refuge, industry, enemy control |
| Holy World preparation | factories, equipment, diplomatic commitments, legitimacy | `90` to `365` days | continent, aligned countries, opposition, route distance |
| Terminal regional campaign | command, equipment reserves, logistics, contribution burden | rapid scheduled pulses | region strength, fronts, supply, coalition response |

## Order demand cadence

| State | Expected interval | Behavior |
| --- | --- | --- |
| Stable council | `150` to `240` days | one demand drawn from valid active orders |
| High Cohesion | `210` to `330` days | fewer territorial ultimatums, more joint proposals |
| Low Cohesion | `75` to `150` days | stronger demands and incident risk |
| Active major dispute | no second demand | resolve, escalate, or expire current demand first |
| Opening emergency | first demand delayed at least `90` days | player learns the opening war before council pressure peaks |

Demand selection requires a complete valid pool and probability audit. The same demand family should not repeat twice in succession unless no other valid demand exists.

## Mission durations

| Mission family | Easy | Medium | Hard |
| --- | --- | --- | --- |
| Hold named port or capital | `90` to `120` days | `150` to `210` days | `240` to `365` days |
| Secure rail and depot network | `100` to `150` days | `180` to `270` days | `300` to `450` days |
| Protect convoy or pilgrimage | `90` to `140` days | `150` to `240` days | `270` to `365` days |
| Prepare regional offensive | `90` to `150` days | `150` to `240` days | `240` to `365` days |
| Rebuild Eleventh Crusade | `120` to `210` days | `240` to `365` days | `365` to `540` days |
| Principality integration | `180` to `270` days | `300` to `450` days | `450` to `720` days |

Emergency missions may be shorter only when the opening state gives the player enough forces and transport to act immediately.

## Evolution pacing

| Evolution | Chaos gate | Base MTTH direction after Event 38 fired | Pre-fire behavior | Main acceleration | Main delay |
| --- | --- | --- | --- | --- | --- |
| I, The Orders Return | `200+` | about `75` to `135` days | applies immediately as opening package when active before fire | successful campaigns, Catholic support, active orders | Malta near defeat, disabled evolution, no viable actor |
| II, The Crusader Principalities | `400+` | about `100` to `180` days after I | includes I and broader setup | stable conquests, low direct occupation capacity, high Cohesion | no valid regions, collapsing Malta, route disabled |
| III, The Age of Holy War | `600+` | about `120` to `210` days after II | includes I and II plus foreign support | high Legitimacy, Papal relation, visible regional success | exposed atrocity, high condemnation, no foreign support |

Evolution state gives zero Chaos.

## Principality balance bands

Use one hidden loyalty calculation and qualitative status unless a selected-principality detail panel needs an exact number.

| Status | Hidden score direction | Behavior |
| --- | --- | --- |
| Loyal | high | pays levy, supports wars, accepts arbitration |
| Cooperative | moderate positive | fulfils most obligations and requests concessions |
| Guarded | near neutral | selective support, succession and autonomy pressure |
| Defiant | moderate negative | refuses levy, seeks patrons, prepares breakaway |
| Rebellious | low | open crisis, war or negotiated independence possible |

Malta cannot extract full production, manpower, and autonomy benefits from the same principality at once. Charter choices should define the exchange.

## Relic result weighting bands

| Outcome | Calm or low support | High Legitimacy and secure route | Foreign competition or poor security |
| --- | --- | --- | --- |
| credible but unproven object | common | common | reduced |
| disputed object | common | moderate | common |
| deliberate fraud | moderate | reduced | high |
| theft or loss | low | low | moderate to high |
| no discovery | common | reduced | common |
| major public success | rare | uncommon | rare |

The system never confirms supernatural authenticity. Strong effects come from belief, custody, politics, and mobilization.

## Holy World preparation and terminal bands

| Surface | Low normal readiness | Strong readiness | Terminal contract |
| --- | --- | --- | --- |
| Believer alignment | a small network of willing states | several regions with capable members | scenario or terminal setup assigns every normal country |
| Approved continent proof | direct control plus valid Papal subjects, stable for proof window | same rule with stronger administration | mandatory for normal route, bypassed only by manual scenario setup |
| Proof window | `180` to `365` days depending on continent size and war state | cannot be satisfied by transient occupation | lost required territory pauses or resets proof according to exact contract |
| Regional war pulse | one bounded region at a time | two fronts only with strong logistics and AI capacity | rapid but staged pulses, never one fragile all-world effect |
| Believer contribution | capacity-scaled, cooldown-limited | stronger members can provide more | no repeated free-unit farming |
| Terminal force cap | based on controlled population, industry, supply, route, and opposition | large but finite | replenishment requires actual equipment, manpower, or terminal contribution contract |

## Manual scenario intensity bands

| Intensity | Holy World position | Believer share direction | Special formations | Nonbeliever safeguards |
| --- | --- | --- | --- | --- |
| Low | Malta, Rome, Jerusalem, selected nearby footholds | modest minority | compact terminal guard | several strong majors and coherent coalition |
| Medium | stronger Mediterranean position and several subjects | substantial minority | additional Papal and knight formations | strong industrial blocs remain outside |
| High | several regional believer blocs | near parity by capability, not raw country count | large terminal army and multiple active fronts | at least two major opposition centres and meaningful naval capacity |
| Maximum | strongest plausible Holy World setup | believer advantage without guaranteed victory | near upper cap | opposition retains enough industry, manpower, technology, and geography for a real global war |

## Atlantis bands

| Surface | Initial rule | Replacement rule | Counterplay |
| --- | --- | --- | --- |
| Supreme formations | exactly `20` fully equipped elite divisions | slow, expensive, technology and industry gated | air, supply disruption, modern anti-tank, encirclement |
| Program claims | immediate ideological program over defined registries | claims or integration decisions become actual cores only after proof | resistance, occupation cost, lost territory |
| War opening | immediate war with Malta or Holy See and Holy Realm | later regions open through program stages | coalition formation and staged fronts |
| Atrocity policy | immediate existing shared system activation | intensity and enforcement follow occupation and policy | evidence, condemnation, resistance, migration, instability |

## Balance acceptance scenarios

At minimum, test these scenarios through named MCP probability and source audits, then through user-owned live testing:

1. baseline Malta against several ordinary regional owners
2. baseline Malta when one opening owner is a major power
3. Evolution I pre-fire opening
4. Evolution II pre-fire with one principality
5. Evolution III pre-fire with foreign support
6. weak Malta forced into Eleventh Crusade
7. strong Malta using direct rule
8. strong Malta using principalities
9. Papal route with Rome secure
10. Papal route with Rome threatened
11. Teutonic Order with balanced members
12. Atlantis betrayal against a prepared Malta and Holy Realm
13. Holy World normal terminal with minimum valid continent proof
14. each manual scenario intensity
15. multiplayer campaign with human Malta, Germany, and a regional opponent

Any scenario with automatic victory, no viable player action, or repeated free spawning requires retuning before completion.
