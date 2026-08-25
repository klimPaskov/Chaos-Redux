# Current Spreadsheet Alignment Handoff

## Audit scope

This is a read-only audit of the authoritative workbook at `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and its three export-only CSV snapshots.

The workbook was not saved or modified, and no CSV or gameplay file was edited.

The shared worktree already showed unrelated uncommitted changes in the workbook, the Events CSV, and the Scenarios CSV when this audit ran; this audit did not touch those files.

## ID 149 evidence

The `Events` sheet contains exactly one row with `ID = 149`, at Excel row 150 and logical CSV row 150.

The row fields are `Event Name = Immigrations`, `Details = Retired and absorbed into the separate famine and migration mechanics through explicit adapters. Unavailable as a random event.`, and `Status = Unavailable`.

The `Evo I`, `Evo II`, `Evo III`, `Evo IV`, `Evo V`, `World-End Scenario`, `Type`, `Chaos level`, `Cluster ID`, and `Member Severity` cells on ID 149 are blank.

This exactly records retirement into the separate famine and migration mechanics through explicit adapters and unavailability as a random event.

## Absence checks

The compound famine/migration search found only the ID 149 retirement row in `Events` and no matching row in `Clusters` or `Scenarios`.

There are zero rows containing a famine/migration incident combination, zero rows containing a replacement-ID or replacement-event marker, and zero famine/migration-related pool, cluster, scenario, or pacing rows.

The workbook has unrelated pre-existing textual references in Event 5 (`famine pressure`), Event 15 (`Migration` in an evolution detail), and Event 118 (`famine` in the unavailable description); none is a famine/migration system incident, replacement, pool, cluster, scenario, or pacing row.

The only pacing-like search hit outside the target wording is unrelated Event 151's `cooldown` text in the Teleportation Experiment row.

## XLSX and CSV evidence

The exporter-equivalent logical row counts, including each header row, are `Events = 177`, `Clusters = 14`, and `Scenarios = 12`.

The current snapshots reserialize from the workbook byte-for-byte with the repository exporter contract, including the UTF-8 BOM and newline handling.

| Sheet | CSV | Bytes | SHA-256 | XLSX-equivalent match |
| --- | --- | ---: | --- | --- |
| Events | `docs/spreadsheets/chaos_redux_events_catalog.csv` | 51240 | `1985a8fed50110098262e4268ccd99fe9c4e676e87666ba56944790446e7fbcb` | Yes |
| Clusters | `docs/spreadsheets/chaos_redux_clusters_catalog.csv` | 2622 | `647c9206de61a70d7a0d7adf0740dc97c81c8e63d01fefac6549b430b666425b` | Yes |
| Scenarios | `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` | 10754 | `c6231be89377eb4e5fdf35966b8493d8400b22fc8e082ac97e6ef9639e653e44` | Yes |

The exporter was not invoked because this was a read-only audit and no successful workbook save occurred; the existing snapshots were verified directly against the exporter serialization logic.

## Formula and structure check

The workbook contains zero formula cells, zero missing formula caches, and zero cached cells with Excel error values, so there is no formula-error status to resolve.

The workbook structure remains intact with the `Events`, `Clusters`, `Scenarios`, and `Legend` sheets and the existing `Events`, `Event_Clusters`, and `Manual_Scenarios` tables.

## Verdict

PASS: The authoritative workbook is aligned with the famine and migration retirement requirement, ID 149 is explicitly retired and unavailable as a random event, no replacement incident or catalog rows were added, and all three CSV snapshots match the workbook exactly.

No blocked or `needs_user_review` cells were identified by this audit.
