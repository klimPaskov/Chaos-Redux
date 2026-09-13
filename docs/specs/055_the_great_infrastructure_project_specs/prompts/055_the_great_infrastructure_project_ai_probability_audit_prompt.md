# AI Probability Audit Prompt for Event 55

Run the required read-only weighted-logic audit for Event 55 after the relevant target, proposal, method, partner, and trouble-response weights exist.

Use `chaosx_ai_probability_auditor` with a context-complete prompt and no inherited conversation context.

Read:

- `quality/055_the_great_infrastructure_project_probability_scenario_matrix.md`
- the Event 55 source specs
- the final Event 55 event, decision, trigger, effect, and AI files
- the current complete candidate pools and external factor contracts

## Required surfaces

1. Event 55 country target selection
2. Project family candidate selection
3. Route or facility target selection inside each family
4. Construction method AI choice
5. Partner acceptance, counteroffer, delay, and refusal
6. Project trouble response, including repair, reroute, reduction, suspension, and abandonment
7. Repeat-firing outcome selection
8. Evolution timing when weighted logic is used

## Required workflow

- Start every surface with `hoi4.probability_inspect`.
- Record whether the candidate pool and external state are complete.
- Run the named scenario IDs from the matrix.
- Use `hoi4.probability_evaluate` for score and normalized results where complete.
- Use sweeps for National Works Capacity, war state, project scale, partner count, relations, embargo, and equipment reserves.
- Use rendering for matrices and sensitivity views when it improves review.
- Do not use sequence analysis unless the complete repeatable event pool, cooldown, cap, recovery, removal, and timer contract is supplied.
- Classify evidence as exact, bounded, sampled, score-only, or unresolved.
- The auditor does not patch source and does not choose the desired balance target.

## Hard checks

- invalid special and capitulated targets are zero
- recent target cooldown is zero
- invalid project families are zero
- unregistered fixed crossings are zero
- hostile foreign routes without consent are zero
- stale partner generations are zero
- no one ordinary family dominates a mixed valid pool without a geographic reason
- unserved countries remain strongly preferred while many exist
- recovery actions outrank weak new projects during serious project trouble
- AI does not consume critical transport stockpiles without strategic benefit

## Patch and compare cycle

Return the baseline evidence to the parent. The parent or owning patch agent applies any accepted weight change. Then rerun `hoi4.probability_compare` against the same named scenarios and report every ordering, dominance, starvation, and hard-zero change.

Do not accept a weight patch without the compare pass.
