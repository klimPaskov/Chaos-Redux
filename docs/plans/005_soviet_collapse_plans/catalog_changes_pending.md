# Event 005 Catalog Changes Pending, 2026-10-05

The Event 005 row is `Events!A6:M6`; its Details value is `Events!C6`. The workbook still contains the former wording with mechanic readouts, action summaries, and process language.

The parent accepted the following replacement under the user's explicit authorization for Event 005 design rewrites:

> The Soviet Union is losing command over its republics and the forces that connect them. Local ministries, garrisons, rail offices, and depots answer to competing authorities as Moscow struggles to keep its orders in force. Across the republics, officials and soldiers must decide whom to follow.

Disposition: accepted and queued for the workbook mirror. The parent applied the exact body to `chaosx.events_log.window.event_details.soviet_collapse` at `localisation/english/chaosx_gui_l_english.yml:693`. The workbook and all three catalog CSV exports remain user-forbidden and untouched; exact catalog parity is pending a separately authorized workbook update and export.

For GUI evidence, the parent inspected the `usa_1936` fixture on 1936.1.1; inspect transformed it to `usa_1936-generated-1` with 32 unresolved, 3 missing, and 21 click-region overlap diagnostics. A normal/long-text 1920 x 1080/uiScale 1 render returned 27 `GUI_RENDERED` artifacts. The artifact reader opened the Fury empty-details fixture, but it contains no Event 005 body; the standard USA scenario also has no seeded Soviet Event Details text. The populated-content before-render for `events_log_event_details_window` used `fury_release_details_1936`, 1936.1.1, 1920 x 1080/uiScale 1, normal and long-text states, and `generatedScenarios=false`; it timed out after 600 seconds with no valid populated Event 005 PNG or validation. No matching before artifact exists for an Event 005 comparison, no layout definitions changed, and visual acceptance remains unresolved.

The title `Soviet Union Collapse`, evolution fields, world-end field, type, chaos level, cluster, and status were not changed. The revised opening popup and news popup do not map to separate columns in this catalog row. After an authorized workbook update, run `python .tools/export_event_catalog_csv.py` from the mod root; never edit generated CSVs directly.
