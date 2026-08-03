# Event 006 catalog alignment current audit — 2026-08-03

## Scope

Audited the editable workbook `docs/spreadsheets/chaos_redux_events_catalog.xlsx` for Event 006 / Cluster 2 / SCN-008 against the current Event 006 player-facing localisation and the current static authority. No gameplay, localisation, scripted-localisation, or other event rows were edited.

## Workbook result

No workbook cells required a change. The scoped rows are:

- `Events!A7:M7` — Event ID `6`, `Independence Wave`.
- `Clusters!A3:G3` — Cluster ID `2`, `Liberations`.
- `Scenarios!A9:F9` — `SCN-008`, `Every Banner Rises`.

Exact mirror checks passed for:

- `Events!B7` event name and `Events!C7` static Event Details paragraph. The runtime key also appends the two dynamic rival-bloc scripted-localisation lines; those dynamic lines remain runtime-only under the established static catalog contract.
- `Events!D7:H7` all five evolution title/body pairs (`independence_wave.evolution.1` through `.5`).
- `Clusters!B3:C3` cluster name and Liberations detail, plus the accepted member list `5, 6`.
- `Scenarios!B9:D9` scenario name, Sovereign Scatter detail, and all eight current mode names.
- `Scenarios!E9` Low, Medium, High, and Maximum impact paragraphs, each copied from the current scenario localisation keys.
- `Events!I7` remains empty because Event 006 has no terminal world-end scenario field.

No blocked or `needs_user_review` wording cells were found in the scoped mirror fields.

## Status boundary

The authority remains whole-event **HOLD / PARTIAL**. `Events!M7` and `Clusters!G3` remain `Partially Available`, while `Scenarios!F9` remains `Playable`. The current evidence sometimes uses `In progress` and `Needs Testing`, but those labels are not permitted by the workbook's existing validation lists. These status/schema contradictions are recorded for user review and were not guessed or written into the workbook.

## Workbook integrity and export

- Workbook formulas: `0`; Excel error cells: `0`.
- Workbook calculation setting remains `fullCalcOnLoad=True` with no formulas requiring recalculation; no workbook save was needed.
- Existing sheet/table structure and validation ranges were preserved (`Events!A1:M1015`, `Clusters!A1:G15`, `Scenarios!A1:F12`).
- Ran `python .tools/export_event_catalog_csv.py` from the mod root for source/export verification. Result: success.
- Export snapshots were unchanged after the run: Events `183 x 13`, SHA-256 `c70410fdd8ece66449f09522c44a8133b8073bd5e9902e8a8a12abd5b609c677`; Clusters `14 x 7`, SHA-256 `ebe0348e9773f2f1affee0d6067503e1be40f3297fe5fac404ceccdae4d4cb2e`; Scenarios `13 x 6`, SHA-256 `1ab7ee1189ba99a8167f2cb98f8e61b698b6adda8b3c648a8b49cc0d67a87708`.

## Changes and remaining mismatches

Changed workbook sheets, rows, columns, and Event IDs: none.

Changed export files: none (the exporter reproduced the committed snapshots exactly).

Remaining item for parent/user review: decide whether the catalog validation schema should add `In progress` and `Needs Testing`, or whether the current conservative status mapping should remain. No status promotion or completion claim was made.
