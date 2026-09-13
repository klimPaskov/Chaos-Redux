# Event 050 probability scenario matrix

No scenario below has measured results in this planning environment. The implementation audit must use the HOI4 probability tools and label exact, bounded, sampled, score-only, and unresolved evidence correctly.

| Scenario ID | Surface | Initial state | Expected ordering or bound | Required tool evidence |
| --- | --- | --- | --- | --- |
| `TGT-01` | Target class | One player and five majors eligible | Player class has substantial minority chance, majors retain majority | Inspect, evaluate, compare |
| `TGT-02` | Target class | Four players and five majors eligible | Player class chance remains near intended class share, not four times higher | Inspect, sweep, compare |
| `TGT-03` | Target class | No player eligible | A valid major receives full normalized pool | Inspect, evaluate |
| `TGT-04` | Target class | No major eligible | A valid player receives full normalized pool | Inspect, evaluate |
| `TGT-05` | Target country | One active target among otherwise valid majors | Active target has zero effective weight | Inspect, evaluate |
| `TGT-06` | Target country | Special Chaos actor and human major both present | Special actor excluded, ordinary major remains | Inspect, evaluate |
| `COL-01` | Convenor | High-rivalry major, friendly major, distant minor | Rival major ranks first when otherwise viable | Inspect, evaluate, render matrix |
| `COL-02` | Core enforcers | Oil supplier, shipping state, distant ideological partner | Supplier and shipping state outrank distant symbolic partner | Inspect, sweep |
| `COL-03` | Coalition membership | Friendly state with heavy target trade | Conditional or refusal score exceeds hard commitment | Inspect, evaluate |
| `NEU-01` | Intermediary selection | Neutral shipping power with route, neutral landlocked minor without route | Shipping power dominates and invalid minor is excluded | Inspect, evaluate |
| `NEU-02` | Intermediary acceptance | High profit, weak coalition dependence, good relations | Acceptance or secret acceptance ranks above refusal | Inspect, sweep |
| `AI-01` | Target response | Critical maritime dependence, low fuel, weak army | Intermediary, fast smuggling, or concession outranks defiance and seizure | Inspect, evaluate, compare |
| `AI-02` | Target response | Low dependence, strong stability, strong army | Defiance or self-sufficiency outranks major concession | Inspect, evaluate, compare |
| `AI-03` | Target response | Severe Pressure, vulnerable nearby oil region, strong army | Resource Seizure becomes competitive without becoming certain | Inspect, sweep, compare |
| `AI-04` | Target response | Severe Pressure, nearby resource belongs to stronger faction | Resource Seizure weight falls to zero or near-zero safety state | Inspect, evaluate |
| `SMG-01` | Smuggling outcome | Baseline, strong route, good relations | Success is most likely, exposure remains possible | Inspect, evaluate, simulate if pool complete |
| `SMG-02` | Smuggling outcome | Evolution I, same route, strong enforcement | Exposure and secondary pressure rise relative to `SMG-01` | Inspect, compare |
| `EVO-01` | Evolution I pacing | Pressure 70, exposed route, united coalition | Faster than base evolution timing | Inspect, evaluate timing, sweep |
| `EVO-02` | Evolution I pacing | Pressure 15, collapsing coalition | Slower or skipped if crisis resolves first | Inspect, timing evaluation |
| `EVO-03` | Evolution II count | Two free registry slots and many valid targets | Two or three total targets, hard cap respected | Inspect, evaluate |
| `EVO-04` | Evolution II count | One free registry slot | Exactly one additional target at most | Inspect, evaluate |
| `EVO-05` | Evolution II targets | Player already targeted, several majors valid | Additional targets are distinct and normally AI majors | Inspect, evaluate |
| `OVR-01` | Overlapping roles | Country core against A, neutral for B, intermediary for C | Each ledger receives its own valid role score | Inspect, evaluate per pool |
| `FAT-01` | Coalition fatigue | Twelve months, weak justification, high participant losses | Exit and conditional scores rise | Inspect, sweep, compare |
| `FAT-02` | Coalition fatigue | Twelve months, high public Condemnation, target threats | Commitment remains competitive | Inspect, sweep, compare |
| `SET-01` | Settlement acceptance | Limited concession, high fatigue, moderate Pressure | Convenor acceptance dominates rejection | Inspect, evaluate |
| `SET-02` | Settlement acceptance | Major concession, hardliner coalition, recent smuggling exposure | Result remains uncertain and hardliner veto can matter | Inspect, evaluate, render matrix |

## Compare discipline

Every source change to a listed weighted surface requires a baseline audit before the patch and `hoi4.probability_compare` after the patch using the same scenario inputs.

Sequence simulation is permitted only when the complete cadence, recovery, cap, removal, reset, and terminal-state contract is supplied.
