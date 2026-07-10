# Event 017 Random faction spreadsheet alignment handoff

- Date: 2026-07-10
- Scope: Event 017 row and Diplomatic Panic cluster row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- Status: complete

## Workbook ranges reconciled

### `Events!18`

| Range | Final content source | Result |
| --- | --- | --- |
| `B18` | `chaosx.event_name.17` and `chaosx.nr17.1.t` | Set to the matching in-game name `Random faction`. |
| `C18` | `chaosx.events_log.window.event_details.random_faction` | Replaced the placeholder text with the exact Event Details wording, including its paragraph break. |
| `D18` | `chaosx.events_log.window.evolution_details.random_faction.title.stage_1` plus `body.stage_1` | Set to the exact Regional Bloc Race title and body, separated by the workbook's established blank-line convention. |
| `E18` | `chaosx.events_log.window.evolution_details.random_faction.title.stage_2` plus `body.stage_2` | Set to the exact Pressured Neutrality title and body. |
| `F18` | `chaosx.events_log.window.evolution_details.random_faction.title.stage_3` plus `body.stage_3` | Set to the exact Collapse of Neutrality title and body. |
| `G18:I18` | Final implementation and event specification | Left empty because Event 017 has no fourth evolution, fifth evolution, or world-end scenario. |
| `J18` | `global.repeatable_events` registration in `common/scripted_effects/chaosx_logic_effects.txt` | Set to `Minor Repeatable`. |
| `K18` | `constant:event_cluster_id.diplomatic_panic` | Set to cluster ID `3`. |
| `L18` | Event 017 member entry in `load_event_cluster_members` | Set to `Low`. |
| `M18` | Parent implementation-status decision | Set to `Needs Testing`. Event 017 is implemented, but it has not yet received user live-session validation. This status does not represent a missing content surface. |

`Events!18` row height changed from `22.5` to `230` points. This was the only layout-property change and prevents the exact Event Details and evolution text from being clipped.

### `Clusters!4`

| Range | Final content source | Result |
| --- | --- | --- |
| `B4` | `chaosx.event_cluster.diplomatic_panic.name` | Confirmed as the exact in-game name `Diplomatic Panic`. |
| `C4` | `chaosx.events_log.window.cluster_details.description.diplomatic_panic` | Replaced the older description with the exact final in-game cluster description. |
| `D4` | Ordered Diplomatic Panic entries in `load_event_cluster_members` | Changed from `8` to the established member-list string `8, 17`. |
| `E4:F4` | Cluster registration and tuning | Confirmed unchanged as `Minor Repeatable` and chaos level `1`. |
| `G4` | Broader cluster status | Preserved as `In progress`. Event 017 did not independently determine the status of the whole cluster. |

The Event 017 cluster member is optional, has a 65 percent participation value from `constant:event_cluster_member_participation.random_faction`, starts at tier 0, and uses `constant:event_cluster_member_danger.low`.

## Exact workbook text

The localisation auditor confirmed that the catalog-facing wording below was final before workbook writeback.

### `Events!18`

`B18`:

```text
Random faction
```

`C18`:

```text
An independent minor outside the factions is cornered by the blocs able to offer membership and forced to choose one. A player country caught in the decision receives up to four faction offers and must sign with one of them.

The accession unsettles nearby neutral capitals, gives faction leaders a reason to court the border, and turns neutrality into work that has to be defended in public, in councils, and at frontier posts.
```

`D18`:

```text
Regional Bloc Race

Regional pressure starts spreading from one accession to neighboring neutrals. Border posts, observer invitations, neutrality councils, and faction staff missions become the public tools of the race.
```

`E18`:

```text
Pressured Neutrality

War draws neutral cabinets into the faction struggle. Countries beside active fronts face sharper demands, and faction leaders press exposed capitals for public commitments.
```

`F18`:

```text
Collapse of Neutrality

Several small states in one region can be drawn toward rival blocs in quick succession. Some capitals still try to hold their line through hurried councils, guarded borders, and costly declarations of neutrality.
```

`J18:M18`:

```text
Minor Repeatable | 3 | Low | Needs Testing
```

### `Clusters!4`

`B4`:

```text
Diplomatic Panic
```

`C4`:

```text
Diplomatic crises spread through public quarrels, collapsing relations, hurried guarantees, and minor states pressed to choose among nearby blocs.
```

`D4:G4`:

```text
8, 17 | Minor Repeatable | 1 | In progress
```

## Validation

- Reopened the saved workbook and compared `Events!B18:F18` and `Clusters!B4:C4` directly with the final localisation keys. Every string matched exactly.
- Confirmed `Events!J18:M18` reads `Minor Repeatable`, `3`, `Low`, and `Needs Testing`.
- Confirmed `Clusters!D4:G4` reads `8, 17`, `Minor Repeatable`, `1`, and `In progress`.
- Compared the edited workbook with a pre-edit copy. Only the intended Event 017 cells, `Clusters!C4:D4`, and the Event 017 row height changed. No cell style IDs changed.
- Preserved all sheet names and dimensions, freeze panes, merged ranges, column widths, workbook tables, images, charts, data-validation definitions, and conditional-formatting definitions.
- The workbook contains no formulas. A full-cell scan found no Excel error tokens.
- Rendered `Events!A1:M18` with only the header and row 18 visible, then rendered `Clusters!A1:G4` with only the header and row 4 visible. The final wording, member list, type, severity, and status were readable without clipped text or damaged formatting.

## Discrepancies resolved

- The Event 017 row still described a removed placeholder, had no evolution entries, and carried placeholder type and status values.
- The Diplomatic Panic row used the older cluster description and listed only Event 8.
- Both discrepancies are resolved in the workbook.

## Simplifications, omissions, and blockers

No fallback or simplification was used. No spreadsheet blocker remains.

No gameplay file or localisation file was edited by this spreadsheet task. No commit was created.
