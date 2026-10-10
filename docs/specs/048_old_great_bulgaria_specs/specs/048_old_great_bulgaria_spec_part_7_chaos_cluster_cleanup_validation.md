# Part 7: Chaos, cluster behavior, cleanup, and validation

## Event classification

Event 048 remains Minor Fire-Once at Chaos level 1.
The authoritative workbook already lists it in the Formables cluster (ID 6) as the Medium member, and the live cluster registry carries the same row.
The workbook row still has the one-line legacy details and empty evolution columns; `quality/048_event_catalog_patch.csv` holds the replacement details and the three evolution names for the implementation to apply to the workbook, never to the CSV exports.

## Chaos handling

Event 048 adds no event-owned Chaos.
Shared sources already account for wars, annexations, puppeting, faction changes, deaths, and other world consequences, and every formation is the sum of those consequences rather than a separate shock.
The final proclamation's weight is carried by its super-event and the real territory behind it.
`matrices/048_old_great_bulgaria_chaos_impact_map.md` lists each outcome and the shared source that counts it.

## Formables cluster

Formables is cluster ID 6, Minor Repeatable, unlock tier 3, in both the workbook and the live registry. Event 048 itself has Chaos level 1, so ordinary event eligibility and cluster participation remain separate gates under the shared cluster rules.

The event must remain fully playable when it fires independently before the cluster tier is available.

## Cleanup

Cleanup must remove obsolete territorial target decisions, completed missions, stale target flags, expired opening-surge state, and formation decisions made invalid by a later formation.

Integration state persists only while it remains meaningful. Lost regions retain bounded memory for reconquest and previous administrative work, but the system must not leave active missions against impossible targets.

## Save and campaign robustness

Every formation and route flag must be idempotent. Reopening the decision category, changing owners, capitulating a target, or saving and reloading must not duplicate the opening package, units, buildings, formation rewards, or evolution records.

## Implementation validation

Required production evidence includes:

- event-chain inspection and comparison
- focus inspection, render, and final route coverage audit
- exact-state map inspection for every formation group
- decision and mission audit
- AI probability scenarios and compare pass for weighted logic
- localisation audit
- asset requirement-to-runtime crosswalk
- super-event quote and audio source evidence
- country package audit where political routes change leaders, flags, or government setup
- final event completion audit against all seven spec parts

## No silent simplification

If exact map binding, final assets, AI behavior, an achievement, a political route, a formation, an integration family, or an evolution-gated branch cannot be completed, the implementation remains incomplete and the blocker must be reported.
