# Event 065 Random Trait Spreadsheet Alignment Prompt

## Role

Run `chaosx_spreadsheet_doc_worker` after Event 65 implementation facts are stable.

Read `AGENTS.md`, the Event 65 specification package, implementation report, Randomizations cluster implementation, permanent event docs, and current workbook export instructions.

## Source of truth

Find and edit the authoritative Chaos Redux XLSX.

Do not treat the supplied CSV files as the editable source.

Use the workbook's existing styles, formulas, data validation, and row conventions.

Use the spreadsheet skill and workbook tools required by the project.

## Event 65 row

Update:

- ID `65`
- event name `Random Trait`
- concise baseline details
- Evolution I `Double Traits` at raw Chaos `200+`
- Evolution II `Exceptional Personalities` at raw Chaos `400+`
- Evolution III `Walking Contradictions` at raw Chaos `600+`
- Minor Repeatable type
- Chaos level `1`
- final Randomizations cluster ID
- Medium member severity
- evidence-backed status

Keep Evolution IV and Evolution V empty.

Do not add unrelated consequence text.

## Randomizations cluster row

Inspect the current workbook and source constants for an existing row and ID collision.

Prefer ID `9` only when it remains unused.

Record:

- cluster name `Randomizations`
- concise randomization premise
- Event `65` membership
- Minor Repeatable type
- Chaos level `1`
- evidence-backed status

If ID `9` is occupied, select one unused ID with the owning agent and update every linked source and document before export.

## Export

Run the repository's official workbook export workflow.

Regenerate:

- event catalog CSV
- cluster catalog CSV
- scenario catalog CSV when the export script produces it

Compare the exported Event 65 and Randomizations data with runtime constants, docs, Event Details, and cluster text.

## Output

Write an alignment handoff that includes:

- workbook path
- sheet and row references
- cells changed
- final cluster ID
- style and validation preservation
- export command
- exported file paths and hashes
- cross-surface comparison
- unresolved mismatch
- status of pass, blocked, or needs user review

Do not implement gameplay source.
