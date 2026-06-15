# Event 010 Death - Catalog Update Brief

## Current Catalog State

The workbook `docs/spreadsheets/chaos_redux_events_catalog.xlsx` currently has row 11 representing Event 010 as:

- ID: `10`
- Name: `Spirit of War/Peace`
- Description: `Random country gets options to either be a symbol of war or a symbol of peace.`
- Type: `Minor Fire-Once`
- Status: `To Be Reworked`

The same row also contains later planning columns for a separate future idea (`Natural Disasters 2`). Do not overwrite unrelated planning columns unless explicitly asked.

## Update Timing

Do not update the workbook during spec-only planning. Update after implementation facts are stable so spreadsheet event detail, evolution detail, and catalog wording match in-game localisation.

Use the `xlsx` skill and `chaosx_spreadsheet_doc_worker` after implementation.

## Target Row Direction

Suggested replacement row fields:

| Field | Target |
| --- | --- |
| ID | `10` |
| Name | `Death` |
| Description | A quiet black country appears on a remote island, spreads through empty coasts, reveals itself as Death, and can become a world-end threat if ignored. |
| Type | `Minor Fire-Once` |
| Status | Implemented when gameplay is complete; otherwise Planned/In Progress as appropriate |
| Cluster | no cluster |

If the workbook has event-detail/evolution columns, align them with in-game wording:

- early hidden absence
- public reveal
- ghost muster
- containment failure
- Living Compact
- forbidden route
- world-end
- defeat aftermath
- world consumed

## Spreadsheet Worker Prompt

After Event 010 implementation is complete, update `docs/spreadsheets/chaos_redux_events_catalog.xlsx` for Event 010 only. Replace obsolete Spirit of War/Peace catalog wording with Death. Preserve unrelated future-planning columns unless asked otherwise. Match the row summary, event-detail fields, evolution-detail fields, status, type, and notes to the final in-game localisation and docs. Use the `xlsx` skill, preserve workbook formatting, and report changed cells.
