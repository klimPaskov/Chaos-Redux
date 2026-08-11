# Event 012 Africa final spreadsheet certification handoff

Date: 2026-08-11.

Status: The Event 012 catalog row is certified against the supplied source-complete release facts. The workbook remains the only editable catalog source. The workbook's valid terminal status label is `Playable`; no out-of-list `Available` value was introduced. No live game, MCP visual/probability, or live-save acceptance claim is made.

## Workbook change

- Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
- Changed sheet and row: `Events!13`, event ID `12`, `Africa Is One`.
- Changed cell: `Events!M13` (`Status`), `Partially Available` -> `Playable`.
- `Events!C13` (`Details`), `Events!D13:F13` (evolution mirrors), and `Events!I13` (`World-End Scenario`) were preserved exactly as present before this certification pass.
- The status change reflects the certified source-complete boundary: 44/44 achievements, 102/102 action concepts, 51 host playbooks (22 full and 29 compact), 16 priority packages, 64 AI profiles, 9 models, 18 animations, 4 super-event roles, and the fully classified 239-row visual disposition matrix (84 installed at runtime, 28 installed but dormant, 10 runtime-gated, and 117 controlled-pool rows). Actions 71-76 remain deliberate runtime authorization/readiness gates rather than omissions; HZX/EUX/ELX remain intentional Event006-origin conditional carriers; source-cropped historical portraits remain accepted placeholders and are not an availability blocker.
- The `Clusters!9` Formables row was not changed. Its status remains `Partially Available` because it is a mixed cluster surface rather than an Event012-only status.

## Preservation and validation

- A pre-save/post-save workbook value comparison found exactly one changed cell: `Events!M13`.
- Sheet names, dimensions, tables, data-validation formulas, styles, and workbook structure were preserved. The workbook contains zero formulas, so no recalculation was required.
- The Events status validation list remains `Playable,Partially Available,Unavailable`; `Playable` is therefore the valid source-complete availability label for this workbook.
- No `blocked` or `needs_user_review` cell was added.
- Saved workbook SHA-256: `1ecfcd83d607f5720316cc07ff5abc02ad5999ba4fc34ac7b5ea2edbd6985765`.

## Export results

Ran `python .tools/export_event_catalog_csv.py` from the mod root successfully.

- `docs/spreadsheets/chaos_redux_events_catalog.csv`: 183 rows, 13 columns, SHA-256 `c5c29bc03092fe12d0a44381d59c5865f085c0bc3759240b6d2f151cd21fc6db`.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`: 14 rows, 7 columns, SHA-256 `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`: 12 rows, 6 columns, SHA-256 `66ea4a5802862c1c72f0f3e8ead04cb4f1bfde5e62f88411e3b29f64cb5cf760`.

The exported Event 012 row matches the saved workbook for all 13 columns, including `Playable` status. The cluster and scenario CSVs were refreshed only by the canonical exporter and remain aligned with their workbook sheets.

## Scope boundary

No gameplay, localisation, scripted-localisation, GFX, GUI, asset, source-spec, or CSV file was edited directly. The three CSV files were only overwritten by the canonical exporter after the workbook save. No Git staging or commit was performed.
