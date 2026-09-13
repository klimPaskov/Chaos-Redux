# Part 7: Chaos, cluster behavior, cleanup, and validation

## Event classification

Event 048 remains Minor Fire-Once at Chaos level 1. It belongs to the Formables cluster and should use Medium member severity once the authoritative workbook is aligned.

The current exported event catalog has the event row without cluster and severity values. The package includes a workbook handoff patch row, but the CSV export itself must not be edited directly in the repository.

## Chaos handling

The event does not receive arbitrary Chaos for becoming stronger. Normal shared sources already account for wars, annexations, puppeting, faction changes, deaths, and other world consequences.

Event-owned Chaos changes should be rare and tied to unique outcomes not already counted by shared systems, such as a major forced regional settlement or the final Black Sea imperial proclamation if the implementation decides it represents a distinct world-order shock.

## Formables cluster

The current cluster export identifies Formables as cluster ID 6, Minor Repeatable, unlock tier 3. Event 048 itself has Chaos level 1, so ordinary event eligibility and cluster participation remain separate gates under the shared cluster rules.

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
