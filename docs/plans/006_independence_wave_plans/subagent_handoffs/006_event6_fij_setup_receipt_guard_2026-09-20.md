# Event 006 FIJ setup-receipt lifecycle guard — 2026-09-20

## Status

**IMPLEMENTED / PACKAGE-LOCAL / ADMISSION UNCHANGED**

The Fiji founding mission now cancels when the IW-177 setup receipt is absent, matching its setup-gated activation and the FSM, HBX, and HAW founding-mission contracts.

## Source change

`common/decisions/006_independence_wave_pacific_decisions.txt:450-454` updates `independence_wave_fij_hold_constituent_congress_together` so `cancel_trigger` includes `NOT = { has_country_flag = independence_wave_iw_177_setup_complete }` and the successful `cancel_effect` branch also requires that receipt.

The receipt is the package-local initialization boundary because `independence_wave_setup_iw_177_fiji` clears it before guarded setup, sets it only after `has_prepared_independence_wave_iw_177_package_setup` succeeds, and `independence_wave_cleanup_iw_177_fiji` clears it during teardown.

The repair prevents a stale or partially torn-down FIJ founding mission from remaining active after the setup contract has disappeared and prevents a stale stable variable from being promoted to a successful founding result after teardown.

## Boundary review

This change does not set an identity or asset gate, promote IW-177, widen the attestation OR-list, change the allocator, change Join or SCN-008, expose FORM-39, add a portrait or flag, or alter any weighted value.

IW-177 remains adapter-only and fail-closed under the current 32 content-attested selectable packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows.

## Validation

The package-local parity scan found no other setup-gated Event 006 activation with a nearby founding-mission cancellation trigger missing its matching setup receipt after the FIJ repair.

The shared allocator, SCN-008 scenario matrix, country API, and Event MCP evidence are unchanged from the FSM tranche and remain recorded in `subagent_handoffs/006_event6_fsm_setup_receipt_guard_2026-09-20.md`.

Live Hearts of Iron IV, save/load, and user-owned visual acceptance were not run by the agent.

## Remaining status

Whole Event 006 remains **HOLD / PARTIAL** under `006_event6_completion_gap_audit_2026-09-19.md` because package coverage, source/rights gates, GUI evidence, audio, typed probability fixtures, formable reachability, and live runtime evidence remain unresolved.
