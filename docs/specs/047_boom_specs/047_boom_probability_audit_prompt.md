# Event 47 BOOM probability audit prompt

Route this work to `chaosx_ai_probability_auditor` as a read-only pass. Use the HOI4 MCP probability workflow and begin with `hoi4.probability_inspect`.

## Surfaces to inspect

1. Uniform first-epicenter selection from the complete eligible-state pool.
2. Evolution II rolled epicenter count.
3. Evolution II resolved epicenter count after pool shortages.
4. Separation-tier candidate selection.
5. Bigger BOOM active-history MTTH.
6. BOOM BOOM BOOM active-history MTTH.

## Named scenarios

### `boom_target_uniform_small_pool`

Use a complete frozen pool of ten eligible states across countries of different sizes. Verify that every state has equal first-target probability. Confirm that country size, player status, major status, war status, and ideology contribute no hidden weight.

### `boom_target_exclusion_pool`

Include valid ordinary states, an actual nonhuman state, an unowned state, a state below the population threshold, and a state that cannot receive the transaction. Verify that excluded states have zero probability and the remaining ordinary states normalize uniformly.

### `boom_multi_count_800`

At Chaos 800 to 899 with a complete pool, verify the intended 75 percent two-blast and 25 percent three-blast distribution.

### `boom_multi_count_900`

At Chaos 900 and above with a complete pool, verify the intended 60 percent two-blast and 40 percent three-blast distribution.

### `boom_multi_shortage`

Test pools that can safely resolve three, two, one, and zero targets. Distinguish rolled count from resolved count and prove clean degradation.

### `boom_separation_continent`

Provide several candidates on another continent and several closer candidates. Verify that the different-continent tier dominates while valid candidates exist.

### `boom_separation_region`

Remove different-continent candidates. Verify that different strategic regions and nonadjacency dominate same-region choices.

### `boom_separation_fallback`

Remove high-tier candidates step by step and verify the selector advances through the declared fallback ladder without starvation or unbounded retries.

### `boom_evolution_one_pacing`

Compare the base 90-day MTTH with Chaos 500+, prior Event 47 firings, and high exact recent casualty totals. Verify monotonic direction and one-time activation.

### `boom_evolution_two_pacing`

Compare the base 110-day MTTH with Chaos 900+, a prior evolved incident, and several past firings. Verify that Evolution II cannot record twice.

## Evidence standard

State whether each result is exact, bounded, sampled, score-only, or unresolved. Record the candidate pool, external factors, scenario hash, and tool revision.

Use `hoi4.probability_evaluate` for complete static pools, `hoi4.probability_sweep` for threshold and factor changes, `hoi4.probability_simulate` when bounded retry resolution needs sampling, and `hoi4.probability_compare` after any source change.

The auditor does not choose new balance targets and does not patch source.
