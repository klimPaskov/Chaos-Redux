# Repression and Camps window: current render pass, 2026-10-04

Disposition: `implemented` for the defects listed below; tooltip bodies and engine text wrapping remain `needs_live_game`.

Route: `hoi4_gui_render` on `repression_ledger_window` (and once on `camp_admin_records_panel`), production MCP, workspace `mod_chaos_redux_ea3b2d67c2c0`.
Every call completed with `GUI_RENDERED`; the 2026-10-03 `INTERNAL_ERROR` and `JOB_WORKER_EXIT` failures did not recur.
Scenarios are built by `build_scenarios.py` in this folder (GER source fixtures, not saves); values are pre-formatted to the precision the localisation prints because the preview substitutes raw values.

## Coverage

| View | Scenario | Resolutions | States | Result |
| --- | --- | --- | --- | --- |
| Administration | `admin_ger_1943_11_01_full` (four-digit custody, long project places, one available and one blocked national action) | 1280x720, 1920x1080, 1920x1080 at 1.25 | normal, hover, disabled | clean after the summary fix |
| Administration | `admin_ger_1943_11_01_shortage` (maintenance shortage panel) | same three | normal, hover | clean |
| Locations | `locations_ger_1943_11_01_records_incomplete` (eight rows, scroll, long names, selected host with incomplete survivor records, locked orders) | same three | normal, hover, full-list, long-text | clean after the row and condition fixes |
| Locations | `locations_ger_1943_11_01_empty` | 1280x720, 1920x1080 at 1.25 | normal, empty-list | clean |
| Records | `records_ger_1945_05_01_full` (large totals, records-incomplete closure, escapes to Sweden, seven history rows) | same three | normal, hover, full-list, maximum-value | clean after the history fix |
| Purpose picker | `picker_role_ger_1943_11_01` (killing center locked) | 1280x720, 1920x1080 at 1.25 | normal, hover, disabled | clean |

Validation reported no blocking checks and no conflicting click regions in the final scenarios.
`GUI_TAB_STATE_CONFLICT` appeared once while the crisis panel was left undeclared in an early Locations scenario; the tab buttons are always visible by design and the marker strip shows the active view, so it is not a layout defect.

## Defects found and fixed

1. Summary band (Administration): value boxes were 181 px wide, so a four-digit custody figure at UI 1.25 was cut (`before_admin_summary_1920_125.png`). The first three columns are now 197 px (16 px gutter) and the deaths column 181 px so it ends 16 px inside the band (`after_admin_full_*.png`).
2. Location rows: a long state name wrapped onto a second line and overlapped the purpose line (`before_locations_row_overlap_1920_125.png`). The name and purpose boxes use `truncate = yes` and a one-line height, following vanilla `countryoccupationview.gui` (`after_locations_*.png`); the full name stays in the row tooltip and the detail panel title.
3. Locations condition line: the incomplete-records condition was a three-sentence paragraph in a one-line box (`before_locations_condition_1280.png`). It now reads "Survivor records are incomplete. Release, transfer and work orders are paused here." and the reform consequence stays in the Records warning and the release tooltip.
4. Records history: "Closed; survivors released without complete origin records" lost its last word in the 372 px title box (`before_records_history_clipped_1280.png`). The entry now reads "Closed; survivors released with incomplete records" (`after_records_history_1280.png`).

## Limits

- The preview applies a window-level visibility value to every list row, so the per-row selection marker cannot be shown on one row only; selection highlight is `needs_live_game`.
- `truncate = yes` is drawn as a hard cut in the preview; the engine adds an ellipsis.
- Tooltip bodies (Records warning, blocked-reason text, institution tooltips, release and closure tooltips) are not drawn by the preview; their text was reviewed in source and is `needs_live_game`.
