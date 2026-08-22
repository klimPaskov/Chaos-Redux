# Event 006 post-transfer capital assignment — 2026-08-22

## Disposition

Implemented a narrow execution-order repair for dormant Event 006 carriers.

The shared execution pass now reapplies each selected package's exact frozen anchor as the released country's capital after ownership and controller transfer, before final package validation.

This closes the AXX/BAX/BBX failure path where a dormant carrier could reach state transfer without a valid live capital even though its package trigger requires the anchor to be capital-owned and controlled.

## Source change

- `common/scripted_effects/006_independence_wave_execution_effects.txt` adds `independence_wave_assign_frozen_country_capitals` and calls it immediately after `independence_wave_transfer_frozen_states`.
- The helper reloads the frozen country and anchor targets from the immutable plan arrays and only calls `set_capital` when the target owns and controls that anchor.
- Existing package gates, reservation controls, rollback guards, and the retired pre-event crisis surface are unchanged.

## Evidence

- `python -B .tools/audit_event6_allocator.py` passes, including the fixed-anchor/no-`capital_scope` regression guard for IW-024, IW-027, and IW-028.
- Country API, strict flag, SCN-008 scenario, FORM-16, and Statehood Ledger semantic source audits pass.
- A fresh `hoi4.event_inspect` lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics; workspace-wide helper and lifecycle analysis remains deferred by the MCP report.

No live game or save/load completion claim is made.
