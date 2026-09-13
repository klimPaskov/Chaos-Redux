# Catalog workbook alignment prompt

Update the authoritative Chaos Redux event catalog workbook after Event 036 gameplay and final localisation are complete.

Use `chaosx_spreadsheet_doc_worker` with a complete context-free prompt and the spreadsheet skill.

Edit only:

```text
docs/spreadsheets/chaos_redux_events_catalog.xlsx
```

Do not edit the three CSV exports directly.

## Event row replacement

Replace the obsolete Event 036 Alien Spacecraft row with:

- Event ID `36`
- Chemical and Biological Weapons Convention
- Minor Fire-Once
- To Be Reworked only until implementation is complete, then the verified implementation status
- Chaos level `1`
- approved cluster `Diplomacy`
- member severity `High`
- complete player-facing event details from final in-game wording
- three evolution details aligned with Event Details
- recurring treaty and international program summary without implementation jargon

Do not retain the old alien technology description or Minor Repeatable classification.

## Cluster alignment

The supplied cluster export has no current cluster named Diplomacy.

Inspect the authoritative workbook and runtime cluster registry.

Create or reconcile the approved Diplomacy cluster row according to current project conventions.

Do not silently assign Event 036 to Diplomatic Panic.

Add Event 036 as a High-severity member with the correct minimum event level and any cluster-specific fields required by the workbook.

## Export

Preserve workbook structure, formatting, formulas, filters, and validation.

After saving successfully, run:

```text
python .tools/export_event_catalog_csv.py
```

Verify that the Events, Clusters, and Scenarios CSV snapshots were regenerated from the workbook.

Report the exact row changes, exported files, and any unresolved cluster-ID decision.
