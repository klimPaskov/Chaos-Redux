# Prompt for `chaosx_spreadsheet_doc_worker`

Work with no inherited conversation context. Update only the authoritative Chaos Redux event catalog workbook after Event 38 implementation facts and final player-facing wording are available.

Read the spreadsheet skill, `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, final Event 38 event-log and Event Details localisation, final public evolution wording, final public Holy World wording, final triggerable scenario wording, and final cluster wording. Read `20_event_logs_details_catalog_localisation.md` only as a field map. Do not read or edit unrelated gameplay, broad repo docs, assets, or other spreadsheets.

Update Event 38 with:

- ID `38`
- name `Malta Crusaders`
- type `Minor Fire-Once`
- Chaos level `1`
- status supported by the final implementation evidence
- cluster ID `6`, Formables, member severity High
- public details matching in-game Event Details premise
- three public evolution fields matching in-game wording
- public world-end field for The Holy World only
- no hidden Teutonic or Atlantis spoilers

Register or update the manual **Believers vs Nonbelievers** scenario using the final collision-checked scenario ID, details, type controls, intensity wording, and status. Do not use the working `SCN-015` value unless the final registry confirms it.

Preserve workbook structure, formats, formulas, filters, validation, and unrelated rows. Save the workbook, then run:

```text
python .tools/export_event_catalog_csv.py
```

Never edit the three CSV exports directly. If export fails, report it and leave the workbook as the only attempted catalog edit. Write a compact handoff listing workbook sheet and row targets, fields changed, exact mirrored localisation keys, export result, and unresolved mismatch.
