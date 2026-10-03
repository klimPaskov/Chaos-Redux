# SCN-019 type and intensity catalog alignment

Status: completed bounded workbook alignment. This handoff does not certify full Event 039.

Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

Changed fields: `Scenarios!D14` (Type Options) and `Scenarios!E14` (Intensity Scaling) for `SCN-019`, Assassin Network. `Scenarios!A14` remains `SCN-019`.

`D14` now contains the exact current player-facing type value returned by the shared `GetTriggerableScenarioTypeName`: `Clandestine network`, from localisation key `chaosx.scenarios.type.assassin_network`. This aligns the catalog with the parent-provided accepted Part11 single-type decision and replaces the stale list `Low, Medium, High, Maximum`.

The four current localisation values below are from `localisation/english/039_murder_mystery_l_english.yml`, keys `chaosx.scenarios.assassin_network.impact.low`, `.medium`, `.high`, and `.maximum`, in that order. They are joined in `E14` with two newline characters, retaining each `§R` and `§!` marker.

```text
§RStarts Assassin Network immediately.§! Low intensity opens a Murder Cult investigation with low reach and a small foreign network. No Assassin State exists at launch.

§RStarts Assassin Network immediately.§! Medium intensity opens a mature international network and a stronger investigation. The host can still prevent the Assassin State split.

§RStarts Assassin Network immediately.§! High intensity opens the Assassin State war and a strong foreign network through the normal country transaction.

§RStarts Assassin Network immediately.§! Maximum intensity opens Evolution IV, the Assassin State war, and foreign derivative operations. World of Anarchy still requires its normal terminal conditions.
```

The original immutable pre-edit workbook copy remains `docs/plans/039_murder_mystery_plans/validation/scenario_registration/catalog.before_intensity.xlsx`, SHA-256 `f2b80a942afa04d97d20904e60cfaafaee16bd9f47959048806c7076830b31d2`. It was not recreated or overwritten and serves as the comparison baseline allowing only `Scenarios!D14` and `Scenarios!E14` to differ.

The existing `scenario_catalog_019.md` handoff and `validation/scenario_registration/catalog.before.xlsx` provenance copy were left unchanged.

After saving the workbook, `python .tools/export_event_catalog_csv.py` completed successfully. It refreshed `docs/spreadsheets/chaos_redux_events_catalog.csv` (SHA-256 `50b4c49e87d6879cd4affcc6cbfb728b5d5ba99780f65556c04ce8d8d858a1ed`), `docs/spreadsheets/chaos_redux_clusters_catalog.csv` (SHA-256 `276964d65cad082f678c7bbfff4d8e89d99930b1f3707b1d8dd07ba1e3755d8a`), and `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` (SHA-256 `cdc1c288a885d6b62225d7d84ed6af560f4267322d74a7a4cf4b28a7d16b124d`). The exported SCN-019 type and intensity values match `D14` and `E14` exactly.

Comparison against the immutable beforecopy confirmed that only the values in `Scenarios!D14` and `Scenarios!E14` differ. Both cells retain their original styles; all other cell values, formulas, styles, sheet structures, and workbook structures are unchanged, including `A14` remaining `SCN-019`. The standard XLSX modified timestamp advanced during the save; no other OOXML content part changed beyond the Scenarios sheet XML for these two cells and `docProps/core.xml` for that timestamp.

Blocked or needs-user-review cells: none in this bounded update. No gameplay or localisation source was edited. No Git staging or commit was performed.
