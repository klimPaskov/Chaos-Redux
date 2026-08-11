# Event 012 Africa final spreadsheet update handoff

Date: 2026-08-10.

Status: The Event 012 catalog row now reflects the current source/runtime release-candidate facts and current gated availability. The workbook remains the only editable catalog source. No live game or live-save validation is claimed.

## Workbook changes

- Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
- Changed sheet and row: `Events!13`, event ID `12`, `Africa Is One`.
- Changed cells: `Events!C13` (`Details`) and `Events!I13` (`World-End Scenario`).
- `Events!C13` now records all 102 parameterized actions on the shared contract, the 22 full and 29 compact host playbooks, 16 priority-member packages, six promoted Tier A packages, the RSA Allied civil-war route, nine installed 3D model packages, 18 full frame-animation packages, all 239 visual disposition rows and their current disposition split, four super-event roles, 44 achievement records, 64 AI profile records, the six external-continent packages with existing-government installers, The World terminal seal and presentation contract, and the remaining political, owner-proof, AI-scenario, playback, and live-save gates.
- `Events!I13` now keeps the exact terminal Event Log branch titles `The World: Unanimous Continental Union`, `The World: Last Standing Resolution`, and `The World: Continental Campaign`, plus `ONE WORLD REMAINS`; it records the installed model/animation and terminal presentation surfaces, distinguishes the six existing-carrier package routes from The World's separate terminal seal, and distinguishes source-present W5 certification from still-gated package installation, terminal political checks, playback review, and live end-state acceptance.
- `Events!D13:F13` (`Regional Consolidation`, `Continental Machinery`, `Africa as a World Pole`) were verified unchanged against `localisation/english/012_africa_evolutions_l_english.yml`.
- `Clusters!9` (cluster ID `6`, `Formables`) was verified unchanged against `chaosx.events_log.window.cluster_details.description.formables`; its member list remains `12`, type remains `Minor Repeatable`, chaos level remains `3`, and status remains `Partially Available`.
- `Events!M13` remains `Partially Available`; no `blocked` or `needs_user_review` cell was invented. This retains the workbook validation vocabulary and does not imply live gameplay acceptance.

## Preservation and validation

- A workbook value comparison against `HEAD` found exactly two changed cells: `Events!C13` and `Events!I13`.
- Sheet names, dimensions, tables, data validations, and merged-cell structure were preserved. The workbook has zero formulas.
- The saved workbook SHA-256 is `bcf1a2d799c762b65b7937278963f94d7750fcb4b8d13d965f1f87263483000b`.

## Export results

Ran `python .tools/export_event_catalog_csv.py` from the mod root successfully.

- `docs/spreadsheets/chaos_redux_events_catalog.csv`: 183 rows, 13 columns, SHA-256 `cfcdbb337b1c137d09d7dd1e6f8cdfeb595bd20011d8a1a2569e1c3163bcda20`.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`: 14 rows, 7 columns, SHA-256 `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`: 12 rows, 6 columns, SHA-256 `66ea4a5802862c1c72f0f3e8ead04cb4f1bfde5e62f88411e3b29f64cb5cf760`.

The exported Event 012 row matches the workbook for all populated fields, including the updated Details, evolution mirrors, World-End Scenario, and Partially Available status. The exported Formables row remains aligned with the workbook and current cluster localisation.

## Scope boundary

No gameplay, localisation, scripted-localisation, GFX, GUI, asset, source-spec, or CSV file was edited directly. The three CSV files were only overwritten by the canonical exporter after the workbook save.
