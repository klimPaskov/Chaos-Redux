# Event 23 Catalog Alignment Handoff

Updated the authoritative workbook at `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, sheet `Events`, for Event ID 23 on Excel row 24.

Changed cells: `E24` (`Evo II`) now matches `sov_nuclear_bombs.evolution.ii.body`; `F24` (`Evo III`) now matches `sov_nuclear_bombs.evolution.iii.body` in `localisation/english/023_soviet_nukes_l_english.yml` exactly.

The other requested cells already matched their localisation values and were not changed: `C24` (`Details`), `D24` (`Evo I`), and `G24` (`Evo IV`). Event name, ID, type, Chaos level, and `To Be Reworked` status remain unchanged. `Evo V`, `World-End Scenario`, and `Cluster ID` remain blank; no cluster membership or scenario row was added.

The workbook was inspected before and after the edit. The only cell-value differences were `Events!E24` and `Events!F24`; sheet order, tables and table styling, data validations, filters, freeze panes, merged ranges, and cell styles were preserved. No formulas were present. The workbook was already dirty before this task; its pre-existing state outside those two cells was retained unchanged.

Ran `python .tools/export_event_catalog_csv.py` from the mod root after saving. It returned `status: success`: Events exported 166 rows x 13 columns (SHA-256 `b46f24c84ab1dffdcf1b49c5e06401a3968cfc6cb556a67a17d618b81025e855`), Clusters 20 x 8 (`689fe07883da14abe2ceb7c29c151db50808cf97a366e60808281b16e37c76a2`), and Scenarios 16 x 6 (`8b944de19817b3887eac22e3d12437e62990273c8b0db1c6f27928f349d4b2e7`). The exported Events CSV row for ID 23 was checked against the workbook for all five requested fields and the preserved values/blanks.

No live-game or spreadsheet-application consumer validation was performed. No gameplay, localisation, asset, or unrelated workbook edits were made by this worker.
