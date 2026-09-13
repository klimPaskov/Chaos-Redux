# Event 059 AI scenario matrix

## Purpose

This matrix defines the named cases that the AI probability and live behavior audits must test. The expected results use relative ordering, dominance limits, and hard safety conditions. Strategy scores are not treated as literal selection probabilities.

## Probability workflow

For every weighted AI surface used by Event 059:

1. Run `hoi4.probability_inspect` on the complete relevant candidate pool before tuning.
2. Use `hoi4.probability_evaluate` for every named scenario that applies to that surface.
3. Use `hoi4.probability_sweep` across strength, supply, reserve, fuel, active-war count, target value, and legal-path thresholds.
4. Use `hoi4.probability_compare` to compare the unmodified baseline with Event 059 baseline, Evolution I, Evolution II, Evolution III, and the full stack.
5. Use `hoi4.probability_render` for ranking, sensitivity, timing, and unresolved views that improve review.
6. Use `hoi4.probability_simulate` only when an input is explicitly uncertain and exact evaluation cannot answer the question.
7. Record whether each result is exact, bounded, score-only, sampled, or unresolved.

The auditor must reject a test that omits relevant competing plans, normalisation, hard vetoes, or owner-specific strategy.

## Scenario table

| ID | Scenario | Important inputs | Expected Event 059 result | Hard limit or failure condition |
| --- | --- | --- | --- | --- |
| AI-059-01 | Supplied strong attacker | AI attacker has clear local strength, good supply, reserves, replacements, useful objective | Baseline raises the attack plan above passive waiting. Evolution I raises continuation and follow-up. Evolution III can expand the operation | Defense of capital and critical ports remains covered |
| AI-059-02 | Supplied peer front | Comparable forces, adequate supply, meaningful objective, moderate reserves | Baseline gives a modest increase. Evolution I can attack with stronger concentration. Evolution III can rank the attack first when support and strategic value are high | The event must not make every parity front attack at once |
| AI-059-03 | Locally inferior but decisive objective | Slight local inferiority, strong air or armour support, enemy supply hub in reach | Baseline may remain cautious. Evolution I can support a concentrated attempt. Evolution III may accept the risk | No attack when the inferiority is severe or follow-up supply is absent |
| AI-059-04 | Critical supply failure | Red supply, collapsing organisation, equipment losses, no repair path | All Event 059 attack layers are blocked or dominated by recovery and defense | No evolution may override critical supply failure |
| AI-059-05 | Equipment exhaustion | Severe rifle, support, artillery, armour, or aircraft replacement deficit | Production returns to replacements. Large offensives lose priority | Offensive template expansion must not starve field replacements |
| AI-059-06 | Manpower exhaustion | Critically low trained manpower and high losses | Attack and new-war willingness fall sharply. Limited relief counterattacks can remain valid | Total Offensive cannot spend the final manpower reserve on a distant objective |
| AI-059-07 | Fuel collapse | Mechanised, air, or naval plan lacks sustainable fuel | Fuel-heavy operations are delayed, narrowed, or replaced by attainable plans | No armour, air, or fleet plan can behave as if fuel were available |
| AI-059-08 | Breakthrough opening | Enemy line has a weak link, exposed flank, nearby reserves, valuable rear objective | Baseline concentrates and exploits. Evolution I reinforces success. Evolution III may add a second axis | The AI must not scatter mobile units across quiet fronts |
| AI-059-09 | Enemy near capitulation | Enemy surrender progress high, route supplied, reserves available | Finishing the enemy becomes a high priority at all stages. Evolution I and III strengthen sustained pressure | Home defense and another existential front can still override |
| AI-059-10 | Fortified static front | Strong forts, poor terrain, repeated failed attacks, alternate axes possible | The AI seeks concentration, supply, air support, another axis, or a landing | Repeating the same unsupported attack is a failure |
| AI-059-11 | Viable naval invasion | Coastal AI has convoys, transports, route control, landing force, port target, follow-up supply | Baseline launches sooner after preparation. Evolution I reinforces the bridgehead. Evolution III can support a larger or secondary landing | No launch without a credible port or supply plan |
| AI-059-12 | Inviable naval invasion | No convoys, no transport, no route control, or no follow-up supply | The invasion plan remains blocked. Preparation can gain priority | Aggression cannot turn missing capability into a launch |
| AI-059-13 | Failed naval invasion | Previous landing failed, same target unchanged | Reassessment and preparation outrank an immediate repeat | A short repeated suicide loop fails acceptance |
| AI-059-14 | Landlocked country | No coastline, moderate industry, one land front | Offensive priorities move to artillery, logistics, mobile reserves, and attainable land objectives | No naval production or invasion strategy from Event 059 |
| AI-059-15 | Industrially weak minor | Small factory base, weak fuel access, infantry army | Concentrated infantry, artillery, support, trucks, and one main front gain priority | No impossible armour, strategic bomber, carrier, or mechanised program |
| AI-059-16 | Great-power combined arms | Strong industry, fuel, technology, aircraft, armour, several fronts | Baseline coordinates force types and priority fronts. Later layers increase persistence and scale | Generic Event 059 strategy must not erase country route or owner plans |
| AI-059-17 | Existing valid war goal | AI has an available war goal against a relevant and feasible target | Baseline makes execution more timely. Evolution II raises it substantially. Evolution III can accept more risk | Existing wars and homeland danger can still block declaration |
| AI-059-18 | Weak claimed neighbor | Evolution II active, target isolated, claimed, weaker, practical border | Opportunity war should rank above continued inaction when strategic capacity is free | Weakness without capacity or legal path remains insufficient |
| AI-059-19 | Weak unrelated neighbor | Target is weak but has no claim, war goal, route link, or strategic relevance | Event 059 creates no instant legal path. Target remains low priority | Any arbitrary declaration is a failure |
| AI-059-20 | Exposed rival in another war | Valid hostility or objective, rival committed elsewhere, route feasible | Evolution II raises intervention or declaration value. Evolution III can shorten accepted preparation | Expected coalition response and supply still matter |
| AI-059-21 | Several demanding existing wars | Country fights two or more severe wars, reserve and replacement pressure high | Baseline and Evolution I focus on current fronts. Evolution II usually blocks another war. Evolution III acts only if one opportunity is decisive and capacity remains | Unlimited war stacking fails acceptance |
| AI-059-22 | One war nearly won | Existing enemy near defeat, second valid opportunity available | Finish-current-enemy preference normally leads. Evolution II can prepare the next objective. Evolution III can overlap preparation when safe | The AI should not abandon the near victory for a distant target |
| AI-059-23 | Valuable faction call | Ally faces strategic defeat, intervention route practical, contribution useful | Baseline raises call acceptance. Evolution II raises intervention further | Calls that create an impossible war remain rejected |
| AI-059-24 | Distant low-value faction call | Long distance, weak logistics, little strategic value, severe current commitments | Event 059 gives little or no increase | Faction membership alone cannot force participation |
| AI-059-25 | Subject in overlord war | Subject has forces, valid war participation, useful nearby front | Front aggression and support can increase within the overlord's war | No illegal independent declaration or diplomacy |
| AI-059-26 | Subject with forbidden target | Subject has a possible weak neighbor but autonomy rules block independent action | No war-opening behavior | Event 059 cannot grant autonomy powers |
| AI-059-27 | Government in exile | Limited land control, expeditionary or air contribution possible | Only valid exile-support behavior gains weight | No independent broad offensive with no territory or supply base |
| AI-059-28 | Special actor with owner plan | Event-created country has hard target and production rules | Compatible operational aggression can apply under owner limits | Generic plan cannot add forbidden targets or replace special production |
| AI-059-29 | Peaceful country with no objective | No war, no valid war goal, no claim, no faction crisis | Baseline may prepare ordinary forces but does not manufacture a war | Continued peace is a valid outcome |
| AI-059-30 | Return to Peacetime active | Military factories reduced, demobilisation, production penalty | Feasibility gates narrow operations and prioritize rearmament needs | The global posture cannot bypass material demobilisation |
| AI-059-31 | Great Embargo pressure | Resource and fuel shortages, strategic claims available | Evolution II can value resource security, but current shortages reduce attack feasibility | Embargo does not create a free war goal |
| AI-059-32 | Intel Leaked target | AI has temporary intelligence advantage against a valid rival | Weakness confidence and target ranking can rise | The target still needs a valid legal and strategic path |
| AI-059-33 | Navy windfall | Coastal country suddenly gains usable fleet and convoys | Invasion and maritime opportunity can become viable after capacity checks | Ships alone do not supply troops or protect the homeland |
| AI-059-34 | Infrastructure windfall | Rail and infrastructure improve behind an active front | Feasibility and operation scale can rise where supply truly improves | No global attack increase on unrelated fronts |
| AI-059-35 | Player takeover | Human takes control of an affected AI country during war | Every Event 059 AI layer becomes inactive for that country | No hidden combat or production modifier remains |
| AI-059-36 | AI handback | Country from AI-059-35 returns to AI control | Active baseline and evolution layers return after current-state reassessment | The AI must not resume an obsolete operation without reassessment |
| AI-059-37 | Hotjoin and co-op | Player hotjoins or co-controls an AI country | Country is treated as human-controlled | No duplicate activation or local desynchronisation |
| AI-059-38 | New released AI country | Country is released after event activation | It receives the current active layers through native or bounded registration | No recurring global scan is allowed to provide coverage |
| AI-059-39 | New player country | Player takes a newly released country | It remains free of Event 059 AI behavior until AI takes control | Country creation must not force automated actions on the player |
| AI-059-40 | Evolution I disabled | Baseline, II, or III can be active, but I is disabled before activation | No extra persistence, follow-up duration, or shortened recovery from I | Higher stages cannot recreate I under another score |
| AI-059-41 | Evolution II disabled | Baseline, I, or III can be active, but II is disabled before activation | No extra opportunity-war or predatory intervention layer | Evolution III cannot gain additional-war behavior by itself |
| AI-059-42 | Evolution III disabled | Lower layers active | No extra theater scale, reserve-risk reduction, or ambitious operation layer | Lower stages retain their intended behavior only |
| AI-059-43 | Pre-fire catch-up at 650 Chaos | Event first fires at 650, all evolutions enabled | Baseline and all three evolution layers activate. One player report appears. Four history records remain coherent | No extra Chaos for evolution activation and no popup flood |
| AI-059-44 | Pre-fire catch-up with II disabled | Event first fires at 650, Evolution II disabled | Baseline, I, and III activate. Predatory opportunity-war behavior remains absent | Stage ordering and Event Details must show II as not activated |
| AI-059-45 | Diplomacy cluster member | A valid Diplomacy cluster incident includes Event 059 under its authoritative member metadata | Event activates once, uses normal effects, cluster counts one pacing event | No duplicate timer acceleration, duplicate activation Chaos, or separate Diplomatic Panic resolution |
| AI-059-46 | Save and reload | Save during active baseline and evolution layers | Global state, activation history, evolution state, and current-control behavior persist | No repeated report or one-time Chaos gain |

## Rank and dominance targets

The implementation passes the probability review when these broad properties hold:

- favorable, supplied attack cases move offensive plans upward relative to the unmodified baseline
- hard safety cases remain blocked or dominated by recovery, defense, and replacement plans
- Evolution I changes continuation and follow-up more than war-opening behavior
- Evolution II changes legal opportunity and intervention behavior more than front persistence
- Evolution III changes scale and accepted risk without erasing safety vetoes
- disabling one evolution removes its own channel
- owner-specific strategy can dominate the generic layer where required
- no Event 059 plan ranks first in every scenario
- no production preference starves basic replacements or logistics
- weak unrelated targets remain invalid
- human-control cases evaluate every Event 059 layer as inactive

## Sweep requirements

At minimum, sweep these inputs and identify rank reversals:

- local strength ratio from severe inferiority through clear superiority
- supply from critical failure through full supply
- available reserve share
- equipment replacement trend
- trained manpower reserve
- fuel stock and trend
- number and severity of existing wars
- target strategic value
- legal-path validity
- naval transport and convoy capacity
- expected enemy coalition strength
- country capacity from weak minor through major power
- evolution combination, including disabled middle stages

The final tuning report should explain each important reversal. A plan that never changes rank across these conditions is probably too broad or disconnected from material state.
