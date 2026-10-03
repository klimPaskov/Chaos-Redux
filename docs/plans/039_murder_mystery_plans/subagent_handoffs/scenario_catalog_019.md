# Scenario Catalog ID 019 Handoff

The Chaos Redux event catalog workbook now reserves `SCN-019` for Assassin Network, confirming the catalog reservation before runtime code uses scenario identity 19.

Changed workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, sheet `Scenarios`, row 14, column A (`Scenario ID`), cell `A14`; event/scenario label: `Assassin Network`.

Cell change: `SCN-014` → `SCN-019`.

Workbook SHA-256 before edit: `42746e24fa814e60daff94f4fee669c85a51e3c2f2c7ad59603cb16004c2f0a0`.

Immutable before-copy: `docs/plans/039_murder_mystery_plans/validation/scenario_registration/catalog.before.xlsx`, SHA-256 `42746e24fa814e60daff94f4fee669c85a51e3c2f2c7ad59603cb16004c2f0a0`.

Saved workbook SHA-256: `f2b80a942afa04d97d20904e60cfaafaee16bd9f47959048806c7076830b31d2`.

Post-save comparison passed: all cell values and styles match the before-copy except the authorized value at `Scenarios!A14`; all five worksheets, workbook style table, tables, validations, conditional formatting, filters, freeze panes, dimensions, and other captured worksheet structures matched. Formula count remains zero.

Ran `python .tools/export_event_catalog_csv.py` from the mod root immediately after the workbook replacement; it returned `status: success`.

| Export | Rows × columns | SHA-256 |
| --- | ---: | --- |
| `docs/spreadsheets/chaos_redux_events_catalog.csv` | 166 × 13 | `50b4c49e87d6879cd4affcc6cbfb728b5d5ba99780f65556c04ce8d8d858a1ed` |
| `docs/spreadsheets/chaos_redux_clusters_catalog.csv` | 20 × 8 | `276964d65cad082f678c7bbfff4d8e89d99930b1f3707b1d8dd07ba1e3755d8a` |
| `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` | 17 × 6 | `48761515f8600b3d1f836bccd9163b79bcccbe9f230bbf53d18f01df0514cbfc` |

The exported `Assassin Network` row contains `Scenario ID = SCN-019`; its name, details, type options, intensity scaling, and status remain unchanged.

No Git staging or commit commands were run. The pre-existing staged/unstaged catalog state was left in place, with the three working-tree CSV snapshots regenerated from the workbook as requested. No gameplay or localisation files were changed.
