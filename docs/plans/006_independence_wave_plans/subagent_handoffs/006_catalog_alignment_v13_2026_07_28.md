# Event 006 catalog alignment v13

Date: 2026-07-28

## Scope and disposition

This handoff records the Event 006 catalog refresh after the current Independence Wave, evolution, cluster, SCN-008, and IW-012 source review. The workbook was loaded and saved in place, with the requested Event 006-facing values reasserted without changing their current player-facing text. Existing workbook structure, tables, data validation, and sheet dimensions were preserved.

The current source-of-truth and completion audits supersede the older catalog handoff's `To Be Reworked` snapshot. Event 006 and the Liberations cluster remain `In progress`; SCN-008 remains `Needs Testing`; the whole Event 006 implementation remains `HOLD / PARTIAL` pending runtime, balance, focus, scenario, league, achievement, and super-event evidence.

## Row-level alignment

- `Events!A7:M7` (Event ID `6`, Independence Wave): the static Event Details paragraph matches `chaosx.events_log.window.event_details.independence_wave`; `Evo I` through `Evo V` exactly join each current evolution title and body with one blank line; terminal scenario remains empty; type is `Minor Repeatable`, cluster is `2`, member severity is `Medium`, and status is `In progress`.
- `Clusters!A3:G3` (Cluster ID `2`, Liberations): name and details match the current Events Log cluster localisation; members remain `5, 6`; type is `Minor Repeatable`, chaos level is `1`, and status is `In progress`.
- `Scenarios!A9:F9` (`SCN-008`, Every Banner Rises): name, Sovereign Scatter premise, all eight selectable type names, all four `Low`/`Medium`/`High`/`Maximum` intensity paragraphs, and status `Needs Testing` match the current scenario localisation. The eight modes are Sovereign Scatter, Common Congress, Wars of Separation, Universal Belligerence: Former Hosts, Universal Belligerence: Neighboring Releases, Universal Belligerence: Nearby Nonleague States, Patron Worlds, and Great Partition.

## Event 006 design invariants checked

- Automatic wave counts are `Calm World 3`, `Gathering Storm 4`, `Rising Chaos 5`, `Chaos Tier 7`, `Totalen Chaos 10`, and `World Collapse 10`, matching `common/script_constants/006_independence_wave_constants.txt` and the wave-tuning matrix. These counts are not inserted into the generic Event Details mirror because that field must remain the exact player-facing event-detail paragraph.
- The five evolution mirrors use the final directions `The Manuals Cross the Border`, `Old Nations Wake`, `Flags Rise Behind the Barracks`, `The Sovereigns Take Their Seats`, and `No Border Is Final` from current localisation. No stale numeric range or working-label text remains in the workbook.
- IW-012's current package docs and audit describe a statically admitted ICE package with remaining live evidence boundaries; no package ID or route-specific implementation detail was added to the generic Event 006 catalog row, consistent with the accepted catalog direction.

## Validation and exports

- Workbook path: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
- Target rows checked: `Events!7`, `Clusters!3`, `Scenarios!9`; 16 key/status cells were reasserted and verified after save. No semantic cell delta was required because the workbook already matched current localisation.
- Workbook structure was preserved: `Events`/`Clusters`/`Scenarios` tables remain registered; data-validation counts remain `3/3/1`; sheet dimensions remain `1015x16`, `13x7`, and `12x6`; no formulas or error-like cells are present.
- `python .tools/export_event_catalog_csv.py` completed successfully after the workbook save and refreshed all three export-only snapshots: Events `257x13` (SHA-256 `daae98719a9d3b23b4cdbbad23fb913154a4f372f00babfa925a3f4864441aee`), Clusters `13x7` (SHA-256 `7cc6d9394240b3f69e39c4dd102a0c6b6b00978f26998a5bda7f96b696333a50`), and Scenarios `12x6` (SHA-256 `9a06c1b5099c0368239b3ab1db10f0a5c5bb4b2407749b78fa14950235941fe5`).

## Unresolved wording and status

No unresolved mirror wording was found. The runtime Event Details key appends dynamic rival-bloc lines; those dynamic lines remain intentionally unflattened in the static catalog summary. Statuses are deliberately not promoted while the accepted whole-event `HOLD / PARTIAL` boundary remains open.
