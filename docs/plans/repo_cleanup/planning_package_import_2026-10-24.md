# Planning package import and catalog migration

The eight uploaded packages are installed under `docs/specs/`, their active instructions have been reconciled with the current repository guidance, and the catalog uses the authorized package numbering.
Lootboxes specifies a worldwide first firing with one free ordinary random-rarity box per existing country and an automatic opening window for every human country.
Fuel Crisis is cataloged as a Severe member of Various Anomalies.
These are specification and catalog changes, with no gameplay implementation or live-game execution in this task.

## Authorization and scope

On 24 October 2026, the user requested the Lootboxes and Fuel Crisis corrections, supplied eight named planning archives, and asked to extract them into the mod and fix inconsistencies and outdated instructions.
The user then explicitly answered: “Adopt uploaded IDs and migrate the catalog.”
That instruction authorizes the identifier migration and preservation of displaced concepts, without automatically accepting every authored gameplay expansion in the imported documents.
The embedded coding, asset, goal and production prompts were reviewed as document content, not executed as instructions for this task.

## Imported packages

| Canonical ID | Package | Archive members | Entry point |
| --- | --- | --- | --- |
| 115 | Heroic Crusade | 28 | [README](../../specs/115_heroic_crusade_specs/README.md) |
| 116 | Warlords | 31 | [README](../../specs/116_warlords_specs/README.md) |
| 117 | Autonomy | 18 | [README](../../specs/117_autonomy_specs/README.md) |
| 118 | Shaman | 24 | [README](../../specs/118_shaman_specs/README.md) |
| 119 | Mistresses | 29 | [README](../../specs/119_mistresses_specs/README.md) |
| 120 | Widespread Mutiny | 23 | [README](../../specs/120_widespread_mutiny_specs/README.md) |
| 121 | Investment | 17 | [README](../../specs/121_investment_specs/README.md) |
| 122 | Gandhi | 28 | [README](../../specs/122_gandhi_specs/README.md) |

All 198 archive members have one recorded repository destination.
Historical source receipts and manifests retain their original scope and hashes, including records relocated into each event’s `docs/plans/.../imported_review/` directory.
The [machine-readable import record](planning_package_import_2026-10-24.json) records archive hashes, each member’s original hash, destination and reviewed content hash.
The package index at [docs/specs/README.md](../../specs/README.md) includes all eight entry points.

## Catalog migration

The migration includes the documented dependency chain needed to move IMRO, SPARTA and Cossacks without losing the earlier Rule, Random Idea, Resistance, Lootboxes and Wrestling Tournament identities.
The canonical workbook is the only edited catalog source, and all three CSV exports were regenerated from it.

| Canonical ID | Event | Former catalog ID |
| --- | --- | --- |
| 104 | Rule | 107 |
| 105 | Random Idea | 110 |
| 106 | Resistance | 111 |
| 107 | Lootboxes | 112 |
| 108 | Wrestling Tournament | 113 |
| 109 | Fuel Crisis | 114 |
| 110 | IMRO | 115 |
| 111 | This is SPARTA!!! | 116 |
| 112 | Rise of Cossacks | 122 |
| 113 | The Partition | 123 |
| 114 | Demilitarization | 124 |
| 115 | Heroic Crusade | 126 |
| 116 | Warlords | 127 |
| 117 | Autonomy | 128 |
| 118 | Shaman | 129 |
| 119 | Mistresses | 130 |
| 120 | Widespread Mutiny | 131 |
| 121 | Investment | 132 |
| 122 | Gandhi | 133 |

The former holds on catalog IDs 110, 113 and 122 are released by this authorized migration, with their historical records preserved in the shared registry.
The source rows at 123, 124 and 126 through 133 retire after their concepts move.
Non-Aggressions remains at 125.
The ten displaced concepts are preserved in full in the JSON record’s original catalog rows: Stability or War support, Anti-player ideology, Paranoia, Fury, Custom laws, 5-Way Civil War, Plague of locust, Random New Alliance, Massive Volcano Eruption and The Pact.
They have no invented replacement IDs and are not silently merged into unrelated events.

All 19 migrated events retain `Unavailable` status because their runtime roots are absent.
Proposed types, Chaos tiers and evolution descriptions were not promoted into catalog facts.
Presentation and playback audio IDs remain separate namespaces, including Event 091’s occupied 121–123 reservations.
The [shared identifier registry](../../specs/shared_identifier_registry.md) and its JSON mirror describe the same completed migration.

## Requested event corrections

The [Lootboxes core specification](../../specs/107_lootboxes_specs/01%20-%20Event%20Identity%20and%20Core%20Loop.md), associated prompts, presentation flow and acceptance scenarios use one guarded worldwide first-fire distribution.
Every existing human or AI country, including subjects and minors, receives one free sealed box without a Political Power affordability gate.
The welcome box uses the ordinary random rarity, recipe, evolution and completion paths, with zero-payment provenance, five human chest activations, automatic local human presentation and ordinary AI resolution.
One unresolved-box limit, country receipt and first-fire guards prevent duplicate grants or rerolls on retries, resumption or reload.
Later purchases remain exactly 50 PP, and the rarity weights are unchanged.

The [Fuel Crisis specification](../../specs/109_fuel_crisis_specs/README.md) and cluster documentation use Various Anomalies, cluster 11, Severe membership without changing independent event eligibility.
The workbook’s membership slot 3 uses Event 109, and its aggregate sequences are `42, 47, 109` and `Low, Low, Severe`.
No runtime cluster row was added for the unimplemented event.

The catalog descriptions for Random Idea, Resistance, Lootboxes and Warlords were corrected where the source row described a different event.

## Review and evidence

Documentation curators reviewed the eight imported packages in four bounded pairs, with separate bounded reviews for the Lootboxes/Fuel Crisis correction and the earlier package migration references.
The parent reviewed their findings and corrected remaining current-state wording, the Cossacks 112 cross-reference, external source-bundle reread instructions and unconditional live/MCP completion gates.
The per-event import handoffs record document dispositions and archive destinations under each event’s `subagent_handoffs/` directory.
The [cross-reference handoff](planning_import_identity_crossrefs_2026-10-24.md) covers the nine earlier dependency packages.
The [catalog handoff](../107_lootboxes_plans/subagent_handoffs/catalog_corrections_2026-10-24.md) records source hashes, migration details and workbook preservation checks.

The catalog contains 155 unique event IDs after migration.
The spreadsheet worker verified all 19 destination mappings, the preserved Unavailable statuses, Fuel Crisis membership agreement, retained table and formatting definitions, and all three parsed exports against the workbook.
The parent’s final import check verifies member coverage, current local links and the declared identifier registry.
These checks concern documentation and catalog integrity, not gameplay behavior or balance measurements.

## Disposition and limitations

Import, instruction corrections, catalog migration and the two requested specification changes are implemented.
The Lootboxes and Fuel Crisis gameplay changes are accepted and queued with their unimplemented event packages.
Other imported mechanics retain their documented acceptance boundaries, and no source review is presented as runtime proof.
No design simplifications were made, no archive member was omitted, and no runtime asset was generated or substituted.

Skills used were `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-xlsx`, `chaos-redux-shared-git-commit`, and the curators’ relevant `chaos-redux-event-planning` and `chaos-redux-event-assets` guidance.
No skills were created or changed.
