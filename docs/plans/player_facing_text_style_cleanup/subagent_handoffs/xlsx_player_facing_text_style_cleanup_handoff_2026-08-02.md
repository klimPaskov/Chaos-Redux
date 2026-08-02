# Workbook Player-Facing Text Style Cleanup Handoff

Updated workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

Changed sheets and fields:

- `Events`: Details column C for event IDs 1 through 166 and backlog rows 168 through 183, selected evolution cells, Status column M, and status cell fills.
- `Clusters`: cluster names in column B, player-facing details in column C, Status column G, and status cell fills.
- `Scenarios`: player-facing Details column C, Type Options column D where wording was process-like, Intensity Scaling column E, Status column F, and status cell fills.
- `Legend`: availability labels and wording in rows 8 through 12, type applies-to wording in rows 3 through 6, and matching color cells.

Status labels now use `Playable`, `Partially Available`, and `Unavailable` across all three catalog sheets. `Fully Functional` and `Needs Testing` map to `Playable`, `In progress` maps to `Partially Available`, and `New`, `To Be Reworked`, `Placeholder`, `Buggy`, and `Under review` map to `Unavailable`. Blank statuses on named backlog rows are now `Unavailable`.

The workbook keeps its existing sheet order, dimensions, tables, row and column dimensions, filters, freeze-pane state, data-validation ranges, and conditional-formatting ranges. Status data validations and conditional-formatting formulas now use the three availability labels while retaining the original palette and rule count.

Actual sourced quotation strings were preserved verbatim, including `“Time Traveler”`, `“Fear of Dracula”`, `“Count Dracula”`, `“Secret Society Influence”`, `"Tomorrow's Girls"`, and `"Kings"`.

Exporter result: `python .tools/export_event_catalog_csv.py` completed successfully and refreshed the three export-only snapshots. Events export contains 183 rows and 13 columns with SHA-256 `6b4b809443323fb5190d33d3c0f02ba9de95f1fe4621c2c2f380a8ca755b3ab7`. Clusters export contains 14 rows and 7 columns with SHA-256 `3707b10ef4beea4595df54b943aac76f8de342a1a13c53a19abf51692d12c840`. Scenarios export contains 13 rows and 6 columns with SHA-256 `4adaf3fcb8e63e10362dd096b2fa582c78b5a715e11075db239c`.

Validation: the workbook contains zero formulas and no formula-error tokens. All target Events, Clusters, Scenarios, and Legend text is free of em or en dashes and semicolons. No `Reserved placeholder` wording or process-style status values remain. The LibreOffice-based `recalc.py` helper could not run because LibreOffice is not installed on this Windows environment.

Blocked or needs-user-review cells: none identified in the workbook scope.
