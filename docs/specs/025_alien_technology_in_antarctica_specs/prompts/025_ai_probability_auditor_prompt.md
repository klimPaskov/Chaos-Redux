# Event 025 AI probability auditor prompt

Spawn `chaosx_ai_probability_auditor` with `fork_context=false` before any weighted implementation patch and again after the owner patch.

This is read-only.

Read:

- `specs/009_ai_strategy_and_probability.md`
- `matrices/025_ai_probability_scenarios.md`
- live participant selection, route selection, action weights, rival targets, withdrawal logic, evolution MTTH, random lists, and reward-selection surfaces

Start every surface with `hoi4.probability_inspect`.

Evaluate the named participation scenarios P01 through P07 and P14, action scenarios, rival-target scenarios, timing scenarios T01 through T08, and same-day resolution scenario P15. State whether each pool and external factor set is complete.

Use `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_simulate`, `hoi4.probability_compare`, and `hoi4.probability_render` only when their evidence conditions are met. Use sequence analysis only when the complete participant-pulse manifest declares cadence, removals, resets, cooldowns, and terminal states.

Return exact, bounded, sampled, score-only, or unresolved evidence separately. Do not choose balance targets and do not patch source.

Baseline report path:

`docs/plans/025_alien_technology_in_antarctica_plans/025_ai_probability_baseline.md`

Post-patch comparison path:

`docs/plans/025_alien_technology_in_antarctica_plans/025_ai_probability_compare.md`
