# Event 23 spreadsheet cluster cleanup

Status: Complete.

Scope: Remove Event 23 (`SOV Nuclear Bombs`) from its existing Military Preparation cluster membership only. No Arms-race cluster was created, and no content was imported from `docs/systems/event_system/event_clusters.md`.

Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

## Exact workbook changes

`blank` below means an empty Excel cell (`None`).

| Sheet | Cells | Before | After |
| --- | --- | --- | --- |
| Events | `A24`, `B24`, `L24` | `23`; `SOV Nuclear Bombs`; `blank` | `23`; `SOV Nuclear Bombs`; `blank` |
| Clusters | `D19` | `22, 23, 42, 56, 64` | `22, 42, 56, 64` |
| Clusters | `E19` | `High, Severe, Low, Medium, Medium` | `High, Low, Medium, Medium` |
| Cluster Memberships | `A72:G72` | `18`; `Military Preparation`; `2`; `23`; `SOV Nuclear Bombs`; `Severe`; `blank` | `blank`; `blank`; `blank`; `blank`; `blank`; `blank`; `blank` |
| Cluster Memberships | `A73:G73` | seven blank cells | seven blank cells |

The remaining Military Preparation membership rows were preserved exactly: row 71 is slot 1 / Event 22 / `Concentration Camps` / `High`; row 74 is slot 4 / Event 42 / `Equipment from Heavens` / `Low`; row 75 is slot 5 / Event 56 / `The Navy` / `Medium`; and row 76 is slot 6 / Event 64 / `Border Fortifications` / `Medium`.

The Event 23 membership row was blanked in place, so the existing blank separator row 73 and all existing slot values remain in their original worksheet positions. The four remaining cluster IDs, severities, and nonblank membership rows are aligned one-to-one.

## Validation

- `Events!A24` remains `23`, `Events!B24` remains `SOV Nuclear Bombs`, and `Events!L24` remains blank.
- `Clusters!D19` and `Clusters!E19` each contain four entries, with IDs `22, 42, 56, 64` aligned to severities `High, Low, Medium, Medium`.
- `Cluster Memberships!A72:G72` is fully blank, `A73:G73` remains fully blank, and the remaining Military Preparation memberships are unchanged.
- Exact searches found no value `23` and no `SOV Nuclear Bombs` in the `Clusters` or `Cluster Memberships` sheets after the edit.
- The saved workbook retained the existing five sheet names, tables, validations, dimensions, blank separator row, and cell styles; the workbook has zero formula cells.

## Export validation

Command run from the mod root: `python .tools/export_event_catalog_csv.py`

Exporter result: `success`.

- `docs/spreadsheets/chaos_redux_events_catalog.csv`: 165 data rows, 14 columns, SHA-256 `941b3e575e2bdc23d675a6e8e738e78b397a2b3e3a6f34b9bf2d0ae2b92030ac`.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`: 19 data rows, 7 columns, SHA-256 `24a914fb257c99c8fc221c88828a229190de2555629dc751df05df1383be5e1e`.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`: 15 data rows, 6 columns, SHA-256 `96d076700cd9da866ca13c2da9eaa89ddc738613e80d5986c5680e4856183602`.

Relevant exported rows were inspected after export. The Events CSV row for ID `23` has Event Name `SOV Nuclear Bombs` and a blank `Cluster ID`. The Clusters CSV row for Cluster ID `18` has Members (ID) `22, 42, 56, 64` and Member Severities `High, Low, Medium, Medium`. The Scenarios CSV contains no Event ID or cluster-membership fields and has no `23` or `SOV Nuclear Bombs` record across its data rows.

Blocked or needs_user_review cells: none.
