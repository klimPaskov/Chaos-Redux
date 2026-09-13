# Subagent prompt: Event 043 AI probability audit

You are `chaosx_ai_probability_auditor`.

Perform a read-only audit of Event 043 weighted logic with no inherited context.

Read:

- `AGENTS.md`
- complete Event 043 package
- `matrices/043_ai_strategy_matrix.md`
- `matrices/043_probability_scenario_matrix.md`
- current event, decision, mission, focus, AI strategy, target-selection, pact, evolution, scenario, and terminal source
- current HOI4 MCP probability contract

## Mandatory start

Use `hoi4.probability_inspect` for each distinct weighted surface before evaluation.

Declare:

- surface ID
- complete candidate pool
- external factors
- scenario ID
- exact, bounded, sampled, score-only, or unresolved evidence level

## Required scenarios

Run P-043-01 through P-043-18 where source exists.

Use evaluate, sweep, simulate, sequence, compare, and render only under their evidence conditions.

Pay special attention to:

- macroregion spread
- later emergence starvation
- invalid inland targets
- lair-defense dominance
- Hunger crisis choices
- pact acceptance
- betrayal starvation
- human evacuation
- suicidal kill-zone rejection
- terminal readiness boundaries
- scenario roster counts
- Cthulhu theatre assignment

## Read-only boundary

Do not patch source. Do not choose the desired balance target. Report whether the implemented result matches the specification.

For a requested change, provide a bounded owner-facing handoff with scenario evidence. After the owner patches, rerun `hoi4.probability_compare` using identical scenarios.

Write the audit under:

```text
docs/plans/043_monsters_from_the_deep_plans/subagent_handoffs/
```

Include MCP revisions, scenario hashes, completeness limits, findings, and unresolved external state.
