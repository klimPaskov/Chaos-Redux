# Event 006 KUB/RUT/TAT lifecycle gate repair — 2026-09-08

## Disposition

Implemented a bounded decision-lifecycle repair for the admitted IW-040 Kuban, IW-038 Ruthenia, and IW-044 Tatarstan packages. Their opening compact missions are now the sole opening action: ordinary package projects remain hidden and unavailable until the matching compact-resolution receipt exists, and the active-project helpers reserve the opening mission while it is running.

## Source changes

- `common/scripted_triggers/006_independence_wave_kuban_package_triggers.txt`
  - `is_independence_wave_kub_project_ready` now requires `independence_wave_kub_compact_crisis_resolved` and continues to reject the failure receipt.
  - `has_independence_wave_kub_active_package_project` now includes `independence_wave_kub_hold_mounted_compact_together`.
- `common/scripted_triggers/006_independence_wave_ruthenia_package_triggers.txt`
  - `is_independence_wave_rut_project_ready` now requires `independence_wave_rut_compact_crisis_resolved` and continues to reject the failure receipt.
  - `has_independence_wave_rut_active_package_project` now includes `independence_wave_rut_hold_mountain_compact_together`.
- `common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt`
  - `is_independence_wave_tat_project_ready` now requires `independence_wave_tat_compact_crisis_resolved` and continues to reject the failure receipt.
  - `has_independence_wave_tat_active_package_project` now includes `independence_wave_tat_hold_river_compact_together`.

No admission, country identity, state, host, force, AI weight, asset, localisation, cost, or fallback behavior changed. Existing package-specific affordability gates already used the inclusive stockpile pattern and were left untouched.

## Evidence and validation

- The opening mission definitions are activation-backed, `available = { always = no }`, and set the matching compact-resolution flag only on their stable, route, anchor, and capital-control success path. Timeout or invalidation sets the failure receipt and applies the existing package failure helper.
- The three packages are in the current central content-attestation and deterministic Join set; adapter-only and unadmitted packages were not widened.
- `.tools/audit_event6_allocator.py --strict` passed: exact 3/4/5/7/10 ladder, World Collapse 10, no pre-event category/mission/cost/queue.
- `.tools/audit_event6_scenario_matrix.py` passed: all 32 SCN-008 cells and eight edge cases.
- `.tools/audit_event6_country_api.py` passed: 191 unique carriers, no missing or duplicate tags, IW-031 crosswalk pass.
- `.tools/audit_event6_flags.py --strict` passed: 102 complete flag families.
- `.tools/audit_event6_form16.py` passed: ARM/GEO/AZR exact member, consent/refusal, mutation, and rollback contracts.

## Remaining boundary

This is source/static evidence only. Live mission completion, save/load persistence, and engine runtime behavior remain user-owned validation. Other packages with different project/mission contracts were not generalized from this repair; no generic substitute or admission bypass was introduced.
