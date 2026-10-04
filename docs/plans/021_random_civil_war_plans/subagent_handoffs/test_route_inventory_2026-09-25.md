# Event 021 acceptance and test-route inventory

Date: 2026-09-25

Disposition: implemented as a test map; all live acceptance results remain pending. This is repository evidence, not a gameplay pass.

## Discovery

The September exploration found no Event 021-specific offline acceptance runner or test script in non-vendored `.tools`.
The connected October 3 tool catalog exposes `hoi4.scenario_test`, `hoi4.mechanic_test`, and `hoi4.package_check`; the earlier absent-route statement is superseded.
Exposure alone does not establish service health, supported fixture coverage, or a passing test.
The focused Maximum-cap mechanic test timed out after 600 seconds without an artifact or interpreter verdict.
The FRT, GLB, SET, and SCN handoffs remain source reviews rather than executed acceptance fixtures.
The shared `transfer_and_event_suite.json` covers civilian transfers and Event 001; it does not provide Event 021 acceptance.
The documented `e chaosx_test` carrier registers readiness and does not select a target, create a front, fire Event 021, or spend resources.

The scenario identity is SCN-018/raw ID 18; the older SCN-014 reference in a weighted-logic document is stale and must not be used as the scenario test identity. Maximum setup exposes requested, preflight, plan-eligible, committed, and skipped counters. No live Maximum timing or one-frame failure measurement exists, so immediate setup remains the implemented path and the seven-day fallback is not justified by current evidence.

## Required live evidence

Outstanding runtime evidence includes FRT-01 through FRT-05, GLB-01 through GLB-07, SET-01 through SET-06, the full recurrence matrix, one-state and all-island same-tag contests, actual-nonhuman immunity, Event 006 package initialization and cleanup, terminal/interruption/save-reload cleanup, mission cancellation and reactivation, category and Event Details presentation, and all six replacement-asset consumers.

The SCN-018 Maximum run must capture the requested, preflight, plan-eligible, committed, and skipped counts and elapsed setup time against the same campaign snapshot. Immediate setup stays the required design unless a measured one-frame failure authorizes the bounded deterministic fallback.

The current event MCP overview is partial and the probability MCP reports do not provide complete distributions, typed fixtures, or a valid same-scenario comparison. They cannot certify these transitions or performance. The agent did not launch the game.

## Status

Keep Event 021 and SCN-018 at `Needs Testing`; this inventory records the test-route gap and evidence boundary, not a pass or a final completion decision.
