# Event 012 catalog merge handoff

Date: 2026-08-02.

Status: Event 012 workbook fields confirmed in the current dirty workbook; export snapshots refreshed. No commit was created.

## Scope

The accepted Event 012 catalog values were checked against the current `docs/spreadsheets/chaos_redux_events_catalog.xlsx` without replacing the workbook or rewriting unrelated Event 006, Event 016, or Event 020 work.

The target values were already present, so no workbook cell write or CSV content change was needed in this pass. The required exporter was rerun and returned the same snapshot hashes.

## Event 012 fields

- `Events!I13` (`World-End Scenario`): `The World Is One`, followed by the uncertified baseline and the gates for external packages, rivals, W5 pre-install receipts, terminal super-event/audio, unique models, and native-language review.
- `Events!M13` (`Status`): `Needs Testing`.
- `Events!C13` (`Details`) and `Events!D13:F13` (`Evo I` through `Evo III`) remain unchanged and match current Event 012 localisation.
- No `Clusters` or `Scenarios` rows were added or changed in this pass.

## Validation

- Current workbook SHA256 before and after export: `bf8e0d8ead8f043cfabebd9fc2d07639a6739be4d0ba7904ad406e768fae1424`.
- Workbook sheets remain `Events`, `Clusters`, `Scenarios`, `Info`, and `Legend`.
- The Events table remains `A1:M1015`.
- Event 012 row identity remains ID `12`, name `Africa Is One`, cluster `6`, Severe member severity, and Minor Fire-Once type.
- The Event 012 row in the exported Events CSV matches the workbook target fields.
- No workbook save occurred because both accepted target cells were already merged. This preserved all unrelated dirty workbook changes.
- No temporary workbook or lock file was left behind. A pre-existing 165-byte lock dated 2026-07-31 was verified stale with no Excel process running and removed.

## Export results

`python .tools/export_event_catalog_csv.py` completed successfully.

- `docs/spreadsheets/chaos_redux_events_catalog.csv`: SHA256 `7b59f52ea145f257f7015ea02e691998ad1dda3d4641c3082c27fcc077568c86`.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`: SHA256 `468115701405df265dba77959d64edc38aa72a61645b1a736bacd889161217c0`.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`: SHA256 `659ccd2aefae3db6156725395093d654614032d17ea0398ae1f74057ca1c68c6`.

## Remaining boundary

The catalog records the terminal route and status without claiming full Event 012 completion. W5 certification, terminal presentation and audio, unique models, and native-language review remain gated as stated in `Events!I13`.
