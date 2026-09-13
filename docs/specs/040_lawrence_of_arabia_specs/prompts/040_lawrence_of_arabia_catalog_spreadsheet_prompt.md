# Event 40 Catalog Spreadsheet Prompt

Update the Chaos Redux event catalog only after Event 40 implementation wording and final status are known.

## Required reading

Read:

- `/home/oai/skills/spreadsheets/SKILL.md` or the active spreadsheet skill
- `AGENTS.md` spreadsheet rules
- `docs/specs/040_lawrence_of_arabia_specs/catalog/040_lawrence_of_arabia_catalog_alignment.md`
- final Event 40 Event Details and evolution localisation
- final implementation documentation

Use `chaosx_spreadsheet_doc_worker` with a context-complete prompt.

## Editable source

Edit only:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Preserve workbook structure, formatting, filters, formulas, validation, and sheet names.

Do not edit:

- `chaos_redux_events_catalog.csv`
- `chaos_redux_clusters_catalog.csv`
- `chaos_redux_scenarios_catalog.csv`

After the workbook saves successfully, run:

`python .tools/export_event_catalog_csv.py`

## Event 40 row requirements

- ID: `40`
- Event name: Lawrence of Arabia
- Type: Minor Fire-Once
- Chaos level: `1`
- Cluster ID: blank
- Member severity: blank
- Details: match final Event Details premise
- Evolution I: match the final Arab Revolt Network wording
- Evolution II: match the final British Arabian System wording
- Evolution III: match the final Lawrence's Arabia wording
- Evolution IV: blank
- Evolution V: blank
- World-End Scenario: blank
- Status: use the implementation evidence, never upgrade status from planning alone

The row must explain that the event fires once while its internal regional chain can continue. It must not imply that the event returns to the random pool.

## Validation

After export:

- reopen the workbook
- verify the Event 40 row
- compare the three exported CSV rows with their workbook sheets
- confirm no cluster or scenario row was added for Event 40
- report the workbook path, exported files, exact row fields, and any preserved uncertainty
