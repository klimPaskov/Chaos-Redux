# Event 016 catalog alignment re-audit

Date: 2026-08-03

## Result

The editable workbook `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is already aligned with the current Event 016 player-facing wording, so no workbook cells or unrelated rows were changed.

The Event 016 status remains `Partially Available`, and no live-game acceptance claim is made.

## Audited rows and fields

- `Events` row 17, Event ID `16`, `Brilliant Scientist`.
- `C17` matches `chaosx.events_log.window.event_details.brilliant_scientist` exactly, including the two-paragraph break.
- `D17:G17` match the current four evolution title/body pairs: `National Scientific Ascendancy`, `The International Scientific Contest`, `Forbidden and Autonomous Science`, and `Sovereign Science`.
- `H17` (`Evo V`) is blank because Event 016 has exactly four logged evolutions.
- `I17` combines the current Event Log `Laboratory World` and `The Strategic Singularity` title/detail wording exactly, including both paragraph breaks.
- `J17` remains `Minor Fire-Once`; `K17` (cluster) and `L17` (member severity) remain blank.
- `M17` remains `Partially Available`.
- `Events` row 177 remains `Crazy Scientist (absorbed into Event 016)` with the absorbed Kruger Directorate detail and `Unavailable` status; no standalone chain is reintroduced.

## Source wording and validation

- Read `localisation/english/chaosx_event_names_l_english.yml` for the Event 016 name.
- Read `localisation/english/016_brilliant_scientist_evolutions_l_english.yml` for Event Details and all four evolution entries.
- Read `localisation/english/chaosx_gui_l_english.yml` for both world-end title/detail pairs.
- Compared the workbook cells with the source strings using `openpyxl`; all audited mirror fields matched exactly.
- Ran `python .tools/export_event_catalog_csv.py` successfully from the mod root; the exporter reported 183 Event rows, 14 Cluster rows, and 13 Scenario rows with SHA-256 values `583315550846824eee087cbf579596f3a98ad76d755a4c8abccd4b0b2ecfeb7d`, `db80ff3e3bd3387d34292bbaf7d769852cde41302ca1afd7dffd173837ba4c75`, and `1ab7ee1189ba99a8167f2cb98f8e61b698b6adda8b3c648a8b49cc0d67a87708` respectively.
- The exporter produced no tracked content diff because the workbook and snapshots were already aligned.

## Remaining blockers

Broader Event 016 quantitative balance evidence, targeted transfer and cleanup validation, native CBRN callback integration, deferred seven 3D packages, and live consumer acceptance remain outside this workbook-only pass.
