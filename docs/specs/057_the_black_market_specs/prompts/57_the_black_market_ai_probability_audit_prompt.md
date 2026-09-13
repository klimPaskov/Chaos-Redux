# Event 57 AI Probability Audit Prompt

Audit every weighted Event 57 surface as `chaosx_ai_probability_auditor` in read-only mode.

Read:

- `docs/specs/057_the_black_market_specs/07_ai_probability_balance_and_edge_cases.md`
- Event 57 event, decision, scripted-effect, scripted-trigger, constants, and AI files
- the current probability tool documentation and repository rules

Start every surface with `hoi4.probability_inspect`.

## Required weighted surfaces

Inspect:

- founding broker selection
- founding member selection
- invitation candidate selection
- candidate response and posture
- offer class generation
- provider-package selection
- seller and source selection
- purchase choice
- sale choice and size
- route selection
- delivery outcome
- Exposure response
- outsider investigation action
- auction bidding
- evolution MTTH

Separate hard validity from score modifiers. State whether each pool is complete. Never report an exact normalized probability from an incomplete candidate pool.

## Named scenarios

Use the same scenario IDs before and after any patch:

- `BM-P01` invitation under desperation
- `BM-P02` route proof over friendly relations
- `BM-P03` safe surplus sale
- `BM-P04` fuel purchase utility
- `BM-P05` route selection
- `BM-P06` high-Exposure posture response
- `BM-P07` provider approval gate
- `BM-P08` Grand Auction utility
- `BM-P09` embargo-circumvention demand
- `BM-P10` counter-smuggling evidence

Use the exact scenario facts and expected ordering in the source spec.

## Evidence methods

Use:

- `hoi4.probability_evaluate` when the full normalized pool is known
- `hoi4.probability_sweep` for shortage, reserve, Exposure, route pressure, embargo, and strategic-utility thresholds
- `hoi4.probability_simulate` for declared offer and invitation pools when sampling is appropriate
- `hoi4.probability_sequence` only when cadence, cooldowns, caps, recovery, expiry, route loss, and terminal states are completely declared
- `hoi4.probability_compare` after the owner patches any weight
- `hoi4.probability_render` for matrix, sensitivity, timing, or comparison evidence when useful

Label each result exact, bounded, sampled, score-only, or unresolved.

## Pass expectations

- A valid desperate embargoed wartime buyer strongly outranks a peaceful open-trade country.
- A no-route invitation candidate has hard zero regardless of relations.
- A seller near its readiness reserve has zero sale score.
- A fuel-starved naval or air power values fuel above unrelated prestige cargo.
- An open land route outranks a strained maritime route for ordinary medium cargo, while an island case reverses feasibility.
- A State Patron above Exposure `75` prioritizes cover, route burn, withdrawal, or suppression when shortage is low.
- An unapproved provider package has exact zero.
- An AI bidder abstains from an exceptional package it cannot use even when it has abundant credit.
- Event 50 raises demand only for strategically relevant packages.
- An outsider with rumor only and no route has no active seizure action.

## Audit cycle

For every weight patch:

1. record baseline inspect and scenario evidence
2. return the bounded issue to the owner
3. do not edit source
4. after the owner patch, run `hoi4.probability_compare` with the same scenarios
5. report improvement, regression, dominance, starvation, unresolved factors, and candidate-pool completeness

## Handoff

Write the audit under:

`docs/plans/057_the_black_market_plans/subagent_handoffs/`

Include:

- surface and source identifiers
- scenario hashes
- candidate-pool completeness
- baseline result
- expected ordering
- post-patch comparison when applicable
- exact blockers
- recommended owner action

Do not choose a new balance philosophy or patch gameplay.
