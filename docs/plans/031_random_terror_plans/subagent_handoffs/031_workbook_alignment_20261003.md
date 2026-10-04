# Event 31 workbook alignment

## Disposition and acceptance basis

Disposition: implemented for the catalog wording and scenario row.

The active user goal explicitly requires the authoritative XLSX update and catalog exporter, preserves the Event 31 identity and evolution names, and forbids registering Internal Fracture before acceptance of its members.

The named `chaosx_spreadsheet_doc_worker` ran with `fork_context=false` and returned a completed result on 2026-10-03.

## Workbook changes

The worker updated `docs/spreadsheets/chaos_redux_events_catalog.xlsx` from the existing working-tree workbook.

`Events!C32:I32` now mirrors the exact Event 31 detail, evolution-title and description, and world-end-title and description localisation.

`Events!L32` is blank, removing the premature cluster assignment.

The event name, Minor Repeatable classification, Chaos level 1, and `To Be Reworked` status remain intact.

`Scenarios!A16:F16` contains SCN-016, Global Jihad, the exact scenario description, all five selector types and their descriptions, all four intensity descriptions, and `Needs Testing` status.

The existing SCN-018 row is preserved at row 17.

The scenario table is `A1:F17` and its status-validation range is `F2:F17`.

## Parent verification

The parent reopened the saved workbook and read all Event 31 fields, both scenario rows, the table metadata, and the validation metadata.

The saved values match the worker's handoff and the named localisation keys.

The workbook contains zero formula cells, so formula recalculation is inapplicable to this edit.

The worker ran `python .tools/export_event_catalog_csv.py` successfully after saving.

The exporter returned 166 Events rows with 13 columns, 20 Clusters rows with eight columns, and 17 Scenarios rows with six columns.

The Clusters export hash did not change during this update, and no Internal Fracture row was registered.

The live script constants confirm Fallout at scenario ID 14, Missile Age at 15, and Global Jihad at 16 in `common/script_constants/chaosx_triggerable_scenarios_constants.txt`.

The existing workbook SCN-014 row describes Assassin Network instead of the live Fallout registry entry.

That pre-existing catalog-to-runtime discrepancy was observed during this Event 31 verification and remains outside this bounded row update.

It does not invalidate the SCN-016 allocation, but it must not be used as proof that the complete scenario catalog matches the live registry.

## Hash evidence

| File | Before worker | After worker |
| --- | --- | --- |
| Workbook | `18e0e76f58b284a95a6761aebcc9304ab03e6ff967448aca8c290c6c93616c47` | `878f5808a8e236b069766b3b7a53a7fdd25c1b29d4f74ae82a3a8dfaff7bb9f6` |
| Events export | `c6a926ba2312993c790a57cbcefb8b11108554f01ef449bc1c2e1a96648788ea` | `26be9657e2954d5a4b87511481a5be6e5e047922fc31074e6375a180c67abaf7` |
| Clusters export | `276964d65cad082f678c7bbfff4d8e89d99930b1f3707b1d8dd07ba1e3755d8a` | `276964d65cad082f678c7bbfff4d8e89d99930b1f3707b1d8dd07ba1e3755d8a` |
| Scenarios export | `8b944de19817b3887eac22e3d12437e62990273c8b0db1c6f27928f349d4b2e7` | `a7a26d10435c451cd555c6e72749a2dda54b20d62a07fda7d2cdb5a8a7065d7e` |

## Commit ownership and limits

The workbook and two exports already contained unrelated local changes when the worker began.

They remain in the shared working tree because a whole-file binary commit would also include unrelated work.

The status labels do not claim Event 31 completion or playable approval.

Final catalog reconciliation must be repeated if the remaining gameplay or localisation repairs change these public fields.
