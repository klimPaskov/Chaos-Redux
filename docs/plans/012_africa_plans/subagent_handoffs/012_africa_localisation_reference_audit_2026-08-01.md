# Event 012 Africa localisation reference audit

Date: 2026-08-01.

## Scope

This read-only audit scans Event 012 event, decision, focus, scripted-localisation, scripted-effect, scripted-trigger, idea, character, and AI-plan sources for literal `africa_` localisation references and compares them with the English localisation catalog.

## Result

The scan found 2,083 Event 012 literal references and zero missing `africa_` localisation keys.

The seventeen package nature invocation keys, including the unrecorded fallback, each occur exactly once in the English catalog and are all referenced by `GetAfricaPriorityMemberNatureInvocationName`.

The localisation file remains UTF-8 with BOM, and the current nature arsenal, launch tooltip, and targeted decision descriptions all use the existing dynamic invocation helper.

## Boundary

This audit does not claim live rendering, save-game acceptance, world-order readiness, achievement completion, or completeness of the controlled asset pool.
