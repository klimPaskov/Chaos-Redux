---
name: chaos-redux-xlsx
description: Inspect, edit, and validate Chaos Redux XLSX workbooks while preserving their structure, formatting, formulas, and package features. Use for the event catalog and its generated CSV exports, the separate doctrine workbook, and other repository spreadsheets.
---

# Chaos Redux XLSX

## Edit sequence

1. Read the workbook contract: [catalog.md](references/catalog.md) for the event catalog, [doctrines.md](references/doctrines.md) for the sectioned doctrine workbook, or the supplied template for another workbook.
2. Confirm real ZIP bytes, resolving a Git LFS pointer as described in [preservation.md](references/preservation.md#source-bytes) if needed.
   Keep an immutable before-copy outside the tracked tree and record its hash plus the intended sheet/key/header/value delta.
3. Discover headers, stable row keys, formulas, merges, tables, validations, formatting, and package features before choosing the writer below.
4. Build and reopen a candidate; use the [literal-edit example and comparison criteria](references/preservation.md) to verify the delta and retained features.
   Recheck the authoritative source hash immediately before replacement; if another writer changed it, rebuild from that version.
5. After every accepted event-catalog save, including formatting-only edits, run `python .tools/export_event_catalog_csv.py` from the mod root and verify all three exports against the workbook using a CSV parser.
   An export failure leaves the update incomplete; repair the workbook or export route and rerun.

| Task | Write route | Required evidence |
| --- | --- | --- |
| Existing cells using supported features | Editable `openpyxl`, `data_only=False`, preserving links/rich text | Reopened delta and relevant feature comparison |
| Bounded cell edit whose full round trip loses unrelated features | Narrow OOXML candidate edit | Unchanged undeclared ZIP payloads plus semantic comparison |
| Rows, columns, ranges, formulas, or dependencies | Explicit dependency repair and calculation where needed | Updated coverage/consumers and independently expected results |

Never save a `data_only=True` inspection or replace a template with a dataframe/write-only rebuild.
Read [preservation.md](references/preservation.md) before writing; formula caches and unsupported package features can change the route.
Use `mcp__codex_app__load_workspace_dependencies` if the shell lacks the required libraries, and check the installed version before using `rich_text=True`.

## Handoff

Give the parent the cell delta, source/after hashes, wording sources, status approval basis where applicable, preservation comparisons, exporter result, and remaining gaps.
Report visual inspection and recalculation only when performed.
For catalog delegation, use `chaos-redux-subagents` and `chaosx_spreadsheet_doc_worker` after implementation facts are available; its default ownership is the catalog and exports.
Spreadsheet transcription alone needs no HOI4 engine references.
Local edits do not authorize schema migration or publication to external copies.
