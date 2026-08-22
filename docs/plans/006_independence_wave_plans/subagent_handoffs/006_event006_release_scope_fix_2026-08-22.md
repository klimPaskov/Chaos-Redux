# Event 006 release-scope correction — 2026-08-22

## Scope

Repair the direct `chaosx.nr6.1` standalone release path when the event is fired by a former host country. The release transaction enters the selected dormant country scope after ownership transfer; checks in that scope must compare the anchor and former host against the current target country, not the event caller.

## Changes

- `common/scripted_triggers/006_independence_wave_triggers.txt`
  - `has_valid_independence_wave_setup_input` now uses `PREV` inside the saved former-host and anchor state scopes.
- `common/scripted_triggers/006_independence_wave_*_package_triggers.txt`
  - Every currently admitted package (IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-033, IW-038, IW-040, IW-041, IW-044, IW-045, IW-070, IW-071, IW-072, IW-173, and IW-184) now compares its nested anchor and former-host proofs against the target country with `PREV`. Adapter-only packages remain fail-closed and are intentionally not admitted by this patch.
- `common/scripted_triggers/006_independence_wave_force_triggers.txt`
  - Dynamic opening-force preflight now validates the setup anchor and former host against the target country with `PREV`.
- `common/scripted_effects/006_independence_wave_force_effects.txt`
  - Opening divisions are explicitly owned by the initialized Event 006 country through a saved event target, and generation receipts read from that target instead of the event caller.

## Evidence

- Offline scope guidance confirms `ROOT` remains the root country of the event block while `PREV` is the containing country inside a nested state or event-target scope.
- `python -B .tools/audit_event6_allocator.py` passes after the change.
- A static scope audit finds zero `ROOT` references inside the admitted package setup, prepared, or runtime-proof functions, and the three previously failing dormant package trigger files contain no `capital_scope` use.
- The earlier `hoi4.event_inspect` lint for `chaosx.nr6.1` refreshed with zero blocking diagnostics (`EVENT_INSPECTED_PARTIAL`; workspace-wide helper projection remained deferred). A post-change refresh then timed out and the MCP transport closed, so no newer MCP revision is claimed here.

## Remaining risk

Adapter-only packages retain package-local `ROOT` references in dormant, non-executable predicates and remain fail-closed. The current admitted execution set is covered by this correction; live game validation remains outside the agent scope.
