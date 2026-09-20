# Event 006 foundation-mission setup-receipt parity — 2026-09-20

## Status

**IMPLEMENTED / PACKAGE-LOCAL / ADMISSION UNCHANGED**

The setup-receipt lifecycle invariant now holds across all setup-gated Event 006 founding missions reviewed in the current decision registry.

## Source changes

The repair covers `IW-047` MEL, `IW-057` FER, `IW-060` KUR, `IW-013` NAV, `IW-015` GLC, `IW-053` Altai, `IW-052` Buryatia, `IW-054` Khakassia, `IW-051` Yakutia, `IW-048` UDM, and `IW-050` Komi in their existing decision files.

The earlier same-day FSM and FIJ repairs cover `IW-179` FSM and `IW-177` FIJ in `common/decisions/006_independence_wave_pacific_decisions.txt`.

Each affected founding mission now requires its matching `independence_wave_iw_<id>_setup_complete` receipt in the cancellation trigger and in the successful cancellation branch that publishes the package's stable founding result.

MEL and FER also now cancel explicitly when their setup receipt disappears, matching the already guarded packages.

The package setup effects clear each receipt before guarded initialization, set it only after the prepared package setup succeeds, and clear it during package cleanup.

This prevents stale stable ledgers or anchors from being promoted to a successful founding result after setup teardown or generation rollover.

## Boundary review

This tranche does not widen the runtime adapter list, content-attestation OR-list, exact preflight, scenario ranking, deterministic Join, allocator, SCN-008, FORM-39, FORM-48, identity gates, asset gates, map reservations, AI weights, or probability surfaces.

IW-013, IW-015, IW-048, IW-050, IW-051, IW-052, IW-053, IW-054, IW-057, IW-060, IW-177, and IW-179 remain subject to their existing package-local and central fail-closed gates.

## Validation

A balanced-brace package scan confirmed that every setup-gated Event 006 decision mission has its matching setup receipt in both `cancel_trigger` and `cancel_effect`.

`python -B .tools/audit_event6_allocator.py --strict` passed with the unchanged 3/4/5/7/10 ladder, World Collapse 10, 32 attested packages, 40 adapters, and eight adapter-only fail-closed IDs.

The bounded read-only Event MCP lint remains `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and the documented workspace-wide helper/lifecycle deferral; the current artifact is recorded in `006_event6_fsm_setup_receipt_guard_2026-09-20.md`.

The required `chaosx_decision_mission_auditor` route was attempted earlier in this tranche with an explicit read-only scope, but it returned no handoff after bounded waits and was shut down; no specialist audit conclusion is claimed.

Live Hearts of Iron IV, save/load, and user-owned visual acceptance were not run by the agent.

## Remaining status

Whole Event 006 remains **HOLD / PARTIAL** under `006_event6_completion_gap_audit_2026-09-19.md` because package coverage, source/rights gates, GUI evidence, audio, typed probability fixtures, formable reachability, and live runtime evidence remain unresolved.
