# Event 012 overlay, host, and external focus AI repair handoff

Date: 2026-08-03

Status: bounded focus and AI patch complete; no gameplay fallback, route substitution, model work, or live HOI4 execution was used.

## Scope and source inputs

This handoff covers the accepted 78-row focus payoff matrix, the 22 full and 29 compact host playbooks, the continental focus tree, six external continental package trees, their focus strategy plans, source-level loading, localisation, icons, prerequisites, rewards, and AI modifiers.

Primary source files were `common/national_focus/012_africa_continental_focus_tree.txt`, `common/ai_strategy_plans/012_africa_focus_plans.txt`, `common/scripted_triggers/012_africa_focus_route_triggers.txt`, `common/scripted_triggers/012_africa_triggers.txt`, `common/scripted_effects/012_africa_world_order_effects.txt`, and the six `common/national_focus/012_africa_world_*_focus.txt` files.

## Changed files and identifiers

### Continental focus AI patch

Changed `common/national_focus/012_africa_continental_focus_tree.txt` only in regional-overlay `ai_will_do` blocks.

Before this patch, 45 of 54 regional-overlay nodes used only their flat `@africa_ai_elevated` or `@africa_ai_high` base factor; the nine mandate capstones had the generic overlay-pressure modifier but no explicit region predicate.

After this patch, all 54 overlay nodes retain their existing base factor and add `@africa_ai_preferred_multiplier` when the matching region predicate and the live `africa_focus_ai_overlay_pressure` receipt trigger are true.

The 54 changed focus IDs are:

| Overlay | Changed focus IDs |
| --- | --- |
| Maghreb and Sahara | `africa_maghreb_sahara_face_divided_sovereignty`, `africa_maghreb_sahara_join_coast_and_caravan`, `africa_maghreb_sahara_prepare_the_first_guarantee`, `africa_maghreb_sahara_reconcile_port_and_interior`, `africa_maghreb_sahara_seat_the_desert_council`, `africa_maghreb_sahara_prove_a_northern_mandate` |
| West Atlantic | `africa_west_atlantic_a_mandate_from_ports_and_hinterlands`, `africa_west_atlantic_open_port_and_inland_route`, `africa_west_atlantic_protect_the_first_neighbour`, `africa_west_atlantic_make_export_wealth_public`, `africa_west_atlantic_seat_coasts_and_interior`, `africa_west_atlantic_prove_the_atlantic_mandate` |
| Sahel and Lake Chad | `africa_sahel_lake_chad_secure_food_and_water`, `africa_sahel_lake_chad_open_the_mobile_corridor`, `africa_sahel_lake_chad_guard_the_first_partner`, `africa_sahel_lake_chad_settle_pasture_and_market`, `africa_sahel_lake_chad_convene_the_lake_council`, `africa_sahel_lake_chad_prove_the_inland_mandate` |
| Nile and Horn | `africa_nile_horn_settle_river_and_highland_authority`, `africa_nile_horn_open_nile_and_red_sea_access`, `africa_nile_horn_answer_the_first_horn_obligation`, `africa_nile_horn_reconcile_court_civic_and_frontier`, `africa_nile_horn_convene_basin_and_horn_delegates`, `africa_nile_horn_prove_the_northeastern_mandate` |
| Congo Basin | `africa_congo_basin_transfer_authority_from_concessions`, `africa_congo_basin_open_the_river_rail_spine`, `africa_congo_basin_protect_the_first_basin_partner`, `africa_congo_basin_return_resource_revenue`, `africa_congo_basin_convene_regional_councils`, `africa_congo_basin_prove_the_river_mandate` |
| Great Lakes | `africa_great_lakes_settle_kingdom_and_civic_authority`, `africa_great_lakes_open_lake_and_rail_access`, `africa_great_lakes_protect_the_first_lake_partner`, `africa_great_lakes_share_land_and_producer_revenue`, `africa_great_lakes_convene_the_kingdom_council`, `africa_great_lakes_prove_the_lake_mandate` |
| Swahili and Indian Ocean | `africa_swahili_indian_ocean_settle_port_and_mainland_authority`, `africa_swahili_indian_ocean_open_the_maritime_corridor`, `africa_swahili_indian_ocean_guard_the_first_convoy_partner`, `africa_swahili_indian_ocean_write_common_customs`, `africa_swahili_indian_ocean_convene_coast_and_islands`, `africa_swahili_indian_ocean_prove_the_maritime_mandate` |
| Southern Africa | `africa_southern_africa_break_the_exclusionary_order`, `africa_southern_africa_secure_rail_port_and_mine`, `africa_southern_africa_guarantee_the_first_neighbour`, `africa_southern_africa_settle_land_and_labour`, `africa_southern_africa_convene_the_southern_council`, `africa_southern_africa_prove_the_reconstruction_mandate` |
| Madagascar and Islands | `africa_madagascar_islands_settle_island_authority`, `africa_madagascar_islands_open_the_convoy_network`, `africa_madagascar_islands_protect_the_first_island_partner`, `africa_madagascar_islands_join_highland_and_coast`, `africa_madagascar_islands_convene_the_islands_council`, `africa_madagascar_islands_prove_the_ocean_mandate` |

The existing predicates are `africa_focus_uses_maghreb_sahara_overlay`, `africa_focus_uses_west_atlantic_overlay`, `africa_focus_uses_sahel_lake_chad_overlay`, `africa_focus_uses_nile_horn_overlay`, `africa_focus_uses_congo_basin_overlay`, `africa_focus_uses_great_lakes_overlay`, `africa_focus_uses_swahili_indian_ocean_overlay`, `africa_focus_uses_southern_africa_overlay`, and `africa_focus_uses_madagascar_islands_overlay` in `common/scripted_triggers/012_africa_triggers.txt:642-686`.

The live receipt helper remains `africa_focus_ai_overlay_pressure` in `common/scripted_triggers/012_africa_focus_route_triggers.txt:123-146`; no new trigger, flag, constant, icon, or localisation key was introduced.

### Documentation alignment

Updated `docs/events/012_africa/charter_autonomy_and_focus_ai.md` to document all 54 region-aware overlay nodes, the 22 full and 29 compact host coverage model, and the six external package loader and 32 route-plan counts.

## Route coverage table

| Surface | Source coverage | Result |
| --- | ---: | --- |
| Shared opening | 16 focuses | Present with opening ledger, corridor, proof, congress, and constitutional choice sequence. |
| Regional overlays | 9 x 6 = 54 focuses | Present; all nodes now use region-aware live overlay pressure. |
| Federal Union | 21 focuses | Present with route root, institutions, crises, recovery, and capstone. |
| Continental Republic | 21 focuses | Present with civic, election, executive, and regional acceptance sequence. |
| Council of Crowns | 21 focuses | Present with succession, arbitration, restoration, and Charter settlement. |
| People’s Union | 21 focuses | Present with coalition, food continuity, administration, and host-privilege outcomes. |
| Military Continentalism | 21 focuses | Present with command, emergency rule, civilian handover, and mandate proof. |
| Continental Confederation | 21 focuses | Present with voting, free-rider, lawful refusal, withdrawal, and capstone. |
| Hidden Covenant | 18 focuses | Present and reveal-gated; grounded-origin history remains visible by design. |
| Shared support | 36 focuses | Present with route-sensitive support effects and AI plan hooks. |
| Host, formation, and post-formation | 26 focuses | Present with four full signatures, two compact signatures, promotion, succession, and formation. |
| Main tree total | 276 focuses | Static source audit found no duplicate IDs or dangling focus references. |

External source trees and route-plan coverage are:

| Package | Focus source | Route plans | Loader evidence |
| --- | ---: | ---: | --- |
| Middle East | 20 | 5 | `africa_middle_east_world_focus_tree` loaded at `common/scripted_effects/012_africa_world_order_effects.txt:1963`. |
| Europe | 20 | 6 | `africa_europe_world_focus_tree` loaded at `:1976`. |
| Asia | 20 | 5 | `africa_asia_world_focus_tree` loaded at `:1988`. |
| North America | 20 | 5 | `africa_north_america_world_focus_tree` loaded at `:2000`. |
| South America | 21 | 6 | `africa_south_america_world_focus_tree` loaded at `:2013`. |
| Oceania | 20 | 5 | `africa_oceania_world_focus_tree` loaded at `:2025`. |

All six external source trees have complete focus references, prerequisites, mutual exclusions, AI blocks, rewards, icons, and title and description localisation. Their route plans use sponsorship, independent, rival, and alignment modifiers and contain no dangling focus references.

## Icon coverage table

| Surface | Icon coverage | Result |
| --- | ---: | --- |
| Continental tree | 13 registered family sprite IDs for 276 focuses | All refs resolve through `interface/012_africa.gfx` and the existing Event 012 DDS family. |
| Middle East | 20 source icon refs | Registered and visible in MCP source scan. |
| Europe | 20 source icon refs | Registered and visible in MCP source scan. |
| Asia | 20 source icon refs | Registered and visible in MCP source scan. |
| North America | 20 source icon refs | Registered and visible in MCP source scan. |
| South America | 21 source icon refs | Registered and visible in MCP source scan. |
| Oceania | 20 source icon refs | Registered and visible in MCP source scan. |

## Localisation, reward, and mismatch list

No localisation mismatch was found. The static audit resolved title and `_desc` keys for all 276 continental focuses and all 121 external package focuses in the Event 012 English localisation sources.

No reward mismatch was found. Every continental and external focus has a `completion_reward` block, and no focus ID was missing a reward or an AI block.

The accepted payoff matrix remains the source of truth for gameplay payoff wording. The external-package readiness row remains gated by `africa_world_package_implementation_ready` as documented in the acceptance ledger; that gate is not a focus source defect and was not bypassed.

## AI behavior gaps and remaining risks

The 22 full host plans are present in `common/ai_strategy_plans/012_africa_focus_plans.txt:653-1910` and use exact `africa_host_playbook` constants. The Somali Territories plan is named `africa_host_somali_specific_focus_plan` but correctly checks `constant:africa_host_playbook.somali_territories` at `:1707`, so it is not a missing profile.

All 29 compact playbooks use the shared `africa_focus_ai_compact_host_pressure` trigger on the two compact signature nodes; they intentionally do not receive 29 duplicated strategy-plan blocks.

The six external package trees have 32 route plans at `common/ai_strategy_plans/012_africa_focus_plans.txt:1938-4157` with no dangling focus references. Their base focus factors remain static within each tree, while route plans add package-state and sponsorship-aware weighting as designed.

The remaining MCP layout diagnostics are known static-graph findings rather than missing AI or source wiring. The inspector reports 570 blocking diagnostics for the main tree because nine mutually exclusive overlay branches share six authored coordinate bands; the branch-insensitive inspector reports them as duplicate coordinates and visible overlaps. The prior branch-safety handoff records the vanilla Congo precedent and the required runtime branch checks.

The six external inspectors also include unrelated vanilla continuous-focus icon diagnostics in their bounded inline output. Their Event 012 source trees themselves reported complete focus counts and no missing Event 012 icon, localisation, reward, or prerequisite reference.

Skipped validation is limited to live HOI4 execution and branch-aware campaign replay because the parent explicitly deferred live validation. Models and asset production were outside this focus scope.

## MCP artifacts and validation

Final continental inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9f318f4a98b6b3d4dde0850df4991e3f37d3c5ff5577f530d61531c405f04a5e/949830ff3ffa0ba908ed7bb7eed919a1b2d250125bf64e015cf94d7978971a8e/focus-inspect.40c7fea981a6a6d0.json`.

Final continental render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/96d1ce4f644ab63c6c2c73c8647b7a58e758eb3ae3b6733178cabeba9d7477ae/08b3fb0821558a45a9cf688d19a50e45fe775d3abd8579398d82811a6aaf97f9/africa_continental_focus_tree.focus.html`.

The six external focus inspections returned `FOCUS_INSPECTED` with focus counts 20, 20, 20, 20, 21, and 20 for Asia, Europe, Middle East, North America, South America, and Oceania respectively. The six external renders returned `FOCUS_RENDERED`; their artifacts are recorded in the MCP run output and can be regenerated from the same workspace and source paths.

Meaningful source validation completed after the patch included focus ID uniqueness and dangling-reference checks, title and description key coverage, icon, reward, and AI block coverage, overlay helper coverage, host-plan count comparison against the 22/29 matrix split, external loader and route-plan cross-checks, and MCP inspect/render.

## Parent follow-up

Keep the existing shared coordinate bands and readiness gate unchanged. The next meaningful confidence step is branch-aware runtime review for one mapped host per overlay, one host per grounded constitution, Covenant reveal, compact promotion, and host succession; no source fallback is required by this handoff.
