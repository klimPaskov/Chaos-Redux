# Event engine and catalog handoff

## Catalog intent

| Field | Intended design |
|---|---|
| Event ID | 073 in filenames and package references, numeric 73 in the catalog |
| Event name | Mongols Rise |
| Type | Minor Fire-Once |
| Current status | To Be Reworked |
| Chaos level | 1 |
| Cluster | Formables |
| Member severity | Low |
| Evolutions | The Yassa Restored at 200+, The Khanates Return at 400+, Universal Khan at 600+ |

The uploaded event catalog has no cluster or Evolution entries for 73. Its row is an older short description. The uploaded cluster catalog does not list 73 among Formables members. The user brief explicitly supplies the intended rework. This package records that change without editing either CSV.

Low is the requested cluster severity, not a promise that the final evolved army is weak. Keep the catalog assignment unless the user changes it. Flag balance tension during playtest instead of silently reclassifying the event.

The CSV files are export-only snapshots. A future catalog update must use the authoritative workbook, preserve its structure, and regenerate exports through the established workflow. The workbook was not provided. Do not mark the event Playable or Complete because these planning files exist.

## Existing implementation inspected

Repository: klimPaskov/Chaos-Redux.
Pinned evidence commit: `879b3007d3b6bf75c726c11635473fccda45c569`.
Fully read target file: `events/073_mongols_rise.txt`.

The existing namespace is `chaosx.nr73`. Event `.1` forwards to Mongolia's `.2`. Acceptance changes politics, creates a faction, grants `legacy_of_khan`, claims states on several continents, creates a sixteen-cavalry-battalion template, and spawns four divisions per controlled state. Refusal starts a civil war. Acceptance calls `chaosx.news.64`.

The rework replaces the unbounded claim and spawn behavior, compulsory faction recreation, and punishment civil war. It preserves the established namespace and inspects all legacy consumers before allocating or retiring identifiers. The old script's AI weights are not a tested probability model for the new campaign.

## Entry transaction

Resolve the physical Mongolian actor before root logging or grant processing. Check a valid reception country, equivalent-empire exclusion, fire-once state, and the correct shared or independent event context. A refusal records the attempted event without granting the restoration. An acceptance records one committed occurrence and one tier entitlement.

The event engine remains responsible for cluster selection, timer behavior, and the event's catalog identity. This package does not create a second independent event scheduler.

Use existing rework allowlists, event log context, and forced-event testing rules. A forced development entry must not qualify as an ordinary achievement run unless the existing achievement framework explicitly permits it.

## Evolution integration

Use the existing Evolution mechanism and enabled settings. The intended eligible MTTH starting anchor is the project's normal ninety-day pattern, with the appropriate dynamic factors and current source implementation verified before coding. The 200, 400, and 600 thresholds identify eligibility, not a separate private instant scheduler.

Each active upgrade adds the difference between recorded cumulative entitlements. It unlocks content without rerunning `.1` or `.2`. Stage activation, logging, and branch unlock have zero direct Chaos effect. Any real military or territorial consequence uses its separately reviewed Chaos source.

## Country classification

Mongolia and its human societies remain subject to ordinary population, famine, migration, casualty, and other applicable systems. An event-owned imperial identity can qualify for special Chaos-actor milestone accounting without being classified as nonhuman.

Do not use the restoration to clear unrelated penalties, grant immunity, or bypass ordinary population accounting. The extraordinary one-time opening muster is explicitly accounted as the event's fictional arrival.

## Required local inspection before coding

Inspect the live dispatcher, namespace consumers, event log wrappers, current Evolution helpers, country identity registry, special-unit registry, existing idea consumers, and the achievement registry. Confirm the current local commit before applying this pinned evidence. The repository may have changed since the inspected commit.

No live repository files were modified for this package. Exact new runtime paths and identifiers remain the implementation agent's responsibility after that inventory. Do not treat proposed planning labels as collision-checked game IDs.
