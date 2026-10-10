# Event 008: Event Log, Localisation, and Text Direction

Finished player text lives in `localisation/english/008_world_tension_rises_l_english.yml` and the shared event-log localisation; the [5 October localisation handoff](../../../plans/008_tensions_rising_plans/subagent_handoffs/localisation_audit_2026-10-05.md) records its acceptance basis.
This file keeps the writing direction and the key map so later edits stay aligned across the report, incidents, log, details, and catalog.
The earlier pasteable draft paragraphs were removed because the final strings supersede them; do not reintroduce draft text as a source.

## Naming

Canonical event name: **Tensions Rising**.
Avoid alternatives that sound as if a war has already begun; the event is pressure before the break.

## Writing direction

- The report is short and report-like: accusations, communiqués, leaks, denials, and public unease, never hidden mechanics, weights, evolutions, or timer behavior.
- The option tooltip shows only the world tension and Chaos actually changed by the batch, with one decimal and a colour-free decrease branch.
- Stage tone moves from wires and desk lamps (Stage I) to a market of rumours (Stage II), sleepless staffs (Stage III), and a sustained alert that has become part of daily government (Stage IV).
- Incident reports follow the families in the main spec; each names a concrete behaviour (a telegram, a side door, a premium, a radio silence) and its tooltip states the consequence plainly.
- Event details describe the situation and premise, not timer values, penalties, achievement routes, or rewards.
- Stage IV text stays non-terminal and implies no super-event or world-end branch.
- Report and news text carries no `§` colour codes, and yellow is never used on report text.

## Key map

| Surface | Key |
| --- | --- |
| Root and batch report | `chaosx.nr8.1.t`, `.d` (`[GetTensionsRisingMainDesc]`), `.a`, `.a.tt` (`[GetTensionsRisingEffectText]`); `.16` reuses them |
| Stage descriptions and options | `chaosx.nr8.baseline.*`, `chaosx.nr8.stage_1.*` through `chaosx.nr8.stage_4.*`, `chaosx.nr8.aggregate.effect` |
| Incidents | `chaosx.nr8.2` through `chaosx.nr8.10` and `chaosx.nr8.12` (`.t`, `.d`, `.a.tt`) |
| Clash results | `chaosx.nr8.13` through `chaosx.nr8.15` |
| Event detail | `chaosx.events_log.window.event_details.tensions_rising` |
| Evolution type | `chaosx.events_log.evolution.type.tensions_rising` |
| Evolution titles and bodies | `chaosx.events_log.window.evolution_details.tensions_rising.title.stage_1`-`4`, `.body.event_detail`, `.body.stage_1`-`4` |
| Opinion modifiers | `tensions_rising_leaked_cables`, `tensions_rising_embassy_dispute`, `tensions_rising_mobilization_suspicion`, `tensions_rising_border_alarm`, `tensions_rising_permanent_alert` |

The in-game evolution titles are `Cable Traffic Increase`, `Competing Accusations`, `Staff Readiness`, and `Extended Alert`; the spec's stage names (Cable Traffic Flood, The Accusation Market, General Staffs Stop Sleeping, The Permanent Alert) are working design names.
The `.4` incident title is `Unease Along the Frontier`; the helper keeps its historical `calm_map` name.

## Catalog alignment

The workbook's Event 8 detail and evolution cells predate the final strings.
Exact pending wording is in `docs/plans/008_tensions_rising_plans/catalog_changes_pending.md`, and the spreadsheet owner mirrors the final keys and then runs `python .tools/export_event_catalog_csv.py`.
