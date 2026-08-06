# IW-030 Montenegro decision repair — 2026-08-06

## Scope

This handoff records the parent-owned repair of the IW-030 Montenegro decision and mission surface after the current country, decision, and probability audits.

## Changed source

- `common/script_constants/006_independence_wave_montenegro_constants.txt`
  - Raised `independence_wave_montenegro_duration.founding_crisis` from 420 to 540 days.
  - Added the MNT one-factory cost profile and a zero factory-floor constant.
- `common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt`
  - Added `is_independence_wave_mnt_project_ready` so every paid project requires the complete setup receipt and cannot reopen after a terminal founding failure.
  - Added `has_independence_wave_mnt_unsettled_host` for an absent or hostile former host.
  - Added MNT-specific administration and sovereignty cost gates that match the one-state opening economy.
- `common/decisions/006_independence_wave_montenegro_decisions.txt`
  - Applied the setup gate to all ten project decisions.
  - Switched MNT administration and sovereignty decisions to the MNT cost profile.
  - Added the missing civilian-factory commitment to the two route-administration projects and durable-sovereignty project.
- `common/scripted_effects/006_independence_wave_montenegro_package_effects.txt`
  - Deduplicated project-failure penalties when an active project and the founding mission cancel in the same incident.
  - Gives the depot settlement a larger crown-legitimacy gain when no bilateral host settlement is possible.
  - Guards generic formable discovery behind an actually registered formable family.
  - Clears the failure latch during setup and cleanup.
- `localisation/english/006_independence_wave_montenegro_l_english.yml`
  - Added MNT-specific factory-cost strings and clarified failure/sovereignty outcomes.
- `docs/events/006_independence_wave/montenegro_package.md`
  - Documents the 540-day window, one-factory cost profile, hostless path, and formable-discovery guard.

## Behavior proof

The critical path remains 75 days for depots, 120 for guards, 120 for offices, and 180 for former-host ledgers: 495 days total. The 540-day mission now leaves a bounded 45-day reaction margin. When the former host is absent or at war, depot reopening uses the decisive crown gain so the non-bilateral path can still reach the 60/60 compact threshold after the other three local projects.

All ten project blocks now contain the setup-ready trigger in both visibility and availability. The failure latch prevents the active-project cancellation and founding-mission cancellation from applying the same penalty twice, and cleanup clears it for a later generation.

## Validation

- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 23 attested packages, 22 compatible reservation groups, and the 6/8/10/14/20 release ladder.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases.
- `python -B .tools/audit_event6_flags.py` passed all 102 registered Event 006 tag flag families.
- Static decision scan confirms all ten MNT projects use the setup-ready gate in visibility and availability.
- MCP probability evidence remains unavailable for the MNT `ai_strategy_factor` surface (`PROBABILITY_SURFACE_EMPTY`); no quantitative AI claim is made.
- Runtime release, dynamic-force materialization, save-load, portraits, and final MNT admission remain outside this repair and remain fail-closed.

## Remaining gates

IW-030 remains outside central content attestation. The three grounded male leader portraits remain rights/provenance/runtime-promotion gated, the vanilla `MNT_1936` OOB reference still needs parent-owned dynamic-force runtime evidence, and typed AI probability evidence is still incomplete.
