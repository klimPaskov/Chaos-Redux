# Event 019 Final Catalog Alignment — 2026-08-22

## Scope

Audited `docs/spreadsheets/chaos_redux_events_catalog.xlsx` after the completed dynamic unit-provider migration. The editable workbook remained the only catalog source. The audit was limited to Event 19, its Event 19 evolution cells, the current direct scenario row, and the requested `SCN-008` row.

## Workbook inspection

- `Events!A20:N20` (`ID 19`, **Soldiers from Nowhere**) was inspected field by field. `A20` remains `19`, `B20` remains the player-facing event name, `C20` remains the exact `chaosx.events_log.window.event_details.infantry_spawn` wording, `D20:G20` contain the four evolution records, `H20` and `I20` remain blank, `J20` remains `Minor Repeatable`, `K20` remains chaos level `1`, `L20` remains blank for the unclustered event, `M20` remains blank, and `N20` remains `Playable`.
- `Events!F20` was updated to retain the exact **Command Fracture** title and body while adding the current decision-only Formation Ledger behavior and closure rule. The text now states that ordinary decisions handle requests, claimant files, demands, coups, and revolt paths, and that the category remains visible only while unresolved or unaccounted formation work, live formations, active claimant or anomalous-family transactions, or pending management operations remain. It also records the takeover, failed-coup, and derivative-revolt closure outcomes in player-facing language.
- `Events!G20` was updated to retain the exact **Anomalous Muster** title and body while adding the provider-migration coverage. The text now includes **Cannibal Irregular Hosts**, provider-owned family presentation and material obligations, derivative-capable family package behavior, and the parent-owned boundary for support-only CBRN bodies. The existing zombie, ghost, golem, clone, Kruger, Africa, cave, rat, CBRN, and separately gated Aryan clone coverage remains intact.
- `Scenarios!A8:F8` (`SCN-008`, **Every Banner Rises**) was inspected and left unchanged. It is the Independence Wave scenario and currently has eight type options, four intensity paragraphs, and `Unavailable` status.
- `Scenarios!A11:F11` (`SCN-013`, **The Unbidden Muster**) was inspected as the current Event 19 direct scenario. It retains four player-facing type labels, four Low/Medium/High/Maximum intensity stops, the immediate revolt/takeover behavior, and `Playable` status.
- No unrelated rows, sheets, formulas, validations, formatting, filters, or workbook structure were changed. The workbook contains zero formulas, so no formula recalculation was required.

## Export result

After saving the workbook, ran:

```text
python .tools/export_event_catalog_csv.py
```

The exporter completed successfully and refreshed the export-only snapshots. Field-by-field readback matched the workbook for Event 19, `SCN-008`, and `SCN-013`.

- `docs/spreadsheets/chaos_redux_events_catalog.csv`: 183 rows, 14 columns, SHA-256 `d7b258ee882817f38a68d41fef17ffd7c5bb363f2ea6c1e3c7b6c3bca40da4b2`
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`: 14 rows, 7 columns, SHA-256 `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`: 12 rows, 6 columns, SHA-256 `8d31d120dd81adb3ef48bae2afed8cf539bb4f23a60b04771c1eacc57875a398`

## Verified scenario identity

The Part 8 scenario-acceptance specification explicitly approves `SCN-013` as Event 19's direct scenario and records it as the first collision-free identity. The Event 19 README and implementation documentation confirm that proposed `SCN-008` was superseded because Independence Wave owns that occupied identity. `SCN-013`, **The Unbidden Muster**, is therefore the approved live identity with four player-facing types and four Low/Medium/High/Maximum intensity stops. `SCN-008` remains Event 006 / Independence Wave's **Every Banner Rises** scenario with its existing eight type options. The catalog correctly preserves both rows; no scenario identity or catalog blocker remains.
