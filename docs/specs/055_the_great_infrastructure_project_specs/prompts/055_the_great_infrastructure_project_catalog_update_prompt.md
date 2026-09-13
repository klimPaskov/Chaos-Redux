# Catalog Update Prompt for Event 55

Update the authoritative Chaos Redux event catalog only after Event 55 implementation facts and final player-facing localisation are available.

Use `chaosx_spreadsheet_doc_worker` and the spreadsheet skill.

Edit only:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Do not edit any CSV export directly.

## Event 55 fields

- ID: `55`
- Event name: The Great Infrastructure Project
- Type: Minor Repeatable
- Chaos level: `1`
- Cluster ID: `7`
- Member severity: Medium
- Status: use the verified implementation status

Replace the stale naval description with the final player-facing Event 55 detail from in-game localisation.

Populate Evolution I, II, and III fields from the final Event Details evolution wording for the `200+`, `400+`, and `600+` stages.

Keep absent surfaces blank. Do not add absence wording.

## Cluster 7 fields

Update Positive Economy to include Event IDs `18` and `55`.

Use the final in-game cluster detail wording. Describe Resources Found and The Great Infrastructure Project as beneficial economic shocks with persistent development choices and a same-actor Resource Corridor connection.

## Neighboring row audit

Review Events `54` through `58` because the supplied export shows shifted details. Correct only with verified source wording. Do not guess missing event descriptions.

## Export

After saving the workbook, run:

```text
python .tools/export_event_catalog_csv.py
```

Review the regenerated Events and Clusters CSV rows for Event 55 and cluster 7. Preserve workbook formatting, formulas, filters, and validation.

Write a handoff listing the workbook cells or rows changed, export result, and any unresolved neighboring-row conflict.
