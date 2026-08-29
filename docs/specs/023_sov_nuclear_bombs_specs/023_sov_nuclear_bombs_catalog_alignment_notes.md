# Event 023 catalog alignment notes

## Supplied catalog state

The supplied event CSV snapshot lists:

| Field | Supplied value |
| --- | --- |
| ID | 23 |
| Event Name | SOV Nuclear Bombs |
| Details | Soviet scientists have secretly developed nuclear weapons. |
| Baseline | Soviet Union gets 100 nuclear bombs. |
| Evolution I | Potential nuclear arms race between USA and Soviets, USA starts testing nuclear bombs. |
| Evolution II | More bombs. |
| Evolution III | Nuclear war. |
| Evolution IV | Blank |
| World-End Scenario | Blank |
| Type | Minor Fire-Once |
| Cluster | Blank |
| Status | Unavailable |

This package preserves the identity, exact baseline grant, and event type. It expands all four evolutions and keeps Fallout under shared consequence ownership. Event 23 has no owned world-end row.

## Proposed event row after implementation

The authoritative workbook should remain unchanged until the implementation is complete enough to support the final player-facing text.

Recommended final alignment:

| Field | Proposed direction |
| --- | --- |
| ID | 23 |
| Event Name | SOV Nuclear Bombs, unless final localisation adopts another approved public name while preserving the stable ID and slug |
| Details | A secret Soviet atomic arsenal opens testing, production, coercion, command, custody, and possible exchange systems |
| Baseline | The Soviet Union receives exactly 100 atomic bombs and chooses how the arsenal is controlled |
| Evolution I | The breakthrough becomes a wider nuclear race, expanding the stockpile and reactor network |
| Evolution II | Coercive doctrine opens direct demands against valid minors and Soviet breakaways |
| Evolution III | Multi-major nuclear conflict and retaliation become possible, with AI major first use still blocked below 1000 Chaos |
| Evolution IV | At World Collapse, Soviet AI major first use becomes rare but possible under severe strategic-loss gates |
| World-End Scenario | Shared Fallout connection only, with no Event 23-owned public branch |
| Type | Minor Fire-Once |
| Cluster | Leave blank until Arms-race has a verified stable ID and implemented members |
| Status | Use the repository's implementation-ready or implemented status only after completion evidence exists |

Final spreadsheet-facing wording must match the in-game Event Details and evolution wording. It should not expose hidden AI gates, exact MTTH, achievement conditions, or internal variables.

## Chaos level

The supplied CSV snapshot has no Chaos level column.

Event 23 should be registered at Chaos level 2, Gathering Storm, which begins at 200 Chaos.

The authoritative workbook, event registry, Event Details, and any generated documentation should agree on this level after implementation.

## Cluster alignment

The supplied cluster CSV contains cluster IDs 1 through 8. It contains no Arms-race cluster.

Do not assign an ID from memory or reuse an occupied ID.

A future Arms-race cluster needs:

- A verified new ID.
- Public name and description.
- Minimum chaos tier.
- Roll chance.
- Cooldown.
- Member roles.
- Participation rules.
- Danger labels.
- Member fire and skip reasons.
- Event Details and Clusters-tab content.
- Workbook row and CSV export.

Possible members named by the user are:

- Event 23 SOV Nuclear Bombs.
- Event 32 Missiles.
- Event 76 USA tests weapons.
- Event 47 BOOM, only after its design is known.

Event 23 is a likely core or severe member. The final role should be chosen by the cluster design.

Until that work exists, Event 23 remains unclustered.

## Scenario catalog discrepancy

The supplied mechanics guide lists:

- `SCN-004 Final Silence`, an explicit nuclear or thermonuclear manual scenario.

The supplied scenario CSV snapshot omits `SCN-004` and jumps from `SCN-003` to `SCN-005`.

This discrepancy must be checked against:

- The authoritative workbook.
- The live triggerable-scenario registry.
- Current scenario localisation.
- Current scenario documentation.

Event 23 should not edit the scenario catalog solely to resolve this discrepancy unless the implementation task explicitly includes shared scenario reconciliation.

Event 23 receives no triggerable scenario in this specification.

## Status transition

The supplied row is Unavailable and the project rules say unreworked events remain disabled by default.

Recommended transition:

1. Keep Event 23 disabled and unavailable during planning and partial implementation.
2. Complete event script, decisions, shared adapters, evolutions, AI, assets, super-event, achievements, docs, and audits.
3. Add Event 23 to the reworked-event default allowlist in the same completion change.
4. Update the authoritative workbook.
5. Run `python .tools/export_event_catalog_csv.py`.
6. Verify Events-tab, Event Details, evolution previews, and workbook wording agree.

Do not change the CSV snapshots directly.

## Event Details fields

The workbook may contain fields beyond the supplied CSV export. After implementation, align at least:

- Event premise.
- Event type.
- Chaos level.
- Actor availability.
- Baseline summary.
- Evolution I through IV summaries.
- Shared Fallout connection.
- Cluster state.
- Status.

World-end fields should not imply that Event 23 owns Fallout.

## Spreadsheet worker handoff

The parent should give `chaosx_spreadsheet_doc_worker`:

- Event ID 23.
- Final in-game Event Details text keys.
- Final evolution detail text keys.
- Final cluster disposition.
- Final status.
- Chaos level.
- Shared Fallout wording.
- The scenario discrepancy as a separate note, not an instruction to invent a row.

The worker should edit only the authoritative XLSX and run the exporter.
