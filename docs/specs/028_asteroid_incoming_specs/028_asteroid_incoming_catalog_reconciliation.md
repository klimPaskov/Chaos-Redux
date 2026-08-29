# Asteroid Incoming: Catalog Reconciliation

## Conflict found

The supplied `chaos_redux_events_catalog` CSV export contains an older Event 28 row. It classifies the event as a minor repeatable event, marks it unavailable, and describes a prediction and research-windfall premise.

The supplied Event 028 brief supersedes that material. The accepted event is a global major event with three directed country targets, a miss option, a two-day impact delay, permanent state destruction, adjacency-ring damage, dust, a super-event, fragmentation, and extraordinary minerals.

The implementation must update the authoritative workbook. The CSV is an export and must not be edited directly.

## Required event row

| Field | Accepted value or direction |
| --- | --- |
| Event ID | 28 |
| Event name | Asteroid Incoming |
| Event type | Major |
| Status during implementation | To Be Reworked |
| Status after full implementation and before live verification | Needs Testing, when that matches current catalog workflow |
| Chaos level | Calm World for baseline eligibility |
| Cluster | Blank or None according to workbook convention |
| Repeatable | No |
| Fire once | Yes through major-event behavior |
| Availability | Valid only when three target pairs can be built |
| Detail premise | Brief scientific control of an incoming asteroid, three country and state targets, miss option, two-day lock, regional destruction, dust, and lasting craters |
| World-end field | Leave blank under workbook convention |
| Scenario field | Leave blank under workbook convention |

The detail field should remain player facing. It should not list raw target scores, helper names, internal flags, exact dust formula, or implementation history.

## Evolution rows

### Global Fragmentation

| Field | Accepted value or direction |
| --- | --- |
| Parent event | 28 |
| Evolution name | Global Fragmentation |
| Tier | Chaos Tier |
| Threshold | 600 Chaos |
| Stage | 1 |
| Detail | The chosen main body still strikes, while separated fragments hit several valid states worldwide with smaller damage rings and additional dust |

### Extraordinary Minerals

| Field | Accepted value or direction |
| --- | --- |
| Parent event | 28 |
| Evolution name | Extraordinary Minerals |
| Tier | Totalen Chaos |
| Threshold | 800 Chaos |
| Stage | 1 |
| Prerequisite | Global Fragmentation |
| Detail | Main and fragment crater control grants transferable armour bonuses, with plus 100 percent from the main crater and plus 20 percent per fragment site |

The exact spreadsheet wording should match the final Event Details localisation in meaning.

## Workbook and export process

1. Edit `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
2. Preserve workbook structure, filters, validation, formulas, and formatting.
3. Replace the stale Event 28 row and add or update its evolution fields.
4. Confirm cluster and scenario sheets do not incorrectly register Event 28.
5. Run `python .tools/export_event_catalog_csv.py` from the mod root.
6. Review all three generated CSV exports for alignment.

## Default enable state

Event 28 should remain disabled by default while the row status is To Be Reworked. The implementation can restore normal default enablement only when event logic, AI, logs, decisions, assets, super-event, docs, achievements, and catalog alignment are complete.

## Catalog acceptance

The catalog is aligned when:

- Event 28 is Major everywhere.
- The old prediction and research-windfall text is gone.
- The event detail matches the directed-impact premise.
- Both evolutions have the accepted thresholds and effects.
- No cluster or manual scenario is registered.
- The CSV files match the workbook export.
