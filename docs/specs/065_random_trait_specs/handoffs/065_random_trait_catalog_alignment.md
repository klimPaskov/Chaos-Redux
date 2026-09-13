# Event 065 Catalog and Documentation Alignment

## Current supplied event row

The supplied event CSV contains:

| Field | Current value |
| --- | --- |
| ID | `65` |
| Event Name | `Random Trait` |
| Details | Every country leader receives a random trait |
| Evolutions | blank |
| Type | Minor Repeatable |
| Chaos level | `1` |
| Cluster ID | blank |
| Member Severity | blank |
| Status | To Be Reworked |

## Accepted target direction

The authoritative workbook should be updated after implementation evidence exists.

### Event 65 row

| Field | Accepted content direction |
| --- | --- |
| ID | Keep `65` |
| Event Name | Keep `Random Trait` |
| Details | State that every active country leader gains random country-leader traits from the complete vanilla and Chaos Redux pool and that repeat firings stack distinct additions |
| Evolution I | `Double Traits`, raw Chaos `200+`, two uniform traits per leader |
| Evolution II | `Exceptional Personalities`, raw Chaos `400+`, three traits per leader with modest featured weighting |
| Evolution III | `Walking Contradictions`, raw Chaos `600+`, five traits per leader with stronger bounded featured weighting |
| Evolution IV | Leave empty |
| Evolution V | Leave empty |
| Type | Keep Minor Repeatable |
| Chaos level | Keep `1` |
| Cluster ID | Use final Randomizations cluster ID |
| Member Severity | Medium |
| Status | `Needs Testing` after implementation and automated validation, then `Available` only after user acceptance |

### Randomizations cluster row

The current supplied cluster CSV has no Randomizations row.

Add one to the authoritative workbook.

| Field | Accepted content direction |
| --- | --- |
| Cluster ID | Prefer `9` after current-source and workbook collision check |
| Cluster Name | Randomizations |
| Details | Describe a cluster of events that randomize existing world systems or identities without normal thematic matching |
| Members | Include Event `65` |
| Type | Minor Repeatable |
| Chaos level | `1` |
| Status | Partially Available when Event 65 is implemented and the cluster framework is wired |

## Runtime member metadata

Use:

- role: optional
- danger: Medium
- participation: `60`
- member event ID: `65`
- entry path: Event 65 authoritative root
- outcome: one cluster member result
- actor: global or no-actor treatment
- state reservation: none
- country reservation: none

## Preferred constants

Subject to repository inspection:

- `event_cluster_id.randomizations = 9`
- `event_cluster_randomizations.unlock_tier` mapped to the accepted Chaos level `1` behavior
- `event_cluster_randomizations.cooldown_days = 120`
- `event_cluster_member_participation.random_trait = 60`

The numeric ID must change if the final collision audit finds a conflict.

The cluster unlock must not add an unintended extra tier above Event 65's own eligibility.

## Permanent event documentation

Recommended event documentation folder:

`docs/events/065_random_trait/`

Recommended files:

- `overview.md`
- `mechanics.md`
- `trait_registry_summary.md`
- `trait_registry.csv`
- `trait_registry_exclusions.md`
- `probability_and_weighting.md`
- `cluster_integration.md`
- `validation.md`

The docs should record implemented facts.

Planning directions, failed alternatives, and temporary work notes belong in `docs/plans/065_random_trait_plans/`.

## Export workflow

1. Open the authoritative Chaos Redux workbook.
2. Update the Event 65 row.
3. Add or update the Randomizations cluster row.
4. Run the existing workbook export workflow.
5. Compare all three CSV outputs.
6. Confirm the Event 65 and cluster values are identical across workbook, docs, runtime constants, Event Details, and event log.
7. Record the export command and resulting file hashes.

Direct editing of the supplied CSV exports is not acceptable as the final update method.
