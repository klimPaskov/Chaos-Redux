# Doctrine workbook and other repository spreadsheets

`docs/spreadsheets/doctrines.xlsx` is independent of the event catalog.
Do not apply event statuses, Legend colors, event columns, or the catalog exporter to it.
Its established structure includes an `Overview`, per-doctrine sheets, and `vanilla_land_officer_spirits`.
Treat these as discovery hints rather than a fixed list of required sheets.

## Preserve the document architecture

The Overview has named columns for doctrine key, doctrine name, description, track keys, and subdoctrine count.
Doctrine sheets contain section headings, descriptive prose, script-effect text, track sections, and merged presentation rows.
They are not flat tables with the same header in row 1.
The officer-spirit sheet has Category, Spirit Key, Name, Description, Script Source, and name/description localisation key/file columns.

- Match a doctrine by its key and a section by its actual heading or script identifier.
  Do not use the current row count, repeated spacing, or freeze-pane position as a schema contract.
- Preserve section order, merges, wrapped multiline script content, fonts, widths, row heights, freeze panes, and source/localisation provenance columns.
  Edit only the anchor of a merged range.
- If approved content additions change an Overview count or track list, reconcile those summary fields with the detailed sections.
  Do not convert established literal counts to formulas unless the requested workbook design calls for that change.
- For another workbook, derive its identities and presentation from its own headers, sections, and template.
  Avoid replacing it with a generic dataframe export or borrowing the event-catalog schema.

## Git LFS source bytes

An XLSX path can contain a Git LFS text pointer rather than ZIP bytes.
For read-only inspection, locate the object via the repository's actual Git common directory and `lfs/objects/<first two hash characters>/<next two>/<full oid>`.
Verify its SHA-256 and declared size against the pointer, then read from bytes without changing the working tree.
Do not assume `.git` is a directory in a worktree.
If the object is absent, report that inspection is blocked on the real workbook bytes or use an authorized normal LFS retrieval route.
Never manufacture a substitute workbook to make the path load successfully.
