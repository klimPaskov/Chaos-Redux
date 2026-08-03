# Event 006 catalog/export post-documentation reconciliation — 2026-08-03

Read-only follow-up after the current Event 006 documentation commits. No workbook, CSV, gameplay, localisation, or scripted-localisation files were edited in this check.

## Current source and authority

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` remains the editable catalog source of truth.
- The current resume packet records Event 006 as incomplete and explicitly records the catalog/export disposition from commit `162a25655`: Event 006 `Unavailable`, SCN-008 `Unavailable`, and the mixed Liberations cluster `Partially Available`.
- Current whole-event authority remains `HOLD / PARTIAL` with 14 of 193 non-overlay packages attested and 14/20 capacity fail-closed. The current documentation reconciliation explicitly excludes obsolete pasted flag-log material; no such evidence was used here.

## Workbook rows verified

| Sheet | Cell | Key | Current status |
| --- | --- | --- | --- |
| Events | `M7` | Event ID `6`, Independence Wave | `Unavailable` |
| Clusters | `G3` | Cluster ID `2`, Liberations | `Partially Available` |
| Scenarios | `F9` | `SCN-008`, Every Banner Rises | `Unavailable` |

Event 006 and SCN-008 therefore remain in the accepted conservative incomplete/unavailable state. Liberations remains partially available because its member set mixes Event 5's playable surface with Event 6's unavailable surface.

## Workbook/export mirror check

The workbook and all three export-only CSVs were parsed and compared row-for-row:

- Events: 183 workbook rows / 183 CSV rows; exact match.
- Clusters: 14 workbook rows / 14 CSV rows; exact match.
- Scenarios: 13 workbook rows / 13 CSV rows; exact match.

Current CSV SHA-256 values are unchanged from the prior export receipt:

- Events `528e3602819710ff7a8cc1bee34e72555f424c5b378670a826a528e7512c09a3`
- Clusters `db80ff3e3bd3387d34292bbaf7d769852cde41302ca1afd7dffd173837ba4c75`
- Scenarios `8ce3abae76f7de3017c8fdeb8c5f8f07a48def274c2aa676851a71f8e129e88c`

Existing workbook tables and status data-validation lists remain present. No export rerun was needed because the workbook was not saved or modified during this read-only check.
