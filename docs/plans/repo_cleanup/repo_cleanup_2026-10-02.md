# Repository cleanup pass: 2026-10-02

This record covers the 2026-10-02 cleanup pass run under the user instruction to carry out `chaos_redux_repo_cleanup_master_prompt.md` for shared systems and confirmed-reworked Events 1 to 40.
It follows the earlier tranche recorded in [`repo_cleanup_completion_report_2026-08-22.md`](repo_cleanup_completion_report_2026-08-22.md) and does not repeat its reviewed items.
The user's chat instruction is the authorization for this pass; the master prompt's 2026-09-05 superseded disposition does not limit it.

## Eligibility

Rework status comes from the `Status` column of `docs/spreadsheets/chaos_redux_events_catalog.xlsx` (read through its `chaos_redux_events_catalog.csv` export without editing either file) together with the event implementation overviews under `docs/events/`.
The catalog `Legend` sheet distinguishes `Needs Testing` (implemented and awaiting validation) from `To Be Reworked`.
An event is eligible only when the catalog reads `Needs Testing` and a current implementation overview exists.

| Event | Catalog status | Implementation evidence | Decision |
| --- | --- | --- | --- |
| 1 to 20 | Needs Testing | `docs/events/001_communism_spread/overview.md` through `docs/events/020_black_plague/overview.md` | Eligible |
| 21 Random Civil War | Needs Testing | `docs/events/021_random_civil_war/overview.md` | Eligible |
| 22 Spain Antisemitism | To Be Reworked | Specification package only | Skipped: not reworked |
| 23 SOV Nuclear Bombs | To Be Reworked | `docs/events/023_sov_nuclear_bombs/` exists with active uncommitted work | Skipped: catalog and documents conflict |
| 24 Video Game in Sweden | Needs Testing | `docs/events/024_video_game_in_sweden/overview.md` | Eligible |
| 25 Alien Technology in Antarctica | To Be Reworked | Specification and plans only | Skipped: not reworked |
| 26 Black Friday | Needs Testing | `docs/events/026_black_friday/overview.md` and `docs/events/026_black_friday.md` | Eligible |
| 27 Doctrine Research | Needs Testing | `docs/events/027_doctrine_research/overview.md` | Eligible |
| 28 Asteroid Incoming | Needs Testing | `docs/events/028_asteroid_incoming/overview.md` | Eligible |
| 29 Riches Found | Needs Testing | `docs/events/029_riches_found/overview.md` | Eligible |
| 30 Time Traveler | To Be Reworked | Specification package only | Skipped: not reworked |
| 31 Random Terror | To Be Reworked | `docs/events/031_random_terror/overview.md` describes an implementation | Skipped: catalog and documents conflict |
| 32 Missiles | Needs Testing | `docs/events/032_missiles/overview.md` and `docs/events/032_missiles.md` | Eligible |
| 33 Acid Rain | To Be Reworked | `docs/events/033_acid_rain/overview.md` describes an implementation | Skipped: catalog and documents conflict |
| 34 Industrial Boom | To Be Reworked | Specification package only | Skipped: not reworked |
| 35 Great Depression 2.0 | Needs Testing | `docs/events/035_great_depression.md` | Eligible |
| 36, 37, 38, 40 | To Be Reworked | Specification packages and plans only | Skipped: not reworked |
| 39 Murder Mystery | Needs Testing | No `docs/events/` overview; implementation is still being committed | Skipped: no implementation record |

Eligible events: 1 to 21, 24, 26, 27, 28, 29, 32, and 35.
Events 41 and higher are outside event-specific scope.

## Method

Mechanical scans built candidate lists: scripted effects and triggers with no token reference outside their own definition, `defined_text` selectors with no consumer, localisation keys left without a reference, script-constant keys without a `constant:` reader, `yes`/`no` calls to names that are neither mod, vanilla, nor engine effects or triggers, event IDs referenced but never defined, and GFX names with no sprite definition.
Six read-only audits then classified every candidate as dead, dynamically constructed, a documented hook, a prior retention, or uncertain, and a shared-logic audit looked for duplicated logic, magic numbers, lifecycle drift, and stale references.
The parent reviewed every verdict before patching, verified removals by definition name and brace balance, rescanned for knock-on dead code until stable, and rebuilt each mixed-ownership file so other agents' pending hunks stay out of these commits.
Files with active uncommitted work by other agents were edited only through separable hunks in shared owners.

## Patched

### Bug fixes with behaviour changes

| Area | Fix | Justification |
| --- | --- | --- |
| Event 006 | `is_at_war = yes` became `has_war = yes` in `events/006_independence_wave.txt` and `common/scripted_effects/006_independence_wave_opening_dispatch_effects.txt`. | `is_at_war` is not a HOI4 trigger, so the three war checks never matched. |
| Chaos Meter | The `on_annex` hook requires both an enabled meter and a non-zombie annexed country. | The ZZZ exclusion was written as an OR with the disabled-meter check, so it only applied when the meter was off and zombie annexations still added Chaos. |
| Event Log | The ID sort mode uses `events_log_history_append_rows_by_event_id_sort`. | The fixed 1 to 2000 loops stopped at the 1,000-iteration engine cap, so ascending showed only IDs up to 1000, descending showed only IDs from 1000 to 1999, and special history IDs never appeared. |
| Triggerable scenarios | Name-descending lists Random Civil War once and ID-descending lists it first. | The name-descending view listed it twice and the ID-descending view omitted it. |
| Events 028 and 029 | The shared history recorder calls `asteroid_incoming_bind_opening_history_sequence` and `riches_found_bind_history_payload`, and Event Details calls `riches_found_load_open_history_payload`. | Both events' history helpers documented this wiring but had no caller, so Event 028 outcomes never updated their row and Event 029 details never loaded their mine. |
| Event 027 | A successful doctrine adoption calls `brilliant_scientist_record_doctrine_research`, and the confirmation option shows its tooltip under the same guards. | The Event 027 architecture plan requires this Event 016 hook, and the rework had dropped every call. |
| Shared helper | `damage_buildings_in_random_states` counts controlled states from zero and applies its optional population loss as a reduction only when requested. | The documented example added population, an omitted input removed population, and the state count was one too high. The helper has no live caller. |

### Dead code removed

Every removal has no direct, dynamic, GUI, localisation, or documented-hook reference.

- Shared event system: eleven `_legacy` cluster effects and the three order helpers only they used, twenty-four retired settings effects, the unused `check_event_availability` trigger, sixteen per-scenario selectors plus `trigger_final_silence_scenario`, `world_end_final_silence_scenario_enabled`, `can_liberation_release_lock_plan`, and `condemnation_relation_is_strategic_embargo_target`.
- Chaos Meter: ten superseded deaths, combat, tier, and on-action handlers, the knock-on `chaos_meter_deaths_entry_matches_active_filter`, and the commented `on_new_term_election` hook.
- Shared scripted localisation: thirteen settings selectors from an older settings window, twenty-nine Chaos Meter, air, and condemnation selectors, whose condemnation cost keys did not exist, and six Event Log label selectors.
- Eligible events: Events 1, 2, 3, 7, 8, 10, 11, 13, 14, 15, 16, 18, 19, 20, 27, 28, 29, 32, and 35 lost unreferenced helpers, including the superseded Event 027 level-capture effects, the Event 016 Computation compatibility aliases, the Event 019 Muster Board close action, Holy Realm dashboard sprite selectors that pointed at unregistered sprites, and unwired Event 1, 2, 5, 11, 13, and 18 dashboard selectors.
- Knock-on cleanup removed 30 localisation keys and 41 script-constant keys that only the removed code used, plus the comment headers attached to removed blocks.

In total 342 scripted effects, scripted triggers, and scripted-localisation selectors were removed.

### Simplification, normalization, and new helpers

- `condemnation_load_pair_target_cost_score_override` replaces six byte-identical blocks in `common/scripted_effects/condemnation_sanctions_effects.txt` and uses `constant:condemnation_cost.cost_multiplier_score_minimum` instead of a literal zero. It is documented in `docs/systems/cbrn_warfare/condemnation/condemnation_sanctions.md`.
- `events_log_history_append_rows_by_event_id_sort` mirrors the existing actor-sort helper and is documented in `common/scripted_effects/chaosx_events_log_effects.md`.
- `is_special_chaos_country` and `is_actual_nonhuman_country` call `is_death_country` and `is_cannibalism_country` instead of repeating their members, and drop a redundant ZZZ check.
- Literal event IDs in the Event Log actor defaults, settings, and scenarios use their event constants. Settings timer tiers, the initial timer modifier, and the minimum timer floor use existing event-system and settings constants. Chaos Meter and Event 010 thousands conversions use `constant:chaos_meter_deaths.people_per_k`, and the irreversible fallout modifier uses its previously unread duration constant.
- Identical if/else branches in `adjust_event_id_for_filter`, six no-op self-assignments in the clone scenario, and a duplicated `was_human_yesterday` update were removed, and a misplaced cluster comment was moved to the block it describes.

### Documentation

A documentation curator corrected stale file pointers, nonexistent helper names, and missing behaviour in thirty helper and system documents, including `chaosx_dynamic_effects.md`, `chaosx_dynamic_triggers.md`, the CBRN helper references, the fallout NZL helper docs, Event 006 constant pointers, the logging-controls and deaths documents, and air-cleanliness, chemical, biological, and condemnation system docs.
The parent reviewed those edits, removed two update-history phrasings, and spot-checked the rewritten battlefield-operations claims against source.
The events index gained its missing Event 028 row, the Event 003 overview records its three reserved text selectors, the Event 027 overview records the Event 016 integration, and the Chaos Meter popup doc records the zombie annexation exclusion.

## Kept with reasons

- Event 006 and Event 012 dead candidates, Event 005 dead candidates, and Event 021, 023, 024, and 026 candidates sit in files with active uncommitted work and remain for their owners.
- `black_friday_fury_pay_core_cost` became unreferenced after the Event 007 core-cost pair was removed, but it lives in Event 026's in-progress file.
- The three Event Log evolution `TypeView` selectors have no consumer, but pending Event 042 work is adding rows to them. Remove them once that work lands.
- The five Chaos Meter Deaths selectors stay with the unresolved Deaths overlay and dashboard decision.
- Event 016 directorate sprite routers have registered art and no GUI consumer, and wiring them is GUI work.
- Event 019 claimant selectors point at portraits that are still pending.
- `GetBlackFridayEventListStatus` stays while Event 026 is under active work.
- Documented hooks stay: world-threat source triggers, Event 032 contract aliases, Event 021 treaty API triggers, Event 019 achievement disqualifier setters and scenario API, Event 016 cross-event APIs and prior-retained helpers, unit-family `remove_public_additions` callbacks, the reserved `clear_special_chaos_country_civilian_effects`, and the `chaosx_test` and debug-probe console entries.
- Uncertain items stay: `chaosx_apply_non_ai_crisis_pressure_extreme_factor`, `death_decay_maritime_evidence` with the two Event 010 evidence-band triggers, `soviet_collapse_report_corridors_decide_news`, Event 029 closure and exhaustion helpers, Event 029 and 032 achievement helpers, and Event 032 survey, warning, inheritance, and natural-disaster bridge helpers.
- Script-constant keys that were already unread before this pass, about 5,800 repository-wide and mostly enumeration members, were not removed because constants carry no runtime cost and many document value domains.

## Deferred bugs and migrations

These need a design or owner decision and are not implemented here.

1. Event 032 survey and warning-verification missions can never succeed because nothing calls `missiles_complete_survey` or `missiles_complete_warning_verification`. Choosing when a survey or verification completes is a timing design decision.
2. Event 032 achievement disqualifier flags are never set, so force-trigger, debug, SCN-015, and ceased-country disqualification are inactive.
3. Event 029's seven documented achievements have localisation, sprites, and route triggers but no entry in `common/achievements/chaos_redux_achievements.txt`, which carries other agents' pending work.
4. Event 029 closure and exhaustion states are unreachable because the closure decision bypasses its helpers.
5. Event 021 external-war and Fury evidence producers are uncalled while Event 021 is under active work.
6. Event 028 does not call `brilliant_scientist_record_asteroid_impact`. Its own handoff requires an explicit Event 016 and Event 028 integration decision.
7. Event 019 achievement disqualifier setters are never called.
8. Event 006 guard missions IW-059 and IW-085 cannot start, the COG and regional overlay guard payments lack an affordability gate, `independence_wave_handle_former_host_death` is unwired, and the Open Sovereignty formable weighting cannot fire.
9. The Event 005 world-threat preview counts seven sources while `refresh_world_threat_state` counts ten.
10. Shared-logic helper candidates in files with pending work: duplicated `find_event_in_array` loops and unfired counters in settings, the Event Log refresh and initialization duplicates, the 32-array Event Details clear, a chaos-history value helper, the cap-reduction and increment-step helpers, and `chaos_tier_at_least_N` triggers across more than 900 OR trees.
11. 169 hand-written stockpile debits could use the dynamic stockpile removal helpers, but each site needs a read-after-negation check.
12. The default-enabled event list, the Event 91 weight initializer, and related registry literals belong with the deferred registry items in [`shared_system_migration_plan_2026-08-22.md`](shared_system_migration_plan_2026-08-22.md) and need a probability auditor pass.
13. Event 015 inline `world_in_threat` checks in AI weight blocks could use `is_world_in_threat`, which needs a probability before-and-after pass.
14. Six constant files define "people per thousand" separately, and consolidation touches event-owned files.

## Validation

- Every removal was verified by comparing HEAD and working-tree definition names and brace balance. A full rescan found no live reference to any of the 342 removed names in script, interface, localisation, or history files.
- The undefined-call scan lost `is_at_war` and gained nothing new.
- No unsupported `<=` or `>=` operator, no whole-world on-action, and no fallback or placeholder was introduced.
- The rebuilt mixed-ownership files differ from the working tree only by other agents' pending hunks.
- No HOI4 MCP inspection was run for this pass. The shared-logic audit recorded that `hoi4.probability_inspect` returned argument and internal errors, so the deferred weight-related items keep that blocker.
- No live-game validation was performed, and it remains with the user.
