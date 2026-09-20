# Event 006 FSM setup-receipt lifecycle guard — 2026-09-20

## Status

**IMPLEMENTED / PACKAGE-LOCAL / ADMISSION UNCHANGED**

The Micronesia founding mission now cancels when the IW-179 setup receipt is absent, matching its setup-gated activation and the corresponding HBX and HAW founding-mission contracts.

## Source change

`common/decisions/006_independence_wave_pacific_decisions.txt:292-296` updates `independence_wave_fsm_keep_island_federation_connected` so `cancel_trigger` includes `NOT = { has_country_flag = independence_wave_iw_179_setup_complete }` and the successful `cancel_effect` branch also requires that receipt.

The receipt is the package-local initialization boundary because `independence_wave_setup_iw_179_micronesia` clears it before guarded setup, sets it only after `has_prepared_independence_wave_iw_179_package_setup` succeeds, and `independence_wave_cleanup_iw_179_micronesia` clears it during teardown.

The repair prevents a stale or partially torn-down FSM founding mission from remaining active after the setup contract has disappeared and prevents a stale stable variable from being promoted to a successful founding result after teardown.

## Boundary review

This change does not set `independence_wave_fsm_sourced_identity_ready`, promote IW-179, widen the attestation OR-list, change the allocator, change Join or SCN-008, expose FORM-48, add a portrait or flag, or alter any weighted value.

IW-179 remains adapter-only and fail-closed under the current 32 content-attested selectable packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows.

## Validation

`python -B .tools/audit_event6_allocator.py --strict` passed with the unchanged 3/4/5/7/10 ladder, World Collapse 10, 32 attested packages, 40 adapters, and eight adapter-only fail-closed IDs.

`python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases with the existing publication order.

`python -B .tools/audit_event6_country_api.py` passed with 242 broad rows, 191 resolved unique carriers, zero missing tags, zero duplicates, and the IW-031 crosswalk pass.

The read-only `hoi4.event_inspect` lint on `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` at revision `a8fde3e58546f004e81d855d73d29674ae3c5be8f894a1caf9586621929a6657`, with zero blocking diagnostics and the documented large-workspace helper/lifecycle deferral; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ae1bd0cf2cc89b3ac8c7f84647f72b9de3344e535fa1978560bd5419a8f26a51/38bfa6a221e3ea5abaae0aee8eebd094f4daf110c5efa528d52d841b19151ca6/event-lint-a8fde3e58546.json`.

The required `chaosx_decision_mission_auditor` route was attempted with an explicit read-only FSM scope, but it returned no handoff after two bounded waits and an interrupt request and was shut down; no auditor conclusion is claimed.

Live Hearts of Iron IV, save/load, and user-owned visual acceptance were not run by the agent.

## Remaining status

Whole Event 006 remains **HOLD / PARTIAL** under `006_event6_completion_gap_audit_2026-09-19.md` because package coverage, source/rights gates, GUI evidence, audio, typed probability fixtures, formable reachability, and live runtime evidence remain unresolved.
