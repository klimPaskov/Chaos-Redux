# Preservation and calculation

## Choose the smallest reliable write

Read ZIP member names, content types, worksheet relationships, and load warnings before deciding whether `openpyxl` can preserve the actual workbook.
Use it for ordinary supported workbook features with an editable load:

```python
from openpyxl import load_workbook

wb = load_workbook(source, data_only=False, keep_links=True, rich_text=True)
# Locate the approved row by ID and column by discovered header.
# Change values on the existing cells so their styles remain attached.
wb.save(candidate)
wb.close()
```

`rich_text=True` needs a supporting library version.
For an actual macro-enabled workbook use `keep_vba=True` and preserve its extension, but this does not establish support for every package feature.
Never save an inspection opened with `data_only=True`, which exposes cached values instead of formula expressions.
A read-only load omits some workbook features and is not a preservation audit.
Pandas replacement writes and `write_only=True` regeneration discard template architecture.

Charts, images, VML drawings, threaded/rich comments, controls, pivots, slicers, external links, embedded objects, custom XML, extension lists, and signatures require feature-specific inspection.
Their presence is not proof that all are unsupported, nor does a warning-free load prove preservation.
Ordinary comment text/author can survive `openpyxl`, while original comment formatting, position, and dimensions do not reliably survive.
Do not silently remove these features or relax preservation because the edit is small.

For a bounded cell edit where a full round trip loses unrelated features, change only the needed worksheet XML cell nodes inside a candidate ZIP and copy all other member payloads unchanged.
Use a task-sized edit rather than a general workbook rewriter.

- Resolve sheet names through `xl/workbook.xml` and its relationships.
  Do not assume a sheet title maps to `sheet1.xml`.
- Assert the expected old value, exact cell reference, data type, and style before changing it.
  Decode shared strings for matching, but avoid modifying a shared-string entry used by unrelated cells.
  A new `inlineStr` can represent replacement literal text without rewriting the shared-string table.
- Preserve the cell's style and unrelated attributes.
  Escape XML text and retain whitespace/newlines with `xml:space="preserve"` where needed.
  Literal text beginning with `=` must remain a string, not become an unintended formula.
- Do not use a broad regex or XML reserialization that drops namespace declarations, extension content, or unrelated nodes.
  Respect inherited namespaces and preserve untouched subtrees.
- Copy member metadata and verify every undeclared member payload is identical after the ZIP rewrite.
  Reopen the candidate and compare semantic values and workbook features as well.
- Formula/dependency changes need cache invalidation and appropriate calculation-chain handling.
  Shared, array, spill, and data-table formulas require their own range semantics, so do not overwrite one cell as though it were an independent scalar formula.
  Editing a signed package also affects signature validity and must be reported.

## Structural edits

`insert_rows`, `delete_cols`, and `move_range` do not maintain every dependent formula, table, chart, or defined name.
For an approved structure change, map the dependencies and update table/filter ranges, validation and conditional-formatting coverage, formulas/names, print areas, merges, and consumers explicitly.
Copy style components with `copy.copy` from the matching reference row/cell rather than assigning a generic palette.
Do not rely on copying a style to extend validation or conditional formatting.
Reopen and verify new rows have the intended presentation and coverage.

## Formula results and recalculation

An OOXML formula (`<f>`) and its cached result (`<v>`) are separate.
`openpyxl` writes formulas but never evaluates them and commonly removes cached formula results when saving.
Setting `fullCalcOnLoad`, `forceFullCalc`, or automatic calculation requests a future calculation, not a result.
Existing cached values can also be stale even when nonempty.

Recalculate when formulas or their dependencies change, or when needed caches are invalidated by the writer.
A literal-only catalog with no formulas does not need an engine.
An unrelated narrow XML text/style edit can preserve unaffected valid formula caches without forcing recalculation.
Do not insert formulas into prose catalogs merely to satisfy a generic spreadsheet rule.

No bundled calculation engine is provided.
Use an installed application's supported calculation operation on a candidate copy:

- With Excel automation, create a separate application instance, disable macro execution and external-link updates, open only the candidate, call `Application.CalculateFullRebuild`, wait for completed calculation, save, close, and quit that instance.
  It recalculates all open workbooks in the instance, so do not attach to the user's active instance.
- With LibreOffice Calc, use its **Data > Calculate > Recalculate Hard** operation, then save the candidate as XLSX and verify preservation and compatibility.
  Headless automation needs an installed working route that explicitly calculates, such as UNO `calculateAll`; `--convert-to` alone is not proof of a full recalculation.
  Use a temporary isolated profile with `-env:UserInstallation=<temporary directory file URI>` rather than changing user macros or settings.

For any automated engine route, enforce a finite timeout, verify completion and a readable saved output, and close only the instance/process tree created by the task.
On timeout or failure, keep the authoritative workbook unchanged and report failure, never success from the existence of the original file.
If no usable engine is installed, preserve the formula candidate and state that calculated output is blocked.
Do not install an engine, change global profiles, refresh remote links, or substitute guessed numeric caches as part of routine workbook editing.

Verify using both formula and cached-value views, or direct worksheet XML for empty-string results:

1. Check expected formula coordinates/text, including shared/array ranges where applicable.
2. Check relevant cached results against independently expected outcomes, including at least the changed dependency path.
3. Detect real error-typed cells (`data_type == "e"` or XML `t="e"`), including newly introduced errors.
   A prose cell mentioning `#N/A` is not a formula error.
4. Treat `None` in a cached-value view conservatively.
   It can indicate an absent cache or a legitimate empty result, so inspect formula semantics and XML cache representation before claiming success.
   The catalog exporter rejects formula cells returning `None` in its cached-value view, so such a formula must be resolved compatibly before export.
5. Do not save with `openpyxl` after calculation if the consumer needs those caches, as that can remove them again.

This read-only check identifies formula caches that need investigation and actual cached error cells without changing the saved output:

```python
formulas = load_workbook(candidate, read_only=True, data_only=False)
values = load_workbook(candidate, read_only=True, data_only=True)
try:
    for sheet in formulas:
        cached = values[sheet.title]
        for row in sheet:
            for cell in row:
                result = cached[cell.coordinate]
                if result.data_type == "e":
                    print("error", sheet.title, cell.coordinate, result.value)
                if cell.data_type == "f" and result.value is None:
                    print("cache needs inspection", sheet.title, cell.coordinate)
finally:
    formulas.close()
    values.close()
```

An empty findings list does not establish freshness or correctness.
Compare the expected outcomes of the edited dependency path separately.

## Comparison evidence

For bounded content edits, compare every changed cell against the requested delta and ensure unrelated values/formulas remain unchanged.
Compare sheet order/visibility, table and filter definitions, merged ranges, validation/conditional-formatting rules and coverage, hyperlinks, comments, defined names, dimensions, styles, freeze panes, and print settings relevant to the source.
A ZIP member inventory catches missing parts but not changed payloads, and matching styles alone does not prove preservation.
When a schema or layout actually changes, use an available spreadsheet renderer or application to inspect affected sheets and report the scope of that inspection.
Do not claim visual QA from a successful parse.

## Primary references

- [openpyxl loading and saving](https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file): data-only, rich-text, VBA, links, and shape preservation limits.
- [openpyxl formulas](https://openpyxl.readthedocs.io/en/stable/simple_formulae.html): formulas are stored, not evaluated, and special formulas have range semantics.
- [openpyxl structural edits](https://openpyxl.readthedocs.io/en/stable/editing_worksheets.html): dependency management limits for insertion, deletion, and movement.
- [openpyxl comments](https://openpyxl.readthedocs.io/en/stable/comments.html): text/author support and loss of original formatting and dimensions.
- [Microsoft SpreadsheetML formulas](https://learn.microsoft.com/en-us/office/open-xml/spreadsheet/working-with-formulas): formula expressions and cached values.
- [Excel CalculateFullRebuild](https://learn.microsoft.com/en-us/office/vba/api/excel.application.calculatefullrebuild): full calculation and dependency rebuild for all open workbooks.
- [LibreOffice Recalculate Hard](https://help.libreoffice.org/latest/en-US/text/scalc/01/recalculate_hard.html): recalculation of all formula cells.
- [LibreOffice XCalculatable](https://api.libreoffice.org/docs/idl/ref/XCalculatable_8idl_source.html): UNO `calculateAll` recalculates all cells.
- [LibreOffice startup parameters](https://help.libreoffice.org/latest/en-US/text/shared/guide/start_parameters.html): Windows console executable, isolated profile, and conversion parameters.
