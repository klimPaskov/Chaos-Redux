# Event 046 probability audit prompt

Use `chaosx_ai_probability_auditor` as a read-only subagent with no inherited conversation context.

Audit every weighted or probabilistic Event 046 surface against `matrices/046_probability_scenario_matrix.md`.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, the Event 046 specifications, the live Event 46 family registry, evolution pacing, cluster membership, repeatable event configuration, direct Chaos compression, and achievement ranking logic.

## Mandatory workflow

Start every surface with `hoi4.probability_inspect`.

Name the exact source, pool, scenario IDs, candidate completeness, external factor completeness, and whether the evidence can be exact.

Use:

- `hoi4.probability_evaluate` for a complete fixed scenario
- `hoi4.probability_sweep` for capability, pool-size, weight, threshold, and distribution sensitivity
- `hoi4.probability_simulate` for sampled family coverage, conflict resolution, result distributions, and rare achievements
- `hoi4.probability_sequence` only when the parent supplies a complete custom-pool manifest covering cadence, recovery, cap reduction, cooldowns, removals, resets, timer changes, and terminal state
- `hoi4.probability_compare` after any owner-applied source change, using the same named scenarios
- `hoi4.probability_render` when a coverage, timing, sensitivity, sequence, or comparison view improves review

Do not edit source and do not choose the intended balance target.

## Required surfaces

Audit:

- eligible-family coverage by capability
- minimum floors and available-pool clamping
- Baseline and new-domain quotas
- compatibility groups and dependency bundles
- core family and owner-adapter starvation
- Evolution V mandatory coverage
- family mood weights and tail ordering
- population and industry independence
- repeated firing independence
- Event 46 repeatable weight, cap, and recovery sequence
- Evolutions I through IV MTTH behavior
- Evolution V immediate activation and bounded reachability
- Randomizations one-member and multi-member cluster behavior
- Event 21 multiple-cluster behavior when weighted
- direct Chaos compression bands
- quantile and comparable-family selection for achievements

## Pass expectations

Later capabilities must select a larger expected and allowed share of the eligible family pool.

No previous firing can alter a later family weight.

Every quota must terminate when the valid pool is smaller than its floor.

One family cannot be selected twice in one transaction unless the registry deliberately models separate compatible instances.

Evolution V must include every non-conflicting mandatory family with valid scopes and reach at least 90 percent of the eligible safe pool.

Owner adapters must remain reachable without crowding out core identity families.

Scarcity, abundance, and split moods must produce the intended ordering without reading old values.

The Randomizations cluster must never produce two Event 46 transactions from one incident.

## Output

Return one report organized by the exact `P46-*` scenario IDs.

For each scenario include source surface, revision, scenario hash, candidate pool, external factors, tool used, evidence type, result, pass or fail, starvation or dominance finding, and unresolved assumption.

After a patch, provide a `hoi4.probability_compare` result against the baseline revision.

Do not describe sampled frequency as exact probability.

When a pool or external factor is incomplete, mark the result bounded, sampled, score-only, or unresolved.
