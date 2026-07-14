# Event 006 Evolution Implementation Handoff

## Scope Delivered

Implemented the five accepted Event 006 evolution stages as one centralized system with pre-fire frozen-plan effects and active aligned-registry delivery:

| Accepted structural label | Player-facing title | Stage / tier |
| --- | --- | --- |
| Gathering Replicable Independence | The Manuals Cross the Border | 1 / 1 |
| Rising Dormant Nations | Old Nations Wake | 2 / 2 |
| Chaos Armed Birth | Flags Rise Behind the Barracks | 3 / 3 |
| Totalen Sovereign Congress | The Sovereigns Take Their Seats | 4 / 4 |
| World Collapse Open Sovereignty | No Border Is Final | 5 / 5 |

Event Log identity is exactly Event `6`, type `21`, stages `1..5`, tiers `1..5`. Activation dates are recorded by the standard evolution ledger. A pre-fire transition with no Event 006 country defers only its log row; the first initialized Event 006 country becomes the actor, and the stored canonical activation date is supplied to the logger instead of the later actor-registration date.

## Files Added

- `common/script_constants/006_independence_wave_evolution_constants.txt`
- `common/mtth/006_independence_wave_evolution_mtth.txt`
- `common/scripted_triggers/006_independence_wave_evolution_triggers.txt`
- `common/scripted_effects/006_independence_wave_evolution_effects.txt`
- `localisation/english/006_independence_wave_evolutions_l_english.yml`
- `docs/events/006_independence_wave_evolutions.md`
- this handoff

## Files Updated

- `common/scripted_effects/006_independence_wave_package_allocator_effects.txt`
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt`
- `common/scripted_triggers/006_independence_wave_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt`
- `common/scripted_effects/006_independence_wave_packages_region_07_effects.txt`
- `common/scripted_effects/006_independence_wave_packages_region_09_effects.txt`
- `common/scripted_effects/006_independence_wave_packages_region_12_effects.txt`
- `common/scripted_effects/006_independence_wave_packages_region_14_effects.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_effects/006_independence_wave_force_effects.txt`
- `common/scripted_triggers/006_independence_wave_focus_triggers.txt`
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `common/scripted_effects/chaosx_events_log_effects.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_triggers/chaosx_settings_triggers.txt`

## Important Identifiers

Canonical stage flags:

- `independence_wave_evolution_replicable_independence_active`
- `independence_wave_evolution_dormant_nations_active`
- `independence_wave_evolution_armed_birth_active`
- `independence_wave_evolution_sovereign_congress_active`
- `independence_wave_evolution_open_sovereignty_active`

Canonical public triggers:

- `has_independence_wave_replicable_independence_evolution`
- `has_independence_wave_dormant_nations_evolution`
- `has_independence_wave_armed_birth_evolution`
- `has_independence_wave_sovereign_congress_evolution`
- `has_independence_wave_open_sovereignty_evolution`

Planner entry and country opening hooks:

- `independence_wave_prepare_evolution_for_incident`
- `independence_wave_freeze_evolution_plan_state`
- `independence_wave_apply_frozen_evolution_opening`
- `independence_wave_sync_active_evolutions_to_registry`

The shared `record_events_log_evolution_entry` effect now accepts the optional one-shot temporary input `events_log_evolution_date_override`. Existing callers still default to `global.date`; Event 006 uses the override only when a deferred row must retain its canonical transition date.

The former focus and decision references to `independence_wave_evolution_open_sovereignty` and `independence_wave_evolution_5_open_sovereignty_enabled` were replaced with the canonical trigger. No compatibility flags were introduced.

## Planner and Delivery Notes

- The first wave activates all setting-enabled, tier-eligible stages before package selection.
- Later waves schedule MTTH from Event 006 invocations and activate at most one missing eligible stage per due invocation.
- No daily, weekly, monthly, or worldwide on action was added.
- Active delivery is restricted to `global.independence_wave_active_countries` after registry reconciliation; generation validity remains owned by the aligned registry.
- Frozen evolution flags are copied to each package country and cleared with pending package metadata.
- Stage 5 admits nine existing `formable_or_route_only` packages into regional automatic weighting only while its frozen plan flag is present: IW-034, IW-035, IW-074, IW-100, IW-133, IW-144, IW-149, IW-183, and IW-196.
- Event 005 evolution identity, origin, arrays, and collision logic were not modified.

## Armed Birth Adapter Dependency

Per parent direction, this tranche does **not** call `independence_wave_apply_dynamic_starting_force` from the evolution layer and does not edit `006_independence_wave_execution_effects.txt`.

Armed Birth sets `independence_wave_armed_birth_force_authorized`. The force calculator consumes that flag for the budget, equipment factor, and experience factor. Military influence is granted once by the idempotent country transition, so opening countries and already-living countries receive the same increase. The package-initialization adapter still must invoke the existing starting-force entry point after package setup has proven:

1. force profile and military tradition,
2. command roster readiness,
3. at least three reinforcement pathways.

Until that adapter hook is present, the evolution's country values, planner weights, unlock, host tension, and force-calculation mapping are live, but its starting divisions and stockpiles are not materialized by this tranche alone.

## Shared Dirty-File Collision Notes

The worktree already contained unrelated or parallel edits. The following touched shared files were dirty before this tranche and must be merged by identifier, not replaced wholesale:

- `common/scripted_effects/006_independence_wave_package_planner_effects.txt`
- `common/scripted_effects/chaosx_events_log_effects.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_triggers/chaosx_settings_triggers.txt`

Other pre-existing Event 006 dirty files were left untouched unless listed in the updated-files section. In particular, the untracked execution effects file was inspected for call order but not edited.

## Targeted Validation Evidence

- Evolution type `21` is unique in the current constants and script corpus.
- The Event 6 detail registry contains five exact preview rows, and scripted localisation exposes the type plus all five titles across the live view, history view, event-detail view, and selected-detail view; all five selected bodies are present.
- All nine route-only package identifiers have a gated weight publisher and matching random-list reservation entry.
- The evolution effect file contains only aligned-array `for_each_scope_loop` delivery and no `every_country`, `every_possible_country`, periodic on-action, or world iterator.
- The MTTH variable is referenced only by the Event 006 preparation path.
- Legacy Open Sovereignty flag references in the Event 006 focus and decision trigger files are gone.
- The Event 006 evolution localisation file is UTF-8 with BOM.
- The optional Event Chain Viewer reported no issues for namespace `chaosx.nr6` (`report.issues` is empty). Its aggregate scan remained partial because two full-game sources were skipped or exceeded the tool inventory limit; this is a viewer coverage limitation rather than an Event 006 diagnostic.

## Remaining Risk / Dependency

- The package-initialization force adapter hook described above remains a cross-tranche dependency.
- This tranche supplies the five-stage progression, frozen openings, active-country mutations, framework unlocks, and Event Log surfaces. The accepted evolution-specific incident families still require country-event implementation and wiring: copied declarations and institutions, dormant-identity disputes, armed-border crises, congress disputes, and open-sovereignty escalation/containment incidents.
- Replicable Independence still needs its explicit survival feedback: rapid annexation, puppetry, and collapse among earlier Event 6 countries must reduce later opening confidence without relocking the evolution.
- Armed Birth cannot truthfully materialize its stronger divisions or stockpiles until the package adapter proves the force profile, command roster, and reinforcement paths.

No fallback was used. No commit was created.
