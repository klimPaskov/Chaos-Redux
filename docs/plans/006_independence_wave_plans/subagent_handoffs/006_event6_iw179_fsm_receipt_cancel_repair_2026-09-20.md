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

The focused read-only `hoi4.event_inspect` lint for the committed source returned `EVENT_INSPECTED_PARTIAL` at revision `5d73a0f565b8e820a715982b124b7e4de595a0c6619f59cebf2dca66ed924d1e`, graph hash `3b646fa519df44eaaa1b3525b1988109369902b9eaaec315dc54f2cd3887b585`, zero blocking diagnostics, and zero skipped sources. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c2d6fea2a8e7897e86d7a6b9184b178255cad013066000bf9c50c3e53813e15/1bb02a7dce478c81f4ab24f4b4551afca30f452ddea1b609212952bcf0f0d5ba/event-lint-5d73a0f565b8.json`.

The matching read-only options render returned `EVENT_RENDERED_PARTIAL` at the same revision with layout hash `dc7c6b2fdb9a3143f5ed65837542c0750cbf4453a8736f2c704ed2e8aa231e38`, 24 selected nodes, and 42,772 omitted nodes. Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7208101839ca2721d931108eefbc63618372e552b80d22bd134f87ba6919be06/344b5bee371cd2bd36ac0682f101663d445833a51e9d3390e8e7a8d754c8f335/event-options-5d73a0f565b8-manifest.json`.

These Event MCP results are structural/partial evidence only. The focused event/on-action projection does not provide direct semantic coverage for the changed common decision and scripted-trigger cancellation blocks, so no decision-source semantic comparison or live/save-load claim follows.

## Scope limits

This repair closes only the IW-179 setup-receipt cancellation gap. It does not admit FSM, publish the withdrawn identity or portrait, change FORM-48 reachability, alter central allocator behavior, or establish live/save-load evidence.
