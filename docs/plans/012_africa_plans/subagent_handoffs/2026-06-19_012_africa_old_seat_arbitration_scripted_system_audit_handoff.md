# Event 012 Old-Seat Arbitration Scripted-System Audit Handoff

Date: 2026-06-19
Subagent: `chaosx_scripted_system_architect`

## Findings And Patch

- Blocking issue fixed: the failure popup for Old-Seat Arbitration no longer uses the success result summary.
- `chaosx.nr12.52.d` now calls `GetAfricaOldSeatArbitrationFailureSummary`.
- `GetAfricaOldSeatArbitrationFailureSummary` selects six pair-specific failure localisation keys plus a none fallback.
- Failure keys describe the actual value damage from failed hearings instead of the success gains.

## Evidence

- Six pair constants, start gates, completion gates, and start assignments are aligned for Great Lakes, Central River, Western Crowns, Red Sea, Monsoon Rova, and Sahel Caravan.
- The pair and old-seat state are country-scoped variables.
- The stored seat is scoped with `var:africa_old_seat_arbitration_seat_state`, matching the supported variable-as-scope pattern.
- Cleanup flows through `africa_clear_old_seat_arbitration_context`.

## Validation

- Confirmed the failure event calls the failure summary and all six failure keys exist.
- Confirmed no unsupported `<=` or `>=` syntax in the audited Event 012 files.
- Confirmed the English localisation BOM remained intact after the subagent patch.
