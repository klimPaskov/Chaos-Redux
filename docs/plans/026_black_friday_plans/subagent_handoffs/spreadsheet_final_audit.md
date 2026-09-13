# Event 26 spreadsheet final audit

Audit date: 2026-08-30, refreshed after the parent localisation follow-up.

Authoritative workbook checked: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

Only the Event 26 details cell was refreshed to mirror the final Event Details premise, and no unrelated workbook rows were touched.

## Events sheet

The sole Event 26 row is Excel row 27.

- `A27` (`ID`): `26`.
- `B27` (`Event Name`): `Black Friday`.
- `C27` (`Details`): exactly matches `black_friday.event_detail.premise` in `localisation/english/026_black_friday_l_english.yml`: `At Gathering Storm and 200 chaos, Black Friday opens a global one-day Friday sale that lowers government, military, intelligence, and procurement costs by 50 percent. The sale waits for the first eligible Friday, and Evolution I can raise that day's snapshot to 75 percent at 600 chaos or higher.`
- `D27` (`Evo I`): exactly matches `black_friday.evolution.1.body` in `localisation/english/026_black_friday_l_english.yml`: `At 600 chaos, the Friday price sheets cut eligible costs by 75 percent when this evolution is enabled. The stronger rate is fixed when the sale begins and lasts until the next daily tick.`
- `E27:H27` (`Evo II` through `Evo V`): blank, with no additional evolution wording present.
- `I27` (`World-End Scenario`): blank.
- `J27` (`Type`): `Minor Fire-Once`.
- `K27` (`Chaos level`): `1`.
- `L27` (`Cluster ID`): blank.
- `M27` (`Member Severity`): blank.
- `N27` (`Status`): `Needs Testing`.

Duplicate checks found exactly one workbook row with `ID = 26`, exactly one workbook row named `Black Friday`, and zero non-empty Events rows with a blank ID. The Clusters sheet has no member list containing Event 26, so the blank cluster fields remain correct.

## Export

The prescribed exporter completed successfully after the audit:

```text
python .tools/export_event_catalog_csv.py
```

It regenerated the export-only snapshots from the workbook. The exact final SHA-256 values are:

- Workbook: `c8b3a4d2ad30f1c50135e51d642ca3f06034b4ef1d2f87d8f02b2a3893aef42a`.
- Events CSV: `ede52357aa8ae88b9f36d427100d4293728aae1f9d476386afce81ecd4425053`.
- Clusters CSV: `83b4b51268824a6974ba893c91196fc86ba509f5c4d130879d16cc5256527e50`.
- Scenarios CSV: `05a5e47238cf23e12a3ac6ba09720106460b42a212b553563f1069e70f139eee`.

## Mismatches and blockers

No spreadsheet mismatch was found after the refresh. Live validation was not performed, so `N27` intentionally remains `Needs Testing`.
