# Event 050 source conflict ledger

| Topic | User-provided design | Supplied catalog or project source | Accepted disposition |
| --- | --- | --- | --- |
| Event ID | `50` | Event export row uses `50` | Preserve `50` |
| Name | The Great Embargo | Event export uses The Great Embargo | Preserve name |
| Type | Minor Repeatable | Event export uses Minor Repeatable | Preserve type |
| Chaos level | 1 | Event export uses 1 | Preserve level 1 |
| Cluster | Negative Economy | Event export leaves cluster blank | Use user-provided cluster in the spec, reconcile workbook later |
| Member severity | Medium | Event export leaves severity blank | Use Medium in the spec, reconcile workbook later |
| Cluster ID | Not supplied | Cluster export has an incomplete Negative Economy row with no ID | Do not invent an ID |
| Cluster type | Not supplied | Incomplete cluster row says Minor Fire-Once | Treat as unresolved workbook data, do not copy to Event 50 |
| Cluster Chaos level | Not supplied | Incomplete cluster row says 2 | Do not change Event 50 level 1, audit the cluster workbook separately |
| Cluster status | User treats membership as accepted design | Incomplete cluster row says Unavailable | Preserve intended membership and flag implementation dependency |
| Public value | Embargo Pressure | Decision and planning skills prefer one or two public values | Preserve one value |
| Target pool | Player country or random major | Catalog summary says major country only | Preserve the fuller user design |
| DLC behavior | Native embargo is optional reinforcement | Mechanics guide says native embargo can depend on DLC | Preserve event-owned baseline functionality |
| Evolutions | Secondary Sanctions at 400, spread at 800 | No evolution details in current event export | Preserve user design, update workbook after implementation wording |

## Authority order used

1. Direct user instructions for Event 50
2. Current project mechanics and skill contracts
3. Supplied event, cluster, and scenario exports as evidence snapshots
4. External research as design support only

The authoritative XLSX remains the only editable catalog source during implementation. The CSV files must be regenerated from it and never edited directly.
