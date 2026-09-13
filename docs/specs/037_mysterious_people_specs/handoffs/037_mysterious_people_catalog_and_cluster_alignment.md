# Event 037 catalog and cluster alignment handoff

## Current supplied event row

The supplied export contains:

| Field | Current value |
| --- | --- |
| ID | `37` |
| Event Name | Mysterious People |
| Details | A major country receives millions of unexplained new recruits. |
| Type | Minor Repeatable |
| Chaos level | `1` |
| Cluster ID | empty |
| Member Severity | empty |
| Status | To Be Reworked |

The detail premise is obsolete. It describes a country-targeted recruit event, while the accepted specification is global, state-based, and civilian.

## Accepted replacement

| Field | Required value or direction |
| --- | --- |
| ID | `37` |
| Event Name | Mysterious People |
| Type | Minor Repeatable |
| Chaos level | `1` |
| Cluster | Various Anomalies |
| Member Severity | Low |
| Status before implementation | To Be Reworked |
| Status after complete implementation | Needs Testing |
| Details direction | Every valid inhabited state gains real civilian population with local records and impossible social history. Repeated manifestations can turn the gift into overpopulation, famine, migration, and repression pressure. |
| Evolution I direction | Population Surge at `200+` Chaos, larger grants and support-capacity projects. |
| Evolution II direction | Overpopulation Crisis at `400+` Chaos, burden feeds existing Famine and Migration systems. |
| Evolution III direction | Humanity Multiplies at `600+` Chaos, enormous demographic increase and extreme policy routes through existing systems. |

Final wording should be copied from the implemented Event Details and evolution localisation so the workbook and in-game text remain aligned.

## Workbook rule

Edit only:

```text
docs/spreadsheets/chaos_redux_events_catalog.xlsx
```

After a successful workbook update, run:

```text
python .tools/export_event_catalog_csv.py
```

Do not edit the three CSV exports directly.

## Cluster findings

The supplied cluster export contains numeric IDs `1` through `8`, then `10`. Various Anomalies has no numeric ID, no members, Chaos level `4`, and status Unavailable.

Event 037's accepted classification is:

- Various Anomalies
- Low member severity
- event Chaos level `1`

The cluster's own unlock tier and event's minimum Chaos level are separate concepts. The live cluster design must decide the final Various Anomalies unlock tier based on its full member set.

## Provisional registry candidate

Numeric ID `9` is the visible gap in the supplied cluster sequence. It is a provisional candidate only.

Before assigning it:

1. Inspect the authoritative workbook.
2. Inspect live cluster constants and registry arrays.
3. Search repository references for cluster ID `9`.
4. Check generated CSV state.
5. Confirm no reserved save-facing identity uses it.
6. Review every intended Various Anomalies member and its minimum event level.
7. Define cluster type, unlock tier, cooldown, participation chance, and member roles.

Do not treat the supplied gap as proof of availability.

## Cluster activation condition

Event 037 should retain its cluster classification even while the cluster remains unavailable.

A live Various Anomalies cluster should be enabled only when:

- it has a stable registry ID
- at least one additional reworked member creates a meaningful multi-event incident
- member availability and role logic are defined
- event and cluster minimum tiers are reconciled
- one cluster firing applies Event 037 once
- cluster history can explain fired and skipped members
- automatic and manual cluster paths pass evidence

Until then, Event 037 remains fully eligible through its normal Minor Repeatable path.

## Cluster transaction requirement

When the cluster eventually fires Event 037:

- one global population transaction
- one Event 037 history entry
- one repeatable cap change
- one set of one-shot Chaos milestone checks
- no population application per cluster actor
- no extra pacing event per affected country
