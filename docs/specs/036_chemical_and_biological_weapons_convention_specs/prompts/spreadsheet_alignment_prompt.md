# Spreadsheet alignment prompt

Update the event catalog after Event 036 gameplay and final localisation exist, through `chaosx_spreadsheet_doc_worker` and [the spreadsheet skill](../../../../.claude/skills/chaos-redux-xlsx/SKILL.md).

## Current catalog state

Checked on 2026-10-10 against the exported snapshots:

| Surface | Current value |
| --- | --- |
| Event row 36 | Alien Spacecraft, Minor Repeatable, Chaos level 1, cluster 3, To Be Reworked |
| Cluster row 3 | Diplomacy, members 8, 17, 36, 59 with severities Medium, Medium, High, High |
| Runtime cluster 3 | `diplomatic_panic` constants with members 8 and 17 only |

The cluster assignment is already in the workbook, so no new cluster is created.

## Required event row

| Field | Value |
| --- | --- |
| Event Name | Chemical and Biological Weapons Convention |
| Details | The final Event Details premise |
| Evo I to Evo III | Summaries matching the evolution detail text |
| Type | Minor Fire-Once |
| Chaos level | `1` |
| Cluster ID | `3` |
| Status | The status the implementation evidence supports |

Edit only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then run `python .tools/export_event_catalog_csv.py` from the mod root and confirm all three CSV snapshots regenerated.
