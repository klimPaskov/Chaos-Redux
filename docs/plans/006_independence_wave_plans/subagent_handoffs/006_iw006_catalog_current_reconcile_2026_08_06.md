# Event 006 catalog current-authority reconciliation — 2026-08-06

Scope: read-only reconciliation of the editable Event 006 catalog workbook against the current 23-package source authority. No workbook, CSV, gameplay, or localisation file was changed because the workbook already matches the current catalog override.

## Workbook cells checked

| Sheet and range | Current row | Reconciliation result |
| --- | --- | --- |
| `Events!A7:M7` | Event ID `6`, `Independence Wave` | Status `M7 = Partially Available`; event name, detail, and five evolution mirrors match current player-facing localisation. |
| `Clusters!A3:G3` | Cluster ID `2`, `Liberations`, members `5, 6` | Status `G3 = Partially Available`; cluster name, detail, and member list match the current Liberations cluster surface. |
| `Scenarios!A8:F8` | `SCN-008`, `Every Banner Rises` | Status `F8 = Unavailable`; scenario name, detail, type options, and intensity wording match current scenario localisation. |

## Current authority cross-check

- Event 006 remains **HOLD / PARTIAL** with 23 content-attested selectable packages across 22 compatible reservation groups and 170 unattested selectable rows out of 193 non-overlay rows. These counts are source/readiness evidence and have no dedicated player-facing workbook field.
- Ordinary super-event identifiers remain `23` for The League of New States and `24` for Every Border a Casus Belli. These implementation identifiers are not inserted into the catalog wording fields.
- The mixed Liberations cluster remains `Partially Available`; SCN-008 remains `Unavailable`.
- No stale or contradictory workbook cell was found. Wording fields were intentionally not paraphrased or expanded with implementation counts/IDs.

## Export and commit disposition

Because the workbook source required no mutation, `python .tools/export_event_catalog_csv.py` was not run and the export-only CSV snapshots were not touched. No commit was created for this no-op reconciliation.

## Remaining blockers

Event 006 remains incomplete: package admission beyond the current attested boundary, source/asset and rights proof, AI/balance evidence, FORM-07/FORM-16 and other formable gates, ordinary super-event `23` audio/wrappers/firing, and factual reachability of ordinary super-event `24` remain open. SCN-008 therefore stays unavailable in the catalog.
