# Event 039 catalog reconciliation, 2026-10-07

Updated the authoritative workbook at `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and regenerated its three export-only CSV snapshots.

## Cell deltas

| Sheet | Cell | Before | After |
| --- | --- | --- | --- |
| Clusters | A9 | `8` | `20` |
| Events | L40 | text `8` | text `20` |
| Events | L53 | text `8` | text `20` |
| Cluster Memberships | A42 | `8` | `20` |
| Cluster Memberships | A43 | `8` | `20` |
| Scenarios | C14 | `Begins the fictional Assassin Network crisis in an eligible government. The host suffers an opening succession shock and begins investigating a movement whose reach and cohesion grow with the selected intensity. Later discoveries may reveal threats beyond the original murder, while uninvolved countries retain their existing leadership.` | `A murder shakes the succession of an eligible government and opens an investigation into a hidden movement. Higher intensity gives it more reach and cohesion, and later discoveries may reveal threats beyond the first killing.` |
| Scenarios | D14 | `Clandestine network` | `Hidden Network` |

`Scenarios!E14` changed from the following prior value, whose leading colour markers were U+FFFD characters:

```text
�RStarts Assassin Network immediately.�! Low intensity opens a Murder Cult investigation with low reach and a small foreign network. No Assassin State exists at launch.

�RStarts Assassin Network immediately.�! Medium intensity opens a mature international network and a stronger investigation. The host can still prevent the Assassin State split.

�RStarts Assassin Network immediately.�! High intensity opens the Assassin State war and a strong foreign network through the normal country transaction.

�RStarts Assassin Network immediately.�! Maximum intensity opens Evolution IV, the Assassin State war, and foreign derivative operations. World of Anarchy still requires its normal terminal conditions.
```

The after value is the following exact localisation text, with one blank line between paragraphs:

```text
§RStarts Assassin Network immediately.§! Low intensity opens a Murder Cult investigation with low reach and a small foreign network. No Assassin State exists at launch.

§RStarts Assassin Network immediately.§! Medium intensity opens a mature international network and a stronger investigation. The host can still prevent the Assassin State split.

§RStarts Assassin Network immediately.§! High intensity opens the Assassin State war and a strong foreign network.

§RStarts Assassin Network immediately.§! Maximum intensity opens Evolution IV, the Assassin State war, and foreign operations. World of Anarchy still needs its usual end conditions.
```

## Reconciliation evidence

Runtime constants assign Intelligence cluster ID 20 and define it as a one-time cluster at Chaos level 1; Event52 is the required Low member and Event39 the optional Medium member. The matching workbook cluster row, event cross-links, and both membership rows now use ID 20. No unrelated cluster IDs were renumbered.

The event catalog retains Event39 as `Minor Fire-Once`, Chaos level 1, with `Needs Testing` status, and retains Event52's `To Be Reworked` status. SCN-019 remains reserved with `Needs Testing` status. No entry was marked `Playable`, and no status was changed.

Event39's event-log detail, five evolution labels, World of Anarchy title and detail, and Intelligence cluster detail already matched the player-facing localisation and remain unchanged. The Intelligence member list and severities remain `39, 52` and `Medium, Low`.

The workbook contained no formulas. Post-save checks found no duplicate Event, Cluster, or Scenario IDs; SCN-019 occurs once, and runtime Assassin Network ID 19 agrees with it. The requested eight value changes were the only cell-value deltas. Cell styles, workbook structure, tables, data validations, filters, and freeze-pane settings were preserved.

## Workbook and export hashes

The workbook SHA-256 immediately before save was `5BAE3142F732BDA3FC2946D546515647DC7022212949724C8FF2B04F83533CD0`, matching the hash captured during initial inspection. After save it was `A0D63C9D885CB5DE3BBAC3480A221A3C94A229D9A33C6682DC50533F643B58C9`.

`python .tools/export_event_catalog_csv.py` completed with status `success` from the mod root.

| Export | Rows including header | Columns | SHA-256 |
| --- | ---: | ---: | --- |
| `docs/spreadsheets/chaos_redux_events_catalog.csv` | 166 | 13 | `5edcd62579ff14831559f772c0378024ba38f7e03dccd5f06080f5e9ea27565f` |
| `docs/spreadsheets/chaos_redux_clusters_catalog.csv` | 20 | 8 | `21a0df3e818b37f9716e6092d8f46a14ca1297121f2ed32ffb01c4a34d18b638` |
| `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` | 17 | 6 | `95d667fa6c1d5e874b0c51c61efb465b814ae484f6dc48616680238ec85dc5e9` |

All three CSVs were reread after export; Event39 and Event52 cross-links, Intelligence ID 20, and SCN-019 description, type, and four warning paragraphs match the workbook. The warning markers are the real section sign U+00A7, not U+FFFD.

## Sources checked

- `common/script_constants/event_cluster_constants.txt` for Intelligence ID 20, one-time classification, Chaos level 1, and the runtime Event39/Event52 membership contract.
- `common/script_constants/chaosx_triggerable_scenarios_constants.txt` for Assassin Network scenario ID 19.
- `common/scripted_effects/chaosx_event_cluster_effects.txt` for Event52 required Low and Event39 optional Medium membership.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` for Event39 detail, five evolution selectors, and World of Anarchy title/detail selectors.
- `localisation/english/039_murder_mystery_l_english.yml` for all player-facing text copied or compared.
- `docs/plans/039_murder_mystery_plans/catalog_changes_pending.md` for the previously queued reconciliation facts; that file was not edited.

## Shared-worktree note

The worktree was already broadly modified when this task began, including the workbook and its three CSV exports.
The shared Git index had no staged paths at the initial check.
The worker created no commit and edited no other file.
The parent must isolate the eight workbook cell deltas and their exporter-produced records when committing, because staging the entire working workbook or CSVs would include other agents' edits.
