# Event 57 Catalog Alignment Prompt

Update only the authoritative workbook:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Use `chaosx_spreadsheet_doc_worker` and the current spreadsheet skill.

Read the final implemented Event 57 name, Event Details text, evolution text, cluster membership, and status. Do not use the stale CSV row as source of truth.

## Event row

Replace the old Event 57 Radar identity with:

- ID `57`
- The Black Market
- Minor Fire-Once
- Chaos level `1`
- Positive Economy
- High member
- final implementation status proven by the parent

Write concise player-facing details that match the in-game Event Details premise.

Add summaries for:

- Evolution I, International Network, `200+`
- Evolution II, The Underground Economy, `400+`
- Evolution III, Anything Has a Price, `600+`

Do not list raw modifiers, hidden formulas, internal values, source file names, or implementation history.

## Cluster row

Add Event 57 to Positive Economy with High member severity while preserving many-to-many and repeated-slot semantics in the current workbook model.

Do not remove Event 18 or unrelated members.

## Export

After saving the workbook, run:

`python .tools/export_event_catalog_csv.py`

Verify that the Events, Clusters, and Scenarios CSV exports regenerate successfully. Never edit those CSVs directly.

## Preservation

Preserve workbook structure, formatting, formulas, filters, validation, and unrelated rows.

Return a handoff with changed sheets, row identifiers, exact fields, export result, and any mismatch that still requires parent action.
