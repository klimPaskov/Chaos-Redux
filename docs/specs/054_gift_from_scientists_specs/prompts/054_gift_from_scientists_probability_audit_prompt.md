# Event 54 Probability Audit Prompt

Use `chaosx_ai_probability_auditor` as a read-only reviewer for Event 54 and the Scientific Research cluster.

Read the complete Event 54 specification, the technology eligibility matrix, `matrices/054_gift_from_scientists_probability_scenarios.md`, all implemented candidate and provider logic, all cluster member logic, and the current script constants.

## Mandatory tool sequence

Start every analyzed surface with `hoi4.probability_inspect`.

Use `hoi4.probability_evaluate` for exact complete pools, without-replacement sequences, candidate rejection, and member participation. Use `hoi4.probability_sweep` for pool size, provider count, recipient date, and cluster availability. Use deterministic simulation only where the declared pool remains too large or stateful for exact evaluation. Use `hoi4.probability_sequence` only when the complete event cadence, recovery, cap, cluster, cooldown, and terminal-state manifest is supplied.

Render matrices or comparisons when they make candidate shares, branch exclusions, or member probabilities easier to review.

## Technology questions

- Does every eligible technology have equal candidate weight?
- Does each country use its own current pool?
- Do draws occur without replacement?
- Does final validation remove branch conflicts after every grant?
- Does a rejected callback remove its candidate and reroll without an infinite loop?
- Does a grant package consume one slot and remove every granted node from later draws?
- Does pool exhaustion stop safely without an excluded fallback?
- Does one provider gain excessive total share because it registers many candidates?
- Do repeat firings and save-reload states preserve committed outcomes?
- Do ordinary, special research-capable, and invalid system actors follow the intended recipient rules?

## Cluster questions

- Are all five accepted member slots present with correct severities?
- Does Event 27 retain independent membership in Military Preparation?
- Can the cluster continue after Fire-Once members are exhausted?
- Are selected-anchor and optional-member probabilities consistent with the final declared model?
- Can Event 54 and Research Failure co-occur without changing either member's intended probability or state?
- Does one cluster firing count once for pacing?

## Evidence contract

Run every applicable named scenario from the scenario matrix. State whether each result is exact, bounded, sampled, score-only, or unresolved. Report the complete candidate pool and external factors when normalization applies.

Do not choose new balance targets and do not patch source. When a result differs from the accepted specification, identify the exact surface, scenario, observed value, expected relationship, and owner who must decide or patch it.

After any candidate weight, provider set, branch family, cluster membership, participation weight, or AI factor changes, rerun the same scenario IDs and use `hoi4.probability_compare` against the baseline.
