# Event 021 Test-Release Gate Handoff

Status: implemented for test release. This handoff records the explicit decision to make the completed rework playable while retaining the catalog status `Needs Testing` and the final acceptance claim closed.

## Source changes

- `common/scripted_triggers/chaosx_settings_triggers.txt` now admits `constant:random_civil_war_event.id` to `event_log_event_is_reworked_default_enabled`.
- `common/scripted_effects/021_random_civil_war_parent_effects.txt` now seeds `random_civil_war_rework_ready` inside the existing one-time `random_civil_war_release_gate_initialized` guard.
- `docs/specs/021_random_civil_war_specs/README.md`, `docs/events/021_random_civil_war/overview.md`, and `docs/events/021_random_civil_war/acceptance_evidence.md` describe the open test-release gate and preserve the separate acceptance boundary.

## Resulting behavior

New runtime initialization can select Event 021 through the normal bounded scheduler and can expose SCN-018 The Fracture Cascade. Event 021 remains `Needs Testing` in the workbook and generated catalog exports. The release flag does not certify the full implementation, engine behavior, probability matrix, performance, save/load behavior, cleanup, or user-owned live consumer scenarios.

The one-time guard preserves the release decision after initialization. It does not add a recurring world-wide loop and does not alter Event 006 lifecycle, weight, cap, evolution, league, or origin state.

## Evidence boundary

The source change was reviewed against the current Event 021 parent triggers and scenario gates. The existing current-revision MCP event lint remains partial because helper and lifecycle projection is deferred. The independent probability certificate, full Event 006 engine-backed matrix, performance measurements, and live gameplay validation remain open and are not implied by this test-release handoff.
