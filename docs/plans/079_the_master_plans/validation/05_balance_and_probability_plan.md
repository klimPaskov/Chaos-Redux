# Balance, probability, and performance plan

## What is fixed and what is initial tuning

The user's core requirements fix independent AI minor targets, every major and player as a participant, separate Influence, real puppet victory, the five action families, direct rivalry, and the two evolution thresholds. This package's 100 finish line, 45 seed cap, three campaign slots, five Great Game target slots, action costs, loss budgets, and time values are authored starting points.

The mechanics specification is complete enough to implement those numbers. It does not establish that they are balanced. Change a tuning value in the central constants and update its specification and tests together. Do not create a hidden AI-only alternative.

## Hypotheses to test

An aligned sponsor should need fewer or cheaper political completions than a weak ideological outsider. A concentrated minor should have a plausible win path against majors that allocate resources elsewhere. Strong material help should matter without making every rich major finish instantly. Rival interference should change close outcomes without preventing all completion. The Great Game should create allocation choices under the three-action cap.

The industrial contracts intentionally grant defined output for a paid period of unavailable factories. Their ratio is an event balance choice. Compare their full opportunity cost to ordinary construction and the value of a puppet. Test for a strategy that farms efficient factory grants, then deliberately cancels or releases clients for repeated rewards.

## Sensitivity grid

| Variable | Values to inspect | Main observation |
| --- | --- | --- |
| Seed cap | 35, 40, 45 | Whether initial relations dominate the entire race |
| Political anchor scale | 75%, 100%, 125% of initial anchors | Time to finish and value of alignment changes |
| Baseline rival loss budget | 5, 10, 15 | Stalling versus meaningful interference |
| Repeated-family floor | 50%, 75% | Route variety and strength of a single-button strategy |
| Sponsor campaign cap | 2, 3, 4 | Minor feasibility and Great Game allocation pressure |
| Industrial duration | 75%, 100%, 125% | Whether projects finish in time and are worth funding |
| AI reserve levels | Initial values ±25 political power | Participation rate and wartime overspending |
| Target capacity | 3, 5 | UI load, AI dispersion, and number of unresolved races |

These are test alternatives, not simultaneous runtime variants. The shipped candidate remains the values in the core specification until evidence justifies a change.

## Probability work

No custom random success roll is introduced for ordinary Influence actions or the defined incidents. Evolution maturation and the shared event selector still require the project's actual probability tools. AI willingness scores require inspection of the actual consumer before interpreting them.

Run `hoi4.probability_inspect` first. Evaluate baseline, post-threshold, rapidly changing Chaos, disabled stages, full capacity, unavailable targets, and multiple timer sources. Use scheduled state changes for a horizon in which Chaos or availability changes. Keep exact, bounded, sampled, and unresolved results separate.

Do not apply a remembered generic MTTH survival formula to this project without the verified game-version adapter. Ninety-day MTTH is a parameter. It is not automatically a promise that half the sample evolves by day 90 under changing conditions.

## Performance

Measure active-target count, participant count, active actions, pending receipts, and callback work. Daily work must be proportional to active event-owned records. Avoid recurring whole-world country scans for rank updates. Build rank views only when authoritative scores change or when a view is opened after invalidation.

Test five active targets with many registered majors and two human clients. Save/load should rebuild presentation caches without replaying payments. Expired histories can be compacted after their longest gameplay window and after achievement facts have been summarized, but permanent refund and victory receipts need safe retained proofs.

## Reference model boundary

The included Python model checks selected score and lifecycle invariants. It has no HOI4 engine, diplomacy, country database, pathfinding, GUI, native stockpile variants, or AI decision consumer. Its pass result cannot close any installed-engine gate or establish a campaign win rate.
