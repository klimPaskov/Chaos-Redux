# Suggested Catalog Update: Event 6 Independence Wave

Use this when updating `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

## Primary row

| Column | Value |
| --- | --- |
| ID | 6 |
| Event Name | Independence Wave |
| Type | Minor Repeatable |
| Cluster | Liberations |
| Cluster threat | Lowest threat, usually first |
| Details | Several inactive countries become independent immediately in weak, unstable, overstretched, colonial, occupied, or wartime hosts. The hidden resolver protects the host survival state, reduces or skips invalid candidates, then releases the successful wave at once. Release dossiers and post-release decisions explain and manage the aftermath. Armies scale by industry, manpower, depots, foreign aid, host weakness, previous waves, and chaos tier. Event 6 is independent from Event 5. Shared tags can appear in both systems, but mechanics follow release origin. Every host keeps at least one state, preferably its capital. Early waves use ordinary HOI4 or modded releasables. Higher chaos releases more countries and can unlock dormant tags, game-rule tags, protectorates, city states, historical-return countries, local polities, indigenous authorities, and strange high-chaos states. |
| Evo I | Committees Learn the Pattern. Batch size rises to 4 to 6, non-democratic releases become possible, starting armies are stronger, startup decisions deepen, and released countries can coordinate with earlier breakaways through recognition, guarantees, aid, and volunteers. |
| Evo II | The Small States Congress. Batch size rises to 5 to 7. Multiple breakaways can coordinate, guarantee each other, share equipment, send volunteers, arbitrate disputes, and prepare a formal league. Dormant or game-rule tags become more likely if valid. |
| Evo III | Claims Follow the Flag and The Protectorate Game. Batch size rises to 6 to 9. Released states can demand territory, ask majors to back transfers, issue ultimatums, accept foreign advisers, resist puppeting, or become patron clients. City, free port, rail, and protectorate packages become more common. |
| Evo IV | The Old and the Local Return. Batch size rises to 8 to 12 if valid candidates and performance allow. Historical-return, local-polity, indigenous authority, city-state, railway, and custom country packages become possible, including packages such as Assyria, Mesopotamia, Mapuche Araucania, Guarani, Charrua, Aymara, Sokoto, Asante, Buganda, Kanem-Bornu, Darfur, Barotseland, Palmares, Volga Bulgaria, Circassia, Bukhara, Khiva, and Kokand if state and asset support exists. |
| Evo V | The Impossible State. Batch size can rise to 10 to 16 if valid candidates and performance allow. Strange packages, necromantic custodianships, anti-mankind doctrine states, archive-states, railway cults, and cooperation with other strange countries can appear. |
| World-End Scenario | No direct world-end by default. At World Collapse, a powerful anti-mankind, necromantic, or impossible-state release can feed existing world-threat systems if it becomes large enough to matter. |
| Host survival note | Event 6 never deletes an existing host. Candidate release is reduced, shrunk, or skipped before violating the one-state survival floor. |
| Event 5 separation note | Event 6 does not use Event 5 collapse progress, missions, route states, focus trees, formables, startup ideas, event logs, or country package flags. Shared tags and Soviet republic style tags use origin-gated Event 6 content when released by Independence Wave. |
| Super-event candidates | First League of New States, Great Partition Week, First Old Name Returns, First Impossible State, League War, Human Renunciation, The Rump That Endures. |
| Achievement count direction | 16 proposed achievements, including host survival, patron-free recognition, league formation, shared-tag separation, historical-return, local-polity, railway, and strange-state mastery. |

## Short spreadsheet text

Several inactive countries become independent immediately inside weak or overstretched hosts. Release dossiers and post-release response decisions appear as the wave fires. Early waves release ordinary HOI4-style countries. Higher chaos releases more countries and can unlock dormant tags, city states, protectorates, historical-return packages, local polities, indigenous authorities, and strange high-chaos states. Event 6 is separate from Event 5. Shared tags use origin-gated mechanics. Every host survives with at least one state.

## Event details view

The event details page should explain the mechanic through four sections.

### What starts the wave

Weak, unstable, wartime, colonial, occupied, or overextended hosts can trigger an instant release wave. Release dossiers describe the countries that just appeared and create pressure, legitimacy, radicalization, foreign attention, and host response strategy.

### How hosts respond

Hosts can negotiate, offer autonomy, suppress, delay, invite observers, arm loyalists, request guarantees, evacuate archives, trade territory, or stage loyalist counter-mobilization. These choices change pressure, legitimacy, radicalization, foreign attention, and later package behavior.

### How countries release

The wave validates candidates as a batch. It protects at least one host state, preferably the capital, then releases valid countries. The release count target scales by evolution, but actual releases can be lower when candidates are invalid or host survival would be violated.

### What happens afterward

Released states get the Independence Wave tree or an origin-gated package overlay. They can seek recognition, build militias, accept or reject patrons, join a small-state congress, arbitrate borders, demand claims, restore historical names, build local-polity institutions, or unlock strange high-chaos routes.

## Event log entries

| Log key | Meaning |
| --- | --- |
| `chaosx_event_006_log_dossiers_opened` | first release dossiers appear |
| `chaosx_event_006_log_host_negotiates` | host opens negotiations |
| `chaosx_event_006_log_host_suppresses` | host starts crackdown |
| `chaosx_event_006_log_observers_invited` | foreign observers enter crisis |
| `chaosx_event_006_log_wave_resolved` | wave resolves with release count |
| `chaosx_event_006_log_host_survives_rump` | host survives as one-state or near-rump |
| `chaosx_event_006_log_first_league` | League of New States forms |
| `chaosx_event_006_log_first_old_name` | first historical-return state appears |
| `chaosx_event_006_log_first_local_polity` | first local-polity state appears |
| `chaosx_event_006_log_first_strange_state` | first strange state appears |
| `chaosx_event_006_log_patron_crisis` | patron tries to control a breakaway |
| `chaosx_event_006_log_border_war` | border dispute becomes war |
| `chaosx_event_006_log_shared_tag_origin_checked` | shared tag receives Event 006 content |

## Spreadsheet implementation notes

- Do not list every package in the main Details cell if the cell becomes too long. Use the docs event page for the full package matrix.
- Keep the host survival rule visible in the Details cell because it prevents a common misunderstanding.
- Keep Event 5 separation visible in Notes or Details because shared tags such as Volga Bulgaria must not imply dependency.
- If focus counts are later implemented, update count-bearing rows only after recounting actual focus blocks.
- If super-events are implemented later, update the super-event catalog rows with actual slot IDs, audio IDs, image sprites, and localisation keys.

## Updated player-facing notes for formables and interfaces

The catalog row can mention formables and interface management only in player-facing language.

Suggested addition to Details if space allows:

```text
Surviving breakaways can later pursue regional congresses, old-state restorations, local-polity confederations, patron-backed mandates, or strange high-chaos proclamations through focus routes and formation decisions. Major waves can open visual ledgers for dossiers, patrons, congress votes, and formations.
```

Do not mention subagents, specs, implementation folders, fork context, or asset workflow in the spreadsheet.
