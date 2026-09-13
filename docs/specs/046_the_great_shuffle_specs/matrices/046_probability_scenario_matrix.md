# Event 046 probability scenario matrix

## Audit ownership

Every weighted family, quota, evolution pacing rule, cluster participation rule, family mood, categorical result, and percentile achievement selector must receive the project's probability workflow.

The read-only `chaosx_ai_probability_auditor` starts with `hoi4.probability_inspect`.

The Event 46 owner supplies the intended balance targets and applies source changes.

The auditor then runs `hoi4.probability_compare` over the same named scenarios.

Exact probability claims require a complete candidate pool and complete external state.

Otherwise the result is reported as bounded, sampled, score-only, or unresolved.

## Family-selection scenarios

| Scenario ID | Scenario | Required setup | Main tools | Expected evidence |
| --- | --- | --- | --- | --- |
| `P46-F01` | Baseline ordinary world | All Baseline core families valid, no later capability, no conflicts | inspect, evaluate, sweep, render | Selected coverage stays inside the Baseline target band and never drops below the available floor |
| `P46-F02` | Capability monotonicity | Same complete pool evaluated at Baseline and Evolutions I through V | inspect, sweep, compare, render | Expected selected share rises monotonically at every capability |
| `P46-F03` | Baseline identity quota | Full pool at Evolutions I through IV | inspect, evaluate, simulate | Every valid result satisfies the required Baseline quota without one Baseline family dominating all sequences |
| `P46-F04` | Domain quota coverage | Full pools at Evolutions I, II, III, and IV | inspect, simulate, compare | Each capability satisfies its new-domain quota when enough valid families exist |
| `P46-F05` | Narrow eligible pool | Only two, four, six, and eight families valid across several capabilities | inspect, evaluate, sweep | Floors clamp to available families without duplicate selection or impossible quota loops |
| `P46-F06` | One family per group | Exactly one eligible family in several selection groups | inspect, evaluate | The family remains selectable and no normalization removes it |
| `P46-F07` | Compatibility collision | Several high-weight families share one compatibility group | inspect, evaluate, simulate | At most one incompatible family enters each result and unused slots refill from legal candidates when intended |
| `P46-F08` | Dependency bundle | A bundle has several child families and competes with independent families | inspect, evaluate, simulate | Bundle weight and slot accounting match the declared design and never partially select children |
| `P46-F09` | Owner adapter starvation | Two valid owner adapters compete with many core families at Evolution IV | inspect, sweep, simulate | Evolution IV quota gives both adapters a material chance and neither remains practically unreachable |
| `P46-F10` | Many owner adapters | Twenty valid adapters with mixed weights at Evolution IV | inspect, sweep, simulate, render | Coverage scales with pool size, rare adapters remain reachable, and no adapter dominates without an explicit reason |
| `P46-F11` | Evolution V saturation | Maximum valid pool with all core and adapter families, some conflicts, and some zero-scope families | inspect, evaluate, simulate | Every non-conflicting mandatory family with valid scopes participates and total coverage reaches at least 90 percent |
| `P46-F12` | Disabled evolution | Evolution III threshold met while Evolution III is disabled | inspect, evaluate, compare | No Evolution III family enters, earlier families remain valid, and the disabled record is not set |
| `P46-F13` | Disabled owner adapter capability | Evolution IV disabled with owner adapters registered | inspect, evaluate | Adapter families have zero eligibility without altering registration or earlier family weights |
| `P46-F14` | Family mood distribution | One numeric family evaluated under balanced, scarcity, abundance, and split moods | inspect, sweep, simulate, render | Result ordering matches the intended low, high, and two-tail profiles without using old values |
| `P46-F15` | State-family independence | Population and industry selected together across many states | inspect, simulate, compare | Their results show no unintended positive correlation beyond shared legal exclusions |

## Repeatability scenarios

| Scenario ID | Scenario | Required setup | Main tools | Expected evidence |
| --- | --- | --- | --- | --- |
| `P46-R01` | Two consecutive firings | Same eligible pool and world anchors, different transaction seeds | inspect, simulate, compare | Second-family selection is unaffected by the first selected set |
| `P46-R02` | Long sequence independence | Complete custom-pool manifest with cadence, repeatable cap, recovery, eligibility, and no external changes | inspect, sequence, simulate, render | No family gains or loses conditional weight because it appeared earlier |
| `P46-R03` | Same family repeated | One family remains high weight across a complete sequence | inspect, simulate | Immediate reselection remains possible and has the declared ordinary probability |
| `P46-R04` | Prior winner and loser | Two countries receive extreme opposite results, then the same family fires again | inspect, simulate | Later result distribution is identical for both scopes after controlling current legal caps |
| `P46-R05` | Repeatable event availability | Current Event 46 weight, cap decay, and monthly recovery over several firings | inspect, sequence, render | Ordinary repeatable availability matches the shared event system and no Event 46 side memory changes it |

## Evolution pacing scenarios

| Scenario ID | Scenario | Required setup | Main tools | Expected evidence |
| --- | --- | --- | --- | --- |
| `P46-E01` | Evolution I threshold | Chaos moves from 199 to 200 with evolution enabled | inspect, evaluate, sweep | Eligibility begins at 200 and MTTH centers near the accepted target under ordinary conditions |
| `P46-E02` | Distance above threshold | Evaluate each evolution at threshold, midpoint, and near next tier | inspect, sweep, render | Any acceleration above threshold follows the intended order without making activation immediate unless specified |
| `P46-E03` | Pre-fire activation | Evolution threshold met before Event 46 ever fires | inspect, evaluate | Activation probability does not depend on prior Event 46 history |
| `P46-E04` | Disabled evolution pacing | Threshold met while the evolution toggle is disabled | inspect, evaluate, compare | Activation probability is zero and no recorded state or content unlock occurs |
| `P46-E05` | Evolution V threshold | Chaos moves from 999 to 1000 under each live freeze ordering | inspect, evaluate, compare | The immediate activation and bounded reachability window are exact, unique, and terminal-safe |

## Cluster scenarios

| Scenario ID | Scenario | Required setup | Main tools | Expected evidence |
| --- | --- | --- | --- | --- |
| `P46-C01` | Randomizations with one valid member | Event 46 is the only valid enabled member | inspect, evaluate, simulate | Cluster logic cannot apply Event 46 twice and automatic expansion follows the accepted one-member rule |
| `P46-C02` | Randomizations with two valid members | Event 46 and one future member valid | inspect, evaluate, sweep | Cluster roll and member participation follow shared rules with no duplicate Event 46 transaction |
| `P46-C03` | Event 21 multiple memberships | Wars and Domestic Unrest both eligible from Event 21 | inspect, evaluate, simulate | Membership selection uses the intended cluster rules and does not erase either relationship |
| `P46-C04` | Member severity relation | One event has different accepted severity by cluster | inspect, evaluate | Severity lookup reads the cluster-member relationship and avoids one overwritten global field |

## Chaos-compression scenarios

| Scenario ID | Scenario | Required setup | Main tools | Expected evidence |
| --- | --- | --- | --- | --- |
| `P46-H01` | Minimum Baseline commit | Lowest legal selected count and only low-disruption families | inspect, evaluate | Direct gain reaches the Baseline lower bound and records once |
| `P46-H02` | Maximum Baseline commit | Highest Baseline coverage with severe legal tails | inspect, sweep | Gain remains within the Baseline cap |
| `P46-H03` | Higher-domain monotonicity | Comparable breadth across every highest committed domain | inspect, evaluate, compare | Deeper domains have a higher possible and expected direct gain |
| `P46-H04` | Owner severity abuse | External owner proposes extreme severity for a minor value | inspect, evaluate | Event 46 approval or cap prevents owner-controlled Chaos farming |
| `P46-H05` | Generic-source suppression | Ruling ideology, population, and a structural family commit together | inspect, evaluate | Only the declared Event 46 entry scores for the rewrite, with zero Deaths or generic ideology duplicate |
| `P46-H06` | Recovery resume | Save and load during commit and report phases | inspect, evaluate | Direct Chaos and first-manifestation premium record once |

## Achievement-selection scenarios

| Scenario ID | Scenario | Required setup | Main tools | Expected evidence |
| --- | --- | --- | --- | --- |
| `P46-A01` | Top and bottom quantile calculation | Complete valid-country value pool after one transaction | inspect, evaluate | Quantile assignment is deterministic, covers ties, and excludes invalid scopes |
| `P46-A02` | Three-reversal candidate selection | Several comparable families available after first firing | inspect, evaluate, simulate | Candidate family selection cannot choose a hidden, incomparable, or absent family |
| `P46-A03` | Impossible geography rankings | Population and industry results for all valid states | inspect, evaluate | Decile and quartile proof is deterministic and stored once |
| `P46-A04` | Maximum transaction coverage | Evolution V with conflicts and zero-scope families | inspect, evaluate | The 90 percent test uses the eligible safe pool after declared exclusions, not every registered row |

## Required output from the probability auditor

The audit report must name each inspected source surface, scenario ID, candidate pool completeness, external factor completeness, evidence type, revision, scenario hash, and result.

It must separate exact probability from sampled frequency.

It must identify starvation, dominance, unreachable quotas, conflict loss, non-monotonic coverage, and sequence memory.

After any weight or probability patch, it must compare the final source against the same baseline scenarios.
