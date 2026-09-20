# IW-179 FSM setup-receipt cancellation repair

Date: 2026-09-20.

Status: implemented as a bounded lifecycle repair; Event 006 remains HOLD / PARTIAL.

## Finding

The eight ordinary FSM timed decisions were created from the IW-179 setup-receipt category, but their active timers did not all cancel if `independence_wave_iw_179_setup_complete` disappeared after activation. The founding mission already had this guard, and package cleanup removes the full decision set, but a receipt-only lifecycle path could otherwise leave a paid timer able to reach its remove effect.

## Change

The three core FSM projects and the autonomous federation mandate now include `NOT = { has_country_flag = independence_wave_iw_179_setup_complete }` in their direct `cancel_trigger` blocks.

The four mutually exclusive government-route decisions share `should_cancel_independence_wave_fsm_government_settlement`, which now cancels on the same setup-receipt loss in addition to package loss, capital loss, and route completion.

The existing cancellation effects, failure transaction, payment, durations, route lock, AI, and cleanup remain unchanged. No new flag, variable, cost, category, route, admission, or formable behavior was added.

## Validation

The focused source assertion resolves all eight ordinary FSM decision IDs and confirms a direct receipt guard on the three core plus autonomous projects and the shared receipt-aware cancellation helper for the four route decisions.

`python -B .tools/audit_event6_allocator.py --strict` passes with the unchanged 32/29/40/161 authority boundary and 3/4/5/7/10 ladder. `python -B .tools/audit_event6_scenario_matrix.py` passes all 32 SCN-008 cells and eight edge cases.

The focused Event MCP lint/render should be refreshed against the committed source. Its event/on-action projection does not provide direct semantic coverage for common decision cancellation blocks; any returned partial artifact must be reported with that boundary.

## Scope limits

This repair closes only the IW-179 setup-receipt cancellation gap. It does not admit FSM, publish the withdrawn identity or portrait, change FORM-48 reachability, alter central allocator behavior, or establish live/save-load evidence.
