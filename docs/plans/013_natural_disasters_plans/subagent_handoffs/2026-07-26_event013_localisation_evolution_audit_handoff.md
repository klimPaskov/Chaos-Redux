# Event 013 localisation and evolution audit handoff

Date: 2026-07-26

Scope: Event 013 player-facing localisation, Event 013 scripted localisation references, evolution names and summaries, event-log and Event Details routing, abnormal-path GUI labels, and Event 013 cluster wording. Shared/general super-event and event-log GUI localisation was inspected but not edited.

## Audit result

The accepted evolution names are already used without `Evolution I`, `Evolution II`, or `Evolution III` prefixes:

- `natural_disaster.evolution.stage_1.title`: `Wider Disaster Seasons`
- `natural_disaster.evolution.stage_2.title`: `Regional Cascades`
- `natural_disaster.evolution.stage_3.title`: `Abnormal Paths`

`natural_disaster.evolution.summary` already exposes only `Chaos Tier` and `Evolution Stage` through the existing dynamic scripted-localisation calls. No evolution-name or summary rewrite was needed.

The Event 013 event-log mappings in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` resolve all three title keys consistently for the event log, selected history, Event Details, and selected evolution surfaces. The Event 013 stage constants remain aligned with the accepted tier/stage definitions.

## Narrow patch

Changed file: `localisation/english/013_natural_disasters_l_english.yml`

Changed keys:

- `natural_disaster.relief_status.refused`: changed `the affected government refused foreign relief` to `the affected country refused foreign relief`.
- `natural_disaster.gui.result.unresolved`: changed `unresolved damage remains under the current authority` to `unresolved damage remains in the affected state`.
- `natural_disaster_foreign_relief_dependency_desc`: removed the abstract `ministries and` phrase so the description now reads `Imported equipment and routes saved lives, but local distribution now depends on foreign schedules, liaison officers, and replacement supplies.`

Before these edits, the affected-state result surface and foreign-relief text used generic institutional framing. After the edits, the same gameplay outcomes remain visible through concrete country/state and local-distribution wording.

No new scripted localisation was added. Existing dynamic state, family, severity, route, timer, and cost localisation remains in place. The unresolved-result key is selected by the existing Event 013 scripted-localisation result mapper, so `affected state` is intentionally a safe concrete label rather than a new scope-dependent interpolation.

## Required audit lists

Missing keys: none found in the scoped Event 013 event fields or Event 013 scripted-localisation `localization_key` references when checked against the repository English localisation set. The Event 013 abnormal-path interface's 65 localisation-shaped tokens also have definitions.

Duplicate keys: none within `localisation/english/013_natural_disasters_l_english.yml`, and no duplicate Event 013-owned keys were found across the repository English localisation files.

Scripted-localisation issues: none found in the Event 013 scripted-localisation mappings. Evolution type, stage titles, bodies, summary, event-detail title, history title, and selected-evolution title mappings all point to the current Event 013 keys and stage constants. Shared stage labels intentionally remain numeric and were not changed.

Dynamic-text opportunities: no required additions. The evolution summary already uses dynamic chaos-tier and stage calls. Event 013 GUI and report surfaces already use dynamic state, family, severity, route, timer, and cost calls where those values are available. The patched unresolved-result label does not have a guaranteed selected-state scope at its localisation call site, so a stable `affected state` phrase avoids a misleading interpolation.

Cross-surface mismatch notes: none found for evolution titles, stages, tiers, event-log entries, Event Details entries, selected evolution details, or the Event 013 cluster description. The shared cluster and super-event GUI surfaces were left untouched by scope. The Event 013 super-event prose uses governments as in-world actors, not as a generic announcer, and remains physically grounded.

File encoding: `localisation/english/013_natural_disasters_l_english.yml` retains its UTF-8 BOM after the patch. No other localisation file was edited.

## Validation

- Parsed all 284 repository English localisation files and found zero missing keys for 587 direct Event 013 event/scripted-localisation references.
- Parsed the Event 013 localisation file and found 1,113 keys with no duplicate definitions.
- Checked Event 013-owned key ownership across English localisation files and found no duplicate owners.
- Checked the 65 localisation-shaped tokens in `interface/013_natural_disasters.gui`; all resolve.
- Rechecked the evolution title lines and summary after editing; titles remain unprefixed and the summary remains tier plus stage only.

Skipped validation: no game launch or live UI session was run, per repository instructions. Shared GUI and super-event files were not modified, so no shared-surface rewrite validation was necessary.

Unresolved wording decisions: `communications offices` remains because it names concrete local warning infrastructure. `Government` in `chaosx_super_event.71.d` remains as an in-world actor reference rather than a generic institution or system speaker. No additional Event 013 wording blocker is known.

