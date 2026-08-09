# Event 12 continental focus MCP layout repair handoff

Date: 2026-08-09

## Scope and result

The retained layout repair changes only static `x`/`y` positions and conditional `offset` values in `common/national_focus/012_africa_continental_focus_tree.txt`.

The tree still contains 276 focuses, nine distinct six-focus regional overlays, seven constitutional route families, and the existing payoff/reward rows; no focus id, prerequisite, mutual exclusion, completion reward, AI block, route lock, or localisation key was removed or simplified.

Every overlay now has a unique static six-node lane so the MCP parser does not place all nine conditional branches on the same coordinates.

When its existing mutually exclusive `africa_regional_overlay` value is active, each overlay uses the original compact runtime pattern: root `(12,2)`, left/right branches `(8,3)` and `(16,3)`, second branches `(8,4)` and `(16,4)`, and capstone `(12,5)`.

## Changed focus identifiers

The six identifiers in each of the nine overlay families received only layout changes.

- Maghreb/Sahara: `africa_maghreb_sahara_face_divided_sovereignty`, `africa_maghreb_sahara_join_coast_and_caravan`, `africa_maghreb_sahara_prepare_the_first_guarantee`, `africa_maghreb_sahara_reconcile_port_and_interior`, `africa_maghreb_sahara_seat_the_desert_council`, `africa_maghreb_sahara_prove_a_northern_mandate`.
- West Atlantic: `africa_west_atlantic_a_mandate_from_ports_and_hinterlands`, `africa_west_atlantic_open_port_and_inland_route`, `africa_west_atlantic_protect_the_first_neighbour`, `africa_west_atlantic_make_export_wealth_public`, `africa_west_atlantic_seat_coasts_and_interior`, `africa_west_atlantic_prove_the_atlantic_mandate`.
- Sahel/Lake Chad: `africa_sahel_lake_chad_secure_food_and_water`, `africa_sahel_lake_chad_open_the_mobile_corridor`, `africa_sahel_lake_chad_guard_the_first_partner`, `africa_sahel_lake_chad_settle_pasture_and_market`, `africa_sahel_lake_chad_convene_the_lake_council`, `africa_sahel_lake_chad_prove_the_inland_mandate`.
- Nile/Horn: `africa_nile_horn_settle_river_and_highland_authority`, `africa_nile_horn_open_nile_and_red_sea_access`, `africa_nile_horn_answer_the_first_horn_obligation`, `africa_nile_horn_reconcile_court_civic_and_frontier`, `africa_nile_horn_convene_basin_and_horn_delegates`, `africa_nile_horn_prove_the_northeastern_mandate`.
- Congo Basin: `africa_congo_basin_transfer_authority_from_concessions`, `africa_congo_basin_open_the_river_rail_spine`, `africa_congo_basin_protect_the_first_basin_partner`, `africa_congo_basin_return_resource_revenue`, `africa_congo_basin_convene_regional_councils`, `africa_congo_basin_prove_the_river_mandate`.
- Great Lakes: `africa_great_lakes_settle_kingdom_and_civic_authority`, `africa_great_lakes_open_lake_and_rail_access`, `africa_great_lakes_protect_the_first_lake_partner`, `africa_great_lakes_share_land_and_producer_revenue`, `africa_great_lakes_convene_the_kingdom_council`, `africa_great_lakes_prove_the_lake_mandate`.
- Swahili/Indian Ocean: `africa_swahili_indian_ocean_settle_port_and_mainland_authority`, `africa_swahili_indian_ocean_open_the_maritime_corridor`, `africa_swahili_indian_ocean_guard_the_first_convoy_partner`, `africa_swahili_indian_ocean_write_common_customs`, `africa_swahili_indian_ocean_convene_coast_and_islands`, `africa_swahili_indian_ocean_prove_the_maritime_mandate`.
- Southern Africa: `africa_southern_africa_break_the_exclusionary_order`, `africa_southern_africa_secure_rail_port_and_mine`, `africa_southern_africa_guarantee_the_first_neighbour`, `africa_southern_africa_settle_land_and_labour`, `africa_southern_africa_convene_the_southern_council`, `africa_southern_africa_prove_the_reconstruction_mandate`.
- Madagascar/Islands: `africa_madagascar_islands_settle_island_authority`, `africa_madagascar_islands_open_the_convoy_network`, `africa_madagascar_islands_protect_the_first_island_partner`, `africa_madagascar_islands_join_highland_and_coast`, `africa_madagascar_islands_convene_the_islands_council`, `africa_madagascar_islands_prove_the_ocean_mandate`.

## MCP evidence

The baseline `hoi4.focus_inspect` used tree `africa_continental_focus_tree` in workspace `mod_chaos_redux_ea3b2d67c2c0` and reported 276 focuses with bounds `x=2..108`, `y=0..45`, 75 connector crossings, 53 connector/node intersections, and 36 long connectors.

Baseline inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9984c64af5957268cfe42d8985b9d5b7373a9b036dd4dfd9867706d6f736e3c6/124d83a9ddc412585804661740d07f899e7f5682af26f4ea900f29df2f75dd69/focus-inspect.643a57c732f99d16.json`.

The mandatory `hoi4.focus_rewrite` compact attempt was made against the same source and stopped with `FOCUS_LAYOUT_WORK_BUDGET_BLOCKED` during connector refinement after the fixed `80,000,000` placement/comparison work ceiling was exhausted; it did not write a file.

A bounded post-patch `hoi4.focus_inspect` completed with 276 focuses, bounds `x=-104..152`, `y=0..45`, no parent-above errors, and zero static overlay coordinate duplicates in the source proof below.

Post-patch inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e39dd428b069d61fad81fd2ab0060ea4d18b927f207feaf2e016ac44c078e7ad/df670d96f11384a2352b4e5757e7fb548e6b01fd0280c2acfbfc032bc1f61ffc/focus-inspect.9f49b7ccf9dd73d5.json`.

The resulting MCP warnings are connector-quality warnings rather than duplicate node placement: 58 crossings, 58 connector/node intersections, and 36 long connectors remain because nine preserved direct prerequisites fan out from `africa_identify_host_problem` and the rewrite route cannot refine this 276-focus graph within its work ceiling.

A subsequent narrow post-inspect detail route exceeded the 180-second bounded window and was interrupted; this is recorded as an MCP timeout blocker, and no additional long MCP call was started after that interruption.

The pre-patch `hoi4.focus_render` was run and returned the expected focus HTML/SVG/JSON artifacts.

Post-patch `hoi4.focus_render` was not rerun after the bounded timeout; this is an explicit validation gap rather than a claim of rendered post-change proof.

## Static source and route checks

The source graph check found 276 focus ids, zero duplicate ids, 54 overlay focus ids in nine groups, zero duplicate static overlay coordinates, and zero unresolved prerequisite references.

All seven constitutional route families remain present: federal, republic, crowns, union, command, confederation, and covenant.

The diff contains only layout coordinates and conditional offsets for the 54 identifiers listed above; completion rewards, the existing 78 payoff rows, prerequisites, route locks, AI weights, and localisation were not edited.

The nine offset triggers are the existing numeric `africa_focus_uses_*_overlay` checks in `common/scripted_triggers/012_africa_triggers.txt`, each keyed to a distinct `africa_overlay` constant, so only one overlay lane is intended to be visible for a host at a time.

## Assets, localisation, and AI

No icon, sprite, localisation, AI, reward, or gameplay wiring was changed.

The baseline MCP scan still reports the pre-existing 14 missing icon references and one missing localisation reference; they are outside this layout-only repair and remain for the parent audit.

No probability-bearing AI surface was changed, so the probability-auditor route was not required for this patch.

## Remaining risks and validation gaps

The static MCP view is intentionally wide because its parser ignores conditional offsets; runtime readability depends on the existing mutually exclusive regional overlay trigger and should be reviewed by the parent in the live consumer.

The post-patch render was skipped after the bounded MCP timeout, and the rewrite tool remains blocked by its fixed work ceiling.

No route content, reward, prerequisite, AI behavior, icon, or localisation simplification was made.
