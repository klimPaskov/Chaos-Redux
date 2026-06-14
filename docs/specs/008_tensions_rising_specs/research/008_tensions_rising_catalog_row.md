# Event 008 Catalog Row Note

The workbook `chaos_redux_events_catalog.xlsx` was inspected after implementation.

Current row finding:

| Field | Value seen in workbook |
| --- | --- |
| ID | 8 |
| Event Name | Tensions Rising |
| Details | Value-neutral event-detail text describing world-tension pressure, timer pacing, timed opinion penalties, AI readiness ideas, delayed reports, and achievement tracking. |
| Type | Minor Repeatable |
| Status | Implemented |

Implementation decision:

The source of truth sets the baseline to `+100` world tension with four evolved chaos/world tension stages. The workbook row does not duplicate these numeric packets, so the `10x` world-tension tuning is represented in script constants, option-tooltip localisation, and source docs rather than in catalog cells.

Spreadsheet action:

No workbook changes were needed for the `10x` tuning pass because the current Event 8 catalog row contains no stale numeric packet values.
