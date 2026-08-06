# Event 006 catalog reconciliation - BOS/IW-029 promotion

Updated the editable catalog workbook at `docs/spreadsheets/chaos_redux_events_catalog.xlsx` after the accepted BOS/IW-029 promotion facts.

Changed workbook sheet and row:

- `Events` row 7, Event ID `6` (`Independence Wave`), `Status` (`M7`): `Unavailable` -> `Partially Available`.

The existing Event 006 event-log/details and evolution wording was retained because it already matches the in-game localisation for the event name, detail, and five evolution stages. The `Clusters` row for Cluster ID 2 (`Liberations`, members `5, 6`) was inspected and already remained `Partially Available`; no cluster cell required a wording or status change. No manual scenario row maps to Event 006.

Accepted source facts represented by this partial status are 22 content-attested selectable packages across 21 reservation groups, 171 unattested rows, and 32 adapters. BOS/IW-029 is source-admitted with explicit YUG former-host proof. Typed AI probability evidence remains unresolved, so the event/package stays HOLD/PARTIAL and this handoff does not claim whole-event completion. The two super-events retain ordinary IDs 23 and 24 in their owning implementation surfaces; no implementation labels were added to player-facing catalog fields.

After saving the workbook, ran `python .tools/export_event_catalog_csv.py` from the mod root successfully.

Export outputs refreshed:

- `docs/spreadsheets/chaos_redux_events_catalog.csv` (Events, 183 rows x 13 columns, SHA-256 `3c8f53de3799af763911ccff72451364340d5406c429f5fe3873181a61c37317`).
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` (Clusters, 14 rows x 7 columns, SHA-256 `db80ff3e3bd3387d34292bbaf7d769852cde41302ca1afd7dffd173837ba4c75`).
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` (Scenarios, 12 rows x 6 columns, SHA-256 `62c360c051d5e172881efe762bc65bddb6548d4bb2b166e6de685ac43c5c3d3f`).

Remaining catalog blocker: typed AI probability evidence is still unresolved; keep Event 006 and its package catalog state at partial/hold until that evidence is accepted.
