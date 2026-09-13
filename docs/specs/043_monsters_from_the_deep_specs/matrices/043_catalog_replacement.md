# Event 043 catalog replacement

## Current export snapshot reviewed during planning

| Field | Current value |
| --- | --- |
| Event ID | 43 |
| Event name | Massive flood |
| Details | A massive flood devastates every coastal state it reaches. |
| Type | Minor Repeatable |
| Chaos level | 1 |
| Status | To Be Reworked |

## Intended Event row after full implementation

| Field | Intended value |
| --- | --- |
| Event ID | 43 |
| Event name | Monsters from the Deep |
| Details | Several named sea monsters emerge as separate nonhuman countries around distant coasts. Each country is ruled and anchored by one irreplaceable apex creature, expands through maritime territory, and can join rival pacts or converge under Cthulhu during World Collapse. |
| Type | Major |
| Chaos level | 3 |
| Cluster ID | empty |
| Member severity | empty |
| Evolution 1 | The Rising Tide |
| Evolution 1 details | More dormant creatures emerge, existing invasions gain stronger support, and monster pacts become easier to form. |
| Evolution 2 | Every Sea Opens |
| Evolution 2 details | Every valid maritime region can produce its registered monster country, final range routes open, and Cthulhu convergence becomes possible during World Collapse. |
| World-end scenario | Cthulhu's Dominion |
| World-end details | Surviving full monster countries unite under Cthulhu, transfer their living apex creatures into one terminal state, and gain continental reach. The union falls through normal capitulation or destruction of every surviving apex. |
| Status | Set from implementation evidence, not from this plan |

The details above are catalog directions. The spreadsheet worker must match final in-game Event Details wording after localisation is implemented.

## Intended Scenario row

| Field | Intended value |
| --- | --- |
| Scenario ID | SCN-015 |
| Scenario name | Monsters from the Deep |
| Source event | 43 |
| Type controls | Warring Titans, Pact of the Deep |
| Low | 2 geographically separated baseline monster countries |
| Medium | 5 invasions across at least 4 macroregions |
| High | 10 Evolution I-strength invasions |
| Maximum | all 16 valid monster countries with Evolution II strength |
| Terminal behavior | Maximum Pact can prepare or invoke Cthulhu only after World Collapse and according to the public terminal toggle |
| Status | To Be Reworked until implementation is complete |

## Workbook rule

Edit only:

```text
docs/spreadsheets/chaos_redux_events_catalog.xlsx
```

Then run:

```text
python .tools/export_event_catalog_csv.py
```

Do not edit the three CSV exports directly.
