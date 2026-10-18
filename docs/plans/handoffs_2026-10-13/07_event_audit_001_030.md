# Handoff 7: event regression audit, events 001 to 030

Read `00_common_rules.md` in this folder first. This handoff can run at the same time as all the others.

## Why

The first rounds restored text, icons, interface layouts and the named systems. Nobody has yet checked the events themselves one by one. The owner: "Current state of chaos redux is honestly very sad, we haven't progressed (I'd say we even regressed) in more than a year. Because of much slop and bloat and overwriting of good things there have been."

## Scope

Events 001 to 030, including Event 011 and its incident pool.

## For each event in scope

1. Read its files (events, decisions, ideas, focuses, scripted effects and triggers, scripted GUI, localisation, on_actions) and its history over the last 14 months (`git log --follow` per file).
2. Find regressions: mechanics, options, branches, evolutions, decisions, missions, countries, leaders, units or rewards that existed and were later removed, merged away, stubbed, simplified or made generic; flows that gained extra steps, delays or windows; tooltips that began exposing internal flags or variables; options above the limit of 4; strong bonuses handed out casually; ideas granted twice; idea, decision or category icons of the wrong size or missing; text that reads vague where the older text was concrete.
3. Restore each regression from history exactly. Keep genuinely new content. Where an event was deliberately reworked under an accepted spec in `docs/specs/`, the spec wins; restore only what the rework lost by accident.
4. Check the event still fires, logs to the event history with its name only, shows its details and evolutions in the event log, and cleans up after itself.
5. One line per event in `docs/plans/event_regression_audit_2026-10-13.md` (append; other workers write there too): event, regressions found with commits, restored or kept and why, your commits.