# Identifier Overlap Audit

This is the read-only pre-allocation snapshot.
Current assignments and the repairs to its confirmed collisions are in the [shared identifier registry](../../../../specs/shared_identifier_registry.md).

## Scope read

- Parent task: audit cross-package identifier collisions and recommend safe assignments for cluster IDs, country tags, event namespaces and roots, world-end registry IDs, and expressly assigned global helpers or asset IDs.
- Explicit constraints: read-only repository exploration except this requested report and JSON; preserve implemented numeric IDs; SCN occupancy belongs to the separate scenario auditor; do not patch source, specs, workbooks, or assets.
- Baseline: 102 package directories and 3,141 files under C:/Users/klimp/AppData/Local/Temp/chaos-redux-specs-audit-yijvocg9/before/docs/specs.
- Current comparison: 103 package directories and 3,141 files under docs/specs. The only added package is the empty chaos_redux_3d_model_workflow_planning_package, which contributes no identifier assignment.
- Skills and guidance read: AGENTS.md, .agents/skills/chaos-redux-subagents/SKILL.md, .agents/skills/chaos-redux-events/SKILL.md, and .agents/skills/xlsx/SKILL.md. The workbook was opened read-only to verify the current Clusters sheet.

## Primary findings

The confirmed package-level cluster collisions are provisional ID 9 claims. The live runtime and current workbook both assign ID 9 to National Breakthroughs. The current workbook already assigns Randomizations ID 14, Sudden Abundance ID 15, and Intelligence ID 20, so Event 065 should use 14, Event 066 should use 15, and the Event 039 and Event 097 Intelligence memberships should use 20.

The cluster registry has a larger unresolved catalog/runtime mismatch. Current runtime constants retain Diseases at ID 8, National Breakthroughs at 9, Random Stuff at 12, and Intelligence at 20. The current workbook instead has no ID 8 row, labels ID 12 Pacts, moves Diseases to 13, moves Random Stuff to 19, and keeps Intelligence at 20. A separate implementation-facing document proposes an unaccepted v2 remapping in which Intelligence is 8 and Scientific Research is 9. Its own source-of-truth section says the candidate contract lacks an attributable acceptance record, and its stated source CSV was absent.

To preserve live identities, retain runtime IDs 8, 9, 12, and 20. Reconcile the workbook so Diseases is 8 and Random Stuff is 12, then assign new Pacts to 13. Keep the workbook's existing reservations Randomizations 14, Sudden Abundance 15, Domestic Unrest 16, Alien Invasions 17, and Military Preparation 18. Do not treat the v2 proposal's new meanings for IDs 8, 9, 12, or 19 as live assignments without an accepted migration.

Scientific Research is a separate cluster proposal in Event 054, not the current runtime National Breakthroughs cluster. If it remains a distinct accepted cluster, ID 21 is the first safe append-only reservation above the current workbook maximum of 20. Event 031's future Internal Fracture proposal also uses the invalid ID 9; if that distinct future cluster remains accepted after the Scientific Research decision, reserve 22. Event 031 is already listed in the current workbook under Domestic Unrest ID 16, so the parent should resolve whether Internal Fracture is a separate membership or a stale duplicate proposal before allocating it.

Event 043 proposes world-end ID 15 for Cthulhu, but ID 15 is already the live Global Jihad world-end identity owned by Event 031. The world-end registry currently ends at ID 16, World of Anarchy for Event 039. No world-end ID 17 reservation appeared in the bounded specs/plans scan, so Cthulhu can use world-end ID 17. Numeric ID 17 in the separate triggerable-scenario registry is not a world-end collision. SCN-015 remains with the assigned scenario auditor.

Event 043 says it has no cluster, while Event 046 proposes Event 043 as a Severe member of Alien Invasions. The canonical workbook currently lists Alien Invasions at cluster ID 17 with Event 043 as Severe. This is a membership/design conflict, not an identifier collision; Event 046's note that the supplied export had no Alien Invasions row is stale against the current workbook.

The runtime event definition scan found one competing definition ID: chaosx.nr18.90 is defined twice with different meanings in events/018_random_resource.txt. Keep the quarter-continent notice at .90 and move only the No Ground for a Survey rejection to the unreferenced local Event 018 sub-ID chaosx.nr18.33. Its caller and three localisation keys are listed below.

The duplicate planning root 012 is already documented as provenance rather than a second runtime event. docs/specs/012_africa_is_one_gods_of_africa_specs/README.md explicitly marks that package superseded by docs/specs/012_africa_specs/ and docs/events/012_africa/gods_of_africa.md. Multiple Event 012 source files intentionally use the single chaosx.nr12 namespace. Event 097 is also not a duplicate runtime assignment: events/097_collaboration.txt owns chaosx.nr97.1. Its current README records two conflicting design variants and leaves their merge unresolved, so no second event root should be allocated.

The mod country-tag source scan found 171 definitions with 171 unique keys and no duplicate tag definitions. DTH and KRG are already registered runtime tags, while current Event 010 and Event 016 specification text still calls them proposed or requires a final collision check; those are stale reservation notes, not free-tag candidates.

No competing exact assignments were found for shared helper, sprite, or entity identifiers in the targeted package search. There is no central proposal ledger that permits an exhaustive global proof for those identifier families, so this finding is bounded to explicit assignments recovered from the specification packages and their named registries.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| common/script_constants/event_cluster_constants.txt | Live cluster ID authority that must be preserved. | Lines 15-31 assign Diseases=8, National Breakthroughs=9, Negative Economy=10, Various Anomalies=11, Random Stuff=12, and Intelligence=20. |
| docs/spreadsheets/chaos_redux_events_catalog.xlsx | Canonical editable catalog source; read-only Clusters sheet inspection. | Current rows assign ID 9 National Breakthroughs, 12 Pacts, 13 Diseases, 14 Randomizations, 15 Sudden Abundance, 16 Domestic Unrest, 17 Alien Invasions, 18 Military Preparation, 19 Random Stuff, and 20 Intelligence; there is no row 8. |
| docs/systems/event_system/event_clusters.md | Candidate v2 mapping that conflicts with live source and the current workbook. | Lines 11 and 20-22 mark a candidate contract and an absent historical CSV; lines 259-275 describe a semantic-ID migration; rows 347-350 and 408-414 map Intelligence=8 and Scientific Research=9. Acceptance remains pending. |
| docs/specs/065_random_trait_specs/specs/065_random_trait_spec_part_4_cluster_chaos_and_persistence.md | Event 065's stale Randomizations reservation. | Lines 31-35 say the supplied CSV leaves 9 open and propose event_cluster_id.randomizations=9. Use the current workbook reservation 14. |
| docs/specs/066_abundance_specs/specs/066_abundance_spec_part_5_evolutions_and_cluster.md | Event 066's stale Sudden Abundance reservation. | Line 127 calls ID 9 the first unused export ID. Use the current workbook reservation 15. |
| docs/specs/039_murder_mystery_specs/manifest.json | Stale Intelligence cluster proposal. | Lines 37-41 reserve planning value 9; the current workbook and runtime use 20. |
| docs/specs/097_collaboration_specs/README.md | Provenance conflict, not a duplicate event root. | Current README records two authored variants and states their conflicting requirements remain unresolved; it also identifies conflicting achievement-ID families. |
| docs/specs/031_random_terror_specs/031_random_terror_manifest.json | Invalid future cluster proposal. | Line 12 proposes Internal Fracture cluster ID 9; current ID 9 is National Breakthroughs and the workbook already includes Event 31 in Domestic Unrest ID 16. |
| docs/specs/027_doctrine_research_specs/027_doctrine_research_catalog_cluster_handoff.md | Shows the current Event 027 handoff is National Breakthroughs, despite older provisional-ID wording elsewhere in that package. | Lines 1, 51, 63, and 70 name National Breakthroughs; the current runtime/workbook ID is 9. |
| docs/specs/054_gift_from_scientists_specs/specs/054_gift_from_scientists_spec_part_5_connections_and_cluster.md | Separate Scientific Research cluster proposal. | Lines 93-97 define a Scientific Research identity and provisionally claim ID 9; if distinct and accepted, allocate a new ID rather than reuse 9. |
| common/script_constants/world_end_scenario_registry_constants.txt | Live world-end numeric registry. | Lines 11-36 include Global Jihad=15 for Event 031 and World of Anarchy=16 for Event 039; ID 17 is not assigned. |
| docs/specs/043_monsters_from_the_deep_specs/specs/043_monsters_from_the_deep_spec_part_7_evolutions_pacts_and_terminal.md | Cthulhu world-end assignment candidate. | Line 410 proposes world-end scenario ID 15, already owned by Global Jihad. |
| docs/specs/043_monsters_from_the_deep_specs/research/043_source_review_log.md | Stale world-end occupancy evidence. | Line 130 says 14 was the latest observed world-end ID; current runtime has IDs 15 and 16. |
| docs/specs/043_monsters_from_the_deep_specs/prompts/043_monsters_from_the_deep_goal_prompt.md | Event 043 cluster design position and SCN boundary. | Line 7 says no cluster and proposes world-end 15; SCN-015 belongs to the other auditor. |
| docs/specs/046_the_great_shuffle_specs/specs/046_the_great_shuffle_spec_part_6_chaos_clusters_and_catalog.md | Explicit cross-package cluster membership conflict. | Lines 212-228 state Event 046 proposes Severe Alien Invasions membership, Event 043 says no cluster, and acceptance is unresolved. The note that the supplied export lacks Alien Invasions is stale against the current workbook. |
| events/018_random_resource.txt | Current duplicate event definition. | Lines 18-24 define No Ground for a Survey as chaosx.nr18.90; lines 3166-3176 define A Quarter of the Continent with the same ID. |
| common/scripted_effects/018_resources_found_prefire_effects.txt | Survey rejection caller. | Line 166 dispatches chaosx.nr18.90. |
| common/scripted_effects/018_resources_found_cave_effects.txt | Quarter milestone caller that should keep .90. | Line 1928 dispatches chaosx.nr18.90 after the configured delay. |
| localisation/english/018_random_resource_l_english.yml | Competing .90 presentation keys. | Lines 14-16 contain survey-failure title, description, and option; lines 593-596 contain the quarter-continent title, description, option, and tooltip. |
| docs/events/018_resources_found/overview.md | Player-independent implementation documentation for the survey failure. | Line 58 documents the rejection as chaosx.nr18.90 and should follow the new sub-ID if the parent applies the repair. |
| common/country_tags/chaosx_countries.txt and common/country_tags/016_brilliant_scientist_country.txt | Runtime tag occupancy evidence. | DTH is registered at line 5 of the first file; KRG is registered at line 8 of the second. |
| docs/testing/runtime_repairs/20260913_cxt_history_followup/standalone_technology_viewer_package_check.json | Separate viewer check, distinct from exposed technology MCP routes. | The installed hoi4-agent-tools package check reports standalone_viewer_in_package=false and says independent external viewer installations were not inventoried. |

## Existing patterns and allocation convention

The numeric cluster namespace is event_cluster_id, not the member-row namespace. Existing runtime values are save-facing and the parent instruction explicitly requires preserving them. Cluster rows in the XLSX are catalog reservations, while source constants and event_cluster initialization effects prove which IDs are currently implemented. When these disagree, record the conflict and align the catalog or accept a documented migration before wiring new rows.

The candidate v2 event-cluster document is not a current accepted registry. Its own authority section points to a source contract candidate pending acceptance, and says its historical CSV was absent. Do not treat its ID 8 through 19 remapping as implementation evidence.

The world-end numeric namespace is world_end_scenario_id. Its owner-event and super-event maps are separate fields, and the triggerable-scenario SCN namespace is separate again. The same integer can be valid in those different namespaces without collision.

Entry event roots follow chaosx.nr<ID>.1. Support files for one event intentionally share its namespace. Event 12's multiple source files and the current Event 97 root therefore do not create duplicate event assignments by themselves.

## Recommended allocation map

| Namespace | Existing reservation or competing claim | Recommended resolution |
| --- | --- | --- |
| event_cluster_id 9 | Runtime and current XLSX assign National Breakthroughs. Provisional claims include Randomizations (065), Sudden Abundance (066), Intelligence (039), Scientific Research (054 and candidate v2 docs), and future Internal Fracture (031). | Keep 9 for the existing National Breakthroughs identity. Set 065 to 14, 066 to 15, and Intelligence members 039/097 to 20. If Scientific Research is accepted as distinct, use 21. If Internal Fracture is also accepted as distinct after that, use 22. |
| event_cluster_id 12, 13, and 19 | Runtime assigns Random Stuff=12 and Diseases=8. The workbook assigns Pacts=12, Diseases=13, and Random Stuff=19. | Preserve runtime meanings: reconcile workbook Diseases to 8 and Random Stuff to 12, then assign the new Pacts row to 13. Do not create duplicate Diseases or Random Stuff clusters at 13 or 19. |
| event_cluster_id 14 and 15 | Current workbook already reserves Randomizations=14 and Sudden Abundance=15; no runtime constants exist yet. | Use 14 for Event 065 and 15 for Event 066. These are package-aligned catalog reservations, not free IDs to repurpose. |
| event_cluster_id 20 | Runtime and workbook both assign Intelligence=20. | Use 20 for Events 039 and 097; update their stale/unresolved ID notes. |
| world_end_scenario_id 15 | Global Jihad, owner Event 031. | Reject Event 043's Cthulhu ID 15. |
| world_end_scenario_id 17 | No current world-end source or planned world-end reservation found; runtime max is 16. Triggerable scenario ID 17 is a separate namespace. | Assign Cthulhu world-end ID 17. SCN-015 is separately audited. |
| Event 018 sub-ID 90 | Two current event definitions and two sets of conflicting localization keys use .90. | Keep Quarter of the Continent at .90. Move only No Ground for a Survey to .33 and update its prefire caller, three localization keys, and overview. |

The suggested future cluster values 21 and 22 are conditional on parent acceptance of distinct Scientific Research and Internal Fracture clusters. A repository-wide exact cluster-ID search found no 21 or 22 reservation in current source, specs, plans, or workbook; event number 21 in names such as Event 021 is a different namespace.

## Likely edit order for the parent

1. Record whether the parent will preserve current live cluster numeric IDs. If yes, update the canonical workbook rows for Diseases, Random Stuff, and Pacts to the recommended values; regenerate CSV exports only through the repository exporter after the XLSX write.
2. Update package claims 065=14, 066=15, and Intelligence=20 in 039/097; retain National Breakthroughs=9 in 027. Mark the old source snapshots in 065, 066, 039, 047, 063, and related handoffs as historical or superseded where they still say the ID is absent or free.
3. Resolve whether Scientific Research and Internal Fracture are distinct accepted clusters before allocating 21/22 or changing member arrays. Keep the Event 043/046 Alien Invasions membership conflict separate from numeric allocation.
4. Change Event 043's world-end proposal from occupied ID 15 to 17 and update the stale source-review maximum. Leave SCN-015 to its assigned auditor.
5. If the parent applies the minimal Event 018 fix, preserve the quarter notification at .90 and move the survey failure to .33 across the definition, caller, localization, and overview in one source/documentation pass.
6. Treat 012's standalone Gods package as superseded provenance and reconcile 097's two accepted-by-parent design variants without allocating a second event root.

## Validation checks

- Re-read the Clusters sheet from docs/spreadsheets/chaos_redux_events_catalog.xlsx after any workbook update, then run python .tools/export_event_catalog_csv.py and check that the generated cluster IDs match the accepted runtime registry.
- Confirm cluster IDs are unique by semantic cluster identity across event_cluster_id, cluster initialization, membership lookup, workbook rows, docs/events, and accepted specs. Do not count event member row IDs or SCN IDs as cluster IDs.
- Search the world-end owner and scenario constants after reserving Event 043 ID 17 and verify that the separate triggerable-scenario ID 17 remains in its own registry.
- For the Event 018 repair, search all repository text for chaosx.nr18.90 and chaosx.nr18.33, verify only the quarter milestone still uses .90, and inspect both event blocks and all four .90/.33 localization keys.
- Run a duplicate top-level event-definition scan after the Event 018 change; the current read-only scan found 1,669 top-level namespaced event definitions, 1,668 unique IDs, and only chaosx.nr18.90 duplicated.
- Re-run the current custom-tag uniqueness scan after any tag change; the current common/country_tags sources have 171 definitions with 171 unique keys.
- Use the required event inspect and render evidence for any event-source change. The current MCP calls did not return usable artifacts, so this source map is not a substitute for that evidence.

## Risks and blockers

### Confirmed collisions

- Cluster ID 9 is already National Breakthroughs in both runtime and current workbook; the stale 065, 066, and 039 claims must not be implemented.
- Workbook ID 12 Pacts conflicts with live Random Stuff ID 12; workbook ID 13 Diseases duplicates live Diseases ID 8; workbook ID 19 Random Stuff duplicates the same live identity at 12.
- World-end ID 15 is already Global Jihad, Event 031.
- Event 018 defines two different events as chaosx.nr18.90 and reuses the same three localization keys for two unrelated meanings.

### Unresolved design or provenance

- The candidate v2 cluster mapping is unaccepted and conflicts with both current workbook and current runtime IDs. A migration acceptance record is missing.
- Event 043 says no cluster while Event 046 proposes Severe Alien Invasions membership; the current workbook includes Event 043 in cluster 17, but the design conflict remains.
- Event 097's package README records two incompatible design variants. Its stable event root remains chaosx.nr97.1, but the package's achievement and cluster integration IDs should not be finalized until the variants are reconciled.
- The second 012 package is explicitly superseded historical planning material; the main Event 012 package remains the source of truth.
- A complete shared-helper/sprite/entity reservation registry was not found, so uniqueness for those identifiers cannot be certified beyond the explicit package assignments and current targeted search.

### Required MCP route blocker

The exposed HOI4 Agent Tools event routes were attempted. A full event_inspect scan with refresh=true returned status error, blocker code INTERNAL_ERROR, message Unexpected internal error, and no artifacts or diagnostics. Targeted event_inspect roots calls for chaosx.nr12.1 and chaosx.nr18.90 remained pending through repeated waits and were canceled without a result. No event_render artifact URI was returned because the inspect calls did not complete. Tool exposure does not establish service health, and no source-only event map should be presented as equivalent engine evidence.

The installed hoi4-agent-tools package check separately reports no standalone Technology Tree Viewer UI entrypoint. Independent viewer installations outside that package were not inventoried. Read-only tech_inspect, tech_render, and tech_compare routes are exposed, but no technology surface was part of this identifier map.

## Recommended next action

Have the parent record an explicit cluster registry decision that preserves live IDs 8, 9, 12, and 20, align the canonical workbook and affected package notes to it, reserve world-end ID 17 for Event 043, and keep Event 043/046 membership unresolved until its design owner chooses whether Event 043 joins Alien Invasions.

No gameplay, localisation, registry, workbook, asset, or existing documentation source was edited in this audit.
