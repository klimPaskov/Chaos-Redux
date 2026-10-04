# Event 021 target ticket resolution, 2026-10-05

Disposition: implemented (agent decision D20 in `agent_decisions_2026-10-04.md`). Live selection shares remain `needs_live_game`, and the MCP probability baseline and compare are blocked as recorded below.
Acceptance basis: the lead's round 2 assignment and the user's full-authority takeover grant.

## Change

`event021_parent_add_target_to_selection_pool` turns a candidate's 0-1000 target weight into selection tickets by dividing by `event021_parent_tuning.target_pool_weight_scale`, rounding, and clamping to 1 through `target_pool_weight_cap`, before the shared individual-crisis load curve multiplies the result by 4, 2, or 1.
The scale falls from 100 to 25 and the cap rises from 10 to 40, so the product still spans the full 0-1000 score and the top of the range keeps the same relative ticket count.
The same helper now creates `individual_crisis_candidate_adjusted_weight` before calling `adjust_individual_crisis_candidate_ticket_weight`, as the shared helper's contract and the repository's helper-output rule require. The manual-scenario ticket helper `event021_parent_add_scenario_target_to_weighted_pool` receives the same initialization, without any change to its ladder.
No target score, major factor, load curve, or draw budget changed, and the change affects only which candidate is drawn, never whether Event 021 fires.

A prefire visits at most `maximum_review_scan` (6) registered countries, so the pool holds at most 6 x 40 x 4 = 960 entries and each country's ticket loop runs at most 160 times, below the engine's 1,000-iteration loop limit.

## Base tickets before and after

Major weight is the raw score multiplied by `major_target_factor` (0.35) and rounded, as `event021_random_civil_war_prepare_target` does. Ticket counts are before the shared load curve, which multiplies both sides equally. Rounding is taken as half away from zero.

| Raw score | Minor weight | Major weight | Minor tickets before | Major tickets before | Minor tickets after | Major tickets after |
| --- | --- | --- | --- | --- | --- | --- |
| 40 | 40 | 14 | 1 | 1 | 2 | 1 |
| 60 | 60 | 21 | 1 | 1 | 2 | 1 |
| 90 | 90 | 31 | 1 | 1 | 4 | 1 |
| 120 | 120 | 42 | 1 | 1 | 5 | 2 |
| 150 | 150 | 53 | 2 | 1 | 6 | 2 |
| 200 | 200 | 70 | 2 | 1 | 8 | 3 |
| 250 | 250 | 88 | 3 | 1 | 10 | 4 |
| 300 | 300 | 105 | 3 | 1 | 12 | 4 |
| 400 | 400 | 140 | 4 | 1 | 16 | 6 |
| 500 | 500 | 175 | 5 | 2 | 20 | 7 |
| 700 | 700 | 245 | 7 | 2 | 28 | 10 |
| 1000 | 1000 | 350 | 10 | 4 | 40 | 14 |

Before the change a major and a minor with the same raw score drew the same single ticket for every raw score below 150. After it they draw the same ticket only below a raw score of 38.
Every candidate has a valid actor route (+80) and the base score (+10), so a candidate without the recent-war memory penalty starts at a raw score of 90, inside the band where the major reduction now holds.
Only a recent-memory candidate with fracture pressure below 17 can still fall under 38, where both kinds draw one ticket.

## Named TGT scenarios (local arithmetic)

These use the TGT scenario names from `docs/specs/021_random_civil_war_specs/021_random_civil_war_probability_scenario_matrix.md`, evaluated at load zero with representative scores built from `random_civil_war_target_weight`. A is the first country and B the second.

| Scenario | Country A | Country B | Tickets before (share of A) | Tickets after (share of A) |
| --- | --- | --- | --- | --- |
| TGT-02 | Unstable minor, pressure 60, failing authority: raw 420, weight 420 | Stable major after Evolution I, pressure 20: raw 220, weight 77 | 4 : 1 (80%) | 17 : 3 (85%) |
| TGT-03 | Stable minor, pressure 20: raw 170, weight 170 | Unstable major after Evolution I, pressure 70, failing authority: raw 510, weight 179 | 2 : 2 (50%) | 7 : 7 (50%) |
| TGT-04 | Fresh minor, pressure 40: raw 250, weight 250 | Former target past its cooldown, pressure 40, recent memory: raw 130, weight 130 | 3 : 1 (75%) | 10 : 5 (67%) |
| TGT-05 | AI minor, pressure 40: raw 250, weight 250 | Player minor, pressure 40: raw 275, weight 275 | 3 : 3 (50%) | 10 : 11 (48%) |
| Low band | Minor, raw 120 | Major, raw 120: weight 42 | 1 : 1 (50%) | 5 : 2 (71%) |

TGT-02 and TGT-03 keep their intents: the minor stays favored over a stable major, and an unstable major becomes a real but not dominant candidate.
TGT-05 stays similar.
TGT-04 still favors the fresh country, now in proportion to the scores (about 2:1) rather than the 3:1 that came from rounding 2.5 up and 1.3 down. A former target is also held out entirely by `random_civil_war_recent_target` until its cooldown ends, so this scenario only describes the period after that hard gate.
The TGT-01, TGT-08, and TGT-10 zero-weight and eligibility outcomes are unchanged because they are decided before ticket conversion.

## MCP probability route

The baseline and compare were attempted once, as the assignment allows. Running as a subagent, this engineer could not spawn `chaosx_ai_probability_auditor`, so the call was made directly.
`hoi4.probability_inspect` with `adapter = custom_weighted_pool` and `source = { path = common/scripted_effects/021_random_civil_war_parent_effects.txt }` (no refresh) returned `INTERNAL_ERROR` with no artifact.
It was not retried, and no `hoi4.probability_compare` was run. The October 3 attempt on the same surface had timed out after 600 seconds.
The before sources for a later compare are the parent effects and constants files at commit `f22c3e53e`, whose working-copy bytes had SHA-256 `405dea3b4755de8d756d41e7e061fd8e5bb1b6fd0e09ba37715d14a4dd4804e6` and `6b1bf54f76d0b52557a6776ce7958ad1f5a4ca1041a91d1fa1953b287657665a`.
