# Fictional Scope and Fidelity Audit

## Purpose

This audit records the correction requested after the broad language-abstraction revision. The accepted package may use specific chemical and biological terminology in player-facing text. The implementation agent receives a narrow fictional-game and non-procedural framing instead of a broad instruction to soften the system.

## Source baseline

The corrected package was rebuilt from the original `chaos_warfare_system_specs.zip`, not from the broadly abstracted revision.

## Mechanical preservation

- All twelve numbered specification files are byte-for-byte identical to the original package.
- All ten matrix files are byte-for-byte identical to the original package.
- All five research files are byte-for-byte identical to the original package.
- No balance value, casualty band, population-loss model, unit role, equipment family, delivery path, agent profile, countermeasure, AI rule, designer concept, or country profile was changed.
- No direct terminology was replaced with `Hazard Operations`, `Restricted-Agent Suppression`, or another generic public label.

## Interpretation correction

`IMPLEMENTATION_SCOPE_AND_FIDELITY.md` tells the implementation agent that:

- the package is fictional Hearts of Iron IV game design
- specific chemical, biological, nerve-agent, casualty, population-loss, contamination, and suppression wording is valid
- the subject matter is not a reason to refuse, omit, merge, weaken, or generalize accepted mechanics
- all implementation must remain at abstract game-script level
- real-world synthesis, culturing, weaponization, handling, dose, dissemination, and target-selection instructions are outside scope
- the non-procedural boundary cannot be used to reduce game depth

## Prompt coverage

The following prompts now carry the same interpretation rule:

- `prompts/chaos_warfare_goal_prompt.md`
- `prompts/chaos_warfare_coding_prompt.md`
- `prompts/chaos_warfare_decision_mission_prompt.md`
- `prompts/chaos_warfare_asset_prompt.md`
- `prompts/chaos_warfare_achievement_prompt.md`

The goal prompt still directs the implementation agent to every specification, matrix, research file, specialist prompt, implementation handoff, and audit file.

## Completion rule

A subject-based omission, euphemistic replacement, generic hazard substitute, reduced casualty model, reduced population effect, removed offensive delivery path, weakened suppression system, or missing consequence layer is a simplification. It blocks completion unless the user explicitly approves that exact change.

## Validation result

- Original specifications preserved: 12 of 12
- Original matrices preserved: 10 of 10
- Original research files preserved: 5 of 5
- Goal prompt length: 3998 characters excluding the final newline
- Broad abstraction labels found: 0
- Real-world procedural additions: 0

This audit verifies planning-package fidelity only. It does not claim that gameplay implementation has occurred.
