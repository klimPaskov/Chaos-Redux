# Event 006 Kosovo lifecycle and cost-gate repair — 2026-09-08

## Disposition

Implemented a bounded IW-031/KOS decision-lifecycle repair. The opening `independence_wave_kos_hold_cantonal_compact_together` mission is now the sole opening action: ordinary KOS projects remain unavailable until its resolved receipt exists, and the active-project helper blocks concurrent starts while the mission is running.

## Source changes

- `common/scripted_triggers/006_independence_wave_kosovo_package_triggers.txt`
  - `is_independence_wave_kos_project_ready` now requires `independence_wave_kos_compact_crisis_resolved` and still rejects the failure receipt.
  - `has_independence_wave_kos_active_package_project` now includes the opening compact mission.
  - KOS light/standard administration and strategic affordability checks now accept stockpiles exactly equal to the displayed debit, matching the shared Event 006 cost-gate contract. The one-factory project floor remains strict because it represents factory availability, not a custom stockpile debit.

No admission, country identity, state, host, force, AI weight, asset, localization, or fallback behavior changed.

## Validation

- `.tools/audit_event6_allocator.py --strict` passed: exact 3/4/5/7/10 ladder, World Collapse 10, no pre-event category/mission/cost/queue.
- `.tools/audit_event6_scenario_matrix.py` passed: all 32 SCN-008 cells and eight edge cases.
- `.tools/audit_event6_country_api.py` passed: 191 unique carriers, no missing or duplicate tags, IW-031 crosswalk pass.
- `.tools/audit_event6_flags.py --strict` passed: 102 complete flag families.
- `.tools/audit_event6_form16.py` passed: ARM/GEO/AZR exact member, consent/refusal, mutation, and rollback contracts.

## Remaining boundary

This is source/static evidence only. Live mission completion, save/load persistence, and engine runtime behavior remain user-owned validation. Other unadmitted packages remain fail-closed; no generic substitute or admission bypass was introduced.
