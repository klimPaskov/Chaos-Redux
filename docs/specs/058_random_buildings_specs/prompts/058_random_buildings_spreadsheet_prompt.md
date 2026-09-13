# Spreadsheet update prompt for Event 58 Random Buildings

Use this prompt with `chaosx_spreadsheet_doc_worker` only after Event 58 implementation and final in-game wording are available. Spawn with `fork_context=false`.

Read the spreadsheet skill, the authoritative workbook, the final Event 58 localisation and scripted localisation needed for mirrored fields, and the final Positive Economy cluster wording. Do not read broad repository files.

## Event row update

Update Event ID `58` in the workbook to replace the stale `The Industrial Complex` entry.

Required facts:

- Event Name: Random Buildings
- Type: Minor Repeatable
- Chaos level: `1`
- Cluster ID: `7`
- Member Severity: Medium
- Details: use the final player-facing Event Details premise wording or the workbook's approved summary field, according to the existing sheet convention
- Evolution I: mirror the final Expanded State Construction preview
- Evolution II: mirror the final Provincial Construction preview
- Evolution III: mirror the final Exceptional Construction preview
- World-End Scenario: leave blank under the current sheet convention
- Status: use the final status supported by implementation and validation evidence

Do not paste raw weights, provider fields, owner callback rules, or implementation history into player-facing cells.

## Cluster row update

Update Cluster ID `7`, Positive Economy:

- add member ID `58` without removing Event `18`
- preserve the cluster's type and Chaos level
- update details so the wording covers beneficial resource and development shocks, including Random Buildings, without becoming a mechanics list
- mirror final in-game cluster wording where the workbook field is intended to match it

## Workbook rules

- edit only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- preserve formatting, formulas, filters, validation, freeze panes, and workbook structure
- never edit any CSV directly
- save the workbook in place
- run `python .tools/export_event_catalog_csv.py`
- confirm all three CSV exports were refreshed

Report the workbook path, sheets, rows, columns, fields, event IDs, exporter result, and any blocked or needs-user-review cell.
