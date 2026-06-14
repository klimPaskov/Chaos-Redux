# Subagent Prompt — chaosx_spreadsheet_doc_worker — Event 009 White Peace

Spawn with `fork_context=false` after Event 009 implementation and final localisation are in place.

Read only:

- the event catalog workbook at `docs/spreadsheets/chaos_redux_events_catalog.xlsx`;
- final Event 009 localisation/scripted localisation needed to mirror player-facing wording;
- the source spec folder `docs/specs/009_white_peace_specs/` as supporting context.

Update only the catalog workbook row for Event ID `9` and Peace cluster fields if present. Preserve workbook structure, formatting, formulas, filters, freeze panes, validation, and existing sheets.

Player-facing fields should mirror final in-game event detail and evolution detail. Event 009 should remain Type `Minor Repeatable`, Cluster `Peace`, Cluster ID `4`, and Status should reflect implementation state only if the parent agent confirms it.

Report changed sheet, row, columns, event id, and any cells that need user review. Do not edit gameplay files or docs.
