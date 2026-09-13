# Event 35 spreadsheet synchronization handoff

Date: 2026-09-01

The first worker read below records a transient malformed-archive result. The parent follow-up at the end is the authoritative state after the workbook was stabilized and the exporter was rerun.

## Initial worker result

No workbook cells were changed. The readable Event 35 catalog values already match the current implementation and player-facing localisation, but the XLSX on disk is a malformed partial archive and cannot be safely opened or saved without risking unrelated dirty-worktree changes.

## Workbook verification

Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

- `Events!A36:M36` is the row for Event ID `35`.
- `Events!B36` is `Great Depression 2.0`, matching `chaosx.event_name.35` and `chaosx.nr35.1.t`.
- `Events!C36` matches `chaosx.events_log.window.event_details.great_depression` exactly.
- `Events!D36:F36` match `great_depression.evolution.1.body`, `.2.body`, and `.3.body` exactly.
- `Events!J36` is `Minor Repeatable`.
- `Events!K36` is `1`.
- `Events!L36` is cluster ID `10`.
- `Events!M36` remains `Needs Testing`; it was not upgraded to `Playable` because engine evidence is partial.
- `Clusters!A11:H11` is cluster ID `10`, `Negative Economy`; its detail matches `chaosx.events_log.window.cluster_details.description.negative_economy` exactly.
- `Cluster Memberships!A58:G58` is slot `1` for Event ID `35`, named `Great Depression 2.0`, with severity `Low`.
- The aligned cluster aggregate remains `Clusters!D11:E11 = 35, 50 / Low, Medium`.

## Export result and blocker

Running `python .tools/export_event_catalog_csv.py` from the mod root failed with exit code `1`:

`CSV export failed: "There is no item named '[Content_Types].xml' in the archive"`

The three export-only CSV hashes were unchanged by the failed export, so no CSV was manually edited or refreshed:

- `docs/spreadsheets/chaos_redux_events_catalog.csv`
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`

Read-only parsing of the unchanged snapshots found one Event ID `35` row and one Cluster ID `10` row, with the same Event 35 text/classification and `Negative Economy` aggregate (`35, 50` / `Low, Medium`) as the worksheet XML.

The current XLSX archive contains only worksheet XML for `Events`, `Clusters`, and `Cluster Memberships` plus their related files. It is missing `[Content_Types].xml`, workbook relationships/workbook metadata, and the `Scenarios` and `Legend` sheets required by the existing workbook structure. Raw inspection found no formula cells or Excel error literals in the available three worksheet XMLs; full-workbook formula/error verification is blocked by the malformed archive.

No gameplay, localisation, implementation, or unrelated worktree files were modified by this worker. The next spreadsheet worker should repair or provide a valid authoritative XLSX from the concurrent workbook owner, then rerun the exporter and verify all three CSV snapshots.

## Parent follow-up: stabilized workbook and export

After the worker's read, the concurrent workbook write completed and the archive was re-read successfully without changing Event 35 cells. The current workbook is a readable five-sheet package containing `Events`, `Clusters`, `Cluster Memberships`, `Scenarios`, and `Legend`; the Event 35 row and cluster membership remain the values recorded above.

The parent then reran `python .tools/export_event_catalog_csv.py` from the mod root successfully. The refreshed export hashes are:

- `docs/spreadsheets/chaos_redux_events_catalog.csv`: `150f76a1c348a46d814cc47da25b2e35dc4fac07fecb24224f056e479cc66945`
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`: `71cb8568b796b953793a026d325f77572eb25d35fbe0070523b1307b678499ae`
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`: `96d076700cd9da866ca13c2da9eaa89ddc738613e80d5986c5680e4856183602`

The initial malformed-archive/export failure remains a real transaction in this handoff; the final workbook/export state is valid, and no direct CSV edit was used.

## Latest parent recheck: 2026-09-04

The five-sheet workbook still contains the required Event 35 row, cluster 10 row, and Event 35 membership row. The exporter was run again from the workbook and completed successfully.

- Workbook SHA-256: `a6e87c892fa7a2c3a3c62dd86fd6daa166a5011d703acaff1171f3dc3e39d3e5`
- Events CSV SHA-256: `2094ed00142065b75ac53c9e30cae46848e5416613a4e796b24dd8d13a6f445a`
- Clusters CSV SHA-256: `6df8ee8871b5896f98e65b736377c49eb98eecfb834774261ba9285c2c184308`
- Scenarios CSV SHA-256: `96d076700cd9da866ca13c2da9eaa89ddc738613e80d5986c5680e4856183602`
