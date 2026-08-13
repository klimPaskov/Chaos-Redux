# Prompt for chaosx_localisation_auditor

Use `fork_context=false`. Audit Event 17 `Random faction` after implementation. Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, and the Event 17 spec package.

Check:

- event name, event detail, history log, evolution log, decision category, decision, mission, idea, achievement, and scripted localisation keys exist
- final text follows project writing style
- no final text exposes hidden weights, variables, or future evolutions
- no raw trigger text appears in UI
- dynamic faction names, country names, values, and durations render cleanly
- spreadsheet-facing mirror fields match in-game wording
- UTF-8 BOM and duplicate key risks are handled according to repo practice

Patch small local text issues if safe. Write a key-level handoff.
