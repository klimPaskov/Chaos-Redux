# Event 006 catalog details sync

Date: 2026-08-30 (Europe/Kyiv).

## Scope and disposition

This bounded spreadsheet pass checked the Event 006 catalog surfaces after the requested localization synchronization gate. The current approved Event Details premise text is already present in the shared worktree, and the scoped workbook fields are already exact mirrors. No workbook edit was justified, so no workbook save or CSV export was performed.

## Workbook rows audited

| Sheet and row | Event or catalog id | Result |
| --- | --- | --- |
| `Events!A7:N7` | Event `6` | No mismatch. Event name, premise, five evolution bodies, empty world-end field, and metadata match current source. |
| `Clusters!A3:G3` | Cluster `2` | No mismatch. Liberations name/details, member list `5, 6`, type, chaos level, and status match current source. |
| `Scenarios!A8:F8` | `SCN-008` | No mismatch. Every Banner Rises name, detail, eight type labels, four intensity paragraphs, and status match current source. |

## Source alignment evidence

- `Events!C7` matches `chaosx.events_log.window.event_details.independence_wave` in `localisation/english/chaosx_gui_l_english.yml:1090`.
- `Events!D7:H7` match `independence_wave.evolution.1.body` through `.5.body` in `localisation/english/006_independence_wave_evolution_l_english.yml:12,14,16,18,20`.
- `Clusters!B3` and `Clusters!C3` match the Liberations name/details keys in `localisation/english/chaosx_gui_l_english.yml:878,418`.
- `Scenarios!B8:E8` match the current scenario name, sovereign-scatter detail, eight type labels, and Low/Medium/High/Maximum impact keys in `localisation/english/006_independence_wave_scenario_l_english.yml:2,5-14,23-26`.
- A direct workbook-to-localization comparison found 12 mirror checks and 0 mismatches. The generated Event 006, Cluster 2, and SCN-008 CSV rows also match their workbook rows field-for-field.

## Status and spoiler checks

Preserved statuses are Event 006 `Needs Testing`, SCN-008 `Needs Testing`, and Liberations `Partially Available`. The scoped cells contain no exact Join thresholds, rival-compact implementation values, automatic-wave counts, package/formable ids, or retired pre-event crisis wording. Event 006 `World-End Scenario` remains empty.

## Changed files and exporter

- Changed workbook path: none.
- Changed sheets, rows, columns, or event ids: none.
- Changed CSV exports: none.
- `python .tools/export_event_catalog_csv.py`: not run because no workbook save occurred.
- Blocked or `needs_user_review` cells introduced: none.

The workbook and export snapshots remain the editable-source/export-only pair already present in the shared worktree. No gameplay or localization files were edited.
