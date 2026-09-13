# Event 26 spreadsheet handoff

Updated authoritative workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

## Workbook changes

- `Events!27` is the sole Event 26 row: `A27=26`, `B27=Black Friday`, `J27=Minor Fire-Once`, `K27=1`, and `M27=Needs Testing`.
- Updated mirror fields `Events!C27` and `Events!D27` to the current localisation values from `localisation/english/026_black_friday_l_english.yml` (`black_friday.event_detail.premise` and `black_friday.evolution.1.body`).
- Cleared `Events!L27` (`Cluster ID`); `E27:I27` remain blank and `World-End Scenario` remains blank.
- Removed the stale Event 26 membership row `Cluster Memberships!37` and updated `Cluster_Memberships` table range from `A1:G77` to `A1:G76`.
- Updated `Clusters!D8:E8` to remove Event 26 and its paired `Medium` severity from Positive Economy.
- No Events row named `Desert question` or no-ID `Black Friday` row remains. The current Events sheet has no separate `Member Severity` column.

## Export and validation

Ran `python .tools/export_event_catalog_csv.py` from the mod root successfully. All three export-only CSV snapshots were regenerated from the workbook and were not edited directly.

- Events: 166 rows × 14 columns, SHA-256 `c38e57e66c5de5b009e7e321d78af955eec310c8d728e63d43958e72c94a783b`.
- Clusters: 20 rows × 7 columns, SHA-256 `6df8ee8871b5896f98e65b736377c49eb98eecfb834774261ba9285c2c184308`.
- Scenarios: 16 rows × 6 columns, SHA-256 `96d076700cd9da866ca13c2da9eaa89ddc738613e80d5986c5680e4856183602`.

Workbook readback confirmed the required sheets, tables, validation collections, and zero formula cells remain present. No live validation was performed; `M27` intentionally remains `Needs Testing`.

Unresolved field mismatch: none. The brief's shorthand Details/Evolution wording differed from the current localisation, so the current localisation was used as the mirror-field source of truth.
