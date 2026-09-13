# Probability-audit prompt for Event 58 Random Buildings

Use this prompt with `chaosx_ai_probability_auditor`. The audit concerns random selection and cluster participation, not AI decision clicks.

Spawn with `fork_context=false`.

Read `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, the full Event 58 specification package, `quality/058_random_buildings_probability_scenarios.md`, the repository explorer handoff, and the exact implemented weight, provider, fallback, cluster, and exceptional-budget source files.

## Required workflow

Start every surface with `hoi4.probability_inspect`.

Audit:

- baseline risk bands
- baseline entry weights
- Evolution I risk bands
- Evolution I entry weights
- Evolution II province-package weights
- Evolution III provider and location selection
- Positive Economy cluster participation
- repeat-firing saturation behavior

Use `hoi4.probability_evaluate` for named scenarios, `hoi4.probability_sweep` for thresholds and rank reversals, and `hoi4.probability_compare` for every implemented tuning change. Use simulation only for declared uncertain inputs. Use sequence analysis only if the complete repeatable pool, cadence, cap, recovery, cooldown, removal, timer, and terminal state are supplied. Render matrices, rankings, sensitivities, comparisons, timing, or unresolved views when useful.

## Core questions

- Do restricted baseline entries remain at or below their accepted world rarity envelope?
- Do rare and extreme Evolution I entries remain uncommon when ordinary candidates become invalid?
- Does safer-only fallback work without upward rarity drift?
- Do factories and dockyards remain a minority of baseline results in a representative mixed world?
- Does ordinary Evolution I construction dominate while advanced entries remain visible at world scale?
- Do rail and ordinary defense packages lead Evolution II without starving ports or supply hubs?
- Can one exceptional provider monopolize the limited budget through duplicate locations or contextual modifiers?
- Does saturation on repeat firings inflate dangerous entries?
- Does Event 58 behave as a meaningful Medium Positive Economy member without approaching guaranteed secondary participation?

## Scenario discipline

Use every scenario ID in `quality/058_random_buildings_probability_scenarios.md` that the implementation can resolve.

For each scenario, state:

- complete candidate pool or missing entries
- external factors
- DLC state
- active evolution state
- validity and capacity assumptions
- score or probability model
- exact, bounded, sampled, score-only, or unresolved result
- artifact URI, revision, and scenario hash

Never state an exact probability from an incomplete candidate pool.

## Before and after requirement

Produce a baseline audit before any owner patches the weights.

After the owner applies a bounded change, run `hoi4.probability_compare` on the same scenarios. Report dominance, starvation, rank reversal, rarity drift, repetition, and exploit risk.

Remain read-only. Recommend concrete fixes with source paths and identifiers, but do not patch the weights.
