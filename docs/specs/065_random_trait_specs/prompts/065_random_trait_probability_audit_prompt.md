# Event 065 Random Trait Probability Audit Prompt

## Role

Run `chaosx_ai_probability_auditor` after the generated registry and runtime pool exist.

Use `fork_context=false`.

Read `AGENTS.md`, all Event 65 specification files, the trait registry summary, the generated probability input manifest, the scripted-system architecture handoff, and:

`quality/065_random_trait_probability_scenario_matrix.md`

Remain read-only.

## Mandatory tool order

1. Start with `hoi4.probability_inspect` on the real Event 65 runtime selection logic.
2. Use `hoi4.probability_evaluate` for exact declared scenarios.
3. Use `hoi4.probability_sweep` for threshold, class-share, settings, and high-saturation scenarios.
4. Use `hoi4.probability_sequence` only when the complete multi-slot pool and state transitions are declared.
5. Use `hoi4.probability_compare` for flat-versus-hierarchical logic, direct-versus-cluster paths, and post-patch review.
6. Use `hoi4.probability_render` for the class matrix, threshold sweep, dispatcher comparison, and unresolved views.
7. Use seeded simulation only when an implementation detail cannot be represented exactly.
8. Label exact, bounded, sampled, score-only, and unresolved evidence separately.

## Required checks

Audit every named scenario `P01` through `P30`.

Confirm:

- uniform Baseline
- uniform Evolution I
- ordinary weight `100`
- featured weight `125` at Evolution II
- featured weight `150` at Evolution III
- no stacked featured reasons
- every eligible trait has positive probability
- every excluded trait has zero probability
- ordinary mass floors
- exact collision renormalization
- exact same-firing without-replacement behavior
- fair high-saturation behavior
- complete content-profile inputs
- one final entry per source ID
- load-order override correctness
- hierarchical dispatcher equivalence when used
- direct and cluster parity
- correct threshold and Evolution-setting transitions

Do not choose a new balance target.

When a target fails, report the measured behavior and the smallest relevant cause.

The main implementation agent owns the patch.

Run `hoi4.probability_compare` again after a patch before marking the scenario passed.

## Output

Write:

`docs/plans/065_random_trait_plans/subagent_handoffs/065_random_trait_probability_audit.md`

Include:

- inspected files and artifacts
- registry version and checksum
- content profiles
- entry and class counts
- exact formulas
- scenario table
- dominance and starvation results
- threshold sweep
- high-saturation result
- direct and cluster comparison
- flat and hierarchical comparison
- sampled uncertainty when any
- blockers
- final status of pass, fail, blocked, or needs user review

If the required probability route is unavailable, record the exact blocker.

Do not replace it with source-only confidence.
