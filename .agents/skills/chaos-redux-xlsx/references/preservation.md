# Preservation and calculation

## Source bytes

For any workbook, check that the source is a ZIP, not a Git LFS text pointer.
For read-only pointer inspection, resolve the repository's actual Git common directory and `lfs/objects/<oid first two>/<oid next two>/<full oid>`; do not assume `.git` is a directory.
Verify object SHA-256 and size against the pointer before reading its bytes.
If bytes are unavailable, report the gap or use an authorized LFS retrieval route; never manufacture a replacement workbook.

Inspect ZIP members, content types, relationships, and load warnings before choosing a writer.
Charts/drawings, controls, pivots/slicers, external links, embedded objects, custom XML, extensions, and signatures need feature-specific preservation checks; their presence alone does not establish support or loss.
Warning-free loading is not proof of preservation.
`openpyxl` retains ordinary comment text/author but can lose comment formatting, position, and dimensions.
For actual macro-enabled files use `keep_vba=True` and the original extension; this does not prove preservation of every feature.
Read-only loading is for inspection, not a complete feature audit.

## Existing literal cell recipe

Use this for an ordinary supported workbook after inspecting its features.
Parameters are the sheet, a dictionary of stable key headers/values (including composite keys), target header, expected old value, and replacement text.
The header can be below a title row and columns can move.
An empty replacement string intentionally clears the cell to `None` while retaining its style.
This creates and verifies a candidate only; perform the comparison below and source-hash check before replacing the authority.

```python
from pathlib import Path
from openpyxl import load_workbook

def edit_literal(source, candidate, sheet_name, key, header, expected, text):
    source, candidate = Path(source), Path(candidate)
    if source.resolve() == candidate.resolve() or not key or not isinstance(text, str):
        raise ValueError("Use a separate candidate, nonempty key, and literal text")
    wb = load_workbook(source, data_only=False, keep_links=True, rich_text=True)
    try:
        ws = wb[sheet_name]
        needed = set(key) | {header}
        header_rows = []
        for row in ws.iter_rows():
            labels = [cell.value for cell in row]
            if all(name in labels for name in needed):
                header_rows.append(row)
        if len(header_rows) != 1:
            raise ValueError("Missing or ambiguous header row")
        row = header_rows[0]
        cols = {}
        for name in needed:
            matches = [cell.column for cell in row if cell.value == name]
            if len(matches) != 1:
                raise ValueError(f"Duplicate header: {name}")
            cols[name] = matches[0]
        matches = [r[0].row for r in ws.iter_rows(min_row=row[0].row + 1)
                   if all(r[cols[name] - 1].value == value for name, value in key.items())]
        if len(matches) != 1:
            raise ValueError(f"Expected one row for {key}, found {len(matches)}")
        cell = ws.cell(matches[0], cols[header])
        if cell.value != expected or cell.data_type in {"f", "e"}:
            raise ValueError(f"Old value/type conflict at {cell.coordinate}")
        coordinate = cell.coordinate
        cell.value = text or None
        if text:
            cell.data_type = "s"  # Keep '=...' and '#N/A' prose literal.
        wb.save(candidate)
    finally:
        wb.close()
    check = load_workbook(candidate, data_only=False, keep_links=True, rich_text=True)
    try:
        cell = check[sheet_name][coordinate]
        if cell.value != (text or None) or (text and cell.data_type != "s"):
            raise ValueError("Candidate does not contain the intended literal")
    finally:
        check.close()
    return coordinate
```

This example requires an `openpyxl` version supporting `rich_text=True` and is not a formula/structure editor or a full preservation audit.
For new presentation rows, copy individual style components with `copy.copy` from a matching row; style copying does not extend validation or conditional-formatting coverage.

## Narrow OOXML or structure edits

If a full round trip loses features during a bounded edit, patch only declared cell nodes in a candidate ZIP:

- Resolve the sheet through `xl/workbook.xml` and relationships, not a guessed `sheet1.xml`.
- Check cell reference, expected value/type, and style; decode shared strings for matching without changing an entry used by unrelated cells.
  Replacement literal text can use `inlineStr`; preserve attributes, namespaces, whitespace/newlines (`xml:space="preserve"`), and unrelated subtrees.
- Copy untouched member payloads and metadata; avoid broad regex or XML serialization that loses extension content.
  Compare every undeclared member's bytes and unaffected content within each edited part.

`insert_rows`, `delete_cols`, and `move_range` do not repair all dependencies.
For scoped structure changes, explicitly reconcile formulas/names, table/filter ranges, validation and conditional-formatting coverage, merges, print areas, charts, and consumers affected by the change.
Shared, array, spill, and data-table formulas have range semantics; do not treat their cells as independent scalar formulas.
Formula/dependency edits also require cache invalidation and appropriate calculation-chain handling.
Report signature invalidation when editing a signed package.

## Formulas and caches

Formula text (`<f>`) and cached output (`<v>`) are separate.
`openpyxl` stores formulas without evaluating them and commonly clears caches on save; calculation-on-open flags are requests, not results.
Recalculate when formulas/dependencies change or the writer removes caches a consumer needs.
Literal-only workbooks need no engine; a narrow unrelated XML edit can preserve unaffected caches.
Never save a `data_only=True` workbook or resave calculated output with `openpyxl` when caches must survive.

Scan formula and cached views with aligned streaming rows, without reparsing a read-only sheet for each cell:

```python
from openpyxl import load_workbook

formulas = load_workbook(candidate, read_only=True, data_only=False)
try:
    values = load_workbook(candidate, read_only=True, data_only=True)
    try:
        for sheet in formulas:
            bounds = dict(min_row=1, max_row=sheet.max_row,
                          min_col=1, max_col=sheet.max_column)
            for row, cached_row in zip(sheet.iter_rows(**bounds),
                                       values[sheet.title].iter_rows(**bounds)):
                for cell, result in zip(row, cached_row):
                    if result.data_type == "e":
                        print("error", sheet.title, result.coordinate, result.value)
                    if cell.data_type == "f" and result.value is None:
                        print("cache needs inspection", sheet.title, cell.coordinate)
    finally:
        values.close()
finally:
    formulas.close()
```

Only error-typed cells are errors; literal prose mentioning `#N/A` is not.
`None` can mean a missing cache or a legitimate empty result; inspect formula semantics and XML before deciding.
The catalog exporter rejects that cached view as unresolved.
Nonempty caches and no scan findings do not prove freshness: compare formula coordinates/text and relevant cached results with independently expected outcomes along the changed dependency path.

Use an installed engine on a candidate if needed:

- Excel: a separate instance, macros/link updates disabled, candidate only, `Application.CalculateFullRebuild`, wait for calculation completion, save/close/quit.
- LibreOffice: Recalculate Hard or a working UNO `calculateAll` route, then save XLSX; `--convert-to` alone is not calculation proof.
  Use an isolated temporary `-env:UserInstallation=<directory file URI>` profile.

Use a finite timeout and verify a readable saved output; close only the instance/processes created by the task.
Failure or no usable engine leaves calculated output blocked and the authority untouched.
Do not install engines, alter global profiles, refresh remote links, or invent caches for routine edits.

## Comparison evidence

A content edit passes when reopened changed values/types equal the declared delta, unrelated values/formulas remain unchanged, and relevant source features below match.
Compare semantic properties rather than just style IDs or file hashes:

- Sheet order/visibility; tables/filter definitions; merges; defined names; validation and conditional-formatting rules and covered ranges.
- Cell fonts/fills/borders/alignment/number formats/protection; widths/heights; freeze panes; print settings; hyperlink targets and supported comment content.
- Source-specific package features identified during inspection, including relationships and drawing/extension parts.

ZIP member names detect missing parts, not silent changes; inspect affected features and, for narrow OOXML, unchanged payloads too.
For intentional structure/layout changes, identify expected differences, verify updated coverage, and inspect affected sheets with a renderer/application if available.
A parse proves readability, not visual appearance or formula correctness; report any unverified feature, appearance, or calculation requirement explicitly.

## Primary references

- [openpyxl loading and saving](https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file): rich text, VBA, links, and shape limits.
- [openpyxl formulas](https://openpyxl.readthedocs.io/en/stable/simple_formulae.html): evaluation and special formulas.
- [openpyxl structural edits](https://openpyxl.readthedocs.io/en/stable/editing_worksheets.html): dependency limits.
- [openpyxl comments](https://openpyxl.readthedocs.io/en/stable/comments.html): appearance loss.
- [Microsoft SpreadsheetML formulas](https://learn.microsoft.com/en-us/office/open-xml/spreadsheet/working-with-formulas): expressions and caches.
- [Excel CalculateFullRebuild](https://learn.microsoft.com/en-us/office/vba/api/excel.application.calculatefullrebuild).
- [LibreOffice Recalculate Hard](https://help.libreoffice.org/latest/en-US/text/scalc/01/recalculate_hard.html).
- [LibreOffice XCalculatable](https://api.libreoffice.org/docs/idl/ref/XCalculatable_8idl_source.html): UNO `calculateAll`.
- [LibreOffice startup parameters](https://help.libreoffice.org/latest/en-US/text/shared/guide/start_parameters.html): isolated profiles.
