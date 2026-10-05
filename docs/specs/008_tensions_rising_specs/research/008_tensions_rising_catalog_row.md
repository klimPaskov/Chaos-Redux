# Event 008 Catalog Row Note

Disposition: implemented documentation correction, with workbook wording alignment blocked by the parent's no-workbook-edit boundary.
The authoritative workbook remains `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
The [2026-10-05 release audit](../../../plans/008_tensions_rising_plans/subagent_handoffs/event_completion_audit_2026-10-05.md) read it without changing cells or exports, and the parent supplied those exact current facts for this reconciliation.
The earlier claim that this note proved a workbook update and `Implemented` status is superseded by that direct read-only evidence.

Current audit finding:

| Field | Value seen in workbook |
| --- | --- |
| ID | 8 |
| Event Name | Tensions Rising |
| Details and Evo I-IV | Pre-2026-10-05 localisation wording, pending alignment with the final in-game keys. |
| Type | Minor Repeatable |
| Status | Needs Testing |

Cluster 3 audit finding:

| Field | Value seen in workbook |
| --- | --- |
| Name | Diplomacy |
| Members | 8,17,36,59 |
| Member severities | Medium,Medium,High,High |
| Status | Partially Available |

## Pending wording handoff

The parent owns the exact pending catalog wording and any later workbook authorization.
Mirror the final assigned keys from [the localisation handoff](../../../plans/008_tensions_rising_plans/subagent_handoffs/localisation_audit_2026-10-05.md):

- `chaosx.events_log.window.event_details.tensions_rising`.
- `chaosx.events_log.window.evolution_details.tensions_rising.body.event_detail`.
- `chaosx.events_log.window.evolution_details.tensions_rising.body.stage_1` through `.stage_4`.

Details fields describe the situation and premise rather than listing timer values, penalties, achievement routes, or mechanical rewards.
The baseline and four evolved packets are implementation facts recorded in the overview and tuning source, without establishing approval for broader design proposals.
Cluster wording remains subject to the cluster owner's source and acceptance evidence because the workbook/four-member overview and the directly inspected runtime member branch disagree.
This reconciliation edited no workbook or CSV and ran no exporter.
After a separately authorized successful workbook update, its owner must run `python .tools/export_event_catalog_csv.py` from the mod root.
