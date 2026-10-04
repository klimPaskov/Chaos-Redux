# Event 039 catalog changes pending

The event catalog workbook (`docs/spreadsheets/chaos_redux_events_catalog.xlsx`) is the only editable catalog source, and this workstream may not edit it or its exported CSVs.
The changes below record where the workbook no longer matches the runtime, so the catalog owner can apply them and rerun `python .tools/export_event_catalog_csv.py`.

## Clusters sheet: Intelligence cluster ID

Disposition: accepted and queued (agent decision D18 in `agent_decisions_2026-10-04.md`); waiting for the catalog owner.

| Field | Current workbook value | Runtime value | Required change |
| --- | --- | --- | --- |
| Cluster ID of Intelligence | 8 | 20 (`event_cluster_id.intelligence`) | Either change the workbook ID to 20, or renumber the runtime clusters to the workbook IDs in one coordinated change |
| Members (ID) | 39, 52 | 52 (required), 39 (optional) | No change; note that 52 is the required Low baseline and 39 the optional Medium member |
| Member Severities | Medium, Low | 39 Medium, 52 Low | No change |
| Type | Minor Fire-Once | `event_cluster_type.one_time` | No change |
| Chaos level | 1 | unlock tier 0 (Chaos level 1) | No change |

Runtime cluster 8 is Diseases, which the workbook lists as cluster 13, so the workbook ID 8 cannot be used at runtime without moving Diseases.
The same drift exists for Random Stuff (runtime 12, workbook 19); the catalog owner should decide whether the runtime or the workbook numbering is authoritative before more clusters are added.
ID 20 is free in both the runtime registry and the workbook.

## Scenarios sheet: row 14, SCN-019 Assassin Network

Disposition: accepted and queued; the workbook must copy the in-game localisation from `localisation/english/039_murder_mystery_l_english.yml`, which is the player-facing source.
The `§R` and `§!` colour codes in E14 are stored in the workbook as the replacement character U+FFFD, which is why the registration check fails on E14; the required value uses the real section sign.

| Cell | Current workbook value | Required value (runtime key) |
| --- | --- | --- |
| C14 Details | "Begins the fictional Assassin Network crisis in an eligible government. The host suffers an opening succession shock and begins investigating a movement whose reach and cohesion grow with the selected intensity. Later discoveries may reveal threats beyond the original murder, while uninvolved countries retain their existing leadership." | "A murder shakes the succession of an eligible government and opens an investigation into a hidden movement. Higher intensity gives it more reach and cohesion, and later discoveries may reveal threats beyond the first killing." (`chaosx.scenarios.assassin_network.desc`) |
| D14 Type Options | "Clandestine network" | "Hidden Network" (`chaosx.scenarios.type.assassin_network`) |
| E14 Intensity Scaling, Low paragraph | Matches the runtime text apart from the U+FFFD colour codes | "§RStarts Assassin Network immediately.§! Low intensity opens a Murder Cult investigation with low reach and a small foreign network. No Assassin State exists at launch." (`chaosx.scenarios.assassin_network.impact.low`) |
| E14 Intensity Scaling, Medium paragraph | Matches the runtime text apart from the U+FFFD colour codes | "§RStarts Assassin Network immediately.§! Medium intensity opens a mature international network and a stronger investigation. The host can still prevent the Assassin State split." (`chaosx.scenarios.assassin_network.impact.medium`) |
| E14 Intensity Scaling, High paragraph | "...High intensity opens the Assassin State war and a strong foreign network through the normal country transaction." | "§RStarts Assassin Network immediately.§! High intensity opens the Assassin State war and a strong foreign network." (`chaosx.scenarios.assassin_network.impact.high`) |
| E14 Intensity Scaling, Maximum paragraph | "...Maximum intensity opens Evolution IV, the Assassin State war, and foreign derivative operations. World of Anarchy still requires its normal terminal conditions." | "§RStarts Assassin Network immediately.§! Maximum intensity opens Evolution IV, the Assassin State war, and foreign operations. World of Anarchy still needs its usual end conditions." (`chaosx.scenarios.assassin_network.impact.maximum`) |

E14 keeps its four paragraphs separated by one blank line, in the order Low, Medium, High, Maximum.

## Events sheet: row 40, Event 39 Murder Mystery

Disposition: accepted and queued.

| Cell | Current workbook value | Runtime value | Required change |
| --- | --- | --- | --- |
| L40 Cluster ID | 8 | 20 | Follow the Intelligence cluster decision above |
| J40 Type | Minor Fire-Once | Fire-once pool event (agent decision D2) | No change |
| K40 Chaos level | 1 | 1 | No change |
| C40 Details, D40 to H40 evolution names, I40 World-End Scenario | Match the runtime localisation | `murder_mystery.event_log.detail`, `murder_mystery.evolution.<i..v>.title`, `chaosx.events_log.world_end.murder_mystery_world_of_anarchy.details` | No change |

The Cluster Memberships sheet rows 42 and 43 (cluster 8, members 39 Medium and 52 Low) need the same cluster ID change as L40.
