# Event 012 catalog merge handoff

Date: 2026-08-02.

Status: Event 012 workbook fields and export snapshots are clean and reconciled. The catalog remains a status record and does not prove gameplay completion. No workbook or CSV edit was made by this documentation reconciliation.

## Scope

The accepted Event 012 catalog values are present in the current `docs/spreadsheets/chaos_redux_events_catalog.xlsx` without replacing the workbook or rewriting unrelated Event 006, Event 016, or Event 020 work.

The target values were already present, so no workbook cell write or CSV content change was needed in this pass. The required exporter completed successfully, and the current workbook and export hashes are recorded below.

## Event 012 fields

- `Events!I13` (`World-End Scenario`): `The World Is One`, followed by the uncertified baseline and the gates for external packages, rivals, W5 pre-install receipts, terminal super-event/audio, unique models, and native-language review.
- `Events!M13` (`Status`): `Needs Testing`.
- `Events!C13` (`Details`) and `Events!D13:F13` (`Evo I` through `Evo III`) remain unchanged and match current Event 012 localisation.
- No `Clusters` or `Scenarios` rows were added or changed in this pass.

## Validation

- Current workbook SHA256: `4b6489d5582ed8be32e10db1d842b2449c49025e06544d386a6d42f1f72c9481`.
- Workbook sheets remain `Events`, `Clusters`, `Scenarios`, `Info`, and `Legend`.
- The Events table remains `A1:M1015`.
- Event 012 row identity is ID `12`, name `Africa Is One`, cluster `6`, Severe member severity, and Minor Fire-Once type.
- `Events!M13` remains `Needs Testing`.
- `Events!I13` retains the accepted gated World-End wording for `The World Is One`, including its uncertified baseline and external-package, rival, W5 pre-install receipt, terminal presentation/audio, unique-model, and native-language gates.
- The Event 012 row in the exported Events CSV matches the workbook target fields.
- `git status -- docs/spreadsheets` is clean.
- No workbook or CSV file was edited by this documentation pass, and no unrelated catalog work was rewritten.

## Export results

`python -B .tools/export_event_catalog_csv.py` completed successfully.

- `docs/spreadsheets/chaos_redux_events_catalog.csv`: SHA256 `1af83ae91ddc71131b7791c01c3522c02101ea7e2a5e870cffe0af435a1aaf10`.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`: SHA256 `468115701405df265dba77959d64ed38aa72a61645b1a736bacd889161217c0`.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`: SHA256 `56be4ed04687f84b47746c6e4a9dd0adec7859d787f80d2ee4cfdf406249252f`.

## Remaining boundary

The clean catalog/export pair records the accepted terminal route wording and `Needs Testing` status without claiming full Event 012 completion. W5 certification, terminal presentation and audio, unique models, native-language review, and live gameplay acceptance remain gated as stated in `Events!I13`.
