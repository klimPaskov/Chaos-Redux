# IW-045 Bashkiria catalog mirror reconciliation — 2026-08-14

## Scope

Superseded the prior IW-045 catalog append by restoring the editable workbook's `Events!C7` field to the exact static player-facing Independence Wave Event Details premise from `localisation/english/chaosx_gui_l_english.yml`, key `chaosx.events_log.window.event_details.independence_wave`.

## Workbook result

- Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- Sheet/row/field: `Events!C7` / Excel row 7 / `Details`
- Event ID: `6` (`Independence Wave`)
- Removed: the appended Bashkiria package paragraph.
- Preserved: the complete existing premise and Join-eligibility wording, while retaining the established static catalog convention of excluding the runtime-only `[GetIndependenceWaveRivalBlocEventDetails]` and `[GetIndependenceWaveRivalBlocEventDetailsMember]` scripted-localisation suffix.
- Preserved all other Event 006 fields, every other sheet, workbook formatting, formulas, filters, validation, freeze panes, and structure.
- No numeric authority/ladder values, state identifiers, package spotlight, or route-specific summary remains in `Events!C7`.

## Export

After saving the workbook, ran from the mod root:

```text
python .tools/export_event_catalog_csv.py
```

Exporter result: success.

- `docs/spreadsheets/chaos_redux_events_catalog.csv` — 183 rows, 13 columns, SHA-256 `c5c29bc03092fe12d0a44381d59c5865f085c0bc3759240b6d2f151cd21fc6db`
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` — 14 rows, 7 columns, SHA-256 `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` — 12 rows, 6 columns, SHA-256 `66ea4a5802862c1c72f0f3e8ead04cb4f1bfde5e62f88411e3b29f64cb5cf760`

The exported Event ID `6` row matches the reconciled workbook field. No CSV was edited directly.

## Validation / blockers

`Events!C7` contains one paragraph, exactly matching the static localisation premise and Join-eligibility sentence. Its existing style ID `43` and wrapped alignment were preserved. No blocked or `needs_user_review` cells were introduced. Runtime admission, whole-event status, and live validation remain outside this spreadsheet-only handoff.
