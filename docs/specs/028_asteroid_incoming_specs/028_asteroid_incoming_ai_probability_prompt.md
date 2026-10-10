# AI probability audit prompt for Event 028: Asteroid Incoming

Role: read-only `chaosx_ai_probability_auditor`.
The named scenarios and expected orderings are in [Part 7](028_asteroid_incoming_spec_part_7_ai_multiplayer_and_balance.md#probability-scenarios); weights are in `asteroid_incoming_ai` and the `ai_*` keys of `asteroid_incoming_recovery`.
Current coverage is recorded in the [October 7 probability resume](../../plans/028_asteroid_incoming_plans/subagent_handoffs/probability_resume_20261007.md): `AST_AI_01` has one conditional result on a populated fixture with a declared no-friendly-neighbour assumption; the remaining scenarios and sweeps are open.

## Method

- Start with `hoi4.probability_inspect` on the complete four-option pool of `chaosx.nr28.1` (identical to `chaosx.nr28.8`), then evaluate each named scenario.
- Separate option score, eligibility and normalized probability, and mark each result exact, bounded, sampled, score-only or unresolved.
- Sweep Chaos (0 to 999), surrender progress, target relation, target value, fragmentation and chooser stability or war support.
- For recovery decisions, evaluate the complete visible pool in each Part 7 recovery scenario.
- When a tool cannot model a surface (the crater AI strategy and peace desires have no adapter), calculate representative cases from the script and state the assumptions.
- Follow the CLAUDE.md retry limit: one corrected retry per failure, then source calculation.

## Comparison

Before an owner changes any weight, record the baseline for the affected scenarios.
After the patch, compare with the same scenarios and report changed ordering, protected-target regressions and new starvation.
Do not patch source or pick balance targets that conflict with the spec.
