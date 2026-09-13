# Event 021 spreadsheet alignment handoff

Date: 2026-09-02.

## Changed files

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` was saved in place as the authoritative catalog source.
- `docs/spreadsheets/chaos_redux_events_catalog.csv` was refreshed by the required exporter.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` was refreshed by the required exporter.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` was refreshed by the required exporter.
- This handoff was added at `docs/plans/021_random_civil_war_plans/subagent_handoffs/spreadsheet_alignment_2026-09-02.md`.

No semantic value delta was required in the targeted cells because the current workbook already contained the requested Event 021 alignment. The authoritative workbook was reopened after the save, and no unrelated event rows were changed.

## Event 021 workbook row

Workbook sheet: `Events`, row 22, catalog ID 21.

- `A22`: `21`.
- `B22`: `Random Civil War`.
- `C22` exact value:

  ```text
  A country's chain of command has split between rival political and military authorities. Capitals, supply routes, public legitimacy, and the terms offered to each front will shape the conflict.

  Settlement

  The sides have accepted terms based on recognition, autonomy, coalition, partition, or disarmament. The peace will last only if every signatory meets its obligations.

  Reconstruction

  The fighting has ended. Repaired railways, restored civil administration, demobilization, and fulfilled peace terms will determine whether the settlement lasts.
  ```
- `D22`: `Additional commands and regional movements have entered the first war. Several rival authorities are now competing for capitals, supply routes, and terms of peace.`
- `E22`: `Arms routes, sponsors, and displaced administrations are carrying the crisis across borders. Civilian relief and armed support now demand separate choices.`
- `F22`: `Countries are moving from stability into exposure, fracture, and open crisis as divided commands and regional movements test weakened governments. Victory, reform, and negotiated terms can still restore public authority.`
- `G22:I22`: blank, with no Event 021 world-end scenario claimed.
- `J22`: `Minor Repeatable`.
- `K22`: `1`.
- `L22`: `1`, for Cluster 1.
- `M22`: `Needs Testing`.

The source documentation confirms the root identity `chaosx.nr21.1` and the closed `random_civil_war_rework_ready` release gate. The workbook Events table has no root-id or separate release/acceptance-gate column, so `Needs Testing` records the rework as ready for testing while the separate runtime release gate remains closed.

## Wars cluster and severity

Workbook sheet: `Clusters`, row 2, Cluster ID 1.

- `B2`: `Wars`.
- `C2`: `Sudden wars and armed conflicts break out between countries, turning local disputes, opportunistic attacks, internal fractures, and alliance betrayals into wider fighting.`
- `D2` includes Event 021 at the seventh member position.
- `E2` contains the aligned seventh severity `Medium`.

Workbook sheet: `Cluster Memberships`, row 8.

- `A8:B8`: `1`, `Wars`.
- `C8`: slot `7`.
- `D8:E8`: `21`, `Random Civil War`.
- `F8`: `Medium`.
- `G8`: blank.

## Export evidence

The exact required command `python .tools/export_event_catalog_csv.py` completed successfully.

- Events export: 166 rows including the header, 14 exported columns, SHA-256 `2094ed00142065b75ac53c9e30cae46848e5416613a4e796b24dd8d13a6f445a`.
- Clusters export: 20 rows including the header, 7 exported columns, SHA-256 `6df8ee8871b5896f98e65b736377c49eb98eecfb834774261ba9285c2c184308`.
- Scenarios export: 16 rows including the header, 6 exported columns, SHA-256 `96d076700cd9da866ca13c2da9eaa89ddc738613e80d5986c5680e4856183602`.

The refreshed Events CSV row for ID 21 matches the workbook row, including `Random Civil War`, the current detail and evolution wording, `Minor Repeatable`, chaos level `1`, Cluster ID `1`, and `Needs Testing`. The refreshed Clusters CSV row for Cluster 1 includes Event 021 and its aligned `Medium` member severity. The refreshed Scenarios CSV retains `SCN-018`, `The Fracture Cascade`, with status `Needs Testing`.

## Unresolved schema limitation

The current Events table is `A1:M1014` with 13 visible columns and no separate member-severity or release-gate field, while the repository exporter is configured for 14 Event columns. The final exported Event CSV therefore retains one trailing blank column. This was preserved because the task forbids changing the workbook schema.

The current Clusters table is `A1:H20`, but the repository exporter is configured for seven Cluster columns, so the exported Clusters CSV omits the workbook's `Status` column. This existing exporter/schema mismatch was also preserved.

No gameplay or localisation files were edited, and no commit was created.
