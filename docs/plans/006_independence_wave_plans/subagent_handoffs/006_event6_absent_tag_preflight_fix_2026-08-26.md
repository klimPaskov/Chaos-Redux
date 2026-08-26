# Event 006 absent-tag preflight repair — 2026-08-26

## Disposition

Source repair applied; whole Event 006 remains HOLD/PARTIAL. The fix addresses the standalone manual-trigger path when a registered release tag is not instantiated at game start. It does not promote any package, change the reservation ladder, or restore a pre-event UI surface.

## Root cause

The planner intentionally supports releasing a dormant fixed tag before that country has been instantiated. The exact package identity predicates and the central runtime preflight nevertheless required `original_tag = TAG` unconditionally. For a genuinely absent tag, that identity test is false even though `is_independence_wave_dormant_country_scope = yes` is explicitly designed to accept `exists = no`; the candidate was rejected before host/country/anchor reservation, leaving the standalone allocator with no executable candidate and therefore no released countries.

## Files and identifiers changed

- `common/scripted_triggers/006_independence_wave_package_triggers.txt`: exact checks for IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-030, IW-031, IW-038, IW-093, IW-098, IW-173, IW-177, and IW-184.
- `common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt`: IW-023, IW-024, IW-026, IW-027, IW-028, and IW-029.
- `common/scripted_triggers/006_independence_wave_karelia_crimea_package_triggers.txt`: IW-033 and IW-041.
- `common/scripted_triggers/006_independence_wave_kuban_package_triggers.txt`: IW-040.
- `common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt`: IW-044.
- `common/scripted_triggers/006_independence_wave_bashkiria_mari_package_triggers.txt`: IW-045.
- `common/scripted_triggers/006_independence_wave_transcaucasus_package_triggers.txt`: IW-070, IW-071, and IW-072.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`: corresponding direct identity branches in `is_independence_wave_runtime_package_preflight_ready`.

Each affected identity test now uses `OR = { original_tag = TAG exists = no }`. The generic legacy content-flag gate and the central content-attestation OR-list were not widened. Adapter-only rows remain fail-closed.

## Safety boundary

An absent tag can pass only the identity half of the pre-release check. The planner still requires a dormant target, exact package-content attestation, an installed runtime adapter, a living former host with an available anchor, origin and Soviet-collision exclusion, reservation-group capacity, force-mapping readiness, and synchronized plan metadata. The execution barrier rechecks the same package ID, country target, anchor, host, reservation, force, and transaction receipts before calling `release` and transferring the frozen states. Existing living or occupied carrier tags continue to fail through the dormant and host/anchor gates.

The normal vanilla pattern supports querying fixed country scopes before release with `exists = no`; the repository's release effect already calls `release = event_target:independence_wave_execution_country` specifically for an absent target. The source fix aligns the identity predicate with that existing executor contract.

## UI contract

No decision category, pressure meter, mission, event text, or other visible crisis indication is created by this repair. The pre-event Independence Wave crisis surface remains retired. Player-facing `.2` presentation is still gated on `independence_wave_standalone_incident_committed` after a non-empty successful transaction.

## Evidence

- `python -B .tools/audit_event6_allocator.py`: publishers 149; automatic/high-chaos selectable 126; SCN-008 selectable 138; runtime adapters 40; eight adapter-only rows; 32 content attestations; 29 compatible groups; static standalone witness 20; ladder 3/4/5/7/10 with World Collapse 10; pre-event crisis retired.
- `python -B .tools/audit_event6_country_api.py`: broad 242, resolved 191, Soviet 34, Africa 45, missing 0, duplicate 0, IW-031 crosswalk pass.
- `python -B .tools/audit_event6_flags.py --strict`: 102 registered and complete.
- `python -B .tools/audit_event6_form16.py`: pass.
- `python -B .tools/audit_event6_scenario_matrix.py`: 32 cells and 8 edge cases.
- Narrow HOI4 MCP event lint on `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`: status `EVENT_INSPECTED_PARTIAL`, no Event 006-specific blocking diagnostic; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/47120b02ad15849ca9910f188400624c27be75034bbce4a0894f271b63bc6e6f/0162a09c13671797591eaf5183000d4952e2c8cb07d00ae88aa6ccb707b7cbeb/event-lint-2b3b330f6626.json`. The MCP result remains partial because the workspace scan truncates inline files and reports unrelated global helper diagnostics.

## Remaining risk and owner action

No live game, save/load, or renderer proof is claimed. The user must manually trigger `chaosx.nr6.1` in a fresh validation session and confirm that the admitted countries are instantiated and the post-commit event appears. If a country still does not appear, the next diagnostic should inspect the staged allocator receipt and the three candidate event targets (`liberation_candidate_country`, `liberation_candidate_anchor`, and `liberation_candidate_primary_host`) before adding temporary logging; no speculative debug code was left in source.
