# Event 008 Catalog Row Note

The workbook `chaos_redux_events_catalog.xlsx` was inspected and updated after implementation.

Current row finding:

| Field | Value seen in workbook |
| --- | --- |
| ID | 8 |
| Event Name | Tensions Rising |
| Details | Value-neutral event-detail text describing world-tension pressure, timer pacing, timed opinion penalties, AI readiness ideas, delayed incidents, achievement tracking, and rare safe border wars. |
| Type | Minor Repeatable |
| Status | Implemented |

Implementation decision:

The source of truth sets the baseline to `+100` world tension with four evolved chaos/world tension stages. The workbook row does not duplicate these numeric packets, so the `10x` world-tension tuning is represented in script constants, option-tooltip localisation, and source docs rather than in catalog cells.

Spreadsheet action:

The workbook row was updated from the final in-game event-detail wording so it uses the delayed-incident terminology and includes the rare safe border-war pressure surface. The `Diplomatic Panic` cluster detail also notes rare safe non-transfer border wars.
