# Event 059 AI probability audit prompt

Spawn `chaosx_ai_probability_auditor` with `fork_context=false` for every complex weighted AI surface used by Event 059. The auditor is read-only.

## Inputs

Provide:

- the complete Event 059 spec pack
- `matrices/059_the_offensive_ai_scenario_matrix.md`
- the final AI architecture plan
- every implemented AI strategy, plan, factor, weight, and competing candidate pool
- current vanilla and Chaos Redux baseline behavior
- the exact evolution and country-role conditions

## Required workflow

1. Begin with `hoi4.probability_inspect` for the complete relevant pool.
2. Run `hoi4.probability_evaluate` for each named scenario that applies.
3. Run `hoi4.probability_sweep` across local strength, supply, reserve, equipment trend, manpower, fuel, active-war count, target value, legal-path validity, naval capacity, coalition strength, country capacity, and evolution combination.
4. Run `hoi4.probability_compare` between the unmodified baseline, Event 059 baseline, each individual evolution, and the full enabled stack.
5. Use `hoi4.probability_render` for scenario rankings, sensitivity, timing, and unresolved cases.
6. Use `hoi4.probability_simulate` only for a clearly declared uncertain input.
7. Do not use `hoi4.probability_sequence` unless a complete custom pool manifest defines cadence, recovery, caps, removals, resets, cooldowns, and terminal states.

## Audit questions

- Do supplied favorable fronts move upward in attack ranking?
- Do critical supply, manpower, equipment, fuel, reserve, and transport failures remain blocked?
- Does Evolution I change continuation more than war opening?
- Does Evolution II change valid opportunity use while unrelated weak targets remain invalid?
- Does Evolution III increase scale and risk without cancelling safety floors?
- Does disabling one evolution remove only its own channel?
- Can owner-specific plans dominate when required?
- Do weak minors avoid impossible production programs?
- Do replacement and recovery plans retain enough weight?
- Do human-control cases evaluate Event 059 as inactive?
- Does the authoritative Diplomacy cluster role and chance avoid making the permanent event appear too often as a bundled member?

## Reporting

For each finding, label the evidence as exact, bounded, score-only, sampled, or unresolved. Do not convert a strategy score into an exact click or declaration probability unless the complete normalized pool and all external factors are included.

Write the handoff under `docs/plans/059_the_offensive_plans/subagent_handoffs/`. Include:

- inspected files and identifiers
- scenarios run
- sweeps and rank reversals
- baseline and final comparisons
- starvation and dominance findings
- timing findings for evolutions and cluster participation
- unresolved engine behavior
- recommended tuning changes
- proof that the auditor did not edit source
