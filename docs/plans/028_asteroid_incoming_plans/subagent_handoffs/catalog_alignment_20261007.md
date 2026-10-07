# Event 028 catalog alignment handoff

Updated the authoritative workbook at `docs/spreadsheets/chaos_redux_events_catalog.xlsx` for Event 028, `Asteroid Incoming`.
Only `Events!C29`, `Events!D29`, and `Events!E29` were changed.
The three export-only CSV snapshots were regenerated with `python .tools/export_event_catalog_csv.py`.

## Source and row confirmation

The `Events` header row is row 1, with `ID`, `Event Name`, `Details`, `Evo I`, and `Evo II` in columns A–E.
Row 29 has ID 28 and name `Asteroid Incoming`.
The C29 text is the exact `asteroid_incoming.event_details.description` localisation string.
The D29 and E29 bodies come from `asteroid_incoming.evolution.fragmentation.body` and `asteroid_incoming.evolution.minerals.body`; colour formatting was removed, and constants were rendered as 3/6 fragments and 100%/20% armour.
The evolution titles and catalog prefixes preserve the queued plan wording.

## Workbook evidence

Read-only before-copy: `C:\Users\klimp\AppData\Local\Temp\chaos_redux_event028_catalog_yn1r2bto\chaos_redux_events_catalog.before.xlsx`.
Before-copy SHA-256: `a0d63c9d885cb5de3bbac3480a221a3c94a229d9a33c6682dc50533f643b58c9`.
Saved workbook SHA-256: `c02840d9089e8196d5b21f49058f550d55abccebdcc3a60b89255cddd4db9106`.
Reopening the saved workbook and comparing every stored cell value, type, style, format, hyperlink, and comment against the before-copy found exactly the three owned value changes listed below.
All formulas are unchanged; the workbook contains zero formulas, so formula recalculation was not needed.
Sheet names and dimensions, filters, tables, data validation, freeze panes, merged cells, row and column layout, named ranges, and ZIP member names match the before-copy.
The eleven pre-existing WIP cells were unchanged: `Events!C13`, `Events!I13`, `Events!L40`, `Events!L53`, `Clusters!A9`, `Cluster Memberships!A42`, `Cluster Memberships!A43`, `Scenarios!C11`, `Scenarios!C14`, `Scenarios!D14`, and `Scenarios!E14`.
At final read-only Git comparison, the current `HEAD` workbook LFS object was `ce78dfe015137337527f383cbdf15d6ff3cb60d8d041c5416039e054d41a613e`; the worktree workbook differed from it at only `Events!C29`, `Events!D29`, and `Events!E29`.
No Git staging or commit operation was performed by this worker.

## Exact cell changes

| Cell | Before | After |
| --- | --- | --- |
| `Events!C29` | A global, fire-once asteroid episode records a locked impact coordinate, its cross-border footprint, actual deaths and destruction, atmospheric dust, fragment sites, recovery decisions, and control of extraordinary mineral sites. The opening choice presents three distinct country and state coordinates plus a genuine near miss; a confirmed impact locks the coordinate for two days and destroys the centre state while three land rings are damaged across borders, leaving a permanent crater. A miss records no physical consequence. | Astronomers identify three possible impact sites and one near-miss course. A strike destroys its centre, damages three surrounding land rings, spreads atmospheric dust, and opens national recovery work. Global Fragmentation adds further impact sites, while Extraordinary Minerals makes control of those sites strategically valuable. The near miss causes no physical damage. |
| `Events!D29` | Global Fragmentation — Chaos Tier, 600 Chaos, Stage 1: The chosen main body still strikes, while separated fragments hit several valid states worldwide with smaller damage rings and additional dust. | Global Fragmentation — Chaos Tier, 600 Chaos, Stage 1: The altered trajectory breaks the asteroid apart. The main body still strikes the chosen state, while 3 to 6 smaller fragments, rising with Chaos, strike populated states elsewhere in the world. Each fragment leaves its own crater and two rings of damage, and adds to the atmospheric dust. |
| `Events!E29` | Extraordinary Minerals — Totalen Chaos, 800 Chaos, Stage 1, requires Global Fragmentation: Main and fragment crater control grants transferable land-division armour bonuses, with plus 100 percent from the main crater and plus 20 percent per fragment site. | Extraordinary Minerals — Totalen Chaos, 800 Chaos, Stage 1, requires Global Fragmentation: The impact sites hold extraordinary material. The country controlling the main crater gains 100% land-division armour, and each controlled fragment site adds 20%. Craters become military objectives with their own security, survey, fortification, and rival actions. |

Cell style IDs remained C29 `30`, D29 `35`, and E29 `36`; their text types and formats were unchanged.
`J29` remains `Major` (style `66`), and `M29` remains `Needs Testing` (style `70`).
The status contract remains “enabled in the default queue and awaiting live-game verification”; this handoff does not claim gameplay approval or event completion.

## Export results

The exporter completed successfully and all CSV rows and columns were compared against the corresponding workbook sheets using the exporter's widths and row-trimming rules.

| Export | Rows including header | Columns | SHA-256 | Change from captured pre-export snapshot |
| --- | ---: | ---: | --- | --- |
| `chaos_redux_events_catalog.csv` | 166 | 13 | `9da9e59e1eb488f3415e5bef0f69895de55221ea715c3a1fe86c237e04d0eea2` | Row 29, ID 28: `Details`, `Evo I`, and `Evo II` changed; no rows added or removed. |
| `chaos_redux_clusters_catalog.csv` | 20 | 8 | `21a0df3e818b37f9716e6092d8f46a14ca1297121f2ed32ffb01c4a34d18b638` | No content changes; hash matches the pre-export snapshot. |
| `chaos_redux_scenarios_catalog.csv` | 17 | 6 | `95d667fa6c1d5e874b0c51c61efb465b814ae484f6dc48616680238ec85dc5e9` | No content changes; hash matches the pre-export snapshot. |

The exported Event 028 row matches the three final workbook strings and retains Type `Major` and Status `Needs Testing`.
No gameplay, localisation, GUI, asset, or other catalog source files were edited.
