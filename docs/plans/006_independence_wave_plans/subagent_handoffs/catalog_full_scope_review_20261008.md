# Event 006 full-scope catalog review, 2026-10-08

Disposition: the initial read-only reconciliation is complete, and its parent-accepted three-cell SCN-008 follow-up is implemented and reviewed at source.
The initial observations below remain dated evidence; the implementation follow-up records the subsequent workbook save and export.
The Event 006 goal remains active and incomplete.

## Authority and review scope

The current resume packet and source-of-truth map identify the integrated Event 006 checkpoint and retain the full objective as active and incomplete. The prior `signature_catalog_review_20261007.md` checked only the Event 006 name, detail, and five evolution mirrors, with no workbook edit or export. This review extends the transcription check to both associated clusters, SCN-008, and the selected records in all three existing exports.

The current implementation facts supplied for this review are the regional source commit `416688b8963ea0b1a47e3c8682b8125455cfca40`, signature and FORM-17/32/36/37 source commit `9e2837f8edc1633cd8e96415366821ca5dc16886`, incident snapshot source commit `00191fdc2e741307846268192392f91d6bf0bac5`, and documentation checkpoint `0a76b693bca00fb4e80de5148e5ffa71a857ac48`.

The allowed sources read for this reconciliation were `AGENTS.md`, the `chaos-redux-subagents`, `chaos-redux-events`, and `chaos-redux-xlsx` skills, the XLSX catalog contract, `docs/spreadsheets/README.md`, the current Event 006 resume packet and source-of-truth map, the prior signature catalog review, the current workbook and export snapshots, the SCN-008 scenario entry, and the exact localisation and scripted-localisation sources named below.

## Workbook structure and selected records

The workbook is a real XLSX ZIP with sheets ordered `Events`, `Clusters`, `Cluster Memberships`, `Scenarios`, and `Legend`. The workbook contains no formulas. Its current tables are `Events!A1:M1014`, `Clusters!A1:H20`, `Cluster Memberships!A1:G77`, and `Scenarios!A1:F17`. The `Legend` sheet occupies `A1:D24` and has no table.

`Events` headers are `ID`, `Event Name`, `Details`, `Evo I`, `Evo II`, `Evo III`, `Evo IV`, `Evo V`, `World-End Scenario`, `Type`, `Chaos level`, `Cluster ID`, and `Status`. Event 006 is `Events!A7:M7`, keyed by ID `6`.

`Clusters` headers are `Cluster ID`, `Cluster Name`, `Details`, `Members (ID)`, `Member Severities`, `Type`, `Chaos level`, and `Status`. The associated records are `Clusters!A3:H3`, cluster `2` (`Liberations`), and `Clusters!A17:H17`, cluster `16` (`Domestic Unrest`).

`Cluster Memberships` headers are `Cluster ID`, `Cluster Name`, `Slot`, `Event ID`, `Event Name`, `Severity`, and `Membership Notes`. Cluster 2 occupies rows 11-15 with slots 1-5, including Event 6 in slots 2-4 at Low, Medium, and High severity. Cluster 16 occupies rows 67-70 with slots 1, 2, 4, and 5, including Event 6 at High severity in slot 2. Both Clusters aggregate ID and severity sequences exactly match their membership rows in Slot order. Event 6's distinct cluster list in `Events!L7` is `2, 16`.

`Scenarios` headers are `Scenario ID`, `Scenario Name`, `Details`, `Type Options`, `Intensity Scaling`, and `Status`. SCN-008 is `Scenarios!A8:F8`, keyed by `SCN-008` and named `Every Banner Rises`.

## Event 006 row result

`Events!B7` exactly matches `chaosx.event_name.6` at `localisation/english/chaosx_event_names_l_english.yml:8`.

`Events!C7` exactly matches `chaosx.events_log.window.event_details.independence_wave` at `localisation/english/chaosx_gui_l_english.yml:1117`. The Event Log detail dispatcher selects that key for Event 006 at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:6761-6763`.

`Events!D7:H7` exactly match `independence_wave.evolution.1.body` through `.5.body` at `localisation/english/006_independence_wave_evolution_l_english.yml:12,14,16,18,20`. The Event Log evolution dispatcher selects those bodies at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:9489-9508`.

`Events!I7` remains blank. The scoped Event 006 localisation and Event Log dispatcher search found no Event 006-owned public terminal-branch key. The blank is retained, and any newly identified public terminal branch would reopen this field.

`Events!J7:M7` remain `Minor Repeatable`, `1`, `2, 16`, and `Needs Testing`. No Event 006 status or classification change is proposed.

## Cluster results

Cluster 2 is fully aligned for this scoped row. `Clusters!B3` exactly matches `chaosx.event_cluster.liberations.name` at `localisation/english/chaosx_gui_l_english.yml:893`, and `Clusters!C3` exactly matches `chaosx.events_log.window.cluster_details.description.liberations` at `localisation/english/chaosx_gui_l_english.yml:419`. The selected-cluster name and description dispatchers route the Liberations ID to those keys at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:12439-12465,12620-12646`. The repeated Event 6 memberships and aggregate lists match in the workbook.

Cluster 16 needs source-owner review. `Clusters!B17` and `C17` textually match the defined `chaosx.event_cluster.domestic_unrest.name` and `chaosx.events_log.window.cluster_details.description.domestic_unrest` keys at `localisation/english/chaosx_gui_l_english.yml:436,910`. However, the Event Log `GetEventsLogSelectedClusterName` dispatcher has no `domestic_unrest` branch and falls through to `chaosx.event_cluster.invalid.name` at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:12439-12539`. The `GetEventsLogSelectedClusterDescription` dispatcher has no `domestic_unrest` branch and falls through to the generic description at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:12620-12720`. The initial read-only disposition flagged `Clusters!B17:C17` as `needs_user_review`. The parent follow-up below supersedes that catalog-cell disposition: the workbook wording matches the defined accepted keys, while runtime integration remains a shared-queue source gap. No replacement wording or gameplay/localisation patch is proposed here.

Cluster 2 remains `Partially Available` and cluster 16 remains `Needs Testing`. Their status cells are unchanged.

## SCN-008 source mapping and proposed cells

`Scenarios!B8` exactly matches `chaosx.scenarios.independence_wave.name` at `localisation/english/006_independence_wave_scenario_l_english.yml:2`. The scenario selector resolves that name for the Independence Wave ID at `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt:50-85`, and the GUI uses it for the title at `interface/chaosx.gui:2822`.

The GUI displays the selected mode's description through `GetTriggerableScenarioSelectedDesc` at `interface/chaosx.gui:2835`. Its eight source keys and display names are defined at `localisation/english/006_independence_wave_scenario_l_english.yml:5-21`, with dispatch at `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt:337-480`. The workbook's current `C8` is a general paraphrase that does not match any selected mode description and leaves seven mode descriptions out.

The GUI displays the selected type through `GetTriggerableScenarioTypeName` at `interface/chaosx.gui:2999`. The current `D8` uses five option names different from the displayed names. The exact displayed sequence is `Sovereign Scatter, Open Congress, Separation Wars, Host Wars, Neighbor Wars, Outsider Wars, Patron Worlds, Great Partition`.

The intensity labels `Low`, `Medium`, `High`, and `Maximum` are selected by `GetTriggerableScenarioIntensityName` at `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt:769-790`, displayed at `interface/chaosx.gui:2963`, and localised at `localisation/english/chaosx_gui_l_english.yml:180-183`.

The GUI displays the intensity warning through `GetTriggerableScenarioWarning` at `interface/chaosx.gui:3022`. Its four Event 006 warning values are dispatched at `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt:1216-1321` and localised at `localisation/english/006_independence_wave_scenario_l_english.yml:23-26`. The current `E8` paraphrases each warning and adds a launch-readiness statement that is not part of the intensity warning.

The following exact values are the proposed workbook delta for the catalog owner. The type and intensity labels separate current UI choices, and each body is copied from the selected-mode or selected-intensity key.

Proposed `Scenarios!C8`:

```text
Sovereign Scatter: Every viable independence movement breaks away. Hosts keep a protected remnant, each new state gets its own starting territory, and none joins a league or faction. Intensity changes territory, forces, and pressure.

Open Congress: Every viable independence movement breaks away from a protected host. The new states join an informal congress, and higher intensity strengthens its charter and shared reserve.

Separation Wars: Every viable independence movement breaks away. A new state able to confront its former host may open one war of separation. The others receive a regional threat mission.

Host Wars: Every viable independence movement breaks away. Each new state may open one war against its former host. Hosts keep their homelands, and wars that cannot start become regional threat missions.

Neighbor Wars: Every viable independence movement breaks away. Each new state may open one war against a neighboring state released in the same crisis. Each state is targeted once, so no all-against-all cascade follows.

Outsider Wars: Every viable independence movement breaks away. Each new state may open one war against a nearby independent state outside the League and every faction. Each target is chosen once and distance keeps the crisis regional.

Patron Worlds: Every viable independence movement breaks away. Each new state seeks one reachable major patron, favoring shared ideology and regional proximity. Intensity scales influence, aid, and recognition.

Great Partition: Every viable independence movement breaks away. Each host keeps one protected remnant, preferring its capital, then a safe core state. Higher intensity adds the next tier of territory, border pressure, claims, and ambitions.
```

Proposed `Scenarios!D8`:

```text
Sovereign Scatter, Open Congress, Separation Wars, Host Wars, Neighbor Wars, Outsider Wars, Patron Worlds, Great Partition
```

Proposed `Scenarios!E8`:

```text
Low: Each release gets only its starting territory, fragile defenses, scarce stocks, weak institutions, low recognition, and severe instability.

Medium: Releases receive compact territory, militia and border formations, baseline institutions, and ordinary route access.

High: Releases receive wider territory where borders allow, armed forces, stronger depots and officers, firmer institutions, and faster ambitions.

Maximum: Releases receive the largest territory and forces, rare support where their route allows it, high-chaos access, early formable discovery, and aggressive AI.
```

`Scenarios!F8` remains `Needs Testing`. The `.80` scenario entry is defined at `events/006_independence_wave.txt:709-722`. The `.81` `No Banner Rises` title, failure text, and option are at `localisation/english/006_independence_wave_scenario_l_english.yml:36-39`. This failure result has no separate field in the manual-scenario schema and does not warrant a new workbook row or column.

## Export snapshot parity at the read-only review baseline

The three current CSVs were parsed read-only and compared to the selected workbook records, using the XLSX as the authority. Headers and all selected values matched: Events ID `6`, Clusters IDs `2` and `16`, and Scenarios ID `SCN-008`. This confirms workbook-to-snapshot parity for the selected records, not source-localisation parity for the three proposed SCN-008 cells or the cluster 16 dispatch gap.

At the initial read-only review, the workbook was not saved, so `python .tools/export_event_catalog_csv.py` was not run. No exporter output existed at that baseline. The parent-authorized follow-up below records the later successful working export.

| File | SHA-256 at baseline start | SHA-256 at baseline end |
| --- | --- | --- |
| `chaos_redux_events_catalog.xlsx` | `C945A81B16454DE68468F73D43348612828DF76EAE463973626990AF06A91A29` | `C945A81B16454DE68468F73D43348612828DF76EAE463973626990AF06A91A29` |
| `chaos_redux_events_catalog.csv` | `4E151015DC928D6F69183EB40E4E15FB5EC0A81A0D0DCD972E42689A20AA2801` | `4E151015DC928D6F69183EB40E4E15FB5EC0A81A0D0D972E42689A20AA2801` |
| `chaos_redux_clusters_catalog.csv` | `97C6A331E832519E87A075D6F9B13744B4249245D56D7B58162188F0ADBC7106` | `97C6A331E832519E87A075D6F9B13744B4249245D56D7B58162188F0ADBC7106` |
| `chaos_redux_scenarios_catalog.csv` | `95D667FA6C1D5E874B0C51C61EFB465B814AE484F6DC48616680238EC85DC5E9` | `95D667FA6C1D5E874B0C51C61EFB465B814AE484F6DC48616680238EC85DC5E9` |

## Pending note dispositions

The current note section classifies D3, D4, D5, D7, D13, D15-D17, and D19-D34 package, formable, incident, milestone, leader, and route metadata as `source implemented; no mapped catalog field`, while retaining the dated acceptance and implementation history. D9's `.81` failure result title, body, and option likewise have no catalog field. D16's five mapped evolution-detail cells were checked separately and already match.

D35-D43 report titles, manual-launch explanations, status-window labels, project reservations, appointment behavior, and aggregate member replies have no dedicated catalog field. The inherited D35-D43 working-tree block was preserved byte-for-byte. Its mapped Event Details and evolution wording has been checked above. The initial read-only review flagged cluster 16's mapped cells for `needs_user_review`; the parent follow-up below supersedes that catalog-cell disposition and records the runtime integration as a shared-queue source gap.

D25 and D29 contain historical Hadhramaut and Comoros inclusion claims. They remain visible with their dates and are superseded by D34's dated correction on 2026-10-05.

Event 006 and SCN-008 remain `Needs Testing`. No playable status or native acceptance is claimed. The parent owns workbook review and any shared-tree commit of these documentation changes.

## Parent-accepted implementation follow-up, 2026-10-08

The parent accepted the exact proposed strings above for `Scenarios!C8`, `D8`, and `E8` within the active catalog-alignment goal. Both the current workbook and the HEAD LFS workbook were independently opened and SCN-008 was located by its `Scenario ID` value. In both files the scenario is on row 8, but the edit route resolved the row and columns from the actual headers and ID.

The current authoritative workbook was rebuilt from `.git/event6_catalog_current_before.xlsx` using a narrow OOXML edit of only the three inline-string cells in the Scenarios worksheet. The current workbook now has SHA-256 `878b605394504b57b760dd0f0ca059e133192dfbc54fcc6a085336c3349b56d3` and is 95,203 bytes. Its immutable beforecopy has SHA-256 `c945a81b16454de68468f73d43348612828df76eae463973626990af06a91a29` and is 94,935 bytes. The final compare-and-swap check matched that beforecopy immediately before replacement.

The isolated HEAD source was read at commit `0761d7150f5624d2e7dc80338d9ef1ccab55c370` and obtained with `git show HEAD:docs/spreadsheets/chaos_redux_events_catalog.xlsx` followed by `git lfs smudge`. The LFS pointer OID and beforecopy SHA-256 are both `eff8d25bec7441fb80118d28df484d214f5268b5814a5e265e134e84520f8d5b`, at 94,936 bytes. The private HEAD candidate `.git/event6_catalog_head_candidate.xlsx` has SHA-256 `8a68ee16ba833f5216b12ed4db685e3d0efa22709c2b7d93aa34487dcd231d0f` and is 95,204 bytes. It contains only the same three SCN-008 cell changes relative to the resolved HEAD workbook. The current-based candidate `.git/event6_catalog_current_candidate.xlsx` matches the current authoritative workbook's final hash.

Both candidate comparisons found only the three intended cell-value differences. `Scenarios!C8`, `D8`, and `E8` retain style ID 52, and `Scenarios!F8` remains `Needs Testing`. Event 006's `Events!M7` remains `Needs Testing`. No other workbook cell, formula, sheet, table, validation, conditional-formatting rule, merge, style, comment, or relationship changed. The ZIP member list remains the same. In both candidates every ZIP payload outside `xl/worksheets/sheet4.xml` is byte-identical to its own base, and restoring the three target cell nodes reconstructs that worksheet payload exactly. The current workbook's comments, VML drawings, and other package features remain byte-identical to the current beforecopy.

The current workbook had pre-existing raw-package differences from HEAD in `docProps/core.xml`, `xl/worksheets/sheet1.xml`, and `xl/worksheets/sheet3.xml`. Parsed XML for those differences had no semantic cell or style differences. The current-based candidate preserves those exact current payloads. The HEAD candidate remains isolated from that working-copy package state so the parent can apply the clean-pointer LFS patch through its isolated-index workflow.

The required `python .tools/export_event_catalog_csv.py` run completed with status `success` after the authoritative workbook save. Full parsed parity passed for each working export: Events 166 rows by 13 columns, Clusters 20 rows by 8 columns, and Scenarios 17 rows by 6 columns. The working export hashes before and after the update are:

| Export | SHA-256 before | SHA-256 after |
| --- | --- | --- |
| `chaos_redux_events_catalog.csv` | `4e151015dc928d6f69183eb40e4e15fb5ec0a81a0d0dcd972e42689a20aa2801` | `4e151015dc928d6f69183eb40e4e15fb5ec0a81a0d0dcd972e42689a20aa2801` |
| `chaos_redux_clusters_catalog.csv` | `97c6a331e832519e87a075d6f9b13744b4249245d56d7b58162188f0adbc7106` | `97c6a331e832519e87a075d6f9b13744b4249245d56d7b58162188f0adbc7106` |
| `chaos_redux_scenarios_catalog.csv` | `95d667fa6c1d5e874b0c51c61efb465b814ae484f6dc48616680238ec85dc5e9` | `8900b01fe7ba94351bb352d9f780d6f348f7ae3b0b4c4daf7a086e21b3cb5927` |

The parent-authorized private export run for `.git/event6_catalog_head_candidate.xlsx` succeeded under `.git/event6_catalog_head_exports`. All three private exports parse back to their candidate workbook sheets. The HEAD-based Scenarios CSV has the same SHA-256 as the working Scenarios CSV because the HEAD and current workbook rows matched before this three-cell update.

Parent disposition for cluster 16: the workbook cells `Clusters!B17:C17` already match the defined accepted wording and were left unchanged. The parent found no `event_cluster_id` constant for ID 16, with existing constants for IDs 1-12 and 20, and no Event 006 specification authority to invent a full Domestic Unrest runtime package. Keep that integration as a shared-queue source gap for its owner. This is not a remaining workbook wording mismatch or a `needs_user_review` cell disposition.

The D25 and D29 Hadhramaut/Comoros statements remain as dated history and are superseded by D34's dated correction. The inherited D35-D43 block remains byte-for-byte preserved, with SHA-256 `98dbfef332708a8133a93351e2d06cff48141c76e96666aa31ec4d83725e3397` for its retained suffix. No Event, Cluster, or other Scenario row was edited. No status was promoted. No Git index, ref, or commit was changed. The parent owns the isolated-index LFS clean-pointer patch and review of the private HEAD candidate.

## Parent publication review

The parent independently confirmed that the HEAD-based candidate changes only `Scenarios!C8`, `D8` and `E8`, preserves every other cell/style, and changes only the Scenarios worksheet ZIP payload.
The HEAD-based candidate and working Scenarios export are byte-identical.
The scoped commit uses the candidate's LFS object `8a68ee16ba833f5216b12ed4db685e3d0efa22709c2b7d93aa34487dcd231d0f`, while the authoritative working copy retains its pre-existing comment-package state and hash `878b605394504b57b760dd0f0ca059e133192dfbc54fcc6a085336c3349b56d3`.
The parent adopts the related inherited D35-D43 note after reviewing its complete diff, with the original historical acceptance and no-workbook-edit wording preserved.
No foreign cell or package metadata is included in this commit.
