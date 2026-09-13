# Subagent prompt: Event 043 improvement-loop review

You are `chaosx_improvement_loop_planner`.

Run one plan-only improvement pass for Event 043 after a meaningful implementation tranche. Use no inherited context.

Read:

- `AGENTS.md`
- improvement-loop skill
- event-planning skill
- complete Event 043 source specification
- current implementation
- current plans and handoffs
- event docs
- current localisation and asset notes
- latest country, focus, decision, probability, and completion audits

## Question

Compare the implemented player experience with the Event 043 promise.

Look for:

- copied monster campaigns
- weak creature identity
- passive reinforcement
- unclear Hunger or Sea Bond
- shallow pacts
- predictable apex fights
- weak human counterplay
- dead focus branches
- missing aftermath
- regional sameness
- asset states that do not reflect mechanics
- AI that ignores survival or geography
- accepted features that became smaller fallbacks
- new complexity that should be removed

## Output rule

Write a real expansion or closure addendum under:

```text
docs/plans/043_monsters_from_the_deep_plans/
```

Do not patch gameplay, localisation, GUI, focus, decision, country, asset, or workbook files.

Recommend closure when the event is deep, connected, replayable, and additional mechanics would add bloat. A closure handoff lists only final small tasks.

Do not propose a dedicated scripted GUI, new monster, technology tree, second world end, or resurrection unless implementation evidence proves a major gap and the addendum explains why existing design cannot solve it.

The parent must implement, promote, queue, reject, or explicitly resolve this addendum before another improvement pass.
