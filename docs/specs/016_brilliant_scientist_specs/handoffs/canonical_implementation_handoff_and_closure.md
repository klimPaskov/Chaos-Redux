# Canonical implementation handoff and closure

This package promotes the first-pass design and the second-pass improvement work into one canonical source-design package for Event 16, Brilliant Scientist.

## Source status

The source design is complete enough to move into repository implementation. Do not write another broad expansion pass before implementation unless the project owner rejects the closure or a live implementation audit finds a structural gap that is not already covered by the package.

## What remains before implementation can be called complete

- Inspect the live Chaos Redux repository, required offline Paradox wiki pages, vanilla HOI4 documentation, vanilla examples, and existing Chaos Redux patterns.
- Choose conflict-free final tag and file identifiers for the Kruger country package.
- Implement gameplay files, localisation, scripted localisation, event log integration, evolutions, decisions, focus trees, country setup, ideas, AI, assets, super-events, achievements, docs, and spreadsheet alignment.
- Run source-specific subagents when available with `fork_context=false` and explicit prompts.
- Run the completion auditor before any final completion claim.

## Closure rule

The improvement loop is closed at the design level. Final work should focus on implementation, audit, validation, asset production, super-event research, and documentation alignment. Additional systems should be rejected as bloat unless they solve a confirmed implementation gap.

## Blocker honesty

This package is not a repository patch. It does not include generated DDS files, final audio, final super-event quotations, live validation, or completed localisation. Those remain implementation and research tasks.
