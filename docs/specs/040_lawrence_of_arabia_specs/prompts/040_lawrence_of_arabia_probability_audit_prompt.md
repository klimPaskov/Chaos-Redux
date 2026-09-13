# Event 40 Probability Audit Prompt

Use `chaosx_ai_probability_auditor` for every weighted Event 40 surface.

## Required reading

Read:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-focus-trees`
- `chaos-redux-subagents`
- the implemented Event 40 weighted source files
- `quality/040_lawrence_of_arabia_probability_scenarios.md`

The auditor is read-only. It does not select balance targets and does not patch source.

## Mandatory workflow

1. Run `hoi4.probability_inspect` for the exact surface.
2. Confirm whether the candidate pool and external factors are complete.
3. Evaluate the named baseline scenarios.
4. Classify each result as exact, bounded, sampled, score-only, or unresolved.
5. Let the owning parent or patch-capable agent change source.
6. Run `hoi4.probability_compare` with the same scenarios.
7. Render timing, matrix, sensitivity, or comparison evidence when it improves review.

Use sweeps for thresholds and strategy transitions. Use simulation only when the inspected surface and scenario contract support sampling. Use sequence analysis only when cadence, cooldowns, removals, recovery, resets, and terminal states are fully declared.

## Required surfaces

- initial target selection
- later target selection
- British commitment decisions
- target decisions
- incident families
- Evolution I cells, coups, and revolts
- Evolution II client contribution and counter-bloc behavior
- Evolution III core and federation outcome selection
- Lawrence defection
- Lawrence's Kingdom
- federation focus AI
- mission priority

## Required report

For each scenario state:

- scenario ID
- source surface
- inspected candidate pool
- relevant external factors
- result type
- intended ordering
- observed ordering or probability
- dominant or starved candidates
- invalid candidates that remained positive
- unresolved facts
- baseline revision
- comparison revision
- material change
- recommendation to the owning agent

Do not write an exact probability when the normalized pool is incomplete.

Any finding that needs a source change returns to the parent or owning agent. The auditor then runs comparison evidence after the patch.
