# Prompt for `chaosx_spreadsheet_doc_worker`

Spawn with `fork_context=false` after implementation, localisation, and permanent docs are final.

Repository root: `<MOD_ROOT>`.

Edit only:

```text
docs/spreadsheets/chaos_redux_events_catalog.xlsx
```

Update affected player-facing rows based on verified implementation and final in-game wording.

Priority rows include:

- Event 5 Soviet Collapse
- Event 6 Independence Wave
- Event 13 natural disasters
- Event 14 Cannibalism and Hunger Lines
- Event 15 Utopia Manifesto
- Event 20 Black Plague
- Event 21 Random Civil War
- Event 28 Asteroid Incoming
- Event 33 Acid Rain Superstorm
- Event 50 Great Embargo
- Event 95 Occupation Revolt
- Event 118 Locust Plague
- Event 120 Volcano
- Event 131 Mutiny
- Event 149 Immigrations
- relevant cluster and scenario rows where behavior changed

Event 149 must describe its retired or shared-system adapter role. It must not retain a flat random population-drain description.

Preserve workbook structure, formatting, formulas, filters, and validation.

After saving, run:

```text
python .tools/export_event_catalog_csv.py
```

Do not edit CSV exports directly.

Write a concise handoff with workbook fields changed and exporter result.
