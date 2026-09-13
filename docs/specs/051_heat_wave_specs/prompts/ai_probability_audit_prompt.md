# AI Probability Audit Prompt

Act as the read-only `chaosx_ai_probability_auditor` for Event 051 Heat Wave.

Use no inherited context. Read:

- `AGENTS.md`
- probability requirements in `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`
- `docs/specs/051_heat_wave_specs/14_ai_strategy_and_probability_scenarios.md`
- all live Event 051 weighted source

## Required workflow

Start with `hoi4.probability_inspect` for every weighted surface:

- national protection priority
- decision willingness
- state target selection
- mission target selection
- surge and regional amplification selection
- report selection where gameplay effects depend on weights
- evolution MTTH factors

Use the full candidate pool when normalization applies. State whether results are exact, bounded, sampled, score-only, or unresolved.

Run named scenarios `HW-AI-01` through `HW-AI-14` exactly as specified. Use evaluate and sweep for baseline evidence. Use simulate only when the complete pool and state changes are declared. Use sequence only when cadence, costs, cooldowns, and terminal states are complete.

## Expectations

Check:

- no universal priority dominance
- no Balanced Plan default monopoly
- invalid actions weight zero
- stockpile reserves remain protected
- lethal cities outrank minor industry in peace
- existential fronts remain defended
- blocked imports weight zero
- recovery actions replace crisis actions after intensity reaches zero
- actual nonhuman countries receive no ordinary civilian actions

## Patch cycle

You are read-only. Return baseline evidence and named findings. After the parent or owner patches source, run `hoi4.probability_compare` against the same scenario IDs and report direction and remaining issues.

Write the report under:

`docs/plans/051_heat_wave_plans/`
