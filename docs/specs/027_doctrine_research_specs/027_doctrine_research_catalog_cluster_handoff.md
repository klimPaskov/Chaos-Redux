# Event 027: Catalog and National Breakthroughs cluster handoff

## Authority

`docs/spreadsheets/chaos_redux_events_catalog.xlsx` is the only editable catalog source, and the `chaos-redux-xlsx` skill and `chaosx_spreadsheet_doc_worker` own its edits and the CSV export.
The historical v2 cluster table reproduced in `docs/systems/event_system/event_clusters.md`, which lists Event 27 under a "Scientific Research" cluster 9 and under Military Preparation, is not the current catalog; the workbook and the runtime registry both use cluster 9 for National Breakthroughs.

## Event 027 row

The workbook row already carries the in-game Event Details and the four evolution texts, Minor Repeatable, Calm World, and cluster 9.
One change is queued: Status moves from To Be Reworked to Needs Testing.
The exact cells are listed in `docs/plans/027_doctrine_research_plans/catalog_changes_pending.md`, which is the single source for pending workbook edits.
Status moves to the project's playable value only after the user's live validation.

If revisions R1 to R7 change Event Details or evolution wording, the workbook row follows the new localisation rather than any text in this package.

## Event 027 cluster member

| Attribute | Value |
| --- | --- |
| Cluster | National Breakthroughs, ID `9` |
| Runtime row | `9001` |
| Role | Optional when another member is selected; guaranteed when Event 027 is the selected event |
| Minimum tier | Calm World |
| Severity | Medium |
| Effect | One normal fanout at the current stage, no extra choices, one pacing event for the whole cluster |

## National Breakthroughs cluster

| Field | Value |
| --- | --- |
| Name | National Breakthroughs |
| Members | `27`, `54`, `65`, `67`, `83`, `85`, `89` |
| Severities | Medium, Medium, Low, Medium, Low, Medium, High |
| Type | Minor Repeatable |
| Chaos level | 1 (Calm World) |
| Status | Partially Available while Event 027 is the only runtime member |

The cluster should feel like a short development cycle of two or three related advances.
Each member keeps its own type, fired state, repeatable cap change, and history, and disabled or exhausted members are skipped with a logged reason.
Participation chances are tuned with the complete member pool once a second member is implemented.

## Member roles for future reworks

Each member needs its own accepted spec; this table only records the cluster role each one should fill.

| Event | Catalog concept | Cluster role | Concern for the cluster |
| --- | --- | --- | --- |
| 27 | Doctrine Research | Global doctrine curriculum | Strong at Evolution IV. |
| 54 | Gift from scientists | Institutional or infrastructure development | Row is vague and needs a rework. |
| 65 | Random Trait | Leadership development | Global leader changes need duplicate and validity guards. |
| 67 | Generalissimo | Exceptional command appointment | Fire-once and potentially strong for one country. |
| 83 | Agency upgrade | Agency or government improvement | Current details describe political power, which conflicts with the name. |
| 85 | XP | Military experience | Compounds with Event 027 when both join; neither may scale the other. |
| 89 | Tech sharing | Doctrine or military-knowledge sharing | Overlaps doctrine content; it must own sharing, never call the Event 027 curriculum as a shortcut. |
