# Event 013 nested runtime state correction

Date: 2026-07-12

## Defect

The Event 013 controller used temporary variables as helper outputs without always initializing them in the scripted effect or decision that consumed them. HOI4 does not reliably carry a temporary variable first created inside a nested scripted effect back to its caller. The affected paths could therefore resolve a valid family and state internally, then appear to return zero or no result when the caller scheduled the sequence. The same pattern affected delayed snapshots, warning costs, cluster availability, and several presentation selectors.

## Correction

Caller-owned initialization now covers:

- random-event preflight, evolution flags, family/origin/target planning, exact API outputs, and accepted sequence counts;
- all 26 delayed-job snapshot fields, reserved due dates, reports, news, chains, control transfer, and external-call results;
- family, severity, resilience, population, building, disruption, warning-cost, recovery, and neighbor profiles;
- aftermath priority, severe-slot reservation, four foreign-relief routes, category display, abnormal history, and GUI urgency;
- cluster definition/type/tier/chance, member availability, random ranges, actor selection, firing counts, runtime readiness, cooldown, settings, history, detail UI, and pacing callers.

The Event 013 manual root remains hidden by design, but an accepted call immediately exposes the exact forecast card and category for the affected country. Warning, impact, report, follow-up, and reassessment jobs remain delayed by at least one worker day.

## Audit evidence

An independent read-only audit re-read the final Event 013 core, public dynamic wrapper, triggerable scenario, decision callers, and cluster controller. It found no remaining concrete caller-to-callee temporary-output defect. Remaining static matches were branch-separated code, inputs, arrays, event targets, or regular/global variables rather than temporary scalar returns.

The full live-engine scenario matrix remains queued because the repository has no deterministic headless HOI4 harness. Event 013 and SCN-007 therefore retain `Needs Testing` workbook status.
