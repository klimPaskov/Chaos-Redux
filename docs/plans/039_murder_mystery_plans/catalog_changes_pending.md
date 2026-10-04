# Event 039 catalog changes pending

The event catalog workbook (`docs/spreadsheets/chaos_redux_events_catalog.xlsx`) is the only editable catalog source, and this workstream may not edit it or its exported CSVs.
The changes below record where the workbook no longer matches the runtime, so the catalog owner can apply them and rerun `python .tools/export_event_catalog_csv.py`.

## Clusters sheet: Intelligence cluster ID

Disposition: accepted and queued (agent decision D18 in `agent_decisions_2026-10-04.md`); waiting for the catalog owner.

| Field | Current workbook value | Runtime value | Required change |
| --- | --- | --- | --- |
| Cluster ID of Intelligence | 8 | 20 (`event_cluster_id.intelligence`) | Either change the workbook ID to 20, or renumber the runtime clusters to the workbook IDs in one coordinated change |
| Members (ID) | 39, 52 | 52 (required), 39 (optional) | No change; note that 52 is the required Low baseline and 39 the optional Medium member |
| Member Severities | Medium, Low | 39 Medium, 52 Low | No change |
| Type | Minor Fire-Once | `event_cluster_type.one_time` | No change |
| Chaos level | 1 | unlock tier 0 (Chaos level 1) | No change |

Runtime cluster 8 is Diseases, which the workbook lists as cluster 13, so the workbook ID 8 cannot be used at runtime without moving Diseases.
The same drift exists for Random Stuff (runtime 12, workbook 19); the catalog owner should decide whether the runtime or the workbook numbering is authoritative before more clusters are added.
ID 20 is free in both the runtime registry and the workbook.
