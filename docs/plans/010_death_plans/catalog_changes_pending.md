# Event 010 catalog updates pending

Date: 2026-10-06.

The workbook source `docs/spreadsheets/chaos_redux_events_catalog.xlsx` was not edited because the parent task prohibited spreadsheet and CSV writes during this source repair. Apply the values below to the existing Event 010 row, then run `python .tools/export_event_catalog_csv.py` only after the workbook update is authorized and complete.

## Event 010 row

| Field | Current in-game source value to mirror |
| --- | --- |
| Event details | The islands fall silent, and governments search the coast for an answer. A cold presence gathers beyond the sea, where ships, letters, and radio calls no longer return. |
| Evolution detail | An unexplained silence spreads from remote islands toward inhabited shores. Governments search for a cause as a cold presence gathers beyond the sea. |
| Evolution II | Ships vanish from a second island's route. The island is not yet known to be lost, but its neighbors have begun to notice the silence. |
| Evolution III | Death reaches the mainland coast. Coastal settlements fall silent, survivors name the force, and the first armies meet it. |
| Evolution IV | Weak ghost hosts stand in broken ranks around the emptied land. Their shadows mark the first boundary between living towns and the dead. |
| Evolution V | Hollow hosts gather in greater numbers and hold the front. More towns fall silent, while the living find fewer routes out. |
| Evolution VI | A continent falls silent, and Death's forces turn toward the last occupied shores. Few governments still have room to retreat. |
| World-end scenario | Death has begun its Last Shores campaign. The living countries that remain must hold distant fronts across empty cities and ruined supply roads. |

The Last Shores world-end condition counts six distinct continents; its foothold count remains a separate soul-budget input.

## Scenario entry row

Keep scenario row 6 aligned with `chaosx.scenarios.death.desc.instant_outbreak` and `chaosx.triggerable_scenarios.6.d`: one hidden island origin and one mainland reveal state are consumed, intensity adds starting territory and ghost hosts, and later spread uses the ordinary Death route after a successful launch. The successful scenario does not create natural evolution entries by shortcut.

## Pending disposition

Disposition: `accepted and queued`. The current in-game wording is implemented, but workbook parity and CSV export remain queued under the no-spreadsheet-writes instruction for this task.
