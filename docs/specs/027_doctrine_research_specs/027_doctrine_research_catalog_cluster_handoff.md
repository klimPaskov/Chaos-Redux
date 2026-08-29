# Event 027: Catalog and National Breakthroughs cluster handoff

## Authority rule

The authoritative catalog source is `docs/spreadsheets/chaos_redux_events_catalog.xlsx` in the Chaos Redux repository.

The supplied CSV files are export snapshots. They must not be edited directly.

The authoritative XLSX was not supplied in this runtime. This file provides the exact design handoff for `chaosx_spreadsheet_doc_worker` after implementation facts and final in-game wording exist.

## Current stale Event 027 row

| Field | Supplied CSV value |
| --- | --- |
| ID | `27` |
| Event Name | Doctrine research |
| Details | A major country gains a complete military doctrine after a sudden research breakthrough. |
| Type | Minor Fire-Once |
| Cluster ID | Empty |
| Member Severity | Empty |
| Status | Unavailable |

The row conflicts with the accepted user brief in target scope, event type, repeat behavior, evolutions, and cluster membership.

## Proposed Event 027 row

| Field | Proposed value or direction |
| --- | --- |
| ID | `27` |
| Event Name | Doctrine Research |
| Details | Every valid country receives a doctrine-development batch. Each choice can establish one eligible Grand Doctrine in a selected military domain, or advance one mastery level in an eligible subdoctrine branch. Establishing a Grand Doctrine consumes the choice without granting mastery. |
| Evo I | Each country receives two separate choices in one firing. The choices may be concentrated or divided. A country can establish a Grand Doctrine with the first choice and begin its mastery with the second. |
| Evo II | Each country receives three separate choices. The choice flow continues until all three are resolved or no valid doctrine option remains. |
| Evo III | Each country receives four separate choices. The batch can cover several tracks or services, including supported custom doctrine domains. |
| Evo IV | Each country receives five separate choices. This is the highest planned batch size and can fully develop a fresh five-level branch. |
| Evo V | Empty |
| World-End Scenario | Empty |
| Type | Minor Repeatable |
| Cluster ID | Provisional `9`, pending authoritative registry and workbook audit |
| Member Severity | Medium |
| Status before implementation | To Be Reworked |
| Status after complete implementation but before live testing | Needs Testing |
| Status after accepted live validation | Use the current project status vocabulary, normally Playable or Implemented according to catalog policy. |

The final Details and evolution fields must mirror the accepted in-game Event Details wording. The spreadsheet worker should not paste this design text when final localization differs.

## Event 027 cluster member contract

| Attribute | Accepted direction |
| --- | --- |
| Cluster | National Breakthroughs |
| Role when another member is selected | Optional |
| Role when Event 027 is the originally selected event | Guaranteed through the shared selected-member behavior |
| Minimum chaos tier | Calm World |
| Severity | Medium |
| Participation chance | Use the cluster's moderate band after a full member-pool probability audit |
| Effect when included | Fire one normal Event 027 global fanout at the current evolution stage |
| Extra cluster reward | None |
| Pacing | The whole cluster counts as one global pacing event |

Exact participation chance should be chosen with the complete cluster pool. Several proposed members have global or large positive effects, so independent high chances could create a reward burst that is too large.

## Proposed National Breakthroughs cluster row

The supplied cluster CSV currently contains numeric IDs through `8`. Numeric `9` is the natural provisional candidate. The implementation agent must audit the current authoritative workbook and runtime constants before reserving it.

| Field | Proposed value or direction |
| --- | --- |
| Cluster ID | Provisional `9` |
| Cluster Name | National Breakthroughs |
| Details | A period of rapid institutional improvement spreads through military schools, research offices, command staffs, public agencies, and national leadership. The selected breakthrough is guaranteed, while other eligible members may join the same worldwide development cycle. |
| Members | `27`, `54`, `65`, `67`, `83`, `85`, `89` |
| Type | Minor Repeatable |
| Chaos level | `1`, Calm World under the catalog's current numeric convention |
| Concept status | Accepted rough cluster concept |
| Runtime status before registry exists | Unavailable |
| Runtime status after some members are implemented | Partially Available |
| Runtime status after the accepted member set is implemented and audited | Playable |

## Provisional member matrix

The matrix records design roles for a future cluster-wide rework. It does not replace each member event's own specification.

| Event ID | Current catalog concept | Proposed cluster role | Provisional severity | Cluster concern |
| --- | --- | --- | --- | --- |
| `27` | Doctrine Research | Global doctrine-development batch | Medium | Direct global mastery can be strong at later evolutions. |
| `54` | Gift from scientists | Infrastructure or institutional development benefit | Medium | Current row is vague and needs its own accepted rework. |
| `65` | Random Trait | Leadership development | Low | Global leader changes need duplicate and validity protection. |
| `67` | Generalissimo | Exceptional command appointment | Medium | Fire-once member and potentially strong for one country. |
| `83` | Agency upgrade | Agency or government institutional improvement | Low or Medium | Current row details describe political power, which conflicts with the event name. |
| `85` | XP | Military experience choice | Medium | A global experience grant can compound Event 027 when both join. |
| `89` | Tech sharing | Doctrine or military-knowledge sharing | High | Current Kamikaze concept overlaps doctrine content and needs careful separation from Event 027. |

The cluster should not treat these stale catalog concepts as implementation-ready. Each event needs its own accepted spec, status, eligibility, AI, and effect contract.

## Cluster behavior direction

National Breakthroughs should feel like a short development cycle with several related advances. It should not routinely grant all seven member effects.

Recommended cluster behavior:

- the originally selected event always fires when the cluster roll succeeds
- other implemented and eligible members roll as optional participants
- the expected total member count should remain small
- fire-once members disappear from later pools after use
- disabled, unavailable, invalid, or exhausted events are skipped with a logged reason
- each member retains its own type, fired state, repeatable cap change, and history
- the cluster owns only the grouping and optional participation

The exact expected member count should be chosen after full-pool probability analysis. A reasonable design target is usually two or three total members, with occasional larger cycles. This is a target for audit, not a final hardcoded count.

## Event 027 and Event 085 interaction

When Event 027 and Event 085 fire in one cluster:

- Event 027 grants direct doctrine actions
- Event 085 grants its own accepted military-experience reward
- Event 027 does not consume, convert, or scale the experience reward
- Event 085 does not enlarge the Event 027 batch
- AI resolves each event through its own logic

The cluster detail should list both member outcomes without merging them into one doctrine reward.

## Event 027 and Event 089 separation

Event 089's stale concept spreads Kamikaze doctrine to every country. That concept overlaps with doctrine selection and may be incompatible with the current Grand Doctrine and subdoctrine model.

Event 027 owns direct country choice. Event 089 should own a distinct sharing event after its rework, such as one doctrine family spreading through factions, captured manuals, advisers, or a global special rule.

Event 027 must not implement Event 089 as one of its options. Event 089 must not call Event 027's full batch as a shortcut unless a later accepted spec explicitly defines that connection.

## Workbook update sequence

After implementation and final localization:

1. Open `docs/spreadsheets/chaos_redux_events_catalog.xlsx` with the spreadsheet skill.
2. Update Event 027 in the Events sheet.
3. Audit whether cluster ID `9` remains free in the current workbook and runtime registry.
4. Add or update National Breakthroughs in the Clusters sheet.
5. Add Event 027's final cluster ID and member severity.
6. Keep Event 54, 65, 67, 83, 85, and 89 statuses honest. Do not mark them implemented from cluster membership alone.
7. Preserve workbook structure, formatting, formulas, filters, and validation.
8. Save the workbook.
9. Run `python .tools/export_event_catalog_csv.py` from the mod root.
10. Review all three regenerated CSV exports for alignment.

## Catalog acceptance criteria

Catalog alignment is complete when:

- Event 027 no longer uses the stale one-major-country description
- Event 027 is Minor Repeatable
- all four evolutions describe two through five choices
- Evolution V and world-end fields remain empty
- cluster ID and severity match the runtime registry
- National Breakthroughs has the accepted details, member list, type, and chaos level
- member statuses remain honest
- CSV exports are regenerated from the XLSX
- Event Details, evolution detail text, cluster detail text, documentation, and spreadsheet wording agree
