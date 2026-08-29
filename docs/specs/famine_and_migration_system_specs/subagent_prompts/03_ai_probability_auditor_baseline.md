# Prompt for `chaosx_ai_probability_auditor`

Spawn with `fork_context=false`.

Repository root: `<MOD_ROOT>`.

Read:

- `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_probability_scenarios.csv`
- the complete system specs
- the final weighted source files named by the parent

Start with `hoi4.probability_inspect` for every in-scope surface.

Audit:

- famine response AI
- concealment and extraction choices
- origin evacuation choices
- destination and route pools
- border policies
- controlled outbreak reception
- corridor acceptance
- requisition and relief donor pools
- voluntary return, integration, resettlement, and forced return
- political opposition movement selection
- any declared registry or cohort sequence with a complete cadence and state manifest

Use the exact scenario IDs from the CSV.

For each scenario, state:

- analyzed surface
- complete or incomplete candidate pool
- external factors supplied
- expected ordering from the spec
- observed scores or probabilities
- exact, bounded, sampled, score-only, or unresolved status
- starvation, dominance, invalid-candidate, and sensitivity findings

Use evaluate, sweep, simulate, render, sequence, or compare only when their evidence conditions are satisfied.

This subagent is read-only. Do not choose the balance target and do not patch source.

Baseline report path:

```text
docs/plans/famine_and_migration_system_plans/ai_probability_baseline.md
```

After the parent applies weighted patches, rerun the same scenarios and require `hoi4.probability_compare`. Write:

```text
docs/plans/famine_and_migration_system_plans/ai_probability_compare.md
```
