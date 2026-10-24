# Event Catalog Correction and ID Migration Handoff — 2026-10-24

Scope: the event catalog XLSX and its three generated CSV exports. No gameplay, localisation, plan, registry, or asset files were edited.

## Initial catalog correction

The first accepted spreadsheet pass corrected Events row 113, ID 112, Lootboxes, Details to the parent-supplied text: “Mysterious chests appear in every country. Each government receives its first chest as a gift, and a permanent market offers further boxes with unpredictable prizes.” It also assigned Fuel crisis ID 114 to cluster 11, added its slot 3 membership at row 78 as Severe, updated the aligned cluster member and severity aggregates, and recorded the planning/catalog identity note supplied by the parent.

No runtime root or localisation exists for the unimplemented Lootboxes event, so this Details wording is the parent-supplied accepted text and is not verified against live in-game localisation. The event status remained Unavailable.

The baseline workbook SHA-256 was `882cabb80387a4999ea67d40b28952c4479e4382a0e38fa18b27ec0e08a8c346`. The intermediate post-correction workbook SHA-256 was `392a673eca46e63e36c410db94ee4b6e6ccf433f7ac6dfcd9f3a48e240afd452`. An immutable baseline copy is retained under ignored `.tmp/planning_import_2026_10_24/catalog/chaos_redux_events_catalog.before_2026-10-24.xlsx`.

## Approved ID migration

After the user approved adopting uploaded IDs, the parent supplied the exact destination-to-current-source map. The catalog was rebuilt from an immutable in-memory snapshot to prevent overlapping IDs from cascading. The Events table now has 155 records, compacted in ascending ID order into rows 2–156; no worksheet rows were deleted. The ten displaced legacy concepts were removed from the active catalog while the parent owns their original-row archive. Current source ID 125, Non-Aggressions, remains unchanged. Consumed source identities 123, 124, and 126–133 were rekeyed to their mapped canonical IDs.

| Destination ID | Source ID | Canonical event name |
| ---: | ---: | --- |
| 104 | 107 | Rule |
| 105 | 110 | Random Idea |
| 106 | 111 | Resistance |
| 107 | 112 | Lootboxes |
| 108 | 113 | Wrestling Tournament |
| 109 | 114 | Fuel Crisis |
| 110 | 115 | IMRO |
| 111 | 116 | This is SPARTA!!! |
| 112 | 122 | Rise of Cossacks |
| 113 | 123 | The Partition |
| 114 | 124 | Demilitarization |
| 115 | 126 | Heroic Crusade |
| 116 | 127 | Warlords |
| 117 | 128 | Autonomy |
| 118 | 129 | Shaman |
| 119 | 130 | Mistresses |
| 120 | 131 | Widespread Mutiny |
| 121 | 132 | Investment |
| 122 | 133 | Gandhi |

Details for source IDs 110, 111, and 127 were corrected exactly as authorized: source 110 now reads “A national spirit appears in every country, bringing an unpredictable change to national life.”; source 111 now reads “Occupied states erupt in resistance across major countries and the player.”; source 127 now reads “Regional commanders break away from weakened governments, building rival states that struggle for territory, loyalty, and survival.” The Lootboxes Details text from the initial pass moved with source ID 112 to destination ID 107. All mapped rows retained their existing Type, Chaos level, evolution, World-End, and Unavailable status values; no planned implementation data was inferred.

Fuel membership moved from Event ID 114 to 109 at Cluster Memberships row 78, slot 3. Its name is now Fuel Crisis and its note is “Worldwide fuel reserve loss. Canonical event identity 109, former catalog identity 114.” Events Cluster ID remains 11. Clusters row 12 now lists Members (ID) `42, 47, 109` and Member Severities `Low, Low, Severe`, aligned with slot order.

The only pre-migration references to the affected ID set were the Fuel membership and its aggregate; no scenario references were found. The other ten displaced active concepts were Stability or War support, Anti-player ideology, Paranoia, Fury, Custom laws, 5-Way Civil War, Plague of locust, Random New Alliance, Massive Volcano Eruption, and The Pact. Their original workbook rows are outside the active catalog now and remain the parent's archive responsibility.

## Preservation and exports

The installed workbook SHA-256 is `d9ad04cedea2162ea66b8dac5d582ac66deb120e15b5865b9c1828ef9f9dbbec`. An immutable pre-migration snapshot is retained under ignored `.tmp/planning_import_2026_10_24/catalog/chaos_redux_events_catalog.before_id_migration_2026-10-24.xlsx` with SHA-256 `392a673eca46e63e36c410db94ee4b6e6ccf433f7ac6dfcd9f3a48e240afd452`.

The migration changed only the Events, Clusters, and Cluster Memberships worksheet XML payloads relative to the pre-migration snapshot. The workbook tables, sheet order and visibility, validation and conditional-formatting ranges, formulas, comments, other package members, and existing per-record cell style IDs were retained. Events remains table `A1:M1014` with Type and Status validation/formatting through row 1014. Cluster Memberships remains table `A1:G78`, with Severity validation and conditional formatting through `F2:F83`; its Severe rule uses the Legend color `FFD9D2E9`.

After the final workbook save, `python .tools/export_event_catalog_csv.py` succeeded. Parsed CSV records match the workbook exactly: Events 156 rows by 13 columns, Clusters 20 by 8, and Scenarios 17 by 6. Export hashes are:

- `chaos_redux_events_catalog.csv`: `a3e02ac5429eb7a94aadcad3257be3fbf1d9a424a69245f48c6c4b1b0fd785dc`
- `chaos_redux_clusters_catalog.csv`: `d780239bc9ab5cca5778e1192df5f8c8f77ad2cd63710038fcb62808704bb4c6`
- `chaos_redux_scenarios_catalog.csv`: `c2c421b1219356482ce1db3db80d84af87b032b1cf0945a8fe2e806c38ce3bb5`

The final audit found 155 unique Event IDs, unique names for all 19 migrated records, preserved Unavailable statuses, and slot-aligned cluster IDs and severities. No visual Excel application render or formula recalculation was needed; the workbook contains no formulas.
