# Event 006 terminal receipt lifecycle repair

Date: 2026-08-24.

Status: source implementation complete; live transaction evidence remains user-owned and unclaimed.

## Scope

This bounded repair closes two lifecycle defects in the standalone `chaosx.nr6.1` transaction without changing package admission, allocation weights, wave counts, costs, pre-event visibility, or release effects.

- `common/scripted_effects/006_independence_wave_execution_effects.txt`
- `common/scripted_effects/chaosx_liberation_release_effects.txt`

## Repairs

1. Before a pre-mutation cancellation or a verified compensating rollback clears the Event 006 contribution, the selected, attempt, sponsorship, chaos-band, and optional-expansion-failure values are copied into a short-lived global staging area. The terminal snapshot consumes those staged values after coordinator cleanup, then clears the staging area.
2. A new standalone transaction clears `global.independence_wave_execution_last_failure` before stale-plan recovery and plan creation, preventing an earlier execution failure from overriding a current allocator or planning failure.
3. Stale-plan recovery staging is cleared again after recovery, so a successful rollback from an abandoned prior transaction cannot contaminate the receipt for the new attempt.

The committed-only `chaosx.nr6.2` presentation gate, shared rollback owner, Event 005/006 joint path, and all admission boundaries remain unchanged.

## Evidence

Static source checks passed:

- Both touched Clausewitz files have balanced braces: `531/531` and `1020/1020`.
- The six maintained Event 006 validators passed: allocator, country API, strict flag families, SCN-008 matrix, FORM-16, and Statehood Ledger.
- `git diff --check` reported no whitespace errors for the owned edits.

The required Event MCP lint was run on `chaosx.nr6.1` with the current workspace. It returned `EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, and deferred workspace-wide helper/lifecycle projections. Artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/746b489da09c82e710c337f7b4a4d133005823d36f60cf2b75df9cdd2c657bb5/7b1caf64ee45d3b46c734fd2c02dc45e930cb3a2004d32c5cce807f3411bac98/event-lint-730923263b0a.json`

This is a source and diagnostic repair only. It does not claim that a live standalone release, save/load receipt, or successful country creation has been observed.
