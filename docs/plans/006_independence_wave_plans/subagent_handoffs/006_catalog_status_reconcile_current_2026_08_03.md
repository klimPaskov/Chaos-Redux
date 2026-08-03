# Event 006 catalog status reconciliation — 2026-08-03

Updated only the editable event catalog workbook and regenerated its export snapshots. Player-facing Event 006, Liberations, and SCN-008 wording was left unchanged because the current localisation/catalog audit already found exact mirror agreement.

## Status cells

| Sheet | Cell | Key/row | Before | After | Reason |
| --- | --- | --- | --- | --- | --- |
| Events | `M7` | Event ID `6`, Independence Wave | `Partially Available` | `Unavailable` | The accepted completion authority keeps Event 006 incomplete / `To Be Reworked` until implementation is complete. The workbook validation vocabulary has no `To Be Reworked`, so `Unavailable` is the conservative fail-closed mapping. |
| Clusters | `G3` | Cluster ID `2`, Liberations | `Partially Available` | `Partially Available` (retained) | The cluster contains Event 5 (Playable) and Event 6 (Unavailable); the existing mixed-member cluster state remains the conservative catalog value. |
| Scenarios | `F9` | `SCN-008`, Every Banner Rises | `Playable` | `Unavailable` | Current static capacity is fail-closed below the admitted package set for the 14/20 bands, and the accepted scenario authority remains needs-testing/incomplete. `Unavailable` is the workbook's conservative status value. |

## Wording boundary

The following player-facing mirror fields were reviewed and not changed: Event 006 name/details/evolution columns, Liberations cluster name/details/member list, and SCN-008 name/details/type options/intensity scaling. The current source/localisation audit reports exact agreement for these fields.

## Validation and exports

- Workbook saved in place at `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
- A baseline comparison against `HEAD` found only the two intended value changes (`Events!M7`, `Scenarios!F9`); no unowned value or style changes were found.
- Existing tables and data-validation lists were preserved, including the status list `Playable,Partially Available,Unavailable`.
- Ran `python .tools/export_event_catalog_csv.py` from the mod root successfully.
- Exported snapshots refreshed: `docs/spreadsheets/chaos_redux_events_catalog.csv` (183 rows, SHA-256 `528e3602819710ff7a8cc1bee34e72555f424c5b378670a826a528e7512c09a3`), `docs/spreadsheets/chaos_redux_clusters_catalog.csv` (14 rows, SHA-256 `db80ff3e3bd3387d34292bbaf7d769852cde41302ca1afd7dffd173837ba4c75`), and `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` (13 rows, SHA-256 `8ce3abae76f7de3017c8fdeb8c5f8f07a48def274c2aa676851a71f8e129e88c`).

## Remaining blocker

The workbook schema cannot express the authority's literal `To Be Reworked`, `In progress`, or `Needs Testing` labels. This handoff uses the existing conservative `Unavailable` value for Event 006 and SCN-008 without changing the validation schema or gameplay/localisation files.
