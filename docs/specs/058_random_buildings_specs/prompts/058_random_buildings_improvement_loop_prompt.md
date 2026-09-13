# Event 58 near-completion improvement-loop prompt

Use the project custom subagent `chaosx_improvement_loop_planner` with no inherited context.

## Task

Perform one near-completion depth review of the implemented Event 58, Random Buildings.

Read:

- `AGENTS.md`
- `chaos-redux-improvement-loop`
- `chaos-redux-event-planning`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-subagents`
- every file under `docs/specs/058_random_buildings_specs/`
- every current Event 58 plan and handoff under `docs/plans/058_random_buildings_plans/`
- all Event 58 implementation, localisation, asset, event-log, achievement, documentation, and workbook surfaces
- the final Event 58 probability and completion-audit evidence available at the time of review

## Review goal

Compare the implemented feature with its playable promise: each world state independently receives valid construction, later Chaos tiers add stronger layers, rare structures remain rare, province packages use real geography, exceptional sites remain limited, and every special structure enters its owner system correctly.

Check whether the event feels thin, generic, disconnected, unreadable, repetitive, exploitable, or larger than its presentation can support. Focus on gameplay consequences, world-state reactivity, provider ownership, repeatability, result readability, achievement quality, and future extension safety.

## Anti-bloat boundary

Keep proposals within the accepted construction transaction, provider registry, reporting, achievement, and art scope. Treat scope expansion as bloat unless implementation evidence proves a necessary design gap.

Do not propose more public mechanic values. Event 58 should remain a single incident with concise result summaries.

Do not turn the event into a player-controlled construction program. Its identity depends on involuntary, independent rolls.

## Output choice

Choose exactly one result:

### Closure handoff

Use this when the implementation is deep, connected, replayable, readable, and clean enough that further expansion would add noise. List only final small tasks, validation gaps, documentation alignment, or unresolved handoffs.

### Bounded improvement addendum

Use this only when a concrete design gap remains. The addendum must name the weak implemented surface, explain how it fails the event promise, define the smallest stronger mechanic, state exact ownership and consequences, give AI or selection behavior where relevant, list presentation and asset needs, define cleanup and acceptance cases, and explain why this work is worth its maintenance cost.

Write the result to:

`docs/plans/058_random_buildings_plans/058_random_buildings_near_completion_improvement_review.md`

The planner must not edit gameplay, localisation, assets, GUI, spreadsheets, or other implementation files. It must record the disposition of any previous Event 58 improvement addendum before proposing another one.
