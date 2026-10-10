# Event 037 catalog and cluster alignment

## Current workbook row

Read from the export `docs/spreadsheets/chaos_redux_events_catalog.csv` on 2026-10-10.

| Field | Current value |
| --- | --- |
| ID | `37` |
| Event Name | Mysterious People |
| Details | A major country receives millions of unexplained new recruits. |
| Evo I to Evo V | empty |
| Type | Minor Repeatable |
| Chaos level | `1` |
| Cluster ID | `15` (Sudden Abundance) |
| Status | To Be Reworked |

The Details premise describes the legacy stub.
The design in this package replaces it with a global civilian population event (see the README's open questions for the acceptance of that replacement).

## Replacement after implementation

| Field | Direction |
| --- | --- |
| Details | People with homes, families, and histories appear in every inhabited state. Repeated manifestations can turn the gift into overcrowding, hunger, and flight. |
| Evo I | Population Surge at `200+` Chaos: larger manifestations that make housing and roads necessary. |
| Evo II | Overpopulation Crisis at `400+` Chaos: crowded states start to go hungry. |
| Evo III | Humanity Multiplies at `600+` Chaos: manifestations large enough to break countries, and governments that count origins. |
| Status after implementation | Needs Testing |

The final Details and Evo fields copy the implemented Event Details and evolution localisation word for word.
Type, Chaos level, and Cluster ID stay as they are.

## Workbook procedure

Edit only `docs/spreadsheets/chaos_redux_events_catalog.xlsx` through `chaosx_spreadsheet_doc_worker` and the `chaos-redux-xlsx` skill, then run `python .tools/export_event_catalog_csv.py` from the mod root.
Never edit the CSV exports.

## Cluster

The workbook and `docs/systems/event_system/event_clusters.md` list Event 037 as member 4 of Sudden Abundance (cluster `15`, Minor Repeatable, Chaos level `1`) at Medium severity.
Sudden Abundance is not registered in `common/script_constants/event_cluster_constants.txt`, so it cannot fire yet.

Event 037 is not a member of Various Anomalies, which is live at cluster ID `11` with Events 42 and 47.

Until Sudden Abundance is registered, Event 037 fires only through its ordinary Minor Repeatable path.
Registering the cluster belongs to the shared cluster work, not to Event 037.
When it is registered, one activation calls Event 037 once with one world transaction, one history entry, one repeatable-weight update, and one set of milestone checks.
