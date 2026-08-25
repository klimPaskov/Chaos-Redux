# Event 016 catalog alignment handoff

Date: 2026-08-26

Status: complete for the bounded Event 016 workbook alignment pass. No runtime completion claim is made.

## Workbook changes

Authoritative workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

- Sheet `Events`, row 17, Event ID `16`, `Brilliant Scientist`: audited `C17` against the current Event Details localisation and retained the base wording plus the conditional D’Rhondan sovereignty clause exposed by `GetDhrondanEventDetailClause`.
- Sheet `Events`, row 17: audited `D17:G17` against the four current evolution descriptions, with exactly Evolutions I–IV present. `H17` (`Evo V`) remains blank.
- Sheet `Events`, row 17: audited `I17` against the current `Laboratory World` and `The Strategic Singularity` Event Log title/detail pairs.
- Sheet `Events`, row 17: retained `J17 = Minor Fire-Once`, `K17 = 1`, blank `L17` (`Cluster ID`) and `M17` (`Member Severity`), and `N17 = Needs Testing`. The status remains conservative because targeted/live acceptance is open and the current catalog contract keeps Events 1–20 at `Needs Testing` until playable approval.
- Sheet `Events`, row 177: restored the absorbed concept record in the existing formatted blank row: `B177 = Crazy Scientist (absorbed into Event 016)`, `C177 = The Crazy Scientist concept is absorbed into Brilliant Scientist and its Kruger Directorate.`, and `N177 = Unavailable`. No standalone event chain was introduced.

No Event 016 member was found in the `Clusters` sheet. No cluster row or unrelated workbook row was changed.

## Export evidence

After saving the workbook, ran `python .tools/export_event_catalog_csv.py` from the mod root. The exporter succeeded and refreshed all three snapshots:

- Events: 177 rows, 14 columns, SHA-256 `8d7b5506a219a92c6c14fa54811eba533f7a1a12765383203b62f4fe206d7c16`.
- Clusters: 14 rows, 7 columns, SHA-256 `647c9206de61a70d7a0d7adf0740dc97c81c8e63d01fefac6549b430b666425b`.
- Scenarios: 12 rows, 6 columns, SHA-256 `52a80f59912841d0b046f889a40bdec66b452d5cc92c3f486245de56f08559cd`.

The export-only CSVs were refreshed by the exporter and were not edited directly.

## Validation and omissions

A focused workbook/export comparison passed for the Event Details text, D’Rhondan clause, four evolution descriptions, blank Evo V, both world-end routes, minor fire-once type, chaos level, blank cluster fields, and the absorbed `Crazy Scientist` record. The current Alien Infantry model/entity/action/audio blocker, DHR dynamic state-transfer and live acceptance boundaries, quantitative balance evidence, and broader Event 016 runtime acceptance remain open and are not represented as completed in the catalog.
