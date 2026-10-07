# Event 012 Gods Catalog Alignment Handoff

Date: 2026-10-07.

Disposition: Event 012 Details, SCN-011 scenario descriptions, and all four runtime World-end event-log outcome sections are aligned to current in-game wording. The dynamic one-branch super-event paragraph has been removed from the World-End Scenario field; no review status remains open.

## Changed files and cells

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is the only edited catalog source.
- `docs/spreadsheets/chaos_redux_events_catalog.csv`, `docs/spreadsheets/chaos_redux_clusters_catalog.csv`, and `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` were overwritten by the required exporter; none was edited directly.
- This handoff file records the requested evidence and out-of-schema notes.
- No localisation or gameplay source was edited, and no Git operation was run.

On the `Events` sheet, row 13 is Event 12, "Africa Is One." Cell `C13` now exactly matches `chaosx.events_log.window.event_details.africa` in `localisation/english/012_african_union_l_english.yml`, including the Gods of Africa paragraph: "Once the continent is consolidated, its government can proclaim the Gods of Africa: great powers are asked for tribute, defiance is punished, loyal partners are protected, and every account is settled when the continent is secured."

Cell `I13` now contains only the four runtime World-end event-log outcomes: "The World: Unanimous Continental Union," "The World: Last Standing Resolution," "The World: Continental Campaign," and "The World Is One," each with its full corresponding detail text. The first three sections match `africa.event_log.the_world.*.title` and `.detail` in `localisation/english/012_africa_event_log_l_english.yml`; the fourth matches `chaosx.events_log.world_end.africa_the_world.title` and `.details` in `localisation/english/chaosx_gui_l_english.yml`. Dynamic actor names in the first three details remain represented by the readable catalog placeholder "The African host." The outdated relationship-history sentence and one-branch `ONE WORLD REMAINS` super-event paragraph were removed.

On the `Scenarios` sheet, row 11 is SCN-011, "Africa Is One." Cell `C11` now contains only the two current triggerable scenario descriptions, labelled by their existing type names: `Africa Is One` and `World Is One`. I removed the extra implementation-status paragraph, which described callbacks, package wiring, proof, identity, and victory behavior and does not appear in the scenario UI. The remaining sentences match `chaosx.scenarios.africa.desc.africa_is_one` and `.desc.world_is_one` in `localisation/english/chaosx_gui_l_english.yml`.

The exact source keys `africa.evolution.1.body`, `.2.body`, and `.3.body` in `localisation/english/012_africa_evolutions_l_english.yml` already matched `Events!D13:F13`; they remain unchanged. The current SCN-011 Type Options and Intensity Scaling words already match the live UI keys `chaosx.scenarios.type.africa.africa_is_one`, `.world_is_one`, and `chaosx.scenarios.africa.impact.low`, `.medium`, `.high`, and `.maximum`; they remain unchanged. The catalog omits only the `§R` and `§!` color-control markers from the intensity text so the field remains readable while preserving all displayed words.

Event 70 remains unassigned: `Events!A71` is `70`, and `B71:M71` remain blank. Its Status was not set to `Unavailable` or any other value. Event 12 and SCN-011 remain `Needs Testing`; neither status changed.

## Workbook and export evidence

### First pass, before the user-directed I13 resolution

Before the edit, the workbook and all three working CSV snapshots were copied byte-for-byte and hashed outside the repository at `C:\Users\klimp\AppData\Local\Temp\chaos_redux_event_catalog_20261007_52ywbw7c`. The saved workbook reopened successfully. Its only semantic value changes are `Events!C13`, `Events!I13`, and `Scenarios!C11`; every other row and cell value matches the initial snapshot. All style IDs, table ranges, data-validation ranges, conditional formatting counts, filters, freeze panes, sheet dimensions, and workbook row topology match the baseline. The workbook contains no formulas, so recalculation was not needed.

| File | Before SHA-256 | After SHA-256 |
| --- | --- | --- |
| `chaos_redux_events_catalog.xlsx` | `3420053b9cedc45b7bde32562efd00c0169ed74f9a9589ca482370ba8a641d67` | `c485a5019b068baa8bb29564599c605bf43f787afbba22eb3a357469110b06d1` |
| `chaos_redux_events_catalog.csv` | `465050976a1134e57945cec56e95232e6c54fa2a8b4c5a3b569b0d638230d2c0` | `c358e0e0c04976166fafeea0eeb949847f59dd4cdf939e8b99f2e2258d2a3ca3` |
| `chaos_redux_clusters_catalog.csv` | `276964d65cad082f678c7bbfff4d8e89d99930b1f3707b1d8dd07ba1e3755d8a` | `276964d65cad082f678c7bbfff4d8e89d99930b1f3707b1d8dd07ba1e3755d8a` |
| `chaos_redux_scenarios_catalog.csv` | `cdc1c288a885d6b62225d7d84ed6af560f4267322d74a7a4cf4b28a7d16b124d` | `bd5b705b6090b917c8dbeca0cba70c44cec81a43077de671f62d9e4bf4546315` |

First-pass exporter command run from the mod root: `python .tools/export_event_catalog_csv.py`.

Exporter result: `status: success`; Events exported 166 rows by 13 columns with SHA-256 `c358e0e0c04976166fafeea0eeb949847f59dd4cdf939e8b99f2e2258d2a3ca3`; Clusters exported 20 rows by 8 columns with SHA-256 `276964d65cad082f678c7bbfff4d8e89d99930b1f3707b1d8dd07ba1e3755d8a`; Scenarios exported 17 rows by 6 columns with SHA-256 `bd5b705b6090b917c8dbeca0cba70c44cec81a43077de671f62d9e4bf4546315`.

Semantic comparison against the initial working CSV snapshots found only Event 12 `Details` and `World-End Scenario` in the Events CSV, and SCN-011 `Details` in the Scenarios CSV. The Clusters CSV has no semantic changes. Before export, every CSV row already matched its workbook source, including Event 42 in the `Various Anomalies` cluster and SCN-016 "Global Jihad"; both remain present and unchanged. All other event, cluster, and scenario rows remain unchanged.

## Follow-up resolution: runtime World-end outcomes in `Events!I13`

The getter `GetAfricaSuperEventTerminalProtocolClause` in `common/scripted_localisation/012_africa_super_event_scripted_localisation.txt` checks the terminal flags in this order: unanimous union, last standing, continental campaign, then the untriggered fallback `africa_super_event_terminal_protocol_recorded`. The exact localized leaves are:

- `africa_super_event_terminal_unanimous_union`: "a unanimous union protocol accepted by every required continental actor".
- `africa_super_event_terminal_last_standing`: "a last-standing settlement after the recorded continental rivals were defeated".
- `africa_super_event_terminal_continental_campaign`: "a continental campaign followed by a public peace settlement".
- `africa_super_event_terminal_protocol_recorded`: "a final protocol founded on consent and a public settlement".

The first three leaves map by outcome to the current event-log title/detail pairs `africa.event_log.the_world.unanimous_union`, `africa.event_log.the_world.last_standing`, and `africa.event_log.the_world.continental_campaign`. The fallback recorded-protocol case is represented by the general runtime world-end pair `chaosx.events_log.world_end.africa_the_world.title` and `.details`, titled "The World Is One." The first three event-log details use a dynamic host name; the workbook keeps the readable placeholder "The African host" while preserving the remaining display words exactly.

I13 now contains those four runtime event-log sections only. I removed the `ONE WORLD REMAINS` super-event paragraph because its single base title was followed by only the recorded-protocol fallback phrase, incorrectly presenting one reachable clause as universal and duplicating the final world-end log. The field follows its existing multi-ending format and preserves each current event-log title and full detail. No new schema, notes field, or approval step was added.

Exact I13 value before this follow-up:

```text
The World: Unanimous Continental Union

The African host completed the constitutional agreement for a unanimous continental union and leads The World resolution. Continental governments now follow the settlement's public terms.

The World: Last Standing Resolution

The African host survived as the last continental government and leads The World resolution. Its final settlement defines the new order.

The World: Continental Campaign

The African host won the final continental campaign and leads the new world order. The settlement binds the continent's rival governments under its terms.

ONE WORLD REMAINS

The last continental rivalries have ended. The African host reached The World through a final protocol founded on consent and a public settlement. Its constitution, surviving obligations, and treatment of defeated rivals now define the final order.

The World Is One

The African Union has absorbed or defeated every rival government. It proclaims The World, binds the surviving territories to one constitutional order, and ends the age of separate states.
```

Exact I13 value after this follow-up:

```text
The World: Unanimous Continental Union

The African host completed the constitutional agreement for a unanimous continental union and leads The World resolution. Continental governments now follow the settlement's public terms.

The World: Last Standing Resolution

The African host survived as the last continental government and leads The World resolution. Its final settlement defines the new order.

The World: Continental Campaign

The African host won the final continental campaign and leads the new world order. The settlement binds the continent's rival governments under its terms.

The World Is One

The African Union has absorbed or defeated every rival government. It proclaims The World, binds the surviving territories to one constitutional order, and ends the age of separate states.
```

The follow-up changed only `Events!I13` in the workbook and only Event 12 `World-End Scenario` in the Events CSV. The Clusters and Scenarios CSVs remain byte-identical to the second-pass baseline; Event 42 and SCN-016 remain unchanged. Reopened-workbook semantic comparison found no other changed cell, and style IDs, tables, validations, filters, panes, conditional formatting, dimensions, and formulas are unchanged; there are no formulas to recalculate.

Second-pass before/after SHA-256 values:

| File | Before SHA-256 | Final SHA-256 |
| --- | --- | --- |
| `chaos_redux_events_catalog.xlsx` | `c485a5019b068baa8bb29564599c605bf43f787afbba22eb3a357469110b06d1` | `5bae3142f732bda3fc2946d546515647dc7022212949724c8ff2b04f83533cd0` |
| `chaos_redux_events_catalog.csv` | `c358e0e0c04976166fafeea0eeb949847f59dd4cdf939e8b99f2e2258d2a3ca3` | `8abba06e5c464360bfcbc34180423aaf42a11e24ea3542d5fe16104d4719acc2` |
| `chaos_redux_clusters_catalog.csv` | `276964d65cad082f678c7bbfff4d8e89d99930b1f3707b1d8dd07ba1e3755d8a` | `276964d65cad082f678c7bbfff4d8e89d99930b1f3707b1d8dd07ba1e3755d8a` |
| `chaos_redux_scenarios_catalog.csv` | `bd5b705b6090b917c8dbeca0cba70c44cec81a43077de671f62d9e4bf4546315` | `bd5b705b6090b917c8dbeca0cba70c44cec81a43077de671f62d9e4bf4546315` |

Second-pass exporter command run from the mod root: `python .tools/export_event_catalog_csv.py`.

Second-pass exporter result: `status: success`; Events exported 166 rows by 13 columns with SHA-256 `8abba06e5c464360bfcbc34180423aaf42a11e24ea3542d5fe16104d4719acc2`; Clusters exported 20 rows by 8 columns with SHA-256 `276964d65cad082f678c7bbfff4d8e89d99930b1f3707b1d8dd07ba1e3755d8a`; Scenarios exported 17 rows by 6 columns with SHA-256 `bd5b705b6090b917c8dbeca0cba70c44cec81a43077de671f62d9e4bf4546315`. The only semantic CSV delta in this pass was Event 12, row 13, `World-End Scenario`.

## Full inline summary of pending Event 012 notes without a catalog surface

- Final settlement grades each surviving participant Favored, Respected, Distrusted, or Enemy from its whole tribute record, including fulfilled-demand ratio and streaks, material sent, voluntary, emergency, and late-campaign help, war, occupation, broken agreements, defiance, reconciliation, and Africa's doctrine. Favored and Respected governments are owed equipment and fuel from Africa's own stocks. Those supplies scale to material sent and Africa's Strength and are delivered in batches through "Deliver settlement support."
- A treaty breach means a broken agreement: agreed tribute terms, a protection compact, accepted reconciliation, or renewed recognition. The pending notes identify `chaosx.nr12.616.t` as "An Agreement Broken by War."
- Four Gods achievements are listed as implemented: "Long Obedience," "Survive Defiance," "Continental Provision," and "The Careful Gambler," with names and descriptions under `africa_gods_*_NAME` and `_DESC` in `localisation/english/012_africa_achievements_l_english.yml`. No achievement rows or notes surface exists in this workbook.
- The activation news event is "Africa Proclaims the Gods of Africa" (`chaosx.nr12.617.t`). The global-credibility super-event is slot 118, "THE WORLD TAKES AFRICA AT ITS WORD" (`chaosx_super_event.118.t`), with its cue and the complete 104-second White House performance of "Nkosi Sikelel' iAfrika." The pending notes say it fires once at active global reach, including an activation that was already qualified. No news or super-event catalog surface exists.
- Recognition wording: "Recognition improves relations both ways, each recognising major power adds to Africa's Strength, and the world order remembers who recognised Africa." (`gods_of_africa_focus_recognize_voice_tt`). Territory wording: "Africa can demand that a foreign government hand back, by name, up to 3 African core states it controls. This demand comes before any request for material." (`gods_of_africa_focus_return_soil_tt`). Ending sponsorship wording: "Africa can demand that a foreign government withdraw the guarantee, military access or volunteers it gives a country Africa is fighting." (`gods_of_africa_focus_end_sponsorship_tt`).
- With Evolution III and Continental Strength or more, Security Oaths can demand military access, a non-aggression pact, or a guarantee of Africa's independence from a free government outside its faction that does not already give it (`gods_of_africa_focus_security_oaths_tt`). The former family label "security access" no longer applies; the current family is "an end to our support for Africa's enemies."
- "The Last Sentence" requires Africa's Strength and Chaos plus the participant's Wrath and record to reach their extreme gates. Africa then gives a final ultimatum: within 60 days the participant must return Africa's land and make peace or pay an extraordinary settlement. Refusal or expiry brings disaster and waves of civilian deaths across up to three of its states (`gods_of_africa_focus_last_sentence_tt`). The pending notes list "Africa's Final Ultimatum" (`chaosx.nr12.618.t`), "Arms for the Offender's Enemies" (`chaosx.nr12.619.t`), and the log entries "Africa Strikes [country] Across the Nation," "Africa's Final Ultimatum to [country]," and "Catastrophe Falls on [country]" under `africa.event_log.gods.*`.
- "No Sanctuary for Occupiers" lets Africa claim the African core states held by a foreign government, gain a war goal to recover them, and arm the African claimant of that land (`gods_of_africa_focus_no_sanctuary_for_occupiers`). The pending notes also list decisions "Send the African Expedition," "Pledge a Final Shipment," "Speak for Africa at the Council," and "No Sanctuary for Occupiers," plus reports "The African Expedition Arrives" (`chaosx.nr12.620.t`) and "Africa Claims Its Land" (`chaosx.nr12.621.t`).
- "Sign the Support Agreement" sends the first instalment immediately and each later instalment every 30 days; agreed terms break if an instalment cannot be paid on its day (`gods_of_africa_sign_support_agreement`). For the response count, intermediate shipments update the mission, and the agreement closes with one report of material sent and the balance still owed (`gods_of_africa_response_support_summary`).
- A host retaining its national focus tree receives "A Programme for the Charter" (`chaosx.nr12.1211.t`) with "Plan the government around the Charter." and "Keep the national programme for now." A Charter League Court decision, "Adopt the Continental Programme," replaces that tree with The African Continental Charter while preserving completed effects and completed Charter focuses (`africa_adopt_continental_programme_tt`). A generic-tree host receives the Charter directly, and South Africa keeps its own tree.

## Parent shared-workbook publication

After the worker finished, another agent changed unrelated workbook cells for the intelligence cluster and SCN-019.
The parent compared the live workbook against the worker's initial snapshot and confirmed that all three Event 012/SCN-011 changes remain intact.
The published workbook candidate is constructed from the captured Git HEAD workbook with only `Events!C13`, `Events!I13`, and `Scenarios!C11` applied from the reviewed current source.
Only the matching Event 12 and SCN-011 hunks from exporter output enter the isolated commit index.
The live workbook and all other working CSV changes remain untouched, including Event 42, SCN-016 and the concurrent intelligence/Assassin edits.
The hashes above identify the worker's own completed snapshots; they are not claims that later shared working bytes still match those snapshots.
No unrelated staged workbook entry was present during capture, and publication guards both the working hashes and real index entries before reconciliation.
