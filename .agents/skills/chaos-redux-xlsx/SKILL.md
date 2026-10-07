---
name: chaos-redux-xlsx
description: Inspect, edit, and validate Chaos Redux XLSX workbooks while preserving their structure, formatting, formulas, and package features. Use for the event catalog and its generated CSV exports, the separate doctrine workbook, and other repository spreadsheets.
---

# Chaos Redux XLSX

Use this skill for repository spreadsheet files.
It does not authorize changes to gameplay, workbook schemas, external Google Sheets, or publication.

## Choose the workbook contract

- For `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, read [catalog.md](references/catalog.md) and the current `docs/spreadsheets/README.md` before editing.
  The XLSX is the only editable catalog source, and the three catalog CSVs are generated outputs.
- For `docs/spreadsheets/doctrines.xlsx`, read [doctrines.md](references/doctrines.md).
  Preserve its sectioned document architecture rather than treating every sheet as a flat table.
- For another workbook, inspect the supplied file and preserve its user/template architecture.
  Apply catalog rules only to the catalog.

For an event-catalog task that can be delegated, follow `chaos-redux-subagents` and route to `chaosx_spreadsheet_doc_worker` after implementation facts are available.
That role owns only the catalog and its exports unless the parent expands its scope.
Spreadsheet-only transcription does not require HOI4 reference tools or wiki reading.
Use the parent's accepted implementation facts and exact localisation inputs.

## Inspect before choosing a writer

1. Confirm the file is a real XLSX ZIP rather than a Git LFS pointer.
   Read a verified local LFS object for inspection if necessary, or report missing workbook bytes.
   Do not overwrite a pointer with a newly created workbook.
2. Discover sheets, table/header locations, IDs, formulas, merged cells, validations, conditional formatting, links, and ZIP package parts.
   Find rows by IDs and columns by headers, never by remembered row numbers.
   Read-only `openpyxl` is suitable for values and formulas, but inspect ZIP parts or an editable in-memory load when features unavailable in read-only mode matter.
3. Read [preservation.md](references/preservation.md) before saving an existing workbook, changing structure, or touching formulas.
   Unsupported features, comment appearance, or formula caches can make a narrow OOXML edit safer than a full library round trip.

Use `mcp__codex_app__load_workspace_dependencies` when available to discover the bundled Python and libraries.
Check the installed library version before using options such as `rich_text=True`.
Use Windows paths and PowerShell from the mod root.
Pandas is useful for analysis, but `DataFrame.to_excel` must not replace an existing repository workbook.

## Edit and verify

- Keep an immutable before-copy outside the tracked tree and record intended sheet/ID/header/value changes.
  Build and reopen a candidate before replacing the source.
  Check the source hash again at replacement time to catch concurrent edits.
- With `openpyxl`, load the editable candidate with `data_only=False`, `keep_links=True`, and supported rich-text preservation.
  Preserve styles, table/filter ranges, validation, conditional formatting, hyperlinks, comments, sheet order/visibility, merged ranges, dimensions, and print settings relevant to the workbook.
  Never save a `data_only=True` inspection workbook.
- Keep source prose as literal strings, including text beginning with `=`.
  Assign `cell.data_type = "s"` after such an `openpyxl` assignment when the field is literal text, and verify it remains a string on reload.
  Do not reinterpret source text as a formula or prepend a visible apostrophe without checking the consumer.
- Preserve existing formulas and use formulas for calculations that should remain editable in the workbook.
  Catalog prose, IDs, status labels, and schema-defined literal data remain literals.
  Recalculate when dependencies change or a chosen writer invalidates caches needed by a consumer.
  Formula strings and calculation-on-open flags do not prove calculated results.
- Compare reopened before/after cells and workbook features, not just file hashes.
  Review the exact changed cells, full multiline text, targeted statuses, relationships, and any layout changes.
  For OOXML edits, also require unchanged ZIP-part payloads outside the declared changes.

After every successful event-catalog update, run:

```powershell
python .tools/export_event_catalog_csv.py
```

If the shell's Python lacks `openpyxl`, use the discovered bundled executable with the same script and arguments.
Verify exporter exit status and all three output row/header shapes against the accepted workbook.
An export failure leaves the task incomplete until corrected and rerun.
Never repair an export by editing CSV directly.

## Handoff

Report the workbook, sheet/ID/header changes, localisation or accepted source inputs, approval basis for any status change, preservation evidence, exporter outcome, and unresolved calculation or source gaps.
For shared binary changes, keep the cell delta and before/after hashes for the parent, which owns commit integration under `chaos-redux-shared-git-commit`.
Do not claim unperformed visual inspection, formula recalculation, or engine validation.
