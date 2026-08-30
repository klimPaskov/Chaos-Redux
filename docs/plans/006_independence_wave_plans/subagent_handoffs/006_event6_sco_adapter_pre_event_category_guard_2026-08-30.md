# Event 006 Scotland adapter pre-event category guard

Date: 2026-08-30

Scope: the IW-001 Scotland decision category visibility gate. This handoff records one narrow source fix; no Event 021 gameplay, package setup, or Event 006 allocator behavior was changed.

## Finding

`is_independence_wave_sco_package` accepts both the live Event 006 origin and the separate Event 021 civil-war adapter (`common/scripted_triggers/006_independence_wave_scotland_wales_package_triggers.txt:8-22`). The adapter deliberately reuses IW-001 package setup while keeping `independence_wave_active_origin` unset. Its setup path can nevertheless set `independence_wave_iw_001_setup_complete` (`common/scripted_effects/021_random_civil_war_parent_effects.txt:1454-1490`).

Before this change, `independence_wave_sco_state_category` tested only the package predicate and setup receipt, so the adapter could expose the Event 006 Scotland decision category before an Event 006 origin had fired.

## Change

`common/decisions/categories/006_independence_wave_categories.txt` now requires `is_independence_wave_active_country = yes` before the IW-001 package and setup checks. The category remains available to a real Event 006 country, while the Event 021 adapter retains its internal package reuse without exposing Event 006 decisions, costs, missions, or UI.

## Evidence

- `is_independence_wave_active_country` requires `independence_wave_active_origin`, the Independence Wave liberation origin, and no ended-origin flag (`common/scripted_triggers/006_independence_wave_triggers.txt`).
- The other Event 006 package predicates already include this active-country contract; IW-001 is the only package predicate with the separate Event 021 adapter exception.
- The root Event 006 entry remains hidden and triggered-only; its public report is still commit-gated in `events/006_independence_wave.txt`.

## Validation

- `python -B .tools/audit_event6_allocator.py` passed: exact 3/4/5/7/10 ladder, retired pre-event crisis surface, and no pre-event category/mission/cost/queue.
- `python -B .tools/audit_event6_flags.py --strict` passed: 102 registered and complete flag families.
- `python -B .tools/audit_event6_gui_matrix.py` passed: five tab contracts and cleanup/static/animated sibling checks.
- No live HOI4 or save/load claim is made.

## Simplifications and blockers

No fallback or identity substitution was used. This is a source-level visibility guard; the Event 021 adapter's separate UI remains outside Event 006 and was not redesigned.
