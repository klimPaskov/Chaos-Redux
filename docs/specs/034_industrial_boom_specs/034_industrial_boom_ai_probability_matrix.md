# Event 34 Industrial Boom AI and probability scenario matrix

Rules and profiles are owned by [part 8](034_industrial_boom_spec_part_8_ai_probability_balance.md).
Use these scenario IDs before and after every weighted change.
Report exact results only when the complete candidate pool and external factors are known; otherwise report ordering, bounds, samples or the unresolved dependency.

## Target selection

The implemented entry is an unweighted `random_country`; these scenarios apply once weighting lands.

| ID | World state | Expected result |
| --- | --- | --- |
| TGT-01 | 1936 majors plus one player non-major | The player has meaningful weight and the largest major does not dominate |
| TGT-02 | One country has an active boom | That country has zero weight |
| TGT-03 | Several recent recipients | Recent recipients rank below comparable untouched countries |
| TGT-04 | One earlier crash, one earlier controlled landing | The crash lowers weight for two years; the landing creates no dominance |
| TGT-05 | Multiplayer with several players | No hidden preference for one player |
| TGT-06 | One valid country | It receives all weight |
| TGT-07 | No valid country | The event is unavailable and nothing is queued |
| TGT-08 | High Chaos, all stages enabled | Country choice is unaffected by evolved openings |

## Decision behavior

| ID | Situation | Expected ordering | Must not happen |
| --- | --- | --- | --- |
| AI-01 | Peacetime major, 15 and steady, strong logistics, no reserve, one unprotected region | Reserve or Designate, then Protect; Run Hot possible but lower; Cool near zero | Emergency rows weighted; Stabilize dominant without a supply cause |
| AI-02 | Winning wartime major, 20 rising slowly, equipment deficit | Run Hot, Factory Conversion project, then Reserve; landing low while the offensive matters | Immediate cooling; overlapping hot windows |
| AI-03 | Losing wartime major, 45 rising, threatened capital | One hot window if still Strained, Protect the critical region, Stabilize, then rough landing or halt | A long project with no chance to finish; Let It Run in Critical |
| AI-04 | Blockaded maritime major, 40 rising, port damaged, no reserve | Stabilize with convoy costs, Protect the port region, Reserve, Cool if access cannot return | Train-only relief at full strength; convoy costs for a landlocked comparison |
| AI-05 | Two regions, one protected, repeated bombing, 50 | Protect the unprotected region, Stabilize, start landing once a project is Secured | Re-targeting the already protected region |
| AI-06 | Small non-major, one region, 25 | Every essential row affordable; one project; landing after it secures | Commitments larger than the country's factories |
| AI-07 | Speculative Mania, 55 rising, one speculative project near Integrating end | Credit restraint or Stabilize by leading cause; abandon if Dangerous approaches first | A second speculative project; zero weight on restraint |
| AI-08 | Industrial Miracle, 65, one Fragile unprotected Miracle Region, reserve held | Protect it, Cool, then landing once below the risk | A new Miracle declaration |
| AI-09 | Runaway Industrialization entry, 35, strong supply | Cautious and balanced choose Direct the Spread, fragile chooses Contain It, only desperate chooses Let It Run | Let It Run dominating every profile |
| AI-10 | Critical, 92 rising fast, no reserve, one transport shock | Stabilize at emergency strength, Prevent the Crash, abandon projects; halt only if its condition holds | Any expansion row with weight; treating a new reserve as instant safety |
| AI-11 | Landing nearly complete, 30 falling, two Secured projects | Keep conditions, Stabilize only if needed | Cancelling the landing for a small output gain |
| AI-12 | New boom after an earlier crash, 25 | Higher weight on Reserve and Stabilize, lower on Run Hot and speculative offers, still able to land well | A permanently passive route |
| AI-13 | Active boom receives an Event 35 supply contract at 30 and at 85 | Event 35's AI offers to the safe supplier and blocks the overheated one (implemented through the supplier adapter triggers) | An offer to a supplier at or above the risk threshold |

## Evolution timing

| ID | Boom state | World state | Expected relation |
| --- | --- | --- | --- |
| EVO-01 | Baseline, low pressure, cautious | Rising Chaos just reached | Later than the 90-day center |
| EVO-02 | Baseline, repeated hot running | Rising Chaos | Earlier than EVO-01 |
| EVO-03 | Landing mission active | Rising Chaos | Paused |
| EVO-04 | Evolution I active | Below Chaos Tier | Evolution II impossible |
| EVO-05 | Evolution I active, high pressure | Chaos Tier | Evolution II eligible with dynamic delay |
| EVO-06 | Evolution II, controlled management versus long time in Dangerous | Totalen Chaos | Controlled management slower |
| EVO-07 | Stage disabled | Any | Zero chance, no record |
| EVO-08 | Evolved opening | Stage already active | No duplicate log row |

## Incident selection

| ID | Conditions | Dominant family | Must be zero |
| --- | --- | --- | --- |
| INC-01 | 20, baseline | Rail Congestion | Maintenance Failure |
| INC-02 | 55, train deficit, landlocked | Rail Congestion, Material Shortfall without convoys | Any convoy branch |
| INC-03 | Evolution I with a speculative project | Speculative incidents | Miracle and spread incidents |
| INC-04 | Evolution II with a Miracle Region | Miracle incidents | Spread incidents |
| INC-05 | Evolution III with Direct the Spread | Spread incidents | Incidents on states that are not spread states or regions |
| INC-06 | Protected region with an open incident | Other regions or national incidents | A second incident in that state |
| INC-07 | No valid region | National incidents only | Every state-specific incident |

## Landing outcomes

| ID | Conditions at mission end | Expected outcome |
| --- | --- | --- |
| LAND-01 | 25, two Secured projects, reserve held | Controlled with full legacy |
| LAND-02 | 45, one Secured project | Rough |
| LAND-03 | 45, one Secured project, active supplier contract | Controlled once |
| LAND-04 | 85, reserve held, Emergency Production Halt | Forced landing succeeds |
| LAND-05 | 92, no reserve, no protected region, halt | Halt fails, crash |
| LAND-06 | Evolution III, directed spread integrated, 30 | Controlled with the strongest legacy, inside budgets |

## Evidence to record per patched surface

Source revision before the change, scenario IDs, candidate pool completeness, external factors, evidence type (exact, bounded, sampled, score-only or unresolved), ordering before and after, and any scenario still unresolved.
The auditor stays read-only; the event owner sets the balance targets and applies the patch.
