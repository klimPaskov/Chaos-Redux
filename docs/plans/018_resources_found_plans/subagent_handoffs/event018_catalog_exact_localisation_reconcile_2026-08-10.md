# Event 018 exact localisation catalog reconciliation

## Scope and disposition

`docs/spreadsheets/chaos_redux_events_catalog.xlsx` was reconciled only in `Events!C19:G19`.
The five cells now exactly mirror `resources_found.event_details.description` and `resources_found.evolution.stage_1.body` through `resources_found.evolution.stage_4.body` from `localisation/english/018_resources_found_system_l_english.yml`.

No gameplay, localisation, scripted localisation, CSV, or unrelated workbook cells were edited directly.

The complete 27-file `docs/specs/018_resources_found_specs/` package, the current Event 018 localisation file, and the existing catalog handoffs were read before the workbook edit.

## Exact before and after values

| Cell | Before | After |
| --- | --- | --- |
| `C19` | `Surveyors in an owned state discover a major strategic resource deposit. Repeated discoveries can deepen the same field, turning local prospecting into a long-lived question of development, labor, trade, and control.` | `Surveyors have struck a major deposit in one of the country's states. The first find promises jobs, trade, and new industry. Repeated discoveries can turn the same field into a boomtown, a diplomatic prize, or something much harder to control.` |
| `D19` | `Veins Without End: One field reveals several large deposits at once. Repeated finds of the same resource deepen its discovery ledger, while foreign buyers, claimants, and a negotiated demilitarized commission compete for access to the concentrated wealth.` | `One field keeps giving. New deposits appear beneath old workings, and foreign buyers, rival claimants, and would-be peacekeepers all want a share of the wealth.` |
| `E19` | `The Workings Turn Sick: Sickness, corrosion, disappearances, and underground attacks spread through the lower workings. Investigation, containment, concealment, suspension, and permanent closure determine whether the field remains an economy or becomes a grave.` | `Miners fall sick, metal corrodes overnight, people vanish, and something attacks in the lower workings. The country must investigate, contain the danger, or close the field before the boomtown becomes a grave.` |
| `F19` | `The Breach Takes Shape: A vast deposit of every standard resource draws the field far below safe workings. Public attacks, hunts, evacuation, partial closure, and a full sealing operation decide whether every registered discovery deposit is surrendered before the breach opens.` | `A huge mixed deposit pulls the workings far below safe ground. Attacks reach the surface, and the country must hunt what escaped, evacuate the field, or seal away every valuable shaft before the breach fully opens.` |
| `G19` | `The Oth-Kesh Emerge: The field becomes the origin chamber of the playable Oth-Kesh Host. Its armored broods draw strength from exploitation and captured resource anchors, attack every adjacent land neighbor, and prepare to carry the connected depths beyond their first continent.` | `The field opens into an Oth-Kesh origin chamber. Armored broods pour through the workings, feed on rich deposits, and attack every country they can reach as they search for roads beneath the next continent.` |

The pre-save workbook SHA-256 was `363b7edfc50c5bba0c5af8b47e7817ec129ffa732669dc8b8db55b91c4d9002a` and the post-save SHA-256 was `03fabc7ccad065d9f02e2ba7dc39ebb1efc5bdcd0966b32f509d95835271f4b0`.

## Export and validation

After saving the workbook, `python .tools/export_event_catalog_csv.py` completed with `status: success`.
It refreshed the three export-only snapshots: `chaos_redux_events_catalog.csv` (183 rows, 13 columns, SHA-256 `0f94392454399c86eeeaa6fa6cbc5aa0e53263fd484d48d4862c0ccacd43f645`), `chaos_redux_clusters_catalog.csv` (14 rows, 7 columns, SHA-256 `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`), and `chaos_redux_scenarios_catalog.csv` (12 rows, 6 columns, SHA-256 `66ea4a5802862c1c72f0f3e8ead04cb4f1bfde5e62f88411e3b29f64cb5cf760`).

`openpyxl` reopened the saved workbook and confirmed the exact five target values, five expected sheets, original `928 x 13` Events dimensions, three Events data validations, the `Events` table, zero formulas, and zero stored Excel error values.

The XLSX ZIP integrity test returned `None` from `ZipFile.testzip()` across all 19 package members.

The exported Event 018 CSV row was checked and its `Details`, `Evo I`, `Evo II`, `Evo III`, and `Evo IV` fields exactly matched `C19:G19`.

LibreOffice headless conversion produced a PDF successfully, and text extraction confirmed the Event 018 description and all four body strings in the rendered Events sheet.

## Concurrent binary-file caveat and blockers

The target-cell guard observed the expected current values before writing, so no concurrent target-cell change was detected.
Because `openpyxl` reserializes the XLSX ZIP package, a binary diff or package hash change can include serialization metadata beyond the five semantic cell assignments even when workbook structure and non-target values remain intact.

No blocked or `needs_user_review` cells remain within the requested `Events!C19:G19` surface.
