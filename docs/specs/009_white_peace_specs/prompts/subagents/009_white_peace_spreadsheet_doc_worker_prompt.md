# Subagent Prompt — chaosx_spreadsheet_doc_worker — Event 009 White Peace

Spawn with `fork_turns="none"` after Event 009 implementation and final localisation are in place.

Read only:

- the event catalog workbook at `docs/spreadsheets/chaos_redux_events_catalog.xlsx`;
- final Event 009 localisation/scripted localisation needed to mirror player-facing wording;
- the `xlsx` skill and named pending fields in `docs/plans/009_white_peace_plans/catalog_changes_pending.md`.

Update only the catalog workbook row for Event ID `9` and Peace cluster fields if present. Preserve workbook structure, formatting, formulas, filters, freeze panes, validation, and existing sheets.

Player-facing fields should mirror final in-game event detail and evolution detail. Event 009 should remain Type `Minor Repeatable`, Cluster `Peace`, Cluster ID `4`, and Status follows the [chaos-redux-events catalog contract](../../../../../.claude/skills/chaos-redux-events/SKILL.md) and attributable user approval, not an inferred implementation verdict.

After saving XLSX, run `python .tools/export_event_catalog_csv.py` from the mod root under [chaos-redux-subagents](../../../../../.claude/skills/chaos-redux-subagents/SKILL.md).
The three catalog CSVs are export-only.
Report changed cells and exporter outcome. Do not edit gameplay files or docs.
