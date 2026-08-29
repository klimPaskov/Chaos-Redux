# Subagent Prompt: Event 021 Spreadsheet Worker

Spawn `chaosx_spreadsheet_doc_worker` with `fork_context=false` only after final in-game wording and implementation facts exist.

Read only:

- parent prompt
- spreadsheet skill
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- final Event 021 localisation and scripted localisation needed to mirror player-facing wording
- final Wars cluster localisation
- final triggerable scenario localisation
- final event, evolution, cluster, and scenario implementation facts

Edit only the authoritative workbook.

Update:

- Event 021 name, type, status, details, chaos level, cluster, and severity
- Evolution I, II, and III player-facing detail fields
- Wars cluster membership and Event 021 role
- the verified manual scenario ID, name, details, type options, intensity scaling, and status
- any workbook fields that mirror Event Details or event logs

Do not use working labels when final localisation differs.

Preserve workbook structure, formulas, formatting, filters, and validation.

After saving, run:

`python .tools/export_event_catalog_csv.py`

Do not edit CSV files directly.

Write:

`docs/plans/021_random_civil_war_plans/subagent_handoffs/spreadsheet_doc_worker_handoff.md`

Report workbook cells or rows changed, exporter result, and unresolved wording or ID conflicts.
