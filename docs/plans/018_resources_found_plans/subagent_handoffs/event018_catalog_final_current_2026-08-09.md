# Event 018 catalog final-current audit

## Scope and verdict

This audit covered only Event 018 workbook rows and the linked Economy-positive cluster record in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, plus the export-only CSV refresh required by the repository contract.

Verdict: CONDITIONAL PASS.

The workbook now matches the parent-supplied final implementation target for Resources Found, its four evolution stages, its world-end wording, cluster 7, Medium severity, and Implemented status. The checked-in shared localisation still contains legacy `A Rich Find` and `Positive economic shocks...` values at `localisation/english/chaosx_event_names_l_english.yml:20` and `localisation/english/chaosx_gui_l_english.yml:411`, while the accepted Event 018 docs and implementation handoffs identify the final player-facing names as Resources Found and Economy (pos). Those localisation files are outside this spreadsheet-only scope and require parent/localisation-owner review before the catalog can be considered unconditional across every source surface.

## Workbook changes

Workbook path: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

Canonical Event 018 row: `Events!A19:M19`.

| Cell | Before | After |
| --- | --- | --- |
| `B19` | `A Rich Find` | `Resources Found` |
| `C19` | `Surveyors strike a major deposit in one of the country's states. The first find promises jobs, trade, and new industry, while later discoveries can turn the field into a boomtown, a diplomatic prize, or a threat rising from the deep workings.` | `Surveyors in an owned state discover a major strategic resource deposit. Repeated discoveries can deepen the same field, turning local prospecting into a long-lived question of development, labor, trade, and control.` |
| `D19` | `Veins Without End` plus the planning-era body | `Veins Without End: One field reveals several large deposits at once. Repeated finds of the same resource deepen its discovery ledger, while foreign buyers, claimants, and a negotiated demilitarized commission compete for access to the concentrated wealth.` |
| `E19` | `The Workings Turn Sick` plus the planning-era body | `The Workings Turn Sick: Sickness, corrosion, disappearances, and underground attacks spread through the lower workings. Investigation, containment, concealment, suspension, and permanent closure determine whether the field remains an economy or becomes a grave.` |
| `F19` | `The Breach Takes Shape` plus the planning-era body | `The Breach Takes Shape: A vast deposit of every standard resource draws the field far below safe workings. Public attacks, hunts, evacuation, partial closure, and a full sealing operation decide whether every registered discovery deposit is surrendered before the breach opens.` |
| `G19` | `The Oth-Kesh Emerge` plus the planning-era body | `The Oth-Kesh Emerge: The field becomes the origin chamber of the playable Oth-Kesh Host. Its armored broods draw strength from exploitation and captured resource anchors, attack every adjacent land neighbor, and prepare to carry the connected depths beyond their first continent.` |
| `I19` | Two-paragraph planning-era world-end text | `The World Opens Below: The first continent is no longer a contained theater. Stronger formations will emerge through resource-weighted footholds on distant continents at once.` |
| `K19` | blank | `7` |
| `L19` | blank | `Medium` |
| `M19` | `Playable` | `Implemented` |

`Events!A19`, `Events!J19`, and `Events!H19` were verified as `18`, `Minor Repeatable`, and intentional blank respectively and were not changed.

Canonical cluster 7 row: `Clusters!A10:G10`.

| Cell | Before | After |
| --- | --- | --- |
| `B10` | `Positive Economy` | `Economy (pos)` |
| `C10` | `Positive economic shocks can create lasting development choices through discoveries, investment, trade, and infrastructure growth.` | `Economy (pos) delivers beneficial economic shocks with persistent development choices. Resources Found is its medium-severity repeatable member: one discovery can mature into trade, investment, foreign pressure, or a cleanly closed field.` |
| `D10` | blank | `18` |
| `G10` | `Unavailable` | `Implemented` |

`Clusters!A10`, `Clusters!E10`, and `Clusters!F10` were verified as `7`, `Minor Repeatable`, and `1` and were not changed.

## Relationship audit

Event 018 is not present in the manual scenario catalog, which is correct because the accepted package defines a world-end branch inside the event rather than a separate triggerable scenario. No `Scenarios` row was added.

Evolution V remains intentionally blank. The accepted design has exactly four evolutions, with Evolution IV creating the Oth-Kesh Host and the world-end branch represented separately in `World-End Scenario`.

## Structure and render checks

The guarded workbook write started from SHA-256 `0ff9034168bd0dd000da1df98d3b53023d835be08bc436cd8b1d0464602aaff6` and produced SHA-256 `0929a7ab10fd2eee58722fea8b03301f377abc0f6c1657fa690c473dd50b2652`.

The workbook still has five expected sheets, tables `Events`, `Event_Clusters`, and `Manual_Scenarios`, no merged ranges, no formulas, the original dimensions, and the original data-validation counts of 3, 3, 1, 0, and 0 for `Events`, `Clusters`, `Scenarios`, `Info`, and `Legend`.

LibreOffice headless conversion produced a 54-page PDF without an error. Spot-rendered pages show `18 Resources Found` on the Events sheet and `7 Economy (pos)` with member `18` on the Clusters sheet. Text extraction confirms the four populated evolution cells, the intentional blank Evo V, `Minor Repeatable`, cluster `7`, `Medium`, and `Implemented` values.

## Export disposition

After the successful workbook save, `python .tools/export_event_catalog_csv.py` completed with `status: success`.

- `docs/spreadsheets/chaos_redux_events_catalog.csv`: 183 rows, 13 columns, SHA-256 `3a0da43a587d50753727700af1707b2a615bb9c2fc09fb6d8c67162886f7a9c1`.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`: 14 rows, 7 columns, SHA-256 `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`: 12 rows, 6 columns, SHA-256 `66ea4a5802862c1c72f0f3e8ead04cb4f1bfde5e62f88411e3b29f64cb5cf760`.

The CSV files were refreshed only by the exporter and were not edited directly.

## Blockers and needs_user_review

No workbook cell remains blocked or needs_user_review within the requested catalog surface. The external localisation contradiction described in the verdict is the only remaining condition. No gameplay, localisation, scripted localisation, asset, GUI, or scenario source files were edited, and no unrelated documentation was changed.

## Parent disposition

Both catalog-adjacent localisation findings were resolved after the spreadsheet audit. `chaosx.event_name.18` now reads `Resources Found`, and `chaosx.events_log.window.cluster_details.description.economy_positive` now matches the accepted Economy (pos) cluster wording in the workbook. Both localisation files retain UTF-8 BOM encoding. The Event 018 catalog surface therefore passes after this disposition; unrelated workbook rows and shared localisation edits remain outside this handoff.
