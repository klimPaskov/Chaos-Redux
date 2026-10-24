# Event 120: Accepted probability scenarios

## Evidence and interpretation

These scenarios record the accepted Event 120 design arithmetic and corrected AI policy.
The calculations use exact rational arithmetic and the authored rounding rule, with nonnegative half-steps rounded upward to the nearest multiple of five.
They are conditional on the declared inputs and complete artificial pools.
They do not establish native engine probabilities, observed AI choices or full-campaign balance.

The [scenario data](120_widespread_mutiny_probability_scenarios.json) preserves named cases, exact fractions, complete inputs, classifications and SHA-256 source revisions.
The relevant design sources are [Part 1](120_widespread_mutiny_spec_part_1_core.md), [Part 2](120_widespread_mutiny_spec_part_2_responses.md), [Part 5](120_widespread_mutiny_spec_part_5_connections.md) and [Part 6](120_widespread_mutiny_spec_part_6_ai_balance.md).
The completed opening and suppression grids are reused because the reviewed formulas and relevant policies are unchanged.
The additional calculation surface is the White Peace adapter in Part 5.

“Exact” means exact arithmetic for the stated formula or complete pool.
“Bounded” describes a lawful maximum rather than a guaranteed outcome.
“Score-only” describes AI willingness and priority without a click percentage.
Focus selection, native timing and owner inputs absent from the design remain explicitly unresolved.

## Seven corrected design findings

| Finding | Accepted correction |
| --- | --- |
| F01, recovery could remain open indefinitely | Containment reduces Disaffection by 25 once. After every cohort has a lawful disposition and no breach remains, recovery reduces it by 5 every ten days without active-crisis pressure. |
| F02, poor countries lacked a concrete affordable exit | Immediate local discharge has zero spendable payment, actual release, 180 days of personnel protection, returns only of secured equipment and no confidence reward. |
| F03, multiple cohorts could ambiguously multiply pressure | Each ten-day review makes one country update. An adverse condition counts once, and relief covers all unresolved cohorts sharing its grievance. |
| F04, recurrence used conflicting clocks | One 180-day settlement-history window includes the first 90 days of ordinary-draw protection. |
| F05, routine negotiation could displace practical remedies | The negotiation bonus requires an unmet command or representation concession. A complete direct remedy gains 50 willingness points. Paid delivery and a confirmed imminent external settlement have stated priorities. |
| F06, discharge scoring could endanger the last defending force | A release bonus requires adequate defense. Immediate survival takes priority during invasion, with a narrow exception for futile defense and a verified settlement protecting survivors. |
| F07, timing and accounting boundaries were ambiguous | Spread obeys the deadline, D 60 and prospective cohort-cap gates. A breach bonus applies to one eligible check within 20 days. Responses use respondent confidence. Recovery admits containment and release. Schedule and protection clocks are separate. Amnesty never reopens the gross loss ceiling. |

## Opening values and country selection

The following inputs use the flags defined in Part 1.
Every omitted flag is zero.

| Scenario | W and active flags | H | Initial D | Confidence |
| --- | --- | --- | --- | --- |
| O01, recently mobilized minor | W 30 | 20 | 40 | 40 |
| O02, exhausted frontline army | W 20, L S K | 60 | 70 from raw 75 | 40 |
| O03, linked desertion | W 10, L S K B X | 70 from raw 90 | 70 from raw 100 | 20 |
| O04, delivered settlement | W 30, R | 10 | 30 | 60 |
| O05, long inactive war | W 30, L remains zero | 20 | 40 | 40 |
| O06, supplied offensive | W 20, L K | 45 | 65 | 40 |
| O07, starved defense | W 20, L S | 50 | 65 | 40 |

The 2,304-case grid covers integer W from 0 through 35 and every combination of the six binary context flags.
H remains between 5 and 70, D between 25 and 70, and ordinary initial confidence between 20 and 60.
Imported incident history is a separate input.
W 35 is eligible, while W 35.0001 is outside the ordinary pool.
The rounding term jumps at W 30, W 20, W 10 and W 0.
The later low-support progression penalty applies strictly below W 25.

P01 declares exactly four eligible countries A through D with weights 20, 60, 70 and 10.
No other candidates or external modifiers exist in this artificial pool.
The primary is guaranteed an outbreak, and each other country receives its independent direct check.
For country i, its total outbreak probability is `H_i / 160 + (1 - H_i / 160) * H_i / 100`.

| Country | H | Primary share | Outbreak through either route |
| --- | --- | --- | --- |
| A | 20 | 1/8 = 12.5% | 3/10 = 30% |
| B | 60 | 3/8 = 37.5% | 3/4 = 75% |
| C | 70 | 7/16 = 43.75% | 133/160 = 83.125% |
| D | 10 | 1/16 = 6.25% | 5/32 = 15.625% |

Expected affected countries are `163/80`, or 2.0375.
Exactly one, two, three or four countries are affected with probabilities 22.65%, 53.05%, 22.2% and 2.1%.
The additional checks are independent conditional on the primary.
The final country outcomes are not mutually independent.
A lone eligible country receives an outbreak with certainty even at H 5.

P02 holds these weights fixed, immediately excludes affected actors, admits no new actors or recoveries, and advances one abstract draw opportunity per step.
The chance that all four have been affected is approximately 33.7891% after draw two, 89.1366% after draw three and exactly 100% after draw four.
The JSON retains the exact fractions.
This sequence has no elapsed-day or global-event-frequency claim.
P03 includes an equal pool of twenty H 15 candidates, whose expected affected count is 3.85 per draw.

## Progression, costs and finite losses

The D-series uses one cohort unless stated otherwise.
D01, with D 40, W 30, confidence 40 and every review condition false, remains at D 40 while unresolved.
D02, with D 45 and only W below 25 active, reaches D 50, D 55 and D 60 at successive ten-day reviews.
The opening deadline still prevents premature escalation.
D03 has D 70, W 20, confidence 20, severe supply failure and an overdue milestone after the response deadline.
Its raw +25 review becomes +20 through the clamp.

D05 applies successful containment to D 40 and confidence 40, giving D 15 and confidence 30.
D07 starts at D 100, reaches D 75 after containment and D 25 after 100 days of lawful recovery.
D08 starts at D 100 and uses actual immediate discharge, reaching D 80 and then D 25 after 110 days, while the 180-day personnel protection still applies.
D09 has three severely undersupplied unresolved cohorts and W 20 with no other modifiers.
It receives one +10 country update.

Q01 covers the size factor from 0.5 to 3, with its floor at 10,000 and cap at 60,000 affected manpower.

| Action | Minimum authored resource quote | Maximum authored resource quote |
| --- | --- | --- |
| Compact | 15 PP and 5 Army XP | 90 PP and 30 Army XP |
| Leave | 10 CP | 45 CP |
| Relief | 25 support equipment and 13 applicable trucks | 150 and 75 |
| Paid discharge | 15 PP | 75 PP |
| Containment | 10 CP and 5 Army XP | 60 CP and 30 Army XP |
| Amnesty | 10 PP | 60 PP |

Actual transport, fuel, factory and force commitments remain separate declared inputs.
At 10,001 manpower, the support-equipment ceiling produces 26.
Immediate local discharge remains the zero-spend exception.

L01 holds D in one loss band, applies each review's maximum, and excludes combat, reinforcement, amnesty and transfers.

| Review | Cumulative loss at 5% of current strength, with 15% ceiling | At 10% of current strength, with 30% ceiling |
| --- | --- | --- |
| 1 | 5% | 10% |
| 2 | 9.75% | 19% |
| 3 | 14.2625% | 27.1% |
| 4 | 15% | 30% |

L02 has one 8,000-person formation at organization 60 and no separate loyal force.
The opening budget is 400 people, or 800 under aggravated entry.
The granularity exception removes no opening personnel or equipment and at most 30 organization.
Containment is unavailable without a qualifying loyal force.
The later personnel-loss ceilings are 1,200 and 2,400.
A loyal formation at organization 60 loses 12 organization after containment.

L03 bounds successful amnesty returns at 1/4, 7/16 and 175/256 of the original eligible outstanding deserters after one, two and four programs.
Those are 25%, 43.75% and 68.359375%.
L04 assumes uniform personal equipment per soldier, giving departure ceilings of 3/80 and 3/40 of opening cohort holdings, or 3.75% and 7.5%.
Heavy equipment requires its separately recorded seizure or transfer.
These are ceilings rather than guaranteed losses or returns.

## Suppression

The S-series supplies the effective loyal ratio R directly.
It does not claim a verified native effective-manpower reader.

| Scenario | R, U, D, confidence | Contained | Partial | Fracture |
| --- | --- | --- | --- | --- |
| S01 | 2, 1, 55, 40 | 80% | 15% | 5% |
| S02 | 1.5, 0, 70, 40 | 50% | 35% | 15% |
| S03 | 1.5, 0, 85, 10 | 20% | 30% | 50% |
| S04 | 4, 1, 55, 80 | 85% | 10% | 5% |

S05 retains 5,412 cases covering R 1.50 through R 6.00 in 0.01 increments, both supply-advantage states, three D bands and both confidence bands.
Every case is nonnegative and totals 100%.
The continuous formula guarantees a nonnegative Partial result because Fracture cannot exceed `100 - Success`.
The legal domain spans Contained 20 to 85, Partial 0 to 35 and Fracture 5 to 50.

S06 gives the exact minimum ratio meeting the AI's 60% chance gate, including the R 1.5 legality floor and half-up rounding.

| D | Confidence | No supply advantage | Supply advantage |
| --- | --- | --- | --- |
| Below 60 | At least 20 | 1.5 | 1.5 |
| Below 60 | Below 20 | 2.125 | 1.625 |
| 60 to 79 | At least 20 | 1.875 | 1.5 |
| 60 to 79 | Below 20 | 2.625 | 2.125 |
| At least 80 | At least 20 | 2.625 | 2.125 |
| At least 80 | Below 20 | 3.375 | 2.875 |

Deployment and defense-gap gates remain necessary.
S07 preserves exact equality cases.
At D 60, Q turns off, and at D 80, V turns on.
At confidence 20, the progression penalty applies but suppression T remains zero.
Confidence 40 and 70 satisfy their inclusive negotiation and return thresholds.
Chaos 600 admits evolution checks only when the separate front and actor gates hold.

## Spread, opposing choices and government scores

SP01 excludes the unprovided shared human-pressure adjustment.
The authored spread chances are 10% at D 60 to 79 and 25% at D 80 or above, with the stated confidence and one-use breach modifiers.
The local maximum is 35% before an owner adjustment.
SP02 has three independent eligible checks twenty days apart, one starting cohort, capacity for two more, and no settlement pause.
At a constant 10% chance, any spread has probability 271/1000 and two additional cohorts 7/250.
At a constant 25%, those probabilities are 37/64 and 5/32.
SP03 supplies one fresh breach only before the first check, with D at least 80 and confidence below 70.
Chances of 35%, 25% and 25% give `203/320 = 63.4375%` for any spread and `31/160 = 19.375%` for two additional cohorts.
Three checks at 35% would require three distinct qualifying breaches.

CP01 declares the complete Accept, Observe, Reject pool and uses the respondent's confidence.

| Context, other modifiers zero and every choice legal | Weights | Exact normalized design shares |
| --- | --- | --- |
| Confidence 40 | 40, 30, 20 | 4/9, 1/3, 2/9 |
| Confidence 39 | 0, 70, 20 | 0, 7/9, 2/9 |
| Both D at least 60, confidence 70, both governments can deliver and an immediate feasible local solution exists | 110, 30, 0 | 11/14, 3/14, 0 |

Authority and expiry gates precede normalization.
CP02 excludes acceptance and observation while rejection has zero weight, requiring noncommittal expiry.
An all-zero native fallback is not assumed.

A01 supplies a complete legal, affordable five-action opening pool with confidence 40, no unmet command concession, no poor-fit penalty, a near-complete primary supply remedy due within ten days, adequate defense, R 2, U 1, D 55 and no repudiation, paired-front penalty, invasion or scheduled peace.
Scores are negotiation 90, supply 150, consenting local discharge 70, containment 75 and waiting 40.
A02 independently supplies a fully resolving leave remedy with a secure replacement and experienced cohort, giving leave 140.
A03 compares negotiation 80 and containment 95 at confidence 20 with an unmet command concession, R 4, U 1, D 85 and repudiated negotiations.
It does not normalize this partial score comparison.
A04 has no resources or funded remedy and the last defending formation under invasion.
Raw discharge 60 and waiting 0 remain subordinate to the survival priority, and the discharge bonus is zero.
All A-series outputs are willingness scores rather than click probabilities.

## White Peace pair multipliers

WP00 through WP07 use the adapter in Part 5, “009 White Peace: settle the right war”.
The complete artificial pool consists of pair A, B, C and D with base scores 40, 30, 20 and 10.
All pass the existing Event 009 gates except in the explicitly named invalid case.
All unrelated factors are neutral, and no other candidates exist by construction.
Only pair A receives the mutiny multiplier.
For this declared proportional model, a share is the effective score divided by the sum of effective scores.

| Scenario | Context for A | Multiplier | Effective pool A, B, C, D | Total |
| --- | --- | --- | --- | --- |
| WP00 | No qualifying mutiny | 1 | 40, 30, 20, 10 | 100 |
| WP01 | One side has a relevant major mutiny | 5/4 = 1.25 | 50, 30, 20, 10 | 110 |
| WP02 | Both sides have relevant major mutinies | 7/4 = 1.75 | 70, 30, 20, 10 | 130 |
| WP03 | Both sides plus a sustained valid reciprocal front compact | 2 = 2.00 | 80, 30, 20, 10 | 140 |

| Scenario | A share | B share | C share | D share |
| --- | --- | --- | --- | --- |
| WP00 | 2/5 = 40% | 3/10 = 30% | 1/5 = 20% | 1/10 = 10% |
| WP01 | 5/11 ≈ 45.4545% | 3/11 ≈ 27.2727% | 2/11 ≈ 18.1818% | 1/11 ≈ 9.0909% |
| WP02 | 7/13 ≈ 53.8462% | 3/13 ≈ 23.0769% | 2/13 ≈ 15.3846% | 1/13 ≈ 7.6923% |
| WP03 | 4/7 ≈ 57.1429% | 3/14 ≈ 21.4286% | 1/7 ≈ 14.2857% | 1/14 ≈ 7.1429% |

The fractions total exactly one in every row.
Displayed decimals are rounded.
WP04 sets A's existing score to zero and separately applies each authored context.
WP05 retains A's base 40 but makes it ineligible and again considers each multiplier separately.
All six variants leave the effective pool at 0, 30, 20, 10, with shares 0, 1/2, 1/3 and 1/6.
Neither zero weight nor failed eligibility is revived.
WP06 makes all three nested descriptions applicable and selects only 2.00, reproducing WP03 without stacking.
WP07 gives every candidate zero weight, producing no positive pool and no Event 120-created peace candidate.

These are exact shares for the declared artificial proportional pool.
**Actual native rounding and live Event 009 owner score composition remain unverified.**
The multiplier is not a direct peace probability, and the live result requires the complete owner pool and its final scoring and selection rules.

## Limits of the evidence

All source revisions and complete scenario inputs are included in the companion JSON using filenames relative to this folder.
No MCP execution, implemented historical baseline, native probability comparison or game launch is claimed.
Exact formation identity, continuity, transfer, protected demobilization and enforceable local ceasefire remain hard implementation feasibility gates with no inferred substitute.
The effective-manpower reader, shared human-pressure adjustment, native payments, complete live country and pair pools, and global event cadence remain external inputs.
Focus probabilities and cumulative MTTH timing remain unresolved without their implemented pools and verified native semantics.
The 90-day MTTH anchor and 30 to 180-day range do not establish a timing distribution.
