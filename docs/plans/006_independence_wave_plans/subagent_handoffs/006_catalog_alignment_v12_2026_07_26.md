# Event 006 catalog alignment v12

Date: 2026-07-26

Scope: read-only audit of the Event 006 catalog mirror against current player-facing localisation and `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`.

## Verdict

**PASS.** The authoritative workbook already matches the current shared Event 006, evolution, Liberations cluster, and SCN-008 mirror fields. No workbook cell was changed, so the export-only CSV snapshots were not regenerated.

## Exact comparison evidence

The following workbook cells were read directly from `docs/spreadsheets/chaos_redux_events_catalog.xlsx`:

- `Events!A7:B7` — ID `6` and `Independence Wave`; `B7` matches `chaosx.event_name.6` in `localisation/english/chaosx_event_names_l_english.yml`.
- `Events!C7` — matches the static player-facing paragraph of `chaosx.events_log.window.event_details.independence_wave` in `localisation/english/chaosx_gui_l_english.yml`. The localisation key appends dynamic rival-bloc lines at runtime; the catalog intentionally mirrors only the shared paragraph and does not enumerate package IDs or route-specific detail, as required by the source-of-truth map.
- `Events!D7:H7` — each cell exactly joins the corresponding `independence_wave.evolution.<1-5>.title` and `.body` values with one blank line from `localisation/english/006_independence_wave_evolutions_l_english.yml`.
- `Events!J7:M7` — `Minor Repeatable`, cluster `2`, member severity `Medium`, and status `In progress` match the current catalog contract and source-of-truth map. The status remains deliberately non-terminal while whole-event completion evidence is open.
- `Clusters!A3:G3` — cluster `2`, `Liberations`, the exact `chaosx.events_log.window.cluster_details.description.liberations` text, members `5, 6`, `Minor Repeatable`, chaos level `1`, and status `In progress` match the current cluster surface and source-of-truth map.
- `Scenarios!A9:F9` — `SCN-008`, `Every Banner Rises`, the exact sovereign-scatter premise, all eight registered type names in UI order, all four `Low`/`Medium`/`High`/`Maximum` impact paragraphs, and status `Needs Testing` match `localisation/english/006_independence_wave_scenario_l_english.yml` and the source-of-truth map.

The direct comparison covered 25 fields and produced 25 exact passes.

## Workbook and export disposition

- Workbook path: `docs/spreadsheets/chaos_redux_events_catalog.xlsx` (unchanged).
- Sheets/rows audited: `Events!7`, `Clusters!3`, `Scenarios!9`.
- Existing CSV rows for Event 006, Liberations, and SCN-008 match the workbook after normalizing Excel numeric cells to CSV text.
- `python .tools/export_event_catalog_csv.py` was not run because no workbook save occurred; the required post-save export condition was not triggered.

## Remaining status boundary

No status was promoted. Event 006 and the Liberations cluster remain `In progress`; SCN-008 remains `Needs Testing`, consistent with the authoritative source-of-truth map and the unresolved whole-event/runtime evidence boundary.
