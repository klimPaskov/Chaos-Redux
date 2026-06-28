# Chaos Redux Repository Cleanup Completion Report

## Scope

This cleanup covered shared Chaos Redux systems and Events 1-10. Events 11 and higher were left alone except where they appeared in shared catalog, cluster, scenario, or documentation surfaces.

Source prompt: `docs/plans/repo_cleanup/repo_cleanup_master_prompt.md`

## Systems Inspected

- random event registration, default disable gates, active-pool gates, and Event 006 reserved wiring
- settings and manual trigger surfaces
- event logs, event details, evolution details, clusters, and reserved catalog text
- triggerable scenarios and reserved scenario text
- chaos meter, deaths, air cleanliness, condemnation, and world-threat documentation surfaces
- shared dynamic effects and triggers
- shared script constants and helper documentation
- shared localisation and spreadsheet catalog fields
- on-action call sites for shared helper cleanup
- super-event selector surfaces at a mapping level only

## Events 1-10 Surfaces Inspected

- Event 001: registration, event-log detail linkage, localisation/docs references
- Event 002: zombie world-threat linkage, civilian-system trigger usage, event-log detail docs
- Event 003: Holy Realm world-threat linkage, civilian-system trigger usage, shared docs references
- Event 004: random-war cluster membership and event-log evolution surfaces
- Event 005: Soviet Collapse cluster membership, world-threat linkage, spreadsheet/catalog fields
- Event 006: reserved event file, localisation, random-event registration, active-pool exclusion, cluster membership, spreadsheet/catalog fields
- Event 007: Fury registration, cluster membership, world-threat linkage, scenario/event-log surfaces
- Event 008: Tensions Rising registration, cluster membership, event-log detail surfaces
- Event 009: White Peace registration, cluster membership, event-log detail surfaces
- Event 010: Death registration, world-threat linkage, scenario/event-log surfaces

## Events 11+ Shared References Touched

- Event 012 and Event 013 reserved cluster/scenario/catalog text in localisation, system docs, and the event catalog workbook
- No Events 11+ gameplay event files, effect files, focus trees, decisions, or country packages were edited.

## Files Changed

- `common/scripted_effects/chaosx_dynamic_effects.txt`
- `common/scripted_effects/chaosx_dynamic_effects.md`
- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/scripted_triggers/chaosx_dynamic_triggers.txt`
- `common/scripted_triggers/chaosx_dynamic_triggers.md`
- `docs/plans/repo_cleanup/repo_cleanup_goal_prompt.md`
- `docs/plans/repo_cleanup/repo_cleanup_master_prompt.md`
- `docs/plans/repo_cleanup/repo_cleanup_completion_report.md`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- `docs/systems/event_clusters.md`
- `docs/systems/triggerable_scenarios.md`
- `docs/systems/world_threat_mechanic.md`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`

## Cleanup Performed

- normalized the cleanup prompt filenames to the paths used by the goal prompt
- removed one live debug log from the dormant `modify_state_population_by_percent` helper
- replaced the open-ended TODO on `clear_special_chaos_country_civilian_effects` with a scoped helper comment
- documented `clear_special_chaos_country_civilian_effects`
- documented `uses_normal_civilian_systems`
- filled in the blank `is_desert_state` helper documentation
- removed duplicate state entries `857` and `402` from `is_desert_state`
- clarified that Event 006 is a reserved catalog entry excluded from active random-pool selection
- updated reserved scenario, event-detail, and cluster-detail wording to avoid player-facing placeholder and rework phrasing
- aligned the event catalog workbook with the reserved-entry terminology
- updated world-threat documentation to reflect current registered sources and owner files

## Helpers, Triggers, Constants, And Code Movement

- Helpers changed: `modify_state_population_by_percent`, `clear_special_chaos_country_civilian_effects`
- Trigger changed: `is_desert_state`
- Trigger documentation added: `uses_normal_civilian_systems`
- Constants changed: none
- Code moved: none
- Prompt docs moved: cleanup prompt files moved from their prefixed names to the canonical repo-cleanup prompt names
- New helper files: none

## Duplication And Dead Code

- Removed duplicate `is_desert_state` state IDs.
- Removed one dormant-helper debug log.
- Deleted no helpers. Dormant helpers retained:
  - `modify_value_based_on_chaos_tier`, retained because it is a plausible chaos-scaling helper and deletion would be a design decision.
  - `damage_buildings_in_random_states`, retained because it is a plausible future sabotage helper and needs a dedicated behavior audit before reuse or removal.
  - `modify_state_population_by_percent`, retained as a focused future hook after removing its debug log and documenting the current deaths-system gap.
  - Event 006 reserved wiring, retained because registration, active-pool exclusion, cluster zero participation, localisation, and catalog text show intentional reserved infrastructure.

## Deferred Migrations

- Do not expand `clear_special_chaos_country_civilian_effects` into Mass Panic variants without Event 049 scope.
- Do not move `refresh_world_threat_state` into a dedicated world-threat effects file until all Event 002, 003, 005, 007, 010, and Germany Mengele call sites are migrated together.
- Do not consolidate event-log evolution setup across Events 001, 002, 004, and 007 until actor target semantics are reviewed per event.
- Do not broadly convert raw event IDs to constants in shared settings/event-log/event-firing files without a dedicated migration pass.
- Do not clear persistent global event targets without an ownership table for each event chain.
- Do not refactor triggerable scenario sorting into a generic helper until the UI list and launch-selection behavior are validated together.

## Validation

- Verified prompt files exist at the goal paths.
- Verified touched localisation files still use UTF-8 with BOM.
- Verified no duplicate state IDs remain in `is_desert_state`.
- Verified Event 006 remains registered as reserved infrastructure, excluded from active random-pool selection, and configured with zero cluster participation.
- Verified workbook reserved text no longer contains the stale future-rework wording and has no formulas to recalculate.
- Reviewed both subagent handoffs and folded safe findings into this patch.

## Behavior Changes

- No gameplay pacing, firing, scenario launch, world-threat, cluster, or event behavior was intentionally changed.
- The only script behavior change is removal of an unused helper debug log if `modify_state_population_by_percent` is called in the future.
- Player-facing wording for reserved and generic fallback UI text is cleaner and less process-oriented.

## Simplifications, Omissions, And Blockers

- No fallbacks or placeholder replacements were introduced.
- No broad risky migrations were implemented.
- Events 11+ old event-specific implementations were intentionally not audited or cleaned.
- The cleanup is bounded to safe shared-system maintenance and documentation/localisation/spreadsheet alignment.
