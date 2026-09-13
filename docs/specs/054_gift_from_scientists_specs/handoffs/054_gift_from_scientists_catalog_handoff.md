# Event 54 Catalog and Cluster Handoff

## Authoritative edit path

Update `docs/spreadsheets/chaos_redux_events_catalog.xlsx` after the event implementation and final player-facing localization are complete. Then run `python .tools/export_event_catalog_csv.py` from the mod root.

The three CSV catalogs are generated snapshots. They must not receive direct edits.

## Event row correction

The current export identifies Event 54 as Gift from scientists while its detail field describes an infrastructure boom. That detail belongs to another idea and must be replaced.

Required Event 54 fields:

| Field | Required value or source |
| --- | --- |
| ID | `54` |
| Event name | Final in-game name for Gift from Scientists |
| Type | `Minor Repeatable` |
| Chaos level | `1` |
| Cluster membership | Scientific Research, Medium |
| Status | Implementation-derived status after audit |
| Details | Final Event Details premise wording from in-game localization |
| Evolution I | Final Multiple Breakthroughs premise wording from in-game localization |
| Evolution II | Final Accelerated Discovery premise wording from in-game localization |
| Evolution III | Final Scientific Deluge premise wording from in-game localization |

The details should describe the worldwide wave of independent random technology grants, including the possibility of advanced or strategically irrelevant results. They should avoid implementation terms such as candidate pool, registry, callback, safety profile, and reroll.

## Scientific Research cluster row

The current cluster export contains an empty Scientific Research placeholder with a Fire-Once classification and Chaos level 2. The final implementation should replace that placeholder with the actual cluster contract.

Required cluster fields:

| Field | Required value or source |
| --- | --- |
| Stable ID | Use the existing repository ID if already reserved. Use proposed ID `9` only after collision inspection confirms it |
| Name | `Scientific Research` |
| Type | `Minor Repeatable` |
| Chaos level | `2` |
| Status | Implementation-derived status after all member checks |
| Details | Final in-game cluster detail wording |

Accepted member slots:

| Event | Member severity | Additional membership |
| --- | --- | --- |
| 16 Brilliant Scientist | Severe | None |
| 24 Video Game in Sweden | High | None |
| 27 Doctrine Research | Medium | Military Preparation, Medium |
| 54 Gift from Scientists | Medium | None |
| 60 Research Failure | High | None |

The cluster runtime must preserve mixed event types, member-specific eligibility, member-specific severity, and many-to-many membership. A Fire-Once member that has already fired must be skipped without disabling remaining repeatable members.

The supplied event export currently labels Event 27 as Minor Fire-Once. The latest accepted Doctrine Research design in the project context treats it as Minor Repeatable. This Event 54 pack follows the accepted repeatable design for cluster behavior. Reconcile Event 27 through its own source specification and implementation review before the workbook is finalized. Do not let the Event 54 catalog edit silently decide that separate event rework.


## Cross-surface wording source

The workbook should copy the final event and cluster premise text from the same localization used by Event Details and cluster details. Do not create a separate spreadsheet-only rewrite that changes meaning.

## Required post-update proof

- Workbook row values match final localization.
- Event 54 has the correct type, Chaos level, cluster membership, severity, and evolution fields.
- Scientific Research has all five member slots.
- Event 27 remains in both accepted clusters.
- Exporter completes successfully.
- All three generated CSVs reflect the workbook without manual corrections.
