# Event 050 AI probability audit prompt

Perform a read-only audit of every Event 050 weighted surface.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, the Event 50 AI spec, the probability scenario matrix, current source files, and the complete external state used by each pool.

Start every surface with `hoi4.probability_inspect`. Name the scenario IDs exactly as listed in `matrices/050_probability_scenario_matrix.md`. State whether the candidate pool and external factors are complete.

## Surfaces

Audit:

- player versus major target class
- target selection inside each class
- convenor selection
- core-enforcer selection
- neutral and intermediary selection
- participant opening choices
- participant review choices
- target response AI
- smuggling outcomes
- intermediary acceptance
- secondary-sanction targets and responses
- settlement acceptance
- Evolution I timing
- Evolution II target count and additional target selection
- sanction-breaker cooperation
- coalition fatigue choices

## Evidence rules

Use `hoi4.probability_evaluate` for fixed scenarios, `hoi4.probability_sweep` for sensitivity, and `hoi4.probability_compare` after an owner patch. Use simulation only when the complete normalized pool is supplied. Use sequence analysis only when cadence, caps, recovery, cooldowns, removals, resets, and terminal states are fully declared.

Distinguish exact, bounded, sampled, score-only, and unresolved results. Do not infer exact probabilities from an incomplete pool. Do not choose the balance target and do not patch source.

## Required behavior checks

- Player-class chance does not multiply with player count.
- Active and excluded targets have zero effective weight.
- Resource suppliers, shipping powers, and real corridors outrank symbolic participants when building the coalition.
- Import-dependent weak targets prefer routes or concessions over defiance and suicidal war.
- Strong self-sufficient targets consider defiance and adaptation.
- Resource Seizure becomes competitive only with a valid military case.
- Evolution I increases exposure risk without making smuggling irrelevant.
- Evolution II respects distinct targets and the active cap.
- Twelve-month fatigue changes participant choices in the intended direction.

## Output

Return scenario hashes or equivalent identifiers, pool completeness, evaluated ordering, sensitivity findings, dominance or starvation risks, unresolved external factors, and required owner changes. After the owner patch, compare the same scenarios and state whether the intended ordering changed without breaking safety cases.
