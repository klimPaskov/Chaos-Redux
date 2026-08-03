# Event 016 country-settlement probability source inspection

## Scope

This is a read-only weighted-logic source inspection for the finite ten-country settlement layer. It does not claim normalized probabilities, runtime AI behavior, transfer safety, affordability, or live campaign acceptance.

## Evidence

- `hoi4_probability_inspect` used adapter `event_option_ai_chance` against `events/016_brilliant_scientist_context_events.txt`.
- The current source returned `PROBABILITY_SOURCE_INSPECTED` with validation passed, no diagnostics, and no blockers.
- The adapter discovered 21 event-option candidates, six required inputs, and one unresolved source input. The candidate pool is intentionally incomplete for normalized evaluation because host, ideology, war, Exposure, Dependence, and Grievance state are runtime inputs.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7985be084bdbc3aa4de3c54f7e5220bfacc84d3218bac94528ac0838348f5364/8f8ed66e5d3026653dd2a8aaa31c0b214db006e722acc5fb20999d1e8f5890b1/probability-inspect-b5ae25990c04.json`.

## Disposition

The result upgrades source-discovery evidence for the `.5`, `.7`, and `.8` event-option surface, but it does not close the remaining acceptance item. Named-state evaluations, rank reversals, affordability, transfer and cleanup scenarios, quantitative balance, and live AI behavior remain open. No gameplay source was changed.

