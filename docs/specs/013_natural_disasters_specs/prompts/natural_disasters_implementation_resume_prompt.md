# Event 013 Natural Disasters resume brief

This is the single resume brief for Event 013.
It replaces the former coding, goal, subagent-routing and implementation-resume prompts, the closure resume packet, the final next-agent prompt, the dependency-order plan and the simplification blocklist (git history keeps them).

## Status

Event 013 is implemented in source.
Resume from `docs/events/013_natural_disasters/overview.md`, the live Event 013 files listed there, and `docs/plans/013_natural_disasters_plans/` (start with `agent_decisions_2026-10-05.md`).
Do not restart from this planning package, rebuild the engine, or recreate completed asset, super-event, achievement or audit tranches.
Pick work only from a concrete defect, an accepted plan item, or an open question in the package README that the owner has accepted.

## Binding design rules

These rules come from the accepted source design and the accepted negative boundaries in `docs_alignment/013_source_of_truth_and_disposition_map.md`.

- Event 013 is a fresh, Minor Repeatable, non-terminal engine; old Natural Disasters and Earth Earthquake logic stay deleted.
- Event 046 stays an inactive placeholder, Event 099 stays a narrow bridge through `call_natural_disaster`, and Event 051 Heat Wave stays separate with no heat stacking.
- One accepted call owns one sequence and at most one Event 013 history row; warnings, impacts, follow-ups and reports never add rows, and evolution rows mark only the three evolutions.
- External callers use only `call_natural_disaster` and never copy damage, Deaths, report, aftermath or follow-up logic; hostile or divine callers prove their own cost, cooldown and target legitimacy.
- Physical family geography is a hard gate; exposure only ranks candidates that already passed it.
- Each recipient gets at most one aggregate report per sequence and each sequence at most one world-news event (accepted 2026-10-05); later recovery outcomes update cards, map and history without a second popup.
- Recovery and relief fees follow the accepted 2026-10-06 bill in Part 2; no Political Power store, no duplicate Stability fees, at most three inline amounts and four spent types.
- Deaths reduce real state population through the shared Deaths system; baseline losses matter, Evolution II scales with vulnerability, Evolution III can devastate regions.
- Normal disasters use the aftermath category; only Evolution III and Maximum Disaster Barrage use the abnormal path map, with frame-sheet animation and static fallbacks.
- Player text is final localisation written from in-game facts; planning labels, formulas and implementation history never appear in it.
- No new countries, focus trees, family-level super-events, normal-disaster GUIs or world-end branch.

## Working rules for a continuation

- Follow CLAUDE.md, `chaos-redux-events`, `chaos-redux-decisions-missions` and the skill for the touched surface; route specialists through `.claude/skills/chaos-redux-subagents/SKILL.md`.
- Change tuning in `common/script_constants/013_natural_disasters_constants.txt`, not in prose or script literals.
- A change to a shared hook (Deaths, Famine, Migration, Air Cleanliness, Events 012, 014, 018, 020, 026) needs both owners named and the same idempotency key on both sides (the sequence id and impact index).
- Record each change and its validation limits in `docs/plans/013_natural_disasters_plans/` and keep the overview current.
- A change to an Event Details, evolution, cluster or scenario field edits `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and then runs `python .tools/export_event_catalog_csv.py`.
- Report every simplification, unverified engine behaviour and unavailable check plainly; do not request user game tests as a completion step.
