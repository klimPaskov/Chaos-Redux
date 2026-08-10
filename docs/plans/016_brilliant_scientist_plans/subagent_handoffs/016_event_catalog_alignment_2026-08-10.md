# Event 016 catalog alignment handoff

Date: 2026-08-10

Status: no workbook change required.

## Scope

The editable source checked was `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. This pass was limited to Event 016's main row, Event Details and evolution wording, its no-cluster classification, and the absorbed `Crazy Scientist` catalog row.

## Evidence and exact cells

- `Events!A17:M17` is the sole row with ID `16`.
- `Events!B17` is `Brilliant Scientist`, matching `chaosx.event_name.16`.
- `Events!C17` exactly matches `chaosx.events_log.window.event_details.brilliant_scientist`.
- `Events!D17:G17` each exactly match the corresponding in-game evolution title followed by its detail text from `brilliant_scientist.evolution.1` through `.4`.
- `Events!H17` is blank. The implementation exposes only four Event 016 evolution stages, so no Evolution V entry is added.
- `Events!J17` remains `Minor Fire-Once`.
- `Events!K17` and `Events!L17` remain blank. Event 016 is not a cluster member and no new cluster is added.
- `Events!M17` remains `Partially Available`, consistent with the rejected and unwired Portal Raider model/entity/actions/sounds while the counters remain wired.
- The absorbed concept remains represented only by `Events!B177:C177` as `Crazy Scientist (absorbed into Event 016)` and `The Crazy Scientist concept is absorbed into Brilliant Scientist and its Kruger Directorate.`, with `Events!M177 = Unavailable`.
- No `Clusters!D*` member cell contains Event ID `16`.

## Export and checks

No workbook cell changed, so the workbook was not saved and `python .tools/export_event_catalog_csv.py` was not run. The export-only CSV snapshots were not edited. This preserves concurrent workbook and CSV changes already present in the worktree.

The focused openpyxl/YAML comparison reported one Event 016 row, exact main name and details, exact Evo I–IV composites, blank Evo V, `Minor Fire-Once`, blank cluster/severity, no cluster member reference, and the expected absorbed `Crazy Scientist` row.

## Remaining review boundary

Portal Raider API behavior, Black Plague access through Biological Weapons Theory and the Mengele registry, and rejected visual model wiring are implementation surfaces outside the catalog fields checked here. No Event 016 evolution, cluster, or additional event row is implied by those changes.
