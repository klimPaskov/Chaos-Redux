# Subagent Prompt: Event 021 AI and Probability Auditor

Spawn `chaosx_ai_probability_auditor` with `fork_context=false`.

This agent is read-only.

Read:

- `docs/specs/021_random_civil_war_specs/021_random_civil_war_probability_scenario_matrix.md`
- all Event 021 weighted source files named by the parent
- the current full candidate pools and external factors
- relevant Event 006 and Wars cluster weighted logic

Start with `hoi4.probability_inspect`.

Audit the exact surfaces for:

- automatic target selection
- opening severity
- archetype selection
- Event 006 independence selection
- Evolution I side count
- major-country eligibility
- active-evolution timing
- Evolution II neighboring exposure
- strange-incident timing and selection
- Evolution III review, queue, and launch ordering
- recurrence timing
- settlement AI
- sponsor AI
- neighbor AI
- cluster member interaction when the complete pool is known
- scenario target share and actor composition

Use named scenarios from the matrix.

Use:

- `hoi4.probability_evaluate` for exact named cases
- `hoi4.probability_sweep` for thresholds and rank reversals
- `hoi4.probability_simulate` only for declared uncertain inputs
- `hoi4.probability_sequence` only when cadence, caps, cooldowns, removals, recovery, resets, and terminal states are complete
- `hoi4.probability_render` when a matrix or timing view improves review
- `hoi4.probability_compare` after a parent or owning agent patch, using the same scenario IDs

Distinguish exact, bounded, sampled, score-only, and unresolved evidence.

Do not choose balance targets and do not patch source.

Write:

`docs/plans/021_random_civil_war_plans/subagent_handoffs/ai_probability_audit.md`

Include source surface, scenario IDs, pool completeness, expected order, observed order, starvation or dominance findings, unresolved inputs, MCP evidence references, and required parent decisions.
