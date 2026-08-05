# Event 012 event-catalog workbook handoff

Date: 2026-08-03.

Status: Historical Event 012 catalog row snapshot updated from the accepted non-model source surfaces and regenerated through the repository exporter. No live in-game validation is claimed.

> Superseding implementation note (2026-08-06): The workbook's broad intentional model boundary now applies to the remaining deferred country and unit rows; the shared armoured elephant package has a static `chaosx_elephant` unit/entity consumer through host and Action 102 formation paths. This dated workbook handoff and its hashes remain historical catalog evidence, while the current visual disposition is the 239-row matrix and the current Event 012 overview. No workbook or export file was edited in this documentation reconciliation.

## Workbook changes

- Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
- Sheet and row: `Events!13`, event ID `12`, `Africa Is One`.
- Changed fields: `Details` (`C13`), `Evo II` (`E13`), `Evo III` (`F13`), `World-End Scenario` (`I13`), and `Status` (`M13`).
- `Evo II` and `Evo III` now mirror the current evolution localisation, including `distant courts` and the concise `Africa as a World Pole` body.
- `Details` records the six distinct external-continent packages, their dedicated constitutional surfaces and existing-government installers, W5's frozen-roster gate, political-state gating for Actions 85-92, and The World's terminal presentation contract.
- `World-End Scenario` records the `The World Is One` identity, the `ONE WORLD REMAINS` terminal super-event, the achievement/flag/audio/emblem contract, the frozen-roster political gate, and the intentional model boundary.
- `Status` is `Partially Available`, using the workbook's existing validation list because W5 and terminal political conditions remain gated and no live gameplay validation is claimed.
- `Evo I` (`D13`), event name, type, cluster, severity, and all other rows remain unchanged.

## Export and validation

`python .tools/export_event_catalog_csv.py` completed successfully from the mod root.

- Workbook SHA256: `0064767d2da3271e547719a30c50b0cdee20a30ed9aa804fe87132b94bfea7a2`.
- `docs/spreadsheets/chaos_redux_events_catalog.csv` was refreshed with SHA256 `913121e090439547dcf1d21ad6ed0cab36fcf0964d83f76efc8d7dab37d81976`.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` was refreshed with SHA256 `db80ff3e3bd3387d34292bbaf7d769852cde41302ca1afd7dffd173837ba4c75`.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` was refreshed with SHA256 `1ab7ee1189ba99a8167f2cb98f8e61b698b6adda8b3c648a8b49cc0d67a87708`.
- Exported Event 012 row fields match the workbook for `Details`, `Evo I` through `Evo III`, `World-End Scenario`, and `Status`.
- The `Events` table remains `A1:M1015`, all three workbook data validations remain present, and no formulas were introduced.

## Blockers and review cells

- `Events!M13` remains `Partially Available` because W5 certification and terminal political-state gates are not live-certified in this pass.
- No `needs_user_review` cell was invented, and no gameplay, localisation, source-matrix, or acceptance-ledger file was edited.
