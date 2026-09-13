# Event 043 AI and probability scenario matrix

## Evidence rule

The probability auditor is read-only. It begins with `hoi4.probability_inspect`, declares the complete candidate pool and external factors, and distinguishes exact, bounded, sampled, score-only, and unresolved results.

| Scenario ID | Surface | Setup | Expected behavior | Evidence type | MCP route |
| --- | --- | --- | --- | --- | --- |
| P-043-01 | Baseline identity spread | Four opening slots, all sixteen packages ready, normal world | Each selected identity in a different macroregion where four valid regions exist | Exact or bounded selection probability | inspect, evaluate, simulate, render |
| P-043-02 | Crowded Mediterranean fallback | Several Nordic and Pacific pools invalid | Selector reduces roster or moves within cultural pools before crowding one sea | Seeded simulation and unresolved reasons | inspect, simulate, render |
| P-043-03 | Evolution I spread | Baseline four active, twelve dormant, four valid unused regions | Four later emergences favor unused macroregions | Sequence timing and selection distribution | inspect, simulate, sequence, render |
| P-043-04 | Evolution II cadence | Eight active, eight dormant, World Collapse | Remaining emergences occur over the declared paced window without starvation | Sequence distribution | inspect, sequence, simulate, render |
| P-043-05 | Coastal versus deep target | One weak port at depth 0 and one rich capital at illegal depth 4 | Port receives positive dominant score, deep capital is invalid | Exact candidate ordering | inspect, evaluate |
| P-043-06 | Own lair threatened | Monster can attack rival or defend original lair | Defense plan dominates until lair is safe | Score ordering | inspect, evaluate, sweep |
| P-043-07 | Hunger crisis | Starving monster has one valid feeding state and one brood receipt | Feeding or contraction dominates brood creation | Score ordering across Hunger bands | inspect, sweep |
| P-043-08 | Pact under pressure | Compatible pair, low Sea Bond, shared major enemy | Proposal and acceptance become likely without certainty | Bounded acceptance probability | inspect, evaluate, sweep |
| P-043-09 | Pact during dominance | Dominant solitary-leaning monster with weak compatible target | Solitary or subject route dominates ordinary compact | Score ordering | inspect, evaluate |
| P-043-10 | Betrayal without gain | Compact stable, no useful target, moderate Hunger | Betrayal remains starved | Upper probability bound | inspect, evaluate |
| P-043-11 | Betrayal with gain | Opportunist, high Hunger, exposed rival lair, sufficient apex health | Betrayal becomes possible but does not dominate preservation crisis | Sensitivity sweep | inspect, sweep |
| P-043-12 | Human evacuation | Dense state likely to fall, valid route and destination | Evacuation is high priority | Score ordering and affordability boundary | inspect, evaluate, sweep |
| P-043-13 | Human kill zone | Observed low-Sea-Bond apex, required divisions present | Kill-zone action becomes likely | Score ordering | inspect, evaluate |
| P-043-14 | Suicidal kill zone | Apex healthy, human capital exposed, divisions absent | AI weight is zero or negligible | Exact invalidation | inspect, evaluate |
| P-043-15 | Pact terminal readiness | Five-apex faction, four regions, coastal threshold near boundary | Readiness turns on only after every declared proof and confirmation | Threshold sweep | inspect, sweep |
| P-043-16 | Last Survivors timing | Four apexes remain, extinction pressure varies | Readiness requires persistent pressure and does not fire instantly | Timing distribution | inspect, evaluate, simulate |
| P-043-17 | Cthulhu theatre assignment | Twelve transferred apexes, several fronts | Apexes distribute by role and protect endangered members | Score-only or sampled assignment | inspect, evaluate, simulate |
| P-043-18 | Scenario roster counts | Low, Medium, High, Maximum | Created roster equals 2, 5, 10, 16 when packages and states are valid | Exact result and failure reporting | inspect, evaluate |

## Audit, patch, compare cycle

1. Run baseline scenarios.
2. Parent or owning specialist applies bounded tuning.
3. Run `hoi4.probability_compare` with the same scenario IDs.
4. Record changed order, timing, dominance, starvation, and unresolved external state.
5. Reject a patch that fixes one scenario by breaking a higher-priority safety case.

## Sequence limitation

Use `hoi4.probability_sequence` only after the complete Event 043 custom-pool manifest declares cadence, removals, cooldowns, receipts, resets, timer changes, and terminal states.
