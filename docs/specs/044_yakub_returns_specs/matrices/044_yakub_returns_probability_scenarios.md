# Event 044 weighted behavior scenario matrix

The implementation must route every probability-bearing surface through `chaosx_ai_probability_auditor`. The auditor begins with `hoi4.probability_inspect`, names the complete candidate pool, states all external factors, and distinguishes exact, bounded, sampled, score-only, and unresolved evidence.

## Named baseline scenarios

| Scenario ID | Surface | World state | Expected ordering |
| --- | --- | --- | --- |
| `P44_US_STABLE_INTEL` | United States response AI | Stable democracy, strong intelligence, peace, low Influence | Infiltration above reform, reform above arrest, arrest above mass crackdown |
| `P44_US_DEPRESSION` | United States response AI | Great Depression 2.0 active, low stability, high unemployment pressure | Material concessions and relief above symbolic messaging |
| `P44_US_WARTIME` | United States response AI | Major war, high casualties, strategic rail risk | Arsenal and rail security above long civic programs |
| `P44_US_AUTHORITARIAN` | United States response AI | Authoritarian government, high coercive capacity | Selective suppression above negotiation, nationwide crackdown remains bounded until high Influence |
| `P44_ARREST_LOW_INFLUENCE` | Arrest outcome random pool | Influence below 30, strong intelligence, low martyr pressure | Clean detention above escape or martyrdom |
| `P44_ARREST_HIGH_INFLUENCE` | Arrest outcome random pool | Influence above 70, entrenched institutions, high repression memory | Martyrdom or underground continuation above clean collapse |
| `P44_ROUTE_PERSONALIST` | Focus route AI | Yakub alive, personal loyalty high, institutions weak | Personal Revelation route dominates |
| `P44_ROUTE_FEDERAL` | Focus route AI | Negotiated compact, civic institutions strong, foreign recognition available | Federal New Nation route dominates |
| `P44_ROUTE_REVOLUTIONARY` | Focus route AI | Secular cadres strong, active war, labor radicalization | Black Republic route dominates |
| `P44_ROUTE_SUPREMACIST` | Focus route AI | Hardliners strong, repression memory high, pariah diplomacy accepted | Original Supremacy route becomes viable without starving every other route |
| `P44_ROUTE_CONGRESS` | Focus route AI | Foreign chapters in three regions, high diplomatic reach | Diaspora Congress route dominates |
| `P44_DIASPORA_COLONIAL` | Foreign target selection | Colonial host, instability, anti-colonial pressure, valid region | Target score above stable independent countries |
| `P44_DIASPORA_REFORMED` | Foreign target selection | Stable country, recent reforms, strong rival movement | Target score below colonial and crisis hosts |
| `P44_DIASPORA_RIVAL` | Local movement outcome | Strong local anti-colonial organization rejects doctrine | Tactical cooperation or rejection above full adoption |
| `P44_INT_LOW_COHESION` | International action AI | Cohesion low, members divided | Congress and mediation above weapons shipments |
| `P44_INT_WAR_SUPPORT` | International action AI | Cohesion high, member at defensive war, convoy route open | Equipment and volunteer support above propaganda |
| `P44_WORLD_END_READY` | Terminal readiness candidate | 1000 Chaos, valid state, International, multi-region footprint | Event 44 terminal candidate available |
| `P44_WORLD_END_INVALID` | Terminal readiness candidate | 1000 Chaos, Yakub alive, no viable state or International | Event 44 terminal candidate unavailable |

## Required evidence methods

- Use `hoi4.probability_evaluate` for complete option pools and decision scores under the named states.
- Use `hoi4.probability_sweep` across Influence bands, intelligence strength, stability, Cohesion, and region count.
- Use `hoi4.probability_compare` after every source change to the audited weights.
- Use `hoi4.probability_simulate` only where a sampled sequence gives useful evidence.
- Use `hoi4.probability_sequence` only after the complete cadence, cooldown, threshold, and terminal contract is declared.
- Use `hoi4.probability_render` for route matrices, influence sweeps, or unresolved candidate gaps.
- Report starvation risks, dominant options, dead branches, and unavailable candidates.
- The auditor does not choose the desired balance target. The source design above supplies the expected ordering.
